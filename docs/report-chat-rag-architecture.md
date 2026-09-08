# 研究型 RAG 与 Course 推荐架构

## 访问边界

- 报告 Chat 同时支持匿名访客和登录账号。匿名身份只使用服务端 HMAC 后的设备标识，原始
  `visitor_id` 不写入归档或分析；登录后以账号为唯一额度主体。
- 每个匿名设备与每个没有有效会员权益的注册账号各可研究 1 次；有效权益原始期限不足 2 个月的
  普通会员按北京时间每天 2 次；原始期限达到 2 个月的会员每天 5 次；super 管理员不限次。
- 公开热门问题读取管理员已经发布的精确快照，不调用模型，也不占用上述额度。
- Course Chat：除登录校验外，还复用 `courseAccessForUser`；仅剩余有效期至少 30 天的完整会员可读取课程候选。
- 所有响应使用 `private, no-store`，页面脚本不包含模型密钥、R2 对象键或源站定位信息。

## 报告研究检索与生成

独立 `/research.html` 页面和导航“研究”入口提供跨报告研究型 RAG；首页保留快捷入口：

1. 独立研究刷新工作流读取现行报告搜索正文和已解析历史正文，`build_report_research_index.py` 把合格正文切成约
   2,600 字、带 260 字重叠的证据块，并构建私有 token、报告与 evidence 三张随机访问表。
2. 额度占位成功后，Worker 先用一次小型 DeepSeek query planner 把当前问题拆成 `core`
   concept groups、research `facets` 与最多 7 个原子检索词；planner 失败时使用相同结构的
   deterministic fallback。检索词按 concept group round-robin 分配，先覆盖不同概念再取
   同义词；AI / artificial / intelligence 属于同组，只贡献 1 票，裸年份、日期和纯数字不
   能成为主题准入词。deterministic fallback 只保留问题中的完整残余实体，不把中文 2–4 字
   滑窗碎片提升为 core，因此“比较全球”等句式片段不会挤占 7 个检索槽。
3. 每个 token 最多返回 192 个 posting。先按必要主题覆盖度、facet 覆盖度和组内最优分数排序。
   posting 名单截断造成的漏召回允许从候选并集补足，但缺失的必要主题必须同时在报告标题与
   取回的证据上下文中验证；所有候选还需在真实标题/正文中命中必要主题及至少一个所问 facet。
   新索引用 datacenter 统一 data center / data-centre / 数据中心，优先其对应证据块，
   不把临床或市场数据中的泛词 data 当成数据中心；老索引仍可兼容读取。planner 的额外优选词只作 facet，不会意外变成必须满足的主题。Worker 最多
   读取 4 份报告、总计 6 个证据块：先按排名给每份报告 1 块，再
   给前两名（或下一份仍有第 2 块的报告）补第 2 块。请求路径不会下载或解析整份全文索引。
4. planner、研究随机读取、Chart index 和生成模型共用单请求 38 次子请求账本。完整冷路径为
   7 token、4 item、6 evidence、1 Chart index、1 planner、1 synthesis；登录 token 校验只读
   已有用户索引，不再在每个 API 请求里重写三份身份索引。研究在 posting 阶段早 miss 时，
   discovery fallback 最多只查 3 个词、返回 4 个 item；已经读取 item/evidence 后的 partial
   miss（包括 item/evidence 的单次读取异常）不再级联第二套索引，而是保留可验证部分并明确
   返回“证据不足”的研究结果。
5. Worker 只把白名单报告元数据、证据块和严格相关的 Charts 交给 DeepSeek。synthesis 的
   `max_tokens` 上限为 7,000、服务端窗口 52 秒；提示要求研究标题、研究范围、结构化长摘要、
   有证据时约 1,800–2,600 字的分析正文、5–8 条分段 findings、6–12 个 data points、来源 ID、Chart image ID 与后续问题，
   证据不足时必须少写，不能填充。
