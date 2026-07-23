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

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); Neutral (over the duration of the price target indicated in this report, we expect this stock will perform in line with the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); and Underweight (over the duration of the price target indicated in this report, we expect this stock will underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe. NR is Not Rated. In this case, JPM has removed the rating and, if applicable, the price target, for this stock because of either a lack of a sufficient fundamental basis 

[中间内容因长度限制已省略]

ent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All

Completed 21 Jul 2026 10:54 PM JST
"""
