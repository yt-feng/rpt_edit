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
US EQUITY VIEWS

More AI capex, more volatility

Consensus 2027 hyperscaler capex estimates are too conservative. Analyst estimates imply hyperscaler capex will equal \$920 billion in 2027, representing a sharp deceleration in growth from 84% in 2026 to 22% in 2027. We estimate that if incremental investment reaches 2-3% of GDP, similar to the build-out of railroads and autos, hyperscaler capex would reach roughly \$1.1 trillion in 2027 (45% growth). In a more extreme upside scenario, hyperscaler cash flow generation and investment grade credit market capacity would imply potentially \$1.4 trillion in capex (89% growth).  
Upside to AI capex implies upside to earnings and share prices of AI infrastructure beneficiaries in the near term. Most of the price gains in the AI infrastructure complex have been driven by earnings. However, recent valuation expansion and positioning dynamics suggest additional volatility ahead. The P/E of the median AI infrastructure stock has expanded to 26x, the highest multiple since the launch of ChatGPT. The median P/E has increased YTD within Semiconductors and power ex-Utilities but not among the hyperscalers nor memory stocks.  
In the medium term, investors must balance stronger-than-expected capex spending with the risks from a potential deceleration in that spending and uncertainty surrounding the persistence of recent earnings power. Investor expectations that earnings will persist appear less demanding among the hyperscalers relative to Semiconductors ex-Memory. However, recent hyperscaler equity issuance underscores the importance of positive revenue revisions.  
Corporate commentary during Q1 earnings season painted a similar picture to economy-wide surveys that suggest enterprise adoption is nascent. Roughly 54% of companies discussed AI in the context of productivity on their earnings call. However, just 11% of companies quantified the AI productivity gains on a specific use case and only 2% of companies quantified the impact of AI productivity on earnings (vs. 10% and 1%, respectively, last quarter). There was little differentiation in company margins and share price reactions between companies that discussed using AI and those that did not.  
The AI enabled versus AI disrupted debate will persist and drive return dispersion. Investors are debating the “terminal value” of equities as lower-cost competition potentially places downward pressure on incumbent revenue

## Ryan Hammond

+1(212)902-5625

ryan.hammond@gs.com

GS & Co. LLC

## Ben Snider

+1(212)357-1744 | ben.snider@gs.com

GS & Co. LLC

## Jenny Ma

+1(212)357-5775 | jenny.ma@gs.com

GS & Co. LLC

## Daniel Chavez

+1(212)357-7657

daniel.chavez@gs.com

GS & Co. LLC

## Kartik Jayachandran

+1(212)855-7744

kartik.jayachandran@gs.com

GS & Co. LLC

## Christophe Sung

+1(212)902-3841

christophe.sung@gs.com

GS & Co. LLC

growth and profit margins. Software P/E valuations peaked at 39x last year, troughed at 21x in March, and currently stand at 25x, with wide dispersion between data infrastructure and services-oriented stocks. In an illustrative discounted cash flow model, we estimate that 85% of the present value of Software was in the terminal value at the start of the year. The YTD decline in Software valuations can be explained by only modest changes to long-term growth and margin assumptions.

AI-exposed equities, and the infrastructure complex in particular, have powered the US equity market to new highs. “Phase 2” AI infrastructure stocks have rallied by 40% since the start of Q2, driven primarily by strong capex spending. Notably, the mega-cap hyperscalers have recently participated in the rally as evidence of return on investment has strengthened. “Phase 3” stocks with potentially AI-enabled revenues, such as Software, have rebounded from their lows while “Phase 4” stocks with the largest potential productivity gains from AI have continued to trade sideways.

Exhibit 1: Performance of AI-related stocks  
![](images/8adb50b9530280117cb2056b653185e1e66ee55cd5cb5018469520f44ad8a43b.jpg)

<details>
<summary>line chart</summary>

