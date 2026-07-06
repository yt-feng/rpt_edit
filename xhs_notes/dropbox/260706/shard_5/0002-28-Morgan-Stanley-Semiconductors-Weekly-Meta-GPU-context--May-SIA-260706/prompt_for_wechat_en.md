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
July 6, 2026 04:01 AM GMT

Semiconductors | North America

# Weekly: Meta GPU context; May SIA

We think that gpu compute remains in shortage, and recent events are more about stronger cloud demand vs. any excess compute capacity. Separately, May SIA #s were slightly below our forecast.

Last week, Bloomberg reported that Meta - covered by Brian Nowak & team - would develop a cloud services unit, competing with Azure, AWS, and others; the company has not finalized details about this offering. Our understanding is that this was at least part of the weakness in the stocks last week, in addition to a broader derisking.

To us, this points to excess demand for GPUs, more so than excess supply from any one hyperscaler: This is not the first report that we have heard of larger internally focused hyperscalers offering GPUs to others, and is something that we are hearing regularly. We would not jump to the negative conclusion that the market seems to be focused on - that these vendors have excess compute. An alternate explanation fits our checks more clearly - that there is a substantial shortage of GPU compute in the market right now, such that the most profitable use of GPUs might be to rent them to others. There is excess demand, more so than excess supply, at least on an industry-wide basis, and the highest utility use of a GPU might be to rent it to someone else.

While clearly some are doing better than others, we expect to hear about very strong cloud compute demand through earnings, across the board, and see this strong cloud backdrop as at least part of the story here.

Meta aside, this larger trend towards subletting GPUs - which we have seen in multiple places - should be a significant positive for NVIDIA market share, in our opinion. If there is a mismatch of compute - whether lower demand internally or higher demand externally - that demand is better served with the chip that is the defacto standard in the industry. ASIC capacity is much harder to sublet, especially for lower volume ASICs. AMD has more ubiquity than ASICs, which is helpful, but lower market share overall would point to a smaller secondary compute market.

NVIDIA made an important point at Computex, where they talked about NVDA offering by far the highest tokens per gigawatt by a large margin - but also offering better economics through faster bring up, longer mean time between failure, and longer asset life as driving better NVDA economics vs. competing solutions. We would certainly add ubiquity of compute as another key advantage.

Specifically at Meta, we do not perceive disruption, though their capex isn't the upside driver that we have seen in the past. At the moment, we are seeing upside in GPU demand from many places, and somewhat in contrast to prior years Meta

MS & CO. LLC

Joseph Moore
Equity Analyst
Joseph.Moore@morganstanley.com +1 212 761-7516

Nicole Kozhukhov
Research Associate
Nicole.Kozhukhov@morganstanley.com +1 212 761-1636

Research Associate
Ella.Tulchinsky@morganstanley.com +1 212 761-2222

Mason Wayne
Research Associate
Mason.Wayne@morganstanley.com +1 212 761-6012

Shane Brett
Equity Analyst
Shane.Brett@morganstanley.com +1 212 761-1022

## SEMICONDUCTORS

North America
Industry View
Attractive

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

isn't as notable an upside driver to GPU trends. We would not be alarmist about this, it's not a deceleration, as in each of the last few years leadership has transitioned from one customer to another.

We do expect Meta to be the early adopter of AMD Helios, though that doesn't seem to have impacted purchasing from NVIDIA that we can tell. The economics of the warrant structure is even more important given the appreciation in the share price of AMD; the warrants are effectively a 75% discount for at least the initial gigawatt, which is a substantial incentive for someone that has been AMD's biggest customer over the life of the MI300/350 families.

Overall SIA data was softer than expected for May, driven by both broad markets and memory. May Semiconductor Industry Association billings data reported on Saturday, July 4th, came in lower than our estimates and seasonality for broad markets and memory:

\- Overall: Sales were up 16.1% m/m, below our estimate of 22.0% though above the 10-yr average change of 6.9%. 3-month y/y growth accelerated to 104.2% from 93.9% in April, and one month y/y growth was 118.8%.

\- Trend by geography (y/y): The Americas (+150.7%) was followed by Asia Pacific (+126.3%), China (+101.9%), Europe (+83.7%), and Japan (+39.4%).

Broad markets decelerated following a strong April:

