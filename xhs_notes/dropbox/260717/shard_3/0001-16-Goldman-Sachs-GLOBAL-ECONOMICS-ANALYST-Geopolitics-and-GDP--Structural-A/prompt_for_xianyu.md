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
GLOBAL ECONOMICS ANALYST

# Geopolitics and GDP: Structural Alignment Matters More than Near-Term Risk

■ Geopolitical risks from the war in Iran have faded since March. But broader risks around geopolitical and economic fragmentation remain, with some measures signaling the lowest level of global alignment since the 1980s. In this Global Economics Analyst, we explore the impact of geopolitics on the global economy, with a particular focus on the longer-run implications for global growth.

The effects of geopolitics on commodity prices and economic outcomes are well-studied, although only a subset of geopolitical crises—typically those directly involving major oil-producing regions—have a material impact on oil prices. Outside of the commodity channel, we find that the direct impacts of geopolitical risk events have created only modest drags on growth due to increased caution from consumers and businesses. For example, a sustained increase in geopolitical risk indices as large as the spike due to the war in Iran would only subtract 0.3pp from global GDP growth in 2026-H1 (incremental to commodity headwinds) according to our estimates.

The long-run impacts from shifting geopolitical alliances are not small, however. A one standard deviation shift in country-specific geopolitical alignment toward improved relations with the rest of the world (defined by the GDP-weighted alignment to all other countries)—a shift roughly as large as during the defrosting of Chinese-western relations following Nixon's visit in 1972—adds $3\%$ to long-run GDP on the back of increased trade and investment, particularly if driven by increased alignment with western nations. We also find larger benefits in EMs than DMs, with stratified estimates suggesting that increased trade, lower resource dependence, and positive spillovers to domestic governance and institutions help EMs catch up.

One reason why shifts in geopolitical alignment lead to long-run GDP effects that build for almost a decade is that they prompt increases in trade that lead to longer-run efficiencies. We find that overall trade volumes increase following an increase in bilateral alignment, a pattern that suggests more efficient allocations of production. We also find increases in FDI and FX reserve allocations following a positive shift in alignment, suggesting that increased capital flow enhances efficiency.

\- Our results suggest that a hypothetical return to mid-2010s levels of geopolitical alignment could add up to 1% to global GDP over the remainder of the decade, with outsized benefits in EMs. In contrast, an incremental increase in

Johan Allen
+44(20)7774-7122 |
johan.allen@gs.com
GS International

Joseph Briggs
+1(212)902-2163 |
joseph.briggs@gs.com
GS & Co. LLC

fragmentation equivalent to that seen since 2016 would lower global GDP by 1% over the long run.

## Geopolitics and GDP: Structural Alignment Matters More than Near-Term Risk

Near-term geopolitical risks appear to be receding. Despite some signs of fragility, the US-Iran memorandum of understanding lays the groundwork for a gradual normalization of global economic conditions as oil flows through the Strait of Hormuz recover. But risks around broader geopolitical and economic fragmentation remain, with some measures signaling the lowest level of global alignment since the 1980s.

In this Global Economics Analyst, we explore the impact of geopolitics on the global economy, with a particular focus on the longer-run implications for global growth.

## Measuring Geopolitical Risk and Alignment

Recent academic research has focused on quantifying two distinct types of geopolitical exposures.

1. Geopolitical risk event measures capture the quantity and intensity of events such as military confrontations, political crises and diplomatic incidents. We use a recently-introduced Geopolitical Risk Index from Iacoviello and Tong (2026) $^{1}$ which analyses historical geopolitical events on a country level by applying an LLM to historical newspaper articles.

2. Geopolitical alignment measures instead quantify the relationships between nations—how aligned a country is to other states. We measure alignment using a Geopolitical Alignment Index constructed from the Global Geopolitical Events Database (GGED) developed by Fan (2025) $^{2}$ . GGED uses a web-search enabled LLM model to identify historical events between country pairs and assign scores reflecting relative alignment or misalignment. Following Fan (2025), we construct country-level alignment scores by taking GDP-weighted averages of the bilateral alignment measures.

Methodologically, the geopolitical risk event index and geopolitical alignment index are somewhat similar. Both combine media and other text to extract a signal of shifting geopolitical stances. Exhibit 1 shows the evolution of the global geopolitical risk index (intensity-weighted share of newspaper coverage devoted to global geopolitical risk) and geopolitical alignment index (GDP-weighted average of country-specific indices) since 1960. There are common trends—for example, geopolitical risks declined in the mid-1970s, around the same time that geopolitical alignment increased against the backdrop of US-Soviet détente. Most relevant for the current outlook, both measures have risen sharply since the 2010s—consistent with more geopolitical risk events and higher fragmentation—and stand close to all-time highs. Although fragmentation eased slightly since 2021, the latest alignment datapoint is 2024—before the 2025 ‘Liberation Day’ tariffs and the Iran war—and therefore fails to capture a likely incremental deterioration in alignment over the last two years.

