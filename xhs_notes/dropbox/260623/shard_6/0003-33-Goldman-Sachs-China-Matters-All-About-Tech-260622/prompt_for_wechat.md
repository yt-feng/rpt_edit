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
- 已识别机构名：`GS`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
CHINA MATTERS

# All About Tech

China's May activity data continued to disappoint outside of exports and industrial production. With export growth contributing roughly 3pp to year-over-year real GDP growth, domestic demand appears to be growing at a sluggish pace of only $1 - 2\%$ yoy in recent months based on official data.

Hui Shan
+852-2978-6634 | hui.shan@gs.com
GS (Asia) L.L.C.

We nudge down our Q2 real GDP forecast from 4.0% qoq annualized to 3.5% on the back of weak April and May data, implying year-over-year growth of 4.5% (vs. 4.7% previously). Assuming lower oil prices, faster fiscal spending, and normalized weather conditions, we project Q3 real GDP growth to rebound to 5.0% qoq annualized (vs. 4.5% previously). Our full-year real GDP growth forecast remains unchanged at 4.7%.

The Chinese government focuses on its long-term objective of transforming the economy into a tech-driven one. The divergence between high-tech/AI and property/consumption continues to widen in both industrial production and capital market data. Top leaders' domestic travel, recent policy communications, and our on-the-ground channel checks all suggest these trends will persist.

While China's long-term planning has proved valuable in weathering external shocks such as the US-China trade war and energy price spikes, we believe cyclical policies are crucial to ensuring a smoother path toward China's strategic goals. We discuss three channels connecting near-term policies with long-term objectives.

First, AI-related job displacement could amplify macroeconomic headwinds and delay, if not derail, the recovery in the property market and household consumption. Second, with export growth likely to remain strong over the next few years, targeting only headline GDP growth could cap domestic demand growth. Third, frequent quarter-to-quarter shifts in the policy stance to steer the economy toward the full-year target are not conducive to confidence-building. If not managed well, persistent cyclical weakness could impede China's goal of restructuring the economy into a virtuous cycle between tech-driven productivity gains and strong domestic demand growth.

## All About Tech

## An even more divergent economy

China's May activity data disappointed again following weak April readings. Both retail sales and fixed asset investment (FAI) contracted: May retail sales declined $0.6\%$ yoy, and January-May FAI dropped $4.1\%$ yoy. In the history of official releases, this is only the second time on record that both retail sales and FAI have printed negative numbers—the first was in 2020 during Covid lockdowns.

Looking across major indicators, exports remain the best-performing sector, rising nearly 20% yoy in nominal USD terms. By contrast, domestic indicators such as property activity, auto sales, and infrastructure investment (on a single-month basis) showed double-digit year-over-year declines (Exhibit 1). Auto sales data best illustrate the significant divergence between exports and domestic demand: domestic sales dropped 22% yoy in May, while auto exports jumped 75% yoy (Exhibit 2).

The April and May production data track roughly 4% yoy real GDP growth, about 1pp lower than the Q1 official real GDP growth of 5%. We calculate that the ongoing robust export growth likely contributes around 3pp to year-over-year real GDP growth, implying that domestic demand is growing at a very sluggish pace of only 1-2% yoy based on official statistics. This is also consistent with our import-implied domestic demand growth estimates.

Exhibit 1: Exports remain the best performing part of the economy  
![](images/b53afe62c13f51be73806d672ee54e50875de389dd0776239ea562e61943d1ac.jpg)  
Source: CEIC, GS Global Investment Research

Exhibit 2: Domestic sales of autos dropped 22% yoy in May while exports jumped 75% yoy  
![](images/becc69f45bfb703d3bf47c243da11266b551e98f6ce7d7bde16a0d7dd0e5b51e.jpg)  
Source: Haver Analytics, GS Global Investment research

## A Slower Q2 and a Faster Q3

Given the April and May realized data, we nudge down our Q2 real GDP growth forecast from 4.0% to 3.5% in qoq annualized terms, or from 4.7% to 4.5% in year-over-year terms. The sequential slowdown from Q1 to April-May was likely driven by three factors.

