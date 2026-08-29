# 研究型 RAG 与 Course 推荐架构

## 访问边界

- 报告 Chat：必须通过 Worker 的 `currentUserFromRequest` 校验，任何已注册且状态正常的账号均可使用。
- Course Chat：除登录校验外，还复用 `courseAccessForUser`；仅剩余有效期至少 30 天的完整会员可读取课程候选。
- 所有响应使用 `private, no-store`，页面脚本不包含模型密钥、R2 对象键或源站定位信息。

## 报告研究检索与生成

首页报告入口是跨报告研究型 RAG，不再只做标题推荐：

1. 静态发布生成全文搜索数据后，`build_report_research_index.py` 把有正文的报告切成约
   1,800 字、带 180 字重叠的证据块，并构建私有 token、报告与 evidence 三张随机访问表。
2. 查询先做 NFKC 规范化、中英文领域词扩展与全文 token 检索。每个 token 最多返回 48 个
   posting，Worker 交叉排序后读取最多 4 份报告、每份 1 个最相关证据块；请求路径不会
   下载或解析整份全文索引。
3. Worker 只把白名单报告元数据、证据块和这些报告名下的历史 Charts 交给 DeepSeek，要求
   返回结构化研究摘要、主要发现、关键数据、来源 ID、Chart image ID 与后续研究问题。
4. 服务端再次校验所有来源 ID 和 Chart ID；带数字的摘要、发现或数据点还必须能在对应
   正文证据中找到同一数值，否则丢弃。模型不能增加未检索到的报告、图表或数字。
5. 前端把摘要、发现、数据、Charts 和来源报告链接组合成一份研究材料。若研究索引尚未
   发布或查询没有全文命中，则回退到原有 Report Chat v2 的“找报告”结果，不伪装成全文研究。

当前 provenance 精度是“报告 + evidence chunk”。现有搜索正文已被扁平化，没有可靠页码，
因此界面不生成虚假页码；未来只有在解析层保存 page/figure 坐标后才增加页级引用。

### Report Research v1 随机访问对象

稳定提交指针是 `_report-research/v1/manifest.json`。每个内容版本位于不可变目录
`_report-research/v1/releases/<release>/`，包含 token、item、evidence 各自的 table/data
对象。table 槽为 12 字节 `uint64 offset + uint32 length`；exact UTF-8 key 以 SHA-256
前 8 字节映射 bucket，range read 后仍比较 exact key，不能把哈希碰撞当成命中。单 bucket
最多 128 KiB；整个 data 对象可以大于 128 MiB，因为 Worker 永远只读取目标 range。

token value 包含报告 ID、词频和相关 chunk ID；item value 只含公开报告字段；evidence
value 只含 `report_id`、chunk ID 与正文。索引不包含文件名、私有路径、PDF/R2 对象键或
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
中性代表条目。候选必须覆盖全部 43 门课程，并受 5,000 行、2 MiB 的双重硬上限约束。
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
与监管机构的具体资料仍在相关查询和 manifest 的 12 条安全默认候选中优先；43 门课程的
候选仍全部存在于 item index。manifest 及所有 bucket 只允许包含原脱敏行的字段，不增加
路径、对象键、上游来源或品牌映射。

Course Chat 仅返回具体资料标题、主题、文件类型、公开机构标签、日期和大小。知名投行、
律所与监管机构在相关度相当时获得更高吸引力评分。推荐卡可把具体标题回填到会员目录
搜索框。Chat 索引不包含完整目录白名单之外的字段，也不能新增源路径、对象键或品牌字段。

## 防滥用与提示注入

- 请求体最多 16 KB，问题限制 600 字，对话历史最多 6 条；只接受 `user` / `assistant` 角色。
- 每个账号按北京时间每天最多 30 次，计数使用 R2 ETag 条件写，避免并发绕过。
- 系统提示明确把问题、历史、标题、正文证据、图表描述和目录名视为不可信数据；其中的指令不得执行。
- 使用事件只记录候选数量、上下文类型和问题哈希，不记录问题明文。
- 报告研究输出的来源与 Chart ID 必须通过服务端白名单；数字还需通过对应 evidence 文本校验。
- 课程候选先经过服务端会员门禁和脱敏，再进入模型；模型输出不能增加候选之外的资料 ID。

## 部署顺序

1. 运行 Worker / 前端自动化测试与语法检查。
2. 推送主分支，使静态构建包含 `assets/report-chat.js` 和两个 Chat 入口。
3. catalog 刷新并完成标题翻译后，运行 `build_report_chat_index.py --upload-r2`，保留报告发现 fallback。
4. 静态全文构建完成后，运行 `build_report_research_index.py --merge-r2-corpus --upload-r2`；
   稳定语料与六个不可变对象全部上传并校验后才提交 `_report-research/v1/manifest.json`。
5. 运行私有 Course 目录发布任务；先生成并校验完整目录、兼容 Chat 对象和四个 revisioned
   lookup 对象，最后才原子替换稳定 manifest。任何分片构建、上传或摘要校验失败都保留旧
   manifest，不能让 Worker 看到半套索引。
6. 部署 Portal API Worker，并确认 `DEEPSEEK_API_KEY`、模型配置、R2 binding 与目录脱敏词配置存在。
7. 发布静态站点。
8. 在线验证匿名报告研究为 401、普通注册用户能收到 `mode=research`、来源与 Chart 均可打开、
   响应无路径或对象键；同时验证无长期会员的 Course Chat 为 403、长期会员 Course Chat 正常。
