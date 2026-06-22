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
# China Consumer Durables: EU anti-dumping investigation on Chinese RLMs to continue but not imposing provisional duties at this time

## The News

The European Commission initiated an anti-dumping investigation on robotic lawn mowers from China in Nov 2025 in response to a complaint (link) by Husqvarna (not covered), a global leader in RLM etc. According to the notice, the EU may: 1) impose provisional measures (e.g., provisional anti-dumping duties) in no later than seven months of the announcement (June 19, 2026); 2) conclude the investigation within one year (Nov 19, 2026), but no more than 14 months upon the announcement (Jan 19, 2027). On Jun 19, 2026, the EU announced that it will continue the anti-dumping investigation rather than imposing provisional measures at the current stage, given the technical complexity of the case (link).

## Our view

While we take no view on the EU's decision, we believe investors could view the update positively with the decision to hold off on imposing provisional measures on Chinese robotic lawn mowers (RLM) players suggesting limited near-term impact to sales performance and margins. In our previous analysis (link), we noted that most Chinese players plans were to ship a majority of their 2026 sales target to Europe by 1H26 with expectations to start to bear the impact of potential provisional anti-dumping duties from June 2026. In light of the recent announcement, the applicable tariff rate will probably remain unchanged in 2026, which should help preserve Chinese RLM players' near-term margins and market competitiveness (considering they may not need to increase prices to mitigate tariff impacts). In the meantime, we continue to expect Chinese RLM players to exert discipline in terms of pricing strategy, at least until there is more clarity around any potential impact from the investigation.

The above said, uncertainty remains as the EU continues the anti-dumping investigation and may still decide to impose an anti-dumping tariff duty with retrospective effects upon completion. However, the current announcement leaves a longer time window for Chinese players to prepare for potential duties, such as relocating manufacturing capacity overseas. We note that manufacturing costs generally increase by 10%-20% in early stage relocation due to less efficient labor productivity and supply chain. A longer preparation time could help improve efficiency in the event of a relocation, though not entirely eliminating the gap.

In our coverage, we think shares of Ninebot, Ecovacs and Roborock could react positively to the announcement with Ninebot likely being the largest beneficiary

+86(21)2401-8922 |
nicolas.yi@goldmansachs.cn
GS (China) Securities
Company Limited

Cecilia Tang
+86(21)2401-8738 |
cecilia.tang@goldmansachs.cn
GS (China) Securities
Company Limited

given its higher exposure to robotic lawn mowers (9% of total revenue and a higher profits contribution in 2025). We continue to believe that leading brands including Ninebot (Buy) are better positioned (vs. small players) to cope with any potential tariff impacts due to the higher pricing position of their products, and their ability to adjust production globally if needed. Specifically for Ninebot, the EU anti-dumping investigation has been one of the overhangs for its valuation, and we believe the latest announcement could help ease investor sentiment at least in the near term.

## Investment Thesis, Valuation and Risks

## Ninebot Ltd (689009.SS, Buy)

Investment thesis: We expect Ninebot to grow as an emerging global leader in micro-mobility and robotic lawn mowers, driven by: 1) Further market share gain in core domestic E2W with rising membership fee contribution supported by its product R&D strength as smart functions play a more important role in products, together with channel expansion and wider product offerings via its dual-brand; 2) Rapidly growing robotic lawn mower business riding on the structural growth of robotic adoption vs. traditional. We view Ninebot as better positioned to gain share leveraging its comprehensive product portfolio, established brand, and stronger presence in the offline channel; 3) Overseas expansion potential: We see near-term revenue and profits opportunities from E-Bikes in developed markets, benefiting from the rising electrification adoption on policy support and rising consumer preference for environment-friendly products. The fragmented market also leaves room for Chinese players like Ninebot to gain share leveraging its accumulated technology and competitive products. In the mid to long-run, we see substantial revenue potential in emerging markets such as ASEAN countries where there is large ICE 2W ownership, current E2W adoption is low and the electric transition has been ongoing driven by supportive government policies.

Valuation: Our 12-month target price of Rmb62 is based on a 16x exit P/E multiple applied to our 2028E EPS and discounted back to 2027E using a 9.5% cost of equity.

