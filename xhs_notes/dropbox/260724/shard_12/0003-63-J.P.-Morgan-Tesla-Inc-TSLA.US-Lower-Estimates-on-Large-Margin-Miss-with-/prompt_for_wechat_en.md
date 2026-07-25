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
Style Exposure

## Tesla Inc

Lower Estimates on Large Margin Miss with Investments Ramping; FSD Subscriptions Rising and Robotaxi on Track, That Should Drive Positive Feedback Loops and Eventual EPS Inflection

TSLA's 2Q26 results came in well below both JPMe and company-compiled consensus on EBIT and EPS (Table 1), largely driven by softer than anticipated gross margins, with the shortfall driven by a combination of lower regulatory credits, rising interest rate subvention costs, warranty headwinds in ESS, and commodity cost headwinds. Underlying automotive gross margins ex-regulatory credits were flat q/q when adjusting for one-time items in 1Q related to warranty and tariff relief, helping alleviate concerns that recent volume strength (see here for our take on 2Q deliveries) was purely incentive-driven. FSD is increasingly becoming a key purchase consideration (subscriptions +15% q/q), a dynamic we have consistently highlighted as fueling positive feedback loops for both sales and ongoing autonomous technology improvement. Robotaxi operations continue to scale, with recent expansions into Orlando and Tampa, and management provided greater clarity around TSLA's approach, prioritizing miles over vehicles, while remaining measured given the regulatory and media spotlight, as well as the ongoing validation of cybercab and the pending release of FSD v15 (see our recent robotaxi deep-dive) - the key takeaway is that unsupervised robotaxi miles are ramping (up 10% w/w since Jan 2026), with the safety record to date remaining solid. Elsewhere, a key highlight was strength in service margins and related profit growth, which we expect to see continued tailwinds as FSD subscriptions rise, coupled with infrastructure leverage. Optimus supply chain ramp is progressing as SoP approaches, though management cautioned that the S-curve ramp will be relatively more protracted and flat initially, a function of the near-total novelty of the componentry and the absence of any incumbent supply chain. The energy storage segment is increasingly being positioned to capture data center and broader electrification demand and backlog remains strong, though with an increasingly crowded industrial storage landscape, long-term gross margin targets continue to be revised down, now expected in the low to mid 20s. Capital spending remains elevated, with management reiterating a \$25 bn+ capex target for 2026 (\~\$8.2 bn YTD), and the return profile is expected to be non-linear as vertical integration and compute infrastructure investments begin to yield results. Finally, on the topic of potential merger with SPCX (click here for our prior thoughts), CEO Musk stopped short of explicit comments though clearly laid out strategic overlap between the two companies. Net-net, we believe TSLA shares are likely to remain range-bound near-term as forward estimate revisions continue to find a bottom as investments ramp, though we continue to see downside support as broader robotaxi rollout nears, Cybercab production ramps, and automotive volume shows signs of sustained re-acceleration, keeping the eventual EPS inflection and SoTP unlock potential intact.

\- Estimate changes (Table 10). We lower our 2026/2027 EPS forecasts to \$1.60/\$1.70 vs. \$2.15/\$2.20 prior (consensus \$1.99/\$2.49), primarily driven by softer automotive gross margin assumptions and higher opex. Our 2030 EPS forecast, off of which we base our P/E based valuation (\~50% component of our overall valuation methodology with the remaining \~50% being a SoTP based), similarly moves lower to \$6.60 from \$7.50 prior, and our Dec 2027

Sources for: Style Exposure – JPM Global Markets Strategy; all other tables are company data and JPM estimates. See page 35 for analyst certification and important disclosures.

Neutral

TSLA, TSLA US
Price (22 Jul 26):\$374.01

▼Price Target (Dec-27):\$445.00
Prior (Dec-27):\$475.00

## Autos & Auto Parts

Rajat Gupta AC
(1-212) 622-6382
rajat.gupta@JPM.com

Jash Patwa
(1-212) 622-5472
jash.patwa@jpmchase.com

Yash Beswala
(1-212) 622-0028
yash.beswala@jpmchase.com
JPM Securities LLC

