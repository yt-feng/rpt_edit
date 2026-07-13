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

# Rotation Temptation

1. We recently held extensive investor meetings in Asia and the Americas, with client conversations centering on: a) the substantial underperformance of H vs. A shares and other regional peers ytd; b) the potential and possible timing for a leadership shift from A to H shares, or from Hard to Soft Tech; c) the reasons for disappointing earnings by listed Chinese companies and the drivers for a profit turnaround; d) are A-share AI stocks overheated? e) investor flows and positioning in Chinese stocks vis-a-vis other North Asian markets; f) the impacts of an active IPO pipeline on market returns and liquidity; g) AI developments in China, and the investment strategy within the Chinese AI ecosystem; and; h) how to make generate returns in 2H26, especially in the non-AI universe?

In this China Musings, we summarize investor feedback/FAQs and our refreshed views on these subjects, reiterate our broad A over H (Hard vs. Soft Tech) tactical preference, emphasize our high-conviction thematic ideas such as GS Select AI Portfolio and GS 15FYP Portfolio, but would start scaling into select Soft Tech/Internet proxies in H shares post their de-rating and in anticipation of their earnings recovery in the months ahead.

2. Extraordinary gains and dispersion of Asian equities. The return dispersion across the region and within the Chinese equity universe has been a subject featured in all of our client conversations. The impressive ytd gains in Korea and Taiwan, propelled by memory, foundry, and AI infrastructure plays, are well recognized and appreciated by international investors, but the equally significant divergence between A and H shares, and in similar vein, the wide relative return gaps between Hard and Soft Tech seem less well-telegraphed among investors outside of Asia. For instance, STAR50 (a proxy for onshore AI Hard Tech) has outpaced HSTECH (dominated by offshore Internet/platform companies) by 68pp ytd, while ChiNext has led SHCOMP/CSI300 by 19pp/17pp so far this year, both reaching unprecedented or extreme levels in the history of Chinese equities. This great divergence suggests to us that the AI bottleneck, Hard vs. Software, or AI infrastructure supplier vs. AI capex spender trade is also at play in China, although manifesting in pockets of the equity universe that are less well followed and positioned by foreign investors.

Kinger Lau, CFA
+852-2978-1224 | kinger.lau@gs.com
GS (Asia) L.L.C.

Timothy Moe, CFA
+65-6889-1199 | timothy.moe@gs.com
GS (Singapore) Pte

Si Fu, Ph.D.
+852-2978-0200 | si.fu@gs.com
GS (Asia) L.L.C.

Kevin Wang, CFA
+852-2978-2446 | kevin.wang@gs.com
GS (Asia) L.L.C.

Exhibit 1: The AI bottleneck, Hard vs. Software, or AI supplier vs. AI capex spender trade has been a dominant equity theme globally  
![](images/e6a746c7c96ecbc08e3b661b6be67b9c49ab65d5dc0681b3b3f04f61d125a4c3.jpg)  
Source: Wind, FactSet, GS Global Investment Research

Exhibit 2: Indexes with higher AI Hardware exposures have outperformed ytd in the Chinese equity universe

![](images/52cc911c139b3da2f3291c4a501eb4505c51747f0ca227d063a0d313dce72b69.jpg)  
Source: FactSet, MSCI, HSI, CSI, GS Global Investment Research

3. Rotation temptation. The significant return disparity and index return concentration has prompted investor questions about the likelihood, necessary conditions, and timing of a potential rotation from A to H, or from Hard to Soft Tech. Indeed, HSTECH has rebounded 11% in the past two weeks (still down 14% ytd), led by a few Internet incumbents on better newsflows, suppressed starting valuations, and continued AI application/monetization developments. Our top-down Hard vs. Soft Tech rotation model, an extension of our A-H Market Rotation Model, also points to the direction that H-share Soft Tech equities may start to trade better in the coming months, potentially narrowing their underperformance gaps vis-a-vis their A-share Hard Tech counterparts on various fundamental, valuation, and liquidity factors. That said, while recognizing that prevailing valuations of leading Internet names may have already factored in further de-rating in their core businesses and/or negative NPV/ROIs on their AI investments, which seem overly bearish to us, we believe a sustained price rally would require a visible recovery in underlying profits, which could be still a couple of months or quarters away as we elaborate below.

