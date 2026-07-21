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
Global Energy Storage

# Global Energy Storage: Data center battery intensity rises as sentiment cools

![](images/2553f186061ef55ac240d1680214ebd5c2240b449f8d82742e13c1a9fc49e976.jpg)

Neil Beveridge, Ph.D.

+852 2123 2648

neil.beveridge@bernsteinsg.com

![](images/ecc58a0b2c00f2f4c77f1bae156bfe9407c11eacd2355f7251633183dc63baa5.jpg)

Brian Ho, CFA

+852 2123 2615

brian.ho@bernsteinsg.com

![](images/453563f166aafc4395a87815a6a7088e6857153f41bba511620d58e086d46a75.jpg)

Kelvin Yuan, Ph.D., CFA

+852 2123 2612

kelvin.yuan@bernsteinsg.com

Data centers are becoming more battery intense with average duration increasing to c. 5hrs as more are built behind the meter. Batteries are used in data centers for centralized power (UPS), distributed power (BBU) and energy storage (ESS). While UPS and BBU demand is relatively short duration (<0.25hrs), ESS demand can be longer. With 24% of data centers under construction off grid and 39% of the pipeline off grid, battery energy storage is rising in duration with some hyperscalers having up to 8hours storage.

Assuming 103GW of data center capacity by 2030, cumulative battery capacity will rise to 277GWh. We assume US data center capacity will increase from 41GW to 103GW by 2030. We expect annual data center battery demand to increase 10x from 5GWh to 66GWh. Cumulative ESS demand for data centers reached 11GWh in 2025 and will likely increase to 277GWh by 2030. This implies the battery /data center capacity GWh/GW multiplier will rise from 0.3 to 2.7x. Newer projects have a multiplier of 4-8x, implying further scope for battery demand to increase.

Increased data center demand raises our total battery demand for the US to 486GWh by 2030 which represents 22% CAGR and a 15% increase on previous estimates. 70% of incremental demand is forecast to be from ESS which will likely grow from 49GWh (2025) to 266GWh by 2030. ESS capacity in the US is currently limited at 36GWh but set to grow to 102GWh this year as more EV plants are converted to ESS.

But while our base case has increased, it's also fair to say that so too has uncertainty in long term growth. Increased data center capex and the success of lower cost Chinese models is creating near term uncertainty in the pace of AI data center build out. While the longer term outlook looks positive, there is a risk that capex could slow if hyperscalers become less confident in returns from the AI business model. Upcoming mid-year results from the hyperscalers may provide further guidance.

Profitability remains another key question, with margins (ex-subsidy) close to breakeven. While demand looks set to grow by 20-25% CAGR though to 2030, margins excluding tax benefits remain negative or close to zero. While guidance is for Korean battery maker margins to turn positive in 2H26, this remains still the subject of debate. While we think that higher ESS utilization will raise margins, continued de-rating of EV demand in the US YTD (-25%) may continue to put pressure on margins in the near term.

Korean battery makers valuations have a better risk-reward (12x EV/EBITDA 2027 and 5x for 2030) but we would wait for a better entry point. LGES and SDI are pricing in 22-26% revenue CAGR to end of decade (in line with industry growth) and a return to high single digit margins. Longer term we assume mid to high single digit growth and margins, which give c. 10% &30% upside from current levels for LGES and SDI respectively. While these stocks look more attractive, we would wait for a better entry point.

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2"></td><td colspan="4">16 Jul 2026</td><td>TTM</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td></td><td></td><td rowspan="2">Closing Price</td><td rowspan="2">Price Target</td><td rowspan="2">Rel. Perf.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Ticker</td><td>Rating</td><td>Cur</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>373220.KS (LGES)</td><td>M</td><td>KRW</td><td>332,000</td><td>351,000</td><td>(29.1)%</td><td>KRW (4,580.94)</td><td>(2,364.33)</td><td>10,225</td><td></td><td>(72.5)</td><td>(140.4)</td><td>32.5</td></tr><tr><td>OLD</td><td></td><td></td><td></td><td>347,000</td><td></td><td></td><td>1,811.04</td><td>9,452.97</td><td></td><td></td><td></td><td></td></tr><tr><td>051910.KS (LG Chem)</td><td>M</td><td>KRW</td><td>260,000</td><td>312,000</td><td>(34.9)%</td><td>KRW(13,258.70)</td><td>2,693.22</td><td>28,743</td><td></td><td>(19.6)</td><td>96.5</td><td>9.0</td></tr><tr><td>OLD</td><td></td><td></td><td></td><td>298,000</td><td></td><td></td><td>3,030.56</td><td>27,968</td><td></td><td></td><td></td><td></td></tr><tr><td>006400.KS (SDI)</td><td>M</td><td>KRW</td><td>430,000</td><td>520,000</td><td>92.9%</td><td>KRW (9,933.80)</td><td>1,751.66</td><td>18,577</td><td></td><td>(43.3)</td><td>245.5</td><td>23.1</td></tr><tr><td>OLD</td><td></td><td></td><td></td><td></td><td></td><td></td><td>2,099.51</td><td>18,376</td><td></td><td></td><td></td><td></td></tr><tr><td>ASIAX</td><td></td><td></td><td>1,865.18</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

