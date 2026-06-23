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
ASIA ECONOMICS ANALYST

# Food inflation in ASEAN - When oil shock meets El Niño

## Key Messages:

Regional food prices face upside risk in coming months from three shocks: oil, fertilizer and climate conditions. First, the oil shock from the Middle East conflict has shown up in fuel-sensitive CPI items, and higher fertilizer prices will raise farm input costs. A potential strong El Niño event in late 2026 could create another food supply shock just as oil and fertilizer pressures are passing through the food chain.

Chris Poh  
+65-6889-3454 | chris.poh@gs.com  
GS (Singapore) Pte

Andrew Tilton  
+852-2978-1802 | andrew.tilton@gs.com GS (Asia) L.L.C.

ASEAN is exposed through trade, CPI weights and commodity linkages. Food inflation is highly synchronized across the region and food carries a large weight in CPI baskets. Singapore and the Philippines are net food importers, while Malaysia's and Indonesia's food surpluses are concentrated in palm oil. Even Thailand, the region's net food exporter, relies heavily on imported fertilizer.

We estimate a $10\%$ increase in local oil prices raises ASEAN food CPI by around 0.3pp after 12 months, all else equal. Fertilizer effects are smaller at 0.2pp, while El Niño effects are less precisely estimated.

The forecast path points to additional pipeline pressures. Feeding our commodities team's forecast and NOAA's El Niño probability-weighted projections through our model implies additional ASEAN food inflation of around 2.1pp, on average, after 12 months. Indonesia, Philippines and Thailand face the clearest upside risks, while the impact on Singapore and Malaysia looks more contained.

■ Policy buffers can blunt El Niño pass-through. Past episodes show that food inventory releases, import liberalization, subsidies and price controls have often cushioned domestic food prices.

The conflict in the Middle East has driven crude oil prices sharply higher, while the initial blockade of key shipping lanes has squeezed fertilizer supply. The first-round inflation impact is straightforward: higher oil prices show up first in fuel-sensitive components such as transport and airfare. However, the second-round inflation impact, which comes with a lag, is likely to start feeding into the food-price pipeline.

## A potential food inflation shock ahead

An additional complication is weather. The National Oceanic and Atmospheric Administration (NOAA) has assessed that El Niño conditions are present, with forecast models pointing to a meaningful risk of a very strong event around November 2026 to January 2027. If realized, this would add another supply shock just as higher oil and fertilizer costs are still passing through the food chain.

ASEAN is not uniformly exposed, but the region is vulnerable through several channels. The region includes near-total food importers as well as major rice and palm oil producers, while food carries a large weight in CPI baskets. In this report, we quantify the potential impact on ASEAN food prices from three shocks: oil, fertilizer and El Niño.

## ASEAN looks particularly vulnerable

ASEAN food inflation is highly synchronized. A simple principal component analysis shows that the first common factor explains around 70% of the variation in food inflation across the region, underscoring how regional food prices tend to move together during major shocks.

Singapore and the Philippines are net food importers, leaving them directly exposed to global food price shocks. Malaysia and Indonesia appear more insulated in aggregate, but their food surpluses are largely a palm-oil story; excluding that component, both become net food importers (Exhibit 1). Thailand is the only broad-based net food exporter in the region. Even then, Thailand is still exposed to global food price shocks through increases in food input prices, such as fertilizer, more than $90\%$ of which Thailand imports. The region's main food commodity imports are cereals, meat and dairy products.

The unprecedented oil shock is also forcing governments to reconsider the food-versus-fuel trade-off. To reduce reliance on imported fuel, Indonesia, Malaysia and Thailand have accelerated higher biodiesel blends, pulling more palm oil into energy use (Exhibit 2). That adds a new demand shock to a market already constrained by yields, while El Niño-related rainfall shortfalls could further pressure palm oil supply. Higher oil prices therefore risk tightening edible-oil markets as well as transport costs, reinforcing why ASEAN looks particularly vulnerable to a broader food inflation shock.

