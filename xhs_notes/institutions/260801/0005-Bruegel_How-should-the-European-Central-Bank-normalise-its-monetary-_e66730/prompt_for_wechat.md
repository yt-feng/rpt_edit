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
# How should the European Central Bank ‘normalise’ its monetary policy?

Grégory Claeys and Maria Demertzis

## GRÉGORY CLAEYS (gregory. claeys@bruegel.org) is a Research Fellow at Bruegel

MARIA DEMERTZIS (maria. demertzis@bruegel.org) is Deputy Director of Bruegel

This policy contribution was prepared for the European Parliament's Committee on Economic and Monetary Affairs (ECON) as an input to the Monetary Dialogue of 20 November 2017 between ECON and the President of the European Central Bank (http://www.europarl.europa.eu/committees/en/econ/monetary-dialogue.html). Copyright remains with the European Parliament at all times. The authors are grateful to Justine Feliu and David Pichler for excellent research assistance.

![](images/2deef1fd9e078b9782348ee6f8a61ee7714e48a457f3bf46c03b5970b87557ba.jpg)

## Executive summary

AS THE GLOBAL financial crisis unfolded, the European Central Bank (ECB) and other central banks greatly extended their monetary policy toolboxes and adjusted their operational frameworks. These unconventional monetary policies have left central banks with large balance sheets.

AS GROWTH PICKS up in the euro area, there are discussions about how to normalise monetary policy, but it is unclear if normalisation means returning to monetary policy as it was prior to the crisis, or whether there is a ‘new normal’ that would justify different monetary policies.

THE DEBATE ON the optimal size of the central bank's balance sheet has not yet been settled. We discuss the benefits and drawbacks of central banks having permanently large balance sheets. It might be difficult to reduce them quickly without negatively affecting financial markets. In order to avoid market volatility, this process needs to be done gradually and preferably passively, by holding to maturity assets purchased during the crisis.

THE INTEREST RATE – the central banks' main conventional tool – might stay at a much lower level than historical standards and closer to the zero-lower bound because of a fall in the neutral rate, implying that in the future monetary policy would have to rely more on balance sheet policies and less on interest rate cuts to provide accommodation during recessions.

THE COMBINATION OF these two issues implies that the normalisation of monetary policy will be very slow and entail a long period with a large balance sheet. In the meantime, the ECB will not be able to go back to its pre-crisis operational framework.

IN TERMS OF the sequencing of the normalisation process, the experience of the US Federal Reserve, which was one of the first central banks to use unconventional tools during the crisis, could provide useful pointers to the ECB. Following the Fed's example would involve tapering (ie gradually reducing asset purchases), then increasing key policy rates slowly before reducing passively the size of the balance sheet.

THE FED'S EXPERIENCE shows that the normalisation process needs to be communicated early in order to reduce uncertainty for market participants and avoid any disruption of financial markets. So far, the ECB has been quite successful in smoothly scaling back its asset purchases, but it has not yet provided a clear vision of what its monetary policy or operational framework will look like at the end of the normalisation process.

## 1 Introduction

Since the start of the global financial crisis in 2008, the European Central Bank (ECB) has increased the means through which it provides monetary stimulus. These unconventional monetary policies have de facto increased the scope of its actions and have direct implications for aggregate demand management and for financial stability. The main characteristic of monetary policy in recent years is that the main instrument, the interest rate, has been at the zero lower bound (ZLB) and has de facto become inactive, leading the ECB to follow in the footsteps of the US Fed and use other ways to implement monetary policy.

While necessary and important, applying unconventional tools might not be without risks. When these tools were introduced there was general consent that while they were a useful addition to central banks' toolkits, they ought to be of a temporary nature. There needs to be therefore a clear and transparent plan to discontinue them in order to start the process of 'normalisation'. In this paper, we discuss the parameters of this normalisation process. While when this process should take place is an important question, it is not our focus here. We discuss how the ECB should implement 'normalisation' and what the 'new normal' might look like.

We begin our discussion by describing the ECB's toolbox and operational framework since its establishment and how they have changed since the start of the financial crisis.

Section 3 describes normalisation experiences so far. We draw primarily from the experience of the Fed, which was much quicker to introduce unconventional monetary policies, in particular large-scale asset purchases, and has now already started to reverse them.

