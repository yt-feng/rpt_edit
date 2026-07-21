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
OECD Artificial Intelligence Papers

# Artificial intelligence and personal finance

No. 62

![](images/1a2bde52725d3d1029a12a9a37b37fadb1762f218da185a6a957c90b7430af6b.jpg)

![](images/263a310bfbe3471f0b82409c99d129502acae4ddfb13187b5e6a10e2b5643f3f.jpg)

# Disclaimer

This work is issued under the responsibility of the Secretary-General of the OECD and does not necessarily reflect the official views of OECD Member countries.

This document, as well as any data and map included herein, are without prejudice to the status of or sovereignty over any territory, to the delimitation of international frontiers and boundaries and to the name of any territory, city or area.

Photo credits: © Getty Images/ AndreyPopov

© OECD 2026.

![](images/f75aa0ac32e1629a18a6544afc7a2c7c501a53892ac4ce32a1bb2dc35b8393df.jpg)

## Attribution 4.0 International (CC BY 4.0).

This work is made available under the Creative Commons Attribution 4.0 International licence. By using this work, you accept to be bound by the terms of this licence (https://creativecommons.org/licenses/by/4.0/).

Attribution – you must cite the work.

Translations – you must cite the original work, identify changes to the original and add the following text: In the event of any discrepancy between the original work and the translation, only the text of original work should be considered valid.

Adaptations – you must cite the original work and add the following text: This is an adaptation of an original work by the OECD. The opinions expressed and arguments employed in this adaptation should not be reported as representing the official views of the OECD or of its Member countries.

Third-party material – the licence does not apply to third-party material in the work. If using such material, you are responsible for obtaining permission from the third party and for any claims of infringement.

You must not use the OECD logo, visual identity or cover image without express permission or suggest the OECD endorses your use of the work.

Any dispute arising under this licence shall be settled by arbitration in accordance with the Permanent Court of Arbitration (PCA) Arbitration Rules 2012. The seat of arbitration shall be Paris (France). The number of arbitrators shall be one.

Consumers' increasing use of AI tools and AI-generated content for personal finance brings opportunities in terms of accessibility, personalisation and decision making, but it also increases risks related to bias, hallucinations, commercial influence, data privacy and exclusion, with uncertain benefits on individual long-term financial well-being.

This policy paper explores how AI tools are transforming the way consumers access and use financial information, education and advice in the management of their personal finances, and how AI tools can make financial education more personalised and accessible.

It provides financial literacy policymakers and stakeholders with an overview of current trends, highlighting key opportunities and emerging risks. Drawing on these trends and on the experiences of members of the OECD International Network on Financial Education (OECD/INFE), the paper presents financial literacy competencies that individuals should possess to benefit from these developments, both as consumers and learners, as well as policy considerations to guide the development of effective financial education responses.

This report has been developed by the Capital Markets and Financial Institutions Division of the OECD Directorate for Financial and Enterprise Affairs. It was prepared by Andrea Grifoni under the supervision of Chiara Monticone, Senior Policy Analyst, Miles Larbey, Head of the Financial Consumer Protection, Education and Inclusion Unit, and Serdar Çelik, Head of Division.

Delegates to the OECD International Network on Financial Education and to the OECD Working Party on Financial Consumer Protection, Education and Inclusion, as well as Iota Kaousar Nassr from the Division, Brigitte Acoca, Nils Adriansson and Nicholas McSpedden-Brown in the OECD Science, Technology and Innovation Directorate, and Stuart Elliot in the OECD Directorate for Education and Skills provided input.

# Executive summary

In 2025, over one third of individuals across OECD countries reported using AI tools. Increasingly, these tools are being used to support financial decision making and to learn about personal finance. Consumers turn to AI for assistance with choosing and understanding financial products, budgeting, credit management, investing, and retirement planning. They also rely on AI to access personalised financial education, sometimes asking questions they might not feel comfortable asking a human advisor.

While these developments hold significant potential to support consumers in managing their personal finances, the use of AI tools also introduces important risks. Some risks are inherent to the technology itself, including hallucinations, biases, potential commercial influence, and the blurring of boundaries between personalised financial advice and general information. Other risks arise from how consumers use AI tools, for example, relying on them to reduce cognitive effort, or acting on the advice received from AI tools without fully understanding the nature or limitations of the advice provided. These risks may lead to consumer harm, such as financial decisions that are inconsistent with individuals' needs and preferences, misuse of personal data, and new forms of digital exclusion.

AI is not a substitute for financial literacy. The use of AI tools by consumers calls for specific financial literacy competencies for their safe and informed use. Consumers need to know how to ask appropriate questions, how to critically assess personal data requests and the responses they receive. Low levels of financial, digital and AI literacy could further increase the potential for harm associated with the use of these technologies.

Although these are relatively recent developments, it is already possible to identify some key policy considerations for financial literacy policymakers and stakeholders:

\- Additional evidence is needed to understand how consumers use AI in the management of their personal finances and the implications on consumer outcomes, both positive and negative. The OECD/INFE International Survey of Adult Financial Literacy, Inclusion & Well-Being 2026 (OECD, 2026[1]) will contribute to fill this gap, as it includes questions to measure digital financial literacy as well as the use of AI for financial advice.

\- It is important to continue promoting financial literacy to empower consumers in using AI tools for personal financial management in safe and informed ways, alongside financial consumer protection measures. Possessing adequate financial literacy remains essential for individuals to retain autonomy and agency when using AI to inform financial decision making. Consumers should be able to critically assess the information they receive and decide whether to act upon it.

\- Policymakers and stakeholders should inform consumers about the opportunities and risks of using AI as a source of financial information, education and advice in their financial education initiatives. In doing so, they can build on the financial literacy competencies suggested in this paper.

\- Policymakers and stakeholders can harness AI to create effective, engaging and personalised financial information and education to support consumers in their personal financial decision making. In doing so, they should consider the importance of robust human oversight, anchoring AI tools' responses in vetted content ("grounding"), and governance models to foster the accuracy, quality and pedagogical soundness of AI-generated content.

\- Consumers with low levels of financial literacy, digital and AI literacy or limited access to AI may benefit from specific support, as well as those without access to the digital infrastructure for the use of AI. This would minimise the risks of new forms of exclusion.

## Table of contents

Foreword 3
Executive summary 4
Introduction 7
1 The use of AI to support personal financial decision making 10
1.1. Current trends in the use of AI by consumers to manage their personal finances 10
1.2. Opportunities and risks for consumers in using AI to manage personal finances 11
2 The use of AI to design and deliver financial education 20
2.1. Opportunities 20
2.2. Risks 23
3 Financial literacy competencies for the use of AI in personal finance 26
3.1. Financial literacy competencies for a safe and informed use of AI in the context of personal finance 26
4 Policy considerations 28
References 30
Annex A. The OECD AI Principles 37
Annex B. Glossary 39
Notes 41
TABLES
Table 1. Financial literacy competencies for a safe and informed use of AI in the context of personal finance 27
BOXES
Box 1. Evidence on the use of AI tools in personal finance in selected jurisdictions 11
Box 2. The use of robo-advice and financial literacy 15
Box 3. Trust in AI tools 17
Box 4. Selected examples of information campaigns about the use of AI 19
Box 5. The use of AI to support financial literacy in the classroom 22
Box 6. IOSCO TechSprint “Investor Education in the Age of Artificial Intelligence” 24
Box 7. Ensuring continued visibility of financial education content developed by public authorities 25

## Introduction

The growing availability and potential of AI tools can transform how consumers access, interpret, and act upon complex financial information, and enable more personalised and adaptive financial education that can better meet individual needs.

AI is increasingly used both in finance and education, among other domains, particularly since it became widely available to the public in late 2022 $^{1}$ following the release of consumer-accessible generative AI tools such as ChatGPT (Lorenz, Perset and Berryhill, 2023 $^{[2]}$ ). In 2025, over one-third of individuals across OECD countries used AI tools (OECD, 2026 $^{[3]}$ ).

In the financial sector, AI is used both on the supply and demand side. On the supply side, AI is embedded across a wide range of products and services, from back-office operations to customer-facing applications (OECD, 2024[4]; New Zealand Financial Market Authority, 2024[5]; OSFI-FCAC, 2024[6]). Notable examples include fraud detection, customer service and client onboarding in banking, credit underwriting, insurance underwriting and claims processing, algorithmic trading, and alternative data-based credit scoring (OECD, 2023[7]; 2024[4]; 2021[8]; Financial Stability Board, 2024[9]; European Banking Authority, 2025[10]). AI is also used by financial service providers through the use of alternative data to assess creditworthiness among individuals with limited financial histories and other underserved groups (OECD, 2021[8]; 2025[11]; CAF, 2025[12]). Other uses include the onboarding of new clients and automated support.

On the demand side, consumers increasingly use AI for financial information and advice, and AI tools have the potential to support financial decision making in areas such as budgeting, credit management and investing (OECD, 2024[4]; Empower, 2025[13]; J.D. Power, 2025[14]; TD Bank, 2025[15]; FINRA, 2024[16]; Lloyds Banking Group, 2025[17]; Jia, Eling and Wang, 2025[18]; IPSOS, 2024[19]). AI tools can also provide easier access to personalised financial education. They can extend the reach and accessibility of financial education, make it more personal, notably as a result of adaptive learning and tutoring, thereby directly supporting financial decision making (OECD, 2021[20]; Varsik and Vosberg, 2024[21]; OECD, 2026[22]). It can also offer new tools to financial literacy policymakers and stakeholders to effectively design and deliver financial education.

Together, these developments present significant opportunities to support individual financial decision making but also bring new risks for consumers (Global Financial Innovation Network, 2025[23]). As in other domains, the use of AI raises important questions about the quality of outputs, privacy, data protection, digital security, as well as equity and inclusion (Varsik and Vosberg, 2024[21]). The possible emergence of consumer detriment calls for a policy response ensuring that the use AI contributes to increasing financial well-being and does not exacerbate inequalities.

In the analysis of these phenomena and their effects on consumers and learners, it is important to note that this field is developing rapidly and that opportunities and risks will evolve, as a result of developments in AI tools and changes in the regulation and supervision of the use of AI.

In addition, it is important to recognise that many sources of evidence describing the use of AI by financial consumers are currently produced by or on behalf of financial institutions offering AI services to their customers, and that evidence on the effects of AI on consumers' financial literacy and well-being is still scarce.

## Scope

This paper explores recent developments, presents evidence and highlights the opportunities and risks related to the use of AI in personal finance. In particular:

\- Section 1 focuses on the use of AI by consumers in personal financial decision making, including through AI tools and AI-generated financial information, education and advice.

\- Section 2 focuses on financial education and on the opportunities and risks offered by AI tools in designing and delivering it.

\- Section 3 focuses on financial literacy competencies for the use of AI in personal finance, looking both at competencies for personal financial decision making with the support of AI tools and at competencies for accessing and using AI-generated financial information, education and advice.

## The paper does not address:

\- The use of AI by financial services providers in designing, marketing and selling financial products and services.

\- The provision of “regulated” personal financial advice. Most jurisdictions have regulations in place relating to the provision of personal financial advice, i.e. advice that contains specific recommendations based on an assessment of a consumer’s profile, financial needs and objectives. This paper does not discuss the extent to which regulated financial advice is affected by AI, or any policy and regulatory responses.

• The use of AI by financial fraudsters and scammers (IOSCO, 2024[24]; OECD, 2026[25]).

## Relevant OECD work

The OECD Council adopted the Recommendation on Artificial Intelligence at its Ministerial meeting in May 2019 and updated it in 2024 (OECD, 2024[26]). This Recommendation includes the OECD AI Principles (see Annex A), which are the first intergovernmental standard on AI. They promote innovative, trustworthy AI that respects human rights and democratic values. They are composed of five values-based principles and five recommendations that provide practical and flexible guidance for policymakers and AI actors.

In addition to these Principles, the following OECD standards relating to consumer finance include provisions that are relevant to the use of AI by financial consumers:

\- The G20/OECD High-Level Principles on Financial Consumer Protection (OECD, 2022[27]) (the FCP Principles), which set out the essential elements of a comprehensive and effective financial consumer protection framework, include a cross-cutting theme on digitalisation. This theme highlights the importance of addressing consumer risks stemming from the use of AI in financial markets.

\- The OECD Recommendation on Financial Literacy (OECD, 2020[28]), which presents a single, comprehensive, instrument on financial literacy, does not address AI explicitly but invites Adherents to develop appropriate tools to support learning (including digital tools) and prepare consumers to deal with the financial advice industry, including via robo-advice.

Besides these international standards, work on AI that is relevant from a consumer finance perspective is being undertaken by the following OECD bodies:

\- The OECD Committee on Financial Markets $^{2}$ has focused on supervisory approaches to AI in finance (OECD, 2026 $^{[29]}$ ) as well as on the interplay between AI and Open Finance (OECD, 2026 forthcoming $^{[30]}$ ), including the implications and avenues for the use of agentic AI in financial services.

\- The OECD Working Party on Financial Consumer Protection, Education and Inclusion $^{3}$ includes the impact, opportunities and risks of digitalisation among its strategic priorities and has held regular roundtable discussions on the use of AI in consumer financial products and services. Among other things, the Working Party will take forward work on the application of the FCP Principles to digital assets and digital financial services, including those powered by AI.

\- The OECD International Network on Financial Education (OECD/INFE) $^{4}$ is addressing AI related issues through its work on digital financial literacy, core competencies and financial literacy measurement. The OECD/INFE organised a roundtable on AI and financial education during its Technical Committee meeting in October 2025, which informed the development of this paper. The OECD/INFE also developed the Digital financial literacy core competency framework for adults in ASEAN (OECD, 2026[31]), which contains competencies related to AI in financial decision making.

\- The OECD Committee on Consumer Policy $^{5}$ developed an issues note on the consumer benefits and risks of businesses' integration of AI in consumer transactions and products. It also conducted a mapping of use of AI tools for consumer and product safety policy and enforcement activities. These include AI tools used by consumer authorities to engage with/and educate consumers, as well as AI tools consumers can use, for example for detecting fraudulent websites and unsafe products.

OECD research, analysis, tools and data on AI, across all policy domains, is released via the OECD.AI Policy Observatory. $^{6}$

# 1 The use of AI to support personal financial decision making

This section focuses on the role of AI in supporting personal financial decision making. It starts by providing evidence on the increasing use of AI by consumers for seeking personal financial information, education and advice to manage their personal finances. It then discusses opportunities and risks for consumers.

## 1.1. Current trends in the use of AI by consumers to manage their personal finances

Currently, the following AI tools are available to consumers as a source of financial information and advice and to manage their personal finances:

\- Conversational guid

[中间内容因长度限制已省略]

al tools and pursue goals over extended periods with limited human supervision. These systems are designed to operate in more open-ended, less predictable environments and often require less human supervision than individual AI agents (OECD, 2025[86]).

AI literacy: with regard to AI literacy, two definitions are proposed, one developed by the European Union in the context of its AI Act, and one for primary and secondary school students developed by the OECD and the European Union in the development of an AI literacy framework.

\- AI literacy: skills, knowledge and understanding that allow providers, deployers and affected persons, taking into account their respective rights and obligations in the context of [the AI Act], to make an informed deployment of AI systems, as well as to gain awareness about the opportunities and risks of AI and possible harm it can cause (European Union, 2024[87]).

\- AI literacy (primary and secondary school students): the technical knowledge, durable skills, and future ready attitudes required to thrive in a world influenced by AI. It enables learners to engage, create with, manage, and design AI, while critically evaluating its benefits, risks, and ethical implications (OECD/European Commission, 2026[88]).

Digital literacy: the ability to locate, evaluate, use and create information using digital tools and platforms (Forsström et al., 2025[89]).

Financial education: The process by which financial consumers/investors improve their understanding of financial products, concepts and risks and, through information, instruction and/or objective advice, develop the skills and confidence to become more aware of financial risks and opportunities, to make informed choices, to know where to go for help, and to take other effective actions to improve their financial well-being (OECD, 2012[90]).

Financial literacy: a combination of financial awareness, knowledge, skills, attitude and behaviours necessary to make sound financial decisions and ultimately achieve individual financial well-being (OECD, 2020[28]).

Financial well-being: a state in which individuals are able to smoothly manage their financial needs and obligations, can cope with negative shocks, can pursue aspirations, goals and capture opportunities, and feel satisfied and confident about their financial lives, keeping in mind country specific circumstances (OECD, 2024[91]).

Generative AI (GenAI): AI models that create new outputs (e.g., text, code, audio, images, video), often in response to prompts, based on their training data (OECD, 2023[92]).

Large language model (LLM): AI models that process, analyse, and generate natural language text or speech trained on vast amounts of data using techniques ranging from rule-based approaches to statistical models and deep learning (OECD, 2023[92]).

$^{1}$ For example, ChatGPT was launched in November 2022, Grok in November 2023, Gemini in December 2023 and Mistral Le Chat in February 2024.

2 www.oecd.org/en/topics/policy-issues/financial-markets.html

3 www.oecd.org/en/topics/policy-issues/financial-consumer-protection-education-and-inclusion.html

4 www.oecd.org/en/networks/infe.html

5 www.oecd.org/en/topics/policy-issues/consumer-policy.html

$^{6}$ oecd.ai/en/

$^{7}$ The OECD Committee on Financial Markets is addressing the implications and avenues for the use of agentic AI in financial services.

$^{8}$ Based on a survey of 2 500 adults conducted in June 2024.

$^{9}$ Based on an online survey of 2 750 adults aged 25–59 conducted from 15 July to 1 August 2025.

$^{10}$ Based on an online survey of approximately 5 000 adults conducted in July 2025.

$^{11}$ Based on an online survey of 1 009 consumers conducted in December 2024.

$^{12}$ Based on a survey of 4 000 consumers conducted in July 2025.

13 bhashini.gov.in/

$^{14}$ The OECD report “Understanding and Responding to Financial Consumer Vulnerability” (OECD, 2025 $^{[93]}$ ) presents a conceptual framework for understanding financial consumer vulnerability. It highlights that vulnerability is rooted in a mix of personal traits (consumer characteristics), personal situations (consumer circumstances), how financial markets are structured (market characteristics), and how financial service providers operate (conduct and culture of firms). It also highlights policy considerations and responses to address this issue.

$^{15}$ Examples include Google Virtual Field Trips (artsandculture.google.com/project/expeditions).

$^{16}$ Examples include Carnegie Learning's adaptive learning platform (www.carnegielearning.com/) and Khan Academy's Khanmigo (www.khanmigo.ai/).

17 www.fca.org.uk/firms/innovation/ai-lab

18 www.iosco.org/v2/training/?subsection=tech-sprint

$^{19}$ For more information please visit: www.oecd.org/en/topics/sub-issues/ai-principles.html

# Artificial intelligence and personal finance

## No. 62

Artificial intelligence (AI) is transforming how consumers access and use financial information, education and advice for personal financial decision making. While consumers' increasing use of AI tools and AI-generated content for personal finance brings opportunities in terms of accessibility, personalisation and decision making, it also increases risks related to bias, hallucinations, commercial influence, data privacy and exclusion, with uncertain benefits on long-term financial well-being. This policy paper provides policymakers and stakeholders with an overview of current trends, opportunities and risks in the use of AI in personal finance and in the design and delivery of financial education. It also proposes a set of financial literacy competencies to support the use of AI in personal financial decision making.
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
