# KCDesk 韩文、日文与阿拉伯文站点架构

## 文档状态与发布边界

本文定义 KCDesk 多语言站点的实现架构、内容边界、生成门禁和上线顺序。代码和离线构建可以完成，但在远端同步、正式翻译、视觉验收和线上验证完成前仍不可发布。

- 远端 `main` 是唯一正式基线。开始实现、合并或发布前，必须重新确认远端 `main`，并从该基线重放多语言改动。
- 当前分支、隔离工作树、未提交文件、测试产物和影子构建都不是正式基线，也不是发布证据。
- 当前状态不可发布：在三种语言都具备完整翻译清单、构建产物、自动化验证、影子站验收和明确激活步骤之前，不得把 locale 路由接入正式流量。
- 本方案不改变中文根站的既有公开 UI、正文和路由语义。根站仍是当前中文站；新增语言仅使用独立前缀。
- 发布结论必须分别说明代码、翻译覆盖、静态产物、部署、激活和线上验证，不能以其中一项代替全部完成。

## 不可破坏的产品契约

### 路由

中文站继续使用现有根路径。新语言使用稳定、可直接访问的路径前缀；是否进入搜索引擎索引按下文固定 cohort 策略控制：

- 韩文：`/ko/`
- 日文：`/ja/`
- 阿拉伯文：`/ar/`

公开页面按一一对应关系镜像，例如：

| 中文根站 | 韩文 | 日文 | 阿拉伯文 |
| --- | --- | --- | --- |
| `/reports/` | `/ko/reports/` | `/ja/reports/` | `/ar/reports/` |
| `/reports/{id}.html` | `/ko/reports/{id}.html` | `/ja/reports/{id}.html` | `/ar/reports/{id}.html` |
| `/reports/institutions/{slug}/` | `/ko/reports/institutions/{slug}/` | `/ja/reports/institutions/{slug}/` | `/ar/reports/institutions/{slug}/` |
| `/reports/topics/{slug}/` | `/ko/reports/topics/{slug}/` | `/ja/reports/topics/{slug}/` | `/ar/reports/topics/{slug}/` |
| `/blog/{slug}.html` | `/ko/blog/{slug}.html` | `/ja/blog/{slug}.html` | `/ar/blog/{slug}.html` |
| `/charts` | `/ko/charts` | `/ja/charts` | `/ar/charts` |

报告 ID、机构 slug、专题 slug 和 Blog slug 必须保持稳定，不做语言化改写。这样才能可靠建立 canonical、hreflang、变更检测和退役映射。

不根据浏览器语言、IP 或地理位置自动跳转。用户或搜索引擎直接请求任一 locale URL 时，服务器始终返回该 URL 对应的固定语言内容；不得通过内容协商让同一 URL 返回不同语言正文。

### 简体中文浏览器不显示多语言入口

“不让简体中文浏览器用户发现多语言 feature”在 UI 层解释为：不渲染语言入口，不改变中文页面正文，不自动跳转。它不能解释为让公开 locale 页面无法从搜索、外链、sitemap 或 HTML `<head>` 中发现，因为那会与可索引的 SEO 目标冲突。

- `zh-CN`、`zh-Hans`、`zh-SG` 以及无地区的 `zh` 视为简体中文浏览器环境。
- 上述环境不插入语言选择器节点，不显示入口占位，不产生首屏闪现，也不发出 locale CSS/JS 请求；中文页 `<head>` 中的轻量内联门禁先读取首选浏览器语言，只有非简体中文环境才按需加载语言入口资源。
- `zh-TW`、`zh-HK`、`zh-MO`、`zh-Hant` 不自动归入简体中文；其入口策略可按非简体环境执行。
- 中文根页的服务端 `<body>` 继续沿用正式基线。若要让其他浏览器语言从中文根站进入 locale，入口只能在确认不是简体中文后由客户端插入。
- 即使简体中文用户知道并直接打开 `/ja/`、`/ko/` 或 `/ar/`，页面仍正常返回、访问和索引，只是不渲染语言选择器。
- 不对 crawler、简体中文用户和其他用户返回不同的主体内容，避免形成 cloaking。

