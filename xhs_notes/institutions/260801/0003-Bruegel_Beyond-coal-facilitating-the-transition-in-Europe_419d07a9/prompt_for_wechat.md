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
# BEYOND COAL: FACILITATING THE TRANSITION IN EUROPE

Simone Tagliapietra
Research Fellow, Bruegel

![](images/e70db600fc850eb958fb4260a06ece33783f8d5a40478f518674d85035712b87.jpg)  
Source: Bruegel.

## THE ISSUE

The European Union energy system is becoming greener and more efficient, but its most polluting component – coal – continues to provide a quarter of its electricity. This is bad for the climate, the environment and human health. A number of EU countries continue to support coal politically for energy security and socio-economic reasons. The energy security argument is understandable, but the feasibility of the energy transition away from coal should not be doubted. Several countries have already successfully phased out coal without compromising energy security or competitiveness. The socio-economic argument is illusory. Coal mining employment in Europe does not represent a sizable issue either at national or regional level.

The author is grateful to Alexander Roth for excellent research assistance and to Grégory Claeys and Georg Zachmann for useful comments.

## POLICY CHALLENGE

The EU should propose that its member countries speedily phase out coal. At the same time, it should put in place a scheme to guarantee the social welfare of coal miners who stand to lose their jobs. The EU does not need to establish a new fund for this; it only needs to make better use of the European Globalisation Adjustment Fund (EGF). For the post-2020 period, the EGF should be transformed into a ‘European Globalisation and Climate Adjustment Fund’ with a higher budget overall, of which €150 million per year should be used to support coal mining regions. By mobilising 0.1 percent of its total budget, the EU could provide a significant incentive to coal-reliant member states to phase out coal, generating substantial benefits for the climate, the environment and human health.

## EUROPE'S DIRTY ENERGY SECRET

Since 2000, Europe's energy system has gone through a profound transformation, underpinned by rapid advances in renewable energy technologies, the costs of which have dropped $^{1}$ , and strong decarbonisation policies, such as the EU 2020 climate and energy package (Tagliapietra and Zachmann, 2015).

But although the EU electricity system has modernised and become greener, it has also maintained its oldest and most polluting component: coal. The share of this fossil fuel in the EU electricity generation mix stands at 25 percent, having declined by only 5 percentage points between 2000 and 2015.

Coal remains predominant in electricity generation in several EU countries: 80 percent in Poland, 77 percent in Estonia $^{2}$ and 49 percent in the Czech Republic, for example (Figure 1). Only a few EU countries have taken decisions to close their coal-fired power plants. The United Kingdom was the first country to set a date for ending the use of coal; its last coal-fired power plant is due to close by 2025. France followed this example, by setting a phase-out date of 2022. The Netherlands and Italy have also proposed plans to close their coal-fired power plants by 2030 and 2025 respectively.

The persistent role of coal in the EU electricity system represents a problem for the climate, for the environment and for human health. From a climate perspective, coal is the worst way to generate electricity. Carbon dioxide $\left(\mathrm{CO}_{2}\right)$ emissions from coal are higher than those of oil and gas. To generate the same amount of electricity, a coal-fired power plant emits 40 percent more $CO_{2}$ than a gas-fired power plant and 20 percent more than an oil-fired power plant (UNFCCC, 2017). To produce enough electricity for an average European household for one year, five tonnes of $CO_{2}$ would be emitted if the electricity was generated from coal, three tonnes if generated from gas and zero tonnes if generated from wind and solar.

There are very limited ways to improve the efficiency of coal and to make it cleaner. New more efficient, or ‘ultra-supercritical’, coal power stations still produce substantially more $CO_{2}$ than gas power stations. Meanwhile, carbon capture and storage technology remains unproven as a fully integrated process. Effective capture technology has not been developed and safe long-term storage at the scale necessary has not been demonstrated. Therefore, it is hard to see how carbon capture and storage for coal would ever be able to compete on price with renewables, the costs of which are rapidly falling.

Coal is broadly bad for the environment, beyond being bad for the climate. Coal-fired power plants across Europe are responsible for the largest volumes of sulphur dioxide, nitrogen oxides and particulate matter released into the air (European Environment Agency, 2017a).

1. In particular, wind and solar have rapidly entered the European Union electricity system, increasing their share in the generation mix from 0.7 percent in 2000 to 13 percent in 2015.

2. Estonia generates electricity with oil shale, a solid fuel similar to coal.

