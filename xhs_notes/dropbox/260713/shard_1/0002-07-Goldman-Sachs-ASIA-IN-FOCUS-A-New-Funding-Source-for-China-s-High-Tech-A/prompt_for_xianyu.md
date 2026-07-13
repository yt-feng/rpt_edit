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
ASIA IN FOCUS

# A New Funding Source for China's High-Tech Ambitions

China's slowing Q2 growth has increased the need for incremental easing and raised market attention on a potentially faster implementation of the RMB800bn “New Policy-Based Financial Instrument” (NPBFI) that was already planned for this year. In this note, we explain how the NPBFI works and why Chinese policymakers have increasingly favored this tool in recent years, and assess its potential impact on GDP.

Lisheng Wang
+852-3966-4004 |
lisheng.wang@gs.com
GS (Asia) L.L.C.

The NPBFI is a “quasi-fiscal” policy instrument used in recent years to fund strategically important investment mainly through policy banks, outside traditional commercial bank lending channels. By providing low-cost, long-term capital to supplement the equity tranche of selected projects, the tool aims to resolve the persistent bottleneck of insufficient equity capital that has historically hindered certain manufacturing and infrastructure investment.

Funding has been targeted toward new-economy sectors and economically stronger provinces. Most NPBFI funding has gone to high-tech manufacturing, AI infrastructure, strategic supply chains, green transition, urban renewal, and “Six Networks” projects (including water networks, new-type power grids, computing power networks, next-generation communication networks, urban underground pipeline networks, and logistics networks). Around 80% of the 2025 quota was allocated to 12 “major economic powerhouse” provinces that account for the majority of China’s R&D spending and GDP.

The tool reflects policymakers' dual objective of supporting high-tech investment while limiting local government debt risks. Compared with local government financing, the NPBFI is more centrally coordinated, relies on policy bank funding via bond issuance and the PBOC's Pledged Supplementary Lending (PSL), and can in theory help mobilize follow-on bank lending and private-sector capital without adding directly to local government off-balance-sheet debt.

The potential impact on GDP could be meaningful, but official multiplier estimates are likely to overstate the true incremental impact, in our view. We estimate the 2026 NPBFI quota of RMB800bn could lift real GDP level by around 0.5pp in the baseline scenario, with the impact concentrated in late 2026 and early 2027. Scenario analysis suggests a range of 0.3pp to 1.1pp depending on our fiscal multiplier assumptions. High-frequency progress tracking remains difficult because PSL and policy bank bond issuance data are volatile and not always synchronized with actual NPBFI deployment.

## A New Funding Source for China's High-Tech Ambitions

China's slowing Q2 growth has increased the need for incremental easing, while recent policy communications reaffirmed top leadership's strong commitment to supporting China's “high-quality growth.” These developments have raised market attention on a potentially faster implementation of fiscal easing measures that were already planned for this year, including the RMB800bn “New Policy-Based Financial Instrument” (NPBFI; 新型政策性金融工具). In this note, we explain how the NPBFI works and why policymakers have increasingly favored this tool in recent years, and assess its potential impact on GDP.

The NPBFI is a “quasi-fiscal” policy instrument used in recent years to fund strategically important investment mainly through policy banks, $^{1}$ outside traditional commercial bank lending channels (Exhibit 1). By providing low-cost, long-term capital to supplement the equity tranche of selected projects, the tool aims to resolve the persistent bottleneck of insufficient equity capital that has historically hindered certain manufacturing and infrastructure investment.

By sector, most NPBFI funding has gone to high-tech manufacturing (e.g., AI infrastructure, the digital economy, and the low-altitude economy), strategic supply chains (e.g., food, energy, and semiconductors), the green transition, and people's livelihoods (e.g., urban renewal) related areas, reflecting the increasing policy support for China's “New Quality Productive Forces” (新质生产力). Some projects are part of the Nationwide “Six Networks” (“六张网”) initiative, which covers water networks, new-type power grids, computing power networks, next-generation communication networks, urban underground pipeline networks, and logistics networks. Geographically, about 80% of funding since 2025 has been allocated to 12 “major economic powerhouse” provinces.

Exhibit 1: A comparison of China's NPBFI implementation between 2025 and 2026

