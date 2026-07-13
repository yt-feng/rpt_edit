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
ASIA ECONOMICS ANALYST

# Transmission of AI Super Surplus in Korea - Mostly Through FX and Fiscal Policy

Korea is among the major beneficiaries of the AI boom. Exports have surged on sharp memory-price gains and are on track to surpass US\$1 trillion in 2026. We use cross-country terms-of-trade (TOT) case studies to assess the macro implications of large AI-driven TOT gains in Korea.

Our cross-country study shows that positive TOT shocks are generally associated with currency appreciation across a broad set of exporters. However, the broad macro effects differ meaningfully between commodity and manufacturing exporters. Commodity exporters tend to experience stronger consumption and inflation but weaker capex, while manufacturing exporters tend to see more stable consumption, lower inflation, and stronger capex. The key distinction lies in how export-income gains are transmitted to consumption and investment across these export groups.

For Korea, whether large TOT gains translate into broader growth will likely depend on FX and fiscal policy. The KRW has recently weakened despite large TOT gains, contrary to the cross-country stylized facts. Given the strong FX passthrough to inflation in Korea, the drag from a weaker KRW on consumers' purchasing power and domestic firms' profit margins, and the diminished export boost from KRW depreciation due to structural changes, sustained KRW weakness could offset some positive TOT spillovers to domestic demand. Fiscal policy, including the implementation of AI mega projects, is also an important factor shaping the timing and scale of TOT spillovers. The newly announced AI projects, if implemented in line with previous initiatives for creating semiconductor clusters, could boost annual real GDP growth by 0.4pp over the medium term.

Taken together, KRW stability would need to be a near-term policy priority to secure price stability and extend the AI boom to domestic demand. Sustained KRW weakness at the outset of the AI boom cycle would add cost-push inflation, weigh on consumption, and widen the divergence between export and domestic industries. Over time, however, the policy challenge is likely to shift from stabilizing prices toward recycling Korea's external surplus productively. Beyond the near term, a mix of gradual monetary tightening and saving part of the fiscal windfall via a new sovereign wealth fund would help preserve macro stability and broaden AI-related gains across sectors. If the AI boom persists, surplus recycling will become increasingly important for both macro stability and potential

Goohoon Kwon, CFA
+852-2978-0048 |
goohoon.kwon@gs.com
GS (Asia) L.L.C.

Irene Choi
+82(2)3788-1722 | irene.choi@gs.com
GS (Asia) L.L.C., Seoul Branch

Andrew Tilton
+852-2978-1802 |
andrew.tilton@gs.com
GS (Asia) L.L.C.

growth.

Korea is among the major beneficiaries of the AI boom. Korea's exports have recently surged and are on track to surpass US\$1 trillion in 2026. This strong performance is mostly due to sharp gains in export prices, especially for memory chips, in contrast to Taiwan, where volume growth dominated export gains. Korea's memory exports rose nearly 150% from a year ago in the first five months of 2026, with nearly 80% of the rise coming from price jumps (Exhibit 1). Surging semiconductor exports—equivalent to a quarter of Korea's total exports in 2025—contributed three quarters of total year-on-year export gains through May. Overall, export price increases accounted for nearly half of total export gains over the same period, with the share exceeding half in high-frequency data.

Exhibit 1: Memory price gains have driven most of Korea's recent export increase  
![](images/bd982bccb3e1ee6e19f9cbc6344ae510857eb8cc10c0e782828da5fdd5c479ce.jpg)  
Source: Haver Analytics

These export-price gains matter beyond trade data because they are already feeding through to Korea's national-income measures. Korea's terms-of-trade (TOT; the ratio of export prices to import prices) improved $8.6\%$ in Q1 from a year ago and accelerated further about $20\%$ in Q2, mainly driving the roughly $13\%$ increase in the overall price level of GDP—the GDP deflator—in Q1 (Exhibit 2). Together with $3.8\%$ real GDP growth, the double-digit GDP deflator increase lifted nominal GDP $17.1\%$ yoy in Q1, the fastest pace in three decades.

Exhibit 2: Korea's overall terms of trade have improved sharply, pushing up its GDP deflator  
![](images/5ceb089bf1470d0e3c7ba85d16c27df6db760a536e8a59d6689c1fb4221e4621.jpg)  
Source: Haver Analytics, GS Global Investment Research

![](images/3f25363a2903b2c7c50ae82e796b751071f13e526834ae8a97c34cf8cc4e13c5.jpg)

## Macro Impact of Terms-of-trade Shocks—Country Cases

