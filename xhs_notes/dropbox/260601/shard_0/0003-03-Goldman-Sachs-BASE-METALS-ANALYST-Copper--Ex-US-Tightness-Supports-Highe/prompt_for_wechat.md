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
# BASE METALS ANALYST

# Copper: Ex-US Tightness Supports Higher Prices

While off the \$14,153 all-time high of mid-May, copper prices remain elevated, up 10% year to date at \$13,600.   
Year-to-date data does suggest that supply recovery from previous disruption events has trailed our expectations. Accordingly, we lower our 2026 global mine supply forecast by 350kt, equivalent to \~1.5% of global mine supply, including \~200kt less from Grasberg (Indonesia) and Kamoa-Kakula (DRC) combined, with neither returning to full capacity until 2028.   
Furthermore, US copper imports in H1 2026 have exceeded our previous forecast, tightening the ex-US balance. As a result, we now expect US inventory to build by 900kt in 2026 (vs. 550kt previously), even as our base case remains that no copper tariff will be announced this year.   
Combined, these factors mean that we now expect the ex-US market to be in a deficit of 640kt/170kt in 2026/2027 (vs. 60kt/40kt deficits previously), leading us to raise our end-2026/average 2027 LME copper forecasts to \$13,735/\$13,800 from \$12,465/\$12,150 previously (vs. forwards at \$13,630/\$13,610). While we expect prices to remain above our 2026 fair value estimate of \$12,600 over the next six months as speculative positioning (reflecting the attractive long-term thematics for copper) continues to support prices above what fundamentals alone would imply, our 2027 price forecast of \$13,800 is in line with our fair value estimate for next year, taking into account the ex-US balance and a stockpiling risk premium.   
While our base case is that the LME copper price remains close to current levels over the coming months, we lay out three alternative price scenarios under different economic and US copper tariff outcomes:

☐ (1) Strait of Hormuz Remains Closed for Longer: While we would expect limited impact on the global copper balance as the demand hit from lower economic growth is largely offset by lower copper supply due to sulfur shortages, a substantial pullback in global risk appetite could push the LME price down to its fundamental support level at \~\$12,600 in H2 2026, before resuming an upward trend.

☐ (2) US Copper Tariff Announced for January 2027: If a US copper tariff is announced prospectively in June 2026, to start in January 2027, we would expect US copper imports to accelerate in H2 2026 (vs. our base case of a

# Aurelia Waltham

+44(20)7051-2547

aurelia.waltham@gs.com

GS International

# Lavinia Forcellese

+44(20)7774-9243

lavinia.forcellese@gs.com

GS International

# Daan Struyven

+1(212)357-4172

daan.struyven@gs.com

GS & Co. LLC

# Samantha Dart

+1(212)357-9428

samantha.dart@gs.com

GS & Co. LLC

slowdown in imports), tightening the ex-US balance and raising prices to over \$14,000 in H2 2026. However, we would expect prices to retreat in 2027 as imports stop once the tariff is imposed.

☐ (3) Announcement of No Copper Tariff: A definitive decision against the tariff would reduce the size of our ex-US deficit forecast in 2026 and push the ex-US market back into surplus in 2027 as imports fall to a negligible level. In this scenario, we would expect the price to fall to an average of \$12,800/t in 2027.

# Copper: Ex-US Tightness Supports Higher Prices

We raise our end-2026/average 2027 LME copper forecasts to \$13,735/\$13,800 from \$12,465/\$12,150 previously (vs. forwards at \$13,630/\$13,610) (Exhibit 1), as we now see the ex-US market tightening more than previously expected in 2026 and 2027. We now forecast the ex-US market to be in a deficit of 640kt/170kt in 2026/2027 (Exhibit 2) (vs. 60kt/40kt previously) as lower mine supply growth tightens the global balance, while higher imports into the US mean less metal is available to the rest of the world where the LME price is set.

Exhibit 1: Two-Sided Risks to our LME Copper Price Forecast   
![](images/49fbc172c34fbd3a7bf6827cb64d61e3f67ca773195f89d1be26dc9e3fd80880.jpg)

