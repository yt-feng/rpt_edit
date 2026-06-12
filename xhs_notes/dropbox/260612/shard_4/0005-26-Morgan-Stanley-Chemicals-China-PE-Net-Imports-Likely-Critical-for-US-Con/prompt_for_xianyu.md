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
## Chemicals | North America

# China PE Net Imports Likely Critical for US Contract Prices

We view the shape of China's net imports of polyethylene as a critical KPI to the trajectory of US PE contract prices. The starting point for this view is the reduction of China's net imports during April (as the Straight of Hormuz remained closed), which added 9% to ex-China global supply, partially offsetting the 15% reduction to global supply caused by the closure of the SOH. In particular, China reduced its net import position from \~1.1m MT per month pre-conflict to \~180K MT in April. It did this by: i) reducing imports by \~500K mt (approximately \~40% less from the US in particular); and ii) increasing exports by \~400K MT (most of which we believe went to Southeast Asia to offset the lost exports from the Middle East). The overall \~900kMT reduction of China's net import position drove China's net import reliance to \~5% in April vs. \~31% in 2025 (see Exhibit 1).

Exhibit 1: China Net Import Reliance for PE  
![](images/fd9a0c3ba52a20bcd53959a077171455f30255be78a16db8232f16605c4e0eb2.jpg)

<details>
<summary>bar chart</summary>

China Net Import Reliance for PE
| Year | Net Import Reliance (%) |
| :--- | :--- |
| 2000 | 56 |
| 2001 | 59 |
| 2002 | 55 |
| 2003 | 55 |
| 2004 | 59 |
| 2005 | 53 |
| 2006 | 46 |
| 2007 | 42 |
| 2008 | 41 |
| 2009 | 51 |
| 2010 | 43 |
| 2011 | 43 |
| 2012 | 43 |
| 2013 | 43 |
| 2014 | 42 |
| 2015 | 43 |
| 2016 | 41 |
| 2017 | 43 |
| 2018 | 46 |
| 2019 | 48 |
| 2020 | 49 |
| 2021 | 37 |
| 2022 | 34 |
| 2023 | 33 |
| 2024 | 33 |
| April 2026 | 31 |
| May 2026 | 5 |
</details>

Source: Chemical Market Analytics, MS

Naturally, this unanticipated behavior by China made the export market less tight than feared in April (with a carry-over impact into May likely, in our view) but there remains debate about how long such behavior can persist. In particular, we believe that China likely held far more excess inventory (pre-conflict) than understood. Discussions with consultants lead us to believe that \~1mm MT of excess inventory was built by Chinese traders in the 6-12 months prior to the Iran conflict, increasing the country's excess inventory position to \~2.3-3.5mm MT, which is equivalent to \~30 days of domestic demand. We expect to learn China's net imports for May in late June/early July.

## (CONTINUED INSIDE)

MS & CO. LLC

## Vincent Andrews

Equity Analyst

Vincent.Andrews@morganstanley.com

+1 212 761-3293

## Turner W Hinrichs

Research Associate

Turner.Hinrichs@morganstanley.com

+1 212 761-1269

2026 EXTEL

ALL-AMERICA

RESEARCH POLL

May 26 – June 12, 2026

VIEW OUR

ANALYSTS >

## CHEMICALS

North America

Industry View

In-Line

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

# China PE Net Imports Likely Critical KPI for US Contract Prices

Small Favor – Vote for us in the Extel (fka Institutional Investor) poll! If you find this report helpful, please consider voting for Vincent Andrews as a five-star Chemicals analyst in this year's Extel poll. Please also vote for team members Steven Haynes, Turner Hinrichs and Justin Pellegrino in Chemicals. If you need a ballot, please let us know. We really appreciate your support.

Our scenario analysis suggests that the excess inventory may thin out by June/July. Should China then revert to its pre-conflict net import purchasing, we believe that this could lead to incremental demand for US exports of \~250K mt per month (12% of US annual supply). Such an outcome would likely help move US contract prices higher, all else equal, while the lack thereof would likely accelerate US contract price reversion to a lower mean. Notably, Chinese polyolefin inventory data from both Sinopec and CNPC demonstrates our expected draw down trend, with inventory now \~19% below recent highs and back to levels comparable with 2024/2025. Note that the inventory buildup through April is also atypical seasonally (with April 2024/2025 highs remaining -13%/-19% below February 2024/2025 levels), though 2026 YTD polyolefin inventories have fallen to comparable levels to 2024/2025 (-1% below the average) following the 19% (170kMT) draw down since April's peak.

