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
- 已识别机构名：`世界银行`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份世界银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Labor Market Effects of Public Employment Guarantee

Yasmine Elkhateeb

Nelly Elmallakh

Luca Flabbi

Roberta Gatti

Mohamed Saleh

POLICY RESEARCH WORKING PAPER 11431

## Abstract

Public employment guarantee schemes, which channeled graduates into lifetime positions in the civil service and state-owned enterprises, were central to state-led industrialization across the postcolonial world, yet they have remained far less studied than temporary workfare programs. This paper provides the first causal estimates of their labor market effects, exploiting the Arab Republic of Egypt's archetypal public employment guarantee, which from the early 1960s guaranteed public sector jobs to secondary and university graduates without competitive examination. The paper measures district-level exposure by secondary school supply on the eve of the reform (1959/60) and links it to individual-level census microdata from 1986, 1996, and 2006. Using an event-study design with continuous treatment intensity, the analysis compares cohorts that differed in age at the time of the public employment guarantee's introduction across districts with differing pre-reform school supply. The findings show that the public employment guarantee reallocated urban male wage employment away from the private sector and toward state-owned enterprises, with no comparable shift in rural districts, where state-owned enterprises were largely absent. The reallocation was concentrated in manufacturing and high-skilled white-collar occupations, consistent with the policy channeling educated workers into sectors that were central to the state's industrialization drive. The paper finds little evidence that the public employment guarantee raised educational attainment, indicating that it primarily redirected an already growing pool of educated workers rather than expanding the supply of schooling.

# Labor Market Effects of Public Employment Guarantee\*

Yasmine Elkhateeb $^{\dagger}$ Nelly Elmallakh $^{\ddagger}$ Luca Flabbi $^{\S}$ Roberta Gatti $^{\ddagger}$ Mohamed Saleh $^{\P}$

Authorized for distribution by Indermit Gill, Chief Economist & Senior Vice President, Development Economics, World Bank Group

JEL classification: J45, J24, O15, J21, O14.

Keywords: employment, guarantee, public sector, education, Middle East.

## 1 Introduction

Governments have long used public employment as an instrument of redistribution and political incorporation. Two broad types exist. The first is workfare and public works programs, which offer episodic short-term employment to the poor or unemployed. These programs range from employment guarantees such as India's Mahatma Gandhi National Rural Employment Guarantee Act (MGNREGA) (Imbert and Papp, 2015; Muralidharan et al., 2023) to crisis-response and safety-net programs such as Argentina's Jefes Plan (Galasso and Ravallion, 2004) and Ethiopia's Productive Safety Net Program (Berhane et al., 2014). $^{1}$ The second type, Public Employment Guarantee (PEG) schemes, by contrast, channel eligible workers into lifetime positions in the civil service and state-owned enterprises (SOEs), as in China's “iron rice bowl” for urban workers (Cai et al., 2008), and employment guarantees for graduates meeting certain educational credentials in postcolonial East Africa (Simson, 2020) and the Middle East (Assaad and Barsoum, 2019).

While a substantial empirical literature has studied the labor market effects of workfare schemes, PEG schemes are far less studied. This is an important omission because the two types serve distinct political and economic functions. Workfare provides short-term income support that, among others, buys social peace among the poor. To the contrary, PEG creates a state-dependent middle class whose livelihood and status are tied to regime survival—the core mechanism of the “authoritarian bargain” social contract that characterized many post-independence polities (Desai et al., 2009; Yousef, 2004). The labor market implications differ accordingly. Workfare raises the reservation wage without removing workers permanently from the private sector. PEG permanently absorbs workers into the state sector, with ambiguous net effects: it crowds out private-sector careers but may also build bureaucratic capacity and staff state-led development programs. Despite decades of reliance on public hiring to absorb educated youth across much of the developing world, we know relatively little about how these permanent guarantees shaped labor markets.

