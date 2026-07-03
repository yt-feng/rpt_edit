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
<table><tr><td colspan="2">CHINA AUTOS &amp; SHARED MOBILITY</td></tr><tr><td>Asia Pacific Industry View</td><td>In-Line</td></tr></table>

<table><tr><td colspan="2">Daisy Dai, CFA</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Daisy.Dai@morganstanley.com</td><td>+852 2848-7310</td></tr></table>

July 1, 2026 09:00 PM GMT

# China Autos & Shared Mobility | Asia Pacific

# Extending 800V EV Technology into AIDC

## WHAT'S CHANGED

<table><tr><td>Suzhou Recodeal Interconnect System (688800.SS)</td><td>From</td><td>To</td></tr><tr><td>Rating</td><td>Underweight</td><td>Overweight</td></tr><tr><td>Price Target</td><td>Rmb42.14</td><td>Rmb121.00</td></tr></table>

The earlier migration from 400V to 800V EVs in China has cultivated a cohort of high-voltage EV component suppliers. We compare them with global peers and explore new opportunities in 800VDC AI data centers. We double-upgrade Recodeal from UW to OW on revenue upside from AI interconnects.

Maturing 800V EV supply chain in China: 800V EV sales penetration in China has risen from 5% in 2023 to 11% in 2025, cultivating an increasingly mature 800V auto supply chain that could benefit from the emerging 800V high-voltage direct current (HVDC) architecture for AI data centers (AIDC). We explore the opportunities and challenges for auto suppliers in addressing 800V AIDC.

Why few auto suppliers have won orders from 800V AIDC so far? The 800V EV supply chain spans upstream auto semis (silicon carbide, gallium nitride), downstream electronics components (inverters, on-board chargers, DC-DC converters), and auxiliaries (connectors, relays, fuses). The 800V AIDC ecosystem shows a similar structure, from silicon providers to power system components. However, auto suppliers must requalify these technologies to support data centers' 24/7 continuous duty, high power density, hot swap, and very low downtime, which takes time to achieve.

## Common parts best positioned; double-upgrade Recodeal (688800.SS) to OW:

We expect generic high-voltage components, such as semis and connectors, to lead migration from 800V EV to AIDC. We upgrade Recodeal to OW on an AI-driven earnings inflection from 2026, as it expands from EV connectors – where margins faced pressure – into AIDC interconnects such as active electrical cables (AEC) and power whips, where we see strong growth potential. We expect AI interconnects to contribute >40% of Recodeal's revenue in 2027. Yangjie (300373.SZ, covered by Daisy Dai), a leading Chinese power semi supplier, can also benefit from auto localization and power semi price increases.

Tier-1 parts can also benefit but require redesign, Joyson (600699.SS) on watch list: We expect auto tier-1 suppliers such as Joyson to have opportunities to supply DC-DC converters, battery management systems, and power electronics to 800V AIDC, but they must redesign auto-grade products. Similar opportunities have emerged in the US. As highlighted by our US auto analyst Andrew Percoco in his Mobility to Megawatts Primer (3 Jun 2026), several suppliers – Aptiv, Versigent, BorgWarner, Magna, and Lear – can leverage their engineering talent and manufacturing scale to address the 800V AIDC market.

Shelley Wang, CFA
Equity Analyst
Shelley.Wang@morganstanley.com +852 3963-0047

MS & CO. LLC
Andrew S Percoco
Equity Analyst
Andrew.Percoco@morganstanley.com +1 212 296-4322

<table><tr><td colspan="2">Andy Meng, CFA</td></tr><tr><td>Equity Analyst</td><td></td></tr><tr><td>Andy.Meng@morganstanley.com</td><td>+852 2239-7689</td></tr></table>

<table><tr><td colspan="2">MS TAIWAN LIMITED+</td></tr><tr><td colspan="2">Derrick Yang</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Derrick.Yang@morganstanley.com</td><td>+886 2 2730-2862</td></tr></table>

<table><tr><td colspan="2">MS ASIA LIMITED+</td></tr><tr><td colspan="2">Tim Hsiao</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Tim.Hsiao@morganstanley.com</td><td>+852 2848-1982</td></tr></table>

<table><tr><td colspan="2">Joey Xu, CFA</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Joey.Xu@morganstanley.com</td><td>+852 3963-0337</td></tr></table>

