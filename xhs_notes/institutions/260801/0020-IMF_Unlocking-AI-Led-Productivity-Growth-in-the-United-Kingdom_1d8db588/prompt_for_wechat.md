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
- 已识别机构名：`IMF`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份IMF研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Unlocking AI-Led Productivity Growth in the United Kingdom

Matthieu Bellon, Pragyan Deb, Mahika Gandhi and Emma Rockall

SIP/2026/072

IMF Selected Issues Papers are prepared by IMF staff as background documentation for periodic consultations with member countries. It is based on the information available at the time it was completed on June 24, 2026. This paper is also published separately as IMF Country Report No 26/173.

2026
JUL

# IMF Selected Issues Paper European Department

# Unlocking AI-Led Productivity Growth in the United Kingdom Prepared by Matthieu Bellon, Pragyan Deb, Mahika Gandhi, and Emma Rockall

Authorized for distribution by Romain Duval
July 2026

IMF Selected Issues Papers are prepared by IMF staff as background documentation for periodic consultations with member countries. It is based on the information available at the time it was completed on June 24, 2026. This paper is also published separately as IMF Country Report No 26/173.

ABSTRACT: AI offers a significant opportunity to lift the UK's lackluster productivity growth. The UK is well positioned, given its concentration in high-skill, knowledge-intensive services where AI shows the greatest potential. Realizing these gains hinges on five enabling conditions—infrastructure, financing, regulation, skills, and trade openness—with bottlenecks identified in each. Economy-wide reforms are a prerequisite but should be complemented by targeted interventions in regulation and skills. A model of endogenous technology adoption calibrated to the UK finds that halving regulatory constraints and expanding AI-related skills supply could jointly increase output gains by two thirds. Investment in sovereign AI capabilities carries substantial insurance value against supply-chain disruptions.

RECOMMENDED CITATION: Bellon, Matthieu, Pragyan Deb, Mahika Gandhi, and Emma Rockall. "Unlocking AI-Led Productivity Growth in the United Kingdom." IMF Selected Issues Paper 26/072.

<table><tr><td>JEL Classification Numbers:</td><td>O33, O38, J24, E17</td></tr><tr><td>Keywords:</td><td>Artificial intelligence, productivity, United Kingdom.</td></tr><tr><td>Author&#x27;s E-Mail Address:</td><td>MBellon@imf.org; PDeb@imf.org; MGandhi2@imf.org; ERockall@imf.org</td></tr></table>

SELECTED ISSUES PAPERS

# Unlocking AI-Led Productivity Growth in the United Kingdom

United Kingdom

Prepared by Matthieu Bellon, Pragyan Deb, Mahika Gandhi and Emma Rockall

UNLOCKING AI-LED PRODUCTIVITY GROWTH IN THE UNITED KINGDOM \_\_\_\_ 3
A. Introduction \_\_\_\_ 3
B. Potential of AI for UK Productivity and Growth \_\_\_\_ 4
C. Bottlenecks to AI Development and Diffusion \_\_\_\_ 7
D. Policies for Lifting the Bottlenecks: Economy-Wide vs Targeted Policies \_\_\_\_ 16
E. Quantifying the Benefits of Targeted AI Policy Interventions \_\_\_\_ 23
F. Conclusion \_\_\_\_ 31

# UNITED KINGDOM

SELECTED ISSUES

July 2026

## Approved By

European Department

Prepared By Matthieu Bellon, Pragyan Deb, Mahika Gandhi (all EUR), and Emma Rockall (RES)

## CONTENTS

## BOXES

1. AI Adoption Over Time and Across Countries \_\_\_\_ 8

2. The Government's AI Strategy \_\_\_\_ 20

## FIGURES

1. Model Determinants of AI 's Potential Gains \_\_\_\_ 5

2. Workforce AI Exposure 6

3. AI Adoption \_\_\_\_ 9

4. ICT and Energy Infrastructure \_\_\_\_ 11

5. Financing of Innovation 13

