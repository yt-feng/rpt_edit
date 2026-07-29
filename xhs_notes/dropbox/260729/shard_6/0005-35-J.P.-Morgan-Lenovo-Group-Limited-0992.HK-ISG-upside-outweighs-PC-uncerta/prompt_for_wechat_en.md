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
## Lenovo Group Limited (0992)

ISG upside outweighs PC uncertainty; u/g to OW

We are upgrading Lenovo to OW with a Jun-27 PT of HK\$30 (based on 16x 12-month forward diluted EPS), driven by strong server profitability improvement, better-than-feared IDG price elasticity, and consolidation tailwinds amid tight component supply. Lenovo stock is up 85% (vs. the HSI index at flat) following a solid Mar-quarter print on May 21. We expect a constructive share-price reaction into the Jun-quarter results, with upside primarily driven by the server segments. Our industry research suggests Lenovo is seeing fast-growing AI-related client traction and healthy server profitability supported by favorable pricing. As a result, we expect further ISG margin expansion over the coming quarters on operating leverage. While PC earnings visibility remains uncertain, we believe Lenovo should outperform PC peers given its industry leadership and scale advantages. Key downside risks include a potential slowdown in AI capex investment in 2027 and a larger-than-expected margin headwind from rising component costs.

\- AI breakthrough + general server strength driving a favorable pricing setup. Despite rising component costs, server OEMs have been enjoying favorable pricing and margins, supported by inference-driven supply tightness across both GPU and traditional servers. We believe Lenovo has navigated component constraints better than peers, helped by a more diversified supplier base (including Chinese suppliers) and business model (ODM + brand). Our industry research suggests Lenovo's AI-related revenue reached 30%+ of ISG revenue in the Jun-quarter and should sustain momentum into 2HCY26. We model \~60% YoY ISG revenue growth and 5% ISG OPM in FY27 (vs. 0.4% in FY26).

\- Mixed IDG outlook, but margin resilience looks better than feared. We keep our IDG revenue and margin assumptions unchanged despite larger-than-expected component price increases over the past three months. We expect Lenovo to sustain an IDG quarterly operating profit run-rate of \~US\$1.0–1.1bn. Lenovo is likely to continue outperforming PC peers on scale advantages, tight cost control, mix management, and supply-chain execution. We model 10%/4% YoY IDG revenue growth and 6.9%/6.8% IDG OPM in CY2026/27E, respectively.

\- Why upgrade now? We previously held a more Neutral stance on Lenovo given PC earnings downside risk. However, we believe server strength is now more than offsetting consumer electronics softness. As Lenovo steps up its position in the AI server supply chain with the GB300 launch, we expect it to ride neocloud demand over the coming years. Improving mix should support further re-rating and sustained stock outperformance vs. peers. Besides, the moderating memory price increase in the next one year could partially mitigate margin risks from higher component costs.

## ▲ Overweight

Previous: Neutral

0992.HK, 992 HK
Price (27 Jul 26): HK\$24.32

▲ Price Target (Jun-27): HK\$30.00
Prior (Mar-27): HK\$20.00

## China

Technology - Hardware

Albert Hung AC
(886-2) 2725-9875
albert.hung@jpmchase.com
JPM Securities (Taiwan) Limited/ JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Gokul Hariharan AC
(852) 2800-8564
gokul.hariharan@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

## Anthony Leng

(886-2) 2725-9240
anthony.leng@JPM.com
JPM Securities (Taiwan) Limited

<table><tr><td colspan="4">Key Changes (FYE Mar)</td></tr><tr><td></td><td>Prev</td><td>Cur</td><td>Δ</td></tr><tr><td>Adj. net income - 27E ($ mn)</td><td>2,289</td><td>2,787</td><td>21.8%</td></tr><tr><td>Adj. net income - 28E ($ mn)</td><td>2,605</td><td>3,353</td><td>28.7%</td></tr></table>