Figure 1: EU countries' electricity generation mixes (2015)  
![](images/d1d29925191cdd08388e2ac8ca89e6996bc8b91a549b731df706f7e29d3246c0.jpg)  
Source: Bruegel based on Eurostat (2017). Note: Estonia generates electricity with oil shale, a solid fuel similar to coal.

3. Consolidated Version of the Treaty on European Union art. 194, 2010 O.J. C 83/01.

4. Directive 2009/28/EC and Directive 2012/27/EU; they established a set of binding measures to help the EU reach its 20 percent renewable energy and 20 percent energy efficiency targets by 2020.

5. Directive 2003/87/EC; intended as the cornerstone of the EU's policy to combat global warming and to be its key tool for reducing emissions cost effectively. However, it has not so far delivered a high enough carbon price.

6. Directive 2010/75/EU; the IED aims to reduce harmful industrial emissions by setting limits on certain pollutants emitted by large combustion plants, including coal-fired power plants. The IED might lead to the retirement of the oldest coal-fired power plants, but all others will continue running.

7. The European Commission proposed in November 2016 to set a 550 grammes CO2/kWh limit for new power plants eligible to take part in national capacity remuneration mechanisms (with a transition period of five years). This proposal is part of ‘Clean Energy for All Europeans,’ a draft package of clean energy legislation that is expected to be approved and adopted around late 2018 or early 2019. See European Commission (2016b).

These pollutants have a range of health effects, causing, in particular, breathing problems such as asthma and bronchitis, which can even prove fatal. Up to 400,000 premature deaths annually in the EU are attributed to air pollution (European Commission, 2017a). Heavy metals such as mercury are also released into the air by coal-fired power plants. These can impact the immune system, with children most at risk. According to the World Health Organisation (2017), 33 out of the 50 most-polluted cities and towns in Europe are located in Poland, notably in the coal mining region of Upper Silesia.

## COAL: AN OBSTACLE TO EU DECARBONISATION

The EU's energy and climate policy architecture has at its core an aim to deliver decarbonisation. On the basis of a long-term vision of reducing greenhouse-gas emissions by 80-95 percent by 2050 compared to 1990, the EU adopted a binding 40 percent emissions reduction target to be achieved by 2030 compared to 1990. This target is also the basis of the EU's international commitment to the United Nations Framework Convention on Climate Change (UNFCCC) Paris Agreement (European Commission, 2016a).

Turning these targets into reality is challenging. It requires radical changes to Europe's power, heating and cooling, industry and transport sectors. This task will become even more challenging if the global effort against global warming is reinforced. The current EU 2050 decarbonisation trajectory is calibrated against the target of keeping the global temperature rise this century below 2 degrees Celsius compared to pre-industrial levels. This is also the central aim of the Paris Agreement. In addition, the Paris Agreement pledges to pursue efforts to limit the temperature increase to 1.5 degrees Celsius (a significantly safer defence line against the worst impacts of a changing climate) (United Nations, 2015).

In 2018, the European Commission will update its 2050 low carbon economy roadmap (European Commission, 2011), to align it with the Paris Agreement's 1.5 degrees pledge. In that context, the EU is set to raise its level of ambition, pledging full decarbonisation of the economy by 2050 (Euractiv, 2017). That could also entail the full decarbonisation of electricity generation well before 2050. To make this possible, a complete phase-out of coal will be necessary. Currently, coal generates 75 percent of the $\mathrm{CO}_{2}$ emissions from the EU's electricity and heat sector, which in turn represents a quarter of the EU's total $\mathrm{CO}_{2}$ emissions (Figure 2).

It should be underlined that the role of electricity and heat in total $CO_{2}$ emissions greatly varies from country to country. The share ranges from 61 percent in Estonia to 40 percent in Poland; from 33 percent in Germany to 18 percent in Italy; down to 7 percent in France (Figure 2, left panel). However, coal is the predominant source of $CO_{2}$ emissions in the sector in almost all countries (Figure 2, right panel).

## IS THE EU READY AND EQUIPPED TO TACKLE ITS COAL PROBLEM?

Given its strong decarbonisation policy, why has the EU not acted so far to solve this coal problem? The answer can be found in the EU Treaties, and in particular in Article 194 of the Treaty on the Functioning of the EU (TFEU), which defines energy policy as a shared competence between the EU and its member countries, but which provides the right for each member country to “determine the conditions for exploiting its energy resources, its choice between different energy sources and the general structure of its energy supply” $^{3}$ .

