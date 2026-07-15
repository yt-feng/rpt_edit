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
RIC: 002008.SZ BBG: 002008 CS

# Han's Laser Technology Industry Strength across all business lines, reiterate Buy

## H126 preliminary results were a strong beat

In its preliminary results, the company reported that H126 net profit rose by 156.1% to 176.6% YoY, representing a strong beat versus both our and Reuters consensus forecasts of 109% YoY. The strong growth was mainly owing to: 1) strong revenue growth (likely up 68% YoY), led by its core PCB and CE equipment business; and 2) improved recurring profitability (pre-exceptional NPM was up 9ppts YoY, based on the mid-point of the guidance). We continue to see the PCB and CE equipment segments as sustainable drivers, as we highlighted in our upgrade report (link), with growth momentum rising on the back of ultrafast laser drilling equipment for high-end HDI (High-Density Interconnector) and mSAP (Modified Semi-Additive Process) PCB, and Apple's solid procurement demand, in our view. PCB and CE equipment aside, solid demand was seen across other businesses, such as battery, pan-semi and other laser equipment. After factoring in the strong preliminary results for H126 and updating our assumptions for its major businesses, our earnings forecasts for 2026-28E rise by 22-74%, and we raise our price target to Rmb193.30 from Rmb92.00. We maintain our Buy rating given its solid fundamentals and attractive valuation (0.84x PEG based on 24x 2027E PE and 28% EPS CAGR for 2027-29E).

## Strong performance across all business lines

PCB equipment H126 revenue was up over 100% YoY, driven by strong downstream demand and product mix improvement (including high-precision back drilling and ultrafast laser drilling equipment). The adoption of ultrafast laser drilling equipment has been faster than we expected, mainly driven by AI PCB and 1.6T optical transceiver demand. We think this growth momentum will continue in 2026-28, driven by more advanced PCB equipment applications, continued market share gains and product mix upgrades. CE equipment revenue was up more than 180% YoY in 1H26, likely driven by its largest customer, Apple, in our view. We see further upside in H226, led by foldable smartphone and 3D printing equipment adoption. Among other businesses, batteries/pan-semis/general purpose laser equipment revenue was up 45%/40%/30% YoY in H126, driven by growing AI exposure, we believe.

## Earnings forecast changes

We revise up our earnings forecasts for 2026-28E by 22-74%, reflecting 16-40% higher revenue forecasts and 2-4 ppts higher blended GPM forecasts mainly to account for the improved product mix.

## Valuation: Lifting our price target to Rmb193.30, maintain Buy

We raise our PE-based price target from Rmb92.00 to Rmb193.30, reflecting: 1) our higher EPS forecasts; and 2) an increase in our target PE multiple from 26x to 35x, implying an unchanged 1.2x PEG ratio. As we think that its growth cycle is likely to sustain in H226-2028, we still see its valuation as attractive.

## Equities

<table><tr><td>China</td></tr><tr><td>Industrial, Diversified</td></tr></table>

12-month rating Buy

12m price target Rmb193.30

Price (10 Jul 2026) Rmb130.30

Trading data and key metrics

