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
# Greater China Semiconductors | Asia Pacific

# Power Semis – Supply Driven Upcycle

Global power discrete sales returned to growth since 4Q25. On the back of limited capacity additions in the past two years, we expect power semi pricing to rise further in 2H26. We like Yangjie (OW) on auto localization, while staying UW on Silan Micro and CR Micro on hyped expectations.

Overall power discrete sales back to growth since 4Q25: Global power discrete revenue growth is now tracking at 16% YoY in April and the yoy growth was back to positive territory since 4Q25 (Exhibit 1). Many Greater China power discrete companies issued price hike notices in Feb 2026, citing higher raw material prices and foundry costs. Except for IGBT for automotive customers, distributors and other end-market customers were willing to accept the price hikes, given low inventory and fears of even higher pricing in 2H26. We think pricing power could support gross margin, with gradual improvement expected for the rest of the year.

Mixed demand picture: robust industrial demand, slower EV growth, and weak solar demand: Auto and industrial segments accounted for 72% of total demand in power discrete in 2025, so the power semi market is less affected by weak smartphone and PC sell-through this year due to memory price hikes. Industrial demand is strong, and leading industrial automation companies' revenue grew at 21% in 1Q26 (Exhibit 4). China EV wholesale growth (3MMA) was tracking at 7% yoy in May, up from zero in April (Exhibit 3). Solar demand was weak, with YTD capacity additions down 51% yoy.

Limited supply additions in the past two years: Global leading power discrete companies' capex declined for two consecutive years, and this year we saw a mild capex increase of around 11% (Exhibit 5). In China, we expect limited capacity additions in power discrete (IGBT, MOSFET etc.) in the next three years, as companies like Silan Micro and UNT (688469.SS, NC) shift focus to AI power management (PMIC, etc.). Given limited capacity additions and high utilization, we think if demand does not sharply deteriorate, the upward pricing trend could sustain into 2H26.

## We like Yangjie (OW), and raise PTs for Yangjie, Silan Micro and CR Micro:

Although we are positive on power discrete pricing, we think it is a supply-driven upcycle. We raise PTs for Yangjie, Silan Micro and CR Micro but make no rating changes. We remain OW on Yangjie Technology – auto is rising in its mix, and operating efficiency is strong. We remain UW on Silan Micro and CR Micro on hyped expectations. We are EW on Starpower due to depreciation concerns.

MS ASIA LIMITED+

## Daisy Dai, CFA

Equity Analyst

Daisy.Dai@morganstanley.com +852 2848-7310

MS TAIWAN LIMITED+

## Charlie Chan

Equity Analyst

Charlie.Chan@morganstanley.com +886 2 2730-1725

## Daniel Yen, CFA

Equity Analyst

Daniel.Yen@morganstanley.com +886 2 2730-2863

## Tiffany Yeh

Equity Analyst

Tiffany.Yeh@morganstanley.com +886 2 7712-3032

MS ASIA LIMITED+

## Henry Zhao

Research Associate

Henry.Zhao@morganstanley.com +852 2239-7731

## Ethan Jia

Research Associate

Ethan.Jia@morganstanley.com +852 3963-2287

## Asia Summer School 2026

![](images/e4ebfb26e7ae22647a5f3eda113d63be60c9a1c9424225b625af990f1cae6142.jpg)

GREATER CHINA TECHNOLOGY SEMICONDUCTORS

<table><tr><td colspan="2">Asia Pacific Industry View</td><td>Attractive</td></tr><tr><td colspan="3">WHAT&#x27;S CHANGED</td></tr><tr><td>Hangzhou Silan Microelectronics Co. Ltd. (600460.SS)Price Target</td><td>FromRmb20.00</td><td>ToRmb26.90</td></tr><tr><td>Yangjie Technology (300373.SZ)Price Target</td><td>FromRmb91.00</td><td>ToRmb136.00</td></tr><tr><td>China Resources Microelectronics Limited (688396.SS)Price Target</td><td>FromRmb43.00</td><td>ToRmb51.60</td></tr></table>

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