<table><tr><td colspan="2">Peggy Wang</td></tr><tr><td>Research Associate</td><td></td></tr><tr><td>Peggy.Pc.Wang@morganstanley.com</td><td>+852 3963-3934</td></tr></table>

![](images/6d67bbc5e5431de454addefb722d5dc3f5e0ad3d371013e46e4b96deda15df70.jpg)

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Who's in the 800V EV supply chain?

## From 400V to 800V EV

800V a more efficient solution for EV: Most EVs historically adopted 400V vehicle architecture. Under Watt's Law, P (power) = U (voltage) × I (current), charging power can increase by raising voltage from 400V to 800V. An 800V architecture helps shorten EV charging time significantly to <10 minutes. It also supports OEM cost reduction as SiC costs decline over time. Compared with battery swapping and high-current fast charging, high-voltage fast charging is more efficient, as it reduces resistive heating and simplifies the wire harness.

Maturing 800V EV supply chain in China: 800V EV sales penetration in China has risen from 5% in 2023 to 11% in 2025, cultivating an increasingly mature 800V auto supply chain. This spans upstream auto semis (SiC, GaN), downstream electronics components (SiC inverters, on-board chargers, DC-DC converters), and auxiliaries (connectors, relays, fuses).

Some EV suppliers have already entered the 800V AIDC supply chain: We map the major 800V EV supply chain in the following chart, covering both global and China players. Names highlighted in green have already partnered with Nvidia's next generation 800VDC AI factories. This suggests EV suppliers can potentially supply similar products to 800V AIDC.

Exhibit 1: 800V EV supply chain - global and China

## Auto Semi

SiC substrate
Wolfspeed (WOLF.N)
Coherent (COHR.N)
SICC 天岳先进 (688234.SS)

GaN
Innoscience 英诺赛科 (2577.HK)

SiC foundry
X-FAB (XFAB.PA)
Episil (3016.TW)
GlobalWafers (6488.TWO)
Times Electric 时代电气 (3898.HK)
United Nova Tech 芯联集成
(688469.SS)

Infineon (IFXGn.DE) STM (STMPA.PA) On Semi (ON.O) Rohm (6963.T) Renesas (6723.T) Wolfspeed (WOLF.N) Yangjie 扬杰科技 (300373.SZ) StarPower 斯达半导 (603290.SS) Silan 士兰微 (600460.SS)

## Electric Motor

Vitesco/Schaeffler (SHA0.DE)
BorgWarner (BWA.N)
Magna (MGA.N)
Denso (6902.T)
Nidec (6594.T)

BYD Fudi 弗迪动力 (1211.HK)
Inovance Auto 联合动力 (301656.SZ)
Founder 方正电机 (002196.SZ)
Jingjin Electric 精进电动 (688280.SS)
Broad-Ocean 大洋电机 (002249.SZ)

## OBC+DCDC

Delta Electronics (2308.TW)
Aptiv (APTV.N)
Eaton (ETN.N)
TDK (6762.T)

Megmeet 麦格米特 (002851.SZ)
BYD Fudi 弗迪动力 (1211.HK)
Joyson 均胜电子 (600699.SS)
VMAX 威迈斯 (688612.SS)
EV-Tech 富特科技 (301607.SZ)
Shinry 欣锐科技 (300745.SZ)
Enpower 英博尔 (300681.SZ)

## Connector

Bizlink (3665.TW)
Amphenol (APH.N)
TE Connectivity (TEL.N)
Aptiv (APTV.N)
JAE (6807.T)
Recodeal 瑞可达 (688800.SS)
Luxshare 立讯精密 (002475.SZ)
AVIC Jonhon 中航光电 (002179.SZ)
CWB 合兴股份 (605005.SS)
Yonggui 永贵电器 (300351.SZ)
ECT 电连技术 (300679.SZ)

## Relay

Panasonic (6752.T)
TE Connectivity (TEL.N)
Omron (6645.T)
Hongfa 宏发股份 (600885.SS)

Fuse

Littelfuse (LFUS.O)
Bel Fuse (BELFA.O)
Eaton Bussmann (ETN.N)
Sinofuse 中熔电气 (301031.SZ)

Source: MS. Names in green are partners for Nvidia's next generation 800VDC AI factories.

## Power semi – silicon carbide (SiC)

