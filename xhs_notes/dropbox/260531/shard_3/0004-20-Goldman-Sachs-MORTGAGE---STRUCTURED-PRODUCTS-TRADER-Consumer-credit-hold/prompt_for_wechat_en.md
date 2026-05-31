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
MORTGAGE & STRUCTURED PRODUCTS TRADER

Consumer credit holds, sentiment splits

# Agency MBS: Prefer GN II/FN 4.0s swap over the GN II/FN 4.5s swap

We find the GN II/FN 4.0s swap offers better relative value vs. the GN II/FN 4.5s swap, within the Ginnie Mae (GN) and Fannie Mae (FN) complexes.   
In recent months, the GN II/FN 4.5s swap has benefited from a higher share of refinance loans in recent GN II 4.5s issuance vs. FN 4.5s issuance. However, the mortgage rate back-up and seasonal increase in purchase issuance could change this trend in the coming months.   
We believe the larger deliverable float of recently produced GN II 4.5s compared to FN 4.5s could exert downside pressure on the swap, especially vs. 4.0s where the size of the floats are more comparable between GNs and conventionals.

# RMBS: Lower prepayment risk driving prime jumbo outperformance

The OAS differential of prime jumbo seniors relative to same-coupon FN TBAs has tightened in recent months, driven by the back up in mortgage rates. Current differential is in line with fair value adjusted for collateral rate incentive.   
If mortgage rates hold steady, rising GWACs on future prime jumbo deal issuance could drive the OAS/price differential vs. TBAs to tighten further.

# ABS: Consumer credit is holding up, despite falling sentiment

- Recent consumer sentiment indicators have been mixed – the University of Michigan Sentiment Index collapsed to a record low, as high gasoline prices and rising inflation weighed on personal finances, while the Conference Board index remained resilient anchored by a stable “low-hire, low-fire” labor market.   
- Philadelphia Fed's LIFE survey data revealed a widening gap in financial security, with higher-income households reporting significant improvements in making ends meet while lower-income segments remain pressured, signaling a potential widening between prime and non-prime delinquency rates within ABS.   
Despite the sentiment trough, consumer ABS delinquencies remain remarkably insulated and track seasonal norms; we maintain that the threshold for energy price driven credit deterioration remains high.

# Arun Manohar

+1(212)902-8763

arun.manohar@gs.com

GS & Co. LLC

# Ben Shumway

+1(801)578-2553

ben.shumway@gs.com

GS & Co. LLC

# Neth Karunamuni

+1(212)934-0799

neth.karunamuni@gs.com

GS & Co. LLC

# Agency MBS

# Reracking the GN belly: Prefer owning GN II/FN 4.0s swap over GN II/FN 4.5s swap

Performance across the belly coupon GN II/FN swaps has been mixed this year. While the GN II/FN 3.5s and 4.0s swaps remain deeply negative, the GN II/FN 4.5s swap has rapidly appreciated to around 6 ticks currently from a low of -12 ticks in January (Exhibit 1). Interestingly, the swap price turned around largely around the same time when GN II 4.5s TBA began trading to a shorter effective duration vs. the FN 4.5s TBA (Exhibit 2). We believe this may have been due to the decline in mortgage rates and a greater increase in the share of refinance loans in the GN float vs. the conventional float (Exhibit 3). As we have noted previously, the weighted average loan age (WALA) ramps for refinance loans are much steeper than that for purchase loans. However, following the recent back-up in mortgage rates as well as the expected increase in purchase issuance during the spring/summer months, we expect GN issuance to migrate towards a greater share of purchase loans. The flatter purchase ramps could once again cause GN II 4.5s to trade with a longer duration vs. FN 4.5s. Finally, we believe the relative sizes of the deliverable floats should negatively impact GN II 4.5s vs. FN 4.5s (Exhibit 4). Interestingly, the size of the 2025-26 vintage float for GN II 4.0s is comparable to that in FN 4.0s (after excluding specified pools); however, the GN II 4.5s 2025-26 vintage float is much larger than the FN 4.5s 2025-26 vintage float. Based on these factors, we expect downside pressure for the GN II/FN 4.5s swap to emerge in the coming months. We expect the price difference between the GN II/FN 4.5s swap and the GN II/FN 4.0s swap to narrow and suggest shorting the GN II/FN 4.5s swap vs. owning the GN II/FN 4.0s swap.

