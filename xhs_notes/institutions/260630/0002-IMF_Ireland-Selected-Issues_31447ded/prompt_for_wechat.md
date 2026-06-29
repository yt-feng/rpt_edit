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
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`IMF`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
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
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：加入社群，领取完整研报解读与原始图表。。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份IMF研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## IRELAND

## SELECTED ISSUES

June 2026

This paper on Ireland was prepared by a staff team of the International Monetary Fund as background documentation for the periodic consultation with the member country. It is based on the information available at the time it was completed on June 10, 2026.

Copies of this report are available to the public from

International Monetary Fund • Publication Services
PO Box 92780 • Washington, D.C. 20090
Telephone: (202) 623-7430 • Fax: (202) 623-7201
E-mail: publications@imf.org Web: http://www.imf.org

International Monetary Fund
Washington, D.C.

## IRELAND

SELECTED ISSUES

June 10, 2026

Approved By

Prepared by Mohammad Khabbazan (ICD)

European Department

## CONTENTS

ESTIMATING THE IMPACTS OF AI, TRADE POLICY, AND THE ENERGY TRANSITION: AN APPLICATION TO IRELAND 3
A. Introduction 3
B. Model Framework and Scenario Design 4
C. Tariff and Trade Agreements: Re-Shaping Global Trade 7
D. Artificial Intelligence and Productivity Gains 10
E. Carbon Pricing Policy and Trade-Offs 15
F. Concluding Remarks 20

## FIGURES

1. Real GDP and Price Index Impacts in Tariff and Trade Agreements Scenarios 7
2. Real Export and Export Price Impacts in Tariff and Trade Agreements Scenarios 8
3. Selected Sectoral Real Output and Real Export Impacts in Tariff and Trade Agreements Scenarios 10
4. Selected Sectoral Labor Movement in Tariff and Trade Agreements Scenarios 10
5. Real GDP and Price Index Impacts in AI-Driven Productivity Gains Scenarios 11
6. Real Export and Export Price Impacts in AI-Driven Productivity Gains Scenarios 12
7. Selected Sectoral Real Output and Real Export Impacts in AI-Driven Productivity Gains Scenarios 13
8. Renewable Share in Electricity Productions and CO2 Emission in AI-Driven Productivity Gains Scenarios 14
9. Selected Sectoral Labor Movement in AI-Driven Productivity Gains Scenarios 15
10. Real GDP and Price Index Impacts in Carbon Pricing Policy Scenarios 16
11. Renewable Share in Electricity Productions and Carbon Price in Carbon Pricing Policy Scenarios 17
12. Real Export and Export Price Impacts in Carbon Pricing Policy Scenarios 18
13. Selected Sectoral Real Output and Real Export Impacts in Carbon Pricing Policy Scenarios 19

14. Selected Sectoral Labor Movement in Carbon Pricing Policy Scenarios \_\_\_\_ 19

## TABLES

1. Scenario Description \_\_\_\_ 6
2. Trade Flows in Tariff and Trade Agreements Scenarios \_\_\_\_ 9
3. Selected Macro Indicators in Tariff and Trade Agreements Scenarios \_\_\_\_ 9
4. Trade Flows in AI-Driven Productivity Gains Scenarios \_\_\_\_ 12
5. Selected Macro Indicators in AI-Driven Productivity Gains Scenarios \_\_\_\_ 14
6. Trade Flows in Carbon Pricing Policy Scenarios \_\_\_\_ 18
7. Selected Macro Indicators in Carbon Pricing Policy Scenarios \_\_\_\_ 18

## ANNEXES

I. The Economic Structure of the Model and the Key Substitution Elasticities 21
II. Sectoral Mapping 24
III. Sectoral Results 26
IV. Labor Movement 28
References 29

# ESTIMATING THE IMPACTS OF AI, TRADE POLICY, AND THE ENERGY TRANSITION: AN APPLICATION TO IRELAND $^{1}$

