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
# Production Networks and the (Asymmetric) Transmission of Monetary Policy

Francesco Grigoli

WP/26/127

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

2026
JUN

![](images/e82a100ace3dc33a0b33496a4884ae5d20e2b53b3d45859ba8885ce81390f77f.jpg)

# IMF Working Paper Research Department

# Production Networks and the (Asymmetric) Transmission of Monetary Policy

Prepared by Francesco Grigoli\*

Authorized for distribution by Antonio Spilimbergo
June 2026

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

ABSTRACT: I study how the production network shapes monetary policy transmission to prices. Using U.S. data, I show that industries farther upstream from final demand exhibit larger cumulative price responses to monetary shocks, while downstream industries absorb shocks through output. A calibrated multi-sector New Keynesian model rationalizes these patterns: upstream sectors, which sell predominantly to other firms, reprice more frequently and therefore exhibit less price rigidity. A counterfactual decomposition of the price response shows that this heterogeneity in price rigidity---rather than cost-cascade propagation through input-output linkages---is the primary driver of the cross-sectional responses. The upstreamness differential is strongly asymmetric, large following expansionary shocks but nearly absent following contractionary ones, consistent with asymmetric price rigidity compounding across production stages. Together, these findings suggest that monetary policy's potency depends on the production network's architecture.

RECOMMENDED CITATION: Grigoli, Francesco “Production Networks and the (Asymmetric) Transmission of Monetary Policy” IMF Working Paper No. 26/127, June 2026

JEL Classification Numbers:

E31, E52, L14, C67

Keywords:

production networks; price rigidity; monetary policy transmission; input-output linkages; asymmetric price adjustment

Author's E-Mail Address:

francesco.grigoli@georgetown.edu

## 1 Introduction

Every dollar of GDP passes through an average of 2.1 intermediate transactions before reaching a final consumer. $^{1}$ This production network structure is a powerful propagation mechanism for real shocks, as idiosyncratic sectoral disturbances can cascade through input-output (IO) linkages and generate aggregate fluctuations (Acemoglu et al., 2012; Baqaee and Farhi, 2019; Carvalho and Tahbaz-Salehi, 2019). Whether production networks also shape the transmission of nominal shocks is far less understood. When the Federal Reserve changes the federal funds rate, the impulse must travel through the web of buyer-seller relationships, encountering a distinct pricing decision—and a distinct degree of nominal rigidity—at each node. Yet the workhorse New Keynesian model collapses this structure into a single representative firm facing a single Calvo friction; and, despite the evidence that prices adjust more readily upward than downward (Peltzman, 2000; Nakamura and Steinsson, 2008), it assumes symmetric price adjustment for rate hikes and cuts. This paper asks whether the architecture of the production network shapes the transmission of monetary policy to prices, and whether it does so differently for expansionary and contractionary shocks.

I develop a multi-sector New Keynesian model in which industries are connected through an IO network and each faces Calvo-style nominal rigidity. The key theoretical result is that aggregate monetary non-neutrality depends on a network-weighted rigidity index rather than the simple average of sectoral price stickiness. As a result, two economies with identical average price rigidity but different production structures will exhibit different degrees of monetary non-neutrality. $^{2}$ The model delivers a sharp cross-sectional prediction: more upstream industries—those farther from final demand, as measured by the upstreamness index of Antràs et al. (2012)—should exhibit larger cumulative price responses to monetary shocks. This is because upstream producers sell predominantly to other firms rather than to consumers, and business-to-business prices are renegotiated more frequently than consumer-facing prices (Nakamura and Steinsson, 2008). Network position thus generates a systematic correlation between upstreamness and intrinsic price rigidity, with more upstream sectors having lower Calvo parameters. $^{3}$

