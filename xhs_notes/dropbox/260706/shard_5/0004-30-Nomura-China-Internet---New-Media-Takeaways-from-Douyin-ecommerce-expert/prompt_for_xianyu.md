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
EQUITY: INTERNET & NEW MEDIA

# Takeaways from Douyin ecommerce expert call

Mixed cross-read for Alibaba and JD

Key highlights

The NOM China internet team recently hosted a group call with an operations manager from Douyin (unlisted) ecommerce. Douyin's 618 Gross Merchandise Volume (GMV) growth in 2026 missed internal targets (\~19% y-y vs. the expected 24%–25%) amid a broader ecommerce sector slowdown caused by weakening consumption and a diminishing contribution from trade-in subsidies. As a rank-and-file operations manager, the expert believes Douyin ecommerce is executing a strategic pivot away from aggressive top-line expansion toward a balanced growth model, prioritizing profitability to fund its AI infrastructure and LLM (e.g., Volcano Engine and Doubao). Hence, the expert thinks a realistic FY26 GMV growth target should be 15%-16% y-y (vs. FY25's 29% y-y), vs. the 19% target set in the beginning of the year.

## Cross-read for Alibaba and JD

We believe the entire China ecommerce sector may have experienced similar macro headwinds to those faced by Douyin ecommerce. As discussed in our 24 June report, we forecast that Alibaba's (BABA US, Buy) reported Customer Management Revenue (CMR) likely declined 8% y-y, while the like-for-like CMR may have remained flat y-y in the June quarter. This is likely below the Street's expected 3%–5% decline for the reported CMR, based on our earlier conversations with some investors.

Yet, despite potential downside risks to the top line, we believe the combined EBITA for BABA's broad core commerce segment may have a chance to come in line with Street expectations, backed by increasingly aggressive loss reduction for quick commerce (QC) and better profitability in international commerce. We further project that BABA may be ready to slow the cash burn for its consumer-facing AI chatbot, Qwen, amidst tight AI chip supplies and an elevated focus on enterprise-oriented AI solutions. All of these efforts should bode positively for the earnings outlook in 2H as the base is aligned. We forecast a V-shaped rebound in BABA's consolidated EBITA in 2H CY2026 (starting from the September quarter) by $78\%$ y-y.

JD.com (JD US, Buy) earlier guided cautiously on its 2Q outlook, expecting JD Retail (JDR) revenue to drop 7%–8% y-y. We believe there is potential upside to this rather cautious 2Q guidance thanks to stronger 618 promotional results. However, the outlook for 2H remains challenging. While the base is trending lower, the pressure on JD's core consumer electronics is likely heightening. Apple (AAPL US, Not rated) recently announced price hikes of 20%–25% on select Mac and iPad models due to cost increases. According to our Douyin ecommerce expert, this action may trigger a chain of price hikes for domestic brands now that Apple has set the precedent. Unless the Chinese government doubles down on its subsidy for this category, the electronic goods category will likely confront a steeper uphill climb in 2H, in our view.

## Douyin ecommerce expert call takeaways

Overview of 618 sales: growth missed target, weaker consumer demand, more disciplined subsidies

The expert characterized this year's 618 e-commerce festival as one of the weakest in recent years, featuring low growth and minimal consumer buzz. For Douyin ecommerce specifically, 618 GMV growth was around 19% y-y, falling below the original target of 24%–25%. This followed a similarly moderate 1Q26 GMV growth rate of 19.4% y-y. For perspective, Douyin ecommerce managed to grow 29% in 2025 (Fig. 2).

The expert attributed the weaker-than-expected 618 performance to several factors:

Research Analysts

China Internet & New Media

Jialong Shi - NIHK

Jialong.shi@NOM.com

+852 2252 1409

Rachel Guo - NIHK

rachel.guo@NOM.com

+852 2252 1400

\- Softening consumption: Overall consumption momentum has softened since late March, with weakness increasing in online retail alongside offline channels.

\- High base effect: Last year's 618 created a high base, as major platforms—including Taobao/Tmall, Douyin, and JD—were significantly aggressive with promotions and subsidies.

\- Simplified mechanics: This year's promotional mechanics were simplified and proved less effective at driving incremental GMV through cross-selling.

\- Fading subsidy tailwinds: Categories previously boosted by trade-in subsidies, especially home appliances and consumer electronics, have started to lose momentum as subsidies retreat and earlier demand was front-loaded into last year.

Subsidy spending increased in absolute terms, but the expert emphasized that the intensity remained disciplined. Douyin's consumer-end subsidy spending during the 618 campaign (which lasted for around 35 days) was close to CNY3.5bn, vs. CNY2.6bn–CNY2.7bn last year. However, the average discount rate was only around 15%, lower than last year's roughly 17%. This suggests that while total subsidy spending rose due to scale, the platform was not materially more aggressive regarding discount intensity.

According to the expert, Douyin ecommerce continues to be plagued by a high return rate. The 1Q26 return/refund rate was around $47\%$ , implying a settlement rate of roughly $53\%$ . The high return rate was mainly due to category mix and purchase behavior. Apparel, bags, and shoes currently account for roughly $38\%$ of Douyin ecommerce's GMV; these non-standard categories historically carry higher return rates. Additionally, Douyin's live-streaming and short-video commerce model is more impulse-driven than traditional search-based ecommerce platforms like Alibaba, further elevating post-purchase returns.