<table><tr><td colspan="2">Trading data and key metrics</td></tr><tr><td>52-wk range</td><td>Rmb152.80-24.22</td></tr><tr><td>Market cap.</td><td>Rmb134b/US$19.8b</td></tr><tr><td>Shares o/s</td><td>1,030m (ORDA)</td></tr><tr><td>Free float</td><td>93%</td></tr><tr><td>Avg. daily volume (&#x27;000)</td><td>59,903</td></tr><tr><td>Avg. daily value (m)</td><td>Rmb7,622.5</td></tr><tr><td>Common s/h equity (12/26E)</td><td>Rmb20.1b</td></tr><tr><td>P/BV (12/26E)</td><td>6.7x</td></tr><tr><td>Net debt to EBITDA (12/26E)</td><td>NM</td></tr></table>

EPS (UBS, diluted) (Rmb)

<table><tr><td></td><td>From</td><td>To</td><td>% ch</td><td>Cons.</td></tr><tr><td>12/26E</td><td>2.39</td><td>2.90</td><td>22</td><td>2.36</td></tr><tr><td>12/27E</td><td>3.54</td><td>5.52</td><td>56</td><td>3.44</td></tr><tr><td>12/28E</td><td>4.28</td><td>7.43</td><td>74</td><td>4.03</td></tr></table>

Jimmy Yu
Analyst
S1460517080002
jimmy.yu@ubs.com
+86-21-3866 8880

Yongwei Lai
Analyst
S1460524110001
yongwei.lai@ubs.com
+86-21-3866 8780

Qing Luo
Associate
S1460125090001
qing-za.luo@ubs.com
+86-213-866 5000

<table><tr><td>Highlights (Rmbm)</td><td>12/23</td><td>12/24</td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td><td>12/29E</td><td>12/30E</td></tr><tr><td>Revenues</td><td>14,091</td><td>14,771</td><td>18,759</td><td>29,257</td><td>39,809</td><td>47,699</td><td>53,076</td><td>59,160</td></tr><tr><td>EBIT (UBS)</td><td>82</td><td>(50)</td><td>888</td><td>3,385</td><td>6,313</td><td>8,456</td><td>10,183</td><td>12,141</td></tr><tr><td>Net earnings (UBS)</td><td>820</td><td>1,694</td><td>1,190</td><td>2,987</td><td>5,685</td><td>7,653</td><td>9,352</td><td>11,237</td></tr><tr><td>EPS (UBS, diluted) (Rmb)</td><td>0.78</td><td>1.61</td><td>1.15</td><td>2.90</td><td>5.52</td><td>7.43</td><td>9.08</td><td>10.91</td></tr><tr><td>DPS (net) (Rmb)</td><td>0.20</td><td>0.34</td><td>0.20</td><td>0.50</td><td>0.96</td><td>1.29</td><td>1.57</td><td>1.89</td></tr><tr><td>Net (debt) / cash</td><td>3,869</td><td>3,052</td><td>2,984</td><td>2,592</td><td>4,763</td><td>9,179</td><td>15,940</td><td>24,170</td></tr></table>

<table><tr><td>Profitability/valuation</td><td>12/23</td><td>12/24</td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td><td>12/29E</td><td>12/30E</td></tr><tr><td>EBIT (UBS) margin %</td><td>0.6</td><td>(0.3)</td><td>4.7</td><td>11.6</td><td>15.9</td><td>17.7</td><td>19.2</td><td>20.5</td></tr><tr><td>ROIC (EBIT) %</td><td>0.7</td><td>(0.4)</td><td>6.5</td><td>21.7</td><td>33.7</td><td>39.6</td><td>44.1</td><td>49.7</td></tr><tr><td>EV/EBITDA (UBS core) x</td><td>72.5</td><td>91.5</td><td>22.1</td><td>33.8</td><td>18.8</td><td>13.8</td><td>11.0</td><td>8.7</td></tr><tr><td>P/E (UBS, diluted) x</td><td>32.1</td><td>13.2</td><td>26.6</td><td>44.9</td><td>23.6</td><td>17.5</td><td>14.3</td><td>11.9</td></tr><tr><td>Equity FCF (UBS) yield %</td><td>(0.4)</td><td>(1.2)</td><td>2.6</td><td>(0.1)</td><td>2.0</td><td>4.0</td><td>6.0</td><td>7.3</td></tr><tr><td>Dividend yield (net) %</td><td>0.8</td><td>1.6</td><td>0.7</td><td>0.4</td><td>0.7</td><td>1.0</td><td>1.2</td><td>1.4</td></tr></table>

Source: Company accounts, LSEG Eikon, UBS estimates. Metrics marked as (UBS) have had analyst adjustments applied. Valuations: based on an average share price that year, (E): based on a share price of Rmb 130.30 on 10-Jul-2026

This report has been prepared by UBS Co. Limited. ANALYST CERTIFICATION AND REQUIRED DISCLOSURES, INCLUDING INFORMATION ON THE QUANTITATIVE RESEARCH REVIEW PUBLISHED BY UBS, BEGIN ON PAGE 14.

## UBS-S Research THESIS MAP a guide to our thinking and what's where in this report

## Q: Could Han's Laser's PCB equipment sustain 60%-plus growth in 2025-28E driven by new applications and customers?

Likely. We see multiple drivers that could boost its PCB equipment revenue, including substantially higher demand from AI&HPC applications, strong new capacity expansion plans from Chinese PCB suppliers, and Han's Laser's market share gains along with product mix upgrade. We forecast its PCB equipment revenue to achieve a 62% CAGR in 2025-28.

## Q: Could the consumer electronics business resume 50%+ revenue growth in 2025-28?

Likely. Driven by its largest customer's product innovation cycle and a broadening range of laser applications, we expect Han's Laser's CE business revenue to achieve a 50% CAGR in 2025-28.

## Q: Will Han's Laser's blended GPM continue to improve in 2025-28?

Yes. With a rising revenue contribution from high-margin PCB and consumer electronics equipment, we expect Han's Laser's blended GPM to improve by 6ppts over 2025-28.

After factoring in strong Q226 preliminary results and our latest industry discussion feedback, we revise up our revenue/earnings forecast by 16-40%/22-74% in 2026-28E, respectively, and lift our price target to Rmb193.30 from Rmb92.00. We estimate its PCB equipment/CE business revenue to grow at 63%/99% 2025-27E CAGR. We expect: 1) its high-value-added PCB equipment to penetrate into more AI PCB manufacturers ahead; 2) its leading global CE customer's innovation and new product cycle to drive increasing laser applications; 3) its other businesses, such as fibre, pan-semiconductor and low-power laser, are likely to contribute increasing revenue owing to their growing AI exposure. Factoring in these positives, we expect its net earnings to grow 151%/90% in 2026/2027, after a 30% decline in 2025.