## “全量翻译”的范围

全量是“全部公开网站展示内容”的 100% 覆盖，而不是对所有被 KCDesk 索引、存储或有权访问的材料做全文翻译。

必须翻译：

- 公开首页、报告列表、机构页、专题页、公开报告落地页、Blog、图表页、About、公开政策页的可见文案；
- 页面标题、摘要、说明、面包屑、导航、筛选、搜索、表单、按钮、加载态、空状态、错误态和页脚；
- `title`、description、Open Graph、可见的可引用摘要、结构化数据中的页面名称与描述；
- `aria-label`、placeholder、图片替代文本及其他会影响可访问性的用户可见语义；
- 公开 catalog 中实际出现在页面上的标题、简介、来源说明和相关推荐文案。

明确不包含：

- 原始版权 PDF、研报附件或第三方受版权保护的全文；
- 会员私有内容、登录后内容、申请交付内容、内部备注及非公开元数据；
- 仅用于搜索召回的私有索引字段；
- 用被截断的搜索索引、snippet 或 OCR 片段冒充“已翻译全文”。

搜索索引中的截断字段可以在确实会公开展示时作为独立展示字段翻译，但不能据此把对应原始文章、PDF 或研报标记为全文完成。翻译覆盖清单必须从权威公开渲染源生成，而不是从搜索 shard 的片段长度推断。

机构法定名称、证券代码、ticker、报告 ID、URL、邮箱、数字和模板变量默认保留；需要本地化的机构别名另行进入受控术语表。阿拉伯文采用现代标准阿拉伯语，不自动假定某个国家方言。

## 翻译数据模型与 DeepSeek 管线

### 分段与覆盖清单

每个可翻译 segment 必须有稳定身份，至少记录：

- `content_id` 和 `content_type`
- `source_field`
- `source_hash`
- `target_locale`
- `prompt_version` 和 `glossary_version`
- `translated_hash`
- `status`
- `translated_at`

构建前先从全部公开页面来源生成 expected segment 清单，再与每种语言的 completed segment 清单做精确比较。只有以下条件同时满足时，该语言快照才是 complete：

1. `expected_count == completed_count`；
2. expected ID 集合与 completed ID 集合完全相同；
3. 所有 `source_hash`、prompt 和术语表版本相符；
4. 没有空字符串、中文 fallback、截断响应、未保护模板或无效 HTML；韩文正文必须含 Hangul，阿拉伯文必须含 Arabic script，日文必须含 kana 或发生合理变化的汉字表达；
5. 页面级必需字段全部存在。

覆盖率必须是 100%。99.9% 也不得激活新快照。`coverage=1` 只统计通过占位符、目标语脚本、目标语占比及源文残留检查的当前 inventory 条目；在原文前添加“韩文/日文/阿拉伯文翻译”等短前缀、随后保留整段英文或中文的结果必须拒绝。机构法定名称字段可以原样保留，URL、数字、ticker 和 KCDesk 等已保护 token 不参与语言占比计算。当前发布链使用一个不可变候选包承载中文和三种 locale；任何翻译失败都会终止该次候选发布，线上继续服务上一份完整发布，中文站不会被半成品覆盖。相应地，该次中文内容更新也会推迟到三种语言全部完成后的下一次成功切换。

### 缓存与增量

缓存键由标准化源文本哈希、目标语言、prompt 版本和术语表版本组成。源文本及翻译规则都未变化时必须零调用复用缓存；只有新增或发生变化的 segment 才调用 DeepSeek。

