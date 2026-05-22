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
# Quantitative Equity Research

# Quant Matters – 2026 DM Quant Equity Mid-Year Outlook: Factors for an AI and Energy-Led Cycle

AI capex and energy volatility frame a more dispersed DM factor cycle: in the US, lean into self-funded growth and earnings delivery; in Europe, prioritize cash-flow resilience and capital discipline; in Japan, balance earnings-based value with selective growth exposure as rates remain key.

QuantWise $\left[\frac{q}{w}\right]$

# Key Takeaways

US: emphasizing quality growth as AI productivity cycle offsets energy headwinds, we recommend Internal Growth, Low PEG, and Up vs. Down EPS Revisions.   
Europe: positioning for energy-driven inflation, we recommend Operating Cash Flow Yield, Low YoY Asset Growth Factor, and 3m Up vs. Down EPS Revisions.   
Japan: using a combined macroeconomic and fundamental lens, we recommend Forward P/E, Low PEG, and Up vs. Down EPS Revisions.

4-Dimensions Framework Rankings (framework in this report) & Factor Views: Europe – Up vs Down EPS Revisions (3ma) (+), Operating CF Yield (+), Low Asset Growth (+). We revise Economic Cycle from Expansion to Slowdown. Comp Value weakened (5→11). Comp Growth climbed (17→13). Comp Quality dropped to bottom (15→17). Comp Momentum surged (9→2). Low Risk rebounded (14→7). Small Size slipped (2→6).

US – Up vs Down EPS Revisions (+), Internal Growth (+), Low PEG (+). Comp Value edged up (17→15). Comp Growth rose (16→14). Comp Quality slipped (11→12). Comp Momentum weakened (9→11). Low Risk softened (5→7). Small Size surged to top (12→1).

Japan – Up vs Down EPS Revisions (+). Forward Earnings Yield (+), Low PEG (+). Comp Value weakened (2→6). Comp Growth declined (11→14). Comp Quality held steady (15). Comp Momentum advanced (16→13). Low Risk slipped (9→10). Small Size held steady (5).

MS & CO. INTERNATIONAL PLC+

# Ronald Ho, CFA

Quantitative Analyst

Ronald.Ho@morganstanley.com +44 20 7425-2722

MS INDIA COMPANY PRIVATE LIMITED+

# Rakhi Arora

Quantitative Analyst

Rakhi.Arora@morganstanley.com +91 22 6996-2259

MS & CO. INTERNATIONAL PLC+

# Stephan Heller

Quantitative Analyst

Stephan.Heller@morganstanley.com +44 20 7425-9753

MS MUFG SECURITIES CO., LTD.+

# Ukyo Haraguchi, CFA

Quantitative Strategist

Ukyo.Haraguchi@morganstanleymufg.com +81 3 6836-8925

MS & CO. INTERNATIONAL PLC+

# Stephan M Kessler

Quantitative Analyst

Stephan.Kessler@morganstanley.com +44 20 7425-2854

# Recent Quant Matters report:

Quantitative Equity Research: Quant Matters – QAML (Quant + Analyst + Machine Learning): A Preview of Our New Stock Selection Model, 29 Apr 2026

QuantWise highlights research that incorporates a robust quantitative approach in our investment analysis.

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

# For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

# Topic of the Month: 2026 DM Quant Equity Mid-Year Outlook: Factors for an AI and Energy-Led Cycle

This month, we present our mid-year outlook for quant equities in the US, Europe and Japan. We recap the views of our economists (here) and strategists (here) as a starting point to highlight the equity factors that are likely to stand out in this environment.

The first half of 2026 has reinforced a familiar but more complex market message: macro and micro fundamentals remain supportive for risk assets, but return dispersion is likely to stay elevated. Strong earnings reports, resilient US labor markets and a powerful AI-driven capex cycle continue to support developed market equities. At the same time, energy-led volatility, driven by the Middle East conflict and uncertainty around the duration of the supply shock, has widened the range of potential macro outcomes. In this environment, the core message from our global strategists is constructive, not complacent.

DM equities remain the asset class preferred by our cross-asset strategists (here), with expected returns in the low-teens across major developed regions. While upside appears broadly similar across the US, Europe and Japan, our strategists prefer the US given its favorable bull-bear skew, stronger earnings profile and support from positive operating leverage. Europe and Japan also offer upside, but with more region-specific constraints: Europe is more exposed to energy-price volatility, faster pass-through into inflation and a different ECB reaction function, while Japan's outlook hinges on energy costs, wage growth, governance reform and sector leadership tied to AI, materials and defense.

