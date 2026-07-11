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
![](images/40bf294e3d880bbaaea7e542b7467c1d4701d1026d0dd0d021feef0f080d037b.jpg)

This material is neither intended to be distributed to Mainland China investors nor to provide securities investment consultancy services within the territory of Mainland China. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM.

# Zijin Mining/Zijin Gold

## First Take: Slight miss but maintain top pick

Our First Take: Zijin Mining issued its 1H26 profit alert, with implied 2Q26 reported/core earnings of Rmb19.0bn (-5% QoQ, +45% YoY)/19.4bn (+5% QoQ, +66% YoY) coming in below JPMe (Rmb21.5bn); 1H26 reported/core earnings were Rmb39.1bn/Rmb37.9bn, representing 49%/48% of JPMe/BBGe FY26 estimates and slightly below JPMe (Rmb38.9bn), respectively. Separately, Zijin Gold's 1H26 profit alert points to implied 2Q26 earnings of \~USD590mn (-27% QoQ, +67% YoY) were a miss (JPMe: USD830mn), while 1H26 reported estimated earnings of USD1.4bn (+169% YoY) accounted for 42%/41% of JPMe/BBGe FY26 estimates. Considering the 2Q26 gold/copper prices (Rmb992/g/Rmb103k/t; -9%/+2% QoQ), we believe the miss in results of both Zijin Mining and Zijin Gold can be attributed to a lower gold price, lower-than-expected target production completion rates (<50% vs FY26 guidance for copper and gold) and more pronounced cost inflation. We maintain Zijin Mining as our top pick as we expect most of the volume ramp-up to be concentrated in 2H26.

## Key Question Marks

\- Both production volumes tracking below 50%. In 1H26, Zijin Mining reported production volumes of 47t for gold, 534kt for copper and 43kt for lithium, representing 42%/45%, 48%/45% and 35%/36% of FY JPMe/guidance, respectively. Gold and copper output was modestly below our expected 1H phasing. Lithium output was broadly in line, with Manono's contribution expected to be more visible in 2H26. Zijin Gold reported \~27t of mine-produced gold output, tracking 45%/46% of FY JPMe/guidance. In our view, slower-than-expected gold and copper volume release was one of the key drivers of the earnings miss.

\- Cost likely to be the drag. Zijin Gold's earnings miss was also largely attributable to higher-than-expected costs (i.e. diesel and royalties cost), in our view. The company has not provided detailed information on cost inflation, and we await further management guidance on the cost trajectory for the rest of 2026.

## Likely Changes to Consensus

We expect consensus earnings for Zijin Mining to remain muted while Zijin Gold could be revised down as (1) production volume tracks below 50% of company guidance; (2) commodity prices, especially the gold price, remain under pressure due to rate hike expectation changes and geopolitical uncertainty; and (3) uncertainty of production cost trajectory.

## Expected Stock Reaction

We expect a muted to negative price reaction for both Zijin Mining and Zijin Gold, with investor focus remaining on commodity price trends, US-Iran talks and interest rate decisions.

FIRST
TAKE

Asia Basic Materials

Avery Chan AC
(852) 2800-8659
avery.chan@JPM.com

Sabrina Liu
(852) 2800-8535
sabrina.liu@JPM.com

Frankie Fong
(852) 2800-8574
frankie.fong@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

601899.SS, 601899 CH

Overweight

Price (09 Jul 26): Rmb27.62

Price Target (Dec-27): Rmb46.00

2899.HK, 2899 HK

Overweight

Price (09 Jul 26): HK\$29.42

Price Target (Dec-27): HK\$50.00

2259.HK, 2259 HK

Overweight

Price (09 Jul 26): HK\$99.70

Price Target (Dec-27): HK\$170.00

See page 5 for analyst certification and important disclosures, including non-US analyst disclosures.

# Investment Thesis, Valuation and Risks

## Zijin Mining - A (Overweight; Price Target: Rmb46.00)

## Investment Thesis

We are positive on both copper and gold, which accounted for 36% and 43% of the company's gross profit in 2025, respectively. We believe tighter supply/demand should drive the next leg of the copper price rally. Zijin's good track record of mine expansion with good cost control could also support its $>10\%$ CAGR volume growth target into 2028. We rate the stock OW.

## Valuation

Our Dec-27 PT of Rmb46 is based on a DCF valuation with a WACC of 13% and a terminal growth rate of 2%. Our PT implies a FY27E P/E multiple of 13x and a FY27E EV/EBITDA multiple of 8x.

