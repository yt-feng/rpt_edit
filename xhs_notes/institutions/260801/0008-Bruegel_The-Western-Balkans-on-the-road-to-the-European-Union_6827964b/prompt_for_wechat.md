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
# The Western Balkans on the road to the European Union

Marek Dabrowski and Yana Myachenkova

MAREK DABROWSKI
(marek.dabrowski@bruegel.org) is a Non-resident
Fellow at Bruegel

YANA MYACHENKOVA (yana.myachenkova@bruegel.org) is a research assistant at Bruegel

The authors would like to thank Alexander Lehmann, J. Scott Marcus, André Sapir, Alessio Terzi, Nicolas Véron, Guntram Wolff and Georg Zachmann for their comments on an earlier version of this paper.

## Executive summary

IN THE 1990s, the Western Balkan region suffered from severe conflicts, which ended after intervention by United Nations and NATO forces and with the promise of accession to the European Union. In the early and mid-2000s, the prospect of EU accession and the global boom facilitated rapid economic recovery in the Western Balkans and boosted economic and institutional reforms. However, the global financial crisis of 2007-09 and the European crisis of 2010-13 slowed the pace of economic growth and amplified high unemployment. In addition, various unresolved legacies from past conflicts slowed the pace of reform and progress towards EU accession.

THE EUROPEAN COMMISSION in February 2018 set an indicative deadline (2025) for admission to the EU of the two most advanced candidates – Serbia and Montenegro. This could incentivise all Western Balkan countries, including those candidates that have not yet started membership negotiations (Macedonia and Albania) and those waiting for candidate status (Bosnia and Herzegovina and Kosovo), to remove domestic political obstacles to EU accession, solve conflicts with neighbours, speed up reforms and accelerate economic growth.

THE EUROPEAN UNION and its member states must not overlook the strategic importance of the Western Balkan region. Geographically, Western Balkan countries form a land bridge and the shortest transit route between the south-east flank of the EU and its central European core. The importance of this transit route was demonstrated during the 2015-16 refugee crisis. Furthermore, Western Balkan economies are already closely integrated with the EU. The EU is their largest trade partner, largest source of incoming foreign investment and other financial flows, and the main destination for outward migration.

## 1 Introduction

The Western Balkans is a geopolitical term coined by the governing bodies of the European Union in the early 2000s and referring to those countries in south-eastern Europe that were not EU members or candidates at the time but could aspire to join the bloc. Originally, the Western Balkan region consisted of seven countries – Albania, Bosnia and Herzegovina, Croatia, Kosovo, Macedonia $^{1}$ , Montenegro and Serbia – but Croatia has since joined the EU.

In the 1990s, the region suffered from severe conflicts that had negative political and economic consequences that continue to be felt. In the early and mid-2000s, the prospect of EU accession and the global boom facilitated rapid economic recovery and boosted economic and institutional reforms in the region. However, the global financial crisis of 2007-09 and the subsequent European financial crisis of 2010-13 (that affected in particular the southern flank of the EU) slowed down the pace of economic growth in the region, and amplified high unemployment, especially among young people. In addition, various unresolved legacies from past conflicts slowed the pace of reform and progress towards EU accession in Western Balkan counties, and intensified nationalist sentiments across the region.

Given its geographical location, the region is important to the EU in terms of security, stability, trade and transit routes. Therefore, the Western Balkan countries' economic and political prospects, and their future within a European framework, should remain one of the top priorities for the EU.

This Policy Contribution concentrates on economic and social development in the region, and the economic and institutional aspects of EU accession (sections 3-6) $^{2}$ . Naturally, we also take political and geopolitical factors into consideration (section 2) but as the background rather than central theme of our analysis. We conclude (section 7) with broad recommendations pertinent to the possible eventual EU accession of Western Balkan countries.

## 2 Conflict legacies and geopolitics

Between 1918 and 1991, all Western Balkan countries except Albania were part of Yugoslavia. After the second world war, similarly to most of their central and eastern European neighbours, the countries were under communist rule. However, in 1948 Yugoslavia split with the Soviet Union and remained independent from major geopolitical and military blocs in Europe, becoming one of the founders of the Non-Aligned Movement. After 1950, Yugoslavia developed a unique decentralised market socialism model based on employee-managed firms. Although this did not protect the country from macroeconomic disequilibria (repeated episodes of high inflation and hyperinflation, large external debt and high unemployment) it allowed the creation of quasi-market institutions and market-oriented microeconomic behaviour. Unlike countries of the Soviet bloc, Yugoslavia remained relatively open to the world in terms of trade and its citizens' freedom to travel.

