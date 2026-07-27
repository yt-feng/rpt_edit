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
# Selection or More Capital? Experimental Evidence on High-Growth Entrepreneurs in Kenya

Francisco Campos

Abla Safir

Celine Koffka

David McKenzie

Bilal Zia

POLICY RESEARCH WORKING PAPER 11432

## Abstract

Business plan competitions aim to identify and spur high-growth entrepreneurs. Two experiments were embedded into in a Kenyan competition to test how intensity of selection and of capital determine entrepreneurial outcomes. Applicants received a US\$9,000 grant after a streamlined process or went through multiple selection stages and were randomly assigned US\$9,000 or US\$36,000. All grants initially generated jobs, but the impacts only persisted over three years under multi-stage selection. The larger grants did not yield greater long-term impacts than the multi-stage US\$9,000 grant, suggesting diminishing returns to capital and limited lumpy investment opportunities. Selection, rather than grant size, determines long-run firm growth..

![](images/6b3897cd0daa6c9966d200a6f32f5fe401923d5b9b881513b21d5fee8514ef0b.jpg)

# Selection or More Capital?

# Experimental Evidence on High-Growth Entrepreneurs in Kenya#

Francisco Campos, Abla Safir, Celine Koffka, David McKenzie and Bilal Zia

Authorized for distribution by Xavier Gine, Lead Economist, Development Research Group, Development Economics, World Bank Group

Keywords: Business plan competition; high-growth entrepreneurship; job creation.

JEL codes: O12, M13, L26.

## 1. Introduction

Of the estimated 244 million firms in Africa, 232 million (95%) are own-account businesses consisting of only the owner, and a further 7.7 million (3.1%) have fewer than five employees (Cruz et al, 2025). Efforts to provide finance and training to these microenterprise owners have yielded increases in profits, but zero increase in employment on average (Grimm and Paffhausen, 2015; McKenzie et al, 2025). A key policy objective is to increase the number of high-growth firms that hire workers and expand beyond this micro size. Business plan competitions have become one popular policy tool for this purpose. They aim to identify from the vast pool of current and potential entrepreneurs a subset with the entrepreneurial ability to grow a larger firm, and then to overcome capital constraints on this growth through awarding grants. This raises the questions of how best to select the firms to support, and how much support to provide them. Competitions can use streamlined or multi-phased approaches to selection, and they vary dramatically in the amount of financial support they offer to winners.

A streamlined selection process can save costs and time for both the entrepreneur and government, potentially allowing funding to be accessed more rapidly. It will also be efficient if most of the selection of talent occurs through self-selection into entry, and through eliminating an easy-to-determine bottom tail of entrants. A multi-stage process may increase complexity and delay access to funding with little improvement in outcomes as it can also be very difficult to predict which entrepreneurs will succeed most (Nanda, 2016; McKenzie and Sansone, 2019), let alone which will have the largest treatment effects. However, a multi-stage process may be better if additional steps screen further on ability and commitment and provide a clearer signal of who will benefit most from support.

It is also unclear how much capital is needed to overcome liquidity constraints. A standard concave production function would suggest offering smaller grants to more firms, due to diminishing returns to capital. In contrast, if setting up or growing a firm beyond the microenterprise size requires large indivisible investments, it would be more efficient to provide larger grants to a smaller number of firms given a fixed budget. In practice there is extremely wide variation in the average size of the grants given in business plan competitions, even just considering competitions in Sub-Saharan Africa. Award sizes range from \$580 in Ethiopia for an ILO Business Plan competition $^{1}$ to \$1,000 in the Aspire competition run in Ethiopia, Tanzania and Zambia (Fafchamps and Quinn, 2017); \$5,000 in the pan-African competition run by the Tony Elumelu Foundation $^{2}$ ; \$5,000-\$15,000 for a youth entrepreneurship competition in Côte d’Ivoire (Weber, 2014); \$25,000 for a youth employment competition in Mozambique $^{3}$ ; \$35,000 for a government competition in Benin $^{4}$ ; \$50,000 for the YouWin! competition in Nigeria (McKenzie, 2017); and up to \$141,000 in Somalia (Weber, 2014).

