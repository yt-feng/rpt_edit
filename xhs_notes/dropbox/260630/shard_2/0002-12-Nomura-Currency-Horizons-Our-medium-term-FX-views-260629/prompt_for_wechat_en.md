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
# Currency Horizons

Foreign Exchange - Global

## Our medium-term FX views

Moving on from the Middle East?

We introduce a new periodical that is focused on the medium-term FX outlook. Our aim is to offer a brief, multi-month view, in addition to our more timely, actionable, trade-idea focused reports.

For G10 FX, we expect the focus to shift back towards central banks' actions relative to rate hike pricing. We do not expect the Fed to hike rates, which should work against USD in H2. We see the greatest value in currencies where we think the respective central banks can start or continue their hiking cycles and where there is room for portfolio flow momentum to improve (EUR, JPY, NZD and AUD on the latter point). We see others as more vulnerable on central bank disappointment (GBP, CAD and SEK).

For Asia, ex-Japan, we favour outperformance in CNH, TWD and SGD, versus underperformance in KRW, IDR and INR through 2026. Strong capital flows are likely to support CNH and TWD, with the latter a clear beneficiary of global AI trade. Singapore's strong domestic momentum amid inflation risks suggest a supportive policy stance for SGD. The latter three may face more challenging BoP dynamics amid local-specific concerns.

Please click on the link below for our views on individual currencies.

Fig. 1: Global FX forecasts

<table><tr><td colspan="2"></td><td>29-Jun</td><td>Q3 26</td><td>Q4 26</td><td>Q4 27</td></tr><tr><td colspan="6">G10</td></tr><tr><td>US Dollar Index</td><td>(DXY)</td><td>101.20</td><td>100.20</td><td>98.00</td><td>92.70</td></tr><tr><td>Japanese yen</td><td>(USD/JPY)</td><td>161.8</td><td>158.0</td><td>154.0</td><td>145.0</td></tr><tr><td rowspan="2">Euro</td><td>(EUR/JPY)</td><td>184.6</td><td>182</td><td>182</td><td>181</td></tr><tr><td>(EUR)</td><td>1.14</td><td>1.15</td><td>1.18</td><td>1.25</td></tr><tr><td rowspan="2">Swiss Franc</td><td>(CHF)</td><td>0.81</td><td>0.79</td><td>0.76</td><td>0.72</td></tr><tr><td>(EUR/CHF)</td><td>0.92</td><td>0.91</td><td>0.90</td><td>0.90</td></tr><tr><td rowspan="2">British Pound</td><td>(GBP)</td><td>1.32</td><td>1.33</td><td>1.35</td><td>1.36</td></tr><tr><td>(EUR/GBP)</td><td>0.86</td><td>0.86</td><td>0.87</td><td>0.92</td></tr><tr><td>Australian Dollar</td><td>(AUD)</td><td>0.69</td><td>0.71</td><td>0.73</td><td>0.75</td></tr><tr><td>Canadian Dollar</td><td>(CAD)</td><td>1.42</td><td>1.41</td><td>1.40</td><td>1.35</td></tr><tr><td>New Zealand Dollar</td><td>(NZD)</td><td>0.57</td><td>0.58</td><td>0.60</td><td>0.63</td></tr><tr><td>Norwegian Krone</td><td>(EUR/NOK)</td><td>11.31</td><td>11.40</td><td>11.50</td><td>11.50</td></tr><tr><td>Swedish Krona</td><td>(EUR/SEK)</td><td>11.08</td><td>11.10</td><td>11.20</td><td>11.20</td></tr><tr><td colspan="6">Asia</td></tr><tr><td>Chinese Renminbi</td><td>(CNH)</td><td>6.79</td><td>6.65</td><td>6.50</td><td>6.30</td></tr><tr><td>Hong Kong Dollar</td><td>(HKD)</td><td>7.843</td><td>7.820</td><td>7.800</td><td>7.790</td></tr><tr><td>Indonesian Rupiah</td><td>(IDR)</td><td>17854.0</td><td>17850</td><td>17800</td><td>17500</td></tr><tr><td>Indian Rupee</td><td>(INR)</td><td>94.3</td><td>94.0</td><td>93.0</td><td>92.0</td></tr><tr><td>Korean Won</td><td>(KRW)</td><td>1541.2</td><td>1550</td><td>1495</td><td>1440</td></tr><tr><td>Malaysian Ringgit</td><td>(MYR)</td><td>4.06</td><td>4.14</td><td>4.13</td><td>4.10</td></tr><tr><td>Philippine Peso</td><td>(PHP)</td><td>61.2</td><td>60.8</td><td>60.3</td><td>59.5</td></tr><tr><td>Singapore Dollar</td><td>(SGD)</td><td>1.293</td><td>1.280</td><td>1.255</td><td>1.225</td></tr><tr><td>Thai Baht</td><td>(THB)</td><td>33.3</td><td>32.9</td><td>32.3</td><td>31.3</td></tr><tr><td>Taiwan Dollar</td><td>(TWD)</td><td>31.9</td><td>31.3</td><td>30.8</td><td>30.0</td></tr></table>

