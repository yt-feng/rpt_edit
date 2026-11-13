"""Real, temporary bare-Git races for generated-output publication; no network."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest


SCRIPT = Path(__file__).resolve().with_name('commit_output_dir.sh')
REAL_GIT = shutil.which('git')


class OutputCommitTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix='output-git-fixture-')
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.remote, self.producer, self.concurrent = (self.root/name for name in ('remote.git','producer','concurrent'))
        self.env = {**os.environ, 'GIT_CONFIG_GLOBAL':os.devnull, 'GIT_CONFIG_NOSYSTEM':'1', 'GIT_OPTIONAL_LOCKS':'0'}
        self.git('init','--bare','-q',str(self.remote))
        self.git('init','-q','-b','main',str(self.producer))
        self.git('config','user.name','Fixture', cwd=self.producer)
        self.git('config','user.email','fixture@example.invalid', cwd=self.producer)
        self.write(self.producer, 'output/existing.txt', 'first\nmiddle\nlast\n')
        self.write(self.producer, 'output/prune.txt', 'explicit deletion\n')
        self.write(self.producer, 'outside.txt', 'outside base\n')
        self.write(self.producer, '.gitignore', 'ignored/\n')
        self.git('add','.',cwd=self.producer); self.git('commit','-q','-m','Seed',cwd=self.producer)
        self.git('remote','add','origin',str(self.remote),cwd=self.producer)
        self.git('push','-q','origin','HEAD:main',cwd=self.producer)
        self.git('clone','-q','--branch','main',str(self.remote),str(self.concurrent))
        self.git('config','user.name','Concurrent',cwd=self.concurrent)
        self.git('config','user.email','concurrent@example.invalid',cwd=self.concurrent)
        self.wrapper = self.root/'bin'; self.wrapper.mkdir()
        wrapper = self.wrapper/'git'
        wrapper.write_text('#!'+sys.executable+'\n'+'''import json, os, pathlib, subprocess, sys
args=sys.argv[1:]
real=os.environ['FIXTURE_REAL_GIT']
state=pathlib.Path(os.environ['FIXTURE_STATE'])
counts=json.loads(state.read_text()) if state.exists() else {}
if args and args[0] in ('fetch','push'):
    counts[args[0]]=counts.get(args[0],0)+1
    state.write_text(json.dumps(counts))
mode=os.environ.get('FIXTURE_MODE','')
if args and args[0]=='fetch' and mode=='fetch-fails': sys.exit(1)
if args and args[0]=='push':
    if mode=='push-fails': sys.exit(1)
    if mode=='accepted-ack-lost' and counts['push']==1:
        subprocess.run([real,*args],check=True)
        sys.exit(1)
    if mode=='race' and counts['push']==1:
        other=pathlib.Path(os.environ['FIXTURE_CONCURRENT'])
        (other/'output/B.txt').write_text('concurrent B during push\\n')
        subprocess.run([real,'add','output'],cwd=other,check=True)
        subprocess.run([real,'commit','-q','-m','Racing B'],cwd=other,check=True)
        subprocess.run([real,'push','-q','origin','HEAD:main'],cwd=other,check=True)
        pathlib.Path('output/A.txt').write_text('changed after frozen intent\\n')
os.execv(real,[real,*args])
''')
        wrapper.chmod(0o755)
        sleep = self.wrapper/'sleep'
        sleep.write_text('#!/bin/sh\nexit 0\n'); sleep.chmod(0o755)
        self.env.update(PATH=str(self.wrapper)+os.pathsep+os.environ['PATH'], FIXTURE_REAL_GIT=REAL_GIT,
            FIXTURE_STATE=str(self.root/'calls.json'), FIXTURE_CONCURRENT=str(self.concurrent),
            GITHUB_ACTIONS='true',GITHUB_REPOSITORY='fixture/repo',GITHUB_RUN_ID='123',
            GITHUB_RUN_ATTEMPT='1',GITHUB_JOB='fixture')

    @staticmethod
    def write(repo, relative, value):
        path=repo/relative; path.parent.mkdir(parents=True,exist_ok=True);path.write_text(value)

    def git(self,*args,cwd=None,check=True):
        return subprocess.run([REAL_GIT,*args],cwd=cwd,env=self.env,capture_output=True,text=True,check=check)

    def push_concurrent(self):
        self.git('add','-A',cwd=self.concurrent)
        self.git('commit','-q','-m','Concurrent change',cwd=self.concurrent)
        self.git('push','-q','origin','HEAD:main',cwd=self.concurrent)

    def remote_file(self,path):
        result=self.git('--git-dir',str(self.remote),'show','main:'+path,check=False)
        return result.stdout if result.returncode==0 else None

    def remote_head(self):
        return self.git('--git-dir',str(self.remote),'rev-parse','refs/heads/main').stdout.strip()

    def call(self, path='output', *, attempts=2, required=True, force=False, mode='', limit=None, run_id='123'):
        env={**self.env,'FIXTURE_MODE':mode}
        env['GITHUB_RUN_ID']=run_id
        if limit is not None:env['GITHUB_MAX_FILE_BYTES']=str(limit)
        return subprocess.run(['bash',str(SCRIPT),path,'Fixture output',str(attempts),str(required).lower(),str(force).lower()],
            cwd=self.producer,env=env,capture_output=True,text=True,timeout=30)

    def snapshot(self):
        files={str(p.relative_to(self.producer)):p.read_bytes() for p in self.producer.rglob('*')
               if p.is_file() and '.git' not in p.relative_to(self.producer).parts}
        return (self.git('rev-parse','HEAD',cwd=self.producer).stdout,
                (self.producer/'.git/index').read_bytes(), (self.producer/'.git/config').read_bytes(), files)

    def test_recovered_publication_resolves_pushed_revision_without_moving_code_head(self):
        relative = 'portal_suite/data/blog_archive/20261113/' + 'c' * 64 + '.json'
        self.write(self.producer, relative, '{"fixture":true}\n')
        code_head = self.git('rev-parse', 'HEAD', cwd=self.producer).stdout.strip()
        result = self.call(path='portal_suite/data/blog_archive')
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(self.git('rev-parse', 'HEAD', cwd=self.producer).stdout.strip(), code_head)
        workflow = (SCRIPT.parents[1] / '.github/workflows/recover-report-article-delivery.yml').read_text()
        block = workflow.split('- name: Resolve the acknowledged archive revision\n', 1)[1].split('\n      - ', 1)[0]
        command = textwrap.dedent(block.split('        run: |\n', 1)[1])
        output = self.root / 'archive-output'
        resolved = subprocess.run(['bash', '-e', '-o', 'pipefail', '-c', command], cwd=self.producer,
                                  env={**self.env, 'GITHUB_OUTPUT': str(output)}, capture_output=True, text=True, timeout=30)
        self.assertEqual(resolved.returncode, 0, resolved.stdout + resolved.stderr)
        archive_commit = output.read_text().strip().removeprefix('sha=')
        self.assertEqual(archive_commit, self.remote_head())
        self.assertNotEqual(archive_commit, code_head)
        check = 'from pathlib import Path; from watch_recovered_article_publication import committed_record; committed_record(Path(%r), %r)'
        env = {**self.env, 'PYTHONPATH': str(SCRIPT.parent)}
        old = subprocess.run([sys.executable, '-c', check % (relative, code_head)], cwd=self.producer,
                             env=env, capture_output=True, text=True, timeout=30)
        self.assertNotEqual(old.returncode, 0)
        self.assertIn('publication_archive_not_committed', old.stderr)
        current = subprocess.run([sys.executable, '-c', check % (relative, archive_commit)], cwd=self.producer,
                                 env=env, capture_output=True, text=True, timeout=30)
        self.assertEqual(current.returncode, 0, current.stdout + current.stderr)

    def test_remote_additions_and_untouched_updates_survive_with_explicit_prune(self):
        self.write(self.producer,'output/A.txt','producer A\n')
        (self.producer/'output/prune.txt').unlink()
        self.write(self.producer,'outside.txt','caller staged change\n')
        self.git('add','outside.txt',cwd=self.producer)
        self.write(self.concurrent,'output/B.txt','concurrent B\n')
        self.write(self.concurrent,'output/existing.txt','remote v2\n')
        self.push_concurrent()
        before=self.snapshot()
        result=self.call()
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)
        self.assertEqual(self.remote_file('output/A.txt'),'producer A\n')
        self.assertEqual(self.remote_file('output/B.txt'),'concurrent B\n')
        self.assertEqual(self.remote_file('output/existing.txt'),'remote v2\n')
        self.assertIsNone(self.remote_file('output/prune.txt'))
        self.assertEqual(self.remote_file('outside.txt'),'outside base\n')
        self.assertEqual(self.snapshot(),before)

    def test_nonoverlapping_same_file_edits_merge(self):
        self.write(self.producer,'output/existing.txt','first\nmiddle\nLOCAL last\n')
        self.write(self.concurrent,'output/existing.txt','REMOTE first\nmiddle\nlast\n')
        self.push_concurrent()
        result=self.call()
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)
        self.assertEqual(self.remote_file('output/existing.txt'),'REMOTE first\nmiddle\nLOCAL last\n')

    def test_true_conflict_does_not_push_or_change_caller_even_for_optional_output(self):
        self.write(self.producer,'output/existing.txt','first\nLOCAL\nlast\n')
        self.write(self.concurrent,'output/existing.txt','first\nREMOTE\nlast\n')
        self.push_concurrent();before=self.snapshot();remote=self.remote_head()
        for required in (True,False):
            result=self.call(required=required)
            self.assertEqual(result.returncode,1 if required else 0,result.stdout+result.stderr)
            self.assertIn('conflicts with current main',result.stdout)
            self.assertEqual(self.remote_head(),remote);self.assertEqual(self.snapshot(),before)

    def test_already_accepted_intent_is_idempotent_and_sequential_additions_preserve_records(self):
        self.write(self.producer,'output/A.txt','A\n')
        self.assertEqual(self.call().returncode,0)
        head=self.remote_head()
        self.assertEqual(self.call().returncode,0)
        self.assertEqual(self.remote_head(),head)
        self.git('fetch','-q','origin','main',cwd=self.concurrent)
        self.git('reset','--hard','FETCH_HEAD',cwd=self.concurrent)
        self.write(self.concurrent,'output/B.txt','B\n');self.push_concurrent()
        self.write(self.producer,'output/C.txt','C\n')
        result=self.call()
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)
        self.assertEqual([self.remote_file('output/'+n+'.txt') for n in ('A','B','C')],['A\n','B\n','C\n'])

    def test_acknowledged_same_file_can_evolve_through_overlapping_output_scopes(self):
        self.write(self.producer,'output/existing.txt','producer v1\n')
        original_head=self.git('rev-parse','HEAD',cwd=self.producer).stdout
        first=self.call('output/existing.txt')
        self.assertEqual(first.returncode,0,first.stdout+first.stderr)
        self.git('fetch','-q','origin','main',cwd=self.concurrent)
        self.git('reset','--hard','FETCH_HEAD',cwd=self.concurrent)
        self.write(self.concurrent,'output/B.txt','remote-only B\n');self.push_concurrent()
        self.write(self.producer,'output/existing.txt','producer v2\n')
        self.write(self.producer,'output/A.txt','new A\n')
        before=self.snapshot();second=self.call('output')
        self.assertEqual(second.returncode,0,second.stdout+second.stderr)
        self.assertEqual(self.remote_file('output/existing.txt'),'producer v2\n')
        self.assertEqual(self.remote_file('output/B.txt'),'remote-only B\n')
        self.assertEqual(self.remote_file('output/A.txt'),'new A\n')
        self.assertEqual(self.git('rev-parse','HEAD',cwd=self.producer).stdout,original_head)
        self.assertEqual(self.snapshot(),before)

    def test_acknowledged_baseline_is_not_shared_with_another_run(self):
        self.write(self.producer,'output/existing.txt','producer v1\n')
        self.assertEqual(self.call().returncode,0)
        self.write(self.producer,'output/existing.txt','different producer v2\n')
        head=self.remote_head();result=self.call(run_id='124')
        self.assertEqual(result.returncode,1,result.stdout+result.stderr)
        self.assertEqual(self.remote_head(),head)

    def test_failed_push_does_not_advance_the_producer_baseline(self):
        self.write(self.producer,'output/existing.txt','unacknowledged v1\n')
        self.assertEqual(self.call(mode='push-fails').returncode,1)
        self.assertEqual(self.git('for-each-ref','--format=%(refname)','refs/codex-output-producers',cwd=self.producer).stdout,'')
        self.write(self.producer,'output/existing.txt','acknowledged v2\n')
        result=self.call()
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)
        self.assertEqual(self.remote_file('output/existing.txt'),'acknowledged v2\n')

    def test_push_race_retries_the_original_frozen_intent(self):
        self.write(self.producer,'output/A.txt','frozen A\n')
        result=self.call(mode='race')
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)
        self.assertEqual(self.remote_file('output/A.txt'),'frozen A\n')
        self.assertEqual(self.remote_file('output/B.txt'),'concurrent B during push\n')
        self.assertEqual((self.producer/'output/A.txt').read_text(),'changed after frozen intent\n')
        self.assertEqual(json.loads((self.root/'calls.json').read_text())['push'],2)

    def test_accepted_push_with_lost_ack_is_verified_without_duplicate_commit(self):
        self.write(self.producer,'output/A.txt','A\n')
        result=self.call(attempts=1,mode='accepted-ack-lost')
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)
        self.assertEqual(json.loads((self.root/'calls.json').read_text()),{'fetch':2,'push':1})
        self.assertEqual(self.git('--git-dir',str(self.remote),'rev-list','--count','main').stdout.strip(),'2')

    def test_bounded_transport_failures_keep_optional_and_required_semantics(self):
        self.write(self.producer,'output/A.txt','A\n');head=self.remote_head()
        for mode in ('fetch-fails','push-fails'):
            for required in (True,False):
                (self.root/'calls.json').unlink(missing_ok=True)
                result=self.call(mode=mode,required=required)
                self.assertEqual(result.returncode,1 if required else 0,result.stdout+result.stderr)
                counts=json.loads((self.root/'calls.json').read_text())
                self.assertEqual(counts['fetch'],3)
                self.assertEqual(counts.get('push',0),0 if mode=='fetch-fails' else 2)
                self.assertEqual(self.remote_head(),head)

    def test_explicit_rename_is_preserved(self):
        (self.producer/'output/existing.txt').rename(self.producer/'output/renamed.txt')
        self.write(self.concurrent,'output/B.txt','B\n');self.push_concurrent()
        result=self.call()
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)
        self.assertIsNone(self.remote_file('output/existing.txt'))
        self.assertEqual(self.remote_file('output/renamed.txt'),'first\nmiddle\nlast\n')
        self.assertEqual(self.remote_file('output/B.txt'),'B\n')

    def test_remote_rename_cannot_move_producer_changes_outside_requested_output(self):
        (self.concurrent/'other').mkdir()
        (self.concurrent/'output/existing.txt').rename(self.concurrent/'other/existing.txt')
        self.push_concurrent()
        self.write(self.producer,'output/existing.txt','first\nmiddle\nproducer edit\n')
        head=self.remote_head();before=self.snapshot();result=self.call()
        self.assertEqual(result.returncode,1,result.stdout+result.stderr)
        self.assertIn('outside the requested output',result.stdout)
        self.assertEqual(self.remote_head(),head)
        self.assertEqual(self.remote_file('other/existing.txt'),'first\nmiddle\nlast\n')
        self.assertEqual(self.snapshot(),before)

    def test_ignored_pdf_requires_exact_opt_in_and_cannot_include_synthesis_inputs(self):
        self.write(self.producer,'ignored/report.pdf','pdf fixture\n')
        self.write(self.producer,'ignored/other.pdf','other fixture\n')
        self.write(self.producer,'ignored/inputs.json','private inputs\n')
        self.assertEqual(self.call('ignored',force=False).returncode,0)
        self.assertIsNone(self.remote_file('ignored/report.pdf'))
        result=self.call('ignored/report.pdf',force=True)
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)
        self.assertEqual(self.remote_file('ignored/report.pdf'),'pdf fixture\n')
        self.assertIsNone(self.remote_file('ignored/other.pdf'))
        self.assertIsNone(self.remote_file('ignored/inputs.json'))

    def test_tracked_ignored_pdf_can_be_updated_from_sparse_checkout(self):
        self.write(self.producer, 'ignored/report.pdf', 'previous public PDF\n')
        self.git('add', '-f', 'ignored/report.pdf', cwd=self.producer)
        self.git('commit', '-q', '-m', 'Previous public PDF', cwd=self.producer)
        self.git('push', '-q', 'origin', 'HEAD:main', cwd=self.producer)
        self.git('sparse-checkout', 'init', '--cone', cwd=self.producer)
        self.git('sparse-checkout', 'set', 'ignored', cwd=self.producer)
        self.write(self.producer, 'ignored/report.pdf', 'updated public PDF\n')
        self.write(self.producer, 'ignored/inputs.json', 'private synthesis\n')
        before = self.snapshot()
        result = self.call('ignored/report.pdf', force=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(self.remote_file('ignored/report.pdf'), 'updated public PDF\n')
        self.assertIsNone(self.remote_file('ignored/inputs.json'))
        self.assertEqual(self.snapshot(), before)

    def test_oversized_intent_and_oversized_three_way_result_never_push(self):
        self.write(self.producer,'output/A.txt','too large\n');head=self.remote_head()
        self.assertEqual(self.call(limit=3).returncode,3)
        self.assertEqual(self.remote_head(),head)
        (self.producer/'output/A.txt').unlink()
        self.write(self.producer,'output/existing.txt','first\nmiddle\nLOCAL last\n')
        self.write(self.concurrent,'output/existing.txt','REMOTE first\nmiddle\nlast\n');self.push_concurrent()
        head=self.remote_head()
        result=self.call(limit=26)
        self.assertEqual(result.returncode,3,result.stdout+result.stderr)
        self.assertEqual(self.remote_head(),head)


if __name__=='__main__':
    unittest.main()
