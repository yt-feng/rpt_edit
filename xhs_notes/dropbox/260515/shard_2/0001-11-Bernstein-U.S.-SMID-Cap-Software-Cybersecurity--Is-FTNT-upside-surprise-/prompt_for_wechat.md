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
1. `# 标题`：一句主判断，不超过 32 字。
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
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# U.S. SMID-Cap Software

# Cybersecurity: Is FTNT upside surprise a signal for other vendors?

![](images/8791c242cde0a31caf8f938bf6e8dc0445ccc803e2ca74daae2ebf9d8fcaf122.jpg)  
Peter Weed

+1 917 344 8390

peter.weed@Bernsteinsg.com

![](images/4446631bedafbd837ca4bf771f61c28b0fa28189b9b88d2823247c301f2bbc2d.jpg)

Armin Hadavi, CFA

+1 917 344 8463

armin.hadavi@Bernsteinsg.com

Last week, Fortinet's Q1'26 earnings delivered a nice upside surprise, with its largest revenue growth beat (+6.9% vs. midpoint guide) since the '21 COVID demand bubble. This is relative to "normal" beats in the 2-3% range. Yes, \~1% of the beat can be attributed to passing through higher memory prices on appliances, but that still leaves a few % of extra that the company chalked up in no small part to a bubble of demand in firewall appliances to support Operational Technology ("OT") cybersecurity. OT cyber focuses on securing critical physical device infrastructure that includes more and more embedded software and even network/internet connected, such as medical devices, power/energy grids, or manufacturing equipment. We understand this demand reflects recent Middle-East friction and nation-state hacks such as Stryker combined with new Europe OT regulations and the US government leaning on businesses with OT infrastructure to improve their cybersecurity posture. In our Fortinet model published after earnings, it implicitly anticipates this excess demand remains elevated for several quarters, perhaps into next year as US and European companies evaluate and address their exposure. It made us think... what other cyber vendors in our coverage could see OT cyber tailwinds?

OT Network security leaders are Fortinet and Palo Alto. According to Gartner, they are effectively tied for #1 in OT Network Security, both with a similar market share. We wonder if this could show up as excess strength in Palo Alto's firewall appliances this quarter. Perhaps a few \$10MM are possible, but we do note the actual regulation forcing OT cyber compliance is in Europe (US is a bit lighter touch, as you can see in the link above), where Fortinet's revenue over-indexes by 2x vs. Palo Alto. On the other hand, the Stryker hack and industry noise are strong in the US, so perhaps demand will be elevated on both sides of the Atlantic. We don't anticipate it would have as much benefit for Palo Alto's NGS ARR, unless its endpoint or SSE are part of the pull like...

IoT endpoint security could benefit? SentinelOne has focused on OT (e.g., manufacturing, energy) including broad OS support and securing for segmented networks (for instance, protected from direct internet access). Their Singularity platform is designed to secure unmanaged, internet-connected devices (IoT/IIoT) that cannot host traditional security agents, such as industrial control systems, surveillance cameras, and building automation systems. In addition, CrowdStrike is making strides with recent announcements of its own OT/IoT capabilities, and historic relationships with partners like Dragos.

Not to be left behind, SASE/SSE is also trying to be relevant in OT. Zscaler acquired Airgap Technologies in 2024 to get closer to the OT/IoT security space. They offer an alternative approach to OT network security that is intended to overcome challenges with the use of physical appliance firewalls, particularly incomplete coverage due to challenging implementation approach. Not to mention, Cloudflare emphasizes similar approaches, with partners like Brixio deploying them for IT/OT converged cyber solutions. We note Cloudflare's focus seems thinner and wasn't a discussed tailwind in their Q1 earnings.

Will there be a noticeable bump outside of firewall appliances? We aren't sure. We are looking forward to the upcoming earnings for Palo Alto, SentinelOne, CrowdStrike, and Zscaler to see if any of all of them get a little extra "juice" from the urgency and government prodding on OT cybersecurity.

Bernstein TICKER TABLE 

