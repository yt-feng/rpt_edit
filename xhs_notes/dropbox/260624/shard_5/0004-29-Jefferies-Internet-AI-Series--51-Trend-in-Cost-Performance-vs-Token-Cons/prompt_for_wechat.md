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
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`JEF`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
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
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

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
## AI Series #51: Trend in Cost Performance vs Token Consumption vs Intelligence

Highlights (1) Silicon Data LLM Token Expenditure Index: it continues to remain soft between 1.64 to 1.68 (14 to 19 Jun), vs 2.04 on 31 May; (2) OpenRouter: Token consumption was up 4.7% vs prior week.; (3) reaffirm highly cost efficient model is key amid global industry trends (link) and lags US models by about 7 months (link); (4) Volcano Engine will have its FORCE conference on Tue / Wed with a number of focus areas (5) Weixin AI is under testing

In this report, we provide investors with over 50 data points on token consumption in OpenRouter, pricing for different models, model intelligence in Artificial Analysis, user trends by sub-sector and other industry data for analysis.

Volcano Engine: anticipate a number of updates in upcoming FORCE conference on 23 (Tue) and 24 Jun (Wed). Volcano Engine will have the conference this week and a number of sessions across different segments. We are watching (1) daily token consumption for Doubao large models. In Mar-26, it disclosed daily token consumption had reached 120tn; (2) monetization plan updates for Doubao and pricing for various subscription packages; (3) video generation model Seedance 2.0 updates, in particular ARR trends; (4) updates on its coding and agents strategy (e.g. TRAE, Arkclaw, coze); (5) MaaS revenue target.

Tencent: Kicking off the testing of Weixin AI. Tencent is doing small-scale testing on Weixin AI across various scenarios in social & communication, information & search, productivity, entertainment/shopping as well as tools generation. Weixin AI is called Xiao Wei: 1) located at top left side of main page 2) one of the features inside messaging. The core model is WeLM which is developed by Weixin team. We view this is an important step for Tencent in A2A and expect official release in 4Q26. PIs refer to report (link) for details.

BABA: Full stack capabilities and investments embrace the huge AI addressable market. Key highlights from Chairman Joe Tsai during VivaTech 2026 in Paris. (1) The TAM of AI is USD50tn, which is half of the world's GDP considering AI producing units of human intelligence and productivity; (2) China is under invested in AI supply. BABA is one of the better positioned companies backed by its free cash flow; (3) BABA's strategy centers on its integrated and full stack capabilities on chips and infrastructure, Qwen models and applications; (4) the setting up of its third European hub in France after Germany and UK. Agentic services is set to be launched in Europe in later 2026.

Silicon Data LLM Token Expenditure Index: Jun data continues to show softness vs end of May. The index (Exhibit 2) is weighted by where usage is concentrated (e.g. expenditure goes up when demand shifts towards premium models). On the other hand, media reports (e.g. The Information, Economic Observer) highlight tech and internet companies set upper limit on token consumption among employees. According to our checks, the index is between 1.64 to 1.68 between 14 to 19 Jun, vs 2.04 on 31 May. Based on Artificial Analysis, China models DeepSeek, Qwen, Kimi, MiniMax and Zhipu are highly cost-efficient vs US models and API cost is a fraction vs US models (Exhibit 3), thanks to former's refined architecture such as MoE (Mixture of Experts), attention mechanism (Group-Query Attention GQA, sparse attention) and MLU (Model FLOPs Utilization).

OpenRouter: Token consumption was up 4.7% vs prior week. Based on analysis of the week of 15 Jun (vs the week of 8 Jun) (Exhibit 1), the number of weekly tokens consumed increased by 4.7% to 46.7tn. In terms of ranking, DeepSeek V4 Flash ranked no 1, followed by Xiaomi MiMo-V2.5 and MiniMax M3.

Exhibit 1 - Weekly token consumption over the past 12 months as of 22 Jun (tn)  
![](images/84721dab7bbea420878aa33bc176d4e7d2e300c146dddc715d6307324911e746.jpg)  
Source: OpenRouter, JEF