Exhibit 1: Among the belly coupon swaps, the GN II/FN 4.5s swap has diverged from the GN II/FN 3.5s and 4.0s swaps over the past few months   
![](images/70e08a220ac23e756be7aedc11221d64882c42592f0cbb8028f652e1a54b32d9.jpg)

<details>
<summary>line</summary>

| Date   | GN II/FN 2.0s | GN II/FN 2.5s | GN II/FN 3.0s | GN II/FN 3.5s | GN II/FN 4.0s | GN II/FN 4.5s |
|--------|---------------|---------------|---------------|---------------|---------------|---------------|
| Jan-25 | ~70           | ~75           | ~60           | ~30           | ~20           | ~15           |
| Mar-25 | ~75           | ~80           | ~65           | ~40           | ~25           | ~20           |
| May-25 | ~80           | ~85           | ~70           | ~45           | ~30           | ~25           |
| Jul-25 | ~85           | ~90           | ~75           | ~50           | ~35           | ~30           |
| Sep-25 | ~80           | ~85           | ~70           | ~45           | ~30           | ~25           |
| Nov-25 | ~75           | ~80           | ~65           | ~40           | ~25           | ~20           |
| Jan-26 | ~70           | ~75           | ~60           | ~35           | ~20           | ~15           |
| Mar-26 | ~65           | ~70           | ~55           | ~30           | ~15           | ~10           |
| May-26 | ~60           | ~65           | ~50           | ~25           | ~10           | ~5            |
</details>

Source: Yield Book, GS Global Investment Research

Exhibit 2: The price of the GN II/FN 4.5s swap appreciated just as GN TBAs traded to a shorter duration vs FN TBAs   
![](images/e14eb73d8b4ba68c7b994f504ddbd88758418b6e54578aefb83600b824fb291a.jpg)

<details>
<summary>line</summary>

| Date   | Price of the GN II/FN 4.5s (in ticks) | Ratio of the effective durations of GN II 4.5s vs FN 4.5s (RHS) |
|--------|----------------------------------------|------------------------------------------------------------------|
| Jul-25 | ~3                                     | ~1.02                                                            |
| Sep-25 | ~7                                     | ~1.08                                                            |
| Nov-25 | ~0                                     | ~1.00                                                            |
| Jan-26 | ~-12                                   | ~0.98                                                            |
| Mar-26 | ~-5                                    | ~0.96                                                            |
| May-26 | ~7                                     | ~0.96                                                            |
</details>

Source: Yield Book, GS Global Investment Research

Exhibit 3: The share of refinance loans in recent GN II 4.5s issuance has exceeded that in FN 4.5s   
![](images/f624c2fc778dc4920e5e9083fd9c3cc5ac7cc03315f8c5edba11d99552d3b77c.jpg)

<details>
<summary>line</summary>

| Issuance date | FN/FH | GN   |
| ------------- | ----- | ---- |
| May-25        | 5%    | 12%  |
| Jul-25        | 3%    | 1%   |
| Sep-25        | 5%    | 1%   |
| Nov-25        | 30%   | 50%  |
| Jan-26        | 28%   | 43%  |
| Mar-26        | 45%   | 50%  |
| May-26        | 42%   | 38%  |
</details>

Source: eMBS, GS Global Investment Research

# Exhibit 4: The size of the outstanding float is most comparable across GNs and conventionals (UMBS) in the 4.0% coupon

