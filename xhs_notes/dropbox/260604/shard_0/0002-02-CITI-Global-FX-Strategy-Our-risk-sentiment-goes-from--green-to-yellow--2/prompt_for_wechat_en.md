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
02 Jun 2026 17:31:01 ET | 17 pages

# Global FX Strategy

Our risk sentiment goes from "green to yellow"

# CITI'S TAKE

Recent indicators suggest increasing potential for a risk correction. These do not turn us bearish risk but tell us the probability of a move lower is increasing. We flag indicators to watch that would turn us outright bearish risk assets, but for now we simply see the backdrop as one where the recent drop in volatility is an opportunity to add tactical risk hedges. One complication for FX has been the increased frequency with which we see equities down with yields up, which produces very different FX behavior compared to equities down with yields down. We like JPY strangles for that uncertainty. Another complication is that historic risk currencies tend to also have positive terms of trade that would benefit should the Iran conflict escalate. Therefore, we prefer puts in SEK and NZD over NOK and AUD as risk-off hedges.

# Daniel Tobon AC

+1-212-816-8340

daniel.tobon@citi.com

# Brian Levine $^{AC}$

+1-212-816-6896

brian.levine@citi.com

# Osamu Takashima

+81-3-6776-3251

osamu.takashima@citi.com

Resilient global growth expectations, the AI capex cycle, better-than-expected energy inventory management, and expectations of a resolution to the Iran conflict have all supported global risk assets in recent months despite consistently elevated uncertainty on the Strait of Hormuz. We have seen this as a positive backdrop for high beta/carry currencies that also benefit from a positive terms of trade impact from the conflict (AUD, NOK, Latam FX).

However, we suspect we are shifting from a positive-risk backdrop to one with increased vulnerability for a correction. To be clear, increased vulnerability of a correction and expectations we are going to see a correction are not the same thing; however, with vol at low levels, downside protection looks attractive. In other words, we would not be exiting risk positions necessarily, but we would be using low vol as an opportunity to add downside hedges.

Below we highlight the current indicators turning us more cautious on risk (“green to yellow”), what it would take to get us outright bearish risk (“yellow to red”), and implications for FX. We stress again this is tactical in nature, and we would still be dip buyers of risk assets on corrections.

# Sentiment shifting from green to yellow

We flag the developments turning us more cautious:

\- Equity Strategy is cautious: Citi's US Equity Strategy team has flagged that the Q1 earnings blowout has led to an equity rally that now appears to have priced euphoric expectations. Thematically, they prefer taking profit on price momentum – a factor that outperformed – and rotating into earnings momentum and quality improvement. This is consistent with their view that more acute bouts of volatility should be expected given high growth expectations, especially if yields remain elevated.

\- POLLS flashes red: One of our favorite risk indicators is POLLS (Positioning, Optimism, Liquidity, Leverage and Stress), which was developed by our equity markets colleagues. It reached 18 last week, a trigger typically seen ahead of corrections. The Quant Global Macro team shows that SPX returns in the next 30-50 trading days are weaker.

\- Earnings season is over: The end of earnings season may remove a tailwind for stocks. We note the relative outperformance of the S&P 500 during earnings season, along with smaller drawdowns and quicker recoveries to new highs (Figure 1). Equities still perform during non-earnings season, though with greater volatility. Re-running the study using the S&P 500 equal-weight series tells a more striking story (Figure 2): broad stock gains have come from earnings (fundamentals work!) but outside of earnings have done little.

Figure 1. S&P 500 returns are strongest during earnings season, with smaller drawdowns and quicker recoveries   
![](images/74856915450f1dcc6da190234ff2cb52febc2838ad07eb4ca289dd6641d7dd12.jpg)

<details>
<summary>line</summary>

| Date   | Earnings Season | All Other Days |
|--------|-----------------|----------------|
| Jan/21 | ~0%             | ~0%            |
| Jan/22 | ~10%            | ~15%           |
| Jan/23 | ~15%            | ~5%            |
| Jan/24 | ~25%            | ~10%           |
| Jan/25 | ~40%            | ~15%           |
| Jan/26 | ~50%            | ~20%           |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
We define “earnings season” from the 10 $^{th}$ (or closest trading day) of the month following quarter-end to NVDA earnings +3 days.   
Source: Citi, Bloomberg