By contrast, Albania, which also split with the Soviet Union in 1962, chose an orthodox model of a centrally planned economy, based on national self-sufficiency and closed to the outside world.

When Yugoslavia began to collapse in 1991, most of its successor states suffered from violent ethnic conflicts, which negatively affected the entire region in terms of war damage, human suffering, disrupted trade links, refugee flows, sanctions, organised crime and so on. The series of civil wars in the region, which lasted throughout the 1990s, was stopped only by the intervention of United Nations and North Atlantic Treaty Organisation (NATO) forces and the EU's generous promise to allow countries in the region to apply for EU membership once they re-established peace and met accession criteria. The prospect of European integration helped to start the process of economic and political reforms, although at various speeds in different countries, and to largely normalise economic and political relations in the region.

However, the legacies of past conflicts continue to overshadow regional politics and economics, and to create obstacles in Western Balkan countries to EU integration.

First, Serbia, five EU member states (Cyprus, Greece, Romania, Slovakia and Spain) and several other countries $^{3}$ do not recognise Kosovo as an independent state. Internally, Kosovo has failed to build peaceful relationships between the Albanian majority and Serbian minority, and its domestic stability relies on international peacekeeping forces.

Second, Bosnia and Herzegovina, where the civil war was brought to an end by the Dayton Agreement in 1995, is a very loose two-tier confederation of three ethnic communities that is hardly manageable at the central level (ICG, 2012). Politics in those communities continues to be dominated by nationalist sentiments. As a result, the international community must continue its peacekeeping mission and state-building support more than 20 years after the end of the war.

Third, Greece disputes Macedonia's country name $^{4}$ and this conflict has frozen the country's EU and NATO accession process for more than decade. Internally, Macedonia has suffered periodically from ethnic tensions between the Macedonian majority and the Albanian minority. Furthermore, the ten-year term of former prime minister Nikola Gruevski (1996-2006) was marred by numerous violations of the rule of law and political and civil liberties.

All countries in the region face problems with corruption (see section 5) and organised crime. The roots of the latter can be tracked back, at least partly, to the conflicts of 1990s and the resulting UN sanctions.

All the above-mentioned legacies of past conflicts contribute to the slow pace of the EU accession process in the region. In addition, EU members' appetites for further enlargement have been reduced by the financial crisis years (2007-13) and associated social and political tensions, the wave of Euroscepticism and nationalism, and Brexit.

However, there are signs of a changing atmosphere. First, in his State of the Union Address of 13 September 2017 $^{5}$ , European Commission president Jean-Claude Juncker recognised the strategic importance of further enlargement once the candidate countries meet the accession criteria. Second, the new enhanced Western Balkan strategy elaborated by the European Commission (2018) sets 2025 as a possible time horizon for Montenegrin and Serbian accession.

This is good news because the slow pace of the accession process and the lack of enthusiasm among current EU members to accept new entrants might weaken incentives for further reforms in Western Balkan countries, reverse those already in place and derail the enlargement process, as already happened partly with Turkey. In turn, this could mean a serious risk of a new round of intra-regional conflicts $^{6}$ , and geopolitical destabilisation in the EU's closest neighbourhood.

Faced by such risks, the EU and its member states must not overlook the strategic importance of the Western Balkan region.

Geographically, Western Balkan countries form a land bridge and the shortest transit route between the south-east flank of the EU (Greece, Bulgaria and Romania) and its central European ‘core’ (Hungary, Croatia, Slovenia and Austria). The importance of this transit area was demonstrated during the 2015-16 refugee crisis. Close cooperation between the Western Balkan governments and the EU played a major role in closing the Balkan route to refugee flows.

Because of its geographical location, and long and complicated land borders with its Western Balkan neighbours, Croatia could be the major beneficiary of further enlargement. The only road connection between its southern and central parts (the Adriatic highway) goes through the territory of Bosnia and Herzegovina, which is an obstacle to Croatia joining the Schengen area.

Economically, the EU is the largest trade partner of the Western Balkan countries, the main source of inward foreign direct investment and the main destination for outward labour migration (section 4). Many European countries have a sizeable Western Balkan diaspora.

The geopolitical vacuum created by the delayed prospect of EU membership and decreasing EU interest in the region could also encourage other players, such as Russia and China (Fouere, 2017), to become more active. To limited extent, this has already happened. China finances an increasing number of infrastructure projects throughout central and eastern Europe, including Western Balkans (Kynge and Peel, 2017; Byrne and Mitchell, 2017).

