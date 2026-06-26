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
# Optimal Currency Basket Estimation

Prepared by Etienne Vaccaro-Grange

WP/26/131

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

2026
APR

![](images/bc31b4f028ecf143731495989e480d51cab9659f69b05b4ea48b21b98d9da55e.jpg)

# IMF Working Paper Monetary and Capital Markets

Optimal Currency Basket Estimation
Prepared by Etienne Vaccaro-Grange

Authorized for distribution by Romain Veyrune
April 2026

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

ABSTRACT: Small open economies often anchor their exchange rate to a basket of foreign currencies, with weights typically set from trade shares or financial exposure. Such schemes ignore the heterogeneity of pass-through across currencies and the covariance structure of bilateral rates, and therefore do not minimize the volatility of imported inflation, the central bank's mandate. This paper proposes a minimum-variance framework — formally analogous to a Markowitz portfolio problem in pass-through space — in which basket weights minimize the variance of exchange-rate-driven imported inflation, subject to a constraint that preserves the basket's cumulative pass-through. Applied to the case of Fiji, an import-intensive island economy with a five-currency basket, the optimization reduces the variance of imported inflation by close to twenty percent, with results robust across alternative specifications.

RECOMMENDED CITATION: E. Vaccaro-Grange, “Optimal Currency Basket Estimation”, IMF Working Paper No. 26/131, International Monetary Fund, Washington DC.

<table><tr><td>JEL Classification Numbers:</td><td>E31, E52, F31, F41</td></tr><tr><td>Keywords:</td><td>currency basket; exchange rate pass-through; minimum-variance portfolio; small open economies; monetary policy.</td></tr><tr><td>Authors&#x27; email addresses:</td><td>evaccaro-grange@IMF.org</td></tr></table>

# Optimal Currency Basket Estimation

Prepared by Etienne Vaccaro-Grange $^{1}$

## Contents

Acronyms....3   
Introduction....4   
Model....5   
Application to a Small Open Economy....10   
Conclusion....16   
Annex I. Derivation....17   
References....19

## FIGURES

1. Historical Exchange Rates (Normalized January 1999=100)....11
2. Inflation....11
3. Inflation Pass-throughs....12
4. Currency Return Correlations....13

TABLES
1. Currency Basket Weights (percent)....14
2. Robustness—Models Specification....14
3. Currency Basket Weights (percent)....15

## Acronyms

AUD Australian Dollar

CPI    Consumer Price Index

EUR Euro

FC Foreign Currency

FX Foreign Exchange

GBP British Pound

JPY Japanese Yen

LC Local Currency

MOM Month-On-Month

NZD New Zealand Dollar

PPP Purchasing Power Parity

USD US Dollar

## INTRODUCTION

A currency basket peg is an exchange rate regime in which the domestic currency is anchored to a weighted average of several foreign currencies rather than to a single anchor. By spreading exchange rate risk across multiple partners, a basket peg offers intermediate flexibility between a hard peg and a managed float and provides a degree of insulation from volatility in any single cross-rate (Williamson, 1998). Such arrangements are often adopted by small open economies for which a freely floating regime is impractical—typically because of thin foreign exchange markets, underdeveloped financial systems, or the desire to import credibility from a more stable monetary jurisdiction (Imam, 2010; Yoshino, Helble, and Prasetyo, 2017). Pacific island economies such as Fiji, Samoa, Tonga, and the Solomon Islands, as well as other small open economies including Kuwait and Morocco, currently operate basket regimes of this kind.

The central design question for any basket peg is how to determine the weights assigned to its constituent currencies. The most widely used approach relies on trade shares, with weights reflecting the geographical distribution of exports and imports, sometimes supplemented by flows of services, remittances, or external debt service (Edison and Vårdal, 1990; Yoshino, Helble, and Prasetyo, 2017). While transparent and intuitive, trade-based weights describe only the structure of external transactions and do not, in general, coincide with the weights that best support a central bank's price-stability mandate. In particular, they exploit neither the heterogeneity of exchange rate pass-through across currencies nor the covariance structure of bilateral exchange rate movements—two features that are central to the behavior of imported inflation.