\- Discrete (miss): -6.9% m/m vs our estimate of -1.0% and the 10-yr average change of -0.9%. Units were below the 10-yr average (-4.1% vs -1.3%) and ASP was below (-2.9% vs -0.4%).

\- Analog (miss): -7.8% m/m vs our estimate of -2.0% and 10-yr average of -1.7%. Units were below the 10-yr average (-4.0% vs 1.5%) and ASP was below (-4.0% vs -3.0%).

\- MCU (in-line): -2.7% m/m vs our estimate of -2.0% and 10-yr average change of -2.1%. Units were above the 10-yr average (1.8% vs -0.8) and ASP was above (-4.4% vs -1.1%).

\- MPU (beat): 5.0% m/m vs our estimate of 3.2% and 10-yr average change of 1.8%.

May was softer than expected after a strong April, with both broad markets and memory coming in below our estimates. Even so, the broader cycle still appears to be improving and remains generally consistent with constructive JunQ supplier commentary. From our checks intra-quarter, Industrial continues to recover from cyclical lows and demand is broadening beyond AI-linked areas into more traditional end markets. On pricing, increases are still showing up across the supply chain, though the primary driver remains cost pass-through for the broader supply chain. AI remains the clear area of outperformance, and while we still do not see evidence of a true replenishment cycle, visibility into a stronger 2H continues to improve.

In analog, the 3-month average y/y growth held flat at 14.2%, led by General Purpose. MCUs' 3-month average y/y growth accelerated to 15.5% from 13.2% in April, led by General Purpose.

Exhibit 1: Global Semiconductor Sales  
![](images/b2da6a162d10d7b272549d0d12643f576b0c75f06982e7290d322f94b36efb9e.jpg)  
Source: SIA, MS

Exhibit 2: Semiconductor Sales by Region  
![](images/9800cbd3e19a82a8b6610e19026aeccf2e62d145b109055c37912cdb2a06f3cb.jpg)  
Source: SIA, MS

Memory was softer in May, likely reflecting supply constraints, with both NAND and DRAM underperforming our estimates while NAND was above seasonality:

\- DRAM: Below expectation and 5-yr average, coming in at 27.7% m/m vs our estimate of 43.0% m/m and 5-yr average of 45.9%. Bits were below our estimate (13.2% vs 30.0%) m/m, up 16.1% y/y), while ASP was above (12.9% vs 10.0%). On a 3-month y/y basis, total DRAM sales reached 304.8% in May, marking another new historical high since 2001, while ASP growth (218.3%) has now increased for ten consecutive quarters.

\- NAND: Slightly below expectation though above the 5-yr average, coming in at 40.7% m/m vs our estimate of 43.8% and 5-yr average of 25.6%. Bits were below our estimate (19.5% m/m vs 22.0%), while ASPs were in-line (up 17.8% m/m vs 17.9%- prices were up 281.6% y/y). On a 3-month average y/y basis, revenue reached 364.6% in May, also marking a new record in our dataset's history, while ASP growth of 277.5% also marked a new record. Volume decelerated slightly to 23.8% from 30.7% in April.

May data does not alter the core memory thesis; we have commented in the past that it is challenging to predict monthly trends when the drivers shifts from seasonal drivers to more linear supply drivers. What stands out now is not just constrained supply, but growing evidence that customers are trying to lock in access before the market loosens, reinforcing our view that this is a structurally constrained AI-led cycle rather than a conventional inventory recovery. DRAM remains the clearest bottleneck, while NAND is increasingly benefiting from tighter mix and better discipline than investors typically assume. Said differently, the key takeaway is no longer just that memory is tight, but that the industry is beginning to formalize that tightness in ways that could extend the earnings window. We continue to see memory as a key constraint on AI buildouts, supporting elevated DRAM pricing, a more durable NAND recovery, and continued preference for MU and SNDK.

Changes to our forecast: Our forecast comes down slightly from up 103% to up 99% for the year, mostly the moderation in memory volumes. Our CY26 memory forecast at \$847bn is slightly lower than our prior forecast but still up meaningfully from \$222bn last year. For CY27, we are assuming 24% growth y/y to \$1.95 trillion, mostly due to memory pricing rippling through - largely unchanged from our prior

## forecast.