This paper provides the first causal evidence on the labor market effects of PEG schemes on sectoral allocation, occupational sorting, and educational attainment, by exploiting the Arab Republic of Egypt's archetypal PEG that was introduced in the early 1960s. Before the PEG, recruitment into public employment was organized through competitive examinations, both written and oral. Beginning in 1961, however, a series of legal reforms entitled all secondary and university graduates, including both general and vocational secondary school tracks, to public sector jobs without competitive examination. This policy coincided with the expansion of the state's administrative apparatus and state-owned enterprises (World Bank, 2014) and with the expansion of mass education (Saleh, 2016). It remained in force until it was de facto suspended in the early 1980s, amid rising cohort sizes and constrained budgets, raising concerns about queuing, meritocracy, and skill mismatch (Assaad, 1997).

We compile and harmonize newly assembled data to construct a district-level measure of potential exposure to PEG, measured by secondary school supply at the district level in 1959/60, which we merge with individual-level population census microdata from 1986, 1996, and 2006. Our identification strategy is an event study that compares the evolution of labor market outcomes between older and younger cohorts born in districts with different supply of secondary schools on the eve of PEG. We study three outcomes: (i) sectoral sorting of wage labor across the public sector (SOEs and government) and the private sector, (ii) occupational sorting across blue- and white-collar jobs, and (iii) educational attainment (secondary and university degree completion). Our analysis focuses on men, since low female labor force participation in Egypt (Gatti et al., 2025) and systematic, sector- and district-varying under-enumeration of female employment in the censuses preclude reliable causal estimates for women; we discuss these data constraints in detail in Section 3.2.

Our findings indicate that the PEG caused a substantial reallocation of urban male wage employment away from the private sector and toward state-owned enterprises: a one-standard-deviation increase in pre-reform secondary school supply raised the probability of SOE employment by up to 1.3 percentage points for the most-exposed cohorts, with an offsetting decline in private-sector employment. We find no comparable shift in rural districts. Because SOEs were overwhelmingly concentrated in urban areas under Egypt's state-led industrialization strategy, the PEG's sectoral channel could only operate where SOEs existed, and we therefore treat the rural sample as a built-in placebo: the absence of any SOE shift precisely where the mechanism was inactive corroborates that our urban estimates reflect the guarantee rather than a coincident shock. Within urban labor markets, exposed cohorts were less likely to work in agriculture and more likely to work in manufacturing, and were sorted into high-skilled white-collar occupations, especially as professionals, technicians, and associate professionals. By contrast, we find little evidence that the PEG raised educational attainment: schooling was rising steadily across cohorts regardless, and the guarantee appears to have redirected this already growing pool of educated workers into the state sector rather than expanding the supply of schooling.

Our paper contributes to several strands of the literature. First, it contributes to the literature on the labor market effects of public employment schemes. A substantial body of empirical work studies India's MGNREGA, the world's largest public workfare program, and documents sizable impacts on workers' labor supply, wages, and welfare. Exploiting the program's phased rollout, Azam (2012) shows that MGNREGA increased labor force participation—particularly among women—and raised female casual wages, while Imbert and Papp (2015) find that public employment crowded out private work but raised private-sector wages, generating welfare gains that often exceeded direct program earnings. Consistent with these findings, Muralidharan et al. (2023) exploit a large-scale randomized improvement in program implementation and document substantial income gains and poverty reduction, driven primarily by higher private-sector wages and employment rather than direct program income.

In contrast, evidence on firm-side responses points to potential costs of employment guarantees for private firms. Using establishment-level data and staggered rollout for identification, Agarwal et al. (2021) find that MGNREGA reduced firms' permanent workforce by about 10 percent, inducing greater mechanization and lowering profits and productivity, consistent with partial crowding out of private-sector labor. However, exploiting discontinuities in rollout timing, Zimmermann (2024) finds little evidence of private job displacement in the program's first year, instead documenting reallocations from paid employment to family work, suggesting that employment guarantees may operate primarily as a safety net. Evidence from employment guarantee schemes outside the MGNREGA context is relatively scarce. Studying a major wage increase in Maharashtra's state-specific Employment Guarantee Scheme, Ravallion et al. (1993) show that higher statutory wages reduced employment through increased job rationing, weakening the guarantee. In a different institutional context, Pastore (2015) documents that Italy's European Youth Guarantee was limited by weak public employment services, resulting in low participation and few actual job placements.

