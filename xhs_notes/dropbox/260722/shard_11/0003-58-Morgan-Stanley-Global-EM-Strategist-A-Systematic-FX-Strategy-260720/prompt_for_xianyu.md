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
<table><tr><td colspan="2">Mingyong Liu</td></tr><tr><td colspan="2">Quantitative Analyst</td></tr><tr><td>Mingyong.Liu@morganstanley.com</td><td>+44 20 7677-0963</td></tr></table>

# Global EM Strategist

# A Systematic FX Strategy

Systematic strategies can add value to a discretionary process by stress-testing views and building conviction. We take a break from our typical FX/EM commentary to highlight a systematic strategy from our QIS team.

## Key Takeaways

The MS QIS team recently highlighted the attractive returns from FX systematic investing strategies throughout different market conditions and regimes.

We don't generally use systematic strategies to drive our views, but there is no reason why we cannot use them as an input to stress-test our views.

The QIS team's strategy is modestly long USD. We are neutral with a bearish bias in part due to the house call on the Fed, which is more dovish than market pricing.

## Must reads from Global EM Strategy

## South Africa Economics & Strategy: SARB Preview: A Divided Hike & Steeper Curve | 20-Jul-2026

We expect the MPC to deliver a 25bp policy rate hike this week. Lower oil prices reduce the near-term CPI path but do not yet eliminate the risk that the energy shock will propagate through services and expectations. We favour 1y1y–2y2y steepeners, while remaining neutral on USD/ZAR.

Korea Macro Strategy, Equity Strategy & Economics: Why Is KRW So Weak? | 09-Jul-2026

KRW has been one of the weakest AXJ currencies YTD despite strong fundamentals. We see scope for moderate KRW appreciation as corporate FX conversion may increase, while foreign equity outflows continue, albeit at a slower pace. Korea retail is looking overseas but outflows seem manageable in 2H26.

Morocco Sovereign Credit Strategy: Buy EUR31s Versus EUR35s as Belly Overshoots | 09-Jul-2026

Buy EUR31s vs EUR35s as belly outperformance looks overdone. Morocco is absorbing higher oil prices without a material deterioration in the credit story, external buffers remain strong, and we think the path to IG in 2026 remains intact as long as oil does not spike again.

Quantitative Investment Strategies: Beyond Carry: Building a More Resilient FX Return Engine | 16-Jul-2026

FX systematic investing has delivered attractive returns over recent years, driven by the re-emergence of carry opportunities and technical return

## MS & CO. INTERNATIONAL PLC+

James K Lord
Strategist
James.Lord@morganstanley.com +44 20 7677-3254

Simon Waever
Strategist
Simon.Waever@morganstanley.com +1 212 296-8101

Stephan M Kessler
Quantitative Analyst
Stephan.Kessler@morganstanley.com +44 20 7425-2854

<table><tr><td colspan="2">Ioana Zamfir</td></tr><tr><td>Strategist</td><td></td></tr><tr><td>Ioana.Zamfir@morganstanley.com</td><td>+1 212 761-4012</td></tr></table>

<table><tr><td colspan="2">Emma C Cerda</td></tr><tr><td colspan="2">Strategist</td></tr><tr><td>Emma.Cerda@morganstanley.com</td><td>+1 212 761-2344</td></tr><tr><td colspan="2">Sofia Palacios</td></tr><tr><td colspan="2">Strategist</td></tr><tr><td>Sofia.Palacios@morganstanley.com</td><td>+1 212 761-0428</td></tr></table>

<table><tr><td colspan="2">Neville Z Mandimika</td></tr><tr><td>Strategist</td><td></td></tr><tr><td>Neville.Mandimika@morganstanley.com</td><td>+44 20 7425-2509</td></tr></table>

<table><tr><td colspan="2">Arnav Gupta</td></tr><tr><td>Strategist</td><td></td></tr><tr><td>Arnav.Gupta@morganstanley.com</td><td>+44 20 7677-0382</td></tr></table>

<table><tr><td colspan="2">Gek Teng Khoo</td></tr><tr><td colspan="2">Strategist</td></tr><tr><td>Gek.Teng.Khoo@morganstanley.com</td><td>+852 3963-0303</td></tr></table>

<table><tr><td colspan="2">Nimish M Prabhune</td></tr><tr><td>Strategist</td><td></td></tr><tr><td>Nimish.Prabhune@morganstanley.com</td><td>+91 22 6996-1862</td></tr></table>

![](images/d572c6e99cbaf15856780cdce6b42c66b1d4fd4519f65425c56ee4beaa0c83c0.jpg)

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

patterns. Extending signal breadth using market insights improves performance further.

The 2026 Extel Global Fixed Income Poll is now open and your participation matters a great deal to us. If you have found our Global FX & EM research insightful and helpful, we would greatly appreciate your support. Click here to request your ballot and please rate us five stars in

