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
# Global Precious Metals

## 2Q26 prod preview: Sequentially better; investor focus likely on cost and inventory release; changes to TPs

## CITI'S TAKE

Reporting season for precious miners will kick off on 17 July and we expect production performance to be sequentially better on lower base (1Q is generally weaker seasonally). However, production performance could look somewhat mixed on a YoY basis for these companies. Overall, we expect the quarterly production trends to closely track the full-year guidance across the coverage. Market will likely focus on outlook commentary to gauge, among other factors: 1) cost performance in the June quarter (impact of higher crude oil prices); 2) production performance at some of the mines e.g., Mogalkewna (1Q was weaker on maintenance being brought forward), Styldrfit, and Eland (both ramping up), IMP's Canadian ops (whether production will exceed guidance), and the Keliber lithium project; and 4) inventory release (IMP/NPH). We have also updated our model to incorporate the latest commodity prices and revisited our assumptions, resulting in TPs but unchanged ratings.

VAL: 2Q26 production preview – we expect stronger production performance QoQ on lower base — VAL reports on 17 July. Total production is likely to increase by 10% QoQ while mined production is likely to increase by 16%. The increase is primarily due to a lower base as 1Q was negatively impacted by seasonality. YoY we expect mined production to increase by 22% primarily due to higher production at Amandelbult (2Q25 was negatively impacted by rainfall-led operational issues). Refined production is expected to increase by 17% QoQ to as (1) 1Q refined production run rate was lower than what the annual guidance suggests (lower base), and (2) VAL plans annual stock counts and planned maintenance in 3Q that could result in lower refined production in the September quarter and higher-than-normal production levels during 2Q/4Q.

IMP: FY26 prod preview – saleable production likely to be flat YoY and towards the upper end of guidance — We expect group saleable production to remain flat (but towards the upper end of the guidance) at c.3.49moz as higher production from the Rustenburg and Zimplats operations are likely to be offset by lower production from Canadian ops Mimosa and Marula mines. Refined production is likely to increase by c.5% YoY within the guidance. QoQ we expect 4Q FY26 production to increase by 11% on lower base (lower matte prod at Zimplats and in general weak March quarter).

SSW: 2Q FY26 prod preview – expecting stronger production performance QoQ — South African PGMs and gold production are likely to increase QoQ on a lower base as the March quarter is generally weaker. US PGM production is also likely to be stronger but in line with the annual guidance.

GFI: 2Q FY26 production preview – expecting stronger production performance YoY — Gold production is likely to increase by 7% YoY on (1) Salares Norte ramp up and (2) accounting for 100% of Gruyere mine production vs 50% in the previous comparable period. This is likely to be offset by lower production from the Damang mine (lease expiry). QoQ production is likely to marginally decline. For 1H FY26, production is likely to be 11% higher YoY.

Ephrem Ravi $^{AC}$ +44-20-7986-2462
ephrem.ravi@citi.com

Shashi Shekhar, CFA
+91-22-4277-5028
shashi.shekhar@citi.com

Krishan M Agarwal

+44-020-7986-4092

krishan.agarwal@citi.com

