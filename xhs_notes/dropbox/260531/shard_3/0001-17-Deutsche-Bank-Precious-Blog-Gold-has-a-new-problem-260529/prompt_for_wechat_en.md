You are a senior financial newsletter editor with a consulting-style strategy lens. You turn research-report material into a long-form English article that is structured, insightful, and suitable for a serious business audience.

Objective:
- Write an English Markdown article based on the report parsing below.
- Target length: around 2200 words, plus or minus 15%.
- Tone: serious, analytical, strategic, and readable.
- The article should not feel like a summary. It should make an argument.
- You may extend the report's logic into reasonable second-order implications, but do not invent data, company actions, or quotes.
- Do not disclose every detail. Leave several meaningful open questions that make readers want the full report.

McKinsey-style writing principles:
1. Answer first: open with the controlling idea, not background.
2. Governing thought: every section must support the main answer.
3. Mutually exclusive, collectively exhaustive logic: avoid overlapping sections.
4. So what: every section must explain why the point matters.
5. Synthesis over summary: do not list facts; interpret what the pattern means.
6. Action titles: section headings must be complete, insight-bearing sentences. Do not use generic headings such as "Key Takeaways", "Market Background", "Core View", or "Reader Implications".
7. Natural hooks: if you want readers to join the community or read the full report, the hook should emerge from unresolved analytical questions, not from promotional language.

Required Markdown structure:
- `# Title`: make it a direct argument, not a topic label.
- Opening: 4-6 short paragraphs that state the main thesis and why now matters.
- 4-6 `##` sections. Each `##` heading must be an action title: a sentence that tells the reader the insight.
- One section should identify what the report does not fully answer yet.
- One section should translate the report into a decision framework for readers.
- Final section: naturally invite readers to join the community or read the full report using this CTA: Join the community to read the full report and review the original charts.
- End with: `*This article is for learning and discussion only and does not constitute investment advice.*`

Content boundaries:
- Do not mention specific investment bank names such as GS. Use "a global investment bank report" if needed.
- Do not use emoji.
- Do not write like a viral post.
- Do not output your reasoning process.
- Do not generate image Markdown; the system will insert original MinerU images afterward.