All these programs, however, are workfare schemes offering temporary employment. The labor market effects of permanent PEG schemes—which were central to state capacity building in postcolonial settings and to industrial development under state planning—remain largely understudied. In China, the state assigned urban workers to lifetime employment in SOEs through the danwei (work unit) system as part of a broader project of state industrialization, until the massive restructuring of the late 1990s. Scholars have described the restructuring reform and its implications for the labor market (Cai et al., 2008), and estimated its causal effect on precautionary savings (He et al., 2018), but not on the original labor allocation induced by the guarantee itself. Simson (2020) documented how manpower planning policies and explicit employment guarantees in postcolonial East Africa—Kenya and Tanzania—channeled graduates into the public sector as part of post-independence state building, but again without causal identification of labor market effects. Across the MENA region, the PEG in Egypt (the focus of this paper) has been documented descriptively (Assaad and Barsoum, 2019; Assaad, 1997). Similar guarantees or quasi-guarantees emerged elsewhere in the region, albeit with distinct institutional designs. In Morocco, a program offered temporary public sector placements to young graduates as a bridge to private employment; in practice, these positions frequently became permanent after two years of civil service (Said, 1996). In Syria, guaranteed public jobs were historically extended to graduates of post-secondary intermediate institutes, a key pipeline into state-owned enterprises; after 2001, the guarantee for higher institute graduates was terminated, pushing them toward private sector absorption (Huitfeldt and Kabbani, 2007). In contrast to Egypt and Syria—where eligibility hinged primarily on reaching minimum educational thresholds—Jordan used public employment as a mechanism of political incorporation, allocating secure positions to Bedouin tribes and other groups central to regime stability (Assaad and Barsoum, 2019). In the Gulf Cooperation Council (GCC), Kuwait formalized a universalistic variant: the Government Sector Employment Law No. 18/1960 guaranteed qualified Kuwaiti citizens access to public employment and advanced “Kuwaitization,” the progressive substitution of expatriate labor with nationals. A dedicated “Complementary Fund Budget” (CFB) was established to provide financial incentives for government departments to hire new Kuwaiti applicants, channeling university graduates and secondary or intermediate school leavers (after completing training programs) into a wide range of government roles (Al-Enezi, 2002). Despite the prevalence and political significance of these schemes, our paper provides the first causal estimates of their labor market effects.

Second, our paper contributes to the literature on the labor market consequences of a large public sector. A growing body of empirical work documents that extensive public employment can crowd out private-sector activity. In MENA countries, the large footprint of SOEs has been linked to talent misallocation and weaker productivity, as public employment draws workers away from the private sector (Gatti et al., 2024). Cross-country evidence from OECD economies between 1960 and 2000 similarly points to substantial crowding-out effects: Algan et al. (2002) estimate that the creation of 100 public jobs eliminated roughly 150 private-sector jobs, lowering labor force participation and increasing unemployment. Extending this analysis to a broader set of countries, Behar and Mok (2019) use a panel of 194 advanced and developing economies over 1988–2011 and find evidence of full or near-full crowding-out of private employment by the public sector, with similar patterns across income groups. Consistent with these findings, both theoretical and empirical evidence emphasizes that crowding-out is more pronounced when public production is highly substitutable for private production and when public-sector jobs offer relatively attractive wages or non-wage benefits (Algan et al., 2002). Country-level evidence further corroborates the crowding-out effects of public employment on private employment in Greece (Demekas and Kontolemis, 2000), Italy (Caponi, 2017), Germany, Japan, and the United States (Malley and Moutos, 1998), while a smaller subset finds limited crowding-in in specific contexts, such as Germany and Spain (Becker et al., 2021; Jofre-Monseny et al., 2020). Our contribution is to document the origins of this crowding-out in MENA: we show that it was not merely a byproduct of an oversized public sector but was actively engineered through an explicit policy instrument—the education-based public employment guarantee. At the same time, interpreting the welfare implications of such crowding-out requires caution, since public employment in these settings was not simply displacing an established private sector but was simultaneously building industrial and bureaucratic capacity where little had previously existed.