% of GDP

Exhibit 1: ASEAN economies are largely net food importers Excluding palm oil, Malaysia and Indonesia are net food importers

![](images/c363c39f8f2843dbcd80a1bd335f8a79908e81194608164e878a119098df7537.jpg)  
Source: ITC Trade Map, GS Global Investment Research

Exhibit 2: The latest biofuel mandates in ASEAN

<table><tr><td>Country</td><td>Policy</td></tr><tr><td>Indonesia</td><td>From 1 July, all diesel fuel must be 50% palm oil, up from 40%; gasoline in Jakarta and other areas of Java island must be 5% ethanol</td></tr><tr><td>Malaysia</td><td>From 1 June, diesel suppliers should provide 15% palm oil blend, up from 10%</td></tr><tr><td>Philippines</td><td>Government council pushing for raising required blend of coconut oil in diesel fuel to 5% from 3%</td></tr><tr><td>Thailand</td><td>From 14 March, regular diesel fuel must be 7% palm oil, up from 5%; supplies of 20% blend increased for large vehicles; exports of crude palm oil restricted from 7 April</td></tr></table>

Source: Asia Nikkei, GS Global Investment Research

## How do supply shocks affect food inflation in ASEAN?

We use the local projections (LPs) method of Jordà (2005) $^{1}$ to quantify the impact of oil, fertilizer and El Niño shocks on ASEAN food inflation. LPs are well suited to this exercise because they estimate the response of food CPI directly at each future horizon, without requiring us to specify the full underlying multivariate system.

Following Borrallo et al. (2024) $^{2}$ , our outcome variable is each country's food CPI, while the key predictors are oil prices, fertilizer prices, El Niño conditions and industrial production as a proxy for economic activity. We adapt their framework in three ways for ASEAN. First, we use the Relative Oceanic Nino Index (RONI) $^{3}$ rather than the standard

Oceanic Nino Index (ONI) to better capture ENSO (El Niño–Southern Oscillation) conditions relative to recent warming trends. Second, we measure the El Niño shock as the month-on-month change in RONI, while controlling for the lagged RONI level to capture the prevailing El Niño state. Third, we estimate both a pooled ASEAN panel LP and country-level LPs to distinguish the average regional response from country-specific heterogeneity. Given data constraints, the estimation sample starts from 2002.

On average, oil shocks generate the clearest pass-through to food prices: a 10% increase in local-currency oil prices raises food inflation by around 0.3% after 12 months, with statistically significant effects across the report horizon (Exhibit 3). Fertilizer effects are smaller but build over time, reaching 0.2% after 12 months (Exhibit 4). The average El Niño effect is less precisely estimated (Exhibit 5).

Country-level LP estimates point to material heterogeneity beyond the regional average. Oil pass-through is the most consistent result: it is positive in all countries and statistically significant in most. Fertilizer effects are generally smaller and less uniform, while El Niño responses vary more sharply across countries.

At the global level, our Commodities team notes that strong El Niño events have not typically been inflationary for global food prices. This is consistent with our more mixed El Niño estimates. We think domestic policy responses such as the release of buffer stocks, import liberalization, administered prices, and other policies blur the El Niño shock estimates.

Exhibit 3: Pooled ASEAN cumulative food CPI response (%) to a 10% increase in oil prices  
![](images/6c017dc4e16753f2e76c2cf5f14b356c8b0537c7d53125ab8b353106a233df6d.jpg)  
Source: Haver Analytics, GS Global Investment Research

Exhibit 4: Pooled ASEAN cumulative food CPI response (%) to a 10% increase in fertiliser prices  
![](images/97441c63f97476ab3a9d79aeee71b5eac44e1cf2a05626c90c678df80ebf6e12.jpg)  
Source: Haver Analytics, GS Global Investment Research