The EU has tried circumnavigate the Treaty's energy limitations and reshape the EU energy mix on the basis of its competence for environmental policy. In particular, the EU has adopted over time four major initiatives with the aim of promoting an electricity sector based more on renewables and less on coal: i) the Renewable Energy and Energy Efficiency Directives $^{4}$ ; ii) the emissions trading system (ETS) $^{5}$ ; iii) the Industrial Emissions Directive (IED); $^{6}$ iv) the Environmental Performance Standard (EPS) $^{7}$ .

Coal remains persistently present in the EU energy system, reflecting its political sensitivity for several coal-reliant EU countries

Figure 2: CO2 emissions, electricity and heat sectors of EU countries
Europe's CO2 emissions by sector (2015): CO2 emissions from electricity and heat (2015)  
![](images/baea1e6899704cb36c6c88c3ad6f3e2524609783ec9c6d65a4036375b450cf5b.jpg)  
Source: Bruegel based on European Environment Agency (2017b).

As coal remains persistently present in the EU energy system, it is clear that these initiatives have not yet delivered the coal phase-out the EU needs to unleash decarbonisation. This reflects coal's political sensitivity for several coal-reliant EU countries.

For instance, supporting ‘coal jobs’ is a key priority of Poland’s ruling Law and Justice party. It was the key element behind the trade unions’ backing for the party in the October 2015 elections (Bloomberg, 2017). In 2017, Poland and Greece refused to sign Eurelectric’s pledge not to build new coal power plants after 2020 (Platts, 2017). In Germany the threat of job losses and wider economic repercussions have also so far deterred politicians from committing to a deadline to ditch coal. Despite growing public pressure, the German government has continued to tacitly support the country's coal industry (DW, 2017).

In general, two arguments are used by governments to support coal – or at least to procrastinate over its phase-out:

1. Energy security and competitiveness;

2. Job losses and wider economic repercussions for coal-mining regions.

The first argument – energy – is reasonable. A country that is highly reliant on coal for its electricity cannot switch overnight to other cleaner sources of electricity. However, many EU countries have already successfully phased out coal without compromising energy security

8. See Article 56 of the ECSC Treaty: "If the introduction of technical processes or new equipment within the framework of the general programs of the High Authority, should lead to an exceptional reduction in labor requirements in the coal or steel industries, creating special difficulties in one or more areas for the re-employment of the workers released, the High Authority, on the request of the interested governments (...) may facilitate the financing of programs for the creation of new and economically sound activities capable of assuring productive employment to the workers thus released."

9. European Parliament (2017a), Amendment 11, Proposal for a directive, Recital 6.

and competitiveness, showing that a transition away from coal is feasible.

The second argument – socio-economic – is illusory and should not be accepted. Coal mining employment in Europe no longer represents a sizable issue either at national or regional levels. Production of hard coal in the EU has been decreasing since 1990. In 2016, only 36 percent of EU hard coal consumption was covered by domestic production, with the remainder imported from Russia, Colombia, Australia, the United States and other minor suppliers. Only the lignite consumed in the EU is almost entirely supplied by domestic production.

Phasing-out coal would therefore not have substantial implications in terms of job losses. Given the relatively small scale of the challenge, the EU could well provide a solution for the (limited) ‘coal jobs’ that will be lost in the transition. Providing such a solution would be beneficial to:

1. Re-focus the coal transition debate on the only area it should belong to, energy economics;

2. Provide an incentive to coal-reliant countries to start or accelerate coal phase-out plans. That is, the EU should openly propose to member states a speedy phase out of coal, and should concurrently put in place a scheme to guarantee social support for coal industry workers who would face losing their jobs.

The EU country with the highest number of coal mining jobs is Poland, with around 115,500 people employed in coal mines and related businesses.

This represents a mere 0.71 percent of Poland's total employment. In all other countries coal mining employment stands below 30,000, always representing less than 0.6 percent of total employment (Figure 3).

Even at regional level, loss of coal-mining jobs would no longer represent a sizeable hit. In coal-mining regions across Poland, the Czech Republic, Bulgaria, Greece and Germany, coal-mining employment generally stands below 10,000 jobs – and below 1 percent of total regional employment.

Only in Poland's Silesia do coal mining jobs exceed 50,000, representing 5 percent of regional employment (Figure 4).

