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

# FCC covered list likely caps US growth

## Grandfathering cushions 2026F, but frozen model pipeline erodes competitiveness into 2027F and beyond

FCC adds foreign-produced inverters to Covered List, effective immediately

The FCC (Federal Communications Commission) Public Safety and Homeland Security Bureau released Public Notice DA 26-786 on 28 July 2026, adding foreign-produced power inverters to the Covered List. The determination defines a power inverter on "two limbs": i) a bi-directional DC/AC conversion device, explicitly including micro-inverters, string, central and hybrid battery-based inverters; and ii) contains components enabling remote communication, control, sensing, data collection or monitoring via Wi-Fi, cellular or Bluetooth. In our view, the product portfolio of Sungrow likely falls within the defined scope, and the explicit naming of hybrid battery-based inverters likely brings storage PCS (power conversion system) into the perimeter. Critically, "foreign-produced" is defined by reference to 48 CFR §25.101(a), the Buy American "domestic end product" test, rather than country-of-origin rules; hence, third-country capacity therefore does not qualify.

Frozen model pipeline near term; SST and margins worth monitoring long term

In the near term, the closure of the new-model certification pathway is one binding constraint, which we expect to erode product competitiveness as the range of inverters ages. In addition, we also see impairment risk to overseas capacity built on a third-country strategy, since such capacity does not satisfy the "Buy America" test and Conditional Approval outcomes remain uncertain. In the long term, we flag classification risk around the EnerNeo SST (solid-state transformer). It is, in our view, an AC-to-DC conversion device that would satisfy both definitional limbs (we also expect the US certification plus grid-interconnection testing to likely extend availability to mid-2028F), would weaken the second-growth-driver narrative. Further, Sungrow's hardware re-sourcing toward non-China components and software and data localization, including US-hosted cloud and source-code audits, should raise costs/expenses, while a stripped-down no-connectivity product variant would impair products competitiveness.

## Maintain Neutral and TP of CNY120; trim 2027/28F EPS

We reiterate our Neutral rating for Sungrow with an unchanged TP of CNY120 to reflect near-term certification and long-term structural margin compression risks. We revise down our 2027/28F EPS to CNY8.78/10.41 from CNY9.13/11.20. Our TP is based on 14x 2027F P/E (previously 16x 2026F P/E), at -0.2x SD of its historical P/E. The stock currently trades at 12x 2027F P/E.

<table><tr><td>Year-end 31 Dec</td><td colspan="2">FY25</td><td colspan="2">FY26F</td><td colspan="2">FY27F</td><td colspan="2">FY28F</td></tr><tr><td>Currency (CNY)</td><td>Actual</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td></td></tr><tr><td>Revenue (mn)</td><td>89,184</td><td>106,417</td><td>103,136</td><td>128,480</td><td>125,455</td><td>156,765</td><td>152,317</td><td></td></tr><tr><td>Reported net profit (mn)</td><td>13,461</td><td>15,083</td><td>15,030</td><td>18,924</td><td>18,201</td><td>23,222</td><td>21,572</td><td></td></tr><tr><td>Normalised net profit (mn)</td><td>13,461</td><td>15,083</td><td>15,030</td><td>18,924</td><td>18,201</td><td>23,222</td><td>21,572</td><td></td></tr><tr><td>FD normalised EPS</td><td>6.49</td><td>7.28</td><td>7.25</td><td>9.13</td><td>8.78</td><td>11.20</td><td>10.41</td><td></td></tr><tr><td>FD norm. EPS growth (%)</td><td>22.0</td><td>12.0</td><td>11.7</td><td>25.5</td><td>21.1</td><td>22.7</td><td>18.5</td><td></td></tr><tr><td>FD normalised P/E (x)</td><td>16.4</td><td>-</td><td>14.7</td><td>-</td><td>12.1</td><td>-</td><td>10.2</td><td></td></tr><tr><td>EV/EBITDA (x)</td><td>11.1</td><td>-</td><td>9.5</td><td>-</td><td>7.2</td><td>-</td><td>5.4</td><td></td></tr><tr><td>Price/book (x)</td><td>4.4</td><td>-</td><td>3.4</td><td>-</td><td>2.6</td><td>-</td><td>2.0</td><td></td></tr><tr><td>Dividend yield (%)</td><td>1.5</td><td>-</td><td>1.7</td><td>-</td><td>2.1</td><td>-</td><td>2.4</td><td></td></tr><tr><td>ROE (%)</td><td>29.9</td><td>26.1</td><td>26.1</td><td>25.1</td><td>24.2</td><td>23.6</td><td>22.4</td><td></td></tr><tr><td>Net debt/equity (%)</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td></td></tr></table>

