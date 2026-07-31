你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
# US Semiconductors

## SWKS & QRVO – Maintain Neutral

## CITI'S TAKE

We update SWKS and QRVO models post Jun-Q results. SWKS reported Jun-Q above Street consensus, and guided Sep-Q rev/EPS +1%/-2% compared to Street on slightly higher interest expense due to financing costs related to QRVO transaction. SWKS expects Sep-Q mobile rev to grow high-teens Q/Q driven by largest customer ramp, partially offset by Android. We adjust SWKS CY26/27 EPS estimates by -2%/-3% on lower GM and higher interest expense. QRVO Jun-Q results came above Street and expects FY27 GM to be above 50% and EPS above \$7.00. We adjust QRVO CY26/27 EPS estimates by +10%/+2%. SWKS now expects the QRVO transaction to be closed within CY26 and could be as early as by Sep-Q end. We lower SWKS TP to \$64, and QRVO TP to \$95 on consistent 12x P/E applied to CY27 EPS, vs prior 14x/13x multiples respectively to reflect lower market multiples. Maintain Neutral on SWKS and QRVO.

Atif Malik $^{AC}$ +1-415-951-1892
atif.malik@citi.com

Elizabeth Sun, CFA
+1-212-816-3308
elizabeth.sun@citi.com

<table><tr><td rowspan="2" colspan="14"></td><td colspan="2">Current Fiscal Year</td><td colspan="2">Next Fiscal Year</td></tr><tr><td rowspan="2" colspan="2">EPS</td><td rowspan="2" colspan="2">EPS</td></tr><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Ccy</td><td rowspan="2">Price</td><td rowspan="2">Mkt Cap (M)</td><td rowspan="2">Date &amp; Time</td><td colspan="2">Rating</td><td rowspan="2">Short-Term View</td><td colspan="2">Target Price</td><td colspan="3"></td></tr><tr><td>Old</td><td>New</td><td>Old</td><td>New</td><td>ESPR (%)</td><td>Div Yld (%)</td><td>ETR (%)</td><td>Last Rpt Yr</td><td>Old</td><td>New</td><td>Old</td></tr><tr><td>Qorvo</td><td>QRVO</td><td>US$</td><td>87.67</td><td>7,734</td><td>28 Jul 22:00</td><td>2</td><td>nc</td><td>-</td><td>100.00</td><td>95.00</td><td>8.4</td><td>0.0</td><td>8.4</td><td>Mar-26</td><td>6.89</td><td>7.64</td><td>7.77</td></tr><tr><td>Skyworks Solutions</td><td>SWKS</td><td>US$</td><td>57.96</td><td>8,721</td><td>28 Jul 22:00</td><td>2</td><td>nc</td><td>-</td><td>77.00</td><td>64.00</td><td>10.4</td><td>0.0</td><td>10.4</td><td>Sep-25</td><td>5.02</td><td>5.04</td><td>5.24</td></tr><tr><td colspan="6">1 = Buy, 2 = Neutral, 3 = Sell, H = High RiskSource: Citi</td><td colspan="12">ESPR = Expected Share Price Return, ETR = Expected Total Return, nc = no change^Catalyst Watch</td></tr></table>

Earnings Estimates

<table><tr><td colspan="4"></td><td colspan="5">Last Reported Year</td><td colspan="5">Current Fiscal Year</td><td colspan="5">Next Fiscal Year</td></tr><tr><td>Company Name</td><td>Ticker</td><td>Last Rpt Year</td><td>Currency</td><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>FY0</td><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>FY1</td><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>FY2</td></tr><tr><td>Qorvo</td><td>QRVO</td><td>Mar-26</td><td>US$</td><td>0.92</td><td>2.22</td><td>2.17</td><td>1.69</td><td>7.01</td><td>1.64</td><td>2.01</td><td>2.01</td><td>1.98</td><td>7.64</td><td>1.88</td><td>2.17</td><td>1.93</td><td>1.93</td><td>7.91</td></tr><tr><td>Old</td><td></td><td>Mar-26</td><td>US$</td><td>0.92</td><td>2.22</td><td>2.17</td><td>1.69</td><td>7.01</td><td>1.03</td><td>1.99</td><td>1.97</td><td>1.92</td><td>6.89</td><td>1.56</td><td>2.32</td><td>2.02</td><td>1.87</td><td>7.77</td></tr><tr><td>Skyworks Solutions</td><td>SWKS</td><td>Sep-25</td><td>US$</td><td>1.60</td><td>1.24</td><td>1.33</td><td>1.76</td><td>5.93</td><td>1.54</td><td>1.15</td><td>1.08</td><td>1.27</td><td>5.04</td><td>1.40</td><td>1.13</td><td>1.09</td><td>1.37</td><td>4.99</td></tr><tr><td>Old</td><td></td><td>Sep-25</td><td>US$</td><td>1.60</td><td>1.24</td><td>1.33</td><td>1.76</td><td>5.93</td><td>1.54</td><td>1.15</td><td>1.03</td><td>1.29</td><td>5.02</td><td>1.51</td><td>1.18</td><td>1.14</td><td>1.40</td><td>5.24</td></tr><tr><td colspan="19">Source: Citi</td></tr></table>