Exhibit 1: Global Geopolitical Fragmentation Has Increased Over the Last 5-10 Years  
![](images/7d237a66cfb837b765d2b23fc7e9ed887c3c92824b58269bf4d49a2d5c2e544c.jpg)  
Source: GS Global Investment Research, Iacoviello and Tong (2026), Fan (2025)

While geopolitical risk and alignment are correlated, it is worth emphasizing that geopolitical risk is a distinct phenomenon from geopolitical alignment. This is most apparent on a national level: to illustrate, Exhibit 2 shows the two country-level indices for the UK and Vietnam (the geopolitical risk index corresponds to the intensity-weighted share of newspaper coverage devoted to UK/Vietnamese geopolitical risk; the geopolitical alignment index is defined as the GDP-weighted average of bilateral alignment between the UK/Vietnam and all other countries). In the case of the UK, Brexit led to a deterioration in overall alignment without a corresponding rise in event risk. And in the case of Vietnam, the end of the Vietnam war led event risk to decline 20 years before alignment improved.

Exhibit 2: Geopolitical Risk and Geopolitical Alignment Are Distinct Phenomena  
![](images/1635da3516349298cbab248b549bb947bc0023f6fcf15bb5068b6501c54e197c.jpg)  
Source: GS Global Investment Research, Iacoviello and Tong (2026), Fan (2025)

![](images/8ac7e127b1330c1a84b0f379f0af504298f50da174e58096ed9c87de03b5baf0.jpg)

A key differentiating factor between geopolitical risk events and changes in geopolitical alignment is their relative persistence: Individual geopolitical risk events tend to be highly salient when they occur but are most often shorter-lived. Geopolitical alignment, by contrast, is a slower yet persistent process.

To quantify this distinction, we run a local projection of the country-level geopolitical risk and alignment indices on themselves. Exhibit 3 shows that a one-unit ‘shock’ in the risk index exhibits some persistence but falls sharply within two years and subsides after five. A one-unit geopolitical alignment shock endures far longer, fully receding only after roughly 14 years. Wars, acts of terror and threats of interstate violence are deeply disruptive—but are fortunately usually measured in days, months or at most years—whereas the strengthening and deterioration of relations between nations is a gradual process that unfolds over decades.

Exhibit 3: Geopolitical Risk Shocks Fade Quickly, but Changes in Geopolitical Alignment Are Much More Persistent  
![](images/fe5c91b0d9ed9f80a5f3d3c20926b5725ad000e7a1c3d73b281b173b025d6372.jpg)  
Source: GS Global Investment Research, Iacoviello and Tong (2026), Fan (2025)

## The Short and Sharp Impact of Geopolitical Risk Events

Many well-known geopolitical crises—the 1979 Iranian revolution, Russia’s 2022 invasion of Ukraine and the ongoing Iran war—hit the global economy primarily through one channel: commodity market disruptions that pushed up commodity prices. We have previously highlighted our rule-of-thumb that a 10% rise in oil prices lowers global GDP by approximately 0.1%, implying that the Hormuz closure has erased roughly 0.3% from global GDP this year. Yet most geopolitical risk events—for instance, the Falklands war, the 1999 NATO bombing of Yugoslavia and the 2025 announcement of US tariffs—have nothing to do with oil. A simple scatter plot of the Geopolitical Risk Index against the one-month change in global oil prices shows no relationship (Exhibit 4) $^{3}$ .

Exhibit 4: We Often Focus on Commodity Price Impacts of Geopolitical Shocks, but the Response of Oil Prices to Geopolitical Events is Surprisingly Weak

![](images/1491fa53b1816336a39af551d64f5c37fa007394c9e5a83acc81c6b1a117dfbf.jpg)

To estimate the direct short-run effects of geopolitical events on global GDP—due to precautionary saving, delayed investment and risk-off capital outflows, but excluding oil—we run a panel local projection of country-level geopolitical risk indices on quarterly GDP growth, controlling for oil prices. A one standard deviation rise in the index—an increase roughly as large as the one that occurred in China following the announcement of tariffs in early 2025—tends to lower country-level GDP growth by 0.2pp in the affected quarter and by a further 0.1pp the following quarter, before the effect subsides (Exhibit 5).

The drag is materially larger in Emerging Markets than in Developed Markets, likely because EMs are more vulnerable to risk-off capital outflows. The key takeaway from these patterns is that growth drags are generally small and only temporary. The global geopolitical risk index was 30% higher in 2025-H1 compared to 2024-H2, implying that global growth in Q1-Q2 was approximately 0.3pp lower than in a counterfactual without the Iran war, with some recovery likely in H2 on the back of the recent normalization in risks.

