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
# UMT (3491.TWO): LEO satellite business in expansion; 3Q26 to see GM improvement; Buy

UMT delivered strong June revenues growth at 89% YoY to NT\$257m, driven by expanding LEO satellite business, leading to 2Q26 revenues at NT\$902m; however, the QoQ is negative and 7% behind our estimates given its major customer's model transition. Nevertheless, we expect the impact from model transition would be lower in 3Q26 compared to 2Q26, supporting the monthly revenues back to sequential growth in 3Q26, GM recovery and better opex ratio considering the larger revenues scale. We remain positive on UMT given (1) riding on the accelerating LEO satellite launches to enhance the satellite communication services and expand Space applications, (2) waveguide for LEO satellite dollar content increase given more bands are adopted per LEO satellite, and (3) waveguide end market expands from LEO satellite to AI data center for high-speed interconnection in scale up (report link). Maintain Buy.

UMT provides rectangular waveguides, which are conducting pipes with a rectangular cross-section used to guide the propagation of microwave or mmwave signals. Different shapes and combinations of waveguides can form various RF passive components, such as filter / diplexer, coupler, isolator, antenna, power amplifiers (PAs), etc. The company serves leading global LEO satellite operators, and its waveguides can be seen in LEO satellites / payloads (main), and gateways in ground stations.

Exhibit 1: We expect company's July revenues at 119% YoY/ 8% MoM to NT\$277m UMT monthly/ quarterly revenues

<table><tr><td></td><td>Apr 2026</td><td>May 2026</td><td>Jun 2026</td><td>Jul 2026E</td><td>Aug 2026E</td><td>Sep 2026E</td><td>2Q26</td><td>3Q26E</td></tr><tr><td>Revenues (NT$m)</td><td>349</td><td>296</td><td>257</td><td>277</td><td>311</td><td>520</td><td>902</td><td>1,108</td></tr><tr><td>YoY</td><td>84%</td><td>57%</td><td>89%</td><td>119%</td><td>87%</td><td>172%</td><td>76%</td><td>129%</td></tr><tr><td>MoM/QoQ</td><td>6%</td><td>-15%</td><td>-13%</td><td>8%</td><td>12%</td><td>68%</td><td>-12%</td><td>23%</td></tr><tr><td>GS estimates (NT$m)</td><td>372</td><td>373</td><td>320</td><td></td><td></td><td></td><td>966</td><td></td></tr><tr><td>Actual vs. GS</td><td>-6%</td><td>-21%</td><td>-20%</td><td></td><td></td><td></td><td>-7%</td><td></td></tr></table>

Source: Company data, GS Global Investment Research

2Q26 miss on major customer's model transition: UMT 2Q26 revenues were up 76% YoY to NT\$902m, with rising LEO satellite revenues contribution, while the revenues is 7% / 12% behind our / Bloomberg consensus given its major customer's model transition. 2Q26 GM was at 55.6% (vs. 2Q25/ 1Q26 at 43.4%/ 58.0%) with improving YoY driven by better product mix, while lower than our estimates / Bloomberg consensus, given the impact from model transition. We expect to see sequential GM improvement ahead on rising LEO satellite contribution and less impact from model transition. 2Q26 Opex ratio was at 28.8%, or higher than our estimates / Bloomberg consensus at 26.7%/ 27.3%, and we attribute it to smaller

Allen Chang
+852-2978-2930 |
allen.k.chang@gs.com
GS (Asia) L.L.C.

Verena Jeng
+852-2978-1681 | verena.jeng@gs.com
GS (Asia) L.L.C.

Ting Song
+852-2978-6466 | ting.song@gs.com
GS (Asia) L.L.C.

revenues scale. Overall, the OP income remains strong in YoY at +158%, while decline 23% QoQ and is 24% / 27% behind our / Bloomberg consensus due to the model transition.

Exhibit 2: UMT 2Q26 result snapshot