I test that more upstream industries exhibit larger cumulative price responses to monetary shocks using a panel of monthly producer price indices for 271 U.S. industries at the six-digit NAICS level and the orthogonalized high-frequency monetary policy surprises of Bauer and Swanson (2023). Local projections of cumulative industry price changes on the interaction of the monetary shocks with upstreamness reveal that the differential price response per unit of upstreamness is statistically and economically significant starting from one year after the shock up to over two years after the shock, peaking one year and a half after the shock. The empirical results imply that an industry at the 75th percentile of upstreamness exhibits a peak cumulative price response 2.8 percentage points larger than one at the 25th percentile, in response to a one percentage point monetary policy shock. Feeding the Bureau of Economic Analysis (BEA) IO matrix into the model with an externally measured rigidity differential—calibrated from industry-level PPI price adjustment frequencies—generates the correct qualitative pattern of interaction coefficients across horizons and captures a substantial share of the quantitative magnitude, providing a credible link between the theoretical mechanism and the reduced-form evidence.

A counterfactual decomposition of the calibrated model confirms that this network-determined rigidity heterogeneity—which I call the flexibility channel—is the primary driver of the cross-sectional pattern. Instead, the cost propagation, or cost-cascade channel, usually emphasized in multi-sector models—through which upstream price adjustments propagate to downstream marginal costs—plays only a secondary, and partially offsetting, role. The intuition is that, holding rigidity fixed, a sector’s price tracks the flexible wage in proportion to its labor share, so cost linkages would reinforce the upstreamness pattern only if upstream sectors were labor-intensive. In U.S. data they are the opposite—intermediate-input intensive, with marginal costs tied to other, themselves sticky, prices rather than to wages. The cost-cascade channel therefore tilts the larger price responses toward downstream sectors, working against the upstream flexibility advantage rather than amplifying it. This decomposition clarifies that the production network’s primary role is to determine which sectors are flexible, rather than to propagate price adjustments across stages.

I highlight a stark asymmetry in the cross-sectional pattern. Extending the model to allow for asymmetric price rigidity—the empirical regularity that prices adjust more readily upward than downward—I show that the upstreamness differential in price responses is substantially larger following expansionary shocks than contractionary ones. The data are consistent with this prediction. In response to a rate cut, the peak interaction coefficient is more than twice the pooled peak; cumulating over the one-to-two-year window where the responses diverge most, the upstreamness differential is large and negative following rate cuts but near zero following rate hikes, providing evidence of downward nominal rigidity. This corroborates the ‘rockets and feathers’ phenomenon long documented at the aggregate level, indicating that inflation is easier to generate than deflation. For central banks, the implication is that rate cuts generate larger cross-sectional price dispersion than rate hikes—a structural asymmetry in the transmission mechanism that is invisible in representative-firm models.

These price dynamics in response to monetary policy shocks have implications for the real economy. The model highlights that industries whose prices adjust more flexibly absorb monetary shocks primarily through price changes, preserving real output; industries with sticky prices instead absorb shocks through quantity changes. The empirical results match these predictions. Upstream sectors, whose prices are more flexible, exhibit less negative real effects than downstream sectors. Examining contractionary and expansionary shocks separately reveals patterns mirroring the price-side asymmetry. That is, I do not find statistically significant real effects in response to expansionary shocks. However, contractionary shocks lead upstream industries to cut prices more aggressively and preserve real output, and downstream industries to absorb the shock through quantity rationing. In sum, price flexibility substitutes for quantity adjustment, generating cross-sectional dispersion in both prices and output that is concentrated in contractionary episodes, consistent with the asymmetric price rigidity mechanism in the model.

Although the decomposition shows that the cost-cascade channel is not the primary driver of the upstreamness differential, costs do propagate through the network, and this propagation is detectable in the data. Three auxiliary tests support the view that buyer-seller price linkages play a role in transmitting price adjustments across sectors, even if they do not generate the cross-sectional pattern on their own. First, controlling for input-cost-weighted supplier prices absorbs most of the upstreamness interaction, consistent with the effect operating partly through cost linkages rather than omitted industry characteristics. Second, the interaction between upstreamness and the monetary shock is significantly stronger for industries with higher intermediate input shares. Third, an industry's suppliers' network positions predict its own price response.

