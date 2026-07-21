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
LONGFOR GROUP (0960.HK)

# 1H26 Preview: DP margin weakness persists despite IP growth and on-track deleveraging; Neutral

We update our estimates to reflect 1) substantial underperformance of contract sales in 1H26 (-53% yoy vs. average mid-teens % yoy decline by coverage DPs and top-100 developers), likely caused by adverse saleable setup and nearly-muted landbank replenishment. We therefore lower our 2026E contract sales target by 28% to Rmb26bn, implying -42% yoy and 35% sell-through (refreshing historical low) to be achieved against the Rmb105bn saleables budgeted for 2026, and lower 27E-28E contract sales by average 27%. We correspondingly lower the DP topline by average 14% across 26E-28E; 2) we cut 2026E GPM to -16%, seeing limited recovery room from the 2H25 trough due to persistent pricing pressure for non-core markets and “aged inventory” (\~80% of Longfor’s saleable resources by 2025). We likewise expanded JV loss to reflect similarly exacerbating profitability pressure; 3) we also lowered PM and related services growth to 2% p.a. for 2026E-28E (vs. prior 7%), reflecting weakened delivery volume outlook and more competitive third-party biddings (increasingly dominated by SOE PMs). As result, we lower our bottomline estimates to Rmb2.4bn net loss in 2026E (vs. prior Rmb471mn net loss), and expect Rmb1.1bn/2.2bn net profits for 2027E-28E (vs. prior Rmb2.2bn/3.3bn). Our revised topline is 11% below Datastream consensus, while our core earnings forecast is substantially lower than consensus (vs. positive profits in 2026E per consensus and average \~60% lower than consensus for 2027E-28E) mainly on less constructive outlook on DP profitability. We lower our 12-month NAV-based target price by 14% to HK\$7.5 (still at a 25% NAV discount). Maintain Neutral.

1H operating data still under pressure: 1) DP: Longfor's 1H26 contract sales declined 53% yoy to Rmb17bn (vs. Rmb100bn budgeted for the whole year), below coverage average of down 15%. In addition, we note Longfor's 1H26 land investment remained muted, vs. our tracked SOE developers' spent average mid-tweenties % of their contract sales in landbanking. Given the deleveraging plan, vintage inventory stock and prolonged property market downcycle, we expect Longfor to unlikely resume land acquisition until late next year. 2) Rental income: rental income grew 4% yoy in 1H26, vs. peer CR Land +13% and Seazen +2% yoy, likely dragged by low-occupancy and unfavorable rent reversion of Longfor's long-term rental apartment assets, while we expect rental income from Longfor's malls could be growing at HSD% level on the back of enhanced operation and post-renovation SSSG recovery.

Yi Wang, CFA
+86(21)2401-8930 |
yi.wang@goldmansachs.cn
GS (China) Securities
Company Limited

Shi Xu
+86(21)2401-8929 |
shi.x.xu@goldmansachs.cn
GS (China) Securities
Company Limited

Kaiyan Jing
+86(21)2411-8092 |
kaiyan.jing@goldmansachs.cn
GS (China) Securities
Company Limited

Our view on 1H26: we expect minor core net loss in 1H26, reflecting (-) double-digit DP topline contraction yoy, aligning with the broader industry trend and approx. 2pp-3pp yoy DP GPM decline from FY25 level given continued property price weakness of vintage inventories, especially those located outside top-tier cities, which might be largely buffered by (+) LSD% topline and profit growth of non-DP segments, mainly supported by mall income ramp-up, though we expect growth of long-term rental apartment and property service legs might be overshadowed by macro adversities and intensified scale expansion competition. Furthermore, we expect the company's debt reduction pace to be on track of achieving Rmb10bn p.a. in 26E-28E (vs. Rmb20bn achieved in average 23A-25A), with N-T repayment needs (Rmb2.3bn scheduled for rest of 2026E) likely well covered by rental-supported OCF.

Keys to watch next: 1) For upcoming 1H26 earnings - management guidance on potential inventory impairment and profitability impacts, rental income growth strength, net profit inflection timeline, etc. 2) the progress of vintage inventory clearance through ordinary project sell-throughs, and rezoning or swapping of acquired lands with government, and whether land acquisition would resume to replenish landbank with higher-quality, better margin plots to drive future contract sales recovery. 3) social retail sales trends and whether Longfor's GMV could continuously outperform that and lead to rental growth upside. 4) debt reduction and restructuring pace (e.g. swapping high-interest financing with low-cost IP operating loans); 5) other policy catalysts which could boost the employment outlook, consumer confidence or support the property market from the supply-side.

Valuation: Longfor trades at a 32% discount to end-26E NAV, 0.3X 2026E P/B vs. coverage average 34%/0.5X. Retain Neutral.

Key risks: 1) Above- or below-policy execution on supply-side liquidity support and demand-side easing; 2) Better-/weaker-than-expected deleveraging plan execution leading to stronger/weaker liquidity conditions; 3) Stronger/weaker-than-expected sell-through; 4) Better-/weaker-than-expected margin especially for old-vintage projects acquired before the current downturn; 5) Above-/below-expectation rental growth.

