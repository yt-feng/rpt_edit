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
# China Internet & New Media

EQUITY: INTERNET & NEW MEDIA

# Takeaways from TikTok shop logistics expert call

Strong GMV momentum supports J&T, while SEA remains better suited to an asset-light model

Key highlights

The NOM China Internet Team recently hosted a call with an expert from TikTok shop (TTS; owned by Bytedance) in charge of logistics solution provision in Southeast Asia (SEA). The expert noted that TTS's e-commerce growth remains robust, with 1H26 GMV reaching \~USD35bn. Southeast Asia and the US remain the key contributors, with growth around doubling in 1H26. For J&T (1519 HK, Buy), the near-term outlook remains supported by its deep integration with TTS. J&T continues to handle a very high share of TTS parcels across most Southeast Asian markets thanks to its strong fulfillment capability, broad network coverage and cost advantages, according to the expert. In Indonesia, regulatory scrutiny may push TTS to onboard more regional logistics providers, but the expert believes that any near-term share loss risk for J&T is likely to be manageable given its scale, service quality and cost competitiveness compared to potential onboarding regional players. Besides, an asset-light third-party logistics and local warehouse ecosystem remains more suitable for TTS in SEA than a capital-intensive FBT-style model, especially given a relatively low AOV in this region, according to the expert.

## TTS's GMV remains strong, with SEA and the U.S. as key growth engines

TTS delivered strong growth in 1H26, with global GMV reaching \~USD35bn. By region, SEA remained the largest contributor, accounting for around 53% of GMV and growing by roughly 100% y-y. The North America market (mainly the US) also scaled meaningfully, contributing around 29% of the GMV, up more than 130% y-y from a lower base last year, which was affected by tariff-related disruptions. Europe remains smaller, contributing around 10% of GMV, while Latin America is still in an early ramp-up stage. According to the expert, TTS has a good opportunity to achieve its aggressive full-year GMV target of \~USD100bn, particularly given the heavier promotional cadence expected in 2H26.

## SEA remains a high-growth, low-AOV market where TTS has not yet pushed FBT aggressively

In SEA, TTS's AOV remains low and relatively stable at around USD4–5, except for Singapore, where AOV is higher but overall contribution is limited. TikTok Shop's daily parcel volume in the region has already reached meaningful scale, estimated by the expert at around 20–30mn parcels per day. Parcel volume growth remains strong, with 2Q growth broadly in line with 1Q (nearly doubling y-y). By country, Indonesia is the largest Southeast Asian market, contributing roughly 30% of regional parcel volume, while Thailand was highlighted as one of the fastest-growing markets in 1H26. For J&T, we think the cross-reading is positive. Given TTS is a major parcel volume contributor for J&T in SEA, TTS's continued GMV and parcel volume growth should support J&T's 2Q parcel volume momentum in this region.

TTS has introduced FBT, or Fulfilled by TikTok, a logistics model comparable to Amazon's (AMZN US, Not rated) FBA model to improve delivery speed and user experience. Under FBT, sellers place inventory into TikTok's warehouse or fulfillment network, while TikTok manages warehousing, picking, packing and outbound delivery. TTS has advanced its FBT build-out in the US, while Europe remains at an earlier stage of rollout. However, according to the expert, TTS is not aggressively pushing a large-scale FBT-style warehouse and fulfillment model in SEA. This is mainly due to the region's low AOV and limited consumer willingness to pay for ultra-fast delivery. As a result, TTS is more likely to pursue a lighter warehouse ecosystem model by working with local certified warehouses through managing fulfillment standards with policy incentives rather than

Research Analysts

China Internet & New Media

Rachel Guo - NIHK

rachel.guo@NOM.com

+852 2252 1400

Jialong Shi - NIHK

Jialong.shi@NOM.com

+852 2252 1409

directly operating a large-scale fulfillment network in SEA, according to the expert.

Indonesia's logistics investigation on TTS may not lead to J&T's abrupt share loss The logistics-related antitrust investigation on TTS in Indonesia appears to focus on TTS's logistics allocation model and the high concentration of parcels handled by its leading logistics partners like J&T, according to the expert. The local logistics association's requests are broadly two-fold. First, it wants merchants to have more direct control over logistics provider selection, rather than having TTS allocate parcels through its internal algorithmic system. Second, it wants TTS to open its logistics interface and allow more third-party logistics providers to enter the platform's fulfillment pool.

The expert believes that a more likely compromise is that TTS maintains its centralized allocation system to balance service quality, network coverage and fulfillment cost, which TTS is unlikely to fully give up, while expanding the pool of eligible logistics partners such as more regional providers with strength in specific geographies. This would also help alleviate TTS's concern of high concentration on a leading logistics partner.

