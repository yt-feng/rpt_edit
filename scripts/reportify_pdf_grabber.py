#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
用途：
    自动打开 Reportify 报告页，尝试抓取页面中“可预览”的 PDF，
    并保存为本地 PDF 文件。

适用场景：
    - 页面本身能显示 PDF 预览
    - 页面可能会弹登录框，但底层 PDF 资源其实已经加载了
    - 想把“浏览器里能看到的 PDF”落地为真正的 .pdf 文件

实现思路（和这次实际抓取过程一致）：
    1. 用 Playwright 打开页面
    2. 等待页面和预览区域加载
    3. 监听浏览器网络响应，优先从响应头 / URL 中识别 PDF
    4. 同时监听浏览器下载事件（有些站点会直接触发下载）
    5. 如果没抓到，再从页面 DOM / performance entries 里补捞 PDF 线索
    6. 最后把 PDF 保存到本地

依赖：
    pip install playwright
    playwright install chromium

运行方式：
    python reportify_pdf_grabber.py \
      --url 'https://reportify.cn/reports/1264649995240476672' \
      --output 'report.pdf'

说明：
    - 脚本尽量写得“可读”和“可改”，所以注释会比较多
    - 某些站点会改前端逻辑，届时你可能需要微调等待时间、选择器或识别规则
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import time
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

from playwright.sync_api import sync_playwright, Response, Download, TimeoutError as PlaywrightTimeoutError


# ------------------------------
# 一些基础工具函数
# ------------------------------

def log(message: str) -> None:
    """
    打印带统一前缀的日志，方便看运行过程。

    为什么要单独封装一个 log 函数？
    - 后面如果你想把日志改成写入文件，或加时间戳，改这里就行
    - 主流程里看起来更清爽
    """
    print(f"[INFO] {message}")



def warn(message: str) -> None:
    """
    打印警告信息。
    """
    print(f"[WARN] {message}")



def is_probably_pdf_response(response: Response) -> bool:
    """
    判断一个网络响应“像不像 PDF”。

    这里不用单一条件判断，而是多条件结合：
    1. Content-Type 是否包含 application/pdf
    2. Content-Disposition 里是否带 .pdf
    3. URL 路径是否以 .pdf 结尾
    4. URL / 查询参数中是否明显包含 pdf 线索

    为什么要这样写？
    因为很多网站并不规范：
    - 有的 URL 根本不带 .pdf
    - 有的返回头不标准
    - 有的把 PDF 包在下载接口里
    所以要尽量“宽松识别，再人工核验”。
    """
    headers = {k.lower(): v for k, v in response.headers.items()}
    content_type = headers.get("content-type", "").lower()
    content_disposition = headers.get("content-disposition", "").lower()
    url = response.url.lower()

    if "application/pdf" in content_type:
        return True

    if ".pdf" in content_disposition:
        return True

    if urlparse(url).path.endswith(".pdf"):
        return True

    if re.search(r"(^|[?&/_=-])pdf([?&/_=-]|$)", url):
        return True

    return False



def is_pdf_bytes(data: bytes) -> bool:
    """
    通过文件头判断一段二进制数据是不是 PDF。

    PDF 文件通常以 `%PDF-` 开头。
    这是最稳的二次确认手段之一。
    """
    return data.startswith(b"%PDF-")



def sanitize_filename(name: str) -> str:
    """
    把文件名里的非法字符替换掉，避免在不同系统上保存失败。
    """
    name = re.sub(r'[\\/:*?"<>|]+', '_', name)
    name = re.sub(r'\s+', ' ', name).strip()
    return name or "downloaded_report.pdf"


def parse_cookie_header(header: str) -> list[tuple[str, str]]:
    """
    Parse a Cookie header into name/value pairs without logging secret values.
    """
    pairs: list[tuple[str, str]] = []
    for part in string_parts(header):
        if "=" not in part:
            continue
        name, value = part.split("=", 1)
        name = name.strip()
        value = value.strip()
        if name and value:
            pairs.append((name, value))
    return pairs


def string_parts(value: str) -> list[str]:
    return [part.strip() for part in str(value or "").split(";") if part.strip()]


def add_cookie_header_to_context(context, cookie_header: str) -> None:
    pairs = parse_cookie_header(cookie_header)
    if not pairs:
        return
    cookies = []
    for domain in ["reportify.cn", ".reportify.cn", "api.reportify.cn", ".api.reportify.cn"]:
        for name, value in pairs:
            cookies.append({
                "name": name,
                "value": value,
                "domain": domain,
                "path": "/",
                "secure": True,
                "sameSite": "Lax",
            })
    context.add_cookies(cookies)
    log(f"已加载后台访问凭证：{len(pairs)} 个 cookie。")


