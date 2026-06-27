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
- 已识别机构名：`摩根斯坦利`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
June 25, 2026 07:47 AM GMT

# China Autos & Shared Mobility | Asia Pacific

# Demand floor in place, rebound catalysts arrive later

Takeaways from recent channel checks and industry calls suggest that auto sales have likely found a floor, but have yet to regain momentum, with demand still conspicuously weak. Next meaningful window appears in Aug–Sept, when new model cycles, seasonal factors, and geopolitical dynamics converge.

As the sector closes out a challenging 2Q, investor conversations indicate that sentiment is worse than underlying reality. Persistent growth concerns, coupled with a lack of near-term earnings catalysts, continue to limit bottom-up conviction. At the same time, the ongoing liquidity drain toward regional AI/tech plays has distorted sector discussions, with most dialogues remaining at a high-level rather than focusing on company fundamentals (e.g., BYD, Geely, NIO, XPeng, Fuyao).

The market increasingly reflects a binary divide between AI and everything else (including autos). That said, we believe this pessimism is setting up potential trading opportunities in 2H, with a window likely emerging in mid-3Q, supported by low base effects, above-seasonal demand underpinned by solid order books, policy-driven consumption support, and an early ramp in new launches from late July. Some investors may also begin to pull forward valuation frameworks to 2027. Within this context, BYD and Geely appear well positioned for a rebound, while XPeng remains an event-driven story despite ongoing debate.

We address some topical enquiries and key feedback from recent channel checks:

June sales should be stronger than headline data suggests, supported by better-than-expected sell-through driven by extended 618 promotions, stacked subsidies, license-plate exemptions in select cities, and lower fuel prices offering temporary relief to ICE demand. Wholesale volumes are likely to rise by low-teens MoM, led by BEVs and PHEVs, with modest gains in HEVs, particularly in the RMB150–200k segment. Notably, some OEMs are subtly lowering targets and prioritizing inventory digestion to protect channel profitability and prepare for a cleaner restart ahead of 2H product launches. We estimate 2Q PV wholesale volumes at 6.7–6.9mn units, down 3–5% YoY (vs. -8% in 1Q), with the YoY gap likely normalizing in 2H.

July should see a seasonal lull, with a more meaningful recovery potentially emerging in Aug–Sept as purchase intent improves. In our view, the market may start to price this in ahead of realization.

On the demand side, consumers remain cautious amid rapid EV iteration. Frequent model refreshes, fast-paced specification upgrades, and ongoing price cuts are extending decision cycles. Meanwhile, the ICE segment appears structurally challenged, with discounting no longer effectively converting traffic, and widening disadvantages in AD/AI capabilities and resale values.

MS ASIA LIMITED+

Tim Hsiao  
Equity Analyst  
Tim.Hsiao@morganstanley.com +852 2848-1982

Peggy Wang  
Research Associate  
Peggy.Pc.Wang@morganstanley.com +852 3963-3934

Equity Analyst
Shelley.Wang@morganstanley.com +852 3963-0047

Joey Xu, CFA  
Equity Analyst  
Joey.Xu@morganstanley.com +852 3963-0337

![](images/f9814f34daf590ee63526204075e93ad58f5a0cf754103a4258e5f6158f1e3a8.jpg)

In-Line

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

The mass-market segment (\~RMB150k) is expected to regain some traction in 2H, supported by new offerings from BYD and Geely filling the gap left by ICE displacement. These launches appear largely incremental rather than cannibalistic.

In contrast, competitive pressures in the premium/luxury segment are intensifying, as reflected in BMW's recent guidance cut. The challenges faced in China and APAC appear structural rather than company-specific. The RMB300–400k segment increasingly looks like the last line of defense, but remains under pressure. Industry feedback suggests that a credible response from global OEMs now requires native EV platforms, advanced ADAS capabilities, and residual value guarantees. We remain cautious, as brand erosion in this segment is unlikely to be linear and could accelerate.

