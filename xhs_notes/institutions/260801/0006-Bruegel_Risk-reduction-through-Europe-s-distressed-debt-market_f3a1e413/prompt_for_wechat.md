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
# Risk reduction through Europe's distressed debt market

ALEXANDER LEHMANN (alexander.lehmann@bruegel.org) is a Non-resident Fellow at Bruegel

A version of this Policy Contribution was originally prepared as the in-depth section of Analysis of developments in EU capital flows in the global context, a report by Bruegel for the European Commission. It has drawn on interviews with the representatives from the European Commission, European Central Bank, European Banking Authority, a number of national institutions and numerous market participants. Comments from Maria Demertzis and Nicolas Véron are also gratefully acknowledged, as is research assistance from Inês Gonçalves-Raposo.

Alexander Lehmann

## Executive summary

THE MARKET FOR distressed debt will need to play a more prominent role in Europe's emerging strategy to tackle the legacy of non-performing loans (NPLs). This market could speed up NPL resolution and allow greater flexibility in bank balance sheet management. Investors could contribute crucial skills and possibly capital to the process of workout and restructuring.

THE LOAN SALE process potentially suffers from a number of market imperfections which manifest themselves in high valuation gaps, and in the market failing to cover certain asset types.

IN EUROPE, TURNOVER from distressed debt sales remains limited relative to the total stock of €870 billion in non-performing loans, and the additional stock of €1.1 trillion of so-called non-core banking assets, which banks also seek to divest in this market.

THERE HAS SO far been little market demand for the bulk of unsecured assets among small and medium-sized companies and other corporate borrowers, loans held by smaller banks with their higher NPL ratios, or exposures to larger enterprises that could benefit from comprehensive debt restructuring and additional finance.

SIGNIFICANT FURTHER SUPPLY might now come into the market as stricter supervisory guidelines are implemented, and as new accounting guidelines force higher provisioning levels. Improved national restructuring and insolvency regimes are beginning to attract a wider range of investors.

AN INITIATIVE BY EU finance ministers to improve transparency around loan quality and foster greater liquidity through transaction platforms might lower transaction-specific fixed costs somewhat. More decisive public support, for instance through asset management companies or in securitisation structures, might be needed.

AS A SIGNIFICANT share of Europe's banking assets might move into the hands of little-known investors, some of the benefits of relationship banking could be lost, and the conduct of the loan servicers will come into the focus of regulators.

'The euro area's gross stock of NPLs amounts to about 8.8 percent of GDP. Including other non-core assets for sale would likely yield twice that as potential supply in this market.'

# 1 Resolving Europe's non-performing loans

The resolution of non-performing loans (NPLs) is central to the recovery of Europe's banking sector and the restructuring of the excess debt owed by private sector borrowers. Banks have typically sought to deal with distressed loans through their own dedicated workout units. The prevailing view has been that debt distress is temporary, that valuable client relationships need to be preserved and that knowledge of the client and its industry means that the bank that originated the loan is best placed to oversee the restructuring.

However, it is increasingly clear that the European Union banking industry as a whole is poorly placed to address its roughly €870 billion stock of NPLs $^{1}$ . Inherently, banks do not have the governance structures or skills to oversee combined financial and operational restructurings that typically require substantial write-downs of claims and an engagement that is more akin to the management of equity positions. The realisation of this explains the heightened interest in engaging in the workout process investors who can contribute specialist skills, long term capital and economies of scale.

At the same time, the ongoing restructuring of Europe's banking systems has led banks to seek to divest substantial portfolios that no longer fit with their re-focused business strategies and their efforts to sustainably raise profitability.

Collectively, NPLs and other performing but ‘non-core’ portfolios are estimated to amount to roughly €2 trillion in gross value. Within the euro area, the gross value of the stock of NPLs amounts to about 8.8 percent of GDP. Including other non-core assets for sale would likely yield twice that as potential supply in this market. This is a substantial stock of assets, even compared to other asset types in the European debt market. Developing the market for asset transfers is therefore an important objective, relevant well beyond the immediate priority of working out distressed loans because it would underpin a broader rebalancing between banks and capital markets.

