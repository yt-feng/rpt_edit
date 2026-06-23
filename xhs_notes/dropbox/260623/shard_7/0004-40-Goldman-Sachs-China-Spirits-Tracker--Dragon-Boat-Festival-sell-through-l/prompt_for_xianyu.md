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
# China Spirits Tracker: Dragon Boat Festival sell-through lapping low base but demand remained polarized across pricing tier; More resilient

Dragon Boat Festival (Jun 19-21) consumption sentiment: Overall pax mobility recorded a -0.9% yoy decline at 648mn, per Ministry of Transport. Retail and catering demand: key 78 shopping areas had 4%/3.5% yoy growth in total traffic and retail sales for the first two days (MOFCOM monitored scope).

Dragon Boat Festival spirits demand remained highly polarized by price range and consumption scenario, with sell-through recovery mainly concentrated in super-premium category and selected regions, while the upper mid end segment remained under pressure. Our latest channel checks suggest Dragon Boat Festival sell-through improved slightly yoy but still meaningfully below the 2024 level (pre Anti-graft policy in May 2025) for the spirits sector. For the super-premium category, most regions saw 10\~20%+ yoy sell-out volume growth for Moutai/Wuliangye with prepayment of 60%+/55%-70%, respectively (while sell-out declined by DD% in Dragon Boat Festival in 2025, ie. down c.10\~20% for Feitian). Meanwhile, sub-premium/mass products are relatively muted yoy except for some key SKUs/regions like King's Luck's Danya reaching DD% sell-through growth (Exhibit 1). Online shared a similar trend, with JD 618 report indicating that overall spirits GMV increased 25% yoy driven by strong growth in Moutai (Feitian original package GMV reached Rmb300mn) and Wuliangye (Common 8th Wuliangye World Cup edition GMV increased over 13-fold). Overall, we noted that Dragon Boat Festival typically has a small seasonal impact on China's spirits consumption vs Mid Autumn Festival/National Holiday and 618 promotional intensity was relatively rational and less disruptive to offline wholesale pricing this year (e.g. Feitian online ASP post-subsidy had a small gap vs distribution channel wholesale prices).

On the demand side, traditional business-related/government related demand still remained significantly below historical levels, while gifting and mass self-consumption continued to serve as the key demand pillars. Banquet scenario consumption volume also remained weak. Gifting demand remained the key pillar for Feitian Moutai, while sell-through for regional mid-end brands (Rmb 100+\~300 price range) was still mainly driven by personal consumption/dining demand. Regional divergence persisted: Anhui remained relatively weak amid ongoing constrained commercial/government-related activities, while Jiangsu/Sichuan saw slight recovery. Jiangsu showed signs of easing policy impact, with mom improvements driven by development of technology sectors. In Sichuan, business demand increased by teens% yoy, although it remained 30%-40% below 2024 levels.

Feitian Moutai wholesale price slightly decreased, while Common Wuliangye

Leaf Liu
+852-3966-4169 | leaf.liu@gs.com
GS (Asia) L.L.C.

Christina Liu
+852-2978-6983 | christina.liu@gs.com
GS (Asia) L.L.C.

Valerie Zhou
+852-2978-0820 | valerie.zhou@gs.com
GS (Asia) L.L.C.

and Guojiao 1573 stayed largely flattish. In the past 1 week, original case Feitian Moutai's wholesale price/bottle decreased by Rmb25 from Rmb1,670 to Rmb1,645, and unpacked Feitian Moutai's wholesale price decreased by Rmb5 from Rmb1,635 to Rmb1,630. For non-standard Moutai SKUs, the wholesale price of Zodiac/Moutai 1L decreased by Rmb10/120 per bottle, Jingpin Moutai stayed flattish and Moutai 15 years increased by Rmb10 per bottle. Common Wuliangye's wholesale price/bottle stayed flattish/decreased by Rmb10 at Rmb840/to Rmb750 per "Daily Spirits Prices"/Bairong Wholesale Market, respectively. Guojiao 1573's wholesale price/bottle stayed flattish at Rmb840.

The authors would like to thank Lily Qi for her contribution to this report.

Exhibit 1: Post Dragon Boat Festival channel check summary table