Exhibit 2 - Silicon Data LLM Token Expenditure Index  
![](images/653f34352de85d739f2cd7e4d24581f624d611074f2c2eaa1e90aa7dd1f0a4e9.jpg)  
Source: FactSet, JEF

Exhibit 3 - Blended prices for China models vs US models (1Q26)  
![](images/6ee79820158e19042d36e50a39f6e4487fa8163dba6f8b80bb7e5d9fa2c99fc5.jpg)  
Source: Artificial Analysis, JEF

Exhibit 4 - Top 10 ranking in terms of token consumption by model the latest week

<table><tr><td>No</td><td>Company</td><td>Model</td><td>Tokens</td></tr><tr><td>1</td><td>DeepSeek</td><td>DeepSeek V4 Flash</td><td>4.94T</td></tr><tr><td>2</td><td>Xiaomi</td><td>MiMo-V2.5</td><td>3.94T</td></tr><tr><td>3</td><td>MiniMax</td><td>MiniMax M3</td><td>3.77T</td></tr><tr><td>4</td><td>Tencent</td><td>Hy3 preview</td><td>3.63T</td></tr><tr><td>5</td><td>OpenRouter</td><td>Owl Alpha</td><td>2.56T</td></tr><tr><td>6</td><td>DeepSeek</td><td>DeepSeek V4 Pro</td><td>2.53T</td></tr><tr><td>7</td><td>Anthropic</td><td>Claude Opus 4.7</td><td>2.53T</td></tr><tr><td>8</td><td>Anthropic</td><td>Claude Opus 4.8</td><td>1.69T</td></tr><tr><td>9</td><td>Anthropic</td><td>Claude Sonnet 4.6</td><td>1.54T</td></tr><tr><td>10</td><td>Z.AI</td><td>GLM 5.2</td><td>1.27T</td></tr></table>

Source: OpenRouter, JEF

Thomas Chong \* | Equity Analyst

852 3743 8016 | thomas.chong@JEF.com

Zoey Zong \* | Equity Analyst

Continued overleaf ...

BAT, KC, AI labs and Kling are Beneficiaries. We expect surge in token consumption on rising demand for AI models and agents to benefit CSPs like Baidu, Alibaba, Tencent (BAT), Kingsoft Cloud (KC), AI labs and Kling. According to analysis from Artificial Analysis, (1) there is a narrowing intelligence gap between US and China models; (2) API cost is just a fraction vs US benefiting from MoE, linear attention, and MFU; (3) Coding, Workspace scenario and mid- to long-form content should see significant opportunities ahead (Exhibit 73-77).

## China vs US comparison

## AI Models

According to OpenRouter, token consumption went up significantly in Feb-26 due to (a) a surge in adoption of coding / agents, which allows people using AI from "to chat" to "to work". It connects with large models which can be deployed locally or on servers, which allows you to automate workflow through natural language chat; (b) release of a number of high-performance and cost-efficient models which include Kimi K2.5 (Jan-26), M2.5 (Feb-26) and GLM-5 (Feb-26).

Exhibit 5 - Weekly token consumption over the past 12 months as of 22 Jun (tn)  
![](images/0b0149b3cd0b72126575970ba911f59a8c15bdf56103684e9cee98102627329a.jpg)  
Source: OpenRouter, JEF

According to OpenRouter (between 15 and 21 Jun), China models token consumption increased by 2.12% compared to prior week at 18.8tn. This compares to US models at 5.8tn token consumption. DeepSeek V4 Flash weekly token consumptions under rapid growth

According to OpenRouter, rising adoption of Coding / Agents and release of high-performance and cost-efficient China models are driving token consumption

In OpenRouter, China models surpassed US models in terms of token consumption the week of 15 Jun

Exhibit 6 - Market share: weekly token consumption by company as of 22 Jun  
![](images/ad19b99743245eb4c9284ec276df4082f2a3bca3fa3f4e1bfc658a18c871601c.jpg)  
Source: OpenRouter, JEF