Key risks: 1) Decline in disposable income and consumer confidence from weaker macro conditions; 2) Slower-than-expected product launches or new category expansion; 3) Intensifying competition in domestic/overseas markets; 4) Potential tariffs/anti-dumping duties may reduce profitability; 5) Higher-than-expected raw materials cost.

## Beijing Roborock Technology (688169.SS, Buy)

Investment Thesis: Roborock is a global leader in robotic vacuum cleaners (RVCs) with an expanding product range and channel expansion growth runway. We believe the company is well-placed for continued global market share gains, driven by: 1) further progress in channel expansion especially in overseas markets; 2) enhanced marketing and branding investment; 3) SKU expansion outside of its core RVC products, such as wet dry vacuums and robotic lawn mowers. Since the company adopted a more proactive branding/marketing strategy in 2H24, the company has been gaining share at a faster pace in both overseas and domestic markets. With most of the previous margin drags (i.e., over-investment in new product, US tariff, Europe business model transition, and self-borne subsidies in China) generally lifted, we see favorable risk-reward in the shares on re-rating prospects as the company resumes fast profit growth driven by resilient revenue growth and strong margin recovery.

Valuation: Our 12-m TP of Rmb170 is based on a 18x exit P/E multiple applied to our 2028E EPS and discounted back to 2027E using a 9.5% cost of equity.

Downside risks: 1) intensifying competition in domestic/overseas markets; 2) slower-than-expected product launches or new category expansion; 3) aggressive branding/marketing investment in new products to impact profitability; 4) a decline in disposable income and consumer confidence from weaker macro conditions; 5) potential increase in US tariffs may reduce US business profitability.

## Ecovacs Robotics Co. (603486.SS, Sell)

Investment Thesis: Ecovacs, the leading cleaning appliances company by market share in China, has strengths in a comprehensive product portfolio and distribution network (both offline and online) leveraging a dual-brand strategy (Ecovacs for RVC and Tineco for wet-dry vacuums and other small appliances). While we remain positive on 1) the long-term potential of cleaning appliances especially RVC in both the domestic and overseas markets and 2) Ecovacs' market share gain potential overseas, we are cautious about competition for cleaning appliances in the domestic market, especially for wet-dry vacuums, as well as the challenges in defending its market share without hurting margins. We see less favorable risk-reward for Ecovacs vs. its peers and are Sell rated.

Valuation: Our 12-m target price of Rmb55 is based on an exit multiple of 17x applied to our 2028E EPS and discounted back to 2027E using a 9.5% cost of equity.

Upside risks: 1) faster demand recovery supported by better-than-expected macro conditions; 2) better-than-expected product development/expansion; 3) easing competition.

## Disclosure Appendix

## Reg AC

We, Nicolas Yi and Cecilia Tang, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Contributing Authors: Nicolas Yi GS (China) Securities Company Limited, Cecilia Tang GS (China) Securities Company Limited.

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

The rating(s) for Beijing Roborock Technology, Ecovacs Robotics Co. and Ninebot Ltd is/are relative to the other companies in its/their coverage universe: Appotronics Corporation Ltd., Bear Electric Appliance Co., Beijing Roborock Technology, Chengdu XGimi Technology Co., Ecovacs Robotics Co., Gongniu Group, Gree Electric Appliances Inc., Guangdong Xinbao Electrical, Haier Smart Home Co. (A), Haier Smart Home Co. (H), Hangzhou Robam Appliances, Hisense Home Appliances Group (A), Hisense Home Appliances Group (H), Jason Furniture Hangzhou Co., Joyoung Co., Man Wah Holdings, Midea Group (A), Midea Group (H), Ninebot Ltd, Oppein Home Group, Suofeiya Home Collection Co., Zhejiang Supor Co.

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS has received compensation for investment banking services in the past 12 months: Beijing Roborock Technology (Rmb97.27)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Beijing Roborock Technology (Rmb97.27), Ecovacs Robotics Co. (Rmb53.08) and Ninebot Ltd (Rmb33.94)

GS had an investment banking services client relationship during the past 12 months with: Beijing Roborock Technology (Rmb97.27), Ecovacs Robotics Co. (Rmb53.08) and Ninebot Ltd (Rmb33.94)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

