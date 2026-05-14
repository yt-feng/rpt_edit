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
# US Economics Mid-Year Outlook

# Capex Over Consumption

Gradual Middle East de-escalation yields trend-like growth. Any consumer drag is modest and offset by strong AI-led capex. Inflation stays firm near term as oil replaces tariffs. The Fed holds through 2026, easing modestly in 2027.

# Key takeaways:

The base case: Gradual de-escalation, a short-lived burst in headline inflation, and a patient Fed. We expect trend-like growth in US real GDP, assuming a gradual de-escalation of the Middle East conflict: 2.3% in 2026 and 2.6% in 2027. A minor drag on consumer spending is offset by AI capex.

Consumer spending: Energy headwinds neutralize fiscal stimulus. Higher gas prices cause growth in real consumption to decelerate to 1.8% in 2026. When the oil shock fades, consumption rebounds in 2027. We are cautious on our outlook for spending by low- and middle-income cohorts, who spend more on energy. Upper-income consumers benefit from high levels of wealth.

Business spending: Full steam ahead. AI-related spending is more structural than cyclical and provides resiliency amid geopolitical uncertainty. We expect nonresidential business fixed investment to grow by 7% in 2026 and accelerate to 8% in 2027. Hyperscaler spending exceeds \$1tr in 2027.

Fiscal policy: Wide deficits. No fiscal stimulus before the midterm elections and divided government afterwards points to budget gridlock. Fiscal deficits remain around 6% of GDP. Deficit risks come from IEEPA tariff refunds and a large reconciliation bill ahead of the midterms that boosts defense spending, includes infrastructure investment, and adds affordability measures.

Trade: A more durable tariff regime. We expect Section 301 and 232 reviews to be completed in the coming weeks. The USMCA review is approaching, but negotiations appear to be progressing slowly, making it increasingly difficult to add new sUBStantive chapters before the July deadline.

Labor market: The "curious balance" persists. We look for modestly stronger employment growth in 2026 and 2027 – about 50-60k per month on average – pushing the unemployment rate to fall to 4.1% in 2027. AI adoption puts some minimal upward pressure on the unemployment rate.

Inflation: A near-term peak, then gradual descent. Core PCE inflation decelerates in 2H 2026, and the 12-month rate of inflation slows in 2027. We see core PCE at 2.8% 4Q/4Q in 2026, and 2.3% in 2027. Risks are in the direction of inflation persistence.

Monetary policy: The bar for rate cuts has risen. Another supply shock keeps the Fed on hold in 2026. Slowing inflation in 2027 leads the Fed to cut

MS & CO. LLC

# Michael T Gapen

Chief US Economist

Michael.Gapen@morganstanley.com +1 212 761-0571

# Sam D Coffin

Economist

Sam.Coffin@morganstanley.com +1 212 761-4630

# Diego Anzoategui

Economist

Diego.Anzoategui@morganstanley.com +1 212 761-8573

# Arunima Sinha

Global Economist

Arunima.Sinha@morganstanley.com +1 212 761-4125

# Heather Berger

Economist

Heather.Berger@morganstanley.com +1 212 761-2296

# Lingdi Xu

Economist

Lingdi.Xu@morganstanley.com +1 212 761-2957

25bp in March and June to a terminal target range of 3.0-3.25%. If inflation is persistent, or r\* is moving higher, then the normalization cycle is likely over.

Monetary policy, part 2: A regime shift at the Fed? Incoming Chair Kevin Warsh pushes for changes. Interest rates will be driven by the data, but balance sheet policies come up for debate. That said, they require consensus, regulatory reform, and time. On communication policy, a Warsh-led Fed may talk less, creating more short-term policy uncertainty.

# Alternate scenarios: We consider four alternatives to our baseline

Scenario 1: Aggregate demand upside. The oil shock fades, while stronger confidence and wealth support consumption and business investment. Inflation firms and the Fed hikes 100bp in 2027.

Scenario 2: AI productivity boost with labor displacement. Broader AI adoption boosts productivity, but pushes unemployment to 4.5% in 2026 and 4.8% in 2027. The Fed begins cutting rates in early 2027.

Scenario 3: Permanent oil premium. Persistent energy costs keep inflation elevated, with core PCE at 3.1% in 2026 and 2.8% in 2027. The Fed remains cautious and keeps rates unchanged at 3.50-3.75% through the end of 2027.

Scenario 4: A global recession. Oil prices surge to \$140-160/bbl through 3Q26, causing supply shortages and demand destruction that push the economy into recession.

# Special topics:

# Special Topic: AI and labor markets: Not yet a macro labor story, but no longer invisible

Labor market data point to early, narrow AI displacement while aggregate disruption remains small. There are signs of overall task reshuffling.

