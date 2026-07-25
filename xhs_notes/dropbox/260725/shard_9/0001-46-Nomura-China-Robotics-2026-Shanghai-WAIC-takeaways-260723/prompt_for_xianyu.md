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
EQUITY: TECHNOLOGY

# 2026 Shanghai WAIC takeaways

## Three shifts for China robotics: bodies scale, brains lag, data bottlenecks bind

From staged demos to deployed fleets: The World Artificial Intelligence Conference (WAIC) 2026 featured fewer acrobatic showcases and a much broader range of robots doing real work. Nearly 60 humanoids delivered actual services across venues hosting 1,100+ exhibitors, and almost every major vendor pitched deployment capability, data assets and "robot brains" ahead of hardware parameters.

## Mass production inflects, demand remains uncertain

WAIC 2026 confirmed, in our view, that embodied AI has crossed the mass-production inflection, shifting the narratives from TAM (total addressable market) to shipments, ASPs and margins, and actual deployment. For example, AgiBot (unlisted) reported 15,000 cumulative units produced; on-site, nearly 60 humanoids performed real services among 1,100+ exhibitors, and management framed reliable manufacturing, delivery and integration as the new yardstick. We see a replay of the 2019-20 EV (electric vehicle) playbook on the manufacturing side, with thematic investing entering the order-verification stage. That said, current shipments of humanoids validate manufacturability, not demand durability. Based on our industry survey, 2026E demand still skews toward entertainment/ performance (\~30%), consumer (\~30%), government procurement (\~20%) and education (\~15%), with industrial/commercial at only \~5%. We flag order composition (paying-customer mix, to-G/related-party share) and per-unit economics as the next milestones to monitor, as it may determine whether the volume story converts into earnings.

## Humanoids meet the factory test: MTBF, takt time, and the payback wall

Technology roadmaps have converged on industrial and logistics settings – predictable, repeatable environments – rather than open-ended use cases: AgiBot's G2 Max and OmniHand 3, MagicLab's (unlisted) wheeled MagicBot D1, and dexterous-hand firms mostly target factories, while consumer launches — Fourier's (unlisted) companion GR Nano and Unitree's (unlisted) GD01 rideable mecha — remain sideshows. Wheeled form-factors becoming the industrial workhorse is itself a signal, in our view: vendors are trading anthropomorphism for reliability and cost, deferring bipeds. Yet, we think, "labor" and "industrial-robotic-arms" substitution economics remain unproven: industrial buyers purchase on ROI, MTBF (mean time between failures) and takt time, and at current humanoid ASPs vs labor costs, payback periods at most workstations have yet to reach adoption thresholds, while grippers suffice at structured stations, leaving five-finger hands over-engineered. Real demand today is data collection and training grounds, OEM-subsidised pilots and to-G showcases — funded by robot-maker capex and policy money, not factory labor budgets — reconciling strong shipments with unproven economics; we view this as a supply-side, not demand-side, inflection. The signal that this flips: the first repeat order from a non-related industrial customer, paid out of an operating budget rather than a pilot budget.

## Data is one binding constraint for embodied AI

We note competitive focus is shifting from bodies to brains: the debate between VLA (vision-language-action) and world models settled on fusion — Spirit AI's (unlisted) v1.6 already runs a fused architecture, while Ant Group's (unlisted) LingBot-VLA 2.0 spans 17 OEMs and 20+ configurations. Our industry survey shows the binding constraint is high-quality real physical-interaction data, not architecture or compute: 2026E demand of \~10mn hours vs \~0.5mn hours of global high-quality stock, a 20x gap, with 2,000-5,000 hours needed per deliverable skill. For data collection, we assume a \~CNY4-5bn 2026F China market size, and with 20+ city-level data factories under construction plus offshore crowdsourcing; we expect unit price to decline within 12-24 months. However, cheaper data only eases collection costs — it neither closes the data gap nor unlocks the collect-train-deploy-feedback loop — we expect robot 'brain' maturity to take years: leading robotics firm's estimates point to an embodied-AI 'ChatGPT moment' in 2-3 years and scaled adoption later, as the effective data feedback from deployed fleets is still low of today's data mix.

