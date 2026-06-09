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
# India Consumer

EQUITY: CONSUMER RELATED

## 4QFY26 Staples review – on an improving track

Staples: Volumes/Sales/EBITDA grew c.9%/10%/12% y-y; Foods: Volumes/Sales/EBITDA grew 14%/12%/21% y-y; HPC: Volumes/Sales/EBITDA grew 6%/7%/7% y-y

## Common trends across consumer companies

\- Staples revenue improved sequentially to 10.5% y-y in 4Q, above its eight-quarter average of 6.7% (Fig. 9).

Volumes (Fig. 7): While the organized sector's volume growth of $9\%$ in 4Q was the highest-ever over the past four years, FMCG industry volume growth was down sequentially, indicating that the organized players grew faster than unorganized players. We note that almost all the staple companies under our coverage, except for Godrej Consumer, witnessed either sequentially stable or improved volume growth in 4Q, supported by the GST-rate cut.

\- Pricing-led growth (Fig. 8), excluding Marico, which had taken sharp price hikes of $60\%$ in earlier quarters, was in low to mid-single-digits for companies under our coverage and for the FMCG industry. However, with rising input costs led by the West-Asia war, we note that all the companies have started to take calibrated price increases in the mid-single-digits to alleviate the impact.

\- Margins remained range-bound, leading to average EBITDA growth of 11.6% y-y, which was above its eight-quarter average of 4.6% (Fig. 11): GPM for staple companies remained largely range-bound (Fig. 14), as the expansion of food companies was offset by the contraction recorded by Home and Personal Care (HPC) companies. Structural cost savings along with stable ad spending helped to maintain OPM (Fig. 16) for the sector.

\- Foods revenue improved sequentially to $16\%$ y-y in 4Q, above the segment's eight-quarter average of $10.2\%$ (Fig. 19).

Volumes (Fig. 17): The organized sector's sequential improvement in volume growth of $14\%$ in 4Q was largely supported by GST-led price cuts and consequent grammage increases. While the FMCG industry volume growth was down q-q, we note that all the food companies under our coverage recorded sustained volume recovery, with Nestle leading the pack, indicating that organized players outpaced unorganized players.

\- Pricing-led growth (Fig. 18): While the pricing growth in 4Q at $2\%$ was below its past eight-quarter average of $4\%$ , we note that the companies we cover began initiating price hikes of close to the mid-single digits towards the end of the quarter as the West-Asia war led to input cost inflation. Thus, we expect pricing growth to pick up going forward.

\- Margins: GPM for food players improved by 55bp y-y / -15bp q-q (Fig. 24) on the back of lower-priced inventory. Cost efficiency and operating leverage across companies aided OPM expansion by 86bp y-y / 170bp q-q (Fig. 26).

\- HPC revenue growth remained stable at 7.4% y-y in 4Q, above its eight-quarter average of c.5% (Fig. 29).

Volumes (Fig. 27): Organized sector volume growth improved sequentially to 6.3%, double than its past eight-quarter average of 3.2%.

\- Pricing-led growth (Fig. 28): Price cuts by hair oil companies such as Marico ed to a moderation in the pricing growth for the organized sector to $1.1\%$ in 4Q, below its past eight-quarter average of $1.7\%$ .

\- Margins: While GPM contracted 70bp y-y / 40bp q-q (Fig. 34) amid high

Research Analysts

India Consumer Related

Mihir P. Shah - NFASL

mihir.shah1@NOM.com

+91 22 403 74232

Riya Patni - NFASL

riya.patni@NOM.com

+91 22 405 33473

competitive intensity, cost efficiency measures and better operating leverage helped maintain OPM (5bp y-y) (Fig. 36).

## - Rural volume growth moderated on a high base, while urban remained stable:

We note that until 3Q, rural growth grew faster. However, many companies recently indicated that while rural continues to outpace urban growth, the gap between rural and urban is narrowing as rural demand recorded some moderation (Fig. 3), while urban stagnated after evidence of green shoots (Fig. 4).  
- Going forward, we remain watchful on rural demand as we believe that it will likely face multiple headwinds of below-normal monsoon (Fig. 79), El Nino impact, and product price increases being taken by companies due to the West-Asia crisis. However, we believe that strong reservoir levels after two years' of above-normal monsoon and adequate foodgrain stocks could ease some pressure off.

## - Our view:

GST-led benefits to continue supporting volume growth: While staples performed well during 4Q vs 3Q due to GST-led product price cuts along with grammage increases, companies also highlighted an improvement in the demand environment.

## - Pricing growth to support overall growth with no/limited impact on volumes:

Given the input cost inflation caused by the West-Asia war. we note that consumer companies have taken mid-single-digit price hikes. We believe that this price increases and the overall inflation are in manageable ranges and may not materially put pressure on volumes as the staple categories are usually relatively less price elastic.  
- Going forward, we expect a return of pricing growth with no pushback on volumes to drive higher sales growth. However, if pricing growth touches double-digit+, it can start pressuring volumes.

\- Margins could see near-term pressure, but will be made up later: We note that the consumer companies in the past have not fully passed on the inflation cost; hence, we believe that the near-term margins could be impacted.

Organised players are relatively better placed: Inflationary conditions are usually better for organized players as the unorganized players may find it difficult to procure raw materials in case of sustained inflation given they have weaker ability to pass on price hikes.

## Sector tailwinds

- Volume growth to sustain momentum: We expect the sequential recovery of volume growth to continue led by lower prices after the GST rate cuts.  
- Opportunity to gain market share from local players: Amid the prevailing geopolitical conditions, rising input costs and unavailability of raw materials exert pressure on smaller/local players while the organized companies with strong brands, bargaining power and higher saliency of premium portfolio are relatively less impacted, and are gaining share from local players, in our view.  
- Premiumization improves across the board: Multiple companies continued to highlight outperformance by premium segments, indicating a structural mix improvement.  
- Harsher summer likely to be positive for summer portfolios: Given the strong summer, we believe that the companies having exposure to the summer-centric categories such as packaging water, cold coffees, cold drinks, juices, glucose, cooling hair oils, soaps, deos and sunscreens should benefit.  
- Quick commerce channel is growing faster than any other distribution channels as consumers are availing of both: (1) discount offers by the channel for customer adoption; and (2) convenience of 10-minute delivery. We view brands/companies with high market shares and recall them as key beneficiaries currently, as their premium portfolios are witnessing a tailwind from the new distribution channel, and competition from new or regional brands has been limited so far.  
- Noise levels and competition from Direct to Consumer (D2C) brands have moderated further vs in the past few years, as they face challenges in scaling up

## - Quick commerce channel is a tailwind; competition from D2C is easing

their brands beyond the INR2-5bn level and turn profitable/maintain profitability.

While D2C/digital-first brands witnessed a significant surge from 300 brands in 2018 to 11K brands in 2025, only 233 brands have crossed sales of INR1.5bn, with most still not being profitable.

We believe any competition from private labels and online first/quick-commerce brands will be limited, given the overall weakness in demand and pressure on margins that are making the environment less conducive for new products/brand launches.

## Sector headwinds

- El Nino and below-normal monsoon could impact rural agricultural yield this year and add to the pressure on overall demand/consumption. However, we note that the Agricultural Ministry is making district-wise contingency plan to counter any adverse impact and ensure the availability of alternative cropping if conditions deteriorate,  
- Input cost inflation to impact near-term margins: While consumer companies have already effected price hikes given the uptrend in key input costs led by the West-Asia war, we believe it will still be lower than the inflation witnessed by them, causing near-term margin pressure. We also expect companies to continue investing in their brands and new launches, while executing cost saving initiatives to help sustain/improve OPM.  
- Harsher summer can lead to limited movements and impact out-of-home consumption categories.

## Notable mentions

• Colgate (CLGT IN, Buy): Strategic pillars of growth:

- Lead in the toothpaste category through Oral Health Movement and strengthened core brands - Strong Teeth (8.5x more effective) and MaxFresh (fastest-growing);  
- Accelerate premiumization with premium growing 6x faster than toothpaste category (35% mix increase over the past two years) led by Total and Visible White Purple, and Periogard doubling annually;  
Lead in toothbrush by dominating value/mid-tiers (1.7x/1.5x competitors) while expanding super-premium (Brilliant Star whitening) and capitalizing on replacement gap (urban 6 months, rural 15 months vs recommended 3 months);  
- Build personal care via Palmolive body/hand wash (double-digit growth) with digital-first partnerships and innovation pipeline, all underpinned by AI capabilities and product superiority,

• Hindustan Unilever (HUVR IN, Buy)

HUL is revising its go-to-market across channels: Investments to create a specialized force for general trade specialist stores, such as open format stores, chemists, and cosmetic stores. Q-Comm is focused on driving capability building in terms of demand generation, market, supply, availability, to ensure that right capabilities are built – customer availability has gone up c.1,400bp.

• Marico (MRCO IN, Buy)

Marico launched Parachute Advansed Protein Shampoo – INR370 for 340ml – priced lower than Dove Intense Repair at INR490 for a 340ml bottle.  
Growth levers for delivering double-digit consolidated sales growth in the current tough environment: 1) synergies and scale-up of new acquisitions; 2) unique position of softening copra prices (key raw material) in an inflationary environment; 3) tailwinds from higher exposure to fast-growing E-comm channel to increase saliency of Premium Personal Care and Digital First portfolio (we expect to be 44% in FY27F vs 37% in FY26); and 4) sustained performance in the international business.

