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
# EUROPEAN ECONOMICS ANALYST

# Rockets and Feathers: Asymmetric Passthrough from Energy Shocks

Studies show that energy price shocks tend to pass through to underlying inflation asymmetrically: rising energy prices push core inflation up much more than falling prices pull it down. This “rocket and feather” pattern matters for the ECB because it implies that renewed increases in energy prices could create persistent inflation pressure, while a decline in energy prices may offer only limited relief.

Research highlights three main reasons for this asymmetry: firms protect margins more aggressively when costs rise than when they fall (given the possibility of bankruptcy), the “menu” cost of lowering prices tends to be higher with positive trend inflation, and wages and prices are sticky on the downside. Together, these mechanisms help explain why inflation can become more persistent after an energy spike than after an equivalent decline.

We provide fresh statistical evidence on this uneven passthrough behaviour in the Euro area. We start with a simple top-down perspective using quarterly data from 1999-2025. We confirm that positive food and energy price shocks have significant passthrough effects into core inflation, while the passthrough of negative non-core shocks is small and insignificant.

We show that this finding is robust to considering a broader set of data. First, we estimate a panel version of the top-down model, which utilises the cross-country variation in energy shocks to provide more statistical information. Second, we create a sectoral panel model of firm pricing intentions using the European Commission business survey.

For the outlook, asymmetric passthrough skews risks to the upside for core inflation because further energy price increases would pass through more forcefully than declines. Uneven passthrough could also raise the chance of ECB tightening by lowering the odds that a sudden drop in energy prices improves the inflation outlook materially and by strengthening the case for risk management hikes. Our analysis thus supports our recent upgrade to core inflation (which we now see peaking at $2.7\%$ ) and our baseline forecast for two ECB hikes (June and September).

# Sven Jari Stehn

+44(20)7774-8061 | jari.stehn@gs.com

GS International

# Alexandre Stott

+33(1)4212-1108

alexandre.stott@gs.com

GS Bank Europe SE - Paris

Branch

# Rockets and Feathers: Asymmetric Passthrough from Energy Shocks

ECB officials are focused on passthrough effects from higher energy prices into underlying inflation, via indirect effects (through supply chains) and second-round effects (through wage bargaining). Our previous work shows that the likelihood of such passthrough depends importantly on the size of the shock, with larger energy price increases more likely to lead to persistent inflationary pressures.

Past energy shocks also point to a potential asymmetry in the transmission of energy shocks. In particular, energy price increases tend to have stronger effects for underlying inflation than energy price declines. This asymmetry is often called “rocket and feather” pricing.

Given the ongoing uncertainty around energy prices, such asymmetries in passthrough could have important implications for the inflation and policy outlook.

# Existing Evidence on Asymmetric Passthrough

Several studies point to asymmetric transmission from energy prices to inflation.

The IMF, for example, has documented uneven passthrough from headline inflation shocks to core inflation in the Euro area, with positive food and energy inflation shocks displaying a strong increasing relation with core inflation, whereas negative headline shocks have an insignificant relationship with core inflation (Exhibit 1, left).

Exhibit 1: Previous Studies Point to Uneven Passthrough of Energy Shocks   
![](images/c36fe5c728610ff20d5e77b646f16bde7dda0f58fdac223eb585e08b1152c688.jpg)

<details>
<summary>line</summary>

| Shock to Headline Inflation (pp, 12-month average) | Point Estimate | 95% Confidence Interval Lower Bound | 95% Confidence Interval Upper Bound |
| -------------------------------------------------- | -------------- | ------------------------------------- | ------------------------------------- |
| -2                                                 | -0.5           | -1.0                                  | -0.2                                  |
| -1                                                 | -0.3           | -0.8                                  | -0.1                                  |
| 0                                                  | 0.0            | 0.0                                   | 0.0                                   |
| 1                                                  | 1.0            | 0.8                                   | 1.2                                   |
| 2                                                  | 2.5            | 2.0                                   | 3.0                                   |
| 3                                                  | 4.0            | 3.5                                   | 5.0                                   |
| 4                                                  | 5.5            | 5.0                                   | 6.5                                   |
</details>

![](images/e1e974603f20e086bd958f55f1c3004479fc834acf7eda9633ad931e223ddbad.jpg)

<details>
<summary>scatter</summary>

