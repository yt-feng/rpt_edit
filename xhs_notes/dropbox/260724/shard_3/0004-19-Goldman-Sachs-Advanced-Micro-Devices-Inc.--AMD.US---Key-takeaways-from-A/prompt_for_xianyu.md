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
# Advanced Micro Devices Inc. (AMD): Key takeaways from Advancing AI 2026

Key stock takeaways: We attended CEO Dr. Lisa Su's keynote at the company's Advancing AI event in San Francisco. Key highlights were: (1) AMD announced a strategic partnership with Anthropic for 2GW of Helios racks beginning in 1H27 (along with a \$5 bn equity investment from AMD); (2) AMD expanded its partnership with Microsoft to deploy Helios racks, Venice CPUs and networking infrastructure across Azure workloads; (3) AMD raised its total compute/accelerator/server CPU TAM to \$2 tn/\$1.4 tn/\$220 bn by 2030, corresponding to \~50% growth in server CPUs; (4) The company launched ROCm.ai to provide developers with an AI-driven software development experience. We believe investors were positioned constructively heading into the event, and based on our conversations we believe the series of announcements this week met these elevated expectations ahead of the company's earnings report on August 4. We reiterate our Buy rating on AMD, as we see the company well positioned to capture an increasing share of overall compute market, driven by an already strong presence in the CPU market and a broadening aperture of key customers in the AI accelerator market.

## Key takeaways include:

\- Partnership with Anthropic: AMD and Anthropic announced a strategic partnership under which Anthropic will deploy 2 GWs of Instinct MI450 GPUs in Helios rack-scale AI systems, with the initial 1 GW expected to begin deployment in 1H27. The partnership extends beyond hardware, with the companies collaborating to optimize Claude workloads on AMD GPUs, accelerate development of AMD's ROCm software platform, and expand Claude's use across AMD's engineering and product teams. AMD also plans to make a strategic equity investment of up to \$5 bn in Anthropic.

\- Partnership with Microsoft: Microsoft and AMD announced an expanded strategic partnership, with Microsoft planning to deploy Helios racks (with shipments to Microsoft beginning in 2H26), CPUs, networking and software on Microsoft Azure. The Azure deployment will use Helios for inference workloads spanning frontier models, as well as Microsoft's own AI services and other Azure customer applications. Azure will also introduce two new virtual machines powered by AMD's next-generation 2nm Venice CPUs, while expanding the use of AMD Pensando DPUs in Azure networking services.

■ Increased Datacenter and CPU TAM: Agentic AI is driving a step-function

James Schneider, Ph.D.
+1(212)357-2929 |
jim.schneider@gs.com
GS & Co. LLC

Anmol Makkar
+1(212)357-1366 |
anmol.makkar@gs.com
GS & Co. LLC

Luya You
+1(212)902-5297 | luya.you@gs.com
GS & Co. LLC

Khalil Fenina
+1(212)357-6392 |
khalil.fenina@gs.com
GS & Co. LLC

change in computing demand, requiring both accelerators and CPUs to orchestrate increasingly complex workflows. As a result, the AI infrastructure market is expanding rapidly, with the datacenter AI accelerator TAM projected to grow from \$200 bn to \$1.4 tn in 2030 (40% CAGR), datacenter CPU TAM from \$26 bn to \$220 bn (50% CAGR), and AMD's total compute TAM from \$365 bn to \$2 tn by 2030. AMD also expects to capture 50% of the datacenter CPU market by 2030.

Helios launch: AMD unveiled its next-generation Helios AI rackscale platform, built on CDNA 5 architecture with GPUs featuring up to 40 PFLOPS (FP4), 20 PFLOPS (FP8), 432 GB of HBM4 memory, and 23.3 TB/s memory bandwidth. The system combines 75 GPUs connected via UALink over Ethernet, a 96-core EPYC CPU, Salina DPU, Volcano 800G AI NIC, and six networking trays to deliver higher-scale AI performance. AMD stated that Helios is already in full production, with shipments beginning at the end of 3Q, and volume ramp in 4Q.

Partnership with Cerebras: AMD and Cerebras have partnered to combine AMD's Helios systems with Cerebras' Wafer-Scale Engine, creating a high-performance AI inference solution that delivers ultra-low latency, higher efficiency, and up to 5x better tokens-per-watt. The solution is expected to launch via Cerebras Cloud in 2H26.

■ ROCm.ai: AMD launched ROCm.ai, which integrates with tools such as Cursor, Claude, Codex and Gemini to provide developers with an AI-driven software development experience. AMD also introduced Hyperloom, an optimization layer that automatically tunes system configurations and optimizes end-to-end AI workloads. AMD stated that over 14,000 models have been optimized through Hyperloom, delivering an average 3.3X performance improvement compared with ROCm 7.

Price target. We are Buy rated on AMD. Our 12-month target price of \$640 is based on a 32X P/E multiple applied to our normalized EPS estimate of \$20.00. Key downside risks include: (1) slower-than-expected adoption of agentic AI; (2) slower-than-anticipated deployment of AMD GPUs related to the Meta deal; (3) share erosion of x86 architecture in enterprise AI and (4) lack of operating leverage.

