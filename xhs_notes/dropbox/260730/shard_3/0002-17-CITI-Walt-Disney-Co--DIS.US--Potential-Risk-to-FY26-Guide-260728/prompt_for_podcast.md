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
# Walt Disney Co (DIS.N)

Potential Risk to FY26 Guide

## CITI'S TAKE

During F3Q26 earnings, we expect investors to focus on five items: 1) Potential changes to the firm's double-digital Adj EPS growth for FY26, 2) Domestic Experiences attendance trends, 3) Potential long-term Experiences EBIT targets to align with recent capex investments, 5) Potentially higher SVOD content spending causing more muted margin expansion and 6) EBIT headwinds from recent box office disappointments (including Mandalorian and Moana).

We See Some Risk to FY26 Guidance — We expect Disney to report 3Q26 segment EBIT of \$5.23 billion, just below guidance of \$5.3 billion. For 4Q26, we expect \$5.13 billion of EBIT and Adj. EPS of \$1.74, slightly below VA consensus estimates of \$1.76. Collectively, we expect \$6.80 of 2026 Adj EPS, or 15% yoy growth, slightly below guidance of 16% growth (which includes the 53 $^{rd}$ week).

F3Q26 Attendance Healthy, but 4Q26 Risks Emerge — Recently, Disney's US attendance growth has been muted. 3P data suggests a sequential improvement in 3Q26 trends, but risk remains to 4Q26 consensus of $6\%$ attendance growth (given recent commentary from Comcast).

Global Guest Growth — Management may shift from a Domestic to Global guest metric in FY27. This new metric would include International guests and Cruise nights. We believe this KPI will help growth, but improvements may be modest.

Experiences EBIT: Biggest Opportunity — In light of higher Experience capex, we see the opportunity for Disney is to provide long-term EBIT targets at Experiences. However, absent new targets, we remain confident that management's investments will generate robust returns based on analysis of past capex and EBIT trends.

SVOD: A Potential Risk — We will be listening for commentary related to higher SVOD content spending (to help lower churn and improve engagement). Given our expectation of higher content spend, our SVOD EBIT margins are below consensus in both FY27 and FY28.

Box Office Disappointments — While Toy Story outperformed, Mandalorian and Moana underperformed. We expect this to weigh on EBIT.

<table><tr><td>EPS (US$)</td><td>Q1</td><td>Q2</td><td>Q3</td><td>Q4</td><td>FY</td><td>FC Cons</td><td>VA Cons</td></tr><tr><td>2025A</td><td>1.76A</td><td>1.46A</td><td>1.60A</td><td>1.11A</td><td>5.93A</td><td>5.93A</td><td>5.93A</td></tr><tr><td>2026E</td><td>1.63A</td><td>1.57A</td><td>1.82E</td><td>1.74E</td><td>6.80E</td><td>6.82E</td><td>6.77E</td></tr><tr><td>Previous</td><td>1.63A</td><td>1.57A</td><td>1.85E</td><td>1.78E</td><td>6.86E</td><td>na</td><td>na</td></tr><tr><td>2027E</td><td>1.76E</td><td>2.06E</td><td>1.87E</td><td>1.62E</td><td>7.31E</td><td>7.47E</td><td>7.44E</td></tr><tr><td>Previous</td><td>1.77E</td><td>2.10E</td><td>1.94E</td><td>1.67E</td><td>7.49E</td><td>na</td><td>na</td></tr><tr><td>2028E</td><td>1.98E</td><td>2.00E</td><td>2.09E</td><td>1.75E</td><td>7.82E</td><td>8.26E</td><td>8.32E</td></tr><tr><td>Previous</td><td>2.01E</td><td>2.05E</td><td>2.16E</td><td>1.84E</td><td>8.06E</td><td>na</td><td>na</td></tr></table>

Click here for Visible Alpha consensus data

## Buy

Price (28 Jul 26 16:00) US\$98.91

Target price US\$135.00↓