| Date    | AI infrastructure | Mega-cap hyperscalers | AI productivity | Software |
|---------|------------------|------------------------|-----------------|----------|
| Dec-23  | ~100             | ~100                   | ~100            | ~100     |
| Jun-24  | ~130             | ~125                   | ~105            | ~100     |
| Dec-24  | ~125             | ~135                   | ~110            | ~110     |
| Jun-25  | ~140             | ~150                   | ~115            | ~120     |
| Dec-25  | ~160             | ~140                   | ~115            | ~110     |
| Jun-26  | ~260             | ~150                   | ~115            | ~90      |
| Dec-26  | ~270             | ~155                   | ~115            | ~100     |
</details>

AI infrastructure = GSCBAIP2, Software = IGV, AI productivity = GSXUPROD  
Source: GS Global Investment Research

At the same time, the return dispersion within AI-exposed equities has reached a new high in Q2. Last week injected volatility to the AI trade, driven in part by disappointing AVGO earnings and headlines about hyperscaler equity issuance and amplified by investor positioning. The standard deviation of returns of a basket of AI-exposed equities has surged to 53 pp in Q2, marking the widest dispersion of returns since the launch of ChatGPT. That return dispersion has generally been created by varying degrees of positive returns within the infrastructure phase in contrast with positive and negative returns within the application complex.

Exhibit 2: Return dispersion of AI-exposed equities standard deviation of returns of GSTMTAIP basket constituents  
![](images/b68bd55a7cb0c8f6d59fd746771a831b132ff9f5a3baf1c059944f33188fd4f8.jpg)

<details>
<summary>bar chart</summary>

| Quarter | Return dispersion (pp) |
| ------- | ---------------------- |
| 1Q 2023 | 19                     |
| 2Q 2023 | 26                     |
| 3Q 2023 | 22                     |
| 4Q 2023 | 14                     |
| 1Q 2024 | 23                     |
| 2Q 2024 | 19                     |
| 3Q 2024 | 19                     |
| 4Q 2024 | 34                     |
| 1Q 2025 | 16                     |
| 2Q 2025 | 46                     |
| 3Q 2025 | 39                     |
| 4Q 2025 | 37                     |
| 1Q 2026 | 40                     |
| 2Q 2026 | 53                     |
</details>

Source: FactSet, GS Global Investment Research

Exhibit 3: Distribution of AI-exposed equities' YTD returns  
![](images/a62cdfa4e39f7da583d4ce4eb43e81b4d0f711594bf409bbaa85672be272e6ef.jpg)

<details>
<summary>bar chart</summary>

| Category | Value |
| -------- | ----- |
| AI infrastructure (GSCBAIP2) | 59% |
| Software (IGV) | -6% |
| AI productivity (GSXUPROD) | 17% |
</details>

Source: FactSet, GS Global Investment Research

The latest leg of the infrastructure complex has primarily been driven by another wave of hyperscaler capex upgrades. Consensus 2026 estimates for hyperscaler capex have increased by \$200 billion since the start of the year. Analysts now expect the group to spend \$757 billion on capex in 2026, representing year/year growth of 84%.

Exhibit 4: Consensus expects the hyperscalers will spend \$757 billion in 2026 and \$920 billion in 2027  
![](images/d2b1e793320f9b6789db8e0d76e97a2bc20f467dc42f811c74261abca446061d.jpg)

<details>
<summary>stacked bar chart</summary>

| Year       | AMZN  | META  | GOOGL | MSFT  | ORCL  | Total |
| ---------- | ----- | ----- | ----- | ----- | ----- | ----- |
| 2022       | $158  | $154  | $158  | $154  | $158  | $158  |
| 2023       | $154  | $154  | $158  | $154  | $158  | $158  |
| 2024       | $237  | $237  | $237  | $237  | $237  | $237  |
| 2025       | $412  | $412  | $412  | $412  | $412  | $412  |
| Consensus 2026 | $757  | $757  | $757  | $757  | $757  | $757  |
| Consensus 2027 | $920  | $920  | $920  | $920  | $920  | $920  |
</details>

Source: FactSet, GS Global Investment Research