We then discuss in section 4 what the destination of this normalisation process could or indeed should be. We argue that unconventional monetary policy has led to large central bank balance sheets, which will be very difficult to reduce over a short period. At the same time, central banks might not be able to rely on the interest rate itself to manage the economy as they could before the crisis. This is because the neutral interest rate appears to have fallen closer to zero, leaving less scope to reduce rates in future recessions to boost aggregate demand. By implication, monetary policy will take place with large balance sheets and the use of balance sheet measures might need to be frequently relied on. The new normal for monetary policy is therefore more likely to be characterised by a combination of interest rate moves and balance sheet measures, negating the temporary nature of unconventional monetary policies. In that case then the ECB will have to learn how to conduct monetary policy with a large quantity of reserves in the system.

Finally, section 5 discusses the sequencing of the normalisation process in which the application of unconventional tools will be reduced. As the Fed is much more advanced in this process, its experience is again very instructive. The Fed began with tapering (ie gradually reducing its asset purchases) before moving on to interest rate increases and lastly an actual reduction in the size of its balance sheet by limiting the reinvestment of maturing assets. We discuss how this might be the safest way of managing a very unfamiliar process while providing maximum predictability. While announcing the timing in advance might be the ideal way of reducing uncertainty, it will be difficult to get this right. A better alternative would be to describe the conditions needed for this normalisation process to begin, to explain how it will take place and what the goal of the process will be. The job of central bank communication will be to describe these elements carefully and provide them early in the process.

## 2 The European Central Bank's conventional and unconventional toolkits

## 2.1 Strategy and operational framework before the crisis

From its creation in 1999 to the beginning of the crisis in 2007, the ECB put in place a simple strategy combined with a fairly efficient operational framework. The ECB focused on price stability, its main objective mandated by the EU Treaties. The ECB's Governing Council defined price stability as a year-on-year increase in the Harmonised Index of Consumer Prices (HICP) for the euro area of below, but close to, 2 percent over the medium term. The main instrument to achieve this objective was the short-term interest rates in order to influence the rest of the yield curve. The operational target of the ECB was the Euro Overnight Index Average (EONIA) rate –the weighted average of all overnight unsecured lending transactions in the euro-area interbank market – given its role as a benchmark for other medium and long-term market rates relevant for the real economy.

In that period, the ECB used three main instruments to control the EONIA rate: 1) weekly main refinancing operations (MROs) and monthly long-term refinancing operations (LTROs) of three months, which took the form of variable-rate fixed-volume tenders; 2) marginal lending and deposit facilities, whose rates formed a corridor of +/- 100 basis points (bp) around the MRO rate; and 3) reserve requirements for banks at 2 percent of certain bank liabilities, mainly customers' deposits and debt securities with a maturity below two years $^{1}$ . As a result of this operational framework and strategy, the ECB's balance sheet size was relatively low $^{2}$ , and overall from 1999 to 2007, the execution of monetary policy of the ECB consisted mainly of varying its three key interest rates in line with the business cycle and the inflation outlook in order to fulfil its price-stability mandate.

## 2.2 Changes to the operational framework and new tools since 2007

Since 2007, the ECB has been challenged by an unprecedented financial and economic crisis. The euro area faced two recessions in the space of five years, persistent low inflation and material deflation risks that have led to inflation being well below target for almost a decade. This has led the ECB to adjust its main instruments and to introduce new tools in order to pursue price stability and to safeguard financial stability.

Following the US sub-prime crisis, the ECB sought to support bank liquidity when short-term funding was hardly available and the interbank market ceased to function. During the market freeze that followed the failure of Lehman Brothers in September 2008, generating a risk of European banking sector meltdown, the ECB quickly played its role of lender of last resort (LoLR) for illiquid but solvent banks.

The ECB increased massively its liquidity provision to the banking sector from 2007-2012 and introduced a number of measures to prevent a credit crunch through ‘enhanced credit support’. Liquidity started to be allocated, through its main refinancing operations (MROs) and long-term refinancing operations (LTROs), on a fixed-rate and full-allotment basis. This meant that banks had unlimited access to central bank liquidity as long as they could provide adequate collateral.

Collateral requirements were also eased a number of times. In addition, the maturity of LTROs – originally of three months only – was lengthened, introducing operations with maturities of, first, six months, then one year and eventually, by conducting two massive long-term refinancing operations, with a maturity of three years (in December 2011 and February 2012). The cumulative take-up of these two operations exceeded €1 trillion (although part of it replaced the borrowing through other maturities, see Figure 1, panel B). Later, from 2014 to

