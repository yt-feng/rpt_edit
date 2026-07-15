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
CHINA COSMETICS

# 2Q/1H26 Preview: Growth fueled while margins mixed with online trending lower; Eyeing 2H new initiatives; Buy MGP/Giant/Forest Cabin/Jahwa

Despite a subdued 1Q26, we expect our cosmetics coverage to demonstrate accelerated topline momentum in 2Q26 (Exhibit 1): We estimate Mao Geping/Forest Cabin will spearhead growth at +28%/+39% yoy respectively for 1H26, followed by Shanghai Jahwa/Botanee/Proya at +14%/+10%/+1% in 2Q26; Giant's 1H26 sales will likely post -7% yoy primarily attributable to a challenging base but on track for the full-year outlook; Bloomage will remain under pressure at -18% yoy. Margins are divergent where we expect -9ppt-+1ppt OPM yoy where MGP/Forest Cabin/Botanee/Shanghai Jahwa are more resilient in our view.

Valerie Zhou  
+852-2978-0820 | valerie.zhou@gs.com  
GS (Asia) L.L.C.

Aside from key lines, we highlight key assumptions including: 1) Stronger online (see our monthly tracker) and offline counters remain solid, as we expect Mao Geping/Forest Cabin continue to deliver 12%+ SSSg in offline, although OTC channel continues to weigh on Botanee/Giant; 2) Companies' core brands will start to show stabilization as we expect Proya core/Comfy/Winona to register up to SD% yoy growth in 2Q26, from up to DD% yoy decline in 1Q26. 3) Emerging brands will likely remain the key growth engine, with Off-relax & Flower Knows /Collagen /Winona Baby & AXOMED /Dr Yu & Herborist projected to deliver up to 50% yoy growth; 4) However we expect ROIs to remain mixed with online margin trending lower, mitigated by the companies' improving offline counter productivity (Mao Geping/Forest Cabin), strategic pricing actions (Botanee), front-loaded first-quarter marketing expenditures and operational efficiency gains (Shanghai Jahwa). We believe Giant's NPM will be better than bearish expectation per GSe with implied online NPM at mid-20s%, sequentially improving from low-20s% in 2H25 though with yoy contraction to facilitate sound growth.

Focus into 1H26/2Q26 results: 1) Online growth sustainability will likely drive stronger sales in 1H/2Q26, where our high-frequency Douyin tracker (Exhibit 5) suggests volatile GMV yoy during non-peak season Jul-to-date, but Mao Geping/Shanghai Jahwa/Forest Cabin will likely maintain robust momentum; 2) Measures to mitigate online competition given softer macro backdrop and global brands' rising momentum compounded by a high base in 2H, including classic product upgrade (Proya, Forest Cabin), new product/business line rollouts (Giant/Forest Cabin/Winona) and omni-channel expansion (Mao Geping, Forest Cabin). 3) Multi-brand strategies that scale secondary brands to diversify sales streams and fuel Group growth.

We slightly tweak our 2026-2028E NI for covered cosmetics by $-1 + 4\%$ , but we cut TP by $10 - 27\%$ mainly to reflect lower valuation PE. We maintain Buy on Mao Geping, Giant Biogene, Forest Cabin, Jahwa for solid brand momentum or recovery trajectory; Neutral on Proya while awaiting more color for new products/brands into 2H, and Botanee for fair valuation; Sell on Bloomage.

## Relevant reads:

China Cosmetics: Monthly tracker: Jun-26: 2Q26 GMV accelerated vs. 1Q26; leading domestic brands and Western MNCs outperformed

Shanghai Forest Cabin Cosmetics (2657.HK): Product upgrades & in-house efficiencies to fuel full year guidance — APAC Consumer & Leisure Corporate Day 2026 Takeaways; Buy

Mao Geping Cosmetics Co. (1318.HK): Strong 618 growth with healthy ROI; balanced channel execution supports momentum — APAC Consumer & Leisure Corporate Day 2026 Takeaways; Buy (on CL)

Giant Biogene Holding (2367.HK): 618 recovery supporting FY growth guidance; more drivers ahead — APAC Consumer & Leisure Corporate Day 2026 Takeaways; Buy

China Cosmetics: 618 pulse check: Expert call takeaways: sound growth, more subsidies/promotion supports and stable channel spending; leading local/MNCs ahead