• Global > Macro Strategy

\- Developed Europe | USA | Japan > Currency and Foreign Exchange

\- Latam | EEMEA | Asia ex Japan > Local Markets
FX Strategy

\- Latam | EEMEA | Asia ex Japan > Local Markets Rates Strategy

Click here for our Bloomberg Ticker Almanac. Please add me to your distribution list.

## Global EM Strategy

MS & CO. INTERNATIONAL PLC

James.Lord@morganstanley.com +44 20 7677-3254

Arnav.Gupta@morganstanley.com +44 20 7677-0382

loana.Zamfir@morganstanley.com +1 212 761-4012

Sofia Palacios
Sofia.Palacios@morganstanley.com +1 212 761-0428

## MS ASIA LIMITED+

Gek.Teng.Khoo@morganstanley.com +852 3963-0303

LIMITED

MS FX and EM Strategy generally do not develop investment ideas following a systematic rule based framework. Our Quantitative Investment Strategy research team does, however, and last week published a new FX Multi-Factor Strategy that has delivered impressive return metrics over many years. See Quantitative Investment Strategies: Beyond Carry: Building a More Resilient FX Return Engine while a brief summary of the publication can be found below. Clients who want to explore following a systematic strategy should consider getting in touch with Stephan Kessler and team. However, just because the Strategy team doesn't run systematic strategies, doesn't mean we can not use them as an input in our process, which discuss now.

Local markets trades overview

\- Rates: CEEMEA: Long 6m EGP T-Bills (FX-Unhedged), SA 1y1y-2y2y steepener, HUF 5Y5Y receiver versus PLN 5Y5Y payer, long NGOMOB 22-Sep-26 (FX-unhedged); Asia: Pay 5y HKD IRS versus USD IRS, pay 5y INR NDOIS, 1s5s THB NDTHOR steepener; LatAm: 2031 vs 2037 PERUGBs flattener, Receive 5y IBR vs SOFR, Buy 2028 MBonos

• FX: CEEMEA: Short EUR/HUF, short 3m USD/TRY forward

## Quantitative Investment Strategies: Beyond Carry: Building a More Resilient FX Return Engine

MS FX and EM Strategy generally do not develop investment ideas following a systematic rule based framework. Our Quantitative Investment Strategy research team does, however, and last week published a new FX Multi-Factor Strategy that has delivered impressive return metrics over many years. See Quantitative Investment Strategies: Beyond Carry: Building a More Resilient FX Return Engine while a brief summary of the publication can be found below.

Clients that want to explore following a systematic strategy should consider getting in

touch with Stephan Kessler and team.

However, just because the Strategy team doesn't run systematic strategies, doesn't mean we can not use them as an input in our process, which discuss now.

## The Systematic Strategy vs MS views

The FX Multi-Factor strategy has a total exposure of -21.0%, which means that it is long the USD versus the traded currencies in the portfolio. Thus, the strategy is positioned for USD strength. Exhibit 1 shows the time series of the strategy's net USD positioning, which makes clear the long USD position is relatively modest vs history.

Currently, the strategy is skewed to be short other currencies versus the USD. In the original note published last week, our QIS colleagues referenced the size of the positions the strategy is long or short vs USD in percentage terms, which referred to the nominal percentage of the overall portfolio risk allocation to a particular currency. The strategy had the largest short in CNH, at -47.2%.

The percentage allocation to each currency is determined in part by the strength of the signal – or conviction level – in the position, but also the volatility of each currency. The weight for CNH appears large because the volatility of CNH is low.

For a discretionary macro PM that may not be looking to implement the full strategy but act selectively depending on the strength of the signal for a particular currency, it is probably more useful to reverse the adjustment for volatility.

In Exhibit 2 we show the z-scores for the weight allocated to each currency relative to the last 12m of data - to account for near-term volatility. When measured in this way, The top five longs are IDR, ZAR, RON, NOK and TWD, and the top five shorts are PEN, COP, CNH, GBP and ILS.

The strategy thus has a long carry bias, and is modestly long USD.

Exhibit 1: Strategy has a modest long USD position  
![](images/2aab027f31e86b0ce103f79dbc4780b440bb9af6fa8279013901b68d836a5884.jpg)  
Source: MS

Exhibit 2: Which are the favourite longs and shorts? \*  
![](images/5ee56ca550d0d0b949d9ef4f0f8fa161d9f83df2241fad4d184246fbdb7fa4e8.jpg)  
Source: MS \*we have taken the weights the Multi-Factor Strategy applies to each currency and converted into a 1y z-score.

Why are we not long USD, if the systematic strategy is? The strategy's net long USD position is sending a different signal to our current view on USD, where we are neutral but have a bearish bias. In recent weeks, the USD has been strong and so the strategy continues to challenge our thinking and encourages us to look for blind spots, in our view.

Indeed, it is notable that the strategy has held long USD position to varying degrees since mid-March, and the USD is generally higher since then.