<table><tr><td colspan="4">Key Changes (FYE Dec)</td></tr><tr><td></td><td>Prev</td><td>Cur</td><td>Δ</td></tr><tr><td>Adj. EPS - 26E ($)</td><td>2.15</td><td>1.60</td><td>-25.4%</td></tr><tr><td>Adj. EPS - 27E ($)</td><td>2.20</td><td>1.70</td><td>-22.5%</td></tr></table>

<table><tr><td>Adj. EPS ($)</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>Q1</td><td>0.27</td><td>0.41A</td><td>0.28</td></tr><tr><td>Q2</td><td>0.40</td><td>0.33A</td><td>0.43</td></tr><tr><td>Q3</td><td>0.50</td><td>0.49</td><td>0.53</td></tr><tr><td>Q4</td><td>0.50</td><td>0.38</td><td>0.45</td></tr><tr><td>FY</td><td>1.66</td><td>1.60</td><td>1.70</td></tr></table>

<table><tr><td rowspan="2">Quant Factors</td><td rowspan="2">Current %Rank</td><td colspan="4">Hist %Rank (1=Top)</td></tr><tr><td>6M</td><td>1Y</td><td>3Y</td><td>5Y</td></tr><tr><td>Value</td><td>96</td><td>96</td><td>94</td><td>92</td><td>91</td></tr><tr><td>Growth</td><td>70</td><td>65</td><td>18</td><td>48</td><td>43</td></tr><tr><td>Momentum</td><td>53</td><td>35</td><td>73</td><td>19</td><td>79</td></tr><tr><td>Quality</td><td>39</td><td>66</td><td>32</td><td>9</td><td>38</td></tr><tr><td>Low Vol</td><td>67</td><td>80</td><td>85</td><td>78</td><td>70</td></tr><tr><td>ESGQ</td><td>37</td><td>30</td><td>90</td><td>10</td><td>31</td></tr></table>

Price Performance  
![](images/66e5fb85687111b41de229ee77296e1938b77b62510e0180c6fc3cfe7280da55.jpg)

— TSLA Price (\$) — RTY (rebased)

<table><tr><td></td><td>YTD</td><td>1m</td><td>3m</td><td>12m</td></tr><tr><td>Abs</td><td>-16.8%</td><td>-7.7%</td><td>-3.5%</td><td>12.6%</td></tr><tr><td>Rel</td><td>-36.1%</td><td>-6.2%</td><td>-9.8%</td><td>-19.0%</td></tr></table>

<table><tr><td colspan="2">Company Data</td></tr><tr><td>Shares O/S (mn)</td><td>3,756</td></tr><tr><td>52-week range ($)</td><td>498.83-297.82</td></tr><tr><td>Market cap ($ mn)</td><td>1,404,678.00</td></tr><tr><td>Exchange rate</td><td>1.00</td></tr><tr><td>Free float (%)</td><td>88.9%</td></tr><tr><td>3M ADV (mn)</td><td>48.65</td></tr><tr><td>3M ADV ($ mn)</td><td>19,622.7</td></tr><tr><td>Volatility (90 Day)</td><td>48</td></tr><tr><td>Index</td><td>RUSSELL 2000</td></tr><tr><td>BBG ANR (Buy | Hold | Sell)</td><td>29|25|9</td></tr></table>

Key Metrics (FYE Dec)

