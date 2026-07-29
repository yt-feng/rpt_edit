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
CHINA MUSINGS

# Investor FAQs on Large-Scale IPOs

ChangXin Memory Technologies (CXMT), a Chinese DRAM maker, completed its primary listing on Shanghai Stock Exchange's STAR market on July 27, raising US\$8.6bn (US\$9.8bn if incl. greenshoe) in IPO proceeds. In this China Musings, we address investor FAQs related to large-scale IPOs.

Kinger Lau, CFA
+852-2978-1224 | kinger.lau@gs.com
GS (Asia) L.L.C.

Timothy Moe, CFA
+65-6889-1199 | timothy.moe@gs.com
GS (Singapore) Pte

1. CXMT's IPO in a historical context? At US\$8.6bn offer size and US\$484bn market cap (based on 27 July 2026 close), it is the largest A-share Tech IPO, the 4th largest (in USD terms) in A shares, and it ranks the 2nd largest in the aggregate China equity universe by total market cap.

Si Fu, Ph.D.
+852-2978-0200 | si.fu@gs.com
GS (Asia) L.L.C.

Kevin Wang, CFA
+852-2978-2446 | kevin.wang@gs.com
GS (Asia) L.L.C.

2. How did large IPOs trade in the past? $30\%+$ 1D and 1M returns on average for the top-50 largest Chinese IPOs, but with high market and sector variations.

3. Historical performance of large IPOs? Headline indexes tended to weaken before but recover shortly post the issuances. The V-shaped pattern is more pronounced in A shares, likely due to strong retail participation there.

4. Sentiment boost or liquidity drain for sector peers? Listed comparables of new IPOs typically traded sideways before but traded better after the event.

5. Macro and market liquidity implications? Liquidity often tightened 2 weeks ahead of the listing dates, and cash turnover usually rose post the transactions.

6. Fast-track inclusion? Per SSE's index methodology, a newly listed large-cap company could be eligible for fast-track inclusion to the STAR50 Index in 1–3 months, but may require 12–18 months for MSCI China/CSI300 inclusion.

7. Pro-forma index weights and potential flows? We estimate that CXMT with a market cap of US\$484bn (as of July 27 close) would represent approximately 7% of the STAR50 Index upon its initial inclusion. Moreover, our analysis suggests a hypothetical company with a market cap of US\$400-600bn could potentially lead to US\$12-17bn of passive buying cumulatively by 4Q27.

8. US sanction risks? Designation on the 1260H CMC list by itself doesn't prevent US persons from trading a company's securities.

9. What's next for China IPO market? It will likely stay active, with US\$30bn and US\$33bn of new IPO supply in A and H shares in 2H26 on GS forecasts.

10. Strategy? We screen for (1) GS Buy-rated names in AI Hard Tech and Semi cohort for a potential V-shaped recovery trade; and (2) existing index constituents that might experience passive index selling.

## 1) CXMT's IPO in a historical context?

\- ChangXin Memory Technologies (CXMT), a Chinese memory chipmaker which accounted for about 8% of global DRAM market share as of 4Q25, completed its IPO on the Shanghai Stock Exchange's STAR market on July 27, raising US\$8.6bn (potentially US\$9.8bn with greenshoe) in IPO proceeds.

On its debut listing day (July 27), CXMT (688825 CH) traded to Rmb49.00 (+466%) compared to its IPO offer price of Rmb8.66. It's worth noting that, per the trading rules by the SSE, new IPOs on STAR Board are not subject to any daily price caps in their first 5 days of listing, but a $+/-20\%$ daily limit will apply thereafter.

At US\$8.6bn realized fund raising (ex-greenshoe) and US\$484bn market cap (as of July 27 close), the listing is the largest A-share Tech IPO, and the 4th largest in the A-share market since 1990 (in USD terms). It is also the largest company by market cap in A shares, and the 2nd largest across the aggregate A, H, and ADR universe.

