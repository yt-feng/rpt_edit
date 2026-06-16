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
# U.S. Multi Industry & Electrical Equipment

# Liquid Cooling Primer: Coolant Distribution Units (CDUs)

![](images/f13458693f5e1f4b339a3cf948d9c760250d8006130740316344c2d0a512ef80.jpg)

Varun Govindaraj

+1 917 344 8543

varun.govindaraj@bernsteinsg.com

![](images/68025f75be50e36971277f7e8f494574c0988985456722e31e3dfa4a9009d791.jpg)

Chad Dillard

+1 917 344 8469

chad.dillard@bernsteinsg.com

![](images/93d2600c4731799d1fa68bfc2195c63b9b761966beba0b81ae02433e35fc753b.jpg)

Alasdair Leslie

+44 20 7762 4952

alasdair.leslie@bernsteinsg.com

![](images/2c5c8977c72bcba191e312391304afbd0f4d7bfa9b1978f2ca4ac5d40be0c151.jpg)

Madison Rezaei

+1 917 344 8622

madison.rezaei@bernsteinsg.com

## Specialist Sales

![](images/b681c380bc6081f83eb8971f65736a84d82c136998f7ec4b316b902800d3e43b.jpg)

Steve Song

+1 917 344 8401

steve.song@bernsteinsg.com

As rack thermal densities in data centers continue to increase, air is no longer powerful enough to handle cooling requirements. And so liquid cooling, once a fridge modality relegated to only the highest-performance computing use cases, increasingly finds itself in the mainstream. At the core of liquid cooling, two components drive the narrative (CDUs and Cold Plates). In this note, we offer perspectives on CDUs, why they are critical, how to evaluate them, key players in the market and their offerings, and a longer term view on what the future for the equipment could look like when the market eventually cools down (pun intended).

We think CDUs are a great business to be in; the equipment is complex enough to not be entirely commoditized and has a material service attach. They are mission-critical; if a CDU fails you are looking at multiple racks burning out (which is a huge issue today when rack values continue to increase). This also creates a technical moat where customers will want reliable service; they are unlikely to go to the lowest cost provider in the market because the cost of failure far outweighs the near-term savings a cheaper service contract can deliver.

While we have not opined on the market size of CDUs, there is clearly debate on both size and growth rates. We are comfortable with an LSD \$B market size for 2026, growing double digits (mid-teens+) over the next 5 years to get to MSD-HSD \$B by 2030. We have developed a proprietary liquid cooling model for this to be modeled; but market size is highly sensitive to GW added, cost per kW of cooling and CDU useful life (all of which are seeing debates). Reach out to the authors or your Bernstein sales contact if you'd like a walkthrough of how to use it.

Looking at the actual CDUs launched in the market today, there are many players, but not everyone is innovating or has a large scale unit. Players in the NVIDIA liquid cooling ecosystem (Vertiv, nVent, Boyd, Motivair) all have great products. Trane Technologies punches above its weight. Carrier and JCI have CDUs but given they are more focused on chillers, we found their CDU breadth, specifications, and level of detail provided to not be at the same level as the other names in this list. CoolIt seems to be more of a cold plate name; their approach temperature lags competitors.

As we think about the next five years, we believe that technology roadmap visibility (which comes from being a partner of NVIDIA since they really set the direction of change) and participation in the Open Compute Project (OCP) create a right to win (because it deepens hyperscaler relationships and creates a pathway for long-term demand generation); and not many companies can say they have both.

Lastly, we think the shift to two-phase DTC cooling (from single-phase) should be closely watched. Only Vertiv and Accelsius (from the companies we have mentioned in this note) have actually announced products / published detailed perspectives. While we're still at least a year out from commercially scaled offerings (if not more), and most other companies serious about liquid cooling are likely working on a product, the step-change in engineering from this shift has the potential to disrupt the market and position occupied by key players.

BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="3">12 Jun 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>VRT (Vertiv)</td><td>O</td><td>USD</td><td>302.87</td><td>416.00</td><td>141.6%</td><td>USD</td><td>4.20</td><td>6.52</td><td>9.21</td><td>72.2</td><td>46.4</td><td>32.9</td></tr><tr><td>NVT (nVent)</td><td>O</td><td>USD</td><td>165.84</td><td>218.00</td><td>114.8%</td><td>USD</td><td>3.34</td><td>4.79</td><td>6.19</td><td>49.6</td><td>34.6</td><td>26.8</td></tr><tr><td>CARR (Carrier)</td><td>M</td><td>USD</td><td>69.91</td><td>75.00</td><td>(26.5)%</td><td>USD</td><td>2.57</td><td>2.81</td><td>3.20</td><td>27.2</td><td>24.9</td><td>21.9</td></tr><tr><td>TT (Trane)</td><td>O</td><td>USD</td><td>458.25</td><td>550.00</td><td>(14.9)%</td><td>USD</td><td>13.06</td><td>14.96</td><td>17.61</td><td>35.1</td><td>30.6</td><td>26.0</td></tr><tr><td>JCI (Johnson Controls)</td><td>O</td><td>USD</td><td>144.96</td><td>176.00</td><td>17.0%</td><td>USD</td><td>3.78</td><td>5.06</td><td>6.04</td><td>38.4</td><td>28.6</td><td>24.0</td></tr><tr><td>SU.FP (Schneider)</td><td>O</td><td>EUR</td><td>265.30</td><td>310.00</td><td>3.8%</td><td>EUR</td><td>8.43</td><td>10.22</td><td>11.95</td><td>31.5</td><td>26.0</td><td>22.2</td></tr><tr><td>ETN (Eaton)</td><td>O</td><td>USD</td><td>391.39</td><td>534.00</td><td>(4.4)%</td><td>USD</td><td>12.07</td><td>13.29</td><td>16.32</td><td>32.4</td><td>29.4</td><td>24.0</td></tr><tr><td>SPX</td><td></td><td></td><td>7,431.46</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EDME</td><td></td><td></td><td>1,570.59</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended  
Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We rate VRT Outperform with a target price of \$416.

We rate NVT Outperform with a target price of \$218.

We rate CARR Market-Perform with a target price of \$75.

We rate TT Outperform with a target price of \$550.

We rate JCI Outperform with a target price of \$176.

We rate Schneider Outperform with a target price of €310.

We rate Eaton Outperform with a target price of \$534.

## DETAILS

EXHIBIT 1: CDU Outlook Summary

## CDUs | We think CDUs are here to stay; some commoditization risk (but less than cold plates)

<table><tr><td>Timeframe</td><td>Near-term(2026–2028)</td><td>Mid-term(2028–2030)</td><td>Long-term(2030+)</td></tr><tr><td>Risk ofCommoditization</td><td>Low</td><td>Moderate</td><td>Moderate</td></tr><tr><td>Risk ofObsolescence</td><td>Low</td><td>Low</td><td>Low</td></tr><tr><td>Commentary</td><td>Near-term, we expectCDUs to be a growth driverfor anyone with exposure toliquid cooling from DCsWe expect the market tobe supply constrained;anyone with a CDU offeringwill probably see largebacklogs through 2028While there are somecommoditization risks fromprograms like OCP, ProjectDeschutes, etc. we believethe pace of productevolutionlargely supportsvendor pricing power</td><td>Regardless of whetherimmersion cooling or DTC isthe dominant configurationat this point, CDUs will stillbe required (so there is noobsolescence risk)We do expect the liquidcooling market to be muchmore mature at this pointand think there is largerpossibilitythat specs.become standardizedHowever, service quality /uptime will remainrelevant(especially if CDUsmove to the facility level vs.rack level), enabling CDUplayers todrive revenuefrom their install base vs.new equipment sales</td><td>Even in a config. with silicon etched microchannels,CDUs will remain relevant(and if anything, become more important asthe flow volume / pressure become critical to finely control)We think CDUs will be able to retain some pricingpower long-term even ifthey are fully specified by hyperscalersat this point –driven by a combination ofhigher complexity(esp. compared to cold plates)and theneed for serviceonce CDUs installedGiven the high value of racks, wedo not think theservice can be outsourced to third-party non-OEMs</td></tr></table>

