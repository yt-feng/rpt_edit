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
EQUITY: TECHNOLOGY

# Honing the edge of advanced silicon test

## Beneficiary of structural AI/HPC testing growth and enabler of new technologies; initiate at Buy

## Initiate coverage at Buy with TP of TWD11,100, implying \~73% upside

We initiate coverage of Hon. Precision (Hon) with a Buy rating and a target price of TWD11,100, based on 40x average 2027-28F EPS of TWD277. Our target P/E multiple is at the high end of Hon's historical trading band of 19-52x since its IPO, which we consider undemanding given a 58% net earnings CAGR through 2026-28F. The stock is currently trading at 29x 2027F EPS of TWD219, compared with semiconductor-backend equipment and test interface vendors (2027E Bloomberg consensus average P/E 37x). Hon is an equipment manufacturer focusing on IC test handlers and active thermal control systems (ATC) used in the final test (FT) or system level test (SLT), and AI/HPC/ASIC make up c.80% of its tool orders. We expect Hon to capitalize on an extended testing time for AI/HPC chips due to increased chip design complexity and larger package footprints, and increasing testing capex by AI OSATs and semiconductor manufacturing reshoring in the US indicate potential upside to Hon's ATC/handlers. We estimate Hon to record a revenue CAGR of 59% and model EPS at TWD134/TWD219/TWD336 for 2026-28F. A major downside risk to our view is CoWoS and backend testing capacity expansion slowdown.

## Clear ATC upgrades down the road could boost ASP; handler upgrades in sight with new technologies on the horizon

A clear visibility of ATC roadmap and well execution, in our view, put Hon in a more favorable position for AI/HPC clients looking to initiate new chip development. We believe Hon should enjoy an ASP uptrend from AI/HPC customers' migration to more powerful ATC in view of increasingly stringent thermal requirements, and GPU-on-GPU SolC stack for a leading AI GPU customer's 2028E platform could make such advancement more imperative. We also think OSATs may have to upgrade the handlers beyond 2027-28F for internal mechanics to support large packages (e.g., 10-11x reticle-size interposers, CoPoS, embedded multi-die interconnect bridge [EMIB]), and the emergence of co-packaged optics (CPO) test insertions and micro-channel lids (MCL) could also drive new purchases of dedicated handlers. In addition to AI/HPC, we observe growing testing contents in mobile application processors (APs) and CPUs as well thanks to advanced packaging or multi-die layouts, and believe Hon should be a key beneficiary of a strong FT handler foothold in these areas.

<table><tr><td>Year-end 31 Dec</td><td colspan="2">FY25</td><td colspan="2">FY26F</td><td colspan="2">FY27F</td><td colspan="2">FY28F</td></tr><tr><td>Currency (TWD)</td><td>Actual</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td></td></tr><tr><td>Revenue (mn)</td><td>30,271</td><td>0</td><td>57,406</td><td>0</td><td>94,295</td><td>0</td><td>145,102</td><td></td></tr><tr><td>Reported net profit (mn)</td><td>12,362</td><td>0</td><td>24,182</td><td>0</td><td>39,375</td><td>0</td><td>60,563</td><td></td></tr><tr><td>Normalised net profit (mn)</td><td>12,362</td><td>0</td><td>24,182</td><td>0</td><td>39,375</td><td>0</td><td>60,563</td><td></td></tr><tr><td>FD normalised EPS</td><td>75.69</td><td></td><td>134.40</td><td></td><td>218.84</td><td></td><td>336.59</td><td></td></tr><tr><td>FD norm. EPS growth (%)</td><td>129.8</td><td></td><td>77.6</td><td></td><td>62.8</td><td></td><td>53.8</td><td></td></tr><tr><td>FD normalised P/E (x)</td><td>84.6</td><td>-</td><td>47.7</td><td>-</td><td>29.3</td><td>-</td><td>19.0</td><td></td></tr><tr><td>EV/EBITDA (x)</td><td>72.7</td><td>-</td><td>37.8</td><td>-</td><td>22.6</td><td>-</td><td>14.3</td><td></td></tr><tr><td>Price/book (x)</td><td>19.9</td><td>-</td><td>16.3</td><td>-</td><td>12.4</td><td>-</td><td>9.1</td><td></td></tr><tr><td>Dividend yield (%)</td><td>1.0</td><td>-</td><td>1.5</td><td>-</td><td>2.4</td><td>-</td><td>3.7</td><td></td></tr><tr><td>ROE (%)</td><td>34.5</td><td></td><td>37.6</td><td></td><td>48.1</td><td></td><td>55.3</td><td></td></tr><tr><td>Net debt/equity (%)</td><td>net cash</td><td></td><td>net cash</td><td></td><td>net cash</td><td></td><td>net cash</td><td></td></tr></table>

