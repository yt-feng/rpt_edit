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
26 July 2026

EQUITY: TECHNOLOGY

## 2Q26 in line, positive on share buyback

## Reiterate Buy with a revised TP of CNY632

## 2Q26 net profit +36% y-y to CNY22.5bn, in line with our expectation

CATL reported 1H26/2Q26 results after market close on 24 July. The company reported 42% y-y earnings growth to CNY43.3bn in 1H26, translating into 36% y-y and 9% q-q earnings growth to CNY22.5bn for 2Q26, which is in line with market expectation of CNY22-23bn, in our view. The company recorded 55% y-y revenue growth to CNY277bn in 1H25 (2Q26: +57% y-y or +14% q-q to CNY148bn), with GPM contracting 1.1pp y-y to 23.9% (2Q26: down 2.4pp y-y or 1.7pp q-q to 23.2%), which we attribute to material cost inflation and change in revenue mix.

Resilient demand outlook for FY27-28F with impact of cost inflation under control

For 1H26, the company recorded revenue growth of 46%/88% y-y for the EV/ESS battery segments to CNY192/53bn. We estimate \~60% y-y growth in total battery shipments to 430-440GWh for 1H26 (2Q26: +10-15% q-q to \~230GWh), implying an ex.VAT battery ASP of approximately CNY0.57/Wh, which is largely flat h-h. We expect the company to record 51% y-y growth in battery shipments to \~1TWh in FY26F, followed by 19-22% growth over FY27-28F, supported by resilient demand growth from global EV penetration and growing ESS installation in both domestic and overseas markets.

## A-share buyback of CNY20-40bn likely positive on market sentiment

CATL also announced to buy back A-shares worth CNY20-40bn within 12 months after shareholders' meeting approval, accounting for approximately 1.1-2.3% of its latest A-share market cap (or 0.8-1.5% if it buys back at a price cap of CNY573 per share). We view the share buyback plan positive on market sentiment with improved shareholders' return for the company.

## Reiterate Buy with TP lifted to CNY632

We raise FY26-28F revenue forecasts by 5.7-8.6% to reflect stronger-than-expected battery shipments and non-battery revenue growth, but we cut GPM forecasts by 0.6-1.4pp considering changes in revenue mix. Our FY26-28F earnings forecast are 3.3-5.3% higher than our previous estimates. We reiterate our Buy rating and lift TP to CNY632, based on unchanged 25x FY27F EPS of CNY25.26, which implies 1.25x FY27F PEG based on FY26-28F earnings CAGR of 20%. The stock is trading at 18/15x FY26/27F P/E, which is undemanding in our view.

<table><tr><td>Year-end 31 Dec</td><td colspan="2">FY25</td><td colspan="2">FY26F</td><td colspan="2">FY27F</td><td colspan="2">FY28F</td></tr><tr><td>Currency (CNY)</td><td>Actual</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td></td></tr><tr><td>Revenue (mn)</td><td>423,702</td><td>604,964</td><td>639,448</td><td>712,550</td><td>765,031</td><td>813,124</td><td>882,936</td><td></td></tr><tr><td>Reported net profit (mn)</td><td>72,201</td><td>91,472</td><td>96,345</td><td>111,655</td><td>115,302</td><td>132,177</td><td>136,785</td><td></td></tr><tr><td>Normalised net profit (mn)</td><td>72,201</td><td>91,472</td><td>96,345</td><td>111,655</td><td>115,302</td><td>132,177</td><td>136,785</td><td></td></tr><tr><td>FD normalised EPS</td><td>15.82</td><td>20.04</td><td>21.11</td><td>24.47</td><td>25.26</td><td>28.96</td><td>29.97</td><td></td></tr><tr><td>FD norm. EPS growth (%)</td><td>42.3</td><td>26.7</td><td>33.4</td><td>22.1</td><td>19.7</td><td>18.4</td><td>18.6</td><td></td></tr><tr><td>FD normalised P/E (x)</td><td>24.2</td><td>-</td><td>18.1</td><td>-</td><td>15.2</td><td>-</td><td>12.8</td><td></td></tr><tr><td>EV/EBITDA (x)</td><td>16.1</td><td>-</td><td>10.6</td><td>-</td><td>8.7</td><td>-</td><td>7.0</td><td></td></tr><tr><td>Price/book (x)</td><td>5.2</td><td>-</td><td>4.4</td><td>-</td><td>3.8</td><td>-</td><td>1.5</td><td></td></tr><tr><td>Dividend yield (%)</td><td>2.1</td><td>-</td><td>2.8</td><td>-</td><td>2.0</td><td>-</td><td>4.9</td><td></td></tr><tr><td>ROE (%)</td><td>24.7</td><td>25.1</td><td>26.2</td><td>26.2</td><td>26.8</td><td>26.0</td><td>26.5</td><td></td></tr><tr><td>Net debt/equity (%)</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td></td></tr></table>