Source: Bloomberg, NOM.

## Research Analysts

Global FX Strategy
Dominic Bunning - Nlplc
dominic.bunning@NOM.com
+44 (0) 20 7102 4063

Craig Chan - NSL
craig.chan@NOM.com
+65 6433 6106

Yujiro Goto - NSC
yujiro.goto@NOM.com
+81 3 6703 1120

Yusuke Miyairi, CFA - NIplc
yusuke.miyairi@NOM.com
+44 (0) 20 7102 4145

Wee Choon Teo - NSL
weechoon.teo@NOM.com
+65 6433 6107

Andrew Ticehurst - NAL
andrew.ticehurst@NOM.com
+61 2 8062 8611

Vicky Chen - NSL
vicky.chen1@NOM.com
+65 6433 6540

## North America (USD, CAD)

Fig. 2: USD: A hawkish Fed and resumption in portfolio inflows likely to wane in H2  
![](images/d22aeb25645a735678d50c066b6772b0f62a22749b6330ba579ca21e529324d6.jpg)  
Source: Bloomberg, Nomu18

We see the DXY falling to around 98 by year-end (a decline of around $3.5\%$ from current levels).

USD has rallied in recent weeks, even though Middle East uncertainty has become less of a concern, thanks to a recalibration higher in the expected Fed rate path. A resumption of inflows into US equities has also been supportive in recent months.

We think this may struggle to be maintained later in the year.

Our base case is that the Fed does not hike in 2026 (vs c40bp priced in), with a sequential softening in growth and inflation momentum in H2 giving Fed Chair Warsh an opportunity to pushback against the hawks. A 40bp decline in relative US yields would likely see USD fall versus its peers (Fig. 2). We also see some downside risk to US data in the summer from residual seasonality issues, and believe the de-dollarisation theme has scope to resume as the year progresses.

Fig. 3: CAD: Low inflation and a soft labour market suggest BoC hikes are unlikely to materialise  
![](images/c15a4b4f370eda875257d2512e7a702126fa4721b2bd9fef6ccb8c8f2c31c090.jpg)

We see short-term upside for USD/CAD, but look for a drift lower to 1.40 by end-2026.

Macroeconomic divergence between the US and Canada has been increasing, putting upward pressure on USD/CAD. We think this is likely to persist in early Q3. In particular, because inflation is much softer in Canada, this will likely keep the hurdle high for the Bank of Canada to re-raise its policy rate. Elsewhere, risks surrounding the USMCA renegotiations will likely add headwinds, with bilateral US-Canada discussions yet to commence and the 1 July deadline for a 16-year extension looking increasingly difficult to be met.

However, we note that the market's short CAD positioning has been expanding among a wide variety of investor types (e.g., asset managers, CTAs and corporates), posing a risk to our long USD/CAD view. Any positive CAD catalyst could trigger short-covering, though as wage growth is cooling and labour market slack us still evident, an imminent position unwind seems unlikely at this point.

## DM Europe (EUR, GBP, CHF, SEK, NOK)