## Quarterly Forecasts (FYE Mar)

<table><tr><td colspan="4">Adj. net income ($ mn)</td></tr><tr><td></td><td>2026A</td><td>2027E</td><td>2028E</td></tr><tr><td>Q1</td><td>389</td><td>663</td><td>753</td></tr><tr><td>Q2</td><td>512</td><td>720</td><td>873</td></tr><tr><td>Q3</td><td>589</td><td>747</td><td>944</td></tr><tr><td>Q4</td><td>559</td><td>657</td><td>783</td></tr><tr><td>FY</td><td>2,049</td><td>2,787</td><td>3,353</td></tr></table>

## Style Exposure

<table><tr><td rowspan="2">Quant Factors</td><td rowspan="2">Current %Rank</td><td colspan="4">Hist %Rank (1=Top)</td></tr><tr><td>6M</td><td>1Y</td><td>3Y</td><td>5Y</td></tr><tr><td>Value</td><td>19</td><td>6</td><td>9</td><td>12</td><td>12</td></tr><tr><td>Growth</td><td>60</td><td>79</td><td>79</td><td>82</td><td>89</td></tr><tr><td>Momentum</td><td>1</td><td>86</td><td>72</td><td>27</td><td>29</td></tr><tr><td>Quality</td><td>24</td><td>29</td><td>29</td><td>22</td><td>26</td></tr><tr><td>Low Vol</td><td>87</td><td>69</td><td>76</td><td>46</td><td>49</td></tr><tr><td>ESGQ</td><td>9</td><td>13</td><td>6</td><td>1</td><td>1</td></tr></table>

Price Performance  
![](images/d8ff9c34ad33008312e185cc9fc81020d6fd165bfe5a4e159a25051bfc8f5584.jpg)

— 0992.HK Price (HK\$) MSCI-Cnx (rebased)

<table><tr><td></td><td>YTD</td><td>1m</td><td>3m</td><td>12m</td></tr><tr><td>Abs</td><td>162.6%</td><td>3.8%</td><td>100.7%</td><td>133.0%</td></tr><tr><td>Rel</td><td>174.1%</td><td>-2.8%</td><td>108.2%</td><td>142.4%</td></tr></table>

Company Data

<table><tr><td>Shares O/S (mn)</td><td>12,405</td></tr><tr><td>52-week range (HK$)</td><td>27.42-8.52</td></tr><tr><td>Market cap ($ mn)</td><td>38,467</td></tr><tr><td>Exchange rate</td><td>7.84</td></tr><tr><td>Free float (%)</td><td>56.9%</td></tr><tr><td>3M ADV (mn)</td><td>169.24</td></tr><tr><td>3M ADV ($ mn)</td><td>445.2</td></tr><tr><td>Volatility (90 Day)</td><td>78</td></tr><tr><td>Index</td><td>MXCNX</td></tr><tr><td>BBG ANR (Buy | Hold | Sell)</td><td>32|4|0</td></tr></table>

Key Metrics (FYE Mar)