1. The negative impact of higher energy prices: Notable declines in the production of refined oil and chemicals, as well as the sharp drop in domestic retail fuel sales, are clear signs that the Iran war and higher oil prices weighed on Chinese economic activity. With the interim deal to reopen the Strait of Hormuz and our commodity team's lower oil price projections reducing our 2026Q4 Brent forecast from \$90/bbl to \$80/bbl, we expect the drag from elevated energy prices to gradually dissipate in the coming quarters.

2. Slowdown in fiscal spending: After January-February activity data beat expectations, the pace of fiscal spending slowed significantly in March and April. Combining the general public budget and government managed fund budget, total government expenditure growth dropped from +6.1% yoy in January-February to -7.3% yoy in April. $^{1}$ Other quasi-fiscal channels also showed tightening in recent months, with the PBOC's Pledged Supplementary Lending (PSL) balance contracting and policy bank bond net issuance falling. Now that April and May activity data have disappointed, we expect the pace of government bond issuance and fiscal spending to accelerate in the coming months (Exhibit 3).

3. Adverse weather conditions and residual seasonality: The NBS noted that heatwaves and heavy rainfall impeded both consumption and investment in May. Adverse weather conditions continued into June, likely weighing on outdoor activities. That said, June industrial production may benefit from positive quarter-end residual seasonality, and Q3 sequential growth should rebound if weather conditions normalize. $^{2}$

Taken together, we expect Q3 sequential growth to pick up to 5.0% qoq annualized (vs. 4.5% previously) from 3.5% in Q2 (Exhibit 4). Our full-year real GDP forecast remains unchanged at 4.7% for 2026.

Exhibit 3: Local government special bond issuance slowed after Q1  
![](images/9d71bc54b5e4a73de0e1176d20f76b37bc89986e427e0d1c7d4f23f47ae72d77.jpg)  
Source: Wind, GS Global Investment Research

Exhibit 4: We nudge down Q2 sequential real GDP growth forecast while raising Q3 forecast

<table><tr><td colspan="6">China real GDP growth forecast</td></tr><tr><td></td><td></td><td>New YoY%</td><td>Previous YoY%</td><td>New QoQ%, SAAR</td><td>Previous QoQ%, SAAR</td></tr><tr><td>2023</td><td></td><td>5.4</td><td>5.4</td><td></td><td></td></tr><tr><td>2024</td><td></td><td>5.0</td><td>5.0</td><td></td><td></td></tr><tr><td>2025</td><td></td><td>5.0</td><td>5.0</td><td></td><td></td></tr><tr><td>2026</td><td></td><td>4.7</td><td>4.7</td><td></td><td></td></tr><tr><td>2027</td><td></td><td>4.7</td><td>4.7</td><td></td><td></td></tr><tr><td rowspan="4">2025</td><td>Q1</td><td>5.4</td><td>5.4</td><td>4.5</td><td>4.5</td></tr><tr><td>Q2</td><td>5.2</td><td>5.2</td><td>4.5</td><td>4.5</td></tr><tr><td>Q3</td><td>4.8</td><td>4.8</td><td>4.5</td><td>4.5</td></tr><tr><td>Q4</td><td>4.5</td><td>4.5</td><td>4.9</td><td>4.9</td></tr><tr><td rowspan="4">2026</td><td>Q1</td><td>5.0</td><td>5.0</td><td>5.3</td><td>5.3</td></tr><tr><td>Q2</td><td>4.5</td><td>4.7</td><td>3.5</td><td>4.0</td></tr><tr><td>Q3</td><td>4.7</td><td>4.7</td><td>5.0</td><td>4.5</td></tr><tr><td>Q4</td><td>4.6</td><td>4.6</td><td>4.5</td><td>4.5</td></tr></table>

Source: NBS, GS Global Investment Research

## Tech drives both the economy and the market

The Chinese government is restructuring the economy by shrinking the property sector and bolstering the technology sector. This transformation is clearly reflected in physical output data. Compared with 2019 levels, production of industrial robots has tripled, and semiconductor production has more than doubled, in sharp contrast to the decline in construction materials such as glass and cement (Exhibit 5). The divergence is also visible in equity market performance. The Shanghai Composite Index has been largely flat year-to-date, but beneath the stable aggregate index, the information technology sector index has rallied by over 50%, while the consumer discretionary sector index has slid by more than 25% (Exhibit 6).