每次写出 cache 前必须按当次权威公开 inventory 做精确裁剪，并重新验证所有复用项；撤稿、过期、已转私有、源 hash 不同或未通过当前质量门的 key 都不得写入候选 cache。当前过渡实现仍把这份 gzip 作为 release-visible build contract，同时使用 GitHub Actions 私有 cache 作为可恢复 checkpoint，因此 gzip 只能含本次仍公开的 presentation units，不能含历史墓碑、私有全文或会员内容。彻底迁移时应把持久副本放到发布前缀之外的私有 R2 key，并同时移除公开 active-release 冷启动回退；在这两部分原子完成前，不宣称 cache 已私有化。

每日新增内容流程为：

1. 完成公开内容摄取和稳定 ID 分配；
2. 生成各 locale 的增量 segment 清单；
3. 从哈希缓存复用未变化结果；
4. 翻译新增或变化内容；
5. 执行格式、占位符、术语和覆盖率验证；
6. 生成包含中文和三种 locale 的新候选快照；
7. 验证全部语言后一次性切换现有发布指针。

该流程应运行在受控的云端 CI 中，可由内容更新事件触发并每天至少补跑一次；不依赖个人电脑上的常驻任务。

### 并发和失败处理

本发布链把 DeepSeek 并发 `500` 设为项目级硬上限，不是必须达到的目标，也不据此推断账户实际配额。当前默认 worker 为 32；即使所选模型的服务端额度更高，也不突破这一上限。

- 实际 worker 数必须可配置且永远不超过 500。
- 对 `429`、`Retry-After`、超时和临时 5xx 使用有界重试、指数退避和随机抖动。
- 发生限流时降低有效并发，不通过启动额外进程绕过上限。
- 请求必须有批次 ID 和 segment ID，但不得把正文写入日志。
- 中断时按已验证 segment checkpoint；重跑只补缺失项。
- 解析失败、占位符破坏、HTML 结构变化或内容被截断都视为未完成，不得静默采用源语言。

现有 `scripts/translate_portal_titles.py` 只覆盖标题到 `title_zh` 的旧用途，不能作为多语言全量完成证据。新管线应复用 `scripts/deepseek_http.py` 的有界重试和 key fallback 能力，并由 locale manifest 提供严格门禁。

### Secrets 与最小化日志

- API key 只从 CI Secret 注入，不进入仓库、构建产物、缓存键、命令回显或 Actions artifact。
- 不记录请求正文、翻译正文、原始 PDF 内容、会员内容或 DeepSeek 完整响应。
- 日志仅记录批次 ID、segment ID 或哈希、locale、计数、耗时、HTTP 状态族、重试次数和错误类型。
- 可发布的本地化页面和翻译资源必然包含公开展示文案；“不记录正文”指运行日志、诊断 artifact 和遥测不复制这些正文。
- 私有或会员内容不得进入翻译 inventory，因此也不得发送给 DeepSeek。

## 静态站与运行时架构

`scripts/build_portal_suite_site.py` 继续作为中文根站的权威生成器。`scripts/build_portal_locales.py` 只在中文静态站完整构建后读取其公开渲染结果，并从同一结果生成三种镜像；它不复制三套页面模板，也不修改中文 `<body>`。locale 配置至少包含：

- URL 前缀、`html_lang`、文本方向和数字格式；
- UI 词典、术语表和翻译 manifest；
- Open Graph locale；
- 页面标题、description、面包屑和结构化数据标签；
- 字体和 RTL 行为。

`portal_suite/site_src/assets/app.js`、`site-runtime.js`、`charts.js` 及报告交互脚本中的公开文案由同一 segment 清单做构建时本地化；程序语义值（路由、DOM ID、CSS class、事件名、状态枚举和语言原生名称）必须保持不变。页面位于 `/ja/` 等前缀后，共享 `data/...` 请求由同步加载的 locale runtime 映射回根数据，并叠加紧凑的本地化 catalog 字段。