These findings survive extensive robustness checks. Alternative network measures (eigenvector centrality, intermediate input share) and monetary policy shocks (Jarociński and Karadi, 2020) yield significant interaction coefficients of comparable magnitude. Similarly, controlling for industry characteristics potentially correlated with industry upstreamness delivers consistent results. The results are also robust to constraining the sample to the manufacturing sector or to removing one industry at a time. Finally, permutation-based placebo tests indicate that upstreamness—not an arbitrary industry ranking—generates the differential price response.

The results of this paper have implications for monetary policy analysis. If the cross-sectional distribution of price rigidity is shaped by the production network, then structural changes in the network can alter the potency of monetary policy even if average price rigidity remains unchanged. Any policy or structural shift that alters the IO matrix—trade agreements, vertical integration, platform-mediated disintermediation—changes the composition of B2B versus B2C activity across the economy, reshaping the distribution of rigidity across network positions. The secular increase in the services share of GDP shifts economic activity toward sectors that are both more downstream and more price-rigid, increasing the wedge between upstream and downstream rigidity and potentially strengthening the asymmetry documented in this paper.

## 1.1 Related literature and contributions

This paper contributes to three strands of the literature. The first is the literature on production networks and nominal rigidities. A large body of work has established that IO linkages shape the propagation of real shocks (Long and Plosser, 1983; Acemoglu et al., 2012; Gabaix, 2011; Barrot and Sauvagnat, 2016; Carvalho et al., 2021; Baqaee and Farhi, 2019). $^{4}$ A separate literature has studied how heterogeneity in nominal price rigidity affects aggregate monetary non-neutrality (Carvalho, 2006; Nakamura and Steinsson, 2010; Kehoe and Midrigan, 2015). $^{5}$

The intersection of these two strands of literature—how nominal rigidities interact with production network structure—has received less attention. The theoretical foundation was laid by Basu (1995), who showed that when firms use other firms' outputs as intermediate inputs, each firm's marginal cost depends on its suppliers' prices, so that upstream price rigidity propagates downstream and amplifies aggregate monetary non-neutrality. Building on this insight, Nakamura and Steinsson (2010) develop a multi-sector menu cost model with intermediate inputs calibrated to 14 U.S. sectors, showing that the combination of heterogeneous price stickiness and roundabout production substantially amplifies monetary non-neutrality. Pasten et al. (2020) calibrate a multi-sector Calvo model with sector-specific adjustment probabilities and find that heterogeneity in price-adjustment frequency is the dominant driver of monetary non-neutrality while IO linkages contribute only marginally—the aggregate counterpart of the cross-sectional decomposition I develop below. Relatedly, Pastén et al. (2024) show that heterogeneity in sectoral price stickiness amplifies the aggregate effects of idiosyncratic productivity shocks and reshapes which sectors matter for aggregate fluctuations. Rubbo (2023) demonstrates that IO linkages propagate rigidity across stages, flattening the aggregate Phillips curve. More recently, Afrouzi and Bhattarai (2024) derive closed-form sufficient statistics for inflation and GDP dynamics in this class of models, showing that all dynamics are governed by a duration-adjusted Leontief matrix and that, as in my decomposition, an upstream sector's contribution depends on whether it is flexible or sticky, not on its network position alone. My theoretical contribution relative to this literature, which uniformly assumes symmetric price adjustment, is to extend the propagation matrix to sign-dependent rigidity. That is, asymmetric rigidity splits the duration-adjusted Leontief into distinct expansionary and contractionary matrices, whose gap generates a network-amplified asymmetry that is absent from all symmetric frameworks.

