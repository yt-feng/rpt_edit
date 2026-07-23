你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
# JPM

## Japan Quant Strategy

## NKY rallies – Sign that worst is over? AI semiconductors a long way off from recapturing their leading role

## Putting the brakes on one-sided pessimism

The Nikkei Average rebounded sharply to 66,000 today (July 21). The market continued to show weakness over the latter half of last week, particularly in AI semiconductor-related stocks, and investor sentiment had become even more cautious. However, the recent pullback was not accompanied by a downward revision in earnings expectations but rather appears to have been largely influenced by a shift in the AI-related narrative and position adjustments by momentum traders.

Given that Japanese stock sentiment has fallen to around zero and the TOPIX's NTM EPS has not collapsed, additional factors are becoming necessary for pessimism to spread further. Meanwhile, sentiment toward South Korean stocks continues to deteriorate significantly. Japanese stocks, mainly memory semiconductor stocks, are still susceptible to global AI-related narratives. While earnings momentum specific to Japanese stocks is firm, the sustainability of market rebounds remains highly dependent on external conditions at this stage.

## Will CTA stop-loss selling fail to spread?

Last week, CTAs triggered stop-loss selling of Nikkei futures, intensifying beta-selling pressure via the futures market. However, with a rebound in AI-semiconductor-related stocks, Nikkei 225 futures recovered to the 66,000 level today. It appears that CTA stop-loss selling has temporarily stopped. If the index falls below 64,600 again, there remains a risk that CTA position unwinding could resume. However, we believe that the considerable portion of the long positions CTAs have built up since May has already been unwound.

As for KOSPI 200 futures, stop-loss selling was triggered when the index fell below 1,100, but we believe the long positions accumulated since March have been largely unwound. Barring any additional shocks that could trigger another sharp decline in the Nikkei Average or the KOSPI 200, the pressure to sell futures, starting with CTAs, is now passing its worst-case scenario.

## Global Quantitative and Derivatives Strategy

Masanari Takada AC (81-3) 6736-8636 masanari.takada@JPM.com JPM Securities Japan Co., Ltd.

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

Figure 1: Japanese stock sentiment and NTM EPS rate of change – Nervous sentiment continues, but earnings expectations remain intact  
![](images/76f1c554e26b606a192f271328dfa32e2a67ff112014d825de29edb52e71e7c8.jpg)  
Source: Bloomberg Finance L.P., JPM Global Markets Strategy

Figure 2: Japanese stock sentiment and South Korean stock sentiment – Is there any ongoing instability in semiconductor stocks during Asian trading hours?  
![](images/4bf76e6b2185e33f9c70f66174e11756a7643ef63ff8119f23cacbea1fa869e8.jpg)  
Source: Bloomberg Finance L.P., JPM Global Markets Strategy

Figure 3: CTA's Nikkei futures positions – After briefly dipping into the 64,000 range, the NKY rebounded on its own and recovered to the 66,000 level  
![](images/1559db2e88fb7de6b5c49cf8580a2f46ce0febfd299fa60457c79c0e8f9241ff.jpg)  
Source: Bloomberg Finance L.P., JPM Global Markets Strategy

Figure 4: CTA's KOSPI 200 futures position – Focus is on whether it can recover to 1,100, but will CTAs' forced unwinding take a breather?  
![](images/1a2be8012776e5d477243b02b1a686310b5f8af7797a6834f2770a3f563d529a.jpg)  
Source: Bloomberg Finance L.P., JPM Global Markets Strategy

## High Beta/High Momentum buyback pressure is still limited

That said, futures were not the main drivers of July's sell-off. In the cash equity market, the decline was particularly pronounced among High-Beta/High-Momentum stocks, especially those in the semiconductor and AI infrastructure-related sectors. Looking at the L/S performance of High Momentum/High Beta and Low Momentum/Low Beta strategies in Japan and South Korea, we are currently seeing signs of a potential bottoming out. On the other hand, the recovery in excess returns for the “High Momentum/High Beta” strategy relative to the market has been slow. This shows that while short covering on the Low Beta/Low Momentum side is nearing completion, the movement to actively buy back the sold-off High Beta/High Momentum stocks has yet to gain momentum. The market appears to have begun to expect a pause in the sell-off (AI-related), but ahead of key earnings reports from major global AI-related companies it remains in a wait-and-see mode before it can shift to a bullish stance.

Figure 5: Japanese & South Korean stocks – High Momentum/High Beta vs. Low Momentum /Low Beta L/S performance

Universe consists of the TOPIX 500 and the KOSPI 200. At the end of each month, the top and bottom 30% of stocks by stock price return (12-month vs. 1-month) and beta are selected.

![](images/fa18fa6edb65f3790f2bf3fd1b7e0b34f887241290757cdc21b11343479e26d5.jpg)  
Source: Bloomberg Finance L.P., JPM Global Markets Strategy  
Figure 6: Japanese & South Korean stocks – High Momentum/High Beta vs. market excess returns