# SWKS/QRVO Jun-Q Review

Figure 1. SWKS CY P&L Changes

<table><tr><td colspan="9">Key Financial Data -- Income Statement</td></tr><tr><td></td><td rowspan="2">CY22Dec-22</td><td rowspan="2">CY23Dec-23</td><td rowspan="2">ActCY24Dec-24</td><td rowspan="2">ActCY25Dec-25</td><td rowspan="2">OldCY26EDec-26</td><td rowspan="2">NewCY26EDec-26</td><td rowspan="2">OldCY27EDec-27</td><td rowspan="2">NewCY27EDec-27</td></tr><tr><td>($M), except per share</td></tr><tr><td>Revenue ($M)</td><td>5,305</td><td>4,645</td><td>4,045</td><td>4,054</td><td>3,985</td><td>3,996</td><td>4,264</td><td>4,281</td></tr><tr><td>YY</td><td>3.8%</td><td>-12.4%</td><td>-12.9%</td><td>0.2%</td><td>-1.7%</td><td>-1.4%</td><td>7.0%</td><td>7.1%</td></tr><tr><td>Gross Margin - GAAP</td><td>47.6%</td><td>42.6%</td><td>40.9%</td><td>41.1%</td><td>41.5%</td><td>40.4%</td><td>42.6%</td><td>41.2%</td></tr><tr><td>Gross Margin - Non-GAAP</td><td>51.3%</td><td>47.7%</td><td>46.0%</td><td>46.9%</td><td>45.4%</td><td>44.8%</td><td>46.3%</td><td>45.4%</td></tr><tr><td>RD Non-GAAP % sales</td><td>11.9%</td><td>12.8%</td><td>16.2%</td><td>20.0%</td><td>21.2%</td><td>21.3%</td><td>20.4%</td><td>20.5%</td></tr><tr><td>SG&amp;A Non-GAAP % sales</td><td>6.3%</td><td>6.6%</td><td>7.5%</td><td>9.8%</td><td>11.8%</td><td>10.5%</td><td>11.1%</td><td>9.4%</td></tr><tr><td>OpExNon-GAAP % Sales</td><td>14.5%</td><td>15.9%</td><td>19.9%</td><td>22.5%</td><td>24.0%</td><td>23.9%</td><td>23.0%</td><td>22.8%</td></tr><tr><td>R&amp;D inc-SBC</td><td>631</td><td>596</td><td>655</td><td>812</td><td>846</td><td>852</td><td>870</td><td>879</td></tr><tr><td>SG&amp;A inc-SBC</td><td>332</td><td>308</td><td>305</td><td>397</td><td>472</td><td>418</td><td>475</td><td>403</td></tr><tr><td>OpEx (GAAP)</td><td>1,079</td><td>960</td><td>1,096</td><td>1,245</td><td>1,351</td><td>1,336</td><td>1,376</td><td>1,351</td></tr><tr><td>OpEx (non-GAAP)</td><td>769</td><td>741</td><td>804</td><td>913</td><td>957</td><td>955</td><td>979</td><td>976</td></tr><tr><td>Stock Compensation</td><td>194.2</td><td>188.9</td><td>178.0</td><td>209.2</td><td>215.0</td><td>184.8</td><td>223.1</td><td>181.5</td></tr><tr><td>Operating Margin Non-GAAP</td><td>36.8%</td><td>31.8%</td><td>26.1%</td><td>24.4%</td><td>21.4%</td><td>20.9%</td><td>23.3%</td><td>22.6%</td></tr><tr><td>Interest Income</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Interest Expense</td><td>(53.9)</td><td>(57.5)</td><td>(27.4)</td><td>(26.5)</td><td>(30.0)</td><td>(35.2)</td><td>(30.0)</td><td>(43.6)</td></tr><tr><td>Other Income</td><td>(3.1)</td><td>21.0</td><td>42.3</td><td>49.9</td><td>27.8</td><td>30.2</td><td>32.0</td><td>33.9</td></tr><tr><td>Pretax Income Non-GAAP</td><td>1895.2</td><td>1441.0</td><td>1070.4</td><td>986.1</td><td>852.3</td><td>828.9</td><td>996.5</td><td>956.8</td></tr><tr><td>Tax Non-GAAP</td><td>168.6</td><td>171.8</td><td>116.4</td><td>93.0</td><td>91.0</td><td>82.2</td><td>117.0</td><td>108.1</td></tr><tr><td>Tax Rate Non-GAAP</td><td>8.9%</td><td>11.9%</td><td>10.9%</td><td>9.4%</td><td>10.7%</td><td>9.9%</td><td>11.7%</td><td>11.3%</td></tr><tr><td>Share Count</td><td>161.8</td><td>160.4</td><td>161.4</td><td>152.4</td><td>152.4</td><td>152.2</td><td>160.1</td><td>159.4</td></tr><tr><td>EPS (ex-1, ex-SBC, ex-amort)</td><td>$10.67</td><td>$7.92</td><td>$5.91</td><td>$5.86</td><td>$4.99</td><td>$4.91</td><td>$5.50</td><td>$5.32</td></tr><tr><td>Y/Y</td><td>4%</td><td>-26%</td><td>-25%</td><td>-1%</td><td>-15%</td><td>-16%</td><td>10%</td><td>7%</td></tr><tr><td>Consensus Sales</td><td></td><td></td><td></td><td></td><td></td><td>3,940</td><td></td><td>4,090</td></tr><tr><td>Consensus EPS (inc-SBC, ex-amort)</td><td></td><td></td><td></td><td></td><td></td><td>$4.85</td><td></td><td>$5.41</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Note: Figures on CY basis