## Research Analysts

China Technology
Frank Fan - NIHK
frank.fan@NOM.com
+852 2252 2195

Donnie Teng - NIHK
donnie.teng@NOM.com
+852 2252 1439

## Headline shipments mask a demand base dominated by non-productive use

Beneath the headline volumes, our survey work points to a demand base still dominated by non-productive use. We forecast 2026 industry shipments of 45-50k units — below the \~100k media narrative — driven by accelerating government procurement and consumer demand inflection from low-priced product launches (Optimus ramps; China scales up as cost curves bend lower published on 28 June 2026). Based on our industry survey, 2026E demand still skews toward entertainment/performance (\~30%), consumer (\~30%), government procurement (\~20%) and education (\~15%), with innovative scenarios (industrial/commercial) at only \~5% — a rotation away from 2025's rental-led mix (45-50%), but not yet toward productive use. Rental economics illustrate the fragility: humanoid day-rates of CNY4,000-20,000 are down 50-60% y-y, stabilising only because OEM selling prices have already fallen; the market remains local and fragmented — too small, per the expert, to support platform-style rental businesses — and rising per-event robot counts (one unit in 2025 to four in 2026, occasionally 20-30) drive volume without recurring revenue. Government-backed data-collection factories, \~20% of 2026F demand, carry 3-5-year paybacks, and we expect humanoid data-collection procurement to be soft in 2027F as body-free collection scales. Capital formation, meanwhile, is running well ahead of this demand reality: per GGII, humanoid OEMs raised CNY70.5bn across 98 deals in 1H26 (53% of total sector financing), with embodied foundation models (CNY22.3bn/40deals), world models (CNY19.1bn/17 deals) and data infrastructure (CNY4.4bn/19 deals) absorbing much of the remainder. The funding mix is effectively underwriting a model-driven capability inflection that the shipment mix has yet to validate. We therefore treat repeat orders from non-related industrial customers as necessary for companies' earnings.

Fig. 1: End market demand mix  
![](images/5f67df4df08d082c8609b52354d951c29b979c472136c081788af7b591566faa.jpg)  
Source: Company data, NOM

Fig. 2: 1H26 financing by sub-segment  
![](images/5b4060babdf99b0ea0c2b5c8a5aaffd4984e7f7599fa0b85cba713b8fb19f0d7.jpg)  
Source: GGII, NOM

## Dexterous hands: three routes converge, hardware iterates faster than demand

Dexterous hands are converging on a three-route roadmap. Linkage hands — low-DOF (≤ 12 degrees of freedom), ASPs of CNY12,000-13,000 and over 80% of industry shipments — form the commoditizing legacy base, led by Inspire Robots (unlisted), with OYMotion (unlisted) and Zhaowei (003021 CH, Not rated) following; sub-CNY10k pricing has already emerged. The high-DOF battleground is tendon-drive versus direct-drive. Tendon designs (15-19 DOF, \~CNY38,000 ASP) most closely replicate the human hand — which proponents argue eases training on human-collected data — championed by LinkerBot (unlisted) and Dexterous Intelligence (unlisted), but face tendon creep and \~2-month lifespans. Direct-drive (20+ DOF, CNY33,000-34,000, volume from 4Q26) is favored by algorithm teams for per-joint force control and RL (reinforcement learning) friendliness — Sharpa (Unlisted) leads, with Sudo's (Unlisted) 22-DOF/840g hand and Kinetix AI's (unlisted) 37-DOF in-palm-motor design at WAIC — but motor heat binds: vendors face a heat-force-size triangle in which only two can be optimized, so hybrid architectures are proliferating. Tactile sensing is consensus at fingertips only; full-palm schemes still diverge. With OEMs such as AgiBot iterating in-house hands (OmniHand 3) and industry shipments guided +80-100% in 2026, hands are the fastest-iterating link in the chain — though supply still runs ahead of end-demand.

