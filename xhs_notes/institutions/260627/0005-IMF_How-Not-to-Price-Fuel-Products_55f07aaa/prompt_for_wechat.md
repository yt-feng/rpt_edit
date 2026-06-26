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
- 已识别机构名：`国际货币基金组织`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份国际货币基金组织研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
![](images/cb6c6ea8f223b2cb3505fada102a672f501d254f92d8462a85d3be603e5f1f8f.jpg)

HOW TO

NOTES

# How (Not) to Price Fuel Products

Delphine Prady, Julieth Pico-Mejia, Jean-François Wen, and Grégoire Rota-Graziosi

HTN/2026/03

This page intentionally left blank

HOW-TO NOTE

How (Not) to Price Fuel Products

Delphine Prady, Julieth Pico-Mejia, Jean-François Wen, and

Grégoire Rota-Graziosi © 2026 International Monetary Fund Cover Design: IMF Creative Solutions

How (Not) to Price Fuel Products
Delphine Prady, Julieth Pico-Mejia, Grégoire Rota-Graziosi, and Jean-François
HTN/2026/03

## DISCLAIMER:

How-To Notes offer practical advice from IMF staff members to policymakers on important issues. The views expressed in How-To Notes are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

## Abstract:

Half of all countries in the world regulate fuel prices through various forms of interventions in price formulas. These interventions pursue a range of social, political, and economic objectives, including protecting consumers from price volatility or promoting domestic industries. However, they rarely achieve their objectives and often have unintended and costly consequences. This How-to-Note provides guidance on the structure and components of fuel price formulas, what practices should be avoided, and why. Policymakers should prioritize transparency, alignment with international market prices, simplicity, and consistency in fuel pricing. Transparency requires regularly publishing all components of fuel prices. Second, domestic fuel prices should reflect international market fluctuations. Policymakers should create a pricing culture that accepts some degree of price volatility, possibly through automatic and transparent adjustments. Third, price interventions should be simple and kept at a minimum. This is key for fuel taxation which should be streamlined to only a few taxes, while parafiscal levies should be avoided. Finally, similar fuel products should be subject to comparable pricing interventions to ensure consistency and reduce inefficiencies, fraud, and smuggling.

## Recommended Citation:

Prady, Delphine, Julieth Pico-Mejia, Grégoire Rota-Graziosi, and Jean-François Wen. 2026. "How (Not) to Price Fuel Products." IMF How-To Note 2026/03, International Monetary Fund, Washington, DC.

ISBNs:
979-8-229-03705-1 (paper)
979-8-229-03728-0 (ePub)
979-8-229-03711-2 (web PDF)

## Contents

Introduction
Components of the Prices of Fuel Products
Different Fuel Price Interventions, Tradeoffs, and Fiscal Risks
Price Intervention at Product Availability
Price Intervention at Product Access
Price Intervention at Product Sale
The Dos and Don'ts When Setting Up Fuel Price Structures
Principle 1. Transparency
Principle 2. Anchoring Domestic Prices to International Reference Prices
Principle 3. Simplicity
Principle 4. Consistency
References
1
3
6
9
9
10
14
14
14
15
15
17

This page intentionally left blank

## Introduction

Fuel products are fundamental inputs in modern economies. $^{1}$ They account for 25 percent of global energy supply and are essential for production, transportation, trade, power generation, and the functioning of critical infrastructure. Fluctuations in their prices have significant macroeconomic implications, shaping inflation dynamics, competitiveness, and overall macroeconomic stability. They also have substantial fiscal implications through both taxation and subsidies. In 2023, the total final consumption of gasoline and diesel amounted to about 6 percent of global GDP, exceeding 10 percent in a dozen countries. Although international markets largely determine fuel prices, supply chain rigidities and distortions also play an important role, and volatility is often amplified by geopolitical events.

The pricing of fuel products should ideally rely on liberalized energy markets, supported by taxation that fully internalizes environmental, health and other negative externalities (Black and others 2023). Fuel prices that do not adequately reflect supply costs and environmental impacts generate fiscal risks and liabilities and weaken environmental policy objectives. Countries should therefore allow price signals to operate through market-based pricing and add all externalities associated with fuel use. Efficient fuel prices can then be compared with current prices to assess how much fuel consumption countries subsidize and how countries can design reform plans (see Black and others 2025). However, despite strong arguments in favor of pricing all externalities from fuel use, many countries do not even capture the supply cost of fuel and remain a long way from efficient pricing.