China Cosmetics: 618 pulse check: performance in Douyin: MNCs/higher-end led; MGP rebound to $50\%+$ yoy

## Looking into 2Q26/1H26 Results

Exhibit 1: We look for DD% growth in Revenue/NP into 2Q/1H26 for most covered brands with acceleration into 2H26 Cosmetics Coverage 2Q26/1H26 Preview

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Company</td><td colspan="4">1Q26</td><td colspan="4">2Q26E</td><td colspan="4">2H26E</td><td colspan="4">2026E</td><td colspan="4">2027E</td><td colspan="4">2028E</td></tr><tr><td>Sales</td><td>Sales yoy</td><td>Net profit</td><td>NP yoy</td><td>Sales</td><td>Sales yoy</td><td>Net profit</td><td>NP yoy</td><td>Sales</td><td>Sales yoy</td><td>Net profit</td><td>NP yoy</td><td>Sales</td><td>Sales yoy</td><td>Net profit</td><td>NP yoy</td><td>Sales</td><td>Sales yoy</td><td>Net profit</td><td>NP yoy</td><td>Sales</td><td>Sales yoy</td><td>Net profit</td><td>NP yoy</td></tr><tr><td colspan="26">Cosmetics</td></tr><tr><td>600315.SS</td><td>Shanghai Jahwa</td><td>1,795</td><td>5%</td><td>222</td><td>2%</td><td>2,015</td><td>14%</td><td>95</td><td>96%</td><td>3,209</td><td>13%</td><td>(5)</td><td>-393%</td><td>7,019</td><td>11%</td><td>312</td><td>17%</td><td>7,709</td><td>10%</td><td>611</td><td>96%</td><td>8,445</td><td>10%</td><td>892</td><td>46%</td></tr><tr><td>300957.SZ</td><td>Botanee</td><td>1,118</td><td>18%</td><td>66</td><td>133%</td><td>1,570</td><td>10%</td><td>272</td><td>25%</td><td>3,298</td><td>10%</td><td>330</td><td>27%</td><td>5,985</td><td>12%</td><td>668</td><td>32%</td><td>6,467</td><td>8%</td><td>744</td><td>11%</td><td>6,863</td><td>6%</td><td>804</td><td>8%</td></tr><tr><td>603605.SS</td><td>Proya</td><td>2,305</td><td>-2%</td><td>367</td><td>-6%</td><td>3,035</td><td>1%</td><td>390</td><td>-5%</td><td>5,760</td><td>10%</td><td>757</td><td>8%</td><td>11,100</td><td>5%</td><td>1,513</td><td>1%</td><td>12,055</td><td>9%</td><td>1,570</td><td>4%</td><td>13,309</td><td>10%</td><td>1,637</td><td>4%</td></tr><tr><td>688363.SS</td><td>Bloomage</td><td>829</td><td>-23%</td><td>65</td><td>-37%</td><td>970</td><td>-18%</td><td>84</td><td>-29%</td><td>1,765</td><td>-9%</td><td>61</td><td>-14%</td><td>3,564</td><td>-15%</td><td>210</td><td>-28%</td><td>4,589</td><td>29%</td><td>576</td><td>174%</td><td>4,913</td><td>7%</td><td>654</td><td>14%</td></tr><tr><td colspan="3">A-Shares Weighted Avg.</td><td>1%</td><td></td><td>7%</td><td></td><td>4%</td><td></td><td>14%</td><td></td><td>8%</td><td></td><td>14%</td><td></td><td>5%</td><td></td><td>8%</td><td></td><td>12%</td><td></td><td>49%</td><td></td><td>9%</td><td></td><td>16%</td></tr></table>

<table><tr><td>Ticker</td><td>Company</td></tr><tr><td>1318.HK</td><td>Mao Geping</td></tr><tr><td>2367.HK</td><td>Giant Biogene</td></tr><tr><td>2657.HK</td><td>Forest Cabin</td></tr><tr><td colspan="2">H-Shares Weighted Avg.</td></tr></table>