大型原始全文搜索索引保持共享，不为三种语言复制完整 corpus。公开显示标题、摘要和搜索标签可以使用紧凑 locale lookup。韩文、日文和阿拉伯文检索必须分别验证：

- 日文无空格查询与 IME composition；
- 韩文归一化和组合输入；
- 阿拉伯字符、变体、附加符号和 RTL 输入；
- 英文机构名、ticker 和数字与本地文字混输。

locale 首页首屏只加载现有 preview 数据。完整 catalog 与标题 overlay 仅在第一次搜索、筛选或翻页等明确用户意图后加载，不设置空闲自动下载；完成后原子替换数据，不清空用户已输入的查询。站内报告详情的 256 个源数据 shard 各自使用同前缀的小型翻译 overlay，只加载当前 shard 的 item 与 related 标题字段，不得复用完整 catalog overlay。本地化 external detail 沿用已加载的 preview 和四个有界 Worker 推荐源，不再下载 14,000+ 项的历史 recommendation catalog；中文根站保持原有行为与加载时序。Hot Reports 的有界 locale 覆盖层可在首屏后单独加载，查询只向 Worker 发送有界公开 ID 集；覆盖层缺失、加载失败或 generation 不一致时显示本地化的更新状态和空结果，不把源语言标题回退给用户。

发布门对首屏 locale CSS/JS 和各类运行时 JSON 分别设置体积上限：preview 512 KB、单个详情 shard overlay 512 KB、完整标题 overlay 8 MB、图表 overlay 32 MB、Hot Reports overlay 6 MB、课程数据 2 MB。首页不等待后四类文件；完整目录构建索引时按小批次让出主线程，失败后保留 preview 并允许用户意图触发有冷却时间的重试。

locale 搜索覆盖公开 catalog、标题、图表和 Hot Reports 的本地化字段。原始报告全文/PDF 不发送给 DeepSeek，也不复制三份；涉及该共享索引的选项必须明确标注为“源语言文档文本”，不能暗示支持目标语言全文检索。

## SEO 与 GEO 契约

### 全量预翻译、分批索引

“已翻译”和“允许首批索引”是两个独立状态。每次 locale 构建仍扫描、翻译并静态生成全部公开 HTML；报告搜索 catalog overlay 也保留全部公开记录。因此未进入首批索引的历史详情仍可由站内搜索、内部链接或直接 URL 打开，且请求时不调用翻译 API。索引策略只改变 locale 详情页的 robots、hreflang、locale sitemap 和 locale `llms*.txt`，不删除页面或搜索数据，也不改变中文根站正文。

默认策略 fail-closed：未显式配置起始日时，仅首页、根级公开页、列表分页、机构页、专题页等 hub/core 页面进入三种 locale sitemap；其余原本可索引的详情页静态生成，但写入 `noindex,follow`。这控制的是搜索结果收录，不宣称可以阻止爬虫请求这些公开 URL。激活时通过 `--index-start-date YYYY-MM-DD` 固定一个不随构建时间滚动的起始日。此后发布日期不早于该日期的新 Blog/Report 自动进入索引，已经进入的页面不会因“最近 N 天”窗口向前滚动而自动退役。需要单篇提升历史内容时，用 `--index-allowlist` 指向一份逐行列出 root canonical URL 或路径的文件；未知 URL 或中文源本身为 `noindex` 的 URL 会让构建失败。

资格日期只读取权威发布字段：

- Blog 详情由文章 `date` 生成 JSON-LD `BlogPosting.datePublished`；门禁只读取与当前 canonical 对应的该结构化实体，可见 `<time datetime>` 不参与资格判断；
- Report 详情只有 catalog 的源字段 `published_at` 可生成 JSON-LD `Report.datePublished`；门禁只读取与当前 canonical 对应的 Report 实体，有合法值时才自动进入 cutoff cohort；
- `date_folder` 是归档/收录目录，`server_modified`、`first_seen_at_bjt`、`last_seen_at_bjt` 是抓取或文件变化时间，不能冒充出版日期；
- sitemap `lastmod` 还包含稳定的页面模板 revision floor，只用于 freshness，不用于首批详情资格；
- 缺少或格式无效的 `datePublished` 默认保持 `noindex,follow`，直到补齐权威日期或显式 allowlist。