A substantial literature has sought to derive optimal basket weights under explicit macroeconomic objectives. Flanders and Helpman (1979) provided an early framework linking basket weights to balance-of-payments and real income stability, extended by Branson and Katseli (1981), Turnovsky (1982), and Bhandari (1985). Edison and Vårdal (1990) derived optimal weights that minimize the variance of tradable-goods production and applied them to the Nordic countries. Yoshino, Kaji, and Suzuki (2004) developed a three-country basket model, later extended by Yoshino, Helble, and Prasetyo (2017) to a four-country setting with tourism flows that minimized the volatility of the exchange rate and of output. They apply the model to Pacific Island economies. Ma and Cheng (2014) proposed a two-stage model in which the basket is chosen to minimize a weighted average of output and inflation volatility, taking into account ex-post fiscal adjustment, and applied it to Hong Kong SAR

. A parallel strand of work by Slavov (2005), Teo (2009), Shioji (2006), Xu (2011), and Zhang, Shi, and Zhang (2011) embed basket choice in general-equilibrium settings that incorporate trade invoicing, net international investment position, and foreign-currency debt. A separate but closely related literature has documented that exchange rate pass-through into import prices is partial, heterogeneous across currencies and industries, and shaped by pricing-to-market, nominal rigidities, and strategic complementarities (Krugman, 1987; Knetter, 1989; Betts and Devereux, 2000; Campa and Goldberg, 2005; Gopinath and Itskhoki, 2010; Gopinath, Itskhoki, and Rigobon, 2010).

This paper contributes to the literature by bringing these two strands together. We propose a basket-weight optimization framework whose objective is to minimize the variance of the exchange-rate-driven component of imported inflation—he basket's inflation pass-through—rather than balance-of-payments or aggregate output volatility. In contrast to trade-weighted schemes, the procedure exploits both the currency-specific pass-through coefficients estimated from a standard import price equation and the covariance structure of bilateral exchange rate returns. The resulting problem is formally analogous to a Markowitz minimum-variance portfolio, with currencies as “assets”, pass-through-adjusted exchange rate changes as “returns”, and basket weights as

portfolio shares. A structural constraint preserves the cumulative pass-through implied by the current basket, so that the optimized weights reduce the volatility of imported inflation without altering the average sensitivity of domestic prices to basket movements. To the best of our knowledge, this is the first paper to cast optimal basket design explicitly as a minimum-variance pass-through problem subject to an invariant structural pass-through.

We illustrate the framework with an application to a small, import-intensive island economy that has operated a five-currency basket since the 1980s: Fiji. We show that the newly optimized weights would reduce variance of inflation by about 20 percent relative to the current weights, while preserving the basket's structural pass-through. A series of robustness exercises confirms the stability of the main results across alternative specifications of the pass-through equation.

Two additional determinants of optimal basket design deserve mention but lie outside the scope of this paper. First, the degree of business cycle synchronization between the home economy and each currency area provides a complementary argument for anchoring: a higher degree of co-movement strengthens the case for assigning greater weight to the corresponding currency. Second, financial dollarization — through foreign-currency-denominated deposits or external debt obligations — introduces balance-sheet stability constraints that neither trade- nor price-based schemes capture. We abstract from both dimensions and focus strictly on minimizing the variance of exchange-rate-driven imported inflation, in line with the central bank's price-stability mandate. Integrating cycle synchronization and balance-sheet considerations into the optimization problem is left for future work.

The rest of the paper is structured as follows: Section 1 presents the model, Section 2 its application to a small open economy, and Section 3 concludes.

## MODEL

From the law of one price, an imported good's domestic currency price is:

$$
P _ {t} ^ {m} = E _ {t} P _ {t} ^ {x}\tag{1}
$$

