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
U.S. SMID-Cap Software Datadog Inc

Rating Market-Perform

Price Target

DDOG

226.00 USD

![](images/4c59cb95f50c142f62854bdf717c4b85d64ced04dd2ba322536081fa096ad393.jpg)  
Peter Weed  
+1 917 344 8390  
peter.weed@bernsteinsg.com

![](images/f49810c1bcdb49afa0eb9be918d65ef3048ddd928afbea3616e1618fc440fd23.jpg)

Luwei Yang  
+1 917 344 8342  
luwei.yang@bernsteinsg.com

# Datadog (DDOG): AWS Q2 results readthrough to earnings

With Datadog's earnings just a week away, we want to offer a quick updated readthrough from AWS' Q2 earnings Thursday after market. If you have been following our quarterly AWS web metric work (latest note here), you may remember that we've found AWS' ex-AI revenue to be a strong signal for the core customers that make up \~85% of Datadog's revenue (the remaining \~15% are Born-in-AI customers, with more than half of that we believe being driven by the two largest AI Labs). We won't bury the lede any deeper: AWS reported 36.7% YoY growth, up from 28.4% last quarter. But this includes AI revenue that grew to "more than \$25B ARR" in Q2 up from "more than \$15B ARR" in Q1. With the AI revenue excluded, we think AWS ex-AI grew QoQ in the \~6% range.

AWS signal: very close to our published Datadog model. Yes, there is a potential few \$MM of error in this read through model (we think more likely to the upside), the least of which is AWS isn't super specific in their AI revenue communications, plus the web metric work is good with mid 0.9x r^2 that still leaves a little wiggle. But nothing we heard in the earnings would be enough for us to change the directional message in our current model: this quarter is likely to see further step-up in core revenue growth in the mid 100bps range (last quarter we estimate at \~26.0%, and think this quarter would be low-to-mid 27.x% range).

<table><tr><td>Close Date</td><td></td><td></td><td colspan="2">30 Jul 2026</td></tr><tr><td>DDOG Close Price (USD)</td><td></td><td></td><td colspan="2">268.56</td></tr><tr><td>Price Target (USD)</td><td></td><td></td><td colspan="2">226.00</td></tr><tr><td>Upside/(Downside)</td><td></td><td></td><td colspan="2">(16)%</td></tr><tr><td>52-Week Range</td><td></td><td></td><td colspan="2">278.71/98.01</td></tr><tr><td>SPX</td><td></td><td></td><td colspan="2">7,437.63</td></tr><tr><td>FYE</td><td></td><td></td><td colspan="2">Dec</td></tr><tr><td>Div Yield</td><td></td><td></td><td colspan="2">NA</td></tr><tr><td>Market Cap (USD) (M)</td><td></td><td></td><td colspan="2">95,605</td></tr><tr><td>EV (USD) (M)</td><td></td><td></td><td colspan="2">92,132</td></tr><tr><td>Performance</td><td>YTD</td><td>1M</td><td>6M</td><td>12M</td></tr><tr><td>Absolute (%)</td><td>97.5</td><td>3.1</td><td>107.7</td><td>80.4</td></tr><tr><td>SPX (%)</td><td>8.6</td><td>(0.8)</td><td>7.2</td><td>16.9</td></tr><tr><td>Relative (%)</td><td>88.8</td><td>4.0</td><td>100.5</td><td>63.5</td></tr></table>

Source: Bloomberg, Bernstein estimates and analysis.

AWS web metrics update: July starting behind, but good trajectory (in line with our model expectation). A quick update on AWS web metrics that we use on a +1 quarter basis to preview how we think core growth could evolve. As we've covered before, Q2 growth flat lined for the latter part of the quarter (Exhibit 1), but this still puts it ahead of 2025 (which was impacted by DOGE/tariffs until late in the quarter) so there will likely be a small further Q3 revenue growth tailwind. BUT! Q4 we warned was likely to see YoY growth headwinds because the -1 year comp is very tough, and the starting point in the quarter is weak (Exhibit 2). Our model assumes slightly above "normal" QoQ growth, and that looks like the current trajectory. The result would be Q4 seeing nearly 200bps YoY growth headwind, if so. Note: for the "Born-in-AI" component of our model, see our note here.

Price Performance, 1YR  
![](images/91e74fbd356678ff3c07ca54adb65e6fb748c500d92c992dad77c693a90536ff.jpg)

## Investment Implications

No change to our model, \$226 PT or Market-Perform recommendation

