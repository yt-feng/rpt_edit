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
GLOBAL RATES TRADER

Relaxed, Not Relieved

Last week's range break in long-end US yields gave way to stabilization amid lower energy prices and supportive headlines out of the UK and Japan. The fundamental challenges are still broadly in place, however, and while long-end USTs are slightly cheap to fair, valuations are not sufficiently stretched to make the case for a deeper rally without a shift in macro risks. European rates continue to outperform as duration is protected by front-footed central bank action—we expect this to continue and recommend long 5y5y EUR real rates. European sovereign credit may have less room to tighten but still offers reasonable carry that should be insulated from front-end rates volatility. There is a growing valuation case for long Gilts, assisted by weakening activity data. But with political risks lingering, compression in Gilt risk premium is likely to be gradual. The moderation in long-end JGB yields partly reflects the ongoing sensitivity to supply/demand dynamics, but we continue to think that without inflation moderation or fiscal restraint, it is up to policy rate outcomes to bring lasting stability to long-end yields.

# United States and Canada

Settling down, but not yet turning around. The sharp selloff that extended into the start of this week found some stability, helped in part by lower energy prices amid another round of optimism about a potential resolution to the conflict. Additionally, just as foreign factors had been a source of bearish spillovers onto US duration through the first several months of the year, quieting domestic news in the UK and Japan helped with the stabilization effort. Even with yields down from the recent (and in the case of 30s, cycle) peak, they remain in the upper part of the range and are still lacking the ingredients for a more sustained reversal. A genuine resumption of energy flows is one route to rate relief, while evidence that the underlying inflation and growth/labor market paths are more dovish than the market anticipates is another; our baseline for lower yields over time is based on a mix of these two factors materializing. Sufficiently cheap valuations and a clearer challenge to risk assets from elevated yield levels is a third potential path to moderation. As things stand, longer-term forwards are modestly above our macro framework's estimate of fair, but valuations aren't stretched (Exhibit 1). Further, the mix of global pressures, the supply shock's damage to duration's portfolio value, and underlying effects from a more debt financed investment cycle—a backdrop that we've found can raise the sensitivity

# George Cole

+44(20)7552-1214

george.cole@gs.com

GS International

# William Marshall

+1(212)357-0413

william.c.marshall@gs.com

GS & Co. LLC

# Simon Freycenet

+44(20)7774-5017

simon.freycenet@gs.com

GS Bank Europe SE - Paris

Branch

# Isabella Rosenberg

+1(212)357-7628

isabella.rosenberg@gs.com

GS & Co. LLC

# Friedrich Schaper

+1(917)343-3214

friedrich.schaper@gs.com

GS & Co. LLC

# Loic Mathys

+44(20)7051-1664

loic.mathys@gs.com

GS International

of yields to debt supply and skew longer term yields higher relative to our model fair value—for now challenge the case for a deeper rally without a macro catalyst.

Convexity risk and the range break. Last week's break above 4.5% and 5.0% in 10-year and 30-year US Treasury yields brought an uptick in rate volatility and questions about whether negative convexity dynamics may have played an amplifying role after strong performance of short gamma strategies in April, and a more sustained period of GSE mortgage purchases. On rate vol specifically, the implied volatility response has been relatively mild compared to the magnitude of the yield range shift (Exhibit 2). That noted, our estimate of gamma exposure in TY options suggests the selloff this month resulted in an abrupt shift away from “peak” gamma (which we estimate was around 4.4%); to the extent that vol sellers are less frequent/threshold hedgers (and dealers are net long vol and hedging more actively), it is possible that the sharp move resulted in a relative pick-up in short gamma hedging. On the mortgage side, although GSE-retained portfolios have grown substantially—FNMA’s more than doubled and FHLMC’s grew by \~50% over the 12 months through March—their hedging behavior remains unclear, as the accumulation of larger duration gaps suggests increased tolerance for interest rate risk. We estimate the selloff from the start of May to the yield peak implied an extension worth roughly \$40 billion in 10-year equivalents for the universe of MBS held by traditional hedgers, but given the observed comfort with a larger duration gap, it is less clear how much was actually hedged. While we think the underlying pressures and yield valuations primarily reflect fundamental risks, these dynamics plausibly helped to amplify the price action in the more acute phase of the selloff. Looking ahead, we think the potential magnitude of any hedging should diminish given selloffs should bring less extension risk from here, while rallies would help to undo any accumulated duration gap.

