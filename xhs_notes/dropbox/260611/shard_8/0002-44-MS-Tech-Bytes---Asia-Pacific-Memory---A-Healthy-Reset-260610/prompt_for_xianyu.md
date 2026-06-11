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
## Tech Bytes | Asia Pacific

# Memory – A Healthy Reset

Corrections are necessary for the cycle to continue. DRAM is the main bottleneck to the AI build-out but the market concerns on the durability of this cycle. We think multiple expansion can be a bigger driver of returns from here. We revise up bear cases substantially for Samsung and SK hynix.

This reset on price performance does not mean the cycle is over. Our core view is that the cycle is still accelerating, earnings revisions remain robust and more sustainable than most believe. The earnings revisions justify the rally – the earnings estimates for memory companies are up just as much as the stocks are – and the LTAs justify a re-rating potential.

Memory cycles – a long-term perspective. We should be near peak cycle by year-end if we go by the historical DRAM cycle duration and a re-rating needs: (1) the supply side to behave, and (2) demand must convert into durable economics in the long-run as well. Prior cycles were never about demand but supply discipline which never held. AI structural demand on top of undisciplined supply is just a longer cycle with a much higher peak, which is a consensus view at the moment.

Memory prices will decline, the cycle always turns as current investment plans come online from late 2027, but price elasticity of AI demand may be different. Lower DRAM prices reduce the cost of running AI inference, making AI deployment cheaper, and create new demand, rather than simply reducing costs for a fixed number of consumer devices.

How much upside? Memory pricing has nearly doubled since February and lead times have stretched out significantly. The underlying driver is constrained physical production due to LTAs. If LTAs could account for 70%+ of total supply in the next 3-5 years, in our view, this implies DRAM stocks could re-rate to at least 8-10x PE vs. 5x PE now, in theory. This is based on simple math of 70%+ of 2027 EPS valued closer to market multiples (rolling 5Y 10-14x PE) and the remaining 30% of non-LTA EPS at historical 5x peak PE of peak earning.

Stock implications. We estimate more than 20-30% DRAM price hikes in 3Q26, enough to keep the YoY rate of change accelerating. Pricing power is translating into earnings revisions that in turn support P/E stability – at 5.2x 2027e earnings – even as stocks surged 70-134% in the last 2-months, and not a change in the discount rate. We revise up our bear case values for SK hynix and Samsung by 175% and 58%, respectively (Revising up the bear case).

MS & CO. INTERNATIONAL PLC+

## Shawn Kim

Equity Analyst

Shawn.Kim@morganstanley.com +44 20 7677-1018

MS ASIA LIMITED+

## Duan Liu

Equity Analyst

Duan.Liu@morganstanley.com +852 2239-7357

MS & CO. INTERNATIONAL PLC+

## Cindy Huang

Equity Analyst

Cindy.Huang@morganstanley.com +44 20 7425-2915

MS & CO. INTERNATIONAL PLC, SEOUL BRANCH+

## Ryan Kim

Equity Analyst

Ryan.G.Kim@morganstanley.com +82 2 399-4939

## Asia Summer School 2026

![](images/5a4cab5a294fc0878cc1bca440fd0dff055a10c1df166e314e78e4a76f5d5c6a.jpg)

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## A Healthy Reset

Markets rarely move in a straight line at the pace seen since the March lows. In our view, a correction was inevitable and ultimately healthy if this memory bull market is going to extend into year-end. Parabolic charts in memory stocks clashed with levered ETF exposure and record crowding by hedge funds and retail investors. This reset on price does not mean the cycle is over. Instead, it is more likely that this is a necessary reset for the cycle to eventually extend – we have had 3 such resets since Generative AI was launched in the fall of 2022. Our constructive year-end view is grounded in: (1) still-strong AI demand, (2) supply growth that is limited by clean room and EUV availability, and (3) LTAs driving durable earnings and FCF growth. We are not at peak cycle yet but acknowledge that accelerative moves in fundamentals always reach an apex in terms of the rate of change and stocks tend to react to that.