<table><tr><td>$ in millions</td><td>FY25A</td><td>FY26E</td><td>FY27E</td><td>FY28E</td></tr><tr><td colspan="5">Financial Estimates</td></tr><tr><td>Revenue</td><td>94,827</td><td>109,825</td><td>123,319</td><td>145,106</td></tr><tr><td>Adj. EBITDA</td><td>10,503</td><td>9,063</td><td>10,751</td><td>15,971</td></tr><tr><td>Adj. EBIT</td><td>4,355</td><td>2,254</td><td>2,551</td><td>6,671</td></tr><tr><td>Adj. net income</td><td>5,858</td><td>5,694</td><td>6,184</td><td>9,097</td></tr><tr><td>Net margin</td><td>6.2%</td><td>5.2%</td><td>5.0%</td><td>6.3%</td></tr><tr><td>Adj. EPS</td><td>1.66</td><td>1.60</td><td>1.70</td><td>2.45</td></tr><tr><td>BBG EPS</td><td>1.61</td><td>1.98</td><td>2.51</td><td>3.46</td></tr><tr><td>Cashflow from operations</td><td>14,747</td><td>13,055</td><td>12,568</td><td>16,630</td></tr><tr><td>FCFF</td><td>7,200</td><td>(9,223)</td><td>(11,000)</td><td>(8,310)</td></tr><tr><td colspan="5">Margins and Growth</td></tr><tr><td>Revenue Growth Y/Y (%)</td><td>(2.9%)</td><td>15.8%</td><td>12.3%</td><td>17.7%</td></tr><tr><td>EBITDA margin</td><td>11.1%</td><td>8.3%</td><td>8.7%</td><td>11.0%</td></tr><tr><td>EBITDA Growth Y/Y (%)</td><td>(15.6%)</td><td>(13.7%)</td><td>18.6%</td><td>48.6%</td></tr><tr><td>EBIT margin</td><td>4.6%</td><td>2.1%</td><td>2.1%</td><td>4.6%</td></tr><tr><td>Adj. EPS growth</td><td>NM</td><td>NM</td><td>6.1%</td><td>43.9%</td></tr><tr><td colspan="5">Ratios</td></tr><tr><td>Adj. tax rate</td><td>27.0%</td><td>23.1%</td><td>25.5%</td><td>25.2%</td></tr><tr><td>Interest cover</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net debt/Equity</td><td>NM</td><td>0.0</td><td>0.1</td><td>0.2</td></tr><tr><td>Net debt/EBITDA</td><td>NM</td><td>0.3</td><td>1.3</td><td>1.4</td></tr><tr><td>ROCE</td><td>3.7%</td><td>1.8%</td><td>1.6%</td><td>3.6%</td></tr><tr><td>ROE</td><td>7.5%</td><td>6.6%</td><td>6.6%</td><td>8.9%</td></tr><tr><td colspan="5">Valuation</td></tr><tr><td>FCFF yield</td><td>0.5%</td><td>(0.7%)</td><td>(0.8%)</td><td>(0.6%)</td></tr><tr><td>Dividend yield</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>EV/EBITDA</td><td>132.8</td><td>155.3</td><td>132.0</td><td>89.4</td></tr><tr><td>EV/Revenue</td><td>14.7</td><td>12.8</td><td>11.5</td><td>9.8</td></tr><tr><td>Adj. P/E</td><td>225.1</td><td>233.2</td><td>219.9</td><td>152.8</td></tr></table>

## Summary Investment Thesis and Valuation

## Investment Thesis

TSLA sits at the forefront of physical AI entering uncharted TAMs where execution will be key to accelerating adoption and expanding those TAMs (the Jevons paradox). Its underappreciated edge is deep vertical integration across hardware + software, paired with speed of technology development: using factories as a test bed for Optimus should lower auto COGS and validate Humanoids at industrial scale (US/Global TAM of \~5 mn/30 mn by 2040E), a flywheel analogous to AWS/Kiva at AMZN. In robotaxi, >10 bn miles recorded and 9 mn personal fleet on road today should drive network-effects across robotaxi and FSD adoption (35 mn personal TSLA fleet and 40 mn robotaxis by 2040E), while Energy Storage benefits from data center and grid tailwinds, and the base infrastructure can be monetized via FSD/Optimus licensing, distributed inference, Cortex compute, and supercharger usage. We see EPS inflection in 2028+ and a 50%+ growth CAGR through 2030 and beyond, with implied SoTP of \$3.9T by 2035E. Valuation on near-term earnings is clearly lofty, but we think TSLA deserves the benefit of the doubt on LT earnings given new TAMs are unlikely to inflect until 2029+, with shares in the interim likely tied to robotaxi/Optimus data points and potential index diversification offering a better entry point, in our view.

## Valuation

We rate TSLA shares Neutral with a \$445 December 2027 price target.

![](images/5116c669e982e3789a594be9fa9ec68441a47297244a6b6cb5973ff2682d411c.jpg)