It is clear that the European secondary loans market is as yet under-developed. Relative to the stock of NPLs and other performing but non-core assets (admittedly hard to estimate), the €146 billion gross value of secondary loan transactions in 2016 represented a turnover ratio of no more than seven percent. Liquidity in EU distressed and secondary loan markets pales in comparison to that seen in episodes of combined debt and NPL resolution in other economies, where the transfer of assets from the banking system to investors accelerated immediately after crisis episodes. Moreover, liquidity in EU secondary loan markets is concentrated in just a handful of EU countries, and is not necessarily available to countries with the highest NPL stocks, or to the most problematic asset types. The market continues to function on a country-by-country basis; no cross-country portfolios have been issued and few loan-servicing companies have expanded beyond their home markets.

The European Central Bank's 2017 guidelines on banks' management of NPL portfolios (ECB, 2017a) already present loan sales as an important tool in NPL reduction, alongside the workout within the bank. Given a much greater focus on market-based solutions by supervisors, various institutions have come forward with proposals to support greater liquidity and integration of the distressed loans market. These proposals address the following aspects:

\- Enhanced transparency through standardised data templates for distressed loans and other assets, as in FSC (2017) and Mersch (2017);

\- NPL transaction platforms that could help reduce barriers to entry related to costly due diligence, thereby attracting more investors (ECB, 2017d);

\- Harmonised regulatory treatment of asset transfers, ownership of non-performing loans and the conduct of servicing companies (also in FSC, 2017);

\- The prudential treatment of securitisation and of other public-private investment struc-

tures that facilitate risk sharing and help bridge valuation gaps (ECB, 2017b);

\- The establishment of public and centralised asset management companies (AMCs), either at national level (Constâncio, 2017; Fell et al, 2017) or EU level (Haben and Quagliariello, 2017).

The European Commission's mid-term review of the 2015 action plan on building a capital markets union also envisages further measures to support secondary markets, possibly through a strengthened framework for collateral recovery, and by building on the Commission's previous initiative to simplify insolvency regimes and restructuring frameworks (European Commission, 2017).

Several of these proposals were also taken up by EU member country finance ministers, who acknowledged that an integrated EU strategy was required. July 2017 Ecofin Council conclusions endorsed several of the proposals on market functioning and better supervision, and also called for a “blueprint for national asset management companies” (Council of the EU, 2017). Work on these proposals is at time of writing underway, underlining the need for a much clearer understanding of the functioning of the secondary loans market.

## 2 Market failures and transaction costs in loan transfers

Before reviewing the various benefits that investors will bring to the workout and recovery of distressed assets, it is important to point out some of the costs and potential market failures inherent in the transfer of bank loans.

First, banks generate borrower-specific information which forms the basis for the further development of their lending. Where banks maintained resources in this type of relationship banking, including close customer contact through their branches, lending has been shown to be more resilient. This borrower-specific information cannot be easily traded in financial markets. As the loan title is transferred to investors, and likely resold subsequently, some of the benefits of relationship banking are likely to be compromised (Schäfer, 2016).

Second, the process of transferring assets consumes substantial resources. For selling banks, the selection and preparation of loan portfolios for investors is inevitably protracted, because loans will have been managed based on each bank's specific documentation standards and IT systems. Some information might not be available in digital form, and standards of public credit registries vary. First-time sellers will face substantial costs.

Investors meanwhile must engage in extended due diligence processes. They will incur substantial fees for legal advice, valuation of collateral and further engagement with the originating bank. The outcomes of bidding processes are uncertain, as is how the quality of the portfolio will change during the due diligence process (Rocha, 2016). Selling banks might withdraw parts of the portfolio, or not go ahead with the sale.

Investors in secondary loans markets also display greater risk appetites, and therefore demand higher returns, which are evident in the low valuations that are offered. It might be argued that a shift of a significant share of EU banking sector assets to investors with higher required rates of return represents a loss in terms of social welfare. However, a large part of the bid-ask spreads can be explained by the lower leverage within the funding of investment vehicles. Moreover, unlike banks, investors deduct immediately from the price the costs related to managing NPLs over the entire workout process (Ciavoliello et al, 2016).

