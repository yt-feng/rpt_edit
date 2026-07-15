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
## The Rise of the RMB Financing Ecosystem From Panda and Dim Sum Bonds to Deeper Capital Markets

Perry Kojodjojo
Perry.Kojodjojo@db.com

Chen Kan
Chen.Kan@db.com

13 July 2026

\- Explicit policy shift to accelerate internationalization. China's 15th Five-Year Plan (2026-30) explicitly elevates RMB internationalization to a strategic priority, departing from its previous cautious approach. This acceleration is evident in early 2026 actions like cutting FX risk reserves and expanding Southbound Bond Connect, boosting liquidity and market access. Supported by Hong Kong, these moves signal a clear, high-level commitment to the RMB's global role.

\- Diverging and complementary market roles. The Panda and Dim Sum bond markets are evolving into a dual-engine system. The Panda market serves as a funding channel for foreign entities to raise globally usable RMB, with proceeds now flexibly remittable offshore. Conversely, the offshore Dim Sum market is solidifying its position as the core asset hub for international investors, fueled by asset diversification and rising mainland demand.

\- Panda market maturation into a strategic tool. The Panda market's recent 60% YoY growth is now structurally driven, not just by cost. Over half of proceeds are used offshore, confirming its value as a global RMB source. However, its strategic potential is constrained by a short-term focus (mostly sub-3-year issuance) and continued dominance by financial sector borrowers.

\- Dim Sum market diversification and sophistication. The Dim Sum market is rapidly maturing as a sophisticated offshore hub. Its significant diversification includes foreign issuers exceeding 25%, a shift from real estate to tech in domestic issuance, and a trend towards longer-dated debt. This reflects growing investor confidence, bolstered by new mainland demand via Southbound Bond Connect.

\- Next frontier - a focus on building a complete financial ecosystem. The next phase of RMB internationalization shifts beyond bond issuance growth to building robust financial infrastructure. The primary challenge is matching offshore RMB supply with deep secondary market liquidity, reliable benchmark yield curves for price discovery, and comprehensive risk management tools. Long-term success hinges on creating this complete, liquid ecosystem.

\- A deeper offshore RMB financial market. RMB internationalization will deepen CNH rates, funding, and FX markets. A more robust CNH government bond market will establish benchmark yield curves, while active IRS, CCS, and FX swap markets will enhance hedging, funding efficiency, and price discovery.

\- Expanding European participation in RMB funding markets. While European entities dominate foreign issuance in both Panda and Dim Sum markets, this participation is highly concentrated among a few financial sector repeat borrowers, with corporates largely absent. Barriers include smaller deal sizes, a narrower investor base, and lack of market familiarity. As RMB internationalization progresses, we anticipate broader international issuer participation, particularly from European corporates given strengthening EU-China ties.

Jan 2018: PBoC clarified that enterprises may settle any cross-border transactions in RMB that can be legally settled in foreign exchange.

May 2018: The daily quota of Stock Connect quadrupled, with Northbound trading increasing from (RMB13bn to 52bn) and Southbound trading from RMB10.5bn to 42bn.

## Jun 2018:

\- China A-shares were first included in the MSCI Emerging Markets Index.

\- The monthly 20% repatriation limit imposed under the QFII scheme was removed

\- The three-month capital lock-up period for QFII and RQFII redemptions was removed

\- QFIIs and RQFIIs were allowed to hedge currency risks deriving from their onshore investments

The PBoC announced that all overseas RMB clearing and settlement banks that participate in CIBM can conduct repo and move the funds abroad

\- QFII can choose currencies and the timing of inward remittance on their own decisions

\- The procedures for QFIIs' repatriation of securities investment income are significantly simplified

\- The limits on the number of custodians are scrapped

Sep 2020: CSRC, PBC and SAFE revised the rules for QFII and RQFII, including:

\- Relaxing qualification requirements and facilitating investment and operations of QFIIs and RQFIIs

\- Separate regimes for QFII and RQFII qualifications and rules are integrated

\- The restriction on the number of intermediaries servicing a QFII or RQFII is removed

