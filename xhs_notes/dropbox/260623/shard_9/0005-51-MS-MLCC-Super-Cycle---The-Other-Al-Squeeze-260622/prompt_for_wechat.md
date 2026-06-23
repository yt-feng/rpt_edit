你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`摩根斯坦利`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
<table><tr><td colspan="2">MS &amp; CO. INTERNATIONAL PLC, SEOUL BRANCH+</td></tr><tr><td colspan="2">Ryan Kim</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Ryan.G.Kim@morganstanley.com</td><td>+82 2 399-4939</td></tr></table>

June 22, 2026 03:46 PM GMT

Asia Technology | Asia Pacific

# MLCC Super Cycle – The Other AI Squeeze

WHAT'S CHANGED

<table><tr><td>Samsung Electro-Mechanics (009150.KS)</td><td>From</td><td>To</td></tr><tr><td>Price Target</td><td>W920,000</td><td>W2,560,000</td></tr></table>

AI is shifting from semiconductors to MLCCs, creating a supply-demand mismatch in high-end components. TAM is set to expand, driven by compute, power, and networking needs. The key question is not if supply tightens, but how long constraints could persist.

What's changed? AI computing platforms are driving a surge in capacitor demand – a single AI server consumes \~440,000 MLCCs, 10–15x more than traditional servers. Producers are reallocating capacity toward high-growth, high-margin AI applications, reducing flexibility in other segments. Demand is shifting from volume to quality, with a focus on high-value solutions and long-term supply lock-ins for AI data centers.

Why it matters? We estimate AI-driven MLCC demand will more than quadruple between 2025 and 2030, while total capacity grows only 10%-15% annually. AI-grade supply already runs ahead of current capacity, with premium high-reliability and high-voltage lines effectively booked out for multiple years. AI platforms now compete directly with consumer, automotive, and industrial applications for advanced materials, heightening supply risk for traditional customers.

Cycle upturn – early innings. Supply concerns extend beyond near-term shortages, with longer-term supply agreements becoming more common. Key indicators to monitor include: (1) evolving AI specifications, (2) sharp reversals in book-to-bill ratios, (3) pricing momentum (YoY), and (4) AI server demand.

Stock implications. We raise our SEMCO earnings estimates and PT following recent AI customer commitments (ABF substrates, embedded MLCCs, silicon capacitors, and potential glass substrates). In Taiwan, we favor Yageo, which benefits from capacity shifting away from commodity MLCCs. In Japan, we favor Murata on rising AI exposure, while we expect Taiyo Yuden to underperform due to elevated expectations.

MS & CO. INTERNATIONAL PLC+

Shawn Kim
Equity Analyst
Shawn.Kim@morganstanley.com +44 20 7677-1018

MS ASIA LIMITED+

Duan Liu
Equity Analyst
Duan.Liu@morganstanley.com +852 2239-7357

MS & CO. INTERNATIONAL PLC+

Cindy Huang
Equity Analyst
Cindy.Huang@morganstanley.com +44 20 7425-2915

Asia Summer School 2026

![](images/8da57f99381536e42718bca47719add670300f0811d3175c48d80ab23b536db2.jpg)

S. KOREA TECHNOLOGY

Asia Pacific

Industry View

Attractive

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Executive summary

The MLCC industry today feels like the legacy DDR4 DRAM two years ago, which experienced unprecedented, AI-driven supply constraints, triggering structural price hikes. These shortages arose as leading DRAM manufacturers redirected fixed capacity toward higher-margin AI hardware (e.g., HBM), away from legacy products. We see several reasons why MLCC constraints are structural this time:

\- Existing MLCC capacity (e.g., EV-related) is not fungible with AI servers, given large differences in specifications, packaging, power conversion, and capacitance–voltage requirements.

\- Long lead times. Greenfield MLCC capacity requires \~2 years from commitment to production. Unlike semiconductors, equipment is customized in-house, limiting rapid efficiency gains.

\- New wave of agentic AI demand. Inference growth and the CPU-intensive nature of agentic AI add incremental demand beyond GPUs. Technology: Rise of the AI Agent – Global Implications (19 Apr 2026)

\- Required returns. Manufacturers require sustained pricing upside to justify new capacity; most target output growth of \~10%–15% p.a. while avoiding speculative investment.

