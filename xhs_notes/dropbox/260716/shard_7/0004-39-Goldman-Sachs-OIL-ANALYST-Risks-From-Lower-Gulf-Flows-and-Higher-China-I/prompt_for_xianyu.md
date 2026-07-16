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
OIL ANALYST

# Risks From Lower Gulf Flows and Higher China Imports

\- Physical market is tightening. The recent Middle East escalation pushed Brent prices back into the mid-80s and reversed an initially sharp recovery in Persian Gulf flows. Meanwhile, price-sensitive Chinese crude imports – whose decline has cushioned the Hormuz disruption – may have bottomed after Middle Eastern producers cut official selling prices for July-August. We assess the durability of both the Persian Gulf flows recovery and of the decline in Chinese imports, and draw implications for crude prices.

Flows recovery lost its momentum. We estimate that Gulf exports recovered to more than 80% of pre-war levels in the first two weeks after the MoU, but fell back to below 50% (11mb/d) after renewed attacks on tankers in the Strait (Exhibit 1). This setback leaves the oil market short 13.4mb/d of Persian Gulf flows and, absent near-term de-escalation, would likely require greater demand destruction and renewed inventory draws (Exhibit 2). That said, the latest estimates of observable Gulf flows may understate actual total Gulf flows as some tankers reportedly cross the Strait with transponders turned off. Most “dark-crossing” tankers eventually switch their signals back on outside the Strait, leading to meaningful upside revisions to flows: observable mid-June Gulf exports are now 1.1mb/d (10%) above the initial estimate from a month ago (Exhibit 3).

## ■ Further recovery in Gulf flows remains uncertain and likely uneven:

☐ Geopolitical escalation—particularly further potential attacks on oil tankers and energy infrastructure—remains the main downside risk to the recovery in Persian Gulf flows and production. Based on the April US blockade, we estimate that the newly reinstated blockade of Iranian ports and coastal areas could reduce Iranian exports by 1.5-2mb/d.

☐ The next phase of Gulf flow recovery could be slower than the initial phase even after geopolitical de-escalation. First, Saudi Arabia and the UAE – producers with the largest tanker capacity and high-quality fields – drove most of the June rebound in the flows (Exhibit 5). UAE production likely already exceeded its pre-war level in June, while other crude production losses (vs. February levels) may still total around 9mb/d (Exhibit 6). Second, shippers using the non-Iranian Hormuz lane remain risk-averse, with flows through Omani and international routes declining sharply after the recent tanker attacks (Exhibit 7). Uncertainly and lingering regional risks had

Yulia Zhestkova Grigsby  
+1(646)446-3905 |  
yulia.grigsby@gs.com  
GS & Co. LLC

Alexandra Paulus  
+1(212)902-7111 | alexandra.paulus@gs.com GS & Co. LLC

Daan Struyven +1(212)357-4172 | daan.struyven@gs.com GS & Co. LLC

already weighed on activity by non-Middle Eastern and private shippers even before the latest escalation (Exhibit 8).

China crude imports may have bottomed. China crude net imports fell by 5mb/d year-over-year in June, even as imports by its Asian neighbors had recovered to seasonal norms (Exhibit 9). In our view, China crude imports need not rebound immediately, given still-elevated estimated total oil inventories of 1.9 billion barrels (117 days of demand) and its ability to substitute some oil demand by coal and power. Still, China crude imports are likely to rise for three reasons.

a. The imports' decline appears unusually large relative to the price increase (Exhibit 10).

b. Historical price sensitivity suggests an imports' rebound after Middle Eastern producers cut July–August selling prices below regional benchmarks.

c. Sustained crude destocking at an estimated 2mb/d pace would likely be inconsistent with Beijing's long-term goal of building inventory buffers.

\- Short-term upside risks to prices, medium-term downside. We continue to see two-sided risks to our Brent crude price forecast of \$80 in 2026Q4 and \$75 in 2027, with risks skewed to the upside in the near term as the risk of further attacks on tankers and Middle East energy infrastructure has increased (Exhibit 11). Brent could overshoot \$110/bbl in 2026Q4 if the Gulf export recovery continues to stall, delaying the production rebound and requiring a larger demand response. Conversely, June's swift recovery in flows showed that Gulf exports can rebound quickly after de-escalation, with Brent potentially falling in the \$60s by year-end if production beats expectations and demand recovers more slowly amid high retail fuel prices.

