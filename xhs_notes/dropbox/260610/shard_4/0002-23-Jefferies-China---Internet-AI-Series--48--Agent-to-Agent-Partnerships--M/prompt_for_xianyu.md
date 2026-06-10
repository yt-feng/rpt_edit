你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

【研报解析内容】
"""
## AI Series #48: Agent-to-Agent Partnerships; Models Expand Use-Case Scenario

Highlights (1) Tencent: partnerships across different sectors in Agent-to-Agent (A2A); (2) BABA: Qwen app opens up to third-party Agents and Skill and provides one-stop personalized service to users; (3) Meitu and WPS forms partnerships with former AI design available to WPS users; ; (4) OpenAI is ramping finance and legal agents in Codex after Anthropic in May. (5) OpenRouter: Token consumption was up 13.5% vs prior week

In this report, we provide investors with over 50 data points on token consumption in OpenRouter, pricing for different models, model intelligence in Artificial Analysis, user trends by sub-sector and other industry data for analysis.

Tencent: Building up Agent-to-Agent ecosystem. These include (1) partnership with Meituan's AI assistant Xiaomei and AI Assistant Yuanbao. There will be Agent-to-Agent (A2A) communication when users submit local service requests in Yuanbao; (2) partner with a number of smartphone brands such as OPPO, Xiaomi, Huawei, Vivo and Honor in A2A (Agent to Agent) capabilities. Users can speak with smartphone's built-in AI voice assistant which will help sending Weixin messages or starting Weixin's audio/video calls (vs open Weixin app). Per Tencent Cloud AI Industry Applications Summit (link), Product is one of key areas in AI other than models and frontier tech exploration. Diversified offerings and data insights can further unlock model intelligence in different used cases.

BABA: Qwen app opens up to third-party Agents and Skill with participation of retail brands and airline; Release of Qwen3.7-Plus on 1 Jun. On Agents and Skill, the first batch includes KFC, Luckin, Mixue and China Eastern. We view Qwen app is building agent ecosystem and provides comprehensive personalized services to users. On the other hand, BABA releases Qwen3.7-Plus on 1 Jun post release of Qwen3.7-Max on Alibaba Cloud Summit in May (link). It is a multimodal interactive hybrid agent with unified GUI (Graphical User Interface) / CLI (Command-Line Interface) across visual and text tasks with comprehensive coding agent and productivity offerings with full-modality input. In addition, it has cross-harness generalization under diverse agent frameworks.

Meitu and WPS forms co-operations in office + design. WPS users benefit from using Meitu features in AI posters via text to image/image to image generation, in particular marketing materials for e-commerce merchants. On the other hand, WPS users can also use Meitu in short video generation for live streaming ecommerce.

Kling exceeds 100m global users in Jun-26. This represents a 67% increase from 60m by end of 2025. Number of enterprise customers increased from 30K in 2025 to 50K in Jun-26. It covers 224 countries and regions globally.

Kimi launches AI desktop Kimi Work. Highlights (1) The local agent can run round the clock autonomously; (2) WebBridge enables it to access browsers and complete multi-step tasks; (3) Swarm Intelligence can complete complex problems by using multiple specialized agents and breaking down the tasks into multi-layered tasks simultaneously; (4) it builds for finance sector and pre-integrated with deep data sources across different markets.

OpenAI launches AI tools for finance and legal sectors after Anthropic in May. OpenAI launched 6 new plugins for Codex with specialized skills in finance sector. Plugins for legal sector is under development. This comes after Anthropic launched 10 financial services agent templates in May in areas such as research and client coverage as well as finance and operations

Exhibit 1 - Weekly token consumption over the past 12 months as of 8 Jun (tn)  
![](images/2368a224adae163bee0a7f65b530798a605677b2f6e00187c4b07c0bb143a29c.jpg)

<details>
<summary>bar chart</summary>

| Category | Value |
|---|---|
| 2019 | 1.5 |
| 2020 | 1.6 |
| 2021 | 1.7 |
| 2022 | 1.8 |
| 2023 | 1.9 |
| 2024 | 2.0 |
| 2025 | 2.1 |
| 2026 | 2.2 |
| 2027 | 2.3 |
| 2028 | 2.4 |
| 2029 | 2.5 |
| 2030 | 2.6 |
| 2031 | 2.7 |
| 2032 | 2.8 |
| 2033 | 2.9 |
| 2034 | 3.0 |
| 2035 | 3.1 |
| 2036 | 3.2 |
| 2037 | 3.3 |
| 2038 | 3.4 |
| 2039 | 3.5 |
| 2040 | 3.6 |
| 2041 | 3.7 |
| 2042 | 3.8 |
| 2043 | 3.9 |
| 2044 | 4.0 |
| 2045 | 4.1 |
| 2046 | 4.2 |
| 2047 | 4.3 |
| 2048 | 4.4 |
| 2049 | 4.5 |
| 2050 | 4.6 |
| 2051 | 4.7 |
| 2052 | 4.8 |
| 2053 | 4.9 |
| 2054 | 5.0 |
| 2055 | 5.1 |
| 2056 | 5.2 |
| 2057 | 5.3 |
| 2058 | 5.4 |
| 2059 | 5.5 |
| 2060 | 5.6 |
| 2061 | 5.7 |
| 2062 | 5.8 |
| 2063 | 5.9 |
| 2064 | 6.0 |
| 2065 | 6.1 |
| 2066 | 6.2 |
| 2067 | 6.3 |
| 2068 | 6.4 |
| 2069 | 6.5 |
| 2070 | 6.6 |
| 2071 | 6.7 |
| 2072 | 6.8 |
| 2073 | 6.9 |
| 2074 | 7.0 |
| 2075 | 7.1 |
| 2076 | 7.2 |
| 2077 | 7.3 |
| 2078 | 7.4 |
| 2079 | 7.5 |
| 2080 | 7.6 |
| 2081 | 7.7 |
| 2082 | 7.8 |
| 2083 | 7.9 |
| 2084 | 8.0 |
| 2085 | 8.1 |
| 2086 | 8.2 |
| 2087 | 8.3 |
| 2088 | 8.4 |
| 2089 | 8.5 |
| 2090 | 8.6 |
| 2091 | 8.7 |
| 2092 | 8.8 |
| 2093 | 8.9 |
| 2094 | 9.0 |
| 2095 | 9.1 |
| 2096 | 9.2 |
| 2097 | 9.3 |
| 2098 | 9.4 |
| 2099 | 9.5 |
| 2100 | 9.6 |
| ... (repeated) | ... (repeated)
</details>

Source: OpenRouter, JEF

Exhibit 2 - Top 10 ranking in terms of token consumption by model the latest week

<table><tr><td>No</td><td>Company</td><td>Model</td><td>Tokens</td></tr><tr><td>1</td><td>DeepSeek</td><td>DeepSeek V4 Flash</td><td>3.69T</td></tr><tr><td>2</td><td>Tencent</td><td>Hy3 preview</td><td>2.94T</td></tr><tr><td>3</td><td>MiniMax</td><td>MiniMax M3</td><td>2.5T</td></tr><tr><td>4</td><td>Xiaomi</td><td>MiMo-V2.5</td><td>2.19T</td></tr><tr><td>5</td><td>OpenRouter</td><td>Owl Alpha</td><td>1.95T</td></tr><tr><td>6</td><td>Anthropic</td><td>Claude Sonnet 4.6</td><td>1.76T</td></tr><tr><td>7</td><td>DeepSeek</td><td>DeepSeek V4 Pro</td><td>1.7T</td></tr><tr><td>8</td><td>Anthropic</td><td>Claude Opus 4.7</td><td>1.44T</td></tr><tr><td>9</td><td>DeepSeek</td><td>DeepSeek V3.2</td><td>1.17T</td></tr><tr><td>10</td><td>Anthropic</td><td>Claude Opus 4.8</td><td>1.16T</td></tr></table>

Source: OpenRouter, JEF

Thomas Chong \* | Equity Analyst

852 3743 8016 | thomas.chong@JEF.com

Zoey Zong \* | Equity Analyst

852 3743 8163 | zoey.zong@JEF.com

OpenRouter: Token consumption was up 13.5% vs prior week. Based on analysis of

Continued overleaf ...

the week of 1 Jun (vs the week of 25 May) (Exhibit 1), the number of weekly tokens consumed increased by 13.5% to 36.1tn. In terms of ranking, DeepSeek V4 Flash ranked no 1, followed by Tencent's Hy3 preview and MiniMax M3.

BAT, KC, AI labs and Kling are Beneficiaries. We expect surge in token consumption on rising demand for AI models and agents to benefit CSPs like Baidu, Alibaba, Tencent (BAT), Kingsoft Cloud (KC), AI labs and Kling. According to analysis from Artificial Analysis, (1) there is a narrowing intelligence gap between US and China models; (2) API cost is just a fraction vs US benefiting from MoE, linear attention, and MFU; (3) Coding, Workspace scenario and mid- to long-form content should see significant opportunities ahead (Exhibit 69-73).

## China vs US comparison

## AI Models

According to OpenRouter, token consumption went up significantly in Feb-26 due to (a) a surge in adoption of coding / agents, which allows people using AI from "to chat" to "to work". It connects with large models which can be deployed locally or on servers, which allows you to automate workflow through natural language chat; (b) release of a number of high-performance and cost-efficient models which include Kimi K2.5 (Jan-26), M2.5 (Feb-26) and GLM-5 (Feb-26).

Exhibit 3 - Weekly token consumption over the past 12 months as of 8 Jun (tn)  
![](images/c4cbc21166827415001cc5c50781f5fc57b924eda3062cccfc7a26ddfc1fa7eb.jpg)

<details>
<summary>bar chart</summary>

| Date | Value |
|---|---|
| 3/10/2025 | 1.0 |
| 3/17/2025 | 1.2 |
| 3/24/2025 | 1.5 |
| 3/31/2025 | 1.8 |
| 4/7/2025 | 1.9 |
| 4/14/2025 | 2.0 |
| 4/21/2025 | 2.1 |
| 4/28/2025 | 2.2 |
| 5/5/2025 | 2.3 |
| 5/12/2025 | 2.4 |
| 5/19/2025 | 2.5 |
| 5/26/2025 | 2.6 |
| 6/2/2025 | 2.7 |
| 6/9/2025 | 2.8 |
| 6/16/2025 | 2.9 |
| 6/23/2025 | 3.0 |
| 6/30/2025 | 3.1 |
| 7/7/2025 | 3.2 |
| 7/14/2025 | 3.3 |
| 7/21/2025 | 3.4 |
| 7/28/2025 | 3.5 |
| 8/4/2025 | 3.6 |
| 8/11/2025 | 3.7 |
| 8/18/2025 | 3.8 |
| 8/25/2025 | 4.0 |
| 9/1/2026 | 4.5 |
| 9/8/2025 | 4.8 |
| 9/15/2025 | 5.0 |
| 9/22/2025 | 5.3 |
| 9/29/2025 | 5.5 |
| 10/6/2025 | 5.7 |
| 10/13/2025 | 4.8 |
| 10/20/2025 | 4.9 |
| 10/27/2025 | 5.3 |
| 11/3/2025 | 5.6 |
| 11/10/2025 | 6.0 |
| 11/17/2025 | 6.3 |
| 11/24/2025 | 7.3 |
| 12/1/2026 | 6.1 |
| 12/8/2026 | 5.9 |
| 12/15/2026 | 5.8 |
| 12/22/2026 | 5.7 |
| 12/29/2026 | 6.3 |
| 1/5/2026 | 7.4 |
| 1/12/2026 | 7.7 |
| 1/19/2026 | 8.3 |
| 1/26/2026 | 9.8 |
| 2/2/2026 | 13.3 |
| 2/9/2026 | 14.0 |
| 2/16/2026 | 14.3 |
| 2/23/2026 | 13.8 |
| 3/2/2026 | 14.9 |
| 3/9/2026 | 17.0 |
| 3/16/2026 | 20.3 |
| 3/23/2026 | 23.0 |
| 3/30/2026 | 27.1 |
| 4/6/2026 | 10.8 |
| 4/13/2026 | 10.7 |
| 4/20/2026 | 14.8 |
| 4/27/2026 | 17.8 |
| 5/4/2026 | 19.8 |
| 5/11/2026 | 19.9 |
| 5/18/2026 | 31.8 |
| 5/25/2026 | 36.4 |
| 6/1/2026 | - |
</details>

Source: OpenRouter, JEF  
According to OpenRouter (between 1 and 7 Jun), China models token consumption increased by 27.5% compared to prior week at 14.2tn. This compares to US models at 3.2tn token consumption. DeepSeek V4 Flash weekly token consumptions under rapid growth

According to OpenRouter, rising adoption of Coding / Agents and release of high-performance and cost-efficient China models are driving token consumption

In OpenRouter, China models surpassed US models in terms of token consumption the week of 1 Jun

Exhibit 4 - Market share: weekly token consumption by company as of 8 Jun  
![](images/86353d4f51cf07595e36aea53abad44fc761fc6b36d4e284277cbc57d0baf7e2.jpg)

<details>
<summary>pie chart</summary>

| Category | Value |
|---|---|
| DeepSeek | 35 |
| Anthropic | 28 |
| Google | 25 |
| MiniMax | 20 |
| Xiaomi | 18 |
| Tencent | 16 |
| OpenAI | 14 |
| OpenRouter | 12 |
| Qwen | 10 |
| Others | 27 |
</details>

Source: OpenRouter, JEF

Exhibit 5 - Weekly token consumption since Jan-26 (bn)  
![](images/2a50510c81d2ac0fc98b6dcac69050db2a101ce13ecfad83e9ffaf8a332d1df0.jpg)

<details>
<summary>line chart</summary>

| Date | MiniMax M2.1 | DeepSeek V3.2 | DeepSeek V4 Flash | DeepSeek V4 Pro | MiMo-V2.5 | GLM-5 | Kimi K2.5 | Kimi K2.6 | MiniMax M2.5 | MiniMax M2.7 | MiniMax M3 | MinMo-V2.5-Pro | Hy3 Preview |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5-Jan |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 12-Jan |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 19-Jan |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 26-Jan |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 2-Feb |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 9-Feb |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 16-Feb |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 23-Feb |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 2-Mar |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 9-Mar |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 16-Mar |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 23-Mar |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 30-Mar |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 6-Apr |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 13-Apr |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 20-Apr |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 27-Apr |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 4-May |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 11-May |  |  |  |  |  |  |  |  |  |  |  |  |  |
</details>

Source: OpenRouter, JEF

On token consumption by company, DeepSeek (18.7%) comes first, followed by Anthropic (14.6%), Google (11.9%), MiniMax (8.4%) and Xiaomi (8.2%). The top 5 in weekly token consumption by model are DeepSeek V4 Flash (3.69tn), Hy3 preview (2.94tn), MiniMax M3 (2.5tn), followed by MiMo V2.5 (2.19tn) and Owl Alpha (1.95tn).

DeepSeek V4 Flash ranked first in terms of token consumption the week of 1 Jun

Exhibit 6 - Top 10 ranking in terms of token consumption by model the latest week

<table><tr><td>No</td><td>Company</td><td>Model</td><td>Tokens</td></tr><tr><td>1</td><td>DeepSeek</td><td>DeepSeek V4 Flash</td><td>3.69T</td></tr><tr><td>2</td><td>Tencent</td><td>Hy3 preview</td><td>2.94T</td></tr><tr><td>3</td><td>MiniMax</td><td>MiniMax M3</td><td>2.5T</td></tr><tr><td>4</td><td>Xiaomi</td><td>MiMo-V2.5</td><td>2.19T</td></tr><tr><td>5</td><td>OpenRouter</td><td>Owl Alpha</td><td>1.95T</td></tr><tr><td>6</td><td>Anthropic</td><td>Claude Sonnet 4.6</td><td>1.76T</td></tr><tr><td>7</td><td>DeepSeek</td><td>DeepSeek V4 Pro</td><td>1.7T</td></tr><tr><td>8</td><td>Anthropic</td><td>Claude Opus 4.7</td><td>1.44T</td></tr><tr><td>9</td><td>DeepSeek</td><td>DeepSeek V3.2</td><td>1.17T</td></tr><tr><td>10</td><td>Anthropic</td><td>Claude Opus 4.8</td><td>1.16T</td></tr></table>

Source: OpenRouter, JEF

Based on Artificial Analysis, China models DeepSeek, Qwen, Kimi, MiniMax and Zhipu are closing the gap with US models in terms of intelligence. China models are highly cost-efficient on Mixture of Experts (MoE) architecture, linear attention, and MLU (Model Flog Utilization). According to 2026 Stanford AI Index Report (Apr-26), the top US model leads Chinese models by 2.7%. Separately, Anthropic (1503), xAI (1495), Google (1494), OpenAI (1481), Alibaba (1449) and DeepSeek (1424) occupy the top tier of Arena Elo ratings as of Mar-26.

Exhibit 7 - No 11-20 ranking in terms of token consumption by model in latest week

<table><tr><td>No</td><td>Company</td><td>Model</td><td>Tokens</td></tr><tr><td>11</td><td>Google</td><td>Gemini 3 Flash Preview</td><td>1.05T</td></tr><tr><td>12</td><td>StepFun</td><td>Step3.7 Flash</td><td>810B</td></tr><tr><td>13</td><td>Xiaomi</td><td>Mimo-V2.5-Pro</td><td>674B</td></tr><tr><td>14</td><td>Google</td><td>Gemini 2.5 Flash</td><td>631B</td></tr><tr><td>15</td><td>Google</td><td>Gemini 2.5 Flash Lite</td><td>594B</td></tr><tr><td>16</td><td>Poolside</td><td>Laguna M.1 (free)</td><td>568B</td></tr><tr><td>17</td><td>NVIDIA</td><td>Nemotron 3 Super (free)</td><td>534B</td></tr><tr><td>18</td><td>Google</td><td>Gemini 3.5 Flash</td><td>487B</td></tr><tr><td>19</td><td>Anthropic</td><td>Claude Opus 4.6</td><td>458B</td></tr><tr><td>20</td><td>OpenAI</td><td>GPT-5.5</td><td>443B</td></tr></table>

Source: OpenRouter, JEF

China models are narrowing the gap with US models in terms of intelligence. On Input/Output API, China large models are highly efficient vs US models.

Exhibit 8 - Cache hit/Input/Output API price for leading models as of 8 Jun  
![](images/b10b62d6c17eddd6605d8d541d9a23b7f02209417541a7ff963386f7e3bd5dcf.jpg)

<details>
<summary>bar chart</summary>

| Model | Cache Hit | Input | Output |
|---|---|---|---|
| GPT-cas-2GB (high) | 0.05 | 0.2 | 0.01 |
| DeltaSeek V4 Flash(Max) | 0.04 | 0.28 | 0.15 |
| GPT-cas-72GB1 (high) | 0.06 | 0.28 | 0.15 |
| DeltaSeek V4 F3 (max) | 0.09 | 0.24 | 0.07 |
| MiniMax-M3 | 0.08 | 0.12 | 0.18 |
| MiniMax-M2.7 | 0.06 | 0.12 | 0.08 |
| Qwen3.5 39TB R1TB | 0.05 | 0.18 | 0.36 |
| GLM-5 | 0.1 | 0.2 | 0.2 |
| Kinn-KJ.6 | 0.16 | 0.054 | 0.2 |
| GPT-5.4 min (kHigh) | 0.09 | 0.18 | 0.45 |
| GLM-5.1 | 0.26 | 0.44 | 0.1 |
| Clavide 4.5 Taku | 0.1 | 0.26 | 0.6 |
| Qwen3.7 Max | 0.25 | 0.25 | 7.5 |
| Gemini 3.5 Fast | 0.16 | 0.15 | 9 |
| Novo 2.0 Pro Preview (medium) | 0.19 | 0.25 | 10 |
| Gemini 31 Pro Preview | 0.22 | 0.2 | 2 |
| Clavide Spreeer 4.61 (max) | 0.3 | 0.375 | 15 |
| Clavide Optus 4 (max) | 0.5 | 0.35 | 25 |
| Clavide Optus 4.8 (max) | 0.5 | 0.325 | 25 |
| GPT-5.1(kHigh) | 0.5 | 0.6 | 30 |
Artificial Analysis
</details>

Source: Artificial Analysis, JEF

In terms of Input/Output API price, China models are just a fraction vs US models.

Exhibit 9 - Intelligence index for top 20 models as of 8 Jun  
![](images/322b887a846a7fce5a1fe7ba348df8c99ae

[中间内容因长度限制已省略]

the recipient based on this report is consistent with a recipient's investment objectives, portfolio holdings, strategy, financial situation, or needs.

By providing this report, neither JRS nor any other JEF entity accepts any authority, discretion, or control over the management of the recipient's assets. Any action taken by the recipient of this report, based on the information in the report, is at the recipient's sole judgment and risk. The recipient must perform his or her own independent review of any prospective investment. If the recipient uses the services of JEF LLC (or other affiliated broker-dealers), in connection with a purchase or sale of a security that is a subject of these materials, such broker-dealer may act as principal for its own accounts or as agent for another person. Only JRS is registered with the SEC as an investment adviser; and therefore neither JEF LLC nor any other JEF affiliate has any fiduciary duty in connection with distribution of these reports.

The price and value of the investments referred to herein and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

This report may contain forward looking statements that may be affected by inaccurate assumptions or by known or unknown risks, uncertainties, and other important factors. As a result, the actual results, events, performance or achievements of the financial product may be materially different from those expressed or implied in such statements.

This report has been prepared independently of any issuer of securities mentioned herein and not as agent of any issuer of securities. No Equity Research personnel have authority whatsoever to make any representations or warranty on behalf of the issuer(s). Any comments or statements made herein are those of the JEF entity producing this report and may differ from the views of other JEF entities.

This report may contain information obtained from third parties, including ratings from credit ratings agencies such as Standard & Poor's, and information derived from third-party or proprietary generative artificial intelligence (Gen AI) models. JEF does not guarantee the accuracy, completeness, timeliness or availability of this information, and is not responsible for any errors or omissions (negligent or otherwise), regardless of the cause, or for the results obtained from the use of such content. Neither JEF nor any third-party content providers, including providers of Gen AI models, give any express or implied warranties, including, but not limited to, any warranties of merchantability or fitness for a particular purpose or use. Neither JEF nor any third-party content provider shall be liable for any direct, indirect, incidental, exemplary, compensatory, punitive, special or consequential damages, costs, expenses, legal fees, or losses (including lost income or profits and opportunity costs) in connection with any use of their content, including ratings. Credit ratings are statements of opinions and are not statements of fact or recommendations to purchase, hold or sell securities. They do not address the suitability of securities or the suitability of securities for investment purposes, and should not be relied on as investment advice. Reproduction and distribution of third party content in any form is prohibited except with the prior written permission of the related third party.

JEF reports are disseminated and available electronically, and, in some cases, also in printed form. Electronic research is simultaneously made available to all clients. This report or any portion hereof may not be copied, reprinted, sold, or redistributed or disclosed by the recipient or any third party, by content scraping or extraction, automated processing, or any other form or means, without the prior written consent of JEF. Any unauthorized use is prohibited. Neither JEF nor any of its respective directors, officers or employees, is responsible for guaranteeing the financial success of any investment, or accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this report or its contents. Nothing herein shall be construed to waive any liability JEF has under applicable U.S. federal or state securities laws.

For Important Disclosure information relating to JRS, please see https://adviserinfo.sec.gov/IAPD/Content/Common/crd\_iapd\_Brochure.aspx?BRCHR\_VRSN\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://javatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.

© 2026 JEF
"""
