#!/usr/bin/env python3
"""Collect small, trusted health reports and reuse the existing operations mailer."""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
from pathlib import Path
import re
import urllib.error
import urllib.parse
import urllib.request
import zipfile

from provider_health_monitor import MAX_BYTES, NoRedirect, utc_now, validate_report
from send_portal_ops_alert import send_alert

WORKFLOW = '.github/workflows/provider-api-health.yml'
ARTIFACT = 'provider-health-report'
LABELS = {
    'healthy': '正常', 'low_balance': '余额低于预警阈值',
    'exhausted': '可用付费余额不足', 'invalid_key': 'API Key 被拒绝或已停用',
    'expired_key': 'API Key 已过期', 'expiring_key': 'API Key 将在14天内到期',
    'permission_denied': 'API Key 权限不足', 'rate_limited': '服务限流',
    'service_unavailable': '供应商服务暂时不可用', 'transport_error': '供应商连接未成功',
    'malformed_response': '供应商响应格式异常', 'missing_key': '尚未配置此密钥槽位',
    'account_disabled': '供应商账户未启用', 'payment_required': '供应商要求充值或检查付费权限',
    'report_unavailable': '健康报告未取得或已过期，请检查监测任务',
}
CRITICAL = {'exhausted', 'invalid_key', 'expired_key', 'missing_key', 'account_disabled', 'payment_required'}


class ReportUnavailable(Exception):
    pass


class GitHubReader:
    def __init__(self, token):
        self.token = token

    def request(self, path, *, archive=False):
        if not self.token:
            raise ReportUnavailable('github_reader_not_configured')
        request = urllib.request.Request('https://api.github.com/' + path, headers={
            'Authorization': f'Bearer {self.token}', 'Accept': 'application/vnd.github+json',
            'X-GitHub-Api-Version': '2022-11-28', 'User-Agent': 'provider-health-mail/1',
        })
        try:
            response = urllib.request.build_opener(NoRedirect()).open(request, timeout=25)
        except urllib.error.HTTPError as error:
            location = error.headers.get('Location', '')
            code = error.code
            error.close()
            if not archive or code != 302:
                raise ReportUnavailable(f'github_http_{code}') from None
            parsed = urllib.parse.urlparse(location)
            allowed = ('blob.core.windows.net', 'githubusercontent.com', 'amazonaws.com')
            if parsed.scheme != 'https' or parsed.username or parsed.password or not any(
                parsed.hostname == host or (parsed.hostname or '').endswith('.' + host) for host in allowed
            ):
                raise ReportUnavailable('unexpected_artifact_host')
            # Signed object-storage redirects never receive the GitHub token.
            response = urllib.request.build_opener(NoRedirect()).open(location, timeout=25)
        with response:
            bound = 65536 if archive else 1024 * 1024
            raw = response.read(bound + 1)
            if len(raw) > bound:
                raise ReportUnavailable('github_response_too_large')
            return raw if archive else json.loads(raw)


def read_consumer(repo, reader, now):
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repo):
        raise ValueError('Invalid consumer repository')
    base = f'repos/{repo}'
    meta = reader.request(base)
    branch = meta['default_branch']
    query = urllib.parse.urlencode({'branch': branch, 'status': 'completed', 'per_page': 10})
    runs = reader.request(f'{base}/actions/workflows/provider-api-health.yml/runs?{query}')['workflow_runs']
    eligible = [run for run in runs if run.get('event') in {'schedule', 'workflow_dispatch', 'workflow_run'}
                and run.get('head_branch') == branch and run.get('path') == WORKFLOW
                and (run.get('head_repository') or {}).get('full_name') == repo]
    if not eligible:
        raise ReportUnavailable('no_default_branch_health_run')
    run = max(eligible, key=lambda item: item['id'])
    if run.get('status') != 'completed' or run.get('conclusion') != 'success':
        raise ReportUnavailable('latest_health_run_failed')
    artifacts = reader.request(f'{base}/actions/runs/{run["id"]}/artifacts?per_page=100')
    if artifacts.get('total_count') != len(artifacts.get('artifacts', [])):
        raise ReportUnavailable('incomplete_artifact_inventory')
    candidates = [a for a in artifacts['artifacts'] if a.get('name') == ARTIFACT and not a.get('expired')]
    if len(candidates) != 1 or not 0 < candidates[0].get('size_in_bytes', 0) <= 65536:
        raise ReportUnavailable('health_artifact_missing_or_oversized')
    raw = reader.request(f'{base}/actions/artifacts/{candidates[0]["id"]}/zip', archive=True)
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        entries = archive.infolist()
        if len(entries) != 1 or entries[0].filename != 'provider-health-report.json' or not 0 < entries[0].file_size <= MAX_BYTES:
            raise ReportUnavailable('unexpected_health_archive')
        report = json.loads(archive.read(entries[0]))
    validate_report(report, now=now, repository=repo, run_id=run['id'],
                    run_attempt=run['run_attempt'], commit=run['head_sha'], workflow=WORKFLOW)
    identities = {(row['provider'], row['slot']) for row in report['checks']}
    if identities != {('tikhub', 'TIKHUB_API_KEY'), ('deepseek', 'DEEPSEEK_API_KEY')}:
        raise ReportUnavailable('consumer_slots_differ')
    return report


