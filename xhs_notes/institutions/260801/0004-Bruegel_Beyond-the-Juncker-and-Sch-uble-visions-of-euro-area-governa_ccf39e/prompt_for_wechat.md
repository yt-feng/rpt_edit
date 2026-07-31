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
# BEYOND THE JUNCKER AND SCHÄUBLE VISIONS OF EURO-AREA GOVERNANCE

Guntram Wolff
Director, Bruegel

![](images/cd67a56bd52ef7361e6bb0b1a0505586d98c759cd52a34b0aa46fad1eca5f5e9.jpg)  
Source: Bruegel.

## THE ISSUE

Two diametrically opposed visions of the euro-area architecture have been put forward. European Commission president Jean-Claude Juncker favours a model that puts the Commission at the centre of fiscal policy decision-making. The former German finance minister Wolfgang Schäuble argues that fiscal surveillance should be centred on a reformed European Stability Mechanism. Juncker's proposal would over-emphasise the Commission when fiscal policy making is national and would unduly mix the roles of Commission and Council. Schäuble, by contrast, neglects the fact that national fiscal policy matters for the euro area not only for sustainability reasons but also because of the provisioning of public goods, stabilisation policy and effects on inflation and growth. This Policy Brief does not discuss the completion of banking union, which is essential for a stable euro area.

## POLICY CHALLENGE

Fiscal policy making in the euro area will remain a difficult balancing act between national politics and European interests. Departing from both Juncker's and Schäuble's proposals, the Eurogroup should be developed into a Eurosystem of fiscal policy (EFP) as the centre of euro-area fiscal governance. The Eurogroup should have a permanent, full-time president, with a mandate to represent the interests of the whole euro area, and who will report regularly to the European Parliament. The Commission would make fiscal policy recommendations to member states; fiscal rules would be reformed. Political, and in some cases market, pressure would increase on countries that fail to comply with recommendations. Ultimate responsibility for debt will remain national. The European Stability Mechanism should become a permanent fire brigade to manage sovereign debt crises, including possible restructurings in extreme cases. Finally, the EU budget should be reformed to focus on European public goods and on a stabilisation function.

1. Juncker outlined his vision in his 13 September 2017 State of the Union address to the European Parliament. See http://europa.eu/rapid/press-release\_SPEECH-17-3165\_en.htm.

2. In an undated non-paper from the German federal finance ministry, published in October 2017; see https://www.scribd.com/document/361120275/German-finance-ministry-non-paper-on-Eurozone-reforms.

3. Though the Schäuble paper is silent on what this would mean for countries outside the euro area, which are also currently subject to the SGP.

4. It is comparable to appointing Wolfgang Schäuble president of the Bundestag while keeping his finance minister position.

5. As was aptly described by Italy's former prime minister Giuliano Amato at an October 2017 conference; see https://www.eu2017.ee/political-meetings/academic-conference (minutes 26ff; Amato, 2017).

6. Some have made a comparison with the high representative for foreign affairs, who is also the vice president of the European Commission, but the high representative position is in fact a double-hat position and not a role in which only a commissioner acquires the chairmanship of the Eurogroup. Also substantively, the EU's Common Foreign and Security Policy does not foresee a clear institutional separation between the issuing of recommendations based on a clear legal framework and decisions that need to be taken in the council based on such recommendations.

## COMPETING VISIONS OF EURO-AREA GOVERNANCE: JUNCKER VERSUS SCHÄUBLE

European Commission president Jean-Claude Juncker and Germany's former finance minister Wolfgang Schäuble have proposed competing visions of euro-area governance. For Juncker, the core of the vision is a strengthened European Commission, with a Commission vice president who would be the euro-area finance minister, chairing the Eurogroup, presiding over a euro-area budget that is part of the European budget and giving recommendations to the Eurogroup and the member states on their national fiscal policies, based on a ‘political’ interpretation of the Stability and Growth Pact (SGP) $^{1}$ .

