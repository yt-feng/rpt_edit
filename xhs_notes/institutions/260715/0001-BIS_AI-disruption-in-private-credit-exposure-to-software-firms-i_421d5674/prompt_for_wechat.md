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
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须短、锐利、可转发，优先 20-35 个中文字符，最长不超过 35 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 要兼顾微信搜一搜：尽量包含一个高意图关键词，例如行业/公司/政策/AI/房地产/半导体/光伏/消费/美联储/利率/通胀/机器人/比特币等。
- `# 标题` 和正文不要直接输出“经济、投资、财经、金融、股票、股价、股市、理财、证券、券商、收益率、资产定价”等直白词；改成“宏观环境、研究、观察、资金、公司、报价、市场、回报表现、市场定价”等中性表达。
- 涉及中国、国内、内地、大陆、人民币、A股、港股时，必须使用中性客观表达；不要写“不好、不行、疲弱、低迷、恶化、危机、衰退、崩盘、放缓、压力、拖累、唱衰”等负面判断。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`国际清算银行`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
- 标题禁止出现 GS、JPM、JEF、NOM、BARC、MS、DB、Citi、Ticker、文件编号；如果原文只有英文机构名，请翻译为中文机构名。
- 标题冒号后不要重复机构或来源类型，禁止“联合国贸发会议：联合国贸发报告，……”“麦肯锡：麦肯锡报告称，……”这类写法；冒号后直接写判断或变量。
- 标题只能保留一层信息，不要把多个长分句全部塞进标题；如果原始标题有三段以上信息，只取最有传播性的主判断，其余放在正文第一段自然展开。
- 如果报告是单一公司/个股报告，标题和正文只能写公司情况、行业变化、业务进展、竞争格局和报告里的事实；禁止出现目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO 等任何卖方操作口径。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
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
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，20-35 个中文字符。
2. 开头 2-3 段：直接给出主判断、为什么现在重要、报告提供了什么新信号；自然带出 4-6 个长尾关键词，覆盖国家/行业/公司/政策/数据/技术词，但不要写成关键词堆砌。
3. 3-4 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份国际清算银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# BIS Bulletin

## No 128

AI disruption in private credit: exposure to software firms in BDCs

Fernando Avalos, Giulio Cornelli and Egemen Eren

BIS Bulletins are written by staff members of the Bank for International Settlements, and from time to time by other economists, and are published by the Bank. The papers are on subjects of topical interest and are technical in character. The views expressed in this publication are those of the authors and do not necessarily reflect the views of the BIS or its member central banks. The authors are grateful to Raphael Auer, Mathias Drehmann, Jon Frost, Blaise Gadanecz, Gaston Gelos, Bryan Hardy, Pablo Hernández de Cos, Daniel Rees, Andreas Schrimpf and Costas Stephanou for comments, Yota Eilers and Vivekananda Allam for excellent analysis and research assistance, and to Nicola Faessler and Danielle Ritzema for administrative support.

The editors of the BIS Bulletin series are Gaston Gelos and Frank Smets.

This publication is available on the BIS website (www.bis.org).

© Bank for International Settlements 2026. All rights reserved. Brief excerpts may be reproduced or translated provided the source is stated.

# AI disruption in private credit: exposure to software firms in BDCs

## Key takeaways

\- Business development companies (BDCs) have lent around \$115 billion to software firms, which represents about a fifth of all their lending and over 80% of their fast-growing technology portfolios.

\- Borrowers' revenue uncertainty posed by generative artificial intelligence has not affected these loans yet, and neither BDCs nor their equity investors have priced software exposure differently.

\- Recently, credit spreads have narrowed, reducing the buffers to absorb losses, and a few large BDCs are exposed to a shared pool of borrowers, though low leverage and secured lending may limit spillovers.

In recent years, direct lenders, such as private credit firms, have built up large exposures to the software sector which could now pose risks due to generative artificial intelligence (AI) disruption. Software has been among the most reliable cash flow businesses of the past decade, with recurring subscription revenues, high margins and low capital needs, which made it attractive to direct lenders. Yet software firms' revenues are now highly vulnerable to AI, which can both substitute for existing products and lower development costs, reducing barriers to entry and intensifying competition. This also raises questions about the pricing of AI disruption risk by lenders and their investors, as well as the future performance of the affected lending portfolios if this risk materialised.

