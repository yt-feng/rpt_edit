你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

【研报解析内容】
"""
THE EM TRADER

# Curves, Chips, Crude and Carry

EM FX: Navigating Energy and Rate Risks. With the re-escalation of the Iran conflict, EM currencies have depreciated versus the Dollar, with energy importers once again underperforming and exporters outperforming. Still, the magnitude of FX moves has been smaller for a similar move in oil to that in March. We attribute this to (1) a more benign risk backdrop, which we think helps explain the better performance of high-beta BRL and COP, (2) the fact that FX had not fully retraced back to its pre-war levels, with many energy importers trading close to their weakest levels in early July, and (3) the underlying terms of trade shock being also smaller in magnitude, especially for CLP and PEN given copper price resilience. When linking FX moves to these fundamentals, we find that most EM currencies outperformed our model slightly during the recent re-escalation episode, contrasting with the sharp underperformance in early March. KRW and COP outperformance and ZAR, CLP and MXN underperformance stand out relative to our model's inputs.

Still a Path for RV Carry; Watching Carry-to-Vol Closely. The disruptive Fed hike tail looks to be curtailed for now, but there are still rate risks from a continued selloff in the long-end of the curve and high energy prices. The easiest way to resolve these risks is a sustained path to lower energy prices, but until that point EM FX carry structures will likely continue to balance risk and reward by choosing both longs and funders carefully, maximising carry-to-vol and monitoring closely local developments that can challenge carry returns. BRL and COP remain the strongest propositions by a wide margin in both carry and carry-to-vol terms, and also benefit from higher energy prices, but are vulnerable to higher long-end US yields (and BRL specifically to upcoming election noise). Within the next set of currencies with around 3% carry versus the Dollar (INR, IDR, MXN, ZAR), there are importance differences in carry-to-vol dynamics and local developments that lead us to prefer MXN carry (rising carry-to-vol, especially versus Euro, greater exposure to US growth and resilience to oil price fluctuations), followed by INR (high carry-to-vol and central bank support, but limited scope for appreciation) and ZAR (much lower carry-to-vol but equally greater scope for spot appreciation on a conflict resolution), while maintaining a more cautious view on IDR (due to domestic developments). HUF carry has declined substantially since the election, making it increasingly more of a spot than a carry trade. We maintain a constructive HUF outlook over the

## Kamakshya Trivedi

+44(20)7051-4005 |
kamakshya.trivedi@gs.com
GS International

Sunil Koul
+44(20)7051-4931 | sunil.koul@gs.com
GS International

Danny Suwanapruti
+65-6889-1987 |
danny.suwanapruti@gs.com
GS (Singapore) Pte

Teresa Alves
+44(20)7051-7566 |
teresa.alves@gs.com
GS International

Tarun Lalwani, CFA
+1(212)934-5821 |
tarun.lalwani@gs.com
GS India SPL

Victor Engel
+44(20)7051-3862 |
victor.engel@gs.com
GS International

Lexi Kanter
+1(212)855-9701 |
alexandra.kanter@gs.com
GS & Co. LLC

Mambuna Njie
+44(20)7051-7705 |
mambuna.njie@gs.com
GS International

medium term but think near-term dynamics look more challenging. Overall, our preferred funders in G10 are CHF, EUR, JPY and CAD in roughly that order, and in EM we think THB, ILS and PLN screen as attractive funders from both a carry and spot asymmetry perspective. CLP's low carry and high beta to risk and energy prices makes it an attractive funder for investors looking to neutralise broader risk exposures.

EM Local Rates: Fed up with Energy... Uncertainty around a sustainable resolution to the Iran war and the energy price volatility this creates remains the primary driver of EM and G10 rates. While cleaner positioning, benign inflation prints and EM central bank reaction functions that have turned out to be more dovish relative to market pricing at the start of the war have helped trim the more adverse tails in local rates pricing despite the recent bouts of energy price increases, we continue to think that any relief is likely to be limited until there is more visibility on the supply side factors. It is therefore important to be tactical and selective against this backdrop of still elevated commodity prices and the prospects for core central bank hikes.

... But the Fatigue Is Uneven. We prefer markets where rates have backed up and central banks lean dovish (PLN, HUF, ILS). Conversely, while we think EM Asia low-yielders (KRW, PHP) are pricing too much in the front-end, very accommodative real policy rates will likely keep hike pressures live. In LatAm, MXN is still vulnerable to Fed hikes given low rate differentials and high US front-end sensitivity; in BRL, despite the BCB's easing bias and attractive front-end in our view, high realised vol into the October elections keep us sidelined. Medium term, tight EM long-end spreads to the US and the possibility of elevated core duration (with a mild version emerging post-FOMC yesterday) limit the scope for broad-based long-end compression, except in select high-yielders with improving fiscal paths (INR, ZAR), or COP, which may join them.

EM Equities: Tech Unwind Extends, Non-Tech Resilient to Renewed Energy Shock. The EM equity index (MSCI EM) has retraced 12% from its late June peak, reversing about half of its strong 1H gains driven by ongoing unwinds in crowded tech and AI infrastructure stocks, and renewed escalation in the US-Iran conflict. While the tech unwind has extended in recent days, non-tech EM equities have shown a muted response to rising oil prices so far, with MSCI EM ex-tech up 2% in July. This resilience is supported by lower starting valuations and price levels in oil-sensitive markets, which remain meaningfully below pre-war levels. Furthermore, strong micro fundamentals have cushioned the downside as early 2Q results are tracking ahead of consensus estimates, with positive median earnings surprise – and beats outpacing misses – driving further EPS upgrades.

Still Expect EM Broadening on Improving Earnings and Diversification Appeal. While the global de-grossing in tech has accelerated in recent weeks amid investor fears around rising China competition, AI capex sustainability, and a high bar for 2Q tech earnings, we remain fundamentally constructive and expect continued strong profit growth in AI infrastructure stocks. Volatility could stay elevated in the near term, however, as leveraged positions, although reset from highs, have not fully cleared. As long as macro volatility related to oil and rates is contained, we continue to expect a broadening in EM equities beyond tech, supported by underlying earnings accrual and the regional diversification appeal of non-tech markets, as evidenced during past major TMT drawdowns.

EM Sovereign Credit Issuance: Robust in H1, With More to Come in H2. Despite concerns that large amounts of AI-related debt supply may be crowding out other sectors or countries, EM gross sovereign USD bond issuance has been robust so far this year, propelled by the forward spend on security and energy infrastructure by IG GCC sovereigns since the onset of the Iran war. Both EM IG and HY H1 issuance stand at their second-highest levels in a decade. Our core view is still that the drivers of such robust issuance include the prevalence of favourable issuance terms, with sovereigns taking advantage of tight spreads, and elevated investor demand for primary supply. Looking ahead, our updated full-year 2026 issuance forecast stands at \~US\$209bn, with the lion's share from IG (\~US\$138bn, 66%), and HY contributing \~US\$72bn (34%). While our forecasts appear consistent with a bullish risk-on scenario that is not our baseline, we think they reflect a strong technical backdrop and a large idiosyncratic issuance profile from IG GCC sovereigns. This gross supply should translate into elevated net supply by the end of the year, which should in turn contribute to the moderate spread widening we expect over the next 12 months.

## EM FX: Navigating Energy and Rate risks

Re-escalation relative performance consistent with, but smaller magnitude than, the initial shock. As oil prices rose through July (specifically, from the re-escalation of the US-Iran conflict on 6 July 2026 to the peak in oil prices on 23 July 2026), EM currencies generally depreciated versus the Dollar, with energy importers underperforming (especially those in CEEMEA and LatAm) and energy exporters (namely, COP and BRL) outperforming (Exhibit 1). These relative moves were largely consistent with the relative performance at the start of the conflict in early March, though KRW is a notable exception, BRL appreciated instead of depreciating and COP outperformed by more than in March. We noted that, while the oil move was similar over these July and March windows, broader risk did not sell off as much in July. We think this helps explain the smaller magnitude of the moves observed in July and the better performance of BRL and COP as energy exporters but equally high-beta currencies. Moreover, looking at where currencies were trading relative to their YTD range on July 6 (red diamonds in Exhibit 2), we find that most energy importers were close to their weakest levels, and had not recovered even as oil prices had fallen close to their pre-conflict levels. Most energy importers in Asia and CEEMEA (with the exception of CNH, KRW and HUF) are currently trading close to their weakest levels year-to-date.

Exhibit 1: EM FX responses have been broadly similar to the start of the war, but more muted overall, with a few notable outliers such as KRW and COP  
![](images/1a5d2ab9e8aea9e30344a741132416638720e912a80c2ffccbadd2c110f9409f.jpg)  
Source: Bloomberg, GS Global Investment Research

Exhibit 2: Many energy importers were trading close to their weakest levels YTD even before the re-escalation  
![](images/e92fa03f9124a6755ce551f6d89a5114726530b5db269bd3999909185ab8ac4b.jpg)  
Source: Bloomberg, GS Global Investment Research

Broader terms of trade shift also smaller than in early March, with many energy importers' indices above their weakest levels YTD. Looking more fundamentally at how terms of trade have shifted over this window in July versus at the start of the conflict, we also find that relative moves have been similar but the magnitudes have been smaller (Exhibit 3), which in our view can also help explain the smaller spot FX moves in energy importers (Exhibit 1). For CLP and PEN, the deterioration in terms of trade has been significantly smaller over the most recent window as copper prices have risen, whereas they had fallen in March. In level terms, our GS terms of trade indices are near their lowest levels for the year for many energy importers, especially HUF and ZAR, though still above their peak deterioration (Exhibit 4). Among the energy importers, CLP stands out again, with Chile's terms of trade not too far from the strongest levels YTD, and similarly INR and PLN terms of trade are far from their

weakest levels YTD.

Exhibit 3: Shifts in terms of trade have been similar to the start of the war in relative terms, although the overall magnitude has been smaller

![](images/ec2f9f5347e8e9e59e47d904b0c9a993921dbac2d54006acc6f870f771540e6e.jpg)  
Source: GS FICC and Equities, GS Global Investment Research

Exhibit 4: Terms of trade currently near their lowest YTD levels for many energy importers but CLP is key exception

![](images/ba6d254c3dbb8f2f089c8fa9caff3f5d693a6d7c87b74d3756b74e086aed4285.jpg)  
Source: GS FICC and Equities, GS Global Investment Research

\- Relative EM FX performance was broadly in line with model predictions, with oil prices the key factor driving relative performance. In order to marry FX market moves with these other developments, we refreshed our simple model of FX returns relative to other market developments (S&P 500, oil and copper prices, and US 10-year real yields) over this period between July 6 and 23; Exhibit 5 shows the ‘predicted’ returns of this model together with the contribution of each input and ‘actual’ returns. Overall, EM FX performance was broadly in line with model predictions, with oil prices the key factor driving relative performance. Energy exporters, such as BRL and COP, were the top performers, though COP outperformed the model-implied prediction whereas BRL slightly underperformed. Energy importers including ZAR, HUF, PLN, THB and PHP were the worst performers, but this can largely be explained by the model’s inputs, except for ZAR (more on this below). Compared with the initial energy shock in February, the deterioration in broader risk sentiment was more muted this time, resulting in a smaller overall depreciation across EM FX, as discussed above.

Exhibit 5: EM FX performance was broadly in line with model predictions, with oil prices the key factor driving relative performance

![](images/5747e21a5f5019e32bd91e1a88ea783e0f5b41c77b3af223f2e6cedd5bd989c5.jpg)

Predicted returns based on sensitivity of weekly FX returns vs USD to changes in the S&P, US 10-year real yields, oil and copper prices over the 5 years before February 27, 2026

Source: Bloomberg, GS Global Investment Research

Most currencies slightly outperformed the model's inputs, with some exceptions. In Exhibit 6, we plot model-predicted returns on the x-axis against actual FX performance on the y-axis. In contrast to the first energy shock in February, when many currencies underperformed their model-implied returns, most EM currencies outperformed during the recent US-Iran re-escalation episode (i.e., lying above the 45-degree line). As discussed above, we think this partly reflects the fact that FX had not fully retraced from the initial shock prior to the renewed escalation and terms of trade shifts were broadly smaller than in March. There were, however, a few notable exceptions, with KRW and COP among the largest outperformers and ZAR, CLP and MXN among the largest underperformers (i.e., furthest away from the 45-degree line). We think these deviations can be explained by idiosyncratic developments. The KRW appreciation this month coincided with policy tightening, measures to curb leverage, and capital inflows associated with reduced equity-related outflows. For COP, continued optimism following the election and expectations of further policy rate hikes have provided support to the Peso beyond the boost from higher oil prices, in our view. By contrast, ZAR underperformed the most relative to model-implied returns, reflecting the SARB's against-consensus decision to keep interest rates on hold. CLP also underperformed relative to the model despite limited local developments. While the direction of the move is consistent with the shift in terms of trade, we believe the move may have gone too far relative to fundamentals, given that the deterioration in ToT has been significantly less severe than during the first energy shock in February.

Exhibit 6: Most EM currencies outperformed model-implied returns based on other market variables during the recent US-Iran re-escalation episode

![](images/da4882b7c5683425897297ccf896e43affecc76528c0965130320b94a147ca51.jpg)  
Source: Bloomberg, GS Global Investment Research

Still a path for RV carry between energy and rate risks, watching carry-to-vol closely. The disruptive Fed hike tail looks to be curtailed for now, especially given our economists' expectations for relatively soft upcoming inflation prints, but there are still rate risks from a continued selloff in the long-end of the curve and high energy prices. The easiest way to resolve these risks is a sustained path to lower energy prices, but until that point EM FX carry structur

[中间内容因长度限制已省略]

ttempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global

Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