from US\$145.00

Expected share price return 36.5%

Expected dividend yield 1.5%

Expected total return 38.0%

Market Cap US\$171,758M

## Price Performance (RIC: DIS.N, BB: DIS US)

![](images/d95f64765e61ed135395bd2e1c34830914369e1c0e1e0b2fe28ce43224a8778b.jpg)

Jason B Bazinet $^{AC}$ +1-212-816-6395
jason.bazinet@citi.com

Michael Lehman
+1-212-816-9300
michael.lehman@citi.com

Aarushi Gupta

+1-212-816-1136

aarushi.gupta@citi.com

Price: US\$98.91; TP: US\$135.00; Market Cap: US\$171,758m; Recomm: Buy

<table><tr><td>Profit &amp; Loss (US$m)</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Sales revenue</td><td>91,361</td><td>94,425</td><td>100,910</td><td>106,618</td><td>110,954</td></tr><tr><td>Cost of sales</td><td>-79,447</td><td>-80,593</td><td>-84,430</td><td>-88,752</td><td>-91,564</td></tr><tr><td>Gross profit</td><td>11,914</td><td>13,832</td><td>16,480</td><td>17,866</td><td>19,390</td></tr><tr><td>Gross Margin (%)</td><td>13.0</td><td>14.6</td><td>16.3</td><td>16.8</td><td>17.5</td></tr><tr><td>EBITDA (Adj)</td><td>20,522</td><td>22,594</td><td>25,040</td><td>26,107</td><td>27,932</td></tr><tr><td>EBITDA Margin (Adj) (%)</td><td>22.5</td><td>23.9</td><td>24.8</td><td>24.5</td><td>25.2</td></tr><tr><td>Depreciation</td><td>-4,990</td><td>-5,326</td><td>-5,470</td><td>-5,562</td><td>-5,483</td></tr><tr><td>Amortisation</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>EBIT (Adj)</td><td>14,166</td><td>15,905</td><td>18,233</td><td>19,245</td><td>21,149</td></tr><tr><td>EBIT Margin (Adj) (%)</td><td>15.5</td><td>16.8</td><td>18.1</td><td>18.1</td><td>19.1</td></tr><tr><td>Net interest</td><td>-1,260</td><td>-1,305</td><td>-1,176</td><td>-1,221</td><td>-1,110</td></tr><tr><td>Associates</td><td>575</td><td>295</td><td>334</td><td>201</td><td>323</td></tr><tr><td>Non-Op/Except/Other Adj</td><td>-5,912</td><td>-2,892</td><td>-1,992</td><td>-1,379</td><td>-1,759</td></tr><tr><td>Pre-tax profit</td><td>7,569</td><td>12,003</td><td>15,399</td><td>16,846</td><td>18,603</td></tr><tr><td>Tax</td><td>-1,796</td><td>1,428</td><td>-4,071</td><td>-4,043</td><td>-4,465</td></tr><tr><td>Extraord./Min.Int./Pref.div.</td><td>-801</td><td>-1,027</td><td>-936</td><td>-984</td><td>-1,085</td></tr><tr><td>Reported net profit</td><td>4,972</td><td>12,404</td><td>10,393</td><td>11,819</td><td>13,054</td></tr><tr><td>Net Margin (%)</td><td>5.4</td><td>13.1</td><td>10.3</td><td>11.1</td><td>11.8</td></tr><tr><td>Core NPAT</td><td>9,100</td><td>10,739</td><td>11,964</td><td>13,035</td><td>14,023</td></tr></table>

