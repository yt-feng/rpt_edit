你是资深小红书内容策划 + 投研翻译官，擅长把英文/中文研报改写成高互动、可收藏、可转发的中文小红书笔记。

【目标】
- 把下面的研报解析内容，改写成一篇中文小红书笔记。
- 风格：投研博主风：信息密度高，但像给朋友讲逻辑
- 长度：不超过 1000 字，信息密度高但不要写长文。
- emoji 密度：中

【必须输出的结构】
1. 第一行：标题，20 字以内，不要像论文标题，也不要用夸张极限词。
2. 第二行：封面短标题，10 字以内，适合放在图中间。
3. 第三行：封面副标题，10-18 字，短句。
4. 正文分段清晰，每段不超过 3 行，可以用编号、小标题或加粗。
5. 正文要自然呈现观点，但不要暴露写作框架或思考过程。
6. 末尾可以保留 2-4 个相关标签，只允许从这些标签里选择：`#学习笔记`、`#研究笔记`、`#学习研究`、`#研报解读`。

【严禁输出】
- 不要出现这些栏目名或类似栏目名：`一句话结论`、`我最想提醒的一点`、`配图建议`、`免责声明`、`非投资建议`、`仅做学习交流`、`仅作学习交流`。
- 不要在正文最后追加配图建议，不要告诉我第 2/3/4 张图怎么配文。
- 不要输出任何包含“投资”的免责声明，也不要输出“非投资建议”这种表述。
- 不要输出财经敏感标签：`#投资学习`、`#财经`、`#金融`、`#股票`、`#基金`、`#理财`。
- 不要输出无关标签：`#小红书笔记`、`#笔记分享`、`#干货分享`。
- 不要写“关注”“点赞”“求关注”“评论区见”“评论区留言”等直接互动诱导；可以写“欢迎一起讨论”“可以继续交流”。

【平台发布合规要求】
- 不要写“爆款”“震惊”“必看”“必读”“最强”“最全”“唯一”“全网首发”等极限词或夸张词。
- 不要写“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要放在中性语境里。
- 不要承诺收益，不要引导交易，不要暗示确定性结果。

【内容要求】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 可以把专业表达翻成人话，但不能扭曲意思。
- 遇到不确定或缺失信息：用“研报未给出”或“这里是推测”明确标注。
- 默认避免出现具体投行品牌名，比如“高盛”“Goldman Sachs”，统一写作“某外资投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【推荐写法】
- 开头直接给一个自然判断，不要加“结论：”标签。
- 中间用 1/2/3 拆逻辑，但小标题要像正常内容标题，不要像写作模板。
- 结尾可以留下一个自然讨论问题，但不要引导关注、点赞或评论。
- 最后一行输出 2-4 个标签，优先：`#学习笔记 #研究笔记 #学习研究 #研报解读`。