Policy remains supportive but is unlikely to be a major catalyst this year. The 2026 trade-in subsidy pool (\~RMB125bn) is being deployed more gradually than last year, with daily applications of 20–30k units (over 50% of monthly sales) and potential upside in Aug–Sept. Recent policy measures targeting auto circulation and after-sales ecosystems are constructive but should have limited near-term demand impact. Overall, policy appears to be in stabilization rather than stimulus mode.

In terms of models that draw market attention, feedback varies, but frequently cited models include BYD Great Tang (with \~40–50k locked orders post-launch), Sea Lion 08, XPeng Mona L03, Li Auto L8 Livis, Geely Battleship 700, and Xiaomi Sky Nomad N90.

Finally, the HIMA ecosystem continues to expand, albeit with rising internal competition. Huawei's strategy of partnering with large state-owned OEMs to deploy HarmonyOS across multiple segments is effectively a broad-based market capture approach. However, with five brands spanning different price tiers and a consistent rollout of lower-priced follow-on models, pricing is increasingly used as a share gain lever rather than a margin driver, raising the risk of internal cannibalization.

## Valuation Methodology and Risks

## BYD Company Limited (002594.SZ)

Blended methodology, weighted 25% bull, 50% base, 25% bear. We think incremental volume from ADAS adoption and trade-in stimulus extension could partially offset the fierce competitive landscape in the mass market segment.

We apply a 5% premium to our H-share bull and bear case scenario values; no premium in our bear case.

We use an exchange rate of 1.06 RMB/HKD.

## Risks to Upside

■ New model launch schedule

■ Faster-than-expected overseas expansion

■ Stronger-than-expected demand for NEVs globally

## Risks to Downside

\- Lack of progress in overseas expansion amid rising protectionism

■ Weaker-than-expected demand for NEVs

■ Worse-than-expected gross margin

## Geely Automobile Holdings (0175.HK)

Base case, DCF. We assume a WACC of $11.2\%$ and terminal growth rate of $3\%$ .

## Risks to Upside

■ Continuous NEV market share gain domestically.

■ More meaningful reduction in losses for its NEV businesses, via scale benefits.

■ Stronger-than-expected profitability, driven by higher overseas sales.

## Risks to Downside

■ More notable than expected slowdown in domestic vehicle demand.

■ Expanding losses at Geely's NEV businesses amid price competition.

■ A slowdown in overseas sales due to competition and protectionism.

## BYD Company Limited (1211.HK)

Blended methodology, weighted 25% bull, 50% base, 25% bear. We think incremental volume from ADAS adoption and trade-in stimulus extension could partially offset the fierce competitive landscape in the mass market segment.

■ Bull: SOTP, implying 40x 2026E bull P/E. Reflects re-rating of comps (CATL, EV startups).

■ Base: DCF (14.3% WACC, 3.0% long-term growth).

■ Bear: 12x 2026E P/E - worse auto sales domestically and overseas, more severe price cuts.

## Risks to Upside

■ New model launches

■ Faster-than-expected overseas expansion

■ Stronger-than-expected demand for NEVs globally

## Risks to Downside

\- Lack of progress in overseas expansion amid rising protectionism

■ Weaker-than-expected demand for NEVs globally

■ Worse-than-expected gross margin

## XPeng Inc. (9868.HK)

Derived from our ADR price target using 7.85 HKD/USD. We assign 30%/50%/20% weightings to our bull/base/bear case scenarios - the bull/bear weighting reflects the potential for valuation re-rating from non-vehicle business/the macro outlook to weaken and sector competition to worsen.

Key base case assumptions: 3% terminal growth rate, 1.6x beta, 12.8% WACC.

## Risks to Upside

■ More competitive model introductions that drive volume growth

■ Greater-than-expected margin expansion

■ Better-than-expected branding with superior in-car user experience

## Risks to Downside

■ Intensified competition in the mid-/high-end segments

■ Cash flow pressure with lower profitability

■ Moderating auto sales growth pressuring overall industry valuation

## XPeng Inc. (XPEV.N)