Third, the market for transferring loans from banks to independent investors might suffer from three key market failures:

\- A concentrated investor base: investors in certain asset types incur considerable sunk costs specific to each transaction. Only a few investors have the capacity to bid repeatedly, and across a number of European markets. This might result in pricing power.

\- Information asymmetry: the inability of the originating bank to portray asset quality fully and credibly means investors will bid based on what they suspect is inferior quality, while the originating bank will hold on to higher-quality assets.

\- Externalities from the investor's restructuring work: once the investor has acquired the loan he will render services by maintaining the asset, by imposing a restructuring solution or by foreclosing. Other creditors will benefit from these solutions, and the investor will therefore demand an additional return which will reduce bid prices (ECB, 2016 and 2017b).

Each of these potential market failures might have contributed to the significant differences that can be observed between the valuations demanded by banks and those offered by investors, and to the failure of the market to clear fully.

## 3 The economic functions of liquid secondary loans markets

A number of debt and NPL crises have underlined that a good part of bank assets can be made fungible and investors can play a valuable role in loan workout and restructuring. In the Japanese banking crisis of the 1990s, for instance, investors in one year acquired nearly a third of the stock of distressed loans (Ohashi and Sing, 2004). This success in engaging investors crucially depended on a local asset management company which put in place criteria for the quality of loan documentation and collateral rights, which subsequently allowed a swift transfer to investors. Korea's banks similarly experienced a crisis from 1997. The Korean bad bank actively marketed distressed assets and encouraged the participation of foreign investors. This in turn led to the development of a domestic investor base (He, 2004).

The costs and pitfalls of asset transfers therefore need to be set against the benefits of secondary loans markets and the engagement of outside investors:

\- Efficiencies in loan servicing and workout: these result from economies of scale as the assets of several lenders are combined, and economies of scope as different asset types are handled simultaneously in judicial processes.

\- Specialist restructuring skills: some borrowers who are debt-distressed but essentially viable will benefit from specialist expertise, which is generally rare within banks, and also from additional equity and senior debt which banks would be unable to provide.

\- Containing the moral hazard problem in loan restructuring: as the relationship between the original lender and borrower is broken, viable borrowers will no longer seek restructuring solutions or contemplate ‘strategic defaults’.

\- Capital relief: the benefits for the divesting banks result primarily from a reduction in risk-weighted assets for which any additional write-down upon sale is less than the capital required had the NPL been managed internally. More broadly, the banking system will benefit because a well-developed secondary loans market will define a price for distressed and other non-core assets, helping guide balance sheet optimisation. Principles for collateral valuation and more transparent practices in enforcement and restructuring will provide a benchmark that banks will use to judge the prospects of their own restructuring efforts.

## 4 Europe's secondary loans market

Judged against the experience of earlier debt crises, the EU secondary loans market still appears underdeveloped. In 2010, the market was miniscule, even though by that point the various national banking crises were already well underway (Figure 1).

In 2016, the European secondary loans market transacted loans with a gross value of €146 billion, comprising a significant share of as yet performing assets. Total volumes remain volatile because large transactions dominate, though the 2016 figure represents an increase over previous years, and will likely have been exceeded in 2017.

Figure 1: Total loan sales and NPL stocks in the EU, 2010-16 (€ billions)  
![](images/39a26036bdd2e7bd45d4c67a7c8d4ea72122ab47653a9b165a52fd75669ab6c6.jpg)  
Source: Bruegel based on PwC and EBA. Note: Because of the limited availability of EBA NPL figures, values for NPL stocks from 2010-13 were taken from IMF Financial Soundness Indicators for some countries. Figures for loan sales were sourced from PwC because the more detailed KPMG data (see main text) does not offer a consistent history. Unlike KPMG, PwC shows a decrease in total loan sales in 2016.

