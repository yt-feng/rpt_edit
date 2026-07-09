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
# Americas Technology: Hardware: C2Q26 PC market share review: Industry unit shipment declines driven by component availability

BOTTOM LINE: IDC released preliminary estimates for 2Q26 PC shipments (including workstations) of 68.2 mn, down -4.9% year-over-year, marking the first decline after 9 sequential quarters of positive growth. IDC attributes the decline to ongoing component shortages (memory, storage), as well as a challenging macro backdrop, which should not ease until early 2028. IDC reiterated its expectation for PC shipments to see sharp declines for 2H26 driven by higher ASPs and limited supply. Though units are down, IDC observes industry revenue growth from price increases. A prolonged supply shortage should benefit larger, scaled players with multiple product lines and sophisticated supply chain management capabilities like Apple, Dell, Lenovo; IDC expects these larger vendors should be able to consolidate market share from smaller players over time.

2Q26 vendor market share: Apple, ASUS, and Lenovo grew ahead of the market, DELL performed in-line, and HP lagged. Specifically, IDC estimates that Apple shipments grew +10% (9.9% share), ASUS shipments grew 0.2% (7.4% share), Lenovo shipments were down -2% (24.4% share), Dell shipments were down -5% (13.6% share), and HP units declined -9% (19.1% share).

Katherine Murphy +1(212)902-1151 | katherine.a.murphy@gs.com GS & Co. LLC

Michael Ng, CFA
+1(212)902-8618 | michael.ng@gs.com
GS & Co. LLC

Zorayda Montemayor +1(212)357-6403 | zorayda.montemayor@gs.com GS & Co. LLC

Exhibit 1: IDC estimates 2Q26 PC shipments (including workstations) of 68.2 mn, marking -5% decline YoY PC units by vendor (mn)