Exhibit 1: DRAM Stocks vs. 200-Day Moving Average  
![](images/af3641be2cbbebdc8c015a14314fa07596bb96613f9255ddbca0d5ae0824e652.jpg)

<details>
<summary>line chart</summary>

| Date     | DRAM stocks vs. 200D moving avg |
| -------- | -------------------------------- |
| Jan-95   | 1.5                              |
| May-98   | 1.8                              |
| Nov-25   | 2.6                              |
</details>

Source: Factset, MS

Exhibit 2: DRAM Stocks: Major sell-offs through the rally  
![](images/18772549c56a656c974c7cb16c584bf8b54f4fd8898813042d93c25cf23f4976.jpg)

<details>
<summary>line chart</summary>

| Date       | DRAM stocks share price |
| ---------- | ----------------------- |
| Apr-25     | -22%                    |
| Mar-26     | -24%                    |
| Apr-26     | -10%                    |
| Jun-26     | -15%                    |
</details>

Source: Factset, MS

## Prior memory corrections after parabolic moves may be instructive. These

developments don't necessarily mark the end of a bull market in the memory cycle, but these areas typically don't spring back right away either. That process takes time and this reminds us of similar price moves we have seen in other commodity areas earlier this year (Gold/Silver, Rare Earths, other Industrial Metals, Energy, etc). We would point out that commodities often exhibit this type of volatility while still in the midst of a long bull market.

We note that for the Korea market, historically, post-circuit breaker dynamics skew constructive, with \~75% next-day hit rates improving to \~87-88% over medium horizons, suggesting that while volatility may persist near term, risk-reward is gradually improving into weakness, particularly with Samsung and SK Hynix now trading at \~5.2x and \~4.7x fwd P/E, respectively.

Exhibit 3: Samsung: Returns following KOSPI Circuit Breaker Events

<table><tr><td>Event</td><td>1st trading day</td><td>1D</td><td>1W</td><td>1M</td><td>3M</td></tr><tr><td>Dotcom Bubble</td><td>17/04/2000</td><td>9.4%</td><td>9.6%</td><td>12.0%</td><td>36.8%</td></tr><tr><td>Dotcom Bubble</td><td>18/09/2000</td><td>4.8%</td><td>-4.3%</td><td>-1.8%</td><td>-12.1%</td></tr><tr><td>Dotcom Bubble</td><td>12/09/2001</td><td>6.2%</td><td>1.5%</td><td>-13.3%</td><td>60.1%</td></tr><tr><td>Covid-19</td><td>13/03/2020</td><td>0.0%</td><td>-8.7%</td><td>-6.3%</td><td>8.7%</td></tr><tr><td>Covid-19</td><td>19/03/2020</td><td>5.7%</td><td>9.3%</td><td>13.2%</td><td>21.5%</td></tr><tr><td>Yen Carry Unwind Scare</td><td>06/08/2024</td><td>3.0%</td><td>3.0%</td><td>5.0%</td><td>-19.0%</td></tr><tr><td>US-Iran Conflict</td><td>04/03/2026</td><td>11.3%</td><td>0.8%</td><td>10.2%</td><td>109.3%</td></tr><tr><td>US-Iran Conflict</td><td>09/03/2026</td><td>8.3%</td><td>5.8%</td><td>3.6%</td><td>89.6%</td></tr><tr><td></td><td>Hit Ratio %</td><td>87.5%</td><td>75.0%</td><td>62.5%</td><td>75.0%</td></tr><tr><td></td><td>Mean Return %</td><td>6.1%</td><td>2.1%</td><td>2.8%</td><td>36.9%</td></tr><tr><td></td><td>Max Return %</td><td>11.3%</td><td>9.6%</td><td>13.2%</td><td>109.3%</td></tr><tr><td></td><td>Min Return %</td><td>0.0%</td><td>-8.7%</td><td>-13.3%</td><td>-19.0%</td></tr><tr><td></td><td>Median Return %</td><td>5.9%</td><td>2.3%</td><td>4.3%</td><td>29.2%</td></tr></table>

