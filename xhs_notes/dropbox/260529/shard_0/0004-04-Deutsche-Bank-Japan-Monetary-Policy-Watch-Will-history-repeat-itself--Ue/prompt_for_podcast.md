你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
Japan Japan

# Economics Japan Monetary Policy Watch

Date 27 May 2026

# Will history repeat itself? Ueda's speech and the policy outlook

# Introduction: Upward price pressures are comparable to past oil shocks

In his opening remarks at an international conference on May 27, BoJ Governor Ueda analyzed Japan's experience with major oil price shocks over the past 50 years and the corresponding reactions of inflation and monetary policy. The Governor concluded that even for shocks of the same magnitude, the outcome can differ greatly depending on the "initial conditions" of the economy.

This speech is highly insightful for understanding the current state of Japan's economy. Tensions in the Middle East since March have caused a sharp rise in crude oil prices. In response, Japan's Corporate Goods Price Index (CGPI) for April rose by 2.3% MoM, the highest increase since 1980 during the second oil shock, excluding periods of consumption tax hikes (Figure 1). Notably, chemical product prices saw their steepest rise since the first oil shock in 1973, indicating that upstream price pressures are now at levels comparable to past oil shocks.

Kentaro Koyama, Ph.D.

Chief Economist

+81-3-6730-0683

Figure 1: MoM changes in domestic corporate goods price index   
![](images/a3fccc73dbc10253e813593094f04a323041f0064954ddb483fb282101ab70c3.jpg)

<details>
<summary>line</summary>

| Year | Total (%) |
| ---- | --------- |
| 1970 | 0         |
| 1975 | 7         |
| 1980 | 3         |
| 1985 | 0         |
| 1990 | 0         |
| 1995 | 0         |
| 2000 | 0         |
| 2005 | 0         |
| 2010 | -2        |
| 2015 | 0         |
| 2020 | 0         |
| 2025 | 2         |
</details>

![](images/f7e1f0eba069f3d81ff2785ca6f00485f8e3cdbd1496634d2d0634e1fe61ce80.jpg)

<details>
<summary>line</summary>

| Year | Plastic (%) |
| ---- | ----------- |
| 1970 | 0           |
| 1975 | 25          |
| 1980 | 0           |
| 1985 | 0           |
| 1990 | 0           |
| 1995 | 0           |
| 2000 | 0           |
| 2005 | 0           |
| 2010 | 0           |
| 2015 | 0           |
| 2020 | 0           |
| 2025 | 0           |
</details>

![](images/b6a83ff3e5e4293ac294de8fe51701d837a9317523d903db35ee411203e6c2de.jpg)

<details>
<summary>line</summary>

| Year | Chemical (%) |
| ---- | ------------ |
| 1970 | 0            |
| 1975 | 16           |
| 1980 | 3            |
| 1985 | 0            |
| 1990 | 0            |
| 1995 | 0            |
| 2000 | 0            |
| 2005 | 0            |
| 2010 | -5           |
| 2015 | 0            |
| 2020 | -5           |
| 2025 | 5            |
</details>

![](images/119d52d9a39feb34523ec1668422b278d4581012c568d02aed1cef62efca1f8c.jpg)

<details>
<summary>line</summary>

Petroleum and coal
| Year | Value (%) |
|---|---|
| 1970 | ~0 |
| 1971 | ~0 |
| 1972 | ~0 |
| 1973 | ~0 |
| 1974 | ~0 |
| 1975 | ~22 |
| 1976 | ~0 |
| 1977 | ~0 |
| 1978 | ~0 |
| 1979 | ~0 |
| 1980 | ~0 |
| 1981 | ~0 |
| 1982 | ~0 |
| 1983 | ~0 |
| 1984 | ~0 |
| 1985 | ~0 |
| 1986 | ~-5 |
| 1987 | ~-5 |
| 1988 | ~-5 |
| 1989 | ~-5 |
| 1990 | ~0 |
| 1991 | ~0 |
| 1992 | ~0 |
| 1993 | ~0 |
| 1994 | ~0 |
| 1995 | ~0 |
| 1996 | ~0 |
| 1997 | ~0 |
| 1998 | ~0 |
| 1999 | ~0 |
| 2000 | ~0 |
| 2001 | ~0 |
| 2002 | ~0 |
| 2003 | ~0 |
| 2004 | ~0 |
| 2005 | ~0 |
| 2006 | ~0 |
| 2007 | ~0 |
| 2008 | ~0 |
| 2009 | ~-20 |
| 2010 | ~0 |
| 2011 | ~0 |
| 2012 | ~0 |
| 2013 | ~0 |
| 2014 | ~0 |
| 2015 | ~0 |
| 2016 | ~0 |
| 2017 | ~0 |
| 2018 | ~0 |
| 2019 | ~0 |
| 2020 | ~-25 |
| 2021 | ~-5 |
| 2022 | ~-5 |
| 2023 | ~-5 |
| 2024 | ~-5 |
| 2025 | ~-5 |
</details>