<table><tr><td colspan="4">1H26E</td><td colspan="4">2H26E</td><td colspan="4">2026E</td><td colspan="4">2027E</td><td colspan="4">2028E</td></tr><tr><td>Sales</td><td>Sales yoy</td><td>Net profit</td><td>NP yoy</td><td>Sales</td><td>Sales yoy</td><td>Net profit</td><td>NP yoy</td><td>Sales</td><td>Sales yoy</td><td>Net profit</td><td>NP yoy</td><td>Sales</td><td>Sales yoy</td><td>Net profit</td><td>NP yoy</td><td>Sales</td><td>Sales yoy</td><td>Net profit</td><td>NP yoy</td></tr><tr><td>3,321</td><td>28%</td><td>858</td><td>28%</td><td>3,231</td><td>31%</td><td>687</td><td>28%</td><td>6,552</td><td>30%</td><td>1,545</td><td>28%</td><td>7,977</td><td>22%</td><td>1,829</td><td>18%</td><td>9,179</td><td>15%</td><td>2,077</td><td>14%</td></tr><tr><td>2,895</td><td>-7%</td><td>928</td><td>-22%</td><td>3,064</td><td>27%</td><td>958</td><td>31%</td><td>5,959</td><td>8%</td><td>1,886</td><td>-1%</td><td>6,930</td><td>16%</td><td>2,181</td><td>16%</td><td>8,235</td><td>19%</td><td>2,650</td><td>21%</td></tr><tr><td>1,463</td><td>39%</td><td>261</td><td>30%</td><td>1,977</td><td>41%</td><td>304</td><td>52%</td><td>3,440</td><td>40%</td><td>565</td><td>41%</td><td>4,480</td><td>30%</td><td>684</td><td>21%</td><td>5,396</td><td>20%</td><td>795</td><td>16%</td></tr><tr><td></td><td>17%</td><td></td><td>6%</td><td></td><td>32%</td><td></td><td>33%</td><td></td><td>24%</td><td></td><td>16%</td><td></td><td>22%</td><td></td><td>18%</td><td></td><td>18%</td><td></td><td>18%</td></tr></table>

Source: Company data, GS Global Investment Research

Exhibit 2: We look for accelerated growth across cosmetics brands in 2Q26 Quarterly yoy growth comparison of players in the China cosmetics market