Exhibit 7 - Weekly token consumption since Jan-26 (bn)  
![](images/34d36e722d8af790e1b44484766a0d376ebd5f4d5054c73d4ceea5eb567a91ed.jpg)  
Source: OpenRouter, JEF

On token consumption by company, DeepSeek (18.5%) comes first, followed by Anthropic (14.1%), Xiaomi (9.6%), Google (8.9%), and MiniMax (8.7%). The top 5 in weekly token consumption by model are DeepSeek V4 Flash (4.94tn), MiMo V2.5 (3.94tn), and MiniMax M3 (3.77tn), followed by Hy3 preview (3.63tn) and Owl Alpha (2.56tn).

Exhibit 8 - Top 10 ranking in terms of token consumption by model the latest week

<table><tr><td>No</td><td>Company</td><td>Model</td><td>Tokens</td></tr><tr><td>1</td><td>DeepSeek</td><td>DeepSeek V4 Flash</td><td>4.94T</td></tr><tr><td>2</td><td>Xiaomi</td><td>MiMo-V2.5</td><td>3.94T</td></tr><tr><td>3</td><td>MiniMax</td><td>MiniMax M3</td><td>3.77T</td></tr><tr><td>4</td><td>Tencent</td><td>Hy3 preview</td><td>3.63T</td></tr><tr><td>5</td><td>OpenRouter</td><td>Owl Alpha</td><td>2.56T</td></tr><tr><td>6</td><td>DeepSeek</td><td>DeepSeek V4 Pro</td><td>2.53T</td></tr><tr><td>7</td><td>Anthropic</td><td>Claude Opus 4.7</td><td>2.53T</td></tr><tr><td>8</td><td>Anthropic</td><td>Claude Opus 4.8</td><td>1.69T</td></tr><tr><td>9</td><td>Anthropic</td><td>Claude Sonnet 4.6</td><td>1.54T</td></tr><tr><td>10</td><td>Z.AI</td><td>GLM 5.2</td><td>1.27T</td></tr></table>

Source: OpenRouter, JEF  
DeepSeek V4 Flash ranked first in terms of token consumption the week of 15 Jun

Based on Artificial Analysis, China models DeepSeek, Qwen, Kimi, MiniMax and Zhipu are closing the gap with US models in terms of intelligence. China models are highly cost-efficient on Mixture of Experts (MoE) architecture, linear attention, and MLU (Model Flog Utilization). According to 2026 Stanford AI Index Report (Apr-26), the top US model leads Chinese models by 2.7%. Separately, Anthropic (1503), xAI (1495), Google (1494), OpenAI (1481), Alibaba (1449) and DeepSeek (1424) occupy the top tier of Arena Elo ratings as of Mar-26.

Exhibit 9 - No 11-20 ranking in terms of token consumption by model in latest week

<table><tr><td>No</td><td>Company</td><td>Model</td><td>Tokens</td></tr><tr><td>11</td><td>OpenAI</td><td>GPT 5.5</td><td>996B</td></tr><tr><td>12</td><td>Z.AI</td><td>GLM 5.1</td><td>993B</td></tr><tr><td>13</td><td>DeepSeek</td><td>DeepSeek V3.2</td><td>989B</td></tr><tr><td>14</td><td>Google</td><td>Gemini 3 Flash Preview</td><td>944B</td></tr><tr><td>15</td><td>StepFun</td><td>Step 3.7 Flash</td><td>886B</td></tr><tr><td>16</td><td>Google</td><td>Gemini 2.5 Flash Lite</td><td>680B</td></tr><tr><td>17</td><td>NVIDIA</td><td>Nemotron 3 Ultra (free)</td><td>629B</td></tr><tr><td>18</td><td>Google</td><td>Gemini 2.5 Flash</td><td>621B</td></tr><tr><td>19</td><td>Nex-AGI</td><td>Nex-N2 -Pro (free)</td><td>583B</td></tr><tr><td>20</td><td>MoonshotAI</td><td>Kimi K2.6</td><td>579B</td></tr></table>

