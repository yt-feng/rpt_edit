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
POWERING UP EUROPE

# Booming Datacenter pipeline and AI spending boom – the pivotal role of energy

European DC pipeline now at nearly 500 GW, 1.5x power demand. We update our datacenter pipeline estimate – the number of DC connection requests received by grid operators across Europe – and the numbers keep increasing. Our latest projection is at c.480 GW, equivalent to 1.5x current European power demand. Our latest update – six months ago – was at c.290 GW (here), and our original estimate (published in January 2025) was 170 GW (here). Although some of this pipeline may be speculative, we believe its growth and size may signal a major construction phase for datacenters. Further, we believe utilities will be pivotal to support the development of datacenters by: providing energy, scouting for land and grid connections, and reinforcing existing power grids.

EU Datacenter Association: +20 GW by 2031. The EUDCA expects +20 GW DC additions by 2031; this would nearly triple the existing capacity to c.35 GW. About $60\%$ of the expected additions are under-construction or have received a final investment decision; the rest is nearly fully approved. This forecast has two implications: (1) DCs would support $+1.5\%$ power consumption growth pa, as of 2028-29 on our estimates, and (2) DCs would be c.10% of Europe's power consumption by 2031E.

Europe and the need for Artificial Intelligence: Productivity, national security, privacy. We see a high likelihood of a major AI roll-out in Europe, supported by the need to enhance productivity, reinforce national security considerations and preserve data sovereignty. As discussed in our report from early 2026 (here), we believe that Europe will reach 65-80 GW (IT capacity) of datacenters by 2035. Later in the decade, datacenters could drive $1.5 - 2\%$ power consumption pa, depending on the adoption rates of AI Agents and AGI.

Big Tech AI spending keeps getting bigger. The AI spending from Big Tech continues to increase: the targets by the five main hyperscalers imply total capex of nearly \$1 trillion in 2027, a near tenfold increase vs 2023.

## Alberto Gandolfi

+39(02)8022-0157

alberto.gandolfi@gs.com

GS Bank Europe SE - Milan

branch

## Ajay Patel

+44(20)7552-1168 | ajay.patel@gs.com

GS International

## Mafalda Pombeiro

+44(20)7552-9425

mafalda.pombeiro@gs.com

GS International

## Dhwani Khenwar

+1(332)245-7724

dhwani.khenwar@gs.com

GS India SPL

## Lawrence Lavizani

+44(20)7051-1060

lawrence.lavizani@gs.com

GS International

Booming Datacenter pipeline and AI spending boom - the pivotal role of energy Europe's datacenter pipeline – measured as the number of connection requests to power grids across Europe – has surged to nearly 500 GW, equivalent to 1.5x current European power demand, up sharply from our most recent projection of c.290 GW six months ago and just 170 GW in January 2025. While some of this pipeline may be speculative, we believe its rapid growth and its scale signal a major datacenter construction phase ahead, spread fairly evenly across the continent. The EUDCA expects +20 GW of additions by 2031, nearly tripling existing capacity, with around 60% already under construction or FID. This would drive +1.5% power consumption growth pa from 2028-29, on our estimates. We continue to believe Europe will reach 65-80 GW of IT capacity by 2035, with datacenters driving 1.5-2% power consumption pa later in the decade, depending on AI Agents and AGI adoption. Meanwhile, Big Tech AI spending keeps climbing, with the five main hyperscalers implying c.\$700 bn of capex in 2026, rising to nearly \$1 trillion in 2027. Next year's AI infrastructure spending would be around ten times larger than in 2023, underscoring that the datacenter boom continues in full force. We believe utilities will be pivotal to this process by providing energy, scouting for land and grid connections, and reinforcing existing power grids to support the incremental consumption.

Exhibit 1: The EU DC pipeline has more than doubled in one year  
EU 28 GSe datacenter pipeline evolution, 2025-26 (GW)  
![](images/b72a367112e3572ed66cde1653687152d4df944a83339986cf4ef8295c867faa.jpg)

<details>
<summary>line chart</summary>

| Date | Value (GW) |
|---|---|
| Jan-25 | c.170 |
| May-25 | c.230 |
| Oct-25 | c.280 |
| Jan-26 | c.290 |
| May-26 | c.480 |
2025 EU-28 Consumption: c.320 GW
</details>

Source: GS Global Investment Research

## Electrification and AI to drive a generational earnings super-cycle

