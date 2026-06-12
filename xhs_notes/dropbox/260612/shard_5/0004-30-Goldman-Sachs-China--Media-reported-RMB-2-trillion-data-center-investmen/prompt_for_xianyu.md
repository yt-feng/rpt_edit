你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

【研报解析内容】
"""
# China: Media reported RMB 2 trillion data center investment not new news

## Bottom line:

A recent Bloomberg article on the Chinese government's plan to spend RMB 2 trillion on data center building has attracted market attention. However, this is not new news and was part of the “Six Networks” laid out in the 15th Five-Year Plan in March. Recent policy signals suggest implementation of China’s broader “Six Networks” — water networks, new-type power grids, computing power networks (including data centers), next-generation communication networks, urban underground pipeline networks, and logistics networks — investment push may be accelerating, supported by a wider funding mix that includes central and local government bonds, the policy bank new financing tool, and commercial bank lending. In our view, this points to a further shift in government-led investment toward high-tech manufacturing, AI infrastructure, strategic supply chains, and people’s livelihoods. Separately, we note that recent increases in policy communication and project preparation suggest policymakers may be laying the groundwork for faster deployment in H2 after the Q2 slowdown in fiscal spending. We continue to expect China’s augmented fiscal deficit (AFD) to widen after narrowing in Q2.

## Main points:

1. What happened? A 9 June Bloomberg article reported that “China is preparing to spend around 2 trillion yuan (\$295 billion) over the next five years on building data centers across the country”, drawing market attention to AI-related high-tech investment. The report said SOEs such as China Mobile and China Telecom will operate most of the facilities, while domestic suppliers including Huawei are expected to provide at least 80% of key technologies, such as AI chips. On 26 May, the Head of National Energy Administration, Wang Hongzhi, projected that annual electricity consumption by China’s data centers will rise to 800TWh in 2030 from 170TWh in 2025, implying 36% annualized growth over 2026-30 and an increase in the share of total power consumption to 6% from 1.6%. On 9 June, the state-run CCTV re-emphasized policymakers’ commitment to strengthening the “Six Networks” (“六张网”) — water networks, new-type power grids, computing power networks (including data centers), next-generation communication networks, urban underground pipeline networks, and logistics networks — echoing the April Politburo meeting. Reputable onshore media, including the 21st Century Business Herald, flagged in early June that some local governments have accelerated implementation of the policy bank new financing tool in recent months to support investment in strategically important areas such as high-tech manufacturing, AI, green transition, urban renewal, and services consumption.

2. How significant? Based on our estimates, the reported RMB2tn of data center

Lisheng Wang

+852-3966-4004

lisheng.wang@gs.com

GS (Asia) L.L.C.

investment would account for only 0.8% of fixed asset investment (FAI) over 2026-30. More broadly, at the March “Two Sessions”, NDRC Head Zheng Shanjie expected that China’s investment in the “Six Networks” could exceed RMB7tn this year — equivalent to about 14% of FAI by our estimates — and that the economic scale of AI-related industries could surpass RMB10tn by 2030, although the definition of those industries remains unclear. Incorporating recent policy communications, we believe the funding for the “Six Networks” in general, and data centers in particular, will come from ultra-long-term central government special bonds (i.e., those earmarked for the “Two Majors” investment projects), local government special bonds, policy bank new financing tool, and commercial bank lending. In our view, this funding structure is intended to crowd in private capital while avoiding the high-risk, off-balance-sheet LGFV borrowing seen in previous cycles.

3. Why now? Under China's current reactive (rather than pre-emptive) policy approach, the timing and scale of easing remain data-dependent. After the stronger-than-expected Q1 GDP data, the pace of government bond issuance and spending slowed markedly in Q2, our proprietary augmented fiscal deficit (AFD) measure narrowed, and investment momentum weakened — all of which, in our view, reflected a deliberate policy choice. Without a meaningful policy offset, the ongoing global energy supply shock has also weighed on sequential growth in Q2. That said, the RMB7.7tn of unspent government bond quota as of end-May (out of RMB11.9tn for the full year), the RMB800bn policy bank new financing tool available this year (up from RMB500bn last year), and the RMB700bn year-on-year increase in outstanding fiscal deposits all suggest ample funding capacity in coming quarters. Recent developments suggest policymakers have become more cautious about the growth slowdown and are stepping up efforts to prepare investment pipelines for deployment.

4. What's the macro implication? The reported RMB2tn plan for data center investment is not new, as authorities have made similar projections before, including in January 2025 by the National Data Administration and in April 2026 by CCTV. While there has been no additional funding arrangement beyond this year's budget, recent developments suggest implementation could accelerate in coming months and reinforce our view that China's AFD may widen in H2 after narrowing in Q2 (Exhibit 1). The continued shift in government-led investment toward high-tech manufacturing, AI infrastructure, strategic supply chains, and people's livelihoods underscores policymakers' growing emphasis on high-quality growth and tech self-reliance, in line with guidance from the 4th Plenum and the 15th Five-Year Plan (for 2026-30). We see July as an important window for potential policy fine-tuning: if growth continues to soften and Q2 GDP disappoints meaningfully, there is a decent chance for policymakers to step up their easing rhetoric in the July Politburo meeting and draw on remaining fiscal buffers quickly to stabilize investment and growth, in our view (Exhibit 2).

## Lisheng Wang

Exhibit 1: We expect China's AFD to widen in H2 after narrowing in Q2  
![](images/f3ddad339a2327b70e59e7d82bfbf99d83972596d4203d49929de44e907f82c1.jpg)

<details>
<summary>line chart</summary>

| Year | 3mma | 12mma |
|------|------|-------|
| 2026 | -12.0% | -12.0% |
</details>

Source: Wind, CEIC, GS Global Investment Research

Exhibit 2: Key upcoming macro catalysts for China markets

<table><tr><td>Date</td><td>Events</td></tr><tr><td>15 Jul 2026</td><td>Q2 2026 GDP release</td></tr><tr><td>End-Jul 2026</td><td>Politburo meeting on economic policies</td></tr><tr><td>24 Sep 2026 (likely)</td><td>President Xi&#x27;s potential state visit to the US (invited by US President Trump)</td></tr><tr><td>19 Oct 2026</td><td>Q3 2026 GDP release</td></tr><tr><td>Fall 2026 (likely)</td><td>The 5th Plenum of the 20th CCP Central Committee</td></tr><tr><td>11 Nov 2026</td><td>Expiration of tariff/rare earth control pause agreed at Trump-Xi meeting in South Korea</td></tr><tr><td>18-19 Nov 2026</td><td>APEC 2026 China (in Shenzhen)</td></tr><tr><td>Early to mid-Dec 2026</td><td>Politburo meeting on economic policies</td></tr><tr><td>Mid-Dec 2026</td><td>Central Economic Work Conference</td></tr><tr><td>14-15 Dec 2026</td><td>G20 Summit in Miami</td></tr></table>

Source: Government websites, Data compiled by GS Global Investment Research

## The China Economics Team

## Andrew Tilton

+852-2978-1802

andrew.tilton@gs.com

GS (Asia) L.L.C.

## Hui Shan

+852-2978-6634

hui.shan@gs.com

GS (Asia) L.L.C.

## Lisheng Wang

+852-3966-4004

lisheng.wang@gs.com

GS (Asia) L.L.C.

## Xinquan Chen

+852-2978-2418

xinquan.chen@gs.com

GS (Asia) L.L.C.

## Yuting Yang

+852-2978-7283

yuting.y.yang@gs.com

GS (Asia) L.L.C.

## Chelsea Song

+852-2978-0106

chelsea.song@gs.com

GS (Asia) L.L.C.

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

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for information purposes only and is not, and under no circumstances should be construed as, an advertisement, offering or solicitation by GS & Co. LLC for purchasers of securities in Canada to trade in any Canadian security. GS & Co. LLC is not registered as a dealer in any jurisdiction in Canada under applicable Canadian securities laws and generally is not permitted to trade in Canadian securities and may be prohibited from selling certain securities and products in certain jurisdictions in Canada. If you wish to trade in any Canadian securities or other products in Canada please contact GS Canada Inc., an affiliate of The GS Group Inc., or another registered Canadian dealer. Hong Kong: Further information on the securities of covered companies referred to in this research may be obtained on request from GS (Asia) L.L.C. India: Further information on the subject company or companies referred to in this research may be obtained from GS (India) Securities Private Limited, Research Analyst - SEBI Registration Number INH000001493, 10th Floor, Ascent-Worli, Sudam Kalu Ahire Marg, Worli, Mumbai-400 025, India, Corporate Identity Number U74140MH2006FTC160634, Phone +91 22 6616 9000, Fax +91 22 6616 9001. GS may beneficially own 1% or more of the securities (as such term is defined in clause 2 (h) the Indian Securities Contracts (Regulation) Act, 1956) of the subject company or companies referred to in this research report. Investment in securities market are subject to market risks. Read all the related documents carefully before investing. Registration granted by SEBI and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. GS (India) Securities Private Limited compliance officer and investor grievance contact details can be found at: https://www.goldmansachs.com/worldwide/india/documents/Grievance-Redressal-and-Escalation-Matrix.pdf, and a copy of the annual audit compliance report can be found at this link: https://publishing.gs.com/content/site/india-annual-compliance-report.html. Japan: See below. Korea: This research, and any access to it, is intended only for “professional investors” within the meaning of the Financial Services and Capital Markets Act, unless otherwise agreed by GS. Further information on the subject company or companies referred to in this research may be obtained from GS (Asia) L.L.C., Seoul Branch. New Zealand: GS New Zealand Limited and its affiliates are neither “registered banks” nor “deposit takers” (as defined in the Reserve Bank of New Zealand Act 1989) in New Zealand. This research, and any access to it, is intended for “wholesale clients” (as defined in the Financial Advisers Act 2008) unless otherwise agreed by GS. A copy of certain GS Australia and New Zealand disclosure of interests is available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Russia: Research reports distributed in the Russian Federation are not advertising as defined in the Russian legislation, but are information and analysis not having product promotion as their main purpose and do not provide appraisal within the meaning of the Russian legislation on appraisal activity. Research reports do not constitute a personalized investment recommendation as defined in Russian laws and regulations, are not addressed to a specific client, and are prepared without analyzing the financial circumstances, investment profiles or risk profiles of clients. GS assumes no respon

[中间内容因长度限制已省略]

ttempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

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
