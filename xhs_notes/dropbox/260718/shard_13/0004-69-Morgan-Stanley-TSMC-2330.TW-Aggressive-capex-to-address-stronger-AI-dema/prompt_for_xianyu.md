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
# Aggressive capex to address stronger AI demand; OW

Greater China Technology Semiconductors | Taiwan

<table><tr><td colspan="3">WHAT&#x27;S CHANGED</td></tr><tr><td>TSMC (2330.TW)</td><td>From</td><td>To</td></tr><tr><td>Price Target</td><td>NT$2,888.00</td><td>NT$2,988.00</td></tr></table>

Stronger capex points to larger and more urgent AI infra demand. TSMC remains the primary, if not the only, 2nm/1.4nm foundry option for major customers over the next five years.

2026 full-year revenue guidance a strong beat: TSMC hosted its 2Q26 earnings call today. It raised its 2026 revenue growth guidance to >40% Y/Y (previously >30% Y/Y). In our 6/28 preview, we expected guidance to increase to 40% Y/Y vs. Consensus 35%-40%. Management attribute upside to strong AI demand despite challenging consumer demand. CSP customers are rapidly increasing cloud capex. TSMC did not update its AI semiconductor revenue CAGR forecast but indicated it is tracking above its previous 55%-60% forecast. We believe a 70%-80% CAGR for TSMC's AI semiconductor business is reasonable.

Capex hike implies urgent AI demand: TSMC raised its 2026 capex target to US \$60–64bn (vs. the previous US\$52–56bn), implying some equipment cost inflation. We attribute the additional US\$8bn to: (1) US\$3bn of cost inflation (reflecting a 5% increase in equipment prices), and (2) US\$5bn of equipment prepayments, given that TSMC is not adding new clean-room capacity this year. These equipment prepayments suggest urgent AI demand, particularly for agentic AI-related CPUs and GPUs. Management said A14 would be an even larger node than 2nm and announced an additional US\$100bn of capex for its US fabs, which we believe supports higher revenue after 2028 than we previously expected.

Do we need to worry about gross margin “miss” and foundry competition? In response to our question on competition from Samsung Foundry and Intel Foundry, management indicated that key customers share their five-year production roadmaps with TSMC, implying TSMC will remain the primary source for customers' top products. We expect TSMC could increase leading-edge wafer pricing by another 5%–10% in 2027, given the value it provides in leading-edge foundry services. On gross margin guidance, the 3Q26 midpoint is 66% vs. MSe 67.5%, reflecting dilution from 2nm. While this falls below some unrealistic 70% Street forecasts, we reiterate our view to buy on any weakness post-Street margin forecast miss. TSMC consistently reminds investors about dilution from 2nm and overseas fabs. We do not believe the margin "miss" reflects foundry competition.

Raise PT to NT\$2,988; stay OW: We raise our 2026–2028 revenue assumptions to reflect stronger AI semiconductor revenue growth. TSMC's high-quality earnings profile should continue to attract fund flows in a volatile market environment. Upcoming 2Q26 cloud capex updates from CSPs are likely key catalysts.

<table><tr><td colspan="2">MS TAIWAN LIMITED+</td></tr><tr><td colspan="2">Charlie Chan</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Charlie.Chan@morganstanley.com</td><td>+886 2 2730-1725</td></tr><tr><td colspan="2">Daniel Yen, CFA</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Daniel.Yen@morganstanley.com</td><td>+886 2 2730-2863</td></tr><tr><td colspan="2">MS ASIA LIMITED+</td></tr><tr><td colspan="2">Daisy Dai, CFA</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Daisy.Dai@morganstanley.com</td><td>+852 2848-7310</td></tr><tr><td colspan="2">MS TAIWAN LIMITED+</td></tr><tr><td colspan="2">Tiffany Yeh</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Tiffany.Yeh@morganstanley.com</td><td>+886 2 7712-3032</td></tr><tr><td colspan="2">Lucas Wang</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Lucas.Wang@morganstanley.com</td><td>+886 2 2730-2875</td></tr></table>

![](images/5c6de7fe20423cbdea15a171691a05c50bbf40ac62d491bdaa9c71306b32bbe7.jpg)

## TSMC (2330.TW, 2330 TT)