The acceleration in the electrification process (energy security), together with rising AI adoption rates and the continued datacenter build-out, should drive materially higher power consumption. Our hyper-electrification scenario points to +5% annual demand by 2029-30. This would drive €3.5 trn of investment needs in power generation (largely renewables) and power grids, thus supporting a generational earnings super-cycle (see here for details). Several companies have also highlighted an ability to extract AI-driven cost efficiencies, which could provide an additional tailwind to the sector's organic growth. While our base case assumes a c.+9% EPS CAGR for our main electrification compounders, we estimate that hyper-electrification would support EPS growth well in excess of +10% pa.

Exhibit 2: We estimate an EPS CAGR of $c. + 9\%$ to the end of the decade for our key electrification compounders  
2026-30E Clean EPS CAGR breakdown by company (percentage)  
![](images/34c55830c7d39ea0a5a8168fa0b9cc9a265f5c9c435c9c0ee380d67e812ded87.jpg)

<details>
<summary>bar chart</summary>

| Company | Value (%) |
| :--- | :--- |
| Solaria | 24 |
| Elia | 16 |
| RWE | 15 |
| EON | 9 |
| Orsted | 8 |
| Enel | 7 |
| Engie | 6 |
| Naturgy | 4 |
Average*: c.9%
</details>

\*Ex-solaria, Naturgy CAGR shown as 2025-30E  
Source: GS Global Investment Research

## Favour transformative electrification stories, renewables, and energy security infrastructure providers

We favor clusters of companies: (1) Transformative electrification stories include companies where we believe electrification capex is about to meaningfully accelerate (Naturgy, Enel and Engie), significantly transforming these portfolios on a 3-5 year basis. (2) Renewable developers that would benefit from rising returns and organic growth opportunities (RWE, EDPR, Solaria, Orsted); and RES manufacturers that would benefit from rising orders and margins (eg Vestas and Nordex). And (3) Energy security providers, such as ENR, EON and Snam.

Exhibit 3: We see three company clusters as the main beneficiaries Infographic

## We favour three company clusters:

![](images/4a0e041fd9dded86b21a49f1572a278b97826c591cb6c96c5b173dc1a6993da4.jpg)

Transformative Electrification Stories: Naturgy, Enel, Engie

![](images/b9c3b18cef00c485321c3941e7e7300fbc115c0db0990e2aa35d1134f95b9189.jpg)

Renewables:  
Developers (RWE, EDPR, Solaria, Orsted)  
Manufacturers (Vestas, Nordex)

![](images/23489822ec2042a67d4181356b54443cf21f98686080e00f98e1e478c4a1f78f.jpg)  
Source: GS Global Investment Research

Energy Security Providers: Siemens Energy, EON, Snam

The main beneficiaries trade on an average P/E of c.12x and an EV/EBITDA of c.7.5x by 2030E, a discount to the sector average, despite higher growth prospects.

Exhibit 4: The three clusters trade on an average P/E of c.12x by 2030E  
Key valuation metrics, 2026-30E (x)

