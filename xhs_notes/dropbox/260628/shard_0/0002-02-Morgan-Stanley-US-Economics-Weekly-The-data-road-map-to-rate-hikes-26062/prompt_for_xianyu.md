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
## The data road map to rate hikes

Incoming data since the June FOMC meeting make us marginally more comfortable in our outlook for a Fed that stays on hold this year. That said, data has to cooperate and we lay out our views about what inflation and labor market data may change our thinking.

## Key Takeaways

<table><tr><td colspan="2">MS &amp; CO. LLC</td></tr><tr><td colspan="2">Michael T Gapen</td></tr><tr><td colspan="2">Chief US Economist</td></tr><tr><td>Michael.Gapen@morganstanley.com</td><td>+1 212 761-0571</td></tr><tr><td colspan="2">Sam D Coffin</td></tr><tr><td colspan="2">Economist</td></tr><tr><td>Sam.Coffin@morganstanley.com</td><td>+1 212 761-4630</td></tr><tr><td colspan="2">Diego Anzoategui</td></tr><tr><td colspan="2">Economist</td></tr><tr><td>Diego.Anzoategui@morganstanley.com</td><td>+1 212 761-8573</td></tr><tr><td colspan="2">Arunima Sinha</td></tr><tr><td colspan="2">Global Economist</td></tr><tr><td>Arunima.Sinha@morganstanley.com</td><td>+1 212 761-4125</td></tr><tr><td colspan="2">Heather Berger</td></tr><tr><td colspan="2">Economist</td></tr><tr><td>Heather.Berger@morganstanley.com</td><td>+1 212 761-2296</td></tr><tr><td colspan="2">Lingdi Xu</td></tr><tr><td colspan="2">Economist</td></tr><tr><td>Lingdi.Xu@morganstanley.com</td><td>+1 212 761-2957</td></tr></table>

Our outlook for inflation is more sanguine than the average Fed participant; we suspect the Fed's forecasts were formed before oil prices fell sharply.

We expect m/m rates of core PCE and CPI inflation of 0.2% or below in the coming months.

If monthly rates of core inflation remain at 0.3% m/m or higher, or if the conflict in the Middle East resumes, then our thinking could change.

\- Our outlook also calls for a moderation in employment growth.

If the unemployment rate falls below 4.0%, the Fed may see risks of an overheating labor market as justifying rate hikes.

Exhibit 1: We expect deceleration in both headline and core PCE inflation...  
![](images/db1d895e688d0bd620b47c80460cadb908a6b078fc93e8ea98deb7989934b864.jpg)  
Source: BEA, MS forecasts. Note: MS forecasts in dashed bars.

Exhibit 2: ...and forecast payroll growth slows this summer  
![](images/9c72f98ae1c5cba626c9a8161bd8d1c82818a7f79ad9a58df74c1db27503f3e6.jpg)  
Source: BLS, MS

## The Data Road Map to Rate Hikes

## We expect a Fed-on-hold through year-end

Following the June FOMC meeting, we retained our outlook for a Fed on hold in 2026 despite 9 FOMC participants who submitted a projection with at least one rate hike this year. We retained our baseline outlook for no rate hikes for several reasons. First, our forecast for inflation is more sanguine. We believe tariff pass through is ending, paving the way for substantial disinflation in core goods over the next year, and the recently signed MOU between the US and Iran has helped push oil prices back toward pre-conflict levels. In addition, we look for further moderation in shelter inflation and some payback from residual seasonality into year end. On net, and following the release of May PCE inflation, our forecast of 4Q/4Q headline and core PCE inflation of 3.2% and 3.0% this year is substantially below the median FOMC participant.

Second, we suspect that FOMC participants' projections may be overstating inflation pressures. In March, FOMC participants had to form their inflation projections shortly after the conflict began. Without knowing the duration of the conflict, participants likely underestimated how much inflation would firm in subsequent months. In June, we think the Fed may be overstating inflation pressures since forecasts were likely formed before the MOU took hold. Nine FOMC participants submitted forecasts of 4Q/4Q headline inflation at 3.5-3.6%, while 8 participants submitted forecasts between 3.7-4.2%. This suggests the average inflation forecast lies above the median forecast. We think these are too high in light of the subsequent decline in energy prices.

Third, we believe most of the 9 dots projecting rate hikes this year are Reserve Bank presidents that may not be voters; we think it is likely that the majority of voters on the committee prefer the status quo policy setting despite the evolution of the outlook. These voters are likely more comfortable with this outlook in light of incoming data since the conclusion of the June meeting.

Finally, consumer spending has softened, in both as-reported and revised data, and we view recent payroll gains as outsized due, in part, to a catch-up effect in hiring following the implementation of protectionist trade policies last year. If the Fed is patient, we expect FOMC voters to prefer the current policy stance over a more restrictive one.

Exhibit 3: Oil prices came down since mid-June  
![](images/4ef1876d6f8e49a7723fcbfb4b8801f2d47cbe901757816541ce96c29a51c3ec.jpg)  
Source: Bloomberg, MS.