locale sitemap 及 locale `llms-full.txt` 只列出 hub/core 与当前 eligible cohort，避免机器发现文件绕过分批索引策略；简版 locale `llms.txt` 同样过滤任何已知但未 eligible 的详情 URL。暂缓索引的详情页保留自引用 canonical，但中、韩、日、阿四个对应页均暂不声明该详情的 hreflang 集群；提升进入 cohort 后再由同一次不可变构建统一补齐。中文 sitemap、中文 `llms.txt`、中文 `llms-full.txt` 均不改。locale RSS 继续沿用中文构建器已限定的近期集合。

Blog 的历史正文可能含不可供国际站使用的知识星球图片地址。在收集翻译单元之前，先针对 locale 副本删除 `<img>`、`<source>`、`<amp-img>` 的 `src`、`srcset`、`data-src`、`data-srcset`、`data-original`、`data-original-src`、`data-url` 或 `url` 中包含 `zsxq.img` / `zsxq_img` 的节点；HTML entity、多重百分号编码以及 inline `background-image` 也纳入识别，避免其 alt/title 等无用文案进入 DeepSeek。locale HTML 渲染后再执行同一过滤作为最终门禁。若父级是只包含该图片的 `a`、`span`、`p`、`picture`、`figure` 或 `div`，连同纯图片包装逐层删除。有正文、caption、非目标 style 或其他有效内容的容器保留。中文 Blog HTML 和其他页面不执行该清理。

### Canonical 与 hreflang

每个公开页面必须自引用 canonical。当前索引 cohort 内的对应页面组成互惠 hreflang 集群：

- 中文：`zh-Hans`
- 韩文：`ko`
- 日文：`ja`
- 阿拉伯文：`ar`
- 默认：`x-default` 指向现有中文根站对应 URL

只有已经完整生成、可访问且已进入索引 cohort 的版本才能出现在集群中。任意两个 eligible locale 页面之间必须互相声明；暂缓索引、退役或不完整版本必须从整个集群删除。`<html lang>` 与当前页面一致，阿拉伯文还必须带 `dir="rtl"`。

Open Graph 使用 `ko_KR`、`ja_JP` 和当前面向 MENA 的 `ar_AE`；阿拉伯文路由与 hreflang 仍保持通用 `ar`，不把 URL 锁定到单一国家。若未来确认新的阿语目标市场，只调整 Open Graph 区域配置，不改既有 `/ar/` URL。
`og:site_name` 也必须走 locale 渲染；源站若使用“KC桌面”，三个国际站统一输出受保护品牌 `KCDesk`，不得把中文品牌字样残留在本地化元数据中。

### Sitemap、robots、RSS 和 IndexNow

根 sitemap index 应列出按语言拆分的页面、报告和 Blog sitemap，例如：

- `sitemap-pages-{locale}.xml`
- `sitemap-reports-{locale}-{n}.xml`
- `sitemap-blog-{locale}-{n}.xml`

URL 节点使用 XHTML alternate 标注全部已完成的 hreflang 对应页。`lastmod` 来自源内容或有效翻译变化，不使用每日构建时间伪造更新。

`sitemap-baidu.xml` 和 `sitemap-sogou.xml` 保持中文专用。根 `robots.txt` 不阻止 `/ko/`、`/ja/`、`/ar/`；私有、运行时数据和管理路径继续维持当前禁止策略。Cloudflare Managed robots 是否覆盖仓库中的 sitemap 声明，需要在激活后单独进行线上验证。