Fig. 3: Average ASP for different technology route  
![](images/599db9dbd24e9634994a8b0c8e411f7f78bb0ff2776c9d083475ce9b1ccf0b29.jpg)  
Source: Company data, NOM estimates

Fig. 4: Dexterous hand gripper penetration in humanoid  
![](images/1d72a716731d5a365b49c79c5bebb58c03c8efdb9f4d1ab3d24d36203ddf1dba.jpg)  
Source: Company data, NOM estimates

Fig. 5: Technology roadmap of dexterous hands

<table><tr><td>Items</td><td>Linkage (screw+rod)</td><td>Tendon (motors in forearm)</td><td>Direct-drive (motors in hand)</td><td>Hybrid (DD-led + tendon)</td></tr><tr><td>DoF (degree of freedom)</td><td>Low-DoF (≤12)</td><td>High-DoF (active ≥16)</td><td>High-DoF</td><td>High-DoFsolution</td></tr><tr><td>2025 shipment share</td><td>&gt;80% (all low-DoF)</td><td>Small; LinkerBot ~80%</td><td>Ramping-up since 4Q25</td><td>Emerging in 2026</td></tr><tr><td>Lifespan</td><td>Mature</td><td>~30 days → 2 months+</td><td>~4 months</td><td>TBD; heat now well-managed</td></tr><tr><td>Key bottleneck</td><td>Ceiling on DoF</td><td>Tendon life / creep / derailing</td><td>Heat / weight</td><td>Life + cost</td></tr><tr><td>Force control &amp; training</td><td>Easy</td><td>Needs creep-compensation</td><td>Joint-level force control</td><td>Easier than pure tendon</td></tr><tr><td>Cost / ASP</td><td>CNY12-13k; sub-10k models emerging</td><td>~CNY38k</td><td>CNY33-34k</td><td>&lt;10% premium vs pure DD; performance +30-40%</td></tr><tr><td>Key players</td><td>Inspire / OYMotion / Zhaowei / BrainCo (low-DoF)</td><td>LinkerBot / DexRobot</td><td>Sharpa / WuJi / Sudo / BrainCo Revo3</td><td>Xynova Flex2 / AgiLink</td></tr></table>

Source: Company data, NOM

Fig. 6: Market survey on dexterous hand and component firms

<table><tr><td>Company</td><td>Robotics firm Feb 2026</td><td>Robotics firm Apr 2026</td><td>Dexterous hand May 2026</td><td>Component firm Jun 2026</td><td>Robotics firm Jun 2026</td><td>Dexterous hand Jul 2026</td><td>Media Jul 2026</td></tr><tr><td>Inspire Robots</td><td>+</td><td>++</td><td>+</td><td></td><td>○</td><td>+</td><td>○</td></tr><tr><td>BrainCo</td><td></td><td>++</td><td>+</td><td></td><td></td><td>+</td><td>+</td></tr><tr><td>Xynova</td><td></td><td>++</td><td>+</td><td>○</td><td></td><td>++</td><td>○</td></tr><tr><td>Wuji Tech</td><td>+</td><td>+</td><td>+</td><td>++</td><td>++</td><td>++</td><td>+</td></tr><tr><td>Sharpa</td><td>+</td><td>○</td><td>+</td><td>+</td><td>○</td><td>++</td><td>+</td></tr><tr><td>Dexterous Intelligence</td><td></td><td>+</td><td></td><td></td><td></td><td>○</td><td>○</td></tr><tr><td>LinkerBot</td><td>++</td><td></td><td></td><td>○</td><td></td><td></td><td>○</td></tr><tr><td>AgiLink</td><td></td><td></td><td></td><td></td><td></td><td>+</td><td>○</td></tr><tr><td>PaXini</td><td>+</td><td>○</td><td>++</td><td></td><td>+</td><td>+</td><td></td></tr><tr><td>++</td><td>++ strong positive</td><td>+</td><td>+ positive</td><td>○</td><td>○ neutral/mixed</td><td></td><td>not mentioned</td></tr></table>

Source: Company data, NOM