6. Skills 15

7. Trade 16

8. Economy-Wide vs Targeted Policies to Ease Bottlenecks 17

9. Baseline Productivity Impacts of AI 25

10. Productivity Impacts of Regulatory Reforms 26

11. Productivity Impacts of Increasing AI Skills \_\_\_\_ 28

12. Comparison Between Regulatory Reform and Skills Investment \_\_\_\_ 28

13. Productivity Impacts of Access Barriers and Domestic Alternative \_\_\_\_ 30

## TABLE

1. AI Policy Reform: Summary of Productivity Impacts 29
ANNEXES
I. Lessons from the ICT Revolution 33
II. Drivers of Business Adoption of AI Across Countries 35
III. Details on AI Policy Intervention Scenarios 37
References 42

# UNLOCKING AI-LED PRODUCTIVITY GROWTH IN THE UNITED KINGDOM $^{1}$

AI technologies offer a significant opportunity to lift the UK's lackluster productivity growth. The UK is well positioned to benefit, given its concentration in high-skill and knowledge-intensive services where AI is showing the greatest potential for productivity gains. However, the full realization of these gains hinges on a set of conditions—appropriate infrastructure, financing for innovation, enabling regulation, appropriate skills, and trade openness—and the paper identifies bottlenecks in each area. Although economy-wide reforms to planning, energy markets, and scale-up financing envisaged under the authorities' "growth mission" are a fundamental pre-requisite for the development and adoption of AI, they should be complemented by more targeted (AI-specific) interventions in regulation, skills, and supply-chain resilience to address market failures. Using a model of endogenous technology adoption calibrated to the UK, the paper finds that halving regulatory constraints and expanding the supply of AI-related skills could jointly increase the output gains from AI by two thirds over the baseline. The government's AI strategy encompasses the right areas, but greater priority could be given to clarifying the regulatory framework and expanding the supply of the skills necessary for effective AI adoption, which our analysis suggests are the most pressing constraints. Investment in the domestic AI ecosystem also carries substantial insurance value, as even moderate disruptions to foreign model access could generate large output losses.

## A. Introduction

1. UK growth has decelerated markedly over the past two decades, with trend productivity weakening relative to peers. Production function decompositions suggest that the UK's slowdown has been driven primarily by weaker total factor productivity (TFP) growth, with subdued capital deepening also contributing (Indraccolo 2025; Goodridge and Haskel, 2022). Looking forward, additional headwinds (aging, migration slowdown, and a depreciated capital stock) may dampen the growth outlook.

2. Artificial intelligence (AI) is widely seen as a transformative opportunity to boost TFP growth in advanced economies. AI has the potential to boost TFP growth by automating tasks, improving process efficiency, accelerating innovation, and enabling new products and business models (Bailey, 2026). Like in past general-purpose technology revolutions—including the Information and Communication Technology (ICT) revolution—economy-wide productivity gains from the rise of AI are expected to be driven by effective AI adoption and to primarily come from AI-using sectors (see Annex I on the lessons from the past ICT revolution).

3. Against this background, the paper assesses the conditions under which the UK could realize AI's productivity potential. The analysis focuses on five enabling conditions—appropriate infrastructure (including but not limited to ICT and energy infrastructure), the financing of innovation, supportive regulation, skills, and resilience through trade openness—that have been highlighted as essential for technology diffusion in general, and for effective AI adoption in particular (Comin and Hobijn, 2010; Cazzaniga and others, 2024). The paper uses these as an organizing framework. It first establishes the rationale behind these factors and why they are considered most critical; then it identifies what constraints may exist in the UK in these areas; finally, it assesses whether public policies have a role in addressing them, and whether current ones are adequately designed.

