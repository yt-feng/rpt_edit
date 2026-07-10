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
## Korea Nuclear EPC

## 2Q nuclear orders remain muted; reshuffle our nuclear order estimates

2Q order intake was solid but nuclear orders remained muted, with only a small KEPCO E&C maintenance contract (W33bn) from KHNP. Non-nuclear orders were strong: Doosan Enerbility's (Doosan) US steam turbine orders and Hyundai E&C's (HDEC) W10tn intake, including the Apgujeong 3rd District reconstruction (W5.6tn). We are reshuffling our order estimates, pushing back our overseas nuclear project assumptions by 1-2 years due to geopolitical tensions, trimming 2026-28E orderbook estimates and lowering price targets. 2Q earnings should be broadly in-line with consensus, with limited downside risk as problematic overseas projects near completion. We maintain a constructive sector view on all three names with Overweight ratings, with Doosan as our top pick.

\- 2Q new orders: strong overall, but nuclear orders remain muted. The only disclosed nuclear-related award was KEPCO E&C's emergency maintenance contract for an existing nuclear plant (W33bn) from KEPCO. Outside nuclear, Doosan booked W2.4tn of new orders, highlighted by another large US steam turbine and generator contract, reinforcing continued robust US CCPP (combined-cycle gas power plant) demand. HDEC also delivered strong order momentum in 2Q, booking W10tn of new orders led by the Apgujeong 3rd District reconstruction project (W5.6tn). Looking ahead, we expect Doosan to secure the \~W3tn construction portion of the Czech Dukovany nuclear project in the coming quarter.

\- Reshuffling our order estimates. Political complications and extended execution timelines have delayed several overseas nuclear projects, and we have pushed back our order assumptions by 1-2 years. In particular, we have pushed back our assumed US timeline from 2028 to 2029. In our view, this is largely dependent on intergovernmental decision-making between Korea and the US, including how Korea's planned \$200bn investment over the next 10 years in US infrastructure is allocated and sequenced. As a result, we cut our 2026-28E orderbook estimates for Doosan, KEPCO E&C, and HDEC by 5-17%, 3-31%, and 12-21%, respectively, which also drives lower target prices. That said, we believe the absence of a nuclear order win this year is largely priced in. Investor feedback from our Asia marketing last week suggests expectations have shifted towards a bear-case scenario in which only Korea and Vietnam orders are awarded (link to our note).

\- 2Q earnings likely a non-event; broadly in-line with BBG consensus. We do not expect a meaningful beat or miss, although quarterly volatility may persist due to uneven project progress. HDEC disclosed an additional upward order revision of W337bn for domestic projects, which should partially offset expected site-related cost overruns. In addition, previously problematic overseas projects are either completed or nearing completion (e.g., HDEC's

Korea Auto, EV battery, Nuclear and Utility

Sonny Lee AC

(82-2) 758 5716

sonny.lee@JPM.com

Seri Yoon

(82-2) 758 5704

seri.yoon@JPM.com

JPM Securities (Far East) Limited, Seoul Branch

Equity Ratings and Price Targets

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Mkt Cap ($ mn)</td><td rowspan="2">Price CCY</td><td rowspan="2">Price</td><td colspan="2">Rating</td><td colspan="4">Price Target</td></tr><tr><td>Cur</td><td>Prev</td><td>Cur</td><td>End Date</td><td>Prev End Date</td><td></td></tr><tr><td>Doosan Enerbility</td><td>034020 KS</td><td>31,290</td><td>KRW</td><td>74,000</td><td>OW</td><td>n/c</td><td>130,000</td><td>Dec-27</td><td>160,000</td><td>n/c</td></tr><tr><td>KEPCO E&amp;C</td><td>052690 KS</td><td>2,407</td><td>KRW</td><td>95,400</td><td>OW</td><td>n/c</td><td>180,000</td><td>Dec-27</td><td>260,000</td><td>n/c</td></tr><tr><td>Hyundai E&amp;C</td><td>000720 KS</td><td>7,457</td><td>KRW</td><td>100,500</td><td>OW</td><td>n/c</td><td>170,000</td><td>Dec-27</td><td>180,000</td><td>n/c</td></tr></table>

Source: Company data, Bloomberg Finance L.P., JPM estimates. n/c = no change. All prices as of 08 Jul 26.

See page 23 for analyst certification and important disclosures, including non-US analyst disclosures.

Saudi Arabia projects), reducing the risk of further margin drag.