Earnings Estimates Revisions

<table><tr><td>Ticker</td><td>Company</td><td>Earnings estimates revision and price target change</td></tr><tr><td>300373.SZ</td><td>Yangjie Technology</td><td>We raise EPS estimates by 3%/6%/9% for 2026/27/28 respectively: We expect stronger sales growth, mainly from better industrial demand, and we also raise our gross margin assumption on better power discrete pricing. We expect Yangjie&#x27;s overseas business could also grow strongly on the back of its Vietnam packaging and foundry capacity ramp.We raise our price target by 50% to Rmb136 from Rmb91: We factor in earnings estimate changes and raise our intermediate growth rate to 18% from 15% previously, as the company decides to allocate more funding to automotive and AI infrastructure related power devices. We continue to derive our base case/price target from a residual income model. All other assumptions are unchanged, including an 8.4% cost of equity (beta 1.06, risk-free rate 2.0% and risk premium 6.0%) and a terminal growth rate of 5.5%, in line with other semiconductor companies we cover.Our base case value/price target implies 33x our 2027e EPS.Our bull and bear case values also rise 50% to Rmb173.8 and Rmb53.4, respectively, implying 42x and 13x our 2027e EPS, in line with our base case change.</td></tr><tr><td>688396.SS</td><td>CR Micro</td><td>We raise our EPS estimates by 9%/14%/14% for 2026/27/28: We raise our sales forecasts slightly on better industrial demand, and we also raise our margin assumptions. We expect CR Micro&#x27;s power semis prices could go up further on the back of full utilization. While the company continues to expand capacity in Shenzhen, it is mainly for YMTC&#x27;s outsourcing orders, with limited capacity additions in power semis.We raise our target price by 20% to Rmb51.6 from Rmb43.0: Our new price target reflects the changes in our earnings estimates. We derive our price target from a residual income model, which we believe best captures the stock&#x27;s long-term value. Our key assumptions include: an 8.2% cost of equity (beta 1.04, risk-free rate 2.0% and risk premium 6.0%; all unchanged), a medium-term growth rate of 19% and a terminal growth rate of 5.5%. We raise our bull case to Rmb109.7 from Rmb91.4, and our bear case to Rmb24.5 from Rmb20.4, both in line with our base case/price target adjustment.</td></tr><tr><td>600460.SS</td><td>Silan Micro</td><td>We raise our 2026/27/28 EPS forecasts by 4%/6%/9%: We raise our sales forecasts slightly on better industrial demand, and we also raise our margin assumptions. Silan Micro has a higher portion of sales through distributors. We think it would be easier for them to raise prices vs. peers, which have more direct sales.We raise our price target by 35% to Rmb26.9 from Rmb20: Our new price target reflects the changes in our earnings estimates. We also raise the payout ratio to 20% from 5%, as we expect the company to increase payout given higher net margin.We continue to derive our price target (base case scenario value) from a residual income model. Our key assumptions are unchanged: an 8.6% cost of equity (beta 1.1, risk-free rate 2.0%, and risk premium 6.0%), an intermediate growth rate of 18% and a terminal growth rate of 5.5%.We raise our bull case value by 70% to Rmb61.2 from Rmb36.1, the upward revision is higher than our base case change, considering higher operating leverage of Silan&#x27;s IDM model compared to its peers (design houses or fab-lite business model). Our bear case value is raised by 35% to Rmb16.8 from Rmb12.5, due to better pricing environment and margin improvement.</td></tr></table>

## Power Semi Industry Tracker

Exhibit 1: Total discrete revenue yoy growth turned positive since 4Q25  
![](images/563a7d0f9081e0d60348cc3a4231258a0b6591e5dbfa07f0c1efa974d2a25cb4.jpg)

<details>
<summary>line chart</summary>

| Date   | Discrete YoY growth (3MMA) |
|--------|-----------------------------|
| Mar-95 | ~45%                        |
| Mar-98 | ~10%                        |
| Mar-01 | ~40%                        |
| Mar-04 | ~20%                        |
| Mar-07 | ~10%                        |
| Mar-10 | ~65%                        |
| Mar-13 | ~-20%                       |
| Mar-16 | ~15%                        |
| Mar-19 | ~10%                        |
| Mar-22 | ~35%                        |
| Mar-25 | ~15%                        |
</details>

