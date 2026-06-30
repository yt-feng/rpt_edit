你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`GS`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
Asia Views: Oil relief, dollar pressure, tech boom

1. The past few weeks have brought welcome relief for the world's biggest oil-importing region. Intensive negotiations between the US and Iran have increased market hopes that the Strait of Hormuz will reopen, and brought down oil prices significantly (notwithstanding another round of tit-for-tat strikes). From a late April peak of near \$120/bbl, Brent crude has fallen to \$72/bbl as of this writing (Exhibit 1). Our commodities team forecasts \$80/bbl in Q4. While the plunge has been dramatic, oil prices remain slightly above levels prior to the war, more so for refined products where margins are likely to remain wide due to damage to facilities both in the Gulf and in Russia. Furthermore, a hawkish shift at the Fed – both in terms of new Chairman Warsh's commentary and in terms of FOMC participants' expectations for the funds rate – has supported the USD, which has moved back towards its March highs (Exhibit 2).

Exhibit 1: Oil prices have nearly round-tripped to pre-war levels, but refined product prices remain elevated  
![](images/380e404ac5c938e46e561ac4db8385e48ca64e4bf304bd1911793c7874a2af1b.jpg)  
Source: Bloomberg, GS Global Investment Research

Exhibit 2: Dollar strengthened to near 2026 highs  
![](images/924cddf7221e57b7ce9fdcda80c2ca094415d3f94517fd4769b1813dbbee22af.jpg)  
Source: Haver Analytics, GS Global Investment Research

2. The energy-driven pickup in inflation has remained manageable in most of Asia – given a more narrowly-based and (as of now) briefer shock than in 2021-22, and the liberal use of inventories and fiscal policy to cushion the impact. The worst inflation outcomes have been in economies with limited energy subsidies, especially the Philippines (where CPI inflation reached 7.2% yoy) and several frontier economies. Elsewhere, though, inflation is generally still within, or near, target bands (Exhibit 4). We still expect core inflation to move higher in coming months as pass-through from higher energy costs (e.g. to chemicals prices) and weaker currencies plays its part. Food inflation is also likely to rise later this year and in early 2027 given the aftereffects of the shock and the potential for a strong El Niño event. In light of the plunge in oil prices, these factors suggest a slower normalization of inflation rather than a renewed sharp rise from here.

Exhibit 3: Asia CPI inflation has moved up, but less dramatically than in 2021-22  
![](images/a73ba1f67a3f4044cb4f9155e5359607f260fae7b8ed22d7929b1a9492ba9f71.jpg)  
Source: Haver Analytics, GS Global Investment Research

Exhibit 4: Inflation is in line with or modestly above targets in most of the region  
![](images/29066d5ff1cfff986b6051ffaebcf6d6bc171cbbdea37b9d28307e676e9b27f7.jpg)  
\* For Hong Kong and Malaysia, we use avg. annualized CPI in 5 years prior to the pandemic; for Singapore $1\% -2\%$ (all light shading). For point targets, a $+0.5 / - 0.5$ range is displayed for clarity. We treat China's target as a ceiling.  
Source: Haver Analytics, GS Global Investment Research

## 3. Tech spending remains a dominant influence on several Asian economies and

markets. Estimates for AI-related capex spending continue to march higher—consensus forecasts now estimate nearly \$1tn for the five large US hyperscalers alone in 2027—and exports from Asian participants in the AI equipment supply chain are surging (Exhibit 5). Korea, Taiwan, Malaysia, and Singapore have each run goods trade surpluses well in excess of 10% of GDP over the past three months. Booming equity markets have eased financial conditions significantly, though volatility has increased recently. A key

question for the second half is the degree to which buoyant exports and equities will spill over into stronger domestic activity. We expect Korea's private consumption growth to recover somewhat on wealth effects, while Taiwan's economy will likely continue to grow at around $10\%$ —the strongest pace in the last four decades—supported by extraordinary strength in tech production.

4. Growth prospects are brightening again. With energy prices much lower, policy pressures easing somewhat, and the tech boom ongoing, we have begun to nudge a few growth forecasts higher. In India, momentum has been better than expected and retail fuel prices will not need to rise as high as we had assumed, so we recently upgraded our full-year GDP growth forecast 30bp to $6.8\%$ . We also took our Korea growth forecasts up slightly, mostly for 2027. Still, in ASEAN economies that have been particularly challenged by high oil prices, e.g. Indonesia, Philippines, Thailand, and Vietnam, we have yet to make changes—the first two of these still face a hangover from significant monetary tightening since the Iran war began.