We embed two randomized experiments in the context of the MbeleNaBiz Business Plan Competition in Kenya in order to test how selection intensity and capital constraints determine the effectiveness of the competition in generating firm growth and employment. The competition was a nationwide competition that attracted more than 12,000 applications. A selection experiment randomizes whether firms go through a streamlined screening, in which only applicants classified with very low potential (26% of eligible applications) are screened out based on a first-stage application form and then submitting a business plan, before 500 firms were randomly selected for \$9,000 grants or for a control group; or a multi-stage screening, in which firms submitted detailed business plans, which were scored and ranked by judges, with the top 750 plans (top 6% of applicants) being eligible to be randomized to a grant or control group. The grant size experiment randomizes these 750 firms to receive either \$9,000, \$36,000, or to a control group. $^{5}$ We then use three rounds of annual follow-up surveys to measure impacts of this \$13.5 million in grant funding on firm size, employment, and profitability.

We find that the selection process has a large impact on the effects of the grants, whereas the multi-stage \$36,000 (36K) grants do not have significantly higher lasting impacts on employment and firm growth than the multi-stage \$9,000 (9K) grant. In the first year, the 36K grants increased employment by more than 100%, adding an average of 5.0 workers per firm and taking an additional 21.8 percentage points of firms beyond a size threshold of 10 workers from a control base of 11.8%. However, after 3 years, this impact has fallen to 2.6 workers per firm (132% impact), compared to 2.0 workers per firm for the 9K multi-stage grant (102% impact), with both grants having impacts of 9-10 percentage points on getting firms above the 10-workers size threshold. The 36K grant increases monthly sales by \$982, a 69% increase on the control mean, and monthly profits by \$211, a 60% increase over the control mean. The multi-stage 9K grant increases monthly sales by \$839 (59%), and monthly profits by \$183 (52%). We cannot reject equality of these impacts with those of the 36K grant, and we can reject that the 36K grant has four times the impact as the 9K.

In contrast with the multi-stage process, the employment impacts of the streamlined 9K grant dissipate over time, and are only 0.6 workers per firm after 3 years, statistically different from those of the multi-stage grant. The streamlined 9K grant only has a pooled impact of \$79 in monthly sales (7% of the control mean, and not statistically significant), and no impact on monthly profits. We can reject equality of impacts of the two 9K grants.

We find that the large and small grants appear to have been spent proportionally on similar items, and largely for non-lumpy investments in capital and labor rather than large indivisible capital investments. Firms improve their business practices and increase innovation and training, but not much more so with the 36K grant than the multi-stage 9K grant. Therefore, there do not appear to be profitable indivisible investment opportunities that these entrepreneurs can pursue with 36K but not 9K, and the 9K multi-stage grants are much more cost-effective at generating new jobs and boosting firm performance than the 36K grants as a result. The limiting factor on firm size in our sample appears to be entrepreneurial ability, as in the model of Lucas (1978), and not capital beyond the 9K grant size. The streamlined selection resulted in more women and new firms being selected by design, reweighting for these characteristics does not change the lower performance of these grants. The multi-stage selection does appear to have been better at selecting who can benefit most from the grants.

This paper contributes to several literatures. The first is a broad literature on why there are so many small firms in developing countries and what policy actions may change this. One explanation is that this size distribution is seen as the result of misallocation (Hsieh and Klenow, 2009) due to factors such as size-dependent policy distortions (Restuccia and Rogerson, 2008), informality (Ulyssea, 2018), and financial frictions (Buera et al, 2011). An alternative explanation is that the small size of many firms is optimal given the inherent structural features of low-income economies, such as limited supply of the managerial talent needed to manage large firms (Engbom et al, 2025), small market sizes (Tybout, 2000), and poorer consumers demanding lower quality goods that are optimally produced at smaller scale (Jain and Kothari, 2025). Our evidence that there is a pool of talented entrepreneurs out there who can grow in size when financial constraints are alleviated suggests that the causes of small firms are not entirely due to these structural factors.

Second, our paper contributes to the debate about the extent to which production non-convexities hold back the size of firms and can generate poverty traps. McKenzie and Woodruff (2006) and de Mel et al. (2009) argue that the high returns from small capital investments of \$100-\$200 suggest a lack of non-convexities at low levels of investment. However, Kaboski et al. (2025) find evidence of indivisibilities when comparing \$100 and \$500 grants in Uganda, and Balboni et al. (2022) argue for the presence of a poverty trap investment threshold at around \$500 in rural Bangladesh, although Karlan et al. (2026) show that this conclusion is not robust to functional form choices and may reflect geographic confounds. Our evidence suggests no such indivisibilities within the range of the much larger grant sizes we study.