Source: Company data, NOM estimates  
Production Complete: 2026-07-26 05:13 UTC

Rating Remains Buy

Target price
Increased from
CNY 612.00
CNY 632.00

Closing price CNY 383.01 24 July 2026

<table><tr><td>Implied upside</td><td>+65.0%</td></tr></table>

<table><tr><td>Market Cap (USD mn)</td><td>249,212.9</td></tr><tr><td>ADT (USD mn)</td><td>2,125.6</td></tr></table>

## Relative performance chart

![](images/0b18f9e5d2730df3f5154932dba4dfab954bde3eb9e5a43d6f73568ce47d805a.jpg)  
Source: LSEG, NOM

## Research Analysts

Global EV Batteries & Materials

Ethan Zhang - NIHK  
ethan.zhang@NOM.com  
+852 2252 2157

China Autos & Auto Parts

Joel Ying, CFA - NIHK
joel.ying@NOM.com
+852 2252 2153

## Japan technology

Manabu Akizuki - NSC
manabu.akizuki@NOM.com
+81 3 6703 1185

# Key data on Contemporary Amperex Technology

<table><tr><td>Performance(%)</td><td>1M</td><td>3M</td><td>12M</td><td></td><td></td></tr><tr><td>Absolute (CNY)</td><td>-3.1</td><td>-13.9</td><td>34.3</td><td>M cap (USDmn)</td><td>249,212.9</td></tr><tr><td>Absolute (USD)</td><td>-2.7</td><td>-13.1</td><td>41.8</td><td>Free float (%)</td><td>54.4</td></tr><tr><td>Rel to CSI 300</td><td>2.8</td><td>-11.4</td><td>22.2</td><td>3-mth ADT (USDmn)</td><td>2,125.6</td></tr></table>

Cashflow statement (CNYmn)