<table><tr><td>$ in millions</td><td>FY26A</td><td>FY27E</td><td>FY28E</td></tr><tr><td colspan="4">Financial Estimates</td></tr><tr><td>Revenue</td><td>83,075</td><td>97,873</td><td>112,556</td></tr><tr><td>Adj. EBIT</td><td>3,124</td><td>4,257</td><td>4,966</td></tr><tr><td>Adj. EBITDA</td><td>4,562</td><td>5,633</td><td>6,342</td></tr><tr><td>Adj. net income</td><td>2,049</td><td>2,787</td><td>3,353</td></tr><tr><td>Adj. EPS</td><td>0.17</td><td>0.22</td><td>0.27</td></tr><tr><td>BBG EPS</td><td>0.13</td><td>0.19</td><td>0.25</td></tr><tr><td>Cashflow from operations</td><td>3,844</td><td>5,143</td><td>5,582</td></tr><tr><td>FCFF</td><td>2,704</td><td>4,353</td><td>4,929</td></tr><tr><td colspan="4">Margins and Growth</td></tr><tr><td>Revenue Growth Y/Y (%)</td><td>20.3%</td><td>17.8%</td><td>15.0%</td></tr><tr><td>EBIT margin</td><td>3.8%</td><td>4.3%</td><td>4.4%</td></tr><tr><td>EBIT Growth Y/Y (%)</td><td>27.4%</td><td>36.3%</td><td>16.7%</td></tr><tr><td>EBITDA margin</td><td>5.5%</td><td>5.8%</td><td>5.6%</td></tr><tr><td>EBITDA Growth Y/Y (%)</td><td>31.6%</td><td>23.5%</td><td>12.6%</td></tr><tr><td>Net margin</td><td>2.5%</td><td>2.8%</td><td>3.0%</td></tr><tr><td>Adj. EPS growth</td><td>41.8%</td><td>36.0%</td><td>20.3%</td></tr><tr><td colspan="4">Ratios</td></tr><tr><td>Adj. tax rate</td><td>19.3%</td><td>17.8%</td><td>19.2%</td></tr><tr><td>Interest cover</td><td>7.9</td><td>8.3</td><td>10.2</td></tr><tr><td>Net debt/Equity</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>Net debt/EBITDA</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>ROE</td><td>27.1%</td><td>29.4%</td><td>28.5%</td></tr><tr><td colspan="4">Valuation</td></tr><tr><td>FCFF yield</td><td>7.0%</td><td>11.3%</td><td>12.8%</td></tr><tr><td>Dividend yield</td><td>1.7%</td><td>1.9%</td><td>2.1%</td></tr><tr><td>EV/Revenue</td><td>0.5</td><td>0.4</td><td>0.3</td></tr><tr><td>EV/EBITDA</td><td>8.4</td><td>6.3</td><td>5.1</td></tr><tr><td>Adj. P/E</td><td>18.8</td><td>13.8</td><td>11.5</td></tr></table>

## Summary Investment Thesis and Valuation

Our industry research suggests Lenovo is seeing fast-growing AI-related client traction and healthy server profitability supported by favorable pricing. As a result, we expect further ISG margin expansion over the coming quarters on operating leverage. While PC earnings visibility remains uncertain, we believe Lenovo should outperform PC peers given its industry leadership and scale advantages. OW.

## Valuation

Our Jun-27 PT of HK\$30 is based on 16x 12-month-forward non-HKFRS diluted EPS (higher than our previous 14x), above the mid-cycle valuation driven by strong server profitability improvement, better-than-feared IDG price elasticity, and consolidation tailwinds amid tight component supply.

Performance Drivers  
![](images/6bbf51ec924d5bafd2545ce3ca0e6b220526096925aa1775280bccf19284e2a4.jpg)

<table><tr><td>Factors</td><td>6M Corr</td><td>1Y Corr</td></tr><tr><td>Market: MSCI Asia Pac ex JP</td><td>0.38</td><td>0.44</td></tr><tr><td>Region: China</td><td>-0.15</td><td>-0.05</td></tr><tr><td>Macro:</td><td></td><td></td></tr><tr><td>Citi Economic Surprise - EM</td><td>-0.32</td><td>-0.23</td></tr><tr><td>Generic 1st &#x27;CO&#x27; Future</td><td>-0.15</td><td>-0.21</td></tr><tr><td>HSI Volatility Index</td><td>-0.10</td><td>-0.12</td></tr><tr><td>Quant Styles:</td><td></td><td></td></tr><tr><td>Growth</td><td>0.29</td><td>0.29</td></tr><tr><td>Size</td><td>0.32</td><td>0.23</td></tr><tr><td>Momentum</td><td>0.07</td><td>0.15</td></tr></table>

## Mixed IDG outlook, but margin resilience looks better than feared