<table><tr><td>NT$ m</td><td>2Q25</td><td>1Q26</td><td>2Q26</td><td>QoQ</td><td>YoY</td><td>GS</td><td>Act/ GS</td><td>Cons.</td><td>Act / Cons.</td></tr><tr><td>Revenues</td><td>514</td><td>1,020</td><td>902</td><td>-12%</td><td>76%</td><td>966</td><td>-7%</td><td>1,028</td><td>-12%</td></tr><tr><td>GP</td><td>223</td><td>592</td><td>502</td><td>-15%</td><td>125%</td><td>576</td><td>-13%</td><td>613</td><td>-18%</td></tr><tr><td>OP</td><td>94</td><td>314</td><td>241</td><td>-23%</td><td>158%</td><td>318</td><td>-24%</td><td>332</td><td>-27%</td></tr><tr><td>Net income</td><td>71</td><td>253</td><td>308</td><td>22%</td><td>333%</td><td>260</td><td>18%</td><td>367</td><td>-16%</td></tr><tr><td>Margins</td><td colspan="5"></td><td colspan="2"></td><td colspan="2"></td></tr><tr><td>GM</td><td>43.3%</td><td>58.0%</td><td>55.6%</td><td></td><td></td><td>59.6%</td><td></td><td>59.6%</td><td></td></tr><tr><td>OPM</td><td>18.2%</td><td>30.7%</td><td>26.8%</td><td></td><td></td><td>32.9%</td><td></td><td>32.3%</td><td></td></tr><tr><td>NM</td><td>13.8%</td><td>24.8%</td><td>34.1%</td><td></td><td></td><td>26.9%</td><td></td><td>35.7%</td><td></td></tr></table>

Source: Company data, GS Global Investment Research, Bloomberg

Earnings revision: We factor in UMT 2Q26 results, and revise down 2026E GM by 2.4ppts to reflect the impact on model transition in 2Q - 3Q26. We continue to expect a strong growth ahead driven by LEO satellites launches and specification upgrade, and thus keep our estimates in 2027 - 28E largely unchanged. The blended GM would continue to expand on product mix upgrade toward LEO satellites from traditional RF products for telecom operators.

Exhibit 3: Earnings revision

<table><tr><td rowspan="2">NT$m</td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td>Old</td><td>New</td><td>Diff %</td><td>Old</td><td>New</td><td>Diff %</td><td>Old</td><td>New</td><td>Diff %</td></tr><tr><td>Revenues</td><td>4,276</td><td>4,293</td><td>0%</td><td>8,991</td><td>8,959</td><td>0%</td><td>12,635</td><td>12,580</td><td>0%</td></tr><tr><td>GP</td><td>2,706</td><td>2,615</td><td>-3%</td><td>6,060</td><td>6,065</td><td>0%</td><td>8,751</td><td>8,714</td><td>0%</td></tr><tr><td>OP</td><td>1,559</td><td>1,419</td><td>-9%</td><td>3,560</td><td>3,574</td><td>0%</td><td>5,239</td><td>5,242</td><td>0%</td></tr><tr><td>Net income</td><td>1,262</td><td>1,261</td><td>0%</td><td>2,851</td><td>2,863</td><td>0%</td><td>4,136</td><td>4,134</td><td>0%</td></tr><tr><td>Margins</td><td colspan="3"></td><td colspan="3"></td><td colspan="3"></td></tr><tr><td>GM</td><td>63.3%</td><td>60.9%</td><td></td><td>67.4%</td><td>67.7%</td><td></td><td>69.3%</td><td>69.3%</td><td></td></tr><tr><td>OPM</td><td>36.5%</td><td>33.1%</td><td></td><td>39.6%</td><td>39.9%</td><td></td><td>41.5%</td><td>41.7%</td><td></td></tr><tr><td>NM</td><td>29.5%</td><td>29.4%</td><td></td><td>31.7%</td><td>32.0%</td><td></td><td>32.7%</td><td>32.9%</td><td></td></tr></table>