Exhibit 5: Pooled ASEAN cumulative food CPI response (%) to a 1°C increase in El Niño (RONI)  
![](images/cc36ebd39127042d0fe65bd130936e304407c8e4296a0ff237ba1358f197bcd1.jpg)  
Source: Haver Analytics, GS Global Investment Research

## Pipeline pressure still building

Using the estimated responses over time after a shock, we translate the recent commodity shock and projected El Niño path into an additional impulse to food prices. The shock is already large: by end-May, Brent and urea prices were still around 46% and 63% above their February levels, even after easing from April's peak. At the same time, NOAA projects that RONI will rise from zero in May 2026 to around 1.7 degrees Celsius by late 2026, adding a potential weather shock on top of higher input costs.

We estimate that the oil, fertilizer and El Niño shocks could add, on average, 1.0pp to ASEAN's food inflation after six months and 2.1pp after 12 months, before moderating to 2.0pp in 18 months, relative to a no-shock baseline path. These estimates should be read as additional pressure on top of the usual food inflation trend, not as forecasts of total food inflation.

The average also masks wide dispersion: Indonesia, Philippines and Thailand face the clearest upside risks, while potential impacts on Singapore and Malaysia look more contained. In the following table, we show the cumulative percentage-point impact on headline CPI, calculated by multiplying the estimated food CPI impulse by each country's food weight in the CPI basket.

Exhibit 6: Percentage point contribution to headline CPI from oil, fertilizer and El Niño shocks

<table><tr><td>Country</td><td>Food weight in CPI</td><td>6m</td><td>12m</td><td>18m</td><td>Peak</td><td>Peak Month</td></tr><tr><td>Indonesia</td><td>22.5%</td><td>0.4</td><td>0.8</td><td>1.1</td><td>1.2</td><td>16</td></tr><tr><td>Philippines</td><td>34.8%</td><td>-0.1</td><td>0.3</td><td>1.1</td><td>1.1</td><td>18</td></tr><tr><td>Thailand</td><td>22.1%</td><td>0.3</td><td>0.7</td><td>0.2</td><td>0.7</td><td>13</td></tr><tr><td>Malaysia</td><td>15.6%</td><td>0.1</td><td>0.2</td><td>0.0</td><td>0.2</td><td>7</td></tr><tr><td>Singapore</td><td>6.5%</td><td>0.1</td><td>0.1</td><td>0.1</td><td>0.1</td><td>12</td></tr></table>

Source: Haver Analytics, GS Global Investment Research

Exhibit 7: Peak headline CPI response from oil, fertilizer and El Niño shocks  
![](images/49b9862f79c11bd7811fee4ea14740fb010c94ded2dafaf0b220dceca5686f68.jpg)  
Source: Haver Analytics, GS Global Investment Research

## Domestic policy responses

Around El Niño episodes, ASEAN governments have often introduced discretionary measures to cushion food prices. Some were not explicitly El Niño-specific but still overlapped with the shock and materially affected inflation through stock releases, import liberalization, subsidies or price controls. These interventions likely weakened the observed pass-through from El Niño to food prices, making our estimates less precise. Below, we highlight selected domestic policy responses, though the list is not exhaustive.

Release of buffer stock: In Thailand, the government's 2011-14 rice-pledging scheme, though fiscally costly, left it holding a record stockpile of roughly 17.8 million tons of rice. While the 2015-16 El Niño drought lowered rice production, the government's steady release of this stockpile actively held prices down, and the pass-through to consumer price inflation was modest. During the episode, Thailand also acted as a regional supply anchor, exporting its surplus to help keep neighbors such as the Philippines and Singapore supplied.

In Indonesia, the State Logistics Agency (Bulog) procures and holds national rice reserves, then releases stock when market prices come under pressure. This buffer proved useful after Indonesia's heavy rice imports in 2018, which reached 2.25 million tons worth over US\$1 billion. When drought cut rice output by 7% in 2019, Bulog's large carryover stocks helped cushion the shock and keep domestic rice prices broadly stable.