# ------------------------------
# 负责抓 PDF 的核心类
# ------------------------------

class ReportifyPDFGrabber:
    """
    一个小型抓取器类，用来管理：
    - 页面
    - 网络响应监听
    - 下载事件监听
    - 最终 PDF 保存

    这样做比把所有逻辑堆在 main() 里更好维护。
    """

    def __init__(self, page, output_path: Path):
        self.page = page
        self.output_path = output_path

        # 这里保存我们抓到的“最佳候选 PDF 数据”
        # 一旦拿到真正的 PDF 字节，就存进来。
        self.captured_pdf_bytes: Optional[bytes] = None
        self.captured_pdf_url: Optional[str] = None

        # 有些网站会直接触发浏览器下载，这里保存下载对象
        self.captured_download: Optional[Download] = None

    def on_response(self, response: Response) -> None:
        """
        网络响应监听器。

        每次页面发出请求并收到响应时，这个函数都会被调用。
        我们在这里筛选“可能是 PDF 的响应”。
        """
        # 如果已经抓到 PDF 了，就没必要继续处理了
        if self.captured_pdf_bytes is not None:
            return

        try:
            if not is_probably_pdf_response(response):
                return

            # 先把 body 读出来，再检查是否真的是 PDF。
            data = response.body()
            if not data:
                return

            if is_pdf_bytes(data):
                self.captured_pdf_bytes = data
                self.captured_pdf_url = response.url
                log(f"抓到 PDF 响应：{response.url}")
        except Exception as exc:
            # 这里故意不让监听器抛异常。
            # 因为监听器报错会打断整个页面流程，得不偿失。
            warn(f"处理网络响应时出错：{exc}")

    def on_download(self, download: Download) -> None:
        """
        浏览器下载事件监听器。

        某些站点会在预览、点击按钮或脚本执行时，直接让浏览器下载文件。
        这种情况下，不一定能从 response 里舒服地拿到 bytes，
        所以同时监听 download 是非常有价值的兜底方案。
        """
        if self.captured_download is None:
            self.captured_download = download
            suggested = download.suggested_filename
            log(f"捕获到浏览器下载事件：{suggested}")

    def attach_listeners(self) -> None:
        """
        给页面挂监听器。
        """
        self.page.on("response", self.on_response)
        self.page.on("download", self.on_download)

    def wait_for_preview(self, timeout_ms: int = 30000) -> None:
        """
        等待页面进入“有预览内容”的状态。

        注意：
        这里不依赖单一选择器，因为不同页面实现可能不同。
        我们采用“尽量宽松”的等待策略：
        - 先等页面 load
        - 再等一会儿让异步资源加载
        - 再尝试等待一些常见的 PDF 预览元素

        为什么不强行写死某个 class？
        因为前端一改 class 名，脚本就废了。
        """
        log("等待页面基础加载...")
        self.page.wait_for_load_state("load", timeout=timeout_ms)

        # 很多现代前端页面在 load 后还会继续拉接口、渲染内容。
        self.page.wait_for_timeout(3000)

        # 尝试等待一些常见的预览线索。
        candidate_selectors = [
            "embed[type='application/pdf']",
            "iframe",
            "canvas",
            "img",
            "text=Global Research",
            "text=Equity Strategy",
            "text=UBS",
        ]

        for selector in candidate_selectors:
            try:
                self.page.locator(selector).first.wait_for(timeout=3000)
                log(f"检测到预览线索：{selector}")
                return
            except PlaywrightTimeoutError:
                continue

        warn("没有明确等到预览元素，但继续尝试抓取资源。")

    def dismiss_login_modal_if_possible(self) -> None:
        """
        尝试关闭登录弹窗。

        为什么是“尝试”而不是“必须”？
        因为很多时候即使弹窗存在，底层 PDF 也已经加载到浏览器里了。
        所以关闭失败并不意味着任务失败。
        """
        possible_close_texts = ["Close", "关闭", "×"]
        for text in possible_close_texts:
            try:
                locator = self.page.get_by_text(text, exact=True)
                if locator.count() > 0:
                    locator.first.click(timeout=2000)
                    log(f"已尝试关闭登录弹窗：{text}")
                    self.page.wait_for_timeout(1000)
                    return
            except Exception:
                continue

        # 再兜底找 aria-label/button 的 close 语义
        try:
            buttons = self.page.locator("button")
            count = min(buttons.count(), 30)
            for i in range(count):
                btn = buttons.nth(i)
                text = (btn.inner_text(timeout=500) or "").strip().lower()
                aria = (btn.get_attribute("aria-label") or "").strip().lower()
                if text in {"close", "关闭", "×"} or aria in {"close", "关闭"}:
                    btn.click(timeout=1500)
                    log("已通过 button 语义尝试关闭登录弹窗")
                    self.page.wait_for_timeout(1000)
                    return
        except Exception:
            pass

        warn("未明确关闭登录弹窗，继续执行抓取。")

    def probe_from_dom(self) -> Optional[str]:
        """
        如果网络监听还没直接抓到 PDF，就从 DOM 和 performance entries 里找线索。

        返回值：
            找到的候选 URL（字符串）或 None

        这个步骤对应我人工排查时做的事情：
        - 看 iframe/embed/object
        - 看页面 HTML 里的 URL
        - 看 performance.getEntriesByType('resource') 里的资源
        """
        log("从 DOM / performance entries 中补捞 PDF 线索...")

        result = self.page.evaluate(
            r"""
            () => {
              const html = document.documentElement.outerHTML || '';

              const urlPattern = /https?:[^"'\\\s>]+/g;
              const htmlUrls = [...new Set((html.match(urlPattern) || []))];

              const resourceUrls = performance
                .getEntriesByType('resource')
                .map(r => r.name)
                .filter(Boolean);

              const embedUrls = Array.from(document.querySelectorAll('iframe, embed, object'))
                .map(el => el.src || el.data || '')
                .filter(Boolean);

              const all = [...new Set([...htmlUrls, ...resourceUrls, ...embedUrls])];

              const candidates = all.filter(u => {
                const s = String(u).toLowerCase();
                return s.includes('.pdf') || s.includes('pdf') || s.includes('preview') || s.includes('download') || s.includes('report');
              });

              return { candidates };
            }
            """
        )

        candidates = result.get("candidates", [])
        for url in candidates:
            low = url.lower()
            if any(blocked in low for blocked in ["rumt-zh.com", "/collect", "/speed", "rateconfig"]):
                continue
            if ".pdf" in low or "application/pdf" in low or "download" in low:
                log(f"发现候选资源：{url}")
                return url

        if candidates:
            filtered = [
                url for url in candidates
                if not any(blocked in url.lower() for blocked in ["rumt-zh.com", "/collect", "/speed", "rateconfig"])
            ]
            if filtered:
                log(f"发现候选资源（首个）：{filtered[0]}")
                return filtered[0]

        return None

    def try_fetch_candidate_url(self, context, candidate_url: str) -> bool:
        """
        尝试直接用浏览器上下文请求候选 URL，并判断是否返回了 PDF。

        为什么不用 requests？
        - 因为浏览器上下文天然带着当前页面环境，更接近真实访问路径
        - 某些站点有基于 cookie / header / referer 的访问限制

        返回：
            True  -> 成功抓到 PDF
            False -> 没抓到
        """
        try:
            log(f"尝试直接请求候选资源：{candidate_url}")
            resp = context.request.get(candidate_url, timeout=30000)
            if not resp.ok:
                warn(f"候选资源请求失败，状态码：{resp.status}")
                return False

            data = resp.body()
            headers = {k.lower(): v for k, v in resp.headers.items()}
            content_type = headers.get("content-type", "").lower()

            if is_pdf_bytes(data) or "application/pdf" in content_type:
                self.captured_pdf_bytes = data
                self.captured_pdf_url = candidate_url
                log("通过候选资源地址成功拿到 PDF")
                return True

            warn("候选资源返回的不是 PDF")
            return False
        except Exception as exc:
            warn(f"请求候选资源时失败：{exc}")
            return False

    def save_result(self) -> Path:
        """
        把最终抓到的结果保存到 output_path。

        保存优先级：
        1. 已捕获的 PDF bytes
        2. 浏览器 download 事件中的临时文件
        3. 都没有 -> 抛错
        """
        self.output_path.parent.mkdir(parents=True, exist_ok=True)

        if self.captured_pdf_bytes is not None:
            self.output_path.write_bytes(self.captured_pdf_bytes)
            log(f"已保存 PDF：{self.output_path}")
            return self.output_path

        if self.captured_download is not None:
            temp_path = self.captured_download.path()
            if temp_path and Path(temp_path).exists():
                data = Path(temp_path).read_bytes()
                if is_pdf_bytes(data):
                    self.output_path.write_bytes(data)
                    log(f"已从浏览器下载文件保存 PDF：{self.output_path}")
                    return self.output_path

        raise RuntimeError("未能抓取到 PDF 文件")

    def is_login_limited_page(self) -> bool:
        try:
            text = self.page.locator("body").inner_text(timeout=5000)
        except Exception:
            return True
        login_markers = ["登录查看全文", "立即登录", "手机号", "验证码"]
        return any(marker in text for marker in login_markers)

    def try_print_page_pdf(self) -> bool:
        """
        Some readable pages render the document directly without exposing the
        original PDF URL. In that case, print the rendered document page to PDF.
        """
        if self.is_login_limited_page():
            warn("页面仍处于登录/预览限制状态，不能打印为交付 PDF。")
            return False
        try:
            self.output_path.parent.mkdir(parents=True, exist_ok=True)
            self.page.pdf(
                path=str(self.output_path),
                format="A4",
                print_background=True,
                margin={"top": "8mm", "right": "8mm", "bottom": "8mm", "left": "8mm"},
            )
            data = self.output_path.read_bytes()
            if is_pdf_bytes(data):
                log(f"已通过页面打印兜底保存 PDF：{self.output_path}")
                return True
        except Exception as exc:
            warn(f"页面打印 PDF 兜底失败：{exc}")
        return False