Electric motors (traction inverters), DC-DC converters, and on-board chargers (OBC) represent the key components that adopt SiC in 800V vehicles.

Power electronics – inverter, DC-DC converter, OBC

We believe tier-1 suppliers that assemble inverter, DC-DC converter, and OBC modules will also see opportunities from the 800V transition. For example, when an 800V EV charges at a 400V pole, a step-up DC-DC converter lifts voltage from 400V to 800V. When the 800V EV distributes power from the battery to 12/48V systems – such as cockpit and body control – a step-down DC-DC converter reduces voltage.

## Connectors

As vehicle architecture shifts from 400V to 800V, certain configurations require additional components, such as step-up or step-down DC-DC converters. We therefore estimate an incremental 20-30% increase in high-voltage connector volume, raising connector value to \~Rmb2.5K per 800V EV from \~Rmb2.0K per 400V EV.

## Relays and fuses

800V raises performance requirements for auxiliary components such as relays and fuses. Industry discussion increasingly focuses on replacing traditional melting fuses with eFuses, as eFuses can detect and isolate faults faster.

## Similarity in 800V EV and AIDC

The need for 800V: Like the EV industry's shift from 400V to 800V, AIDC migration to 800V reflects the need to deliver higher power without allowing current, cable size, heat, and conversion losses to scale disproportionately. In EVs, 800V enables faster DC charging, lighter high-voltage cabling, higher inverter efficiency, and greater power delivery to traction motors. In AIDC, the shift from 400VAC to 800VDC enables higher rack power, lower distribution current, reduced copper usage, fewer conversion stages, and improved end-to-end efficiency.

Redesigning the ecosystem: Both transitions require redesign of the surrounding ecosystem. EVs require 800V-compatible inverters, OBCs, DC-DC converters, and fast-charging interfaces, while AIDC requires 800V-ready rectifiers or solid-state transformers, busbars, protection devices, rack power shelves, energy storage interfaces, and server power supplies.

Exhibit 2: 800V EV architecture  
![](images/dca12352b5add0b19790831b1da33efb912848e8d1cc5dba47125b8c08741b7c.jpg)  
Source: STMicroelectronics

## Exhibit 3: 800V AIDC architecture

Data Center Roadmap
Architecting AI Infrastructure for Next-Gen AI Factories

2025  
![](images/6720d8a0fcec4cc690317014e03d68ea7527a44cf769791726382b4b3ee90bb0.jpg)

2027  
![](images/9bed712b1be0a6ca2ef2a049fbd0844f1b9a2d6bf280ca9236abf53e10ea66ec.jpg)  
Source: Nvidia

## Migrating to 800V AIDC Supply Chain

Opportunities from 800V EV to AIDC: Our US auto analyst Andrew Percoco explores migration opportunities in his Mobility to Megawatts Primer – Energy Storage, Onsite Power, 800V Architecture, and What's in the Price (3 Jun 2026). 800V AIDC requires a high-voltage technology stack that overlaps with capabilities auto suppliers have developed and commercialized for 800V EV platforms, including SiC-based inverters, DC-DC converters, high-voltage distribution, connectors, busbars, battery disconnect units, and thermal management systems.

Why few auto suppliers have won orders from 800V AIDC so far? While 800V AIDC and 800V EV share a similar high-voltage ecosystem, the customer requirements and qualification process are meaningfully different. Data centers prioritize 24/7 continuous operation, high power density, redundancy, hot-swap serviceability, very low downtime, and infrastructure-level reliability. Auto suppliers need to validate performance over longer operating lifecycles, demonstrate reliability at infrastructure scale, meet data-center certification/safety requirements, and build credibility with a new customer base. These commercial and qualification hurdles take time, which likely explains why auto-supplier traction in 800V AIDC remains limited so far.

What repurposing could require: The technology overlap is clear, but auto components are not direct drop-ins. Auto-grade inverters convert battery DC into AC motor power under dynamic driving conditions, while data center power systems must deliver reliable power flow across grid, batteries, on-site generation, and compute loads. At the component level, serving data-center applications would likely require auto suppliers to adapt their designs for stationary, high-utilization power infrastructure, including tighter voltage regulation, bidirectional power flow, packaging, cooling, protection schemes, serviceability, and facility-level controls. The opportunity lies less in reusing identical components and more in applying high-voltage EV engineering expertise to stationary, mission-critical power infrastructure. Selected suppliers – Aptiv, Versigent, BorgWarner, Magna, Lear – could benefit by extending their capabilities into power conversion, distribution, connectivity, and energy management.