This note focuses on improving fuel pricing practices without attempting to incorporate all environmental externalities or quantifying fuel subsidies. Half of all countries in the world regulate fuel prices through various forms of interventions in price formulas. These regulations typically involve administratively set prices across multiple components of numerous pricing structures, resulting in significant complexity and limited transparency. Although such practices are more common in low-income developing countries, fuel price regulation remains widespread across income groups, with 95 countries maintaining some form of intervention as of January 2025. $^{2}$ For example, Belgium has regulated fuel prices using a formula-based retail price cap introduced in 1974, and in Malawi, the Energy Regulatory Authority sets retail prices through an automatic mechanism that adjusts when landed costs deviate by more than $\pm5$ percent (FPS Economy 2025; Malawi Energy Regulatory Authority 2025).

Governments intervene in fuel pricing to pursue a range of social, political, and economic objectives. These include protecting consumers from price volatility and maintaining affordability, securing fiscal revenues, ensuring reliable supply in low-income developing countries, limiting rent-seeking, and pursuing political goals such as promoting social cohesion or protecting energy-intensive industries. However, such interventions rarely achieve their objectives and tend to have unintended and costly consequences (for example, encouraging smuggling).

This note provides guidance on the structure and components of fuel price formulas, what pricing practices should be avoided, and why. The note starts by detailing the key components of a reference fuel price. This price reflects the full cost of supplying fuel in a liberalized market and includes all taxes applied in a given country. This reference price excludes discretionary policy interventions, such as noncompetitive regulation of supply costs, special tax arrangements that would deviate from standard tax regimes (for example, reduction or exemption), or discretionary caps on final prices. The note then describes the most common forms of intervention applied to each component, and the associated policy tradeoffs. It proposes a pricing framework and highlights the fiscal risks and policy challenges that arise from regulatory interventions. These tradeoffs are often opaque, can generate entrenched rents within the downstream fuel sector, and may impose significant fiscal and economic costs and unintended distributional effects.

Policymakers should prioritize transparency, alignment with international market prices, simplicity, and consistency in fuel pricing. First, transparency requires regularly publishing all components of fuel price formulas. Second, domestic fuel prices should reflect international market fluctuations. Policymakers should create a pricing culture that accepts some degree of volatility, possibly through automatic and transparent adjustments. Third, price interventions should be simple and minimal. This is particularly key for fuel taxation, which should be streamlined to only few taxes and should avoid parafiscal levies. Last, similar fuel products should be subject to comparable pricing interventions to reduce inefficiencies, fraud, and smuggling.

This note is organized as follows. First, it outlines the components of reference fuel prices. Second, it examines the fiscal, governance, and economic risks—as well as the policy tradeoffs—associated with rigid or discretionary interventions in these components. Last, the note presents key dos and don'ts for fuel price interventions, highlighting principles to reduce distortions and align existing pricing mechanisms more closely with the reference price.

# Components of the Prices of Fuel Products

The supply of fuel products involves three main components: product availability, access, and sale (see Table 1). First, fuel products must be made available in a country, whether through domestic production, importation, or a combination of both. $^{3}$ Second, access to these products must be ensured through an effective distribution system, supported by adequate storage facilities and transportation networks across the country. Third, fuel products must be sold to consumers, either directly at points of consumption—typically on a wholesale basis for businesses and large users—or through retail outlets such as gas stations for the general public.

In this note, reference fuel prices are prices that reflect the full cost of supply in a liberalized market and that incorporate all taxes applied in a given country. A liberalized market supply cost corresponds to the economic cost of delivering fuel products within a competitive environment that minimizes rent-seeking behaviors (such as those arising from information asymmetries) and inefficiencies (such as collusion among market participants) across all stages of the downstream supply chain (that is, all steps from transporting crude oil to refineries up to the point where fuels are ready for consumers). With respect to taxation, a reference fuel price should, by default, include only those taxes explicitly defined in the current legislation—such as customs duties, value-added tax (VAT), and excise taxes. $^{4}$

