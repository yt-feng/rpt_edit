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
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`JPM`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
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
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份JPM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
This material is neither intended to be distributed to Mainland China investors nor to provide securities investment consultancy services within the territory of Mainland China. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM.

# China Local Markets 2026 Mid-Year Outlook

Safer harbor, calmer waters

\- CNY FX and rates emerged as relative safe havens amid elevated global volatility in 1H26. USD/CNH declined a further 2.4% in a smoother-than-expected glide, aided by a near one-way lowering in the fix. This resilience, against a shifting USD backdrop, lifted the CNY TWI by 4.5% and drove outperformance versus Asia and major G10 FX. Meanwhile, CNY rates remained insulated from the global rates sell-off, with yields lower across the curve. Combined with FX gains, CGBs delivered a total return of \~5% ytd —modest versus EM high-yielders, but still notable for a low-yielding market.

\- CNY FX: Staying constructive; expecting further CNY strength in 2H26. Despite soft domestic conditions, resilient exports and a pickup in foreign inflows continue to underpin a strong flow backdrop for CNY FX. While wide US–China rate differentials remain a structural headwind, upcoming presidential engagements should encourage a supportive PBoC stance. Although the CNY TWI is above recent year trends, it remains well below prior peaks, leaving room for further gains. We remain bullish CNY FX and short USD/CNH via options, while staying open to rotate into higher CNH crosses if DXY firms further.

\- CNY Rates: Neutral on local duration; expecting yields to range bound. CNY rates head into 2H26 with valuations looking slightly rich, as 10Y CGB yields trade below our estimated fair value of $1.85\%$ . While these technicals point to near-term upside risks to yields, the misalignment is not large enough to suggest a meaningful risk of trend reversal. The strong duration demand seen in 1H26 is unlikely to fade meaningfully unless domestic demand shows a sustained recovery. Expectations for additional PBoC easing remain modest, with the forward curve pricing in roughly 5bp of cuts in the coming months, which we view as reasonable.

Emerging Markets Strategy

Tiffany Wang AC
(852) 2800-1726
tiffany.r.wang@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Arindam Sandilya
(65) 6882-7759
arindam.x.sandilya@JPM.com
JPM Chase Bank, N.A., Singapore Branch

Summary of JPM Forecasts and Strategy Views

<table><tr><td rowspan="2" colspan="2"></td><td rowspan="2">Latest</td><td colspan="4">Forecasts</td><td rowspan="2">Strategy Views</td><td rowspan="2">Risk bias and trade recommendation</td></tr><tr><td>3Q26</td><td>4Q26</td><td>1Q27</td><td>2Q27</td></tr><tr><td rowspan="3">China Local Markets</td><td>USD/CNY</td><td>6.80</td><td>6.70</td><td>6.70</td><td>6.75</td><td>6.80</td><td rowspan="2">Despite that domestic cyclical conditions remain soft amid weak demand, resilient exports and persistent corporate USD selling interest as well a pick-up in foreign inflows to Chinese assets continue to underpin a strong BoP backdrop for CNY FX. Although wider US–China rate differentials remain a structural headwind, upcoming high-level engagements could incentivize the PBoC to retain a supportive bias, helping sustain currency gains. The CNY TWI is running above recent year trends but it still remains well below prior cycle peaks, leaving room for further appreciation. We head into 2H26 remaining bullish on CNY FX via short USD/CNH in options, while we stay open to rotating into higher CNH crosses should DXY momentum firm further.</td><td rowspan="2">BullishMW CNY FX in GBI-EM3m 6.75 USD/CNH put</td></tr><tr><td>CNY TWI</td><td>102.7</td><td>104.0</td><td>105.0</td><td>104.5</td><td>104.0</td></tr><tr><td>10y CGB yield</td><td>1.74</td><td>1.80</td><td>1.80</td><td>1.70</td><td>1.70</td><td>CNY rates head into 2H26 with valuations looking slightly rich, as 10Y CGB yields trade around 10bp below our estimated fair value of 1.85%. While these technicals point to near-term upside risks to yields, the misalignment is not large enough to suggest a meaningful risk of trend reversal. The strong duration demand seen in 1H26 is unlikely to fade unless domestic demand shows a sustained recovery. While there is some optimism that an end to the Middle East conflict and a pickup in lagged fiscal spending could support a rebound in investment activity in the 2H, structural headwinds—including household balance sheet constraints and a prolonged property downturn—are likely to limit the scope for a domestically driven reflation, thereby keeping a cap on yields. Expectations for additional PBoC easing remain modest, with the forward curve pricing in roughly 5bp of cuts in the coming months, which we view as reasonable. We stay neutral on local duration, expecting yields to range bound.</td><td>NeutralMW CNY rates in GBI-EM</td></tr><tr><td rowspan="9">Global Markets</td><td>DXY</td><td>101.4</td><td>101.1</td><td>102.4</td><td>102.8</td><td>104.0</td><td></td><td></td></tr><tr><td>EUR/USD</td><td>1.14</td><td>1.14</td><td>1.13</td><td>1.12</td><td>1.10</td><td></td><td></td></tr><tr><td>AUD/USD</td><td>0.69</td><td>0.71</td><td>0.69</td><td>0.69</td><td>0.69</td><td></td><td></td></tr><tr><td>USD/JPY</td><td>162</td><td>160</td><td>164</td><td>164</td><td>164</td><td></td><td></td></tr><tr><td>USD/KRW</td><td>1548</td><td>1540</td><td>1560</td><td>1580</td><td>1585</td><td></td><td></td></tr><tr><td>Fed Funds Target Rate</td><td>3.75</td><td>3.75</td><td>3.75</td><td>3.75</td><td>3.75</td><td></td><td></td></tr><tr><td>2y UST yield</td><td>4.09</td><td>4.15</td><td>4.20</td><td>4.20</td><td>4.30</td><td></td><td></td></tr><tr><td>10y UST yield</td><td>4.37</td><td>4.65</td><td>4.70</td><td>4.75</td><td>4.75</td><td></td><td></td></tr><tr><td>Brent oil price (eop)</td><td>74</td><td>87</td><td>78</td><td>71</td><td>67</td><td></td><td></td></tr></table>

