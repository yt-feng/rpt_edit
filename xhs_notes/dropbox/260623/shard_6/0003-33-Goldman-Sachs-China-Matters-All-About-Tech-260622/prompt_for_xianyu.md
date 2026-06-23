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

3. Confidence-building 

[中间内容因长度限制已省略]

ttempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

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