Data Summary

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Ccy</td><td rowspan="2">Price</td><td rowspan="2">Mkt Cap (M)</td><td rowspan="2">Date &amp; Time</td><td colspan="2">Rating</td><td rowspan="2">Short-Term View</td><td colspan="2">Target Price</td><td rowspan="2">ESPR (%)</td><td rowspan="2">DivYld (%)</td><td rowspan="2">ETR (%)</td><td rowspan="2">Last Rpt Yr</td><td colspan="2">Current Fiscal Year</td><td colspan="2">Next Fiscal Year</td></tr><tr><td>Old</td><td>New</td><td>Old</td><td>New</td><td colspan="2">EPS</td><td colspan="2">EPS</td></tr><tr><td>Anglogold Ashanti PLC</td><td>AU</td><td>US$</td><td>79.76</td><td>40,327</td><td>13 Jul 16:00</td><td>1</td><td>nc</td><td>-</td><td>130.00</td><td>125.00</td><td>56.7</td><td>5.5</td><td>62.2</td><td>Dec-25</td><td>9.57</td><td>8.70</td><td>10.74</td><td>10.77</td></tr><tr><td>AngloGold Ashanti plc</td><td>ANGJJ</td><td>R</td><td>1,315.35</td><td>665,054</td><td>13 Jul 17:00</td><td>1</td><td>nc</td><td>-</td><td>2,100.00</td><td>2,040.00</td><td>55.1</td><td>5.3</td><td>60.4</td><td>Dec-25</td><td>9.57</td><td>8.70</td><td>10.74</td><td>10.77</td></tr><tr><td>Gold Fields GFI Ltd</td><td>GFIJ.J</td><td>US$</td><td>33.53</td><td>29,990</td><td>13 Jul 16:00</td><td>1</td><td>nc</td><td>Downside</td><td>58.00</td><td>57.00</td><td>70.0</td><td>6.3</td><td>76.3</td><td>Dec-25</td><td>6.34</td><td>5.85</td><td>6.69</td><td>6.70</td></tr><tr><td>Gold fields</td><td>GFIJJ</td><td>R</td><td>554.94</td><td>496,685</td><td>13 Jul 17:00</td><td>1</td><td>nc</td><td>Downside</td><td>950.00</td><td>930.00</td><td>67.6</td><td>6.3</td><td>73.9</td><td>Dec-25</td><td>6.34</td><td>5.85</td><td>6.69</td><td>6.70</td></tr><tr><td>Impala Platinum Hldgs</td><td>IMPJJ</td><td>R</td><td>182.60</td><td>165,138</td><td>13 Jul 17:00</td><td>1</td><td>nc</td><td>Upside</td><td>360.00</td><td>250.00</td><td>36.9</td><td>13.7</td><td>50.6</td><td>Jun-25</td><td>30.23</td><td>32.63</td><td>36.50</td><td>33.97</td></tr><tr><td>Northam Platinum Holdings LTD</td><td>NPHJJ</td><td>R</td><td>236.79</td><td>94,740</td><td>13 Jul 17:00</td><td>1</td><td>nc</td><td>-</td><td>420.00</td><td>290.00</td><td>22.5</td><td>10.6</td><td>33.0</td><td>Jun-25</td><td>34.48</td><td>36.59</td><td>39.97</td><td>40.84</td></tr><tr><td>Sibanye Stillwat</td><td>SSWJJ</td><td>R</td><td>34.45</td><td>97,513</td><td>13 Jul 17:00</td><td>2</td><td>nc</td><td>-</td><td>57.00</td><td>37.00</td><td>7.4</td><td>5.8</td><td>13.2</td><td>Dec-25</td><td>13.09</td><td>12.21</td><td>11.72</td><td>12.36</td></tr><tr><td>Valterra Platinum Ltd</td><td>VALJJ</td><td>R</td><td>1,082.21</td><td>287,102</td><td>13 Jul 17:00</td><td>2</td><td>nc</td><td>Upside</td><td>1,600.00</td><td>1,150.00</td><td>6.3</td><td>5.3</td><td>11.5</td><td>Dec-25</td><td>13,442</td><td>14,155</td><td>12,813</td><td>12,225</td></tr><tr><td>Valterra Platinum Ltd</td><td>VALT.L</td><td>£</td><td>48.86</td><td>12,962</td><td>13 Jul 16:30</td><td>2</td><td>nc</td><td>Upside</td><td>73.00</td><td>52.00</td><td>6.4</td><td>5.3</td><td>11.7</td><td>Dec-25</td><td>13,442</td><td>14,155</td><td>12,813</td><td>12,225</td></tr><tr><td colspan="6">1 = Buy, 2 = Neutral, 3 = Sell, H = High Risk</td><td colspan="13">ESPR = Expected Share Price Return, ETR = Expected Total Return, nc = no change</td></tr><tr><td colspan="6">Source: Citi</td><td colspan="13">^Catalyst Watch</td></tr></table>

## Anglogold Ashanti PLC (AU.N)

Buy | TP US\$125.00 from US\$130.00 | Price US\$79.76 (13 Jul 26 16:00)

Maintain Buy with TP marginally reduced to US\$125 — We update our model by incorporating the latest commodity prices (link, resulting in -5%/0%/0% changes to gold price estimates for CY26/27/28e), marking to market FX and revisiting our operational assumptions. The net result is -8%/0%/0% changes to our FY26/27/28 EBITDA estimates. We reduce our TP to US\$125 (from US\$130) primarily driven by lower gold price estimates. At our TP, AU offers c.60% ETR, and we maintain Buy rating on the stock.