Exhibit 1: Longer term UST forwards are only modestly cheap to our macro framework's estimate of fair value 5y5y UST yield vs model fair value with $+/-1$ standard deviation bands   
![](images/0b6e978caf12284e49e1fd7e6c11e24d855aa60a9b328fd55a12fd68d5a7f5e9.jpg)

<details>
<summary>line</summary>

| Year | UST 5y5y | Fitted Value | Residual |
|------|----------|--------------|----------|
| 2010 | 5.5      | 5.0          | 0.5      |
| 2012 | 4.0      | 4.5          | -1.0     |
| 2014 | 4.5      | 3.5          | 0.5      |
| 2016 | 3.0      | 2.5          | -0.5     |
| 2018 | 3.5      | 3.0          | 0.0      |
| 2020 | 1.0      | 1.5          | -1.0     |
| 2022 | 3.0      | 3.5          | 0.0      |
| 2024 | 5.0      | 4.5          | 1.0      |
| 2026 | 4.5      | 4.0          | 0.0      |
</details>

Source: Bloomberg, GS Global Investment Research

Exhibit 2: Implied vol has lagged the magnitude of the rate shift   
1m trailing range on 10y swap vs 1m10y implied vol   
![](images/c67f932fe4171cfd03680e1dd790638d2413b02e500cc838cce7b6d52b27ce5d.jpg)

<details>
<summary>line</summary>

| Date    | 1m range, 10y USD | 1m10y Implied Vol (rhs) |
|---------|-------------------|--------------------------|
| May-21  | ~15               | ~4                       |
| Feb-22  | ~75               | ~8                       |
| Nov-22  | ~85               | ~9                       |
| Aug-23  | ~60               | ~7                       |
| May-24  | ~50               | ~6                       |
| Feb-25  | ~40               | ~5                       |
| Nov-25  | ~30               | ~4                       |
| Aug-26  | ~40               | ~5                       |
</details>

Source: GS FICC and Equities, GS Global Investment Research

■ Funding costs ease further. Repo rates continued to decline this week, and while the broader trend suggests reserve demand has likely shifted relative to late last year, we think a few other factors have likely exacerbated the move. First, as noted previously, negative bill issuance had combined with Fed reserve management purchases (RMPs) and a drop in the TGA to constrain bill supply and boost system-wide liquidity; those effects are starting to turn. Second, this week overlaps with GSEs' "float period," during which MBS issuers build up cash reserves that temporarily deploy into the repo market ahead of making principal and interest payments. Third, limited carry in cash/futures bases may have led to reduced demand for leverage, with a steady reduction in levered funds' short position (Exhibit 3). We expect some reversal of this downdraft in funding costs over the coming weeks. Bill issuance has turned positive and the Fed has reduced RMPs, any effects from the "float period" should fade, and the TGA is likely to increase to levels closer to Treasury's target over the coming month. Even accounting for these factors, we think there is likely scope for RMPs to slow further, with our baseline for purchases to decline to a \$5bn per month average until early 2027, which we expect to take the steady state level of reserves to \~11% of bank assets (versus 11.5-12.0% recently)—levels we estimate are consistent with tri-party rates settling slightly below IORB. As discussed earlier this week, there are downside risks to our Fed balance sheet projections, but we see a high bar to a meaningful decline in balance sheet size.

# - Fourth consecutive downside inflation surprise makes two-sided BoC outlook.

