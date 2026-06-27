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
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`GS`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
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
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

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
# Europe Wind Manufacturers: US orders continue to progress, adding upside risk to profit outlook

Yesterday evening, Vestas announced it had received orders totaling 869 MW in the US for undisclosed onshore wind projects. This comes without full policy certainty over Section 232. The US onshore market continues to show signs of gradual recovery, with Vestas having secured 1.5 GW of orders so far in Q2 from the US, and 5.2 GW of orders in the trailing 4 quarters. Nordex has also received three firm orders totaling 0.5 GW, in addition to the 1.1 GW conditional order received in H2 2025. Nordex aims to return to its previous US market share which was c.20%.

Exhibit 1: Nordex had started to see a pick-up in orders over the last 12 months, helping to reach its US market share ambitions Vestas and Nordex Announced US Onshore Orders (GW)

Vestas and Nordex Announced US Onshore Orders (GW)

![](images/ec01662c7d85a9bb8b9f24fd94d551fe7a99d6185835b6fee9a563f54f44c941.jpg)  
Source: Company data, GS Global Investment Research

This is while rising power demand, less competition and rising equipment costs/waiting times (re-shoring) – coupled with a higher cost of capital – have supported a strong increase in PPA prices from c.\$30/MWh in 2020-21 to above \$70/MWh currently in the US. Better pricing has been translating into higher returns in US renewables.

Ajay Patel  
+44(20)7552-1168 | ajay.patel@gs.com  
GS International

Lawrence Lavizani +44(20)7051-1060 | lawrence.lavizani@gs.com GS International

Alberto Gandolfi  
+39(02)8022-0157 | alberto.gandolfi@gs.com GS Bank Europe SE - Milan branch

Exhibit 2: US PPA prices have gone up significantly from \$30/MWh in 2020-21 to c.\$70/MWh currently
Evolution of PPA prices in the US over 2020-26 (\$/MWh)  
![](images/20b72199646c6a7bcb3e25a2d1b6efa4d66bdd58700324aea30392cdacb1f470.jpg)  
Source: LevelTen

We see the contribution of US orders as an upside risk to our estimates, which do not include sizeable US additions to reflect the increased policy uncertainty. We remain Buy rated on both names.

## Vestas: Buy, 12m PT of Dkr236

## Investment Thesis, Valuation and Key Risks

We are Buy-rated on Vestas. In our view, Vestas is the best-positioned company in our wind manufacturer coverage, set to benefit from rising wind installation demand, with strong fundamentals (cash flow generation, growth, balance sheet) owing to its geographical diversification and scale. We expect margin expansion over FY 2026, de-risking of the offshore ramp up and a stronger picture for volume growth through higher order intake. We forecast Vestas to deliver 90% of its medium-term target in FY 2027 largely driven by the offshore business reaching break-even. With Vestas reaching peak offshore wind capital expenditure, we see FCF expansion into FY 2027. Combined with targets for capital structure (between +1x and -1x net debt to EBITDA through-the-cycle) and shareholder returns (at least 40% payout for dividends & buybacks), we expect a step up in returns of value over the coming years. Our estimates assume €5bn in cumulative buybacks between FY 2026 and FY 2030. We expect further improvement in margins and higher cash returns which, combined with an uptick in onshore US and German orders into this year, sets the stage for a much stronger medium-term outlook and we expect the re-rating to continue.

We are Buy rated on Vestas with a 12-month price target of Dkr236. Our valuation methodology (both DCF and M&A) reflects ex-IRA linked US installations. Our valuation methodology is based on a combination of a DCF (85% weighting, Dkr213/share) and an M&A valuation (15% weighting, Dkr364/share). Our DCF-based valuation equates to a target multiple of c.10x 2030E EV/EBIT. For our DCF valuation, we use a 7.8% post-tax WACC in both the medium and long term. Our M&A valuation is derived by applying a

22x multiple to 2030E EBIT (on an ex-IRA growth basis) discounted back to 2026E. Our M&A multiple is based on the second-quartile median average M&A multiple for the Industrials sector in Western Europe over the last ten years. We apply the target multiple to 2030E earnings to capture the growth trajectory of the company.

Key downside risks to our view and price target include a decline in global volumes in onshore/offshore wind that would likely negatively impact order intake; lower US installations; the absence of M&A in the wind sector that could make our M&A component less meaningful; and a significant decline in commodity prices that would likely make wind less profitable vs. thermal technologies.

## Nordex: Buy, 12m PT of €53.2

## Investment Thesis, Valuation & Risks

Nordex is benefiting from the same tailwinds we see driving the broader onshore wind turbine industry. At the top line, improved pricing alongside order growth has supported a recovery of margins. Combined, this creates a picture of higher profits and a stronger balance sheet. We see this translating to higher returns of value over time. This could be used for dividends, buybacks, reserves and for investment into the businesses. We expect further improvement in margins and higher cash returns which, combined with an uptick in onshore US and German orders into this year, sets the stage for the company to achieve its medium-term outlook, and we expect the strong share performance to continue.

