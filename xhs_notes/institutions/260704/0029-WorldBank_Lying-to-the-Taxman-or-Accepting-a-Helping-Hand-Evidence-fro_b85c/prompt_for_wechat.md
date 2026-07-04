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
- 已识别机构名：`世界银行`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- CTA 必须每篇重新写，不能固定套话。它需要自然包含这些信息：更多国际信源汇编&评论，扫码交流，每日更新，汇总国际主流叙事&数据&图表，观测边际变化；汇聚了头部券商、PE/VC、投行、并购、hedge fund、资管机构、战略咨询、智库等朋友，期待交流。

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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份世界银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Lying to the Taxman or Accepting a Helping Hand?

Evidence from a Novel Experiment on SMEs in Tanzania

Revocatus Paul

Ephraim Mdee

Massaga Fimbo

Jonathan Karver

Zain Chaudhry

Christopher Hoy

POLICY RESEARCH WORKING PAPER 11062

## Abstract

This paper presents the results from a novel field experiment that examined the impact of in-creasing the presence of revenue authority officers on tax compliance and tax morale among small and medium-size enterprises in a lower-income country. The experiment was embedded in the implementation of a representative, face-to-face survey of SMEs across mainland Tanzania. An independent survey firm was accompanied by Tanzania Revenue Authority officers, who observed the interviews in a randomly selected set of urban and peri-urban wards. This translated into a temporary increase in the presence of tax officers throughout parts of the country. The findings indicate that an increase in tax officer presence did not have a significant overall impact on tax compliance and tax morale among SMEs, as measured using a combination of administrative and survey data. However, there were short-term increases in compliance in the largest city and sustained increases in tax morale in the rest of the country. A follow-up survey suggests that these results were likely driven by an increase in the perceived credibility of enforcement rather than meaningful increases in perceptions of facilitation and trust.

# Lying to the Taxman or Accepting a Helping Hand? Evidence from a Novel Experiment on SMEs in Tanzania\*

Revocatus Paul (World Bank),
Ephraim Mdee (Tanzania Revenue Authority),
Massaga Fimbo (Tanzania Revenue Authority),
Jonathan Karver (World Bank),
Zain Chaudhry (World Bank)
and Christopher Hoy (World Bank)

JEL Classification: D04, D80, D90, H20, H30, H50

Keywords: Taxation, Public Finance, Small Businesses, Randomized Experiment

## 1 Introduction

Taxing small and medium-sized businesses -otherwise known as small and medium-sized enterprises, or SMEs- can be challenging for a variety of reasons (e.g., see Hoy et al. 2024), with uncertain or, at best, unambiguously small fiscal gains, depending on the context. Moreover, the direct and indirect costs for governments from trying to enforce tax compliance among SMEs can be substantial. As a result, revenue authorities are increasingly investing in quasi-voluntary strategies to improve compliance among SMEs, such as greater engagement between tax officials and firms to help facilitate the tax payment process (Dom et al. 2022). However, relatively little is known about how SMEs respond to closer engagement and community presence by revenue authorities, particularly when this engagement transcends the usual audit-oriented interactions.

This paper examines how SMEs react to increased local presence by tax officials by drawing on a novel field experiment in Tanzania. The World Bank and the Tanzania Revenue Authority (TRA) implemented a broadly representative in-person survey of SMEs across mainland Tanzania in December 2022. Among the 119 urban and peri-urban wards that were included in the study, half were randomly assigned to have tax officials present during the data collection exercise. This clustered randomized controlled trial introduced exogenous variation in the visibility and physical presence of tax officials among SMEs. While the tax officials did not directly survey the businesses (the survey was conducted by a local survey research firm and trained enumerators were tasked with conducting the interviews), simply having a tax official present was expected to have repercussions on respondents' self-reported behavior (captured through the survey) as well as declaration behavior (captured through administrative data). As a consequence, it is valuable to examine both the impact of TRA presence on survey outcomes and ward-level indicators of compliance.