Third, our paper contributes to the literature on gender and entrepreneurship. Small grants of \$100 to \$200 to women entrepreneurs have had smaller impacts than for men (de Mel et al, 2009; Fafchamps et al. 2014; Hussam et al, 2022). This may reflect the efficient scale for many of these firms being very low, given other constraints such as a lack of demand (Hardy and Kagy, 2020) or household constraints being more binding (Jayachandran, 2021). However, there is large heterogeneity in the returns to capital (Hussam et al, 2022; Bryan et al, 2024), suggesting some women may still have high returns. There was no gender difference in impacts of large grants in Nigeria for women making it through the business plan competition (McKenzie, 2017). In our experiments, we cannot reject that the women who won had equal treatment effects from the 36K and 9K multi-stage grants as men. Since women were less likely to be running firms, and had smaller firms in absence of treatment, these similar absolute gains represent larger gains in relative terms for women. The competition thus was able to identify and support the growth of talented women entrepreneurs as well as men.

Finally, we contribute to the literature on business plan competitions as a tool for policy makers to directly identify and spur high-talent entrepreneurs. Key questions revolve around the extent to which high-growth entrepreneurs are capital constrained, and whether their marginal returns to capital vary at different amounts of capital infusion. McKenzie (2017) finds a \$50,000 grant in Nigeria led to firms being 20 percentage points more likely to reach a threshold of 10 or more workers over three years. But grants of this size are expensive to provide, raising the question of whether it would be more effective to support more firms with smaller grants for each. Our results provide support for the hypothesis that funding more firms with less money per firm can deliver higher returns in terms of job creation, but they also show the importance of screening for high returns.

## 2. The Business Plan Competition

## 2.1 MbeleNaBiz

MbeleNaBiz (Swahili for “Moving Ahead with Business”) was a business plan competition in the Kenya Youth Employment and Opportunities Project (KYEOP), a US\$150 million World

Bank-financed project, implemented between 2016 and 2023. MbeleNaBiz was jointly implemented by the Ministry of ICT, Innovation and Youth Affairs (MIIYA) and the Kenyan Micro and Small Enterprises Authority (MSEA), with technical support from KPMG. The objective was to drive job creation among youth, the age group most likely to be without jobs in Kenya (World Bank, 2016). Women were identified at the design phase as potentially facing additional constraints in starting and growing businesses due to family and household responsibilities (World Bank, 2016), and as being less likely than men to enter competitive settings in lab experiments (Paryavi et al, 2025). This led to a policy interest in examining gender differences in both participation and performance in the competition.

The program was launched in 2019, accepting application submissions between June 24, 2019, and September 2, 2019 (see timeline in Appendix A). The launch was accompanied by a large-scale awareness campaign including radio, internet, newspapers, in-person awareness events in universities, microfinance institutions, incubation centres, and outreach through business associations, women's groups, and tech-development networks. Female participants were specifically targeted in this awareness campaign with the objective of achieving higher participation than in other settings (e.g. in the Nigeria YouWin! Competition, women were 18.5 percent of new business applicants and 14.9 percent of existing business applicants (McKenzie, 2017)).

To be eligible, the lead applicant had to be between 18 to 35 years old, of Kenyan nationality, have completed at least secondary education, and be seeking to operate a business in Kenya. Applicants could apply with either a new business idea or an existing business that they wanted to expand. The program received 12,171 applications, which were screened for eligibility and completeness to 11,466 eligible applications. Twenty-five percent of the applicants were women, and 52 percent were for new business proposals.

Proposals were anonymized and KPMG completed a first-round scoring. Two consultants were assigned to each proposal and scored the quality of the business idea, the expected number of jobs with an emphasis on jobs for young women, what sets them apart from competitors, business risks, the planned investment of the award grant should they win, and their relevant experience. $^{6}$ The proposals were ranked in multiple buckets of potential with the bottom two buckets (amounting to 26% of eligible applications) screened out during this process, and the top 8,475 applicants randomly allocated to either pass through a streamlined selection process, or go through a multi-stage process, as set out in Figure 1.

## 2.2 Streamlined Selection Process

A random sample of 1,003 applicants were randomly allocated to the streamlined selection process, stratified by gender and whether the applicant had an existing or new business. This included 500 women and 503 men, oversampling women to have increased statistical power to detect gender differences in effects. We conducted a baseline survey, and those in this group were then asked to submit a business plan online (following the same process and timeline as the multi-stage process described below), with 829 applicants submitting plans. From this set of 829, 250 applicants were randomly assigned to receive a grant of \$9,000, 250 were randomly assigned as a control group, and the remaining 329 had their plans scored in the multi-stage process. Since it was unclear what the composition of awardees would be in the multi-stage process, selection for streamlined awards was stratified by gender and new/existing business status to have equal numbers from each subgroup.