Figure 2. The equally-weighted S&P 500 is more sensitive to earnings, with little happenings outside of the period   
![](images/fa8755a96bf8b2661e68ba6fa977b5f2a772be98aa8a9049159c2ccc1fb3efda.jpg)

<details>
<summary>line</summary>

| Date   | Earnings Season | All Other Days |
|--------|-----------------|----------------|
| Jan/21 | ~0%             | ~0%            |
| Jan/22 | ~15%            | ~10%           |
| Jan/23 | ~25%            | ~-5%           |
| Jan/24 | ~30%            | ~0%            |
| Jan/25 | ~40%            | ~-15%          |
| Jan/26 | ~50%            | ~0%            |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
We define “earnings season” from the 10 $^{th}$ (or closest trading day) of the month following quarter-end to NVDA earnings +3 days.   
Source: Citi, Bloomberg

\- Equity dispersion extreme: The ratio of S&P 500 constituent volatility versus index volatility has reached historically extreme levels (above 2.5; Figure 3). This shows large dispersion, which can be typical during earnings season (related to the point above). It is notable that prior moves above 2.5 have typically seen sideways/lower price in equities (Figure 4).

Figure 3. Constituent vol vs index vol is at extreme levels   
![](images/724bf598cb7feb0e657b79af7bfe884d920c4566f0e6d79833408ec515a6d909.jpg)

<details>
<summary>line</summary>

| Date   | VIXEQ/VIX Ratio |
|--------|-----------------|
| Jan/24 | 2.5             |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: Citi, Bloomberg

Figure 4. This generally sees equities sideways/lower   
![](images/9e457f51ece5a649b5c56d2324f8ff34880cfef2266eb586898d65a9476ea23b.jpg)

<details>
<summary>line</summary>

| Weekdays around flag (t=O indexed to 0) | Mean | Median | 75th & 25th Pctl | Current (RHS) |
| --------------------------------------- | ---- | ------ | ---------------- | ------------- |
| T-30                                    | 96   | 95     | 94               | 93            |
| T-20                                    | 97   | 97     | 96               | 95            |
| T-10                                    | 98   | 98     | 97               | 97            |
| 0                                       | 100  | 100    | 100              | 100           |
| T+10                                    | 101  | 101    | 102              | 101           |
| T+20                                    | 100  | 100    | 101              | 102           |
| T+30                                    | 99   | 99     | 100              | 101           |
| T+40                                    | 100  | 101    | 102              | 102           |
| T+50                                    | 98   | 102    | 103              | 103           |
| T+60                                    | 97   | 101    | 102              | 102           |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: Citi, Bloomberg

\- Cracks in AI narrative?: We are believers in the AI capex story, and its potential to keep driving economic growth, earnings and eventually productivity (though to what degree on the latter is still uncertain).

However, recent news around corporate AI costs (Axios 05/28) could call into question the pace of spend by end users.

\- Put-call spread collapse: The CBOE Equity Put/Call Ratio hit new lows last week to levels rarely seen over the past decade. S&P 500 normalized 1m skew shows a similar demand for calls over puts (Figure 5). This suggests investors have built euphoric longs through options. Two implications:

- Low put ownership could see chasing of put buying in risk-off, which is positive for vol. Vol squeezes fuel VAR-driven unwinds.   
☐ Dealers may be long equities to hedge skewed positioning (they are the net call sellers to the market). Should equities start to sell-off, dealers could exacerbate the move by reducing their delta hedges.

Again, this is not necessarily a risk-off signal but does point to euphoric sentiment and downside acceleration risk if equities begin to move lower.

\- Midterm seasonality: Midterm years tend to underperform non-midterms years, and this becomes especially notable starting in June (Figure 6). This may be due to expectations of less fiscal as mid-term years tend to see congressional leadership change/divided government. Or it could be a coincidence. We do not put significant weight on this, but note it as interesting in light of all the other risks flagged above.