The most important macro uncertainty is the oil-price path. Our economists note that the level and duration of the Middle East-related supply shock will dictate economic outcomes, with growth and inflation elasticities becoming increasingly non-linear as oil prices rise and remain elevated. The base case assumes de-escalation, but the range of outcomes is wider than usual. In the US, higher energy prices act as a tax on consumption, partially offsetting fiscal support, but AI capex and resilient labor markets keep the economy on a constructive path. In Europe, energy-price pass-through is faster and more direct, leaving the ECB with a different reaction function from the Fed. In Japan, higher energy prices create pressure on margins, but the broader equity story remains supported by domestic reflation, structural capex demand and improving corporate governance.

Across regions, one common thread remains central: the AI capex cycle. Hyperscaler capex expectations have been revised sharply higher, and the investment impulse from AI infrastructure is now relevant not only for technology and communication services, but also for semiconductors, industrials, utilities, power equipment, robotics, data centers and parts of credit and securitized markets. For quant investors, this reinforces the importance of factors that combine earnings delivery, quality, valuation discipline, cash-flow resilience and positive revisions.

Against this backdrop, our regional factor recommendations are as follows. In the US, we continue to emphasize Internal Growth, Low PEG, and Up vs. Down EPS Revisions, reflecting a preference for quality growth, valuation-aware earnings growth and positive earnings momentum. In Europe, we recommend Operating Cash Flow Yield, Low YoY Asset Growth, and 3-Month Up vs. Down EPS Revisions Breadth, reflecting the need for cash-flow resilience, capital discipline and earnings selectivity in an energy-sensitive market. In Japan, we recommend Forward Earnings Yield, Low PEG, and Up vs. Down EPS Revisions, combining value exposure, valuation-aware earnings growth and bottom-up earnings momentum in a rising but more dispersed equity market.

# US quant factors – Quality Growth as AI Productivity Cycle Offsets Energy Headwinds

In Exhibit 1, we show the key US forecasts from our economists and strategists for 2026 and 2027. Our economists expect US growth to soften modestly through mid-2026 as higher energy prices weigh on consumption, though AI-driven capex, fiscal support and resilient labor markets should continue to support underlying momentum. On an annual basis, real GDP growth is expected to be 2.2% in 2026 and 2.5% in 2027 as energy pressures fade and the economy avoids recession. Inflation remains above target in the near term, but both headline and core inflation are expected to decelerate over the forecast horizon, allowing the Fed to remain on hold through 2026 before delivering two cuts in 1H27.

Our US equity strategists continue to expect the rolling recovery to progress. The constructive equity view is primarily an earnings story rather than a multiple-expansion story. Positive operating leverage, AI adoption, “run it lean” efficiency gains, improving pricing power and continued momentum in the AI capex cycle are expected to support earnings growth. Sector preferences remain tilted toward Financials, Industrials, Consumer Discretionary Goods and hyperscalers.

Exhibit 1: Key economist and strategist forecasts – US 

<table><tr><td>Macro</td><td>Current</td><td colspan="2">Estimates</td></tr><tr><td>S&amp;P 500</td><td>7444.25</td><td colspan="2">8300 (2Q 2027)</td></tr><tr><td>US 10Y</td><td>4.47%</td><td colspan="2">4.20% (2Q 2027)</td></tr><tr><td></td><td>2025</td><td>2026E</td><td>2027E</td></tr><tr><td>GDP (Annual)</td><td>2.1</td><td>2.2</td><td>2.5</td></tr><tr><td>Inflation (Annual)</td><td>2.7</td><td>3.5</td><td>2.1</td></tr><tr><td>Policy Rate</td><td>3.625</td><td>3.625</td><td>3.125</td></tr></table>

Source: Datastream, MS. Data as of 13 May 2026.

Reflecting this combination of resilient earnings, AI-led productivity gains and persistent but moderating inflation pressure, we maintain our preference for Growth with a quality bias. We recommend positioning via three equity factors: Internal Growth, Low PEG, and Up vs. Down EPS Revisions. Together, these factors capture companies with the ability to fund growth internally, combine sustainable growth with valuation discipline, and benefit from positive analyst revisions as productivity gains and pricing power are incorporated into earnings forecasts.