Fig. 4: EUR: Upside expected owing to rate convergence and supportive portfolio flows  
![](images/a82af23fc3e05a9b41b95f2e90137599d848969a571dada5557b8e1d8f55e620.jpg)  
Source: Bloomberg, NOM

We see EUR/USD rising to 1.18 by end-2026 and into the 1.20s in 2027.

Cyclically, we think that market pricing may have over-reacted on the hawkish side to Fed Chair Warsh's first meeting. His comments contained dovish elements that have been somewhat overlooked (a focus on the 2 on “the left of the decimal” rather than specifically on 2.0% on inflation, for example). The task forces he announced may eventually see a dovish change at the Fed. We see unchanged rates this year versus c40bp of hikes priced.

Meanwhile, the ECB's reaction function remains hawkish, in our view, with a shift higher in its neutral rate expectations. We see a terminal rate of $2.75\%$ – around 25bp higher than market pricing.

From a flow perspective, portfolio inflows into the euro area have been improving in recent months (Fig. 4), while the current account surplus has remained in place. We see scope for EUR to benefit from any resumption in the “de-dollariation” and diversification theme that has gained popularity at various points in the last few years.

Fig. 5: GBP: Underperformance due to a softer rate profile and fiscal risk premium  
![](images/49fd632179e9dd62766f1a5373f91677d25b7ede70c02b2e249ab813e93abbf0.jpg)  
Source: Bloomberg, NOM

We see GBP/USD at 1.35 by end-2026. We see EUR/GBP rising to 0.90 by end-2027.

Our economists recently removed their forecast for a July BoE rate hike and see two cuts next year. This is the most dovish central bank outlook among our G10 forecasts. A softer labour market and limited sequential inflation pressures (Fig. 5), as well as a more dovish reaction function, suggest GBP will receive less support from rates in the months ahead.

Fiscal concerns may also continue to linger and cause a risk of acute GBP weakness. There are obvious questions about how the new Prime Minister will manage spending and taxation following Keir Starmer's unsurprising resignation on 22 June. Andy Burnham is the most likely replacement, according to polling and betting odds. Risks include tweaks to fiscal rules, a shift towards re-nationalisation or increases in taxes, which may curb investment and growth, even if the latter helps to maintain fiscal credibility among investors.

Fig. 6: CHF: Fundamentals are firm but be wary of carry trades becoming more prominent  
![](images/780dd8c064ab04c28ab8be459de9cf6867bb97fb934f272a2140ba6de440bc3e.jpg)  
Source:

We expect EUR/CHF to decline towards 0.90 in the latter part of 2026, with USD/CHF falling on broader USD factors to 0.76.

Long-term fundamentals remain highly supportive for CHF, even if some “debasement trade” flows, which helped the currency in Q1, fade. Carry trade momentum has been powerful in Q2, but historically this has not caused sustained CHF underperformance. A wider rate differential working against CHF, as other central banks hike rates is, however, a risk factor.

A large and resilient current account surplus and persistent inflows into financial account deposits provide a firm backdrop for gradual CHF appreciation. Meanwhile, low and stable inflation allows nominal CHF gains, without putting much upward pressure on the real effective exchange rate. The SNB has tended to focus on the REER with regard to its FX intervention activity, and so we do not expect sizable FX purchases to return (Fig. 6), barring any rapid “risk off” type of appreciation of the currency.

Fig. 7: SEK: A relatively dovish monetary policy and a recycling of the current account surplus hampers SEK potential  
![](images/3479e83837815c0510ae8369907ba507534fced33484af460ea80ddf299e4a16.jpg)  
Source: Bloomberg, NOM

We forecast EUR/SEK to trade at 11.2 at end-2026, with NOK/SEK trading around 0.97 over the same period.

SEK may continue to struggle in 2026 as the soft inflation backdrop and sluggish domestic growth momentum make it difficult for the Riksbank to hike rates. Below-target inflation may be partly attributed to tax changes enacted earlier this year to lower food prices. But even accounting for these factors, inflation momentum appears weak, and we struggle to see a hike this year. The drop in energy prices in recent months should also limit concerns about inflation remaining persistent and generating second-round effects.