# ------------------------------
# 主流程
# ------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description="抓取 Reportify 页面中可预览的 PDF")
    parser.add_argument("--url", required=True, help="报告页面 URL")
    parser.add_argument("--output", required=True, help="输出 PDF 路径")
    parser.add_argument(
        "--headless",
        action="store_true",
        help="启用无头模式（默认是有头，便于调试）",
    )
    parser.add_argument(
        "--cookie-header",
        default=os.getenv("REPORTIFY_COOKIE_HEADER") or os.getenv("REPORTIFY_COOKIE") or "",
        help="可选 Cookie header，用于后台浏览器访问需要登录的页面。",
    )
    args = parser.parse_args()

    page_url = args.url
    output_path = Path(args.output).expanduser().resolve()

    with sync_playwright() as p:
        # 这里启动 Chromium。
        # headless=False 更方便你观察页面过程；
        # 如果要挂到服务器定时跑，可以传 --headless。
        browser = p.chromium.launch(headless=args.headless)

        # accept_downloads=True 非常关键：
        # 只有开启后，Playwright 才会真正接住浏览器下载文件。
        context = browser.new_context(accept_downloads=True)
        add_cookie_header_to_context(context, args.cookie_header)
        page = context.new_page()

        grabber = ReportifyPDFGrabber(page=page, output_path=output_path)
        grabber.attach_listeners()

        try:
            log(f"打开页面：{page_url}")
            page.goto(page_url, wait_until="domcontentloaded", timeout=60000)

            # 让页面先初步稳定下来
            page.wait_for_timeout(2000)

            # 尝试关闭弹窗，但不是强制步骤
            grabber.dismiss_login_modal_if_possible()

            # 等待预览内容或相关资源加载
            grabber.wait_for_preview(timeout_ms=30000)

            # 再额外给页面一点时间，让潜在的 PDF 请求跑出来
            page.wait_for_timeout(5000)

            # 第一优先：网络监听器已经直接抓到了 PDF
            if grabber.captured_pdf_bytes is not None:
                log("网络监听阶段已成功抓到 PDF")
            else:
                # 第二优先：浏览器是否已经触发下载
                if grabber.captured_download is not None:
                    log("已捕获浏览器下载事件，稍后直接保存")
                else:
                    # 第三优先：从 DOM / performance 中找候选资源，再主动请求
                    candidate_url = grabber.probe_from_dom()
                    if candidate_url:
                        grabber.try_fetch_candidate_url(context=context, candidate_url=candidate_url)

            printed = False
            if grabber.captured_pdf_bytes is None and grabber.captured_download is None:
                printed = grabber.try_print_page_pdf()

            saved = output_path if printed else grabber.save_result()

            # 最后再做一次非常轻量的文件头校验
            data = saved.read_bytes()
            if not is_pdf_bytes(data):
                raise RuntimeError("输出文件已保存，但文件头不是合法 PDF")

            size_kb = len(data) / 1024
            log(f"抓取完成：{saved} （{size_kb:.1f} KB）")
            return 0

        finally:
            # 无论成功失败，都把浏览器关掉，避免残留进程
            context.close()
            browser.close()


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        warn("用户中断执行")
        raise SystemExit(130)
    except Exception as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        raise SystemExit(1)
