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
THE EM TRADER

# Curves, Chips, Crude and Carry

EM FX: Navigating Energy and Rate Risks. With the re-escalation of the Iran conflict, EM currencies have depreciated versus the Dollar, with energy importers once again underperforming and exporters outperforming. Still, the magnitude of FX moves has been smaller for a similar move in oil to that in March. We attribute this to (1) a more benign risk backdrop, which we think helps explain the better performance of high-beta BRL and COP, (2) the fact that FX had not fully retraced back to its pre-war levels, with many energy importers trading close to their weakest levels in early July, and (3) the underlying terms of trade shock being also smaller in magnitude, especially for CLP and PEN given copper price resilience. When linking FX moves to these fundamentals, we find that most EM currencies outperformed our model slightly during the recent re-escalation episode, contrasting with the sharp underperformance in early March. KRW and COP outperformance and ZAR, CLP and MXN underperformance stand out relative to our model's inputs.

Still a Path for RV Carry; Watching Carry-to-Vol Closely. The disruptive Fed hike tail looks to be curtailed for now, but there are still rate risks from a continued selloff in the long-end of the curve and high energy prices. The easiest way to resolve these risks is a sustained path to lower energy prices, but until that point EM FX carry structures will likely continue to balance risk and reward by choosing both longs and funders carefully, maximising carry-to-vol and monitoring closely local developments that can challenge carry returns. BRL and COP remain the strongest propositions by a wide margin in both carry and carry-to-vol terms, and also benefit from higher energy prices, but are vulnerable to higher long-end US yields (and BRL specifically to upcoming election noise). Within the next set of currencies with around 3% carry versus the Dollar (INR, IDR, MXN, ZAR), there are importance differences in carry-to-vol dynamics and local developments that lead us to prefer MXN carry (rising carry-to-vol, especially versus Euro, greater exposure to US growth and resilience to oil price fluctuations), followed by INR (high carry-to-vol and central bank support, but limited scope for appreciation) and ZAR (much lower carry-to-vol but equally greater scope for spot appreciation on a conflict resolution), while maintaining a more cautious view on IDR (due to domestic developments). HUF carry has declined substantially since the election, making it increasingly more of a spot than a carry trade. We maintain a constructive HUF outlook over the

## Kamakshya Trivedi

+44(20)7051-4005 |
kamakshya.trivedi@gs.com
GS International

Sunil Koul
+44(20)7051-4931 | sunil.koul@gs.com
GS International

Danny Suwanapruti
+65-6889-1987 |
danny.suwanapruti@gs.com
GS (Singapore) Pte

Teresa Alves
+44(20)7051-7566 |
teresa.alves@gs.com
GS International

Tarun Lalwani, CFA
+1(212)934-5821 |
tarun.lalwani@gs.com
GS India SPL

Victor Engel
+44(20)7051-3862 |
victor.engel@gs.com
GS International

Lexi Kanter
+1(212)855-9701 |
alexandra.kanter@gs.com
GS & Co. LLC

Mambuna Njie
+44(20)7051-7705 |
mambuna.njie@gs.com
GS International

medium term but think near-term dynamics look more challenging. Overall, our preferred funders in G10 are CHF, EUR, JPY and CAD in roughly that order, and in EM we think THB, ILS and PLN screen as attractive funders from both a carry and spot asymmetry perspective. CLP's low carry and high beta to risk and energy prices makes it an attractive funder for investors looking to neutralise broader risk exposures.

EM Local Rates: Fed up with Energy... Uncertainty around a sustainable resolution to the Iran war and the energy price volatility this creates remains the primary driver of EM and G10 rates. While cleaner positioning, benign inflation prints and EM central bank reaction functions that have turned out to be more dovish relative to market pricing at the start of the war have helped trim the more adverse tails in local rates pricing despite the recent bouts of energy price increases, we continue to think that any relief is likely to be limited until there is more visibility on the supply side factors. It is therefore important to be tactical and selective against this backdrop of still elevated commodity prices and the prospects for core central bank hikes.