<table><tr><td>Valuation ratios</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>PE (x)</td><td>19.9</td><td>16.7</td><td>14.6</td><td>13.5</td><td>12.7</td></tr><tr><td>PB (x)</td><td>1.8</td><td>1.6</td><td>1.6</td><td>1.5</td><td>1.4</td></tr><tr><td>EV/EBITDA (x)</td><td>10.2</td><td>9.2</td><td>8.2</td><td>7.9</td><td>7.3</td></tr><tr><td>FCF yield (%)</td><td>4.7</td><td>5.6</td><td>5.8</td><td>6.7</td><td>4.9</td></tr><tr><td>Dividend yield (%)</td><td>0.8</td><td>1.0</td><td>1.5</td><td>1.6</td><td>1.7</td></tr><tr><td>Payout ratio (%)</td><td>15</td><td>17</td><td>22</td><td>22</td><td>22</td></tr><tr><td>ROE (%)</td><td>5.0</td><td>11.8</td><td>9.4</td><td>10.3</td><td>10.7</td></tr></table>

<table><tr><td>Cashflow (US$m)</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>EBITDA</td><td>16,839</td><td>19,158</td><td>21,950</td><td>23,428</td><td>24,873</td></tr><tr><td>Working capital</td><td>-1,613</td><td>-430</td><td>-1,811</td><td>1,455</td><td>-274</td></tr><tr><td>Other</td><td>-1,255</td><td>-627</td><td>-1,071</td><td>-3,766</td><td>-6,361</td></tr><tr><td>Operating cashflow</td><td>13,971</td><td>18,101</td><td>19,069</td><td>21,116</td><td>18,238</td></tr><tr><td>Capex</td><td>-5,412</td><td>-8,024</td><td>-9,003</td><td>-9,349</td><td>-9,617</td></tr><tr><td>Net acq/disposals</td><td>-1,401</td><td>-94</td><td>-540</td><td>0</td><td>0</td></tr><tr><td>Other</td><td>-68</td><td>75</td><td>57</td><td>0</td><td>0</td></tr><tr><td>Investing cashflow</td><td>-6,881</td><td>-8,043</td><td>-9,486</td><td>-9,349</td><td>-9,617</td></tr><tr><td>Dividends paid</td><td>-1,366</td><td>-1,803</td><td>-2,647</td><td>-2,851</td><td>-3,071</td></tr><tr><td>Financing cashflow</td><td>-6,678</td><td>-9,927</td><td>-7,366</td><td>-9,457</td><td>-9,249</td></tr><tr><td>Net change in cash</td><td>477</td><td>136</td><td>2,188</td><td>2,310</td><td>-628</td></tr><tr><td>Free cashflow to s/holders</td><td>8,559</td><td>10,077</td><td>10,065</td><td>11,767</td><td>8,622</td></tr></table>

<table><tr><td>Per share data</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Reported EPS ($)</td><td>2.72</td><td>6.85</td><td>5.90</td><td>6.62</td><td>7.28</td></tr><tr><td>Core EPS ($)</td><td>4.97</td><td>5.93</td><td>6.80</td><td>7.31</td><td>7.82</td></tr><tr><td>DPS ($)</td><td>0.75</td><td>1.00</td><td>1.51</td><td>1.60</td><td>1.72</td></tr><tr><td>CFPS ($)</td><td>7.63</td><td>10.00</td><td>10.83</td><td>11.84</td><td>10.17</td></tr><tr><td>FCFPS ($)</td><td>4.67</td><td>5.56</td><td>5.72</td><td>6.60</td><td>4.81</td></tr><tr><td>BVPS ($)</td><td>55.57</td><td>61.35</td><td>62.08</td><td>65.22</td><td>69.20</td></tr><tr><td>Wtd avg ord shares (m)</td><td>1,825</td><td>1,804</td><td>1,755</td><td>1,778</td><td>1,788</td></tr><tr><td>Wtd avg diluted shares (m)</td><td>1,831</td><td>1,811</td><td>1,761</td><td>1,784</td><td>1,794</td></tr></table>

