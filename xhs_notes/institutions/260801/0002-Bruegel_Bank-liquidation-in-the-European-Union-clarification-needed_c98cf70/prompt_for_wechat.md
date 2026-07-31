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
Policy Contribution
Issue n°01 | January 2017

# Bank liquidation in the European Union: clarification needed

Silvia Merler

SILVIA MERLER (silvia. merler@bruegel.org) is a Research Fellow at Bruegel

This material was originally published in a paper titled ‘Critical functions and public interest in banking services: Need for clarification?’ provided at the request of the European Parliament Committee on Economic and Monetary Affairs, commissioned by the Directorate-General for Internal Policies of the Union and supervised by its Economic Governance Support Unit (EGOV). The original paper is available on the European Parliament’s website. © European Union, 2017

## Executive summary

UNDER THE CURRENT European Union frameworks for dealing with banking problems, resolution of banks is seen as an exception to be activated only if liquidation under national insolvency proceedings would not be warranted. This is most notably the case when the bank provides critical functions to the economy, or when its liquidation might threaten financial stability.

THE TWO OPTIONS – resolution and liquidation – differ substantially when it comes to the scope of legislation that is applicable to the use of public funds. The EU Bank Recovery and Resolution Directive (2014/59/EU) covers resolution, while liquidation is regulated by national insolvency laws. The liquidations of Veneto Banca and Banca Popolare di Vicenza in Italy highlight how this two-tier framework raises important questions in the context of EU banking union.

THE FIRST QUESTION is whether the definitions of critical functions and public interest – key elements in the context of liquidation – should be clarified. A second question is whether the current legal and regulatory situation within banking union ensures that similar banks can expect predictable equal treatment in case of failure.

WE ARGUE THAT there should be more clarity over the role that the concepts of critical functions and public interest play in Member States' decision to grant liquidation aid, as the current framework might give rise to situations in which the views of national authorities seem to contradict the Single Resolution Board's assessment.

WHILE THE PURPOSE of this Policy Contribution is not to provide a comprehensive overview of different national insolvency regimes, we argue that the current diversity is a source of uncertainty about the outcome of liquidation procedures, for all participants. For banking union to function effectively, the framework should be changed to provide the same level of certainty in liquidation as there is expected to be in resolution.

## 1 Introduction

On 27 January 2017, Single Resolution Board (SRB) chair Elke König said $^{1}$ “[m]ost banks are now in such a shape that [...] their failure would not endanger financial stability and that they can be resolved if they fail – like any other business in the market economy – through regular insolvency procedures. [...] The extra safety net of resolution is only for the few”. Under the current European Union frameworks for dealing with banking problems, resolution is seen as an exception to be allowed only if liquidation under national insolvency proceedings would not be warranted. This is the case when the bank provides critical functions to the economy, or when its liquidation might threaten financial stability. In such instances, the Single Resolution Board (SRB) is expected to establish the existence of a public interest, for the bank to be put into resolution.

The two options – resolution and liquidation – differ substantially when it comes to the legislation that is applicable to the use of public funds. The EU Bank Recovery and Resolution Directive (BRRD, 2014/59/EU) governs resolution, while liquidation is regulated by national insolvency laws. The use of public funds in resolution is subject to both state aid rules and the BRRD – thus requiring a preliminary bail-in up to at least 8 percent of total liabilities – but the use of public funds in liquidation is only subject to the state aid requirement that there be a ‘light’ burden-sharing of equity and junior debt. Depending on the structure of individual banks’ balance sheets – ie on how much junior debt they have on their liability side – the BRRD bail-in requirement could potentially reach up to senior bondholders, whereas the light state aid burden allows them to be shielded from losses.

We look at the liquidations of Veneto Banca and Banca Popolare di Vicenza and highlight how this two-tier framework raises important questions in the context of banking union, the ultimate aim of which is to ensure clarity about the rules governing banking crises and their outcomes for banks, private creditors and taxpayers. The first question is whether the definitions of critical functions and of public interest – two key elements in the context of liquidation – should be clarified. While we think these concepts are clear for the purpose of the SRB's assessment, more clarity is warranted in terms of their application in the context of member states' decisions to grant liquidation aid.