Lenovo's PC shipments were up $3\%$ YoY in 1HCY26 (vs. industry PC shipments at up $+1\%$ YoY), according to Gartner® data, driven by better-than-expected PC demand and m/s gains on better supply chain execution. Looking ahead, we expect a flattish 2HCY26 PC outlook (i.e. a $50\% / 50\%$ 1H/2H PC shipment split vs. traditional seasonality of $45\% / 55\%$ ). We attribute the sub-seasonal trend to PC end-demand weakness due to memory-led negative price elasticity and fading Win-10 replacement demand.

Figure 1: Lenovo PC shipments and YoY mn units, %  
![](images/1070521cc1a2e690d5f6df055a861f207a391678d6337ae88e032650b5984f41.jpg)  
Source: Gartner® quarterly PC tracker, JPM estimates.

Figure 2: Lenovo's PC Revenue and YoY US\$ in billions, %  
![](images/f464119895475376c6327a36a2807ea696c32abc1514d8e594ed23e8dd2b0015.jpg)  
Source: JPM estimates, Company reports FY16-FY26.

On PC margins, Lenovo delivered a resilient PC OPM in Mar-Q at 7.6% (flattish QoQ). Our research indicates that Lenovo's PC margin could remain resilient in Jun-Q and outperform PC peers in the next few quarters, supported by scale benefits, supply chain excellence, and mix management.

Figure 3: Lenovo PC ASP and GM US\$, %  
![](images/be104ac6b31176c386dc15dd318f518ceb197b16fc1ba424c82c10ee56be94df.jpg)  
Source: JPM estimates for both historical and forecast data.

Figure 4: Lenovo's PC operating income and OPM US\$ in millions, %  
![](images/e1b514e5d03368c4e01f8de09fa6f1f5413e3978d20ad80b65f99b3b898b2574.jpg)  
Source: JPM estimates, Company reports FY16-FY26.

Overall, we model 3% IDG revenue growth in FY27, as PC ASP expansion should more than offset the unit declines. We expect PC margins to decline to 6.8% in FY27 vs. 7.2% in FY26, mainly due to memory cost hikes.

AI breakthrough + general server strength driving a favorable pricing setup

We expect accelerating server shipment growth for Lenovo in FY27 (JPMe 23% YoY growth vs. +13% in FY26), driven by strong MSFT traditional server demand, better-than-expected enterprise server demand, and m/s gain in AI servers.

Our research indicates that Lenovo has started GB300 shipments to neocloud customers in late Mar-Q to early Jun-Q, and AI servers could reach \~30% of Lenovo's total ISG revenue in Jun-Q. More importantly, Lenovo's AI server order pipelines have reached US\$21bn+ in Mar-Q and are likely to see continued increase given the strong AI demand, which could help sustain the server revenue momentum in the next few quarters.

Overall, we forecast $\sim 60\%$ ISG revenue growth in FY27, driven by strong server demand, AI server breakthrough, and pricing actions in general servers.

Figure 5: Lenovo server shipments and market share  
![](images/59113e8f250071232e6015f9825cc4bbb175ff9677e9600394d337b69831e0a6.jpg)  
Source: Gartner® quarterly server tracker, JPM estimates.

Figure 6: Lenovo's ISG Revenue and YoY US\$ in billions, %  
![](images/8084a58fa7f86bfb321c18fe9c4437894bcc00da09d4f572a53baafcbe8a513a.jpg)  
Source: JPM estimates, Company reports FY17-FY26.

Server OEMs such as Lenovo have enjoyed a favorable pricing dynamics across AI and traditional servers amid strong AI demand and supply constraints. This could more than offset the negative impact from memory component price hikes, in our view. In addition, we believe Lenovo will navigate through this super memory cycle better than peers due to its diversified supplier base (including Chinese suppliers) and scale benefits levered from its PC biz.

