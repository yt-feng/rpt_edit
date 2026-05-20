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
18 May 2026 05:00:00 ET | 20 pages

# US Semiconductors

CPU TAM of \$132B by 2030E; Raising TPs on INTC & AMD

# CITI'S TAKE

We introduce our server CPU TAM model that includes general purpose CPUs, AI head nodes, and agentic CPU applications. We forecast the CPU TAM to expand to \$132B by 2030 or a 35% CAGR, led by agentic CPU growth of an 185% CAGR. We increase our TPs on Buy-rated INTC and Neutral-rated AMD to align with our updated CPU model.

Citi CPU TAM Model — We introduce our server CPU TAM model that includes general purpose CPUs, AI head nodes, and agentic CPU applications. We believe the CPU TAM could expand from \$29.3 billion in 2025 to \$131.5 billion in 2030, or a 35% CAGR. We expect general purpose CPUs to grow at a 20% CAGR to \$50.9 billion in 2030, AI head nodes to grow at a 21% CAGR to \$21.1 billion in 2030, and agentic CPUs to grow at a 185% CAGR to \$59.4 billion in 2030. We model general purpose CPUs to represent 39% of the TAM in 2030, AI head nodes to represent 16% of the TAM in 2030, and agentic CPUs to represent 45% of the TAM in 2030. For reference, ARM (covered by Andrew Gardiner) forecasted a TAM of \$100 billion by 2030 and AMD forecasted a TAM of \$120 billion by 2030. By 2030, we expect Intel to have 47% share, AMD to have 34% share, and ARM/Others to have 19% share.

INTC — We raise our data center sales estimates to reflect our updated CPU model, potential upside from Intel's ASIC business, namely its Mount Evans IPU that is used by Google and extends to Anthropic. We lift our price target to \$130 using our updated SOTP valuation.

AMD — We raise our data center sales estimates to reflect our updated CPU model. We believe AMD has won Anthropic as a customer for MI450 AI accelerator, based on our discussions with industry contacts, and expect AMD to announce it at Advancing AI day in July. We believe AMD could be the primary beneficiary of the CPU renaissance given its performance leadership and capacity allocation at TSMC. While we are constructive on AMD's CPU opportunity on agentic AI demand, we await the release and success of its next-gen GPU product MI450 and Helios racks. We lift our price target to \$460 using our updated SOTP valuation.

# Atif Malik $^{AC}$

+1-415-951-1892

atif.malik@citi.com

Kelsey Chia, CFA

+1-415-951-1791

kelsey.chia@citi.com

James Bowlin

+1-415-951-1790

james.bowlin@citi.com

Data Summary 

<table><tr><td rowspan="2" colspan="6"></td><td rowspan="2" colspan="2">Rating</td><td rowspan="3">Short-Term View</td><td rowspan="2" colspan="2">Target Price</td><td rowspan="2" colspan="4"></td><td colspan="2">Current Fiscal Year</td><td colspan="2">Next Fiscal Year</td></tr><tr><td colspan="2">EPS</td><td colspan="2">EPS</td></tr><tr><td>Company</td><td>Ticker</td><td>Ccy</td><td>Price</td><td>Mkt Cap (M)</td><td>Date &amp; Time</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td>ESPR (%)</td><td>Div Yld (%)</td><td>ETR (%)</td><td>Last Rpt Yr</td><td>Old</td><td>New</td><td>Old</td><td>New</td></tr><tr><td>Advanced Micro Devices</td><td>AMD</td><td>US$</td><td>424.10</td><td>691,538</td><td>15 May 16:00</td><td>2</td><td>nc</td><td>-</td><td>358.00</td><td>460.00</td><td>8.5</td><td>0.0</td><td>8.5</td><td>Dec-25</td><td>8.26</td><td>nc</td><td>14.67</td><td>14.41</td></tr><tr><td>Intel Corp</td><td>INTC</td><td>US$</td><td>108.77</td><td>546,678</td><td>15 May 16:00</td><td>1</td><td>nc</td><td>-</td><td>95.00</td><td>130.00</td><td>19.5</td><td>0.0</td><td>19.5</td><td>Dec-25</td><td>0.63</td><td>0.67</td><td>1.24</td><td>1.27</td></tr><tr><td colspan="6">1 = Buy, 2 = Neutral, 3 = Sell, H = High RiskSource: Citi</td><td colspan="13">ESPR = Expected Share Price Return, ETR = Expected Total Return, nc = no change^Catalyst Watch</td></tr></table>