Large Crude Stockpiles Allow China Imports to Be Price Sensitive and Postpone Imports When Crude Prices Are High  
![](images/641adb673f34a7ebc985d7da872be65392ded66d5289cf44e09ea4aadfaf3772.jpg)  
The sample is January 2017 to June 2026, excluding March-May 2020. The crude prices included are Arab Light (Saudi Arabia), Iran Heavy (Iran), Basrah Medium (Iraq), Murban (UAE), Oman Crude (Oman), ESPO Kozmino (Russia).  
Source: Platts, OPEC, Kpler, GS Global Investment Research

## Risks From Lower Gulf Flows and Higher China Imports

## Persian Gulf Flows Are Falling

Initially Swift Persian Gulf Flows Recovery Is Reversing Following the Recent Escalation

Exhibit 1: Estimated Oil Flows From the Persian Gulf Recovered to Over $80\%$ of Normal Levels in the First Two Weeks After the MoU but Retreated Back to Below $50\%$ Over the Last Week Following Renewed Attacks on Tankers

![](images/71dc8111b0d00c6ee6f61e9518bb67d94032e2bb5e4af069ed63164252794c45.jpg)  
Includes flows through the Strait of Hormuz, Yanbu, Fujairah, Gulf of Oman, and Botas Ceyhan.

![](images/bf675db0285c8c8c5c0dc7c9ec17c618868574915cb6634ea931aa0cd1853493.jpg)  
Source: Kpler, S&P Global Commodities at Sea, GS Global Investment Research  
Exhibit 2: Estimated Net Hit to Persian Gulf Flows Doubled Over the Last Week to 13.4mb/d, Implying that the Market Requires More Adjustment Mechanisms to Buffer the Hit

![](images/c28991f58474da39282cb64dfe7a05d1534b6903be526650d6e89b2bb6ef44b9.jpg)  
Source: Kpler, S&P Global Commodities at Sea, GS Global Investment Research

Recently Estimated Observable Persian Gulf Flows May Be a Lower Bound on Total Gulf

## Flows Given "Dark" Crossings

Exhibit 3: Estimates of Persian Gulf Flows as of Mid-June Have Been Revised Up by 1.1mb/d, With UAE Flows Driving 2/3 of the Revisions

![](images/aba8ee48476e84225f7ffd24e15dd56e5c95968b6985d5e4a19af93affca607e.jpg)  
Source: Kpler, GS Global Investment Research

## Downside Risk to Further Flow Recovery

US Blockade Poses Downside Risks to Iranian Oil Flows

Exhibit 4: Iranian Oil Exports Decreased by 1.5-2mb/d During the First US Blockage While Other Persian Gulf Exports Increased by Nearly 4-5mb/d Over the Course of the Blockade

![](images/312b89fc4b96ad05789350db122ea68bd05f466b743995fc1483f06a6bae9bfc.jpg)  
Source: Kpler, GS Global Investment Research

The Next Phase of Gulf Flow Recovery Could Be Slower Than the Initial Phase Even

## After Geopolitical De-escalation

Exhibit 5: Saudi Arabia and UAE — Countries With the Largest Tanker Capacity and High-Quality Fields — Drove the Initial Recovery in the Persian Gulf Flows Since Early June

![](images/325869d026d4a4edd13d3e23da6b9152ce995b770ed68489dffa89fe4b1bbaa1.jpg)  
Source: Kpler, GS Global Investment Research

Exhibit 6: June Persian Gulf Production Losses Are Likely Smaller Than Our Month-Ago Expectations as UAE Production Beat Expectations, but 9-10mb/d of Crude Production Losses Are Yet to Recover

<table><tr><td colspan="11">Average Persian Gulf Oil Production Losses in June vs February (mb/d)</td></tr><tr><td rowspan="2"></td><td rowspan="2">Liquids 
Gulf Incl. 
Qatar</td><td colspan="2">Crude</td><td rowspan="2">NGLs 
Gulf Incl. 
Qatar</td><td colspan="6">Crude</td></tr><tr><td>Gulf Incl. 
Qatar</td><td>Gulf Excl. 
Qatar</td><td>Iran</td><td>Iraq</td><td>Kuwait</td><td>Qatar</td><td>Saudi Arabia</td><td>UAE</td></tr><tr><td>IEA 
(As of July 10)</td><td>11.2</td><td>9.1</td><td>8.1</td><td>2.2</td><td>1.4</td><td>2.6</td><td>1.2</td><td>0.9</td><td>3.4</td><td>-0.4</td></tr><tr><td>OPEC Secondary Sources 
(As of July 13)</td><td>-</td><td>-</td><td>7.0</td><td>-</td><td>0.8</td><td>2.2</td><td>1.1</td><td>-</td><td>3.3</td><td>-0.4</td></tr><tr><td>Kpler 
(As of June 19)</td><td>-</td><td>9.5</td><td>8.4</td><td>-</td><td>1.0</td><td>2.6</td><td>1.4</td><td>1.1</td><td>2.9</td><td>0.6</td></tr><tr><td>GS Balance 
(As of June 15)</td><td>12.8</td><td>10.5</td><td>9.4</td><td>2.3</td><td>0.8</td><td>2.7</td><td>1.8</td><td>1.1</td><td>3.0</td><td>1.0</td></tr></table>

