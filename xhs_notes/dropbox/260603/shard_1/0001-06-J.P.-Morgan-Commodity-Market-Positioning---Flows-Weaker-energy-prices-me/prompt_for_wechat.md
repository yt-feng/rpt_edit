你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：一句主判断，不超过 32 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Commodity Market Positioning & Flows

Weaker energy prices meet gold-led net outflows

- The estimated value of open interest across tracked commodity markets decreased by 4% WoW (\$69 billion) to \$1.82 trillion as of May 29 (Table 2, Figure 2). The decline was primarily driven by lower energy prices (ex. US natural gas) and \$22 billion of outflows from gold markets across all trader types. Higher energy prices are now finding their way into the headline inflation forecasts by our economists, however global (ex. China) core inflation is still expected to remain “sticky” at around 3%. This potentially increases pressure on the Fed to tighten, but expectations for a mix of easing and stability elsewhere have shifted to a projection for a broad but shallow global tightening cycle over the coming year (Global Data Watch: Tenor madness, Kasman et al, 29 May 2026).   
- The estimated value of net investor positioning aggregated across global commodity futures markets decreased by 8% WoW (\$20 billion WoW) to \$223 billion as of the latest data available (Table 1, Figure 3, Figure 4). The decline was largely driven by the energy and agri markets. Net length in energy markets declined by \$9 billion WoW, primarily driven by the decline across crude oil, where net length decreased from \$61 billion to \$51 billion over the week, followed by a \$1.4 billion net shortening in TTF natural gas. Net length in agri markets declined by \$6.5 billion WoW, driven by a decline across corn, soybean and livestock markets. Net length in precious metals decreased by \$3.5 billion WoW, led by gold (-\$2.7 billion WoW), while net length in base metals decreased by \$1.5 billion WoW, driven by copper and aluminum. JPM QDS's latest projections, as of June 1, indicate that positioning across commodity markets is expected to decline by a further \$2.6 billion, largely driven by energy markets.   
- The estimated value of open interest in energy markets decreased by 6% WoW (\$56 billion WoW) to \$816 billion (29 May, Figure 6). This was driven by a decline in prices across the crude oil and petroleum products markets over the week (Brent down 11% WoW, WTI down 10%, ICE Gasoil down 11%), in addition to net contract-based outflows of \$14 billion, primarily from the crude oil markets. We estimate a 9% decline in China's oil demand, with limited decline in underlying economic activity—with a portion of the loss in gasoline, diesel, and fuel oil demand likely to persist, as jet fuel and naphta will largely recover. The estimated value of open interest in natural gas markets decreased by 3% over the week to \$175 billion (29 May, Figure 13). This was driven by a decline in prices across European and Asian benchmarks and net contract-based outflows of \$3 billion, partially offset by an increase in the US natural gas prices over the week. We estimate that the global LNG market has absorbed about 60% of the Hormuz-driven supply shock through increased output from new projects in North America and Africa, keeping spot prices relatively stable. However, with market flexibility now fading and European storage levels well below average, we expect prices to rise into peak injection season to accelerate gas-to-coal switching in Europe and soften Asian spot LNG demand, ultimately supporting Europe's storage trajectory.   
- The estimated value of open interest in precious metals markets declined by 8%

# Global Commodities Research

# Otar Dgebuadze, CFA

(44-20) 3493-8246

otar.dgebuadze@JPM.com

JPM Securities plc

# Natasha Kaneva

(1-212) 834-3175

natasha.kaneva@JPM.com

JPM Chase Bank NA

# Gregory C. Shearer

(44-20) 7134-8161

gregory.c.shearer@JPM.com

JPM Securities plc

# Tracey Allen

(44-20) 7134-6732

tracey.l.allen@JPM.com

JPM Securities plc

# Ali A. Ibrahim

(44-20) 3493-6438

ali.ibrahim@JPM.com

JPM Securities plc

# Aradhaya Makkar