Tanzania is a useful context to explore strategies for improving SME taxation. Tanzania's SMEs are overwhelmingly informal. Those that are registered with the TRA are primarily subject to a simplified, presumptive tax regime. However, evidence has shown that there are likely many non-compliant businesses within the SME sector: firms that have managed to remain informal as well as those that have registered but stopped paying taxes at some point along the way. The cost of enforcing compliance among this group is particularly high: there are a considerable number of registered SMEs in Tanzania (with fewer than 10 employees) but many of these do not regularly pay taxes.

Though the TRA has offices in all tax regions and districts of Tanzania, tax administration activities are more pronounced within the country's economic capital, Dar es Salaam, which houses the headquarters of the TRA. This reflects the high concentration of economic activity in Dar es Salaam relative to the rest of the country. As a result, the visibility of the TRA on the ground varies tremendously, even across urban and peri-urban areas. For example, of the 32 tax regions in mainland Tanzania, 5 are in Dar es Salaam owing to the city's potential for raising revenue and being the trading hub (business center) of the country. Moreover, after many years of what Tanzanian society viewed as tax administration centered around enforcement that was considered excessive and unfair -in particular, by SMEs- the TRA has shifted efforts to promote voluntary compliance by engaging with taxpayers more positively. For example, by implementing awareness campaigns such as the "Door to Door" initiative to enhance taxpayers' knowledge, setting up self-service facilities like the taxpayer portal, and sending reminder messages to taxpayers regarding their tax obligations.

The TRA has adopted a tax administration approach focused on facilitation and building trust. This is evident in the expansion of awareness campaigns led by the Taxpayers' Education and Communication Department, where officials regularly visit businesses to educate them on tax responsibilities and understand their challenges. This marks a shift from traditional enforcement-based interactions. However, the effect of these engagements, which differ from audit-driven approaches, on tax morale and compliance has not yet been studied. Our experiment, designed to reflect this type of interaction, provides initial insights into its potential impact.

The findings from our field experiment provide mixed results in terms of the impact of increasing local presence of tax officers on taxpayer attitudes and behaviors. Findings from the survey suggest that increasing the local presence of tax officers had a positive impact on tax morale, but this was concentrated outside Dar es Salaam and centered around limited survey measures. The impact on compliance of taxpayers in targeted wards is also not straightforward. On the extensive (paid anything) and intensive (amount paid) margins, overall the treatment has no impact. However, looking at heterogeneity across regions, increased local presence of tax officers had a positive impact on both the likelihood of payment and the payment amount in the Eastern region of Tanzania (primarily made up of Dar es Salaam and Pwani) in the first quarter of 2023 (immediately after the data collection).

The explanation for the lack of overall impact is likely due to the limited spillover effects on non-visited businesses, which is supported by an endline survey conducted in April/May 2024 in treatment and control wards with the same and neighboring businesses as the December 2022 survey. Combining findings from survey and administrative data, we try to reconcile these by exploring whether survey responses were biased (i.e., untruthful) -reflecting fear of reprimand for claiming low tax morale- or unbiased (i.e., truthful) -reflecting the increase positive view of the TRA and own obligations as a result of increased visibility. Anecdotal evidence suggests that the first hypothesis -where businesses are ‘lying to the taxman’ -is more likely, though more research is needed to validate this.

