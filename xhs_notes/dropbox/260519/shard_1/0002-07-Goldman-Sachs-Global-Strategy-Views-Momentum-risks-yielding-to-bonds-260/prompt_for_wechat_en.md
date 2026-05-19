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
# GLOBAL STRATEGY VIEWS

# Momentum risks yielding to bonds

1. Despite the ongoing closure of the Straits of Hormuz, and a deterioration in the growth/inflation mix, equities are making new highs. Why? The main reason is that earnings growth is robust. This partly reflects the ongoing growth in the global economy; our economists estimate nominal global GDP growth this year (the main driver of revenues in the corporate sector) of 5.9%, compared with 4.7% last year. It is also a function of extraordinary growth in technology and energy related earnings – the two main drivers of market returns (Exhibit 1).

Exhibit 1: Year-to-date EPS revisions have been strong for IT and Energy - the two main drivers of market returns   
MSCI AC World sectors and Global Regions. Local currency   
![](images/fc911d8addc4e108bc8c8410598b1af9b49eb9dce44a698722deb189b8fd832a.jpg)

<details>
<summary>bar</summary>

| Sector | 2026 (%) | 2027 (%) |
| :--- | :--- | :--- |
| IT | 28 | 36 |
| MXAPJ | 27.5 | 34.5 |
| MSCI EM | 26 | 32 |
| Energy | 47 | 18.5 |
| Materials | 14.5 | 13.5 |
| MSCI AC World | 9.5 | 10 |
| S&P 500 | 7.5 | 7.5 |
| Topix | 2.5 | 4.5 |
| Comm Svs | 9.5 | 3 |
| Industrials | 3.5 | 2.5 |
| STOXX 600 | 4.5 | 2.5 |
| Financials | 2.5 | 1.5 |
| Utilities | -0.5 | 0.5 |
| Health Care | -5.5 | -0.5 |
| Consumer Staples | -1.5 | -1.5 |
| Real Estate | -1.5 | -2.5 |
| Consumer Discretionary | -3.5 | -3.5 |
</details>

Source: Datastream, I/B/E/S, STOXX, FactSet, GS Global Investment Research

In the US, for example, bottom-up consensus estimates for S&P 500 EPS in 2026 and 2027 have each risen by 8pp so far this year, but increasing expectations for AI capex spending and higher energy prices have driven the majority of the positive revisions. However, EPS revisions during the past month has been positive in every S&P 500 sector and earnings have been strong across the main regions. In most years, bottom-up analysts' consensus estimates are too optimistic and gradually decline. So far this year, and for next year, global earnings have been revised higher (Exhibit 2).

# Peter Oppenheimer

+44(20)7552-5782 | peter.oppenheimer@gs.com GS International

# Sharon Bell

+44(20)7552-1341 | sharon.bell@gs.com GS International

# Guillaume Jaisson

+44(20)7552-3000 | guillaume.jaisson@gs.com GS International

# Giovanni Ferrannini

+44(20)7051-2589 | giovanni.ferrannini@gs.com GS International

Exhibit 2: So far this year, and for next year, global earnings have been revised higher Consensus estimates in USD. MSCI AC World EPS   
![](images/219c9506777e69f92768b12da063340c906e3111bfa7e9cd22b4489b13abf3dc.jpg)

<details>
<summary>line</summary>

| Year | Value |
|------|-------|
| 2016 | ~25   |
| 2017 | ~28   |
| 2018 | ~30   |
| 2019 | ~35   |
| 2020 | ~25   |
| 2021 | ~38   |
| 2022 | ~40   |
| 2023 | ~38   |
| 2024 | ~42   |
| 2025 | ~45   |
| 2026 | ~48   |
| 2027 | ~55   |
</details>

Source: FactSet, Datastream, STOXX, GS Global Investment Research

# 2. The leadership of technology and energy has been responsible for a strong rise in the ‘Momentum’ factor (see: US Weekly Kickstart: AI, Momentum, and the One Big Trade) (Exhibit 3).

Exhibit 3: Momentum vs. Market   
MSCI Momentum Indices relative price return (USD)   
![](images/1caa2773b9f09687eb59be7f917ac5d8e035429b69447a48774b49b6922b87d8.jpg)

<details>
<summary>line</summary>

| Date   | US   | Europe | Japan | EM   | AC World |
|--------|------|--------|-------|------|----------|
| May-25 | 100  | 100    | 100   | 100  | 100      |
| Jul-25 | 98   | 103    | 103   | 103  | 101      |
| Sep-25 | 97   | 104    | 104   | 104  | 100      |
| Nov-25 | 95   | 102    | 103   | 103  | 98       |
| Jan-26 | 94   | 103    | 104   | 104  | 101      |
| Mar-26 | 92   | 104    | 105   | 106  | 103      |
| May-26 | 105  | 107    | 108   | 122  | 115      |
</details>

