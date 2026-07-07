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

# We expect secular growth beyond 2027...

## ...Driven by 2.4T/3.2T transceivers, NPO and CPO

Action: Maintain Buy; raise TP to CNY1,325, implying 20.6% upside

Despite recent share price pull-back in the AI infra sector, we think the fundamental growth driver for InnoLight remains unchanged in FY26-28F: 1) 1.6T and Silicon photonics (SiPh) transceiver upgrade; and 2) NPO (Near-field packaging optics) / CPO (Co-packaged optics) market expansion. Although there are concerns about component shortages, as well as double bookings from hyperscale AI customers, we think high-end optical communication products remain key bottlenecks in the AIDC market. We raise our FY27/28F global shipment forecasts for 800G transceivers to 55mn / 78mn units (from 50mn / 71.5mn), and 1.6T to 71.5mn / 126mn units (from 60mn / 110mn), while we also factor in 2mn / 5mn units of 2.4T in FY27/28F, and 2mn units of 3.2T in 2028F. We expect the company to maintain 30%\~35% market share in the global AIDC transceiver market due to strong R&D and effective supply chain management. We raise our FY27-28F revenue / earnings forecasts by 28-37%/30-38% (Fig. 1) to reflect the strong product upgrade, as well as margin expansion. Hence, we maintain our Buy rating and raise TP to CNY1,325, based on 20x (unchanged) FY27F EPS of CNY66.06, in line with WIND's China A share tech/electronic component sector median P/E. The stock is trading at 16.6x FY27F EPS.

Component shortage to ease in the long-term, while the company's leadership to remain in the high-end transceiver and NPO / CPO markets

Due to the buoyant demand for high-end optical transceivers (especially 1.6T), the entire supply chain is striving to fulfil the end customers' demand, but supply bottlenecks remain in the near-term, from upstream material (i.e. InP wafer), equipment (i.e. MOCVD machine), and components (i.e. 200G EML), owing to yield ramp-up and supply chain disruption, in our view. We estimate 25% / 22% q-q revenue / earnings growth in 2Q26F. However, we think in the long-term (likely from 2028F), the supply shortage will ease owing to increased capacity expansion from dedicated players in China, Japan, and the US. Recently, Nikkei reported that JX Advanced Metals [5016 JP] (Neutral, covered by Daiki Ban) will expand production capacity for indium phosphide (InP) wafer to 7–10x the 26/3 level (see NOM report) in around 5 years. We think InnoLight's leadership in the optical communication market will solidify in the high-end transceiver (2.4T / 3.2T) and NPO / CPO markets, which should lead to sustainable growth from 2028F onwards.

<table><tr><td>Year-end 31 Dec</td><td colspan="2">FY25</td><td colspan="2">FY26F</td><td colspan="2">FY27F</td><td colspan="2">FY28F</td></tr><tr><td>Currency (CNY)</td><td>Actual</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td></td></tr><tr><td>Revenue (mn)</td><td>38,240</td><td>122,105</td><td>122,105</td><td>204,546</td><td>261,031</td><td>271,717</td><td>371,545</td><td></td></tr><tr><td>Reported net profit (mn)</td><td>10,797</td><td>32,433</td><td>33,654</td><td>56,525</td><td>73,396</td><td>75,374</td><td>103,944</td><td></td></tr><tr><td>Normalised net profit (mn)</td><td>10,797</td><td>32,433</td><td>33,654</td><td>56,525</td><td>73,396</td><td>75,374</td><td>103,944</td><td></td></tr><tr><td>FD normalised EPS</td><td>9.72</td><td>29.19</td><td>30.29</td><td>50.87</td><td>66.06</td><td>67.84</td><td>93.55</td><td></td></tr><tr><td>FD norm. EPS growth (%)</td><td>110.7</td><td>200.4</td><td>211.7</td><td>74.3</td><td>118.1</td><td>33.3</td><td>41.6</td><td></td></tr><tr><td>FD normalised P/E (x)</td><td>113.1</td><td>-</td><td>36.3</td><td>-</td><td>16.6</td><td>-</td><td>11.7</td><td></td></tr><tr><td>EV/EBITDA (x)</td><td>83.6</td><td>-</td><td>27.7</td><td>-</td><td>12.4</td><td>-</td><td>8.2</td><td></td></tr><tr><td>Price/book (x)</td><td>41.0</td><td>-</td><td>21.1</td><td>-</td><td>10.2</td><td>-</td><td>5.9</td><td></td></tr><tr><td>Dividend yield (%)</td><td>0.1</td><td>-</td><td>0.5</td><td>-</td><td>1.0</td><td>-</td><td>1.4</td><td></td></tr><tr><td>ROE (%)</td><td>44.2</td><td>74.8</td><td>76.8</td><td>70.2</td><td>82.8</td><td>55.5</td><td>63.8</td><td></td></tr><tr><td>Net debt/equity (%)</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td></td></tr></table>