Source: JPM

See page 15 for analyst certification and important disclosures.

## Safer Harbor, Calmer Waters

## CNY FX (4Q26 USD/CNY 6.70): Stay bullish, short USD/CNH via options

A smoother-than-expected glide in 1H26. We entered 2026 bullish on CNY FX, and while the direction has proved correct, our year-end target of USD/CNY at 7.05—set in the 2026 year-ahead outlook (YAO)—apparently appears conservative. At the time, this reflected concerns that a Fed on hold, alongside lingering tightening risks, would keep upward pressure on US yields and create a less supportive external backdrop for CNY FX as a low-yielder. In 2025, declining core rates and narrowing US–China differentials were a major source of CNY strength, accounting for more than half of the 4.5% decline in USD/CNH in 2H25. At the time of writing the YAO, we expected such impulses to turn less positive. Indeed, US–China rate differentials have re-widened in 1H26, yet USD/CNH has largely bucked this move, leaving the recent acceleration in its decline increasingly disconnected from rate fundamentals (Figure 1, Figure 2). At the same time, CNY strength, especially in 2Q26, appears somewhat misaligned with cyclical conditions, as data surprises turned sharply negative in 2Q amid broad-based weakness in domestic investment and demand. Our tracking of China’s market-implied risk premium suggests only limited adjustment in China-linked assets (Figure 3), including CNY FX to this softer backdrop, leaving pricing relatively bullish versus cyclical fundamentals, with gaps near year-highs (Figure 4).

Figure 1: USD/CNH is becoming incrementally disconnected with rate fundamentals, ...  
contribution to 6m change in USD/CNH  
![](images/444201244376a6f3ee1dc19b0be6fb9c1e8f62ec127a4fdec0ddfadb5a774fc2.jpg)  
Source: Bloomberg Finance L.P., JPM

Figure 2: , ... with US-China yield differentials pointing to a much higher fair value for USD/CNH  
![](images/dd7a457e43ecd43d4e671c041181b5970e10a06d60ed1a2504210d5da5dd80ac.jpg)  
Source: Bloomberg Finance L.P., JPM

Figure 3: China-linked assets have yet to fully reprice the recent string of sharply negative data surprises, ...

s.d., misalignment between market-implied China risk premium vs economic data surprises, +ve indicate bullish market pricing

![](images/80ec5e3646b936d41134e43336954f51b1cda6fee76b01ce808bc68daf13f014.jpg)  
Source: JPM  
Figure 4: , ... with CNY FX standing out as notably more bullish than other China-linked assets  
s.d., misalignment between different asset returns vs market-implied China risk premium, +ve indicate bullish market pricing

![](images/2ad10f27124f921a0e2201b5c698ac3ccf685e389a6d324cfd35aefd1bfc79b5.jpg)  
Source: JPM

