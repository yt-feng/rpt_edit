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
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
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
1. `# 标题`：一句主判断，不超过 32 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Technology - European Semiconductors | Europe

# Framing the CPO opportunity for Soitec and Besi

WHAT'S CHANGED 

<table><tr><td>Soitec SA (SOIT.PA)</td><td>From</td><td>To</td></tr><tr><td>Price Target</td><td>€70.00</td><td>€200.00</td></tr><tr><td colspan="3">BE Semiconductor Industries NV (BESI.AS)</td></tr><tr><td>Price Target</td><td>€200.00</td><td>€300.00</td></tr></table>

Larger, more tightly coupled AI rack clusters should push optics deeper into the datacenter, lifting Soitec's Photonics SOI wafer content and Besi's hybrid bonding demand. Detailed modelling raises our conviction, resulting in material PT increases for both.

# Key Takeaways

■ Agentic systems increase the need for high bandwidth, low latency communication in the AI datacenter which may accelerate the penetration of photonics.   
The attach rate of optical engines per GPU may increase sharply, from c.2-4 in a single rack domain to >35 in a multi-rack architecture leveraging CPO.   
We built a detailed model to size the implications for Soitec and Besi and expect a material increase in addressable demand towards 2028.   
Soitec is the more direct beneficiary through Photonics SOI wafers. We raise CY28 revenue estimates as well as our PT, which moves to €200.   
- Besi benefits from CPO adoption as TSMC's COUPE leverages hybrid bonding. In addition, we expect increased use in future GPU and HBM generations. PT to €300.

Upcoming architectural changes in NVIDIA's rack-scale infrastructure, introduced with NVL576 and beyond, will create a material, multi-year benefit for both Soitec and Besi, in our view. We've been modelling the networking opportunity through growth of transceivers, but we now identify a much larger opportunity when co-packaged optics (CPO) starts to be used in the scale-up domain that is still dominated by copper connections. Using insights from Corning's recent investor meeting, we model a meaningful increase in the addressable market for Soitec's Photonic SOI technology. Besi should also benefit, as we expect a large proportion of this market, and especially NVIDIA, to use TSMC's COUPE architecture, which is enabled by Besi's hybrid bonding tools. In addition to networking, we see opportunities for adoption within GPU and HBM memory, where we had been more cautious previously. As a result, we raise our estimates for Soitec and Besi meaningfully and increase our price targets to €200 and €300, respectively, as we stay Overweight on both names.

MS & CO. INTERNATIONAL PLC+

# Nigel van Putten

Equity Analyst
Nigel.Putten@morganstanley.com +44 20 7425-2803

# Shawn Kim

Equity Analyst
Shawn.Kim@morganstanley.com +44 20 7677-1018

# Lee Simpson

Equity Analyst
Lee.Simpson@morganstanley.com +44 20 7425-3378

# Amelia M Scicluna

Research Associate
Amelia.Scicluna@morganstanley.com +44 20 7425-6694

# Terence Tsui

Equity Analyst
Terence.Tsui@morganstanley.com +44 20 7425-3095

# TECHNOLOGY - EUROPEAN SEMICONDUCTORS

Europe
Industry View In-Line

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

# For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

Corning's Investor Day points to a 10x increase in fiber content per GPU as data centres move to co-packaged optics. In photonic networking, fibers carry the light, but at each end sits an optical engine (OE), a package of an electronic and photonics chip, which converts electrical signals to light and electrical signals. The photonics chips are built on photonic integrated circuits (PIC) using Soitec's engineered photonics SOI wafers. Meanwhile, Besi's hybrid bonding tools are often (depending on the assembly process) used to package the electrical IC (EIC) on top of the PIC. Corning presented the opportunity in fibers (160 per GPU in a fully optical architecture versus 16 today), and in doing so, disclosed enough about the underlying switch architecture, lane counts and SerDes rates for us to calculate the number of optical engines required. That count maps closely on a near one-to-one basis to Soitec's addressable market for AI datacenter Photonics wafers and gives a useful indication of Besi's hybrid bonding opportunity.

