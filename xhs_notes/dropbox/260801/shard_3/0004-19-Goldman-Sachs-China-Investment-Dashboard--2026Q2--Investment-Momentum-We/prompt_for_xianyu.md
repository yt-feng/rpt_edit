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
# China Investment Dashboard: 2026Q2: Investment Momentum Weakened amid Fiscal Tightening

Investment momentum: Headline FAI growth fell sharply in Q2 2026 after a brief Q1 rebound, with weakness broad-based across sectors. While we caution that occasional NBS “statistical corrections” of previously over-reported data may have amplified reported FAI volatility in recent quarters, alternative measures and fiscal data all point to investment momentum slowing in Q2. Divergence persisted between SOEs and non-SOEs, less-developed inland and more-developed coastal regions, and high-tech versus other industries. Our proprietary investment tracker suggests China’s real investment growth made a round trip in H1 2026, rising from 2.0% yoy in Q4 2025 to 3.2% yoy in Q1 2026 before falling back to 2.1% yoy in Q2 2026.

Lisheng Wang
+852-3966-4004 |
lisheng.wang@gs.com
GS (Asia) L.L.C.

Fiscal stance: Strong Q1 GDP growth and resilient exports likely increased comfort with the growth trajectory among top leaders and reduced the urgency for incremental easing, while local officials became more cautious amid political turnover, anti-corruption pressure, and accountability risks. Tax revenue continued to rise on higher PPI inflation and stronger collection efforts. By contrast, government bond issuance and proceeds spending slowed meaningfully in Q2, while some off-budget financing channels—such as land sales and policy bank support—contracted more sharply than usual. Together, these developments turned the fiscal impulse negative at an inopportune time, as the global energy-supply shock also weighed on growth. We estimate the negative fiscal impulse contributed to nearly half of the sequential real GDP slowdown from Q1 to Q2 (from 5.3% qoq annualized to 3.6% qoq annualized).

Property sector: Local housing easing slowed in Q2, and property activity continued to contract despite recent green shoots in some large cities. Most property activity indicators were down 60-80% from their 2020-21 peaks as of Q2, led by new home starts and land sales revenue, which do not bode well for home construction and completions in coming years given their lead-lag relationship. From a global perspective, the decline in new home starts has exceeded the US housing bust during the GFC, while the home price decline appears modestly larger than the average “large housing bust” based on global experience. Hong Kong property prices have rebounded by around 18% since mid-2025, while home prices in some Mainland China Tier-1 cities have begun to show early signs of stabilization. Housing inventory has moderated in recent months, helped by improved new home sales.

Investment outlook: We recently lowered our 2026 full-year AFD forecast by 0.5pp of GDP to 11.5% (vs. 11.0% in 2025) after incorporating H1 realized

numbers. Following the sharp Q2 fiscal tightening, however, our forecast still implies a modest H2 expansion. We expect central and local governments to accelerate bond issuance and proceeds spending in coming months, speed up implementation of the RMB800bn new policy-based financial instrument, and leave the door open for additional easing later this year if needed. The Politburo's call at its July meeting to “step up counter-cyclical adjustments, and make greater efforts to expand domestic demand and optimize supply” reinforces our view. The government spending focus continues to tilt toward high-tech manufacturing, strategic supply chains, the green transition, urban renewal, and “Six Networks” projects. We also recently cut our 2026 gross fixed capital formation (GFCF) growth forecast to 2.0% yoy from 2.5% yoy previously after incorporating Q2 realized data (vs. 1.2% in 2025), with risks still two-sided. Upside risks could come from additional extra-budget funding and new demand-side measures, while downside risks stem from continued central-level complacency and increasing local implementation constraints.

## 2026Q2: Investment Momentum Weakened amid Fiscal Tightening

## 1. Investment momentum – A slowdown in Q2, but milder than reported FAI data imply

Exhibit 1: Our investment tracker suggests China's real investment growth declined to $2.1\%$ yoy in Q2 from $3.2\%$ yoy in Q1