PCB business: Han's CNC's NPM has grown from 10%/17% in Q225/Q126 to 20% in Q226E, owing to its product mix upgrade. Major AI PCB players, Victory Giant and Avary, have provided a positive capex outlook for 2026 (up 172% and 154% YoY, respectively) after industry capex doubled in 2025. Newly announced capex on industry AI PCB capacity expansion exceeds Rmb100bn. Han's CNC was Victory Giant's second largest supplier in 2025, with total PCB equipment shipments of Rmb1.27bn, accounting for 20% of Victory Giant's total capex. Consumer electronics business: Han's Laser's consumer electronics business recorded more than 180% YoY revenue growth in H126. We see its largest North America customer entering a flagship product cycle again.

Han's Laser is trading at 24x 2027E PE multiple (against our forecast of a 28% EPS CAGR for 2027-29E), which is significantly lower than its closest peers. We think its valuation is attractive at this level, considering its robust growth outlook in the next 2-3 years. Our 35x target PE multiple is 1.6x SD above its historical average PE of 28x, which we think is justified given its solid earnings growth outlook.

![](images/061a26cf2fd0ffdfe3d2c985714d4facbee4cab8627d8335bfddcce1d20f1344.jpg)

<table><tr><td>Value drivers(2025-27E)</td><td>PCB equipment sales CAGR</td><td>CE equipment sales CAGR</td><td>Other sales CAGR</td><td>Blended GPM (2027E)</td><td>SG&amp;A expense ratio (incl. R&amp;D, 2027E)</td></tr><tr><td>Rmb282.00 upside</td><td>80%</td><td>120%</td><td>30%</td><td>40%</td><td>20%</td></tr><tr><td>Rmb193.30 base</td><td>63%</td><td>99%</td><td>18%</td><td>38%</td><td>20%</td></tr><tr><td>Rmb51.00 downside</td><td>30%</td><td>20%</td><td>0%</td><td>33%</td><td>23%</td></tr></table>

Source: UBS-S estimates. Note: Data as of 10 July 2026.

Han's Laser Technology Industry (Han's Laser) is a market and technology leader in laser-related equipment in China. The company was the largest PCB equipment supplier in the global market in 2025, and is a major supplier of laser equipment for consumer electronics applications.

## Q226 preliminary results

Based on the preliminary results, H126 net profit rose by 156.1% to 176.6% YoY, implying a strong beat compared with both our and Reuters consensus forecasts of around 109% YoY growth. Revenue performance was strong across all business segments:

\- PCB equipment: Han's Laser's PCB equipment revenue grew by more than 100% YoY growth in H126, implying around 100% YoY revenue growth in Q226. The growth was driven by increasing high-value-added equipment shipments, including high-precision back drilling machines and mSAP ultrafast laser drilling solutions. According to Han's CNC (Han's Laser's PCB equipment subsidiary), the PCB equipment business is likely to achieve an NPM of around 20% in Q226 (vs 10%/17% in Q225/Q126), reflecting a significant improvement in the product mix.

\- Consumer electronics equipment: Han's Laser's consumer electronics business recorded growth in revenue of more than 180% YoY in H126, owing to penetration into a leading global consumer electronics player's innovation cycle.

\- Other equipment:

\- Battery equipment: H126 revenue increased by around 45% YoY, benefiting from capacity expansion by large customers.

\- Pan-semi equipment: H126 revenue grew by around 40% YoY, driven by repeat AMOLED orders, and a recovery in the packaging and testing business.

\- General purpose laser equipment: H126 revenue increased by around 30% YoY, owing to the broadening range of applications for its low-power laser equipment.

Figure 1: Q226 preliminary results vs UBS-S and consensus estimates