Source: Company data, NOM estimates

<table><tr><td>Rating Remains</td><td>Neutral</td></tr><tr><td>Target price Remains</td><td>CNY 120.00</td></tr><tr><td>Closing price 29 July 2026</td><td>CNY 106.55</td></tr><tr><td>Implied upside</td><td>+12.6%</td></tr><tr><td>Market Cap (USD mn)</td><td>32,631.8</td></tr><tr><td>ADT (USD mn)</td><td>1,629.4</td></tr></table>

## Relative performance chart

![](images/d1b46fd0fb7fd5e8acfdcb303ea780217db99aee7e4db5bb7d8cd6bee0666d79.jpg)  
Source: LSEG, NOM

## Research Analysts

Advanced Manufacturing

Frank Fan - NIHK

frank.fan@NOM.com

+852 2252 2195

Donnie Teng - NIHK
donnie.teng@NOM.com
+852 2252 1439

## Key data on Sungrow Power Supply

<table><tr><td>Performance(%)</td><td>1M</td><td>3M</td><td>12M</td><td></td><td></td><td></td></tr><tr><td>Absolute (CNY)</td><td>-31.5</td><td>-22.8</td><td>41.2</td><td colspan="2">M cap (USDmn)</td><td>32,631.8</td></tr><tr><td>Absolute (USD)</td><td>-31.3</td><td>-22.1</td><td>49.7</td><td colspan="2">Free float (%)</td><td>61.0</td></tr><tr><td>Rel to CSI 300</td><td>-24.3</td><td>-17.8</td><td>31.2</td><td colspan="2">3-mth ADT (USDmn)</td><td>1,629.4</td></tr><tr><td colspan="7">Income statement (CNYmn)</td></tr><tr><td>Year-end 31 Dec</td><td></td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>Revenue</td><td></td><td>77,857</td><td>89,184</td><td>103,136</td><td>125,455</td><td>152,317</td></tr><tr><td>Cost of goods sold</td><td></td><td>-54,545</td><td>-60,795</td><td>-72,344</td><td>-88,576</td><td>-108,621</td></tr><tr><td>Gross profit</td><td></td><td>23,312</td><td>28,389</td><td>30,791</td><td>36,879</td><td>43,696</td></tr><tr><td>SG&amp;A</td><td></td><td>-8,528</td><td>-11,230</td><td>-12,715</td><td>-15,066</td><td>-17,835</td></tr><tr><td colspan="7">Employee share expense</td></tr><tr><td>Operating profit</td><td></td><td>14,784</td><td>17,159</td><td>18,076</td><td>21,812</td><td>25,860</td></tr><tr><td>EBITDA</td><td></td><td>15,706</td><td>18,414</td><td>19,389</td><td>23,184</td><td>27,295</td></tr><tr><td>Depreciation</td><td></td><td>-783</td><td>-1,112</td><td>-1,168</td><td>-1,226</td><td>-1,288</td></tr><tr><td>Amortisation</td><td></td><td>-138</td><td>-143</td><td>-144</td><td>-146</td><td>-147</td></tr><tr><td>EBIT</td><td></td><td>14,784</td><td>17,159</td><td>18,076</td><td>21,812</td><td>25,860</td></tr><tr><td>Net interest expense</td><td></td><td>-290</td><td>-40</td><td>-651</td><td>-459</td><td>-560</td></tr><tr><td colspan="7">Associates &amp; JCEs</td></tr><tr><td>Other income</td><td></td><td>-950</td><td>-859</td><td>307</td><td>187</td><td>229</td></tr><tr><td>Earnings before tax</td><td></td><td>13,544</td><td>16,260</td><td>17,733</td><td>21,540</td><td>25,529</td></tr><tr><td>Income tax</td><td></td><td>-2,280</td><td>-2,727</td><td>-2,673</td><td>-3,231</td><td>-3,829</td></tr><tr><td>Net profit after tax</td><td></td><td>11,264</td><td>13,533</td><td>15,060</td><td>18,309</td><td>21,700</td></tr><tr><td>Minority interests</td><td></td><td>-228</td><td>-72</td><td>-30</td><td>-108</td><td>-128</td></tr><tr><td colspan="7">Other items</td></tr><tr><td colspan="7">Preferred dividends</td></tr><tr><td>Normalised NPAT</td><td></td><td>11,036</td><td>13,461</td><td>15,030</td><td>18,201</td><td>21,572</td></tr><tr><td colspan="7">Extraordinary items</td></tr><tr><td>Reported NPAT</td><td></td><td>11,036</td><td>13,461</td><td>15,030</td><td>18,201</td><td>21,572</td></tr><tr><td>Dividends</td><td></td><td>-2,217</td><td>-3,367</td><td>-3,757</td><td>-4,550</td><td>-5,393</td></tr><tr><td>Transfer to reserves</td><td></td><td>8,820</td><td>10,095</td><td>11,272</td><td>13,651</td><td>16,179</td></tr><tr><td colspan="7">Valuations and ratios</td></tr><tr><td>Reported P/E (x)</td><td></td><td>20.0</td><td>16.4</td><td>14.7</td><td>12.1</td><td>10.2</td></tr><tr><td>Normalised P/E (x)</td><td></td><td>20.0</td><td>16.4</td><td>14.7</td><td>12.1</td><td>10.2</td></tr><tr><td>FD normalised P/E (x)</td><td></td><td>20.0</td><td>16.4</td><td>14.7</td><td>12.1</td><td>10.2</td></tr><tr><td>Dividend yield (%)</td><td></td><td>1.0</td><td>1.5</td><td>1.7</td><td>2.1</td><td>2.4</td></tr><tr><td>Price/cashflow (x)</td><td></td><td>18.3</td><td>13.1</td><td>13.4</td><td>10.1</td><td>8.5</td></tr><tr><td>Price/book (x)</td><td></td><td>5.5</td><td>4.4</td><td>3.4</td><td>2.6</td><td>2.0</td></tr><tr><td>EV/EBITDA (x)</td><td></td><td>13.4</td><td>11.1</td><td>9.5</td><td>7.2</td><td>5.4</td></tr><tr><td>EV/EBIT (x)</td><td></td><td>14.2</td><td>11.9</td><td>10.2</td><td>7.7</td><td>5.7</td></tr><tr><td>Gross margin (%)</td><td></td><td>29.9</td><td>31.8</td><td>29.9</td><td>29.4</td><td>28.7</td></tr><tr><td>EBITDA margin (%)</td><td></td><td>20.2</td><td>20.6</td><td>18.8</td><td>18.5</td><td>17.9</td></tr><tr><td>EBIT margin (%)</td><td></td><td>19.0</td><td>19.2</td><td>17.5</td><td>17.4</td><td>17.0</td></tr><tr><td>Net margin (%)</td><td></td><td>14.2</td><td>15.1</td><td>14.6</td><td>14.5</td><td>14.2</td></tr><tr><td>Effective tax rate (%)</td><td></td><td>16.8</td><td>16.8</td><td>15.1</td><td>15.0</td><td>15.0</td></tr><tr><td>Dividend payout (%)</td><td></td><td>20.1</td><td>25.0</td><td>25.0</td><td>25.0</td><td>25.0</td></tr><tr><td>ROE (%)</td><td></td><td>31.7</td><td>29.9</td><td>26.1</td><td>24.2</td><td>22.4</td></tr><tr><td>ROA (pretax %)</td><td></td><td>18.5</td><td>18.0</td><td>17.4</td><td>17.6</td><td>17.6</td></tr><tr><td colspan="7">Growth (%)</td></tr><tr><td>Revenue</td><td></td><td>7.8</td><td>14.5</td><td>15.6</td><td>21.6</td><td>21.4</td></tr><tr><td>EBITDA</td><td></td><td>18.9</td><td>17.2</td><td>5.3</td><td>19.6</td><td>17.7</td></tr><tr><td>Normalised EPS</td><td></td><td>-16.4</td><td>22.0</td><td>11.7</td><td>21.1</td><td>18.5</td></tr><tr><td>Normalised FDEPS</td><td></td><td>-16.4</td><td>22.0</td><td>11.7</td><td>21.1</td><td>18.5</td></tr></table>