<table><tr><td colspan="2">New Policy-Based Financial Instrument (NPBFI)</td><td>2025 Outturn</td><td>2026 Target</td><td>Highlights</td></tr><tr><td>Annual quota (RMB bn)</td><td>RMB bn% in annual GDP</td><td>5000.4</td><td>8000.5</td><td>Notable expansion in the quota from 2025 to 2026; 2025 quota mainly used in Q4 2025</td></tr><tr><td>Lending entities</td><td>China Development Bank (CDB)Agricultural Development Bank of China (ADBC)Export-Import Bank of China (EXIM)</td><td>RMB250bnRMB150bnRMB100bn</td><td>Distribution among the three policy banks likely similar to 2025</td><td>Traditional and new infrastructure, high-tech manufacturing, digital economyRural and agriculture related infrastructureTrade-related infrastructure, new economy sectors</td></tr><tr><td>Share of spending in the 12 &quot;major economic powerhouse&quot; provinces</td><td>% of total</td><td>~77</td><td>Likely around 80</td><td>Skewed to more deleveloped coastal regions with rapid expansion of the new economy</td></tr><tr><td>Share of spending to support the private sector</td><td>% of total</td><td>~23</td><td>Likely &gt;=20</td><td>The 2025 outturn was slightly higher than the target (20%)</td></tr><tr><td colspan="2">The window for implementing the tool</td><td>~1 month, from end-Sep to end-Oct 2025</td><td>In or after Q3 2026</td><td>Part of funding from the 2025 quota was spent in 2026</td></tr><tr><td colspan="2">Major areas for investment</td><td colspan="2">&quot;Major economic powerhouse&quot; provinces, &quot;New Quality Productive Forces&quot;, high-tech manufacturing (e.g., AI infrastructure, the digital economy, the low-altitude economy), strategic supply chains (e.g., food, energy and semiconductors), green transition, and people&#x27;s livelihoods (e.g., urban renewal) related projects.</td><td>Increasingly focusing on the new economy sectors</td></tr></table>

Source: Government websites, Data compiled by GS Global Investment Research

## A brief history and operating mechanism of the NPBFI

The NPBFI traces its roots to the 2022 “Policy-backed and Development-oriented Financial Instrument” (政策性开发性金融工具), which deployed RMB740bn of equity funding for major infrastructure projects during the Covid pandemic, particularly in transport, water conservancy, energy, and new infrastructure. At the April 2025 Politburo meeting, amid the US-China tariff escalation, the leadership pledged to establish the NPBFI, institutionalizing the earlier tool and broadening its mandate beyond traditional infrastructure to support China’s “New Quality Productive Forces.” The National Development and Reform Commission (NDRC) announced a RMB500bn quota for 2025 in late September, which policy banks had fully deployed by end-October. In 2026, policymakers raised the quota to RMB800bn, with a greater tilt toward new-economy sectors.

Under the current NPBFI mechanism, the three major policy banks raise low-cost funding by issuing financial bonds or using the PBOC's Pledged Supplementary Lending (PSL) facility (Exhibit 2). The proceeds are channeled into dedicated investment funds set up by the policy banks, which then provide equity capital to key strategic projects pre-screened by the NDRC. The NPBFI is intended to provide a new source of equity capital, helping eligible projects meet the initial 15-25% (of total project cost) minimum funding requirement before they can borrow from commercial banks or private-sector lenders. $^{2}$

The NPBFI's effective financing cost is generally lower than that of most government financing channels (see Exhibit 12 in the Appendix for a detailed comparison). This reflects the already-low PSL interest rate (currently $1.75\%$ , typically with tenors of 3y or longer) and China Development Bank Bond (CDB, as a representative of policy bank financial bonds) yields (around $1.5\% / 1.6\%$ p.a. in recent months for the 3y/5y tenor), both of which are below local government financing costs (Exhibit 3). The central budget also offers additional interest subsidies for some designated areas, such as loans to projects involving small and medium-sized private enterprises.

Exhibit 2: How the NPBFI mechanism works  
![](images/9e5137e27dcef0e4dc3e3a38d0042dbc0570e0edfdca7cc8a6f7ec7c3c563bee.jpg)  
Source: PBOC, NDRC, GS Global Investment Research

## Why have Chinese policymakers increasingly favored this tool in recent years?

In our view, China's fiscal system now faces a dual mandate: supporting the economy's transition toward high-tech sectors while containing local government debt risks. On one side, the ongoing US-China technology race calls for larger and more durable funding support for high-tech industries over the medium to long term. Funding for China's high-tech manufacturing sector, including AI supply chains, remains largely government-led, as policymakers seek to narrow the gap in hyperscaler capex between the US and China (Exhibit 4). On the other side, several off-budget government financing channels—especially local government financing vehicle (LGFV) financing and land sales revenue—are likely to remain under pressure amid the 2024-28 local government debt resolution program and the prolonged property downturn.

China therefore needs a financing approach that can address both objectives, and the NPBFI is one of its new tools. The instrument is centrally controlled, requires high-level coordination among the PBOC, NDRC, Ministry of Finance (MOF) and policy banks, and in theory helps fill project capital shortfalls to better leverage private investment without adding directly to local government off-balance-sheet debt. It also complements China's existing government funding channels for high-tech investment, including state-run national investment funds (e.g., for semiconductors, AI, and venture capital), central government special bonds (CGSB) for “Two Majors” projects (“两重”项目；i.e., projects and areas of strategic importance, including high-tech manufacturing), local government special bonds (LGSB) for new infrastructure, and commercial bank loans backed by the PBOC’s low-cost relending support.