Source: OpenRouter, JEF

China models are narrowing the gap with US models in terms of intelligence. On Input/Output API, China large models are highly efficient vs US models.

Exhibit 10 - Cache hit/Input/Output API price for leading models as of 22 Jun  
![](images/a63fd1be14a70d124fe345adcab8e924b936956bd7b82eb038271aee780ed9ea.jpg)

Exhibit 11 - Quarterly Input / Output prices for China models  
![](images/c8e14a2eca478b3b3b64654524ad85dd88ab97700ddca2a2d70c9f22ea06aedc.jpg)  
Source: Artificial Analysis, JEF  
In terms of Input/Output API price, China models are just a fraction vs US models.

Exhibit 12 - Quarterly Input / Output prices for US models  
![](images/461b073e557d29f640bb1b4702ff518f37fec2aa44ea3c5d664deca1934a9416.jpg)  
Source: Artificial Analysis, JEF

■ Proprietary ■ Open Weights ■ Open Weights (Commercial Use Restricted)

Exhibit 13 - Intelligence index for top 20 models as of 22 Jun  
![](images/165360cd831b8fd3e1b2072689d9900316cbf66e95bd223d257947e619338f88.jpg)

Exhibit 14 - Frontier Language Model Intelligence over time as of 22 Jun  
![](images/5cf1699b5b80bb2f7047074d2c42fb4402fc7781334aabd07866efcc0ca117df.jpg)  
■ Proprietary □ Open Weights ■ Open Weights (Commercial Use Restricted)  
Source: Artificial Analysis, JEF  
Source: Artificial Analysis, JEF

Among top 20 large models, there are 9 which are China models and open weighted as of 22 Jun.

Exhibit 15 - Agentic index for top 20 models as of 22 Jun  
![](images/0d769b6c3af8eab4d2dfb4fac1d5b418cd0c84a981a3f5a25ac3ea07ab3d76b8.jpg)  
■ Proprietary □ Open Weights ▪ Open Weights (Commercial Use Restricted)

Exhibit 16 - Coding index for top 20 models as of 22 Jun  
![](images/47eed46c216740a1280988340e296496a3803ea686a9eb8a192b12c0ffc7aac0.jpg)  
Source: Artificial Analysis, JEF  
Source: Artificial Analysis, JEF

Exhibit 17 - Cost to run Artificial Intelligence Index as of 22 Jun
Most attractive quadrant  
![](images/738d533398ae6a3389425cd6c40e31a4063a282cb3915239597174d787a4565e.jpg)  
Source: Artificial Analysis, JEF

## Exhibit 18 - Output speed to run Artificial Intelligence Index as of 22 Jun Most attractive quadrant

![](images/ff211ee820ace188674a033e4ba6179b68d31be765e064544213b1c8fd52406b.jpg)  
Source: Artificial Analysis, JEF

# Input/Output Price for Different Models / Pricing for Coding Plan and Agents Offerings

Red color denotes price hike / new price during the month

Exhibit 19 - Pricing plans for Alibaba, Tencent, Baidu and ByteDance

