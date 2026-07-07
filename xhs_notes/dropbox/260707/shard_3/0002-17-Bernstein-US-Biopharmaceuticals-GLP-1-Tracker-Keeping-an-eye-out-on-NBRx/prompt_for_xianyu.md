你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

【研报解析内容】
"""
# US Biopharmaceuticals

# GLP-1 Tracker: Keeping an eye out on NBRx as DTC ads and Medicare start to switch on (W/E June 26th)

![](images/e16ba9f794108f39c6438aa0f032ea5ad68335cf7673b44b93868581f4659147.jpg)  
Courtney Breen
+1 917 344 8407
courtney.breen@bernsteinsg.com

![](images/1870e6fa7ce7eed94b3a591803b470de693210ffb6c79de1116557c99a57ca63.jpg)

Woody Polglase

+1 917 344 8314

woody.polglase@bernsteinsg.com

![](images/7b8064daed39ec71883bb27d622a703682a0bd21bf1b29c34e33337dde33ab7d.jpg)

Louisa Qiu

+1 917 344 8495

louisa.qiu@bernsteinsg.com

## Specialist Sales

![](images/799cb146452a7c94a6c2d94123a022bd74ac0a96d09b9ee9db2ae415546750a6.jpg)

Christian Moore

+1 917 344 8555

christian.moore@bernsteinsg.com

This week's scripts were mostly stable, with total scripts up +0.51% WoW, or +13k in absolute terms. Foundayo TRx declined sequentially week on week along with Wegovy Pill; specifically, Foundayo saw 19,831 TRx in week 12, -762 WoW and -3.7% sequentially. Wegovy Pill saw 149k TRx this week, down -2.5k sequentially, or \~-1.6%. Per LLY IR, IQVIA capture rates for the Foundayo weekly data have improved, and sat at around \~90% in Q2 (however they do fluctuate week to week). The equivalent rate for Zepbound is >90%. On NBRx, Lilly's share was 53.5%, down from 54.4% last week. As a reminder - direct to consumer advertising for Foundayo is still in its early innings, and we expect to see script inflection as customer/patient awareness increases over the months once full-blown advertising in play. Finally, reimbursement of GLP-1s for obesity in Medicare began last week ( $1^{st}$ Jul) through the GLP-1 BRIDGE program. We will be monitoring channel-level scripts (TRx/NBRx) in the coming weeks to assess the impact.

Total scripts: Total weekly scripts were 2.60M, up vs last week (+0.51%, or +13k in absolute terms). The 4-week YoY growth for sema+tirz was 33.4%, down from 35.1% last week. The company market share split on a TRx basis is now 60.6% Lilly (26.9% Zepbound, 32.9% Mounjaro, 0.8% Foundayo) to 39.4% Novo (12.7% Wegovy pen, 20.6% Ozempic, 6.0% Wegovy Pill).

New starts (NBRx): Total new starts for all GLP-1 brands remain high at 210k per week. NBRx for Foundayo now sits at 10.4k vs 38.2k for Wegovy Pill, with Foundayo having declined sequentially since a peak of 12.6k in W/E $12^{\text{th}}$ June (Exhibit 3). There has been some disruption due to holidays in recent weeks, but also not the rebound we would have expected for an early launch product. Wegovy Pill's starter dose (1.5mg) NBRx's look to be in decline (Exhibit 28). These are data points to watch, especially as broader DTC advertising and Medicare eligibility begin to switch on. Lilly's NBRx share was $53.5\%$ , down from $54.4\%$ last week.

Zepbound: Zepbound market share remained broadly stable this week at 26.9% (+0.09 pp vs last week). YoY growth on a 4-week average decreased to 52% from 57%. Absolute Zepbound prescriptions increased by +5k WoW.

Mounjaro: This week Mounjaro posted 39.1% growth on a 4-week YoY basis, roughly flat vs 39.7% last week. Market share increased marginally to 32.9% from 32.7%, and absolute prescriptions increased by +10k WoW.

Semaglutide: Growth diverges significantly by indication and presentation. Wegovy Pill had 149k TRx this week, down -2.5k sequentially, and is now in week 25 of launch. Wegovy pen's 4-week average YoY growth was 37.3%, down from 40.8% last week, with absolute Wegovy pen prescriptions up +1k WoW. Ozempic continued to decline YoY at a 4-week average of -13.1%, versus -12.8% last week. Overall, semaglutide posted 19.8% YoY growth, down from 20.7% last week.

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2"></td><td colspan="4">2 Jul 2026</td><td>TTM</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td>Rating</td><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Rel. Perf.</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>LLY (Eli Lilly)</td><td>O</td><td>USD</td><td>1,213.91</td><td>1,300.00</td><td>36.3%</td><td>USD</td><td>24.20</td><td>37.41</td><td>47.99</td><td>50.2</td><td>32.4</td><td>25.3</td></tr><tr><td>SPX</td><td></td><td></td><td>7,483.24</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended  
Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We rate LLY Outperform with a price target of \$1,300.

## Q2E AND FY26E FOUNDAYO ESTIMATES

Pricing dynamics will evolve in multiple dimensions - Cash pay patient pricing will likely increase on a blended basis, as patients move from lower to higher doses. Medicare will become a more dominant driver of market growth in H2, where all doses will be priced at \$249 once BRIDGE/BALANCE goes into effect & Commercial prices will also decline as payor coverage expands & is formalised across the three major PBMs by June $1^{st}$ .

Actual script data is still only available for the first twelve weeks of the Foundayo launch, inflections associated with fullsome patient activation (including linear TV) as well as the BRIDGE/BALANCE program create meaningful uncertainty. Ex-US launches are currently only underway for those countries which reference the US regulation (e.g. UAE), while key early launch countries (such as the UK) are likely to drive further Q4 revenue inflection outside the US.

EXHIBIT 1: Our estimates for Q2 Foundayo Revenue is \$126m, based on blended pricing and IQVIA scripts split by channel

<table><tr><td colspan="2">Scripts</td><td colspan="5">Pricing</td></tr><tr><td colspan="2"></td><td colspan="2">Cash Pay</td><td colspan="2">Reimbursed</td><td rowspan="2">Blended avg price</td></tr><tr><td colspan="2">TRx (Q2)</td><td>Cash Pay</td><td>Medicare</td><td>Medicaid</td><td>Commercial</td></tr><tr><td colspan="2">Channel TRx Split</td><td>56.8%</td><td>0.2%</td><td>0.1%</td><td>43.0%</td><td></td></tr><tr><td>0.8MG</td><td>124,283</td><td>$ 149</td><td>$ 350</td><td>$ 350</td><td>$ 489</td><td>$ 296</td></tr><tr><td>2.5MG</td><td>49,298</td><td>$ 199</td><td>$ 350</td><td>$ 350</td><td>$ 489</td><td>$ 324</td></tr><tr><td>5.5MG</td><td>10,313</td><td>$ 299</td><td>$ 350</td><td>$ 350</td><td>$ 489</td><td>$ 381</td></tr><tr><td>9MG</td><td>6,554</td><td>$ 299</td><td>$ 350</td><td>$ 350</td><td>$ 489</td><td>$ 381</td></tr><tr><td>14.5MG</td><td>2,561</td><td>$ 309</td><td>$ 350</td><td>$ 350</td><td>$ 489</td><td>$ 386</td></tr><tr><td>17.2MG</td><td>1,406</td><td>$ 309</td><td>$ 350</td><td>$ 350</td><td>$ 489</td><td>$ 386</td></tr><tr><td>Total</td><td>194,415</td><td></td><td></td><td></td><td></td><td>$ 312</td></tr><tr><td colspan="2">Revenue ($ 000s)</td><td>Cash</td><td>Medicare</td><td>Medicaid</td><td>Commercial</td><td></td></tr><tr><td>0.8MG</td><td></td><td>$ 10,510</td><td>$ 90</td><td>$ 37</td><td>$ 26,095</td><td></td></tr><tr><td>2.5MG</td><td></td><td>$ 5,568</td><td>$ 36</td><td>$ 15</td><td>$ 10,351</td><td></td></tr><tr><td>5.5MG</td><td></td><td>$ 1,750</td><td>$ 8</td><td>$ 3</td><td>$ 2,165</td><td></td></tr><tr><td>9MG</td><td></td><td>$ 1,112</td><td>$ 5</td><td>$ 2</td><td>$ 1,376</td><td></td></tr><tr><td>14.5MG</td><td></td><td>$ 449</td><td>$ 2</td><td>$ 1</td><td>$ 538</td><td></td></tr><tr><td>17.2MG</td><td></td><td>$ 247</td><td>$ 1</td><td>$ 0</td><td>$ 295</td><td></td></tr><tr><td colspan="2">Total US Revenue</td><td>$ 19,636</td><td>$ 142</td><td>$ 58</td><td>$ 40,821</td><td>$ 60,657</td></tr><tr><td colspan="6">Wegovy Pill stocking as % of Q1 revenue</td><td>43%</td></tr><tr><td colspan="6"></td><td>$ 106,415</td></tr><tr><td colspan="6">Ex-US stocking (UAE)</td><td>$ 20,000</td></tr><tr><td colspan="6">Total Global Revenue ($ 000s)</td><td>$ 126,415</td></tr></table>

Source: IQVIA, Bernstein analysis

EXHIBIT 2: Foundayo US launch is proceeding slower than we'd anticipated - based on script trajectories FY26E revenue likely to be in the range of \$1.3B

<table><tr><td rowspan="2"></td><td colspan="3">US</td><td>Ex-US</td><td>Total</td></tr><tr><td>Scripts (000s)</td><td>Avg price</td><td>Revenue ($M)</td><td>Revenue</td><td>Revenue</td></tr><tr><td>Q2E</td><td>194</td><td>$ 312</td><td>106</td><td>20</td><td>126</td></tr><tr><td>Q3E</td><td>893</td><td>$ 265</td><td>261</td><td>100</td><td>361</td></tr><tr><td>Q4E</td><td>2,285</td><td>$ 273</td><td>648</td><td>200</td><td>848</td></tr><tr><td>FY 2026E</td><td>3,372</td><td></td><td>1,016</td><td>320</td><td>1,336</td></tr></table>

Source: IQVIA, Bernstein analysis and estimates

EXHIBIT 3: TRx and NBRx in the initial weeks of launch for Zepbound, Wegovy Pill, Foundayo  
![](images/3804612e6e3d6c84371ce1b3cfe378e75aac733c3f3105b691afa017530ac067.jpg)  
Source: IQVIA, Bernstein

EXHIBIT 4: Initial weeks of launch show similar levels of continuing patients on Zepbound and Wegovy Pill, with Foundayo slightly diverging in its most recent data point

<table><tr><td>NBRx</td><td>Week 0</td><td>W+1</td><td>W+2</td><td>W+3</td><td>W+4</td><td>W+5</td><td>W+6</td><td>W+7</td><td>W+8</td><td>W+9</td><td>W+10</td><td>W+11</td><td>W+12</td></tr><tr><td>Zepbound - TRx</td><td>-</td><td>1,255</td><td>7,642</td><td>15,964</td><td>22,327</td><td>19,045</td><td>25,199</td><td>38,703</td><td>37,021</td><td>50,165</td><td>56,097</td><td>58,019</td><td>62,021</td></tr><tr><td>Zepbound - NBRx</td><td>-</td><td>1,104</td><td>7,010</td><td>14,863</td><td>20,117</td><td>15,367</td><td>17,634</td><td>25,227</td><td>22,896</td><td>29,434</td><td>29,159</td><td>27,435</td><td>26,843</td></tr><tr><td>Contribution of continuing patients (abs)</td><td></td><td>151</td><td>632</td><td>1,101</td><td>2,210</td><td>3,678</td><td>7,565</td><td>13,476</td><td>14,125</td><td>20,731</td><td>26,938</td><td>30,584</td><td>35,178</td></tr><tr><td>Contribution of continuing patients (% of TRx)</td><td></td><td>12%</td><td>8%</td><td>7%</td><td>10%</td><td>19%</td><td>30%</td><td>35%</td><td>38%</td><td>41%</td><td>48%</td><td>53%</td><td>57%</td></tr><tr><td>Wegovy Pill - TRx</td><td>-</td><td>3,071</td><td>18,410</td><td>26,109</td><td>28,515</td><td>38,220</td><td>56,943</td><td>66,748</td><td>73,544</td><td>81,184</td><td>89,279</td><td>94,654</td><td>101,388</td></tr><tr><td>Wegovy Pill - NBRx</td><td>-</td><td>2,690</td><td>16,022</td><td>22,260</td><td>23,547</td><td>29,217</td><td>39,366</td><td>44,366</td><td>45,822</td><td>46,530</td><td>45,011</td><td>44,191</td><td>45,130</td></tr><tr><td>Contribution of continuing patients (abs)</td><td></td><td>381</td><td>2,388</td><td>3,849</td><td>4,968</td><td>9,003</td><td>17,577</td><td>22,382</td><td>27,722</td><td>34,654</td><td>44,268</td><td>50,463</td><td>56,258</td></tr><tr><td>Contribution of continuing patients (% of TRx)</td><td></td><td>12%</td><td>13%</td><td>15%</td><td>17%</td><td>24%</td><td>31%</td><td>34%</td><td>38%</td><td>43%</td><td>50%</td><td>53%</td><td>55%</td></tr><tr><td>Foundayo - TRx</td><td>-</td><td>1,390</td><td>3,707</td><td>5,612</td><td>7,335</td><td>10,248</td><td>16,698</td><td>16,011</td><td>16,982</td><td>19,879</td><td>21,648</td><td>20,593</td><td>19,831</td></tr><tr><td>Foundayo - NBRx</td><td>-</td><td>1,381</td><td>3,641</td><td>5,494</td><td>6,710</td><td>8,578</td><td>12,078</td><td>10,475</td><td>9,911</td><td>12,195</td><td>12,574</td><td>11,992</td><td></td></tr><tr><td>Contribution of continuing patients (abs)</td><td></td><td>9</td><td>66</td><td>118</td><td>625</td><td>1,670</td><td>4,620</td><td>5,536</td><td>7,071</td><td>7,684</td><td>9,074</td><td>8,601</td><td></td></tr><tr><td>Contribution of continuing patients (% of TRx)</td><td></td><td>1%</td><td>2%</td><td>2%</td><td>9%</td><td>16%</td><td>28%</td><td>35%</td><td>42%</td><td>39%</td><td>42%</td><td>42%</td><td></td></tr></table>

<table><tr><td>NBRx</td><td>W+13</td><td>W+14</td><td>W+15</td><td>W+16</td><td>W+17</td><td>W+18</td><td>W+19</td><td>W+20</td><td>W+21</td><td>W+22</td><td>W+23</td><td>W+24</td><td>W+25</td></tr><tr><td>Zepbound - TRx</td><td>58,019</td><td>62,021</td><td>59,253</td><td>64,858</td><td>87,744</td><td>92,710</td><td>79,223</td><td>59,821</td><td>86,544</td><td>87,106</td><td>58,447</td><td>73,097</td><td>68,970</td></tr><tr><td>Zepbound - NBRx</td><td>27,435</td><td>26,843</td><td>23,577</td><td>24,004</td><td>33,204</td><td>35,490</td><td>28,744</td><td>20,786</td><td>26,801</td><td>30,576</td><td>19,990</td><td>26,009</td><td>21,687</td></tr><tr><td>Contribution of continuing patients (abs)</td><td>30,584</td><td>35,178</td><td>35,676</td><td>40,854</td><td>54,540</td><td>57,220</td><td>50,479</td><td>39,035</td><td>59,743</td><td>56,530</td><td>38,457</td><td>47,088</td><td>47,283</td></tr><tr><td>Contribution of continuing patients (% of TRx)</td><td>53%</td><td>57%</td><td>60%</td><td>63%</td><td>62%</td><td>62%</td><td>64%</td><td>65%</td><td>69%</td><td>65%</td><td>66%</td><td>64%</td><td>69%</td></tr><tr><td>Wegovy Pill - TRx</td><td>94,654</td><td>101,388</td><td>105,366</td><td>113,354</td><td>124,608</td><td>134,751</td><td>143,611</td><td>137,333</td><td>142,959</td><td>145,922</td><td>134,054</td><td>159,415</td><td>161,525</td></tr><tr><td>Wegovy Pill - NBRx</td><td>44,191</td><td>45,130</td><td>44,439</td><td>45,680</td><td>45,910</td><td>49,004</td><td>49,607</td><td>45,299</td><td>47,344</td><td>45,219</td><td>39,978</td><td>48,770</td><td>45,880</td></tr><tr><td>Contribution of continuing patients (abs)</td><td>50,463</td><td>56,258</td><td>60,927</td><td>67,674</td><td>78,698</td><td>85,747</td><td>94,004</td><td>92,034</td><td>95,615</td><td>100,703</td><td>94,076</td><td>110,645</td><td>115,645</td></tr><tr><td>Contribution of continuing patients (% of TRx)</td><td>53%</td><td>55%</td><td>58%</td><td>60%</td><td>63%</td><td>64%</td><td>65%</td><td>67%</td><td>67%</td><td>69%</td><td>70%</td><td>69%</td><td>72%</td></tr><tr><td>Foundayo - TRx</td><td colspan="13"></td></tr><tr><td>Foundayo - NBRx</td><td colspan="13"></td></tr><tr><td>Contribution of continuing patients (abs)</td><td colspan="13"></td></tr><tr><td>Contribution of continuing patients (% of TRx)</td><td colspan="13"></td></tr></table>

Source: IQVIA, Bernstein analysis

EXHIBIT 5: Whilst previously tracking in-line with Zepbound/Wegovy, recent data points show fewer continuing patients on Foundayo as a % of total scripts. Something to continue to monitor as data can be patchy  
![](images/385061377d898a32169c1c240061fdde92cc4562cc18f437d3025e6c3d75881b.jpg)  
Source: IQVIA, Bernstein analysis

## ORAL GLP-1 LAUNCH DYNAMICS

Early, daily-to-weekly script conversion for Foundayo seems to correlate (Exhibit 12), but large gaps in conversion of absolute daily TRx into weekly numbers continue (Exhibit 14). However, based on Lilly's earnings commentary, we continue to view oral GLP-1s as market-expanding, and previously estimated the IQVIA capture rate for Foundayo at \~70%. IR has now said that in aggregate Foundayo's capture rate in IQVIA is around 90% now. We agree with management that this launch is likely to play out over months, not weeks, for a couple of reasons: (1) this is an entirely new molecule (Wegovy Pill is a sema line extension), and requires greater physician education, and (2) given this, DTC advertising is unable to begin until physicians have been sufficiently educated, meaning DTC ads, including TV, won't start in full-force until Q3 (a few began to air - including during the World Cup &

NBA Finals - towards the end of Q2).

At the 2026 Novo AGM, Novo (covered by Justin Smith) reported that weekly Wegovy pill TRx were 3x higher than tirzepatide at week 10, whereas IQVIA prescription data suggested 1.6× (assuming tirzepatide = Zepb

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