A second question is whether the current legal and regulatory environment within banking union ensures that similar banks can expect predictable equal treatment in case of failure. While the purpose of this paper is not to provide a comprehensive overview of different national insolvency regimes across the EU – work that others have done $^{2}$ – we argue that the current diversity in national insolvency frameworks is a source of uncertainty about the outcomes of liquidation procedures, for all participants. The fact that insolvency law remains national allows member states to amend it compared to the normal insolvency proceedings that constitute the reference for the SRB's assessment of the no-creditor-worse-off condition. In particular, to the extent that different governments have different propensities to provide liquidation aid to the banking sector, the final outcome is unclear. Without an EU insolvency law – or at least further harmonisation – this can lead to paradoxical results, such as in the Italian case where senior creditors were eventually better off under insolvency than they would have been under resolution, while taxpayers were worse off. For banking union to function effectively, the framework should be clarified to provide the same level of certainty over liquidation as there is expected to be over resolution.

## 2 The Veneto and Vicenza cases

On 23 June 2017, Veneto Banca and Banca Popolare di Vicenza- were declared to be “failing or likely to fail” by the European Central Bank (ECB) in its capacity as supervisor for euro-area significant institutions $^{3}$ . The two banks had already been among the Italian institutions that failed the ECB’s comprehensive assessment in 2014. In 2016, they benefitted from €3.5 billion in investment from the Italian bank-funded Atlante fund, but their financial positions deteriorated further in 2017 (Merler, 2017a), ultimately resulting in a combined capital need of €1.2 billion. In March 2017, the two banks requested precautionary recapitalisations, which however would have required the capital shortfall to be covered by private means as a pre-condition (Merler, 2017b). The ECB eventually deemed the banks’ business plans not credible. This negative assessment opened up the possibility of either resolution or liquidation, with the decision referred to the Single Resolution Board (SRB). The SRB decided that public interest in resolution was not present, because neither of the banks provided critical functions and their failure was unlikely to have a significant adverse impact on financial stability.

Table 1: Assets and liabilities acquired by Intesa (ISP)

<table><tr><td>Assets</td><td>€ bns</td><td>Liabilities</td><td>€ bns</td></tr><tr><td>Credits vis-à-vis banks</td><td>3.8</td><td>Debts vis-à-vis banks</td><td>9.3</td></tr><tr><td>Credits vis-à-vis customers</td><td>30.1</td><td>Debts vis-à-vis customers</td><td>25.8</td></tr><tr><td>Financial Assets</td><td>8.8</td><td>Bonds (ISP only takes senior)</td><td>11.8</td></tr><tr><td>Shareholdings</td><td>0.02</td><td>Financial liabilities</td><td>2.6</td></tr><tr><td>Others</td><td>3.01</td><td>Others</td><td>1.8</td></tr><tr><td>Total(incl. imbalance and financing to LCA)</td><td>51.3</td><td>Total</td><td>51.3</td></tr></table>

Source: Bank of Italy (2017).

As a result, Veneto Banca and Banca Popolare di Vicenza were wound down under Italian insolvency law on 25 June 2017. Italian law provides for several insolvency procedures: banks and other financial institutions – and other selected types of enterprises – are subject to “forced administrative liquidation” (Liquidazione Coatta Amministrativa (Baker McKenzie, 2017); see Box 1 in section 4.2 for details). In the context of liquidation, shares (mostly owned by Atlante) and subordinated debt were wiped out to meet the minimum burden-sharing requirement established in the European Commission’s 2013 Communication on State Aid to Banks. The performing parts of the banks’ assets were acquired by Intesa San Paolo – Italy’s second largest bank – together with some of the liabilities, most notably deposits and senior debt (see Table 1 for details). Intesa paid a symbolic sum of €1 for the acquisition, and benefitted from a €4.8 billion cash injection by the state. Of this, €3.5 billion was intended to ensure that the acquisition would not undermine Intesa’s equity ratios, while €1.3 billion was destined to cover the costs of closing branches and managing dismissal/redeployment of the staff of the banks being liquidated. Intesa was also granted state guarantees that could potentially total up to €12 billion $^{4}$ . Of this, up to €6.35 billion might cover the repayment of debt held that was deemed to be not good after due diligence; up to €4 billion might constitute a buffer for currently performing debts that are high risk; and the remaining guarantee of up to €2 billion might cover potential legal risks of the banks being liquidated. The non-performing parts of the two banks’ balance sheets were transferred to SGA (Società per la Gestione di Attività) – a vehicle set up for the rescue of Banco di Napoli at the end of the 1990s – with aim of maximising the recovery over time.