\- High entry barriers. High-capacitance, low-ESL MLCCs for servers and autos face strict qualification constraints, limiting competition from lower-end producers.

\- 2026 vs. 2017. The commodity part of the MLCC industry will likely face shortages similar to the 2017-18 super cycle driven by a demand surge from EV adoption and smartphone content (5G and iPhone), although current dynamics are more structural, supported by durable AI demand.

## What's changed?

How AI is impacting MLCCs? MLCCs are evolving from commodity components into strategic resources. The focus has shifted from quantity to increasingly complex technical requirements, including closer system integration, higher capacitance density, and AI-specific power architectures.

\- Content surge: AI servers require \~8–13x more MLCCs than traditional servers, driven by rapid load changes and the need for stable multi-rail power delivery. MLCCs play a critical role in decoupling and noise suppression due to fast response at high frequencies.

\- Volume surge. NVIDIA's GB300 platform uses \~320,000 units per full cabinet, \~30x the consumption of a high-end smartphone. The upcoming Vera Rubin platform implies \~1.8x higher content value.

\- Specs surge. AI GPUs require ultra-low ESR and minimal ESL to manage nanosecond transient responses and prevent system instability under high-load conditions.

\- Tiny but mighty. Limited board space increases the importance of small-size, high-capacitance MLCCs, making advanced materials science a key competitive differentiator.

Embedded MLCC – a new trend addressing multiple issues. Embedded MLCCs are emerging as a key design feature in AI servers. They facilitate current flow and reduce power loss by integrating power supply circuits within ABF substrates, shortening the distance to semiconductor chips. This enables efficient vertical power delivery, reduces losses, and frees board space for additional components.

Multilayer substrates in AI servers use copper interconnects, requiring embedded components to be copper-plated for effective bonding. Embedded MLCCs feature flat surfaces that improve substrate integration and reliability. This design also increases usable board space, supporting higher component density.

Exhibit 1: Embedded MLCC architecture  
![](images/4f5756f3635401229acdfff263bce014aa49ee2818cedb052d4f273ee7d5605f.jpg)  
Source: Samsung Electro-Mechanics

The importance of AI server power integrity. AI servers increasingly require high-performance power supply circuits, driving demand for MLCCs capable of handling higher current and enabling more efficient power delivery. This shift is reshaping power solutions toward high-density integration of electronic components within constrained spaces, supporting enhanced system performance.

Exhibit 2: MLCC evolution in AI servers  
![](images/b809d2ee77cdcb2fc7429069582c43afc0a80f9a0f305866bdf38ffd428d868c.jpg)  
Source: Taiyo Yuden

## Channel Checks

Our recent channel checks point to 200%–300% price increases at distributors since 1Q26 (vs. a 10x peak in 2017) and direct sales up to 30% QoQ.

\- Spot pricing: The Huaqiangbei spot market in Shenzhen has seen significant price increases since early May. Initially concentrated in high-capacitance products, increases have spread to consumer grades. Distributor pricing to spot customers has risen 2–10x for some specifications (e.g., 0805 27uF up \~6x YTD), from cycle trough levels over the past two years.

\- Contract pricing: Leading suppliers have raised distributor pricing by 20%–30% QoQ in 2Q26. Some have removed volume discounts and stopped accepting orders at 1Q low prices. Distributors expect further price increases in 3Q26 and are actively negotiating LTA-like agreements to secure supply.

\- Inventory: Supply chain inventory remains lean after two years of destocking. Distributors hold \~1.5 months of inventory on average, while downstream customers hold less than one month.

\- Is this hype? Distributors do not expect meaningful demand growth from consumer applications and note that some extreme price increases (10–20x) reflect inventory hoarding by traders in Huaqiangbei rather than end demand. However, with lean inventories and leading suppliers reallocating capacity toward Al-grade products, distributors expect a more durable trend vs. the short-lived tariff-driven spike in early 2025.

## Still early in the cycle?

The market has moved beyond a typical commodity cycle into structural competition in materials science, precision manufacturing, and supply chain resilience. Lead times exceed 20 weeks for high-end products, and pricing dynamics are shifting from cyclical volatility to structurally elevated premiums for strategic AI components. High-end shortages remain real, while distributors have begun precautionary stockpiling of standard X5R products – a segment not currently in shortage.