All these papers focus on aggregate statistics—the level of GDP volatility, the slope of the Phillips curve. Ghassibe (2023) is the first to provide empirical evidence on network amplification of monetary policy, estimating that at least 30% of the effect of monetary shocks on U.S. aggregate final consumption comes from amplification through IO linkages. His analysis uses sectoral consumption data for up to 161 BEA sectors and focuses on the aggregate contribution of networks. I shift the lens from the aggregate to the cross-section, asking not how much total non-neutrality production networks generate but which industries bear the largest price and output responses and through what mechanism. I provide direct empirical evidence for the cross-sectional anatomy of monetary transmission through production chains and document a novel asymmetry that is absent from all three frameworks.

The second strand of literature this paper relates to is the one on asymmetric price adjustment and production networks. Micro-level evidence has long documented that prices rise faster than they fall (Peltzman, 2000; Nakamura and Steinsson, 2008). In a representative-firm model, such asymmetric rigidity merely shifts the level of price adjustment. I show that in a production network, asymmetric rigidity shifts the differential across upstream and downstream sectors: the asymmetry compounds through K - 1 intermediate pricing decisions along a chain of length K, so the direction of the shock matters multiplicatively. The data are in line with this prediction. This result connects to the broader literature on nonlinearities in monetary transmission (Tenreyro and Thwaites, 2016) and provides a micro-founded, cross-sectional mechanism for the aggregate observation that inflation is easier to generate than deflation.

Finally, this paper also speaks to the empirical evidence on networks and monetary policy. Ozdagli and Weber (2025) document that network-central firms exhibit stronger stock-price responses to monetary surprises, and Ghassibe (2023) provides consumption-side evidence that network amplification accounts for a substantial share of aggregate monetary non-neutrality. I focus on goods prices, providing a more direct test of the New Keynesian pricing mechanism. $^{6}$ Moreover, I provide suggestive evidence that costs propagate through buyer-seller price linkages, confirming that the IO network transmits price signals across production stages even though the cross-sectional differential is primarily driven by the flexibility channel. Closest in spirit on the empi

[中间内容因长度限制已省略]

</td><td>-0.058**(0.029)</td><td>-0.188(0.140)</td><td>-0.214(0.141)</td><td>-0.193(0.119)</td><td>-0.200(0.154)</td><td>-0.165(0.190)</td><td>-0.062(0.209)</td><td>0.075(0.239)</td><td>0.061(0.245)</td><td>0.166(0.265)</td><td>0.246(0.256)</td><td>0.316(0.278)</td><td>0.386(0.301)</td></tr><tr><td rowspan="3">Observations</td><td rowspan="3">56,803</td><td rowspan="3">56,779</td><td rowspan="3">56,755</td><td rowspan="3">56,731</td><td rowspan="3">56,707</td><td rowspan="3">56,059</td><td rowspan="3">55,411</td><td rowspan="3">54,763</td><td rowspan="3">54,115</td><td rowspan="3">53,469</td><td rowspan="3">52,824</td><td rowspan="3">52,179</td><td rowspan="3">51,534</td></tr><tr></tr><tr></tr></table>

Notes: Each column reports local projection estimates at the indicated horizon h (months). The sample is restricted to manufacturing sectors. The dependent variable is the cumulative log price change. Panel A reports the interaction coefficient from the symmetric specification in Equation 27. Panel B reports estimates from the asymmetric specification in Equation 28. All specifications include industry fixed effects, sector-time fixed effects, and one lag of own-industry PPI inflation. Driscoll-Kraay standard errors in parentheses. \*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.10.

Outliers Figure A3 plots the distribution of leave-one-out estimates at selected horizons. Each panel shows the distribution of the coefficient on the interaction term between upstreamness and monetary policy shocks obtained by re-estimating Equation 27 after dropping one industry from the sample. The estimates are tightly concentrated around the baseline at all horizons, confirming that no single industry drives the results.

## Figure A3: Leave-one-out distribution

