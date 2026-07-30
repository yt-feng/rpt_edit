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

# Competition in the age of AI Initial evidence from microdata

No. 62

![](images/f0ed6ee03e0d7aa1a2bb6eb9c5f66f5822ae4604d0f4a73a207e1eec5c192ace.jpg)

OECD AI Working Papers

# Competition in the age of Al: initial evidence from microdata

# Disclaimer

This work is issued under the responsibility of the Secretary-General of the OECD and does not necessarily reflect the official views of OECD Member countries.

This document, as well as any data and map included herein, are without prejudice to the status of or sovereignty over any territory, to the delimitation of international frontiers and boundaries and to the name of any territory, city or area.

The statistical data for Israel are supplied by and under the responsibility of the relevant Israeli authorities. The use of such data by the OECD is without prejudice to the status of the Golan Heights, East Jerusalem and Israeli settlements in the West Bank under the terms of international law.

This publication contributes to the OECD's Artificial Intelligence in Work, Innovation, Productivity and Skills (AI-WIPS) programme, which provides policymakers with new evidence and analysis to keep abreast of the fast-evolving changes in AI capabilities and diffusion and their implications for the world of work. The programme aims to help ensure that adoption of AI in the world of work is effective, beneficial to all, people-centred and accepted by the population at large. AI-WIPS is supported by the German Federal Ministry of Labour and Social Affairs (BMAS) and will complement the work of the German AI Observatory in the Ministry's Policy Lab Digital, Work & Society. For more information, visit https://oecd.ai/work-innovation-productivity-skills and https://denkfabrik-bmas.de/.

![](images/33f85f4c7bcfd834389970463cbee10e3448fad90267e464f9da5ffd99353d35.jpg)

Federal Ministry of Labour and Social Affairs

Photo credits: © Kjpargeter/Shutterstock

© OECD 2026

![](images/1bf8f42530b849aa31fcaa9d1d07502f4b10a4b12e7f8088cd313832452acc9c.jpg)

## Attribution 4.0 International (CC BY 4.0)