By contrast, Schäuble's vision $^{2}$ is clearly motivated by a mistrust of the European Commission. Schäuble proposes to transform the European Stability Mechanism into a permanent European Monetary Fund (EMF) – the euro area needs a fire brigade even when no fire is burning. According to this plan, the EMF would have a clear crisis prevention mandate comparable but more far-reaching than the International Monetary Fund's Article IV. In particular, the ESM would “gradually” be put in charge of monitoring the SGP $^{3}$ . Eventually, the Fiscal Compact and ESM Treaty would be changed so the ESM would fully monitor euro-area compliance with fiscal rules. Schäuble's mistrust of the European Commission is expressed in the wording that the ESM would play a “stronger, neutral” role.

These visions of the euro-area architecture are diametrically opposed – and both are flawed. Juncker's proposal ignores the reality of the strong intergovernmental nature of European fiscal policy coordination, while Schäuble disregards the numerous spillovers from European fiscal policymaking.

Juncker's plan to merge the role of the chair of the Eurogroup with that of the economic and financial affairs commissioner is institutionally problematic. In fact, the proposal would amount to asking the prosecutor to preside as the chief judge over fiscal decision making $^{4}$ . The European Union is built on a fine balance between community interests and national interests. At its core, this gives the European Commission primacy in initiating legislation and in issuing recommendations in the context of the SGP, while giving member countries supremacy in taking final decisions on the SGP, and giving the Council of the European Union and the European Parliament the final say on legislation $^{5}$ . A merging of the roles of chair of the council and commissioner would upset this fine balance.

It would also lead to conflicts of interest. How could the European Commissioner/finance minister issue a recommendation based on the EU legal framework, and then risk losing her/his authority as the chairperson of the council that might want to take a political decision to reject the recommendation $^{6}$ ?

The European Commission already has an impossibly difficult task to interpret a set of rather incomprehensible fiscal rules. But the political approach taken to SGP recommendations has undermined trust in the European Commission as an independent guardian of the treaty and has disturbed the delicate EU balance described above $^{7}$ . Flexibility in fiscal rules is useful but needs to be deployed in a broad forum with strong support from the member states, and should be applied even-handedly. Juncker’s European finance minister proposal is also inefficient because it would give the position of chair of the Eurogroup to the European Commission, disregarding the fact that fiscal policy is national and legitimacy for national fiscal policy derives from national parliaments. Having a commissioner, whose legitimacy is based on European processes, as chair of the group of national finance ministers would not provide adequate political legitimacy and the efficiency of the group would suffer as national ownership would decline. Having said this, it is true that Eurogroup decisions should be made more transparent. Schäuble’s intergovernmental vision also has major shortcomings, and some parts of his proposal, such as

7. Representatives of smaller countries have voiced concerns that they cannot rely on the Commission to take an even-handed approach between smaller and larger member states. This can have negative effects well beyond the application of the SGP. How can the Commission ask member states to respect the rule of law when it itself appears ready to interpret the SGP rules differently for different countries?

8. The paper does not discuss the completion of banking union, which is essential for a stable euro area, nor next steps on capital markets union.

9. For a recent paper see Farhi and Werning (2017).

automatic restructuring, would be highly problematic.

According to Schäuble, the ESM should remain an intergovernmental institution (at least if there is no will to change the treaties). Nevertheless, the proposal is worrying institutionally because it would unsettle the delicate balance between interests of the euro area as a whole and national interests. In particular, the ESM as an intergovernmental institution cannot make ‘neutral’ recommendations – on the contrary, it is a highly political institution. As its decision-making process is based on unanimity among its Board of Governors, it would essentially have to fully internalise the political process when issuing fiscal policy recommendations. In doing so, the role of the neutral interpreter – ie the prosecutor – and the judge would again be blurred.

The proposal would deprive the Commission of its role as the institution in charge of applying the fiscal rules (at least for the euro-area countries). The important separation between political interpretation and neutral application of the rules would be lost.

