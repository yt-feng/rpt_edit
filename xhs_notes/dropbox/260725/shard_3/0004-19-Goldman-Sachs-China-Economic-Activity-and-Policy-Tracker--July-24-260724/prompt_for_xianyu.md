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
# China Economic Activity and Policy Tracker: July 24

In this note, we update four sets of high-frequency indicators that we track: 1) consumption and mobility; 2) production and investment; 3) other macro activity; and 4) markets and policy. To track closely the impact of higher energy price supply shock on Chinese economic activity, we now publish our tracker on a weekly basis.

## 1) Consumption and mobility

Exhibit 1: 30-city daily property transaction volume in the primary market ticked up over the last week and was around year-ago level

![](images/b4fad6bd71d27d0778e314ccc02dcaba2be6e3ecfc6b9d38e89890cf904a51a1.jpg)  
\*Percentage change relative to 2025.  
Source: Wind, GS Global Investment Research

Chelsea Song
+852-2978-0106 |
chelsea.song@gs.com
GS (Asia) L.L.C.

Exhibit 2: 16-city daily property transaction volume in the secondary market edged up over the last week and remained above year-ago level  
![](images/86372f475397b21bf5c91559b3fb1497cfb6e7b70e57d7793fd65cb9d03f00b3.jpg)  
Source: Wind, GS Global Investment Research

Exhibit 3: China's passenger flights for domestic routes increased further over the last week  
![](images/4793bb81288759fb7f78b3965d5d6ae3557c487beca1767ee904927b7851a049.jpg)  
Source: Wind, GS Global Investment Research

Exhibit 4: China's passenger flights cancellation rate declined over the last week  
![](images/7984df20df76d54dc30466c31e9745708bf0453b562f53d1f3d7c1c96857d5ec.jpg)  
\*Difference relative to 2025.  
Source: Wind, GS Global Investment Research

Exhibit 5: Traffic congestion declined over the last week  
![](images/be262309019e1228588a3ba0f73803fb32056cfd5c049c7312dcb21bf4cae271.jpg)  
\*Calculated as the ratio of actual travel time to 'free flow' travel time, higher = more congested.  
\*Percentage change relative to 2025.

From 2022 onwards, we changed our data source from Gaode map to Baidu map. Baidu congestion data starts from September 2021 and moves closely with that from Gaode map. The two sets of data are different in sample coverage: Gaode map covers 100 cities and Baidu map covers 98 cities.

Exhibit 6: Domestic gasoline and diesel prices were raised by 300 and 290 RMB/tonne respectively on 17 July  
![](images/56cb439242937c02801989aaaff1518b035d91d8a8623eb684f7f682dbd1993e.jpg)  
Source: Haver Analytics, GS Global Investment Research

Exhibit 7: Prices for sulfuric acid and urea edged down over the last week  
![](images/98a0b33035bd5dd43bb30b25a8ca60fd84ce3cc0005f67e3e0286a15e88fa1bc.jpg)  
Source: Wind, Haver Analytics, GS Global Investment Research

Exhibit 8: The Morning Consult consumer confidence declined over the past week  
![](images/6db5a2b3faab989d7b7bf9bbbaef144a1b88556840810406fcfe0f7b9df9f2ba.jpg)  
Source: Haver Analytics, Morning Consult, GS Global Investment Research

## 2) Production and investment

Exhibit 9: Steel demand edged down over the past week

![](images/2fe9da6dfd459c8d65fec1df6aa513f254fd1084fb47675f401fbc8b343b52c4.jpg)  
Source: Mysteel, GS Global Investment Research

Exhibit 10: Steel production increased over the past week  
![](images/06d9c79bddaf7d66f46c24abafe15d6de63bfe3cba00eb8de491f7386c0e5d3f.jpg)  
Source: Mysteel, GS Global Investment Research

Exhibit 11: Daily coal consumption in coastal provinces decreased over the last week but remained above year-ago level  
![](images/ea07932676697824656af4cdf3f8a188f94f4250cbcaeaa55f5f68afecafe60a.jpg)  
Note: Data available since July 2020, data prior to that are derived based on coal consumption at six major coastal power plants.  
Source: Haver, CCTD, GS Global Investment Research