Our take: May SIA being a bit slow is surprising given the generally positive tone of business across the broader markets during 2q, but it doesn't change our view that 2q will be generally a very strong quarter. Memory remains the clearest area of tightness, with DRAM still the main bottleneck to AI deployments and NAND also holding firmer than many expected. We continue to favor that exposure through MU and SNDK, given limited near-term supply flexibility and a pricing backdrop that still looks more durable than investors had expected. Outside memory, the May data is also supportive of a more constructive broad-market view, as improving conditions are no longer limited to AI-linked demand. That keeps us constructive on NVDA, AVGO, and CBRS in leading-edge logic, LRCX, KLAC, MKSI, and ON in cap equipment/supply-chain, and ADI and NXP in premium analog/MCU.

## SIA Note Charts

Exhibit 3: May 2026 Semiconductor Sales by Product (Y/Y)  
![](images/fb3286cb3d5dca55be3e3e7234fd44126722e6a78b1e2e0a17519ca0fc9cab91.jpg)  
Source: SIA, MS

Exhibit 4: Variance Table

<table><tr><td>Reported Item ($ mn)</td><td>May 2026 Actual</td><td>May 2026 Est.</td><td>Difference (Act-Est)</td><td>Last Mth</td><td>MoM</td><td>Last Yr</td><td>YoY</td><td>Last Mth (Before Revision)</td><td>Last Mth Revised vs. Reported</td></tr><tr><td>Discrete / Opto / Sensors Sales</td><td>7,936</td><td>8,435</td><td>-5.9%</td><td>8,521</td><td>-6.9%</td><td>6,923</td><td>14.6%</td><td>8,521</td><td></td></tr><tr><td>Analog Sales</td><td>7,297</td><td>7,758</td><td>-6.0%</td><td>7,917</td><td>-7.8%</td><td>6,548</td><td>11.4%</td><td>7,917</td><td></td></tr><tr><td>MCU Sales</td><td>1,993</td><td>2,008</td><td>-0.7%</td><td>2,049</td><td>-2.7%</td><td>1,666</td><td>19.6%</td><td>2,049</td><td>0</td></tr><tr><td>MPU Sales</td><td>6,034</td><td>5,929</td><td>1.8%</td><td>5,745</td><td>5.0%</td><td>4,615</td><td>30.8%</td><td>5,745</td><td>0</td></tr><tr><td>Total Micro Sales</td><td>8,257</td><td>8,160</td><td>1.2%</td><td>8,017</td><td>3.0%</td><td>6,515</td><td>26.7%</td><td>8,017</td><td>0</td></tr><tr><td>Total Logic (ex Micro) Sales</td><td>33,853</td><td>33,546</td><td>0.9%</td><td>32,569</td><td>3.9%</td><td>22,800</td><td>48.5%</td><td>32,569</td><td></td></tr><tr><td>Total Logic Sales</td><td>42,109</td><td>41,706</td><td>1.0%</td><td>40,586</td><td>3.8%</td><td>29,314</td><td>43.6%</td><td>40,586</td><td></td></tr><tr><td>DRAM Sales</td><td>47,978</td><td>53,720</td><td>-10.7%</td><td>37,566</td><td>27.7%</td><td>11,730</td><td>309.0%</td><td>37,566</td><td>0</td></tr><tr><td>DRAM Gigabit Equivalents</td><td>32,158,182</td><td>36,942,211</td><td>-13.0%</td><td>28,417,085</td><td>13.2%</td><td>27,705,526</td><td>16.1%</td><td>28,417,085</td><td>0</td></tr><tr><td>DRAM Price per Gb Equivalent</td><td>$1.4919</td><td>$1.4542</td><td>2.6%</td><td>$1.3220</td><td>12.9%</td><td>$0.4234</td><td>252.4%</td><td>$1.3220</td><td>$0.0000</td></tr><tr><td>NAND Sales</td><td>25,811</td><td>26,377</td><td>-2.1%</td><td>18,349</td><td>40.7%</td><td>5,410</td><td>377.1%</td><td>18,349</td><td></td></tr><tr><td>NAND 1 Gigabit Equivalent</td><td>732,553,576</td><td>747,996,074</td><td>-2.1%</td><td>613,243,576</td><td>19.5%</td><td>662,338,864</td><td>10.6%</td><td>613,243,576</td><td></td></tr><tr><td>NAND Price per Gb Equivalent</td><td>$0.0352</td><td>$0.0353</td><td>-0.1%</td><td>$0.0299</td><td>17.8%</td><td>$0.0082</td><td>331.4%</td><td>$0.0299</td><td></td></tr><tr><td>Total Memory Sales</td><td>74,596</td><td>80,835</td><td>-7.7%</td><td>56,654</td><td>31.7%</td><td>17,522</td><td>325.7%</td><td>56,654</td><td>0</td></tr><tr><td>Total ICs</td><td>124,002</td><td>130,299</td><td>-4.8%</td><td>105,156</td><td>17.9%</td><td>53,384</td><td>132.3%</td><td>105,156</td><td>0</td></tr><tr><td>Semiconductor Sales</td><td>131,938</td><td>138,734</td><td>-4.9%</td><td>113,677</td><td>16.1%</td><td>60,307</td><td>118.8%</td><td>113,677</td><td>0</td></tr></table>

