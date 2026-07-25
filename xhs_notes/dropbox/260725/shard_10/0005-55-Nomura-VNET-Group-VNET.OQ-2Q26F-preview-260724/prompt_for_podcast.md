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

# 2Q26F preview

Maintain Buy, lower TP to USD13

## 2Q26F preview: revenue +13% y-y with EBITDA +23% y-y

We expect VNET to record 13.2% y-y revenue growth to CNY2.76bn in 2Q26F (+2.4% q-q), including 1.2% y-y growth in retail IDC revenue, 36.4% y-y growth in wholesale IDC revenue, and flat y-y for non-IDC revenue. We estimate \~60MW net addition for utilized wholesale IT power during the quarter, largely flat q-q, which was mainly constrained by the ramp-up of domestic chip capacity, in our view. We expect the company to record 23.1% y-y growth in adjusted EBITDA to CNY902mn in 2Q26F, with 2.6pp y-y expansion in adjusted EBITDA margin to 32.7% (down 0.4pp q-q), as a result of more revenue contribution from the wholesale IDC business.

## Long-term demand intact with solid backlog growth

We expect solid growth in domestic AIDC demand over 2026-28F, supported by robust AI spending by key Chinese CSPs as well as fast development of domestic LLM players. We believe VNET is well positioned for its strong regional footprint in Inner Mongolia, with annual capacity delivery of 400-500GW over 2026-28F. We also expect the pricing for the company's wholesale IDC segment to stay stable-to-rising for 2027-28F, given the surging demand for domestic LLMs and agentic AI applications.

## Maintain Buy with lower TP of USD13

We trim our 2026-28F revenue forecasts by 1.2-2.7%, to reflect a slower-than-expected move-in pace for CSP customers in the near term, leading to a longer revenue recognition period. On the other hand, we lift our 2026-28F forecasts for adjusted EBITDA by 0.6-1.9%, as a result of fast-growing wholesale IDC business and effective cost control. We maintain our Buy rating with lower TP of USD13, based on a DCF valuation model with a WACC of 7.0% (unchanged) and terminal growth rate of 2.0% (unchanged). Our TP implies 12.7x 2027F EV/EBITDA. The stock currently trades at 11x 2027F EV/EBITDA.

<table><tr><td>Year-end 31 Dec</td><td colspan="2">FY25</td><td colspan="2">FY26F</td><td colspan="2">FY27F</td><td colspan="2">FY28F</td></tr><tr><td>Currency (CNY)</td><td>Actual</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td></td></tr><tr><td>Revenue (mn)</td><td>9,949</td><td>11,697</td><td>11,556</td><td>14,740</td><td>14,385</td><td>18,522</td><td>18,028</td><td></td></tr><tr><td>Reported net profit (mn)</td><td>-257</td><td>595</td><td>-1,994</td><td>874</td><td>433</td><td>1,552</td><td>707</td><td></td></tr><tr><td>Normalised net profit (mn)</td><td>-257</td><td>595</td><td>-1,994</td><td>874</td><td>433</td><td>1,552</td><td>707</td><td></td></tr><tr><td>FD normalised EPS</td><td>-96.49c</td><td>2.21</td><td>-7.41</td><td>3.25</td><td>1.61</td><td>5.77</td><td>2.63</td><td></td></tr><tr><td>FD norm. EPS growth (%)</td><td>-237.1</td><td>-</td><td>-</td><td>46.9</td><td>-</td><td>77.7</td><td>63.6</td><td></td></tr><tr><td>FD normalised P/E (x)</td><td>-</td><td>-</td><td>-</td><td>-</td><td>34.7</td><td>-</td><td>21.2</td><td></td></tr><tr><td>EV/EBITDA (x)</td><td>12.2</td><td>-</td><td>12.3</td><td>-</td><td>11.1</td><td>-</td><td>9.4</td><td></td></tr><tr><td>Price/book (x)</td><td>2.3</td><td>-</td><td>3.4</td><td>-</td><td>3.1</td><td>-</td><td>2.7</td><td></td></tr><tr><td>Dividend yield (%)</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td></td></tr><tr><td>ROE (%)</td><td>-4.1</td><td>9.1</td><td>-38.1</td><td>12.0</td><td>9.7</td><td>18.2</td><td>14.0</td><td></td></tr><tr><td>Net debt/equity (%)</td><td>232.0</td><td>338.9</td><td>556.1</td><td>379.8</td><td>631.0</td><td>341.2</td><td>624.5</td><td></td></tr></table>

Source: Company data, NOM estimates

Rating Remains Buy

