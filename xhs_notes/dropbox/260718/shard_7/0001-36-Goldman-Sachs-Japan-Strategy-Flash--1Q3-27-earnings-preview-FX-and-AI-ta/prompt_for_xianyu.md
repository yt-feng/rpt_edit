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
# Japan Strategy Flash: 1Q3/27 earnings preview - FX and AI tailwinds meet a high consensus bar

1Q3/27 earnings releases by companies with a March fiscal year-end are set to move into full swing. The peak days for scheduled announcements are July 29-31 (Wednesday-Friday) and August 3-7 (Monday-Friday), with $38\%$ and $50\%$ (market cap basis) of TOPIX companies with a February/March fiscal year-end due to report during the initial and latter periods, respectively.

Bruce Kirk, CFA
+81(3)4587-9950 | bruce.kirk@gs.com
GS Japan Co., Ltd.

Julius Chan  
+81(3)4587-1789 | julius.chan@gs.com  
GS Japan Co., Ltd.

Excluding Softbank Group (given its volatile earnings), I/B/E/S consensus estimates for TOPIX companies with a February/March fiscal year-end call for double-digit (%) increase in both 1Q recurring profits (+22% yoy) and net profits (+26% yoy). Consensus also expects positive profit growth over the next 4 quarters with an average quarterly yoy recurring profit growth of 18% (Exhibit 6).

\- AI-related stocks have contributed to almost half of TOPIX EPS change YTD (Exhibit 5). Given the heightened expectation entering into the earnings season, price reactions will likely be negative if these related companies fail to deliver large positive surprises.

Average USDJPY has risen from 144 in FY25 Q1 to 159 in FY26 Q1 (Exhibit 8). Our FX strategists see further weakening of the Yen (link) and expect the USDJPY to reach 165 in 12M. Our sensitivity analysis indicates for every ¥10 increase (decrease) in USDJPY, TOPIX EPS increases (decreases) by 3.5%. The median/average of corporates' initial assumptions for FY26 are 151/152 respectively (Exhibit 9).

The earnings revision index continues to trend in positive territory. Over the past three months, sectors with large upward revisions to net profits have included semis & SPE, financials, construction, and machinery. In contrast, sectors with significant downward revisions to earnings have included pharmaceuticals, autos & auto-parts, and other materials.

Exhibit 1: Consensus calls for TOPIX (ex-Softbank Group) NP to increase by 26% yoy in 1Q TOPIX companies with Feb/Mar fiscal year-end, yoy growth (%)

<table><tr><td rowspan="2">YoY%</td><td colspan="3">Prev. 4Q FY3/26</td><td colspan="3">1Q FY3/27 Consensus</td><td colspan="3">FY3/27 Full-YearConsensus</td></tr><tr><td>Sales</td><td>RP</td><td>NP</td><td>Sales</td><td>RP</td><td>NP</td><td>Sales</td><td>RP</td><td>NP</td></tr><tr><td>Topix stocks</td><td>5</td><td>30</td><td>34</td><td>7</td><td>18</td><td>25</td><td>6</td><td>13</td><td>17</td></tr><tr><td>Topix (ex-Financials)</td><td>5</td><td>19</td><td>25</td><td>7</td><td>19</td><td>29</td><td>7</td><td>15</td><td>18</td></tr><tr><td>Manufacturers</td><td>7</td><td>5</td><td>11</td><td>9</td><td>43</td><td>39</td><td>8</td><td>41</td><td>53</td></tr><tr><td>Nonmanufacturers</td><td>3</td><td>34</td><td>36</td><td>4</td><td>-5</td><td>15</td><td>6</td><td>-9</td><td>-13</td></tr><tr><td>Financials</td><td>-</td><td>118</td><td>106</td><td>-</td><td>15</td><td>13</td><td>1</td><td>4</td><td>11</td></tr><tr><td>Topix stocks(ex-SoftbankGr)</td><td>5</td><td>18</td><td>35</td><td>7</td><td>22</td><td>26</td><td>6</td><td>20</td><td>27</td></tr><tr><td>Nonmanufacturers(ex-SoftbankGr)</td><td>3</td><td>5</td><td>39</td><td>4</td><td>3</td><td>17</td><td>6</td><td>6</td><td>7</td></tr></table>

Source: I/B/E/S, Toyo Keizai, FactSet, Data compiled by GS Global Investment Research