Source: Company data, NOM estimates

24 July 2026

Rating
Starts at
Buy

Target price
Starts at
TWD 11,100.00

Closing price 22 July 2026 TWD 6,405.00

<table><tr><td>Implied upside</td><td>+73.3%</td></tr></table>

<table><tr><td>Market Cap (USD mn)</td><td>35,647.6</td></tr><tr><td>ADT (USD mn)</td><td>188.9</td></tr></table>

## Relative performance chart

![](images/a002956ea8ad477761599c26920336df0b66a3e8627bd8677c42fe7fb5cf4d46.jpg)  
Source: LSEG, NOM

## Research Analysts

Semiconductor

Eric Chen, CFA - NITB
eric.chen@NOM.com
+886(2) 21769965

Aaron Jeng, CFA - NITB
aaron.jeng@NOM.com
+886(2) 21769962

Vivian Yang - NITB
vivian.yang@NOM.com
+886(2) 21769970

## Key data on Hon. Precision, Inc.

Income statement (TWDmn)

<table><tr><td>Performance(%)</td><td>1M</td><td>3M</td><td>12M</td><td></td><td></td></tr><tr><td>Absolute (TWD)</td><td>-7.4</td><td>35.0</td><td>305.4</td><td>M cap (USDmn)</td><td>35,647.6</td></tr><tr><td>Absolute (USD)</td><td>-9.3</td><td>31.4</td><td>269.6</td><td>Free float (%)</td><td>46.7</td></tr><tr><td>Rel to TaiwanTAIEX Index</td><td>-1.3</td><td>16.6</td><td>210.4</td><td>3-mth ADT (USDmn)</td><td>188.9</td></tr></table>