Source: Company data, NOM estimates

Cashflow statement (CNYmn)

<table><tr><td colspan="6">Cashflow statement (CNYmn)</td></tr><tr><td>Year-end 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>EBITDA</td><td>15,706</td><td>18,414</td><td>19,389</td><td>23,184</td><td>27,295</td></tr><tr><td>Change in working capital</td><td>-6,009</td><td>1,473</td><td>5,655</td><td>-1,022</td><td>-2,144</td></tr><tr><td>Other operating cashflow</td><td>2,372</td><td>-2,969</td><td>-8,549</td><td>-321</td><td>736</td></tr><tr><td>Cashflow from operations</td><td>12,068</td><td>16,918</td><td>16,495</td><td>21,841</td><td>25,887</td></tr><tr><td>Capital expenditure</td><td>-2,786</td><td>-3,008</td><td>-3,720</td><td>-4,391</td><td>-5,331</td></tr><tr><td>Free cashflow</td><td>9,282</td><td>13,910</td><td>12,775</td><td>17,451</td><td>20,556</td></tr><tr><td>Reduction in investments</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>Net acquisitions</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Dec in other LT assets</td><td>-810</td><td>-899</td><td>-738</td><td>-798</td><td></td></tr><tr><td>Inc in other LT liabilities</td><td>-1,099</td><td>-689</td><td>0</td><td>0</td><td></td></tr><tr><td>Adjustments</td><td>-8,067</td><td>1,646</td><td>2,242</td><td>738</td><td>798</td></tr><tr><td>CF after investing acts</td><td>1,215</td><td>13,647</td><td>13,429</td><td>17,451</td><td>20,556</td></tr><tr><td>Cash dividends</td><td>-2,217</td><td>-3,367</td><td>-3,757</td><td>-4,550</td><td>-5,393</td></tr><tr><td>Equity issue</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Debt issue</td><td>897</td><td>-2,713</td><td>2,280</td><td>2,280</td><td>2,280</td></tr><tr><td>Convertible debt issue</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Others</td><td>3,637</td><td>-4,536</td><td>6,827</td><td>1,399</td><td>2,242</td></tr><tr><td>CF from financial acts</td><td>2,317</td><td>-10,616</td><td>5,350</td><td>-871</td><td>-871</td></tr><tr><td>Net cashflow</td><td>3,532</td><td>3,031</td><td>18,779</td><td>16,579</td><td>19,684</td></tr><tr><td>Beginning cash</td><td>16,267</td><td>19,799</td><td>22,831</td><td>41,610</td><td>58,189</td></tr><tr><td>Ending cash</td><td>19,799</td><td>22,831</td><td>41,610</td><td>58,189</td><td>77,874</td></tr><tr><td>Ending net debt</td><td>-10,722</td><td>-17,343</td><td>-36,248</td><td>-52,828</td><td>-72,512</td></tr><tr><td colspan="6">Balance sheet (CNYmn)</td></tr><tr><td>As at 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>Cash &amp; equivalents</td><td>19,799</td><td>22,831</td><td>41,610</td><td>58,189</td><td>77,874</td></tr><tr><td>Marketable securities</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Accounts receivable</td><td>28,486</td><td>24,733</td><td>34,468</td><td>42,517</td><td>52,269</td></tr><tr><td>Inventories</td><td>29,028</td><td>27,255</td><td>36,918</td><td>48,585</td><td>59,988</td></tr><tr><td>Other current assets</td><td>17,836</td><td>20,609</td><td>16,038</td><td>17,360</td><td>18,791</td></tr><tr><td>Total current assets</td><td>95,149</td><td>95,428</td><td>129,034</td><td>166,652</td><td>208,922</td></tr><tr><td>LT investments</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Fixed assets</td><td>11,267</td><td>13,674</td><td>14,538</td><td>15,293</td><td>16,187</td></tr><tr><td>Goodwill</td><td>297</td><td>297</td><td>297</td><td>297</td><td>297</td></tr><tr><td>Other intangible assets</td><td>1,122</td><td>1,231</td><td>1,295</td><td>1,321</td><td>1,348</td></tr><tr><td>Other LT assets</td><td>7,239</td><td>8,049</td><td>8,948</td><td>9,685</td><td>10,483</td></tr><tr><td>Total assets</td><td>115,074</td><td>118,679</td><td>154,111</td><td>193,248</td><td>237,237</td></tr><tr><td>Short-term debt</td><td>4,214</td><td>2,422</td><td>2,279</td><td>2,279</td><td>2,279</td></tr><tr><td>Accounts payable</td><td>36,757</td><td>36,636</td><td>50,762</td><td>66,805</td><td>82,484</td></tr><tr><td>Other current liabilities</td><td>19,327</td><td>18,169</td><td>24,525</td><td>28,498</td><td>33,261</td></tr><tr><td>Total current liabilities</td><td>60,298</td><td>57,228</td><td>77,565</td><td>97,582</td><td>118,024</td></tr><tr><td>Long-term debt</td><td>4,863</td><td>3,065</td><td>3,083</td><td>3,083</td><td>3,083</td></tr><tr><td>Convertible debt</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other LT liabilities</td><td>9,714</td><td>8,615</td><td>7,926</td><td>7,926</td><td>7,926</td></tr><tr><td>Total liabilities</td><td>74,875</td><td>68,908</td><td>88,574</td><td>108,591</td><td>129,033</td></tr><tr><td>Minority interest</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Preferred stock</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Common stock</td><td>2,073</td><td>2,073</td><td>2,073</td><td>2,073</td><td>2,073</td></tr><tr><td>Retained earnings</td><td>28,346</td><td>37,640</td><td>52,670</td><td>70,871</td><td>92,444</td></tr><tr><td>Proposed dividends</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other equity and reserves</td><td>9,779</td><td>10,058</td><td>10,793</td><td>11,712</td><td>13,688</td></tr><tr><td>Total shareholders&#x27; equity</td><td>40,199</td><td>49,772</td><td>65,537</td><td>84,657</td><td>108,205</td></tr><tr><td>Total equity &amp; liabilities</td><td>115,074</td><td>118,679</td><td>154,111</td><td>193,248</td><td>237,237</td></tr><tr><td>Liquidity (x)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Current ratio</td><td>1.58</td><td>1.67</td><td>1.66</td><td>1.71</td><td>1.77</td></tr><tr><td>Interest cover</td><td>50.9</td><td>433.8</td><td>27.8</td><td>47.5</td><td>46.2</td></tr><tr><td>Leverage</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Net debt/EBITDA (x)</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td></tr><tr><td>Net debt/equity (%)</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td></tr><tr><td>Per share</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Reported EPS (CNY)</td><td>5.32</td><td>6.49</td><td>7.25</td><td>8.78</td><td>10.41</td></tr><tr><td>Norm EPS (CNY)</td><td>5.32</td><td>6.49</td><td>7.25</td><td>8.78</td><td>10.41</td></tr><tr><td>FD norm EPS (CNY)</td><td>5.32</td><td>6.49</td><td>7.25</td><td>8.78</td><td>10.41</td></tr><tr><td>BVPS (CNY)</td><td>19.39</td><td>24.01</td><td>31.61</td><td>40.83</td><td>52.19</td></tr><tr><td>DPS (CNY)</td><td>1.07</td><td>1.62</td><td>1.81</td><td>2.19</td><td>2.60</td></tr><tr><td>Activity (days)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Days receivable</td><td>133.5</td><td>108.9</td><td>104.8</td><td>112.0</td><td>113.9</td></tr><tr><td>Days inventory</td><td>194.2</td><td>169.0</td><td>161.9</td><td>176.2</td><td>182.9</td></tr><tr><td>Days payable</td><td>246.0</td><td>220.3</td><td>220.5</td><td>242.2</td><td>251.5</td></tr><tr><td>Cash cycle</td><td>81.8</td><td>57.5</td><td>46.2</td><td>45.9</td><td>45.3</td></tr></table>