<table><tr><td>Brand</td><td>Sell-through</td><td>Prepayment YTD</td><td>Distributor inventory</td><td>Wholesale price trend</td></tr><tr><td>Moutai</td><td>Feitian 20%+ yoy growth YTD</td><td>c.63% (Jun prepayment executed, 5% of full year)</td><td></td><td>Feitian at Rmb1,630-1,645/ bottle; non-standard SKUs price slightly decreased recently</td></tr><tr><td>Wuliangye</td><td>Common Wuliangye 20%+ yoy growth; 1618 is expected to grow at 15%</td><td>overall 55%-70% (divergent nationwide), 1618 at 70%</td><td></td><td>Common Wuliangye stable at Rmb750/bottle</td></tr><tr><td>Luzhou Laojiao</td><td>Decreased significantly, esp. in Henan</td><td>30%+ (40-60% last year for most distributors)</td><td></td><td>Guojiao 1573 price stable at Rmb850/bottle</td></tr><tr><td>Fen Wine</td><td>10%+ growth YTD, DD% growth for Bofen</td><td>45%-55% (55% in same period last year), no compulsory prepayment</td><td>Qing 20 at c.3.5 months</td><td>Qing 20 price stable at Rmb350/bottle</td></tr><tr><td>King&#x27;s Luck</td><td>slightly improved in 2Q; DD% growth for Danya driven by stable channel profit and strict pricing policy</td><td>55% for mid-Jun, expect to reach 60% in end-Jun, slower yoy</td><td>c.4 months+</td><td>largely stable for key SKUs</td></tr><tr><td>Yanghe</td><td>slightly decreased in 2Q</td><td>40%+</td><td>Ocean Blue &lt; 2 months</td><td>largely stable for key SKUs</td></tr><tr><td>Gujing</td><td>Dragon Boat Festival sell-through backed by Rmb200 below price range (mass product)</td><td>55%-60%+ (vs 70% target from company at end-2Q)</td><td>&gt;3 months</td><td>Resilient for Rmb300+ price range in Anhui</td></tr></table>

Source: Channel checks  
Weekly Momentum of China Spirits Sector

![](images/52ec476f2204e83d5075ee0a64973b8904c1e428c8121bdc357df625ce22ba82.jpg)  
Source: GS Global Investment Research

i-Moutai APP tracker: Our Quest Mobile database indicated monthly active users (MAU) on the i-Moutai app reached 10.2mn/10.1mn in May/Apr, up by 4.4%/0.4% yoy, normalized vs. 18mn MAU in 1Q26 on average and is still above the level before Feitian Moutai's launch (MAU at 5\~7mn in 4Q25). DAU/MAU penetration ratio was at 11%/11% in May/Apr.

Exhibit 2: I-Moutai active users surged from Jan 1st 2026 when Feitian was officially launched on i-Moutai  
![](images/4863b459c63e007d75581e040558ad796783ef335d7d9b0f040894f2da38e692.jpg)  
Source: Quest Mobile

## Key news this week:

Moutai announced its 2025 final dividend distribution (Jun 21): Moutai's 2025 dividend distribution was approved on Jun 21 with a cash amount of Rm35.033bn (2025 accumulated dividend at Rmb65.033bn after including interim dividend) and ex-dividend date on Jun 26.

JD released its 618 spirits report (Jun 19): JD released its 618 spirits report covering May 13 to Jun 18, showing 25% yoy growth for overall spirits GMV and strong growth for brands including Moutai/Wuliangye/Guotai etc. Moutai 26 Feitian (original package) GMV reached Rmb300mn and Common 8th Wuliangye (collaborating with World Cup 2026) GMV increased over 13-fold.

\- Jiugui collaborated with Hunan restaurant chains during Dragon Boat Festival (Jun 19): Jiugui launched its 2026 Dragon Boat Festival themed event with well-known Hunan cuisine restaurant chains including Huogongdian and Qinhuang shifu.

## Wholesale price summary of high-end liquors

## From Jun 12 to Jun 21, 2026:

Original case Feitian Moutai's wholesale price/bottle decreased by Rmb25 from Rmb1,670 to Rmb1,645, and unpacked Feitian Moutai's wholesale price decreased by Rmb5 from Rmb1,635 to Rmb1,630.

Common Wuliangye's wholesale price/bottle stayed flattish/decreased by Rmb10 at Rmb840/to Rmb750 per “Daily Spirits Prices”/Bairong Wholesale Market, respectively.

Guojiao 1573's wholesale price/bottle stayed flattish at Rmb840.

From Jan 1 to Jun 21, 2026:

Original case Feitian Moutai's wholesale price/bottle increased by Rmb140 from

Rmb1,505 to Rmb1,645. Unpacked Feitian Moutai's wholesale price/bottle increased by Rmb140 from Rmb1,490 to Rmb1,630.