Exhibit 5: Surging tech exports from key Asian suppliers  
![](images/3ee74563e6e04b3c5818f24cd4d49277fa21ff47a2fe448fca5c5040ae53311c.jpg)  
Source: GS Global Investment Research

Exhibit 6: Exports by far the largest driver of China's recent growth  
![](images/5d4d98ea8f90714a2e66235ea760315038c8b61aea8ca46f9f3e306622b0174d.jpg)  
Source: GS Global Investment Research

5. China's exports power on amid weak domestic activity. In May, both retail sales (-0.6% yoy) and fixed asset investment (-4.1% yoy) contracted, for only the second time on record—the first was in 2020 during Covid lockdowns. Weak retail sales reflect the fade-out of the trade-in program as well as pressure from higher oil prices, while investment is still being suppressed by the property downturn and tight local government finances. Overall, domestic demand looks to be growing at only a 1-2% annual rate (Exhibit 6). By contrast, exports were up over 19% yoy in May, fueling industrial production growth of 4.5% yoy and a monthly trade surplus of over \$100bn. Policymakers seem willing to be fairly patient, with only limited evidence thus far of a pickup in spending. Recent policy communications emphasized a more price-based monetary policy framework, reduced emphasis on aggregate credit extension, and rules-based capital account opening. We detect a clear pickup in efforts to accelerate RMB internationalization, by building out the “financial plumbing” to facilitate holdings by foreign central banks and institutional investors, alongside an ongoing grind stronger in the currency against both the USD and regional trade partners (Exhibit 7).

Exhibit 7: CNY stands out among Asian FX in 2026  
![](images/2ed6c887a7138503c424869300636dbda38a0c24b9d3bece851db0f44a4d4513.jpg)  
Source: Bloomberg, GS Global Investment Research

6. Asian central bankers retain a conservative bias. The Bank of Japan hiked as planned and two monetary board members advocated an accelerated pace of hikes going forward. Elsewhere in DM Asia, the RBA paused but retains a hawkish bias, while the RBNZ has teed up a likely hike for its next meeting. Central banks in the Philippines and Indonesia hiked again (Indonesia after an inter-meeting move the week prior). Rhetoric from the Bank of Korea has been clearly hawkish, and we now forecast three hikes, the first in July. Among the regional high-yielders, India is an outlier, pushing back against market expectations of rate hikes (we still expect two late in the year) while taking measures to incentivize capital inflows to support the currency. Among the low-yielders, the Bank of Thailand held at $1\%$ as expected last week, and we expect Malaysia (and now Taiwan, which also pushed back against hike expectations) to remain on hold.

Exhibit 8: We still expect tightening by several Asian central banks in coming months

<table><tr><td colspan="9">Policy rates - actual and forecast</td></tr><tr><td rowspan="2"></td><td colspan="4">2025</td><td colspan="4">2026</td></tr><tr><td>Q1</td><td>Q2</td><td>Q3</td><td>Q4</td><td>Q1</td><td>Q2</td><td>Q3F</td><td>Q4F</td></tr><tr><td>US</td><td></td><td></td><td>-25bp</td><td>-50bp</td><td></td><td></td><td></td><td></td></tr><tr><td>Euro area</td><td>-50bp</td><td>-50bp</td><td></td><td></td><td></td><td>+25bp</td><td>+25bp</td><td></td></tr><tr><td>Japan</td><td>+25bp</td><td></td><td></td><td>+25bp</td><td></td><td>+25bp</td><td></td><td></td></tr><tr><td>China</td><td></td><td>-10bp</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>India</td><td>-25bp</td><td>-75bp</td><td></td><td>-25bp</td><td></td><td></td><td></td><td>+50bp</td></tr><tr><td>Indonesia</td><td>-25bp</td><td>-25bp</td><td>-75bp</td><td></td><td></td><td>+100bp</td><td></td><td></td></tr><tr><td>Malaysia</td><td></td><td></td><td>-25bp</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Philippines</td><td></td><td>-50bp</td><td>-25bp</td><td>-50bp</td><td>-25bp</td><td>+50bp</td><td>+25bp</td><td>+50bp</td></tr><tr><td>Korea</td><td>-25bp</td><td>-25bp</td><td></td><td></td><td></td><td></td><td>+25bp</td><td>+25bp</td></tr><tr><td>Singapore*</td><td>-50bp</td><td>-50bp</td><td></td><td></td><td></td><td>+50bp</td><td></td><td></td></tr><tr><td>Taiwan</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Thailand</td><td>-25bp</td><td>-25bp</td><td>-25bp</td><td>-25bp</td><td>-25bp</td><td></td><td></td><td></td></tr><tr><td>Australia</td><td>-25bp</td><td>-25bp</td><td>-25bp</td><td></td><td>+50bp</td><td>+25bp</td><td>+25bp</td><td></td></tr><tr><td>New Zealand</td><td>-50bp</td><td>-50bp</td><td>-25bp</td><td>-75bp</td><td></td><td></td><td>+50bp</td><td></td></tr></table>

