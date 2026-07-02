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
US AUTOS & INDUSTRIAL TECH

# June US auto SAAR was in the mid to high 16 mn range

## Synopsis:

US light vehicle sales at a seasonally adjusted annualized rate (SAAR) in June were about 16.7 mn per Motor Intelligence and 16.5 mn per Wards, well above StreetAccounts consensus at 16.3 mn.

In June per Motor Intelligence, US light vehicles sales in total were up about $8\%$ yoy, with car sales up about $6\%$ yoy, pickup truck sales up about $5\%$ yoy, and SUV sales up about $8\%$ yoy. Total units were down $7\%$ sequentially.

Per Motor Intelligence, Ford sales were down about $2\%$ yoy, while GM's sales were up about $6\%$ yoy in the month of June.

June EV sales were down about $30\%$ yoy, and hybrid sales were up about $43\%$ yoy. EVs (BEVs) made up about $5\%$ of monthly unit volumes. However, because Tesla does not report US specific data or monthly sales, we believe there is more estimation in the BEV data.

Incentive spending per vehicle was up about $2\%$ yoy and down about $1\%$ sequentially in June.

For 2Q in total, industry sales were up $1\%$ yoy per Motor Intelligence, with GM's unit sales down $4\%$ (which GM attributed to EVs, discontinued vehicles, and some inventory constraints) and Ford's unit sales down $10\%$ yoy.

\- Inventory was up sequentially to \~2.72 mn units in June. Inventory on a unit basis remains slightly below the historical range of 3 mn+, and inventory days are near the lower end of the historical range.

Mark Delaney, CFA +1(212)357-0535 | mark.delaney@gs.com GS & Co. LLC

Will Bryant
+1(212)934-4705 | will.bryant@gs.com
GS & Co. LLC

Aman Gupta  
+1(212)357-1549 |  
aman.s.gupta@gs.com  
GS & Co. LLC

Ayush Ghose +1(212)902-7257 | ayush.ghose@gs.com GS & Co. LLC

## June SAAR was up mom and up yoy

US light vehicle sales at a seasonally adjusted annualized rate (SAAR) in June were about 16.7 mn per Motor Intelligence and 16.5 mn per Wards (note that there is a degree of estimation in the calculation as not all OEMs report monthly sales results). This compares to a SAAR of about 16.1 mn in May 2026 and about 15.8 mn in June 2025 (per Wards). SAAR for June was above the StreetAccounts consensus of 16.3 mn.

Absolute units were down month-on-month to about 1.38 mn in June from 1.48 mn in May, and up yoy from 1.28 mn in June 2025 (per Motor Intelligence). This implies growth in the mid to high single digit range yoy in absolute units. We note that June 2026 had 1 more selling day vs June 2025 and 1 less selling day than May 2026.

Exhibit 1: June US SAAR was about 16.5 mn per Wards US LV SAAR  
![](images/060b62a7f73cf872653a6f3ed0d25a99240dde7605bf0cdfa7d8df3b5d18a672.jpg)  
Source: Wards

Exhibit 2: US SAAR was in the mid to high 16 mn range in June US LV SAAR  
![](images/c8c4f79c2a6a77e497e03f332b68fa674ecc4fface386ec8a4d99cc3fd7ca914.jpg)  
Source: Wards

In June, car sales were up about 6% yoy, pickup truck sales were up about 5% yoy, and SUV sales were up about 8% yoy. SUV sales as a percent of total units were up to 57.4% vs. 57.2% in June 2025, and pickup truck sales as a percent of total units declined to 19.4% (vs. June 2025 at 20.0%).

Exhibit 3: In June, car, SUV, and pickup unit sales were up yoy US light vehicle unit sales by segment  
![](images/09fc78e5741c00d8d5e8b9dc8b05f16dbd28d8a6b4ebc1ec97f44c59918804ef.jpg)  
Source: Autodata  
Exhibit 4: In June, SUV market share increased, and car and pickup market share decreased yoy US light vehicle market share by segment

![](images/403288c4b5249d15a769030c9706043e7eecf10c64a64358094d3172dacb0013.jpg)  
Source: Autodata

Per Motor Intelligence, Ford sales were down about $2\%$ yoy in June and GM sales were up about $6\%$ yoy. Ford's market share in June was down to $13.0\%$ compared to June 2025 at $14.2\%$ , and GM's market share was down to $16.7\%$ from $17.0\%$ in June 2025.

In terms of large pickups, GM's share increased to $40.3\%$ from $38.6\%$ in June 2025, and was up from $39.2\%$ in May 2026. Ford's share declined to $33.1\%$ vs $35.1\%$ in June 2025, but its share was up slightly from $32.8\%$ in May 2026. Stellantis' share increased to $17.9\%$ from $16.9\%$ last year, but was down from $18.6\%$ in May 2026.

Recall that Ford lost about 100K units of production in 2025 from the Novelis fire, with the fire having a disproportionate impact on F-Series production. Ford still expects to make up \~50-60K of that production in 2026. The reduced F-Series production likely had some effect on certain SKUs of its pickup sales, including for fleets or consumers that may have specific requirements (although inventory on hand likely mitigated share dynamics).

Exhibit 5: In June, GM sales increased yoy on a units basis, while Ford and Tesla volumes decreased US light vehicle unit sales by OEM  
![](images/5d6a7399a59bd1b2ed9ee570674b09c6154ccbd1df77d7caafbc5d1ba03e9512.jpg)  
Source: Autodata

