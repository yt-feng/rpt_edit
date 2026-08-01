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
# A-share Sentiment Edged Down on Lower Volume Turnover; Still Prefer HK

MSASI weakened further as turnover contracted amid the liquidity overhang from CXMT IPO and further global AI trade pullback. We continue to prefer Hong Kong over A-shares tactically, supported by a more independent market cycle, greater resilience versus broader EM and improving fundamentals.

A-share investor sentiment decreased vs. the previous cycle: Weighted MSASI decreased by 5ppt vs. the prior cutoff date (July 22) to 32%. Weighted MSASI 1MMA also decreased by 4ppt over the same period at 53%. Turnover for ChiNext, A-share, equity futures turnover and margin transaction outstanding declined by 24% (to Rmb509bn), 21% (to Rmb2,107bn), 22% (to Rmb574bn) and 3% (to Rmb2,652bn), respectively. The 30-day RSI decreased by 4ppt over the same period (July 22-29). Consensus earnings estimate revision breadth remained negative, although it did improve marginally vs. last week.

Southbound net outflows – US\$2bn over July 23-29: MTD net inflows were US \$9.2bn and YTD net inflows were US\$47.7bn (47% of same period last year).

Note: As announced on July 26, 2024, by HKEX, Shanghai Stock Exchange and Shenzhen Stock Exchange, the publication of Northbound daily purchase and sales data was terminated as of August 19, 2024. Northbound daily buying and selling data were last made available on August 16, 2024.

The listing of CXMT, one of the largest IPOs in A-share history, may tighten liquidity and increase near-term market volatility. Meanwhile, the July Politburo meeting reinforced a "fine-tuning rather than stimulus" message, broadly in line with our China Macro team's expectations. Policymakers acknowledged rising growth challenges but focused on accelerating the rollout of the roughly Rmb2tn of remaining fiscal and quasi-fiscal support, rather than unveiling new stimulus measures. Policy priorities remain tilted toward hard tech ("Al+") and infrastructure ("Six Networks"), with limited incremental support for consumption and housing. Beijing's commitment to roll out additional "practical and effective" measures if needed keeps September-October as the key window for potential policy easing.

<table><tr><td colspan="2">MS ASIA LIMITED+</td></tr><tr><td colspan="2">Laura Wang</td></tr><tr><td colspan="2">Equity Strategist</td></tr><tr><td>Laura.Wang@morganstanley.com</td><td>+852 2848-6853</td></tr><tr><td colspan="2">Chloe Liu</td></tr><tr><td colspan="2">Equity Strategist</td></tr><tr><td>Chloe.Liu1@morganstanley.com</td><td>+852 2848-5497</td></tr><tr><td colspan="2">Vicky Wu</td></tr><tr><td colspan="2">Equity Strategist</td></tr><tr><td>Vicky.Wu@morganstanley.com</td><td>+852 3963-3928</td></tr></table>

![](images/69eef56fc5b59c73765729d9086fbe8405a0fc97db0510192f8e1f3a3e8f7591.jpg)

Exhibit 1: MS A-share Sentiment Indicator: MSASI weighted and MSASI weighted 1MMA  
![](images/4cde1e24fc0c1994c9245e85a73197d66da8aebcf920268c3ff5f2c4afb53cf8.jpg)  
Source: CEIC, Bloomberg, Wind, RIMES, MS. Data as of July 29, 2026.

Exhibit 2 : MSASI trajectory since January 1, 2019  
![](images/cbe3da46eed8b3175ca826f537840995a7381fff355a24496529371f4cbc4167.jpg)  
Source: CEIC, Bloomberg, Wind, RIMES, MS Research. Data as of July 29, 2026.

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Overview (continued)

We continue to favor Hong Kong equities in the near term and expect recent outperformance to persist despite elevated global volatility. Key supporting factors include:

\- A more independent equity cycle. Hong Kong has significantly lower exposure to the crowded global AI trade than A-shares, making it less sensitive to recent swings in global technology sentiment.

