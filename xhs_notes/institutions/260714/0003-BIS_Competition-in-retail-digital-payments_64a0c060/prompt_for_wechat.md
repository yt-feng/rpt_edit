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
- 已识别机构名：`国际清算银行`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份国际清算银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## BIS Bulletin

No 127

## Competition in retail digital payments

Daniele Natalizi and Vatsala Shreeti

13 July 2026

BIS Bulletins are written by staff members of the Bank for International Settlements, and from time to time by other economists, and are published by the Bank. The papers are on subjects of topical interest and are technical in character. The views expressed in this publication are those of the authors and do not necessarily reflect the views of the BIS or its member central banks. The authors are grateful to Iñaki Aldasoro, Jon Frost, Pablo Hernández de Cos, Gaston Gelos, Anneke Kosse, Thomas Lammer, Ulf Lewrick, Andrea Maechler, Benoit Mojon, Tara Rice, Tom Rosewall, Takeshi Shirakami, Peter Wierts and Leanne Zhang for comments, to Rudraksh Kansal for excellent research assistance, and to Nicola Faessler for administrative support.

The editors of the BIS Bulletin series are Gaston Gelos and Frank Smets.

This publication is available on the BIS website (www.bis.org).

# Competition in retail digital payments

## Key takeaways

\- Retail payments have digitalised rapidly in both advanced economies and emerging market and developing economies.

\- Digitalisation has altered the competitive landscape, with new entrants (eg fintechs and big techs) and new technologies, yet incumbent banks and card networks retain their dominant position in key markets.

\- In their role as operators, overseers and catalysts in payment systems, central banks support competition in diverse ways, depending on their mandates and institutional arrangements.

Digitalisation has transformed retail payments. Expanding internet and smartphone adoption, entry of new players like fintechs, big techs and other non-banks, innovations in underlying payment systems and the development of new payment technologies have changed the way households and businesses make payments. At the same time, these shifts are also altering the competitive landscape and the industrial organisation of retail digital payments.

Central banks play diverse roles in ensuring the safety and efficiency of retail payments – objectives that are influenced by the competitive landscape. This Bulletin examines recent trends in retail digital payments in advanced economies (AEs) and emerging market and developing economies (EMDEs). It highlights structural features of payment markets, the strategic behaviour of market participants and the ensuing risks of reduced competition. While mandates differ, several central banks support competition through direct interventions or close coordination with competition authorities.

## The changing landscape of retail payments