Source: SIA, MS

Exhibit 5: Quarterly SIA Data

<table><tr><td></td><td>Mar/24A</td><td>Jun/24A</td><td>Sep/24A</td><td>Dec/24A</td><td>Mar/25A</td><td>Jun/25A</td><td>Sep/25A</td><td>Dec/25A</td><td>Mar/26A</td><td>Jun/26E</td><td>Sep/26E</td><td>Dec/26E</td></tr><tr><td colspan="13">Revenues ($ Millions)</td></tr><tr><td>Discretes / Optos / Sensors</td><td>22,185</td><td>21,383</td><td>24,285</td><td>23,191</td><td>21,519</td><td>22,629</td><td>25,449</td><td>24,905</td><td>23,996</td><td>25,106</td><td>27,392</td><td>27,254</td></tr><tr><td>Analog</td><td>19,276</td><td>19,011</td><td>20,648</td><td>20,653</td><td>19,813</td><td>20,186</td><td>23,052</td><td>23,396</td><td>22,756</td><td>23,531</td><td>25,365</td><td>25,727</td></tr><tr><td>MCU</td><td>5,751</td><td>5,409</td><td>5,512</td><td>5,087</td><td>4,950</td><td>5,326</td><td>5,694</td><td>5,628</td><td>5,788</td><td>6,433</td><td>6,700</td><td>6,688</td></tr><tr><td>MPU</td><td>12,124</td><td>13,276</td><td>13,911</td><td>14,860</td><td>13,606</td><td>13,943</td><td>15,894</td><td>17,615</td><td>16,548</td><td>18,295</td><td>19,644</td><td>20,826</td></tr><tr><td>Other</td><td>651</td><td>658</td><td>690</td><td>703</td><td>728</td><td>752</td><td>813</td><td>758</td><td>565</td><td>683</td><td>100</td><td>100</td></tr><tr><td>Total Micro</td><td>18,526</td><td>19,343</td><td>20,114</td><td>20,650</td><td>19,284</td><td>20,021</td><td>22,401</td><td>24,011</td><td>22,902</td><td>25,412</td><td>26,445</td><td>27,614</td></tr><tr><td>Logic (ex Micro)</td><td>48,462</td><td>49,479</td><td>56,194</td><td>61,634</td><td>65,356</td><td>68,892</td><td>78,853</td><td>88,783</td><td>91,117</td><td>101,967</td><td>110,263</td><td>117,750</td></tr><tr><td>Total Logic</td><td>66,988</td><td>68,822</td><td>76,307</td><td>82,283</td><td>84,640</td><td>88,913</td><td>101,254</td><td>112,794</td><td>114,019</td><td>127,379</td><td>136,708</td><td>145,364</td></tr><tr><td>DRAM</td><td>18,175</td><td>22,269</td><td>26,173</td><td>28,243</td><td>27,074</td><td>31,635</td><td>39,949</td><td>51,939</td><td>93,436</td><td>135,769</td><td>155,616</td><td>177,742</td></tr><tr><td>NAND</td><td>13,472</td><td>17,813</td><td>18,003</td><td>17,140</td><td>12,617</td><td>15,404</td><td>17,382</td><td>22,282</td><td>42,794</td><td>66,484</td><td>81,979</td><td>89,151</td></tr><tr><td>Other</td><td>1,039</td><td>1,010</td><td>1,133</td><td>1,048</td><td>1,070</td><td>1,154</td><td>1,310</td><td>1,329</td><td>1,544</td><td>7,459</td><td>7,459</td><td>7,459</td></tr><tr><td>Total Memory</td><td>32,685</td><td>41,092</td><td>45,308</td><td>46,431</td><td>40,761</td><td>48,193</td><td>58,641</td><td>75,550</td><td>137,775</td><td>209,712</td><td>245,055</td><td>274,352</td></tr><tr><td>Total ICs</td><td>118,949</td><td>128,925</td><td>142,263</td><td>149,367</td><td>145,214</td><td>157,293</td><td>182,946</td><td>211,740</td><td>274,550</td><td>360,622</td><td>407,127</td><td>445,444</td></tr><tr><td>Total Semiconductor</td><td>141,134</td><td>150,308</td><td>166,547</td><td>172,558</td><td>166,732</td><td>179,921</td><td>208,395</td><td>236,645</td><td>298,546</td><td>385,728</td><td>434,519</td><td>472,697</td></tr><tr><td>Q/Q Change</td><td>-3.3%</td><td>6.5%</td><td>10.8%</td><td>3.6%</td><td>-3.4%</td><td>7.9%</td><td>15.8%</td><td>13.6%</td><td>26.2%</td><td>29.2%</td><td>12.6%</td><td>8.8%</td></tr><tr><td>Y/Y Change</td><td>18.1%</td><td>18.6%</td><td>23.7%</td><td>18.2%</td><td>18.1%</td><td>19.7%</td><td>25.1%</td><td>37.1%</td><td>79.1%</td><td>114.4%</td><td>108.5%</td><td>99.7%</td></tr></table>