Exhibit 2: MSe 2026 US PE contract expectations, alongside (i) a scenario where incremental US exports drive higher prices and (ii) another where the reversion to a lower mean is accelerated

![](images/76e9a45a4d3bd9056cc1c074f62671daf9aba3ad6b662c5042d71ab994c256e8.jpg)

<details>
<summary>line chart</summary>

| Month     | MSe PE Forecasts | Incremental Exports | Faster Mean-Reversion |
| --------- | ---------------- | ------------------- | --------------------- |
| January   | 53               | -                   | -                     |
| February  | 53               | -                   | -                     |
| March     | 63               | -                   | -                     |
| April     | 93               | -                   | -                     |
| May       | 93               | 93                  | 93                    |
| June      | 93               | 98                  | 92                    |
| July      | 88               | 92                  | 86                    |
| August    | 83               | 88                  | 78                    |
| September | 73               | 83                  | 68                    |
| October   | 73               | 83                  | 68                    |
| November  | 70               | 80                  | 65                    |
| December  | 70               | 80                  | 65                    |
</details>

Source: MS

Exhibit 3: Sinopec and Petrochina Polyolefin Inventories (PE & PP)  
![](images/3e85da1da7258f10a798521426c0739dbd2ace68ce7288e1f163689349199f05.jpg)

<details>
<summary>line chart</summary>

| Year | Feb Restock | April High | ~End May Low |
|------|-------------|------------|--------------|
| 2024 | 955         | 835        | 765          |
| 2025 | 930         | 755        | 730          |
| 2026 | 870         | 910        | 740          |
</details>

Note: the data represents inventories within China, inclusive of joint ventures.  
Source: ICIS, Company data, MS

## As it stands right now, the US market is largely playing out as we expected (see:

Chemicals: Polyethylene S&D Update (21 Apr 2026)) with spot prices in a downward trend following substantial March and April contract increases (+10cpp/+30cpp) and a flat May settlement. Looking ahead to June's contract negotiations, Dow and LyondellBasell have nominated 20cpp and 10cpp increases, respectively. At present, we model another flat settlement. Importantly, market commentary indicates that exports have lagged expectations, driving an expected producer inventory increase to \~46 days in May from 42.5 days in April and 44.0 days in February.

Exhibit 4: North American Polyethylene Prices  
![](images/190025ab497799f697c7ddb8056089969f9a7b73b718f0945bdecdcf92af1308.jpg)

<details>
<summary>line chart</summary>