\- Greater resilience versus the broader EM complex. Near-term global market volatility could lead to sustained liquidity tightness, which could weigh on other EM markets, while China/Hong Kong equities remain supported by relief from funding short unwinding and very low investor positioning.

• Hong Kong's internal market dynamics are improving.

• 2Q results bottoming out vs. 1Q and 2025;

• Liquidity stabilizing post earlier IPO unlocking supply side shock;

• AI trade broadening out to data center/cloud services benefiting the Chinese hyperscalers that are listed in HK (not in the A-share market).

## Over the longer term, however, we remain highly constructive on A-shares,

particularly in technology and innovation sectors. We expect earnings growth in China's hard-tech industries to continue accelerating, supporting a recovery in market leadership and creating the foundation for new highs over the cycle. (2Q26 Pre-Announcements: A-share Earnings Pressure Eased, While MSCI China Signals Strengthened)

## Read more:

China Market-Wise: Global Marketing Feedback – Rising Interest with Uncertain Timing (1 Jul 2026);

China Market-Wise: China Outperforming in a Volatile Market – What's Next? (9 Jul 2026)

## MSASI Methodology

Related report: China Equity Strategy: Relaunching MSASI: A New Take on A-share Market Sentiment and Technical Signals (27 Oct 2025)

## Step 1: Normalizing sentiment metrics

The new MSASI is based on 12 individual indicators, each designed to capture a different dimension of investor sentiment and market activity.

To make these metrics comparable, each is re-scaled using a 100-day moving min-max normalization. This approach helps reduce noise from high-frequency movements and better reflects whether sentiment is improving or deteriorating over the medium term.

## Normalization Formula:

Normalized Value = (Latest Value-Min (Last 100 Days)) /

(Max (Last 100 Days)–Min (Last 100 Days))

Each normalized series is expressed on a 0-100 scale, where higher values indicate stronger or more active sentiment conditions.

## The 12 metrics included are:

1. ChiNext Turnover: Daily trading turnover on ChiNext, normalized using the 100-day moving min-max method (available daily; weekly closing values used for analysis).

2. A-share Turnover: Daily turnover of all A-shares, normalized using the 100-day moving min-max method (available daily; weekly closing values used for analysis).

3. Equity Index Futures Turnover: Daily turnover of equity index futures, normalized using the 100-day moving min-max method (available daily; weekly closing values used for analysis).

4. Northbound Turnover: Daily Stock Connect northbound trading turnover, normalized using the 100-day moving min-max method (available daily; weekly closing values used for analysis).

5. Margin Financing Outstanding: Total margin transaction balances, normalized using the 100-day moving min-max method (available daily; weekly closing values used for analysis).

6. New Accounts Registered with the Shanghai Stock Exchange: Monthly number of new retail accounts registered with the Shanghai Exchange, normalized using the 100-day moving min-max method (available monthly).

7. 30-Day RSI (CSI 300): Relative Strength Index over a 30-day period for CSI 300 (available daily; weekly closing values used).

8. Number of Limit-Up A-shares: Daily count of stocks hitting the 10% upper price limit, normalized using the 100-day moving min-max method (available daily; weekly closing values used for analysis).

9. CSI 300 Futures Backwardation: The percentage difference between CSI 300 futures and spot prices, calculated as (Futures Price – Spot Price)/Spot Price, normalized using the 100-day moving min-max method (available daily; weekly closing values used for analysis).

10. CSI 300 Call-Put Ratio: Ratio of open interest in call options to put options, normalized using the 100-day moving min-max method (available daily; weekly closing values used for analysis).

11. Foreign Passive Fund Flows to CSI 300 (1MMA): One-month moving average of daily flows from foreign-domiciled passive funds to CSI 300, normalized using the 100-day moving min-max method (available daily; weekly closing values used for analysis).

12. Earnings Estimate Revision Breadth (3MMA): Three-month moving average of the net proportion of upward earnings estimate revisions vs. downward earnings estimate revisions, based on the Shanghai A Index, normalized using the 100-day moving min-max method (available weekly).