2017, an additional series of four-year Targeted Long-Term Refinancing Operations (TLTROs) was launched to refinance European banks at very low interest rates and to encourage them to extend credit to the real economy. The operations are targeted because the amount counterparties can borrow from the ECB is linked to their loans to non-financial corporations and households. Therefore, these measures are directly aimed at facilitating lending to the real economy, rather than solely improving the liquidity condition of credit institutions.

Figure 1: ECB monetary policy since 1999  
![](images/bbc5f03151ab88b7ef3fa37df88be3642831c1e5c6b5909c760ea22bdc5110de.jpg)  
Source: ECB via Bloomberg.

![](images/8eefe8c88a651993470cf0db7fcc33ba393f6c1c1ea7923cc1439dbcbe3b3b1a.jpg)

Additionally, the ECB engaged in its first asset purchase programme in June 2009. The €60 billion covered bond purchase programme (CBPP1) was aimed at reviving the covered bond market, which is a primary funding source for banks.

Furthermore, the required reserve ratio was reduced from 2 percent to 1 percent and eligibility of assets used as collateral for monetary operations was further extended to lower rated ABSs and other performing credit claims. To further improve conditions in the covered bond lending market, the ECB launched in November 2011 a second CBPP with a total volume of €40 billion. The ECB nevertheless decided to interrupt the programme in October 2012, after covered bonds totalling only €16.4 billion had been purchased.

In terms of rate cuts, the ECB cut its MRO rate from 4.25 percent to 1 percent between October 2008 and May 2009 (see Figure 1, panel A). After mistakenly hiking rates twice in 2011, the ECB reversed them and lowered further its policy rates. As a result, the deposit facility rate reached zero in July 2012 and entered negative territory in June 2014. The MRO rate finally reached 0 percent in July 2016. Constrained by the zero-lower bound (ZLB) and the resulting difficulty of making an impact and lowering the whole yield curve, the ECB decided in July 2013 to introduce ‘forward guidance’ as an additional monetary policy tool. During the introductory statement of the press conference, President Draghi announced that “the Governing Council expects the key ECB interest rates to remain at present or lower levels for an extended period of time”. The idea was to better anchor expectations about the future path of interest rates and weigh on the long-end part of the yield curve.

Finally, the ECB decided to complement its existing instruments with additional measures in order to reduce deflationary dynamics in the economy and ultimately to reach its inflation target. Therefore, to further provide monetary policy accommodation, the ECB introduced asset-backed securities (ABS) purchases and its third covered bond purchase programme. Given that inflation and inflation expectations were still slowly drifting downwards away from the ECB's target, the ECB decided in January 2015 to significantly step up its quantitative easing programme through its ‘expanded asset purchase programme’ (APP). The programme, built on the two existing asset purchase programmes, additionally encompasses the ‘public sector purchase programme’ (PSPP) and the ‘corporate sector purchase programme’ (CSPP)

introduced in March 2015 and June 2016 respectively. With an initial average monthly pace of asset purchases of €60 billion in March 2015, the ECB raised its target to €80 billion in April 2016.

Overall these measures resulted in the quadrupling of the size the European System of Central Banks (ESCB)'s balance sheet (Figure 1, panel B).

Table 1: Summary of the changes in the ECB's toolbox during the crisis

<table><tr><td></td><td>Instrument</td><td>Pre-crisis</td><td>In 2017</td></tr><tr><td rowspan="3">Open market operations</td><td>Main refinancing operations</td><td>Variable-rate, limited quantity tenders, minimum bid rate</td><td>Fixed-rate full-allotment tenders</td></tr><tr><td>Long term refinancing operations</td><td>Max 3-month maturity</td><td>Increased length up to 3 years + Targeted LTROs with 4-year maturity Fixed-rate full-allotment tenders</td></tr><tr><td>Collateral</td><td></td><td>Extension of eligibility</td></tr><tr><td rowspan="2">Standing facilities</td><td>Deposit Facility</td><td rowspan="2">Corridor: MRO rate +/-1%; EONIA close to MRO rate</td><td rowspan="2">Corridor: compressed and asymmetric, EONIA close to deposit rate</td></tr><tr><td>Marginal Lending Facility</td></tr><tr><td>Reserve requirements</td><td>Minimum reserves</td><td>2% of deposits, debt securities &lt;2 years</td><td>1% of deposits, debt securities &lt;2 years</td></tr><tr><td rowspan="5">Asset purchase programmes</td><td>Securities Market Programme</td><td>-</td><td>SMP</td></tr><tr><td>Covered Bond Purchase Programme</td><td>-</td><td>CBPP1, CBPP2, CBPP3</td></tr><tr><td>Corporate Sector Purchase Programme</td><td>-</td><td>CSPP</td></tr><tr><td>Public Sector Purchase Programme</td><td>-</td><td>PSPP</td></tr><tr><td>Asset-Backed Securities Purchase Programme</td><td>-</td><td>ABSPP</td></tr></table>

