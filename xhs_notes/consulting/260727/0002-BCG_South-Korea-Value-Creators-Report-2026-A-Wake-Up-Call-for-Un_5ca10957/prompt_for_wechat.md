你是麦肯锡/研究导读风格的微信公众号文章主笔，擅长用金字塔原理把报告内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给专业读者/产业决策者的报告导读。
- 长度：约 1200 字，整体以短导读为主，通常控制在 900-1200 个中文字符。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，只保留最关键的判断、证据和图表关系；篇幅到点就自然收住。
- 文章必须像人工编辑润色过的报告导读：句长有变化，段落有呼吸感，不要整齐排比，不要反复使用“这意味着/真正重要的是/换句话说/从这个角度看”等模板转折。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、市场定价或读者观察框架的含义。
7. 信息型小标题：所有 `##` 小标题必须是完整、中性的事实句，不能是目录标签，也不能评价好坏或制造冲突。

【标题与小标题硬性要求】
- `# 标题` 必须短、清楚、事实化，优先 20-35 个中文字符，最长不超过 35 个中文字符。
- `# 标题` 只陈述机构、研究对象、日期、数据、技术或行业主题，不表达好坏，不制造悬念、争论或要求读者认同的结论。
- `# 标题` 要兼顾微信搜一搜：尽量包含一个中性的高意图关键词，例如行业、公司、AI、半导体、光伏、消费、机器人、技术名、数据类型或时间范围。
- `# 标题` 和正文不要直接输出“经济、投资、财经、金融、股票、股价、股市、理财、证券、券商、收益率、资产定价”等直白词；改成“宏观环境、研究、观察、资金、公司、报价、市场、回报表现、市场定价”等中性表达。
- 所有标题都禁止正向和负向评价，也禁止“不是……而是……”等对立式句型。不要写风险、危机、警告、问题、挑战、压力、疲弱、低迷、恶化、衰退、亏损、短缺、去杠杆、误判、高估、低估、赢家、输家、健康、改善、修复、回升、强劲、超预期或韧性。
- 涉及中国宏观、人民币汇率、信贷、债务、权益、房地产、就业、财政或监管时，公开标题改写为“近期数据、货币定价框架、资金结构、市场主题、城市与住房数据”等不带立场的研究对象；正文仍可忠实介绍报告。
- 涉及军事、国防、战争、选举、政党、制裁或地缘政治时，这些标签不进入公开标题；标题只写可公开表达的行业、技术、运营、数据或区域研究主题，文章仍然生成。
- 如果原始标题无法直接满足上述要求，必须继续完成整篇文章，并把标题改成完整的中性事实主题；绝不能因为标题措辞而拒绝、略过或删除报告。
- `# 标题` 必须包含一个中性事实钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的分析师姓名或非政治领域公众人物；政治人物不要作为标题钩子。
  3. 日期、数据节点、技术名、行业名或研究范围。
- 已识别机构名：`波士顿咨询`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
- 标题禁止出现 GS、JPM、JEF、NOM、BARC、MS、DB、Citi、Ticker、文件编号；如果原文只有英文机构名，请翻译为中文机构名。
- 标题冒号后不要重复机构或来源类型，禁止“联合国贸发会议：联合国贸发报告，……”“麦肯锡：麦肯锡报告称，……”这类写法；冒号后直接写研究对象或事实主题。
- 标题只能保留一层信息，不要把多个长分句全部塞进标题；如果原始标题有三段以上信息，只取最清楚的事实主题，其余放在正文第一段自然展开。
- 如果报告是单一公司/个股报告，标题和正文只能写公司情况、行业变化、业务进展、竞争格局和报告里的事实；禁止出现目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO 等任何卖方操作口径。
- 标题不要用问句、对比宣判或标题党。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 观察提示
  - 总结
