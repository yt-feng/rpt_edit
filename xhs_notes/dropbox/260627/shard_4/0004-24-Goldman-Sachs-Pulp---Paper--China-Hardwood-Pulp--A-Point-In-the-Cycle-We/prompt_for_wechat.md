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
# Pulp & Paper: China Hardwood Pulp: A Point In the Cycle We Have Seen Many Times

We have been arguing that we see hardwood prices at around \$600/t as being close to peak through the cycles (link), as around and above those levels China integrated paper producers are more competitive and tend to gain market share from non integrated. So that reduces market pulp demand and also pricing power for pulp and paper sellers.

Hardwood prices have been flat in China since late 1Q, but our channel checks note that volumes sold in April-May have been below 50% of regular volumes. And while producers had limited availability due to downtime in the quarter, sales were below available volumes and sellers inventories have been trending higher. With June being the last month of the quarter, pressure to sell increases and buyers are in no rush to place orders.

RISI reports that Arauco and CMPC have cut offers by \$20/t to around \$580/t, but our conversations suggest this is not enough to attract significant buying. So our view is that prices need to fall further for buying to be sufficient to a point where full volumes can be allocated.

We have seen the same situation in pretty much all bear cycles, and sellers usually decide to hold back volumes to temporarily limit price declines in China as this would preserve benchmark prices in other regions, including Europe and the US. But we see as inevitable that China hardwood prices continue to fall and that eventually will impact other major regions, specially as current net prices are at least \$50/t higher outside of China, a situation that we view as unsustainable.

With new pulp capacity coming online in China and in Indonesia by YE, expectations are that we will likely trend towards marginal cost before significant buying or production slowdowns stabilize supply/demand and pricing.

China FOEX hardwood imported pulp prices were flat at \$605/t, while domestic resale prices were down by RMB 22-70/t to the equivalent of \$549-556/t. On the softwood side, imported FOEX prices were down by \$12/t to \$641/t, while domestic resale prices declined by RMB 114-155/t w/w, to the equivalent of \$584-616/t.

Marcio Farid  
+55(11)3371-4580 |  
marcio.farid@gs.com  
GS do Brasil CTVM S.A.

Henrique Marques  
+55(11)3371-0778 |  
henrique.marques@gs.com  
GS do Brasil CTVM S.A.

Emerson Vieira
+55(11)3372-0256 |
emerson.vieira@gs.com
GS do Brasil CTVM S.A.

Exhibit 1: Hardwood domestic resale prices vs. Hardwood PIX China price (in USD)  
![](images/ec0682142bed60b2234c32b87f4e9cbe930ada07395cf8ec0d932ed02577f7ed.jpg)  
Source: RISI, GS Global Investment Research

Exhibit 2: Softwood domestic resale prices vs. Softwood PIX China price (in USD)  
![](images/ab2a6ee8930163451d222db27a854a3506221fb6b926e09fd117b606a230484a.jpg)  
Source: RISI, GS Global Investment Research

## Global

Global pulp statistics: May shipments increased 3% m/m but decreased 1% y/y. May's shipments increase was driven by both softwood (+7% m/m) and hardwood (+2% m/m), in line with seasonality. Compared to 2025, the shipments decrease was mainly driven by hardwood (-5% y/y), partially offset by softwood (+4% y/y). Sellers' hardwood inventories increased 3 days m/m to 43 in May. Seller's softwood inventories increased 1 day m/m to 47 days. YTD global shipments are down by 2.5%.

Exhibit 3: Global pulp shipments (kt)  
![](images/389681fa1b804a054d008facb4c10083f2394c65c230b1c3043969a72232ae75.jpg)  
Source: PPPC

Exhibit 4: Global pulp sellers' inventories (days of supply)  
![](images/1be1f67dc37cd7b81a3dae61df2b234ed96aa58040bcc2bdf6a56d9497db3ba6.jpg)  
Source: PPPC

## China

China's pulp imports decreased $10\%$ m/m but increased $4\%$ y/y in May. Total pulp imports reached 2.1 mt in May, mainly on lower imports for softwood $(-20\%$ m/m) and hardwood $(-3\%$ m/m). YTD imports are up $2\%$ .

Exhibit 5: China's hardwood and softwood imports (kt)  
![](images/2a7ba241832c7befe422701150998b5d850583e8250a19263cefb451a2762a69.jpg)  
Source: China Customs

China's woodchips imports decreased $2\%$ m/m and $4\%$ y/y in May. May's imports showed a decrease vs April numbers, likely explained by rising prices and competition with China domestic wood, which reached the highest level since 2023. YTD imports up $8\%$ y/y (+0.5mt). With China wood supply increasing and prices falling, coupled with lower oil/freight rates, we would expect imported chips prices to also follow a negative trend.

Exhibit 6: China woodchip imports (kt) and prices (in RMB/t)  
![](images/2894404bb53d0c21c6ab7beb72207e3714a4fca97bd86bb975be8315ddf69f35.jpg)  
Source: China Customs

## Europe

Essity: Oil relief lifts forecasts, but margin risks persist; Neutral. Our GS Europe consumer products team has updated its view on Essity after oil prices have fallen $30\%$ , easing pressure across petrochemical, energy, and fuel inputs, while pulp prices have continued to edge modestly higher. On balance, they now expect mid-single-digit unit cost inflation in FY26, weighted toward H2 as raw material costs feed through with a lag. In their view, while lower oil alleviates some earnings pressure, it does not eliminate the risk of mounting gross margin headwinds later in the year, which they believe consensus still underappreciates. In terms of prices, although several tissue producers, including Essity, have announced price increases, they expect implementation to lag, as it did during the 2022 inflation cycle. In the