Source: Company data, NOM estimates

Rating Remains Buy

Target price
Increased from
CNY 1,015.00
CNY 1,325.00

Closing price 6 July 2026 CNY 1,098.92

<table><tr><td>Implied upside</td><td>+20.6%</td></tr></table>

<table><tr><td>Market Cap (USD mn)</td><td>181,397.6</td></tr><tr><td>ADT (USD mn)</td><td>4,469.0</td></tr></table>

## Relative performance chart

![](images/e2e48fe5391ef385c63126338009b502d92ab8e125f651c11171fbc005df096c.jpg)  
Source: LSEG, NOM

## Research Analysts

China Technology
Bing Duan - NIHK
bing.duan1@NOM.com
+852 2252 2141

Ethan Zhang - NIHK
ethan.zhang@NOM.com
+852 2252 2157

## Key data on Zhongji InnoLight

Cashflow statement (CNYmn)

<table><tr><td>Performance(%)</td><td>1M</td><td>3M</td><td>12M</td><td></td><td></td></tr><tr><td>Absolute (CNY)</td><td>-6.9</td><td>81.2</td><td>688.0</td><td>M cap (USDmn)</td><td>181,397.6</td></tr><tr><td>Absolute (USD)</td><td>-7.2</td><td>83.6</td><td>731.4</td><td>Free float (%)</td><td>68.1</td></tr><tr><td>Rel to CSI 300</td><td>-7.4</td><td>72.1</td><td>666.4</td><td>3-mth ADT (USDmn)</td><td>4,469.0</td></tr></table>