The screening for the recipients of 9k in the streamlined process was then only the initial scoring based on the application form, and the self-selection of completing a business plan. There was no scoring or judging of the business plans to determine these streamlined awards.

## 2.3 Multi-Stage Selection Process

In the multi-stage process, the scores from the initial applications were used to further reduce the set of applications to the top 4,000 applicants. These applicants were then invited to proceed to a second stage and submit business plans online, to join the 329 submissions from the streamlined process. $^{7}$ These business plans were intended to capture the potential of the businesses and their plans for growth, rather than focusing on how they would use the grant money. A total of 3,182 applicants submitted business plans by the deadline of August 31, 2020. $^{8}$ These plans were evaluated by independent judges assembled by KPMG, comprising entrepreneurs, business coaches, and industry leaders. There was an effort to ensure diversity in the judges, and they were a combination of 38 women and 24 men, of whom 11 were international. These judges were each paid an honorarium of around \$500 for contributing their time.

The judges evaluated the business plans on a scale of 0 to 100 based on scoring eleven different elements: the elevator pitch of the overall business plan (6 points); the value proposition (15 points); understanding of customers (7 points); and of competitors (7 points); marketing strategy (15 points); business processes (7 points); human resource plans including potential to create jobs and understanding the roles these workers will play (15 points); financial plans and economic viability (15 points); risk and mitigation strategies (7 points); any additional benefits to society (2 points); and a capstone score for overall promise (4 points). Note that the plans did not say how they would use grants of different sizes, but rather what their overall potential and plans for growth for the business would be.

Business plans were anonymized and scored by one judge, with those that scored more than 60 then moved to a second round to be evaluated by a second judge. Business plans were ra

[中间内容因长度限制已省略]

es includes all workers employed by the business, excluding the owner, and is winsorized at the 99th percentile. Has 10 or More Employees is an indicator equal to one if the business employs at least 10 workers. Monthly Profits are winsorized at the 1st and 99th percentiles; all other transformations are the same.

Table F2: Heterogeneity in Impacts for the Multi-stage Top 750 by Judges' scores

<table><tr><td rowspan="2"></td><td colspan="3">3 Year Follow-up survey</td><td colspan="3">Pooled Specification</td></tr><tr><td>Number of Employees (1)</td><td>More than 10 employees (2)</td><td>Profits (3)</td><td>Number of Employees (4)</td><td>More than 10 employees (5)</td><td>Profits (6)</td></tr><tr><td>36k</td><td>2.333***(0.651)</td><td>0.076**(0.036)</td><td>188**(96)</td><td>3.185***(0.629)</td><td>0.126***(0.033)</td><td>13(87)</td></tr><tr><td>36k * Above</td><td>0.734(1.137)</td><td>0.052(0.065)</td><td>234(221)</td><td>1.183(0.921)</td><td>0.045(0.051)</td><td>412**(176)</td></tr><tr><td>9k-Multi</td><td>1.620**(0.648)</td><td>0.053(0.035)</td><td>128(109)</td><td>2.025***(0.568)</td><td>0.079***(0.029)</td><td>83(105)</td></tr><tr><td>9k-Multi * Above</td><td>0.902(1.079)</td><td>0.071(0.064)</td><td>198(222)</td><td>0.435(0.842)</td><td>0.016(0.046)</td><td>194(189)</td></tr><tr><td>Dummy Above</td><td>0.534(0.593)</td><td>0.041(0.037)</td><td>-44(131)</td><td>0.184(0.540)</td><td>0.034(0.028)</td><td>-60(117)</td></tr><tr><td>Observations Multi</td><td>508</td><td>508</td><td>507</td><td>1584</td><td>1584</td><td>1597</td></tr><tr><td>Control Multi Mean</td><td>1.993</td><td>0.054</td><td>291</td><td>2.947</td><td>0.081</td><td>352</td></tr><tr><td>P-value: 36k = 9k (Below)</td><td>0.365</td><td>0.574</td><td>0.626</td><td>0.059</td><td>0.163</td><td>0.462</td></tr><tr><td>P-value: 36k = 9k (Above)</td><td>0.592</td><td>0.947</td><td>0.646</td><td>0.014</td><td>0.084</td><td>0.378</td></tr><tr><td>P-value: 36k = 9k-Multi (joint)</td><td>0.579</td><td>0.852</td><td>0.800</td><td>0.010</td><td>0.089</td><td>0.523</td></tr></table>

