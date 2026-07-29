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
## As Scale Grows, So Does Ambition

Global Principal Investors

Report 2026

![](images/46008571511972f2fd082874b0d88f9f324627ef71c993181761145f4daac3c5.jpg)

![](images/0f72d1d86b20282d12afe9c21af2cc3fd9cebabad57c3a4d521eae7964f0842b.jpg)

![](images/2f47d11f9a9a54d3a3b2f2967cc8758140f56465498156c8f4e1f7b8101afa91.jpg)

![](images/37bba191dc349aca6c8af90ecc3cd7b98a7a6d507b61c82fcbfd08b399e6cb26.jpg)

Principal investors are playing a more active role in an increasingly complex market landscape 01
How principal investors are changing the way they lead 02
How general partners can partner with principal investors 03

## Principal investors in a new era: expanding influence, active strategies, and a market shaped by geopolitics and AI

![](images/153a1d3d8d7a0c4e692b6b625b2fd47369b8c42b1b5addee925ff583cdbc2af4.jpg)

The PI universe continues to expand in scale and influence, with \$43T in AuM in 2025 and ten new sovereign vehicles established in 2025 alone. Family offices are also growing and increasingly professionalizing

![](images/bf46ecc8f19bb46ca6e63953665ddf6a7518914261a88939433354b8a550476a.jpg)

Private markets allocations have grown steadily over the past decade, led by PE and infrastructure. Recent years have seen longer holding periods and weaker distributions, driving a concentration of capital toward top-tier GPs

![](images/10367c43fa9f7328f6c95a5be21a54e2326ee96a3042763a1ca3156052a973ed.jpg)

More sophisticated PIs are increasingly experimenting with direct, co-investment, and platform capabilities. In some cases, these are emerging as peers and partners for GPs

![](images/19f546dea524db6f657666d266c786c1d47b535c29be15e25ea566897f685a74.jpg)

Geopolitical uncertainty has increased structurally since 2020, with likely implications for geographic allocation, sector mix, and liquidity positioning—particularly for SWFs with explicit national mandates

![](images/19aef62916640d70226340c87a7093b0ca89fc146e62bad73e0fd484aaef976e.jpg)

AI has emerged as a defining thematic area for PIs—both as an investment opportunity across the full stack and as an operational capability. Leading PIs are actively building coordinated AI exposure and embedding AI across fund operations and value creation

## PIs continue to increase in influence as concentrated sources of capital that can shape capital flows and yields across markets

Principal Investors have grown in scale and influence over the last decade, making up \~30% of the total assets under management globally

TOTAL AUM BY PRINCIPAL INVESTOR TYPE (\$T)

![](images/f78168f62a526902809b7ad195000e78050648c084bd66a57214fe5953ba089f.jpg)  
Sources: Global SWF; BCG analysis.  
GLOBAL PROFESSIONALLY MANAGED AUM (\$T)

![](images/fd0ecfea93dad5dd50b56ce193ff81819b28c8d67869d5d05552ede64399233d.jpg)  
Note: PI AuM refers to fair value of assets as reported by each fund, or estimated by Global SWF based on tracked investment activities where fund-level data is unavailable. Global AuM corresponds to assets sourced from each region and professionally managed in exchange for management fees; it includes captive AuM of insurance groups or pension funds where AuM is delegated to asset management entities with fees paid. Overall, 44 markets are covered globally, including offshore AuM (which is not included in any region). For all countries where the currency is not US dollar, end-of-year 2025 exchange rate is applied to all years to synchronize current and historic data.

\- Principal investors—sovereign wealth funds and public pension funds—have grown from \$21T in AuM in 2015 to \$43T in 2025, a compound annual growth rate of 7%, and are projected to reach \$59T by 2030

\- SWFs have grown more rapidly than PPFs over the decade, driven by sustained commodity and fiscal surpluses, stronger-than-expected market returns, and the creation of new vehicles. Ten new sovereign funds were established in 2025 alone