Common Wuliangye's wholesale price/bottle decreased by Rmb10 to Rmb840 per "Daily Spirits Prices," and decreased by Rmb60 to Rmb750 per Bairong Wholesale Market.

Guojiao 1573's wholesale price/bottle stayed flattish at Rmb840.

Exhibit 3: 53% Feitian Moutai product prices  
![](images/c2ed777183542d6b1182e3968bcef3e689044daedde7bca6ee389f343659f2c4.jpg)  
Most recent data points as of Jun 21, 2026.  
Source: Daily Spirits Prices, Data compiled by GS Global Investment Research

Exhibit 4: 52% Common Wuliangye product prices  
![](images/b7887a67453be5ced47a7d9c29d8c97841b363de15f19cd46cc3f2cf1e08ef35.jpg)  
Most recent data points as of Jun 21, 2026. Source 1 = Spirits Price References; Source 2 = Daily Spirits Prices; Source 3 = Bairong Wholesale Market  
Source: Spirits Price References, Daily Spirits Prices, Bairong Wholesale Market, Data compiled by GS Global Investment Research

Exhibit 5: Guojiao 1573 product prices  
![](images/75d7e4b75c4e285d926adb91a0b7483b9694ee6ec29b5d0bde2786252cd4cfff.jpg)  
Most recent data points as of Jun 21, 2026.  
Source: Daily Spirits Prices, Data compiled by GS Global Investment Research

Moutai non-standard SKUs: In the past 1 week, the wholesale price of Zodiac/Moutai 1L decreased by Rmb10/120 per bottle, Jingpin Moutai stayed flattish and Moutai 15 years increased by Rmb10 per bottle.

Exhibit 6: Wholesale prices of Moutai's 4 non-standard SKUs  
![](images/62f9c22b05383cb04422714afe28392ffbd90c4aeeecf9c58214c9ffb507e990.jpg)  
Rmb/bottle Jingpin Moutai (53%, 500ml)

![](images/d7879f400ce86aca9682f092c22208f379baa08ddd7e9e73abd0698c29ead5f4.jpg)

![](images/ed7f962aa5cf6d1e13d0c5f97d2bddc5f24f3d2d8229b8f56fbb9df2c7ec35fb.jpg)  
Latest data as of Jun 21, 2026.

Rmb/bottle Moutai 15 years (53%, 500ml)  
![](images/27aaa06073ab9432507070f5b060265dc5e617b1d0b79056967ade558df751e1.jpg)

Exhibit 7: 2024-2026 channel policy and product launch summary of key spirits companies - Part I

