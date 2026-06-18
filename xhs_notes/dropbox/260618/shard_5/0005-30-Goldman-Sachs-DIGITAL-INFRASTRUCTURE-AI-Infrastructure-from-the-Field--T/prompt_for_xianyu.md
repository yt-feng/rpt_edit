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
## DIGITAL INFRASTRUCTURE

# AI Infrastructure from the Field: Takeaways from 2nd Annual Denver trip

We hosted an investor trip to Denver to explore AI infrastructure themes around data centers and enterprise fiber. Our trip included a data center tour and meetings with management from Flexential (private data center company) and Lumen (LUMN, Neutral). In general, hyperscaler AI infrastructure demand remains strong, with continued strengthening of data center pricing power. Meanwhile, widespread enterprise AI use and infrastructure demand remains nascent, but with increased optimism for future growth. Please see our detailed takeaways within.

## Flexential

During our 2026 Denver data center bus tour, we toured Flexential's Englewood site, an 18 MW air-cooled facility with \~150K square feet with near full occupancy supporting both traditional and AI workloads for both wholesale, multitenancy, and colocation customers. Per the company, the site supported a 60/40 ratio of AI/Non-AI workloads. We come away from our tour of Flexential's Englewood data center with a better understanding of long-term supply constraints across both data center equipment and power, which should continue to drive data center supply tightness supporting pricing power over the longer term.

We also hosted Q&A with Ryan Mallory, CEO; Sam Rudek, COO; Jacob Horr, SVP, Strategic Initiatives; Jack Faunce, VP, Procurement; and Tom Bailey, VP, Energy. Key takeaways include:

## ■ Data center supply/demand tightness continuing to strengthen pricing