每种语言生成自己的 RSS：`/{locale}/feed.xml`。`scripts/submit_portal_indexnow.py` 必须能把同一公开内容的全部已完成 locale URL 作为一组提交或退役；不能继续只以中文 `sitemap-baidu.xml` 代表所有变更。

线上 SEO 审计把三份 locale sitemap 视为一个完整集合，禁止只启用其中一部分。IndexNow 增量同时比较当前与上一份站点产物：新增/更新的 eligible URL 进入更新集合，已从 locale sitemap 退役的 URL 也进入通知集合；中文增量仍独立保持既有行为。

### llms 与可引用内容

每种语言生成：

- `/{locale}/llms.txt`
- `/{locale}/llms-full.txt`

内容必须与当前 locale 页面一致，包含自然语言的可引用摘要、清楚的来源归属、稳定 canonical 和相关内部链接。`llms.txt` 只作为可能采用该格式的其他系统的发现辅助，不替代可抓取的静态 HTML、sitemap 或真实页面内容；Google Search 明确不使用该文件，因此不能把它计作 Google SEO/GEO 成果。

不得为了 GEO 虚构原始材料没有提供的结论、作者、发布日期、引用、FAQ 或地域属性。韩文、日文和阿拉伯文应使用当地用户自然搜索问题的表达，但事实、数值和来源必须保持一致。

### JSON-LD

- `WebPage`、`CollectionPage`、`BlogPosting` 的 `inLanguage` 使用页面 locale。
- `BreadcrumbList`、`ItemList` 的名称和 URL 使用本地化页面值。
- Publisher、来源机构和原始作者身份不因页面翻译而改变。
- 页面语言与原始报告语言分离：页面可以是 `ar`，但 `Report.inLanguage` 只能来自 catalog 中可证实的原始语言字段。
- 原始英文标题可作为 `alternateName`，不能把翻译标题冒充原始出版物标题。

## 阿拉伯文 RTL 与双向文本

阿拉伯文页面使用 `<html lang="ar" dir="rtl">`。CSS 优先使用逻辑属性：

- `margin-inline-*`、`padding-inline-*`
- `border-inline-*`
- `inset-inline-*`
- `text-align: start/end`

移动抽屉、面包屑、前进/后退箭头、关闭按钮和悬浮控件需要显式 `:dir(rtl)` 验证。不能机械镜像图表、品牌图形、照片、播放图标或有固定含义的方向符号。

混合文本使用以下规则：

- 英文机构名、ticker、报告 ID 使用 `<bdi dir="auto">`；
- URL、邮箱、代码和金融图表坐标使用 `dir="ltr"`；
- 搜索输入使用 `dir="auto"`；
- 数字由 `Intl` 和 locale 配置格式化，金融数字必要时保持 LTR，不能继续硬编码 `zh-CN`。

字体使用操作系统本地的阿拉伯文、日文和韩文字体 fallback 栈，不在首屏新增外部字体请求；如果后续需要更强的一致性，再在现有 CSP 下自托管并做体积预算。阿拉伯文需单独校准字号、行高和断行，不应用拉丁字母 uppercase 或 letter-spacing 规则。

## 分阶段交付、激活与回滚

### 阶段 0：冻结契约

- 以远端 `main` 为正式基线；
- 固化中文根站 UI/body/路由快照；
- 固化公开内容 inventory 和排除清单；
- 确认阿拉伯文术语、字体和区域性 Open Graph 配置。

### 阶段 1：翻译系统与首次回填

- 构建稳定 segment ledger、哈希缓存、术语保护和 100% 覆盖检查；
- 按 locale 分批回填全部公开展示内容；
- 初始回填与每日增量分开，不把大规模首次翻译塞进日常发布窗口；
- 估算并调整静态文件数、对象存储大小和上传时长门限。报告详情页镜像三种语言后，现有 20,000 文件上限不再适用。

### 阶段 2：候选构建

