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
- 已识别机构名：`布鲁盖尔研究所`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份布鲁盖尔研究所研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Tales from a crisis: diverging narratives of the euro area

GERRET VON NORDHEIM (gerret.vonnordheim@tu-dortmund.de) is a researcher at Dortmund University

Henrik Müller, Giuseppe Porcaro and Gerret von Nordheim

## Executive summary

ECONOMIC ANALYSES LARGELY ignore Europe's fragmented public sphere, a feature that distinguishes the euro area from other major currency areas.

THIS POLICY CONTRIBUTION identifies how narratives of the crisis developed since 2007, by identifying the key crisis-related topics in articles from four opinion-forming newspapers in the largest euro-area countries (Germany's Süddeutsche Zeitung, France's Le Monde, Italy's La Stampa and Spain's El País). In particular, the analysis considers where blame for the crisis has been laid with the aim of informing the current debate on euro-area governance reform. Such an exercise can help to understand the difficulties euro-area policymakers face when it comes to formulating solutions that are both appropriate and commonly acceptable.

THE ANALYSIS SHOWED that Süddeutsche Zeitung blames everyone but Germany, the chief suspects being Greece and the European Central Bank; the paper stresses the need to return to a perceived status quo of stability and fairness. Le Monde blames everyone including the French political class, but largely refrains from criticism of European institutions such as the European Commission and the European Central Bank. La Stampa sees Italy as the victim of unfortunate circumstances, including the European Union austerity measures promoted by Germany, and Italy's own politicians. El País primarily blames Spain for misconduct during the boom years preceding the crisis.

THIS PICTURE OF differing narratives shows that each euro-area country faces different pressures from its respective public when discussing how to press ahead with effective euro-area governance reform. The global financial crisis and the subsequent recession had quite different effects in different euro-area countries. Therefore, it is unsurprising that the narratives differ in the four papers. National problems and solutions took centre stage in national discourses leaving systemic euro-area issues largely unmentioned.

## 1 Introduction

The global financial crisis that started in 2008 created considerable stress in the euro area. The common shock triggered different problems in each euro-area country. In Spain, for instance, the bursting of a housing bubble and a banking crisis strained the economy. In France and Italy, structural weaknesses, particularly in labour markets, were exposed. In Germany, an overreliance on exports for economic growth led to a particularly pronounced recession followed by a partial shift of exports to emerging markets, away from other euro-area countries.

Though national circumstances differed, there were common systemic deficiencies (Darvas, 2012). Compared with other major economies, the euro area struggled to deal with the crisis swiftly and, between 2010 and 2012, the currency area fought a sovereign debt crisis that only receded after the European Central Bank stepped in, assuring financial markets it would do “whatever it takes” to keep the euro afloat. Euro-area countries still struggle to answer the fundamental question of what happened and what steps need to be taken to prevent another crisis.

Disagreement about the causes and potential remedies appears to be the major obstacle to creating a more stable and crisis-proof set-up. The on-going debate about augmenting the euro area with new, potentially powerful institutions (see for example Wolff, 2017) is a case in point. The European Commission has pushed for reforms of the common currency area $^{1}$ , while French president Emmanuel Macron has made even more ambitious proposals. Some EU countries have resisted, or even been hostile, to these ideas. Against this backdrop it would be a surprise if the current debate yielded any meaningful institutional enhancements.

This paper focusses on an issue that is largely ignored by economic analyses: Europe's fragmented public sphere, a feature that distinguishes the euro area from other major currency areas. At the national level, public opinion is formed through mass media, which provides a platforms for public discourse (McCombs et al, 2017), but the European Union and the euro area lack a common public sphere (De Beus, 2010) $^{2}$ . In the context of the euro-area crisis, it has been argued that the lack of common European communication channels constitutes a missing link that holds back national discourses from converging on common framings when it comes to economic policy priorities (Müller, 2016).

Our analysis identifies historical trends in narrative building linked to the crisis in order to inform the current debate on euro-area governance reform. We analysed a set of newspaper articles published between 2007 and 2016 in the four biggest euro-area countries – Germany, France, Italy and Spain. We were able to observe the evolution of newspaper coverage of economic policy topics over time and to compare similarities and differences between countries.