Conventional float excludes balances locked in CMOs, held by the Fed or trade as specified pools. GN float is based on the GN II Multi pools and excludes balances locked in CMOs or held by the Fed; vintage for GN defined as issuance year.

![](images/0debced2ff23f5df05516af2901f78b7f7fecddc38e7d324797a41d081073661.jpg)

<details>
<summary>bar</summary>

| Year | Conventional float (ex-Fed/CMO/spec) ($bn) | GN II Multi float (ex-Fed/CMO) ($bn) |
| :--- | :--- | :--- |
| 2023 | 1.5 | 0.5 |
| 2024 | 0.8 | 2.5 |
| 2025 | 2.0 | 9.5 |
| 2026 | 0.7 | 4.5 |
| 2023 | 5.3 | 3.8 |
| 2024 | 5.1 | 6.2 |
| 2025 | 6.7 | 7.9 |
| 2026 | 5.0 | 2.8 |
| 2023 | 14.8 | 20.1 |
| 2024 | 15.4 | 29.6 |
| 2025 | 10.6 | 24.7 |
| 2026 | 16.9 | 22.3 |
The chart displays two sets of bars: the first set represents a single metric (e.g., cost or revenue in $bn), and the second set represents a multi-float metric (e.g., cost or revenue in $bn). The x-axis labels are 'Year' (3.5, 4, 4.5) and the y-axis is labeled as '$bn'. The legend distinguishes between 'Conventional float' (dark blue) and 'GN II Multi float' (light blue). The data points for each year are explicitly labeled on the bars.
</details>

Source: eMBS, Fannie Mae, GS Global Investment Research

# RMBS

# Prime Jumbo RMBS: Recent outperformance driven by dampened prepayment risk

Prime jumbo RMBS has outperformed over recent weeks, with OAS differentials between super-senior pass-throughs with a 5.5% coupon (SSNR PT 5.5s) and FN 5.5s TBA tightening to levels last seen towards the end of 2025. The tightening was likely driven by dampened prepayment risk, as mortgage rates backed up over the past three months. Prime jumbo issuance continues to remain healthy year-to-date, highlighting the strong demand for the deal type. As the GWAC of future prime jumbo deals increase and if mortgage rates hold steady, we believe the OAS differentials could tighten further.

# OAS differentials have tightened in recent weeks, likely reflecting declining

refinance incentives: Prime jumbo SSNR PT spreads have tightened relative to same-coupon FN TBAs in recent weeks, based on Yield Book OAS for new issue tranches that are priced closest to par dollar price (Exhibit 5). The latest OAS differential of around 20bp between SSNR PT 5.5s and FN 5.5s TBA is comparable to the differential in early December 2025. This recent tightening was likely driven by the uptick in mortgage rates and a corresponding decline in prepayment risk. Based on the relationship between the OAS differential on closest-to-par SSNR PT 5.5s vs TBA FN 5.5s and the corresponding collateral's rate incentive, we find that the current OAS differential is consistent with the historically observed relationship (Exhibit 6). If mortgage rates remain around current levels, the gross weighted average coupons (GWACs) of future deal issuance will begin to climb higher. This should bring the collateral closer to being at-the-money and can help compress the OAS/price differential vs. TBA, in our view.

Exhibit 5: Treasury OAS for prime jumbo super senior PT 5.5s has tightened as mortgage rates moved higher over the past three months   
Treasury OAS for prime jumbo SSNR PT 5.5s tranches that are priced closest to par   
![](images/8141adf1bccc2422890c46cf325b79c8dcea584b4616eea8874331f083057c89.jpg)

<details>
<summary>line</summary>

| Date    | 30-Year Fixed Mortgage Rate | FN 5.5s OAS (RHS) |
|---------|-----------------------------|-------------------|
| Sep-24  | ~7.0%                       | ~58               |
| Dec-24  | ~6.8%                       | ~56               |
| Mar-25  | ~6.5%                       | ~54               |
| Jun-25  | ~6.3%                       | ~52               |
| Sep-25  | ~6.0%                       | ~50               |
| Dec-25  | ~5.8%                       | ~48               |
| Mar-26  | ~6.0%                       | ~46               |
</details>