Exhibit 12: RMB 2.36tn local government special bonds have been issued year-to-date  
![](images/bb517945d080a37857e809a77218d8b4f20202057c5df93a958754c98f1ff687.jpg)  
Source: Wind, GS Global Investment Research

Exhibit 13: After seasonal adjustment, EPMI inched up in July  
![](images/915ede6c39d4f17f45f60111d3d43d5e25aedfd2ddda7109662a278ed6caa409.jpg)  
Source: CFLP, Haver Analytics, Wind, GS Global Investment Research

## 3) Other macro activity

Exhibit 14: Official port container throughput stayed below year-ago level  
![](images/389965cc36bc1a7aa34d198f71363dc5d83df68c9c2a87187a8130c79c3d6677.jpg)  
Source: Ministry of Transport, Haver Analytics, GS Global Investment Research  
Exhibit 15: Freight volume of departing ships at 20 major ports rebounded sharply after Typhoon Bavi

![](images/12fe98c365322dd5e3e72681cb6887006f79a1bcd375d7dab79ab0ef53735274.jpg)  
Source: CEIC, GS Global Investment Research

Exhibit 16: Export volume of China's rare earth magnets to EU rebounded in June, whereas volume to US and Japan were largely flat  
![](images/281478c580619a3369520a0d61d8ca3b4475c9fe9a20ae64a281ae25405244e0.jpg)  
Source: GACC, Haver Analytics, CEIC, GS Global Investment Research

Exhibit 17: Our nowcast indicates China oil demand edged down to 16.4mb/d in the latest reading  
![](images/9a8690118e5bb7fcd2ab8b6b217ce4e4768e1b897c87fd5b60cc6a4f141d38b2.jpg)  
Our GS Commodities research team detail their updated methodology for nowcasting China demand in their oil tracker. GS nowcast provides a high-frequency measure of demand, while GS balances are based on supply-demand estimates updated every six weeks.  
Source: Kpler, ICIS, Oilchem, IEA, GS Global Investment Research

## 4) Markets and policy

Exhibit 18: Interbank repo rates edged down over the week  
![](images/39d78853785042e82023373df9e65c5a07455769b6f28f9b36ebb7f7e33e97a7.jpg)  
Source: Wind, GS Global Investment Research

Exhibit 19: Overnight repo rate edged down over the last week  
![](images/d146af033c7878fa99d813a949be6d4b94ff00a1881a263797d132ca7911b44a.jpg)  
The grey dashed lines represent the corridor defined by the temporary overnight OMOs.  
Source: CEIC, Wind, GS Global Investment Research

Exhibit 20: CNY appreciated slightly against USD and CFETS basket over the past week  
![](images/6fbc7896a06a071f7c3614a38479ed7fb438d77b179d2dbc25197f9b4e393fa1.jpg)  
Source: GS Global Investment Research, Wind

Exhibit 21: USDCNY fixing implied countercyclical factor remained range-bound over the past week  
![](images/8b1bfd89cfe68f959107b4cd9c4fae06b5f8bf2b2448cdb12eb21c956998e8d5.jpg)  
Source: Bloomberg, Data compiled by GS Global Investment Research

Exhibit 22: Major macro policy announcements since mid-May

