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

Figure 12: Foreign inflows to onshore Chinese stock

[中间内容因长度限制已省略]

of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