Source: Bloomberg, Yield Book, Optimal Blue, GS FICC & Equities, GS Global Investment Research

Exhibit 6: Recent OAS differentials between prime jumbo SSNRs and FN TBAs appear fair, adjusted for collateral rate incentive   
Polynomial best-fit between the collateral rate incentive and the OAS differential between the closest-to-par prime jumbo SSNR PT 5.5s and FN 5.5s TBA   
![](images/c542927ec329892f3e06d5b4ee9dfc3c1df394376a90a57a42f9694a2488344e.jpg)

<details>
<summary>scatter</summary>

| Collateral rate incentive (%) | OAS differential (bp) |
| ----------------------------- | --------------------- |
| -0.50                         | 20                    |
| -0.25                         | 15                    |
| 0.00                          | 10                    |
| 0.25                          | 15                    |
| 0.50                          | 20                    |
| 0.75                          | 30                    |
| 1.00                          | 40                    |
| 1.25                          | 50                    |
| 1.50                          | 45                    |
</details>

Source: Intex, Yield Book, GS FICC & Equities, GS Global Investment Research

Execution arb estimates have continued to decline: Earlier this year, we noted that the execution economics of prime jumbo RMBS deals have drifted closer towards par and more in line with our estimate of fair levels. We estimate that this trend has persisted for the recently priced deals as well (Exhibit 7). Overall pricing is closer to the FN 5.5s TBA than FN 6.0s TBA. A rise in GWACs on future prime jumbo deals, coupled with tightening spreads vs. TBAs, could lead to improved execution economics (Exhibit 8).

Exhibit 7: Prime Jumbo deal arb has continued to decline in line with lower GWACs   
Deal pricing and GWAC computed from sample deals available for the displayed months   
![](images/74662dd8c99d24992c2c32ec45fd6abaf0b4702a346f2a9c64770603455708a8.jpg)

<details>
<summary>line</summary>

| Date   | Deal Price (LHS) | FN 5.5 TBA (LHS) | FN 6.0 TBA (LHS) | Deal GWAC (RHS) |
|--------|------------------|------------------|------------------|-----------------|
| Sep 25 | 102.1            | 101.0            | 102.3            | 6.7             |
| Oct 25 | 102.3            | 101.2            | 102.4            | 6.7             |
| Nov 25 | 101.8            | 100.8            | 102.1            | 6.6             |
| Dec 25 | 101.8            | 101.0            | 102.4            | 6.4             |
| Jan 26 | 101.5            | 101.5            | 102.4            | 6.1             |
| Apr 26 | 101.0            | 100.9            | 102.3            | 6.1             |
| May 26 | 100.5            | 100.3            | 102.0            | 6.0             |
</details>

Source: Intex, Bloomberg, Global Sachs Global Investment Research

Exhibit 8: Deal prices are trading below fair value estimates, stemming from negative rate incentives   
Fair value estimate calculated based on the Optimal Blue 30-year conforming fixed rate and closest-to-par FN TBA as of deal pricing; additional pricing parameters are calibrated to sample deal pricing   
![](images/4e7825636aac12a28540219620919c759da77a19ab50ba6b7e8a7208bd9e6718.jpg)

<details>
<summary>scatter</summary>

| Month   | Deal Price | Fair Value Estimate |
|---------|------------|---------------------|
| Sep 25  | 102.1      | 101.1               |
| Oct 25  | 102.3      | 101.1               |
| Nov 25  | 101.8      | 100.8               |
| Dec 25  | 101.8      | 101.0               |
| Jan 26  | 101.3      | 101.2               |
| Apr 26  | 100.9      | 100.9               |
| May 26  | 100.6      | 100.7               |
</details>

Source: Bloomberg, Intex, Goldman Sach Global Investment Research