Source: Bruegel based on ECB.

## 3 The normalisation of monetary policy so far

## 3.1 The Fed's experience

The Fed started its large-scale asset purchase programme soon after the crisis hit the US economy. Shortly before the federal funds target rate got close to the zero-lower bound (in December 2008), the Fed announced its first quantitative easing (QE) programme aimed at purchasing mortgage-backed securities worth \$600 billion. The second round followed in November 2010, with purchases of \$600 billion of US treasury securities. QE3 came at the end of 2012, with initial monthly bond purchases of \$40 billion. QE3 was an open-ended programme that signalled further possible accommodation if necessary. Soon after the launch the monthly target was raised to \$85 billion.

The normalisation of US monetary policy started on the wrong foot when the market reacted violently to Ben Bernanke's unexpected announcement in spring 2013 that the Fed would likely start tapering (ie slowing the pace of its bond purchases) later in the year, conditional on continuing good economic news. As a result, long-term US yields and the value of the dollar relative to other currencies rose quickly and significantly, as market participants had not expected the reduction of monetary stimulus to start early. This episode became known as the ‘taper tantrum’. Finally, after more than one year of QE3, the Fed effectively decide to start tapering in December 2013. It ultimately stopped its asset purchases in October 2014 after reducing them by \$10 billion per month.

However, the Fed's normalisation strategy was first discussed extensively at a very early stage in the process, at the 22 June 2011 Federal Open Market Committee (FOMC) meeting. Shortly before the large-scale asset purchases were phased out, the Fed (2014) provided more details in its ‘Policy Normalisation Principles and Plans,’ in which it explained that in the long run it wished to conduct monetary policy similarly to before the financial crisis. Without pre-determining the timing, the road map included three main actions: a) lifting the interest rate range target $^{3}$ ; b) ending the reinvestment of asset purchases; and c) shrinking the balance sheet to a level at which the Fed would “hold no more securities than necessary to implement monetary policy efficiently and effectively”. On 16 December 2015, given improved economic activity and an inflation outlook in line with the 2 percent inflation target, the Fed decided to lift its policy rate targets by 25 bp for the first time since the financial crisis. Since then th

[中间内容因长度限制已省略]

ssary. These include: raising interest rates even with a large balance sheet, increasing reserve requirements, using reverse repo operations or issuing ECB securities to drain excess liquidity if credit were to accelerate as a result of excess liquidity $^{16}$ .

\- Allow the balance sheet to shrink passively by holding the assets purchased to maturity. In particular, if the ECB publishes a roadmap, it should make it clear that this is indeed its intention.

In the long run, having a lean balance sheet would allow the ECB to return to its pre-2007 operational framework with a well-functioning interbank market. But this might not be desirable in the short run because a quick reduction of its balance sheet could be disruptive. In the long run it might not be easily feasible, if neutral rates in particular stay at the current low level. Low neutral rates reduce the scope for rate cuts in the future and increase the need to use QE as a monetary policy tool more frequently.

Even if the ECB wants to reduce the size of its balance sheet, it needs to reckon with a long period: excess liquidity will be absorbed gradually by the increase in currency in circulation and reserve requirements that grow mechanically with the economy. But letting the balance sheet shrink passively will still take approximately 14 years to before the pre-crisis level in terms of GDP (thanks to both real growth and inflation).

If the ECB accepts that its balance sheet might not be as lean in the future as it was before the crisis, it will have to deal with the consequences for its operational framework and revise how it conducts monetary policy and how its policy stance is transmitted to the real economy.

## References

Altavilla, C., M. Boucinha and J.L. Peydró (2017) 'Monetary policy and bank profitability in a low interest rate environment', Working Paper No. 2105, European Central Bank