Firm-Level Data on Input Price Growth Forecast vs. Realised Own Price Growth
| Input Price Growth Forecast (pp) | Own Price Growth (%) | Type |
|---|---|---|
| -14 | 4.2 | Negative Forecast Errors |
| -5 | 4.1 | Negative Forecast Errors |
| -1 | 3.6 | Negative Forecast Errors |
| -1 | 3.0 | Negative Forecast Errors |
| -1 | 2.8 | Negative Forecast Errors |
| -1 | 1.7 | Negative Forecast Errors |
| 0 | 3.0 | Positive Forecast Errors |
| 0 | 3.5 | Positive Forecast Errors |
| 0 | 3.6 | Positive Forecast Errors |
| 0 | 4.4 | Positive Forecast Errors |
| 0 | 5.2 | Positive Forecast Errors |
| 0 | 6.1 | Positive Forecast Errors |
| 0 | 7.0 | Positive Forecast Errors |
| 0 | 7.9 | Positive Forecast Errors |
| 0 | 8.9 | Positive Forecast Errors |
| 0 | 9.9 | Positive Forecast Errors |
| 25 | 12.8 | Positive Forecast Errors |
Line of Best Fit
</details>

On the left, the chart is visually approximated from Dao et al. (2023). On the right, the chart is visually approximated from De Fiore et al. (2025).

Research from Denmark's Nationalbank similarly found that higher natural gas prices have a significantly greater and more persistent impact on Euro area inflation, whereas a negative shock of the same magnitude had an almost negligible effect. For crude oil, the asymmetry was also present but less pronounced.

Similar insights emerge from micro data at the firm level. For example, a study of the French manufacturing sector estimated a passthrough rate for positive energy price shocks of over $100\%$ , compared to just $58\%$ for negative shocks. A BIS study similarly found that Italian corporate pricing responds strongly to rising input costs but only

weakly to falling ones (Exhibit 1, right).

# Why the Asymmetry?

Uneven passthrough could reflect several factors.

First, asymmetric firm markup adjustment. When input costs rise, firms are forced to adjust prices upward to protect their profit margins given the constraint of bankruptcy. But when costs fall, firms might retain prices to expand margins, especially when they have market power.

Second, the cost of changing prices (“menu costs”) could play a role. Given the cost of changing prices—both physical “menu costs” and the desire to avoid negative reactions to frequent price changes—firms may absorb small cost decreases rather than incur these broader adjustment costs with positive trend inflation.

Third, the asymmetry could reflect downward nominal stickiness in prices and wages. When a positive energy shock erodes purchasing power, workers are likely to demand higher wages. Conversely, firms find it very difficult to cut nominal wages when their costs fall, meaning cost savings are not fully passed on through lower labour costs.

# New Evidence

We provide fresh statistical evidence on this passthrough behaviour in the Euro area.

We start with a simple top-down perspective, similar to the IMF and Danish national central bank. In particular, we use a statistical (vector autoregressive) model to estimate the effect of non-core (food and energy) inflation on sUBSequent core inflation, controlling for long-term inflation expectations and labour market slack. Using a quarterly sample from 1999-2025 we find that commodity price shocks have statistically significant effects on sUBSequent core inflation. This passthrough, however, is entirely driven by positive price shocks, while the passthrough of negative non-core shocks is small and insignificant (Exhibit 2).

Exhibit 2: Top-Down Evidence Clearly Shows an Asymmetry in Food and Energy Shock Passthrough   
![](images/bde4429edffc219ae236eb9b41bdff60172a0097660bd2748a55d1d0b98d6d7d.jpg)

<details>
<summary>line</summary>

| Quarters Since Energy Shock | Positive Shock | Negative Shock |
| --------------------------- | -------------- | -------------- |
| 0                           | 0.0            | 0.0            |
| 2                           | 0.3            | -0.1           |
| 4                           | 0.4            | -0.2           |
| 6                           | 0.2            | -0.1           |
| 8                           | 0.0            | 0.0            |
| 10                          | 0.0            | 0.0            |
</details>

Source: GS Global Investment Research

This result, however, is sensitive to the inclusion of the 2022-23 energy shock. Restricting the sample to 1999-2019 reveals no significant evidence for asymmetric passthrough behaviour.

We therefore consider two extensions that consider a broader set of data.

