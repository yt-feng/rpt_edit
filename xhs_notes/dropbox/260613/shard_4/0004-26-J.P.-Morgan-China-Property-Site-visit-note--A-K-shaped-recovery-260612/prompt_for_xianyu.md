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
## China Property

Site visit note: A K-shaped recovery

Our property trip to Shenzhen and Shanghai last week revealed that the local housing markets are stabilizing in a K-shape. Luxury property sales are robust on the back of strong demand. Transaction volume for entry-level units has recovered, but the midrange segment remains soft. While China Property's recovery remains city-/segment-specific, we selectively prefer developers with IP transformation stories and credits with decent valuations. We stay OW on: (1) the Longfor curve (9-10%) due to its solid debt servicing ability; and (2) SHUION '29s (9%), as they are a proxy for Shanghai's luxury market recovery with declining maturities. Seazen has managed to handle refinancing so far, but we stay Neutral on the '28s, as we find valuation fair after the compression from a 19% yield to 13% YTD.

- Shenzhen housing market stabilizing in a K-shape: A Shenzhen property expert we met noted that the city's secondary housing market has stabilized in pricing/volume on the back of policy easing in 1H26. Nevertheless, there is a clear differentiation across pricing tiers and districts. Luxury home sales are robust, and entry-level transactions have recovered, but the midrange segment remains weak. Nanshan and Futian have outperformed, but other districts are softer. Primary sales are driven by premium projects, and affordable/entry-level unit transactions are shifting to the secondary market. The expert believes Shenzhen's large-scale rollout of affordable housing may weigh on the mass market's recovery in the next few years.  
- Polarization seen on the ground: Our channel checks in Shenzhen/Shanghai largely confirmed the expert's views. Luxury homes (>Rmb20mn) see robust sales on the back of limited supply and strong demand from young tech elites (a positive wealth effect from the AI/robotics boom). However, mass-market buyers remain price-sensitive due to concerns about job security, the wage outlook, etc. The IP projects we visited showed divergent performance, as well. While premium malls are solid on the back of property market stabilization/strong equity markets, mass-market malls diverge subject to their location, tenant mix, operating strategies, etc.  
- Seazen: IP transformation and REIT as new funding channel: Seazen aims to clear a majority of its DP inventories in three years, with no land acquisition plans in the near term. Management believes the retail market in tier-3/4 cities is more stable and less competitive, and it targets steady IP earnings growth with a focus on long-term competitiveness. Seazen sees Wanda as the key competitor in low-tier cities and noted limited competition from CR Mixc for now. It has managed to refinance maturities so far, thanks partly to a higher LTV for IP-backed loans, and it is exploring REIT as a new funding channel.  
- Stay selective, prefer Longfor curve and SHUION '29s: We are OW on the LNGFOR curve and SHUION '29s at a $>9\%$ yield. We appreciate: (1) Longfor's solid debt servicing ability (Rmb17bn accessible cash + Rmb5bn-10bn annual FCF vs. Rmb6bn-7bn annual maturities); and (2) Shui On as a proxy for Shanghai's luxury market recovery with declining maturities. Seazen has managed to refinance maturities, but we find the '28s fair at a $13\%$ yield.

## Asia Pacific Credit Research

Alvin Au AC

(852) 2800-8533

alvin.au@JPM.com

Soo Chong Lim

(852) 2800-7387

soochong.lim@JPM.com

JPM Securities (Asia Pacific) Limited

## Highlights from experts and companies

## Expert meeting with Director of Centraline Property Agency (Shenzhen)