Despite unfavorable base effects and the energy shock, Canadian CPI surprised to the downside for the fourth consecutive time this week. We think this reinforces the on-hold baseline for the BoC and argues for more two-sided risks around that modal case than market pricing implies. Benign underlying inflation (CPI-trim is back at the BoC's target), a pickup in the unemployment rate and soft growth were the ingredients that caused a restart of the BoC's cutting cycle late last year. And with those conditions present again, and transmission from higher oil prices to other categories limited thus far, we see further room for front-end hike premium to fade, especially in the near term. Given greater insulation against directional shifts in the oil price trajectory, we continue to like expressing this via 2s5s CAD curve steepeners, and given recent performance have tightened the stop, but would look to shift to outright longs if the front-end cheapens from here.

# Europe

Improving risk-reward for EUR rate longs. With the market still buffeted by energy prices (in both directions), we continue to think that EUR rates markets have broadly done enough to reprice inflation risk stemming from the conflict in Iran, even as the absence of tangible signs of progress limits the scope for European rates to rally. This week's PMIs highlight the ongoing passthrough of energy price pressures to broader inflation measures, while weakness in activity data points to precautionary rather than urgent ECB action. We expect this to solidify pricing for a June hike, while 1y1y will likely continue to be the point of the curve most sensitive to shifts in commodities markets. Further out the curve, we continue to see evidence that a front-footed central bank response should help anchor yields, with 5y5y forwards in EUR (and AUD — an early hiker) outperforming other curves. This is consistent with our spillover framework, which shows that Bunds have contributed bullish shocks to

G4 rates during the global sell-off (Exhibit 4). We think this dynamic will continue — while a protracted closure of the Strait of Hormuz may still see European rates move higher, we would expect this to be front-end-led, with the curve flattening and inverting. We continue to recommend 5y5y real yields longs.

Exhibit 3: The reduction in levered fund shorts in Treasury futures may in part reflect the diminished carry in Treasury basis   
Leveraged fund net UST futures position (notional, adjusted for valuation changes)   
![](images/00fe985d6f6742a53bb62abd62c959187096f5cc4912b7d42719304b33bcd10b.jpg)

<details>
<summary>line</summary>

| Date   | Value ($bn) |
|--------|-------------|
| Jan-24 | -800        |
| Jul-24 | -1000       |
| Jan-25 | -1300       |
| Jul-25 | -1100       |
| Jan-26 | -1200       |
| Jul-26 | -1100       |
</details>

Source: CFTC, Haver Analytics, GS Global Investment Research

Exhibit 4: Bunds have been a receiver rather than provider of bearish shocks   
G4 yields decomposition following our spillover framework   
![](images/3b12d5a10fd0f44654ad5ccd96fa53103a505014917210f1b6a20c9ee8c6a90d.jpg)

<details>
<summary>bar_line</summary>

| Date | US (bp) | UK (bp) | DE (bp) | JP (bp) | 10y Bunds (bp) |
|---|---|---|---|---|---|
| 01-Jan | 0 | -1 | 0 | 0 | 0 |
| 16-Jan | 8 | -13 | -14 | 11 | -5 |
| 06-Feb | 7 | -10 | -19 | 13 | -7 |
| 27-Feb | -5 | -10 | -28 | 3 | -28 |
| 20-Mar | 1 | 17 | -13 | 14 | 14 |
| 10-Apr | -3 | 14 | -8 | 19 | 10 |
| 01-May | -4 | 16 | -22 | 26 | 6 |
| 22-May | 6 | 15 | -24 | 33 | 18 |
</details>

Source: GS Global Investment Research, Bloomberg

Status quo in European sovereign spreads. Amid the stalemate in the conflict in Iran, sovereign spread compression has broadly stalled after a strong period of tightening. We continue to think that rates volatility will prove a better guide to sovereign credit performance than rates levels. As long as re-escalation is avoided, sovereign spreads can remain near current tights and offer reasonable carry, despite high and sticky front-end rates. We continue to recommend sovereign spread longs (FR, IT, and ES) vs ESTR at the front-end of the curve. For a more directional view on the conflict, we find that Greek and (to a lesser extent) Italian bonds continue to provide the strongest exposure to potential commodities price relief (Exhibit 5). Albeit with a lower beta, we note that the Spanish credit curve has also exhibited a strong sensitivity to oil price shifts. Government fiscal support across European economies for households and firms also remains contained — while some relief has been extended in France for instance, it remains modest in comparison to the 2022 energy shock. As long as this remains the case, we continue to think sovereign credit offers reasonable carry and should remain somewhat insulated from an increase in front-end rates volatility.

Gilts gain from softer data. Macro data weakened in the UK this week, with downside surprises in inflation, the labour market, services PMIs and retail sales. Energy and supply chain pressures are still likely to build throughout 2026, as illustrated by the strength in PPI, but we think this weakening in broad activity data reinforces our view that the BoE will remain on hold. We continue to expect Gilts to rally over the medium term despite lingering risk premium associated with political and fiscal risks. In our view, this rally will be driven by the ongoing repricing of a more dovish BoE path rather than a compression in risk premium. With any potential leadership challenge likely to follow a lengthy process, Gilt risk premium is unlikely to relax decisively; however, we increasingly see a positive valuation case to be long 10y Gilts — both on an overshoot of rate expectations vs what we forecast the BoE will deliver, and on 5y5y, which sits high relative to our valuation framework (Exhibit 6).

Exhibit 5: In the EMU-4, Italian bonds look best placed to benefit from potential oil price relief

Using GS fitted yields. Credit curve = 5s10s Country XX – Germany. Beta computed since the start of the Iran conflict.

![](images/e99ce6de83f1dea4de91b4f84fcf97c17affd6e101f53032803ca0123c6fe56a.jpg)

<details>
<summary>bar_line</summary>

| Category | 10y spread (bp/$/bbl) | Credit curve (RHS) (bp/$/bbl) |
|---|---|---|
| gr | 0.67 | 0.25 |
| it | 0.51 | 0.08 |
| fr | 0.26 | 0.02 |
| pt | 0.24 | 0.05 |
| es | 0.23 | 0.07 |
| be | 0.22 | 0.03 |
| at | 0.09 | 0.02 |
| fi | 0.06 | -0.03 |
| nl | 0.05 | 0.01 |
</details>

Source: GS Global Investment Research, GS FICC and Equities   
Difference between UK 5y5y and fair value

Exhibit 6: UK 5y5y levels look stretched from a macro perspective

![](images/38f85adec470aa8c6cfa95ccf385e2607e115f86bb7a87c5d39af1a888def47c.jpg)

<details>
<summary>line</summary>

| Year | 5y5y UK Actual - fitted value (%) |
|------|------------------------------------|
| 1993 | ~0.8                               |
| 1997 | ~1.6                               |
| 2001 | ~-1.5                              |
| 2005 | ~0.0                               |
| 2009 | ~1.3                               |
| 2013 | ~0.8                               |
| 2017 | ~-0.5                              |
| 2021 | ~-1.2                              |
| 2025 | ~1.2                               |
</details>

Source: GS Global Investment Research, GS FICC and Equities, Bloomberg, Consensus Economics

# Japan

Long-end meets rate relief. Comments from Governor Ueda brought some reprieve to pressure on long-end JGBs this week, as he emphasized that the BoJ would coordinate with the government to watch the bond market with a focus on rising long-term bond yields, and that the Bank would conduct interest rate policy for “stable inflation.” This focus on supply risks, particularly after the supplementary budget announcement, and the perceived validation of hike pricing saw long-end yields move lower and the front-end cheapen slightly. That said, our economists do not think a change to the BoJ QT path in June is likely following the results of the latest Bond Market Survey. While this could incrementally reverse some long-end rate relief, we still think interest rate policy remains the key driver for yields and risk premium across the curve. The latest JSDA data show that lifers net purchased super long-term bonds in April, as they had been signaling some openness to do, following net sales from Jan-Feb. If sustained, these purchases could alleviate pressure on 30s, but it remains to be seen whether this appetite only materializes during periods of relative market calm—longer term JGB yields were relatively stable in April before volatility picked back up in May. Ultimately, while supply risks remain, we continue to think that it is up to macro factors—inflation moderation, fiscal restraint, or front-loaded rate policy—to bring lasting stability to long-end yields.

# Australia and New Zealand

Too early to relax about RBA hike risk. The unexpected pickup in the unemployment rate caused a relief rally across the AUD curve, taking yields close to the post-March lows. While the data likely delays the timing of the next hike (our economists now expect the RBA to hike in August, vs June before) we still think

markets are underpricing near-term hawkish risks, with only 19bp of hike risk priced through September. We think this is at odds with the minutes released this week, which stated that while the previous hikes have provided some space to assess the conflict's impact, the growth impact from higher oil prices is likely to be cushioned, and instead highlighting the upside risks to the inflation forecast. Next week's inflation print may offer incremental clarity into the urgency for further hikes. Given current cheapness and RBA's doubts on how restrictive the current stance is, we think positions such as paying Se

[中间内容因长度限制已省略]

e have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not

necessarily reflect those of Global Investment Research and are not an official view of GS.

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