Overall, we expect a significant OPM improvement for Lenovo's ISG biz to $5\%$ in FY27 from $0.4\%$ in FY26, driven by favorable pricing dynamics and positive OP leverage. Beyond FY27, we anticipate a sustained ISG growth momentum on the AI-driven multi-year server cycle with continued margin improvement on better scale.

Figure 7: Lenovo's ISG operating income and OPM trend \$ in millions, %  
![](images/7e10112a87abb441de509f8a3266cccdc476feb877db1c9dced038b353055676.jpg)  
Source: JPM estimates, Company reports FY17-FY26.

## PE/PB 12m fwd bands

Figure 8: One-year forward P/E band  
![](images/6f5e78246cce06f22fd54a05c4ac40dfe68121f810c27bf9edbff09d4ffbc379.jpg)  
Source: JPM calculations, Bloomberg Finance L.P. estimates as of close of July 27, 2026. Based on non HKFRS 12M fwd EPS.

Figure 9: One-year forward P/B band  
![](images/f0ed03e5be1570b94f5084bb62b63461ee3647b09789024c78becb410110a554.jpg)  
Source: JPM calculations, Bloomberg Finance L.P. estimates as of close of July 27, 2026.

Table 1: Lenovo earnings revision

<table><tr><td rowspan="2">US$ million, YE Mar</td><td colspan="3">Revised</td><td colspan="3">Prior</td><td colspan="3">Change (%)</td></tr><tr><td>FY27E</td><td>FY28E</td><td>FY29E</td><td>FY27E</td><td>FY28E</td><td>FY29E</td><td>FY27E</td><td>FY28E</td><td>FY29E</td></tr><tr><td>Sales</td><td>97,873</td><td>112,556</td><td>128,139</td><td>93,878</td><td>104,502</td><td>N.A</td><td>4%</td><td>8%</td><td>N.A</td></tr><tr><td>Gross profit</td><td>15,093</td><td>16,811</td><td>18,885</td><td>14,190</td><td>15,234</td><td>N.A</td><td>6%</td><td>10%</td><td>N.A</td></tr><tr><td>Non-HKFRS Operating profit</td><td>4,257</td><td>4,966</td><td>5,881</td><td>3,687</td><td>4,035</td><td>N.A</td><td>15%</td><td>23%</td><td>N.A</td></tr><tr><td>Non-HKFRS Pretax profit</td><td>3,701</td><td>4,463</td><td>5,436</td><td>3,132</td><td>3,528</td><td>N.A</td><td>18%</td><td>27%</td><td>N.A</td></tr><tr><td>Non-HKFRS Net Income</td><td>2,787</td><td>3,353</td><td>4,132</td><td>2,289</td><td>2,605</td><td>N.A</td><td>22%</td><td>29%</td><td>N.A</td></tr><tr><td>Non-HKFRS diluted EPS (US$)</td><td>0.19</td><td>0.23</td><td>0.28</td><td>0.16</td><td>0.18</td><td>N.A</td><td>22%</td><td>29%</td><td>N.A</td></tr><tr><td>Gross Margin</td><td>15.4%</td><td>14.9%</td><td>14.7%</td><td>15.1%</td><td>14.6%</td><td>N.A</td><td>31bps</td><td>36bps</td><td>N.A</td></tr><tr><td>Operating Margin</td><td>4.3%</td><td>4.4%</td><td>4.6%</td><td>3.9%</td><td>3.9%</td><td>N.A</td><td>42bps</td><td>55bps</td><td>N.A</td></tr><tr><td>Net Margin</td><td>2.8%</td><td>3.0%</td><td>3.2%</td><td>2.4%</td><td>2.5%</td><td>N.A</td><td>41bps</td><td>49bps</td><td>N.A</td></tr><tr><td>OPEX Ratio</td><td>11.1%</td><td>10.5%</td><td>10.1%</td><td>11.2%</td><td>10.7%</td><td>N.A</td><td>-12bps</td><td>-19bps</td><td>N.A</td></tr><tr><td>Segment Revenue</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>PCSD</td><td>50,094</td><td>53,194</td><td>55,484</td><td>49,960</td><td>53,042</td><td>N.A</td><td>0%</td><td>0%</td><td>N.A</td></tr><tr><td>MBG</td><td>10,889</td><td>11,314</td><td>11,906</td><td>10,889</td><td>11,344</td><td>N.A</td><td>0%</td><td>0%</td><td>N.A</td></tr><tr><td>ISG</td><td>30,517</td><td>40,362</td><td>51,642</td><td>26,436</td><td>31,988</td><td>N.A</td><td>15%</td><td>26%</td><td>N.A</td></tr><tr><td>SSG</td><td>11,795</td><td>13,860</td><td>16,135</td><td>11,795</td><td>13,860</td><td>N.A</td><td>0%</td><td>0%</td><td>N.A</td></tr><tr><td>Segment PTI</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>PCSD</td><td>3,766</td><td>3,958</td><td>4,129</td><td>3,757</td><td>3,947</td><td>N.A</td><td>0%</td><td>0%</td><td>N.A</td></tr><tr><td>MBG</td><td>410</td><td>442</td><td>462</td><td>410</td><td>443</td><td>N.A</td><td>0%</td><td>0%</td><td>N.A</td></tr><tr><td>ISG</td><td>1,512</td><td>2,049</td><td>2,673</td><td>823</td><td>824</td><td>N.A</td><td>84%</td><td>149%</td><td>N.A</td></tr><tr><td>SSG</td><td>2,462</td><td>2,755</td><td>3,207</td><td>2,462</td><td>2,755</td><td>N.A</td><td>0%</td><td>0%</td><td>N.A</td></tr></table>