4. The paper is organized in five main sections. It first reviews the literature quantifying the potential impact of AI on advanced economies' growth—with a focus on the main channels through which AI can raise TFP—and benchmarking the UK's potential relative to peers (Section B). Second, Section C draws from the literature and empirical findings to propose a framework to identify constraints to AI development and identify the main bottlenecks in the UK. Third, Section D discusses the role of economy-wide versus more targeted policies, and in particular the extent to which the UK authorities' AI strategy may address the bottlenecks identified in the previous section. Fourth, Section E conducts policy simulations to quantitatively assess the effects of targeted policies by leveraging a model of AI adoption calibrated to the UK economy. Section F concludes by highlighting areas where additional policy measures may be beneficial.

## B. Potential of AI for UK Productivity and Growth

Estimates of aggregate TFP gains from AI vary widely across studies. Differences across estimates highlight that these gains depend on assumptions about the share of tasks that are exposed to AI, the average productivity gain per task, and cost-savings opportunities from AI adoption. The UK is well positioned to benefit from AI because (1) a large share of its workforce is in occupations exposed to AI, and (2) its most important sectors are those with the greatest potential for AI-driven productivity gains and cost savings from substituting hours of labor with AI services.

## A Wide Range of Estimates in the Literature

5. The potential impact of AI on economic growth remains a highly debated topic and is marked by significant uncertainty. While empirical estimates are emerging at the micro level (see Misch and others, 2025, for a review), most studies of the macroeconomic effects on productivity remain essentially theoretical or focus on the labor market. Academic studies, private-sector analyses, and work by the Fund estimate a medium-term impact on aggregate TFP level ranging from below 1 to 35 percent over a decade (Briggs and others, 2023; Acemoglu 2024; Aghion and Bunel, 2024; IMF 2024; Filippucci and others, 2024; Filippucci and others, 2025; Cerutti and others, 2025; Misch and others, 2025; Bontadini and others, 2025).

6. Model estimates of aggregate AI gains typically rely on two determinants – the first one being the share of tasks that can legally or technically be automated and performed with AI (Figure 1). This share reflects both assumptions about the scope and capabilities of AI applications and the extent to which regulation can constrain AI use. A job is exposed to AI if the technology can be used for certain tasks and if regulation (licensing and training requirements, data privacy frameworks etc.) allows for its deployment. $^{2}$ Studies find that AI could support the performance of between 23 to 80 percent of tasks, illustrating the wide range of potential AI applications (Aghion and Bunel, 2024). $^{3}$

![](images/190ecab211e5991b2de26529718140b0a0e1ae6e52a530c06ee266a7edcb8e26.jpg)

7. Then, the economic potential of automating tasks with AI depends on the average productivity gain and cost savings across AI-exposed tasks (second circle in Figure 1). Within the AI-exposed tasks, it is also important that tasks see their productivity increase through AI adoption. Micro-economic studies of AI task-level performance suggest that productivity could improve by between 15 and 55 percent (Brynjolfsson and others, 2023; Peng and others, 2023). Many factors affect these productivity gains. In particular, it depends on the extent of cost savings from capital-labor substitution as AI adoption implies the performance of tasks by AI models supported by capital –computers, data centers, and software—instead of workers. Therefore, countries with relatively high wages can benefit more from AI (Misch and others, 2025).

Source: Pizzinelli and others (2023). High Exposure, High Complementarity are jobs highly exposed to AI and can be enhanced by it such as professionals and managers. High Exposure, Low Complementarity are jobs exposed to AI where substitution risk is higher such as administrative and clerical roles.

8. On both counts, current estimates of AI's economic potential could prove conservative as AI could accelerate the innovation process. AI capabilities and the associated productivity gains are still evolving, as the underlying innovation process remains rapid and dynamic. Continued innovation –both in fundamental models and in the complementary layers that support deployment (software, work organization)—will be crucial to expanding AI's potential. Furthermore, AI adoption can have positive feedback effects on the innovation process itself and accelerate innovation by automating the production of ideas and new technologies (see Aghion and Bunel, 2024 for examples; Bontadini and others, 2025).

## Application to the United Kingdom