Although policymakers have shown some concerns over the latest weakness in consumption growth, policy signals still point to unwavering support for tech and AI as China's structural transformation continues. During its press conference after the May data release, for example, the NBS touted China's technological advances in optical quantum computing and turbofan engine testing. According to NBS officials, high-tech manufacturing value-added grew 15.1% yoy, far outpacing overall IP growth of 4.5% yoy in May. In contrast to the 4.1% yoy decline in overall FAI in January-May, investment in the information transmission industry (which includes AI computing), R&D, and high-tech sectors increased 30.4% yoy, 9.3% yoy, and 4.5% yoy, respectively.

Exhibit 5: Physical output of industrial robots and semiconductors climbed while that of glass and cement fell  
![](images/c385724e2c52b26795ec1c640c36a05b19c4c6bd3c670fad3f33f2c224cb3028.jpg)  
Source: CEIC, GS Global Investment Research

Exhibit 6: In the onshore equity market, tech index rallied while consumer index slid  
![](images/3fa1ccc7dd36768a18450ce6cc2698cef398c83a72e1c2f177c219cc014c8e04.jpg)  
Source: Bloomberg, GS Global Investment Research

## Racing for AI in a different way

On the surface, China's AI capex appears to fall far short of that in the US. For example, while US hyperscalers Amazon, Meta, Google, Microsoft, and Oracle are estimated to increase capex to over \$750bn in 2026, Chinese hyperscalers Alibaba, Tencent, ByteDance, and Baidu are expected to reach only \$100bn in total capex this year (Exhibit 7). However, this does not mean China's computing power is only a fraction of that in the US. As of mid-2025, installed data center capacity in China was already 60% of that in the US (Exhibit 8).

Two factors contributed to China's low hyperscaler capex relative to its data center capacity. First, the cost of building data centers is much lower in China than in the US. Second, a significant share of China's AI-related capex is conducted by the government. In the $15^{\text{th}}$ Five-Year Plan (2026-30), for instance, policymakers plan to invest RMB2tn in computing power networks, including data centers. China's push for AI development and adoption is real, even though the way it is financed and applied differs significantly from the US.

Exhibit 7: Hyperscaler capex is much lower in China than in the US  
![](images/2721937f778c0b9de6ea924b6cf5c80365c30cdc5cfa5deb79f091b9188c2674.jpg)  
Source: FactSet, GS Global Investment Research

Exhibit 8: China's installed data center capacity was $60\%$ of that in the US as of June 2025  
![](images/60dd144a0543bcafb72b792747c65afb91b7c7d60970b0a28d671509f9d493d4.jpg)  
Source: IEA, GS Global Investment Research

As China continues to push aggressively on tech and AI advancement, investors are increasingly asking what this means for China's employment and consumption outlook. Regarding the pace at which AI adoption may replace labor, there are arguments on both sides. The case for slower AI adoption and less job displacement in China than in the US rests on relatively cheap labor and a government with more levers to discourage AI-related job losses in order to ensure social stability.

On the other hand, historical experience suggests that tech adoption to reduce labor costs accelerates during economic downturns, when profits erode and pressure on employers mounts. For example, our Global Economics team's research shows that, historically, nearly all job losses from automation of routine occupations in the US have been concentrated in economic downturns (Exhibit 9). With fierce competition persisting and many companies facing low margins, Chinese employers may be more willing than their US counterparts to replace labor with AI to stay competitive.

Herein lies the risk that too rapid a spread of tech and AI applications puts additional pressure on China's already weak labor market. After five years of decline, house prices are getting close to finding a bottom in the next year or two, based on the experience of historical international housing busts. However, if AI adoption were to lead to significant job losses, stagnant or even falling income would imply declining rents and further downward adjustment in house prices. In other words, with the domestic economy still weak and confidence fragile, another negative shock such as AI-related job displacement could amplify existing macro headwinds and delay the recovery in the property market and household consumption.