## Feb 2024:

\- CGBs and PBBs were accepted as collaterals for HKMA's RMB Liquidity Facility

\- Overseas investors that have engaged in cash bond transactions in the CIBM can conduct bond repo transactions in the CIBM

Northbound bond connect was established

\- PBoC cut the FX risk reserve requirement on forward sales to 0%.

## Apr 2026:

\- QFIIs and RQFIIs were allowed to invest in stock options, commodity futures and participate in bond repo and margin trading.

## Jun 2026:

\- PBoC will establish a FIMA repo facility, allowing foreign central banks and other official institutions to access RMB liquidity

![](images/8f280403808e190515c9c9f67ec56a1d47569e58aa88d56292b1a2302f6c347f.jpg)

## Jul 2026:

\- Southbound Bond Connect annual quota was increased from RMB500 to 800bn
- HKMA to support next stage of RMB internationalization through (1) boosting CNH liquidity by increasing quota for RMB liquidity facility; (2) deepening RMB infrastructure, such as issuing RMB debt, launching CGB futures in HK, developing a fixed-income trading platform; (3) promoting connectivity with onshore markets, like enhancing Swap Connect

May 2023: Northbound Swap Connect was launched Jun 2023: HKD-RMB Dual Counter Model was launched for trading and settlement in secondary market.

Jan 2025: CGBs and PBBs held through Bond Connect can be used as collateral for Northbound Swap Connect

Feb 2025: HKMA RMB Trade Financing Liquidity Facility was launched to support banks' RMB trade finance services

Sep 2025: HKMA enhanced the CNH liquidity by:

\- lowering the funding cost

\- expanding the scope of eligible activities and the tenor of the funding

\- allocating more quota to intraday RMB funding

Oct 2025: All foreign institutions eligible for spot bond trading in the onshore market are allowed to conduct onshore bond repos

Policy stance has shifted from cautious to explicit. China's 15th Five-Year Plan (2026-30) elevates RMB internationalization to a strategic priority, removing the previous "cautious" language. This policy shift is backed by a rapid and concrete sequence of actions in early 2026 amid a global de-dollarisation trend.

The PBoC has moved to boost liquidity and ease controls by cutting FX risk reserve requirements, unifying lending quotas, and raising loan leverage ratios to support the Panda bond market. It also established a FIMA repo facility for foreign central banks and significantly expanded the

Southbound Bond Connect, increasing its quota to RMB 800bn while extending its scope to Macau and HKD-denominated assets.

Concurrently, Hong Kong authorities are actively supporting this push by increasing their RMB liquidity facility to RMB500bn, extending its tenure, launching CGB futures, and enabling direct RMB-IDR trading.

Progress is uneven. While official commitment to RMB internationalization is strong—evidenced by record transaction volumes on China's CIPS payment system—progress remains uneven. RMB settlement in China's goods trade has surged from 13% (2019) to a projected 30% by 2025. However, the currency's broader global footprint is modest, holding only a \~1-4% share across global payments, FX reserves, and debt securities. This is disproportionately low compared to China's \~19% share of global GDP, highlighting significant room for growth, particularly in the RMB's role as a global financing currency.

The center of gravity has moved from trade to investment flows. The nature of cross-border RMB usage has fundamentally changed. While total transaction volume has surged to RMB 70tn, the critical story is the shift in composition. Capital and financial account transactions now constitute \~75% of total RMB settlements, marking a decisive move from trade to investment as the main engine.

This shift means the next phase requires a deeper financial ecosystem. The focus must be on creating more robust channels for both raising and deploying RMB capital. This includes: easier access to RMB funding through both onshore (Panda bonds) and offshore (Dim Sum bonds) markets, more sophisticated hedging tools, and a broader array of attractive RMB-denominated assets for global portfolios (such as offshore Dim Sum bonds).

USD's declining share of reserves points to ongoing de-dollarization  
![](images/1a7e6660f97a7c31b11d2745da98025a79899695b0567a72243b91423d06ddf2.jpg)

