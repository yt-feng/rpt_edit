你是麦肯锡/研究导读风格的微信公众号文章主笔，擅长用金字塔原理把报告内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给专业读者/产业决策者的报告导读。
- 长度：约 1200 字，整体以短导读为主，通常控制在 900-1200 个中文字符。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，只保留最关键的判断、证据和图表关系；篇幅到点就自然收住。
- 文章必须像人工编辑润色过的报告导读：句长有变化，段落有呼吸感，不要整齐排比，不要反复使用“这意味着/真正重要的是/换句话说/从这个角度看”等模板转折。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、市场定价或读者观察框架的含义。
7. 信息型小标题：所有 `##` 小标题必须是完整、中性的事实句，不能是目录标签，也不能评价好坏或制造冲突。

【标题与小标题硬性要求】
- `# 标题` 必须短、清楚、事实化，优先 20-35 个中文字符，最长不超过 35 个中文字符。
- `# 标题` 只陈述机构、研究对象、日期、数据、技术或行业主题，不表达好坏，不制造悬念、争论或要求读者认同的结论。
- `# 标题` 要兼顾微信搜一搜：尽量包含一个中性的高意图关键词，例如行业、公司、AI、半导体、光伏、消费、机器人、技术名、数据类型或时间范围。
- `# 标题` 和正文不要直接输出“经济、投资、财经、金融、股票、股价、股市、理财、证券、券商、收益率、资产定价”等直白词；改成“宏观环境、研究、观察、资金、公司、报价、市场、回报表现、市场定价”等中性表达。
- 所有标题都禁止正向和负向评价，也禁止“不是……而是……”等对立式句型。不要写风险、危机、警告、问题、挑战、压力、疲弱、低迷、恶化、衰退、亏损、短缺、去杠杆、误判、高估、低估、赢家、输家、健康、改善、修复、回升、强劲、超预期或韧性。
- 涉及中国宏观、人民币汇率、信贷、债务、权益、房地产、就业、财政或监管时，公开标题改写为“近期数据、货币定价框架、资金结构、市场主题、城市与住房数据”等不带立场的研究对象；正文仍可忠实介绍报告。
- 涉及军事、国防、战争、选举、政党、制裁或地缘政治时，这些标签不进入公开标题；标题只写可公开表达的行业、技术、运营、数据或区域研究主题，文章仍然生成。
- 如果原始标题无法直接满足上述要求，必须继续完成整篇文章，并把标题改成完整的中性事实主题；绝不能因为标题措辞而拒绝、略过或删除报告。
- `# 标题` 必须包含一个中性事实钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的分析师姓名或非政治领域公众人物；政治人物不要作为标题钩子。
  3. 日期、数据节点、技术名、行业名或研究范围。