Figure 5. Notable demand for calls over puts   
![](images/af5f4b6a7ae24205491bfb65842cf0ae4d889a5cc54f0fe6ac716872f24f157a.jpg)

<details>
<summary>line</summary>

| Date   | SPX 1m Skew | Put/Call Ratio (RHS) |
|--------|-------------|----------------------|
| Jun/25 | 0.30        | 0.60                 |
| Aug/25 | 0.40        | 0.70                 |
| Oct/25 | 0.35        | 0.65                 |
| Dec/25 | 0.45        | 0.75                 |
| Feb/26 | 0.50        | 0.80                 |
| Apr/26 | 0.45        | 0.75                 |
| Jun/26 | 0.30        | 0.60                 |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: Citi, Bloomberg

Figure 6. Equities underperform in midterm years   
![](images/d4c3e7a2031e14a4a05b742083287f6412295267882f15160188b9fbe20a40a2.jpg)

<details>
<summary>line</summary>

| Month | 2026 | Median in midterm election years since 1978 (excl. 2026) | Median in all other years since 1978 |
|-------|------|----------------------------------------------------------|----------------------------------------|
| Jan   | ~1%  | ~0%                                                      | ~0%                                    |
| Feb   | ~2%  | ~-2%                                                     | ~2%                                    |
| Mar   | ~0%  | ~-4%                                                     | ~4%                                    |
| Apr   | ~-8% | ~-3%                                                     | ~3%                                    |
| May   | ~4%  | ~0%                                                      | ~5%                                    |
| Jun   | ~10% | ~2%                                                      | ~7%                                    |
| Jul   | ~10% | ~1%                                                      | ~8%                                    |
| Aug   | ~10% | ~1%                                                      | ~9%                                    |
| Sep   | ~10% | ~3%                                                      | ~10%                                   |
| Oct   | ~10% | ~5%                                                      | ~11%                                   |
| Nov   | ~10% | ~5%                                                      | ~12%                                   |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: Citi, Bloomberg

# What causes us to get outright tactically bearish

We reiterate the above factors suggest the distribution of outcomes for risk assets over the short-term has shifted to balanced/slightly bearish (compared to skewed positive over earnings). However, we still do not see an immediate trigger to suggest positioning for a correction; rather this simply suggests low vol should be opportunistically used for tactical downside protection.

What would it take to get outright bearish?

\- Discretionary underperformance: We like using the relative performance of consumer discretionary versus staples as an early indicator for equity deterioration (we use equal-weight to avoid distortions from any single names). This has been recovering, rather than declining (Figure 7). A correction lower would be negative for the broader index, in our view.

Figure 7. Discretionary underperformance versus staples (equal weight index) is negative for equities   
![](images/3171bbe48ade2ee17f5920917dd996c956b159c1abeaef0ee0d894f511aa0819.jpg)

<details>
<summary>line</summary>

| Date   | Equal Weight Consumer Discretionary to Staples Ratio | SPX Index (RHS) |
|--------|-----------------------------------------------------|-----------------|
| Jun/24 | 1.5                                                 | 5200            |
| Oct/24 | 1.6                                                 | 5700            |
| Feb/25 | 1.9                                                 | 6200            |
| Jun/25 | 1.8                                                 | 6700            |
| Oct/25 | 2.0                                                 | 7200            |
| Feb/26 | 1.8                                                 | 6700            |
| Jun/26 | 1.7                                                 | 7700            |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: Citi, Bloomberg

Figure 8. Front-end risk curves remain steep; flattening into inversion is risk-negative   
![](images/343fd5cea8fc86c36d1256fa69e973539f14034043b4dbaae1b434dbb8dd6afe.jpg)

<details>
<summary>line</summary>