\- Stay Overweight on the three nuclear EPC names. Despite softer sentiment on the near-term nuclear project outlook, we maintain a constructive view on the Korea nuclear EPC sector. Our top pick remains Doosan, supported by its expanding orderbook and balanced exposure across large-scale nuclear, SMRs, and gas turbines. We prefer the nuclear EPC names over KEPCO (UW), given: 1) better visibility on overseas EPC catalysts; and 2) relatively lower policy risk vs. KEPCO.

Wbn  
Table 1: Korea nuclear EPC companies: major order intake in 2Q26

<table><tr><td rowspan="2">Date announced</td><td rowspan="2">New/ Revision</td><td rowspan="2">Contract amount (Wbn)</td><td rowspan="2">Detail</td><td rowspan="2">Project owner</td><td colspan="2">Contract period</td></tr><tr><td>Start</td><td>End</td></tr><tr><td>Doosan Enerbility</td><td></td><td>2,369</td><td></td><td></td><td></td><td></td></tr><tr><td>5/6/2026</td><td>New</td><td>523</td><td>Busan Metropolitan City Myeongjang Park apartment construction</td><td>Jeongsang City Park</td><td>9/30/2026</td><td>12/30/2030</td></tr><tr><td>5/26/2026</td><td>New</td><td>480</td><td>Long Term Procurement Management contract for GT</td><td>Korea Southern Power</td><td>n/a</td><td>n/a</td></tr><tr><td>5/27/2026</td><td>New</td><td>n/a</td><td>W370MW steam turbine + generator supply contract</td><td>US company</td><td>n/a</td><td>~2029</td></tr><tr><td>6/1/2026</td><td>New</td><td>837</td><td>Jafurah Phase II cogeneration plant</td><td>KEPCO</td><td>6/1/2026</td><td>6/30/2029</td></tr><tr><td>6/15/2026</td><td>New</td><td>529</td><td>Duqm independent power project</td><td>Coastal Power SAOC</td><td>6/12/2026</td><td>4/1/2029</td></tr><tr><td>HDEC</td><td></td><td>9,791</td><td></td><td></td><td></td><td></td></tr><tr><td>4/15/2026</td><td>Reivision</td><td>241</td><td>Daejang-Hongdae metropolitan railway private investment facility construction</td><td>Seobu Metropolitan Metro</td><td>n/a</td><td>n/a</td></tr><tr><td>4/29/2026</td><td>Reivision</td><td>96</td><td>Itaewon UN site complex development</td><td>Yongsan Eleven</td><td>2/11/2023</td><td>6/4/2027</td></tr><tr><td>5/26/2026</td><td>New</td><td>5,561</td><td>Apgujeong Apartment District Special Planning Zone 3 housing redevelopment</td><td>Apgujeong Apartment District Special Planning Zone 3 Redevelopment Association</td><td>n/a</td><td>n/a</td></tr><tr><td>6/5/2026</td><td>New</td><td>3,039</td><td>Wirye Bokjeong station area complex development</td><td>Songpa Biz Cluster PFV</td><td>6/15/2026</td><td>1/14/2031</td></tr><tr><td>6/22/2026</td><td>New</td><td>853</td><td>Beomcheon 4 District housing redevelopment</td><td>Beomcheon 4 District Redevelopment Association</td><td>n/a</td><td>n/a</td></tr><tr><td>KEPCO E&amp;C</td><td></td><td>33</td><td></td><td></td><td></td><td></td></tr><tr><td>4/16/2026</td><td>New</td><td>33</td><td>Operating nuclear plants emergency maintenance</td><td>KHNP</td><td>4/14/2026</td><td>4/13/2027</td></tr></table>

Source: Company data

Table 2: Nearest nuclear projects relevant to Korea EPC companies  
Number of reactor units

