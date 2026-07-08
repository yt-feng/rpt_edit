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
# Taiwan Semiconductors

## Mediatek and GUC riding on Google; Alchip more back-end loaded and capacity allocation is key

## CITI'S TAKE

Investors have been optimistic about AI ASIC surpassing GPU in AI computing since last year, yet due to a more fragmented supply chain and tight component/material supply, such as wafer foundry, advanced packaging, HBM and ABF, we expect Taiwanese design service companies with better supply chain management capability to stand out with positive growth outlooks into 2027. We expect Mediatek and GUC to see the strongest AI ASIC growth momentum into next year. We prefer Mediatek most thanks to its higher value content upside with its increasing contribution from I/O, top die and potentially optics and memory custom based die in the longer term.

Mediatek - AI ASIC revenue to rise 50% in 2027, continue doubling into 2028 — We estimate Mediatek's AI ASIC revenue to reach US\$18bn in 2027 and expect it to further rise to US\$40bn in 2028 (from previous expectations of US\$13.6bn/18bn for 2027/28) mainly due to higher dollar content increase thanks to its value added not just in I/O die but also compute die. From 2028, we see Mediatek will contribute more on multiple chip tile of its client's chiplet design. Mediatek is also working on multiple opportunities in AI ASIC projects – not only chip design but also hardware L6 architecture. We expect its AI revenue to exceed its current existing business in 2 years.

GUC - CPU business upside intact in next 2 years; automotive business also showing good potential in 2028 — Thanks to solid CPU ASIC demand from its US CSP clients, we expect GUC's growth into 2027/28 to be stronger with more supply chain support. Its robotic/automotive for US client will also start contributing in late 2027/early 2028. Although its customers may look for another foundry's support besides TSMC, we expect GUC's solid partnership with TSMC to continue to be the main source for the automotive/robotic project. And GUC's CPU projects' visibility is intact through 2028. The company is also working on consumer electronics for CSP client. Along with its interconnect IP and CPO technology, we believe GUC's ASIC business growth trend remains intact.

Alchip - new product to kick off in 3Q26, suggest revisiting once 2026 expectations reset; 2027 outlook intact — We expect Alchip's revenue to snap back substantially in 2H26 thanks to its client's N3 AI accelerator ramp-up. However, due to potential capacity constraints, its client's COT business model and diversification strategy, Alchip's near-term momentum could be capped. Yet GM may see upside thanks to Alchip's back-end design contribution for more complex chip design. We would expect stronger 2027 growth once Alchip can secure more order allocation and supply.

Mediatek remains our favorite stock; Our pecking order: Mediatek > GUC > Alchip — We prefer Mediatek in AI ASIC design service thanks to its better front-end design capability in advanced node, interconnect, advanced packaging and upstream semiconductor supply chain. We also see GUC's diversification in AI ASIC/automotive/robotic, consumer product projects and strong CPU upside to support growth in the next 2-3 years. Alchip's momentum would be more back-end loaded, and we expect to see better growth into next year.

Laura (Chia Yi) Chen $^{AC}$ +886-2-8726-9090
laura.cy.chen@citi.com

Jack Chen

+886-2-8726-9091

jack1.chen@citi.com

Nicholas Lai

+886-2-8726-9093

nicholas.lai@citi.com

Data Summary