Source: Company data, GS Global Investment Research

Valuation: We continue to derive our target price based on a discounted P/E, and based on 2029E (methodology unchanged). We continue to derive the target P/E multiple from the average PEG&M ratio of peers in the satellite supply chain, and we remove outliers (telecom operators who face competition from LEO satellite operators). Our target 2029E discounted P/E multiple is at 37.0x (unchanged) which is based on peers' avg. PEG&M, and UMT's 2029-30E avg. NI YoY and OPM. We apply the 37.0x multiple to 2029E EPS and discount it back to 2027E via a COE of 7.8% (no change). Our target price is at NT\$2,513 (unchanged), implying 60x 2027E P/E, which is above the company's average +1 stv. P/E of 40x, reflecting our positive view on UMT's product mix upgrade toward LEO satellites. Maintain Buy.

Exhibit 4: UMT discounted P/E

<table><tr><td>(NT$ mn)</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td></tr><tr><td>Milestones</td><td colspan="3">Telecom components</td><td colspan="4">LEO satellite launch accelerations</td><td colspan="2">LEO satellite users ramp up</td></tr><tr><td>Satellite revenues %</td><td>15%</td><td>15%</td><td>43%</td><td>59%</td><td>80%</td><td>90%</td><td>93%</td><td></td><td></td></tr><tr><td>Revenue</td><td>1,838</td><td>1,585</td><td>2,335</td><td>2,452</td><td>4,293</td><td>8,959</td><td>12,580</td><td>16,228</td><td>19,798</td></tr><tr><td>YoY</td><td>5%</td><td>-14%</td><td>47%</td><td>5%</td><td>75%</td><td>109%</td><td>40%</td><td>29%</td><td>22%</td></tr><tr><td>Gross margin</td><td>40.9%</td><td>40.4%</td><td>51.3%</td><td>51.1%</td><td>60.9%</td><td>67.7%</td><td>69.3%</td><td>69.8%</td><td>70.1%</td></tr><tr><td>Operating profit</td><td>294</td><td>202</td><td>624</td><td>575</td><td>1,419</td><td>3,574</td><td>5,242</td><td>6,859</td><td>8,467</td></tr><tr><td>YoY</td><td>33%</td><td>-31%</td><td>208%</td><td>-8%</td><td>147%</td><td>152%</td><td>47%</td><td>31%</td><td>23%</td></tr><tr><td>Operating margin</td><td>16%</td><td>13%</td><td>27%</td><td>23%</td><td>33%</td><td>40%</td><td>42%</td><td>42%</td><td>43%</td></tr><tr><td>Net profit</td><td>271</td><td>200</td><td>547</td><td>518</td><td>1,261</td><td>2,863</td><td>4,134</td><td>5,410</td><td>6,667</td></tr><tr><td>EPS (NT$, diluted)</td><td>4.34</td><td>3.12</td><td>8.27</td><td>7.60</td><td>18.82</td><td>41.73</td><td>60.26</td><td>78.85</td><td>97.18</td></tr><tr><td>YoY</td><td>15%</td><td>-26%</td><td>173%</td><td>-5%</td><td>143%</td><td>127%</td><td>44%</td><td>31%</td><td>23%</td></tr><tr><td>TP implied P/E</td><td>579</td><td>807</td><td>304</td><td>331</td><td>134</td><td>60</td><td>42</td><td>32</td><td>26</td></tr></table>

<table><tr><td>2029E target P/E</td><td>37.0</td></tr><tr><td>Target multiple x EPS</td><td>2,918</td></tr><tr><td>Discounted back to 2027; TP (NTD)</td><td>2,513.0</td></tr><tr><td>Implied 2027 P/E</td><td>60</td></tr><tr><td colspan="2">COE assumption</td></tr><tr><td>Beta</td><td>1.2</td></tr><tr><td>Risk free</td><td>1.6%</td></tr><tr><td>Market risk premium</td><td>5.1%</td></tr><tr><td>COE</td><td>7.8%</td></tr></table>

