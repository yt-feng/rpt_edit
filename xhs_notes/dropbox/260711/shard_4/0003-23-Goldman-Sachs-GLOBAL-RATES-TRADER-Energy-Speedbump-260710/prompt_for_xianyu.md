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
GLOBAL RATES TRADER Energy Speedbump

AI issuance and capex remain the structural focus for markets, but oil reemerged as the main driver of rates volatility this week. Long-end valuations are no longer rich in the US, and the investment backdrop should be a factor keeping yields higher, but there's little to suggest meaningful risk premium versus what macro and fiscal fundamentals imply. Near-term oil dynamics will likely dictate asymmetry around CPI, but our economists' benign expectations for the print can allow front-end risks to compress. The sell-off in European and UK front-end rates is a reminder that stalling on the progress of disinflation presents some risk for long positioning. We think that ECB pricing will oscillate around one hike, and prefer 1y1y for longs on the curve. In the UK, despite the risks to the front-end we continue to think the 2s10s curve will steepen in coming months. Greater GPIF demand could support JGBs from an NIIP perspective, but would likely fall short of addressing the underlying macro disequilibrium that has fueled JGB volatility this year.

## United States and Canada

Recent rate vol more oil than issuance. Renewed escalation of the US-Iran conflict at least temporarily restored energy as the common global factor for markets, with US yields trading in relative lockstep with oil prices over the middle of the week (Exhibit 1). The larger sell-off further out the curve in the context of continued elevated corporate supply at the start of a typically quieter issuance period has helped to increase focus on the impact of AI-related borrowing on the broader level of yields. While the focus is understandable, and we have argued previously that a debt financed investment cycle should put upward pressure on yields, we would note the recent rebound in longer-term yields has taken US forwards from levels that were slightly rich to about fair. To the extent that rising borrowing is financing investment that is in turn boosting future growth expectations and adding to cyclical pressure, it should push our estimates of fair value higher. However, we think the lack of clear dislocation between the level of longer-term yields and what macro and fiscal fundamentals imply undercut the notion that the level of corporate borrowing is playing an outsized role in driving Treasury valuations. Fed officials' ongoing focus on the inflation side of the mandate puts the spotlight on next Tuesday's June CPI release. Energy prices will have some bearing on the degree of asymmetry surrounding the print, with higher oil leaving markets more vulnerable to a firmer print. That said, we think realizing our economists' projections for a $0.17\%$ increase in core CPI alongside a

George Cole  
+44(20)7552-1214 |  
george.cole@gs.com  
GS International

William Marshall +1(212)357-0413 | william.c.marshall@gs.com GS & Co. LLC

Simon Freycenet  
+44(20)7774-5017 | simon.freycenet@gs.com GS Bank Europe SE - Paris Branch

Isabella Rosenberg +1(212)357-7628 | isabella.rosenberg@gs.com GS & Co. LLC

Friedrich Schaper +1(917)343-3214 | friedrich.schaper@gs.com GS & Co. LLC

Loic Mathys +44(20)7051-1664 | loic.mathys@gs.com GS International

0.11% decline in headline CPI should compress the distribution of risks around front-end rates and erode hike pricing. With about 45bp of hikes priced through early-27 and Fed uncertainty premium already embedded in upper left vol, we think limited downside distributional structures that position for an on-hold Fed are sensible carry expressions here.

Front-end uncertainty a headwind to bill valuations. 1-month bills remain well-supported, reflecting a period of seasonally low bill supply, favorable funding conditions and solid MMF AUM growth. At the same time, 3m and 6m bills have underperformed the very front-end as MMF WAM has skewed shorter (Exhibit 2), also reflected in modestly higher primary dealer take-up at auctions for term bills. We think higher policy uncertainty as the Fed's leadership redefines how much guidance to give around its reaction function is likely to keep WAM shorter for now, and 1m bills relatively rich. Our Bills-OIS valuation framework suggests that one day shorter WAM translates into \~0.1bp cheaper 3m/6m bills vs OIS, but richens 1m bills by 0.3bp. Heavier bill supply throughout the summer could also provide a headwind to valuations. But with money fund AUM expected to continue to grow given elevated policy rates and a generally flatter curve, and the cautious tone by SOMA Manager Perli likely indicative of greater willingness to wait before further slowing the pace of RMPs, we expect cheapening pressure in 3m and 6m bills to remain somewhat contained.

Exhibit 1: US yields traded with oil prices for much of the week  
![](images/28b7e5e9c4c3b3d07e2ea739ae2b438ead5b8abed56bbebab79f00681d3026b2.jpg)  
Source: GS Global Investment Research, Bloomberg