The cases of Veneto Banca and Popolare di Vicenza are reminiscent of that of Banca Romagna Cooperativa (BRC), a significantly smaller $^{5}$ Italian lender liquidated in July 2015 (Merler, 2016). BRC’s assets and liabilities were transferred to Banca Sviluppo, part of the Italian ICCREA Group. In the process, BRC equity and junior debt remained in the liquidation estate – similarly to what happened in the Veneto and Vicenza cases. The BRC operation was conducted under national insolvency law by selling only parts of assets and liabilities out of liquidation. The Italian mandatory deposit guarantee scheme for the sector (FGDCC) covered the negative difference between the transferred assets and liabilities – an action that qualified as state aid, because it was beyond the DGS’ pay-out function. This was authorised by the European Commission. The scale of the BRC case was obviously much smaller than the Veneto and Vicenza cases, and the cost of the operation for the Mutual Bank Deposit Guarantee Fund (FGDCC) was estimated at the time as €260.8 million maximum (European Commission, 2015).

Because of the structure of the operation, the Veneto Banca and Banca Popolare di Vicenza cases have also been compared to the case of the Spanish Banco Popular, which was acquired for a symbolic amount of €1 by Banco Santander. In contrast to the two Italian banks, however, Banco Popular was put in resolution by the SRB for public interest reasons. The similarity between the Italian and Spanish cases stems from the fact that the sale and transfer of part of the failing banks' balance sheets to a buyer is also foreseen as a resolution tool under Article 38 BRRD. Mesnard et al (2017) highlights also that the measures implemented in the Italian case are very similar to those in previous resolution cases implemented in the EU, such as the resolution of the Greek Panellinia Bank through a transfer order to Piraeus Bank in April 2015 $^{6}$ . Despite superficial similarities, however, there are significant differences between the Italian and Spanish operations when it comes to the applicability of EU legislation in terms of use of public funds. Section 3 reviews this in more detail.

## 3 Liquidation vs. resolution

## 3.1 Conditions

The current EU rules give two options for dealing with banks that declared by the Single Supervisory Mechanism to be failing or likely to fail: liquidation or resolution. The decision on which approach should be followed in each case is a prerogative of the Single Resolution Board (SRB), and it hinges on an assessment of the existence of public interest. Because of its potential effects on property rights, the choice to put a bank into resolution should be seen as an exception (European Commission, 2017), limited to cases in which winding up the institution under normal insolvency proceedings would not meet the resolution objectives to the same extent $^{7}$ . Resolution aims at ensuring continuity of critical functions, avoiding a significant adverse effect on the financial system, protecting public funds, covered depositors and covered investors, and clients' assets and funds $^{8}$ . If the SRB decides that resolution is not in the public interest, then the bank is wound down under national insolvency law.

## 3.2 Use of public funds

One important point to note is that the two options differ quite significantly when it comes to the scope of EU legislation applicable to the use of public funds (Figure 1).

Article 32(4) of the Bank Recovery and Resolution Directive (BRRD) suggests that, as a rule, the fact that a banks needs public support is sufficient for the ECB to declare the bank failing or likely to fail. Banks that happen to have capital shortfalls should therefore ideally cover that from private sources. If that is not feasible, a member state can still intervene in line with market conditions, ie on terms that would be the same for a private investor. This kind of intervention would remain outside the scope of both the resolution framework and EU state aid policy $^{9}$ . Alternatively, if the bank is solvent it could qualify for precautionary recapitalisation, which allows the use of public funds in compliance with state-aid rules and outside the scope of the BRRD resolution framework. Article 32(4.d) BRRD states that this extraordinary public financial support does not trigger resolution if it is required “in order to remedy a serious disturbance in the economy of a member state and preserve financial stability”, and if it is “at prices and on terms that do not confer an advantage upon the institution.” If the conditions for precautionary recapitalisation are met, public funds can thus be used without triggering resolution and the associated 8 percent bail-in requirement. The burden-sharing requirement of equity and junior debt would still apply, as per the Commission’s 2013 State Aid Communication $^{10}$ .

