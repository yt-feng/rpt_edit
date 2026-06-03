# Skew Is Not Noise: Why Options Market Positioning Still Predicts Rate Moves After 17 Years

Most market participants treat options skew as a second-order derivative—interesting for volatility traders but too noisy for directional rate calls. That assumption is wrong. After testing over 120 strategy specifications across two distinct macro eras, the evidence is clear: changes in short-expiry skew contain robust, tradeable information about subsequent rate moves. The signal has worked consistently since at least 2009, and its predictive power has actually strengthened in the long end of the curve precisely when many investors abandoned it.

The conventional wisdom holds that macro shocks have overwhelmed all positioning-based signals in recent years. The data tells a more nuanced story. Since 2019, skew's predictive power did deteriorate in the 2-year sector, where front-end rates became dominated by policy shocks and inflation surprises. But in the 30-year tail, the signal improved meaningfully. This divergence is not random—it reveals something fundamental about how different parts of the curve absorb information.

The key lesson from the post-2019 period is not that skew stopped working. It is that markets began changing faster. The signal's robustness depends on the speed at which you measure it, and the optimal lookback window has shifted. Slower-moving specifications that performed well during the low-volatility LIBOR era now underperform, while faster signals have proven resilient through the pandemic, the inflation surge, the tightening cycle, and the current geopolitical environment.

This matters now because the signal continues to point decisively to short duration across the curve. Skew has richened further despite already elevated starting levels. For investors trying to navigate a market where consensus views have become crowded, understanding what skew is actually saying—and when to trust it—has become a critical edge.


![Report chart 1](assets/source_image_01.jpg)

## The Signal Survives Every Reasonable Specification Change, Proving It Reflects Real Market Structure

The most common objection to any quantitative signal is data mining. If you test enough parameter combinations, something will appear significant by chance. The analysis here addresses that concern directly by testing 120 distinct specifications—four lookback windows, three option expiries, and ten trading delays—and finding that the relationship holds across virtually all of them.

The results are broadly unchanged whether duration exposure is expressed through swaps or Treasury futures. Skew signals derived from 1-month, 3-month, and 6-month expiries produce comparable performance. This consistency rules out the possibility that the signal is an artifact of a specific instrument or a particular point on the skew surface. What skew captures is broader: the collective positioning of investors who use options to express views on rate direction.

The 21-day lookback window emerges as the most consistent performer across regimes. Shorter lookbacks can achieve similar Sharpe ratios but introduce more noise and larger drawdowns. The 63-day lookback generally underperforms, particularly after 2019. This pattern tells us that the information in skew decays relatively quickly—it is not a slow-moving structural indicator but a signal that reflects positioning dynamics with a horizon of several weeks.

Crucially, the signal retains predictive power even when trades are delayed by several days after the skew move is observed. Performance declines as delays increase, but the relationship remains positive for up to ten trading days. This gradual decay suggests that the information embedded in skew is incorporated into rates incrementally, not instantaneously. For active managers, this creates a meaningful window to act.


![Report chart 2](assets/source_image_02.jpg)

## The Post-2019 Regime Shift Rewarded Faster Signals and Revealed a Structural Divergence Across the Curve

The LIBOR-SOFR transition provides a natural dividing line between two fundamentally different macro environments. From 2009 to mid-2019, rates were persistently low, volatility was subdued, and the skew signal worked well across all lookback windows. The 63-day lookback performed similarly to shorter specifications. The signal was robust but also patient—it did not punish slower implementation.

After 2019, everything changed. The pandemic, the inflation surge, the most aggressive tightening cycle in decades, and now geopolitical shocks have compressed the time horizon over which positioning information remains relevant. The 63-day lookback deteriorated materially. Shorter lookbacks remained more resilient, though they too experienced a significant drawdown from July 2021 to July 2023.

This is where the curve divergence becomes analytically important. In the 2-year sector, skew's predictive power weakened substantially. Front-end rates became dominated by macro and policy shocks—Fed decisions, inflation data, employment reports—that overwhelmed whatever information was embedded in options positioning. The signal was not wrong; it was simply competing with forces of a different magnitude.

In the 30-year tail, the opposite occurred. Predictive power improved. Why? Because long-end rates remain more sensitive to positioning dynamics. When macro shocks hit, they affect the entire curve, but the long end has additional layers of complexity—term premium dynamics, foreign demand, pension fund hedging, and duration supply—that create persistent opportunities for positioning-based signals to add value.

The implication is strategic: investors should not treat the skew signal as a single input applied uniformly across the curve. It works differently in different sectors, and understanding where it works best is as important as understanding what it says.


![Report chart 3](assets/source_image_03.jpg)

## The 2021-2023 Drawdown Reveals the Signal's Limitations and Provides a Decision Framework for When to Override It

Every quantitative signal has failure modes, and the period from July 2021 to July 2023 represents the most significant underperformance episode for the skew signal. Understanding why it failed during this window is essential for knowing when to trust it and when to set it aside.

