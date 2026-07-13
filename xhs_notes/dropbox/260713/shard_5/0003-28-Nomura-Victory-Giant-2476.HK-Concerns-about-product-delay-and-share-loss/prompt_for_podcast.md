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

# Concerns about product delay and share loss overdone...

... rubin upgrade, ASIC and optical transceiver PCB are key drivers

Action: Maintain Buy but cut TP to CNY389; implying $94\%$ upside; short-term concerns overdone

Despite recent market concerns about the delay of NVIDIA's (NVDA US, Not rated) Kyber rack, we think the production ramp-up of Rubin GPU in 2H26 would continue to support Victory Giant's (VGT) PCB value content upgrade as well as margin expansion. Although there might be more competition in NVIDIA's Rubin compute tray / HDI (High Density Interconnect) PCB, likely from ZDT (4958 TT, Buy), we think this should be the supply chain diversification efforts of AI customers, amid an extremely under supply situation. Meanwhile, we think VGT remains as the leading supplier of a GPU customer, while its entry into ASIC and optical transceiver customers would drive sustainable growth and more balanced customer exposure in 2H26-2027F. We cut FY26-28F revenue / earnings forecasts by 7-13%/ 7-14% to reflect a likely lower HDI revenue contribution. We maintain our Buy rating with a lower TP of HKD447, based on 27x (unchanged) FY27F EPS of CNY14.41. The stock is currently trading at 14x FY27F EPS.

Market concerns about Kyber / backplane delay and GPU customer's supply chain diversification likely overdone; the company's HDI capacity is still a strategic asset We think VGT's GPU shipments for NVIDIA's Rubin GPU may have already started in mid-2026, and this could ramp up in 2H26F. Despite market concerns about technology issues and huge market share loss, we think the company's existing and potential HDI capacity remain as a strategic asset to secure a lead in this segment, and there are not many challengers in sight due to high technology barriers and material / equipment shortages, in our view. Moreover, we believe not only the GPU customer, but also ASIC customers may start to adopt HDI from 2028F, leading to better demand for the company's HDI products. We expect a $82\%$ revenue CAGR for the HDI segment in FY26-28F, contributing $63\%$ of total revenue in FY28F.

ASIC and optical transceiver help company to diversify its customer portfolio
We think the company has already made good progress in the ASIC customer segment, as well as the 800G / 1.6T transceiver market, which should enjoy strong demand uptick in the next few years. We believe VGT still stands out as one of the leading AI PCB makers, and we estimate a 77% revenue CAGR for the company's AI & HPC (high performance computing) sector over 2026F-28F, contributing 77% of total sales in FY28F.

<table><tr><td>Year-end 31 Dec</td><td colspan="2">FY25</td><td colspan="2">FY26F</td><td colspan="2">FY27F</td><td colspan="2">FY28F</td></tr><tr><td>Currency (CNY)</td><td>Actual</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td></td></tr><tr><td>Revenue (mn)</td><td>19,292</td><td>31,948</td><td>27,850</td><td>52,317</td><td>49,158</td><td>75,880</td><td>70,941</td><td></td></tr><tr><td>Reported net profit (mn)</td><td>4,312</td><td>8,698</td><td>7,497</td><td>15,174</td><td>14,162</td><td>22,509</td><td>20,927</td><td></td></tr><tr><td>Normalised net profit (mn)</td><td>4,312</td><td>8,698</td><td>7,497</td><td>15,174</td><td>14,162</td><td>22,509</td><td>20,927</td><td></td></tr><tr><td>FD normalised EPS</td><td>4.98</td><td>9.39</td><td>8.09</td><td>15.44</td><td>14.41</td><td>22.90</td><td>21.29</td><td></td></tr><tr><td>FD norm. EPS growth (%)</td><td>271.9</td><td>88.6</td><td>62.6</td><td>64.5</td><td>78.1</td><td>48.3</td><td>47.8</td><td></td></tr><tr><td>FD normalised P/E (x)</td><td>39.1</td><td>-</td><td>24.0</td><td>-</td><td>13.5</td><td>-</td><td>9.1</td><td></td></tr><tr><td>EV/EBITDA (x)</td><td>2.9</td><td>-</td><td>0.9</td><td>-</td><td>0.1</td><td>-</td><td>-0.4</td><td></td></tr><tr><td>Price/book (x)</td><td>10.2</td><td>-</td><td>4.6</td><td>-</td><td>3.5</td><td>-</td><td>2.5</td><td></td></tr><tr><td>Dividend yield (%)</td><td>0.2</td><td>-</td><td>0.2</td><td>-</td><td>0.4</td><td>-</td><td>0.7</td><td></td></tr><tr><td>ROE (%)</td><td>33.8</td><td>29.5</td><td>26.0</td><td>30.5</td><td>29.5</td><td>33.2</td><td>32.2</td><td></td></tr><tr><td>Net debt/equity (%)</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td></td></tr></table>