Figure 1: Use of public funds in the EU framework  
![](images/65aab58db62c2275bd4476d59327c02632e26f789168598aa1d11da69badb49f.jpg)  
Source: European Commission (2017).

If a bank is declared by the ECB to be failing or likely to fail $^{11}$ , the precautionary recapitalisation option is not available, and the choice is between liquidation or resolution. If the bank is put into resolution, the Single Resolution Mechanism Regulation (SRMR) requires that the bank's losses be covered by the bail-in of shareholders and creditors up to 8 percent of the bank's liabilities, before the Single Resolution Fund (SRF) can be accessed. Depending on the composition of individual banks' balance sheets, this may imply the bail-in of senior debt and potentially even uncovered deposits. The use of funds from the SRF is anyway subject to the Commission's State aid assessment. State aid is possible in the context of liquidation – in the form of liquidation aid – and it is subject to the State aid discipline, including the burden-sharing requirements laid out in the 2013 Communication. The rationale underlying aid in liquidation is that while the winding up of small banks is not expected to have systemic effects, it may still have important local effects. Currently, it is for Member States to decide whether liquidation may harm the local economy, and whether the use national funds is warranted to mitigate the damage – although liquidation aid would then need to be cleared by the Commission.

A comparison of the Banco Popular case with the Veneto and Vicenza cases highlights the practical implications of this different legal scope. The use of public funds in the context of resolution with sale of assets to a private investor would have required the preliminary bail-in of at least 8 percent of the banks' equity and liabilities. Depending on the structure of the bank's balance sheet, this preliminary requirement could have entailed a bail-in of senior liabilities. The use of public funds in the context of a similar operation conducted in liquidation is instead regulated under the State aid framework, which requires a preliminary contribution of equity and junior debt only. In both the case of Popular and the case of the two Italian banks, senior debt was not touched. But Banco Popular was resolved under BRRD, and the sale of business was accompanied by a €7 billion capital raise from the acquiring bank (Santander) and a €3.3 billion bail-in of equity and debt. In the case of two Italian banks, which were dealt with under national insolvency law, equity and junior debt were wiped out but the acquiring bank (Intesa) benefitted from publicly financed liquidation aid.

## 4 Question raised

Since the scope of EU law regulating the use of public money in resolution and liquidation is different, a substantially similar operation conducted under these two different frameworks can lead to very different outcomes for (i) the acquiring bank; (ii) the banks' creditors; and (iii) the taxpayers. The distinction between resolution and liquidation is ultimately based on the existence of public interest, an assessment that is the task of the SRB. In this section we look at the SRB's assessments in the cases of Veneto Banca and Banca Popolare di Vicenza, and at the implications national insolvency frameworks might have on the clarity of EU rules in the context of banking union.

## 4.1 Critical functions and public

[中间内容因长度限制已省略]

c issues.

First, while the definition of critical functions seems clear as regards the SRB's assessment of the existence of a public interest, it is not equally clear what role it plays in the EU discipline on liquidation aid, as the 2013 Banking Communication does not include guidelines or on how the local effect of liquidation should be evaluated. In the absence of clarity on what constitutes a serious impact on the regional economy, the rules on liquidation aid leave room for governments to effectively re-instate at the local level the public interest that the SRB has denied at national (or, in the Italian case, even at the regional) level. One way to overcome this problem could be to task the SRB with providing an explicit assessment of the impact of liquidation at the local level, to ensure the assessment is homogeneous.

The second, related, issue is that the Veneto and Vicenza cases highlight the problematic nature of a two-tier framework in which resolution is dealt with under EU law and liquidation is left for diverse national insolvency procedures. The problem with this is twofold. On one hand, the difference in insolvency frameworks implies that failing banks would face different insolvency proceedings in different countries. For example, in Spain, banks would face a court-based process, while the Italian special regime for banks is essentially administrative. The fact that insolvency is regulated under national law also makes it easier for governments to amend the ordinary insolvency framework. This could give rise to peculiar situations whereby senior creditors fare better in insolvency than they would in resolution, such as in