<table><tr><td>Stock Rating</td><td>Overweight</td></tr><tr><td>Industry View</td><td>Attractive</td></tr><tr><td>Price target</td><td>NT$2,988.00</td></tr><tr><td>Up/downside to price target (%)</td><td>21</td></tr><tr><td>Shr price, close (Jul 16, 2026)</td><td>NT$2,470.00</td></tr><tr><td>Mkt cap, curr (mn)</td><td>NT$64,042,111</td></tr><tr><td>Avg daily trading value (mn)</td><td>NT$65,119</td></tr></table>

<table><tr><td>Fiscal Year Ending</td><td>12/25</td><td>12/26e</td><td>12/27e</td><td>12/28e</td></tr><tr><td>EPS (NT$)**</td><td>66.25</td><td>111.08</td><td>144.93</td><td>183.55</td></tr><tr><td>Prior EPS (NT$)**</td><td>-</td><td>107.56</td><td>143.01</td><td>177.30</td></tr><tr><td>EPS (NT$)§</td><td>64.56</td><td>100.37</td><td>130.74</td><td>166.68</td></tr><tr><td>ModelWare net inc (NT $ bn)</td><td>1,718</td><td>2,874</td><td>3,758</td><td>4,759</td></tr><tr><td>P/E</td><td>23.4</td><td>22.3</td><td>17.0</td><td>13.5</td></tr><tr><td>Div yld (%)</td><td>1.4</td><td>1.1</td><td>1.4</td><td>1.7</td></tr></table>

Unless otherwise noted, all metrics are based on MS ModelWare framework
\*\* = Based on consensus methodology
§ = Consensus data is provided by Refinitiv Estimates
e = MS estimates

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## 2Q26 earnings and 3Q26 guidance review

TSMC hosted its 2Q26 earnings call on July 16. The company's 2Q26 results and 3Q26 guidance fall in line with our Catalyst preview Scenarios 1 and 2, where we assume the stock moves up 1%-5% over the coming trading days. See Exhibit 1 and Exhibit 2 for our review of the quarterly results and guidance.

2Q26 gross margin of 67.7% is roughly in line with MSe 67.4% and above the company's initial guidance range of 65.5%-67.5%. TSMC's 3Q26 revenue growth guidance of 12% Q/Q at the mid-point is also in line with our bullish forecast of 10-15% Q/Q. The flattish 3Q26 gross margin figure is in line with our preview, but lower than some bullish buy-side expectations of 70%. We therefore recommend investors buy on any weakness should the share price decline following the margin miss.

We now assume 2026-2028 three-year capex of US\$213bn vs. US\$206bn previously.

Exhibit 1: TSMC 2Q26 Earnings review

<table><tr><td rowspan="2">(NT$ mn)</td><td colspan="5">2Q26</td></tr><tr><td>Actual</td><td>Q/Q</td><td>Y/Y</td><td>MS Est.</td><td>Consensus</td></tr><tr><td colspan="6">Financials</td></tr><tr><td>Revenue</td><td>1,270,380</td><td>12.0%</td><td>36.0%</td><td>1,266,623</td><td>1,267,975</td></tr><tr><td>Opex</td><td>(93,708)</td><td>1.5%</td><td>11.6%</td><td>(96,667)</td><td>(109,471)</td></tr><tr><td>EPS (NT$)</td><td>27.25</td><td>23.4%</td><td>77.4%</td><td>25.08</td><td>24.33</td></tr><tr><td colspan="6">Ratios</td></tr><tr><td>GM (%)</td><td>67.7%</td><td>147bps</td><td>910bps</td><td>67.4%</td><td>67.3%</td></tr><tr><td>Opex (%)</td><td>7.4%</td><td>-76bps</td><td>-161bps</td><td>7.6%</td><td>8.6%</td></tr><tr><td>OPM (%)</td><td>60.3%</td><td>224bps</td><td>1,072bps</td><td>59.8%</td><td>58.7%</td></tr></table>

Source: Company Data, Visible Alpha, MS estimates

Exhibit 2: TSMC 3Q26 Guidance review