Source: Citi, FactSet

Figure 2. QRVO CY P&L Changes

<table><tr><td colspan="9">Key Financial Data -- Income Statement</td></tr><tr><td>($M), except per share</td><td>CY22Dec-22</td><td>CY23Dec-23</td><td>CY24Dec-24</td><td>CY25Dec-25</td><td>OldCY26EDec-26</td><td>NewCY26EDec-26</td><td>OldCY27EDec-27</td><td>NewCY27EDec-27</td></tr><tr><td>Revenue ($M)</td><td>4,103</td><td>3,461</td><td>3,790</td><td>3,740</td><td>3,371</td><td>3,474</td><td>3,702</td><td>3,738</td></tr><tr><td>YY</td><td>-9.9%</td><td>-15.6%</td><td>9.5%</td><td>-1.3%</td><td>-9.9%</td><td>-7.1%</td><td>9.8%</td><td>7.6%</td></tr><tr><td>Gross Margin - non-GAAP</td><td>48.7%</td><td>44.4%</td><td>44.4%</td><td>47.4%</td><td>50.7%</td><td>51.0%</td><td>50.2%</td><td>50.4%</td></tr><tr><td>RD % sales</td><td>15.7%</td><td>19.2%</td><td>19.7%</td><td>19.7%</td><td>20.6%</td><td>20.2%</td><td>19.2%</td><td>19.8%</td></tr><tr><td>SG&amp;A % sales</td><td>8.8%</td><td>10.9%</td><td>10.7%</td><td>10.4%</td><td>10.1%</td><td>10.4%</td><td>9.3%</td><td>10.2%</td></tr><tr><td>OpEx % Sales</td><td>22.0%</td><td>27.2%</td><td>27.6%</td><td>27.1%</td><td>28.3%</td><td>27.6%</td><td>26.2%</td><td>27.0%</td></tr><tr><td>R&amp;D</td><td>645</td><td>666</td><td>748</td><td>736</td><td>694</td><td>701</td><td>710</td><td>740</td></tr><tr><td>SG&amp;A</td><td>360</td><td>379</td><td>406</td><td>387</td><td>340</td><td>360</td><td>345</td><td>383</td></tr><tr><td>OpEx (GAAP)</td><td>1,110</td><td>1,349</td><td>1,454</td><td>1,252</td><td>1,470</td><td>1,295</td><td>1,492</td><td>1,289</td></tr><tr><td>OpEx (non-GAAP)</td><td>901</td><td>940</td><td>1,046</td><td>1,012</td><td>954</td><td>958</td><td>972</td><td>1,008</td></tr><tr><td>Stock Compensation</td><td>97.2</td><td>117.9</td><td>130.2</td><td>137.4</td><td>94.5</td><td>134.9</td><td>99.9</td><td>153.7</td></tr><tr><td>Operating Income non-GAAP</td><td>1,097.8</td><td>596.5</td><td>635.5</td><td>760.2</td><td>754.0</td><td>811.6</td><td>885.3</td><td>876.9</td></tr><tr><td>Operating Margin (non-GAAP)</td><td>26.8%</td><td>17.2%</td><td>16.8%</td><td>20.3%</td><td>22.4%</td><td>23.4%</td><td>23.9%</td><td>23.5%</td></tr><tr><td>Interest Income</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Interest Expense</td><td>(68.6)</td><td>(69.2)</td><td>(75.6)</td><td>(75.3)</td><td>(72.7)</td><td>(65.4)</td><td>(73.1)</td><td>(63.4)</td></tr><tr><td>Other Income</td><td>(3.0)</td><td>41.5</td><td>58.5</td><td>59.0</td><td>53.0</td><td>57.6</td><td>60.0</td><td>60.0</td></tr><tr><td>Pretax Income (non-GAAP)</td><td>1043.5</td><td>564.2</td><td>610.6</td><td>728.2</td><td>727.1</td><td>781.2</td><td>857.1</td><td>837.9</td></tr><tr><td>Tax (GAAP)</td><td>117.3</td><td>56.5</td><td>53.2</td><td>51.2</td><td>(32.6)</td><td>50.4</td><td>(5.8)</td><td>84.5</td></tr><tr><td>Tax Rate (non-GAAP)</td><td>111.9</td><td>63.5</td><td>58.9</td><td>96.9</td><td>110.0</td><td>119.5</td><td>136.9</td><td>129.1</td></tr><tr><td>Share Count</td><td>104.8</td><td>98.4</td><td>95.8</td><td>92.9</td><td>91.6</td><td>88.9</td><td>91.6</td><td>88.0</td></tr><tr><td>EPS (ex-1, ex-SBC, ex-amort)</td><td>$8.87</td><td>$5.06</td><td>$5.74</td><td>$6.73</td><td>$6.67</td><td>$7.34</td><td>$7.82</td><td>$7.97</td></tr><tr><td>Consensus Sales</td><td></td><td></td><td></td><td></td><td></td><td>3,388</td><td></td><td>3,586</td></tr><tr><td>Consensus EPS</td><td></td><td></td><td></td><td></td><td></td><td>$6.73</td><td></td><td>$7.72</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Note: Figures on CY basis