<table><tr><td></td><td>Prime contractor</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td></tr><tr><td colspan="6">Large-scale projects</td></tr><tr><td>Bulgaria</td><td>Westinghouse</td><td></td><td>2</td><td></td><td></td></tr><tr><td>Poland</td><td>Westinghouse</td><td></td><td>3</td><td></td><td></td></tr><tr><td>Vietnam</td><td>KEPCO</td><td></td><td>2</td><td></td><td></td></tr><tr><td>Korea</td><td>KEPCO</td><td></td><td></td><td>2</td><td></td></tr><tr><td>US</td><td>Westinghouse</td><td></td><td></td><td></td><td>2</td></tr><tr><td>US</td><td>KEPCO</td><td></td><td></td><td></td><td>2</td></tr><tr><td colspan="6">Reactor units by prime contractor</td></tr><tr><td>KEPCO</td><td></td><td></td><td>2</td><td>2</td><td>2</td></tr><tr><td>Westinghouse</td><td></td><td></td><td>5</td><td></td><td>2</td></tr></table>

Source: Company data, JPM estimates.

Table 3: Estimated orders from the nearest large-scale nuclear projects \$bn

<table><tr><td></td><td>Prime contractor</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td></tr><tr><td colspan="6">Projected contract value</td></tr><tr><td>Bulgaria</td><td>Westinghouse</td><td></td><td>&gt;20</td><td></td><td></td></tr><tr><td>Poland</td><td>Westinghouse</td><td></td><td>&gt;30</td><td></td><td></td></tr><tr><td>Vietnam</td><td>KEPCO</td><td></td><td>10</td><td></td><td></td></tr><tr><td>Korea</td><td>KEPCO</td><td></td><td></td><td>10</td><td></td></tr><tr><td>US</td><td>Westinghouse</td><td></td><td></td><td></td><td>&gt;20</td></tr><tr><td>US</td><td>KEPCO</td><td></td><td></td><td></td><td>20</td></tr><tr><td colspan="6">Project by prime contractor</td></tr><tr><td>KEPCO</td><td></td><td></td><td>10</td><td>10</td><td>20</td></tr><tr><td>Westinghouse</td><td></td><td></td><td>&gt;50</td><td></td><td>&gt;20</td></tr><tr><td colspan="6">Est. order size for Korean EPC companies</td></tr><tr><td>Doosan</td><td>~$2bn for KEPCO reactor; ~$200mn per Westinghouse reactor</td><td></td><td>5.0</td><td>4.0</td><td>4.4</td></tr><tr><td>KEPCO E&amp;C</td><td>~$0.5bn per KEPCO reactor</td><td></td><td>1.0</td><td>1.0</td><td>1.0</td></tr><tr><td>HDEC</td><td>~$1.2bn per KEPCO reactor in Korea (double for overseas) x 50% chance; ~$4bn per Westinghouse reactor (Bulgaria, US)</td><td></td><td>10.4</td><td>1.2</td><td>10.4</td></tr></table>

Source: IAEA, company data, JPM estimates

Table 4: Estimated orders from the nearest SMR projects \$bn

<table><tr><td></td><td>SMR projects</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td></tr><tr><td>Doosan</td><td>NuScale, TerraPower, etc.</td><td>0.7</td><td>0.7</td><td>1.4</td><td>2.1</td></tr><tr><td>HDEC</td><td>Holtec International</td><td>2.0</td><td>2.0</td><td></td><td></td></tr></table>

Source: Company data, JPM estimates

## Table 5: JPMe vs consensus

