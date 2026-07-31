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
# A ‘twin peaks’ vision for Europe

Dirk Schoenmaker and Nicolas Véron

## DIRK SCHOENMAKER (dirk.schoenmaker@bruegel.org) is a Senior Fellow at Bruegel

NICOLAS VÉRON (n.veron@bruegel.org) is a Senior Fellow at Bruegel and at the Peterson Institute for International Economics.

The authors would like to thank Andre Sapir for useful comments and Inês Goncalves Raposo for excellent research assistance. The text of this Policy Contribution will be published as a chapter in Godwin, A. and A. Schmulow (eds) (2018) The Cambridge Handbook of twin peaks financial regulation, Cambridge University Press.

## Executive summary

THE EUROPEAN UNION'S FINANCIAL SUPERVISORY ARCHITECTURE is based on a sectoral model with separate authorities for banking, insurance and securities and markets. New developments in the EU financial sector make this sectoral structure increasingly out of date:

\- BREXIT CREATES A NEED FOR STRONG EU-LEVEL WHOLESALE MARKET and conduct-of-business supervision to build an integrated capital market for the EU27;

\- MIS-SELLING OF BANK BONDS – that can be bailed in – to retail consumers has highlighted the need for a strong conduct-of-business supervisor for banking and other retail financial services, separate from prudential supervision to ensure a strong focus on the interests of consumers;

\- FINANCIAL CONGLOMERATES, COMBINING BANKING AND INSURANCE, make up about a third of Europe's banking and insurance sector. Joined-up supervision would strengthen the prudential supervision of these conglomerates.

TO DEAL WITH THESE CHALLENGES, the EU should commit to a twin peaks model as a long-term vision for supervision. The first peak would be prudential supervision focusing on the health and soundness of financial firms. As these financial firms have become increasingly interwoven, the vision of integrated cross-sector prudential supervision is increasingly compelling, even though legal obstacles imply it cannot be implemented at the European level in the near term.

THE SECOND PEAK would be a strong markets and conduct of business supervisor. This supervisor would solely focus on the proper functioning of markets and fair treatment of consumers. This twin peaks model should guide Europe's efforts to deal with current challenges.

## Introduction

Some countries, such as the Netherlands, France and the United Kingdom, have moved to a supervisory model known as ‘twin peaks’, with one supervisor for prudential supervision and another for markets and conduct-of-business supervision.

The organisation of the European Supervisory Authorities (ESAs) is based on a sectoral approach with one ESA for each sector: the European Banking Authority for banking, the European Insurance and Occupational Pensions Authority for insurance and pension funds and the European Securities and Markets Authority (ESMA) for the securities markets. But is this sectoral approach still valid $^{1}$ ? Some countries, such as the Netherlands, France and the United Kingdom, have moved to a supervisory model known as ‘twin peaks’ (Taylor, 1995 and 2009), with one supervisor for prudential supervision and another for markets and conduct-of-business supervision. Other countries, such as Germany, Sweden and Poland, have adopted the single supervisory model.

This Policy Contribution outlines a long-term vision for the supervisory architecture in the European Union. In the aftermath of the global financial crisis, the euro-area crisis, and the Brexit vote, it is time to work on this long-term agenda. There is global trend towards the twin peaks model based on positive experiences (see Huang and Schoenmaker, 2015, for a review). Examples are found in Australia, the Netherlands and more recently the United Kingdom and South Africa.

There are several arguments in favour of a twin peaks structure for the European Union. Brexit creates a need for a strong market and conduct-of-business supervisor to build an integrated capital market for the EU27 and the European Economic Area (EEA) $^{2}$ . With the move towards bail-in of bank bonds, cases of mis-selling of these bonds to retail consumers who were not fully aware of the bonds' risk profile have come to widespread public attention. That requires a strong and proactive conduct-of-business supervisor, which is separate from the prudential supervisor. Finally, there are interlinkages between banks and insurers within financial conglomerates. Integrated prudential supervision would make it possible to supervise these conglomerates on a joined-up basis.

## Supervisory models

