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
# Oil Tracker: Negative Supply News From Gulf and Russia

\- Spot Brent futures prices increased to around \$80/bbl this Wednesday as President Trump said a ceasefire with Iran was over following yesterday's escalation in the Strait of Hormuz.

☐ One LNG and two oil tankers were hit by drones near the Omani coast in the Strait on Tuesday, triggering a US response including revoking the waiver on sales of Iranian oil and launching strikes against Iran Tuesday night.

☐ Iran retaliated with strikes against Bahrain and Kuwait saying it will not allow “interference” in the Strait, while the US conducted additional strikes against Iran Wednesday night.

☐ The recent attacks on tankers highlight still elevated risks of crossing, and shippers may hesitate to cross under the currently unclear ceasefire status, weighing on near-term Hormuz flows.

\- Our estimated oil flows from the Persian Gulf recovered to above 80% of pre-war flows within the first 10 days after Hormuz reopening as trapped tankers rushed to leave the Persian Gulf, but retreated to the low-70s% of normal (16-17mb/d, 7-day moving average) following recent attacks on tankers (Exhibit 1).

☐ Hormuz flows accounted for all the pick-up in Persian Gulf flows as our estimated oil exports through the Strait recovered to 10mb/d or 1/2 of pre-war flows within the first 10 days after the MoU but decreased to 8.3mb/d recently (7-day moving average) (Exhibit 2).

The recent attacks in the Strait support our view that Iran's willingness, rather than lack of transportation capacity, is the main constraint for a swift flows recovery.

\- Combined transportation capacity of oil tankers in the proximity of the Strait of Hormuz is at 926mb, with empty oil tanker capacity inside the Gulf more than $50\%$ higher than loaded volumes (Exhibit 3).

☐ The cancellation of the US sanctions waiver may weight again on imports of Iranian oil that had just started picking up but remain down 0.8mb/d year-over-year (Exhibit 4).

☐ While Middle Eastern producers have started reopening their shut-in wells over the last month, Hormuz disruptions could slow down the production recovery.

Yulia Zhestkova Grigsby  
+1(646)446-3905 |  
yulia.grigsby@gs.com  
GS & Co. LLC

Alexandra Paulus +1(212)902-7111 | alexandra.paulus@gs.com GS & Co. LLC

Filippo Cuscito +44(20)7051-9073 | filippo.cuscito@gs.com GS International

## Daan Struyven

Daan Struyven +1(212)357-4172 | daan.struyven@gs.com GS & Co. LLC

We estimate that Persian Gulf crude production was still down 10.5mb/d in June vs. its pre-war level (Exhibit 5).

We see two-sided risks to Persian Gulf flows (and hence near-term prices):

☐ If the 60-day negotiations continue along with a reinstated waiver on Iranian oil and security reassurances for shippers, we still expect Persian Gulf flows to recover by the end of July, which would require a 6.6mb/d ramp up in Hormuz flows (Exhibit 6).

☐ While not our base case, if the negotiations fail and attacks on tankers escalate along with a potential US blockade of Iranian oil, Persian Gulf flows may decrease further.

\- Our global visible stocks counter bottomed mid-June, avoiding all-time lows, and has built by 3.9mb/d over the first three weeks since the Hormuz reopening (Exhibit 7).

☐ The rapid ramp-up in Persian Gulf flows amid still soft Asia oil demand allowed stocks to build as China has been postponing crude imports until very recently.

While high-frequency stocks data are noisy and can be revised, we note a 6.5mb/d decline in our global visible stocks counter over the last week driven by a drop in products in transit, likely following recent attacks on Russia refineries.

The acceleration in drone attacks on Russian refineries, oil tankers, and mid-stream oil infrastructure has kept refinery margins at very high levels despite higher Persian Gulf flows and some pick-up in global ex Russia refinery runs.

☐ European diesel margins vs. Brent climbed to \$60/bbl today (vs. \$25/bbl a year ago) following Russia’s diesel export ban announcement, while US diesel margins rose to \$75/bbl.

☐ Russia refinery outages jumped to 3.8mb/d, suggesting that over 1/2 of Russia refining capacity is offline (Exhibit 8).

☐ Russia refinery runs are down 2.0mb/d year-over-year, weighing both on domestic products supply and products exports (Exhibit 9).