<table><tr><td colspan="10">Doosan Enerbility</td></tr><tr><td rowspan="2"></td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td>JPMe</td><td>Consensus</td><td>Diff</td><td>JPMe</td><td>Consensus</td><td>Diff</td><td>JPMe</td><td>Consensus</td><td>Diff</td></tr><tr><td>Revenue</td><td>17,060</td><td>18,037</td><td>-5%</td><td>19,240</td><td>20,096</td><td>-4%</td><td>22,484</td><td>22,458</td><td>0%</td></tr><tr><td>OP</td><td>1,119</td><td>1,145</td><td>-2%</td><td>1,542</td><td>1,568</td><td>-2%</td><td>2,065</td><td>2,042</td><td>1%</td></tr><tr><td colspan="10">Hyundai E&amp;C</td></tr><tr><td rowspan="2"></td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td>JPMe</td><td>Consensus</td><td>Diff</td><td>JPMe</td><td>Consensus</td><td>Diff</td><td>JPMe</td><td>Consensus</td><td>Diff</td></tr><tr><td>Revenue</td><td>27,492</td><td>27,168</td><td>1%</td><td>28,484</td><td>29,218</td><td>-3%</td><td>31,029</td><td>31,444</td><td>-1%</td></tr><tr><td>OP</td><td>817</td><td>826</td><td>-1%</td><td>1,137</td><td>1,184</td><td>-4%</td><td>1,426</td><td>1,487</td><td>-4%</td></tr></table>

No consensus est. for KEPCO E&C  
Source: Bloomberg Finance L.P., JPM estimates.

## Overweight

034020.KS, 034020 KS
Price (08 Jul 26):W74,000

▼ Price Target (Dec-27):W130,000  
Prior (Dec-27):W160,000

## Korea Auto, EV battery, Nuclear and Utility

Sonny Lee AC
(82-2) 758 5716
sonny.lee@JPM.com
JPM Securities (Far East) Limited, Seoul Branch

Key Changes (FYE Dec)

<table><tr><td></td><td>Prev</td><td>Cur</td><td>Δ</td></tr><tr><td>Adj. EPS - 26E (W)</td><td>578</td><td>512</td><td>-11.5%</td></tr><tr><td>Adj. EPS - 27E (W)</td><td>1,193</td><td>1,046</td><td>-12.3%</td></tr></table>

Quarterly Forecasts (FYE Dec)
Adj. EPS (W)

<table><tr><td colspan="4">Adj. EPS (R)</td></tr><tr><td></td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>Q1</td><td>(107)</td><td>1A</td><td>173</td></tr><tr><td>Q2</td><td>204</td><td>153</td><td>248</td></tr><tr><td>Q3</td><td>(78)</td><td>175</td><td>258</td></tr><tr><td>Q4</td><td>114</td><td>183</td><td>367</td></tr><tr><td>FY</td><td>132</td><td>512</td><td>1,046</td></tr></table>

Style Exposure

<table><tr><td rowspan="2">Quant Factors</td><td rowspan="2">Current %Rank</td><td colspan="4">Hist %Rank (1=Top)</td></tr><tr><td>6M</td><td>1Y</td><td>3Y</td><td>5Y</td></tr><tr><td>Value</td><td>90</td><td>88</td><td>74</td><td>70</td><td>4</td></tr><tr><td>Growth</td><td>7</td><td>62</td><td>42</td><td>9</td><td>58</td></tr><tr><td>Momentum</td><td>21</td><td>6</td><td>25</td><td>54</td><td>11</td></tr><tr><td>Quality</td><td>85</td><td>81</td><td>74</td><td>15</td><td>100</td></tr><tr><td>Low Vol</td><td>82</td><td>81</td><td>66</td><td>82</td><td>100</td></tr><tr><td>ESGQ</td><td>19</td><td>14</td><td>29</td><td>97</td><td>-</td></tr></table>

## Doosan Enerbility

## Gas turbines to fill orderbook while nuclear remains silent

Doosan Enerbility continues to benefit from robust gas/steam turbine demand and CCPP (combined-cycle gas power plant) EPC, with orders flowing in steadily and robust demand continuing for the next several years. Nuclear orders remained muted in 1H: the Czech Dukovany construction portion (\~W3tn) leads the order momentum, but we have pushed Bulgaria's Kozloduy project into 2027 following a change in government that has slowed progress, and conservatively deferred Korea's domestic nuclear project order to next year, as site selection was only confirmed in June 2026. Accordingly, we trim our 2026-28E orderbook est. by 5-17% and cut our PT to W130,000, while earnings estimates remain largely unchanged.