The hyperscalers are on track to allocate all of their cash flows from operations to capex this year. Alongside strong capex spending, the group has sharply reduced share repurchases.

Exhibit 5: Hyperscalers expected to allocate 100% of cash flows from operations to capex  
![](images/7cb0e87f1f30ca06d97641ae5387a89b841cbfdd7bdc23c27ef340e3f667d02e.jpg)

<details>
<summary>line chart</summary>

| Year | S&P 500 Telecom | S&P 500 TMT | Hyperscalers |
|------|-----------------|-------------|--------------|
| 2026 | 98%             | -           | -            |
</details>

Source: Compustat, FactSet, GS Global Investment Research

## We believe consensus 2027 capex estimates are once again too conservative.

Consensus estimates imply hyperscaler capex will equal \$920 billion in 2027, representing a sharp deceleration in growth from 84% to 22%. Analyst estimates have been too conservative during each of the past three years by an average of 45 pp.

Exhibit 6: Consensus hyperscaler capex estimates versus realized capex  
![](images/1cf67521b44a4e0e77d31d1430740bef31fbfa22a7478c2a00612b446beb4f4a.jpg)

<details>
<summary>bar chart</summary>

Consensus capex growth estimates for AI hyperscalers
| Year | Start of year (%) | Realized/Current (%) |
| :--- | :--- | :--- |
| 2024 | 19 | 54 |
| 2025 | 22 | 73 |
| 2026 | 36 | 84 |
| 2027 | 22 | - |
</details>

Source: FactSet, GS Global Investment Research

Exhibit 7: Recent consensus hyperscaler capex estimate revisions  
![](images/f493411ff28d56a7fdb2ec4e02333c3b0e26d82c52a797aeacd41621cfebad72.jpg)

<details>
<summary>bar chart</summary>

Consensus hyperscaler capex estimates
| Period | Year | Capex ($) | Growth (%) |
| :--- | :--- | :--- | :--- |
| Start of Q1 earnings season | 2025 | 412 | +73 |
| Start of Q1 earnings season | 2026 | 673 | +64 |
| Start of Q1 earnings season | 2027 | 790 | +17 |
| Current | 2025 | 412 | +73 |
| Current | 2026 | 757 | +84 |
| Current | 2027 | 920 | +22 |
</details>

Source: FactSet, GS Global Investment Research

The latest earnings season and recent corporate issuance point to upside risk to consensus capex estimates in 2027. The larger-than-expected revenue backlog for the group highlights the persistent imbalance between AI supply and demand. Google Cloud and Amazon's AWS combined backlog equaled \$832 billion as of Q1 compared with \$358 billion six months ago. Our equity analysts do not expect a supply/demand balance will be reached until 2H 2027 at the earliest. GOOGL stated it expects to “significantly

increase” 2027 capex compared to 2026 and recently raised \$86 billion in equity, in part to fund AI spending. There are press reports that META is also considering raising equity.

Exhibit 8: AI hyperscaler 2027 capex scenarios  
![](images/bc41e0cab1482daa51eb1bf95c3d29f13dee61c477cc16e00423eeb9fa3296aa.jpg)

<details>
<summary>bar chart</summary>

2027 AI hyperscaler capex scenarios ($ billion)
| Scenario | Capex ($ billion) | Percentage (%) |
| :--- | :--- | :--- |
| Consensus 2026 | 757 | 84 |
| Consensus 2027 | 920 | 22 |
| Incremental investment equals 2% of GDP | 950 | 26 |
| GS equity analysts | 994 | 31 |
| Incremental investment equals 3% of GDP | 1250 | 65 |
| CFO and IG market capacity | 1433 | 89 |
</details>

Source: GS Global Investment Research

Our equity analysts believe that token consumption will increase by 24x through 2030, led by enterprise agents. The hyperscalers have messaged that their capex spending plans are driven by strong demand signals. Hyperscaler capex will depend on token demand, energy intensity, and input costs. Higher input costs also puts upward pressure on the nominal dollars of capex required to support a given amount of token consumption.