Exhibit 2: We expect positive surprises to outweigh negative surprises in 1Q TOPIX companies with Feb/Mar fiscal year-end  
![](images/e5d4a7802fd54a3bf9dc62471a0c1b7d7bcd23eb1ce5b41ddd43b41652e6ef95.jpg)  
Source: I/B/E/S, Toyo Keizai, FactSet, GS Global Investment Research

Exhibit 3: Earnings growth has contributed 68% of TOPIX return YTD  
![](images/18df4f0c2c9f70fbe5026128a4c8c4408f21de0b4f45be038620d9d5362ecdb4.jpg)  
Source: FactSet, Data compiled by GS Global Investment Research

Exhibit 4: Earnings revision index remains positive  
![](images/0fe833a3422889bd5c8b1750f219588d324f333d5b039f7105f0bc5a1b09dbb5.jpg)  
Earnings forecast revision index = (no. of analyst upward revisions for past 1 mo. - no. of downward revisions) / Total no. of forecasts.  
Source: I/B/E/S, FactSet

Exhibit 5: AI-related stocks have contributed almost half of EPS change YTD Breakdown of TOPIX NTM EPS change  
![](images/eb766bc67908b4ec5bf5feee31175541a78c2d089dd046283d5356e00b615faa.jpg)  
Source: FactSet, Data compiled by GS Global Investment Research

Exhibit 6: Consensus expects average yoy recurring profit growth of $18\%$ over the next 4 quarters TOPIX companies with Feb/Mar fiscal year-end (excluding Softbank Group), %  
![](images/c8ceac3d23c5875ca17d1813eacc514ef2a35d60415ef93376029ca112774d0e.jpg)  
Estimates are I/B/E/S consensus  
Source: I/B/E/S, Toyo Keizai, FactSet

Exhibit 7: Quarterly recurring profits
TOPIX companies with Feb/Mar fiscal year-end (excluding Softbank Group), ¥ tn  
![](images/574a6e687e590508265603b9177b9a66070a79aa62de3d086de4f96740587887.jpg)  
Source: I/B/E/S, Toyo Keizai, FactSet

Exhibit 8: USDJPY has risen from 144 in FY25 Q1 to 159 in FY26 Q1, our FX strategists expect further weakening to 165 in 12M  
![](images/27883c00138f6ed662c8cf1e73ee96e521d2ee0021d9bab529d34f0e0db12c4d.jpg)

Exhibit 9: Initial median/average corporate USDJPY assumptions for FY26 are 151.0/152.3
Companies with Feb/Mar FY-end  
![](images/a8b0fc83f8090d4048ee06c006e8a59fe4ea9eb11e90bfd4342c72de7ac7d6bb.jpg)  
Source: FactSet, GS Global Investment Research  
Source: QUICK

Exhibit 10: FY26 net profit revisions by sector  
![](images/938fd096c170447298a1366f7579d75ed89b6c0f9b1d8d28d0db17fe55e95e49.jpg)  
Source: I/B/E/S, FactSet

## Earnings calendar

1Q3/27 earnings releases by companies with a March fiscal year-end are set to move into full swing. The peak days for scheduled announcements are July 29-31 (Wednesday-Friday) and August 3-7 (Monday-Friday), with $38\%$ and $50\%$ (market cap basis) of TOPIX companies with a February/March fiscal year-end due to report during the initial and latter periods, respectively.

On a market cap basis, 46% of companies are expected to have announced earnings by July 31 (Friday), 95% by August 7 (Friday), and all companies by August 14 (Friday).

Exhibit 11: TOPIX company announcement schedule (number of companies)
TOPIX companies with Feb/Mar fiscal year-end  
![](images/16303a0c4f6dbe3fad71f8decbb1a1896c68dbb58d99f5b88bf1b21fd077a456.jpg)  
Source: QUICK, Bloomberg

Exhibit 12: TOPIX company announcement schedule (market cap, ¥ tn)
TOPIX companies with Feb/Mar fiscal year-end  
![](images/5f6d6017a12b70eb7dc9911dd1aebc564462d15695d823e166db53ef4bb56cd7.jpg)  
Source: QUICK, Bloomberg

Exhibit 13: TOPIX company announcement schedule (sector market cap)
TOPIX companies with Feb/Mar fiscal year-end

