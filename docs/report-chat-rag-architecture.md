# 资料 Chat 与 Course 推荐架构

## 访问边界

- 报告 Chat：必须通过 Worker 的 `currentUserFromRequest` 校验，任何已注册且状态正常的账号均可使用。
- Course Chat：除登录校验外，还复用 `courseAccessForUser`；仅剩余有效期至少 30 天的完整会员可读取课程候选。
- 所有响应使用 `private, no-store`，页面脚本不包含模型密钥、R2 对象键或源站定位信息。

## 检索与生成

报告链路是词法 RAG，不让模型直接遍历存储：

1. 刷新任务在发布阶段从已生成的 catalog 构建私有随机访问索引。Worker 不再在请求中下载或解析完整 catalog。
2. 问题被规范为最多 8 个检索 token；英文、数字使用完整 token，中文支持 2、3、4 gram。每个 token 最多保留 48 个按时效、可用状态和机构吸引力预排序的候选 ID，服务端合并后截取最多 12 个候选。
3. 仅将白名单候选字段交给 DeepSeek，以 JSON 形式重排并生成回答。
4. 模型返回的推荐 ID 必须存在于候选白名单；无模型配置或调用失败时使用同一批检索结果生成确定性回退答案。

报告 Chat 的用途是“找报告”，不是在报告全文上问答。请求路径不得加载约 91 MB 的 `search_index.json`，从而避免 Worker 在解析全文索引时超出内存；站内普通全文搜索仍走原有分片/静态链路。

### Report Chat v2 随机访问对象

当前提交指针固定为 `_report-chat/v2/manifest.json`。每个版本写入不可变目录
`_report-chat/v2/releases/<release>/`，包含 `tokens.tbl`、`tokens.dat`、
`items.tbl` 和 `items.dat`。发布器先逐个上传并校验四个不可变对象，最后才覆盖
manifest；任何中途失败都不会让 Worker 看见半套索引。

token 表和 item 表使用相同格式：哈希是 exact UTF-8 key 的 SHA-256 前 8 字节，
按大端无符号数对 bucket 数取模。table 中每个 bucket 是固定 12 字节的
`uint64 offset + uint32 length` 大端槽；Worker 读取一个槽后，仅对 data 对象发出该
bucket 的 range read。bucket payload 是紧凑 JSON entry list，读取后仍必须比较 exact
key，不能把 hash collision 当成命中。

token bucket 映射到候选报告 ID；item bucket 映射到公开候选字段：`id`、中英文标题、
机构、行业、日期、页数、可用状态和吸引力评分。它不包含文件名、源目录、R2 对象键、
下载定位或目录的其他私有字段。manifest 内嵌 12 个默认候选，用于空 token 或没有命中
时的推荐，不依赖特殊 token。一次最多 8 个 token、12 个 item，因此最多 40 次 table /
data range reads；实际空 bucket 或去重候选会更少。

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
- 系统提示明确把问题、历史、标题、目录名和候选内容视为不可信数据；候选数据中的指令不得执行。
- 使用事件只记录候选数量、上下文类型和问题哈希，不记录问题明文。
- 目录候选先经过服务端会员门禁和脱敏，再进入模型；模型输出不能增加候选之外的资料 ID。

## 部署顺序

1. 运行 Worker / 前端自动化测试与语法检查。
2. 推送主分支，使静态构建包含 `assets/report-chat.js` 和两个 Chat 入口。
3. catalog 刷新并完成标题翻译后，运行 `build_report_chat_index.py --upload-r2`。发布器校验不可变对象并最后提交 v2 manifest。
4. 运行私有 Course 目录发布任务；先生成并校验完整目录、兼容 Chat 对象和四个 revisioned
   lookup 对象，最后才原子替换稳定 manifest。任何分片构建、上传或摘要校验失败都保留旧
   manifest，不能让 Worker 看到半套索引。
5. 部署 Portal API Worker，并确认 `DEEPSEEK_API_KEY`、模型配置、R2 binding 与目录脱敏词配置存在。
6. 发布静态站点。
7. 在线验证匿名报告 Chat 为 401、普通注册用户报告 Chat 为 200、无长期会员的 Course Chat 为 403、长期会员 Course Chat 能返回具体目录资料且响应无路径或对象键。
