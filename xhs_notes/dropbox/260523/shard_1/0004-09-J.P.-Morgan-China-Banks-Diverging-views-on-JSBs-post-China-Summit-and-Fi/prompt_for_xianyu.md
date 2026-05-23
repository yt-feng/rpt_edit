你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  ✅ 三大情景框架：DCF、P/ARR、EV/Sales
  ✅ 关键变量分析
  ✅ 估值逻辑、假设、终值占比等核心内容覆盖
  ✅ 适合准备 AI 相关面试、研究 AI 估值的同学
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
This material is neither intended to be distributed to Mainland China investors nor to provide securities investment consultancy services within the territory of Mainland China. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM.

# China Banks

# Diverging views on JSBs post China Summit and Financial Tour

We met with four joint-stock banks during our recent Financial Tour and the JPM Global China Summit. The meetings confirmed the prevailing industry trends on weak loan demand (particularly in retail), a recovering NIM trajectory, stable fee income growth, and a continuing drag from retail asset quality. At the individual bank level, however, our views are mixed. We turn more positive on SPDB (OW): the bank guided for high-single-digit profit growth in FY26, implying a meaningful acceleration from the modest +1% y/y recorded in 1Q26. Takeaways from PAB and Citic meetings are more neutral, as Citic guidance remains largely unchanged from earlier in the year. PAB reiterated its profit turnaround, but highlighted headwinds on investment income growth on base effects. Takeaways from our meeting with Minsheng are more negative, as management indicated they are still in the early stages of recognizing retail asset quality deterioration and expect subdued profit growth given persistently high retail NPL formation and low NPL coverage.

# Loan demand and growth

- Weak loan demand, particularly on retail segment: April loan contraction in the system is partly due to seasonality. One bank commented that the PBOC hosted meetings with banks in April but did not give hard quota or loan growth targets; instead, the focus was on smoothing the pace of loan growth. In general, retail demand has been weak. For mortgages, banks we spoke with believe the use of provident fund is not the reason for weak mortgages, despite recovery in transaction volume; rather, there could be a rise in downpayment (cash payment).   
- At an individual bank level, Citic is more confident on achieving its loan growth target for the full year, mainly supported by corporate loans. New corporate loans reached \~RMB230bn in 1Q26 (some pipeline was pulled forward from 4Q25), with strength concentrated in the Greater Bay Area and Yangtze River regions. SPDB said the new loan amount is targeted to be \~RMB300bn in 2026, vs \~RMB320bn in 2025, implying slowing loan growth (from 5.8% in 2025 to 5.3% in 2026). SPDB wants to be more balanced between corporate and retail but actual results depend on demand. Minsheng saw corporate loan demand exceed expectations in 1Q26, but April saw some retreat in loan growth and May remains weak. Retail loans have been contracting across all lines since mid-2025, including mortgages in 2026. PAB achieved positive retail loan growth in 1Q26 (one of the few in the industry), but overall loan growth is under pressure, with a full-year expectation of only low-single-digit growth, while the structure is “corporate-led, retail-supplementary”.

# NIM

\- Banks are in general more optimistic on NIM trends: Citic guided for NIM to be largely flattish q/q for the remainder of 2026. On a full-year basis, NIM contraction is likely to be 3-5bps in 2026 (vs -13bps in 2025). SPDB saw NIM

# Banks & Financial Services

Katherine Lei AC

(852) 2800-8552

katherine.lei@JPM.com

JPM Securities (Asia Pacific) Limited/

JPM Broking (Hong Kong) Limited

# Peter Zhang

(852) 2800-8557

peter.zhang@JPM.com

JPM Securities (Asia Pacific) Limited/

JPM Broking (Hong Kong) Limited

# Lincoln Yu

(852) 2800 8523

lincoln.yu@JPM.com

JPM Securities (Asia Pacific) Limited/

JPM Broking (Hong Kong) Limited

# Haomin Chen

(86-21) 6106 6347

haomin.chen@JPM.com

SAC Registration Number: S1730524080002

JPM Securities (China) Company

Limited

improve +2bps q/q to 1.44% in 1Q26 (from 1.42% in 4Q25) and aims to maintain stable or mildly improving NIM y/y in FY26. Minsheng expects NIM to rebound y/y in 2026, even under the scenario of one symmetrical rate cut. PAB expects a low-single-digit bps contraction in NIM in 2026. The bank is focused on structural optimization (more loans, less bills).

# Non-NII