Developments in trade policy, AI, and the energy transition are shaping small open economies. This paper uses a static, multi-region, multi-sector computable general equilibrium model to assess the impacts of these forces on Ireland in the long run through three channels: (i) current tariffs and trade agreements, (ii) AI-driven productivity gains, and (iii) carbon pricing, abstracting from short-run dynamics and frictions. The findings suggest that (i) the current trade policy shocks primarily redirect trade across partners and sectors, with modest aggregate output and export effects; (ii) AI-driven productivity gains can generate strong output and export growth, particularly in knowledge-intensive sectors, while inducing significant sectoral labor reallocation and distributional implications across factors of production which needs to be managed; (iii) carbon pricing can play a key role in addressing rising energy demand from AI and offsetting emissions, by shifting production toward lower-emission activities and increasing the renewable share in electricity generation.

## A. Introduction

1. Artificial intelligence, trade policy shifts, and the energy transition are simultaneously reshaping the outlook for small open economies. For Ireland, these structural forces are particularly salient given the economy's openness, deep integration into global value chains, and specialization in high-value tradable sectors. Changes in tariff regimes and the emergence of new trade agreements can alter relative market access and reconfigure export patterns, while AI-driven productivity gains offer scope to strengthen competitiveness through the supply side. At the same time, productivity-led expansion raises energy demand and emissions, intensifying policy trade-offs around climate objectives and the electricity mix. Understanding how trade policy, technological change, and climate policy interact is therefore central to assessing their implications for Ireland's product and labor markets, growth prospects, and progress toward decarbonization.

2. To assess these interactions quantitatively, this paper brings trade policy, AI-driven productivity gains, and climate policies together within a single, integrated analytical framework. Using a multi-region, multi-sector computable general equilibrium model calibrated to a 2025 baseline, the analysis embeds granular tariff data and sector- and region-specific AI productivity shocks, allowing policy changes and technological advances to interact consistently through relative prices, production structures, bilateral trade flows, and factor markets. The framework highlights the distinct and interrelated channels through which trade policy re-routes activity across markets, AI amplifies growth and competitiveness through the supply side, and

carbon pricing reshapes sectoral composition and energy use. By comparing standalone and combined scenarios, the paper clarifies whether trade adjustment operates primarily through prices or quantities, how AI-driven productivity reshapes Ireland's economic structure, and the extent to which climate policy may temper productivity-led expansion—ultimately shedding light on how policy choices affect Ireland's ability to reconcile strong growth with decarbonization objectives.

## B. Model Framework and Scenario Design

3. The paper aims to quantify Ireland's adjustment to trade shocks, AI-related productivity changes, and climate policy using a multi-region, multi-sector computable general equilibrium (CGE) model. The analysis is implemented in CGE-MOD (Khabbazan and Von Hirschhausen, 2021), a static general equilibrium framework designed to capture economy-wide spillovers through relative prices, trade flows, sectoral reallocation, and factor markets. The model features nested constant elasticity of substitution (CES) technologies and a standard Armington trade structure: inputs are differentiated by origin, while domestic output is allocated between domestic and export markets via constant elasticity of transformation (CET) functions, so trade shocks operate through wedges between import and domestic prices that induce substitution, trade diversion, and resource reallocation across sectors. Labor and capital are mobile across sectors within each region, while an immobile natural-resource factor anchors fossil-fuel supply, allowing for region-specific supply responses and the emergence of natural-resource rents. Annex I presents the economic structure of the model and the key substitution elasticities, calibrated using standard values from the literature. All factor incomes—labor, capital, and natural resources—as well as tax revenues accrue to the representative household in the model, so changes in household income reflect their combined evolution.

## 4. The framework features an explicit treatment of energy, allowing emissions to

respond through both activity and composition channels. Electricity generation is disaggregated by technology, including renewables, nuclear, fossil-fuel-based generation, and other sources, so that changes in relative costs induce substitution across power technologies, while $CO_{2}$ emissions are linked to fuel use through fixed emissions coefficients. The model also allows for carbon pricing and emissions trading systems, ensuring that policy-driven changes in carbon costs are transmitted consistently through production decisions, energy use, and emissions outcomes. This structure is essential for interpreting scenarios in which shifts in the electricity generation mix either reinforce or offset changes driven by aggregate economic activity.