- Stabilizing secondary pricing and volume: The average price for secondary homes in Shenzhen has dropped 43% from the 2020 peak, to Rmb46,103/sqm. However, it has recovered by >2% since Jan-26, indicating a price bottom. Transaction volume in the secondary market bottomed last year. It reached 56K units in 2025 (+3.2% yoy) and 31K in 5M26 (+4.5% yoy). Secondary transactions have outpaced primary home sales (38K/15K units in 2025/5M26, -21%/-21% yoy).  
- Driven by policy relaxation: There were three rounds of policy relaxation in 1H26: (1) VAT reduction on secondary home sales (lowered from 5% to 3% for units held for <2 years; full exemption after 2 years); (2) the downpayment for commercial properties lowered to 30%; and (3) the relaxation of home purchase restrictions (HPR) in core districts (SZ/non-SZ residents allowed to buy one extra unit) with a higher home provident fund loan limit. These policies have triggered a surge in total property transactions to >10K units in May (a 14-month high).  
- K-shaped recovery: Luxury homes (>Rmb20mn) see strong demand and robust sales on the back of tech elites and a positive wealth effect from the AI/robotics boom. Transactions for entry-level homes (\~Rmb3mn) have recovered after a sharp price drop over the past five years. The midrange segment (Rmb5bn-10mn) is under pressure, with the weakest performance. By district, Nanshan and Futian are the best performers in Shenzhen.  
- Shrinking primary market and land supply: Primary launches have declined for three consecutive years, with only 9,600 units launched in Shenzhen in 5M26 (-23% yoy). Land auctions have also slowed dramatically, with only three plots sold in 2026 YTD, leading to a product skew toward high-margin high-end products. National policies prohibit local governments from supplying new land if primary inventory months are above 10 (Shenzhen: 13.7). Land supply cannot improve materially if inventory months do not come down.  
- Primary vs. secondary market: Transactions are shifting toward the secondary market due to declining primary launches and new land supply. For the primary market, luxury/premium projects are driving sales. For the secondary market, affordable and entry-level homes dominate transactions.  
- Mass-market recovery weighed on by large-scale rollout of affordable housing: Shenzhen will roll out 200K-300K units of affordable housing over 2026E-30E. Affordable housing is priced at 50-70% of comparable commodity housing, and the large supply will weigh on pricing in the low-/mid-tier segment. Shenzhen rolled out 43K units of affordable housing in 2025, which is 1.2x new commodity housing supply (35K).  
- Stringent risk management: Shenzhen has no unfinished buildings since 2022, and $42\%$ of property transactions are on completed projects. Stricter escrow rules have also reduced unfinished building risk. Vanke's Shenzhen projects are now co-managed by SOEs (e.g., Shenzhen Metro). It has therefore maintained a decent sell-through rate and price stability for its projects.

## Company meeting with Seazen Holdings

\- Targets clearing most DP inventories in three years: Seazen is actively contracting the DP business with a focus on reducing inventories and debts. Current DP inventory stands at Rmb71bn. This includes: (1) Rmb2.6bn of undeveloped land (拟开发土地); (2) Rmb45.6bn of projects under construction (在建项目); and (3) Rmb22.9bn of completed, but unsettled/transferred projects (竣工未结转). There are also Rmb30bn of construction payables and Rmb10bn of tax payables. Sales are stable at Rmb1bn/month, mainly from existing projects with minimal new launches, and the developer targets clearing most DP inventories in three years, partly by repaying debt/payables with existing inventories. It has maintained a DP team, but has shifted its focus toward third-party construction service. Seazen has no land acquisition plan in 2026, but may participate in select opportunities in the future.

\- Investment Property a solid cash cow: Seazen's IP business is solid, with commercial operation revenue (rental income + property management fee) growing 3% yoy, to Rmb4.7bn in 4M26, on the back of a 7%/10% increase in tenant sales/foot traffic over the period. Compared to tier-1/2 cities, Seazen believes the consumption market in low-tier cities is: (1) more stable (family-centric, less policy-sensitive); and (2) less competitive (Wanda as the major competitor). Seazen is ramping up investments to improve mall quality and tenant mix, and is increasing the adoption of the fixed + turnover rent model to improve rental income (mostly fixed rent contracts now). It targets Rmb14.5bn in commercial operation revenue in 2026 (+4% yoy, 70%/50% gross/net margin), which more than covers its SG&A expenses (Rmb4bn), interest payments (Rmb3bn) and taxes (Rmb3bn).

\- Clear positioning to defend against competition from Wanda and CR Mixc: Seazen sees Wanda as the major IP competitor in tier-3/4 cities. Compared to Wanda, Seazen believes it has a better long-term strategy to cultivate mall competitiveness and shopping experience, instead of being focused on near-term profits for liquidity. Seazen sees a clear difference in positioning among IP players, which include CR Mixc (premium), Longfor (midrange focus in tier-1/2 cities) and Seazen (mass-focused on tier-3/4 cities). CR Mixc's expansion to lower-tier cities could be a potential challenge to Seazen, but management believes the former's near-term expansion would be constrained by heavy funding needs for mall buildup. Seazen can reposition its malls toward the mass market even in the face of CR Mixc's competition in certain cities, as well.