<table><tr><td></td><td colspan="5">P/E</td><td colspan="5">EV/EBITDA</td></tr><tr><td></td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td></tr><tr><td colspan="11">Transformative Electrification Stories</td></tr><tr><td>Naturgy</td><td>13.2x</td><td>13.1x</td><td>12.5x</td><td>12.0x</td><td>11.3x</td><td>8.3x</td><td>8.3x</td><td>8.1x</td><td>7.9x</td><td>7.7x</td></tr><tr><td>Enel</td><td>13.3x</td><td>12.6x</td><td>11.7x</td><td>10.9x</td><td>10.2x</td><td>7.3x</td><td>7.3x</td><td>7.1x</td><td>6.9x</td><td>6.7x</td></tr><tr><td>Engie</td><td>14.3x</td><td>14.1x</td><td>13.1x</td><td>12.5x</td><td>11.5x</td><td>9.7x</td><td>9.1x</td><td>8.8x</td><td>8.7x</td><td>8.5x</td></tr><tr><td>Average</td><td>13.6x</td><td>13.3x</td><td>12.4x</td><td>11.8x</td><td>11.0x</td><td>8.4x</td><td>8.2x</td><td>8.0x</td><td>7.9x</td><td>7.6x</td></tr><tr><td>Renewables</td><td colspan="10"></td></tr><tr><td>RWE</td><td>22.2x</td><td>17.2x</td><td>16.0x</td><td>13.6x</td><td>12.7x</td><td>10.4x</td><td>9.4x</td><td>9.0x</td><td>8.2x</td><td>7.9x</td></tr><tr><td>EDPR (ex-gains)</td><td>48.6x</td><td>35.2x</td><td>31.8x</td><td>27.0x</td><td>21.5x</td><td>12.6x</td><td>11.7x</td><td>11.1x</td><td>10.4x</td><td>9.4x</td></tr><tr><td>Solaria</td><td>18.9x</td><td>14.4x</td><td>10.9x</td><td>9.2x</td><td>8.1x</td><td>12.0x</td><td>9.3x</td><td>9.4x</td><td>8.1x</td><td>7.3x</td></tr><tr><td>Orsted</td><td>17.8x</td><td>18.9x</td><td>13.8x</td><td>14.2x</td><td>13.1x</td><td>8.2x</td><td>8.1x</td><td>6.2x</td><td>6.5x</td><td>6.3x</td></tr><tr><td>Vestas</td><td>19.4x</td><td>14.1x</td><td>11.6x</td><td>9.7x</td><td>8.4x</td><td>8.4x</td><td>6.6x</td><td>5.5x</td><td>4.5x</td><td>3.7x</td></tr><tr><td>Nordex</td><td>21.0x</td><td>16.1x</td><td>13.5x</td><td>11.9x</td><td>11.0x</td><td>8.5x</td><td>6.5x</td><td>5.4x</td><td>4.8x</td><td>4.4x</td></tr><tr><td>Average</td><td>24.7x</td><td>19.3x</td><td>16.3x</td><td>14.3x</td><td>12.5x</td><td>10.0x</td><td>8.6x</td><td>7.8x</td><td>7.1x</td><td>6.5x</td></tr><tr><td>Energy Security Providers</td><td colspan="10"></td></tr><tr><td>Siemens Energy</td><td>33.0x</td><td>24.6x</td><td>18.6x</td><td>14.6x</td><td>11.8x</td><td>17.4x</td><td>13.1x</td><td>10.1x</td><td>7.9x</td><td>6.6x</td></tr><tr><td>E.ON</td><td>16.5x</td><td>14.1x</td><td>13.2x</td><td>12.4x</td><td>11.8x</td><td>10.6x</td><td>10.0x</td><td>9.8x</td><td>9.6x</td><td>9.5x</td></tr><tr><td>Snam</td><td>14.6x</td><td>14.1x</td><td>13.1x</td><td>12.7x</td><td>12.1x</td><td>11.9x</td><td>11.6x</td><td>11.4x</td><td>11.1x</td><td>10.5x</td></tr><tr><td>Average</td><td>21.3x</td><td>17.6x</td><td>15.0x</td><td>13.2x</td><td>11.9x</td><td>13.3x</td><td>11.6x</td><td>10.4x</td><td>9.5x</td><td>8.8x</td></tr><tr><td>Total Average</td><td>21.1x</td><td>17.4x</td><td>15.0x</td><td>13.4x</td><td>12.0x</td><td>10.5x</td><td>9.3x</td><td>8.5x</td><td>7.9x</td><td>7.4x</td></tr><tr><td>Sector Average</td><td>19.2x</td><td>16.8x</td><td>15.2x</td><td>13.9x</td><td>12.9x</td><td>10.4x</td><td>10.0x</td><td>9.6x</td><td>9.2x</td><td>8.8x</td></tr></table>

Source: GS Global Investment Research, Bloomberg

## AI spending boom and the pivotal role of energy

## European DC pipeline now at nearly 500 GW, or 1.5x EU consumption

Datacenter connection requests to the European power grid have seen, since we first discussed this topic (here) in early 2025, an exponential increase. This is signaling a major upcoming boost to European power demand, in our view. Based on data which we have collected from the main European power grid operators, we estimate the current EU datacenter pipeline at 480 GW. Regionally, the UK, Italy and Germany are the largest regions in absolute terms. Yet, relative to the size of the domestic market, we note that Finland is also quite large.

## Exhibit 5: The european DC pipeline has reached c.480 GW

European data center connection requests, by country (GW, percentage)

Equivalent to c.1.5x of power demand (c.320 GW in 2025)  
![](images/8c7dd4d4f8c518f5215a07004f8a7b3484c00ce0395ab2f7f925526e97136fc0.jpg)

<details>
<summary>pie chart</summary>

