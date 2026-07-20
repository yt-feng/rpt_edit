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
AUSTRALIA METALS & MINING: GOLD

# GMD merger appears accretive vs. baseline ASPIRE 500 and VAU outlooks; Reinstate GMD at Buy, RRL at Neutral

Following GMD's 6-Jul proposal, and RRL electing not to match the offer, GMD and VAU have agreed to merge via a Scheme of Arrangement, with implementation targeted Oct/Nov-26. GMD reaffirmed the strategic rationale, though a strategic review and new plan is targeted for 1H CY27 to better outline a combined outlook, including production uplifts/LoM extensions, capex savings, mine plan optimisations, and potential non-core divestments. GMD noted they will also provide some FY27 guidance with the upcoming quarterly result.

We conduct an illustrative scenario analysis to assess the outlook for a MergeCo scenario vs. our assumptions around GMD's baseline ASPIRE 500 plan on our bottom up mine/mill/cost modeling within, all else equal. We see the merger as potentially accretive, with MergeCo lifting gold production by \~30-80kozpa to \~690-780kozpa over FY27-28E vs. a pro forma of our baseline GMD/VAU outlooks with a \~10% lower AISC of \~A\$2,850/oz, with an EBITDA lift of \~15-25% over the same period (before any mine plan/cost optimisation). On a 10yr outlook, we see aggregate production broadly similar vs. the pro forma despite not having the Tower Hill mill/deferred Laverton mill expansion, while longer-term production declines may be deferred with LoM extension enabled by enhanced exploration spend medium-term.