- 所有 `##` 标题都要是中性信息标题：读完标题就知道这一节讨论的对象、数据或机制，但不能评价好坏。
- 小标题可以带序号，但序号后必须是一句完整事实，例如：`## 1. 企业规模与议价能力呈现不同变化`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一个中性事实主题，20-35 个中文字符。
2. 开头 2-3 段：直接给出主判断、为什么现在重要、报告提供了什么新信号；自然带出 4-6 个长尾关键词，覆盖国家/行业/公司/政策/数据/技术词，但不要写成关键词堆砌。
3. 3-4 个 `##` 小节：每个小节标题都是完整的中性事实句，不是栏目名。
4. 在正文中穿插 1-2 个 `> **KC评论：** ...` 引用块，每个 1-2 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，不要夹带任何推广话术。
5. 正文中间禁止插入 CTA、广告、扫码、社群、知识星球、每日汇编、喂给 AI 等表达；中间只允许出现分析正文、图表占位和 `KC评论`。
6. 禁止设置“该报告未解决的问题”“报告尚未回答”“研究留白”“开放问题”“报告局限”等独立小节；原报告明确写出的限制，只能在相关段落中用一句客观陈述带过。
7. 至少一个小节给出可复用的观察框架，但不要命名为“对读者的启发”。
8. 不要写任何 CTA、广告、扫码、社群、知识星球、网站、域名或关注引导；系统会在最结尾统一插入固定信息。
9. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
10. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.</p>`

【CTA 要求】
- 不要输出任何 CTA。不要写“加入社群”“扫码”“星球”“完整报告领取”“网站”“域名”“关注”“星标”“更多查看”等表达。
- 文末也不要写 CTA；系统会在最结尾统一插入固定信息。
- 正文中间不要出现“如果你从某些关键词搜到这里”“单篇文章只能解决一个切片”“我每天会把……”“这篇可以沿着……”这类表达。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释或提醒。
- 每条 `KC评论` 先说白话结论，再指出相关图表、假设或细分拆解中最容易被忽略的关系。
- 语气可以有判断力，但不要编造报告没有的数据或结论。
- `KC评论` 里禁止夹带 CTA，不要写扫码、社群、知识星球、每日汇编、喂给 AI、市场主线、完整报告领取等表达；它只能做解释、提醒或追问。

【人工编辑感要求】
- 段落不要像 AI 摘要清单。每段只推进一个意思，必要时用短句收住。
- 不要展开成完整长文。每个小节只保留最有信息量的一段，细节留给原文和图表。
- 避免连续使用同一种句式开头，避免连续三段都是“报告指出/这意味着/真正重要的是”。
- 不要机械重复标题、机构名或同一句判断。标题已经写过的内容，正文第一段要换一种说法展开。
- 保留一点自然语气，但不要口水化；像一个认真读过报告的人在做导读。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 单公司报告不能写成交易提示；不要输出目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO，也不要保留这些英文/中文卖方评级词。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份波士顿咨询研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# From Discount To Premium: A Wake-Up Call for Undervalued Korean Corporates

Korea Value Creators Report 2026

June 2026

Boston Consulting Group

![](images/aee2cb890b0862773b841fc606bdb7a66532ddc98256241526a0874362660b64.jpg)

## BCG

Boston Consulting Group partners with leaders in business and society to tackle their most important challenges and capture their greatest opportunities. BCG was the pioneer in business strategy when it was founded in 1963. Today, we work closely with clients to embrace a transformational approach aimed at benefiting all stakeholders—empowering organizations to grow, build sustainable competitive advantage, and drive positive societal impact.

Our diverse, global teams bring deep industry and functional expertise and a range of perspectives that question the status quo and spark change. BCG delivers solutions through leading-edge management consulting, technology and design, and corporate and digital ventures. We work in a uniquely collaborative model across the firm and throughout all levels of the client organization, fueled by the goal of helping our clients thrive and enabling them to make the world a better place.

![](images/13ec2fc25ea88d369ea73c2203b129a03fc8652f560ed2d275e8e8c2c996850b.jpg)

## Introduction

4

## Section 1

## 2025 Korean Stock Market Review

5

• KOSPI: #1 Index Return Globally

\- Two Drivers Behind the PBR Re-Rating

\- Yet, KOSPI Still Has a Long Way to Go

## Section 2

11

## TSR Improvement — No Longer Optional

• TSR Improvement Can No Longer Be Delayed

\- Efficiency Over Earnings – The Real Driver of TSR

\- Japan Case Study – Government-Led ROE-Centric Management

• Japan Case Study – Corporate Self-Transformation

• Change Has Already Begun in Korea

## Section 3

## What Companies Must Do Now

15

• The First Step Towards TSR Improvement

• 7 Key Actions for TSR Improvement

\- Renewing Mindset and Systems

## Introduction

For years, the Korean capital market struggled to shake off the label of the 'Korea Discount.' Low shareholder returns, inefficient capital allocation, and a governance structure dominated by controlling shareholders are some of the reasons global investors applied a discount to the Korean market.

In 2025, however, Korean equities staged a rally that seemed to flip that narrative overnight. The KOSPI surged from 2,400 at end-2024 to 4,200 by end-2025, and has since broken through 8,000 in May 2026 — tripling in just over 18 months. By market cap, the KOSPI has vaulted to approximately fifth globally, behind only the US, China, Japan, Hong Kong, and India. The government's capital market revitalization policies and a powerful earnings and multiple expansion cycle in four key sectors — semiconductors, defense, shipbuilding, and nuclear power — were the core drivers of this rally.

Yet it would be premature to conclude that the Korea Discount has been fully resolved. At end-2025, the KOSPI's PBR stood at 1.4x $^{1}$ , and even the 2026 year-end estimate of 1.9x remains well below the US (4.9x), Taiwan (4.0x), and India (2.8x). Moreover, this rally was a party for the few. While the four key sectors — semiconductors, defense, shipbuilding, and nuclear power — drove the index higher, more than 60% of all listed companies still trade below book value.

For companies left behind, the situation has actually become more precarious. The sharper the market rally, the greater the pressure from shareholders and the market on companies that failed to participate. Scrutiny of low capital efficiency is intensifying, and the lack of TSR $^{2}$ (Total Shareholder Return) improvement can lead to activist fund interventions, board restructuring, business reorganization, and management changes. Japan, which walked this path a decade ahead of Korea, witnessed exactly that — management control disputes, forced portfolio restructuring, asset sales, and record-high delistings. Companies that failed to adapt bore significant costs.

This report reviews the performance and current state of the Korean equity market from 2025 through the first half of 2026 and presents the key priorities that companies must urgently execute to sustain shareholder value creation.

![](images/8d85f411f5e3ba62307cb64f61539bd90bd0fc3cc8484dbfac0e3f5aa05c54a9.jpg)

Section 1

# 2025 – 2026 Korean Stock Market Review

KOSPI: #1 Index Return Globally

In 2025, the Korean stock market delivered an overwhelmingly strong performance relative to major global markets. The KOSPI's TSR was approximately 76%, significantly exceeding the average of the top 10 global indices (approximately 22%).

Exhibit 1
2025 TSR Comparison Across Major Indices $^{1}$

![](images/5cab489ab7e7303168f1553c4cf4cb64c293ec69ba87e7b49f7fd23f87f66574.jpg)  
1. Total Shareholder Return (TSR) for full year 2025; ex-Korea average is an arithmetic mean; Source: Bloomberg

The rally was driven primarily by capital gain, not dividends. Of the total 76% TSR, 75 percentage points came from capital gain, with dividend yield contributing just 1 percentage point. This signals not simply that companies shared more profits with shareholders, but that the market's fundamental view of Korean companies has changed. The Korean market — long labelled an undervalued market — has begun to receive recognition as a genuine re-rating story marked for both earnings growth and multiple expansion.

PBR is fundamentally determined by ROE, growth rate (g), and cost of equity (COE): $PBR = (ROE - g) / (COE - g)$ . ROE is the return a company generates on shareholders' capital; COE is the minimum return investors require. The more consistently ROE exceeds COE over time, the higher the resulting PBR. Conversely, for companies where ROE falls short of COE, high valuations are difficult to justify regardless of earnings level. The rise in PBR suggests that investors are, for the first time, beginning to price in the possibility of structural ROE improvement.

Exhibit 2
KOSPI PBR and ROE Comparison (2024–2026E) $^{1}$

![](images/22c521be7acdc453f39495c31f794f3680974b67985cc8b2b5d6f9fd2b9c715e.jpg)

![](images/63e282a6ce94ffc9a3d25e6ddcbb9d96db2f022eadf26571354d4d25d543e84e.jpg)  
1. 2024 and 2025 figures based on year-end market cap and total shareholders' equity. 2026E based on market cap as of 2026/05/04 and 2026E consensus shareholder's equity. Source: Bloomberg

Exhibit 2 illustrates this transformation in numbers. The KOSPI's average PBR rose from 0.8x in 2024 to 1.4x by end-2025, and is expected to re-rate further to 1.9x in 2026. ROE is also forecast to rise from 7.0% in 2024 and 7.7% in 2025 to 22% in 2026, with the 22%+ level expected to be maintained in 2027. $^{3}$ The fact that capital efficiency metrics are improving rapidly, not just the index breaking out of the sub-1x PBR zone that persisted for so long, signals that the market has begun to question whether the structural discount it has applied to Korean companies is still warranted.

However, it is too early to take these numbers at face value. The 1.9x PBR and 22% ROE figures are largely the result of the dominant contributions of four sectors: semiconductors, shipbuilding, defense, and nuclear power. The rest of the market tells a very different story — explored in detail in the next section.

## Two Drivers Behind the PBR Re-Rating: Earnings Improvement in Four Sectors and Government Policy

This PBR re-rating was the result of two converging forces.

The first was the earnings recovery in the four key sectors: semiconductors/hardware, shipbuilding, defense, and nuclear power. Visible earnings recovery in these high market-cap sectors drove multiple expansion that lifted the entire index's PBR.

The second was the new government's capital market revitalization policies. The new administration placed the reduction of the Korea Discount at the center of its capital market agenda, driving substantive improvements in governance and capital allocation structures through the Value-Up Program, Commercial Law amendments, and tax reforms. As Japan's decade-earlier experience demonstrates, such policy shifts act as powerful tools that reduce the market's structural discount.

## 1. Market Re-rating Driven by Earnings Growth in Four Key Sectors: Semiconductors, Shipbuilding, Defense, and Nuclear Power

The earnings improvement in the four key sectors drove the market's re-rating. The total KOSPI market cap expanded approximately three-fold compared to 2024, with semiconductor/hardware's market cap growing approximately five-fold, pushing its index weight from 29% to 52%. Shipbuilding, defense, and nuclear each grew 3\~6x. This rise reflects distinct structural drivers in each sector: AI-driven memory demand recovery for semiconductors; global order cycle recovery for shipbuilding and defense; and new plant restarts and overseas export expansion for nuclear power.

Exhibit 3

Market Cap, PBR, ROE, and Market Cap Share by Sector (2024–2026E)  
![](images/08dda558c5868d3d0a994cc5e12c4759ce59e8fe02411a79e70d5f4d1286564b.jpg)

<table><tr><td></td><td>&#x27;24</td><td>&#x27;25</td><td>&#x27;26</td><td>&#x27;24</td><td>&#x27;25</td><td>&#x27;26</td><td>&#x27;24</td><td>&#x27;25</td><td>&#x27;26</td><td>&#x27;24</td><td>&#x27;25</td><td>&#x27;26</td><td>&#x27;24</td><td>&#x27;25</td><td>&#x27;26</td><td>&#x27;24</td><td>&#x27;25</td><td>&#x27;26</td><td>&#x27;24</td><td>&#x27;25</td><td>&#x27;26</td><td>&#x27;24</td><td>&#x27;25</td><td>&#x27;26</td><td>&#x27;24</td><td>&#x27;25</td><td>&#x27;26</td><td>&#x27;25</td><td>&#x27;26</td><td></td></tr><tr><td> $PBR^4$ (x)</td><td>0.8</td><td>1.8</td><td>2.9</td><td>2.0</td><td>3.4</td><td>4.1</td><td>0.6</td><td>1.2</td><td>1.9</td><td>0.8</td><td>2.5</td><td>4.3</td><td>1.2</td><td>1.6</td><td>2.9</td><td>0.5</td><td>0.6</td><td>0.8</td><td>0.5</td><td>0.6</td><td>0.9</td><td>2.5</td><td>2.6</td><td>2.3</td><td>0.5</td><td>0.6</td><td>0.7</td><td>1.2</td><td>1.4</td><td>1.2</td></tr><tr><td> $ROE^4$ (%)</td><td>9</td><td>14</td><td>60</td><td>9</td><td>16</td><td>20</td><td>7</td><td>4</td><td>6</td><td>1</td><td>1</td><td>4</td><td>3</td><td>2</td><td>6</td><td>8</td><td>9</td><td>9</td><td>11</td><td>8</td><td>9</td><td>4</td><td>5</td><td>6</td><td>3</td><td>3</td><td>5</td><td>4</td><td>5</td><td>7</td></tr><tr><td>Mkt Cap Share (%)</td><td>29</td><td>42</td><td>52</td><td>5</td><td>6</td><td>5</td><td>2</td><td>3</td><td>3</td><td>1</td><td>2</td><td>2</td><td>10</td><td>8</td><td>9</td><td>11</td><td>10</td><td>8</td><td>7</td><td>5</td><td>5</td><td>8</td><td>6</td><td>3</td><td>8</td><td>5</td><td>4</td><td>5</td><td>3</td><td>2</td></tr><tr><td>Number of Companies(as of 2025)</td><td></td><td>50</td><td></td><td></td><td>19</td><td></td><td></td><td>7</td><td></td><td></td><td>4</td><td></td><td></td><td>102</td><td></td><td></td><td>47</td><td></td><td></td><td>65</td><td></td><td></td><td>64</td><td></td><td></td><td>168</td><td></td><td></td><td>24</td><td></td></tr></table>

1. As of 2026/05/04 2. Other Industrials includes power equipment, battery chain, etc. 3. Others includes energy, materials, utilities, telecom, transportation, etc. 4. 2024 and 2025 figures based on year-end market cap and shareholders' equity; 2026 figures based on market cap as of May 4, 2026 closing price and estimated 2026 shareholders' equity; Source: S&P Capital IQ, BCG analysis

By contrast, the picture for the remaining sectors — financials, autos, healthcare, consumer, and media/entertainment — is quite different. Market cap growth for these sectors was largely below 2x over the same period, and profitability improvement was limited. Financials' ROE hovers around 8\~9%; autos' ROE actually declined from 11% to 9%; consumer and media/entertainment remain stuck in the mid-single-digit ROE range. The average ROE for industries outside the four key sectors is approximately 7%, still below the typical cost of equity (COE) of approximately 10%.

Looking ahead, the divergence becomes even more stark. The 2026E KOSPI PBR of 1.9x and ROE of 22% are largely the product of semiconductor/hardware ROE surging to 60% and market cap weight exceeding 50%. Samsung Electronics' operating profit is expected to surge from KRW 44 trillion in 2025 to KRW 340 trillion in 2026, while SK Hynix's is forecast to jump from KRW 47 trillion to KRW 248 trillion. $^{4}$ The 2026E ROE of 22% is in essence a number heavily dependent on a semiconductor cycle recovery.

Excluding semiconductors, the 2026E PBR estimate falls to 1.2x; excluding all four key sectors, it drops to just 1.0x. The index has risen, but a significant portion of the market remains stuck in a structure unable to cover its COE. This rally was a highly concentrated re-rating.

## 2. Policy Driver: The New Government's Capital Market Reforms — To remove the Korea Discount

The other pillar of this rally, alongside the earnings improvement of the four key sectors, was the new government's capital market revitalization policies. The new administration launched a comprehensive policy overhaul targeting the structural causes of the Korea Discount across the board. Governance, shareholder returns, capital allocation, dual listings, and market fairness — practices tolerated for decades are now being addressed one by one through explicit regulation and policy. The significance lies in the comprehensiveness: rather than piecemeal responses to individual issues, this is a systematic effort to address the structural drivers of the Korea Discount simultaneously.

As both the direction of the policies and the government's commitment to execution have become clear, the view that Korea's structural discount is chronic has started to shift — and this has been one of the foundations of this rally. Below is a detailed look at what policy changes are underway for each major discount factor.

![](images/41c82312b6b02e0eefa6048c58b8d43ff61b2d756ddac41fcf3468d9c802cb86.jpg)  
Source: News reports, capital market interviews  
4. Source: FnGuide, as of May 4, 2026

## 2-1. From 'Controlling Shareholders' to 'All Shareholders' — The Governing Standard Itself Is Changing

Korean companies have long operated under a controlling shareholder-centric decision-making structure, with limited real checks by the board. Recent Commercial Law amendments directly target this structure. Expanding directors' fiduciary duty to 'all shareholders,' along with expanding separately-elected audit committee members, strengthening the 3% rule, $^{5}$ and introducing cumulative voting, are institutional mechanisms to constrain controlling shareholder influence and strengthen board independence. From an investor perspective, these changes build trust that 'my capital is being used for shareholder value,' contributing to a reduction in valuation discounts.

## 2-2. Strengthening Profit Sharing with Shareholders — From 'Retaining' to 'Returning'

Korean companies have long had a strong tendency to retain profits internally even when generating strong earnings. While the US total shareholder return ratio stands at 70% and Japan at 60%, $^{6}$ Korea's figure was just 37% as of 2025. The government has lowered investors' tax burden through separate dividend income taxation, $^{7}$ incentivized higher dividend payouts, and curbed the practice of using treasury share buybacks as a control defense mechanism by mandating their cancellation. The shift in the destination of a company's generated profits — from 'within the company' to 'shareholders' — is providing another foundation for the reduction of valuation discounts.

## 2-3. Inefficient Capital Allocation and Low ROE — Increasing Pressure for Improvement Through the Value-Up Program

Targeting the inefficient capital allocation where generated profits fail to translate into shareholder value, the government and the exchange are prompting companies to explicitly present ROE improvement targets and action plans through Value-Up disclosures. Initial response was slow, but momentum shifted when tax benefits from dividend income separation were linked to Value-Up disclosures. As of April 2026, the number of disclosing companies has surged to 714, and if the 'stock price suppression prevention law' under legislative discussion becomes a reality, an environment in which companies can no longer afford to ignore capital efficiency will firmly take hold. ROE improvement is no longer a company's voluntary choice — it is transitioning to a mandatory requirement demanded by both the market and the policy.

## 2-4. Dual Listings and Stock Price Suppression Practices — Direct Regulation of Structural Discount Factors

Parent-subsidiary dual listings have been a representative factor eroding shareholder value in the Korean market. While the dual listing ratio in the US is below 0.1%, Korea's is approximately 11% $^{8}$ , explaining that the issue is rather structural. Since the current government took office, new dual listings have effectively been halted, and if the stock price suppression prevention law under legislative discussion becomes a reality, maintaining value-destructive structures will become genuinely difficult.

## 2-5. Market Fairness — The End of Slap-on-the-Wrist Punishment

A structure where enforcement, even when violations are detected, was light and slow, has been eroding market trust. With the launch of a joint financial authorities response unit in July 2025, the 'one-strike-out' principle was introduced. When violations are detected, a fine of up to twice the illicit gain, account freezes, and officer employment restrictions are applied simultaneously, and penalties for serious securities crimes have been elevated up to life imprisonment. The signal that the Korean market is transitioning from a 'market where fairness risk can be tolerated' to a 'market where discipline operates' is a significant change that reduces foreign investors' risk premium and contributes to reduction of valuation discounts.

## Yet, KOSPI Still Has a Long Way to Go

Despite the recent rise, the KOSPI's PBR remains low relative to major global markets. Korea's 2026E PBR of 1.9x is significantly lower than the US (4.9x), Taiwan (4.0x), India (2.8x), and Europe $^{9}$ (2.2x). Among all KOSPI listed companies, those trading below 1x PBR decreased modestly from 553 in 2024 to 541 at end-2025, but still 64% of the total trade below the book value. The index has risen, but more than half the market has yet to receive recognition for even its book value.

Exhibit 5
PBR $^{1}$ and ROE $^{1}$ Comparison Across Major Indices  
![](images/8049668d74f9c915e416957f08a4610bbbfcbef445ccac82ca9e025574da87b2.jpg)  
1. Based on 2026/05/04 closing price, 2026E PBR, 2026E forward ROE

Korea's 

[中间内容因长度限制已省略]

g agenda generator, that wins investor trust, rather than a passive vehicle transmitting past results. If a dedicated IR function does not exist, one must be set up immediately.

However, creating an IR organization does not automatically solve the problem. IR can construct the equity story that appeals to the market only if each business division and finance provide their respective plans. IR cannot create that content from scratch. Business divisions want growth; finance wants efficiency. It is the CEO's responsibility to organize the different divisions, resolve conflicts, and drive the coherent company-wide strategy and message. When the CEO leads cross-functional collaboration and communicates directly with the market through Investor Days and similar events, IR becomes a strategic function that moves valuations.

## 3. When Incentives Align, Management and Shareholders Look in the Same Direction

Even the best strategy and strongest CEO intent will fall short if the organization does not follow. And what moves the organization is ultimately the KPI and compensation system. If management's KPIs are tied only to revenue and earnings, capital efficiency improvement will always be pushed to the back burner. What gets measured gets managed. Ultimately, designing performance metrics and compensation systems linked to TSR is the starting point.

For companies in developed markets such as the US, long-term incentives account for more than 70% of compensation, with stock-based compensation such as RSUs and PSUs. TSR acts as a core performance indicator. Recently this trend has been spreading rapidly in Korea. Major domestic companies — Samsung Electronics, Hanwha, SK, Amorepacific, Naver — have successively introduced stock-based compensation, and when management looks in the same direction as shareholders, the entire organization begins to move toward TSR improvement.

![](images/bb031e691ebf8e1d0b167be45188de17005f55da245f874a262041d397759e40.jpg)

## Conclusion

Korea's capital market opened the first chapter of a historic re-rating from 2025 through the first half of 2026. Yet this achievement was led by government-driven policy changes and earnings improvement in a handful of key sectors. For the KOSPI's PBR to leap to the level of the US or Taiwan, the structural quality improvement of the market as a whole — not just a handful of sectors — must provide support. The key is not simply generating more earnings but transitioning to a structure of generating earnings with less capital. It is the quality of earnings, not the size, that determines valuations.

The next phase of re-rating will depend on corporate actions. Companies that reset their strategic orientation toward corporate value maximization, align capital allocation, shareholder returns, and market communication in that direction, and simultaneously change their organizational and incentive systems — these companies will write the next chapter of Korea's capital market.

Finally, one final observation concerns the role of government. The government's contribution to this rally was immense. The compressed institutional overhaul — Commercial Law amendments, Value-Up Program, tax reforms — created market expectations and laid the foundation for the first re-rating. However, the change thus far has been the product of expectations. The Value-Up disclosure participation rate still hovers around 28%, $^{14}$ still well below the Tokyo Stock Exchange Prime Market disclosure rate of 94%. $^{15}$ Many companies still operate with the belief that a low share price is acceptable.

Going forward, it is the government's task to fine-tune regulations at the execution stage and to create the conditions for companies to change. Just as the Japanese government refined regulations persistently over a decade and created a culture where companies internalize shareholder value as the core of management, the Korean government must also continuously drive all listed companies across the market to raise capital efficiency — not just relying on the structure of a few sectors like semiconductors, shipbuilding, and defense.

## Authors

![](images/2785bec2378f4bcb4be66d8f9fd9636c1cebffeb18973379a73c445c8392967a.jpg)

Joonho Lee
Managing Director and Senior
Partner, Seoul

Lee.Joonho@bcg.com

![](images/18636f1dc7b1468ba98b398b006dd3b28c0dd8d11c136527ba9a8c3bf3f4809f.jpg)

Seoha Kim
Managing Director and Partner,
Seoul

![](images/a332522299f420e44a0dca9e8535ec8450ff88cec1726d5077a43f48797bffda.jpg)

Kim.Seoha@bcg.com

![](images/462d8ffd243fe1fe466f45486d0b888b24368892176ce0b9eda474087b0eda52.jpg)

For Further Contact

If you would like to discuss this report, please contact the authors.

Ichiro Kaku
Managing Director and Senior
Partner, Tokyo

![](images/bbb4971958d28a5e78ea67e0026fa1f3c9094ca7a5e47cb89dadf8c3049d39b0.jpg)

Kaku.Ichiro@bcg.com

Kyungjae Lee
Project Leader,
Seoul

![](images/a52cd9604643b33786172ea138ee5cfb12db42382acbbb968abaf40273e883df.jpg)

Lee.Kyungjae@bcg.com

Acknowledgments

The authors are grateful to a number of colleagues for their continued support and assistance. They include Eugene Khoo and Shi Wei Lim in BCG Value Science Center and the members of the CFS Research Team for their specific contributions for quantitative analysis in this report.

For information or permission to reprint, please contact BCG at permissions@bcg.com. To find the latest BCG content and register to receive e-alerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on LinkedIn, Facebook, and X (formerly Twitter).

© Boston Consulting Group 2026. All rights reserved.

![](images/825aba20180f6ff7baff600fde362773b3697c4331800906874ef55c78a83466.jpg)
"""

【DeepSeek 交稿硬约束】
1. 全文只服务一个主判断。不要按原报告目录逐段摘要，也不要把多个结论平铺成清单。
2. 开头直接使用原文中最有辨识度的事实、数字、对比或矛盾切入；禁止用“在……背景下”“随着……”“近年来……”空泛起笔。
3. 正文至少使用三个原文锚点：一个可核验的数字或日期、一个具体主体/项目/制度名、一个比较或因果关系。判断必须紧挨证据，保留“可能、样本显示、报告认为”等限定词。
4. 句子长短要自然变化。大多数段落写 2-4 句，允许用一句短句收住；不要连续使用“报告指出、这意味着、换句话说、真正重要的是、值得注意的是”等模板转折。
5. KC评论只写一条具体、平白的解释或提醒，不能复述正文，不能提推广、原文领取、完整报告、读者行动或网站。
6. 禁止单独设置“该报告未解决的问题、报告尚未回答、研究留白、开放问题、报告局限、还需追问”等小节，也禁止用问句收尾。若原报告明确写了限制，只能在相关正文中用一句客观陈述自然带过。
7. 最后一段必须仍是实质内容或 KC评论。不要添加总结、结语、延伸阅读、继续阅读、关注引导、社群、扫码、网站或任何 CTA；系统会统一处理文末固定信息。
8. 不要虚构“我读完后”“我们采访了”等个人经历，不要故意口语化或加入情绪。人工编辑感来自具体证据、准确取舍和自然节奏。
9. 输出前自行核对：标题与导语不重复；主标题和每个小标题都是完整、中性的事实表达，不评价好坏、不制造冲突；没有元话语、推广语和未解问题栏目。只输出最终 Markdown，不输出核对过程。