Note: Excluding consumption tax. Source: BoJ, Deutsche Securities

As Governor Ueda pointed out, revisiting past experiences serves as a vital compass for forecasting the BoJ's future monetary policy. By delving deeper into the Governor's speech, we will clarify the differences in initial conditions between the two past oil shocks and the present, and consider the implications for monetary policy.

# Analytical framework: The six "initial conditions" highlighted by Governor Ueda

In his speech, the Governor identified the following six key initial conditions that influence inflation dynamics:

1. Wage dynamics and labor supply/demand   
2. Inflation expectations   
3. Price and wage-setting norms   
4. The exchange rate   
5. Economic momentum (demand-side conditions) pre-shock   
6. The monetary policy stance

In this report, we will focus on "wage dynamics" and the "monetary policy stance," which are particularly important and can be analyzed quantitatively, to conduct a comparative analysis with past episodes.

# Deep dive (1): Will a wage-price spiral occur?

Past experience: Unit labor costs made all the difference Comparing the first oil shock in 1973 and the second in 1980, the pace of import price increases was similar, yet there was a significant difference in the resulting CPI inflation rates (Figure 2).

Figure 2: Inflation rates during the previous oil shocks   
![](images/35a3ab5ef9d5e8ec611ec1594b2d7739c3e2dc6be982fa097c0d19d46ebe5a95.jpg)

<details>
<summary>line</summary>

| Year | Core-core CPI YoY inflation (LHS) (%) | Import price YoY inflation (RHS) (%) |
|------|----------------------------------------|---------------------------------------|
| 1970 | ~6                                     | ~0                                    |
| 1975 | ~23                                    | ~18                                   |
| 1980 | ~3                                     | ~22                                   |
| 1985 | ~1                                     | ~-12                                  |
| 1990 | ~2                                     | ~3                                    |
| 1995 | ~1                                     | ~0                                    |
| 2000 | ~0                                     | ~0                                    |
| 2005 | ~0                                     | ~5                                    |
| 2010 | ~-1                                    | ~-30                                  |
| 2015 | ~0                                     | ~0                                    |
| 2020 | ~0                                     | ~-20                                  |
| 2025 | ~3                                     | ~5                                    |
</details>

Note: Core-core inflation rate excludes consumption tax effects  
Source: Haver Analytics, Deutsche Securities

During the first oil shock in 1973, which triggered a wage-price spiral, Japan's economy was already in a high-pressure state. Amid chronic labor shortages, nominal wages were growing at +15-20% YoY even before the shock (Figure 3). The surge in oil prices further accelerated wage growth to 30% at its peak, leading to a classic spiral.

Figure 3: Wage growth during the previous oil shocks   
![](images/3f40cc1037e6b4dd38da9c115f0e63584f46e7b6afbfd4fcffee18e207c3976f.jpg)  
Source: Haver Analytics, Deutsche Securities

In contrast, during the second oil shock in 1980, when inflation was successfully contained, wage growth was restrained through labor-management coordination, based on the painful lessons from the first shock. Real wages decelerated in response to accelerating inflation, and a spiral was averted.

This difference becomes clearer when looking at Unit Labor Costs (ULC), defined as nominal employee compensation divided by real GDP, which indicates corporate labor cost pressure (Figure 4). The sharp rise in ULC growth during the first shock, versus its limited increase during the second, contributed significantly to price stability.

Figure 4: Unit labor costs (ULC) during the previous oil shocks   
![](images/7f65526e67510a5702fff7fac2a1e1fcb3ba05b48bde8a4f0e1e43376835d115.jpg)

<details>
<summary>line</summary>