Europe can manage the transition in coal-mining regions. To ensure their social and economic cohesion during the phase-out, the EU should put in place a mechanism to provide assistance – as is already the case in the United States and Canada, and as was the case in Europe during the coal-mining transformation of the 1950s.

Europe's 1950s transition mechanism for coal-mining regions was the European Coal and Steel Community (ECSC) Fund for the Retraining and Resettlement of Workers. It was created on the basis of Article 56 of the ECSC Treaty, to facilitate re-employment opportunities for those coal and steel workers who lost their jobs as a result of the introduction of new technical processes or new equipment $^{8}$ .

The fund represented the first attempt at a European social and regional policy. With the 1957 Treaty of Rome, this fund was transformed into the European Social Fund (ESF), which in its early stages was indeed used to support workers who lost their jobs in sectors that were modernising, such as coal mining (European Commission, 2007).

## USING THE EUROPEAN GLOBALISATION ADJUSTMENT FUND TO ENSURE A 'JUST TRANSITION' IN COAL REGIONS

The concept of ‘just transition’ has recently entered the EU energy and climate policy debate. In the framework of the broader revision of the ETS Directive, the European Parliament proposed in February 2017 the creation of a ‘Just Transition Fund’, pooling 2 percent of revenues from the auctioning of emission allowances to support regions with a high share of workers in carbon-dependent sectors and a GDP per capita well below the EU average $^{9}$ . This proposal was rapidly dismissed during the negotiations between the European Parliament, the European Commission and the Council of the EU on the ETS Directive revision.

Figure 3: Coal mining employment in EU countries  
![](images/36b57ff335418e0ff8d60dc1e1f432615668b388ff8a53d9fc2bc08be441d0d8.jpg)  
Source: Bruegel based on Eurostat (2017) and Euracoal (2017).

Figure 4: Coal mining employment in EU countries and regions  
![](images/bb508945925f909269da2723422e93ca232a1700be48e4d346f7c0da14236004.jpg)  
Source: Bruegel based on Eurostat (2017).

![](images/e4874910a6e736f5d9ca26ea2cf1e236abb1679ceacd09a9fb2a41f0926301e7.jpg)

That proposal did not survive was a result of both a lack of concreteness and the opposition of the European Commission (according to which such an initiative would not fit into the ETS area of competence).

But the EU does not need to establish a new fund to support the transition of coal mining regions. It only needs to make a better use of the already existing European Globalisation Adjustment Fund (EGF), which was established in 2006 and has a maximum annual budget of €150 million for the 2014-20 period – a budget ceiling that has so far not been fully employed, with on average €40 million disbursed from the EGF each year.

The EGF supports workers who lose their jobs as a result of major structural changes in world trade patterns resulting from globalisation. It can be triggered only when more than 500 workers are made redundant by a single company, or if a large number of workers are laid off in a particular sector in one or more neighbouring regions. The EGF provides up to 60 percent of the funding for projects, lasting up to two years, to help workers who have been made redundant find another job or set up their own business. EU countries app

[中间内容因长度限制已省略]

l-exemptions

Claeys, G and A. Sapir (2017) 'Easing Pain from Trade: the European Globalisation Adjustment Fund', forthcoming, Bruegel

DW(2017) 'Pressure on Germany to ditch coal intensifies', 2 October, available at http://www.dw.com/en/pressure-on-germany-to-ditch-coal-intensifies/a-40778356

EDA (2017) 'U.S. Department of Commerce Invests \$30 Million to Assist America's Coal Communities,' press release, 11 October, available at: https://www.eda.gov/news/press-releases/2017/10/11/2017-acc.htm

Euracoal (2017) Coal industry across Europe, available at http://euracoal2.org/download/Public-Archive/Library/Coal-industry-across-Europe/EURACOAL-Coal-industry-across-Europe-6th.pdf

Euractiv (2017) 'EU to aim for 100% emission cuts in new ‘mid-century roadmap’, 21 September, available at https://www.euractiv.com/section/climate-environment/news/eu-to-aim-for-100-emission-cuts-in-new-mid-century-roadmap/

European Commission (2007) European Social Fund. 50 years investing in people, available at http://ec.europa.eu/employment\_social/esf/docs/50th\_anniversary\_book\_en.pdf

European Commission (2011) 'Communication from the Commission to the European Parliament, the Council, the European Economic and Social Committee and the Committee of the Regions – A Roadmap for moving to a competitive low carbon economy in 2050', COM(2011) 112 final