6. 服务端再次校验所有来源 ID 和 Chart ID。数字校验按句/分句执行：一句里只要有不能在所引
   evidence 中逐字找到的数字，就删除整句而不是删除整条 finding；同一 finding 中其他有根据
   的句子继续保留。data point 仍按整项校验。模型不能增加未检索到的报告、图表或数字。
7. Chart 候选使用 planner 的完整 concept terms。无论是否来自已选报告，Chart 自身都必须命中
   全部 required core，并在问题存在 facet 时至少命中一个 facet；报告标题只用于无 required core
   的旧数据辅助判断，不能替一张仅含“AI + capex”的图补齐 data center。只命中泛化 AI、
   年份或无关实体的图不会入选；每份报告最多 2 张、总计最多 6 张。最终响应严格采用模型返回
   的数组型 `chart_image_ids` 白名单顺序；字段缺失、类型错误或 ID 不在候选白名单时返回空图表，
   不再把全部候选无条件塞入结果。
8. 全文没有命中、证据读取部分失败或研究 manifest 不可用时，同一次请求仍会查询独立的
   Charts 索引。满足主题与质量条件的图表以 `chart_metadata` 证据参与综合，不把图表提取
   内容冒充报告全文。独立图表报告加入来源白名单，因此不要求它必须是前四份正文报告之一。
   没有 catalog `report_id` 的真实图表使用 `chart:<image_id>` 独立来源，不制造报告 ID；
   来源链接为 `/charts.html?image=<image_id>`。Charts 页面按确切图像 ID 打开；静态索引
   滞后时经 `/api/charts?image=<image_id>` 查询私有索引中实际存在的公开图表元数据。
   若正文和 Charts 都没有合格证据，才走原报告发现 fallback。
9. 前端把摘要、发现、数据、Charts 和来源报告链接组合成一份研究材料。研究响应同时带安全的
   `research_title`、`research_scope` 与服务端 `generated_at`。服务端根据实际正文证据块与图表数量生成研究范围；仅命中图表时明确说明未命中报告正文。

当前 provenance 精度是“报告 + evidence chunk”或“真实图像 ID + 已识别图表内容”。现有搜索正文已被扁平化，没有可靠页码，
因此界面不生成虚假页码；未来只有在解析层保存 page/figure 坐标后才增加页级引用。

### 正文覆盖与历史节选边界

- catalog 是资料目录，并不代表每条都有已解析正文。当前正文输入只来自 `search_index.json` 中匹配 catalog ID、长度至少 1,000 字符的报告正文；附加的 `[[CHART_SEARCH_V1]]` 图表描述会被剥离，仍由独立 Charts 通道检索。
- `--history-catalog-path` 与 `--history-text-dir` 复用站点现有 `merge_history_catalog` 标题去重和 ID remap，直接读取已经解析的历史 gzip 文本，无需重新下载或解析 PDF。也可用 `--history-index-path` 传入已完成 ID 对齐的历史 items 索引。
- 历史导入最多保留每条 10,000 字符，且没有逐条完整性证明，因此全部保守标为 `partial_excerpt=true`、`text_scope=partial_excerpt`，不称完整全文。范围标识贯穿持久语料、item/evidence、Worker、界面和 Word/PDF；模型同样收到节选限制。
- 当前合格的完整提取优先于历史节选；重复正文保留较完整候选。短标题或不足 1,000 字符的历史文本不会进入证据。历史节选不能覆盖已保存的完整正文，后续正常刷新不会因公开搜索窗缩小而删除稳定语料。
- 其他报告、报告线索、高权报告和国际智库的实时搜索适配器，以及 `_search-mirror` 元数据缓存，没有整体接入研究正文。下载到 PDF、出现在目录或搜索结果中也不等于已经解析并入库。Charts 覆盖与正文覆盖分别计算。
- 本地 2026-08-30 输入快照的历史库有 5,488 条已解析文本；站点去重后 5,480 条。严格目录 ID 与长度校验后的实际本地构建为 6,285 份资料（964 份当前正文、5,321 份历史节选）和 96,431 个证据块。此构建未合并或发布生产稳定语料，生产新增量须以专用工作流的实际去重结果为准。


