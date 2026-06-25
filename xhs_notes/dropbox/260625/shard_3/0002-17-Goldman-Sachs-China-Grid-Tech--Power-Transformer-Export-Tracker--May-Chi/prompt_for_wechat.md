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
# China Grid Tech: Power Transformer Export Tracker: May China transformer total exports picked up to $72\%$ yoy, with exports to US at

In this latest Power Transformer Export Tracker, we provide an update as of May. US transformer PPI remained stable at an elevated level, while China's export price showed some weakness in the 220-330MVA segment, with March-May rolling average pricing down $29\%$ yoy. That said, pricing has largely remained within its normal range since 2024. May total ( $>10$ MVA) transformer export value growth picked up to $72\%$ yoy (vs $27\%$ yoy in April). In particular, transformer exports to the US delivered 114x yoy growth on a low base, or $26\%$ mom (vs $+95\%$ yoy in April).

Jacqueline Du  
+852-2978-1783 |  
jacqueline.du@gs.com  
GS (Asia) L.L.C.

We continue to estimate that the US power transformer demand-local supply gap will narrow from $72\%$ currently to $57\%$ by 2028E, despite many capacity expansion plans announced by local transformer manufacturers, with a new one by Virginia Transformer to expand a greenfield transformer plant in Alabama, US. We still expect the shortage to persist, leaving room for non-traditional suppliers, including those in China.

Key ideas: Sieyuan (Buy), Nari Tech (Buy), Huaming (Neutral): Among Chinese grid technology names, we favor Sieyuan and Nari Tech, while remain Neutral on Huaming. Global transformer lead times remain elevated at around 128 weeks (link), while capacity expansion typically takes 2-3 years. By contrast, Sieyuan can deliver transformers in around 6-9 months, or 24-36 weeks, and expand capacity within roughly one year, supported by China's agile supply chain. Sieyuan has also just announced Phase III transformer factory to support a total production value of up to Rmb9-10bn of annual production value (report link). We like Nari Tech for its exposure to domestic grid capex and rising export potential in converter valves and secondary equipment. Huaming's share price has pulled back $48\%$ from its peak, reflecting normalized expectations that the company will achieve steady, rather than accelerated, overseas market share gains in the absence of an on-load tap changer shortage. We maintain our Neutral rating.

US local power transformer demand/supply gap (%)

![](images/f56d8c428e6f54926a8ed4a1e66e1e7d5c1c6474817fb6d138c82847aaf914b1.jpg)

Exhibit 1: We estimate that US power transformer demand/local supply gap would narrow from 72% to 57% in 2028E; despite China export ASP volatilities, US PPI has stabilized at a high level  
![](images/27862de65f26b3978f1d207f6fbad18eb7a18b4f77e63915674e69e7f2ac73db.jpg)  
China Customs export pricing is on a FOB basis. US local pricing is estimated with a bidding document, then applied with the PPI for transformers of all power range, not 220-300MVA specifically.  
Source: Company data, Expert estimate, FRED, State Grid, China Customs, GS Global Investment Research  
Exhibit 2: China total transformer export value growth picked up to $72\%$ yoy in May (vs $27\%$ in April)

![](images/8f864b36acbd7064ee90ff102d4fe06d57e283cc22e0f16958f4cb87d6221cb9.jpg)  
Source: China Customs, Data compiled by GS Global Investment Research  
Exhibit 3: China transformer export value to the US grew 114x yoy on a low base, or +26% mom (vs +95% yoy in April)

![](images/4e84a64c27170c62ca1cfd5085aebf532d2f4dafe7e29738587c359cb2b86938.jpg)  
Source: China customs, Data compiled by GS Global Investment Research

Pricing remained stable in US: US transformer PPI has remained stable since Oct 2025 at a high level, at $3.9\%$ yoy in May. Power transformers had an earlier price appreciation than other categories (due to renewable energy penetration prior to AIDC), while switchgear has caught up in pricing appreciation and turbine pricing also inched up in recent months, reaching $12\%$ yoy growth in May.