PRICE TARGET CHANGE / ESTIMATE CHANGE IN BOLD

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

Korean battery makers look well place to benefit from the growth in ESS demand in the US and the tariff wall & subsidies which have been put in place to protect them from Chinese competition. Data center demand in particular could be a material driver of growth with a 10x increase in cumulative demand through to the end of the decade. Even by 2030, the storage/capacity multiplier of 2.7x could well below the 4-8x multiplier for new data centers which are increasingly being build off grid. With LFP capacity set to expand significantly this year, Korean battery makers also look better placed to service this demand. SDI is more exposed to the ESS trend than LGES, with almost half of battery sales set to come from ESS and relatively lower EV exposure. Valuations more attractive given the sell-off driving forward EV/EBITDA multiples to 12x and long term (2030) multiples to 5x. But with questions surrounding the sustainability of AI capex and continued uncertainty on 2H26 margins we still believe there are better entry points ahead. We remain Market-Perform on LGES, LG Chem and SDI.

Model updates: we make a series of mostly minor update based on our recent demand update. For the details of the model updates, please see page 14 onwards.

## VALUATION COMPS TABLE

<table><tr><td rowspan="2">Company</td><td rowspan="2">Price20-Jul</td><td rowspan="2">Curcy</td><td rowspan="2">EVUSD mn</td><td rowspan="2">Mkt capUSD mn</td><td colspan="4">P/E</td><td colspan="4">EV/Sales</td><td rowspan="2">Sales Growth24-25</td></tr><tr><td>24A</td><td>25A</td><td>26E</td><td>27E</td><td>24A</td><td>25A</td><td>26E</td><td>27E</td></tr><tr><td>LGES</td><td>319,500.0</td><td>KRW</td><td>69,432</td><td>50,510</td><td>-109.9</td><td>-101.9</td><td>-2,094.1</td><td>45.3</td><td>3.9</td><td>4.3</td><td>3.5</td><td>2.8</td><td>-8%</td></tr><tr><td>CATL(H)</td><td>616.0</td><td>HKD</td><td>350,197</td><td>368,912</td><td>0.0</td><td>37.4</td><td>26.0</td><td>21.3</td><td>0.0</td><td>5.7</td><td>3.9</td><td>3.2</td><td>19%</td></tr><tr><td>CATL(A)</td><td>372.5</td><td>CNY</td><td>240,705</td><td>259,421</td><td>36.5</td><td>26.0</td><td>18.3</td><td>14.8</td><td>4.7</td><td>3.9</td><td>2.7</td><td>2.2</td><td>19%</td></tr><tr><td>Samsung SDI</td><td>403,500.0</td><td>KRW</td><td>30,136</td><td>22,002</td><td>31.9</td><td>-60.9</td><td>80.5</td><td>23.7</td><td>2.5</td><td>3.3</td><td>2.8</td><td>2.3</td><td>-26%</td></tr><tr><td>Panasonic</td><td>1,607</td><td>JPY</td><td>23,722</td><td>60,363</td><td>20.9</td><td>27.1</td><td>38.3</td><td>21.5</td><td>0.4</td><td>0.4</td><td>0.5</td><td>0.5</td><td>7%</td></tr><tr><td>BYD</td><td>89.9</td><td>HKD</td><td>130,640</td><td>117,066</td><td>21.4</td><td>22.7</td><td>20.0</td><td>15.7</td><td>1.2</td><td>1.1</td><td>1.0</td><td>0.9</td><td>15%</td></tr><tr><td>SK Innovation</td><td>117,600</td><td>KRW</td><td>40,697</td><td>13,452</td><td>-14.2</td><td>-15.4</td><td>12.7</td><td>19.6</td><td>0.8</td><td>0.7</td><td>0.7</td><td>0.7</td><td>8%</td></tr><tr><td>Gotion High Tech</td><td>26.0</td><td>CNY</td><td>15,265</td><td>6,968</td><td>59.4</td><td>15.9</td><td>25.4</td><td>17.3</td><td>3.0</td><td>2.3</td><td>1.7</td><td>1.3</td><td>29%</td></tr><tr><td>EVE</td><td>50.6</td><td>CNY</td><td>20,318</td><td>16,222</td><td>27.5</td><td>24.7</td><td>15.8</td><td>11.9</td><td>3.0</td><td>2.1</td><td>1.4</td><td>1.1</td><td>41%</td></tr><tr><td>Sunwoda</td><td>16.2</td><td>CNY</td><td>8,748</td><td>4,418</td><td>19.2</td><td>15.0</td><td>12.6</td><td>8.7</td><td>1.1</td><td>0.9</td><td>0.7</td><td>0.6</td><td>25%</td></tr><tr><td>CALB</td><td>17.2</td><td>HKD</td><td>15,446</td><td>3,897</td><td>46.2</td><td>21.0</td><td>10.6</td><td>7.0</td><td>3.5</td><td>2.6</td><td>1.5</td><td>1.2</td><td>38%</td></tr></table>