<table><tr><td colspan="6">Income statement (CNYmn)</td></tr><tr><td>Year-end 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>Revenue</td><td>23,862</td><td>38,240</td><td>122,105</td><td>261,031</td><td>371,545</td></tr><tr><td>Cost of goods sold</td><td>-15,796</td><td>-22,166</td><td>-66,275</td><td>-140,825</td><td>-199,824</td></tr><tr><td>Gross profit</td><td>8,067</td><td>16,074</td><td>55,830</td><td>120,206</td><td>171,721</td></tr><tr><td>SG&amp;A</td><td>-2,170</td><td>-2,170</td><td>-13,033</td><td>-29,168</td><td>-43,374</td></tr><tr><td>Employee share expense</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Operating profit</td><td>5,897</td><td>13,905</td><td>42,796</td><td>91,038</td><td>128,347</td></tr><tr><td>EBITDA</td><td>6,442</td><td>14,644</td><td>43,304</td><td>91,633</td><td>129,009</td></tr><tr><td>Depreciation</td><td>-545</td><td>-740</td><td>-508</td><td>-595</td><td>-663</td></tr><tr><td>Amortisation</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EBIT</td><td>5,897</td><td>13,905</td><td>42,796</td><td>91,038</td><td>128,347</td></tr><tr><td>Net interest expense</td><td>144</td><td>-183</td><td>-584</td><td>-1,248</td><td>-1,776</td></tr><tr><td>Associates &amp; JCEs</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other income</td><td>11</td><td>-122</td><td>-390</td><td>-834</td><td>-1,188</td></tr><tr><td>Earnings before tax</td><td>6,052</td><td>13,600</td><td>41,822</td><td>88,956</td><td>125,383</td></tr><tr><td>Income tax</td><td>-681</td><td>-2,020</td><td>-6,212</td><td>-13,212</td><td>-18,622</td></tr><tr><td>Net profit after tax</td><td>5,372</td><td>11,580</td><td>35,610</td><td>75,744</td><td>106,761</td></tr><tr><td>Minority interests</td><td>-200</td><td>-782</td><td>-1,956</td><td>-2,347</td><td>-2,817</td></tr><tr><td>Other items</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Preferred dividends</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Normalised NPAT</td><td>5,171</td><td>10,797</td><td>33,654</td><td>73,396</td><td>103,944</td></tr><tr><td>Extraordinary items</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Reported NPAT</td><td>5,171</td><td>10,797</td><td>33,654</td><td>73,396</td><td>103,944</td></tr><tr><td>Dividends</td><td>-845</td><td>-1,764</td><td>-5,498</td><td>-11,991</td><td>-16,981</td></tr><tr><td>Transfer to reserves</td><td>4,327</td><td>9,033</td><td>28,156</td><td>61,406</td><td>86,963</td></tr><tr><td>Valuations and ratios</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Reported P/E (x)</td><td>238.2</td><td>113.1</td><td>36.3</td><td>16.6</td><td>11.7</td></tr><tr><td>Normalised P/E (x)</td><td>238.2</td><td>113.1</td><td>36.3</td><td>16.6</td><td>11.7</td></tr><tr><td>FD normalised P/E (x)</td><td>238.2</td><td>113.1</td><td>36.3</td><td>16.6</td><td>11.7</td></tr><tr><td>Dividend yield (%)</td><td>0.1</td><td>0.1</td><td>0.5</td><td>1.0</td><td>1.4</td></tr><tr><td>Price/cashflow (x)</td><td>389.3</td><td>112.1</td><td>35.2</td><td>16.2</td><td>11.9</td></tr><tr><td>Price/book (x)</td><td>64.4</td><td>41.0</td><td>21.1</td><td>10.2</td><td>5.9</td></tr><tr><td>EV/EBITDA (x)</td><td>191.0</td><td>83.6</td><td>27.7</td><td>12.4</td><td>8.2</td></tr><tr><td>EV/EBIT (x)</td><td>208.7</td><td>88.1</td><td>28.0</td><td>12.5</td><td>8.2</td></tr><tr><td>Gross margin (%)</td><td>33.8</td><td>42.0</td><td>45.7</td><td>46.1</td><td>46.2</td></tr><tr><td>EBITDA margin (%)</td><td>27.0</td><td>38.3</td><td>35.5</td><td>35.1</td><td>34.7</td></tr><tr><td>EBIT margin (%)</td><td>24.7</td><td>36.4</td><td>35.0</td><td>34.9</td><td>34.5</td></tr><tr><td>Net margin (%)</td><td>21.7</td><td>28.2</td><td>27.6</td><td>28.1</td><td>28.0</td></tr><tr><td>Effective tax rate (%)</td><td>11.2</td><td>14.9</td><td>14.9</td><td>14.9</td><td>14.9</td></tr><tr><td>Dividend payout (%)</td><td>16.3</td><td>16.3</td><td>16.3</td><td>16.3</td><td>16.3</td></tr><tr><td>ROE (%)</td><td>31.0</td><td>44.2</td><td>76.8</td><td>82.8</td><td>63.8</td></tr><tr><td>ROA (pretax %)</td><td>29.1</td><td>47.9</td><td>105.4</td><td>165.1</td><td>173.9</td></tr><tr><td>Growth (%)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Revenue</td><td>122.6</td><td>60.3</td><td>219.3</td><td>113.8</td><td>42.3</td></tr><tr><td>EBITDA</td><td>150.4</td><td>127.3</td><td>195.7</td><td>111.6</td><td>40.8</td></tr><tr><td>Normalised EPS</td><td>70.4</td><td>110.7</td><td>211.7</td><td>118.1</td><td>41.6</td></tr><tr><td>Normalised FDEPS</td><td>70.4</td><td>110.7</td><td>211.7</td><td>118.1</td><td>41.6</td></tr></table>

Source: Company data, NOM estimates

