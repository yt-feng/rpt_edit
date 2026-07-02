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
# Americas Technology: Hardware: Data center & campus networking preview

We update our industry networking model to reflect the latest C1Q26 data from 650 Group. 650 Group upgraded its outlook for the AI Ethernet data center switching market, where spending should reach \~\$89 bn in 2030, growing at a 61% 2025-30 CAGR with stronger demand across all customer verticals (hyperscalers, tier 2 cloud, and enterprise). We view the outlook for increased networking spend as a result of the growing complexity of AI data center builds which should require greater networking attach to support high-performance, low-latency data traffic flows. Within the campus market: (1) WLAN (indoor + cloud)'s 2026-2030 outlook was raised by \~10% on average (now expecting \~\$13.4 bn in 2030, growing at a \~7% 5-yr CAGR v. \~\$10.6 bn prior), primarily driven by higher WiFi 7 estimates (+13% on average across 2026-2030); (2) Enterprise switching estimates grew by \~3% on average to reach \~\$28 bn by 2030 (v. \$27 bn prior). We view upgraded campus spending outlooks as a result of (a) continued need for network modernization to support greater network data traffic flows, as well as (b) partial impact of memory price increases (for campus switches). We highlight market share shifts by equipment market below.

Set up into C2Q26 earnings: Across our networking coverage, we believe ANET & CLS are well set up into earnings. Quarter-to-date, CLS (+26% in C2Q26) and ANET (+36% in C2Q26) underperformed the rest of our networking coverage (CSCO +51%, HPE +88%, FFIV +41%). We believe the relative underperformance of these two companies may be in part due to supply chain constraints on switching silicon that limits near-term revenue upside to guidance. However, we believe demand for AI Ethernet data center networking switches, for which spending by hyperscalers (their largest customers) should grow by \~10X by 2030 (Exhibit 1), should be non-perishable and further benefit 2028/29 growth. For HPE, we remain constructive on the positive synergies in HPE's campus portfolio with stable market share in WLAN and campus switching in the 3 quarters post acquisition of Juniper, and continue to see upside to F2027 networking outlook (+8-12% revenue growth) on strong industry trends in data center switching & DCI.

Michael Ng, CFA +1(212)902-8618 | michael.ng@gs.com GS & Co. LLC

Zorayda Montemayor +1(212)357-6403 | zorayda.montemayor@gs.com GS & Co. LLC

Katherine Murphy  
+1(212)902-1151 |  
katherine.a.murphy@gs.com  
GS & Co. LLC

## Data center networking forecast updates

Exhibit 1: Global data center switching spend is expected to grow robustly, quadrupling by 2030 (relative to 2025) Global data center switching spend by vertical and AI/traditional (\$, mn)

<table><tr><td rowspan="2">($, mn)</td><td colspan="3">AI Data Center Switching*</td></tr><tr><td>2025</td><td>2030</td><td>5-yr CAGR</td></tr><tr><td>Hyperscalers</td><td>$4,948</td><td>$52,717</td><td>61%</td></tr><tr><td>Tier 2 Cloud + SP</td><td>$2,606</td><td>$28,249</td><td>61%</td></tr><tr><td>Enterprise</td><td>$553</td><td>$7,933</td><td>70%</td></tr><tr><td>Total AI Data Center</td><td>$8,107</td><td>$88,899</td><td>61%</td></tr></table>

<table><tr><td rowspan="2"></td><td colspan="3">Traditional Data Center Switching</td></tr><tr><td>2025</td><td>2030</td><td>5-yr CAGR</td></tr><tr><td>Hyperscalers</td><td>$7,708</td><td>$7,573</td><td>0%</td></tr><tr><td>Tier 2 Cloud + SP</td><td>$7,013</td><td>$18,497</td><td>21%</td></tr><tr><td>Enterprise</td><td>$8,960</td><td>$9,570</td><td>1%</td></tr><tr><td>Total Traditional Data Center</td><td>$23,682</td><td>$35,640</td><td>9%</td></tr></table>

<table><tr><td rowspan="2"></td><td colspan="3">Total Data Center Switching*</td></tr><tr><td>2025</td><td>2030</td><td>5-yr CAGR</td></tr><tr><td>Hyperscalers</td><td>$12,656</td><td>$60,289</td><td>37%</td></tr><tr><td>Tier 2 Cloud + SP</td><td>$9,619</td><td>$46,746</td><td>37%</td></tr><tr><td>Enterprise</td><td>$9,514</td><td>$17,503</td><td>13%</td></tr><tr><td>Total Data Center</td><td>$31,788</td><td>$124,538</td><td>31%</td></tr></table>