<table><tr><td rowspan="2">(NT$ mn)</td><td colspan="5">3Q26</td></tr><tr><td>Guidance</td><td>MS Est.</td><td>Q/Q</td><td>Y/Y</td><td>Consensus</td></tr><tr><td colspan="6">Financials</td></tr><tr><td>Revenue</td><td>US$44.6bn to US$45.8bn,+12% Q/Q increase at mid-point</td><td>1,435,872</td><td>13.0%</td><td>45.0%</td><td>1,385,740</td></tr><tr><td>Opex</td><td></td><td>(104,250)</td><td>11.2%</td><td>18.7%</td><td>(116,721)</td></tr><tr><td>EPS (NT$)</td><td></td><td>29.21</td><td>7.2%</td><td>67.5%</td><td>27.21</td></tr><tr><td colspan="6">Ratios</td></tr><tr><td>GM (%)</td><td>65.0% - 67.0%</td><td>67.5%</td><td>-20bps</td><td>807bps</td><td>66.4%</td></tr><tr><td>Opex (%)</td><td></td><td>7.3%</td><td>-12bps</td><td>-161bps</td><td>8.4%</td></tr><tr><td>OPM (%)</td><td>56.0% - 58.0%</td><td>60.3%</td><td>-8bps</td><td>969bps</td><td>58.0%</td></tr></table>

Source: Company Data, Visible Alpha, MS estimates

## AI semi demand remains strong and requires additional capex

## TSMC's 2026–2028 foundry floorplan broadly aligns with our bottom-up demand analysis

Our industry checks suggest ASML allocates capacity based largely on historical demand and long-term partnerships, indicating that TSMC remains the largest customer for EUV shipments. If so, TSMC should retain strong pricing power and could increase leading-edge wafer prices by 5%–10% in 2027, reflecting both the value it delivers to customers and the potential for margin expansion.

Exhibit 3: TSMC – Wafer pricing trend  
![](images/f3e0dee3aaecfb686d6ae367bbfc97ef60dc20e88bfcfb7b679ece64d7d44126.jpg)  
Source: Company data, MS (e) estimates

Exhibit 4: TSMC's GM and depreciation trends – 60% should be the floor  
![](images/413854ce85d05ab50eb7c869a71c1a6993e29f0975c0a8460702b3e8be7de4b7.jpg)  
Source: Company data, MS (e) estimates

Exhibit 5:  
TSMC's capex intensity should drop significantly as a result of robust revenue growth  
![](images/d09f469ecb3fb1bcebdcb64455b908d124dd7b26cc45cc0f5ca98fa6b5fee91e.jpg)  
Source: Company data, MS estimates

## TSMC revealed strong capacity growth in 2nm and 3nm with 5nm set to decline

Consistent with our demand forecast, TSMC indicated very strong capacity requirements for both 2nm and 3nm starting in 2026E, implying a 70% capacity CAGR for N2 from 2026E to 2028E. TSMC also suggested that 5nm capacity will begin to decline from 2027, in line with our forecast that 5nm demand will fall as Blackwell transitions to Rubin on 3nm.

Separately, advanced packaging capacity expansion should remain a key focus for TSMC in 2027. This includes, but is not limited to, CoWoS and SolC, for which we now expect capacity to reach 200kwpm and 70kwpm, respectively, by 2027.

Exhibit 6: TSMC – Our estimate of 2nm customer demand breakdown  
![](images/c241d399b91bfae52c010c4c35897d84b784b297a5d14e5d97173a8390614ef4.jpg)  
Source: MS estimates

Exhibit 7: TSMC suggests N2 capacity can be >70% CAGR from 2026-2028e  
![](images/3d1d08609342e178b6bb7fddf61425dc44201c70e3bcacaf2b9358b03f4c2c24.jpg)  
Source: TSMC

Since nodes below 3nm should also continue to see strong demand, our checks suggest TSMC's 2nm/1.6nm capacity could approach 100kwpm by end-2026, increase to 150–170kwpm in 2027, and exceed 200kwpm in 2028. We expect 1.4nm to begin pulling in tools in 2027, with the bulk of capacity ramping in 2028. Looking further ahead, we expect TSMC to introduce initial 1.0nm capacity in Tainan in 2029.

Exhibit 8: TSMC fab roadmap