Source: WSTS, MS

Exhibit 2: Auto and industrial accounted for 70% of end demand in discrete semiconductors (2025)  
![](images/715dddb17386ec9f4d6448fd7e6c8fa3cc40eff7bd052fd954c8074bc137242c.jpg)

<details>
<summary>pie chart</summary>

| Category | Percentage (%) |
| :--- | :--- |
| Auto | 41 |
| Industrial | 31 |
| Consumer | 12 |
| Communication | 8 |
| Data processing | 8 |
</details>

Source: Gartner, MS

Exhibit 3: China EV wholesale growth is turning incrementally positive  
![](images/1cfae95d23a302502620689c36e61863dd08ad7502cc1d27a75b28980d67ddad.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Month    | China EV (whole sales, k unit) | China EV wholesale YoY (3MMA, RHS) |
| -------- | ------------------------------ | ---------------------------------- |
| Jan-23   | 400                            | 10%                                |
| Feb-23   | 500                            | 8%                                 |
| Mar-23   | 600                            | 15%                                |
| Apr-23   | 700                            | 20%                                |
| May-23   | 800                            | 25%                                |
| Jun-23   | 900                            | 30%                                |
| Jul-23   | 1000                           | 35%                                |
| Aug-23   | 1100                           | 40%                                |
| Sep-23   | 1200                           | 45%                                |
| Oct-23   | 1300                           | 50%                                |
| Nov-23   | 1400                           | 55%                                |
| Dec-23   | 1500                           | 60%                                |
| Jan-24   | 1600                           | 65%                                |
| Feb-24   | 1700                           | 70%                                |
| Mar-24   | 1800                           | 75%                                |
| Apr-24   | 1900                           | 80%                                |
| May-24   | 2000                           | 85%                                |
| Jun-24   | 2100                           | 90%                                |
| Jul-24   | 2200                           | 95%                                |
| Aug-24   | 2300                           | 100%                               |
| Sep-24   | 2400                           | 105%                               |
| Oct-24   | 2500                           | 110%                               |
| Nov-24   | 2600                           | 115%                               |
| Dec-24   | 2700                           | 120%                               |
| Jan-25   | 2800                           | 125%                               |
| Feb-25   | 2900                           | 130%                               |
| Mar-25   | 3000                           | 135%                               |
| Apr-25   | 3100                           | 140%                               |
| May-25   | 3200                           | 145%                               |
| Jun-25   | 3300                           | 150%                               |
| Jul-25   | 3400                           | 155%                               |
| Aug-25   | 3500                           | 160%                               |
| Sep-25   | 3600                           | 165%                               |
| Oct-25   | 3700                           | 170%                               |
| Nov-25   | 3800                           | 175%                               |
| Dec-25   | 3900                           | 180%                               |
| Jan-26   | 4000                           | 185%                               |
| Feb-26   | 4100                           | 190%                               |
| Mar-26   | 4200                           | 195%                               |
| Apr-26   | 4300                           | 200%                               |
| May-26   | 4400                           | 205%                               |
| Jun-26   | 4500                           | 210%                               |
| Jul-26   | 4600                           | 215%                               |
| Aug-26   | 4700                           | 220%                               |
| Sep-26   | 4800                           | 225%                               |
| Oct-26   | 4900                           | 230%                               |
| Nov-26   | 5000                           | 235%                               |
| Dec-26   | 5100                           | 240%                               |
| Jan-27   | 5200                           | 245%                               |
| Feb-27   | 5300                           | 250%                               |
| Mar-27   | 5400                           | 255%                               |
| Apr-27   | 5500                           | 260%                               |
| May-27   | 5600                           | 265%                               |
| Jun-27   | 5700                           | 270%                               |
| Jul-27   | 5800                           | 275%                               |
| Aug-27   | 5900                           | 280%                               |
| Sep-27   | 6000                           | 285%                               |
| Oct-27   | 6100                           | 290%                               |
| Nov-27   | 6200                           | 295%                               |
| Dec-27   | 6300                           | 300%                               |
| Jan-28   | 6400                           | 305%                               |
| Feb-28   | 6500                           | 310%                               |
| Mar-28   | 6600                           | 315%                               |
| Apr-28   | 6700                           | 320%                               |
| May-28   | 6800                           | 325%                               |
| Jun-28   | 6900                           | 330%                               |
| Jul-28   | 7000                           | 335%                               |
| Aug-28   | 7100                           | 340%                               |
| Sep-28   | 7200                           | 345%                               |
| Oct-28   | 7300                           | 350%                               |
| Nov-28   | 7400                           | 355%                               |
| Dec-28   | 7500                           | 360%                               |
| Jan-29   | 7600                           | 365%                               |
| Feb-29   | 7700                           | 370%                   

[中间内容因长度限制已省略]

3501.SS)</td><td>E (11/17/2025)</td><td>Rmb90.12</td></tr><tr><td>Phison Electronics Corp (8299.TWO)</td><td>E (02/25/2026)</td><td>NT$2,330.00</td></tr><tr><td>SG Micro Corp. (300661.SZ)</td><td>E (11/03/2025)</td><td>Rmb131.55</td></tr><tr><td>Silergy Corp. (6415.TW)</td><td>U (05/19/2026)</td><td>NT$572.00</td></tr><tr><td>SMIC (0981.HK)</td><td>O (10/21/2025)</td><td>HK$75.75</td></tr><tr><td>TSMC (2330.TW)</td><td>O (02/07/2022)</td><td>NT$2,385.00</td></tr><tr><td>UMC (2303.TW)</td><td>O (05/19/2026)</td><td>NT$140.00</td></tr><tr><td>Vanguard International Semiconductor (5347.TWO)</td><td>E (01/14/2026)</td><td>NT$166.50</td></tr><tr><td>WIN Semiconductors Corp (3105.TWO)</td><td>U (07/14/2025)</td><td>NT$519.00</td></tr></table>

