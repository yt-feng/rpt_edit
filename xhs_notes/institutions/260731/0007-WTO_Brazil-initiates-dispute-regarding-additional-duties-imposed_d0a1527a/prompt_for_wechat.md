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
- 已识别机构名：`世界贸易组织`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份世界贸易组织研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
(26-5459)

Page: 1/7

Original: English

# UNITED STATES – ADDITIONAL DUTIES ON CERTAIN PRODUCTS FROM BRAZIL

# REQUEST FOR CONSULTATIONS BY BRAZIL

The following communication, dated 27 July 2026, from the delegation of Brazil to the delegation of the United States, is circulated to the Dispute Settlement Body in accordance with Article 4.4 of the DSU.

My authorities have instructed me to request consultations with the Government of the United States of America ("United States") pursuant to Article 4.4 of the Understanding on Rules and Procedures Governing the Settlement of Disputes ("DSU") and Article XXII:1 of the General Agreement on Tariffs and Trade 1994 ("GATT 1994"). This request concerns additional tariffs imposed by the United States on products originating in Brazil pursuant to two investigations initiated by the United States Trade Representative ("USTR") under Section 301 of the Trade Act of 1974, as amended ("Trade Act").

## I. Background

1. Since February 2025, the United States has imposed a series of additional tariffs on imports from its trading partners, including Brazil, in response to acts, policies, and practices that the United States unilaterally characterizes as non-reciprocal, unfair, unreasonable, or discriminatory.

2. On 13 February 2025, the US President signed a Presidential Memorandum entitled "Reciprocal Trade and Tariffs", which ordered the development of a "Fair and Reciprocal Plan". The Presidential Memorandum announced that, under that plan, the United States would counter so-called "non-reciprocal trading arrangements" by determining and imposing an "equivalent of a reciprocal tariff" with respect to each trading partner. The Presidential Memorandum instructed named US agencies, including USTR, to investigate the alleged harm to the United States resulting from such arrangements and to propose remedies in pursuit of what the United States considered reciprocal trade relations. $^{1}$

3. On 2 April 2025, the US President issued Executive Order 14257, which imposed so-called "reciprocal" tariffs on imports from numerous trading partners, including Brazil. Under Executive Order 14257, imports from Brazil became subject to an additional ad valorem duty of 10 per cent. $^{2}$ On 30 July 2025, the US President further issued Executive Order 14323, imposing an additional ad valorem duty of 40 per cent on certain products of Brazilian origin. As a result, certain Brazilian products became subject to additional duties of 50 per cent upon importation into the United States. $^{3}$

4. The United States purported to impose these additional duties under the International Emergency Economic Powers Act ("IEEPA"). On 20 February 2026, the US Supreme Court held that IEEPA does not authorize the President to impose tariffs. $^{4}$ As a result, the United States terminated the additional duties imposed under IEEPA $^{5}$ and imposed, instead, a temporary additional duty of 10 per cent under Section 122 of the Trade Act. $^{6}$ The additional duty imposed under Section 122 expired on 24 July 2026. $^{7}$

5. In parallel with these tariff actions, the United States initiated two investigations under Section 301 of the Trade Act concerning acts, policies, and practices of Brazil. These investigations, as detailed further below, resulted in additional tariffs on products originating in Brazil.

6. On 15 July 2025, at the direction of the US President, USTR initiated an investigation under Section 301 of the Trade Act into Brazil's acts, policies, and practices relating to digital trade and electronic payment services; allegedly unfair, preferential tariffs; anti-corruption enforcement; intellectual property protection; ethanol market access; and illegal deforestation ("Brazil Section 301 Investigation"). USTR initiated the investigation purportedly to determine whether the identified acts, policies, and practices were unreasonable or discriminatory, burdened or restricted US commerce, and were actionable under Section 301 of the Trade Act. $^{8}$

7. While the Brazil Section 301 Investigation was ongoing, USTR initiated a separate investigation under Section 301 of the Trade Act concerning Brazil and 59 other economies. On 12 March 2026, USTR initiated investigations into the alleged failure of these economies to impose and effectively enforce a prohibition on the importation of goods produced wholly or in part with forced labor ("Forced Labor Section 301 Investigation"). USTR initiated the investigations purportedly to determine whether the alleged failure of each investigated economy to impose and effectively enforce such an import prohibition was unreasonable or discriminatory and burdened or restricted US commerce. $^{9}$

8. On 1 June 2026, USTR determined in the Brazil Section 301 Investigation that certain acts, policies, and practices of Brazil were unreasonable or discriminatory, burdened or restricted US commerce, and were actionable under Section 301 of the Trade Act. In its Notice of Proposed Action, USTR proposed to impose an additional ad valorem duty of 25 per cent on all products originating in Brazil, subject to certain exemptions. $^{10}$

