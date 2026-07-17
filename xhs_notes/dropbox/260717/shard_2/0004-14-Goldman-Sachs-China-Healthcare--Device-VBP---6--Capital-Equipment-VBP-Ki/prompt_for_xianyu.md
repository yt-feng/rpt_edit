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
# China Healthcare: Device VBP: #6: Capital Equipment VBP Kicks Off; Faster Category B Rollout but Emphasis on Reasonable Pricing

On July 14, the government released a notice on capital equipment VBP (see the notice here). The requirement to complete at least one procurement round for Category B equipment by year-end 2026 came earlier than expected, implying a faster rollout of detailed provincial procurement rules over the coming months. Meanwhile, the notice emphasizes reasonable pricing, technological appropriateness, product quality, and total life cycle costs—including consumables and maintenance—rather than focusing solely on upfront equipment prices.

Overall, the notice is broadly consistent with our previous expectations regarding the scope of equipment VBP, given the continued pressure on local government finances and hospital balance sheets through 2025. The fragmented nature of equipment procurement and the lack of unified national standards make provincial-level VBP more feasible than a centrally coordinated national rollout (see our previous note). We await further details on the implementation rules to assess the potential impact on pricing and margins. While the extent of pricing pressure will depend on the final bidding framework and individual company strategies, we expect relatively moderate price cuts for equipment versus consumables. That said, the phased rollout of equipment VBP could slowdown the near term bidding activities, as the provinces prepare for the VBP. For domestic market leaders, we believe any pricing impact could be partially offset by market share gains under VBP and increasing overseas expansion.

## Key incremental changes include:

Category A equipment to be subject to national-level VBP. Advanced radiation therapy equipment, including MR-Linac and X-ray stereotactic radiosurgery systems (e.g., CyberKnife), will be included under centrally organized VBP managed by the NHC. In contrast, highly customized systems that require supporting infrastructure construction and device-by-device regulatory approval—such as heavy-ion and proton radiation therapy systems—are temporarily excluded from the current VBP framework.

■ Accelerated rollout of Category B equipment VBP at the provincial level. Each province is required to complete at least one procurement round for Category B equipment by year-end 2026. The initial scope includes PET/MR, PET/CT, laparoscopic surgical robots, and conventional radiotherapy equipment, with plans to gradually expand coverage to other categories characterized by high capital intensity and limited market competition. In principle, procurement

+852-2978-7993 | chris.pan@gs.com
GS (Asia) L.L.C.

Ziyi Chen
+852-2978-0526 | ziyi.chen@gs.com
GS (Asia) L.L.C.

Tianyi Yan
+86(21)2401-8609 |
tianyi.yan@goldmansachs.cn
GS (China) Securities
Company Limited

Michael Zheng
+86(21)2401-8928 |
michael.zheng@goldmansachs.cn
GS (China) Securities
Company Limited

exercises should be conducted at least once annually in 1H, with greater frequency where necessary. By end-June 2027, each province must designate at least one prefecture-level city or municipality to conduct a pilot program and complete one procurement round.

Greater emphasis on reasonable pricing and value-based procurement. The notice reiterates that the configuration of the medical equipment and procurement should be aligned with hospitals' actual needs while balancing quality, price, and service in procurement evaluations. Importantly, the policy places considerable emphasis on achieving “high quality at a reasonable price” rather than pursuing the lowest acquisition cost. The guidance seeks to leverage VBP to eliminate the unreasonable pricing inflation while incorporating life cycle cost considerations—including consumables, maintenance, and after-sales service—into evaluation frameworks. This suggests a more holistic approach to procurement and may help mitigate the risk of excessive price competition or “race-to-the-bottom” bidding behavior.

## Quick refresher on the definitions of Category A and Category B capital equipment

Categories A and B are administrative classifications used by regulators for procurement approval, quota management, and allocation planning. They are distinct from the Class I, II, and III medical device classifications, which are based on product risk profile and determine the level of NMPA regulatory oversight. 1) Category A equipment includes advanced radiotherapy systems, heavy-ion and proton therapy systems, and other large-scale medical devices with an initial single-unit purchase price of Rmb50mn or above. 2) Category B equipment includes PET/MR, PET/CT, laparoscopic surgical robots, and conventional radiotherapy equipment, such as medical linear accelerators (LINAC), TomoTherapy systems, and Gamma Knife systems, as well as other large medical devices with an initial single-unit purchase price of Rmb30–50mn.

## Implications for our coverage

Surgical robots: We believe quota release for next cycle remains the more important determinant of domestic demand than pricing. Lower equipment prices are unlikely to drive meaningful volume growth while hospital purchases remain constrained by installation quotas. For our covered names, overseas markets have increasingly become the primary growth driver for both MedBot and Edge Medical (See our previous note), while the domestic market continues to provide additional upside optionality.