Exhibit 6: In June, GM, Ford, and and Tesla market share decreased yoy US light vehicle market share by OEM  
![](images/364d80456e09ae5d6e72cf77f37d6301c3127d006c67c3503eaeaf8ea745213c.jpg)  
Source: Autodata

## EVs and hybrids

June EV sales were down about 30% yoy, and hybrid sales were up about 43% yoy, per Motor Intelligence. Notably, Tesla does not report monthly sales or US specific sales data, and given its dominant EV market share in the US, we believe the EV data has a greater degree of estimation than the other monthly datapoints. EV mix was about 5% of total sales in the month, down from about 8% a year ago.

Per Motor Intelligence, Tesla sales overall were down 27% yoy with Tesla Model Y sales down 17% yoy, Model 3 sales down 40%, Model S/X down 71%/78% respectively (recall these models ended production in 2Q), and Cybertruck units declined 27%. For Ford, E-Transit sales were down 10%, Mach-E sales declined 32% and F-150 Lightning sales declined 78%. For GM, Lyriq sales were down 21%, Equinox EV sales were down 82%, and Blazer EV sales were down 64%. For Rivian, Motor Intelligence estimates its sales were down 9% with R1S sales down 24%, R1T sales down 54%, and EDV sales up 89%.

Exhibit 7: BEV sales were down $30\%$ yoy US BEV unit sales

![](images/a16b47582acaf72621ccc9f1b3d0c2741964531a3b995a3bd59ce03214abd83e.jpg)  
Source: Autodata

Exhibit 8: Hybrid sales were up about $43\%$ yoy US hybrid unit sales  
![](images/300fd7d39a876cffb4007b6540739b1656cf241ef24cf3ae4e9bb369b061d545.jpg)  
Source: Autodata

Incentive spending per vehicle was up 2% yoy and down 1% sequentially in June June's industry incentive spending per vehicle was up 2% yoy and was down 1% sequentially to \~\$3,464 per vehicle (per Motor Intelligence).

Exhibit 9: US light vehicle incentives were up slightly yoy in June

US light vehicle incentives

![](images/69074d19ee38217d7dfd1484e6deddaa7e2267de85ffabd0d33d3052c1bcf561.jpg)  
Source: Autodata

Inventory increased sequentially to \~2,717K units in June from \~2,667K in May. Finished vehicle inventory increased sequentially to \~2,717K in June from \~2,667K units in May, and remains modestly below historical levels in the 3-4 mn range. Industry DOI came in at 49 days compared to 47 days in May 2026 and 50 days in June 2025. Pickup truck DOI was 70 days (vs. 66 days in May 2026 and 69 days in June 2025), SUV DOI was 47 days (vs. 44 days in May 2026 and 47 days in June 2025), and car DOI was 36 days (vs. 34 days in May 2026 and 37 days in June 2025).

Exhibit 10: Finished vehicle inventory remains below historical levels  
Total US light vehicle DOI  
![](images/d160bbc03e04b15530202dcaa071cd27a9ac5a2c1c756b21e10f185a45e1a204.jpg)  
Source: Autodata

Exhibit 11: Finished vehicle inventory remains below historical levels US light vehicle inventory  
![](images/4d181a9adaa8e9f294b7925b4d0f199d9537bc45a3717f8d4be7ebe96af6f6f3.jpg)  
Source: Autodata

Exhibit 12: Days of inventory at the Detroit 3 (GM, Ford, and Stellantis)  
![](images/62e0d0a8164aefbdf82ef1bf69d0e3ded7ce7b2f5c923b52122f385d3446baf0.jpg)  
Source: Autodata

## 2Q26 highlights

For 2Q26 in total, units were up $1\%$ yoy and up $15\%$ qoq.

GM's units were down $4\%$ yoy and up $14\%$ qoq, with GM having top market share in 2Q. GM attributed the yoy decline to discontinued units (a 12K unit or roughly $1\%$ impact), EVs, and some supply constraints. For large pickups, GM's units were down $3\%$ yoy and up $18\%$ qoq.

Ford's units were down $10\%$ yoy and up $20\%$ qoq. For large pickups, Ford's units were down $11\%$ yoy and up $24\%$ qoq.

## Implications

Auto demand has remained strong, and better than consensus. This is directionally consistent with our recent auto leading indicators analysis (showing improvement based on consumer surveys and Google search traffic) and despite soft overall consumer sentiment and a trend higher in pricing (as OEMs have been effective at passing on higher costs). YTD SAAR has now averaged 15.9 per Wards, and we believe our 16 mn forecast for light vehicle SAAR in 2026 remains reasonable.

We expect key themes from here to include: 1) Price-cost, including with volatility in memory and commodity costs; 2) tariffs including USMCA uncertainty, with the US opting not to renew the USMCA and the agreement now being subject to ongoing annual reviews per Bloomberg; 3) Product cycles and new launches, including the Y L from Tesla, R2 from Rivian, the new full size pickups for MY27 for GM, and the F-Series recovery post the Novelis fire for Ford.

## Disclosure Appendix

## Reg AC

We, Mark Delaney, CFA, Will Bryant, Aman Gupta and Ayush Ghose, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Mark Delaney, CFA GS & Co. LLC, Will Bryant GS & Co. LLC, Aman Gupta GS & Co. LLC, Ayush Ghose GS & Co. LLC.

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

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See 'Ratings, Coverage universe and related definitions' below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; $1\%$ or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

Additional disclosures required under the laws and regulations of jurisdictions other than the United States
The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for information purposes only and is not, and under no circumstances should be construed as, an advertisement, offering or solicitation by GS & Co. LLC for purchasers of securities in Canada to trade in any Canadian security. GS & Co. LLC 

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