... But the Fatigue Is Uneven. We prefer markets where rates have backed up and central banks lean dovish (PLN, HUF, ILS). Conversely, while we think EM Asia low-yielders (KRW, PHP) are pricing too much in the front-end, very accommodative real policy rates will likely keep hike pressures live. In LatAm, MXN is still vulnerable to Fed hikes given low rate differentials and high US front-end sensitivity; in BRL, despite the BCB's easing bias and attractive front-end in our view, high realised vol into the October elections keep us sidelined. Medium term, tight EM long-end spreads to the US and the possibility of elevated core duration (with a mild version emerging post-FOMC yesterday) limit the scope for broad-based long-end compression, except in select high-yielders with improving fiscal paths (INR, ZAR), or COP, which may join them.

EM Equities: Tech Unwind Extends, Non-Tech Resilient to Renewed Energy Shock. The EM equity index (MSCI EM) has retraced 12% from its late June peak, reversing about half of its strong 1H gains driven by ongoing unwinds in crowded tech and AI infrastructure stocks, and renewed escalation in the US-Iran conflict. While the tech unwind has extended in recent days, non-tech EM equities have shown a muted response to rising oil prices so far, with MSCI EM ex-tech up 2% in July. This resilience is supported by lower starting valuations and price levels in oil-sensitive markets, which remain meaningfully below pre-war levels. Furthermore, strong micro fundamentals have cushioned the downside as early 2Q results are tracking ahead of consensus estimates, with positive median earnings surprise – and beats outpacing misses – driving further EPS upgrades.

Still Expect EM Broadening on Improving Earnings and Diversification Appeal. While the global de-grossing in tech has accelerated in recent weeks amid investor fears around rising China competition, AI capex sustainability, and a high bar for 2Q tech earnings, we remain fundamentally constructive and expect continued strong profit growth in AI infrastructure stocks. Volatility could stay elevated in the near term, however, as leveraged positions, although reset from highs, have not fully cleared. As long as macro volatility related to oil and rates is contained, we continue to expect a broadening in EM equities beyond tech, supported by underlying earnings accrual and the regional diversification appeal of non-tech markets, as evidenced during past major TMT drawdowns.

EM Sovereign Credit Issuance: Robust in H1, With More to Come in H2. Despite concerns that large amounts of AI-related debt supply may be crowding out other sectors or countries, EM gross sovereign USD bond issuance has been robust so far this year, propelled by the forward spend on security and energy infrastructure by IG GCC sovereigns since the onset of the Iran war. Both EM IG and HY H1 issuance stand at their second-highest levels in a decade. Our core view is still that the drivers of such robust issuance include the prevalence of favourable issuance terms, with sovereigns taking advantage of tight spreads, and elevated investor demand for primary supply. Looking ahead, our updated full-year 2026 issuance forecast stands at \~US\$209bn, with the lion's share from IG (\~US\$138bn, 66%), and HY contributing \~US\$72bn (34%). While our forecasts appear consistent with a bullish risk-on scenario that is not our baseline, we think they reflect a strong technical backdrop and a large idiosyncratic issuance profile from IG GCC sovereigns. This gross supply should translate into elevated net supply by the end of the year, which should in turn contribute to the moderate spread widening we expect over the next 12 months.

## EM FX: Navigating Energy and Rate risks

Re-escalation relative performance consistent with, but smaller magnitude than, the initial shock. As oil prices rose through July (specifically, from the re-escalation of the US-Iran conflict on 6 July 2026 to the peak in oil prices on 23 July 2026), EM currencies generally depreciated versus the Dollar, with energy importers underperforming (especially those in CEEMEA and LatAm) and energy exporters (namely, COP and BRL) outperforming (Exhibit 1). These relative moves were largely consistent with the relative performance at the start of the conflict in early March, though KRW is a notable exception, BRL appreciated instead of depreciating and COP outperformed by more than in March. We noted that, while the oil move was similar over these July and March windows, broader risk did not sell off as much in July. We think this helps explain the smaller magnitude of the moves observed in July and the better performance of BRL and COP as energy exporters but equally high-beta currencies. Moreover, looking at where currencies were trading relative to their YTD range on July 6 (red diamonds in Exhibit 2), we find that most energy importers were close to their weakest levels, and had not recovered even as oil prices had fallen close to their pre-conflict levels. Most energy importers in Asia and CEEMEA (with the exception of CNH, KRW and HUF) are currently trading close to their weakest levels year-to-date.