Business development companies (BDCs) offer an unusually clear view into the private credit ecosystem and its exposures. BDCs are a type of private credit intermediary in the United States that typically lends to small or mid-sized firms (Davydiuk et al (2024)). BDCs originate one fifth of all US direct loans, and thus are broadly representative of direct lenders (Doerr et al (2026)). They have lent around \$115 billion to software firms, which represents about a fifth of all their lending and over 80% of their technology portfolios. As of end-2025, there are about 170 BDCs, which are required to report their holdings loan by loan on a quarterly basis to the US Securities and Exchange Commission (SEC), covering some \$550 billion in assets. $^{1}$ The rest of the private credit ecosystem is comprised of a variety of funds operating under different legal provisions and remains highly opaque regarding their exposures. This makes BDCs a useful case study of the vulnerabilities which may be building up in the unobservable segments of private credit.

While current pricing and performance indicators do not point to stress, they may understate the vulnerabilities lying beneath the surface. Spreads within software loans and across different sectors do not show systematic differences. Similarly, valuations of publicly listed BDCs do not differ depending on the respective weight of software loans in their overall portfolio. Limited leverage and a high incidence of secured lending may have in part alleviated concerns about elevated cash flow uncertainty due to AI disruption. But narrowing spreads in recent years have reduced lenders' cushions to absorb potential losses. Moreover, each borrower usually draws on many lenders at once, so a shock might surface across many BDCs simultaneously. Since the lending side of the market is also concentrated, a handful of major BDCs would bear a larger part of the losses in the case of a sizeable credit event. Funding fragilities in non-traded BDCs might add to these strains. Opaque exposures beyond BDCs could amplify the impact of any disruption from generative AI, leaving the sector more vulnerable than its credit metrics suggest.

![](images/e1c7139a06358cad0c70edb0cdeea910033bcc927d2f204fe8247bb34dddbbee.jpg)  
$^{1}$ Software lending as a share of BDC IT lending.  
Sources: PitchBook Data Inc | LCD; authors' calculations.

## Software is now a large exposure for direct lenders

BDC lending to software has grown into one of the sector's largest exposures. $^{2}$ Over the past decade, these funds tilted heavily towards technology: lending to the information technology (IT) sector climbed to nearly \$140 billion, about a quarter of all BDC loans and now its second largest sector after business services, which might also be impacted by generative AI (Graph 1.A). $^{3}$ Almost all of that growth was in software, which now accounts for more than 80% of the IT portfolios, or around \$115 billion (Graph 1.B). This trend contrasts with the sectoral composition of the broader US economy, where IT accounts for a smaller and more stable share of output. $^{4}$

The rise of generative AI heightens uncertainty about the revenue streams of software firms through direct product substitution and margin pressures. For some products, AI tools can now do the same job at lower cost, taking revenue away from the borrower by substituting software directly. For other products,

## Software is a large and growing exposure for direct lenders

2 We use BDC holding-level data from PitchBook Data Inc. Around one quarter of the BDCs in our sample are publicly listed. Our sample includes 18,097 borrowers over the period Q1 2015–Q4 2025. Sector classifications follow PitchBook's proprietary industry system – shaped by commonly used systems such as the North American Industrial Classification System (NAICS), Standard Industrial Classification (SIC) and Global Industrial Classification Standard (GICS) – and are structurally most comparable in granularity to the GICS. These data are available with a reporting lag.

$^{3}$ The rising share reflects new lending rather than higher valuations, as portfolio weights computed on cost and on fair value move together.

4 For more information, see US Bureau of Economic Analysis, Gross Output by Industry.

incumbents can fold AI into their own offering and keep their customers, but at thinner margins, as AI tools enhance competition by reducing barriers to entry. $^{5}$ Either way, the cash flows that service these loans have become subject to greater uncertainty than in the past, even if reported earnings do not show it yet. And because these loans typically run for several years, the impact of fast-paced AI improvements could surface before their eventual maturity date.

## Software risk pricing remains undifferentiated for lenders and equity investors

Over the past few quarters, despite the gradual increase in the risk of AI disruption, lenders did not charge a higher spread to software borrowers. Instead, credit spreads have fallen both within and across sectors and largely converged. By late 2025 software, other-IT and non-IT borrowers paid broadly similar spreads on their loans (Graph 2.A). $^{6}$ The compression has been steepest for newly issued loans, the spreads on which fell faster than those on outstanding loans. Spreads were also lower for loans originated by non-listed BDCs, arguably the segment under the least market scrutiny (Graph 2.B).

These loans are performing well so far, and generative AI has yet to leave a visible mark on realised credit quality. Less than 1% of software loans are behind on payments, a smaller share than for the rest of the BDC portfolios. Other measures – eg the share written down as impaired and signs of cash-flow strain $^{7}$ – tell the same story (Graph 2.C). These measures look backward and are computed by managers