Exhibit 3: Taiwan monthly MLCC sales – cycle edging up with May +40% YoY  
![](images/9ae66f632df8cdc73d361811dc0b8fb05b31ab75629eb6916105bac302dde2e8.jpg)  
Source: Company data, MS

## Market structure

Who dominates? The high-end AI MLCC market is dominated by a Japanese-Korean duopoly, with a combined 85% market share.

\- Murata (45% share): As the industry benchmark, Murata's AI server orders are running at \~2x capacity, with utilization at 90%–95%. Its competitive edge stems from vertical material integration and leadership in ultra-small 008004 form factors.

\- Samsung Electro-Mechanics (40% share): SEMCO has narrowed the gap with Murata by pivoting from low-margin consumer electronics to higher-margin AI and automotive segments. Its Tianjin plant is operating at full capacity to meet global demand.

\- Other key players including TDK, Taiyo Yuden, and Yageo focus on high-voltage and specialized industrial modules. Chinese firms like CCTC (San Huan Group) are entering domestic server supply chains. Commodity-grade producers, including Walsin Tech in Taiwan and Guangdong Fenghua Advanced Technology, Chaozhou Three-Circle and Eyang Technology in China, primarily serve consumer electronics.

\- Kyocera AVX is strongly positioned in automotive and industrial segments, while Vishay Intertechnology offers a broad capacitor portfolio.

## Stock implications

MLCC has lagged the broader AI trade but has delivered strong returns since the onset of agentic AI (Yageo +379% YTD, SEMCO +763% and Fenghua +355%). We remain constructive despite the rally, as price increases are broadening beyond spot markets, while book-to-bill ratios and utilization continue to improve. AI and data center demand are pulling scarce high-end MLCC capacity away from standard applications.

We recommend SEMCO supported by \~20% potential upside to our price target and its still reasonable valuation at 1.4x P/B vs. historical average of 1.7x.

In Taiwan, Howard Kao continues to prefer Yageo OW for its business transformation growth story (link). Yageo's preliminary May earnings tracked ahead of expectations with supply chain checks pointing to substantially stronger pricing in 2H26.

In Japan, Shoji Sato believes Murata OW will benefit most from increased demand and product mix improvements, while Taiyo Yuden UW may only see modest benefits from improved mix, driven by compact larger-capacity products. Electronic Components: Murata Mfg Now Our Top Pick, Lowering Taiyo Yuden to UW (16 Jun 2026).

Exhibit 4: MLCC Bull-Base-Bear risk reward analysis  
![](images/105faf42e9d2ae5fa2c03db37dc0884ace5109145c2068aab4c50e4d01cdf5fa.jpg)  
Source: Factset, MS. Note: X-axis (Base Return/Vol) represents our base case price target return divided by 10-year realized volatility (RV10y). Y-axis (Skew) represents the sum of our bull and bear case returns divided by RV10y, capturing payoff asymmetry.

## Key Charts

Exhibit 5: MLCC remains one of the best performing segments within Asia Tech YTD  
![](images/a82da493389ffd5f9fa94d231f38f717848a9a14930be4e3e5bcb92c5bfaa557.jpg)  
Source: Factset, MS

Exhibit 6: SEMCO outperform MLCC peers YTD  
![](images/c1b91b3dca79bc86214cf90f6ecc538747bffd76213df7f161ab94a78064f99f.jpg)  
Source: Factset, MS

Exhibit 7: MLCC group now trading at 9.6x NTM P/B vs.

historical average of 1.7x  
![](images/ca65ee02738a64c50f735985671bfb13ff00861ee65cd01d5681cd19199d0ef2.jpg)  
Source: Factset, MS

Exhibit 8: Taiwan monthly MLCC sales – cycle edging up with May +40% YoY  
![](images/d22c5da26c6fbd8cb73668ec2339d775eda5818d6bf7fa2dbe3a88b3dcff144d.jpg)  
Source: Company data, MS

Exhibit 9: Earnings revision breadth has bounced back since Oct-25 and is moving to positive territory  
![](images/73feaa7c9371e73a412235f6df12505b8aedabb68bf738263f3752ade2add943.jpg)  
Source: Factset, MS

