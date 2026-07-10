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

## Samsung Electronics

## 2Q26 headline results beat; focus on durability of earnings cycle beyond 2H26

Samsung Electronics (SEC) disclosed 2Q26 headline results above the recently revised-down consensus estimate after recognizing W15+trn worth of labor cost provisions covering the two quarters of 1H26. Given our bullish view on the near-term memory market S-D (i.e. CPU taking over LPDDR supply with demand upward revision and ongoing enterprise SSD order strength), we continue to see memory pricing in favor of suppliers and expect another leg of upward EPS revisions. The current share price (SEC shares are trading at 5.2x FTM P/E, the cheapest memory stock globally) appears to price in only a little of the structural S&D dynamic shifts (e.g., multi-year shortage, growing LTA mix, and other factors). We reiterate our bullish “longer for higher up-cycle” view on the memory industry and SEC shares, and recommend investors accumulate. The company is likely to disclose the full earnings details on July 30, Asia morning time.

\- Record-breaking results and consensus beats, albeit on a labor cost provisions. SEC's 2Q26 headline OP of W89.4trn came in above recently lowered Street estimates of W75trn-84trn and headline consensus, likely thanks to better-than-expected memory price strength and Won depreciation. On memory pricing, we believe NAND blended ASP trends (above $70\%$ Q/Q increase vs. JPMe $+53\%$ Q/Q) have been better than our expectations vs. DRAM being below our estimate of a high- $50s\%$ Q/Q increase due mainly to the product mix. We believe the overall volume sales must have been slightly better than the initial guidance if the company used some strategic inventory (more on DRAM than NAND). On the LSI/foundry side, 4nm HBM4 base-die production appears to have entered full-scale mass production supporting the top-line trends; however, we expect the overall division earnings to have widened the loss due, mainly to one-off labor cost provisions. As for the set business, it remains unclear if the MX division has turned into a loss-making one, but we believe y-y margin deterioration is accelerating with greater pressure from component price hikes.

\- Diverging operational momentum continues, with memory ASP strength to lead to further EPS upgrades from 2H26 onwards. We expect the memory-led earnings structure to continue in 2H26 (i.e. greater divergence between memory and non-memory businesses) and view the memory pricing forecast to be the most important variable that dictates the earnings outlook. As memory sufficiency remains extremely low (50-60% of procurement is only met via supply), the pricing environment is likely to remain favorable in 2H26. Yet, we are witnessing an increase in customer pushback due to substantial BOM cost pressure, and expect server-driven memory consumption trends to accelerate, implying lower volume allocation to consumer electronic customers. Between DRAM and NAND, we believe NAND pricing could surprise on the upside relative to investor expectations (20% +/- q-q increase) given U.S. hyperscalers' appetite for sourcing eSSD for KV cache offloading purposes.

Chip shortage broadening out to foundry? All eyes on Samsung Foundry's new customer order win. Following the tightening of capacity tightness at TSMC's leading edge foundry/packaging capacity, Samsung Foundry seems

## Overweight

005930.KS, 005930 KS  
Price (07 Jul 26):W299,000  
Price Target (Dec-26):W480,000

## Technology - Semiconductors

Jay Kwon AC  
(82-2) 758-5725  
jay.h.kwon@JPM.com  
JPM Securities (Far East) Limited, Seoul Branch

Sangsik Lee  
(82-2) 758 5146  
sangsik.lee@JPM.com  
JPM Securities (Far East) Limited, Seoul Branch

Neelay Y Kamath  
(91-22) 6157 3764  
neelay.kamath@jpmchase.com  
JPM India Private Limited

to be engaging with multiple new customers for AI chip projects; according to press release – Google, Anthropic, Meta, AMD, BYD, and others; for potential order discussions. This is on top of its order win for Tesla AI5/AI6 chips (note) and the Apple CIS (note) partnership. Such customer order wins could help Samsung's foundry division's utilization rate move up to the full run rate with the need for additional capacity buildout at the U.S. Taylor fab, in our view. From the recent Korea AI mega-investment master plan announcement (note), there was little information about the foundry investment roadmap. After the labor cost settlement terms, we view the fixed cost pressure on the foundry/LSI division as greater vs. the past and believe new order wins are critical for a sustainable business turnaround.