• Britannia (BRIT IN, Buy)

Industry likely to transition to price parity in 4Q: Our channel checks suggests that Parle (unlisted) has moved to INR5/10 price points (c.65% of BRIT's business) from mid-March; however, we believe that they will have nearly two months of inventory in the channel, and thus the positive impact of this change to

BRIT's numbers will likely be visible from 2QFY27. The dual pricing impacted transactions growth for BRIT in rural from wholesale channels (c.25% of the business); however, BRIT highlighted that the impact should normalize. Given relatively higher realization of the company, the value market share remains similar for the company.

## - Nestle (NEST IN, Buy)

Nestle is benefiting from a confluence of external and internal factors. Apart from GST rate cut benefits, external factors like low inflation and benign input costs negated the need for price hikes, which in turn drove volumes. Internal factors yielding results, in our view, include: 1) a rise in its distribution reach by continued expansion through route-to-market strategy (the highest numeric increase last year; current reach: c.216k villages) while improving coverage effectiveness; 2) omni-channel strategy of scaling ecomm/q-comm with platform-specific pack portfolio being created across categories, strengthening modern trade and chain pharmacy and sustaining growth via general trade – this led to strong double-digit growth across business channels; 3) improving in-stock availability and tech-enabled replenishment to cut lead time and sharpen channel-wise assortment; and 4) stepping up value-added new product launches and brand building initiatives indicated by a material step-up in ad spends (50%+/42%+ y-y in 4Q/3Q) which augurs well for future volumes, in our view.

## • EPL (EPLL IN, Buy)

Oral care on the path to recovery while Beauty & Cosmetics sustained strong growth momentum.  
Middle-East crisis driving higher raw material cost, but EPL says it will maintain margins: Management is confident in leveraging its strong supplier relationships and operational scale, and indicated that it has supplies secured until mid-July and is expanding its inventory weekly. The company's advanced cost pass-through model (c.50% of business) through contractual agreements (being reviewed proactively) that include landed costs, power, logistics, and currency enables recovery of all additional costs without significant lag, even from non-contractual customers while creating market share opportunities as competitors face supply constraints.

## • GCPL (GCPL IN, Buy)

Palm oil inflation, not as alarming as perceived: GCPL is witnessing 7-9% cost inflation (with crude at USD100-110/bbl and palm oil at MYR4,500-4,800), and took a 5% price hike in soaps and 1HFY27, and 7% in detergents in April, which will lift FY27F consolidated sales growth to double-digits / low teens, in our view.  
Opportunity to gain market share: The entry of domestic competitors in 1H and laundry likely facing high cost / sourcing issues for kerosene / linear alkyl benzene (LAB) could benefit GCPL in terms of share gains.  
- Indonesia continued to improve as pricing pressure bottomed out:

Management expects a meaningful step-up in performance from FY27E, targeting mid-single digit volume and high-single-digit value growth, as operating conditions normalize.

## Company guidance / forward-looking comments and our view

## - Britannia Industries (BRIT IN) (Buy) – 4Q headwinds getting addressed; expect normalization during 1QFY27

- BRIT expects the dual pricing-led impact on transaction growth to normalize as the remaining players transition to coinage price points of INR5/INR10.  
- Our view: We expect price hikes from competition (undertaken in March) to establish price parity in the industry and drive sequential improvement going forward.

## • Dabur India (DABUR IN) (Buy) – Every storm runs out of rain

Dabur expects price hikes to drive double-digit sales growth vs earlier guidance of high-single-digit growth. Management emphasised its strategic intent to prioritize and maintain India margins y-y on the back of price hikes, mix improvement, and cost savings, while continuing to monitor international margins given the geopolitical headwinds.

For FY27E: the company expects HPC to sustain double-digit growth in FY27E and Foods and Beverages (F&B) to deliver double-digit growth, supported by increasing focus shift towards Real Activ, albeit contingent on El Nino.  
Our view: We expect price hikes to drive a sequential improvement to near-double-digit sales growth as we believe that the probability of a harsher summer may support a recovery of Beverages after being impacted for the past 12 quarters.

\- Godrej Consumer Products (GCPL IN) (Buy) – Near-term hiccup, but on a structural upswing

FY27E:

While 1Q/2Q FY27E margins will likely see some pressure and be marginally below normative levels of 24-26%, GCPL expects higher revenue/pricing growth to off

[中间内容因长度限制已省略]

ingdom of Saudi Arabia (‘Saudi Arabia’) or a ‘Market Counterparty’ or a ‘Professional Client’ (as defined by the Dubai Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM Financial Advisory and Securities (India) Private Limited, India. All rights reserved.
"""