<table><tr><td>Adjusted EPS</td><td>F25A</td><td>F26E</td><td>F27E</td><td>Financials</td><td>F25A</td><td>F26E</td><td>F27E</td><td>CAGR</td></tr><tr><td>DDOG (USD)</td><td>2.05</td><td>2.69</td><td>3.37</td><td>Cost of Goods Sold (M)</td><td>686.96</td><td>928.45</td><td>1,164</td><td>--</td></tr><tr><td></td><td></td><td></td><td></td><td>FCF (M)</td><td>914.72</td><td>1,296</td><td>1,747</td><td>--</td></tr><tr><td></td><td></td><td></td><td></td><td>Operating Earnings (M)</td><td>768.04</td><td>1,086</td><td>1,420</td><td>--</td></tr><tr><td></td><td></td><td></td><td></td><td>Revenues (M)</td><td>3,427</td><td>4,543</td><td>5,654</td><td>28.4%</td></tr></table>

Source: Bloomberg, Bernstein estimates and analysis.

<table><tr><td>Valuation Metrics</td><td>25A</td><td>26E</td><td>27E</td></tr><tr><td>EV/EBIT (x)</td><td>N/M</td><td>644</td><td>254</td></tr><tr><td>Adjusted P/E (x)</td><td>130.7</td><td>100.0</td><td>79.6</td></tr><tr><td>EV/FCF (x)</td><td>100.7</td><td>71.1</td><td>52.7</td></tr><tr><td>EV/Sales (x)</td><td>26.9</td><td>20.3</td><td>16.3</td></tr></table>

## DETAILS

EXHIBIT 1: AWS web metrics were tracking well above prior year levels in April but began to level off in May, with the relative softness persisting through June. After the July 4th holiday, the consumption trend started to pick up again, following a similar trajectory to prior years. Because 2025 was even weaker, this signals acceleration will continue modestly into Q3. [reminder: current quarter web metrics are similar to ARR added, thus signal +1 quarter revenue recognition, with Q2 web metrics signaling Q3 revenue, in this case]

AWS SSO Web Metrics: % change relative to March average

![](images/104ee75d71f0c55641bc02d8ca6536595dfadc811c03e38e2f4ed45718b82471.jpg)  
AWS SSO = awsapps.com

Similarweb data for $4^{\text{th}}$ week in July includes a Bernstein estimate for Saturday July $25^{\text{th}}$ (as the data is not yet available) — this day is normally a very small contributor, so we anticipate our estimate to be roughly accurate.  
Source: Similarweb, Bernstein estimates and analysis

EXHIBIT 2: Although this July started at a lower base than the prior years due to the softness we saw in Q2, the trend has large tracked the pattern observed in 2025. Our model assumes it to mirror 2025's trajectory for the remainder of the quarter, allowing it to catch up from a weak starting point and result in a "normal" sequential growth quarter close or a bit above 2023 (but still below 2025, implying some YoY growth headwinds in Q4 revenue recognition). [reminder: current quarter web metrics are similar to ARR added, thus signal +1 quarter revenue recognition]

AWS SSO Web Metrics: % change relative to Q2 average (adj.)

![](images/278e29e81657c91f771ad880e4e99ec2da98b767016efcf49b78d1b43a18c6f9.jpg)  
AWS SSO = awsapps.com

Similarweb data for $4^{\text{th}}$ week in July includes a Bernstein estimate for Saturday July $25^{\text{th}}$ (as the data is not yet available) — this day is normally a very small contributor, so we anticipate our estimate to be roughly accurate.  
Source: Similarweb, Bernstein estimates and analysis

## APPENDIX - FINANCIAL FORECASTS

EXHIBIT 3: Datadog Financial Summary