## Douyin is balancing scale growth and profitability

Douyin's original FY26 full-year GMV target was around 18%–19% y-y, but the expert believes this target is increasingly difficult to achieve as 1H growth came in at only around 19% and the outlook for 2H26 remains challenging. A more realistic full-year growth rate could be around 15%–16%, with an internal target review likely scheduled for July.

Importantly, the expert does not expect Douyin to materially increase subsidies or investments just to defend its top-line target. This reflects a broader strategic shift from aggressive GMV expansion toward a more balanced approach across scale, revenue, and profitability. Douyin Ecommerce has already grown into a very large business and, according to the expert, is now more focused on stability than on maximum market share gains.

## Agentic commerce: early stage but strategically important

The cooperation between Doubao and Douyin ecommerce is still in an early stage. According to the expert, the project only began to expand and iterate around February–March 2026. The current GMV contribution from Doubao remains small, at around 2% of Douyin's ecommerce GMV.

That said, the expert views this as one of the most important strategic initiatives for next year. The current focus is not on near-term GMV contribution, but rather product iteration, data integration, supply-chain integration, and product-catalogue understanding. Doubao needs to process and comprehend a massive product library before it can serve as an effective AI shopping assistant, according to the expert.

Apple price hikes and implications for broader ecommerce

Apple recently announced price increases of 20%–25% for select models of Mac laptops and tablets. Douyin Ecommerce's exposure to Apple products is limited, as Apple only opened its official flagship store on Douyin last year and previously relied more heavily on authorized resellers. As a result, the direct impact of Apple's price hikes on Douyin should be limited, according to the expert.

The broader implications, however, are more significant. The expert believes that Apple's price hikes could signal a wider cost-pressure trend across consumer electronics, as many brands face the pinch of rising cost structures. If Apple raises prices, other electronics brands may follow. This could create further pressure on the consumer electronics and home appliance categories in 2H26, according to the expert. In view of the expert, this is negative not only for Douyin but also for the broader ecommerce industry, especially platforms with higher exposure to electronics and appliances, such as JD.

Douyin's strategy toward quick commerce: low priority

The expert believes that Douyin is unlikely to make quick commerce (QC) a major strategic priority in the near-term. Although Douyin has integrated “one-hour arrival” fulfilment services into certain categories on its ecommerce marketplace, the expert does not view this as a sign of a major escalation against Alibaba or Meituan (3690 HK, Buy) in the QC space.

The key reason is that QC requires more than just traffic; it necessitates local merchant supply, warehousing, logistics, fulfilment infrastructure, operational subsidies, and strong local execution. Compared with Alibaba and Meituan, Douyin does not possess an obvious competitive advantage in these crucial areas. The expert also noted that existing players are already reducing subsidies in food delivery, which further reduces the appeal of the QC business to Douyin's senior management.

## More expert calls to come next

The NOM China internet team will continue to host calls with industry experts in the days to come. Please refer to below table for the latest schedule. Please contact the NOM sales team if interested to join any of the calls.

Fig. 1: China internet expert series schedule

<table><tr><td>#</td><td>Date</td><td>Time (HKT)</td><td>Topic</td><td>Speaker Bio</td></tr><tr><td>1</td><td>Tue, 23 Jun</td><td>09:30-10:30</td><td>Douyin local service: will it try to grab more market shares?</td><td>Expert from ByteDance local service in charge of local hotel and travel business</td></tr><tr><td>2</td><td>Tue, 23 Jun</td><td>15:30-16:30</td><td>Online music streaming: Soda Music&#x27;s growth strategies and targets</td><td>Expert works for Soda Music as a product manager</td></tr><tr><td>3</td><td>Fri, 26 Jun</td><td>09:30-10:30</td><td>ByteDance cloud business: what&#x27;s the latest market landscape and competitive intensity?</td><td>Expert from ByteDance cloud business in charge of client engagement in the pan-internet and AI U Mirahani search</td></tr><tr><td>5</td><td>Tue, 30 Jun</td><td>09:30-10:30</td><td>Douyin E-commerce: 618 promotions review and 2H outlook</td><td>Expert works for Douyin ecommerce as an operation manager</td></tr><tr><td>6</td><td>Tue, 30 Jun</td><td>15:30-16:30</td><td>China travel industry: taking pulse on the strength of travel post the fuel surcharges adjustments *CPT Eligible*</td><td>Mr. Lei Wang, Head of data intelligence division, Flights Management</td></tr><tr><td>7</td><td>Fri, 3 Jul</td><td>09:30-10:30</td><td>TikTok expert: Check for the latest ecommerce growth trends in overseas markets</td><td>Expert works for TikTok shop as a cross-border logistics solution manager</td></tr><tr><td>8</td><td>Fri, 3 Jul</td><td>15:30-16:30</td><td>LLM (1): How to view the evolution of China&#x27;s LLM market competitiveness and commercialization trajectory</td><td>Expert works for a leading Chinese AI lab as a product manager</td></tr><tr><td>9</td><td>Tue, 7 Jul</td><td>15:30-16:30</td><td>Online healthcare: What&#x27;s the impact of recently released regulations on online healthcare platform sales?</td><td>Expert works from a leading Chinese online healthcare platform as a KA and brand operation manager</td></tr><tr><td>10</td><td>Thu, 9 Jul</td><td>09:30-10:30</td><td>LLM (2): How to view the evolution of China&#x27;s LLM market competitiveness and commercialization trajectory</td><td>Expert from a Chinese research lab in charge of AI research</td></tr><tr><td>4</td><td>Thu, 9 Jul</td><td>15:00-16:00</td><td>AI animated drama and short drama: the industry status quo and the growth sustainability</td><td>Expert is from China&#x27;s No 1 short-drama platform, Red Fruit, which is owned by ByteDance</td></tr></table>