Exhibit 4: FOMC participants' projections may be overstating inflation pressures  
![](images/907ab5a70c7e91bb0e9313c15f208929cf2ea4ab4580e0cd1d631a0a18410d9d.jpg)  
Source: BEA, Federal Reserve, MS forecasts.

## The Road Map to Rate Hikes

That said, our outlook for monetary policy in 2026 is depending on several conditioning assumptions which may not hold and we detail how data could evolve in a way that leads us to change our outlook in favor of rate hikes. We focus most of our attention on our outlook for the data flow in June through August given that the Fed will see this data before it meets in September. If the Fed wants to raise rates in July, then it seems unlikely that any data between now and then will sway the Fed's thinking. Hence, we frame the data road map in terms of what may kick the Fed into action in September, or keep it on hold longer.

On the inflation front, the Fed's projections assume monthly run rates that persisted from April through December of 2025, which could result from core goods inflation closer to 0.2% m/m on account of elongated tariff pass through or more robust second-round effects from higher energy prices. This would mean m/m rates of core inflation of around 0.3%. In our forecast, core CPI and PCE inflation run slightly below 0.2% m/m, on average, in the three releases between June and August. Hence, upside surprises to core could lead us to change our thinking.

In addition, oil futures prices point to substantial payback in energy prices in June and July, with energy prices in PCE inflation set to fall by about 5.0% and 2.6%, respectively. Should the MOU between the US and Iran not hold and subsequent hostilities re-close the strait, then our forecast for monthly declines in headline CPI inflation (-0.16% and -0.04% m/m in June and July) and roughly flat readings on headline PCE inflation (0.02% m/m on average) may not materialize. This would represent a higher probability of our oil risk premium scenario, where headline inflation remains firm and second round effects on core materialize.

In the labor market, we expect recent payroll gains (114k per month from January to May and 188k over the past three months) to moderate. We project increases of 50-60k per month on average over the summer (total nonfarm and private), which should keep the unemployment rate roughly steady near current levels. Should payroll gains outperform our expectations and push the unemployment rate below the median FOMC participants' estimate of the longer run neutral rate (4.2%), then the Fed may decide a more restrictive stance is needed to prevent labor market overheating. We think a move below 4.0% on the unemployment rate by September would increase cause for concern that the labor market is much stronger than thought.

Finally, we also acknowledge that data may not be the deciding factor for some participants. A year ago, the Fed viewed its policy stance as inappropriate in light of their view that downside risk to employment outweighed upside risk to inflation. Some of the nine projections for rate hikes may reflect a reversal in this risk management approach; they may see the distribution of risks as skewed sufficiently in the direction of firmer inflation and view the current policy stance as inappropriate. In other words, subjective assessments about the distribution of outcomes around the modal path may be enough for hikes, diminishing the influence of incoming data.

For now, we retain our outlook for no rate hikes from the Fed this year. While incoming data since the June FOMC have made us marginally more comfortable in this view, we remain attentive to the data and will adjust our views accordingly as the economy evolves.

Average monthly change, 000s  
Exhibit 5: We forecast deceleration in both headline and core PCE inflation  
![](images/a977dac48b4f4d7787f56dbf0eb52f9ba4b5cffcd2de1819d6e86f0990958e5f.jpg)  
Source: BEA, MS forecasts. Note: MS forecasts in dashed bars.

Exhibit 6: We forecast slower payroll growth  
![](images/41e9334eb856fa8f0de4d4d53892f60b419ad9ff8642938a7c8c430bc2de4e3e.jpg)  
Source: BLS, MS

# Oil Tracker: US ending stocks of crude oil edge lower amid increased exports and unchanged production

We continue to track the evolution of petroleum-product inventory and production. US stocks of crude oil and petroleum products, which represent the EIA's estimate of how many barrels of oil and petroleum products are physically sitting in US storage at period end, continue to move lower. Inclusive of the SPR, inventory is falling by about 2mn barrels a day. The spot price of oil for immediate purchase and delivery in the physical market remains high despite futures prices declining since the MOU between the US and Iran.

US domestic crude production has edged modestly higher in recent weeks, but it remains about in line with pre-conflict production. Net imports of oil (imports - exports) are declining because of increased oil exports.

Exhibit 7: US ending stocks of crude oil continue to move lower  
![](images/08b663caef3559b13c64c7157d6faffb66dac5c7a0602d5009e60376d9e3d14d.jpg)  
Source: Energy Information Administration, Haver Analytics, MS

Exhibit 8: Prices of oil in the physical market have eased but remain higher than before the Iran conflict  
![](images/2500e3764f748717227caf8ff9f7956e57ea57d41ee3881fb817171d01baf18a.jpg)  
Source: Energy Information Administration, Haver Analytics, MS

Exhibit 9: Including the SPR, US oil stocks are falling about 2mn barrels per day  
![](images/8e8de36ae3424d3916fa094e725a4e05e63ac20595509c308a49b044e47256c1.jpg)  
Source: Energy Information Administration, Haver Analytics, MS  
Exhibit 10: US domestic oil production remains broadly unchanged

