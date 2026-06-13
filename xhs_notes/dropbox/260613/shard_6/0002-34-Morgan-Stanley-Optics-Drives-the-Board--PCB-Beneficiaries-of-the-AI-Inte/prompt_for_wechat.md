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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`摩根斯坦利`。标题格式建议：`# 摩根斯坦利：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

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

Incumbents like Unimicron and Shennan should continue to do well in the optical transceiver market, but we see ZDT as being aggressive and gaining share: We believe incumbent optical transceiver PCB suppliers, including Shennan and Unimicron, are well positioned to benefit from both volume growth and rising PCB content per transceiver over CY26-28. At the same time, the expanding addressable market is creating opportunities for new entrants, as existing industry capacity appears insufficient to meet anticipated demand.

Our channel checks indicate that ZDT and Compeq (2313.TW, not covered) are actively expanding capacity to support the ramp of 800G and 1.6T optical transceiver PCBs. We believe ZDT's share gains began with the initial ramp-up of 800G transceivers in CY25, and we estimate its supply share increased to approximately 7.5% in CY25, with the potential to reach \~20% by CY28. In the 1.6T segment, we estimate that ZDT entered the market with roughly 5% share in CY25 and could expand its position to \~25% by CY28E.

We expect ZDT's share gains to accelerate with the industry's migration toward 1.6T transceivers and beyond, where PCB technology requirements become increasingly demanding. Specifically, 1.6T+ transceiver PCBs are expected to require mSAP manufacturing processes, raising both technical barriers and qualification requirements. We believe ZDT is particularly well positioned to capitalize on this transition, given its extensive experience with mSAP technology, developed and refined through its participation in Apple's iPhone mainboard supply chain since the adoption of mSAP-based SLP architectures in 2017.

Exhibit 7: AI transceiver PCB value contribution to suppliers - we expect suppliers to see 50-176% CAGR over CY25-28E  
AI Transceiver PCB value by supplier (US\$M)  
![](images/34a219b5a5ac821b8738503414c3189a47090f4c50c5d502673539c3c45ae265.jpg)

<details>
<summary>bar chart</summary>

| Company           | 2025  | 2026E | 2027E | 2028E |
| ----------------- | ----- | ----- | ----- | ----- |
| Unimicron         | $200  | $480  | $760  | $890  |
| Shennan Circuits  | $290  | $730  | $1140 | $1050 |
| Zhen Ding/Avary   | $30   | $300  | $670  | $850  |
</details>

Source: MS estimates.

## MSe vs. Consensus

Our 2026-28 revenue estimates are 1%, 2% and -3% different from Consensus, while our net income estimates are 0%, 3% and 4% higher than Consensus. We think the variance comes from our incorporation of higher AI transceiver PCB supply share assumptions for ZDT at 17%/20%/22% for 2026/2027/2028. The stock has rallied \~145% since April 1, vs. TAIEX +26% over the same period, driven primarily by the progress of its ABF substrate business and its potential share g

[中间内容因长度限制已省略]

le JSC Ltd (601869.SS)</td><td>U (10/13/2021)</td><td>Rmb442.51</td></tr><tr><td>Yangtze Optical Fibre and Cable JSC Ltd (6869.HK)</td><td>E (04/20/2023)</td><td>HK$230.60</td></tr><tr><td>Yongxin Optics Co Ltd (603297.SS)</td><td>E (11/15/2022)</td><td>Rmb117.96</td></tr><tr><td>Zhejiang Crystal-Optech Co Ltd (002273.SZ)</td><td>O (11/15/2022)</td><td>Rmb33.18</td></tr><tr><td>Zhongji Innolight Co Ltd (300308.SZ)</td><td>++</td><td>Rmb1,124.00</td></tr><tr><td>ZTE Corporation (0763.HK)</td><td>O (06/04/2026)</td><td>HK$26.20</td></tr><tr><td>ZTE Corporation (000063.SZ)</td><td>E (06/04/2026)</td><td>Rmb37.81</td></tr><tr><td colspan="3">Derrick Yang</td></tr><tr><td>Accton Technology Corporation (2345.TW)</td><td>O (06/06/2024)</td><td>NT$2,275.00</td></tr><tr><td>Advantech (2395.TW)</td><td>O (01/20/2021)</td><td>NT$464.00</td></tr><tr><td>AirTAC International (1590.TW)</td><td>O (04/16/2025)</td><td>NT$1,265.00</td></tr><tr><td>AU Optronics (2409.TW)</td><td>E (02/10/2026)</td><td>NT$23.15</td></tr><tr><td>Bizlink (3665.TW)</td><td>O (03/10/2025)</td><td>NT$2,160.00</td></tr><tr><td>BOE Technology (000725.SZ)</td><td>O (09/06/2019)</td><td>Rmb5.83</td></tr><tr><td>Chenbro (8210.TW)</td><td>O (07/23/2025)</td><td>NT$1,440.00</td></tr><tr><td>Chroma Ate Inc. (2360.TW)</td><td>O (10/05/2021)</td><td>NT$2,190.00</td></tr><tr><td>E Ink Holdings Inc. (8069.TWO)</td><td>O (05/11/2026)</td><td>NT$190.50</td></tr><tr><td>Ennostar Inc (3714.TW)</td><td>U (09/23/2022)</td><td>NT$63.50</td></tr><tr><td>Hiwin Technologies Corp. (2049.TW)</td><td>O (03/30/2026)</td><td>NT$318.50</td></tr><tr><td>Innolux (3481.TW)</td><td>E (04/07/2025)</td><td>NT$46.95</td></tr><tr><td>King Slide Works Co. Ltd. (2059.TW)</td><td>O (11/08/2023)</td><td>NT$6,400.00</td></tr><tr><td>Lens Technology (300433.SZ)</td><td>E (07/22/2020)</td><td>Rmb42.68</td></tr><tr><td>Radiant Opto-Electronics Corporation (6176.TW)</td><td>E (03/01/2024)</td><td>NT$91.70</td></tr><tr><td>Sanan Optoelectronics (600703.SS)</td><td>U (08/21/2023)</td><td>Rmb15.26</td></tr><tr><td>TCL Corp. (000100.SZ)</td><td>E (04/07/2025)</td><td>Rmb4.51</td></tr><tr><td>Tianma Microelectronics (000050.SZ)</td><td>U (01/24/2018)</td><td>Rmb7.66</td></tr><tr><td>Wuhan Jingce Electronic Group Co Ltd (300567.SZ)</td><td>E (11/26/2021)</td><td>Rmb192.90</td></tr><tr><td colspan="3">Howard Kao</td></tr><tr><td>Acer Inc. (2353.TW)</td><td>U (04/23/2025)</td><td>NT$36.90</td></tr><tr><td>Asustek Computer Inc. (2357.TW)</td><td>U (11/16/2025)</td><td>NT$784.00</td></tr><tr><td>Compal Electronics (2324.TW)</td><td>U (04/23/2025)</td><td>NT$36.15</td></tr><tr><td>FIT Hon Teng Ltd (6088.HK)</td><td>O (11/03/2025)</td><td>HK$7.30</td></tr><tr><td>Giga-Byte Technology Co. Ltd. (2376.TW)</td><td>E (11/16/2025)</td><td>NT$340.00</td></tr><tr><td>Gold Circuit Electronics Ltd. (2368.TW)</td><td>O (10/06/2022)</td><td>NT$1,345.00</td></tr><tr><td>Inspur Electronic Information (000977.SZ)</td><td>E (08/28/2023)</td><td>Rmb57.84</td></tr><tr><td>Lenovo (0992.HK)</td><td>E (11/16/2025)</td><td>HK$22.88</td></tr><tr><td>Lotes Co. Ltd. (3533.TW)</td><td>E (05/12/2025)</td><td>NT$2,145.00</td></tr><tr><td>Nan Ya PCB (8046.TW)</td><td>O (02/23/2026)</td><td>NT$807.00</td></tr><tr><td>Pegatron Corporation (4938.TW)</td><td>E (03/25/2026)</td><td>NT$95.40</td></tr><tr><td>Quanta Computer Inc. (2382.TW)</td><td>O (05/01/2023)</td><td>NT$370.00</td></tr><tr><td>Shengyi Technology Co Ltd. (600183.SS)</td><td>E (05/26/2022)</td><td>Rmb149.73</td></tr><tr><td>Shennan Circuits Co Ltd (002916.SZ)</td><td>E (08/24/2023)</td><td>Rmb376.16</td></tr><tr><td>Unimicron (3037.TW)</td><td>O (02/23/2026)</td><td>NT$854.00</td></tr><tr><td>Wistron Corporation (3231.TW)</td><td>O (07/12/2023)</td><td>NT$152.50</td></tr><tr><td>Wiwynn Corp (6669.TW)</td><td>O (11/10/2025)</td><td>NT$4,900.00</td></tr><tr><td>Yageo Corp. (2327.TW)</td><td>O (10/28/2025)</td><td>NT$842.00</td></tr><tr><td>Zhen Ding (4958.TW)</td><td>O (05/18/2026)</td><td>NT$529.00</td></tr><tr><td colspan="3">Sharon Shih</td></tr><tr><td>Asia Vital Components Co. Ltd. (3017.TW)</td><td>O (07/30/2024)</td><td>NT$2,335.00</td></tr><tr><td>Auras Technology Co Ltd (3324.TWO)</td><td>E (05/04/2023)</td><td>NT$998.00</td></tr><tr><td>Catcher Technology (2474.TW)</td><td>U (11/17/2025)</td><td>NT$205.50</td></tr><tr><td>Delta Electronics Inc. (2308.TW)</td><td>O (07/13/2017)</td><td>NT$2,160.00</td></tr><tr><td>Fositek Corp (6805.TW)</td><td>O (06/25/2025)</td><td>NT$1,750.00</td></tr><tr><td>Foxconn Industrial Internet Co. Ltd. (601138.SS)</td><td>O (07/10/2019)</td><td>Rmb69.52</td></tr><tr><td>Foxconn Technology (2354.TW)</td><td>U (04/23/2025)</td><td>NT$56.20</td></tr><tr><td>GoerTek Inc (002241.SZ)</td><td>U (04/23/2025)</td><td>Rmb22.72</td></tr><tr><td>Hon Hai Precision (2317.TW)</td><td>O (03/15/2024)</td><td>NT$258.50</td></tr><tr><td>LandMark Optoelectronics Corporation (3081.TWO)</td><td>E (03/26/2026)</td><td>NT$2,165.00</td></tr><tr><td>Lingyi Itech Guangdong Co (002600.SZ)</td><td>U (04/23/2025)</td><td>Rmb13.63</td></tr><tr><td>Lite-On Technology (2301.TW)</td><td>E (01/15/2025)</td><td>NT$208.50</td></tr><tr><td>Luxshare Precision Industry Co., Ltd. (002475.SZ)</td><td>O (10/24/2016)</td><td>Rmb64.58</td></tr><tr><td>Sunonwealth Electric Machine Industry Co (2421.TW)</td><td>E (02/23/2024)</td><td>NT$142.00</td></tr><tr><td>Tong Hsing (6271.TW)</td><td>E (03/18/2019)</td><td>NT$217.00</td></tr><tr><td>Visual Photonics Epitaxy Co Ltd (2455.TW)</td><td>E (09/11/2023)</td><td>NT$320.00</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