Retail digital payments are based on an architecture with three components: the user-facing front end, back-end retail payment systems and back-end wholesale settlement among payment service providers (PSPs) ((BIS (2020); OECD (2025)). This Bulletin focuses on domestic retail payments and analyses the first two components. $^{1}$

The user-facing front end refers to the interfaces, services and instruments through which end consumers, like households or businesses, initiate or accept digital payments. These can include payment cards, bank consortium apps (eg Swish in Sweden, TWINT in Switzerland), fintech payment services (eg PayPal, Revolut, PhonePe), big tech wallets (eg Apple Pay, Google Pay, Alipay, WeChat Pay) and mobile network operator-based systems (eg Airtel, M-Pesa, MTN). Some of these hold user funds in their ecosystem, while others transfer funds directly using the underlying retail payment system. These interfaces are usually compatible with various access technologies like near field communication (NFC) or quick response (QR) codes and can work remotely for e-commerce as well as at physical points of sale.

Retail payment systems refer to infrastructures and arrangements that route, authorise and clear retail transactions. These can include card networks, such as Visa, Mastercard, Cartes Bancaires, Bancomat or Rupay. They can also include account-to-account (A2A) transactions based on fast payment systems (FPS) such as Pix in Brazil, the Unified Payments Interface (UPI) in India or TARGET Instant Payment Settlement (TIPS) in Europe. Finally, they can include proprietary systems like the ones used by M-Pesa and other mobile money providers in East Africa for A2A payments.

Retail digital payments have taken off rapidly in both AEs and EMDEs, although important differences between them remain. In AEs, the increase in the volume of retail digital payments has been driven largely by card payments, while in EMDEs, A2A transactions dominate (Graph 1.A). At the same time, cash in circulation has fallen in many AEs and EMDEs, particularly those that launched an FPS (Graph 1.B).

Retail digital payments are increasingly popular in AEs and EMDEs  
![](images/8a50eaa78b1bf789e8ccfe65a00616efb02035b074b81a52106c0ba875f0e9ea.jpg)

Graph 1

![](images/c2861f83025424ac182ed403b48e63853af358582ea8011e871908da234000f4.jpg)  
- Global average, year 0 = 2015 (no FPS)  
Sources: Aksonthung et al (2026); Frost et al (2024); authors' calculations.

$^{1}$ Account-to-account (A2A) transactions include credit transfers, direct debit and e-money payments. AEs include Australia, Belgium, Canada, France, Germany, Hong Kong SAR, Italy, Japan, Korea, Netherlands, Singapore, Spain, Sweden, Switzerland, United Kingdom and United States. EMDEs include Argentina, Brazil, China, India, Indonesia, Mexico, Saudi Arabia, South Africa and Türkiye. $^{2}$ Banknotes and coins in circulation are shown as a percentage of narrow money (M1), except for KR for which currency in circulation/narrow money is shown. The dashed black line represents the average cash in circulation in jurisdictions that do not have a fast payment system (FPS).

Broader market changes have been important catalysts for rapid digitalisation of retail payments. These include rising smartphone penetration and mobile internet access, particularly in EMDEs. Mobile devices can also allow unbanked households and businesses to access digital payments (OECD (2025)). Moreover, the Covid-19 pandemic sharply accelerated digitalisation in several jurisdictions, as many individuals made their first retail digital payment during the pandemic (Demirgüç-Kunt et al (2022)).

Beyond these changes, the entry of new players in the payments market and the development of new technologies have also propelled retail digital payments. Mobile applications and wallet-based payment services provided by non-banks – including fintechs and big techs – have become popular. These are particularly prominent in economies with low penetration of alternative digital payment methods like cards (eg Alipay and WeChat Pay in China).

At the same time, new technologies like NFC and QR codes for contactless payments have made digital payments easier to make, increasing their popularity. Recent innovations in building alternative

Graph 2

retail-level payment systems, like the launch of FPS, have also led to greater uptake of retail digital payments. $^{2}$ Together, these forces have shifted the competitive landscape in retail payments and expanded the choices for households and businesses.

## Market structure and competition considerations

Markets for retail digital payments have become more contestable in many economies in the past decade. This has paved the way for new entrants. In the user-facing front end, mobile payment apps for both person-to-person (P2P) payments and person-to-merchant (P2M) payments (often provided by non-bank PSPs) have become popular in AEs and EMDEs alike, enabling greater choice for consumers (Graph 2.A). Contestability has also increased for back-end retail payment systems, supported by FPS that can provide alternatives to card networks. Yet the entry of new players does not guarantee effective competition by itself. In some cases, eg for card payments, incumbents continue to dominate retail digital payments. In the past decade, major global card networks have seen rising revenue and high margins (Graph 2.B). $^{3}$

Ensuring competition in payments markets can be inherently challenging. Many markets for front-end payment services, such as P2M payments, are two-sided (Rochet and Tirole (2003)). A wallet, app or card is valuable to consumers only if many merchants accept it and it is valuable to merchants only if

## The competitive landscape in retail digital payments

![](images/a0a9e157f5902b0ca246d7d0ab7c77ce410dc52621f27fcd243f71df3939a4c5.jpg)

![](images/17e0caaf40ff3c2ad196b6ec441f7a01d6a4c1480665faec8ee7e5ce74cc9dbd.jpg)  
$^{1}$ Based on the top 100 person-to-person (P2P) and top 100 person-to-merchant (P2M) apps as classified by Sensor Tower for each AE and EMDE category. $^{2}$ The profit margins are expressed as a percentage, calculated as the ratio of net income to net revenue. AEs include Australia, Canada, Czechia, Denmark, euro area, Hong Kong SAR, Israel, Japan, Korea, New Zealand, Norway, Singapore, Sweden, Switzerland, United Kingdom and United States. EMDEs include Algeria, Argentina, Brazil, Chile, China, Colombia, Hungary, India, Indonesia, Kuwait, Malaysia, Mexico, Morocco, Peru, Philippines, Poland, Romania, Russia, Saudi Arabia, South Africa, Thailand, Türkiye, United Arab Emirates and Vietnam.  
Sources: Lubbersen (2026); Sensor Tower; authors' elaboration based on the annual reports of Visa and Mastercard (accessed online on 13 April 2026).

2 Other recent innovations include cryptoassets, stablecoins and retail central bank digital currencies, but their use in retail payments is currently limited (Hernández de Cos (2026)). Since the focus of this Bulletin is on gauging the current competitive landscape in retail digital payments, we do not focus on innovations that have not yet achieved scale.

3 The combined global market share of Mastercard and Visa, as measured by the annual number of card transactions in major jurisdictions (excluding China), has been stable at around 95% of all card transactions in the last decade. See Statista (2025), accessed on 25 April 2026.

consumers use it. This can give rise to significant direct and indirect network effects, organically creating barriers for new entrants and coordination failures, reinforcing the market power of incumbents. $^{4}$

At the same time, strategic behaviour by market participants in the front end can also stifle competition. Where digital payments rely on third-party providers, as with NFC technology for in-store payments, front-end competition can be constrained by gatekeepers that provide hardware. An example is Apple restricting third-party payment apps from accessing the NFC functionality on iPhones. $^{5}$

Fragmentation and lack of interoperability add to these challenges. If not addressed adequately, competing private payment interfaces may choose to keep their systems siloed, increasing costs for merchants and locking in consumers, ie reducing contestability. For example, prior to regulatory interventions in China and Peru, the biggest payment apps (eg WeChat Pay and Alipay in China and Yape and Plin in Peru) were incompatible with each other and with other payment apps.

Differences among PSPs in data access and usage capabilities, advantages from adjacent markets and strategic partnerships can be additional threats to competition in front-end payment markets. Banks hold detailed financial data. Fintechs may have superior data analytics tools but can lack the scale of banks. Big techs, when they provide payments, can combine transaction data with other data from their wider ecosystems (eg social media, search history). These differences in the scope and use of data can translate into competitive advantages, particularly when data-sharing obligations across market participants are also asymmetric. Participants can also leverage market power in adjacent markets to distort competition in payments by bundling, cross-selling or subsidising products and services. For example, Safaricom's market dominance in the Kenyan mobile money market has been sustained in part due to its control of the underlying telecom infrastructure (CAK (2016)). Traditional players like banks may also enter partnerships with their competitors like fintechs. In some cases, such partnerships can weaken competition (Puri et al (2024)).

The competitive forces shaping the market for underlying retail-level payment systems differ from front-end markets. Retail-level payment systems involve high fixed costs to build and maintain, and they exhibit strong network effects since a payment system's value for a participant depends on wide participation by other banks, non-banks, consumers and merchants. Payment systems also exhibit economies of scale in transaction processing (Bolt and Humphrey (2007)). These characteristics mean that the market structure can often tend towards a natural monopoly. As such, in many jurisdictions, particularly in AEs, incumbent card networks have retained their dominant positions, contestability is limited, and fees are high. More recently, FPS have increased contestability by providing alternative payment systems (especially in EMDEs), but competition challenges can re-emerge in the front end. $^{6}$

## The role of central banks in supporting competition

Central banks' engagement with retail digital payments varies significantly across jurisdictions. This reflects differences in mandates, institutional arrangements and market structures. Only a few central banks have explicit mandates to promote competition in retail payments (eg Reserve Bank of Australia). But many are responsible for the efficiency of payment systems, ultimately supporting competition.

Generally, central bank roles in payments fall into three broad categories: operator, overseer and catalyst (CPSS (2003); BIS (2020)). As operators, central banks build and run payment systems directly. As overseers (and regulators), they set requirements regarding access, risk management, governance, transparency and compliance in payment systems. As catalysts, they convene stakeholders, promote standards (eg ISO 20022) and encourage innovation without directly mandating outcomes. Despite these differences in roles, central banks are increasingly attentive to issues surrounding retail digital payments, particularly in EMDEs, as reflected in speeches on these issues (Graphs A.1.A and A.1.B in the online annex).

As operators, some central banks have built public payment systems that can directly reshape competitive dynamics at the retail level. For example, the Central Bank of Brazil (BCB) developed and operates Pix, an FPS that created a credible alternative to card networks. Pix enabled competitive entry by fintech companies and smaller banks (Duarte et al (2022)). Other examples include FedNow in the United States, SINPE Móvil in Costa Rica and TIPS in Europe. In these cases, central banks' direct operation of a retail payment system can enhance contestability. Some central banks have also introduced retail digital currencies, and others are actively experimenting with them. Their overall impact on the evolution of competition remains to be seen.

As regulators and overseers, central banks collaborate with the legislative bodies and can stimulate competition by fostering interoperability and non-discriminatory market access and regulating fees. For example, central banks in China, India and Peru mandated the interoperability of competing mobile wallets, which were previously closed-loop and incompatible with each other. In terms of market access, some central banks have issued explicit regulation to allow non-banks to participate in the payment system (eg BCB in 2013, Bank of England in 2017, ECB in 2025). $^{7}$ Several central banks also regulate prices of retail digital payments, particularly interchange fees and more unusually merchant fees. The overall effect of such regulation on competition is mixed (Mukharlyamov and Sarin (2025); Wang (2025)).

As catalysts, central banks have facilitated the development of standards and promoted coordination with the industry and other public authorities. In this role, many central banks sponsor national forums where stakeholders can convene to discuss issues related to coordination failures, a key risk arising in two-sided retail payment markets (for example, European Central Bank's Euro Retail Payments Board or the National Payments Council of India, a not-for-profit consortium of private and public banks supported by the Reserve Bank of India).

Central bank approaches to competition in retail digital payments reflect complex policy trade-offs. First is the trade-off between competition and fragmentation. Intense competition at the front end without interoperability can lead to fragmentation, limiting the benefits of economies of scale, reducing payment speed and fragmenting liquidity. Promoting and mandating interoperability can reduce consumer lock-in and switching costs but may not be effective if the market has already tipped towards the dominant participants. Second, central banks may also face stability and security concerns when expanding market access to non-banks. Opening payment systems to non-bank participants can spur innovation and improve efficiency but requires robust prudential and operational frameworks to manage the risks of operational outages, fraud, cyber attacks, money laundering or PSP default. Third, promoting competition at the retail payment system level, eg by launching an FPS with zero user fees and mandatory PSP participation, can accelerate adoption but may constrain the profitability of private sector participants.

Navigating these trade-offs can be challenging. Data on pricing schemes and the costs of different payment instruments remain scant. For central banks and other regulators, enhancing data collection and sharing efforts can address blind spots in decision-making. Another challenge concerns potential overlaps in the regulatory perimeter with competition authorities and other regulators. This makes close coordination between different regulatory authorities essential.

Aksonthung, C, A Kosse and I Mustafi (2026): "Tap a card, pay by phone, but cash still holds its own", CPMI Briefs, no 12.

Bank for International Settlements (BIS) (2020): "Central banks and payments in the digital era", Annual Economic Report 2020, Chapter III.

Bolt, W and D Humphrey (2007): "Payment network scale economies, SEPA, and cash replacement", Review of Network Economics, vol 6, no 4.

Claessens, S and T Rice (2026): "Cross-border payment technologies: innovations and challenges", BIS Papers, no 167.

Committee on Payment and Settlement Systems (CPSS) (2003): Policy issues for central banks in retail payments.

Competition Authority of Kenya (CAK) (2016): Competition inquiry into USSD service provision in Kenya.

Cornelli, G, J Frost, L Gambacorta, S Sinha and R Townsend (2024): "The organisation of digital payments in India – lessons from the Unified Payments Interface (UPI)", SUERF Policy Note, no 355.

Demirgüç-Kunt, A, L Klapper, D Singer and S Ansar (2022): The global 2021 findex database; financial inclusion, digital payments and resilience in the age of Covid-19, World Bank Group.

Duarte, A, J Frost, L Gambacorta, P K Wilkens and H S Shin (2022): "Central banks, the monetary system and public payment infrastructures: lessons from Brazil's Pix", BIS Bulletin, no 52, March.

Eroglu, H, G Cornelli, J Frost, F Rühmann and V Shreeti (2026): “Opening doors to open finance: evidence from the international experience”, BIS Papers, no 168.

Frost, J, P K Wilkens, A Kosse, V Shreeti and C Velásquez (2024): "Fast payments: design and adoption", BIS Quarterly Review, March.

Hernández de Cos, P (2026): "Stablecoins: framing the debate", speech at a Bank of Japan seminar, Tokyo, 20 April.

Lubbersen, V (2026): "Locked out by loyalty: entry deterrence through rebates in payment card markets", De Nederlandsche Bank Working Papers, no 856.

Mukharlyamov, V and N Sarin (2025): "Price regulation in two-sided markets: empirical evidence from debit cards", Journal of Financial Economics, vol 172, 104094.

Organisation for Economic Co-operation and Development (OECD) (2025): "Competition in mobile payment services", OECD Roundtables on Competition Policy Papers, no 324.

Puri, M, Y Qian and X Zheng (2024): "From competitors to partners: banks' venture investments in fintechs", NBER Working Papers, no 33297.

Rochet, J-C and J Tirole (2003): "Platform competition in two-sided markets", Journal of the European Economic Association, vol 1, no 4.

Statista (2025): "Number of purchase transactions on global general purpose card brands American Express, Diners/Discover, JCB, Mastercard, UnionPay and Visa from 2014 to 2024 (in billions)".

Vipps MobilePay (2026): "Vipps MobilePay close to profitability after strong turnaround", press release, 12 May.

Wang, L (2025): "Regulating competing payment networks", Kilts Center at Chicago Booth Marketing Data Center Paper.
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
9. 输出前自行核对：标题与导语不重复；每个小标题都是完整判断；没有元话语、推广语和未解问题栏目。只输出最终 Markdown，不输出核对过程。