RMB transactions through CIPS hit a record high  
![](images/721c591e0b6b3307d7c869b79a7b39acce6d19f0ba65c8a3f124cc250f50fb6a.jpg)

A more active use of RMB in trade settlement  
![](images/4ae33f45aef679ade2796afdacb3dc8fd8ebc73025fcfff225c9263987c4df30.jpg)

RMB-denominated debt issuance has risen notably particularly as China pushes to develop the Panda and Dim Sum Bond markets  
![](images/7c624728108a6e2e47c393408f63a02da6a667b1fcc0e3cbffe26ec5c70e9605.jpg)

Since our 2025 primers on the Dim Sum and Panda bond markets, the two have entered a new, more dynamic chapter. The pace of change has accelerated, and the characteristics of each market are beginning to diverge in important ways. How so?

First, by accelerating on different tracks. The onshore Panda bond market is experiencing a record year, with issuance surging. In the first half of 2026 alone, volume exceeded RMB 160bn, marking an annual growth rate of over 60%. This boom is driven by more than just low financing costs; it is a direct result of fundamental improvements to the market's architecture.

Streamlined issuance procedures—such as unified regulatory oversight and shelf registration frameworks—have made the process feel more like a mainstream funding market. Crucially, more flexible fund rules allowing issuers to remit proceeds overseas without many operational hurdles, transforming Panda bonds from a ring-fenced pot of onshore currency into globally usable RMB funding. This flexibility, combined with a clear upward trend in gross issuance, signals a new stage of maturity for the market.

In contrast, the offshore Dim Sum market's strong growth is driven by diversification. This market is poised for a significant boost not only as mainland insurers gain access via the Southbound Bond Connect but also the expansion of the quota to RMB800bn from RMB500bn, creating a new source of demand for an issuer base that is increasingly foreign-led.

Second, by developing distinctly different market "DNA". While both markets are crucial for RMB internationalization, they are evolving with unique characteristics:

Issuer base - Panda stays traditional while Dim Sum embraces Tech. The Panda market remains dominated by financials and other traditional sectors. The Dim Sum market, however, shows a clear trend of diversification. Issuance from the IT sector has risen sharply, a visible and growing slice of the market that is almost non-existent in the Panda space. This surge is driven by a perfect storm of factors: Chinese tech giants are seeking cheap, long-tenor CNH funding to finance their massive AI and cloud capex cycles. The Dim Sum market meets this need, offering low borrowing costs and longer durations that match their investment horizons, all while tapping into strong investor appetite for high-grade CNH credit.

Duration profile. Panda stays short, Dim Sum extends. The markets operate on different time horizons. The Panda market is overwhelmingly short-term, with nearly all issuance YTD having a tenor of 3 years or less. This is not due to regulatory caps, but rather a reflection of the onshore market's structure: demand is concentrated at the front end, dominated by banks managing short-term assets. With a historically flat yield curve offering little extra yield (term premium) to go further out, there has been limited incentive for issuers to offer or investors to buy longer-dated paper.

The Dim Sum market, conversely, is showing clear signs of maturity with a discernible trend towards longer-dated issuance, with a significant and growing share of bonds in the 5-year and longer tenors.

Steady growth in the Dim Sum bond market poised to deepen

![](images/b7a69e3fd3ef5135dd1639de0f81593d00ef4cbb6f35843fd0bc76c9a9902518.jpg)

Policy easing unlocks new growth phase in the Panda bond market  
![](images/17089124cc8033cd2a60dd8313132c3d694c60ac89930d2d8ac894e832f0d67f.jpg)

Becoming the Go-To offshore RMB hub not just for government entities but also corporates  
![](images/a73c14f44158065508b839cf2e655c5a205d8804fce0021d73c5b52bbb837dfb.jpg)

A hybrid market set to attract more foreign issuers  
![](images/16035bc373eb32bc61fa08943ad9145b9120cef29d866a1ff9c6a2715fd4f56c.jpg)  
Source: DB, Bloomberg Finance LP, CEIC, Haver, Wind

Internationalization deepens as foreign issuers gain dominance