Source: JPM estimates.

Table 2: Lenovo: JPM vs Bloomberg Consensus Estimates

<table><tr><td rowspan="2">US$ million, YE Mar</td><td colspan="4">JPMe</td><td colspan="4">Consensus</td><td colspan="4">Difference (%)</td></tr><tr><td>1QFY27E</td><td>2QFY27E</td><td>FY27E</td><td>FY28E</td><td>1QFY27E</td><td>2QFY27E</td><td>FY27E</td><td>FY28E</td><td>1QFY27E</td><td>2QFY27E</td><td>FY27E</td><td>FY28E</td></tr><tr><td>Sales</td><td>23,270</td><td>25,165</td><td>97,873</td><td>112,556</td><td>22,258</td><td>23,744</td><td>94,069</td><td>105,239</td><td>5%</td><td>6%</td><td>4%</td><td>7%</td></tr><tr><td>Gross profit</td><td>3,650</td><td>3,845</td><td>15,093</td><td>16,811</td><td>3,522</td><td>3,687</td><td>14,664</td><td>16,367</td><td>4%</td><td>4%</td><td>3%</td><td>3%</td></tr><tr><td>Operating profit</td><td>969</td><td>1,094</td><td>4,189</td><td>4,898</td><td>634</td><td>964</td><td>3,915</td><td>4,881</td><td>53%</td><td>13%</td><td>7%</td><td>0%</td></tr><tr><td>Pretax profit</td><td>578</td><td>920</td><td>3,295</td><td>4,275</td><td>609</td><td>609</td><td>3,231</td><td>4,249</td><td>-5%</td><td>51%</td><td>2%</td><td>1%</td></tr><tr><td>Net Income</td><td>403</td><td>676</td><td>2,396</td><td>3,180</td><td>432</td><td>432</td><td>2,485</td><td>3,127</td><td>-7%</td><td>57%</td><td>-4%</td><td>2%</td></tr><tr><td>Gross Margin</td><td>15.7%</td><td>15.3%</td><td>15.4%</td><td>14.9%</td><td>15.8%</td><td>15.5%</td><td>15.6%</td><td>15.6%</td><td>-14bps<

[中间内容因长度限制已省略]

erial only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own

independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