where $E_{t}$ is the nominal exchange rate (units of domestic currency per unit of foreign currency; up equals depreciation), $P_{t}^{m}$ is the domestic currency-denominated import price, and $P_{t}^{x}$ is the foreign currency-denominated export price. In log-differences, we obtain: $^{2}$

$$
\Delta p _ {t} ^ {m} = \Delta e _ {t} + \Delta p _ {t} ^ {\mathrm{x}}
$$

(2)

Or with usual notations $\pi_t^m = \Delta p_t^m$ , $\pi_t^x = \Delta p_t^x$ :

$$
\pi_ {t} ^ {m} = \Delta e _ {t} + \pi_ {t} ^ {\mathrm{x}}\tag{3}
$$

This equation holds for a single trading partner j:

$$
\pi_ {j, t} ^ {m} = \Delta e _ {j, t} + \pi_ {j, t} ^ {\mathrm{x}}\tag{4}
$$

Aggregate imported inflation is the trade-weighted sum across all n partners:

$$
\pi_ {t} ^ {m} = \sum_ {j = 1} ^ {n} w _ {j} \pi_ {j, t} ^ {m}\tag{5}
$$

$$
\pi_ {t} ^ {m} = \sum_ {j = 1} ^ {n} w _ {j} \Delta e _ {j, t} + \sum_ {j = 1} ^ {n} w _ {j} \pi_ {j, t} ^ {\mathrm{x}}\tag{6}
$$

where $w_{j}$ is the import share of partner j and $\sum_{j=1}^{n} w_{j}=1$ .

In theory, the law of one price implies that exchange rate movements are fully and instantaneously reflected in domestic currency-denominated import prices. In practice, however, a well-documented set of microeconomic frictions attenuates this transmission. We say that the pass-through is incomplete.

Under local currency pricing (Betts and Devereux, 2000), exporters set prices in the destination currency, rendering import prices mechanically insensitive to exchange rate fluctuations between repricing episodes. Even upon repricing, firms operating in imperfectly competitive markets may optimally absorb part of the exchange rate change into their markups rather than pass it through to final prices, a behavior formalized in the pricing-to-market literature (Krugman, 1987; Knetter, 1989). This markup adjustment is reinforced by strategic complementarity in price setting: when importers' demand depends on their price relative to domestic competitors, optimal pricing tilts toward the domestic price level, dampening the response to exchange rate shocks (Gopinath and Itskhoki, 2010). Nominal rigidities in the form of menu costs or staggered price adjustment à la Calvo (1983) introduce additional delays in the transmission process. Collectively, these frictions imply that only a fraction of any given exchange rate movement is ultimately transmitted to import prices, a result consistently supported by the empirical evidence (Campa and Goldberg, 2005; Gopinath, Itskhoki, and Rigobon, 2010). This motivates an empirical specification in which the incomplete pass-through is freely estimated rather than imposed at unity.

In that framework, Equation (6) becomes:

$$
\pi_ {t} ^ {m} = \sum_ {j = 1} ^ {n} \beta_ {j} \Delta e _ {j, t} + \sum_ {j = 1} ^ {n} \delta_ {j} \pi_ {j, t} ^ {\mathrm{x}} + \varepsilon_ {t}\tag{7}
$$

where the $\beta_{j}$ are no longer constrained to equal $w_{j}$ — they capture they capture the effective pass-through of each bilateral exchange rate into aggregate import prices, reflecting both trade shares and the degree of passthrough specific to each partner. Similarly, $\delta_{j}$ may differ from $w_{j}$ since the same pricing frictions that attenuate exchange rate pass-through — markup absorption, nominal rigidities, and strategic complementarity — also apply to the transmission of foreign cost changes (though to a lesser extent as firms have stronger incentives to pass through increases in their own production costs). Both coefficients are expected to be lower than the trade weight $w_{j}$ , so that $\sum_{j=1}^{n}\beta_{j}<1$ and $\sum_{j=1}^{n}\delta_{j}<1$ .