\- Higher LTV for IP-backed loans: Offshore debts are mainly in USD bonds (Rmb5bn-equivalent outstanding), and onshore debts are mainly in Wuyue Plaza-backed operating loans. Seazen has raised LTV for the IP-backed loans from 38% (2024) to 43% (2025), and recent new borrowings are made at 50% LTV. There are only Rmb2bn of remaining development loans due to a lack of new projects.

\- REIT the new financing channel: Seazen has launched a private REIT backed by Shanghai's Qingpu Wuyue Plaza. It owns 34% of the REIT (consolidated) and has raised Rmb400mn by disposing 66% of the mall (5-6% expected return, based on rental income). It has raised Rmb420mn of bank loans and Rmb400mn of equity funds from the Qingpu mall in total. Seazen will launch another private REIT project this year, and it aims to launch a public REIT with a Rmb2bn issuance later in 2026. It believes the REIT channel helps: (1) marginally improve liquidity; and (2) improve debt structure (replace debt with equity) on the back of Rmb120bn of IP assets.

## Site visits in Shenzhen and Shanghai

## Shenzhen

- Premium residential project: We visited Marivista (观潮), a high-end residential project in Bao'an Xin'an Street near Qianhai that is co-developed by CR Land and China Merchants Shekou. With pricing at Rmb140K-150K/sqm with a lump sum of Rmb20mn-100mn, sales are robust and every new batch launched is sold out in a few minutes, per the sales manager. Buyers are mainly Shenzhen locals (non-locals are restricted by home purchase restrictions) aged 30-40 working in industries such as tech, finance, AI/semiconductors, etc. These young elites have amassed wealth in recent years, and some of the sales manager's customers earn Rmb100mn per year. Buyers pay a 15-20% downpayment, and most borrow mortgages at a \~3% cost.  
- NWD K11 ECOAST: We visited New World's K11 ECOAST shopping mall in Nanshan, which opened in April 2025. Occupancy was decent, at $80 - 90\%$ (no disclosure on rents), but foot traffic was weak on Wednesday at lunch time. The tenant mix was broad across EV (Tesla, Nio), F&B, game stores, bicycle rental shops and artwork shops, and the seafront coffee shop was relatively popular. There are new office buildings under construction nearby, which could be positive for foot traffic in the future.

## Shanghai

- Premium residential projects: We visited: (1) COLI's Anlan Shanghai (安澜上海), a high-end residential/commercial complex in Xuhui CBD district; and (2) Shui On's premium Riverville (翠湖滨江) villa project in Yangpu district. Both projects price Rmb20mn to >Rmb100mn in lump sum per unit. Similar to Shenzhen, sales are fast, and the two projects we visited are nearly fully sold. Buyers are mainly Shanghai locals or from the nearby Yangtze River Delta, aged 30-40. There will be a lot of new office supply in the Xuhui CBD district in the next few years. Besides the commercial complex we visited, Hongkong Land will also complete the Westbund Central project in that area by 2028E.  
- IP: We visited Hang Lung's Plaza 66, a high-end luxury mall in Jing'an district, and Longfor's Paradisewalk shopping mall in Minhang, Shanghai.  
- Hang Lung Plaza 66 (恒隆广场): The mall enjoys unique positioning, with a high concentration of luxury brands in the city center area. Tenant sales were strong, at >10% yoy in 1Q26, driven partly by the promotion event of a major tenant in 1Q. The sales manager noted that the national tax refund policy for tourist purchases is supportive of foot traffic, but the impact on sales is limited. She also observed increased visitors from Korea, Taiwan (which benefited from the AI boom) and the Middle East.  
- Longfor Minghang Paradisewalk (龙湖闵行天街): Foot traffic was decent on a Thursday afternoon, and key tenants include fashion wear/sportswear (CK Jeans, North Face), F&B and consumer electronics (e.g., Xiaomi, Huawei). The sales manager noted that the mall targets business, family and students as customers, and sees Wanda as the key competitor in the region. She believes Wanda is more focused on near-term profits, but the mall focuses on cultivating a decent shopping experience with an optimal tenant mix.

Figure 1: Strong sell-through at Marivista (观潮) in Bao'an, Shenzhen  
![](images/e9bb8d995f1a60579527e8172a76a17bb77c02e19993d38342e9d743651e13ba.jpg)

<details>
<summary>text_image</summary>