## Anglogold Ashanti PLC (ANGJ.J)

Buy | TP R2,040.00 from R2,100.00 | Price R1,315.35 (13 Jul 26 17:00)

Maintain Buy with TP marginally reduced to ZAR 2,040 — We update our model by incorporating the latest commodity prices (link, resulting in -5%/0%/0% changes to gold price estimates for CY26/27/28e), marking to market FX and revisiting our operational assumptions. The net result is -8%/0%/0% changes to our FY26/27/28 EBITDA estimates. We reduce our TP to ZAR 2,040 (from ZAR 2,100) primarily driven by lower gold price estimates. At our TP, ANG offers c.60% ETR, and we maintain Buy rating on the stock.

## Gold Fields Ltd (GFI.N)

Buy | TP US\$57.00 from US\$58.00 | Price US\$33.53 (13 Jul 26 16:00)

Maintain Buy with TP marginally reduced to US\$57 — We update our model by incorporating the latest commodity prices (link, resulting in -5%/0%/0% changes to gold price estimates for CY26/27/28e), marking to market FX and revisiting our operational assumptions. The net result is -7%/0%/0% changes to our FY26/27/28 EBITDA estimates. We reduce our TP to US\$57 (from US\$58) primarily driven by lower gold price estimates. At our TP, GFI offers c.70% ETR, and we maintain Buy rating on the stock.

Figure 1. GFI - 2Q'FY26 production preview

<table><tr><td>GFI - 2Q26E</td><td>Unit</td><td>2Q-25 A</td><td>3Q-25 A</td><td>4Q-25 A</td><td>1Q-26 A</td><td>2Q-26 E</td><td>% Y/Y</td><td>% Q/Q</td><td>VAconsensu</td></tr><tr><td>Gold Produced (attributable)</td><td>koz</td><td>583</td><td>620</td><td>682</td><td>633</td><td>622</td><td>7%</td><td>-2%</td><td>629</td></tr><tr><td>Gold Produced</td><td>koz</td><td>600</td><td>638</td><td>699</td><td>649</td><td>638</td><td>6%</td><td>-2%</td><td>644</td></tr><tr><td>AISC</td><td>$/oz</td><td>1,730</td><td>1,530</td><td>1,637</td><td>1,844</td><td>1,844</td><td>7%</td><td>0%</td><td></td></tr><tr><td>AIC</td><td>$/oz</td><td>1,937</td><td>1,730</td><td>1,769</td><td>2,009</td><td>2,009</td><td>4%</td><td>0%</td><td></td></tr></table>

Source: Citi, Company Reports  
© 2026 Citi Inc. No redistribution without Citi's written permission.

## Gold Fields Ltd (GFIJ.J)

Buy | TP R930.00 from R950.00 | Price R554.94 (13 Jul 26 17:00)

2Q FY26 production preview – expecting stronger production performance YoY — Gold Fields will provide a production update along with the trading update. Gold production is likely to increase by 7% YoY on (1) the Salares Norte ramp up and (2) accounting for 100% of Gruyere mine production vs 50% in the previous comparable period. This is likely to be offset by lower production from the Damang mine (lease expiry). QoQ production is likely to marginally decline. Overall, production is likely to remain within the guidance, and we do not expect any material changes to the full-year production guidance at this stage. For 1H FY26, production is likely to be 11% higher YoY.

Maintain Buy with TP marginally reduced to ZAR 930 — We update our model by incorporating the latest commodity prices (link, resulting in -5%/0%/0% changes to gold price estimates for CY26/27/28e), marking to market FX and revisiting our operational assumptions. The net result is -7%/0%/0% changes to our FY26/27/28 EBITDA estimates. We reduce our TP to ZAR 930 (from ZAR 950) primarily driven by lower gold price estimates. At our TP, GFI offers c.70% ETR, and we maintain Buy rating on the stock.

Figure 2. GFI - 2Q FY26 production preview