Finally, our paper contributes to the literature on nationalization policies and the expansion of SOEs in developing countries. A related strand of literature examines how state ownership and nationalization of private firms shape labor markets in developing economies, even if much of the historical evidence remains descriptive rather than causal. Historical episodes of formal nationalization illustrate how state control of private industry restructures labor allocation and industrial performance. Quantitative analysis of nationalization in oil-producing countries, such as the República Bolivariana de Venezuela in the 1970s, finds significant declines in productivity and shifts in workforce composition following expropriation of foreign-owned assets (Melek, 2020). Studies of Pakistan's nationalization program under Zulfikar Ali Bhutto in the 1970s similarly show a reconfiguration of the industrial base under state ownership, with long-run implications for private investment and labor allocation as capital and entrepreneurs shifted to small-scale and informal sectors (Chengappa, 2002). An extreme case is Cuba's 1968 Revolutionary Offensive, in which virtually all remaining private small businesses were nationalized and employment consolidated under state planning, illustrating how deep nationalization can reshape employment structures and labor mobilization in a developing economy (Mesa-Lago, 1972). Together, this literature suggests that ownership transitions toward the state can significantly reshape employment patterns, productivity, and labor allocation, providing a useful backdrop for interpreting our findings on increased SOE and manufacturing employment during nationalization episodes. $^{2}$

The rest of this paper is organized as follows: Section 2 provides background information on the public sector employment guarantee scheme in Egypt. Section 3 presents the data. Section 4 discusses the empirical strategy. Section 5 presents the main results, while Section 6 presents some robustness checks. Finally, Section 7 discusses the mechanisms and Section 8 concludes.

## 2 Egypt's Public Employment Guarantee Scheme

Employment in the public sector in 1950s Egypt was subject to a public competition examination. Law 210 of 1951 and Law 113 of 1958 determined the procedure for recruitment for state civil servants and in joint stock companies and public institutions, respectively. $^{3}$ In order to be appointed, individuals must have successfully passed the examination prescribed for the position, which often consisted of both written exams and oral interviews. $^{4}$ Moreover, the public competition examination for joint stock companies and public institutions was advertised in newspapers.

Starting from 1961, gradual reforms were implemented, paving the way for a full-fledged implementation of the public employment guarantee scheme in Egypt. First, Law 8 of 1961 introduced a temporary two-year exemption—starting from the law’s date of entry into force—from the public competition examination requirement, allowing entities to fill existing vacancies for public sector appointments without an examination. In 1962, under Presidential Decree No. 425, new budget lines were created in the state budget to fund sixth-grade civil service positions allocated to graduates of non-STEM faculties at universities 

[中间内容因长度限制已省略]

orce by birth cohort, separately for urban districts in (a) and rural districts in (b). The sample is restricted to females aged 30 to 60 years, born in 1963 or earlier, in 1986, 1996, and 2006. The dependent variable is a binary indicator equal to 1 if the individual is in the labor force and 0 if he is out of labor force. The estimates are obtained from a specification that interacts birth cohort dummies with a continuous measure of treatment intensity: the number of secondary schools per 1,000 school-aged individuals (aged 15-19 in 1960) in the district of birth in 1959. The omitted cohort is 1941. Controls include the share of cultivated land redistributed between 1952 and 1961 by the land reform, interacted with birth cohort, as well as fixed effects for birth cohort, district of birth, census year, and age. Standard errors are clustered at the district of birth level. Vertical bars represent $95\%$ confidence intervals.

Source: Authors' calculations based on IPUMS Egypt census data (1986, 1996, 2006) and administrative school statistics (1959/1960).

Fig. E.3. Public Employment Guarantee and Female Wage Employment Among the Employed  
(a) Urban  
![](images/2c20144118f4a364a66a93bf18f8aa576ed152afc836cf6f6ab32a02e81e86df.jpg)

(b) Rural  
![](images/3b808947abd05e4cf70742181bfe8c54a0a32a1c98e47056c4d1bcfb5201f249.jpg)