![](images/f89ff2c3c4df86c0fc393745cd2975d765a58fd63baebcf83eac1c60e621ca92.jpg)

![](images/8bd421b24dcf3174188e1544d22af550ddcee1d97770eb9639cb70b5ae5eeac0.jpg)

(c) h = 18  
![](images/69ae088b5722fc720520b0c34997973ac7f69cdfb8fa6ed0fb9440154a023190.jpg)

(d) h = 24  
![](images/c07c5d08495256b97521f4fbd65e032f02e87d2e69de82c6a05340fdc8fb022b.jpg)  
Notes: Each panel shows the distribution of the coefficient on the interaction term between upstreamness and monetary policy shocks from 271 leave-one-out re-estimations at the indicated horizon. The vertical dashed line marks the baseline estimate using all industries. All specifications include industry fixed effects, sector×time fixed effects, and one lag of own-industry PPI inflation.

Placebo test I randomly reassign the upstreamness measure across industries and re-estimate the baseline interaction coefficient, repeating the procedure 200 times to build a placebo distribution under the null that network position is unrelated to price responsiveness. Figure A4 plots this distribution against the actual estimate at each horizon. The placebo distribution is centered near zero, whereas the baseline estimate lies far in its left tail at every horizon, indicating that the result is specific to the observed upstreamness ranking.

Figure A4: Distribution of permutation estimates  
![](images/b8725466abb6e78a07eb9deb217f5e11b8e07bdc719c95366d0410b8d22d8a7c.jpg)  
(c) h = 18

![](images/fd65819af4f68158d56a201c9ed298ba7a196f32e8a0cb7100d01190b7d1fe3e.jpg)  
(d) h = 24

![](images/349552537915b18ad5ddd9a15610b44ae5a83bf392d92473f926e07f2ead9a1b.jpg)  
Upstreamness × MP shocks

![](images/45506ef92ce56da0f0190db412ae7761ba40cf93615b471d7ee2e3c766fff144.jpg)  
Upstreamness × MP shocks  
Notes: Each panel shows the distribution of the coefficient on the interaction term between upstreamness and the monetary policy shocks from 200 permutations of upstreamness across industries at the indicated horizon, along with the actual estimate from the baseline specification.

Sub-samples Table A11 verifies that the main interaction coefficient is stable across sub-samples. The first column reports the full-sample baseline, while the remaining columns split the sample into the period up to the Global Financial Crisis (2010), the post-crisis period (2011 onward), and the full sample excluding the COVID period (through December 2019).

Table A11: Interaction coefficient across sub-periods

<table><tr><td></td><td>Full sample</td><td>Up to GFC</td><td>Post-GFC</td><td>Excl. COVID-19</td></tr><tr><td>Upstreamness × MP shocks</td><td>-0.113***(0.039)</td><td>-0.083*(0.048)</td><td>-0.118**(0.060)</td><td>-0.103***(0.037)</td></tr><tr><td>Observations</td><td>69,772</td><td>25,592</td><td>39,622</td><td>53,795</td></tr><tr><td> $R^2$ </td><td>0.003</td><td>0.011</td><td>0.004</td><td>0.004</td></tr></table>

Notes: Each column reports the estimated interaction coefficient $\hat{\beta}_{18}$ for the indicated sub-period. The dependent variable is the cumulative log price change. The pre-crisis sub-period ends in December 2010; the post-crisis sub-period begins in January 2011; the excluding-COVID sub-sample ends in December 2019. All specifications include industry fixed effects, sector-time fixed effects, and one lag of own-industry PPI inflation. Driscoll-Kraay standard errors in parentheses. \*\*\* $p < 0.01$ ; \*\* $p < 0.05$ ; \* $p < 0.10$ .

![](images/2850b1c437d653b3c5232e4277da7db48abaf6aa77ba5a3c46e6b0d8db20474f.jpg)
"""