![](images/d1e071a5907ab16cb153b2ca59cdb81b89fd6d47b63e6a3aff5cf833b751d7c6.jpg)  
$^{1}$ Value-weighted spread over the base rate on BDC loans.  
Sources: PitchBook Data Inc | LCD; Bloomberg; authors' calculations.

5 These are mostly middle market software firms rather than large, listed software groups. About three quarters of BDC software exposure is in horizontal and workflow categories such as productivity, application and automation tools, where AI substitution is most direct.

6 A panel regression on 152,116 observations of IT and software spreads for the period Q1 2015–Q4 2025 yields similar results. The sample includes 208 BDCs and 2,302 borrowers. The analysis also suggests that spreads between software and other IT loans do not differ over the sample period, even after removing heterogeneity (by introducing fixed effects) related to time period, BDC identity and investment type, while controlling for the tenor of the loan, its accrual status and principal size.

7 The proxy for cash flow distress is the payment-in-kind rate. Payment-in-kind is a common arrangement in private markets or structured financing deals where interest or dividends owed on a debt or equity instrument are not paid in cash but instead by issuing additional securities, such as more debt or equity.

based on their own assessments, but they point consistently in one direction, and the loans face no nearer-term wall of maturities than other sectors. Credit metrics may also be delayed in reflecting current risks for structural reasons: a revenue shock takes time to translate into a missed payment, and payment-in-kind arrangements – which allow borrowers to defer the cash outlays of debt servicing – can postpone the point at which strains become visible.

Equity investors, too, have drawn little distinction in pricing BDCs by software sector exposure. This is despite valuations of equity indices of software firms having underperformed the broader technology sector for several months. Coming out of the pandemic, software-related stocks saw a rally that, by end-2021, had created a significant valuation premium over the broader IT sector. Since December 2022, after the release of ChatGPT, software's valuation premium narrowed and ultimately turned into a discount by end-2025 (Graph 3.A). Conversely, BDC valuations tell a different story: BDCs with high and low software exposure trade at similar price/dividend ratios, with no discount for software concentration (Graph 3.B). $^{8}$ This may partly reflect that BDCs are held for their distributions, and so long as dividends hold up and distance to default does not fall below some threshold, a slow-building credit risk does not show in prices.

Undifferentiated risk pricing can be read in two ways. A benign view is that BDCs target a consistent borrower risk profile regardless of the sector. Thus, BDCs extend credit only to software firms whose fundamentals match those of their other borrowers, and similar spreads are warranted. Similarly benign would be the case in which risks posed by generative AI to the software sector are overstated. A less reassuring view could be that lending standards have been loosened by competition in credit origination during a prolonged private credit boom. In the latter case, if risk is underpriced, a shock is more likely to bring correlated losses and abrupt repricing.

## Equity markets attach little discount to BDC software exposure

A. Valuations of software firms have underperformed the broader technology sector recently  
![](images/81b4c1bcbba0de65e96baa9a59ef44f82ba3333952c18a41c81318fd11659a40.jpg)  
$^{a}$ ChatGPT released to the public (November 2022).

Graph 3

B. From the second half of 2025, valuations of BDCs with high and low software exposure have converged $^{1}$  
![](images/b099327e30488d47840fd963903dcbe8af9310d531355e9044ef439393cad1d3.jpg)  
$^{1}$ Based on listed BDCs which are split into the top tercile (high) and bottom tercile (low) by software exposure over the period Q1 2020–Q4 2020. Each group contains 17 BDCs.  
Sources: PitchBook Data Inc | LCD; Bloomberg; authors' calculations.

## Declining spreads, concentrated exposures and opaque interconnections

While current loan pricing and performance indicators do not point to imminent stress, there may be vulnerabilities hidden beneath the surface.

Spread compression has eroded the cushion against potential losses in BDC loan portfolios. That is particularly surprising in the case of software loans, as the sector faces the immediate challenge from AI competition. Because software credit spreads did not rise to reflect the higher cash flow uncertainty from AI disruption risk, and have in fact narrowed, the interest earned on software loans leaves little room to absorb losses if credit quality weakens. Thus, lenders are being paid less to carry a risk that has grown.

The exposure is also concentrated in two ways that could compound each other. First, software borrowers increasingly rely on many lenders: about 60% of software lending now goes to firms that borrow from seven or more BDCs, up from under 10% in 2015 (Graph 4.A). While from a single borrower's point of view this represents diversified funding, from the BDC's perspective it also means that a software-specific shock would surface across many balance sheets at once. Second, the lending itself is dominated by a few large BDCs, with the five largest accounting for around 37% of all software loans and the 10 largest accounting for more than half (Graph 4.B). A shock to software credit would therefore reach many portfolios, while the largest losses would fall on a small number of lenders. $^{9}$