<table><tr><td rowspan="2" colspan="3"></td><td colspan="2">13 May2026</td><td rowspan="2">TTMRel.</td><td rowspan="2"></td><td rowspan="2" colspan="3">Adjusted EPS</td><td rowspan="2" colspan="3">Adjusted P/E (x)</td></tr><tr><td>Closing</td><td>Price</td></tr><tr><td>Ticker</td><td>Rating</td><td>Cur</td><td>Price</td><td>Target</td><td>Perf.</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>FTNT (Fortinet)</td><td>M</td><td>USD</td><td>117.69</td><td>92.00</td><td>(14.4)%</td><td>USD</td><td>2.76</td><td>3.37</td><td>3.93</td><td>42.7</td><td>34.9</td><td>29.9</td></tr><tr><td>PANW (Palo Alto Networks)</td><td>O</td><td>USD</td><td>227.79</td><td>209.00</td><td>(7.8)%</td><td>USD</td><td>3.34</td><td>3.97</td><td>4.45</td><td>68.2</td><td>57.3</td><td>51.2</td></tr><tr><td>S (SentinelOne)</td><td>O</td><td>USD</td><td>16.08</td><td>19.00</td><td>(47.4)%</td><td>USD</td><td>0.20</td><td>0.34</td><td>0.55</td><td>80.2</td><td>46.7</td><td>29.1</td></tr><tr><td>ZS (Zscaler)</td><td>O</td><td>USD</td><td>152.43</td><td>228.00</td><td>(64.2)%</td><td>USD</td><td>3.28</td><td>4.20</td><td>5.23</td><td>46.5</td><td>36.3</td><td>29.1</td></tr><tr><td>NET (Cloudflare)</td><td>M</td><td>USD</td><td>192.62</td><td>136.00</td><td>1.6%</td><td>USD</td><td>0.92</td><td>1.33</td><td>1.73</td><td>208.3</td><td>145.3</td><td>111.3</td></tr><tr><td>SPX</td><td></td><td></td><td>7,444.25</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended   
S base year is 2026;   
Source: Bloomberg, Bernstein estimates and analysis.

# INVESTMENT IMPLICATIONS

No changes to models, price targets, or ratings.

# I. REQUIRED DISCLOSURES

References to "Bernstein" or the "Firm" in these disclosures relate to the following entities: Bernstein Institutional Services LLC (April 1, 2024 onwards), Bernstein & Co., LLC (pre April 1, 2024), Bernstein Autonomous LLP, BSG France S.A. (April 1, 2024 onwards), Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited, Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社) and analysts employed by SG Africa Technologies & Services to produce Bernstein under a Global Services Agreement in place between Bernstein and SG.

Bernstein is part of a joint venture between SG (SG) and AllianceBernstein, L.P. (AB). Unless specifically noted otherwise, for purposes of these disclosures, references to Bernstein's “affiliates” relate to both SG and AB and their respective affiliates.

# VALUATION METHODOLOGY

# Fortinet Inc

Our price target of \$92 is an average of DCF (with 11% WACC and 3% terminal growth) and 8x P / Sales (Next 5-8Q) comp multiple. P / Sales (Next 5-8Q) comp multiple is selected in the >10% OpM Cloud SaaS cohort from our valuation framework analysis. Because of its large hardware footprint, we discount the multiple consistent with its historical level. We assume current Cloud SaaS multiples regression line remains consistent for 1+ year.

# Palo Alto Networks Inc

Our target price \$209 is a 50/50 average of DCF (with 10% WACC and 3% terminal growth) and P / Sales (Next 5-8Q) comp multiple. P / Sales (Next 5-8Q) comp multiple of 13X is selected in the >10% OpM Cloud SaaS cohort from our “Rule-of-40” based valuation framework analysis. We assume current Cloud SaaS multiples regression line remains consistent for 1+ year.

# SentinelOne Inc

Our price target of \$19 is an average of DCF (12% WACC, 3% terminal growth) and 5.5x P / Sales (Next 5-8Q) comp multiple. P / Sales (Next 5-8Q) comp multiple is selected in the high-growth proportion of Ro40 Cloud SaaS cohort from our valuation framework analysis. We assume the current Cloud SaaS multiples regression line remains consistent for 1+ year.

# Zscaler Inc

Our price target of \$228 is an average of DCF (11% WACC, 3% terminal growth) and 10x P / Sales (Next 5-8Q) comp multiple. P / Sales (Next 5-8Q) comp multiple is selected in the >10% OpM Cloud SaaS cohort from our valuation framework analysis. We assume current Cloud SaaS multiples regression line remains consistent for 1+ year.

# Cloudflare Inc

