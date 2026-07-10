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
# The flaws in the European Union's proposed Industrial Accelerator Act and how to fix them

Antoine Mathieu Collin, Ignacio García Bercero, Ben McWilliams and Simone Tagliapietra

Antoine Mathieu Collin (antoine.mathieu-collin@bruegel.org) is a Visiting Fellow at Bruegel

Ignacio García Bercero (ignacio.garcia@bruegel.org) is a Senior Fellow at Bruegel

Ben McWilliams (ben. mcwilliams@bruegel.org) is an Affiliate Fellow at Bruegel

Simone Tagliapietra (simone. tagliapietra@bruegel.org) is a Senior Fellow at Bruegel

## Executive summary

THE INDUSTRIAL ACCELERATOR ACT (IAA), proposed by the European Commission in March 2026, is intended to boost demand for European Union-made, low-carbon steel, cement, clean technologies and electric vehicles. It sets a target for manufacturing to contribute 20 percent of EU GDP by 2035 and introduces 'Made in EU' (or trusted partners) and low-carbon preferences into public procurement and support schemes, along with conditions on foreign direct investment (FDI).

THE IAA COULD potentially impact billions of euros in annual subsidies and public procurement spending. Because of this, it is important that policymakers address three shortcomings when finalising the law. First, the 20 percent manufacturing target lacks an economic rationale and distorts resource allocation. Second, origin-based content rules in support schemes risk delaying decarbonisation, raising costs for firms and consumers, and inviting challenges at the World Trade Organization. Third, the choice of sectors covered by the IAA has not been justified transparently and does not account for industry's need to adapt to new competitive challenges.

TO TURN THE IAA into an effective instrument of clean industrial transformation, EU policymakers should drop the 20 percent GDP target, provide rigorous justification for the selection of strategic sectors, replace origin-based content rules with existing sustainability and resilience criteria, ensure reciprocal market access rather than blanket exclusions, apply FDI screening in a way that does not block value-adding investment and remain open to green energy-intensive intermediate inputs.

## 1 Introduction

Economic competitiveness and building the resilience of domestic industry are priorities for the European Union. The EU Clean Industrial Deal, a plan proposed by the European Commission in early 2025, is intended to accelerate decarbonisation while securing the future of manufacturing in Europe through measures including electrification to cut energy costs and increasing investment in large green industrial projects (European Commission, 2025a). At the heart of this effort lies the need to boost demand for clean products in Europe.

In March 2026, the European Commission proposed a regulation that aims to achieve this: the Industrial Accelerator Act (IAA; European Commission, 2026a) $^{1}$ . The proposed approach is controversial because of disagreement over the degree to which the EU should introduce protectionist measures to shield domestic industry from foreign competition. Nevertheless, the IAA matters for three reasons. First, it proposes to attach conditions to billions of euros in annual subsidies and public procurement spending. Second, it contains the first proposal for a regulatory 'Made in EU' (sic) standard and may become a template for future initiatives in other sectors, such as digital and biotech. Third, alongside trade measures, it is Europe's response to the competitiveness challenge posed by Chinese dominance of clean technology and other industrial value chains $^{2}$ .

In this Policy Brief, we describe the IAA proposal and place it into international and historical contexts. In section 4, we make an economic assessment of the plan. In section 5, we make recommendations on how the IAA can be strengthened ahead of its final adoption $^{3}$ .

## 2 What does the IAA propose?

The IAA is built upon an explicit industrialisation objective: that the share of the EU economy devoted to manufacturing should grow from 14 percent today to 20 percent by 2035. To get to this objective, four ‘pillars’ are set out (Table 1).

The first is the introduction of mandatory ‘Made in EU’ and low-carbon requirements for public procurement – such as a government purchasing steel to build a bridge or a local council leasing a bus fleet – and support schemes targeting certain goods. Support schemes might cover, for example, electric vehicle subsidies or auctions to connect new solar and battery plants to the electricity grid.

The IAA second pillar is the application of conditions to some foreign investment in

1 See European Commission press release of 4 March 2026, 'Commission proposes Industrial Accelerator Act to strengthen industry and create jobs in Europe', https://ec.europa.eu/commission/presscorner/detail/en/ip\_26\_515.