This work is made available under the Creative Commons Attribution 4.0 International licence. By using this work, you accept to be bound by the terms of this licence (https://creativecommons.org/licenses/by/4.0/).

Attribution – you must cite the work.

Translations – you must cite the original work, identify changes to the original and add the following text: In the event of any discrepancy between the original work and the translation, only the text of the original work should be considered valid.

Adaptations – you must cite the original work and add the following text: This is an adaptation of an original work by the OECD. The opinions expressed and arguments employed in this adaptation should not be reported as representing the official views of the OECD or of its Member countries.

Third-party material – the licence does not apply to third-party material in the work. If using such material, you are responsible for obtaining permission from the third party and for any claims of infringement.

You must not use the OECD logo, visual identity or cover image without express permission or suggest the OECD endorses your use of the work.

Any dispute arising under this licence shall be settled by arbitration in accordance with the Permanent Court of Arbitration (PCA) Arbitration Rules 2012. The seat of arbitration shall be Paris (France). The number of arbitrators shall be one.

Artificial intelligence (AI) can reshape markets, yet its implications for competition remain underexplored. This paper develops a conceptual framework distinguishing AI users from developers, and generative (GenAI) from non-generative AI, showing how competitive mechanisms differ across these dimensions. Using multiple microdata sources, the analysis documents several findings. Adoption of non-GenAI is not associated with significant increases in market power. Descriptive evidence on firms' exposure to GenAI suggests opportunities for smaller firms alongside advantages for firms with stronger existing capabilities. Concentration in AI innovation is correlated with higher sales concentration. AI-related patenting is associated with faster markup growth, particularly in the ICT sector, where AI is an output. The AI start-up ecosystem is dynamic and attracts substantial venture capital, but start-ups are frequently acquired by large incumbents. Overall, the evidence points to a dynamic yet uneven landscape, underscoring the need for continued monitoring as AI diffusion progresses.

## Résumé

L'intelligence artificielle (IA) peut remodeler les marchés, mais ses implications pour la concurrence demeurent peu étudiées. Ce document élabore un cadre conceptuel distinguant les utilisateurs d'IA de ses développeurs, ainsi que l'IA générative (GenAI) de l'IA non générative, en montrant comment les mécanismes concurrentiels diffèrent selon ces dimensions. À partir de multiples sources de microdonnées, l'analyse établit plusieurs constats. L'adoption de l'IA non générative n'est pas associée à des hausses significatives du pouvoir de marché. Les données descriptives sur l'exposition des entreprises à la GenAI suggèrent des opportunités pour les petites entreprises, ainsi que des avantages pour celles dont les capacités existantes sont plus solides. La concentration de l'innovation en IA est corrélée à une concentration plus élevée des ventes. L'activité de brevetage liée à l'IA est associée à une croissance plus rapide des marges, en particulier dans le secteur des TIC, où l'IA constitue un produit. L'écosystème des start-ups en IA est dynamique et attire des capitaux-risque substantiels, mais ces start-ups sont fréquemment rachetées par de grands acteurs établis. Dans l'ensemble, les données dépeignent un paysage dynamique mais inégal, soulignant la nécessité d'un suivi continu à mesure que la diffusion de l'IA progresse.

Künstliche Intelligenz (KI) kann Märkte umgestalten, doch ihre Auswirkungen auf den Wettbewerb sind nach wie vor wenig erforscht. Die vorliegende Studie entwickelt einen konzeptionellen Rahmen, der zwischen KI-Nutzern und KI-Entwicklern sowie zwischen generativer KI (GenAI) und nicht-generativer KI differenziert, und zeigt auf, wie sich die Wettbewerbsmechanismen entlang dieser Dimensionen unterscheiden. Auf Grundlage verschiedener Mikrodatenquellen dokumentiert die Analyse mehrere Befunde. Die Einführung nicht-generativer KI geht nicht mit einem signifikanten Anstieg der Marktmacht einher. Eine deskriptive Betrachtung der Exposition von Unternehmen gegenüber GenAI deutet auf Chancen für kleinere Unternehmen sowie auf Vorteile für solche mit ausgeprägteren bestehenden Fähigkeiten hin. Die Konzentration der KI-Innovation korreliert mit einer höheren Umsatzkonzentration. KI-bezogene Patentaktivität ist mit einem rascheren Wachstum der Preisaufschläge verbunden, insbesondere im IKT-Sektor, in dem KI ein Produkt darstellt. Das Start-up-Ökosystem der KI ist dynamisch und zieht erhebliches Wagniskapital an, doch werden diese Start-ups häufig von großen etablierten Unternehmen übernommen. Insgesamt zeichnen die Ergebnisse ein dynamisches, aber uneinheitliches Bild und unterstreichen die Notwendigkeit einer fortlaufenden Beobachtung im Zuge der weiteren Verbreitung von KI.

# Acknowledgements

This report was drafted by Sara Calligaris, Flavio Calvino, Hélder Costa, Andrea Greppi and Oliviero Pallanch.

The authors would like to thank Guy Lalanne, who contributed with several insights at different stages and provided guidance throughout the project. The authors would also like to thank Sarah Liu who carried out, during her period at the OECD, initial analysis related to the subsection on AI start-ups ecosystem. The authors would also like to thank Alice Holt, Jerry Sheehan, Peter Gal, Cristiana Vitale, Luca Marcolin, Francesco Filippucci, Richard May, as well as Delegates to the OECD Working Party on Industry Analysis (WPIA) and the Committee on Industry, Innovation and Entrepreneurship (CIIE) for insightful comments, suggestions or discussions. Access to French data used in this work was made possible within a secure environment provided by CASD – Centre d'accès sécurisé aux données (Ref. 10.34724/CASD).

This publication contributes to the OECD's Artificial Intelligence in Work, Innovation, Productivity and Skills (AI-WIPS) programme, which provides policymakers with new evidence and analysis to keep abreast of the fast-evolving changes in AI capabilities and diffusion and their implications for the world of work. The programme aims to help ensure that adoption of AI in the world of work is effective, beneficial to all, people-centred and accepted by the population at large. AI-WIPS is supported by the German Federal Ministry of Labour and Social Affairs (BMAS) and will complement the work of the German AI Observatory in the Ministry's Policy Lab Digital, Work & Society. For more information, visit https://oecd.ai/work-innovation-productivity-skills and https://denkfabrik-bmas.de/.

## Table of contents

Disclaimer 2
Abstract 3
Résumé 4
Kurzfassung 5
Acknowledgements 6
Executive summary 9
Synthèse 11
Zusammenfassung 13
1 Introduction 15
2 The conceptual framework 19
Generative AI users 19
Generative AI developers 20
Non-GenAI users 21
Non-GenAI developers 22
3 Data 25
Administrative data from France and Portugal 25
Patent data 26
Firm-level financial data 27
Start-up data 27
Other data 28
4 Evidence from microdata 30
Evidence on AI use from official ICT surveys 30
Evidence on AI innovation from patent data 36
Evidence on the AI start-ups ecosystem 44
Linking the initial empirical evidence to the conceptual framework 50

5 Conclusions 52   
Endnotes 54   
References 60   
Annex A. Technical appendix 67   
Annex B. Further graphs and tables 70

## FIGURES

Figure 4.1. Ratio of the average market share of AI users to non-users: France and Portugal 31  
Figure 4.2. Markups growth rate for Users and Non-users of AI 33  
Figure 4.3. Trends of concentration in AI patenting activity 37  
Figure 4.4. Country share of AI inventions 38  
Figure 4.5. Market and AI-related patenting concentration 40  
Figure 4.6. Transition matrix of Top 4 firms in terms of yearly inventions. 42  
Figure 4.7. Average markup trend 43  
Figure 4.8. Number and share of and GenAI and non-GenAI start-ups by foundation year 45  
Figure 4.9. VC funding by year across types of start-ups 46

Figure A B.1. Country share 70  
Figure A B.2. Distributions of patenting concentration 71  
Figure A B.3. Markups of AI patentees across AI intensity taxonomy 72  
Figure A B.4. AI switchers 73  
Figure A B.5. Total VC funding to GenAI start-ups by region 73

## TABLES

Table 2.1. A proposed conceptual framework 24  
Table 4.1. Firm's market share decile and AI use: France and Portugal 32  
Table 4.2. Changes in firm's position in the market share distribution and AI use: France and Portugal 33  
Table 4.3. Growth in firm's markup and AI use: France and Portugal 34  
Table 4.4. Firm's characteristics by generative AI quintile - Portugal 35  
Table 4.5. Market concentration and patenting concentration 41  
Table 4.6. AI patenting and firms' markups 44  
Table 4.7. Determinants of Total VC funding raised by start-ups 47  
Table 4.8. Determinants of start-up acquisition 49

# Executive summary

AI has the potential to become a general-purpose technology, radically reshaping how firms organise production and compete. While a growing body of research analyses AI adoption and its impacts on productivity and labour markets, the relationship between AI and competition – especially beyond the foundation models market – remains largely unexplored. This report bridges this gap by outlining a novel conceptual framework and providing initial empirical evidence on the links between AI use, AI development and competition.

The proposed conceptual framework distinguishes between AI users (firms leveraging AI in their processes) and AI developers (firms building AI systems) and further differentiates between generative AI (GenAI) and non-generative AI (non-GenAI). These two distinctions are crucial, as actors' economic characteristics and competition concerns vary significantly. For instance, the development of foundation models is characterised by high fixed costs and economies of scale, which may undermine competition in the long run. The downstream use of these models is widely accessible to firms, creating potential for disruption via market entry. However, advantages in the ability to use them effectively might also strengthen the position of incumbents.

Empirically, the analysis focuses on competition dynamics beyond the foundation models and AI-inputs markets. It leverages a rich set of cross-country microdata, including official firm-level ICT surveys for France and Portugal, linked employer-employee data (LEED) for Portugal, alongside global AI-related patent filings and start-up data, documenting several key findings:

1. On average over the period analysed (2011-2022), focusing on France and Portugal, the use of non-GenAI does not appear associated with a systematic increase in proxies of market power. In particular, while AI adopters are generally larger and more productive, their markups are not substantially higher than those of non-users.

2. Combining occupational data at firm level with occupation-level measures of AI exposure allows the computation of a firm-specific indicator of AI exposure which – interpreted as a proxy for AI's potential adoption – suggests that GenAI can offer opportunities for smaller and younger firms to enter the market and challenge incumbents. However, the benefits of GenAI appear more easily unlocked by firms with higher existing capabilities, such as human capital and complementary assets, posing a risk of widening productivity gaps.

3. Focusing more closely on development, without distinguishing between GenAI and non-GenAI, patent data uncover a positive correlation between concentration in AI innovation and market concentration. Concentration in AI innovation is computed as the share of AI patents accounted for by the 4 largest patentees relative to the total number of AI patents in each year, while market concentration is defined at the level of a 3-digit industry, the geographic scope of competition (domestic, European, or global), and year. The development of the technology currently mirrors existing heterogeneities among firms, potentially entrenching the advantages of established leaders. Furthermore, in ICT sectors, firms with an AI-related patent exhibit higher markup growth, suggesting that owning AI technology may contribute to market power, but only in those sectors where AI is an output rather than an input.

4. The AI entrepreneurial ecosystem remains highly dynamic, characterised by sustained entry and significant venture capital investments, particularly in GenAI. However, this is accompanied by intense acquisition activity by large incumbents. While acquisitions can favour entry of start-ups in the market, facilitate their exit, and transfer technology, they also raise concerns about potential “killer acquisitions” that may stifle future innovation and growth prospects.

Overall, the early empirical evidence documented presents a mixed picture. The current ecosystem displays signs of both dynamism and potential emerging concentration risks. However, as AI diffusion is still in its early stages (20.2% of OECD enterprises in 2025, according to OECD ICT usage data), it may take time before competition dynamics become fully observable. These findings underscore the need for continuous and vigilant monitoring of AI markets to ensure that the technology fosters innovation and contestability, rather than consolidating dominance. Finally, the report highlights the need for more comprehensive data collection on AI use and development, which is crucial for effectively monitoring the relationship between AI and competition.

L'IA pourrait devenir une technologie à usage général, transformant radicalement la manière dont les entreprises organisent leur production et se font concurrence. Si un nombre croissant de travaux analysent l'adoption de l'IA et ses effets sur la productivité et le marché du travail, la relation entre l'IA et la concurrence – en particulier au-delà du marché des modèles de fondation – demeure largement inexporée. Ce rapport comble cette lacune en exposant un cadre conceptuel inédit et en fournissant des données empiriques initiales sur les liens entre l'utilisation de l'IA, son développement et la concurrence.

Le cadre conceptuel proposé distingue les utilisateurs d'IA (entreprises qui mobilisent l'IA dans leurs processus) des développeurs d'IA (entreprises qui conçoivent des systèmes d'IA), et différencie en outre l'IA générative (GenAI) de l'IA non générative (non-GenAI). Ces deux distinctions sont essentielles, car les caractéristiques économiques des acteurs et les préoccupations en matière de concurrence varient sensiblement. Ainsi, le développement des modèles de fondation se caractérise par des coûts fixes élevés et des économies d'échelle, qui pourraient nuire à la concurrence à long terme. L'utilisation en aval de ces modèles est largement accessible aux entreprises, ce qui crée des opportunités d'entrée sur le marché pour de nouveaux acteurs. Toutefois, les avantages liés à la capacité de les utiliser efficacement pourraient également renforcer la position des acteurs établis.

