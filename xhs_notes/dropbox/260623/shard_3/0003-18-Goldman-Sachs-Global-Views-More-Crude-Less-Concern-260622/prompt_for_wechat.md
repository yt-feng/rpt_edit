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
## Global Views: More Crude, Less Concern

1. The agreement between the US and Iran has reduced the downside risks to our economic outlook. Our commodities strategists now see Brent crude at \$80 per barrel by the end of 2026, with two-sided risks. On the upside, Iran's announcement on Saturday that the Strait was closed again served as a reminder that oil flows might only recover slowly. On the downside, a near-term glut could develop as oil is released quickly into a market that was already oversupplied before the war. The agreement has led us to cut our 12-month US recession risk estimate further from 25% to the long-term norm of 15%. (This is below our 20% estimate on the eve of the war because the labor market improvement since then indicates greater underlying resilience.)

Jan Hatzius  
+1(212)902-0394 | jan.hatzius@gs.com  
GS & Co. LLC

Exhibit 1: US Recession Risk Back to the Long-Term Norm of $15\%$  
![](images/520645d2364eb4d3083df5484a9736df533cbbcc9c20d935e8b1df8258f43b56.jpg)  
Source: Bloomberg, GS Global Investment Research

2. Alongside the cut to our recession risk estimate, we have nudged up our sequential H2 GDP growth forecast to 2%. The slightly stronger path reflects a positive sequential impulse to real income from lower gas prices, at a time when the economy continues to benefit from the AI boom via higher equity wealth as well as strong capex. But we still expect growth to remain moderate. First, AI capex largely consists of goods that are imported from Asia and, in the case of semiconductors, don't even show up in GDP. Second, even with the drop in gas prices, real income defined on a cash flow basis is likely to slow in H2 as the impact of higher tax refunds and lower final tax payments in Q2 peters out. This is likely to keep real consumer spending growth at just 1½%.

Exhibit 2: AI Investment Surge Adds Little to US GDP and the US Consumer Remains Under Pressure  
![](images/e73ec51c3beba44b987387a65d11a1a5f735739c4f765cfe6dae84feb73ec661.jpg)  
Source: Bureau of Economic Analysis, Haver Analytics, GS Global Investment Research

3. With GDP still growing modestly below potential, we expect a slowdown in payroll gains from the outsized 188k rate over the past three months to just below our 60k breakeven estimate. Beyond the growth forecast, we would note the failure of other labor market indicators to confirm a sharp recent improvement. Household employment has grown much more slowly than payrolls, the employment/population ratio has trended sideways to lower, and our updated slack tracker—which summarizes ten key indicators of labor market utilization—has recently resumed its gradual loosening of the prior three years. Consistent with this, we expect wage and unit labor cost growth to remain muted despite the earlier increase in headline inflation.

Exhibit 3: The Payroll Surge Is an Outlier Relative to Other Labor Market Indicators  
![](images/52724b937666fbac0dc7ce44349d27c1938b6fde4945a1144e07c6cfae5a961b.jpg)  
Source: US Bureau of Labor Statistics, Haver Analytics, GS Global Investment Research

4. The plunge in gasoline prices so far in June should result in an outright decline in seasonally adjusted consumer prices. We also expect core CPI inflation to average just 0.17% in the next three months as airfares decline on the back of lower jet fuel prices, hotel rates—which are measured at the time of booking—drop from their World Cup highs, and rent inflation reverses what looks like a high-side outlier in the Northeast in May. Core PCE inflation is likely to remain more stubborn, in part because of ongoing upward pressure on imputed financial services prices from the equity market rally and price increases in software/accessories whose weight in core PCE is 30 times larger than in core CPI. More statistically based measures such as trimmed-mean PCE should continue to look more benign, however.

Exhibit 4: Trimmed-Mean PCE Still Looks More Benign Than Core PCE

![](images/1945696f5a8d54a00051f66d793b73fd6b92ed4a3dd8c9669e3166efd47a013e.jpg)  
Source: Haver Analytics, GS Global Investment Research