Exhibit 5: Geopolitical Risk Events Have a Short-Run Impact on Real GDP Growth (Incremental to Commodity Price Effects)...  
![](images/e28c38aa3aee58722898d288a109efd964f55ed1b461dfa1a3a213efe48aeb4a.jpg)  
Source: GS Global Investment Research, Iacoviello and Tong (2026)

## The Larger Long-Term Consequences of Geopolitical Alignment

Geopolitical alignment shapes economic activity over a far longer horizon. To demonstrate, we run a set of local projections that exploit country-level changes in the GDP-weighted average of bilateral geopolitical alignment indices on annual GDP, while also controlling for country and time fixed effects (we include separate time fixed effects for DMs and split EMs by the seven World Bank regions). The resulting estimates therefore capture the effect of a one standard deviation shift in a specific country's alignment with the rest of the world, holding alignment for all other countries fixed. Causal identification is admittedly difficult—economic progress could lead to an improvement in alignment, while not all alignment shifts will necessarily generate significant economic benefits—but idiosyncratic time variation in alignment likely provides useful insight into the impact on GDP.

We find that a one standard-deviation $^{4}$ increase in country-level geopolitical alignment raises the level of GDP by approximately 3% over seven years for the average country in our panel. This effect is large but generally follows from material shifts in alignment—an alignment shock of this magnitude would roughly correspond to the shock that occurred to China after Nixon visited in 1972 or the shift in Iran's alignment after it signed the JCPOA in 2015 $^{5}$ .

While the estimated impact on GDP is large, it aligns with a growing body of economic literature that finds large effects of alignment on economic activity. As examples, 1) Fan (2025) finds that a one-standard deviation permanent shift in alignment raises GDP per capita by 10% over 25 years, 2) Fan Wo and Xiang (2026) find that a similar shift in

alignment boosts bilateral trade by 20% over 10 years, 3) Shan and Tilton (2024) find that the US does not trade much with or invest in countries that are geopolitically distant, though China has close trade and investment relationships with both geopolitically close countries and many countries that are geopolitically more distant. 4) Gopinath Gourinchas Presbitero and Topalova (2024) find that trade and FDI flows across misaligned blocs have declined by 12% and 20% more than flows within the same bloc since the start of the war in Ukraine, 5) Javorick Kitzmuller Schweiger and Yildirim (2024) find that reversing recent alignment trends and economic integration could subtract 4.7% from GDP. Additional research highlights the importance of geoeconomic power and pressure in explaining long-run economic dynamics, suggesting that such forces are increasingly recognized as an important driver of long-run activity.

Exhibit 6: ...Whereas Geopolitical Alignment Effects Have a Long-Run Impact on GDP  
![](images/c98df0040de5b32cd458c283fe1b4fd8e77c852a8ea8d1de209019f92f5d885d.jpg)  
Source: GS Global Investment Research, Fan (2025)

What drives this increase in GDP? Rerunning our model to estimate the impact of country-level changes in the GDP-weighted average of bilateral geopolitical alignment indices (i.e., alignment with the rest of the world) on the subcomponents of GDP reveals three channels. First, fixed investment rises the most, as improved relations widen access to global capital markets and lower the risk of domestic investment for local and international investors alike (Exhibit 7). Although investment may also rise in response to a deterioration of bilateral relations—through channels such as higher domestic defense expenditure, the nearshoring of supply chains and higher domestic energy infrastructure construction—our results suggest that larger longer-run investment gains accrue from an improvement, rather than a decline, in geopolitical alignment. Second, exports rise as improved alignment lowers trade barriers and deepens bilateral commerce. This effect is more pronounced for smaller economies—re-estimating our model only on the largest economies shows a smaller (though still significant) contribution from exports. Third, household and government consumption also rise, though by less than overall GDP, likely as a second-order effect of stronger investment and trade.

Exhibit 7: The Positive GDP Impacts from Increased Geopolitical Alignment Comes Mostly From Increases in Investment and Trade  
![](images/2ee05719519f3adf613c5857fa607c8d2e2da5eedf4593a83346119d6737a294.jpg)  
Source: GS Global Investment Research, Fan (2025)

Given the importance of the investment and trade channels, it is unsurprising that emerging markets see materially larger gains from improved geopolitical alignment compared to developed markets (Exhibit 8). Stratifying our results suggests two further reasons. First, closer alignment helps EMs move away from a resource-extraction model and its associated volatility. Second, effects are larger for countries with weaker domestic institutions and governance, suggesting closer alignment with other countries generates positive spillovers beyond direct economic channels.

Exhibit 8: Less-Develo

[中间内容因长度限制已省略]

ttempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints.

As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