<table><tr><td colspan="6">Cashflow statement (CNYmn)</td></tr><tr><td>Year-end 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>EBITDA</td><td>6,442</td><td>14,644</td><td>43,304</td><td>91,633</td><td>129,009</td></tr><tr><td>Change in working capital</td><td>-4,452</td><td>-910</td><td>275</td><td>1,279</td><td>-2,093</td></tr><tr><td>Other operating cashflow</td><td>1,174</td><td>-2,839</td><td>-8,914</td><td>-17,414</td><td>-24,175</td></tr><tr><td>Cashflow from operations</td><td>3,165</td><td>10,896</td><td>34,665</td><td>75,498</td><td>102,742</td></tr><tr><td>Capital expenditure</td><td>-2,866</td><td>-2,760</td><td>-2,460</td><td>-2,160</td><td>-1,860</td></tr><tr><td>Free cashflow</td><td>298</td><td>8,136</td><td>32,205</td><td>73,338</td><td>100,882</td></tr><tr><td>Reduction in investments</td><td>0</td><td>0</td><td>0</td><td></td><td></td></tr><tr><td>Net acquisitions</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Dec in other LT assets</td><td>0</td><td>0</td><td>0</td><td></td><td></td></tr><tr><td>Inc in other LT liabilities</td><td>917</td><td>130</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Adjustments</td><td>-993</td><td>12</td><td>0</td><td></td><td></td></tr><tr><td>CF after investing acts</td><td>223</td><td>8,278</td><td>32,205</td><td>73,338</td><td>100,882</td></tr><tr><td>Cash dividends</td><td>-845</td><td>-1,764</td><td>-5,498</td><td>-11,991</td><td>-16,981</td></tr><tr><td>Equity issue</td><td>246</td><td>205</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Debt issue</td><td>1,685</td><td>-1,114</td><td>500</td><td>500</td><td>500</td></tr><tr><td>Convertible debt issue</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Others</td><td>428</td><td>328</td><td>0</td><td>0</td><td>0</td></tr><tr><td>CF from financial acts</td><td>1,514</td><td>-2,344</td><td>-4,998</td><td>-11,491</td><td>-16,481</td></tr><tr><td>Net cashflow</td><td>1,737</td><td>5,933</td><td>27,207</td><td>61,848</td><td>84,401</td></tr><tr><td>Beginning cash</td><td>3,317</td><td>5,054</td><td>10,987</td><td>38,193</td><td>100,041</td></tr><tr><td>Ending cash</td><td>5,054</td><td>10,987</td><td>38,193</td><td>100,041</td><td>184,442</td></tr><tr><td>Ending net debt</td><td>-2,377</td><td>-9,391</td><td>-36,098</td><td>-97,446</td><td>-181,346</td></tr><tr><td colspan="6">Balance sheet (CNYmn)</td></tr><tr><td>As at 31 Dec</td><td>FY24</td><td>FY25</td><td>FY26F</td><td>FY27F</td><td>FY28F</td></tr><tr><td>Cash &amp; equivalents</td><td>5,054</td><td>10,987</td><td>38,193</td><td>100,041</td><td>184,442</td></tr><tr><td>Marketable securities</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Accounts receivable</td><td>4,988</td><td>6,635</td><td>8,629</td><td>10,962</td><td>13,597</td></tr><tr><td>Inventories</td><td>7,051</td><td>12,681</td><td>21,536</td><td>34,422</td><td>51,577</td></tr><tr><td>Other current assets</td><td>1,103</td><td>781</td><td>781</td><td>781</td><td>781</td></tr><tr><td>Total current assets</td><td>18,196</td><td>31,084</td><td>69,139</td><td>146,206</td><td>250,396</td></tr><tr><td>LT investments</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Fixed assets</td><td>5,872</td><td>8,503</td><td>10,455</td><td>12,020</td><td>13,217</td></tr><tr><td>Goodwill</td><td>378</td><td>378</td><td>291</td><td>205</td><td>118</td></tr><tr><td>Other intangible assets</td><td>4,420</td><td>5,325</td><td>5,184</td><td>5,042</td><td>4,901</td></tr><tr><td>Other LT assets</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Total assets</td><td>28,866</td><td>45,289</td><td>85,069</td><td>163,473</td><td>268,632</td></tr><tr><td>Short-term debt</td><td>2,070</td><td>1,086</td><td>1,586</td><td>2,086</td><td>2,586</td></tr><tr><td>Accounts payable</td><td>4,417</td><td>10,446</td><td>21,570</td><td>38,068</td><td>55,765</td></tr><tr><td>Other current liabilities</td><td>10</td><td>27</td><td>27</td><td>27</td><td>27</td></tr><tr><td>Total current liabilities</td><td>6,497</td><td>11,558</td><td>23,182</td><td>40,180</td><td>58,377</td></tr><tr><td>Long-term debt</td><td>606</td><td>510</td><td>510</td><td>510</td><td>510</td></tr><tr><td>Convertible debt</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other LT liabilities</td><td>1,470</td><td>1,599</td><td>1,599</td><td>1,599</td><td>1,599</td></tr><tr><td>Total liabilities</td><td>8,573</td><td>13,668</td><td>25,292</td><td>42,290</td><td>60,486</td></tr><tr><td>Minority interest</td><td>1,159</td><td>1,856</td><td>1,856</td><td>1,856</td><td>1,856</td></tr><tr><td>Preferred stock</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Common stock</td><td>19,134</td><td>29,765</td><td>57,921</td><td>119,327</td><td>206,290</td></tr><tr><td>Retained earnings</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Proposed dividends</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other equity and reserves</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Total shareholders&#x27; equity</td><td>19,134</td><td>29,765</td><td>57,921</td><td>119,327</td><td>206,290</td></tr><tr><td>Total equity &amp; liabilities</td><td>28,866</td><td>45,289</td><td>85,069</td><td>163,473</td><td>268,632</td></tr><tr><td>Liquidity (x)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Current ratio</td><td>2.80</td><td>2.69</td><td>2.98</td><td>3.64</td><td>4.29</td></tr><tr><td>Interest cover</td><td>-</td><td>76.1</td><td>73.3</td><td>73.0</td><td>72.3</td></tr><tr><td>Leverage</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Net debt/EBITDA (x)</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td></tr><tr><td>Net debt/equity (%)</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td><td>net cash</td></tr><tr><td>Per share</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Reported EPS (CNY)</td><td>4.61</td><td>9.72</td><td>30.29</td><td>66.06</td><td>93.55</td></tr><tr><td>Norm EPS (CNY)</td><td>4.61</td><td>9.72</td><td>30.29</td><td>66.06</td><td>93.55</td></tr><tr><td>FD norm EPS (CNY)</td><td>4.61</td><td>9.72</td><td>30.29</td><td>66.06</td><td>93.55</td></tr><tr><td>BVPS (CNY)</td><td>17.07</td><td>26.79</td><td>52.13</td><td>107.39</td><td>185.66</td></tr><tr><td>DPS (CNY)</td><td>0.75</td><td>1.59</td><td>4.95</td><td>10.79</td><td>15.28</td></tr><tr><td>Activity (days)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Days receivable</td><td>61.0</td><td>55.5</td><td>22.8</td><td>13.7</td><td>12.1</td></tr><tr><td>Days inventory</td><td>131.1</td><td>162.5</td><td>94.2</td><td>72.5</td><td>78.8</td></tr><tr><td>Days payable</td><td>94.1</td><td>122.4</td><td>88.2</td><td>77.3</td><td>85.9</td></tr><tr><td>Cash cycle</td><td>98.0</td><td>95.6</td><td>28.9</td><td>8.9</td><td>4.9</td></tr></table>