5. The first FOMC meeting under Chairman Warsh was more hawkish than expected. Half of the 18 participants that submitted interest rate projections penciled in one or more rate hikes in the remainder of 2026, and the median projection for core PCE inflation in 2027Q4 rose to $2.5\%$ . While this has increased the upside risks, our baseline forecast remains for no hikes. First, we suspect that about half of the 2026 hikers are nonvoting Federal Reserve Bank presidents, which would leave a majority of voters projecting unchanged or lower rates under appropriate policy. Second, the projections might be stale given the rapid improvement in the news from the Middle East and the plunge in energy prices over the past week. If inflation comes down in coming months—rapidly for headline and gradually for core—and growth remains muted, we expect most voters to continue supporting unchanged rates.

Exhibit 5: While Hikes Have Become More Likely, We Think They Are Less Likely Than Markets Are Pricing  
![](images/c668829a41a7d0a90c9267c7344c1cbdf17cf5ff4004ea55906ec75a254af71e.jpg)  
Source: Bloomberg, GS Global Investment Research

6. We had expected Warsh's refusal to provide either a "dot" or verbal guidance about upcoming rate decisions but his broader comments on Fed communications with financial markets went further:

"So I think financial markets perform best when they react to incoming data. I think the financial markets work less efficiently when they ask [the] question 'how will the Federal Reserve react to that incoming information?' The more that markets are paying attention to what's happening in the real economy, deciding what's good data and what's less good data, the more financial markets can price what they believe is the most likely and what are the tail risks."

Since the Fed essentially controls short-term interest rates and the interest rate path matters for asset pricing, it is inevitable that markets ask how the Fed will react to incoming information. Admittedly, this can turn into an unproductive obsession with computing the Fed's reaction function, which is often harder to summarize and subject to greater change than many market participants think. Still, a significant reduction in Fed transparency could make financial conditions—and thus economic outcomes—more volatile as market assumptions about the Fed's thinking become subject to fewer reality checks.

Exhibit 6: FOMC Meeting Illustrates the Importance of Fed Communications for Financial Conditions  
![](images/dd8406d8d8689b141c711cd66d9e686a0d8c693ba96a24969d71e5c340a0362e.jpg)  
Source: Bloomberg, GS Global Investment Research

7. The ECB hike to $2.25\%$ was widely expected, but the drop in energy prices has shifted the balance of risks around our forecast of one more 25bp move in September to the downside. Either way, we continue to expect a return to a $2\%$ deposit rate in 2027 and thus remain dovish relative to market pricing. In the UK, Sir Keir Starmer has stepped down as prime minister in favor of Andy Burnham, who inherits an economy with more potential than widely appreciated. On monetary policy, the improvement in wage and price inflation even prior to the recent oil price drop has strengthened our view that the MPC won't hike in coming months and will ultimately cut Bank Rate to $3\%$ in 2027, well below market pricing.

Exhibit 7: Our ECB and BoE Rate Views Remain Below Market Pricing  
![](images/b17014904835a70824819c31eca34eb3cb2fc9b1c88fbaf81f3b81accb48d1c8.jpg)  
Source: Bloomberg, GS Global Investment Research

8. The Bank of Japan hiked by 25bp to $1\%$ , the highest level in 30 years. We expect two more 25bp hikes every six months or so until the policy rate hits $1 \frac{1}{2}\%$ next summer. The BoJ can take its time because inflation—using its estimate of CPI excluding all food and energy as well as institutional factors such as changes in school tuition rates—is running at only about 1½% year-on-year and GDP is likely to grow just 0.5% in 2026. The biggest challenge for the Japanese economy remains fiscal sustainability, as the decline in the debt/GDP ratio over the past decade could reverse if Prime Minister Takaichi implements her expansionary plans and long-term interest rates climb further toward the levels seen in other G10 economies.

Exhibit 8: Underlying Inflation in Japan Remains Benign  
![](images/439f66878a07615402eeac96f915060f667fe07bc7a9e481c155055f44c80dca.jpg)  
Source: BoJ, Haver Analytics, GS Global Investment Research