### 新闻与近期事件补充

- 前端报告研究请求 `include_news=true`。后台 `research-news-refresh.yml` 每小时从 GDELT GAL
  最近 75 分钟的分钟文件采集发布者自带简介，合并最近七天的私有 R2 快照。最多六路并发，
  每次下载/解压受字节上限约束；只保留符合主题的中英文真实简介、HTTPS 来源，按 URL 去重。
  单快照最多 1,800 条 / 2 MiB；没有新合格记录时不覆盖现有快照，写入后回读验证。
- Worker 只用一次有预算的 R2 读取查询摘要快照；本次最多四条新闻，并限制同一媒体重复。
  必要主题必须匹配。摘要不足时，可在剩余额度允许时读取 EIA Today in Energy 和 Federal
  Reserve FEDS Notes 两个固定官方 RSS；并行截止时间不超过六秒，合计响应不超过 512 KiB。
  新闻失败或缺失仍继续已有报告/图表研究，研究范围明确没有引用近期新闻。
- `news_description` 仅指 GAL 发布者简介，`news_snippet` 仅指官方 RSS 摘要，均非新闻全文。
  `observed_at` 不冒充发布时间，只有官方明确给出的 `pubDate` 写入 `published_at`。原文和
  图片不会被自动抓取或打包。每条新闻用 `news:<URL SHA-256>` 引用，页面和 Word/PDF 保留
  原文链接及 GDELT 署名；新闻数量不会计入报告正文覆盖数。
- 38 次预算仍包括新闻读取，正文 evidence 数量按剩余额度动态缩减，至少预留 Chart 与生成
  调用。综合要求分别说明事实、证据推论、条件情景，把最新事件与报告判断比较；正文段落
  从生成、公共响应清理到导出均保留，数字和引用白名单校验继续生效。
- GDELT DOC/Context 实时 API 本次未取得可验证响应，没有上线猜测 JSON 字段的解析器。
  GAL 的真实字段已核验；官方文档：
  https://blog.gdeltproject.org/announcing-the-gdelt-article-list-rss-feed/ 。

### 研究结果导出

- Word 下载直接复用已经返回并通过服务端白名单校验的研究 JSON，不再次请求模型，也不消耗
  研究额度。前端生成真实 OOXML `.docx`，把相关 Chart 作为 JPEG 嵌入文档，并把来源写成
  可点击的当前站点 `/report.html?id=...` 链接；无报告关联的图表使用精确图表链接；文件名不包含原始问题，正文可保留研究问题；导出包不含账号、归档 ID、
  R2 对象键或报告原 PDF。
- PDF 使用同一份规范化研究数据直接生成可下载的 A4 PDF 二进制文件，保留可搜索、可复制
  的中文正文、内嵌 JPEG 图表和可点击来源链接，不再打开打印对话框。仅点击导出时懒加载
  同站点固定版本的 pdf-lib、fontkit 与 TrueType 中文字体；图表与研究数据不送第三方。
  完整嵌入字体解决 CJK 子集丢字问题，典型图文 PDF 约 6.5 MB；首次字体下载约 10.6 MB。
  资源失败、图像格式错误、权限变化和超时均显示可重试错误，不生成缺图的成功文件。
- Chart 只有在 `source_id`（有报告关联时等于 `report_id`）与 finding 的 `source_ids`
  精确一致时才嵌入该结论；未匹配 Chart
  统一放入“补充图表证据”，不能通过数组顺序或泛化关键词伪装成某条结论的直接证据。
- 热门问题的公开缓存使用相同导出器，因此点击历史快照后同样可以导出，且不会重新触发
  R2 evidence 检索、DeepSeek 或额度占用。

### Report Research v1 随机访问对象