The organisational structure of financial supervision has been changed in most EU countries over the last 20 years (see Table 1). All countries used to have a sectoral model of financial supervision with separate supervisors for banking, insurance and securities, reflecting the traditional dividing lines between financial sectors. But the sectors are converging. The universal banking model allows banks to combine banking activities, such as lending and deposit-taking, with securities activities, such as offering investment funds and underwriting securities offerings. Meanwhile, banks and insurers are allowed to operate as part of financial conglomerates. Financial products are converging. Banking and life-insurance products, for example, both serve the market for long-term savings. Mortgages are no longer the sole province of banks, but are also offered by insurers and pension funds. Because of the blurring of the dividing lines between financial sectors, cross-sector models of supervision have emerged. There are two main cross-sector models of supervision: a functional (or twin peaks) model and an integrated model.

In the twin peaks model, there are separate supervisors for each of the supervisory objectives: prudential supervision and conduct of business. In some countries, especially in the euro area where central banks have transferred their responsibility for monetary policy to the European Central Bank, the central bank is responsible for prudential supervision. In other countries – Australia is one example – a separate agency is responsible for prudential supervision.

In the integrated model, there is a single supervisor for banking, insurance and securities combined (or, put differently, one supervisor who oversees both prudential supervision and conduct-of-business). There are two versions of the integrated model. Denmark and Sweden have adopted a fully integrated model without central bank involvement in financial supervision. In Germany and Austria, the central bank still has a role in banking supervision, alongside the integrated supervisor (respectively, BaFin in Germany and FMA in Austria). The twin peaks model combines the objectives of systemic supervision and prudential supervision, leaving conduct-of-business supervision as a separate function. The integrated model combines the objectives of prudential supervision and conduct-of-business supervision, leaving systemic supervision (financial stability) as a separate function that is usually performed by the central bank.

Table 1: Organisational structure of financial supervision (as of mid-2017)

<table><tr><td colspan="5">Basic models</td></tr><tr><td>Countries</td><td>(1) Sectoral</td><td>(2) Cross-sector: functional (twin peaks)</td><td>(3a) Cross-sector: integrated without central bank role in banking supervision</td><td>(3b) Cross-sector: integrated with central bank role in banking supervision</td></tr><tr><td rowspan="9">European Union</td><td>Bulgaria</td><td>Belgium (2011)</td><td>Denmark (1988)</td><td>Austria (2002)</td></tr><tr><td>Cyprus</td><td>Croatia (2005)</td><td>Estonia (2002)</td><td>Czech Republic (2006)</td></tr><tr><td>Greece</td><td>France (2003)</td><td>Hungary (2000)</td><td>Finland (2009)</td></tr><tr><td>Lithuania</td><td>Italy (1999)</td><td>Latvia (2001)</td><td>Germany (2002)</td></tr><tr><td>Luxembourg</td><td>Netherlands (2002)</td><td>Malta (2002)</td><td>Ireland (2003)</td></tr><tr><td>Portugal</td><td>United Kingdom (2011)</td><td>Poland (2008)</td><td>Slovakia (2006)</td></tr><tr><td>Romania</td><td></td><td>Sweden (1991)</td><td></td></tr><tr><td>Slovenia</td><td></td><td></td><td></td></tr><tr><td>Spain</td><td></td><td></td><td></td></tr><tr><td rowspan="3">Outside EU</td><td></td><td>Australia (1998)</td><td></td><td>Japan (2000)</td></tr><tr><td></td><td>Canada (1987)</td><td></td><td></td></tr><tr><td></td><td>United States (2011)</td><td></td><td></td></tr></table>

Source: Updated from De Haan, Schoenmaker and Oosterloo (2012). Note: The United States is categorised as a functional model, because the Dodd-Frank Act of 2010 gave strong cross-sectoral powers to the Federal Reserve as the main systemic supervisor, while conduct-of-business supervision is mostly entrusted to the SEC, CFTC and CFPB. Underlying this, there are still multiple sectoral supervisory agencies in the United States at the federal and state levels. France has twin peaks features, but with some retail conduct of business supervision for banks and insurance at ACPR (prudential supervisor) instead of AMF (markets supervisor). Italy has also twin peak features, with conduct-of-business supervision of banks at CONSOB. Portugal is currently reviewing its supervisory model.