Sur le plan empirique, l'analyse porte sur les dynamiques concurrentielles au-delà des marchés des modèles de fondation et des intrants de l'IA. Elle s'appuie sur un riche ensemble de microdonnées multi-pays, dont les enquêtes officielles sur les TIC au niveau des entreprises en France et au Portugal, des données employeurs-salariés appariées (LEED) pour le Portugal, ainsi que des dépôts mondiaux de brevets liés à l'IA et des données sur les start-ups. L'analyse fait ressortir plusieurs constats principaux:

5. En moyenne sur la période analysée (2011-2022), en France et au Portugal, l'utilisation de l'IA non générative ne semble pas associée à une augmentation systématique des indicateurs indirects du pouvoir de marché. En particulier, si les entreprises adoptantes sont généralement plus grandes et plus productives, leurs marges ne sont pas sensiblement supérieures à celles des non-utilisatrices.

6. La combinaison de données professionnelles au niveau des entreprises avec des mesures d'exposition à l'IA par profession permet de calculer un indicateur d'exposition à l'IA propre à chaque entreprise, qui peut être interprété co

[中间内容因长度限制已省略]

ef060c728a2939fca259ba146c6df588462d411192a5c7cba72f.jpg)

![](images/f3d855f1e5ac178442af23d9f542b5da0ac62a56dd7b14e9d549f6d0738cdde4.jpg)  
Note: In Panel A, the lines represent the AI-related patent concentration ratio, calculated as the share of patents associated respectively, the largest single one (CR1, blue), the top 4 (CR4, red), the top 20 (CR20, green), and the top 100 (CR100, yellow). In Panel B, the bars represent the growth rate, between 2001 and 2021, of each indicator of Panel A. The graphs are based on Patents of Invention applications filed under the Patent Cooperation Treaty, contained in PATSTAT, and associated with the AI tag developed by OECD (2025[60]). Source: OECD calculations based on PATSTAT Global and Moody's Orbis.