## The brain race runs through data: brain maturity may take years on scarce feedback

WAIC made the data bottleneck visible on the show floor, where data tooling emerged as a product category in its own right (Data emerges as the critical part for robotics published on 5 July 2026). Exhibitors moved beyond robots to full acquisition stacks — PsiBot's (unlisted) SynCap system synchronizing vision, language, tactile and motion streams, BrainCo's (unlisted) training-platform-plus-collection solution and a cluster of exoskeleton-glove and teleoperation rigs — while DexForce (unlisted) open-sourced a human-simulation-real aligned dataset and JD.com (JD US, Buy) was reported to be building a large-scale collection center, signaling platform capital entering the trade. Standardized collection-simulation-evaluation-deployment pipelines were the common pitch — echoing the closed-loop model we favor — and are gaining regulatory scaffolding: a national standard on humanoid dataset quality evaluation was formally initiated in July 2026 (under China's robotics standards committee TC591), alongside an MIIT industry standard on training-data management now in public consultation—though vendors guarding private standards may slow adoption. We expect that VLA's generalization and long-horizon limits, acknowledged since 4Q25, are at core a data problem, pushing vendors toward world-model fusion — pretraining corpora already run near 1:9 real-to-synthetic, lowering but not eliminating real-data needs — while the simulation-heavy US route contrasts with China's real-machine teleoperation weighting.

Fig. 7: Data collection market size  
![](images/44444b167d79881c00ec29ef5911df1843d8ab768815505485a0e38b904b9068.jpg)  
Source: Company data, NOM estimates

Fig. 8: Share and ASP in different data collection types  
![](images/120d92287b7038c8f787ef9f6ba1a596f42ce63d636309c6e4e72330e142a38c.jpg)  
Source: Company data, NOM estimates

## Appendix A-1

This report has been produced by NOM International (Hong Kong) Ltd. (NIHK), Hong Kong. See Disclaimers for NOM Group entity details.

## Analyst Certification

We, Frank Fan and Donnie Teng, hereby certify (1) that the views expressed in this Research report accurately reflect our personal views about any or all of the subject securities or issuers referred to in this Research report, (2) no part of our compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this Research report and (3) no part of our compensation is tied to any specific investment banking transactions performed by NOM Securities International, Inc., NOM International plc or any other NOM Group company.

## Important Disclosures

## Online availability of research and conflict-of-interest disclosures

NOM Group research is available on www.NOMnow.com/research, Bloomberg, Capital IQ, Factset, LSEG.

Important disclosures may be read at http://go.NOMnow.com/research/m/Disclosures or requested from NOM Securities International, Inc. If you have any difficulties with the website, please email grpsupport@NOM.com for help.

The analysts responsible for preparing this report have received compensation based upon various factors including the firm's total revenues, a portion of which is generated by Investment Banking activities. Unless otherwise noted, the non-US analysts listed at the front of this report are not registered/qualified as research analysts under FINRA rules, may not be associated persons of NSI, and may not be subject to FINRA Rule 2241 restrictions on communications with covered companies, public appearances, and trading securities held by a research analyst account.

NOM Global Financial Products Inc. (NGFP) NOM Derivative Products Inc. (NDP) and NOM International plc. (NIplc) are registered with the Commodities Futures Trading Commission and the National Futures Association (NFA) as swap dealers. NGFP, NDPI, and NIplc are generally engaged in the trading of swaps and other derivative products, any of which may be the subject of this report.

## Distribution of ratings (NOM Group)

The distribution of all ratings published by NOM Group Global Equity Research is as follows:

58% have been assigned a Buy rating which, for purposes of mandatory disclosures, are classified as a Buy rating; 33% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services\*\* by the NOM Group.

39%

[中间内容因长度限制已省略]

bai Financial Services Authority) in the United Arab Emirates ('UAE') or a 'Market Counterparty' or a 'Business Customer' (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar ('Qatar') by NOM Saudi Arabia, Nlplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than 'Authorised Persons', 'Exempt Persons' or 'Institutions' located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but

not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page: http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