Source: Citi, FactSet

## Bull/Bear: Qorvo (QRVO.O)

![](images/375d0ce510b67848a1a8bed407ab5a29ba37a653faeebf2018612218a51301b0.jpg)  
Spread 68pp
Current Price and expected returns (upside/downside) as of 28 Jul 2026

## BULL Assumptions

![](images/9a9cc673f40bb841dfd7628854a34616abf5947f8a6b2901bd011262a743ae83.jpg)

• Stronger than expected 5G Units/\$ Content + share gains

\- Valuation = 17x

![](images/7e75838308f1a74b9c3c35e5c13d7dbc9c3021150913eae3621e6237eca62958.jpg)

\- Moderate 5G \$ content gains + stable share

\- Valuation = 12x

![](images/c3f3e936fe48427f1c90576c8c98e00ade8c3fbb44567ff8e2ce504b81b4f938.jpg)

\- Weaker than expected 5G Units/\$ Content

\- Share loss and gross margin deterioration

## Bull/Bear: Skyworks Solutions, Inc. (SWKS.O)

![](images/3eac48d10bfe5f58718bbb209ed2ec0af7613750afc5961305985a995ca75719.jpg)  
Spread 95pp
Current Price and expected returns (upside/downside) as of 28 Jul 2026

## BULL Assumptions

![](images/bf35ab043d2283a616577b283eff11fcde9ca261fcf65e4f302b3c5a9cb9720a.jpg)

\- 5G opportunity grows strongly in 2026 + share gains

• Low L/T Apple substitution risk

\- Valuation 19x