Source: Company data, GS Global Investment Research

Exhibit 5: UMT 12M forward P/E ratio  
![](images/d07ddaa07438e57f5bd810df0e4d11622f633254f205701c1e29035e2058519f.jpg)  
Source: Company data, GS Global Investment Research, Bloomberg

Exhibit 6: UMT QFII holdings  
![](images/1694cae9f0a04b8dbcb13312577f76cbbc2c1d1095e0017eadfcca878a6e4b76.jpg)  
Source: TEJ

Exhibit 7: UMT P&L Summary

<table><tr><td>NT$ mn</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td colspan="7">Income statement</td></tr><tr><td>Revenue</td><td>1,585</td><td>2,335</td><td>2,452</td><td>4,293</td><td>8,959</td><td>12,580</td></tr><tr><td>Gross profit</td><td>641</td><td>1,198</td><td>1,254</td><td>2,615</td><td>6,065</td><td>8,714</td></tr><tr><td>OP income</td><td>202</td><td>624</td><td>575</td><td>1,419</td><td>3,574</td><td>5,242</td></tr><tr><td>Net income</td><td>200</td><td>547</td><td>518</td><td>1,261</td><td>2,863</td><td>4,134</td></tr><tr><td>EPS (NT$)</td><td>3.12</td><td>8.27</td><td>7.60</td><td>18.82</td><td>41.73</td><td>60.26</td></tr><tr><td colspan="7">Ratios</td></tr><tr><td>Opex ratio</td><td>27.7%</td><td>24.6%</td><td>27.7%</td><td>27.8%</td><td>27.8%</td><td>27.6%</td></tr><tr><td>Tax rate</td><td>19.4%</td><td>21.7%</td><td>19.0%</td><td>21.7%</td><td>22.0%</td><td>22.0%</td></tr><tr><td colspan="7">Margins</td></tr><tr><td>Gross margin</td><td>40.4%</td><td>51.3%</td><td>51.1%</td><td>60.9%</td><td>67.7%</td><td>69.3%</td></tr><tr><td>Operating margin</td><td>12.8%</td><td>26.7%</td><td>23.4%</td><td>33.1%</td><td>39.9%</td><td>41.7%</td></tr><tr><td>Net margin</td><td>12.6%</td><td>23.4%</td><td>21.1%</td><td>29.4%</td><td>32.0%</td><td>32.9%</td></tr><tr><td colspan="7">YoY</td></tr><tr><td>Revenue</td><td>-14%</td><td>47%</td><td>5%</td><td>75%</td><td>109%</td><td>40%</td></tr><tr><td>Gross profit</td><td>-15%</td><td>87%</td><td>5%</td><td>109%</td><td>132%</td><td>44%</td></tr><tr><td>OP income</td><td>-31%</td><td>208%</td><td>-8%</td><td>147%</td><td>152%</td><td>47%</td></tr><tr><td>Net income</td><td>-26%</td><td>173%</td><td>-5%</td><td>143%</td><td>127%</td><td>44%</td></tr><tr><td colspan="7">QoQ</td></tr><tr><td>Revenue</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Gross profit</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>OP income</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Net income</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Source: Company data, GS Global Investment Research

