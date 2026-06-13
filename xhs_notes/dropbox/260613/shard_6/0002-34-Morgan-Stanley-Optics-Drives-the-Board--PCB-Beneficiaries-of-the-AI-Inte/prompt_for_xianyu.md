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
# Greater China Technology Hardware | Asia Pacific

# Optics Drives the Board: PCB Beneficiaries of the AI Interconnect Build-out

Although incumbent suppliers, including Unimicron and Shennan Circuits, will likely benefit from the growth in transceiver PCB demand and content expansion, we view ZDT as the most compelling beneficiary, given its potential to capture meaningful share as the industry transitions to higher speeds.

The AI investment cycle is entering a new phase in which optical connectivity is becoming as critical as compute. As hyperscalers scale AI clusters from tens of thousands to hundreds of thousands of GPUs, the number of optical transceivers required to connect these systems is growing rapidly. While investors have largely focused on beneficiaries such as GPUs, networking chips, and optical module vendors, we believe there are also opportunities further down the supply chain: printed circuit board (PCB) manufacturers. These companies provide a differentiated way to participate in the secular growth of AI infrastructure spend.

The opportunity is not solely driven by unit growth; content is also rising. As the industry migrates from 400G to 800G and eventually 1.6T optical transceivers, PCB complexity is increasing materially. Higher layer counts (10L to 16L), higher grade CCL (M6 to M8), and the adoption of advanced manufacturing technologies (HDI to mSAP) are driving a step-function increase in PCB content per module (US\$10 to US \$25). As a result, we expect the optical transceiver PCB market to grow substantially faster (83% CAGR) than underlying transceiver shipments (60% CAGR) from CY25-28. We are forecasting AI transceiver PCB TAM growing from \~US \$620M in CY25 to \~US\$3,773M by CY28, and this content-driven growth should also translate into improved profitability and expanding returns for suppliers with the requisite technological capabilities.

ZDT is best positioned to capture share: We expect incumbent leaders to benefit from both volume and content growth; however, we believe the most attractive investment opportunity is Zhen Ding (ZDT). The transition to 1.6T and beyond is raising qualification barriers and increasing the importance of advanced manufacturing know-how, particularly in mSAP processes. As the market expands and customers seek additional qualified suppliers, companies with proven high-end PCB capabilities are positioned to capture disproportionate growth. In our view, this combination of secular AI demand, rising content intensity, and market share gains creates a compelling angle for ZDT, hence we raise our PT to NT\$666, implying 20x CY28 P/E (0.5x PEG). We reiterate our OW on Unimicron, with a raised PT of NT \$1,285, implying 25x CY28 P/E (0.25x PEG), but stay EW on Shennan with a raised PT of Rmb400, implying 25x CY28 P/E (0.6x PEG). We prefer ZDT (15x CY28 P/E) and Unimicron (17x CY28 P/E) but are EW Shennan (25x CY28 P/E) on valuation.

MS TAIWAN LIMITED+

## Howard Kao

Equity Analyst

Howard.Kao@morganstanley.com +886 2 2730-2989

## Irene Yen

Research Associate

Irene.Yen@morganstanley.com +886 2 2730-2869

## Sharon Shih

Equity Analyst

Sharon.Shih@morganstanley.com +886 2 2730-2865

## Asia Summer School 2026

![](images/ca6f6f3d746d34e25ee836849b1f1cdad75d6f11831ba9a3b780e64acad2b032.jpg)

## GREATER CHINA TECHNOLOGY HARDWARE

## Asia Pacific

Industry View

In-Line

