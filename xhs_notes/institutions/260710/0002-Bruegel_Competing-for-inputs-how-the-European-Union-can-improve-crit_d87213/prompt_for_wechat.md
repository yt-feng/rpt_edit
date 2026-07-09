你是麦肯锡/研究导读风格的微信公众号文章主笔，擅长用金字塔原理把报告内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给专业读者/产业决策者的报告导读。
- 长度：约 1200 字，整体以短导读为主，通常控制在 900-1200 个中文字符。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，只讲最关键的判断、图表和未解问题，让读者有动力去看原文。
- 文章必须像人工编辑润色过的报告导读：句长有变化，段落有呼吸感，不要整齐排比，不要反复使用“这意味着/真正重要的是/换句话说/从这个角度看”等模板转折。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、市场定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须短、锐利、可转发，优先 20-35 个中文字符，最长不超过 35 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 要兼顾微信搜一搜：尽量包含一个高意图关键词，例如行业/公司/政策/AI/房地产/半导体/光伏/消费/美联储/利率/通胀/机器人/比特币等。
- `# 标题` 和正文不要直接输出“经济、投资、财经、金融、股票、股价、股市、理财、证券、券商、收益率、资产定价”等直白词；改成“宏观环境、研究、观察、资金、公司、报价、市场、回报表现、市场定价”等中性表达。
- 涉及中国、国内、内地、大陆、人民币、A股、港股时，必须使用中性客观表达；不要写“不好、不行、疲弱、低迷、恶化、危机、衰退、崩盘、放缓、压力、拖累、唱衰”等负面判断。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`布鲁盖尔研究所`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
- 标题禁止出现 GS、JPM、JEF、NOM、BARC、MS、DB、Citi、Ticker、文件编号；如果原文只有英文机构名，请翻译为中文机构名。
- 标题冒号后不要重复机构或来源类型，禁止“联合国贸发会议：联合国贸发报告，……”“麦肯锡：麦肯锡报告称，……”这类写法；冒号后直接写判断或变量。
- 标题只能保留一层信息，不要把多个长分句全部塞进标题；如果原始标题有三段以上信息，只取最有传播性的主判断，其余放在正文第一段自然展开。
- 如果报告是单一公司/个股报告，标题和正文只能写公司情况、行业变化、业务进展、竞争格局和报告里的事实；禁止出现目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO 等任何卖方操作口径。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 观察提示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，20-35 个中文字符。
2. 开头 2-3 段：直接给出主判断、为什么现在重要、报告提供了什么新信号；自然带出 4-6 个长尾关键词，覆盖国家/行业/公司/政策/数据/技术词，但不要写成关键词堆砌。
3. 3-4 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 1-2 个 `> **KC评论：** ...` 引用块，每个 1-2 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，不要夹带任何推广话术。
5. 正文中间禁止插入 CTA、广告、扫码、社群、知识星球、每日汇编、喂给 AI 等表达；中间只允许出现分析正文、图表占位和 `KC评论`。
6. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
7. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
8. 不要写任何 CTA、广告、扫码、社群、知识星球、网站、域名或关注引导；系统会在最结尾统一插入固定信息。
9. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
10. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.</p>`

【CTA 要求】
- 不要输出任何 CTA。不要写“加入社群”“扫码”“星球”“完整报告领取”“网站”“域名”“关注”“星标”“更多查看”等表达。
- 文末也不要写 CTA；系统会在最结尾统一插入固定信息。
- 正文中间不要出现“如果你从某些关键词搜到这里”“单篇文章只能解决一个切片”“我每天会把……”“这篇可以沿着……”这类表达。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。
- `KC评论` 里禁止夹带 CTA，不要写扫码、社群、知识星球、每日汇编、喂给 AI、市场主线、完整报告领取等表达；它只能做解释、提醒或追问。

【人工编辑感要求】
- 段落不要像 AI 摘要清单。每段只推进一个意思，必要时用短句收住。
- 不要展开成完整长文。每个小节只保留最有信息量的一段，细节留给原文和图表。
- 避免连续使用同一种句式开头，避免连续三段都是“报告指出/这意味着/真正重要的是”。
- 不要机械重复标题、机构名或同一句判断。标题已经写过的内容，正文第一段要换一种说法展开。
- 保留一点自然语气，但不要口水化；像一个认真读过报告的人在做导读。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 单公司报告不能写成交易提示；不要输出目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO，也不要保留这些英文/中文卖方评级词。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份布鲁盖尔研究所研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Competing for inputs: how the European Union can improve critical raw materials supply security

Madalena Barata da Rocha and Camille Reverdy

Madalena Barata da Rocha (madalena.barata-rocha@bruegel.org) is a Research Analyst at Bruegel

Camille Reverdy (camille.reverdy@bruegel.org) is an Affiliate Fellow at Bruegel

The authors thank Ben McWilliams, Ignacio Garcia Bercero, Flora Marchioro and participants to the Bruegel research seminar for their useful comments. We are grateful to Niclas Poitiers for his insightful suggestions and to Benjamin Bjerkan-Wade for the subsidies analysis.

## Executive summary

CRITICAL RAW MATERIALS (CRMs) are essential to the European Union's green and digital transition, underpinning technologies from batteries to semiconductors. Demand is expected to increase hugely by 2050, yet CRM supply chains remain highly concentrated and exposed to geopolitical and market risks. The EU also faces growing competition from Japan and the United States, both of which are actively securing CRM supply through third-country partnerships and domestic investment.

WE ANALYSE THE INTERNAL AND EXTERNAL ASPECTS of the EU strategy on CRMs, drawing on data on the 60 CRM strategic projects, EU CRM strategic partnerships with third countries and trade agreements with CRM provisions. We find that strategic projects are unlikely to meet EU self-sufficiency targets and strategic partnerships have not yet produced measurable trade effects. So far, provisions in trade agreements have been the EU's most effective external instrument, leading to significant increases in CRM exports to the EU.

THE EU SHOULD BETTER ALIGN CRM investments with supply risks, strengthen CRM governance through strategic partnerships and trade frameworks and ensuring support for CRM projects. It should engage cautiously with price-floor proposals led by the United States, favouring instead bilateral off-take agreements and plurilateral cooperation involving developing supplier countries, with the goal of serving broad supply-security objectives.

## 1 Introduction

As essential inputs for technologies including batteries, wind turbines, solar panels and semiconductors, critical raw materials (CRMs) are a strategic priority in European Union trade and industrial policy. Rising demand for these materials, including substances such as cobalt, copper and lithium, is driven by the need to meet climate targets and rapid technological change. But rising global demand has also highlighted significant vulnerabilities in European supply chains, especially following the surge in commodity prices in the 2000s.

Securing access to CRM supply chains has thus become an increasingly pressing priority for the EU. The EU has sought to increase domestic supply of CRMs and to improve resource efficiency, including through substitution and recycling (Szczepanski, 2021). Since 2011, the European Commission has published five CRM lists and has mapped dependencies on third countries (Figure 1). Since 2021, it has also established strategic partnerships with third countries covering CRMs.

The EU is particularly dependent on China, and especially Chinese refining and processing, for a range of CRMs. However, China has shown it is prepared to weaponise supply chains, by imposing export controls, notably through restrictions on rare-earth element exports in 2009 and 2012, and controls on critical minerals and related products since 2023 and 2025 (Teer, 2026; Gormley et al, 2026). This shows the risks associated with concentrated external dependency in critical supply chains. Other major economies, including the United States, Japan and Canada, are also competing aggressively for CRMs while seeking to diversify away from China.

![](images/e3c75dee635f603b326944c0720e418f7800d37b0ab2ecab20e04a7379d35bea.jpg)

Source: Bruegel based on CEPII BACI and EU CRMA official list. Note: bar width is proportional to extra-EU import values. Tables A1 and A2 in the appendix list countries included in the 'FTA with CRM provisions countries' group and the 'CRM Partnership' group respectively. Canada and Chile both have an FTA with CRM provisions and a CRM partnership with the EU; to avoid double counting, these countries are only included in the former group.

As part of the response to these challenges, the EU adopted in 2024 the Critical Raw Materials Act (CRMA, Regulation (EU) 2024/1252). Among other things, this sets the framework for pursuing strategic CRM projects both outside and within the EU, meaning upstream raw materials and downstream clean-tech capacity are governed according to the same logic of supply security and resilience. EU external policies, including strategic partnerships and free trade agreements (FTAs) with resource-rich countries (see the appendix for lists), complement the CRMA.

The EU approach has faced harsh criticism (Blot, 2024; Küblböck et al, 2025; Tröster et al, 2024). The European Court of Auditors (ECA, 2026) described the CRM framework as "not a rock-solid policy". Hool et al (2024) emphasised the practical and political constraints associated with expanding domestic extraction and requirements for diversification and reduced dependencies on single third-country suppliers, including local opposition and the risk of exacerbating trade tension. Le Mouel and Poitiers (2023) argued that domestic efforts alone are insufficient to solve the EU's supply vulnerabilities. Rietveld et al (2022) stressed the need for risk-management tools, such as strategic stockpiling and more public-private coordination to make supply chains more resilient. However, such contributions are largely descriptive and provide limited empirical evidence on the effectiveness of specific policy instruments.

Alongside the EU-level policy, several EU countries have national CRM initiatives, leading to significant overlap in partner countries, duplication of efforts, intra-European competition and reduced bargaining power with third countries.

Against this background, this policy brief answers two main questions: how successful is the EU CRM strategy, and how can it be improved? We first highlight the main challenges for EU CRM policy and evaluate both the policy's internal and external dimensions. We then compare the EU approach to the Japanese and US approaches, before setting out policy recommendations.

## 2 The main challenges for EU CRM policy

## 2.1 Fast growing demand

The global demand for critical raw materials is projected to increase substantially, driven in part by the deployment of clean energy technologies. The International Energy Agency (IEA) has illustrated the magnitude of the future demand pressures on CRMs in three scenarios that relate to future demand for clean-energy technologies depending on changes in climate policy: a current policy settings scenario (STEPS; Figure 2), an announced emissions-reduction pledges scenario (APS) that assumes governments deliver on all commitments, and the net-zero emissions (NZE) by 2050 scenario.

The top panels of Figure 2 show projected global demand growth for six critical raw materials relative to their 2024 levels in each of these scenarios $^{1}$ . Lithium stands out with projected demand growth by 2050 ranging from 470 percent to 800 percent. Demand for graphite and nickel would also grow substantially, though with variation across the different scenarios, with projected demand growth by 2050 ranging from 130 percent to 250 percent. The bottom panels of Figure 2 show how, over the same period, the yearly share of total demand accounted for by clean technologies is projected to grow, rising from, on average, 20 percent to 60 percent in 2024 to 35 percent to 93 percent by 2050, depending on the mineral and scenario. This highlights the need to secure the supply chains for these minerals. Table 1 sets out the main characteristics of the CRMs in Figure 2.

## 2.2 Highly concentrated supply

A small number of countries dominate CRM extraction and processing, creating significant supply chain risks (Figure 3). Some EU countries play comparatively larger roles in the export of processed and recycled CRMs. The Democratic Republic of the Congo (DRC), Chile, Australia and Indonesia dominate the export of raw and processed cobalt, copper, lithium and nickel, respectively, whereas China accounts for large shares of the extraction and processing of graphite, cobalt and rare earth elements $^{2}$ .

Figure 4 shows the main extra-EU sources from which EU imports CRMs. The EU imports relatively little of unprocessed cobalt because most cobalt is processed before it reaches the EU. The EU relies heavily on China for processed cobalt and for extracted and processed graphite, lithium and rare earth elements. The EU imports copper is significant quantities; unprocessed copper is mostly imported from Brazil, Peru and Chile, while the main sources of processed copper are Chile, DRC and Türkiye. Russia is still the largest source of EU raw nickel as the EU has not at time of writing implemented a full import ban on Russian-origin nickel (Caprile and Cirlig, 2025). Notably, intra-EU trade also accounts for a significant share of EU CRM imports, especially of recycled CRMs.

## Figure 2: CRM demand projections in three IEA scenarios

Stated policies (STEPS) -- Net Zero emissions (NZE)
Announced pledges (APS) □ STEPS–NZE range

a) Growth of worldwide CRM demand relative

![](images/4f8fe8c3c2e68dc85d00dd0ba72f95f8ccc4d596f3bc75012f84e4119a242601.jpg)  
Source: Bruegel based on IEA (2025). Note: see section 2.1 for a description of the IEA scenarios.

Concentration increases the vulnerability of supply chains to disruption in a limited number of suppliers. However, not all CRMs have the same economic or strategic importance. The quantities and values imported by the EU vary widely (Figure 1). For instance, in 2024, EU imports from outside the EU amounted to €24 billion for copper, €7 billion for nickel and €1 billion for lithium, with supplies destined for a wide range of industrial applications (Table 1). In contrast, the EU imported only about €0.1 billion euros worth of rare earths and germanium. These elements are nevertheless crucial for the manufacturing of electrical and electronic components and magnetic materials used in, for example, clean technologies, semiconductors and optic fibre. For rare earths and germanium, among others, the EU depends on China, which is the dominant and near-monopolistic supplier (Figure 1).

Table 1: Selected CRMs: market size, main uses, supply risks and substitutability

<table><tr><td>Material</td><td>Main uses (%)</td><td>Supply risks</td><td>Can it be replaced?</td></tr><tr><td>Lithium</td><td>Batteries (87%); ceramics and glass (5%); lubricating greases (2%)</td><td>Australia, Chile and China account for 80% of mining; China refines 70% of the world&#x27;s supply; prices spiked in early 2026 after two years of oversupply</td><td>Hard to replace in batteries. Sodium-ion batteries are a cheaper emerging alternative for short-range and stationary storage; no commercial substitute for high-performance EV batteries</td></tr><tr><td>Copper</td><td>Buildings and construction (26%); equipment manufacturing (23%); infrastructure (17%); transport (13%); industrial (12%)</td><td>China represents more than 45% of global processing; average time to open a new mine almost 18 years for mines started in 2020–23</td><td>Hard to replace. Aluminium is an alternative in some applications, but no scalable alternative for power grids or EVs</td></tr><tr><td>Graphite</td><td>Batteries and electrodes for steelmaking, other steelmaking processes</td><td>China processes more than 90% of the graphite used in battery anodes; China has required export licences since 2024</td><td>Hard to replace. Can be lab-made but lab-made graphite uses five times more energy than natural; silicon-based alternatives are improving but cannot fully replace graphite</td></tr><tr><td>Cobalt</td><td>EV batteries (43%); portable device batteries (30%); high-performance metal alloys (12%); chemical catalysts (3%); ceramics and colours (3%)</td><td>DRC supplies more than 75% of mined cobalt; small-scale informal mining (15%–30% of supply) raises ethical and environmental issues; China refines more than 75% of the world&#x27;s cobalt</td><td>Currently easy to replace. LFP batteries (now over half the electric-vehicle market) use no cobalt</td></tr><tr><td>Nickel</td><td>Stainless steel (66%); EV batteries (14%); high-performance alloys and metal coatings (14%)</td><td>The high-purity grade needed for batteries is scarce, though lower-grade nickel is abundant; Western mines are closing; Indonesia, the main producer, is imposing stricter control on its mining sector</td><td>Partly replaceable. LFP batteries are pushing nickel out of mass-market EVs, but nickel-rich batteries are still preferred for long-range models; nickel is not yet replaceable in stainless steel</td></tr><tr><td>Rare earth elements (REE)</td><td>Permanent magnets over 50% (EVs, wind turbines, robots); other industrial equipment (25%)</td><td>China controls 60% of global REE production and 90% of refining; export licences imposed in April 2025</td><td>Almost impossible to replace. The REE group comprises 17 substances; no workable substitute for rare earths in high-performance magnets</td></tr></table>

Sources: Bruegel. Note: DRC = Democratic Republic of the Congo; LFP = lithium iron phosphate.

However, Chinese dominance in the mining and processing of CRMs does not automatically translate into high EU import dependency (Figure 4). For some CRMs including copper and nickel, China controls a large share of global production and refining capacity (Teer, 2026), yet the EU's actual import exposure to materials from China remains rather limited. This is partly explained by EU efforts to diversify supply, and by China using part of its production for later stages of the value chain (Gormley et al, 2026). However, even where direct EU dependence on Chinese processed CRMs appears limited, China may still have a hold over downstream chokepoints in intermediate products, such as magnets, highlighting the need for the EU to diversify its supply chains for all stages of processing.

Recycling

Figure 3: Main exporters of CRMs by production stage, 2024  
![](images/cfaf4582f2462d6cc051754d5093171fae0421271e909a25a0e784cbcc2b2b45.jpg)

![](images/9d50555b00be7e0df84fdbd351ae0603f89724b856baa339187d91cebe6ec80e.jpg)

![](images/b2e4777908a23b4bd1782829a1b8074c62107e1fcd3b95c421c53a9c4672aafa.jpg)

Source: Bruegel based on CEPII BACI and Georgitzikis et al (2023). Note: the size of the bubbles is proportional to the total export value of the mineral in 2024. The EU rare earths export share in the recycling stage cannot be estimated as no product code is assigned to exports of recycled REE. Intra-EU trade is removed from the calculations. While some nickel intermediates might contain some cobalt and copper components, we only include it in the nickel category.

Figure 4: Value of EU CRM imports from extra-EU suppliers, 2024  
![](images/03c5dafb6ed73f147ecacb7fa2a888ee5cd3b15e418c6f8cdb7cab87c27cc539.jpg)

![](images/4ba700923e83af0a5dcd669dd436fa3d70f4871ad411384aa48329c948cb3302.jpg)

![](images/f2dd62eb7d1989eea4dfe18fd4838c67de93129944ff2eabe2cc936def0ff0ac.jpg)

Source: Bruegel based on CEPII BACI and Georgitzikis et al (2023). Note: intra-EU trade is removed from the calculation. See note to Figure 3. While under sanctions on Russia issued on of 23 April 2026, the EU banned the importation of Russian-origin cobalt, it has not implemented a full import ban on Russian-origin nickel. See Reuters, 'LME issues notice on warranting of Russian-origin copper, cobalt in EU', 17 June 2026, https://www.reuters.com/business/lme-issues-notice-warranting-russian-origin-copper-cobalt-eu-2026-06-17/.

Figure 5: EU shares of CRM exports by CRM and production stage, 2024  
![](images/8b6c68a0299eeaed3fc5f5fe54088662e52055765843a16b1fa9a19a5ec306dc.jpg)  
Source: Bruegel based on CEPII BACI and Georgitzikis et al (2023). Note: the shares exclude intra-EU trade.

The EU's own extraction and processing capacity remains limited. The EU share of global extraction is negligible for most CRMs, lower than 10 percent, while its processing shares range from 9.5 percent for lithium to 49.4 percent for graphite. However, the EU has a large share of global exports of recycled CRMs (Figure 5) $^{3}$ .

## 2.3 Market failures

Three types of market failure are particularly relevant in CRM markets: moral hazard, competitive pressures and collective action. Moral hazard arises when firms underinvest in supply-chain diversification because they expect government intervention during shortages, meaning in the CRM context that firms are unwilling to pay for sourcing other than from China.

Competitive pressures make sourcing from more expensive suppliers a disadvantage for European manufacturers, particularly in sectors in which CRMs make up a significant share of the final product cost $^{4}$ . Finally, collective-action problems arise because most industrial firms purchase only small quantities of specialised materials. Even when a firm is willing to invest in diversification, its limited demand is often insufficient to justify the development of new mining or processing facilities. In such cases, government coordination, through demand aggregation or direct support, can help overcome constraints.

# 3 Does the EU have a sufficient CRM strategy?

## 3.1 Current EU policies

The CRMA sets four benchmarks for 2030 covering all CRMs:

1. A minimum of 10 percent of annual CRM consumption should be sourced from domestic extraction;

2. Domestically processed CRMs should meet 40 percent of domestic consumption;

3. Recycling should meet 25 percent of domestic consumption;

4. No more than 65 percent of supply of a CRM at any relevant stage of processing should be sourced from a single third country.

This approach has been reinforced by several measures to expand primary and secondary CRM production, notably through a €3 billion 'financing hub' supporting CRMA strategic projects $^{5}$ , a proposed Critical Raw Materials Centre, a Raw Materials Mechanism to coordinate demand and investment and a pilot scheme for stockpiling. In addition, a critical raw materials Important Project of Common European Interest (IPCEI) – a joint project backed by EU member state funding – is underway with 13 EU involved, at time of writing $^{6}$ .

EU financing for CRM-related projects has relied on many existing instruments and has involved relatively low amounts (ECA, 2026). To complement EU fun

[中间内容因长度限制已省略]

>State Aid (EUR M)</td><td>Total (EUR M)</td><td>SA Country</td></tr><tr><td>Elemental Battery Metals</td><td>POLVOLT</td><td>PL</td><td>Ni, Cu, Co, Li, PGM, Mn</td><td>78.7</td><td>5.7</td><td>244.1</td><td>328.4</td><td>PL</td></tr><tr><td>Northvolt Revolt</td><td>NorthCYCLE</td><td>SE</td><td>Mn, Li, Gr, Ni, Co</td><td>232.7</td><td>52.7</td><td>0.6</td><td>285.9</td><td>DE</td></tr><tr><td>Sibanye-Stillwater</td><td>GALLICAM</td><td>FR</td><td>Ni, Co, Li, Gr, Mn, Cu</td><td>143.3</td><td>—</td><td>—</td><td>143.3</td><td>—</td></tr><tr><td>Talga AB</td><td>Talga Natural Graphite ONE</td><td>SE</td><td>Graphite</td><td>69.1</td><td>22.5</td><td>1.1</td><td>92.7</td><td>UK</td></tr><tr><td>Caremag</td><td>CAREMAG</td><td>FR</td><td>REE for magnets, boron</td><td>—</td><td>—</td><td>58.5</td><td>58.5</td><td>FR</td></tr><tr><td>Cobre Las Cruces</td><td>Polymetallic sulphide</td><td>ES</td><td>Copper</td><td>2.5</td><td>—</td><td>42.6</td><td>45.2</td><td>ES</td></tr><tr><td>Mag Resource</td><td>MagFactory</td><td>FR</td><td>REE for magnets</td><td>3.8</td><td>—</td><td>38.5</td><td>42.3</td><td>FR</td></tr><tr><td>Vulcan Energie</td><td>Zero Carbon Lithium</td><td>DE</td><td>Lithium</td><td>—</td><td>37.5</td><td>2.7</td><td>40.2</td><td>DE</td></tr><tr><td>Metlen Energy &amp; Metals</td><td>Metlen CRM Investments</td><td>GR</td><td>Al, Bauxite, Ga</td><td>—</td><td>13.5</td><td>—</td><td>13.5</td><td>—</td></tr><tr><td>Lithium Iberia</td><td>Las Navas</td><td>ES</td><td>Lithium</td><td>—</td><td>—</td><td>32.5</td><td>32.5</td><td>ES</td></tr><tr><td>Geomet</td><td>Cinovec lithium</td><td>CZ</td><td>Lithium</td><td>32.4</td><td>—</td><td>—</td><td>32.4</td><td>—</td></tr><tr><td>Eramet</td><td>Ageli</td><td>FR</td><td>Lithium</td><td>—</td><td>30.0</td><td>0.6</td><td>30.6</td><td>FR</td></tr><tr><td>Kelib Technology</td><td>KELIBER LITHIUM</td><td>FI</td><td>Lithium</td><td>0.1</td><td>25.1</td><td>1.6</td><td>26.8</td><td>FI</td></tr><tr><td>Tokai Cobex Savoie</td><td>BAM4EVER</td><td>FR</td><td>Graphite</td><td>—</td><td>—</td><td>20.3</td><td>20.3</td><td>FR</td></tr><tr><td>Iberian Resources</td><td>P6 Metals</td><td>ES</td><td>Tungsten</td><td>13.3</td><td>—</td><td>5.3</td><td>18.6</td><td>ES</td></tr><tr><td>Up Catalyst</td><td>CO2 Graphite</td><td>EE</td><td>Graphite</td><td>—</td><td>2.7</td><td>4.4</td><td>7.1</td><td>EE</td></tr><tr><td>Euro Manganese</td><td>Chvaletice Manganese Project</td><td>CZ</td><td>Manganese</td><td>—</td><td>5.9</td><td>—</td><td>5.9</td><td>—</td></tr><tr><td>Rock Tech Guben</td><td>Li Hydroxide Converter</td><td>DE</td><td>Lithium</td><td>—</td><td>22.5</td><td>5.2</td><td>27.7</td><td>DE</td></tr><tr><td>Hycamite TCD</td><td>Hycamite TCD</td><td>FI</td><td>Graphite</td><td>0.2</td><td>—</td><td>2.0</td><td>2.2</td><td>FI</td></tr><tr><td>PCC Thorion</td><td>ProHiPerSi</td><td>DE</td><td>Graphite</td><td>—</td><td>—</td><td>0.5</td><td>0.5</td><td>DE</td></tr><tr><td>Jervois Finland</td><td>Cobalt Refinery Expansion</td><td>FI</td><td>Cobalt</td><td>—</td><td>—</td><td>0.4</td><td>0.4</td><td>FI</td></tr><tr><td>Total (21 projects)</td><td></td><td>576.0</td><td>218.1</td><td>460.9</td><td>1,254.9</td><td></td><td></td><td></td></tr></table>

Source: Bruegel. Note: 'Proj. Loc.' is the country in which the strategic project is located while 'SA Country' is the EU country allocating state aid to the project. EU Funds encompass all expenditures under direct EU budget management, EU Cohesion Policy project records, Innovation Fund and CINEA programme grants, and Horizon Europe/Horizon 2020 research participation while IFIs comprise EIB and EBRD loans, equity and guarantees. To ensure comparability amounts are converted to gross grant-equivalent (GGE) amounts using rates fixed per instrument class: grants and subsidies = 100%, repayable advances = 90%, equity = 50%, loans = 15%, guarantees = 10%, tax advantages = 15%, following the European Commission State Aid Scoreboard methodology.

Table A4: CRM policies of EU countries

<table><tr><td>Member State(s)</td><td>Strategic approach</td><td>Key instruments</td><td>International partnerships</td></tr><tr><td>France</td><td>State-led; strategic industrial autonomy</td><td>Domestic CRM projects and industrial capacity development</td><td>Japan (2024, 2026), Australia (2022), Canada (2023), Morocco (2023), Chile (2024)</td></tr><tr><td>Nordic countries (Sweden, Finland)</td><td>Resource endowment-led; domestic focus</td><td>Extraction and refining within the EU</td><td>—</td></tr><tr><td>Germany</td><td>Industry-driven; import diversification</td><td>Long-term contracts, equity investments, offtake agreements, joint ventures; public financial institution guarantees and co-financing; National Raw Materials Strategy</td><td>Chile (2013), Kazakhstan (2012), Mongolia (2011, renewed 2024), Peru (2014)</td></tr></table>

Source: Bruegel.

## Republishing and referencing policy

© Bruegel 2026. Bruegel publications can be freely republished and quoted according to the Creative Commons licence CC BY-ND 4.0. Please provide a full reference, clearly stating the relevant author(s) and including a prominent hyperlink to the original publication on Bruegel's website. You may do so in any reasonable manner, but not in any way that suggests the author(s) or Bruegel endorse you or your use. Any reproduction must be unaltered and in the original language. For any alteration (for example, translation), please contact us at press@bruegel.org. Publication of altered content (for example, translated content) is allowed only with Bruegel's explicit written approval. Bruegel takes no institutional standpoint. All views expressed are the researchers' own.
"""