Source: Datastream, GS Global Investment Research

The speed of the rebound in technology has been the most dramatic driver in recent weeks and reflected, in our view, the valuation opportunity following the step de-rating earlier in the year (Exhibit 4).

Exhibit 4: The rebound in technology has reflected the valuation opportunity following the de-rating earlier in the year   
Distribution of returns of World Tech vs. World ex. TMT, data since 1973   
![](images/f5a6050105d4b2592e3429336474ec2411e9d1c77f5687b665c32aeae5a9d6f1.jpg)

<details>
<summary>line</summary>

| Month | Current | Median | Top Quartile | Bottom Quartile |
|-------|---------|--------|--------------|-----------------|
| Jan   | 0%      | 0%     | 0%           | 0%              |
| Feb   | -5%     | 0%     | 0%           | 0%              |
| Mar   | -10%    | 0%     | 0%           | 0%              |
| Apr   | -5%     | 0%     | 0%           | 0%              |
| May   | 15%     | 0%     | 0%           | 0%              |
| Jun   | 0%      | 0%     | 0%           | 0%              |
| Jul   | 0%      | 0%     | 0%           | 0%              |
| Aug   | 0%      | 0%     | 0%           | 0%              |
| Sep   | 0%      | 0%     | 0%           | 0%              |
| Oct   | 0%      | 0%     | 0%           | 0%              |
| Nov   | 0%      | 0%     | 0%           | 0%              |
| Dec   | 0%      | 0%     | 0%           | 0%              |
</details>

Source: Datastream, GS Global Investment Research

But the recovery in technology, and the rise in commodity related sectors reflected in the rise in momentum has also made the equity rally very concentrated. For example, the S&P 500 has returned ca. $10\%$ YTD in 2026, with TMT accounting for $85\%$ of the return. Korea, at the sharp end of the chips boom, has enjoyed a surge of nearly $80\%$ this year (following similar advances last year) but our Asia strategists now expect $300\%$ profit growth this year for the index. Other regions have also experienced significant concentration of returns driven by either technology, energy or both. Despite the fact that the Momentum rallies across regions has been a reflection of strong underlying profit growth, it does raise the risks in the market of a correction on the back of a deterioration in the growth and inflation mix.

3. These nearer terms risks have also become more elevated given the sharp rise in investor sentiment and positioning. Our Risk Appetite Indicator (RAI) rose above 1.1 last week, in its 99th percentile since 1991, and the highest read since 2021. Rising optimism is also reflected in the surge in retail participation, particularly in the US. GS trading desk estimates show that retail trading volumes have risen by $28\%$ since mid-April and a basket of retail favorite stocks (GSXURFAV) has rallied by $29\%$ over the same period.

At the same time, the rise in equity markets has occurred despite the rise in bond yields, pushing down equity risk premia (ERP) (Exhibit 5), making equity markets more vulnerable to disappointments on growth or inflation.

Exhibit 5: Equity market valuations have increased and largely shrugged off the rise in bond yields, pushing down equity risk premia  
Global market implied ERP (%)   
![](images/a92399816b78769160ad2b9eace920469a0b540c01ad5b367873c5a08ab44ec3.jpg)

<details>
<summary>line</summary>

| Year | Asia Pacific ex Japan | Europe | Japan | US | World* |
|------|------------------------|--------|-------|----|--------|
| 2025 | 5.1%                   | 3.8%   | 3.1%  | 2.8% | 2.5%   |
</details>

Source: GS Global Investment Research

The correlation of equities to bond yields has turned negative (Exhibit 6). If oil disruptions continue into 2H of this year and inflation expectations rise further, there is a real risk of a speed bump for equity markets.

Exhibit 6: The correlation of equities to bond yields has turned negative 3m rolling correlation of daily changes   
![](images/1df18a40b71e0fd4f5f7b61b63ac6d1b9f7b13bd22d5c19ec5c53ec6296fe004.jpg)

<details>
<summary>line</summary>

| Year | 3m rolling correlation |
|------|------------------------|
| 96   | -0.7                   |
| 97   | -0.5                   |
| 98   | 0.5                    |
| 99   | 0.6                    |
| 00   | -0.4                   |
| 01   | 0.1                    |
| 02   | 0.4                    |
| 03   | 0.8                    |
| 04   | 0.3                    |
| 05   | -0.2                   |
| 06   | 0.1                    |
| 07   | -0.5                   |
| 08   | 0.6                    |
| 09   | 0.7                    |
| 10   | 0.4                    |
| 11   | 0.6                    |
| 12   | 0.8                    |
| 13   | 0.6                    |
| 14   | -0.3                   |
| 15   | 0.5                    |
| 16   | 0.6                    |
| 17   | -0.2                   |
| 18   | 0.4                    |
| 19   | 0.6                    |
| 20   | 0.7                    |
| 21   | 0.5                    |
| 22   | -0.4                   |
| 23   | -0.5                   |
| 24   | -0.3                   |
| 25   | -0.2                   |
| 26   | -0.4                   |
</details>