Transparency in this market remains quite limited. Data comes almost entirely from private advisory firms, which track transactions that are reported in the financial press. Investor valuations of loan portfolios are not generally available, and can only be gauged from commentary about individual transactions. Non-performing assets and other non-core assets often cannot be distinguished. The latter might be performing or might be considered problematic and only subsequently turn out to be non-performing in regulatory terms. Where banks retain risk exposures to NPLs or sell to other banks, aggregate transactions will overstate the true extent of banking sector relief.

With these caveats in mind, some data sources provide a more detailed picture. Data from advisory firm KPMG for 2015 to mid-2017 suggest that four countries – the UK, Italy, Ireland and Spain – account for 80 percent of the total value of transactions. The growth in EU markets underlines that investors operate in a number of distinct and parallel national markets, rather than an integrated European market.

A number of large investment funds, many from the US, operate across all key jurisdictions. Only about a fifth of the roughly 100 investors were active in more than one market, and these investors accounted for nearly half the total sales volume. Given the very different workout procedures and legal environments, it is of course not surprising that no multi-country portfolios have emerged.

NPL stocks in Europe are concentrated in seven countries (Cyprus, Greece, Ireland, Italy, Portugal, Slovenia and Spain; Demertzis and Lehmann, 2017). However, loan sales in Greece and Cyprus, each with NPL ratios above 40 percent, remain miniscule. On the whole, the shares of bank assets sold within national banking systems shows little correlation with these countries' shares of distressed loans (Figure 2).

Figure 2: NPLs and cumulative loan sales as a share of gross loans  
![](images/4ec3ad6ed8de8c36550bee23c9adeac75e263cc25320e0df35bcced1e88cd68b.jpg)  
Source: Bruegel based on EBA and KPMG.

Figure 3: Composition of all loan sales by asset class (€ billions)  
![](images/cd205d73e33e5d2f1c2c4db42e9791271f3739eaacf4b590ae7de419cb9a6992.jpg)  
Source: Bruegel based on KPMG. Note: comprises both performing and non-performing assets. Asset types are not categorised consistently in different countries, and 'other' types comprise transactions that span several asset classes.

This is not surprising, because in several respects market activity does not match the incidence of loan distress:

\- FSC (2017) showed a striking dispersion of NPL ratios between banks of different sizes. Smaller banks had significantly larger NPL ratios, and slightly lower coverage ratios, including within individual jurisdictions. It is a concern that investors primarily seek larger transaction sizes to match the significant due diligence costs and larger banks in turn appear to be better prepared to engage investors repeatedly.

\- EBA data also underlines that NPL stocks are roughly evenly split between large enterprises, SMEs and households. This distribution is not matched by the loan sales transactions, which are primarily in secured credit in commercial and residential real estate and to a lesser extent in unsecured retail credit. Exposures to SMEs and larger enterprises so far do not sell on the secondary mar

[中间内容因长度限制已省略]

ght up exposures from several institutions they were also able to internalise the gains of any restructuring prior to a sale.

An alternative could be securitisation structures in which the public sector is exposed to some risks alongside private investors. While this would overcome problems around discerning the true quality of loans sold, these structures would further fragment the investor base, diluting investors' incentives for restructuring.

It is clear that reforms in the functioning of the EU capital market will need to be backed by reforms of national restructuring frameworks and insolvency regimes. The observed bid-ask valuation gaps in loan sales markets are related to the recovery rate, the expected cash flow in recovery and the uncertainty about the evolution of the recovery process. To the extent that national reforms speed up this process and make it more predictable, valuations will converge.

5 The Capital Requirements Regulation (CRR, Regulation (EU) 575/2013) and Directive (CRD IV, 2013/36/EU), adopted in 2013.

The development of distressed debt markets could be a new element of capital market deepening in Europe, even though the market would likely continue functioning in distinct national segments. Large asset managers already cover portfolios from several European jurisdictions in a single fund, even though of course no pan-European asset class can be defined. Gradually, the now numerous smaller investors might diversify across borders, as is already the case for loan servicers.