Exhibit 1: What's changed?

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td colspan="2">Rating</td><td colspan="2">PT</td><td rowspan="2">Last close</td><td rowspan="2">Upside (%)</td><td colspan="3">EPS change (%)</td><td colspan="3">PEG</td></tr><tr><td>New</td><td>Old</td><td>New</td><td>Old</td><td>26e</td><td>27e</td><td>28e</td><td>26e</td><td>27e</td><td>28e</td></tr><tr><td>Unimicron</td><td>3037.TW</td><td>OW</td><td>OW</td><td>1,285.0</td><td>1,225.0</td><td>884.0</td><td>45%</td><td>2%</td><td>5%</td><td>4%</td><td>0.63</td><td>0.45</td><td>0.25</td></tr><tr><td>Zhen Ding</td><td>4958.TW</td><td>OW</td><td>OW</td><td>660.0</td><td>570.0</td><td>502.0</td><td>31%</td><td>5%</td><td>15%</td><td>17%</td><td>0.42</td><td>0.40</td><td>0.52</td></tr><tr><td>Shennan Circuits</td><td>002916.SZ</td><td>EW</td><td>EW</td><td>400.0</td><td>320.0</td><td>383.1</td><td>4%</td><td>9%</td><td>17%</td><td>24%</td><td>1.21</td><td>0.63</td><td>0.63</td></tr></table>

Source: Bloomberg, MS estimates. Pricing as of the close on June 10, 2026.

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Contextualizing the AI Transceiver PCB Opportunity

To put the opportunity into perspective, we forecast the global AI transceiver PCB TAM to expand from approximately US\$620mn in CY25 to \~US\$3.8bn by CY28. For comparison, we estimate that Apple (covered by Erik Woodring) – currently the world's largest consumer of HDI PCBs – accounts for roughly US\$3.0-3.5B of annual HDI PCB demand. On our estimates, the AI transceiver PCB market will grow from a niche, sub-US \$1B segment today to a market comparable in size to Apple's HDI PCB demand by CY27, before surpassing it by CY28.

The significance of this comparison extends beyond the absolute market size. For years, Apple has been the primary driver of technology advancement, capacity investment, and profitability within the HDI PCB industry. We believe AI optical connectivity is emerging as the next major demand engine, creating a new growth vector for PCB suppliers and potentially reshaping the industry's competitive landscape.

Given the pace of market expansion, increasing technology requirements, and improving economics associated with next-generation transceiver PCBs, we believe AI transceiver PCBs are rapidly evolving into one of the most compelling structural growth opportunities within the global PCB sector.

Viewed from another angle, Prismark estimates the global HDI PCB market at approximately US\$16.2bn. Based on our forecast of a \~US\$3.8bn AI transceiver PCB market by CY28, AI optical connectivity alone could generate incremental demand equivalent to roughly 23% of the current global HDI market, underscoring the significance of this emerging growth driver for the PCB industry

In February 2026, our global team highlighted that the AI transceiver market is entering an 'exponential' growth phase, driven by scale-out, scale-up and even scale-across in AI datacenters (report link: AI Transceivers: Growth Dominates Disruption).

While CPO (co-packaged optics) remains a fundamental architectural shift and a legitimate long-term risk to pluggable transceivers, the impact on transceivers vendors and their supply chains is limited in the medium term, as large-scale adoption of CPO is unlikely before 2027-28, considering its manufacturing yield, thermal complexity, cost, ecosystem, and serviceability. Thus, our global team expects AI transceiver growth to dominate the disruption from CPO in the medium term, and that transceivers and CPO will coexist through the 3.2T transition expected in CY28.

Our Global team expects strong optical transceiver volumes in CY26-28: In May 2026, our global team raised (link) its CY26-28 AI transceiver shipments forecast from 53 / 71 / 80mn units to 73 / 141 / 158 M units, respectively, within which 29 / 79 / 87M are 1.6T optical transceivers, with 8mn 3.2T optical transceivers expected in CY28 (Exhibit 1). This translates into a \~99% CAGR over CY25-28, creating a significant surge in demand for supply chain capacity. This signal a robust growth prospect not only for the optical transceivers vendors but also for the entire supply chain, including the PCB manufacturers. This is because within each optical transceiver module, there is 1 PCB, so it is a one-for-one opportunity for PCB manufacturers.