<table><tr><td colspan="6">Income Statement (FYBH)</td></tr><tr><td>Year-end 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>Revenue</td><td>13,992</td><td>30,271</td><td>57,406</td><td>94,295</td><td>145,102</td></tr><tr><td>Cost of goods sold</td><td>-6,293</td><td>-13,157</td><td>-24,835</td><td>-40,624</td><td>-62,610</td></tr><tr><td>Gross profit</td><td>7,700</td><td>17,114</td><td>32,571</td><td>53,671</td><td>82,492</td></tr><tr><td>SG&amp;A</td><td>-1,415</td><td>-2,068</td><td>-3,613</td><td>-5,752</td><td>-8,416</td></tr><tr><td>Employee share expense</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Operating profit</td><td>6,285</td><td>15,046</td><td>28,958</td><td>47,919</td><td>74,076</td></tr><tr><td>EBITDA</td><td>6,330</td><td>15,114</td><td>29,076</td><td>48,108</td><td>74,380</td></tr><tr><td>Depreciation</td><td>-46</td><td>-69</td><td>-118</td><td>-189</td><td>-304</td></tr><tr><td>Amortisation</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>EBIT</td><td>6,285</td><td>15,046</td><td>28,958</td><td>47,919</td><td>74,076</td></tr><tr><td>Net interest expense</td><td>160</td><td>306</td><td>1,108</td><td>1,300</td><td>1,627</td></tr><tr><td>Associates &amp; JCEs</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Other income</td><td>239</td><td>232</td><td>179</td><td>0</td><td>0</td></tr><tr><td>Earnings before tax</td><td>6,683</td><td>15,584</td><td>30,245</td><td>49,219</td><td>75,703</td></tr><tr><td>Income tax</td><td>-1,397</td><td>-3,222</td><td>-6,063</td><td>-9,844</td><td>-15,141</td></tr><tr><td>Net profit after tax</td><td>5,286</td><td>12,362</td><td>24,182</td><td>39,375</td><td>60,563</td></tr><tr><td>Minority interests</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Other items</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Preferred dividends</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Normalised NPAT</td><td>5,286</td><td>12,362</td><td>24,182</td><td>39,375</td><td>60,563</td></tr><tr><td>Extraordinary items</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Reported NPAT</td><td>5,286</td><td>12,362</td><td>24,182</td><td>39,375</td><td>60,563</td></tr><tr><td>Dividends</td><td>-3,636</td><td>-11,694</td><td>-16,927</td><td>-27,563</td><td>-42,394</td></tr><tr><td>Transfer to reserves</td><td>1,650</td><td>668</td><td>7,255</td><td>11,813</td><td>18,169</td></tr><tr><td colspan="6">Valuations and ratios</td></tr><tr><td>Reported P/E (x)</td><td>194.4</td><td>84.6</td><td>47.7</td><td>29.3</td><td>19.0</td></tr><tr><td>Normalised P/E (x)</td><td>194.4</td><td>84.6</td><td>47.7</td><td>29.3</td><td>19.0</td></tr><tr><td>FD normalised P/E (x)</td><td>194.4</td><td>84.6</td><td>47.7</td><td>29.3</td><td>19.0</td></tr><tr><td>Dividend yield (%)</td><td>0.4</td><td>1.0</td><td>1.5</td><td>2.4</td><td>3.7</td></tr><tr><td>Price/cashflow (x)</td><td>445.3</td><td>64.6</td><td>56.5</td><td>34.5</td><td>22.7</td></tr><tr><td>Price/book (x)</td><td>75.4</td><td>19.9</td><td>16.3</td><td>12.4</td><td>9.1</td></tr><tr><td>EV/EBITDA (x)</td><td>181.1</td><td>72.7</td><td>37.8</td><td>22.6</td><td>14.3</td></tr><tr><td>EV/EBIT (x)</td><td>182.4</td><td>73.0</td><td>38.0</td><td>22.6</td><td>14.4</td></tr><tr><td>Gross margin (%)</td><td>55.0</td><td>56.5</td><td>56.7</td><td>56.9</td><td>56.9</td></tr><tr><td>EBITDA margin (%)</td><td>45.2</td><td>49.9</td><td>50.7</td><td>51.0</td><td>51.3</td></tr><tr><td>EBIT margin (%)</td><td>44.9</td><td>49.7</td><td>50.4</td><td>50.8</td><td>51.1</td></tr><tr><td>Net margin (%)</td><td>37.8</td><td>40.8</td><td>42.1</td><td>41.8</td><td>41.7</td></tr><tr><td>Effective tax rate (%)</td><td>20.9</td><td>20.7</td><td>20.0</td><td>20.0</td><td>20.0</td></tr><tr><td>Dividend payout (%)</td><td>68.8</td><td>94.6</td><td>70.0</td><td>70.0</td><td>70.0</td></tr><tr><td>ROE (%)</td><td>40.6</td><td>34.5</td><td>37.6</td><td>48.1</td><td>55.3</td></tr><tr><td>ROA (pretax %)</td><td>52.5</td><td>84.3</td><td>88.8</td><td>85.9</td><td>89.6</td></tr><tr><td colspan="6">Growth (%)</td></tr><tr><td>Revenue</td><td>47.5</td><td>116.3</td><td>89.6</td><td>64.3</td><td>53.9</td></tr><tr><td>EBITDA</td><td>66.6</td><td>138.8</td><td>92.4</td><td>65.5</td><td>54.6</td></tr><tr><td>Normalised EPS</td><td>72.3</td><td>129.8</td><td>77.6</td><td>62.8</td><td>53.8</td></tr><tr><td>Normalised FDEPS</td><td>72.3</td><td>129.8</td><td>77.6</td><td>62.8</td><td>53.8</td></tr></table>

Source: Company data, NOM estimates

Cashflow statement (TWDmn)