<table><tr><td rowspan="2" colspan="14"></td><td colspan="2">Current Fiscal Year</td><td colspan="2">Next Fiscal Year</td><td></td></tr><tr><td colspan="2">EPS</td><td colspan="2">EPS</td><td></td></tr><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Ccy</td><td rowspan="2">Price</td><td rowspan="2">Mkt Cap (M)</td><td rowspan="2">Date &amp; Time</td><td colspan="2">Rating</td><td rowspan="2">Short-Term View</td><td colspan="2">Target Price</td><td rowspan="2">ESPR (%)</td><td rowspan="2">Div Yld (%)</td><td rowspan="2">ETR (%)</td><td rowspan="2">Last Rpt Yr</td><td rowspan="2">Old</td><td rowspan="2">New</td><td rowspan="2">Old</td><td rowspan="2">New</td></tr><tr><td>Old</td><td>New</td><td>Old</td><td>New</td></tr><tr><td>Alchip</td><td>3661.TW</td><td>NT$</td><td>4,215.00</td><td>346,493</td><td>06 Jul 13:30</td><td>1</td><td>nc</td><td>Upside</td><td>6,200.00</td><td>nc</td><td>47.1</td><td>0.8</td><td>47.9</td><td>Dec-25</td><td>90.64</td><td>103.06</td><td>155.14</td><td>168.72</td></tr><tr><td>GUC</td><td>3443.TW</td><td>NT$</td><td>4,605.00</td><td>617,125</td><td>06 Jul 13:30</td><td>1H</td><td>nc</td><td>Upside</td><td>5,550.00</td><td>6,000.00</td><td>30.3</td><td>0.4</td><td>30.7</td><td>Dec-25</td><td>51.08</td><td>49.23</td><td>88.08</td><td>101.56</td></tr><tr><td>MediaTek</td><td>2454.TW</td><td>NT$</td><td>4,125.00</td><td>6,616,069</td><td>06 Jul 13:30</td><td>1</td><td>nc</td><td>Upside^</td><td>5,950.00</td><td>6,055.00</td><td>46.8</td><td>1.3</td><td>48.1</td><td>Dec-25</td><td>68.28</td><td>68.11</td><td>124.07</td><td>119.47</td></tr><tr><td colspan="6">1 = Buy, 2 = Neutral, 3 = Sell, H = High Risk</td><td colspan="13">ESPR = Expected Share Price Return, ETR = Expected Total Return, nc = no change</td></tr><tr><td colspan="6">Source: Citi</td><td colspan="13">^Catalyst Watch</td></tr></table>

Earnings Estimates

<table><tr><td colspan="4"></td><td colspan="4">Last Reported Year</td><td></td><td colspan="4">Current Fiscal Year</td><td></td><td colspan="4">Next Fiscal Year</td><td></td></tr><tr><td>Company Name</td><td>Ticker</td><td>Last Rpt Year</td><td>Currency</td><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>FY0</td><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>FY1</td><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>FY2</td></tr><tr><td>Alchip</td><td>3661.TW</td><td>Dec-25</td><td>NT$</td><td>17.69</td><td>16.02</td><td>16.04</td><td>17.92</td><td>67.68</td><td>17.25</td><td>24.64</td><td>25.57</td><td>35.61</td><td>103.06</td><td>31.34</td><td>37.86</td><td>45.62</td><td>53.90</td><td>168.72</td></tr><tr><td>Old</td><td></td><td>Dec-25</td><td>NT$</td><td>17.69</td><td>16.02</td><td>16.04</td><td>17.92</td><td>67.68</td><td>17.25</td><td>20.78</td><td>25.19</td><td>27.42</td><td>90.64</td><td>28.29</td><td>33.90</td><td>44.35</td><td>48.61</td><td>155.14</td></tr><tr><td>GUC</td><td>3443.TW</td><td>Dec-25</td><td>NT$</td><td>7.14</td><td>5.81</td><td>6.44</td><td>8.61</td><td>28.01</td><td>10.38</td><td>11.59</td><td>12.94</td><td>14.32</td><td>49.23</td><td>16.00</td><td>22.13</td><td>27.81</td><td>35.63</td><td>101.56</td></tr><tr><td>Old</td><td></td><td>Dec-25</td><td>NT$</td><td>7.14</td><td>5.81</td><td>6.44</td><td>8.61</td><td>28.01</td><td>12.23</td><td>11.59</td><td>12.94</td><td>14.32</td><td>51.08</td><td>15.02</td><td>19.58</td><td>24.75</td><td>28.74</td><td>88.08</td></tr><tr><td>MediaTek</td><td>2454.TW</td><td>Dec-25</td><td>NT$</td><td>18.43</td><td>17.50</td><td>15.84</td><td>14.40</td><td>66.17</td><td>15.17</td><td>15.94</td><td>18.26</td><td>18.75</td><td>68.11</td><td>21.88</td><td>24.98</td><td>32.91</td><td>39.70</td><td>119.47</td></tr><tr><td>Old</td><td></td><td>Dec-25</td><td>NT$</td><td>18.43</td><td>17.50</td><td>15.84</td><td>14.40</td><td>66.17</td><td>15.17</td><td>15.94</td><td>18.26</td><td>18.91</td><td>68.28</td><td>21.67</td><td>24.66</td><td>34.04</td><td>43.69</td><td>124.07</td></tr><tr><td colspan="19">Source: Citi</td></tr></table>

## Mediatek- AI ASIC revenue to rise 50% in 2027, continue doubling into 2028

We expect Mediatek to gain further market share in Google's growing TPU opportunity thanks to its better supply chain management capability and advanced node design capability. Other than N3 top die, Mediatek has been working on global leading 300G Serdes I/O for its next generation AI accelerator. Mediatek is also working on CPO technology with various partners such as Arya Labs and Microsoft in Micro LED CPO light source. With large-scale TPU revenue contribution, we now expect Mediatek's TPU shipment to reach 500k/4m/4m in 2026/2027/2028 with revenue contribution at US\$2bn/US\$18bn/US\$40bn.