# CPU Market TAM Update

# Introducing server CPU model TAM of \$132 billion by 2030E

We introduce our server CPU TAM model that includes general purpose CPUs, AI head nodes, and agentic CPU applications. We believe the CPU TAM could expand from \$29.3 billion in 2025 to \$131.5 billion in 2030, or a 35% CAGR. We expect general purpose CPUs to grow at a 20% CAGR to \$50.9 billion in 2030, AI head nodes to grow at a 21% CAGR to \$21.1 billion in 2030, and agentic CPUs to grow at a 185% CAGR to \$59.4 billion in 2030. We model general purpose CPUs to represent 39% of the TAM in 2030, AI head nodes to represent 16% of the TAM in 2030, and agentic CPUs to represent 45% of the TAM by 2030. For reference, ARM forecasted a TAM of \$100 billion by 2030 and AMD forecasted a TAM of \$120 billion by 2030.

Figure 1. Citi CPU TAM Model (\$M) 

<table><tr><td>TAM Estimates ($M)</td><td>C25</td><td>C26E</td><td>C27E</td><td>C28E</td><td>C29E</td><td>C30E</td></tr><tr><td>General Purpose CPU</td><td>$20,756</td><td>$29,376</td><td>$35,206</td><td>$39,724</td><td>$46,531</td><td>$50,933</td></tr><tr><td>% of Total</td><td>71%</td><td>57%</td><td>50%</td><td>46%</td><td>42%</td><td>39%</td></tr><tr><td>YoY</td><td></td><td>42%</td><td>20%</td><td>13%</td><td>17%</td><td>9%</td></tr><tr><td>AI Headnodes</td><td>$8,197</td><td>$12,148</td><td>$15,549</td><td>$17,246</td><td>$19,247</td><td>$21,139</td></tr><tr><td>% of Total</td><td>28%</td><td>24%</td><td>22%</td><td>20%</td><td>17%</td><td>16%</td></tr><tr><td>YoY</td><td></td><td>48%</td><td>28%</td><td>11%</td><td>12%</td><td>10%</td></tr><tr><td>Agentic CPU Applications</td><td>$313</td><td>$9,989</td><td>$18,986</td><td>$29,207</td><td>$46,088</td><td>$59,396</td></tr><tr><td>% of Total</td><td>1%</td><td>19%</td><td>27%</td><td>34%</td><td>41%</td><td>45%</td></tr><tr><td>YoY</td><td></td><td>3086%</td><td>90%</td><td>54%</td><td>58%</td><td>29%</td></tr><tr><td>Total</td><td>$29,266</td><td>$51,512</td><td>$69,741</td><td>$86,176</td><td>$111,866</td><td>$131,468</td></tr><tr><td>YoY</td><td></td><td>76%</td><td>35%</td><td>24%</td><td>30%</td><td>18%</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: Citi, Mercury Research

We model total server CPU units to grow from 29.2 million units in 2025 to 62.6 million units in 2030, or a 16% CAGR. We believe Intel units could grow at a 10% CAGR, AMD units could grow at a 24% CAGR, and ARM units could grow at a 24% CAGR.

Figure 2. Citi Server CPU Unit Model 