<table><tr><td>0960.HK</td><td>12m Price Target: HK$7.5</td><td colspan="2">Price: HK$6.79</td><td colspan="2">Upside: 10.5%</td></tr><tr><td rowspan="2">Neutral</td><td>GS Forecast</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Market cap: HK$35.1bn / $4.5bn</td><td>Revenue (Rmb mn) New</td><td>97,308.6</td><td>75,125.5</td><td>71,845.0</td><td>67,268.5</td></tr><tr><td>Enterprise value: HK$244.7bn / $31.2bn</td><td>Revenue (Rmb mn) Old</td><td>97,308.6</td><td>82,205.2</td><td>79,673.4</td><td>76,627.3</td></tr><tr><td>3m ADTV :HK$164.3mn/ $21.0mn</td><td>EBITDA (Rmb mn)</td><td>6,926.0</td><td>415.4</td><td>6,283.6</td><td>8,562.6</td></tr><tr><td>China</td><td>EPS (Rmb) New</td><td>(0.24)</td><td>(0.34)</td><td>0.15</td><td>0.30</td></tr><tr><td>China Property</td><td>EPS (Rmb) Old</td><td>(0.24)</td><td>(0.07)</td><td>0.31</td><td>0.47</td></tr><tr><td></td><td>P/E (X)</td><td>NM</td><td>NM</td><td>38.0</td><td>19.2</td></tr><tr><td>M&amp;A Rank: 3</td><td>P/B (X)</td><td>0.4</td><td>0.3</td><td>0.3</td><td>0.3</td></tr><tr><td>Leases incl. in net debt &amp; EV?: No</td><td>Dividend yield (%)</td><td>0.8</td><td>0.0</td><td>0.8</td><td>1.6</td></tr><tr><td></td><td>CROCI (%)</td><td>NM</td><td>0.1</td><td>0.7</td><td>1.1</td></tr><tr><td></td><td></td><td>12/25</td><td>6/26E</td><td>12/26E</td><td>6/27E</td></tr><tr><td></td><td>EPS (Rmb)</td><td>(0.44)</td><td>(0.03)</td><td>(0.31)</td><td>0.06</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 16 Jul 2026 close.

## Price Target Risks & Methodology

Our 12m end-26E NAV-based target price is HK\$7.5, based on a 25% discount to end-25E NAV.

## Key risks:

1) Above- or below-policy execution on supply-side liquidity support and demand-side easing; 2) Better-/weaker-than-expected deleveraging plan execution leading to stronger/weaker liquidity conditions; 3) Stronger/weaker-than-expected sell-through; 4) Better-/weaker-than-expected margin especially for old-vintage projects acquired before the current downturn; 5) Above-/below-expectation rental growth.

## Disclosure Appendix

## Reg AC

We, Yi Wang, CFA, Shi Xu and Kaiyan Jing, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Contributing Authors: Yi Wang, CFA GS (China) Securities Company Limited, Shi Xu GS (China) Securities Company Limited, Kaiyan Jing GS (China) Securities Company Limited.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses inputs for the fiscal year at least seven quarters in the future compared with the year at least three quarters in the future (on a per-share basis for all metrics).

For a more detailed description of how we calculate the GS Factor Profile, please contact your GS representative.

## M&A Rank

Across our global coverage, we examine stocks using an M&A framework, considering both qualitative factors and quantitative factors (which may vary across sectors and regions) to incorporate the potential that certain companies could be acquired. We then assign a M&A rank as a means of scoring companies under our rated coverage from 1 to 3, with 1 representing high (30%-50%) probability of the company becoming an acquisition target, 2 representing medium (15%-30%) probability and 3 representing low (0%-15%) probability. For companies ranked 1 or 2, in line with our standard departmental guidelines we incorporate an M&A component into our target price. M&A rank of 3 is considered immaterial and therefore does not factor into our price target, and may or may not be discussed in research.

## Quantum

Quantum is GS' proprietary database providing access to detailed financial statement histories, forecasts and ratios. It can be used for in-depth analysis of a single company, or to make comparisons between companies in different sectors and markets.

## Disclosures

The rating(s) for Longfor Group is/are relative to the other companies in its/their coverage universe: China Jinmao Holdings, China Merchants Shekou Inds Zone, China Overseas Land & Investment, China Resources Land, China Vanke (A), China Vanke (H), Country Garden Holdings, Greentown China Holdings, Longfor Group, Poly Developments and Holdings, Seazen Group Ltd

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Longfor Group (HK\$6.67)

GS had an investment banking services client relationship during the past 12 months with: Longfor Group (HK\$6.67)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: Longfor Group (HK\$6.67)

GS had a non-securities services client relationship during the past 12 months with: Longfor Group (HK\$6.67)

GS makes a market in the securities or derivatives thereof: Longfor Group (HK\$6.67)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See 'Ratings, Coverage universe and related definitions' below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/e33ed3329ef143137ef37306d88c6a40746981292c696d2e2c75ac294d1b04ad.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s) Longfor Group (0960.HK)

Date of report Target price (HK\$) Closing price (HK\$)

<table><tr><td>09-Apr-26</td><td>8.70</td><td>7.43</td></tr><tr><td>30-Mar-26</td><td>8.60</td><td>7.69</td></tr><tr><td>17-Dec-25</td><td>9.90</td><td>9.07</td></tr><tr><td>01-Sep-25</td><td>12.50</td><td>10.83</td></tr><tr><td>22-Apr-25</td><td>13.50</td><td>10.84</td></tr><tr><td>31-Mar-25</td><td>14.40</td><td>9.81</td></tr><tr><td>06-Feb-25</td><td>16.50</td><td>9.80</td></tr><tr><td>22-Oct-24</td><td>17.00</td><td>12.54</td></tr><tr><td>26-Aug-24</td><td>11.90</td><td>8.75</td></tr><tr><td>25-Mar-24</td><td>13.00</td><td>10.66</td></tr><tr><td>02-Feb-24</td><td>14.60</td><td>8.70</td></tr><tr><td>31-Oct-23</td><td>17.00</td><td>11.38</td></tr><tr><td>21-Aug-23</td><td>26.00</td><td>15.98</td></tr></table>

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an offi

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