Table 6: Doosan: 2Q26 preview
Wbn, %

<table><tr><td rowspan="2"></td><td colspan="3">2Q26</td><td rowspan="2">2Q25</td><td rowspan="2">% y/y</td><td rowspan="2">1Q26</td><td rowspan="2">% q/q</td></tr><tr><td>JPMe</td><td>BBG</td><td>Diff.</td></tr><tr><td>Revenue</td><td>4,487</td><td>4,657</td><td>-4%</td><td>4,569</td><td>-2%</td><td>4,261</td><td>5%</td></tr><tr><td>OP</td><td>283</td><td>268</td><td>5%</td><td>271</td><td>4%</td><td>234</td><td>21%</td></tr><tr><td>OP margin</td><td>6.3%</td><td>5.8%</td><td></td><td>5.9%</td><td></td><td>5.5%</td><td></td></tr><tr><td>NP</td><td>163</td><td>68</td><td>142%</td><td>198</td><td>-17%</td><td>60</td><td>171%</td></tr><tr><td>NP margin</td><td>3.6%</td><td>1.5%</td><td></td><td>4.3%</td><td></td><td>1.4%</td><td></td></tr></table>

Source: Company data, Bloomberg Finance L.P.  
Table 7: Doosan: Price target

Wbn, W, x

<table><tr><td colspan="2"></td><td>Value</td><td>Note</td></tr><tr><td>Doosan Enerbility</td><td>(a)</td><td>82,293</td><td></td></tr><tr><td>2028E Orderbook</td><td></td><td>43,312</td><td>Enerbility-only orderbook</td></tr><tr><td>Target Price/Orderbook</td><td></td><td>1.9x</td><td>Upcycle multiple</td></tr><tr><td>Investment value</td><td>(b)</td><td>4,445</td><td></td></tr><tr><td>Doosan Bobcat</td><td></td><td>2,839</td><td>48.2% stake x Market cap</td></tr><tr><td>Doosan Fuelcell</td><td></td><td>847</td><td>30.3% stake x Market cap</td></tr><tr><td>Doosan Skoda Power</td><td></td><td>759</td><td>67.0% stake x Market cap</td></tr><tr><td>Discount to investment value</td><td>(c)</td><td>50%</td><td></td></tr><tr><td>Target market cap</td><td>(a)+(b)x(1-c)</td><td>84,516</td><td></td></tr><tr><td>Price target</td><td></td><td>130,000</td><td></td></tr></table>

Source: Bloomberg Finance L.P., JPM estimates.

Price Performance  
![](images/b145642f31b8bfdf676abffca8a35b2ba85995048dc7f5c33d2f0ab0aa6ddcc9.jpg)

— 034020.

[中间内容因长度限制已省略]

al information is available upon request. The information in this material has been obtained from sources believed to be reliable. While all reasonable care has been taken to ensure that the facts stated in this material are accurate and that the forecasts, opinions and expectations contained herein are fair and reasonable, JPM Chase & Co. or its affiliates and/or subsidiaries (collectively JPM) make no representations or warranties whatsoever to the completeness or accuracy of the material provided, except with respect to any disclosures relative to JPM and the Research Analyst's involvement with the issuer that is the subject of the material. Accordingly, no reliance should be placed on the accuracy, fairness or completeness of the information contained in this material. There may be certain discrepancies with data and/or limited content in this material as a result of calculations, adjustments, translations to different languages, and/or local regulatory restrictions, as applicable. These discrepancies should not impact the overall investment analysis, views and/or recommendations of the subject company(ies) that may be discussed in the material. Artificial intelligence tools may have been used in the preparation of this material, including assisting in data analysis, pattern recognition, and content drafting for research material. JPM accepts no liability whatsoever for any loss arising from any use of this material or its contents, and neither JPM nor any of its respective directors, officers or employees, shall be in any way responsible for the contents hereof, apart from the liabilities and responsibilities that may be imposed on them by the relevant regulatory authority in the jurisdiction in question, or the regulatory regime thereunder. Opinions, forecasts or projections contained in this material represent JPM's current opinions or judgment as of the date of the material only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or
"""
