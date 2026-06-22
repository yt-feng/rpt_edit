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
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`JPM`。标题格式建议：`# JPM：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份JPM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Japan Quant Strategy

MLCCs and supply bottleneck effect: Next candidates, momentum positions, and tailwind from long-term investors' shift to Japan

In recent years, so-called MLCC (multilayer ceramic capacitors)-related stocks, such as Murata Manufacturing (6981) and Taiyo Yuden (6976), have been trading at elevated levels, attracting the attention of both domestic and overseas investors. While this phenomenon is seen by most market participants as an extension of fundamentals-driven AI demand, there has been little discussion from a technical perspective regarding upside potential or exit strategies.

We, the QDS team, have long viewed the current AI boom in relation to the EM (Emerging Markets) boom of the mid-2000s. Under this framework, we expect MLCC stocks to continue to enjoy upward momentum for the time being, albeit with some volatility. This is because, when compared to the EM boom, we believe the AI boom is currently past the sixth stage overall and that there is room for buying by both short-term and long-term investors.

Specifically, two MLCC-related companies (Murata and Taiyo Yuden), for example, are generally seen to possess oligopolistic market positions, a supply structure that makes it difficult to increase production. Consequently, when supply/demand tightens due to a surge in demand (extraordinary demand), their profits tend to grow more rapidly than their sales volume. In addition, the phenomenon of excess profits flowing to companies that command such supply bottlenecks is not unique to the current situation. For example, during the EM boom, following the first wave of infrastructure investment in the BRICs during the early phase (2002–2005), nickel smelting at Sumitomo Metal Mining (5713), ultra-thin copper foil at Mitsui Mining (5706), silicon wafers at Shin-Etsu Chemical (4063), and low-thermal expansion alloys at Shinpokoku Materials (5542) all entered a period of excess profit generation that followed a similar pattern, propelled by rising volumes of flat-panel TVs, mobile phones, and semiconductors (Figure 1). Note that the correlation between stock prices in both phases is based on the results of measuring the “similarity” by applying an embedded method (Embedding), which utilizes return patterns as features after aligning each company’s stock prices using the Dynamic Time-Winding (DTW) method.

What is important is the sequence of events that led to the simultaneous collapse of these EM-related stocks in the second half of 2007. The subprime mortgage crisis was merely a trigger. In our view, the fundamental reason was that supply bottlenecks shifted from electronics components to bulk commodities and ocean freight rates (Figure 2), causing speculative capital (attempting to follow the shifting boom) to pull out simultaneously from the existing group of stocks. It is our belief that it was not that the oligopoly or technological advantages were compromised but rather that the source of excess profits shifted to the next group of stocks, where bottlenecks were forming within the supply chain. In other words, the sustainability of this profit depends more on the position of the bottleneck in the supply network than on the competitiveness of the company. At present, there are few signs of such a “shift” driven by risk capital flowing into MLCC-related companies. Upstream sectors, such as semiconductors and manufacturing equipment, HBM, and CoWoS, are still on an expansion

See page 5 for analyst certification and important disclosures.

Global Quantitative and Derivatives Strategy

Masanari Takada AC
(81-3) 6736-8636
masanari.takada@JPM.com
JPM Securities Japan Co., Ltd.

Tony SK Lee
(852) 2800-8857
tony.sk.lee@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Robert Smith, PhD
(61-2) 9003-8808
robert.z.smith@JPM.com
JPM Securities Australia Limited

Khuram Chaudhry
(44-20) 7134-6297
khuram.chaudhry@JPM.com
JPM Securities plc

Dubravko Lakos-Bujas
(1-212) 622-3601
dubravko.lakos-bujas@JPM.com
JPM Securities LLC

trend, and the bottleneck position is likely to remain within the current stock group, including MLCCs.

Factor characteristics also reflect this. We estimate the factor structure of the two MLCC-related companies and the electrical equipment sector (TSE Sector 33) to which they belong (Figure 3). Recently, Momentum and Beta factors have been notably high while Quality has been low. Stock prices are currently being supported not by the quality of earnings but by price trends and market correlation (Beta). Of course, this could become a weakness if the expected peak of the AI boom is near. However, assuming that there is still room for growth in the AI boom itself, this combination is likely to produce positive returns over the short term (high expected returns). The core buyers are short-term momentum traders that follow the trend based on signs of improving earnings, and we think there is still room to build up positions, especially if the improvement in profit margin momentum is maintained.

On the other hand, the flow of global active investment trusts, which represent long-term capital, are also likely to broadly support growth sectors such as electrical equipment. In terms of sector allocation to Japanese stocks by these active funds (focused on developed markets), the Technology, Hardware & Equipment sector (to which MLCC-related companies belong) has remained neutral to slightly underweight relative to the benchmark and has been largely stable for the past six months (Figure 10). It is highly likely that more patient, long-term investors have not yet entered the market for current bottleneck stocks such as MLCC-related companies. It seems reasonable to expect a pattern in which these long-term investors begin buying once a price correction has cooled the overheated market. In addition, global active funds are continuing a rotation that reduces China's weighting in their regional allocations and shifts it toward Japan, South Korea, and Taiwan as part of their broader investment strategy. From a relative perspective as well, growth sectors such as Japanese electrical equipment look well-positioned to benefit from this shift. From this perspective as well, we think that Japan's bottleneck-related stocks, such as MLCC makers, have characteristics that are easy to sustain once momentum is maintained. However, given their high Beta and low Quality, investors should be aware that corrections during cool-down periods tend to be both rapid and severe. On the other hand, when considering taking profits on MLCC-related companies, it could be appropriate to measure the situation based on three factors: the position of the upstream semiconductor and manufacturing equipment cycles, the allocation of long-term overseas capital, and the rise of the next bottleneck-related sector.

Figure 1: Similar patterns seen in the AI Boom and the EM Boom (example of Japanese stocks) – The same behavior seen in current MLCC-related stocks also occurred among bottleneck stocks during the EM boom  
![](images/f4d028529761ed9b1078d26dcf73d77f2ee5cb257a8b9ea72df2c4c8f6fdde45.jpg)  
Source: Bloomberg Finance L.P., JPM Global Markets Strategy

Figure 2: Similar patterns seen in the AI Boom and the EM Boom (example of Japanese stocks) – The “bottleneck cascade effect” during the EM boom subsequently shifted its main focus to ocean freight rates  
![](images/eb97df257282442217379e192f9dc4c61beec44a17316d87d5f8e793f636b66a.jpg)  
Source: Bloomberg Finance L.P., JPM Global Markets Strategy

Figure 3: Factor exposure of electrical equipment (TSE 33 sector): As of June 12  
![](images/2057a44f5abd49754988476bbfece00a1181c7a70af7838c9be46ebcce82dfa0.jpg)  
Source: Bloomberg Finance L.P., JPM Global Markets Strategy

Figure 4: Factor exposure of two MLCC-related companies (Murata Manufacturing and Taiyo Yuden): As of June 12  
![](images/b86855c5130ebda044909887d7ed50cc7a5ef4e21571cb0cd0cfeadcf728c833.jpg)  
Source: Bloomberg Finance L.P., JPM Global Markets Strategy

Figure 5: Estimated net position and profit margin momentum of Cash Equity Trend-Followers for two MLCC-related companies: Murata Manufacturing  
![](images/cc3c91005874fc73564c29a696688af52b92e908e347061b9152b752b93c7c2c.jpg)  
Source: Bloomberg Finance L.P., JPM Global Markets Strategy

Figure 6: Estimated net position and profit margin momentum of Cash Equity Trend-Followers for two MLCC-related companies: Taiyo Yuden  
![](images/eb0b56a4aa6a4dfda95232fe53ae1deb032684bf6dd568b3ea70c2f00be584eb.jpg)  
Source: Bloomberg Finance L.P., JPM Global Markets Strategy

Figure 7: Regional Allocation of global active investment trusts (DM+EM) (mainland China stocks + Hong Kong stocks) and US import ratios from China  
![](images/41453177c1b3c4aba075c2b5cb51f700048e08ababe8dd4b1110e878a7e5c707.jpg)  
Source: EPFR, Bloomberg Finance L.P., JPM Global Markets Strategy

Figure 8: Relative differences in regional allocation of global active investment trusts (DM+EM) (Japanese stocks vs. mainland China stocks + Hong Kong stocks) and relative performance of growth stock indices (Japanese stocks vs. Chinese stocks)  
![](images/e0ce7be0b74fbe98edbad4ba67f6fd1bc7b300c87be8c17e9a2ed33ec332ef24.jpg)  
Source: EPFR, Bloomberg Finance L.P., JPM Global Markets Strategy

Figure 9: Regional allocation of global active investment trusts (DM+EM): As of end-April  
![](images/8be2f6044def3677854befa7dfc8cac7447eaf5496580aeac3ad778e5a55eb16.jpg)  
Source: EPFR, Bloomberg Finance L.P., JPM Global Markets Strategy

Figure 10: Regional allocation of global active investment trusts (DM+EM) – Trends for Japan, South Korea, and Taiwan: As of end-April  
![](images/6d97fd5345d12a1df9e3dd7649417db494b3a80f58eea48911b2c3908925d2cc.jpg)  
Source: EPFR, Bloomberg Finance L.P., JPM Global Markets Strategy

Figure 11: Sector weightings of Japanese stocks in global active investment trusts (DM) (Active vs. Passive): As of end-April  
![](images/ebd5991d3d649b5c72fc4de51c6ff5ecff27a13f49dc63e92bcad530c7e4ce2d.jpg)  
Source: EPFR, Bloomberg Finance L.P., JPM Global Markets Strategy

Figure 12: Changes in sector weightings of Japanese stocks in global active investment trusts (DM) (Active vs. Passive): As of end-April  
![](images/f57ebc3121703fd627a4cf55d68349c7e257da03f68408367bae110ff9d74db5.jpg)  
Source: EPFR, Bloomberg Finance L.P., JPM Global Markets Strategy

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

## Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); Neutral (over the duration of the price target indicated in this report, we expect this stock will perform in line with the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); and Underweight (over the duration of the price target indicated in this report, we expect this stock will underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe. NR is Not Rated. In this case, JPM has removed the rating and, if applicable, the price target, for this stock because of either a lack of a sufficient fundamental basis or for legal, regulatory or policy reasons. The previous rating and, if applicable, the price target, no longer should be relied upon. An NR designation is not a recommendation or a rating. Some stocks under coverage have a rating but no price target; in these cases, we expect the stock will outperform/perform in line/underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe of the relevant duration of the region. In our Asia (ex-Australia and ex-India) and U.K. small- and mid-cap Equity Research, each stock's expected total return is compared to the expected total return of a benchmark country market index, not to those Research Analysts' coverage universe. If it does not appear in the Important Disclosures section of this report, the certifying Research Analyst's coverage universe can be found on JPM's Research website, https://www.JPMmarkets.com.

JPM Equity Research Ratings Distribution, as of April 04, 2026

<table><tr><td></td><td>Overweight (buy)</td><td>Neutral (hold)</td><td>Underweight (sell)</td></tr><tr><td>JPM Global Equity Research Coverage*</td><td>51%</td><td>37%</td><td>12%</td></tr><tr><td>IB clients**</td><td>83%</td><td>79%</td><td>74%</td></tr><tr><td>JPMS Equity Research Coverage*</td><td>49%</td><td>39%</td><td>13%</td></tr><tr><td>IB clients**</td><td>94%</td><td>93%</td><td>85%</td></tr></table>

\*Please note that the percentages may not add to 100% because of rounding.

\*\*Percentage of subject companies within each of the "buy," "hold" and "sell" categories for which JPM has provided investment banking services within the previous 12 months.

For purposes of FINRA ratings distribution rules only, our Overweight rating falls into a buy rating category; our Neutral rating falls into a hold rating category; and our Underweight rating falls into a sell rating category. Please note that stocks with an NR designation are not included in the table above. This information is current as of the end of the most recent calendar quarter.

Equity Valuation and Risks: For valuation methodology and risks associated with covered companies or price targets for covered companies, please see the most recent company-specific research report at http://www.JPMmarkets.com, contact the primary analyst or your JPM representative, or email research.disclosure.inquiries@JPM.com. For material information about the proprietary models used, please see the Summary of Financials in company-specific research reports and the Company Tearsheets, which are available to download on the company pages of our client website, http://www.JPMmarkets.com. This report also sets out within it the material underlying assumptions used.

## History of Investment Recommendations:

A history of JPM investment recommendations disseminated during the preceding 12 months can be accessed on the Research & Commentary page of http://www.JPMmarkets.com where you can also search by analyst name, sector or financial instrument.

Analysts' Compensation: The research analysts responsible for the preparation of this report receive compensation based upon various factors, including the quality and accuracy of research, client feedback, competitive factors, and overall firm revenues.

Registration of non-US Analysts: Unless otherwise noted, the non-US analysts listed on the front of this report are employees of non-US affiliates of JPM Securities LLC, may not be registered as research analysts under FINRA rules, may not be associated persons of JPM Securities LLC, and may not be subject to FINRA Rule 2241 or 2242 restrictions on communications with covered companies, public appearances, and trading securities held by a research analyst account.

## Other Disclosures

JPM is a marketing name for investment banking businesses of JPM Chase & Co. and its subsidiaries and affiliates worldwide.

UK MIFID FICC research unbundling exemption: UK clients should refer to UK MIFID Research Unbundling exemption for details of JPM's implementation of the FICC research exemption and guidance on relevant FICC research categorisation.

All research material made available to clients are simultaneously available on our client website, JPM Markets, unless specifically permitted by relevant laws. Not all research content is redistributed, e-mailed or made available to third-party aggregators. For all research material available on a particular stock, please contact your sales representative.

Any long form nomenclature for references to China; Hong Kong; Taiwan; and Macau within this research material are Mainland China; Hong Kong SAR (China); Taiwan (China); and Macau SAR (China).

JPM may, from time to time, write on issuers or securities targeted by economic or financial sanctions imposed or administered by the governmental authorities of the U.S., EU, UK or other relevant jurisdictions (Sanctioned 

[中间内容因长度限制已省略]

dates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All

Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 19 Jun 2026 04:55 PM JST

Disseminated 19 Jun 2026 04:55 PM JST
"""