Recodeal (688800.SS): Recodeal supplies connectors across EV, energy storage systems (ESS), robotaxi, eVTOL, and AIDC. Its AI-related products – AEC, active copper cable (ACC), direct attach cable (DAC), and power whips – do not specifically target 800V today. However, given its experience in high-voltage connectors for 800V EVs, we see strong potential to extend this know-how into 800V AIDC over time.

Joyson (600699.SS): Joyson supplies 800V auto electronics for the Porsche Taycan, including high-voltage boosters, multifunctional DC-DC converters, and OBCs. It secured Rmb13bn in new 800V orders in April 2023 to supply DC-DC converters and OBCs to a German luxury OEM's next-generation vehicles. Together with a Rmb9bn order win in 2022, Joyson now holds a Rmb22bn 800V backlog, supporting growth beyond 2025. While technically adjacent, application to 800V AIDC will require customer verification and time.

BYD (1211.HK) Fudi: BYD vertically integrates 800V EV components, including electric drive systems, motor controllers, on-board power electronics, high-voltage distribution, and harness-related parts. In addition to technical adjacency, BYD can bundle energy storage batteries with 800V powertrain technologies to address AIDC demand.

Keboda (603786.SS): Keboda supplies eFuses to Volkswagen, Mercedes-Benz, Li Auto, and others. eFuses detect and isolate faults – such as overcurrent or short circuits – faster than traditional melting fuses. This capability positions eFuses for potential adoption in high-voltage AIDC environments.

Exhibit 4: China auto parts with 800V exposure

<table><tr><td>China auto supplier</td><td>800V EV parts</td><td>Potential 800V AIDC parts</td><td>US peers</td></tr><tr><td>Recodeal (688800.SS)</td><td>800V EV connector</td><td>High-voltage power whip, active electrical cable</td><td>Aptiv (APTV.N)Amphenol (APH.N, NC)</td></tr><tr><td>Joyson (600699.SS)</td><td>800V on-board charger, DC-DC converter, booster</td><td>800V DC-DC converter, on-board charger, power distribution unit</td><td>Aptiv (APTV.N)BorgWarner (BWA.N)</td></tr><tr><td>BYD (1211.HK) Semi / Fudi</td><td>1200V SiC power module; 800V electric drive, motor controller, inverter</td><td>800V SiC inverter</td><td>BorgWarner (BWA.N)Magna (MGA.N)</td></tr><tr><td>Keboda (603786.SS)</td><td>eFuse (rapid-response protection) for auto PCB, not necessarily for 800V</td><td>High-voltage eFuse for rack</td><td>Versigent (VGNT.N)Lear (LEA.N)</td></tr></table>

Source: Company data, MS

## Upgrade Recodeal to OW

## Power whip a potential new growth driver

Margin pressure in EV connectors: Recodeal supplies high-voltage connectors to EV and ESS. We previously had concerns on margins, as EV OEM price cuts pass through to suppliers and intensify pricing pressure. Competition has also increased, with more connector makers entering, including players from consumer electronics.

Entering AIDC power whip: However, the rise of 800V AIDC architecture creates potential for Recodeal to supply high-voltage power whips into data centers. Power whips are pre-assembled cable systems that include cables, connectors, plugs, terminals, and protective conduits, delivering power from PDUs, busways, or power shelves to server racks or equipment. Currently, Bizlink (3665.TW, covered by Derrick Yang) leads as a power whip supplier to Nvidia Blackwell GPU racks and has developed connectors, cables, and busbar technologies supporting 800VDC architectures, according to company disclosures. Recodeal has already developed AIDC power whips. While not yet fully focused on 800V, we see strong potential for future 800V AIDC supply, given its expertise in 800V EV connectors.

Potential power whip revenue in 2026: In our base case, we assume no power whip revenue contribution in 2026. In our bull case, we expect mass production from 2H26, with \~Rmb0.5bn revenue contribution this year.

## AEC revenue ramping up in 2026