<details>
<summary>line</summary>

LME Copper Price
| Date | Copper Price ($/t) | Scenario 1: Strait of Hormuz Remains Closed for Longer ($/t) | Scenario 2: US Copper Tariff Announced for January 2027 ($/t) | Scenario 3: Announcement of No Copper Tariff ($/t) | GS Base Case ($/t) | Futures ($/t) |
|---|---|---|---|---|---|---|
| Jan-25 | 9000 | | | | | |
| Jul-25 | 9800 | | | | | |
| Jan-26 | 13000 | | | | | |
| Jul-26 | 13600 | 13400 | 13800 | 13400 | 13600 | 13600 |
| Jan-27 | 13600 | 12600 | 14400 | 12800 | 13800 | 13600 |
| Jul-27 | 13600 | 13600 | 13800 | 12800 | 13800 | 13600 |
</details>

Source: Bloomberg, GS Global Investment Research

Exhibit 2: We Expect the Ex-US Market to be in Substantial Deficit This Year, Keeping the LME Price Supported   
![](images/7529c86a36ded133afce4fc3f4d5537d974df6422a4fe955f8c1ccf7b1be6965.jpg)

<details>
<summary>bar</summary>

Global Copper Market Balance
| Year | Ex-US (kt) | US (kt) | Global (kt) |
|---|---|---|---|
| 2025 | -80 | 800 | 730 |
| 2026 | -680 | 900 | 260 |
| 2027 | -180 | 380 | 220 |
</details>

Source: CRU, Wood Mackenzie, Bloomberg, GS Global Investment Research

We have removed \~350kt of global copper mine supply from our 2026/2027 balances (Exhibit 3), explaining half of the \~600kt tightening in our ex-US balance since our April update. This is predominantly due to a slower than previously expected recovery in output from the Grasberg and Kamoa-Kakula mines following incidents in 2025. We do not expect either mine to return to full capacity until 2028. Furthermore, scrap has not been providing an offset to the tighter refined balance. In particular, China's domestic scrap output is down 12% YoY YTD, as stricter VAT invoice compliance has reduced the volume of domestic scrap that compliant buyers can source, keeping better-documented imported scrap in strong demand and limiting scrap's ability to substitute for refined copper $^{1}$ (Exhibit 4).

Exhibit 3: We Have Removed \~350kt of Mine Supply in 2026 As the Impacts of Last Year's Mine Supply Disruptions Persist   
![](images/5f4e105d8ff196f5b9da9bd0de89bb80632e4ef0034f4a557d1a5d3558e40454.jpg)

<details>
<summary>bar_stacked</summary>

Change in GS Copper Mine Supply Forecast (May vs. February 2026)
| Year | Grasberg (kt) | Kamoa Kakula (kt) | Other (kt) |
|---|---|---|---|
| 2026 | -350 | -150 | -150 |
| 2027 | -350 | -150 | -150 |
</details>

Source: Visible Alpha Consensus Data, Wood Mackenzie, GS Global Investment Research

Exhibit 4: China Copper Scrap Output Falls 12% YoY YTD on Invoice Scrutiny   
![](images/8f64863c59871613ea58437d5fbe8100636ce5d9e8a6df7196c80364288fdd93.jpg)

<details>
<summary>line</summary>

China Domestic Copper Scrap Output
| Month | 2025 (kt) | 2026 (kt) |
|---|---|---|
| Jan | 220 | 240 |
| Feb | 210 | 205 |
| Mar | 250 | 185 |
| Apr | 210 | 160 |
| May | 230 | - |
| Jun | 270 | - |
| Jul | 240 | - |
| Aug | 220 | - |
| Sep | 200 | - |
| Oct | 190 | - |
| Nov | 225 | - |
| Dec | 240 | - |
</details>

Source: SMM, GS Global Investment Research