For CNY FX, though, such disconnects from rate differentials and domestic macro conditions are not uncommon, and model-implied valuations often fail to provide reliable contrarian signals. History has proved that the currency can decouple from rate fundamentals for extended periods without near-term mean reversion (e.g., 2018-22, Figure 5), particularly in the absence of clear PBoC guidance toward a weaker yuan. CNY FX is also less cyclically sensitive than many peers, with even pronounced misalignment versus domestic cyclical conditions not necessarily implying imminent reversal risks (Figure 6). These dynamics largely reflect China's trade-led BoP, a tightly managed capital account, and still-limited foreign participation, which dampen the transmission from macro and cyclical conditions into capital flows—especially outflows—so long as domestic weakness does not escalate into a complete confidence shock. Indeed, post-COVID-19 growth imbalances in China, with exports leading the recovery, have created a structurally supportive backdrop for CNY FX. In recent years, China's export performance has consistently surprised to the upside (Figure 7), supported by high-tech exports and emerging champions such as the “new three” (solar, EVs, and batteries), alongside favorable price dynamics. Amid the global AI cycle, Chinese tech exporters appear to be raising export prices (Figure 8), lifting nominal export growth beyond volume-based measures. Notably, export growth surprises (actual minus consensus) have closely tracked movements in export prices, underscoring the important role of pricing in shaping China's export performance.

Figure 5: CNY FX can decouple from rate fundamentals for extended periods  
R-square of out-of-sample regressions of USD/CNH vs US-China yield differentials  
![](images/abefbf734c11440242548531c4965bb4952a093b854dfb87840e9a2821be0e39.jpg)  
Source: Bloomberg Finance L.P., JPM

Figure 6: CNY's disconnect with cyclical fundamentals is not indicative of reversal risks  
![](images/82eb759b69e1e98e6fd366cbffe4a94d4f7c7d8fb562caeadae1934e50d4a18f.jpg)  
Source: Bloomberg Finance L.P., JPM

Figure 7: China's export performance has consistently surprised to the upside in recent years  
![](images/58c69809feca082afb3622f7e2a0b221eaf208a0d8ff51acc674b4fed3645056.jpg)  
Source: Bloomberg Finance L.P., JPM

Figure 8: Chinese tech exporters have managed to raise prices, contributing to headline export strength  
![](images/9d962b52cbc0d87e2ca8e420c45d80ed35b03c70584b76be0ee0448605c7ad27.jpg)  
Source: China Customs, JPM

## Export strength only translates into FX strength if exporters are actively

converting. This has been the case in China since 2025 when Chinese corporates turned from net dollar buyers to net dollar sellers, leaving it in contrast to its regional peers in North Asia where exporters' dollar income has yet to be translated into currency strength. According to SAFE's FX settlement data, Chinese corporates net sold \~\$543bn dollars since 2Q25, with the 12m run rate even outpacing that in 2021 when CNY FX also saw similar appreciation cycles (Figure 9). While the headline dollar selling has been impressively large, this needs to be put into the context of China's outsized monthly trade surplus at a monthly run rate of nearly \$100bn. Once flows are taken into account, it appears that corporates are merely converting part of their incremental trade income while the excess dollar savings that they have accumulated since 2022 during the period of CNY depreciation has yet to be offloaded in a meaningful way (Figure 10). As per our estimates, excess dollar savings accumulated by Chinese corporates since 2022 remain sizable, at around \$550bn–915bn. Even partial conversion of these holdings could exert appreciation pressure on CNY, leaving this stock of USD assets a persistent source of structural support for the yuan.

Figure 9: Chinese corporates have turned into net dollar sellers since 2H25, ...  
12m sum, \$bn, corporates net FX settlement  
![](images/5b0ce7bcb6388af701c31a1aa74fc9482c7b50f175d6f387ed43ae74d74447e8.jpg)  
Source: SAFE, JPM

Figure 10: , ... although FX conversion appears to be limited to incremental trade income, with the outsized stock of excess dollar savings accumulated in prior years yet to be meaningfully offloaded JPMe of excess dollar savings by Chinese corporates, \$bn, cumulative since 2022

![](images/48aa1875b9f40fe9471531f80be917a425092d18d0454d17f886f1e22fa67971.jpg)  
Source: JPM

While the widening goods trade surplus and increased FX conversion have drawn most attention, CNY's BoP fundamentals have improved more broadly than that.

First, China's services deficit has narrowed visibly since 2025, moving back toward the COVID-19-era lows after widening post-reopening. This largely reflects a surprisingly strong rebound in inbound tourism, now exceeding pre-COVID-19 levels following the expansion of transit visa/visa-free schemes since 2024 (Figure 11). Residents from 55 countries can now visit and stay in China for up to 240 hours under the new visa policy. This has helped to boost tourism inflows while outbound tourism has largely plateaued after its post-reopening normalization, which on net helps to narrow China's service deficit by around \$50-60bn per year.