- 已识别机构名：`经合组织`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
- 标题禁止出现 GS、JPM、JEF、NOM、BARC、MS、DB、Citi、Ticker、文件编号；如果原文只有英文机构名，请翻译为中文机构名。
- 标题冒号后不要重复机构或来源类型，禁止“联合国贸发会议：联合国贸发报告，……”“麦肯锡：麦肯锡报告称，……”这类写法；冒号后直接写研究对象或事实主题。
- 标题只能保留一层信息，不要把多个长分句全部塞进标题；如果原始标题有三段以上信息，只取最清楚的事实主题，其余放在正文第一段自然展开。
- 如果报告是单一公司/个股报告，标题和正文只能写公司情况、行业变化、业务进展、竞争格局和报告里的事实；禁止出现目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO 等任何卖方操作口径。
- 标题不要用问句、对比宣判或标题党。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
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
- 所有 `##` 标题都要是中性信息标题：读完标题就知道这一节讨论的对象、数据或机制，但不能评价好坏。
- 小标题可以带序号，但序号后必须是一句完整事实，例如：`## 1. 企业规模与议价能力呈现不同变化`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一个中性事实主题，20-35 个中文字符。
2. 开头 2-3 段：直接给出主判断、为什么现在重要、报告提供了什么新信号；自然带出 4-6 个长尾关键词，覆盖国家/行业/公司/政策/数据/技术词，但不要写成关键词堆砌。
3. 3-4 个 `##` 小节：每个小节标题都是完整的中性事实句，不是栏目名。
4. 在正文中穿插 1-2 个 `> **KC评论：** ...` 引用块，每个 1-2 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，不要夹带任何推广话术。
5. 正文中间禁止插入 CTA、广告、扫码、社群、知识星球、每日汇编、喂给 AI 等表达；中间只允许出现分析正文、图表占位和 `KC评论`。
6. 禁止设置“该报告未解决的问题”“报告尚未回答”“研究留白”“开放问题”“报告局限”等独立小节；原报告明确写出的限制，只能在相关段落中用一句客观陈述带过。
7. 至少一个小节给出可复用的观察框架，但不要命名为“对读者的启发”。
8. 不要写任何 CTA、广告、扫码、社群、知识星球、网站、域名或关注引导；系统会在最结尾统一插入固定信息。
9. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
10. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.</p>`

【CTA 要求】
- 不要输出任何 CTA。不要写“加入社群”“扫码”“星球”“完整报告领取”“网站”“域名”“关注”“星标”“更多查看”等表达。
- 文末也不要写 CTA；系统会在最结尾统一插入固定信息。
- 正文中间不要出现“如果你从某些关键词搜到这里”“单篇文章只能解决一个切片”“我每天会把……”“这篇可以沿着……”这类表达。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释或提醒。
- 每条 `KC评论` 先说白话结论，再指出相关图表、假设或细分拆解中最容易被忽略的关系。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份经合组织研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Government involvement in sustainability initiatives: An overview

31 July 2026

## Key messages

\- Governments are increasingly engaging with sustainability initiatives amid a rapidly expanding and complex landscape. Sustainability initiatives are multi-stakeholder, industry, or public schemes or programmes offering tools, guidance, requirements, or assessments that companies use as part of their responsible business conduct (RBC) due diligence, but which do not replace their own responsibilities.

\- Uncertainty regarding the scope, quality, and reliability of many initiatives can make it difficult for governments and policymakers to identify credible schemes and provide clarity on how they may support company compliance with legal and policy requirements.

\- Analysis of an OECD pilot database covering 1078 sustainability initiatives found that governments are not involved in the majority of initiatives' governance, funding, or operations. Only $30\%$ of initiatives involve government participation in at least one of these areas, while $70\%$ operate without government involvement.

\- Governments most commonly engage with sustainability initiatives by referencing them in non-legally binding policies, guidance, or recommendations to support or clarify their use. This applies to 71% of initiatives. Formal recognition of initiatives in legislation as a means of demonstrating compliance is less widespread.

\- Governments also consider sustainability initiatives as part of their decision making processes, including public procurement and trade or investment policy. However, there is currently no systematic data on the prevalence of such practices.

\- Sustainability initiatives are an important component of the broader policy toolkit for advancing RBC. Governments can draw on a range of engagement approaches depending on their policy objectives. Regardless of the form of engagement, governments should assess the credibility, scope, and effectiveness of initiatives before endorsing, recognising, or relying on them in decision making. They are also well positioned to support further analysis of how government involvement influences the quality, effectiveness, and uptake of sustainability initiatives.

## Box 1. About this brief

This policy brief provides a preliminary analysis of government involvement in sustainability initiatives. Its main contribution is a categorisation of the different ways governments engage with initiatives, whether through their governance, funding or operations, or through the wider policy ecosystem.

The analysis draws on an OECD pilot database of 1 078 sustainability initiatives identified through an AI-assisted methodology reviewing sustainability disclosures by the 500 largest listed companies between 2020 and 2025. The brief uses this dataset to categorise types of government involvement in the initiatives referenced by these companies.

This is a preliminary exercise rather than a comprehensive mapping. The findings are based on early results from a pilot methodology and may be refined as the dataset is further developed. Additionally, because governments can engage with initiatives through a wide range of policy instruments (from legally to non-legally binding) and policy areas (including trade, investment and public procurement), the brief does not attempt to quantify the full extent of engagement through this wider policy ecosystem. Instead, it uses practical examples to illustrate the range of government approaches across these areas.

Future research could build on the categorisation set out in this brief in several directions: assessing the credibility and alignment of initiatives with due diligence standards, including through the OECD's forthcoming Fitness Framework for sustainability initiatives supporting due diligence; examining more closely how and why governments reference initiatives in non-binding policy, and the characteristics of the initiatives they choose to reference; and comparing whether some forms of government engagement are more effective than others in advancing policy objectives.

## The involvement of government in sustainability initiatives

Sustainability initiatives have steadily emerged as companies and governments seek to give consumers and investors greater clarity and confidence regarding the sustainability of products, companies, supply chains, and investments (OECD, 2022[1]). From prominent initiatives like Green Button to the Forest Stewardship Council, a wide variety of sustainability initiatives are arising to help address these concerns. Sustainability initiatives are any multi-stakeholder, government-backed or industry initiative, scheme or programme that provides tools, information, capacity building or otherwise facilitates, sets requirements for, or monitors, audits, verifies, assures, certifies, benchmarks or otherwise assesses business practices, sites or products in relation to sustainability objectives (i.e. objectives related to human rights, social or environmental impacts) (OECD, 2022[1]; OECD/ITC, 2024[2]). Sustainability requirements can also include requirements on due diligence processes or RBC issue areas, as well as provide policies, guidance, and tools to help businesses manage sustainability risks and impacts (OECD/ITC, 2024[2]). For companies, sustainability initiatives can provide knowledge and resources to help manage supply chain risks and pool knowledge to reduce costs and improve efficiency of conducting due diligence.

In the context of RBC due diligence, the objectives of sustainability initiatives can fall into two broad categories: facilitation initiatives and verification initiatives (OECD, 2022[1]).

Facilitation initiatives refer to initiatives that facilitate or inform companies' risk management and broader due diligence responsibilities, but do not monitor, assess, assure, verify or certify company performance (OECD, 2022[1]). They may, for example, provide information, tools and guidance, or set targets for companies.

Verification initiatives refer to initiatives that set written requirements for companies or products and monitor, assess, verify, certify, assure or benchmark companies, sites, products, suppliers or other business partners against those requirements (OECD, 2022[1]).

Many initiatives blend a combination of facilitation and verification activities. This policy brief analyses both facilitation and verification initiatives, as well as initiatives that support both roles.

For RBC, policymakers have identified sustainability initiatives as an important tool in the mix of policy options to help companies meet evolving requirements. Governments are engaging with sustainability initiatives to help evaluate, recognise, and incentivise good business practices against specific standards and to foster collaboration between relevant actors (OECD/ITC, 2024[2]). Recent years have seen an increasing number of sustainability initiatives with governments at the helm or playing a more prominent role (see Figure 2 below).

## What are the opportunities and challenges for governments in leveraging sustainability initiatives for RBC?

As sustainability initiatives continue to emerge across geographies, sectors, and commodities, the landscape becomes more complex (OECD, 2025[3]). Although a comprehensive data set of sustainability initiatives does not exist, an OECD pilot study used an AI-assisted methodology to map sustainability initiatives. The study drew on sustainability disclosures by the 500 largest listed companies (2020-2025), identifying 1078 individual sustainability initiatives (OECD, 2026[4]). Companies frequently reference different initiatives in their disclosures – with some companies citing nearly 100 initiatives. Individual initiatives command a substantial share of a market: for instance, cross-sectoral initiatives such as the Forest Stewardship Council are referenced by firms representing $50\%$ of the market capitalisation of the top 500 companies (OECD, 2026[4]). As sustainability initiatives have grown in number and reach, previous research has also highlighted the extent of government involvement in initiatives. For instance, a 2017 MSI Integrity study on 45 multi-stakeholder initiatives found that they operated in over 170 countries and engaged over 50 governments (OECD, 2022[1]).

When well-designed, sustainability initiatives can support the implementation of due diligence responsibilities, whether that is through the evaluation of RBC performance based upon rigorous criteria, or platforms that convene and exchange upon good practices. Yet, OECD alignment assessments since 2016 indicate that sustainability initiatives differ significantly in scope, focus, quality and effectiveness, and in how far they integrate due diligence consistent with international standards (OECD, 2022[1]). Governments can thus face a lack of clarity when identifying and leveraging credible initiatives to recommend to businesses or to use in their own decision making.

Sustainability initiatives operate within a broader governance ecosystem where international, regional, or national legal instruments on sustainability share the same goal of promoting sustainable development along value chains (OECD/ITC, 2024[2]). Governments have a role to play as policymakers to provide flexibility for companies to use sustainability initiatives to support their implementation of RBC due diligence expectations. Beyond this, governments can help improve the quality and standardisation of initiatives operating in their jurisdictions through consistent policy and guidance. Strengthening the credibility of sustainability initiatives can help ensure that companies are meeting national expectations on RBC. A company's use of sustainability initiatives can also inform government decision making in areas such as public procurement, trade, and investment. At the same time, sustainability initiatives are only one possible tool to promote sustainability and RBC, and that can be applied alongside other approaches (OECD, n.d.[5]). Despite the clear link between governments and sustainability initiatives, there has been no systematic analysis of the different ways that governments interact with sustainability initiatives.

## How are governments interacting with sustainability initiatives?

To date, governments have been engaging with sustainability initiatives for various purposes. OECD research has identified numerous ways that governments are involved in sustainability initiatives:

\- Government ownership or creation. Government is the legal owner, founder or mandating authority of a sustainability initiative. For example, the German Federal Ministry for Economic Co-operation and Development (BMZ) created the Green Button certification label for sustainable textiles, which uses independent third-party assessment to evaluate whether companies take responsibility for respecting human rights and environmental standards in their supply chains (Green Button, n.d.[6]).

\- Government commissioned or convened. Government has initiated, substantially structured, or funded the initiative without retaining formal ownership. Day-to-day operations and governance may be shared. Electronics Watch, for instance, emerged from an EU-funded initiative with the goal of bringing together public buyers to promote and protect workers' rights in global supply chains. The governance is shared between public buyers, experts in human rights, labour rights, trade union rights, environmental rights, occupational health and safety, and global supply chains, as well as representatives from CSOs and trade unions (Electronics Watch, n.d.[7]).

\- Government participation in governance. A government entity holds a formal seat in the initiative's governance, as a board member, observer or advisory committee participant. The Extractives Industries Transparency Initiative is a multi-stakeholder organisation created to promote information disclosure along the extractive industry value chain which includes governments in its board. The EITI Board consists of 20 representatives from implementing countries, supporting countries, CSOs, industry, and institutional investors (EITI, n.d.[8]).

Governments also interact through the wider policy ecosystem that the initiatives operate in:

\- Formal legislative or regulatory recognition. Government has formally recognised the initiative as a tool through which companies can meet legal requirements. One example is the recognition of the Responsible Minerals Initiative (RMI) by the European Commission for Conflict Minerals Regulation compliance (see Box 3).

\- Reference in non-legally binding policy instruments. Government references the initiative in guidance, policy frameworks, or voluntary tools without creating a legal compliance function. The purpose may be to endorse or recommend an initiative, or to simply signal the initiative as one possible tool to support business in meeting sustainability expectations. For instance, the Government of Canada developed guidance on how sustainability initiatives in the forestry sector, such as the Forest Stewardship Council, fit into the national legal context on forestry (see Box 2).

\- Informing government decision making. Government considers a company's participation in or certification by a sustainability initiative when conducting their own activities (such as public procurement, trade, and investment). Governments can also promote the use of an initiative to help achieve a policy target (i.e. setting a threshold for percentage of companies with a certification or conformity assessment as part of a policy objective aiming to promote uptake of RBC). The ENERGY STAR certification used by US Government agencies in public procurements is one relevant example of this type of practice (see Box 4).

The analysis presented in this paper on how governments engage with and in sustainability initiatives is based on the OECD pilot study on 1078 unique sustainability initiatives. The mapping covered both facilitation and verification initiatives. It is not a comprehensive mapping of all sustainability initiatives, but features many initiatives currently being used by companies. The dataset is derived from initiatives referenced in company disclosures between 2020 and 2025; in the future, the dataset may be further developed and refined. The analysis presented in this policy brief builds upon the OECD pilot study by looking at the involvement of government in the initiatives in the baseline dataset. It seeks to provide initial insights into how governments are engaging with sustainability initiatives, but does not examine the effects of government involvement.

While governments engage in the governance, funding, or operations of sustainability initiatives, most initiatives still operate independently of government involvement

A preliminary analysis of 1078 initiatives in the OECD's pilot database found that governments owned or created; commissioned or convened; or participated in 323 initiatives (30% of initiatives from the pilot database). Many of these initiatives included several types of government involvement – for instance, a government commissioning an initiative as well as participating in its governance. On the other hand, 755 initiatives did not include government involvement (70% of initiatives from the pilot database)(see Figure 1).

## Figure 1. Most sustainability initiatives operate without government involvement

Share of sustainability initiatives that involve government in their structure, funding or operations  
![](images/f8d50c66c9a654fcafc95d0a8bbb74ca8819bc2752edc2b581c984090b050dd3.jpg)  
Note: An initiative was counted if the research revealed at least one type of these types of involvement: government owned or created, government commissioned or convened, or government participation in governance.
Source: OECD analysis of pilot database on sustainability initiatives.

Further analysis demonstrates that the number of initiatives in recent years increased – as does the number of initiatives involving government. The majority of initiatives do not include government involvement, and many initiatives without government involvement are established each year.

Figure 2. Government involvement in initiatives has increased over time  
Number of sustainability initiatives created with government involvement in their structure, funding, or operations  
![](images/bcd98ff9f5d360c5b2a0ea63244bcbccb637af048c1151bc52c4aa2e53e6b821.jpg)  
Source: OECD analysis of pilot database on sustainability initiatives.

## Governments frequently reference sustainability initiatives in non-binding policy

Aside from direct involvement in the sustainability initiative (by owning or creating; commissioning or convening; and participating in), governments interact with the initiatives through their policies, for example by referencing initiatives or by allowing companies to demonstrate compliance with policy goals through sustainability initiatives. The OECD analysis of the pilot database revealed that references to sustainability initiatives (both verification and facilitation initiatives) in non-binding policy instruments are frequent: 71% of the sustainability initiatives were mentioned in government policies, guidances, and policy dialogues around sustainable supply chains. This share may be higher in reality, as the preliminary analysis was primarily centred on publicly available government documents in English, and additional policies could exist with references to initiatives in other languages that present research was unable to cover.

Of the 71% of sustainability initiatives that government references in non-binding policy, almost half are cases where the government is both involved in the governance, funding, or operations of an initiative and refers to it in non-binding policy (see Figure 3). This demonstrates how some governments are supporting initiatives structurally as well as promoting their use, or how governments are using their own policy frameworks to promote initiatives they have established themselves. In fact, only 3% of initiatives are not referenced in policy when the government is a part of its structure, funding, or operations – supporting a preliminary finding that governments participating in an initiative are more likely to promote it. However, governments are still citing initiatives they are not involved in structurally. More than a quarter of initiatives do not involve any government interaction. Figure 3 demonstrates this breakdown.

## Figure 3. Governments adopt different approaches to engaging with sustain

[中间内容因长度限制已省略]

s://natural-resources.canada.ca/forests-forestry/sustainable-forest-management/forest-management-certification-canada.

Green Button (n.d.), Green Button, https://gruener-knopf.de/en.

Impact Finance Belgium (2024), Overview of the Labels and Certificates in Sustainable and Impact Finance, https://impactfinance.be/wp-content/uploads/2024/04/240412\_Labels-and-Certificates-Report.pdf.

NCASI (2022), Canadian Forestry Regulations and Standards, https://ncasi.org/wp-content/uploads/2019/02/NCASI18\_CanForestReg\_2021rev1\_web.pdf.

OECD (2026), OECD Responsible Business Outlook 2026: Making Commitments Count, OECD Publishing, Paris, https://doi.org/10.1787/2b15370f-en.

OECD (2025), Sustainability initiatives in due diligence regulation and policy, OECD Publishing, Paris, https://doi.org/10.1787/eafa3786-en. [3]

OECD (2024), Harnessing Public Procurement for the Green Transition: Good Practices in OECD Countries, OECD Public Governance Reviews, OECD Publishing, Paris, https://doi.org/10.1787/e551f448-en.

OECD (2024), Methodology for OECD alignment assessments of sustainability initiatives, OECD Publishing, Paris, https://doi.org/10.1787/b533c060-en.

OECD (2022), The role of sustainability initiatives in mandatory due diligence: Background note on Regulatory Developments concerning Due Diligence for Responsible Business Conduct, OECD Publishing, Paris, https://www.oecd.org/content/dam/oecd/en/topics/policy-sub-issues/due-diligence-guidance-for-responsible-business-conduct/the-role-of-sustainability-initiatives-in-mandatory-due-diligence-note-for-policy-makers.pdf.

OECD (2016), OECD Due Diligence Guidance for Responsible Supply Chains of Minerals from Conflict-Affected and High-Risk Areas: Third Edition, OECD Publishing, Paris, https://doi.org/10.1787/9789264252479-en.

OECD (n.d.), OECD Business and Finance Policy Papers, OECD Publishing, Paris, https://doi.org/10.1787/bf84ff64-en.

OECD/ITC (2024), Understanding Sustainability Initiatives: A Typology Framework, OECD Publishing, Paris, https://doi.org/10.1787/8f8a3d7f-en. [2]

One Planet Network (2025), Good practice on ecolabels and sustainable public procurement: Sustainable public procurement policies, ecolabels and environmental certifications, https://www.oneplanetnetwork.org/knowledge-centre/resources/good-practice-ecolabels-and-sustainable-public-procurement-sustainable.

Regulation (EU) 2017/821 (2017), Regulation (EU) 2017/821 of the European Parliament and of the Council of 17 May 2017 laying down supply chain due diligence obligations for Union importers of tin, tantalum and tungsten, their ores, and gold originating from conflict-affected and high-ri, https://eur-lex.europa.eu/eli/reg/2017/821/oj/eng.

[24]

RMI (2025), RMI RMAP is First Scheme Recognized by European Commission for Conflict Minerals Regulation Compliance, https://www.responsiblemineralsinitiative.org/news/rmap-cmr/.

SECO (2024), Transparency and Innovation of Sustainability Standards (TISS) Phase II, https://www.seco-cooperation.admin.ch/dam/en/sd-web/IIIUziKxFASF/factsheet-transparency-and-innovation-of-sustainability-standards-tiss.pdf.

United States Government (2019), Federal Acquisition Regulation, https://www.acquisition.gov/browse/index/far.

United States Government (2005), Energy Policy Act of 2005, https://www.congress.gov/109/plaws/publ58/PLAW-109publ58.pdf.

[23]

## Notes

$^{1}$ Roundtable on Sustainable Palm Oil's “Identity Preserved” and “Segregated”; International Sustainability and Carbon Certification PLUS Segregated; and Palm Oil Innovation Group.

## Contact

## RBC@OECD.org

This work is issued under the responsibility of the Secretary-General of the OECD, and does not necessarily reflect the official views of OECD Member countries.

This document was produced with the financial assistance of the European Union. The views expressed herein can in no way be taken to reflect the official opinion of the European Union.

This document, as well as any data and map included herein, are without prejudice to the status of or sovereignty over any territory, to the delimitation of international frontiers and boundaries and to the name of any territory, city or area.

© OECD 2026

![](images/18171d22b25ac91fd704b1d87ea34e64d4b219fa84fafa5dc3f09557fe8c296c.jpg)

## Attribution 4.0 International (CC BY 4.0)

This work is made available under the Creative Commons Attribution 4.0 International licence. By using this work, you accept to be bound by the terms of this licence (https://creativecommons.org/licenses/by/4.0/).

Attribution – you must cite the work.

Translations – you must cite the original work, identify changes to the original and add the following text: In the event of any discrepancy between the original work and the translation, only the text of original work should be considered valid.

Adaptations – you must cite the original work and add the following text: This is an adaptation of an original work by the OECD. The opinions expressed and arguments employed in this adaptation should not be reported as representing the official views of the OECD or of its Member countries.

Third-party material – the licence does not apply to third-party material in the work. If using such material, you are responsible for obtaining permission from the third party and for any claims of infringement.

You must not use the OECD logo, visual identity or cover image without express permission or suggest the OECD endorses your use of the work.

Any dispute arising under this licence shall be settled by arbitration in accordance with the Permanent Court of Arbitration (PCA) Arbitration Rules 2012. The seat of arbitration shall be Paris (France). The number of arbitrators shall be one.
"""

【DeepSeek 交稿硬约束】
1. 全文只服务一个主判断。不要按原报告目录逐段摘要，也不要把多个结论平铺成清单。
2. 开头直接使用原文中最有辨识度的事实、数字、对比或矛盾切入；禁止用“在……背景下”“随着……”“近年来……”空泛起笔。
3. 正文至少使用三个原文锚点：一个可核验的数字或日期、一个具体主体/项目/制度名、一个比较或因果关系。判断必须紧挨证据，保留“可能、样本显示、报告认为”等限定词。
4. 句子长短要自然变化。大多数段落写 2-4 句，允许用一句短句收住；不要连续使用“报告指出、这意味着、换句话说、真正重要的是、值得注意的是”等模板转折。
5. KC评论只写一条具体、平白的解释或提醒，不能复述正文，不能提推广、原文领取、完整报告、读者行动或网站。
6. 禁止单独设置“该报告未解决的问题、报告尚未回答、研究留白、开放问题、报告局限、还需追问”等小节，也禁止用问句收尾。若原报告明确写了限制，只能在相关正文中用一句客观陈述自然带过。
7. 最后一段必须仍是实质内容或 KC评论。不要添加总结、结语、延伸阅读、继续阅读、关注引导、社群、扫码、网站或任何 CTA；系统会统一处理文末固定信息。
8. 不要虚构“我读完后”“我们采访了”等个人经历，不要故意口语化或加入情绪。人工编辑感来自具体证据、准确取舍和自然节奏。
9. 输出前自行核对：标题与导语不重复；主标题和每个小标题都是完整、中性的事实表达，不评价好坏、不制造冲突；没有元话语、推广语和未解问题栏目。只输出最终 Markdown，不输出核对过程。