| Year | YoY (%) |
|------|---------|
| 1965 | ~12     |
| 1970 | ~16     |
| 1975 | ~31     |
| 1980 | ~6      |
| 1985 | ~2      |
| 1990 | ~4      |
| 1995 | ~2      |
| 2000 | ~-2     |
| 2005 | ~-4     |
| 2010 | ~-6     |
| 2015 | ~2      |
| 2020 | ~8      |
| 2025 | ~3      |
</details>

Source: Haver Analytics, Deutsche Securities

Current assessment: Low short-term risk, but next year's wage negotiations are key Current ULC growth is at a higher level than it was just before the second oil shock in 1979. Furthermore, the employment conditions DI in the BoJ Tankan survey is lower than during past oil shocks, indicating that labor shortages are more severe now (Figure 5). Whether the current inflation proves to be temporary or persistent depends on whether this ULC growth accelerates further.

Figure 5: BoJ Tankan: Employment condition DI (all industries)   
![](images/c0320466e1a79d964162036f64bb9468821bd501de82f0abb154b5a6e981f63d.jpg)

<details>
<summary>line</summary>

| Year | Value |
| ---- | ----- |
| 1974 | -25   |
| 1978 | 25    |
| 1982 | 10    |
| 1986 | 10    |
| 1990 | -45   |
| 1994 | 15    |
| 1998 | 25    |
| 2002 | 20    |
| 2006 | -10   |
| 2010 | 25    |
| 2014 | -15   |
| 2018 | -35   |
| 2022 | -5    |
| 2026 | -40   |
</details>

Source: BoJ, Deutsche Securities

In this regard, since the crude oil price surge occurred after the 2026 "Shunto" spring wage negotiations were largely concluded for major corporations, a significant reflection of the price hikes in scheduled cash earnings (base salary) will likely be deferred until next year. Moreover, surveys indicate that summer bonus growth will be lower than last year. Thus, the probability of a sharp near-term increase in ULC is low.

In conclusion, the risk of a wage-price spiral in the short term is limited. However, against a backdrop of historic labor shortages, if this year's high inflation translates into strong wage demands in the 2027 Shunto, a scenario of relatively high inflation persisting for a longer period is entirely plausible.

# Deep dive (2): Is the monetary policy stance appropriate?

Past experience: Accommodative policy that fueled inflation vs. tightening that curbed it During the first oil shock, monetary policy was accommodative both before and after the shock. A comparison of the policy rate with a proxy for the nominal neutral rate of interest (using a 4-year moving average of nominal GDP growth) shows that the policy rate was consistently below the neutral rate throughout the 1970s (Figure 6). As the Governor himself mentioned in his speech, "the degree of tightening was clearly inadequate," and monetary policy undeniably contributed to the inflation.

Figure 6: Policy rates during the oil shocks   
![](images/1523011c6e8fae7308d2e49032015ec517ad8fb14decb222c3e53a41b785a361.jpg)

<details>
<summary>line</summary>

| Year | Nominal growth (4-year average) | Policy rate |
|------|----------------------------------|-------------|
| 1965 | ~10.5%                           | ~5.5%       |
| 1970 | ~13.5%                           | ~6.0%       |
| 1975 | ~14.0%                           | ~9.0%       |
| 1980 | ~7.0%                            | ~9.0%       |
| 1985 | ~4.5%                            | ~5.0%       |
| 1990 | ~5.5%                            | ~6.0%       |
| 1995 | ~1.0%                            | ~1.0%       |
| 2000 | ~-1.0%                           | ~0.0%       |
| 2005 | ~0.5%                            | ~0.0%       |
| 2010 | ~-2.5%                           | ~0.0%       |
| 2015 | ~2.5%                            | ~0.0%       |
| 2020 | ~-1.5%                           | ~0.0%       |
| 2025 | ~3.0%                            | ~1.0%       |
</details>

Source: Haver Analytics, Deutsche Securities

In contrast, after the second oil shock from 1980 onwards, the policy rate was raised above the rate of nominal growth, which is considered to have exerted downward pressure on inflation.

Current assessment: Unprecedented accommodation, risk of delay Measuring the degree of monetary accommodation by the gap between the nominal growth and policy rate, we find that even after the initiation of rate hikes since 2024, the current degree of accommodation is at its highest level since 1980 (Figure 7).

