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
- End with: `*For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.*`

Content boundaries:
- Do not mention specific investment bank names such as GS. Use "a global investment bank report" if needed.
- Do not use emoji.
- Do not write like a viral post.
- Do not output your reasoning process.
- Do not generate image Markdown; the system will insert original MinerU images afterward.

Report parsing:
"""
NVIDIA Corporation

# Durable high-quality growth at compelling value multiple, reit Buy

Maintain Rating: BUY | PO: 350.00 USD | Price: 195.55 USD

## Addressing key debates for unique growth franchise

Despite its AI dominance, NVDA stock is up just 3% YTD vs. SOX +82%. We address 4 key investor concerns: 1) Gross margin pressure from higher memory costs, 2) Custom ASIC competition, 3) Crowded investor ownership, and 4) Unproductive use of cash in vendor financing vs. stronger buybacks/dividend. Our analysis suggests that at NVDA's current valuation, investors might already be implicitly discounting an unjustified \~30-35% headwind to CY27/28 EPS ests (effectively delta between NVDA and growth peer forward PE). We strongly disagree with the EPS discount and see as an enhanced Buy opp'ty for a unique, durable growth franchise now trading at a 7-yr low 18x forward PE.

## Memory inflation predictable, pricing power unappreciated

We believe investors overstate HBM cost pressure while underestimating NVDA's pricing power, scale, and \$119bn of supply-chain commitments. HBM content per rack may rise by \~\$0.2-0.3mn from Blackwell to Rubin, but rack pricing could increase by \$2-3mn (from \~\$3-4mn to \~\$6-7mn), driven by upgrades across compute, networking, and software. We therefore expect gross margins to remain around the mid-70% range.

## NVDA GPU sales up \~700x since ASICs launched in 2015

Google TPU (2015), Amazon Trainium (2020), and Meta MTIA (2023) have all been around, yet NVDA GPU revenue has grown \~700x since 2015. NVDA sales to hyperscaler rose 115% YoY, nearly 2x cloud capex growth, suggesting continued wallet-share gains. Over the long-term, we expect NVDA to sustain a 65-70%+ share of AI capex.

## Valuation already bakes in 30-35% EPS headwind

Despite similar AI opportunities and memory-cost pressures as Amazon, Meta, Google, Microsoft, and Apple, NVDA trades \~30-35% below their 22x/19x CY27/28E PE. We expect upcoming NVDA earnings to reinforce its moats in products, pricing, and supply chain. While ownership concentration (1.15x weighting, 78% ownership within active S&P 500 funds) and strategic investments (\~\$65bn) remain overhangs, we estimate the latter consumes <35% of FCF, leaving substantial capacity for dividends and buybacks.

<table><tr><td>Estimates (Jan) (US$)</td><td>2025A</td><td>2026A</td><td>2027E</td><td>2028E</td><td>2029E</td></tr><tr><td>EPS</td><td>2.83</td><td>4.55</td><td>9.09</td><td>13.27</td><td>18.04</td></tr><tr><td>GAAP EPS</td><td>2.94</td><td>4.90</td><td>9.59</td><td>13.08</td><td>17.79</td></tr><tr><td>EPS Change (YoY)</td><td>141.9%</td><td>60.8%</td><td>99.8%</td><td>46.0%</td><td>35.9%</td></tr><tr><td>Consensus EPS (Bloomberg)</td><td></td><td></td><td>8.99</td><td>12.94</td><td>NA</td></tr><tr><td>Consensus EPS (Visible Alpha)</td><td></td><td></td><td>8.95</td><td>12.59</td><td>15.30</td></tr><tr><td>DPS</td><td>0.03</td><td>0.04</td><td>0.76</td><td>1.15</td><td>1.38</td></tr><tr><td>Valuation (Jan)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>P/E</td><td>69.1x</td><td>43.0x</td><td>21.5x</td><td>14.7x</td><td>10.8x</td></tr><tr><td>GAAP P/E</td><td>66.5x</td><td>39.9x</td><td>20.4x</td><td>15.0x</td><td>11.0x</td></tr><tr><td>Dividend Yield</td><td>0%</td><td>0%</td><td>0.4%</td><td>0.6%</td><td>0.7%</td></tr><tr><td>EV / EBITDA*</td><td>57.3x</td><td>35.9x</td><td>17.9x</td><td>12.5x</td><td>9.5x</td></tr><tr><td>Free Cash Flow Yield*</td><td>1.3%</td><td>2.0%</td><td>3.8%</td><td>5.8%</td><td>7.9%</td></tr></table>

\* For full definitions of iQmethod $^{SM}$ measures, see page 11.

BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.
Refer to important disclosures on page 12 to 14. Analyst Certification on page 10. Price Objective Basis/Risk on page 10.
12991664

## 07 July 2026

Equity

Vivek Arya
Research Analyst
BofAS
vivek.arya@bofa.com

Duksan Jang
Research Analyst
BofAS
duksan.jang@bofa.com

Michael Mani
Research Analyst
BofAS
michael.mani@bofa.com

Liam Pharr
Research Analyst
BofAS
liam.pharr@bofa.com

## Stock Data

<table><tr><td>Price</td><td>195.55 USD</td></tr><tr><td>Price Objective</td><td>350.00 USD</td></tr><tr><td>Date Established</td><td>20-May-2026</td></tr><tr><td>Investment Opinion</td><td>C-1-7</td></tr><tr><td>52-Week Range</td><td>157.34 USD - 236.54 USD</td></tr><tr><td>Mrkt Val (mn) / Shares Out (mn)</td><td>4,865,284 USD / 24,880.0</td></tr><tr><td>Free Float</td><td>96.2%</td></tr><tr><td>Average Daily Value (mn)</td><td>32485.45 USD</td></tr><tr><td>BofA Ticker / Exchange</td><td>NVDA / NAS</td></tr><tr><td>Bloomberg / Reuters</td><td>NVDA US / NVDA.OQ</td></tr><tr><td>ROE (2027E)</td><td>95.9%</td></tr><tr><td>Net Dbt to Eqty (Jan-2026A)</td><td>-1.4%</td></tr></table>

See glossary on page 8

## iQprofile $^{SM}$ NVIDIA Corporation

iQmethod $^{SM}$ – Bus Performance\*

<table><tr><td>(US$ Millions)</td><td>2025A</td><td>2026A</td><td>2027E</td><td>2028E</td><td>2029E</td></tr><tr><td>Return on Capital Employed</td><td>100.4%</td><td>86.6%</td><td>90.4%</td><td>76.8%</td><td>67.3%</td></tr><tr><td>Return on Equity</td><td>114.7%</td><td>94.3%</td><td>95.9%</td><td>80.3%</td><td>69.3%</td></tr><tr><td>Operating Margin</td><td>66.5%</td><td>63.6%</td><td>68.5%</td><td>68.6%</td><td>69.0%</td></tr><tr><td>Free Cash Flow</td><td>60,855</td><td>96,677</td><td>186,824</td><td>282,008</td><td>384,596</td></tr></table>

## iQmethod $^{SM}$ – Quality of Earnings\*

<table><tr><td>(US$ Millions)</td><td>2025A</td><td>2026A</td><td>2027E</td><td>2028E</td><td>2029E</td></tr><tr><td>Cash Realization Ratio</td><td>0.9x</td><td>0.9x</td><td>0.9x</td><td>0.9x</td><td>1.0x</td></tr><tr><td>Asset Replacement Ratio</td><td>1.7x</td><td>2.1x</td><td>2.0x</td><td>2.0x</td><td>2.0x</td></tr><tr><td>Tax Rate</td><td>13.3%</td><td>15.1%</td><td>16.9%</td><td>18.0%</td><td>18.0%</td></tr><tr><td>Net Debt-to-Equity Ratio</td><td>-0.2%</td><td>-1.4%</td><td>-22.9%</td><td>-43.7%</td><td>-57.1%</td></tr><tr><td>Interest Cover</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr></table>

Income Statement Data (Jan)

<table><tr><td>(US$ Millions)</td><td>2025A</td><td>2026A</td><td>2027E</td><td>2028E</td><td>2029E</td></tr><tr><td>Sales</td><td>130,497</td><td>215,938</td><td>396,135</td><td>564,622</td><td>738,998</td></tr><tr><td>% Change</td><td>114.2%</td><td>65.5%</td><td>83.4%</td><td>42.5%</td><td>30.9%</td></tr><tr><td>Gross Profit</td><td>98,505</td><td>153,994</td><td>297,498</td><td>422,508</td><td>549,515</td></tr><tr><td>% Change</td><td>119.1%</td><td>56.3%</td><td>93.2%</td><td>42.0%</td><td>30.1%</td></tr><tr><td>EBITDA</td><td>83,915</td><td>133,755</td><td>268,142</td><td>385,165</td><td>508,478</td></tr><tr><td>% Change</td><td>139.3%</td><td>59.4%</td><td>100.5%</td><td>43.6%</td><td>32.0%</td></tr><tr><td>Net Interest &amp; Other Income</td><td>1,550</td><td>2,161</td><td>1,849</td><td>1,856</td><td>1,856</td></tr><tr><td>Net Income (Adjusted)</td><td>70,159</td><td>111,574</td><td>220,605</td><td>315,502</td><td>416,084</td></tr><tr><td>% Change</td><td>140.8%</td><td>59.0%</td><td>97.7%</td><td>43.0%</td><td>31.9%</td></tr></table>

## Free Cash Flow Data (Jan)

<table><tr><td>(US$ Millions)</td><td>2025A</td><td>2026A</td><td>2027E</td><td>2028E</td><td>2029E</td></tr><tr><td>Net Income from Cont Operations (GAAP)</td><td>72,880</td><td>120,067</td><td>232,803</td><td>310,989</td><td>410,216</td></tr><tr><td>Depreciation &amp; Amortization</td><td>1,864</td><td>2,842</td><td>4,839</td><td>6,897</td><td>9,028</td></tr><tr><td>Change in Working Capital</td><td>(9,383)</td><td>(15,948)</td><td>(34,980)</td><td>(31,079)</td><td>(26,402)</td></tr><tr><td>Deferred Taxation Charge</td><td>(4,476)</td><td>(1,424)</td><td>1,584</td><td>0</td><td>0</td></tr><tr><td>Other Adjustments, Net</td><td>3,206</td><td>(2,818)</td><td>(7,802)</td><td>9,317</td><td>10,230</td></tr><tr><td>Capital Expenditure</td><td>(3,236)</td><td>(6,042)</td><td>(9,620)</td><td>(14,116)</td><td>(18,475)</td></tr><tr><td>Free Cash Flow</td><td>60,855</td><td>96,677</td><td>186,824</td><td>282,008</td><td>384,596</td></tr><tr><td>% Change</td><td>125.2%</td><td>58.9%</td><td>93.2%</td><td>50.9%</td><td>36.4%</td></tr><tr><td>Share / Issue Repurchase</td><td>(33,217)</td><td>(39,443)</td><td>(74,092)</td><td>(112,803)</td><td>(153,839)</td></tr><tr><td>Cost of Dividends Paid</td><td>(834)</td><td>(974)</td><td>(18,479)</td><td>(27,493)</td><td>(32,080)</td></tr><tr><td>Change in Debt</td><td>(1,250)</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

Balance Sheet Data (Jan)

<table><tr><td>(US$ Millions)</td><td>2025A</td><td>2026A</td><td>2027E</td><td>2028E</td><td>2029E</td></tr><tr><td>Cash &amp; Equivalents</td><td>8,589</td><td>10,605</td><td>77,943</td><td>219,655</td><td>418,332</td></tr><tr><td>Trade Receivables</td><td>23,065</td><td>38,466</td><td>73,104</td><td>97,182</td><td>117,112</td></tr><tr><td>Other Current Assets</td><td>48,472</td><td>76,534</td><td>109,523</td><td>122,838</td><td>134,659</td></tr><tr><td>Property, Plant &amp; Equipment</td><td>6,283</td><td>10,383</td><td>16,424</td><td>23,642</td><td>33,089</td></tr><tr><td>Other Non-Current Assets</td><td>25,192</td><td>70,815</td><td>96,076</td><td>96,076</td><td>96,076</td></tr><tr><td>Total Assets</td><td>111,601</td><td>206,803</td><td>373,070</td><td>559,393</td><td>799,269</td></tr><tr><td>Short-Term Debt</td><td>0</td><td>999</td><td>1,000</td><td>1,000</td><td>1,000</td></tr><tr><td>Other Current Liabilities</td><td>18,047</td><td>31,164</td><td>49,228</td><td>55,542</td><td>60,891</td></tr><tr><td>Long-Term Debt</td><td>8,463</td><td>7,469</td><td>7,470</td><td>7,470</td><td>7,470</td></tr><tr><td>Other Non-Current Liabilities</td><td>5,764</td><td>9,878</td><td>12,646</td><td>12,646</td><td>12,646</td></tr><tr><td>Total Liabilities</td><td>32,274</td><td>49,510</td><td>70,344</td><td>76,658</td><td>82,007</td></tr><tr><td>Total Equity</td><td>79,327</td><td>157,293</td><td>302,726</td><td>482,735</td><td>717,262</td></tr><tr><td>Total Equity &amp; Liabilities</td><td>111,601</td><td>206,803</td><td>373,070</td><td>559,393</td><td>799,269</td></tr></table>

\* For full definitions of iQmethod $^{SM}$ measures, see page 11.

<table><tr><td>Company Sector</td></tr><tr><td>Semiconductors</td></tr></table>

## Company Description

Nvidia designs and sell graphics and video processing chips for desktop and notebook gaming PCs, workstations, game consoles, and accelerated computing servers and supercomputers.

## Investment Rationale

Our positive view on Nvidia is based on its unique full-stack and leadership in artificial intelligence silicon, hardware and software. The company's strong balance sheet and free cash flow returns further enables ecosystem investments and enhanced shareholder returns.

## Stock Data

<table><tr><td>Average Daily Volume</td><td>166,123,520</td></tr></table>

## Quarterly Earnings Estimates

<table><tr><td></td><td>2026</td><td>2027</td></tr><tr><td>Q1</td><td>0.76A</td><td>1.87A</td></tr><tr><td>Q2</td><td>0.99A</td><td>2.06E</td></tr><tr><td>Q3</td><td>1.24A</td><td>2.35E</td></tr><tr><td>Q4</td><td>1.56A</td><td>2.82E</td></tr></table>

## Memory inflation predictable, Price power un-appreciated

We believe investors simultaneously overestimate the GM impact of rising memory input cost, while underestimating NVDA's pricing power, long-range planning, product co-design, scale and supply chain alignment via over \$119bn in prepurchase commitments across memory, wafers, packaging and power.

To first order, NVDA high bandwidth memory content per rack goes up by \~\$0.2-0.3mn incrementally from Blackwell to Rubin, while product pricing is likely to go up by over \$2-3mn (from \$3-4mn/rack in Blackwell, to \$6-7mn/rack in Vera Rubin) because of the advancements in multiple other parts of the rack such as an upgraded Vera CPU, upgraded NVLink and Quantum Ethernet networking (none of which need HBM memory), and a host of other software features that speed-up (and lower cost) time to first token.

Moreover, we flag NVDA's comments that Vera Rubin can deliver 10x more performance per watt (\~10x lower inference token cost), 3.3x more powerful on inference, and up to 5x more powerful on training than Blackwell.

Overall we expect NVDA to maintain its roughly mid-70s GM, blended across its breadth of cloud, enterprise, neocloud, sovereign customers, and across its breadth of products in the rack-scale architecture.

Exhibit 1: We expect HBM \$/rack goes from \~\$150-300k/rack in Blackwell to \~\$400k/rack in Vera Rubin  
HBM cost per rack by GPU generation

<table><tr><td></td><td>Blackwell</td><td>Blackwell Ultra</td><td>Rubin</td><td>Rubin Ultra</td></tr><tr><td>GPU</td><td>B200</td><td>B300</td><td>V200</td><td>V300</td></tr><tr><td>Architecture</td><td>Oberon</td><td>Oberon</td><td>Oberon</td><td>Kyber</td></tr><tr><td>Ramp</td><td>2H24-2H25</td><td>2H25-2H26</td><td>2H26-2H27</td><td>2H27-2H28</td></tr><tr><td>GPUs/rack</td><td>72x</td><td>72x</td><td>72x</td><td>144x</td></tr><tr><td>HBM/GPU</td><td>192 GB</td><td>288 GB</td><td>288 GB</td><td>576 GB</td></tr><tr><td>HBM GB/rack</td><td>13,824 GB</td><td>20,736 GB</td><td>20,736 GB</td><td>82,944 GB</td></tr><tr><td>HBM Type</td><td>HBM3e</td><td>HBM3e</td><td>HBM4</td><td>HBM4e</td></tr><tr><td>$/GB</td><td>$11.26</td><td>$15.27</td><td>$18.40</td><td>$18.49</td></tr><tr><td>HBM $k/rack</td><td>$156</td><td>$317</td><td>$382</td><td>$1,534</td></tr><tr><td>ASP $k/rack</td><td>$3,000</td><td>$4,000</td><td>$6,000</td><td>$21,000</td></tr><tr><td>HBM % of rack cost</td><td>5.2%</td><td>7.9%</td><td>6.4%</td><td>7.3%</td></tr></table>

Source: BofA Global Research estimates  
BofA GLOBAL RESEARCH

## NVDA GPU revs up 700x since ASICs launched in 2015

NVDA has faced competition from custom ASIC since Google first launched its TPU in 2015, Amazon Trainium launched in 2020 and Meta MTIA in 2023. Despite these competitions, NVDA GPU accelerator sales have grown by a factor of 700x since 2015. In fact, per its new segment disclosure, NVDA sales to hyperscalers surged 115% YoY, nearly 2x the growth in cloud capex, suggesting growing rather than shrinking share of hyperscaler wallet. NVDA provides a widely available and supported platform, while ASICs are narrow products for a limited range of functionality, available only at that hyperscaler. Long-term we expect NVDA's breadth of AI products to help it maintain dominant (65-70%+) share of AI capex, with remaining 30-35% shared across ASICs and other merchant (AMD) vendors.

## Valuation already bakes in 30-35% EPS headwind

We believe that at a high level NVDA faces a similar set of opportunities (from AI) and potential headwinds (from memory inflation) as its fellow tech peers including Amazon, Meta, Google, Microsoft and Apple. Those 5 peers are currently trading at an average 22x/19x PE on consensus CY27/28 estimates, about 30-35% higher than NVDA's current valuation, which we attribute to an implied headwind/overhang from cost/competition arguments discussed above. We expect upcoming earnings call to be a positive catalyst, clarifying NVDA's durable moats across its products, pricing and supply chain.

Exhibit 2: NVDA is trading at 16x/12x CY27/28E PE, or at >40% average discount to its large tech peers at 22x/19x NVDA Valuation vs. Key Large Cap Tech/Hyperscaler Peers

<table><tr><td rowspan="2"></td><td rowspan="2">Mkt cap(in bn)</td><td colspan="3">P/E</td><td colspan="3">EV/FCF</td><td colspan="3">FCF Margin</td><td rowspan="2">SalesCAGR25-28E</td><td rowspan="2">EPS CAGR25-28E</td><td rowspan="2">PEG2027E</td></tr><tr><td>2026E</td><td>2027E</td><td>2028E</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Nvidia</td><td>$4,778</td><td>22.9x</td><td>15.7x</td><td>12.4x</td><td>23.3x</td><td>16.0x</td><td>13.1x</td><td>53%</td><td>54%</td><td>53%</td><td>48%</td><td>52%</td><td>0.3x</td></tr><tr><td>Apple</td><td>$4,587</td><td>35.0x</td><td>30.9x</td><td>28.5x</td><td>33.3x</td><td>29.4x</td><td>26.8x</td><td>28%</td><td>29%</td><td>31%</td><td>8%</td><td>11%</td><td>2.7x</td></tr><tr><td>Microsoft</td><td>$2,911</td><td>21.8x</td><td>18.7x</td><td>15.5x</td><td>73.5x</td><td>60.4x</td><td>38.2x</td><td>11%</td><td>12%</td><td>15%</td><td>18%</td><td>18%</td><td>1.0x</td></tr><tr><td>Google</td><td>$4,477</td><td>25.6x</td><td>24.1x</td><td>20.0x</td><td>211.3x</td><td>358.6x</td><td>85.8x</td><td>5%</td><td>2%</td><td>8%</td><td>22%</td><td>13%</td><td>1.9x</td></tr><tr><td>Amazon</td><td>$2,648</td><td>24.0x</td><td>21.4x</td><td>17.3x</td><td>-213.4x</td><td>179.5x</td><td>38.3x</td><td>-2%</td><td>2%</td><td>7%</td><td>13%</td><td>17%</td><td>1.3x</td></tr><tr><td>Meta</td><td>$1,583</td><td>15.9x</td><td>16.3x</td><td>13.4x</td><td>703.0x</td><td>615.7x</td><td>56.4x</td><td>1%</td><td>1%</td><td>8%</td><td>21%</td><td>14%</td><td>1.2x</td></tr><tr><td>Avg Ex-Nvidia</td><td>$3,241</td><td>24.5x</td><td>22.3x</td><td>19.0x</td><td>161.5x</td><td>248.7x</td><td>49.1x</td><td>9%</td><td>9%</td><td>14%</td><td>16%</td><td>15%</td><td>1.6x</td></tr><tr><td>Med Ex-Nvidia</td><td>$2,911</td><td>24.0x</td><td>21.4x</td><td>17.3x</td><td>73.5x</td><td>179.5x</td><td>38.3x</td><td>5%</td><td>2%</td><td>8%</td><td>18%</td><td>14%</td><td>1.3x</td></tr></table>

Source: BofA Global Research estimates, Bloomberg  
BofA GLOBAL RESEARCH

As the largest market cap in the S&P 500, NVDA's large ownership/positioning is likely to remain a headwind, at least until the market absorbs additional supply from new/upcoming tech stock issuance.

Exhibit 3: NVDA is owned at 1.15x weighting vs. its relative market cap within the S&P 500 index by active funds, vs. non-NVDA peer average of 1.28x NVDA relative weighting of active funds in S&P 500 vs. other key tech peers  
![](images/2b15d204c79ab995be1e2df93ebf91c2ea23dc142ae28a8b0abeda87ed4f6da7.jpg)  
Source: BofA Global Research estimates  
BofA GLOBAL RESEARCH

Exhibit 4: NVDA is owned by 78% of active funds of S&P 500 index, vs. non-NVDA peer average of 81% NVDA ownership of active funds in S&P 500 vs. other key tech peers  
![](images/d5c3b121a8110e33babfa98ab577e85d282c6fbf3703b0a12879b0063d44cf27.jpg)  
Source: BofA Global Research estimates  
BofA GLOBAL RESEARCH

Lastly, NVDA's investments across its supplier

[中间内容因长度限制已省略]

ailable material. Any unauthorized use or disclosure is prohibited. Receipt and review of this information constitutes your agreement not to redistribute, retransmit, or disclose to others the contents, opinions, conclusion, or information contained herein (including any investment recommendations, estimates or price targets) without first obtaining express permission from an authorized officer of BofA.

Materials prepared by BofA Global Research personnel are based on public information. Facts and views presented in this material have not been reviewed by, and may not reflect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Subject to the quiet period applicable under laws of the various jurisdictions in which we distribute research reports and other legal and BofA policy-related restrictions on the publication of research reports, fundamental equity reports are produced on a regular basis as necessary to keep the investment recommendation current.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.
"""