Positive numbers represent losses; negative numbers represent gains.

Exhibit 7: The Recent Decline in the Strait of Hormuz Crossings Is Driven by a Sharp Decline in Flows via Omani and IMO Central Routes Following Attacks of Tankers Using Those Routes

Strait of Hormuz Oil Tanker Crossings

![](images/7303bc5881358799af885d108942adef1e0df529b22a8b9f3e8063bf55dcf1af.jpg)  
IMO stands for the International Maritime Organization.  
Source: Kpler, GS Global Investment Research

![](images/1c7a45d085e44137d966d5d825fb415db4cde56f5ef5d3ba009ab9cf16e14a60.jpg)  
Exhibit 8: While Middle Eastern State-Owned Charters Flows Recovered to 85% of Normal in Early July, Security Concerns Have Likely Been Weighing on Transits by Private and Non-Middle Eastern Shippers

![](images/1c2aab64522a49670c5ee17c8c2f3096ae53029447d92e418f24dd2e1126e93b.jpg)  
Source: Kpler, GS Global Investment Research

Low China Crude Imports Helped to Keep a Lid on Prices, for Now

Price-Sensitive Crude Imports Dropped as Large Stockpiles Helped to Meet Demand, But Will Likely Recover as Middle Eastern Producers Announced Price Declines for July

and August  
Exhibit 9: China Crude Net Imports Declined to Nearly 5mb/d Year-Over-Year in Early July Despite a Steep Recovery in ex China Asia Imports  
![](images/401dca0783bb9726446cea0137a3268fdf4a23c531e94a4fc7b87d3e73aa0601.jpg)  
Source: Kpler, GS Global Investment Research

Exhibit 10: Large Crude Stockpiles Allow China Imports to Be Price Sensitive and Postpone Imports When Crude Prices Are High  
![](images/605c504265f5a5c3a5516680fe454b9d7a0973d9c8f6ed13fbae0002ab9bc4c8.jpg)

The sample is January 2017 to June 2026, excluding March-May 2020. The crude prices included are Arab Light (Saudi Arabia), Iran Heavy (Iran), Basrah Medium (Iraq), Murban (UAE), Oman Crude (Oman), ESPO Kozmino (Russia).

Source: Platts, OPEC, Kpler, GS Global Investment Research

Two-Sided Risks to Prices, but Skewed to the Upside in the Short-Run Short-Run Upside Risks to Prices on Geopolitical Risks, but Medium-Run Downside

Risks to Prices as Flows Have Proven to Be Able to Recover Fast After a Deescalation

Exhibit 11: Brent Could Overshoot \$110/bbl in 2026Q4 if the Gulf Export Recovery Continues to Stall, Delaying the Production Rebound and Requiring a Larger Demand Response  
![](images/bfefdc667f930e295cbb0ac3ea7ed0add3a77a32cb70f2237d73e22417cb9164.jpg)  
Source: ICE, GS Global Investment Research

## Disclosure Appendix

## Reg AC

We, Yulia Zhestkova Grigsby, Alexandra Paulus and Daan Struyven, hereby certify that all of the views expressed in this report accurately reflect our personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Yulia Zhestkova Grigsby GS & Co. LLC, Alexandra Paulus GS & Co. LLC, Daan Struyven GS & Co. LLC.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for information purposes only and is not, and under no circumstances should be construed as, an advertisement, offering or solicitation by GS & Co. LLC for purchasers of securities in Canada to trade in any Canadian security. GS & Co. LLC is not registered as a dealer in any jurisdiction in Canada under applicable Canadian securi

[中间内容因长度限制已省略]

ttempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g.,

marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