Among China exports to US pricing, it's hard to observe a trend in 10-220MVA category given the wide range. And 220-330MVA segment transformers' past three month rolling average price in March-May saw a decline by $29\%$ , but was largely in the normal pricing range since 2024. Key raw materials for transformer, GOES, saw price inching down.

Exhibit 4: Export transformer to the US market has seen a relatively volatile ASP in 10-220MVA due to volatile mix change...

![](images/261ef9ec480b877c09a6a964db24f074c237575b0bd96bbb6a87763232cdc103.jpg)  
Source: China Customs, Data compiled by GS Global Investment Research  
Exhibit 6: US PPI for the power and specialty transformer price remained stable at a high level (3.9% yoy in May)  
US PPI for Electric Power and Specialty Transformer vs CPI (Jan 2018 indexed to 100)
US PPI for electrical equipment and specialty power transformer US CPI

![](images/211113fbf7e2dc230f8efed75bd467cc2eacf6ee349acfd62349ee765deb2824.jpg)  
Source: FRED, Data compiled by GS Global Investment Research

Exhibit 5: Transformer in the 220-330MVA category saw March-May rolling average pricing -29% yoy  
![](images/2f116ee849f5bbfa4dd9b58d180a11b60eb3fd1a2fc96e6d39594c2362a311a1.jpg)  
Source: China Customs, Data compiled by GS Global Investment Research

Exhibit 7: US power and specialty transformers' PPI rose earlier than other product categories, while switchgear pricing has caught up in recent months (+12% yoy in May)  
![](images/6cf1c5a09f6e3aa96d992cf96e15ced34919c82071fcf9bc8f36965d325ce4a7.jpg)  
Source: FRED, Data compiled by GS Global Investment Research  
Exhibit 8: Key raw materials for transformer, GOES, saw prices inch down  
Price index for transformer key materials (Jan 2018 indexed to 100)

![](images/1d127edccf1f01c6bf644abeb4f9cadebc68497341b890019da61af4c02a812c.jpg)  
Source: TDEurope, Wind, Data compiled by GS Global Investment Research

China total (>10MVA) transformer export value picked up to $72\%$ in May (vs $27\%$ yoy in April), which was in particular driven by Africa at 252% yoy (18% contribution to total export), Middle East at 152% yoy (23% contribution to total export), Americas at 113% yoy (21% contribution), Asia at 35% yoy (23% contribution to total export), Europe at -12% yoy (15% contribution).

In particular, transformer export value to US grew 114x yoy in May on a low base or +26% mom (vs 95% yoy in April). Export breakdown by voltage level was 52% from 10-220MVA segment, 19% from 220-330MVA segment, and 29% from 400-500MVA segment.

For other categories, China electronic meter export value was -11% yoy in May (vs flat in April); China circuit breaker (>72.5kV) export value was -16% yoy in May (vs 77% yoy in April).

Exhibit 9: China total transformer export value picked up to $72\%$ yoy in May (vs $27\%$ in April)  
![](images/cd25fd8e9b6177203cb0f1b7025c2672bbab21134e3609f12cc8fc030500b99b.jpg)  
Source: China Customs, Data compiled by GS Global Investment Research  
Exhibit 10: China transformer export value to the US grew 114x yoy on a low base, or $26\%$ mom (vs $+95\%$ yoy in April)

![](images/3548e61a59d50bb4b86ed55e1943c0b408f97907632ee8b299ae2cbf2529955b.jpg)  
Source: China customs, Data compiled by GS Global Investment Research

Exhibit 11: China electronic meter export value was -11% yoy in May (vs flat in April)  
![](images/c440d15c821723e3051c273eba638daedbe1b2d18fa21b8216a38ea7a6e874dc.jpg)  
Source: China customs, Data compiled by GS Global Investment Research