Exhibit 3: H-share Soft Tech may start to close its underperformance gaps vis-a-vis Hard Tech in A shares in the months ahead

MSCI China AI Hard Tech vs Soft Tech Relative Returns (rolling 6 months)  
![](images/1c1b0afa85f83468c976b5fed5de2855915b742c52937439319c2531caa65309.jpg)

<table><tr><td></td><td>Coef.</td><td>t Stat</td></tr><tr><td>Intercept</td><td>-0.15</td><td>-2.86</td></tr><tr><td>PE premium</td><td>-0.24</td><td>-1.87</td></tr><tr><td>fEPS revision gap</td><td>0.80</td><td>3.11</td></tr><tr><td>24m fEPSg gap</td><td>1.89</td><td>3.66</td></tr><tr><td>Turnover velocity ratio</td><td>0.13</td><td>5.05</td></tr><tr><td>CSI300 vs MXCN return</td><td>1.32</td><td>9.22</td></tr></table>

Source: Wind, FactSet, GS Global Investment Research  
Exhibit 4: A bearish scenario in terms of Chinese Internet companies' AI investments could be already in the price

![](images/a13591a5cbc2ba80c96ae381d3581d7beb2ec9d0dd1baac4fc3327fa5c0df644.jpg)  
Top 9 internet companies include: Tencent, Alibaba, PDD, Xiaomi, Meituan, NetEase, Baidu, JD, and Trip.com.

Source: Company data, GS Global Investment Research

4. No earnings, no gains. Subdued earnings delivery has weighed on returns of offshore indexes, and was a key input to our downgrade of MSCI China from Overweight to Market-weight 6 weeks ago. 1Q26 profits were down 8% for MSCI China, dragged primarily by the Internet sector (35% of earnings weight), which has incurred more than Rmb180bn of subsidy losses cumulatively since 2Q25, and has been a major sponsor for AI capex domestically that could top US\$100bn/US\$120bn this year and next on GS estimates. The weak 1Q results follow a lackluster year in 2025 when index earnings grew merely 7%, trailing below consensus expectations for 6 consecutive years. Looking ahead, we are still of the view that narrowing subsidy losses, fast-growing AI-related new opportunities (e.g. Cloud, agentic AI, and AI tokens), and stable, cash-generating

e-commerce businesses could help drive a (operating) profit turnaround for Internet heavyweights in their 2Q or 3Q results season, at which point investors may be better placed to quantify these companies' AI upside optionality, and could be more incentivized to value these stocks on a sum-of-the-parts basis as opposed to a likely blended (earnings) approach now, in our view.

Exhibit 5: Chinese Internet/Soft Tech stocks have seen persistent downward earnings pressures in the past year  
![](images/5dcc8497e7a9f3e5c1e1a2b4f8dbc5d02a9e364712a48979753c50d11cf0b7cc.jpg)  
Source: MSCI, FactSet, IBES, GS Global Investment Research

Exhibit 6: Chinese big tech companies' returns are most sensitive to realized profit growth  
![](images/e3da0aaed5a59c0518f275cbb9ec9e63148db2eb67953835a2e4ece972930d4a.jpg)  
Source: Wind, FactSet, GS Global Investment Research

Exhibit 7: Profit growth momentum for offshore tech could improve in 2H26 per GS and consensus expectations  
Earnings growth yoy - 9 large Chinese Internet companies  
![](images/05d5532fad39736387a1c2832cacc3ef19323bfdc61981fe0212d2800bef22ec.jpg)  
Source: MSCI, FactSet, GS Global Investment Research