# Special Topic: AI is boosting output rather than cutting jobs

Productivity is rising faster in industries MS identifies as high-AI exposure than in median- or low-AI industries. The productivity pickup reflects faster output growth and capital deepening rather than labor displacement.

# Executive Summary

# A Multipolar World Brings More Geopolitical Competition

Just as it appeared that "animal spirits" were ready for liftoff in early 2026, the US economy was hit with an oil price shock following the initiation of hostilities in the Middle East. Brent futures, which had been hovering around \$70/bbl in early February, have ranged between \$90-120/bbl since. This represents the fourth supply shock to hit the economy in recent years, with the first three being the COVID pandemic, the Russia-Ukraine conflict, and the tariff shock of 2025.

We continue to emphasize that uncertainty is elevated, particularly given the tenuous ceasefire in place between the US and Iran. Multiple paths for the US economy remain viable and baseline forecasts are less relevant than normal. We remain prepared to revise early and often, as the facts and developments dictate.

As we look back over recent years and cast our gaze forward, four key themes for 2026 from MS are: (1) rewiring commerce for a Multipolar World, (2) AI Tech Diffusion, (3) the Future of Energy, and (4) Societal Shifts.

As it relates to the macroeconomic performance of the US economy, these key themes mean we continue to see a shift away from an era of benign globalization toward one defined by rising economic nationalism in key sectors, intensifying geopolitical competition, and the growing risk that strategic resources are used as policy tools. For example, the conflict in the Middle East is likely to intensify competition for energy sources and delivery channels in the same way trade and pandemic shocks reshaped the landscape in prior years. Just how much remains to be seen, but the direction of travel seems clear. This transition is increasing uncertainty and prompting us to rethink monetary policy settings, inflation trends, and the underlying drivers of GDP growth.

Our 2026 US Economics Mid-Year Outlook is anchored around the following themes:

\- A Multipolar World means rewiring of supply chains: Our outlook for the US and global economy includes a modestly higher oil risk premium with Brent at \$80-90/bbl for the rest of this year and \$80/bbl next. This reflects two assumptions: 1) a generally benign de-escalation of the conflict and 2) strategic stockpiling behavior, a shift toward more secure energy supply chains, and a repricing of geopolitical risk in oil logistics. The oil shock and conflict that started it complement trends in recent years where more countries, including the US, desire domestic inventories of key imports, encourage resource hoarding, reconfigure supply chains, and reduce reliance on foreign supplies.

\- Capex over consumption: Higher gasoline prices are likely to neutralize the effects of the OBBBA on households, suppressing spending on goods in the process. In the other direction is nonresidential business investment, where AI-related spending continues apace and interest in building out domestic resilience and self-sufficiency remains high. Evidence of reshoring remains thin, but the US continues to favor policies that pull capital back home. If we exclude imports, business spending and private consumption contribute similar amounts to GDP growth across the forecast horizon.

\- Above-target inflation: Just as tariff effects were expected to wane, energy prices have taken over and should keep headline inflation firm into year end. We view spending in the AI build-out phase as keeping demand for power, infrastructure, and commodities firm. We believe AI will ultimately boost productivity and has the potential to be disinflationary, but we cannot rule out near-term demand effects on inflation. This tension matters for the Fed, as indicated by their change in tone in April. Patience is the order of the day and the bar for easing appears higher. We remain optimistic on inflation and see it moderating in 2027.

\- Regime shift: If our outlook proves accurate, this would be another data point that suggests the US economy has exited the low inflation, low interest rate, loose monetary policy, and tight fiscal backdrop that characterized the post-GFC economy. The regime shift is from a world optimized for efficiency to one optimized for resilience.

# The Baseline: Benign de-escalation, capex over consumption

Taking a view on the US economy requires assumptions about the outcome of the conflict in the Middle East, however uncertain that process may be. While downside risks to global growth remain elevated on account of high energy prices, the US enjoys greater insulation (though not isolation) from the effects of higher energy prices. With about 85% of the oil exiting the Strait of Hormuz bound for Asia and much of Europe's natural gas supply coming from the region, we expect the more acute effects of the energy crisis felt in other economic zones.

Oil price shocks generally have three transmission mechanisms into the US economy: 1) higher gasoline prices weigh on real purchasing power, 2) falling equity markets can generate negative wealth effects, and 3) prolonged uncertainty can weigh on business spending and hiring. To date, with emphasis on "to date", the US economy is receiving the first of these effects, but not the latter. This is the case when oil rises high enough to boost inflation, but not so high as to turn the narrative to a growth story.

Our baseline assumption is that we see gradual de-escalation of the conflict, leaving oil as a modest drag on real spending that does not metastasize further. If so, then the US economy should see trend-like growth in real GDP, stability in labor markets, and a boost to headline inflation that fades out of year-on-year rates of inflation in 2027. This outlook is less optimistic than we had pencilled in earlier this year, but it would be a favorable outcome, all else equal.