Source: Company data, NOM estimates

## Company profile

Zhongji InnoLight is a China-based company mainly engaged in high-end optical communication transceiver module business and intelligent equipment manufacturing business. The company supplies optical transceiver modules to cloud computing data centers, data communications, 5G wireless networks and telecommunications transmission networks.

## Valuation Methodology

Our TP of CNY1,325.00 is based on 20x 2027F EPS of CNY66.06, in line with the WIND China's A share tech / electronic component sector median P/E range. The benchmark index is CSI300.

Risks that may impede the achievement of the target price

Downside risks: 1) weaker-than-expected demand for high-end optical modules in both the datacom and telecom markets; 2) fierce competition in the 400G and 800G optical modules segments; 3) slower-than-expected product upgrades (i.e., 800G, 1.6T); and 4) escalated price war which may affect company's export to global customers.

## ESG

Zhongji InnoLight, as a social responsibility, offers infrastructure products to telecom network and data centers. The manufacturing of optical modules requires land, equipment and other materials, which may impact the environment, while factory automation may help to improve its environmental friendliness.

## Earnings forecast revisions

We raise our FY26-28F revenue forecasts by 0-37% to reflect the strong demand for high-end transceiver products such as 1.6T/3.2T transceivers,

[中间内容因长度限制已省略]

 SUITABILITY OF THE INVESTMENT, UNDER A SEPARATE ENGAGEMENT, AS THE RECIPIENT DEEMS FIT. Unless prohibited by the provisions of Regulation S of the 1933 Act, this material is distributed in the US, by NSI, a US-registered broker-dealer, which accepts responsibility for its contents in accordance with the provisions of Rule 15a-6, under the US Securities Exchange Act of 1934. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia ('Saudi Arabia') or a 'Market Counterparty' or a 'Professional Client' (as defined by the Dubai Financial Services Authority) in the United Arab Emirates ('UAE') or a 'Market Counterparty' or a 'Business Customer' (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar ('Qatar') by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
