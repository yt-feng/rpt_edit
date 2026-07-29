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
# ASIA ECONOMICS ANALYST

# Gen-AI in India: Jobs Crosswinds, Productivity Tailwinds

Generative Artificial Intelligence (Gen-AI) is likely to have wide-ranging effects on the macroeconomy. In our baseline view, we see the adoption of Gen-AI as a medium-term positive for India's growth outlook, even as the labour market effects are likely to be uneven.

\- More complement than substitute: Extending our global team's methodology, we estimate that Gen-AI could perform 9-17% of the tasks currently undertaken by India's non-agricultural workforce, depending on assumptions about the level of task complexity that it can perform. We further classify occupations by the share of task content exposed to Gen-AI: occupations with high exposure are more likely to face substitution, while those with moderate exposure are more likely to be complemented. Weighting these occupations by employment across sectors, we estimate 8-12% of non-agricultural employment is at risk of substitution, while 42-48% of non-agricultural employment is likely to be complemented, with the balance remaining largely unaffected.

Gen-AI likely to reshape the composition of occupations: Based on occupation-level analysis, we estimate employment declines are likely to be concentrated in occupations like routine clerical support, professional and technician. Meanwhile, routine-physical occupations, followed by craft and trade-related workers and machine operators, may see an increase in employment, as physical, manual and interpersonal tasks remain difficult to automate.

■ Exposure is concentrated in services: Healthcare, education, financial and professional services appear more exposed to AI-related augmentation through diagnostics and data analytics, while IT-enabled business-process services (BPS) and postal & telecom services face greater substitution risk given their concentration in repetitive, codifiable tasks. Manufacturing is less directly affected given the more physical task mix. An important caveat is that Gen-AI adoption, as with earlier technology cycles, is also likely to create new job categories over time, which is outside the scope of this report.

Productivity gains could be meaningful, but timing is difficult to predict: Our baseline suggests Gen-AI adoption could lift annual labour-productivity growth by around 0.4pp over a 10-year period, with a wider range of 0.1pp to 0.8pp depending on the complexity of tasks that it is able to perform.

## Santanu Sengupta

+91(22)6616-9042 | santanu.sengupta@gs.com GS India SPL

Arjun Varma
+91(22)6616-9043 |
arjun.varma@gs.com
GS India SPL

Andrew Tilton
+852-2978-1802 |
andrew.tilton@gs.com
GS (Asia) L.L.C.

Knowledge-intensive services i.e. healthcare, education, media, parts of financial and professional services look best placed to benefit, while gains in construction and manufacturing are likely to be limited.

\- Sequencing of adoption will matter. The main productivity upside is likely to come from broad-based deployment across firms. If deployment of labour-augmenting Gen-AI is prioritized before substitution-intensive deployment, productivity gains would likely broaden before labour-market disruption becomes more visible.

Global capability centre (GCC) resilience may cushion substitution risks to routine business services. In our view, while routine IT-BPS functions face substitution risk, aggregate tech sector employment (around 2% of non-agricultural employment), services exports, and GCC expansion remain resilient, as of now. We find that headcount rationalization has been concentrated in the top 6 IT services firms (net employment reduction around 64k out of 1.7mn), while the rest of the technology services sector (including the GCCs) have added around 0.7mn headcount to reach 4.4mn over the last three years.

## Key risks to our baseline view:

Infrastructure remains a key constraint. India's Gen-AI diffusion will depend not just on software capability, but also on compute affordability, data-centre buildout, reliable power, water availability, and broader digital infrastructure. With India's current data-centre capacity of only around 1GW (1% of global data centre capacity), scaling AI adoption will require substantial investment in both physical and digital infrastructure.

Rising protectionism in destination markets for services exports. Beyond the usual dependence on global ICT spending, a more restrictive policy environment around cross-border data, digital services, and the use of foreign AI models could weigh on services export growth. For example, the EU has tightened scrutiny of cross-border data transfers, while the US has increasingly emphasized AI sovereignty, potentially advocating for restriction of deployment of Gen-AI models outside the US.

## Gen-AI Adoption in India: More Complement Than Substitute

The rapid advancement of generative artificial intelligence (Gen-AI) marks the latest in a series of technological advancements that have shaped India's growth and labor markets over recent decades. In this Asia Economics Analyst, we place the current Gen-AI adoption in the context of India's past technology adoption cycles and assess the Indian labor market's potential exposure to Gen-AI and the scope for productivity gains from the Gen-AI adoption. We further document Gen-AI-related capex in India, including data centres, semiconductor chips and digital infrastructure. Finally, we explore what Gen-AI adoption could look like in India – specifically, compute and physical infrastructure requirements needed to scale Gen-AI use across its 1.4bn population.