9. We attribute most of the downside growth surprises in China in April and May to a combination of the oil shock, payback for the consumer goods trade-in program, and the government's decision to slow fiscal spending after the strong Q1 GDP print. June is likely to remain sluggish because of heavy rainfall, but we expect a rebound in Q3 as the temporary drags abate, the oil shock reverses, and policymakers respond to the recent weakness with more fiscal spending. Underneath the short-term ups and downs, the gap between domestic demand and exports continues to grow, which drives up the current account surplus with negative effects on many of China's trading partners.

Exhibit 9: China's Domestic Demand Is Growing Far More Slowly Than Its Exports  
![](images/8888b2bffc19e07e3905f26d652bc5092decc5badbc406b33cd785ba01b40543.jpg)  
Source: Haver Analytics, GS Global Investment Research

10. US financial markets have digested the hawkish FOMC shock well, with declines in breakeven inflation and 30-year Treasury yields alongside a rebound in broad equity indices. If the near-term economic outlook settles into calmer waters, the focus on the sustainability of the AI trade is likely to grow even further. The work of our equity and cross-asset strategists suggests that ongoing upside surprises in AI capex, strength in S&P earnings, and the relative absence of private sector financial imbalances should all help equity markets make further headway in coming months. However, valuations of AI-related stocks are now high even relative to our optimistic views regarding the economic value that is likely to be created by AI over the next decade, so it is getting harder to justify further large gains.

## Jan Hatzius

## Disclosure Appendix

## Reg AC

I, Jan Hatzius, hereby certify that all of the views expressed in this report accurately reflect my personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Jan Hatzius GS & Co. LLC.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; $1\%$ or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for information purposes only and is not, and under no circumstances should be construed as, an advertisement, offering or solicitation by GS & Co. LLC for purchasers of securities in Canada to trade in any Canadian security. GS & Co. LLC is not registered as a dealer in any jurisdiction in Canada under applicable Canadian securities laws and generally is not permitted to trade in Canadian securities and may be prohibited from selling certain securities and products in certain jurisdictions in Canada. If you wish to trade in any Canadian securities or other products in Canada please contact GS Canada Inc., an affiliate of The GS Group Inc., or another registered Canadian dealer. Hong Kong: Further information on the securities of covered companies referred to in this research may be obtained on request from GS (Asia) L.L.C. India: Further information on the subject company or companies referred to in this research may be obtained from GS (India) Securities Private Limited, Research Analyst – SEBI Registration Number INH000001493, 10th Floor, Ascent-Worli, Sudam Kalu Ahire Marg, Worli, Mumbai-400 025, India, Corporate Identity Number U74140MH2006FTC160634, Phone +91 22 6616 9000, Fax +91 22 6616 9001. GS may beneficially own 1% or more of the securities (as such term is defined in clause 2 (h) the Indian Securities Contracts (Regulation) Act, 1956) of the subject company or companies referred to in this research report. Investment in securities market are subject to market risks. Read all the related documents carefully before investing. Registration granted by SEBI and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. GS (India) Securities Private Limited compliance officer and investor grievance contact details can be found at: https://www.goldmansachs.com/worldwide/india/documents/Grievance-Redressal-and-Escalation-Matrix.pdf, and a copy of the annual audit compliance report can be found at this link: https://publishing.gs.com/content/site/india-annual-compliance-report.html. Japan: See below. Korea: This research, and any access to it, is intended only for “professional investors” within the meaning of the Financial Services and Capital Markets Act, unless otherwise agreed by GS. Further information on the subject company or companies referred to in this research may be obtained from GS (Asia) L.L.C., Seoul Branch. New Zealand: GS New Zealand Limited and its affiliates are neither “registered banks” nor “deposit takers” (as defined in the Reserve Bank of New Zealand Act 1989) in New Zealand. This research, and any access to it, is intended for “wholesale clients” (as defined in the Financial Advisers Act 2008) unless otherwise agreed by GS. A copy of certain GS Australia and New Zealand disclosure of interests is available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html.

Russia: Research reports distributed in the Russian Federation are not advertising as defined in the Russian legislation, but are information and analysis not having product promotion as their main purpose and do not provide appraisal within the meaning of the Russian legislation on appraisal activity. Research reports do not constitute a personalized investment recommendation as defined in Russian laws and regulations, are not addressed to a specific client, and are prepared without analyzing the 

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