Exhibit 2: Our Global team raised forecasts for 800G and 1.6T optical transceiver shipments

<table><tr><td colspan="4">(mn units)</td></tr><tr><td>New Estimates</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>800G</td><td>44</td><td>63</td><td>64</td></tr><tr><td>1.6T</td><td>29</td><td>79</td><td>87</td></tr><tr><td>3.2T</td><td>0</td><td>0</td><td>8</td></tr><tr><td>Total</td><td>73</td><td>141</td><td>158</td></tr><tr><td>Previous Estimates</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>800G</td><td>34</td><td>48</td><td>54</td></tr><tr><td>1.6T</td><td>19</td><td>24</td><td>27</td></tr><tr><td>3.2T</td><td>0</td><td>0</td><td>5</td></tr><tr><td>Total</td><td>53</td><td>71</td><td>85</td></tr><tr><td>Pct. of change</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>800G</td><td>29%</td><td>31%</td><td>19%</td></tr><tr><td>1.6T</td><td>52%</td><td>233%</td><td>226%</td></tr><tr><td>3.2T</td><td>--</td><td>--</td><td>60%</td></tr><tr><td>Total</td><td>38%</td><td>98%</td><td>86%</td></tr></table>

Source: Company data, MS estimates.

Exhibit 3: Our Global team estimates AI optical transceivers growing at \~60% CAGR from 2025-28E  
We estimate AI transceivers growing at 60% CAGR from 2025-28E  
![](images/05713d1d051fd1ed11ba38f46b03f5ea5c04f54fbbc7532bb2ce179163517ff3.jpg)

<details>
<summary>bar chart</summary>

| Year | Value |
| :--- | :--- |
| 2022 | 3 |
| 2023 | 7 |
| 2024 | 26 |
| 2025 | 41 |
| 2026E | 90 |
| 2027E | 153 |
| 2028E | 168 |
</details>

Source: MS estimates.

## Aside from volume growth, optical transceiver PCB is also seeing content growth...

Our industry checks suggest optical transceiver PCBs will see content growth mainly coming from three aspects.

1. Upgrades in CCL material (M6 to M8): The migration from 400G to 800G and 1.6T transceivers is driving increased adoption of higher-specification CCL materials. Whereas 400G modules generally utilized M6-grade CCL, next-generation transceivers increasingly require M7- or M8-grade CCL to meet more demanding signal integrity requirements, supporting higher PCB ASPs.  
2. Increased layer count (10L to 16L): Increasing PCB layer counts represent another tailwind for ASP growth. Layer requirements rise from 10–12 layers in 400G transceivers to 12-14 layers in 800G and 14-16 layers in 1.6T modules, reflecting greater design complexity and supporting higher PCB ASPs.  
3. More complex manufacturing process (HDI to mSAP): The adoption of more advanced fabrication technologies is another driver of PCB ASP expansion. While 400G transceivers typically rely on HDI (high density interconnect) processes, next-generation 800G and 1.6T modules increasingly require mSAP (modified semi-additive process), reflecting higher design complexity and supporting higher ASPs.

The combination of the three drivers mentioned above is driving a strong growth of the overall PCB market for optical transceiver modules. The reason why mSAP is required is that it saves space by allowing denser conducting path layouts, which makes it the perfect material for optical transceivers. This is commonly found in compact devices, such as smartphone mainboards and smartphone camera modules. Apple is one of the first companies to start using mSAP technology in its smartphone PCB, going back to 2017, for the iPhone 8/X generation. Which is why today, a lot of the optical transceiver modules makers are also companies that have been HDI/SLP PCB suppliers for Apple iPhone, including Unimicron, ZDT, and Compeq.

