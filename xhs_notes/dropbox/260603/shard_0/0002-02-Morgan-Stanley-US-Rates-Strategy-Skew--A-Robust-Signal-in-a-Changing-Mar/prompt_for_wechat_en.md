You are a senior financial newsletter editor with a consulting-style strategy lens. You turn research-report material into a long-form English article that is structured, insightful, and suitable for a serious business audience.

Objective:
- Write an English Markdown article based on the report parsing below.
- Target length: around 2200 words, plus or minus 15%.
- Tone: serious, analytical, strategic, and readable.
- The article should not feel like a summary. It should make an argument.
- You may extend the report's logic into reasonable second-order implications, but do not invent data, company actions, or quotes.
- Do not disclose every detail. Leave several meaningful open questions that make readers want the full report.

McKinsey-style writing principles:
1. Answer first: open with the controlling idea, not background.
2. Governing thought: every section must support the main answer.
3. Mutually exclusive, collectively exhaustive logic: avoid overlapping sections.
4. So what: every section must explain why the point matters.
5. Synthesis over summary: do not list facts; interpret what the pattern means.
6. Action titles: section headings must be complete, insight-bearing sentences. Do not use generic headings such as "Key Takeaways", "Market Background", "Core View", or "Reader Implications".
7. Natural hooks: if you want readers to join the community or read the full report, the hook should emerge from unresolved analytical questions, not from promotional language.

Required Markdown structure:
- `# Title`: make it a direct argument, not a topic label.
- Opening: 4-6 short paragraphs that state the main thesis and why now matters.
- 4-6 `##` sections. Each `##` heading must be an action title: a sentence that tells the reader the insight.
- One section should identify what the report does not fully answer yet.
- One section should translate the report into a decision framework for readers.
- Final section: naturally invite readers to join the community or read the full report using this CTA: Join the community to read the full report and review the original charts.
- End with: `*This article is for learning and discussion only and does not constitute investment advice.*`

Content boundaries:
- Do not mention specific investment bank names such as GS. Use "a global investment bank report" if needed.
- Do not use emoji.
- Do not write like a viral post.
- Do not output your reasoning process.
- Do not generate image Markdown; the system will insert original MinerU images afterward.

