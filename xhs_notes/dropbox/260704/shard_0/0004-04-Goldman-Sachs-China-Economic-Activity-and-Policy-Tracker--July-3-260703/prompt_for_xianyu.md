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
## China Economic Activity and Policy Tracker: July 3

In this note, we update four sets of high-frequency indicators that we track: 1) consumption and mobility; 2) production and investment; 3) other macro activity; and 4) markets and policy. To track closely the impact of higher energy price supply shock on Chinese economic activity, we now publish our tracker on a weekly basis.

Chelsea Song +852-2978-0106 | chelsea.song@gs.com GS (Asia) L.L.C.

## 1) Consumption and mobility

Exhibit 1: 30-city daily property transaction volume in the primary market edged down over the last week and remained below year-ago level

![](images/b1e1cbd0ae00e05a75b62b6fed5e206481ef57f9532752c38d31acdecb043725.jpg)  
Source: Wind, GS Global Investment Research

Exhibit 2: 16-city daily property transaction volume in the secondary market fell over the last week but remained above year-ago level  
![](images/2d8d0d1637e70bf2e66559fa66633ac697c98f47d352c46ff3c59c6bdf6ce160.jpg)  
Source: Wind, GS Global Investment Research

Exhibit 3: China's passenger flights for domestic routes increased towards year-ago level  
![](images/bbf2837b0b7f3333d9ac531a028dd6f223b39c9473ef0e30e1715895a337a666.jpg)  
Source: Wind, GS Global Investment Research

Exhibit 4: China's passenger flights cancellation rate also edged down towards year-ago level  
![](images/58475eb6dc2c05894d3aa1503bd61d5f9cb0c774efeb90972d4fe30136e1e4a7.jpg)  
Source: Wind, GS Global Investment Research  
Exhibit 5: Traffic congestion normalized after Dragon Boat Festival and is currently around year-ago level

![](images/95e836f969ebaea98b0ff6105c93189ad59382606a6fe3ef065d02b4dde437a0.jpg)  
\*Calculated as the ratio of actual travel time to 'free flow' travel time, higher = more congested.  
\*Percentage change relative to 2025.

From 2022 onwards, we changed our data source from Gaode map to Baidu map. Baidu congestion data starts from September 2021 and moves closely with that from Gaode map. The two sets of data are different in sample coverage: Gaode map covers 100 cities and Baidu map covers 98 cities.

Exhibit 6: Domestic gasoline and diesel prices remained unchanged over the last week while Brent price continued to fall  
![](images/82b36e3c3a7a64c73cc6abf2cfe00e151065bfa49ce7928c961bc841b8d66dd3.jpg)  
Source: Haver Analytics, GS Global Investment Research

Exhibit 7: Prices for sulfuric acid edged up over the last week while prices for other chemicals edged down  
![](images/6e566cfc36d666443c8902e4b9343b1ccd9d5f3d7e58b1411f64d0631be2f3c2.jpg)  
Source: Wind, Haver Analytics, GS Global Investment Research

Exhibit 8: The NBS consumer confidence edged up in May, and the Morning Consult consumer confidence also rebounded over the past week  
![](images/fec1e681caa81879426a7a61f594216fc13c2e3bc5e3954e4f364da016e5bcb5.jpg)  
Source: Haver Analytics, Morning Consult, GS Global Investment Research

Exhibit 9: Weighted PMI employment sub-index edged up in June  
![](images/882011c8316ac3c515de7113ebeff9758b6bedf0a2583135e9add639029efc99.jpg)  
Source: NBS, RatingDog, CKGSB, Haver Analytics, GS Global Investment Research

\*Percentage change relative to the same week in 2025.

## 2) Production and investment

![](images/28f8008ceaa490f1951039bd26dd5a202a2cd8b2970fb95036616922c26df8fc.jpg)  
Source: Mysteel, GS Global Investment Research

Exhibit 11: Steel production edged up slightly over the past week  
![](images/202726e3a6541ad2fc055bd99a3b7bd7865c37bc5b5ba7e24efce73f2c048c00.jpg)  
Source: Mysteel, GS Global Investment Research