2 Peggy Corlin, 'China pushes EU capitals to scrap 'Made in Europe' law or face retaliation', Euronews, 29 April 2026, https://www.euronews.com/my-europe/2026/04/29/china-pushes-eu-capitals-to-scrap-made-in-europe-law-or-face-retaliation.

3 At the time of writing, legislative discussions on the proposed IAA are at an early stage.

the EU. The conditions would be triggered when three criteria are met: the investment is in manufacturing, the investment exceeds €100 million and the investment is in a sector in which more than 40 percent of global production capacity is controlled by the country from where the investment comes. The third and fourth pillars involve the speeding up of permitting for industrial projects and designation by national governments of industrial-acceleration areas to attract low-carbon investment.

Table 1: Proposed measures in the IAA

<table><tr><td colspan="10">Headline target: industry = 20% of share of GDP</td></tr><tr><td colspan="2">Speeding up permitting</td><td colspan="2">Create lead markets for certain strategic sectors</td><td colspan="5">Conditions on FDI in strategic sectors (meet 4 out of 6)</td><td>Industrial acceleration areas</td></tr><tr><td>Single access point for permitting</td><td>Stricter deadlines for permit granting</td><td colspan="2">(i) Union origin requirements(ii) Low-carbon requirements</td><td colspan="5">(i) investments &gt; €100 million(ii) when a single third-country supplier &gt; 40% of global manufacturing capacity(iii) for batteries, EVs, solar panels, critical raw materials</td><td>Facilitate finance, research, energy grid, skills, permits in such areas</td></tr><tr><td colspan="2"></td><td>In public procurement</td><td>In public support schemes</td><td>1&amp;2 minority owned or minority joint venture</td><td>3 hiring more than 50% Europeans</td><td>4 investing 1% of asset revenue into R&amp;D</td><td>5 creating a website to detail local- content approach</td><td>6 licensing intellectual property</td><td></td></tr></table>

Source: Bruegel. Note: see the annex for further detail.

The European Commission has defined the strategic sectors to which these provisions would apply. They include energy-intensive industries, net-zero technologies and automobile manufacturing. In this context, energy-intensive industries are steel, cement and aluminium production, while net-zero technologies are the production of batteries, electrolysers, heat pumps, wind and solar power equipment. The selected sectors account for 15 percent of EU manufacturing production according to the draft IAA (European Commission, 2026a).

## 2.1 What does 'Made in EU' mean?

The provision that has attracted the most pushback inside the Commission $^{4}$ , from European industry $^{5}$ and governments is the definition of ‘Made in EU’ (Wunnerlich and Drumm, 2026). The Commission uses the term ‘Made in EU’ in its public communications, but the proposed IAA defines both ‘content of Union origin’ and ‘content equivalent to Union origin’. The definition of ‘content equivalent to Union origin’ is not uniform across the different provisions of the IAA, which introduces complexity.

In particular, for public procurement, product content that comes from countries with free trade agreements (FTAs) or in a customs union with the EU, or which are parties to the World Trade Organization Government Procurement Agreement (GPA), is considered equivalent to EU content. This excludes China. Countries with FTAs are also excluded if the FTA includes no procurement commitments – this is the case for India, for example. But for public support schemes, the definition includes all countries that have concluded an FTA or a customs union with the EU, which notably excludes both the United States and China. For the special case of electric vehicles, the draft implies that only EVs assembled in the EU, excluding FTA partners, would qualify $^{6}$ . In addition, a disproportionate-cost clause means that 'Union origin or equivalent' requirements can be sidelined if the associated cost increase is above 20 percent to 30 percent, depending on the measure and product.

Importantly, the proposal would give the European Commission powers to withdraw equivalency, fully or partly, on grounds of reciprocity in case a third country does not apply equivalent national treatment to EU firms in a sector covered by the IAA, or on economic-security grounds in case of excessive dependence on a single third-country supplier.

## 2.2 Conditions applied to clean-technology auctions and support schemes

For clean technology auctions, building on the Net-Zero Industry Act (NZIA), the IAA raises the existing threshold for non-price sustainability and resilience criteria in renewable energy auctions. The IAA amends the NZIA to increase the requirement to apply such criteria – now including an explicit 'Made in EU' (Union-origin) requirement – from 30 percent to 40 percent of auctioned volume, or 8 GW per year, whichever is lower.