aradhaya.makkar@jpmchase.com

JPM India Private Limited

# Ananyashree Gupta

(91-22) 6157 3627

ananyashree.gupta@jpmchase.com

JPM India Private Limited

WoW (\$22 billion) to \$264 billion, falling for the third straight week (29 May, Figure 8). Across all trader types, the sector saw strong net contract-based outflows totalling \$22 billion WoW, primarily from gold (\$22 billion WoW). Meanwhile, net Managed Money positioning in COMEX Gold futures increased by 3.9k contracts to a total of 97.4k contracts net long. Global gold ETF holdings now sit at 4,131 tonnes (+3% YTD), despite another wave of selling in April and May.

- The estimated value of open interest in base metals markets increased by 1% WoW (\$1.8 billion) to \$239 billion (29 May, Figure 9). The sector saw net contract-based inflows across all trader types, as the outflows from aluminium (-\$0.9 billion WoW) and zinc (-\$0.3 billion) markets have been more than offset by inflows in copper (+\$2.3 billion WoW). Supply disappointments and disruptions have swelled once again in 2026, supporting a higher-for-longer zinc price environment despite still-lifeless demand. LME zinc prices are expected to remain in a higher for longer range of \$3,400–\$3,500/mt on average over the balance of 2026 to incentivize Chinese exports, though risks are skewed towards a quicker cooling over 2H26 as Chinese exports could overshoot while inflationary pressures risk curbing demand more sharply than our forecast.   
- The estimated value of open interest across environmental markets increased by 7% WoW (\$5 billion) to \$76 billion WoW (29 May, Figure 7). This was driven by a 5% increase in the EUA prices, further supported by net contract-based inflows of \$1 billion, primarily into the EUA market. Investment Funds increased their net long position across EUAs as of 22 May to 38,981 lots, up by 422 lots WoW.   
- The estimated value of open interest in agricultural markets remained largely stable over the week at \$393 billion (29 May, Figure 10, Figure 14), as net contract-based inflows of \$4 billion, primarily into the soybean markets, were broadly offset by a decline in prices across corn, wheat, sugar and cotton markets.   
- Price momentum largely decreased across most of the complex over the week (29 May, Figure 17, Figure 18). The short-term price momentum trading signals on Gasoil, TTF, Soybeans and Sugar switched negative to a ‘sell’ signal during the week.

See Agricultural Commodities CFTC COT Report for relevant supplemental data across agricultural markets.

Table 1: Net investor positioning across tracked commodity markets   
USD million 