5. The model is benchmarked to the Global Trade Analysis Project (GTAP) database and calibrated to a 2025 baseline. Specifically, the GTAP 11 Power dataset is used as the benchmark, providing internally consistent data on production, consumption, bilateral trade, energy use, and CO $_{2}$ emissions. To align the analysis with Ireland's policy questions, the global economy is aggregated into eight regions—Ireland, the rest of the European Union, the United States, the United Kingdom, China, India, Mercosur, and the rest of the world—and 44 economic sectors (see Annex II for the sector mapping). Baseline calibration draws on historical data and projections for GDP and CO $_{2}$ emissions over 2017–25, using IMF projections (IMF, 2024) to anchor regional macroeconomic paths. Regional factor endowments—labor, capital, and natural resources—are

scaled using a common adjustment factor to match projected aggregates, and where relevant, sector-specific production features and either market-based carbon pricing or taxes on $CO_{2}$ -emitting intermediate inputs are incorporated to ensure consistency with emissions projections and the energy mix. For Ireland, an initial economy-wide carbon price of around USD 72.3 per ton of $CO_{2}$ is incorporated in the baseline, reflecting both EU Emissions Trading System pricing and domestic carbon taxation. $^{2}$ Policy simulations are conducted as comparative statics relative to this baseline, and results should therefore be interpreted as medium-to-long-run reallocations rather than short-run dynamics. The 2025 baseline abstracts from the U.S. tariff increases, which are introduced only in the counterfactual tariff scenarios.

## 6. Several counterfactual scenarios are of main interest in the case of Ireland and are organized into three groups. These are:

• Tariff and Trade Agreements scenarios include the end-2025 tariffs imposed by the United States

and counterfactual trade agreements between the EU and Mercosur and between the EU and India, as well as a combination of these policy changes. Tariff inputs are drawn from the WTO Tariff & Trade Data (TTD) platform, using the WTO–IMF Tariff Tracker that records changes in effectively applied duties at the tariff line level and provides standardized aggregations to HS 6 and GTAP product categories with implementation dates. Trade agreements are modeled as reductions in

![](images/a535e9ad618cde4a43d4c8ea96d96dd41bb1012f0c254c64067ef8d8d321150b.jpg)

bilateral goods tariffs to zero for the relevant partners; non-tariff barriers are not included, so the scenarios isolate the general equilibrium effects of tariff changes operating through relative prices, trade diversion, and sectoral reallocation (see Table 1).

\- AI-driven Productivity Gains scenarios implement sector- and region-specific productivity improvements that raise efficiency while reshaping sectoral factor demand and the composition of income. The calibration of productivity shocks follows published evidence on AI exposure and adoption, drawing on Cerutti et al. (2025) and OECD (2025), and is implemented under low, medium, and high variants to reflect uncertainty about the pace and breadth of diffusion. These scenarios are designed to map differences in AI intensity across sectors and countries into macroeconomic outcomes through general equilibrium adjustments in production, trade, and factor allocation (see Table 1). AI-driven productivity gains are assumed to occur across all regions, with heterogeneous sector- and country-specific magnitudes, implying that Ireland's results reflect relative rather than unilateral productivity gains.

\- Carbon Pricing Policy scenarios allow the carbon price instrument to adjust where relevant, either to offset the emissions implications of AI productivity shocks (keeping emissions at their baseline level) or to achieve a 20 percent reduction in emissions relative to baseline in the absence of AI. The policy is represented through an additional carbon price over the calibrated baseline, generating associated carbon revenues and inducing reallocation across energy sources and sectors, including through changes in the electricity mix (see Table 1). The simulations impose economy-wide carbon pricing across all sectors, while current policy coverage in Ireland remains incomplete.