<table><tr><td>Year-end 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>EBITDA</td><td>6,330</td><td>15,114</td><td>29,076</td><td>48,108</td><td>74,380</td></tr><tr><td>Change in working capital</td><td>-3,509</td><td>2,681</td><td>-3,944</td><td>-6,161</td><td>-10,023</td></tr><tr><td>Other operating cashflow</td><td>-513</td><td>-1,610</td><td>-4,734</td><td>-8,544</td><td>-13,513</td></tr><tr><td>Cashflow from operations</td><td>2,308</td><td>16,186</td><td>20,399</td><td>33,404</td><td>50,844</td></tr><tr><td>Capital expenditure</td><td>-114</td><td>-285</td><td>-1,537</td><td>-2,399</td><td>-3,662</td></tr><tr><td>Free cashflow</td><td>2,193</td><td>15,901</td><td>18,862</td><td>31,005</td><td>47,182</td></tr><tr><td>Reduction in investments</td><td>-1,196</td><td>1,218</td><td>-7,847</td><td>0</td><td>0</td></tr><tr><td>Net acquisitions</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Dec in other LT assets</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Inc in other LT liabilities</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Adjustments</td><td>-11</td><td>-364</td><td>331</td><td>0</td><td>0</td></tr><tr><td>CF after investing acts</td><td>986</td><td>16,754</td><td>11,346</td><td>31,005</td><td>47,182</td></tr><tr><td>Cash dividends</td><td>-4,800</td><td>-3,636</td><td>-11,694</td><td>-16,927</td><td>-27,563</td></tr><tr><td>Equity issue</td><td>894</td><td>34,466</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Debt issue</td><td>156</td><td>-152</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Convertible debt issue</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Others</td><td>-5</td><td>-31</td><td>1</td><td>0</td><td>0</td></tr><tr><td>CF from financial acts</td><td>-3,755</td><td>30,648</td><td>-11,692</td><td>-16,927</td><td>-27,563</td></tr><tr><td>Net cashflow</td><td>-2,769</td><td>47,402</td><td>-346</td><td>14,077</td><td>19,619</td></tr><tr><td>Beginning cash</td><td>8,794</td><td>6,025</td><td>53,427</td><td>53,081</td><td>67,159</td></tr><tr><td>Ending cash</td><td>6,025</td><td>53,427</td><td>53,081</td><td>67,159</td><td>86,778</td></tr><tr><td>Ending net debt</td><td>-5,868</td><td>-53,427</td><td>-53,081</td><td>-67,159</td><td>-86,778</td></tr></table>

<table><tr><td colspan="6">Balance sheet (TWDmn)</td></tr><tr><td>As at 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>Cash &amp; equivalents</td><td>6,025</td><td>53,427</td><td>53,081</td><td>67,159</td><td>86,778</td></tr><tr><td>Marketable securities</td><td>2,020</td><td>801</td><td>8,652</td><td>8,652</td><td>8,652</td></tr><tr><td>Accounts receivable</td><td>2,913</td><td>2,935</td><td>7,438</td><td>11,760</td><td>18,614</td></tr><tr><td>Inventories</td><td>8,444</td><td>12,641</td><td>24,597</td><td>38,825</td><td>61,643</td></tr><tr><td>Other current assets</td><td>135</td><td>391</td><td>424</td><td>424</td><td>424</td></tr><tr><td>Total current assets</td><td>19,537</td><td>70,195</td><td>94,191</td><td>126,820</td><td>176,110</td></tr><tr><td>LT investments</td><td>81</td><td>174</td><td>212</td><td>212</td><td>212</td></tr><tr><td>Fixed assets</td><td>1,888</td><td>2,106</td><td>3,427</td><td>5,637</td><td>8,995</td></tr><tr><td>Goodwill</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Other intangible assets</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Other LT assets</td><td>360</td><td>795</td><td>624</td><td>624</td><td>624</td></tr><tr><td>Total assets</td><td>21,866</td><td>73,270</td><td>98,454</td><td>133,292</td><td>185,940</td></tr><tr><td>Short-term debt</td><td>157</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Accounts payable</td><td>3,181</td><td>3,402</td><td>9,484</td><td>14,970</td><td>23,768</td></tr><tr><td>Other current liabilities</td><td>4,691</td><td>11,626</td><td>18,092</td><td>24,996</td><td>35,846</td></tr><tr><td>Total current liabilities</td><td>8,028</td><td>15,028</td><td>27,576</td><td>39,966</td><td>59,614</td></tr><tr><td>Long-term debt</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Convertible debt</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Other LT liabilities</td><td>106</td><td>211</td><td>296</td><td>296</td><td>296</td></tr><tr><td>Total liabilities</td><td>8,134</td><td>15,239</td><td>27,872</td><td>40,262</td><td>59,910</td></tr><tr><td>Minority interest</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Preferred stock</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Common stock</td><td>2,494</td><td>37,979</td><td>37,979</td><td>37,979</td><td>37,979</td></tr><tr><td>Retained earnings</td><td>11,182</td><td>19,908</td><td>32,398</td><td>54,846</td><td>87,845</td></tr><tr><td>Proposed dividends</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Other equity and reserves</td><td>55</td><td>144</td><td>205</td><td>205</td><td>205</td></tr><tr><td>Total shareholders&#x27; equity</td><td>13,732</td><td>58,031</td><td>70,582</td><td>93,030</td><td>126,030</td></tr><tr><td>Total equity &amp; liabilities</td><td>21,866</td><td>73,270</td><td>98,454</td><td>133,292</td><td>185,940</td></tr></table>

