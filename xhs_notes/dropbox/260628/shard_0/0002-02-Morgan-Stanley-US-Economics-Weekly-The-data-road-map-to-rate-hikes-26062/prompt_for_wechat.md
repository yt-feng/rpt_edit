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
- 已识别机构名：`摩根斯坦利`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

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

Year-to-date, the implication is a sharper slowing in consumer spending growth—a 1.2% rate of growth in H1 2026. Residual seasonality and higher tariffs appear to have weighed on consumption. Before today's revisions, we had been surprised at the resilience in spending; now, we are instead surprised at the softness reported in 2Q services. We are also alert to the fragility of that estimate. It is so far based on very little input data: underlying services spending measures from the Quarterly Services Survey will not be available until about a month and a half from now. Before then, the services estimates are more judgmental.

In our 2Q tracking, we are building in 2.7% goods spending and 1.6% services spending, with the apprehension that the services could be heavily revised once the services company revenues are finally pulled into 2Q GDP in about two months.

The result is 2Q GDP tracking at a 2.5% q/q annual rate rather than the 3.0% we expected a week ago. The May and June trade data and June retail sales could still alter our forecast materially. Also, we have held off on estimating the impact of the falling SPR, which won't affect headline GDP but will shift spending away from government consumption and toward private inventory investment.

Following the 2.1% real GDP growth in 1Q, the 2.5% growth in 2Q puts the recent run rate at slightly above last year's 2.1% 4Q/4Q real GDP growth.

The Atlanta Fed tracking for 2Q also fell to a 2.5% q/q annual rate from 3.0%. However, their forecasts include more strength in business investment and show a drag from trade rather than the boost we have. The New York Fed 2Q GDP Nowcast was about unchanged at 2.7%.

Exhibit 17: The effect of incoming data on our US GDP tracking estimate

<table><tr><td colspan="14">Details of Q2 2026 US GDP tracking (% q/q saar unless indicated)</td></tr><tr><td rowspan="2">Date</td><td rowspan="2">Data release</td><td rowspan="2"></td><td colspan="9">Final</td><td>NX (level)</td><td rowspan="2">CPI (level)</td></tr><tr><td>GDP</td><td>sales</td><td>PCE</td><td>Res</td><td>Equip</td><td>Struct</td><td>IPP</td><td>Gov</td><td>X</td><td>M</td></tr><tr><td>12-May</td><td>Baseline</td><td></td><td>2.3</td><td>2.3</td><td>1.7</td><td>1.0</td><td>8.0</td><td>-3.0</td><td>8.0</td><td>1.4</td><td>0.0</td><td>-0.1</td><td>-1067</td></tr><tr><td rowspan="2">14-May</td><td>Retail sales</td><td>Apr</td><td>2.4</td><td>2.4</td><td>1.8</td><td>1.0</td><td>8.0</td><td>-3.0</td><td>8.0</td><td>1.4</td><td>0.0</td><td>-0.1</td><td>-1067</td></tr><tr><td>Adjustments</td><td></td><td>2.6</

[中间内容因长度限制已省略]

ts responsibility for its contents; in Korea by MS & Co International plc, Seoul Branch; in India by MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi

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