The first is a panel version of the model above, which utilises the cross-country variation in energy shocks and passthrough to provide more statistical information. We find that passthrough is significant for positive energy inflation, but statistically insignificant for negative energy price growth (second columns in Exhibit 3, left). In other words, the relationship between energy inflation and core inflation appears to be “kinked” (as shown in Exhibit 3, right). Our results are also robust to ending the sample in 2019 (third column in Exhibit 3, left).

Exhibit 3: A Cross-Country Panel Confirms Uneven Passthrough 

<table><tr><td rowspan="2"></td><td colspan="3">Dependent variable: Core Inflation (%qoq, non-ann.)</td></tr><tr><td>(1) Linear 2000-2025</td><td>(2) Kinked 2000-2025</td><td>(3) Kinked 2000-2019</td></tr><tr><td>Core Inflation (%qoq, non-ann., 1q lag)</td><td>0.17***</td><td>0.16***</td><td>0.11**</td></tr><tr><td>Core Inflation (%qoq, non-ann.d, 2q lag)</td><td>0.23***</td><td>0.23***</td><td>0.29***</td></tr><tr><td>Inflation Expectations (%qoq, non-ann.)</td><td>0.48***</td><td>0.47***</td><td>0.44***</td></tr><tr><td>Labour Market Tightness (standard deviations, 1q lag)</td><td>0.12***</td><td>0.12***</td><td>0.12***</td></tr><tr><td>Energy Inflation (%qoq, non-ann., 1q lag)</td><td>0.01***</td><td></td><td></td></tr><tr><td>Positive Energy Inflation (%qoq, non-ann., 1q lag)</td><td></td><td>0.02***</td><td>0.02***</td></tr><tr><td>Negative Energy Inflation (%qoq, non-ann., 1q lag)</td><td></td><td>0.00</td><td>0.00</td></tr><tr><td>Fixed Effects</td><td>Country</td><td>Country</td><td>Country</td></tr><tr><td>Observations</td><td>1027</td><td>1027</td><td>798</td></tr><tr><td>R-squared</td><td>0.49</td><td>0.49</td><td>0.37</td></tr></table>

\*, \*\* and \*\*\* means significance at 10/5/1% levels under Driscoll and Kraay (1998) standard errors.

![](images/69d9149e7449570a6966946a5026a6c1ea08ee55cb5e6fb268d3716f7c2dde08.jpg)

<details>
<summary>scatter</summary>

| Energy Inflation (%qoq) | Core Inflation (%qoq) |
| ------------------------ | --------------------- |
| -30                      | 0.5                   |
| -20                      | 0.0                   |
| 0                        | 0.0                   |
| 10                       | 0.5                   |
| 20                       | 0.5                   |
| 30                       | 0.5                   |
</details>

Source: GS Global Investment Research

The second is a panel of firm pricing intentions, using the European Commission business survey. The intuition is that firms look much more likely to report selling price increases after energy prices rise—such as in 2021 and 2022—than report selling price decreases when energy prices fall—like in 2023 and 2024 (Exhibit 4, left). We test for this statistically by regressing selling price expectations across sectors on the product of wholesale energy prices and each sector’s energy intensity, as an “instrument” for sector-level energy prices. We also control for employment expectations to capture aggregate demand.

Exhibit 4: Uneven Pricing is also Found in Sectoral Firm Pricing Surveys   
![](images/d619bb9ec190d0da8332576744b430d6ef871cf6f14cb34ce2f68b983c6da439.jpg)

<details>
<summary>line</summary>

| Year | Share of Firms Expecting Price Increases (%) | Share of Firms Expecting Price Declines (%) |
|------|---------------------------------------------|----------------------------------------------|
| 2016 | ~8                                          | ~15                                          |
| 2017 | ~15                                         | ~10                                          |
| 2018 | ~20                                         | ~8                                           |
| 2019 | ~15                                         | ~6                                           |
| 2020 | ~10                                         | ~10                                          |
| 2021 | ~30                                         | ~5                                           |
| 2022 | ~60                                         | ~3                                           |
| 2023 | ~45                                         | ~5                                           |
| 2024 | ~20                                         | ~10                                          |
| 2025 | ~15                                         | ~8                                           |
| 2026 | ~35                                         | ~5                                           |
</details>