Source: SIA, MS

Exhibit 6: Annual SIA Data

<table><tr><td></td><td>2010A</td><td>2017A</td><td>2018A</td><td>2019A</td><td>2020A</td><td>2021A</td><td>2022A</td><td>2023A</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td colspan="13">Revenues ($ Millions)</td></tr><tr><td>Discretes / Optos / Sensors</td><td>48,406</td><td>69,087</td><td>75,446</td><td>78,953</td><td>79,164</td><td>92,945</td><td>99,591</td><td>98,359</td><td>91,044</td><td>94,502</td><td>103,748</td><td>109,730</td></tr><tr><td>Analog</td><td>42,285</td><td>53,069</td><td>58,380</td><td>53,939</td><td>55,658</td><td>73,816</td><td>88,919</td><td>81,146</td><td>79,588</td><td>86,447</td><td>97,379</td><td>105,203</td></tr><tr><td>MCU</td><td>14,799</td><td>16,430</td><td>17,027</td><td>15,808</td><td>15,484</td><td>19,622</td><td>25,030</td><td>27,861</td><td>21,758</td><td>21,597</td><td>25,610</td><td>28,331</td></tr><tr><td>MPU</td><td>39,927</td><td>44,370</td><td>46,371</td><td>47,974</td><td>51,812</td><td>56,766</td><td>51,299</td><td>45,480</td><td>54,172</td><td>61,059</td><td>75,313</td><td>84,108</td></tr><tr><td>Other</td><td>5,908</td><td>3,286</td><td>3,262</td><td>2,658</td><td>2,382</td><td>2,845</td><td>3,217</td><td>3,172</td><td>2,702</td><td>3,062</td><td>1,449</td><td>400</td></tr><tr><td>Total Micro</td><td>60,633</td><td>64,086</td><td>66,660</td><td>66,440</td><td>69,678</td><td>79,234</td><td>79,546</td><td>76,513</td><td>78,633</td><td>85,718</td><td>102,372</td><td>112,839</td></tr><tr><td>Logic (ex Micro)</td><td>77,377</td><td>102,196</td><td>109,411</td><td>106,535</td><td>118,408</td><td>153,710</td><td>176,097</td><td>178,493</td><td>215,768</td><td>301,883</td><td>421,098</td><td>503,416</td></tr><tr><td>Total Logic</td><td>138,010</td><td>166,281</td><td>176,071</td><td>172,975</td><td>188,086</td><td>232,944</td><td>255,643</td><td>255,006</td><td>294,401</td><td>387,601</td><td>523,470</td><td>616,256</td></tr><tr><td>DRAM</td><td>39,210</td><td>72,802</td><td>98,604</td><td>6

