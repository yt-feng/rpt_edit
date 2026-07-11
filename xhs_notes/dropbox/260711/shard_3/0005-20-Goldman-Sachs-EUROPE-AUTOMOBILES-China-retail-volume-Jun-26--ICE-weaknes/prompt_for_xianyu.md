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
EUROPE AUTOMOBILES

# China retail volume Jun-26: ICE weakness weighs on German JVs pending new product launches

China domestic passenger vehicle retail volume reached 1.60 mn units in Jun-2026, -23.2% yoy. Avg. list price increased +3.1% yoy (reflecting mix shift instead of incentive level, see appendix). By powertrain, NEV volume came in at 1.01mn units, -9.4% yoy (avg list price +9.2% yoy), while ICE volume was 594k units, -39.0% yoy (avg list price -0.5% yoy). NEV adoption rate stood at 62.9%.

On a rolling 3-month/R6M/R12M basis, PV retail volume is in an accelerating decline, down -22.2%/-20.0%/-10.0% yoy, driven by ICE (-38.3%/-26.3%/-18.7% yoy) while NEV held up better (-7.8%/-13.7%/-1.7% yoy), taking NEV penetration to 62.5%/54.1%/55.9%.

German OEM JVs declines were largely consistent with the weakness in the ICE segment. With c.95% of their volume still coming from ICE products, the near-term outlook remains challenging until the new products arrive.

□ Mercedes-Benz Cars sold 24,800 units in June (-41.8% yoy; 1.5% share, -49bps yoy), with the volume being almost entirely contributed by ICE. Over R3M/R6M/R12M, volumes down -32.8%/-31.2%/-28.3% yoy, yielding market shares of 1.7%/1.9%/1.7% (-27/-31/-45bps yoy).

☐ BMW brand delivered 33,073 units (-32.7% yoy; 2.1% share, -29bps yoy). Amid the product transition lull, volumes lean heavily on the 3- and 5-Series. On R3M/R6M/R12M, volumes fell -28.9%/-18.1%/-13.5%, translating to market shares of 2.2%/2.5%/2.2% (-21/+6/-9bps yoy).

□ Audi/AUDI's retail volume was 33,000 units (-35.3% yoy; 2.1% market share, -39bps yoy) and -23.3%/-15.7%/-6.0% across R3M/R6M/R12M (market shares of 2.3%/2.6%/2.5%, -3/+13/+10bps yoy). The new AUDI E7X EV, launched in May and just two months into sales, was Audi's 3rd best-selling nameplate in June, contributing substantially to volume.

☐ VW brand recorded 103,505 units (-37.2% yoy; 6.5% market share, -156bps yoy). R3M/R6M/R12M volumes tracked at -35.0%/-27.3%/-18.1%, equating to market shares of 6.6%/7.7%/7.7% (-159/-98/-106bps yoy). FAW-VW launched the Tayron L PHEV in June - volume contribution remains marginal as the model ramps.

Christian Frenes +44(20)7051-8641 | christian.frenes@gs.com GS International

Monika Mengting Liu, CFA +44(20)7051-7601 | monika.liu@gs.com GS International

Shivam Kotecha +1(332)245-7822 | shivam.kotecha@gs.com GS India SPL

Robert Triulzi  
+44(20)7552-2281 | robert.triulzi@gs.com GS International

## China retail volume overview

Market share top 10 at FY25  
NEV R1M retail volume yoy growth, %  
R1M Average MSRP (RMB)  
Exhibit 1: China domestic PV retail volume dashboard As of Jun-26

<table><tr><td colspan="2">PV retail volume (units)</td></tr><tr><td>R1M</td><td>1,601,924</td></tr><tr><td>R3M</td><td>4,495,533</td></tr><tr><td>R6M</td><td>8,721,468</td></tr><tr><td>R12M</td><td>21,564,129</td></tr></table>

<table><tr><td colspan="2">PV retail volume yoy growth (%)</td></tr><tr><td>R1M</td><td>-23.2%</td></tr><tr><td>R3M</td><td>-22.2%</td></tr><tr><td>R6M</td><td>-20.0%</td></tr><tr><td>R12M</td><td>-10.0%</td></tr></table>