Target price
Reduced from USD 14.10
USD 13.00

Closing price 23 July 2026 USD 7.77

<table><tr><td>Implied upside</td><td>+67.3%</td></tr></table>

<table><tr><td>Market Cap (USD mn)</td><td>2,212.1</td></tr><tr><td>ADT (USD mn)</td><td>66.0</td></tr></table>

## Relative performance chart

![](images/8a323c7df4e75fbe48aa6918dcf4ce9a6faeb8b6af8bb9b9320eb93c630a4d72.jpg)  
Source: LSEG, NOM

## Research Analysts

China Technology

Ethan Zhang - NIHK

ethan.zhang@NOM.com

+852 2252 2157

Bing Duan - NIHK
bing.duan1@NOM.com
+852 2252 2141

## Key data on VNET Group

Cashflow statement (CNYmn)

<table><tr><td>Performance(%)</td><td>1M</td><td>3M</td><td>12M</td><td></td><td></td></tr><tr><td>Absolute (USD)</td><td>-7.1</td><td>-12.1</td><td>-11.1</td><td>M cap (USDmn)</td><td>2,212.1</td></tr><tr><td>Absolute (USD)</td><td>-7.1</td><td>-12.1</td><td>-11.1</td><td>Free float (%)</td><td>26.1</td></tr><tr><td>Rel to NASDAQ COMPOSITE</td><td>-5.3</td><td>-15.0</td><td>-30.7</td><td>3-mth ADT (USDmn)</td><td>66.0</td></tr></table>

<table><tr><td colspan="6">Income statement (CNYmn)</td></tr><tr><td>Year-end 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>Revenue</td><td>8,259</td><td>9,949</td><td>11,556</td><td>14,385</td><td>18,028</td></tr><tr><td>Cost of goods sold</td><td>-6,427</td><td>-7,757</td><td>-8,928</td><td>-11,042</td><td>-13,658</td></tr><tr><td>Gross profit</td><td>1,832</td><td>2,192</td><td>2,628</td><td>3,343</td><td>4,370</td></tr><tr><td>SG&amp;A</td><td>-1,163</td><td>-1,412</td><td>-1,459</td><td>-1,682</td><td>-2,090</td></tr><tr><td>Employee share expense</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Operating profit</td><td>669</td><td>780</td><td>1,168</td><td>1,662</td><td>2,281</td></tr><tr><td>EBITDA</td><td>2,276</td><td>2,706</td><td>3,604</td><td>4,598</td><td>5,871</td></tr><tr><td>Depreciation</td><td>-1,503</td><td>-1,822</td><td>-2,332</td><td>-2,878</td><td>-3,532</td></tr><tr><td>Amortisation</td><td>-104</td><td>-104</td><td>-104</td><td>-58</td><td>-58</td></tr><tr><td>EBIT</td><td>669</td><td>780</td><td>1,168</td><td>1,662</td><td>2,281</td></tr><tr><td>Net interest expense</td><td>-373</td><td>-561</td><td>-734</td><td>-983</td><td>-1,171</td></tr><tr><td>Associates &amp; JCEs</td><td>8</td><td>7</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Other income</td><td>178</td><td>198</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Earnings before tax</td><td>483</td><td>424</td><td>434</td><td>678</td><td>1,110</td></tr><tr><td>Income tax</td><td>-234</td><td>-558</td><td>-565</td><td>-102</td><td>-166</td></tr><tr><td>Net profit after tax</td><td>248</td><td>-133</td><td>-130</td><td>577</td><td>943</td></tr><tr><td>Minority interests</td><td>-65</td><td>-123</td><td>-1,863</td><td>-144</td><td>-236</td></tr><tr><td>Other items</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Preferred dividends</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Normalised NPAT</td><td>183</td><td>-257</td><td>-1,994</td><td>433</td><td>707</td></tr><tr><td>Extraordinary items</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Reported NPAT</td><td>183</td><td>-257</td><td>-1,994</td><td>433</td><td>707</td></tr><tr><td>Dividends</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Transfer to reserves</td><td>183</td><td>-257</td><td>-1,994</td><td>433</td><td>707</td></tr><tr><td>Valuations and ratios</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Reported P/E (x)</td><td>79.5</td><td>-</td><td>-</td><td>34.7</td><td>21.2</td></tr><tr><td>Normalised P/E (x)</td><td>79.5</td><td>-57.9</td><td>-7.5</td><td>34.7</td><td>21.2</td></tr><tr><td>FD normalised P/E (x)</td><td>79.5</td><td>-</td><td>-</td><td>34.7</td><td>21.2</td></tr><tr><td>Dividend yield (%)</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Price/cashflow (x)</td><td>7.3</td><td>7.7</td><td>6.4</td><td>4.8</td><td>3.7</td></tr><tr><td>Price/book (x)</td><td>2.3</td><td>2.3</td><td>3.4</td><td>3.1</td><td>2.7</td></tr><tr><td>EV/EBITDA (x)</td><td>11.6</td><td>12.2</td><td>12.3</td><td>11.1</td><td>9.4</td></tr><tr><td>EV/EBIT (x)</td><td>39.1</td><td>42.1</td><td>38.1</td><td>30.6</td><td>24.3</td></tr><tr><td>Gross margin (%)</td><td>22.2</td><td>22.0</td><td>22.7</td><td>23.2</td><td>24.2</td></tr><tr><td>EBITDA margin (%)</td><td>27.6</td><td>27.2</td><td>31.2</td><td>32.0</td><td>32.6</td></tr><tr><td>EBIT margin (%)</td><td>8.1</td><td>7.8</td><td>10.1</td><td>11.6</td><td>12.7</td></tr><tr><td>Net margin (%)</td><td>2.2</td><td>-2.6</td><td>-17.3</td><td>3.0</td><td>3.9</td></tr><tr><td>Effective tax rate (%)</td><td>48.5</td><td>131.5</td><td>130.0</td><td>15.0</td><td>15.0</td></tr><tr><td>Dividend payout (%)</td><td>0.0</td><td>-</td><td>-</td><td>0.0</td><td>0.0</td></tr><tr><td>ROE (%)</td><td>3.0</td><td>-4.1</td><td>-38.1</td><td>9.7</td><td>14.0</td></tr><tr><td>ROA (pretax %)</td><td>2.3</td><td>2.3</td><td>2.7</td><td>3.2</td><td>3.9</td></tr><tr><td>Growth (%)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Revenue</td><td>11.4</td><td>20.5</td><td>16.1</td><td>24.5</td><td>25.3</td></tr><tr><td>EBITDA</td><td></td><td>18.9</td><td>33.2</td><td>27.6</td><td>27.7</td></tr><tr><td>Normalised EPS</td><td></td><td>-237.1</td><td>-</td><td>-</td><td>63.6</td></tr><tr><td>Normalised FDEPS</td><td></td><td>-237.1</td><td>-</td><td>-</td><td>63.6</td></tr></table>