9. The UK economy compares favorably with peers across the two dimensions of Figure 1 and is therefore well positioned to benefit from AI. Misch and others (2025) estimates that the UK's TFP gains could range from 0.1 to 0.5 percent per year in the medium term, clearly above the average of European countries and on par with estimated US gains. These above-average gains stem from the UK's sectoral and labor characteristics which have positive implications for the two determinants of AI potential.

10. First, the UK's workforce is employed in tasks that are both highly exposed and complementary to AI. With roughly 36 percent of the workforce holding a college degree and nearly two-thirds employed in AI-exposed occupations, the country is well placed to capture substantial growth gains (Pizzinelli and others, 2023; Bick and others, 2025). Furthermore, more than half of these workers are in high complementary occupations –where AI can improve the productivity of existing workers rather than replace them—which suggests that disruption risks are limited for many occupations (Figure 2).

Figure 2. Workforce AI Exposure  
![](images/13df966483917d72ab427469662109085d38dcb2c5f9ce7a32fa744f6504b06e.jpg)

11. Second, the UK's economic structure and past experience with technologies suggest it could benefit from large productivity gains and cost savings per exposed task on average. During the ICT revolution, the UK stood out among European countries as more capable of reaping productivity gains from the new technologies (Annex I). Furthermore, occupations that have been identified as those likely to experience the largest productivity gains from AI (in business services, finance, IT, pharma) happen to be prevalent in UK's key sectors (Filippucci and others, 2024). These occupations are dominated by cognitive, knowledge-intensive, and analytical tasks — precisely the activities where current generative AI and LLMs demonstrate the largest micro-level performance gains. Furthermore, various measures of labor costs place the UK above the OECD average (OECD, 2025). As a result, UK businesses have relatively more to gain from using AI to reduce labor costs and/or to increase worker productivity.

## C. Bottlenecks to AI Development and Diffusion

This section identifies bottlenecks that could impede the realization of potential AI gains on the basis of a simple stylized framework. We examine five AI-enabling conditions and investigate how the UK performs across these conditions, drawing from surveys and independent assessments. The analysis identifies a few bottlenecks— barriers to the construction of ICT and energy infrastructure, constraints on business scale-up, regulation uncertainty, shortages of AI-relevant skills, and more speculatively, trade and geo-fragmentation risks to the sourcing of critical inputs which could constrain AI diffusion in the future.

12. Delivering the AI-driven productivity gains depends on key enabling conditions—infrastructure, innovation, regulation, skills, and resilience through trade openness. This simplified framework leaves out other, less critical, conditions supporting AI development and adoption, but these five general “enablers” are generally seen as essential for productivity—enhancing technology diffusion in general (Comin and Hobijn, 2010), and for effective AI adoption in particular (see the AI preparedness index in Cazzaniga and others, 2024).

\- Infrastructure (both ICT and energy), skills, and trade openness are important enabling conditions for AI adoption. Econometric analysis of cross-country adoption rates confirms that these enabling conditions are meaningful drivers of AI adoption (Box 1 and Annex II). According to a variance decomposition of adoption rates, AI-relevant skills are the most important driver, followed by infrastructure and openness (see third panel in Figure 3). Beyond ICT infrastructure, energy prices –and by extension energy infrastructure—also matter (Annex II). These findings are consistent with prior empirical work highlighting the importance of skills and both ICT and energy infrastructure (Haag 2025; Misch and others, 2025).

\- Surveys emphasize the relevance of two additional enabling conditions. Many businesses cite regulatory framework and access to financing as key factors shaping the pace of AI adoption and innovation (fourth and fifth panels in Figure 3) (DSIT 2024; DBT and DSIT, 2025; TechNation 2025).