![](images/53fc507717bfbd31e2c4b3f34b1851e4f64900e873ef069b467f859fc5d0f952.jpg)

## Historicals vs. recent R12M retail volume

<table><tr><td>Min</td><td>8,297,426</td><td>-61.5%</td></tr><tr><td>Max</td><td>24,320,214</td><td>12.8%</td></tr><tr><td>L5Y median</td><td>21,553,192</td><td>-0.1%</td></tr><tr><td>L10Y median</td><td>21,563,200</td><td>0.0%</td></tr><tr><td>Median since &#x27;10</td><td>20,188,372</td><td>-6.4%</td></tr></table>

<table><tr><td colspan="2">European OEMs China JV volume mix at FY25</td></tr><tr><td>Mercedes Cars</td><td>25%</td></tr><tr><td>BMW brand</td><td>25%</td></tr><tr><td>Audi/AUDI</td><td>36%</td></tr><tr><td>VW brand</td><td>40%</td></tr><tr><td>Volvo</td><td>19%</td></tr></table>

![](images/63bf6f1e11c01e543216946642cc29da28148ccfa92ed40dd3cd637ef9943b7a.jpg)

![](images/e67913d4b40907714c175f3fe534d3992077631f24f73bfdea8f1e3df7cb4136.jpg)

![](images/99134573a503350afb50534c30ccedab59fceb871dae976493a10e5ca9d1456a.jpg)  
Source: CPCA, Company data, GS Global Investment Research

## Exhibit 2: China NEV retail volume dashboard As of Jun-26. NEV = BEV/PHEV/EREV/FuelCell

<table><tr><td colspan="2">NEV retail volume (units)</td></tr><tr><td>R1M</td><td>1,007,633</td></tr><tr><td>R3M</td><td>2,807,583</td></tr><tr><td>R6M</td><td>4,716,209</td></tr><tr><td>R12M</td><td>12,056,764</td></tr></table>

<table><tr><td colspan="2">NEV retail volume yoy growth (%)</td></tr><tr><td>R1M</td><td>-9.4%</td></tr><tr><td>R3M</td><td>-7.8%</td></tr><tr><td>R6M</td><td>-13.7%</td></tr><tr><td>R12M</td><td>-1.7%</td></tr></table>

![](images/8d0fa8d212e35bc1396eede36bcc6037d757324502cc1819470cef4d700eb5e9.jpg)

<table><tr><td colspan="2">NEV share (%)</td></tr><tr><td>R1M</td><td>62.9%</td></tr><tr><td>R3M</td><td>62.5%</td></tr><tr><td>R6M</td><td>54.1%</td></tr><tr><td>R12M</td><td>55.9%</td></tr></table>

<table><tr><td colspan="2">R1M NEV mix in China by brand</td></tr><tr><td>Mercedes Cars</td><td>0.1%</td></tr><tr><td>BMW brand</td><td>6.1%</td></tr><tr><td>Audi/AUDI</td><td>15.1%</td></tr><tr><td>VW brand</td><td>2.3%</td></tr><tr><td>Volvo</td><td>44.4%</td></tr></table>

![](images/1090377af2258a9f34ce585e26e3bbf87f31e124ba0b78d9c61907abd31202c0.jpg)

![](images/8470f6c0c07168ca53a885631b79ac228809cda078af9e47f79c3305d7f84e28.jpg)  
Source: CPCA, GS Global Investment Research

![](images/d0c4245fe8a8426bd8df3a2132542e3e25b5c5cc06b88938c2e6cb8afdcc1a40.jpg)

## Exhibit 3: China ICE retail volume dashboard As of Jun-26

<table><tr><td colspan="2">ICE retail volume (units)</td></tr><tr><td>R1M</td><td>594,291</td></tr><tr><td>R3M</td><td>1,687,950</td></tr><tr><td>R6M</td><td>4,005,259</td></tr><tr><td>R12M</td><td>9,507,365</td></tr></table>

<table><tr><td colspan="2">ICE retail volume yoy growth (%)</td></tr><tr><td>R1M</td><td>-39.0%</td></tr><tr><td>R3M</td><td>-38.3%</td></tr><tr><td>R6M</td><td>-26.3%</td></tr><tr><td>R12M</td><td>-18.7%</td></tr></table>