For J&T, this could create some diversification risks, but the near-term impact is likely to be limited, according to the expert, as J&T's broad network coverage, strong fulfillment capability and cost advantages should help it defend a significant share of TTS parcels.

Fuel cost inflation has limited impact on SEA e-commerce logistics economics According to the expert, fuel price increases have had a limited impact on SEA's e-commerce delivery costs, as around 60% of unit cost per parcel are related to last-mile delivery, mainly courier cost, while line-haul transportation accounts for \~20%. Fuel costs only affect part of the line-haul component. Meanwhile, TTS and J&T renegotiate logistics pricing annually. Historically, TTS usually cut unit parcel price by single digit y-y, supported by rising parcel volume provided. This year, however, fuel cost inflation has reduced the scope for further price cuts, leading to only minimal final pricing adjustments. According to the expert, TTS is unlikely to apply excessive pricing pressure on J&T, as weakening service quality as a result of irrational parcel price could hurt user experience on the platform. We, therefore, believe J&T should be able to maintain a reasonable profit margin in SEA despite fuel cost pressures.

## Large-scale self-built logistics is not a near-term priority for TTS in SEA

Logistics is capital- and operations-intensive, while TikTok Shop's current third-party logistics model remains functional and cost-effective, according to the expert. The platform has not yet faced a severe fulfillment pain point that would require it to build a large self-operated logistics network. Thus, the more likely near-term strategy is to remain asset-light, rely on third-party logistics partners, maintain centralized allocation, and selectively test self-built capabilities in specific markets such as Indonesia by leveraging Tokopedia's (owned by TTS) self-operated logistics capabilities. According to the expert, a full-scale shift to self-operated logistics does not appear to be the base case.

HKD 9.25 (03-Jul-2026) Buy (Sector rating: N/A)

## Appendix A-1

This report has been produced by NOM International (Hong Kong) Ltd. (NIHK), Hong Kong. See Disclaimers for NOM Group entity details.

## Analyst Certification

We, Rachel Guo and Jialong Shi, hereby certify (1) that the views expressed in this Research report accurately reflect our personal views about any or all of the subject securities or issuers referred to in this Research report, (2) no part of our compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this Research report and (3) no part of our compensation is tied to any specific investment banking transactions performed by NOM Securities International, Inc., NOM International plc or any other NOM Group company.

## Issuer Specific Regulatory Disclosures

The terms "NOM" and "NOM Group" used herein refer to NOM Holdings, Inc. and its affiliates and subsidiaries, including NOM Securities International, Inc. ('NSI') and Instinet, LLC ('ILLC'), U. S. registered broker dealers and members of SIPC.

## Materially mentioned issuers

<table><tr><td>Issuer</td><td>Ticker</td><td>Price</td><td>Price date</td><td>Stock rating</td><td>Sector rating</td><td>Disclosures</td></tr><tr><td>J&amp;T Express</td><td>1519 HK</td><td>HKD 9.25</td><td>03-Jul-2026</td><td>Buy</td><td>N/A</td><td></td></tr></table>

![](images/65447dce5a254f6a6d56926e60baaab4bae249bfcf09a4eb43056d0ae2bf8df2.jpg)  
For explanation of ratings refer to the stock rating keys located after chart(s)

Valuation Methodology We use EV/EBIT as our primary valuation methodology to derive our TP of HKD14, based on 18x FY26F EV/EBIT. The benchmark index for this stock is Hang Seng Index.
Risks that may impede the achievement of the target price Downside risks: 1) intensifying market competition, 2) slower-than-expected parcel volume growth; 3) weaker-than-expected cost optimization; 4) country-specific regulatory risks

## Important Disclosures

## Online availability of research and conflict-of-interest disclosures

NOM Group research is available on www.NOMnow.com/research, Bloomberg, Capital IQ, Factset, LSEG.

Important disclosures may be read at http://go.NOMnow.com/research/m/Disclosures or requested from NOM Securities International, Inc. If you have any difficulties with the website, please email grpsupport@NOM.com for help.

The analysts responsible for preparing this report have received compensation based upon various factors including the firm's total revenues, a portion of which is generated by Investment Banking activities. Unless otherwise noted, the non-US analysts listed at the front of this report are not registered/qualified as research analysts under FINRA rules, may not be associated persons of NSI, and may not be subject to FINRA Rule 2241 restrictions on communications with covered companies, public appearances, and trading securities held by a research analyst account.

