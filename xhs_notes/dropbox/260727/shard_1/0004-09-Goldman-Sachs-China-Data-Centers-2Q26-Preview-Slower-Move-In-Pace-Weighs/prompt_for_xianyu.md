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
CHINA DATA CENTERS

# 2Q26 Preview: Slower Move-In Pace Weighs on Quarter, But 12-Month Thesis Intact; Buy VNET/GDS/Range

Favorable developments in the China AI industry on both demand and supply sides have been supporting our constructive view on the China data center industry in the mid-to-long term. On the demand side, we believe China's AI

open-source/open-weight models are reaching a critical point of intelligence performance for global proliferation, and continue to expand token share by pushing the efficiency frontiers of LLMs in terms of inference cost (e.g. DeepSeek, Xiaomi MiMo). We think these which should further drive data center demand (e.g. Zhipu has reportedly commissioned the construction of a 1GW data center).

Meanwhile, domestic hardware systems continue narrowing the gap with advanced imported chips, as illustrated by Huawei's Atlas 950 SuperPoD (scheduled for 2H26 shipment) and Alibaba's T-head Lingjun Zhenwu M890 SuperPoD (live and compatible with Qwen3.8). We estimate that Huawei's Atlas 950 SuperPoD may double the computational power and token throughput per GW vs. the prior Atlas 910C SuperPoD, and narrow the gap with Nvidia B300 to 1/4 from 1/8 in the case of Atlas 910C despite 3x cost per computational power (Exhibit 5).

That said, industry growth in 1H26 appears to be marginally slower than our prior expectations, likely dragged by tighter chip availability (including domestic and imported chips). As per MIIT, China added 595EFLOPS (FP16) intelligent computational power in 1H26 (Exhibit 3, equivalent to 0.7GW AI-related move-in in 1H26 by GSe) to 2,185EFLOPS as of Jun 2026, below the 802EFLOPS addition in 2H25 and similar to 1H25 level when the Nvidia H20 export controls kicked in. We trim our 2026E China data center move-in demand estimate (AI and non-AI combined) to c.3GW (Exhibit 2) but continue to expect robust $20\%$ demand CAGR in 2025-28E from 16GW in 2025 to 27GW in 2028E (Exhibit 1).

Eunice Liu  
+852-2978-7472 | eunice.liu@gs.com  
GS (Asia) L.L.C.

Tighter chip availability coupled with robust AI training/inference demand has led to surging spot rates in the GPUaaS/GPU rental business as mentioned in our prior report (e.g. Nvidia H100 server monthly spot price almost doubled from c.Rmb50k in Jan-Feb to c.Rmb100k recently), while long-term contract price may not move as markedly, in our view. We note strong preliminary results from A-share companies involved in GPUaaS/GPU rental (all Not Covered) e.g. Sharetronic Data (300857.SZ), Lettall Electronic (603629.SS).

Timothy Zhao
+852-2978-2673 |
timothy.zhao@gs.com
GS (Asia) L.L.C.

Ronald Keung, CFA
+852-2978-0856 |
ronald.keung@gs.com
GS (Asia) L.L.C.

## Stock implications

GDS (Buy): We keep 2Q26E forecasts unchanged and look for revenue +6% yoy to Rmb3.07bn (2% below Visible Alpha Consensus Data) and adj. EBITDA -2% yoy to Rmb1.34bn (2% above consensus). We lower 2027E revenue/adj. EBITDA by 2% but raise 2028E revenue/adj. EBITDA by 2% as we fine-tune our utilized capacity and MSR assumptions. Our 12-month TPs for GDS/9698.HK are lowered to US\$46/HK\$45 (from US\$49/HK\$47 prior), based on SOTP valuation in which we apply (all unchanged): 1) 13.5x target EV/EBITDA to GDS China's 2027E EBITDA; 2) 23x target EV/EBITDA to DayOne's 2027E EBITDA (unchanged), adjusted by the 19.9% stake owned by GDS; 3) 10% holdco. discount. We believe the market has priced in the 500MW potential order volume in 1H26 given management's positive tone at the 1Q26 results call, and hence look for order updates in Jul-Aug.