Practically no obsolescence risk; we think CDUs are here to stay regardless of the dominant cooling config.

Some commoditization risk; hyperscalers will specify designs but CDUs are more complex (multiple connected pieces) than cold plates which preserves pricing power

In addition, CDUs need service (which cold plates do not) which also defends margin

We think CDUs are a great business to be in, ESPECIALLY for companies that can drive the innovation roadmap vs. just become contract mfg.

We see wide dispersion of forecasts for broader CDU market; but an LSD \$B market size today growing MSD/HSD \$B in the next 5 years does not seem too improbable

EXHIBIT 2: Comparison of Flagship Liquid-to-Liquid CDUs across OEMs

<table><tr><td>Company</td><td>Product</td><td>Configuration</td><td>TCS Flow rate1</td><td>Capacity1</td><td>Flow ratio</td><td>ATD2</td><td>Pressure Head</td><td>Modularity</td></tr><tr><td rowspan="4">VRT3</td><td>Coolchip 121</td><td>Rack</td><td>120 lpm</td><td>121 kW</td><td>1 lpm / kW</td><td>4°C</td><td>17 psi</td><td>No</td></tr><tr><td>Coolchip 1350</td><td>Row</td><td>1200 lpm</td><td>1.37 MW</td><td>0.9 lpm / kW</td><td>4°C</td><td>35 psi</td><td>No</td></tr><tr><td>Coolchip 2300</td><td>Row/Perimeter</td><td>3400 lpm</td><td>2.3 MW</td><td>1.5 lpm / kW</td><td>4°C</td><td>Expected &gt;50 psi</td><td>Cluster control</td></tr><tr><td>Deschutes 5.0</td><td>Row/Perimeter</td><td>1900 lpm</td><td>2 MW</td><td>0.9 lpm / kW</td><td>3°C</td><td>80 psi</td><td>N/A</td></tr><tr><td rowspan="4">NVT</td><td>Rackchiller 100</td><td>Rack</td><td>N/A</td><td>100 kW</td><td>N/A</td><td>4°C</td><td>N/A</td><td>No</td></tr><tr><td>Rackchiller 800</td><td>Row</td><td>690 lpm</td><td>575 kW</td><td>1.2 lpm / kW</td><td>4°C</td><td>~50 psi4</td><td>No</td></tr><tr><td>CZ and CX series</td><td>CZ (rack)/CX (row)</td><td colspan="5">To be released in 2H 2026; expected to be bleeding edge technology</td><td>Advertised</td></tr><tr><td>Deschutes 5.0</td><td>Row/Perimeter</td><td>1900 lpm</td><td>2MW</td><td>1.1 lpm / kW</td><td>3°C</td><td>80 psi</td><td>N/A</td></tr><tr><td rowspan="2">TT</td><td>CDU-1MW</td><td>Row</td><td>1500 lpm</td><td>1.35 MW</td><td>1.1 lpm / kW</td><td>4°C</td><td>40 psi</td><td>No</td></tr><tr><td>Giga-modular CDU</td><td>Row/Perimeter</td><td>3900 lpm</td><td>2.5 MW</td><td>&gt;1.5 lpm / kW</td><td>3°C</td><td>50 psi</td><td>Yes, up to 14MW</td></tr><tr><td>JCI</td><td>Silent-Aire</td><td>Row/Perimeter</td><td>1600 lpm</td><td>1.05 MW</td><td>1.5 lpm / kW</td><td>5.2°C</td><td>30 psi</td><td>10 MW (skid only)</td></tr><tr><td>CARR5</td><td>QL 65LL</td><td>Row/Perimeter</td><td>N/A</td><td>1.35 MW</td><td>N/A</td><td>2 - 4°C8</td><td>N/A</td><td>5 MW (skid only)</td></tr><tr><td rowspan="5">Boyd</td><td>RAL110-04U19</td><td>Rack</td><td>80 lpm</td><td>80 kW</td><td>1 lpm / kW</td><td>8°C</td><td>21 psi</td><td>No</td></tr><tr><td>RAL300-04U21</td><td>Rack</td><td>160 lpm</td><td>160 kW</td><td>1 lpm / kW</td><td>5°C</td><td>25 psi</td><td>No</td></tr><tr><td>ROL1100-48U32</td><td>Row</td><td>473 lpm</td><td>550 kW</td><td>1 lpm / kW</td><td>4°C</td><td>30 psi</td><td>No</td></tr><tr><td>ROL2300-48U40</td><td>Row</td><td>1514 lpm</td><td>1150 kW</td><td>1.3 lpm / kW</td><td>4°C</td><td>55 psi</td><td>No</td></tr><tr><td>ROL4000-48U65</td><td>Row/Perimeter</td><td>1893 lpm</td><td>2 MW</td><td>0.9 lpm / kW</td><td>3°C</td><td>80 psi</td><td>No</td></tr><tr><td rowspan="3">Motivair6</td><td>MCDU 45</td><td>Row</td><td>1166 lpm</td><td>853 kW</td><td>1.4 lpm / kW</td><td>4°C</td><td>29 psi</td><td>No</td></tr><tr><td>MCDU 55</td><td>Row</td><td>1632 lpm</td><td>728 kW</td><td>&gt;1.5 lpm / kW</td><td>4°C</td><td>51 psi</td><td>No</td></tr><tr><td>MCDU 70</td><td>Row/Perimeter</td><td>3751 lpm</td><td>2.5 MW</td><td>&gt;1.5 lpm / kW</td><td>4°C</td><td>38 psi</td><td>Yes, up to 10MW</td></tr><tr><td rowspan="3">CoolIT</td><td>CHx80</td><td>Rack</td><td>N/A</td><td>80 kW</td><td>N/A</td><td>N/A (expect MSD)</td><td>N/A</td><td>No</td></tr><tr><td>CHx200</td><td>Rack</td><td>N/A</td><td>200 kW</td><td>N/A</td><td>N/A (expect MSD)</td><td>N/A</td><td>No</td></tr><tr><td>CHx20007</td><td>Row/Perimeter</td><td>2125 lpm</td><td>2 MW</td><td>1.05 lpm / kW</td><td>5°C</td><td>35 psi</td><td>Cluster Control</td></tr></table>