<table><tr><td>Unit Model (M)</td><td>C25</td><td>C26E</td><td>C27E</td><td>C28E</td><td>C29E</td><td>C30E</td></tr><tr><td>CPU Units (M)</td><td>29,210</td><td>40,465</td><td>47,145</td><td>50,078</td><td>57,709</td><td>62,600</td></tr><tr><td>YoY</td><td>21%</td><td>39%</td><td>17%</td><td>6%</td><td>15%</td><td>8%</td></tr><tr><td>Intel</td><td>17,943</td><td>22,426</td><td>25,300</td><td>26,013</td><td>27,787</td><td>29,320</td></tr><tr><td>YoY</td><td>6%</td><td>25%</td><td>13%</td><td>3%</td><td>7%</td><td>6%</td></tr><tr><td>AMD</td><td>7,240</td><td>11,319</td><td>14,641</td><td>16,761</td><td>20,549</td><td>21,440</td></tr><tr><td>YoY</td><td>32%</td><td>56%</td><td>29%</td><td>14%</td><td>23%</td><td>4%</td></tr><tr><td>ARM/Others</td><td>4,027</td><td>6,719</td><td>7,204</td><td>7,304</td><td>9,372</td><td>11,840</td></tr><tr><td>YoY</td><td>127%</td><td>67%</td><td>7%</td><td>1%</td><td>28%</td><td>26%</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: Citi, Mercury Research

By 2030, we expect Intel to have 47% share, AMD to have 34% share, and ARM/Others to have 19% share. We believe AMD could be the primary beneficiary of the CPU renaissance given its performance leadership and capacity allocation at TSMC.

Figure 3. Citi Server Market Share Forecast 

<table><tr><td>Unit Market Share (%)</td><td>C25</td><td>C26E</td><td>C27E</td><td>C28E</td><td>C29E</td><td>C30E</td></tr><tr><td>Intel</td><td>61%</td><td>55%</td><td>54%</td><td>52%</td><td>48%</td><td>47%</td></tr><tr><td>YoY</td><td>-859 bps</td><td>-600 bps</td><td>-176 bps</td><td>-172 bps</td><td>-379 bps</td><td>-131 bps</td></tr><tr><td>AMD</td><td>25%</td><td>28%</td><td>31%</td><td>33%</td><td>36%</td><td>34%</td></tr><tr><td>YoY</td><td>214 bps</td><td>319 bps</td><td>308 bps</td><td>241 bps</td><td>214 bps</td><td>-136 bps</td></tr><tr><td>ARM/Others</td><td>14%</td><td>17%</td><td>15%</td><td>15%</td><td>16%</td><td>19%</td></tr><tr><td>YoY</td><td>645 bps</td><td>282 bps</td><td>-132 bps</td><td>-70 bps</td><td>166 bps</td><td>267 bps</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: Citi, Mercury Research

# 1Q26 Market Share Data

AMD and ARM continued to gain unit share over Intel in 1Q26. Intel's server MPU share was down 372 basis points QoQ from $58.7\%$ in 4Q25 to $54.9\%$ in 1Q26 on server CPU supply constraints. AMD's server MPU share was up 228 basis points QoQ from $25.1\%$ in 4Q25 to $27.4\%$ in 1Q26 on strong CPU demand and share gains. ARM's server MPU share was up 145 basis points QoQ from $16.3\%$ in 4Q25 to $17.7\%$ in 1Q26, driven by Nvidia GB200 strength and increased internal server adoption by the CSPs.

Figure 4. Server MPU Unit Share, 1Q21-1Q26   
![](images/0b15a64fb66f445f164336ff17cc535da47b205cc5aa151908838b2846f81772.jpg)

<details>
<summary>line</summary>