A key pillar of our current bearish bias on the USD is the expectation for the Fed Funds rate to be lower than what markets and the broader consensus expect. This more dovish path for US monetary policy is not something that the systematic strategy would necessarily reflect and helps to explain where we differ.

The short position against CNH is notable, as the currency has been among the top performers within Asia so far this year and investors are on the look out for catalysts that could reverse the trend.

The continued dependence on the export channel for economic growth likely means that sustained CNY strength and outperformance vs peers poses headwinds for the economy. Recent data show continued increases in the trade surplus, which don't indicate a significant concern for the currency yet, but the systematic Strategy is picking up something that deserves further interrogation.

## How Discretionary Macro PMs Could Use Systematic Strategies

Most of our research in the FX EM Strategy relies on a discretionary approach, with an analysis of business cycles, monetary policy, and risk appetite, mixed in with quantitative tools to help us understand valuation, positioning, and risk premia. In these quantitative tools, considerations around sentiment, technical, and fundamental signals - which we apply in our FX Multi-Factor strategy - play an important role.

Thus, we are strong proponents of quantitative inputs in a fundamental decision-making process. However, we don't necessarily mix these variables together in a fixed or systematic way, but use our judgement to tie the pieces of the puzzle and place different weights on various components of the story as the cycle evolves. Many of our clients at asset managers and hedges funds will follow a similar approach.

There is, however, value in considering signals from systematic strategies as another input within a broader discretionary approach. Cherry-picking when to incorporate a signal from a systematic strategy is not within the spirit of how systematic strategies are intended, of course. However, for a discretionary macro portfolio manager, there is no such promise to stick to a systematic model-driven approach in the first place. Using such signal selectively is normal discretionary practice, similar to incorporating other inputs such as positioning, central bank commentary, or macro data.

When might systematic signals add value to a discretionary process?

\- Guarding against confirmation bias: Any discretionary process is potentially exposed to confirmation bias. Adding a proven systematic overlay could serve as a tool to guard against this. If a particular currency has been performing well for some time in a discretionary portfolio and an investor is inclined to keep the position, but the systematic strategy suddenly starts sending the opposite signal this can act as a prompt to re-examine the thesis and check for blind spots.

\- Timing & sizing trades: Validation and support for a particular position by a systematic strategy could help with conviction and thus provide the signal needed to enter or exit a trade, or to adjust the size of it within the overall portfolio.

\- Filtering a market view: Multi-factor systematic strategies are agnostic to the market regime. However, discretionary portfolio managers will likely take a view on whether markets are trending, in a risk on or off backdrop and thus whether carry trades are likely to be effective. By taking a view, the discretionary macro PM could tune into a particular factor within the multi-factor strategy that he/she expects to be dominant, filtering out those that are not likely to apply. If we are in a range-trading environment, momentum strategies could be filtered out, for example.

As mentioned previously, within the FX Strategy team we use a range of quantitative signals (valuation signals, risk premia, and positioning indicators, for example) as an input to our process already. Over time, we expect to integrate more factor-based strategies such as those found within this publication into our process.

## Quantitative Investment Strategies: Beyond Carry: Building a More Resilient FX Return Engine

The below is a summary of Quantitative Investment Strategies: Beyond Carry: Building a More Resilient FX Return Engine, first published on 16th July 2026.

Systematic FX is back: After a prolonged period of weak performance in the decade following the GFC, FX Carry has returned to the strength it showed in the early 2000s, and the broader systematic FX complex is enjoying a renaissance (Exhibit 3). Our QIS colleagues attribute this revival mainly to wider rate dispersion across the globe, with the JPY's multi-year depreciation adding a further tailwind (though expected to continue, but less strongly). The broader opportunity, however, extends beyond carry. Combining technical, fundamental and sentiment signals creates a more balanced return engine that can participate in different market environments rather than depending on a single risk premium.

A Multi-Factor approach is the core idea: Rather than leaning on any single signal, the MS FX Multi-Factor strategy blends three loosely related signal groups - technical, fundamental, and sentiment -scoring each currency, translating scores into long/short positions, and rebalancing to a constant risk target. Because the factors capture distinct return drivers, weakness in one can be offset by strength in another. The result is a Sharpe ratio of 1.87, a CAGR of 9.3%, and a maximum drawdown of just -6.8%, with returns that compound steadily and no prolonged down periods. (Exhibit 4)

Exhibit 3: Carry opportunities in developed FX markets (DM) over time 

[中间内容因长度限制已省略]

the reference number 149169; in the US by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i)

are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

The following authors are Fixed Income Research Analysts/Strategists and are not opining on or expressing recommendations on equity securities: Nimish M Prabhune; Simon Waever; Ioana Zamfir; Emma C Cerda; Gek Teng Khoo; Neville Z Mandimika; James K Lord.

## © 2026 MS
"""