The ESM itself also has interests that might not be in line with the interests of the euro area as a whole. In particular, it could take an excessively risk-averse approach to fiscal deficits, neglecting the positive economic effects that good stabilisation policy can deliver, while focussing excessively on sustainability concerns, which are the primary interest of the ESM.

The proposal would therefore deprive the Eurogroup of the important representation of euro-area-wide interests in its decision making. Beyond ensuring that national fiscal policy remains sustainable, community interests would be little represented. However, it is well known and well established that there are numerous spillovers and interactions between national fiscal policies, monetary policy, inflation and euro-area growth.

It is indispensable that euro-area interests should be strongly represented in the Eurogroup. That is not visible in the Schäuble paper beyond emergency lending and strengthening of banking union.

## TOWARDS A MORE EFFECTIVE INSTITUTIONAL SET-UP: A 'EUROSYSTEM OF FISCAL POLICY'8

Neither Juncker's nor Schäuble's visions would deliver effective decision making. But they are right to highlight that the current set-up suffers from drawbacks and should therefore be changed. Currently, fiscal coordination primarily focuses on sustainability or more specifically the avoidance of excessive deficits. But two important aspects are not sufficiently considered in the current system: (1) The framework for management of sovereign debt crisis, including possible debt restructurings in extreme cases, is weak and (2) the representation of common interests in decision-making is weak while fiscal rules do not sufficiently take care of stabilisation policy, in particular in terms of the area-wide fiscal stance.

National fiscal policies matter for the union beyond sustainability concerns: in particular, the area-wide fiscal stance and its impact on inflation, and spillovers of national policies across borders, are relevant channels that need to be considered $^{9}$ . In the absence of a large central/federal treasury, it is indispensable to have a forum in which national policies can be discussed and, ideally, adapted if necessary. Coordination of fiscal policies will remain important in Europe's monetary union unless a giant leap towards a federation with central fiscal powers is made. Since national fiscal policy is driven by national policymakers, a forum needs to exist where these national politics can be reconciled.

Of course, one could hope to create a system in which national fiscal policy is exercised fully independently and a hard no-bail-out clause prevents moral hazard. However, such a system is only credible with significant European-level policies (in particular banking union) and only efficient with European-level stabilisation policy. The latter seems unlikely to be available anytime soon while the former is being built-up. Coordination

President of the Eurogroup should be a permanent, full time position; it has been argued that it is not a full-time job, but this view seems to disregard the complexity of the task

10. For the last months of his mandate, Jeroen Dijsel-bloom has become such a full-time Eurogroup chair.

11. As Eurogroup insiders know, one of the reasons why Eurogroup meetings are now less less likely to last into the night is that more preparatory work is done by the current Euro-group president.

policies will therefore remain important for stabilisation. When banking union is completed and financial policies are truly European, the no-bail-out clause will become more credible. That also means that fiscal rules can become less intrusive. At the same time, to achieve better stabilisation policy, the rules should become more binding politically as the following sections explain.

STRENGTHEN THE ROLE OF THE EUROGROUP PRESIDENT BY MAKING IT A FULL-TIME POSITION AND IMPROVE ACCOUNTABILITY
An obvious starting point to better represent euro-area interests is to transform the president of the Eurogroup into a permanent, full time position $^{10}$ . It is sometimes argued that chairing the Eurogroup is not a full-time job, but this view seems to disregard the complexity of the task. Key decisions need to be prepared through many bilateral discussions between key stakeholders before the meeting $^{11}$ . Moreover, a full-time president should also increasingly represent the euro area's interests. For example, the Eurogroup president could regularly visit national parliaments and give press conferences in Brussels and in the national contexts to explain Eurogroup decisions. In fact, it is very important to make the European voice heard in the national decision-making bodies so that collective decisions do not only rely on the national finance minister in the national contexts. A further advantage of a full-time position is that conflicting interests between the national and the European mandate would disappear.