- 构建独立、不可变、同时包含中文与三种 locale 的 candidate release 和 manifest；
- candidate 中可以存在 `/ko/`、`/ja/`、`/ar/` 文件，但在发布指针切换前不承接正式流量；
- 候选上传到非活动 slot 时，增量跳过的每个旧对象都必须通过 `HEAD` 精确匹配长度与发布器写入的 SHA-256 metadata；缺失、错误或同长度漂移一律重传。随后同一次 workflow 记录 commit SHA、实际 static tree SHA-256 和固定索引策略 SHA-256，并把完整 identity 放入短期验证 artifact 和 Job Summary；
- `locale-shadow` 只生成这个候选和 identity，既不进入生产 Environment 审批，也不切换公开流量；
- 对每种语言抽样首页、列表、机构、专题、详情、Blog、图表和政策页；
- 验证翻译覆盖、链接、数据加载、移动端、RTL、SEO 产物和文件完整性。

候选构建通过并不等于可发布；必须再通过激活前门禁。

### 阶段 3：激活前门禁

每个 locale 至少满足：

1. 翻译 manifest 100% complete；
2. sitemap、RSS、llms、JSON-LD 与页面集合一致；
3. canonical 与 hreflang 互惠完整；
4. 无中文 fallback、无私有内容、无原始 PDF 正文；
5. edge 路由和末尾斜杠 canonical 测试通过；
6. 简体中文浏览器入口零渲染测试通过；
7. 阿拉伯文 RTL 和 bidi 移动端验收通过；
8. 回滚目标和上一版 release manifest 已确认。

### 阶段 4：受控激活

- 只有明确开启 `PORTAL_MULTILINGUAL_ENABLED` 后，日常发布才构建三种 locale；默认关闭，不会意外激活；
- 仓库级变量 `PORTAL_MULTILINGUAL_LIVE` 是“多语言已通过首次线上验收”的人工状态，默认必须为 `false`。prepare 只读取并传递该状态，workflow 不得创建、修改或自动推断它；
- 自动 schedule/workflow_run 只有在多语言未启用，或 `PORTAL_MULTILINGUAL_LIVE=true` 时才允许进入 prepare；因此 `ENABLED=true`、`LIVE=false` 的首次激活只能由人工 dispatch 发起，不会由定时任务反复构建并堆积待审批作业；
- 当 `PORTAL_MULTILINGUAL_ENABLED=true` 且 `PORTAL_MULTILINGUAL_LIVE!=true` 时，首次真实多语言切换必须在构建候选的同一次 workflow 中等待 `kcdesk-multilingual-production` GitHub Environment 审批。审核人先查看 prepare Job Summary/artifact 中的三项 identity，再把同一组值写入该 Environment 的 `PORTAL_MULTILINGUAL_APPROVED_COMMIT_SHA`、`PORTAL_MULTILINGUAL_APPROVED_STATIC_TREE`、`PORTAL_MULTILINGUAL_APPROVED_INDEX_POLICY_SHA256`，并明确设定 `PORTAL_MULTILINGUAL_ACTIVATION_APPROVED=true` 后批准；审批后不重新构建候选；
- 审批作业从同一次 artifact 和 `prepare_release` outputs 分别读取 identity 并互相校验，然后再与 Environment vars 比较。Environment 未配置 required reviewers 时也不能直接放行：审批 flag 缺失或任一 identity 为空、过期或不一致都会终止，Edge 不切换；
- 整个 workflow 在等待 Environment 审批期间继续占用既有的 `portal-production-release` 非取消 concurrency 锁，避免后续发布覆盖当前非活动 slot；identity artifact 保留 7 天，超过审核窗口应重新生成候选；
- 不得拿较早 `locale-shadow` 或另一 workflow 的 raw static tree 给新候选放行。catalog 的 `last_seen` / `updated_at` 会让另一次构建的树发生变化；同一次候选审批正是为了消除“审核旧树、重建新树”的循环；
- 首次切换完成后仍不能由 workflow 自动把状态改为 live。只有真实 URL、RTL、资源加载和 SEO 等线上验收全部通过，运营者才可人工把仓库变量 `PORTAL_MULTILINGUAL_LIVE` 设为 `true`；首次切换失败、回滚或尚未验收时必须保持 `false`；
- `PORTAL_MULTILINGUAL_LIVE=true` 后，schedule 和可信 `workflow_run` 产生的每日新增/变化内容仍必须通过 100% 翻译覆盖、静态完整性、性能预算、Portal Worker capability、线上前置检查和 A/B 回滚门禁，但跳过首次 Environment 人工树审批并自动切换，从而实现新增内容的日常增量发布；
- 非多语言中文发布不读取多语言 Environment 审批值，跳过该审批作业并继续沿用既有 cutover；`locale-shadow` 无论 live 状态如何都跳过审批且被 cutover 条件明确排除，不会承接正式流量；
- 中文根站与三个 locale 一次性切到同一个通过验证的不可变 release；
- 切换前比较中文 body 契约，切换后比较候选与线上 locale 文件及 manifest；
- 激活后验证真实 URL、状态码、canonical、hreflang、HTML 语言、资源加载、sitemap、robots、RSS、llms 和 IndexNow；
- 只有线上验证完成后才能报告该 locale 已上线。