Source: Factset, MS

## Memory cycles – a long-term perspective

We should be near peak cycle by year-end if we go by the historical DRAM cycle duration – the playbook has been the typical 6 quarters on the way up before supply becomes less tight (i.e. the YoY rate of change in pricing) and stocks moving about 4-months before that. But because of AI agent demand (which dates from January 2026), it is reasonable to assume the top is at least several quarters away from today. The re-rating needs (1) the supply side to behave, and (2) demand must convert into durable economics in the long-run as well.

- Prior cycles were never about demand (every prior cycle had real, growing demand with the exceptions of the 2008 GFC and 2021 initial COVID demand shocks). But the cycles were always supply-driven, racing to meet any demand gap and overshooting.  
- What breaks the cycle is supply discipline, and that is the variable that has never held. Structural demand on top of undisciplined supply is just a longer cycle with a much higher peak, which is consensus thinking at the moment.

Exhibit 4: Long-Term DRAM cycle YoY chart  
![](images/464601a16511a0895011320de723c6d01fc09282720bc5fc82a4b8a51a47083d.jpg)

<details>
<summary>line chart</summary>

| Date   | DRAM Contract YoY (RHS) | NTM PB - DRAM |
|--------|--------------------------|---------------|
| Jan-10 | ~90%                     | ~0.5x         |
| Jun-10 | ~50%                     | ~1.0x         |
| Nov-10 | ~0%                      | ~1.5x         |
| Apr-11 | ~-50%                    | ~1.0x         |
| Sep-11 | ~-50%                    | ~1.5x         |
| Feb-12 | ~-50%                    | ~1.0x         |
| Jul-12 | ~-50%                    | ~1.5x         |
| Dec-12 | ~-50%                    | ~1.0x         |
| May-13 | ~50%                     | ~1.5x         |
| Oct-13 | ~150%                    | ~2.0x         |
| Mar-14 | ~20%                     | ~2.5x         |
| Aug-14 | ~20%                     | ~2.0x         |
| Jan-15 | ~0%                      | ~1.5x         |
| Jun-15 | ~-50%                    | ~1.0x         |
| Nov-15 | ~-50%                    | ~1.5x         |
| Apr-16 | ~-50%                    | ~1.0x         |
| Sep-16 | ~-50%                    | ~1.5x         |
| Feb-17 | ~70%                     | ~2.0x         |
| Jul-17 | ~70%                     | ~2.5x         |
| Dec-17 | ~30%                     | ~2.0x         |
| May-18 | ~20%                     | ~1.5x         |
| Oct-18 | ~-50%                    | ~1.0x         |
| Mar-19 | ~-50%                    | ~1.5x         |
| Aug-19 | ~-50%                    | ~2.0x         |
| Jan-20 | ~-50%                    | ~2.5x         |
| Jun-20 | ~0%                      | ~3.0x         |
| Nov-20 | ~20%                     | ~3.5x         |
| Apr-21 | ~30%                     | ~4.0x         |
| Sep-21 | ~30%                     | ~4.5x         |
| Feb-22 | ~20%                     | ~4.0x         |
| Jul-22 | ~-50%                    | ~3.5x         |
| Dec-22 | ~-50%                    | ~3.0x         |
| May-23 | ~-50%                    | ~2.5x         |
| Oct-23 | ~20%                     | ~2.0x         |
| Mar-24 | ~40%                     | ~2.5x         |
| Aug-24 | ~40%                     | ~3.0x         |
| Jan-25 | ~20%                     | ~2.5x         |
| Jun-25 | ~-50%                    | ~2.0x         |
| Nov-25 | ~30%                     | ~3.0x         |
| Apr-26 | ~80%                     | ~4.0x         |
| Sep-26 | ~80%                     | ~4.5x         |
</details>