\*Includes Ethernet (frontend, backend) switches  
Source: 650 Group

Exhibit 2: 650 Group's AI data center switching 2026-2030 outlook was raised by $9 \%$ on average annually Industry AI data center switching estimate revisions, ( $, mn$ )  
![](images/50c5ea70abefe5cbc91ee9e4bf3af6f73b57009b4761da4d8522f2e53d55b867.jpg)  
Only includes AI Ethernet Front-end & Back-end switching

Exhibit 3: The outlook for the rest of the data center switching market (excluding AI Ethernet) was revised upwards by 9% on average as well for 2026-2030 Non-AI Ethernet DC switching estimate revisions (\$, mn)  
![](images/ca85afb1a80b1b801fb6b406c8db08fa9cbdbd33408f9985d74f1ce8108fcf3b.jpg)  
Source: 650 Group  
Excludes AI Ethernet front end & back end switching

Source: 650 Group

Exhibit 4: Celestica and Nvidia lead the back-end AI Ethernet networking market, with Arista closely following Backend AI Ethernet networking revenue market share (%)  
![](images/1f04d99c466ab753b1bc9cb47430ca31c9088b418809357337faee02529c1fb8.jpg)  
Source: 650 Group

Exhibit 5: Celestica and Arista lead the front-end networking market with $30\%+$ share, though Cisco has gained 12pp of share over the past 3 quarters Front-end AI Ethernet networking revenue market share (\% of total)

![](images/0699ceb150c1f0309d17859b577f8680902e831e0f29814259384d641f4911b9.jpg)  
Source: 650 Group

Exhibit 6: 800G should comprise \~80% of total AI DC Ethernet Switching revenue in 2026, before 1.6T begins to meaningfully ramp in 2027
Share of AI Ethernet data center switching revenue (%) by port speed  
![](images/d29b3068aac936e707aae0fe63aa0c37c2a8bdcfd643cc8764f0d096583ba31f.jpg)  
Source: 650 Group  
Share of 800G switching revenue (%)

Exhibit 7: Celestica continues to lead the 800G switching market, though Arista and Nvidia have gained share over the past year

![](images/2ee8780a46ee34b14d71c7e64a2fd2f2df04e41b7c1019cffdf16e0943c0412f.jpg)  
Source: 650 Group

Exhibit 8: DCI spending growth, nearly a $100\%$ 5-yr CAGR through 2030, should be roughly evenly distributed across switching and routing  
DCI revenue by switching vs routing  
![](images/8de25ae3cdcdad65949db70d6c42f771e34d3d243fc7243d782b33941c041a0f.jpg)  
Exhibit 9: Arista strongly leads the overall DCI switching market  
Source: 650 Group

DCI switching market revenue share by vendor $(\%)$  
![](images/1a7bdcf238d680a3cb81a642ba96abb825a7bec529ddbb2039b7a14a115438af.jpg)  
Source: 650 Group

Exhibit 10: Cisco & HPE closely lead the DCI routing market with 39% and 36% of market revenue respectively
DCI revenue market share (%)  
![](images/c14fbd27b3c904ca99b2384a9425534a322362ffa57c211517107b21633544f9.jpg)  
Source: 650 Group

Exhibit 11: The overall scale-up switching market should grow from \~\$7 bn in 2025 to \~\$100 bn in 2030, with Ethernet growing to make up \~20% of industry revenues
Scale up switching market revenue (\$, mn)  
![](images/735afd36a57255dd382500e532d2a5ae768fd4ec64023fe33cbf98315b74ab94.jpg)  
Source: 650 Group  
Exhibit 13: Cloud data center equipment capital expenditures are expected to grow at a 33% 2025-2030 CAGR to \~\$3.2 trillion in 2030, in-line with total cloud provider capex growing at a 34% 5-year CAGR over the same period  
Cloud capital expenditures over time (\$, bn)

![](images/dd19da89bdffb23dee0885e1a55d670a2afab6df2b39bd4a429081df690210b7.jpg)  
Source: 650 Group  
Exhibit 12: 2026-2030 forecasts for cloud data center equipment capital expenditures were raised by \~28% on average relative to forecasts from 4Q25
Cloud DC equipment capital expenditures (\$, mn)

![](images/5e3920c6a147dd9eeddf87ab64a12960bf84c78d2a403033607dae7e2c7a5fae.jpg)  
Source: 650 Group, Data compiled by GS Global Investment Research

## Campus networking forecast updates

Exhibit 14: The enterprise switching market should grow 7% year-over-year in 2026, in-line its 7% 5-yr 2025-30 CAGR

Enterprise switching revenue (\$, mn) & year-over-year change (%)