<table><tr><td rowspan="2">Company</td><td rowspan="2">LTM %</td><td rowspan="2">Rel LTM %</td><td rowspan="2">LTM High</td><td rowspan="2">LTM Low</td><td rowspan="2">GPM (%) 25A</td><td rowspan="2">OPM (%) 25A</td><td colspan="3">ND/E</td><td colspan="3">EV/EBITDA</td><td rowspan="2">25A EV/Capacity (USD M/GWh)</td></tr><tr><td>24A</td><td>25A</td><td>24A</td><td>25A</td><td>26E</td><td>27E</td></tr><tr><td>LGES</td><td>-1%</td><td>-55%</td><td>437,500</td><td>247,000</td><td>18%</td><td>6%</td><td>40%</td><td>48%</td><td>28.9</td><td>20.5</td><td>18.4</td><td>12.3</td><td>196</td></tr><tr><td>CATL(H)</td><td>64%</td><td>56%</td><td>795</td><td>392</td><td>25%</td><td>19%</td><td>-34%</td><td>-46%</td><td>0.0</td><td>24.1</td><td>17.1</td><td>14.0</td><td>467</td></tr><tr><td>CATL(A)</td><td>38%</td><td>-7%</td><td>469</td><td>255</td><td>25%</td><td>19%</td><td>-34%</td><td>-46%</td><td>20.4</td><td>16.6</td><td>11.7</td><td>9.6</td><td>321</td></tr><tr><td>Samsung SDI</td><td>144%</td><td>8%</td><td>820,000</td><td>180,100</td><td>8%</td><td>-13%</td><td>42%</td><td>34%</td><td>16.3</td><td>89.4</td><td>18.9</td><td>11.7</td><td>479</td></tr><tr><td>Panasonic</td><td>182%</td><td>102%</td><td>4,770</td><td>1,411</td><td>30%</td><td>5%</td><td>11%</td><td>15%</td><td>4.5</td><td>4.1</td><td>5.3</td><td>3.7</td><td>395</td></tr><tr><td>BYD</td><td>-28%</td><td>-29%</td><td>136</td><td>71</td><td>18%</td><td>4%</td><td>-51%</td><td>5%</td><td>9.3</td><td>9.0</td><td>7.1</td><td>6.0</td><td>278</td></tr><tr><td>SK Innovation</td><td>7%</td><td>-49%</td><td>166,000</td><td>87,700</td><td>6%</td><td>1%</td><td>78%</td><td>68%</td><td>20.3</td><td>16.2</td><td>8.5</td><td>9.1</td><td>369</td></tr><tr><td>Gotion High Tech</td><td>-10%</td><td>-25%</td><td>49.8</td><td>24.3</td><td>18%</td><td>7%</td><td>125%</td><td>122%</td><td>26.3</td><td>16.9</td><td>13.8</td><td>11.4</td><td>70</td></tr><tr><td>EVE</td><td>16%</td><td>-26%</td><td>94.4</td><td>43.4</td><td>17%</td><td>8%</td><td>37%</td><td>49%</td><td>22.0</td><td>17.0</td><td>12.2</td><td>9.7</td><td>157</td></tr><tr><td>Sunwoda</td><td>-21%</td><td>-49%</td><td>37.9</td><td>16.0</td><td>16%</td><td>3%</td><td>61%</td><td>99%</td><td>16.0</td><td>14.7</td><td>9.0</td><td>6.9</td><td>107</td></tr><tr><td>CALB</td><td>1%</td><td>-9%</td><td>39.3</td><td>16.3</td><td>17%</td><td>6%</td><td>96%</td><td>106%</td><td>26.7</td><td>19.6</td><td>10.6</td><td>8.0</td><td>82</td></tr></table>

CATL, LG Energy Solution, and Samsung SDI are covered by Neil Beveridge. BYD is covered by Eunice Lee. All other stocks are not covered by Bernstein. Source: Bloomberg (consensus), Bernstein analysis

## DETAILS

## DATA CENTER DEMAND IN US