Severe demand destruction remains possible and our downside scenario is oil that moves to \$140/bbl over the remainder of the year. It is also possible that we see a permanently higher oil risk premium than we are thinking, which we include in an alternative scenario where oil averages \$120/bbl this year and \$90-100/bbl next year. This could mean energy prices have more pronounced second round effects on inflation than we assume. We include two other alternative scenarios: one where the conflict de-escalates rapidly and animal spirits take over, and another where AI adoption boosts productivity, but displaces some labor.

Exhibit 1: US Economics Year-Ahead Outlook: Forecast Summary 

<table><tr><td colspan="5">4Q/4Q % change, except where noted</td></tr><tr><td></td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>Real GDP</td><td>2.4</td><td>2.0</td><td>2.3</td><td>2.6</td></tr><tr><td>Final Sales1</td><td>2.6</td><td>2.2</td><td>2.1</td><td>2.3</td></tr><tr><td>Final Domestic Demand2</td><td>3.0</td><td>1.8</td><td>2.4</td><td>2.8</td></tr><tr><td>Final Private Domestic Demand3</td><td>2.9</td><td>2.4</td><td>2.5</td><td>3.1</td></tr><tr><td>Personal Consumption Expenditures</td><td>3.4</td><td>2.1</td><td>1.8</td><td>2.1</td></tr><tr><td>Nonresidential Fixed Investment</td><td>0.9</td><td>5.6</td><td>7.0</td><td>8.0</td></tr><tr><td>- Structures</td><td>-4.8</td><td>-5.5</td><td>-3.9</td><td>2.0</td></tr><tr><td>- Equipment</td><td>3.2</td><td>9.6</td><td>10.2</td><td>10.5</td></tr><tr><td>- IPP</td><td>2.3</td><td>8.0</td><td>9.2</td><td>8.0</td></tr><tr><td>Residential Investment</td><td>1.3</td><td>-3.8</td><td>-1.3</td><td>1.5</td></tr><tr><td>Exports</td><td>3.3</td><td>1.1</td><td>4.0</td><td>1.8</td></tr><tr><td>Imports</td><td>6.2</td><td>-1.9</td><td>6.0</td><td>5.0</td></tr><tr><td>Government</td><td>3.6</td><td>-1.2</td><td>2.1</td><td>1.3</td></tr><tr><td>Inventory contribution (pct pts, a.r.)</td><td>-0.2</td><td>-0.2</td><td>0.1</td><td>0.2</td></tr><tr><td>Trade contribution (pct pts, a.r.)</td><td>-0.5</td><td>0.4</td><td>-0.4</td><td>-0.4</td></tr><tr><td colspan="5">Labor market</td></tr><tr><td>Civilian Unemployment Rate (%, eop)</td><td>4.1</td><td>4.5</td><td>4.3</td><td>4.1</td></tr><tr><td colspan="5">Inflation</td></tr><tr><td>Consumer Price Index</td><td>2.7</td><td>2.7</td><td>3.4</td><td>2.0</td></tr><tr><td>CPI ex Food &amp; Energy</td><td>3.3</td><td>2.7</td><td>2.7</td><td>2.5</td></tr><tr><td>PCE Price Index</td><td>2.6</td><td>2.8</td><td>3.2</td><td>2.0</td></tr><tr><td>PCE ex Food &amp; Energy</td><td>3.0</td><td>2.9</td><td>2.8</td><td>2.3</td></tr><tr><td colspan="5">Monetary Policy</td></tr><tr><td>Fed Funds Target (%, midpoint of target range, eop)</td><td>4.375</td><td>3.625</td><td>3.625</td><td>3.125</td></tr></table>

Note: 1. GDP less inventories. 2. GDP less inventories and trade. 3. Consumption plus fixed investment. Source: Bureau of Economic Analysis, Bureau of Labor Statistics, Federal Reserve Board, MS forecasts

Exhibit 2: US Economics Year-Ahead Outlook:   
![](images/1046bbdaa2850e345623a5076f8e40279e01646d33de7fb0023880f6c565eeb3.jpg)

<details>
<summary>bar_line</summary>