Kremers et al (2003) developed a framework to analyse the trade-offs by listing the synergies and conflicts of supervisory interests for both models. Figure 1 summarises these potential synergies and conflicts. The first synergy in the left panel of Figure 1 results from combining systemic supervision with the prudential supervision of financial institutions. The synergy between stability issues on the micro level (at the level of the financial institution) and the macro level (economy-wide) refers to the ability to act decisively and swiftly in the event of a crisis. Crisis management usually requires key decisions to be taken within hours rather than days. Combining both micro- and macro-prudential supervision within a single institution ensures that relevant information is available at short notice and that a speedy decision to act can be taken if necessary. The Northern Rock crisis in the UK in 2007 indicated that crisis management by two institutions might not be very effective. According to Buiter (2007), coordination between the Bank of England and the UK Financial Services Authority was shown to be insufficient. Goodhart (2017) also argues that the working of what was then called the tripartite regulatory system – comprising the Treasury, the Bank of England and the Financial Services Authority – failed in the United Kingdom during the great financial crisis.

The second synergy in Figure 1 is ‘one-stop supervision,’ ie the synergy between prudential supervision and conduct-of-business supervision. Furthermore, synergies in the execution of supervision are exploited by combining different supervisory activities within one institution.

Figure 1: Supervisory synergies and conflicts  
![](images/71ddc89454d35f923b5b78b93bd5eccb15d4004ca30112008d47f4ed548fd2a8.jpg)

The first potential conflict of interest between systemic supervision and prudential supervision relates to the possibility of lender-of-last-resort operations (LoLR) by the central bank. How can the pressure to extend the benefits of LoLR operations (avoiding systemic risk, such as a financial panic or bank runs) to all financial institutions be balanced against its costs (moral hazard)? The answer adopted by many central banks is to limit the possibility of LoLR operations to banks, which are subject to systemic risk. Thus LoLR operations are not available to insurance companies. However, when financial groups integrate, it might become more difficult to isolate only the banking part of financial institutions for potential LoLR operations. The financial panic of September-October 2008 in the United States provided an illustration of this. Hitherto non-bank financial groups such as Morgan Stanley and Goldman Sachs hastily converted to bank holding company status in order to access the federal banking safety net.

The second potential conflict of interest between prudential supervision and conduct-of-business supervision relates to the different nature of their objectives. The two types of supervision generally require different mindsets and skills, and occasionally conflict with each other (Véron, 2017). Especially in times of financial crisis, or to avert a crisis, the imperative of financial stability can be so overwhelming that authorities might neglect some conduct duties in order to help firms satisfy prudential requirements – for example, authorities might close their eyes to questionable commercial practices if these help a bank to increase its profitability and capital. Conversely, in non-crisis times, conduct mandates might be so all-consuming that prudential considerations are neglected, as arguably happened in the run-up to 2007 at the UK Financial Services Authority in its supervision of several British banks (including Northern Rock and Royal Bank of Scotland), or at the US Securities and Exchange Commission in its supervision of large broker-dealers (including Bear Stearns and Lehman Brothers). Various cases of mis-selling of securities in several European countries (including most prominently Italy in recent years, but also Finland, Slovenia, Spain and others in the past), when banks sold their own risky shares, subordinated debt and/or senior debt instruments to retail clients, including some with low levels of financial literacy, can be considered in a similar light. These experiences suggest that the enforcement of consumer protection regulation in the financial sector should not be entrusted to prudential supervisors.

The prudential supervisor will be interested in the soundness of financial firms including profitability, while the conduct-of-business supervisor will focus on the interests of those firms' clients. Mixing up the responsibilities of financial stability and conduct-of-business could create incentives for the supervisor to prioritise one objective over the other. By separating the supervisory functions, the conduct-of-business supervisor is ideally situated to supervise possible conflicts of interest between a financial institution and its clients because it will focus only on the interests of the clients. Furthermore, the stability objective is consistent with preserving public confidence and may require discretion and confidentiality, which could be counter-productive to the transparency objective.

## Twin peaks for Europe