| Date       | N. Am. Spot Export Price | N. Am. PE Spot Average | US PE Contract Price (NTP) |
| ---------- | ------------------------ | ----------------------- | ------------------------- |
| 1/5/2023   | ~45                      | ~45                     | ~57                       |
| 3/5/2023   | ~48                      | ~47                     | ~58                       |
| 5/5/2023   | ~47                      | ~46                     | ~59                       |
| 7/5/2023   | ~40                      | ~41                     | ~55                       |
| 9/5/2023   | ~42                      | ~43                     | ~57                       |
| 11/5/2023  | ~44                      | ~44                     | ~58                       |
| 1/5/2024   | ~40                      | ~41                     | ~56                       |
| 3/5/2024   | ~45                      | ~46                     | ~59                       |
| 5/5/2024   | ~47                      | ~47                     | ~60                       |
| 7/5/2024   | ~48                      | ~48                     | ~61                       |
| 9/5/2024   | ~49                      | ~49                     | ~61                       |
| 11/5/2024  | ~47                      | ~47                     | ~60                       |
| 1/5/2025   | ~45                      | ~45                     | ~59                       |
| 3/5/2025   | ~47                      | ~46                     | ~58                       |
| 5/5/2025   | ~45                      | ~45                     | ~57                       |
| 7/5/2025   | ~43                      | ~43                     | ~56                       |
| 9/5/2025   | ~41                      | ~41                     | ~55                       |
| 11/5/2025  | ~38                      | ~38                     | ~53                       |
| 1/5/2026   | ~36                      | ~36                     | ~51                       |
| 3/5/2026   | ~38                      | ~38                     | ~53                       |
| 5/5/2026   | ~80                      | ~80                     | ~93                       |
| 7/5/2026   | ~70                      | ~70                     | ~93                       |
| 9/5/2026   | ~60                      | ~60                     | ~93                       |
| 11/5/2026  | ~50                      | ~50                     | ~93                       |
| 1/5/2027   | ~40                      | ~40                     | ~93                       |
| 3/5/2027   | ~30                      | ~30                     | ~93                       |
| 5/5/2027   | ~20                      | ~20                     | ~93                       |
| 7/5/2027   | ~10                      | ~10                     | ~93                       |
| 9/5/2027   | ~5                       | ~5                      | ~93                       |
| 11/5/2027  | ~3                       | ~3                      | ~93                       |
| 1/5/2028   | ~1                       | ~1                      | ~93                       |
| 3/5/2028   | ~0.5                     | ~0.5                    | ~93                       |
| 5/5/2028   | ~0.3                     | ~0.3                    | ~93                       |
| 7/5/2028   | ~0.2                     | ~0.2                    | ~93                       |
| 9/5/2028   | ~0.1                     | ~0.1                    | ~93                       |
| 11/5/2028  | ~0.05                    | ~0.05                   | ~93                       |
| 1/5/2029   | ~0.03                    | ~0.03                   | ~93                       |
| 3/5/2029   | ~0.01                    | ~0.01                   | ~93                       |
| 5/5/2029   | ~0.005                   | ~0.005                  | ~93                       |
| 7/5/2029   | ~0.003                   | ~0.003                  | ~93                       |
| 9/5/2029   | ~0.001                   | ~0.001                  | ~93                       |
| 11/5/2029  | ~-0.001                  | ~-0.001                 | ~93                       |
| 1/5/2030   | -0.003                   | -0.003                  | ~93                       |
| 3/5/2030   | -0.005                   | -0.005                  | ~93                       |
| 5/5/2030   | -0.007                   | -0.007                  | ~93                       |
| 7/5/2030   | -0.01                    | -0.01                   | ~93                       |
| 9/5/2030   | -0.013                   | -0.013                  | ~93                       |
| 11/5/2030  | -0.016                   | -0.016                  | ~93                       |
| 1/5/2031   | -0.018                   | -0.018                  | ~93                       |
| 3/5/2031   | -0.02                    | -0.02                    | ~93                       |
| 5/5/2031   | -0.023                   | -0.023                  | ~93                       |
| 7/5/2031   | -0.026                   | -0.026                  | ~93                       |
| 9/5/2031   | -0.028                   | -0.028                  | ~93                       |
| 11/5/2031  | -0.03                    | -0.03                    | ~93                       |
| 1/5/2032   | -0.033                   | -0.033                  | ~93                       |
| 3/5/2032   | -0.036                   | -0.036                  | ~93                       |
| 5/5/2032   | -0.038                   | -0.038                  | ~93                       |
| 7/5/2032   | -0.04                    | -0.04                    | ~93                       |
| 9/5/2032   | -0.043                   | -0.043                  | ~93                       |
| 11/5/2032  | -0.046                   | -0.046                  | ~93                       |
| 1/5/2033   | -0.048                   | -0.048                  | ~93                       |
| 3/5/2033   | -0.05                    | -0.05                    | ~93                       |
| 5/5/2033   | -0.053                   | -0.053                  | ~93                       |
| 7/5/2033   | -0.056                   | -0.056                  | ~93                       |
| 9/5/2033   | -0.058                   | -0.058                  | ~93                       |
| 11/5/2033  | -0.06                    | -0.06                    | ~93                       |
| 1/5/2034   | -0.063                   | -0.063                  | ~93                       |
| 3/5/2034   | -0.066                   | -0.066                  | ~93                       |
| 5/5/2034   | -0.068                   | -0.068                  | ~93                       |
| 7/5/2O        | -         |                         nan          |                           |
|            (additional values) for the last few entries are not explicitly labeled in the code; they are estimated based on the original data and are not explicitly provided in the code format.
</details>

Source: Chemical Market Analytics, Platts, MS

Our estimate for 250K mt of potential incremental US exports is derived by dividing Chinese imports ratably by import share (excluding historical Middle Eastern volumes, which are assumed to still be constrained). This uplift would represent \~21% upside to US export volumes, likely maximizing US export volumes (consultants have estimated a \~17% import increase over 2025 levels is the maximum increase given current infrastructure limitations). Considering effective operating rates are already near-maximum levels

(\~98.8% effective operating rates estimated for May), we would expect US inventories to draw down up to \~8 days through August, potentially driving the monthly contract settlement higher.