Source: Company data, NOM estimates

Rating Remains Buy

Target price
Reduced from
HKD 479.00
HKD 447.00

Closing price
10 July 2026
HKD 230.20

<table><tr><td>Implied upside</td><td>+94.2%</td></tr></table>

<table><tr><td>Market Cap (USD mn)</td><td>3,236.7</td></tr><tr><td>ADT (USD mn)</td><td>249.6</td></tr></table>

## Relative performance chart

![](images/442f6141df4b6abef6bbca6830dae066ed348a8e03fa76508facd1a3c2368b0e.jpg)  
Source: LSEG, NOM

## Research Analysts

China Technology
Bing Duan - NIHK
bing.duan1@NOM.com
+852 2252 2141

Anne Lee, CFA - NITB
anne.lee@NOM.com
+886(2) 21769966

## Key data on Victory Giant

<table><tr><td>Performance(%)</td><td>1M</td><td>3M</td><td>12M</td><td></td><td></td></tr><tr><td>Absolute (HKD)</td><td>-35.9</td><td></td><td></td><td>M cap (USDmn)</td><td>3,236.7</td></tr><tr><td>Absolute (USD)</td><td>-35.9</td><td></td><td></td><td>Free float (%)</td><td>62.0</td></tr><tr><td>Rel to Hang Seng Index</td><td>-34.9</td><td></td><td></td><td>3-mth ADT (USDmn)</td><td>249.6</td></tr></table>