<table><tr><td>Date</td><td>Announcement</td><td>Type</td></tr><tr><td>21-Jul</td><td>China to allocate RMB22bn in ultra-long-term CGSB to support the scrapping and replacement of aging freight trucks</td><td>Growth</td></tr><tr><td>20-Jul</td><td>State council meeting on the supervision of service-sector capacity enhancement and quality upgrading, planning and construction of the &quot;six networks&quot;, and optimising the social security system</td><td>Growth</td></tr><tr><td>17-Jul</td><td>Ministry of Finance reinstates consumption tax on some batteries</td><td>Other</td></tr><tr><td>13-Jul</td><td>Premier Li Qiang held a symposium with experts and entrepreneurs to discuss economic policies</td><td>Growth</td></tr><tr><td>13-Jul</td><td>State council approved the 15th FYP for expanding consumption</td><td>Consumption</td></tr><tr><td>10-Jul</td><td>State council meeting on cultivating emerging industries</td><td>Growth</td></tr><tr><td>8-Jul</td><td>PBOC reiterated its measured easing stance at its Q2 MPC meeting</td><td>Monetary</td></tr><tr><td>5-Jul</td><td>State council released the action plan for carbon peaking during China&#x27;s 15th FYP</td><td>Other</td></tr><tr><td>29/30-Jun</td><td>The PBOC conducted its first overnight reverse repos, with the rate undisclosed</td><td>Monetary</td></tr><tr><td>29-Jun</td><td>State Council meeting focused on AI development and the current foreign trade situation, and reviewed the carbon peaking plan for the 15th Five-Year Plan</td><td>Other</td></tr><tr><td>25-Jun</td><td>NDRC and National Energy Administration released China&#x27;s 15th FYP for building the new-type energy system</td><td>Investment</td></tr><tr><td>23-Jun</td><td>Ministry of Commerce issued notices to intensify efforts to promote the expansion of automobile consumption across the entire chain</td><td>Consumption</td></tr><tr><td>22-Jun</td><td>Ministry of Commerce issued a plan to stabilize and improve the utilization of foreign investment</td><td>Investment</td></tr><tr><td>18-Jun</td><td>Ministry of Commerce issued opinions on accelerating the development of AI+ consumption</td><td>Consumption</td></tr><tr><td>18-Jun</td><td>NDRC will issue the complete list of this year&#x27;s 200bn yuan equipment upgrade projects and the third batch of 62.5bn yuan in CGSB funds for the consumer goods trade-in program by end June</td><td>Consumption</td></tr><tr><td>17-Jun</td><td>Lujiazui Forum reinforced three policy directions: a more price-based monetary policy framework, reduced emphasis on aggregate credit extension, and rules-based capital opening</td><td>Monetary</td></tr><tr><td>15-Jun</td><td>MOF issued administrative measures for service industry development funds</td><td>Consumption</td></tr><tr><td>11-Jun</td><td>State council meeting on rectifying issues from 2025 audit of central budget execution and other fiscal revenues and expenditures</td><td>Fiscal</td></tr><tr><td>10-Jun</td><td>NDRC meeting on accelerated preparation of targeted policy tools for timely implementation as needed</td><td>Growth</td></tr><tr><td>2-Jun</td><td>The central government allocated 99.9 billion yuan in childcare subsidy funds to support the implementation of the childcare subsidy system</td><td>Consumption/Growth</td></tr><tr><td>1-Jun</td><td>State council issued a document setting out guidelines on corporate and individuals&#x27; overseas investments</td><td>Other</td></tr><tr><td>28-May</td><td>State council issued a notice on the Urban Renewal Plan for the 15th Five-year period</td><td>Growth</td></tr><tr><td>22-May</td><td>State council issued note on promoting the provision of basic public services at the place of permanent residence</td><td>Other</td></tr><tr><td>21-May</td><td>State council meeting on advancing the construction of a unified national market</td><td>Growth</td></tr><tr><td>18-May</td><td>State council issued the action plan for stabilizing employment, expanding job openings, and improving job qualities</td><td>Employment</td></tr><tr><td>15-May</td><td>State council meeting on the implementation of Central Urban Work Conference&#x27;s directives and progress of urban renewal</td><td>Growth</td></tr></table>

Source: Government websites, GS Global Investment Research

Thanks to Samson Yau and Ming Yang, interns on the Asia Economics team, for their contribution to this report.

## The China Economics Team

Andrew Tilton
+852-2978-1802
andrew.tilton@gs.com
GS (Asia) L.L.C.

Xinquan Chen
+852-2978-2418
xinquan.chen@gs.com
GS (Asia) L.L.C.

Hui Shan
+852-2978-6634
hui.shan@gs.com
GS (Asia) L.L.C.

Yuting Yang
+852-2978-7283
yuting.y.yang@gs.com
GS (Asia) L.L.C.

Lisheng Wang
+852-3966-4004
lisheng.wang@gs.com
GS (Asia) L.L.C.

Chelsea Song
+852-2978-0106
chelsea.song@gs.com
GS (Asia) L.L.C.

## Disclosure Appendix

## Reg AC

I, Chelsea Song, hereby certify that all of the views expressed in this report accurately reflect my personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Chelsea Song GS (Asia) L.L.C..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for information purposes only and is not, and under no circumstances should be construed as, an advertisement, offering or solicitation by GS & Co. LLC for purchasers of securities in Canada to trade in any Canadian security. GS & Co. LLC is not registered as a dealer in any jurisdiction in Canada under 

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