We expect cumulative U.S. data center power capacity to reach 103 GW by 2030, driving incremental battery demand to 69 GWh in 2030 and cumulative battery installations to 277 GWh.

EXHIBIT 2: Total capacity is expected to reach 103 GW in 2030, with cumulative battery capacity reaching 277 GWh.  
![](images/8e22b10dbe592fa2952106a4c4de82f8be3bfafb6970348303f1e1fee1e33ee9.jpg)  
Source: BNEF, Bernstein analysis and estimates

Based on more than 20 announced U.S. data center projects, we have compiled a project-level summary table. The table shows that most projects are structured as utility-scale DC-PPAs or on-site behind-the-meter installations, with both power capacity and battery demand increasing clearly toward the end of the decade. For projects announced after 2024, the implied battery duration is generally above four hours, typically in the 4–8 hour range. This suggests that new data centers are increasingly adopting longer-duration battery solutions.

EXHIBIT 3: Project-Level Benchmark for US Data Center BESS

<table><tr><td>Project Name</td><td>Company / Operator</td><td>Year (Op./Ann.)</td><td>Power (MW)</td><td>Energy (MWh)</td><td>Duration (Hours)</td><td>Status</td><td>Storage Category</td></tr><tr><td>Apple California Flats CA</td><td>Apple</td><td>2022</td><td>60</td><td>240</td><td>4.0</td><td>Operational</td><td>Utility-tied (PPA)</td></tr><tr><td>Switch Gigawatt 1 Nevada (4 phases)</td><td>Switch / Capital Dynamics</td><td>2022</td><td>200</td><td>800</td><td>4.0</td><td>Operational</td><td>On-site BTM (off-grid DC campus)</td></tr><tr><td>AES / Microsoft California</td><td>Microsoft / AES</td><td>2023</td><td>55</td><td>220</td><td>4.0</td><td>Operational</td><td>Utility DC-PPA</td></tr><tr><td>Microsoft Sweden (Saft) — 24 MW / 16 MWh</td><td>Microsoft / Saft (TotalEnergies)</td><td>2023</td><td>24</td><td>16</td><td>0.7</td><td>Operational</td><td>On-site BTM (UPS replacement)</td></tr><tr><td>AES Baldy Mesa + Silver Peak CA</td><td>Amazon / AES</td><td>2024</td><td>100</td><td>400</td><td>4.0</td><td>Operational</td><td>Utility DC-PPA</td></tr><tr><td>Eleven Mile Solar Center AZ (∅rsted / Fluence → Meta)</td><td>Meta / ∅rsted / Fluence</td><td>2024</td><td>300</td><td>1,200</td><td>4.0</td><td>Operational</td><td>Utility DC-PPA</td></tr><tr><td>Google BESS Portfolio 2024</td><td>Google</td><td>2024</td><td>250</td><td>936</td><td>3.7</td><td>Operational</td><td>Utility DC-PPA</td></tr><tr><td>xAI Colossus Phase 1 TN</td><td>xAI / Tesla</td><td>2024</td><td>150</td><td>608</td><td>4.1</td><td>Operational</td><td>On-site BTM</td></tr><tr><td>xAI Colossus Phase 2 TN</td><td>xAI / Tesla</td><td>2025</td><td>150</td><td>655</td><td>4.4</td><td>Operational</td><td>On-site BTM</td></tr><tr><td>AES Bellefield 1 CA</td><td>Amazon / AES</td><td>2025</td><td>500</td><td>2,000</td><td>4.0</td><td>Operational</td><td>Utility DC-PPA</td></tr><tr><td>Google Bell Solar TX (X-ELIO / Fluence)</td><td>Google / X-ELIO</td><td>2025</td><td>300</td><td>1,200</td><td>4.0</td><td>Operational</td><td>Utility DC-PPA</td></tr><tr><td>Menifee Power Bank CA (Calpine)</td><td>Multi-DC Tenants (Calpine)</td><td>2025</td><td>680</td><td>2,720</td><td>4.0</td><td>Operational</td><td>Utility DC-PPA</td></tr><tr><td>Greenflash Project Soho TX</td><td>Greenflash Infrastructure (H.I.G.)</td><td>2026</td><td>400</td><td>800</td><td>2.0</td><td>Under Construction</td><td>Utility DC-PPA</td></tr><tr><td>Iron Mountain NJE-1 NJ</td><td>Iron Mountain</td><td>2026</td><td>12</td><td>23</td><td>1.9</td><td>Under Construction</td><td>On-site BTM</td></tr><tr><td>Aligned DC + Calibrant OR</td><td>Aligned Data Centers / Calibrant Energy</td><td>2026</td><td>31</td><td>62</td><td>2.0</td><td>Under Construction</td><td>On-site BTM</td></tr><tr><td>Crusoe / Redwood Energy TX</td><td>Cruso

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