To gauge how such a large price-led export shock could transmit through the broader economy, we undertake case studies of the transmission of terms-of-trade (TOT) shocks to assess the macro implications of massive AI-driven TOT gains in Korea.

We examine how terms-of-trade shocks map into inflation, private consumption, and investment between 2000Q1 and 2026Q1. Our sample includes 32 major economies in our coverage, excluding the US and economies with exchange-rate pegs in the Middle East. Within the sample, we distinguish between exporters of extractive commodities—energy and ores—and other economies, since commodity exporters tend to experience terms-of-trade volatility on a scale comparable to Korea’s. The terms of trade improved by nearly 20% in Korea in Q2, comparable to those of many commodity exporters such as Chile, South Africa, Kazakhstan, Brazil, and Indonesia (Exhibit 3). Extractive commodity sectors also require large capex, similar to the memory sector. $^{1}$

Exhibit 3: Recent terms of trade gains in commodity exporters and in Korea and Taiwan, which export semiconductors  
![](images/70b306e56a5620ed8da3ce051cc0c86d2610496575926ef3e286a6d03d8ac55b.jpg)  
Source: Haver Analytics, GS Global Investment Research

Four findings stand out in our cross-country analysis. First, terms-of-trade gains broadly strengthen currencies across exporters, in line with the findings of most empirical studies. Quarterly data suggest that a one-standard deviation gain of 2.9% in the terms of trade appreciates the currencies of manufacturing exporters by 0.5% in the near term and by 1% over four quarters. We find similar patterns in commodity exporters, although their terms of trade are three times more volatile and the transmission is faster than in manufacturing exporters (Exhibit 4).

Exhibit 4: Currencies appreciate on positive terms-of-trade shocks equal to one standard deviation both in manufacturing and commodity exporters  
![](images/925f0d09748ab500001088139b7d37caad3fea5eafa4ca0e36c606b2e25c3a47.jpg)  
Source: Haver Analytics, GS Global Investment Research

Second, the broad macro effects differ meaningfully between commodity and manufacturing exporters. Real private consumption tends to move in line with commodity prices in commodity exporters, reflecting more jobs, higher wages, and/or procyclical fiscal policy (Exhibit 5). This is consistent with the commodity boom-bust literature and raises consumption volatility as a share of GDP. In contrast, real private consumption in manufacturing exporters is largely stable and invariant to changes in the terms of trade.

Exhibit 5: Improving terms of trade tend to boost real consumption in commodity exporters but not in manufacturing exporters  
![](images/24e103e6de90f1f47847147765b59ee4da37b57941e2585534370fd7eda6f178.jpg)  
Source: Haver Analytics, GS Global Investment Research

![](images/21fa5377c9bc31aaa7794d1b45730b36fa6f79cde104fdca027526f813edf90f.jpg)

Third, these differences in currency and consumption transmission also shape inflation outcomes. Terms-of-trade gains tend to lower inflation in manufacturing exporters (Exhibit 6). The disinflationary impact of terms-of-trade gains in manufacturing exporters comes through currency appreciation, as discussed above. However, for commodity exporters, terms of trade gains increase inflation, with the disinflationary effect of stronger currencies more than offset by procyclical consumption.

Exhibit 6: Terms-of-trade gains lower inflation in manufacturing exporters but raise inflation in commodity exporters  
![](images/a23d3e1ee1bc8b278c775bb1c00adda10ded12984d7383c4722781f4ee6b6112.jpg)  
Source: Haver Analytics, GS Global Investment Research

Finally, investment is another key channel through which terms-of-trade gains affect the real economy. Our panel regression, which controls for both time and country effects, suggests that a 10% rise in the terms of trade tends to increase real capex by 0.9% for manufacturing exporters (Exhibit 7). In contrast, the same terms-of-trade improvement tends to reduce capex by 0.6% for commodity exporters. This counterintuitive finding may reflect reverse causality, which is common in extractive industries with overcapacity and pricing power (such as OPEC), where lower capex tends to drive price increases and therefore terms-of-trade improvement. Currency depreciation also tends to reduce capex volumes for manufacturing exporters within the same quarter, likely reflecting higher costs of imported equipment.

Exhibit 7: Commodity exporters reduce capex on terms-of-trade gains, while capex of manufacturing exporters responds positively

