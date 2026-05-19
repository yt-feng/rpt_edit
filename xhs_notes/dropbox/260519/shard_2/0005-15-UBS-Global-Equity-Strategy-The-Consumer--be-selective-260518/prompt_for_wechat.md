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
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
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
1. `# 标题`：一句主判断，不超过 32 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Global Equity Strategy

# The Consumer: be selective

We look at consumer plays in Europe, US and China.

Our concerns about the European consumer. There are several headwinds for the European consumer. First, even if the conflict ends tomorrow, we are left with gas at elevated price levels (120% above pre-conflict scenario in Q4 26), oil at 40% above pre-conflict scenario in end-26 (each 10% on oil takes 0.2% off consumption), food being affected by fertiliser prices (we are at peak planning season and if fertiliser prices are up c30%, then this leads to a c10% increase in food prices, adding c0.5% to CPI) and potentially higher rates (UBS forecast 2 rate hikes compared to none pre-conflict and we estimate each 50bps on rates taking 0.3% off consumption). The offset would be fiscal gifts to the household (which appear to be tiny compared to 2022/3), dis-saving (with current savings ratios being abnormally high) and slightly higher wage growth (though the ECB wage tracker shows little sign of this). Thus, we think it is quite feasible that consumption is c1%+ lower than pre-conflict estimates. Even employment growth has faded, running at just 0.1% QoQ in Q1 and 0.5% YoY in EZ and is negative in the UK.

The consumer sectors, particularly retailing, outperforms when the Euro or Sterling strengthen (as typically they have more dollar costs than revenues). UBS forecasts EUR/USD at 1.14 by year-end (although on the global strategy team we see significantly upside risks to this forecast).

What's in the price? The following consumer sectors have de-rated more than 10% since 26/2: European and Global household products, Global luxury & European retailing. The following sectors are now more than 1.5std cheap (relative to their normal P/E against the market): European and Global household products and Beverages, Global luxury, and European retailing. The aggregate basket of consumer cyclicals is trading close to its norm (on a 8% discount to the market) despite being oversold. The consumer staples are abnormally cheap (7% discount to the market compared to average premium of 25%) but face huge disruptive issues (i.e., Gen Z, GLP1 and, above all, Agentic Agents de-branding non conspicuous brands).

# Where would we focus on the consumer side globally:

The China consumer: UBS have turned more positive on China property (see here) with property accounting for c60% of household wealth. Also, China consumption should be aided by some modest acceleration in wage growth (from 2% to 4%) and the end of deflation. In the long run, the China's consumer share of GDP has to rise. This backs up a buy on L'Oreal (17% of sale to China), luxury and Chinese domestic brand (Yum Brands, Li Ning and Moutai).

Don't give up on luxury: 26% of luxury spend is from the China cluster. The P/E relative to global markets is 0.8 std deviations cheap against its norm globally (36% premium versus norm of 45% premium) and critically: i) EPS is now back to trend (having been 100% above); ii) EPS estimates are very conservative (consensus has EPS being 2% less than the Eurostoxx - close to historic lows); iii) Earnings momentum (though poor) is much better than performance (hence the de-rating of c10% since 26/2); iv) the US cluster is now almost as big as China and there is a clear positive wealth effect (if 0.2% of the equities gains in the US ytd were spent on luxury items, then global luxury spend would rise by c4%); v) we think high end/hard luxury is amongst the sectors least disrupted by Gen AI; and vi) the sector is 2.7 std oversold. We have a buy on Richemont.

# Equity Strategy

Global

Andrew Garthwaite

Strategist

andrew.garthwaite@ubs.com

+44-20-7567 4343

Marc el Koussa

Strategist

marc.el-koussa@ubs.com

+44-20-7567 0298

Ryanair: the low-cost carriers get a huge competitive advantage when the cost of oil rises in what is a structurally much better industry. The stock trades on a 2% discount to its fleet value on 2027 estimates. Easyjet trades on a 76% discount to fleet value.