Exhibit 5: US PE Export Destinations and Chinese PE Import Origins

<table><tr><td colspan="6">United States exports</td><td colspan="6">China (mainland) imports</td></tr><tr><td>Export Region</td><td>Export Country/Territory</td><td>Import Region</td><td>Import Country/Territory</td><td>kMT</td><td>% Total</td><td>Export Region</td><td>Export Country/Territory</td><td>Import Region</td><td>Import Country/Territory</td><td>kMT</td><td>% Total</td></tr><tr><td>North America</td><td>United States</td><td>North East Asia</td><td>China (Mainland)</td><td>2,566.1</td><t

[中间内容因长度限制已省略]

mers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Chemicals

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/10/2026)</td></tr><tr><td colspan="3">Lisa H De Neve</td></tr><tr><td>ICL Group Ltd (ICL.N)</td><td>E (01/05/2024)</td><td>$5.50</td></tr><tr><td>International Flavors &amp; Fragrances (IFF.N)</td><td>O (11/11/2024)</td><td>$74.23</td></tr><tr><td colspan="3">Steven K Haynes, CFA</td></tr><tr><td>Ashland Inc. (ASH.N)</td><td>E (09/08/2025)</td><td>$64.87</td></tr><tr><td colspan="3">Vincent Andrews</td></tr><tr><td>Air Products and Chemicals Inc. (APD.N)</td><td>E (05/29/2025)</td><td>$276.51</td></tr><tr><td>Albemarle Corporation (ALB.N)</td><td>E (12/15/2025)</td><td>$147.22</td></tr><tr><td>Avient Corporation (AVNT.N)</td><td>E (12/14/2020)</td><td>$34.97</td></tr><tr><td>Axalta Coating Systems Ltd (AXTA.N)</td><td>++</td><td>$32.10</td></tr><tr><td>Celanese Corp. (CE.N)</td><td>E (01/20/2026)</td><td>$50.38</td></tr><tr><td>CF Industries (CF.N)</td><td>E (05/25/2016)</td><td>$109.26</td></tr><tr><td>Chemours Co (CC.N)</td><td>E (01/30/2018)</td><td>$20.31</td></tr><tr><td>Corteva Inc. (CTVA.N)</td><td>O (12/14/2020)</td><td>$74.46</td></tr><tr><td>Dow Inc. (DOW.N)</td><td>E (12/01/2019)</td><td>$34.24</td></tr><tr><td>DuPont De Nemours Inc. (DD.N)</td><td>E (05/26/2021)</td><td>$45.06</td></tr><tr><td>Eastman Chemical Co (EMN.N)</td><td>O (01/17/2019)</td><td>$71.34</td></tr><tr><td>Ecolab Inc. (ECL.N)</td><td>O (01/28/2025)</td><td>$256.99</td></tr><tr><td>FMC Corporation (FMC.N)</td><td>E (10/24/2023)</td><td>$10.80</td></tr><tr><td>Huntsman Corp (HUN.N)</td><td>E (12/11/2023)</td><td>$14.23</td></tr><tr><td>Intrepid Potash (IPI.N)</td><td>U (10/03/2013)</td><td>$33.80</td></tr><tr><td>Linde PLC (LIN.O)</td><td>O (02/09/2020)</td><td>$509.16</td></tr><tr><td>LyondellBasell Industries N.V. (LYB.N)</td><td>O (12/01/2019)</td><td>$65.15</td></tr><tr><td>Mosaic Company (MOS.N)</td><td>E (03/16/2016)</td><td>$19.82</td></tr><tr><td>Nutrien Ltd (NTR.N)</td><td>O (01/14/2026)</td><td>$65.03</td></tr><tr><td>Olin Corp. (OLN.N)</td><td>U (01/10/2023)</td><td>$23.92</td></tr><tr><td>PPG Industries Inc. (PPG.N)</td><td>E (11/01/2019)</td><td>$112.97</td></tr><tr><td>RPM International Inc. (RPM.N)</td><td>E (12/14/2020)</td><td>$104.28</td></tr><tr><td>Sherwin-Williams Co. (SHW.N)</td><td>O (03/19/2014)</td><td>$303.91</td></tr><tr><td>Tronox Holdings Plc-Class A (TROX.N)</td><td>E (01/30/2018)</td><td>$7.15</td></tr><tr><td>Westlake Corp (WLK.N)</td><td>E (01/09/2018)</td><td>$87.12</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