Exhibit 12: Daily coal consumption in coastal provinces remained rangebound over the last week and was above year-ago level  
![](images/26bc961598b4f35fc78b5066750f1cae7942b385f02062b42b717d8b87adc081.jpg)  
\*Percent change relative to 2025.  
Note: Data available since July 2020, data prior to that are derived based on coal consumption at six major coastal power plants.  
Source: Haver, CCTD, GS Global Investment Research

Exhibit 13: RMB 2.04bn local government special bonds have been issued year-to-date  
![](images/23a0482d24f88dcde38d3bb8f0855b0d4b20a0965e1cf14b22ef9704f56f9656.jpg)  
Source: Wind, GS Global Investment Research

Exhibit 14: The anti-corruption proxy at national level stayed elevated, while that at local level rose to record high in Q2 2026  
![](images/6b5bcccf22405e54c6633995727655efcc879bb947d01e8bed8dbc1d39cd5536.jpg)  
Note: The proxy represents the number of government officials announced as under investigation each quarter. National level is deputy ministerial level and above; local level is any level but in practice mostly deputy bureau level and above.  
Source: CCDI, GS Global Investment Research

Exhibit 15: Policy bank support remained soft in June  
![](images/65e95d100ba8d4a1d80477249a4910d75f51550f3447c4859d9c7dec7c2446ad.jpg)  
Source: PBOC, Wind, Data compiled by GS Global Investment Research

## 3) Other macro activity

Exhibit 16: Official port container throughput increased over the last week and was above year-ago level

![](images/13c5ab2ae3a3f03b8510fe2206c29a29de642ad00d475e30463fdbf53464332c.jpg)  
Source: Ministry of Transport, Haver Analytics, GS Global Investment Research

Exhibit 17: Freight volume of departing ships at 20 major ports increased and was above year-ago level

![](images/308e0fb400d7288b7ec8e21bdfcf3b1baac845f3db9dbf24dc6a974b5378b851.jpg)  
Source: CEIC, GS Global Investment Research

Exhibit 18: Our nowcast indicates China oil demand edged up to 16.4mb/d in the latest reading  
![](images/f82f5b95bda757329b7a24c09534ac68518ef68785d0fb18b6d62f01ffd688cc.jpg)  
Our GS Commodities research team detail their updated methodology for nowcasting China demand in their oil tracker. GS nowcast provides a high-frequency measure of demand, while GS balances are based on supply-demand estimates updated every six weeks.  
Source: Kpler, ICIS, Oilchem, IEA, GS Global Investment Research

Exhibit 19: China visible landed crude inventories fell over the last week of June  
![](images/fff3db076219f5ae38295c25a92b98e33df0b60bf9b44f129e5852ee07a0f661.jpg)  
Source: GS Global Investment Research

## 4) Markets and policy

Exhibit 20: Interbank repo rates edged up over the last week  
![](images/5f1534a5e16cf961078909c3e813e2912033b6d506d843b9f560bc88f9413adf.jpg)  
Source: Wind, GS Global Investment Research

Exhibit 21: Overnight rate remained below the 7-day OMO rate  
![](images/316b086574a855b5afc01d2e662d824992e7ffebcc24e7e248524a04596c3bab.jpg)  
The grey dashed lines represent the corridor defined by the temporary overnight OMOs.  
Source: CEIC, Wind, GS Global Investment Research

Exhibit 22: CNY appreciated against CFETS basket while remained rangebound against USD over the past week  
![](images/40da79be6df83fb248af39b944665e6d555f431033d10c030748a4895ecffa9b.jpg)  
Source: GS Global Investment Research, Wind

Exhibit 23: USDCNY fixing implied countercyclical factor dropped in recent weeks  
![](images/ed4dcd1296d0ffa31089d4e46181c6143523cc1e88f1a1bb08b3abbd6e616175.jpg)  
Source: Bloomberg, Data compiled by GS Global Investment Research