### 回滚

回滚通过现有 A/B 发布指针恢复到上一份完整的整站版本，不原地覆盖或删除当前对象：

- 中文根站不受影响；
- 中文、三种 locale、sitemap、RSS、llms 和 hreflang 一起恢复到上一版一致状态；
- 不完整的新版本保留为不可访问的诊断产物，按既有保留期清理；
- 首次激活前没有上一份多语言版本时，保持 feature flag 关闭，不让 locale 路由进入正式发布。

## 自动化验证清单

建议将门禁落在以下现有或新增测试：

- 扩展 `scripts/test_portal_seo.py`：locale 路径、lang/dir、自 canonical、互惠 hreflang、本地化 metadata、JSON-LD、sitemap alternate、RSS 和 llms。
- `scripts/test_build_portal_locales.py`：源哈希缓存、零变化零调用、程序语义保护、重试/checkpoint、500 硬上限、100% 覆盖阻断和无源语言 fallback。
- `scripts/test_portal_locale_runtime.js`：简体中文环境零入口节点、其他环境按规则显示、无自动跳转、locale-aware 数据 URL 与 Intl 配置。
- 扩展 `portal_suite/tests/home-search-ux.test.mjs`：日文 IME、韩文和阿拉伯文查询及混合 ticker。
- 扩展 `workers/edge-static-host/test/index.test.mjs`：`/ja` 到 `/ja/`、`/ar/index.html` 到 `/ar/`、locale 列表/详情/Blog canonical 和 query 保留。
- 扩展 `scripts/test_submit_portal_indexnow.py`：同一内容的已完成 locale 新增、更新、退役和未完成版本过滤。
- 扩展 `scripts/test_audit_portal_seo_live.py`：线上 lang、dir、hreflang 互惠和每个 locale 的确定性页面样本。
- 为中文根站增加 body/路由回归快照，并验证简体中文环境执行 locale runtime 后 DOM 不发生入口相关变化。

`.github/workflows/neutral-edge-cutover.yml` 在构建、上传和激活之间执行这些门禁，并把 locale builder 与 runtime 纳入语义 build contract。首次全量回填仍通过 `locale-shadow` 在不切换流量的前提下完成审阅；首次真实切换经同一次候选审批和线上验收后，才由运营者人工设置 `PORTAL_MULTILINGUAL_LIVE=true`。此后定时发布复用活动发布中的压缩缓存，只翻译新增或变化 segment，并在完整门禁通过后自动切换。