Exhibit 1: Top-50 Chinese IPOs across the 3 major listing locations in the history of Chinese equities  
![](images/d9b0ee8241a80c927ded5ec3c566468161cb81d9320278ad380245c78b2469f4.jpg)  
Source: Bloomberg, Factset, compiled by GS Global Investment Research

## 2) How did large IPOs trade in the past?

Using the top-50 largest IPOs in China onshore and offshore markets (22 A shares, 27 H shares and 1 ADR) historically as our study universe, we note that they generally performed well immediately post their debuts, gaining $34\%$ on day 1 and $31\%$ over the first 21 trading days on average (vs offer prices).

They also tended to outperform their local benchmarks shortly after their debuts, posting average 1-month excess returns of $49\%$ in A shares and $18\%$ in H shares.

The return divergence is nevertheless fairly significant along various vectors, with A-share listings typically outperforming the offshore deals, and Healthcare IPOs lagging from a sector standpoint.

Exhibit 2: On average, large-scale Chinese IPOs tended to perform well post their listings  
![](images/3b1a49818f228f14e58d1d7bf8ff1169b9b93bfd8a311f5344cd10b3c64890ea.jpg)  
Source: Wind, Bloomberg, Compiled by GS Global Investment Research

Exhibit 3: Large IPOs usually outperformed their local benchmarks, posting an average 1-month excess return of 49% in A shares and 18% in H shares  
![](images/745a8f83929be47adb368c3b7dec930499b42ce0ea6a519b4602c497cde2b547.jpg)  
Source: Wind, Bloomberg, Compiled by GS Global Investment Research

Exhibit 4: Significant post-listing return disparity of large IPOs across sectors  
1-month post-IPO returns of top 50 Chinese IPOs  
![](images/80343d9819f56ac95c256baf5f4aa01990599dd65c07ec9a96c145e836ea5418.jpg)  
Source: Wind, FactSet, Compiled by GS Global Investment Research

3) Historical performance of large IPOs?

In our top-50 largest Chinese IPOs universe, the A-share index benchmark (CSI300) tended to trade softly (-2% on average) and underperform the regional benchmark (MXAPJ) by around 1% around one week before the new issuances. However, the index usually reversed the short-term weakness thereafter, recovering 2% 1 week after the events.

The pre-listing weakness seems less pronounced in Hong Kong as the market was mostly flat or range-trading before the issuances, and importantly, the benchmark often traded well after the listings as those large deals could sometimes be seen as a sentiment and liquidity boost.

The tactical ‘V-shaped’ pattern for A shares at the index level, possibly due to strong retail participation there, could weaken somewhat given regulatory reforms and IPO pricing liberalization/enhancements that have been made in the past decade. For instance, the requirement of 100% capital lock-up equivalent to individual investors’ full IPO subscription amount was scrapped in 2016 and the implicit IPO valuation pricing cap of 23x trailing P/E was also removed in 2023, both likely reducing and helping smooth the liquidity impacts of large IPOs than would otherwise be the case, in our view.

Exhibit 5: A clear “V-shaped” pattern around the issuance dates of large IPOs in the past  
![](images/bd2ab58d3c494d3a2a3c427ce8168ca3f4f89923db210f0a7996de12e2901245.jpg)  
Source: Factset, Bloomberg, Compiled by GS Global Investment Research

Exhibit 6: HK market tends to trade well post large IPOs  
![](images/7043b1ef30f2e90606a8be8f76222353de64e1b3651c7e8f4fe6c81e14019cf1.jpg)  
Source: Factset, Bloomberg, Compiled by GS Global Investment Research

## 4) Sentiment boost or liquidity drain for sector peers?

\- Focusing on the sectors to which the IPOs belong, we observe that existing (listed) comparables often traded sideways or gave up previous gains 1 month before large IPOs’ debut in both A shares and in Hong Kong. However, contrary to common perception that they could be taken as funding sources for the new IPOs, the sector peers usually managed to hold up well before the new listings came to the market.

It's also noteworthy that, similar to the V-shaped trading pattern at the index level, the sector peers tended to trade better post the event, gaining $2 - 3\%$ on average one month after the IPOs' debut for offshore listings, although the positive spillover effects in A shares were less noticeable. This suggests to us that successful listings could be regarded as a market-clearing event and generally boost overall sector sentiment, everything else being equal.

