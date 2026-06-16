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
## Americas Energy & Transition

# Bernstein Energy: Applying the 5 "W"s to an upstream capex supercycle...we are unconvinced

![](images/d68d235fa34efdc1eec0279d9c4f36c82f78853ac05aa12998c436ba6a99135f.jpg)

Bob Brackett, Ph.D.

+1 917 344 8422

bob.brackett@bernsteinsg.com

![](images/a273173373dfd2df5ae41ab983ed45cef62ab5d1076356c54e001843eef20b6c.jpg)

Minnie Xu

+1 917 344 8574

minnie.xu@bernsteinsg.com

![](images/5126fddcf168e2a7d20178185f13f639b4ac1eaad3409d7c166e6454eca4f405.jpg)

Anshika Bajpai

+1 917 344 8306

anshika.bajpai@bernsteinsg.com

Today, we use our outlook for global upstream oil & gas capital expenditures (Bernstein Energy: Global Upstream Capex 2026...the quantity of capex falls now...does the quality of capex follow?) to consider the current environment. We still see a pullback of \~\$40 bln upstream capex in 2026 driven by lagging company conservatism in uncertain oil and geopolitical environment. Public E&Ps remain disciplined, OFS companies are not materially resetting FY26 guidance higher, shale productivity gains are harder to achieve, and a large share of discovered resources remains undeveloped because the barrels are long-cycle, politically difficult, or no longer cheap to develop.

In a post Strait of Hormuz world, we would expect perhaps \~\$560 bln in total upstream capex Exhibit 1, \~\$50 bln more from our previous forecast in Jan 2026, when Brent averaged \~\$70/bbl. Today, Brent is \~\$90/bbl, but we'd expect planning prices have risen to at most \$70/bbl.

In this note, we use the five-W framework to assess the likelihood of an upstream capex supercycle.