While mine supply disruptions tighten the global balance, US import volumes impact the ex-US market, where the LME price is set. We have lifted our 2027 US stock build forecast to 900kt (vs. 550kt previously), widening the ex-US deficit. US imports beat expectations in H1 2026, and we expect US imports to reaccelerate over the coming month, reflecting the now-open import arbitrage. While we expect the pace of imports to slow in H2 2026 and 2027 under our base case of no tariff decision as the market-implied risk of a tariff reduces, we expect some flow of metal into the US to continue (reflecting the risk of a later tariff announcement), keeping the ex-US market in deficit for the next two years.

Exhibit 5: We Expect US Copper Inventory Growth to Accelerate in the Coming Weeks, but Slow in H2 Under the Base Case of No Tariff Announcement   
![](images/a468a89f51d4e0d3b9598e604e6eaf1c7f2b4fd936bd4733d76f41d8118701a7.jpg)

<details>
<summary>bar_line</summary>

US Copper Inventory Change
| Date | US weekly inventory change (including GSe of unreported inventory) (kt) | GS forecast (weekly average) (kt) |
|---|---|---|
| Jan-25 | 0.5 | 0 |
| Feb-25 | 1.2 | 0 |
| Mar-25 | -2.1 | 0 |
| Apr-25 | 13.4 | 0 |
| May-25 | 53.8 | 0 |
| Jun-25 | 17.9 | 0 |
| Jul-25 | 44.3 | 0 |
| Aug-25 | 37.1 | 0 |
| Sep-25 | 47.8 | 0 |
| Oct-25 | 39.2 | 0 |
| Nov-25 | 28.7 | 0 |
| Dec-25 | -4.3 | 0 |
| Jan-26 | 46.9 | 0 |
| Feb-26 | 40.1 | 0 |
| Mar-26 | 50.3 | 0 |
| Apr-26 | 17.3 | 0 |
| May-26 | -1.8 | 0 |
| Jun-26 | 8.4 | 0 |
| Jul-26 | 17.9 | 20 |
| Aug-26 | 17.9 | 20 |
| Sep-26 | -10.8 | 20 |
| Oct-26 | -11.9 | 10 |
The chart displays a bar chart with bars representing weekly inventory changes (including GSe of unreported inventory) and a line chart showing the GS forecast (weekly average). The data is already in English.
</details>

Source: Bloomberg, GS Global Investment Research

Our updated 2026/2027 ex-US balance alone provides copper prices support at \$12,120 in 2026 and \$13,300 in 2027 (Exhibit 6). To this, we add a 25% probability of broad strategic copper stockpiling $^{2}$ , which we estimate can drive an additional \~\$500/t of price support, reflecting what we believe will be sustained market concerns that strategic stockpiling might limit visible inventory builds and support prices above what physical fundamentals alone would imply. This brings our estimated fair value for LME copper to \~\$12,600 in 2026 and \$13,800 in 2027. While the current copper price of \$13,600 sits above our 2026 fair value, the price has been supported by speculative inflows into the market, in part driven by the hard asset rotation, and we do not see a catalyst for reversal in the near term due to copper demand's exposure to strategic sectors such as energy security, AI, and defence, plus the constrained nature of new supply. We see speculative outflows as especially unlikely as the ex-US market looks ahead to a potential tightening as copper imports into the US likely accelerate over the coming months.

Exhibit 6: We Estimate That a 1-Day Decline in the Copper Balance (Inventory Days) Results in a \~1.4% Boost to the LME Price   
![](images/02e14e747818716a8d71de5354cd67a733ac245b8cd45a376afe43a07dccd189.jpg)

<details>
<summary>scatter</summary>

| Year | Balance (Days of Consumption) | YoY LME Copper Price % Change |
|------|-------------------------------|--------------------------------|
| 2026 | -10                           | 20                             |
| 2027 | 0                             | 10                             |
</details>

On an annual average year-over-year basis. Regression based on annual data (1990–2024); LME copper price year-on-year change versus refined balance in days of consumption. The year 2006 is excluded from the sample. The estimated slope of –1.39 indicates that each 1-day change in the balance (equivalent to roughly 75kt of global refined copper) is associated with a \~1.40% change in the copper price. This corresponds to an implied price effect of about +1.85% for each –100kt change in the refined balance. Forecast points (2026–2027 ex-US) are shown for illustration but are not included in the estimation. The price action in 2025 is in line with the model using the ex-US balance, as US inventory is effectively “trapped”.

