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

Entering AIDC power whip: However, the ris

[中间内容因长度限制已省略]

ully before investing.

## INDUSTRY COVERAGE: China Autos & Shared Mobility

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/30/2026)</td></tr><tr><td colspan="3">Joey Xu, CFA</td></tr><tr><td>Anhui Jianghuai Automobile (600418.SS)</td><td>E (08/19/2023)</td><td>Rmb25.83</td></tr><tr><td>BAIC Motor (1958.HK)</td><td>E (10/02/2025)</td><td>HK$0.78</td></tr><tr><td>Brilliance China Automotive (1114.HK)</td><td>E (03/31/2025)</td><td>HK$1.91</td></tr><tr><td>Chongqing Changan Automobile (000625.SZ)</td><td>E (03/03/2026)</td><td>Rmb7.17</td></tr><tr><td>Guangzhou Automobile Group (601238.SS)</td><td>U (10/23/2019)</td><td>Rmb5.08</td></tr><tr><td>Guangzhou Automobile Group (2238.HK)</td><td>O (05/05/2020)</td><td>HK$2.08</td></tr><tr><td>Huayu Automotive (600741.SS)</td><td>O (09/08/2020)</td><td>Rmb15.52</td></tr><tr><td>Jiangsu Changshu Automotive Trim Group (603035.SS)</td><td>E (08/14/2023)</td><td>Rmb10.62</td></tr><tr><td>Ningbo Huaxiang Electronic Co., Ltd. (002048.SZ)</td><td>E (05/05/2026)</td><td>Rmb23.00</td></tr><tr><td>SAIC Motor Corp. Ltd. (600104.SS)</td><td>O (11/25/2021)</td><td>Rmb9.76</td></tr><tr><td>Voyah Automotive Technology Co. Ltd, (7489.HK)</td><td>O (03/31/2026)</td><td>HK$2.90</td></tr><tr><td>Zhengzhou Yutong Bus Co (600066.SS)</td><td>E (09/22/2023)</td><td>Rmb26.81</td></tr><tr><td colspan="3">Shelley Wang, CFA</td></tr><tr><td>Beijing Jingwei Hirain Technologies (688326.SS)</td><td>U (09/27/2024)</td><td>Rmb70.88</td></tr><tr><td>Bethel Automotive Safety Systems Co Ltd (603596.SS)</td><td>O (12/11/2023)</td><td>Rmb24.84</td></tr><tr><td>Changzhou Xingyu Automotive Lighting Sys (601799.SS)</td><td>O (09/27/2024)</td><td>Rmb90.62</td></tr><tr><td>China MeiDong Auto Holdings Ltd (1268.HK)</td><td>E (01/08/2024)</td><td>HK$0.51</td></tr><tr><td>China Yongda Automobiles Services (3669.HK)</td><td>E (08/13/2024)</td><td>HK$0.70</td></tr><tr><td>Foryou Corporation (002906.SZ)</td><td>O (03/06/2024)</td><td>Rmb24.96</td></tr><tr><td>Fuyao Glass Industry Group (600660.SS)</td><td>E (12/01/2016)</td><td>Rmb50.44</td></tr><tr><td>Fuyao Glass Industry Group (3606.HK)</td><td>E (12/01/2016)</td><td>HK$51.20</td></tr><tr><td>Huizhou Desay SV Automotive Co Ltd (002920.SZ)</td><td>O (02/28/2025)</td><td>Rmb81.50</td></tr><tr><td>Keboda (603786.SS)</td><td>O (01/17/2024)</td><td>Rmb40.91</td></tr><tr><td>Minth Group Limited (0425.HK)</td><td>O (08/24/2015)</td><td>HK$26.42</td></tr><tr><td>NavInfo Co Ltd (002405.SZ)</td><td>U (03/06/2024)</td><td>Rmb6.47</td></tr><tr><td>Nexteer Automotive Group (1316.HK)</td><td>E (02/28/2025)</td><td>HK$3.81</td></tr><tr><td>Ningbo Joyson Electronic Corp (600699.SS)</td><td>E (03/11/2026)</td><td>Rmb21.61</td></tr><tr><td>Ningbo Tuopu Group Co Ltd (601689.SS)</td><td>E (11/12/2025)</td><td>Rmb56.42</td></tr><tr><td>Ningbo Xusheng Group Co Ltd (603305.SS)</td><td>E (06/18/2025)</td><td>Rmb12.12</td></tr><tr><td>Suzhou Recodeal Interconnect System (688800.SS)</td><td>O (07/01/2026)</td><td>Rmb95.97</td></tr><tr><td>TUHU Car Inc (9690.HK)</td><td>O (07/29/2024)</td><td>HK$12.70</td></tr><tr><td>Zhejiang Sanhua Intelligent Controls (002050.SZ)</td><td>E (11/12/2025)</td><td>Rmb43.83</td></tr><tr><td>Zhongsheng Group Holdings (0881.HK)</td><td>O (10/12/2021)</td><td>HK$4.85</td></tr><tr><td colspan="3">Tim Hsiao</td></tr><tr><td>BAIC BluePark New Energy (600733.SS)</td><td>U (08/07/2024)</td><td>Rmb4.87</td></tr><tr><td>BYD Company Limited (002594.SZ)</td><td>O (04/14/2025)</td><td>Rmb79.70</td></tr><tr><td>BYD Company Limited (1211.HK)</td><td>O (04/14/2025)</td><td>HK$72.45</td></tr><tr><td>EHang Holdings Ltd (EH.O)</td><td>O (03/13/2025)</td><td>US$6.55</td></tr><tr><td>Geely Automobile Holdings (0175.HK)</td><td>O (06/26/2024)</td><td>HK$16.86</td></tr><tr><td>Great Wall Motor Company Limited (601633.SS)</td><td>U (03/16/2022)</td><td>Rmb15.09</td></tr><tr><td>Great Wall Motor Company Limited (2333.HK)</td><td>E (01/08/2024)</td><td>HK$8.81</td></tr><tr><td>Hesai Group (HSAI.O)</td><td>O (07/28/2025)</td><td>US$18.22</td></tr><tr><td>Horizon Robotics (9660.HK)</td><td>O (12/02/2024)</td><td>HK$4.08</td></tr><tr><td>Li Auto Inc. (LI.O)</td><td>O (08/24/2020)</td><td>US$11.74</td></tr><tr><td>Li Auto Inc. (2015.HK)</td><td>O (11/16/2021)</td><td>HK$46.08</td></tr><tr><td>NIO Inc. (9866.HK)</td><td>O (10/03/2022)</td><td>HK$38.74</td></tr><tr><td>NIO Inc. (NIO.N)</td><td>O (08/26/2020)</td><td>US$5.06</td></tr><tr><td>WeRide Inc (WRD.O)</td><td>O (11/19/2024)</td><td>US$5.82</td></tr><tr><td>XPeng Inc. (9868.HK)</td><td>O (11/16/2021)</td><td>HK$50.65</td></tr><tr><td>XPeng Inc. (XPEV.N)</td><td>O (01/29/2021)</td><td>US$13.24</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.

\* Historical prices are not split adjusted.

© 2026 MS
"""