<table><tr><td colspan="6">Income statement (CNYmn)</td></tr><tr><td>Year-end 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>Revenue</td><td>362,013</td><td>423,702</td><td>639,448</td><td>765,031</td><td>882,936</td></tr><tr><td>Cost of goods sold</td><td>-273,519</td><td>-312,383</td><td>-488,315</td><td>-584,296</td><td>-669,703</td></tr><tr><td>Gross profit</td><td>88,494</td><td>111,319</td><td>151,133</td><td>180,735</td><td>213,233</td></tr><tr><td>SG&amp;A</td><td>-33,917</td><td>-40,381</td><td>-49,752</td><td>-58,758</td><td>-68,697</td></tr><tr><td>Employee share expense</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Operating profit</td><td>54,577</td><td>70,938</td><td>101,381</td><td>121,977</td><td>144,537</td></tr><tr><td>EBITDA</td><td>77,015</td><td>95,261</td><td>137,331</td><td>157,155</td><td>177,186</td></tr><tr><td>Depreciation</td><td>-22,438</td><td>-24,323</td><td>-35,950</td><td>-35,178</td><td>-32,650</td></tr><tr><td>Amortisation</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EBIT</td><td>54,577</td><td>70,938</td><td>101,381</td><td>121,977</td><td>144,537</td></tr><tr><td>Net interest expense</td><td>4,132</td><td>7,940</td><td>4,665</td><td>7,234</td><td>11,668</td></tr><tr><td>Associates &amp; JCEs</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other income</td><td>4,473</td><td>10,649</td><td>17,990</td><td>19,228</td><td>19,542</td></tr><tr><td>Earnings before tax</td><td>63,182</td><td>89,527</td><td>124,036</td><td>148,438</td><td>175,747</td></tr><tr><td>Income tax</td><td>-9,175</td><td>-12,740</td><td>-20,132</td><td>-24,093</td><td>-28,525</td></tr><tr><td>Net profit after tax</td><td>54,007</td><td>76,786</td><td>103,904</td><td>124,346</td><td>147,222</td></tr><tr><td>Minority interests</td><td>-3,262</td><td>-4,585</td><td>-7,559</td><td>-9,044</td><td>-10,438</td></tr><tr><td>Other items</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Preferred dividends</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Normalised NPAT</td><td>50,745</td><td>72,201</td><td>96,345</td><td>115,302</td><td>136,785</td></tr><tr><td>Extraordinary items</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Reported NPAT</td><td>50,745</td><td>72,201</td><td>96,345</td><td>115,302</td><td>136,785</td></tr><tr><td>Dividends</td><td>-25,372</td><td>-36,101</td><td>-48,172</td><td>-34,591</td><td>-41,035</td></tr><tr><td>Transfer to reserves</td><td>25,372</td><td>36,101</td><td>48,172</td><td>80,711</td><td>95,749</td></tr><tr><td>Valuations and ratios</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Reported P/E (x)</td><td>34.4</td><td>24.2</td><td>18.1</td><td>15.2</td><td>12.8</td></tr><tr><td>Normalised P/E (x)</td><td>34.4</td><td>24.2</td><td>18.1</td><td>15.2</td><td>12.8</td></tr><tr><td>FD normalised P/E (x)</td><td>34.4</td><td>24.2</td><td>18.1</td><td>15.2</td><td>12.8</td></tr><tr><td>Dividend yield (%)</td><td>1.5</td><td>2.1</td><td>2.8</td><td>2.0</td><td>4.9</td></tr><tr><td>Price/cashflow (x)</td><td>18.0</td><td>13.1</td><td>10.6</td><td>9.9</td><td>9.4</td></tr><tr><td>Price/book (x)</td><td>7.1</td><td>5.2</td><td>4.4</td><td>3.8</td><td>1.5</td></tr><tr><td>EV/EBITDA (x)</td><td>20.4</td><td>16.1</td><td>10.6</td><td>8.7</td><td>7.0</td></tr><tr><td>EV/EBIT (x)</td><td>28.7</td><td>21.7</td><td>14.3</td><td>11.2</td><td>8.6</td></tr><tr><td>Gross margin (%)</td><td>24.4</td><td>26.3</td><td>23.6</td><td>23.6</td><td>24.2</td></tr><tr><td>EBITDA margin (%)</td><td>21.3</td><td>22.5</td><td>21.5</td><td>20.5</td><td>20.1</td></tr><tr><td>EBIT margin (%)</td><td>15.1</td><td>16.7</td><td>15.9</td><td>15.9</td><td>16.4</td></tr><tr><td>Net margin (%)</td><td>14.0</td><td>17.0</td><td>15.1</td><td>15.1</td><td>15.5</td></tr><tr><td>Effective tax rate (%)</td><td>14.5</td><td>14.2</td><td>16.2</td><td>16.2</td><td>16.2</td></tr><tr><td>Dividend payout (%)</td><td>50.0</td><td>50.0</td><td>50.0</td><td>30.0</td><td>30.0</td></tr><tr><td>ROE (%)</td><td>22.8</td><td>24.7</td><td>26.2</td><td>26.8</td><td>26.5</td></tr><tr><td>ROA (pretax %)</td><td>11.0</td><td>11.9</td><td>14.7</td><td>17.0</td><td>19.9</td></tr><tr><td>Growth (%)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Revenue</td><td>-9.7</td><td>17.0</td><td>50.9</td><td>19.6</td><td>15.4</td></tr><tr><td>EBITDA</td><td>15.9</td><td>23.7</td><td>44.2</td><td>14.4</td><td>12.7</td></tr><tr><td>Normalised EPS</td><td>11.0</td><td>42.3</td><td>33.4</td><td>19.7</td><td>18.6</td></tr><tr><td>Normalised FDEPS</td><td>11.0</td><td>42.3</td><td>33.4</td><td>19.7</td><td>18.6</td></tr></table>

Source: Company data, NOM estimates

