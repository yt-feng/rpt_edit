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
## Our view on the stock post 2Q26 earnings

GE Aerospace 2Q26 results were ahead of FactSet consensus on revenue, margins, EBIT, EPS, and free cash flow, and the company raised 2026 guidance across the board. Aerospace fundamentals remain strong, including on the aftermarket side, and GE holds a particularly strong position with high market shares in the engine business. Units, price, and operating performance continue to surprise to the upside near-term; while the long-term earnings power impact of its engine market share remains underappreciated by the market in our view. We remain Buy rated on the stock.

## Key elements of the quarter

2Q26 adjusted EPS of \$2.02 was ahead of FactSet consensus at \$1.86. Segment EBIT in the quarter was 9% above consensus. Revenue of \$12.6bn was up 24% yoy. Commercial Engines & Services revenue was up 27% yoy and Defense & Propulsion Technologies revenue was up 16% yoy. Total company orders grew 17% yoy, with CES up 18% and DPT up 12%. CES saw growth in internal shop visit revenue, spare parts and improvement in unit volume. DPT experienced growth in its Propulsion & Additive Technologies business driven by Avio Aero. Operating profit of \$2.75bn was 7% ahead of consensus on a 21.7% margin. EBIT margin at CES was 27.3% relative to our model at 26.7%, while EBIT margin at DPT is 13.8% relative to our model at 12.2%. 2Q26 free cash flow was \$3.03bn, ahead of our \$2.0bn estimate and consensus at \$1.82bn.

GE updated its 2026 guidance, including adjusted revenue growth of high-teens (LDD% prior, consensus implied growth at 15.1%), operating profit of \$10.55-10.75bn (\$9.85-10.25bn prior; consensus at \$10.44bn), adjusted EPS of \$7.65-\$7.85 (\$7.10-\$7.40 prior; consensus at \$7.56), and free cash flow of \$8.9-\$9.2bn (\$8.0-\$8.4bn prior; consensus at \$8.37bn).

## BUY

Noah Poponak, CFA
+1(212)357-0954 | noah.poponak@gs.com
GS & Co. LLC

Connor Dessert
+1(212)357-6166 | connor.dessert@gs.com
GS & Co. LLC

Nizar Mesani
+1(212)934-6965 | nizar.mesani@gs.com
GS India SPL

## Key Data

Market cap: \$365.8bn  
Enterprise value: \$375.0bn  
3m ADTV: \$1.8bn  
United States  
Americas Aerospace & Defense  
M&A Rank: 3

## GS Forecast

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Revenue ($ mn) New</td><td>45,855.0</td><td>51,910.2</td><td>56,183.6</td><td>61,398.2</td></tr><tr><td>Revenue ($ mn) Old</td><td>45,855.0</td><td>49,527.6</td><td>53,009.0</td><td>56,713.8</td></tr><tr><td>EBITDA ($ mn)</td><td>10,275.0</td><td>12,064.1</td><td>13,496.1</td><td>15,000.9</td></tr><tr><td>EBIT ($ mn)</td><td>9,055.0</td><td>10,730.1</td><td>12,003.1</td><td>13,420.9</td></tr><tr><td>EPS ($) New</td><td>6.39</td><td>7.87</td><td>8.93</td><td>10.11</td></tr><tr><td>EPS ($) Old</td><td>6.39</td><td>7.59</td><td>8.47</td><td>9.39</td></tr><tr><td>P/E (X)</td><td>38.9</td><td>44.3</td><td>39.1</td><td>34.5</td></tr><tr><td>Dividend yield (%)</td><td>0.6</td><td>0.1</td><td>0.0</td><td>0.0</td></tr><tr><td>Net debt/EBITDA (X)</td><td>0.8</td><td>0.8</td><td>0.5</td><td>0.2</td></tr><tr><td></td><td>6/26</td><td>9/26E</td><td>12/26E</td><td>3/27E</td></tr><tr><td>EPS ($)</td><td>2.02</td><td>1.97</td><td>2.02</td><td>2.07</td></tr></table>