7. Interpretation of the results should take into account the scope and simplifying assumptions of the modeling framework. The analysis is conducted in a static general-equilibrium setting and should therefore be interpreted as comparing alternative equilibrium outcomes in the medium to long term, rather than tracing short-run dynamics or transition paths. In this framework, AI adoption is modeled as an exogenous, sector- and region-specific productivity improvement, abstracting from the endogenous accumulation of AI capital, skills, and innovation capacity, as well as from potential labor displacement or unemployment effects. The framework abstracts from AI-specific energy use (for example, data-center demand), capturing only the indirect effects of AI through higher aggregate activity. The analysis also abstracts from uncertainty around key drivers, including future trade policy developments, the scale and diffusion of AI productivity gains, climate impacts, and climate policy responses, which could affect the results. Climate policy is represented through carbon pricing as a stylized instrument to internalize emissions costs, with both carbon pricing revenues and other tax revenues rebated lump-sum to households. Accordingly, the analysis does not incorporate the full range of Ireland's climate policy framework, including the targets and renewable energy policies set out in the Government's Climate Action Plan 2025 (Department of Climate, Energy and the Environment, 2025), for example, policies supporting onshore and offshore wind, solar, and related energy measures. Alternative policy instruments, such as regulations or subsidies, are not explicitly modeled. While these simplifying assumptions limit the analysis of adjustment dynamics and distributional frictions, they allow for a transparent characterization of the economy-wide reallocation, price, and trade channels through which trade policy, AI-driven productivity gains, and climate policies jointly shape Ireland's equilibrium outcomes.

<table><tr><td colspan="3">Table 1. Ireland: Scenario Description</td></tr><tr><td>Group</td><td>Scenario</td><td>Scenario Description</td></tr><tr><td rowspan="4">Tariff and Trade Agreements</td><td>USTar</td><td>End-2025 U.S. tariffs on trading partners, differentiated by region and sector.</td></tr><tr><td>EUMSC</td><td>EU and Ireland eliminate bilateral tariffs with Mercosur.</td></tr><tr><td>EUIND</td><td>EU and Ireland eliminate bilateral tariffs with India.</td></tr><tr><td>UST+FT</td><td>U.S. tariffs combined with EU trade agreements with Mercosur and India.</td></tr><tr><td rowspan="3">AI-driven Productivity Gains</td><td>AI-L</td><td>Low AI-driven productivity gains across all regions and sectors.</td></tr><tr><td>AI-M</td><td>Medium AI-driven productivity gains across all regions and sectors.</td></tr><tr><td>AI-H</td><td>High AI-driven productivity gains across all regions and sectors.</td></tr><tr><td rowspan="4">Carbon Pricing Policy</td><td>AIL-CP</td><td>Low AI productivity gains with carbon pricing to keep Ireland&#x27;s emissions at baseline.</td></tr><tr><td>AIM-CP</td><td>Medium AI productivity gains with carbon pricing to keep Ireland&#x27;s emissions at base</td></tr><tr><td>AIH-CP</td><td>High AI productivity gains with carbon pricing to keep Ireland&#x27;s emissions at baseline.</td></tr><tr><td>CARB20</td><td>Carbon pricing in Ireland to reduce emissions by 20 percent relative to baseline.</td></tr></table>

## C. Tariff and Trade Agreements: Re-Shaping Global Trade

8. Trade policy shocks affect Ireland primarily through trade reallocation rather than through large aggregate output effects. Consistent with standard trade theory, the tariff shock has negative global effects in the model: world real output declines by 0.13 percent and global real exports fall by 2.84 percent, while the global price index rises by 0.64 percent, even as activity is redistributed across countries and sectors. Globally, tariff changes are uneven across sectors and partners, and pharmaceuticals face comparatively lighter tariff increases than many other traded goods, which tends to cushion Ireland's core export base given its specialization. At the same time, preferential trade agreements operate through improved market access, generating trade creation and diversion as bilateral tariffs are reduced to zero for partner pairs. Taken together, these forces imply that Ireland's adjustment shows most clearly in shifts in export composition, bilateral trade patterns, and sectoral activity, rather than in headline macroeconomic aggregates. The limited aggregate effects reflect economy-wide reallocation of labor and capital across sectors, which offsets large sector- and partner-specific export shifts at the macro level.