meantime, European producer price data continues to point to manufacturer-level price declines in April and May, while Nielsen data suggests shelf-price deflation is still persisting. More details here.

Latin America  
Exhibit 7: LatAm Pulp & Paper coverage comp table

<table><tr><td rowspan="2">Pulp &amp; Paper Companies</td><td rowspan="2">Ticker</td><td rowspan="2">Country</td><td rowspan="2">M. Cap (US$bn)</td><td rowspan="2">Rating</td><td rowspan="2">Target Price 12-m fwd.</td><td rowspan="2">Price (in LC)</td><td rowspan="2">Upside/Downside</td><td colspan="2">EV/EBITDA</td><td colspan="2">FCF Yield (%)</td><td colspan="2">Dividend Yield (%)</td><td colspan="2">Net Debt / EBITDA</td></tr><tr><td>2026</td><td>2027</td><td>2026</td><td>2027</td><td>2026</td><td>2027</td><td>2026</td><td>2027</td></tr><tr><td>Suzano SA</td><td>SUZB3.SA</td><td>Brazil</td><td>10.9</td><td>Buy</td><td>52.00</td><td>42.00</td><td>23.8%</td><td>6.0x</td><td>5.6x</td><td>8.7%</td><td>16.0%</td><td>2.7%</td><td>3.1%</td><td>3.4x</td><td>3.1x</td></tr><tr><td>Klabin SA</td><td>KLBN11.SA</td><td>Brazil</td><td>4.0</td><td>Neutral</td><td>18.00</td><td>17.05</td><td>5.6%</td><td>7.2x</td><td>7.1x</td><td>3.6%</td><td>7.9%</td><td>6.4%</td><td>6.7%</td><td>3.5x</td><td>3.5x</td></tr><tr><td>Empresas COPEC SA</td><td>COPEC.SN</td><td>Chile</td><td>8.2</td><td>Sell</td><td>5,743</td><td>5,802</td><td>(1.0%)</td><td>7.8x</td><td>8.5x</td><td>-26.4%</td><td>-20.6%</td><td>2.6%</td><td>1.8%</td><td>4.5x</td><td>5.2x</td></tr><tr><td>Dexco SA</td><td>DXCO3.SA</td><td>Brazil</td><td>0.8</td><td>Neutral</td><td>5.60</td><td>5.02</td><td>11.6%</td><td>5.5x</td><td>4.9x</td><td>7.1%</td><td>11.7%</td><td>0.3%</td><td>4.9%</td><td>3.0x</td><td>2.6x</td></tr><tr><td>Empresas CMPC SA</td><td>CMPC.SN</td><td>Chile</td><td>2.8</td><td>Neutral</td><td>1,389</td><td>1,040</td><td>33.6%</td><td>7.0x</td><td>6.1x</td><td>6.5%</td><td>11.6%</td><td>1.1%</td><td>0.7%</td><td>4.6x</td><td>3.9x</td></tr><tr><td>LatAm Average</td><td></td><td></td><td>5.4</td><td></td><td></td><td></td><td>14.7%</td><td>6.7x</td><td>6.4x</td><td>-0.1%</td><td>5.3%</td><td>2.6%</td><td>3.4%</td><td>3.8x</td><td>3.7x</td></tr></table>

Closing prices as of 25-Jun-2026.

Target Prices in R\$ and in CH\$ for COPEC and CMPC

Source: Bloomberg, GS Global Investment Research

## Disclosure Appendix

## Reg AC

We, Marcio Farid, Henrique Marques and Emerson Vieira, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Marcio Farid GS do Brasil CTVM S.A., Henrique Marques GS do Brasil CTVM S.A., Emerson Vieira GS do Brasil CTVM S.A..

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

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

Additional disclosures required under the laws and regulations of jurisdictions other than the United States
The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for information purposes only and is not, and under no circumstances should be construed as, an advertisement, offering or solicitation by GS & Co. LLC for purchasers of securities in Canada to trade in any Canadian security. GS & Co. LLC is not registered as a dealer in any jurisdiction in Canada under applicable Canadian securities laws and generally is not permitted to trade in Canadian securities and may be prohibited from selling certain securities and products in certain jurisdictions in Canada. If you wish to trade in any Canadian securities or other products in Canada please contact GS Canada Inc., an affiliate of The GS Group Inc., or another registered Canadian dealer. Hong Kong: Further information on the securities of covered companies referred to in this research may be obtained on request from GS (Asia) L.L.C. India: Further information on the subject company or companies referred to in this research may be obtained from GS (India) Securities Private Limited, Research Analyst - SEBI Registration Number INH000001493, 10th Floor, Ascent-Worli, Sudam Kalu Ahire Marg, Worli, Mumbai-400 025, India, Corporate Identity Number U74140MH2006FTC160634, Phone +91 22 6616 9000, Fax +91 22 6616 9001. GS may beneficially own 1% or more of the securities (as such term is defined in clause 2 (h) the Indian Securities Contracts (Regulation) Act, 1956) of the subject company or companies referred to in this research report. Registration granted by SEBI and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. GS (India) Securities Private Limited compliance officer and investor grievance contact details, a copy of the annual compliance audit report and other relevant informati

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
