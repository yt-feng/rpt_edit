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
OECD Public Governance Reviews

# Citizen Participation for Better Cohesion Policy

Insights from 11 Pilot Initiatives

![](images/6935f468737608902987a76c93413549e376cf0409f53e42909f6346f2d20f8b.jpg)

OECD Public Governance Reviews

# Citizen Participation for Better Cohesion Policy

INSIGHTS FROM 11 PILOT INITIATIVES

This work was approved and declassified by the Public Governance Committee on 21 July 2026.

This document was produced with the financial assistance of the European Union. The views expressed herein can in no way be taken to reflect the official opinion of the European Union.

This document, as well as any data and map included herein, are without prejudice to the status of or sovereignty over any territory, to the delimitation of international frontiers and boundaries and to the name of any territory, city or area.

Please cite this publication as:
OECD (2026), Citizen Participation for Better Cohesion Policy: Insights from 11 Pilot Initiatives, OECD Public Governance Reviews, OECD Publishing, Paris, https://doi.org/10.1787/6b66cff6-en.

ISBN 978-92-64-36839-2 (print)
ISBN 978-92-64-99689-2 (PDF)
ISBN 978-92-64-71242-3 (HTML)

OECD Public Governance Reviews
ISSN 2219-0406 (print)
ISSN 2219-0414 (online)

Photo credits: Cover © Drazen Zigic/Shutterstock.com.

Corrigenda to OECD publications may be found at: https://www.oecd.org/en/publications/support/corrigenda.html.
© OECD 2026

![](images/dc05b5471ced323d11185465d2e2a103477e4ece7d2bb1becacb3f30651a1ed5.jpg)

## Attribution 4.0 International (CC BY 4.0)