To underpin a neutral president who chairs and represents the euro-area interest while simultaneously being fully accepted by national ministers, a dual appointment process would be desirable. The appointment could be based on a qualified majority vote in the Eurogroup followed by a (non-binding) confirmation vote in the European Parliament (possibly in euro-area composition). An important legal question would be whether the Eurogroup, which is currently officially still an informal body according to the Treaties, would need a different formal status if the European Parliament were to play a role in the appointment process.

To increase transparency around decisions taken, the Eurogroup president would have to regularly report to the European Parliament, perhaps back-to-back with the appearance of the European Central Bank president. However, the European Parliament should not have the right to dismiss the Eurogroup president; that right would remain with the Eurogroup to reflect the fact that the ultimate ‘judges’ on national fiscal policies remain in the council. After all, national fiscal policies are not decided in the European Parliament. A further step towards increasing the common interest in the decision making on national fiscal policies would be to give the president of the Eurogroup a certain voting weight in formal Economic and Financial Affairs Council (ECOFIN) decision making. Of course, to merge the role of the Eurogroup president with the ECOFIN chair or to give voting weight would require a treaty change.

## THE EUROPEAN COMMISSION AND THE FISCAL RULES

The Commission should continue to be in charge of fiscal surveillance and give neutral recommendations to the Euro-group. However, fiscal rules are in urgent need of reform. They are overly complex, opaque and often provide faulty recommendations in real time. Moreover, European fiscal rules do not give sufficient weight to the stabilisation policies needed for the monetary union as a whole.

In addition, while rules such as the Fiscal Compact put significant weight on debt reduction, in their application the debt reduction is not achieved. Too many loopholes and unclear interpretations prevent transparent and clear decision making that makes economic and political sense.

Instead, a simple ‘Taylor rule’ for deficits should be put in place to provide transparent guidance to national policymakers: Deficits should be higher as the output gap increases (and conversely). Deficits should be lower, the larger the debt level is compared to the 60 percent SGP benchmark. The weights attached to stabilisation and debt would need to

12. Claeys (2017) emphasises that the reformed ESM should also have mechanisms to deal with pure multiple equilibria/liquidity problems without any need to resort to conditionality.

13. The main justification for the ESBies in Brunnermeier et al (2016) is exactly the problem of multiple equilibria in sovereign bond markets.

14. For a detailed discussion, see Wolff (2014).

be agreed and fixed. Finally, to prevent liquidity traps when the nominal interest rate is close to zero, all countries should run higher deficits than what the Taylor rule suggests. An alternative proposal worthwhile considering is an expenditure rule, see for example Claeys et al (2016).

A simple rule can be translated into a simple formula and would lead to greater transparency and even-handedness in fiscal recommendations. It would lead to sensible recommendations that take account of each country's sustainability concerns, stabilisation needs and the need to support monetary policy when it is at the zero lower bound.

The Commission would compute the deficit suggested by the rule and make a recommendation to the Eurogroup on how much of the gap between the actual deficit and the one given by the simple formula should be closed by the next year's budget.

The Eurogroup, in turn, would make a political assessment based on the neutral Commission numbers. In particular, it would give a recommendation on the fiscal adjustment member states should undertake. If countries do not comply with the recommendation, politically pressure would gradually build-up. In particular, it would be the role of the permanent chair to explain in the national context why a decision was taken. Decisions would thus become increasingly binding on 

[中间内容因长度限制已省略]

 a provision, amounting to about 10 to 15 percent of the EU budget, would be a helpful instrument. However, it should be clear that such a fund would not play a significant role in area-wide macroeconomic stabilisation policy. It would be insurance to support specific countries hit by severe shocks.

It would be important to define the conditions under which such support payments would be made. The idea of creating a catastrophic unemployment reinsurance scheme has the advantage of enabling automatic payments based on a clear indicator. However, it raises serious political concerns that the countries that would most need support are those that have failed to reform their labour markets $^{21}$ . An alternative would be to have an instrument linked to clear conditions in terms of structural reform. A third option would be to link it to an objective trigger, such as a large fall in GDP.

