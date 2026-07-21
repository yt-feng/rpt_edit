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
# China Spirits Tracker: Feitian wholesale price trended up; channel feedback post price hike

Moutai announced its 5th Market-oriented reform on Jul 17, with 7.9%/6.5% or Rmb100/bottle each hike on ex-factory price/RSP of 500ml Feitian Moutai products. Meanwhile, our channel check also indicated different magnitudes of price hikes of 500ml Feitian in self-operated specialty stores (Rmb1,719/bottle vs prior Rmb1,639/bottle)/KA & E-commerce platforms (Rmb1,529/bottle vs prior Rmb1,399/bottle) and 1L Feitian on i-Moutai (Rmb3,269/bottle vs prior Rmb3,119/bottle). 53% Feitian wholesale price rebounded by Rmb50-55/bottle post Moutai's announcement to Rmb1,705-Rmb1,680/bottle on Jul 19 vs those of Jul 17. Distributors broadly viewed this round of price hike as anticipated (though a bit earlier and higher in magnitude) which also indicated Moutai's intention on maintaining a more sustainable/steady channel profitability of Feitian for Wholesalers going forward. This also echoed with our expectation of more frequent and commercialized pricing actions under the market-orientation reform going forward, and emphasized Moutai's key strategy of DTC transition and strong pricing power over retail-end.

Moutai underlying sell-through remained healthy: channel checks suggest Moutai 2Q sell-through was broadly stable with more resilient demand for Feitian, despite a still soft macro backdrop. Distributor inventory remained lean at c. 2 weeks for Feitian while cumulative shipment is running ahead of last year level (c.65%\~70% YTD vs 55% in 2025 same period) primarily due to front-loaded 1Q allocations. i-Moutai volume control for non-standard SKUs are still stringent in order to protect a healthy pricing level. Non-standard Moutai shipment in 2Q26 is still meaningfully below 2Q25 level (some regional channel check shows c. 30% behind) while we believe that a healthy S/D and pricing level for Non-standard SKUs is critical for its long-term growth and success. We also expect Moutai to conduct more frequent and market driven pricing actions once Non-standard Moutai products start to see healthy demand improvement (similar to Feitian).

Feitian Moutai wholesale price trended up, while Common Wuliangye and Guojiao 1573 stayed soft. In the past 2 weeks, original case Feitian Moutai's wholesale price/bottle increased by Rmb55 from Rmb1,650 to Rmb1,705, and unpacked Feitian Moutai's wholesale price increased by Rmb60 from Rmb1,620 to Rmb1,680. For non-standard Moutai SKUs, the wholesale price of Zodiac/Jingpin/1-litre Feitian Moutai increased by Rmb5/15/100 per bottle, while Moutai 15 years decreased by Rmb20 per bottle. Common Wuliangye's wholesale price/bottle stayed flattish at Rmb840/ decreased by Rmb20 to Rmb730 per

Leaf Liu
+852-3966-4169 | leaf.liu@gs.com
GS (Asia) L.L.C.

Christina Liu
+852-2978-6983 | christina.liu@gs.com
GS (Asia) L.L.C.

Valerie Zhou
+852-2978-0820 | valerie.zhou@gs.com
GS (Asia) L.L.C.

“Daily Spirits Prices”/Bairong Wholesale Market, respectively. Guojiao 1573’s wholesale price/bottle stayed flattish at Rmb825.

The authors would like to thank Lily Qi for her contribution to this report.

![](images/cf2611effd288dd7777b460b524777f557d6ed4075f9a9772348d2ba9c0a8efe.jpg)  
Source: GS Global Investment Research

i-Moutai APP tracker: Our Quest Mobile database indicated monthly active users (MAU) on the i-Moutai app reached 7.97mn/10.2mn in Jun/May, up by 4%/-12% yoy, and avg 9.4mn MAU in 2Q26 vs. avg 18mn in 1Q26 while is still above the level before Feitian Moutai's launch (MAU at 5\~7mn in 4Q25). DAU/MAU penetration ratio was at 10%/11% in Jun/May.

Exhibit 1: I-Moutai active users surged from Jan 1st 2026 when Feitian was officially launched on i-Moutai  
![](images/90598534785d5b2ca793572a9c09104f47773cd8655fd3ef2a7d16c65c0c7828.jpg)  
Source: Quest Mobile

## Key news this week:

■ Neican raised ex-factory price of 52% 500ml Neican liquor (Jul 15): Neican announced an ex-factory price hike on its 52% 500ml Neican product (incl. 2021 edition and Jiachen edition) by Rmb30/bottle with unchanged annual volume rebate of Rmb20/bottle, effective on Jul 15. The company also suspended the shipment of 52% Neican products from Jul 15 to Aug 15.