Source: Company data, NOM estimates

<table><tr><td>Year-end 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>EBITDA</td><td>2,276</td><td>2,706</td><td>3,604</td><td>4,598</td><td>5,871</td></tr><tr><td>Change in working capital</td><td>3,111</td><td>1,281</td><td>32</td><td>-381</td><td>-505</td></tr><tr><td>Other operating cashflow</td><td>-3,381</td><td>-2,068</td><td>-1,279</td><td>-1,065</td><td>-1,318</td></tr><tr><td>Cashflow from operations</td><td>2,005</td><td>1,919</td><td>2,357</td><td>3,152</td><td>4,049</td></tr><tr><td>Capital expenditure</td><td>-4,924</td><td>-7,657</td><td>-11,350</td><td>-9,000</td><td>-8,100</td></tr><tr><td>Free cashflow</td><td>-2,918</td><td>-5,738</td><td>-8,993</td><td>-5,848</td><td>-4,051</td></tr><tr><td>Reduction in investments</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Net acquisitions</td><td>205</td><td>707</td><td>-187</td><td>-187</td><td>-187</td></tr><tr><td>Dec in other LT assets</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Inc in other LT liabilities</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Adjustments</td><td>328</td><td>-1,062</td><td>0</td><td>0</td><td>0</td></tr><tr><td>CF after investing acts</td><td>-2,385</td><td>-6,093</td><td>-9,180</td><td>-6,035</td><td>-4,238</td></tr><tr><td>Cash dividends</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Equity issue</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Debt issue</td><td>2,751</td><td>4,834</td><td>7,000</td><td>5,000</td><td>5,000</td></tr><tr><td>Convertible debt issue</td><td>-4,262</td><td>3,085</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Others</td><td>3,145</td><td>2,206</td><td>0</td><td>0</td><td>0</td></tr><tr><td>CF from financial acts</td><td>1,634</td><td>10,124</td><td>7,000</td><td>5,000</td><td>5,000</td></tr><tr><td>Net cashflow</td><td>-751</td><td>4,031</td><td>-2,180</td><td>-1,035</td><td>762</td></tr><tr><td>Beginning cash</td><td>2,244</td><td>1,492</td><td>5,524</td><td>3,343</td><td>2,308</td></tr><tr><td>Ending cash</td><td>1,492</td><td>5,524</td><td>3,343</td><td>2,308</td><td>3,070</td></tr><tr><td>Ending net debt</td><td>10,182</td><td>14,426</td><td>23,607</td><td>29,642</td><td>33,880</td></tr><tr><td>Balance sheet (CNYmn)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>As at 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>Cash &amp; equivalents</td><td>1,492</td><td>5,524</td><td>3,343</td><td>2,308</td><td>3,070</td></tr><tr><td>Marketable securities</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Accounts receivable</td><td>1,656</td><td>2,222</td><td>2,284</td><td>2,863</td><td>3,612</td></tr><tr><td>Inventories</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Other current assets</td><td>3,672</td><td>3,706</td><td>3,706</td><td>3,706</td><td>3,706</td></tr><tr><td>Total current assets</td><td>6,820</td><td>11,452</td><td>9,333</td><td>8,877</td><td>10,388</td></tr><tr><td>LT investments</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Fixed assets</td><td>17,217</td><td>22,776</td><td>31,794</td><td>37,915</td><td>42,483</td></tr><tr><td>Goodwill</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Other intangible assets</td><td>1,404</td><td>2,005</td><td>2,096</td><td>2,233</td><td>2,370</td></tr><tr><td>Other LT assets</td><td>6,916</td><td>8,362</td><td>8,354</td><td>8,346</td><td>8,338</td></tr><tr><td>Total assets</td><td>32,357</td><td>44,594</td><td>51,577</td><td>57,372</td><td>63,580</td></tr><tr><td>Short-term debt</td><td>2,009</td><td>3,232</td><td>3,232</td><td>3,232</td><td>3,232</td></tr><tr><td>Accounts payable</td><td>709</td><td>742</td><td>835</td><td>1,033</td><td>1,278</td></tr><tr><td>Other current liabilities</td><td>6,625</td><td>8,474</td><td>8,474</td><td>8,474</td><td>8,474</td></tr><tr><td>Total current liabilities</td><td>9,343</td><td>12,447</td><td>12,540</td><td>12,738</td><td>12,983</td></tr><tr><td>Long-term debt</td><td>7,767</td><td>11,580</td><td>18,580</td><td>23,580</td><td>28,580</td></tr><tr><td>Convertible debt</td><td>1,898</td><td>5,139</td><td>5,139</td><td>5,139</td><td>5,139</td></tr><tr><td>Other LT liabilities</td><td>6,428</td><td>6,864</td><td>6,864</td><td>6,864</td><td>6,864</td></tr><tr><td>Total liabilities</td><td>25,436</td><td>36,030</td><td>43,123</td><td>48,321</td><td>53,565</td></tr><tr><td>Minority interest</td><td>555</td><td>2,346</td><td>4,209</td><td>4,353</td><td>4,589</td></tr><tr><td>Preferred stock</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Common stock</td><td>17,299</td><td>17,360</td><td>17,380</td><td>17,400</td><td>17,420</td></tr><tr><td>Retained earnings</td><td>-10,860</td><td>-11,126</td><td>-13,119</td><td>-12,687</td><td>-11,979</td></tr><tr><td>Proposed dividends</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other equity and reserves</td><td>-73</td><td>-16</td><td>-16</td><td>-16</td><td>-16</td></tr><tr><td>Total shareholders&#x27; equity</td><td>6,366</td><td>6,218</td><td>4,245</td><td>4,697</td><td>5,425</td></tr><tr><td>Total equity &amp; liabilities</td><td>32,357</td><td>44,594</td><td>51,577</td><td>57,371</td><td>63,579</td></tr><tr><td>Liquidity (x)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Current ratio</td><td>0.73</td><td>0.92</td><td>0.74</td><td>0.70</td><td>0.80</td></tr><tr><td>Interest cover</td><td>1.8</td><td>1.4</td><td>1.6</td><td>1.7</td><td>1.9</td></tr><tr><td>Leverage</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Net debt/EBITDA (x)</td><td>4.47</td><td>5.33</td><td>6.55</td><td>6.45</td><td>5.77</td></tr><tr><td>Net debt/equity (%)</td><td>159.9</td><td>232.0</td><td>556.1</td><td>631.0</td><td>624.5</td></tr><tr><td>Per share</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Reported EPS (CNY)</td><td>70.38c</td><td>-96.49c</td><td>-7.41</td><td>1.61</td><td>2.63</td></tr><tr><td>Norm EPS (CNY)</td><td>70.38c</td><td>-96.49c</td><td>-7.41</td><td>1.61</td><td>2.63</td></tr><tr><td>FD norm EPS (CNY)</td><td>70.38c</td><td>-96.49c</td><td>-7.41</td><td>1.61</td><td>2.63</td></tr><tr><td>BVPS (CNY)</td><td>24.46</td><td>23.37</td><td>15.78</td><td>17.46</td><td>20.16</td></tr><tr><td>DPS (CNY)</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>Activity (days)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Days receivable</td><td>74.5</td><td>71.1</td><td>71.2</td><td>65.3</td><td>65.7</td></tr><tr><td>Days inventory</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td></td></tr><tr><td>Days payable</td><td>39.9</td><td>34.1</td><td>32.2</td><td>30.9</td><td>31.0</td></tr><tr><td>Cash cycle</td><td>34.6</td><td>37.0</td><td>38.9</td><td>34.4</td><td>34.8</td></tr></table>

