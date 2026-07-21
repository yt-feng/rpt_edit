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
# Oil Comment: Hedging Escalation With Diesel Length

■ Lower Gulf flows means higher prices. Escalation in the Middle East and the decline in estimated Persian Gulf flows to below 45% of pre-war levels have pushed oil prices back up (Exhibit 1). The Brent futures curve is now modestly above our \$80/75 forecasts for 2026Q4/2027, which assume de-escalation in 2026Q4.

■ Upside price risks. We see risks to our price forecast as tilted to the upside on net, especially in the near term (Exhibit 2). The key upside price risks are:

□ Shipping disruptions in Hormuz—and potentially the Red Sea—as the estimated 5mb/d rise since the start of the war in pipeline flows via Yanbu to the Red Sea, to more than 6mb/d (Exhibit 3), has played a key role in offsetting part of the decline in Hormuz flows.

☐ Damage to energy infrastructure from the Middle East and Russia-Ukraine wars. While the Iran war has likely not caused lasting major damage to oil production capacity so far, our analysis of the 5 largest prior supply shocks shows an average 42% hit to production in the affected country after 5 years, often reflecting infrastructure damage, underinvestment, or tight sanctions (Exhibit 4).

■ Lower stocks vs. greater flexibility. Brent might exceed \$120/bbl in 2026Q4 and average \$100 in 2027 if Hormuz remains disrupted through 2027 (Exhibit 2, red line). This scenario assumes Gulf output only fully recovers by Dec27, supported by pipeline extensions. The estimated Q2 inventory draw of more than 3mb/d leaves the market more vulnerable than in February, with inventories particularly low for OECD diesel and OECD SPR (Exhibit 5). Still, global visible oil stocks are down only 0.3mb/d year-over-year (Exhibit 6), and the simulated price upside is less high than comparable estimates from the start of the war. This reflects that we now assume greater demand elasticity, more adaptable Mideast supply, and a higher market tolerance for low inventories before it requires aggressive demand destruction.

China has helped stabilize crude markets. The decline in crude import demand remains especially large for China (Exhibit 7), where demand appears highly sensitive to crude purchase prices (Exhibit 8). The 4.7mb/d year-over-year (YoY) decline in China crude net seaborne imports in June reflects both weaker refinery runs and products demand (China retail gasoline sales volumes fell 21% year-over-year), and a shift from stockpiling in 2025 to destocking since the start of the war, with crude destocking estimated at just over 1mb/d in June (Exhibit

Daan Struyven
+1(212)357-4172 |
daan.struyven@gs.com
GS & Co. LLC

Yulia Zhestkova Grigsby
+1(646)446-3905 |
yulia.grigsby@gs.com
GS & Co. LLC

Alexandra Paulus
+1(212)902-7111 |
alexandra.paulus@gs.com
GS & Co. LLC

Filippo Cuscito
+44(20)7051-9073 |
filippo.cuscito@gs.com
GS International

9). In our view, China crude imports need not rebound immediately, especially if prices were to rise further, given still-elevated estimated China oil inventories of roughly 2 billion barrels and its ability to substitute some oil demand by coal and power.

Hedging escalation with diesel length. We recommend that investors and consumers seeking to hedge persistent geopolitical shocks in the Mideast and Russia go long the Dec26-March27 European diesel (“gasoil”) timespread. This spread has potential to rise further—or “roll up” strongly—(Exhibit 10) given fundamental tightness even absent the Iran war, and high exposure to Russia and Mideast refinery outages. We prefer European diesel timespread length to crude, gasoline, or US diesel length for three reasons.

☐ Diesel timespreads over crude. Unlike the crude market, refining and diesel markets were already very tight before the war, with high refining utilization and low diesel stocks (Exhibit 11). As Ukraine continues to scale decentralized drone production, the persistence of record-high Russian refinery outages of nearly 5mb/d (Exhibit 12) is highly plausible, which would likely keep Russia diesel net exports very low (Exhibit 13). Hurricanes, extreme summer heat, and year-to-date significant deferrals in planned maintenance also pose greater downside supply risk to products than to crude.