Our specific objective is to dig deeper into the question of whether there is scapegoating underway in terms of responsibility for the crisis. More broadly, our analysis can help in understanding the difficulties euro-area policymakers face when it comes to formulating solutions that are both appropriate and commonly acceptable.

## 2 Methodology and data

Narrative-building is complex. It involves public opinion, media and politicians, among others (private sector, civil society, academics, etc). Following Shiller (2017), narratives can

1 European Commission president Jean-Claude Juncker outlined his vision in his 13 September 2017 State of the Union address to the European Parliament. See http:// europa.eu/rapid/press-re- lease\_SPEECH-17-3165\_ en.htm.

2 The implications of the absence of common EU media platforms have been a matter of intensive debate. Some studies come to the conclusion that fundamental problems for further integration may arise (Erikson, 2005); others find a cross-border convergence of discourses because of interaction between national media systems and the agenda-setting abilities of European institutions (eg Latzer and Saurwein, 2006).

be considered as central, though broadly disregarded, factors in forming economic behaviour in a social context. Narratives typically involve a sequence of events over time in which a set of antagonistic players interact, the formulation of a problem, moral judgements and possible solutions (Müller, 2017) $^{3}$ . Because of the highly complex nature of economic systems, the virtue of economic narratives lies in their capacity to reduce this complexity so that underlying developments become fathomable and discussable. Being social phenomena, shared economic narratives enable large groups of individuals to coordinate the processing of information. They can be interpreted as a specific form of social capital in an intangibles-rich economy (Haskel and Westlake, 2017). In a political context, narratives enhance the collective perception of social reality, thereby enabling societies to formulate political priorities. For example, British exceptionalism and the idea of a special relationship with the United States rather than the EU contributed to Brexit.

Discourses typically comprise a set of competing narratives. Over time dominant narratives tend to emerge, influencing the way a society views itself and forms its policy priorities. A discourse can thus be seen as an ensemble of ideas, concepts and categories through which meaning is given to social and physical phenomena, and which is produced and reproduced by means of an identifiable set of practices (Hajer and Versteeg, 2005). The discourse around migrants and refugees in Europe, for example, has translated into varying public attitudes and policy responses, and a general perception among the public that over-estimates the real number of refugees (Batsaikhan et al, 2018).

Therefore the narrative structure of discourses comes at a cost. Two types of problems might arise. First, like formal economic models, economic narratives focus on certain relationships while neglecting parts of the larger picture. If problematic developments occur outside the scope of dominant narratives, they may not be detected, and dealt with, in a timely fashion. Second, if different social groups are linked by common public goods while pursuing distinctly different, or even contradictory, narratives, they might find it hard to effectively manage those public goods. Take the case of net neutrality in the United States. One might think this would be a relatively benign, technocratic issue, but the polarisation of the positions around the topic has led to a sort of tribalisation of the debate around the topic $^{4}$ .

As Ostrom (1990) showed, communication between users of common resources is a key precondition for the development of institutional arrangements to overcome the ‘tragedy of the commons’, or the pursuit by individuals of self-interest. To have a positive effect on the cooperative abilities of groups of individuals, communication has to be based on a set of shared convictions, typically taking the form of economic narratives.

The empirical study of economic narratives is complicated by the fact that they often cannot be observed directly. Articles, TV programmes or speeches seldomly formulate a narrative explicitly but do so implicitly by relying on recipients' shared perceptions. One way to gauge narratives is the analysis of reporting patterns in mass media. Since major newspapers cater to the broader public they can be expected to reflected the prevailing economic narratives. As shown in von Nordheim et al (2018), they also take up dominant narratives from social media, albeit with considerable time-lags. The analysis of traditional newspapers therefore allows a glimpse at these complex communicative relationships. In this context, newspaper coverage is used as a proxy for narratives prevalent in the broader public debate. The analysis does not imply any kind of judgement on the reporting itself – it should not be read as a critique of media bias but rather as a representation of public debates.

