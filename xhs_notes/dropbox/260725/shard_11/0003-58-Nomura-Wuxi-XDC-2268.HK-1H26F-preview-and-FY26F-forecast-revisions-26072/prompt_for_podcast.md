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
EQUITY: HEALTH CARE & PHARMACEUTICALS

# 1H26F preview and FY26F forecast revisions

We expect stable, high top-line growth, despite some FX headwinds on earnings; reaffirm Buy

1H26F sales/earnings likely grew 41.2%/0.2% y-y

We forecast Wuxi XDC to report 1H26F revenue of CNY3.8bn (41.2% y-y), driven by the on-track high growth of existing business and consolidation of BioDlink (1875 HK, Not rated) since this April, which contributed CNY225mn.

On the margin front, we estimate a largely stable gross margin of $36.0\%$ in 1H26F (factoring in economies of scale that mitigated negative FX impact, and CNY appreciation against USD by $4\%$ in 1H26 vs 1H25), and a lower operating margin of $27.4\%$ (-1.1pp y-y) on higher G&A expenses related to the BioDlink acquisition. Along with a higher FX loss, we expect 1H26F net profit to shareholders at CNY747mn.

For 2H26F, we estimate Wuxi XDC tol book revenue/net profit of CNY4.3bn/CNY941mn (+32%/28% y-y), owing to contributions from commercial projects and further enhanced operational efficiency.

Maintain Buy rating and lower TP to HKD82.60 from HKD87.73, implying 48.4% upside

We cut FY26F revenue growth by 0.2% and lower FY26F earnings by 22.3%, considering the negative FX impact and M&A fees for the BioDlink acquisition. Our FY26F revenue / earnings are 0.2%/17.4% below Bloomberg consensus estimates.

We maintain our Buy rating. Due to our estimates change, t our DCF-based (assuming a WACC of 10.3% and a terminal growth rate of 4.5% -- both unchanged) TP drops to HKD82.60 from HKD87.73. The stock currently trades at 37.1x FY26F fully diluted EPS of CNY1.38.

<table><tr><td>Year-end 31 Dec</td><td colspan="2">FY25</td><td colspan="2">FY26F</td><td colspan="2">FY27F</td><td colspan="2">FY28F</td></tr><tr><td>Currency (CNY)</td><td>Actual</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td></td></tr><tr><td>Revenue (mn)</td><td>5,944</td><td>8,109</td><td>8,092</td><td>10,530</td><td>10,714</td><td>0</td><td>13,287</td><td></td></tr><tr><td>Reported net profit (mn)</td><td>1,480</td><td>2,173</td><td>1,688</td><td>2,894</td><td>2,554</td><td>0</td><td>3,238</td><td></td></tr><tr><td>Normalised net profit (mn)</td><td>1,480</td><td>2,173</td><td>1,688</td><td>2,894</td><td>2,554</td><td>0</td><td>3,238</td><td></td></tr><tr><td>FD normalised EPS</td><td>1.21</td><td>1.77</td><td>1.38</td><td>2.36</td><td>2.08</td><td></td><td>2.64</td><td></td></tr><tr><td>FD norm. EPS growth (%)</td><td>35.3</td><td>46.8</td><td>14.0</td><td>33.2</td><td>51.3</td><td></td><td>26.8</td><td></td></tr><tr><td>FD normalised P/E (x)</td><td>42.3</td><td>-</td><td>37.1</td><td>-</td><td>24.5</td><td>-</td><td>19.3</td><td></td></tr><tr><td>EV/EBITDA (x)</td><td>35.3</td><td>-</td><td>25.7</td><td>-</td><td>18.5</td><td>-</td><td>14.2</td><td></td></tr><tr><td>Price/book (x)</td><td>5.8</td><td>-</td><td>5.0</td><td>-</td><td>4.2</td><td>-</td><td>3.4</td><td></td></tr><tr><td>Dividend yield (%)</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td></td></tr><tr><td>ROE (%)</td><td>17.1</td><td>20.7</td><td>14.6</td><td>22.2</td><td>18.7</td><td></td><td>19.5</td><td></td></tr><tr><td>Net debt/equity (%)</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td></td><td>net cash</td><td></td></tr></table>

Source: Company data, NOM estimates  
Production Complete: 2026-07-24 08:01 UTC

Rating Remains Buy

Target price
Reduced from
HKD 87.73
HKD 82.60

Closing price
23 July 2026
HKD 55.65

<table><tr><td>Implied upside</td><td>+48.4%</td></tr></table>