Exhibit 10: EPS revision YTD  
![](images/1659adffb0d0894f9dcb22db9f38853fcde59215175b3c2f10a8e89c4f3b2fa0.jpg)  
Source: Factset, MS

## Will AI Impact MLCC?

MLCCs (multilayer ceramic capacitors) are critical components in modern electronic systems, serving as local energy reservoirs that stabilize voltage and suppress noise in electronic circuits. In AI servers, MLCCs are particularly important because GPUs, CPUs, ASICs, and FPGAs operate at very low voltages and switch on and off within nanoseconds, creating significant transient current demands and voltage fluctuations.

Positioned close to these processors, MLCCs provide immediate charge delivery to support rapid current spikes while simultaneously filtering high-frequency noise. Their inherently low equivalent series resistance (ESR) and low equivalent series inductance (ESL) enable them to respond to the nanosecond-scale current fluctuations associated with AI accelerators, making them indispensable for maintaining power integrity.

The importance of MLCCs has increased as semiconductor process nodes continue to shrink. Lower operating voltages improve computing performance and power efficiency but also reduce voltage tolerance, meaning even small voltage deviations can impair chip functionality. At the same time, AI workloads are driving higher processor power consumption, increasing the need for local decoupling capacitance. Given board space constraints, this creates sustained demand for smaller, higher-capacitance MLCCs.

Content Growth: AI Drives a Step-Function Increase in MLCC Consumption. AI accelerators are transient-current hungry — high di/dt, very low operating voltages — so designers pack far more local decoupling capacitance around the die to hold power integrity. At the board level, an AI server mainboard carries an estimated 15,000-25,000 MLCCs, roughly 10x a general server. That scales sharply at the system level: a fully configured Rubin NVL72 rack runs \~570k MCCs vs\~320k for GB300, with total dollar content per rack up \~182%.

Mix Upgrade: AI Demand Favors High-Value MLCCs. The AI opportunity is not only about higher unit consumption but also a significant shift toward more technologically demanding products. Demand is increasingly concentrated in small-form-factor, high-capacitance, high-temperature, and low-ESL MLCCs that are optimized for accelerator power delivery. In particular, 47μF+ high-capacitance MLCCs are becoming a larger portion of AI server bill-of-materials requirements, accounting for more than 30% of units in Rubin-generation platforms versus less than 20% in GB300 systems. We estimate cloud AI demand for 47μF+ MLCCs could expand from \~4bn units in CY25 to\~38bn units by CY30. This mix shift toward premium products is likely to be a more durable driver of industry ASPs than cyclical pricing movements.

Capacity Intensity: AI Creates Disproportionate Capacity Consumption. High-cap AI MLCCs need several hundred to over a thousand dielectric layers, so each part eats a disproportionate share of capacity relative to its unit count. Even at only \~3% of industry units and \~5% of revenue by CY27, AI absorbs far more capacity than that. As the leaders shift toward AI, supply tightens and pricing firms across everything else. That's what the channel data is now showing.

Exhibit 11: VR200 MLCC unit demand is rising to 570K+, up close to 80% vs a GB300 rack