<table><tr><td rowspan="2"></td><td rowspan="2">Total Mkt-cap</td><td colspan="4">Percent of Weight Reporting</td></tr><tr><td>- Jul 24</td><td>Jul 27 - Jul 31</td><td>Aug 3 - Aug 7</td><td>Aug 10 - Aug 14</td></tr><tr><td>TOPIX</td><td></td><td>5%</td><td>41%</td><td>50%</td><td>5%</td></tr><tr><td>Energy</td><td>1%</td><td>0%</td><td>3%</td><td>96%</td><td>1%</td></tr><tr><td>Materials</td><td>6%</td><td>24%</td><td>22%</td><td>49%</td><td>5%</td></tr><tr><td>Industrials</td><td>25%</td><td>1%</td><td>35%</td><td>61%</td><td>3%</td></tr><tr><td>Consumer Discretionary</td><td>13%</td><td>4%</td><td>40%</td><td>52%</td><td>4%</td></tr><tr><td>Consumer Staples</td><td>3%</td><td>37%</td><td>12%</td><td>45%</td><td>7%</td></tr><tr><td>Health Care</td><td>4%</td><td>0%</td><td>54%</td><td>44%</td><td>2%</td></tr><tr><td>Financials</td><td>19%</td><td>0%</td><td>37%</td><td>49%</td><td>14%</td></tr><tr><td>Information Technology</td><td>19%</td><td>5%</td><td>78%</td><td>15%</td><td>2%</td></tr><tr><td>Communication Services</td><td>9%</td><td>1%</td><td>6%</td><td>90%</td><td>2%</td></tr><tr><td>Utilities</td><td>1%</td><td>0%</td><td>99%</td><td>1%</td><td>0%</td></tr><tr><td>Real Estate</td><td>2%</td><td>1%</td><td>12%</td><td>87%</td><td>0%</td></tr></table>

Source: QUICK, Bloomberg

## Disclosure Appendix

## Reg AC

We, Bruce Kirk, CFA and Julius Chan, hereby certify that all of the views expressed in this report accurately reflect our personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Bruce Kirk, CFA GS Japan Co., Ltd., Julius Chan GS Japan Co., Ltd..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for information purposes only and is not, and under no circumstances should be construed as, an advertisement, offering or solicitation by GS & Co. LLC for purchasers of securities in Canada to trade in any Canadian security. GS & Co. LLC is not registered as a dealer in any jurisdiction in Canada under applicable Canadian securities laws and generally is not permitted to trade in Canadian securities and may be prohibited from selling certain securities and products in certain jurisdictions in Canada. If you wish to trade in any Canadian securities or other products in Canada please contact GS Canada Inc., an affiliate of The GS Group Inc., or another registered Canadian dealer. Hong Kong: Further information on the securities of covered companies referred to in this research may be obtained on request from GS (Asia) L.L.C. India: Further information on the subject company or companies referred to in this research may be obtained from GS (India) Securities Private Limited, Research Analyst - SEBI Registration Number INH000001493, 10th Floor, Ascent-Worli, Sudam Kalu Ahire Marg, Worli, Mumbai-400 025, India, Corporate Identity Number U74140MH2006FTC160634, Phone +91 22 6616 9000, Fax +91 22 6616 9001. GS may beneficially own 1% or more of the securities (as such term is defined in clause 2 (h) the Indian Securities Contracts (Regulation) Act, 1956) of the subject company or companies referred to in this research report. Registration granted by SEBI and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. GS (India) Securities Private Limited compliance officer and investor grievance contact details, a copy of the annual compliance audit report and other relevant information and disclosures can be found at this link: http://www.goldmansachs.com/worldwide/india/research.ac.uk/japan.Soc.baiy.Korea:This research and approach to it is intended only for

https://www.goldmansachs.com/worldwide/india/research-analyst. Japan: See below. Korea: This research, and any access to it, is intended only for “professional investors” within the meaning of the Financial Services and Capital Markets Act, unless otherwise agreed by GS. Further information on the subject company or companies referred to in this research may be obtained from GS (Asia) L.L.C., Seoul Branch. New Zealand: GS New Zealand Limited and its affiliates are neither “registered banks” nor “deposit takers” (as defined in the Reserve Bank of New Zealand Act 1989) in New Zealand. This research, and any access to it, is intended for “wholesale clients” (as defined in the Financial Advisers Act 2008) unless otherwise agreed by GS. A copy of certain GS Australia and New Zealand disclosure of interests is available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Russia: Research reports distributed in the Russian Federation are not advertising as defined in the Russian legislation, but are information and analysis not having product promotion as their main purpose and do not prov

[中间内容因长度限制已省略]

ttempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints.

As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