Regressions include randomization strata and the baseline value of the outcome, as well as an indicator for missing baseline values. The pooled specification includes survey-wave fixed effects. Standard errors are robust and, in the pooled specification, clustered at the respondent level. Above is a dummy variable taking the value 1 if the respondent scored above the median in their application. \*, \*\*, and \*\*\* denote significance at the 10, 5, and 1 percent levels, respectively. Number of Employees includes all workers employed by the business, excluding the owner, and is winsorized at the 99th percentile. Has 10 or More Employees is an indicator equal to one if the business employs at least 10 workers. Monthly Profits are winsorized at the 1st and 99th percentiles; all other transformations are the same.

Table F3: Baseline Correlates of Judges' Score in the Multi-stage Sample

<table><tr><td>Variable</td><td>Baseline judge score</td></tr><tr><td>Strata: Female, new business</td><td>-0.809(0.938)</td></tr><tr><td>Strata: Male, existing business</td><td>-0.483(0.575)</td></tr><tr><td>Strata: Male, new business</td><td>-0.242(0.678)</td></tr><tr><td>Age</td><td>-0.004(0.054)</td></tr><tr><td>Education = Certificate</td><td>-0.692(0.994)</td></tr><tr><td>Education = University/College</td><td>0.834(0.632)</td></tr><tr><td>Education = Postgraduate</td><td>0.798(0.951)</td></tr><tr><td>Sector = Agriculture</td><td>0.738(0.689)</td></tr><tr><td>Sector = Retail</td><td>1.284(0.833)</td></tr><tr><td>Sector = Information/Communication</td><td>0.333(0.778)</td></tr><tr><td>Sector = Manufacturing</td><td>1.508(0.960)</td></tr><tr><td>Sector = Technology</td><td>-0.782(0.826)</td></tr><tr><td>Number of Businesses</td><td>-0.403(0.462)</td></tr><tr><td>Has more than 1 Business</td><td>0.627(0.790)</td></tr><tr><td>Sales</td><td>0.000***(0.000)</td></tr><tr><td>Profit</td><td>-0.000(0.000)</td></tr><tr><td>Profit from all Businesses</td><td>-0.001(0.002)</td></tr><tr><td>Employees</td><td>-0.011(0.027)</td></tr><tr><td>Percentage of Paid Workers</td><td>-0.137(0.634)</td></tr><tr><td>Hours Worked on Business</td><td>0.004(0.008)</td></tr><tr><td>Inventory Value</td><td>0.000(0.000)</td></tr><tr><td>Equipment Value</td><td>-0.000(0.000)</td></tr><tr><td>Business Salary</td><td>0.000(0.001)</td></tr><tr><td>Employment Income</td><td>-0.001(0.002)</td></tr><tr><td>Total Income</td><td>0.001(0.002)</td></tr><tr><td>Business Practices Index</td><td>-2.970(1.992)</td></tr><tr><td>Innovation and Training Index</td><td>2.813(1.803)</td></tr><tr><td>Expects Life Improvement in 5 Years</td><td>1.078(1.522)</td></tr><tr><td>Confidence</td><td>1.859(1.579)</td></tr><tr><td>Borrowed in the Past from a Microfinance Institution or Bank</td><td>-0.122(0.553)</td></tr><tr><td>Lived Abroad at Baseline</td><td>-2.167(1.399)</td></tr><tr><td>Business Name Registered in Company Registrar</td><td>1.092**(0.546)</td></tr><tr><td>Streamlined Score</td><td>0.047*(0.026)</td></tr><tr><td>N</td><td>750</td></tr><tr><td>R-squared</td><td>0.093</td></tr></table>

For age, information from intake is used to account for the fact that the two baselines did not take place at the same point of time. All monetary variables have been deflated to real Kenyian shillings using 2024 prices, and have then converted to US-dollars. Sales and Profit variables are reported for the last month. Number of Employees, Sales, Value of Inventory, have been winsorized at the 99 percentile. Value of equipment has been winsorized at the 95th percentile. Profits, Salary, and hours worked have been winsoried at the 1st and 99th percentiles.
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