\- Imaging equipment: The latest PET-CT VBP framework is broadly consistent with our previous expectations, reaffirming a provincial-level procurement approach without introducing a nationwide VBP mechanism for PET-CT. As such, we do not expect a material change to the competitive landscape and believe United Imaging's leading market position in the segment should remain intact (See Tianyi's note).

## VBP tracker

Exhibit 1: VBP for consumables likely to see full coverage by YE26, likely extending to capital equipment As of Jul 16, 2026  
![](images/5cff849598b11290fb652cf8197a584a66c1cffaa88ce230c329f897f19bb3c2.jpg)

![](images/b2e7e4215473befccfd1f2c860a8e4a8f4d0fd3e3ae61f0aa2a9216749b1e0b5.jpg)

Numbers refer to # of provinces that announced/implemented VBP; N denotes the number of provinces to be announced.

Source: National/Regional Healthcare Security Administration

Exhibit 2: Dental implant renewal VBP started in July; expecting additional announcements towards year end 2026

<table><tr><td>Date of announcement</td><td>Product categories</td><td>Covered regions</td><td>Domestic companies</td><td>MNCs</td></tr><tr><td>Jul-26</td><td>Dental implant</td><td>Sichuan-led VBP renewal, covering all provinces/regions</td><td>BLBC, Bioconcept, Weigao, etc.</td><td>Straumann, Anthogyr, Adin, Alpha-Bio, Zimmer, Osstem etc.</td></tr><tr><td>Jun-26</td><td>Medical adhesives (cyanoacrylate-based)</td><td>Tianjin-led 3+N alliance, GSe 20+ provinces/ regions</td><td>Weigao, Compont, Success Pharmaceutical, etc.</td><td>J&amp;J, B. Braun</td></tr><tr><td>May-26</td><td>Pressure pump</td><td>Inner Mongolia-led regional VBP</td><td>Lepu Medical, MicroPort, Shanghai Kindly / KDL, Shenzhen Antmed, Beijing Demax, etc.</td><td>Medtronic, Boston Scientific, Cook, B. Braun, Abbott, etc.</td></tr><tr><td>Mar-26</td><td>Incision Protector</td><td>Shangdong-led regional VBP, 4 provinces</td><td>Kangji Medical, Weigao, Bluesail Surgical, etc.</td><td>Applied Medical, Medtronic, J&amp;J, etc.</td></tr><tr><td>Mar-26</td><td>Bronchoscopy internversion: Tracheal &amp; Bronchial stent, Airway balloon dilation catheter, Electronic bronchoscope/ imaging catheter, etc.</td><td>Hunan-led regional VBP</td><td>Microtech, Aohua Endoscopy, SonoScape, etc.</td><td>Boston Scientific, Olympus, Medtronic, Cook, etc.</td></tr><tr><td>Mar-26</td><td>Coronary balloon</td><td>Henan-led regional VBP, 16 provinces/ regions</td><td>Lepu, MicroPort Rhythm, Sinomed, Brosmed, DK Medtech, etc.</td><td>Boston Scientific; Nipro</td></tr><tr><td>Mar-26</td><td>Snare devices, Peripheral vascular constraint-type balloon dilation catheter, Powered irrigation device (orthopedic and trauma surgery)</td><td>Hebei-led regional VBP</td><td>Zylox-Tonbridge, Acotec, Lepu, BrosMed, Shunmei, Double Medical, etc</td><td>Medtronic, Boston Scientific, Cook, Becton Dickinson, Stryker, etc.</td></tr><tr><td>Feb-26</td><td>Neurointerventional microcatheter, Peripheral interventional microcatheter, Pacemaker consumables</td><td>Zhejiang-led regional VBP, 27/29 provinces/ regions</td><td>MicroPort NeuroTech, HeartCare, Zylox-Tonbridge, Peijia Medical, Shunmei, Lepu, MicroPort CRM, etc.</td><td>Medtronic, Abbott, Boston Scientific, Stryker, Terumo, Biotronik, etc.</td></tr></table>

Source: Regional healthcare security administration

## Related research

## Top level

China Healthcare: Device VBP: #5: DES VBP 2nd renewal: Pricing Continues to Trend Up; MNC Participation Rebounds (May 25, 2026)

China Healthcare: Device VBP : #4: Full Consumables Coverage on Track, Capital Equipment Broadening in 2026 (Mar 9, 2026)

China Healthcare: Device VBP #3: Accelerating VBP implementations in 4Q after a slower start YTD (Nov 19, 2025)