Source: Bloomberg, CRU, Wood Mackenzie, GS Global Investment Research

While our base case is that the LME copper price remains supported close to current levels in 2026/2027, we lay out three alternative price scenarios under different economic and US copper tariff outcomes.

(1) Strait of Hormuz (SoH) Remains Closed for Longer: Under the scenario that the SoH remains closed for longer than our base case that flows recover by end-June, the LME copper price could fall towards our estimated fair value of \$12,600 in H2 2026. Notably, this fair value remains the same as our base case, as we would not expect any substantial change in either our global or ex-US balances. On the demand front, we previously estimated that a 1pp slowdown in world real GDP growth is associated with a \~0.9pp slowdown in global copper demand growth. Therefore, under our economists' severely adverse scenario of a 1.1pp hit to global economic growth, this would result in \~300kt lower copper demand in 2026 vs. our February forecast. However, we would expect this to be largely offset by lower supply stemming from tightness in the sulfur/sulfuric acid market. Our base case does not account for these potential sulfur-related disruptions, but industry feedback suggests that \~125kt of DRC output is at risk from the lack of sulfur flowing through the SoH, and a further \~200kt in Chile is at risk from China's sulfuric acid export restrictions.

Furthermore, we note that copper demand's increasing exposure to strategic sectors may provide some limit to the demand hit vs. historical economic slowdowns. We expect more than 60% of copper demand growth by 2030 (vs. 2025) to come from grid and power infrastructure as AI and defence place grids – many of which are old and vulnerable in DMs – at the centre of energy security. Demand from these critical sectors is likely to be (1) less sensitive to an economic slowdown than cyclical sectors such as construction or white goods, and (2) less sensitive to high copper prices. For example, Chinese apparent copper demand remained resilient at +1% YoY in Q1 2026 (Exhibit 7), despite copper prices trading near all-time highs, as strength in grid and power infrastructure demand (+10% YoY YTD) helped offset weakness in solar and EV-related demand. We have also close to doubled our global datacentre copper demand YoY growth forecast for 2026/27, reflecting the latest update from our global datacentre team (although we note that the majority of copper demand from datacentres comes indirectly via grid and power infrastructure investment).

Exhibit 7: Chinese Apparent Copper Demand Remained Resilient at $+1\%$ YoY in Q1 2026   
![](images/0c66afc20eee00a8c152a8aa87d7471ceaa87bfe253616cd2b329012e0c0b77a.jpg)

<details>
<summary>line</summary>

China Copper Apparent Demand
| Month | 2019 - 2023 range (kt) | 2024 (kt) | 2025 (kt) | 2026 (kt) |
|---|---|---|---|---|
| Jan | 600 | 1180 | 1180 | 1180 |
| Feb | 700 | 1000 | 1050 | 950 |
| Mar | 1280 | 1200 | 1380 | 1550 |
| Apr | 1300 | 1220 | 1480 | - |
| May | 1300 | 1230 | 1450 | - |
| Jun | 1300 | 1180 | 1380 | - |
| Jul | 1350 | 1280 | 1360 | - |
| Aug | 1350 | 1320 | 1380 | - |
| Sep | 1350 | 1380 | 1430 | - |
| Oct | 1350 | 1320 | 1250 | - |
| Nov | 1350 | 1450 | 1300 | - |
| Dec | 1350 | 1480 | 1380 | - |
</details>

Source: SMM, Wind, GS Global Investment Research

However, unlike in our base case, where we expect speculative positioning to remain long, keeping the LME price trading above its fair value in 2026, a prolonged closure of the SoH and the resulting lower global economic growth expectations would likely result in a pullback in global risk appetite. We previously estimated a 0.7% short-term boost to copper prices from a 1pp increase (0.1 standard deviation) in net managed money as % of open interest. Using this rule of thumb, a reversal back to the March low of COMEX+LME net managed money positioning as a % of OI (8.4% vs. 18.2% currently) would imply 6.6% of downside to prices, taking copper to \~\$12,700, close to our estimated fair value.

