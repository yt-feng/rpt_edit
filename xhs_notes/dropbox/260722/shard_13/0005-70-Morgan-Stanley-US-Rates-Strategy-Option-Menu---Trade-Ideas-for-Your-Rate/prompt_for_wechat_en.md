You are a senior financial newsletter editor with a consulting-style strategy lens. You turn research-report material into a long-form English article that is structured, insightful, and suitable for a serious business audience.

Objective:
- Write an English Markdown article based on the report parsing below.
- Target length: around 2200 words, plus or minus 15%.
- Tone: serious, analytical, strategic, and readable.
- The article should not feel like a summary. It should make an argument.
- You may extend the report's logic into reasonable second-order implications, but do not invent data, company actions, or quotes.
- Do not disclose every detail. Keep the article concise and end after the last substantive point.

McKinsey-style writing principles:
1. Answer first: open with the controlling idea, not background.
2. Governing thought: every section must support the main answer.
3. Mutually exclusive, collectively exhaustive logic: avoid overlapping sections.
4. So what: every section must explain why the point matters.
5. Synthesis over summary: do not list facts; interpret what the pattern means.
6. Action titles: section headings must be complete, insight-bearing sentences. Do not use generic headings such as "Key Takeaways", "Market Background", "Core View", or "Reader Implications".
7. Source specificity: ground every interpretation in a concrete number, named mechanism, comparison, or causal relationship from the report.

Required Markdown structure:
- `# Title`: make it a direct argument, not a topic label.
- Opening: 4-6 short paragraphs that state the main thesis and why now matters.
- 4-6 `##` sections. Each `##` heading must be an action title: a sentence that tells the reader the insight.
- One section should translate the report into a decision framework for readers.
- Never create a section about unresolved questions, what the report failed to answer, research gaps, limitations, further reading, or community access. If the source explicitly states a limitation, mention it once inside the relevant analytical paragraph.
- End with the final substantive paragraph. Do not add a CTA, promotional invitation, website, community reference, summary, or rhetorical question.
- End with: `*For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.*`

Content boundaries:
- Do not mention specific investment bank names such as GS. Use "a global investment bank report" if needed.
- Do not use emoji.
- Do not write like a viral post.
- Open with the most specific fact, contrast, or tension in the source. Avoid generic openings such as "Against this backdrop", "In recent years", or "As the market evolves".
- Vary sentence and paragraph length naturally. Do not repeat stock transitions such as "This means", "In other words", or "What matters most".
- Do not invent a personal voice, interview, or first-hand experience. Editorial character must come from evidence selection and precise phrasing.
- Do not output your reasoning process.
- Do not generate image Markdown; the system will insert original MinerU images afterward.