Numerous studies have compared national elite newspapers' coverage of the EU (eg Trenz, 2004; Brüggemann and Kleinen-von Königslöw, 2009; Veltri, 2012). For our purposes, we chose one newspaper per major euro-area country: Süddeutsche Zeitung (Germany), Le Monde (France), La Stampa (Italy) and El País (Spain). All are elite newspapers recognised as opinion forming in their respective countries. All four have a centrist or slightly left-of-centre leaning, enabling analysis of different narratives within comparable worldviews. Box 1 details our dataset and approach.

## Box 1: Search parameters

We used search words related to economic crisis to extract the relevant body of articles. Search words used: in German: ‘Eurokrise,’ ‘Finanzkrise,’ ‘Wirtschaftskrise’; in French: ‘crise de l’euro,’ ‘crise financière,’ ‘crise économique’; in Italian: ‘crisi dell’euro,’ ‘Crisi finanziaria,’ ‘crisi economica,’ ‘Crisi dei subprime,’ ‘Grande recessione’; in Spanish: ‘crisis del euro,’ ‘crisis financiera,’ ‘crisis económico,’ ‘grande recessione’.

This resulted in a dataset of 51,714 news articles: 16,486 articles from Süddeutsche Zeitung, 9,566 from Le Monde, 6,416 from La Stampa and 19,246 from El País.

We applied an algorithmic topic modelling approach known as Latent Dirichlet Allocation (LDA; Blei et al, 2003). This methodology, applied to words collected into documents, considers that each document is a mixture of a small number of topics and that each word's creation is attributable to one of the document's topics.

Our utilisation of LDA is meant to reveal reporting patterns in different countries over time. The algorithmic nature of the quantitative analysis allows us to process texts irrespective of language. However, the algorithm merely sorts the content, but doesn't understand it; human researchers remain vital to the analysis.

As a first step we ran an LDA with the parameters set to produce 30 topics for each of the four newspapers. These topics were then labelled by close-reading of representative articles selected by the algorithm. We developed a taxonomy to match related topics in different languages by comparing the semantics of top words as produced by the algorithm. As a result, we were able to identify topics related to the causes of the crisis, the way these topics interlink with each other, and the main players in all four countries. We also found blank spaces representing topics that were missing in some national debates while they were present in others.

To get closer to answering the question of who is blamed for the euro crisis, we took the analysis further by creating a ‘blaming dictionary,’ made up of lists containing 140 words that attribute responsibility to entities, persons, institutions and systems. We then applied these lists to the relevant topics, revealing the extent of scapegoating about the crisis as portrayed in the sample dataset we analysed.

## 3 Findings

Following the notion that narrative building is about the evolution of discourses over time, involving distinct events and players, we focus on a set of comparable topics in all four newspapers. They can be clustered into two categories: institutions and systemic topics.

In terms of institutions, crisis-related topics comprise the following:

\- Greece/southern Europe: overdebtedness as a result of fiscal irresponsibility and general over-leverage;

• Germany/the troika: austerity policies imposed by the institutions (EU, European

Financial Stability Facility/European Stability Mechanism, International Monetary Fund, European Central Bank) on debtor countries, demanded primarily by Germany;

\- Government: the respective newspaper's national government for mishandling the economy before and during the crisis;

\- Banking: banks' and other financial institutions' practices that were at the core of the crisis, the banking-state link in terms solvency being a recurrent issue during the crisis and its aftermath;

\- Markets: exuberant capital markets mispricing risk and frequently undershooting in terms of solvency assessments, leading to vicious spirals;

\- EU: Brussels institutions not being willing or able to put the right remedies in place, be they stricter oversight of national budgets or misguided subsidy schemes;

\- ECB: the European Central Bank for being reluctant to act aggressively, or for being too aggressive.

Note that each topic might be viewed from different perspectives. For instance, Germany and the troika institutions might be criticised by one newspaper article for being too strict, while they are criticised for being too soft in another. Greece's overspending might be attributed to the country's reliance on the willingness of euro-area partners to bail it out, but it might also be highlighted for dragging down less-vulnerable countries as well because of contagion effects. Thus, one entity might be blamed for different, sometimes contradictory, reasons.