<table><tr><td colspan="2">Server Assumptions</td><td colspan="2"># of MLCCs</td><td colspan="2">US$</td></tr><tr><td colspan="2">General server</td><td colspan="2">2,000</td><td colspan="2">30</td></tr><tr><td colspan="2">HGX Hopper AI server (8x GPU)</td><td colspan="2">22,000</td><td colspan="2">190</td></tr><tr><td>GPU module (OAM)</td><td>8x</td><td>1,300</td><td>10,400</td><td>10</td><td>80</td></tr><tr><td>GPU baseboard (UBB)</td><td>1x</td><td>4,900</td><td>4,900</td><td>45</td><td>45</td></tr><tr><td>CPU motherboard</td><td>1x</td><td>1,500</td><td>1,500</td><td>25</td><td>25</td></tr><tr><td>Peripheral boards</td><td>8x</td><td>650</td><td>5,200</td><td>5</td><td>40</td></tr><tr><td colspan="2">HGX B200 AI server (8x GPU)</td><td colspan="2">36,000</td><td colspan="2">317</td></tr><tr><td>GPU module (OAM)</td><td>8x</td><td>3,000</td><td>24,000</td><td>24</td><td>192</td></tr><tr><td>GPU baseboard (UBB)</td><td>1x</td><td>5,300</td><td>5,300</td><td>60</td><td>60</td></tr><tr><td>CPU motherboard</td><td>1x</td><td>1,500</td><td>1,500</td><td>25</td><td>25</td></tr><tr><td>Peripheral boards</td><td>8x</td><td>650</td><td>5,200</td><td>5</td><td>40</td></tr><tr><td colspan="2">HGX B300 AI server (8x GPU)</td><td colspan="2">48,000</td><td colspan="2">435</td></tr><tr><td>GPU module (OAM)</td><td>8x</td><td>4,400</td><td>35,200</td><td>40</td><td>320</td></tr><tr><td>GPU baseboard (UBB)</td><td>1x</td><td>6,100</td><td>6,100</td><td>50</td><td>50</td></tr><tr><td>CPU motherboard</td><td>1x</td><td>1,500</td><td>1,500</td><td>25</td><td>25</td>

[中间内容因长度限制已省略]

Research is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The following companies do business in countries which are generally subject to comprehensive sanctions programs administered or enforced by the U.S. Department of the Treasury's Office of Foreign Assets Control ("OFAC") and by other countries and multi-national bodies: Samsung Electronics.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: S. Korea Technology

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/22/2026)</td></tr><tr><td colspan="3">Ryan Kim</td></tr><tr><td>Ecopro BM (247540.KQ)</td><td>U (03/20/2023)</td><td>W166,700</td></tr><tr><td>Fadu Inc (440110.KQ)</td><td>O (09/21/2025)</td><td>W115,900</td></tr><tr><td>Hanmi Semiconductor Co. Ltd. (042700.KS)</td><td>O (08/16/2024)</td><td>W301,500</td></tr><tr><td>HD Hyundai Electric Co Ltd (267260.KS)</td><td>O (03/25/2025)</td><td>W1,033,000</td></tr><tr><td>Isu Petasys Co. Ltd. (007660.KS)</td><td>O (02/03/2025)</td><td>W117,900</td></tr><tr><td>L&amp;F Co Ltd (066970.KS)</td><td>E (04/03/2025)</td><td>W125,700</td></tr><tr><td>Leeno Industrial Inc. (058470.KQ)</td><td>O (04/03/2025)</td><td>W92,400</td></tr><tr><td>Lotte Energy Materials Corp (020150.KS)</td><td>U (04/03/2025)</td><td>W47,550</td></tr><tr><td>LS Electric (010120.KS)</td><td>O (01/22/2026)</td><td>W245,000</td></tr><tr><td>POSCO FUTURE M (003670.KS)</td><td>U (04/03/2025)</td><td>W192,000</td></tr><tr><td>SK IE Technology (361610.KS)</td><td>U (04/03/2025)</td><td>W17,950</td></tr><tr><td>SK Square Co Ltd. (402340.KS)</td><td>O (05/06/2026)</td><td>W1,970,000</td></tr><tr><td>Wonik IPS Co Ltd (240810.KQ)</td><td>O (08/08/2025)</td><td>W172,500</td></tr><tr><td colspan="3">Shawn Kim</td></tr><tr><td>LG Display (034220.KS)</td><td>E (06/11/2025)</td><td>W12,930</td></tr><tr><td>LG Electronics (066570.KS)</td><td>E (04/07/2025)</td><td>W227,500</td></tr><tr><td>LG Innotek (011070.KS)</td><td>E (03/12/2025)</td><td>W1,130,000</td></tr><tr><td>Samsung Electro-Mechanics (009150.KS)</td><td>O (07/31/2025)</td><td>W2,228,000</td></tr><tr><td>Samsung Electronics (005935.KS)</td><td>O (11/18/2019)</td><td>W224,000</td></tr><tr><td>Samsung Electronics (005930.KS)</td><td>O (11/18/2019)</td><td>W353,500</td></tr><tr><td>SK hynix (000660.KS)</td><td>O (09/21/2025)</td><td>W2,919,000</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## © 2026 MS
"""