Exhibit 1: We expect the optical engines attach rate per GPU to increase 10x in future configurations   
![](images/e438d26b56903d85392e761f34168748e6428fc604d08acaabcbe41b5f02a474.jpg)

<details>
<summary>bar</summary>

| Category | Optical Engines per GPU |
|---|---|
| Current | 2 |
| Copper/CPO hybrid | 17 |
| Full CPO | 35 |
| CPO bull case | 70 |
</details>

Source: MS

# We estimate optical engines per GPU rise from c.2 to 4 today to 17 in NVL576 and potentially >35 in a fully optical configuration. Today's pre-CPO setup uses 2-

4 pluggable transceivers (two for the leaf, two for spine with oversubscription potentially reducing this number) per GPU, all in the scale-out network. NVL576 introduces co-packaged optics (CPO) for inter-rack scale-up traffic, lifting optical engine attach rate to c.17 per GPU, on our estimates. A fully optical variant, where the connection between GPU and the networking switch also moves to photonics, roughly doubles that to c.35. Looking ahead to Feynman architectures and Keyber rack architectures, OEs per-GPU could remain at that level if SerDes speeds move to 400G, but could double again if SerDes stays at 200G, which Corning CEO Wendell Weeks flagged as closer to the historical pattern.

Soitec benefits directly from rising silicon photonics content. Today, the company's exposure is largely limited to pluggable optics used in the inter-rack networking infrastructure. This is already contributing to growth within Soitec's photonics-related revenue, expected to have reached >\$100m (MSe: \$112m) in fiscal year '26 (March year-end), but remains modest relative to what we believe is about to emerge. With the introduction of CPO for scale-up, first in a hybrid and later in full CPO architectures, photonic SOI content is expected to significantly increase, driving an acceleration of growth in calendar years '27 and '28. As a result, we raise our Soitec estimates on the photonics upgrade, even as we leave the remainder of our assumptions broadly unchanged. We now model Photonics SOI revenue of

\$468m in CY28, up from \$387m previously, lifting our CY28 EPS forecast to €6.09 from €5.40. Our new PT of €200 applies a 35x multiple to CY28 earnings power, discounted by one year. The increase in our price target from €70 to €200 is a result of a combination of higher estimates, moving the base year to CY28 from CY27 and raising the multiple to 35x from 30x. We think the higher multiple is warranted due to our higher conviction on Soitec's growth trajectory into CY30e. The transition towards scale-up CPO architectures may start with early NVL576 hybrid racks in late '26 but we expect this design to move into mainstream adoption towards '28. In order to capture this development, which is supported by our detailed wafer model, we move to CY28 (fiscal '29 March end) as the base year for Soitec and discount by one year. For Besi, and other equipment companies in our coverage, we continue to use CY27 as our base year. Here, visibility on capex investment beyond '28, although directionally positive, remains somewhat limited.

Besi represents a second route into the CPO ramp. CPO should become an incremental growth driver for Besi's hybrid bonders because optical engines need advanced assembly. We expect TSMC's COUPE to become a leading integration route for the optical engine, especially at NVIDIA, which supports additional tool demand for Besi's hybrid bonders. From the Feynman GPU onwards, the opportunity broadens into stacked GPU dies, which we expect to use hybrid bonding, and into (custom) HBM, where we expect hybrid bonding to start in CY27 and widen thereafter. Applying a 37x (previously 35x) multiple to c.€8 CY27 earnings power gives our revised PT of €300. Our target multiple moves up slightly on higher valuation across the semiconductor sector as well as increased visibility of the hybrid bonding opportunity for HBM.