5. Are China AI stocks overheated? This is a popular question from investors, probably a derivative of the AI bubble debate that has dominated investors' mind-share globally in recent months. In sum, we push back to the notion that the aggregate Chinese AI equity bloc is a bubble as our top-down analysis shows that the potential economic benefits via efficiency gains and new profit/TAM creation could be 50% to 100% higher than what is currently discounted in AI equity prices. That said, we see emerging signs of overheating in certain pockets of the AI universe, namely the semi cohort and select A-share Hard Tech proxies where valuations are at rich premiums vs. historical

(USD tn) Market cap increase vs PDV of AI-related value creation norms and global comparables, and concentration and leverage risks are rising at somewhat concerning paces. This warrants heightened focus from investors on controlling risks, diversifying exposures, and leaning into earnings-powered strategies to strike better risk/reward. See #10 for details.

Exhibit 8: The (net) appreciation in Chinese AI market cap since the DeepSeek moment looks moderate compared with the potential growth and earnings upside that AI could generate in the future

![](images/a32efc76c1028eaf26bf611585957d24a6a53a6b414bf2a6fc6ce922c6a7f011.jpg)  
Please refer to AI changes the game (Part 2) for the definition of China AI and non-AI universe.  
Source: Bloomberg, FactSet, GS Global Investment Research

Exhibit 9: Valuations have risen, but not at extreme levels  
![](images/e25d941934a86e171bcb0257727918000e7c5f4360ae31d7d4262f90c32f60d0.jpg)  
Source: Wind, GS Global Investment Research

Exhibit 10: Valuations for A-share Hard Tech equities are still slightly below their historical norms  
![](images/9586d143f06bc1bec3d12e4c66292bfbedb8485b2e72dc0530a0b42ff4d7f24c.jpg)  
Note: Based on latest constituents; z-score over past 12 years (monthly)  
Source: FactSet, I/B/E/S, CSI, GS Global Investment Research

6. Are Korea and Taiwan stealing thunder from China? Empirically, the directional return correlations between China and the two North Asian markets are near their respective historical troughs. Per GS Prime Brokerage statistics, hedge funds' net risk exposures in EM Asia (ex-China) are at all-time highs while those in Chinese stocks are at the bottom of the range. However, allocations from mutual funds, especially for EM mandates, have edged up to multi-year highs (modest Overweight by EM funds for the first time on record dating back to 2011, likely due to China's reduced index weights in the EM benchmark), gross exposures from hedge funds are near cycle peaks, and participation from foreign cornerstone investors in HK IPOs ytd are comparable to the historical highs in 2021, all suggesting that foreign investors are still active and engaged, but prioritizing market-neutral strategies and alpha opportunities over beta risks in

Chinese equities.  
Exhibit 11: Chinese equities' return correlations with Korea and Taiwan are close to historical lows  
![](images/cacc0133646f360a3407a8ccc9f483d69cb461a731a36e14c1cc2450b5c2afc3.jpg)  
Source: FactSet, GS Global Investment Research

Exhibit 12: EM funds are now Overweight China for the first time in history  
![](images/1d671697f748479719d610f92862fcea1e300036b1c8c90b4433701d1e05697b.jpg)  
Source: EPFR, GS Global Investment Research

Exhibit 13: Global hedge funds' gross allocation to China has risen faster than their net exposures, suggesting stronger bias for alpha trading  
![](images/3575542dc5de88d8e75c78c8f3bc7123239e3946eaaf658e440334d76143687f.jpg)  
Source: GS FICC and Equities and Prime Services data as of July 3, 2026.