9. On 2 June 2026, USTR issued determinations in the Forced Labor Section 301 Investigation. USTR determined that Brazil had failed to impose and effectively enforce a prohibition on the importation of goods produced with forced labor and that this alleged failure was unreasonable, burdened or restricted US commerce, and actionable under Section 301 of the Trade Act. USTR proposed to impose an additional ad valorem duty of 10 per cent on products of certain investigated economies that, according to USTR, had imposed a forced labor import prohibition, undertaken relevant commitments to the United States, or established a partial regime preventing certain imports of goods produced with forced labor. For Brazil and other investigated economies that USTR considered not to fall within these categories,

USTR proposed an additional ad valorem duty of 12.5 per cent. The proposed additional duties were subject to certain exemptions. $^{11}$

10. On 15 July 2026, the US President issued a Presidential Memorandum in connection with the Brazil Section 301 Investigation, directing USTR to impose an additional ad valorem duty of 25 per cent on products of Brazil, subject to certain exemptions. $^{12}$

11. On 20 July 2026, USTR published a Notice of Action in the Brazil Section 301 Investigation implementing the President's direction. The Notice of Action imposed an additional ad valorem duty of 25 per cent on products of Brazil, subject to specified exemptions, applicable to products entered for consumption, or withdrawn from warehouse for consumption, on or after 22 July 2026. $^{13}$

12. On 23 July 2026, the US President issued a Presidential Memorandum in connection with the Forced Labor Section 301 Investigation, directing USTR to impose an additional ad valorem duty of 12.5 per cent on products of Brazil, subject to certain exemptions. $^{14}$

13. On 23 July 2026, USTR published a Notice of Action in the Forced Labor Section 301 Investigation implementing the President's direction. The Notice of Action imposed an additional ad valorem duty of 12.5 per cent on products of Brazil, subject to specified exemptions, applicable to products entered for consumption, or withdrawn from warehouse for consumption, on or after 24 July 2026. $^{15}$

14. As a result of these two Section 301 actions, products originating in Brazil are subject to additional tariffs upon importation into the United States, over and above the duties otherwise applicable under the Harmonized Tariff Schedule of the United States.

## II. Measures at Issue

15. The measures at issue in this request are:

a. the determinations made by the United States concerning acts, policies, and practices of Brazil in the Brazil Section 301 Investigation, and the resulting tariff action imposing an additional ad valorem duty of 25 per cent on products originating in Brazil, subject to specified exemptions; and

b. the determinations made by the United States concerning Brazil in the Forced Labor Section 301 Investigation, and the resulting tariff action imposing an additional ad valorem duty of 12.5 per cent on products originating in Brazil, subject to specified exemptions.

16. The measures at issue are purportedly authorized under, and/or are reflected in, implemented through, or maintained pursuant to, inter alia, the following instruments:

a. Sections 301 and 304 of the Trade Act of 1974, as amended (19 U.S.C. §§ 2411 and 2414);

b. with respect to the Brazil Section 301 Investigation:

i. the Notice of Initiation of Section 301 Investigation: Brazil's Acts, Policies, and Practices Related to Digital Trade and Electronic Payment Services; Unfair, Preferential Tariffs; Anti-Corruption Enforcement; Intellectual Property Protection; Ethanol Market Access; and Illegal Deforestation, published in the US Federal Register on 18 July 2025 (90 Fed. Reg. 34069);

ii. the Notice of Determination and Request for Comments Concerning Action Pursuant to Section 301: Brazil's Acts, Policies, and Practices Related to Digital Trade and Electronic Payment Services; Unfair, Preferential Tariffs; Anti-Corruption Enforcement; Intellectual Property Protection; Ethanol Market Access; and Illegal Deforestation, published in the US Federal Register on 4 June 2026 (91 Fed. Reg. 33854);

iii. the Presidential Memorandum of 15 July 2026 entitled Action by the United States in the Investigation Under Section 301 of the Trade Act of 1974 of Brazil's Acts, Policies, and Practices Related to Digital Trade and Electronic Payment Services; Unfair, Preferential Tariffs; Anti-Corruption Enforcement; Intellectual Property Protection; Ethanol Market Access; and Illegal Deforestation, published in the US Federal Register on 20 July 2026 (91 Fed. Reg. 45619);

iv. the Notice of Action: Brazil's Acts, Policies, and Practices Related to Digital Trade and Electronic Payment Services; Unfair, Preferential Tariffs; Anti-Corruption Enforcement; Intellectual Property Protection; Ethanol Market Access; and Illegal Deforestation, published in the US Federal Register on 20 July 2026 (91 Fed. Reg. 45516), including the modifications to the Harmonized Tariff Schedule of the United States set out in Annexes I and II thereto; and

v. any guidance or other instruments issued, or that may be issued, by US Customs and Border Protection or any other US authority implementing or administering the additional tariffs imposed pursuant to the Brazil Section 301 Investigation;

c. with respect to the Forced Labor Section 301 Investigation:

i. the Notice of Initiation of Section 301 Investigations of Acts, Policies, and Practices of Various Economies Related to the Failure to Impose and Effectively

Enforce a Prohibition on the Importation of Goods Produced With Forced Labor, published in the US Federal Register on 17 March 2026 (91 Fed. Reg. 12884);

ii. the USTR report of 2 June 2026 entitled Report in Section 301 Investigations: Acts, Policies, and Practices of Various Economies Related to the Failure to Impose and Effectively Enforce a Prohibition on the Importation of Goods Produced with Forced Labor; $^{16}$

iii. the Notice of Determinations and Request for Comments Concerning Actions in Section 301 Investigations of Acts, Policies, and Practices of Various Economies Related to the Failure to Impose and Effectively Enforce a Prohibition on the Importation of Goods Produced With Forced Labor, published in the US Federal Register on 5 June 2026 (91 Fed. Reg. 34272);

iv. the Presidential Memorandum of 23 July 2026 entitled Actions by the United States in the Investigations under Section 301 of the Trade Act of 1974 of the Acts, Policies, and Practices of 60 Economies Related to the Failure of Each Economy to Impose and Effectively Enforce a Prohibition on the Importation of Goods Produced with Forced Labor; $^{17}$

v. the Notice of Actions in Section 301 Investigations of Acts, Policies, and Practices of Various Economies Related to the Failure of Each Economy to Impose and Effectively Enforce a Prohibition on the Importation of Goods Produced with Forced Labor, including the modifications to the Harmonized Tariff Schedule of the United States set out in the annexes thereto; $^{18}$ and

vi. any guidance or other instruments issued, or that may be issued, by US Customs and Border Protection or any other US authority implementing or administering the additional tariffs imposed pursuant to the Forced Labor Section 301 Investigation.

17. This request also covers any amendments, supplements, extensions, replacement measures, renewal measures, implementing measures, or other related measures or instruments in respect of the measures identified above, including any subsequent measures that modify, replace, implement, administer, or give effect to the determinations or tariff actions described in this Section, and any related measures or instruments referred to by either party during consultations.

## III. Legal Basis for the Complaint

18. The measures at issue, as described in Section II of this request, appear to be inconsistent with the obligations of the United States under the GATT 1994 and the DSU. In particular, Brazil considers that:

a. the United States acts inconsistently with Article I:1 of the GATT 1994 because:

i. by imposing additional tariffs on products originating in Brazil under the tariff action resulting from the Brazil Section 301 Investigation, while not imposing such tariffs on like products originating in other WTO Members, the United States fails to accord immediately and unconditionally to products originating in Brazil advantages, favours, privileges or immunities accorded to like products originating in other WTO Members; and

ii. by imposing additional tariffs on products originating in Brazil under the tariff action resulting from the Forced Labor Section 301 Investigation, while not imposing such tariffs on like products originating in certain other WTO Members, and by applying a lower additional tariff rate to like products originating in certain WTO Members than the rate applied to products originating in Brazil, the United States fails to accord immediately and unconditionally to products originating in Brazil advantages, favours, privileges or immunities accorded to like products originating in other WTO Members;

b. the United States acts inconsistently with Article II:1(b) of the GATT 1994 by imposing ordinary customs duties on products originating in Brazil in excess of the bound rates set forth in the United States' Schedule of Concessions annexed to the GATT 1994, and/or by imposing other duties or charges of any kind on or in connection with the importation of products originating in Brazil in excess of those provided for in that Schedule;

c. as a consequence of the inconsistency with Article II:1(b) of the GATT 1994, the United States acts inconsistently with Article II:1(a) of the GATT 1994 because the measures at issue fail to accord to the commerce of Brazil treatment no less favourable than that provided for in the United States' Schedule of Concessions annexed to the GATT 1994;

d. the United States acts inconsistently with Article 23.1 of the DSU by seeking redress of purported violations of obligations or other nullification or impairment of benefits under the covered agreements, or impediments to the attainment of objectives of the covered agreements, through unilateral determinations and tariff actions, rather than by having recourse to and abiding by the rules and procedures of the DSU; and

e. the United States acts inconsistently with Article 23.2(a) of the DSU by making determinations to the effect that violations have occurred, benefits have been nullified or impaired, or the attainment of objectives of the covered agreements has been impeded, except through recourse to dispute settlement in accordance with the rules and procedures of the DSU.

19. Brazil considers that the measures at issue, as described in Section II of this request, nullify or impair, within the meaning of Article XXIII:1 of the GATT 1994, benefits accruing to Brazil under that Agreement.

20. Brazil reserves the right to raise further related facts and claims, including claims under other provisions of the covered agreements, during the course of consultations and in any future request for the establishment of a panel under Article 6.2 of the DSU.

Brazil looks forward to receiving a reply from the United States to this request and to fixing a mutually convenient date for the holding of consultations.
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