The first challenge was that skew repriced early in the selloff. As investors adjusted to higher inflation, payer skew richened rapidly. The signal correctly identified that positioning had shifted, but it did not capture the scale of the macro repricing that followed. When the Fed began its tightening cycle, rate moves were driven by policy expectations that overwhelmed the positioning signal.

The second challenge was that the relationship between skew and subsequent rate moves broke down during the most volatile periods. When markets are driven by surprise data releases or sudden policy shifts, the information in options positioning becomes stale almost immediately. The signal's gradual decay property—which is normally an advantage—becomes a liability.

The third challenge was the extended duration of the drawdown. Short-delay strategies eventually recovered, but longer-delay strategies did not. This tells us that the signal's recovery is not automatic; it depends on the speed of implementation.

For investors using this signal, the decision framework should be straightforward. The skew signal works best when: (1) macro volatility is moderate, not extreme; (2) positioning dynamics are the primary driver of rate moves, particularly in the long end; and (3) the lookback window is calibrated to the current market regime. The signal should be overridden or sized down when: (1) major policy surprises are imminent; (2) the signal has already richened to extreme levels without generating follow-through; or (3) the macro environment is experiencing structural breaks rather than cyclical adjustments.

## What the Report Does Not Fully Answer: The Interaction Between Skew and Other Positioning Signals

The analysis establishes that skew contains independent predictive power, but it does not fully explore how this signal interacts with other positioning indicators. This is a meaningful gap because no single signal operates in isolation.

Several open questions remain. Does skew provide information that is orthogonal to CFTC positioning data, or are they capturing the same underlying dynamics through different instruments? How does the skew signal correlate with dealer positioning and the flow of Treasury auctions? Does the signal work differently when the market is at extremes of positioning versus when positions are balanced?

The most important unanswered question is whether the skew signal's predictive power comes from informed trading or from mechanical hedging flows. If it is informed trading, then the signal reflects genuine information advantage and should persist. If it is mechanical—driven by delta hedging of large option positions—then the signal could break down if market structure changes. The report's robustness tests suggest the signal reflects something real, but the causal mechanism remains unclear.

Another area for further research is the signal's performance during periods of quantitative tightening and balance sheet reduction. The analysis covers the post-2019 period, which includes the Fed's balance sheet runoff, but does not isolate whether the signal works differently when the central bank is actively withdrawing liquidity.

## A Decision Framework for Incorporating Skew Into Rate Strategies

For investors who want to use this signal, the analysis supports a structured approach rather than a mechanical one. The signal is robust but not foolproof, and its effectiveness depends on how it is implemented.

First, calibrate the lookback window to the current regime. The 21-day lookback provides the best balance between responsiveness and stability across both the LIBOR and SOFR eras. In periods of elevated macro volatility, consider shortening the lookback further. In periods of low volatility, a longer lookback may reduce noise without sacrificing too much signal.

Second, differentiate by curve sector. The signal is weaker in the front end and stronger in the long end. For 2-year trades, the skew signal should be one input among many, with macro forecasts carrying more weight. For 30-year trades, the skew signal deserves higher conviction, particularly when positioning appears stretched.

Third, implement with a trading delay of no more than a few days. The signal decays gradually but meaningfully. Waiting more than five days after observing a skew move eliminates a significant portion of the alpha. The best risk-adjusted returns come from acting within one to three days.

Fourth, monitor for regime changes. The signal experienced a prolonged drawdown from 2021 to 2023. When the signal stops working, the appropriate response is not to abandon it but to ask whether the macro environment has shifted in a way that temporarily overrides positioning dynamics. The signal tends to recover when macro volatility subsides.

Fifth, use the signal's current reading as a starting point. Skew continues to point to short duration across the curve, and it has richened further despite already elevated levels. This suggests that positioning is not just bearish but increasingly one-sided. In such environments, the signal may be more reliable for timing than for direction—the question is not whether rates will move but when.

## The Unresolved Analytical Questions That Make the Full Report Worth Reading

The analysis presented here answers important questions about robustness and regime dependence, but it also raises deeper questions that only a full reading of the original report can address.

How exactly does the skew signal perform when broken down by specific macro regimes—not just LIBOR versus SOFR, but periods of rising rates, falling rates, quantitative easing, and quantitative tightening? The original charts provide this granularity, and the patterns are revealing.

What happens when you combine the skew signal with other quantitative inputs? The report focuses on skew in isolation, which is analytically clean but operationally incomplete. The full report contains the data that would allow investors to test multi-signal frameworks.

How does the signal perform in real time versus in-sample? The analysis covers 17 years of history, but the most important test is whether the signal has continued to work after the research was conducted. The original report addresses this through its most recent data points.

These are not minor details. They are the difference between knowing that a signal exists and knowing how to use it effectively. The full report provides the charts and data necessary to answer these questions.

Join the community to read the full report and review the original charts.

*This article is for learning and discussion only and does not constitute investment advice.*

<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>