Exhibit 11: US exports of oil and petroleum products have risen, pushing down net imports of these energy goods  
![](images/8c19037f37289bca74d55e185fc4cef9489a8dff5fdad4e910c514d7b318b4a8.jpg)  
Source: Energy Information Administration, Haver Analytics, MS

US Net Imports of Crude Oil and Petroleum Products (Thous.Barrels per Day)  
Exhibit 12: US imports of oil have decelerated a little while exports have picked up  
![](images/5b6f175377c13417bd2bc7825ec35d5fb967879b16bc8c993d19dec5c9b2631b.jpg)  
Source: Energy Information Administration, Haver Analytics, MS

![](images/32c90192775ae6413c3a07baff8a0557df2b9e13bf334f824966f0d0e2ab7b75.jpg)  
Source: Energy Information Administration, Haver Analytics, MS

# Financial Conditions: A near-reversal following the April 7 ceasefire

Following the conflict in the Middle East and the uncertainty it brings to the next steps for monetary policy, we include the evolution of our FRB/US-based model of financial conditions, which aims to capture how changes in asset prices weigh on future economic activity. The index includes five daily variables: the 10-year Treasury yield, S&P 500 returns, the corporate BBB credit spread, the valuation of the U.S. dollar, and the price of oil. These are aggregated based on their estimated growth elasticities relative to the federal funds rate, using the Federal Reserve's FRB/US model. As a result, the index can be interpreted as the equivalent change in the federal funds rate, expressed in basis points, required to generate a similar effect on economic activity.

Since hostilities in the Middle East began on February 28, the tightening in financial conditions is equivalent to about a 40bp rise in the federal funds rate. The tightening reversed all of the easing seen earlier this year, most of which occurred between the December and January FOMC meetings and was primarily driven by a weaker U.S. dollar. The net tightening since February 28 has been driven mainly by a weaker U.S. dollar, with higher 10-year U.S. Treasury yields playing a secondary role. Buoyant equity markets have offset some of the tightening. Since the hawkish June FOMC meeting, financial conditions have tightened by 22 bp, primarily driven by U.S. dollar depreciation and weaker stock market returns.

Exhibit 13: Financial conditions have tightened following the conflict in the Middle East

![](images/43507c291ca93079ab7a825fb7eaaca80bb41d29d0853f09032e6310a56e9bef.jpg)  
Source: Bloomberg, MS

# The effective tariff rate, tariff receipts and refunds

## The tariff rate on US imports has fallen to 8.3% in 1Q26 data

On February 20, 2026, the Supreme Court struck down the President's authority to impose tariffs under IEEPA. Section 122 tariffs will replace IEEPA tariffs in the short term, though uncertainty rises after the 150-day period when Congress would need to extend those tariffs. Replacing IEEPA with Section 122 tariffs of 15% and considering composition effects of US imports, we estimate baseline tariffs near 11%. Our estimate of "core" tariffs (ex fuels, gold and AI-related imports) remains closer to 13-14%. In our view, near-term tariffs are likely capped below 'Liberation Day' levels, at least until Section 232 and 301 investigations are complete. In the April 2026 data, the effective tariff rate is estimated at \~6.9%, and the 1Q26 tariff rate averages to 8.3%.

Exhibit 14: US effective tariff rate  
![](images/ed537852319f6e972ed9e433f58ff5e1760e84aeb4a4e4df0148d8a7c0053dc3.jpg)  
Source: US Census, US HTS, USITC, MS

Exhibit 16: Cash withdrawals from the DHS - CBP, as a proxy for tariff refunds  
![](images/f5c91b8f34816fd8d2359372e6a8fbad2bd0ac073d56619f797938e850b2b4e4.jpg)  
Source: US Treasury, Haver Analytics, MS

Exhibit 15: US Treasury: Customs and excise deposits from tariffs  
![](images/0d87eddc19aebccb7c3274407da94609802f56900505c0c690c0d4c5729aeb2c.jpg)  
Source: US Treasury, Bloomberg, MS

Tariff refunds represent cash returned to importers when customs duties were previously overpaid or later determined to be refundable, for different reasons including a tariff exclusion or court-ordered refund, or a drawback claim tied to goods that are exported or destroyed. The process generally runs through CBP, where importers or brokers submit the relevant claim and supporting documentation; CBP then reviews eligibility, confirms the entry and status, and certifies approved refunds for payment. In Treasury cash-flow data, we monitor these payments at high frequency through CBP-related withdrawals in the Daily Treasury Statement. We interpret this as a tariff-refund proxy.

## 2Q GDP tracking trimmed $\frac{1}{2}$ point to 2.5%

1Q GDP revisions and April-May consumer spending data showed much softer consumer spending growth than we had known. 1Q consumption was cut to 0.5% from 1.4% because of services, which are now reported at 0.5% growth instead of 1.8%. (The BEA sharply reduced its estimates of consumption growth in financial services—not the most reliable series—and international travel.) Add to that a downward revision to April goods spending, and we are now tracking 2Q consumption at 1.9% instead of 2.9%.

Year-to-date, the implication is a sharper slowing in cons

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