Household products: have seen the biggest de-rating of any sectors, are 2.5 std cheap globally (and 2.7 std cheap in Europe), and are abnormally oversold. We struggle to understand why they are perceived to be more disrupted than any other sector. The teams have buys on Reckitt Benckiser and Colgate (the latter has positive earnings revisions in the past 3 months).

Spain: If there is a bright spot for European consumer, then it is Spain (it accounts for a quarter of EZ employment growth) with employment up 2.3% yoy fuelled by net migration of 1.3% yoy and house prices rising 13% yoy. Moreover, Spain with c75% of power from nuclear and renewables is one of the most resilient EU countries to higher oil/gas prices. The sizeable consumer proxy would be consumer banks (i.e., Santander), Inditex (buy rated and 17% of sales are from Spain).

Stock screen: If we screen for names that rank well in Europe on valuation (P/E, P/B), earnings revisions, price momentum, crowding and quality, then the best ranked buys are Zalando, Inditex, Carlsberg, Heineken, L'Oreal, and ABI. If we look at names that are at least 1 std cheap on P/E relatives, buy rated with positive earnings revisions, then we would look at Carlsberg, Heineken, and M&S.

# Where do we find ourselves cautious:

Underweight autos: P/E is not that cheap (with P/E relative to the market 5% above their norm in EU and 63% Globally) with the sector only having de-rated 4% since 26/2. Global margins are at average levels but there are both huge structural and cyclical pressures. The structural headwinds being: China competition; over-investing because of both the need to invest in both ICE and EV; legacy car markets have up to 60% cost disadvantage compared to new entrants in EV according to BCG, with additional uncertainties over the appropriate technologies. There are also large cyclical pressures: with the rise in aluminium and memory prices; US light vehicle car sales are down 6% yoy and used car prices are now falling. A rise in EV sales depresses margins (according to UBS). Historically, autos (owing to financing divisions) underperform if credit spreads rise and UBS forecast spreads to rise. Earnings momentum looks poor (ranking 24 out of 27 in Europe and bottom globally). The team have sells on Nissan, Volvo, and Renault.

We prefer the pure battery players (i.e., LGES and CATL) to those autos pivoting into batteries.