<table><tr><td>Models Provider</td><td>Model</td><td>Context</td><td colspan="2">Jun-26</td></tr><tr><td></td><td></td><td></td><td>Input (RMB)</td><td>Output (RMB)</td></tr><tr><td></td><td></td><td></td><td>(million tokens)</td><td>(million tokens)</td></tr><tr><td rowspan="10">Alibaba</td><td>Qwen3.7-Max</td><td>(0, 1m]</td><td>6 (original 12, promo till 22 Jun)</td><td>18 (original 36, promo till 22 Jun)</td></tr><tr><td rowspan="2">Qwen3.7-Plus</td><td>(0, 256k]</td><td>1.6 (original 2, promo till 2 Jul)</td><td>6.4 (original 8, promo till 2 Jul)</td></tr><tr><td>(256k, 1m]</td><td>4.8 (original 6, promo till 2 Jul)</td><td>19.2 (original 24, promo till 2 Jul)</td></tr><tr><td rowspan="2">Qwen3.6-Max-Preview</td><td>(0, 128k]</td><td>9</td><td>54</td></tr><tr><td>(128k, 256k]</td><td>15</td><td>90</td></tr><tr><td rowspan="2">Qwen3.6-Plus</td><td>(0, 256k]</td><td>2</td><td>12</td></tr><tr><td>(256k, 1m]</td><td>8</td><td>48</td></tr><tr><td rowspan="3">Qwen3.5-Plus</td><td>(0, 128k]</td><td>0.8</td><td>4.8</td></tr><tr><td>(128k, 256k]</td><td>2</td><td>12</td></tr><tr><td>(256k, 1m]</td><td>4</td><td>24</td></tr><tr><td rowspan="11">Tencent</td><td rowspan="3">HY 3.0 Preview</td><td>(0, 16k]</td><td>1.2</td><td>4</td></tr><tr><td>(16k,32k]</td><td>1.6</td><td>6.4</td></tr><tr><td>(32k,256k]</td><td>2</td><td>8</td></tr><tr><td rowspan="2">HY 2.0 Think</td><td>(0, 32k]</td><td>3.975</td><td>15.9</td></tr><tr><td>(32k,128k]</td><td>5.3</td><td>21.2</td></tr><tr><td rowspan="2">HY 2.0 Instruct</td><td>(0, 32k]</td><td>3.18</td><td>7.95</td></tr><tr><td>(32k,128k]</td><td>4.505</td><td>11.13</td></tr><tr><td>Hunyuan-T1</td><td></td><td>1</td><td>4</td></tr><tr><td>Hunyuan-TurboS</td><td></td><td>0.8</td><td>2</td></tr><tr><td>Tencent HY Vision 1.5 Instruct</td><td></td><td>3</td><td>9</td></tr><tr><td>Hunyuan-translation</td><td></td><td>1.2</td><td>3.6</td></tr><tr><td rowspan="6">Baidu</td><td rowspan="2">ERNIE-5.1</td><td>(0, 32k]</td><td>4</td><td>18</td></tr><tr><td>(32k, 128k]</td><td>6</td><td>22</td></tr><tr><td rowspan="2">ERNIE-5.0</td><td>(0, 32k]</td><td>6</td><td>24</td></tr><tr><td>(32k, 128k]</td><td>10</td><td>40</td></tr><tr><td>ERNIE-4.5-Turbo</td><td></td><td>0.8</td><td>3.2</td></tr><tr><td>ERNIE-4.5-Turbo-VL</td><td></td><td>3</td><td>9</td></tr><tr><td rowspan="12">ByteDance</td><td rowspan="3">Doubao-seed-2.0-pro</td><td>[0, 32k]</td><td>3.2</td><td>16</td></tr><tr><td>(32k, 128k]</td><td>4.8</td><td>24</td></tr><tr><td>(128k, 256k]</td><td>9.6</td><td>48</td></tr><tr><td rowspan="3">Doubao-seed-2.0-lite</td><td>[0, 32k]</td><td>0.6</td><td>3.6</td></tr><tr><td>(32k, 128k]</td><td>0.9</td><td>5.4</td></tr><tr><td>(128k, 256k]</td><td>1.8</td><td>10.8</td></tr><tr><td rowspan="3">Doubao-seed-2.0-mini</td><td>[0, 32k]</td><td>0.2</td><td>2</td></tr><tr><td>(32k, 128k]</td><td>0.4</td><td>4</td></tr><tr><td>(128k, 256k]</td><td>0.8</td><td>8</td></tr><tr><td rowspan="3">Doubao-seed-2.0-code</td><td>[0, 32k]</td><td>3.2</td><td>16</td></tr><tr><td>(32k, 128k]</td><td>4.8</td><td>24</td></tr><tr><td>(128k, 256k]</td><td>9.6</td><td>48</td></tr></table>

