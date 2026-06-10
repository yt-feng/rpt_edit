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
## Global EM Strategist

# Finding Your Funder

A divergence in growth trajectories favouring the US, shaky risk appetite amid continued high energy prices is a USD bullish alignment and a headwind for EM. We continue to expect appetite for EM local currency exposure but diversifying funding can help de-risk and isolate the EM view.

## Key Takeaways

We remain constructive on EM currencies, but the rebounding USD has challenged the near-term outlook.  
Even if the USD rebound persists, EM should still perform vs G3. Fundamentals and policy credibility anchor the asset class vs DM.  
We explore the return profiles of long EM exposure with different funding currencies. CAD has been an effective choice by raising returns while lowering vol.  
- Across multiple time frames though, using a basket of funding currencies is generally an improvement across various metrics vs any single DM funding currency.

## Must reads from Global EM Strategy

Global EM Fixed Income Mid-Year Outlook: Ride the Volatility, Keep the Carry | 15-May-2026

Strong EM fundamentals led to resilient performance amidst a roller coaster of oil market and inflation uncertainty. Spreads and FX have performed well. From here a weak USD helps, but limited duration gains and already tight spreads don't, with carry now doing the heavy lifting to year-end.

Poland Economics and Macro Strategy: NBP Preview: Waiting to Act | 28-May-2026

We expect the NBP to remain on hold, with the MPC continuing to signal readiness to tighten if persistent second-round effects start to materialise. We continue to expect one rate hike in September, with risks to our forecast skewed to the upside. In strategy, we prefer to pay 5y5y PLN vs HUF.

LatAm Macro Strategy: Mid-Year Outlook - Top 4 FAQ | 27-May-2026

We provide more color and analysis on the top four questions we have received over the last week, following the publication of our Mid-Year Outlook

Argentina Economics and Sovereign Credit Strategy: IMF Second Review: Our 10 Takeaways | 26-May-2026

The IMF reports have a constructive tone. Argentina appears to be delivering on several key fronts, demonstrating strong commitment to difficult policy

MS & CO. INTERNATIONAL PLC+

## James K Lord

Strategist

James.Lord@morganstanley.com +44 20 7677-3254

MS & CO. LLC

## Simon Waever

Strategist

Simon.Waever@morganstanley.com +1 212 296-8101

## Ioana Zamfir

Strategist

loana.Zamfir@morganstanley.com +1 212 761-4012

## Emma C Cerda

Strategist

Emma.Cerda@morganstanley.com +1 212 761-2344

## Sofia Palacios

Strategist

Sofia.Palacios@morganstanley.com +1 212 761-0428

MS & CO. INTERNATIONAL PLC+

## Neville Z Mandimika

Strategist

Neville.Mandimika@morganstanley.com +44 20 7425-2509

## Arnav Gupta

Strategist

Arnav.Gupta@morganstanley.com +44 20 7677-0382

MS ASIA LIMITED+

## Gek Teng Khoo

Strategist

Gek.Teng.Khoo@morganstanley.com +852 3963-0303

MS INDIA COMPANY PRIVATE LIMITED+

## Nimish M Prabhune

Strategist

Nimish.Prabhune@morganstanley.com +91 22 6996-1862

Please add me to your distribution list.

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

measures and the structural reform agenda. The weakest link remains the country's FX reserve position despite recent meaningful progress.

## Global EM Strategy

MS & CO. INTERNATIONAL PLC

MS & CO. LLC

MS ASIA LIMITED+

MS INDIA PRIVATE COMPANY LIMITED

James Lord

James.Lord@morganstanley.com +44 20 7677-3254

Arnav Gupta

Arnav.Gupta@morganstanley.com +44 20 7677-0382

Ioana Zamfir

Ioana.Zamfir@morganstanley.com +1 212 761-4012

Sofia Palacios

Sofia.Palacios@morganstanley.com 112127010428

Gek Teng Khoo

Gek.Teng.Khoo@morganstanley.com +852 3963-0303