Figure A B.2. Distributions of patenting concentration  
![](images/da16fd8b2dea7783fff35e07bd93d32712508f71e946a4e85cdcd0614435f5d4.jpg)

Note: The two histograms represent the distribution, across markets (industry-geographical region pairs) of two variables capturing concentration in patenting activity. The red histogram represents the share of AI-related inventions associated to the largest business groups in terms of patents (patent leaders in short). The blue one represents the share of AI-related inventions owned by the largest business groups in terms of sales (patents to market leader in short). This sample includes 15 industries (mostly from Manufacture of basic pharmaceutical products; Manufacture of computer, electronic and optical products; Professional, scientific, and technical activities) over the years 2000-2019. Each industry is classified either as domestic, European, or global, according to the taxonomy by Calligaris et al., (2024[66]). The countries included in the sample are Denmark, Finland, France, Germany, Greece, Hungary, Italy, Norway, Poland, Portugal, Slovenia, Spain, Sweden, and the United Kingdom for the domestic and European buckets, while in the global one also Japan, Korea, and the United States are included. Source: OECD calculations based on PATSTAT Global and Moody's Orbis.

## Markups

Figure A B.3. Markups of AI patentees across AI intensity taxonomy  
![](images/40448b27bf5dbab793e852684ad55843ca076d65d7f18d4424c62b7bb8f21661.jpg)