We argue that the European supervisory architecture should eventually move to a twin peaks model for three main reasons. First, banks and insurers are often part of a financial conglomerate, which warrants integrated banking-insurance supervision. Second, the EU27 will need to upgrade the supervision of its capital markets after Brexit. A dedicated markets supervisor can adapt quickly to this new reality. Third, prudential supervision and markets and conduct-of-business supervision require different skills and approaches. While the first deals more with technical capital adequacy issues and requires staff trained in economics, finance and/or accountancy, the second is more behavioural and legalistic (Goodhart et al, 2002). This behavioural and legalistic approach concerns policing the conduct of financial institutions in the markets (eg insider trading, market abuse, disclosure) and towards clients (eg adequate information provision, duty of care, know your customer).

We frame our recommendation for twin peaks supervision in the EU as a long-term aspirational goal. Defining a long-term goal is important for taking decisions on short-term issues, such as the relocation of the European Banking Authority from London to the EU27 and the upgrading of ESMA.

## Prudential supervision

Close interaction between banking and insurance supervision is needed for the effective supervision of financial conglomerates that combine banking and insurance. Figure 2 shows that 31 percent of banks and 36 percent of insurers belong to a financial conglomerate. These percentages are for 2015 and measured in assets (ie bank conglomerate assets as a share of total banking assets and total insurance assets).

Why is such close interaction necessary? During the financial crisis, several financial institutions experienced solvency problems. These could emerge in any part of the financial institution (eg sub-prime mortgages in the bank or on the insurance balance sheet). It appeared that several financial conglomerates made use of double counting and thus had insufficient capital. Double counting (also known as double gearing) is the practice whereby the same capital base at the holding level of a financial conglomerate is counted as regulatory capital for both the banking activities and the insurance activities.

Figure 2: Share of financial conglomerates in banking and insurance at EU level (2015)  
![](images/cf78ba9ddecb5f379f722510f25cd1b3b735b3d7bb770c392f6c9b009ef667a0.jpg)  
Source: Bruegel based on Joint Committee (2016). Note: The graph shows the share of EU banks and insurance groups that are part of a financial conglomerate.

Such double counting was, and still is, allowed because of the fragmented financial architecture, both on the rule-making and supervisory sides. On the regulatory front, the so-called Danish compromise, agreed in the process of EU transposition of the Basel III capital accord and enshrined in the EU Capital Requirements Regulation, allows double counting of capital (Financial Times, 2012). On the supervisory front, the absence of an integrated focus (the supervisory focus is on the banking and insurance parts but not on the aggregate) leaves no-one responsible for the overall capitalisation of financial conglomerates. The current weak form of supplementary supervision of financial conglomerates, in which either the banking or insurance supervisor has some responsibilities for the supervision of conglomerates, cannot replace proper integrated supervision.

Nevertheless, the industry and the supervisory authorities are keen to preserve the current sectoral structure and unwilling to adopt a twin peaks model (European Commission, 2017b). From a political economy point of view, this position is understandable. Financial institutions and their supervisors are keen to preserve the status quo, including any cosy relationships between the main players. In particular, the insurance sector is afraid that a merged banking/insurance prudential authority would be dominated by banking regulatory approaches. By c

[中间内容因长度限制已省略]

ormerly known as OMX), covering the exchanges of the Nordic countries (Helsinki, Copenhagen, Stockholm, Iceland) and Baltic countries (Riga, Tallinn and Vilnius). It would be far more effective and efficient to make ESMA responsible for the direct supervision of these platforms (in a hub-and-spoke model, with relevant operational tasks duly delegated to national market supervisors) instead of four (in the case of Euronext) or seven (in the case of Nasdaq Nordic) separate local national market authorities. ESMA would thus become responsible for safeguarding the integrity of markets and avoiding insider trading and market abuse.

The wholesale market activities of the large players, comprising the large European universal banks and the US, UK, Swiss and Japanese investment banks, which will partly relocate to the EU27, also need to be supervised. This supervision covers the wholesale banking aspects of the Markets in Financial instruments Directive (MiFID). $^{3}$