☐ Diesel over gasoline. We recommend diesel length over gasoline length because Russia refinery outages cause more price upside for diesel than for gasoline, diesel margins tend to rise disproportionately when inventories fall from low levels, diesel demand is less price-elastic and has yet to reach its seasonal peak in Q4, and refiners have limited capacity to raise diesel yields further (Exhibit 14).

☐ European diesel over US diesel. We prefer European diesel over US diesel length because US margins face downside risk from potential policy changes, including export tariffs or lifting of the US Renewable Volume Obligation (RVO), while European refining costs face upside risks, including higher TTF prices.

## Hedging Escalation With Diesel Length

Exhibit 1: Lower Gulf Flows Means Higher Crude Prices  
![](images/a4ea0fb90d2f87dc5697069c8ab5ebd0f77fbdf95e32cc6f7ddcdbc40953b68e.jpg)  
Source: ICE, GS Global Investment Research

## Upside Price Risks

Exhibit 2: Oil Price Risks Are Tilted to the Upside  
![](images/43d30815cbcfbd7c699f738ab8f7fb788c82e87d74c5ab9bdfa672508bb47036.jpg)  
Source: ICE, GS Global Investment Research

## Risks to Shipping Flows

Exhibit 3: The Estimated 5mb/d Rise Since the Start of the War in Pipeline Flows via Yanbu to the Red Sea Has Played a Key Role in Offsetting Part of the Decline in Hormuz Flows

![](images/250e14dfc2c1d8a3662ae2b707cc42f9eb59905d9ae44f2cba7aa3ca9083917a.jpg)  
Source: Kpler, GS Global Investment Research

## Risk to Energy Infrastructure

Exhibit 4: Looking at the Prior Largest Supply Shocks of the Past 50 Years, We Estimate an Average Hit to Production of 42% After 4 Years

![](images/3b04318c04b76a593c1cd32302e3f289e1e27adb5625c72a3222b6bc99a3b6a6.jpg)  
Source: EIA, IEA, GS Global Investment Research

## Lower Inventories

Exhibit 5: Visible Oil Stocks Are Low for OECD Diesel and SPR But High in China and on Water

![](images/7c1a198c7ba0ee05fd216c44d2868348532652b1a66e883b6f47a1ba2cb277da.jpg)  
Contains crude and products unless otherwise specified. DoD stands for days of demand; stocks in DoD is calculated by dividing by 12MMA demand. For OECD commercial diesel/gasoline, the percentiles shown are of monthly deviations from 2017-2026 seasonal averages. \*Global SPR excludes China SPR.  
Source: IEA, Kpler, DOE, Euroilstocks, ARA PJK, PAJ, Haver, GS Global Investment Research

Exhibit 6: Global Visible Oil Stocks Are Down Only 0.3mb/d Year-Over-Year  
![](images/300c12d681c3efe671159472b7e450ec4322bf6a921d6235fd7c90691d5369e4.jpg)  
Source: IEA, Kpler, DOE, Euroilstocks, ARA PJK, PAJ, Haver, GS Global Investment Research

## China Crude Stabilization

Exhibit 7: China Net Seaborne Imports of Crude Are Down 44% Year-Over-Year  
![](images/b561c8a3e30597ff589b0b68769375a2c0aabd9c4d4b96aa651b03a400a4271f.jpg)  
Source: Kpler, GS Global Investment Research

![](images/e350ef2c829580cce248db66d5b789ff9be49e00d720e5cbc8efa07f01f13ab4.jpg)

Exhibit 8: Large Crude Stockpiles Allow China Imports to Be Price-Sensitive and Postpone Imports When Crude Imports Prices Are High  
![](images/a2683248b03e70c0f2dcdc311dc240a4371defc4581c9de0a3c39023475c8139.jpg)  
The sample is January 2017 to June 2026, excluding March-May 2020. The crude prices included are Arab Light (Saudi Arabia), Iran Heavy (Iran), Basrah Medium (Iraq), Murban (UAE), Oman Crude (Oman), ESPO Kozmino (Russia).  
Source: Platts, OPEC, Kpler, GS Global Investment Research

Exhibit 9: We Estimate China Crude Destocking of Just Over 1mb/d