For clean technologies covered by the NZIA, the IAA makes Union-origin compliance a condition of eligibility for both demand-side and manufacturing support schemes respectively.

Together, these requirements would affect billions of euros in annual government spending. In 2023, European governments allocated €63 billion to support renewable energy sources alone (European Commission, 2025b). The precise financial exposure for other type of public support schemes is difficult to quantify but is substantial, given the breadth of support schemes covered.

## 2.3 Public procurement of clean energy-intensive products becomes mandatory

The IAA, as proposed, is potentially transformative in proposing low-carbon product shares for public procurement of steel, aluminium and cement. These sectors account for around half of the EU's industrial greenhouse-gas emissions, and public procurement can provide much-needed demand for early green investors. The IAA proposes that, by 2029, at least 25 percent of the steel and aluminium, and 5 percent of the concrete, bought by governments via public procurement or under public support schemes that benefit households or companies to support the construction or renovation of buildings must be low-carbon. Low-carbon and EU-origin requirements should apply to support schemes covering at least 45% of the total national budget allocated. In addition, 'Union origin or equivalent' requirements are included for aluminium and cement, but not for steel.

## 2.4 A stricter approach to electric vehicles?

Many European countries offer consumer subsidies for EV purchases and EU law requires these schemes to apply resilience $^{7}$ and sustainability conditions. The IAA would require national public-procurement procedures and government subsidy schemes for EVs (notably for corporate EVs) to include EU-origin or equivalent requirements for the battery and 70 percent of the non-battery components, including items such as electric motors, power electronics, semiconductors, chassis and interior sound systems.

The EU has already introduced, after concluding anti-subsidy investigations, countervailing duties ranging from 10 percent to 40 percent on EVs produced in China $^{8}$ . The European Commission has also proposed, separately from the IAA, weakening a 2035 target for phasing out new polluting cars, reducing a requirement for all newly registered cars and to be zero emission to a 90 percent emissions reduction $^{9}$ , because of weaker-than-expected consumer demand for EVs. Together with subsidies, these measures are intended to provide support for European producers but there is no recognition that such support should be temporary and intended to provide breathing space to adjust to the reality of Chinese competition. The risk of shielding domestic industries from foreign competition over the long term is that innovation will be disincentivised and prices for consumers will be raised.

The proposed IAA text is unclear on how the ‘Union origin or equivalent’ principle would apply to EV assembly, and whether only EVs assembled in the EU, excluding FTA partners, would qualify. The European Commission should clarify this point urgently: a restrictive interpretation would be contrary to the EU’s WTO and FTA commitments.

It is also unclear if small EVs manufactured by FTA partners would qualify for favourable treatment, as applied to EU EVs, for the purposes of emission calculations $^{10}$ . This prompted reaction from the EU's main trade partners. Japanese business has noted, for example, that certain Japanese products might be considered equivalent to European products, but others not $^{11}$ .

## 2.5 Conditions on incoming FDI

The proposed IAA's industrialisation objective is framed as domestic production, irrespective of ownership. Alongside encouragement of domestic manufacturing, the IAA would introduce new requirements for foreign companies investing in the EU. These conditions would apply to investors from third countries that have global manufacturing capacity shares of more than 40 percent in the identified strategic sectors (Figure 1).

In practice the threshold is binding only for China for batteries, solar PVs and certain critical raw materials. Chinese investment would have to comply with four out of six other criteria: entering into minority ownership or a compulsory minority joint venture, Europeans making up more than 50 percent of the personnel in the facility or plant that is the subject of the investment, investing 1 percent of asset revenue in R&D, creating a website detailing the local-content approach and licensing intellectual property related to the asset that is the subject of the investment.

Importantly, the IAA would impose an EU-origin (and EU-only) requirement for products and components, and the exclusion of high-risk suppliers, as conditions for foreign investors to receive state aid for the construction and manufacturing of net-zero technologies. EU countries would be able to derogate from these requirements if they are practically infeasible or too costly (more than 25 percent cost surcharge). This would be an additional hurdle for Chinese FDI in the EU, which is often supported by state aid granted by host countries.

Unsurprisingly, China has criticised the IAA and threatened countermeasures on the basis that the proposals discriminate against China and include some WTO-inconsistent elements $^{12}$ . China has said local content requirements, mandatory transfer of intellectual property and technology, and restrictions on public procurement should be removed from the proposed IAA. Chinese opposition raises the risk that Chinese investment in the EU could be frozen, going against the objectives of favouring partnerships between EU and Chinese companies and attracting more value added investment.