![](images/f8cdacdb6807dea97b43806ac8b203ee47c834ab6d7c9c1b2dd5c5ff1aec6b47.jpg)  
Dim Sum diversifies into Tech, signalling a shift to new-economy funding

Financials pave the way, laying the foundation for broader corporate use  
![](images/e8bc150714c9cb0300536dfddf175b9c1945bb0e69c55f45298160c95556d6b8.jpg)

![](images/f2fec6446e596f72e5a50028718e416f5732a9cf72b8f917721a61ace7a311ad.jpg)  
■Financials ■Industrials ■Consumer Staples ■Information Technology ■Utilities ■Others

Dim Sum matures with longer tenors as Panda stays short-term focused  
![](images/a392d18867be63ee15fef0486d568c60ba16642326427d95f15f705a8296de45.jpg)

The Panda bond market is showing clear signs of maturation, with net issuance remaining resiliently positive even as financing cost advantage narrows. This indicates the market views the Panda bond market increasingly as a strategic funding tool. This shift is driven by structural improvements on both the supply and demand side. On the supply side, three key trends are evident:

\- Broadening foreign participation. Foreign issuers have become a cornerstone of the market, consistently accounting for over 30% of issuance from less than 10% a decade ago. While financial institutions remain the core issuer base, the market is gradually diversifying.

\- Rising offshore usage. Issuers are increasingly using Panda bonds for offshore funding. The proportion of proceeds repatriated for offshore use has climbed to $53\%$ in 2026 YTD, a notable increase from the sub- $40\%$ levels seen previously. This is a direct result of regulatory easing that has transformed Panda bonds from a ring-fenced onshore tool into flexible, globally usable RMB funding.

\- Persistent short-term focus. The market remains heavily concentrated in shorter tenors, with issuances of 3 years or less making up the vast majority of activity. This reflects an onshore investor base that is still predominantly focused on the front end of the curve.

On the demand side, domestic banks continue to be the primary absorbers of new issuance. However, a positive sign for market depth is the modest return of foreign buying this year, reversing the net selling seen in 2025.

Issuance remains resilient as market moves beyond cost saving

![](images/8dbc827af955689583331b33a156cf535bbb76b515b9708d853e2b2f436a090a.jpg)  
Foreign participation becomes a cornerstone of the market

![](images/ba131d044ab63712b43001634933018386c0592820ab6a2bf65c78e3fb3fbc7a.jpg)  
Source: DB, Bloomberg Finance LP, CEIC, Haver, Wind

Onshore Offshore Others % of proceed repatriated offshore (RHS

[中间内容因长度限制已省略]

usiness in the DIFC: Dubai International Financial Centre, The Gate Village, Building 5, PO Box 504902, Dubai, U.A.E. This information has been distributed by DB AG. Related financial products or services are available only to Professional Clients, as defined by the Dubai Financial Services Authority.

Australia and New Zealand: This research is intended only for "wholesale clients" within the meaning of the Australian Corporations Act and New Zealand Financial Advisors Act, respectively. Please refer to Australian specific research disclosures and related information at https://www.dbresearch.com/PROD/RPS\_EN-PROD/PROD000000000521304.xhtml. Where research refers to any particular financial product recipients of the research should consider any product disclosure statement, prospectus or other applicable disclosure document before making any decision about whether to acquire the product. In preparing this report, the primary analyst or an individual who assisted in the preparation of this report has likely been in contact with the company that is the subject of this research for confirmation/clarification of data, facts, statements, permission to use company-sourced material in the report, and/or site-visit attendance. Without prior approval from Research Management, analysts may not accept from current or potential Banking clients the costs of travel, accommodations, or other expenses incurred by analysts attending site visits, conferences, social events, and the like. Similarly, without prior approval from Research Management and Anti-Bribery and Corruption ("ABC") team, analysts may not accept perks or other items of value for their personal use from issuers they cover.

Additional information relative to securities, other financial products or issuers discussed in this report is available upon request. This report may not be reproduced, distributed or published without DB's prior written consent.

Backtested, hypothetical or simulated performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG.

It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG
"""