We evaluate this factor mix through three lenses. First, in Exhibit 2, we present the backtested performance of our recommended US factors across rising and flat inflation regimes. Internal Growth and Up vs. Down EPS Revisions remain resilient across both regimes, while Low PEG performs particularly well in flatter inflation environments. This is consistent with the current macro setup: inflation remains a risk, but the direction of travel should become more benign as energy and tariff effects fade, allowing investors to re-focus on earnings quality and growth durability.

Second, in Exhibit 3, we evaluate the performance of our recommended US factors across normal and high Brent oil-volatility regimes. Internal Growth and Low PEG delivered positive returns in both regimes, with stronger performance during high oil volatility, highlighting the resilience of quality-growth and valuation-disciplined growth when energy uncertainty is elevated. Up vs. Down EPS Revisions performed positively in normal oil-volatility regimes but was weaker during high-volatility episodes, potentially because analyst estimates would lag the initial shock as earnings, margin and demand assumptions are recalibrated. This supports a balanced US factor basket: Internal Growth and Low PEG provide resilience during the energy-shock phase, while Up vs. Down EPS Revisions becomes more relevant as oil volatility stabilizes and earnings visibility improves.

Third, in Exhibit 4, we assess the thematic alignment of our recommended factors with the AI & Tech Diffusion main theme and AI Infrastructure sub-theme, measured as the mean exposure of top-quintile stocks minus bottom-quintile stocks. The exhibit shows positive exposure to the AI themes, reinforcing the alignment of our factor recommendations with our US equity strategists' emphasis on AI as a key driver of the earnings cycle. The exposure to AI Infrastructure is particularly relevant as AI-related capex remains an important global theme, with hyperscaler capex expectations revised sharply higher for 2026 and 2027.

Exhibit 2: Backtest performance of our recommended US factors in rising and flat inflation scenarios – Internal Growth and EPS Revisions Breadth remain resilient across regimes, while Low PEG benefits from flatter inflation environments   
![](images/90c2e8f018bcc6e9861724df316ca18ab2edd0e7ac1e5b9b985ce8f74ad98b93.jpg)

<details>
<summary>bar</summary>

| Scenario        | Internal Growth | EPS Up vs. Down Revisions | Low PEG |
| --------------- | --------------- | ------------------------- | ------- |
| Inflation Rising | 1.8%            | 1.8%                      | -0.5%   |
| Inflation Flat   | 1.0%            | 6.8%                      | 2.1%    |
</details>

Source: Factset, Haver, MS. Inflation regimes based on spread between 1M and 6M moving averages of lagged inflation. Regimes classified as Rising when spread exceeds +0.15 and Flat when between -0.15 and +0.15. Factor returns are shown on an annualized basis. Data as of Dec 2024.

Exhibit 3: Internal Growth and Low PEG remain resilient in high oil volatility, while EPS Revisions improve as volatility normalizes   
![](images/87b8c2b3c4392162e781347f131521449ee7100097f3917bdc7a91a527efa0ab.jpg)

<details>
<summary>bar</summary>

Annualized Performance of our recommended US Factors in High and Normal Oil Volatility Regimes
| Factor | High oil volatility (%) | Normal oil volatility (%) |
|---|---|---|
| Internal Growth | 7.8 | 0.9 |
| Low PEG | 13.2 | 3.1 |
| EPS Up vs. Down Revisions | -1.5 | 2.6 |
</details>

Source: Datastream, MS. Oil-volatility regimes are defined using weekly Brent prices. Realized oil volatility is calculated as the annualized 12-week (\~3M) rolling standard deviation of weekly Brent returns. High and normal oil-volatility regimes correspond to periods above the 75th percentile and between the 25th and 75th percentiles, respectively. Factor returns are shown on an annualized basis.

Exhibit 4: Recommended US Factors Capture AI Diffusion and Infrastructure Capex Exposure   
![](images/5f2a3039b0bf1fe594a9d8278da325e3b3ccf782c01a87022e1728c800746dad.jpg)

<details>
<summary>bar</summary>

Net thematic exposure of US recommended factors to selected AI themes
| Factor | AI & Tech Diffusion | AI Infrastructure |
| :--- | :--- | :--- |
| Up vs. Down EPS Revisions | 0.12 | 0.20 |
| Low PEG | 0.26 | 0.18 |
| Internal Growth | 0.34 | 0.37 |
</details>