![](images/a04276fca5e986b23736c37fdb81bb441261fc7de9cc591658d36f2ec398d5a6.jpg)  
Source: 659 Group, Data compiled by GS Global Investment Research  
Exhibit 15: Cisco continues to dominate the enterprise switching market Enterprise switching market share by vendor (%)

![](images/20336c7a31a0e61129c80f8f6041f24f571e9f94c9a7757b7ccafe2c639cee34.jpg)  
Source: 650 Group, Data compiled by GS Global Investment Research

Exhibit 16: The enterprise WLAN (indoor & cloud) market should grow 11% year-over-year in 2026, though should decelerate to MSD% annual growth thereafter
WLAN market revenue (\$, mn) & year-over-year change (%)  
![](images/dbe198841ac438703d5eec904b1de6466b03cfffaf5405ba1f095903bb4b341d.jpg)  
Source: 650 Group, Data compiled by GS Global Investment Research  
Exhibit 17: Cisco leads the Enterprise WLAN (indoor & cloud) market at $36\%$ , followed by HPE Aruba at $20\%$ , Huawei $(13\%)$ , and Ubiquiti $(8\%)$ WLAN (indoor + cloud) market share by vendor $(\%)$

![](images/92face97426902439419646975af0b6de3bb821900be985bdbc125d71c192e86.jpg)  
Source: 650 Group, Data compiled by GS Global Investment Research

Exhibit 18: Wi-Fi 7 grew its share of the total Enterprise WLAN market (including cloud) to 39% of total market revenue in 1Q26 and should grow its share towards \~60-70% by 4Q26-1Q27
Enterprise WLAN revenue by infrastructure type (\$, mn)  
![](images/19f2be93954316e8b722509f659f795870d820f1fa43e1c0054bb69f5cc67a24.jpg)  
Source: 650 Group, Data compiled by GS Global Investment Research

Exhibit 19: Within the WiFi 7 market, Cisco was the biggest sequential share gainer in 1Q26 (+6 pp to 31% share), followed by HPE which gained \~2 pp share (18%)
Wi-Fi 7 revenue by vendor (\$, mn)  
![](images/cb52f8dfe6af951b07ce192b67ef640a74cdd60fb37f03e404ce69a2cf7c9356.jpg)  
Includes select vendors  
Source: 650 Group, Data compiled by GS Global Investment Research

## Historical stock performance around earnings

Exhibit 20: Across our networking coverage, all companies outperformed SPX  
C2Q26 stock performance  
![](images/18c3baf66ee89624647d858ec58c289450394f4190f66aa3e4cf9d3cca15544a.jpg)  
Source: FactSet

Exhibit 21: With CLS most deviated from its 1Y average P/E (NTM) multiple  
P/E (NTM) multiples across networking companies  
![](images/525c74d9195692a8db87cde3a24a5beabcb912d25ae7ca556ff9467e17801ac3.jpg)  
Source: FactSet

Exhibit 22: Across our networking coverage, ANET has the strongest historical average performance in the two weeks leading up to earnings (but flat performance day of) while HPE has the strongest performance on the day following earnings (but worst average performance leading up to the print)  
Historical stock performance around earnings