<table><tr><td>Growth rates</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Sales revenue (%)</td><td>2.8</td><td>3.4</td><td>6.9</td><td>5.7</td><td>4.1</td></tr><tr><td>EBIT (Adj) (%)</td><td>20.9</td><td>12.3</td><td>14.6</td><td>5.5</td><td>9.9</td></tr><tr><td>Core NPAT (%)</td><td>32.3</td><td>18.0</td><td>11.4</td><td>9.0</td><td>7.6</td></tr><tr><td>Core EPS (%)</td><td>32.2</td><td>19.3</td><td>14.6</td><td>7.5</td><td>7.0</td></tr></table>

<table><tr><td>Balance Sheet (US$m)</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Cash &amp; cash equiv.</td><td>6,002</td><td>5,695</td><td>7,880</td><td>10,190</td><td>9,563</td></tr><tr><td>Accounts receivables</td><td>12,729</td><td>13,217</td><td>13,148</td><td>14,183</td><td>14,826</td></tr><tr><td>Inventory</td><td>2,022</td><td>2,134</td><td>2,212</td><td>2,293</td><td>2,378</td></tr><tr><td>Net fixed &amp; other tangibles</td><td>82,454</td><td>82,584</td><td>89,716</td><td>94,980</td><td>102,999</td></tr><tr><td>Goodwill &amp; intangibles</td><td>84,065</td><td>82,566</td><td>84,010</td><td>82,542</td><td>81,074</td></tr><tr><td>Financial &amp; other assets</td><td>8,947</td><td>11,318</td><td>10,733</td><td>10,771</td><td>10,818</td></tr><tr><td>Total assets</td><td>196,219</td><td>197,514</td><td>207,699</td><td>214,959</td><td>221,657</td></tr><tr><td>Accounts payable</td><td>21,070</td><td>21,203</td><td>20,668</td><td>23,282</td><td>23,791</td></tr><tr><td>Short-term debt</td><td>6,845</td><td>6,711</td><td>8,887</td><td>8,887</td><td>8,887</td></tr><tr><td>Long-term debt</td><td>38,970</td><td>35,315</td><td>37,271</td><td>35,871</td><td>34,471</td></tr><tr><td>Provisions &amp; other liab</td><td>23,812</td><td>19,673</td><td>22,586</td><td>22,586</td><td>22,586</td></tr><tr><td>Total liabilities</td><td>90,697</td><td>82,902</td><td>89,412</td><td>90,626</td><td>89,735</td></tr><tr><td>Shareholders&#x27; equity</td><td>100,696</td><td>109,869</td><td>111,683</td><td>117,729</td><td>125,318</td></tr><tr><td>Minority interests</td><td>4,826</td><td>4,743</td><td>6,604</td><td>6,604</td><td>6,604</td></tr><tr><td>Total equity</td><td>105,522</td><td>114,612</td><td>118,287</td><td>124,333</td><td>131,922</td></tr><tr><td>Net debt (Adj)</td><td>39,813</td><td>36,331</td><td>38,278</td><td>34,568</td><td>33,795</td></tr><tr><td>Net debt to equity (Adj) (%)</td><td>37.7</td><td>31.7</td><td>32.4</td><td>27.8</td><td>25.6</td></tr></table>

For definitions of the items in this table, please click here.

# Preparing for F3Q26 Results

During earnings, we suspect investors will focus on six areas:

■ First, investors continue to fear a reduction in FY26 guidance. Unlike last quarter, we think there is some risk to the FY26 guide (see Figure 1).

■ Second, the buy side (based on our conversations with investors) remains focused on domestic attendance trends. These fears increased when Comcast noted that higher gas prices and dour consumer sentiment weighed on Epic's performance in June. Our 3P data suggests Street estimates for F3Q26 are reasonable at 1%. However, we see risks to the 4Q26 estimate of 6% growth, even with an easier comp of -4% (see Figure 8).

■ Third, management hinted they may sunset Domestic attendance growth and shift to a broader global metric (which includes International parks and Cruise nights). We looked at historical trends for global attendance and do not expect a demonstrably better growth rate from this potentially new KPI (see Figure 10).