<table><tr><td colspan="6">Cashflow statement (CNYmn)</td></tr><tr><td>Year-end 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>EBITDA</td><td>77,015</td><td>95,261</td><td>137,331</td><td>157,155</td><td>177,186</td></tr><tr><td>Change in working capital</td><td>-11,366</td><td>-8,479</td><td>21,790</td><td>14,426</td><td>6,515</td></tr><tr><td>Other operating cashflow</td><td>31,342</td><td>46,439</td><td>5,900</td><td>4,262</td><td>3,184</td></tr><tr><td>Cashflow from operations</td><td>96,990</td><td>133,220</td><td>165,022</td><td>175,843</td><td>186,886</td></tr><tr><td>Capital expenditure</td><td>-31,180</td><td>-42,345</td><td>-45,000</td><td>-40,500</td><td>-30,375</td></tr><tr><td>Free cashflow</td><td>65,810</td><td>90,875</td><td>120,022</td><td>135,343</td><td>156,511</td></tr><tr><td>Reduction in investments</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Net acquisitions</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Dec in other LT assets</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Inc in other LT liabilities</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Adjustments</td><td>-17,695</td><td>-52,131</td><td>0</td><td>0</td><td>0</td></tr><tr><td>CF after investing acts</td><td>48,115</td><td>38,744</td><td>120,022</td><td>135,343</td><td>156,511</td></tr><tr><td>Cash dividends</td><td>-25,807</td><td>-34,923</td><td>-36,101</td><td>-48,172</td><td>-34,591</td></tr><tr><td>Equity issue</td><td>2,560</td><td>44,814</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Debt issue</td><td>10,568</td><td>-11,912</td><td>-5,000</td><td>-5,000</td><td>-5,000</td></tr><tr><td>Convertible debt issue</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Others</td><td>-3,442</td><td>-6,953</td><td>0</td><td>0</td><td>0</td></tr><tr><td>CF from financial acts</td><td>-16,121</td><td>-8,974</td><td>-41,101</td><td>-53,172</td><td>-39,591</td></tr><tr><td>Net cashflow</td><td>31,994</td><td>29,770</td><td>78,921</td><td>82,171</td><td>116,920</td></tr><tr><td>Beginning cash</td><td>238,165</td><td>270,160</td><td>299,930</td><td>378,851</td><td>461,022</td></tr><tr><td>Ending cash</td><td>270,160</td><td>299,930</td><td>378,851</td><td>461,022</td><td>577,942</td></tr><tr><td>Ending net debt</td><td>-146,344</td><td>-186,522</td><td>-270,443</td><td>-357,614</td><td>-479,534</td></tr><tr><td colspan="6">Balance sheet (CNYmn)</td></tr><tr><td>As at 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>Cash &amp; equivalents</td><td>270,160</td><td>299,930</td><td>378,851</td><td>461,022</td><td>577,942</td></tr><tr><td>Marketable securities</td><td>33,352</td><td>33,583</td><td>33,583</td><td>33,583</td><td>33,583</td></tr><tr><td>Accounts receivable</td><td>72,377</td><td>94,108</td><td>108,110</td><td>118,862</td><td>125,086</td></tr><tr><td>Inventories</td><td>59,836</td><td>94,526</td><td>113,959</td><td>128,355</td><td>137,942</td></tr><tr><td>Other current assets</td><td>74,417</td><td>116,334</td><td>116,334</td><td>116,334</td><td>116,334</td></tr><tr><td>Total current assets</td><td>510,142</td><td>638,482</td><td>750,838</td><td>858,156</td><td>990,888</td></tr><tr><td>LT investments</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Fixed assets</td><td>142,344</td><td>176,134</td><td>176,523</td><td>173,185</td><td>162,250</td></tr><tr><td>Goodwill</td><td>14,420</td><td>15,264</td><td>14,752</td><td>14,240</td><td>13,728</td></tr><tr><td>Other intangible assets</td><td>119,752</td><td>144,948</td><td>143,184</td><td>141,419</td><td>139,655</td></tr><tr><td>Other LT assets</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Total assets</td><td>786,658</td><td>974,828</td><td>1,085,297</td><td>1,187,000</td><td>1,306,521</td></tr><tr><td>Short-term debt</td><td>42,578</td><td>35,173</td><td>35,173</td><td>35,173</td><td>35,173</td></tr><tr><td>Accounts payable</td><td>242,585</td><td>308,996</td><td>364,221</td><td>403,795</td><td>426,121</td></tr><tr><td>Other current liabilities</td><td>32,009</td><td>55,457</td><td>55,457</td><td>55,457</td><td>55,457</td></tr><tr><td>Total current liabilities</td><td>317,172</td><td>399,626</td><td>454,851</td><td>494,425</td><td>516,751</td></tr><tr><td>Long-term debt</td><td>81,238</td><td>78,235</td><td>73,235</td><td>68,235</td><td>63,235</td></tr><tr><td>Convertible debt</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other LT liabilities</td><td>114,792</td><td>125,940</td><td>125,940</td><td>125,940</td><td>125,940</td></tr><tr><td>Total liabilities</td><td>513,202</td><td>603,801</td><td>654,026</td><td>688,600</td><td>705,927</td></tr><tr><td>Minority interest</td><td>26,526</td><td>33,919</td><td>33,919</td><td>33,919</td><td>33,919</td></tr><tr><td>Preferred stock</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Common stock</td><td>4,403</td><td>4,564</td><td>4,564</td><td>4,564</td><td>4,564</td></tr><tr><td>Retained earnings</td><td>242,527</td><td>332,544</td><td>392,788</td><td>459,918</td><td>562,112</td></tr><tr><td>Proposed dividends</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other equity and reserves</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Total shareholders&#x27; equity</td><td>246,930</td><td>337,108</td><td>397,352</td><td>464,481</td><td>566,675</td></tr><tr><td>Total equity &amp; liabilities</td><td>786,658</td><td>974,828</td><td>1,085,297</td><td>1,187,000</td><td>1,306,521</td></tr><tr><td>Liquidity (x)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Current ratio</td><td>1.61</td><td>1.60</td><td>1.65</td><td>1.74</td><td>1.92</td></tr><tr><td>Interest cover</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Leverage</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Net debt/EBITDA (x)</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td></tr><tr><td>Net debt/equity (%)</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td></tr><tr><td>Per share</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Reported EPS (CNY)</td><td>11.12</td><td>15.82</td><td>21.11</td><td>25.26</td><td>29.97</td></tr><tr><td>Norm EPS (CNY)</td><td>11.12</td><td>15.82</td><td>21.11</td><td>25.26</td><td>29.97</td></tr><tr><td>FD norm EPS (CNY)</td><td>11.12</td><td>15.82</td><td>21.11</td><td>25.26</td><td>29.97</td></tr><tr><td>BVPS (CNY)</td><td>54.11</td><td>73.87</td><td>87.07</td><td>101.78</td><td>257.38</td></tr><tr><td>DPS (CNY)</td><td>5.56</td><td>7.91</td><td>10.56</td><td>7.58</td><td>18.64</td></tr><tr><td>Activity (days)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Days receivable</td><td>74.7</td><td>71.7</td><td>57.7</td><td>54.1</td><td>50.6</td></tr><tr><td>Days inventory</td><td>70.2</td><td>90.2</td><td>77.9</td><td>75.7</td><td>72.8</td></tr><tr><td>Days payable</td><td>318.5</td><td>322.2</td><td>251.6</td><td>239.9</td><td>226.8</td></tr><tr><td>Cash cycle</td><td>-173.6</td><td>-160.4</td><td>-116.0</td><td>-110.1</td><td>-103.5</td></tr></table>