Note: Liquid-to-liquid only; We have focused primarily on CDUs released around or after mid-2024; OEM specs are often intentionally complex; we have made our best attempt at representing data here; 1. Nominal; 2. Approach temp. differential; 3. Unclear if water / PG25; 4. Inferred from spec sheet at 690 lpm; 5. Unclear if water/PG25 rated; 6. Water rated (so actual numbers will be lower); 7. CoolIT published different specs for the same product; we have used PDP details; CHx1500 not shown as it does not have a distinct PDP; 8. $^{2}$ °C ATD available using a high-efficiency heat exchanger  
Source: Bernstein Analysis and Estimates, Company Reports

## INTRODUCTION

In the past, a continuous flow of cool air over servers was sufficient to cool data centers. With time, chips and racks have grown increasingly dense, to the point where even freezing cold air blowing at gale force speeds wouldn't do the job. Needless to say, finding an alternative cooling modality became critical. And so, liquid cooling technology, which long sat at the fringe of data center infrastructure, suddenly found itself thrust into the spotlight. Looking ahead, rack densities and chip TDPs seem set to keep growing, forcing liquid cooling solutions to evolve with more rigorous server demands.

## OVERVIEW OF LIQUID COOLING

Liquid cooling encompasses multiple different types of technology, with varying levels of efficiency and at distinct stages of maturity. At their core, they share one common principle; liquid flows over a surface (directly or indirectly) and uses principles of convection to extract heat. We describe five modalities of liquid cooling below:

1. Single-phase DTC: The predominant format of liquid cooling today. DTC stands for Direct-To-Chip. It involves cold plates (which are aptly named slabs of metal that have reduced temperature due to refrigerant that circulates inside them) coming into contact with racks / chips to extract heat. Coolant Distribution Units (CDUs) pump low temperature coolant (usually a water - propylene glycol mix) through the plates and recollect the spent liquid once they have extracted heat from the server. The heat is then extracted from the coolant (making it cold again) and the process repeats. It is called single phase because the coolant stays in a single phase (liquid) and does not change phases from to gas via evaporation. This loop (i.e., circulating from the CDU through cold plates in the server) is called the TCS or technology cooling system. Once spent coolant reaches the CDU, it passes through a heat exchanger where it transfers heat to another cooling loop called the FWS or Facility Water System. The FWS connects to a chiller or dry cooler to reject this heat outside a data center. However, as rack power densities continue to increase, single phase DTC is seemingly reaching the theoretical limit of how much heat it can extract.  
2. Two-phase DTC: The principles remain exactly the same as single phase DTC, but in this case the liquid coolant boils and evaporates when it comes in contact with the server after absorbing heat. Evaporation requires significant energy, so it enables the refrigerant to extract a lot of heat without having its own temperature rise too much. In most cases, the refrigerant is maintained as close to its boiling point as possible. Not yet mainstream, but a number of companies are experimenting at the lab scale and approaching commercial maturity (which is expected over the next couple of years). It is worth noting that capacities of CDUs that support two-phase liquid are limited; Accelsius for example has a relatively mature offering and their highest capacity CDU is well below 1MW (vs. 2MW+ for single phase cooling). Equipment (both CDUs and cold plates) need to be designed differently for two-phase; gas flowing through an ecosystem behaves much differently from liquid.  
3. Immersion cooling: Once a competitor to DTC, now largely relegated to niche applications. Does not need cold plates; the entire server is submerged in dielectric (i.e., non-conducting) fluid which extracts heat. Has both single phase and two-phase versions. Fell off due to convenience; cold plates can rapidly be replaced and servers can still be maintained with relative ease, in contrast, immersion cooling requires a large tank to be moved, and a wet server to be extracted and dried before any work can be done on it. R&D is still taking place, but hyperscaler roadmaps clearly lean towards DTC.  
4. Cold plate etched DTC: Micro-channels are etched into the surface of a cold plate to improve contact with the chip surface. Enables better heat transfer compared to traditional single phase or two-phase DTC but still very nascent tech.  
5. Silicon-etched DTC: Forgoes cold plates entirely and etches cooling channels on the surface of the chip itself. Very nascent, unlikely to see commercialization before the end of the decade, although key players like Microsoft and TSMC are making investments here.

The reason we have laid out these technologies is that it has implications on the outlook of equipment that make up the liquid cooling ecosystem. CDUs and cold plates are the most important to discuss. CDUs (Coolant Distribution Units) are essentially responsible for controlling the distribution, flow, and pressure of coolant across multiple rows and racks. Cold plates receive coolant from CDUs (via a manifold) and absorb heat through their surface before returning the spent coolant to the CDU. Both these components are seeing significant demand (and shortages today) and there has been a flurry of investment activity in the space with larger players making strategic investments and acquisitions (e.g., JCI investing in Accelsius, Eaton acquiring Boyd). In today's note, we focus specifically on CDUs.

EXHIBIT 3: Overview of 

[中间内容因长度限制已省略]

nce system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