Source: Company, JEF

Exhibit 20 - Pricing plans for AI Labs MiniMax, Zhipu, Kimi

<table><tr><td>Models Provider</td><td>Model</td><td>Context</td><td colspan="2">Jun-26</td></tr><tr><td></td><td></td><td></td><td>Input (RMB)</td><td>Output (RMB)</td></tr><tr><td></td><td></td><td></td><td>(million tokens)</td><td>(million tokens)</td></tr><tr><td rowspan="6">MiniMax</td><td rowspan="2">MiniMax-M3</td><td>Input: [0, 512k]</td><td>2.1</td><td>8.4</td></tr><tr><td>Input: [512k+)</td><td>4.2</td><td>16.8</td></tr><tr><td>MiniMax-M2.7</td><td></td><td>2.1</td><td>8.4</td></tr><tr><td>MiniMax-M2.7-highspeed</td><td></td><td>4.2</td><td>16.8</td></tr><tr><td>MiniMax-M2.5</td><td></td><td>2.1</td><td>8.4</td></tr><tr><td>MiniMax-M2.5-highspeed</td><td></td><td>4.2</td><td>16.8</td></tr><tr><td rowspan="10">Zhipu AI</td><td>GLM-5.2</td><td></td><td>8</td><td>28</td></tr><tr><td rowspan="2">GLM-5.1</td><td>[0, 32k)</td><td>6</td><td>24</td></tr><tr><td>[32k+)</td><td>8</td><td>28</td></tr><tr><td rowspan="2">GLM-5-Turbo</td><td>[0, 32k)</td><td>5</td><td>22</td></tr><tr><td>[32k+)</td><td>7</td><td>26</td></tr><tr><td rowspan="2">GLM-5</td><td>[0, 32k)</td><td>4</td><td>18</td></tr><tr><td>[32k+)</td><td>6</td><td>22</td></tr><tr><td rowspan="3">GLM-4.7</td><td>Input length: [0,32k)Output length: [0,0.2k)</td><td>2</td><td>8</td></tr><tr><td>Input length: [0,32k)Output length: [0,2k+)</td><td>3</td><td>14</td></tr><tr><td>[32k, 200k)</td><td>4</td><td>16</td></tr><tr><td rowspan="9">Kimi</td><td>Kimi K2.7 Code</td><td></td><td>6.5</td><td>27</td></tr><tr><td>Kimi K2.6</td><td></td><td>6.5</td><td>27</td></tr><tr><td>Kimi K2.5</td><td></td><td>4</td><td>21</td></tr><tr><td>kimi-k2-thinking</td><td></td><td>4</td><td>16</td></tr><tr><td>kimi-k2-thinking-turbo kimi-k2-turbo-preview</td><td></td><td>8</td><td>58</td></tr><tr><td>kimi-k2-0905-preview kimi-k2-0711-preview</td><td></td><td>4</td><td>16</td></tr><tr><td>moonshot-v1-8k moonshot-v1-8k-vision-preview</td><td></td><td>2</td><td>10</td></tr><tr><td>moonshot-v1-32k moonshot-v1-32k-vision-preview</td><td></td><td>5</td><td>20</td></tr><tr><td>moonshot-v1-128k moonshot-v1-128k-vision-preview</td><td></td><td>10</td><td>30</td></tr></table>

Source: Company, JEF

Exhibit 21 - Pricing plans for AI Labs StepFun, Xiaomi, and DeepSeek

<table><tr><td>Models Provider</td><td>Model</td><td>Context</td><td colspan="2">Jun-26</td></tr><tr><td></td><td></td><td></td><td>Input (RMB)</td><td>Output (RMB)</td></tr><tr><td></td><td></td><td></td><td>(million tokens)</td><td>(million tokens)</td></tr><tr><td rowspan="9">StepFun</td><td>step-3.5-flash</td><td></td><td>0.7</td><td>2.1</td></tr><tr><td>step-r1-v-mini</td><td></td><td>2.5</td><td>8</td></tr><tr><td rowspan="3">step-3</td><td>input≤4k &amp; output≤4k</td><td>1.5</td><td>4</td></tr><tr><td>input≤4k &amp; 