13. We use this simple framework to identify possible bottlenecks impeding the realization of AI productivity gains. We do so by examining trends, benchmarking the UK versus peers across indexes, studying responses from business surveys, and leveraging independent assessments. Specifically, we consider (1) whether appropriate infrastructure is in place to support AI deployment at scale; (2) whether financing is available for product and business-model innovation—especially for high-growth-potential firms; (3) whether regulation provides an enabling and predictable environment facilitating investment in organizational and process transformations while safeguarding trust; (4) whether a critical mass of skilled workers are available to drive adoption and innovation, ensuring effective use within firms; and (5) whether openness to trade supports access to frontier inputs (on the import side) and expands market opportunities for UK exporters of AI-enabled goods and services, thereby increasing expected returns to effective adoption.

## Box 1. United Kingdom: AI Adoption Over Time and Across Countries

AI adoption rates by businesses in the UK are high and growing fast. Surveys asking businesses whether they use AI to yield only rough proxies for the extent of effective AI adoption but are nevertheless informative of cross-country differences and trends. As of mid-2025, business surveys indicate that the AI adoption rate in the UK equaled 34 percent, close to the EU average of 37 percent and the US rate of 36 percent (first panel of Figure 3). $^{1}$ As elsewhere in the wor

[中间内容因长度限制已省略]

aumotte, F., Kim, J., Koll, D., Li, E., Li, L., Melina, G., Song, A. and Tavares, M.M., 2026. "Bridging Skill Gaps for the Future: New Jobs Creation in the AI Age." IMF Staff Discussion Note SDN/2026/001. https://doi.org/10.5089/9798229028196.006

Jorgenson, D.W., 2001. "Information Technology and the U.S. Economy." American Economic Review, 91(1), 1–32. https://doi.org/10.1257/aer.91.1.1

Jorgenson, D.W., Ho, M.S. and Stiroh, K.J., 2008. "A Retrospective Look at the U.S. Productivity Growth Resurgence." Journal of Economic Perspectives, 22(1), 3–24. https://doi.org/10.1257/jep.22.1.3

Martin, J., 2025. "The UK Productivity Slowdown: A Review of Timing, Magnitude, and Drivers." International Productivity Monitor, 48 (Spring), 29–62. https://www.csls.ca/ipm/48/Martin\_Final.pdf

McLean, A. and Smith, D., 2025. Technology Adoption Review 2025.
https://assets.publishing.service.gov.uk/media/6857e0995225e4ed0bf3ceb5/dsit\_technology\_adoption\_review\_web.pdf

Microsoft and Public First, 2025. Unlocking the UK's AI Potential: Harnessing AI for Economic Growth. https://microsoftuk.publicfirst.co.uk/uploads/Unlocking\_the\_UKs\_AI\_Potential.pdf

Misch, F., Park, B., Pizzinelli, C. and Sher, G., 2025. "AI and Productivity in Europe." IMF Working Paper 2025/067. https://doi.org/10.5089/9798229006057.001

Moll, B., Rachel, L. and Restrepo, P., 2022. "Uneven Growth: Automation's Impact on Income and Wealth Inequality." Econometrica, 90(6), 2645–2683. https://doi.org/10.3982/ECTA19417

NewMind AI, 2025. "AI Policy and Regulations of United Kingdom." NewMind AI Journal Country Report. https://www.newmind.ai/NewMind%20AI%20Journal%20Country%20Report-AI%20Policy%20and%20Regulations%20of%20United%20Kingdom.pdf

Nguyen, N. and Coyle, D., 2025. "Start-ups and Scale-ups in UK Technology Sectors." Bennett School for Public Policy, University of Cambridge. https://doi.org/10.17863/CAM.121131

Noy, S. and Zhang, W., 2023. "Experimental Evidence on the Productivity Effects of Generative Artificial Intelligence." Science, 381, 187–192. https://doi.org/10.1126/science.adh2586

OECD, 2025. Taxing Wages 2025: Decomposition of Personal Income Taxes and the Role of Tax Reliefs. https://doi.org/10.1787/b3a95829-en

OECD, 2026. "OECD Overall R&D Growth Stable; Government R&D Budgets Decline and Reorient towards Defence." OECD Statistical Release, March 2026.

https://www.oecd.org/en/data/insights/statistical-releases/2026/03/oecd-overall-rd-growth-stable-government-rd-budgets-decline-and-reorient-towards-defence.html