While the intervention does not provide clear results on the causal impact of a temporary, exogenous facilitation and trust based increase in the local presence of a revenue authority on compliance, the implementation itself provides many lessons learned for future experiments. This study was particularly unique since it involved embedding a field experiment within a data collection activity. To our knowledge, no studies exist where tax officials accompany enumerators in data collection to act as observers. This represents a useful exercise in understanding how responses about tax compliance and tax morale are and are not sensitive to who is perceived to be conducting a data collection activity. Questions around tax compliance and morale are considered particularly sensitive; a third-party survey firm is meant to represent an objective entity that can obtain unbiased responses, even when these relate to sensitive questions like tax compliance. Our study shows that potential bias exists for some tax-related questions, but not all of them. Moreover, given that this experiment was conducted with the full involvement of the tax authority, it shows the promise and perils of introducing experimentation and insights from behavioral science into revenue administration strategies when these go beyond simple “nudging” approaches (something the TRA has recently adopted) (see, for example, Pomeranz & Vila-Belda 2019, for a useful overview).

Our experiment is relevant within two strands of literature that document how increases in tax administration capacity on the ground can influence taxpayer behavior -particularly around compliance- and revenue collection more generally. An extensive literature documents the impact of increased audits -and the expectation of audits- on tax compliance (see, for example, Slemrod 2019 and Alm 2019 for a summary of studies). Increasing the expected probability of an audit can reduce evasion and improve payment compliance: for example, Bergolo et al. (2023) find letters to SMEs about audits increased tax payments in the short-term. However, actual audits can actually backfire, as highlighted in some recent field experiments (Beer et al., 2020; Erard et al., 2020; Gemmel and Ratto, 2012; Kotsogiannis et al., 2021). Audits might be viewed as unfair, and thus willingness to comply in the future might decrease (lower trust and tax morale) (Mendoza et al. 2017). Alternatively, being subject to an audit may lead to misperceptions of future audits (“Lightning never strikes in one place twice”), thus leading to lower compliance in the long-run. Finally, audits that do not fully uncover evasion (audits that underestimate true income) might reduce compliance along a similar vein, as documented in recent laboratory experiments (Kasper & Alm 2022 and Lancee et al. 2023).

A separate set of literature evaluates the role of local and regional taxpayer offices on compliance and collection. Okunogbe and Tourek (2024) document how tax officials can influence compliance and find that both the scale of tax administration (number of tax officers relative to the population) and their deployment can influence compliance and collection. On the scale of tax administration, a well-known study in Indonesia (Basri et al. 2021) studies the impact of the creation of medium taxpayer offices (MTOs) on compliance and finds that increasing the intensity of tax administration at the local level can increase compliance to corporate income tax. The authors conclude that the creation of these MTOs -whose objective was to simultaneously expand enforcement reach and facilitate compliance (through customer service) through increased local staff -led to sustainable, long-term impacts on tax filing and payment behavior, and they estimate that MTOs more than doubled revenue collection in the nine-year study period. On the deployment side, a study in Peru (Kapon et al. 2022) finds that Prioritized Iterative Enforcement (PIE) -where small groups of high risk tax payers are targeted in batches -can improve property tax collection by as much as 10 percent. Other studies look at how the assignment of tax officers to jurisdictions can improve compliance (Bergeron et al. 2023).

The remainder of the paper is organized as follows; section 2 will discuss the Tanzanian context in greater detail; section 3 will discuss the study design; section 4 will summarize the experimental impacts from the intervention (identified through the survey and administrative data, with validation from a follow-up survey); and section 5 concludes with a discussion on policy implications.

## 2 Context

Tanzania is classified as a lower-middle-income country with an annual per capita income of \$1,057.7 (constant 2015 US\$). Despite the challenges posed by the COVID-19 pandemic and ongoing geopolitical tensions, Tanzania’s economy grew by 5.2 percent in 2023. The country’s economy relies heavily on agriculture, which employs approximately 66 percent of the population and contributes 26.5 percent to the country’s GDP. Following agriculture, the business and trade services sector is the next most significant contributor, providing employment to 16 percent of the population and boasting a 21 percent GDP contribution. Despite the importance of the business and trade services sector, it is predominantly informal, which limits the scale and development of Tanzania’s formal private sector. The creation of new businesses remains remarkably low, with fewer than 0.2 new firms created per 1,000 adults annually (World Bank, 2023). This new business density rate is the lowest among comparable economies, including South Africa (12.5 new businesses per 1,000 adults), Rwanda (2.2), and Kenya (1.6).