Historical technology cycles provide precedent for more than \$1 trillion in capex in 2027. Incremental AI spending equated to 0.9% of GDP in 2025 and is estimated to reach 1.5% of GDP in 2026. This impulse is similar to the peak impulse during the 1990s, but below the peak of 2-3% during the railroads and electric motor build-outs. We estimate that 2027 hyperscaler capex would equal \$950 billion if the incremental investment impulse reaches 2% of GDP and \$1,250 billion if it reaches 3% of GDP.

Exhibit 9: GS equity analysts forecast a 24x increase in token consumption by 2030  
![](images/07a92c47c7a33691734880ad0ba2bd534f1f900d5babb195107f7e79eb12bc69.jpg)

<details>
<summary>area chart</summary>

| Year | Enterprise Agents | Consumer Agents |
| ---- | ----------------- | --------------- |
| 2025 | ~0                | ~0              |
| 2026 | ~0                | ~0              |
| 2027 | ~10,000,000       | ~5,000,000      |
| 2028 | ~25,000,000       | ~10,000,000     |
| 2029 | ~45,000,000       | ~15,000,000     |
| 2030 | ~75,000,000       | ~25,000,000     |
</details>

Source: GS Global Investment Research

Exhibit 10: Incremental investment in emerging technologies as a share of GDP  
![](images/4c52dda10c068b07e28ce8616cccece617fe93027320f8eb6c0cf60b800ea82d.jpg)

<details>
<summary>bar chart</summary>

"US Generative AI" includes 2026 forecast
| Sector | Share of GDP (%) |
| :--- | :--- |
| US Generative AI (2020s) | 1.5 |
| US Telecom (1990s) | 1.4 |
| US ICT Hardware (1990s) | 1.6 |
| US Auto Infrastructure (1910s) | 2.1 |
| US Electric Motor (1920s) | 2.2 |
| US Railroads (1880s) | 3.4 |
| UK Railroads (1860s) | 4.5 |
</details>

Source: GS Global Investment Research

Availability of capital is unlikely to prevent another year of strong capex growth in 2027. Since the start of 2025, hyperscaler net debt has increased by \$170 billion, but their collective net debt to EBITDA remains extremely low at 0.4x. The hyperscalers could increase their net debt by up to \$950 billion and still carry a net leverage ratio below 1x, consistent with the upper end of the range of companies with AA ratings or better. However, our credit strategists estimate the near-term USD investment grade (IG) market capacity is likely smaller than that, based on the current composition of single-issuer weightings and potential market saturation constraints, though the extent of how “binding” these will be is still a subject of investor debate. Using the USD IG index-eligible debt weightings of money center banks as a guide, they estimate an incremental \$450 billion of issuance for the four largest hyperscalers before reaching the sizing of the index’s current largest issuers. As a result, our credit strategy team expects other syndicated debt financing markets, such as ex-USD corporate bond issuance and new JV “project finance style” structures to play a larger role in the years ahead. They also see significant scope for the private infrastructure market to fill some of the financing need. The hyperscalers could also tap into existing cash balances or use alternative financing sources, such as equity issuance.

Physical capacity could limit hyperscaler capex surprises. There are numerous delayed data center projects in the pipeline and memory, power, and labor have been flagged as constraints to the capex build-out. We believe the recent rise in interest rates could make debt financing more expensive but is unlikely to meaningfully derail large AI hyperscaler capex spending. The AI hyperscalers appear to be taking a long-term approach to their capex spending plans and the strong balance sheets of large AI hyperscalers means that their cost of financing remains historically low even after the backup in yields. The increase in interest rates could pose more of a headwind to the smaller AI hyperscalers that carry more leverage.

Exhibit 11: Hyperscaler net debt to EBITDA has risen but is close to zero  
![](images/a4e69033830cc7b59d1ce5167ef1e673d03842cb651b3bba973b3d01834e74

[中间内容因长度限制已省略]

attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