## History of Internet and Technology Developments in India

India's past technology adoption accelerated when connectivity costs fell and digital infrastructure scaled. In our view, Gen-AI adoption is likely to follow a similar path, with the pace and breadth of diffusion depending on cheaper compute, reliable power, and the build-out of supporting digital and physical infrastructure. India's digital evolution moved through successive infrastructure-led phases – from an early internet phase that was limited and rationed, to mobile and mobile internet adoption, and then to the build-out of digital public infrastructure (Exhibit 1). Over the last ten years, the expansion of the India Stack $^{1}$ , broader smartphone penetration (Exhibit 2), and a sharp decline in mobile data costs have materially broadened digital access and usage.

Exhibit 1: The number of Aadhar cards (digital identification) issued has grown significantly since their launch  
![](images/69758fdbf08e7407c4febe797e7d431fad86336c8e28d18aeaf59268f6db2414.jpg)  
Source: UIDAI

Exhibit 2: India's smartphone penetration has more than doubled in the last decade  
![](images/0a27c2ba7cb1524b5fb9d21eec83d27ee659814905ce903add64d751b33fc620.jpg)  
Source: Various news articles, GS Global Investment Research

Globally competitive digital services: These technology cycles also helped create a globally competitive digital services ecosystem. The rise of the Information Technology-Business Process Management (IT-BPM) sector embedded India more deeply into global services value chains, built a digitally skilled workforce, and reinforced the role of infrastructure and affordability as key enablers of technology diffusion. Affordable mobile internet and rising smartphone penetration also enabled the emergence of food delivery platforms in India, which scaled on digital commerce.

![](images/e9ea5e22d9bf8e8919dd88faff687b627d5a75251b2f326dbd272fa295252dd4.jpg)  
Source: GS Global Investment Research

Prior technology waves in India were enabled by falling connectivity costs and scalable digital infrastructure. In our view, Gen-AI adoption is likely to depend similarly on compute affordability, power availability, and supporting digital infrastructure. At the same time, Gen-AI capabilities appear to be advancing materially faster than in earlier technology cycles, with recent models moving well beyond basic text generation toward a broader set of routine knowledge-based tasks, that are difficult to distinguish from human output. This unusually rapid improvement has important implications for India's labour market, and also points to potentially meaningful productivity gains, particularly across service-oriented and knowledge-intensive sectors.

## Labour Market Impact from Gen-AI in India

To analyze these implications, we first examine the extent to which the Indian labour market is exposed to Gen-AI adoption, and then assess the degree to which it can augment the existing workforce.

We estimate Gen-AI's potential labour-market impact by combining task-level Occupational Information Network (O\*NET) data with International Labour Organization (ILO) occupation-level employment data for India. We begin with O\*NET, which contains information on approximately 900 occupations and 39 underlying work activities, in the US. We identify 13 of these 39 work activities as exposed to Gen-AI-related automation (Please see Appendix 1 for details) and use the associated task difficulty levels (on a 1-6 scale) $^{2}$ to construct a Gen-AI exposure score for each occupation, as per our global economics team's methodology.

Specifically, we take a complexity-weighted average of the tasks to estimate the share of each occupation's task content potentially automatable by Gen-AI. In our baseline, we assume that the difficulty assigned to similar tasks is similar across the US and India.

For instance, tasks like “Studying scripts to determine project requirements”, “Monitoring financial performance” are assigned a difficulty level 2, while tasks like “Monitoring a patient during treatment” or “Analyzing data to identify trends and relationships between variables” or “Research topics in area of expertise” are assigned a difficulty level of 6 (Please see Appendix 1 for details).

We then aggregate and map the occupation-level exposure scores to India's occupation structure using employment data from the ILO, which is available at the National Classification of Occupations (NCO) 2015 Division-1 occupational level (e.g., Managers, Professionals, Technicians and Associate Professionals, Clerical Support Workers, and others).

The ILO database also provides the distribution of these occupations across 22 broad sectors, allowing us to estimate the share of each sector's workload that is potentially exposed to Gen-AI. Since employment data for India are available only at the broad NCO-2015 Division-1 occupational level, we average the occupation-level Gen-AI exposure scores across the underlying sub-divisions to arrive at the exposure scores at the NCO-2015 Division 1 level, resulting in a narrower distribution of AI exposure score than at the more granular occupation level (Exhibit 4).