For other aspects, such as authorisations of initial public offerings and fund management registrations, ESMA's policy-setting role should be strengthened but individual decisions could continue to be taken by national authorities for the foreseeable future. Similarly, the conduct-of-business supervision of smaller investment and insurance intermediaries to protect retail investors can stay at the national level. These activities – IPOs, fund management and intermediaries – comprise the bulk of the current workload of the national markets authorities. This would remain at the national level, in line with the subsidiarity principle, with ESMA given greater authority to ensure supervisory consistency in line with the European Commission's recent proposals (European Commission, 2017d).

## Policy conclusions

There are too many policy constraints for the European Union to adopt a twin peaks financial supervisory architecture in the short term, including uncertainties about Brexit, treaty provisions and possible changes to the geographical coverage of the banking union (currently the 19-country euro area, possibly expanding in the future through the close cooperation procedure). With this in mind, we suggest twin peaks as a long-term guiding vision for the EU, not a rapidly achievable target.

Even so, the vision could have practical consequences in the near term, in multiple areas such as the reform of ESMA's governance and funding, the supervision of emerging (fintech) financial market segments, the future of the European Banking Authority and the EU approach to consumer financial protection. Twin peaks holds the promise of a financial system that is both safer, thanks to joined-up prudential oversight, and fairer, thanks to the better protection of savers, investors, and more generally of users of financial services. It is desirable that the European Union should commit itself explicitly to that vision, even if the time needed for its fulfilment is likely to be measured in decades rather than years.

## References

De Haan, J., D. Schoenmaker and S. Oosterloo (2012) Financial Markets and Institutions: A European Perspective, Second Edition, Cambridge University Press, Cambridge, UK

European Commission (2017a) 'Public Consultation on the Operation of the European Supervisory Authorities (ESAs)', DG FISMA, Brussels

European Commission (2017b) 'Feedback statement on the public consultation on the operations of the European Supervisory Authorities having taken place from 21 March to 16 May 2017', DG FISMA, Brussels

European Commission (2017c) ‘Communication on the Mid-Term Review of the Capital Markets Union Action Plan,’ COM(2017) 292, 8 June, Brussels

European Commission (2017d) 'Communication on Reinforcing integrated supervision to strengthen Capital Markets Union and financial integration in a changing environment,' COM(2017) 542, 20 September, Brussels

Financial Times (2012) 'Basel III - the case for the defence', 23 January

Goodhart, C. (2017) The Bank of England, 1694-2017, forthcoming.

Goodhart, C., D. Schoenmaker and P. Dasgupta (2002) 'The Skill Profile of Central Bankers and Supervisors', European Finance Review 6: 397-427

Huang, R. and D. Schoenmaker (eds) (2015) Institutional Structure of Financial Regulation: Theories and International Experiences, Routledge, London

Hüttl, P. and D. Schoenmaker (2016) 'Should the 'outs' join the Banking Union?', Policy Contribution 2016/03, Bruegel

Joint Committee of the European Supervisory Authorities (2016) List of Financial Conglomerates 2016

Kremers, J., D. Schoenmaker and P. Wierts (2003) 'Cross-Sector Supervision: Which Model?' in R. Herring and R. Litan (eds) Brookings-Wharton Papers on Financial Services: 2003, Brookings Institution, Washington DC

Lenz, R. (2017) 'Europäisches System der Finanzaufsicht effizient weiterentwickeln', written statement to the German Bundestag Finance Committee hearing, 31 May, available at https://www.bundestag.de/blob/508694/9d745061e6587ef0e86c7aa42891d2c9/13-data.pdf

Sapir, A., D. Schoenmaker and N. Véron (2017) 'Making the Best of Brexit in Finance: The EU27 Side', Policy Brief 2017/01, Bruegel

Schoenmaker, D. (2016) 'European Insurance Union and How to Get There?' Policy Brief 2016/04, Bruegel

Schoenmaker, D. and N. Véron (2017) 'EBA relocation should support a long-term 'Twin Peaks' vision', Bruegel Blog, 5 April

Taylor, M. (1995) Twin Peaks: A Regulatory Structure for the New Century, Centre for the Study of Financial Innovation, London

Taylor, M. (2009) Twin Peaks Revisited, Centre for Study of Financial Innovation, London

Véron, N. (2017) 'Charting the next steps for the EU financial supervisory architecture', Policy Contribution 2017/16, Bruegel
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