7. Excitements and worries about IPOs. IPOs have become a popular avenue for investors to extract alpha in a challenging beta environment. Our study shows that 100 companies have made their debuts on the HK bourse ytd, raising US\$35bn in total and generating a median stock return of 32% and 30% in the first 1 and 3 months post-listing. Factors such as (large) issuance size, standalone H-share listing, and moderate cornerstone ownership (30%-50%) have explained a large extent of the outperformance among the new listings. The active and long IPO pipeline in HK has nevertheless raised investor concerns about liquidity drain, which appears overdone to us considering the expected issuance size in the remainder of this year (US\$25bn for IPOs and US\$45bn including follow-ons on GS estimates) and the record-high cash returned to shareholders by listed companies via dividends and buybacks (US\$500bn/FU\$560bn for FY2025/FY2026). A-share IPO activity is also picking up pace with CXMT, a Chinese DRAM maker, reportedly aiming for STAR board listing and looking to raise US\$4.3bn in its primary issuance, which would be the largest A-share IPO since May 2022.

Exhibit 14: Investors participating in IPOs over the past two years could have achieved approximately 20-30% returns in the first three months post-listing

![](images/2de646bcde8dd7178ce176ee24405636c30632cb9b75079fbb8abddae954f868.jpg)  
Source: Wind, FactSet, GS Global Investment Research

Exhibit 15: The amount of new issuance supply looks manageable compared with the record-high cash returns to shareholders from listed corporates

![](images/79518b288e87b9196291b02ea0a2732cdba90268f7e56a835700f7e3968198e0.jpg)  
Source: Wind, Bloomberg, GS Global Investment Research

8. AI has indeed changed the game and has dominated our client conversations, which have revolved mainly around: a) the progress of the self-reliant AI ecosystem build-out in China; b) the technological breakthroughs in certain choke points in the supply chain, namely EDA, lithography, advanced packaging, and High-Bandwidth Memory (HBM); c) the cost and efficiency differentials between AI capex spent in the US and China; d) China's competitive threats to global incumbents in areas such as LLMs, robotics, and AI tokens, with the latter already representing almost half of the global consumption; e) AI use cases, monetization, and economics of AI investment; and, f) the role of the Chinese government in AI regulation and infrastructure build-out. Overall, China is an integral part of the global AI equity universe, accounting for 11%/18% of AI-related market cap/revenue worldwide, but China AI equities are significantly under-owned by international investors, especially in the Power, Infra, and Physical AI layers where Chinese companies arguably have comparative and competitive advantages on a global basis. We'd continue to recommend our China Select AI Portfolio which comprises 50 names from 22 specific AI industries, aiming to provide investors with balanced and comprehensive exposures across the whole AI value chain. See Part 1, 2, 3, and 4 of our AI changes the game series for details.

Exhibit 16: China is an integral part of the global AI equity universe  
![](images/47d4cef321769bbc31cc9efa7134cf7663be26fca03f31746452b3d29dcb086b.jpg)  
Source: FactSet, MSCI, GS Global Investment Research

Exhibit 17: Chinese AI models account for almost half of the world's token usage  
![](images/1c6e64edb81ce1e1c2cebff8a55056281f6d60d3a16347df9ef859c296927fe4.jpg)  
Note: based on top 10 used model companies in OpenRouter; other US/Chinese model companies may be classified under "Others".  
Source: OpenRouter

9. Macro taking a backseat, for now. The topicality of AI has overshadowed investors' interest in macro-related subjects. That said, important economic subjects such as the China's potential housing market stabilization in 2027, China's resiliency in the latest global oil shock, the continued weakness in domestic consumption, the strength of the Rmb (vs. the USD) and Chinese exports, and potential policy responses (stimulus) in the July Politburo meeting have come up in our meetings with macro-focused investors and asset allocators. This orientation is partly reflected in and consistent with (the readings) our US-China Relations Barometer, which is currently at the lowest levels since 2022 (i.e. low bilateral tensions implied by market prices), indicating that prevailing equity market pricing could be more driven by the AI theme and other idiosyncratic micro factors as opposed 

[中间内容因长度限制已省略]

mpt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be

## supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