Figure 7: Degree of monetary accommodation (nominal growth rate - policy interest rate)   
![](images/0c2a29c5f4531e39d6f3968844e8557ce627e1c4e001b8473debb2631225cf5f.jpg)

<details>
<summary>line</summary>

| Year | Value (%) |
|------|-----------|
| 1965 | 4.5       |
| 1970 | 7.5       |
| 1975 | 3.0       |
| 1980 | -2.5      |
| 1985 | -1.0      |
| 1990 | 2.0       |
| 1995 | -1.5      |
| 2000 | 0.5       |
| 2005 | 0.0       |
| 2010 | -2.0      |
| 2015 | 2.5       |
| 2020 | -1.0      |
| 2025 | 2.0       |
</details>

Source: Haver Analytics, Deutsche Securities

In the near future, nominal growth may temporarily slow as deteriorating terms of trade squeeze the economy. However, if this transitions into an "homemade inflation" accompanied by wage growth, nominal growth will likely re-accelerate. In such a scenario, a delay in monetary policy normalization would significantly increase the risk of accelerating inflation.

# Conclusion: Greater vigilance is needed than during the second oil shock

A comprehensive comparison of the initial conditions, as mentioned by Governor Ueda, reveals that the current situation is vastly different from the one preceding the first oil shock (Figure 8). However, the story changes when we compare it to the second oil shock, during which inflation was (relatively) successfully contained.

Figure 8: Assessment of the initial conditions pointed out by Governor Ueda in his speech 

<table><tr><td>Initial Conditions</td><td>Pre-1st Oil Shock (around 1973)</td><td>Pre-2nd Oil Shock (around 1979)</td><td>Present</td></tr><tr><td>Wage dynamics and labor supply/demand</td><td>Wage growth had reached nearly 20% and was already accelerating.</td><td>Wage developments were subdued.</td><td>Wages have started to rise, but not with the same momentum as in the 1970s. The labor market is tighter than in the 1970s.</td></tr><tr><td>Inflation expectations</td><td>Not mentioned, but likely already high.</td><td>Subdued due to the lessons from the 1st Oil Shock.</td><td>Has shifted upward from near zero to the 1.5-2% range, but it is uncertain if this is firmly anchored.</td></tr><tr><td>Price and wage-setting norms</td><td>An inflationary norm had been established.</td><td>A cautious view on inflation was entrenched due to the experience of the 1st Oil Shock.</td><td>The long-standing deflationary norm has begun to change, but it is uncertain if a new norm is in place.</td></tr><tr><td>Exchange rate</td><td>A slightly depreciating trend.</td><td>The yen had appreciated significantly.</td><td>A slightly depreciating trend.</td></tr><tr><td>Economic momentum</td><td>The economy was overheating, with inflation already approaching 10%.</td><td>Inflation was stable at around 3%.</td><td>The output gap is positive, and the inflation rate is around 2%, excluding institutional factors.</td></tr><tr><td>Monetary policy stance</td><td>Was highly accommodative.</td><td>The degree of accommodation was being reduced, but it was still accommodative.</td><td>In the process of policy normalization, but still accommodative.</td></tr></table>

Note: Orange indicates inflationary, yellow indicates moderately inflationary, and blue indicates deflationary. Source: Deutsche Securities

While yen appreciation acted as a buffer against inflation then, a weakening yen is now a headwind. Upward pressure on ULC is also higher than at that time. Furthermore, the monetary policy stance is accommodative, similar to that period. Taking these factors into account, we can assess that Japan's current economy is in a more inflationary (pro-inflationary) environment than it was during the second oil shock.

The Governor cited "prompt monetary policy response" as a key factor in the success of the second episode. Reflecting on the current situation, we believe the BoJ is now required to act with similar timeliness, carefully assessing the data but without missing the opportune moment.

# Appendix 1

# Important Disclosures

\*Other information available upon request

\*Prices are current as of the end of the previous trading session unless otherwise indicated and are sourced from local exchanges via Reuters, Bloomberg and other vendors. Other information is sourced from DB, subject companies, and other sources. For further information regarding disclosures relevant to DB, please visit our global disclosure look-up page on our website at https://research.db.com/Research/Disclosures/FICCDisclosures. Aside from within this report, important risk and conflict disclosures can also be found at https://research.db.com/Research/Disclosures/Disclaimer. Investors are strongly encouraged to review this information before investing.

# Analyst Certification