NOM Global Financial Products Inc. (NGFP) NOM Derivative Products Inc. (NDP) and NOM International plc. (NIplc) are registered with the Commodities Futures Trading Commission and the National Futures Association (NFA) as swap dealers. NGFP, NDPI, and NIplc are generally engaged in the trading of swaps and other derivative products, any of which may be the subject of this report.

## Distribution of ratings (NOM Group)

The distribution of all ratings published by NOM Group Global Equity Research is as follows:

58% have been assigned a Buy rating which, for purposes of mandatory disclosures, are classified as a Buy rating; 33% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services\*\* by the NOM Group.

39% have been assigned a Neutral rating which, for purposes of mandatory disclosures, is classified as a Hold rating; 57% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services by the NOM Group

3% have been assigned a Reduce rating which, for purposes of mandatory disclosures, are classified as a Sell rating; 15% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services by the NOM Group.
As at 30 June 2026

\*The NOM Group as defined in the Disclaimer section at the end of this report.

\*\* As defined by the EU Market Abuse Regulation

## Definition of NOM Group's equity research rating system and sectors

The rating system is a relative system, indicating expected performance against a specific benchmark identified for each individual stock, subject to limited management discretion. An analyst's target price is an assessment of the current intrinsic fair value of the stock based on an appropriate valuation methodology determined by the analyst. Valuation methodologies include, but are not limited to, discounted cash flow analysis, expected return on equity and multiple analysis. Analysts may also indicate expected absolute upside/downside relative to the stated target price, defined as (target price - current price)/current price.

## STOCKS

A rating of 'Buy', indicates that the analyst expects the stock to outperform the Benchmark over the next 12 months. A rating of 'Neutral', indicates that the analyst expects the stock to perform in line with the Benchmark over the next 12 months. A rating of 'Reduce', indicates that the analyst expects the stock to underperform the Benchmark over the next 12 months. A rating of 'Suspended', indicates that the rating, target price and estimates have been suspended temporarily to comply with applicable regulations and/or firm policies. Securities and/or companies that are labelled as 'Not rated' or shown as 'No rating' are not in regular research coverage. Investors should not expect continuing or additional information from NOM relating to such securities and/or companies. Benchmarks are as follows: United States/Europe/Asia ex-Japan: please see valuation methodologies for explanations of relevant benchmarks for stocks, which can be accessed at: http://go.NOMnow.com/research/m/Disclosures; Global Emerging Markets (ex-Asia): MSCI Emerging Markets ex-Asia, unless otherwise stated in the valuation methodology; Japan: Russell/NOM Large Cap.

## SECTORS

A 'Bullish' stance, indicates that the analyst expects the sector to outperform the Benchmark during the next 12 months. A 'Neutral' stance, indicates that the analyst expects the sector to perform in line with the Benchmark during the next 12 months. A 'Bearish' stance, indicates that the analyst expects the sector to underperform the Benchmark during the next 12 months. Sectors that are labelled as 'Not rated' or shown as 'N/A' are not assigned ratings. Benchmarks are as follows: United States: S&P 500; Europe: Dow Jones STOXX 600; Global Emerging Markets (ex-Asia): MSCI Emerging Markets ex-Asia. Japan/Asia ex-Japan: Sector ratings are not assigned.

## Target Price

A Target Price, if discussed, indicates the analyst's forecast for the share price with a 12-month time horizon, reflecting in part the analyst's estimates for the company's earnings. The achievement of any target price may be impeded by general market and macroeconomic trends, and by other risks related to the company or the market, and may not occur if the company's earnings differ from estimates.

## Disclaimers

This publication contains material that has been prepared by the NOM Group entity identified on page 1 and, if applicable, with the contributions of one or more NOM Group entities whose employees and their respective affiliations are specified on page 1 or identified elsewhere in this publication. The term "NOM Group" used herein refers to NOM Holdings, Inc. and its affiliates and subsidiaries including: (a) NOM Securities Co., Ltd. ('NSC') Tokyo, Japan, (b) NOM Financial Products Europe GmbH ('NFPE'), Germany, (c) NOM International plc ('NIplc'), UK, (d) NOM Securities International, Inc. ('NSI'), New York, US, (e) NOM International (Hong Kong) Ltd. ('NIHK'), Hong Kong, (f) NOM Financial Investment (Korea) Co., Ltd. ('NFIK'), Korea (Information 

[中间内容因长度限制已省略]

a 'Professional Client' (as defined by the Dubai Financial Services Authority) in the United Arab Emirates ('UAE') or a 'Market Counterparty' or a 'Business Customer' (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar ('Qatar') by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than 'Authorised Persons', 'Exempt Persons' or 'Institutions' located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, "Offshore Issuers") that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