<table><tr><td colspan="3">China Oil Balances: June 2026 (mb/d)</td></tr><tr><td></td><td>Crude</td><td>Refined Products</td></tr><tr><td>1) Domestic Production</td><td>4.2</td><td>12.1</td></tr><tr><td>2) Net Imports</td><td>6.9</td><td>0.0</td></tr><tr><td>3) Demand</td><td>12.1</td><td>12.2</td></tr><tr><td>4) Implied Change in Stocks: (1) + (2) - (3)</td><td>-1.1</td><td>-0.1</td></tr><tr><td>5) Visible Change in Stocks</td><td>-1.0</td><td>-0.4</td></tr><tr><td>(6) Estimated Invisible Stock Changes: (4) - (5)</td><td>-0.1</td><td>0.3</td></tr></table>

We combine estimates of domestic production from the IEA, net imports and visible changes in stocks from Kpler and Petrologistics, crude demand (i.e. refinery runs) from NBS, and refined products demand from S&P Global Market Intelligence. We assume China condensate production of 0.2mb/d and use Petrologistics estimates for pipeline crude imports of 0.8mb/d and railroad refined products imports of <0.1mb/d.

Source: China National Bureau of Statistics, Kpler, S&P Global Market Intelligence, Oilchem, GS Global Investment Research

## Hedging With Diesel Length

Exhibit 10: We Recommend That Investors and Consumers Seeking to Hedge Geopolitical Shocks in the Mideast and Russia Go Long the Dec26-March27 European Diesel Timespread

![](images/e56de46839786c4135f7a5af3cddcb4f874084c9ade049f8e96971e331e05407.jpg)  
Source: ICE, NYMEX, GS Global Investment Research

![](images/ae094699ccb5ce62e613d12cd75abee9403e755959f83ea1954560cea7f15985.jpg)

Exhibit 11: OECD Commercial Distillate Stocks Remain Low  
![](images/590ce32b8dcd8f2906a7beb9b7cf016216c8663198de9002430f172106f18d2c.jpg)  
Source: IEA, GS Global Investment Research

Exhibit 12: Refinery Outages Are Very High in the Mideast and Especially Russia  
![](images/335ac8323b9646f4c73108024afb7018cbe22cce0706b48da2fe729ca1ee9511.jpg)  
Source: IIR, GS Global Investment Research

Exhibit 13: High Russia Refinery Outages Mean Low Russia Diesel Net Exports  
![](images/3b1c80bc20828cf724e6afcb4d18026186624267a818655d3b241052512bc128.jpg)  
Source: Industrial Info Resources, Kpler, GS Global Investment Research

Exhibit 14: US Refiners Likely Have Limited Capacity to Raise Diesel Yields Further  
![](images/49be926154c4041931151809623e03cb78c53eff5d2a418398bbdd88dfa85570.jpg)  
Source: EIA, GS Global Investment Research

## Disclosure Appendix

## Reg AC

We, Daan Struyven, Yulia Zhestkova Grigsby, Alexandra Paulus and Filippo Cuscito, hereby certify that all of the views expressed in this report accurately reflect our personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Daan Struyven GS & Co. LLC, Yulia Zhestkova Grigsby GS & Co. LLC, Alexandra Paulus GS & Co. LLC, Filippo Cuscito GS International.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for information purposes only and is not, and under no circumstances should be construed as, an advertisement, offering or solicitation by GS & Co. LLC for purchasers of securities in Canada to trade in any Canadian security. GS & Co. LLC is not registered as a dealer in any jurisdiction in Canada under applicable Canadian securities laws and generally is not permitted to trade in Canadian securities and may be prohibited from selling certain securities and products in certain jurisdictions in Canada. If you wish to trade in any Canadian securities or other products in Canada please contact GS Canada Inc., an affiliate of The GS Group Inc., or another registered Canadian dealer. Hong Kong: Further information on the securities of covered companies referred to in this research may be obtained on request from GS (Asia) L.L.C. India: Further information on the subject company or companies referred to in this research may be obtained from GS (India) Securities Private Limited, Research Analyst - SEBI Registration Number INH000001493, 10th Floor, Ascent-Worli, Sudam Kalu Ahire Marg, Worli, Mumbai-400 025, India, Corporate Identity Number U74140MH2006FTC160634, Pho

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
