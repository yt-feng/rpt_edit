你是知乎商业/行业研究作者，擅长把英文/中文研报改写成适合知乎发布的长文。

【目标】
- 基于下面研报解析内容，生成一篇中文知乎文章。
- 风格接近微信公众号文章，但更适合知乎：论证更完整、语气更克制、有问题意识、有推理链条。
- 文章不需要把研报所有内容讲完，要留下继续阅读完整报告或加入社群讨论的空间。
- 目标长度：约 2200 字，允许上下浮动 20%。

【结构要求】
1. 第一行：知乎标题，直接讲观点，不要标题党，不要夸张极限词。
2. 开头 2-3 段：用一个真实问题或市场分歧切入，说明为什么这份报告值得看。
3. 正文按金字塔原则组织：先给核心判断，再展开 3-5 个支撑逻辑。
4. 每个小标题都要像观点句，不要写“核心判断”“支撑逻辑一”“对读者的启发”这种模板名。
5. 内容要比小红书更理性，比微信更像问答式分析，可以适度提出反问。
6. 结尾自然留下讨论空间，可使用这类表达：`完整报告里还有不少细节，适合放在社群里继续拆。`

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- 不要写“非投资建议”“仅做学习交流”这种免责声明，也不要出现包含“投资”的免责声明。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要使用“爆款”“震惊”“必看”“必读”“最强”“最全”“唯一”“全网首发”等极限词。

【内容要求】
- 只能基于研报原文和解析内容推导，不要编造数据、页数、作者、结论或引用。
- 可以基于报告内容做适度发散，但必须明确哪些是报告内容，哪些是你的延展观察。
- 默认避免具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或使用 GS/JPM/MS 等缩写。
- 不要输出解释说明，只输出知乎文章正文。