| Date   | UX1 - UX3 (inverted) | SPX Index (RHS) |
|--------|----------------------|-----------------|
| Jun/24 | -2                   | 5000            |
| Oct/24 | -1                   | 5500            |
| Feb/25 | -3                   | 6000            |
| Jun/25 | -1                   | 6500            |
| Oct/25 | -2                   | 7000            |
| Feb/26 | -1                   | 7500            |
| Jun/26 | -3                   | 7500            |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: Citi, Bloomberg

- Vol curve flattening/vol of vol outperforming: We look at the shape of the front-end of the VIX curve, with quick flattening into inversion as an early/ coincidental signal (Figure 8). We do the same with the ratio of vol of vol (VVIX) to the VIX, which can often start to move higher ahead of market corrections (Figure 9). Neither shows negative indications yet.   
- Negative technicals: We respect price, and for now the trend higher in risk assets remains intact. There is some mild momentum divergence developing on the daily S&P 500 chart, but it is neither confirmed nor is one indicator enough to lead us to fight the trend (Figure 10). A close below the 21dma (7,460) may be the first signal for caution.

Figure 9. The ratio of VVIX to VIX typically falls ahead of equities (currently pushing higher)   
![](images/e6608091b332e7b0bffbd6ba7a38a3b33ff8a52330924e89cae77bf698aa40bc.jpg)

<details>
<summary>line</summary>

| Date   | VVIX/VIX Ratio | SPX Index (RHS) |
|--------|----------------|-----------------|
| Jun/24 | 6.5            | 4.0             |
| Oct/24 | 7.0            | 4.5             |
| Feb/25 | 5.5            | 5.0             |
| Jun/25 | 3.5            | 5.5             |
| Oct/25 | 6.0            | 6.0             |
| Feb/26 | 5.0            | 6.5             |
| Jun/26 | 5.5            | 7.0             |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: Citi, Bloomberg

Figure 10. S&P 500 trend higher remains intact; mild momentum divergence hints at correction risk   
![](images/c81d78366ed15a0eae169b062c7c3b62c1751917fc7999dc4a543a2b77cc6a3f.jpg)

<details>
<summary>line</summary>

| Date       | SPX Index Value | SMAVG (21) on Close | Slow K(9,3) | Slow K(8,0)(3) |
|------------|-----------------|---------------------|-------------|----------------|
| Jun 2024   | ~5500           | ~5500               | ~60         | ~60            |
| Sep 2024   | ~6000           | ~6000               | ~70         | ~70            |
| Dec 2024   | ~6500           | ~6500               | ~80         | ~80            |
| Mar 2025   | ~7000           | ~7000               | ~90         | ~90            |
| Jun 2025   | ~7500           | ~7500               | ~100        | ~100           |
| Sep 2025   | ~7800           | ~7800               | ~110        | ~110           |
| Dec 2025   | ~7900           | ~7900               | ~120        | ~120           |
| Mar 2026   | ~8000           | ~8000               | ~130        | ~130           |
| Jun 2026   | 7011.14844      | 7439.62014          | 91.7936     | 85.5996        |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: Citi, Bloomberg

- Strait closure exacerbates/yields surge: Markets are optimistic on the prospects of a deal that re-opens the Strait of Hormuz, with progress seemingly being made towards a deal. Should market expectations shift to a long closure, commodity prices could spike up again alongside yields, weighing on risk assets more broadly.   
- Price reaction to news diverges: There has been asymmetrical price reaction to news around the Iran conflict, with good news seeing larger price reactions than bad news as the market leans towards the “de-escalation trade.” However, markets typically price in such events ahead of the outcome itself, with the actual event then seeing little follow-through (the market cliché of “buy the rumor, sell the news”).

A similar dynamic was seen over COVID, when market enthusiasm around vaccines and re-opening was rapidly priced into markets before the first vaccine was administered. Markets topped out soon after the vaccine rollout began as the market pivoted focus to upcoming central bank hikes in light of rapidly rising inflation (Figure 11).

The market has been anticipating an Iran deal, with much of the good news potentially priced-in. This creates risk of a “sell the rumor” dynamic once/if a resolution is confirmed. A negative sign for markets would be if the rally is short-lived and quickly reverses after such a

[中间内容因长度限制已省略]

lar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