As fuel products are traded globally, international market prices serve as the primary benchmark for supply costs, regardless of whether a country imports or produces fuel domestically (see Table 1, component 1). For importing countries, these prices represent the main cost borne by importers, whereas for exporting countries, they reflect the opportunity cost–foregone revenue from selling the products domestically instead of abroad at international prices. These costs are further increased by the services required to make fuels available to distributors, such as freight, trading, and insurance, which vary across countries. The most common international reference is the free-on-board price, which refer to fuel prices at the point of export, excluding shipping and insurance fees. $^{5,6}$ International market prices are subject to significant market volatility, which exchange rate fluctuations may further amplify. In principle, fuel prices should reflect this volatility to convey accurate market signals to consumers, enabling them to adjust their consumption patterns accordingly. Once fuel products reach distributors, additional supply-chain costs arise to account for distribution and retail operations (see Table 1, component 2).

Table 1. Components of Reference Fuel Prices  
![](images/378a42b65f57ce255aa5e8e07958f31123f7d78801a1ea7cc62a1ba889e36704.jpg)  
Sources: Authors; Petroleum Authority of Uganda (http://www.pau.go.ug); and UFIP 2026 (for France December 2025 diesel price).  
Note: Excise taxes can be collected at customs; VAT should be collected at each stage of the supply chain, but in a regulated price context, VAT collection is usually done only once at the distribution entry point of the supply chain (for example, at the border or at the refinery's exit) and not at later stages of the supply chain. TICPE refers to the excise tax on domestic consumption of petroleum products, and UGX refers to Ugandan shilling. VAT = value-added tax.  
For fuel producers, transportation costs and margins borne to ensure products' availability to downstream marketers are usually expressed in local currency and do not need to be converted with the exchange rate.  
2 For fuel producers, custom duties can be broken down in two parts: first, custom duties on imported oil products (for example, crude oil) where applicable, and second, local producers' costs (including refining costs) and margins.

The taxation of fuel products typically consists of customs duties, VAT, and excise taxes (see Table 1, components 3, 7, and 8). Differences in tax burdens across fuel types such as gasoline, diesel, or kerosene tend to lack a clear economic rationale—such as the internalization of different environmental impact—and are often justified by nontransparent policy considerations (for example, the “diesel differential” in Europe; Harding 2014). These can result from lobbying (by industrial or specific political interests) or inertia from past policies not explicitly related to economic efficiency goals. The standard VAT base for fuel products is the pre-VAT consumer price, which includes supply costs and all other applicable taxes. Excise taxes are usually limited in number to avoid overly complex price structures and to reduce opportunities for rent-seeking by specialized agencies or administrations. They may also incorporate behavioral incentives to encourage particular consumption patterns, such as energy conservation or the use of specific fuels. $^{7}$

Reference fuel prices include VAT—applied inclusive of excise taxes—in countries where VAT or an equivalent tax is levied (see Table 1, component 8). VAT is typically collected through the credit-invoice method, whereby suppliers levy VAT on their taxable sales and issue invoices that allow purchasers to claim input tax credits. Consequently, the VAT burden falls solely on final consumers, but businesses along the supply chain remit only the net VAT, calculated as the difference between VAT collected on sales and VAT paid on inputs. In regulated price environments, VAT on the final fuel consumption is often collected only once, either at the border or at the point of exit from domestic refineries or storage facilities. This approach is generally adopted for administrative efficiency, as collecting VAT from a limited number of importers or producers is simpler, ensures higher compliance, and minimizes enforcement costs compared to collecting it throughout the supply chain and from numerous retailers.

Given the relatively low-price elasticity of demand for fuel products, applying uniform taxation without preferential treatments is an effective means of generating revenue. $^{8}$ This is the case even in contexts characterized by high levels of informality. In most countries, fuel consumption is relatively inelastic and, in many developing economies, constitutes one of the few formal and stable tax bases available to fiscally constrained governments. With worldwide fuel consumption averaging about 6 percent of GDP in 2023, fuel products represent a significant and reliable source of tax revenue in these countries.

When fuel prices are fully liberalized, consumer prices are the sum of the three components of the reference prices and therefore fluctuate in line with international market conditions. However, when policymakers intervene at any stage of the supply chain and introduce price controls or other regulatory measures, consumer prices may diverge from the reference price. The following section outlines these types of interventions and examines the associated fiscal implications.

# Different Fuel Price Interventions, Tradeoffs, and Fiscal Risks

In practice, deviations from reference prices occur widely across countries, regardless of their level of development. Governments often justify intervening in fuel pricing to (1) shield consumers from volatility shocks by preserving affordability of fuel products; (2) preserve revenue targets; (3) in low-income developing countries, ensure supply while limiting rent-seeking from fuel market players; and (4) pursue broader social, economic, or political objectives—such as maintaining social cohesion, supporting income redistribution, or advancing industrial policy goals. Although fuel price liberalization remains the long-term objective in many countries, interim price controls—when supported by sound regulation and effective enforcement—serve as milestones toward this goal (Kojima 2016). Effective enforcement may involve transparent and evidence-based monitoring systems, penalties for noncompliance, and regular audits to ensure that regulated prices are being implemented as intended. Setting regulated prices as close as possible to reference prices and doing so in a manner that minimizes economic distortions, facilitates progress toward achieving full liberalization over time.

Fuel price interventions generally result in lower prices for final consumers and, consequently, imply some form of fiscal costs. Between 2015 and 2024, average consumer prices for diesel, high-octane gasoline, and kerosene were approximately 32, 26, and 21 percent lower, respectively, in countries with regulated fuel prices compared with those with liberalized pricing regimes (see Figure 1, panel 1). The gap between regulated and liberalized prices is substantially larger in high-income countries than in low-income and lower-middle-income countries (see Figure 1, panel 2, diesel consumer prices). This wider differential partly reflects higher fuel taxation in high-income countries with liberalized prices, as well as higher, largely unavoidable supply costs in many low-income countries, regardless of whether prices are regulated. $^{9}$ This effectively reduces potential tax revenues from a significant and predominantly formal consumption base in countries with regulated prices. At the same time, the share of advanced economies that regulate fuel prices is considerably smaller than that of low- and middle-income countries.

Figure 1. Differences between Liberalized and Regulated Fuel Consumer Prices (US dollars per liter, by fuel type and country income group)

1. Yearly Averages of Liberalized and Regulated Consumer Prices, by Fuel Type

![](images/2af29d8f3a492716018a5a369dd7c99a30ca19c7bbc482a3e6a8f59a9fc7d320.jpg)  
2. Yearly Averages of Liberalized and Regulated Diesel Consumer Prices, by Country Income Group

![](images/6d04749a1f95a50186db9d61111c738907f18cfafb77e9ce52d05fef8d136065.jpg)  
Sources: Authors; and World Bank Global Fuel Subsidies and Price Control Measures Database 2025.  
Note: Prices are 

[中间内容因长度限制已省略]

ustments.·Do not disconnect domestic prices from global supply conditions.·Do not implement pricing mechanisms while prices remain misaligned with international levels.·Do not shield consumers from all volatility in ways that endanger fiscal sustainability.</td></tr><tr><td>Simplicity</td><td>·Keep interventions few and simple to enhance clarity and reduce administrative burden.·Ensure interventions reflect actual market or governance needs.·Streamline taxation and ensure taxes are legally grounded and easy to administer.·Use explicit, standalone subsidies applied to the final consumer price and reflected in the budget.</td><td>·Do not multiply differentiated interventions (for example, by region, importer, or route).·Do not introduce benefits for actors loosely connected to the fuel sector.·Do not impose parafiscal levies or off-budget charges.·Do not embed subsidies within intermediate cost components.</td></tr><tr><td>Consistency</td><td>·Apply similar interventions to similar fuel products to ensure coherence.·Ensure pricing differences between fuels or users are economically justified.·Monitor cross-border price differentials to mitigate smuggling incentives.·Consider socioeconomic impacts when reforming price interventions, especially in regulated downstream sectors.</td><td>·Do not maintain unjustified price discrepancies between comparable fuels or across users.·Do not ignore regional price disparities that encourage smuggling.·Do not implement adjustments without considering effects on regulated sectors or households.·Do not reform price structures in isolation from broader economic conditions.</td></tr></table>

Source: Authors.

## References

Abdallah, Chadi, David Coady, and Nghia-Piotr Le. 2020. "The Time Is Right! Reforming Fuel Product Pricing Under Low Oil Prices." IMF Special Series on COVID-19, Washington, DC.

Black, Simon, Antung A. Liu, Ian Parry, and Nate Vernon. 2023. "IMF Fossil Fuel Subsidies Data: 2023 Update." IMF Working Paper 23/169, Washington, DC.

Black, Simon, Weronika Celniak, Alberto Garcia-Huitron, Ian W. H. Parry, Paulina Schulz-Antipa, and Nate Vernon-Lin. 2025. "Underpriced, Overused, and Fueling Inequality: Fossil Fuel Subsidies Data 2025 Update." IMF Working Paper 25/270, Washington, DC.

Coady, David, Javier Arze del Granado, Luc Eyraud, and Anita Tuladhar. 2013. "Automatic Fuel Pricing Mechanisms with Price Smoothing: Design, Implementation, and Fiscal Implications." IMF Technical Notes and Manual 2012/003, Washington, DC.

Coady, David, Ian Parry, and Baoping Shang. 2017. "Energy Price Reform: A Guide for Policymakers." CESifo Working Paper 6342, CESifo Group, Munich, Germany.

Chetty, Raj, Adam Looney, and Kory Kroft. 2009. "Salience and Taxation: Theory and Evidence." American Economic Review 99 (4): 1145-77.

De Broeck, Mark, and Roland Kpodar. 2014. "Mali: Technical Assistance Report—Automatic Fuel Pricing Mechanism." IMF Country Report 14/31, Washington, DC.

FPS Economy. 2025. "Maximum Prices of Petroleum Products." Federal Public Service, Belgium. https://economie.fgov.be/nl/themas/energie/energieprijzen/maximumprijzen#The%20pricing%20structure

Goldin, Jacob. 2022. "Optimal Tax Salience." Quarterly Journal of Economics 137 (4): 2463-511.

Harding, Michelle. 2014. "The Diesel Differential: Differences in the Tax Treatment of Gasoline and Diesel for Road Use." OECD Taxation Working Papers No. 21. Organisation for Economic Co-operation and Development, Paris, France.

International Monetary Fund (IMF). 1996. "Quasi-Fiscal Operations of Public Financial Institutions." IMF Occasional Paper 142, Washington, DC.

International Monetary Fund (IMF). 2014. "Government Finance Statistics Manual." IMF, Washington, DC. https://www.imf.org/en/Publications/CR/Issues/2016/12/31/Mali-Technical-Assistance-Report-Automatic-Fuel-Pricing-Mechanism-41303.

International Monetary Fund (IMF). 2020. "Draft Guidance Note - C.11 Valuation of Imports and Exports of Goods in the International Standards (CIF to FOB Adjustment)." Thirty-Fourth Meeting of the IMF Committee on Balance of Payments Statistics, BOPCOM-20/06. https://www.imf.org/external/pubs/ft/bop/2020/pdf/20-06.pdf

International Monetary Fund (IMF). 2025. "Public Sentiment Matters: The Essence of Successful Energy Subsidies and Pension Reforms" (Chapter 2). In Fiscal Monitor: Fiscal Policy under Uncertainty. Washington, DC, April.

Kilian, Lutz, and Xiaoqing Zhou. 2024. "Heterogeneity in the Pass-Through from Oil to Gasoline Prices: A New Instrument for Estimating the Price Elasticity of Gasoline Demand." Journal of Public Economics 232: 105099.

Kojima, Masami. 2016. "Fossil Fuel Subsidy and Pricing Policies: Recent Developing Country Experience." World Bank Policy Research Working Paper 7531, World Bank, Washington, DC.

Kpodar, Kangni R., and Patrick A. Imam. 2021. "To Pass (or Not to Pass) through International Fuel Price Changes to Domestic Fuel Prices in Developing Countries: What Are the Drivers?" Energy Policy 149: 111999.

Labandeira, Xavier, Jose Maria Labeaga, and Xiral López-Otero. 2017. "A Meta-Analysis on the Price Elasticity of Energy Demand." Energy Policy 102: 549-68.

Malawi Energy Regulatory Authority. 2025. "Review of Prices of Petrol and Diesel." Malawi Energy Regulatory Authority. https://mera.mw/2025/10/01/review-of-prices-of-petrol-and-diesel/

UFIP. 2026. "Décomposition des prix des carburants." https://www.energiesetmobilites.fr/presse/informations/decomposition-des-prix-des-carburants

World Bank. 2025. Global Landscape of Fuel Subsidies and Price Controls. Washington, DC: World Bank.

This page intentionally left blank

![](images/289b532a2092f724d12b702ea6877dc2fe22f3e673e88dd37e7cdf19f2c39ef7.jpg)
"""