Although tax revenue is the primary source of domestic resources, Tanzania's tax-to-GDP ratio remains relatively low at 11.4, compared to Africa's average of 15.6, Kenya's 15.2, and Rwanda's 17. Currently, approximately 4 million taxpayers are registered with the Tanzania Revenue Authority (TRA) and are thus tax-eligible. However, an overwhelming majority of these are classified as small firms, employing fewer than 10 individuals, and their contribution to domestic revenue taxes is minimal. These small firms typically pay personal income tax through the presumptive tax regime (presumptive taxpayers) or via standard personal income tax if they exceed the TZS 100 million turnover threshold. Medium-sized enterprises, on the other hand, contribute 18.8 percent, while large firms, despite being relatively few in number, dominate contributions, accounting for 58.7 percent of total business tax revenue. This disproportionate distribution of tax contributions was emphasized by the Minister of Finance in the 2022/2023 budget speech, who noted that, in 2021/2022, 80 percent of the TRA's revenue came from only 20 percent of business taxpayers, yielding a total of TZS

16.75 trillion.

Presumptive taxpayers are individuals taxed based on an estimate of their annual turnover, provided it does not exceed TZS 100 million (the presumptive tax schedule is provided in Table 1). They are not legally required to prepare or submit business records or audited accounts to the TRA unless they choose to do so. Once registered, presumptive taxpayers must visit the TRA annually for a tax assessment and receive a notice of estimated taxes. Estimates are based on annual turnover determined through interviews between TRA officials and the taxpayer, as well as a review of any available business records. The estimated tax is paid in four quarterly installments in March, June, September, and December. After the assessment, the taxpayer receives a notice of estimated taxes. When filing returns online, taxpayers can obtain a control number via the internet, but presumptive taxpayers typically are not required to file online. The generated control number, which contains the particular payment reference, helps taxpayers pay directly to the government.

Table 1: Presumptive Tax Schedule

<table><tr><td>Annual turnover</td><td>Tax payable when records are incomplete</td><td>Tax payable when records are complete</td></tr><tr><td>Where turnovers does not exceed Tshs 4,000,000</td><td>NIL</td><td>NIL</td></tr><tr><td>Where turnover exceeds Tshs 4,000,000/= but does not exceed Tshs 7,000,000</td><td>Tshs 100,000/=</td><td>3% of the turnover in excess of Tshs 4,000,000/=</td></tr><tr><td>Where turnover exceeds Tshs 7,000,000/= but does not exceeds Tshs 11,000,000/=</td><td>Tshs 250,000/=</td><td>Tshs 90,000/= plus 3% of the turnover in excess of Tshs 7,000,000/=</td></tr><tr><td>Where turnovers exceed Tshs. 11,000,000/= but does not exceed Tshs. 100,000,000/=</td><td colspan="2">3.5% of turnover</td></tr></table>

The underperformance of tax collection, especially among small businesses, reveals significant structural and compliance challenges. Joint research by the University of Dar es Salaam and the TRA indicates that many taxpayers who appear for tax reassessment in one year fail to return for reassessment in subsequent years. For instance, only 60 percent of assessed presumptive taxpayers returned the following year between 2014 and 2018. This problem was even more pronounced between 2018 and 2019, when only 45 percent of taxpayers reassessed in 2018 returned the next year. A longer-term perspective reveals that by 2019, just 41 percent of taxpayers assessed in 2014 remained within the government's tax base. Recognizing these challenges, the TRA has implemented several measures to improve compliance. Efforts have been directed toward simplifying the presumptive tax system, while awareness campaigns such as the "Door to Door" initiative have been introduced to enhance taxpayers' knowledge. These efforts have often been paired with self-service arrangements via the taxpayer portal and reminder messages sent to taxpayers regarding their tax obligations.