Source: NOM

Fig. 2: Douyin ecommerce GMV growth trend (% y-y)  
![](images/68c83cfafe489c7f4545eff02b75612080730e90e4cc05500217ee9d4401807e.jpg)  
Source: Company data, NOM estimates

## Appendix A-1

This report has been produced by NOM International (Hong Kong) Ltd. (NIHK), Hong Kong. See Disclaimers for NOM Group entity details.

## Analyst Certification

We, Rachel Guo and Jialong Shi, hereby certify (1) that the views expressed in this Research report accurately reflect our personal views about any or all of the subject securities or issuers referred to in this Research report, (2) no part of our compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this Research report and (3) no part of our compensation is tied to any specific investment banking transactions performed by NOM Securities International, Inc., NOM International plc or any other NOM Group company.

## Issuer Specific Regulatory Disclosures

The terms "NOM" and "NOM Group" used herein refer to NOM Holdings, Inc. and its affiliates and subsidiaries, including NOM Securities International, Inc. ('NSI') and Instinet, LLC ('ILLC'), U. S. registered broker dealers and members of SIPC.

Materially mentioned issuers

<table><tr><td>Issuer</td><td>Ticker</td><td>Price</td><td>Price date</td><td>Stock rating</td><td>Sector rating</td><td>Disclosures</td></tr><tr><td>Meituan</td><td>3690 HK</td><td>HKD 71.60</td><td>03-Jul-2026</td><td>Buy</td><td>N/A</td><td>A10</td></tr><tr><td>Alibaba Group Holding</td><td>BABA US</td><td>USD 96.14</td><td>02-Jul-2026</td><td>Buy</td><td>N/A</td><td>A10</td></tr><tr><td>JD.com</td><td>JD US</td><td>USD 26.62</td><td>02-Jul-2026</td><td>Buy</td><td>N/A</td><td>A10</td></tr></table>

A10 The NOM Group is a registered market maker in the securities / related derivatives of the issuer.

![](images/307ab6bb1677b261dc783fa72a9bad58a6df68252db2880bf881e289af7d16b0.jpg)  
For explanation of ratings refer to the stock rating keys located after chart(s)

Valuation Methodology We value the food delivery business at USD16bn based on 7x FY28F P/E and discounted to FY26. We value the instashopping business at USD5bn based on 15x FY27F P/E and discounted to FY26. We value the in-store, hotel and travel business at USD21bn based on 8x FY27F P/E and discounted to FY26. We value the new business at USD28bn, based on 1.5x FY26F P/S. The resulting TP is HKD109. The benchmark index for the stock is the Hang Seng Index. Risks that may impede the achievement of the target price Downside risks include: (1) intensifying competition in the food delivery or in-store consumption verticals; and (2) worse-than-expected performance in the new initiatives.

USD 96.14 (02-Jul-2026) Buy (Sector rating: N/A)  
![](images/a6638fe4e122c6045ca6cb9d94ad225ed6c660a62b56094a4a38901a61887645.jpg)  
For explanation of ratings refer to the stock rating keys located after chart(s)

Valuation Methodology We value Alibaba's China Ecommerce Group at USD89bn, based on 5x FY27F P/E; its AliCloud business at USD270bn, based on 7x FY28F P/S; and its net valuation of non-core assets (including international ecommerce business) at USD40bn. The resulting TP is USD178. The benchmark index for this stock is Nasdaq Composite. Risks that may impede the achievement of the target price Downside risks include: margin downside due to ramp-up in investments; regulatory risks related to the payment and internet finance industry, which could hurt Alibaba's main business and its value in Ant Group.

USD 26.62 (02-Jul-2026) Buy (Sector rating: N/A)  
![](images/a149560cdf3f9fa6612ec56def805b2c2345557ee6bfe7f47dc2e38f66b4fb3c.jpg)  
For explanation of ratings refer to the stock rating keys located after chart(s)

Valuation Methodology Our SOTP-based TP

[中间内容因长度限制已省略]

bai Financial Services Authority) in the United Arab Emirates ('UAE') or a 'Market Counterparty' or a 'Business Customer' (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar ('Qatar') by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than 'Authorised Persons', 'Exempt Persons' or 'Institutions' located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