【研报解析内容】
"""
Asia Global

# Foreign Exchange FX Special Report

# Where's fair value for EUR/CNY?

The EU is currently in the middle of what has been described as 'China Shock 2.0', with its trade deficit with China widening materially in recent years. There are multiple factors simultaneously at play, including relative energy prices and subsidy policies. Another factor is the exchange rate.

At the recent G7 Summit, German Chancellor Friedrich Merz said that the European Union was competing with countries whose currencies were highly undervalued. While not explicitly mentioned, the spotlight has fallen most heavily on the CNY.

In this special report we investigate yuan valuations against the euro. To ensure robustness, we employ ten different models to assess valuations in EUR/CNY. Extending the analysis, we also look to where our suite of models would put the hypothetical fair value for DEM/CNY. This helps to understand whether Germany faces a more acute competitiveness problem compared to the wider Euro area.

Our central results indicate that at its peak last year, EUR/CNY overvaluation was likely around 20%. With its recent appreciation, the yuan remains around 15% undervalued against the euro on our central estimates. This level of undervaluation is similar to the extremes seen during 2005-08. However, during that period euro over-valuation was much more broad-based. All our models suggest that yuan undervaluation is more pronounced against a hypothetical Deutschmark, illustrative of how Germany's competitiveness challenge is larger than the wider Euro Area.

Figure 1: CNY remains firmly undervalued against the euro, and screens even cheaper against a hypothetical Deutschmark

<table><tr><td>Type of valuation</td><td>Model</td><td>CNY valuation vs EUR</td><td>CNY valuation vs DEM</td></tr><tr><td rowspan="2">Absolute PPP</td><td>Big Mac Index</td><td>-46%</td><td>-52%</td></tr><tr><td>OECD PPP</td><td>-34%</td><td>-38%</td></tr><tr><td rowspan="2">Absolute PPP - detrended for Balassa-Samuelson effect</td><td>Big Mac Index - detrended</td><td>-20%</td><td>/</td></tr><tr><td>OECD PPP - detrended*</td><td>-18%</td><td>-22%</td></tr><tr><td rowspan="2">Relative PPP</td><td>Bilateral, PPI-based PPP*</td><td>-14%</td><td>-14%</td></tr><tr><td>Bilateral, CPI-based PPP</td><td>-11%</td><td>-12%</td></tr><tr><td>Relative PPP adjusted for growth, terms of trade</td><td>Dbeer</td><td>-10%</td><td>/</td></tr><tr><td rowspan="3">External balance</td><td>FEER - full current account</td><td>-9%</td><td>-16%</td></tr><tr><td>FEER - Goods and services (Setser-adjusted)</td><td>-9%</td><td>-14%</td></tr><tr><td>FEER - Goods trade only, exc. 22 energy shock*</td><td>-10%</td><td>-13%</td></tr><tr><td></td><td>Average of preferred (*) models</td><td>-14%</td><td></td></tr></table>

Source : DB, The Economist, OECD, Haver Analytics, Bloomberg Finance LP
Note: The EUR/CNH spot rate was taken as 7.75 for all the PPP results.

## Introduction

The European Union is currently in the middle of what our economists have described as 'China Shock 2.0', with its trade deficit with China widening materially in recent years.

There are many factors at play. Firstly, China has moved up the manufacturing value chain. China is now in direct trade competition with the EU in more sectors, with cars perhaps the most visible example. Secondly, price differentials have moved in China's favour and against Europe, which is itself a result of multiple factors. These include the larger shock to European energy costs after Russia's invasion of Ukraine, subsidies which are lowering China's production costs, and the exchange rate. The latter is the broad focus of this report, and has become an increasingly prevalent topic of discussion in recent weeks.

Indeed, at the G7 Summit a few weeks ago, German Chancellor Friedrich Merz reportedly said that the EU was competing against countries whose currencies were highly undervalued, thus further hurting the European Union's competitiveness problem.

In this report, we look at ten different long-term metrics to assess the undervaluation of the yuan against the euro and a hypothetical Deutschmark. We look at two different types of long-term currency valuation: Purchasing Power Parity (PPP) and external balance models. They range from the very simple, but accessible, Big Mac Index to a Fundamental Equilibrium Exchange Rate (FEER) model adjusting for idiosyncracies of the respective China and Euro Area trade data.

Our central results indicate that, despite its recent appreciation, the yuan remains around 15% undervalued against the euro. This compares to an undervaluation of over 20% twelve months ago. All our models suggest that the undervaluation of the yuan is more pronounced against a hypothetical Deutschmark than that of the euro, illustrative of how Germany's competitiveness challenge is larger than the wider Euro Area.

Figure 2: Euro Area trade deficit with China in goods is widening  
![](images/4faa27bf1c5d185aa4ea9e4f1fdda85707d5cc0325b33787a401cb4b9a4f0675.jpg)  
Source : DB, Haver Analytics

## Purchasing Power Parity (PPP)

PPP models remain the bedrock of long-term currency valuation assessment, and use differences in prices to assess where nominal (spot) exchange rates should trade ("fair value").

We start with absolute PPP, and specifically with perhaps the simplest and most widely known model: The Economist's Big Mac Index. Under the model, since a Big Mac costs around 25.5 yuan in China and €6.10 in the Euro Area (€6.90 in Germany), the law of one price in turn implies that fair value for EUR/CNY is just under 4.20 (Figure 3). With spot trading at around 7.75 at the time of writing, this very simple model suggests that CNY is around 45% undervalued against the euro.

The OECD's PPP metric uses similar logic as the Big Mac Index, but looks at the relative price levels across a wide range of goods and services, rather than focusing on the relative cost of a single good. $^{1}$ Its results are similarly stark, pointing to an approximate 35% undervaluation of the yuan against the euro (Figure 4).

Figure 3: The relative price of a burger suggests the yuan is close to 50% undervalued against the euro  
![](images/d787161eeb908888ab57452e5c3fa3b1b065ef5139f58769d0fde03b5298f900.jpg)  
Source : DB, Haver Analytics

Figure 4: OECD measures - aggregated up at economy-wide scale - also imply material undervaluation  
![](images/4c66b98bdf977a440f79c759778284b2922ee8b34b48a3ac378c635c3acfb00d.jpg)  
Source : DB, Haver Analytics

However, plotting the misalignments from these metrics over time is informative in several ways (Figure 5 and Figure 6). Firstly, the yuan has always screened cheap on these metrics, showing between 20% and 70% undervaluation. Nevertheless, the undervaluations on these metrics had – until relatively recently – been firmly trending in a positive direction. In other words, CNY was becoming less undervalued over time. This is consistent with Balassa-Samuelson effect, a country like China with high productivity growth in its tradable goods sector should see its real exchange rate strengthen over time - leaving it less undervalued on absolute PPP metrics. However, this trend notably reversed over the past four years, which have seen a clear break in CNY valuation from this trend with valuations cheapening again since 2022.

To adjust for these factors, Figure 7 shows detrended Big Mac and OECD PPP valuations. These measures help illustrate the sharp cheapening over recent years, which even after this year's partial correction and fall in EUR/CNY spot, still sees the yuan around 20% undervalued against the euro, and cheaper still against a hypothetical Deutschmark, using German price data (Figure 8).

Figure 5: CNY had trended less cheap over time on Big Mac Index...  
![](images/9a94c11f16badc0d8b01b238c405834d881a3843a7352f3db588b09b325e9a67.jpg)  
Source : DB, Haver Analytics

Figure 6:... and on OECD PPP basis  
![](images/2a84453460f4786279284eca7a125dc3ded0a442eb20810f75453fd088f81109.jpg)  
Source : DB, Haver Analytics

Figure 7: Detrended absolute PPP measures show around 20% cheapness in CNY vs EUR  
![](images/dca23f12701e6cbc5d0924ce7cbbaa73a4ced2714d49a4c8bfd937811f03d4b5.jpg)  
Source : DB, Haver Analytics

Figure 8: Absolute PPP metrics suggest yuan even more undervalued against a hypothetical Deutschmark than euro  
![](images/69bb6da127980fc97ec15a779e34cacaf7c61272b326c97cf128035033e34305.jpg)  
Source : DB, Haver Analytics

Absolute PPP imposes a strict condition for valuations by assuming that nominal exchange rates should move to offset specific price level differences. A softer variant is relative PPP, which instead assumes that exchange rates should move to offset differences in changes in prices (i.e., inflation) over time. In other words, the assumption is that real exchange rates are stationary.

We build two simple relative PPP models. Firstly, we calculate the bilateral real exchange rate for EUR/CNY by deflating spot by the ratio of the respective consumer price indices (CPI). To then obtain our valuation, we simply compare this real exchange rate to its (rolling) 10-year average. We then repeat this methodology using producer prices (PPI), and also then again specifically using German rather than Euro Area-wide price data. The results over time are shown in Figure 9 and Figure 10. The PPI-metric currently points to a c. 14% undervaluation in the yuan against the euro, with similar results when looking just at Germany.

One thing to note is that this PPI-based metric implicitly assumes that the impact of any subsidies in China is directly reflected in lower producer prices. If, for example, manufacturers instead paid the market rate for their inputs but were then later reimbursed via these subsidies, then the "true" undervaluation of the yuan on this metric would be larger in magnitude.

Going one step further, we can add some "extra trimmings" to our relative (CPI-based) PPP model, to control for other long-term drivers of real exchange rates such as productivity differentials, terms of trade changes, and economic openness. The implied fair value on this metric – our DBeer model – is just over 7.15, suggesting CNY is around 8% undervalued against the euro (Figure 11). $^{2}$

Figure 9: EUR/CNY spot vs CPI and PPI-implied relative PPP fair value  
![](images/5e1613e6779f3232ff1436f50cdef6c64c3cb1d9be792469420d65ec8c1ca21e.jpg)  
Source : DB, Bloomberg Finance LP, Haver Analytics

Figure 10: DEM/CNY spot vs CPI and PPI-implied relative PPP fair value  
![](images/eede0bcd3927e646f7a6996c84b22d98e6a52f8ac82db611c8f0d09a80f63e21.jpg)  
Source : DB, Bloomberg Finance LP, Haver Analytics

Figure 11: EUR/CNY vs DBeer (relative PPP adjusted for terms of trade and productivity)  
![](images/ad6a6abd5f606ab7e6e34cf64467ad67238ad775ff8099749dec637edc522bfa.jpg)  
Source : DB, Bloomberg Finance LP, Haver Analytics

Figure 12: Overall yuan screens c. 12% cheap against the euro and c. 15% cheap vs DEM on relative PPP metrics  
![](images/5b895a88fc99f182581bde65b3c2f465d9d6b68527d3573771b671fd7ba1b1b3.jpg)  
Source : DB, Bloomberg Finance LP, Haver Analytics. Note: EUR/CNH spot rate taken as 7.75 in these results

## External balance models

The PPP models described above all focus on the exchange rate movements required to equalise price levels or to offset inflation differences between regions. By contrast, external balance models estimate the exchange rate movement required to drive a single region's current account or trade balance to a specific level or "equilibrium".

Our benchmark external balance model, FEER, uses full current account data as its key input. This in turn comprises of trade in goods and services as well as income balances which capture cross-border investment returns (e.g. dividends) and transfer payments. Specifically, our benchmark model estimates the currency movement required to return a regions latest (last 12m) current account balance to its 10-year average, which we use as our proxy for the region's "equilibrium". To calculate the valuation, we use the average across two different estimates of current account sensitivity to exchange rates ("elasticity"), one from the IMF and one from Cline and Williamson (2008).

So, what do the latest results on our benchmark FEER model show? Overall, the full current account (inclusive of income balances) for the entire Euro Area is quite close to its average over the past decade (+1.7% of GDP vs 10y avg. +1.9%). To be sure, this average includes a period (2022-23) when the large energy shock put huge downward pressure on the goods balance, in particular. Nevertheless, as a result of the latest reading sitting only slightly below its average, on an aggregate trade-weighted (TWI) basis this baseline model only suggests a mild (<1%) overvaluation for the Euro. Meanwhile, China's headline current account balance sits at just under 4% of GDP, compared to an average over the last decade of c. 1.8% of GDP. As a result, our benchmark FEER model points to the renminbi being c. 7.5% undervalued on a broad, TWI, basis.

However, the headline current account data for both regions notably contain significant distortions. On the Euro Area side, the headline current account data are distorted by Ireland – see here for more. On the China side, Setser has noted the potential distortions to both the goods trade data flowing into the reported Balance of Payments figures and to the (investment) income side. To account for these, we also consider a few variations of our FEER model.

Firstly, we exclude income balances and focus just on the trade component of the current account, which captures both goods and services trade. We also use Setser's customs-based adjustment to the goods trade for China to account for the apparent change in methodology and reporting over the past few years. And on the Euro Area side, we exclude Irish trade from the data.

Secondly, we isolate trade in goods only. Here, for China, we take an average of three different reporting sources of Chinese goods trade data (domestic statistics body, WTO, IMF). All three broadly point to a surplus in goods trade alone of around 6% of GDP, vs a 10-year average of closer to 4% (Figure 13). For the Euro Area here, we again exclude Ireland, and we reduce the effect of the energy shock by assuming an unchanged goods balance between early 2022 and mid 2023. The gap between the Euro Area's latest external balance metrics and its 10-year average is most pronounced here, when looking only at goods trade (0.3% of GDP vs 0.9% average) (Figure 14).

Finally, we also look at external balance metrics for Germany specifically (Figure 15). Interestingly, the gap between Germany's latest external balance and its historical average widens when factoring in both services and income balances (full current account at 4.3% of GDP vs 6.8% average), compared to when solely looking at trade in goods (4.5% of GDP vs 6.0% average). Figure 16 summarises the trade and external balance metrics used across our FEER iterations.

Figure 13: China external balances roughly 2ppt of GDP better than average, across multiple metrics  
![](images/c1fc4886646bfb6e1beb504e1d2cd42203a80c1921018dca47c8a2286d4e6518.jpg)  
Source : DB, Haver Analytics, CFR

Figure 14: Euro Area wide external balances a little worse than average  
![](images/66006a01d44690c7e72483d6022e731c86357ea5b7daac4eac32c4e6943b8700.jpg)  
Source : DB, Haver Analytics

Figure 15: German external balance metrics firmly worse than historical average  
![](images/ac342bb1d404977ea94e7e157139948bf6fc4231049f0e7eb04191c67810da59.jpg)

Figure 16: Summary of external balance metrics for China, Euro Area, and Germany  
![](images/8d27416505f5fdbf893c0d75eeeb92bd0ebaf9234c4460802cbac59628eb6f56.jpg)

Figure 17 plots the results over time for China on our three different FEER iterations. All produce similar results, showing the yuan to be close to its historical extremes of undervaluation in trade-weighted terms. For Europe, all three iterations of the model indicate only a very mild overvaluation for the euro as a whole. However, the results are more striking when looking at Germany specifically. Using goods trade only, a hypothetical Deutschmark is just over 4% overvalued on a broad basis. $^{3}$ However, its overvaluation doubles when looking at the whole German current account, inclusive of services trade and income balances (Figure 18).

FEER metrics are generally used for partial equilibrium analysis for one regions's trade with the rest of the world, as opposed to bilateral analysis between two specific countries. As such, results are usually presented in terms of trade-weighted currency valuations (TWI, rather than specific crosses. Nevertheless, to allow for comparison with our other metrics, we use the matrix inversion method (Cline) to convert our implied broader TWI valuations into EUR/CNY (& DEM/CNY) misalignments. Figure 19 shows the results across the three FEER variations.

Unlike PPP metrics, the valuations are not directly affected by immediate changes in spot rates. Its valuations only change once the external balance metrics start to converge closer to their average and thus are slower-moving. As our colleagues note for Germany, there are some small signs of a nascent reversal in the worsening trade deficit with China (Figure 20). In part this may be because some of the strengthening over the past year in the yuan against the euro is starting to feed through. But as all our models here show, a large portion of the currency undervaluation remains.

Figure 17: Yuan undervaluation close to historical extremes across all iterations of our FEER models  
![](images/0d3f2ddaa990a610ffd81be3caa715bf87c3db0503953f34eae129e2d970c495.jpg)  
Source : DB, Haver Analytics  
Figure 18: FEER models show more pronounced overvaluation for a hypothetical DEM than wider Euro Area

![](images/60b4fc0195ecb761e5a9a6ef2f8b3cebf628bad0c035bd1ab97f9b9b8bd48dd8.jpg)  
Source : DB, Haver Analytics

Figure 19: Implied CNY undervaluation vs EUR & DEM on FEER metrics  
![](images/25321545aae6f568661523dddbd8839cf9650d4b26dd87d370ebf585deb75c01.jpg)  
Source : DB, Haver Analytics

Figure 20: Nascent signs of slowing down in deterioration of Euro Area trade deficit with China  
![](images/23011b2f9517b69878e5ec7c8561397bf98456f0402aedd46d885210d864f360.jpg)  
Source : DB, Haver Analytics

## Conclusion

Our central results indicate that, despite its recent appreciation, the yuan remains around 15% undervalued against the euro. This compares to an undervaluation of over 20% twelve months ago. Nearly all our mo

[中间内容因长度限制已省略]

h for confirmation/clarification of data, facts, statements, permission to use company-sourced material in the report, and/or site-visit attendance. Without prior approval from Research Management, analysts may not accept from current or potential Banking clients the costs of travel, accommodations, or other expenses incurred by analysts attending site visits, conferences, social events, and the like. Similarly, without prior approval from Research Management and Anti-Bribery and Corruption ("ABC") team, analysts may not accept perks or other items of value for their personal use from issuers they cover.

Additional information relative to securities, other financial products or issuers discussed in this report is available upon request. This report may not be reproduced, distributed or published without DB's prior written consent.

Backtested, hypothetical or simulated performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG.

It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG

<table><tr><td>DB AG21 MoorfieldsLondon EC2Y 9DBUnited KingdomTel: (44) 20 7545 8000</td><td>DB Securities Inc.The DB Center1 Columbus CircleNew York, NY 10019Tel: (1) 212 250 2500</td><td>DB AGFiliale SingapurOne Raffles Quay, South Tower,Singapore 048583TeL: +65 6423 8001</td></tr></table>

<table><tr><td colspan="4">David Folkerts-LandauGroup Chief Economist and Global Head of Research</td></tr><tr><td>Pam FinelliCOO and Head of Fixed Income Research</td><td>Steve PollardGlobal Head of Company Research and Sales</td><td>Jim ReidGlobal Head of Macro and Thematic Research</td><td>Tim RokossaHead of European Company Research</td></tr><tr><td>Matthew BarnardHead of AmericasCompany Research</td><td>Debbie JonesGlobal Head of Sustainability and Data Innovation, Research</td><td>Robin WinklerHead of German Macro Research</td><td>Sameer GoelGlobal Head of EM &amp; APAC Research</td></tr><tr><td>Francis YaredGlobal Head of Rates Research</td><td>George SaravelosGlobal Head of FX Research</td><td>Peter HooperVice-Chair of Research</td><td>Nilendra de-MelHead of APAC &amp; Middle East Product Development</td></tr></table>

## International Production Locations

<table><tr><td>DB AG</td><td>DB AG</td><td>DB AG</td><td>Deutsche Securities Inc.</td></tr><tr><td>DB Place</td><td>Equity Research</td><td>Filiale Hongkong</td><td>1-3-1 Azabudai</td></tr><tr><td>Level 16</td><td>Mainzer Landstrasse 11-17</td><td>International Commerce</td><td>Azabudai Hills Mori JP Tower</td></tr><tr><td>Corner of Hunter &amp; Phillip</td><td>60329 Frankfurt am Main</td><td>Centre,</td><td>Minato-ku, Tokyo 106-0041</td></tr><tr><td>Streets</td><td>Germany</td><td>1 Austin Road West,Kowloon,</td><td>Japan</td></tr><tr><td>Sydney, NSW 2000</td><td>Tel: (49) 69 910 00</td><td>Hong Kong</td><td>Tel: (81) 3 6730 1000</td></tr><tr><td>Australia</td><td></td><td>Tel: (852) 2203 8888</td><td></td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td></td><td></td></tr></table>
"""
