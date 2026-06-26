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
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`国际货币基金组织`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
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
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：加入社群，领取完整研报解读与原始图表。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份国际货币基金组织研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

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
\boxed {\pi_ {t} ^ {m} = \mu + \sum_ {k = 1} ^ {p} \rho_ {k}   \pi_ {t - k} ^ {m} + \sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {q} \beta_ {j, k}   \Delta e _ {j, t - k} + \sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {l} \delta_ {j, k}   \pi_ {j, t - k} ^ {*} + \varepsilon_ {t}}\tag{14}
$$

An alternative modeling approach consists in defining the cumulative pass-through given by $\bar{\beta}_{j} = \sum_{k=0}^{q} \beta_{j,k}$

Assuming that $\beta_{j,k}$ is constant over time for country j, so that $\beta_{j,1} = \beta_{j,2} = \ldots = \beta_{j,q}$ , we can then re-write Equation (13) as:

$$
\boxed {\pi_ {t} ^ {m} = \mu + \sum_ {k = 1} ^ {p} \rho_ {k} \pi_ {t - k} ^ {m} + \sum_ {j = 1} ^ {n} \bar {\beta} _ {j} \sum_ {k = 1} ^ {q} \Delta e _ {j, t - k} + \varepsilon_ {t}}\tag{15}
$$

Equation (13), (14), and (15) are three different versions of the pass-through regression equations. Let's now define, $z_{j,t}$ , the total pass-through contribution of currency $j$ :

$$
z _ {j, t} = \sum_ {k = 1} ^ {q} \beta_ {j, k} \Delta e _ {j, t - k}\tag{16}
$$

Further, let's define the basket rate as the weighted geometric average of $n$ currencies:

$$
e _ {t} ^ {B} = \prod_ {j = 1} ^ {n} e _ {j, t} ^ {\theta_ {j}}\tag{17}
$$

Where $e_{t}^{B}$ is the basket rate per unit of domestic currency, $e_{j,t}$ is the exchange rate of foreign currency j per unit of domestic currency, and $\theta_{j}$ its weight in the basket. Besides, we have: $\theta_{j} \in [0, 1]$ and $\sum_{j=1}^{n} \theta_{j} = 1$ .

In that framework, the total inflation pass-through from the currency basket, $z_{t}^{B}$ , i

[中间内容因长度限制已省略]

t} ^ {F C / F C _ {0}} + \sum_ {j = 1} ^ {n} \theta_ {j} c _ {j, t}\right)\tag{8}
$$

$$
\begin{array}{l} V a r \left(\sum_ {j = 1} ^ {n} \theta_ {j} z _ {j, t}\right) = V a r \left(\sum_ {j = 1} ^ {n} \theta_ {j} z _ {j, t} ^ {\mathrm{FC/FC} _ {0}}\right) + V a r \left(\sum_ {j = 1} ^ {n} \theta_ {j} c _ {j, t}\right) + \operatorname{cov} \left(\sum_ {j = 1} ^ {n} \theta_ {j} z _ {j, t} ^ {\mathrm{FC/FC} _ {0}}, \sum_ {j = 1} ^ {n} \theta_ {j} c _ {j, t}\right) \\ + \operatorname{cov} \left(\sum_ {j = 1} ^ {n} \theta_ {j} z _ {j, t} ^ {\mathrm{FC/FC} _ {0}}, \sum_ {j = 1} ^ {n} \theta_ {j} c _ {j, t}\right) ^ {T} \end{array}\tag{9}
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