Wuliangye's FIFA World Cup campaign spurs off-season sales (Jul 8): Wuliangye's FIFA World Cup with themed marketing drove robust sales. The co-branded portfolio centered on the 8th-generation Wuliangye World Cup Edition generated cumulative sales of Rmb 1.6bn and attracted 4mn new users, with consumers under 35 accounting for 40% of the total.

\- Swellfun announced crackdowns on parallel goods trafficking (Jul 17): Swellfun will launch cross-regional crackdowns on unauthorized parallel goods trafficking on all markets to its distributors, starting from the week of Jul 20.

## Wholesale price summary of high-end liquors

## From Jul 5 to Jul 19, 2026:

Original case Feitian Moutai's wholesale price/bottle increased by Rmb55 from Rmb1,650 to Rmb1,705, and unpacked Feitian Moutai's wholesale price increased by Rmb60 from Rmb1,620 to Rmb1,680.

Common Wuliangye's wholesale price/bottle stayed flattish at Rmb840/decreased by Rmb20 to Rmb730 per "Daily Spirits Prices"/Bairong Wholesale Market, respectively.

Guojiao 1573's wholesale price/bottle stayed flattish at Rmb825.

## From Jan 1 to Jul 19, 2026:

Original case Feitian Moutai's wholesale price/bottle increased by Rmb200 from Rmb1,505 to Rmb1,705. Unpacked Feitian Moutai's wholesale price/bottle increased by Rmb190 from Rmb1,490 to Rmb1,680.

Common Wuliangye's wholesale price/bottle decreased by Rmb20 to Rmb830 per "Daily Spirits Prices," and decreased by Rmb80 to Rmb730 per Bairong Wholesale Market.

Guojiao 1573's wholesale price/bottle decreased by Rmb15 to Rmb825.

Exhibit 2: $53\%$ Feitian Moutai product prices  
![](images/fa40301498358e0e8950c2be87b42fe5dc9c2446d2dbdedc1b9798106703e1ce.jpg)  
Most recent data points as of Jul 19, 2026.  
Source: Daily Spirits Prices, Data compiled by GS Global Investment Research

Exhibit 3: 52% Common Wuliangye product prices  
![](images/63099a4b1506f0a95f47bdd7459275c7a4f14f94b271b1d627fc421f7c6d1bcb.jpg)  
Most recent data points as of Jul 19, 2026. Source 1 = Spirits Price References; Source 2 = Daily Spirits Prices; Source 3 = Bairong Wholesale Market  
Source: Spirits Price References, Daily Spirits Prices, Bairong Wholesale Market, Data compiled by GS Global Investment Research

Exhibit 4: Guojiao 1573 product prices  
![](images/ae8113d7993b8e3bd89beb78325a34a74e5493b5d2a27c69b617694bca8d4235.jpg)  
Most recent data points as of Jul 19, 2026.  
Source: Daily Spirits Prices, Data compiled by GS Global Investment Research

Moutai non-standard SKUs: In the past 2 weeks, the wholesale price of Zodiac/Jingpin/1-litre Feitian Moutai increased by Rmb5/15/100 per bottle, while Moutai 15 years decreased by Rmb20 per bottle.

Source: Data compiled by GS Global Investment Research, Daily Spirits Prices

Exhibit 5: Wholesale prices of Moutai's 4 non-standard SKUs  
![](images/e835245f9e9358b73a1b4e1049e8a5e0b74370650a12f9917df3161fe14e5dc6.jpg)  
Rmb/bottle Jingpin Moutai (53%, 500ml)

![](images/1e5fe361c1ffaed7d74fd2f9f69ee648a3bec6e23382a5ad65a6c8c6f1ed22d5.jpg)  
Rmb/bottle Moutai 15 years (53%, 500ml)

![](images/d4c37ffbb45d2a2d12ee5027749a68c47bf5af6c74cd00c77a15541fe68f8be5.jpg)  
Latest data as of Jul 19, 2026.

![](images/d86d23d07ec3029f68b2fab4fc9e85e340c8b35d56dba8e707b1538ac04b7df5.jpg)

## Exhibit 6: 2025-2026 channel policy and product launch summary of key spirits companies - Part I