...why is why we estimate PCB ASP per transceiver module will rise from US\$5-15 for a 400G transceiver to US\$20-30 for a 1.6T transceiver. We expect the transition from 400G to 1.6T transceivers to drive a substantial increase in PCB content and complexity. PCB designs are likely to upgrade from 10- to 12-layer HDI structures with 2-3 lamination cycles and M6-grade CCL to 14- to 16-layer mSAP-based architectures with 6-10 mSAP layers and M8-grade CCL. Consequently, we estimate PCB ASPs could rise \~2.5x, from approximately US\$10 to US\$25 per unit. Moreover, the higher technical barriers and value-add should drive gross margins from 20-30% to 40-50%+, approaching those of ABF substrates. The combination of strong volume growth and rising PCB content per transceiver is expected to drive AI transceiver PCB TAM growth well ahead of underlying module shipments. We estimate the global AI transceiver PCB market will grow at an 83% CAGR over CY25-28E, versus a 60% CAGR growth in AI transceiver unit volumes, reflecting increasing PCB complexity and higher content per module as the industry migrates to 800G and 1.6T transceivers.

Simply put, as the AI transceiver speeds migrate from 400G to 1.6T or 3.2T, the electrical signals needs to travel at much higher speeds, and the PCB traces start to make a difference, where signal loss, reflections, crosstalk, and timing variations become major challenges. To preserve signal integrity, the PCB needs to be designed with lower-loss

laminate materials are required (M8 grade CCL), tighter impedance control, more sophisticated routing, optimized vias, etc. As a result, each generation of faster optical transceivers increases the technical complexity and value-added content of the PCB, creating a structural tailwind for advanced PCB suppliers with expertise in mSAP capability.

Exhibit 4: Optical transceiver PCB specs

<table><tr><td></td><td>400G</td><td>800G</td><td>1.6T</td></tr><tr><td>Layers</td><td>10-12L2-3 press HDI</td><td>12-14L, 4-8L mSAP or HDI</td><td>14-16L6-10L mSAP</td></tr><tr><td>Process</td><td>HDI</td><td>HDI or mSAP</td><td>mSAP</td></tr><tr><td>CCL Spec</td><td>M6</td><td>M7(LDK1) / M7+ (LDK2)</td><td>M7+ / M8 (LDK2)</td></tr><tr><td>ASP (US$)</td><td>$5-15</td><td>$15-25</td><td>$20-30</td></tr><tr><td>GM Est.</td><td>20-30%</td><td>30-40%</td><td>40-50%+</td></tr><tr><td>Suppliers</td><td>Unmicron, Shennan, WUS, other smaller suppliers.</td><td>Unimicron, Shennan, Zhen Ding, WUS, Compeq, etc.</td><td>Unimicron, Shennan, Zhen Ding, Compeq, WUS, etc.</td></tr></table>

Source: MS.

Exhibit 5: We estimate Global AI Transceiver PCB TAM to grow at 83% CAGR from 2025-28E  
![](images/9826218e0b8fa6a827817d13f3fff7750c454fa2b20036c987cd71e8ebac7466.jpg)

<details>
<summary>stacked bar chart</summary>

AI transceiver PCB TAM is growing at 83% CAR from 2025-28E (US$ M)
| Year | Unimicron | Shennan | Zhen Ding | Others |
| :--- | :--- | :--- | :--- | :--- |
| 2022 | $27 | | | |
| 2023 | $80 | | | |
| 2024 | $310 | | | |
| 2025 | $620 | | | |
| 2026E | $1,780 | Shennan | Zhen Ding | Others |
| 2027E | $3,343 | Shennan | Zhen Ding | Others |
| 2028E | $3,773 | Shennan | Zhen Ding | Others |
</details>

Source: MS estimates.

Exhibit 6: TAM comparison: AI transceiver vs. AI transceiver PCB  
![](images/468fb35b143d0ed188eee99a38f554dcec570b88e5c611804deb0cb4b6cd4a02.jpg)

<details>
<summary>bar-line hybrid</summary>