Price target and rating history chart(s)  
![](images/00f02bc3742a39456e4dfb3d8050884d12ab6447f562fb9455ea14fcb5c49f56.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/b5b990feedbe553a5980f857ef5e29bf2af91f9bcfde43bb48e1bb0bd6e38d1d.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

Target price history table(s)

## Ninebot Ltd (689009.SS)

<table><tr><td>Date of report</td><td>Target price (Rmb)</td><td>Closing price (Rmb)</td></tr><tr><td>02-Apr-26</td><td>62.00</td><td>43.48</td></tr></table>

Ecovacs Robotics Co. (603486.SS)

<table><tr><td>Date of report</td><td>Target price (Rmb)</td><td>Closing price (Rmb)</td></tr><tr><td>27-Apr-26</td><td>55.00</td><td>67.80</td></tr><tr><td>15-Apr-26</td><td>49.00</td><td>62.61</td></tr><tr><td>02-Feb-26</td><td>56.00</td><td>71.42</td></tr><tr><td>13-Jan-26</td><td>60.00</td><td>83.41</td></tr><tr><td>27-Oct-25</td><td>56.00</td><td>93.85</td></tr><tr><td>19-Aug-25</td><td>51.00</td><td>89.20</td></tr><tr><td>15-Jul-25</td><td>45.00</td><td>70.43</td></tr><tr><td>19-May-25</td><td>40.00</td><td>57.42</td></tr><tr><td>28-Apr-25</td><td>37.00</td><td>49.68</td></tr><tr><td>08-Apr-25</td><td>34.00</td><td>46.22</td></tr><tr><td>03-Mar-25</td><td>39.00</td><td>57.90</td></tr><tr><td>16-Jan-25</td><td>44.00</td><td>44.85</td></tr><tr><td>03-Sep-24</td><td>42.00</td><td>42.00</td></tr><tr><td>08-May-24</td><td>40.00</td><td>49.25</td></tr><tr><td>05-Mar-24</td><td>32.00</td><td>38.39</td></tr><tr><td>31-Jan-24</td><td>34.00</td><td>31.97</td></tr><tr><td>31-Oct-23</td><td>39.00</td><td>43.16</td></tr><tr><td>28-Aug-23</td><td>60.00</td><td>60.26</td></tr></table>

Beijing Roborock Technology (688169.SS)

<table><tr><td>Date of report</td><td>Target price (Rmb)</td><td>Closing price (Rmb)</td></tr><tr><td>27-Apr-26</td><td>170.00</td><td>118.68</td></tr><tr><td>15-Apr-26</td><td>180.00</td><td>113.62</td></tr><tr><td>13-Jan-26</td><td>210.00</td><td>158.53</td></tr><tr><td>03-Nov-25</td><td>180.00</td><td>156.97</td></tr><tr><td>18-Aug-25</td><td>170.00</td><td>209.04</td></tr><tr><td>15-Jul-25</td><td>150.00</td><td>163.70</td></tr><tr><td>19-May-25</td><td>220.00</td><td>156.99</td></tr><tr><td>07-Apr-25</td><td>210.00</td><td>134.34</td></tr><tr><td>28-Feb-25</td><td>240.00</td><td>170.71</td></tr><tr><td>16-Jan-25</td><td>250.00</td><td>169.50</td></tr><tr><td>05-Nov-24</td><td>240.00</td><td>166.59</td></tr><tr><td>29-Aug-24</td><td>320.00</td><td>157.13</td></tr><tr><td>09-Aug-24</td><td>330.00</td><td>144.89</td></tr><tr><td>27-Jun-24</td><td>540.00</td><td>200.61</td></tr><tr><td>30-Apr-24</td><td>520.00</td><td>216.85</td></tr><tr><td>28-Mar-24</td><td>468.00</td><td>174.45</td></tr><tr><td>05-Mar-24</td><td>470.00</td><td>174.34</td></tr><tr><td>24-Jan-24</td><td>450.00</td><td>146.94</td></tr><tr><td>31-Oct-23</td><td>418.00</td><td>161.22</td></tr><tr><td>08-Sep-23</td><td>364.00</td><td>155.39</td></tr><tr><td>22-Aug-23</td><td>285.00</td><td>130.62</td></tr></table>

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting

[中间内容因长度限制已省略]

m impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