Mediatek - Maintain Buy and raise TP to NT\$6,055 — In the near term, despite smartphone demand remaining lukewarm, thanks to better ASP we expect Mediatek to beat its 2Q revenue guidance and see c5% sequential growth in 3Q26. We slightly lower our 2026/2027 earnings projections mainly on smartphone weakness yet lift our 2028E earnings by 9%. We also raise our target price from NT\$5,950 to NT\$6,055 (35x PER to 2027/2028 EPS, which is 1.5-std above its 3-year average forward P/E given the promising outlook from its AI ASIC business starting from 2H26).

Figure 1. Mediatek – AI ASIC revenues and shipment forecast  
![](images/da27327bd8211b3233a536cc89be87710f02a99adf8a75b7e72dd6558b8483c7.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi

Figure 2. Mediatek – Estimates Revisions

<table><tr><td rowspan="2">(NT$mn)</td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td>New</td><td>Old</td><td>Chg.</td><td>New</td><td>Old</td><td>Chg.</td><td>New</td><td>Old</td><td>Chg.</td></tr><tr><td>Sales</td><td>616,651</td><td>619,460</td><td>-0.5%</td><td>1,083,075</td><td>1,128,745</td><td>-4.0%</td><td>2,110,784</td><td>1,928,342</td><td>9.5%</td></tr><tr><td>YoY growth</td><td>3%</td><td>4%</td><td></td><td>76%</td><td>82%</td><td></td><td>95%</td><td>71%</td><td></td></tr><tr><td>Gross profit</td><td>284,934</td><td>286,058</td><td>-0.4%</td><td>492,443</td><td>513,381</td><td>-4.1%</td><td>943,367</td><td>861,801</td><td>9.5%</td></tr><tr><td>Opex</td><td>185,062</td><td>185,891</td><td>-0.4%</td><td>304,633</td><td>317,447</td><td>-4.0%</td><td>568,994</td><td>519,906</td><td>9.4%</td></tr><tr><td>Operating profit</td><td>99,872</td><td>100,167</td><td>-0.3%</td><td>187,810</td><td>195,934</td><td>-4.1%</td><td>374,373</td><td>341,894</td><td>9.5%</td></tr><tr><td>Pre-tax profit</td><td>121,102</td><td>121,397</td><td>-0.2%</td><td>211,699</td><td>219,823</td><td>-3.7%</td><td>399,316</td><td>366,837</td><td>8.9%</td></tr><tr><td>Net income</td><td>108,435</td><td>108,701</td><td>-0.2%</td><td>190,184</td><td>197,514</td><td>-3.7%</td><td>359,452</td><td>330,149</td><td>8.9%</td></tr><tr><td>EPS (NT$)</td><td>68.11</td><td>68.28</td><td>-0.2%</td><td>119.47</td><td>124.07</td><td>-3.7%</td><td>225.79</td><td>207.39</td><td>8.9%</td></tr><tr><td>Gross margin</td><td>46.2%</td><td>46.2%</td><td>+0.0 ppt</td><td>45.5%</td><td>45.5%</td><td>-0.0 ppt</td><td>44.7%</td><td>44.7%</td><td>+0.0 ppt</td></tr><tr><td>Opex ratio</td><td>30.0%</td><td>30.0%</td><td>+0.0 ppt</td><td>28.1%</td><td>28.1%</td><td>+0.0 ppt</td><td>27.0%</td><td>27.0%</td><td>-0.0 ppt</td></tr><tr><td>Operating margin</td><td>16.2%</td><td>16.2%</td><td>+0.0 ppt</td><td>17.3%</td><td>17.4%</td><td>-0.0 ppt</td><td>17.7%</td><td>17.7%</td><td>+0.0 ppt</td></tr><tr><td>Net margin</td><td>17.6%</td><td>17.5%</td><td>+0.0 ppt</td><td>17.6%</td><td>17.5%</td><td>+0.1 ppt</td><td>17.0%</td><td>17.1%</td><td>-0.1 ppt</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi

Figure 3. Mediatek – Forward P/E band  
![](images/2e314ecea971a385b20f7d8c8c00fd1a2e00348dd54bff66cdd06e5c1c41628f.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission. Source: Citi, company data

Figure 4. Mediatek – Forward P/B band & ROE  
![](images/e648b9a65368e7c032fe798039e2eeae95e810cedefe65b290c313ee5e8f069f.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission. Source: Citi, company data

Figure 5. Mediatek – Forecast Summary

<table><tr><td>NT$mn</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>1Q27E</td><td>2Q27E</td><td>3Q27E</td><td>4Q27E</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Net sales</td><td>150,369</td><td>142,097</td><td>150,188</td><td>149,151</td><td>143,591</td><td>150,023</td><td>173,885</td><td>203,214</td><td>236,298</td><td>287,482</td><td>356,081</td><td>595,966</td><td>616,651</td><td>1,083,075</td><td>2,110,784</td></tr><tr><td>Gross profit</td><td>73,878</td><td>66,112</td><td>69,281</td><td>69,055</td><td>66,644</td><td>70,488</td><td>78,747</td><td>90,891</td><td>104,532</td><td>132,787</td><td>164,233</td><td>283,080</td><td>284,934</td><td>492,443</td><td>943,367</td></tr><tr><td>OPEX</td><td>44,499</td><td>43,924</td><td>47,431</td><td>46,164</td><td>43,795</td><td>43,807</td><td>51,296</td><td>57,916</td><td>66,163</td><td>80,495</td><td>100,059</td><td>179,610</td><td>185,062</td><td>304,633</td><td>568,994</td></tr><tr><td>Operating profit</td><td>29,379</td><td>22,188</td><td>21,850</td><td>22,891</td><td>22,848</td><td>26,681</td><td>27,451</td><td>32,975</td><td>38,369</td><td>52,292</td><td>64,174</td><td>103,470</td><td>99,872</td><td>187,810</td><td>374,373</td></tr><tr><td>Total Non-OP</td><td>3,849</td><td>7,772</td><td>5,298</td><td>4,128</td><td>5,497</td><td>5,761</td><td>5,844</td><td>5,854</td><td>5,930</td><td>6,008</td><td>6,096</td><td>21,418</td><td>21,230</td><td>23,889</td><td>24,943</td></tr><tr><td>Pre-tax profit</td><td>33,228</td><td>29,960</td><td>27,147</td><td>27,019</td><td>28,345</td><td>32,442</td><td>33,295</td><td>38,829</td><td>44,299</td><td>58,301</td><td>70,270</td><td>124,888</td><td>121,102</td><td>211,699</td><td>399,316</td></tr><tr><td>Income tax</td><td>5,163</td><td>4,509</td><td>4,074</td><td>2,643</td><td>2,773</td><td>3,173</td><td>3,257</td><td>3,798</td><td>4,333</td><td>5,703</td><td>6,874</td><td>18,770</td><td>11,846</td><td>20,708</td><td>39,060</td></tr><tr><td>Net profit</td><td>27,848</td><td>25,221</td><td>22,925</td><td>24,154</td><td>25,369</td><td>29,067</td><td>29,844</td><td>34,826</td><td>39,764</td><td>52,397</td><td>63,197</td><td>105,319</td><td>108,435</td><td>190,184</td><td>359,452</td></tr><tr><td>EPS (NT$)</td><td>17.50</td><td>15.84</td><td>14.40</td><td>15.17</td><td>15.94</td><td>18.26</td><td>18.75</td><td>21.88</td><td>24.98</td><td>32.91</td><td>39.70</td><td>66.17</td><td>68.11</td><td>119.47</td><td>225.79</td></tr><tr><td>Margins (%)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Gross profit</td><td>49.1</td><td>46.5</td><td>46.1</td><td>46.3</td><td>46.4</td><td>47.0</td><td>45.3</td><td>44.7</td><td>44.2</td><td>46.2</td><td>46.1</td><td>47.5</td><td>46.2</td><td>45.5</td><td>44.7</td></tr><tr><td>OPEX to Sales Ratio</td><td>29.6</td><td>30.9</td><td>31.6</td><td>31.0</td><td>30.5</td><td>29.2</td><td>29.5</td><td>28.5</td><td>28.0</td><td>28.0</td><td>28.1</td><td>30.1</td><td>30.0</td><td>28.1</td><td>27.0</td></tr><tr><td>Operating profit</td><td>19.5</td><td>15.6</td><td>14.5</td><td>15.3</td><td>15.9</td><td>17.8</td><td>15.8</td><td>16.2</td><td>16.2</td><td>18.2</td><td>18.0</td><td>17.4</td><td>16.2</td><td>17.3</td><td>17.7</td></tr><tr><td>Pre-tax profit</td><td>22.1</td><td>21.1</td><td>18.1</td><td>18.1</td><td>19.7</td><td>21.6</td><td>19.1</td><td>19.1</td><td>18.7</td><td>20.3</td><td>19.7</td><td>21.0</td><td>19.6</td><td>19.5</td><td>18.9</td></tr><tr><td>Net profit</td><td>18.5</td><td>17.7</td><td>15.3</td><td>16.2</td><td>17.7</td><td>19.4</td><td>17.2</td><td>17.1</td><td>16.8</td><td>18.2</td><td>17.7</td><td>17.7</td><td>17.6</td><td>17.6</td><td>17.0</td></tr><tr><td>Y/Y(%)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Net sales</td><td>18.1</td><td>7.8</td><td>8.8</td><td>(2.7)</td><td>(4.5)</td><td>5.6</td><td>15.8</td><td>36.2</td><td>64.6</td><td>91.6</td><td>104.8</td><td>12.3</td><td>3.5</td><td>75.6</td><td>94.9</td></tr><tr><td>Gross profit</td><td>18.9</td><td>2.7</td><td>3.4</td><td>(6.4)</td><td>(9.8)</td><td>6.6</td><td>13.7</td><td>31.6</td><td>56.9</td><td>88.4</td><td>108.6</td><td>7.5</td><td>0.7</td><td>72.8</td><td>91.6</td></tr><tr><td>OPEX</td><td>19.7</td><td>8.5</td><td>4.0</td><td>5.5</td><td>(1.6)</td><td>(0.3)</td><td>8.1</td><td>25.5</td><td>51.1</td><td>83.7</td><td>95.1</td><td>11.6</td><td>3.0</td><td>64.6</td><td>86.8</td></tr><tr><td>Operating profit</td><td>17.7</td><td>(7.0)</td><td>2.0</td><td>(23.8)</td><td>(22.2)</td><td>20.3</td><td>25.6</td><td>44.1</td><td>67.9</td><td>96.0</td><td>133.8</td><td>1.0</td><td>(3.5)</td><td>88.1</td><td>99.3</td></tr><tr><td>Pre-tax profit</td><td>13.8</td><td>5.3</td><td>3.6</td><td>(21.8)</td><td>(14.7)</td><td>8.3</td><td>22.6</td><td>43.7</td><td>56.3</td><td>79.7</td><td>111.1</td><td>4.5</td><td>(3.0)</td><td>74.8</td><td>88.6</td></tr><tr><td>Net profit</td><td>8.3</td><td>(0.5)</td><td>(3.6)</td><td>(17.6)</td><td>(8.9)</td><td>15.3</td><td>30.2</td><td>44.2</td><td>56.7</td><td>80.3</td><td>111.8</td><td>(1.0)</td><td>3.0</td><td>75.4</td><td>89.0</td></tr><tr><td>Q/Q(%)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Net sales</td><td>(1.9)</td><td>(5.5)</td><td>5.7</td><td>(0.7)</td><td>(3.7)</td><td>4.5</td><td>15.9</td><td>16.9</td><td>16.3</td><td>21.7</td><td>23.9</td><td></td><td></td><td></td><td></td></tr><tr><td>Gross profit</td><td>0.1</td><td>(10.5)</td><td>4.8</td><td>(0.3)</td><td>(3.5)</td><td>5.8</td><td>11.7</td><td>15.4</td><td>15.0</td><td>27.0</td><td>23.7</td><td></td><td></td><td></td><td></td></tr><tr><td>Operating profit</td><td>(2.2)</td><td>(24.5)</td><td>(1.5)</td><td>4.8</td><td>(0.2)</td><td>16.8</td><td>2.9</td><td>20.1</td><td>16.4</td><td>36.3</td><td>22.7</td><td></td><td></td><td></td><td></td></tr><tr><td>Pre-tax profit</td><td>(3.8)</td><td>(9.8)</td><td>(9.4)</td><td>(0.5)</td><td>4.9</td><td>14.5</td><td>2.6</td><td>16.6</td><td>14.1</td><td>31.6</td><td>20.5</td><td></td><td></td><td></td><td></td></tr><tr><td>Net profit</td><td>(5.0)</td><td>(9.4)</td><td>(9.1)</td><td>5.4</td><td>5.0</td><td>14.6</td><td>2.7</td><td>16.7</td><td>14.2</td><td>31.8</td><td>20.6</td><td></td><td></td><td></td><td></td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, company data

## GUC- Solid order visibility into 2028

We note that there is rising concern about GUC's CPU ASIC order sustainability and potential foundr

[中间内容因长度限制已省略]

lar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