| Quarter | Intel (%) | AMD (%) | ARM (%) |
|---|---|---|---|
| 1Q21 | 90.4 | 8.9 | 0.7 |
| 2Q21 | 90.0 | 9.5 | 0.7 |
| 3Q21 | 89.5 | 10.0 | 0.7 |
| 4Q21 | 89.0 | 10.5 | 0.7 |
| 1Q22 | 88.5 | 11.0 | 0.7 |
| 2Q22 | 86.0 | 13.0 | 0.7 |
| 3Q22 | 82.0 | 17.0 | 1.0 |
| 4Q22 | 80.5 | 17.5 | 2.0 |
| 1Q23 | 79.5 | 17.5 | 3.5 |
| 2Q23 | 78.0 | 17.5 | 5.0 |
| 3Q23 | 72.0 | 21.5 | 6.5 |
| 4Q23 | 72.5 | 21.5 | 6.5 |
| 1Q24 | 72.0 | 22.0 | 6.5 |
| 2Q24 | 71.5 | 22.5 | 6.5 |
| 3Q24 | 71.0 | 22.5 | 6.5 |
| 4Q24 | 68.0 | 23.5 | 9.0 |
| 1Q25 | 65.0 | 24.5 | 11.5 |
| 2Q25 | 63.0 | 25.5 | 12.5 |
| 3Q25 | 61.0 | 25.0 | 14.5 |
| 4Q25 | 59.0 | 26.0 | 16.5 |
| 1Q26 | 54.9 | 27.4 | 17.7 |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: Citi, Mercury Research

AMD gained revenue CPU share over Intel in 1Q26. Intel's server MPU revenue share was down 492 basis points QoQ from $58.7\%$ in 4Q25 to $53.8\%$ in 1Q26. AMD's server MPU revenue share was up 492 basis points QoQ from $41.3\%$ in 4Q25 to $46.2\%$ in 1Q26.

Figure 5. Server MPU Revenue Share, 1Q21-1Q26   
![](images/ab4f372918abe4cde4cba5bbc2afd8baba954b079fef26f6575b084bc8e57ede.jpg)

<details>
<summary>line</summary>

| Quarter | Intel (%) | AMD (%) |
|---|---|---|
| 1Q21 | 89.2 | 10.8 |
| 4Q21 | 85.0 | 13.0 |
| 1Q22 | 82.0 | 17.0 |
| 2Q22 | 76.0 | 24.0 |
| 3Q22 | 72.0 | 28.0 |
| 4Q22 | 72.0 | 28.0 |
| 1Q23 | 72.0 | 28.0 |
| 2Q23 | 73.0 | 27.0 |
| 3Q23 | 69.0 | 31.0 |
| 4Q23 | 68.0 | 32.0 |
| 1Q24 | 67.0 | 33.0 |
| 2Q24 | 66.0 | 34.0 |
| 3Q24 | 66.0 | 34.0 |
| 4Q24 | 64.0 | 36.0 |
| 1Q25 | 61.0 | 39.0 |
| 2Q25 | 60.0 | 39.0 |
| 3Q25 | 61.0 | 39.0 |
| 4Q25 | 59.0 | 41.0 |
| 1Q26 | 53.8 | 46.2 |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: Citi, Mercury Research

# Intel

Last week, the WSJ (May 8, 2026) reported (citing people familiar with the matter) that Intel and Apple have reached a preliminary agreement for Intel to manufacture some of Apple's chips. While the details weren't specific, Intel traded up $15\%$ on the news. We previously wrote that it was reported in the media that Apple was evaluating using Intel Foundry to manufacture its M-series chips (please see note). We expect a formal announcement of this deal in the coming months as we believe Apple is incentivized to diversity its supply chain. We also believe Intel will likely sign Nvidia as a foundry customer for gaming GPUs, based on our conversations with industry contacts.

We are also raising our data center sales estimates on Intel as we expect upside from Intel's ASIC business, namely its Mount Evans IPU that is used by Google and extends to Anthropic. We are raising our price target on Intel from \$95 to \$130 using our SOTP valuation framework. We raise our C27 sales estimate by 3% to account for higher foundry and data center sales and raise our C27 EPS estimate by 2%.

Figure 6. Raising C26 EPS by 4%, Raising C27 EPS by 2% 