Universe consists of the TOPIX 500 and the KOSPI 200. At the end of each month, the top and bottom 30% of stocks by stock price return (12-month vs. 1-month) and beta are selected. Excess returns relative to each market index are shown.

![](images/54ff055af63c113663d4eeea07c8d96f75ca8c0575afefc57a703144d9f721f0.jpg)  
Source: Bloomberg Finance L.P., JPM Global Markets Strategy

Therefore, the current focus is on the extent of restoration of Old Winners (defined as High Beta/High Momentum stocks as measured at the end of June) that suffered a significant decline in June. Looking at cumulative excess returns for July, both the Old Winners overall and the “June-hit Old Winners” (i.e., those Old Winners whose drawdowns widened and momentum collapsed in June) have rebounded from their lows around July 17. However, the “June-hit Old Winners” are still underperforming the Old Winners as a whole, so we cannot conclude that the group of stocks that was heavily sold off in June has regained their leading role. While a technical rebound is evident, there still appears to be some way to go before the market returns to the buying interest seen before the correction.

Figure 7: Performance details of the expanded High Momentum/High Beta stock group that has begun to lose momentum - 1/1

Universe uses the TOPIX 500. As of the end of June, we extracted stocks with the highest stock returns (12-month - 1-month basis) and high beta. We used the intersection of the top 30% of stocks meeting each criterion. We defined this group as “Old Winners,” and further defined the top 50% of stocks in this group that experienced the largest declines from their June peak through June 30 as “June Hit, Old Winners.”

TOPIX500 July 2026: Old Winners Reversal  
![](images/48bbd222a2accc2c4cd85f885c95af7dda325d2de1b62e47873a4a422e56738e.jpg)  
Source: Bloomberg Finance L.P., JPM Global Markets Strategy

![](images/bae530ff43b7cd85f78c15e944235209d3e7a6bbe8a7ac6c8455dbefb2a8ab93.jpg)

This June-hit stock group (= the top 50% of the drawdowns) remains weak compared with the stocks with smaller drawdowns in June (= less than 50%, June-resilient). In particular, the group of “high chip sensitivity” stocks, which are highly sensitive to AI (i.e., have a high SOX beta), continues to lag significantly behind the group of stocks with low sensitivity. Although there are signs that the market has bottomed out, it is still difficult to say that stocks with strong ties to semiconductors and AI have returned to their role as market drivers. The recovery of the “Old Winners” that faltered in June appears to have begun, but it may still be one step away from confirming a bottom.

## Figure 8: Performance details of the expanded High Momentum/High Beta stock group that has begun to lose momentum - 2/2

The figure on the left shows the performance of the “Old Winners” overall, divided into two groups: the half with the largest price declines in June (“June-hit”) and the half with the smallest declines (“June-resilient”). The figure on the right further divides the “June-hit” group into high and low categories based on residual SOX beta, namely SOX sensitivity after adjusting for TOPIX beta. Stocks with “High Chip Sensitivity” are considered to be “June-hit” stocks with strong ties to semiconductors and AI.

TOPIX500 July 2026: What Broke Inside Old Winners  
![](images/d3ae6866e8fee7875e1874c3d1627c25483d83f420aee438e01218d36d05f148.jpg)

![](images/36b7d01f5f727ee0d3e6dbcb9e895cadad9775e00a0327d655fdd7150543dfef.jpg)  
Source: Bloomberg Finance L.P., JPM Global Markets Strategy

## Expanding the scope of stock selection in the AI-semiconductor sector

To provide additional context regarding the group of “June-hit” stocks mentioned earlier, which are highly sensitive to semiconductor and AI trends, we believe their weakness is running its course. However, there is still not enough evidence to confirm a strong reversal. The percentage of stocks trading above the previous day’s closing price rose significantly through July 21, indicating that short-term buying is no longer limited to just a few stocks. On the other hand, the share of stocks that outperformed the TOPIX 500 over the past five days remains low, and the breadth of outperformance relative to the market on a day-to-day basis is still limited. At present, the main change is the receding of downside concerns, and it seems that it will take additional days to transition to a full-fledged outperforming phase.

There is also improvement in selling pressure. The percentage of stocks hitting new intraday lows jumped sharply in mid-July but has since declined, indicating a decrease in the number of stocks hitting new lows. However, the number of stocks supporting the recovery of the entire basket remains limited. Looking at the cumulative returns of the equally-weighted basket, key stocks such as Ibiden (4062.JT), Kioxia (285A.JT), and Yaskawa Electric (6506.JT) continue to weigh on the index. Although selling pressure is gradually peaking out, the group of stocks leading the rebound remains small. In order for High Beta/High Momentum stocks to return to center stage, there needs to be a clear broadening of investor interest among the oversold stocks from this point forward.

Figure 9: Performance details of AI-Sensitive Stock Groups - 1/2