Exhibit 2: Term bills have cheapened vs OIS relative to shorter term bills as MMFs skewed their WAM shorter  
![](images/c5682b61dde32839f17f707f495a6ec459a0ba64315c9a4433d5d7b31f848675.jpg)  
Source: GS Global Investment Research, GS FICC and Equities, Crane Data

Dollar strength still a drag on foreign official demand. Dollar strength remains a drag on foreign official Treasury demand, with both TIC and New York Fed custody holdings data pointing to continued net selling of USTs (Exhibit 3). That said, the selling pressure has had a limited impact on the broader market. Our FX strategists recently revised their Dollar forecasts stronger, suggesting Dollar performance may continue to weigh on foreign official demand. While those forecasts are differentiated across low- and high-yielders, we find little meaningful difference in foreign official UST flows based on the source of Dollar strength or weakness; typically, the broader Dollar backdrop matters most. As we have written, Dollar performance is a key driver of foreign official Treasury demand, and with sustained, broad-based depreciation unlikely to return for some time, this demand may stay soft. However, a lower vol environment for the Dollar should keep outright selling contained.

No clarity, no outlook change for BOC after USMCA. The decision to annually review the terms of USMCA seems to have dispelled some of deeper escalation concerns without offering much certainty around the Canadian outlook, leaving lingering trade policy concerns. With little additional clarity, our economists think this most likely keeps the BoC on hold next week and throughout this year. The BoC's Business Outlook Survey reflected a still soft underlying activity picture, but businesses also seem to be acclimating to a new normal rather than expecting further trade relief, while expectations on investment and the AI build-out also point to some optimism and the labor market appears to have stabilized. We think this should continue to push the CAD curve steeper, as markets focus on an eventual normalization (which our economists expect in 2H27). Following recent performance, we close our 2s5s steepener recommendation for a potential profit of 9bp incl carry and shift it out to 2s10s steepeners (Entry: 53bp, Target: 80bp, Stop: 40bp). We expect the underperformance to be led by 5y5y and think front-end pricing can decay over time (Exhibit 4).

Exhibit 3: The decline in foreign official holdings has tracked the strengthening of the USD  
![](images/adabc58c1db6e718e9568c0c38d7f695f7e63af5be3fdd94304cb0c265393983.jpg)  
Source: GS Global Investment Research, Haver Analytics, NY Fed

Exhibit 4: We expect underperformance to be led by 5y5y part of the CAD curve  
![](images/25069866b88340450fc3816b2cfec5e088cc911c9c958b8d416339e7a4422a92.jpg)  
Source: GS Global Investment Research, GS FICC and Equities

## Europe