\- Russia gasoline and diesel retail prices increased by over 10% over the last two months to all-time highs, and fuel shortages are reported in nearly every region (Exhibit 10).

☐ As its effective capacity to refine crude into products has dropped, Russia is redirecting more crude for exports.

\- Russia crude exports are up 1.1mb/d from a year ago, while refined products exports decreased by 0.9mb/d from a year ago, led by diesel (-0.6mb/d yoy) (Exhibit 11).

☐ The ramp up in Russia refinery attacks amid low products stocks and still low Middle East and Asia runs amplifies our high-for-longer products margins view.

## 1) Persian Gulf Flows

Exhibit 1: Oil Exports From the Persian Gulf Are at 71% of Normal Levels, Down from the 83% June Peak Right Before the First Attack on a Crude Tanker Since the MoU on June 27

![](images/79f89dde9dae9becc7b274689f2ac51bb2ce9dc62810a5c0dc5fe259b20dda41.jpg)

Yanbu is on the west coast of Saudi Arabia, bordering the Red Sea and connected to Saudi eastern oil fields via the East-West pipeline. Fujairah lies east (outside) of the Strait of Hormuz and is connected to Abu Dhabi's onshore fields via the Abu Dhabi Crude Oil Pipeline (ADCOP). The Gulf of Oman connects the Strait to the Arabian Sea (southeast). The Kirkuk-Ceyhan pipeline allows northern Iraqi crude to be pumped through Turkiye to the Mediterranean sea. "Normal" flows are assumed to be 20mb/d for Strait of Hormuz and 2025 average for Yanbu (1.4mb/d), Fujairah (1.7mb/d), Gulf of Oman (0mb/d), and Botas Ceyhan (0mb/d).

Source: Kpler, S&P Global Commodities at Sea, GS Global Investment Research

Exhibit 2: Flows Through the Strait of Hormuz Stand at $42\%$ of Normal Levels (7-Day Moving Average)  
![](images/d4fe7199720742089384a5df6abead8f8744950484ef07441bafca0bed245211.jpg)  
Oil exports are estimated by taking an average of S&P and Kpler data on the daily number of oil tankers crossing the Strait of Hormuz and scaling by the average oil volumes per vessel since March 1 from Kpler. Normal oil volumes are assumed to be $20\mathrm{mb / d}$ .  
Source: Kpler, S&P Global Commodities at Sea, GS Global Investment Research

Exhibit 3: We Estimate That Empty Oil Tankers Within the Strait or Within 5 Days of Navigation Have the Capacity to Load 926mb  
![](images/acf725a5d2aa7cd5d8532f1515260230552f6ed9857996080eb020881f8dfd2a.jpg)  
Source: Kpler, GS Global Investment Research

![](images/4633d6348fc4e307713233c3dd19a029954c715249b0f7bef3c18badfcf3096b.jpg)

Exhibit 4: Global Imports of Iranian Oil Have Edged Up Since the US Sanctions Waiver But Remain 0.8mb/d Below Year-Ago Levels  
![](images/bf0de0ede6b84c3e2a6c82544d90019bf87995ec1df1f915bd5632cfbe592087.jpg)  
Source: Kpler, GS Global Investment Research

![](images/8eabddef5a8d4e0ea53ba4002b03975383c433e1fd2319619caeb6b9270ee47a.jpg)

Exhibit 5: We Estimate Gulf Crude Production Losses in June at Around 10.5mb/d

<table><tr><td colspan="3">Average Persian Gulf Crude Oil Production Losses in June vs February (mb/d)</td></tr><tr><td></td><td>GS Balance (June 15)</td><td>Kpler (as of June 19)</td></tr><tr><td>Iran</td><td>0.8</td><td>1.0</td></tr><tr><td>Iraq</td><td>2.7</td><td>2.6</td></tr><tr><td>Kuwait</td><td>1.8</td><td>1.4</td></tr><tr><td>Qatar</td><td>1.1</td><td>1.1</td></tr><tr><td>Saudi Arabia</td><td>3.0</td><td>2.9</td></tr><tr><td>UAE</td><td>1.0</td><td>0.6</td></tr><tr><td>Total Gulf</td><td>10.5</td><td>9.5</td></tr></table>

Excludes Neutral Zone.  
Source: Kpler, GS Global Investment Research