<table><tr><td>(in millions)</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26</td></tr><tr><td>Vendor, Global (Includes Workstations)</td><td colspan="4"></td><td colspan="4"></td><td colspan="2"></td></tr><tr><td>Units</td><td colspan="4"></td><td colspan="4"></td><td colspan="2"></td></tr><tr><td>Apple</td><td>4.8</td><td>5.1</td><td>6.0</td><td>7.1</td><td>5.7</td><td>6.1</td><td>6.7</td><td>7.2</td><td>6.3</td><td>6.7</td></tr><tr><td>ASUS</td><td>3.6</td><td>4.2</td><td>5.3</td><td>4.9</td><td>4.1</td><td>5.0</td><td>6.0</td><td>5.5</td><td>4.8</td><td>5.0</td></tr><tr><td>Dell Technologies</td><td>9.3</td><td>10.1</td><td>9.8</td><td>9.9</td><td>9.6</td><td>9.8</td><td>10.1</td><td>11.7</td><td>10.3</td><td>9.3</td></tr><tr><td>HP Inc</td><td>12.0</td><td>13.7</td><td>13.6</td><td>13.7</td><td>12.8</td><td>14.3</td><td>15.0</td><td>15.4</td><td>12.1</td><td>13.0</td></tr><tr><td>Lenovo</td><td>13.7</td><td>14.7</td><td>16.5</td><td>16.9</td><td>15.2</td><td>17.0</td><td>19.3</td><td>19.4</td><td>16.5</td><td>16.6</td></tr><tr><td>Acer</td><td colspan="4"></td><td colspan="4"></td><td colspan="2"></td></tr><tr><td>Others</td><td>16.7</td><td>16.3</td><td>19.8</td><td>19.1</td><td>18.6</td><td>19.6</td><td>21.4</td><td>21.3</td><td>17.8</td><td>17.5</td></tr><tr><td>Total PC Units</td><td>60.2</td><td>64.2</td><td>71.0</td><td>71.6</td><td>65.9</td><td>71.7</td><td>78.5</td><td>80.5</td><td>67.9</td><td>68.2</td></tr><tr><td>Units market share</td><td colspan="4"></td><td colspan="4"></td><td colspan="2"></td></tr><tr><td>Apple</td><td>8%</td><td>8%</td><td>8%</td><td>10%</td><td>9%</td><td>9%</td><td>9%</td><td>9%</td><td>9%</td><td>10%</td></tr><tr><td>ASUS</td><td>6%</td><td>7%</td><td>8%</td><td>7%</td><td>6%</td><td>7%</td><td>8%</td><td>7%</td><td>7%</td><td>7%</td></tr><tr><td>Dell Technologies</td><td>15%</td><td>16%</td><td>14%</td><td>14%</td><td>14%</td><td>14%</td><td>13%</td><td>15%</td><td>15%</td><td>14%</td></tr><tr><td>HP Inc</td><td>20%</td><td>21%</td><td>19%</td><td>19%</td><td>19%</td><td>20%</td><td>19%</td><td>19%</td><td>18%</td><td>19%</td></tr><tr><td>Lenovo</td><td>23%</td><td>23%</td><td>23%</td><td>24%</td><td>23%</td><td>24%</td><td>25%</td><td>24%</td><td>24%</td><td>24%</td></tr><tr><td>Acer</td><td colspan="4"></td><td colspan="4"></td><td colspan="2"></td></tr><tr><td>Others</td><td>28%</td><td>25%</td><td>28%</td><td>27%</td><td>28%</td><td>27%</td><td>27%</td><td>26%</td><td>26%</td><td>26%</td></tr><tr><td>Year-over-year change</td><td colspan="4"></td><td colspan="4"></td><td colspan="2"></td></tr><tr><td>Units</td><td colspan="4"></td><td colspan="4"></td><td colspan="2"></td></tr><tr><td>Apple</td><td>14%</td><td>8%</td><td>-15%</td><td>19%</td><td>19%</td><td>19%</td><td>12%</td><td>1%</td><td>11%</td><td>10%</td></tr><tr><td>ASUS</td><td>-5%</td><td>10%</td><td>7%</td><td>15%</td><td>13%</td><td>19%</td><td>12%</td><td>12%</td><td>18%</td><td>0%</td></tr><tr><td>Dell Technologies</td><td>-2%</td><td>-2%</td><td>-4%</td><td>0%</td><td>3%</td><td>-3%</td><td>3%</td><td>18%</td><td>8%</td><td>-5%</td></tr><tr><td>HP Inc</td><td>0%</td><td>2%</td><td>0%</td><td>-2%</td><td>6%</td><td>4%</td><td>10%</td><td>12%</td><td>-5%</td><td>-9%</td></tr><tr><td>Lenovo</td><td>8%</td><td>4%</td><td>3%</td><td>5%</td><td>11%</td><td>15%</td><td>17%</td><td>15%</td><td>9%</td><td>-2%</td></tr><tr><td>Acer</td><td colspan="4"></td><td colspan="4"></td><td colspan="2"></td></tr><tr><td>Others</td><td>26%</td><td>29%</td><td>6%</td><td>9%</td><td>11%</td><td>20%</td><td>8%</td><td>12%</td><td>-4%</td><td>-10%</td></tr><tr><td>Total PC Units</td><td>2%</td><td>2%</td><td>1%</td><td>6%</td><td>10%</td><td>12%</td><td>11%</td><td>12%</td><td>3%</td><td>-5%</td></tr><tr><td></td><td colspan="4"></td><td colspan="4"></td><td colspan="2"></td></tr><tr><td>Quarter-over-Quarter growth</td><td colspan="4"></td><td colspan="4"></td><td colspan="2"></td></tr><tr><td>Units</td><td colspan="4"></td><td colspan="4"></td><td colspan="2"></td></tr><tr><td>Apple</td><td>-19%</td><td>7%</td><td>17%</td><td>18%</td><td>-20%</td><td>7%</td><td>10%</td><td>7%</td><td>-12%</td><td>6%</td></tr><tr><td>ASUS</td><td>-15%</td><td>17%</td><td>26%</td><td>-8%</td><td>-17%</td><td>23%</td><td>19%</td><td>-8%</td><td>-13%</td><td>5%</td></tr><tr><td>Dell Technologies</td><td>-6%</td><td>9%</td><td>-2%</td><td>1%</td><td>-4%</td><td>2%</td><td>3%</td><td>16%</td><td>-12%</td><td>-10%</td></tr><tr><td>HP Inc</td><td>-14%</td><td>14%</td><td>-1%</td><td>1%</td><td>-7%</td><td>12%</td><td>5%</td><td>3%</td><td>-21%</td><td>7%</td></tr><tr><td>Lenovo</td><td>-15%</td><td>7%</td><td>12%</td><td>2%</td><td>-10%</td><td>11%</td><td>14%</td><td>0%</td><td>-15%</td><td>0%</td></tr><tr><td>Acer</td><td colspan="4"></td><td colspan="4"></td><td colspan="2"></td></tr><tr><td>Total PC Units</td><td>-11%</td><td>7%</td><td>11%</td><td>1%</td><td>-8%</td><td>9%</td><td>9%</td><td>3%</td><td>-16%</td><td>0%</td></tr></table>

PC shipments include desktops, notebooks, and workstations. Totals may be affected by rounding.