<table><tr><td colspan="6">2Q26</td></tr><tr><td></td><td>Preliminary results</td><td>UBS-Se</td><td>diff.</td><td>Reuters consensus</td><td>diff.</td></tr><tr><td>Revenue (Rmb m)</td><td>7,865*</td><td>6,792</td><td>16%</td><td>6,665</td><td>18%</td></tr><tr><td>Net profit (Rmb m)</td><td>946</td><td>680</td><td>39%</td><td>680</td><td>39%</td></tr></table>

Source: Reuters, UBS-S estimates. Note:\* denotes UBS-S estimates based on company preliminary results.

Figure 2: Han's Laser's half-yearly revenue  
![](images/27fbfe43fc5eccb7df0b7b168bfd9a4341550d7d19ed38429b675a803d403c65.jpg)  
Source: Company data, UBS-S estimates

Figure 3: Han's Laser's revenue growth in H126, by sector  
![](images/ac5eca920d9e02292231fa724dadd8002dcfcdc5941304b6aa8c83c800ab63a4.jpg)  
Source: Company data, UBS-S estimates

## Changes in our key assumptions

We raise our full-year revenue forecasts by 16% for 2026E, 29% for 2027E and 40% for 2028E, mainly reflecting the stronger-than-expected demand for consumer electronics equipment, PCB equipment, and other equipment.

Figure 4: Changes in our revenue forecasts

<table><tr><td rowspan="2">(Rmb m)</td><td colspan="3">UBS-Se (New)</td><td colspan="3">UBS-Se (Old)</td><td colspan="3">%/ppt chg</td></tr><tr><td>2026E</td><td>2027E</td><td>2028E</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Information Technology</td><td>16,224</td><td>25,174</td><td>30,116</td><td>14,819</td><td>19,409</td><td>21,422</td><td>9%</td><td>30%</td><td>41%</td></tr><tr><td>- Consumer electronic</td><td>5,200</td><td>9,800</td><td>10,475</td><td>4,900</td><td>6,300</td><td>6,060</td><td>6%</td><td>56%</td><td>73%</td></tr><tr><td>- PCB</td><td>11,024</td><td>15,374</td><td>19,641</td><td>9,919</td><td>13,109</td><td>15,362</td><td>11%</td><td>17%</td><td>28%</td></tr><tr><td>New Energy</td><td>3,017</td><td>3,302</td><td>3,689</td><td>2,255</td><td>2,774</td><td>3,299</td><td>34%</td><td>19%</td><td>12%</td></tr><tr><td>Pan semiconductor</td><td>2,301</td><td>2,613</td><td>3,036</td><td>1,601</td><td>1,784</td><td>1,990</td><td>44%</td><td>46%</td><td>53%</td></tr><tr><td>General industrial laser equipment</td><td>7,685</td><td>8,521</td><td>9,857</td><td>6,481</td><td>6,946</td><td>7,375</td><td>19%</td><td>23%</td><td>34%</td></tr><tr><td>- High power</td><td>3,557</td><td>3,773</td><td>4,160</td><td>3,165</td><td>3,497</td><td>3,823</td><td>12%</td><td>8%</td><td>9%</td></tr><tr><td>- Low power and others</td><td>4,129</td><td>4,748</td><td>5,697</td><td>3,316</td><td>3,449</td><td>3,552</td><td>24%</td><td>38%</td><td>60%</td></tr><tr><td>Fiber</td><td>30</td><td>200</td><td>1,000</td><td>0</td><td>0</td><td>0</td><td>n.a.</td><td>n.a.</td><td>n.a.</td></tr><tr><td>Total revenue</td><td>29,257</td><td>39,809</td><td>47,699</td><td>25,157</td><td>30,913</td><td>34,086</td><td>16%</td><td>29%</td><td>40%</td></tr></table>

Source: UBS-S estimates

The major reasons for the increase in our revenue forecasts are:

## 1. PCB equipment:

We lift our PCB equipment revenue forecast by 11-28% in 2026-28E, mainly to reflect the combined impact of: 1) a higher laser drilling equipment forecast, owing to rising demand for mSAP applications in high-end HDI (mainly for 1.6T optical transceiver processing); and 2) a higher forecast for mechanical and other drilling equipment (mainly formation and testing equipment for mSAP applications).

We see a number of major positives for the PCB equipment business including: 1) major AI PCB players, Victory Giant and Avary, provided a positive capex outlook for 2026 (up 172% and 154% YoY, respectively) after an industry-wide doubling in capex in 2025; 2) newly announced capex for AI PCB exceeds Rmb100bn, of which there is increasing advanced PCB capacity expansion (eg, high-order HDI and mSAP), which requires more high-value-added laser drilling equipment; 3) PCB equipment procurement in 2H26-2028 is likely to accelerate after infrastructure construction (such as land and plants) in 2025-26 in the industry; and 4) according to Victory Giant, its procurement from Han's CNC (Han's Laser's PCB subsidiary, dedicated to PCB equipment business) accounted for 20% of its total capex in 2025; as Han's CNC's products have been recognized by the global AI PCB market leader, we believe that Han's CNC's PCB equipment is likely to penetrate more AI PCB players.