GS Factor Profile

![](images/4bdcbfe7269f822b625d962b3721deab14d88e56af380d5b63086aaf8158510c.jpg)  
Source: Company data, GS estimates. See disclosures for details.

GE Aerospace (GE) Rating since Oct 9, 2020

Ratios & Valuation

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>P/E (X)</td><td>38.9</td><td>44.3</td><td>39.1</td><td>34.5</td></tr><tr><td>EV/EBITDA (X)</td><td>26.4</td><td>30.7</td><td>27.0</td><td>23.7</td></tr><tr><td>EV/sales (X)</td><td>5.9</td><td>7.1</td><td>6.5</td><td>5.8</td></tr><tr><td>FCF yield (%)</td><td>2.8</td><td>2.4</td><td>2.7</td><td>3.0</td></tr><tr><td>EV/DACF (X)</td><td>28.3</td><td>37.3</td><td>27.8</td><td>28.4</td></tr><tr><td>CROCI (%)</td><td>25.5</td><td>25.5</td><td>32.1</td><td>29.1</td></tr><tr><td>ROE (%)</td><td>45.8</td><td>46.9</td><td>47.9</td><td>45.5</td></tr><tr><td>Net debt/EBITDA (X)</td><td>0.8</td><td>0.8</td><td>0.5</td><td>0.2</td></tr><tr><td>Net debt/equity (%)</td><td>42.9</td><td>52.8</td><td>30.5</td><td>11.9</td></tr><tr><td>Interest cover (X)</td><td>13.3</td><td>13.2</td><td>14.7</td><td>17.6</td></tr><tr><td>Inventory days</td><td>136.3</td><td>128.3</td><td>123.4</td><td>120.0</td></tr><tr><td>Receivable days</td><td>84.0</td><td>80.5</td><td>75.4</td><td>73.4</td></tr><tr><td>Days payable outstanding</td><td>113.3</td><td>107.2</td><td>101.4</td><td>98.6</td></tr></table>

Growth & Margins (%)

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue growth</td><td>0.1</td><td>13.2</td><td>8.2</td><td>9.3</td></tr><tr><td>EBITDA growth</td><td>18.3</td><td>17.4</td><td>11.9</td><td>11.1</td></tr><tr><td>EPS growth</td><td>42.2</td><td>23.3</td><td>13.4</td><td>13.2</td></tr><tr><td>DPS growth</td><td>56.9</td><td>(67.4)</td><td>(100.0)</td><td>NM</td></tr><tr><td>Gross margin</td><td>36.8</td><td>34.4</td><td>33.9</td><td>34.4</td></tr><tr><td>EBIT margin</td><td>24.5</td><td>22.1</td><td>21.4</td><td>21.9</td></tr></table>

