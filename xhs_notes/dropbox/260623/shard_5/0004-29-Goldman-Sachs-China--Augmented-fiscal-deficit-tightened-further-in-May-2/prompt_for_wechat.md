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
# China: Augmented fiscal deficit tightened further in May

## Bottom line:

Year-on-year growth in on-budget fiscal revenue remained solid in May amid continued increase in PPI inflation and still-soft activity growth, as slower tax revenue growth largely offset faster non-tax revenue growth. Year-on-year contraction in on-budget fiscal expenditure narrowed, although growth in infrastructure-related on-budget spending remained subdued. Property-related government revenue weakened further in May, due mainly to wider year-on-year contraction in off-budget land sales revenue. Combining on-budget and off-budget financing channels, our proprietary “augmented fiscal deficit” (AFD) metric tightened further in May on both a 3-month and 12-month moving average basis, suggesting fiscal policy has become less supportive of growth in Q2 vs. Q1 on the back of falling land sales revenue and shrinking policy bank support. We expect the central and local governments to step up their bond issuance and proceeds spending in coming months, and accelerate the implementation of the RMB800bn policy bank new financing tool.

Lisheng Wang  
+852-3966-4004 |  
lisheng.wang@gs.com  
GS (Asia) L.L.C.

## Key numbers:

Fiscal revenue growth: +6.6% yoy in May (-0.4% mom sa non-annualized, estimated by GS), vs. +6.7% yoy in April (+1.9% mom sa non-annualized).

Fiscal expenditure growth: -1.6% yoy in May (+0.3% mom sa non-annualized), vs. -3.2% yoy in April (-2.7% mom sa non-annualized).

Land sales revenue growth: -35.8% yoy in May (-1.2% mom sa non-annualized), vs. -34.9% yoy in April (-5.6% mom sa non-annualized).

Property-related tax revenue growth: -2.6% yoy in May, vs. -0.7% yoy in April.

Effective fiscal deficit ratio (after GS seasonal adjustment): -4.1% of GDP 3mma and -4.7% 12mma as of May, vs. -4.7% of GDP 3mma and -4.8% 12mma as of April.

Augmented fiscal deficit (AFD) ratio (after GS seasonal adjustment): -8.5% of GDP 3mma and -10.6% 12mma as of May, vs. -9.5% of GDP 3mma and -10.8% 12mma as of April. $^{1}$

## Main points:

1. On-budget fiscal revenue growth remained solid at +6.6% yoy in May (vs. +6.7% yoy in April; Exhibit 1) amid continued increase in PPI inflation and still-soft activity growth, as slower tax revenue growth (to +6.8% yoy in May from +8.2% yoy in April) largely offset faster non-tax revenue growth (to +5.6% yoy on favorable base effects from -5.3% yoy). April-to-May slowdown in year-on-year revenue growth was broad-based across major tax categories, led by individual income tax, corporate income tax and consumption tax. Year-on-year growth in stamp duty on stock trading jumped to +145.9% in May from +62.9% in April, though it only accounted for 1.2% of total tax revenue in 2025.

2. Year-on-year contraction in on-budget fiscal expenditure narrowed to -1.6% in May from -3.2% in April, as faster spending growth in science & technology, urban & rural community affairs, and energy saving & environmental protection more than offset slower spending growth in culture, tourism, sports & media. Based on our estimates, growth in infrastructure-related on-budget fiscal spending $^{2}$ remained subdued at -12.0% yoy in May despite a modest improvement from -18.6% yoy in April, which continued to weigh on infrastructure investment growth (slowing to -11.2% yoy in May from -5.6% yoy in April).

3. Property-related government revenue weakened further in May — year-on-year contraction in off-budget land sales revenue widened further to -35.8% in May from -34.9% in April, and on-budget property-related tax revenue growth slid to -2.6% yoy from -0.7% yoy (Exhibit 2). $^{3}$ Combining these two items, we estimate that government revenue directly from the property sector contracted 23.9% yoy in May (vs. -20.1% yoy in April). Despite recent green shoots in home transactions in some large cities, we expect continued decline in land sales revenue this year and beyond, given the prolonged property downturn (especially for construction activity) and still-stretched funding conditions for many developers.