<table><tr><td>Datadog$, ThousandsIncome Statement (Non-GAAP)</td><td>202012/31/20202020</td><td>202112/31/20212021</td><td>202212/31/20222022</td><td>202312/31/20232023</td><td>202412/31/20242024</td><td>202512/31/20252025</td><td>Q1263/31/2026Q126</td><td>Q2266/30/2026Q226E</td><td>Q3269/30/2026Q326E</td><td>Q42612/31/2026Q426E</td><td>202612/31/20262026E</td><td>202712/31/20272027E</td><td>202812/31/20282028E</td></tr><tr><td>Total Revenue</td><td>603,466</td><td>1,028,784</td><td>1,675,100</td><td>2,128,359</td><td>2,684,275</td><td>3,427,158</td><td>1,006,426</td><td>1,114,858</td><td>1,190,299</td><td>1,231,810</td><td>4,543,393</td><td>5,653,900</td><td>7,066,261</td></tr><tr><td>Cost of Revenue (Non-GAAP)</td><td>127,273</td><td>225,543</td><td>328,900</td><td>383,925</td><td>483,222</td><td>651,105</td><td>199,200</td><td>218,432</td><td>230,832</td><td>236,419</td><td>884,884</td><td>1,112,518</td><td>1,404,626</td></tr><tr><td>Gross Profit (Non-GAAP)</td><td>476,193</td><td>803,241</td><td>1,346,200</td><td>1,744,434</td><td>2,201,053</td><td>2,776,053</td><td>807,226</td><td>896,426</td><td>959,466</td><td>995,391</td><td>3,658,510</td><td>4,541,382</td><td>5,661,635</td></tr><tr><td>R&amp;D (Non-GAAP)</td><td>172,511</td><td>309,684</td><td>504,847</td><td>627,902</td><td>758,268</td><td>1,038,742</td><td>300,351</td><td>349,366</td><td>356,274</td><td>356,024</td><td>1,362,016</td><td>1,666,107</td><td>2,011,772</td></tr><tr><td>S&amp;M (Non-GAAP)</td><td>189,886</td><td>257,513</td><td>414,962</td><td>500,597</td><td>629,007</td><td>793,082</td><td>235,272</td><td>246,045</td><td>245,836</td><td>273,117</td><td>1,000,269</td><td>1,206,511</td><td>1,438,264</td></tr><tr><td>G&amp;A (Non-GAAP)</td><td>50,195</td><td>70,986</td><td>100,111</td><td>125,692</td><td>139,565</td><td>176,184</td><td>48,106</td><td>51,059</td><td>54,514</td><td>56,415</td><td>210,095</td><td>248,952</td><td>287,630</td></tr><tr><td>Total Operating Expenses (Non-GAAP)</td><td>412,592</td><td>638,183</td><td>1,019,920</td><td>1,254,191</td><td>1,526,840</td><td>2,008,008</td><td>583,729</td><td>646,470</td><td>656,624</td><td>685,556</td><td>2,572,380</td><td>3,121,570</td><td>3,737,666</td></tr><tr><td>Operating Income (Non-GAAP)</td><td>63,601</td><td>165,058</td><td>326,280</td><td>490,243</td><td>674,213</td><td>768,044</td><td>223,497</td><td>249,956</td><td>302,842</td><td>309,835</td><td>1,086,130</td><td>1,419,812</td><td>1,923,969</td></tr><tr><td>Margin %</td><td>11%</td><td>16%</td><td>19%</td><td>23%</td><td>25%</td><td>22%</td><td>22%</td><td>22.4%</td><td>25.4%</td><td>25.2%</td><td>23.9%</td><td>25.1%</td><td>27.2%</td></tr><tr><td>Interest income and other, net</td><td>10,278</td><td>4,083</td><td>23,994</td><td>97,087</td><td>153,417</td><td>176,996</td><td>52,650</td><td>39,070</td><td>41,110</td><td>43,559</td><td>176,389</td><td>210,330</td><td>280,947</td></tr><tr><td>[Non-GAAP] Earnings before taxes</td><td>73,879</td><td>169,141</td><td>350,274</td><td>587,330</td><td>827,630</td><td>945,040</td><td>276,147</td><td>289,026</td><td>343,952</td><td>353,394</td><td>1,262,519</td><td>1,630,141</td><td>2,204,916</td></tr><tr><td>Provision for income taxes</td><td>(2,325)</td><td>(2,323)</td><td>(73,557)</td><td>(123,339)</td><td>(173,802)</td><td>(198,458)</td><td>(57,991)</td><td>(60,696)</td><td>(72,230)</td><td>(74,213)</td><td>(265,130)</td><td>(342,330)</td><td>(463,033)</td></tr><tr><td>Net income (loss)</td><td>71,554</td><td>166,818</td><td>276,717</td><td>463,991</td><td>653,828</td><td>746,582</td><td>218,156</td><td>228,331</td><td>271,722</td><td>279,181</td><td>997,389</td><td>1,287,811</td><td>1,741,882</td></tr><tr><td>Net income attributable to common shareholders</td><td>71,554</td><td>166,818</td><td>276,717</td><td>463,991</td><td>653,828</td><td>746,582</td><td>218,156</td><td>228,331</td><td>271,722</td><td>279,181</td><td>997,389</td><td>1,287,811</td><td>1.741,882</td></tr><tr><td>Earnings (loss) per share - Basic</td><td>$0.24</td><td>$0.54</td><td>$0.88</td><td>$1.43</td><td>$1.94</td><td>$2.15</td><td>$0.62</td><td>$0.64</td><td>$0.75</td><td>$0.77</td><td>$2.78</td><td>$3.48</td><td>$4.58</td></tr><tr><td>Earnings (loss) per share - Diluted</td><td>$0.22</td><td>$0.48</td><td>$0.80</td><td>$1.32</td><td>$1.82</td><td>$2.05</td><td>$0.60</td><td>$0.62</td><td>$0.73</td><td>$0.74</td><td>$2.69</td><td>$3.37</td><td>$4.47</td></tr><tr><td>Balance Sheet</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>Q126</td><td>Q226E</td><td>Q326E</td><td>Q426E</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Cash and cash equivalents</td><td>224,927</td><td>270,973</td><td>338,985</td><td>330,339</td><td>1,246,983</td><td>401,305</td><td>426,360</td><td>472,192</td><td>504,032</td><td>545,121</td><td>545,121</td><td>708,339</td><td>924,191</td></tr><tr><td>Marketable securities</td><td>1,292,532</td><td>1,283,473</td><td>1,545,341</td><td>2,252,559</td><td>2,942,076</td><td>4,073,531</td><td>4,332,257</td><td>4,575,786</td><td>4,880,046</td><td>5,274,449</td><td>5,274,449</td><td>6,925,929</td><td>9,131,469</td></tr><tr><td>Receivables</td><td>163,359</td><td>268,824</td><td>399,551</td><td>509,279</td><td>598,919</td><td>741,262</td><td>680,434</td><td>812,983</td><td>737,153</td><td>908,108</td><td>908,108</td><td>1,085,313</td><td>1,279,836</td></tr><tr><td>Other current assets</td><td>37,262</td><td>47,678</td><td>60,357</td><td>85,960</td><td>123,137</td><td>166,182</td><td>186,155</td><td>174,825</td><td>195,734</td><td>213,015</td><td>213,015</td><td>259,796</td><td>300,278</td></tr><tr><td>Total current assets</td><td>1,718,080</td><td>1,870,948</td><td>2,344,234</td><td>3,178,137</td><td>4,911,115</td><td>5,382,280</td><td>5,625,206</td><td>6,035,786</td><td>6,316,964</td><td>6,940,693</td><td>6,940,693</td><td>8,979,376</td><td>11,635,773</td></tr><tr><td>Total PPE</td><td>47,197</td><td>75,152</td><td>125,346</td><td>171,872</td><td>226,970</td><td>338,093</td><td>378,944</td><td>411,592</td><td>445,867</td><td>480,333</td><td>480,333</td><td>626,969</td><td>804,480</td></tr><tr><td>Other assets</td><td>125,008</td><td>434,694</td><td>535,272</td><td>586,063</td><td>647,254</td><td>923,471</td><td>947,862</td><td>950,046</td><td>957,647</td><td>973,683</td><td>973,683</td><td>1,011,081</td><td>1,035,440</td></tr><tr><td>Total assets</td><td>1,890,285</td><td>2,380,794</td><td>3,004,852</td><td>3,936,072</td><td>5,785,339</td><td>6,643,844</td><td>6,952,012</td><td>7,397,424</td><td>7,720,478</td><td>8,394,709</td><td>8,394,709</td><td>10,617,426</td><td>13,475,693</td></tr><tr><td>Accounts payable</td><td>21,342</td><td>25,270</td><td>23,474</td><td>87,712</td><td>107,731</td><td>148,791</td><td>174,801</td><td>275,643</td><td>224,798</td><td>233,704</td><td>233,704</td><td>314,473</td><td>375,230</td></tr><tr><td>Other current liabilities</td><td>276,502</td><td>503,426</td><td>736,274</td><td>915,340</td><td>1,120,959</td><td>1,442,610</td><td>1,481,102</td><td>1,542,320</td><td>1,580,028</td><td>1,885,914</td><td>1,885,914</td><td>2,437,914</td><td>3,114,301</td></tr><tr><td>Total current liabilities</td><td>297,844</td><td>528,696</td><td>759,748</td><td>1,003,052</td><td>1,862,713</td><td>1,591,401</td><td>1,655,903</td><td>1,817,963</td><td>1,804,826</td><td>2,119,617</td><td>2,119,617</td><td>2,752,387</td><td>3,489,531</td></tr><tr><td>Deferred revenue, non-current</td><td>3,450</td><td>13,896</td><td>12,944</td><td>21,210</td><td>22,693</td><td>68,711</td><td>50,918</td><td>51,407</td><td>54,389</td><td>70,452</td><td>70,452</td><td>87,511</td><td>111,315</td></tr><tr><td>Other liabilities, non-current</td><td>631,559</td><td>796,999</td><td>821,655</td><td>886,456</td><td>1,185,570</td><td>1,251,526</td><td>1,256,969</td><td>1,274,129</td><td>1,291,281</td><td>1,309,124</td><td>1,309,124</td><td>1,381,771</td><td>1,459,265</td></tr><tr><td>Total non-current liabilities</td><td>635,009</td><td>810,895</td><td>834,599</td><td>907,666</td><td>1,208,263</td><td>1,320,237</td><td>1,307,887</td><td>1,325,536</td><td>1,345,670</td><td>1,379,575</td><td>1,379,575</td><td>1,469,282</td><td>1,570,580</td></tr><tr><td>Total Liabilities</td><td>932,853</td><td>1,339,591</td><td>1,594,347</td><td>1,910,718</td><td>3,070,976</td><td>2,911,638</td><td>2,963,790</td><td>3,143,499</td><td>3,150,496</td><td>3,499,193</td><td>3,499,193</td><td>4,221,669</td><td>5,060,111</td></tr><tr><td>Total Equity</td><td>957,432</td><td>1,041,203</td><td>1,410,505</td><td>2,025,354</td><td>2,714,363</td><td>3,732,206</td><td>3,988,222</td><td>4,253,925</td><td>4,569,982</td><td>4,895,516</td><td>4,895,516</td><td>6,395,757</td><td>8,415,582</td></tr><tr><td>Total Liabilities and Equity</td><td>1,890,285</td><td>2,380,794</td><td>3,004,852</td><td>3,936,072</td><td>5,785,339</td><td>6,643,844</td><td>6,952,012</td><td>7,397,424</td><td>7,720,478</td><td>8,394,708</td><td>8,394,708</td><td>10,617,426</td><td>13,475,693</td></tr><tr><td>Balance Sheet Check</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Cash Flow Statement</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>Q126</td><td>Q226E</td><td>Q326E</td><td>Q426E</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Cash used for operating activities</td><td>109,091</td><td>286,545</td><td>418,407</td><td>659,954</td><td>870,603</td><td>1,050,135</td><td>334,622</td><td>323,541</td><td>372,170</td><td>471,649</td><td>1,501,981</td><td>1,995,230</td><td>2,677,260</td></tr><tr><td>Cash used for investing activities</td><td>(1,152,624)</td><td>(273,740)</td><td>(384,670)</td><td>(731,365)</td><td>(736,840)</td><td>(1,334,480)</td><td>(314,798)</td><td>(281,331)</td><td>(344,765)</td><td>(435,898)</td><td>(1,376,792)</td><td>(1,855,054)</td><td>(2,486,562)</td></tr><tr><td>Cash used for financing activities</td><td>670,276</td><td>34,940</td><td>36,023</td><td>58,279</td><td>787,083</td><td>(572,483)</td><td>9,711</td><td>3,622</td><td>4,435</td><td>5,339</td><td>23,107</td><td>23,042</td><td>25,154</td></tr><tr><td>Effect of exchange rate changes on cash and cash equi</td><td>779</td><td>(1,993)</td><td>(1,935)</td><td>1,183</td><td>(4,202)</td><td>11,150</td><td>(4,480)</td><td></td><td></td><td></td><td>(4,480)</td><td></td><td></td></tr><tr><td rowspan="25">Increase (decrease) in cash, cash equivalents, and rncash, cash equivalents and restricted cash at beginnncash, cash equivalents and restricted cash at end ofcash flow from operations</td><td>(372,478)</td><td>45,752</td><td>67,825</td><td>(11,949)</td><td>916,644</td><td>(845,678)</td><td>25,055</td><td>45,832</td><td>31,840</td><td>41,089</td><td>143,816</td><td>163,218</td><td>215,851</td></tr><tr><td>601,189</td><td>228,711</td><td>274,463</td><td>342,288</td><td>330,339</td><td>1,246,983</td><td>401,305</td><td>426,360</td><td>472,192</td><td>504,032</td><td>504,032</td><td>541,121</td><td>708,339</td></tr><tr><td>228,711</td><td>274,463</td><td>342,288</td><td>330,339</td><td>1,246,983</td><td>401,305</td><td>426,360</td><td>472,192</td><td>504,032</td><td>545,121</td><td>545,121</td><td>708,339</td><td>924,191</td></tr><tr><td>109,091</td><td>286,545</td><td>418,407</td><td>659,954</td><td>870,603</td><td>1,050,135<

[中间内容因长度限制已省略]

ence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively "Bloomberg"). Bloomberg or Bloomberg's licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg's licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