<table><tr><td>Market Cap (USD mn)</td><td>8,988.0</td></tr><tr><td>ADT (USD mn)</td><td>40.6</td></tr></table>

## Relative performance chart

![](images/44dcc82167638ec53d9df94edba2ddac15c0896ab312cfdddf5d868b0b9c81c7.jpg)  
Source: LSEG, NOM Analysts

China Health Care & Pharmaceuticals

Jialin Zhang, CFA, CPA - NIHK  
jialin.zhang@NOM.com  
+852 2252 6134

## Key data on Wuxi XDC

<table><tr><td>Performance(%)</td><td>1M</td><td>3M</td><td>12M</td><td></td><td></td></tr><tr><td>Absolute (HKD)</td><td>13.9</td><td>-4.7</td><td>3.7</td><td>M cap (USDmn)</td><td>8,988.0</td></tr><tr><td>Absolute (USD)</td><td>13.9</td><td>-4.8</td><td>3.8</td><td>Free float (%)</td><td>78.4</td></tr><tr><td>Rel to Hang Seng Index</td><td>7.2</td><td>-0.8</td><td>6.3</td><td>3-mth ADT (USDmn)</td><td>40.6</td></tr></table>

<table><tr><td colspan="6">Income statement (CNYmn)</td></tr><tr><td>Year-end 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>Revenue</td><td>4,052</td><td>5,944</td><td>8,092</td><td>10,714</td><td>13,287</td></tr><tr><td>Cost of goods sold</td><td>-2,812</td><td>-3,805</td><td>-5,195</td><td>-6,825</td><td>-8,397</td></tr><tr><td>Gross profit</td><td>1,240</td><td>2,139</td><td>2,897</td><td>3,889</td><td>4,889</td></tr><tr><td>SG&amp;A</td><td>-320</td><td>-482</td><td>-630</td><td>-775</td><td>-942</td></tr><tr><td>Employee share expense</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Operating profit</td><td>920</td><td>1,658</td><td>2,267</td><td>3,114</td><td>3,948</td></tr><tr><td>EBITDA</td><td>1,027</td><td>1,787</td><td>2,514</td><td>3,433</td><td>4,339</td></tr><tr><td>Depreciation</td><td>-99</td><td>-126</td><td>-237</td><td>-303</td><td>-362</td></tr><tr><td>Amortisation</td><td>-8</td><td>-4</td><td>-10</td><td>-16</td><td>-29</td></tr><tr><td>EBIT</td><td>920</td><td>1,658</td><td>2,267</td><td>3,114</td><td>3,948</td></tr><tr><td>Net interest expense</td><td>-3</td><td>-17</td><td>-19</td><td>-21</td><td>-23</td></tr><tr><td>Associates &amp; JCEs</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other income</td><td>303</td><td>96</td><td>-81</td><td>107</td><td>133</td></tr><tr><td>Earnings before tax</td><td>1,220</td><td>1,737</td><td>2,167</td><td>3,200</td><td>4,058</td></tr><tr><td>Income tax</td><td>-150</td><td>-256</td><td>-390</td><td>-512</td><td>-649</td></tr><tr><td>Net profit after tax</td><td>1,070</td><td>1,480</td><td>1,777</td><td>2,688</td><td>3,409</td></tr><tr><td>Minority interests</td><td>0</td><td>0</td><td>-89</td><td>-134</td><td>-170</td></tr><tr><td>Other items</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Preferred dividends</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Normalised NPAT</td><td>1,070</td><td>1,480</td><td>1,688</td><td>2,554</td><td>3,238</td></tr><tr><td>Extraordinary items</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Reported NPAT</td><td>1,070</td><td>1,480</td><td>1,688</td><td>2,554</td><td>3,238</td></tr><tr><td>Dividends</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Transfer to reserves</td><td>1,070</td><td>1,480</td><td>1,688</td><td>2,554</td><td>3,238</td></tr><tr><td>Valuations and ratios</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Reported P/E (x)</td><td>57.3</td><td>42.3</td><td>37.1</td><td>24.5</td><td>19.3</td></tr><tr><td>Normalised P/E (x)</td><td>57.3</td><td>42.3</td><td>37.1</td><td>24.5</td><td>19.3</td></tr><tr><td>FD normalised P/E (x)</td><td>57.3</td><td>42.3</td><td>37.1</td><td>24.5</td><td>19.3</td></tr><tr><td>Dividend yield (%)</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Price/cashflow (x)</td><td>85.4</td><td>35.1</td><td>44.5</td><td>24.2</td><td>18.7</td></tr><tr><td>Price/book (x)</td><td>9.2</td><td>5.8</td><td>5.0</td><td>4.2</td><td>3.4</td></tr><tr><td>EV/EBITDA (x)</td><td>61.1</td><td>35.3</td><td>25.7</td><td>18.5</td><td>14.2</td></tr><tr><td>EV/EBIT (x)</td><td>68.2</td><td>38.1</td><td>28.5</td><td>20.4</td><td>15.6</td></tr><tr><td>Gross margin (%)</td><td>30.6</td><td>36.0</td><td>35.8</td><td>36.3</td><td>36.8</td></tr><tr><td>EBITDA margin (%)</td><td>25.3</td><td>30.1</td><td>31.1</td><td>32.0</td><td>32.7</td></tr><tr><td>EBIT margin (%)</td><td>22.7</td><td>27.9</td><td>28.0</td><td>29.1</td><td>29.7</td></tr><tr><td>Net margin (%)</td><td>26.4</td><td>24.9</td><td>20.9</td><td>23.8</td><td>24.4</td></tr><tr><td>Effective tax rate (%)</td><td>12.3</td><td>14.7</td><td>18.0</td><td>16.0</td><td>16.0</td></tr><tr><td>Dividend payout (%)</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>ROE (%)</td><td>17.7</td><td>17.1</td><td>14.6</td><td>18.7</td><td>19.5</td></tr><tr><td>ROA (pretax %)</td><td>18.6</td><td>16.5</td><td>15.6</td><td>18.1</td><td>20.5</td></tr><tr><td>Growth (%)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Revenue</td><td>90.8</td><td>46.7</td><td>36.1</td><td>32.4</td><td>24.0</td></tr><tr><td>EBITDA</td><td>153.3</td><td>74.0</td><td>40.6</td><td>36.6</td><td>26.4</td></tr><tr><td>Normalised EPS</td><td>221.6</td><td>35.3</td><td>14.0</td><td>51.3</td><td>26.8</td></tr><tr><td>Normalised FDEPS</td><td>238.9</td><td>35.3</td><td>14.0</td><td>51.3</td><td>26.8</td></tr></table>