<table><tr><td></td><td colspan="3">Performance</td></tr><tr><td>CSCO</td><td>2 wks prior</td><td>Earnings</td><td>2 wks after</td></tr><tr><td>F3Q26</td><td>(14.9%)</td><td>13.4%</td><td>(12.1%)</td></tr><tr><td>F2Q26</td><td>8.1%</td><td>(12.3%)</td><td>(7.7%)</td></tr><tr><td>F1Q26</td><td>(2.8%)</td><td>4.6%</td><td>(3.6%)</td></tr><tr><td>F4Q25</td><td>2.9%</td><td>(1.6%)</td><td>(3.0%)</td></tr><tr><td>Average</td><td>(1.7%)</td><td>1.0%</td><td>(6.6%)</td></tr><tr><td>ANET</td><td>2 wks prior</td><td>Earnings</td><td>2 wks after</td></tr><tr><td>C1Q26</td><td>20.2%</td><td>(13.6%)</td><td>1.6%</td></tr><tr><td>C4Q25</td><td>3.7%</td><td>4.8%</td><td>9.6%</td></tr><tr><td>C3Q25</td><td>24.4%</td><td>(8.6%)</td><td>(5.0%)</td></tr><tr><td>C2Q25</td><td>(11.0%)</td><td>17.5%</td><td>(7.1%)</td></tr><tr><td>Average</td><td>9.3%</td><td>0.0%</td><td>(0.2%)</td></tr><tr><td>CLS</td><td>2 wks prior</td><td>Earnings</td><td>2 wks after</td></tr><tr><td>C1Q26</td><td>10.8%</td><td>(14.4%)</td><td>(13.4%)</td></tr><tr><td>C4Q25</td><td>16.8%</td><td>(13.1%)</td><td>(10.2%)</td></tr><tr><td>C3Q25</td><td>(12.4%)</td><td>8.2%</td><td>(13.5%)</td></tr><tr><td>C2Q25</td><td>(15.3%)</td><td>16.5%</td><td>(6.4%)</td></tr><tr><td>Average</td><td>(0.0%)</td><td>(0.7%)</td><td>(10.9%)</td></tr><tr><td>HPE</td><td>2 wks prior</td><td>Earnings</td><td>2 wks after</td></tr><tr><td>F2Q26</td><td>(4.1%)</td><td>19.5%</td><td>(29.8%)</td></tr><tr><td>F1Q26</td><td>(2.3%)</td><td>(3.3%)</td><td>(8.3%)</td></tr><tr><td>F4Q25</td><td>(4.3%)</td><td>1.9%</td><td>(12.6%)</td></tr><tr><td>F3Q25</td><td>(7.7%)</td><td>1.5%</td><td>(7.8%)</td></tr><tr><td>Average</td><td>(4.6%)</td><td>4.9%</td><td>(14.6%)</td></tr><tr><td>FFIV</td><td>2 wks prior</td><td>Earnings</td><td>2 wks after</td></tr><tr><td>C1Q26</td><td>(0.3%)</td><td>3.4%</td><td>(4.0%)</td></tr><tr><td>C4Q25</td><td>(1.5%)</td><td>0.3%</td><td>(5.5%)</td></tr><tr><td>C3Q25</td><td>(6.1%)</td><td>2.0%</td><td>(7.2%)</td></tr><tr><td>C2Q25</td><td>(4.6%)</td><td>1.7%</td><td>2.2%</td></tr><tr><td>Average</td><td>(3.1%)</td><td>1.8%</td><td>(3.6%)</td></tr></table>

2 weeks prior & after refers to 10 workdays before and after the earnings print  
Source: FactSet

## Rating, price target, valuation, and key risks

## Arista Networks Inc (ANET, Buy)

We are Buy-rated on ANET with a 12-month target price of \$196 (unchanged) based on 36X (unchanged) our NTM+1Y EPS.

Key downside risks include slower cloud capex spending; customer concentration, with META and MSFT representing 16% and 26% of total revenue in 2025 respectively; competition, including from Cisco, major Chinese providers Huawei & H3C and whitebox switching solutions; margin degradation from investment in enterprise sales force, elevated costs associated with supply chain headwinds; broader pricing pressure from commoditization of networking hardware; inability to execute on enterprise/campus strategy & development of new SD-WAN platform.

## Cisco Systems, Inc (CSCO, Neutral)

We are Neutral-rated on CSCO with a 12-month target price of \$125 (unchanged) based on 25x (unchanged) our NTM+1Y (Q5-Q8) EPS.

Key upside risks include secular tailwinds including hybrid work, multi-cloud network architecture adoption, broader roll-out of WiFi 6/6E and 5G, increasing edge compute use cases; New disaggregated consumption models to target previously underserved cloud providers, near-term revenue visibility from elevated backlog; downside risks include competition, including from major Chinese providers Huawei & H3C and White Box solutions; margin degradation from mix shift into more cloud customers, elevated costs associated with supply chain headwinds; broader pricing pressure from commoditization of networking hardware; dilutive acquisitions.

## Hewlett Packard Enterprise Co. (HPE, Buy)

We are Buy rated on HPE with a 12-month target price of \$79 (unchanged) based on 18x (unchanged) our NTM+1Y EPS.

Key risks: (-) Lower-than-expected corporate IT spending and data center capex could result in worse-than-expected hardware sales; (-) Competition from white box manufacturers could result in cannibalization in HPE's server market share; (-) Market share loss from customer churn during Juniper integration; (-) Component costs could be higher than expected, resulting in worse gross margins; (-) Corporate actions from strategic investors; (-) Failure to deliver market share gains in storage driven by a strategy shift towards selling more owned-IP storage products that carry higher gross margins; (-) Worse-than-expected demand for enterprise and sovereign AI data center infrastructure.

## Celestica Inc (CLS, Buy)

We are Buy rated on CLS with a 12-month target price of \$475 (unchanged), reflecting 28X (unchanged) our NTM+1Y EPS.

Key downside risks include: (-) continued competition from branded data center equipment OEMs and ODMs, which could pressure market share; (-) AI server market competitive intensity, which can pressure AI server margi

[中间内容因长度限制已省略]

including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS.

This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