One interesting result is the prevalence of what we call systemic topics in all the newspapers analysed. These topics are evidence of the dominant overall framing of the crisis in the respective publication. Systemic topics are typically included in opinion pieces such as commentaries, op-eds, interviews or book reviews. They are at the core of the debate about the broader meaning and consequences of the economic and financial crisis as it spilled over into a wider societal, political and cultural spectrum.

There are several common elements in the groups of articles analysed. In each newspaper there is a clear indication that the economic crisis led to a political crisis and a crisis of values, provoking specific feelings and leading to the naming of scapegoats. Close reading of typical articles within the respective systemic topics reveals a sense of gloom in all the newspapers, though there are notable differences. The Italian, Spanish and, to some extent, French newspapers convey a generalised loss of hope resulting from a downgraded long-term outlook, a fear of the end of European integration and even the death of democracy. The German discourse as represented by the Süddeutsche Zeitung is rather technocratic.

To give some examples, the systemic topics contain typical phrases such as:

\- Pour la première fois depuis 1945, l'idée d'avenir est en crise en Europe (For the first time since 1945, the idea of the future is in crisis in Europe) – Le Monde, 28 May 2011

\- Crisis de confianza (crisis of trust) – El País, 16 June 2011

\- Resa, perdita di futuro, incapacità di reinventarlo (Defeat, loss of future, incapacity of re-invent the future) – La Stampa, 10 May 2014.

\- Die Finanzkrise hat Vertrauen zerstört (The financial crisis has destroyed trust) – Süddeutsche Zeitung 16 July 2009.

The notion of broken social values is common to the narratives in all the newspapers. They all mention democracy as a value that is being severely damaged by the crisis. Le Monde speaks about the “dream of egalitarian emancipation” being broken (17 January 2010). La Stampa detects an overall sense of decadence that could be compared to the Byzantine Empire (7 February 2009). Süddeutsche Zeitung ponders the possibility of violent upheavels but tends to dismiss such a revolutionary scenario, trusting Germany’s institutions to be

able to weather the storm (25 April 2009) $^{4}$ . Overall, the following general narratives can be identified:

Süddeutsche Zeitung considers a departure from the traditional West German social market economy model as a chief underlying cause of the crisis. In line with this view, Süddeutsche Zeitung maintains that the increasing dominance of financial markets and, correspondingly, of shareholders' interests has led to an economy prone to severe slumps and crashes (22 December 2008). During the course of the debate though, and at the time when Germany enjoyed a strong upswing starting in late 2009 that distinguished it from the rest of the euro area, the focus shifted to the issue of inequality of income and wealth. From such a diagnosis follows a call to return to stability and fairness through regulation and redistribution. Financial prudence is of the essence in domestic and European economic policies. As Figure 1 shows, at the outset of the crisis, Süddeutsche Zeitung blamed bankers with particular intensity. Subsequently, much attention was devoted 

[中间内容因长度限制已省略]

misconduct during the boom years preceding the crisis.

The global financial crisis and the subsequent recession had quite different effects in different euro-area countries. Therefore, it is unsurprising that we find different reporting patterns in the four papers. National problems and solutions took centre-stage in national discourses leaving systemic euro-area issues largely unmentioned. Where these issues were raised, they were dealt with from a distinctly national point of view. The coverage of the ECB (section 4) is a case in point. A transnational consensus view on the causes and consequences of the euro-area crisis – in other words, a common economic narrative on the risks faced by the euro area – is missing. This impedes the emergence of a common body of public opinion as the basis for a debate around the reform agenda for the euro area as a whole.

Our findings correspond with the countries' economic policies during and after the euro-area crisis. Germany's insistence on fiscal prudence, its tough stance on Greece and its (initial) opposition to accommodating ECB policies are in line with the discourses we found in the data. The resignation in 2011 of Germany's member of the ECB board, for instance, was an example of how such differing narratives have had consequences in policymaking $^{6}$ . The French government's passive role during the euro crisis was mirrored in the self-perception in Le Monde of secular decline and weakness. Italy's reluctance to reform can be associated with the apparent belief in being victimised. Spain, in contrast, drew hard lessons from rigorous self-analysis, which led it to pursue tough structural reforms, such as cleaning up the banking sector and liberalising the labour market (OECD, 2017), while paying little attention to the requirements of, say, EU deficit rules.

