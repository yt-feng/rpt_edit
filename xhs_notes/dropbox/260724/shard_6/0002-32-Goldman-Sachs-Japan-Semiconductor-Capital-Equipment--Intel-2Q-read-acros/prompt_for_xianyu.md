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
# Japan Semiconductor Capital Equipment: Intel 2Q read-across: Significantly raises capex outlook; we highlight Buy-rated Lasertec/TEL

Intel (covered by our US semiconductor analyst Jim Schneider) announced 2Q12/26 (Apr-Jun) results and held a conference call early morning on July 24 (JST). We outline our key takeaways below, focusing on the implications for Japanese SPE makers.

## Current business environment

Intel explained that while it is expanding production capacity on the back of robust demand, demand continues to outstrip supply, and thus it is seeing the strongest revenue growth in more than 15 years. From a technology roadmap perspective, the company highlighted that 18A product ramp-up has started, that it has begun risk production of 18A-P, and that it plans to commence 14A risk production in 2HCY27. The company said it already increased capex in 2Q (Apr-Jun) to expand 14A production.

## Views on capex

Intel raised capex guidance by c.US\$3 bn and expects capex to exceed US\$20 bn for the full year. The company said it has secured sufficient fab space via building investments over the past few years, so most of the capex is expected to be directed toward equipment. Intel explained that equipment capex is set to increase 40% yoy in 2026 (it previously guided for WFE investment in 2026 to rise c.25% yoy). While management provided no quantitative guidance for 2027, directionally it pointed to a significant yoy increase in capex in view of yields in 18A and advanced processes and current levels of customer inquiries.

## Read-across for Japanese SPE makers

We think the clear path toward production ramp-up in advanced processes and Intel's meaningfully higher capex outlook have positive implications particularly for Lasertec (Buy, on CL) and Tokyo Electron (Buy), which have high sales exposure to Intel. With Intel's investment in advanced packaging is also set to accelerate in back-end processes, we also see positive read-across for Disco (Buy), which stands to benefit from EMIB-T production capacity expansion.

## Shuhei Nakamura

+81(3)4587-9932 |
shuhei.nakamura@gs.com
GS Japan Co., Ltd.

Kaho Otake
+81(3)4587-7498 | kaho.otake@gs.com
GS Japan Co., Ltd.

Exhibit 1: Intel sales exposure across our Japan SPE coverage (FY25E GSe)  
![](images/ade57d3c792aab4fca7f51540fb8964b266f7224a75da788b07fcc3e40e6b8f7.jpg)  
Source: GS Global Investment Research

Exhibit 2: Target prices, methodologies and risks for stocks mentioned

<table><tr><td>Company Name (rating)</td><td>Ticker</td><td>12-m TP (¥)</td><td>Methodology</td><td>Risks</td></tr><tr><td>DISCO (Buy)</td><td>6146.T</td><td>100,000</td><td>Based on the global SPE sector average multiple of 18X and our FY3/28E estimates. We then apply a sector-relative premium of 50%.</td><td>(-) slowdown or share loss in AI-related demand(-) slowdown in China demand or tightening of export controls(-) rapid yen appreciation against the USD</td></tr><tr><td>Lasertec (Buy)*</td><td>6920.T</td><td>70,000</td><td>Based on the global SPE sector average multiple of 18X and the average of our FY6/28E estimates. We then apply a sector-relative premium of 50%.</td><td>(-) Decline in market share due to new entrants(-) Lack of progress in ACTIS adoption by wafer fabs(-) Weaker customer investment appetite for leading-edge process nodes(-) Rapid appreciation of the yen against the US dollar</td></tr><tr><td>Tokyo Electron (Buy)</td><td>8035.T</td><td>83,000</td><td>Based on the global SPE sector average multiple of 18X and our FY3/28E estimates. We then apply a sector-relative premium of 30%.</td><td>(-) prolonged inventory adjustment phase in the semiconductor industry(-) further strengthening of export restrictions(-) depressed valuation multiple amid upward pressure on interest rates and other factors</td></tr></table>

\*on APAC Conviction List

Source: GS Global Investment Research

## Disclosure Appendix

## Reg AC

We, Shuhei Nakamura and Kaho Otake, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Shuhei Nakamura GS Japan Co., Ltd., Kaho Otake GS Japan Co., Ltd..

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

The rating(s) for DISCO, Lasertec and Tokyo Electron is/are relative to the other companies in its/their coverage universe: Advantest, DISCO, Ebara, HOYA, JEOL, Kioxia Holdings, Kokusai Electric, Lasertec, SCREEN Holdings, Tokyo Electron, Tokyo Seimitsu, Ulvac

The rating(s) for Intel Corp. is/are relative to the other companies in its/their coverage universe: ARM Holdings, Accenture Plc, Advanced Micro Devices Inc., Amkor Technology Inc., Analog Devices Inc., Applied Materials Inc., Broadcom Inc., Cadence Design Systems Inc., Camtek, Cognizant Technology Solutions, Credo Technology Group, EPAM Systems Inc., Entegris Inc., GlobalFoundries Inc., Globant SA, Intel Corp., International Business Machines Corp., KLA Corp., Lam Research Corp., MKS Instruments Inc., Marvell Technology Inc., Microchip Technology Inc., Micron Technology Inc., NXP Semiconductors NV, Nvidia Corp., ON Semiconductor Corp., Qnity, Qualcomm Inc., SanDisk Corp., Seagate Technology, SiTime Corp., Synopsys Inc., TaskUs Inc., Teradyne Inc., Texas Instruments Inc., Western Digital Corp.

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS beneficially owned 1% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the month end preceding this report: Lasertec (¥45,130)