Speed bumps on the decline in European vol. The rally in European front-end rates ended abruptly this week as renewed strikes in Iran pushed energy prices higher. The emerging narrative was that the ECB may pass on future hikes, but with elevated volatility in energy markets, limited relief in refined products and ongoing upside risks to European gas prices, suggests that pricing in Z6 will oscillate around one more additional hike in September (our economists' base case). Even as the ECB is unlikely to hike in a way designed to tighten financial conditions materially, we continue to think there is more value in front-end flatteners, with about 15bps of hikes priced between October and June next year. Flattening exposure can work across a range of scenarios. A re-escalation in Iran would likely see markets pull forward hike pricing and place less relative weight on projection meetings. At the

same time, there is limited steepening risk given a gradual decline in inflation risk would erode cumulative hike pricing including to terminal rates. The main challenge to this view is that elevated long-end yields naturally bias the curve steeper via bear-steepening risk – for this reason we recommend pairing front-end flatteners vs short 2y2y rates. Or equivalently we believe EUR OIS 2y2y vs 1y1y steepeners offer good risk-reward in a world of steeper global curves.

OAT weakness on French elections premature. European sovereign spreads have widened in recent weeks, and we recently hit the (tight) stop on our 3y BTP, Bono, OAT long vs OIS recommendation, which we've closed for a small potential gain from carry. This week French political focus and renewed front-end volatility have added to these headwinds, however we expect both to subside in coming months. As above, the ECB is likely to hike again but inflationary pressure does not appear high enough for future hikes to be designed to restrict growth, which reduces the risk to sovereign spreads. We also believe the hurdle is high for the market to stay focused on French politics this far away from the presidential elections. The RN Marine Le Pen's decision to run despite her conviction and to appeal her verdict may increase uncertainty around the RN's future policy platform, but at this stage of the campaign, polls are still imprecise and economic platforms have yet to be fleshed out. We also think differences in sensitivities between the RN candidates are small compared to the scale of France's fiscal challenges. Taken together, we think that means risk-reward is poor for shorts in OATs given the premium already priced and think that carry will continue to dictate returns over the coming months.

Euro-area money market crunch getting closer. At a high level, we continue to think that Euro-area banks are adjusting smoothly to a lower liquidity environment. Borrowing at the ECB remains muted, but as liquidity continues to drain this may change in coming quarters. The number of bidders at the ECB's regular tenders has picked up, and an increasing number of bank treasurer report reserves are getting closer to their preferred level. A higher minimum reserve requirement (MRR) would reduce the level of excess liquidity, potentially leading to an increased demand for funding given the uneven distribution of reserves across the Euro area. We expect the liquidity drain to exert only a gentle pressure on money market rates and bases, however. The main reason for this is that we think broader conditions are not in place for a sharp widening; narrow spreads between financials and non-financials suggests bank credit risk is seen as low and macro-economic uncertainty is likely to trend lower. Against this, our empirical work suggests front-to-belly ESTR-BOR bases screen fair and are likely to widen only gradually over time (Exhibit 5).

Exhibit 5: Our analysis points to a modest widening pressure on ESTR-BOR basis  
![](images/f94e79748d41e5deaa00c8fa190265eda4f1083fe942c5eefce979ca6eab0fb9.jpg)  
Source: GS FICC and Equities, GS Global Investment Research

UK front-end reprices on energy, but should rally back. Limited data and central bank guidance this week left the UK front-end to respond to the repricing higher in energy prices. We think the front-end sell-off was likely exacerbated by long positioning, but is a reminder that stalling progress on energy relief remains a source of risk for BoE pricing. Nonetheless, we continue to think that the UK curve will continue to steepen as the hurdle for BoE hikes is unlikely to be met, but longer-run fiscal challenges will remain. Sticky risk premium is better expressed in curve trades than in Gilts on asset swap, in our view. Adjustments to the leverage ratio should create a modest tailwind for Gilts, by freeing up around £150bn of balance sheet capacity by our banks team estimates. At the current share of bank Gilt holdings, this would translate to a £2-3bn increase in Gilt holdings which is unlikely to make a difference to the level or relative yield on Gilts. But the indirect effect via the extension of leverage to the broader financial system offers more support, with carry on long Gilts on asset swaps offering reasonable risk reward in the 5y and 10y parts of the curve.

## Japan

JGBs still on a steepening path. 10y and 30y JGBs rallied close to 10bps following comments from Finance Minister Katayama suggesting that the government is “looking to pursue measures to encourage pension funds, including GPIF, to make further investments in Japanese financial assets.” GPIF currently holds about 26.9% of its assets in domestic bonds, slightly above the target allocation of 25%, but well within the +/-6pp deviation limit. Last week, GPIF President Uchida stated that the fund would not change its strategic asset allocation in response to short-term risk factors given solid performance; its domestic bond portfolio returned -5.1% versus sizable gains across domestic equities and foreign equities and bonds. While greater GPIF demand could support JGBs from an NIIP perspective, we are skeptical that it would fully address the underlying macro disequilibrium. Critically, most of this year’s cheapening in JGBs appears to have been macro-led rather than a function of supply/demand imbalances—long-end swap spreads have widened this year, likely supported by renewed buying from Lifers, but 30y bonds have still cheapened. From that perspective, a shift from GPIF would be more likely to support 30s, which saw the brunt of the supply-led cheapening last year, but may have less impact further in on the curve where macro volatility has become increasingly dominant of late. Other reports this week that the Takaichi administration added a reference to “inflation stabilization” in the Basic Policy to ease concerns about its stance on BoJ independence garnered minimal reaction from JGBs. Fiscal dominance concerns have continued to see the curve steepen in Japan in contrast to the rest of G3, where curves have mostly flattened year-to-date, with the long-end underperformance not counteracted by easing in inflation pricing following the US-Iran MOU. In fact, 2s10s and 10y traded inflation have begun to decouple, suggesting that broader (not just inflation) risk premium is still on the rise (Exhibit 6). Through this, JPY has continued to weaken, and our FX strategists have revised their forecasts to show a JPY weakening trend over the next 12 months. Intervention remains likely and could exacerbate volatility in JGBs as limiting JPY depreciation necessarily means rates become the pressure release valve in markets. Provided fiscal dominance concerns remain in focus, the market seems likely to continue loading risk premium into the long-end, with the release of the Basic Policy this month a key focus.

Exhibit 6: JGB curve steepening and inflation pricing have started to decouple  
2s10s JGB curve vs 10y JPY inflation swap  
![](images/8f771b5b29cfdae291fe7423f5cc602b7394fb20dd4b11afaf7d3384926c4089.jpg)  
Source: GS FICC and Equities,

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