<table><tr><td>Year</td><td>Month</td><td>Kweichow Moutai (600519.SS)</td><td>Wuliangye Yibin (000858.SZ)</td><td>Luzhou Laojiao (000568.SZ)</td><td>Jiangsu Yanghe (002304.SZ)</td><td>Shanxi Fen Wine (600809.SS)</td><td>Jian Nan Chun(Private, Not Covered)</td></tr><tr><td>2026</td><td>May</td><td>Week 3: Moutai raised the RSP of select non-standard SKUs on a Moutai APP effective May 16. The scope of price hikes include 53% vol 500ml Moutai 15 years (Rmb4,199/bottle to Rmb4,279/bottle), Jingpin Moutai (Rmb2,299/bottle to Rmb2,359/bottle), Zodiac Moutai (Horse precious) (Rmb2,499/bottle to Rmb2,669/bottle) and 1L Moutai (Rmb2,989/bottle to Rmb3,119/bottle).</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2026</td><td>Mar</td><td>Week 4: raised the ex-factory price of Feitian Moutai (53% vol, 500ml, 2026 edition) from Rmb1,169/bottle to c.Rmb1,269 per bottle (mainly cover wholesale channels), and the RSP of Feitian Moutai from Rmb1,499 to Rmb1,539 (mainly cover direct sales channels, esp. i-Moutai platform), effective immediately from Mar 31, 2026.</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2026</td><td>Mar</td><td>Week 3: introduced a consignment sales policy for non-standard Moutai products participating distributors must apply and pay a deposit and will receive a c.5% rebate on these products sales</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2026</td><td>Jan</td><td>Week 3: plans to employ a more market-driven pricing framework to optimize channel investments and safeguard channel profitability, presented new RSP for Feitian Moutai vintage and other non-standard SKUs and lowered ex-factory price for some non-standard/series products</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2025</td><td>Dec</td><td>Week 5: officially announced the launch of Feitian Moutai across 53% vol 500ml (years 2019-2026), 100ml/1,000ml Feitian, and multiple series on i-Moutai, including Jingpin, Zodiac, Vintage, Cultural, and lower-alcohol variants (Dec 30)</td><td>Week 2: nominal prepayment price for Common Wuliangye lowered to Rmb900 from Rmb1,019 for 2026 and distributor cost below c.Rmb850 (more rebate will be announced on 18 Dec)</td><td></td><td></td><td></td><td></td></tr><tr><td>2025</td><td>Nov</td><td>Week 4: New series of Moutai Prince (Black Gold) new version released</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2025</td><td>Aug</td><td>W4: New version of Moutai 1935 was launched with suggested retail price set at Rmb998&#x27;</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2025</td><td>Jun</td><td>W3: Suspended the shipment of 53% 500ml Feitian Moutai for all channels; Implemented disciplinary measures to distributors including punishments against selling below RMB2,000/bottle and restrictions from shipping to certain retailers.</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2025</td><td>Apr</td><td>W4: Updated bundled sales policy in self-operated specialty stores for registered enterprise and individual customers</td><td></td><td>W4: Suspended order taking and shipment until pre-Dragon Boat Festival for all SKUs</td><td></td><td></td><td></td></tr><tr><td>2025</td><td>Feb</td><td></td><td></td><td>W3: Suspended order taking and shipment of Tequ 60 and Old Touqu</td><td>W2: Suspended order taking for 6th Ocean Blue in Jiangsu; Suspended order taking for Guijiu - Gold/Red in Henan since Feb 14</td><td>W2: Suspended shipment of Qinghua 20; Laobafen 10</td><td></td></tr><tr><td>2025</td><td>Jan</td><td></td><td>W2: Suspended shipment of 8th Common Wuliangye since Jan 9</td><td></td><td>W3: Online Shipment suspension for Sky and Ocean Blue since Jan 17 2025</td><td></td><td></td></tr><tr><td>2024</td><td>Dec</td><td></td><td></td><td></td><td></td><td></td><td>W4: Launched Zodiac Spirits for the Snake year:at::RSP of::Rmb1,299/bottle</td></tr><tr><td>2024</td><td>Nov</td><td>W1: Suspended shipment from distributors to retail terminals of all SKUs in some regions</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2024</td><td>Aug</td><td></td><td></td><td></td><td></td><td>W4: Launched new super premium::products..&quot;Master&quot;:series on Aug 21</td><td></td></tr><tr><td>2024</td><td>Jul</td><td>W1: Suspended shipment of Moutai 1935 from Jul 2</td><td></td><td>W1: Hiked the within-quota price of 38C Guojiao 1573 by Rmb30 per bottle effective from Jul 2; Laojiao distribution company suspended order-taking and shipment of 52C Laojiao effective from Jul 3</td><td></td><td></td><td></td></tr><tr><td>2024</td><td>Jun</td><td>W1: Asked distributors to split prepayment to two times for June (3%-4% of annual); Suspended direct sales of Feitian to enterprises at Rmb1,499 in some regions and suspended evaluation of qualifying enterprises W2/W3: Ceased &quot;open case&quot; policy of Feitian::Moutai and distribution of Feitian in large cases, Controlled shipment quota for June; Suspended 375ml Feitian::on Xunfeng; Suspended shipments of 15-year and Jingpin::Moutai; Communicated with distributors to control wholesale prices above Rmb2,400; Requested supply suspension::on channels of::Guizhou distributors</td><td></td><td>W4: Ceased the order-taking and shipment of 38° Guojiao 1573 since Jun 28</td><td></td><td>W1: Hiked the ex-factory price of Laobafen series by Rmb5/bottle, effective since Jun 20</td><td></td></tr><tr><td>2024</td><td>May</td><td></td><td>W2: Launched 45% common Wuliangye in 1st-batch 52 cities with ex-If suggested retail price at Rmb839/1,199</td><td></td><td></td><td></td><td></td></tr><tr><td>2024</td><td>Apr</td><td></td><td></td><td>W1: Hiked the outside quota price of Touqu by Rmb14 per bottle, effective immediately</td><td>W1: Hiked the ex-factory price of M6+ by Rmb20 per bottle, effective from:-Apr&#x27; 1st 2024</td><td></td><td></td></tr><tr><td>2024</td><td>Mar</td><td></td><td>W1: Launched new retail sales platform; hiked the Jianzhu

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