9. Aggregate macroeconomic effects of the trade scenarios are modest. Ireland's real GDP increases marginally under the U.S. tariff shock, and the increase remains below 0.20 percent even when tariffs are combined with the two EU trade agreements. The modest positive GDP response reflects a reallocation toward relatively higher-value and less-tariff-exposed export activities—most notably pharmaceuticals—combined with factor reallocation toward more capital-intensive sectors, which offsets negative demand effects at the aggregate level. These results indicate that the dominant adjustment margin is reallocation rather than a broad-based shift in domestic activity (Figure 1). The limited aggregate impact of the EU–Mercosur and EU–India agreements is consistent with their tariff-only design: by reducing bilateral tariffs to zero, these scenarios m

[中间内容因长度限制已省略]

47</td><td>-10.56</td><td>-2.26</td><td>-6.56</td><td>-9.29</td><td>2.09</td></tr><tr><td>OMF</td><td>-15.56</td><td>0.01</td><td>0.80</td><td>-14.53</td><td>-2.47</td><td>-6.75</td><td>-9.83</td><td>-2.01</td><td>-5.55</td><td>-8.14</td><td>2.68</td></tr><tr><td>ATP</td><td>0.38</td><td>-0.02</td><td>0.12</td><td>0.48</td><td>1.12</td><td>2.98</td><td>4.16</td><td>-2.73</td><td>-7.29</td><td>-10.50</td><td>-20.74</td></tr><tr><td>WTP</td><td>-1.42</td><td>0.11</td><td>0.08</td><td>-1.23</td><td>1.27</td><td>3.52</td><td>4.75</td><td>-0.31</td><td>-0.85</td><td>-1.64</td><td>-9.00</td></tr><tr><td>OTP</td><td>0.29</td><td>0.02</td><td>0.03</td><td>0.33</td><td>2.91</td><td>7.76</td><td>11.37</td><td>2.79</td><td>7.41</td><td>10.85</td><td>-0.70</td></tr><tr><td>AFS</td><td>2.06</td><td>-0.01</td><td>-0.06</td><td>1.99</td><td>3.75</td><td>10.18</td><td>14.64</td><td>3.79</td><td>10.31</td><td>14.83</td><td>0.12</td></tr><tr><td>WHS</td><td>0.15</td><td>0.01</td><td>0.04</td><td>0.20</td><td>2.89</td><td>7.85</td><td>11.30</td><td>2.27</td><td>6.18</td><td>8.89</td><td>-3.40</td></tr><tr><td>CNS</td><td>0.33</td><td>0.00</td><td>-0.01</td><td>0.31</td><td>-1.23</td><td>-3.54</td><td>-5.06</td><td>-1.19</td><td>-3.43</td><td>-4.90</td><td>0.23</td></tr><tr><td>OSG</td><td>0.43</td><td>0.00</td><td>-0.01</td><td>0.41</td><td>-1.47</td><td>-3.70</td><td>-5.29</td><td>-1.45</td><td>-3.65</td><td>-5.22</td><td>0.10</td></tr><tr><td>EDU</td><td>0.37</td><td>0.01</td><td>0.00</td><td>0.38</td><td>-0.08</td><td>0.07</td><td>0.20</td><td>-0.08</td><td>0.07</td><td>0.20</td><td>-0.03</td></tr><tr><td>HHT</td><td>0.50</td><td>0.01</td><td>0.00</td><td>0.50</td><td>-0.84</td><td>-1.87</td><td>-2.61</td><td>-0.84</td><td>-1.86</td><td>-2.60</td><td>0.00</td></tr><tr><td>WTR</td><td>0.18</td><td>0.01</td><td>0.02</td><td>0.20</td><td>1.17</td><td>3.34</td><td>4.90</td><td>1.12</td><td>3.20</td><td>4.69</td><td>-0.31</td></tr><tr><td>TRD</td><td>-0.28</td><td>0.01</td><td>0.01</td><td>-0.26</td><td>2.02</td><td>5.52</td><td>7.84</td><td>2.04</td><td>5.56</td><td>7.89</td><td>0.04</td></tr><tr><td>CMN</td><td>-0.61</td><td>0.02</td><td>-0.05</td><td>-0.63</td><td>-0.27</td><td>-1.39</td><td>-2.08</td><td>-0.19</td><td>-1.17</td><td>-1.79</td><td>0.44</td></tr><tr><td>FIN</td><td>1.43</td><td>-0.05</td><td>-0.08</td><td>1.30</td><td>0.60</td><td>1.42</td><td>1.83</td><td>0.77</td><td>1.89</td><td>2.51</td><td>0.95</td></tr><tr><td>REA</td><td>-0.43</td><td>0.01</td><td>0.02</td><td>-0.40</td><td>2.55</td><td>6.18</td><td>8.60</td><td>2.54</td><td>6.16</td><td>8.56</td><td>-0.09</td></tr><tr><td>OBS</td><td>1.89</td><td>-0.07</td><td>-0.09</td><td>1.73</td><td>-1.28</td><td>-3.57</td><td>-5.17</td><td>-1.20</td><td>-3.36</td><td>-4.88</td><td>0.44</td></tr><tr><td>ROS</td><td>0.54</td><td>0.02</td><td>0.03</td><td>0.59</td><td>2.75</td><td>7.57</td><td>10.85</td><td>2.51</td><td>6.93</td><td>9.92</td><td>-1.34</td></tr></table>

