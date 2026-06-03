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


# Matthew Hornbach


# Aryaman Singh


# Eli P Carter


2026 EXTEL


May 26 – June, 12 2026

VIEW OUR ANALYSTS >

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

# Interest Rate Derivative Strategy

# United States | Skew: A robust signal in a changing market

MS & CO. LLC


Matthew Hornbach, CMT


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

[[KC_IMAGE_001]]

Source: Bloomberg, S&P, MS

# Compare LIBOR and SOFR era

The LIBOR-SOFR transition provides a convenient division of the sample into two distinct macro environments. The LIBOR era (2009 to mid-2019) was characterized by persistently low rates and subdued volatility, while the SOFR era (mid-2019 to today) encompassed the pandemic shock, inflation surge, subsequent policy tightening cycle, and the current Iran conflict.

The comparison shows that the deterioration of the 63-day lookback is largely a post-2019 phenomenon (Exhibit 2 and Exhibit 3). During the LIBOR era, it performed similarly to shorter lookbacks. During the SOFR era, performance weakened materially while shorter specifications remained more resilient.


[[KC_IMAGE_002]]

Source: Bloomberg, S&P, MS

Exhibit 3: 10y tail results from 2019 - today

[[KC_IMAGE_003]]


Source: Bloomberg, S&P, MS

# Signal decay

The original note focused on strategies with a one-day trading delay, whereby positions are established on $(t+1)$ and held through $(t+2)$ based on signals observed at $(t)$ .

Here, we extend the framework to consider longer trading delays. Strategies with longer holding periods can be replicated as linear combinations of portfolios formed using different trading delays, enabling us to characterize the evolution of signal alpha over time.

Examining performance across different trading delays provides insight into how quickly the information embedded in skew is incorporated into rates. Exhibit 4 and Exhibit 5 show the historical total return of strategies based on 3m10y skews.


Most strategy specifications experienced a drawdown between July 2021 and July 2023. Short-delay strategies eventually recovered from the drawdown, while longer-delay strategies did not.

Exhibit 4: Historical return over the LIBOR era

[[KC_IMAGE_004]]


Source: Bloomberg, S&P, MS

Exhibit 5: Historical return over the SOFR era

[[KC_IMAGE_005]]


Source: Bloomberg, S&P, MS

# A closer look at 2021 to 2023

The period from 2021 to 2023 represents the most significant underperformance episode for the skew signal and provides useful insight into its limitations.

The first challenge was that skew repriced early in the selloff. As investors adjusted to higher inflation, payer skew richened sharply and reached historically elevated levels by early 2021. Rates then sold off by another 300bp over the next two years, but skew did not continue to richen at the same pace because much of the bearish outlook had already been priced in. As a result, the signal could no longer benefit from the broader directional move in rates and instead relied on correctly identifying shorter-term fluctuations. This made performance more sensitive to the choice of lookback window.

A second challenge was the high level of implied volatility. By 2022, both implied volatility and payer skew were already elevated. This left little room for further skew richening, even as rates continued to sell off. Once 3m10y implied volatility rose above roughly 100bp/year, skew became less responsive to additional moves in rates.

Taken together, these observations suggest that the signal was most effective during the initial repricing phase. Once skew and implied volatility reached elevated levels, further rate sell-offs generated little additional skew richening, reducing the signal's predictive power.

Exhibit 6: 3m10y skew and 10y rates

[[KC_IMAGE_006]]


Source: Bloomberg. MS

Exhibit 7: 3m10y skew and 3m10y implied vol

[[KC_IMAGE_007]]


Source: Bloomberg. MS

# Extending the analysis to all parts of the curve

The performance deterioration since 2019 has been most pronounced in the 2y tail, while the 30y tail is the only part of the curve that saw an improvement. One interpretation is that front-end rates have become increasingly driven by macro and policy shocks, reducing the impact of positioning signals. Long-end rates, by contrast, appear to remain more influenced by investor flows, allowing skew to retain (or even improve) its predictive power.

The 63-day lookback underperformed across nearly all tails, while 21-day lookback delivered more consistent results.

Together, these findings suggest that the post-2019 environment has increased the value of speed. Signals that adapt quickly to changes in positioning continue to perform well, while those relying on older information have become less effective.


[[KC_IMAGE_008]]


Source: Bloomberg. S&P. MS.

Exhibit 9: 2y tail results from 2019 - today

[[KC_IMAGE_009]]


Source: Bloomberg. S&P. MS.


[[KC_IMAGE_010]]

Source: Bloomberg. S&P. MS

Exhibit 11: 5y tail results from 2019 - today

[[KC_IMAGE_011]]


Source: Bloomberg. S&P. MS


[[KC_IMAGE_012]]


Source: Bloomberg. S&P. MS

Exhibit 13: 30y tail results from 2019 - today

[[KC_IMAGE_013]]


Source: Bloomberg. S&P. MS

# Conclusion

The skew signal remains robust across a wide range of model parameter choices, suggesting it captures a genuine feature of market behavior rather than a sample-specific artifact.

Since 2019, markets have experienced more frequent shocks and regime shifts. As a result, signals with 63-day lookback have underperformed. The signal has also become less relevant at the front end, where macro shocks increasingly dominate rate moves, while retaining predictive power in longer-dated tails.

The 21-day change in 3m skew remains a reasonable baseline, but the appropriate implementation should depend on market regime rather than historical optimization.

# Skew Signal Monitor

Skew signals continue to indicate near 100% short duration exposure across the curve. Despite the recent retracement in rates, payer skew remains well supported.

Exhibit 14: Exposure across the curve based on skew signal

[[KC_IMAGE_014]]


Source: Bloomberg, MS

Exhibit 15: Total return of strategies based on skew signal over the past year

[[KC_IMAGE_015]]


Source: Bloomberg, MS

# SDR Monitor

While dealers' peak net gamma position has stabilized near \$0.7mm in recent sessions, their gamma exposure at current spot levels has turned net short. Spot gamma exposure is now at its lowest level of the past year. In the long end, this pattern suggests customers have been net buyers of short-dated ATM options while continuing to sell lower-strike receivers. Together, these flows have left dealers increasingly short gamma around prevailing market levels.

Exhibit 16: Dealers' gamma exposure profile

[[KC_IMAGE_016]]


Source: DTCC, MS

Exhibit 17: Historical peak gamma exposure

[[KC_IMAGE_017]]


Source: DTCC, MS

# Callable Issuance Monitor

Issuance in May was modestly higher than in April but remained below the elevated levels seen in 1Q. June is typically a seasonally slow month for callable issuance. If realized, lower issuance could provide support to the intermediate sector of the volatility surface.

Exhibit 18: Notional of callable bond issuance

[[KC_IMAGE_018]]


Source: Bloomberg, MS

Exhibit 19: Vega supply from callable issuance

[[KC_IMAGE_019]]


Source: Bloomberg, MS

• Trade idea: Maintain long 2y10y straddle vs. short 6m10y straddle
• Trade idea: Maintain long 1y1y F/F+25/F+50 payer ladder

# Valuation Methodology and Risks

Below you will find a list of our current trade ideas, entry levels, entry dates, rationales, and risks.
