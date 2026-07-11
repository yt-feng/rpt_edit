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
## E-Town Semis (688729.SS): Riding on memory and advanced node capacity expansion in local market; maintain Neutral on fair valuation

We remain positive on the China Semi supply chain, riding on rising advanced node capacity expansion and the generative AI trend supporting China semis ecosystem development. Media reports (Link) of a long-term supply agreement between CXMT and Tencent for server DRAM chips indicate strong demand from local clients and mix upgrade towards high-end applications. We expect E-Town to benefit from the China Semi capex uptrend, along with its supply chain switching to China suppliers, driving the company's revenue growth and profitability improvement. The company's 1Q26 GM was higher than our estimate, representing 3 consecutive quarters with GM over $40\%$ , while 1Q26 revenue was lower than our estimate, which we attribute to new products' ramp up taking more time. We maintain our Neutral rating as we believe the positives are largely priced in.

Earnings revision: We factor in E-Town's 4Q25 and 1Q26 results and revise down our 2026E net income by $5\%$ , mainly on lower revenues. We lower our 2026E revenue to reflect the 1Q26 revenue miss due to new products' ramp up taking more time, but raise 2027-28E revenues as we expect E-Town to benefit from memory and advanced node capacity expansion in the local market. We raise our 2026-28E GMs to reflect the company moving its supply chain to China suppliers. Our 2026-28E opex ratios are largely unchanged, leading to 2026-28E net incomes $-5\% / +4\% / +6\%$ .

Exhibit 1: Earnings revision

<table><tr><td rowspan="2">Rmb mn</td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td>Old</td><td>New</td><td>Chg</td><td>Old</td><td>New</td><td>Chg</td><td>Old</td><td>New</td><td>Chg</td></tr><tr><td>Revenue</td><td>7,131</td><td>6,204</td><td>-13%</td><td>8,762</td><td>8,938</td><td>2%</td><td>9,936</td><td>10,231</td><td>3%</td></tr><tr><td>GP</td><td>2,747</td><td>2,465</td><td>-10%</td><td>3,438</td><td>3,584</td><td>4%</td><td>3,921</td><td>4,136</td><td>5%</td></tr><tr><td>OP</td><td>1,337</td><td>1,185</td><td>-11%</td><td>1,979</td><td>2,078</td><td>5%</td><td>2,317</td><td>2,463</td><td>6%</td></tr><tr><td>Net income</td><td>1,298</td><td>1,235</td><td>-5%</td><td>1,877</td><td>1,950</td><td>4%</td><td>2,173</td><td>2,294</td><td>6%</td></tr><tr><td>Margins</td><td colspan="3"></td><td colspan="3"></td><td colspan="3"></td></tr><tr><td>GM</td><td>38.5%</td><td>39.7%</td><td></td><td>39.2%</td><td>40.1%</td><td></td><td>39.5%</td><td>40.4%</td><td></td></tr><tr><td>OPM</td><td>18.7%</td><td>19.1%</td><td></td><td>22.6%</td><td>23.3%</td><td></td><td>23.3%</td><td>24.1%</td><td></td></tr><tr><td>NM</td><td>18.2%</td><td>19.9%</td><td></td><td>21.4%</td><td>21.8%</td><td></td><td>21.9%</td><td>22.4%</td><td></td></tr></table>

Source: Company data, GS Global Investment Research

Valuation: We roll over our base year to 2027E and continue to use a near-term P/E to derive our 12M TP. Our 2027E target P/E is updated to 49.9x (vs. 45.9x previously), which is derived from peers' correlation of 2027E P/E to 2027-28E avg. EPS growth, and reflects the sector re-rating on memory and advanced node capacity expansion and rising AI related end demand. With the updated target multiple and earnings estimates, our 12M TP is updated to Rmb32.9 (vs. Rmb28.9 previously). Our new TP

Allen Chang  
+852-2978-2930 |  
allen.k.chang@gs.com  
GS (Asia) L.L.C.

Verena Jeng
+852-2978-1681 | verena.jeng@gs.com
GS (Asia) L.L.C.