Import liberalization: In the Philippines, the 2019 Rice Tariffication Law was not an El Niño-specific measure, but it overlapped with the drought episode and helped cushion food price pressure by liberalizing rice imports. The law replaced quantitative import restrictions with tariffs, allowing much freer private-sector rice imports and expanded domestic supply. As imports rose, rice prices fell: the Philippines Department of Finance said rice tariffication helped cut rice prices in 2019, while the World Bank later described the liberalized sector as supporting stable food prices and cited 17 consecutive months of negative rice inflation after May 2019.

Subsidies/price ceilings: During the 2023/2024 El Niño episode, which coincided with India's rice export ban, the Malaysian government maintained the price cap on local

white rice despite rising input costs. This eventually triggered shortages that pushed demand toward imported rice and drove its price higher, prompting the government to extend subsidies to imported rice as well. Price controls stretched beyond rice: eggs and chicken were cushioned by subsidies and price ceilings, and sugar prices were held fixed through direct incentives paid to sugar producers.

Exhibit 8: Cumulative food CPI response (%) to a 10% increase in oil prices

<table><tr><td>Country</td><td>6m</td><td>12m</td><td>18m</td></tr><tr><td>Thailand</td><td>0.34**</td><td>0.56***</td><td>0.57***</td></tr><tr><td>Singapore</td><td>0.05</td><td>0.20</td><td>0.21</td></tr><tr><td>Malaysia</td><td>0.23*</td><td>0.33*</td><td>0.27</td></tr><tr><td>Indonesia</td><td>0.40*</td><td>0.32</td><td>0.64**</td></tr><tr><td>Philippines</td><td>0.20</td><td>0.32</td><td>0.55</td></tr><tr><td colspan="4">*p&lt;0.10; **p&lt;0.05; ***p&lt;0.01</td></tr></table>

Source: GS Global Investment Research

Exhibit 9: Cumulative food CPI response (%) to a 10% increase in fertiliser prices

<table><tr><td>Country</td><td>6m</td><td>12m</td><td>18m</td></tr><tr><td>Thailand</td><td>0.10</td><td>0.24**</td><td>0.25*</td></tr><tr><td>Singapore</td><td>0.09*</td><td>0.16**</td><td>0.22**</td></tr><tr><td>Malaysia</td><td>0.10**</td><td>0.16**</td><td>0.22**</td></tr><tr><td>Indonesia</td><td>0.14</td><td>0.09</td><td>0.11</td></tr><tr><td>Philippines</td><td>-0.16</td><td>-0.20</td><td>-0.25</td></tr><tr><td colspan="4">*p&lt;0.10; **p&lt;0.05; ***p&lt;0.01</td></tr></table>

Source: GS Global Investment Research

Exhibit 10: Cumulative food CPI response (%) to a $1^{\circ}\mathrm{C}$ increase in El Niño (RONI)

<table><tr><td>Country</td><td>6m</td><td>12m</td><td>18m</td></tr><tr><td>Thailand</td><td>-0.11</td><td>0.46</td><td>-0.06</td></tr><tr><td>Singapore</td><td>0.28</td><td>0.19</td><td>0.47</td></tr><tr><td>Malaysia</td><td>0.19</td><td>-0.27</td><td>-0.47</td></tr><tr><td>Indonesia</td><td>0.06</td><td>0.96</td><td>2.37</td></tr><tr><td>Philippines</td><td>1.95</td><td>2.95</td><td>3.07</td></tr><tr><td colspan="4">*p&lt;0.10; **p&lt;0.05; ***p&lt;0.01</td></tr></table>

Source: GS Global Investment Research

## Disclosure Appendix

## Reg AC

We, Chris Poh and Andrew Tilton, hereby certify that all of the views expressed in this report accurately reflect our personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Chris Poh GS (Singapore) Pte, Andrew Tilton GS (Asia) L.L.C..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is inte

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