Report parsing:
"""
<table><tr><td>MS | RESEARCH</td><td>We appreciate your support</td></tr><tr><td>2026 EXTEL GLOBALFIXED INCOME POLL</td><td>VOTE NOW★★★★★</td></tr></table>

# Option Menu | Trade Ideas for Your Rates View

Investors often have a directional view on rates, but face a trade off between accepting unwanted risks or paying for option outcomes they do not expect. We scan the USD rates vol surface to identify our preferred expressions for higher rates, lower rates, steeper curves, and flatter curves.

## Key Takeaways

To balance unwanted risk and option cost, we identify preferred option expressions based on prevailing market drivers and volatility pricing.

\- Higher rates: 3m30y payer spread. Attractive entry level with low ATM volatility and rich payer skew.

■ Lower rates: 6m5y low strike receiver. Cheap receiver skew and sufficient time for macro data to challenge Fed hike pricing.

\- Steepener: 3m 5s30s curve cap. Captures multiple steepening scenarios while limiting downside to the premium paid.

\- Flattener: 1m 2s5s bear flattener. Targets a flatter curve only in a higher rate scenario with zero upfront premium.

The 2026 Extel Global Fixed Income Poll is now open and your participation matters a great deal to us. If you have found our research helpful, we would greatly appreciate your support in the following categories (please click here to request your ballot):

• USA > Interest Rate Derivatives

• USA > U.S. Rates Strategy

• Global > Macro Strategy

Please add me to your distribution list.

Click here for our Bloomberg Ticker Almanac.

Shaun Zhou  
Strategist  
Shaun.Zhou@morganstanley.com +1 212 761-3348

Matthew Hornbach  
Strategist  
Matthew.Hornbach@morganstanley.com +1 212 761-1837

Aryaman Singh  
Strategist  
Aryaman@morganstanley.com +1 212 761-1993

Eli P Carter
Strategist
Eli.Carter@morganstanley.com +1 212 761-4703

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

# Interest Rate Derivative Strategy

MS & CO. LLC

## United States | Trade ideas for your rates view

<table><tr><td>Shaun Zhou</td><td></td></tr><tr><td>Shaun.Zhou@morganstanley.com</td><td>+1 212 761-3348</td></tr><tr><td>Matthew Hornbach, CMT</td><td></td></tr><tr><td>Matthew.Hornbach@morganstanley.com</td><td>+1 212 761-1837</td></tr><tr><td>Martin Tobias, CFA, CMT</td><td></td></tr><tr><td>Martin.Tobias@morganstanley.com</td><td>+1 212 761-6076</td></tr><tr><td>Aryaman Singh</td><td></td></tr><tr><td>Aryaman@morganstanley.com</td><td>+1 212 761-1993</td></tr><tr><td>Eli Carter</td><td></td></tr><tr><td>Eli.Carter@morganstanley.com</td><td>+1 212 761-4703</td></tr></table>

Investors often have a clear directional view on rates but face a trade off between expressing that view with linear instruments, which introduces risks they do not intend, and buying vanilla options, which provide protection against scenarios they do not expect to realize.

We scan the USD rates option surface with expiries under one year to find the best value options for expressing four broad views: higher rates, lower rates, steeper curves, and flatter curves. These trades are not meant to fit every investor, but they offer a practical starting point for expressing directional views on USD rates.

## Higher Rates

Long-end Treasury yields continue to approach cycle highs but have repeatedly failed to break higher. At the same time, daily realized volatility has fallen close to multi year lows, leaving top-right implied volatility near the bottom of its recent range (Exhibit 1). Meanwhile, elevated payer skew reflects persistent demand for tail hedges amid inflation and geopolitical risks.

We recommend 3m30y F/F+25 payer spread as the preferred expression for investors seeking higher rate exposure:

\- Attractive valuation. Low ATM volatility keeps entry cost low, while elevated high strike payer skew allows investors to monetize rich upside volatility through the spread structure.

\- Prefer 3m expiry. The sub one year volatility surface is reasonably steep. While 1m expiry is cheaper, it captures too few macro catalysts. Longer expiries provide more event risk but become increasingly expensive. The late October expiry strikes a good balance, capturing three CPI releases, three payroll reports, and the September FOMC meeting, providing multiple opportunities for rates to reprice higher.

Trade idea: Buy equal notional 3m30y F/F+25 payer spread for 135c, equivalent to 8bp running. The structure offers a maximum payout of roughly 3x if the 30y swap rate

finishes above the high strike at expiry. Downside is limited to the premium paid. The main risk is that long-end yields fail to sell off over the next three months, for example, if softer inflation data alleviate concerns over long-term inflation.

Exhibit 1: 3m30y vol and skew  
![](images/f6a17527c9d733d99a0206f8310b1383e0bce09ea18b2d582fa7ec8454e6b7d4.jpg)  
Source: Bloomberg, MS

Exhibit 2: 30y rate, 3m forward and max payout level  
![](images/d86674d578c0c71db5df24bafacae8f6d0542deeb0117edacfc862ffe145c457.jpg)  
Source: Bloomberg, MS

## Lower Rates

The front end of the curve is pricing 35bp of additional Fed hikes by the end of 2026. Barring an exogenous shock, a rally would most likely require incoming data to challenge that pricing through softer inflation, weaker labor market data, or both. We therefore prefer an option with sufficient time for the macro data to play out.

We recommend a 6m5y F-25 receiver as the preferred expression to position for lower rates:

\- Cheap implied volatility. 6m5y implied volatility trades at only a 10bp/year premium to 21-day realized volatility (Exhibit 3), lower than both the 1y and 2y tails.

\- Limited term premium. The 5y volatility surface is the flattest among liquid tails (Exhibit 4), allowing investors to extend into six month expiry at relatively little additional cost.

\- Attractive receiver skew. Low strike volatility trades slightly below ATM volatility, close to the cheapest level since March 2023.

Trade idea: Buy a 6m5y F-25 receiver for 60c, equivalent to 13bp running. Downside is limited to the premium paid. The main risk is that incoming data remain resilient enough for the Fed to deliver one or more additional hikes over the next six months.

Exhibit 3: 6m5y vol and 21-day realized  
![](images/7289e91657fa7feeed958e776ef1019985af62584eb8e016c43b76b3036c46ab.jpg)  
Source: Bloomberg, MS

Exhibit 4: Vol premium relative to 1m expiry implied up to 1y expiry  
![](images/dd8213e8c489828014af8562aa10bebef4eb785dbf2fd84cf0673f54455c3940.jpg)  
Source: Bloomberg, MS

## Steeper Curve

Following our preferred expressions for higher and lower rates, it should come as no surprise that our favorite curve steepener is 5s30s. In a recent note, we highlighted UST 7s30s steepener as having the best vol-adjusted carry and roll.

We recommend a 3m ATM 5s30s curve cap as the preferred option expression for a steeper curve:

\- Constructive macro backdrop. The 5s30s curve has historically steepened during Fed cutting cycles. Spot 5s30s has retraced all of the steepening since April 2025 (Exhibit 5), despite the Fed having cut 75bp since then.

\- Balanced exposure. A curve cap provides asymmetric exposure to multiple steepening scenarios. The structure benefits from both front end repricing on Fed easing and a potential breakout in the long end. Correlation savings are close to historical median levels rather than an extreme, but we believe the balanced payoff profile more than offsets the average valuation.

Trade idea: Buy a 3m ATM 5s30s curve cap for 12c. Downside is limited to the premium paid. The main risk is a curve flattening over the next three months, for example if the Fed delivers additional hikes and signals a renewed hiking cycle.

Exhibit 5: 5s30s curve and latest value  
![](images/bc41cfd0a5be9415a2f90b0f76bcf4a56c51acfc86233d18a2552c4c37ae5187.jpg)  
Source: Bloomberg, MS

Exhibit 6: 3m 5s30s curve option implied curve correlation  
![](images/e2c926818cd7e8917f6d580775bd50a2dbf806c56df55c138da803dd61f3f0a8.jpg)  
Source: Bloomberg, MS

## Flatter Curve

The front end of the curve is likely to be driven by developments in Iran over the coming month. The transmission mechanism is straightforward: disruption to energy supply pushes commodity prices higher. This lifts inflation and inflation expectations, increasing the risk of a more hawkish Fed response and a bear flattening of the 2s5s curve.

We recommend a zero cost 2s5s bear flattener as the preferred expression for a flattening curve:

\- Prefer 1 month expiry. The calendar is light until the end of July, with no first tier data releases or meaningful Fed communication before the July FOMC meeting. As a result, developments in Iran are likely to be the dominant market catalyst for most of the 1-month period.

\- High uncertainty. The bear flattener provides targeted exposure to a hawkish repricing driven by higher inflation expectations while limiting exposure to other rate scenarios. If geopolitical tensions ease, inflation risk should fade and the curve would likely bull steepen, allowing the structure to expire worthless. In that scenario, investors avoid paying upfront premium for an outcome they do not expect.

\- Reasonable vol premium. A bear flattener typically carries a volatility premium. That premium is currently near the cheapest level since March, making the structure an attractive way to hedge geopolitical risks.

Trade idea: Buy 2.36x ATM+1bp 1m2y payer and sell 1x ATM 1m5y payer to achieve zero upfront premium. Downside is unlimited. The main risk is that the Fed delivers a hike at the July meeting while signaling a more hawkish policy path. In that scenario, the curve would likely bear steepen, causing the trade to underperform.

Exhibit 7: Vol benefit of 1m 2s5s bear flattener  
![](images/a980fe129104619bf01a0a4fab9ca67a26b83d94b7b7cb36995bd68c964a6015.jpg)  
Source: Bloomberg, MS

Exhibit 8: 2s5s and breakeven level  
![](images/2dda318bf2ff8a6130acb07ca4c0b09d0590c72baff1eaf0c0c23205b0f8988e.jpg)  
Source: Bloomberg, MS

• Trade idea: Maintain long 2y10y straddle outright

• Trade idea: Maintain long 1y1y F/F+25/F+50 payer ladder

\- Trade ideas:

• Higher rates: Enter buy 3m30y F/F+25 payer spread

• Lower rates: Enter buy 6m5y F-25 receiver

\- Steepener: Enter 3m 5s30s ATM curve cap

\- Flattener: Enter buy 2.36x 1m2y F+1 payer, sell 1x 1m5y ATM payer

## SDR Monitor

Investors have resumed selling volatility. In aggregate, dealers now hold roughly $50\%$ of the maximum long gamma position observed over the past year.

The long-end gamma profile exhibits two distinct peaks: one around current rate levels and another roughly 50bp lower. This suggests investors are comfortable selling gamma in a contained rally, but reluctant to be short gamma in any sell off.

Exhibit 9: Dealer net gamma exposure  
![](images/c0599ca62c07b200e33b41ad897b28dab41102192ebb1c39ca35b97ced78031a.jpg)  
Source: DTCC, MS

Exhibit 10: Historical spot dealer net gamma  
![](images/e7dbaaf4161c688f16305a8fe3c96ed16c99b96bf87ff75fb2a20cb770ec918f.jpg)  
Source: DTCC, MS

Exhibit 11: Net customer flow in gamma (\$k)

<table><tr><td>exp\tail</td><td>1Y</td><td>2Y</td><td>3Y</td><td>5Y</td><td>10Y</td><td>15Y</td><td>20Y</td><td>30Y</td></tr><tr><td>1M</td><td>1</td><td>(2)</td><td>(1)</td><td>(40)</td><td>(124)</td><td>(6)</td><td>(18)</td><td>(49)</td></tr><tr><td>2M</td><td>5</td><td>(3)</td><td>0</td><td>(5)</td><td>1</td><td>0</td><td>0</td><td>3</td></tr><tr><td>3M</td><td>(3)</td><td>6</td><td>2</td><td>(3)</td><td>21</td><td>14</td><td>0</td><td>(67)</td></tr><tr><td>6M</td><td>(1)</td><td>(0)</td><td>0</td><td>4</td><td>(11)</td><td>0</td><td>(2)</td><td>(1)</td></tr><tr><td>9M</td><td>2</td><td>0</td><td>0</td><td>5</td><td>0</td><td>0</td><td>(0)</td><td>4</td></tr><tr><td>1Y</td><td>(1)</td><td>1</td><td>(0)</td><td>0</td><td>10</td><td>0</td><td>0</td><td>39</td></tr><tr><td>18M</td><td>2</td><td>(1)</td><td>(0)</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2Y</td><td>(2)</td><td>(0)</td><td>(0)</td><td>0</td><td>(4)</td><td>0</td><td>0</td><td>(0)</td></tr><tr><td>3Y</td><td>(0)</td><td>0</td><td>(1)</td><td>(1)</td><td>0</td><td>0</td><td>(0)</td><td>0</td></tr><tr><td>5Y</td><td>(0)</td><td>0</td><td>0</td><td>(1)</td><td>(1)</td><td>0</td><td>(0)</td><td>(7)</td></tr><tr><td>10Y</td><td>0</td><td>0</td><td>0</td><td>(1)</td><td>(1)</td><td>0</td><td>(1)</td><td>0</td></tr><tr><td>15Y</td><td>0</td><td>0</td><td>0</td><td>(0)</td><td>(0)</td><td>0</td><td>0</td><td>0</td></tr><tr><td>20Y</td><td>0</td><td>0</td><td>0</td><td>0</td><td>(1)</td><td>0</td><td>0</td><td>0</td></tr></table>

Source: DTCC, MS

Exhibit 12: Net customer flow in vega (\$k)

<table><tr><td>exp\tail</td><td>1Y</td><td>2Y</td><td>3Y</td><td>5Y</td><td>10Y</td><td>15Y</td><td>20Y</td><td>30Y</td></tr><tr><td>1M</td><td>4</td><td>(19)</td><td>(5)</td><td>(310)</td><td>(689)</td><td>(32)</td><td>(91)</td><td>(253)</td></tr><tr><td>2M</td><td>69</td><td>(37)</td><td>0</td><td>(54)</td><td>16</td><td>0</td><td>0</td><td>33</td></tr><tr><td>3M</td><td>(59)</td><td>120</td><td>41</td><td>(57)</td><td>360</td><td>236</td><td>0</td><td>(1,053)</td></tr><tr><td>6M</td><td>(68)</td><td>(19)</td><td>0</td><td>163</td><td>(468)</td><td>0</td><td>(56)</td><td>(37)</td></tr><tr><td>9M</td><td>107</td><td>14</td><td>0</td><td>338</td><td>19</td><td>0</td><td>(26)</td><td>267</td></tr><tr><td>1Y</td><td>(51)</td><td>90</td><td>(2)</td><td>22</td><td>819</td><td>0</td><td>0</td><td>2,828</td></tr><tr><td>18M</td><td>334</td><td>(98)</td><td>(5)</td><td>51</td><td>34</td><td>0</td><td>0</td><td>33</td></tr><tr><td>2Y</td><td>(341)</td><td>(53)</td><td>(40)</td><td>1</td><td>(537)</td><td>64</td><td>0</td><td>(52)</td></tr><tr><td>3Y</td><td>(70)</td><td>2</td><td>(146)</td><td>(220)</td><td>213</td><td>0</td><td>(47)</td><td>110</td></tr><tr><td>5Y</td><td>(51)</td><td>0</td><td>0</td><td>(271)</td><td>(283)</td><td>0</td><td>(176)</td><td>(2,555)</td></tr><tr><td>10Y</td><td>88</td><td>0</td><td>0</td><td>(632)</td><td>(579)</td><td>0</td><td>(848)</td><td>0</td></tr><tr><td>15Y</td><td>0</td><td>0</td><td>0</td><td>(51)</td><td>(344)</td><td>18</td><td>82</td><td>0</td></tr><tr><td>20Y</td><td>0</td><td>0</td><td>0</td><td>0</td><td>(775)</td><td>0</td><td>0</td><td>0</td></tr></table>

Source: DTCC, MS

## Callable Issuance Monitor

Consistent with seasonal patterns, callable issuance has rebounded from the lows observed in June.

However, supranational issuance remains largely absent. We believe this reflects the well funded position of several supranational issuers and provides structural support for the 2y10y sector of the volatility surface.

Exhibit 13: Vega supply from callable issuance  
![](images/846d1c08a8b66208426977beca88cc6c173c6cac8c95c7022e80f3afe827c432.jpg)  
Source: Bloomberg, MS

Exhibit 14: Recent vega supply by pricing date  
![](images/4fe3019b51923c4cd630ebd2eb15034ff93a42ec8d0c8b3829bfed75ed932285.jpg)  
Source: Bloomberg, MS

## Skew Signal Monitor

The 3m10y OTC skew signal remains long duration. The recommended position is currently around 50% of the model's maximum long exposure.

Exhibit 15: Skew change and duration position  
![](images/8d6d4f380719d474023ff1d7a1d359ed5f25b69579fedf6f8fd9b1b9704a3722.jpg)  
Source: Bloomberg, S&P, MS  
Exhibit 16: Duration position and signal performance

![](images/5684fea61a8b87faa9760e06866f899d6dbd84c4010a6c43ddbf87606f709214.jpg)  
Source: Bloomberg, S&P, MS

## Valuation Methodology and Risks

Below you will find a list of our current trade ideas, entry levels, entry dates, rationales, and risks.

<table><tr><td>Interest Rate Derivatives</td><td></td><td></td><td colspan="2"></td></tr><tr><td>TRADE</td><td>ENTRY LEVEL</td><td>ENTRY DATE</td><td>RATIONALE</td><td>RISKS</td></tr><tr><td>Buy 3m30y F/F+25 payer spread</td><td>135c</td><td>7/20/2026</td><td>Low ATM vol and rich payer skew provides attractive entry level.</td><td>The main risk is that long end yields fail to sell off over the next three months, for example if softer inflation data alleviate concerns over long term inflation.</td></tr><tr><td>Buy 6m5y F-25 receiver</td><td>60c</td><td>7/20/2026</td><td>6m5y implied vol trades with limited premium over realized vol, limited premium across expiry surface, and allows enough time for macro data to challenge market pricing of Fed cycle.</td><td>The main risk is that incoming data remain resilient enough for the Fed to deliver one or more additional hikes over the next six months.</td></tr><tr><td>Buy 3m 5s30s ATM curve cap</td><td>12c</td><td>7/20/2026</td><td>A curve cap provides asymmetric exposure to multiple steepening scenarios. The structure benefits from both front end repricing on Fed easing and a potential breakout in the long end.</td><td>The main risk is a curve flattening over the next three months, for example if the Fed delivers additional hikes and signals a renewed hiking cycle.</td></tr><tr><td>Buy 2.36x 1m2y F+1bp payer, sell 1x 1m5y ATM payer</td><td>0c</td><td>7/20/2026</td><td>The bear flattener provides targeted exposure to a hawkish repricing driven by higher inflation expectations while limiting exposure to other rate scenarios.</td><td>The main risk is that the Fed delivers a hike at the July meeting while signaling a more hawkish policy path. In that scenario, the curve would likely bear steepen, causing the trade to underperform.</td></tr><tr><td>Buy 2y10y straddle</td><td>670c</td><td>6/10/2026</td><td>2y10y expected to be supported by structural flow from mortgage hedgers demand and reduced supply from callable issuance.</td><td>The risk is if vol drops significantly while rates remain anchored near strike level.</td></tr><tr><td>Buy 1y1y F/F+25/F+50 payer ladder</td><td>0c</td><td>3/10/2026</td><td>Recent selloff in rates and pick up in vol created an attractive window for 1y1y payer ladders. Breakeven level sits at levels that imply Fed hike over the next 2 years.</td><td>The risk is if energy-driven inflation becomes sustainable and forces the Fed to hike rates as a response.</td></tr></table>

Global Macro Strategy Team

<table><tr><td>MS &amp; CO. LLC</td><td>Matthew Hornbach, CMT
Matthew.Hornbach

[中间内容因长度限制已省略]

ce Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., authorised and regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the US by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

The following authors are Fixed Income Research Analysts/Strategists and are not opining on or expressing recommendations on equity securities: Aryaman Singh; Shaun Zhou; Eli P Carter; Matthew Hornbach; Martin W Tobias, CFA.

© 2026 MS
"""