<table><tr><td></td><td>Old</td><td>New</td><td></td><td>Old</td><td>New</td><td></td></tr><tr><td>FY end: December</td><td>2026E</td><td>2026E</td><td>Delta</td><td>2027E</td><td>2027E</td><td>Delta</td></tr><tr><td>Total Revenue</td><td>57,477.0</td><td>58,577.0</td><td>2%</td><td>63,100.0</td><td>64,700.0</td><td>3%</td></tr><tr><td>% Change Y/Y</td><td>8.7%</td><td>10.8%</td><td></td><td>9.8%</td><td>10.5%</td><td></td></tr><tr><td>% Change Q/Q</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Gross Margins</td><td>40.1%</td><td>40.4%</td><td>26 bps</td><td>45.2%</td><td>45.1%</td><td>-6 bps</td></tr><tr><td>SG&amp;A</td><td>4,478.5</td><td>4,566.0</td><td>2.0%</td><td>5,048.0</td><td>5,176.0</td><td>2.5%</td></tr><tr><td>% Total Revenue</td><td>7.8%</td><td>7.8%</td><td>0.0%</td><td>8.0%</td><td>8.0%</td><td>0.0%</td></tr><tr><td>R&amp;D</td><td>13,983.0</td><td>14,250.5</td><td>1.9%</td><td>14,978.5</td><td>15,358.0</td><td>2.5%</td></tr><tr><td>% Total Revenue</td><td>24.3%</td><td>24.3%</td><td>0.0%</td><td>23.7%</td><td>23.7%</td><td>0.0%</td></tr><tr><td>Operating Margins %</td><td>8.0%</td><td>8.3%</td><td>26 bps</td><td>13.5%</td><td>13.4%</td><td>-6 bps</td></tr><tr><td>Other Income (Expense)</td><td>340</td><td>340</td><td>0%</td><td>40</td><td>40</td><td>0%</td></tr><tr><td>Pretax Income</td><td>4,945</td><td>5,185</td><td>5%</td><td>8,528</td><td>8,702</td><td>2%</td></tr><tr><td>% Total Revenue</td><td>8.6%</td><td>8.9%</td><td>3%</td><td>13.5%</td><td>13.4%</td><td>0%</td></tr><tr><td>Tax Rate</td><td>12.9%</td><td>12.9%</td><td>0%</td><td>12.0%</td><td>12.0%</td><td>0%</td></tr><tr><td>Net Income attributable to Intel</td><td>4,307</td><td>4,519</td><td>5%</td><td>7,504</td><td>7,658</td><td>2%</td></tr><tr><td>Diluted Shares</td><td>5,122</td><td>5,122</td><td>0%</td><td>5,160</td><td>5,159</td><td>0%</td></tr><tr><td>Proforma EPS No options</td><td>$1.12</td><td>$1.17</td><td>4%</td><td>$1.74</td><td>$1.77</td><td>2%</td></tr><tr><td>% Change Y/Y</td><td>169.9%</td><td>179.8%</td><td></td><td>54.7%</td><td>51.8%</td><td></td></tr><tr><td>% Change Q/Q</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: Citi. Note: EPS estimates exclude SBC.

# AMD

We are raising our price target on AMD from \$358 to \$460. We value AMD using SOTP analysis with data center GPU/CPU biz at \$176/\$198 (30/30x 2028 PE), client \$26 (15x), gaming \$2 (8x), embedded \$24 (18x), and net cash per share \~\$33.

We believe AMD has won Anthropic as a customer for MI450 AI accelerator and we expect AMD to announce Anthropic as a customer at its Advancing AI day in July. We model AMD AI sales of \$15.1 billion in 2026 (up 127% YoY) and \$31.8 billion in 2027 (up 111% YoY).

Figure 7. Lowering C27 EPS by 2%, Raising C28 EPS by 4% 