Source: Datastream, GS Global Investment Research

While bond yields have been rising, the speed of the adjustment is important and could become a trigger for an equity correction. As shown in Exhibit 7, sharp bond yield moves have coincided with negative equity returns. The surge in government

borrowing is an additional factor pushing up longer dated yields across bond markets. Political developments can rapidly undermine confidence in government funding as they compete to raise money in an environment where capital spending is rising in the private sector. A sharp increase in bond yields from current levels present an additional meaningful risk for equity investors.

Exhibit 7: Sharp bond yield moves have coincided with negative equity returns   
Average global equities returns depending on absolute moves in US 10-year yields (data since 2000)   
![](images/9242676ca75d1028e77d6756c33c912dbd5347e995a1885f03faaa2205f141cb.jpg)

<details>
<summary>bar</summary>

| 1-month (absolute) change in interest rate (measured in standard deviation vs. past 3 years) | US nominal yield (%) | US real yield (%) |
| :--- | :--- | :--- |
| 0 to 0.5 | 1.6 | 1.3 |
| 0.5 to 1 | 1.3 | 1.25 |
| 1 to 1.5 | 0.8 | 0.7 |
| 1.5 to 2 | -0.1 | 0.3 |
| 2 to 2.5 | -0.7 | -0.4 |
| 2.5 to 3 | -1.2 | -0.6 |
| 3 to 3.5 | -2.6 | -2.0 |
| 3.5 to 4 | -3.6 | -2.0 |
| >4 | -3.4 | -4.4 |
Current
</details>

Source: Datastream, GS Global Investment Research

4. Nevertheless, taking a step back from the recent rise in Momentum, and the shorter term risks, we have argued that the core drivers of equity returns, and the distribution between relative winners and losers has shifted. For nearly 15 years equity returns followed a repeated pattern driven by three factors: geography, sector and factor. The US equity market consistently outperformed other regions, technology outperformed other sectors and the ‘Growth’ factor outperformed ‘Value’. Over this period, the technology sector experienced a boom in earnings as the world accelerated its transition to a digital world benefiting software and cloud computing. These companies were largely detached from the sluggish growth in economies around them and benefited from the capex that was installed during the internet boom a decade earlier and very low interest rates. Whereas slow growing ‘old economy’ businesses suffered from overcapacity, sluggish nominal economic growth and private sector deleveraging; rather than accruing value for shareholders, many were seen as ‘Value traps’.

5. What has changed? First, the rise in bond yields and inflation. After years of ultra-low interest rates, we have seen a significant rise in long term bond yields. Only a handful of years ago, a quarter of 10-year government bond yields had a negative yield; even 30-year yields in Germany and Japan were around zero, and in other markets around $1\%$ - they are now between 3.5 and $6\%$ with the US moving above $5\%$ for the first time since 2007. (Exhibit 8).

Exhibit 8: After years of ultra-low interest rates, we have seen a significant rise in long term bond yields   
30-year government bond benchmark yields   
![](images/13e1ec6f45adf69ca0f47c71b5bd4beb989b9e6b5b9ac0232a1cb3c722ba4393.jpg)

<details>
<summary>line</summary>

| Year | US    | Germany | Japan | UK    |
|------|-------|---------|-------|-------|
| 10   | 4.8%  | 4.0%    | 2.3%  | 4.5%  |
| 11   | 4.7%  | 3.8%    | 2.2%  | 4.4%  |
| 12   | 4.5%  | 3.5%    | 2.1%  | 4.2%  |
| 13   | 4.3%  | 3.3%    | 2.0%  | 4.0%  |
| 14   | 4.1%  | 3.1%    | 1.9%  | 3.8%  |
| 15   | 3.9%  | 2.9%    | 1.8%  | 3.6%  |
| 16   | 3.7%  | 2.7%    | 1.7%  | 3.4%  |
| 17   | 3.5%  | 2.5%    | 1.6%  | 3.2%  |
| 18   | 3.3%  | 2.3%    | 1.5%  | 3.0%  |
| 19   | 3.1%  | 2.1%    | 1.4%  | 2.8%  |
| 20   | 2.9%  | 1.9%    | 1.3%  | 2.6%  |
| 21   | 2.7%  | 1.7%    | 1.2%  | 2.4%  |
| 22   | 2.5%  | 1.5%    | 1.1%  | 2.2%  |
| 23   | 2.3%  | 1.3%    | 1.0%  | 2.0%  |
| 24   | 2.1%  | 1.1%    | 0.9%  | 1.8%  |
| 25   | 1.9%  | 0.9%    | 0.8%  | 1.6%  |
| 26   | 1.7%  | 0.7%    | 0.7%  | 1.4%  |
</details>