Probability-weighted DCF methodology. Weightings for our bull (SoTP)/base/bear case scenarios are 30%/50%/20% - the bull/bear weighting reflects the potential for valuation re-rating from non-vehicle business/the macro outlook to weaken and sector competition to worsen.

Key base case assumptions: 3% terminal growth rate, 1.6x beta, 12.8% WACC.

## Risks to Upside

■ More competitive model introductions that drive volume growth

■ Greater-than-expected margin expansion

■ Better-than-expected branding with superior in-car user experience

## Risks to Downside

■ Intensified competition in the midrange/high-end segments

■ Cash flow pressure with lower profitability

■ Moderating auto sales growth pressuring overall industry valuation

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Asia Limited (which accepts the responsibility for its contents) and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents), and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS, and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Tim Hsiao; Shelley Wang, CFA; Joey Xu, CFA.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

As of May 29, 2026, MS beneficially owned 1% or more of a class of common equity securities of the following companies covered in MS: Brilliance China Automotive, BYD Company Limited, Changzhou Xingyu Automotive Lighting Sys, EHang Holdings Ltd, Geely Automobile Holdings, Great Wall Motor Company Limited, Li Auto Inc., NIO Inc., Suzhou Recodeal Interconnect System, Voyah Automotive Technology Co. Ltd., WeRide Inc, XPeng Inc., Zhengzhou Yutong Bus Co.

Within the last 12 months, MS managed or co-managed a public offering (or 144A offering) of securities of Horizon Robotics, NIO Inc., WeRide Inc, Zhongsheng Group Holdings. Within the last 12 months, MS has received compensation for investment banking services from Huizhou Desay SV Automotive Co Ltd, NIO Inc., WeRide Inc.

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from BYD Company Limited, Changzhou Xingyu Automotive Lighting Sys, Chongqing Changan Automobile, EHang Holdings Ltd, Fuyao Glass Industry Group, Geely Automobile Holdings, Great Wall Motor Company Limited, Hesai Group, Huayu Automotive, Huizhou Desay SV Automotive Co Ltd, Li Auto Inc., Minth Group Limited, Ningbo Joyson Electronic Corp, Ningbo Tuopu Group Co Ltd, NIO Inc., SAIC Motor Corp. Ltd., WeRide Inc, Zhongsheng Group Holdings.

Within the last 12 months, MS has received compensation for products and services other than investment banking services from BYD Company Limited, EHang Holdings Ltd, Geely Automobile Holdings, Hesai Group, Horizon Robotics, Minth Group Limited, Zhongsheng Group Holdings.

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: BYD Company Limited, Changzhou Xingyu Automotive Lighting Sys, Chongqing Changan Automobile, EHang Holdings Ltd, Fuyao Glass Industry Group, Geely Automobile Holdings, Great Wall Motor Company Limited, Hesai Group, Horizon Robotics, Huayu Automotive, Huizhou Desay SV Automotive Co Ltd, Li Auto Inc., Minth Group Limited, Ningbo Joyson Electronic Corp, Ningbo Tuopu Group Co Ltd, NIO Inc., SAIC Motor Corp. Ltd., WeRide Inc, Zhongsheng Group Holdings.

Within the last 12 months, MS has either provided or is providing non-investment banking, securities-related services to and/or in the past has entered into an agreement to provide services or has a client relationship with the following company: BYD Company Limited, China MeiDong Auto Holdings Ltd, EHang Holdings Ltd, Geely Automobile Holdings, Hesai Group, Horizon Robotics, Minth Group Limited, NIO Inc., Zhongsheng Group Holdings.

The equity research analysts or strategists principally responsible for the preparation of MS have received compensation based upon various factors, including quality of research, investor client feedback, stock picking, competitive factors, firm revenues and overall investment banking revenues. Equity Research analysts' or strategists' compensation is not linked to investment banking or capital markets transactions performed by MS or the profitability or revenues of particular trading desks.