A process of shifting a significant share of European bank assets – potentially a gross value of up to 18 percent of GDP in the euro area – into the hands of lightly-regulated investors will need to be well governed. Public scrutiny of this new investor class will likely demand the setting out of clear codes of conduct, which will inevitably need to be based on national practice in debt resolution.

## References

Arcand, J., E. Berkes and U. Panizza (2012) 'Too much finance?' IMF Working Paper no. 12/161, International Monetary Fund

Ciavoliello, L., F. Ciocchetta, F. Conti, I. Guida, A. Rendina and G. Santini (2016) 'What's the value of NPLs?' Notes on Financial Stability and Supervision no. 3, Banca d'Italia

Constâncio, V. (2017) ‘Resolving Europe’s NPLs: challenges and benefits,’ speech to a Bruegel conference, 3 February

Council of the EU (2017) 'Council Conclusions on action plan to tackle non-performing loans in Europe,' Press Release 459/17, 11 July

Demertzis, M., and A. Lehmann (2017) 'Tackling Europe's crisis legacy: a comprehensive strategy for bad loans and debt restructuring; Policy Contribution 11/2017, Bruegel

EBA (2017) Report on results from the 2nd EBA IFRS9 impact assessment, European Banking Authority

ECB (2016) 'Addressing market failures in the resolution of non-performing loans in the euro area,' Financial Stability Review, November, European Central Bank

ECB (2017a) 'Guidance to banks on tackling non-performing loans,' European Central Bank, available at: www.bankingsupervision.europa.eu

ECB (2017b) 'Resolving non-performing loans: a role for securitisation and other financial structures?', Financial Stability Review, May, European Central Bank

ECB (2017c) Stocktake of national supervisory practices and legal frameworks related to NPLs, European Central Bank

ECB (2017d) 'Overcoming non-performing loan market failures with transaction platforms', Financial Stability Review, November, European Central Bank

European Commission (2017) ‘Mid-term review of the capital markets union action plan,’ COM(2017) 292 final

ESRB (2014) 'Is Europe overbanked?' Report of the Advisory Scientific Committee no. 4, European Systemic Risk Board

ESRB (2017) Resolving NPLs in Europe, European Systemic Risk Board

Fell, J., M. Grodzicki, R. Martin and E. O'Brien (2017) 'A role for systemic asset management companies in solving Europe's non-performing loan problems', European Economy – Banks, Regulation and the Real Sector, no. 17.1

FSC (Financial Services Committee) (2017) 'Report of the FSC Subgroup on Non-Performing Loans', Council of the European Union, Brussels, 31 May, available at http://data.consilium.europa.eu/doc/document/ST-9854-2017-INIT/en/pdf

Haben, P., and M. Quagliariello (2017) 'Why the EU needs an asset management company', Central Banking, 20 February, available at: http://www.centralbanking.com/central-banking-journal/opinion/2481794/why-the-eu-needs-an-asset-management-company

He, D. (2004) 'The role of KAMCO in Resolving Nonperforming Loans in the Republic of Korea', IMF Working Paper no. 04/172, International Monetary Fund

Mersch, Y. (2017) 'Loan-level data transparency: achievements and future prospects,' speech given on the occasion of the $5^{\text{th}}$ anniversary of the European Data Warehouse, July

Nouy, D. (2017) 'Too much of a good thing? The need for consolidation in the European banking sector', speech to the VIII Financial Forum, Madrid, September

Ohashi, K., and M. Singh (2004) 'Japan's distressed debt market', IMF Working Paper no. 04/86, International Monetary Fund

PwC (2017) Restructuring Europe's banks: Still plenty to do, report from the European Bank Restructuring Conference 2017, available at: https://www.pwc.co.uk/services/transaction-services/insights/european-bank-restructuring-conference-2017.html

Rocha, I. (2016) 'NPL resolution: prerequisites for loan portfolio sales in the CESEE region', NPL Initiative, available at http://npl.vienna-initiative.com/best-practices/

Schäfer, L. (2016) 'Forgive but not forget: the behaviour of relationship banks when firms are in distress,' EBRD Working Paper no. 186, European Bank for Reconstruction and Development
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