Oliner, S.D., Sichel, D.E. and Stiroh, K.J., 2008. "Explaining a Productive Decade." Brookings Papers on Economic Activity, 2007(1), 81–152. https://doi.org/10.1353/eca.2007.0019

Oliveira-Cunha, J., Serra-Lorenzo, B. and Valero, A., 2024. "What an LSE-CBI Survey Found about AI Adoption in UK Firms." LSE Business Review Blog.
https://blogs.lse.ac.uk/businessreview/2024/07/02/what-an-lse-cbi-survey-found-about-ai-adoption-in-uk-firms/

Parry, C., 2025. "Start-up Financing, Entry and Innovation", unpublished working paper. https://cparry96.github.io/website/parry\_jmp.pdf

Peng, S., Kalliamvakou, E., Cihon, P. and Demirer, M., 2023. "The Impact of AI on Developer Productivity: Evidence from GitHub Copilot." arXiv preprint arXiv:2302.06590. https://arxiv.org/abs/2302.06590

Pierdomenico, G., 2026. "AI in Europe: Modest Near-Term Lift, Meaningful Long-Term Gain." Goldman Sachs European Economics Analyst, 21 January 2026.

Pizzinelli, C., Panton, A.J., Tavares, M.M., Cazzaniga, M. and Li, L., 2023. "Labor Market Exposure to AI: Cross-Country Differences and Distributional Implications." IMF Working Paper 2023/216. https://doi.org/10.5089/9798400254802.001

PwC, 2025. Global Compliance Survey 2025. https://www.pwc.com/gx/en/issues/risk-regulation/pwc-global-compliance-study-2025.pdf

Resolution Foundation, 2025. Mountain Climbing: Making Progress on the UK's Growth Policy Challenge. https://www.resolutionfoundation.org/publications/mountain-climbing/

Rockall, E.J., Tavares, M.M. and Pizzinelli, C., 2025. "AI Adoption and Inequality." IMF Working Paper 2025/068. https://doi.org/10.5089/9798229006828.001

Stanford Institute for Human-Centered Artificial Intelligence (HAI), 2025. Artificial Intelligence Index Report 2025. Stanford University. https://hai.stanford.edu/ai-index/2025-ai-index-report

TechNation, 2025. Unlocking the UK's Growth Potential: The Tech Nation Report 2025. https://2025.report.technation.io/

Tony Blair Institute (TBI) for Global Change, 2025. From Startup to Scaleup: Turning UK Innovation into Prosperity and Power.

https://assets.ctfassets.net/75ila1cntaeh/10q8nKyiuKD4yWom2eM0rP/7fb039238ce5fc8d6880a60b04933cd5/50yltD2eFDmkz3vmFWVjHg--153208082025

van Ark, B., Inklaar, R. and McGuckin, R.H., 2003. "ICT and Productivity in Europe and the United States: Where Do the Differences Come From?" CESifo Economic Studies, 49(3), 295–318. https://doi.org/10.1093/cesifo/49.3.295

van Ark, B., O'Mahony, M. and Timmer, M.P., 2008. "The Productivity Gap between Europe and the United States: Trends and Causes." Journal of Economic Perspectives, 22(1), 25–44. https://doi.org/10.1257/jep.22.1.25

Vandenbussche, J., Aghion, P. and Meghir, C., 2006. "Growth, Distance to Frontier and Composition of Human Capital." Journal of Economic Growth, 11(2), 97–127. https://doi.org/10.1007/s10887-006-9002-y

Willemyns, J., 2025. "Copyright & AI: the case for a pro-growth approach." Centre for British Progress. https://britishprogress.org/briefings/copyright-ai-the-case-for-a-pro-growth-approach

Yotzov, I., Barrero, J.M., Bloom, N., Davis, S.J. et al., 2026. "Firm Data on AI." NBER Working Paper No. 34836. https://www.nber.org/papers/w34836
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