Our price target of \$136 is an average of DCF (with 10% WACC and 3% terminal growth) and 16x P / Sales (Next 5-8Q) comp multiple. P / Sales (Next 5-8Q) comp multiple is selected in the 10%+ OpM Cloud SaaS cohort from our valuation framework analysis. We assume current Cloud SaaS multiples regression line remains consistent for 1+ year.

# RISKS

# Fortinet Inc

Downside risks beyond the macroeconomic risks include: high customer penetration, focus on integrated hardware + software while the market moves to software only, competitive overlap on platform strategy with both best-of-breed and hyperscaler consolidators, “good enough” product that could face technical risk with customers preferring “best-of-breed”.

Upside risks include strong success with their new SASE offering, longer more durable demand for hardware firewalls, success moving up market into enterprise.

# Palo Alto Networks Inc

Downside risks beyond the macroeconomic risks include: high customer penetration, exposure to churn on their hardware firewalls, trade financing to keep billings and cash flow high, competitive overlap on platform strategy with both best-of-breed and hyperscaler consolidators, premium price, “good enough” product that could face technical risk with customers preferring “best-of-breed”, high valuation, slowing billings growth in the near term.

# SentinelOne Inc

Downside risks beyond the macroeconomic risks include: continued tie to cloud growth, executive talent churn and operational disruption during ramp up of replacements, execution risk in going up-market to target enterprise customers; maintaining traction in the product portfolio outside their core endpoint business, upmarket “best-of-breed” competitors moving into their managed service provider customers, platforms moving into their core business

# Zscaler Inc

Downside risks beyond the macroeconomic risks include: continued tie to cloud growth, attractiveness of alternative technology in single-vendor SASE and cloud-native SSE as competitive threats, premium price and competitors undercutting them, preferences for cybersecurity consolidation.

# Cloudflare Inc

Downside risks beyond the macroeconomic risks include: continued tie to cloud growth, execution risk in sales model transformation; less visibility in consumption and revenue predictability; building credible Act II / III products and demonstrating demand, hyperscalers moving into their core CDN and expansion security businesses, high valuation.

Upside risks include AI driving demand for their edge PaaS, and success selling a broader cybersecurity platform either of both of which exceed revenue expectations.

# RATINGS DEFINITIONS, BENCHMARKS AND DISTRIBUTION

# EQUITY RATINGS DEFINITIONS

# Bernstein brand

The Bernstein brand rates stocks based on forecasts of relative performance for the next 12 months versus the S&P 500 for stocks listed on the U.S. and Canadian exchanges, versus the Bloomberg Europe Developed Markets Large and Mid Cap Price Return Index EUR (EDME) for stocks listed on the European exchanges and emerging markets exchanges outside of the Asia Pacific region, versus the Bloomberg Japan Large and Mid Cap Price Return Index USD (JPL) for stocks listed on the Japanese exchanges, and versus the Bloomberg Asia ex-Japan Large and Mid Cap Price Return Index (ASIAX) for stocks listed on the Asian (ex-Japan) exchanges -unless otherwise specified.

The Bernstein brand has three categories of ratings:

- Outperform: Stock will outpace the market index by more than 15 pp   
- Market-Perform: Stock will perform in line with the market index to within +/-15 pp   
- Underperform: Stock will trail the performance of the market index by more than 15 pp

Coverage Suspended: Coverage of a company under the Bernstein brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors on events and developments.

Not Covered (NC) denotes companies that are not under coverage.

Bernstein brand stock ratings are based on a 12-month time horizon.

# Autonomous brand – common stocks

The Autonomous brand rates common stocks as indicated below. As our benchmarks we use the Bloomberg Europe 500 Banks And Financial Services Index (BEBANKS) and Bloomberg Europe Dev Mkt Financials Large and Mid Cap Price Ret Index EUR (EDMFI) index for developed European banks and Payments, the Bloomberg Europe 500 Insurance Index (BEINSUR) for European insurers, the S&P 500 and S&P Financials for US banks and Payments coverage, S5LIFE for US Insurance, the S&P Insurance Select Industry (SPSIINS) for US Non-Life Insurers coverage, and the Bloomberg Emerging Markets Financials Large, Mid and Small Cap Price Return Index (EMLSF) for emerging market banks and insurers and Payments. Ratings are stated relative to the sector (not the market).

The Autonomous brand has three categories of common stock ratings:

- Outperform (OP): Stock will outpace the relevant index by more than 10 pp   
- Neutral (N): Stock will perform in line with the market index to within +/-10 pp   
- Underperform (UP): Stock will trail the performance of the relevant index by more than 10 pp

Coverage Suspended: Coverage of a company under the Autonomous research brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors on events and developments.

Those denoted as 'Feature' (e.g., Feature Outperform FOP, Feature Under Outperform FUP) are our core ideas.

Not Covered (NC) denotes companies that are not under coverage.

Autonomous brand common stock ratings are based on a 12-month time horizon.

# Autonomous brand – preferred stocks

The Autonomous brand has three categories of preferred stock ratings:

- Outperform (OP): The total return of the preferred instrument is expected to outperform preferred securities of other issuers operating in similar sectors or rating categories over the next six months.   
- Neutral (N): The total return of the preferred instrument is expected to perform in line with preferred securities of other issuers operating in similar sectors or rating categories over the next six months.   
- Underperform (UP): The total return of the preferred instrument is expected to underperform preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

Autonomous preferred stock ratings are based on a 6-month time horizon.

# AUTONOMOUS CREDIT RESEARCH

Where this report contains investment recommendations for credit instruments, as defined in article 3(1)(35) of the Market Abuse Regulation, the information below is presented to comply with its disclosure requirements.

The report may also include reference(s) to published opinions by other Autonomous or Bernstein analysts covering the equity securities of the issuer(s) referenced herein. Please note an investment recommendation for credit instruments published by the author(s) of this report may differ from the published view of the analyst covering equity securities for the issuer(s) contained in this report and vice versa.

# CREDIT RATINGS DEFINITIONS

The Autonomous brand has three categories of credit ratings:

\- Credit Outperform (C-OP): The total return of the Reference Credit Instrument is expected to outperform the credit spread of bonds of other issuers operating in similar sectors or rating categories over the next six months.

- Credit Neutral (C-N): The total return of the Reference Credit Instrument is expected to perform in line with the credit spread of bonds of other issuers operating in similar sectors or rating categories over the next six months.   
- Credit Underperform (C-UP): The total return of the Reference Credit Instrument is expected to underperform the credit spread of bonds of other issuers operating in similar sectors or rating categories over the next six months.

Autonomous credit ratings are based on a 6-month time horizon.

A list of all investment recommendations produced by the author(s) of this report alongside credit ratings history are available upon request.

It is at the sole discretion of the Firm as to when to initiate, update and cease research coverage. The Firm has established, maintains and relies on information barriers to control the flow of information contained in one or more areas (i.e. the private side) within the Firm, and into other areas, units, groups or affiliates (i.e. public side) of the Firm

DISTRIBUTION OF EQUITY RATINGS/INVESTMENT BANKING SERVICES 

<table><tr><td>Equity Rating</td><td>Market Abuse Regulation (MAR) and FINRA Rating Category</td><td>Global Rating Distribution</td><td>Investment Banking Relationships*</td></tr><tr><td>Outperform</td><td>BUY</td><td>51.1%</td><td>16.5%</td></tr><tr><td>Market-Perform (Bernstein Brand) Neutral (Autonomous Brand)</td><td>HOLD</td><td>36.3%</td><td>17.8%</td></tr><tr><td>Underperform</td><td>SELL</td><td>12.6%</td><td>14.9%</td></tr></table>

\* These figures represent the percentage of companies within each equity rating category for which affiliates of Bernstein have provided investment banking services within the previous 12 months.
As of March 31, 2026. All figures are updated quarterly.

# PRICE CHARTS / RATINGS AND PRICE TARGET HISTORY

Prior to April 1, 2024, Bernstein & Co., LLC. issued the ratings and price target information in the graph(s) below for the following companies: Fortinet Inc, Palo Alto Networks Inc, SentinelOne Inc, Zscaler Inc and Cloudflare Inc.

![](images/bad8e740d99e6b2e9289e8440cd46a986d12f095609f9e911ba4401b8c2ffc45.jpg)

<details>
<summary>line</summary>

| Date       | Rating | Price   |
| ------

[中间内容因长度限制已省略]

 learning or artificial intelligence system, or as a prompt or input into any such system. You also may not, without Bernstein's express written consent, do any of the foregoing in connection with your own internal machine learning or artificial intelligence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or sUBScribe for shares, or to induce engage in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek for independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a Citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively "Bloomberg"). Bloomberg or Bloomberg's licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg's licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