Asness, C., M.J. Boskin, R.X. Bove, C. Calomiris, J. Chanos, J. Cogan, N. Ferguson, N. Gelinas, J. Grant, K. Hassett, R. Hertog, G. Hess, D. Holtz-Eakin, S. Klarman, W. Kristol, D. Malpass, R. McKinnon, D. Senor, A. Shlaes, P. Singer, J.B. Taylor, P. Wallison and G. Wood (2010) 'Open Letter to Ben Bernanke', Hoover Institution, 15 November, available at https://www.hoover.org/research/open-letter-ben-bernanke

Bernanke, B. (2017) 'Shrinking the Fed's balance sheet', Brookings Blog, 26 January, available at https://www.brookings.edu/blog/ben-bernanke/2017/01/26/shrinking-the-feds-balance-sheet/

Bindseil, U. (2016) 'Evaluating monetary policy operational frameworks', speech to the symposium on 'Designing resilient monetary policy frameworks for the future,' Jackson Hole, Wyoming, 26 August

Bank of Japan (2016) 'Key Points of Today's Policy Decisions', 29 January, available at https://www.boj.or.jp/en/announcements/release\_2016/k160129b.pdf

Bonis, B., J. Ihrig and M. Wei (2017) 'Projected Evolution of the SOMA Portfolio and the 10-year Treasury Term Premium Effect', FEDS Notes, Washington: Board of Governors of the Federal Reserve System, available at https://www.federalreserve.gov/econres/notes/feds-notes/projected-evolution-of-the-soma-portfolio-and-the-10-year-treasury-term-premium-effect-20170922.htm

Borio, C. (2001) 'A hundred ways to skin a cat: comparing monetary policy operating procedures in the United States, Japan and the euro area,' BIS Papers No. 9

16 The latter will probably not even be necessary because credit creation is mainly limited by prudential regulation, risk management of bank, level of interest and demand for credit from firms and households.

Claeys, G. (2016) 'The decline of long-term rates: bond bubble or secular stagnation symptom?' Policy Contribution 2016/16, Bruegel

De Santis, R.A. and F. Holm-Hadulla (2017) 'Flow effects of central bank asset purchases on euro area sovereign bond yields: evidence from a natural experiment,' Working Paper No. 2052, European Central Bank

Demertzis, M. and G.B. Wolff (2016) 'What impact does the ECB's quantitative easing policy have on bank profitability?' Policy Contribution 2016/20, Bruegel

ECB (2011) The implementation of monetary policy in the euro area, European Central Bank, available at https://www.ecb.europa.eu/pub/pdf/other/gendoc201109en.pdf

ECB (2017) 'Base Money, Broad Money and the APP', ECB Economic Bulletin, Issue 6/2017, European Central Bank

Fed (2011) 'Minutes of the FOMC meeting', 22 June, available at https://www.federalreserve.gov/monetarypolicy/fomcminutes20110622.htm

Fed (2014) 'Policy Normalisation Principles and Plans', 16 September, available at https://www.federalreserve.gov/monetarypolicy/files/FOMC\_PolicyNormalisation.pdf

Fed (2015) 'Policy Normalisation Principles and Plans,' amended in 2015, available at https://www.federalreserve.gov/monetarypolicy/files/FOMC\_PolicyNormalisation.20150318.pdf

Fed (2017) 'Policy Normalisation Principles and Plans,' amended in 2017, available at https://www.federalreserve.gov/monetarypolicy/files/FOMC\_PolicyNormalisation.20170613.pdf

Haincourt, S. (2017) 'Exchange rate impact on the US and euro area', Eco Notepad, Banque de France blog, 15 March, available at https://blocnotesdeleco.banque-france.fr/en/blog-entry/exchange-rate-impact-us-and-euro-area

Holston, K., T. Laubach and J.C. Williams (2017) 'Measuring the natural rate of interest: International trends and determinants,' Journal of International Economics 108/1: 59-75

Moghadam, R. (2017) 'Europe needs a non-standard exit from its monetary stimulus', Financial Times, available at: https://www.ft.com/content/5ee8fa84-34df-11e7-99bd-13beb0903fa3

Sims, C. (2016) 'Fiscal policy, monetary policy and central bank independence,' Jackson Hole Lunch Seminar, 23 August
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