## References

Aguiar, A., M. Chepeliev, E. Corong, and D. van der Mensbrugghe. 2023. The Global Trade Analysis Project (GTAP) Data Base: Version 11. Journal of Global Economic Analysis 7 (2).

Beckman, J., T. Hertel, and W. Tyner. 2011. Validating Energy-Oriented CGE Models. Energy Economics 33 (5): 799–807.

Böhringer, C., and T. Rutherford. 2010. The Costs of Compliance: A CGE Assessment of Canada's Policy Options under the Kyoto Protocol. World Economy 33 (2): 177–211.

Cerutti, E., A. Garcia Pascual, Y. Kido, L. Li, G. Melina, M. M. Tavares, and P. Wingender. 2025. The Global Impact of AI: Mind the Gap. IMF Working Paper No. 25/76, International Monetary Fund, Washington, DC.

Chepeliev, M. 2023. GTAP-Power Data Base: Version 11. Journal of Global Economic Analysis 8 (2): 100–133. Center for Global Trade Analysis, Purdue University.

Department of Climate, Energy and the Environment. 2025. "Climate Action Plan 2025." Government of Ireland. Available at: https://www.gov.ie/en/department-of-the-taoiseach/publications/climate-action-plan-progress-reports/#climate-action-plan-2025

Doorley, K., O'Connor, S., O'Shea, R., and Tuda, D. 2026. Artificial Intelligence and Income Inequality in Ireland. Jointly Published Report No. 16. Dublin: Economic and Social Research Institute (ESRI). https://doi.org/10.26504/jr16

International Monetary Fund (IMF). 2024. World Economic Outlook: Steady but Slow—Resilience amid Divergence. Washington, DC, April.

Khabbazan, M. M., and C. von Hirschhausen. 2021. The Implication of the Paris Targets for the Middle East through Different Cooperation Options. Energy Economics 104: 105629.

Khabbazan, M. M. 2022. "The EU's Gain (Loss) from More Emission Trading Flexibility—A CGE Analysis with Parallel Emission Trading Systems." Journal of Open Innovation: Technology, Market, and Complexity 8 (2): 91. https://doi.org/10.3390/joitmc8020091

Khabbazan, M. M., and M. Garcia-Escribano. Forthcoming. A CGE-Based Macroeconomic Assessment of Energy Diversification in Morocco. IMF Working Paper, International Monetary Fund, Washington, DC.

Lanz, B., and T. Rutherford. 2016. GTAP In GAMS: Multiregional and Small Open Economy Models. Journal of Global Economic Analysis 1 (2): 1–77.

Okagawa, A., and K. Ban. 2008. Estimation of Substitution Elasticities for CGE Models. Discussion Paper 08-16, Research Institute of Economy, Trade and Industry (RIETI), Tokyo.

Organisation for Economic Co-operation and Development (OECD). 2025. Macroeconomic Productivity Gains from Artificial Intelligence in G7 Economies. OECD Artificial Intelligence Papers No. 41, Paris.

World Trade Organization (WTO) and International Monetary Fund (IMF). 2026. WTO–IMF Tariff Tracker. WTO Tariff & Trade Data Platform, Geneva.
"""