\*Estimated adjustment of SGD NEER slope  
Source: Haver Analytics, Wind, GS Global Investment Research

7. Fiscal policy adjustments are coming in the second half, however. With oil prices plunging, large-scale fiscal subsidies can be dialed back. Price caps/subsidy mechanisms in Japan and China will no longer be binding, while the cost of maintaining fixed retail prices will decline substantially in Indonesia and Malaysia. There could be new discretionary fiscal easing in Japan (where the Takaichi administration plans a tax cut on food as well as an increase in defense spending), Korea (an extension of fuel tax cuts, and new price subsidies for agricultural good prices—presumably funded by windfall tax revenues), and China (an acceleration in local govt special bond issuance and possibly spend-through). It’s a relatively quiet period for regional elections, but upcoming state-level contests in Malaysia could have broader implications (which have weighed on the MYR recently). Unless a snap general election is called, we think the MYR will rebound as the underlying macro fundamentals remain positive, and therefore hold onto our short SGD/MYR recommendation.

8. Similar equity market themes, new rate FX/dynamics. Our equity strategists prefer to “stick with the winners”, remaining overweight Japan/Korea/Taiwan/China A shares, and underweight several Southeast Asian markets. In fixed income, the easing in price pressures has made us slightly more constructive; we think 30y India government bonds look attractive on the improving macro backdrop, recent RBI FX measures, and potential index inclusion. We also favor short THB/INR, again reflecting the RBI measures, current account dynamics, relatively better INR valuation vs other high-carry EM currencies, and what we believe are different policymaker preferences in the two economies with respect to exchange rates. We expect broader global developments—particularly Fed policy, the AI investment theme, and progress on reopening the Strait of Hormuz—to

remain principal drivers of regional markets in coming months.

## Disclosure Appendix

## Reg AC

I, Andrew Tilton, hereby certify that all of the views expressed in this report accurately reflect my personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Andrew Tilton GS (Asia) L.L.C..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for information purposes only and is not, and under no circumstances should be construed as, an advertisement, offering or solicitation by GS & Co. LLC for purchasers of securities in Canada to trade in any Canadian security. GS & Co. LLC is not registered as a dealer in any jurisdiction in Canada under applicable Canadian securities laws and generally is not permitted to trade in Canadian securities and may be prohibited from selling certain securities and products in certain jurisdictions in Canada. If you wish to trade in any Canadian securities or other products in Canada please contact GS Canada Inc., an affiliate of The GS Group Inc., or another registered Canadian dealer. Hong Kong: Further information on the securities of covered companies referred to in this research may be obtained on request from GS (Asia) L.L.C. India: Further information on the subject company or companies referred to in this research may be obtained from GS (India) Securities Private Limited, Research Analyst - SEBI Registration Number INH000001493, 10th Floor, Ascent-Worli, Sudam Kalu Ahire Marg, Worli, Mumbai-400 025, India, Corporate Identity Number U74140MH2006FTC160634, Phone +91 22 6616 9000, Fax +91 22 6616 9001. GS may beneficially own 1% or more of the securities (as such term is defined in clause 2 (h) the Indian Securities Contracts (Regulation) Act, 1956) of the subject company or companies referred to in this research report. Registration granted by SEBI and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. GS (India) Securities Private Limited compliance officer and investor grievance contact details, a copy of the annual compliance audit report and other relevant information and disclosures can be found at this link:

https://www.goldmansachs.com/worldwide/india/research-analyst. Japan: See below. Korea: This research, and any access to it, is intended only for “professional investors” within the meaning of the Financial Services and Capital Markets Act, unless otherwise agreed by GS. Further information on the subject company or companies referred to in this research may be obtained from GS (Asia) L.L.C., Seoul Branch. New Zea

[中间内容因长度限制已省略]

 have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints.

As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