![](images/64eb922db4ee3d45896c40ae51a0fc50943dcf4348cec0d7b1aac6b02711d34f.jpg)

Note: The lines in the figure represent the growth rate of average markups across two groups of firms. The blue line is based on a sample of patenting firms (non AI-related), while the red one is based on firms associated with at least one AI-related invention, and only for the years after the first AI-related invention. The sample is further split into sectors considered as broadly related with ICT (Manufacture of computer, electronic and optical products (26), Publishing, audiovisual and broadcasting activities (58 to 60), Telecommunications (61), IT and other information services and (62 to 63), Panel B) and other sectors. Countries included in the sample are Austria, Belgium, Czech Republic, Denmark, Estonia, Finland, France, Germany, Hungary, Ireland, Italy, Latvia, Luxembourg, the Netherlands, Poland, Portugal, Slovakia, Slovenia, Spain, Sweden, and the United Kingdom.

Source: OECD calculations based on PATSTAT Global and Moody's Orbis.

Figure A B.4. AI switchers  
![](images/4e4f64ecbda9a76b9c28b82df55caf03cfa896c592c5cfd97b99fd40242ce4e0.jpg)  
Note: The figure represents the number of firms in the sample (having data for both markups and inventions) that each year are associated for the first time with an AI-related invention. Countries included in the sample are Austria, Belgium, Czech Republic, Denmark, Estonia, Finland, France, Germany, Hungary, Ireland, Italy, Latvia, Luxembourg, the Netherlands, Poland, Portugal, Slovakia, Slovenia, Spain, Sweden, and the United Kingdom.

Source: OECD calculations based on PATSTAT Global and Moody's Orbis.

## AI start-up ecosystem – further results

Figure A B.5. Total VC funding to GenAI start-ups by region  
![](images/f80184350b3f5279706e656d46159d57bac5f7ab5de8f6daa64951aa2050c5ab.jpg)  
Note: The figure reports the amount of VC equity financing expressed in USD billions channelled to GenAI start-ups in the OECD start-up database. EU includes the 27 member countries of the European Union, OECD includes other OECD member countries excluding EU countries and the US, reported on their own. Rest world includes countries not included in the categories mentioned above.
Source: OECD calculations based on OECD Start-ups Database.

# Competition in the age of AI

Initial evidence from microdata

## No. 62

Artificial intelligence (AI) can reshape markets, yet its implications for competition remain underexplored. This paper develops a conceptual framework distinguishing AI users from developers, and generative (GenAI) from non-generative AI, showing how competitive mechanisms differ across these dimensions. Using multiple microdata sources, the analysis documents several findings. Adoption of non-GenAI is not associated with significant increases in market power. Descriptive evidence on firms' exposure to GenAI suggests opportunities for smaller firms alongside advantages for firms with stronger existing capabilities. Concentration in AI innovation is correlated with higher sales concentration. AI-related patenting is associated with faster markup growth, particularly in the ICT sector, where AI is an output. The AI start-up ecosystem is dynamic and attracts substantial venture capital, but start-ups are frequently acquired by large incumbents. Overall, the evidence points to a dynamic yet uneven landscape, underscoring the need for continued monitoring as AI diffusion progresses.
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