In June, the State Council released a document entitled “Implementation of the 15th Five-Year Plan for the Employment-First Strategy”, which tries to strike a balance between accelerating China’s AI development and ensuring labor market stability during 2026-30. However, it is unclear what concrete and effective measures could be introduced to create more jobs when the youth unemployment rate is already high and AI adoption threatens an increasing number of entry-level white-collar positions. Anecdotally, online job postings data suggest that growth in entry-level positions is underperforming the overall job market.

Exhibit 9: US experience shows that labor replacement tends to accelerate during economic downturns  
![](images/d5a03cbff09164f0355d2ff30f7b02dd61dd6648211bd3a5ed34ea46f8155993.jpg)  
Routine occupations include sales (e.g., clerks/telemarketers), office/administrative support (e.g., secretaries/typists), production (e.g., factory machine operators), construction/extraction (e.g., miners), and installation/maintenance/repair (e.g., mechanics).  
Source: Jaimovich Siu 2018, GS Global Investment Research

Exhibit 10: Rising unemployment often precedes falling rents in China  
![](images/fb9f87d6429543399ecf2ea62e47598c5da9eb5c49b826ae464e5c4ea825cd36.jpg)  
Source: Haver Analytics, GS Global Investment Research

## Policymakers focusing on the long-term

Recent policy news has focused on long-term strategies. The State Council Decree 834, published in April, addressed supply chain security. The State Council Decree 837, made public at the beginning of June, relates to monitoring and regulating tech transfers and cross-border investment amid US-China competition and Chinese companies' global expansion. The Lujiazui Forum in mid-June announced steps to build a price-based monetary policy framework and accelerate RMB internationalization.

In contrast, near-term cyclical policies have attracted less attention. But the near term is the path to the long term. We think three aspects of cyclical economic management are important in this regard.

1. As discussed earlier, if rapid AI adoption were to lead to significant job replacement, it would disrupt China's pursuit of a self-sustaining, robust, tech-driven growth model. Therefore, concrete and effective policies to boost employment and income are crucial to creating a domestic environment conducive to continued tech development.

2. With Chinese exports poised for strong growth in the next few years, the current economic planning system, which targets only headline real GDP growth, effectively caps domestic demand growth. This runs contrary to the government's long-term goal of expanding domestic demand. Instead, domestically oriented targets such as employment and consumption growth would be more suitable for China's stated long-term strategic objective of expanding domestic demand.

3. Confidence-building takes time and persistence. Over the past few years, we have observed a repeated pattern in which a solid quarter of real GDP growth is followed by a slowdown in fiscal spending, and policy easing accelerates only after weak data put the full-year target at risk. Quarter-to-quarter shifts in the policy stance do not help boost sentiment and bolster confidence, which are important to households' propensity to consume and private businesses' propensity to invest, even if such shifts help the government land official GDP statistics exactly on the growth target laid out at the beginning of the year.

The experience of the past two years, including the US-China trade war of 2025 and the energy supply shock of 2026, has demonstrated the advantages of China's long-term planning and strategic thinking. However, if long-term planning becomes policymakers' sole focus, it could hinder progress toward achieving strategic goals. Fostering consistent and strong economic growth through cyclical tools should be an indispensable part of macro management. Robust growth, a strong labor market, and optimistic sentiment provide the cushion needed for the government to push through difficult structural changes and enable a virtuous cycle between tech-driven productivity gains and strong domestic demand growth.

## Hui Shan

The China Economics Team

Andrew Tilton
+852-2978-1802
andrew.tilton@gs.com
GS (Asia) L.L.C.

Hui Shan
+852-2978-6634
hui.shan@gs.com
GS (Asia) L.L.C.

Lisheng Wang
+852-3966-4004
lisheng.wang@gs.com
GS (Asia) L.L.C.

Xinquan Chen
+852-2978-2418
xinquan.chen@gs.com
GS (Asia) L.L.C.

Yuting Yang
+852-2978-7283
yuting.y.yang@gs.com
GS (Asia) L.L.C.

Chelsea Song
+852-2978-0106
chelsea.song@gs.com
GS (Asia) L.L.C.

## Disclosure Appendix

## Reg AC

I, Hui Shan, hereby certify that all of the views expressed in this report accurately reflect my personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Hui Shan GS (Asia) L.L.C..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensa

[中间内容因长度限制已省略]

 have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g.,

marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