Nimish Prabhune

Nimish.Prabhune@morganstanley.com

Strong US data has caused higher volumes of USD, as investors re-engage with long USD vs G3 while taking off short USD vs EM positions. Global headwinds have picked up with core rates repricing, debate over Fed hikes and growing economic divergence between the US and other major economies putting upward pressure on USD once again

We continue to think the bottom up fundamentals of the EM asset class are for the most part strong. Asia continues to underperform but much of the remainder of the asset class remains supported by improving monetary and fiscal credibility relative to much of DM.

As such, we think investors will want to maintain exposure to the asset class but a more diversified funding approach should be considered. CAD is an interesting option within the single currency universe, but we think a basket approach is consistently attractive across multiple time periods.

## Local markets trades overview

\- Rates: CEEMEA: 1y TRY OIS Payers, HUF 5Y5Y receiver versus PLN 5Y5Y payer, long NGOMOB 22-Sep-26 (FX-unhedged); Asia: Pay 5y HKD IRS versus USD IRS, pay 5y INR NDOIS, 1s5s THB NDTHOR steepener; LatAm: Buy 2028 MBonos, Jan 28 versus Jan 31 DI steepener

\- FX: CEEMEA: Short EUR/HUF, short 3m USD/TRY forward; Asia: Long SGD/INR; LatAm: Short PEN/CLP

## EM Under Top Down Pressure

In the weeks since we published our Mid Year Outlook it's clear that clients broadly share our constructive view on two key aspects of our EM investment thesis:

- Improving fundamentals of the EM local currency asset class.  
- Global investors have limited exposure to EM local currency assets with scope to increase.

However, not everyone agrees with other aspects of our investment thesis - namely, the top down aspects:

- Some agree with our bearish USD view, though some do not  
- There is plenty of debate and push back around our call for the Fed to stay on hold in 26 and cut in 27, and our forecast for lower UST yields is similarly debated.

That push back will only grow in the aftermath of last Friday's US strong employment report (see here).

Indeed, many clients believe the outperformance of the US equity market and the growth outlook will likely keep the USD on the front foot - at least on a DXY basis.

USD strength is of course a significant headwind for the asset class, given the majority of investors benchmark returns, but does not mean the EM asset class does not offer value vs DM. While we have not changed our USD view, investors could consider a more diversified approach to funding EM exposure to de-risk from the USD/Fed cycle - an approach we suggested investors took in our Mid-Year Outlook.

Long EM vs basket: Our forecasts suggest an index-weighted basket of EM currencies, funded by an equally-weighted basket of USD, EUR and JPY, would generate steady total returns over the next 12m, while a purely USD funded approach would see returns flatline from the end of 2026 (Exhibit 1 & Exhibit 2).

EUR-funding has outperformed. Year-to-date, funding EM via EUR has generated strong total returns with little volatility. EUR-funded exposure has been the best approach for investors. Yet, given the challenges that can come with picking the most effective funding currency, a basket approach could similarly offer an attractive return profile for investors, with a G3 funding strategy delivering both attractive absolute returns with a Sharpe ratio only modestly below the narrower EUR-funded approach. (Exhibit 3 & Exhibit 4)

Diversified funding with DM commodity currencies, less attractive: Funding EM exposure via a broader basket of DM of G3 + CHF, AUD and CAD would have delivered a less attractive return profile with AUD helping to reduce volatility relative to USD funding but at the expense of returns.

Exhibit 1: EM gains vs G3 expected  
![](images/a81d58bce772147ee9fe5d735aa25fca6cb55828f99a43f112ff18a6725923da.jpg)

<details>
<summary>line chart</summary>

| Date   | EM FX vs G3 | EM FX vs USD | Forecast |
|--------|-------------|--------------|----------|
| Jun-19 | 100         | 100          | -        |
| Jun-21 | 100         | 95           | -        |
| Jun-23 | 120         | 105          | -        |
| Jun-25 | 140         | 120          | 130      |
| Jun-27 | 175         | 135          | 135      |
</details>