China Healthcare: Medical Devices: Accelerating VBP expansion; focus on targets for next round, with direction likely to remain consistent (Mar 11, 2025)

Investor feedback on VBP policy: increasing visibility at national level; monitoring regional pilots (Nov 9, 2022)

China Healthcare Mapping the regulatory paths in China healthcare; eyeing opportunities in divergence (Aug 8, 2021)

## Capital equipment

China Healthcare: Aug 2025 China hospital equipment bidding: Better-than-expected MoM growth, with both MNC/domestic to thrive (Sep 10, 2025)

China Healthcare: Addressing VBP risks for medical equipment; three debates after NHSA guidelines (Nov 25, 2024)

China Healthcare: Anhui VBP on large medical equipment, market share/ASP changes since 2019 (Feb 22, 2024)

## DES renewal

China Healthcare: Medical Devices: Price increase in DES VBP renewal; positive signs for long-term post-VBP pricing (Nov 30, 2022)

## Artificial joints

China Healthcare: Medical Devices: VBP update: National joints renewal results as expected; FY24 notice focuses on regional alliance (May 21, 2024)

AK Medical (1789.HK): Joint VBP renewal rules released, largely inline with our expectation; final bidding on May 21st (May 1, 2024)

AK Medical (1789.HK): Call takeaway: Encouraging volume uptake for hip/knee post VBP; Raised guidance for revenue/NP; Buy (Aug 21, 2022)

AK Medical (1789.HK): VBP uncertainty cleared, eyeing long term growth after 2022; Buy (Sep 15, 2021)

AK Medical Holdings (1789.HK): Updated VBP rules - Better than expected ceiling prices; continue to favor leading brands; Buy (Aug 24, 2021)

AK Medical Holdings (1789.HK): Final joints VBP rules released; Favors leader

brands; Buy (Jun 22, 2021)

## IVD

China Healthcare: Medical Devices: 2024 IVD VBP in-line; leading domestic players to see continued share gain; Buy Mindray, SNIBE (Jan 2, 2025)

China Healthcare: Diagnostics and Clinical Labs: IVD regional VBP final result of avg 51% cut in line with prior market expectations (Jan 2, 2024)

China Healthcare: Diagnostics and Clinical Labs: Biochemistry reagent volume-based procurement draft (Oct 14, 2022)

## Spine VBP

China Healthcare: Medical Devices: Encouraging final results for Spine VBP released; potentially sets positive tone for future rounds (Sep 28, 2022)

China Healthcare: Medical Devices: Mixed signs from Spine VBP's latest bidding rule; eyes on final result on Sep 27th (Sep 13, 2022)

China Healthcare: Expert call: Orthopedics industry back to healthy recovery; accelerating import substitution post VBP implementation (Aug 15, 2022)

Shandong Weigao Group (1066.HK): Spine VBP results could be mild; focusing on volume uptake (June 29, 2022)

## Trauma

China Healthcare: Price increase in regional trauma VBP renewal; reaffirming long-term post-VBP pricing stability (Sep 27, 2023)

## Ophthalmology

China Healthcare: Medical Devices: China IOL VBP bid price released, in-line price cut for monofocal and bifocal but significant cut for trifocal (Nov 30, 2023)

Aier Eye Hospital (300015.SZ): Planned OK lens VBP in Hebei province and scenario analysis (Oct 27, 2022)

## Dental

Americas Dental: China's implant VBP results released: NVST & XRAY receive majority of submitted volume, pricing in-line (Jan 12, 2023)

Angelalign Technology (6699.HK): Manageable price cut in 15-province VBP on clear aligners; minimal volume impact in near-term (Dec 20, 2022)

First take on dental implant pricing guidelines: Better-than-market-feared amid ongoing step-up in regulatory oversight; Neutral (Sep 12, 2022)

China Healthcare: Medical Devices: Draft guideline released for regional orthodontics VBP; awaiting submitted volume/final bidding in Nov/Dec (Oct 24, 2022)

## Disclosure Appendix

## Reg AC

We, Chris Pan, CFA, Ziyi Chen, Tianyi Yan and Michael Zheng, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Chris Pan, CFA GS (Asia) L.L.C., Ziyi Chen GS (Asia) L.L.C., Tianyi Yan GS (China) Securities Company Limited, Michael Zheng GS (China) Securities Company Limited.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses inputs for the fiscal year at least seven quarters in the future compared with the year at least three quarters in the future (on a per-share basis for all metrics).

For a more detailed description of how we calculate the GS Factor Profile, please contact your GS representative.

## M&A Rank

Across our global coverage, we examine stocks using an M&A frame

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