<table><tr><td colspan="6">Income statement (CNYmn)</td></tr><tr><td>Year-end 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>Revenue</td><td>10,731</td><td>19,292</td><td>27,850</td><td>49,158</td><td>70,941</td></tr><tr><td>Cost of goods sold</td><td>-8,293</td><td>-12,497</td><td>-16,544</td><td>-27,602</td><td>-38,516</td></tr><tr><td>Gross profit</td><td>2,439</td><td>6,795</td><td>11,306</td><td>21,556</td><td>32,425</td></tr><tr><td>SG&amp;A</td><td>-1,013</td><td>-1,631</td><td>-2,370</td><td>-4,700</td><td>-7,530</td></tr><tr><td>Employee share expense</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Operating profit</td><td>1,425</td><td>5,164</td><td>8,936</td><td>16,856</td><td>24,895</td></tr><tr><td>EBITDA</td><td>2,142</td><td>6,047</td><td>10,714</td><td>19,159</td><td>27,370</td></tr><tr><td>Depreciation</td><td>-717</td><td>-883</td><td>-1,778</td><td>-2,303</td><td>-2,475</td></tr><tr><td>Amortisation</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EBIT</td><td>1,425</td><td>5,164</td><td>8,936</td><td>16,856</td><td>24,895</td></tr><tr><td>Net interest expense</td><td>-114</td><td>-142</td><td>-206</td><td>-363</td><td>-524</td></tr><tr><td>Associates &amp; JCEs</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Other income</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Earnings before tax</td><td>1,312</td><td>5,022</td><td>8,730</td><td>16,493</td><td>24,371</td></tr><tr><td>Income tax</td><td>-157</td><td>-710</td><td>-1,234</td><td>-2,331</td><td>-3,444</td></tr><tr><td>Net profit after tax</td><td>1,154</td><td>4,312</td><td>7,497</td><td>14,162</td><td>20,927</td></tr><tr><td>Minority interests</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Other items</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Preferred dividends</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Normalised NPAT</td><td>1,154</td><td>4,312</td><td>7,497</td><td>14,162</td><td>20,927</td></tr><tr><td>Extraordinary items</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Reported NPAT</td><td>1,154</td><td>4,312</td><td>7,497</td><td>14,162</td><td>20,927</td></tr><tr><td>Dividends</td><td>-163</td><td>-258</td><td>-448</td><td>-846</td><td>-1,250</td></tr><tr><td>Transfer to reserves</td><td>991</td><td>4,054</td><td>7,049</td><td>13,316</td><td>19,677</td></tr><tr><td>Valuations and ratios</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Reported P/E (x)</td><td>145.3</td><td>39.1</td><td>24.0</td><td>13.5</td><td>9.1</td></tr><tr><td>Normalised P/E (x)</td><td>145.3</td><td>39.1</td><td>24.0</td><td>13.5</td><td>9.1</td></tr><tr><td>FD normalised P/E (x)</td><td>145.3</td><td>39.1</td><td>24.0</td><td>13.5</td><td>9.1</td></tr><tr><td>Dividend yield (%)</td><td>0.1</td><td>0.2</td><td>0.2</td><td>0.4</td><td>0.7</td></tr><tr><td>Price/cashflow (x)</td><td>81.0</td><td>36.5</td><td>30.3</td><td>10.6</td><td>9.7</td></tr><tr><td>Price/book (x)</td><td>18.8</td><td>10.2</td><td>4.6</td><td>3.5</td><td>2.5</td></tr><tr><td>EV/EBITDA (x)</td><td>8.8</td><td>2.9</td><td>0.9</td><td>0.1</td><td>-0.4</td></tr><tr><td>EV/EBIT (x)</td><td>13.2</td><td>3.5</td><td>1.1</td><td>0.1</td><td>-0.5</td></tr><tr><td>Gross margin (%)</td><td>22.7</td><td>35.2</td><td>40.6</td><td>43.8</td><td>45.7</td></tr><tr><td>EBITDA margin (%)</td><td>20.0</td><td>31.3</td><td>38.5</td><td>39.0</td><td>38.6</td></tr><tr><td>EBIT margin (%)</td><td>13.3</td><td>26.8</td><td>32.1</td><td>34.3</td><td>35.1</td></tr><tr><td>Net margin (%)</td><td>10.8</td><td>22.4</td><td>26.9</td><td>28.8</td><td>29.5</td></tr><tr><td>Effective tax rate (%)</td><td>12.0</td><td>14.1</td><td>14.1</td><td>14.1</td><td>14.1</td></tr><tr><td>Dividend payout (%)</td><td>14.1</td><td>6.0</td><td>6.0</td><td>6.0</td><td>6.0</td></tr><tr><td>ROE (%)</td><td>13.9</td><td>33.8</td><td>26.0</td><td>29.5</td><td>32.2</td></tr><tr><td>ROA (pretax %)</td><td>8.7</td><td>20.9</td><td>22.3</td><td>28.7</td><td>34.5</td></tr><tr><td>Growth (%)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Revenue</td><td>35.3</td><td>79.8</td><td>44.4</td><td>76.5</td><td>44.3</td></tr><tr><td>EBITDA</td><td>41.7</td><td>182.3</td><td>77.2</td><td>78.8</td><td>42.9</td></tr><tr><td>Normalised EPS</td><td>2.2</td><td>271.9</td><td>62.6</td><td>78.1</td><td>47.8</td></tr><tr><td>Normalised FDEPS</td><td>2.2</td><td>271.9</td><td>62.6</td><td>78.1</td><td>47.8</td></tr></table>

Source: Company data, NOM estimates