Exhibit 24: Major macro policy announcements since May

<table><tr><td>Date</td><td>Announcement</td><td>Type</td></tr><tr><td>29/30-Jun</td><td>The PBOC conducted its first overnight reverse repos, with the rate undisclosed.</td><td>Monetary</td></tr><tr><td>29-Jun</td><td>State council meeting on the development of AI, current foreign trade situation, and reviewed the plan for carbon peaking during the 15th FPY</td><td>Other</td></tr><tr><td>25-Jun</td><td>NDRC and National Energy Administration released China&#x27;s 15th FYP for building the new-type energy system</td><td>Investment</td></tr><tr><td>23-Jun</td><td>Ministry of Commerce issued notices to intensify efforts to promote the expansion of automobile consumption across the entire chain</td><td>Consumption</td></tr><tr><td>22-Jun</td><td>Ministry of Commerce issued a plan to stabilize and improve the utilization of foreign investment</td><td>Investment</td></tr><tr><td>18-Jun</td><td>Ministry of Commerce issued opinions on accelerating the development of AI+ consumption</td><td>Consumption</td></tr><tr><td>18-Jun</td><td>NDRC will issue the complete list of this year&#x27;s 200bn yuan equipment upgrade projects and the third batch of 62.5bn yuan in CGSB funds for the consumer goods trade-in program by end June</td><td>Consumption</td></tr><tr><td>17-Jun</td><td>Lujiazui Forum reinforced three policy directions: a more price-based monetary policy framework, reduced emphasis on aggregate credit extension, and rules-based capital opening</td><td>Monetary</td></tr><tr><td>15-Jun</td><td>MOF issued administrative measures for service industry development funds</td><td>Consumption</td></tr><tr><td>11-Jun</td><td>State council meeting on rectifying issues from 2025 audit of central budget execution and other fiscal revenues and expenditures</td><td>Fiscal</td></tr><tr><td>10-Jun</td><td>NDRC meeting on accelerated preparation of targeted policy tools for timely implementation as needed</td><td>Growth</td></tr><tr><td>2-Jun</td><td>The central government allocated 99.9 billion yuan in childcare subsidy funds to support the implementation of the childcare subsidy system</td><td>Consumption/Growth</td></tr><tr><td>1-Jun</td><td>State council issued a document setting out guidelines on corporate and individuals&#x27; overseas investments</td><td>Other</td></tr><tr><td>28-May</td><td>State council issued a notice on the Urban Renewal Plan for the 15th Five-year period</td><td>Growth</td></tr><tr><td>22-May</td><td>State council issued note on promoting the provision of basic public services at the place of permanent residence</td><td>Other</td></tr><tr><td>21-May</td><td>State council meeting on advancing the construction of a unified national market</td><td>Growth</td></tr><tr><td>18-May</td><td>State council issued the action plan for stabilizing employment, expanding job openings, and improving job qualities</td><td>Employment</td></tr><tr><td>15-May</td><td>State council meeting on the implementation of Central Urban Work Conference&#x27;s directives and progress of urban renewal</td><td>Growth</td></tr><tr><td>9-May</td><td>State council meeting on the development of the national transportation system and progress in resolving local government debt risks</td><td>Other</td></tr><tr><td>8-May</td><td>MOF allocated RMB 45.8 billion in 2026 to support the development of preschool education</td><td>Growth</td></tr><tr><td>1-May</td><td>Premier Li Qiang emphasized accelerating the construction of the water network</td><td>Growth</td></tr></table>

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

Lisheng Wang +852-3966-4004 lisheng.wang@gs.com GS (Asia) L.L.C.

Chelsea Song +852-2978-0106 chelsea.song@gs.com GS (Asia) L.L.C.

## Disclosure Appendix

## Reg AC

I, Chelsea Song, hereby certify that all of the views expressed in this report accurately reflect my personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Chelsea Song GS (Asia) L.L.C..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; $1\%$ or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for information purposes only and is not, and under no c

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