![](images/19472056c60352b259627035f5f1bb6f2bc5d3a2969d81c0a72ffa04b08fe99d.jpg)  
Source: Haver Analytics, GS Global Investment Research  
Exhibit 2: Newly signed contracts in the construction sector and headline FAI both declined sequentially in Q2

![](images/74a5362e4cb0fcfdfc128e7a3b8a575d90f1b6b32cc2626311e99db556595418.jpg)  
Source: NBS, Wind, Data compiled by GS Global Investment Research  
Exhibit 3: Steel and cement output both weakened in Q2, but their volatility was smaller than FAI-implied commodity demand in recent quarters  
Real FAI Implied vs. Actual Commodity Demand

![](images/16fcdf31db07712251cd3adaf3248ce5eb2abd2a68bb3ba9c88cdf6bf1b71301.jpg)

![](images/cb816f257f84162a3957366f76b886636048990612015dc3c6c553ba8da6e570.jpg)  
Real FAI-implied commodity demand is calculated by applying sector-specific multipliers—covering property, infrastructure, and manufacturing—to the value-added of each commodity. We use a construction-sector-specific index to adjust FAI to real terms.  
Source: CEIC, Mysteel, GS Global Investment Research

## Exhibit 4: FAI by both SOEs and non-SOEs showed a synchronized decline in Q2, with the gap still wide

![](images/3b205753abc45fce9a3d50e57c06d2dee96ab51a891063bf32d378cf8ccc08a0.jpg)  
Source: CEIC, GS Global Investment Research

Exhibit 5: FAI divergence between less developed inland provinces and coastal regions has been significant since 2023  
![](images/73a46715a1f1fd3b415d0f8d6a88ba90af74d0f194268562ba868703f65af863.jpg)  
The 12 provinces with high debt pressure include Guizhou, Tianjin, Yunnan, Inner Mongolia, Liaoning, Jilin, Chongqing, Guangxi, Heilongjiang, Gansu, Ningxia, and Qinghai, as listed in the “Document #47”.  
Source: Wind, GS Global Investment Research

Exhibit 6: The significant volatility in reported FAI growth in recent quarters stems from construction and installation, while the contribution from equipment purchases remained positive  
![](images/4cfa094c9d45a63b4c654a84cd326ca9d3a10f860778110790aa14fff4ea5b6c.jpg)  
Source: Wind, GS Global Investment Research

Exhibit 7: The quarterly averages of investment-related PMIs eased in Q2, despite still-wide divergence among different measures  
![](images/3a393e7b25f5be6cd812507884a0b1a2fc0284be55c10e8fbecf01637b08c1ca.jpg)  
NBS has suspended publication of the civil engineering-related construction PMI since early 2026. The CKGSB BCI survey covers all industries but is more weighted toward private SMEs, while the NBS construction PMI focuses only on the construction sector and is more weighted toward large enterprises.  
Source: NBS, CFLP, Wind, Data compiled by GS Global Investment Research

## 2. Fiscal stance – Fiscal impulse turned negative in Q2

Exhibit 9: Government revenue continued to increase in Q2, while government expenditure declined sequentially  
![](images/cdd265dbfef3bbba7849a5589d0c4a7016e4bbdb57e774c36a2ae4d69166abe5.jpg)  
Government revenue and expenditure cover both the general public budget and the government-managed fund budget.  
Source: Wind, GS Global Investment Research

Exhibit 10: Year-on-year fiscal expenditure growth slowed in Q2, mainly weighed on by falling spending in infrastructure-related areas  
![](images/29bda1ff723ce72095590882e82225c90f4b7810a17a4047e26735175065a9d3.jpg)  
We define infrastructure-related fiscal spending as on-budget fiscal spending on energy saving & environment protection, agriculture & water conservancy, transportation, and urban & rural community affairs.  
Source: Wind, GS Global Investment Research  
Exhibit 11: Effective fiscal deficit ratio narrowed in Q2 on a four-quarter moving-average basis, although it remained above the official fiscal deficit target