Contributions to Real GDP (pp, annual rate)
| Quarter | Business fixed investment (pp) | Residential investment (pp) | Trade (pp) | Inventories (pp) | Government (pp) | Consumption (pp) | Real GDP (pp) |
|---|---|---|---|---|---|---|---|
| 1Q25 | 1.0 | -0.5 | -3.0 | 2.0 | -0.5 | 1.0 | -0.5 |
| 2Q | 0.8 | 0.0 | 5.0 | -3.0 | -0.5 | 1.0 | 3.8 |
| 3Q | 0.0 | 0.0 | 2.0 | -0.5 | -1.0 | 4.5 | 4.3 |
| 4Q | 0.5 | 0.0 | 0.5 | -1.0 | -1.5 | 1.0 | 0.5 |
| 1Q26 | 1.0 | -0.5 | -2.0 | 0.5 | -1.0 | 3.5 | 2.0 |
| 2QE | 0.8 | -0.5 | -1.5 | 0.5 | -1.0 | 1.5 | 2.3 |
| 3QE | 0.8 | -0.5 | -1.5 | 0.5 | -1.0 | 1.5 | 2.2 |
| 4QE | 0.8 | -0.5 | -1.5 | 0.5 | -1.0 | 1.5 | 2.3 |
| 1Q27E | 1.0 | -0.5 | -1.5 | 0.5 | -1.0 | 1.5 | 2.3 |
| 2QE | 1.0 | -0.5 | -1.5 | 0.5 | -1.0 | 1.5 | 2.4 |
| 3QE | 1.0 | -0.5 | -1.5 | 0.5 | -1.0 | 1.5 | 2.4 |
| 4QE | 1.0 | -0.5 | -1.5 | 0.5 | -1.0 | 1.5 | 2.4 |
| 2025E | 1.0 | -0.5 | -1.5 | 0.5 | -1.0 | 1.5 | 2.2 |
| 2026E | 1.0 | -0.5 | -1.5 | 0.5 | -1.0 | 1.5 | 2.3 |
| 2027E | 1.0 | -0.5 | -1.5 | 0.5 | -1.0 | 1.5 | 2.4 |
The chart displays the contribution of each sector to the real GDP over time, with a separate line graph overlaying the bars for the 'Real GDP' series against the x-axis labeled with quarters from Q1 to Q4 and years from 2025E to 2027E.
</details>

Note: The annual measures are a 4Q to 4Q % change or contribution. Sources: Bureau of Economic Analysis, MS forecasts

# Key inputs from our Public Policy team for 2026-27

Ariana Salvatore, first published in Mapping the Midterms: A First Look

# 1) Divided government is likely, but don't extrapolate the implications too far

While historical precedent is strong – and polling and economic indicators point to waning support for Republican governance – prediction markets are likely underestimating the challenge that Democrats will have taking the Senate. If the election were held today, polls indicate it is very likely that control of the House of Representatives would shift to Democratic hands.

While a divided government would likely inject gridlock into budget negotiations, we are not convinced overall policy uncertainty would wane. A divided government outcome would not derail the policy variables that have introduced elevated uncertainty over the past (tariffs, immigration, and foreign policy), that remain largely under the control of the Executive Branch.

# 2) Fiscal stimulus ahead of the midterms remains unlikely

Congress put priority on funding for the Department of Homeland Security and chose not to add other fiscal spending to the bill. Although it remains feasible for Republicans to pass two budget reconciliation bills ahead of the midterms – one before the fiscal year-end in September and a second after October 1 in the new fiscal year – we think time is limited, as is the appetite for larger deficits.

Under a potential divided government in 2027, the scope for new tax cuts would be limited. The main fiscal variables under consideration will be changes to SNAP/Medicaid cuts in the OBBBA and the potential for government shutdowns. We expect potential differences in other policy areas (deregulation, AI, housing) would have limited macro effects through our forecast horizon. In a unified Republican Congress, we expect SNAP and Medicaid cuts would ensue as written in the bill. In a scenario of a Democratic sweep of the House and Senate, we would see upside risk to our growth forecasts if cuts to transfer payments were rolled back, while prolonged shutdowns under a more narrow Democratic House win could weigh on growth.

# 3) Don't look now, but tariffs are coming back

The Trump administration began trade reviews under Sections 232 and 301 following the Supreme Court ruling that the IEEPA tariffs were improper. These reviews should be completed in May and June ahead of the July 24 deadline when the 10% across-the-board tariffs under Section 122 expire. We do not expect a forceful push on tariffs ahead of the midterms, particularly given recent moves in gasoline prices, but tariff authority under Sections 232 and 301 is strong and tariff policy uncertainty may re-assert itself.

# 4) The July USMCA review deadline in pending. We do not expect big changes

The closer we get to the mid-2026 deadline for the USMCA review, the more challenging we expect it will be to add new sUBStantial chapters to the existing agreement. We are constructive overall in the longer term on trade alignment between the US, Mexico, and Canada, but see limited progress in sUBStantially expanding the agreement ahead of the July deadline. While it'

[中间内容因长度限制已省略]

cepts responsibility for its contents; in Korea by MS & Co International plc, Seoul Branch; in India by MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi

Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the United States by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

© 2026 MS
"""