Source: Company data, NOM estimates

<table><tr><td colspan="6">Cashflow statement (CNYmn)</td></tr><tr><td>Year-end 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>EBITDA</td><td>1,027</td><td>1,787</td><td>2,514</td><td>3,433</td><td>4,339</td></tr><tr><td>Change in working capital</td><td>-1,837</td><td>-3,177</td><td>-615</td><td>-419</td><td>-457</td></tr><tr><td>Other operating cashflow</td><td>1,527</td><td>3,173</td><td>-490</td><td>-425</td><td>-539</td></tr><tr><td>Cashflow from operations</td><td>717</td><td>1,783</td><td>1,409</td><td>2,588</td><td>3,343</td></tr><tr><td>Capital expenditure</td><td>-1,504</td><td>-1,245</td><td>-1,699</td><td></td><td></td></tr><tr><td>Free cashflow</td><td>-787</td><td>538</td><td>-290</td><td>2,588</td><td>3,343</td></tr><tr><td>Reduction in investments</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>Net acquisitions</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Dec in other LT assets</td><td>-17</td><td>-21</td><td>-78</td><td>-99</td><td>-116</td></tr><tr><td>Inc in other LT liabilities</td><td>17</td><td>26</td><td>17</td><td>18</td><td>18</td></tr><tr><td>Adjustments</td><td>-1,826</td><td>-3,808</td><td>-996</td><td>-1,185</td><td>-1,344</td></tr><tr><td>CF after investing acts</td><td>-2,613</td><td>-3,265</td><td>-1,346</td><td>1,322</td><td>1,901</td></tr><tr><td>Cash dividends</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Equity issue</td><td>0</td><td>2,486</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Debt issue</td><td>478</td><td>364</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Convertible debt issue</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Others</td><td>13</td><td>1</td><td>-3</td><td>-2</td><td>-2</td></tr><tr><td>CF from financial acts</td><td>491</td><td>2,851</td><td>-3</td><td>-2</td><td>-2</td></tr><tr><td>Net cashflow</td><td>-2,122</td><td>-414</td><td>-1,349</td><td>1,320</td><td>1,899</td></tr><tr><td>Beginning cash</td><td>4,048</td><td>1,925</td><td>1,511</td><td>162</td><td>1,481</td></tr><tr><td>Ending cash</td><td>1,925</td><td>1,511</td><td>162</td><td>1,481</td><td>3,380</td></tr><tr><td>Ending net debt</td><td>-1,925</td><td>-1,511</td><td>-162</td><td>-1,481</td><td>-3,380</td></tr><tr><td colspan="6">Balance sheet (CNYmn)</td></tr><tr><td>As at 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>Cash &amp; equivalents</td><td>1,925</td><td>1,511</td><td>162</td><td>1,481</td><td>3,380</td></tr><tr><td>Marketable securities</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Accounts receivable</td><td>1,800</td><td>2,138</td><td>2,620</td><td>3,380</td><td>4,083</td></tr><tr><td>Inventories</td><td>119</td><td>173</td><td>295</td><td>481</td><td>707</td></tr><tr><td>Other current assets</td><td>2,257</td><td>6,242</td><td>6,366</td><td>6,494</td><td>6,624</td></tr><tr><td>Total current assets</td><td>6,101</td><td>10,063</td><td>9,443</td><td>11,837</td><td>14,794</td></tr><tr><td>LT investments</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Fixed assets</td><td>2,725</td><td>4,039</td><td>5,424</td><td>6,201</td><td>7,052</td></tr><tr><td>Goodwill</td><td>215</td><td>215</td><td>1,291</td><td>1,291</td><td>1,291</td></tr><tr><td>Other intangible assets</td><td>45</td><td>58</td><td>48</td><td>139</td><td>243</td></tr><tr><td>Other LT assets</td><td>38</td><td>59</td><td>137</td><td>236</td><td>352</td></tr><tr><td>Total assets</td><td>9,124</td><td>14,435</td><td>16,343</td><td>19,704</td><td>23,732</td></tr><tr><td>Short-term debt</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Accounts payable</td><td>1,409</td><td>1,924</td><td>1,708</td><td>2,057</td><td>2,301</td></tr><tr><td>Other current liabilities</td><td>1,058</td><td>1,742</td><td>2,071</td><td>2,378</td><td>2,735</td></tr><tr><td>Total current liabilities</td><td>2,466</td><td>3,666</td><td>3,779</td><td>4,434</td><td>5,035</td></tr><tr><td>Long-term debt</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Convertible debt</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other LT liabilities</td><td>18</td><td>44</td><td>61</td><td>79</td><td>97</td></tr><tr><td>Total liabilities</td><td>2,485</td><td>3,710</td><td>3,841</td><td>4,513</td><td>5,133</td></tr><tr><td>Minority interest</td><td>0</td><td>0</td><td>89</td><td>223</td><td>394</td></tr><tr><td>Preferred stock</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Common stock</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Retained earnings</td><td>6,639</td><td>10,725</td><td>12,413</td><td>14,967</td><td>18,205</td></tr><tr><td>Proposed dividends</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other equity and reserves</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Total shareholders&#x27; equity</td><td>6,639</td><td>10,725</td><td>12,414</td><td>14,968</td><td>18,206</td></tr><tr><td>Total equity &amp; liabilities</td><td>9,124</td><td>14,435</td><td>16,343</td><td>19,704</td><td>23,732</td></tr><tr><td>Liquidity (x)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Current ratio</td><td>2.47</td><td>2.75</td><td>2.50</td><td>2.67</td><td>2.94</td></tr><tr><td>Interest cover</td><td>286.9</td><td>97.7</td><td>121.4</td><td>151.6</td><td>174.8</td></tr><tr><td>Leverage</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Net debt/EBITDA (x)</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td></tr><tr><td>Net debt/equity (%)</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td></tr><tr><td>Per share</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Reported EPS (CNY)</td><td>89.13c</td><td>1.21</td><td>1.38</td><td>2.08</td><td>2.64</td></tr><tr><td>Norm EPS (CNY)</td><td>89.13c</td><td>1.21</td><td>1.38</td><td>2.08</td><td>2.64</td></tr><tr><td>FD norm EPS (CNY)</td><td>89.13c</td><td>1.21</td><td>1.38</td><td>2.08</td><td>2.64</td></tr><tr><td>BVPS (CNY)</td><td>5.53</td><td>8.74</td><td>10.11</td><td>12.20</td><td>14.83</td></tr><tr><td>DPS (CNY)</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>Activity (days)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Days receivable</td><td>124.2</td><td>120.9</td><td>107.3</td><td>102.2</td><td>102.8</td></tr><tr><td>Days inventory</td><td>10.7</td><td>14.0</td><td>16.5</td><td>20.8</td><td>25.9</td></tr><tr><td>Days payable</td><td>150.8</td><td>159.8</td><td>127.6</td><td>100.7</td><td>95.0</td></tr><tr><td>Cash cycle</td><td>-15.9</td><td>-24.9</td><td>-3.8</td><td>22.3</td><td>33.7</td></tr></table>