Yifan Hu  
+852-2978-0996 | yifan.hu@gs.com  
GS (Asia) L.L.C.

implied PEG is at 1.3x, within peers' range of 0.9x to 1.8x. The stock currently trades at 57.9x 2027E P/E, vs. our 2027E target P/E at 49.9x, implying the positives are largely priced in. Maintain Neutral.

Exhibit 2: Peers' correlation of 2027E P/E to 2027-28E avg. EPS growth  
![](images/d94cd59c66a1234c1f4429e4a1a3479b89742ab867698ef70efdeda3970bd4f1.jpg)  
Source: Company data, GS Global Investment Research, Refinitiv Eikon

Exhibit 3: E-Town Semis 12M forward P/E  
![](images/ea38aeae9d38e5f2065af35e446990c044f457c1c397e35b63d5c203972913ec.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 4: E-Town and peers' PEG

<table><tr><td></td><td>Ticker</td><td>Rating</td><td>2027E PE</td><td>2027-28E avg. EPS growth</td><td>PEG</td></tr><tr><td>NAURA</td><td>002371.SZ</td><td>Buy</td><td>43.3</td><td>50%</td><td>0.9</td></tr><tr><td>Piotech</td><td>688072.SS</td><td>NC</td><td>91.5</td><td>51%</td><td>1.8</td></tr><tr><td>Hwatsing</td><td>688120.SS</td><td>Neutral</td><td>49.5</td><td>29%</td><td>1.7</td></tr><tr><td>Lam Research</td><td>LRCX</td><td>Buy</td><td>42.6</td><td>30%</td><td>1.4</td></tr><tr><td>E-Town Semi</td><td>688729.SS</td><td>Neutral</td><td>49.9</td><td>38%</td><td>1.3</td></tr></table>

Source: Company data, GS Global Investment Research, Refinitiv Eikon

Exhibit 5: E-Town P&L summary

<table><tr><td>Rmb m</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td></tr><tr><td colspan="18">Income statement</td></tr><tr><td>Revenues</td><td>1,160</td><td>1,322</td><td>1,314</td><td>1,280</td><td>1,037</td><td>1,230</td><td>1,962</td><td>1,975</td><td>4,763</td><td>3,931</td><td>4,633</td><td>5,076</td><td>6,204</td><td>8,938</td><td>10,231</td><td>11,317</td><td>12,318</td></tr><tr><td>GP</td><td>413</td><td>478</td><td>528</td><td>523</td><td>415</td><td>488</td><td>778</td><td>784</td><td>1,358</td><td>1,377</td><td>1,732</td><td>1,942</td><td>2,465</td><td>3,584</td><td>4,136</td><td>4,573</td><td>4,984</td></tr><tr><td>OP</td><td>97</td><td>134</td><td>202</td><td>183</td><td>114</td><td>166</td><td>450</td><td>455</td><td>385</td><td>275</td><td>494</td><td>615</td><td>1,185</td><td>2,078</td><td>2,463</td><td>2,734</td><td>3,031</td></tr><tr><td>Net income</td><td>218</td><td>130</td><td>168</td><td>155</td><td>159</td><td>168</td><td>452</td><td>455</td><td>383</td><td>309</td><td>541</td><td>671</td><td>1,235</td><td>1,950</td><td>2,294</td><td>2,514</td><td>2,765</td></tr><tr><td>EPS (Rmb)</td><td>0.07</td><td>0.04</td><td>0.06</td><td>0.05</td><td>0.05</td><td>0.06</td><td>0.15</td><td>0.15</td><td>0.14</td><td>0.12</td><td>0.20</td><td>0.23</td><td>0.42</td><td>0.66</td><td>0.78</td><td>0.85</td><td>0.94</td></tr><tr><td colspan="18">Margins</td></tr><tr><td>GM</td><td>35.6%</td><td>36.1%</td><td>40.1%</td><td>40.9%</td><td>40.0%</td><td>39.7%</td><td>39.6%</td><td>39.7%</td><td>28.5%</td><td>35.0%</td><td>37.4%</td><td>38.3%</td><td>39.7%</td><td>40.1%</td><td>40.4%</td><td>40.4%</td><td>40.5%</td></tr><tr><td>OPM</td><td>8.4%</td><td>10.1%</td><td>15.3%</td><td>14.3%</td><td>11.0%</td><td>13.5%</td><td>23.0%</td><td>23.0%</td><td>8.1%</td><td>7.0%</td><td>10.7%</td><td>12.1%</td><td>19.1%</td><td>23.3%</td><td>24.1%</td><td>24.2%</td><td>24.6%</td></tr><tr><td>NM</td><td>18.8%</td><td>9.9%</td><td>12.8%</td><td>12.1%</td><td>15.4%</td><td>13.6%</td><td>23.1%</td><td>23.1%</td><td>8.0%</td><td>7.9%</td><td>11.7%</td><td>13.2%</td><td>19.9%</td><td>21.8%</td><td>22.4%</td><td>22.2%</td><td>22.4%</td></tr><tr><td colspan="18">Ratios</td></tr><tr><td>Opex ratio</td><td>27.3%</td><td>26.0%</td><td>24.8%</td><td>26.6%</td><td>29.0%</td><td>26.2%</td><td>16.7%</td><td>16.7%</td><td>20.4%</td><td>28.0%</td><td>26.7%</td><td>26.1%</td><td>20.6%</td><td>16.9%</td><td>16.4%</td><td>16.3%</td><td>15.9%</td></tr><tr><td>Tax rate</td><td>-19.0%</td><td>-0.4%</td><td>17.1%</td><td>6.2%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>4.4%</td><td>-16.8%</td><td>-5.6%</td><td>1.4%</td><td>0.0%</td><td>7.2%</td><td>8.0%</td><td>9.0%</td><td>10.0%</td></tr><tr><td colspan="18">YoY</td></tr><tr><td>Revenues</td><td>15%</td><td>23%</td><td>6%</td><td>-2%</td><td>-11%</td><td>-7%</td><td>49%</td><td>54%</td><td>47%</td><td>-17%</td><td>18%</td><td>10%</td><td>22%</td><td>44%</td><td>14%</td><td>11%</td><td>9%</td></tr><tr><td>GP</td><td>12%</td><td>4%</td><td>12%</td><td>22%</td><td>0%</td><td>2%</td><td>47%</td><td>50%</td><td>39%</td><td>1%</td><td>26%</td><td>12%</td><td>27%</td><td>45%</td><td>15%</td><td>11%</td><td>9%</td></tr><tr><td>OP</td><td>23%</td><td>-7%</td><td>21%</td><td>73%</td><td>18%</td><td>24%</td><td>123%</td><td>149%</td><td>78%</td><td>-29%</td><td>80%</td><td>24%</td><td>93%</td><td>75%</td><td>19%</td><td>11%</td><td>11%</td></tr><tr><td>Net income</td><td>113%</td><td>-11%</td><td>-2%</td><td>29%</td><td>-27%</td><td>29%</td><td>170%</td><td>194%</td><td>111%</td><td>-19%</td><td>75%</td><td>24%</td><td>84%</td><td>58%</td><td>18%</td><td>10%</td><td>10%</td></tr><tr><td colspan="18">QoQ</td></tr><tr><td>Revenues</td><td>-11%</td><td>14%</td><td>-1%</td><td>-3%</td><td>-19%</td><td>19%</td><td>60%</td><td>1%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>GP</td><td>-4%</td><td>16%</td><td>10%</td><td>-1%</td><td>-21%</td><td>18%</td><td>59%</td><td>1%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>OP</td><td>-8%</td><td>38%</td><td>50%</td><td>-9%</td><td>-38%</td><td>45%</td><td>172%</td><td>1%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Net income</td><td>80%</td><td>-40%</td><td>29%</td><td>-8%</td><td>3%</td><td>5%</td><td>169%</td><td>1%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Source: Company data, GS Global Investment Research

Valuation: We derive our 12M TP of Rmb32.9 on a target P/E multiple of 49.9x 2026E EPS. Our target P/E of 49.9x is derived from the correlation between P/E and EPS growth of E-Town's peers, based on E-Town's 2027-28E EPS YoY growth.

Key risks: Faster-/slower-than-expected semis capex expansion in China; Milder-/fiercer-than-expected competition; Faster-/slower-than-expected ramp up of RTP and dry etcher's shipments

<table><tr><td>688729.SS</td><td>12m Price Target: Rmb32.90</td><td colspan="2">Price: Rmb37.57</td><td colspan="2">Downside: 12.4%</td></tr><tr><td>Neutral</td><td colspan="5">GS Forecast</td></tr><tr><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Market cap:</td><td>Revenue (Rmb mn) New</td><td>5,076.3</td><td>6,204.4</td><td>8,937.8</td><td>10,231.4</td></tr><tr><td>Rmb111.0bn / $16.3bn</td><td>Revenue (Rmb mn) Old</td><td>5,076.3</td><td>7,131.3</td><td>8,762.3</td><td>9,935.5</td></tr><tr><td>Enterprise value:</td><td>EBITDA (Rmb mn)</td><td>777.7</td><td>1,324.2</td><td>2,195.8</td><td>2,579.1</td></tr><tr><td>Rmb108.9bn / $16.0bn</td><td>EPS (Rmb) New</td><td>0.23</td><td>0.42</td><td>0.66</td><td>0.78</td></tr><tr><td>3m ADTV:</td><td>EPS (Rmb) Old</td><td>0.23</td><td>0.44</td><td>0.63</td><td>0.74</td></tr><tr><td>Rmb796.6mn / $117.3mn</td><td>P/E (X)</td><td>112.3</td><td>89.9</td><td>56.9</td><td>48.4</td></tr><tr><td rowspan="5">China Greater China Technology M&amp;A Rank: 3 Leases incl. in net debt &amp; EV?: Yes</td><td>P/B (X)</td><td>8.4</td><td>10.9</td><td>9.2</td><td>7.7</td></tr><tr><td>Dividend yield (%)</td><td>0.1</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>CROCI (%)</td><td>1.0</td><td>20.8</td><td>27.9</td><td>29.5</td></tr><tr><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td>EPS (Rmb)</td><td>0.05</td><td>0.06</td><td>0.15</td><td>0.15</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 9 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, Allen Chang, Verena Jeng and Yifan Hu, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Allen Chang GS (Asia) L.L.C., Verena Jeng GS (Asia) L.L.C., Yifan Hu GS (Asia) L.L.C..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses inputs for the fiscal year at least seven quarters in the future compared with the year at least three quarters in the future (on a per-share basis for all metrics).

For a more detailed description of how we calculate the GS Factor Profile, please contact your GS representative.

## M&A Rank

Across our global coverage, we examine stocks using an M&A framework, considering both qualitative factors and quantitative factors (which may vary across sectors and regions) to incorporate the potential that certain companies could be acquired. We then assign a M&A rank as a means of scoring companies under our rated coverage from 1 to 3, with 1 representing high (30%-50%) probability of the company becoming an acquisition target, 2 representing medium (15%-30%) probability and 3 representing low (0%-15%) probability. For companies ranked 1 or 2, in line with our standard departmental guidelines we incorporate an M&A component into our target price. M&A rank of 3 is considered immaterial and therefore does not factor into our price target, and may or may not be discussed in research.

## Quantum

Quantum is GS' proprietary database providing access to detailed financial statement histories, forecasts and ratios. It can be used for in-depth analysis of a single company, or to make comparisons between companies in different sectors and markets.

## Disclosures

The rating(s) for E-Town Semis is/are relative to the other companies in its/their coverage universe: AAC, ACM Research, AMEC, ASMPT, AVC, AccoTest, Anji Micro, Asus, Auras, BOE, BYDE, Biren, CR Micro, Cambricon, Chenbro, China Mobile (HK), China Telecom, China Tower Corp., China

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