<table><tr><td colspan="3">Daisy Dai, CFA</td></tr><tr><td>ASMPT Ltd (0522.HK)</td><td>O (07/24/2025)</td><td>HK$210.00</td></tr><tr><td>China Resources Microelectronics Limited (688396.SS)</td><td>U (03/02/2026)</td><td>Rmb73.78</td></tr><tr><td>Elan Microelectronics Corp (2458.TW)</td><td>O (10/03/2025)</td><td>NT$156.50</td></tr><tr><td>Empyrean Technology Co Ltd (301269.SZ)</td><td>E (01/17/2025)</td><td>Rmb105.01</td></tr><tr><td>Hangzhou Silan Microelectronics Co. Ltd. (600460.SS)</td><td>U (08/25/2025)</td><td>Rmb40.83</td></tr><tr><td>Innoscience (2577.HK)</td><td>E (10/13/2025)</td><td>HK$63.05</td></tr><tr><td>JCET Group Co Ltd (600584.SS)</td><td>E (01/16/2026)</td><td>Rmb81.76</td></tr><tr><td>Shanghai Fudan Microelectronics (1385.HK)</td><td>O (03/07/2025)</td><td>HK$29.48</td></tr><tr><td>SICC Co Ltd (688234.SS)</td><td>O (03/20/2026)</td><td>Rmb149.66</td></tr><tr><td>StarPower Semiconductor Ltd (603290.SS)</td><td>E (05/14/2026)</td><td>Rmb130.98</td></tr><tr><td>Unigroup Guoxin Microelectronics Co Ltd (002049.SZ)</td><td>U (01/10/2023)</td><td>Rmb80.00</td></tr><tr><td>Universal Scientific Ind. (Shanghai) (601231.SS)</td><td>O (11/05/2025)</td><td>Rmb37.08</td></tr><tr><td>Yangjie Technology (300373.SZ)</td><td>O (06/10/2022)</td><td>Rmb114.10</td></tr></table>