## Risks to Rating and Price Target

Downside risks include: (1) the risk of overpayment on M&A relative to eventual returns; (2) geopolitical risks surrounding Zijin's overseas mines; (3) weaker-than-expected gold and copper prices; and (4) delay or non-completion of the Allied Gold and/or Chifeng acquisitions, which would result in downside to our base case production and earnings forecasts.

Upside catalysts include: (1) stronger-than-expected gold and copper prices; and (2) stronger-than-expected volume growth, either organic or inorganic.

# Investment Thesis, Valuation and Risks

## Zijin Mining – H (Overweight; Price Target: HK\$50.00)

## Investment Thesis

We are positive on both copper and gold, which accounted for 36% and 43% of the company's gross profit in 2025, respectively. We believe tighter supply/demand should drive the next leg of the copper price rally. Zijin's good track record of mine expansion with good cost control could also support its $>10\%$ CAGR volume growth target into 2028. We rate the stock OW.

## Valuation

Our Dec-27 PT of HK\$50 is based on a 6% average 3-month A/H premium on our A-share PT. The PT implies a FY27E P/E multiple of 12x and a FY27E EV/EBITDA multiple of 7x.

## Risks to Rating and Price Target

Downside risks include: (1) the risk of overpayment on M&A relative to eventual returns; (2) geopolitical risks surrounding Zijin's overseas mines; (3) weaker-than-expected gold and copper prices; and (4) delay or non-completion of the Allied Gold and/or Chifeng acquisitions, which would result in downside to our base case production and earnings forecasts.

Upside catalysts include: (1) stronger-than-expected gold and copper prices; and (2) stronger-than-expected volume growth, either organic or inorganic.

# Investment Thesis, Valuation and Risks

## Zijin Gold International - H (Overweight; Price Target: HK\$170.00)

## Investment Thesis

Zijin Gold, a subsidiary of Zijin Mining, has established a strong growth platform through acquisitions and reserve expansion, achieving a 15% CAGR in gold production from 2023 to 2025. Operating nine mines across four continents, the company is expanding capacity at key sites. Our base case assumes the Allied Gold acquisition closes in 3Q26 and contributes from 4Q26, bringing 2026 gold production to 60t. The company expects the acquisition to add up to 25t by 2029; even without it, existing mines should deliver a 15% CAGR. Zijin Gold's disciplined acquisition strategy drives improving capital efficiency, with ROLTA reaching 29% in 2025 (vs. 12% in 2024). With a favorable gold price outlook and robust growth pipeline, we forecast earnings to grow at a 42% CAGR from 2025 to 2028. We have an OW rating and Dec-27 PT of HK\$170.

## Valuation

Our Dec-27 price target of HK\$170 is based on a DCF valuation with a WACC of 8.5% and a terminal growth rate of 2.5%. Our PT implies a FY27E P/E multiple of 13x and a FY27E EV/EBITDA multiple of 8.5x.

## Risks to Rating and Price Target

Key downside risks to our rating and price target include: 1) gold price volatility; 2) operational risks arising from exposure to multiple foreign jurisdictions, project construction delays, and illegal mining activities at the Buriticá gold mine in Colombia; 3) lower-than-expected realized prices for mineral products; and 4) delay or non-completion of the Allied Gold acquisition, which would result in downside to our base case production and earnings forecasts.

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

\- Market Maker/ Liquidity Provider: JPM is a market maker and/or liquidity provider in the financial instruments of/related to Zijin Mining - A, Zijin Mining – H, Zijin Gold International - H or related entities.

\- Market Maker/ Liquidity Provider (Hong Kong): JPM Securities (Asia Pacific) Limited and/or JPM Broking (Hong Kong) Limited and/or an affiliate is a market maker and/or liquidity provider in the securities of Zijin Mining - A, Zijin Mining – H, Zijin Gold International - H or related entities and/or warrants or options thereon, which are listed or traded on The Stock Exchange of Hong Kong Limited.

\- Beneficial Ownership (1% or more): JPM beneficially owns 1% or more of a class of common equity securities of Zijin Mining - A, Zijin Mining – H or related entities.

\- Client: JPM currently has, or had within the past 12 months, the following entity(ies) as clients: Zijin Mining - A, Zijin Mining – H, Zijin Gold International - H or related entities.