![](images/8ef9011417fa0ced66086a99c7c6ef3ff5b906996d5e1ac7ce134db3d1924c95.jpg)

<table><tr><td colspan="2">ICE share (%)</td></tr><tr><td>R1M</td><td>37.1%</td></tr><tr><td>R3M</td><td>37.5%</td></tr><tr><td>R6M</td><td>45.9%</td></tr><tr><td>R12M</td><td>44.1%</td></tr></table>

![](images/3d031afa0c907f348417c0f341bb2a1b788a7018d51bf1d9dabc5d4d5fd3b8f6.jpg)

<table><tr><td colspan="2">R1M ICE mix in China by brand</td></tr><tr><td>Mercedes Cars</td><td>99.9%</td></tr><tr><td>BMW brand</td><td>93.9%</td></tr><tr><td>Audi/AUDI</td><td>84.9%</td></tr><tr><td>VW brand</td><td>97.7%</td></tr><tr><td>Volvo</td><td>55.6%</td></tr></table>

![](images/e45a7cfb4d79395822741bef7cba1f73a1f9e877109c17a48c5839fffe9179ce.jpg)

![](images/a26add19cd6ee12831c6131c0fc7090a1e9feefa8ed37201a221201b8c1b904a.jpg)  
Source: CPCA, GS Global Investment Research

Exhibit 4: Appendix: China BEV retail volume dashboard As of May-26

<table><tr><td colspan="2">BEV retail volume (units)</td></tr><tr><td>R1M</td><td>685,451</td></tr><tr><td>R3M</td><td>1,902,260</td></tr><tr><td>R6M</td><td>3,096,445</td></tr><tr><td>R12M</td><td>7,642,567</td></tr></table>

<table><tr><td colspan="2">BEV retail volume yoy growth (%)</td></tr><tr><td>R1M</td><td>3.7%</td></tr><tr><td>R3M</td><td>3.8%</td></tr><tr><td>R6M</td><td>-6.8%</td></tr><tr><td>R12M</td><td>5.8%</td></tr></table>

![](images/82cdf20cb4070a9cb3259f7889a478dee5abdce0596595791ee47ba434aced4a.jpg)

<table><tr><td colspan="2">BEV share (%)</td></tr><tr><td>R1M</td><td>42.8%</td></tr><tr><td>R3M</td><td>42.3%</td></tr><tr><td>R6M</td><td>35.5%</td></tr><tr><td>R12M</td><td>35.4%</td></tr></table>

![](images/d2679bd730ea410a93dee029be2d2d8852a2a8fa9bc1e0b522f879cc0636a588.jpg)

<table><tr><td colspan="2">RIM BEV mix in China by brand</td></tr><tr><td>Mercedes Cars</td><td>0.1%</td></tr><tr><td>BMW brand</td><td>6.1%</td></tr><tr><td>Audi/AUDI</td><td>15.1%</td></tr><tr><td>VW brand</td><td>1.5%</td></tr><tr><td>Volvo</td><td>2.2%</td></tr></table>

![](images/aa65f9039054fb2497cd8c6aced4830d9a7b8fa809b22991f903ea223c788e0b.jpg)  
Source: CPCA, GS Global Investment Research

![](images/aa79088cf27ed7afefce2c639d8f473e40f8983ca9c99901ec2d9802a7d0f800.jpg)

![](images/9e052cb36855eb6705e95786081aa2a7b559d5003d17c8808931d95abf1e062f.jpg)

## European OEM volume and market shares

Exhibit 5: Mercedes JV China retail volume dashboard As of Jun-26

<table><tr><td colspan="3">Registrations (units) and yoy (%)</td></tr><tr><td>R1M</td><td>24,800</td><td>-41.8%</td></tr><tr><td>R3M</td><td>77,598</td><td>-32.8%</td></tr><tr><td>R6M</td><td>165,727</td><td>-31.2%</td></tr><tr><td>R12M</td><td>376,668</td><td>-28.3%</td></tr></table>

<table><tr><td colspan="3">Historicals vs. recent R12M</td></tr><tr><td>Min</td><td>237,896</td><td>-36.8%</td></tr><tr><td>Max</td><td>693,720</td><td>84.2%</td></tr><tr><td>5yr median</td><td>564,339</td><td>49.8%</td></tr></table>