<table><tr><td colspan="3">Daniel Yen, CFA</td></tr><tr><td>AP Memory Technology Corp (6531.TW)</td><td>O (07/11/2025)</td><td>NT$933.00</td></tr><tr><td>ASMedia Technology Inc (5269.TW)</td><td>U (10/03/2025)</td><td>NT$1,425.00</td></tr><tr><td>Aspeed Technology (5274.TWO)</td><td>O (06/09/2025)</td><td>NT$18,485.00</td></tr><tr><td>Egis Technology Inc (6462.TWO)</td><td>E (01/28/2026)</td><td>NT$112.50</td></tr><tr><td>Espressif Systems (688018.SS)</td><td>O (05/15/2023)</td><td>Rmb122.40</td></tr><tr><td>GigaDevice Semiconductor Beijing Inc (603986.SS)</td><td>O (05/15/2025)</td><td>Rmb586.04</td></tr><tr><td>Macronix International Co Ltd (2337.TW)</td><td>O (09/18/2025)</td><td>NT$161.50</td></tr><tr><td>Montage Technology Co Ltd (6809.HK)</td><td>O (03/18/2026)</td><td>HK$420.60</td></tr><tr><td>Montage Technology Co Ltd (688008.SS)</td><td>O (03/18/2026)</td><td>Rmb262.50</td></tr><tr><td>Novatek (3034.TW)</td><td>U (02/04/2026)</td><td>NT$515.00</td></tr><tr><td>Nuvoton Technology Corporation (4919.TW)</td><td>U (11/10/2025)</td><td>NT$187.50</td></tr><tr><td>Parade Technologies Ltd (4966.TWO)</td><td>O (05/27/2026)</td><td>NT$675.00</td></tr><tr><td>Powerchip Semiconductor Manufacturing Co (6770.TW)</td><td>O (10/27/2025)</td><td>NT$70.20</td></tr><tr><td>Realtek Semiconductor (2379.TW)</td><td>E (01/30/2026)</td><td>NT$745.00</td></tr><tr><td>Shenzhen Goodix Technology Co Ltd (603160.SS)</td><td>U (07/14/2025)</td><td>Rmb59.74</td></tr><tr><td>Winbond Electronics Corp (2344.TW)</td><td>O (05/28/2026)</td><td>NT$199.00</td></tr><tr><td>WPG Holdings (3702.TW)</td><td>O (03/16/2026)</td><td>NT$107.00</td></tr><tr><td>WT Microelectronics Co. Ltd. (3036.TW)</td><td>O (01/27/2026)</td><td>NT$224.00</td></tr><tr><td colspan="3">Duan Liu</td></tr><tr><td>Dosilicon Co Ltd (688110.SS)</td><td>U (09/06/2024)</td><td>Rmb152.91</td></tr><tr><td>Shenzhen Longsys Electronics Co Ltd (301308.SZ)</td><td>E (02/25/2026)</td><td>Rmb571.68</td></tr><tr><td colspan="3">Tiffany Yeh</td></tr><tr><td>AllRing Tech Co. (6187.TWO)</td><td>O (09/23/2025)</td><td>NT$1,155.00</td></tr><tr><td>FOCI Fiber Optic Communications Inc (3363.TWO)</td><td>O (01/15/2025)</td><td>NT$685.00</td></tr><tr><td>Himax Technologies Inc (HIMX.O)</td><td>E (02/04/2026)</td><td>US$16.95</td></tr><tr><td>Hon Precision (7769.TW)</td><td>O (04/17/2026)</td><td>NT$7,330.00</td></tr><tr><td>MPI Corporation (6223.TWO)</td><td>O (04/17/2026)</td><td>NT$6,420.00</td></tr><tr><td>Silicon Motion (SIMO.O)</td><td>O (05/06/2024)</td><td>US$307.12</td></tr><tr><td>WinWay Technology Co Ltd (6515.TW)</td><td>O (04/17/2026)</td><td>NT$9,450.00</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
