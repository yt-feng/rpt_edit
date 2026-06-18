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
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`GS`。标题格式建议：`# GS：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

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
| AI Chatbots | 0.3 |
| Agentic AI (Microsoft paper) | 4.0 |
| Upper-end energy intensity Agentic AI | 15.0 |
Our assumption: 2 Wh/query; c.6x |
| c.13x | c.13x |
| c.50x | c.50x |
</details>

Source: Research Gate

Most industry experts suggest that the current rate of datacenter development is consistent with a share of 20-30% of queries being Agentic AI by 2030 in the US. Considering that we see Europe lagging the US by around five years, we take a similar share of Agentic queries by 2035. We estimate that +10pp uptick in Agentic AI adoption rates could boost European datacenter needs by c.25-30%, resulting in an installed capacity of c.80 GW by 2035. By then, datacenters would account for c.25% of total power demand.

Exhibit 10: Europe's datacenter market would reach c.80 GW total DC capacity by 2035 in our upside case, equivalent to c.25% of demand  
Breakdown of total DC capacity in our base and upside case, 2035 (GW)  
![](images/eb4f1a78181b8371174b39bfa25fd56c7f8d3ec1bfd646f820fa4e65f05db51e.jpg)

<details>
<summary>waterfall chart</summary>

| Category | Value (GW) |
|---|---|
| 2025 | 15 |
| Additions | 20 |
| 2031 EUDCA | 35 |
| Gse Additions | 27 |
| 2035 GSe | 62 |
| AAI Additions | 17 |
| 2035 GSe Upside Case | 79 |
</details>

Source: GS Global Investment Research, European Data Center Association

Our top-down analysis of European power demand indicates that datacenters could contribute to growing power demand by c.1.5-2% later in the decade - that is without the impact of Agentic AI needs, which would add additional tail winds.

Exhibit 11: We expect power consumption to grow by 1.5-2% pa over 2025-29E, with growth rising to 2.5-3.5% pa as electrification and datacenter rollout accelerate  
EU 2025-32E power demand power evolution, breakdown by driver (TWh, percentage)  
![](images/f9b451b355461ef4585fea5858604efc2640ba2f54d1b49db596d68b11068760.jpg)

<details>
<summary>bar chart</summary>

| 2025 | Datacenters | 2,467 |  |
| --- | --- | --- | --- |
| 2025 | Mobility | 1 | 1% |
| 2025 | Heating | 1 | 1% |
| 2025 | Hydrogen | 0 | 0% |
| 2025 | Manufacturing | 1 | 1% |
| 2025 | Aircon | 0 | 0% |
| 2032E | Aircon |  | 0% |
| 2032E | Datacenters | 4 | +c.1.5 - 2% pa |
| 2032E | Mobility | 1 |  |
| 2032E | Heating | 1 |  |
| 2032E | Hydrogen | 1 |  |
| 2032E | Manufacturing | 1 |  |
| 2032E | Aircon |  |  |
</details>

Source: GS Global Investment Research

We simulate a third scenario: hyper-electrification scenario (here). Here — on top of assuming adoption rates for AI Agents similar to our upside case — we broadly assume delivery of Europe’s existing 2030 electrification goals. On this basis, we estimate that power demand could grow even faster, by $+5\%$ pa as early 

[中间内容因长度限制已省略]

m impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