On the capital account side, foreign portfolio inflows have also strengthened, particularly in equities, with foreign buying of onshore Chinese stocks running at the fastest pace in recent years (Figure 12). The synchronized strength in CNY and domestic equities over the past year has created return synergies that are attracting inflows. While regional funds have added exposure to Chinese stocks since 2025, global active funds remain structurally underweight, leaving scope for further inflows if/when positions neutralize further (Figure 13). Despite weak domestic cyclicals, China's positioning as a credible AI alternative play could support foreign allocation (China Equity Strategy: Unique opportunities in the China AI ecosystem).

On the bond side, while the low yield profile of Chinese bonds remains a relative drawback and a constraint on a meaningful return of foreign participation, we have seen tentative signs of a pickup in inflows in recent months (Figure 14). The resilience of both CNY FX and the bond market during recent global rates sell-offs reinforces their “safe-haven” characteristics, while low correlation with global rates enhances their appeal as a diversification asset. Looking ahead, the expected rollout of bond futures in Hong Kong and the PBoC’s FIMA repo facility—aimed at advancing RMB internationalization—could provide incremental support for foreign demand for Chinese bonds (EM Quicktake: New PBoC facilities announced at Lujiazui).

Figure 11: The accelerated growth in inbound tourism has helped to narrow China's service deficit  
R-square of out-of-sample regressions of USD/CNH vs US-China yield differentials  
![](images/f13a3d4b2539d8876b9d4056ad9c3365dcc75547e90528d0cfe20623fcc5dad1.jpg)  
Source: SAFE, JPM

Figure 12: Foreign inflows to onshore Chinese stocks have picked up  
![](images/1717088d09c16eef96f62dda4ffe976628217132494faef85167f75a123f0977.jpg)  
Figure 13: Active global funds remain UW China, preserving room for more inflows  
Source: JPM

![](images/241fe1003ec02881a6da07735a039f6f7c9b234a12bce842b546c041c5494a11.jpg)

Figure 14: Foreign demand in Chinese bonds has shown tentative recovery  
![](images/ea5f38c63f97a2f5205ed7b385d151a74b4257db9ae183db780b417325c81050.jpg)  
Source: EPFR Global (30 April 2026), MSCI (30 April 2026), JPM Equity Strategy  
Source: CFETS, JPM

2021 déjà vu? Recent CNY strength has drawn comparisons to 2021, when a similar appreciation cycle was driven by strong twin surpluses. At the time, the narrative around China exceptionalism underpinned a sustained move in USD/CNH toward the 6.3 handle. Even as the USD cycle turned bullish in 2H21, USD/CNH continued to decline—falling a further \~2.5% in the second half of 2021—despite a broader dollar rally of over 4%. While there are clear similarities, particularly in the supportive BoP backdrop, important differences point to a less organic foundation for CNY strength this time.

For one, domestic fundamentals are notably weaker nowadays. In 2021, post-COVID-19 policy easing and pent-up demand drove a strong cyclical upswing in China, with consumer sentiment rising to multi-year highs (Figure 15). In contrast, a prolonged property destocking cycle and lingering balance sheet scars among households continue to constrain the recovery in investor confidence, limiting upside in China-linked risk assets beyond selected structural themes such as AI. The external backdrop is also less supportive this time. In 2021, global monetary easing left CNY offering a positive carry of around $3\%$ , making it an organically attractive long for global FX investors (Figure 16). Today, CNY's carry profile has effectively reversed, with its low-yielding nature dampening its investment appeal. Against this backdrop, the currency's ability to sustain appreciation—particularly against a strengthening dollar—may be more limited than in 2021 and could require more active policy support from the PBoC.

Figure 15: China's consumer confidence has yet to recover consumer confidence index  
![](images/89f3c0ac08a11c8acb25c892ebe913612f55da03b8594dba3b794044cf8c20ef.jpg)  
Source: PBoC, JPM

Figure 16: The external backdrop was more favorable for CNY FX in 2021, with low global yields underpinning CNY's positive carry back then  
![](images/4bf6496c8b64ba45d7fc2d93c3aaba9f12c85f957a7485776b34c1a755d075c6.jpg)  
Source: Bloomberg Finance L.P., JPM

PBoC FX policy since 2Q25 has reflected a well-calibrated stance. On one hand, the near one-way glide in the da

[中间内容因长度限制已省略]

aterial only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