Source: Bloomberg, MS

Exhibit 2: Diversified funding reduces risk  
![](images/f87b3f7003ab9e188cd304eefd4aed6f995da17d8c79ad61af10881f6c7d4e8d.jpg)

<details>
<summary>bar chart</summary>

Expected Total Returns / Vol
| Period | EM vs USD | EM vs JPY | EM vs EUR | EM vs G3 |
| :--- | :--- | :--- | :--- | :--- |
| End-26 | 1.03 | 1.44 | 0.35 | 0.86 |
| Mid-27 | 0.96 | 1.78 | 1.53 | 1.38 |
</details>

Source: Bloomberg, MS

Exhibit 3: EM vs DM Gains Continue  
![](images/13ea8ee5b196a4e5aa28ed697af592768b546adc0accbeebfdbf25aba711a2a2.jpg)

<details>
<summary>line chart</summary>

| Date   | EM vs G3 | EM vs DM Basket |
|--------|----------|-----------------|
| Jun-25 | 100      | 100             |
| Sep-25 | 104      | 105             |
| Dec-25 | 108      | 110             |
| Mar-26 | 110      | 114             |
| Jun-26 | 112      | 116             |
</details>

Source: Bloomberg, MS

Exhibit 4: Long EM vs EUR has been effective, but vs G3 also attractive  
![](images/e53658cc22f56995cbd0bf7be98009a3b13d40597c27fcf5e893b6f44e3346d9.jpg)

<details>
<summary>bar chart</summary>

| Category       | Return (ytd, annualised) | Vol (ytd d/d, annualised) | Ratio |
| -------------- | ------------------------ | ------------------------- | ----- |
| EM_USD         | 6%                       | 7%                        | 0.5   |
| EM_EUR         | 9%                       | 4%                        | 2.5   |
| EM_JPY         | 11%                      | 7%                        | 1.5   |
| EM_CHF         | 5%                       | 6%                        | 0.5   |
| EM_AUD         | -8%                      | 5%                        | -1.5  |
| EM_CAD         | 9%                       | 6%                        | 1.5   |
| EM vs DM Basket| 5%                       | 4%                        | 1.0   |
| EM vs G3       | 9%                       | 5%                        | 1.5   |
</details>

Source: Bloomberg, MS

## Which Currencies or Baskets Have Been the Most Effective Funders Over Longer-Run Trends?

While EUR funded strategies have been the most successful so far this year, what about over a longer period?

We present some return statistics showing the pros and cons of funding EM currency exposure across:

\- a range of different individual DM currencies (USD, EUR, JPY, CHF, AUD, CAD)

\- three baskets of DM funding currencies, including: 1) an equally-weighted basket of these same 5 DM currencies; 2) an equally-weighted basket of the same currencies excluding USD and 3) a basket of USD, EUR and JPY - DM currencies that are more defensive in nature.

Our return statistics examined:

- the cumulative returns of all funding strategies, comparing the non-USD funding strategies vs USD funding  
- Volatility, Sharpe ratios, max drawdown, Calmar, hit ratios, worst 3m performance and the worst 12m performance.

The full sample of our return analysis runs from January 2010 to May 2026, and Exhibit 5 shows the full return statistics across the various funding strategies. The results are just indicative and are for comparative purposes, without taking into account any transaction costs or strategies for implementation. The results should be self explanatory but for clarity:

- The Calmar ratio shows the annualised returns divided by the absolute value of the maximum drawdown - an indicator of overall return vs portfolio stress.  
- The Hit Rate shows the number of positive return periods divided by the total number of periods - we are using daily data so a hit rate of 53% suggests returns were positive of 53% of trading days.

Exhibit 6 shows specifically the Sharpe ratios of the different strategies for funding long EM exposure over different horizons. In addition to the full sample since 2010 we also calculated the return statistics for the last 1, 3 and 5 years. Given the variety of FX market conditions over these time periods, conclusions that are consistent across the different time frames could be more robust.