power. Per the company, continued tightness between data center capacity supply & demand industry-wide has driven benefits to pricing through both new leases and renewals. For example, for leases on new capacity, Flexential described how it is seeing pricing per kilowatt approaching \$200 (and should trend towards \$250 later this year), relative to \~\$70 in 2021. As such, in order to benefit from the beneficial pricing environment, Flexential aims to avoid pre-selling new capacity further out than 9 months (e.g. Flexential's Atlanta Douglasville 2 site is 85% pre-sold, with final completion in 4Q27). For lease renegotiations (which the company begins 6-8 months in advance of lease endings), the company is able to negotiate 3-4% annual escalators for wholesale deals & 5-6% annual escalators on multi-tenancy deals. Flexential expects to

## Michael Ng, CFA

+1(212)902-8618 | michael.ng@gs.com

GS & Co. LLC

## Zorayda Montemayor

+1(212)357-6403

zorayda.montemayor@gs.com

GS & Co. LLC

## Lindsey Shema

+1(801)578-2673

lindsey.shema@gs.com

GS & Co. LLC

continue to benefit from data center supply tightness on a forward basis given (a) ongoing constraints on power availability & supply chain components, and (b) data center opposition.

Supply chain constraints driving elongated lead times in new builds. Per the company, Flexential is seeing industry-wide supply chain constraints, with the greatest lead times on substations (4 years) and power generators (2 years). As such, the company is actively pre-ordering inventory to prepare for future deployments. Given widespread component constraints, Flexential expects new site builds to take \~3 years to complete, nearly double relative to 2021. Comparatively, Flexential estimates leasable capacity takes \~18 months to become available when the company acquires sites.

Large enterprise & hyperscale customer focus with long-term ROIC targets. Per Flexential, it is increasingly focusing on serving multi-MW high-density multi-tenant and wholesale workloads, (44% of March 2026 MRR), where it estimates TAM is growing at a 19% 2024-2030 CAGR, and primarily serves large enterprise and hyperscale customers. That said, it continues to serve Enterprise Co-location services (smaller scale deployments below 1MW, 31% of March 2026 MRR), where it estimates its TAM growing at a 6% 2025-2030 CAGR. The majority of customer churn it sees today is largely smaller enterprises which decide to transition to the public cloud.

## Lumen Technologies

At Lumen, we hosted Q&A with Chris Stansbury, President and CFO; Michael Reinke, SVP, Transformation Office; and Jim Breem, Investor Relations. Key takeaways include:

## ■ Positive reception of Networking-as-a-Service and cloud on-ramps.

Management highlighted that through Lumen's NaaS platform, clients can use its multi-cloud gateway offering to access its vast cloud on-ramps. They explained that this bypasses the need for enterprises to pay cross-connect fees to co-location centers, can significantly reduce latency, and improves security by creating entirely private connections that do not flow through the public internet. For reference, more than $20\%$ of NaaS net adds in 1Q26 were from new customers and more than $60\%$ were expanding their footprint with NaaS. They are also seeing lower churn from NaaS customers. Furthermore, management noted cloud partners have seen customers who use Lumen's direct cloud on-ramps scale faster.

■ Management sees strong outlook for East-West market, particularly once the proposed Alkira acquisition finalizes. Management estimates a \$58bn TAM for East-West connectivity, growing at a \~13% CAGR. They stated that the recently announced Alkira acquisition (which they expect to finalize in 3Q26), would enable a cloud and carrier agnostic smart, programmable network and eliminate the time it would have taken to develop an in-house solution. Lumen’s offering is primarily for enterprise customers. Management acknowledged enterprise use remains relatively nascent, but they see substantial growth potential for Lumen’s offering as AI use scales. In addition to first mover advantage, management believes their competitive moat is Lumen’s vast physical network. In fact, they explained that recent PCF deals allow Lumen to expand its physical network concurrently with the almost entirely pre-paid hyperscaler builds, drastically reducing build-out costs. The proximity of Lumen's fiber to the hyperscalers also enables Lumen's multi-cloud gateways.

## Price targets and risks

Valuation: We are Neutral rated on LUMN with a 12-month target price target of \$8.00 reflecting 6.00X NTM+1Y EBITDA.

Key risks: Upside risks: (1) Lumen could execute better on cost takeouts, driving margins, and EBITDA higher than consensus forecasts; (2) Revenue stabilization could come sooner than expected and this, coupled with improved margins, could drive significant upside to EBITDA and FCF forecasts; (3) A significant change in capital structure could be a material positive for the equity. Downside risks: (1) Lumen could find that incremental cost takeout opportunities are more difficult to achieve than currently expected; (2) Business fiber's structural headwinds may continue to limit Lumen's ability to turnaround revenue for longer; (3) Lumen could encounter fiercer competition from industry peers for incremental private connectivity fabric deals, limiting its ability to restructure.

## Disclosure Appendix

## Reg AC

I, Michael Ng, CFA, hereby certify that all of the views expressed in this report accurately reflect my personal views about the subject company or companies and its or their securities. I also certify that no part of my compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Michael Ng, CFA GS & Co. LLC, Zorayda Montemayor GS & Co. LLC, Lindsey Shema GS & Co. LLC.

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

## Rating and pricing information

Lumen Technologies Inc. (Neutral, \$8.43).

## Financial advisory disclosure

GS and/or one of its affiliates is acting as a financial advisor in connection with an announced strategic matter involving the following company or one of its affiliates: LUMEN TECHNOLOGIES, INC.

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS has received compensation for investment banking services in the past 12 months: Flexential Corp.

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Flexential Corp.

GS had an investment banking services client relationship during the past 12 months with: Flexential Corp.

The rating(s) for Lumen Technologies Inc. is/are relative to the other companies in its/their coverage universe: AT&T Inc., Apple Inc., Arista Networks Inc., Axon Enterprise Inc., Blend Labs, Celestica Inc., Charter Communications Inc., Cisco Systems Inc., Cogent Communications Holdings, Comcast Corp., Compass Inc., Dell Technologies Inc., Digital Realty Trust Inc., Equinix Inc., F5 Inc., HP Inc., Hewlett Packard Enterprise Co., IREN Ltd., Ingram Micro, Lumen Technologies Inc., NetApp Inc., Opendoor Technologies Inc., Optimum Communications Inc., Penguin Solutions Inc., Stagwell Inc., Super Micro Computer Inc., T-Mobile US Inc., TD SYNNEX Corp., Verizon Communications, Versant Media Group, Walt Disney Co., Zillow Group

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS beneficially owned 1% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the month end preceding this report: Lumen Technologies Inc. (\$8.43)

GS has received compensation for investment banking services in the past 12 months: Flexential Corp. and Lumen Technologies Inc. (\$8.43)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Flexential Corp. and Lumen Technologies Inc. (\$8.43)

GS had an investment banking services client relationship during the past 12 months with: Flexential Corp. and Lumen Technologies Inc. (\$8.43)

GS had a non-securities services client relationship during the past 12 months with: Lumen Technologies Inc. (\$8.43)

GS makes a market in the securities or derivatives thereof: Lumen Technologies Inc. (\$8.43)

GS holds a position greater than U.S. \$15 million (or equivalent) in the debt or debt instruments of: Lumen Technologies Inc. (\$8.43)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

Price target and rating history chart(s)  
![](images/80da1f066e287cf79d6f25c353a9ce2a5b45698c51851f5fd1b2d5ac699ca7d8.jpg)

<details>
<summary>line chart</summary>

| Date | Stock Price | Index Price | Rating |
| --- | --- | --- | --- |
| Dec 7 | ~1.5 | ~4,000 | N |
| Aug 6 | ~4.5 | ~5,000 | CS |
| Jun 13, 2024 | ~5.5 | ~5,500 | NA |
| Jul 1, 2024 | ~7.25 | ~6,500 | S from NA |
| Jun 13, 2024 | ~8.0 | ~7,000 | NA |
| Jul 1, 2024 | ~9.0 | ~6,500 | NA |
| Sep 2, 2025 | ~10.0 | ~6,000 | NA |
| Oct 2024 | ~11.0 | ~5,500 | NA |
| Nov 2024 | ~12.0 | ~5,000 | NA |
| Dec 2024 | ~13.0 | ~4,500 | NA |
| Jan 2025 | ~14.0 | ~4,000 | NA |
| Feb 2025 | ~13.5 | ~4,500 | NA |
| Mar 2025 | ~13.0 | ~5,000 | NA |
| Apr 2025 | ~12.5 | ~5,500 | NA |
| May 2025 | ~12.0 | ~6,000 | NA |
| Jun 2025 | ~11.5 | ~6,500 | NA |
| Jul 2025 | ~11.0 | ~7,000 | NA |
| Aug 2025 | ~10.5 | ~6,500 | NA |
| Sep 2025 | ~10.0 | ~6,000 | NA |
| Oct 2025 | ~9.5 | ~5,500 | NA |
| Nov 2025 | ~9.0 | ~5,000 | NA |
| Dec 2025 | ~8.5 | ~4,500 | NA |
| Jan 2026 | ~8.0 | ~4,000 | NA |
| Feb 2026 | ~7.5 | ~3,500 | N

[中间内容因长度限制已省略]

including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors.

Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