[中间内容因长度限制已省略]

riteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## INDUSTRY COVERAGE: Semiconductors

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/02/2026)</td></tr><tr><td colspan="3">Joseph Moore</td></tr><tr><td>Advanced Micro Devices (AMD.O)</td><td>E (06/09/2024)</td><td>$517.82</td></tr><tr><td>Aeva Technologies Inc (AEVA.O)</td><td>E (07/19/2021)</td><td>$23.98</td></tr><tr><td>Allegro Microsystems Inc (ALGM.O)</td><td>O (02/13/2026)</td><td>$55.49</td></tr><tr><td>Ambarella Inc (AMBA.O)</td><td>O (03/29/2016)</td><td>$78.36</td></tr><tr><td>Amkor Technology Inc (AMKR.O)</td><td>E (11/08/2023)</td><td>$69.65</td></tr><tr><td>Analog Devices Inc. (ADI.O)</td><td>O (11/16/2023)</td><td>$377.16</td></tr><tr><td>Astera Labs Inc (ALAB.O)</td><td>O (05/11/2025)</td><td>$406.42</td></tr><tr><td>Broadcom Inc. (AVGO.O)</td><td>O (06/09/2024)</td><td>$360.45</td></tr><tr><td>Cerebras Systems (CBRS.O)</td><td>O (06/08/2026)</td><td>$204.86</td></tr><tr><td>GlobalFoundries Inc (GFS.O)</td><td>E (10/28/2024)</td><td>$69.84</td></tr><tr><td>Intel Corporation (INTC.O)</td><td>E (02/22/2023)</td><td>$120.35</td></tr><tr><td>IonQ Inc (IONQ.N)</td><td>E (04/25/2023)</td><td>$49.12</td></tr><tr><td>Marvell Technology Group Ltd (MRVL.O)</td><td>E (09/14/2015)</td><td>$245.29</td></tr><tr><td>Microchip Technology Inc. (MCHP.O)</td><td>E (07/10/2024)</td><td>$84.64</td></tr><tr><td>Micron Technology Inc. (MU.O)</td><td>O (10/06/2025)</td><td>$975.56</td></tr><tr><td>Navitas Semiconductor Corp (NVTS.O)</td><td>U (04/06/2025)</td><td>$14.46</td></tr><tr><td>NVIDIA Corp. (NVDA.O)</td><td>O (03/16/2023)</td><td>$194.83</td></tr><tr><td>NXP Semiconductor NV (NXPI.O)</td><td>O (02/11/2025)</td><td>$273.36</td></tr><tr><td>ON Semiconductor Corp. (ON.O)</td><td>++</td><td>$91.22</td></tr><tr><td>Qorvo Inc (QRVO.O)</td><td>E (10/28/2025)</td><td>$87.57</td></tr><tr><td>Qualcomm Inc. (QCOM.O)</td><td>E (06/24/2026)</td><td>$176.25</td></tr><tr><td>Quantinuum (QNT.O)</td><td>E (06/29/2026)</td><td>$74.56</td></tr><tr><td>SanDisk Corporation. (SNDK.O)</td><td>O (03/03/2025)</td><td>$1,745.00</td></tr><tr><td>Semtech Corp. (SMTC.O)</td><td>E (04/06/2025)</td><td>$135.27</td></tr><tr><td>Silicon Laboratories Inc. (SLAB.O)</td><td>E (01/19/2021)</td><td>$218.22</td></tr><tr><td>Skyworks Solutions Inc (SWKS.O)</td><td>E (11/28/2018)</td><td>$62.56</td></tr><tr><td>Texas Instruments (TXN.O)</td><td>U (04/13/2020)</td><td>$293.08</td></tr><tr><td>Wolfspeed, INC (WOLF.N)</td><td>NR (04/06/2025)</td><td>$40.00</td></tr><tr><td colspan="3">Lee Simpson</td></tr><tr><td>Arm Holdings plc (ARM.O)</td><td>E (04/07/2026)</td><td>$315.28</td></tr><tr><td>Cadence Design Systems Inc (CDNS.O)</td><td>O (02/14/2024)</td><td>$373.14</td></tr><tr><td>Synopsys Inc. (SNPS.O)</td><td>E (02/27/2026)</td><td>$437.16</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## © 2026 MS
"""