Monthly issuance volumes are broadly comparable to 2025 trends: Prime jumbo RMBS issuance activity remains healthy, with year-to-date issuance (through May 28 $^{th}$ ) surpassing 16 billion. On average, monthly issuance volumes are on track to slightly outpace 2025 volumes (Exhibit 9). The trends remain the same even with the inclusion of prime agency-eligible deals. We retain our forecast for total prime issuance (jumbo+agency eligible) to reach 52 billion this year (Exhibit 10).

Exhibit 9: Prime jumbo issuance volume has remained healthy throughout 2026   
Prime jumbo issuance volumes by pricing calendar year and month   
![](images/6ec42c758ae97f3d5d67f0ef469eacd9b629813b126f79918ad2b3e7425df3b2.jpg)

<details>
<summary>bar</summary>

Prime Jumbo Issuance Volumes
| Month | 2025 ($bn) | 2026 ($bn) |
| :--- | :--- | :--- |
| Jan | 2.6 | 3.1 |
| Feb | 3.5 | 3.3 |
| Mar | 2.3 | 4.6 |
| Apr | 2.3 | 2.6 |
| May | 3.8 | 2.5 |
| Jun | 3.2 | - |
| Jul | 3.0 | - |
| Aug | 2.0 | - |
| Sep | 4.9 | - |
| Oct | 4.1 | - |
| Nov | 2.8 | - |
| Dec | 3.6 | - |
</details>

Note: Issuance estimate as of May 28, 2026.   
Source: Bloomberg, Intex, GS Global Investment Research

Exhibit 10: Total prime issuance is also largely tracking 2025 volumes   
Prime RMBS issuance volumes by pricing calendar year and month; prime deals include prime jumbo and agency-eligible collateral   
![](images/e1bcc1c45cd878abf084347a33ab30201b6eafec4a3e25ffb64c45484f6f2f6c.jpg)

<details>
<summary>bar</summary>

Prime Issuance Volumes
| Month | 2025 ($bn) | 2026 ($bn) |
| :--- | :--- | :--- |
| Jan | 3.3 | 4.4 |
| Feb | 4.7 | 4.8 |
| Mar | 2.7 | 6.2 |
| Apr | 2.7 | 3.4 |
| May | 4.4 | 5.1 |
| Jun | 4.6 | - |
| Jul | 3.4 | - |
| Aug | 2.8 | - |
| Sep | 5.8 | - |
| Oct | 4.5 | - |
| Nov | 3.9 | - |
| Dec | 4.8 | - |
</details>

Note: Issuance estimate as of May 28, 2026.   
Source: Bloomberg, Intex, GS Global Investment Research

Prepays risks subside following the recent back-up in mortgage rates: Prime jumbo prepays have largely tracked 30-year mortgage rates in recent months. Prepays spiked in April, corresponding to the mortgage rate declines in January and February. However, the sharp reversal in rates since then has resulted in prepays subsequently dropping in May (Exhibit 11). Initial reporting indicates that the prepay decline is observable across GWAC buckets (Exhibit 12).

Exhibit 11: Prepays slowed in May as mortgage rates remain relatively high   
Prepays for fixed rate, all WALA prime jumbo loans. Optimal Blue 30-year conforming fixed rate displayed at a 2-month lag   
![](images/b48264025932b0bfaea25aec5b0f3286453855b7971172b183a8cbdcf52627d8.jpg)

<details>
<summary>line</summary>

| Date   | Prime Jumbo | 30 Year Mortgage (2-month lag, RHS) |
|--------|-------------|-------------------------------------|
| Jan-24 | 3.5         | 15.5                                |
| Jul-24 | 7.0         | 16.0                                |
| Jan-25 | 11.0        | 13.0                                |
| Jul-25 | 8.5         | 13.5                                |
| Jan-26 | 17.0        | 11.0                                |
</details>

Source: Bloomberg, Optimal Blue, Intex, Goldma

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