Low end US consumer faces substantial headwinds: we find ourselves relatively cautious because: i) real wage growth is likely to turn negative as core PCE rises to 3.2%; ii) employment PMIs imply slower employment growth; iii) excess savings have been largely utilised (apart from the top income decile), iv) earnings momentum of retailing is rolling over with P/E relative to the market (ex-Amazon) for retailing close to its norm (at 4% discount to the market). The positives would be a strong dollar and the wealth effect (10% on equities can add up to 1.5% to consumption but this helps the high-end consumer with the richest 20% of the population accounting for 40% of consumption and owning 83% of equities). Those names most exposed to the US low-end consumer (who is disproportionately hit by higher oil but they don't own much equities) include Jet Blue and Kohls.

# Contents

# The Consumer: be highly selective....4

The European consumer....mounting headwinds....4

Other headwinds for the European consumer stocks: 7

Where are the pockets of value:....10

China consumer....15

Spain – a port on a storm in Europe for the consumer. 16

Underweight global Autos. 17

Low-end US consumer looks set to disappoint....20

Screens. 24

Appendix....27

Andrew Garthwaite

Strategist

andrew.garthwaite@ubs.com

+44-20-7567 4343

Marc el Koussa

Strategist

marc.el-koussa@ubs.com

+44-20-7567 0298

# THE CONSUMER: BE SELECTIVE

In this note, we highlight the headwinds for the European consumer but highlight where we see pockets of value (i.e., household products, luxury, budget airlines). We also highlight why we want to focus on the China consumer. We want to be cautious of the low-end US consumer. We stay underweight of autos.

# The European consumer....mounting headwinds

The European consumer seems to face the following headwinds.

Real wage growth is likely to turn negative: The ECB Eurotracker wage index shows nominal wage growth to be around 2.3% and with headline inflation likely to rise to 3.4% on UBS forecasts, real wage growth could at one point fall by 50 to 100bps. Wages are already growing less strongly than inflation in Europe if we look at the Indeed Survey (for new employees).

Figure 1: ECB wage trackers shows c2.3% wage growth but UBS forecast CPI inflation to rise to 3.4%   
![](images/c4002ec5b5b6ba7443adef2505362a3dc028a746d5694557a1987ee027848e89.jpg)

<details>
<summary>line</summary>

| Date       | ECB wage growth yoy% | UBS headline inflation (base case) |
|------------|----------------------|------------------------------------|
| January-2025 | 5.0%                 | 2.2%                               |
| April-2025  | 4.5%                 | 2.1%                               |
| July-2025   | 4.0%                 | 2.0%                               |
| October-2025| 3.5%                 | 2.1%                               |
| January-2026| 2.0%                 | 1.9%                               |
| April-2026  | 1.8%                 | 2.6%                               |
| July-2026   | 2.5%                 | 3.5%                               |
| October-2026| 2.6%                 | 3.4%                               |
| January-2027| 2.5%                 | 3.4%                               |
| April-2027  | 2.5%                 | 2.6%                               |
| July-2027   | 2.0%                 | 2.1%                               |
| October-2027| 2.3%                 | 2.2%                               |
</details>

Source: UBS, Haver

Figure 2: European real wage growth on the Indeed Survey is now negative   
![](images/92868d2cbee4140385c2c12cf275294650ccb1df50c690745849ef999f735181.jpg)

<details>
<summary>line</summary>

| Month   | Europe real wage growth on indeed (yoy% ch) | UK real wage growth on indeed (yoy% ch) |
|---------|-----------------------------------------------|------------------------------------------|
| Jan-19  | ~1.5%                                         | ~3.5%                                    |
| Oct-19  | ~0.5%                                         | ~2.0%                                    |
| Jul-20  | ~2.5%                                         | ~3.5%                                    |
| Apr-21  | ~-2.0%                                        | ~3.0%                                    |
| Jan-22  | ~-3.0%                                        | ~-1.0%                                   |
| Oct-22  | ~-6.0%                                        | ~-4.0%                                   |
| Jul-23  | ~-2.0%                                        | ~1.0%                                    |
| Apr-24  | ~1.5%                                         | ~4.5%                                    |
| Jan-25  | ~1.0%                                         | ~3.0%                                    |
| Oct-25  | ~0.5%                                         | ~1.0%                                    |
</details>

Source: UBS, Haver, Refinitiv Datastream

Employment growth is weak: UBS forecast employment growth of 0.6% in the EZ and 0.8% in the UK. We can see downside risks to this with employment growth in EZ in Q1 up just 0.5% YoY and 0.1% QoQ and UK employment growth actually contracting YoY and QoQ - and for most regions employment is contracting.

Figure 3: Latest employment growth in Eurozone & select European countries 

<table><tr><td colspan="3">2026 Q1 Employment growth</td></tr><tr><td>Region</td><td>QoQ %</td><td>YoY%</td></tr><tr><td>UK</td><td>-0.01%</td><td>-0.25%</td></tr><tr><td>Italy</td><td>0.12%</td><td>0.03%</td></tr><tr><td>Germany</td><td>0.05%</td><td>-0.28%</td></tr><tr><td>Netherland</td><td>0.00%</td><td>0.34%</td></tr><tr><td>Spain</td><td>0.32%</td><td>2.46%</td></tr><tr><td>France</td><td>-0.15%</td><td>-0.17%</td></tr><tr><td>EU 27</td><td>0.11%</td><td>0.58%</td></tr><tr><td>EZ</td><td>0.10%</td><td>0.50%</td></tr></table>

Source: UBS, Haver

Employment PMIs tend to have fallen quite sharply and seem to be consistent with 0.3% employment growth.

Figure 4: UK Employment PMI vs Vacancy growth   
![](images/a5d05682a012781d363c9647e3a29e7b3a275053a91a236eb55b00cfd0573499.jpg)

<details>
<summary>line</summary>

| Year | UK employment PMI | UK vacancies growth, 3m ann,RHS |
|------|---------------------|----------------------------------|
| 2006 | ~53                 | ~10%                             |
| 2009 | ~37                 | ~-40%                            |
| 2012 | ~50                 | ~20%                             |
| 2015 | ~58                 | ~40%                             |
| 2018 | ~52                 | ~-10%                            |
| 2021 | ~58                 | ~60%                             |
| 2024 | ~45                 | ~-20%                            |
</details>

Source: UBS, Refinitiv Datastream

Figure 5: Europe employment PMIs vs employment growth   
![](images/c4f72a980d8793485b40c8cec1168de2d0d4d3c643674b491b24ae6b0ea9e40b.jpg)

<details>
<summary>line</summary>

| Year | Eurozone composite PMI employment | Europe employment growth (%QoQ, chg), rhs |
|------|------------------------------------|---------------------------------------------|
| 2021 | 49.5                               | 51.0                                        |
| 2022 | 55.5                               | 4.5                                         |
| 2023 | 52.0                               | 2.0                                         |
| 2024 | 49.5                               | 1.5                                         |
| 2025 | 49.0                               | 1.0                                         |
| 2026 | 50.0                               | 0.5                                         |
</details>

Source: UBS, Refinitiv Datastream

Commodity prices: there are three particular hits to commodity prices that we worry about being more permanent, even if the Middle East conflict were to end very soon.

Food. Fertiliser prices are up c30% which pushes up food prices by c10% (the IMF actually highlight that half of the increase in fertiliser prices feeds through to food prices). While food has a large weighting in CPI (14% in EU21 and 11% in UK), large proportion of the prices are relatively fixed. Thus, the rise in fertilizers prices could lead to a c50bp CPI (see here). We hear reports of farmers not being able to afford fertiliser. This will just mean that yields are lower (pushing up food prices).

Oil: each 10% on the oil prices takes 0.2% off consumption, using the ECB ready reckoner. If we just take the forward curve a year out to be the predictor of the oil price, then the 1-year forward oil price is 15% higher than 26-2 levels and thus implying a 0.3% hit to consumption, with UBS forecasting (under a 5 week disruption scenario) oil at the end of 2026 to be \$86pb - 40% higher than pre 26th February forecasts, resulting in a 80bps hit to consumption. In the short term, companies hedge or may temporarily take the hit in profit margin. In the long term, they cut costs (i.e. wages) or raise prices. Neither is good for the consumer.

Gas: UBS forecast a TTF price of €74 by Q4 26 (i.e. up 60% from current levels and 120% above pre 26-2 forecasts). Gas sets the price of electricity in c60% of countries, and gas and electricity is c5% of CPI. Hece, it is quite possible that a much higher gas prices takes up to 40bps off consumption. This comes through with a lag as countries tend to set electricity prices slowly in response to a rise in gas prices.

Rates: UBS now see two rate rises this year (prior to the Middle East crisis it was none). 50bps on rates takes about 30bps off consumption (with a 1-year lag on ECB data).

It is quite possible that gas, oil, food, and rates means that consumption growth is c2% lower than the pre-conflict scenario, without any of the offsets discussed below.

# What are the offsets?

The consumer starts off with one clear advantage compared to the period preceding the invasion of Ukraine. Specifically, the consumer has excess savings of c10% of GDP in both the UK and Europe and the savings ratio in the UK and EZ are still 3.5% and 3% above pre-Covid levels, respectively. This is to be contrasted with the US where the savings ratio is 4% below pre-covid levels.

Figure 6: Excess savings are 10% of GDP   
![](images/f421a8abf93d7c11518decc72e54c3cb19ec6095038aef71ef5161f060c0f133.jpg)

<details>
<summary>bar_stacked</summary>

| Quarter | Germany (RHS) (%) | France (RHS) (%) | Italy (RHS) (%) | Spain (RHS) (%) | Rest (RHS) (%) | Savings rate (LHS) |
|---|---|---|---|---|---|---|
| 1Q-20 | 12 | 10 | 5 | 5 | 0 | 170 |
| 2Q-20 | 12 | 10 | 5 | 5 | 0 | 180 |
| 3Q-20 | 12 | 10 | 5 | 5 | 0 | 190 |
| 4Q-20 | 12 | 10 | 5 | 5 | 0 | 195 |
| 1Q-21 | 13 | 10 | 5 | 5 | 0 | 205 |
| 2Q-21 | 13 | 10 | 5 | 5 | 0 | 200 |
| 3Q-21 | 13 | 10 | 5 | 5 | 0 | 205 |
| 4Q-21 | 13 | 10 | 5 | 5 | 0 | 205 |
| 1Q-22 | 13 | 10 | 5 | 5 | 0 | 205 |
| 2Q-22 | 13 | 10 | 5 | 5 | 0 | 205 |
| 3Q-22 | 13 | 10 | 5 | 5 | 0 | 205 |
| 4Q-22 | 13 | 10 | 5 | 5 | 0 | 205 |
| 1Q-23 | 13 | 10 | 5 | 5 | 0 | 205 |
| 2Q-23 | 13 | 10 | 5 | 5 | 0 | 205 |
| 3Q-23 | 13 | 10 | 5 | 5 | 0 | 205 |
| 4Q-23 | 13 | 10 | 5 | 5 | 0 | 205 |
| 1Q-24 | 13 | 10 | 5 | 5 | 0 | 205 |
| 2Q-24 | 13 | 10 | 5 | 5 | 0 | 205 |
| 3Q-24 | 13 | 10 | 5 | 5 | 0 | 205 |
| 4Q-24 | 13 | 10 | 5 | 5 | 0 | 205 |
| 1Q-25 | 13 | 10 | 5 | 5 | 0 | 205 |
| 2Q-25 | 13 | 10 | 5 | 5 | 0 | 205 |
| 3Q-25 | 13 | 10 | 5 | 5 | 0 | 205 |
9.6% of GDP in Q4, Q4, Q4, Q4, Q4, Q4, Q4, Q4, Q4, Q4, Q4, Q4, Q4, Q4, Q4, Q4, Q4, Q4, Q4, Q4, Q4, Q4, Q4, Q4, Q4, Q4, Q4, Q4, Q4, Q4, Q4, Q4, Q4, Q4, q4, q4, q4, q4, q4, q4, q4, q4, q4, q4, q4, q4, q4, q4, q4, q4, q4, q4, q4, q4, q4, q4, q4, q4, q4, q4, q4, q4, q4, q4, q4, q4, q4, q6, q6, q6, q6, q6, q6, q6, q6, q6, q6, q6, q6, q6, q6, q6, q6, q6, q6, q6, q6, q6, q6, q6, q6, q6, q6, q6, q6, q6, q6, q6, q6, q6, q6 |
| Q3-25* (Last Quarter) - Savings rate (LHS) = (9.6% of GDP in Q4, Q4) - The chart displays the percentage of GDP allocated to savings rates for Germany (RHS), France (RHS), Italy (RHS), Spain (RHS), and Rest (RHS). The data series are extracted quarterly from Q3-25 to Q3-26. The values for each quarter are labeled on the chart.
</deta

[中间内容因长度限制已省略]

y recommendations or opinions in such this publication or material are not made or provided to you, and (ii) to the maximum extent permitted by law (a) indemnify UBS and its associates or related entities (and their respective Directors, officers, agents and Advisors) (each a 'Relevant Person') for any loss, damage, liability or claim any of them may incur or suffer as a result of, or in connection with, your unauthorised reliance on this publication or material and (b) waive any rights or remedies you may have against any Relevant Person for (or in respect of) any loss, damage, liability or claim you may incur or suffer as a result of, or in connection with, your unauthorised reliance on this publication or material. Korea: Distributed in Korea by UBS Pte. Ltd., Seoul Branch. This report may have been edited or contributed to from time to time by affiliates of UBS Pte. Ltd., Seoul Branch. This material is intended for professional/institutional clients only and not for distribution to any retail clients. Malaysia: This material is authorized to be distributed in Malaysia by UBS Malaysia Sdn. Bhd (Capital Markets Services License No.: CMSL/A0063/2007). This material is intended for professional/institutional clients only and not for distribution to any retail clients. India: Distributed by UBS India Private Ltd. (Corporate Identity Number U67120MH1996PTC097299) 2/F, 3 North Avenue, Maker Maxity, Bandra Kurla Complex, Bandra (East), Mumbai (India) 400051. Phone: +912261556000. It provides brokerage services bearing SEBI Registration Number: INZ000259830; Merchant Banking services bearing SEBI Registration Number: INM000013101; and Research Analyst services bearing SEBI Registration Number: INH000001204. Name of Compliance Officer Mr. Parameshwaran Shivaramakrishnan, Phone: +912261556151, Email: ol-ubs-sec-compliance@ubs.com Registration granted by SEBI, and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. UBS may have debt holdings or positions in the subject Indian company/companies. UBS may have financial interests (e.g. loan/derivative products, rights to or interests in investments, etc.) in the subject Indian company/companies from time to time. Within the past 12 months, UBS may have received compensation for non-investment banking securities-related services and/or non-securities services from the subject Indian company/companies. The subject company/companies may have been a client/clients of UBS during the 12 months preceding the date of distribution of the research report with respect to investment banking and/or non-investment banking securities-related services and/or non-securities services. With regard to information on associates, please refer to the Annual Report at: https://www.ubs.com/global/en/about\_ubs/investor\_relations/annualreporting.html The Research Annual Compliance Report for UBS India Private Limited is available on www.ubs.com/ubssi under Research tab. Taiwan: Except as otherwise specified herein, this material may not be distributed in Taiwan. Information and material on securities/instruments that are traded in a Taiwan organized exchange is deemed to be issued and distributed by UBS Pte. LTD., Taipei Branch, which is licensed and regulated by Taiwan Financial Supervisory Commission. Save for securities/instruments that are traded in a Taiwan organized exchange, this material should not constitute "recommendation" to clients or recipients in Taiwan for the covered companies or any companies mentioned in this document. No portion of the document may be reproduced or quoted by the press or any other person without authorisation from UBS. Indonesia: This report is being distributed by PT UBS Sekuritas Indonesia and is delivered by its licensed employee(s), including marketing/sales person, to its client. PT UBS Sekuritas Indonesia, having its registered office at Sequis Tower Level 22 unit 22-1,Jl.Jend. Sudirman, kav.71, SCBD lot 11B, Jakarta 12190. Indonesia, is a subsidiary company of UBS AG and licensed under Capital Market Law no. 8 year 1995, a holder of broker-dealer and underwriter licenses issued by the Capital Market and Financial Institution Supervisory Agency (now Otoritas Jasa Keuangan/OJK). PT UBS Sekuritas Indonesia is also a member of Indonesia Stock Exchange and supervised by Otoritas Jasa Keuangan (OJK). Neither this report nor any copy hereof may be distributed in Indonesia or to any Indonesian citizens except in compliance with applicable Indonesian capital market laws and regulations. This report is not an offer of securities in Indonesia and may not be distributed within the territory of the Republic of Indonesia or to Indonesian citizens in circumstance which constitutes an offering within the meaning of Indonesian capital market laws and regulations.

The disclosures contained in research documents produced by UBS AG, London Branch or UBS Europe SE shall be governed by and construed in accordance with English law.

UBS specifically prohibits the redistribution of this document in whole or in part without the written permission of UBS and in any event UBS accepts no liability whatsoever for any redistribution of this document or its contents or the actions of third parties in this respect. Images may depict objects or elements that are protected by third party copyright, trademarks and other intellectual property rights. © UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/0aa8bf886e57106657ff3afbc14b894262df4639b5b14ae8f0344442e96a72bf.jpg)

# UBS
"""
