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
Payments, Processors & IT Services

# PayPal + Stripe Round 2? The deal that could reshape global payments. But can it happen? And at \$60.50?

![](images/ac74809b47eaa5f4f3726ed2e3e7f2299bb1e499be7fcd95c8c510aacd1617e6.jpg)  
Harshita Rawat, CFA  
+1 917 344 8485  
harshita.rawat@bernsteinsg.com

![](images/e581a5ad59398ad7600b483730f6696989360c82e2039a4ac367577fedd470b1.jpg)

Simran Ratani

+1 917 344 8329

simran.ratani@bernsteinsg.com

![](images/c241ef8097e62dcfcd001a5395633fd649a89e40c665319a1375e0548c54f806.jpg)

Viola Chen

+1 917 344 8614

viola.chen@bernsteinsg.com

Reuters reported late last night (link) that Stripe (private) and Advent have submitted a \$60.50/share bid (would value PayPal at \$53B, +28% from Tuesday's price) for PayPal, supported by \$50B committed financing. The proposal was reportedly made in July after an initial approach in April. This follows news in February that PayPal is attracting takeover interest from multiple parties, and Stripe had expressed a preliminary interest in acquiring all or parts of PayPal (link). PayPal shares are up 16% in pre-market to \$56.

As we have highlighted in our prior research, at < \$50 PYPL stock (pre-deal price), strategic actions (M&A, divestitures) cannot be ruled out. For a company with waterfront properties (Braintree, Venmo) and 231m monthly active users, 67m for Venmo (\~20% of US population; highly attractive Gen Z skew), reach across \~90% of online merchants, \$1.8T in volumes, double-digit % share in e-commerce processing in the U.S. and \~50% share within digital wallets - it's not a surprise to us that buyers are circling post the significant sell-off even though the branded business is challenged.

incorporate a more significant deal premium on PayPal's all-time low valuation, considering its fortress balance sheet and \~15% FCF yield. There are also other strategic options e.g., selling Venmo, Braintree and Branded separately - especially since the check (for the entirety of PayPal) is too big to write for many. Stripe's acquisition rumor came on the back of its own valuation marked up to \$159B in Feb. Note that PayPal's new CEO just did a reorg of the company across checkout solutions, Venmo and Braintree and targeting \$1.5B+ of cost savings over 2-3 years. Accepting a bid which is only 28% above current price and near PayPal's lowest valuation since its IPO is unlikely.

There is then the massive financing task — especially since Stripe has shown no interest in becoming public. The financing may become more complicated if the deal price goes up. Stripe and Advent have \$50bn in committed financing (on a \$53B proposal) and the goal may be to likely lever PayPal's fortress balance sheet (with net cash position) and \~\$6B/yr FCF generation. That said, this could push PayPal's leverage quite high (potentially to 5-6x) - for a business with potentially declining FCF.

The deal also faces significant regulatory hurdles given the combined scale of the two companies. We believe that Stripe/Advent will likely make the argument, however, that digital payments are highly competitive with numerous acquirers and digital wallets/BNPL options.

It may potentially be possible that Stripe pursues only specific assets rather than the entire company. There are also cultural, and infrastructure challenges associated with integrating modern architecture with legacy systems, and the complexity of a B2B company owning B2C customer service infrastructure.

Stripe's potential interest in PayPal could also spur a bidding war (e.g., for Braintree and Venmo) with other prospective buyers (continued on the next page).

## DETAILS

## [continued from 1 $^{st}$ page]

## Why Stripe might be interested in PayPal?

\- There are probably multifold reasons: scale-driven horizontal and vertical consolidation (through branded and Braintree), further market-share expansion through bundling (precisely what PayPal did with Braintree), an improved value proposition for merchants (e.g., better conversion, lower fraud through ownership of the PayPal digital wallet), cross-sell opportunities (e.g., Stripe products into PayPal's massive SMB and enterprise base), closed-loop optionality (better economics and data), and a growing willingness to expand further into the consumer side. Note that Stripe already has the Link product—which is an order of magnitude smaller vs. PayPal.

\- There is also meaningful agentic optionality, where integrating PayPal's vast consumer infrastructure (BNPL, debit cards, data) with Stripe's merchant distribution could be valuable in an agentic commerce era.

\- Finally, Stablecoins could present an interesting angle - post Stripe's recent infrastructure investments (Bridge) and product launches (Stablecoins as a Service) - PayPal can give Stripe an avenue for Stablecoin payments (e.g., for cross-border B2B and payouts). PayPal also owns PYUSD (\$3B in market cap).

## This would, however, take Stripe deeper into consumer-facing territory

\- Potentially creating some conflict with some existing customers such as Shopify which has Shop Pay (frenemy to PayPal), BNPL providers (e.g. Klarna, which relies on Stripe as a key distribution partner), bank partners (banks view PayPal as a potential competitor) and potentially the networks as well.

Also note that Advent is not new to Payments having previously been involved in Vantiv, Worldpay, Nexi and Nuvei.

Other possible suitors (for the entire entity including core, and separately for Braintree, Venmo) that could emerge in our view:

All of PayPal (a big \~\$50B+ check to write including M&A premium)

\- More likely: Private Equity (PayPal is currently trading at 14% 2026 FCF yield and has a pristine balance sheet).

\- Less likely but possible - Elon Musk (fits in with everything-app strategy and X-Money), large banks e.g., JPM (regulatory scrutiny; likely more interested in diminishing PayPal than acquiring it as a whole), tech giants (strategically could be valuable but faces significant regulatory hurdles) and Amex (likely more interested in just Venmo).

\- Wildcard: Walmart (historically under-indexed in financial services, current CFO is PayPal's ex-CFO; Walmart is not new to Fintech e.g., PhonePe, OnePay)

Braintree (likely a \$10-20B check to write; comps' public valuation currently depressed)

\- Many possible suitors for horizontal consolidation including JPM (largest merchant acquirer online)

\- Less likely - Fiserv (has its own challenges and is already 3x levered, big check to write compared to market cap for Braintree).

\- Players such as Adyen are non-acquisitive so highly unlikely as a buyer.

Venmo (possibly \~\$10-20B check to write)

\- Many possible suitors including Revolut (prized P2P capability asset), banks including JPM (P2P is strategically valuable to protect customer relationships) and Amex (Gen Z synergy, already existing partnership).

\- Less likely: Affirm (Venmo/PayPal strategically valuable but Affirm doesn't have sufficient scale to and unlikely that PayPal sells to a competitor; interestingly Max Levchin was a co-founder at PayPal).

\- Crypto heavy firms (e.g., Robinhood) are a wildcard.

## The implications of this potential deal go far beyond Stripe and PayPal.

The combined scale of the two companies will be breathtaking: \~\$3.2T of payment volumes (ex-PayPal P2P), \~\$20B of net revenues (using PayPal gross profit for like-for-like comparison), FCF machine (PayPal generates \$6B, Stripe is also cash generative with potentially \~\$3B in FCF), 231m consumers, >30% of global e-commerce and >40% of U.S. e-commerce. This is likely a long-term negative for Adyen - not least because of the horizontal and vertical consolidation by Stripe. It is likely even more negative for legacy e-commerce acquirers (e.g., WP owned by GPN).

While being inconsequential to the medium-term numbers, this is also a long-term negative for Visa/Mastercard as the combination puts Stripe more in the formidable frenemy category (vs. a critical distribution partner historically). Even banks ought to be worried - Jamie Dimon has called out Fintechs including Stripe as his biggest competitors.

## Putting a floor on fintech valuations by embedding an M&A premium?

\- On a high level, PayPal possibly attracting suitors at these rock bottom valuation levels potentially could put a floor across the sell off in fintech. Strategic buyers and PE would likely see greater value than public market investors.

• See our recent note: 12 Jun 2026 - Payments/Fintech: Stocks near 10yr lows – is it time for bold actions?

## INVESTMENT IMPLICATIONS

We rate V, MA, ADYEN, XYZ, TOST Outperform. We rate PYPL, FIS, FISV, GPN, KLAR Market-Perform.

BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="3">14 Jul 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>V (Visa)</td><td>O</td><td>USD</td><td>356.02</td><td>450.00</td><td>(17.7)%</td><td>USD</td><td>11.47</td><td>13.17</td><td>15.16</td><td>31.0</td><td>27.0</td><td>23.5</td></tr><tr><td>MA (Mastercard)</td><td>O</td><td>USD</td><td>538.02</td><td>710.00</td><td>(22.6)%</td><td>USD</td><td>17.01</td><td>19.82</td><td>22.82</td><td>31.6</td><td>27.1</td><td>23.6</td></tr><tr><td>ADYEN.NA (Adyen)</td><td>O</td><td>EUR</td><td>827.50</td><td>1,600.00</td><td>(62.5)%</td><td>EUR</td><td>33.62</td><td>42.83</td><td>51.05</td><td>24.6</td><td>19.3</td><td>16.2</td></tr><tr><td>ADYEY (Adyen)</td><td>O</td><td>USD</td><td>9.32</td><td>18.63</td><td>(67.0)%</td><td>USD</td><td>0.39</td><td>0.50</td><td>0.60</td><td>23.8</td><td>18.5</td><td>15.6</td></tr><tr><td>XYZ (Block Inc)</td><td>O</td><td>USD</td><td>79.99</td><td>85.00</td><td>0.8%</td><td>USD</td><td>2,084</td><td>3,347</td><td>4,700</td><td>44.2%</td><td>50.2%</td><td>32.0%</td></tr><tr><td>TOST (Toast)</td><td>O</td><td>USD</td><td>30.00</td><td>39.00</td><td>(52.7)%</td><td>USD</td><td>633.00</td><td>802.78</td><td>990.80</td><td>24.7</td><td>19.5</td><td>15.8</td></tr><tr><td>PYPL (PayPal)</td><td>M</td><td>USD</td><td>47.37</td><td>45.00</td><td>(55.4)%</td><td>USD</td><td>5.31</td><td>5.23</td><td>5.30</td><td>8.9</td><td>9.0</td><td>8.9</td></tr><tr><td>FIS (FIS)</td><td>M</td><td>USD</td><td>40.58</td><td>73.00</td><td>(68.8)%</td><td>USD</td><td>5.76</td><td>6.30</td><td>6.91</td><td>7.0</td><td>6.4</td><td>5.9</td></tr><tr><td>FISV(Fiserv)</td><td>M</td><td>USD</td><td>49.54</td><td>76.00</td><td>(90.2)%</td><td>USD</td><td>8.64</td><td>8.06</td><td>8.76</td><td>5.7</td><td>6.1</td><td>5.7</td></tr><tr><td>GPN (Global Payments)</td><td>M</td><td>USD</td><td>75.89</td><td>86.00</td><td>(22.6)%</td><td>USD</td><td>12.22</td><td>13.89</td><td>16.13</td><td>6.2</td><td>5.5</td><td>4.7</td></tr><tr><td>KLAR (Klarna)</td><td>M</td><td>USD</td><td>19.63</td><td>20.00</td><td>NA</td><td>USD</td><td>65.1</td><td>305.3</td><td>461.7</td><td>62.5</td><td>13.3</td><td>8.8</td></tr><tr><td>SPX</td><td></td><td></td><td>7,543.59</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EDME</td><td></td><td></td><td>1,594.78</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended  
XYZ estimate is EBIT (M); TOST estimate is EBITDA (M); KLAR estimate is Adjusted EBIT; XYZ valuation is EBIT CAGR; TOST valuation is EV/EBITDA (x); KLAR valuation is EV/Adj EBIT (x);  
Source: Bloomberg, Bernstein estimates and analysis.

## I. REQUIRED DISCLOSURES

References to "Bernstein" or the "Firm" in these disclosures relate to the following entities: Bernstein Institutional Services LLC (April 1, 2024 onwards), Bernstein & Co., LLC (pre April 1, 2024), Bernstein Autonomous LLP, BSG France S.A. (April 1, 2024 onwards), Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited, Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社) and analysts employed by SG Africa Technologies & Services to produce Bernstein under a Global Services Agreement in place between Bernstein and SG.

Bernstein is part of a joint venture between SG (SG) and AllianceBernstein, L.P. (AB). Unless specifically noted otherwise, for purposes of these disclosures, references to Bernstein's “affiliates” relate to both SG and AB and their respective affiliates.

## VALUATION METHODOLOGY

This research publication covers six or more companies. For valuation methodology and other company disclosures: Please visit: https://bernstein-autonomous.bluematrix.com/sellside/Disclosures.action.

Or, you can also write to the Director of Compliance, Bernstein Institutional Services LLC, 245 Park Avenue, New York, NY 10167.

## RISKS

This research publication covers six or more companies. For risks and other company disclosures:

Please visit: https://bernstein-autonomous.bluematrix.com/sellside/Disclosures.action.

Or, you can also write to the Director of Compliance, Bernstein Institutional Services LLC, 245 Park Avenue, New York, NY 10167.

RATINGS DEFINITIONS, BENCHMARKS AND DISTRIBUTION

## EQUITY RATINGS DEFINITIONS

## Bernstein brand

The Bernstein brand rates stocks based on forecasts of relative performance for the next 12 months versus the S&P 500 for stocks listed on the U.S. and Canadian exchanges, versus the Bloomberg Europe Developed Markets Large and Mid Cap Price Return Index EUR (EDME) for stocks listed on the European exchanges and emerging markets exchanges outside of the Asia Pacific region, versus the Bloomberg Japan Large and Mid Cap Price Return Index USD (JPL) for stocks listed on the Japanese exchanges, and versus the Bloomberg Asia ex-Japan Large and Mid Cap Price Return Index (ASIAX) for stocks listed on the Asian (ex-Japan) exchanges -unless otherwise specified.

The Bernstein brand has three categories of ratings:

\- Outperform: Stock will outpace the market index by more than 15 pp

• Market-Perform: Stock will perform in line with the market index to within +/-15 pp

• Underperform: Stock will trail the performance of the market index by more than 15 pp

Coverage Suspended: Coverage of a company under the Bernstein brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors on events and developments.

Not Covered (NC) denotes companies that are not under coverage.

Bernstein brand stock ratings are based on a 12-month time horizon.

Autonomous brand – common stocks

The Autonomous brand rates common stocks as indicated below. As our benchmarks we use the Bloomberg Europe 600 Financials Price Return Index (E600BK) and Bloomberg Europe Dev Mkt Financials Large and Mid Cap Price Ret Index EUR (EDMFI) index for developed European banks and Payments, the Bloomberg Europe 600 Insurance Price Return Index (E600IN) for European insurers, the S&P 500 and S&P Financials for US banks and Payments coverage, S5LIFE for US Insurance, the S&P Insurance Select Industry (SPSIINS) for US Non-Life Insurers coverage, and the Bloomberg Emerging Markets Financials Large, Mid and Small Cap Price Return Index (EMLSF) for emerging market banks and insurers and Payments. Ratings are stated relative to the sector (not the market).

The Autonomous brand has three categories of common stock ratings:

\- Outperform (OP): Stock will outpace the relevant index by more than 10 pp

\- Neutral (N): Stock will perform in line with the market index to within +/-10 pp

\- Underperform (UP): Stock will trail the performance of the relevant index by more than 10 pp

Coverage Suspended: Coverage of a company under the Autonomous research brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors on events and developments.

Those denoted as ‘Feature’ (e.g., Feature Outperform FOP, Feature Under Outperform FUP) are our core ideas.

Not Covered (NC) denotes companies that are not under coverage.

Autonomous brand common stock ratings are based on a 12-month time horizon.

## Autonomous brand – preferred stocks

The Autonomous brand has three categories of preferred stock ratings:

\- Outperform (OP): The total return of the preferred instrument is expected to outperform preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

\- Neutral (N): The total return of the preferred instrument is expected to perform in line with preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

\- Underperform (UP): The total return of the preferred instrument is expected to underperform preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

Autonomous preferred stock ratings are based on a 6-month time horizon.

## AUTONOMOUS CREDIT RESEARCH

Where this report contains investment recommendations for credit instruments, as defined in article 3(1)(35) of the Market Abuse Regulation, the information below is presented to comply with its disclosure requirements.

The report may also include reference(s) to published opinions by other Autonomous or Bernstein analysts covering the equity securities of the issuer(s) referenced herein. Please note an investment recommendation for credit instruments published by the author(s) of this report may differ from the published view of the analyst covering equity securities for the issuer(s) contained in this report and vice versa.

## CREDIT RATINGS DEFINITIONS

The Autonomous brand has three categories of credit ratings:

\- Credit Outperform (C-OP): The total return of the Reference Credit

[中间内容因长度限制已省略]

ence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