<table><tr><td colspan="6">Liquidity (x)</td></tr><tr><td>Current ratio</td><td>2.43</td><td>4.67</td><td>3.42</td><td>3.17</td><td>2.95</td></tr><tr><td>Interest cover</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td colspan="6">Leverage</td></tr><tr><td>Net debt/EBITDA (x)</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td></tr><tr><td>Net debt/equity (%)</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td></tr><tr><td colspan="6">Per share</td></tr><tr><td>Reported EPS (TWD)</td><td>32.95</td><td>75.71</td><td>134.42</td><td>218.87</td><td>336.64</td></tr><tr><td>Norm EPS (TWD)</td><td>32.95</td><td>75.71</td><td>134.42</td><td>218.87</td><td>336.64</td></tr><tr><td>FD norm EPS (TWD)</td><td>32.95</td><td>75.69</td><td>134.40</td><td>218.84</td><td>336.59</td></tr><tr><td>BVPS (TWD)</td><td>84.97</td><td>322.57</td><td>392.33</td><td>517.11</td><td>700.54</td></tr><tr><td>DPS (TWD)</td><td>22.50</td><td>65.00</td><td>94.09</td><td>153.21</td><td>235.65</td></tr><tr><td colspan="6">Activity (days)</td></tr><tr><td>Days receivable</td><td>76.0</td><td>35.3</td><td>33.0</td><td>37.2</td><td>38.3</td></tr><tr><td>Days inventory</td><td>489.8</td><td>292.5</td><td>273.6</td><td>284.9</td><td>293.7</td></tr><tr><td>Days payable</td><td>184.5</td><td>91.3</td><td>94.7</td><td>109.9</td><td>113.2</td></tr><tr><td>Cash cycle</td><td>381.3</td><td>236.4</td><td>211.9</td><td>212.2</td><td>218.7</td></tr></table>

Source: Company data, NOM estimates

## Company profile

Founded in 1999, Hon. Precision (Hon) is a dedicated semiconductor equipment manufacturer focusing on IC test handlers and active thermal control systems (ATC) for IC backend testing. Hon's client base spans across major IC design houses, outsourced semiconductor assembly and test vendors (OSATs), and integrated device manufacturers (IDMs) worldwide.

## Valuation Methodology

Our TP of TWD11,100 is derived from 40x average 2027-28F EPS, at the higher end of historical trading band (19-52x) since IPO. The benchmark of this stock is TAIEX.

## Risks that may impede the achievement of the target price

Downside risks to our call include: 1) CoWoS and backend testing capacity expansion slowdown; 2) slower-than-expected product refresh, platform performance upgrade, or ramp-up by the AI chip end customers; 3) fiercer-than-expected market competition in test handlers; and 4) weaker-than-expected end-market demand, particularly AI servers.

## ESG

Hon. Precision has built its sustainability framework around three pillars: environmental protection based on the TCFD framework to assess energy/greenhouse gas management and water source risks, a "happy workplace" for employees, and social participation. All of these are overseen by a dedicated sustainable development unit that coordinates ESG risk responses and reports regularly to the Board of Directors.

## FT and SLT are Hon's equipment addressable markets

The semiconductor backend processes are punctuated by a few test insertions that sort out defective silicon as early as possible, serving as a gate to ensure output quality – chip probe (CP), final test (FT), burn-in test (BIT), and system-l

[中间内容因长度限制已省略]

 OF THE INVESTMENT, UNDER A SEPARATE ENGAGEMENT, AS THE RECIPIENT DEEMS FIT.

Unless prohibited by the provisions of Regulation S of the 1933 Act, this material is distributed in the US, by NSI, a US-registered broker-dealer, which accepts responsibility for its contents in accordance with the provisions of Rule 15a-6, under the US Securities Exchange Act of 1934. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia (‘Saudi Arabia’) or a ‘Market Counterparty’ or a ‘Professional Client’ (as defined by the Dubai Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page: http://no.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM International (Hong Kong) Ltd., Taipei Branch, Taiwan. All rights reserved.
"""
