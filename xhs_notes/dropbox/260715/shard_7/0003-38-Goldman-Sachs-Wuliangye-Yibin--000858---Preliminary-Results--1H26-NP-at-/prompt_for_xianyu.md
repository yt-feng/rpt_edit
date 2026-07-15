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
# Wuliangye Yibin (000858.SZ): Preliminary Results: 1H26 NP at c.50% of 1H24 level likely on continued de-stocking; Sell

Wuliangye pre-announced its 1H26 results. The company expects 1H26 NP of Rmb8,730\~9,200mn, representing 89%\~99% yoy growth (vs. Rmb4.6bn low base in 1H25 post restatement), recovering to 46\~48% of 1H24 NP of Rmb19.1bn, with the midpoint at Rmb8,965mn (up 94% yoy) and 15% below GSe of Rmb10,559mn (up 128% yoy). The implied 2Q26 NP is Rmb667\~1,137mn, up 222%\~448% yoy from the Rmb208mn low base in 2Q25, with the midpoint at Rmb902mn (up 335% yoy), still at a fraction (13\~23%) of 2Q24 NP at Rmb5.0bn. We think the weaker-than-expected NP rebound in 2Q26 may reflect that the company's sell-in remains under de-stocking and recovers slower than expectation despite DD% sell-through growth YTD in Common Wuliangye.

Leaf Liu
+852-3966-4169 | leaf.liu@gs.com
GS (Asia) L.L.C.

Christina Liu
+852-2978-6983 | christina.liu@gs.com
GS (Asia) L.L.C.

Valerie Zhou
+852-2978-0820 | valerie.zhou@gs.com
GS (Asia) L.L.C.

Exhibit 1: Wuliangye 1H/2Q26 Pre-result Summary

<table><tr><td colspan="2">Wuliangye</td><td colspan="4">Pre-results</td><td colspan="4">Diff. vs GSe</td><td colspan="3">vs. 1H/2Q24</td></tr><tr><td>1H26 (Rmb mn)</td><td>Low-end</td><td>Mid-point</td><td>High-end</td><td>GSe</td><td>1H24</td><td>Low-end</td><td>Mid-point</td><td>High-end</td><td>Low-end</td><td>Mid-point</td><td>High-end</td><td></td></tr><tr><td>Net profits</td><td>8,730</td><td>8,965</td><td>9,200</td><td>10,559</td><td>19,057</td><td>-17%</td><td>-15%</td><td>-13%</td><td>46%</td><td>47%</td><td>48%</td><td></td></tr><tr><td>yoy</td><td>89%</td><td>94%</td><td>99%</td><td>128%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Recurring net profits</td><td>8,460</td><td>8,695</td><td>8,930</td><td>10,559</td><td>18,939</td><td>-20%</td><td>-18%</td><td>-15%</td><td>45%</td><td>46%</td><td>47%</td><td></td></tr><tr><td>yoy</td><td>83%</td><td>89%</td><td>94%</td><td>129%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Implied 2Q26 (Rmb mn)</td><td>Low-end</td><td>Mid-point</td><td>High-end</td><td>GSe</td><td>2Q24</td><td></td><td></td><td></td><td>Low-end</td><td>Mid-point</td><td>High-end</td><td></td></tr><tr><td>Net profits</td><td>667</td><td>902</td><td>1,137</td><td>2,496</td><td>5,012</td><td></td><td></td><td></td><td>13%</td><td>18%</td><td>23%</td><td></td></tr><tr><td>yoy</td><td>222%</td><td>335%</td><td>448%</td><td>1103%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Recurring net profits</td><td>424</td><td>659</td><td>894</td><td>2,496</td><td>4,900</td><td></td><td></td><td></td><td>9%</td><td>13%</td><td>18%</td><td></td></tr><tr><td>yoy</td><td>118%</td><td>239%</td><td>361%</td><td>1186%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Source: Company data, GS Global Investment Research

## Price Target Risks and Methodology - Wuliangye Yibin

Valuation methodology: We are Sell rated. Our 12m TP of Rmb70 is based on a 16x 2027E P/E discounted back to mid-2027E at a 7.8% COE.  
Key upside risks: 1) Successful new product roll-out, esp. in mid-end price range; 2) Reduced competition in super-premium segment from Moutai/Laojiao; 3) Policy stimulus that will meaningfully drive demand recovery for high-end spirits; 4) More shareholder return enhancements.