<table><tr><td>Factors</td><td>6M Corr</td><td>1Y Corr</td></tr><tr><td>Market: MSCI US</td><td>0.59</td><td>0.58</td></tr><tr><td>Sect: Cons Discretionary</td><td>0.48</td><td>0.61</td></tr><tr><td>Ind: Automobiles &amp; Comp</td><td>0.99</td><td>1.00</td></tr><tr><td>Macro:</td><td></td><td></td></tr><tr><td>US 10yr yield</td><td>-0.04</td><td>-0.20</td></tr><tr><td>Economic Surprise</td><td>-0.21</td><td>0.16</td></tr><tr><td>US Dollar</td><td>-0.19</td><td>0.10</td></tr><tr><td>Quant Styles:</td><td></td><td></td></tr><tr><td>LowVol</td><td>-0.49</td><td>-0.24</td></tr><tr><td>Value</td><td>-0.21</td><td>-0.14</td></tr><tr><td>DivYld</td><td>-0.26</td><td>-0.14</td></tr></table>

price target relatedly moves lower to \$445 from \$475 prior.

\- 2Q26 results summary (Table 1). Overall 2Q26 revenue was \$28.2 bn vs. JPMe/ company-compiled consensus \$28.2/\$27.6 bn, with automotive revenue of \$20.5 bn vs. JPMe \$20.4 bn. Blended automotive ASPs tracked \$41.6K, \~1% below JPMe of \$42.2K. Service revenue was \$4.6 bn vs. JPMe \$4.1 bn, while Solar & Energy Storage revenue were \$3.1 bn vs. JPMe \$3.7 bn. Automotive regulatory credits related revenue was \$146 mn vs, JPMe \$325 mm. Non-GAAP automotive gross margins tracked 18.1% (16.3% ex-regulatory credits) vs. JPMe 21.6% (19.5% ex-regulatory credits). Overall EBIT tracked at \$398 mn vs, JPMe \$1,619 mn and consensus for \$1,503 mn. EPS was \$0.33 vs. JPMe/consensus \$0.60/\$0.55.