Baskets outperform: Over the full sample since 2010, the funding EM exposure via baskets results generally produced more consistent outcomes that any single funding currency approach. Over the full sample, all 3 basket funding approaches generated significantly higher Sharpe ratios and materially lower drawdowns than the traditional USD-funded approach.

Importantly, this advantage persisted across the 5-year and 3-year horizons, suggesting that the benefit is not simply a consequence of the long USD bull market from 2010 to 2022. Not taking into account transaction costs of course artificially boosts the relative attractiveness of baskets, as these approaches would likely have involved higher costs.

Among the individual funding currency strategies, CAD stands out. In the full sample since 2010, long EM versus CAD delivered an annualized total return of 3.6%, volatility of 6.3%, and a Sharpe ratio of 0.58, which was close to the best basket result. It also had the lowest maximum drawdown among the individual funders at -12.3%, compared with -28.8% for USD, -25.2% for JPY, and -28.7% for CHF.

CAD also had the best worst-3-month and worst-12-month results among the single funders, at around -8.2% and -8.4%, respectively. This suggests that CAD funding historically provided a more balanced exposure: it improved return versus USD while not introducing the same degree of left-tail risk as JPY or CHF.

With the exception of the last 1y, funding long EM exposure in CAD has produced higher Sharpe ratios than the other individual funding currency choices across all time frames.

Exhibit 5: Return statistics for differently funded long EM currency exposure (since 2010)

<table><tr><td>Strategy</td><td>Ann. Return</td><td>Ann. Vol</td><td>Sharpe</td><td>Max Drawdown</td><td>Worst 3M</td><td>Worst 12M</td><td>Calmar</td><td>Hit Rate</td><td>Total Return</td></tr><tr><td>EM_USD</td><td>1.9%</td><td>7.3%</td><td>0.26</td><td>-28.8%</td><td>-15.5%</td><td>-18.4%</td><td>0.07</td><td>52.4%</td><td>37.2%</td></tr><tr><td>EM_EUR</td><td>3.2%</td><td>6.6%</td><td>0.48</td><td>-15.5%</td><td>-12.8%</td><td>-12.3%</td><td>0.20</td><td>52.4%</td><td>69.7%</td></tr><tr><td>EM_JPY</td><td>5.2%</td><td>10.7%</td><td>0.49</td><td>-25.2%</td><td>-16.9%</td><td>-19.8%</td><td>0.21</td><td>53.9%</td><td>136.8%</td></tr><tr><td>EM_CHF</td><td>0.3%</td><td>9.2%</td><td>0.03</td><td>-28.7%</td><td>-19.5%</td><td>-24.0%</td><td>0.01</td><td>51.4%</td><td>4.6%</td></tr><tr><td>EM_AUD</td><td>3.4%</td><td>7.5%</td><td>0.45</td><td>-18.5%</td><td>-11.2%</td><td>-17.8%</td><td>0.18</td><td>51.4%</td><td>75.0%</td></tr><tr><td>EM_CAD</td><td>3.6%</td><td>6.3%</td><td>0.58</td><td>-12.3%</td><td>-8.2%</td><td>-8.4%</td><td>0.30</td><td>52.9%</td><td>83.6%</td></tr><tr><td>Basket_All_Equal</td><td>3.1%</td><td>5.4%</td><td>0.57</td><td>-12.6%</td><td>-11.9%</td><td>-10.2%</td><td>0.25</td><td>53.4%</td><td>67.8%</td></tr><tr><td>Basket_NonUSD_Equal</td><td>3.3%</td><td>5.6%</td><td>0.59</td><td>-12.3%</td><td>-11.6%</td><td>-10.7%</td><td>0.27</td><td>53.8%</td><td>73.6%</td></tr><tr><td>Basket_G3_USD_EUR_JPY</td><td>3.7%</td><td>6.8%</td><td>0.54</td><td>

[中间内容因长度限制已省略]

er the reference number 149169; in the US by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i)

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

© 2026 MS
"""