\- Fourth, investors want to understand how higher Experiences capex may translate into long-term EBIT growth. A long-term target may be the greatest opportunity for multiple expansion. However, if we don't get a long-term Experiences EBIT target, we continue to view incremental capex as a positive. Management has a long track record of disciplined investments with favorable ROICs (see Figure 18).

■ Fifth, strategically, investors wonder if SVOD needs more content spending to improve engagement. We think it does. As such, we are lowering our estimates on higher SVOD content spending. Our SVOD margins are below the Street by 130bps in 2027 and 200bps in 2028 (see Figure 22).

■ Sixth, recent box office disappointments from The Mandalorian in F3Q26 and Moana in F4Q26 will likely weigh on near-term estimates (see Figure 24).

## #1: FY26 Guidance

For full-year 2026, investor's ‘north star’ is double digit Adj EPS growth. The company guided to 16% growth including the $53^{\text{rd}}$ week. We believe there is some risk to this estimate driven by the Entertainment segment.

Figure 1. FY26 Estimates (\$ millions, percent, \$ per share)

<table><tr><td></td><td>CitiFY26E</td><td>VAConsensusFY26E</td><td>Citi vsConsensusFY26E</td><td>2025A</td><td>CitiYoY growthinc. 53rd week</td><td>ConsensusYoY growthinc. 53rd week</td><td>Guidancefor FY26(ex 53rd week)</td></tr><tr><td>Entertainment Revenue</td><td>45,966</td><td>46,705</td><td>-1.6%</td><td>42,466</td><td>8.2%</td><td>10.0%</td><td></td></tr><tr><td>+ Sports Revenue</td><td>18,403</td><td>18,446</td><td>-0.2%</td><td>17,672</td><td>4.1%</td><td>4.4%</td><td></td></tr><tr><td>+ Experiences Revenue</td><td>38,926</td><td>39,125</td><td>-0.5%</td><td>36,156</td><td>7.7%</td><td>8.2%</td><td></td></tr><tr><td>+ Eliminations</td><td>(2,386)</td><td>(2,137)</td><td>11.7%</td><td>(1,869)</td><td>27.7%</td><td>14.3%</td><td></td></tr><tr><td>= FY26 Revenue</td><td>100,910</td><td>101,892</td><td>-1.0%</td><td>94,425</td><td>6.9%</td><td>7.9%</td><td></td></tr><tr><td>Entertainment EBIT</td><td>5,247</td><td>5,396</td><td>-2.8%</td><td>4,674</td><td>12.3%</td><td>15.5%</td><td>Double digits</td></tr><tr><td>+ Sports EBIT</td><td>3,071</td><td>3,055</td><td>0.5%</td><td>2,882</td><td>6.6%</td><td>6.0%</td><td>Mid single digits</td></tr><tr><td>+ Experiences EBIT</td><td>11,249</td><td>11,014</td><td>2.1%</td><td>9,995</td><td>12.5%</td><td>10.2%</td><td>High single digits</td></tr><tr><td>= FY26 Segment Operating Income</td><td>19,567</td><td>19,465</td><td>0.5%</td><td>17,551</td><td>11.5%</td><td>10.9%</td><td></td></tr><tr><td>Operating Income Margin</td><td>19.4%</td><td>19.1%</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SVOD EBIT margin</td><td>10.8%</td><td>10.8%</td><td>0.0%</td><td>6.6%</td><td></td><td></td><td>At least 10% margin</td></tr><tr><td>FY26 Adj. EPS</td><td>6.80</td><td>6.82</td><td>-0.3%</td><td>5.93</td><td>14.6%</td><td>14.9%</td><td>16% inc. 53rd week12% ex. 53rd week</td></tr><tr><td>FY26 Cash from operations</td><td>19,069</td><td>19,174</td><td>-0.5%</td><td>18,101</td><td>5.3%</td><td>5.9%</td><td>$19 billion</td></tr><tr><td>FY26 Share repurchases</td><td>8,194</td><td>8,245</td><td>-0.6%</td><td>3,500</td><td>134.1%</td><td>135.6%</td><td>At least $8 billion</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.