<table><tr><td rowspan="2"></td><td rowspan="2"># of markets / Last reported date</td><td rowspan="2">Last reported value</td><td rowspan="2">Latest projection 01-Jun-26</td><td rowspan="2">Projection vs last reported</td><td colspan="4">Change in Positioning (reported)</td></tr><tr><td>1 Week</td><td>1 Month</td><td>3 Months</td><td>2026 YTD</td></tr><tr><td>Total Commodities</td><td>33</td><td>222,598</td><td>220,047</td><td>-2,551</td><td>-20,240</td><td>-11,476</td><td>39,593</td><td>29,109</td></tr><tr><td>Energy</td><td>8</td><td>43,207</td><td>40,831</td><td>-2,376</td><td>-9,039</td><td>-9,364</td><td>32,168</td><td>44,495</td></tr><tr><td>Crude Oil</td><td>3</td><td>51,192</td><td>49,725</td><td>-1,467</td><td>-10,206</td><td>-13,350</td><td>28,869</td><td>37,311</td></tr><tr><td>ICE Brent</td><td>26-May-26</td><td>21,843</td><td>20,886</td><td>-958</td><td>-8,223</td><td>-10,867</td><td>26,568</td><td>26,917</td></tr><tr><td>NYMEX WTI</td><td>26-May-26</td><td>15,116</td><td>14,607</td><td>-509</td><td>-3,483</td><td>-4,062</td><td>2,281</td><td>11,320</td></tr><tr><td>ICE Dubai</td><td>26-May-26</td><td>14,233</td><td>na</td><td>na</td><td>1,499</td><td>1,579</td><td>20</td><td>-926</td></tr><tr><td>Petroleum Products</td><td>3</td><td>-17,990</td><td>-18,417</td><td>-427</td><td>2,489</td><td>3,630</td><td>-8,389</td><td>-12,143</td></tr><tr><td>NYMEX Gasoline</td><td>26-May-26</td><td>7,389</td><td>7,223</td><td>-165</td><td>-517</td><td>-1,017</td><td>-2,088</td><td>2,037</td></tr><tr><td>ICE Gasoil</td><td>26-May-26</td><td>-25,785</td><td>na</td><td>na</td><td>3,586</td><td>4,853</td><td>-4,345</td><td>-12,970</td></tr><tr><td>NYMEX Heat Oil</td><td>26-May-26</td><td>407</td><td>145</td><td>-262</td><td>-580</td><td>-205</td><td>-1,956</td><td>-1,210</td></tr><tr><td>Natural Gas</td><td>2</td><td>10,005</td><td>9,523</td><td>-482</td><td>-1,321</td><td>356</td><td>11,689</td><td>19,327</td></tr><tr><td>NYMEX Natgas</td><td>26-May-26</td><td>-5,880</td><td>-6,362</td><td>-482</td><td>105</td><td>-1,625</td><td>424</td><td>359</td></tr><tr><td>TTF Natgas</td><td>22-May-26</td><td>15,885</td><td>na</td><td>na</td><td>-1,426</td><td>1,981</td><td>11,265</td><td>18,968</td></tr><tr><td>Environmental</td><td>2</td><td>5,256</td><td>5,256</td><td>0</td><td>286</td><td>405</td><td>-1,406</td><td>-8,691</td></tr><tr><td>EUA</td><td>22-May-26</td><td>3,650</td><td>na</td><td>na</td><td>107</td><td>161</td><td>-1,763</td><td>-8,613</td></tr><tr><td>UKA</td><td>22-May-26</td><td>1,605</td><td>na</td><td>na</td><td>179</td><td>244</td><td>357</td><td>-79</td></tr><tr><td>Metals</td><td>10</td><td>132,934</td><td>133,805</td><td>871</td><td>-5,008</td><td>3,433</td><td>-4,815</td><td>-33,898</td></tr><tr><td>Precious</td><td>4</td><td>79,253</td><td>79,280</td><td>27</td><td>-3,482</td><td>-4,445</td><td>-13,938</td><td>-37,399</td></tr><tr><td>CMX Gold</td><td>26-May-26</td><td>69,452</td><td>69,848</td><td>396</td><td>-2,651</td><td>-3,815</td><td>-12,601</td><td>-33,379</td></tr><tr><td>CMX Silver</td><td>26-May-26</td><td>8,479</td><td>8,165</td><td>-314</td><td>-752</td><td>-366</td><td>-1,198</td><td>-3,399</td></tr><tr><td>NYMX Platinum</td><td>26-May-26</td><td>1,723</td><td>1,672</td><td>-51</td><td>-18</td><td>-78</td><td>288</td><td>-319</td></tr><tr><td>NYMX Palladium</td><td>26-May-26</td><td>-401</td><td>-405</td><td>-4</td><td>-61</td><td>-186</td><td>-427</td><td>-301</td></tr><tr><td>Base</td><td>6</td><td>53,681</td><td>54,525</td><td>844</td><td>-1,526</td><td>7,878</td><td>9,123</td><td>3,500</td></tr><tr><td>CMX Copper</td><td>26-May-26</td><td>11,615</td><td>12,459</td><td>844</td><td>-81</td><td>2,254</td><td>3,290</td><td>2,844</td></tr><tr><td>LME Copper</td><td>29-May-26</td><td>14,270</td><td>na</td><td>na</td><td>-955</td><td>2,024</td><td>2,621</td><td>-8,084</td></tr><tr><td>LME Aluminum</td><td>29-May-26</td><td>19,587</td><td>na</td><td>na</td><td>-770</td><td>2,104</td><td>943</td><td>5,495</td></tr><tr><td>LME Zinc</td><td>29-May-26</td><td>4,143</td><td>na</td><td>na</td><td>43</td><td>977</td><td>804</td><td>1,478</td></tr><tr><td>LME Nickel</td><td>29-May-26</td><td>4,188</td><td>na</td><td>na</td><td>-33</td><td>-437</td><td>568</td><td>1,290</td></tr><tr><td>LME Lead</td><td>29-May-26</td><td>-123</td><td>na</td><td>na</td><td>269</td><td>957</td><td>897</td><td>477</td></tr><tr><td>Agriculture</td><td>13</td><td>41,201</td><td>40,155</td><td>-1,045</td><td>-6,480</td><td>-5,950</td><td>13,645</td><td>27,203</td></tr><tr><td>Grains</td><td>6</td><td>30,083</td><td>30,013</td><td>-70</td><td>-3,926</td><td>-2,022</td><td>11,003</td><td>26,189</td></tr><tr><td>CBT Corn</td><td>26-May-26</td><td>6,908</td><td>6,013</td><td>-895</td><td>-1,601</td><td>-1,018</td><td>4,953</td><td>5,720</td></tr><tr><td>CBT Wheat</td><td>26-May-26</td><td>-301</td><td>-498</td><td>-198</td><td>-309</td><td>-329</td><td>444</td><td>1,538</td></tr><tr><td>KBT Wheat</td><td>26-May-26</td><td>-59</td><td>-265</td><td>-206</td><td>-249</td><td>-499</td><td>-110</td><td>-11</td></tr><tr><td>CBT Soy beans</td><td>26-May-26</td><td>12,137</td><td>12,205</td><td>68</td><td>-698</td><td>763</td><td>-686</td><td>5,675</td></tr><tr><td>CBT Soy Meal</td><td>26-May-26</td><td>5,080</td><td>5,026</td><td>-54</td><td>-228</td><td>309</td><td>2,821</td><td>5,151</td></tr><tr><td>CBT Soy Oil</td><td>26-May-26</td><td>6,316</td><td>7,533</td><td>1,216</td><td>-840</td><td>-1,248</td><td>3,582</td><td>8,116</td></tr><tr><td>Softs</td><td>4</td><td>3,125</td><td>2,350</td><td>-775</td><td>-367</td><td>176</td><td>7,179</td><td>2,995</td></tr><tr><td>ICE Cotton</td><td>26-May-26</td><td>3,392</td><td>3,259</td><td>-133</td><td>-415</td><td>262</td><td>4,263</td><td>4,401</td></tr><tr><td>ICE Sugar</td><td>26-May-26</td><td>-1,299</td><td>-1,539</td><td>-240</td><td>28</td><td>976</td><td>2,524</td><td>1,024</td></tr><tr><td>ICE Coffee</td><td>26-May-26</td><td>1,709</td><td>1,393</td><td>-316</td><td>92</td><td>-1,167</td><td>547</td><td>-1,560</td></tr><tr><td>ICE Cocoa</td><td>26-May-26</td><td>-677</td><td>-763</td><td>-86</td><td>-72</td><td>104</td><td>-156</td><td>-871</td></tr><tr><td>Livestock</td><td>3</td><td>7,993</td><td>7,792</td><td>-201</td><td>-2,187</td><td>-4,103</td><td>-4,536</td><td>-1,981</td></tr><tr><td>CME Live Cattle</td><td>26-May-26</td><td>8,622</td><td>8,587</td><td>-35</td><td>-632</td><td>-1,519</td><td>395</td><td>1,290</td></tr><tr><td>CME Lean Hogs</td><td>26-May-26</td><td>-908</td><td>-983</td><td>-76</td><td>-626</td><td>-1,517</td><td>-3,779</td><td>-2,340</td></tr><tr><td>CME Feeder Cattle</td><td>26-May-26</td><td>279</td><td>188</td><td>-91</td><td>-929</td><td>-1,067</td><td>-1,152</td><td>-930</td></tr></table>