4. Taking into consideration general public budget and government-managed fund budget, we estimate year-on-year growth in total government revenue rose slightly to +2.4% in May from +2.0% in April, and year-on-year contraction in total government expenditure narrowed to -3.9% from -7.3%. Further incorporating more off-budget financing channels, our proprietary “augmented fiscal deficit” (AFD) metric narrowed further in May, on both a 3-month and 12-month moving average basis (Exhibit 3). Although our proprietary measure of fiscal “spend-through” ratio (which is based on 12-month moving average) and the year-on-year change in outstanding amount of fiscal deposits pointed to slightly faster government spending of previously raised funds in May (Exhibit 4), the meaningful tightening of our AFD metric suggests fiscal policy has become less supportive of growth in Q2 vs. Q1, on the back of falling land sales revenue and shrinking policy bank support (Exhibit 5).

5. Onboarding the weaker-than-expected activity data in April-May, we recently nudged down our sequential real GDP growth forecast for Q2 to 3.5% qoq annualized (implying a 4.5% yoy growth), while raising it slightly for Q3 on our assumptions of lower oil prices, faster fiscal spending, and normalized weather conditions. The RMB7.7tn of unspent government bond quota as of end-May (out of RMB11.9tn for the full year), the

RMB800bn policy bank new financing tool available this year (up from RMB500bn last year), and the RMB536bn year-on-year increase in outstanding fiscal deposits all suggest ample funding capacity in coming quarters. We expect the central and local governments to step up their bond issuance and proceeds spending in coming months, accelerate the implementation of the policy bank new financing tool, and leave the door open for incremental easing should Q2 GDP disappoint meaningfully. However, given firmer-than-expected exports and the conservative growth target for this year (“4.5-5%”), we do not expect significant, broad-based stimulus in the near-term.

## Lisheng Wang

Exhibit 1: Fiscal revenue growth continued to outperform fiscal spending growth in May  
![](images/bd650b33cd6f54eea5138a259d4c255fe2b06ec4b543cfb1e75dbc38b49a79c1.jpg)  
Source: Wind, Data compiled by GS Global Investment Research

Exhibit 2: Property-related government revenue continued to weaken in May  
![](images/2d2485283975813f756f1b8d032d3d3ff6fc8ffe7d29abb82a269cf6511bc2f3.jpg)  
Source: Wind, Data compiled by GS Global Investment Research

Exhibit 3: Our augmented fiscal deficit (AFD) metric tightened further in May  
![](images/76e4dbb9f8eb46a939f9c9d86db682d28ca5322f3e347b38eed38e9597e64e41.jpg)  
Source: Wind, CEIC, GS Global Investment Research

Exhibit 4: China's fiscal "spend-through" ratio rose slightly in May on a 12mma basis  
![](images/e383e76ae2cd61bd7a486e851015552aa7597893893858b8d7bdff1f029908a5.jpg)  
Shaded areas refer to periods when China's year-to-date real GDP growth was equal to or below the full-year growth target. Note that the Chinese government did not set a national growth target for 2020.  
Source: MOF, Wind, CEIC, GS Global Investment Research  
Exhibit 5: Fiscal impulse has weighed on sequential growth in Q2, while we expect it to be more supportive of growth in H2

![](images/6a62a8efdcc692ba07fc8fd49255a870c03ea4f00f9eb254520d0fe520d111a2.jpg)  
Source: GS Global Investment Research

## The China Economics Team

Andrew Tilton  
+852-2978-1802  
andrew.tilton@gs.com  
GS (Asia) L.L.C.

## Xinquan Chen

+852-2978-2418
xinquan.chen@gs.com
GS (Asia) L.L.C.

Hui Shan  
+852-2978-6634  
hui.shan@gs.com  
GS (Asia) L.L.C.

Yuting Yang  
+852-2978-7283  
yuting.y.yang@gs.com  
GS (Asia) L.L.C.

Lisheng Wang +852-3966-4004 lisheng.wang@gs.com GS (Asia) L.L.C.

Chelsea Song +852-2978-0106 chelsea.song@gs.com GS (Asia) L.L.C.

## Disclosure Appendix

## Reg AC