On the plus side, the large current account surplus and relatively cheap valuations are likely to prevent excessive currency weakness. However, the continued recycling of the current account surplus into financial assets – mainly overseas equities (Fig. 7) – remains a drag, even as FX hedging ratios have risen a little more among Swedish institutions than their international peers.

Fig. 8: NOK: Expecting a Norges Bank rate hike and a potential reversal to FX purchases  
![](images/82e12247fa7f5a26dbc2e9121f1aed3026c1c6a01e05d6cfeed9e4b2e32b9012.jpg)  
Source: Bloomberg, NOM

We forecast EUR/NOK rising to 11.5 by end-2026 and see NOK/SEK trading at 0.97 over the same period.

NOK has been one of the few currencies to outperform USD year-to-date, though this has been undermined as oil prices have fallen, alongside progress towards a US-Iran deal. Oil prices will likely remain highly correlated with NOK, but we would expect two other factors to play major roles from here.

1) Norges Bank FX activity: FX sales by the central bank on behalf of the government have slowed already year-to-date (Fig. 8). They could even start to buy FX again in H2 if NOK tax receipts from oil activity rise sufficiently to offset domestic spending. These recycling flows could undermine NOK later this year.

2) Norges Bank rate hikes: The central bank has signalled a hike in the months ahead, and although this is now priced in for the months ahead, it may still leave carry differentials firmly in NOK's favour.

## DM Asia (JPY, AUD, NZD)

Fig. 9: JPY: Near-term risk of further upside in USD/JPY, but a medium-term peak may be approaching for the pair  
![](images/3b9bd5e3e81e040f7437c3405dabfcc9389597a5a908e19f16945c173df8c505.jpg)  
Source: Bloomberg, NOM

We forecast USD/JPY at 154.0 by end-2026 and 145.0 by end-2027.

The BOJ's 25bp hike in June was unable to limit JPY depreciation and the government's stance on the BOJ likely reduces its scope for aggressive rate hikes in the immediate term. With the 2y1y rate currently above $2\%$ , it will be difficult for the BOJ to out-hawk the market.

Looking further ahead, however, we see the balance of risks shifting in favour of a lower USD/JPY. Our USD weakness view aside, the MOF still has reasonable firepower for intervention, and its impact could be larger than a few months ago, owing to stretched net JPY short positions. The MOF could judge that USD/JPY going higher despite lower oil prices signals that the currency is “not reflecting fundamentals”. Moreover, the risk of the BOJ becoming more hawkish is growing, as our Japan economics team flags, because it has become more concerned about upside inflation risks.

Fig. 10: AUD: Terms of trade and capital flow dynamics should support AUD in the medium term AUDbn  
![](images/0c9d2dba18d86262fd6e171e494a507c7753fe24a1242bbd649ba858d3c9ad91.jpg)  
Source: ABS, NOM

## We see AUD/USD rising to 0.73 by end-2026.

From a medium-term perspective, we see the balance of forces tilting towards a higher AUD later in the year. The terms of trade have risen a little over recent quarters, and net portfolio capital flows, particularly into AUD bonds, remain very strong. Australia's fundamentals, including low government debt levels, remain sound, and we think AUD could be a winner, should any “de-dollarisation” theme re-emerge, though there have been few signs of Australian super funds changing their FX hedging ratios in the last year or so.

Our RBA view is not a big driver of our current AUD/USD thinking. Markets are pricing some risk of near-term rate hikes in both Australia and the US, but we do not envisage further policy tightening from either central bank this year. AUD remains highly correlated with broad risk sentiment, as proxied by equity indices, credit spreads and commodity prices, so swings in global risk sentiment remain an “X-factor” for AUD.

Fig. 11: NZD: Under-owned currency/assets and with a rate hike cycle set to start suggests upside for NZD
RBNZ Kiwi-GDP nowcast, % q-o-q  
![](images/4d669e9921a60cd3188e00e0cce2a0f6a61857b511aff19b8aa8e1ac81a6ccaa.jpg)  
Source: RBNZ, NOM

We see NZD/USD rising to 0.60 by end-2026, and see AUD/NZD at 1.20 over the same horizon.