GS has received compensation for investment banking services in the past 12 months: Intel Corp. (\$100.23)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: DISCO (¥69,410), Intel Corp. (\$100.23), Lasertec (¥45,130) and Tokyo Electron (¥65,950)

GS has received compensation for non-investment banking services during the past 12 months: Intel Corp. (\$100.23) and Tokyo Electron (¥65,950)

GS had an investment banking services client relationship during the past 12 months with: DISCO (¥69,410), Intel Corp. (\$100.23), Lasertec (¥45,130) and Tokyo Electron (¥65,950)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: Intel Corp. (\$100.23) and Tokyo Electron (¥65,950)

GS had a non-securities services client relationship during the past 12 months with: DISCO (¥69,410), Intel Corp. (\$100.23) and Tokyo Electron (¥65,950)

GS makes a market in the securities or derivatives thereof: Intel Corp. (\$100.23)

DISCO (6146.T)  
Distribution of ratings/investment banking relationships
GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/b3be9e8bb378fb7ca7c8214a1e05f2391d557c6132fc2900eefeb6dd9d1c9cbd.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/f35696aa0c6ee59d2c304621af01c08d855ae6a74accaa6bdd510ac85a5c51d7.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/3948d92329cf99eab3280823c53d690e4f9ffe1d45fdc0283377799e75bbb0fe.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/217ee951ed666c64a12b43ed7579b33febeb3901514550116c03afb4cf302d16.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s)

## Intel Corp. (INTC)

<table><tr><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td><td>Date of report</td><td>Target price ($)</td><td>Closing price ($)</td></tr><tr><td>06-Jul-26</td><td>100,000</td><td>78,000</td><td>25-Jun-26</td><td>150.00</td><td>132.87</td></tr><tr><td>30-Jun-26</td><td>95,000</td><td>81,260</td><td>31-Jan-25</td><td>18.00</td><td>19.43</td></tr><tr><td>31-May-26</td><td>87,000</td><td>65,090</td><td>10-Jan-25</td><td>19.00</td><td>19.15</td></tr><tr><td>22-Apr-26</td><td>86,000</td><td>74,830</td><td>01-Nov-24</td><td>20.00</td><td>23.20</td></tr><tr><td>09-Mar-26</td><td>83,000</td><td>66,500</td><td>17-Oct-24</td><td>21.00</td><td>22.44</td></tr><tr><td>21-Jan-26</td><td>68,000</td><td>58,570</td><td>02-Aug-24</td><td>22.00</td><td>21.48</td></tr><tr><td>08-Jan-26</td><td>64,000</td><td>55,590</td><td>20-May-24</td><td>29.00</td><td>32.10</td></tr><tr><td>06-Jan-26</td><td>62,000</td><td>54,200</td><td>08-May-24</td><td>30.00</td><td>30.00</td></tr><tr><td>29-Oct-25</td><td>61,000</td><td>56,390</td><td>26-Apr-24</td><td>34.00</td><td>31.88</td></tr><tr><td>08-Oct-25</td><td>60,000</td><td>52,140</td><td>26-Jan-24</td><td>39.00</td><td>43.65</td></tr></table>

<table><tr><td colspan="3">DISCO (6146.T)</td></tr><tr><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td></tr><tr><td>06-Oct-25</td><td>56,000</td><td>54,000</td></tr><tr><td>09-Jul-25</td><td>51,000</td><td>41,290</td></tr><tr><td>30-Jun-25</td><td>47,000</td><td>42,630</td></tr><tr><td>13-Apr-25</td><td>43,000</td><td>27,470</td></tr><tr><td>04-Apr-25</td><td>44,000</td><td>27,635</td></tr><tr><td>24-Mar-25</td><td>51,000</td><td>33,060</td></tr><tr><td>21-Nov-24</td><td>59,000</td><td>42,380</td></tr><tr><td>01-Nov-24</td><td>57,000</td><td>42,810</td></tr><tr><td>04-Oct-24</td><td>54,000</td><td>39,710</td></tr><tr><td>02-Oct-24</td><td>56,000</td><td>37,410</td></tr><tr><td>02-Sep-24</td><td>63,000</td><td>41,350</td></tr><tr><td>22-Aug-24</td><td>66,000</td><td>43,560</td></tr><tr><td>04-Jul-24</td><td>71,000</td><td>64,580</td></tr><tr><td>27-May-24</td><td>65,000</td><td>61,790</td></tr><tr><td>04-Apr-24</td><td>60,000</td><td>56,750</td></tr><tr><td>21-Mar-24</td><td>56,000</td><td>52,960</td></tr><tr><td>13-Mar-24</td><td>53,000</td><td>50,000</td></tr><tr><td>31-Jan-24</td><td>43,000</td><td>40,380</td></tr><tr><td>24-Jan-24</td><td>42,000</td><td>40,730</td></tr><tr><td>04-Jan-24</td><td>39,000</td><td>33,630</td></tr><tr><td>21-Nov-23</td><td>34,000</td><td>32,030</td></tr><tr><td>26-Oct-23</td><td>32,000</td><td>26,960</td></tr><tr><td>05-Oct-23</td><td>31,000</td><td>27,940</td></tr><tr><td>15-Aug-23</td><td>30,000</td><td>25,865</td></tr></table>

<table><tr><td colspan="3">Intel Corp. (INTC)</td></tr><tr><td>Date of report</td><td>Target price ($)</td><td>Closing price ($)</td></tr><tr><td>12-Jan-24</td><td>34.00</td><td>47.12</td></tr><tr><td>27-Oct-23</td><td>30.00</td><td>35.54</td></tr><tr><td>28-Jul-23</td><td>28.00</td><td>36.83</td></tr></table>

Tokyo Electron (8035.T)

<table><tr><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td></tr><tr><td>30-Jun-26</td><td>83,00

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