Exhibit 7: Large IPOs usually boded well for their sector peers in the offshore market  
![](images/3ffa82c9a0da7551abd17c0c4dbdc879fb6469777760df01fab701f4e3a9a8ae.jpg)  
Source: Factset, Compiled by GS Global Investment Research

5) Macro and market liquidity implications?

On interest rates, we note that front-end proxies such as the 7-day REPO and 1-month HIBOR often increased in the lead-up to the large IPO issuances, peaking around 2 weeks before the actual listing dates. This may reflect the temporary liquidity tightness due to the capital lock-up in the IPO subscription process. However, the situation usually eased shortly after the listings as (excess) liquidity returned to the inter-bank system in HK where the aggregate balance tended to rise with stable HKD spot exchange rates.

The easing in macro liquidity conditions often resulted in noticeable improvements in market liquidity and appetite for equity allocations, with cash turnover in both A shares and HK markedly strengthening and domestic A-share active funds raising equity exposures by as much as 1pp post the issuance dates.

Exhibit 8: Front-end rates usually rose ahead of large-scale IPO listings  
![](images/860120dcb56d591ddd60024aec75962126c9b4d1e384749fe175535f78fba34c.jpg)  
Source: Wind, Compiled by GS Global Investment Research

Exhibit 9: Macro liquidity often eased after large-scale IPO listings in HK  
![](images/773dbd95eee9d8995dbef26f2e1495b2b2db91b836c0fcd8ae7ec88c936b6b6c.jpg)  
Source: Bloomberg, Compiled by GS Global Investment Research  
Exhibit 10: Market turnover usually strengthened post significant A-share IPO listings

![](images/85d66393818f12e55778dab3810000282278a2ffe4fe456163d7cf5831661584.jpg)  
Source: Bloomberg, Compiled by GS Global Investment Research

Exhibit 11: Onshore mutual funds' allocation to equities often increased post large-IPO listings  
![](images/2452def391bac3e435b12f84943d89cc58c1c5665eb695a6b4a9a31054216c9b.jpg)  
Source: Wind, Compiled by GS Global Investment Research

## 6) Fast-track index inclusion?

Based on the latest index methodology published by the SSE, a newly listed large-cap company could be eligible for fast-track inclusion to the STAR50 Index as early as 1 month post-listing, subject to the approval by the Index Advisory Committee and other market cap requirements (top-3 by total market cap on the STAR board). For sector-specific benchmarks, such an issuer could potentially be added to the STAR Chip and CNI Chip Index during the next scheduled index rebalancing, typically within 1-2 quarters post listing.

Inclusion to the SSE A-Share Index is a pre-condition for Northbound Stock Connect eligibility for non-A+H dual listings. If the newly listed company ranks in the top 10 by market capitalization on the SSE, it could be fast-tracked into the index within 3 months of listing, thereby paving the way for Northbound Connect inclusion shortly thereafter. Otherwise, under the standard 1-year listing history rule, it would be added to the SSE A-Share Index 12 months post-listing and gain Northbound eligibility in the subsequent month.

As Northbound eligibility is a prerequisite for MSCI inclusion for A-shares, the company might be eligible for MSCI addition in the following quarter index review if it achieves its Northbound status as discussed above.

For broad-market benchmarks such as the CSI 300 and CSI A500, STAR board constituents are generally subject to a 1-year listing history requirement. Hence, a newly listed STAR board company could be added to these indexes during the first semi-annual index review following its one-year listing anniversary.

Exhibit 12: Fast-Track index eligibility and entry criteria for newly listed large-cap companies on the SSE STAR Board