![](images/5b7fc9238af782bb2ba21eb723ea4918b842e80c0c27c870dceb0340ce5b3559.jpg)  
Source: Wind, GS Global Investment Research  
Exhibit 12: The outstanding fiscal deposit amount was RMB410bn (or 6%) above the year-ago level at end-Q2, slightly wider than the gap seen at end-Q1

![](images/6aa8d57be4d947f1d210f1d0c12f49de7ab5142226bb9038143e8245daa2e7c9.jpg)  
Source: CEIC, GS Global Investment Research

Exhibit 13: The pace of government bond issuance began to lag its 2025 run rate in Q2 this year  
![](images/0aaefb3fccd9ba9866702e1d3951542d70e50c75e2379c6407b4d80d1513e6ab.jpg)  
Full-year quotas refer to those approved in the budget report during March “Two Sessions”. Extra-budget bond issuance quota approved later was not included when estimating the run rates. July 2026 print refers to GS advance estimate based on Wind data.  
Source: Wind, GS Global Investment Research

Exhibit 14: China's fiscal “spend-through” ratio moderated in Q2 despite slower government bond issuance  
![](images/0d8a8a794895cccb9165cc6312c027f482bfb19d2a093187743aa7001bfdebb2.jpg)  
Shaded areas refer to periods when China's year-to-date real GDP growth was equal to or below the full-year growth target. Note that the Chinese government didn't set a national growth target for 2020.  
Source: MOF, Wind, CEIC, GS Global Investment Research  
Exhibit 15: Policy bank support contracted sharply in Q2, with PSL and bond net issuance both falling

![](images/09375d6bd37ec43872b43346b0c195a0bb74c293578b5f8dcd5a4a071a0d48f9.jpg)  
Source: Wind, CEIC, GS Global Investment Research

Exhibit 16: China's AFD narrowed notably to $10.2\%$ of GDP in Q2 from $11.2\%$ in Q1 on a 4QMA basis, while we expect it to expand in H2  
![](images/22078c89cb0e8c729e73dbe39a7d1cd8c2269dd5707ae35044251aaa77b6c4b0.jpg)  
Source: Wind, CEIC, GS Global Investment Research

Exhibit 17: We expect the fiscal impulse to shift from a growth drag in Q2 to a modest driver in H2  
![](images/285e28eb64e61d60283d142ce8023ded911e6d669648f4dd755411fdac90990d.jpg)  
Source: GS Global Investment Research

Exhibit 18: Municipal construction and industrial parks accounted for the largest share of local government bonds (LGB) proceeds spending in the first five months of 2026  
![](images/194b3377065a5d8efbb4e4c4942d6fa2e42b1a52fc7c3a569a6e3d421127961d.jpg)  
“Others” in 2024-26 may include local government repayment for corporate arrears and delayed salaries to civil servants.  
Source: MOF, GS Global Investment Research  
Exhibit 19: Our anti-corruption intensity proxy remained elevated in Q2 2026

![](images/d6e61bf3971affc495368eaf9d8f193ab289a6b335121c89eb423a21e4cc1378.jpg)  
Note: The proxy represents the number of government officials announced as under investigation each quarter. National level is deputy ministerial level and above; local level is any level but in practice mostly deputy bureau level and above.  
Source: CCDI, GS Global Investment Research

## 3. Property sector – Continued downturn nationwide despite some “green shoots” in large cities

Exhibit 20: The pace of property easing has slowed meaningfully since end-2024

![](images/180d52075f9e56e27423858286a8e1f6b0a8f96ee2e3a4846f411136b8cc7262.jpg)  
Source: GS Global Investment Research  
Exhibit 21: Some property activity indicators started to show signs of stabilization, though sustainability remains uncertain

![](images/0e9ecad8a1e495b4d903fcb1cf787805bb3b66c3f6169ebcf7da4fca8d8eaddf.jpg)  
Source: GS Global Investment Research, Haver Analytics  
Exhibit 22: The magnitude of declines in China's new home starts and home prices from their 2020-21 peaks has slightly exceeded the US housing bust during the GFC

![](images/a3cdc16576794f4369f1a40c5830e020a381b2b287384365b388533741e0a80b.jpg)  
Source: Centraline, NBS, Haver Analytics, GS Global Investment Research