<table><tr><td colspan="2">Revenue yoy</td><td>1Q23</td><td>2Q23</td><td>3Q23</td><td>4Q23</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26</td><td>3Q26E</td><td>4Q26E</td></tr><tr><td colspan="2">China retail sales yoy</td><td>5.8%</td><td>10.7%</td><td>4.2%</td><td>8.3%</td><td>4.7%</td><td>2.6%</td><td>2.7%</td><td>3.8%</td><td>3.6%</td><td>4.4%</td><td>2.4%</td><td>0.7%</td><td>2.4%</td><td></td><td></td><td></td></tr><tr><td colspan="2">China cosmetics retail sales yoy</td><td>9.0%</td><td>13.7%</td><td>4.1%</td><td>2.4%</td><td>3.8%</td><td>3.0%</td><td>-0.1%</td><td>4.9%</td><td>5.4%</td><td>5.7%</td><td>10.0%</td><td>9.9%</td><td>5.9%</td><td></td><td></td><td></td></tr><tr><td colspan="18">Local brands (Consolidated)</td></tr><tr><td>Shanghai Jahwa</td><td>600315.SS</td><td>-6.5%</td><td>3.3%</td><td>-10.8%</td><td>-14.0%</td><td>-3.8%</td><td>-14.2%</td><td>-20.9%</td><td>-20.2%</td><td>-10.6%</td><td>25.4%</td><td>28.3%</td><td>12.8%</td><td>5.4%</td><td>13.5%</td><td>8.7%</td><td>17.8%</td></tr><tr><td>Botanee</td><td>300957.SZ</td><td>6.8%</td><td>21.2%</td><td>25.8%</td><td>-1.3%</td><td>27.1%</td><td>13.5%</td><td>14.0%</td><td>-17.8%</td><td>-13.5%</td><td>-16.7%</td><td>-9.9%</td><td>10.3%</td><td>17.8%</td><td>10.3%</td><td>10.4%</td><td>10.4%</td></tr><tr><td>Proya Cosmetics</td><td>603605.SS</td><td>29.3%</td><td>46.2%</td><td>21.4%</td><td>50.9%</td><td>34.6%</td><td>40.6%</td><td>21.2%</td><td>4.3%</td><td>8.1%</td><td>6.5%</td><td>-11.6%</td><td>-8.2%</td><td>-2.3%</td><td>1.1%</td><td>5.0%</td><td>12.5%</td></tr><tr><td>Bloomage</td><td>688363.SS</td><td>4.0%</td><td>5.3%</td><td>-17.3%</td><td>-9.0%</td><td>4.2%</td><td>-18.1%</td><td>-7.1%</td><td>-19.3%</td><td>-20.8%</td><td>-18.4%</td><td>-15.2%</td><td>-30.8%</td><td>-23.1%</td><td>-18.0%</td><td>-11.0%</td><td>-7.2%</td></tr><tr><td>Chicmax</td><td>2145.HK</td><td>25.7%</td><td></td><td>84.3%</td><td></td><td>120.7%</td><td></td><td>26.4%</td><td></td><td>17.3%</td><td></td><td>54.1%</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Giant Biogene</td><td>2367.HK</td><td>63.0%</td><td></td><td>39.1%</td><td></td><td>58.2%</td><td></td><td>56.3%</td><td></td><td>22.5%</td><td></td><td>-19.8%</td><td></td><td>-7.0%</td><td></td><td>27.3%</td><td></td></tr><tr><td>Mao Geping</td><td>1318.HK</td><td></td><td></td><td></td><td></td><td>41.0%</td><td></td><td>28.6%</td><td></td><td>31.3%</td><td></td><td>28.7%</td><td></td><td>28.3%</td><td></td><td>31.2%</td><td></td></tr><tr><td>Forest Cabin</td><td>2657.HK</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>98.3%</td><td></td><td>105.8%</td><td></td><td>39.1%</td><td></td><td>41.4%</td><td></td></tr><tr><td colspan="2">Average (excl. Giant, Chicmax, MGP, Forest Cabin)</td><td>11.6%</td><td>22.0%</td><td>13.0%</td><td>8.7%</td><td>20.2%</td><td>8.1%</td><td>6.6%</td><td>-1.1%</td><td>-1.7%</td><td>6.1%</td><td>1.0%</td><td>-4.0%</td><td>-0.5%</td><td>1.7%</td><td>3.3%</td><td>8.4%</td></tr><tr><td colspan="18">MNC brands (China revenue)</td></tr><tr><td>L&#x27;Oreal</td><td>OREP.PA</td><td>0.0%</td><td>16.2%</td><td>7.7%</td><td>n.a.</td><td>6.0%</td><td>0.8%</td><td>-MSD%</td><td>negative</td><td>1.0%</td><td></td><td>5.0%</td><td></td><td>MSD-HSD%</td><td></td><td></td><td></td></tr><tr><td>Amorepacific</td><td>090430.KS</td><td>-43.0%</td><td>23.2%</td><td>-18.4%</td><td>-43.6%</td><td>-20.0%</td><td>-50.0%</td><td>-40.0%</td><td>-10.0%</td><td>-15.0%</td><td>30.0%</td><td>18.0%</td><td>-10.0%</td><td>-13.5%</td><td>-20.3%</td><td>-5.3%</td><td>-18.7%</td></tr><tr><td>LGHH</td><td>051900.KS</td><td>-17.0%</td><td>-4.0%</td><td>-31.4%</td><td>-28.7%</td><td>9.5%</td><td>8.6%</td><td>18.3%</td><td>23.6%</td><td>-6.5%</td><td>-10.9%</td><td>4.6%</td><td>-19.0%</td><td>-12.3%</td><td></td><td></td><td></td></tr><tr><td>Shiseido</td><td>4911.T</td><td>-2.9%</td><td>20.0%</td><td>-9.0%</td><td>-21.0%</td><td>-2.6%</td><td>-10.6%</td><td>-13.2%</td><td>5.1%</td><td>-14.0%</td><td>-7.0%</td><td>8.0%</td><td>2.4%</td><td>-1.4%</td><td>4.9%</td><td>0.2%</td><td>-0.6%</td></tr><tr><td>Estee Lauder</td><td>EL</td><td>17.2%</td><td>40.9%</td><td>-12.3%</td><td>-11.7%</td><td>-7.2%</td><td>-6.0%</td><td>-16.0%</td><td>-10.0%</td><td>4.0%</td><td>-1.0%</td><td>9.0%</td><td>13.0%</td><td>6.0%</td><td>4.0%</td><td>6.5%</td><td>5.5%</td></tr><tr><td colspan="2">Average (excl. Amore)</td><td>-0.9%</td><td>19.0%</td><td>-17.6%</td><td>-20.5%</td><td>-0.1%</td><td>-2.7%</td><td>-3.6%</td><td>6.2%</td><td>-5.5%</td><td>-6.3%</td><td>7.2%</td><td>-1.2%</td><td>-2.6%</td><td>4.4%</td><td>3.3%</td><td>2.4%</td></tr><tr><td colspan="2">OPM</td><td>1Q23</td><td>2Q23</td><td>3Q23</td><td>4Q23</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td></tr><tr><td colspan="18">Local brands (Consolidated)</td></tr><tr><td>Shanghai Jahwa</td><td>600315.SS</td><td>9.2%</td><td>1.4%</td><td>0.1%</td><td>7.0%</td><td>17.0%</td><td>-5.6%</td><td>-10.7%</td><td>-25.4%</td><td>12.2%</td><td>4.4%</td><td>-2.6%</td><td>-12.1%</td><td>13.7%</td><td>5.6%</td><td>1.9%</td><td>-3.5%</td></tr><tr><td>Botanee</td><td>300957.SZ</td><td>16.0%</td><td>17.6%</td><td>14.5%</td><td>6.6%</td><td>14.7%</td><td>16.9%</td><td>-5.5%</td><td>6.0%</td><td>2.1%</td><td>11.5%</td><td>1.1%</td><td>16.3%</td><td>6.8%</td><td>12.4%</td><td>6.7%</td><td>15.3%</td></tr><tr><td>Proya Cosmetics</td><td>603605.SS</td><td>16.6%</td><td>19.2%</td><td>21.3%</td><td>14.6%</td><td>15.8%</td><td>17.6%</td><td>17.5%</td><td>18.1%</td><td>20.0%</td><td>16.2%</td><td>14.7%</td><td>16.5%</td><td>16.0%</td><td>13.9%</td><td>16.2%</td><td>16.5%</td></tr><tr><td>Bloomage</td><td>688363.SS</td><td>13.7%</td><td>14.0%</td><td>6.4%</td><td>5.7%</td><td>23.0%</td><td>8.4%</td><td>1.3%</td><td>-8.3%</td><td>12.0%</td><td>11.4%</td><td>4.1%</td><td>6.6%</td><td>10.9%</td><td>11.1%</td><td>4.0%</td><td>7.2%</td></tr><tr><td>Chicmax</td><td>2145.HK</td><td>5.0%</td><td></td><td>14.0%</td><td></td><td>13.5%</td><td></td><td>8.2%</td><td></td><td>12.4%</td><td></td><td>11.8%</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Giant Biogene</td><td>2367.HK</td><td>44.5%</td><td></td><td>46.7%</td><td></td><td>42.8%</td><td></td><td>39.8%</td><td></td><td>43.7%</td><td></td><td>31.6%</td><td></td><td>34.4%</td><td></td><td>33.5%</td><td></td></tr><tr><td>Mao Geping</td><td>1318.HK</td><td>30.9%</td><td></td><td>27.7%</td><td></td><td>30.6%</td><td></td><td>26.3%</td><td></td><td>33.7%</td><td></td><td>27.3%</td><td></td><td>33.9%</td><td></td><td>27.4%</td><td></td></tr><tr><td>Forest Cabin</td><td>2657.HK</td><td></td><td></td><td></td><td></td><td>18.7%</td><td></td><td>15.0%</td><td></td><td>19.6%</td><td></td><td>14.7%</td><td></td><td>19.8%</td><td></td><td>17.2%</td><td></td></tr><tr><td colspan="18">MNC brands (China OPM)</td></tr><tr><td>Amorepacific</td><td>090430.KS</td><td>0.5%</td><td>-23.9%</td><td>-18.2%</td><td>-41.5%</td><td>-6.4%</td><td>-48.7%</td><td>-41.0%</td><td>-13.0%</td><td>2.0%</td><td>7.0%</td><td>5.0%</td><td>LSD%</td><td>LSD%</td><td></td><td></td><td></td></tr><tr><td>LGHH (China only)</td><td>051900.

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