<table><tr><td>GFI - 2Q26E</td><td>Unit</td><td>2Q-25 A</td><td>3Q-25 A</td><td>4Q-25 A</td><td>1Q-26 A</td><td>2Q-26 E</td><td>% Y/Y</td><td>% Q/Q</td><td>VAconsensu</td></tr><tr><td>Gold Produced (attributable)</td><td>koz</td><td>583</td><td>620</td><td>682</td><td>633</td><td>622</td><td>7%</td><td>-2%</td><td>629</td></tr><tr><td>Gold Produced</td><td>koz</td><td>600</td><td>638</td><td>699</td><td>649</td><td>638</td><td>6%</td><td>-2%</td><td>644</td></tr><tr><td>AISC</td><td>$/oz</td><td>1,730</td><td>1,530</td><td>1,637</td><td>1,844</td><td>1,844</td><td>7%</td><td>0%</td><td></td></tr><tr><td>AIC</td><td>$/oz</td><td>1,937</td><td>1,730</td><td>1,769</td><td>2,009</td><td>2,009</td><td>4%</td><td>0%</td><td></td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, Company Reports

## Impala Platinum (IMPJ.J)

Buy | TP R250.00 from R360.00 | Price R182.60 (13 Jul 26 17:00)

FY26 production preview – group saleable production likely to be flat YoY and towards the upper end of guidance — Impala will report FY26 production along with the trading update. We expect group saleable production to remain flat (but towards the upper end of the guidance) at c.3.49moz as higher production from Rustenburg and Zimplats ops are likely to be offset by lower production from Canadian ops Mimosa and Marula mines. Refined production is likely to increase by c.5% YoY within the guidance. QoQ we expect 4Q FY26 production to increase by 11% on a lower base (lower matte prod at Zimplats and in general a weak March quarter).

Maintain Buy with TP reduced to ZAR 250 — We update our model by incorporating the latest commodity prices (link), marking to market Ruthenium/Iridium prices and revisiting our operational assumptions. The net result is +6%/-6%/-6% changes to our FY26/27/28 EBITDA estimates. FY26 EBITDA is positively impacted by marking to market higher Ruthenium/Iridium prices. We also lower our valuation multiple for the company to 3.5x (vs 7.0x before). We view this to be appropriate as IMP has traded near this multiple during higher-for-longer PGM price environments. We reduce our TP to ZAR 250 (from ZAR 360) primarily driven by lower multiples used and marginally lower rand basket price estimates medium term. At our TP, IMP offers c50% ETR, and we maintain Buy rating on the stock.

Figure 3. Impala FY26 production preview

<table><tr><td>IMP - FY26</td><td>Unit</td><td>FY25 A</td><td>FY26 E</td><td>Annual guidance/trading update*</td><td>% Y/Y</td></tr><tr><td>Managed + JV</td><td>koz</td><td>3,272</td><td>3,303</td><td></td><td>1%</td></tr><tr><td>Third party purchase</td><td>koz</td><td>209</td><td>190</td><td></td><td>-9%</td></tr><tr><td>Tolled</td><td>koz</td><td>0</td><td>0</td><td></td><td>na</td></tr><tr><td>Group production (saleable)</td><td>koz</td><td>3,481</td><td>3,493</td><td></td><td>0%</td></tr><tr><td>Production (refined)</td><td>koz</td><td>3,375</td><td>3,552</td><td>3,400-3,600</td><td>5%</td></tr><tr><td>Unit cost stock adjusted</td><td>R/oz (6E)</td><td>22,491</td><td>23,624</td><td>23,500-24,500</td><td>5%</td></tr><tr><td>Capex</td><td>Rm</td><td>6,978</td><td>8,495</td><td>8,000-9,000</td><td>22%</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, Company Reports

# Northam Platinum Holdings LTD (NPHJ.J)

Buy | TP R290.00 from R420.00 | Price R236.79 (13 Jul 26 17:00)

Maintain Buy with TP reduced to ZAR290 — We update our model by incorporating the latest commodity prices (link), marking to market Ruthenium/Iridium prices, the latest operating update (link), and revisiting our operational assumptions. The net result is +6%/+2%/-5% changes to our FY26/27/28 EBITDA estimates. FY26 EBITDA is positively impacted by marking to market higher Ruthenium/Iridium prices. We also lower our valuation multiple for the company to 5.0x (vs 9.0x before). We view this to be appropriate as NPH has traded near this multiple during higher-for-longer PGM price environments. We reduce our TP to ZAR 290 (from ZAR 420) primarily driven by lower multiples used and marginally lower rand basket price estimates medium term. At our TP, NPH offers over 30% ETR, and we maintain Buy rating on the stock.