Source: Company data, NOM estimates

## Company profile

WuXi XDC a leading Contract Research, Development and Manufacturing Organization (CRDMO), is focused on the global ADC and broader bioconjugate market. The company was co-founded by Wuxi Apptec and Wuxi Bio in May 2021 and went public on HKEX in November 2023, raising c.USD490mn. Up to date, Wuxi Bio and STA (Wuxi Apptec's holding subsidiary) held $c.49\%$ and $c.21\%$ of total shares.

## Valuation Methodology

We derive our target price of HKD82.60 from a DCF model assuming WACC of $10.3\%$ and terminal growth of $4.5\%$ . The benchmark index for the stock is the Hang Seng Index.

Risks that may impede the achievement of the target price

Downside risks: 1) geopolitical tensions; 2) failure to obtain commercial-stage programs; 3) ADC modality become unattractive; and 4) rising competition.

## ESG

Wuxi XDC has established a comprehensive and integrated Environmental, Health and Safety (EHS) management system, sourcing ethically, reducing environmental footprint, advocating reduced energy consumption, minimizing effluent, and acting responsibly to reduce operational impact on the environment. The company strives to advance a diverse workforce and create an equal and inclusive corporate culture. Wuxi XDC recruits employees based on their professional and academic achievements regardless of religion, disability, age, race, color, sex, gender identity, sexual orientation, or marital status to provide equal employment opportunity. Along with the creation of self-owned compliance management system and ethical standards training programs for all employees, the company has a firm “Zero tolerance” for bribery and corruption principles along with commitment to honesty and trustworthy business conduct to promote ESG culture.