<table><tr><td colspan="5">Balance Sheet ($ mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Cash &amp; cash equivalents</td><td>12,392.0</td><td>10,030.0</td><td>12,685.0</td><td>16,245.0</td></tr><tr><td>Accounts receivable</td><td>11,773.0</td><td>11,121.8</td><td>12,090.7</td><td>12,616.1</td></tr><tr><td>Inventory</td><td>11,868.0</td><td>12,054.8</td><td>13,061.9</td><td>13,434.2</td></tr><tr><td>Other current assets</td><td>4,563.0</td><td>5,044.8</td><td>5,303.2</td><td>4,602.2</td></tr><tr><td>Total current assets</td><td>40,596.0</td><td>38,251.4</td><td>43,140.7</td><td>46,897.4</td></tr><tr><td>Net PP&amp;E</td><td>7,987.0</td><td>8,285.0</td><td>8,565.0</td><td>8,825.0</td></tr><tr><td>Net intangibles</td><td>13,285.0</td><td>12,845.0</td><td>12,457.0</td><td>12,057.0</td></tr><tr><td>Total investments</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Other long-term assets</td><td>68,301.0</td><td>66,801.0</td><td>66,801.0</td><td>66,801.0</td></tr><tr><td>Total assets</td><td>130,169.0</td><td>126,182.4</td><td>130,963.7</td><td>134,580.4</td></tr><tr><td>Accounts payable</td><td>10,078.0</td><td>9,908.1</td><td>10,735.8</td><td>11,041.8</td></tr><tr><td>Short-term debt</td><td>1,686.0</td><td>2,000.0</td><td>2,000.0</td><td>2,000.0</td></tr><tr><td>Current lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other current liabilities</td><td>27,216.0</td><td>27,608.0</td><td>27,608.0</td><td>27,608.0</td></tr><tr><td>Total current liabilities</td><td>38,980.0</td><td>39,516.1</td><td>40,343.8</td><td>40,649.8</td></tr><tr><td>Long-term debt</td><td>18,808.0</td><td>17,157.0</td><td>17,157.0</td><td>17,157.0</td></tr><tr><td>Non-current lease liabilities</td><td>0.0</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other long-term liabilities</td><td>53,483.0</td><td>52,218.0</td><td>52,218.0</td><td>52,218.0</td></tr><tr><td>Total long-term liabilities</td><td>72,291.0</td><td>69,375.0</td><td>69,375.0</td><td>69,375.0</td></tr><tr><td>Total liabilities</td><td>111,271.0</td><td>108,891.1</td><td>109,718.8</td><td>110,024.8</td></tr><tr><td>Preferred shares</td><td>0.0</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total common equity</td><td>18,677.0</td><td>17,064.3</td><td>21,018.0</td><td>24,328.7</td></tr><tr><td>Minority interest</td><td>221.0</td><td>227.0</td><td>227.0</td><td>227.0</td></tr><tr><td>Total liabilities &amp; equity</td><td>130,169.0</td><td>126,182.4</td><td>130,963.7</td><td>134,580.4</td></tr><tr><td>BVPS ($)</td><td>17.81</td><td>16.53</td><td>20.54</td><td>24.06</td></tr></table>

Price Performance  
![](images/7df97e10ccc03153037e632f651d5c8a63a57f53b5a90f29d44d4ba156c37883.jpg)

<table><tr><td colspan="5">Cash Flow ($ mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Net income</td><td>8,703.0</td><td>8,373.5</td><td>9,114.2</td><td>10,315.3</td></tr><tr><td>D&amp;A add-back</td><td>1,220.0</td><td>1,334.0</td><td>1,493.0</td><td>1,580.0</td></tr><tr><td>Minority interest add-back</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net (inc)/dec working capital</td><td>(334.0)</td><td>914.7</td><td>(1,406.6)</td><td>109.3</td></tr><tr><td>Others</td><td>(1,047.0)</td><td>(506.2)</td><td>1,839.5</td><td>(4.7)</td></tr><tr><td>Cash flow from operations</td><td>8,537.0</td><td>10,118.0</td><td>11,040.0</td><td>12,000.0</td></tr><tr><td>Capital expenditures</td><td>(1,273.0)</td><td>(1,331.0)</td><td>(1,385.0)</td><td>(1,440.0)</td></tr><tr><td>Acquisitions</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Divestitures</td><td>123.0</td><td>58.0</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>(3.0)</td><td>(1,365.0)</td><td>-</td><td>-</td></tr><tr><td>Cash flow from investing</td><td>(1,153.0)</td><td>(2,638.0)</td><td>(1,385.0)</td><td>(1,440.0)</td></tr><tr><td>Dividends paid</td><td>(1,452.0)</td><td>(873.0)</td><td>0.0</td><td>0.0</td></tr><tr><td>Share issuance/(repurchase)</td><td>(7,551.0)</td><td>(8,277.0)</td><td>(7,000.0)</td><td>(7,000.0)</td></tr><tr><td>Inc/(dec) in debt</td><td>199.0</td><td>(1,046.0)</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>359.0</td><td>354.0</td><td>-</td><td>-</td></tr><tr><td>Cash flow from financing</td><td>(8,445.0)</td><td>(9,842.0)</td><td>(7,000.0)</td><td>(7,000.0)</td></tr><tr><td>Total cash flow</td><td>(1,061.0)</td><td>(2,362.0)</td><td>2,655.0</td><td>3,560.0</td></tr><tr><td>Free cash flow</td><td>7,264.0</td><td>8,787.0</td><td>9,655.0</td><td>10,560.0</td></tr><tr><td>Free cash flow per share (basic) ($)</td><td>6.87</td><td>8.48</td><td>9.42</td><td>10.45</td></tr></table>

Source: FactSet. Price as of 17 Jul 2026 close.

Income Statement (\$ mn)

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue</td><td>45,855.0</td><td>51,910.2</td><td>56,183.6</td><td>61,398.2</td></tr><tr><td>Cost of goods sold</td><td>(28,966.0)</td><td>(34,037.0)</td><td>(37,157.5)</td><td>(40,302.5)</td></tr><tr><td>SG&amp;A</td><td>(4,088.0)</td><td>(4,570.2)</td><td>(5,056.5)</td><td>(5,525.8)</td></tr><tr><td>R&amp;D</td><td>(1,581.0)</td><td>(1,815.9)</td><td>(1,966.4)</td><td>(2,148.9)</td></tr><tr><td>Other operating inc./(exp.)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>EBITDA</td><td>10,275.0</td><td>12,064.1</td><td>13,496.1</td><td>15,000.9</td></tr><tr><td>Depreciation &amp; amortization</td><td>(1,220.0)</td><td>(1,334.0)</td><td>(1,493.0)</td><td>(1,580.0)</td></tr><tr><td>EBIT</td><td>11,220.0</td><td>11,487.1</td><td>12,003.1</td><td>13,420.9</td></tr><tr><td>Net interest inc./(exp.)</td><td>(843.0)</td><td>(871.0)</td><td>(818.7)</td><td>(764.0)</td></tr><tr><td>Income/(loss) from associates</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Pre-tax profit</td><td>10,006.0</td><td>10,029.1</td><td>11,184.4</td><td>12,656.9</td></tr><tr><td>Provision for taxes</td><td>(1,406.0)</td><td>(1,588.6)</td><td>(2,070.2)</td><td>(2,341.5)</td></tr><tr><td>Minority interest</td><td>109.0</td><td>(67.0)</td><td>-</td><td>-</td></tr><tr><td>Preferred dividends</td><td>0.0</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (pre-exceptionals)</td><td>8,709.0</td><td>8,373.5</td><td>9,114.2</td><td>10,315.3</td></tr><tr><td>Net inc. (post-exceptionals)</td><td>6,809.0</td><td>8,236.5</td><td>9,234.2</td><td>10,315.3</td></tr><tr><td>EPS (basic, pre-except) ($)</td><td>8.23</td><td>8.08</td><td>8.89</td><td>10.20</td></tr><tr><td>EPS (diluted, pre-except) ($)</td><td>8.21</td><td>8.00</td><td>8.81</td><td>10.11</td></tr><tr><td>EPS (ex-ESO exp., dil.) ($)</td><td>--</td><td>--</td><td>--</td><td>--</td></tr><tr><td>DPS ($)</td><td>1.44</td><td>0.47</td><td>0.00</td><td>0.00</td></tr><tr><td>Div. payout ratio (%)</td><td>17.5</td><td>5.8</td><td>0.0</td><td>0.0</td></tr><tr><td>Wtd avg shares out. (basic) (mn)</td><td>1,057.6</td><td>1,036.8</td><td>1,024.9</td><td>1,010.9</td></tr><tr><td>Wtd avg shares out. (diluted) (mn)</td><td>1,061.4</td><td>1,046.3</td><td>1,034.5</td><td>1,020.5</td></tr></table>

Source: Company data, GS estimates.

## Exhibit 1: GE 2Q26 adjusted variance \$mn

<table><tr><td rowspan="2">Adjusted</td><td rowspan="2">Actual</td><td rowspan="2">GS Estimate</td><td rowspan="2">$ variance</td><td rowspan="2">% variance</td><td rowspan="2">EPS Impact</td><td colspan="2">YoY change</td></tr><tr><td>2Q25</td><td>Growth</td></tr><tr><td>REVENUE</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Commercial Engines &amp; Services</td><td>9,731</td><td>9,022</td><td>709</td><td>7.9%</td><td>0.15</td><td>7,646</td><td>27.3%</td></tr><tr><td>Defense &amp; Propulsion Technology</td><td>3,443</td><td>3,216</td><td>227</td><td>7.1%</td><td>0.02</td><td>2,978</td><td>15.6%</td></tr><tr><td>Eliminations and Other</td><td>(540)</td><td>(530)</td><td>(10)</td><td></td><td>(0.00)</td><td>(473)</td><td>14.2%</td></tr><tr><td>Total sales</td><td>12,634</td><td>11,709</td><td>925</td><td>7.9%</td><td>$0.15</td><td>10,151</td><td>24.5%</td></tr><tr><td>OPERATING PROFIT</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Commercial Engines &amp; Services</td><td>2,657</td><td>2,409</td><td>248</td><td>10.3%</td><td>0.19</td><td>2,208</td><td>20.3%</td></tr><tr><td>Defense &amp; Propulsion Technology</td><td>475</td><td>392</td><td>83</td><td>21.1%</td><td>0.06</td><td>403</td><td>17.9%</td></tr><tr><td>Segment Operating Profit</td><td>3,132</td><td>2,801</td><td>331</td><td>11.8%</td><td>0.26</td><td>2,611</td><td>20.0%</td></tr><tr><td>Unallocated corporate income (expenses)</td><td>(386)</td><td>(305)</td><td>(81)</td><td>26.6%</td><td>(0.06)</td><td>(274)</td><td>40.9%</td></tr><tr><td>Total Adjusted Operating Profit</td><td>2,746</td><td>2,496</td><td>250</td><td>10.0%</td><td>$0.19</td><td>2,337</td><td>17.5%</td></tr><tr><td>MARGIN</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Commercial Engines &amp; Services</td><td>27.3%</td><td>26.7%</td><td></td><td>60 bp</td><td></td><td>28.9%</td><td>-160 bp</td></tr><tr><td>Defense &amp; Propulsion Technology</td><td>13.8%</td><td>12.2%</td><td></td><td>160 bp</td><td></td><td>13.5%</td><td>30 bp</td></tr><tr><td>Segment Operating Margin</td><td>24.8%</td><td>23.9%</td><td></td><td>90 bp</td><td></td><td>25.7%</td><td>-90 bp</td></tr><tr><td>Total Adjusted Operating Margin</td><td>21.7%</td><td>21.3%</td><td></td><td>40 bp</td><td></td><td>23.0%</td><td>-130 bp</td></tr><tr><td>Interest expense</td><td>(215)</td><td>(225)</td><td>10</td><td>-4.5%</td><td>0.01</td><td>(158)</td><td>36.1%</td></tr><tr><td>Non-service FAS income (cost)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other (loss)/income, net</td><td>(69)</td><td>0</td><td>(69)</td><td></td><td>(0.05)</td><td>(251)</td><td>-72.5%</td></tr><tr><td>EBT</td><td>2,801</td><td>2,271</td><td>530</td><td>23.3%</td><td></td><td>2,389</td><td>17.2%</td></tr><tr><td>Income tax expense</td><td>(406)</td><td>(409)</td><td>3</td><td>-0.7%</td><td>0.09</td><td>(389)</td><td>4.4%</td></tr><tr><td>Effective income tax rate</td><td>14.5%</td><td>18.0%</td><td></td><td>-350 bp</td><td></td><td>16.3%</td><td>-180 bp</td></tr><tr><td>Net income continuing ops</td><td>2,395</td><td>1,862</td><td>533</td><td>28.6%</td><td></td><td>2,000</td><td>19.8%</td></tr><tr><td>Adjustments</td><td>(281)</td><td>30</td><td>(311)</td><td>-1036.7%</td><td>(0.30)</td><td>(223)</td><td>26.0%</td></tr><tr><td>Adjusted Net income continuing ops</td><td>2,114</td><td>1,892</td><td>222</td><td>11.7%</td><td></td><td>1,777</td><td>19.0%</td></tr><tr><td>Adjusted Diluted EPS</td><td>$2.02</td><td>$1.80</td><td>$0.22</td><td>12.2%</td><td>-$0.04</td><td>$1.66</td><td>21.6%</td></tr><tr><td>Diluted Shares outstanding</td><td>1,047.0</td><td>1,051.3</td><td>(4.3)</td><td>-0.4%</td><td>0.01</td><td>1,070.4</td><td>-2.2%</td></tr></table>

Source: Company data, GS Global Investment Research

## Revenue

Total GE Aerospace revenue of \$12.6bn was up 24% yoy.

\- CES revenue of \$9.7bn was up 27% yoy, driven by growth in internal shop visit revenue, spare parts sales and improvement in unit volume.

DPT revenue of \$3.4bn was up 16% yoy driven by growth in both services and equipment.

## Margins

Reported segment EBIT was \$3.1bn.

■ CES segment EBIT was \$2.7bn, up 20% yoy. EBIT margin of 27.3% was above our model at 26.7%.

DPT margin was 13.8%, above our model at 12.2%. Margin increase from higher volume and price were partially offset by mix, investments, and inflation.

## Balance sheet and cash flow

■ Free cash flow in the quarter was \$3.03bn, compared to \$2.1bn in the year-ago period.

■ GE ended the quarter with \$9.35bn in cash and cash equivalents (\$8.93 per share).

## Outlook

GE updated its 2026 guidance, including adjusted revenue growth of high-teens (LDD% prior, consensus implied growth at 15.1%), operating profit of \$10.55-10.75bn (\$9.85-10.25bn prior; consensus at \$10.44bn), adjusted EPS of \$7.65-\$7.85 (\$7.10-\$7.40 prior; consensus at \$7.56), and free cash flow of \$8.9-\$9.2bn (\$8.0-\$8.4bn prior; consensus at \$8.37bn).

Exhibit 2: 2026 Guidance

<table><tr><td rowspan="2"></td><td colspan="3">2026 Outlook</td></tr><tr><td>January</td><td>April</td><td>July</td></tr><tr><td>Adjusted revenue growth (%)</td><td>LDD</td><td>--</td><td>High-teens</td></tr><tr><td>CES</td><td>Mid-teens</td><td>--</td><td>~20%</td></tr><tr><td>D&amp;PT</td><td>MSD/HSD</td><td>--</td><td>LDD</td></tr><tr><td>Operating profit</td><td>$9.85-$10.25bn</td><td>--</td><td>$10.55-$10.75bn</td></tr><tr><td>CES</td><td>$9.6-$9.9bn</td><td>--</td><td>$10.25-$10.35bn</td></tr><tr><td>D&amp;PT</td><td>$1.55-$1.65bn</td><td>--</td><td>$1.6-$1.7bn</td></tr><tr><td>Other</td><td>$(1.2)-$(1.3)bn</td><td>--</td><td>--</td></tr><tr><td>Adjusted EPS</td><td>$7.10-$7.40</td><td>--</td><td>$7.65-$7.85</td></tr><tr><td>Free cash flow</td><td>$8.0-$8.4bn</td><td>--</td><td>$8.9-$9.2bn</td></tr></table>

Source: Company data

## Price target methodology and key risks

We revise our FY2026-2030E EBITDA to \$12,064/13,496/15,001/17,110/18,915mn from \$11,771/13,060/14,275/16,234/17,852mn to reflect revisions to our segment gro

[中间内容因长度限制已省略]

 impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be

supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