<table><tr><td>Total Regions</td><td>33</td><td>222,598</td><td>220,047</td><td>-2,551</td><td>-20,240</td><td>-11,476</td><td>39,593</td><td>29,109</td></tr><tr><td>US</td><td>22</td><td>149,101</td><td>147,508</td><td>-1,593</td><td>-14,518</td><td>-15,051</td><td>1,657</td><td>5,155</td></tr><tr><td>UK</td><td>9</td><td>53,961</td><td>53,004</td><td>-958</td><td>-4,404</td><td>1,432</td><td>28,433</td><td>13,599</td></tr><tr><td>EU</td><td>2</td><td>19,536</td><td>19,536</td><td>0</td><td>-1,319</td><td>2,142</td><td>9,502</td><td>10,355</td></tr></table>

Where projections are not available, latest reported values are used for totals   
Projections by JPM QDS Research; US exchanges data is an aggregate of Managed Money and Other Reportables, European exchanges data is an aggregate of Investment Funds and Other Financial Firms.   
Source: Exchange data, Bloomberg Finance L.P., JPM QDS and Commodities Research

Table 2: The estimated value of commodity market open interest across major global exchanges reached \$1.82 trillion in the week ending 29 May USD million 

<table><tr><td rowspan="2">Sector</td><td>Number of futures markets</td><td>Total estimated Open Interest</td><td colspan="4">Change in Open Interest</td><td colspan="4">Cumulative flows</td><td colspan="5">Tracked Open Interest by location of exchange (% of global total)</td></tr><tr><td>Count</td><td>29-May-26</td><td>1 Week</td><td>1 Month</td><td>3 Months</td><td>2026 YTD</td><td>1 Week</td><td>1 Month</td><td>3 Months</td><td>2026 YTD</td><td>US</td><td>UK</td><td>EU</td><td>China</td><td>RoW</td></tr><tr><td>Total commodities</td><td>91</td><td>1,822,559</td><td>-69,238</td><td>-40,537</td><td>-94,468</td><td>116,348</td><td>-34,239</td><td>-607</td><td>-135,940</td><td>-212,061</td><td>45%</td><td>32%</td><td>9%</td><td>12%</td><td>1%</td></tr><tr><td>Energy</td><td>18</td><td>816,478</td><td>-55,631</td><td>-55,444</td><td>-51,880</td><td>155,842</td><td>-16,773</td><td>-9,291</td><td>-93,871</td><td>-113,275</td><td>35%</td><td>51%</td><td>9%</td><td>1%</td><td>0%</td></tr><tr><td>Crude Oil</td><td>7</td><td>491,350</td><td>-36,356</td><td>-37,871</td><td>-17,969</td><td>112,725</td><td>-10,613</td><td>-7,784</td><td>-54,709</td><td>-53,601</td><td>32%</td><td>66%</td><td>0%</td><td>1%</td><td>1%</td></tr><tr><td>Petroleum Products</td><td>7</td><td>149,921</td><td>-13,927</td><td>-19,070</td><td>-17,738</td><td>23,887</td><td>-3,058</td><td>-5,124</td><td>-33,313</td><td>-47,799</td><td>47%</td><td>52%</td><td>0%</td><td>1%</td><td>0%</td></tr><tr><td>Natural Gas</td><td>4</td><td>175,208</td><td>-5,348</td><td>1,497</td><td>-16,173</td><td>19,229</td><td>-3,102</td><td>3,618</td><td>-5,848</td><td>-11,874</td><td>34%</td><td>9%</td><td>41%</td><td>0%</td><td>0%</td></tr><tr><td>Environmental</td><td>3</td><td>75,672</td><td>5,030</td><td>9,307</td><td>11,686</td><td>4,046</td><td>1,049</td><td>3,146</td><td>1,416</td><td>11,193</td><td>0%</td><td>0%</td><td>100%</td><td>0%</td><td>0%</td></tr><tr><td>EU Allowances</td><td>2</td><td>70,957</td><td>4,621</td><td>8,373</td><td>10,287</td><td>3,970</td><td>1,067</td><td>2,879</td><td>1,483</td><td>10,305</td><td>0%</td><td>0%</td><td>100%</td><td>0%</td><td>0%</td></tr><tr><td>UK ETS</td><td>1</td><td>4,715</td><td>408</td><td>934</td><td>1,399</td><td>77</td><td>-17</td><td>267</td><td>-67</td><td>888</td><td>0%</td><td>0%</td><td>100%</td><td>0%</td><td>0%</td></tr><tr><td>Metals</td><td>34</td><td>537,350</td><td>-20,402</td><td>-4,132</td><td>-77,538</td><td>-119,460</td><td>-22,446</td><td>-10,538</td><td>-54,199</td><td>-164,884</td><td>44%</td><td>27%</td><td>0%</td><td>28%</td><td>2%</td></tr><tr><td>Precious</td><td>15</td><td>264,249</td><td>-21,709</td><td>-21,538</td><td>-82,642</td><td>-122,941</td><td>-22,135</td><td>-17,240</td><td>-42,556</td><td>-133,883</td><td>74%</td><td>0%</td><td>0%</td><td>24%</td><td>3%</td></tr><tr><td>Base</td><td>13</td><td>239,215</td><td>1,760</td><td>16,164</td><td>2,073</td><td>-1,385</td><td>743</td><td>6,086</td><td>-12,030</td><td>-31,725</td><td>17%</td><td>59%</td><td>0%</td><td>24%</td><td>0%</td></tr><tr><td>Bulk</td><td>6</td><td>33,886</td><td>-452</td><td>1,242</td><td>3,031</td><td>4,867</td><td>-1,054</td><td>616</td><td>387</td><td>724</td><td>0%</td><td>10%</td><td>0%</td><td>90%</td><td>0%</td></tr><tr><td>Agriculture</td><td>36</td><td>393,058</td><td>1,766</td><td>9,732</td><td>23,263</td><td>75,919</td><td>3,931</td><td>16,075</td><td>10,715</td><td>54,905</td><td>77%</td><td>4%</td><td>3%</td><td>16%</td><td>0%</td></tr><tr><td>Grains &amp; Oilseeds</td><td>17</td><td>240,365</td><td>2,594</td><td>15,220</td><td>22,078</td><td>66,710</td><td>3,987</td><td>16,282</td><td>13,106</td><td>39,355</td><td>78%</td><td>0%</td><td>2%</td><td>19%</td><td>0%</td></tr><tr><td>Softs</td><td>15</td><td>96,966</td><td>601</td><td>-253</td><td>6,500</td><td>6,102</td><td>1,071</td><td>1,966</td><td>1,640</td><td>12,578</td><td>60%</td><td>16%</td><td>6%</td><td>18%</td><td>0%</td></tr><tr><td>Livestock</td><td>4</td><td>55,727</td><td>-1,429</td><td>-5,235</td><td>-5,315</td><td>3,107</td><td>-1,127</td><td>-2,173</td><td>-4,031</td><td>2,972</td><td>98%</td><td>0%</td><td>0%</td><td>0%</td><td>2%</td></tr><tr><td colspan="16"></td></tr><tr><td

[中间内容因长度限制已省略]

pdates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 02 Jun 2026 07:12 PM BST

Disseminated 02 Jun 2026 07:12 PM BST
"""