\- Client/Non-Investment Banking, Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-investment-banking, securities-related: Zijin Mining - A, Zijin Mining – H, Zijin Gold International - H or related entities.

\- Client/Non-Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-securities-related: Zijin Mining - A, Zijin Mining – H or related entities.

\- Potential Investment Banking Compensation: JPM expects to receive, or intends to seek, compensation for investment banking services in the next three months from Zijin Mining - A, Zijin Mining – H or related entities.

\- Non-Investment Banking Compensation Received: JPM has received compensation in the past 12 months for products or services other than investment banking from Zijin Mining - A, Zijin Mining – H, Zijin Gold International - H or related entities.

\- Debt Position: JPM may hold a position in the debt securities of Zijin Mining - A, Zijin Mining – H, Zijin Gold International - H or related entities, if any.

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

Zijin Mining - A (601899.SS, 601899 CH) Price Chart  
![](images/1afd97422e727d99093010fffaa5e05cd42e7959b521ce888d11413c6bfb6abf.jpg)

<table><tr><td>Date</td><td>Rating</td><td>Price (Rmb)</td><td>Price Target (Rmb)</td></tr><tr><td>20-Aug-24</td><td>OW</td><td>16.22</td><td>21</td></tr><tr><td>25-Mar-25</td><td>OW</td><td>18.05</td><td>25</td></tr><tr><td>28-Aug-25</td><td>OW</td><td>22.53</td><td>26.5</td></tr><tr><td>21-Oct-25</td><td>OW</td><td>29.75</td><td>38</td></tr><tr><td>09-Jan-26</td><td>OW</td><td>36.30</td><td>45</td></tr><tr><td>25-Mar-26</td><td>OW</td><td>32.20</td><td>50</td></tr><tr><td>09-Jul-26</td><td>OW</td><td>27.36</td><td>46</td></tr></table>

Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends. Initiated coverage Dec 03, 2014. All share prices are as of market close on the previous business day. Break in coverage Jun 15, 2023 - Aug 20, 2024.

Zijin Mining – H (2899.HK, 2899 HK) Price Chart  
![](images/73c614cdea5593ae5b1b93516959e08902e804185732685ff7f085c07189cce9.jpg)

<table><tr><td>Date</td><td>Rating</td><td>Price (HK$)</td><td>Price Target (HK$)</td></tr><tr><td>20-Aug-24</td><td>OW</td><td>16.06</td><td>20</td></tr><tr><td>25-Mar-25</td><td>OW</td><td>18.14</td><td>23.7</td></tr><tr><td>28-Aug-25</td><td>OW</td><td>24.74</td><td>28</td></tr><tr><td>21-Oct-25</td><td>OW</td><td>32.46</td><td>42</td></tr><tr><td>09-Jan-26</td><td>OW</td><td>37.20</td><td>48</td></tr><tr><td>25-Mar-26</td><td>OW</td><td>34.86</td><td>55</td></tr><tr><td>09-Jul-26</td><td>OW</td><td>29.74</td><td>50</td></tr></table>

Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends. Initiated coverage Feb 06, 2006. All share prices are as of market close on the previous business day. Break in coverage Jun 15, 2023 - Aug 20, 2024.

Zijin Gold International - H (2259.HK, 2259 HK) Price Chart  
![](images/17f802eed9182183fc92e08c46ad310393e5beb6b9abe492c07458e409156157.jpg)

<table><tr><td>Date</td><td>Rating</td><td>Price (HK$)</td><td>Price Target(HK$)</td></tr><tr><td>25-Mar-26</td><td>OW</td><td>180.10</td><td>240</td></tr><tr><td>09-Jul-26</td><td>OW</td><td>104.30</td><td>170</td></tr></table>

Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends. Initiated coverage Mar 24, 2026. All share prices are as of market close on the previous business day.

The chart(s) show JPM's continuing coverage of the stocks; the current analysts may or may not have covered it over the entire period. JPM ratings or designations: OW = Overweight, N = Neutral, UW = Underweight, NR = Not Rated

## Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); Neutral (over the duration of the price target indicated in this report, we expect this stock will perform in line with the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); and Underweight (over the duration of the price target indicated in this report, we expect this stock will underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe. NR is Not Rated. In this case, JPM has removed the rating and, if applicable, the price target, for this stock because of either a lack of a sufficient fundamental basis or for legal, regulatory or policy reasons. The previous rating and, if applicable, the price target, no longer should be relied upon. An NR designat

[中间内容因长度限制已省略]

f market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
