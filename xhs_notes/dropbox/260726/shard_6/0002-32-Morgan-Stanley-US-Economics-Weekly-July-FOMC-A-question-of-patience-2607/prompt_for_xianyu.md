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
# US Economics Weekly | North America

# July FOMC: A question of patience

Recent data have strengthened the case for a patient Fed, with softer payrolls and easing inflation. We expect the Fed to keep rates on hold next week and through the remainder of the year. Risks remain skewed toward higher rates, particularly following the recent escalation in the Middle East.

## Key Takeaways

We expect the Fed to hold rates at 3.50–3.75% in July, with recent labor market and inflation data supporting a patient, wait-and-see approach.

■ Labor market overheating concerns have eased and last CPI report suggests that, absent additional shocks, more disinflation might be in the pipeline.

■ Upside risks to rates include persistently high oil prices, a more hawkish Fed reaction function, or stronger AI-driven investment lifting neutral rates.

The temporary Section 122 tariff bridge expired earlier today, but we expect the broader tariff regime to remain, combining section 301 and 232 authorities.

Our baseline remains that the statutory effective tariff rate converges toward \~10% by year-end, similar to levels before the expiration of section 122 tariffs.

Exhibit 1: Higher oil prices remain a risk to our outlook for disinflation  
![](images/96d5cace6afd8c895d8b0fbad44824476e028c2e5cdb1a1ad622951abe930362.jpg)  
Source: Bloomberg, MS

<table><tr><td colspan="2">MS &amp; CO. LLC</td></tr><tr><td colspan="2">Michael T Gapen</td></tr><tr><td colspan="2">Chief US Economist</td></tr><tr><td>Michael.Gapen@morganstanley.com</td><td>+1 212 761-0571</td></tr><tr><td colspan="2">Sam D Coffin</td></tr><tr><td colspan="2">Economist</td></tr><tr><td>Sam.Coffin@morganstanley.com</td><td>+1 212 761-4630</td></tr><tr><td colspan="2">Diego Anzoategui</td></tr><tr><td colspan="2">Economist</td></tr><tr><td>Diego.Anzoategui@morganstanley.com</td><td>+1 212 761-8573</td></tr><tr><td colspan="2">Arunima Sinha</td></tr><tr><td colspan="2">Global Economist</td></tr><tr><td>Arunima.Sinha@morganstanley.com</td><td>+1 212 761-4125</td></tr><tr><td colspan="2">Heather Berger</td></tr><tr><td colspan="2">Economist</td></tr><tr><td>Heather.Berger@morganstanley.com</td><td>+1 212 761-2296</td></tr><tr><td colspan="2">Lingdi Xu</td></tr><tr><td colspan="2">Economist</td></tr><tr><td>Lingdi.Xu@morganstanley.com</td><td>+1 212 761-2957</td></tr></table>

<table><tr><td>MS | RESEARCH2026 EXTEL GLOBALFIXED INCOME POLL</td><td>We appreciate your supportVOTE NOW★★★★★</td></tr></table>

## July FOMC: A question of patience

## Despite a rebound in oil prices, hikes are less compelling

The question hanging over the July FOMC meeting is whether the Fed will display patience or whether it has run out of patience. We believe the former. At next week's meeting, we expect the Fed to keep the target range for the federal funds rate unchanged at 3.50-3.75%. Since the committee met in June, the bulk of incoming data supports patience, in our view. The June employment report revealed a moderation in hiring and saw downward revisions to prior months. The rebound in hiring early in the year remains evident, but now appears shorter lived than the as-reported data suggested. Nonfarm payrolls rose 57k on the month, and longer-term averages are about in line with our estimate of breakeven payroll growth (\~50k per month), leaving the unemployment rate little changed at 4.2%. Wage growth in terms of average hourly earnings is up only 3.5% y/y. Risks to the labor market appear balanced to our eyes and concerns about overheating have diminished.

Recent inflation data suggest to us that disinflation has begun. Headline CPI prices declined 0.4% and core was flat. Our three drivers of disinflation — a reversal in energy prices, the end of tariff pass-though, and diminishing shelter inflation — all contributed to the soft print. The tariff pass-through to core goods prices has now been flat since February, providing a strong signal that the corporate sector has adequately adjusted prices to account for higher production costs. If so, our estimates suggest as much as 60-70bp of disinflation may be in the pipeline, providing an important source of disinflation. As we note below, we think the resolution of Section 232 and 301 reviews this week will move tariffs back to their IEEPA-based rates over time, but not above.

On net, we think the committee will read the data as we do and remain on hold in July. Inflation has shown enough improvement to buy more time and keep the Fed on the sideline. We think subsequent inflation prints will continue to point to disinflation — our m/m readings on core inflation in the second half of that year annualized close to 2.0% — and expect the Fed to remain on hold through year end.