The NZ economy was finally emerging from recession over late 2025/early 2026 before the Middle East crisis hit its terms of trade, owing to its heavy dependence on imported fuel. Higher fuel prices also caused an inflation scare, and the RBNZ, with a singular inflation remit, appears close to starting a hiking cycle.

We see several specific supports for NZD over the rest of the year: i) current rate spreads and the RBNZ starting a rate hike cycle; ii) short investor positioning; and iii) low but rising foreign holdings of NZGBs.

While the market path for hikes is slightly faster than our own projections, the narrowing of the carry differential may help NZD in the months ahead. Survey data have perhaps held up better than expected, and the RBNZ's latest Kiwi-GDP Nowcast suggests a solid bounce in GDP in Q3. We also see scope for the recent trend of rising foreign ownership of NZGBs to continue. Relative positioning, plus the theme of approaching central bank rate convergence should push AUD/NZD lower.

## AeJ FX: Our medium-term view

We favour outperformance in CNH, TWD and SGD, versus underperformance in KRW, IDR and INR through 2026.

## Fig. 12: CNH: Strong onshore corporate FX repatriation and stable US-China relation supports CNH outperformance

![](images/201c508902343e748a844a80628e948fc6d68ef656d5ab690149639a10522b01.jpg)

Source: Bloomberg, CEIC, NOM.

We forecast USD/CNH at 6.50 by end-2026, owing to FX policy, robust trade settlement and structural drivers of internationalisation and undervaluation.

An important driver of CNH outperformance since November 2025 has been Chinese corporates' strong net FX trade settlement, supported by China's resilient external sector and the stabilisation of US-China relations. We expect Chinese corporates' FX selling to stay robust in the coming months, with our economics team forecasting 2026 China export growth of $8.6\%$ y-o-y and a full-year trade surplus of USD1.161bn (Q1: USD247bn). Our economics team also expects no policy rate or RRR cuts in 2026.

Meanwhile, the USD/CNY fixing has also been drifting lower with rather stable positive fixing errors (i.e., actual fix minus projection). We believe the Chinese authorities may still be comfortable with a gradual pace of RMB appreciation despite some restraints in daily fixing. On BoP dynamics, stable US-China relations and the authorities' RMB internalization push should continue to create a conducive environment for China's capital inflows amid substantial RMB undervaluation.

Fig. 13: TWD: Global AI demand and capex support robust local fundamentals and capital inflows  
![](images/344e9fbb090e6594920680be5fddf2fb34452ecf2ac2954e2578ca3dce632c47.jpg)  
Mar-20 Feb-21 Jan-22 Dec-22 Nov-23 Oct-24 Sep-25

## We forecast USD/TWD at 30.8 by end-2026.

Taiwan should continue to benefit significantly from strong global AI demand and capex. The sustained AI boom and TSMC's strong capex (\~USD70bn in 2027) and local sourcing plan will be a positive catalyst for Taiwan's domestic semi supply chain. Export growth continues to exceed expectations, and our economist forecasts a current account surplus of USD220bn (21.3% of GDP) and above-consensus GDP growth of 9.9% in 2026, along with two 12.5bp CBC rate hikes this year. Besides current account inflows, we also expect foreign equity inflows to be broadly supportive for TWD.

We believe that a softer USD environment (if it materializes) may encour

[中间内容因长度限制已省略]

PURCHASE ANY SECURITIES, INCLUDING SEEKING ADVICE FROM AN INDEPENDENT FINANCIAL ADVISER REGARDING THE SUITABILITY OF THE INVESTMENT, UNDER A SEPARATE ENGAGEMENT, AS THE RECIPIENT DEEMS FIT. Unless prohibited by the provisions of Regulation S of the 1933 Act, this material is distributed in the US, by NSI, a US-registered broker-dealer, which accepts responsibility for its contents in accordance with the provisions of Rule 15a-6, under the US Securities Exchange Act of 1934. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia (‘Saudi Arabia’) or a ‘Market Counterparty’ or a ‘Professional Client’ (as defined by the Dubai Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, Nlplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

Copyright © 2026 NOM International plc, UK. All rights reserved.
"""