The picture of differing public spheres shows that each euro-area country faces different pressures from their respective publics when discussing how to press ahead with sensible and comprehensive institutional euro-area governance reforms.

Still, two caveats seem warranted. First, we chose just one centrist newspaper per country, assuming they would represent a large part of the respective public sphere. Further research needs to include a complete set of right-of-centre and left-of-centre newspapers, though this might produce even more pronounced divergences between countries. Second, we entered uncharted territory as far as the inter-lingual algorithm-based content analysis and the application of a ‘blaming dictionary’ are concerned. Both methods look promising but need further verification and refinement.

## References

Batsaikhan, U., Z. Darvas and I. Goncalves Raposo (2018) People on the move: Migration and mobility in the European Union, Blueprint 28, Bruegel

Blei, D.M., A.Y. Ng and M.I. Jordan (2003) 'Latent Dirichlet Allocation', Journal of Machine Learning Research 3 (4–5): 993–1022

Brüggemann, M. and K. Kleinen-von Königslöw (2009) 'Let's Talk about Europe: Why Europeanization Shows a Different Face in Different Newspapers', European Journal of Communication 24(27): 27-48

Darvas, Z. (2012) 'The euro crisis: ten roots, but fewer solutions', Policy Contribution 2012/17, Bruegel

De Beus, J. (2010) 'The European Union and the Public Sphere: Conceptual Issues, Political Tensions, Moral Concerns, and Empirical Questions', in R. Koopmans and P. Statham (eds) The Making of a European Public Sphere: Media Discourse and Political Contention, Cambridge University Press

Entman, R. M. (1993) 'Framing. Towards a Clarification of a Fractured Paradigm', Journal of Communication 43(4): 51-58

Erikson, E.O. (2005) 'An emerging European public sphere', European Journal of Social Theory 8(3): 341-363

Hajer, M. and W. Versteeg (2005) 'A decade of discourse analysis of environmental politics: achievements, challenges, perspectives', Journal of Environmental Policy & Planning 7(3): 175-184

Haskel, J. and S. Westlake (2017) Capitalism without Capital: The Rise of the Intangible Economy, Princeton University Press

Latzer, M. and F. Saurwein (2006) 'Europäisierung durch Medien: Ansätze und Erkenntnisse der Öffentlichkeitsforschung', in W.R. Langbucher and M. Latzer (eds) Europäische Öffentlichkeit und medialaer Wandel: Eine transdisziplinäre Perspektive, Wiesbaden: VS Verlag für Sozialwissenschaften

McCombs, M.E., E.F. Einsiedel and D.H. Weaver (2017) Contemporary Public Opinion: Issues and the News, London: Routledge

Müller, H. (2016) Fighting Europe's Crisis with Innovative Media: a Modest Proposal, Journal of Business and Economics, September 2016, Volume 7, No. 9, pp. 1399-1409

Müller, H. (2017) 'Funktion und Selbstverständnis des wirtschaftspolitischen Journalismus,' in K. Otto and A. Köhler (eds) Qualität im wirtschaftspolitischen Journalismus, Springer

OECD (2017) Economic Survey of Spain, March

Ostrom, E. (1990) Governing the Commons, Cambridge University Press

Shiller R.J. (2017) 'Narrative Economics', NBER Working Paper 23075, National Bureau of Economic Research

Trenz, H-J. (2004) 'Media Coverage on European Governance. Exploring the European Public Sphere in National Quality Newspapers', European Journal of Communication 19(3): 291–319

Veltri, G.A. (2012) 'Information flows and centrality among elite European newspapers', European Journal of Communication 27(4): 354-375

Von Nordheim, G., K. Boczek, L. Koppers and E. Erdmann (2018) 'Reuniting a Divided Public? Tracing the TTIP Debate on Twitter and in Traditional Media,' International Journal of Communication, 12 (2018): 548–569

Wolff, G.B. (2017) 'Beyond the Juncker and Schäuble visions of euro-area governance', Policy Brief 2017/06, Bruegel
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