Exhibit 6: Normalization in Oil Exports From Gulf Producers to Their Pre-War Level May be Achieved With a 6.6mb/d Increase in Hormuz Flows From Current Levels  
![](images/12c7febcca102483712d8321d3ebcc2c11daf499b21505f2070672ce0cab10d6.jpg)

Yanbu is on the west coast of Saudi Arabia, bordering the Red Sea and connected to Saudi eastern oil fields via the East-West pipeline. Fujairah lies east (outside) of the Strait of Hormuz and is connected to Abu Dhabi's onshore fields via the Abu Dhabi Crude Oil Pipeline (ADCOP). The Gulf of Oman connects the Strait to the Arabian Sea (southeast). The Kirkuk-Ceyhan pipeline allows northern Iraqi crude to be pumped through Turkiye to the Mediterranean sea.

## 2) Stocks

Exhibit 7: Our Global Visible Stocks Counter Has Bottomed Mid-June and Now Stands Only 0.2mb/d Below Its Year-Ago Level

![](images/5fd11a9c28ccc06762d40d9f0165be194e73887a95cd6094a5b640a791078599.jpg)  
Source: IEA, Kpler, DOE, Euroilstocks, ARA PJK, PAJ, Haver, GS Global Investment Research

## 3) Russia Runs and Flows

Exhibit 8: Russia Total Refinery Outages Are 3.2mb/d Above Their Historical Seasonal Norms  
![](images/cf0f3ad1a3733bf6718d955b35259c26c1653f1ac072229d9f39419a419ce87d.jpg)  
Source: IIR, GS Global Investment Research

Exhibit 9: Russia Refinery Runs Have Declined by 2.0mb/d Since Year Ago  
![](images/0f96799f3294323caabe6f45f06b2d6ff32a5c18d9af46dd5816eced87afb16d.jpg)  
Source: Kpler, GS Global Investment Research

Exhibit 10: Russia Retail Diesel/Gasoline Prices Have Increased by $12\% / 10\%$ Over the Last Two Months  
![](images/32505a7632063a96c29c2165cc5cf9c7ab2483689e056a7b4beefd095fab7dd2.jpg)  
Source: Federal State Statistics Service, Central Bank of the Russian Federation, GS Global Investment Research

Exhibit 11: Russia Crude Exports Increased by 1.3mb/d Year-to-Date While Refined Products Exports Decreased by 0.8mb/d  
![](images/8afaa57bde383fbbc60caeb72f2e4c141613506942548be9b047daff31914310.jpg)  
Source: Kpler, GS Global Investment Research

Exhibit 12: Russia Net Exports of Crude/Condensate Are Up 1.7mb/d From Their Average Seasonal Level, While Net Exports of Refined Products Are Down 1.0mb/d Driven by Gasoil/Diesel

![](images/48cdd59eb145fc73ff0cc4c4355ecad6c4a12c7d041b52ec7697889ce4898e3a.jpg)  
Source: Kpler, GS Global Investment Research

## Disclosure Appendix

## Reg AC

We, Yulia Zhestkova Grigsby, Alexandra Paulus, Filippo Cuscito and Daan Struyven, hereby certify that all of the views expressed in this report accurately reflect our personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Yulia Zhestkova Grigsby GS & Co. LLC, Alexandra Paulus GS & Co. LLC, Filippo Cuscito GS International, Daan Struyven GS & Co. LLC.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Disclosure

Iran is subject to comprehensive sanctions by the United States.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; $1\%$ or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

Additional disclosures required under the laws and regulations of jurisdictions other than the United States
The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for information purposes only and is not, and under no circumstances should be construed as, an advertisement, offering or solicitation by GS & Co. LLC for purchasers of securities in Canada to trade in any Canadian security. GS & Co. LLC is not registered as a dealer in any jurisdiction in Canada under applicable Canadian securities laws and generally is not permitted to trade in Canadian securities and may be prohibited from selling certain securities and products in certain jurisdictions in Canada. If you wish to trade in any Canadian securities or other products in Canada please contact GS Canada Inc., an affiliate of The GS Group Inc., or another registered Canadian dealer. Hong Kong: Further information on the securities of covered companies referred to in this research may be obtained on request from GS (Asia) L.L.C. India: Further information on the subject company or companies referred to in this research may be obtained from GS (India) Securities Private Limited, Research A

[中间内容因长度限制已省略]

attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