【研报解析内容】
"""
# Repo Rate Dynamics

# The Role of Dealers, Hedge Funds, and Issuance

Prepared by Kleopatra Nikolaou

WP/26/145

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

2026
JUL

![](images/f9ca219e01d76b598be8fd18028e79f5b3629e3d01c8728085c9c0e0554aeeed.jpg)

IMF Working Paper
Monetary and Capital Markets

Repo Rate Dynamics: The Role of Dealers, Hedge Funds, and Issuance Prepared by Kleopatra Nikolaou

Authorized for distribution by Jason Wu
July 2026

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

ABSTRACT: This paper analyses U.S. secured repo spreads by jointly looking into reserves, dealer balance-sheet usage, hedge fund leverage, and Treasury issuance. Using a quantile regression framework, the results show that repo market dynamics are strongly state-dependent. Higher level of reserves consistently compress repo spreads to the Federal Reserve's overnight reverse repo offering rate and remain the primary stabilizing force, particularly in tighter funding conditions. Hedge fund activity appears to amplify dealer balance-sheet pressures in lower quantiles, reflecting the impact of leveraged demand in normal markets. As spreads rise, this effect weakens. Instead, heavier Treasury issuance appears to weigh on repo spreads via its stronger effect on dealer balance sheet pressures. Overall, U.S. repo spreads are affected by the supply of central bank liquidity, demand for leverage, Treasury issuance and intermediary capacity. Crucially, these drivers are not equally relevant across the distribution of funding conditions.

RECOMMENDED CITATION: Nikolaou, Kleopatra. 2026. JUL. IMF Working Paper. International Monetary Fund.

JEL Classification Numbers:

G12, G23, E43, E58

Keywords:

Repo, Hedge Funds, Treasury issuance, Broker-dealers, Reserve Demand

Author's E-Mail Address:

KNikolaou@imf.org

WORKING PAPERS

# Repo Rate Dynamics:

The Role of Dealers, Hedge Funds, and Issuance

Prepared by Kleopatra Nikolaou\*

## Contents

Glossary....4   
Executive Summary....5   
Introduction....6   
Relation to Literature....9   
Empirical Methodology....11 Baseline Specification: Reserves and Dealer Balance Sheet Usage....11 Endogeneity in Dealer Balance Sheets and Repo Spreads....11 How Dealer Balance Sheet Pressure is Amplified by Hedge Funds....12 How Treasury Issuance Pressure is Amplified by Dealer Balance Sheets....13   
Results....15 Baseline Specification: Reserves and Dealer Balance Sheet Usage....15 Figure 1: Spreads Are Largely Driven by Reserve Dynamics and Dealer Balance Sheet Usage....16 Amplification Effect from Hedge Funds....16 Figure 2: Hedge Funds Amplify Impact on Repo Spreads in "Normal" Times....18 Amplification Effect from Issuance....19 Figure 3: Issuance Amplifies Impact on Repo Spreads When Funding Conditions Tighten....20   
Conclusion....21   
Annex....22 Figure 4: As Funding Conditions Tighten, Issuance Affects Repo Rates Via the Balance Sheet Channel ....Error! Bookmark not defined. Tables: Quantile Regression Results....27   
References....29

## Glossary

DP......Dealer Balance Sheet Usage
HF......Hedge Fund
RRP......Reverse Repurchase Facility
SOFR......Secured Overnight Financing Rate
MOVE......Merrill Lynch Option Volatility Estimate (Treasury volatility index)
VIX......CBOE Volatility Index (equity market volatility)
Repo......Repurchase Agreement

## Executive Summary

This paper examines the dynamics of U.S. repo market spreads by jointly analyzing the roles of reserves, dealer balance-sheet usage, hedge fund activity, and Treasury issuance. Using a quantile regression framework, the analysis shows that the forces shaping repo rates differ across funding conditions.

Three main conclusions emerge. First, reserve balances remain the primary stabilizing force in U.S. repo markets. Higher reserves consistently compress repo spreads, and their effect becomes particularly important when funding conditions tighten. This result highlights the continued importance of adequate liquidity buffers in floor-type monetary policy frameworks.

Second, hedge fund activity appears to affect U.S. repo markets also through its impact on dealer balance-sheet pressures. In periods of relatively benign funding conditions, growing leveraged hedge fund demand, such as basis trades, can exert pressure on dealer balance sheets and contribute to rising repo spreads. As funding conditions tighten, however, hedge funds tend to reduce positions, and their influence on repo spreads appear to be declining.

Third, Treasury issuance can become a more important driver of U.S. repo spreads in tighter funding environments. While issuance exerts a modest direct effect on repo spreads, its interaction with dealer balance-sheet usage can become significantly stronger as repo spreads rise. This result suggests that supply-driven inventory pressures on dealers may play an increasingly important role during periods of market stress.

Overall, the results of this paper indicate that repo market outcomes reflect the interaction between liquidity supply, leveraged demand, and intermediation capacity. While reserves provide the main buffer against funding pressures, both hedge fund leverage and Treasury issuance can amplify repo market strains through their impact on dealer balance sheets.

## Introduction

Repurchase agreement (repo) markets are a cornerstone of modern financial systems. They provide the primary mechanism through which government securities are financed and redistributed, support the liquidity of government bond markets and serve as the channel through which monetary policy rates are transmitted to short-term funding markets more broadly. The U.S. repo market alone exceeds \$12 trillion in daily outstanding volume, with dealers at its center, simultaneously sourcing cash from lenders and channeling it to borrowers (Hempel et al., 2025).

In recent years, repo markets have experienced significant structural shifts. Rapid growth in U.S. Treasury issuance has expanded the volume of collateral that must be financed and intermediated through repo markets. Yet the capacity of primary dealers to warehouse and redistribute that supply has not kept pace (Adrian, et al., 2025). At the same time, the composition of Treasury market participants has shifted markedly. Hedge funds have increasingly absorbed the growing supply of Treasuries through leveraged relative-value trades, most prominently the Treasury cash-futures basis trade, which relies heavily on repo borrowing (Barth and Kahn 2021, 2025; FSB 2026). While academic and policy literature has examined the implications of higher issuance and hedge fund activity for Treasury yields and term premia, there is comparatively limited empirical evidence on their impact on short-term funding markets, particularly repo rates.

Existing research on repo rate dynamics has largely focused on the role of bank reserves as the primary determinant of short-term funding conditions. In frameworks developed after the Global Financial Crisis, fluctuations in aggregate reserves are often viewed as the key driver of repo rate movements relative to policy rates (Afonso et al., 2025). While reserves undoubtedly play a key role in shaping funding conditions a separate strand of research suggests that repo rates may also reflect shifts in collateral supply, leveraged demand for financing, and the balance-sheet capacity of intermediaries (see for example Cordes and Infante, 2025; Barth and Kahn, 2025). This paper aims to bridge these approaches by jointly examining reserves, Treasury issuance, hedge fund activity, and dealer balance-sheet capacity within a unified empirical framework, allowing their relative importance to vary across funding conditions.

A key element in this mechanism is the role of dealers as the central intermediaries of repo markets. Primary dealers stand between cash lenders and borrowers in repo markets, expanding their balance sheets to finance Treasury securities and support market liquidity. Because these intermediation activities require balance-sheet capacity, the ability of dealers to absorb shifts in funding demand or collateral supply is inherently limited. Changes in repo market conditions stemming from increased Issuance or demand for leveraged trades financed by repo may therefore reflect fluctuations in dealer balance sheet usage, which can impact the cost of repo intermediation (Chabot et al., 2024; Besugo et al., 2025).

Using the overnight repo spread as a measure of funding conditions, I investigate the joint roles of central bank reserves, dealer balance sheet utilization, hedge fund activity, and Treasury issuance in shaping that spread. A key premise is that these drivers are not equally relevant across the distribution of funding conditions. For example, the build-up of leveraged positions is highly procyclical, increasing when funding rates are low (IMF, 2025; Barth and Kahn, 2025), while the impact of Treasury issuance may be more pronounced when dealer balance sheets are already under pressure. I test this heterogeneity in impact using quantile regressions, which characterize the full conditional distribution of the spread rather than its conditional mean, allowing the impact of repo market drivers to vary across funding regimes.

The methodology and results of this paper contribute to the literature in three ways. The first contribution is to provide a joint empirical characterization of repo rate dynamics that integrates the two key drivers identified in the literature, bank reserves and dealer balance-sheet capacity, while also accounting for the role of hedge fund activity and Treasury issuance within a unified quantile regression framework. Existing studies have examined these forces quasi in isolation. The reserve demand literature documents a non-linear relationship between reserves and short-term rate spreads, but the analysis focuses on federal fund spread, instead of repo spreads and typically abstracts from the role of non-bank intermediaries (Langowski, 2023; Lopez-Salido and Vissing-Jorgensen, 2025; Afonso et al., 2025). $^{1}$ The dealer intermediation literature explains the link between intermediary balance sheet and strains in market conditions, including repo rates, but typically abstracts from integrating the role of issuance and hedge funds. $^{2}$ A related strand examining the Treasury basis trade highlights the importance of hedge fund repo borrowing in basis trade volumes, and documents that, in normal times, higher basis trade volumes can be associated with higher repo spreads. (Barth and Kahn, 2021, 2025; Barth, Kahn, and Mann, 2023). However, the role of reserves and, in some cases issuance, does not feature prominently. Finally, the Treasury supply literature documents how issuance affects dealer inventories and market intermediation, but sheds limited light on how the resulting intermediation pressures affect funding markets (Fleming, Nguyen, and Rosenberg, 2024; Adrian, Fleming, and Nikolaou, 2025). This paper brings these strands together in a single empirical framework that allows these forces to interact and vary across funding conditions.

The second contribution is to document a novel, state-dependent mechanism that determines repo spreads. The baseline results confirm the key role of reserves. Higher reserves are associated with lower repo spreads, consistent with the non-linear reserve demand relationship documented in the reserve literature. The stabilizing effect of reserves becomes particularly strong in the upper part of the conditional spread distribution, suggesting that reserve balances are especially effective in containing repo market pressures when funding conditions are already strained. This result aligns with the impact on repo spreads from a scarce-to-ample reserve transition, emphasized in the reserve demand literature.

Results on the impact of growing dealer balance sheet usage on repo spreads, however, demonstrate a U-shaped pattern across spread quantiles. Greater balance sheet usage appears to put upward pressure on repo rates at both low and high quantiles, while compressing spreads in the middle of the distribution. The higher-quantile pattern is consistent with evidence that dealer intermediation can become constrained precisely when it is needed most (Duffie et al., 2023; Adrian et al., 2025), but the analysis further explains the U-shape through amplification channels tied to Treasury supply and hedge-fund demand. Increased Treasury issuance can amplify dealer balance sheet pressure on spreads in higher quantiles, consistent with the narrative that additional collateral supply strains dealer intermediation capacity. Conversely, stronger hedge fund demand for repo –measured by hedge fund short positions in Treasury futures– can put upward pressure on repo rates in lower quantiles, consistent with dealers charging more for balance-sheet space when basis-trade activity is strong (Kashyap et al., 2025; Barth and Kahn, 2025; IMF, 2025). By contrast, in the middle of the distribution, dealer balance-sheet expansion is associated with lower spreads, suggesting that dealers appear to step in as liquidity providers and smooth supply-demand imbalances.

Framing it differently, in more benign funding conditions, when repo spreads are low, hedge fund borrowing demand can place upward pressure on repo spreads primarily through increased dealer balance sheet usage. As funding conditions tighten, the dynamics shift. Treasury issuance appears to become a more important driver of spreads likely because it increases the volume of securities that must be financed and temporarily warehoused by dealers, which can amplify pressures on intermediary balance sheets. Across funding regimes, reserves appear to emerge as the primary stabilizing force: higher reserve balances compress repo spreads, and their effect becomes particularly strong when funding conditions deteriorate.

The empirical findings are supported by a range of robustness checks designed to mitigate potential concerns related to endogeneity, variable construction and sample selection. Nevertheless, the workhorse specifications in the paper remains reduced-form and therefore the results ultimately describe conditional relationships rather than structural causal effects, a limitation shared with the broader empirical literature on dealer intermediation capacity.

The third contribution speaks directly to the policy debate on the calibration of ample-reserves operating frameworks. A key realization for central banks normalizing their balance sheets is that the “optimal” reserve level, the level at which repo markets transition from stable conditions to a regime where funding rate volatility becomes persistent, is time varying (Lopez-Salido and Vissing-Jorgensen 2025; Bailey 2024). The results in this paper provide additional evidence on this transition. Consistent with the reserve demand literature, reserves emerge as the dominant determinant of repo spreads. At the same time, the analysis shows that repo market outcomes also reflect pressures from dealer balance sheet usage, leveraged hedge fund demand, and Treasury issuance. Importantly, the stabilizing effect of reserves becomes stronger as funding conditions tighten, indicating that reserve balances play a critical role in offsetting these market pressures when intermediation capacity becomes strained. In this sense, the “optimal” level of reserves depends not only on aggregate liquidity but also on the structure of repo intermediation and the scale of leveraged activity in Treasury markets.

The remainder of the paper is organized as follows. Section 2 reviews the related literature. Section 3 presents the empirical methodology, including the baseline quantile regression specification and extensions incorporating hedge fund activity and Treasury issuance. Section 4 reports and discusses the main results, with particular attention to the state-dependent transmission mechanism. Section 5 concludes with a summary of the results.

## Relation to Literature

This paper brings together several strands of literature.

A core strand of the literature examines the demand for reserves and its implications for short-term rate dynamics, a central issue for monetary policy implementation. Since the Global Financial Crisis, however, the operating framework has shifted from corridor to floor-type systems, placing the quantity and distribution of bank reserves (scarce vs ample) at the center of rate determination (Langowski, 2023). In such regimes, overnight rates remain well anchored when reserves are abundant but can deviate sharply as reserves approach a scarcity threshold (Afonso et al., 2025; Cordes and Infante, 2025). As a result, the reserve-rate relationship is st

[中间内容因长度限制已省略]

iables are standardized. \*\*\* p<0.01, \*\* p<0.05, \* p<0.1.

## References

Adrian, Tobias, and Hyun Song Shin. 2014. "Procyclical Leverage and Endogenous Financial Stability." Journal of Political Economy 122 (2): 373–415.

Adrian, Tobias, Michael Fleming, and Kleopatra Nikolaou. 2025. "US Treasury Market Functioning from the GFC to the Pandemic." Annual Review of Financial Economics, Vol. 17:49-76.

Afonso, Gara, Domenico Giannone, Gabriele La Spada, and John C. Williams. 2025. "Scarce, Abundant, or Ample? A Time-Varying Model of the Reserve Demand Curve." Federal Reserve Bank of New York Staff Report No. 1019.

Bailey, Andrew. 2024. "The Importance of Central Bank Reserves." Speech delivered at the London School of Economics, London, October 2024. Bank of England.

Barth, Daniel, and R. Jay Kahn. 2021. "Hedge Funds and the Treasury Cash-Futures Disconnect." OFR Working Paper No. 21-01. Washington, DC: Office of Financial Research.

Barth, Daniel, and R. Jay Kahn. 2025. "Hedge Funds and the Treasury Cash-Futures Basis Trade." Journal of Monetary Economics 155: 103823., https://doi.org/10.1016/j.jmoneco.2025.103823.

Barth, Daniel, R. Jay Kahn, and Robert Mann (2023). "Recent Developments in Hedge Funds' Treasury Futures and Repo Positions: is the Basis Trade "Back"?," FEDS Notes. Washington: Board of Governors of the Federal Reserve System, August 30, 2023, https://doi.org/10.17016/2380-7172.3355.

Besugo, Rita, Benoit Nguyen, Andrea Poinelli, and Martin Scheicher. 2025. "Dealers' Costs of Intermediation in Fixed Income Markets: Empirical Results for the Euro Area." SUERF Policy Brief No. 1226. Frankfurt: European Central Bank.

Chabot, Marianne, Sebastian Infante, James Orr, and Zack Saravay. 2024. "Dealer Balance Sheet Constraints: Evidence from Dealer-Level Data across Repo Market Segments." FEDS Notes. Washington, DC: Board of Governors of the Federal Reserve System.

Cochran, Paul, Sebastian Infante, Lubomir Petrasek, Zack Saravay, and Mary Tian. 2023. "Dealers' Treasury Market Intermediation and the Supplementary Leverage Ratio." Finance and Economics Discussion Series 2023. Washington, DC: Board of Governors of the Federal Reserve System.

Copeland, Adam, Darrell Duffie, and Yilin Yang. 2025. "Reserves Were Not So Ample After All." Quarterly Journal of Economics, Volume 140, Issue 1, February 2025, Pages 239–281, https://doi.org/10.1093/qje/qjae034

Cordes, Lucy, and Sebastian Infante. 2025. 'Repo Rate Sensitivity to Treasury Issuance and Quantitative Tightening.' FEDS Notes, February 12. Washington, DC: Board of Governors of the Federal Reserve System. https://doi.org/10.17016/2380-7172.3707.

Du, Wenxin, Benjamin Hébert, Wenhao Li. (2023). "Intermediary Balance Sheets and the Treasury Yield Curve.", Journal of Financial Economics, Volume 150, Issue 3, 103722, ISSN 0304-405X, https://doi.org/10.1016/j.jfineco.2023.103722.

Duffie, Darrell, Michael Fleming, Frank Keane, Claire Nelson, Or Shachar, and Peter Van Tassel. 2023. "Dealer Capacity and U.S. Treasury Market Functionality." Federal Reserve Bank of New York Staff Report No. 1070. New York: Federal Reserve Bank of New York.

Favara, Giovanni and Infante, Sebastian and Rezende, Marcelo. 2025. Leverage Regulations and Treasury Market Participation: Evidence from Credit Line Drawdowns. Available at SSRN: https://ssrn.com/abstract=4175429 or http://dx.doi.org/10.2139/ssrn.4175429

Financial Stability Board (FSB). 2021. Lessons Learnt from the COVID-19 Pandemic from a Financial Stability Perspective. Basel: Financial Stability Board.

Financial Stability Board (FSB). 2026. Vulnerabilities in Government Bond-Backed Repo Markets. Basel: Financial Stability Board.

Fleming, Michael, Giang Nguyen, and Joshua Rosenberg. 2024. "How Do Treasury Dealers Manage Their Positions?" Journal of Financial Economics 158: 103885.

Hempel Samuel J., R. Jay Kahn, Robert Mann, and Mark E. Paddrik. 2024. "Repo Market Intermediation: Dealer Cash and Collateral Flow Management across the U.S. Repo Market". OFR Brief Series, November 14, 2024.

Sam Hempel, R. Jay Kahn, Julia Shephard (2025). "The \$12 Trillion US Repo Market: Evidence from a Novel Panel of Intermediaries," FEDS Notes. Washington: Board of Governors of the Federal Reserve System, July 11, 2025, https://doi.org/10.17016/2380-7172.3843.

International Monetary Fund. 2025. Global Financial Stability Report: Safeguarding Financial Stability amid High Uncertainty. Washington, DC: International Monetary Fund, October.

International Monetary Fund. 2026. Global Financial Stability Report. Washington, DC: International Monetary Fund, April.

Kashyap, Anil K., Jeremy C. Stein, Jonathan Wallen, and Joshua Younger. 2025. "Treasury Market Dysfunction and the Role of the Central Bank." Brookings Papers on Economic Activity, Spring.

Langowski, Philipp. 2023. "Reserve Demand, Quantitative Tightening, and the Fed Funds Rate." Job Market Paper.

Logan, Lorie. 2025. “The case for modernizing the FOMC’s operating target rate”. Speech available at https://www.dallasfed.org/news/speeches/logan/2025/Ikl250925

Lopez-Salido, David, and Annette Vissing-Jorgensen. 2025. "Reserve Demand and Quantitative Tightening." mimeo

![](images/ff613c79457e5eca81a905b765ca8e255aee411715ce2a5fe4cadc673db52b73.jpg)
"""