稳定提交指针是 `_report-research/v1/manifest.json`。每个内容版本位于不可变目录
`_report-research/v1/releases/<release>/`，包含 token、item、evidence 各自的 table/data
对象。table 槽为 12 字节 `uint64 offset + uint32 length`；exact UTF-8 key 以 SHA-256
前 8 字节映射 bucket，range read 后仍比较 exact key，不能把哈希碰撞当成命中。单 bucket
最多 128 KiB；整个 data 对象可以大于 128 MiB，因为 Worker 永远只读取目标 range。

token value 包含报告 ID、词频和相关 chunk ID；item value 只含公开报告字段；evidence
value 包含 `report_id`、chunk ID、正文与 `partial_excerpt` / `text_scope` 范围标识。索引不包含文件名、私有路径、PDF/R2 对象键或
上游定位信息。

每个 release 还保存一份确定性 gzip JSONL 研究语料。下一轮发布先从当前 manifest 读取并
校验这份稳定语料，再按 `report_id` 合并本轮正文：本轮有合格正文时覆盖，当前公开搜索窗口
未再包含的旧报告与旧正文继续保留。因此 GitHub 仓库清理、Actions 临时 artifact 到期或公开
全文搜索窗口收缩，都不会让已经纳入研究索引的报告从私有证据库消失。语料同样只允许公开
报告字段与正文，并用 SHA-256、压缩/解压字节数和条目数校验；损坏或缺失时在任何上传前停止。
发布器先上传并校验语料与六个不可变索引对象，最后才替换 manifest。

原 `_report-chat/v2/manifest.json` 及其 token/item 随机访问表继续作为无全文命中或研究索引
不可用时的报告发现 fallback；它不再是首页报告入口的目标产品形态。

Course 链路不读取约四万行的完整会员目录，也不在冷启动时解析 1.5 MiB 左右的整份
Chat JSON。发布任务先从已脱敏、已按字段白名单重建的 `safe_items` 派生候选集合：
所有带公开机构标签的行无条件保留，每门课程再按原始顺序保留最多 30 个不带机构标签的
中性代表条目。候选必须覆盖全部 44 门课程，并受 5,000 行、2 MiB 的双重硬上限约束。
随后发布任务在私有 R2 中构建 v2 direct-bucket 索引；完整目录仍只供会员目录浏览 API
使用，v1 JSON 只作为回滚兼容对象保留。

稳定入口是 `_course-directory/v2/chat-lookup/manifest.json`。manifest 指向一个带内容摘要
revision 的 token table/data 与 item table/data。table 每槽固定 12 字节：8 字节大端
offset 加 4 字节大端 length；槽号为 exact UTF-8 key 的 SHA-256 前 8 字节大端整数对
bucket 数取模。bucket data 是 compact JSON collision list，读取后还必须比对 exact key，
不能把哈希命中直接当作命中。问题最多取 8 个 NFKC、小写化后的拉丁词或 2/3/4 字中文
gram，每个词只读取一个 table range 和一个 data range；最多 12 个候选 ID 再各读取一组
item ranges。manifest 缓存后，单次推荐最多 40 次小范围读取，不再解析整个索引。

token posting 在发布时按机构吸引力、资料类型、日期和稳定标题顺序预排。知名投行、律所
与监管机构的具体资料仍在相关查询和 manifest 的 12 条安全默认候选中优先；44 门课程的
候选仍全部存在于 item index。manifest 及所有 bucket 只允许包含原脱敏行的字段，不增加
路径、对象键、上游来源或品牌映射。

Course Chat 仅返回具体资料标题、主题、文件类型、公开机构标签、日期和大小。知名投行、
律所与监管机构在相关度相当时获得更高吸引力评分。推荐卡可把具体标题回填到会员目录
搜索框。Chat 索引不包含完整目录白名单之外的字段，也不能新增源路径、对象键或品牌字段。

## 检索覆盖边界

- 标题目录可发现的报告数量不等于正文研究覆盖数量。研究正文来自已匹配报告的 MinerU
  `source_mineru.md` 及持久化历史语料；银行目录抓取只贡献标题，默认不足 1000 字不会
  进入正文证据库。未解析 PDF、仅目录标题、博客与独立 Course 会员目录不等于已纳入正文。
