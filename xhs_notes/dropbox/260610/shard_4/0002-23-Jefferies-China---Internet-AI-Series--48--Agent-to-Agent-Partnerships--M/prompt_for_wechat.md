你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`JEF`。标题格式建议：`# JEF：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份JEF研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

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
![](images/322b887a846a7fce5a1fe7ba348df8c99aed726f03e33084b9f6cbae5571955f.jpg)

<details>
<summary>bar chart</summary>

| Model | Proprietary | Open Weights | Open Weights (Commercial Use Restricted) |
|---|---|---|---|
| Claude Opus 48 (max) | 61 | 0 | 0 |
| GPT-5.5 (xhigh) | 60 | 0 | 0 |
| Claude Opus 4.7 (max) | 57 | 0 | 0 |
| Gemini 3.1 Pro Preview | 57 | 0 | 0 |
| Qwen3.7 Max | 56 | 0 | 0 |
| Gemini 3.5 Flash | 55 | 0 | 0 |
| MiniMax-M3 | 54 | 0 | 0 |
| Kim K2.6 | 54 | 0 | 0 |
| MiMo-V2.5-Pro | 53 | 0 | 0 |
| Grok 4.3 (high) | 52 | 0 | 0 |
| Muse Spark | 51 | 0 | 0 |
| Claude Sonnet 46 (max) | 51 | 0 | 0 |
| DeepSeek V4 Pro (Max) | 51 | 0 | 0 |
| GLM-5.1 | 51 | 0 | 0 |
| MiniMax-M2.7 | 49 | 0 | 0 |
| GPT-5.4 mini (xhigh) | 49 | 0 | 0 |
| Nenotron 3 Ultra | 47 | 0 | 0 |
| DeepSeek V4 Flash (Max) | 46 | 0 | 0 |
| Qwen3.5 S97BA17B | 45 | 0 | 0 |
| Mistral Medium 3.5 | 39 | 0 | 0 |
</details>

Source: Artificial Analysis, JEF

Among top 20 large models, there are 9 which are China models and open weighted as of 1 Jun.

Exhibit 10 - Frontier Language Model Intelligence over time as of 8 Jun  
![](images/a9b9621621f1f98f302fabdc4393c08b7abf3acd1924b50a428e8f749cc5a053.jpg)

<details>
<summary>line chart</summary>

| Release Date | Google | Anthropic | DeepSeek | MiniMax | Kimi | Alibaba | Z AI |
| ------------ | ------ | --------- | -------- | ------- | ---- | ------- | ---- |
| Mar 23       | 5      | 5         | 5        | 5       | 5    | 5       | 5    |
| Jul 23       | 5      | 5         | 5        | 5       | 5    | 5       | 5    |
| Oct 23       | 5      | 5         | 5        | 5       | 5    | 5       | 5    |
| Feb 24       | 10     | 10        | 10       | 10      | 10   | 10      | 10   |
| May 24       | 15     | 15        | 15       | 15      | 15   | 15      | 15   |
| Sep 24       | 20     | 20        | 20       | 20      | 20   | 20      | 20   |
| Jan 25       | 25     | 25        | 25       | 25      | 25   | 25      | 25   |
| Apr 25       | 30     | 30        | 30       | 30      | 30   | 30      | 30   |
| Aug 25       | 35     | 35        | 35       | 35      | 35   | 35      | 35   |
| Nov 25       | 40     | 40        | 40       | 40      | 40   | 40      | 40   |
| Mar 26       | 45     | 45        | 45       | 45      | 45   | 45      | 45   |
| Jun 26       | 50     | 50        | 50       | 50      | 50   | 50      | 50   |
</details>

Source: Artificial Analysis, JEF

Exhibit 11 - Agentic index for top 20 models as of 8 Jun  
![](images/f5480571267b4dbffec0dde45dc9e1e60ddc6d3b41fe61e7bfb86dd45e21d7d7.jpg)

<details>
<summary>bar chart</summary>

| Model | Proprietary | Open Weights | Open Weights (Commercial Use Restricted) |
| :--- | :--- | :--- | :--- |
| Claude Opus 4.8 (max) | 78 | 0 | 0 |
| GP1-5.5 (xhigh) | 74 | 0 | 0 |
| Claude Opus 4.7 (max) | 72 | 0 | 0 |
| Gemin

[中间内容因长度限制已省略]

lar investment objectives, portfolio holdings, strategy, financial situation, or needs of any recipient. As such, any advice or recommendation in this report may not be suitable for a particular recipient. JEF assumes recipients of this report are capable of evaluating the information contained herein and of exercising independent judgment. A recipient of this report should not make any investment decision without first considering whether any advice or recommendation in this report is suitable for the recipient based on the recipient's particular circumstances and, if appropriate or otherwise needed, seeking professional advice, including tax advice. JEF does not perform any suitability or other analysis to check whether an investment decision made by the recipient based on this report is consistent with a recipient's investment objectives, portfolio holdings, strategy, financial situation, or needs.

By providing this report, neither JRS nor any other JEF entity accepts any authority, discretion, or control over the management of the recipient's assets. Any action taken by the recipient of this report, based on the information in the report, is at the recipient's sole judgment and risk. The recipient must perform his or her own independent review of any prospective investment. If the recipient uses the services of JEF LLC (or other affiliated broker-dealers), in connection with a purchase or sale of a security that is a subject of these materials, such broker-dealer may act as principal for its own accounts or as agent for another person. Only JRS is registered with the SEC as an investment adviser; and therefore neither JEF LLC nor any other JEF affiliate has any fiduciary duty in connection with distribution of these reports.

The price and value of the investments referred to herein and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

This report may contain forward looking statements that may be affected by inaccurate assumptions or by known or unknown risks, uncertainties, and other important factors. As a result, the actual results, events, performance or achievements of the financial product may be materially different from those expressed or implied in such statements.

This report has been prepared independently of any issuer of securities mentioned herein and not as agent of any issuer of securities. No Equity Research personnel have authority whatsoever to make any representations or warranty on behalf of the issuer(s). Any comments or statements made herein are those of the JEF entity producing this report and may differ from the views of other JEF entities.

This report may contain information obtained from third parties, including ratings from credit ratings agencies such as Standard & Poor's, and information derived from third-party or proprietary generative artificial intelligence (Gen AI) models. JEF does not guarantee the accuracy, completeness, timeliness or availability of this information, and is not responsible for any errors or omissions (negligent or otherwise), regardless of the cause, or for the results obtained from the use of such content. Neither JEF nor any third-party content providers, including providers of Gen AI models, give any express or implied warranties, including, but not limited to, any warranties of merchantability or fitness for a particular purpose or use. Neither JEF nor any third-party content provider shall be liable for any direct, indirect, incidental, exemplary, compensatory, punitive, special or consequential damages, costs, expenses, legal fees, or losses (including lost income or profits and opportunity costs) in connection with any use of their content, including ratings. Credit ratings are statements of opinions and are not statements of fact or recommendations to purchase, hold or sell securities. They do not address the suitability of securities or the suitability of securities for investment purposes, and should not be relied on as investment advice. Reproduction and distribution of third party content in any form is prohibited except with the prior written permission of the related third party.

JEF reports are disseminated and available electronically, and, in some cases, also in printed form. Electronic research is simultaneously made available to all clients. This report or any portion hereof may not be copied, reprinted, sold, or redistributed or disclosed by the recipient or any third party, by content scraping or extraction, automated processing, or any other form or means, without the prior written consent of JEF. Any unauthorized use is prohibited. Neither JEF nor any of its respective directors, officers or employees, is responsible for guaranteeing the financial success of any investment, or accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this report or its contents. Nothing herein shall be construed to waive any liability JEF has under applicable U.S. federal or state securities laws.

For Important Disclosure information relating to JRS, please see https://adviserinfo.sec.gov/IAPD/Content/Common/crd\_iapd\_Brochure.aspx?BRCHR\_VRSN\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://javatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.

© 2026 JEF
"""