Source: Trendforce, Factset, MS

What's different? Intelligence vs. consumer electronics demand. Memory has become an essential input for intelligence or token manufacturing where more HBM bandwidth, more DRAM and NAND capacity mean more intelligence output per second. The larger the model usage, the longer the context and number of users simultaneously supporting more AI agents deployed – this demand is not the same as traditional PC or smartphone where the TAM is fixed.

- AI inference growing exponentially as well as AI agent usage in its infancy and very far from saturation.  
- The ratio of memory that goes into PCs and smartphones and other personal-use devices is lower each day as memory capacity keeps moving to AI-related infrastructure.  
- Every generation of GPU is constrained by memory, not compute. DRAM content per AI unit is growing 4-7x (from 80GB per A100 to 288-768GB for Rubin GPU/Superchip) while AI chips are growing at about 60% annual run rate today.

Memory prices will decline, the cycle always turns... as new fab capacity from current investment plans comes online in late 2027. The nature of demand for memory however, is AI-driven and tied to long-lived infrastructure programs rather than short consumer cycles. This gives memory producers more visibility and confidence on future demand but not enough to aggressively overbuild as in the past cycles. According to management targets, adding capacity may be coming in much more controlled stages.

... but price elasticity of AI demand may be different. Lower DRAM prices reduce the cost of running AI inference, making AI deployment cheaper. This creates new demand and expands the addressable market, rather than simply reducing costs for a fixed number of consumer devices.

## On bubbles

A bubble can inflate for a long time. We had two great years of stock performance back during that internet build out, and we think we can have at least one more great year this year. If we go back to the internet build out, the Generative AI equivalent of internet – Netscape Navigator – was out at the end of 1994, NASDAQ over the next 4-years was up 149%, and in year-5 in 1999 up 86%. Generative AI came out at the end of 2022, and we are 3-years into this, NASDAQ is up 122%. The Dot.com peak in March 2000 can be explained by: (1) fundamentals where the rate of change in internet traffic growth slowed from doubling every 3-months to doubling every year – that slowdown was not what was built into valuations, and (2) post Fed easy money before Y2K (M2 up >10%), oil prices spiked and the Fed started to withdraw that liquidity. NASDAQ then fell 85% and mean reverted back to mid-1996.

It is hard to predict exactly how much of the current demand bubble will persist in the long-run. Agentic AI is a step change in token generation, up from 20% growth 2-months before OpenClaw and over 120% after its launch on January 2026. Clearly, the current market is distorted by short-term dynamics but which part is base demand and which distortion?

Exhibit 5: AI vs. Dot.com: NASDAQ Performance from the Technology's arriva  
![](images/c7bca12134e1448f940db34901b24576945bfb9c5655f474455760b0d6367096.jpg)

<details>
<summary>line chart</summary>

| Date       | Dot.com | AI     |
| ---------- | ------- | ------ |
| Nov-22     | -       | -      |
| Jan-26     | -       | +124% (now) |
</details>

Source: Factset, MS

## Key risks

The risk for the memory cycle at the current stage is plentiful. Technology will evolve, competition and supply will normalize and so will memory stocks. However, the chances of this happening in the very near-term are low, but worth pointing out as it would be significant enough to derail our positive industry view.

- A technical breakthrough on efficiency that would use significantly less memory/HBM, or a change that would bypass memory altogether. We would exclude memory compression as it has been a constant, but acknowledge that the industry always looks for ways around bottlenecks.  
- Falling off the AI race. We still need five major drivers of frontier LLMs and hyperscale AI infrastructure spend to stay elevated.  
- AI demand rate of change moving off-course and no longer exponential. The ARR

[中间内容因长度限制已省略]

e US by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section

21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The following companies do business in countries which are generally subject to comprehensive sanctions programs administered or enforced by the U.S. Department of the Treasury's Office of Foreign Assets Control ("OFAC") and by other countries and multi-national bodies: Samsung Electronics.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

© 2026 MS
"""