\- Most remain optimistic on fees: Citic is confident fee growth will be better this year, driven by wealth business (WMP distribution, custody). SPDB targets positive fee income growth in FY26. The growth will likely be driven by wealth (wealth management +12-14% y/y in 2025), while the competition is still intense. DCM drag is easing on base effects, but bank card fees remain a headwind. Minsheng expects fee income to be “stable and improving”, driven by wealth, settlement, and custodian fees. PAB saw strong 1Q fee growth driven by bancassurance, and is optimistic on wealth management recovery as it rebuilds its retail team and product shelf. But PAB also commented on lower investment income due to a high base in 2Q25 and 3Q25 (when the bond market was strong), which will pressure revenue growth in the middle quarters.

# Asset quality and provisions

\- Retail asset quality remains a drag, while NPL formation trends diverge: Banks in general commented that retail asset quality remains a drag, attributing this to the weak macro conditions. At an individual bank level, comments on NPL formation trends varied, with PAB and SPDB guiding NPL formation trending down, Citic bank guiding flattish credit costs, while Minsheng commented it is still in the early stages of recognizing retail asset quality deterioration.

\- Citic: Mortgage NPL formation is declining; however, personal business loans, credit cards, and consumption loans continue to see pressure. CRE NPL formation ratio is declining. Credit cost is expected to be similar to prior years, with pressure concentrated in retail.

\- PAB: The NPL ratio is stable, with NPL formation rate significantly improved, leading to lower write-off pressure and declining credit costs. The full-year NPL coverage ratio is expected to decline \~20ppts (after -30ppts in 2025, with 200% as the floor). Credit card remains the primary risk concern. It is targeting a virtuous cycle of “lower NPL formation → less write-off → lower provisioning → profit accretion”. Internet loans (\~RMB100bn, 4-5% of total) have manageable risk.

\- SPDB: Overall NPL formation will decline y/y, likely leading to lower impairment charges. The coverage ratio, $>200\%$ in 1Q26, will be stable or mildly increase. Credit costs are on an improving trend. Off-BS WMP fully brought on-BS and over-provisioned by end-2025; confident that asset quality clearing has concluded. AQ is at the best level of the past 10 years. Retail NPLs are concentrated in mortgages and credit cards; credit card NPL formation dropped notably and is stabilizing; mortgage NPL formation has peaked but is still at a high level.

\- Minsheng: Has no confidence to call an inflection point in retail AQ. Credit card is the key concern (NPL formation still high with no clear improvement).

Personal business loan NPL formation rebounded in 1Q26 but is not above the 2025 peaks. Mortgage AQ is showing some improvement. Impairment charges are expected to be slightly higher than in 2025 (mainly due to retail). NPL coverage is only \~140%, and management prioritizes rebuilding coverage to 150%. Corporate NPLs (including CRE) are being managed through scheduled write-offs; no further large-scale problematic loan recognition expected in CRE (RMB20bn in 2024 vs RMB15bn in 2025).

# Revenue and profits

- Diverging guidance on profits growth: On the positive side, SPDB guided for high-single-digit profit growth in FY26, implying a meaningful acceleration from the modest +1% y/y recorded in 1Q26. PAB and Citic are largely in line with expectations, as their guidance remains mostly unchanged from earlier in the year. On the negative side, Minsheng expects subdued profit growth given persistently high retail NPL formation and low NPL coverage.   
- SPDB: Expects low-single-digit growth for revenue, high-single-digit growth for profits. 1Q26 profit growth was only 1% due to the high base in 1Q25 (which contributed 35% of FY25 profits); it has been deliberately reducing the 1Q profit contribution to full year. It targets ROE of 7% in 2026 (up from 6.7% in 2025). CIR to decline to \~26% in 2026 from 28.5% in 2025.   
- Minsheng: Impairment is a drag on profits growth. Management disclosed that Minsheng will focus on building the provision and expects there to be no ROE rebound before provision coverage reaches 150%.   
- PAB: The full-year revenue target is “relatively stable”, with low-single-digit percentage profit growth. 2Q-3Q revenue growth will face pressure as the investment income base normalizes. CET1 at 9.5%, ROE \~9%, no external capital needs; payout ratio at 27% with no plan to exceed 30% near-term.   
- Citic: Management has set a 5/3/3 growth target earlier this year (i.e. assets, revenues and profits to achieve 5%/3%/3% growth, respectively, in 2026). Management said they will keep this target unchanged in 1H and may review it in 2H.

Companies Discussed in This Report (all prices in this report as of market close on 20 May 2026, unless otherwise indicated)