<table><tr><td>Year</td><td>Month</td><td>Kweichow Moutai (600519.SS)</td><td>Wuliangye Yibin (000858.SZ)</td><td>Luzhou Laojiao (000568.SZ)</td><td>Jiangsu Yanghe (002304.SZ)</td><td>Shanxi Fen Wine (600809.SS)</td><td>Jian Nan Chun(Private, Not Covered)</td></tr><tr><td>2026</td><td>Jul</td><td>Week3: Moutai raised the ex-factory price of Feitian Moutai (53% vol, 500ml, 2026 edition) from Rmb1,269/bottle to Rmb1,369/bottle(mainly covering wholesale channels), and RSP of Feitian Moutai on i-Moutai platform from Rmb1,539/bottle to Rmb1,639/bottle(mainly covering direct sales channels).</td><td colspan="5"></td></tr><tr><td>2026</td><td>May</td><td>Week3: Moutai raised the RSP of select non-standard SKUs on i-Moutai APP effective May 16. The scope of price hikes include 53% vol 500ml Moutai 15 years (Rmb4,199/bottle to Rmb4,279/bottle), Jingpin Moutai (Rmb2,299/bottle to Rmb2,359/bottle), Zodiac Moutai (Horse precious) (Rmb2,499/bottle to Rmb2,699/bottle) and 1L Moutai (Rmb2,989/bottle to Rmb3,119/bottle).</td><td colspan="5"></td></tr><tr><td>2026</td><td>Mar</td><td>Week 4: raised the ex-factory price of Feitian Moutai (53% vol, 500ml, 2026 edition) from Rmb1,169/bottle to c.Rmb1,269 per bottle(mainly cover wholesale channels), and the RSP of Feitian Moutai from Rmb1,499 to Rmb1,539 (mainly cover direct sales channels, esp. i-Moutai platform), effective immediately from Mar 31, 2026.</td><td colspan="5"></td></tr><tr><td>2026</td><td>Mar</td><td>Week3: introduced a consignment sales policy for non-standard Moutai products: participating distributors must apply and pay a deposit and will receive a c.5% rebate on these products sales</td><td colspan="5"></td></tr><tr><td>2026</td><td>Jan</td><td>Week 3: plans to employ a more market-driven pricing framework to optimize channel investments and safeguard channel profitability, presented new RSP for Feitian Moutai vintage and other non-standard SKUs and lowered ex-factory price for some non-standard/series prproducts</td><td colspan="5"></td></tr><tr><td>2025</td><td>Dec</td><td>Week 5: officially announced the launch of Feitian Moutai across 53% vol 500ml (years 2019-2026), 100ml/1,000ml Feitian, and multiple series on i-Moutai, including Jingpin, Zodiac, Vintage, Cultural, and lower-alcohol variants (Dec 30)</td><td>Week 2: nominal prepayment price for Common Wuliangye lowered to Rmb900 from Rmb1,019 for 2026 and distributor cost below c.Rmb850 (more rebate will be announced on 18 Dec)</td><td colspan="4"></td></tr><tr><td>2025</td><td>Nov</td><td>Week 4: New series of Moutai Prince (Black Gold) new version released</td><td colspan="5"></td></tr><tr><td>2025</td><td>Aug</td><td>W4: New version of Moutai 1935 was launched with suggested retail price set at Rmb998&#x27;</td><td colspan="5"></td></tr><tr><td>2025</td><td>Jun</td><td>W3: Suspended the shipment of 53% 500ml Feitian Moutai for all channels; Implemented disciplinary measures to distributors including punishments against selling below RMB2,000/bottle and restrictions from shipping to certain retailers.</td><td colspan="5"></td></tr><tr><td>2025</td><td>Apr</td><td>W4: Updated bundled sales policy in self-operated specialty stores for registered enterprise and individual customers</td><td></td><td>W4: Suspended order taking and shipment until pre-Dragon Boat Festival for all SKUs</td><td colspan="3"></td></tr><tr><td>2025</td><td>Feb</td><td colspan="2"></td><td>W3: Suspended order taking and shipment of Tequ 60 and Old Touqu</td><td>W2: Suspended order taking for 6th Ocean Blue in Jiangsu: Suspended order taking for Guiju - Gold/Red in Henan since Feb 14</td><td>W2: Suspended shipment of Qinghua 20; Laobaifen 10</td><td></td></tr><tr><td>2025</td><td>Jan</td><td></td><td>W2: Suspended shipment of 8th Common Wuliangye since Jan 9</td><td></td><td>W3: Online Shipment suspension for Sky and Ocean Blue since Jan 17 2025</td><td colspan="2"></td></tr></table>

Source: Yunjiu Toutiao, Jiuyejia, Company reports, Data compiled by GS Global Investment Research

Exhibit 7: 2024-2025 channel policy and product launch summary of key spirits companies - Part II