This normalization process ensures that each indicator contributes proportionally, regardless of scale or data frequency, while highlighting directional shifts in sentiment over time.

## Step 2: Constructing the Weighted Sentiment Indicator

Once normalized, each of the 12 series is assigned a weight based on its historical explanatory power relative to the CSI 300 Index.

Weights are determined by the R-squared values from a single-factor regression between the metric (relative to its 100-day moving min max) and the CSI 300 (relative to 100MA) performance.

This weighting method gives greater emphasis to indicators that have historically demonstrated stronger correlations with market movements, ensuring that the overall index reflects sentiment components most relevant to A-share performance.

## Step 3: Constructing the MSASI (Weighted)

Using the weighted sentiment indicator derived in Step 2, we construct the MSASI (Weighted) as the composite measure of overall market sentiment.

This index is then re-scaled to a 0-100 range, based on its distance from historical high and low values since January 2024.

This scaling allows the indicator to reflect relative sentiment strength over time – where higher readings indicate stronger investor enthusiasm, and lower readings reflect weaker sentiment or risk aversion.

## Step 4: Constructing the MSASI (Weighted 1MMA)

To highlight underlying trends and reduce short-term volatility, we apply a one-month moving average to the MSASI (Weighted). The resulting MSASI (Weighted 1MMA) smooths out high-frequency fluctuations, providing a clearer picture of medium-term sentiment dynamics and improving interpretability for tactical or strategic analysis.

Exhibit 3: Weighting of 12 indicators of MSASI, and R-squared of indicators vs. CSI 300 (relative to 100MA)

<table><tr><td>Indicator</td><td>R-sq vs. CSI 300 (relative to 100MA)</td><td>Weighting</td></tr><tr><td>ChiNext Turnover</td><td>12.6%</td><td>10%</td></tr><tr><td>A-share Turnover</td><td>19.7%</td><td>15%</td></tr><tr><td>Equity Futures Turnover</td><td>8.1%</td><td>6%</td></tr><tr><td>Northbound Turnover</td><td>7.6%</td><td>8%</td></tr><tr><td>Margin Transaction Outstanding</td><td>34.3%</td><td>15%</td></tr><tr><td>SHSE New accounts Registered</td><td>14.3%</td><td>3%</td></tr><tr><td>Earnings Revision Breadth (3MMA)</td><td>6.6%</td><td>8%</td></tr><tr><td>RSI-30D</td><td>49.0%</td><td>15%</td></tr><tr><td>No. of Limit Up A-share</td><td>4.6%</td><td>6%</td></tr><tr><td>CSI300 backwardation</td><td>3.9%</td><td>4%</td></tr><tr><td>CSI300 call put ratio</td><td>14.0%</td><td>6%</td></tr><tr><td>Foreign domiciled passive funds flows to CSI300 (1MMA)</td><td>0.5%</td><td>4%</td></tr></table>

Note: For SHSE new account registrations, although the R-squared with the CSI 300 is high, the data is available only on a monthly basis rather than daily or weekly, so we assign it a relatively lower weight. Similarly, for the CSI 300 call-put ratio, despite its high R-squared with the CSI 300, the data is only available from late 2019 onward, so we also assign it a relatively lower weight.
Source: CEIC, Wind, Rimes, EPFR, Bloomberg, MS.

## Other items to keep in mind

\- The charts below show the scaled version of all these metrics as they are used in our MSASI compilation analysis.

\- We use data from January 2014 to the present because some of the market-influencing factors were not fully developed before that, i.e., Stock Connect Northbound (program only launched in November 2014).

\- Some metrics have gone through regime shifts owing to regulatory changes, i.e., index futures trading, which became heavily regulated as part of market stabilization measures during the 2015 correction. We try to accommodate/ normalize, such shifts by looking at relative level to moving 100 days min-max level rather than absolute volume/value.

