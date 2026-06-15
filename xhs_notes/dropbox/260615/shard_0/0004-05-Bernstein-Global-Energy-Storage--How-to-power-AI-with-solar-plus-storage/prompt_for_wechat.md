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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`Bernstein`。标题格式建议：`# Bernstein：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份Bernstein研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## Global Energy Storage

# Global Energy Storage: How to power AI with solar-plus-storage

![](images/0e9de7c08efcadde37d724c27bfb44a41b946ab2d8060b813fa4344ec6e6699a.jpg)

Brian Ho, CFA

+852 2123 2615

brian.ho@bernsteinsg.com

![](images/205faff560a86e9a6d7174d727fe62073267961a9c2bc1932a3ace071a2f6a09.jpg)

Neil Beveridge, Ph.D.

+852 2123 2648

neil.beveridge@bernsteinsg.com

![](images/ca87267ccf4fe86c835719866576b0a5b9f17d41b445f94a58fbc187e93c0bad.jpg)

Kelvin Yuan, Ph.D., CFA

+852 2123 2612

kelvin.yuan@bernsteinsg.com

The industry has long viewed solar-plus-storage as insufficient for baseload power particularly for 24/7 AI-driven demand. Masdar and EWEC's gigascale solar-plus-storage project challenges this view with the world's first deployment of firm renewable power at scale. Our analysis leaves us incrementally more constructive on solar-plus-storage as a competitive source of baseload power, with Sungrow and CATL as key beneficiaries.

Solar-plus-storage can deliver baseload reliability at scale. UAE's Masdar and EWEC are building 5.2 GW of solar combined with 19 GWh of storage (19 hours duration) to deliver \~1 GW of continuous power, with completion targeted by 2027. Based on our analysis, the system could achieve \~99.6% system reliability, representing a structural shift in renewables from intermittent energy sources to providers of firm capacity.

Economics are competitiveness particularly for higher gas price markets. While the upfront capex is high at \~\$6,000/kW, solar-plus-storage benefits from low operating costs and zero fuel exposure. At an estimated LCOE of \$97/MWh for the project, solar-plus-storage can compete with gas-fired power at gas price of \~\$8/mmbtu or higher. At 12-hour storage scenario, the LCOE falls to around \$80/MWh which can still achieve high system reliability of 95%. The attractiveness of solar-plus-storage as baseload is important given ongoing volatility and disruption in global gas supply. That said, we still believe gas-fired power is favored in regions with abundant low cost gas supply such as the US.

Faster deployment versus gas and nuclear is a key advantage. Solar and storage projects can be delivered in roughly two years, compared with current gas turbine lead times of around four years due to supply constraints, and even longer timelines for nuclear, typically six years or more.

The key constraint is access to high solar irradiance and land. While the system is replicable, we think it is still limited to solar-rich regions with abundant, low-cost land. This project alone requires $\sim60\ km^{2}$ of land—roughly the size of Manhattan—highlighting the significant physical footprint required to deliver firm renewable power at scale.

Storage is the primary driver of system economics rather than solar. ESS account for roughly half of total project capex, meaning cost competitiveness is primarily driven by storage cost, efficiency, and performance rather than module pricing.

We expect global ESS demand to grow at \~34% CAGR over the next five years, driven by the need for firming renewable generation and grid stability. Within the value chain, CATL leads in ESS battery supply and technology, while Sungrow is a key player in system integration, inverters, and broader power conversion solutions, positioning both as primary beneficiaries of this structural shift.

BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="3">12 Jun 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>300750.CH (CATL)</td><td>O</td><td>CNY</td><td>394.85</td><td>800.00</td><td>18.9%</td><td>CNY</td><td>16.14</td><td>21.95</td><td>28.77</td><td>24.5</td><td>18.0</td><td>13.7</td></tr><tr><td>247540.KS (EcoPro BM)</td><td>U</td><td>KRW</td><td>167,800</td><td>140,000</td><td>32.9%</td><td>KRW</td><td>403.00</td><td>854.00</td><td>1,963.00</td><td>416.4</td><td>196.5</td><td>85.5</td></tr><tr><td>051910.KS (LG Chem)</td><td>M</td><td>KRW</td><td>320,000</td><td>298,000</td><td>20.7%</td><td colspan="2">KRW(13,258.70)</td><td>2,042.47</td><td>31,118</td><td>(24.1)</td><td>156.7</td><td>10.3</td></tr><tr><td>373220.KS (LGES)</td><td>M</td><td>KRW</td><td>387,000</td><td>347,000</td><td>(9.9)%</td><td colspan="2">KRW (5,308.10)</td><td>1,811.04</td><td>9,452.97</td><td>(72.9)</td><td>213.7</td><td>40.9</td></tr><tr><td>003670.KS (Posco Future M)</td><td>U</td><td>KRW</td><td>188,800</td><td>190,000</td><td>13.4%</td><td colspan="2">KRW (2,740.96)</td><td>376.72</td><td>898.20</td><td>(68.9)</td><td>501.2</td><td>210.2</td></tr><tr><td>006400.KS (SDI)</td><td>M</td><td>KRW</td><td>507,000</td><td>520,000</td><td>168.1%</td><td colspan="2">KRW (9,933.80)</td><td>2,099.51</td><td>18,376</td><td>(51.0)</td><td>241.5</td><td>27.6</td></tr><tr><td>300274.CH (Sungrow)</td><td>O</td><td>RMB</td><td>148.76</td><td>185.00</td><td>90.9%</td><td>RMB</td><td>6.55</td><td>8.22</td><td>9.33</td><td>22.7</td><td>18.1</td><td>15.9</td></tr><tr><td>002466.CH (Tianqi Lithium)</td><td>O</td><td>CNY</td><td>62.50</td><td>73.00</td><td>63.3%</td><td>CNY</td><td>0.28</td><td>3.29</td><td>6.18</td><td>221.5</td><td>19.0</td><td>10.1</td></tr><tr><td>9696.HK (Tianqi Lithium)</td><td>O</td><td>HKD</td><td>47.58</td><td>61.00</td><td>36.7%</td><td>CNY</td><td>0.28</td><td>3.29</td><td>6.18</td><td>145.5</td><td>12.5</td><td>6.6</td></tr><tr><td>034020.KS (Doosan Enerbility)</td><td>O</td><td>KRW</td><td>90,100</td><td>95,000</td><td>32.8%</td><td>KRW</td><td>173.88</td><td>45.91</td><td>687.53</td><td>518.2</td><td>N/M</td><td>131.0</td></tr><tr><td>3750.HK (CATL)</td><td>M</td><td>HKD</td><td>670.00</td><td>770.00</td><td>77.7%</td><td>CNY</td><td>16.14</td><td>21.95</td><td>28.77</td><td>35.8</td><td>26.3</td><td>20.1</td></tr><tr><td>ASIAX</td><td></td><td></td><td>1,966.72</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended  
003670.KS, 034020.KS base year is 2024;  
Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

In a structurally power-constrained world, solar-plus-storage is emerging as an increasingly important solution to deliver stable, baseload-like power, particularly for fast-growing AI and data center demand. The Masdar project demonstrates that, with sufficient overbuild and long-duration storage, renewables could achieve high system reliability while offering competitive economics in higher gas price environments, alongside the key advantages of being emissions-free and having no fuel price risk. While scalability remains dependent on geography, land availability, and grid infrastructure, the overall direction is clearly positive, with costs expected to decline further through scale and ongoing technology improvements, including next-generation batteries such as sodium-ion. As storage now drives system economics and demand continues to accelerate, we see strong upside for global ESS deployment and recommend Sungrow and CATL as key beneficiaries of this structural shift.

## DETAILS

The UAE's Masdar and EWEC project demonstrates at scale that solar-plus-storage can deliver firm baseload power. This fundamentally reframes the role of renewables: the key question is no longer whether solar can generate cheap energy, but whether it can reliably meet a continuous load profile when paired with sufficient storage and overbuild. The project combines 5.2 GW of solar with 19 GWh of storage to deliver \~1 GW of continuous power, with completion targeted by 2027. This represents the first gigascale attempt to overcome solar intermittency through system design, and therefore serves as a key proof point for the industry. We find that solar-plus-storage is increasingly cost competitive in higher gas price environments. At current cost levels, it can compete with gas-fired generation when fuel prices are elevated, making it an attractive alternative amid volatility in global gas markets. However, gas remains structurally advantaged in regions with persistently low fuel costs, such as the US.

EXHIBIT 1: Solar plus storage (12+ hours) are competitive against gas-fired power at high gas prices  
![](images/766e1072c17a7a2945458340dd99f33f7ce547889c423267c87e0442c09a7170.jpg)

<details>
<summary>line chart</summary>

| Gas price ($/mmbtu) | LCOE ($/MWh) |
| ------------------- | ------------ |
| 4                   | 65           |
| 17                  | 160          |
</details>

Source: Company data, Bernstein analysis

We estimate total project capex at approximately \$6bn for 1GW of firm solar-plus-storage capacity (or \~\$6,000/kW). This can be broadly broken down into \~\$0.5bn for solar modules, \~\$0.5bn for inverters and balance-of-plant, and \~\$2.5bn for ESS, with the remaining \~\$2.5bn covering grid/electrical infrastructure, EPC, land, and other development costs. The key takeaway is that while solar generation itself is already low cost, storage dominates the economics, accounting for roughly half of total system cost. As a result, the competitiveness of baseload solar-plus-storage is primarily driven by battery cost declines rather than further reductions in module pricing. This reinforces our view that continued cost reductions in ESS will be the critical enabler for scaling firm renewable power.

EXHIBIT 2: We estimate total project capex at approximately \$6bn (or \~\$6,000/kW). Energy storage dominates the economics  
![](images/6ee1c40b83014698da378c020f9f19d58dd7086427a3b0bac5d8c62075e4bc76.jpg)

<details>
<summary>bar chart</summary>

Project cost ($bn) for 5.2GW solar + 19GWh storage = 1GW baseload power
| Project developer | Project cost ($bn) |
| :--- | :--- |
| Solar module | 0.5 |
| Inverter and BOP | 0.5 |
| ESS (excl. EPC) | 2.5 |
| Other (Electrical, EPC, Land) | 2.5 |
Jinko Solar
JA SOLAR
CATL SUNGROW
Jinko MASDAI
EWEC
中国电建 POWERCHINA
Larsen & TOUBRO
</details>

CATL and Sungrow are covered by Bernstein. All other companies are not covered by Bernstein.  
Source: Company data, Bernstein analysis and estimates

Solar-plus-storage is emerging as a credible alternative to traditional baseload generation, offering several advantages over gas and nuclear, but with clear trade-offs. The Masdar project demonstrates that, with sufficient overbuild and long-duration storage, renewables can achieve near-baseload reliability (\~99% uptime), while also benefiting from faster deployment timelines of \~2 years compared to \~3–6 years for gas (given turbine bottlenecks) and \~6+ years for nuclear. Economically, solar-plus-storage is increasingly competitive in higher gas price environments, providing cost certainty without fuel price exposure. However, it remains constrained by geography, requiring high solar irradiance and large land footprints, and its economics are heavily dependent on battery costs, which account for \~50% of capex. By contrast, gas remains more flexible and competitive in low-cost fuel markets such as the US, while nuclear offers the highest level of clean baseload reliability but with significantly longer build times and higher execution risk. As such, solar-plus-storage can deliver very competitive firm power in select regions, particularly for new demand such as AI and data centers.

EXHIBIT 3: Comparison of solar-plus-storage, gas and nuclear power for baseload power

<table><tr><td>Metric</td><td colspan="2">Solar + Storage (12+ hours)</td><td colspan="2">Gas - CCGT</td><td colspan="2">Nuclear</td></tr><tr><td>Uptime</td><td>~90–99.x%</td><td>√</td><td>~95–99.9%</td><td>√</td><td>~95–99.9%</td><td>√</td></tr><tr><td>LCOE</td><td>~$80-100/MWh</td><td>√</td><td>~$50/MWh ($3.5/mmbtu) ~$110/MWh ($12/mmbtu)</td><td>√</td><td>~$50-150/MWh</td><td></td></tr><tr><td>Lead time</td><td>~2 years</td><td>√</td><td>~3–6 years</td><td></td><td>6+ years</td><td></td></tr><tr><td>Land requirement</td><td>~60 km2</td><td></td><td>~0.02–0.05 km2</td><td>√</td><td>~1–4 km2</td><td>√</td></tr><tr><td>Carbon emissions</td><td>Zero</td><td>√</td><td>~0.35–0.4 tCO2/MWh</td><td></td><td>Near zero</td><td>√</td></tr><tr><td>Fuel risk</td><td>none</td><td>√</td><td>gas - high fuel cost</td><td></td><td>uranium - low fuel cost</td><td>√</td></tr><tr><td>Bottleneck</td><td>location, grid connection</td><td></td><td>turbine supply, gas supply</td><td></td><td>long development</td><td></td></tr></table>

Assuming a build for 1GW of baseload power  
Source: Company data, Bernstein analysis

## SOLAR-PLUS-STORAGE PROVIDES BASELOAD POWER

The UAE's Masdar and EWEC project represents a step-change in solar-plus-storage system design. Rather than optimizing for peak shaving, it is engineered to deliver round-the-clock baseload power. By pairing 5.2 GW of solar with 19 GWh of storage, \~1 GW of continuous power output can be achieved to match stable power load of 1GW. This “abundance” is critical: excess midday generation is not curtailed but stored in the battery system (equivalent to \~19 hours of duration) and discharged through the evening and overnight. In effect, the project replaces curtailment with energy shifting, reshaping variable solar generation into a stable, near-continuous output profile.

EXHIBIT 4: By pairing 5.2 GW of solar with 19 GWh of storage, 1 GW of continuous power output can be achieved to match stable a power load of 1GW  
![](images/1f6874d0328f53d0f055f45f4d7df5793775d19865d89e118223cac414530413.jpg)

<details>
<summary>text_image</summary>

EWEC
Enagas Water & Electricity Co.
J20D
MASDAR
5 GW
19 GW Hrs
1 GW of
uninterrupted
power
</details>

Source: Company presentation

How does this work? With 5.2 GW of installed solar capacity, the project could generate approximately 12.45 TWh of annual solar output, implying a \~27% capacity factor based on the local irradiance profile. This equates to \~34 GWh per day of energy production vs. a constant 24 GWh/day load for 1 GW baseload, highlighting that the system is intentionally overbuilt by \~40% on an energy basis. Of this total generation, around 4.09 TWh is used to directly supply daytime demand, while \~4.62 TWh is stored in the battery during the day and discharged at nighttime to maintain continuous output. The remaining \~3.74 TWh represents surplus generation, which serves as headroom to meet storage losses, seasonal variability, and system reliability requirements. With this system, we estimate a 99.6% system reliability can be achieved.

EXHIBIT 5: Annual power output of the project (TWh). Solar and storage overbuilt enables continuous 1 GW output  
![](images/93a71d3e27a97e2b222951ec993cea66d135c06c85ed9f632ef2b0aa4501214b.jpg)

<details>
<summary>sankey diagram</summary>

| Category                  | Value |
| ------------------------- | ----- |
| Daytime supply            | 4.09  |
| Baseload served          | 8.71  |
| Battery charging          | 4.62  |
| Night discharge           | 4.62  |
| Reserve / curtailment / headroom | 3.74  |
</details>

Source: Company data, Bernstein analysis

We have carried out an analysis of what the operations and economics would look like for the project based on the region's irradiance profile and the system design. Building solar capacity in UAE offers significant advantages due to the region's abundant solar resources, characterized by high solar irradiance and vast available land, enabling large-scale, cost-effective solar power generation. Additionally, favorable government policy and expanding transmission infrastructure support export of electricity. Based on the irradiance profile, we expect the project can generate 12.45TWh of electricity generation with a 1-axis tilt and azimuth. On average, the annual capacity factor is approximately $27\%$ assuming no curtailment.

EXHIBIT 6: We have modeled 5.2GW of solar capacity. The solar farm can achieve an average capacity factor of 27% although we have not factored in curtailment and power load  
![](images/708b2c8e5f00e07804428887a292e1aa70e935e8f8a83967040de37de451f6db.jpg)

<details>
<summary>bar chart</summary>

| Month   | Capacity factor (%) |
|---------|---------------------|
| Jan-01  | 30%                 |
| Feb-01  | 30%                 |
| Mar-01  | 30%                 |
| Apr-01  | 30%                 |
| May-01  | 30%                 |
| Jun-01  | 30%                 |
| Jul-01  | 30%                 |
| Aug-01  | 30%                 |
| Sep-01  | 30%                 |
| Oct-01  | 30%                 |
| Nov-01  | 30%                 |
| Dec-01  | 30%                 |
| Jan-01  | 30%                 |
</details>

Source: Company data, Bernstein analysis

Solar has significant variability in capacity factor by months and hours of the day. Capacity factors are generally higher in summer months with longer daylight hours and stronger solar irradiance. Solar power generation are typically between 6am to 5pm with peak generation between 10am to 1pm where the sun's ray strikes the panels most directly.

EXHIBIT 7: Solar power is mostly generated between 7am to 5pm, which means there is no power for more than 12 hours of the day without storage or other power source  
![](images/d3b12dee66954262fd1da127931fff9a0cfbf2edf6ba491b49df0ee013ae9281.jpg)

<details>
<summary>line chart</summary>

| Hour of the day | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 10   | 11   | 12   | Average |
| --------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ------- |
| 0               | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%      |
| 1               | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%      |
| 2               | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%      |
| 3               | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%      |
| 4               | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%      |
| 5               | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%   | 0%      |
| 6               | ~10% | ~15% | ~20% | ~25% | ~30% | ~35% | ~40% | ~45% | ~50% | ~55% | ~60% | ~65% | ~70%    |
| 7               | ~45% | ~55% | ~65% | ~75% | ~85% | ~95% | ~98% | ~99% | ~98% | ~97% | ~96% | ~95% | ~95%    |
| 8             

[中间内容因长度限制已省略]

ence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