深圳观潮房源销控表
MARIVISTA
深圳观潮房源销控表
MARIVISTA
模板
1栋三单元
楼栋
1栋五单元
建筑面积(m²)
536.6m²
建筑面积(m²)
503.46m²
25F
250
24F
2401
257.94m² 257.94m²
257.94m² 257.94m²
257.94m² 257.94m²
257.94m² 257.94m²
257.94m² 257.94m²
257.94m² 257.94m²
257.94m²
257.94m² 257.94m²
257.94m² 257.94m²
257.94m² 257.94m²
257.94m² 257.94m²
257.94m² 257.94m²
Mangzhou ◆ Marivista
模板
1栋六单元
1栋七单元
建筑面积(m²)
189.23m² 188.26m² 188.26m²
169.61m² 169.61m² 169.61m²
169.61m² 169.61m² 169.61m²
169.61m² 169.61m² 169.61m²
169.61m² 169.61m² 169.61m²
169.61m² 169.61n² 169.61n² 169.61n²
20F 已售 已售 已售 已售 已售 已售 已售
20F 已售 已售 已售 已售 已售 已售 已售
20F 已售 已售 已售 已售 已售 已售 已售
20F 已售 已售 已售 已售 已售 已售 已售 已售
20F 已售 已售 已售 已售 已售 已售 已售 已售
20F 已售 已售 已售 已售 已售 已售 已售 已售
20F 已售 已售 已售 已售 已售 已售工已售
20F 已售 已售 已售 已售 已售 已售 已售 已售
19F 已售 已售 18F 已售 已售 18F 已售 已售 18F 已售 已售 18F 已售
19F 已售 已售 17F 已售 已售 17F 已售 已售 17F 已售 已售 17F 已售
17F 已售 已售 16F 已售 已售 16F 已售 已售 16F 已售
16F 已售 已售 15F 已售 已售 15F 已售 已售 15F 已售
15F 已售 已售 14F 已售 已售 14F 已售 已售 14F 已售
14F 已售 已售 13F 已售 已售 13F 已售 已售 13F 已售
13F 已售 已售 12F 已售 已售 12F 已售 已售 12F 已售
12F 已售 已售 11F 已售 已售 11F 已售 已售 11F 巳告
11F 巳告 巳告 10F 巳告 巳告 10F 巳告 巳告 10F 巳告
10F 巳告 空间样板面积 SF
SF 巳告 空间样板面积 SF
SF 巳告 空间样板面积 SF
SF 巳告 空间样板面积 SF
SF 巳告 空间样板面积 SF
SF 巳告 空间样板面积 SF
SF 巳告 空间样板面积 SF
SF 巳告 空间样板面积 SF
SF 巳告 空间样板面积 SF
SF 巳告 智格样板面积 SF
SF 巳告 智格样板面积 SF
SF 巳告 智格样板面积 SF
SF 巳告 智格样板面积 SF
SF 巳告 智格样板面积 SF
SF 巳告 智格样板面积 SF
SF 巳告 智格样板面积 SF
SF 巳告 智格样板面积 SF
SF 巳告 智格样板面积 SF
</details>

Source: JPM. Note: 已售 = sold.

Figure 2: Neighborhood and school network near Marivista (观潮) in Bao'an, Shenzhen  
![](images/7ecd31fc52de120d84656950c9403985276a61ec783f32c1f181af622ad50128.jpg)

<details>
<summary>text_image</summary>

西安云游集团海洋学校
西安中宇集团海洋学校
</details>

Source: JPM.

Figure 3: NWD's K11 ECOAST shopping mall in Nanshan, Shenzhen  
![](images/b3344097613c56977fccedde292ce5a25d2e839cba9d8cd23a87617fa005659b.jpg)

<details>
<summary>text_image</summary>

QQ音乐
K11
价值超·500游客礼遇
免费领
New Flavor!
MAKE IT LEMONADE
</details>

Source: JPM.

Figure 4: NWD's K11 ECOAST shopping mall in Nanshan, Shenzhen  
![](images/3e2fa156eebe59168168bb4b78aee370380e3ef0405dba837e1ccf936f5956bc.jpg)

<details>
<summary>natural_image</summary>

Interior view of a modern luxury shopping mall with a large

[中间内容因长度限制已省略]

rmance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 11 Jun 2026 11:43 PM HKT

Disseminated 12 Jun 2026 07:30 AM HKT
"""