Exhibit 4: ChiNext turnover adjusted by moving 100D min-max (scaled to 0-100% based on the percentage away from its 100-day high and low levels) vs. CSI 300 relative to 100D MA  
![](images/ebc23c1b229984828192baa02cbb1f4870a4e0f7fd1b5a7c159e1624ffa5dea5.jpg)  
Source: CEIC, MS. Data as of July 29, 2026.

Exhibit 5: A-share turnover adjusted by moving 100D min-max (scaled to 0-100% based on the percentage away from its 100-day high and low levels) vs. CSI 300 relative to 100D MA  
![](images/572443fa9e1ce275d0ab74278283bae2ea1c752fc71e87640f091f668005d53d.jpg)  
Source: CEIC, Bloomberg, MS. Data as of July 29, 2026.

Exhibit 6: Equity futures turnover adjusted by moving 100D min-max (scaled to 0-100% based on the percentage away from its 100-day high and low levels) vs. CSI 300 relative to 100D MA  
![](images/6e914407d9045f80126b8f78e68d38dd25473e7842433f17b5252e579872f4b1.jpg)  
Source: CEIC, MS. Data as of July 29, 2026.

Exhibit 7: Northbound turnover adjusted by moving 100D min-max (scaled to 0-100% based on the percentage away from its 100-day high and low levels) vs. CSI 300 relative to 100D MA  
![](images/00df989a973f2d432c2f19673889b8966140ea22240c2757f5afeb9124554bea.jpg)  
Source: CEIC, MS. Data as of July 29, 2026.

Exhibit 8: Margin transactions adjusted by moving 100D min-max (scaled to 0-100% based on the percentage away from its 100-day high and low levels) vs. CSI 300 relative to 100D MA  
![](images/7303c9c2f6af4f1b3474a4709a2e3f1113a85e6e47350c5bca81539b156821b2.jpg)  
Source: CEIC, MS. Data as of July 29, 2026.

Exhibit 9: SSE new accounts adjusted by moving 100D min-max (scaled to 0-100% based on the percentage away from its 100-day high and low levels) vs. CSI 300 relative to 100D MA  
![](images/c1bc84193b4b2c10f9f7439ff6525d2131083805f2df252589e0c93e853f2465.jpg)  
Source: CEIC, Bloomberg, MS. Data as of July 29, 2026.

Exhibit 10: RSI-30D since January 2014 vs. CSI 300 relative to 100D MA  
![](images/6cfa4aa3a091cd719f966a0d50a88e7c87eaea215ab12192f509e44e6771fd61.jpg)  
Source: CEIC, Bloomberg, MS. Data as of July 29, 2026.

Exhibit 11: Number of limit-up A-shares adjusted by moving 100D min-max (scaled to 0-100% based on the percentage away from its 100-day high and low levels) vs. CSI 300 relative to 100D MA  
![](images/84f53837997ad19e954f22bbb20210c6fb6a08d84bf8c1dfbf0a549022cde732.jpg)  
Source: CEIC, Wind, Bloomberg, MS. Data as of July 29, 2026.

Exhibit 12: CSI 300 future backwardation adjusted by moving 100D min-max (scaled to 0-100% based on the percentage away from its 100-day high and low levels) vs. CSI 300 relative to 100D MA  
![](images/29c61a01bcbe73d10f378963f83b136fd01fe9550578526452d1f49e58c74b73.jpg)  
Source: CEIC, Wind, MS. Data as of July 29, 2026.

Exhibit 13: CSI 300 put-call ratio adjusted by moving 100D min-max (scaled to 0-100% based on the percentage away from its 100-day high and low levels) vs. CSI 300 relative to 100D MA  
![](images/745346acac203a56c2cb6c6f6f2b5fea2569afa1fdc64117aad00c300b483605.jpg)  
Source: CEIC, Wind, MS. Data as of July 29, 2026.

Exh

[中间内容因长度限制已省略]

herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., authorised and regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the US by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital

Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## © 2026 MS
"""