![](images/34acaebeec9db185c2bbcca99578e29aeaacc4bd9cc735a349877936e10b82b7.jpg)  
Source: CPCA, GS Global Investment Research

![](images/9e0501cd34d3c96ac87ca3942e07e68f0c09b2c18339dbe46617f05197593c1b.jpg)

![](images/d198c2f197a4424382cb59da7960a1517210a11ecec1375a943e7c3cd3d580dd.jpg)

Exhibit 6: BMW JV China retail volume dashboard As of Jun-26

<table><tr><td colspan="3">Registrations (units) and yoy (%)</td></tr><tr><td>R1M</td><td>33,073</td><td>-32.7%</td></tr><tr><td>R3M</td><td>98,059</td><td>-28.9%</td></tr><tr><td>R6M</td><td>220,972</td><td>-18.1%</td></tr><tr><td>R12M</td><td>484,682</td><td>-13.5%</td></tr></table>

<table><tr><td colspan="3">Historicals vs. recent R12M</td></tr><tr><td>Min</td><td>282,000</td><td>-41.8%</td></tr><tr><td>Max</td><td>717,269</td><td>48.0%</td></tr><tr><td>5yr median</td><td>640,345</td><td>32.1%</td></tr></table>

![](images/393ad07437703ca0a12e7361f2de309ae28a58cfd590fb5931ae90b7a2816e36.jpg)

![](images/0e9bc4c435b2e2bb88340ab9e839becf73f4ccdb96c558bb4c71448fa7c7f957.jpg)  
Source: CPCA, GS Global Investment Research

![](images/40fa2687707d5410bb4ab2af3dc84bd3864f9ecf1e0448b2a1fc188e19c5b5b7.jpg)

Exhibit 7: Audi JV China retail volume dashboard As of Jun-26

<table><tr><td colspan="3">Registrations (units) and yoy (%)</td></tr><tr><td>R1M</td><td>33,000</td><td>-35.3%</td></tr><tr><td>R3M</td><td>103,050</td><td>-23.3%</td></tr><tr><td>R6M</td><td>227,643</td><td>-15.7%</td></tr><tr><td>R12M</td><td>541,069</td><td>-6.0%</td></tr></table>

<table><tr><td colspan="3">Historicals vs. recent R12M</td></tr><tr><td>Min</td><td>505,087</td><td>-6.7%</td></tr><tr><td>Max</td><td>766,171</td><td>41.6%</td></tr><tr><td>5yr median</td><td>599,169</td><td>10.7%</td></tr></table>

![](images/bdd87bd46e00c0057ff66f304b73851d042a69382314661e25637090820d1a50.jpg)  
Source: CPCA, GS Global Investment Research

![](images/f5d233e6747020acfc8d18fe35a1334ed21f6b1faef43f2ff6297a3b4eb1a60b.jpg)

## Appendix

Exhibit 8: Jun-26 R1M avg. list price change +3.1% was mainly driven by sales growth of premium models like NIO ES9 (¥498k), NIO ES8 (¥407k) and Li Auto i6 (¥250k), largely offset by volume declines in Aito M8 EREV (¥360k), and introduction of entry models Leapmotor A10 (¥66k) and Changan Nevo Q05 (¥80k). In k RMB

China - retail volume yoy change by price range  
![](images/cc87f4107418903a726e915bdba779acaef23a02489b2fbf8bcd2c5f8c3de283.jpg)  
Source: CPCA, GS Global Investment Research

Exhibit 9: Jun-26 domestic retail volume by price range In k RMB

China - retail volume (units) by price range  
![](images/1da934dda9d824a9cee6065f759e20708b68b7668d0bc0bf4de611d4b01fd478.jpg)  
Source: CPCA, GS Global Investment Research

## Disclosure Appendix

## Reg AC

We, Christian Frenes, Monika Mengting Liu, CFA, Shivam Kotecha and Robert Triulzi, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Christian Frenes GS International, Monika Mengting Liu, CFA GS International, Shivam Kotecha GS India SPL, Robert Triulzi GS International.

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

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investmen

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