I, Lisheng Wang, hereby certify that all of the views expressed in this report accurately reflect my personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Lisheng Wang GS (Asia) L.L.C..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; $1\%$ or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for information purposes only and is not, and under no circumstances should be construed as, an advertisement, offering or solicitation by GS & Co. LLC for purchasers of securities in Canada to trade in any Canadian security. GS & Co. LLC is not registered as a dealer in any jurisdiction in Canada under applicable Canadian securities laws and generally is not permitted to trade in Canadian securities and may be prohibited from selling certain securities and products in certain jurisdictions in Canada. If you wish to trade in any Canadian securities or other products in Canada please contact GS Canada Inc., an affiliate of The GS Group Inc., or another registered Canadian dealer. Hong Kong: Further information on the securities of covered companies referred to in this research may be obtained on request from GS (Asia) L.L.C. India: Further information on the subject company or companies referred to in this research may be obtained from GS (India) Securities Private Limited, Research Analyst – SEBI Registration Number INH000001493, 10th Floor, Ascent-Worli, Sudam Kalu Ahire Marg, Worli, Mumbai-400 025, India, Corporate Identity Number U74140MH2006FTC160634, Phone +91 22 6616 9000, Fax +91 22 6616 9001. GS may beneficially own 1% or more of the securities (as such term is defined in clause 2 (h) the Indian Securities Contracts (Regulation) Act, 1956) of the subject company or companies referred to in this research report. Investment in securities market are subject to market risks. Read all the related documents carefully before investing. Registration granted by SEBI and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. GS (India) Securities Private Limited compliance officer and investor grievance contact details can be found at: https://www.goldmansachs.com/worldwide/india/documents/Grievance-Redressal-and-Escalation-Matrix.pdf, and a copy of the annual audit compliance report can be found at this link: https://publishing.gs.com/content/site/india-annual-compliance-report.html. Japan: See below. Korea: This research, and any access to it, is intended only for “professional investors” within the meaning of the Financial Services and Capital Markets Act, unless otherwise agreed by GS. Further information on the subject company or companies referred to in this research may be obtained from GS (Asia) L.L.C., Seoul Branch. New Zealand: GS New Zealand Limited and its affiliates are neither “registered banks” nor “deposit takers” (as defined in the Reserve Bank of New Zealand Act 1989) in New Zealand. This research, and any access to it, is intended for “wholesale clients” (as defined in the Financial Advisers Act 2008) unless otherwise agreed by GS. A copy of certain GS Australia and New Zealand disclosure of interests is available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html.

Russia: Research reports distributed in the Russian Federation are not advertising as defined in the Russian legislation, but are information and analysis not having product promotion as their main purpose and do not provide appraisal within the meaning of the Russian legislation on appraisal activity. Research reports do not constitute a personalized investment recommendation as defined in Russian laws and regulations, are not addressed to a specific client, and are prepared without analyzing the financial circumstances, investment profiles or risk profiles of clients. GS assumes no responsibility for any investment decisions that may be taken by a client or any other person based on this research report. Singapore: GS (Singapore) Pte. (Company Number: 198602165W), which is regulated by the Monetary Authority of Singapore, accepts legal responsibility for this research, and should be contacted with respect to any matters arising from, or in connection with, this research. Taiwan: This material is for reference only and must not be reprinted without permission. Investors should carefully consider their own investment risk. Investment results are the responsibility of the individual investor. United Kingdom: Persons who would be categorized as retail clients in the United Kingdom, as such term is defined in the rules of the Financial Conduct Authority, should read this research in conjunction with prior GS on the covered

companies referred to herein and should refer to the risk warnings that have been sent to them by GS International. A copy of these risks warnings, and a glossary of certain financial terms used in this report, are available from GS International on request.

European Union and United Kingdom: Disclosure information in relation to Article 6 (2) of the European Commission Delegated Regulation (EU) (2016/958) supplementing Regulation (EU) No 596/2014 of the European Parliament and of the Council (including as that Delegated Regulation is implemented into United Kingdom domestic law and regulation following the United Kingdom's departure from the European Union and the European Economic Area) with regard to regulatory technical standards for the technical arrangements for objective presentation of investment recommendations or other information recommending or suggesting an investment strategy and for disclosure of particular interests or indications of conflicts of interest is available at https://www.gs.com/disclosures/europeanpolicy.html which states the European Policy for Managing Conflicts of Interest in Connection with Investment Research.

Japan: GS Japan Co., Ltd. is a Financial Instrument Dealer registered with the Kanto Financial Bureau under registration number Kinsho 69, and a member of Japan Securities Dealers Association, Financial Futures Associatio

[中间内容因长度限制已省略]

 have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g.,

marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