The empirical specification includes several standard features motivated by theory. Lags of the bilateral exchange rate returns and exported price inflation capture the gradual adjustment of import prices under nominal rigidities. Indeed, as firms reprice at discrete intervals, the full pass-through of an exchange rate shock materializes over several periods rather than instantaneously, so that the sum of contemporaneous and lagged coefficients measures the cumulative long-run pass-through while individual coefficients trace the dynamic adjustment profile (Campa and Goldberg, 2005). Lags of imported inflation are included for the same reason — under staggered price-setting à la Calvo (1983), only a fraction of importers reprice each period, generating intrinsic persistence in the aggregate import price level that the autoregressive terms capture. The constant absorbs any secular trend in imported inflation unrelated to exchange rate movements, such as a persistent differential between domestic and foreign trend inflation or a systematic evolution in importers' markups over time.

Equation (7) becomes:

$$
\pi_ {t} ^ {m} = \mu + \sum_ {k = 1} ^ {p} \rho_ {k} \pi_ {t - k} ^ {m} + \sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {q} \beta_ {j, k} \Delta e _ {j, t - k} + \sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {l} \delta_ {j, k} \pi_ {j, t - k} ^ {\mathrm{x}} + \varepsilon_ {t}\tag{8}
$$

where $\mu$ is a constant, $\rho_{k}$ captures the persistence in imported inflation arising from staggered price-setting, $\beta_{j,k}$ is the pass-through of currency j at lag k, and $\delta_{j,k}$ captures the lagged transmission of partner j's export price inflation. Further, we assume that foreign exported inflation is approximately equal to foreign inflation for the tractability of the model: $\pi_{j,t}^{x} \approx \pi_{j,t}^{*}$ .³

Equation (8) can be further simplified under relative PPP condition, since: $\Delta e_{j,t} = \pi_{t} - \pi_{j,t}^{*} \approx \pi_{t}^{m} - \pi_{j,t}^{x}$ . That is, the difference between domestic inflation and foreign inflation is roughly the difference between imported inflation and foreign exported inflation.

Therefore,

$$
\pi_ {t} ^ {m} = \mu + \sum_ {k = 1} ^ {p} \rho_ {k} \pi_ {t - k} ^ {m} + \sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {q} \beta_ {j, k} \Delta e _ {j, t - k} + \sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {l} \delta_ {j, k} (\pi_ {t - k} ^ {m} - \Delta e _ {j, t - k}) + \varepsilon_ {t}\tag{9}
$$

$$
\pi_ {t} ^ {m} = \mu + \left(\sum_ {k = 1} ^ {p} \rho_ {k} + \sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {l} \delta_ {j, k}\right) \pi_ {t - k} ^ {m} + \sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {q} \beta_ {j, k} \Delta e _ {j, t - k} - \sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {l} \delta_ {j, k} \Delta e _ {j, t - k} + \varepsilon_ {t}
$$

(10)

$$
\pi_ {t} ^ {m} = \mu + \left(\sum_ {k = 1} ^ {p} \rho_ {k} + \sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {l} \delta_ {j, k}\right) \pi_ {t - k} ^ {m} + \sum_ {j = 1} ^ {n} \left(\sum_ {k = 1} ^ {q} \beta_ {j, k} - \sum_ {k = 1} ^ {l} \delta_ {j, k}\right) \Delta e _ {j, t - k} + \varepsilon_ {t}\tag{11}
$$

$$
\pi_ {t} ^ {m} = \mu + \sum_ {k = 1} ^ {\tilde {p}} \tilde {\rho} _ {k} \pi_ {t - k} ^ {m} + \sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {\tilde {q}} \tilde {\beta} _ {j, k} \Delta e _ {j, t - k} + \varepsilon_ {t}\tag{12}
$$

with $\sum_{k=1}^{\tilde{p}}\tilde{\rho}_k = \sum_{k=1}^p\rho_k + \sum_{j=1}^n\sum_{k=1}^l\delta_{j,k}$ and $\sum_{k=1}^{\tilde{q}}\tilde{\beta}_{j,k} = \sum_{k=1}^q\beta_{j,k} - \sum_{k=1}^l\delta_{j,k}$ . For simplicity, we will drop the $\sim$ and retain the following pass-through equation:

$$
\boxed {\pi_ {t} ^ {m} = \mu + \sum_ {k = 1} ^ {p} \rho_ {k} \pi_ {t - k} ^ {m} + \sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {q} \beta_ {j, k} \Delta e _ {j, t - k} + \varepsilon_ {t}}\tag{13}
$$

Another less strict specification consists in assuming that foreign exported inflation is approximately equal to foreign inflation: $\pi_{j,t}^{\mathrm{x}}\approx \pi_{j,t}^{*}$ . Equation (7) then becomes:

$$
\boxed {\pi_ {t} ^ {m} = \mu + \sum_ {k = 1} ^ {p} \rho_ {k}   \pi_ {t - k} ^ {m} + \sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {q} \beta_ {j, k}   \Delta e

[中间内容因长度限制已省略]

eta_ {j} c _ {j, t}\right) \\ + \operatorname{cov} \left(\sum_ {j = 1} ^ {n} \theta_ {j} z _ {j, t} ^ {\mathrm{FC/FC} _ {0}}, \sum_ {j = 1} ^ {n} \theta_ {j} c _ {j, t}\right) ^ {T} \end{array}\tag{9}
$$

Let's define $Z_{t}^{FC/FC_{0}} = \left\{ z_{j,t}^{FC/FC_{0}} \right\}$ , $\Sigma_{z}^{FC/FC_{0}} = \text{Var}(Z^{FC/FC_{0}})$ , $\Sigma_{c} = \text{Var}(c_{t})$ , and $\Gamma = \text{Cov}(Z_{t}^{FC/FC_{0}}, c_{t})$ . Then,

$$
\operatorname{Var} \left(\sum_ {j = 1} ^ {n} \theta_ {j} z _ {j, t}\right) = \theta^ {\prime} \Sigma_ {\mathrm{z}} ^ {\mathrm{FC/FC} _ {0}} \theta + \theta^ {\prime} \Sigma_ {\mathrm{c}} \theta + \theta^ {\prime} \Gamma \theta + \theta^ {\prime} \Gamma^ {\prime} \theta\tag{10}
$$

$$
\operatorname{Var} \left(\sum_ {j = 1} ^ {n} \theta_ {j} z _ {j, t}\right) = \theta^ {\prime} \left(\Sigma_ {\mathrm{z}} ^ {\mathrm{FC/FC} _ {0}} + \Sigma_ {\mathrm{c}} + \Gamma + \Gamma^ {\prime}\right) \theta\tag{11}
$$

Define, $\Sigma_{\overline{Z}} = \Sigma_{z}^{\mathrm{FC / FC_0}} + \Sigma_c + \Gamma +\Gamma '$

Therefore,

$$
\boxed {a r g m i n _ {\theta} \left[ V a r (z _ {t} ^ {B}) \right] = a r g m i n _ {\theta} \left[ V a r \left(\sum_ {j = 1} ^ {n} \theta_ {j} z _ {j, t}\right) \right] = a r g m i n _ {\theta} [ \theta^ {\prime} \Sigma_ {\overline {{Z}}} \theta ]}\tag{12}
$$

## REFERENCES

Betts, Caroline, and Michael B. Devereux. 2000. “Exchange Rate Dynamics in a Model of Pricing-to-Market.” Journal of International Economics, 50(1): 215–244.

Bhandari, Jagdeep S. 1985. "Experiments with the Optimal Currency Composite." Southern Economic Journal, 51(3): 711–730.

Branson, William H., and Louka T. Katseli, 1981. "Currency Baskets and the Real Effective Exchange Rates." NBER Working Paper 0666, National Bureau of Economic Research, Inc.

Calvo, Guillermo A. 1983. “Staggered Prices in a Utility-Maximizing Framework.” Journal of Monetary Economics, 12(3): 383–398.