## 3 Study Design

This study involved 1,210 small and medium-sized businesses spread across urban and peri-urban areas in Tanzania. These businesses were randomly selected within each of their representative wards and can be considered representative of typical small and medium-size business in these locations, covering sectors such as retail and wholesale trade, manufacturing, education, accommodation and food service activities, human health and social work, and other services. The sample design ensured representation across different business sizes, including small businesses with 1–4 employees, medium-sized enterprises with up to 49 employees, and various economic activiti

[中间内容因长度限制已省略]

ance on correspondence audits. Taxpayer Advocate Service: Annual Report to Congress 2019, 257–268.

[8] Gemmell, N., & Ratto, M. (2012). Behavioral responses to taxpayer audits: Evidence from random taxpayer inquiries. National Tax Journal, 65(1), 33-58.

[9] Hoy, Christopher, Thiago Scot, Alex Oguso, Anna Custers, Daniel Zalo, Ruggero Doino, Jonathan Karver, and Nicolas Orgeira Pillai. 2024. “Trade-offs in the Design of Simpli-

fied Tax Regimes: Evidence from Sub-Saharan Africa.” World Bank Policy Research Working Paper 10909.

[10] Kapon, S., Del Carpio, L., & Chassang, S. (2022). Using divide-and-conquer to improve tax collection. NBER Working Paper No. 30218. National Bureau of Economic Research.

[11] Kasper, M., & Alm, J. (2022). Audits, audit effectiveness, and post-audit tax compliance. Journal of Economic Behavior & Organization. Tulane University Working Paper No. 2010.

[12] Lancee, B., Rossel, L., & Kasper, M. (2023). When the agency wants too much: Experimental evidence on unfair audits and tax compliance. Journal of Economic Behavior & Organization, 214, 406–442.

[13] Mendoza, J. P., Wielhouwer, J. L., & Kirchler, E. (2017). The backfiring effect of auditing on tax compliance. Journal of Economic Psychology, 62, 284–294.

[14] Okunogbe, O., & Tourek, G. (2024). How can lower-income countries collect more taxes? The role of technology, tax agents, and politics. Journal of Economic Perspectives, 38(1), 81–106.

[15] Slemrod, J. (2019). Tax compliance and enforcement. Journal of Economic Literature, 57(4), 904–954.

[16] World Bank. (2023). Privatizing growth: A country economic memorandum for the United Republic of Tanzania. World Bank.

Appendix 1: Balance Test - Surveyed Wards from Census

