你是麦肯锡/研究导读风格的微信公众号文章主笔，擅长用金字塔原理把报告内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给专业读者/产业决策者的报告导读。
- 长度：约 1200 字，整体以短导读为主，通常控制在 900-1200 个中文字符。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，只讲最关键的判断、图表和未解问题，让读者有动力去看原文。
- 文章必须像人工编辑润色过的报告导读：句长有变化，段落有呼吸感，不要整齐排比，不要反复使用“这意味着/真正重要的是/换句话说/从这个角度看”等模板转折。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、市场定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须短、锐利、可转发，优先 20-35 个中文字符，最长不超过 35 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 要兼顾微信搜一搜：尽量包含一个高意图关键词，例如行业/公司/政策/AI/房地产/半导体/光伏/消费/美联储/利率/通胀/机器人/比特币等。
- `# 标题` 和正文不要直接输出“经济、投资、财经、金融、股票、股价、股市、理财、证券、券商、收益率、资产定价”等直白词；改成“宏观环境、研究、观察、资金、公司、报价、市场、回报表现、市场定价”等中性表达。
- 涉及中国、国内、内地、大陆、人民币、A股、港股时，必须使用中性客观表达；不要写“不好、不行、疲弱、低迷、恶化、危机、衰退、崩盘、放缓、压力、拖累、唱衰”等负面判断。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`亚洲开发银行`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
- 标题禁止出现 GS、JPM、JEF、NOM、BARC、MS、DB、Citi、Ticker、文件编号；如果原文只有英文机构名，请翻译为中文机构名。
- 标题冒号后不要重复机构或来源类型，禁止“联合国贸发会议：联合国贸发报告，……”“麦肯锡：麦肯锡报告称，……”这类写法；冒号后直接写判断或变量。
- 标题只能保留一层信息，不要把多个长分句全部塞进标题；如果原始标题有三段以上信息，只取最有传播性的主判断，其余放在正文第一段自然展开。
- 如果报告是单一公司/个股报告，标题和正文只能写公司情况、行业变化、业务进展、竞争格局和报告里的事实；禁止出现目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO 等任何卖方操作口径。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
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
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，20-35 个中文字符。
2. 开头 2-3 段：直接给出主判断、为什么现在重要、报告提供了什么新信号；自然带出 4-6 个长尾关键词，覆盖国家/行业/公司/政策/数据/技术词，但不要写成关键词堆砌。
3. 3-4 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 1-2 个 `> **KC评论：** ...` 引用块，每个 1-2 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，不要夹带任何推广话术。
5. 正文中间禁止插入 CTA、广告、扫码、社群、知识星球、每日汇编、喂给 AI 等表达；中间只允许出现分析正文、图表占位和 `KC评论`。
6. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
7. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
8. 不要写任何 CTA、广告、扫码、社群、知识星球、网站、域名或关注引导；系统会在最结尾统一插入固定信息。
9. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
10. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.</p>`

【CTA 要求】
- 不要输出任何 CTA。不要写“加入社群”“扫码”“星球”“完整报告领取”“网站”“域名”“关注”“星标”“更多查看”等表达。
- 文末也不要写 CTA；系统会在最结尾统一插入固定信息。
- 正文中间不要出现“如果你从某些关键词搜到这里”“单篇文章只能解决一个切片”“我每天会把……”“这篇可以沿着……”这类表达。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份亚洲开发银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
No. 2026-10 (July)

## Key Points

\- Mediation is an amicable dispute resolution tool that is speedy, cost-effective, flexible, and tailored to the needs of the disputing parties, which can facilitate trade and investment.

\- However, the merits of mediation may not be fully realized in investor–state disputes due to the unique characteristics of governments, including accountability concerns, diverse stakeholders, and transparent and equitable rule-based administration.

\- Mandatory mediation, clear mandates, coordination among line ministries, and the involvement of globally reputable institutions such as the International Centre for Settlement of Investment Disputes (ICSID) can enable a state to use mediation in investor–state disputes.

\- Ratifying the Singapore Convention on Mediation, which ensures the enforceability of mediated settlement agreements, can facilitate the broader use of mediation, including in investor-to-state disputes.

\- Capacity building for enhancing awareness of investment mediation should be carried out in a targeted, tailored, and systemic manner.

# Ways to Promote Mediation in Investor-to-State Disputes

Byungsik Jung, Deputy Dean, Asian Development Bank Institute

## 1. Introduction

Foreign direct investment (FDI) is crucial for economic growth in developing countries because it brings new capital for job creation and industrial development. Many countries have bilateral investment treaties or free trade agreements that include investment chapters to induce FDI by securing foreign investors' rights to protect their assets in a host country. Alternative dispute resolution systems such as mediation and arbitration are well embedded in most international investment treaties to resolve disputes arising in the course of foreign direct investment.

In the case of arbitration, it has frequently been used as the main tool to address disputes between an investor and a state because both disputing parties can select an independent arbitrator who adjudicates their case, and the arbitral decision is enforceable through the New York Convention $^{1}$ or the International Centre for Settlement of Investment Disputes (ICSID) Convention. $^{2}$ Arbitration is costly because it follows a quasi-judicial process, including discovery and hearing procedures for fact-finding. This high cost has been burdensome for both host countries and investors. Furthermore, the arbitrator's adjudication may not meet the expectations of both disputing parties, similar to court rulings.

In this context, mediation has drawn increasing attention. Mediation offers several advantages over arbitration, including lower costs, faster resolution, greater flexibility, and party-controlled outcomes. A mediator facilitates negotiations between disputing parties, helping them reach a mutually satisfactory solution. Unlike arbitration, mediation avoids time-consuming procedures such as document discovery, formal advocacy by legal counsel, and the establishment of an arbitral tribunal. As a result, mediation is typically quicker and more cost-effective. Moreover, mediation allows the parties themselves to determine the outcome through negotiation, in contrast to arbitration, where the arbitral tribunal issues a binding award that the parties must accept.

Recognizing these benefits, ICSID and the United Nations Commission on International Trade Law (UNCITRAL) have introduced investment mediation frameworks, $^{3}$ particularly for investor–state disputes. Their rules encourage mediation as a preliminary step before arbitration, based on the belief that mediation enables both the state and the investor to better understand each other's interests and to arrive at tailored solutions. ICSID reports that there are 40 known instances of mediation in investor–state disputes, that the mediation process typically takes around 6 months to 1 year, and that total costs range from approximately \$25,000 to \$1 million (Nitschke 2026). By contrast, the average duration of investment arbitration is 4 years, and its cost is about \$4.7 million for a host country and \$4 million for an investor (BIICL and Allen & Overy 2021). ICSID statistics indicate a strong possibility that mediation in investor–state disputes will increase, as around 20% of ICSID arbitration cases have been settled between investors and states before an arbitral award is issued (ICSID 2026).

The implementation of mediation in investor–state dispute settlement (ISDS) may face difficulties due to the unique characteristics of governments. Unlike commercial entities, states operate under different constraints and priorities, which may limit their ability to engage in flexible, interest-based negotiation. This policy brief assesses the challenges of conducting mediation in ISDS and explores ways to promote its effective use in practice, particularly from a government perspective.

## 2. Process of Investment Mediation

Before diving deeply into the challenges of mediation in ISDS, it is worthwhile to first provide an overview of the general process of mediation in ISDS. The UNCITRAL Model Provisions on Mediation (2021), the UNCITRAL Guidelines on Mediation for International Investment Disputes (2023), and the ICSID Mediation Rules (2022a) set out the process of mediation in ISDS, and ICSID explains the flow of the mediation process in investor-to-state disputes in a background paper on investment mediation (ICSID 2021). Given that mediation is an extended negotiation supported by a third party, namely a mediator, eight steps can be identified: (i) negotiation between both parties, (ii) appointment of mediators, (iii) the first meeting with mediators and explanation of ground rules, (iv) exchange of objectives and agenda setting, (v) private sessions, (vi) joint sessions, (vii) a mediated agreement, and (viii) implementation. For clarity, this policy brief uses a hypothetical case in which a foreign investor has a dispute with a host country that has canceled mining rights for environmental protection purposes.

## 2.1 Extended Negotiation

Mediation derives from the parties' negotiation. If both parties face difficulties in making progress in their negotiations, they seek the support of a mediator to facilitate the process. In this sense, mediation can be understood as structured negotiation facilitated by a mediator. In the hypothetical example above, the disputing parties bring in an internationally well-known former judge to mediate their negotiation.

## 2.2 Appointment of Mediators

There are three types of mediators: facilitative mediators, evaluative mediators, and transformative mediators (Shonk 2026). A facilitative mediator encourages disputing parties to negotiate and reach a settlement by facilitating communication. An evaluative mediator guides the negotiation by sharing views on the issues and suggesting possible solutions, if requested by the disputing parties. A transformative mediator seeks to build mutual recognition and empathy to improve the quality of interaction between the parties. Given that investor–state disputes attract extensive public attention and are likely to lead to adjudicatory arbitration, an evaluative mediator appears to be most appropriate in ISDS.

## 2.3 First Meeting and Ground Rules

A mediator explains the ground rules of mediation: mediation is voluntary, and each party may withdraw at any time. Each party is expected to listen respectfully to the other party's statements. In addition, the mediator explains the overall process of mediation. In the hypothetical example, the former judge explains the ground rules and the main process of the mediation to the disputing parties.

## 2.4 Exchange of Objectives and Agenda Setting

Each disputing party outlines its objectives and desired outcomes. The mediator and the disputing parties jointly set the main agenda after identifying each party's objectives and interests. In the hypothetical example, the investor may seek revocation of the cancellation and compensation for damages incurred, while the host country may argue that the cancellation is unavoidable due to nationally determined contribution (NDC) commitments and pressure from the local community, although compensation could be negotiable. The mediator and the disputing parties may therefore set two key agenda items: extension of permission and compensation.

## 2.5 Private Sessions

A mediator may hold separate private sessions with each disputing party to clarify their interests and explore potential solutions. The mediator may propose solutions if requested. Information disclosed in private sessions must not be shared with the other party without consent. In the hypothetical case, the investor may reveal that its primary interest is to extend the mining permit during a transition period, while the host country may indicate that a limited extension is possible if the investor contributes financially to the local community. The mediator may suggest focusing on an extension of permission combined with reasonable compensation.

## 2.6 Joint Sessions

In joint sessions, the mediator clarifies each party's interests and facilitates negotiations on the main agenda items. The mediator may propose solutions for consideration if requested by both parties. In the hypothetical case, negotiations focus on extending the mining permit and determining reasonable compensation. The mediator may present possible solutions based on insights obtained from both private and joint sessions.

## 2.7 Mediated Agreement

If both parties reach agreement, the mediator drafts a detailed settlement agreement, including terms, conditions, confidentiality provisions, implementation arrangements, monitoring mechanisms, governing law, and procedures for resolving future disputes. In the hypothetical case, the parties may agree that the host country will extend the mining permit for an additional 10 years, while the foreign investor will provide job-transition training for affected workers and establish a \$2 million fund for environmental compensation and restoration of the polluted areas. They may also agree to establish a joint monitoring committee to oversee implementation and to keep information obtained during the mediation confidential. The agreement should reflect these commitments and confirm that both parties entered into the agreement voluntarily and that the mediator acted as a neutral third party who facilitated negotiations without imposing a decision.

## 2.8 Implementation of the Mediated Agreement

The mediated settlement has a strong likelihood of being implemented because both parties participate in developing and agreeing to the solution. If a party fails to comply, the agreement can be enforced by domestic courts through standard contractual enforcement procedures. In other words, a party files a claim before a court seeking enforcement of the mediated settlement agreement, and the court may reexamine the merits of the dispute before rendering a judgment. Where a party's country has ratified the Singapore Convention, the mediated settlement agreement may be enforced directly without additional domestic procedures required for general contract enforcement. In the hypothetical case, if the foreign investor fails to establish the \$2 million fund required under the mediated settlement agreement, the host country may seek direct enforcement of the agreement under the Singapore Convention and, where permitted by domestic law, obtain measures such as the seizure of the investor's assets.

## 3. Unique Characteristics of States That May Hinder Investment Mediation

While mediation offers many advantages, its application in investor–state disputes is likely to face challenges due to the distinct nature of states compared to commercial entities. These challenges stem from concerns about accountability, the presence of diverse internal and external stakeholders, transparent and equitable rule-based administration, and uncertainty regarding the enforceability of mediated settlements.

## 3.1 Concerns About Accountability

Government officials are highly sensitive to accountability because any flaws in the process or outcomes of their activities may result in serious consequences for their careers. Therefore, they tend to adhere strictly to rules and regulations and are likely to seek guidance from their superiors when discretion is required. For example, when a complaint is raised by a foreign investor, a government official would not engage in negotiations unless such engagement was permitted by applicable laws and regulations. Even when negotiations are lawfully initiated, officials are unlikely to deviate from their given mandates.

This concern about accountability extends beyond individual officials. Each ministry has clearly defined areas of responsibility under applicable laws and regulations. When an investment dispute involves multiple ministries, the relevant ministries are expected to coordinate their response, including designating a representative of the government to engage with the foreign investor. In practice, however, coordination among line ministries is not easy without preestablished rules and procedures, as no ministry wishes to assume responsibility beyond its formal mandate.

## 3.2 Diverse Stakeholders

Foreign direct investment involves not only the Ministry of Investment but also other ministries, such as those responsible for the environment, finance, and local governance, depending on the case. For example, in the Lone Star v. Republic of Korea case, $^{4}$ where Lone Star alleged that Korean authorities delayed and politically interfered with its ability to sell Korea Exchange Bank, imposed unfair tax measures, and undermined the value of its investment, the Republic of Korea established a formal cross-ministerial task force. This task force included the Prime Minister's Office, Ministry of Justice, Ministry of Finance and Economy, Ministry of Foreign Affairs, Ministry of Trade and Industry, Financial Services Commission, and National Tax Service. This demonstrates that multiple internal stakeholders within the government must have their interests reflected during mediation between a state and a foreign investor.

In addition, there are stakeholders outside the government, including Congress, civic groups, and the general public, often represented by the mass media.

In some cases, the investor's home country may also act as a diplomatic stakeholder. Government activities are typically reported to Congress, shared with civic groups, and disclosed to the public. As transparency increases, so does the demand for information. In the Republic of Korea, investor–state dispute cases are closely scrutinized, and any issues or criticisms arising during mediation may be subject to review by Congress or the Board of Audit and Inspection and, in extreme cases, investigation by law enforcement authorities.

It is also important to note that the public tends to view the state as sovereign and expects the government to defend national interests vigorously. As a result, any concession made by the government in a dispute is often perceived as unfavorable or unjust. Such expectations tend to push governments to maintain rigid positions rather than pursue amicable solutions, even when the likelihood of success in arbitration is low.

## 3.3 Transparent and Equitable Rule-Based Administration

Government administration is governed by laws and regulations, which must be applied uniformly without granting special treatment to parties in similar circumstances. Although governments may exercise discretion, such discretion is subject to strict scrutiny to ensure compliance with legal boundaries. For example, if a state grants a mining permit to one foreign investor, it must provide equivalent treatment to others in similar circumstances. Accordingly, governments are cautious about creating precedents that may affect future administrative decisions.

Mediation, by its nature, produces tailored solutions that address the specific needs of the disputing parties. Such settlements are generally intended to remain confidential unless both parties agree otherwise. However, in disputes involving public interests, confidentiality is difficult to maintain, as stakeholders, including Congress and civic groups, often demand disclosure. The nondisclosure of key elements, if later revealed, may lead to misunderstandings and serious repercussions.

If key elements of a mediated settlement are disclosed, other domestic or foreign investors may seek similar treatment. International agreements, including free trade agreements, investment treaties, and tax treaties, typically include national treatment obligations requiring equal treatment of domestic and foreign investors in like circumstances. Some agreements also contain most-favored-nation provisions requiring treatment no less favorable than that accorded to investors from third countries. Granting favorable treatment to a specific investor may therefore raise concerns of treaty violations, even if the circumstances differ.

## 3.4 Uncertainty of Enforceability of Mediated Settlement

Arbitral awards are widely enforceable because 172 countries have ratified the New York Convention on arbitration. By contrast, although the Singapore Convention on Mediation entered into force in September 2020, its coverage remains limited, with only 22 countries having ratified it as of May 2026 (United Nations Commission on International Trade Law n.d.). As a result, hybrid mechanisms such as med-arb or arb-med-arb are often recommended, as they allow mediated settlements to be incorporated into arbitral awards that are enforceable under the New York Convention. Mediated settlement agreements may also be enforced by domestic courts under general contract law, provided that the necessary legal requirements are met.

In ISDS, the enforceability of mediated settlements typically relies on domestic legal processes or the Singapore Convention. The Convention may apply to settlements involving states unless a country enters a reservation excluding settlements involving the state or its agencies. $^{5}$ From the perspective of foreign investors, there is limited incentive to pursue mediation with a state that has not ratified the Singapore Convention or has adopted such reservations.

## 4. Ways to Promote Mediation in Investor-State Dispute Settlement

Despite the challenges facing mediation in ISDS, it is worthwhile to promote its use because of its merits, such as low cost, speed, tailored solutions, and the ability to maintain good relationships. The key issue, therefore, is h

[中间内容因长度限制已省略]

vention further enhances the value of international commercial mediation by strengthening the enforceability of mediated settlements. ICSID and UNCITRAL promote mediation in ISDS as part of ongoing reforms to an arbitration-oriented system.

Despite this potential, the wider use of mediation in ISDS faces challenges because of the unique characteristics of states, such as concerns about accountability, the involvement of diverse stakeholders, and the need for transparent and equitable rule-based administration, together with the limited ratification of the Singapore Convention.

Addressing accountability concerns through measures such as mandatory mediation, clear mandates, and the use of globally reputable mediation institutions like ICSID can help facilitate mediation in ISDS.

Effective coordination among line ministries within government, along with engagement of civic groups, can further enhance the credibility and acceptability of mediation outcomes.

Ratification of the Singapore Convention will also play a key role in promoting mediation in ISDS by expanding the global enforceability framework. As awareness of the Convention increases, more countries are expected to move toward ratification. It is encouraging that the Republic of Korea, Malaysia, and Bhutan are likely to ratify the Convention in 2026. $^{12}$

ADBI and ADB remain committed to tightening regional cooperation and integration by promoting ADR, including mediation in ISDS, across Asia and the Pacific in collaboration with governments, UNCITRAL, ICSID, ADR institutions, and academia (ADBI and ADB n.d.).

## References

ADBI (Asian Development Bank Institute) and ADB (Asian Development Bank). n.d. ADBI–ADB Alternative Dispute Resolution Program. https://www.adb.org/adbi/adbi-adb-alternative-dispute-resolution-program.

BIICL (British Institute of International and Comparative Law) and Allen & Overy. 2021. Empirical Study: Costs, Damages and Duration in Investor-State Arbitration.

Carter, J. 2026. Camp David Accords. Encyclopedia Britannica. 22 March. https://www.britannica.com/event/Camp-David-Accords.

Department of Foreign Affairs and Trade, Australia. 2019. Indonesia–Australia Comprehensive Economic Partnership Agreement (IA-CEPA).

Fisher, R., W. Ury, and B. Patton. 2011. Getting to Yes: Negotiating Agreement Without Giving In. 3rd ed. New York: Penguin.

Foreign Investment Ombudsman. n.d. Who We Are. https://ombudsman.kotra.or.kr/ob-en/cntnts/i-2642/web.do.

FRONTLINE. 2002. Shattered Dreams of Peace: The Road from Oslo. PBS. 27 June. https://www.pbs.org/wgbh/pages/frontline/shows/oslo/negotiations/index.html.

ICSID (International Centre for Settlement of Disputes). 2015. Suez, Sociedad General de Aguas de Barcelona S.A. and Vivendi Universal S.A. v. Argentine Republic. ICSID Case No. ARB/03/19.

———. 2021. Background Paper on Investment Mediation. Washington, DC.

——. 2022a. ICSID Mediation Rules. Washington, DC.

——. 2022b. Lone Star Funds v. Republic of Korea. ICSID Award, 30 August.
——. 2026. The ICSID Caseload – Statistics. Issue 2026-1.

Nitschke, F. 2026. Presentation by Chief Counsel of ICSID. Asian Development Bank Institute–Asian Development Bank Second Alternative Dispute Resolution Policy Dialogue. 20–22 April.

Republic of Korea. 1998. Foreign Investment Promotion Act.

——. 2017. Regulations on Ministerial Meeting on International Economic Affairs (Presidential Decree No. 28211).

Shonk, K. 2026. Types of Mediation: Choose the Type Best Suited to Your Conflict. Daily Blog, 10 March. Harvard Law School Program on Negotiation. https://www.pon.harvard.edu/daily/mediation/types-mediation-choose-type-best-suited-conflict/.

UNCITRAL (United Nations Commission on International Trade Law). 2013. Rules on Transparency in Treaty-Based Investor-State Arbitration.

———. 2018. Model Law on International Commercial Mediation and International Settlement Agreements Resulting from ediation.
———. 2021. Model Provisions on Mediation for International Investment Disputes.

——. 2023. Guidelines on Mediation for International Investment Disputes.

United Nations. 1958. Convention on the Recognition and Enforcement of Foreign Arbitral Awards (New York Convention).

———. 2019. United Nations Convention on International Settlement Agreements Resulting from Mediation (Singapore Convention on Mediation).

United Nations Commission on International Trade Law. n.d. Status: United Nations Convention on International Settlement Agreements Resulting from Mediation. United Nations. https://uncitral.un.org/en/texts/mediation/conventions/international\_settlement\_agreements/status.

## Asian Development Bank Institute

ADBI, located in Tokyo, is the think tank of the Asian Development Bank (ADB). Its mission is to identify effective development strategies and improve development management in ADB's developing member countries.

ADBI Policy Briefs are based on events organized or co-organized by ADBI. The series is designed to provide concise, nontechnical accounts of policy issues of topical interest, with a view to facilitating informed debate.

The views expressed in this publication are those of the authors and do not necessarily reflect the views and policies of ADBI, ADB, or its Board or Governors or the governments they represent.

ADBI encourages printing or copying information exclusively for personal and noncommercial use with proper acknowledgment of ADBI. Users are restricted from reselling, redistributing, or creating derivative works for commercial purposes without the express, written consent of ADBI.

Asian Development Bank Institute
Kasumigaseki Building 8F
3-2-5 Kasumigaseki, Chiyoda-ku
Tokyo 100-6008
Japan
Tel: +813 3593 5500
www.adbi.org
"""