That said, there are clear risks to our outlook in the direction of higher policy rates. First, the Fed could conclude the distribution of risks to the dual mandate favors a tighter policy stance. Second, our inflation forecast could be wrong and renewed escalation in the Middle East and the rebound in oil prices will lead to a higher oil risk premium outcome, boosting core inflation through second-round effects. Third, committee members may conclude that monetary policy is not restrictive with inelastic AI-related capital spending boosting neutral rates of interest. Fourth, Chairman Warsh may have a much more hawkish reaction function than we think. Will he seek to establish his inflation-fighting bona fides and bolster Fed independence with rate hikes now to help inflation converge to 2.0% more quickly? We do not think so, but we cannot rule it out. He has repeatedly said the Fed would achieve price stability, but has not said how that will be done. If we are wrong on the Fed in July, it is likely because the reaction function has changed and we are still thinking like the prior reaction function.

Exhibit 2: Core goods CPI reflects an end to tariff pass through  
![](images/e3d39aad4962862bc777c7294cd48750966a8a3dc0f69594514dd2e340692d6f.jpg)  
Source: BLS, MS.

Exhibit 3: Higher oil prices remain a risk to our outlook for disinflation  
![](images/fced5b7072c1ff3f4860bec40fc7141819c605e52df3c7f1bbad05089face48c.jpg)  
Source: Bloomberg, MS.

## The hand-off in tariffs

The temporary Section 122 tariff bridge expired earlier today, but we expect the broader tariff regime to remain. The 10% surcharge was limited to 150 days and applied through 12:01 a.m. EDT on July 24. We expect that the tariff regime will now be a combination of the section 301 and 232 authorities. USTR has already issued findings and proposed 10–12.5% duties in the forced-labor Section 301 cases. The July 7–9 hearings are complete, and the proposal has cleared the principal public-hearing stage, although USTR has not yet issued final action. USTR has also already completed a separate Section 301 investigation into Brazil, imposing 25% tariffs on non-exempt Brazilian imports effective July 22. The U.S. Department of Commerce has a Section 232 pipeline covering robotics and industrial machinery, medical products, wind turbines, unmanned aircraft systems and polysilicon. We therefore view today as a handoff rather than a tariff cliff: the procedural groundwork for new Section 301 action and additional sectoral Section 232 measures is advanced, but the timing, scope and interaction of those measures remain uncertain.

Our baseline remains that the statutory effective tariff rate converges toward roughly 10% by year-end. We expect Section 301 to carry a broad country-level floor, while Section 232 provides a more targeted sectoral overlay in strategic and capital-intensive goods. We also expect that while the statutory rate ends up in the 9–10% range, actual collections can differ because of exemptions, bilateral deals, refund timing and import composition, including the rising share of zero-tariff AI hardware. The replacement framework should also be more durable than the IEEPA/Section 122 regime: Sections 301 and 232 require investigations, findings and formal implementation processes, but neither faces Section 122's 150-day statutory sunset. The tariff regime is therefore less likely to carry legal and rollover risk, though not necessarily less implementation uncertainty.

Exhibit 4: Recent tariff authorities

<table><tr><td>Authority</td><td>Primary rationale</td><td>Typical scope</td><td>Process</td><td>Expected role in the tariff regime</td><td>Current example</td></tr><tr><td>Section 122 of the Trade Act of 1974</td><td>Fundamental balance-of-payments problems</td><td>Broad import surcharge or quota, generally applied uniformly</td><td>Tariff capped at 15%; maximum 150 days unless extended by Congress</td><td>Temporary bridge</td><td>10% surcharge expiring July 24</td></tr><tr><td>Section 301 of the Trade Act of 1974</td><td>Unjustifiable, unreasonable or discriminatory foreign practices that burden US commerce</td><td>Broad country- or practice-level action across goods and potentially services</td><td>USTR investigation, findings and public process; no explicit tariff-rate cap; actions subject to a four-year continuation process</td><td>Broad tariff baseline and country-specific enforcement</td><td>Proposed forced-labor baseline; 25% Brazil action</td></tr><tr><td>Section 232 of the Trade Expansion Act of 1962</td><td>Imports that threaten to impair national security</td><td>Product-, sector- and derivative-specific</td><td>Commerce report within 270 days; presidential determination and implementation process; response can include tariffs or negotiations</td><td>Strategic sectoral overlay</td><td>Metals, autos, semiconductors, pharma</td></tr><tr><td>Section 338 of the Smoot-Hawley Tariff Act of 1930</td><td>Foreign discrimination or unequal treatment that disadvantages US commerce</td><td>Country- and product-specific</td><td>Additional duties of up to 50%; at least 30 days before effectiveness; can be amended or escalated to import exclusion</td><td>Bilateral escalation and tail-risk tool</td><td>Recent Canada actions</td></tr></table>

Source: USTR, US Code, White House, MS