<table><tr><td rowspan="2"></td><td colspan="2">treatment-Control</td><td colspan="2">treatment-Treatment</td><td rowspan="2">Std Diff</td></tr><tr><td>Mean or N</td><td>SD or (%)</td><td>Mean or N</td><td>SD or (%)</td></tr><tr><td colspan="6">femalehead</td></tr><tr><td>0</td><td>144060</td><td>(65.1)</td><td>139650</td><td>(65.6)</td><td>0.00960</td></tr><tr><td>1</td><td>77103</td><td>(34.9)</td><td>73250</td><td>(34.4)</td><td></td></tr><tr><td colspan="6">primary</td></tr><tr><td>0</td><td>95059</td><td>(44.2)</td><td>93897</td><td>(44.3)</td><td>0.00372</td></tr><tr><td>1</td><td>120202</td><td>(55.8)</td><td>117846</td><td>(55.7)</td><td></td></tr><tr><td colspan="6">secondary</td></tr><tr><td>0</td><td>167945</td><td>(78.0)</td><td>165680</td><td>(78.2)</td><td>0.00548</td></tr><tr><td>1</td><td>47316</td><td>(22.0)</td><td>46063</td><td>(21.8)</td><td></td></tr><tr><td colspan="6">wage</td></tr><tr><td>0</td><td>188080</td><td>(85.0)</td><td>179976</td><td>(84.5)</td><td>0.01409</td></tr><tr><td>1</td><td>33083</td><td>(15.0)</td><td>32924</td><td>(15.5)</td><td></td></tr><tr><td colspan="6">agri</td></tr><tr><td>0</td><td>202903</td><td>(91.7)</td><td>196392</td><td>(92.2)</td><td>0.01852</td></tr><tr><td>1</td><td>18260</td><td>(8.3)</td><td>16508</td><td>(7.8)</td><td></td></tr><tr><td colspan="6">grass roof</td></tr><tr><td>0</td><td>212612</td><td>(96.1)</td><td>206143</td><td>(96.8)</td><td>0.03759</td></tr><tr><td>1</td><td>8551</td><td>(3.9)</td><td>6757</td><td>(3.2)</td><td></td></tr><tr><td colspan="6">mud wall</td></tr><tr><td>0</td><td>209481</td><td>(94.7)</td><td>201115</td><td>(94.5)</td><td>0.01120</td></tr><tr><td>1</td><td>11682</td><td>(5.3)</td><td>11785</td><td>(5.5)</td><td></td></tr><tr><td colspan="6">earth floor</td></tr><tr><td>0</td><td>185139</td><td>(83.7)</td><td>183365</td><td>(86.1)</td><td>0.06754</td></tr><tr><td>1</td><td>36024</td><td>(16.3)</td><td>29535</td><td>(13.9)</td><td></td></tr><tr><td colspan="6">improved w~r</td></tr><tr><td>0</td><td>29488</td><td>(13.3)</td><td>26003</td><td>(12.2)</td><td>0.03354</td></tr><tr><td>1</td><td>191675</td><td>(86.7)</td><td>186897</td><td>(87.8)</td><td></td></tr><tr><td colspan="6">electric</td></tr><tr><td>0</td><td>74763</td><td>(33.8)</td><td>65660</td><td>(30.8)</td><td>0.06340</td></tr><tr><td>1</td><td>146400</td><td>(66.2)</td><td>147240</td><td>(69.2)</td><td></td></tr></table>

Appendix 2: Balance Test - Surveyed Firms from Survey

<table><tr><td rowspan="2"></td><td colspan="2">treatment=Control</td><td colspan="2">treatment=Treatment</td><td rowspan="2">Std Diff</td></tr><tr><td>Mean or N</td><td>SD or (%)</td><td>Mean or N</td><td>SD or (%)</td></tr><tr><td>owner</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Not Owner</td><td>248</td><td>(40.7)</td><td>238</td><td>(39.7)</td><td>0.02018</td></tr><tr><td>Owner</td><td>362</td><td>(59.3)</td><td>362</td><td>(60.3)</td><td></td></tr><tr><td>soletrader</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>other</td><td>167</td><td>(27.4)</td><td>131</td><td>(21.8)</td><td>0.12898</td></tr><tr><td>soletrader</td><td>443</td><td>(72.6)</td><td>469</td><td>(78.2)</td><td></td></tr><tr><td>male</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Female</td><td>241</td><td>(39.5)</td><td>238</td><td>(39.7)</td><td>0.00324</td></tr><tr><td>Male</td><td>369</td><td>(60.5)</td><td>362</td><td>(60.3)</td><td></td></tr><tr><td>TObelow 1mil</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Above 1 mil</td><td>170</td><td>(27.9)</td><td>186</td><td>(31.0)</td><td>0.06874</td></tr><tr><td>Below 1 mil</td><td>440</td><td>(72.1)</td><td>414</td><td>(69.0)</td><td></td></tr><tr><td>wr trade</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Other</td><td>381</td><td>(62.5)</td><td>345</td><td>(57.5)</td><td>0.10135</td></tr><tr><td>Wholesale ~1</td><td>229</td><td>(37.5)</td><td>255</td><td>(42.5)</td><td></td></tr></table>
"""