Campa, José Manuel, and Linda S. Goldberg. 2005. "Exchange Rate Pass-Through into Import Prices." Review of Economics and Statistics, 87(4): 679–690.

Edison, Hali J., and Erling Vårdal. 1990. “Optimal Currency Baskets for Small, Developed Economies.” Scandinavian Journal of Economics, 92(4): 559–571.

Flanders, M. June, and Elhanan Helpman. 1979. “An Optimal Exchange Rate Peg in a World of General Floating.” Review of Economic Studies, 46(3): 533–542.

Gopinath, Gita, and Oleg Itskhoki. 2010. “Frequency of Price Adjustment and Pass-Through.” Quarterly Journal of Economics, 125(2): 675–727.

Gopinath, Gita, Oleg Itskhoki, and Roberto Rigobon. 2010. "Currency Choice and Exchange Rate Pass-Through." American Economic Review, 100(1): 304–336.

Imam, Patrick A. 2010. “Exchange Rate Choices of Microstates.” IMF Working Paper No. 10/12. Washington, DC: International Monetary Fund.

Jayaraman, T. K., and C-K., Choong. 2011. "Impact of Exchange Rate Changes on Domestic Inflation: A Study of a Small Pacific Island Economy." MPRA Paper No. 33719, University Library of Munich.

Knetter, Michael M. 1989. "Price Discrimination by U.S. and German Exporters." American Economic Review, 79(1): 198–210.

Krugman, Paul. 1986. "Pricing to Market When the Exchange Rate Changes.", NBER Working Paper 1926, National Bureau of Economic Research, Inc.

Ma, Zihui, and Leonard K. Cheng. 2014. “An Optimal Currency Basket to Minimize Output and Inflation Volatility: Theory and an Application to Hong Kong.” Pacific Economic Review, 19(1): 90–111.

Peiris, S. J., and D. Ding. 2012. "Global Commodity Prices, Monetary Transmission, and Exchange Rate Pass Through in the Pacific Islands."

Shioji, Etsuro. 2006. “Invoicing Currency and the Optimal Basket Peg for East Asia: Analysis Using a New Open Economy Macroeconomic Model.” Journal of the Japanese and International Economies, 20(4):569–589.

Slavov, Slavi T. 2005. “Should Small Open Economies in East Asia Keep All Their Eggs in One Basket? The Role of Balance Sheet Effects.” Journal of the Korean Economy, 9(1): 1–43.

Teo, Wing Leong. 2009. "Should East Asia's Currencies Be Pegged to the Yen? The Role of Invoice Currency." Journal of the Japanese and International Economies, 23(3): 283–308.

Turnovsky, Stephen J. 1982. "A Determination of the Optimal Currency Basket: A Macroeconomic Analysis." Journal of International Economics, 12(3–4): 333–354.

Williamson, John. 1998. “Crawling Bands or Monitoring Bands: How to Manage Exchange Rates in a World of Capital Mobility.” International Finance, 1(1): 59–79.

Xu, Juanyi. 2011. "Optimal Currency Basket with Vertical Trade." Journal of International Money and Finance, 30(7): 1323–1340.

Yoshino, Naoyuki, Matthias Helble, and Ahmad Danu Prasetyo. 2017. “Exchange Rate Policy in the Pacific: An Evaluation of Currency Basket Regimes.” Asian-Pacific Economic Literature, 31(1): 3–20.

Yoshino, Naoyuki, Sahoko Kaji, and Ayako Suzuki. 2004. “The Basket-Peg, Dollar-Peg, and Floating: A Comparative Analysis.” Journal of the Japanese and International Economies, 18(2): 183–217.

Zhang, Zhichao, Nan Shi, and Xiaoli Zhang. 2011. “China’s New Exchange Rate Regime, Optimal Basket Currency and Currency Diversification.” MPRA Paper No. 32642. Munich: University Library of Munich.

![](images/0939fa876f8dec0794694b1ecf1e44ac6284d125164603b9cb6b9385faa22687.jpg)
"""