Russia's engagement in the region concentrates on geopolitical goals. In particular, Russia wants to discourage Western Balkan countries from joining NATO and is not enthusiastic about their EU membership bids. Serbia is a major target for Russian efforts because of historical and cultural links between the two countries (Hartwell and Sidlo, 2017). However, Serbia has been reluctant to take any step that would damage its EU accession prospects and openly distance it from mainstream EU foreign policy. The exception in this respect is its refusal to join EU sanctions against Russia (in retaliation for the annexation of Crimea and Russia's involvement in the Donbass conflict).

Beyond Serbia, there was some evidence of Russia's involvement in the failed coup plot in Montenegro in October 2016, which was seen by the ruling Democratic Party of Socialists as the attempt to stop Montenegro's accession to NATO (Hopkins, 2017).

Turkey, another historical player in the region, is active in the economic and cultural sphere, especially in Albania, Kosovo and Bosnia and Herzegovina. It also has the ambition playoff playing an active peacebuilding role in the region (Bechev, 2012).

## 3 Macroeconomic and social performance

## 3.1 Income per capita

In 2016, all Western Balkan countries except Kosovo were classified according to the World Bank Atlas method as upper middle-income countries. This category includes countries with gross national income (GNI) per capita between \$3,956 and \$12,235. However, most Western Balkan countries are towards the bottom of this income group – between \$4,180 in Albania and \$5,310 in Serbia. Even Montenegro with the region’s highest GNI per capita (\$7,120) recorded approximately only one sixth of German and one fifth of EU average GNI per capita. Kosovo, the region’s poorest country with GNI per capita of \$3,850, belonged to a lower middle-income economy group.

Nevertheless, since 2000 the Western Balkan region has seen income per-capita convergence towards Western European levels, represented in our analysis by Germany $^{7}$ (Figure 1).

Figure 1: GDP per capita in current international \$, PPP adjusted, Germany = 100%, 2000-16  
![](images/ed9cf4761e4289b0c50287a07a36be48c990c0c7f7053714ca37a3c377269b65.jpg)  
Source: World Economic Outlook database, October 2017. Note: IMF staff estimates for Kosovo (the entire period), Albania (2012-16) and Montenegro (2016)

Figure 2: Real GDP growth, annual percent change, 2000-16  
![](images/fee9126bff6671a2f90ea3de36417a7aa6a167777b091b58d59fa88f71390685.jpg)  
Source: World Economic Outlook database, October 2017.

The income convergence process was particularly strong between 2000 and 2009, on the back of rapid economic growth in the region (Figure 2) and the global economic boom. The gap in income per-capita levels in purchasing power parity (PPP) between Serbia and Germany narrowed by 10.5 percentage points, between Albania and Germany by 9.1 percentage points and between Montenegro and Germany by 7.7 percentage points. Other countries converged at a slower pace – Bosnia and Herzegovina by 5.6 percentage points, Macedonia by 4.7 percentage points and Kosovo by only 2.2 percentage points. After 2010, convergence slowed as a result of the spillover effects of the global and European financial crises. The 2010-12 period brought even de-convergence, compared to the 2009 relative income per capita level. Since 2012-13, convergence has restarted but at slower pace than in the 2000s. By 2016, Bosnia and Herzegovina and Serbia had still not managed to regain the relative income per capita level (as compared to Germany) of 2009.

Overall, between 2000 and 2016 Albania saw the biggest progress in income per capita convergence (by 10.5 percentage points) followed by Serbia (9.6 percentage points), Montenegro (8.3 percentage points), Macedonia (6.2 percentage points), Bosnia and Herzegovina (5.3 percentage points) and Kosovo (3.4 percentage points). The political and geopolitical factors discussed in section 2 have had at least partial impacts on the observed differences in the pace of convergence.

## 3.2 Social challenges

Despite progress in income convergence, the Western Balkan region continues to face social risks associated with poverty, income inequality, unemployment – especially among young people – and other forms of social exclusion.

Table 1 shows there has been some progress in the Western Balkans since 2001 in reducing poverty gaps $^{8}$ at 1.90, 3.20 and 5.50 a day (in 2011 PPP). For Macedonia, the proportion of people living below the thresholds of 1.90 and 3.20 almost halved after 2010. Substantial reductions in the percentage of people living below the thresholds of 3.20 and 5.50 a day were also accomplished in Kosovo (2013 compared to 2005). In Serbia, the percentage of people living below all three thresholds was largely unchanged between 2002 and 2013. In Montenegro, there was even some deterioration for the highest threshold, probably as result of the global and European financial crises. However, in both Serbia and Montenegro, poverty figures remain low compared to their Western Balkan neighbours.

Table 1: Poverty gap at \$1.90, \$3.20 and \$5.50 a day (2011 PPP), in percent