Shanghai Pudong Development Bank - A(600000.SS/Rmb8.94/OW)

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

# Important Disclosures

- Market Maker/ Liquidity Provider: JPM is a market maker and/or liquidity provider in the financial instruments of/related to Shanghai Pudong Development Bank - A or related entities.   
- Manager or Co-manager: JPM acted as manager or co-manager in a public offering of securities or financial instruments (as such term is defined in Directive 2014/65/EU) of/for Shanghai Pudong Development Bank - A or related entities within the past 12 months.   
- Client: JPM currently has, or had within the past 12 months, the following entity(ies) as clients: Shanghai Pudong Development Bank - A or related entities.   
- Client/Investment Banking: JPM currently has, or had within the past 12 months, the following entity(ies) as investment banking clients: Shanghai Pudong Development Bank - A or related entities.   
- Client/Non-Investment Banking, Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-investment-banking, securities-related: Shanghai Pudong Development Bank - A or related entities.   
- Client/Non-Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-securities-related: Shanghai Pudong Development Bank - A or related entities.   
- Investment Banking Compensation Received: JPM has received in the past 12 months compensation for investment banking services from Shanghai Pudong Development Bank - A or related entities.   
- Potential Investment Banking Compensation: JPM expects to receive, or intends to seek, compensation for investment banking services in the next three months from Shanghai Pudong Development Bank - A or related entities.   
- Non-Investment Banking Compensation Received: JPM has received compensation in the past 12 months for products or services other than investment banking from Shanghai Pudong Development Bank - A or related entities.   
- Debt Position: JPM may hold a position in the debt securities of Shanghai Pudong Development Bank - A or related entities, if any.

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

Shanghai Pudong Development Bank - A (600000.SS, 600000 CH) Price Chart 20   
![](images/be77eb141b280c951da21451dfd663b8ec93db1bc2f519aff3e322c05116dfde.jpg)

<details>
<summary>line</summary>

| Date       | Price(Rmb) |
| ---------- | ---------- |
| Sep 23     | N Rmb6.5   |
| Jan 24     | N Rmb6.3   |
| May 24     | UW Rmb5.8  |
| Sep 24     | N Rmb8     |
| Sep 24     | OW Rmb10.2 |
| Jan 25     | OW Rmb11.1 |
| May 25     | OW Rmb12    |
| May 25     | OW Rmb13    |
| Sep 25     | OW Rmb13.7  |
| Sep 25     | OW Rmb16.2  |
| Jan 26     | OW Rmb15.7  |
| Jan 26     | OW Rmb14.6  |
| May 26     | OW Rmb13.9  |
</details>

<table><tr><td>Date</td><td>Rating</td><td>Price (Rmb)</td><td>Price Target (Rmb)</td></tr><tr><td>26-Jul-23</td><td>N</td><td>7.27</td><td>6.5</td></tr><tr><td>13-Oct-23</td><td>N</td><td>7.14</td><td>6.3</td></tr><tr><td>01-Nov-23</td><td>UW</td><td>6.82</td><td>5.5</td></tr><tr><td>05-Mar-24</td><td>UW</td><td>7.07</td><td>5.8</td></tr><tr><td>01-May-24</td><td>N</td><td>7.70</td><td>8</td></tr><tr><td>02-Aug-24</td><td>OW</td><td>8.57</td><td>10.2</td></tr><tr><td>16-Oct-24</td><td>OW</td><td>10.25</td><td>11.1</td></tr><tr><td>08-Jan-25</td><td>OW</td><td>10.27</td><td>12</td></tr><tr><td>18-Apr-25</td><td>OW</td><td>10.75</td><td>13</td></tr><tr><td>09-Jun-25</td><td>OW</td><td>12.32</td><td>13.7</td></tr><tr><td>08-Aug-25</td><td>OW</td><td>13.93</td><td>16.2</td></tr><tr><td>24-Oct-25</td><td>OW</td><td>12.97</td><td>15.7</td></tr><tr><td>19-Jan-26</td><td>OW</td><td>11.04</td><td>14.6</td></tr><tr><td>22-Apr-26</td><td>OW</td><td>9.72</td><td>13.9</td></tr></table>

Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends.   
Initiated coverage Mar 19, 2013. All share prices are as of market close on the previous business day.

The chart(s) show JPM's continuing coverage of the stocks; the current analysts may or may not have covered it over the entire period.

JPM ratings or designations: OW = Overweight, N = Neutral, UW = Underweight, NR = Not Rated

# Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage unive

[中间内容因长度限制已省略]

f market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own

independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