[中间内容因长度限制已省略]

ular investment objectives, portfolio holdings, strategy, financial situation, or needs of any recipient. As such, any advice or recommendation in this report may not be suitable for a particular recipient. JEF assumes recipients of this report are capable of evaluating the information contained herein and of exercising independent judgment. A recipient of this report should not make any investment decision without first considering whether any advice or recommendation in this report is suitable for the recipient based on the recipient's particular circumstances and, if appropriate or otherwise needed, seeking professional advice, including tax advice. JEF does not perform any suitability or other analysis to check whether an investment decision made by the recipient based on this report is consistent with a recipient's investment objectives, portfolio holdings, strategy, financial situation, or needs.

By providing this report, neither JRS nor any other JEF entity accepts any authority, discretion, or control over the management of the recipient's assets. Any action taken by the recipient of this report, based on the information in the report, is at the recipient's sole judgment and risk. The recipient must perform his or her own independent review of any prospective investment. If the recipient uses the services of JEF LLC (or other affiliated broker-dealers), in connection with a purchase or sale of a security that is a subject of these materials, such broker-dealer may act as principal for its own accounts or as agent for another person. Only JRS is registered with the SEC as an investment adviser; and therefore neither JEF LLC nor any other JEF affiliate has any fiduciary duty in connection with distribution of these reports.

The price and value of the investments referred to herein and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

This report may contain forward looking statements that may be affected by inaccurate assumptions or by known or unknown risks, uncertainties, and other important factors. As a result, the actual results, events, performance or achievements of the financial product may be materially different from those expressed or implied in such statements.

This report has been prepared independently of any issuer of securities mentioned herein and not as agent of any issuer of securities. No Equity Research personnel have authority whatsoever to make any representations or warranty on behalf of the issuer(s). Any comments or statements made herein are those of the JEF entity producing this report and may differ from the views of other JEF entities.

This report may contain information obtained from third parties, including ratings from credit ratings agencies such as Standard & Poor's, and information derived from third-party or proprietary generative artificial intelligence (Gen AI) models. JEF does not guarantee the accuracy, completeness, timeliness or availability of this information, and is not responsible for any errors or omissions (negligent or otherwise), regardless of the cause, or for the results obtained from the use of such content. Neither JEF nor any third-party content providers, including providers of Gen AI models, give any express or implied warranties, including, but not limited to, any warranties of merchantability or fitness for a particular purpose or use. Neither JEF nor any third-party content provider shall be liable for any direct, indirect, incidental, exemplary, compensatory, punitive, special or consequential damages, costs, expenses, legal fees, or losses (including lost income or profits and opportunity costs) in connection with any use of their content, including ratings. Credit ratings are statements of opinions and are not statements of fact or recommendations to purchase, hold or sell securities. They do not address the suitability of securities or the suitability of securities for investment purposes, and should not be relied on as investment advice. Reproduction and distribution of third party content in any form is prohibited except with the prior written permission of the related third party.

JEF reports are disseminated and available electronically, and, in some cases, also in printed form. Electronic research is simultaneously made available to all clients. This report or any portion hereof may not be copied, reprinted, sold, or redistributed or disclosed by the recipient or any third party, by content scraping or extraction, automated processing, or any other form or means, without the prior written consent of JEF. Any unauthorized use is prohibited. Neither JEF nor any of its respective directors, officers or employees, is responsible for guaranteeing the financial success of any investment, or accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this report or its contents. Nothing herein shall be construed to waive any liability JEF has under applicable U.S. federal or state securities laws.

For Important Disclosure information relating to JRS, please see https://adviserinfo.sec.gov/IAPD/Content/Common/crd\_iapd\_Brochure.aspx?BRCHR\_VRSN\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://avatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.

© 2026 JEF
"""