Source: Company data, NOM estimates

## Company profile

Contemporary Amperex Technology Co Ltd (CATL) is a China-based battery manufacturer founded in 2011. The company specializes in the manufacturing of lithium-ion batteries for electric vehicles and energy storage systems, as well as battery management systems.

## Valuation Methodology

Our TP of CNY632.00 is based on 25x of 2027F EPS of CNY25.26, which implies 1.25x FY27F PEG based on FY26-28F earnings CAGR of $20\%$ . The benchmark index is CSI300.

Risks that may impede the achievement of the target price

Downside risks: 1) stronger-than-expected raw material price hike; 2) slower-than-expected shipments to global OEMs; and 3) intensified competition in both China and overseas markets.

## ESG

As the leading lithium-ion battery manufacturer globally, CATL supplies batteries to both electric vehicle (EV) and energy storage application (ESS) sectors. Battery is the key component to promote the electrification trend of the global auto industry to replace traditional internal combustion engine (ICE) vehicles with reduced carbon dioxide emission. ESS battery helps to improve the utilization of electricity generated by renewable ener

[中间内容因长度限制已省略]

 SUITABILITY OF THE INVESTMENT, UNDER A SEPARATE ENGAGEMENT, AS THE RECIPIENT DEEMS FIT. Unless prohibited by the provisions of Regulation S of the 1933 Act, this material is distributed in the US, by NSI, a US-registered broker-dealer, which accepts responsibility for its contents in accordance with the provisions of Rule 15a-6, under the US Securities Exchange Act of 1934. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia ('Saudi Arabia') or a 'Market Counterparty' or a 'Professional Client' (as defined by the Dubai Financial Services Authority) in the United Arab Emirates ('UAE') or a 'Market Counterparty' or a 'Business Customer' (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar ('Qatar') by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, "Offshore Issuers") that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