the cases of Veneto and Vicenza. In order to avoid this uncertainty, the best option would be to further harmonise insolvency laws, possibly introducing an EU-wide regime.

For banking union to function properly, banks, creditors and taxpayers deserve to have certainty about the rules governing liquidation. This objective would best be served by a single EU insolvency regime to complement the current EU framework for resolution, and by a clarification of the extent to which Member States have discretion to establish the local public interest when it comes to liquidation aid.

## References

Baker McKenzie (2017) 'Italy', in Global restructuring & insolvency guide, available at: http://restructuring.bakermckenzie.com/wp-content/uploads/sites/23/2017/01/Global-Restructuring-Insolvency-Guide-12-2016New-Logo-Italy.pdf

Bank of Italy (2017) 'Informazioni sulla soluzione della crisi di Veneto Banca S.p.A. e Banca Popolare di Vicenza S.p.A. Memoria per la VI Commissione Finanze della Camera dei Deputati', July, available at www.bancaditalia.it/media/notizie/2017/Nota-Venetobanca-e-BPV.pdf

ECB (2017) 'ECB deemed Veneto Banca and Banca Popolare di Vicenza failing or likely to fail', press release, 23 June, European Central Bank

European Commission (2017) 'State aid: How the EU rules apply to banks with a capital shortfall - Factsheet,' 25 June

European Commission (2015) 'State Aid SA.41924 (2015/N) (ex 2015/PN) - Italy Resolution (via liquidation) of Banca Romagna Cooperativa - Credito Cooperativo Romagna Centro e Macerone - Società Cooperativa', 2 July

European Commission (2013) 'Communication from the Commission on the application, from 1 August 2013, of State aid rules to support measures in favour of banks in the context of the financial crisis ('Banking Communication'); 2013/C 216/01, 30 July

Italian Parliament (2017) ‘Disegno di legge: “Conversione in legge del decreto-legge 25 giugno 2017, n. 99, recante disposizioni urgenti per la liquidazione coatta amministrativa di Banca Popolare di Vicenza S.p.A. e di Veneto Banca S.p.A.”

McCormack, G., A. Keay, S. Brown and J. Dhlgreen (2016) Study on a new approach to business failure and insolvency. Comparative legal analysis of the Member States' relevant provisions and practices, European Commission

Ministry of Economy and Finance, Italy (2017), The liquidation of Banca Pop. di Vicenza and Veneto Banca, 2017, available at: http://www.mef.gov.it/inevidenza/documenti/Liquidation\_of\_banks\_in\_Veneto.pdf

Merler, S. (2016) 'Italy,' chapter in Bank resolution and bail-in in the EU: selected case studies pre and post BRRD, World Bank FinSAC report

Merler, S. (2017a) 'Italian banks: not quiet on the eastern front', Bruegel Blog, 31 March

Merler, S. (2017b) 'A tangled tale of bank liquidation in Venice', Bruegel Blog, 26 June

Mesnard, B., A. Margerit and M. Magnus (2017) 'The orderly liquidation of Veneto Banca and Banca Popolare di Vicenza,' European Parliament Briefing

SRB (2017) 'The SRB will not take resolution action in relation to Banca Popolare di Vicenza and Veneto Banca', press release, 23 June, Single Resolution Board

SRB (2017a) 'Decision of the Single Resolution Board in its executive session of 23 June 2017 concerning

the assessment of the conditions for resolution in respect of Banca Popolare di Vicenza S.p.A., non-confidential version', SRB/EES/2017/12, Single Resolution Board

SRB (2017b) 'Decision of the Single Resolution Board in its executive session of 7 June 2017 concerning the adoption of a resolution scheme in respect of Banco Popular Espanol S.A., non-confidential version', SRB/EES/2017/08, Single Resolution Board

SRB (2017c) 'Decision of the Single Resolution Board in its executive session of 23 June 2017 concerning the assessment of the conditions for resolution in respect of Veneto Banca S.p.A., non-confidential version', SRB/EES/2017/11, Single Resolution Board

SRB (2017d) 'Notice summarising the effects of the decision taken in respect of Banca Popolare di Vicenza S.p.A,' Single Resolution Board
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