<table><tr><td>2016</td><td>2017</td><td>2018</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td></tr><tr><td>18.6</td><td>19.0</td><td>18.1</td><td>17.9</td><td>22.8</td><td>27.8</td><td>27.9</td><td>21.9</td><td>23.0</td><td>25.7</td></tr><tr><td>19.1</td><td>17.1</td><td>15.4</td><td>14.9</td><td>18.2</td><td>21.8</td><td></td><td>16.8</td><td>18.0</td><td>20.5</td></tr><tr><td>39.2</td><td>40.1</td><td>42.2</td><td>44.3</td><td>48.0</td><td>56.3</td><td>48.1</td><td>40.0</td><td>39.1</td><td>41.1</td></tr><tr><td>52.7</td><td>57.1</td><td>58.2</td><td>60.8</td><td>66.0</td><td>71.5</td><td>53.9</td><td>52.9</td><td>53.0</td><td>57.5</td></tr><tr><td>54.9</td><td>54.1</td><td>58.0</td><td>63.6</td><td>70.6</td><td>79.9</td><td>67.0</td><td>59.1</td><td>61.8</td><td>70.9</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>24.0</td><td>18.2</td><td></td><td></td><td></td></tr><tr><td>256.2</td><td>255.4</td><td>254.7</td><td>262.1</td><td>298.8</td><td>353.6</td><td>297.4</td><td>260.1</td><td>267.0</td><td>296.6</td></tr><tr><td>7%</td><td>7%</td><td>7%</td><td>7%</td><td>8%</td><td>8%</td><td>9%</td><td>8%</td><td>9%</td><td>9%</td></tr><tr><td>7%</td><td>7%</td><td>6%</td><td>6%</td><td>6%</td><td>6%</td><td>0%</td><td>6%</td><td>7%</td><td>7%</td></tr><tr><td>15%</td><td>16%</td><td>17%</td><td>17%</td><td>16%</td><td>16%</td><td>16%</td><td>15%</td><td>15%</td><td>14%</td></tr><tr><td>21%</td><td>22%</td><td>23%</td><td>23%</td><td>22%</td><td>20%</td><td>18%</td><td>20%</td><td>20%</td><td>19%</td></tr><tr><td>21%</td><td>21%</td><td>23%</td><td>24%</td><td>24%</td><td>23%</td><td>23%</td><td>23%</td><td>23%</td><td>24%</td></tr><tr><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td colspan="10"></td></tr><tr><td></td><td>2%</td><td>-5%</td><td>-1%</td><td>27%</td><td>22%</td><td>0%</td><td>-21%</td><td>5%</td><td>12%</td></tr><tr><td></td><td></td><td></td><td>-3%</td><td>22%</td><td></td><td></td><td></td><td>7%</td><td>14%</td></tr><tr><td></td><td>2%</td><td>5%</td><td>5%</td><td>8%</td><td>17%</td><td>-15%</td><td>-17%</td><td>-2%</td><td>5%</td></tr><tr><td></td><td>8%</td><td>2%</td><td>5%</td><td>9%</td><td>8%</td><td>-25%</td><td>-2%</td><td>0%</td><td>8%</td></tr><tr><td></td><td>-1%</td><td>7%</td><td>10%</td><td>11%</td><td>13%</td><td>-16%</td><td>-12%</td><td>5%</td><td>15%</td></tr><tr><td></td><td>0%</td><td>0%</td><td>3%</td><td>14%</td><td>18%</td><td>-16%</td><td>-13%</td><td>3%</td><td>11%</td></tr><tr><td colspan="10"></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Source: IDC

## Disclosure Appendix

## Reg AC

I, Katherine Murphy, hereby certify that all of the views expressed in this report accurately reflect my personal views about the subject company or companies and its or their securities. I also certify that no part of my compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Katherine Murphy GS & Co. LLC, Michael Ng, CFA GS & Co. LLC, Zorayda Montemayor GS & Co. LLC.

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

The rating(s) for Apple Inc., Dell Technologies Inc. and HP Inc. is/are relative to the other companies in its/their coverage universe: AT&T Inc., American Tower Corp., Apple Inc., Arista Networks Inc., Axon Enterprise Inc., Blend Labs, Celestica Inc., Charter Communications Inc., Cisco Systems Inc., Cogent Communications Holdings, Comcast Corp., Compass Inc., Crown Castle Inc., Dell Technologies Inc., Digital Realty Trust Inc., Equinix Inc., F5 Inc., HP Inc., Hewlett Packard Enterprise Co., IREN Ltd., Ingram Micro, Lumen Technologies Inc., NetApp Inc., Opendoor Technologies Inc., Optimum Communications Inc., Penguin Solutions Inc., SBA Communications Corp., Stagwell Inc., Super Micro Computer Inc., T-Mobile US Inc., TD SYNNEX Corp., Verizon Communications, Versant Media Group, Walt Disney Co., Zillow Group

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS beneficially owned 1% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the second most recent month end: Dell Technologies Inc. (\$417.28)

GS has received compensation for investment banking services in the past 12 months: Apple Inc. (\$310.66), Dell Technologies Inc. (\$417.28) and HP Inc. (\$22.96)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Apple Inc. (\$310.66), Dell Technologies Inc. (\$417.28) and HP Inc. (\$22.96)

GS has received compensation for non-investment banking services during the past 12 months: Apple Inc. (\$310.66), Dell Technologies Inc. (\$417.28) and HP Inc. (\$22.96)

GS had an investment banking services client relationship during the past 12 months with: Apple Inc. (\$310.66), Dell Technologies Inc. (\$417.28) and HP Inc. (\$22.96)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: Apple Inc. (\$310.66), Dell Technologies Inc. (\$417.28) and HP Inc. (\$22.96)

GS had a non-securities services client relationship during the past 12 months with: Apple Inc. (\$310.66), Dell Technolog

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