Fig. 1: Wuxi XDC 1H26F income statement forecast

<table><tr><td>CNY mn</td><td>1H25</td><td>1H26F</td><td>YoY</td></tr><tr><td>Revenue</td><td>2,701</td><td>3,815</td><td>41%</td></tr><tr><td>COGS</td><td>(1,726)</td><td>(2,441)</td><td>41%</td></tr><tr><td>Gross profit</td><td>975</td><td>1,373</td><td>41%</td></tr><tr><td>GP margin(%)</td><td>36.1%</td><td>36.0%</td><td></td></tr><tr><td>R&amp;D expenses</td><td>(49)</td><td>(69)</td><td>39%</td></tr><tr><td>G&amp;A expenses</td><td>(108)</td><td>(191)</td><td>77%</td></tr><tr><td>Selling expenses</td><td>(49)</td><td>(69)</td><td>40%</td></tr><tr><td>Operating profit</td><td>769</td><td>1,045</td><td>36%</td></tr><tr><td>OP margin(%)</td><td>28.5%</td><td>27.4%</td><td></td></tr><tr><td>Other income and expenses</td><td>106</td><td>(76)</td><td>-172%</td></tr><tr><td>Interest expenses</td><td>(8)</td><td>(10)</td><td>30%</td></tr><tr><td>Pre-tax profit</td><td>867</td><td>959</td><td>11%</td></tr><tr><td>Income tax</td><td>(121)</td><td>(173)</td><td>42%</td></tr><tr><td>Profit after tax</td><td>746</td><td>786</td><td>5%</td></tr><tr><td>NP margin(%)</td><td>2

[中间内容因长度限制已省略]

 AN INDEPENDENT FINANCIAL ADVISER REGARDING THE SUITABILITY OF THE INVESTMENT, UNDER A SEPARATE ENGAGEMENT, AS THE RECIPIENT DEEMS FIT. Unless prohibited by the provisions of Regulation S of the 1933 Act, this material is distributed in the US, by NSI, a US-registered broker-dealer, which accepts responsibility for its contents in accordance with the provisions of Rule 15a-6, under the US Securities Exchange Act of 1934. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents

available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia ('Saudi Arabia') or a 'Market Counterparty' or a 'Professional Client' (as defined by the Dubai Financial Services Authority) in the United Arab Emirates ('UAE') or a 'Market Counterparty' or a 'Business Customer' (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar ('Qatar') by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