Source: Company data, NOM estimates

## Company profile

VNET develops and operates internet data centers (IDCs) in China. The company provides colocation, managed hosting and consulting services to cloud services providers, internet companies, financial institutions and other large domestic private sector or multinational corporations.

## Valuation Methodology

Our target price of USD13.00 is based on a DCF valuation model. We assume a WACC of 7.0% and terminal growth rate of 2.0%. Cash flows are discounted back to end-2026F. Our TP implies 12.7x 2027F EV/EBITDA. The benchmark index is NASDAQ.

Risks that may impede the achievement of the target price

Downside risks include: (1) slower-than-expected ramp-up of utilization rates for newly-built data centers; and (2) faster-than-expected decline in MRR on intensified market competition.

## ESG

VNET has been focusing on building IDCs with industry-leading standards to maximize the energy utilization. The company also targets to increase the usage of renewable energy to power its data centers.

Fig. 1: VNET – 2Q26F earnings preview

<table><tr><td rowspan="2" colspan="2">(CNY mn)</td><td rowspan="2">1Q25Actual</td><td rowspan="2">2Q25Actual</td><td rowspan="2">3Q25Actual</td><td rowspan="2">4Q25Actual</td><td rowspan="2">1Q26Actual</td><td rowspan="2">2Q26FForecast</td><td rowspan="2">3Q26FForecast</td><td rowspan="2">4Q26FForecast</td><td colspan="2">% change</td></tr><tr><td>y-y</td><td>q-q</td></tr><tr><td>Net revenue</td><td></td><td>2,246</td><td>2,434</td><td>2,582</td><td>2,687</td><td>2,691</td><td>2,757</td><td>2,901</td><td>3,207</td><td>13.2%</td><td>2.4%</td></tr><tr><td></td><td>y-y</td><td>18.3%</td><td>22.1%</td><td>21.7%</td><td>19.6%</td><td>19.8%</td><td>13.2%</td><td>12.4%</td><td>19.3%</td><td></td><td></td></tr><tr><td>COGS</td><td></td><td>(1,681)</td><td>(1,886)</td><td>(2,043)</td><td>(2,147)</td><td>(2,075)</td><td>(2,159)</td><td>(2,272)</td><td>(2,422)</td><td>14.4%</td><td>4.0%</td></tr><tr><td>Gross Profit</td><td></td><td>565</td><td>548</td><td>539</td><td>540</td><td>616</td><td>598</td><td>629</td><td>785</td><td>9.1%</td><td>-2.9%</td></tr><tr><td></td><td>y-y</td><td>37.6%</td><td>28.9%</td><td>9.6%</td><td>7.0%</td><td>8.9%</td><td>9.1%</td><td>16.7%</td><td>45.2%</td><td></td><td></td></tr><tr><td>Adjusted cash gross profit</td><td></td><td>968</td><td>1,062</td><td>1,051</td><td>1,138</td><td>1,211</td><td>1,180</td><td>1,213</td><td>1,376</td><td>11.1%</td><td>-2.6%</

[中间内容因长度限制已省略]

SUITABILITY OF THE INVESTMENT, UNDER A SEPARATE ENGAGEMENT, AS THE RECIPIENT DEEMS FIT. Unless prohibited by the provisions of Regulation S of the 1933 Act, this material is distributed in the US, by NSI, a US-registered broker-dealer, which accepts responsibility for its contents in accordance with the provisions of Rule 15a-6, under the US Securities Exchange Act of 1934.

The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia (‘Saudi Arabia’) or a ‘Market Counterparty’ or a ‘Professional Client’ (as defined by the Dubai Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