<table><tr><td>Year</td><td>Month</td><td>Anhui Gujing (000596.SZ)</td><td>Sichuan Swellfun (600779.SS)</td><td>Jiugui Liquor (000799.SZ)</td><td>King&#x27;s Luck (603369.SS)</td><td>ZJLD (6979.HK)</td><td>Shede Spirits (600702.SS) Not Covered</td></tr><tr><td>2025</td><td>Feb</td><td colspan="2"></td><td>W3: Jiugui suspended order taking for 52°/42° 500ml Jiugui Spirits (transparent packaging)</td><td>W1: King&#x27;s Luck has ceased accepting orders for Guoyuan 4K/2K</td><td colspan="2"></td></tr><tr><td>2025</td><td>Jan</td><td colspan="6"></td></tr><tr><td>2024</td><td>Dec</td><td colspan="4"></td><td>W2: ZJLD launched fourth-gen Zhen 15</td><td></td></tr><tr><td>2024</td><td>Nov</td><td colspan="3"></td><td>W3: King&#x27;s Luck launched 3 new SKUs for Planet. Large-bottle series named &quot;Grand moon&quot;/&quot;Grand Earth&quot;/&quot;Grand Sun&quot; (42%, 700ml) at..RSP of Rmb168/388/268 per bottle.</td><td colspan="2"></td></tr><tr><td>2024</td><td>Oct</td><td></td><td>W1: Raised price of Zhenniang series 52° 500ml by Rmb10 per bottle, effective since Oct 1; W3: suspended order taking of Zhennniang No.8 38c/42c/52c</td><td colspan="4"></td></tr><tr><td>2024</td><td>Aug-Sep</td><td colspan="6"></td></tr><tr><td>2024</td><td>July</td><td></td><td>W2: Adjusted suggested retail prices for Zhenniang No.8; price of 52-degree SKU up by Rmb20 per bottle, and that of 42/38-degree up by Rmb10 per bottle to...Rmb578/538/528 respectively, effective since Jun 20</td><td colspan="2"></td><td>W1: Lidu hiked the ex-factory price of the Lidu Sorghum 1308 by Rmb100 per bottle and group-purchase price by Rmb200; hiked the Lidu King ex-factory by Rmb20/bottle and group purchase price by 30</td><td></td></tr><tr><td>2024</td><td>Apr-Jun</td><td colspan="6"></td></tr><tr><td>2024</td><td>Apr</td><td colspan="4"></td><td>W1:Hiked retail price of Yingshanhong products (online exclusive) by 13% W3: suspended supply of 2nd gen Li Du 1955/1975 until further notice</td><td>W2: Hiked the ex-factory price of 64.5C Tianzihu 500ml (Chen Flavor and Strong flavor) by 500Rmb/bottle, effective from Apr 15; halved the planned production volume of Tianzihu to 5,000 bottles effective from 2024</td></tr><tr><td>2024</td><td>Mar</td><td colspan="4"></td><td>W1: Lidu launched the 2nd Lidu Sorghum and hiked the price to Rmb1,230 per bottle</td><td>W1: Hiked ex-factory price of Tequ Jiaoling 20/30 by Rmb10/15 per bottle</td></tr><tr><td>2024</td><td>Feb</td><td colspan="3"></td><td>W4: King&#x27;s Luck ceased accepting orders for 4th-gen Guoyuan 4K, and offers 5th-gen Guoyaun 4K/2K/1K with Rmb20/10/8 per bottle higher vs. 4th-gen since March 1, 2024, and suggests to hike wholesale/retail/ group buy price accordingly; Outside quota price to hike Rmb10/bottle</td><td colspan="2"></td></tr><tr><td>2024</td><td>Jan</td><td colspan="6"></td></tr></table>

Source: Yunjiu Toutiao, Jiuyejia, Data compiled by GS Global Investment Research

## Performance & Valuation

Exhibit 8: Select Spirits names - 2026 YTD and weekly (Jul 13 \~Jul 17) stock performance  
Shunxin (+9.5%) and Anhui Golden Seed (+8.5%) were relatively better price performers among China Spirits last week

![](images/44ab5bfa26e065a0fb90f08668f1d4a1e4f7ea641b1bbe719e7e42eef877d68f.jpg)  
Priced as of Jul 17, 2026.  
Source: LSEG Data & Analytics, Data compiled by GS Global Investment Research

## Valuation table

Exhibit 9: China Spirits Comps

<table><tr><td rowspan="2"></td><td rowspan="2">Company</td><td rowspan="2">Rating</td><td rowspan="2">Ccy</td><td rowspan="2">Price 7/17/2026</td><td rowspan="2">12-m TP</td><td rowspan="2">+/-</td><td colspan="3">PE</td><td colspan="3">TP Implied PE</td><td rowspan="2">26-28E Rev CAGR</td><td rowspan="2">26-28E NP CAGR</td><td colspan="3">EV/EBITDA</td><td>ROE</td><td>Div yield</td><td rowspan="2">YTD perf %</td></tr><tr><td>2026E</td><td>2027E</td><td>2028E</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2026E</td><td>2026E</td></tr><tr><td colspan="21">Spirits</td></tr><tr><td>600519.SS</td><td>Kweichow Moutai</td><td>Buy</td><td>CNY</td><td>1253.00

[中间内容因长度限制已省略]

including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for

equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
