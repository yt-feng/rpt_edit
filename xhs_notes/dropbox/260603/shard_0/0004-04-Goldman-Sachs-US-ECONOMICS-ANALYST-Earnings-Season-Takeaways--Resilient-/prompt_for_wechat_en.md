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
US ECONOMICS ANALYST

# Earnings Season Takeaways: Resilient, but for How Long?

With nearly all the S&P 500 now reported, we analyze Q1 company results and management commentary in order to draw macroeconomic lessons from micro-level insights.

Companies reported strong and broad-based revenue growth, reaffirming that economic activity increased at a solid pace. Our preferred guidepost for economic activity among S&P 500 companies—real revenues excluding the volatile energy sector—rose $6.3\%$ year-over-year.

Companies reported limited evidence of any slowdown in spending growth so far despite the Iran war and jump in oil prices but voiced concern about the near-term outlook. We expect below-consensus real consumer spending growth of just $1.3\%$ in 2026H2, reflecting the poor starting point for consumer cashflow (the personal saving rate is low and real disposable income fell $1.1\%$ year over year in last week's April personal income report), the fading boost from strong tax refunds, and a continued headwind from elevated inflation.

The war put upward pressure on input costs and downward pressure on company margins. Our company price announcement tracker—which captures both prices paid and received—increased to its highest level since late 2023. When discussing higher prices, companies most frequently mentioned the impact of higher oil prices but also noted increases in the costs of shipping, resin-based materials, and computer memory. Companies expect higher input costs to put downward pressure on margins in Q2: analysts revised their margin expectations—a proxy for corporate guidance—down the most in the sectors for which our price announcement tracker increased the most.

AI investment continues to support strong economywide capex growth. Hyperscaler capex plans once again surprised to the upside. Analysts revised their 2026 expectations—a proxy for corporate guidance—12% higher from the start of the earnings season to over \$750bn, corresponding to 83% growth vs. 2025. We expect business fixed investment in the national accounts to grow nearly 8% this year, reflecting a 3pp boost from AI-related spending as well as a 3pp boost from the tax incentives in last year’s fiscal package.

Limited impact from AI on the labor market so far, but lessons from early movers. A very modest share of management teams mentioned AI when discussing layoffs and hiring freezes, and business surveys and our own analysis

Ronnie Walker  
+1(917)343-4543 | ronnie.walker@gs.com GS & Co. LLC

suggest that the labor market impact has been limited so far. That said, in a narrow segment of the economy—tech companies and startups—the frequency of companies tying layoffs to AI increased sharply this month, with companies often attributing the recent reductions to advances in agentic models. Companies reporting AI-driven layoffs most frequently reported cuts to operations, data labeling, software development, and customer support roles. However, online job postings data from LinkUp suggest that those same companies have increased their demand for other roles, such as those focused on computer hardware and systems engineering and research.

# Earnings Season Takeaways: Resilient, but for How Long?

We review the Q1 corporate earnings season by analyzing company fundamentals, equity analyst forecasts, company-level alternative data, and management commentary.

# Another Quarter of Strong Results

With nearly all the S&P 500 now reported, the Q1 earnings season was again characterized by strong fundamentals. Q1 earnings are on track to grow $26\%$ year-over-year $^{1}$ (vs. an expectation of $12\%$ at the start of earnings season), earnings grew a robust $14\%$ for the median S&P 500 company (vs. $8\%$ ), and analysts raised their earnings estimates for the remainder of the year.

In Exhibit 1, we plot our preferred guidepost for economic activity for the S&P 500: revenues excluding the volatile and idiosyncratic energy sector, converted to real terms using the GDP price deflator (ex-energy). On this basis, real revenues rose $6.3\%$ year-over-year in Q1, the fastest pace since 2021 and near the top-end of the range seen last cycle.

The current pace of S&P 500 revenue growth is elevated relative to GDP growth, even after accounting for the fact that the S&P 500 is more cyclical than the broader economy—the historical relationship between the two suggests that the $2.6\%$ year-over-year increase in real GDP in Q1 is consistent with S&P 500 real revenue growth just below $4\%$ . The current outperformance reflects that there has been particularly strong revenue growth among the largest public companies—real revenues have increased by a more moderate $5\%$ over the last year for the median S&P 500 company—and especially the large tech companies—real revenues have increased by $2\%$ for the S&P 500 excluding the tech and energy sectors.

Exhibit 1: Real Corporate Revenues Grew a Strong $6.3\%$ Year-over-Year in 2026Q1   
![](images/c52137b775fec4381f5faef12ada35b2b2e2beaa5c93a03a3584c8707ebe613c.jpg)

<details>
<summary>line</summary>

| Year | Percent change, year ago |
|------|--------------------------|
| 1970 | +2.6%                    |
| Avg. during Recessions | -2.7%                  |
| Avg. during Expansions | +3.5%                  |
</details>

Source: Standard and Poor's, GS Global Investment Research

# Impacts of the War: A More Challenging Consumer Outlook

Despite the sharp rise in oil prices, company commentary and results suggest that the consumer remained healthy in the first quarter. Sales growth among consumer-facing companies improved—sales increased $9\%$ year-over-year among the median S&P 500 consumer discretionary company and $5\%$ for the median consumer staples company. That message from company results is corroborated by the official statistics and alternative data: Exhibit 2 shows that monthly measures of nominal consumer spending—including those that exclude gasoline purchases—have continued to grow at roughly the same rate for the last few months.

Exhibit 2: Alternative Measures of Nominal Consumer Spending Growth Remain Solid   
![](images/1b98df9430a7b8197496aabf92a2394faf3b244f0379314ab6c475074f3f6d6f.jpg)

<details>
<summary>line</summary>

| Year | Costco* | SpendTrend | Retail Control | Second Measure |
|------|---------|------------|----------------|----------------|
| 2022 | 13.0    | 21.0       | 9.0            | 3.0            |
| 2023 | 8.0     | 9.0        | 7.0            | 4.0            |
| 2024 | 7.0     | 7.0        | 5.0            | 2.0            |
| 2025 | 9.0     | 8.0        | 6.0            | -3.0           |
| 2026 | 7.0     | 7.0        | 6.0            | 3.0            |
</details>

Source: Company data, Bloomberg, GS Global Investment Research

However, companies voiced concerns that we share about the near-term consumer outlook, and Exhibit 3 shows that our quantitative measure of sentiment around the consumer on earnings calls declined sequentially. $^{2}$

Exhibit 3: Sentiment Around the Consumer Declined but Remained Around Its Historical Average   
![](images/19fb1774bfd38eb115283a369ea345e291e51c3f85ccc311ce973274d02470bd.jpg)

<details>
<summary>line</summary>

| Year | Index |
|------|-------|
| 2012 | 50    |
| 2014 | 55    |
| 2016 | 60    |
| 2018 | 58    |
| 2020 | 35    |
| 2022 | 65    |
| 2024 | 55    |
| 2026 | 60    |
</details>

Source: GS Global Investment Research

Discussed in more detail in our just-published note, we expect below-consensus real consumer spending growth of just $1.3\%$ in 2026H2, reflecting the poor starting point for consumer cashflow (the personal saving rate is low and real disposable income fell $1.1\%$ year over year in last week's April personal income report), the fading boost from strong tax refunds, and a continued headwind from elevated inflation and gasoline prices.

Differences in spending growth for low- and high-income households appeared to be normalizing on the eve of the rise in oil prices. The left panel of Exhibit 4 updates our analysis that compares nominal same-store sales growth for retailers that are generally located in lower-income zip codes to those that are in higher-income zip codes. Over the last year, the gap between their sales narrowed from 3.1pp in 2025Q1 to 1.1pp in 2026Q1. However, for the remainder of the year, consumption growth is likely to be weaker at the low end, where government spending cuts will hit hardest, lower immigration will weigh more on job and income growth, and higher gasoline prices will disproportionately burden households (Exhibit 4, right panel).

Exhibit 4: Sales Growth Between Companies Exposed to Households on Different Ends of the Income Spectrum Had Narrowed Over the Last Couple of Quarters, but the Rise in Gasoline Prices Will Weigh More on Consumption Growth at the Low End This Year   
![](images/dba38352017f39ef4c35bcacff0680781264032339e52a0e1058a2f3bbd6a542.jpg)

<details>
<summary>line</summary>

| Year | Lower Income* | Mid-to-High Income** |
|------|---------------|------------------------|
| 2015 | ~3%           | ~2%                    |
| 2016 | ~5%           | ~4%                    |
| 2017 | ~3%           | ~2%                    |
| 2018 | ~2%           | ~3%                    |
| 2019 | ~3%           | ~4%                    |
| 2020 | ~4%           | ~5%                    |
| 2021 | ~12%          | ~-5%                   |
| 2022 | ~22%          | ~25%                   |
| 2023 | ~8%           | ~10%                   |
| 2024 | ~1%           | ~2%                    |
| 2025 | ~1%           | ~3%                    |
| 2026 | ~1%           | ~2%                    |
</details>

\* 15 companies for which the median household income in the zip codes containing store locations is <80k/year on average. Includes DG, DLTR, TSCO, BIG, WMT, KR.   
\*\* 20 companies for which the median household income in the zip codes containing store locations is >=80k/year on average. Includes JWN, URBN, LULU, SFM, GAP, COST, TGT.

![](images/670091605ab0c89a36a26f1cce3e504c340e6cc1ad304ffb6b6fd339ff0b7cc3.jpg)

<details>
<summary>bar</summary>

Impact of Higher Gasoline Prices on 2026 Real Income Growth (Full-Year Basis), GS Forecast
| Income Cohort | Percentage points |
| :--- | :--- |
| Bottom | -1.25 |
| Second | -1.15 |
| Third | -1.05 |
| Fourth | -0.85 |
| Fifth | -0.6 |
| Overall | -0.75 |
</details>

Source: Company data, GS Global Investment Research

# Impacts of the War: Upward Pressure on Input Costs and Downward Pressure on Margins

Exhibit 5 shows that our company price announcement tracker—which captures both prices paid and received—increased to its highest level since late 2023 but remained well below its 2022 peak. When discussing higher prices, companies most frequently mentioned the impact of higher oil prices but also noted increases in other input costs, such as shipping, resin-based materials, and computer memory.

Exhibit 5: Our Company Price Announcement Tracker Increased to the Highest Level Since 2023 but Remained Well Below its 2022 Peak   
![](images/32a8aabf1cd346ff92a708e034a84532efa8f61e392412a70510c4a219754deb.jpg)

<details>
<summary>line</summary>

| Year | GS Company Price Announcement Index* (left) | PCE Inflation (right) |
|------|---------------------------------------------|------------------------|
| 2010 | ~4.0                                        | ~3.5                   |
| 2011 | ~5.0                                        | ~5.5                   |
| 2012 | ~4.5                                        | ~4.0                   |
| 2013 | ~4.0                                        | ~3.5                   |
| 2014 | ~3.5                                        | ~4.0                   |
| 2015 | ~3.0                                        | ~1.5                   |
| 2016 | ~3.5                                        | ~2.5                   |
| 2017 | ~4.5                                        | ~4.0                   |
| 2018 | ~5.5                                        | ~4.5                   |
| 2019 | ~5.0                                        | ~3.5                   |
| 2020 | ~4.0                                        | ~1.5                   |
| 2021 | ~6.0                                        | ~7.0                   |
| 2022 | ~8.0                                        | ~8.5                   |
| 2023 | ~7.0                                        | ~6.0                   |
| 2024 | ~5.0                                        | ~4.0                   |
| 2025 | ~4.0                                        | ~3.0                   |
| 2026 | ~5.0                                        | ~6.0                   |
</details>

\* Share of sentences mentioning higher prices less share of sentences mentioning lower prices.   
Source: Department of Commerce, GS Global Investment Research

Companies appear to expect these higher input costs to put downward pressure on margins in Q2. Exhibit 6 shows that analysts revised their margin expectations—a proxy for corporate guidance—down the most in the sectors for which our price announcement tracker increased the most.

Exhibit 6: Analysts Revised Their Margin Expectations—a Proxy for Corporate Guidance—Down the Most in the Sectors Facing the Greatest Input Cost Increases From the War   
![](images/06a51c4f04c158227b424193400513e247b0b498440ec4c5b73c4e73226ca781.jpg)

<details>
<summary>scatter</summary>

| Sector              | Change in GS company price announcement tracker (percentage points) | Analyst revisions to 2026Q2 margin forecasts since the start of earnings season (basis points) |
|---------------------|------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| Energy              | 1.5                                                                    | 2.0                                                                              |
| Consumer Staples    | 1.2                                                                    | -10.0                                                                            |
| Industrials Disc.   | 1.0                                                                    | -13.0                                                                            |
| Materials           | 3.8                                                                    | -16.0                                                                            |
| Energy (top)       | 0.0                                                                    | 1.0                                                                              |
| Consumer Staples    | 0.3                                                                    | -5.0                                                                             |
| Consumer Disc.      | 0.9                                                                    | -13.0                                                                            |
</details>

Source: FactSet, GS Global Investment Research

While the rise in energy prices will again delay progress on inflation, we believe that underlying price pressures remain benign. In particular, cost pressures from the labor market look quite restrained. Exhibit 7 shows that mentions of wages and labor costs on earnings calls fell to the bottom of the pre-pandemic range, and our tracker suggests that wages have increased $3.6\%$ over the last year and $3.1\%$ annualized in Q1, below the $4\%$ rate we estimate would be consistent with $2\%$ price inflation.

Exhibit 7: Worries Over Labor Costs Have Fallen to the Lowest Levels in a Decade   
![](images/03390d0c7fde786ecf77f27f191f2569e9616a429bcff9d03540689683914459.jpg)

<details>
<summary>line</summary>

| Year | Share of Management Teams Discussing Labor Costs |
| ---- | ----------------------------------------------- |
| 2010 | ~18%                                            |
| 2011 | ~20%                                            |
| 2012 | ~19%                                            |
| 2013 | ~17%                                            |
| 2014 | ~16%                                            |
| 2015 | ~17%                                            |
| 2016 | ~19%                                            |
| 2017 | ~18%                                            |
| 2018 | ~24%                                            |
| 2019 | ~20%                                            |
| 2020 | ~33%                                            |
| 2021 | ~18%                                            |
| 2022 | ~35%                                            |
| 2023 | ~30%                                            |
| 2024 | ~25%                                            |
| 2025 | ~20%                                            |
| 2026 | ~15%                                            |
</details>

Source: GS Dataworks, GS Global Investment Research

# Continued Focus on AI: Surging Investment, Limited Layoffs

Discussions about AI continued to dominate earnings calls. Exhibit 8 shows that $66\%$ of S&P 500 management teams discussed AI.

Exhibit 8: $66\%$ of S&P 500 Management Teams Mentioned AI on Q1 Earnings Calls   
![](images/33132188978f7b8ed9c6b00160a8d77022d921fc5c21b39ae85411f2e665b403.jpg)

<details>
<summary>line</summary>

| Year | S&P 500 | Russell 3000 |
|------|---------|--------------|
| 2016 | ~2      | ~1           |
| 2017 | ~8      | ~4           |
| 2018 | ~12     | ~6           |
| 2019 | ~15     | ~8           |
| 2020 | ~13     | ~6           |
| 2021 | ~17     | ~10          |
| 2022 | ~15     | ~9           |
| 2023 | ~38     | ~25          |
| 2024 | ~45     | ~30          |
| 2025 | ~50     | ~35          |
| 2026 | ~68     | ~52          |
</details>

Source: GS Dataworks, GS Global Investment Research

Company discussions about AI centered on two macro-relevant contexts. The first context was capex. Hyperscaler capex plans once again surprised to the upside. Exhibit 9 shows that analysts revised their 2026 expectations $12\%$ higher from the start of the earnings season to over \$750bn, corresponding to 83% growth vs. 2025.

In contrast to the slowdown we expect in consumer spending, we expect continued rapid growth in business fixed investment in the national accounts. Detailed in our mid-year capex update, we expect real business fixed investment to grow nearly $8\%$ this year, reflecting a 3pp boost from AI-related spendin

[中间内容因长度限制已省略]

e have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

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

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