## BASE Assumptions

![](images/bc3fc19e0f64b7d253e736e1f32fe970d46ac94a61b986990310161268f96a7a.jpg)

• 5G opportunity grows modestly in 2026

• Moderate L/T Apple substitution risk

\- Valuation 12x

## BEAR Assumptions

![](images/ac0e5297976a3aecb8c3b7e74dec9b7a936f32d080542bbe934652570478b3d9.jpg)

\- 5G opportunity not material in 2026 + further Apple share loss

• High L/T Apple substitution risk

\- Valuation 9x

## Qorvo

## Company description

Qorvo, Inc. engages in the provision of core technologies and radio frequency solutions for mobile, infrastructure, and aerospace or defense applications. Its products include amplifiers, control products, discrete transistors and integrated circuits, filters and duplexers, frequency converters, integrated modules, optical components, oscillators, passives and switches. The company was founded on December 13, 2013 and is headquartered in Greensboro, NC.

## Investment strategy

We rate QRVO Neutral as the announced SWKS/QRVO merger deal could help with competition and concentration risk, while RF semis not being a major beneficiary of AI demand.

## Valuation

Our target price of \$95 is based on 12x P/E or below the three-year average of 14x times 2027E EPS to reflect market multiples contraction on smartphone market softness.

## Risks

Upside risks to our estimates and target price include: 1) better-than-expected global smartphone demand and 5G adoption particularly in China; 2) higher-than-expected share gains at major customers; and 3) higher gross margins on manufacturing synergies.

Downside risks to our estimates and target price include: 1) new product introduction delays or unexpected loss in \$ content at major OEMs; 2) faster-than-expected deceleration in global smartphone demand and 5G adoption; 3) increasing competition among four major RF makers and domestic China competitors; 4) lower gross margins and ASPs on aggressive capacity ramps at peers; 5) the announced SWKS/QRVO deal could not get regulatory approval.

## Skyworks Solutions, Inc.

## Company description

Skyworks Solutions is an innovator of high-performance analog semiconductors connecting people, places, and things. Skyworks Solutions designs, develops, manufactures, and markets proprietary semiconductor products. It supports automotive, broadband, cellular infrastructure, energy management, GPS, industrial, medical, military, wireless networking, smartphone, and tablet applications.

## Investment strategy

We rate SWKS Neutral as the announced SWKS/QRVO merger deal could help with competition and concentration risk, while RF semis not being a major beneficiary of AI demand.

## Valuation

Our target price of \$64 is based on \~12x P/E multiplied by CY27E EPS, which is lower than one-year average of 16x to reflect smartphone market multiple compression.

## Risks

Upside risks to achieving our estimates and target price include: 1) new product introduction or unexpected gain in \$ content at major OEMs; 2) faster-than-expected China recovery; and 3) faster ramp to target gross margins.

Downside risks to achieving our estimates and target price include: 1) deceleration in global smartphone demand and 5G adoption; 2) higher competition among four major RF makers and domestic China competitors; and 3) lower gross margins and ASPs; 4) the announced SWKS/QRVO deal could not get regulatory approval.

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

Qorvo (QRVO)
Ratings and Target Price History
Fundamental Research

Analyst: Atif Malik

![](images/92c74e4f8808d684c19232cbf6395ca7129a9b8c1c9f3a98cfbe868972d6a6fb.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>03-Aug-23 06:36:32</td><td>2</td><td>*116.00</td><td>105.84</td></tr><tr><td>2</td><td>10-Oct-23 05:00:00</td><td>*3</td><td>*78.00</td><td>93.26</td></tr><tr><td>3</td><td>02-Nov-23 08:42:00</td><td>3</td><td>*79.00</td><td>85.48</td></tr><tr><td>4</td><td>01-Feb-24 06:51:49</td><td>3</td><td>*84.00</td><td>105.75</td></tr><tr><td>5</td><td>01-May-24 22:47:02</td><td>3</td><td>*82.00</td><td>111.89</td></tr></table>

\*Indicates Change

<table><tr><td colspan="2">Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>6</td><td>31-Jul-24 03:12:47</td><td>3</td><td>*85.00</td><td>119.80</td></tr><tr><td>7</td><td>30-Oct-24 06:56:20</td><td>3</td><td>*72.00</td><td>73.04</td></tr><tr><td>8</td><td>29-Jan-25 02:43:56</td><td>3<

[中间内容因长度限制已省略]

lar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