\- Investors will focus on the durability of earnings and look forward to a long-term strategy update (incl. LTA progress). Looking at SEC's FTM P/E trend in 1H26, it remained 3-6x (or 3.2x during 1Q26 and 4.8x during 2Q26) implying a peak-cycle multiple with high skepticism on the sustainability of earnings in the following year (i.e., SEC shares are still at an inflection point between de-rating and multiple normalization). Compared to 1H26, 2H26 price H-H momentum will likely be slower due to a higher base effect, and suppliers will initiate LTA discussions more actively with key customers (mainly CSP customers) amidst accelerating infrastructure investment. Provided there is an unprecedented shortage, we may see several different procurement initiatives from key customers (balancing the new server platform specs); however, none of these will be an alarm to the demand signal, and we view the memory side of the S-D equation as very healthy. We view investors as having underestimated the duration of the elongated up-cycle and remain constructive on SEC and memory stock fundamentals and risk-reward on a medium-term horizon on the recent pullback.

\- Potential next key catalysts: (1) CSP commentary on AI service business model progress and consequent hardware capex spending update; (2) AI ecosystem funding progress update (esp. CSP and AI foundation model players' capex-related funding needs); (3) memory LTA progress update (key headlines such as percentage of coverage, volume vs. pricing guarantee, and ceiling/floor price as well as target margin); and (4) memory technology commentary update (KV cache offloading related memory tiering concept specifics update heading into agents-to-agents interaction vs. memory spending optimization initiatives from software stack level). For SEC specifically, we also note a 2024A-2026E shareholder return update (how much of the 2026E FCF is returned as a split between buyback and dividend; JPMe: over W110trn total shareholder return pool) and the following 2027-2029 shareholder return update (whether SEC connects the concept of sustainable earnings to LTA and business structure changes and if it provides a more progressive stance on the total amount and duration of return) to be critical elements to the 2H26 share price outlook.

Table 1: 2Q26 preliminary earnings result comparison  
Wbn, year-end December

<table><tr><td></td><td>2Q26</td><td>1Q26</td><td>QoQ</td><td>2Q25</td><td>YoY</td><td>JPMe</td><td>vs. JPMe</td><td>BBG</td><td>vs. BBG</td></tr><tr><td>Revenue</td><td>171,000</td><td>133,873</td><td>28%</td><td>74,566</td><td>129%</td><td>171,931</td><td>-1%</td><td>176,053</td><td>-3%</td></tr><tr><td>EBIT</td><td>89,400</td><td>57,233</td><td>56%</td><td>4,676</td><td>1812%</td><td>91,458</td><td>-2%</td><td>85,932</td><td>4%</td></tr><tr><td>EBIT margin</td><td>52.3%</td><td>42.8%</td><td></td><td>6.3%</td><td></td><td>53.2%</td><td></td><td>48.8%</td><td></td></tr></table>

Source: Company data, Bloomberg Finance L.P., JPM estimates. Note: Bloomberg consensus as of 7 July 2026 (past 28 days).

Figure 1: Global memory makers' share price performance, including SOX (Philadelphia Semiconductor Index)  
![](images/840ac6d4340fbf72a4cce41113fc4989dbef4b605bf5296c46f5888ee99afd90.jpg)  
Source: Bloomberg Finance L.P. Note: Past performance is not an indication of future results.

# Investment Thesis, Valuation and Risks

Samsung Electronics (Overweight; Price Target: W480,000)

## Investment Thesis

We are OW on SEC given the profit growth cycle is reaccelerating due to improving legacy fundamentals. Although our view on SEC's HBM business execution remains conservative, given the lack of evidence of its regaining its technology moat (1cnm), we believe its improving HBM qualification progress tactically bodes well for its near- to mid-term share price trajectory amid a positive industry setup. In order for SEC's shares to be fundamentally even more appealing, we believe increasing evidence of its technology leadership is required to restore investor confidence.

## Valuation

Our Dec-26 PT of W480K based on a mid-cycle P/E valuation: 8x FY26E-27E P/E (vs. 6x down-cycle and 10x up-cycle).

## Risks to Rating and Price Target

Downside risks to our rating and price target include: (1) an elongated memory price downcycle; (2) weaker-than-expected HBM demand from ASIC customers in FY25-26E; (3) delayed HBM qualification for future product generations; and (4) slower-than-expected mobile unit growth.

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

\- Market Maker/ Liquidity Provider: JPM is a market maker and/or liquidity provider in the financial instruments of/related to Samsung Electronics or related entities.

\- Manager or Co-manager: JPM acted as manager or co-manager in a public offering of securities or financial instruments (as such term is defined in Directive 2014/65/EU) of/for Samsung Electronics or related entities within the past 12 months.

\- Beneficial Ownership (1% or more): JPM beneficially owns 1% or more of a class of common equity securities of Samsung Electronics or related entities.

\- Client: JPM currently has, or had within the past 12 months, the following entity(ies) as clients: Samsung Electronics or related entities.

\- Client/Investment Banking: JPM currently has, or had within the past 12 months, the following entity(ies) as investment banking clients: Samsung Electronics or related entities.

\- Client/Non-Investment Banking, Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-investment-banking, securities-related: Samsung Electronics or related entities.

\- Client/Non-Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-securities-related: Samsung Electronics or related entities.

\- Investment Banking Compensation Received: JPM has received in the past 12 months compensation for investment banking services from Samsung Electronics or related entities.

\- Potential Investment Banking Compensation: JPM expects to receive, or intends to seek, compensation for investment banking services in the next three months from Samsung Electronics or related entities.

• Non-Investment Banking Compensation Received: JPM has received compensation in the past 12 months for products or services other than investment banking from Samsung Electronics or related entities.

\- Debt Position: JPM may hold a position in the debt securities of Samsung Electronics or related entities, if any.

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

Samsung Electronics (005930.KS, 005930 KS) Price Chart  
![](images/e63b09c8e0c67b476268634c812e1cdd8cd1253fc0fe71490c250daceca39bc8.jpg)  
Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends. Initiated coverage Oct 09, 2011. All share prices are as of market close on the previous business day.

<table><tr><td>Date</td><td>Rating</td><td>Price (W)</td><td>Price Target (W)</td></tr><tr><td>01-Feb-24</td><td>OW</td><td>72700</td><td>95,000</td></tr><tr><td>03-Apr-24</td><td>OW</td><td>85000</td><td>110,000</td></tr><tr><td>03-Jul-24</td><td>OW</td><td>81800</td><td>120,000</td></tr><tr><td>08-Sep-24</td><td>OW</td><td>68900</td><td>100,000</td></tr><tr><td>08-Oct-24</td><td>OW</td><td>61000</td><td>84,000</td></tr><tr><td>31-Oct-24</td><td>OW</td><td>59100</td><td>83,000</td></tr><tr><td>10-Dec-24</td><td>N</td><td>53400</td><td>60,000</td></tr><tr><td>03-Apr-25</td><td>OW</td><td>58800</td><td>74,000</td></tr><tr><td>30-Apr-25</td><td>OW</td><td>55800</td><td>68,000</td></tr><tr><td>02-Jul-25</td><td>OW</td><td>60200</td><td>71,000</td></tr><tr><td>01-Aug-25</td><td>OW</td><td>71400</td><td>84,000</td></tr><tr><td>25-Sep-25</td><td>OW</td><td>85400</td><td>100,000</td></tr><tr><td>27-Oct-25</td><td>OW</td><td>98900</td><td>135,000</td></tr><tr><td>30-Oct-25</td><td>OW</td><td>101700</td><td>140,000</td></tr><tr><td>14-Dec-25</td><td>OW</td><td>108500</td><td>160,000</td></tr><tr><td>16-Jan-26</td><td>OW</td><td>145000</td><td>200,000</td></tr><tr><td>29-Jan-26</td><td>OW</td><td>164300</td><td>240,000</td></tr><tr><td>22-Mar-26</td><td>OW</td><td>199800</td><td>300,000</td></tr><tr><td>30-Apr-26</td><td>OW</td><td>226500</td><td>350,000</td></tr><tr><td>17-May-26</td><td>OW</td><td>273500</td><td>480,000</td></tr></table>

The chart(s) show JPM's continuing coverage of the stocks; the current analysts may or may not have covered it over the entire period. JPM ratings or designations: OW = Overweight, N = Neutral, UW = Underweight, NR = Not Rated

## Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); Neutral (over the duration of the price target indicated in this report, we expect this stock will perform in line with the average total return of the stocks in the Research Analyst's, or the 

[中间内容因长度限制已省略]

cements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or

Completed 07 Jul 2026 03:02 PM HKT
"""