Source: FactSet, Datastream, MS. Each stock's sensitivity to thematic movements is estimated in two steps: we first obtain the thematic-specific return by regressing the thematic portfolio's weekly return on MSCI ACWI Equal-Weight (EQL) and defining the theme-specific component as the regression intercept plus the residual. We then regress each stock's weekly return on this thematic-specific return, controlling for EQL, to estimate its thematic beta. All regressions are run over a rolling two-year weekly estimation horizon (approximately 104 observations). Data as of April 30, 2026.

Having evaluated the recommended factors across the broader macro and thematic lenses, we now take a more granular view of the supportive characteristics behind each signal. We continue to favor a quality-oriented approach to growth investing, positioning Internal Growth as our preferred factor within the US equity landscape. Internal Growth is explicitly defined as:

# Internal Growth = Retention Ratio × ROE

Among the growth factors we analyze, Internal Growth distinctly exhibits the strongest positive exposure to quality characteristics, measured as the difference between median Composite Quality scores of top quintile (Q1) and bottom quintile (Q5) portfolios (see Exhibit 5). This notable quality tilt underscores the factor's strategic appeal, identifying companies capable of sustainably funding growth internally through disciplined profitability and effective reinvestment.

To further illustrate the fundamental strengths underlying Internal Growth, we employ the DuPont decomposition framework to expand ROE into its component drivers:

# ROE = Profit Margin × Asset Turnover × Financial Leverage

In Exhibit 6, we apply this decomposition by comparing median fundamental exposures of top quintile (Q1) versus bottom quintile (Q5) firms. The top-quintile companies consistently demonstrate superior fundamentals across all key drivers – including notably stronger profit margins and greater asset efficiency, partly offset by lower financial leverage – highlighting their ability to sustain internally funded growth. This aligns with our US equity strategists' view that the rolling recovery is being driven by earnings durability, positive operating leverage and AI-enabled efficiency gains. Internal Growth is well suited to that backdrop because it captures companies with the profitability and retained earnings capacity to fund expansion internally.

Exhibit 5: Internal Growth factor stands out with strongest quality exposure, highlighting companies with sustainable profitability and disciplined reinvestment   
![](images/06c5d11c5efc7a0b52351e0d3d5e9f4913562174f9e792f7211663d3bb0736a2.jpg)

<details>
<summary>bar</summary>

| Category             | Value |
| -------------------- | ----- |
| Internal Growth      | 0.45  |
| Low PEG              | -0.18 |
| Long Term Growth     | -0.12 |
| YoY Earnings Growth  | -0.05 |
| YoY Sales Growth     | -0.25 |
| ST EPS Growth Rate   | -0.15 |
</details>

Source: Factset, MS. Data as of April 30, 2026.

Exhibit 6: Top-quintile stocks in EPS revisions factor show superior operating leverage, margin momentum, and R&D intensity, aligned with strategists' rolling recovery outlook.   
![](images/66694b7aa7c9e1d884e9567ebc8d8a96aa66fb13c92a431c8b2605225cf5f56a.jpg)

<details>
<summary>bar</summary>

Internal Growth Decomposition: Relative Strength of Key Drivers (Q1 vs Q5)
| Metric | Quintile 1 | Quintile 5 |
| :--- | :--- | :--- |
| Low Leverage | 0.54 | 0.34 |
| Asset Turnover | 0.66 | 0.24 |
| Profit Margin | 0.72 | 0.28 |
| Retention | 0.66 | 0.10 |
</details>

Source: Factset, MS. Data as of April 30, 2026.

As a complement to Internal Growth, Low PEG adds valuation discipline to the quality-growth framework. The Low PEG factor identifies companies with attractive valuations relative to their earnings growth trajectories.

Exhibit 7 shows the rolling 252-day correlation of Low PEG with Composite Value and Composite Growth. Low PEG has recently shown a higher correlation with Composite Growth than Composite Value, which is particularly relevant in the current US backdrop. Our strategists expect modest multiple compression, with the S&P 500 forward P/E declining to 20.5x from 21.2x, making their bullish index view an earnings story r

[中间内容因长度限制已省略]

 providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., authorised and regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the US by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

MS Hong Kong Securities Limited is the liquidity provider/market maker for securities of Las Vegas Sands Corp listed on the Stock Exchange of Hong Kong Limited. An updated list can be found on HKEx website: http://www.hkex.com.hk.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The following companies do business in countries which are generally subject to comprehensive sanctions programs administered or enforced by the U.S. Department of the Treasury's Office of Foreign Assets Control ("OFAC") and by other countries and multi-national bodies: Holcim Ltd..

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products.

MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

© 2026 MS
"""