Source: Datastream, GS Global Investment Research

The impact of this rise in long term interest rates - reflecting a combination of rising term premium and higher government debt - has both reduced the value of very long duration growth within equity markets, while also undermining the valuation of Defensive and ‘Quality’ parts of the equity market (Exhibit 9), which are most sensitive to interest rates and were largely valued as bond proxies.

Exhibit 9: The rise in long term interest rates has undermined the valuation of Defensive and 'Quality' parts of the equity market   
MSCI Europe Quality vs. Market   
![](images/6284f900f8a26c3a81733a580e2659e237b62177621d43c1f61f6b9845f97129.jpg)

<details>
<summary>line</summary>

| Year | Europe Quality vs. Market | German 10y real interest rates (RHS, Inverted) |
|------|---------------------------|-----------------------------------------------|
| 90   | ~100                      | ~4.0                                          |
| 92   | ~105                      | ~3.5                                          |
| 94   | ~110                      | ~3.0                                          |
| 96   | ~115                      | ~2.5                                          |
| 98   | ~120                      | ~2.0                                          |
| 00   | ~130                      | ~1.5                                          |
| 02   | ~140                      | ~1.0                                          |
| 04   | ~150                      | ~0.5                                          |
| 06   | ~145                      | ~0.0                                          |
| 08   | ~160                      | ~-0.5                                         |
| 10   | ~170                      | ~-1.0                                         |
| 12   | ~180                      | ~-1.5                                         |
| 14   | ~190                      | ~-2.0                                         |
| 16   | ~200                      | ~-2.5                                         |
| 18   | ~210                      | ~-3.0                                         |
| 20   | ~230                      | ~-3.5                                         |
| 22   | ~220                      | ~-4.0                                         |
| 24   | ~210                      | ~-4.5                                         |
| 26   | ~185                      | ~-5.0                                         |
</details>

Source: Datastream, Bloomberg, GS Global Investment Research

6. Second, the increase in capital spending has been dramatic. In the decade and a half post the Global Financial Crisis there was little appetite or incentive for companies to invest heavily in capex. Growth and returns were low and there was excess capacity in many older economy industries. The launch of Chat-GPT, and growing demands for critical infrastructure, has shifted the balance in favour of capital spending. In the US alone, S&P 500 companies have reported year/year capex growth of +38% so far in Q1 2026 vs. just +1% for buybacks, a remarkable shift from the trend over the decade and a half following the financial crisis when companies were generally rewarded for buybacks and penalised for capex. The explosion of spending on capex by the major hyperscalers in the US has been the biggest driver. So far this year consensus estimates for the spend of the top 5 have increased by around \$80bn to \$755bn, 80% higher than a year ago. The result has been a significant boost to the earnings of AI infrastructure companies, including chip manufacturers (Exhibit 10).

Exhibit 10: The explosion of CAPEX spending boosted earnings of AI infrastructure companies, including chip manufacturers   
![](images/ed581c4ac8cd1bae2bbe2e5ed26f09bb5710b1ae2b0efc9436be50c4b35c019c.jpg)

<details>
<summary>line</summary>

| Date    | AI infrastructure stocks | S&P 500 | S&P 500 ex. AI infrastructure stocks |
|---------|--------------------------|---------|----------------------------------------|
| May-26  | +59%                     | +9%     | +1%                                    |
</details>

Source: FactSet, GS Global Investment Research

7. In combination, the rise in interest rates and the increase in infrastructure and capex spend have changed the drivers of returns within and across equity markets. The old pattern of US, technology and growth outperformance has given way to a more eclectic mix of returns across geographies, sectors and factors. The rise in capex spending has contributed to outperformance of the main infrastructure beneficiaries, both across technology (chips) and the old economy (energy and industrials) while the rise in bond yields has dampened the valuations and returns in the Defensive and Consumer parts of the market (Exhibit 11).

Exhibit 11: The rise in CAPEX boosted infrastructure beneficiaries; the rise in bond yields has dampened defensive and consumer parts of the market   
Price performance relative to Global Market. Renewables = GSWDRNEW   
![](images/b436dfdc3c5f894628fb18f268161a5a927df395f843ba5f283185bf6c1bb1ed.jpg)

<details>
<summary>line</summary>

| Date   | Renewables | Hardware | Cons. Staples | Cons. Discret. Health Care |
|--------|------------|----------|---------------|-----------------------------|
| Jan

[中间内容因长度限制已省略]

me have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