MS and its affiliates do business that relates to companies/instruments covered in MS, including market making, providing liquidity, fund management, commercial banking, extension of credit, investment services and investment banking. MS sells to and buys from customers the securities/instruments of companies covered in MS on a principal basis. MS may have a position in the debt of the Company or instruments discussed in this report. MS trades or may trade as principal in the debt securities (or in related derivatives) that are the subject of the debt research report.

Certain disclosures listed above are also for compliance with applicable regulations in non-US jurisdictions.

## STOCK RATINGS

MS uses a relative rating system using terms such as Overweight, Equal-weight, Not-Rated or Underweight (see definitions below). MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold and sell. Investors should carefully read the definitions of all ratings used in MS. In addition, since MS contains more complete information concerning the analyst's views, investors should carefully read MS, in its entirety, and not infer the contents from the rating alone. In any case, ratings (or research) should not be used or relied upon as investment advice. An investor's decision to buy or sell a sto

[中间内容因长度限制已省略]

 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: China Autos & Shared Mobility

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/24/2026)</td></tr><tr><td colspan="3">Joey Xu, CFA</td></tr><tr><td>Anhui Jianghuai Automobile (600418.SS)</td><td>E (08/19/2023)</td><td>Rmb28.97</td></tr><tr><td>BAIC Motor (1958.HK)</td><td>E (10/02/2025)</td><td>HK$0.89</td></tr><tr><td>Brilliance China Automotive (1114.HK)</td><td>E (03/31/2025)</td><td>HK$1.98</td></tr><tr><td>Chongqing Changan Automobile (000625.SZ)</td><td>E (03/03/2026)</td><td>Rmb7.02</td></tr><tr><td>Guangzhou Automobile Group (601238.SS)</td><td>U (10/23/2019)</td><td>Rmb5.32</td></tr><tr><td>Guangzhou Automobile Group (2238.HK)</td><td>O (05/05/2020)</td><td>HK$2.18</td></tr><tr><td>Huayu Automotive (600741.SS)</td><td>O (09/08/2020)</td><td>Rmb16.53</td></tr><tr><td>Jiangsu Changshu Automotive Trim Group (603035.SS)</td><td>E (08/14/2023)</td><td>Rmb10.90</td></tr><tr><td>Ningbo Huaxiang Electronic Co., Ltd. (002048.SZ)</td><td>E (05/05/2026)</td><td>Rmb24.73</td></tr><tr><td>SAIC Motor Corp. Ltd. (600104.SS)</td><td>O (11/25/2021)</td><td>Rmb10.08</td></tr><tr><td>Voyah Automotive Technology Co. Ltd, (7489.HK)</td><td>O (03/31/2026)</td><td>HK$3.43</td></tr><tr><td>Zhengzhou Yutong Bus Co (600066.SS)</td><td>E (09/22/2023)</td><td>Rmb26.65</td></tr><tr><td colspan="3">Shelley Wang, CFA</td></tr><tr><td>Beijing Jingwei Hirain Technologies (688326.SS)</td><td>U (09/27/2024)</td><td>Rmb72.18</td></tr><tr><td>Bethel Automotive Safety Systems Co Ltd (603596.SS)</td><td>O (12/11/2023)</td><td>Rmb25.73</td></tr><tr><td>Changzhou Xingyu Automotive Lighting Sys (601799.SS)</td><td>O (09/27/2024)</td><td>Rmb110.58</td></tr><tr><td>China MeiDong Auto Holdings Ltd (1268.HK)</td><td>E (01/08/2024)</td><td>HK$0.59</td></tr><tr><td>China Yongda Automobiles Services (3669.HK)</td><td>E (08/13/2024)</td><td>HK$0.74</td></tr><tr><td>Foryou Corporation (002906.SZ)</td><td>O (03/06/2024)</td><td>Rmb26.14</td></tr><tr><td>Fuyao Glass Industry Group (600660.SS)</td><td>E (12/01/2016)</td><td>Rmb48.13</td></tr><tr><td>Fuyao Glass Industry Group (3606.HK)</td><td>E (12/01/2016)</td><td>HK$49.42</td></tr><tr><td>Huizhou Desay SV Automotive Co Ltd (002920.SZ)</td><td>O (02/28/2025)</td><td>Rmb83.87</td></tr><tr><td>Keboda (603786.SS)</td><td>O (01/17/2024)</td><td>Rmb44.40</td></tr><tr><td>Minth Group Limited (0425.HK)</td><td>O (08/24/2015)</td><td>HK$27.38</td></tr><tr><td>NavInfo Co Ltd (002405.SZ)</td><td>U (03/06/2024)</td><td>Rmb6.92</td></tr><tr><td>Nexteer Automotive Group (1316.HK)</td><td>E (02/28/2025)</td><td>HK$4.06</td></tr><tr><td>Ningbo Joyson Electronic Corp (600699.SS)</td><td>E (03/11/2026)</td><td>Rmb22.76</td></tr><tr><td>Ningbo Tuopu Group Co Ltd (601689.SS)</td><td>E (11/12/2025)</td><td>Rmb58.20</td></tr><tr><td>Ningbo Xusheng Group Co Ltd (603305.SS)</td><td>E (06/18/2025)</td><td>Rmb12.91</td></tr><tr><td>Suzhou Recodeal Interconnect System (688800.SS)</td><td>U (09/27/2024)</td><td>Rmb99.80</td></tr><tr><td>TUHU Car Inc (9690.HK)</td><td>O (07/29/2024)</td><td>HK$12.24</td></tr><tr><td>Zhejiang Sanhua Intelligent Controls (002050.SZ)</td><td>E (11/12/2025)</td><td>Rmb43.90</td></tr><tr><td>Zhongsheng Group Holdings (0881.HK)</td><td>O (10/12/2021)</td><td>HK$5.20</td></tr><tr><td colspan="3">Tim Hsiao</td></tr><tr><td>BAIC BluePark New Energy (600733.SS)</td><td>U (08/07/2024)</td><td>Rmb5.22</td></tr><tr><td>BYD Company Limited (002594.SZ)</td><td>O (04/14/2025)</td><td>Rmb83.30</td></tr><tr><td>BYD Company Limited (1211.HK)</td><td>O (04/14/2025)</td><td>HK$75.95</td></tr><tr><td>EHang Holdings Ltd (EH.O)</td><td>O (03/13/2025)</td><td>US$6.63</td></tr><tr><td>Geely Automobile Holdings (0175.HK)</td><td>O (06/26/2024)</td><td>HK$17.56</td></tr><tr><td>Great Wall Motor Company Limited (601633.SS)</td><td>U (03/16/2022)</td><td>Rmb16.02</td></tr><tr><td>Great Wall Motor Company Limited (2333.HK)</td><td>E (01/08/2024)</td><td>HK$9.60</td></tr><tr><td>Hesai Group (HSAI.O)</td><td>O (07/28/2025)</td><td>US$15.61</td></tr><tr><td>Horizon Robotics (9660.HK)</td><td>O (12/02/2024)</td><td>HK$4.02</td></tr><tr><td>Li Auto Inc. (LI.O)</td><td>O (08/24/2020)</td><td>US$12.39</td></tr><tr><td>Li Auto Inc. (2015.HK)</td><td>O (11/16/2021)</td><td>HK$49.44</td></tr><tr><td>NIO Inc. (9866.HK)</td><td>O (10/03/2022)</td><td>HK$39.08</td></tr><tr><td>NIO Inc. (NIO.N)</td><td>O (08/26/2020)</td><td>US$4.90</td></tr><tr><td>WeRide Inc (WRD.O)</td><td>O (11/19/2024)</td><td>US$5.60</td></tr><tr><td>XPeng Inc. (9868.HK)</td><td>O (11/16/2021)</td><td>HK$49.14</td></tr><tr><td>XPeng Inc. (XPEV.N)</td><td>O (01/29/2021)</td><td>US$12.48</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.

\* Historical prices are not split adjusted.

© 2026 MS
"""