Report parsing:
"""
# Commodities Precious Blog

# Gold has a new problem

Gold prices have diverged from oil trends due to concerns of persistent inflation driven by a more varied set of causes, and rising real interest rates. The occurrence of bond market weakness has been a global phenomenon with key events in Japan and the UK. Watchpoints going forward will include global inflation data and upcoming Federal Reserve meetings.   
We think it would be a mistake to link gold too tightly with an extrapolation of further real rates repricing (48 bps so far this year). In 2022, we experienced a much sharper real-rate repricing of 270 bps which was effectively neutralized by a 716 tonne swing in official gold demand (H2'22 vs H2'21).   
All indications are that incoming Fed Chair Warsh may attempt to steer the center of FOMC opinion from the “somewhat hawkish” characterization seen in mid-May (Link). While the effectiveness of this remains to be seen, it could meaningfully change the pace of ETF gold investment without necessarily changing our team’s view of a Fed on an “indefinite hold near neutral.”   
Central bank and bar & coin demand were both stronger than expected in Q1, but ETF demand is down by $78\%$ versus last year's quarterly run-rate. We see upside risk to ETF demand in the balance of the year, and note that overall demand weakness in 2023 was still associated with an increase in gold prices. One bearish risk is the upside to recycled gold supply as capacity bottlenecks ease.

# Inflation and bond markets constrain gold

Gold has diverged from its negative oil correlation in the last 10 days as Brent front month dropped below USD 100/bbl (Figure 1). This has sustained a short term downtrend from the USD 4,700/oz level around mid May, and reflected in -1.6 mm troy oz selling visible in ETFs (-0.4 mm troy oz) and futures (-1.2 mm troy oz).

The most relevant macro frame for gold continues to be the risk of higher inflation, a hawkish monetary policy reaction, and the attendant rise in real interest rates. Put simply, gold's new problem lies in the combination of more persistent inflation and responsible monetary policy-making. That suggests that a breakdown in either one could tilt the macro picture for gold, suggesting gold sensitivity to policy communications and inflation data going forward.

Date 29 May 2026

Michael Hsueh
Research Analyst
+65-6423-7510

Figure 1: Gold diverging from oil   
![](images/abb39f34a066346640ca4ecfb10f1d1e97d7954d324f3f3a961fb6c220af6f56.jpg)

<details>
<summary>line</summary>

| Date       | Gold (lhs USD/oz) | Brent M1 (rhs USD/bbl) |
| ---------- | ----------------- | ---------------------- |
| 3/19/2026  | -                 | -                      |
| 3/18/2026  | -                 | -                      |
| 19/5/2026  | -                 | -                      |
</details>

Source: Bloomberg Finance LP, DB

Figure 2: 10y US Treasury nominal yield more closely related to Dec'26 Brent than front month (where coefficient of determination is 0.51)   
![](images/34a16f2ec0aa08284a4df826526c2913e856133ac3d3686674bfd1ad8aae8ece.jpg)

<details>
<summary>scatter</summary>

| Dec'26 Brent | US 10y yield |
| ------------ | ------------ |
| 100          | 102          |
| 105          | 104          |
| 110          | 106          |
| 115          | 108          |
| 120          | 110          |
| 125          | 112          |
| 130          | 114          |
| 135          | 116          |
| 140          | 118          |
</details>

Source: Bloomberg Finance LP, DB

Two simple charts illustrate this. First, US 10y nominal and real rates have been more closely related to deferred crude futures (e.g., Dec'26) than front month (Figure 2), with the deferred crude futures $\mathsf{R}^2$ being $77\%$ and the front month $\mathsf{R}^2$ being $51\%$ . That suggests the market is more attuned to the possibility of a longer period of higher energy prices than the short term picture. Second, 10y real yields have been linked to hawkish Fed re-pricing (Figure 3), which provides the transmission channel into financial fair value for gold that takes the 10y real yield as an input (Link).

Figure 3: 10y real rates have followed Dec Fed pricing   
![](images/4e03d9ccc39a305c9da14fd8f93387b256baf5e88042e0b7d0b11c3a9f9538a2.jpg)

<details>
<summary>line</summary>

| Date       | Real 10y yield (lhs) | Fed Dec'26 pricing |
| ---------- | -------------------- | ------------------ |
| 19/5/2026  | 2.2                  | 3.9                |
</details>

Source: Bloomberg Finance LP, DB

Figure 4: Gold Dec'26 and Fed Dec'26   
![](images/c3ec310dc076347689c5337d7cf60cfbce97a5945bb8de671f1917b678bc7c76.jpg)

<details>
<summary>line</summary>

| Date     | Fed Dec'26 pricing | GCZ6  |
| -------- | ------------------ | ----- |
| 27-Feb   | 3.0                | 3.2   |
| 13-Mar   | 3.4                | 3.4   |
| 27-Mar   | 3.8                | 4.4   |
| 10-Apr   | 3.6                | 4.8   |
| 24-Apr   | 3.5                | 4.8   |
| 08-May   | 3.7                | 4.8   |
| 22-May   | 3.8                | 4.6   |
</details>

Source: Bloomberg Finance LP, DB

# Bond market sell-off is a global phenomenon

The sell-off in bond markets since the upside break of $4.5\%$ on 10y UST was important enough to rank as a point of discussion at the meeting of G-7 finance ministers in Paris (18-19 May). According to Japan's finance minister Katayama, there has been a compounding effect amongst the three major markets of the US, UK and Japan $^{1}$ which facilitated weekly moves of 21 bps, 24 bps and 23 bps respectively in that week. This reflects the fact that these are global bond market moves, not exclusively borne of any one country's idiosyncrasies.

From the Japanese side, bond market concerns centered on the need for a supplementary budget, including government subsidies for energy, following "repeated denials that an extra budget was necessary". $^{2}$ Significant moderating influences came from a strong 20yr JGB auction (19-May), Prime Minister Takaichi's indication that with the extra budget, Japan does not "necessarily need to issue a large amount of government bonds," (20-May) $^{3}$ and the announcement from the CEO that Japan Post Bank would continue to rebuild its JGB holdings, depending on "the relative appeal of other assets." $^{4}$

From the UK side, recent difficulty for the Gilt market dates from the early May local elections seeing Labour party losses, the possibility of a leadership challenge for Prime Minister Starmer, and that a new leader may introduce fiscal easing and higher debt issuance. $^{5}$ This narrative was extended by data showing April's UK government deficit was larger than expected. $^{6}$

From the US side, our Rates strategists express concern that “a string of shocks have left real rates too low to return inflation to 2%” (Link), while staying short 10y UST and seeing upside to their yield forecast (Link). They remain short UST 10y with upside risk to their 4.65% target, and would not be surprised by a 10y term premium of 135 bps, implying risk of 10y UST at 5% (Link).

Our US Econ team observes that for the Fed, the “balance of risks appears to have shifted toward inflation persistence” (Link). Upside inflation drivers are wider than oil prices alone, including measures of trend inflation, an elevated output gap, AI demand in some goods categories, PPI pipeline inflation, and shorter-run inflation expectations (Link). Our team’s relative CPI forecasts indicate greater upside for the US short-end (Link), implying that the lack of market pricing for Fed hikes may be at risk of turning higher rather than lower.

# What to watch for: Potential Warsh positives

The near-term difficulty for gold may be that as the US-Iran war draws to a close and the Strait of Hormuz gradually sees an increasing rate of commercial traffic, sources of inflation that outlive the conflict may keep real rates elevated. However, we think it would be a mistake to link gold too tightly with an extrapolation of further real rates repricing (48 bps so far this year). In 2022, we experienced a much sharper real-rate repricing of 270 bps which was effectively neutralized by a 716 tonne swing in official gold demand (H2'22 vs H2'21).

If the above macro framing is correct, then important watchpoints going forward will include global inflation data with emphasis on the US, and the first Fed meeting chaired by Kevin Warsh (17-18 June). If Warsh is able to visibly steer the center of Committee opinion from the “somewhat hawkish” characterization in mid-May (Link), then this could prove gold-positive. This could move rates pricing without necessarily any change in our team’s view of a Fed on “indefinite hold near neutral” (Link). That could in turn meaningfully change the pace of ETF gold investment which has flagged from 2025 (see below).

Last November, Warsh indicated in his WSJ op-ed that the Fed should discard its forecast of stagflation, that AI will be a significant disinflationary force owing to its positive impact on productivity, and that a reduced Fed balance sheet can be accompanied by lower policy rates. $^{7}$ To some extent the Fed's forecast of stagflation has already changed, with the Fed's SEP on growth higher by 40-60 bps over the 2026-27 timeframe, although it is also higher on PCE by 10 bps (Mar'26 vs Sep'25 SEP).

Conditional on a US-Iran peace deal, our US Econ team believes Warsh will reinforce the inclination to “look-through” near-term core inflation pressures (Link). That would defy both market pricing (58% chance of Fed hike by Dec), evidence that AI is inflationary in some categories (Link), and evidence that layoffs are not associated with AI adoption rates and US firms are not using AI as a substitute for employment but rather to “supplement or enhance” employees (Link).

An inclination to look through near term inflation would contrast with the Fed officials dissenting from the easing bias in the April statement, St Louis Fed President Musalem who cautioned that Fed policy is below neutral, and that the US is unlikely to be in a high productivity growth period. $^{8}$ It would also contrast with ECB April minutes indicating that "it had become increasingly unlikely that a 'looking through' approach without any monetary policy action would be appropriate." $^{9}$

# Gold demand shaping up to be weaker year on year

From a gold supply-demand perspective, central bank demand surpassed our estimates in Q1 based on China other investment demand (Link). We also note that Q1 bar & coin demand is $+38\%$ above last year's run-rate. This supports an important piece of the narrative where we see inelastic demand stealing supply away from elastic sources of demand (Link). However, the contraction in ETF demand year on year is the most significant change in this dynamic. Despite offsetting strength in central bank and bar & coin demand in the first quarter, we would still likely need to see some resumption of ETF demand (62 tonnes in Q1) in order to realise our full year assumption around 450 tonnes (Figure 5). This does not necessarily equate to lower year-on-year gold prices, however, as the similarly weak year of 2023 still saw gold prices rise modestly.

Among supply developments, we think the pace of recycled gold is likely to be the most important swing factor, since it can respond more quickly than mined production. The factors weighing on recycled supply in recent years have been extrapolative price expectations, and a relative lack of household financial stress as compared to the peak 4 consecutive years of gold recycling following the global financial crisis in 2009-2012. Modestly higher recycling volume in Q1 could accelerate over the balance of the year as bottlenecks in refining and recycling capacity ease over time, according to the World Gold Council, while distress selling may be driven by weaker domestic currencies in some markets. That would suggest upside risk to our recycled gold supply assumption of 1,470 tonnes versus 366 tonnes estimated in the first quarter (Figure 6).

Figure 5: Gold demand weaker in key categories   
![](images/4697a23c1b620335cc035ebbae4d0c1aed67df83414bfb4f59d0e0866e5fa2ec.jpg)

<details>
<summary>bar</summary>

| Year | Central banks & other inst. | ETFs & similar products | Total bar and coin | Technology | Jewellery fabrication | Annual net chg (tonnes) |
|------|-----------------------------|--------------------------|--------------------|------------|------------------------|-------------------------|
| 2022 | 800                         | 50                       | -100               | -50        | -50                    | 700                     |
| 2023 | -100                        | -100                     | -100               | -100       | -100                   | -300                    |
| 2024 | 0                           | 250                      | -150               | 0          | -150                   | 100                     |
| 2025 | -400                        | 750                      | 150                | 100        | 350                    | 450                     |
| 2026 | 250                         | -450                     | 150                | -150       | 250                    | -300                    |
</details>

Source: World Gold Council, DB

Figure 6: Recycled gold in Q1 of 366 tonnes supports full year assumption   
![](images/3670db6aa3ca1787dd6125159b89dc244f907d78c355d6595677eedd649278d2.jpg)

<details>
<summary>scatter</summary>

| Real gold price chg | Recycled gold |
| ------------------- | ------------- |
| -10%                | 1150          |
| -5%                 | 1180          |
| 0%                  | 1120          |
| 5%                  | 1250          |
| 10%                 | 1280          |
| 20%                 | 1380          |
| 25%                 | 1650          |
| 30%                 | 1480          |
| 40%                 | 1400          |
| 45%                 | 1470          |
</details>

Source: World Gold Council, DB

# Appendix 1

# Analyst Certification

The views expressed in this report accurately reflect the personal views of the undersigned lead analyst(s). In addition, the undersigned lead analyst(s) has not and will not receive any compensation for providing a specific recommendation or view in this report. Michael Hsueh.

# Important Disclosures

Prices are current as of the end of the previous trading session unless otherwise indicated and are sourced from local exchanges via Reuters, Bloomberg and other vendors. Other information is sourced from DB, subject companies, and other sources. For further information regarding disclosures relevant to DB, please visit our global disclosure look-up page on our website at

https://research.db.com/Research/Disclosures/FICCDisclosures. Aside from within this report, important risk and conflict disclosures can also be found at https://research.db.com/Research/Disclosures/Disclaimer. Investors are strongly encouraged to review this information before investing.

# Additional Information

The information and opinions in this report were prepared by DB AG or one of its affiliates (collectively 'DB'). Though the information herein is believed to be reliable and has been obtained from public sources believed to be reliable, DB makes no representation as to its accuracy or completeness. Hyperlinks to third-party websites in this report are provided for reader convenience only. DB neither endorses the content nor is responsible for the accuracy or security controls of those websites.

If you use the services of DB in connection with a purchase or sale of a security that is discussed in this report, or is included or discussed in another communication (oral or written) from a DB analyst, DB may act as principal for its own account or as agent for another person.

DB may consider this report in deciding to trade as principal. It may also engage in transactions, for its own account or with customers, in a manner inconsistent with the views taken in this research report. Others within DB, including strategists, sales staff and other analysts, may take views that are inconsistent with those taken in this research report. DB issues a variety of research products, including fundamental analysis, equity-linked analysis, quantitative analysis and trade ideas. Recommendations contained in one type of communication may differ from recommendations contained in others, whether as a result of differing time horizons, methodologies, perspectives or otherwise. DB and/or its affiliates may also be holding debt or equity securities of the issuers it writes on. Analysts are paid in part based on the profitability of DB AG and its affiliates, which includes investment banking, trading and principal trading revenues.

Opinions, estimates and projections constitute the current judgment of the author as of the date of this report. They do not necessarily reflect the opinions of DB and are subject to change without notice. DB provides liquidity for buyers and sellers of securities issued by the companies it covers. DB analysts sometimes have shorter-term trade ideas that may be inconsistent with DB's existing longer-term ratings. Some trade ideas for equities are listed as Catalyst Calls on the Research Website (https://research.db.com/Research/), and can be found on the general coverage list and also on the covered company's page. A Catalyst Call represents a high-conviction belief by an analyst that a stock will outperform or underperform the market and/or a specified sector over a time frame of no less than two weeks and no more than three months. In addition to Catalyst Calls, analysts may occasionally discuss with our clients, and with DB salespersons and traders, trading strategies or ideas that reference catalysts or events that may have a near-term or medium-term impact on the market price of the securities discussed in this report, which impact may be directionally counter to the analysts' current 12-month view of total return or investment return as described herein. DB has no obligation to update, modify or amend this report or to otherwise notify a recipient thereof if an opinion, forecast or estimate changes or becomes inaccurate. Coverage and the fr

[中间内容因长度限制已省略]

company-sourced material in the report, and/or site-visit attendance. Without prior approval from Research Management, analysts may not accept from current or potential Banking clients the costs of travel, accommodations, or other expenses incurred by analysts attending site visits, conferences, social events, and the like. Similarly, without prior approval from Research Management and Anti-Bribery and Corruption ("ABC") team, analysts may not accept perks or other items of value for their personal use from issuers they cover.

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

<table><tr><td>DB AG</td><td>DB AG</td><td>DB AG</td><td>Deutsche Securities Inc.</td></tr><tr><td>DB Place</td><td>Equity Research</td><td>Filiale Hongkong</td><td>1-3-1 Azabudai</td></tr><tr><td>Level 16</td><td>Mainzer Landstrasse 11-17</td><td>International Commerce Centre</td><td>Azabudai Hills Mori JP Tower</td></tr><tr><td>Corner of Hunter &amp; Phillip Streets</td><td>60329 Frankfurt am Main Germany</td><td>1 Austin Road West, Kowloon,</td><td>Minato-ku, Tokyo 106-0041</td></tr><tr><td>Sydney, NSW 2000 Australia</td><td>Tel: (49) 69 910 00</td><td>Hong Kong</td><td>Japan</td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td>Tel: (852) 2203 8888</td><td>Tel: (81) 3 6730 1000</td></tr><tr><td>DB AG</td><td>DB Securities Inc.</td><td>DB AG</td><td></td></tr><tr><td>21 Moorfields London EC2Y 9DB United Kingdom Tel: (44) 20 7545 8000</td><td>The DB Center 1 Columbus Circle New York, NY 10019 Tel: (1) 212 250 2500</td><td>Filiale Singapur One Raffles Quay, South Tower Singapore 048583 Tel: (65) 6423 8001</td><td></td></tr></table>
"""