(2) US Copper Tariff Announced for January 2027: If a US copper tariff is announced prospectively in June 2026, to start in January 2027, we would expect US copper imports to accelerate in H2 2026 (vs. our base case of a slowdown in imports), tightening the 2026 ex-US balance and resulting in prices exceeding \$14,000 in H2 2026 $^{3}$ . However, we would expect prices to retreat in 2027 as imports stop once the tariff is imposed. Assuming that all of the global 210kt surplus builds outside of the US in 2027, we would expect the copper price to retreat to \~\$13,900 in 2027 under this scenario.

(3) Announcement of No Copper Tariff: A definitive decision against the tariff would reduce the size of our ex-US deficit forecast in 2026, and push the ex-US market back into surplus in 2027, weighing on prices vs. our base case in both years. Under this scenario, we would expect US refined copper imports to decrease to a very small volume in H2 2026 and 2027, but not completely stop, nor would US stockpiles likely leave the US. This is because even if not imposed for now, a tariff would likely remain on the cards for the future, similar to the critical minerals tariff decision which stated “it may be appropriate to impose import restrictions, such as tariffs, if satisfactory agreements are not reached in a timely manner”. In this scenario, we would expect the ex-US market to be in a 410kt deficit in 2026, but move to 130kt surplus in 2027, and the LME price to move lower to \~\$12,800 next year (our 2027 estimated fair value in this scenario).

Exhibit 8: We Raise our LME Copper Price Forecast 

<table><tr><td colspan="3">GS Forecast ($/mt)</td><td></td></tr><tr><td></td><td>LME Copper New</td><td>LME Copper Prior</td><td>LME Copper Futures</td></tr><tr><td>2026</td><td>13,400</td><td>12,650</td><td>13,392</td></tr><tr><td>2027</td><td>13,800</td><td>12,150</td><td>13,629</td></tr><tr><td>2028</td><td>13,700</td><td>12,150</td><td>13,608</td></tr><tr><td>1Q26</td><td>12,878</td><td>12,878</td><td>12,878</td></tr><tr><td>2Q26</td><td>13,400</td><td>12,700</td><td>13,415</td></tr><tr><td>3Q26</td><td>13,600</td><td>12,600</td><td>13,636</td></tr><tr><td>4Q26</td><td>13,700</td><td>12,500</td><td>13,633</td></tr><tr><td>1Q27</td><td>13,800</td><td>12,400</td><td>13,629</td></tr><tr><td>2Q27</td><td>13,800</td><td>12,200</td><td>13,633</td></tr><tr><td>3Q27</td><td>13,800</td><td>12,000</td><td>13,634</td></tr><tr><td>4Q27</td><td>13,800</td><td>12,000</td><td>13,622</td></tr><tr><td>Jan-26</td><td>13,012</td><td>13,012</td><td>13,012</td></tr><tr><td>Feb-26</td><td>13,034</td><td>13,034</td><td>13,034</td></tr><tr><td>Mar-26</td><td>12,609</td><td>12,609</td><td>12,609</td></tr><tr><td>Apr-26</td><td>13,020</td><td>12,600</td><td>13,020</td></tr><tr><td>May-26</td><td>13,600</td><td>12,700</td><td>13,602</td></tr><tr><td>Jun-26</td><td>13,600</td><td>12,800</td><td>13,625</td></tr><tr><td>Jul-26</td><td>13,600</td><td>12,635</td><td>13,633</td></tr><tr><td>Aug-26</td><td>13,600</td><td>12,600</td><td>13,639</td></tr><tr><td>Sep-26</td><td>13,620</td><td>12,565</td><td>13,636</td></tr><tr><td>Oct-26</td><td>13,665</td><td>12,535</td><td>13,634</td></tr><tr><t

[中间内容因长度限制已省略]

me have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