From a statistical perspective, the NPBFI is not fully captured in the PBOC's total social financing (TSF) metric, $^{3}$ because the funds are raised by policy banks (rather than non-financial sectors) through bond issuance and PSL, and then deployed as project equity capital (rather than lending to corporates).

Exhibit 3: PSL interest rates and CDB yields have declined since the start of 2026  
![](images/a3aa1a0c27fa2f0fcc7cf84dc36bfe9becf2971dfa319451fc20a83fdcfb6d2c.jpg)  
PSL, CDB and LGB refer to Pledged Supplementary Lending, China Development Bank Bond, and Local Government Bond, respectively.  
Source: PBOC, Wind, Data compiled by GS Global Investment Research

Exhibit 4: The US-China hyperscaler capex gap remains significant  
![](images/e6a3715d4eb3d7f6ab2961f84136789fe09fe37109a2f53b451227f17f3d7740.jpg)  
For ByteDance (Not Covered), our China Internet Research team imputed capex based on industry trends. We caution that the US-China gap in AI-related computing capacity is likely smaller than nominal hyperscaler capex suggests, given China's lower data-center construction costs and the government's sizable role in AI-related investment.

## NPBFI funding is skewed toward larger, more developed provinces

According to policy bank announcements, around 80% of 2025 NPBFI funding—roughly RMB400bn out of the RMB500bn annual quota—was allocated to China’s 12 “major economic powerhouse provinces” (“12个经济大省”): Guangdong, Jiangsu, Shandong, Zhejiang, Sichuan, Henan, Hubei, Fujian, Shanghai, Hunan, Anhui, and Beijing, based on official definitions ranked by nominal GDP size in recent years. The share was 78% for CDB, 73% for ADBC, and 83% for EXIM. Together, these provinces accounted for 80% of national R&D spending, 72% of retail sales, 69% of GDP, 59% of the population, and 58% of fixed asset investment (FAI), based on our estimates (Exhibit 5). We expect the FAI gap between more developed coastal regions and fiscally constrained inland regions to remain wide in coming years, reflecting stronger policy support for high-tech development (with the NPBFI as one example), ongoing local government debt resolution, and continued population inflows to large cities (Exhibit 6).

Exhibit 5: The 12 “major economic powerhouse” provinces account for large shares of national R&D spending and GDP  
![](images/cd74e951c16087018ef4f2911175edf2a02ee5adbc1e3f56c4a5cc947ed8ea22.jpg)  
The 12 “major economic powerhouse” provinces are based on official definitions, including Guangdong, Jiangsu, Shandong, Zhejiang, Sichuan, Henan, Hubei, Fujian, Shanghai, Hunan, Anhui, and Beijing.  
Source: Wind, CEIC, GS Global Investment Research

Exhibit 6: FAI divergence between “major economic powerhouse” provinces and heavily indebted provinces remains wide  
![](images/3a8b4336098ecadb573f063ae4897e82334278b4644d67be484dbeff52dc35d2.jpg)  
The 12 “major economic powerhouse” provinces include Guangdong, Jiangsu, Shandong, Zhejiang, Sichuan, Henan, Hubei, Fujian, Shanghai, Hunan, Anhui and Beijing; and the 12 heavily-indebted provinces include Guizhou, Tianjin, Yunnan, Inner Mongolia, Liaoning, Jilin, Chongqing, Guangxi, Heilongjiang, Gansu, Ningxia, and Qinghai, both according to official definitions.  
Source: Wind, CEIC, GS Global Investment Research

## Assessing the GDP impact under different scenarios

Using last year as a reference, policy banks completed the deployment of the 2025 quota by end-October, roughly one month after its approval in late September, while some supplementary private-sector capital for approved projects was still being mobilized in H1 this year. High-tech-related FAI rebounded quickly in the following months and continued to outperform headline FAI (despite our long-standing concerns about FAI data reliability, the relative performance of FAI sub-sectors may still provide useful signal value; Exhibit 7). Our proprietary China investment tracker suggests that real investment growth improved to 3.5% yoy in H1 2026 from 2.2% yoy in Q4 2025.

Official estimates typically assume investment multipliers of 10-15x, implying that the RMB500bn and RMB800bn NPBFI quotas in 2025 and 2026, respectively, could lift headline FAI by RMB7tn and RMB10tn over the medium to long term. Some China watchers estimate that this year's RMB800bn NPBFI could generate RMB5-8tn of total FAI, based on the minimum equity capital requirement of $20 - 30\%$ for most infrastructure projects and the maximum $50\%$ share of NPBFI in project equity capital, assuming other funding channels such as proceeds from central and local government special bond issuance provide the remaining equity capital needed for project launches.

Although we expect the NPBFI to deliver a larger investment and growth multiplier than some traditional government funding tools, such as LGFV financing and LGSB, we believe these estimates overstate the net impact because the expected “crowding-in” effect could partly crowd out financing for other investment projects. Specifically:

Some complementary funding may come from the government budget rather than purely incremental private-secto

[中间内容因长度限制已省略]

ttempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints.

As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