def incident_groups(reports):
    groups = []
    for report in reports:
        for provider in sorted({row['provider'] for row in report['checks']}):
            checks = [row for row in report['checks'] if row['provider'] == provider and row['status'] != 'healthy']
            if not checks:
                continue
            # No amounts, timestamps, or run IDs in the dedupe fingerprint.
            signature = [(row['slot'], row['signals']) for row in sorted(checks, key=lambda row: row['slot'])]
            digest = hashlib.sha256(json.dumps(signature, sort_keys=True).encode()).hexdigest()[:24]
            groups.append({'report': report, 'provider': provider, 'checks': checks,
                           'dedupe_key': f'provider-health:{report["repository"]}:{provider}:{digest}'})
    return groups


def send_groups(reports, *, worker, signing_key, mailer=send_alert):
    results = []
    for group in incident_groups(reports):
        report, provider, checks = group['report'], group['provider'], group['checks']
        severity = 'critical' if any(s in CRITICAL for row in checks for s in row['signals']) else 'warning'
        subject = f'API 服务提醒 | {report["repository"]} | {provider}'
        lines = [f'项目：{report["repository"]}', f'检查时间（UTC）：{report["checked_at"]}', '']
        record_url = (f'https://github.com/{report["repository"]}/actions/runs/{report["run_id"]}'
                      if report.get('run_id') else
                      f'https://github.com/{report["repository"]}/actions/workflows/provider-api-health.yml')
        for row in checks:
            lines.append(f'{row["slot"]}：' + '；'.join(LABELS[s] for s in row['signals']))
        lines += ['', '默认余额预警：TikHub 付费余额 ≤ 5 USD；DeepSeek ≤ 20 CNY / 5 USD（仓库变量可调整）。',
                  'TikHub 免费额度可能不适用于低粉爆款使用的付费接口；空付费余额仍需处理。',
                  '请在对应供应商后台充值或更新原仓库的 API Key。限流、连接异常不等于密钥失效。',
                  '此次只查询账户状态，没有发起内容生成或媒体采集。',
                  f'检查记录：{record_url}',
                  '相同问题24小时内去重；问题升级会单独通知。']
        result = mailer(worker_base_url=worker, signing_key=signing_key, subject=subject,
                        text='\n'.join(lines), dedupe_key=group['dedupe_key'], severity=severity,
                        dedupe_hours=24, attempts=1)
        results.append({'repository': report['repository'], 'provider': provider,
                        'sent': result.get('sent') is True, 'deduplicated': result.get('deduplicated') is True})
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--local-report', type=Path, required=True)
    parser.add_argument('--consumer', action='append', default=[])
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    now = utc_now()
    local = json.loads(args.local_report.read_text())
    validate_report(local, now=now, repository=os.environ['GITHUB_REPOSITORY'],
                    run_id=os.environ['GITHUB_RUN_ID'], run_attempt=int(os.environ['GITHUB_RUN_ATTEMPT']),
                    commit=os.environ['GITHUB_SHA'], workflow=WORKFLOW)
    reports, unavailable = [local], []
    reader = GitHubReader(os.environ.get('PROVIDER_HEALTH_READ_TOKEN', ''))
    for repo in args.consumer:
        try:
            reports.append(read_consumer(repo, reader, now))
        except (ReportUnavailable, urllib.error.URLError, OSError, ValueError, KeyError, TypeError, zipfile.BadZipFile):
            unavailable.append(repo)
            reports.append({'repository': repo, 'run_id': '',
                            'checked_at': now.isoformat(), 'checks': [{
                                'provider': 'monitor', 'slot': 'PROVIDER_HEALTH_REPORT',
                                'status': 'report_unavailable', 'signals': ['report_unavailable']} ]})
    results = [] if args.dry_run else send_groups(reports,
        worker=os.environ.get('PORTAL_WORKER_URL', ''), signing_key=os.environ.get('OPS_ALERT_SIGNING_KEY', ''))
    summary = {'schema_version': 1, 'reports': len(reports), 'issues': len(incident_groups(reports)),
               'consumer_report_unavailable': unavailable, 'emails': results, 'dry_run': args.dry_run}
    args.output.write_text(json.dumps(summary, sort_keys=True, indent=2) + '\n')
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except Exception:
        print('Provider health notification did not complete; inspect sanitized workflow steps.')
        raise SystemExit(1)