■ VNET (Buy): We lower 2Q26E revenue by 3% to Rmb2.77bn (+14% yoy being the trough level of the year, 1% below consensus) to account for slower move-in, but keep 2Q26E adj. EBITDA largely unchanged at Rmb927mn (+26% yoy, 2% above consensus). We fine-tune 2026-28E revenue and adj. EBITDA in the range of -1% to 0%. Our 12m TP is unchanged at US\$16 based on 12x 2027E EV/EBITDA. We also look for potentially more color on its strategic collaboration with CATL and overseas expansion at the results call, and see large new orders as a positive surprise.

A-share names: We keep our estimates and TPs unchanged. Range Intelligent (300442.SZ, Buy) remains our preferred name among A-share data center operators, given its rich capacity reserves, full-stack AIDC capabilities (e.g. China's first 200MW, 100k chip-scale data center building operational starting from 1H26), strong customer relationships, and diverse, low-cost financing capabilities. We are Neutral rated on Athub (603881.SS) and Sell rated on Sinnet (300383.SZ).

Exhibit 1: We model c.3GW move-in demand in China data centers in 2026E, largely on par with 2025 despite stronger order volume

China data center live capacity vs. demand

![](images/eb69ce75b9778158ae7ced548c39d015286731928d698315ec89a350c3949b7f.jpg)  
Source: MIIT, CAICT, GS Global Investment Research  
Exhibit 2: ... out of which we estimate 50%+ is attributable to intelligent computing demand and 80%+ is captured by third-party data centers  
2026E China data center order volume and move-in demand breakdown

![](images/366ddf0883fd93bfffd66a2746c5a13e3f1b0730f1b7f38ffe2a10b94687fd30.jpg)  
Source: MIIT, NEA, GS Global Investment Research

Exhibit 3: China's \~600 EFLOPS intelligent computational power addition in 1H26 tracks below 2H25 run rate, yet we expect the pace to re-accelerate in 2H26E
China's intelligent computational power (EFLOPS, FP16)  
![](images/c1d2a23492647b32b45564863a85e2f17832e74b842010ae21a851f20347c7b3.jpg)  
Source: MIIT, GS Global Investment Research

Exhibit 4: China's internet data services industry power consumption growth stayed robust at $44\%$ yoy in 1H26  
![](images/d9291bc9cbc86b8a93823fce3490faa72191f1822710de237f85b8635438065f.jpg)  
Source: NEA

Exhibit 5: Economics of a 200MW IT power data center based on different IT infrastructure

<table><tr><td>Capex per 200MW IT power data center</td><td>Nvidia B300</td><td>Nvidia H800</td><td>Huawei CM384 910C</td><td>Huawei CM1024 950</td><td colspan="2">vs. 910C vs. B300</td></tr><tr><td>Computing power (EFLOPS, FP16)</td><td>250</td><td>240</td><td>80</td><td>76</td><td></td><td></td></tr><tr><td>Computing power (EFLOPS, FP8)</td><td>500</td><td>480</td><td>80</td><td>142</td><td></td><td></td></tr><tr><td>Total IT power (kW)</td><td>187,500</td><td>190,400</td><td>208,800</td><td>199,066</td><td></td><td></td></tr><tr><td>Servers/supermodes #</td><td>12,500</td><td>20,000</td><td>261</td><td>135</td><td></td><td></td></tr><tr><td>GPUs # per unit</td><td>8</td><td>8</td><td>384</td><td>1,024</td><td></td><td></td></tr><tr><td>CPUs # per unit</td><td>2</td><td>2</td><td>192</td><td>256</td><td></td><td></td></tr><tr><td>Computing power per unit (PFLOPS, FP16)</td><td>20</td><td>12</td><td>307</td><td>563</td><td></td><td></td></tr><tr><td>Computing power per GPU (TFLOPS, FP16)</td><td>2,500</td><td>1,500</td><td>800</td><td>550</td><td></td><td></td></tr><tr><td>Computing power per GPU (TFLOPS, FP8)</td><td>5,000</td><td>3,000</td><td>800</td><td>1,024</td><td></td><td></td></tr><tr><td>IT power per unit (kW)</td><td>15</td><td>10</td><td>800</td><td>1,475</td><td></td><td></td></tr><tr><td>TDP per GPU (W)</td><td>1,400</td><td>700</td><td>800</td><td>600</td><td></td><td></td></tr><tr><td>Coefficient</td><td>1.3</td><td>1.7</td><td>2.6</td><td>2.4</td><td></td><td></td></tr><tr><td>IT power per server (kW)</td><td>15</td><td>10</td><td>17</td><td>12</td><td></td><td></td></tr><tr><td>Total capex (Rmb bn)</td><td>61.0</td><td>54.8</td><td>41.0</td><td>54.9</td><td></td><td></td></tr><tr><td>Capex per IT power (Rmb bn/GW)</td><td>325</td><td>288</td><td>196</td><td>276</td><td>1.4x</td><td>0.8x</td></tr><tr><td>Capex per computing power (Rmb bn/EFLOPS, FP8)</td><td>0.12</td><td>0.11</td><td>0.51</td><td>0.39</td><td>0.8x</td><td>3.2x</td></tr><tr><td>Computing power per IT power (EFLOPS/GW, FP8)</td><td>2,667</td><td>2,521</td><td>384</td><td>711</td><td>1.9x</td><td>0.3x</td></tr></table>

Source: Company data, GS Global Investment Research

Exhibit 6: We expect VNET's move-in pace related to order backlog to improve qoq in 2Q26E yet absolute move-in (MW) may drop qoq
VNET's net addition as % backlog 4 quarters ago  
![](images/549ce96e1a4a12db495b96be2de9a38900046c31c16d83641534d366cfb70b42.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 7: ...while GDS' move-in pace moderated in 1Q26 and we expect it to be marginally softer in 2Q26E
GDS' gross addition as % backlog 4 quarters ago  
![](images/1197dec48bd6a88c963837d46443ae6445b2ca079487f8664b296933482ed767.jpg)  
Source: Company data, GS Global Investment Research

## GDS Holdings (GDS/9698.HK)

<table><tr><td>9698.HK</td><td>12m Price Target: HK$45</td><td colspan="2">Price: HK$31.42</td><td colspan="2">Upside: 43.2%</td></tr><tr><td>GDS</td><td>12m Price Target: $46</td><td colspan="2">Price: $31.63</td><td colspan="2">Upside: 45.4%</td></tr><tr><td>Buy</td><td colspan="5">GS Forecast</td></tr><tr><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Market cap: $6.1bn</td><td>Revenue (Rmb mn) New</td><td>11,432.3</td><td>12,712.7</td><td>13,600.3</td><td>16,103.2</td></tr><tr><td>Enterprise value: $11.6bn</td><td>Revenue (Rmb mn) Old</td><td>11,432.3</td><td>12,746.9</td><td>13,820.6</td><td>15,799.5</td></tr><tr><td>3m ADTV :$83.4mn</td><td>EBITDA (Rmb mn)</td><td>5,403.5</td><td>5,973.4</td><td>6,098.2</td><td>7,159.9</td></tr><tr><td>China</td><td>EPS (Rmb) New</td><td>4.71</td><td>11.47</td><td>(1.37)</td><td>1.25</td></tr><tr><td>China Internet Verticals</td><td>EPS (Rmb) Old</td><td>4.71</td><td>11.53</td><td>(0.83)</td><td>0.64</td></tr><tr><td></td><td>P/E (X)</td><td>48.0</td><td>18.7</td><td>NM</td><td>170.8</td></tr><tr><td>M&amp;A Rank: 3</td><td>P/B (X)</td><td>1.7</td><td>1.6</td><td>1.3</td><td>1.2</td></tr><tr><td>Leases incl. in net debt &amp; EV?: Yes</td><td>Dividend yield (%)</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td></td><td>CROCI (%)</td><td>8.0</td><td>12.1</td><td>7.6</td><td>7.8</td></tr><tr><td></td><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td></td><td>EPS (Rmb)</td><td>13.51</td><td>(0.51)</td><td>(0.74)</td><td>(0.78)</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 24 Jul 2028 close.

Exhibit 8: We forecast 25%/24% CAGR in 2025-28E for both capacity in service and capacity utilized to 2.9GW/2.2GW in-service/utilized capacity by 2028E  
![](images/e145c4ac57b6fcadf8387e21166710e1231e9511fa23a8e88edcadd81fcb0ce2.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 9: We continue to expect MSR to decline $7 - 9\%$ yoy in 2026-28E in Rmb/kW terms GDS China annual MSR  
![](images/d03b38ca63c3bc5207b21f5fbd07c311998956823b13e51520b89ffd2229de40.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 10: GDS expects to renew 16%/21% of committed area in 2Q-4Q26E/27E, one of key drivers behind MSR decline  
Contract renewal area sqm and \% of total area committed  
![](images/85385501e772d8f50537e921ceadfb38fc1900a8ce6214975826cd09a9cecab5.jpg)  
Source: Company data

Exhibit 11: We expect revenue/adj.EBITDA of DayOne to grow at $96\% / 113\%$ 2025-28E CAGRs  
DayOne annual revenue, adj.EBITDA and adj.EBITDA margin  
![](images/05ae85774a76de2d387551cd11f677cfd3103792dc661345bf539664040b4f01.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 12: Our SOTP-based target prices for GDS/9698.HK are US\$46 and HK\$45

<table><tr><td></td><td>EV/EBITDA</td><td>27EEBITDARmb mn</td><td>EnterprisevalueRmb mn</td><td>Net debtRmb mn</td><td>EquityvalueRmb mn</td><td>Value toGDSRmb mn</td><td>% val</td><td>Val/AD US$</td><td>Val/shareHK$</td></tr><tr><td>GDS China</td><td>13.5x</td><td>6,098</td><td>82,326</td><td>28,030</td><td>54,297</td><td>54,297</td><td>76%</td><td>34.9</td><td>34.0</td></tr><tr><td>DayOne</td><td>23.0x</td><td>7,268</td><td>167,153</td><td>39,022</td><td>128,130</td><td>25,498</td><td>36%</td><td>16.4</td><td>16.0</td></tr><tr><td>Total</td><td>18.7x</td><td>13,366</td><td>249,479</td><td>67,052</td><td>182,427</td><td>79,794</td><td>111%</td><td>51.4</td><td>50.0</td></tr><tr><td>Holdco. discount</td><td>10%</td><td></td><td></td><td></td><td></td><td>(7,979)</td><td>-11%</td><td>(5.1)</td><td>(5.0)</td></tr><tr><td>12m target price</td><td>16.4x</td><td></td><td>99,845</td><td>28,030</td><td></td><td>71,815</td><td>100%</td><td>46.0</td><td>45.0</td></tr></table>

Source: GS Global Investment Research

Exhibit 13: GDS & DayOne financials summary

<table><tr><td>GDS China (Rmb mn)</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Net revenue</td><td>10,322</td><td>11,432</td><td>12,713</td><td>13,600</td><td>16,103</td></tr><tr><td>COGS</td><td>(4,893)</td><td>(5,517)</td><td>(6,158)</td><td>(6,826)</td><td>(8,082)</td></tr><tr><td>Utility cost</td><td>(3,361)</td><td>(3,995)</td><td>(4,533)</td><td>(5,053)</td><td>(5,983)</td></tr><tr><td>Rent, Labour &amp; Other cost</td><td>(1,532)</td><td>(1,522)</td><td>(1,625)</td><td>(1,772)</td><td>(2,099)</td></tr><tr><td>Adjusted gross profit</td><td>5,429</td><td>5,915</td><td>6,555</td><td>6,775</td><td>8,021</td></tr><tr><td>Sales and marketing expenses</td><td>(116)</td><td>(149)</td><td>(173)</td><td>(185)</td><td>(211)</td></tr><tr><td>General and admin expenses</td><td>(918)</td><td>(898)</td><td>(944)</td><td>(1,010)</td><td>(1,179)</td></tr><tr><td>Research and development expens</td><td>(36)</td><td>(33)</td><td>(40)</td><td>(42)</td><td>(50)</td></tr><tr><td>Total operating expenses</td><td>(1,071)</td><td>(1,080)</td><td>(1,156)</td><td>(1,237)</td><td>(1,440)</td></tr><tr><td>Adjusted EBITDA</td><td>4,876</td><td>5,403</td><td>5,973</td><td>6,098</td><td>7,160</td></tr><tr><td>Operating profit (non-GAAP)</td><td>1,633</td><td>1,944</td><td>2,378</td><td>1,950</td><td>2,551</td></tr><tr><td>Net income</td><td>(771)</td><td>895</td><td>2,229</td><td>(267)</td><td>244</td></tr><tr><td>Net income (non-GAAP)</td><td>(289)</td><td>2,243</td><td>616</td><td>173</td><td>683</td></tr><tr><td>Adjusted GPM %</td><td>52.6%</td><td>51.7%</td><td>51.6%</td><td>49.8%</td><td>49.8%</td></tr><tr><td>Adjusted EBITDA %</td><td>47.2%</td><td>47.3%</td><td>47.0%</td><td>44.8%</td><td>44.5%</td></tr><tr><td>Operating profit, adj.</td><td>15.8%</td><td>17.0%</td><td>18.7%</td><td>14.3%</td><td>15.8%</td></tr><tr><td>Net income %</td><td>-7.5%</td><td>7.8%</td><td>17.5%</td><td>-2.0%</td><td>1.5%</td></tr><tr><td>Net income (non-GAAP) %</td><td>-2.8%</td><td>19.6%</td><td>4.8%</td><td>1.3%</td><td>4.2%</td></tr><tr><td colspan="6">Operating metrics</td></tr><tr><td>Area in service (sqm)</td><td>613,583</td><td>668,283</td><td>738,283</td><td>918,283</td><td>1,098,283</td></tr><tr><td>yoy%</td><td>12%</td><td>9%</td><td>10%</td><td>24%</td><td>20%</td></tr><tr><td>Area utilized (sqm)</td><td>453,094</td><td>504,843</td><td>571,864</td><td>680,864</td><td>809,864</td></tr><tr><td>yoy%</td><td>12%</td><td>11%</td><td>13%</td><td>19%</td><td>19%</td></tr><tr><td>MSR (Rmb/sqm/month)</td><td>2,004</td><td>1,989</td><td>1,901</td><td>1,809</td><td>1,800</td></tr><tr><td>yoy%</td><td>-4%</td><td>-1%</td><td>-4%</td><td>-5%</td><td>-1%</td></tr><tr><td>Utilization rate</td><td>73.8%</td><td>75.5%</td><td>77.5%</td><td>74.1%</td><td>73.7%</td></tr></table>

<table><tr><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td></tr><tr><td>2,723(1,268)(893)(375)</td><td>2,900(1,391)(1,012)(379)</td><td>2,887(1,415)(1,030)(384)</td><td>2,922(1,444)(1,060)(384)</td><td>3,367(1,415)(1,037)(378)</td><td>3,073(1,545)(1,134)(411)</td><td>3,106(1,591)(1,171)(420)</td><td>3,166(1,606)(1,191)(41

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