<table><tr><td rowspan="2">Node</td><td rowspan="2">Location</td><td rowspan="2">Fab</td><td colspan="5">Capacity</td></tr><tr><td>2025</td><td>2026</td><td>2027</td><td>2028</td><td>2029</td></tr><tr><td rowspan="3">N3</td><td>Tainan</td><td>F18 - P4/P5/P6/P8/P9</td><td>110k</td><td>160-170k</td><td></td><td></td><td></td></tr><tr><td>Arizona</td><td>F21 - P2</td><td></td><td>20k</td><td></td><td></td><td></td></tr><tr><td>Japan</td><td>F23 - P2</td><td></td><td></td><td></td><td>15k</td><td></td></tr><tr><td>Total</td><td></td><td></td><td>110k</td><td>180-190k</td><td>190k</td><td>200-205k</td><td></td></tr><tr><td rowspan="4">N2/A16</td><td>HsinChu</td><td>F20 - P1/P2</td><td>20k</td><td>30k</td><td></td><td></td><td></td></tr><tr><td>Tainan</td><td>F22 - P7/P8/P9</td><td></td><td></td><td>40-50k</td><td>60k</td><td></td></tr><tr><td>KaoHsiung</td><td>F22 - P1/P2/P3/P4/P5/P6</td><td>25k</td><td>60k</td><td>80-90k</td><td>100k</td><td></td></tr><tr><td>Arizona</td><td>F21 - P3/P4/P5/P6</td><td></td><td></td><td></td><td>20k</td><td></td></tr><tr><td>Total</td><td></td><td></td><td>45k</td><td>90-100k</td><td>150-170k</td><td>210k</td><td></td></tr><tr><td>A14</td><td>HsinChu</td><td>F20 - P3/P4</td><td></td><td></td><td>10-20k</td><td>30-40k</td><td>40k</td></tr><tr><td>A14/A13/A12</td><td>Taichung</td><td>F25 - P1/P2/P3/P4</td><td></td><td></td><td>10-20k</td><td>30-40k</td><td>80k</td></tr><tr><td>Total</td><td></td><td></td><td></td><td></td><td>20-40k</td><td>60-80k</td><td>120k</td></tr><tr><td>A10</td><td>Tainan</td><td>F26 - P1/P2/P3/P4</td><td></td><td></td><td></td><td></td><td>5k</td></tr><tr><td>N40/28/22/12</td><td>Japan</td><td>F23 - P1</td><td>25k</td><td></td><td></td><td></td><td></td></tr><tr><td>N28/16</td><td>Germany</td><td>F24</td><td></td><td></td><td>5k</td><td>40k</td><td></td></tr></table>

Source: MS estimates

Exhibit 9: TSMC fab details

<table><tr><td>Front-end Plant</td><td>Location</td><td>Focused Technology</td></tr><tr><td>F18 - P4/P5/P6/P8/P9</td><td>Tainan</td><td>N3</td></tr><tr><td>F20 - P1/P2/P3/P4</td><td>HsinChu</td><td>N2/A14</td></tr><tr><td>F21 - P2</td><td>Arizona</td><td>N3</td></tr><tr><td>F22 - P1/P2/P3/P5/P6</td><td>KaoHsiung</td><td>N2</td></tr><tr><td>F22 - P7/P8/P9</td><td>Tainan</td><td>N2</td></tr><tr><td>F22 - P4</td><td>KaoHsiung</td><td>A16</td></tr><tr><td>F23 - P2</td><td>Kumamoto</td><td>N3</td></tr><tr><td>F25 - P1/P2/P3/P4</td><td>Taichung</td><td>A14</td></tr><tr><td>F26 - P1/P2/P3/P4</td><td>Tainan</td><td>A10</td></tr></table>

Source: MS estimates

## Non-AI demand – China's smartphone chip inventory correction begins, but the impact on TSMC should be limited

In 1Q26, we saw semiconductor industry inventory days increase amid strong AI and peripheral demand. Some consumer and non-AI customers also refrained from cutting orders given tight capacity across the supply chain and the prospect of foundry price increases in 2H26 and 2027. However, we believe it is now time for these non-AI customers, particularly in smartphones and PCs, to address rising BOM costs either by reducing orders or passing through higher costs. Even so, we expect the impact on TSMC to remain limited, as its consumer customer base is concentrated in the premium segment, where passing through higher costs is generally easier. In addition, high-end PCs and smartphones primarily consume leading-edge capacity at TSMC, which AI demand can readily absorb once any wafer capacity becomes available.