<table><tr><td>000858.SZ</td><td colspan="2">12m Price Target: Rmb70.00</td><td colspan="2">Price: Rmb73.40</td><td colspan="2">Downside: 4.6%</td></tr><tr><td colspan="2">Sell</td><td colspan="5">GS Forecast</td></tr><tr><td colspan="2"></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>1/28E</td></tr><tr><td></td><td>Market cap:</td><td>Revenue (Rmb mn)</td><td>40,528.5</td><td>51,412.4</td><td>55,769.4</td><td>62,414.5</td></tr><tr><td></td><td>Rmb284.9bn / $42.0bn</td><td>EBITDA (Rmb mn)</td><td>10,065.8</td><td>20,156.0</td><td>22,489.1</td><td>25,975.7</td></tr><tr><td></td><td>Enterprise value:</td><td>EPS (Rmb)</td><td>2.31</td><td>4.19</td><td>4.57</td><td>5.22</td></tr><tr><td></td><td>Rmb174.1bn / $25.7bn</td><td>P/E (X)</td><td>54.1</td><td>17.5</td><td>16.1</td><td>14.0</td></tr><tr><td></td><td>3m ADTV: Rmb2.6bn / $381.6mn</td><td>P/B (X)</td><td>4.0</td><td>2.5</td><td>2.5</td><td>2.5</td></tr><tr><td></td><td>China Consumer Staples</td><td>Dividend yield (%)</td><td>4.1</td><td>7.0</td><td>7.0</td><td>7.0</td></tr><tr><td></td><td>M&amp;A Rank: 3</td><td>N debt/EBITDA (ex lease,X)</td><td>(12.6)</td><td>(5.6)</td><td>(5.1)</td><td>(4.4)</td></tr><tr><td></td><td>Leases incl. in net debt &amp; EV?: No</td><td>CROCI (%)</td><td>6.9</td><td>14.0</td><td>15.2</td><td>17.2</td></tr><tr><td></td><td></td><td>FCF yield (%)</td><td>5.7</td><td>2.4</td><td>7.4</td><td>6.4</td></tr><tr><td colspan="2"></td><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td colspan="2"></td><td>EPS (Rmb)</td><td>2.08</td><td>0.64</td><td>0.74</td><td>0.73</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 14 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, Leaf Liu, Christina Liu and Valerie Zhou, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Leaf Liu GS (Asia) L.L.C., Christina Liu GS (Asia) L.L.C., Valerie Zhou GS (Asia) L.L.C..

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

The rating(s) for Wuliangye Yibin is/are relative to the other companies in its/their coverage universe: Anhui Gujing Distillery Co., Budweiser APAC, Busy Ming Group, China Feihe Ltd., China Resources Beer, China Resources Beverage, Chongqing Brewery, Eastroc Beverage (A), Foshan Haitian Flavouring & Food (A), Foshan Haitian Flavouring & Food (H), Fujian Wanchen Food, Jiangsu King's Luck Brewery, Jiangsu Yanghe, Jiugui Liquor, Jonjee Hi-Tech, Kweichow Moutai, Luzhou Laojiao, Mengniu Dairy, Nongfu Spring, Qianhe Condiment and Food, Shanghai Bairun, Shanxi Xinghuacun Fen Wine, Sichuan Swellfun Co., Sichuan Teway Food Group, Tingyi, Tsingtao Brewery (A), Tsingtao Brewery (H), Uni-President China, Wuliangye Yibin, Yihai International Holding, Yili Industrial, ZJLD

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Wuliangye Yibin (Rmb73.40)

GS had an investment banking services client relationship during the past 12 months with: Wuliangye Yibin (Rmb73.40)

Distribution of ratings/investment banking relationships
GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/41c52fcc815e0da8ff3419fc0f8121026b6bf5615393d22cdd24246498f9a034.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s) Wuliangye Yibin (000858.SZ)

<table><tr><td>Date of report</td><td>Target price (Rmb)</td><td>Closing price (Rmb)</td></tr><tr><td>23-Jun-26</td><td>70.00</td><td>74.76</td></tr><tr><td>05-May-26</td><td>83.00</td><td>97.08</td></tr><tr><td>30-Oct-25</td><td>133.00</td><td>118.47</td></tr><tr><td>16-Sep-25</td><td>145.00</td><td>125.80</td></tr><tr><td>09-Jul-25</td><td>139.00</td><td>121.60</td></tr><tr><td>05-May-25</td><td>170.00</td><td>128.70</td></tr><tr><td>16-Jan-25</td><td>166.00</td><td>131.48</td></tr><tr><td>06-Nov-24</td><td>177.00</td><td>151.25</td></tr><tr><td>10-Sep-24</td><td>180.00</td><td>116.43</td></tr><tr><td>01-Aug-24</td><td>172.00</td><td>124.00</td></tr><tr><td>06-May-24</td><td>188.00</td><td>155.01</td></tr><tr><td>15-Apr-24</td><td>190.00</td><td>147.32</td></tr><tr><td>31-Jan-24</td><td>189.00</td><td>126.30</td></tr><tr><td>29-Oct-23</td><td>202.00</td><td>152.99</td></tr><tr><td>27-Aug-23</td><td>200.00</td><td>161.55</td></tr><tr><td>21-Jul-23</td><td>212.00</td><td>171.27</td></tr></table>

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such

advice, consider the appropriateness of the advice havi

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