```txt
Source: Citi, Company Reports, Visible Alpha
```

Investors' anxiety about the FY26 Adj EPS guide likely stems from the robust EBIT growth needed in 4Q (given 3Q26 guidance for \$5.3 billion of EBIT). We are less nervous about the implied 4Q26 growth given the easy compare in the year-ago period.

Figure 2. Segment EBIT Growth (\$ millions; percent)

<table><tr><td rowspan="2"></td><td colspan="4">2025</td><td colspan="4">2026</td><td></td></tr><tr><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>1Q</td><td>2Q</td><td>3QE</td><td>4QE</td><td>Total</td></tr><tr><td>Current year segment EBIT</td><td>5,060</td><td>4,436</td><td>4,575</td><td>3,480</td><td>4,600</td><td>4,603</td><td>5,235</td><td>5,129</td><td>19,567</td></tr><tr><td>- Year ago segment EBIT</td><td>3,876</td><td>3,845</td><td>4,225</td><td>3,655</td><td>5,060</td><td>4,436</td><td>4,575</td><td>3,480</td><td>17,551</td></tr><tr><td>= YoY change in segment EBIT</td><td>1,184</td><td>591</td><td>350</td><td>(175)</td><td>(460)</td><td>167</td><td>660</td><td>1,649</td><td>2,016</td></tr><tr><td>memo: growth</td><td>31%</td><td>15%</td><td>8%</td><td>-5%</td><td>-9%</td><td>4%</td><td>14%</td><td>47%</td><td></td></tr><tr><td>memo: 2-year stacked growth</td><td>58%</td><td>32%</td><td>27%</td><td>18%</td><td>21%</td><td>19%</td><td>23%</td><td>43%</td><td></td></tr></table>

For 3Q26, we forecast EBIT of \$5.2 billion, which falls just below the guide of \$5.3 billion.

Figure 3. F3Q26 Expectations (\$ millions; percent; \$ per share)

<table><tr><td></td><td>CitiF3Q26E</td><td>VAConsensusF3Q26E</td><td>Citi vsConsensusF3Q26E</td><td>3Q25A</td><td>CitiYoY growth</td><td>ConsensusYoY growth</td><td>GuidanceF3Q26E</td></tr><tr><td>SVOD</td><td>610</td><td>628</td><td>-2.8%</td><td>329</td><td>85.5%</td><td>90.9%</td><td></td></tr><tr><td>+ Other</td><td>778</td><td>923</td><td>-15.7%</td><td>693</td><td>12.3%</td><td>33.2%</td><td></td></tr><tr><td>= Entertainment EBIT</td><td>1,388</td><td>1,551</td><td>-10.5%</td><td>1,022</td><td>35.8%</td><td>51.8%</td><td></td></tr><tr><td>+ Sports EBIT</td><td>893</td><td>898</td><td>-0.7%</td><td>1,037</td><td>-13.9%</td><td>-13.4%</td><td>14% decline</td></tr><tr><td>+ Experiences EBIT</td><td>2,954</td><td>2,779</td><td>6.3%</td><td>2,516</td><td>17.4%</td><td>10.5%</td><td></td></tr><tr><td>= Segment Operating Income</td><td>5,235</td><td>5,229</td><td>0.1%</td><td>4,575</td><td>14.4%</td><td>14.3%</td><td>$5.3 billion</td></tr><tr><td>Adj. EPS</td><td>1.82</td><td>1.85</td><td>-1.2%</td><td>1.60</td><td>14.3%</td><td>15.7%</td><td></td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, Visible Alpha, Company Reports

## 4Q26 Expectations

Regarding 4Q26, we are above the Street for segment EBIT and expect 47% EBIT growth driven largely by Experiences and Entertainment.

Figure 4. F4Q26 Expectations 

[中间内容因长度限制已省略]

lar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