Several features of BDCs in principle serve to reduce the risk of wider spillovers, but the extent to which they effectively do so is hard to gauge. Listed BDCs, which hold most of the exposure, are funded by equity investors cannot withdraw. They can also tap term funding and committed facilities to meet liquidity needs. BDC leverage is low, capped by statute and well below that of banks, and loans are mostly senior and secured, with covenants that let lenders act early. These features would work to support recoveries in default (Graph 4.C). However, it is hard to assess in aggregate the quality of the structural protections or the degree of interconnections with other financial intermediaries.

## High concentration in software exposure may be somewhat mitigated by low leverage and secure lending

Graph 4

![](images/967ae6da2a0879705765eff51a5d47c1ceffddfcdeacef4e6442e3fab234016e.jpg)  
$^{1}$ Number of distinct BDCs lending to the same borrower, expressed as a share of the total BDC loan volume to the software sector. $^{2}$ Share of BDC software principal held by the five and 10 largest lenders. $^{3}$ Based on listed BDCs. Principal-weighted average leverage, ratio of debt to equity.

Sources: PitchBook Data Inc | LCD; Bloomberg; authors' calculations.

9 Meanwhile, investment in AI itself is shifting from equity to private credit. See Aldasoro et al (2026) and Eren et al (2026).

A potential vulnerability concerns the roughly one quarter of software loans held by non-traded BDCs, often semi-open structures where liquidity risk is more salient. Their investors can only exit by redeeming shares against the issuing BDC, generating cash demands that can be met by using pre-funded cash positions, drawing on bank lines or selling assets. Quarterly redemption caps – typically 5% of assets under management – are meant to manage this liquidity risk, but under stress they might offer less protection than anticipated. $^{10}$ Cash buffers and loan repayments are usually insufficient to fund repeated 5% quarterly redemptions (Fang et al (2026)). Moreover, managers may feel tempted or pressured, perhaps for reputational reasons, to accommodate larger redemptions than contractually required. In early 2026, for instance, a large non-traded BDC breached its redemption cap for the first time, illustrating how funding structure-related fragility can surface despite fair weather contractual provisions. Such fragility could compound any repricing triggered by AI-related credit events, posing sustained liquidity stress.

Broader concerns emerge from what cannot be observed. The protections above rest on disclosure and underwriting. But recent events have called this into question, as several cases exposed weak due diligence practices and cast doubt on the quality of the covenants lenders are relying on. $^{11}$ More importantly, BDCs are only the visible part of private credit. BDCs' software exposure is roughly similar to that of other direct lenders, so their portfolios may offer a representative picture of how similar software exposures may be building in other segments of the private credit ecosystem, where disclosure is thinner and links to banks and other lenders are harder to trace (Berg and Lee (2026)). $^{12}$ Stress tests suggest that a severe downturn could force sizeable asset sales across the sector (Chernenko and Scharfstein (2025)). It is probably through these channels, rather than through BDCs themselves, that disruption to software credit could spread more widely.

## References

Aldasoro, I, S Doerr and D Rees (2026): "Financing the AI boom: from cash flows to debt", BIS Bulletin, no 120, January.

Berg, T and J H Lee (2026): "Measuring counterparty exposures to private credit", OFR Brief, 26-02.

Chernenko, S and D Scharfstein (2025): "Private credit and financial stability", working paper.

Davydiuk, T, T Marchuk and S Rosen (2024): "Direct lenders in the US middle market", Journal of Financial Economics, vol 162, 103946.

Doerr, S, E Eren, I Krohn and K Todorov (2026): "Private credit's software lending meets AI disruption ", BIS Quarterly Review, March.

Eren, E, I Krohn and K Todorov (2026): "Financing the AI infrastructure boom: on- and off-balance sheet borrowing", BIS Quarterly Review, March.

Fang, C, I Goldstein and Y Zeng (2026): "The fragility of semi-liquid private credit funds", NBER Working Papers, no 35385.

International Monetary Fund (IMF) (2026): "Global financial markets confront the war in the Middle East and amplification risks", Global Financial Stability Report, April.
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
9. 输出前自行核对：标题与导语不重复；每个小标题都是完整判断；没有元话语、推广语和未解问题栏目。只输出最终 Markdown，不输出核对过程。