<table><tr><td>Poverty gap at</td><td colspan="3">$1.90 a day</td><td colspan="3">$3.20 a day</td><td colspan="3">$5.50 a day</td></tr><tr><td></td><td>2005</td><td>2010</td><td>2013</td><td>2005</td><td>2010</td><td>2013</td><td>2005</td><td>2010</td><td>2013</td></tr><tr><td>Albania</td><td>0.2</td><td> $0.1^b$ </td><td> $0.2^d$ </td><td>2.2</td><td> $1.1^b$ </td><td> $1.6^d$ </td><td>12.4</td><td> $9.0^b$ </td><td> $10.3^d$ </td></tr><tr><td>Bosnia &amp; Herzegovina</td><td> $0.1^a$ </td><td> $0.0^c$ </td><td></td><td> $0.2^a$ </td><td> $0.1^c$ </td><td></td><td> $1.0^a$ </td><td> $0.8^c$ </td><td></td></tr><tr><td>Macedonia</td><td></td><td>4.3</td><td>3.5</td><td></td><td>8.0</td><td>6.5</td><td></td><td>15.9</td><td>13.0</td></tr><tr><td>Kosovo</td><td>0.6</td><td>0.3</td><td>0.2</td><td>4.2</td><td>2.8</td><td>0.9</td><td>17.7</td><td>13.9</td><td>5.8</td></tr><tr><td>Montenegro</td><td>0.1</td><td>0.0</td><td>0.2</td><td>0.3</td><td>0.1</td><td>0.9</td><td>2.1</td><td>0.8</td><td>2.4</td></tr><tr><td>Serbia</td><td>0.3</td><td>0.0</td><td>0.0</td><td>1.1</td><td>0.3</td><td>0.3</td><td>5.0</td><td>2.1</td><td>2.0</td></tr></table>

Source: World Bank's World Development Indicators. Note: a = 2004, b = 2008, c = 2011, d = 2012. See footnote 8 for poverty gap definition.

In terms of income inequality, the region does not differ from the rest of Europe, ie its Gini index represents a moderate level. The exception was Macedonia in 2010, where a high Gini index of 42.8 was recorded (Figure 3), but it declined to 28.5 in 2013. Changes in the Gini index in the region have not followed a single trend: it has remained broadly stable in Albania and Bosnia and Herzegovina, but has fluctuated somewhat in other countries. World Bank (2017) attributes these trends to problems with job creation prior to 2009, combined with low productivity in most sectors.

This points to the inefficiency of labour market institutions in Western Balkan countries, one of the legacies of employee self-management in the former Yugoslavia (Roaf et al, 2014). As a result, the region has been always characterised by very high unemployment rates, even before the transition started.

Figure 4 shows that in 2001, the unemployment rate in Kosovo approached 60 percent of the labour force. Since then, Kosovo's labour market had improved: its unemployment rate in 2016 was only half the 2001 level, but still close to 30 percent. Macedonia has been the Western Balkans' second-highest unemployment country, with the unemploym

[中间内容因长度限制已省略]

al institutional reforms before admitting more members, most of which would be small countries.

## References

Bechev, D. (2012) 'The Periphery of the periphery: the Western Balkans and the Euro Crisis', Policy Brief ECFR/60, European Council on Foreign Relations, available at http://www.ecfr.eu/publications/summary/the\_periphery\_of\_the\_periphery\_the\_western\_balkans\_and\_the\_euro\_crisis

Byrne, A. and T. Mitchell (2017) 'Eastern Europe welcomes China investment promise', Financial Times, 28 November

Council of the European Union (2003) 'Thessaloniki European Council 19 and 20 June 2003: Presidency Conclusions', Document 11638/03, available at http://www.consilium.europa.eu/uedocs/cms\_data/docs/pressdata/en/ec/76279.pdf

Estrin, S. and M. Uvalic (2016) 'Foreign direct investment in the Western Balkans: what role has it played during transition?' Comparative Economic Studies 58(3): 455-483

European Commission (2018) 'A credible enlargement perspective for and enhanced EU engagement with the Western Balkans', Communication COM(2018) 65 final, available at https://ec.europa.eu/commission/sites/beta-political/files/communication-credible-enlargement-perspective-western-balkans\_en.pdf

Evans, D., P. Holmes, L. Iacovone and S. Robinson (2004) 'A Framework for Evaluating Regional Trade Agreements: Deep Integration and New Regionalism', University of Sussex, mimeo