<table><tr><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26</td><td>3Q26E</td><td>4Q26E</td></tr><tr><td colspan="4"></td><td colspan="4"></td></tr><tr><td>620</td><td>514</td><td>484</td><td>834</td><td>1,020</td><td>902</td><td>1,108</td><td>1,263</td></tr><tr><td>314</td><td>223</td><td>229</td><td>489</td><td>592</td><td>502</td><td>662</td><td>859</td></tr><tr><td>167</td><td>94</td><td>84</td><td>230</td><td>314</td><td>241</td><td>361</td><td>503</td></tr><tr><td>143</td><td>71</td><td>88</td><td>216</td><td>253</td><td>308</td><td>333</td><td>397</td></tr><tr><td>2.09</td><td>1.07</td><td>1.29</td><td>3.15</td><td>3.69</td><td>4.49</td><td>4.85</td><td>5.79</td></tr><tr><td colspan="4"></td><td colspan="4"></td></tr><tr><td>23.7%</td><td>25.1%</td><td>29.9%</td><td>31.0%</td><td>27.2%</td><td>28.8%</td><td>27.2%</td><td>28.2%</td></tr><tr><td>21.9%</td><td>7.7%</td><td>21.8%</td><td>19.1%</td><td>22.0%</td><td>22.0%</td><td>22.0%</td><td>22.0%</td></tr><tr><td colspan="4"></td><td colspan="4"></td></tr><tr><td>50.6%</td><td>43.3%</td><td>47.3%</td><td>58.6%</td><td>58.0%</td><td>55.6%</td><td>59.8%</td><td>68.0%</td></tr><tr><td>26.9%</td><td>18.2%</td><td>17.4%</td><td>27.6%</td><td>30.7%</td><td>16.5%</td><td>32.6%</td><td>39.8%</td></tr><tr><td>23.0%</td><td>13.8%</td><td>18.2%</td><td>25.9%</td><td>24.8%</td><td>180.4%</td><td>30.1%</td><td>31.5%</td></tr><tr><td colspan="4"></td><td colspan="4"></td></tr><tr><td>43%</td><td>-21%</td><td>-24%</td><td>36%</td><td>65%</td><td>76%</td><td>129%</td><td>51%</td></tr><tr><td>60%</td><td>-38%</td><td>-31%</td><td>56%</td><td>89%</td><td>125%</td><td>189%</td><td>76%</td></tr><tr><td>117%</td><td>-53%</td><td>-55%</td><td>40%</td><td>88%</td><td>158%</td><td>329%</td><td>119%</td></tr><tr><td>84%</td><td>-60%</td><td>-33%</td><td>36%</td><td>77%</td><td>333%</td><td>277%</td><td>84%</td></tr><tr><td colspan="4"></td><td colspan="4"></td></tr><tr><td>1%</td><td>-17%</td><td>-6%</td><td>72%</td><td>22%</td><td>-12%</td><td>23%</td><td>14%</td></tr><tr><td>0%</td><td>-29%</td><td>3%</td><td>113%</td><td>21%</td><td>-15%</td><td>32%</td><td>30%</td></tr><tr><td>2%</td><td>-44%</td><td>-10%</td><td>173%</td><td>36%</td><td>-23%</td><td>50%</td><td>39%</td></tr><tr><td>-10%</td><td>-50%</td><td>24%</td><td>145%</td><td>17%</td><td>22%</td><td>8%</td><td>19%</td></tr></table>

## Price target risks and methodology - UMT

Valuation: We use a discounted P/E methodology and apply a 37.0x target P/E multiple to UMT's 2029E EPS, discounting it back to 2027E at a COE of 7.8% (beta 1.2x, risk-free rate 1.6% and market risk premium at 5.1%), which leads to our 12-month target price of NT\$2,513. The target P/E is based on the average PEG&M ratio of peers in the satellite supply chain. We are Buy-rated on UMT.

Key Risks: Slower-than-expected LEO satellite deployment; Potential competition from new-entrant suppliers; LEO satellite operators manufacturing in-house components.

<table><tr><td>3491.TWO</td><td colspan="2">12m Price Target: NT$2,513.00</td><td colspan="2">Price: NT$1,155.00</td><td colspan="2">Upside: 117.6%</td></tr><tr><td>Buy</td><td></td><td>GS Forecast</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td rowspan="11" colspan="2">Market cap: NT$76.5bn / $2.4bnEnterprise value:NT$75.8bn / $2.3bn3m ADTV: NT$3.3bn / $103.8mnTaiwanGreat

[中间内容因长度限制已省略]

including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any

such system.
"""