How to position for upcoming catalysts. Both companies have catalyst events in the coming weeks. Soitec will report its FY26 (March '26 year-end) on 27 May after close followed by an investor meeting on May 28 in Paris. Besides the print this event matters because it will be the first opportunity for new CEO Laurent Rémont to present to the market. We expect Mr Rémont to lay out an optimistic view but numbers are likely to be conservative and expressed in medium-term CAGRs. Against high expectations in the market we would position tactically cautious into this event. Besi will host its annual investor day on June 18 in Amsterdam. Here we expect the company to provide more detail on optical interconnect as a driver for its mainstream, hybrid bonding, and potentially thermo-compression bonding (TCB) tools. We also expect more colour on expectations around the introduction of hybrid bonding for HBM.

Inside the note, we provide insight into our detailed model that bridges GPU/ASIC and transceiver assumptions into Photonics SOI wafers and hybrid bonding tool capacity.

# Transceiver growth and increased CPO penetration bodes well for Soitec and Besi

Meaningful update to Transceiver forecasts. Our colleague covering Greater China Technology Hardware, Andy Meng, updated his transceiver forecasts last week Friday – see Global AI Transceivers: Industry Demand Likely to be Even Stronger. The team raised its AI transceiver shipment forecasts to 73m units from 53m in '26, to 141m units from 71m in '27, and to 150m from 80m for '28. The larger '27-'28 revisions mainly reflect a more positive view on 1.6T demand, and now forecasts the AI transceiver TAM to grow from US \$18 bn in 2025 to US\$102 bn in 2028, or >4x in three years. In the near term, we expect transceivers to be the main driver of growth for Silicon Photonics, benefiting Soitec's photonics SOI revenue line and Besi's mainstream business. However, from '27e onwards we expect the main contribution for each to shift to Co-Packaged Optics (CPO).

Exhibit 2: AI Transceivers global volume - Global market volume ('000 units)   
![](images/c602ca6ea36515c7d7177638bc6b6b72383990f26797ebdbc3caa680e236a0c2.jpg)

<details>
<summary>bar_stacked</summary>

| Year | 400G | 800G | 1.6T | 3.2T |
|---|---|---|---|---|
| 2023 | ~5,00 | 0 | 0 | 0 |
| 2024 | ~20,00 | ~5,00 | 0 | 0 |
| 2025 | ~20,00 | ~10,00 | 0 | 0 |
| 2026E | ~15,00 | ~45,00 | ~30,00 | 0 |
| 2027E | ~10,00 | ~75,00 | ~95,00 | 0 |
| 2028E | ~10,00 | ~75,00 | ~115,00 | ~15,00 |
</details>

Source: Companyy data, MS estimates (E)

# Insights from Corning's Investor Day

France's Soitec, a leader in manufacturing engineered substrates; Netherlands-based Besi, which develops leading edge assembly equipment; and Corning, the American multi-technology company (covered by Meta Marshall) seem mostly unrelated at first glance, but they overlap in Silicon Photonics. Corning's fibre discussion gives us a way to estimate optical engine demand, which then maps into Soitec's photonics SOI wafers. For Besi, the more relevant issue is the optical engine package, especially where the EIC is bonded directly on top of the PIC. Here the company's hybrid bonders are required when integration uses die to wafer hybrid bonding, which is the case for TSMC's COUPE, which we expect to emerge as one of the main CPO integration routes.

The scale-up opportunity starts when NVLink moves beyond one rack. Scale-up is the part of the AI cluster where GPUs work as one tightly connected system. NVL72 keeps that domain inside one rack, and NVL144 can still be managed through copper over relatively short distances. As model sizes, context windows and inference workloads grow, NVIDIA (and other providers of AI accelerators) needs larger pools of compute to share data at high bandwidth and low latency. That pushes the scale-up domain across racks, where copper reaches its distance limit and optical links become the practical answer.

Exhibit 3: NVL72 single rack platform at 100G within-rack links < 2m works with copper while multi-rack platform at 200G with links between racks >10m requires optical   
![](images/0b18eb2c90e58b3f6b989016cc0b9757333b09e8110f10e6f71924e93417a070.jpg)

<details>
<summary>scatter</summary>

| Method     | Distance (m) | Data Rates (Gb/s) |
| ---------- | ------------ | ----------------- |
| NVL72      | 0.3          | 100               |
| NVL576     | 10           | 200               |
| ELECTRICAL | 0.3          | 0.1               |
</details>

Source: Corning

Corning laid out three drivers for optical content growth per GPU, each additive. The first is cluster size. As GPU clusters grow beyond roughly 130,000 GPUs, a third switching layer, the superspine, is required, adding approximately 50% more optical connections. The second is bandwidth growth. GPU and switch ASIC bandwidth doubles roughly every two years, and Corning links this to fiber demand through lane rate and lane count. The third, and largest, is the optical scale-up network. NVL576 introduces optical links between racks for the first time, creating a new category of fiber and photonics demand that did not exist in NVL72. Corning estimates that the combination of these three factors will grow optical content 1.3x to 1.5x per GPU through 2028. That is content growth per GPU, on top of GPU unit growth.

Exhibit 4: Corning estimates that optical content will increase 1.3x to 1.5x per GPU by 2028 

<table><tr><td>Technical Driver</td><td>Logic</td><td>Impact</td></tr><tr><td>Cluster Size Growth</td><td>Cluster size &gt;130k GPUs will require an additional optical layer</td><td>+</td></tr><tr><td>Bandwidth (BW) Growth</td><td>GPU and ASIC BW doubles every ~2 years... we link them through lane rate and number of lanes</td><td>= +</td></tr><tr><td>Scale Up Network</td><td>This is a whole new optical opportunity</td><td>+ + +</td></tr></table>

Source: Corning

# Framing the opportunity for Soitec and Besi

Fibers carry the signal, while photonic ICs, or PICs, sit within the optical engines at each end. This allows us to model Soitec content and Besi's hybrid bonding opportunity, at least directionally, through Corning's views on fiber expansion. Before diving deeper into the model drivers, we first recap how Soitec and Besi are exposed to the theme.

Soitec's Photonics SOI wafers are used for the fabrication of silicon photonics IC's (SiPho PICs) that, together with an Electric Integrated Circuit (EIC) form the optical engine (OE). An optical engine is the core functional unit that converts electrical signals into optical signals and vice versa. It is the fundamental building block of any optical transceiver, whether that transceiver takes the form of a pluggable module, on-board optics, or co-packaged optics. The PIC handles the optical functions: modulation (encoding data onto light), detection (reading incoming light), waveguiding (routing light on-chip), and coupling to external fiber. The EIC drives the laser, amplifies signals from the photodetector and interfaces electrically with the host ASIC or SerDes. Soitec's Photonics SOI are the material of choice for foundries like Global Foundries, Tower Semiconductor and TSMC to create the PICs. Soitec has a dominant share, especially on the larger wafer sizes (300mm) that are increasingly preferred by the industry.

Exhibit 5: How Soitec's Photonics SOI enables PIC   
![](images/0ac77111d3ba371a4357d73aa25a19206d37fb3a493f019d650a546beef2aef9.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["CONTROL OF TOP SI THICKNESS"] --> B["PHOTONICS-SOI"]
    C["OPTIMAL TOP SI ROUGHNESS"] --> B
    D["BASE WAFER MECHANICAL STABILITY"] --> B
    E["LOW LEVEL OF DEFECTS"] --> B
    B --> F["Single-Crystal Silicon (Si)"]
    B --> G["Buried Oxide (BOX)"]
    B --> H["Handle Silicon"]
    F --> I["Optical Amplifiers"]
    F --> J["MZI/juring modulators"]
    F --> K["Si Waveguides"]
    F --> L["GeSi, InP photodiode"]
    F --> M["Silicon Nitride devices"]
    F --> N["Surface/Edge Fiber Couplers"]
    B --> O["Waveguide Loss"]
    B --> P["Photodiodes Responsivity"]
    B --> Q["Wafer Handling"]
    B --> R["TSV Driver Integration"]
    B --> S["Chip-to-Fiber Attach"]
```
</details>

Source: Soitec

Besi's hybrid bonders are often used for the packaging process that integrates the EIC and PIC into a an optical engine. The OE itself is essentially the same functional block regardless of where it sits. What changes is how close it is to the switch ASIC and how it is packaged. In a pluggable transceiver, the OE sits in a front-panel module and relatively long electrical traces connect it to the networking chip or ASIC.

In CPO, the OE is co-packaged on the same substrate as the ASIC resulting in ultra-short electrical interconnects, often resulting 20-30% lower power per bit and lower latency. This requires tighter integration and is where TSMC's COUPE shines. COUPE is TSMC's Compact Universal Photonic Engine: a silicon-photonics platform for co-packaged optics, intended to move optical I/O closer to compute. It combines a silicon photonics wafer/PIC and EIC with advanced packaging, aiming for a smaller-footprint and high(est) performance. COUPE on substrate can deliver 4x better power efficiency and 90% lower latency, rising to 10x and 95% lower latency when integrated on an interposer. Hybrid bonding enters through TSMC SolC. COUPE uses SolC, or 3D stacking/hybrid bonding, to place the high-speed electronic IC directly onto a photonic IC, creating a compact “sandwich” of electronics and optics. Today, Besi is the sole provider of hybrid bonding tools to TSMC.

Exhibit 6: TSMC Coupe increases power efficiency and reduces latency through hybrid bonding   
![](images/0dacff8665e40c621110780a2f8fe67445cd2b8235330b659792f296589457fd.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Power Efficiency"] --> B["Cu Wire 1X"]
    C["

[中间内容因长度限制已省略]

rsons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

MS Hong Kong Securities Limited is the liquidity provider/market maker for securities of ASM International NV listed on the Stock Exchange of Hong Kong Limited. An updated list can be found on HKEx website: http://www.hkex.com.hk.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

Stock Ratings are subject to change. Please see latest research for each company.   
\* Historical prices are not split adjusted.   
INDUSTRY COVERAGE: Technology - European Semiconductors 

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (05/18/2026)</td></tr><tr><td>Lee Simpson</td><td></td><td></td></tr><tr><td>ASML Holding NV (ASML.AS)</td><td>O (09/22/2025)</td><td>€1,264.40</td></tr><tr><td>Infineon Technologies AG (IFXGn.DE)</td><td>O (02/06/2025)</td><td>€66.33</td></tr><tr><td>STMicroelectronics NV (STMPA.PA)</td><td>O (03/26/2026)</td><td>€52.42</td></tr><tr><td colspan="3">Nigel van Putten</td></tr><tr><td>Aixtron SE (AIXGn.DE)</td><td>E (05/25/2023)</td><td>€50.36</td></tr><tr><td>ASM International NV (ASMI.AS)</td><td>O (06/19/2024)</td><td>€844.60</td></tr><tr><td>BE Semiconductor Industries NV (BESI.AS)</td><td>O (11/07/2022)</td><td>€255.80</td></tr><tr><td>Melexis N.V. (MLXS.BR)</td><td>E (02/05/2026)</td><td>€78.25</td></tr><tr><td>Nordic Semiconductor ASA (NOD.OL)</td><td>E (02/10/2025)</td><td>NKr 201.20</td></tr><tr><td>Soitec SA (SOIT.PA)</td><td>O (03/26/2026)</td><td>€140.25</td></tr><tr><td>VAT Group AG (VACN.S)</td><td>E (03/21/2025)</td><td>SFr 586.80</td></tr></table>

© 2026 MS
"""