The analysis focuses on the group of stocks within the TOPIX 500 with high residual SOX beta (see Figure 8). In other words, the basket of High Beta/High Momentum stocks, which have experienced notable drawdowns since June, that exhibit high sensitivity to AI. Rebound Breadth is calculated on the 1-hour chart and represents the percentage of stocks in the sample that are trading above the previous day's closing price. A figure exceeding $50\%$ indicates that more than half of the stocks rebounded compared to the previous day. 5-Day Breadth is the percentage of stocks in the sample whose returns over the past five days have outperformed the TOPIX 500. A figure exceeding $50\%$ indicates that the basket as a whole is broadly outperforming the TOPIX.

TOPIX500 July 2026: Rebound Breadth  
![](images/e60117dddf4d6746df2985c387734451cf7fbd46af7d3cd48d0bc5b0e35a70fb.jpg)  
Source: Bloomberg Finance L.P., JPM Global Markets Strategy

![](images/3734384467376f105fdca465a5e697e0a9e952ba570b69a4477700d8dda6d19f.jpg)  
Figure 10: Performance details for the group of stocks with high AI sensitivity - 2/2

The analysis focuses on the group of stocks within the TOPIX 500 with high residual SOX beta (see Figure 8). In other words, the basket of High Beta/High Momentum stocks, which have experienced notable drawdowns since June, that exhibit high sensitivity to AI. Selling Pressure is the percentage of the target stocks that have a new low price in Japan and China at that time. A lower value suggests that selling pressure may be easing. Top 3 / Bottom 3 Stock Contribution refers to the contributions of the top three and bottom three stocks, respectively, to the cumulative return of the target basket, weighted equally.

TOPIX500 July 2026: Selling Pressure and Stock Impact  
![](images/953ea9c8a342c2323b700a95cf85cf1292f5e50a208245c71cb841766da88b5b.jpg)  
Source: Bloomberg Finance L.P., JPM Global Markets Strategy

![](images/61da74fb1fb7a8f2f4110d2243129d6efe9c68e84cc06631edc8087da98047ba.jpg)

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

## Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); Neutral (over the duration of the price target indicated in this report, we expect this stock will perform in line with the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); and Underweight (over the duration of the price target indicated in this report, we expect this stock will underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe. NR is Not Rated. In this case, JPM has removed the rating and, if applicable, the price target, for this stock because of either a lack of a sufficient fundamental basis or for legal, regulatory or policy reasons. The previous rating and, if applicable, the price target, no longer should be relied upon. An NR designation is not a recommendation or a rating. Some stocks under coverage have a rating but no price target; in these cases, we expect the stock will outperform/perform in line/underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe of the relevant duration of the region. In our Asia (ex-Australia and ex-India) and U.K. small- and mid-cap Equity Research, each stock's expected total return is compared to the expected total return of a benchmark country market index, not to those Research Analysts' coverage universe. If it does not appear in the Important Disclosures section of this report, the certifying Research Analyst's coverage universe can be found on JPM's Research website, https://www.JPMmarkets.com.

JPM Equity Research Ratings Distribution, as of July 04, 2026

<table><tr><td></td><td>Overweight (buy)</td><td>Neutral (hold)</td><td>Underweight (sell)</td></tr><tr><td>JPM Global Equity Research Coverage*</td><td>53%</td><td>36%</td><td>12%</td></tr><tr><td>IB clients**</td><td>83%</td><td>80%</td><td>73%</td></tr><tr><td>JPMS Equity Research Coverage*</td><td>51%</td><td>37%</td><td>12%</td></tr><tr><td>IB clients**</td><td>95%</td><td>92%</td><td>87%</td></tr></table>

\*Please note that the percentages may not add to 100% because of rounding.

\*\*Percentage of subject companies within each of the "buy," "hold" and "sell" categories for which JPM has provided investment banking services within the previous 12 months.

For purposes of FINRA ratings distribution rules only, our Overweight rating falls into a buy rating category; our Neutral rating falls into a hold rating category; and our Underweight rating falls into a sell rating category. Please note that stocks with an NR designation are not included in the table above. This information is current as of the end of the most recent calendar quarter.

Equity Valuation and Risks: For valuation methodology and risks associated with covered companies or price targets for covered companies, please see the most recent company-specific research report at http://www.JPMmarkets.com, contact the primary analyst or your JPM representative, or email research.disclosure.inquiries@JPM.com. For material information about the proprietary models used, please see the Summary of Financials in company-specific research reports and the Company Tearsheets, which are available to download on the company pages of our client website, 

[中间内容因长度限制已省略]

ny loss arising from any use of this material or its contents, and neither JPM nor any of its respective directors, officers or employees, shall be in any way responsible for the contents hereof, apart from the liabilities and responsibilities that may be imposed on them by the relevant regulatory authority in the jurisdiction in question, or the regulatory regime thereunder. Opinions, forecasts or projections contained in this material represent JPM's current opinions or judgment as of the date of the material only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All

Completed 21 Jul 2026 10:54 PM JST
"""