Such insurance is more important for weaker than for stronger countries. Strong countries are more able to borrow and insure themselves in the markets than weaker countries that are more at risk of losing market access while still engaging in sensible macroeconomic stabilisation policy. As desirable as insurance is for the functioning of a monetary union, it is this asymmetry that makes the introduction of insurance in the euro area so difficult.

Politically, it might therefore be easier not to differentiate between a fund for stabilisation policy and spending for European public goods. One could, for example, create more contingent budget lines that would allow spending more in specific countries when they are hit by shocks, such as an increase in immigration $^{22}$ .

One significant step further towards creating meaningful EU-level fiscal capacity would be to introduce an EU tax to fund the EU budget and create a borrowing capacity in the EU budget. For example, if one based the EU budget on a rather volatile tax, such as a corporate tax, then the EU budget itself would become a stabilising factor. One could also consider a carbon tax, which could be raised already under the current EU treaties. This would be a step towards a true centralisation of stabilisation policy funded with own resources and combined with a borrowing capacity. Such a ‘federalisation’ of stabilisation policy would improve the working of the euro area but it is politically, legally and institutionally difficult to do.

The EU budget commissioner manages meaningful resources and a reorientation of the EU budget could provide meaningful insurance that would be helpful in specific circumstances. This budget commissioner would not stand above national ministers in that she would not have the resources to replace national borrowing or national spending. National fiscal policies will remain the core of fiscal policies in the euro area. The budget commissioner would also not have the power to overrule national decisions, a political power that would remain with the Eurogroup. This is why she would not be a euro area finance minister. Yet, she should participate in the Eurogroup.

23. See Sapir and Wolff (2015) for an earlier discussion with a somewhat different set-up.

This institutional set-up could be called a ‘Eurosystem of fiscal policy’ $^{23}$ . It would be a Eurogroup with significant modifications to strengthen the euro-area-wide interest. At the top would be a powerful Eurogroup chair, who would also be the voice representing the euro-area interests in national and international forums. She would not be a national minster and ideally would have voting rights. The Commissioner for economic and financial affairs and the ESM managing directors would be participants without voting rights. As today, the Commission would have the right of initiative and the obligation to make recommendations on fiscal policy. In addition, the ESM managing director would be given the right to initiate discussions on ESM programmes. If the euro area were to decide to create additional fiscal capacities, the EU budget commissioner would be an additional member of the group. In the long term, the positions of budget commissioner and ESM managing director could be merged, especially if the ESM became a full EU institution and the resources of the ESM became true European resources.

Institutional set-up and governance matter. In this proposal, the Eurogroup would be transformed into a Eurosystem of fiscal policy and remain at the centre of joint fiscal policy decision-making in the euro area. The proposal here outlined would not remove the tensions between national and euro-area wide interests in fiscal decision making. These are inherent to the decentralised organisation of fiscal policies in the euro area. Yet, the proposal would help manage these tensions and strengthen in the debate the voice of the centre with the creation of permanent positions, new rights of initiative (and possibly votes) and greater accountability to the European Parliament. The Eurosystem of fiscal policy would thus be the centre of coordination where difficult trade-offs between national and European interests are negotiated and coordinated. Reformed fiscal rules would provide transparent guidance focussing not only on sustainability but also area-wide stabilisation. The EU budget would become more useful for providing public goods and supporting stabilisation. Nevertheless, fiscal policymaking will remain a delicate political balancing act, which is unavoidable unless Europe decides to become a federation.

![](images/5e7fb2a266f050b75abba95772909ed0795542b92df7150ae85743c30b668ec7.jpg)

## REFERENCES

Amato, Giuliano (2017) Keynote speech to the Estonian Presidency conference ‘Nation States or Member
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