Finally, we aggregate these estimates across occupations and sectors to estimate the share of the economy's total task content that could potentially be exposed to Gen-AI-related automation and augmentation. In our baseline, we assume that occupations involving predominantly physical or outdoor tasks—such as in agriculture—have no exposure to Gen-AI-driven automation.

Exhibit 4: Framework for estimating the share of employment potentially exposed to Gen-AI-related automation  
![](images/fd698e663f1692360c9fe59572ebfdea08b72f92d40d49dad693276862345f64.jpg)  
Source: GS Global Investment Research

Gen-AI exposure scores vary across occupations, ranging from around 2% to 40% of task content depending on both the occupation and the level of task complexity Gen-AI is able to automate. We first weight these occupation-level exposure scores by employment to derive sector-level estimates of the share of task content exposed to Gen-AI. We then weight each sector's exposure by its employment share in the overall economy to estimate the economy-wide share of tasks exposed to Gen-AI-related automation.

Under our baseline, if Gen-AI can complete tasks of difficulty levels up to 3-4, such as “monitor organizational compliance with regulations” (difficulty level 3), “examine financial records” (difficulty level 3) or “analyzing trends and relationships in data” (difficulty level 4), then we estimate that around 13-15% of non-agricultural work tasks are exposed to Gen-AI-related automation. Exposure is high in the services sector, with education, media, and financial and professional services $^{3}$ . Meanwhile, more physically intensive sectors such as construction show relatively low task exposure ( $\sim$ 8%) (Exhibit 5).

Exhibit 5: Services sector has the highest share of tasks exposed to Gen-AI related automation Note where is tech services sector

![](images/410e93f4009349676b53aa9be7f617831869a8dacca5fd50b4020e811d0eea46.jpg)  
Note: i) ED: Education, ME: Media, HC: Health care, PS: Public services, FS: Financial services, HO: Hotels, UT: Utilities, CH: Chemicals, TS: Transport services, TX: Textiles.  
ii) ILO's classification includes computer programming, information services and parts of consultancy activities in media, while parts of consultancy and professional services in financial services

## Source: O\*NET database, ILO, GS Global Investment Research

We construct alternative scenarios by varying the difficulty threshold of tasks that Gen-AI can automate. If Gen-AI is able to perform only lower-complexity tasks (up to difficulty level 2), the share of tasks exposed to Gen-AI declines significantly to 9%. Meanwhile, if Gen-AI is capable of performing more complex tasks (up to difficulty level 6), the share of tasks exposed to AI rises to 17% (Exhibit 6).

Even under the upper-bound scenario, economy-wide share of tasks exposed rises only to around 17% for two reasons. Firstly, our framework identifies only a subset of work activities as potentially automatable by Gen-AI, while the remainder predominantly involve physical execution, interpersonal interaction or supervision that continue to require human input. Secondly, occupations with relatively high Gen-AI exposure scores—such as clerical support workers and technicians—are concentrated in sectors with a relatively low share in overall non-agricultural employment in the economy.

Exhibit 6: Based on our estimates around $9 - 17\%$ of India's current work tasks may be exposed to Gen-AI automation

![](images/e289d157bdc7f538a7dcfbaf8a183a148c46b18e6d9a85f296bc01e5ea716d80.jpg)  
ILO's classification includes computer programming, information services and parts of consultancy activities in media, while parts of consultancy and professional services in financial services

Source: GS Global Investment Research

## More complement than substitute

We estimate that around 9–17% of India’s non-agricultural tasks are exposed to Gen-AI driven automation, but the labor-market impact will depend on how much of each occupation’s task content can be automated. Where exposure is limited, Gen-AI is more likely to complement workers by reducing time spent on routine tasks and freeing capacity for higher-value work. Where exposure is higher, substitution risks rise. Meanwhile, occupations dominated by physical tasks are likely to remain unaffected.

To illustrate this, we group workers into five broad categories: routine and administrative workers (clerical support), who face the greatest substitution risk; top-management employees (managers), who are more likely to be complemented; professionals, technicians and service and sales workers, who face a mixed outcome $^{4}$ ; and blue-collar and manual workers $^{5}$ , who should see more limited direct impact from Gen-AI adoption.

At the sector level, healthcare, education, media and entertainment, and parts of financial services appear more likely to benefit from labor augmentation, reflecting their relatively higher share of skilled work

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