12m Price Target: \$640.00

<table><tr><td>Buy</td><td colspan="5">GS Forecast</td></tr><tr><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Market cap: $890.5bn</td><td>Revenue ($ mn)</td><td>34,639.0</td><td>50,572.5</td><td>86,013.3</td><td>109,024.8</td></tr><tr><td>Enterprise value: $877.8bn</td><td>EBITDA ($ mn)</td><td>6,984.0</td><td>13,179.7</td><td>26,559.4</td><td>36,357.5</td></tr><tr><td>3m ADTV: $16.2bn</td><td>EBIT ($ mn)</td><td>6,130.0</td><td>12,344.7</td><td>25,715.4</td><td>35,493.5</td></tr><tr><td>United States</td><td>EPS ($)</td><td>2.64</td><td>6.20</td><td>13.20</td><td>17.94</td></tr><tr><td rowspan="2">Americas Semiconductors &amp; IT Services</td><td>P/E (X)</td><td>57.7</td><td>87.1</td><td>40.9</td><td>30.1</td></tr><tr><td>EV/EBITDA (X)</td><td>34.3</td><td>66.2</td><td>32.8</td><td>23.6</td></tr><tr><td rowspan="3">M&amp;A Rank: 3</td><td>FCF yield (%)</td><td>2.7</td><td>0.5</td><td>0.7</td><td>2.6</td></tr><tr><td>Dividend yield (%)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net debt/EBITDA (X)</td><td>(1.2)</td><td>(1.0)</td><td>(1.2)</td><td>(2.0)</td></tr><tr><td></td><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td></td><td>EPS ($)</td><td>0.84</td><td>1.32</td><td>1.53</td><td>2.51</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 23 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, James Schneider, Ph.D., Anmol Makkar, Luya You and Khalil Fenina, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: James Schneider, Ph.D. GS & Co. LLC, Anmol Makkar GS & Co. LLC, Luya You GS & Co. LLC, Khalil Fenina GS & Co. LLC.

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

The rating(s) for Advanced Micro Devices Inc. is/are relative to the other companies in its/their coverage universe: ARM Holdings, Accenture Plc, Advanced Micro Devices Inc., Amkor Technology Inc., Analog Devices Inc., Applied Materials Inc., Broadcom Inc., Cadence Design Systems Inc., Camtek, Cognizant Technology Solutions, Credo Technology Group, EPAM Systems Inc., Entegris Inc., GlobalFoundries Inc., Globant SA, Intel Corp., International Business Machines Corp., KLA Corp., Lam Research Corp., MKS Instruments Inc., Marvell Technology Inc., Microchip Technology Inc., Micron Technology Inc., NXP Semiconductors NV, Nvidia Corp., ON Semiconductor Corp., Qnity, Qualcomm Inc., SanDisk Corp., Seagate Technology, SiTime Corp., Synopsys Inc., TaskUs Inc., Teradyne Inc., Texas Instruments Inc., Western Digital Corp.

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS has received compensation for investment banking services in the past 12 months: Advanced Micro Devices Inc. (\$539.69)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Advanced Micro Devices Inc. (\$539.69)

GS has received compensation for non-investment banking services during the past 12 months: Advanced Micro Devices Inc. (\$539.69)

GS had an investment banking services client relationship during the past 12 months with: Advanced Micro Devices Inc. (\$539.69)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: Advanced Micro Devices Inc. (\$539.69)

GS had a non-securities services client relationship during the past 12 months with: Advanced Micro Devices Inc. (\$539.69)

A director and/or employee of GS is a director: Advanced Micro Devices Inc. (\$539.69)

GS makes a market in the securities or derivatives thereof: Advanced Micro Devices Inc. (\$539.69)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td colspan="3">Rating Distribution</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>50%</td><td>34%</td><td>16%</td></tr></table>

<table><tr><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/bd67ca1347794ab8803ba5edb824f9b68c5be035c738e6325383417c116cdd63.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s)

## Advanced Micro Devices Inc. (AMD)

## Date of report Target price (\$) Closing price (\$)

<table><tr><td>05-Jul-26</td><td>640.00</td><td>517.82</td></tr><tr><td>06-May-26</td><td>450.00</td><td>421.39</td></tr><tr><td>24-Feb-26</td><td>240.00</td><td>213.84</td></tr><tr><td>07-Oct-25</td><td>210.00</td><td>211.51</td></tr><tr><td>06-Aug-25</td><td>150.00</td><td>163.12</td></tr><tr><td>10-Jul-25</td><td>140.00</td><td>144.16</td></tr><tr><td>05-Feb-25</td><td>125.00</td><td>112.01</td></tr><tr><td>10-Jan-25</td><td>129.00</td><td>116.04</td></tr><tr><td>01-May-24</td><td>175.00</td><td>144.27</td></tr><tr><td>31-Jan-24</td><td>180.00</td><td>167.69</td></tr><tr><td>18-Dec-23</td><td>157.00</td><td>138.90</td></tr><tr><td>07-Dec-23</td><td>137.00</td><td>128.37</td></tr><tr><td>01-Nov-23</td><td>125.00</td><td>108.04</td></tr></table>

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from servin

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