Source: Company data, NOM estimates

## Company profile

Sungrow Power Supply is a top-tier power control system and energy storage vendor in China, with major product being PV inverter, energy storage equipment, and solar EPC.

## Valuation Methodology

We use P/E method to value Sungrow and our TP of CNY120 is based on 14x 2027F P/E, -0.2x SD of its historical average at 17x, which is due to declining gross margins in 2026-28F. The benchmark index is CSI300.

Risks that may impede the achievement of the target price

Upside risks include: 1) faster ESS development in data center clients; 2) better gross margins due to stable battery prices. Downside risks include: 1) policy headwinds for ESS business; 2) softening utility-scale project demand.

## ESG

Sungrow fits the ESG theme since it is one of leading solar inverter companies, helping generate renewable energy with low consumption costs.

Fig. 1: Sungrow – forward P/E band  
![](images/5875b75490f7628e0577aac01bb83c1f221feca29ec19eb3cf1a6fe2286cda56.jpg)  
Source: Bloomberg Finance L.P., N

[中间内容因长度限制已省略]

 SUITABILITY OF THE INVESTMENT, UNDER A SEPARATE ENGAGEMENT, AS THE RECIPIENT DEEMS FIT. Unless prohibited by the provisions of Regulation S of the 1933 Act, this material is distributed in the US, by NSI, a US-registered broker-dealer, which accepts responsibility for its contents in accordance with the provisions of Rule 15a-6, under the US Securities Exchange Act of 1934. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia ('Saudi Arabia') or a 'Market Counterparty' or a 'Professional Client' (as defined by the Dubai Financial Services Authority) in the United Arab Emirates ('UAE') or a 'Market Counterparty' or a 'Business Customer' (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar ('Qatar') by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than 'Authorised Persons', 'Exempt Persons' or 'Institutions' located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