Figure 5: Changes in our PCB equipment revenue forecasts

<table><tr><td rowspan="2">Rmb m</td><td colspan="3">UBS-Se (New)</td><td colspan="3">UBS-Se (Old)</td><td colspan="3">%/ppt chg</td></tr><tr><td>2026</td><td>2027</td><td>2028</td><td>2026</td><td>2027</td><td>2028</td><td>2026</td><td>2027</td><td>2028</td></tr><tr><td>Mechanical drilling equipment</td><td>7,190</td><td>8,833</td><td>9,608</td><td>7,415</td><td>9,521</td><td>10,090</td><td>-3%</td><td>-7%</td><td>-5%</td></tr><tr><td>Laser drilling equipment</td><td>2,730</td><td>3,510</td><td>4,136</td><td>713</td><td>1,433</td><td>2,749</td><td>283%</td><td>145%</td><td>50%</td></tr><tr><td>Other equipment</td><td>1,104</td><td>3,031</td><td>5,898</td><td>1,791</td><td>2,155</td><td>2,524</td><td>-38%</td><td>41%</td><td>134%</td></tr><tr><td>Total</td><td>11,024</td><td>15,374</td><td>19,641</td><td>9,919</td><td>13,109</td><td>15,362</td><td>11%</td><td>17%</td><td>28%</td></tr></table>

Source: UBS-S estimates

Figure 6: PCB manufacturers' recently announced capacity expansion plans

<table><tr><td>Company</td><td>Announcement Date</td><td>Country</td><td>Province/city</td><td>Major product</td><td>Capacity</td><td>Total investment (Rmb bn)</td><td>Annual output (Rmb100m)</td><td>Estimated launch date</td><td>Current status</td></tr><tr><td rowspan="8">Victory Giant</td><td>May-24</td><td>Vietnam</td><td></td><td>HDI</td><td>150,000 sqm</td><td>1.8</td><td>1.65</td><td>2026</td><td rowspan="3">Expected to start production in June-July 2026Phase I upgrade of the company&#x27;s Thailand factory Building A1 completed in March 2025; Phase II high-end capacity has begun production for qualification; The construction of Building A2 in Thailand and the facility in Vietnam is also proceeding per schedule.L1-3 will be launched in June; L4-5 in November; L6 in December. Huizhou fab 4 project has started to ramp up in stages.</td></tr><tr><td>Aug-24</td><td>Thailand</td><td></td><td>HLC</td><td>1.5m sqm</td><td>1.4</td><td>1.95</td><

[中间内容因长度限制已省略]

ded in financial markets outside of the Republic of Türkiye. Further to this, pursuant to article 9 of the Communiqué on Principles Regarding Investment Services, Activities and Ancillary Services No. III-37.1, investment services provided abroad to residents of the Republic of Türkiye based on their own initiative are not restricted. United Arab Emirates (UAE) / DIFC / Abu Dhabi: UBS is not licensed in the UAE by the Central Bank of the UAE nor by the Emirates' Securities and Commodities Authority and does not undertake banking activities in the UAE. This document is provided for your information only and does not constitute financial advice. DIFC: UBS AG Dubai Branch is regulated by the DFSA in the DIFC. This material is strictly intended for Professional Clients and/or Market Counterparties only as classified under the DFSA rulebook. It should not be distributed to Retail Clients. The Investment Research is provided for information purposes only and is not a recommendation or offer to buy/sell/hold a particular investment. The investment research may be out of date. You should seek investment advice before acting on the basis of the Investment Research. Abu Dhabi: UBS AG Abu Dhabi Branch is licensed and regulated by the Financial Services Regulatory Authority ("FSRA") of the Abu Dhabi Global Market. This material is intended solely for professional clients or market counterparties, as defined in the rules of the FSRA. It is not directed at, nor intended for, retail clients or any person who does not meet the criteria of a professional client or market counterparty. United Kingdom: This document is issued by UBS Wealth Management, a division of UBS AG which is authorised and regulated by the Financial Market Supervisory Authority in Switzerland. In the United Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/15056b3a5c80e5d693479330e2f06dc9e2955355c8ed8245481e07083c702c4c.jpg)
"""