Exhibit 12: China circuit breaker (>72.5kV) export value was -16% yoy in May (vs 77% yoy in April)  
![](images/7d33bd7d7b29a14c6e9a226b6398ade8dd0d5c32c1a0d3040639639e6233d4b8.jpg)  
Source: China customs, Data compiled by GS Global Investment Research  
The author would like to thank Zhou Li, Hao Chen, Zhihan Ye, and Junfang Zhang for their contributions to this report.

## Disclosure Appendix

## Reg AC

I, Jacqueline Du, hereby certify that all of the views expressed in this report accurately reflect my personal views about the subject company or companies and its or their securities. I also certify that no part of my compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Jacqueline Du GS (Asia) L.L.C..

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

Huaming (Neutral, Rmb20.40), NARI Technology (Buy, Rmb22.95) and Sieyuan Electric (Buy, Rmb187.00)

The rating(s) for NARI Technology and Sieyuan Electric is/are relative to the other companies in its/their coverage universe: AVIC Jonhon, Best, Bochu, CRRC Corp. (A), CRRC Corp. (H), Centre Testing Intl Group, Estun Automation Co.(A), Estun Automation Co.(H), Faratronic, Haitian International Holdings, Han's Laser Technology, HangKe Technology, Hongfa Technology, Huaming, Kehua Data Co., Lead Intelligent (A), Lead Intelligent (H), Leader Harmonious Drive Systems Co., Luster LightTech Co., Megmeet, Moons' Electric, NARI Technology, Nantong Jianghai Capacitor Co., OPT Machine Vision Tech Co., Sanhua Intelligent Controls (A), Sanhua Intelligent Controls (H), Shanghai Baosight Software, Shenzhen Envicool Technology, Shenzhen Inovance Technology Co., Shenzhen Kstar Science & Tech, Shuanghuan Driveline, Sieyuan Electric, Techtronic Industries, Wuhan Raycus Fiber Laser Tech, Yiheda Automation, Yingliu, Zhejiang Supcon Technology Co., Zhuzhou CRRC Times Electric Co. (A), Zhuzhou CRRC Times Electric Co. (H)

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS beneficially owned 1% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the month end preceding this report: Sieyuan Electric (Rmb187.00)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Sieyuan Electric (Rmb187.00)

GS had an investment banking services client relationship during the past 12 months with: Sieyuan Electric (Rmb187.00)

There are no company-specific disclosures for: NARI Technology (Rmb22.95)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/9ee97455000dbbaa0d63315db5abe150677a9904cdc1bbe584df543c3d5dceaf.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/6e96de14c72f996ffe4916a946b086cee22bacb4d44b56f9cb9574e8af517ba0.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s)

## NARI Technology (600406.SS)

Sieyuan Electric (002028.SZ)

<table><tr><td>Date of report</td><td>Target price (Rmb)</td><td>Closing price (Rmb)</td><td>Date of report</td><td>Target price (Rmb)</td><td>Closing price (Rmb)</td></tr><tr><td>05-May-26</td><td>31.50</td><td>25.97</td><td>03-Mar-26</td><td>223.90</td><td>219.40</td></tr><tr><td>17-Apr-26</td><td>29.20</td><td>26.81</td><td>19-Jan-26</td><td>195.60</td><td>204.49</td></tr><tr><td>24-Feb-26</td><td>29.90</td><td>26.86</td><td>13-Jan-26</td><td>194.60</td><td>162.33</td></tr><tr><td>22-Dec-25</td><td>30.10</td><td>22.96</td><td></td><td></td><td></td></tr><tr><td>27-Aug-25</td><td>30.20</td><td>22.00</td><td></td><td></td><td></td></tr><tr><td>29-Apr-25</td><td>31.80</td><td>22.21</td><td></td><td></td><td></td></tr><tr><td>20-Jan-25</td><td>29.00</td><td>22.87</td><td></td><td></td><td></td></tr><tr><td>13-Sep-23</td><td>32.00</td><td>22.76</td><td></td><td></td><td></td></tr><tr><td>11-Aug-23</td><td>27.92</td><td>23.59</td><td></td><td></td><td></td></tr></table>

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; $1\%$ or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Austr

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