![](images/dd7c257385aa6589eeba596b41976647eab7a422f7ffbf8fc8d98223453deaa3.jpg)  
We used a simple average of the Centraline 6-city and NBS 70-city secondary market prices as an input to measure China's real house prices.

Exhibit 23: China's home price decline appears slightly larger than a typical “large housing bust” based on global experience  
![](images/e5597c06a3e728abe81c0ba214a8e6e6a652f119e29f00dc8b8c7a992814fdda.jpg)  
The benchmark illustrates 21 large housing booms/busts across 15 economies around the world since the 1960s.  
Source: OECD, Haver Analytics, GS Global Investment Research  
Exhibit 24: Hong Kong property prices have rebounded by around 18% since mid-2025, while home prices in some Mainland China Tier-1 cities have begun to show early signs of stabilization

![](images/5ea2892d89ba340fb5a692270c002b28701a421e970b2b76302508a5e53eae11.jpg)  
Peak month refers to November 2021 for Hong Kong, May 2023 for Beijing, January 2022 for Shanghai, June 2022 for Guangzhou and August 2021 for Shenzhen, based on Centraline secondary home price data.  
Source: Wind, Data compiled by GS Global Investment Research, Centraline

Exhibit 25: Most property activity indicators have contacted by 60-80% from 2020-21 peaks as of end-Q2 2026, led by new home sales and land sales revenue

![](images/f59e0885cafa178c2a600ed008ce83755ffd9bb3ff01b550f0dbda7b51212744.jpg)  
All metrics other than Wind home sales volume and Centraline secondary home prices are for national total.

Source: NBS, Centraline, Wind, Data compiled by GS Global Investment Research

Exhibit 26: Land sales maintained double-digit year-on-year contraction in Q2 across various measures  
![](images/41a273769ee0bc802dbc1fb31b6dcafb66c4b3beea2f6e122280303049b8c53e.jpg)  
NBS suspended the release of developer land purchase value in early 2026.  
Source: Wind, CREIS, Data compiled by GS Global Investment Research  
Exhibit 27: Year-on-year contraction in bank lending to the property sector widened further in Q2

![](images/28f1d020fee65b8d8f5ecf70496e696c772be601a73e786906c0da35aa601175.jpg)  
Source: PBOC, Wind, Data compiled by GS Global Investment Research

Exhibit 28: Housing inventory moderated in recent months, thanks to an improvement in new home sales  
![](images/1a7f10ef3c8c2871213e6da456a2478e647740426854ba8d569106c495149d03.jpg)  
Housing inventory is estimated as housing inventory levels divided by the number of 12-month moving average new home sales.

Exhibit 29: New mortgage interest rates remained above housing rental yields  
![](images/2cd942d2374d78a0acb895b6af203185eae502537ce080b4efa2b8965d70c28e.jpg)  
Source: Wind, Data compiled by GS Global Investment Research  
Source: CREIS, Data compiled by GS Global Investment Research

## Lisheng Wang

The author would like to thank Samson Yau, an intern on the Asia Economics team, for his contribution to this report.

## The China Economics Team

Andrew Tilton
+852-2978-1802
andrew.tilton@gs.com
GS (Asia) L.L.C.

Xinquan Chen
+852-2978-2418
xinquan.chen@gs.com
GS (Asia) L.L.C.

Hui Shan
+852-2978-6634
hui.shan@gs.com
GS (Asia) L.L.C.

Yuting Yang
+852-2978-7283
yuting.y.yang@gs.com
GS (Asia) L.L.C.

Lisheng Wang
+852-3966-4004
lisheng.wang@gs.com
GS (Asia) L.L.C.

Chelsea Song
+852-2978-0106
chelsea.song@gs.com
GS (Asia) L.L.C.

## Disclosure Appendix

## Reg AC

I, Lisheng Wang, hereby certify that all of the views expressed in this report accurately reflect my personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Lisheng Wang GS (Asia) L.L.C..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disc

[中间内容因长度限制已省略]

ttempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints.

As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