European Commission (2016a) ‘Paris Agreement to enter into force as EU agrees ratification,’ 5 October, available at https://ec.europa.eu/energy/en/news/paris-agreement-enter-force-eu-agrees-ratification

European Commission (2016b) 'Proposal for a Regulation of the European Parliament and of the Council on the Internal Market for Electricity', COM(2016) 861 final/2, available at http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=COM:2016:861:FIN

European Commission (2017a) 'Commission warns Germany, France, Spain, Italy and the United Kingdom of continued air pollution breaches,' press release 15 February, available at http://europa.eu/rapid/press-release\_IP-17-238\_en.htm

European Commission (2017b) 'Country Datasheets – August 2017 update,' available at https://ec.europa.eu/energy/sites/ener/files/documents/countrydatasheets\_august2017.xlsx

European Commission (2017c) 'Proposal for a Decision of the European Parliament and of the Council on the mobilisation of the European Globalisation Adjustment Fund following an application from Spain - EGF/2017/001 ES/Castilla y León mining,' available at http://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:52017PC0266&from=EN

European Environment Agency (2017a) Releases of pollutants to the environment from Europe's industrial sector – 2015, available at https://www.eea.europa.eu/themes/industry/releases-of-pollutants-from-industrial-sector

European Environment Agency (2017b) 'National emissions reported to the UNFCCC and to the EU Greenhouse Gas Monitoring Mechanism', available at https://www.eea.europa.eu/data-and-maps/data/national-emissions-reported-to-the-unfccc-and-to-the-eu-greenhouse-gas-monitoring-mechanism-13#tab-figures-produced

![](images/894faaec06cd3cf3c20b64a75491b2285cd0af5df258cd87e44ec1d775aad034.jpg)

European Parliament (2017a) 'Amendments adopted by the European Parliament on 15 February 2017 on the proposal for a directive of the European Parliament and of the Council amending Directive 2003/87/EC to enhance cost-effective emission reductions and low-carbon investments,' available at http://www.europarl.europa.eu/sides/getDoc.do?pubRef=--//EP//TEXT+TA+P8-TA-2017-0035+0+DOC+XML+V0//EN

European Parliament (2017b) 'Mobilisation of the European Globalisation Adjustment Fund: application EGF/2017/001 ES/Castilla y León mining', available at http://www.europarl.europa.eu/sides/getDoc.do?type=TA&reference=P8-TA-2017-0277&format=XML&language=EN

Bruegel, Rue de la Charité
33, B-1210 Brussels
(+32) 2 227 4210
info@bruegel.org
www.bruegel.org

Bruegel 2017. All rights reserved. Short sections, not to exceed two paragraphs, may be quoted in the original language without explicit permission provided that the source is acknowledged. Opinions expressed in this publication are those of the author[s] alone.

Eurostat (2017) 'SBS data by NUTS 2 regions and NACE Rev. 2 (from 2008 onwards)', [sbs\_r\_nuts06\_r2]
Government of Albert (2017) 'Coal Community Transition Fund', available at https://www.alberta.ca/coal-community-transition-fund.aspx

Government of Canada (2016) 'News Release - The Government of Canada Accelerates Investments in Clean Energy', 21 November, available at https://www.canada.ca/en/environment-climate-change/news/2016/11/government-canada-accelerates-investments-clean-electricity.html

Platts (2017) 'Poland, Greece reject Eurelectric's no new coal plant after 2020 plan,' 5 April, available at: https://www.platts.com/latest-news/coal/brussels/poland-greece-reject-eurelectrics-no-new-coal-26704436

Tagliapietra, S. and G. Zachmann (2015) 'The EU 2030 Climate and Energy Framework: Keeping up pressure on governance structures,' Bruegel Blog, 17 September, available at http://bruegel.org/2015/09/the-eu-2030-climate-and-energy-framework-keeping-up-pressure-on-governance-structures/

UNFCCC (2017) 'National Inventory Submissions 2017 – European Union', available at http://unfccc.int/national\_reports/annex\_i\_ghg\_inventories/national\_inventories\_submissions/items/10116.php

United Nations (2015) Paris Agreement, available at http://unfccc.int/files/essential\_background/convention/application/pdf/english\_paris\_agreement.pdf

World Health Organisation (2017) 'WHO Global Urban Ambient Air Pollution Database (update 2016)', available at http://www.who.int/phe/health\_topics/outdoorair/databases/cities/en/
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