<table><tr><td colspan="6">Cashflow statement (CNYmn)</td></tr><tr><td>Year-end 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>EBITDA</td><td>2,142</td><td>6,047</td><td>10,714</td><td>19,159</td><td>27,370</td></tr><tr><td>Change in working capital</td><td>184</td><td>2,128</td><td>-3,374</td><td>1,506</td><td>-3,773</td></tr><tr><td>Other operating cashflow</td><td>-255</td><td>-3,555</td><td>-1,399</td><td>-2,654</td><td>-3,928</td></tr><tr><td>Cashflow from operations</td><td>2,071</td><td>4,620</td><td>5,941</td><td>18,011</td><td>19,669</td></tr><tr><td>Capital expenditure</td><td>-1,116</td><td>-6,364</td><td>-15,000</td><td>-10,000</td><td>-5,000</td></tr><tr><td>Free cashflow</td><td>955</td><td>-1,744</td><td>-9,059</td><td>8,011</td><td>14,669</td></tr><tr><td>Reduction in investments</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>Net acquisitions</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Dec in other LT assets</td><td>-5,263</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>Inc in other LT liabilities</td><td>1,869</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>Adjustments</td><td>469</td><td>666</td><td>0</td><td>0</td><td>0</td></tr><tr><td>CF after investing acts</td><td>1,424</td><td>-4,471</td><td>-9,059</td><td>8,011</td><td>14,669</td></tr><tr><td>Cash dividends</td><td>-163</td><td>-258</td><td>-258</td><td>-448</td><td>-846</td></tr><tr><td>Equity issue</td><td>0</td><td>1,876</td><td>17,300</td><td>0</td><td>0</td></tr><tr><td>Debt issue</td><td>-935</td><td>2,119</td><td>2,441</td><td>0</td><td>0</td></tr><tr><td>Convertible debt issue</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Others</td><td>1,186</td><td>2,351</td><td>0</td><td>0</td><td>0</td></tr><tr><td>CF from financial acts</td><td>89</td><td>6,089</td><td>19,483</td><td>-448</td><td>-846</td></tr><tr><td>Net cashflow</td><td>1,513</td><td>1,618</td><td>10,424</td><td>7,563</td><td>13,823</td></tr><tr><td>Beginning cash</td><td>749</td><td>1,662</td><td>3,280</td><td>13,704</td><td>21,267</td></tr><tr><td>Ending cash</td><td>2,262</td><td>3,280</td><td>13,704</td><td>21,267</td><td>35,090</td></tr><tr><td>Ending net debt</td><td>927</td><td>-806</td><td>-8,789</td><td>-16,352</td><td>-30,175</td></tr><tr><td colspan="6">Balance sheet (CNYmn)</td></tr><tr><td>As at 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>Cash &amp; equivalents</td><td>1,662</td><td>3,280</td><td>13,704</td><td>21,267</td><td>35,090</td></tr><tr><td>Marketable securities</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Accounts receivable</td><td>4,272</td><td>6,561</td><td>9,077</td><td>18,525</td><td>21,308</td></tr><tr><td>Inventories</td><td>2,045</td><td>3,162</td><td>3,732</td><td>7,771</td><td>8,280</td></tr><tr><td>Other current assets</td><td>101</td><td>511</td><td>511</td><td>511</td><td>511</td></tr><tr><td>Total current assets</td><td>8,080</td><td>13,514</td><td>27,023</td><td>48,074</td><td>65,189</td></tr><tr><td>LT investments</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Fixed assets</td><td>7,477</td><td>12,876</td><td>26,098</td><td>33,796</td><td>36,321</td></tr><tr><td>Goodwill</td><td>615</td><td>588</td><td>547</td><td>507</td><td>466</td></tr><tr><td>Other intangible assets</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other LT assets</td><td>3,004</td><td>8,267</td><td>8,267</td><td>8,267</td><td>8,267</td></tr><tr><td>Total assets</td><td>19,175</td><td>35,244</td><td>61,935</td><td>90,643</td><td>110,243</td></tr><tr><td>Short-term debt</td><td>1,908</td><td>2,474</td><td>4,915</td><td>4,915</td><td>4,915</td></tr><tr><td>Accounts payable</td><td>5,473</td><td>11,144</td><td>10,855</td><td>25,848</td><td>25,368</td></tr><tr><td>Other current liabilities</td><td>155</td><td>429</td><td>429</td><td>429</td><td>429</td></tr><tr><td>Total current liabilities</td><td>7,537</td><td>14,047</td><td>16,199</td><td>31,192</td><td>30,711</td></tr><tr><td>Long-term debt</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Convertible debt</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other LT liabilities</td><td>2,711</td><td>4,580</td><td>4,580</td><td>4,580</td><td>4,580</td></tr><tr><td>Total liabilities</td><td>10,247</td><td>18,627</td><td>20,779</td><td>35,772</td><td>35,291</td></tr><tr><td>Minority interest</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Preferred stock</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Common stock</td><td>863</td><td>870</td><td>18,170</td><td>18,170</td><td>18,170</td></tr><tr><td>Retained earnings</td><td>8,065</td><td>15,747</td><td>22,986</td><td>36,700</td><td>56,781</td></tr><tr><td>Proposed dividends</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other equity and reserves</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Total shareholders&#x27; equity</td><td>8,928</td><td>16,618</td><td>41,157</td><td>54,871</td><td>74,952</td></tr><tr><td>Total equity &amp; liabilities</td><td>19,175</td><td>35,244</td><td>61,935</td><td>90,643</td><td>110,243</td></tr><tr><td>Liquidity (x)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Current ratio</td><td>1.07</td><td>0.96</td><td>1.67</td><td>1.54</td><td>2.12</td></tr><tr><td>Interest cover</td><td>12.5</td><td>36.2</td><td>43.4</td><td>46.4</td><td>47.5</td></tr><tr><td>Leverage</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Net debt/EBITDA (x)</td><td>0.43</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td></tr><tr><td>Net debt/equity (%)</td><td>10.4</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td></tr><tr><td>Per share</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Reported EPS (CNY)</td><td>1.34</td><td>4.98</td><td>8.09</td><td>14.41</td><td>21.29</td></tr><tr><td>Norm EPS (CNY)</td><td>1.34</td><td>4.98</td><td>8.09</td><td>14.41</td><td>21.29</td></tr><tr><td>FD norm EPS (CNY)</td><td>1.34</td><td>4.98</td><td>8.09</td><td>14.41</td><td>21.29</td></tr><tr><td>BVPS (CNY)</td><td>10.35</td><td>19.09</td><td>41.88</td><td>55.83</td><td>76.26</td></tr><tr><td>DPS (CNY)</td><td>0.19</td><td>0.30</td><td>0.46</td><td>0.86</td><td>1.27</td></tr><tr><td>Activity (days)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Days receivable</td><td>132.5</td><td>102.5</td><td>102.5</td><td>102.5</td><td>102.8</td></tr><tr><td>Days inventory</td><td>75.5</td><td>76.1</td><td>76.1</td><td>76.1</td><td>76.3</td></tr><tr><td>Days payable</td><td>213.3</td><td>242.7</td><td>242.7</td><td>242.7</td><td>243.3</td></tr><tr><td>Cash cycle</td><td>-5.3</td><td>-64.1</td><td>-64.1</td><td>-64.1</td><td>-64.3</td></tr></table>