The US decision not to extend USMCA at the July 1 review does not itself change our Public Policy team's view on the year-end tariff baseline, as the agreement remains in force. But it moves the process into annual reviews. The new Section 338 tariffs only on Canada also do not materially alter our baseline tariff rate path, but they raise the uncertainty around it, especially as they break through the USMCA protection. The notice imposes additional 50% duties on nearly \$20 billion of selected Canadian imports beginning August 19, including USMCA-compliant goods, while excluding energy, potash, Section 232 goods and several other categories. We estimate that if imposed, these 50% duties would add \~0.2 percentage point to the aggregate tariff rate. While that is not enough to move our year-end baseline materially, the use of Section 338 adds a rapid, high-rate and country-specific tool with no fixed sunset. Both the USMCA moving into annual reviews, and the announcement of the 338 tariffs widen the range of outcomes for North American supply chains, creating more scope for future country- or product-specific escalation.

# Oil Tracker: Price rise and inventory stabilization

Since the Middle East conflict intensified a week ago, oil prices have risen. Only the price data here are reported since the recent re-escalation in the conflict. Next week's data on production, exports, and inventory could show responses to the new strains.

We continue to track the evolution of petroleum-product inventory and production. US stocks of crude oil and petroleum products, which represent the EIA's estimate of how many barrels of oil and petroleum products are physically sitting in US storage at period end, inched up from a low level. However, the stocks of crude oil in the Strategic Petroleum Reserve (SPR) fell to around 311 million barrels, its lowest level since April 1984. The Energy Department said the SPR's minimum inventory is determined by 'cavern mechanics,' which, when applied across the full system, translates to a conservative operational minimum of about 70 million barrels. If the SPR continues to decline at roughly its recent pace of 30 million barrels every four weeks, inventories would approach the operational minimum by the end of February 2027.

After the signing of the MOU between the US and Iran, the spot price of oil for immediate physical delivery approached its pre-conflict level. However, following the recent re-escalation, both spot prices and futures prices have risen meaningfully, renewing concerns about inflation.

US domestic crude production has edged modestly higher in recent weeks. Net imports of oil and petroleum (imports - exports) initially declined as exports increased but have returned to earlier levels.

Exhibit 5: US ending stocks of crude oil and petroleum products edged up recently  
![](images/d70582569e728e0faded8bfa8bbefb6888ccb86d85077d3a3acf03465fa8c61d.jpg)  
Source: Energy Information Administration, Haver Analytics, MS

Exhibit 6: Following the recent re-escalation, the spot price of oil for immediate physical delivery has risen meaningfully.  
![](images/5fd5ad44123035504a82ce53721151ad40fc05f3c341cbaeeb9968d1f113be96.jpg)  
Source: Energy Information Administration, Haver Analytics, MS

US Domestic Production of Crude Oil (Thous.Barrels per Day)

Exhibit 7: Including the SPR, US oil stocks are now falling only 1mn barrels per day  
![](images/af857a34ce24d6044e7cb69ddee93d34fd154578ec50f457c1b7ff4dbfd057e0.jpg)  
Source: Energy Information Administration, Haver Analytics, MS  
Exhibit 9: US exports of crude oil trended down over the past two months, pushing up net imports of crude oil and petroleum products

Exhibit 8: US domestic oil production has been rising gradually  
![](images/1bd82724cfc0e43578ebd4769861656e95c1fe201922c4228171fb034b271a33.jpg)  
Source: Energy Information Administration, Haver Analytics, MS  
US Net Imports of Crude Oil and Petroleum Products (Thous.Barrels per Day)

![](images/39b0c308c9dd0ac20e542b71525c6c1736fb2e6ea91e2834b37a9b5efa57d0a5.jpg)  
Source: Energy Information Administration, Haver Analytics, MS

Exhibit 10: US exports of oil decelerated following the signing of the MOU  
![](images/3b25a0cc8e6f85e33956912a00fc2003ff4a606d42bdb937ceec8df4e2cce481.jpg)  
Source: Energy Information Administration, Haver Analytics, MS

## Financial Conditions: More restrictive

Following the conflict in the Middle East and the uncertainty it brings to the next steps for monetary policy, we include the evolution of our FRB/US-based model of financial conditions, which aims to capture how changes in asset prices weigh on future economic activity. The index includes five daily variables: the 10-year Treasury yield, S&P 500 returns, the corporate BBB credit spread, the valuation of the U.S. dollar, and the price of oil. These are aggregated based on their estimated growth elasticities relative to the federal funds rate, using the Federal Reserve's FRB/US model. As a result, the index can be interpreted as the equivalent change in the federal funds rate, expressed in basis points, required to generate a similar effect on economic activity.

Since hostilities in the Middle East began on February 28, the tightening in financial conditions is equivalent to about a 67bp rise in the federal funds rate. The tightening since February 28 reversed the easing seen earlier in the year, most of which was driven by a weaker U.S. dollar. The net tightening since February 28 has been driven mainly by a reversal in dollar weakness and higher 10-year U.S. Treasury yields.

The contribution from oil prices disappeared for a couple of weeks following the MOU between Iran and the U.S., but has now reappeared d

[中间内容因长度限制已省略]

P-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi

Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the United States by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## © 2026 MS
"""