\- At roughly 30% of global AuM, this capital base is large enough to move markets. Allocation decisions of a small number of institutions—where to deploy, which asset classes to favor, which geographies to reduce—can shift sector flows, compress or widen credit spreads, and affect asset prices at scale

## New sovereign vehicles are entering private markets with more strategic and active mandates, further expanding influence

SWFs ESTABLISHED (#)

![](images/997e2c5c7f0055a8f75c2dad569c220baf2b1d5d23e1468bd99e2bbfc0be502a.jpg)

<table><tr><td>SWFs established in 2025</td><td>Country</td></tr><tr><td>Danantara</td><td>Indonesia</td></tr><tr><td>Chinggis</td><td>Mongolia</td></tr><tr><td>Botswana SWF</td><td>Botswana</td></tr><tr><td>Eksab Saudi</td><td>Saudi Arabia</td></tr><tr><td>Eswatini SWF</td><td>Eswatini</td></tr><tr><td>FIS DRC</td><td>DR Congo</td></tr><tr><td>Kenya SWF</td><td>Kenya</td></tr><tr><td>Oyo SWF</td><td>Nigeria</td></tr><tr><td>Syrian Sovereign Fund</td><td>Syria</td></tr><tr><td>Uzbekistan NIF</td><td>Uzbekistan</td></tr></table>

\- The new wave of sovereign vehicles reflects a shift from surplus management to state-led transformation, with reserves and windfalls being organized into investable platforms for priority agendas

\- A growing number of new vehicles sit closer to strategic investment funds than traditional savings SWFs, explicitly pursuing a double mandate of financial return plus domestic economic impact

\- The pipeline for new funds remains active as well, with several countries openly exploring new SWFs (often to monetize state assets or repurpose reserves). This could add a further wave of inorganic growth over the next few years. Examples of this pipeline include:

\- US: Executive order signed Feb 2025 to stand up a fund from \$5.7T federal asset base

\- Taiwan: President committed to first-ever SWF in May 2025, drawing on \$600B in reserves

\- South Korea: New national fund announced Dec 2025, seeded at \$100B from \$0.9T in state assets

\- Canada: Canada Strong Fund announced Apr 2026, seeded at \$25B to back major national projects
- India: \$50B sovereign fund in design, backed by government stakes in public companies

## Family offices are also becoming an influential pool of capital, with scaled FOs increasingly influential capital allocators

## # OF FOs (THOUSANDS) YEAR-ON-YEAR AND REGIONAL DISTRIBUTION (%)

![](images/a05f6a50acc0a01820cebdeb9b4351aba6d332463b28087002300141ccd21076.jpg)  
Sources: Preqin; BCG Global Asset Management Market Sizing; BCG analysis.

Family office growth driven by Asia, while North America and Europe remain the largest and most established bases

\- The total number of family offices has increased steadily since 2019, with Asia contributing to \~42% of growth, equal to NA and EU combined, even as the latter continue to represent the majority of installed base

\- With over \$6T in AuM, family offices are an increasingly influential source of capital

Increasing institutionalization underway across FOs, large FOs transitioning to more direct investing

• Large family offices are building dedicated CIO-led investment teams with formal governance structures, reflecting a shift from founder-led capital stewardship towards professionally managed, multi-generational platforms

\- Scaled FOs are transitioning from passive fund allocations toward active, direct and control-oriented investing, becoming quasi-GP platforms

## Private markets are becoming a larger and more actively managed sleeve for major PIs over the last decade

Across SWFs and PPFs, the share of PE and infra allocation has increased meaningfully over the last decade
ASSET ALLOCATION FOR PRINCIPAL INVESTORS (%)

![](images/821473d071a6c13055cff8cac8870175e077d27c7031dc6779a755a5c2f46c1e.jpg)  
Sources: Global SWF; BCG analysis.  
Note: Percents may total more than 100 due to rounding. Global SWF sources allocation information from the funds directly (annual reports and websites) if publicly available; otherwise, estimates are provided based on their knowledge of the funds.

Private market allocations have grown steadily as a share of PI portfolios over the past decade, driven by PE and infra

\- SWF PE allocations have risen from \~23% to \~26% of AuM; PPF PE allocations have grown more materially, from \~6% to \~11%

\- Infrastructure has followed a similar trajectory, growing from \~10% to \~15% for SWFs and from \~3% to \~6% for PPFs

\- As overall AuM has grown, higher allocation means absolute capital flows into private markets have expanded substantially

Infrastructure has matured from a niche into a core allocation, driven by its return and diversification profile

\- PI allocations to infrastructure grew at a 13% CAGR from 2015 to 2025—the second-highest growth rate across asset classes after PE, reflecting its appeal as a natural inflation hedge with stable, contracted cash flows

\- More recently, the asset class has been further supported by rising investment in digital infrastructure and green energy, with infrastructure outperforming PE over a one-year horizon

As PE sleeves have expanded, PIs are pushing for greater fee efficiency and direct control over execution

\- PIs are increasingly pursuing co-investments and direct deals alongside GP relationships, with targeted co-investment ratios shifting from \~20% to 25% of fund commitments in the early 2000s to close to 100% for larger investments today

\- Average deal sizes have stepped up materially, reflecting both larger balance sheets and greater conviction

UNREALIZED VALUE (\$T)

## However, at the same time holding periods in private markets have risen, locking in liquidity and constraining reallocation

## Average and median holding periods overall and by region

AVERAGE AND MEDIAN HOLDING PERIOD (YEARS), FOR EXIT YEARS 2014–2025

![](images/909026b7dd20ba14dea36cb5406e2a1036d9598fdd564fedaa544359ce88b251.jpg)  
AVERAGE PRIVATE EQUITY HOLDING PERIOD (YEARS)

![](images/7372a4473376278bc29261828b99a0af23c4f2298b755352ec0b316619e82744.jpg)

HOLDING PERIOD FOR COMPANIES (#)  
![](images/c7dd40d0c0638965d53eabf73b0bb372a59a3080811958c61518caefb9e5bd80.jpg)

![](images/0ae46d404943250da106a08098d370957dad9cbe5a81d0e7d3b74593eb4827b4.jpg)

Holding periods have lengthened materially since the 2020 trough across all major regions
Both average and median holding periods declined into 2020 but have risen steadily through 2025 across North America, EU, and Asia—with North America peaking highest in 2024 before moderating

The gap between average and median signals a concentration of longer-held assets
Across the full period, the average consistently sits above the median, indicating a subset of deals held significantly longer than the typical investment

Compared to earlier vintages, a growing share of assets are being held beyond five years
The proportion of companies held for more than five years has increased steadily since 2020, reflecting delayed exit activity and extended ownership cycles

Unrealized value has reached record highs
As holding periods extend and exits slow, unrealized value has accumulated to record highs, constraining capital recycling across the ecosystem

Sources: Preqin; BCG analysis.

## Distributions have lagged capital calls, resulting in negative cashflows and locked capital for LPs

Cumulative capital called and distributed by GPs $^{1}$ GLOBAL (T)

![](images/e3842895abae91377fe0322f993074728e3d76c72754247e3d442fdaf4d6a0f1.jpg)  
Global buyout distribution as % of buyout NAV

![](images/feca1ada202739069d9625a49c85e21550f4cc44e06dfdfb19f414ee9f2b1604.jpg)  
Sources: Preqin; BCG analysis.  
$^{1}$ Called-up capital refers to LP’s aggregate commitments to the partnership that have been contributed to the partnership. Distributed refers to the called-up capital that has been distributed or returned back to LPs. Net distributed is calculated as the difference between distributed and called-up capital.

Cumulative LP cash flows remain negative
Since 2018, capital calls have exceeded distributions, with the gap widening post-2020 as exits slowed. LPs have therefore remained net cash contributors over the period

Buyout distributions remain below historical norms
Global buyout distributions as % of NAV have declined from pre-2020 levels, reinforcing liquidity pressure

Delayed realization is driving limited distribution
Weak M&A activity and volatile markets have extended holding periods and built exit backlogs as sponsors are reluctant to sell below target valuations

Higher rates have increased the cost of illiquidity
Attractive public yields have increased opportunity cost of locked capital, driving need for secondaries and CVs to return capital

## Consequently, flight to quality is being seen with PIs becoming more selective and discerning in how they engage private markets

Commitment from SWFs and PPFs to GPs  
![](images/06585fa0c52c443f8f78e86f52c6b78aff6508df171867b5b00989d0c45c31a0.jpg)

Total annual fund-raising for closed-end funds split by ranking brackets $^{1}$  
![](images/be45c9e4c63993ca412b9c117f7ca83d402c60b111d11c8722d86cfb6ad3dc3a.jpg)  
Sources: Pitchbook; BCG analysis.  
Note: 2019 average commitment value is high due to SoftBank's large commitments in the year to Gulf Cooperation Council SWFs. Average commitment value is calculated based on where the size of commitment is disclosed by Pitchbook and includes commitments from top 100 PPFs and SWFs.  
$^{1}$ Includes flagship buyout/growth/VC/infra fund closes, continuation vehicles, and co-investment funds.

Flight to quality evident with PIs becoming more selective with funds they engage with

\- Fewer commitments (−45%, 2020 vs. 2025), coupled with larger average commitment sizes (+5%, 2020 vs. 2025), indicate that capital is being concentrated in a smaller set of high-conviction managers

\- Fundraising for closed-end funds is increasingly concentrated in the largest managers, with the top five GPs accounting for \~41% and the top ten for \~59% of fundraising in 2024

\- Emerging and smaller GPs need to prove they can deliver differentiated access / edge to be attractive against larger GPs or competing mid-market fund

Governance and capacity constraints are further reinforcing concentration in GPs

\- With more direct/co-invest activity and monitoring needs, investors are rationalizing bandwidth. Fewer, deeper relationships enable better pacing coordination and more efficient oversight

## Growth in secondary markets creating viable, alternative investment opportunities for PIs

Growth of secondaries and cumulative value of PE continuation vehicles
TRANSACTION VOLUME IN SECONDARY MARKET (\$B) AND SHARE OF GP-LED TRANSACTIONS (%)  
![](images/9fcdeb183b2ff0f22f78f0ed158dc76bda7b23f451163863cc9866c2989c7ca6.jpg)

Cumulative value of PE continuation vehicles
PE CONTINUATION VEHICLE FUND SIZE (\$B) AND PE CUMULATIVE VALUE (%)  
![](images/0157c36bc556e4400d87ea0391a2521e46ab332744f996ed232dc2a11bfc5dff.jpg)  
Sources: Evercore 2025 Secondary Market Survey Highlights (Jan 2026); Pitchbook; Jefferies & UBS; BCG analysis. Note: CV = continuation vehicle.

## Capital-efficient entry at a discount

Secondary buyers acquire stakes in mature funds at NAV discounts, typically 5%–15% for PE, mid-single digits for infrastructure, accessing high-quality portfolios below intrinsic value, an advantage structurally unavailable in primary fund commitments

## J-curve eliminated with immediate yield from day one

Secondary entry skips the capital call and negative return period entirely. For PIs managing against long-dated obligations, receiving distributions from mature, cash-generating portfolios immediately is far preferable to waiting 5–7 years for primary fund cashflows to turn positive

GP-led CVs offer curated access to proven assets
GPs are selectively migrating their highest-conviction portfolio companies into continuation vehicles. Secondary buyers gain concentrated exposure to performing assets with an established track record, rather than a diversified blind-pool commitment at fund inception

## Several PIs are also shifting to a more direct posture, spanning direct deals, co-investments, and third-party platform building

Average ticket for co-investment
fundraising is at all-time high
CO-INVESTMENT FUNDRAISING

![](images/7e1ab03d9533feee93813079f8e736983ffc78f73dadf0db1c6f06d122eaaa7e.jpg)  
Direct deals as share of PI deals has expanded

![](images/4f9a288c27728a07434f747ed7825a54cb7f7eaa1b1881e981e63bb79996bd7f.jpg)  
Sources: Preqin; Pitchbook; Mubadala Capital; Seviora; Financial Times; BCG analysis.

## PIs are also creating platforms for raising and managing third-party capital

## Mubadala Capital

• Used acquisitions to quickly add fundraising capability, products, and client channels—most notably owning 68% of Fortress from SoftBank

• Commitments from TIAA, SoftBank, StepStone Private Wealth, Mutual of Omaha Foundation, among others

## Seviora

\- Wholly owned by Temasek and operating through a group of asset management companies

\- Subsidiaries have raised commitments from NUS Endowment Fund, Singlife, Avendus, Aozora, among others

Co-investment fundraising has grown, with capital consolidating into fewer, larger programs
Average co-investment ticket sizes have reached an all-time high of \$336M in 2025, up from \$104M in 2015—even as fund counts have pulled back from their 2020 peak, signaling a concentration of capital into larger, more selective partnerships

## Direct deals as a share of overall PI activity have expanded meaningfully

Share of LP direct deals in PI deals has expanded, reflecting a sustained structural shift toward direct ownership and away from intermediated fund exposure

Leading PIs are moving beyond LP roles to manage third-party capital directly
Examples like Mubadala Capital and Seviora show PIs moving from “LP+” to platform managers, using acquisitions and multi-manager structures to raise external capital and institutionalize investing edge

## Geopolitical realignments likely to reshape PI capital flows, influencing growth and yields across markets

## Geopolitical shifts and realignment likely to shape global allocations, both geographically and sector-wise

US
Still the largest economy and reserve currency, though facing selective capital reallocation

Europe
Potential capital reallocation from the US amid diversification efforts

Developed Asia
Potential capital
reallocation to
diversify portfolio risk

Emerging Asia
Limited in liquidity depth
but offers significant
growth opportunity

![](images/1e1db032719736ac52ba6ccb499dd0b329d06f5c4dbded0dd718373819e30494.jpg)

China
Access to high-quality deals increasingly constrained for Western-affiliated PIs

## GLOBAL PI ASSETS U

[中间内容因长度限制已省略]

 a core relationship tool, enabling deal-by-deal participation alongside primary funds

## Co-investment structures are emerging as the preferred vehicle for FO private markets exposure

\- PE fund commitments have fallen while interest in co-investment and direct deal participation has grown. For GPs, this represents a growing opportunity to engage FOs at the deal level rather than through committed capital vehicles

\- Larger proportion of FOs anticipate an increase in private equity direct investments rather than private equity fund investments

\- Historically, larger FOs have been more active in direct investments, reflecting stronger in-house capabilities

FO SENTIMENT ON CAPITAL ALLOCATION IN PE (2025) $^{1}$

<table><tr><td></td><td>Increase</td><td>No change</td><td>Decrease</td></tr><tr><td>Private equity direct</td><td>28%</td><td>59%</td><td>13%</td></tr><tr><td>Private equity funds</td><td>24%</td><td>59%</td><td>17%</td></tr></table>

## Subscale FO capital can be aggregated through feeder vehicles or platform partnerships

\- Structured access vehicles can reach FOs below traditional minimums, reducing LP concentration risk

![](images/21a8c2ee5ef122d152233cc97dfa9cef7ade808be98bf85cd169d45fa6e33e41.jpg)

iCapital partnered with Blackstone and KKR to distribute fund access via standardized feeder structures, opening each GP to a wider FO universe

## Platform opportunity: structures where the FO network itself generates proprietary deal access

\- A small number of GPs may find value in FO-native structures where families are genuine platform participants

![](images/38514d392a1b8d0a5c4b318c28846bc5e1a6a785b549aae9f32ae5eff12241c2.jpg)

Built around major tech founder families; the network's relationships generate proprietary late-stage deal access that defines the platform's competitive edge

## About the Authors

Benjamin Sheridan is a managing director and senior partner in BCG's Singapore office. You may contact him by email at sheridan.benjamin@bcg.com.

Benjamin Entraygues is a managing director and senior partner in BCG's Paris office. You may contact him by email at entraygues.benjamin@bcg.com.

Ihab Khalil is a managing director and senior partner in the UAE office of BCG. You may contact him by email at khalil.ihab@bcg.com.

Christy Carter is a managing director and senior partner in the New York office of BCG. You may contact her by email at carter.christy@bcg.com.

Mark Harris is a managing director and senior partner in BCG's Toronto office. You may contact him by email at harris.mark@bcg.com.

Saleh Al-Ateeqi is a managing director and partner in the UAE office of BCG. You may contact him by email at alateeqi.saleh@bcg.com.

Andrew Claerhout is a partner and director in BCG's Singapore office. You may contact him by email at claerhout.andrew@bcg.com.

Shobhit Shubhankar is a partner in BCG's Singapore office. You may contact him by email at shubhankar.shobhit@bcg.com.

Katharina Obinger is a partner in the UAE office of BCG. You may contact her by email at obinger.katharina@bcg.com.

## Acknowledgments

The authors would like to thank Gwenhael Le Boulay, Johannes Glugla, Eric Ritsema, James Loughridge, Dieuwertje ten Feld, Jade Tan, Jonathan Chin, Aisha Khandelwal, Gloria Tan, Alexander Raju, and Angela Everitt for their support in preparing this report.

## Disclaimer

The services and materials provided by Boston Consulting Group (BCG) are subject to BCG's Standard Terms (a copy of which is available upon request) or such other agreement as may have been previously executed by BCG. BCG does not provide legal, accounting, or tax advice. The Client is responsible for obtaining independent advice concerning these matters. This advice may affect the guidance given by BCG. Further, BCG has made no undertaking to update these materials after the date hereof, notwithstanding that such information may become outdated or inaccurate.

The materials contained in this presentation are designed for the sole use by the board of directors or senior management of the Client and solely for the limited purposes described in the presentation. The materials shall not be copied or given to any person or entity other than the Client (“Third Party”) without the prior written consent of BCG. These materials serve only as the focus for discussion; they are incomplete without the accompanying oral commentary and may not be relied on as a stand-alone document. Further, Third Parties may not, and it is unreasonable for any Third Party to, rely on these materials for any purpose whatsoever. To the fullest extent permitted by law (and except to the extent otherwise agreed in a signed writing by BCG), BCG shall have no liability whatsoever to any Third Party, and any Third Party hereby waives any rights and claims it may have at any time against BCG with regard to the services, this presentation, or other materials, including the accuracy or completeness thereof. Receipt and review of this document shall be deemed agreement with and consideration for the foregoing.

BCG does not provide fairness opinions or valuations of market transactions, and these materials should not be relied on or construed as such. Further, the financial evaluations, projected market and financial information, and conclusions contained in these materials are based upon standard valuation methodologies, are not definitive forecasts, and are not guaranteed by BCG. BCG has used public and/or confidential data and assumptions provided to BCG by the Client. BCG has not independently verified the data and assumptions used in these analyses. Changes in the underlying data or operating assumptions will clearly impact the analyses and conclusions.
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