- 图表来自独立图像提取与视觉分析索引；目前是图表识别内容和指标供综合模型使用，图像
  原件用于结果展示与导出。此过程不意味着综合模型重新逐页阅读所有原 PDF。
- 私有研究与 Charts 索引、公开静态 Charts 列表有各自发布时间，核对覆盖数量时必须标注
  各自更新时间。新图的引用深链支持精确 API 回补，避免静态列表滞后导致来源打不开。

## 防滥用与提示注入

- 请求体最多 16 KB，问题限制 600 字，对话历史最多 6 条；只接受 `user` / `assistant` 角色。
- Report Chat 在读取证据或调用模型前用 R2 ETag 条件写原子占位，避免并发请求同时产生模型
  调用；下游检索、模型或归档失败会原子归还该次额度。Course Chat 保留原有独立的账号日
  额度，不与首页研究额度混用。
- 达到首页研究额度后，用户可以用该次限额归档的 `archive_id` 提交继续研究申请。服务端校验
  归档归属并固定发送到服务端 `CONTACT_EMAIL`，不接受浏览器指定收件人。
- 系统提示明确把问题、历史、标题、正文证据、图表描述和目录名视为不可信数据；其中的指令不得执行。
- 每次成功、失败、限额命中和公开缓存读取都有私有问答归档；管理后台仅向 super 管理员展示。
  管理员可把一条优质归档发布为热门问题，也可撤下；公开快照只含安全研究结果和来源字段，
  不含账号、邮箱、设备标识、内部路径或对象键。
- 服务端使用事件记录额度层级、结果模式、候选/来源/Chart 数量、缓存状态、耗时和问题哈希；
  前端另记录热门曝光/点击、提交、失败、限额申请等交互。分析事件不记录问题明文，RAG
  交互中的匿名设备 ID 也会在服务端 HMAC 后才写入主、副分析存档。
- 报告研究输出的来源与 Chart ID 必须通过服务端白名单；数字还需通过对应 evidence 文本逐句
  校验，不能通过简单删掉数字而保留原句语义。
- 课程候选先经过服务端会员门禁和脱敏，再进入模型；模型输出不能增加候选之外的资料 ID。

## 部署顺序

1. 运行 Worker / 前端自动化测试与语法检查。
2. 推送主分支，使静态构建包含 `assets/report-chat.js`、独立研究页 `/research.html`、导航研究入口及 Course Chat。
3. catalog 刷新并完成标题翻译后，运行 `build_report_chat_index.py --upload-r2`，保留报告发现 fallback。
4. 静态发布完成后，运行独立 `Portal research index refresh` 工作流。手动默认 `publish=false` 只构建核查；
   `publish=true` 才发布。启用 `PORTAL_RESEARCH_REFRESH_ENABLED=true` 后，成功的主分支静态刷新自动触发。
   工作流读取现行 catalog/search_index，并合并仓库中 history_catalog/history_text 与 R2 稳定语料；
   使用现有 `--merge-r2-corpus --upload-r2` 原子发布契约，稳定语料与六个不可变对象全部校验后才提交 manifest。
   研究刷新与静态发布共用生产串行锁，但不属于 neutral-edge-cutover 事务。
5. 运行私有 Course 目录发布任务；先生成并校验完整目录、兼容 Chat 对象和四个 revisioned
   lookup 对象，最后才原子替换稳定 manifest。任何分片构建、上传或摘要校验失败都保留旧
   manifest，不能让 Worker 看到半套索引。
6. 部署 Portal API Worker，并确认 `DEEPSEEK_API_KEY`、模型配置、R2 binding 与目录脱敏词配置存在。
7. 发布静态站点。
8. 在线验证匿名访客第 1 次成功、第 2 次返回额度申请入口，普通会员和高阶会员分别显示
   2/5 次额度，super 管理员不限次；同时验证热门问题不调用模型、来源与 Chart 均可打开、
   响应无路径或对象键。Course Chat 仍验证无长期会员为 403、长期会员正常。