DC Connection Requests EU-28
| Country | Percentage (%) |
| :--- | :--- |
| UK | 18 |
| Italy | 17 |
| Germany | 16 |
| Finland | 10 |
| Spain | 8 |
| France | 5 |
| Others | 26 |
</details>

Source: Company data, GS Global Investment Research

Our initial analysis on EU datacenters – published in early 2025 – saw c.170 GW of connection requests across the EU28. Since then, we have completed several iterations with our January 2026 analysis (here) indicating c.290 GW, equivalent to c.90% of Europe's current power demand (c.320 GW). Our latest analysis now implies a DC pipeline of 480 GW, or a +60% increase over our previous projections. The current DC pipeline is also equivalent to 1.5x the current power consumption in Europe.

Exhibit 6: The EU DC pipeline has more than doubled in one year EU 28 GSe datacenter pipeline evolution, 2025-26 (GW)  
![](images/18286c39ac3d223c69a733c6fc807fb77b2858fc0c5dadd454dd8809c5450e72.jpg)

<details>
<summary>line chart</summary>

| Date | Value (GW) |
|---|---|
| Jan-25 | c.170 |
| May-25 | c.230 |
| Oct-25 | c.280 |
| Jan-26 | c.290 |
| May-26 | c.480 |
2025 EU-28 Consumption: c.320 GW
</details>

Source: GS Global Investment Research

## EU Datacenter Association forecasts +20 GW by 2031

As of the end of 2025, Europe featured datacenter capacity of c.15 GW, mostly located in the FLAP-D area (Frankfurt, London, Amsterdam, Paris, Dublin). The European Data Center Association collects bottom-up estimates by operators in the DC supply chain; on this basis, the EUDCA expects that +20 GW will be built by 2031, bringing the total EU DC capacity to c.35 GW by then. Out of the expected additions, the EUDCA points out that about $60\%$ is already under construction or FID. The rest has essentially reached all the authorizations — this implies a high visibility on DC additions over the coming five years in Europe.

Exhibit 7: The EUDCA forecasts +20 GW DC capacity additions by 2031  
European datacenter evolution, 2025-31 (GW)  
![](images/106dfa9fee3e006aa394079436c0c38dad497bd26d60b93b26e97dbac319fa78.jpg)

<details>
<summary>waterfall chart</summary>

| Period | Capacity (GW) |
|---|---|
| 2025 | 15 |
| Final Investment Decision/Under-construction | 12 |
| Reay-to-build | 8 |
| 2031 | 35 |
</details>

Source: European Data Center Association

This expected DC build-out would, we estimate, represent +c.7% vis a vis the current power consumption in Europe. Considering that most of these projects are projected to be operational in 2028-29, we estimate that by then, datacenters could drive +c.1.5% annual power consumption in Europe. By 2031, 35 GW of DC capacity would account for c.10% of total European power demand.

## Exhibit 8: DC capacity development to 2031 could drive +1.5% power demand growth pa, as of 2028-29

35 GW of DC capacity in 2031 would be equivalent to $10\%$ of total EU power demand

![](images/53db59b137a4ff6ffbb9305e041bcab71a34c04be0d730b600cc00d8200e8225.jpg)

<details>
<summary>pie chart</summary>

| Scenario | Value |
| --- | --- |
| c.1.5% increase in annual power demand by 2028-29 | 1.5% increase |
| 10% of European power demand by 2031 | 10% increase |
</details>

Source: GS Global Investment Research

## AI Agents might significantly increase DC needs

Based on our recent analysis (here), we believe the market underestimates Agentic AI (AAI) as a catalyst for datacenter needs, as well as power demand growth. Tech

literature suggests that Agentic AI queries can consume up to 50x more energy than a typical AI chatbot. A recent paper by Microsoft implies that Agentic AI energy intensity may drop to 13x (c.4.0Wh/query). Our analysis on AI Agents assumes a further 50% improvement in energy intensity and instead of adopting a 15 Wh power need per agentic query, we lower this to 2 Wh/query. This compares with current AI chatbots at 0.3 Wh/query.

Exhibit 9: Agentic AI queries are much more energy-intensive than traditional queries; we adopt a conservative approach  
Energy use of traditional vs. Agentic AI query (Wh/query)  
![](images/c5c13efcd403d850186e83e0adbd3e5b8f7521a52ac9b22c5d2965c41b7a541d.jpg)

<details>
<summary>bar chart</summary>

| Category | Value (c. Wh/query) |
|---|---|
| AI Cha

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