Report parsing:
"""
# US Rates Strategy | North America

# Skew: A Robust Signal in a Changing Market

We show that the skew signal is robust across model parameter choices and has retained predictive power for rate moves over the past 17 years. Since 2019, more frequent shocks have favored faster signals. Predictive power has weakened in front-end rates but strengthened in longer-dated tails.

# Key Takeaways

We extend the skew analysis across market regimes to understand when the signal works, when it fails, and what drives performance.   
■ Results are consistent across model parameter choices, whether duration is expressed through swaps or Treasury futures, and across short-dated expiries.   
The signal retains predictive power back to at least 2009. Since 2019, faster signals have outperformed amid more frequent shocks.   
Predictive power weakened in 2y tails as macro shocks dominated front-end rates, but improved in 30y tails where positioning remains important.   
The signal continues to point to short duration across the curve, with skew richening further despite already elevated starting levels.

Please add me to your distribution list.

MS & CO. LLC

# Shaun Zhou

Strategist

Shaun.Zhou@morganstanley.com +1 212 761-3348

# Matthew Hornbach

Strategist

Matthew.Hornbach@morganstanley.com +1 212 761-1837

# Martin W Tobias, CFA

Strategist

Martin.Tobias@morganstanley.com +1 212 761-6076

# Aryaman Singh

Strategist

Aryaman@morganstanley.com +1 212 761-1993

# Eli P Carter

Strategist

Eli.Carter@morganstanley.com +1 212 761-4703

2026 EXTEL

ALL-AMERICA RESEARCH POLL

May 26 – June, 12 2026

VIEW OUR ANALYSTS >

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

# Interest Rate Derivative Strategy

# United States | Skew: A robust signal in a changing market

MS & CO. LLC

Shaun Zhou +1 212 761-3348

Matthew Hornbach, CMT
Matthew.Hornbach@morganstanley.com +1 212 761-1863

Martin Tobias, CFA, CMT
Martin.Tobias@morganstanley.com +1 212 761-6076

Aryaman Singh
Aryaman@morganstanley.com +1 212 761-1993

Eli Carter
Eli.Carter@morganstanley.com +1 212 761-4703

# Follow-up on the skew signal analysis

# Executive summary

In our previous note, we showed that changes in short-expiry skew contain predictive information about subsequent rate moves. In this follow-up, we test the robustness of that result across different implementation choices, parameter specifications, and market regimes. We find that:

- The signal remains robust. Performance is broadly unchanged when duration exposure is expressed using swaps rather than Treasury futures. Similarly, skew signals derived from 1m, 3m, and 6m expiries produce comparable results, suggesting that the information content is not tied to a specific instrument.   
- The signal also exhibits a meaningful information horizon. Predictive power remains observable for at least several days after a skew move, although its value declines over time. This suggests that changes in skew are incorporated into rates gradually rather than immediately.   
- Extending the sample back to 2009 confirms that the relationship is not unique to the post-COVID period. However, performance has become more sensitive to signal speed since 2019. Across lookback-window and trading delays, faster-moving signals have generally outperformed slower-moving alternatives.   
- Since 2019, signal performance deteriorated most in the 2y sector, where rate moves have increasingly been driven by macro and policy shocks. By contrast, the 30y tail experienced the largest improvement, suggesting that investor positioning remains an important driver of long-end rates.

Overall, the evidence suggests that skew captures a genuine feature of market behavior rather than a sample-specific artifact. We think the key lesson from the post-2019 period is that markets began changing faster.

# Testing signal robustness

The robustness analysis spans a large parameter space. We evaluate four lookback windows, three expiries, and 10 trading delays, resulting in 120 specifications.

The goal of is not to identify the best-performing combination – that would be data mining. Rather, we want to test whether the signal remains effective under reasonable specification changes and use-performance differences to understand when and why the signal works.

# One chart is worth a thousand words

Exhibit 1 summarizes the results using a bubble chart. For each specification, we focus on three aspects of performance: risk-adjusted return (Sharpe ratio on y-axis), downside risk (maximum drawdown on x-axis), and consistency (the percentage of months with positive cumulative returns as bubble size). Opacity represents trading delay. The darkest bubble indicates 1-day trading delay, where the lightest indicates 10-day trading delay (i.e., trade based on signal observed 10 days ago).

This visualization allows us to compare all 120 strategy specifications simultaneously. All else equal, the most attractive configurations are those that combine high Sharpe ratios, limited drawdowns, and strong consistency, appearing as large bubbles in the top-right portion of the chart.

Two conclusions stand out. First, the results are broadly consistent with those obtained using Treasury futures, and performance varies little across 1m, 3m, and 6m expiries. This suggests the signal reflects broad investor positioning rather than the pricing of a specific instrument or point on the skew surface.

Second, the 21-day lookback delivers the most consistent performance. Shorter lookbacks can achieve similar Sharpe ratios but are more sensitive to noise, while the 63-day lookback generally underperforms.

Overall, the signal appears robust to the choice of duration instrument and option expiry. Performance is more sensitive to the speed at which changes in skew are measured, with the 21-day lookback providing a reasonable balance between responsiveness and stability.

Exhibit 1: 10y tail results for all combinations of lookback window, option expiry, and trading delay   
![](images/5ed37ab2f268c5a5c036de539e3c4941599362b7b320503ea5e1fe40c8b1f5d4.jpg)  
Source: Bloomberg, S&P, MS

# Compare LIBOR and SOFR era

The LIBOR-SOFR transition provides a convenient division of the sample into two distinct macro environments. The LIBOR era (2009 to mid-2019) was characterized by persistently low rates and subdued volatility, while the SOFR era (mid-2019 to today) encompassed the pandemic shock, inflation surge, subsequent policy tightening cycle, and the current Iran conflict.

The comparison shows that the deterioration of the 63-day lookback is largely a post-2019 phenomenon (Exhibit 2 and Exhibit 3). During the LIBOR era, it performed similarly to shorter lookbacks. During the SOFR era, performance weakened materially while shorter specifications remained more resilient.

Exhibit 2: 10y tail results during 2009 - 2019   
![](images/de60446ccac5385f53f17e0dc497725047e23e585c6e599d9fcc4bbff56b8738.jpg)  
Source: Bloomberg, S&P, MS

Exhibit 3: 10y tail results from 2019 - today   
![](images/4d20f4a60d5e1eb9cd18d21d7797ea9a3d341f1ebb8b456da39ab21da236c28e.jpg)

<details>
<summary>scatter</summary>

| Max Drawdown | Sharpe Ratio (10Y SOFR) | Maturity |
| ------------ | ------------------------ | -------- |
| -30%         | -0.4                     | 6M       |
| -25%         | 0.2                      | 1M       |
| -20%         | 0.3                      | 3M       |
| -15%         | 0.4                      | 6M       |
| -10%         | 0.6                      | 1M       |
| -5%          | 0.8                      | 3M       |
| -30%         | -0.2                     | 10-day   |
| -25%         | 0.1                      | 10-day   |
| -20%         | 0.3                      | 10-day   |
| -15%         | 0.5                      | 10-day   |
| -10%         | 0.7                      | 10-day   |
| -5%          | 0.9                      | 10-day   |
| -30%         | -0.3                     | 21-day   |
| -25%         | 0.2                      | 21-day   |
| -20%         | 0.4                      | 21-day   |
| -15%         | 0.6                      | 21-day   |
| -10%         | 0.8                      | 21-day   |
| -5%          | 1.0                      | 21-day   |
| -30%         | -0.4                     | 63-day   |
| -25%         | 0.1                      | 63-day   |
| -20%         | 0.3                      | 63-day   |
| -15%         | 0.5                      | 63-day   |
| -10%         | 0.7                      | 63-day   |
| -5%          | 0.9                      | 63-day   |
| -30%         | -0.3                     | 1M       |
| -25%         | 0.2                      | 1M       |
| -20%         | 0.4                      | 1M       |
| -15%         | 0.6                      | 1M       |
| -10%         | 0.8                      | 1M       |
| -5%          | 1.0                      | 1M       |
| -30%         | -0.2                     | 3M       |
| -25%         | 0.1                      | 3M       |
| -20%         | 0.3                      | 3M       |
| -15%         | 0.5                      | 3M       |
| -10%         | 0.7                      | 3M       |
| -5%          | 0.9                      | 3M       |
| -30%         | -0.1                     | 6M       |
| -25%         | 0.2                      | 6M       |
| -20%         | 0.4                      | 6M       |
| -15%         | 0.6                      | 6M       |
| -10%         | 0.8                      | 6M       |
| -5%          | 1.0                      | 6M       |
| -30%         | 0.3                      | 1M       |
| -25%         | 0.5                      | 1M       |
| -20%         | 0.7                      | 1M       |
| -15%         | 0.9                      | 1M       |
| -10%         | 1.1                      | 1M       |
| -5%          | 1.3                      | 1M       |
| -30%         | 0.4                      | 3M       |
| -25%         | 0.6                      | 3M       |
| -20%         | 0.8                      | 3M       |
| -15%         | 1.0                      | 3M       |
| -10%         | 1.2                      | 3M       |
| -5%          | 1.4                      | 3M       |
| -30%         | 0.5                      | 6M       |
| -25%         | 0.7                      | 6M       |
| -20%         | 0.9                      | 6M       |
| -15%         | 1.1                      | 6M       |
| -10%         | 1.3                      | 6M       |
| -5%          | 1.5                      | 6M       |
| -30%         | 0.6                      | 1M       |
| -25%         | 0.8                      | 1M       |
| -20%         | 1.0                      | 1M       |
| -15%         | 1.2                      | 1M       |
| -10%         | 1.4                      | 1M       |
| -5%          | 1.6                      | 1M       |
| -30%         | 0.7                      | 3M       |
| -25%         | 0.9                      | 3M       |
| -20%         | 1.1                      | 3M       |
| -15%         | 1.3                      | 3M       |
| -10%         | 1.5                      | 3M       |
| -5%          | 1.7                      | 3M       |
| -30%         | 0.8                      | 6M       |
| -25%         | 1.0                      | 6M       |
| -20%         | 1.2                      | 6M       |
| -15%         | 1.4                      | 6M       |
| -10%         | 1.6                      | 6M       |
| -5%          | 1.8                      | 6M       |
| -30%         | 0.9                      | 1M       |
| -25%         | 1.1                      | 1M       |
| -20%         | 1.3                      | 1M       |
| -15%         | 1.5                      | 1M       |
| -10%         | 1.7                      | 1M       |
| -5%          | 1.9                      | 1M       |
| -30%         | 1.0                      | 3M       |
| -25%         | 1.2                      | 3M       |
| -20%         | 1.4                      | 3M       |
| -15%         | 1.6                      | 3M       |
| -10%         | 1.8                      | 3M       |
| -5%          | 2.0                      | 3M       |
| -30%         | 1.2                      | 6M       |
| -25%         | 1.4                      | 6M       |
| -20%         | 1.6                      | 6M       |
| -15%         | 1.8                      | 6M       |
| -10%         | 2.0                      | 6M       |
| -5%          | 2.2                      | 6M       |
| -30%         | 1.4                      | 1M       |
| -25%         | 1.6                      | 1M       |
| -20%         | 1.8                      | 1M       |
| -15%         | 2.0                      | 1M       |
| -10%         | 2.2                      | 1M       |
| -5%          | 2.4                      | 1M       |
| -30%         | 1.6                      | 3M       |
| -25%         | 1.8                      | 3M       |
| -20%         | 2.0                      | 3M       |
| -15%         | 2.2                      | 3M       |
| -10%         | 2.4                      | 3M       |
| -5%          | 2.6                      | 3M       |
| -30%         | 1.8                      | 6M       |
| -25%         | 2.0                      | 6M       |
| -20%         | 2.2                      | 6M       |
| -15%         | 2.4                      | 6M       |
| -10%         | 2.6                      | 6M       |
| -5%          | 2.8                      | 6M       |
| -30%         | 2.0                      | >6M      |
| -25%         | <line>                   | >6M      |
| -20%         | <line>                   | >6M      |
| -15%         | <line>                   | >6M      |
| -10%         | <line>                   | >6M      |
| -5%          | <line>                   | >6M      |
| +5           | <line>                   | >6M      |
The chart displays the Sharpe Ratio for each period (Max Drawdown) on the x-axis and the Sharpe Ratio for each period (Max Drawdown) on the y-axis.
</details>

Source: Bloomberg, S&P, MS

# Signal decay

The original note focused on strategies with a one-day trading delay, whereby positions are established on $(t+1)$ and held through $(t+2)$ based on signals observed at $(t)$ .

Here, we extend the framework to consider longer trading delays. Strategies with longer holding periods can be replicated as linear combinations of portfolios formed using different trading delays, enabling us to characterize the evolution of signal alpha over time.

Examining performance across different trading delays provides insight into how quickly the information embedded in skew is incorporated into rates. Exhibit 4 and Exhibit 5 show the historical total return of strategies based on 3m10y skews.

During 2009 - 2019, all trading delays from one to ten days generated positive returns, although performance declined as delays increased. The same pattern persists after 2019. This suggests that the information contained in skew was not immediately reflected in market prices and remained relevant for several days after the signal was observed.

Most strategy specifications experienced a drawdown between July 2021 and July 2023. Short-delay strategies eventually recovered from the drawdown, while longer-delay strategies did not.

Exhibit 4: Historical return over the LIBOR era   
![](images/f007926772888f8bf6465717d9e8f2481af37e20a3639dc59285283be22727e9.jpg)

<details>
<summary>line</summary>

| Year | 1-day delay | 2-day | 3-day | 4-day | 5-day | 6-day | 7-day | 8-day | 9-day |
|------|-------------|-------|-------|-------|-------|-------|-------|-------|-------|
| '09  | ~0%         | ~0%   | ~0%   | ~0%   | ~0%   | ~0%   | ~0%   | ~0%   | ~0%   |
| '10  | ~10%        | ~5%   | ~10%  | ~5%   | ~5%   | ~5%   | ~5%   | ~5%   | ~5%   |
| '11  | ~20%        | ~10%  | ~20%  | ~10%  | ~10%  | ~10%  | ~10%  | ~10%  | ~10%  |
| '12  | ~30%        | ~15%  | ~30%  | ~15%  | ~15%  | ~15%  | ~15%  | ~15%  | ~15%  |
| '13  | ~40%        | ~20%  | ~40%  | ~20%  | ~20%  | ~20%  | ~20%  | ~20%  | ~20%  |
| '14  | ~50%        | ~25%  | ~50%  | ~25%  | ~25%  | ~25%  | ~25%  | ~25%  | ~25%  |
| '15  | ~60%        | ~30%  | ~60%  | ~30%  | ~30%  | ~30%  | ~30%  | ~30%  | ~30%  |
| '16  | ~70%        | ~35%  | ~70%  | ~35%  | ~35%  | ~35%  | ~35%  | ~35%  | ~35%  |
| '17  | ~75%        | ~40%  | ~75%  | ~40%  | ~40%  | ~40%  | ~40%  | ~40%  | ~40%  |
| '18  | ~80%        | ~45%  | ~80%  | ~45%  | ~45%  | ~45%  | ~45%  | ~45%  | ~45%  |
| '19  | ~85%        | ~50%  | ~85%  | ~50%  | ~50%  | ~50%  | ~50%  | ~50%  | ~50%  |
| '20  | ~90%        | ~55%  | ~90%  | ~55%  | ~55%  | ~55%  | ~55%  | ~55%  | ~55%  |
</details>

Source: Bloomberg, S&P, MS

Exhibit 5: Historical return over the SOFR era   
![](images/6984d2c530b3abd6ee7740050543033c223fd9d8189a3da34f3679cdf4c30a66.jpg)

<details>
<summary>line</summary>

| Year | 1-day delay | 2-day | 3-day | 4-day | 5-day | 6-day | 7-day | 8-day | 9-day |
|------|-------------|-------|-------|-------|-------|-------|-------|-------|-------|
| '19  | ~0%         | ~0%   | ~0%   | ~0%   | ~0%   | ~0%   | ~0%   | ~0%   | ~0%   |
| '20  | ~5%         | ~5%   | ~5%   | ~5%   | ~5%   | ~5%   | ~5%   | ~5%   | ~5%   |
| '21  | ~10%        | ~10%  | ~10%  | ~10%  | ~10%  | ~10%  | ~10%  | ~10%  | ~10%  |
| '22  | ~15%        | ~15%  | ~15%  | ~15%  | ~15%  | ~15%  | ~15%  | ~15%  | ~15%  |
| '23  | ~5%         | ~5%   | ~5%   | ~5%   | ~5%   | ~5%   | ~5%   | ~5%   | ~5%   |
| '24  | ~10%        | ~10%  | ~10%  | ~10%  | ~10%  | ~10%  | ~10%  | ~10%  | ~10%  |
| '25  | ~20%        | ~20%  | ~20%  | ~20%  | ~20%  | ~20%  | ~20%  | ~20%  | ~20%  |
| '26  | ~15%        | ~15%  | ~15%  | ~15%  | ~15%  | ~15%  | ~15%  | ~15%  | ~15%  |
</details>

Source: Bloomberg, S&P, MS

# A closer look at 2021 to 2023

The period from 2021 to 2023 represents the most significant underperformance episode for the skew signal and provides useful insight into its limitations.

The first challenge was that skew repriced early in the selloff. As investors adjusted to higher inflation, payer 

[中间内容因长度限制已省略]

ce Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., authorised and regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the US by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

The following authors are Fixed Income Research Analysts/Strategists and are not opining on or expressing recommendations on equity securities: Aryaman Singh; Shaun Zhou; Eli P Carter; Matthew Hornbach; Martin W Tobias, CFA.

© 2026 MS
"""