JV for AEC since 2025: Recodeal established a JV with a China-based AIDC optical transceiver supplier in February 2025 – Suzhou Ruichuang Connection Technology – and held a 60.61% stake as of May 2026. The JV targets AEC supply and commenced mass production in 1Q26, according to management. AEC represents copper cable assemblies with embedded signal-conditioning chips (retimers or redrivers) that extend short-reach, high-speed transmission within AIDC racks, offering lower power, lower cost, and lower latency versus optical solutions at these distances. We believe the JV strengthens Recodeal's AEC business through:

1) Customer access: Combining Recodeal's expertise in high-speed connectors, cable assembly, and precision manufacturing with its partner's customer access and system know-how in global AIDCs shortens validation cycles and accelerates the transition from sampling to volume production for 400G / 800G / 1.6T AEC. It should also improve Recodeal's chances of entering overseas CSP supply chains, upgrading its role from a traditional connector supplier to a higher-value AIDC interconnect platform provider.

2) Integrated offering: The JV enables positioning AEC within a broader “copper + optical” solution, where Recodeal focuses on lower-cost, lower-power active copper for short-reach links, while its partner focuses on optical transceivers for medium- and long-reach links.

>Rmb1bn AEC revenue in 2026: Management guides AEC capacity expansion from 15k units per month in 1Q26 to 120-150k units per month in 4Q26. Based on an estimated ASP of USD150-250, we expect AEC to contribute Rmb1.1bn revenue in 2026 and Rmb2.6bn in 2027.

## EV connector business recovering

Weak 1Q26 due to de-stocking: Recod

[中间内容因长度限制已省略]