We are Buy rated on Nordex with a 12-month price target of €53.2. Our price target is based on a DCF valuation, for which we use a 7.9% post-tax WACC in the medium and long term.

Key downside risks to our investment thesis and price target include lower global volumes, changes in government policy, and a decline in commodity prices.

## Disclosure Appendix

## Reg AC

We, Ajay Patel, Lawrence Lavizani and Alberto Gandolfi, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Ajay Patel GS International, Lawrence Lavizani GS International, Alberto Gandolfi GS Bank Europe SE - Milan branch.

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

The rating(s) for Nordex SE and Vestas Wind Systems A/S is/are relative to the other companies in its/their coverage universe: Acciona Energia, Centrica, Drax Group, E.ON, EDP Renovaveis SA, Elia Group, Enagas, Endesa SA, Enel SpA, Energias de Portugal, Engie, Fortum OYJ, Iberdrola SA, National Grid Plc, Naturgy Energy Group, Nordex SE, Orsted A/S, Pennon Group, Public Power Corp., RWE, Redeia, SSE Plc, Severn Trent Plc, Siemens Energy, Snam SpA, Solaria, Terna, United Utilities Group, Veolia Environnement, Vestas Wind Systems A/S

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS has received compensation for investment banking services in the past 12 months: Nordex SE (€43.70)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Nordex SE (€43.70) and Vestas Wind Systems A/S (Dkr170.15)

GS had an investment banking services client relationship during the past 12 months with: Nordex SE (€43.70) and Vestas Wind Systems A/S (Dkr170.15)

GS has managed or co-managed a public or Rule 144A offering in the past 12 months: Nordex SE (€43.70)

Distribution of ratings/investment banking relationships GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment

banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/726d163e7bb787fdb4a7927793096607cf45dae29b257075323ad2b4a01f816b.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/8f48361d0d32630ee04bec2691ab305e829efabccaa8bf307b28f938c8679edb.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s)

Nordex SE (NDXG.DE)

## Vestas Wind Systems A/S (VWS.CO)

<table><tr><td>Date of report</td><td>Target price (€)</td><td>Closing price (€)</td><td>Date of report</td><td>Target price (Dkr)</td><td>Closing price (Dkr)</td></tr><tr><td>27-Apr-26</td><td>53.20</td><td>47.52</td><td>06-May-26</td><td>236.00</td><td>193.65</td></tr><tr><td>13-Apr-26</td><td>49.60</td><td>45.50</td><td>16-Feb-26</td><td>220.00</td><td>155.95</td></tr><tr><td>27-Feb-26</td><td>46.10</td><td>43.12</td><td>07-Jan-26</td><td>203.00</td><td>186.00</td></tr><tr><td>07-Jan-26</td><td>34.50</td><td>33.10</td><td>07-Nov-25</td><td>200.00</td><td>151.60</td></tr><tr><td>04-Nov-25</td><td>31.90</td><td>26.00</td><td>14-Aug-25</td><td>196.00</td><td>113.25</td></tr><tr><td>28-Jul-25</td><td>25.10</td><td>20.16</td><td>06-May-25</td><td>195.00</td><td>96.46</td></tr><tr><td>30-Apr-25</td><td>23.00</td><td>16.49</td><td>05-Feb-25</td><td>197.00</td><td>109.50</td></tr><tr><td>07-Mar-25</td><td>22.60</td><td>15.96</td><td>27-Jan-25</td><td>205.00</td><td>94.96</td></tr><tr><td>27-Jan-25</td><td>20.10</td><td>11.46</td><td>11-Nov-24</td><td>236.00</td><td>102.65</td></tr><tr><td>07-Nov-24</td><td>21.50</td><td>12.29</td><td>15-Aug-24</td><td>259.00</td><td>160.10</td></tr><tr><td>25-Jul-24</td><td>21.10</td><td>13.63</td><td>02-May-24</td><td>274.00</td><td>179.20</td></tr><tr><td>15-May-24</td><td>20.30</td><td>14.98</td><td>13-Feb-24</td><td>270.00</td><td>188.66</td></tr><tr><td>05-Mar-24</td><td>17.50</td><td>11.66</td><td>02-Oct-23</td><td>259.00</td><td>147.08</td></tr><tr><td>28-Jul-23</td><td>15.00</td><td>12.71</td><td></td><td></td><td></td></tr></table>

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain

GS Australia and New Zealand disclosure of interests and a copy of GS' Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for information purposes only and is not, and under no circumstances should be construed as, an advertisement, offering or solicitation by GS & Co. LLC for pu

[中间内容因长度限制已省略]

 impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS.

This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