<table><tr><td>AMD</td><td>Old</td><td>New</td><td></td><td>Old</td><td>New</td><td></td></tr><tr><td>FY end: December</td><td>2027E</td><td>2027E</td><td>Delta</td><td>2028E</td><td>2028E</td><td>Delta</td></tr><tr><td>Total Revenue</td><td>78,000.0</td><td>78,000.0</td><td>0%</td><td>91,000.0</td><td>97,500.0</td><td>7%</td></tr><tr><td>% Change Y/Y</td><td>49.8%</td><td>49.8%</td><td></td><td>16.7%</td><td>25.0%</td><td></td></tr><tr><td>% Change Q/Q</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3-year Seasonality</td><td>32.8%</td><td>32.8%</td><td></td><td>44.8%</td><td>44.8%</td><td></td></tr><tr><td>5-year Seasonality</td><td>27.6%</td><td>27.6%</td><td></td><td>28.8%</td><td>28.8%</td><td></td></tr><tr><td>Cost of Sales</td><td>35,445.0</td><td>35,445.0</td><td>0.0</td><td>40,480.0</td><td>43,365.0</td><td>0.1</td></tr><tr><td>% Change Y/Y</td><td>50.3%</td><td>50.3%</td><td>0.0%</td><td>14.2%</td><td>22.3%</td><td>57.3%</td></tr><tr><td>% Change Q/Q</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Gross Margins</td><td>54.6%</td><td>54.6%</td><td>0 bps</td><td>55.5%</td><td>55.5%</td><td>1 bps</td></tr><tr><td>SG&amp;A</td><td>5,570.0</td><td>5,570.0</td><td>0.0%</td><td>6,370.0</td><td>6,825.0</td><td>7.1%</td></tr><tr><td>% Total Revenue</td><td>7.1%</td><td>7.1%</td><td>0.0%</td><td>7.0%</td><td>7.0%</td><td>0.0%</td></tr><tr><td>R&amp;D</td><td>12,825.0</td><td>12,825.0</td><td>0.0%</td><td>15,910.0</td><td>17,040.0</td><td>7.1%</td></tr><tr><td>% Total Revenue</td><td>16.4%</td><td>16.4%</td><td>0.0%</td><td>17.5%</td><td>17.5%</td><td>0.0%</td></tr><tr><td>Operating Income</td><td>24160.0</td><td>24160.0</td><td>0.0%</td><td>28240.0</td><td>30270.0</td><td>7.2%</td></tr><tr><td>% Total Revenue</td><td>31.0%</td><td>31.0%</td><td>0%</td><td>31.0%</td><td>31.0%</td><td>0%</td></tr><tr><td>Tax Rate</td><td>13.0%</td><td>13.0%</td><td>0 bps</td><td>13.0%</td><td>13.0%</td><td>0 bps</td></tr><tr><td>Net Income</td><td>21,228.0</td><td>21,228.0</td><td>0%</td><td>24,777.6</td><td>26,543.7</td><td>7%</td></tr><tr><td>% Total Revenue</td><td>27.2%</td><td>27.2%</td><td>0 bps</td><td>27.2%</td><td>27.2%</td><td>0 bps</td></tr><tr><td>Diluted Shares</td><td>1,700.0</td><td>1,730.0</td><td>2%</td><td>1,700.0</td><td>1,755.0</td><td>3%</td></tr><tr><td>Proforma EPS - ex-options</td><td>$14.67</td><td>$14.41</td><td>-2%</td><td>$17.12</td><td>$17.76</td><td>4%</td></tr><tr><td>% Change Y/Y</td><td>77.5%</td><td>74.4%</td><td></td><td>16.7%</td><td>23.3%</td><td></td></tr><tr><td>% Change Q/Q</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: Citi

# Bull/Bear: Advanced Micro Devices (AMD.O)

![](images/f5a99a2ad0501bb8f46f0659c0786391f965e9dfc0bd14c2851570e2b5b1c0a3.jpg)

<details>
<summary>line</summary>

| Date       | Price     |
| ---------- | --------- |
| 15 May 26  | US$424.10 |
| May 27     | US$500.00 |
| May 27     | US$460.00 |
| May 27     | US$250.00 |
</details>

Spread 59pp   
Current Price and expected returns (upside/downside) as of 15 May 2026

# BULL Assumptions

![](images/e0a785f2cbbf9b2478f964ec859f01b88a56cc4dba425d0effa0f50eda74d8ee.jpg)

• Stronger than expected AI GPU ramp   
• Better than expected AI GPU margins

![](images/1c86afe5de885185d62c7d874c42448092ad75ce499e551194f3feab00fd0056.jpg)

# BASE Assumptions

\- SOTP analysis

[中间内容因长度限制已省略]

ar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective

investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