This work is made available under the Creative Commons Attribution 4.0 International licence. By using this work, you accept to be bound by the terms of this licence (https://creativecommons.org/licenses/by/4.0/).

Attribution – you must cite the work.

Translations – you must cite the original work, identify changes to the original and add the following text: In the event of any discrepancy between the original work and the translation, only the text of the original work should be considered valid.

Adaptations – you must cite the original work and add the following text: This is an adaptation of an original work by the OECD. The opinions expressed and arguments employed in this adaptation should not be reported as representing the official views of the OECD or of its Member countries.

Third-party material – the licence does not apply to third-party material in the work. If using such material, you are responsible for obtaining permission from the third party and for any claims of infringement.

You must not use the OECD logo, visual identity or cover image without express permission or suggest the OECD endorses your use of the work.

Any dispute arising under this licence shall be settled by arbitration in accordance with the Permanent Court of Arbitration (PCA) Arbitration Rules 2012. The seat of arbitration shall be Paris (France). The number of arbitrators shall be one.

## Foreword

Citizen participation is a strategic asset for governments to design and implement better and more effective and responsive policies while strengthening public trust. Findings from the 2023 OECD Survey on the Drivers of Trust in Public Institutions underscore the importance of political agency, which combines the confidence of being able to participate in politics and the confidence of one's voice being heard, as the strongest driver of citizens' trust in government, namely at the local level. Moreover, government currently operate in a context of wide-ranging and rapid chances that require effective and responsive actions. In this context, putting citizens at the centre of policy and decision-making allows governments to better target policies to address citizens' needs and act more efficiently, while enhancing the legitimacy and acceptability of policy decisions.

EU Cohesion Policy is the largest investment strategy of the European Union to promote the development of its Member States and regions. Its nature is rooted in the principles of effective multilevel governance and partnership with local stakeholders to ensure that investments are targeted and in line with citizens' needs and priorities. Since 2020, the OECD and the European Commission – Directorate General for Urban and Regional Policy (DG REGIO) have partnered to support EU regions and cities in improving their capacity to involve citizens and stakeholders in shaping, prioritising, and implementing EU Cohesion Policy funding instruments. A first cohort of five territories and related pilot initiatives assessed the opportunities and challenges of leveraging citizen participation processes to shape Cohesion Policy at the subnational level. Findings from the first cohort can be found in the OECD report Engaging Citizens in Cohesion Policy (2022). Since 2022, the OECD-DG REGIO collaboration has focused on designing and implementing tailored citizen participation processes in 11 territories across 7 EU Countries. The present report takes stock of this experience and showcases evidence from three deliberative processes implemented in France, Romania and Poland; one multistakeholder forum in Spain; a Student Assembly in Italy; an ‘ideathon’ in the Slovak Republic; a hybrid consultation in Romania; budget consultations in Spain, a civic monitoring exercise in Italy, and the development of tailored participatory methodologies and related capacities in Belgium and Poland.

The conclusions of this report align with the ongoing debate on the future of Cohesion Policy within EU institutions, which highlights the key role of meaningful stakeholder engagement as part of good governance and administrative capacity to enhance policy effectiveness.

# Acknowledgements

The OECD Secretariat wishes to express its gratitude to all those who contributed substantively to the preparation of this report.

This Report was prepared by the OECD Public Governance Directorate (GOV), under the leadership of Elsa Pilichowski, Director for Public Governance. It was developed under the strategic direction of Nejla Saula, Head of Division, and David Goessmann, Head of the Open Governance Unit within the Anti-Corruption, Integrity and Open Government (ACIOG) Division.

This report was drafted by Charlotte Denise-Adam, Policy Analyst, Manon Epherre-Iriart, Policy Analyst, and Giulia Cibrario, Policy Analyst. David Goessmann, Head of Unit and Raphaël Pouyé, Policy Analyst, provided strategic comments throughout the document.

This report was developed in close collaboration with the European Commission – Directorate General for Regional and Urban Policy (DG REGIO) – Unit E1: Administrative Capacity Building & Solidarity Instruments. Francesco Amodeo participated in the conceptualisation of the report. Dominika Chroszcz and Klaudia Dywel provided strategic comments on all chapters.

Project teams from the 11 EU regions and cities involved provided feedback to this report. The OECD would like to thank Magdalena Jochemczyk, Agnieszka Stroińska (GZM Metropolis, Poland), Ewa Paderewska (Centre for European Transport Projects in Poland – CEUTP), Daniela Ferrara, Anna Maria Linsalata, Raffaella Gentile (Emilia-Romagna Region, Italy), Ilaria Dallasta (Union of Municipalities of Appennino Reggiano, Italy), Massimiliano Pacifico (Lazio Region, Italy), Fabrice Saint, Mathilde Adriassens (Normandy Region, France), Barbara Szafir, Dominika Stan, Agata Woźniak (Marshal’s Office of the Silesian Voivodeship, Poland), Marta García Hospital (Cantabria Region, Spain), Xavier Mestre Rosanes (Government of Catalunya, Spain), Simona Iliescu (City of Râmnicu Vâlcea, Romania), Gilda Niculescu (South Muntania Regional Development Agency – SMRDA, Romania), Ruxandra Pavel (Dambovita County Council, Romania), Sona Karikova, Milan Hagovski (City of Banská Bystrica, Slovak Republic), Frédérique Van Nyen, and Quentin Richard (Brussels Region, Belgium).

The report also benefitted from strategic comments by Gillian Dorner, Deputy Director of the OECD Public Governance Directorate.

This report benefitted from consultation with Delegates to the Working Party on Open Government.

Neringa Gudziunaite and Valentin Py provided editorial assistance.

This report is a deliverable of the project “Innovative Implementation of the Partnership Principle in Cohesion Policy”, a collaboration between the OECD and the European Commission – DG REGIO. The OECD extends its sincere thanks to the European Commission for its financial support for this project.

## Table of contents

Foreword 3   
Acknowledgements 4   
Executive summary 7 Key findings 8   
1 Introduction: Citizen participation in Cohesion Policy 11 Setting the scene: Cohesion Policy is the main investment policy in the European Union 12 Citizen participation in Cohesion Policy 13 Cohesion Policy and the OECD-DG REGIO collaboration 15 References 18   
2 The experience of 11 pilots across seven EU countries 19 Selection of participating territories 20 The 11 OECD-DG REGIO pilots 20 Beyond individual pilots: Citizen participation as a versatile toolbox to improve Cohesion Policy at the subnational level 30 References 37   
3 Lessons learned: Well-designed participation improves policies while strengthening trust and legitimacy 39 Designing and implementing meaningful participatory processes 41 Achieving policy impact: participation can increase policy effectiveness 48 Building democratic skills and increasing public trust 50 Challenges identified through the OECD-DG REGIO pilots 52 References 55   
4 Beyond experimentation: Transforming local governance to embed meaningful participation in Cohesion Policy 57 Strengthening the preconditions that enable meaningful participation 58 Conclusion 64 Next steps: Key actions for Cohesion Policy to increase the value and impact of participation 65 References 68   
Glossary 71 Key terms on EU Cohesion Policy 71 Key terms on participation 72

References 74

## FIGURES

Figure 1.1. Pilot territories participating in the project "Innovative Implementation of the Partnership Principle in Cohesion Policy" 17

## TABLES

Table 2.1. Summary of the selected pilots for the OECD-DG REGIO project 21
Table 2.2. Participants per pilot of the OECD-DG REGIO project “Innovative Implementation of the Partnership Principle in Cohesion Policy” 31

## BOXES

Box 1.1. European Union's Cohesion Policy 12  
Box 1.2. OECD and European Commission work on Citizen Participation and Deliberation 14  
Box 2.1. Multilevel coordination and support to increase impact of participatory processes in Romania 32  
Box 2.2. Multi-staged processes can involve citizens at different stages of the policy cycle 34  
Box 3.1. OECD's Guiding Principles for Citizen Participation Processes 42  
Box 3.2. Involving people with disabilities in Poland 43  
Box 3.3. Closing the feedback loop: good practices 45  
Box 3.4. Using different media supports to increase the reach and impact of participation in Romania 47  
Box 3.5. Banská Bystrica digital democracy platform 52  
Box 4.1. A sound environment for participatory processes in Catalonia 59  
Box 4.2. Banská Bystrica digital democracy platform 61  
Box 4.3. Local resolutions to enable deliberative democracy in Romania 63

# Executive summary

This report shares insights from the 11 pilots of the project “Innovative Implementation of the Partnership Principle in EU Cohesion Policy”, a partnership between the OECD and the European Commission – Directorate General for Regional and Urban Policy (DG REGIO) which aimed at experimenting and embedding meaningful citizen participation in the management of Cohesion Policy instruments at the subnational level. Citizen participation in policymaking is identified as a key enabler to reinforce citizens’ trust in public institutions, especially at the local level, as well as a crucial government process to ensure responsive and effective policy delivery. The pilots involved local authorities and civil society organisations (CSOs) from 11 regions and cities across 7 EU countries: Belgium, France, Italy, Poland, Romania, Slovak Republic, and Spain. The OECD - DG REGIO collaboration tested tailored participatory methods in real settings to understand what works in different governance and policy contexts and identify the conditions needed to embed meaningful participation in the Cohesion Policy cycle. The pilots covered a broad range of participatory approaches and policy issues, including:

\- Three representative deliberative processes in France, Poland, and Romania. These processes brought together groups of citizens selected through stratified sortition to learn about a public issue, deliberate, and produce recommendations.

\- One multistakeholder forum in Spain, designed to involve citizens, stakeholders, experts and civil society in the design and implementation of a policy that directly affects them.

• A student assembly in Italy, adapting deliberative elements to a school environment.

\- An ‘ideathon’ in the Slovak Republic, using open innovation methods to identify and prioritise local development projects and initiatives.

\- A multistage hybrid consultation in Romania, designed to involve a wide range of citizens and stakeholders in local development programmes.

\- Budget consultations in Spain, where citizens, experts and stakeholders contributed to define the orientation of investments.

\- A civic monitoring process in Italy, enabling citizens to oversee EU Cohesion Policy-funded projects.

\- Capacity building activities in Belgium and Poland to identify meaningful opportunities for participation in the management of EU Cohesion Policy instruments while strengthening internal capacities to design and implement participatory processes tailored to their respective contexts.

## Key findings

## The pilots demonstrate that citizen participation is a versatile toolbox for Cohesion Policy

The pilots tested a wide range of participatory methodologies applied at various stages of the policy cycle, to inform a variety of policy instruments and documents related to Cohesion Policy, involving both citizens and stakeholders – including by targeting specific groups. Moreover, the pilots covered several policy areas, including transport, access to culture, territorial development and intergenerational fairness. With the support of the OECD and local CSOs, the 11 local authorities designed and implemented tailored participatory processes and ensured policy impact by establishing mechanisms to ‘close the loop’ and by leveraging public communication to provide feedback to participants and to all citizens.

## The pilots show that participation can improve policy decisions while strengthening trust and legitimacy

Citizen participation can improve Cohesion Policy by helping local authorities to better identify problems, surface bottlenecks and inefficiencies, and reveal blind spots. It does so by providing authorities with structured channels to tap into citizens' everyday life experiences as users of infrastructure and services and as participants in public life. Ultimately, policymakers can use these insights to inform decisions that better reflect territorial needs. The 11 pilots demonstrated that, when adequately designed and implemented, citizen participation processes can increase the accuracy and pertinence of policies and services. These experiences also highlighted the potential of involving citizens to increase public acceptability and legitimacy of policy decisions, all while improving public understanding of the role of the EU in fostering territorial development. Finally, participants of various pilots reported an increased sense of agency and confidence that their voice was heard by the government on decisions that mattered to them.

## The pilots also demonstrated that challenges to implementing meaningful participation persist

Throughout the implementation of the pilots, public authorities and CSOs faced several concrete challenges, including the lack of political and institutional support, which reduced the likelihood that citizen input would influence decisions, as well as limited or insufficient availability of human and financial resources. Moreover, the experience of the pilots highlighted the difficulties in coordinating participation across the multiple levels of governance that implement Cohesion Policy at the subnational level. Furthermore, citizens face barriers to engagement and might not see the value of participating. Finally, and most importantly, participation is not well integrated into the Cohesion Policy cycle; existing procedures and timelines left little space for meaningful participation, meaning that citizen contributions sometimes arrived too late to shape key choices.

## Moving forward, governments should act to embed meaningful participation in Cohesion Policy

Citizen participation is not a “nice-to-have” but a strategic imperative for the legitimacy and success of Cohesion Policy. As the EU discusses the next Multiannual Financial Framework in a context of geopolitical tensions and major transitions, facing increasing expectations for effective public spending, failing to involve citizens meaningfully in setting priorities and shaping policies carries significant political risk. The EU acknowledged meaningful citizen participation as a strategic asset to achieve better policies and strengthen democracy by making it a crucial piece of various initiatives and policy documents, including the European Democracy Shield, the Strategy for Civil Society, and the Recommendation on promoting the engagement and effective participation of citizens and civil society organisations. To embed meaningful participation in Cohesion Policy, governments at all levels should act to: (1) strengthen the preconditions to meaningful participation, including legal, policy frameworks and institutional arrangements, (2) enhance institutional capacity to build a culture of participation, (3) strengthen vertical and horizontal coordination, and (4) institutionalise and mainstream participation throughout the Cohesion Policy cycle.

Regarding the immediate next steps, the experience of the 11 pilots suggests two complementary areas of action: (1) moving from experimentation to building and embedding capacities within Managing Authorities so that participation becomes an integral part of the governance of Cohesion Policy; and (2) continuing to expand experimentation at the municipal level as laboratory for democratic innovation to ensure that EU priorities remain rooted in citizens' priorities.

## 1 Introduction: Citizen participation in Cohesion Policy

This chapter frames the collaboration between the European Commission – Di

[中间内容因长度限制已省略]

nvolved in the policy cycle and in service design and delivery”. It refers to the efforts by public institutions to hear the views, perspectives, and inputs from citizens and stakeholders. Participation allows citizens and stakeholders to influence the activities and decisions of public authorities at different stages of the policy cycle (OECD, 2022[3]). The OECD Recommendation of the Council on Open Government (OECD, 2017[4]) distinguishes among three levels of citizen and stakeholder participation, which differ according to the level of involvement:

\- Information: an initial level of participation characterised by a one-way relationship in which the government produces and delivers information to citizens and stakeholders. It covers both on-demand provision of information and “proactive” measures by the government to disseminate information.

\- Consultation: a more advanced level of participation that entails a two-way relationship in which citizens and stakeholders provide feedback to the government and vice-versa. It is based on the prior definition of the issue for which views are being sought and requires the provision of relevant information, in addition to feedback on the outcomes of the process.

\- Engagement: when citizens and stakeholders are given the opportunity and the necessary resources (e.g., information, data, and digital tools) to collaborate during all phases of the policy-cycle and in the service design and delivery. It acknowledges equal standing for citizens in setting the agenda, proposing project or policy options and shaping the dialogue – although the responsibility for the final decision or policy formulation in many cases rests with public authorities.

Citizens: Refers to the ‘inhabitants of a particular place’, which can be in reference to a village, town, city, region, state, or country depending on the context. It is not meant in the more restrictive sense of ‘legally recognised nationals of a state’. In this larger sense, it is equivalent of people/individuals.

Civic monitoring: Refers to the process of involving the public in the monitoring and evaluation of public decisions, policies, and services. This participatory method can also be considered as a vertical or social accountability tool, as it allows citizens and stakeholders to directly participate in making public authorities accountable for their decisions or actions (OECD, 2022[3]).

Consultation: A consultation is a two-way relationship in which citizens provide feedback to a public institution (such as comments, perceptions, information, advice, experiences, and ideas). Usually, governments define the issues for consultation, set the questions, and manage the process, while citizens are invited to contribute their views and opinions (OECD, 2022[3]).

Open innovation: Open innovation practices, such as crowdsourcing, hackathons, or public challenges, are a way for public authorities to tap into collective intelligence to co-create solutions for specific public issues. Open innovation is regularly inspired from business development strategies or technological development, and can be defined as “the cooperative creation of ideas and applications outside of the boundaries of any single organisation” (Seltzer and Mahmoudi, 2012[5]; OECD, 2022[3]).

Representative deliberative processes: Structured participation processes in which a broadly representative group of citizens, selected through a civic lottery, learns about a public issue, deliberates with the support of facilitators, and develops collective recommendations for decision makers. Examples include citizens' assemblies, citizens' juries, and panels. These processes allow citizens to grapple with complexity, weigh trade-offs, and find common ground. They are particularly well-suited to Cohesion Policy issues that require informed public judgment (OECD, 2022[3]).

Stakeholders: Includes any interested and/or affected party, including institutions and organisations, whether governmental or non-governmental, from civil society, academia, the media, or the private sector (OECD, 2022[3]).

## References

European Commission (2024), Forging A Sustainable Future Together: Cohesion for A Competitive and Inclusive Europe: Report of the High-Level Group on the Future of Cohesion Policy, https://doi.org/10.2776/974536.

European Commission (2025), Glossary, https://ec.europa.eu/regional\_policy/policy/what/glossary\_en.

OECD (2022), OECD Guidelines for Citizen Participation Processes, OECD Publishing, https://doi.org/10.1787/f765caf6-en.

OECD (2017), Recommendation of the Council on Open Government, https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0438.

Seltzer, E. and D. Mahmoudi (2012), “Citizen Participation, Open Innovation, and Crowdsourcing: Challenges and Opportunities for Planning”, Journal of Planning Literature, Vol. 28/1, https://doi.org/10.1177/0885412212469112.

# Citizen Participation for Better Cohesion Policy

## Insights from 11 Pilot Initiatives

This report shares insights from the 11 pilot initiatives of the project “Innovative Implementation of the Partnership Principle in EU Cohesion Policy”, a partnership between the OECD and the European Commission’s Directorate General for Regional and Urban Policy (DG REGIO). The pilots involved local authorities and civil society organisations from regions and cities across seven European Union countries: Belgium, France, Italy, Poland, Romania, the Slovak Republic, and Spain. The project tested participatory methods in real settings to understand what works in different governance and policy contexts, and identify the conditions needed to embed meaningful participation in the Cohesion Policy cycle.
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