<table><tr><td></td><td>Index Name</td><td># constituents (current)</td><td>Passive tracking AUM (US$bn)</td><td>Eligible for fast track inclusion</td></tr><tr><td rowspan="9">Onshore Index</td><td>STAR50</td><td>50</td><td>24.7</td><td>Top 3 by mkt cap: 1-month listing history^Top 5 by mkt cap: 3-month listing history</td></tr><tr><td>SHCOMP</td><td>2224</td><td>3.6</td><td>Top 10 by mkt cap: 3-month listing historyOthers: 1-year listing history</td></tr><tr><td>SSE50</td><td>50</td><td>4.6</td><td>-</td></tr><tr><td>SSE A-Share</td><td>2284</td><td>-</td><td>Top 10 by mkt cap in SSE: 3-month listing historyOthers: 1-year listing history</td></tr><tr><td>CSI300</td><td>300</td><td>49.0</td><td>STAR Board: 1-year listing history</td></tr><tr><td>CSI A500</td><td>500</td><td>29.9</td><td>STAR Board: 1-year listing history</td></tr><tr><td>STAR Chip</td><td>50</td><td>12.2</td><td>Top 5 by mkt cap: 3-month listing historyOthers: 6-month listing history</td></tr><tr><td>CSI Chip</td><td>50</td><td>1.4</td><td>STAR Board: 1-year listing history</td></tr><tr><td>CNI Chip</td><td>30</td><td>6.1</td><td>Top 3 by mkt cap: 3-month listing historyOthers in STAR Board: 1-year listing history</td></tr><tr><td colspan="2">Northbound Connect</td><td>3265</td><td>-</td><td>Prerequisite: SSE A-Share Index inclusion + Avg mkt cap&gt;Rmb5bn &amp; liquidity criteria (for non A+H, non WVR)</td></tr><tr><td rowspan="2">Offshore Index</td><td>MSCI China</td><td>576</td><td>203.8^^</td><td>Prerequisite: Northbound Stock Connect eligibility</td></tr><tr><td>MSCI China A</td><td>410</td><td>103.5</td><td>Prerequisite: Northbound Stock Connect eligibility</td></tr></table>

Note: ^Under the SSE STAR 50 Index methodology, newly listed companies ranking in the top 3 by daily average market capitalization since their IPO can be fast-tracked for inclusion after 1 month of trading, subject to formal review and approval by the Index Advisory Committee; ^^The passive tracking AUM for MSCI China includes both direct index-tracking assets and the pro-rata portion of passive assets tracking broader regional and global benchmarks—such as MSCI ACWI, EM, AEJ, and APJ—calculated based on China's respective weight in those indices.  
Source: MSCI, HSI, SSE, FactSet, GS Global Investment Research

## 7) Pro-forma index weights and potential flows?

Large-cap IPOs generally represent smaller weights in the benchmark indices initially, before growing as more shares are floated. Based on CXMT's current market cap of US\$484bn (as of July 27 close), we estimate that the company would represent approximately 7% of the STAR50 Index upon its initial inclusion. Thematically, this addition would modestly raise the STAR50 Index's Hard Tech exposure by approximately 1 percentage point (from 94% to 95%), further cementing the benchmark's status as a leading proxy for AI Hard Tech and semiconductor/memory industries.

\- With more than Rmb177bn/US\$26bn AUMs across active and passive strategies and mandates tracking STAR50 as the underlier, we calculate that inclusion of a hypothetical company with a US\$400-600bn market cap could result in it receiving US\$1.9-2.5bn assuming its free float reaches 30%.

Moreover, such a hypothetical company would account for approximately 3.0%-4.6% of the CSI300, 1.0%-1.4% of the MSCI China, 5.5%-8.3% of the MSCI China A, and 10.0% (maximum index weight for STAR50 constituents) of the STAR50 Index assuming it reaches a free float ratio of 30% by the end of 2027 following inclusion to these indexes. This would in turn result in around US\$12-17bn of potential passive inflows for the stock cumulatively by 4Q27, ceteris paribus.

Exhibit 13: The addition of a large-cap semiconductor company to STAR50 would further cement its status as a leading Chinese “Hard Tech” proxy  
![](images/ccf08e11496872406d647c46f32f23f2a5e44557ad8c151e031990869dd84bf1.jpg)  
Source: Wind, F

[中间内容因长度限制已省略]

ttempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g.,

marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