Exhibit 1: EM FX responses have been broadly similar to the start of the war, but more muted overall, with a few notable outliers such as KRW and COP  
![](images/1a5d2ab9e8aea9e30344a741132416638720e912a80c2ffccbadd2c110f9409f.jpg)  
Source: Bloomberg, GS Global Investment Research

Exhibit 2: Many energy importers were trading close to their weakest levels YTD even before the re-escalation  
![](images/e92fa03f9124a6755ce551f6d89a5114726530b5db269bd3999909185ab8ac4b.jpg)  
Source: Bloomberg, GS Global Investment Research

Broader terms of trade shift also smaller than in early March, with many energy importers' indices above their weakest levels YTD. Looking more fundamentally at how terms of trade have shifted over this window in July versus at the start of the conflict, we also find that relative moves have been similar but the magnitudes have been smaller (Exhibit 3), which in our view can also help explain the smaller spot FX moves in energy importers (Exhibit 1). For CLP and PEN, the deterioration in terms of trade has been significantly smaller over the most recent window as copper prices have risen, whereas they had fallen in March. In level terms, our GS terms of trade indices are near their lowest levels for the year for many energy importers, especially HUF and ZAR, though still above their peak deterioration (Exhibit 4). Among the energy importers, CLP stands out again, with Chile's terms of trade not too far from the strongest levels YTD, and similarly INR and PLN terms of trade are far from their

weakest levels YTD.

Exhibit 3: Shifts in terms of trade have been similar to the start of the war in relative terms, although the overall magnitude has been smaller

![](images/ec2f9f5347e8e9e59e47d904b0c9a993921dbac2d54006acc6f870f771540e6e.jpg)  
Source: GS FICC and Equities, GS Global Investment Research

Exhibit 4: Terms of trade currently near their lowest YTD levels for many energy importers but CLP is key exception

![](images/ba6d254c3dbb8f2f089c8fa9caff3f5d693a6d7c87b74d3756b74e086aed4285.jpg)  
Source: GS FICC and Equities, GS Global Investment Research

\- Relative EM FX performance was broadly in line with model predictions, with oil prices the key factor driving relative performance. In order to marry FX market moves with these other developments, we refreshed our simple model of FX returns relative to other market developments (S&P 500, oil and copper prices, and US 10-year real yields) over this period between July 6 and 23; Exhibit 5 shows the ‘predicted’ returns of this model together with the contribution of each input and ‘actual’ returns. Overall, EM FX performance was broadly in line with model predictions, with oil prices the key factor driving relative performance. Energy exporters, such as BRL and COP, were the top performers, though COP outperformed the model-implied prediction whereas BRL slightly underperformed. Energy importers including ZAR, HUF, PLN, THB and PHP were the worst performers, but this can largely be explained by the model’s inputs, except for ZAR (more on this below). Compared with the initial energy shock in February, the deterioration in broader risk sentiment was more muted this time, resulting in a smaller overall depreciation across EM FX, as discussed above.

Exhibit 5: EM FX performance was broadly in line with model predictions, with oil prices the key factor driving relative performance

![](images/5747e21a5f5019e32bd91e1a88ea783e0f5b41c77b3af223f2e6cedd5bd989c5.jpg)

Predicted returns based on sensitivity of weekly FX returns vs USD to changes in the S&P, US 10-year real yields, oil and copper prices over the 5 years before February 27, 2026

Source: Bloomberg, GS Global Investment Research