1. WHY invest? Cash flow is up, but reinvestment appetite is not. Higher Brent has improved E&P cash flow, but investors continue to reward capital discipline, buybacks and free cash flow durability over production growth (Exhibit 3 - Exhibit 7.  
2. WHAT barrels get developed? Roughly 1/3 of the discovered resources over the past century remains undeveloped (Exhibit 8) with deepwater + barrels leading discoveries. The problem is that those deepwater barrels are increasingly harder to convert into supply (Exhibit 9 and Exhibit 10). Shale barrels are content to plateau (Exhibit 12) while oil sands barrels (Exhibit 13) need more clarity.  
3. WHO will invest? NOCs, not public E&Ps, lead the next cycle. The marginal growth barrel is increasingly controlled by NOCs and state-directed players, not U.S. shale independents (Exhibit 14 - Exhibit 16).  
4. WHERE can capital go? The best geology is often in the worst jurisdictions. Many of the largest undeveloped barrels sit in countries with high fiscal take, political instability, sanctions or weak rule of law (Exhibit 17 - Exhibit 18)  
5. WHEN to invest? Usually, high oil prices trigger a sharp pickup in rig activity, but that pattern has broken down this time, and we have not yet seen any raise of guidance from oil services and equipment companies (Exhibit 19 - Exhibit 20). Upstream inflation also means companies are spending more simply to hold activity flat.

Finally, we highlight that oil price has outperformed E&P equities year to date (Exhibit 21). The thesis of higher for longer prices driving better than historic volume growth is not one that we find resonating.

Instead we'd suggest that as we exit the current crisis and the Strait reopens, the dominant theme will be a comfortable oil price with a powerful floor (refilling strategic reserves at \$70+?) where excess free cash flow is rapidly collected by E&Ps and returned to shareholders.

BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="3">12 Jun 2026</td><td colspan="2">TTMRel.</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Target Perf.</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td><td></td></tr><tr><td>APA (APA)</td><td>M</td><td>USD</td><td>37.02</td><td>40.00</td><td>62.6%</td><td>USD</td><td>2.83</td><td>7.20</td><td>6.42</td><td>13.1</td><td>5.1</td><td>5.8</td><td></td></tr><tr><td>COP (ConocoPhillips)</td><td>O</td><td>USD</td><td>116.98</td><td>121.00</td><td>0.6%</td><td>USD</td><td>6.18</td><td>13.89</td><td>10.88</td><td>18.9</td><td>8.4</td><td>10.8</td><td></td></tr><tr><td>CVX (Chevron)</td><td>M</td><td>USD</td><td>187.22</td><td>204.00</td><td>6.2%</td><td>USD</td><td>8.43</td><td>16.58</td><td>13.26</td><td>22.2</td><td>11.3</td><td>14.1</td><td></td></tr><tr><td>DVN (Devon Energy)</td><td>O</td><td>USD</td><td>45.31</td><td>59.00</td><td>9.1%</td><td>USD</td><td>4.17</td><td>10.06</td><td>8.43</td><td>10.9</td><td>4.5</td><td>5.4</td><td></td></tr><tr><td>FANG (Diamondback)</td><td>O</td><td>USD</td><td>192.13</td><td>241.00</td><td>5.7%</td><td>USD</td><td>4.57</td><td>32.21</td><td>27.22</td><td>42.0</td><td>6.0</td><td>7.1</td><td></td></tr><tr><td>EQT (EQT)</td><td>O</td><td>USD</td><td>51.94</td><td>69.00</td><td>(29.4)%</td><td>USD</td><td>3.31</td><td>8.15</td><td>8.58</td><td>8.0</td><td>5.0</td><td>4.8</td><td></td></tr><tr><td>EOG (EOG)</td><td>M</td><td>USD</td><td>136.65</td><td>155.00</td><td>(9.6)%</td><td>USD</td><td>9.88</td><td>18.93</td><td>16.25</td><td>13.8</td><td>7.2</td><td>8.4</td><td></td></tr><tr><td>KOS (Kosmos Energy)</td><td>M</td><td>USD</td><td>2.87</td><td>2.40</td><td>14.4%</td><td>USD</td><td>(1.58)</td><td>1.13</td><td>0.75</td><td>(1.8)</td><td>2.5</td><td>3.8</td><td></td></tr><tr><td>KOS.LN (Kosmos Energy)</td><td>M</td><td>GBp</td><td>217.00</td><td>177.00</td><td>28.9%</td><td>GBP</td><td>(1.17)</td><td>0.83</td><td>0.56</td><td>(1.9)</td><td>2.6</td><td>3.9</td><td></td></tr><tr><td>XOM (ExxonMobil)</td><td>O</td><td>USD</td><td>147.01</td><td>182.00</td><td>11.0%</td><td>USD</td><td>7.37</td><td>16.37</td><td>14.49</td><td>19.9</td><td>9.0</td><td>10.1</td><td></td></tr><tr><td>SPX</td><td></td><td></td><td>7,431.46</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EDME</td><td></td><td></td><td>1,570.59</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended  
EQT estimate is Reported EPS; EQT valuation is EV/EBITDA (x);  
Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

Capex discipline and a normalizing price might be an attractive entry point for oily E&Ps. We have outperform ratings on FANG, COP and DVN.

## DETAILS

## SYNTHESIZING THE 5 "W"S ... WE EXPECT ONLY TWEAKS TO UPSTREAM CAPEX

It is reasonable to assume somewhat higher upstream capex than in our previous forecast, as stronger Brent prices have encouraged some less disciplined operators to step up investment, driving a gradual increase into 2027. Once Brent prices normalize to \$75/bbl in 2028 under our price deck, we expect upstream spending to trend lower again to our long run views.

Our capex model takes oil price assumptions as a strong driver, but despite the price on the screen (and risks of higher prices), we do not use, say, current \~\$90 Brent for our capex model as we don't believe planning prices have fundamentally changed in a post Strait of Hormuz world, especially given (1) the uncertainty, and (2) the strong desire for the market to want lower prices. We have always perhaps believed that inflation was closer to a popular delusion than a law of physics. Our favorite author, Philip K. Dick, argued “Reality is that which, when you stop believing in it, doesn't go away.” Apparently oil economics can defy reality for now.

In any case, we provide our (unimpressive) capex forecast below reflecting our view of the current situation.

Then we apply a 5 "W" framework to support our view.

EXHIBIT 1: We forecast \~\$560 bln in upstream capital expenditures in 2026 including \~\$56 bln toward exploration  
![](images/041d04220ae50c019f7adee69a81aa7b053dcb9224acde56921af247d903d9d8.jpg)

<details>
<summary>stacked area chart</summary>

| Year | Exploration | Int'l E&Ps | National Oil | Integrated Energy | US E&Ps |
|------|-------------|------------|--------------|-------------------|---------|
| 2026e | $70 brent | $78 | $78 | $78 | $78 |
| 2027e | $70 | $78 | $78 | $78 | $78 |
</details>

Source: Company reports, Rystad Energy, IEA, EIA, Bloomberg, Bernstein estimates and analysis

## WHY...

...INVEST IN UPSTREAM CAPEX?

## because reserve replacement ultimately matters

Reserve lives (ex long cycle projects such as LNG) are unimpressive amongst E&Ps and integrateds. Furthermore, shale ‘resources’ have created a comfort cushion that was lacking say 15 years ago (a strong internal conviction that resources can be migrated to reserves and then out the wellhead). While significant resources and reserves no doubt exist, we note that discoveries have collapsed in a world of shale and that the best days of deepwater and ultradeepwater are perhaps behind us.

EXHIBIT 2: The world has discovered abundant resources, largely in shale and shelf  
![](images/d12209b156e65764b6dc3e5930f4a5049e71b5d1580198afc42a1109d1d4c2ac.jpg)

<details>
<summary>area chart</summary>

| Year | Ultra deepwater (1500+ meter) | Deep water (125-1500 meter) | Shelf (to 125 meter) | Land |
|------|-------------------------------|-----------------------------|----------------------|------|
| 1972 | ~30,000                       | ~10,000                     | ~250,000             | ~240,000 |
| 1988 | ~10,000                       | ~5,000                      | ~15,000              | ~15,000 |
| 2000-2010+ US Shale | ~15,000                   | ~5,000                      | ~15,000              | ~15,000 |
</details>

Source: Rystad, Bernstein and analysis

## because E&Ps have enjoyed higher cash flows for the last several years (partly due to consolidation)

While Middle East disruption is still a Q2 headwind to some company's production, the Iran conflict will ultimately case more overall cash flow due to higher Brent price. In any case, large cap E&P cash flows have been relatively impressive since Covid-19 days (in strong part due to industry consolidation).

EXHIBIT 3: US majors operating cash flow is rising thanks to supply discipline  
![](images/c400f0f87dd284a725c043ee2afcf184eea4ac1703560b05108039ae90bf323d.jpg)

<details>
<summary>area chart</summary>

| Year | XOM   | CVX   | COP   | FANG  | EOG   | DVN   | APA   | BP    | TTE   | OXY   | OVV   |
|------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| 2009 | 30000 | 15000 | 10000 | 5000  | 3000  | 2000  | 1500  | 1000  | 5000  | 3000  | 2000  |
| 2010 | 25000 | 12000 | 8000  | 4000  | 2500  | 1500  | 1200  | 800   | 4000  | 2500  | 1500  |
| 2011 | 28000 | 13000 | 9000  | 4500  | 2800  | 1700  | 1300  | 900   | 4500  | 2800  | 1700  |
| 2012 | 32000 | 14000 | 10000 | 5000  | 3200  | 1800  | 1400  | 1000  | 5000  | 3200  | 1800  |
| 2013 | 35000 | 15000 | 11000 | 5500  | 3500  | 1900  | 1500  | 1100  | 5500  | 3500  | 1900  |
| 2014 | 38000 | 16000 | 12000 | 6000  | 3800  | 2100  | 1600  | 1200  | 6000  | 3800  | 2100  |
| 2015 | 42000 | 17000 | 13000 | 6500  | 4200  | 2300  | 1700  | 1300  | 6500  | 4200  | 2300  |
| 2016 | 45000 | 18000 | 14000 | 7000  | 4500  | 2400  | 1800  | 1400  | 7000  | 4500  | 2400  |
| 2017 | 48000 | 19000 | 15000 | 7500  | 4800  | 2500  | 1900  | 1500  | 7500  | 4800  | 2500  |
| 2018 | 52000 | 21000 | 16543| -     | -     | -     | -     | -     | -     | -     | -     |
| 2019 | -     | -     | -     | -     | -     | -     | -     | -     | -     | -     | -     |
| 2020 | -     | -     | -     | -     | -     | -     | -     | -     | -     | -     | -     |
| 2021 | -     | -     | -     | -     | -     | -     | -     | -     | -     | -     | -     |
| 2022 | -     | -     | -     | -     | -     | -     | -     | -     | -     | -     | -     |
| 2023E| -     | -     | -     | -     | -     | -     | -     | -     | -     | -     | -     |
| OXY                  | -     | -     | -     | -     | -     | -     | -     | -     | -     | -     | -     |
| OVV                  | -     | -     | -     | -     | -     | -     | -     | -     | -     | -     | -     |
| Total                | ~68,367| ~46,367| ~36,367| ~26,367| ~16,367| ~9,367| ~6,367| ~4,367| ~26,367| ~16,367| ~9,367|
</details>

Source: Rystad, Bloomberg, company reports, Bernstein and analysis

Despite the higher cash flow, capex spending has simply returned to near pre-Covid levels.

EXHIBIT 4: And they will try not to break this discipline  
![](images/365c313b1546f5382d6f2edfc1446efdaad7e2b773c9a28916073a29fc9b0a13.jpg)

<details>
<summary>stacked area chart</summary>

| Year | XOM  | CVX  | COP  | FANG | EOG  | DVN  | APA  | BP   | TTE  | OXY  | OVV  |
|------|------|------|------|------|------|------|------|------|------|------|------|
| 2009 | 7000 | 5000 | 3000 | 4000 | 2000 | 1000 | 800  | 600  | 500  | 400  | 300  |
| 2010 | 7500 | 5500 | 3500 | 4500 | 2500 | 1200 | 900  | 650  | 550  | 450  | 350  |
| 2011 | 8000 | 6000 | 4000 | 5000 | 3000 | 1500 | 1100 | 700  | 600  | 500  | 400  |
| 2012 | 9000 | 7000 | 5000 | 6000 | 3500 | 1800 | 1300 | 750  | 650  | 550  | 450  |
| 2013 | 8500 | 6500 | 4500 | 5500 | 3200 | 1600 | 1200 | 720  | 620  | 520  | 420  |
| 2014 | 8800 | 6800 | 4800 | 6200 | 3300 | 1700 | 1350 | 780  | 680  | 580  | 480  |
| 2015 | 7500 | 5500 | 4200 | 5800 | 3100 | 1450 | 1250 | 730  | 630  | 530  | 430  |
| 2016 | 6500 | 4800 | 3800 | 5200 | 2900 | 1350 | 1150 | 680  | 580  | 480  | 380  |
| 2017 | 7800 | 5200 | 4100 | 5600 | 3250 | 1550 | 1350 | 735  | 635  | 535  | 435  |
| 2018 | 8200 | 5600 | 4400 | 6100 | 3450 | 1750 | 1550 | 785  | 675  | 575  | 475  |
| 2019 | 7900 | 5450 | 4350 | 5950 | 3450 | 1750 | 1550 | 785  | 675  | 575  | 475  |
| 2020 | 6800 | 4950 | 3950 | 5450 | 3150 | 1450 | 1350 | 695  | 615  | 495  | 415  |
| 2021 | 7250 | 5150 | 4150 | 5750 | 3350 | 1650 | 1450 | 735  | 645  | 535  | 445  |
| 2022 | 8125| -    | -     | -     | -     | -     | -    | -    | -    | -    | -    |
| 2023 | -     | -    | -     | -     | -     | -     | -    | -    | -    | -    | -    |
| 2024 | -     | -    | -     | -     | -     | -     | -    | -    | -    | -    | -    |
| 2025 | -     | -    | -     | -     | -     | -     | -    | -    | -    | -    | -    |
| Peak (approx.)<lcel><lcel><lcel><lcel><lcel><lcel><lcel><lcel><lcel><lcel><lcel><lcel><lcel><nl>
</details>

Source: Rystad, Bloomberg, company reports, Bernstein and analysis

## because shareholders want it?

If we track share price changes since the conflict, it shows the market ‘rewarded’ those returning less CFO to shareholders. We don’t truly believe the causality is correct.

Ultimately we believe that more levered names benefit the most from rising cash flow (allowing for deleveraging, etc.).

We don't believe this is anywhere near a signal to companies to spend.

EXHIBIT 5: Weak correlation, but companies that were less shareholder-friendly based on 1Q26 reporting have actually seen larger share-price gains since the war began.  
![](images/64cf06dee8d71462c1bcbe8a03ecfeb64302d1db0ab5a27d29f4503461cb20c2.jpg)

<details>
<summary>scatterplot</summary>

| Company | Shareholder return as % of CFO in 1Q26 | Share price change after Mar.1, 2026 |
|---------|----------------------------------------|--------------------------------------|
| APA     | ~18%                                   | ~24%                                 |
| OVV     | ~17%                                   | ~14%                                 |
| PR      | ~18%                                   | ~11%                                 |
| DVN  

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