The views expressed in this report accurately reflect the personal views of the undersigned lead analyst(s). In addition, the undersigned lead analyst(s) has not and will not receive any compensation for providing a specific recommendation or view in this report. Kentaro Koyama.

# Additional Information

The information and opinions in this report were prepared by DB AG or one of its affiliates (collectively 'DB'). Though the information herein is believed to be reliable and has been obtained from public sources believed to be reliable, DB makes no representation as to its accuracy or completeness. Hyperlinks to third-party websites in this report are provided for reader convenience only. DB neither endorses the content nor is responsible for the accuracy or security controls of those websites.

If you use the services of DB in connection with a purchase or sale of a security that is discussed in this report, or is included or discussed in another communication (oral or written) from a DB analyst, DB may act as principal for its own account or as agent for another person.

DB may consider this report in deciding to trade as principal. It may also engage in transactions, for its own account or with customers, in a manner inconsistent with the views taken in this research report. Others within DB, including strategists, sales staff and other analysts, may take views that are inconsistent with those taken in this research report. DB issues a variety of research products, including fundamental analysis, equity-linked analysis, quantitative analysis and trade ideas. Recommendations contained in one type of communication may differ from recommendations contained in others, whether as a result of dif

[中间内容因长度限制已省略]

ysts attending site visits, conferences, social events, and the like. Similarly, without prior approval from Research Management and Anti-Bribery and Corruption ("ABC") team, analysts may not accept perks or other items of value for their personal use from issuers they cover.

Additional information relative to securities, other financial products or issuers discussed in this report is available upon request. This report may not be reproduced, distributed or published without DB's prior written consent.

Backtested, hypothetical or simulated performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG.

It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG

David Folkerts-Landau   
Group Chief Economist and Global Head of Research 

<table><tr><td>Pam Finelli
Global Chief Operating Officer Research</td><td>Steve Pollard
Global Head of Company Research and Sales</td><td>Jim Reid
Global Head of Macro and Thematic Research</td><td>Tim Rokossa
Head of Germany Research</td></tr><tr><td>Gerry Gallagher
Head of European Company Research</td><td>Matthew Barnard
Head of Americas Company Research</td><td>Peter Milliken
Head of APAC Company Research</td><td>Debbie Jones
Global Head of Sustainability and Data Innovation, Research</td></tr><tr><td>Sameer Goel
Global Head of EM &amp; APAC Research</td><td>Francis Yared
Global Head of Rates Research</td><td>George Saravelos
Global Head of FX Research</td><td>Peter Hooper
Vice-Chair of Research</td></tr></table>

International Production Locations 

<table><tr><td>DB AG</td><td>DB AG</td><td>DB AG</td><td>Deutsche Securities Inc.</td></tr><tr><td>DB Place</td><td>Equity Research</td><td>Filiale Hongkong</td><td>1-3-1 Azabudai</td></tr><tr><td>Level 16</td><td>Mainzer Landstrasse 11-17</td><td>International Commerce</td><td>Azabudai Hills Mori JP Tower</td></tr><tr><td>Corner of Hunter &amp; Phillip</td><td>60329 Frankfurt am Main</td><td>Centre,</td><td>Minato-ku, Tokyo 106-0041</td></tr><tr><td>Streets</td><td>Germany</td><td>1 Austin Road West,Kowloon,</td><td>Japan</td></tr><tr><td>Sydney, NSW 2000</td><td>Tel: (49) 69 910 00</td><td>Hong Kong</td><td>Tel: (81) 3 6730 1000</td></tr><tr><td>Australia</td><td></td><td>Tel: (852) 2203 8888</td><td></td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td></td><td></td></tr><tr><td>DB AG</td><td>DB Securities Inc.</td><td>DB AG</td><td></td></tr><tr><td>21 Moorfields</td><td>The DB Center</td><td>Filiale Singapur</td><td></td></tr><tr><td>London EC2Y 9DB</td><td>1 Columbus Circle</td><td>One Raffles Quay, South</td><td></td></tr><tr><td>United Kingdom</td><td>New York, NY 10019</td><td>Tower,</td><td></td></tr><tr><td>Tel: (44) 20 7545 8000</td><td>Tel: (1) 212 250 2500</td><td>Singapore 048583</td><td></td></tr><tr><td></td><td></td><td>TeL: +65 6423 8001</td><td></td></tr></table>
"""