Most currencies slightly outperformed the model's inputs, with some exceptions. In Exhibit 6, we plot model-predicted returns on the x-axis against actual FX performance on the y-axis. In contrast to the first energy shock in February, when many currencies underperformed their model-implied returns, most EM currencies outperformed during the recent US-Iran re-escalation episode (i.e., lying above the 45-degree line). As discussed above, we think this partly reflects the fact that FX had not fully retraced from the initial shock prior to the renewed escalation and terms of trade shifts were broadly smaller than in March. There were, however, a few notable exceptions, with KRW and COP among the largest outperformers and ZAR, CLP and MXN among the largest underperformers (i.e., furthest away from the 45-degree line). We think these deviations can be explained by idiosyncratic developments. The KRW appreciation this month coincided with policy tightening, measures to curb leverage, and capital inflows associated with reduced equity-related outflows. For COP, continued optimism following the election and expectations of further policy rate hikes have provided support to the Peso beyond the boost from higher oil prices, in our view. By contrast, ZAR underperformed the most relative to model-implied returns, reflecting the SARB's against-consensus decision to keep interest rates on hold. CLP also underperformed relative to the model despite limited local developments. While the direction of the move is consistent with the shift in terms of trade, we believe the move may have gone too far relative to fundamentals, given that the deterioration in ToT has been significantly less severe than during the first energy shock in February.

Exhibit 6: Most EM currencies outperformed model-implied returns based on other market variables during the recent US-Iran re-escalation episode

![](images/da4882b7c5683425897297ccf896e43affecc76528c0965130320b94a147ca51.jpg)  
Source: Bloomberg, GS Global Investment Research

Still a path for RV carry between energy and rate risks, watching carry-to-vol closely. The disruptive Fed hike tail looks to be curtailed for now, especially given our economists' expectations for relatively soft upcoming inflation prints, but there are still rate risks from a continued selloff in the long-end of the curve and high energy prices. The easiest way to resolve these risks is a sustained path to lower energy prices, but until that point EM FX carry structures will likely continue to balance risk and reward by choosing both longs and funders carefully, maximising carry-to-vol and monitoring closely local developments that can challenge carry returns. Looking at carry and carry-to-vol ratios, BRL and COP remain the strongest propositions by a wide margin (Exhibit 7) and this is also the case in carry-to-vol terms versus the Dollar (Exhibit 8). Set against this high carry and positive exposure to energy prices, these currencies' high betas to US long-end yields are a key vulnerability. Between the two, the upcoming pick-up in election noise in Brazil and continuation of a rate cutting cycle (whereas BanRep in Colombia is likely to deliver another hike this week) lead us to prefer COP longs over BRL here. Within the next set of currencies with around $3\%$ carry versus the Dollar (INR, IDR, MXN, ZAR), there are importance differences in carry-to-vol dynamics and local developments that lead us to prefer MXN carry followed by INR and ZAR, while maintaining a more cautious view on IDR due to domestic developments. MXN stands out from a carry-to-vol perspective, especially versus the Euro where this ratio has been steadily increasing (Exhibit 9). Moreover, the Peso's relative resilience to energy price shifts and exposure to US cyclical pricing argue for MXN carry longs. USMCA negotiation risks and a dovish Banxico in a hawkish Fed scenario are the main risks to this view, but our base case is for no Fed hikes and for USMCA negotiations to be less contentious for Mexico than for Canada. INR's carry-to-vol has also been rising supported by the RBI's measures to mitigate FX depreciation pressures, though this

also means the scope for spot appreciation is more limited, in our view. Moreover, INR remains vulnerable to a more disruptive energy price scenario, although we think pairing INR longs with THB shorts (where we maintain a bearish view) can help neutralise this exposure to a large extent. ZAR carry-to-vol is significantly lower than for its peers. On one hand, higher volatility means that the Rand can outperform in an energy relief scenario, but equally that it is not the most attractive carry long in a more uncertain backdrop, especially if central bank support is also less certain than before. HUF carry and carry-to-vol has declined substantially since the election as rates have moved lower. We expect this yield convergence to the Euro area to continue, which means HUF longs are increasingly more of a spot than a carry trade. We maintain a constructive HUF outlook over the medium term, and forecast spot appreciation to 350 in EUR/HUF in 6 months. However, with limited central bank support and energy supply, a

[中间内容因长度限制已省略]

 have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global

Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