Fouere, E. (2017) 'Western Balkans and the EU: Still in stand-by', Commentary, Italian Institute for International Political Studies, 10 July, available at http://www.ispionline.it/en/pubblicazione/western-balkans-and-eu-still-stand-17166

Gligorov, V. (2018) 'Disagreeing about Alexander the Great is embarrassing', News & Opinions, The Vienna Institute for International Economic Studies, 16 February, available at https://wiiw.ac.at/disagreeing-about-alexander-the-great-is-embarrassing-n-285.html

Hartwell, C. and K. Sidlo (2017) Serbia's cooperation with China, the European Union, Russia and the United States of America, study for the European Parliament, Directorate-General for External Policies, available at http://www.europarl.europa.eu/cmsdata/133504/Serbia%20cooperation%20with%20China,%20the%20EU,%20Russia%20and%20the%20USA.pdf

Hopkins, V. (2017) 'Indictment tells murky Montenegrin coup tale,' Politico, 23 May, available at https://www.politico.eu/article/montenegro-nato-milo-dukanovicmurky-coup-plot/

Hunya, G. and M. Schwarzhappel (2016) FDI in Central, East and Southeast Europe: Slump despite Global Upturn, FDI Report 2016, The Vienna Institute for International Economic Studies, available at https://wiw.ac.at/slump-despite-global-upturn-dlp-3899.pdf

ICG (2012) 'Bosnia's Gordian Knot: Constitutional Reform,' Europe Brief 68, International Crisis Group, available at https://www.crisisgroup.org/file/1377/download?token=-5jv1Ew8

IMF (2016) Annual Report on Exchange Arrangements and Exchange Restrictions 2016, International Monetary Fund, Washington DC, available at https://www.imf.org/\~/media/Files/Publications/AREAER/AREAER\_2016\_Overview.ashx

IMF (2017a) 'Albania: 2017 Article IV Consultation-Press Release; Staff Report; and Statement by the

Executive Director for Albania', IMF Country Report No. 17/373, International Monetary Fund, available at http://www.imf.org/-/media/Files/Publications/CR/2017/cr17373.ashx

IMF (2017b) 'Former Yugoslav Republic of Macedonia: 2017 Article IV Consultation-Press Release; Staff Report; and Statement by the Executive Director for the Former Yugoslav Republic of Macedonia', IMF Country Report No. 17/354, International Monetary Fund, available at http://www.imf.org/\~/media/Files/Publications/CR/2017/cr17354.ashx

IMF (2017c) 'Republic of Serbia: 2017 Article IV Consultation, Seventh Review Under the Stand-by Arrangement and Modification of Performance Criteria - Press Release; Staff Report; and Statement by the Executive Director for the Republic of Serbia,' IMF Country Report No. 17/263, International Monetary Fund, available at http://www.imf.org/\~media/Files/Publications/CR/2017/cr17263.ashx

Koen, V. and P. De Masi (1997) 'Prices in Transition: Ten Stylized Facts', IMF Working Papers WP/97/158, International Monetary Fund, available at http://www.imf.org/\~/media/Websites/IMF/imported-full-text-pdf/external/pubs/ft/wp/\_wp97158.ashx

Koettl-Brodmann, J., S. Johansson de Silva and O. Kupets (2017) Firm dynamics and job creation in the former Yugoslav Republic of Macedonia, Report Number 112197-MK, World Bank Group, Washington DC, available at http://documents.worldbank.org/curated/en/982121498623703665/pdf/112197-WP-P133003-PUBLIC-27-6-2017-13-30-59-MKDReportLaborDemandAnalysisFinal.pdf

Kynge, J. and M. Peel (2017) 'Brussels rattled as China reaches out to eastern Europe', Financial Times, 27 November

Roaf, J., R. Atoyan, B. Joshi, K. Krogulski and an IMF Staff Team (2014) 25 Years of Transition: Post-Communist Europe and the IMF, International Monetary Fund, available at http://www.imf.org/external/region/bal/rr/2014/25\_years\_of\_transition.pdf

Sanfey, P., J. Milatovic and A. Kresic (2016) 'How the Western Balkans can catch up', EBRD Working Paper No. 186, European Bank for Reconstruction and Development, available at http://www.ebrd.com/documents/oce/pdf-working-paper-186.pdf

Stehrer, R. and M. Holzner (2018) 'Western Balkan countries knocking on EU's door', News & Opinions, The Vienna Institute for International Economic Studies, 5 February, available at https://wiw.ac.at/n-282.html

World Bank (2017) Western Balkans: Revving up the engines of growth and prosperity, World Bank Group, Washington DC, available at https://openknowledge.worldbank.org/bitstream/handle/10986/28894/ACS22690.pdf
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