![](images/7eec6f7dc3d5032f85b0606b4768d3c889374ba3c559e0512cefa057e954edb0.jpg)

<details>
<summary>bar</summary>

| Category | Pctg. Points (Left Axis) | Change in Firm Selling Price Expectations After a 10% Energy Price Increases (Right Axis) |
|---|---|---|
| All Energy Price Changes | 2.7 | 1 |
| Only Energy Price Decreases | 0.8 | -1 |
| Only Energy Price Increases | 5.0 | 7 |
</details>

Source: GS Global Investment Research, European Commission

Our results suggest that firms in more energy-intensive sectors are more likely to report higher selling price expectations when energy prices increase (Exhibit 4, right). In contrast, a fall in energy prices does not lead to a statistically significant change in firms' selling price expectations. This confirms that firms are more likely to adjust prices after a rise than a fall in energy prices.

# Implications for the Outlook

We see two implications of this "rocket and feather" passthrough for the outlook.

First, the asymmetric passthrough creates upside risks to the core inflation outlook. That is, declines in energy prices from here (following a reopening of the Strait of Hormuz) might provide little relief for the core inflation outlook, while further energy price increases could push up inflation sharply further. This can be seen by mapping symmetric energy price assumptions into core inflation using our cross-country panel regression results (Exhibit 5).

Exhibit 5: The Pricing Asymmetry Creates Upside Risks for Core Inflation   
![](images/77b8c017b5cc465bc63f4ec0d8f4a862b2ba797cc26056f1160466e8af98afa6.jpg)

<details>
<summary>line</summary>

| Quarter   | Actual | Baseline GS Forecast | Downside | Upside |
| --------- | ------ | -------------------- | -------- | ------ |
| 2025Q1    | 75     | -                    | -        | -      |
| 2025Q4    | 65     | -                    | -        | -      |
| 2026Q3    | 100    | 100                  | 80       | 130    |
| 2027Q2    | -      | 90                   | 75       | 110    |
| 2028Q1    | -      | 85                   | 70       | 95     |
| 2028Q4    | -      | 80                   | 70       | 90     |
</details>

![](images/f81308bd0c2b0df024c3033f08ff9a8ffd29303cd2225ef6dfc82dca32c7e40c.jpg)

<details>
<summary>line</summary>

YoY Core Inflation Simulations Deviation From Baseline GS Forecast
| Period | Actual (yoy) | Baseline GS Forecast (yoy) | Downside Simulation (yoy) | Upside Simulation (yoy) |
|---|---|---|---|---|
| 2025Q1 | 2.56 | | | |
| 2025Q4 | 2.32 | | | |
| 2026Q3 | 2.38 | 2.58 | 2.42 | 2.78 |
| 2027Q2 | 2.68 | 2.68 | 2.49 | 3.00 |
| 2028Q1 | 2.30 | 2.30 | 2.30 | 2.30 |
| 2028Q4 | 2.00 | 2.00 | 2.00 | 2.00 |
</details>

On the left, the downside assumption converges towards 70\$/bbl. The upside assumption features the same but positive deviation from the baseline, so as to be symmetric to the downside assumption.   
Source: GS Global Investment Research, Haver Analytics

Second, uneven passthrough could support the case for ECB rate hikes. This is both by lowering the chance that a sudden drop in energy prices could improve the inflation outlook significantly and by strengthening the case for risk management hikes in the presence of upside inflation risks.

Taken together, our analysis supports our recent upgrade to the core inflation profile (which we now see peaking at $2.7\%$ ) and our baseline forecast for two ECB hikes (June and September).

# Sven Jari Stehn

# Alexandre Stott

# European Economics Team

# Sven Jari Stehn

+44(20)7774-8061

jari.stehn@gs.com

GS International

# Filippo Taddei

+44(20)7774-5458

filippo.taddei@gs.com

GS International

# Alexandre Stott

+33(1)4212-1108

alexandre.stott@gs.com

GS Bank Europe SE - Paris

Branch

# James Moberly

+44(20)7774-9444

james.r.moberly@gs.com

GS International

# Niklas Garnadt

+49(69)7532-1537

niklas.garnadt@gs.com

GS Bank Europe SE

# Katya Vashkinskaya

+44(20)7774-4833

katya.vashkinska

[中间内容因长度限制已省略]

e have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to sUBStantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g.,

marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