2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## INDUSTRY COVERAGE: China Autos & Shared Mobility

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/30/2026)</td></tr><tr><td colspan="3">Joey Xu, CFA</td></tr><tr><td>Anhui Jianghuai Automobile (600418.SS)</td><td>E (08/19/2023)</td><td>Rmb25.83</td></tr><tr><td>BAIC Motor (1958.HK)</td><td>E (10/02/2025)</td><td>HK$0.78</td></tr><tr><td>Brilliance China Automotive (1114.HK)</td><td>E (03/31/2025)</td><td>HK$1.91</td></tr><tr><td>Chongqing Changan Automobile (000625.SZ)</td><td>E (03/03/2026)</td><td>Rmb7.17</td></tr><tr><td>Guangzhou Automobile Group (601238.SS)</td><td>U (10/23/2019)</td><td>Rmb5.08</td></tr><tr><td>Guangzhou Automobile Group (2238.HK)</td><td>O (05/05/2020)</td><td>HK$2.08</td></tr><tr><td>Huayu Automotive (600741.SS)</td><td>O (09/08/2020)</td><td>Rmb15.52</td></tr><tr><td>Jiangsu Changshu Automotive Trim Group (603035.SS)</td><td>E (08/14/2023)</td><td>Rmb10.62</td></tr><tr><td>Ningbo Huaxiang Electronic Co., Ltd. (002048.SZ)</td><td>E (05/05/2026)</td><td>Rmb23.00</td></tr><tr><td>SAIC Motor Corp. Ltd. (600104.SS)</td><td>O (11/25/2021)</td><td>Rmb9.76</td></tr><tr><td>Voyah Automotive Technology Co. Ltd, (7489.HK)</td><td>O (03/31/2026)</td><td>HK$2.90</td></tr><tr><td>Zhengzhou Yutong Bus Co (600066.SS)</td><td>E (09/22/2023)</td><td>Rmb26.81</td></tr><tr><td colspan="3">Shelley Wang, CFA</td></tr><tr><td>Beijing Jingwei Hirain Technologies (688326.SS)</td><td>U (09/27/2024)</td><td>Rmb70.88</td></tr><tr><td>Bethel Automotive Safety Systems Co Ltd (603596.SS)</td><td>O (12/11/2023)</td><td>Rmb24.84</td></tr><tr><td>Changzhou Xingyu Automotive Lighting Sys (601799.SS)</td><td>O (09/27/2024)</td><td>Rmb90.62</td></tr><tr><td>China MeiDong Auto Holdings Ltd (1268.HK)</td><td>E (01/08/2024)</td><td>HK$0.51</td></tr><tr><td>China Yongda Automobiles Services (3669.HK)</td><td>E (08/13/2024)</td><td>HK$0.70</td></tr><tr><td>Foryou Corporation (002906.SZ)</td><td>O (03/06/2024)</td><td>Rmb24.96</td></tr><tr><td>Fuyao Glass Industry Group (600660.SS)</td><td>E (12/01/2016)</td><td>Rmb50.44</td></tr><tr><td>Fuyao Glass Industry Group (3606.HK)</td><td>E (12/01/2016)</td><td>HK$51.20</td></tr><tr><td>Huizhou Desay SV Automotive Co Ltd (002920.SZ)</td><td>O (02/28/2025)</td><td>Rmb81.50</td></tr><tr><td>Keboda (603786.SS)</td><td>O (01/17/2024)</td><td>Rmb40.91</td></tr><tr><td>Minth Group Limited (0425.HK)</td><td>O (08/24/2015)</td><td>HK$26.42</td></tr><tr><td>NavInfo Co Ltd (002405.SZ)</td><td>U (03/06/2024)</td><td>Rmb6.47</td></tr><tr><td>Nexteer Automotive Group (1316.HK)</td><td>E (02/28/2025)</td><td>HK$3.81</td></tr><tr><td>Ningbo Joyson Electronic Corp (600699.SS)</td><td>E (03/11/2026)</td><td>Rmb21.61</td></tr><tr><td>Ningbo Tuopu Group Co Ltd (601689.SS)</td><td>E (11/12/2025)</td><td>Rmb56.42</td></tr><tr><td>Ningbo Xusheng Group Co Ltd (603305.SS)</td><td>E (06/18/2025)</td><td>Rmb12.12</td></tr><tr><td>Suzhou Recodeal Interconnect System (688800.SS)</td><td>O (07/01/2026)</td><td>Rmb95.97</td></tr><tr><td>TUHU Car Inc (9690.HK)</td><td>O (07/29/2024)</td><td>HK$12.70</td></tr><tr><td>Zhejiang Sanhua Intelligent Controls (002050.SZ)</td><td>E (11/12/2025)</td><td>Rmb43.83</td></tr><tr><td>Zhongsheng Group Holdings (0881.HK)</td><td>O (10/12/2021)</td><td>HK$4.85</td></tr><tr><td colspan="3">Tim Hsiao</td></tr><tr><td>BAIC BluePark New Energy (600733.SS)</td><td>U (08/07/2024)</td><td>Rmb4.87</td></tr><tr><td>BYD Company Limited (002594.SZ)</td><td>O (04/14/2025)</td><td>Rmb79.70</td></tr><tr><td>BYD Company Limited (1211.HK)</td><td>O (04/14/2025)</td><td>HK$72.45</td></tr><tr><td>EHang Holdings Ltd (EH.O)</td><td>O (03/13/2025)</td><td>US$6.55</td></tr><tr><td>Geely Automobile Holdings (0175.HK)</td><td>O (06/26/2024)</td><td>HK$16.86</td></tr><tr><td>Great Wall Motor Company Limited (601633.SS)</td><td>U (03/16/2022)</td><td>Rmb15.09</td></tr><tr><td>Great Wall Motor Company Limited (2333.HK)</td><td>E (01/08/2024)</td><td>HK$8.81</td></tr><tr><td>Hesai Group (HSAI.O)</td><td>O (07/28/2025)</td><td>US$18.22</td></tr><tr><td>Horizon Robotics (9660.HK)</td><td>O (12/02/2024)</td><td>HK$4.08</td></tr><tr><td>Li Auto Inc. (LI.O)</td><td>O (08/24/2020)</td><td>US$11.74</td></tr><tr><td>Li Auto Inc. (2015.HK)</td><td>O (11/16/2021)</td><td>HK$46.08</td></tr><tr><td>NIO Inc. (9866.HK)</td><td>O (10/03/2022)</td><td>HK$38.74</td></tr><tr><td>NIO Inc. (NIO.N)</td><td>O (08/26/2020)</td><td>US$5.06</td></tr><tr><td>WeRide Inc (WRD.O)</td><td>O (11/19/2024)</td><td>US$5.82</td></tr><tr><td>XPeng Inc. (9868.HK)</td><td>O (11/16/2021)</td><td>HK$50.65</td></tr><tr><td>XPeng Inc. (XPEV.N)</td><td>O (01/29/2021)</td><td>US$13.24</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.

\* Historical prices are not split adjusted.

© 2026 MS
"""