# 3 Context: are the IAA proposals unusual?

## 3.1 EU local-content requirements

Traditionally, green subsidies in Europe have supported clean industries irrespective of where products are produced. For example, solar support schemes beginning in the 2000s offered fixed payments for the electricity generated from a solar power system connected to the grid, with the origin of the solar panels considered irrelevant (Kuntze and Moerenhout, 2013). The logic is that growing green industries is good for the climate transition, regardless of the source of the good, and that European consumers benefit from access to competitive green goods.

In 2024, the EU broke from this approach when the Net-Zero Industry Act (NZIA, Regulation (EU) 2024/1735) entered into force. The NZIA introduced mandatory 'sustainability and resilience' criteria, either as a requirement or as an award criterion, for clean-tech public procurement, auctions and consumer schemes. For public procurement, countries must include non-price sustainability and resilience criteria for 30 percent of auctioned volumes. These criteria must be taken into consideration alongside price and quality criteria. In 2025, Italy was the first country to run an auction including such criteria, awarding 1.1 gigawatts of solar installed capacity to projects excluding Chinese components (cells, modules and inverters) $^{13}$ .

The NZIA requirements clash with the longstanding prohibition under EU law and competition policy of local-content requirements (LCRs), in line with the EU's traditional commitment to open trade. Other major economies have been less cautious: the United States built local-content rules into the 2022 Inflation Reduction Act (Kleimann et al, 2023) for a range of clean technologies, and is further strengthening them for wind power and iron $^{14}$ . China has used LCRs throughout its industrial development, especially in clean technologies. Canada has introduced LCRs into EV subsidies $^{15}$ . A points system for weighting electric vehicle subsidies in Japan takes into account domestic production, locally sourced batteries and supply-chain resilience $^{16}$ .

In line with the NZIA sustainability and resilience criteria, France's bonus écologique for EVs incorporates a carbon-footprint requirement that de facto excludes several

foreign-built vehicles $^{17}$ . This shows that NZIA sustainability and resilience criteria can deliver the de-risking objective the IAA pursues with explicit 'Union origin or equivalent' content rules, but without the risk of breaking WTO rules or the competitiveness costs of an origin-based regime.

## 3.2 International context

While the mooted IAA procurement conditions appear consistent with WTO and FTA obligations, the proposal to link consumption subsidies or other incentives to 'Union origin or equivalent' conditions entails a serious risk of legal challenge at the WTO by countries that are not party to an FTA with the EU. Exceptions to the General Ag

[中间内容因长度限制已省略]

ystem/files/2023-08/Bruegel%20Blueprint%2033%20080823%20web.pdf

Hufbauer, G.C., J.J. Schott, C. Cimino-Isaacs, M. Vieiro and E. Wada (2013) Local Content Requirements: A Global Problem, Peterson Institute for International Economics, available at

IEA (2026) Energy Technology Perspectives 2026, International Energy Agency, available at https://www.iea.org/reports/energy-technology-perspectives-2026

Juhász, R., N. Lane and D. Rodrik (2024) 'The New Economics of Industrial Policy', Annual Review of Economics 16: 213-242, available at https://doi.org/10.1146/annurev-economics-081023-024638

Kleimann, D., N. Poitiers, A. Sapir, S. Tagliapietra, N. Véron, R. Veugelers and J. Zettelmeyer (2023) 'How Europe should answer the US Inflation Reduction Act', Policy Contribution 04/2023, Bruegel, available at https://www.bruegel.org/policy-brief/how-europe-should-answer-us-inflation-reduction-act

Kuntze, J.-C. and T. Moerenhout (2013) Local Content Requirements and the Renewable Energy Industry – A Good Match? International Centre for Trade and Sustainable Development, available at https://unctad.org/system/files/non-official-document/DITC\_TED\_13062013\_Study\_ICTSD.pdf

Mähönen, M., L. Martini, J. Gardiner, S. Lehtilä and B. Görlach (2023) Public Procurement for Climate Neutrality: a transformative policy instrument? 4i-TRACTION, University of Eastern Finland and Ecologic Institute, available at https://www.ecologic.eu/19385