Together with a more capital-light MergeCo pathway by avoiding construction of a mill at Tower Hill (and the associated capex/timing risks in the current project environment; See our buy vs. build analysis), and a \~1-2yr deferral of Laverton capacity expansion (with Hub/Bruno-Lewis/Admiral material processed through the KoTH mill adding incremental ounces vs. GMD's target and liberating capacity at Laverton), our analysis implies operating FCF yields increasing +5-10% to \~10-15% on average near-term with scope for growing capital returns (average \~4-5% DPS yield) from a further strengthened balance sheet/lowered cost of capital.

We reinstate ratings on GMD to Buy (\~30% upside), Neutral on RRL (\~15% upside), and remain Not Rated on VAU. Though we have historically been more cautious on GMD's outlook, we now see reasonable upside to our revised estimates (including further elevated capex), with the standalone business on our ASPIRE 500 outlook trading \~0.8x NAV. Separately, under our MergeCo scenario, we see the potential for the business to be more defensively positioned for ongoing gold price volatility, while trading at \~0.75x NAV or pricing \~US\$3,190/oz.

Hugo Nicolaci
+61(2)9321-8323 |
hugo.nicolaci@gs.com
GS Australia Pty Ltd

Paul Young
+61(2)9321-8302 |
paul.young1@gs.com
GS Australia Pty Ltd

Marcus Dosanjh
+61(2)9321-8780 |
marcus.dosanjh@gs.com
GS Australia Pty Ltd

## High level merger summary

Following the 6-Jul proposal from Genesis Minerals (GMD.AX) to merge with Vault Minerals (VAU), and the subsequent expiration of Regis Resources' (RRL.AX) exclusive matching period, GMD and VAU have now agreed to merge via a Scheme of Arrangement, under which GMD will acquire 100% of the fully paid ordinary shares in VAU. The consideration remains unchanged from the initial proposal, with VAU shareholders to receive 0.7629 new fully paid ordinary shares in GMD plus A\$0.475 in cash for each VAU share held (a cash/scrip mix with a mix-and-match facility, subject to the aggregate \~A\$500mn cash and \~803.4mn GMD shares on offer). Based on GMD's closing share price of A\$6.29/sh on the 3rd of July 2026 (being the last close prior to GMD's initial proposal), the offer values VAU at \~A\$5.274/sh (\~A\$5.6bn fully diluted equity value), representing a \~15.7% premium to VAU's close price on the 3rd of July 2026, where upon Scheme Implementation, GMD/VAU shareholders would own \~59.8%/\~40.2% of the combined entity respectively (fully diluted).

GMD have reaffirmed the strategic rationale, where the merger remains intended to create a new Australian gold major anchored in the Tier 1 Leonora-Laverton district. GMD expects MergeCo to have an immediate pro forma production of 600-700kozpa pre-optimisation (all 100%-owned in WA), underpinned by \~400-500kozpa from the Leonora-Laverton district. The combination consolidates total milling capacity to \~15.9Mtpa (\~11.5Mtpa VAU post KOTH expansion to \~8Mtpa + \~4.4Mtpa GMD current capacity pre-Laverton expansion), with GMD noting this presents a capital-light pathway greater production by avoiding construction of a mill at Tower Hill and the associated capex/timing risks of executing in the current WA project pipeline (we see the number of expected projects tripling vs. CY25 levels on our buy vs. build analysis), whilst retaining organic expansion optionality through continued contractor support.

According to GMD, the transaction will bring together a combined mineral endowment of \~9.4Moz in Ore Reserves and \~33.6Moz in Mineral Resources, making it the dominant producer in the district. GMD expect the combined group would be underpinned by a stronger balance sheet with \~A\$611mn in pro forma net cash (incl. bullion and investments, and excluding \~A\$89mn GMD asset finance; GSe illustrative analysis \~A\$490mn of cash including asset finance (GMD \~A\$220mn and VAU \~A\$820mn, less cash consideration (\~A\$500mn) and Regis break fee (\~A\$51mn)) and \~A\$1.3bn in pro forma liquidity. GMD noted this positions the MergeCo as well-funded for both growth and shareholder returns (capital management program part of strategic review), with a pro forma market capitalisation of \~A\$12.6bn (at announcement) providing enhanced scale, liquidity and global market relevance.

The Scheme is subject to various conditions including approval by VAU shareholders at a Scheme Meeting expected to be held in Sep/Oct (following scheme booklet in Aug/Sep), with implementation of the Scheme expected to occur in Oct/Nov 2026. The VAU Board has unanimously recommended that shareholders vote in favour of the Scheme, in the absence of a superior proposal and subject to the independent expert concluding that the Scheme is in the best interests of VAU shareholders. Following the strategic review, GMD plans to release a new strategic plan in 1H CY27, including a multi-year production, cost, capex, and exploration outlook, with revised capital management framework. GMD noted some FY27 guidance to be provided with the upcoming quarterly (previously planned with a Sep-Q multi-year outlook), with some reduced capex (i.e. Tower Hill spend) as a result of the merger.

Merger appears accretive based on our illustrative analysis vs. our baseline GMD ASPIRE 500 and VAU outlooks

## Synergies, and MergeCo scenario assumptions

On synergies, GMD continues to estimate potential post-tax, undiscounted synergies of \~A\$2.0bn (net of transaction costs, stamp duty and the RRL break fee; Exhibit 55), including \~A\$1.5bn in pre-tax, undiscounted synergies over ten years that are unique to a GMD/VAU combination and only available given the proximity of the two companies' operations at Leonora (within 35km) and Bardoc-Mt Monger (see our WA gold map), with additional, yet-to-be-quantified synergies and operational flexibility also continuing to be targeted. We outline GMD's key announced synergies and our MergeCo assumptions/comments in Exhibit 1 below, along with an illustrative MergeCo outlook vs. a baseline pro forma (including the detail of our ASPIRE 500 GMD standalone outlook). We further outline underlying peer comps beneath (including production and AISC, along with the trailing 12 month milling, and OP/UG mining costs by asset vs. peers in Exhibit 48 below (see our Gold Book for further industry comps)).

Post merger completion, GMD announced that it will look to conduct a strategic review to be released in 1H CY27 which will target a review of the MergeCo asset portfolio and the optimisation of ore and mills, including:

■ Processing of Tower Hill ore through the expanded KOTH mill;

■ Acceleration of development of Focus Laverton and Lady Julie deposits;

\- Unlocking of free milling Bardoc ore at the \~1.3Mtpa Mount Monger Randalls mill;

Further resource to reserve conversion (\~25Moz of resource currently not in reserves; Exhibit 60), where GMD noted VAU have historically maintained a \~3 year reserve life in recent years, with upside from resource conversion on increased drilling;

■ Acceleration of exploration across the portfolio, with initial opportunities identified within the Chatterbox Trend, Gwalia Uppers, and King of the Hills/Darlot undergrounds;

■ Potential for non-core divestments (where GMD highlighted the Leonora-Laverton region as the core asset) up to \~A\$0.76bn on GSe including Deflector/Rothsay (\~A\$330mn; see our WA gold map) and Sugar Zone (\~A\$430mn) on our VAU base case outlook, where Mt. Monger could add \~A\$0.9bn including our resource conversion (\~A\$0.8bn) and Bardoc free milling scenario (+ \~A\$150mn).

Exhibit 1: We see a number of upfront and longer-term synergies supporting an accretive outlook, though see a shorter deferral of Laverton hub mill expansion

Summary of GMD Outlined Synergies vs. our assumptions for MergeCo in our illustrative analysis

<table><tr><td colspan="2">Summary of GMD Outlined Synergies vs. GSe</td><td>GMD Assumed Synergy Value (A$mn; undiscounted)</td><td>GSe Assumption / Comment</td></tr><tr><td rowspan="4">Infrastructure</td><td>Enabling Tower Hill ore to be processed through KOTH mill, avoiding construction of Tower Hill mill</td><td>350</td><td>We assume A$350mn total capex for the Tower Hill mill including supporting infrastructure (quoted A$229mn just for mill component), where we assume a ~A$25mn sunk cost in 1H FY27. We note this also avoids ongoing sustaining capex of the new mill.GMD noted on the target deal completion timeline of late Oct/Nov-26 this would time well with commissioning of the Stage 2 expansion at KoTH mill, with first ore from Tower Hill expected in early FY28 (reasonably ahead of schedule; first production from a Tower Hill mill was expected late FY28) accelerating production, where the ball mill enables maintaining grind size and avoiding recovery loss vs. the displaced ore.We note the Tower Hill mill contractor, GR Engineering outlined separately that they have already commenced engineering works and the procurement of long lead items for the Tower Hill mill (contract sum A$229mn), but will continue to work with GMD to optimise outcomes based on both the work scheduled and performed to date. GMD noted this may include fast tracking mill works at the Laverton hub.</td></tr><tr><td>Potential for liberation of Laverton mill capacity to accelerate development of Focus Laverton and Lady Julie assets (yet to be quantified), and defer expansion of Laverton mill capacity (capex saving)</td><td>365</td><td>On our ASPIRE 500 GMD baseline outlook, we assume expansion of Laverton hub milling capacity from ~3Mtpa to ~4.75Mtpa with mill capex of ~A$350mn, ramping up over FY30/31E and delivering a GMD group standalone ~500kozpa. We see this also potentially supported by upside to Lady Julie development vs. prior planning with an initial started pit while a larger mine incorporating prior GMD tennements goes through permit revisions.On a MergeCo scenario, while we assume further gold production uplift at the KoTH mill via additional low grade displacement from Hub/Bruno-Lewis/Admiral mines, liberating Laverton mill capacity, we assume an expansion of Laverton hub milling capacity is only deferred ~1-2yrs before making economic sense to proceed on available ore in the Laverton region.</td></tr><tr><td>Includes growth, non-process infrastructure, tailings storage facility and sustaining capital, for a total capital saving of A$715m</td><td>715</td><td></td></tr><tr><td>Subject to economic conditions, the Merged Group would have the flexibility to utilise or expand the operational 1.4Mtpa Gwalia Mill (Gwalia mill production of ~195koz based on Genesis&#x27; FY29 production outlook for Leonora)</td><td rowspan="14">~745+</td><td>We see the Gwalia and Ulysses mines ramping up to nearly fill the Gwalia mill for &gt;10 years on ~80% existing resource conversion, averaging ~160-190kozpa over the period.</td></tr><tr><td rowspan="4">Mine optimisation</td><td>Introduction of Genesis ore to the KOTH mill may enable the KOTH open pit stages 2-5 to be re-optimised based on delivery of highest value for the combined portfolio (i.e. optimising for grade and cashflow), with potential upside from streaming high grade (0.9g/t) and low grade (0.3g/t) KoTH OP ore</td><td rowspan="2">We assume current mine plans, with stockpiling for future mill expansion optionality on higher gold prices (see below on operational optionality / &quot;future proofing&quot;), with mine optimisation further potential upside to our MergeCo scenario (including further upside from streaming high grade and low grade KoTH OP ore).We assume an ~A$0.5/t OP mining cost saving at the KoTH open pit, equating to a ~A$16mnpa saving, using GMS (and avoiding third party contractor margins).GMD noted the fleet ordered for Tower Hill mining are a larger size than initially contemplated, with these lowering unit costs of future stripping programs, including KoTH stage 4/5 cutbacks.We see net regional haulage savings as more modest, with lower haulage of Hub/Bruno-Lewis/Admiral to KoTH (vs. Laverton) partly offset by increased haulage of Tower Hill to KoTH.</td></tr><tr><td>Reduction in group open pit mining costs by embedding KOTH&#x27;s owner-operator fleet into Genesis Mining Services (GMS) and utilising GMS across the enlarged Group, enabling optimisation of talent and equipment between sites, including KOTH and Tower Hill given their similar fleet size and location. GMD assume KOTH to commence owner-operator load and haul on 1 January 2027</td></tr><tr><td>Potential to defer or avoid costs associated with development and operation of the high strip ratio Westralia open pit (23:1 LOM strip ratio) in preference for higher-quality assets (e.g. Beasley Creek and Lady Julie)</td><td>We see the Westralia deferral taking place either way as part of the GMD base case ASPIRE 500 plan, with this largely deferred by the Lady Julie mine as part of the completed MAU acquisition. We factor in Westralia development from the mid-2030s, supporting stockpiles and filling the expanded Laverton hub milling capacity.</td></tr><tr><td>Optimisation of underground mining (fleet, personnel, technical expertise, infrastructure, etc) and shared technical expertise</td><td></td></tr><tr><td rowspan="5">Operational flexibility</td><td>Potential to use ore from the Tower Hill project to displace low grade open pit feed ore at KOTH which could:</td><td></td></tr><tr><td>• Materially increase production from KOTH1</td><td>The introduction of Tower Hill ore (~2-3Mtpa at ~2.0g/t) to the expanded KOTH mill, displacing low-grade KOTH open pit feed (~0.3g/t), and potentially adding an incremental ~100kozpa, taking KoTH production to ~300kozpa+ by ~FY29.</td></tr><tr><td>• Enable the building of sizeable stockpiles for operational optionality / &quot;future proofing&quot;1</td><td></td></tr><tr><td>• Lower processing costs by processing Genesis ore through the lower cost KOTH mill (net of additional haulage costs to KOTH vs. Tower Hill mill)3</td><td>We see a cost benefit of processing at the expanded ~8Mtpa KoTH mill atA$30/t (see exhibits below comparing gold asset processing costs).</td></tr><tr><td>Unlock GMD&#x27;s Bardoc free-milling ore via processing at the ~1.3Mtpa Mount Monger Randalls Mill.Free-milling Resource within Bardoc tenure includes Mineral Resource from Zoroastrian

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