Source: Company data, NOM estimates

Company profile

VGT is a key player in advanced printed circuit board (PCB) products for AI and high-performance computing.

Valuation Methodology

Our TP of HKD447.00 is based on 27x 2027F EPS of CNY14.41, in line with its A-share historical median P/E. The benchmark index is Hang Seng Index.

Risks that may impede the achievement of the target price

Downside risks: 1) lower-than-expected PCB demand in downstream sectors such as servers and auto electronics; 2) more fierce competition in the high-end PCB market leading to pressure on margins; 3) higher-than-expected raw material cost pressure, and 4) worse-than-expected geopolitical tensions in global AI value chain.

## ESG

VGT is a leading PCB maker, who shares social responsibility by offering PCB products for network hardware such as server and switch. The PCB manufacturing may have impact on the environment while factory automation may help to improve the environmental friendliness.

<table><tr><td>2026F</td><td>2027F</td><td>2028F</td></tr><tr><td>% diff</td><td>% diff</td><td>% diff</td></tr><tr><td>-13%</td><td>-6%</td><td>-7%</td></tr><tr><td>-12%</td><td>-6%</td><td>-6%</td></tr><tr><td>-14%</td><td>-7%</td><td>-7%</td></tr><tr><td>-13%</td><td>-6%</td><td>-7%</td></tr><tr><td>-14%</td><td>-7%</td><td>-7%</td></tr><tr><td>-14%</td><td>-7%</td><td>-7%</td></tr><tr><td>-14%</td><td>-7%</td><td>-7%</td></tr><tr><td>-0.4pp</td><td>-0.2pp</td><td>-0.2pp</td></tr><tr><td>0.0pp</td><td>0.0pp</td><td>0.0pp</td></tr><tr><td>-0.4pp</td><td>-0.2pp</td><td>-0.2pp</td></tr><tr><td>-0.3pp</td><td>-0.2pp</td><td>-0.2pp</td></tr></table>

## Earnings forecasts revisions

We cut FY26-28F revenue forecasts by 7-13% to prim

[中间内容因长度限制已省略]

 AN INDEPENDENT FINANCIAL ADVISER REGARDING THE SUITABILITY OF THE INVESTMENT, UNDER A SEPARATE ENGAGEMENT, AS THE RECIPIENT DEEMS FIT. Unless prohibited by the provisions of Regulation S of the 1933 Act, this material is distributed in the US, by NSI, a US-registered broker-dealer, which accepts responsibility for its contents in accordance with the provisions of Rule 15a-6, under the US Securities Exchange Act of 1934.

The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia ('Saudi Arabia') or a 'Market Counterparty' or a 'Professional Client' (as defined by the Dubai Financial Services Authority) in the United Arab Emirates ('UAE') or a 'Market Counterparty' or a 'Business Customer' (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar ('Qatar') by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, "Offshore Issuers") that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