Apple provides an example of successful price increases to end customers (see Apple, Inc.: As Expected, Apple Is Raising Product Pricing (25 Jun 2026) by Erik Woodring) while maintaining the same wafer demand at TSMC based on our checks.

In contrast, Chinese smartphone shipments are tracking at down 20% Y/Y, compared with our previous assumption of down 15% Y/Y (see our MediaTek report). Even so, we expect AI demand to quickly backfill any leading-edge wafer capacity, particularly at 5nm and below.

## Earnings estimate revisions

We raise our earnings forecasts 3% for 2026, 1% for 2027 and 4% for 2028: We raise our 2026 revenue forecast and modestly increase our margin assumptions to reflect stronger-than-expected 2Q26 performance, driven by robust AI demand, including sustained Blackwell shipments. We also raise our 2027–2028 revenue assumptions by 1%–3%, reflecting the increase in 2026 capex guidance from US\$54bn to US\$62bn at the midpoint.

Exhibit 11: TSMC: Earnings revision

<table><tr><td>(NT$ mn)</td><td>New 2026e</td><td>Old 2026e</td><td>Diff.%</td><td>New 2027e</td><

[中间内容因长度限制已省略]

tronics Corp (8299.TWO)</td><td>E (02/25/2026)</td><td>NT$1,980.00</td></tr><tr><td>SG Micro Corp. (300661.SZ)</td><td>E (11/03/2025)</td><td>Rmb107.32</td></tr><tr><td>Silergy Corp. (6415.TW)</td><td>U (05/19/2026)</td><td>NT$473.00</td></tr><tr><td>SMIC (0981.HK)</td><td>O (10/21/2025)</td><td>HK$75.20</td></tr><tr><td>TSMC (2330.TW)</td><td>O (02/07/2022)</td><td>NT$2,470.00</td></tr><tr><td>UMC (2303.TW)</td><td>O (05/19/2026)</td><td>NT$160.00</td></tr><tr><td>Vanguard International Semiconductor (5347.TWO)</td><td>E (01/14/2026)</td><td>NT$187.50</td></tr><tr><td>WIN Semiconductors Corp (3105.TWO)</td><td>U (07/14/2025)</td><td>NT$369.00</td></tr><tr><td colspan="3">Daisy Dai, CFA</td></tr><tr><td>ASMPT Ltd (0522.HK)</td><td>O (07/24/2025)</td><td>HK$177.50</td></tr><tr><td>China Resources Microelectronics Limited (688396.SS)</td><td>U (03/02/2026)</td><td>Rmb65.50</td></tr><tr><td>Empyrean Technology Co Ltd (301269.SZ)</td><td>E (01/17/2025)</td><td>Rmb106.21</td></tr><tr><td>Hangzhou Silan Microelectronics Co. Ltd. (600460.SS)</td><td>U (08/25/2025)</td><td>Rmb36.22</td></tr><tr><td>Hygon Information Technology Co., Ltd. (688041.SS)</td><td>O (07/03/2026)</td><td>Rmb320.40</td></tr><tr><td>Innoscience (2577.HK)</td><td>E (10/13/2025)</td><td>HK$48.00</td></tr><tr><td>JCET Group Co Ltd (600584.SS)</td><td>E (01/16/2026)</td><td>Rmb83.21</td></tr><tr><td>Shanghai Fudan Microelectronics (1385.HK)</td><td>O (03/07/2025)</td><td>HK$28.10</td></tr><tr><td>SICC Co Ltd (688234.SS)</td><td>O (03/20/2026)</td><td>Rmb120.24</td></tr><tr><td>StarPower Semiconductor Ltd (603290.SS)</td><td>E (05/14/2026)</td><td>Rmb97.93</td></tr><tr><td>Unigroup Guoxin Microelectronics Co Ltd (002049.SZ)</td><td>U (01/10/2023)</td><td>Rmb70.16</td></tr><tr><td>Universal Scientific Ind. (Shanghai) (601231.SS)</td><td>O (11/05/2025)</td><td>Rmb26.10</td></tr><tr><td>Yangjie Technology (300373.SZ)</td><td>O (06/10/2022)</td><td>Rmb101.70</td></tr><tr><td colspan="3">Daniel Yen, CFA</td></tr><tr><td>AP Memory Technology Corp (6531.TW)</td><td>O (07/11/2025)</td><td>NT$909.00</td></tr><tr><td>ASMedia Technology Inc (5269.TW)</td><td>U (10/03/2025)</td><td>NT$1,515.00</td></tr><tr><td>Aspeed Technology (5274.TWO)</td><td>O (06/09/2025)</td><td>NT$13,905.00</td></tr><tr><td>Egis Technology Inc (6462.TWO)</td><td>E (01/28/2026)</td><td>NT$101.50</td></tr><tr><td>Elan Microelectronics Corp (2458.TW)</td><td>O (10/03/2025)</td><td>NT$175.50</td></tr><tr><td>Espressif Systems (688018.SS)</td><td>O (05/15/2023)</td><td>Rmb120.61</td></tr><tr><td>GigaDevice Semiconductor Beijing Inc (603986.SS)</td><td>O (05/15/2025)</td><td>Rmb514.61</td></tr><tr><td>Macronix International Co Ltd (2337.TW)</td><td>O (09/18/2025)</td><td>NT$136.50</td></tr><tr><td>Montage Technology Co Ltd (6809.HK)</td><td>O (03/18/2026)</td><td>HK$278.60</td></tr><tr><td>Montage Technology Co Ltd (688008.SS)</td><td>O (03/18/2026)</td><td>Rmb211.13</td></tr><tr><td>Novatek (3034.TW)</td><td>U (02/04/2026)</td><td>NT$471.50</td></tr><tr><td>Nuvoton Technology Corporation (4919.TW)</td><td>U (11/10/2025)</td><td>NT$156.50</td></tr><tr><td>Parade Technologies Ltd (4966.TWO)</td><td>O (05/27/2026)</td><td>NT$631.00</td></tr><tr><td>Powerchip Semiconductor Manufacturing Co (6770.TW)</td><td>O (10/27/2025)</td><td>NT$76.50</td></tr><tr><td>Realtek Semiconductor (2379.TW)</td><td>E (01/30/2026)</td><td>NT$712.00</td></tr><tr><td>Shenzhen Goodix Technology Co Ltd (603160.SS)</td><td>U (07/14/2025)</td><td>Rmb54.83</td></tr><tr><td>Winbond Electronics Corp (2344.TW)</td><td>O (05/28/2026)</td><td>NT$172.00</td></tr><tr><td>WPG Holdings (3702.TW)</td><td>O (03/16/2026)</td><td>NT$113.50</td></tr><tr><td>WT Microelectronics Co. Ltd. (3036.TW)</td><td>O (01/27/2026)</td><td>NT$196.00</td></tr><tr><td colspan="3">Duan Liu</td></tr><tr><td>Dosilicon Co Ltd (688110.SS)</td><td>U (09/06/2024)</td><td>Rmb136.50</td></tr><tr><td>Shenzhen Longsys Electronics Co Ltd (301308.SZ)</td><td>E (02/25/2026)</td><td>Rmb463.59</td></tr><tr><td colspan="3">Tiffany Yeh</td></tr><tr><td>AllRing Tech Co. (6187.TWO)</td><td>O (09/23/2025)</td><td>NT$1,075.00</td></tr><tr><td>FOCI Fiber Optic Communications Inc (3363.TWO)</td><td>O (01/15/2025)</td><td>NT$555.00</td></tr><tr><td>Himax Technologies Inc (HIMX.O)</td><td>E (02/04/2026)</td><td>US$13.92</td></tr><tr><td>Hon Precision (7769.TW)</td><td>O (04/17/2026)</td><td>NT$6,695.00</td></tr><tr><td>MPI Corporation (6223.TWO)</td><td>O (04/17/2026)</td><td>NT$6,220.00</td></tr><tr><td>Silicon Motion (SIMO.O)</td><td>O (05/06/2024)</td><td>US$293.40</td></tr><tr><td>WinWay Technology Co Ltd (6515.TW)</td><td>O (04/17/2026)</td><td>NT$6,735.00</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## © 2026 MS
"""