\- Robotaxi scaling tracking well ahead of fleet size, with a clean safety record to date. TSLA reported >380K cumulative unsupervised robotaxi miles across six cities and two states with zero notable incidents to date, which management frames as validation of its camera-only stack that forgoes lidar, radar, and HD maps. Unsupervised miles are compounding >10% w/w since Jan 2026, with the focus on mileage rather than vehicle count reflecting near-continuous fleet utilization that generates substantial miles even off a modest base. The city-by-city expansion, now across seven US metros, is a deliberate choice to prove stack generality across varied environments and clear fragmented state and local requirements rather than a capacity constraint, with time-to-launch per new city trending lower and an eventual shift to state-wide operation roll-outs over time. Cybercab entered production at Gigafactory Texas, with an installed capacity of >125K units/year (\~25x Zoox's capacity and \~3-5x higher than Waymo), though near-term fleet counts remains suppressed as the new chassis first accumulates its own calibration miles via retrofitted units. The fleet already runs an early V15 build, shared across Model Y and Cybercab, and management flagged no imminent federal regulatory unlock is required, characterizing the NHTSA relationship as constructive. The binding constraint on scaling is reliability rather than demand or regulation, reinforced by the company's deliberately cautious pace given the outsized regulatory and media scrutiny a single incident would attract.

\- No explicit comment on a SPCX combination, but strategic overlaps were clearly laid out. TSLA sidestepped directly commenting on a potential merger with TSLA, citing the need for a proper process, yet pointed to a widening set of ties that collectively sketch the case for closer integration, spanning the existing equity stake and framework agreement, Grok orchestrating digital Optimus and embedded in vehicles, Starlink embedding into Cybercab and eventually the broader fleet to guarantee connectivity for autonomous operation, and growing overlap on the chip fabrication initiatives. We had previously outlined our puts and takes around a potential combination (click here for our detailed thoughts), and we see TSLA's caution on robotaxi-related media and regulatory scrutiny underscoring another incremental risk, primarily reputational but potentially financial, that could span a wider organization were a combination to materialize.

\- FSD increasingly provind to be a demand engine; Gross margin drag a function of lower regulatory credits, rates and non-repeat of 1Q tailwinds and ongoing commodity inflation. TSLA observed demand resurgence in 2Q (total deliveries up +25% y/y, see our initial take) led by FSD, which is increasingly becoming a primary factor in the purchase consideration process and points to repeatable demand uplift in other markets as the technology gains regulatory approval. On gross margins (automotive gross margins ex-regulatory credits tracked 16.3% vs. JPMe 19.5%), which were a key driver of the 2Q miss, management noted that automotive gross margins ex-regulatory credits tracked flat q/q, when adjusting for non-recurring warranty true-downs (\~\$230 mn) and tariff benefits in 1Q, indicating pricing and cost discipline. Besides this, gross margins also reflected a growing drag from interest rate subvention costs (as interest rates moved higher q/q in 2Q) and commodity inflation. All-in, demand remains robust, with TSLA's order backlog scaling to its highest level since 2023, and TSLA is ramping up

production to meet stronger demand.

\- FSD attach rates ramp to 55% in North America. FSD revenue split is \~55%/45% upfront purchases/subscriptions, albeit the cessation of upfront purchase option earlier this year continues to drive a higher mix towards a recurring base of subscription revenue. Attach rates remain strong, tracking at \~55% in North America and trending upwards (vs. \~30-35% penetration management indicated as a reasonable ballpark at the time of 1Q earnings). Notably, active FSD subscriptions tracked higher to \~1.5 mn users, up from \~1.3 mn in 1Q, and with just \~31 mn miles coming from new European FSD markets, there appears to be a clear acceleration in FSD miles driven per subscriber, indicating improved reliability and functionality. For context, \~500 mn cumulative FSD miles were added between early March through early April, indicating \~390 incremental monthly miles/subscriber (using the 1Q subscriber base), whereas between late June and late July, FSD miles scaled by \~800 mn, indicating \~540 incremental monthly miles/subscriber. Lastly, TSLA also sees FSD extending to the Semi by 2026-end/early-2027.

\- \$25 bn+ 2026 capex guidance reiterated. FCF was an outflow of -\$1.1 bn, with capex tracking at \$5.8 bn (up \~132% q/q, \~\$8.2 bn YTD) and TSLA reiterated 2026 capex of \$25 bn+ with continued growth expected over the next 2-3 years across the robotaxi fleet, Optimus, semiconductor fab, solar, and AI compute. Notably, TSLA is opportunistically securing debt facilities providing up to \$30 bn of incremental borrowing capacity to fund investments.

\- Optimus progress continues with Fremont line installation underway. TSLA reiterated the anticipated S-curve for Optimus production, which is expected to be relatively more protracted and flat initially, a function of the near-total novelty of the componentry and the absence of any incumbent supply chain, that has compelled extensive in-housing at the Fremont line that replaced the decommissioned Model S/X capacity. The early builds are earmarked for the Optimus Academy, where they seed a two-stage data flywheel entailing factory workers and a dedicated demonstration team supplying high-quality training data atop internet-scale video, followed by reinforcement learning as the fleet practices tasks to convergence. Regarding the supply chain, a substantial mix of specialized power electronics for the Gen 3 are designed in-house but fabricated externally, whereas the Austin-built Gen 4 humanoids are expected to be more vertically integrated. TSLA emphasized that suppliers are investing alongside the company to develop the domestic humanoid supply chain, specifically highlighting Samsung, TSMC and Panasonic.

\- Energy storage gross margins normalize lower. Energy storage deployment strength (13.5 GWh in 2Q, +41% y/y) was attributed to a mix of timing impact related to customer deployment timelines as well as solid EMEA deployment trends, supported by Megafactory Shanghai ramp, with Megapack 3 production expected to start soon at the new Texas Megafactory. Energy storage gross margins moderated to \~20.4% from 39.5% in 1Q, which TSLA attributed to a \~\$240 mn vendor battery cell warranty true-up on legacy deployments, the non-recurrence of \~\$200 mn in 1Q t

[中间内容因长度限制已省略]

ates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 23 Jul 2026 03:40 AM EDT

Disseminated 23 Jul 2026 03:41 AM EDT
"""