| Year | AI transceiver TAM (US$ M) | AI transceiver PCB TAM (US$ M) | PCB as % of transceiver (RHS) (%) |
| :--- | :--- | :--- | :--- |
| 2022 | 1,080 | 27 | 2.5 |
| 2023 | 2,975 | 80 | 2.7 |
| 2024 | 10,725 | 310 | 2.9 |
| 2025 | 18,140 | 620 | 3.4 |
| 2026E | 48,739 | 1,780 | 3.7 |
| 2027E | 86,736 | 3,343 | 3.9 |
| 2028E | 101,545 | 3,773 | 3.7 |
</details>

Source: MS estimates.

Incumbents like Unimicron and Shennan should continue to do well in the optical transce

[中间内容因长度限制已省略]

tional (1590.TW)</td><td>O (04/16/2025)</td><td>NT$1,265.00</td></tr><tr><td>AU Optronics (2409.TW)</td><td>E (02/10/2026)</td><td>NT$23.15</td></tr><tr><td>Bizlink (3665.TW)</td><td>O (03/10/2025)</td><td>NT$2,160.00</td></tr><tr><td>BOE Technology (000725.SZ)</td><td>O (09/06/2019)</td><td>Rmb5.83</td></tr><tr><td>Chenbro (8210.TW)</td><td>O (07/23/2025)</td><td>NT$1,440.00</td></tr><tr><td>Chroma Ate Inc. (2360.TW)</td><td>O (10/05/2021)</td><td>NT$2,190.00</td></tr><tr><td>E Ink Holdings Inc. (8069.TWO)</td><td>O (05/11/2026)</td><td>NT$190.50</td></tr><tr><td>Ennostar Inc (3714.TW)</td><td>U (09/23/2022)</td><td>NT$63.50</td></tr><tr><td>Hiwin Technologies Corp. (2049.TW)</td><td>O (03/30/2026)</td><td>NT$318.50</td></tr><tr><td>Innolux (3481.TW)</td><td>E (04/07/2025)</td><td>NT$46.95</td></tr><tr><td>King Slide Works Co. Ltd. (2059.TW)</td><td>O (11/08/2023)</td><td>NT$6,400.00</td></tr><tr><td>Lens Technology (300433.SZ)</td><td>E (07/22/2020)</td><td>Rmb42.68</td></tr><tr><td>Radiant Opto-Electronics Corporation (6176.TW)</td><td>E (03/01/2024)</td><td>NT$91.70</td></tr><tr><td>Sanan Optoelectronics (600703.SS)</td><td>U (08/21/2023)</td><td>Rmb15.26</td></tr><tr><td>TCL Corp. (000100.SZ)</td><td>E (04/07/2025)</td><td>Rmb4.51</td></tr><tr><td>Tianma Microelectronics (000050.SZ)</td><td>U (01/24/2018)</td><td>Rmb7.66</td></tr><tr><td>Wuhan Jingce Electronic Group Co Ltd (300567.SZ)</td><td>E (11/26/2021)</td><td>Rmb192.90</td></tr><tr><td colspan="3">Howard Kao</td></tr><tr><td>Acer Inc. (2353.TW)</td><td>U (04/23/2025)</td><td>NT$36.90</td></tr><tr><td>Asustek Computer Inc. (2357.TW)</td><td>U (11/16/2025)</td><td>NT$784.00</td></tr><tr><td>Compal Electronics (2324.TW)</td><td>U (04/23/2025)</td><td>NT$36.15</td></tr><tr><td>FIT Hon Teng Ltd (6088.HK)</td><td>O (11/03/2025)</td><td>HK$7.30</td></tr><tr><td>Giga-Byte Technology Co. Ltd. (2376.TW)</td><td>E (11/16/2025)</td><td>NT$340.00</td></tr><tr><td>Gold Circuit Electronics Ltd. (2368.TW)</td><td>O (10/06/2022)</td><td>NT$1,345.00</td></tr><tr><td>Inspur Electronic Information (000977.SZ)</td><td>E (08/28/2023)</td><td>Rmb57.84</td></tr><tr><td>Lenovo (0992.HK)</td><td>E (11/16/2025)</td><td>HK$22.88</td></tr><tr><td>Lotes Co. Ltd. (3533.TW)</td><td>E (05/12/2025)</td><td>NT$2,145.00</td></tr><tr><td>Nan Ya PCB (8046.TW)</td><td>O (02/23/2026)</td><td>NT$807.00</td></tr><tr><td>Pegatron Corporation (4938.TW)</td><td>E (03/25/2026)</td><td>NT$95.40</td></tr><tr><td>Quanta Computer Inc. (2382.TW)</td><td>O (05/01/2023)</td><td>NT$370.00</td></tr><tr><td>Shengyi Technology Co Ltd. (600183.SS)</td><td>E (05/26/2022)</td><td>Rmb149.73</td></tr><tr><td>Shennan Circuits Co Ltd (002916.SZ)</td><td>E (08/24/2023)</td><td>Rmb376.16</td></tr><tr><td>Unimicron (3037.TW)</td><td>O (02/23/2026)</td><td>NT$854.00</td></tr><tr><td>Wistron Corporation (3231.TW)</td><td>O (07/12/2023)</td><td>NT$152.50</td></tr><tr><td>Wiwynn Corp (6669.TW)</td><td>O (11/10/2025)</td><td>NT$4,900.00</td></tr><tr><td>Yageo Corp. (2327.TW)</td><td>O (10/28/2025)</td><td>NT$842.00</td></tr><tr><td>Zhen Ding (4958.TW)</td><td>O (05/18/2026)</td><td>NT$529.00</td></tr><tr><td colspan="3">Sharon Shih</td></tr><tr><td>Asia Vital Components Co. Ltd. (3017.TW)</td><td>O (07/30/2024)</td><td>NT$2,335.00</td></tr><tr><td>Auras Technology Co Ltd (3324.TWO)</td><td>E (05/04/2023)</td><td>NT$998.00</td></tr><tr><td>Catcher Technology (2474.TW)</td><td>U (11/17/2025)</td><td>NT$205.50</td></tr><tr><td>Delta Electronics Inc. (2308.TW)</td><td>O (07/13/2017)</td><td>NT$2,160.00</td></tr><tr><td>Fositek Corp (6805.TW)</td><td>O (06/25/2025)</td><td>NT$1,750.00</td></tr><tr><td>Foxconn Industrial Internet Co. Ltd. (601138.SS)</td><td>O (07/10/2019)</td><td>Rmb69.52</td></tr><tr><td>Foxconn Technology (2354.TW)</td><td>U (04/23/2025)</td><td>NT$56.20</td></tr><tr><td>GoerTek Inc (002241.SZ)</td><td>U (04/23/2025)</td><td>Rmb22.72</td></tr><tr><td>Hon Hai Precision (2317.TW)</td><td>O (03/15/2024)</td><td>NT$258.50</td></tr><tr><td>LandMark Optoelectronics Corporation (3081.TWO)</td><td>E (03/26/2026)</td><td>NT$2,165.00</td></tr><tr><td>Lingyi Itech Guangdong Co (002600.SZ)</td><td>U (04/23/2025)</td><td>Rmb13.63</td></tr><tr><td>Lite-On Technology (2301.TW)</td><td>E (01/15/2025)</td><td>NT$208.50</td></tr><tr><td>Luxshare Precision Industry Co., Ltd. (002475.SZ)</td><td>O (10/24/2016)</td><td>Rmb64.58</td></tr><tr><td>Sunonwealth Electric Machine Industry Co (2421.TW)</td><td>E (02/23/2024)</td><td>NT$142.00</td></tr><tr><td>Tong Hsing (6271.TW)</td><td>E (03/18/2019)</td><td>NT$217.00</td></tr><tr><td>Visual Photonics Epitaxy Co Ltd (2455.TW)</td><td>E (09/11/2023)</td><td>NT$320.00</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