McWilliams, B., S. Tagliapietra and J. Zettelmeyer (2025) 'Reconciling the European Union's clean industrialisation goals with those of the Global South', Policy Brief 18/2025, Bruegel, available at https://www.bruegel.org/sites/default/files/2025-07/PB%2018%202025\_1.pdf

Pisani-Ferry, J., B. Weder di Mauro and J. Zettelmeyer (2024) 'How to de-risk: European economic security in a world of interdependence', Policy Brief 07/2024, Bruegel, available at https://www.bruegel.org/system/files/2024-05/PB%2007%202024.pdf

Resende Carvalho, L., E. Cornago, E. Höra and P. Jäger (2025) 'Between a rock and a hard place: Europe's clean tech industry between Trump's policies and Chinese pressure', Policy Brief, Bertelsmann Stiftung, available at https://www.bertelsmann-stiftung.de/fileadmin/files/user\_upload/EZ\_PB\_Cleantech\_2025\_ENG.pdf

Rodrik, D. (2016) 'Premature deindustrialization', Journal of Economic Growth 21: 1-33, available at https://doi.org/10.1007/s10887-015-9122-3

Sapir, A., T. Schraepen and S. Tagliapietra (2022) 'Green Public Procurement: A Neglected Tool in the European Green Deal Toolbox?' Intereconomics 57(3), available at https://www.intereconomics.eu/contents/year/2022/number/3/article/green-public-procurement-a-neglected-tool-in-the-european-green-deal-toolbox.html

Wunnerlich, A. and E. Drumm (2026) 'The EU's Industrial Accelerator Act Puts Pedal to the Metal', Insights, 19 March, German Marshall Fund, available at https://www.gmfus.org/news/eus-industrial-accelerator-act-puts-pedal-metal

Annex: key provisions of the proposed IAA

<table><tr><td>Measure</td><td>Articles</td><td>Provisions</td></tr><tr><td>Headline target</td><td>Art. 2</td><td>Industry to contribute 20% of EU GDP by 2035</td></tr><tr><td>Faster permit-granting for industrial projects, including decarbonisation of energy-intensive industries</td><td>Art. 4, Art. 5</td><td>Single access point for permitting; stricter deadlines for permit granting</td></tr><tr><td>Lead markets for strategic sectors via (i) Union origin requirement and (ii) low-carbon requirements in (a) public procurement and (b) public-support schemes</td><td>Art. 7–8 (Union origin), Art. 10 (low-carbon products), Art. 11 (procurement), Art. 12 (support schemes), Art. 13 (corporate vehicles), Art. 14 (super credits), Art. 15 (ex post verification), Art. 16 (delegated acts)</td><td>Union origin = content from the EU, FTA partners and customs-union countries; GPA partners included for procurement only. Requirements apply up to 45% of national budgets (100% for EVs). The Commission can exclude trading partners on non-reciprocity grounds. Definition of low-carbon products based on existing legislation and delegated acts</td></tr><tr><td>Conditions on inbound FDI in strategic sectors</td><td>Art. 17–24</td><td>Apply to investments above €100 million in sectors for which a single third country controls more than 40% of global manufacturing capacity (batteries, EVs, solar panels, critical raw materials). Investors must satisfy four out of six criteria: minority ownership or minority joint venture; more than 50% European employment; investment of 1% of asset revenue in R&amp;D; transparent local-content disclosure; intellectual-property licensing</td></tr><tr><td>Industrial manufacturing acceleration areas</td><td>Art. 25–27</td><td>Member states designate areas and concentrate on finance, R&amp;D, energy-grid, skills and permitting support</td></tr></table>

## Republishing and referencing policy

© Bruegel 2026. Bruegel publications can be freely republished and quoted according to the Creative Commons licence CC BY-ND 4.0. Please provide a full reference, clearly stating the relevant author(s) and including a prominent hyperlink to the original publication on Bruegel's website. You may do so in any reasonable manner, but not in any way that suggests the author(s) or Bruegel endorse you or your use. Any reproduction must be unaltered and in the original language. For any alteration (for example, translation), please contact us at press@bruegel.org. Publication of altered content (for example, translated content) is allowed only with Bruegel's explicit written approval. Bruegel takes no institutional standpoint. All views expressed are the researchers' own.
"""