Notes: These figures plot the estimated effect of exposure to the PEG on the probability of being a wage worker (as opposed to self-employed) by birth cohort, separately for urban districts in (a) and rural districts in (b). The sample is restricted to females aged 30 to 60 years, born in 1963 or earlier, in 1986, 1996, and 2006, who are employed, excluding unpaid family workers. The dependent variable is a binary indicator equal to 1 if the employed individual is a wage worker and 0 if he is self-employed. The estimates are obtained from a specification that interacts birth cohort dummies with a continuous measure of treatment intensity: the number of secondary schools per 1,000 school-aged individuals (aged 15–19 in 1960) in the district of birth in 1959. The omitted cohort is 1941. Controls include the share of cultivated land redistributed between 1952 and 1961 by the land reform, interacted with birth cohort, as well as fixed effects for birth cohort, district of birth, census year, and age. Standard errors are clustered at the district of birth level. Vertical bars represent 95% confidence intervals. Source: Authors' calculations based on IPUMS Egypt census data (1986, 1996, 2006) and administrative school statistics (1959/1960).

Fig. E.4. Public Employment Guarantee and Female Wage Workers Sector of Employment in Urban Districts  
(a) State-owned enterprises  
![](images/49d0a529d0f105b331795ef861d7521b824546573cbed01b0c4031a73ab3da25.jpg)

(b) Private sector  
![](images/bb37a9457c9177fa75d3fd6aa7cf70c87d5b306611c1c56c0b195afda3336ada.jpg)  
(c) Government

![](images/02f80e973d81ef8a682362dd27351d9acecb2e42df6012e25d9b3b7d9fb0d140.jpg)  
Notes: These figures plot the estimated effect of exposure to the PEG on the probability of employment in each sector among wage workers in urban districts, by birth cohort. The sample is restricted to females aged 30 to 60 years, born in 1963 or earlier, in 1986, 1996, and 2006. The dependent variable in each panel is a binary indicator equal to 1 if the wage worker is employed in the specified sector and 0 otherwise. The estimates are obtained from equation (1), a specification that interacts birth cohort dummies with a continuous measure of treatment intensity: the number of secondary schools per 1,000 school-aged individuals (aged 15–19 in 1960) in the district of birth in 1959. The omitted cohort is 1941. Controls include the share of cultivated land redistributed between 1952 and 1961 by the land reform, interacted with birth cohort, as well as fixed effects for birth cohort, district of birth, census year, and age. Standard errors are clustered at the district of birth level. Vertical bars represent 95% confidence intervals.

Source: Authors' calculations based on IPUMS Egypt census data (1986, 1996, 2006) and administrative school statistics (1959/1960).

Fig. E.5. Public Employment Guarantee and Female Wage Workers Sector of Employment in Rural Districts  
(a) State-owned enterprises  
(b) Private sector  
![](images/6711abd41e6b1d7aa35a211df67cc553f9a1ef0129f2d09448e2382b65e7f1c9.jpg)

(c) Government  
![](images/379f117e024e03c6ccc048eb1b568d8f600f7612cf82111fcd73a28a6f993676.jpg)

Notes: These figures plot the estimated effect of exposure to the PEG on the probability of employment in each sector among wage workers in rural districts, by birth cohort. The sample is restricted to males aged 30 to 60 years, born in 1963 or earlier, in 1986, 1996, and 2006. The dependent variable in each panel is a binary indicator equal to 1 if the wage worker is employed in the specified sector and 0 otherwise. The estimates are obtained from equation (1), a specification that interacts birth cohort dummies with a continuous measure of treatment intensity: the number of secondary schools per 1,000 school-aged individuals (aged 15–19 in 1960) in the district of birth in 1959. The omitted cohort is 1941. Controls include the share of cultivated land redistributed between 1952 and 1961 by the land reform, interacted with birth cohort, as well as fixed effects for birth cohort, district of birth, census year, and age. Standard errors are clustered at the district of birth level. Vertical bars represent 95% confidence intervals.

Source: Authors' calculations based on IPUMS Egypt census data (1986, 1996, 2006) and administrative school statistics (1959/1960).
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
