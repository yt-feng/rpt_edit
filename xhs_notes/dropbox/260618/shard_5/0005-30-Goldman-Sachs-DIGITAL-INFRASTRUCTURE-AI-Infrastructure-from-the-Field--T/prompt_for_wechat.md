你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`GS`。标题格式建议：`# GS：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

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
| Feb 2026 | ~7.5 | ~3,500 | NA |
| Mar 2026 | ~7.0 | ~3,000 | NA |
| Apr 2026 | ~6.5 | ~2,500 | NA |
| May 2026 | ~6.0 | ~2,000 | NA |
| Jun 2026 | ~5.5 | ~1,500 | NA |
| Jul 2026 | ~5.0 | ~1,000 | NA |
| Aug 2026 | ~4.5 | ~5 | NA |
| Sep 2026 | ~4.0 | ~4 | NA |
| Oct 2026 | ~3.5 | ~3 | NA |
| Nov 2026 | ~3.0 | ~2 | NA |
| Dec 2026 | ~2.5 | ~1 | NA |
| Jan 2027 | ~2.0 | ~1 | NA |
| Feb 2027 | ~1.5 | ~1 | NA |
| Mar 2027 | ~1.0 | ~1 | NA |
| Apr 2027 | ~1.5 | ~1 | NA |
| May 2027 | ~2.0 | ~1 | NA |
| Jun 2027 | ~2.5 | ~1 | NA |
| Jul 2027 | ~3.0 | ~1 | NA |
| Aug 2027 | ~3.5 | ~1 | NA |
| Sep 2027 | ~4.0 | ~1 | NA |
| Oct 2027 | ~4.5 | ~1 | NA |
| Nov 2027 | ~5.0 | ~1 | NA |
| Dec 2027 | ~5.5 | ~1 | NA |
| Jan 2028 | ~6.0 | ~1 | NA |
| Feb 2028 | ~6.5 | ~1 | NA |
| Mar 2028 | ~7.0 | ~1 | NA |
| Apr 2028 | ~7.5 | ~1 | NA |
| May 2028 | ~8.0 | ~1 | NA |
| Jun 2028 | ~8.5 | ~1 | NA |
| Jul 2028 | ~9.0 | ~1 | NA |
| Aug 2028 | ~9.5 | ~1 | NA |
| Sep 2028 | ~10.0 | ~1 | NA |
| Oct 2028 | ~11.0 | ~1 | NA |
| Nov 2028 | ~12.0 | ~1 | NA |
| Dec 2028 | ~13.0 | ~1 | NA |
| Jan 2029 | ~14.0 | ~1 | NA |
| Feb 2029 | ~13.5 | ~1 | NA |
| Mar 2029 | ~13.0 | ~1 | NA |
| Apr 2029 | ~12.5 | ~1 | NA |
| May 2029 | ~12.0 | ~1 | NA |
| Jun 2029 | ~11.5 | ~1 | NA |
| Jul 2029 | ~11.0 | ~1 | NA |
| Aug 2029 | ~10.5 | ~1 | NA |
| Sep 2029 | ~11.5 | ~1 | NA |
| Oct 2029 | ~13.5 | ~1 | NA |
| Nov 2029 | ~14.5 | ~1 | NA |
| Dec 2029 | ~15.5 | ~1 | NA |
</details>

The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

Target price history table(s)
Lumen Technologies Inc. (LUMN)

<table><tr><td>Date of report</td><td>Target price ($)</td><td>Closing price ($)</td></tr><tr><td>06-May-26</td><td>8.00</td><td>9.81</td></tr><tr><td>04-Feb-26</td><td>7.25</td><td>6.63</td></tr><tr><td>06-Jan-26</td><td>5.50</td><td>8.30</td></tr><tr><td>31-Oct-25</td><td>5.00</td><td>10.28</td></tr><tr><td>03-Oct-25</td><td>4.60</td><td>6.56</td></tr><tr><td>02-Sep-25</td><td>4.10</td><td>4.79</td></tr><tr><td>06-Nov-24</td><td>5.00</td><td>9.02</td></tr><tr><td>04-Oct-24</td><td>4.50</td><td>6.78</td></tr><tr><td>07-Aug-24</td><td>4.00</td><td>6.63</td></tr><tr><td>01-Jul-24</td><td>1.00</td><td>1.11</td></tr><tr><td>09-Nov-23</td><td>1.50</td><td>1.18</td></tr><tr><td>02-Aug-23</td><td>3.00</td><td>1.79</td></tr></table>

Price targets shown in table(s) are unadjusted for cor

[中间内容因长度限制已省略]

 impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

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