## Sibanye Stillwater Ltd (SSWJ.J)

Neutral | TP R37.00 from R57.00 | Price R34.45 (13 Jul 26 17:00)

2Q FY26 production preview – expecting stronger production performance QoQ — Sibanye will provide production update along with the trading update. South African PGMs and gold production are likely to increase QoQ on a lower base as the March quarter is generally weaker. US PGM production is also likely to be stronger but in line with the annual guidance. Overall, production is likely to remain within the guidance, and we do not expect any material changes to the full-year guidance at this stage. For 1H FY26, production from SA/US PGM ops are likely to remain flat and within the guidance, while production from SA gold ops is likely to be -5% lower YoY.

Maintain Neutral with TP reduced to ZAR37 — We update our model by incorporating the latest commodity prices (link) and company guidance during CMD (higher production and capex, link), and revisiting our operational assumptions. The net result is -2%/+10%/+39% changes to our FY26/27/28 EBITDA estimates. FY28 EBITDA is positively impacted by higher production estimates from SA PGM/gold ops (link). We also lower our valuation multiple for the company to 2.2x (vs 3.6x before). We view this to be appropriate as SSW has traded near this multiple during higher-for-longer PGM price environments. We reduce our TP to ZAR37 (from ZAR57) primarily driven by lower multiples used and lower gold price and lower rand basket price estimates. At our TP, SSW offers over c.13% ETR, and we maintain Neutral rating on the stock.

Figure 4. Sibanye - 2Q'FY26 Production Preview

<table><tr><td>SSW - 2Q26E</td><td>Unit</td><td>2Q-25 A</td><td>3Q-25 A</td><td>4Q-25 A</td><td>1Q-26 A</td><td>2Q-26 E</td><td>% Y/Y</td><td>% Q/Q</td></tr><tr><td>PGM - SA</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>PGM produced (4E)</td><td>koz</td><td>446</td><td>511</td><td>447</td><td>403</td><td>438</td><td>-2%</td><td>9%</td></tr><tr><td>PGM produced (4E),excl third party pu</td><td>koz</td><td>428</td><td>494</td><td>427</td><td>383</td><td>418</td><td>-2%</td><td>9%</td></tr><tr><td>SA</td><td>koz</td><td>397</td><td>464</td><td>398</td><td>356</td><td>389</td><td>-2%</td><td>9%</td></tr><tr><td>non-SA</td><td>koz</td><td>31</td><td>30</td><td>28</td><td>28</td><td>29</td><td>-6%</td><td>5%</td></tr><tr><td>PGM - US</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>PGM produced (2E)</td><td>koz</td><td>69</td><td>73</td><td>70</td><td>68</td><td>72</td><td>5%</td><td>6%</td></tr><tr><td>Gold</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Gold produced</td><td>koz</td><td>159</td><td>176</td><td>156</td><td>139</td><td>150</td><td>-5%</td><td>8%</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, Company Reports

Figure 5. Sibanye - 1H'FY26 Production Preview

<table><tr><td>SSW - 1H26</td><td>Unit</td><td>1H&#x27;FY25a</td><td>1H&#x27;FY26e</td><td>Annual guidance</td><td>% Y/Y</td></tr><tr><td>SA PGM Production (incl third party purchase, 4E)</td><td>koz</td><td>840</td><td>841</td><td>1650-1750</td><td>0%</td></tr><tr><td>Third party purchase</td><td>koz</td><td>36</td><td>40</td><td></td><td></td></tr><tr><td>SA PGM Production (own prod, 4E)</td><td>koz</td><td>804</td><td>802</td><td></td>

[中间内容因长度限制已省略]

ortgage holders prepay the mortgages underlying the CMO and changes in current interest rates. Any government agency backing of the CMO applies only to the face value of the CMO and not to any premium paid. Certain investments contained in the Product may have tax implications for private customers whereby levels and basis of taxation may be subject to change. If in doubt,</td></tr></table>

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