<table><tr><td rowspan="2">Dependent variable</td><td colspan="2">Real capex growth (qoq, sa, 2000-26)</td></tr><tr><td>Commodity exporters</td><td>Manufacturing exporters</td></tr><tr><td>Explanatory variables</td><td colspan="2">Regression coefficients of a fixed effect model</td></tr><tr><td>Real capex growth in the previous quarter</td><td>-0.20</td><td>-0.20</td></tr><tr><td>Terms of trade change (+: Improvement)</td><td>-0.06</td><td>0.09</td></tr><tr><td>Exchange rate (+: Depreciation)</td><td>-0.03</td><td>-0.08</td></tr><tr><td>Memorandum item:</td><td></td><td></td></tr><tr><td>R-squared</td><td>26%</td><td>27%</td></tr><tr><td>Total observations</td><td>710</td><td>2432</td></tr><tr><td>Number of countries</td><td>8</td><td>24</td></tr><tr><td colspan="3">Note: Bold coefficients are significant at a 95% confidence level.</td></tr></table>

Source: Haver Analytics, GS Global Investment Research

## Application to Korea—Similarities and Differences

Applying these cross-country patterns to Korea highlights the importance of the KRW in translating the AI boom into broader growth. The KRW has recently weakened sharply despite large terms-of-trade gains, contrary to the stylized facts (Exhibit 8). Key drivers include overseas portfolio investment by retail investors and social security funds, foreign hedging demand, and recent rebalancing by foreign investors amid the KOSPI rally.

Sustained KRW weakness could offset positive terms-of-trade spillovers to growth. In Korea, where FX passthrough to inflation is strong—about 30bp for a 5% depreciation—sustained KRW depreciation would weigh on consumers' purchasing power through higher import prices and the associated need for monetary tightening, which we expect to start at the upcoming monetary policy meeting on July 16. Profit margins of domestic companies, including local small and medium-sized suppliers to large exporters, would also decline. Moreover, ongoing structural changes in Korea's export industry reduce the positive effects of a weaker KRW on exports. We estimate that overseas sales by Korean subsidiaries abroad have increased steadily over the last decade, reaching about 90% of their direct exports from Korea onshore. In addition, more Korean companies, in particular semiconductor firms, have managed to increase their profit margins through improved productivity, reducing the significance of exchange rates on their export earnings.

## Exhibit 8: The KRW has recently become countercyclical, weakening amid surging exports

![](images/38207a598d7a15cdc50d2008e64b61121e7c573fe5bda5dd05f0423aab150889.jpg)  
Source: Haver Analytics

While FX policy determines whether terms-of-trade gains support domestic purchasing power, fiscal policy will help determine how effectively they translate into investment. The global memory industry is currently capacity constrained, rather than facing overcapacity as in some extractive industries. Tight memory capacity bottlenecks could require substantial capex in public infrastructure as well as expanded corporate production capacity. In this context, the government has recently announced the “3 Mega Projects,” a large public-private investment plan for Korea’s AI development initiatives. If implemented in line with previous memory-cluster initiatives, the newly announced AI projects could increase real capex growth in Korea by 2-3pp per year and lift annual GDP growth by 0.4pp over the medium term. Under this scenario, nominal private investment in the AI projects, together with public investment, would rise by about 3-4pp of GDP over the medium term (Exhibit 9).

Exhibit 9: Mega AI projects suggest meaningful recovery in capex by the tech sector and the government

% of GDP

![](images/5d5a748c05e85b7dd6cde1eabec02dbd5726112e49be8cb0bf4b8276432b1d04.jpg)  
Source: Haver Analytics, Quantiwise, GS Global Investment Research

## Policy and Market Implications

These FX and fiscal transmission channels point to two policy priorities. KRW stability would need to be a near-term policy priority to secure price stability and extend the AI boom to domestic demand. Sustained KRW weakness at the outset of the AI boom cycle would add to cost-push inflation, weigh on consumption, and widen the divergence between export and domestic industries.

Over time, however, the policy challenge is likely to shift from stabilizing prices toward recycling the surplus productively. Beyond the near term, a mix of gradual monetary tightening and saving part of the fiscal windfall—including through the creation of a sovereign wealth fund called the “Future Response Fund”—would help preserve macro stability and broaden AI-related gains across sectors. If the AI boom persists, recycling Korea’s external surplus will become increasingly important for both macro stability and potential growth.

## Disclosure Appendix

## Reg AC

We, Goohoon Kwon, CFA, Irene Choi and Andrew Tilton, hereby certify that all of the views expressed in this report accurately reflect our personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Goohoon Kwon, CFA GS (Asia) L.L.C., Irene Choi GS (Asia) L.L.C., Seoul Branch, Andrew Tilton GS (Asia) L.L.C..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst

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
