你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  ✅ 三大情景框架：DCF、P/ARR、EV/Sales
  ✅ 关键变量分析
  ✅ 估值逻辑、假设、终值占比等核心内容覆盖
  ✅ 适合准备 AI 相关面试、研究 AI 估值的同学
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
# China Insurance: Financials trip takeaways

We spent five days (May 25-29) in mainland China, meeting a broad set of financial companies, including banks, insurers, brokers, and online lending platforms. Among insurers, we met the IR and management teams of Ping An, CPIC, China Taiping, ZhongAn (not covered), China Life, NCI, and PICC P&C.

Life insurers remain confident of strong growth in the bancassurance channel and expect the tightening of channel expense supervision to benefit the large insurers. On the asset side, strong equity market performance since the end of March has driven a rebound in investment results, but insurers mostly see stable equity allocation at the current level, emphasizing a balanced portfolio between growth and dividend stocks. P&C insurers generally expect to see improvements in underwriting results, as a result of expense regulation (both auto & non-auto insurance) and reductions in claims frequency (auto insurance).

Overall, we believe industry fundamentals are solid, with continued new policy sales momentum for lifers, and profit and book value growth recovery for all insurers following the equity market rebound.

# Thomas Wang

+852-2978-1697

thomas.wang@gs.com

GS (Asia) L.L.C.

# Simone Chen

+852-2978-0619

simone.chen@gs.com

GS (Asia) L.L.C.

Exhibit 1: China Insurance valuation comp 

<table><tr><td rowspan="2">As of 05-Jun-2026</td><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td rowspan="2">Share price</td><td rowspan="2">Target Price</td><td rowspan="2">Potential upside /downside%</td><td colspan="3">P/B</td><td colspan="3">P/E</td><td>Div. yield</td><td>ROE</td></tr><tr><td>2025</td><td>2026E</td><td>2027E</td><td>2025</td><td>2026E</td><td>2027E</td><td>2026E</td><td>26/27E</td></tr><tr><td>China insurers - H share</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>China Life Insurance Co. (H)</td><td>2628.HK</td><td>Neutral</td><td>28.00</td><td>28.5</td><td>2%</td><td>1.2</td><td>1.1</td><td>1.0</td><td>4.7</td><td>8.9</td><td>8.0</td><td>3.5%</td><td>13%</td></tr><tr><td>Ping An Insurance Group (H)</td><td>2318.HK</td><td>Buy</td><td>56.90</td><td>75.0</td><td>32%</td><td>0.9</td><td>0.9</td><td>0.8</td><td>6.8</td><td>7.3</td><td>6.5</td><td>5.3%</td><td>12%</td></tr><tr><td>China Pacific Insurance (H)</td><td>2601.HK</td><td>Buy</td><td>31.10</td><td>38.0</td><td>22%</td><td>0.9</td><td>0.8</td><td>0.8</td><td>5.1</td><td>6.5</td><td>6.3</td><td>4.1%</td><td>13%</td></tr><tr><td>New China Life Insurance (H)</td><td>1336.HK</td><td>Sell</td><td>47.38</td><td>37.0</td><td>-22%</td><td>1.2</td><td>1.1</td><td>1.1</td><td>3.7</td><td>7.0</td><td>7.7</td><td>4.3%</td><td>15%</td></tr><tr><td>China Taiping Insurance Holdings</td><td>0966.HK</td><td>Neutral</td><td>19.31</td><td>21.0</td><td>9%</td><td>0.7</td><td>0.7</td><td>0.6</td><td>2.7</td><td>5.4</td><td>5.2</td><td>3.8%</td><td>13%</td></tr><tr><td>PICC Group (H)</td><td>1339.HK</td><td>Neutral</td><td>5.08</td><td>6.7</td><td>32%</td><td>0.7</td><td>0.6</td><td>0.6</td><td>4.5</td><td>6.1</td><td>5.5</td><td>5.0%</td><td>11%</td></tr><tr><td>PICC P&amp;C</td><td>2328.HK</td><td>Buy</td><td>14.27</td><td>19.6</td><td>37%</td><td>1.0</td><td>1.0</td><td>0.9</td><td>7.2</td><td>8.3</td><td>7.6</td><td>5.4%</td><td>12%</td></tr><tr><td>China insurers - A share</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>China Life Insurance Co. (A)</td><td>601628.SS</td><td>Neutral</td><td>32.82</td><td>42.0</td><td>28%</td><td>1.6</td><td>1.4</td><td>1.3</td><td>6.0</td><td>11.4</td><td>10.2</td><td>2.7%</td><td>13%</td></tr><tr><td>Ping An Insurance Group (A)</td><td>601318.SS</td><td>Buy</td><td>53.48</td><td>77.0</td><td>44%</td><td>1.0</td><td>0.9</td><td>0.8</td><td>7.0</td><td>7.5</td><td>6.7</td><td>5.2%</td><td>12%</td></tr><tr><td>China Pacific Insurance (A)</td><td>601601.SS</td><td>Neutral</td><td>31.05</td><td>39.0</td><td>26%</td><td>1.0</td><td>0.9</td><td>0.8</td><td>5.6</td><td>7.1</td><td>6.9</td><td>3.8%</td><td>13%</td></tr><tr><td>New China Life Insurance (A)</td><td>601336.SS</td><td>Sell</td><td>56.35</td><td>49.0</td><td>-13%</td><td>1.6</td><td>1.5</td><td>1.4</td><td>4.8</td><td>9.1</td><td>10.0</td><td>3.3%</td><td>15%</td></tr><tr><td>PICC Group (A)</td><td>601319.SS</td><td>Sell</td><td>6.57</td><td>6.1</td><td>-7%</td><td>0.9</td><td>0.9</td><td>0.8</td><td>6.3</td><td>8.5</td><td>7.8</td><td>3.5%</td><td>11%</td></tr></table>

Prices are as of Jun 5. Target prices are 12-month.   
Source: Thomson Reuters, GS Global Investment Research

# Sector takeaways

1) Investment strategy: Lifers generally hold a neutral view on the interest rate outlook, while focusing on asset and liability duration and cash flow matching. Long-term government bonds remain an important instrument to anchor asset duration. However, given that the long-term bond yield remains depressed (vs. historical levels), the focus is more on the equity investment side, especially on high-dividend yield stocks that can be held over the long term, thereby providing a bond-like yield and duration.

In the near-term, strong equity market performance since the end of March has driven a rebound in portfolio returns for all insurers. But insurers generally do not expect a material uplift in equity asset allocation (vs. the current level). Within equity investment, despite the rally in AI-related stocks, insurers are targeting a more balanced allocation between growth and value stocks. Dividend stocks remain a focus, as evident in the increase in the mix of OCI equity investment (vs. FVTPL). The target dividend yield is generally $4\%$ or higher.

2) Bancassurance regulation and growth: The life insurers we met all welcomed the new regulation on bancassurance channel fees, issued by the NFRA in March, as they expect the more granular examination of channel fees to further encourage banks to cooperate with large insurers. That said, insurers do expect to see near-term disruptions, as sales incentives are reduced. Generally, insurers do not expect this to have a material impact on margins, as companies are likely to pass on most of the savings to policyholders.

3) Agency development: Lifers generally expect stable agent headcount over the next 2-3 years, and the focus is mostly on (high-quality) productive agents. There are targeted recruitment and training processes in place, while resource support is also tilted towards the high-quality agency team. Despite the surge in bancassurance sales, most lifers believe agents are better positioned to serve upper affluent and HNW customers.

4) Auto insurance underwriting results outlook: Excluding the potential impact from natural catastrophes, insurers generally see room for improvement in underwriting results, driven by: 1) better risk underwriting and more pricing flexibility, 2) higher

penetration and usage of ADAS features, 3) improvements in the repair process, and 4) the potential re-calibration of the risk premium. While premium growth in 2026 could be affected by a yoy decline in new car sales, insurers generally expect premium growth to recover to low-to-mid single digits in the medium term.

5) Update to the C-ROSS regime: The Phase III update for the C-ROSS regime is still under discussion, as the regulator has yet to decide on the various risk parameters. Companies expect that implementation is likely in 2H26 or 2027. For the large insurers, companies noted that current solvency ratios are well above the regulatory minimum.

# Company meeting takeaways

# Ping An

- Ping An reiterated its multi-channel distribution strategy, including agency, bancassurance, community finance, and others. In the bancassurance channel, Ping An is working with fewer than 30k bank branches, just over $10\%$ of more than 220k bank branches in China. Ping An expects to increase branch penetration, and noted that in the last 2 years, it could add as many as 1,000 branches in a single month, although the pace of growth is likely to be slower going forward.   
- On equity investment, Ping An reiterated a balanced strategy, with a focus on using equity as an important through-cycle instrument, providing bond-like duration and yield. On dividend stocks, the company has a diversified portfolio, not just banks. The target yield is above $4\%$ , but the company noted that the hurdle rate could be reduced if the cost of liability continues to decline.   
On asset quality, Ping An continues to expect the asset management segment to provide a positive profit contribution in 2026. The company sees limited property-related impairment pressure in 2026, thanks to provisions already taken and improved market sentiment in Tier 1 and Tier 2 cities. Within the asset management segment, Ping An highlighted that the securities business achieved a high ROE in 1Q26, well above the industry average.

# CPIC

■ VONB growth and margin outlook: CPIC aims to achieve a balanced value contribution between the agency and bancassurance channels. The agency VONB margin is close to 30%, largely driven by long premium term savings products. The bancassurance margin is around 15%, and the company sees potential upside by reducing the mix of single premium policies. Participating products are an important growth driver in both channels, and CPIC sees potential for the market to evolve toward HK par products, with a low guaranteed return and diversified investment allocation.   
On P&C, CPIC sees potential for a further reduction in the expense ratio, thanks to tight regulation for both auto and non-auto insurance. In the NEV segment, there is room for the COR to decline as autonomous driving features improve, and the repair network and process develop. On credit guarantee insurance, CPIC sees positive

development in 2026, after a business adjustment starting from early 2025.

# China Taiping

Bancassurance contribution: Taiping noted that banks prefer 3- to 5-year products and struggle to sell protection products, so margin upside is limited. But there is significant volume growth potential, given that moderate deposit migration from banks can be a significant growth driver for insurers. For Taiping, bancassurance VONB contribution was c.35% in 2025, but management sees potential for this to gradually increase toward 50%. Taiping noted that the channel is dominated by the top 7 largest life insurers (including Taiping Life), following the regulatory clampdown on channel expenses.   
Investments: Taiping Life is cautiously optimistic on equity market performance, and holds a neutral view on rates. The focus is on duration and cash flow matching, to ensure the investment return covers the cost of liability. The company would also seek to enhance the yield on the fixed income portfolio through trading gains.

# ZhongAn

Online health insurance: ZhongAn (ZA) noted that health insurance in mainland China has significant development potential, while online penetration within health insurance is also low. ZA is the largest online health insurance distributor and expects to maintain strong growth momentum as the market develops.

# China Life

China Life expects VONB growth momentum to normalize in the coming quarters, after an exceptional 1Q26 (+75% yoy). The base effects in 2Q and 3Q are higher, and China Life also noted that the new bancassurance channel expense regulation could disrupt near-term sales momentum. Nonetheless, China Life is confident of double-digit VONB growth for FY26 and sees margin expansion, driven by 2025 repricing actions and a greater focus on long-term, regular premium policy sales.   
Equities investment will continue to increase as new premiums come in, but China Life sees relatively stable overall equity investment allocation. Allocation within the portfolio is diversified, tracking broad market indices, despite strong performance in the AI supply chain. China Life noted that the mix of OCI equity investment has increased, reaching c.30% of the equity portfolio, broadly in line with the industry average.

# NCI

Both agency and bancassurance sales and VONB are tracking well ahead of FY26 targets. Starting from 2Q26, NCI is focusing on health insurance and long-term products. Detailed regulation on the participating critical illness (CI) product has not been launched, so sales are mainly of the traditional CI product in the agency channel. The bancassurance channel is still mainly a savings-product channel.

On investment, total equity investment allocation was $22\%$ in 2025, and declined slightly in 1Q26, due to market movement. In the medium term, NCI does not have a target level, but does not expect this to increase to the 25-30% range. NCI sees opportunities in H-shares now, especially when considering dividend yield and cash flow.

On dividend payout, the $25\%$ payout ratio in 2025 was sufficient to drive DPS growth, even off a high base in 2024. There is no decision yet on the FY26 dividend policy, but the company will take absolute DPS into consideration.

# PICC P&C

Equity investment is approaching 30% of the portfolio, including stakes in Huaxia Bank, Industrial Bank, PICC Life, and PICC Health. PICC P&C sees limited room for a further increase in the equity asset mix, as 30% is the cap based on its current comprehensive solvency ratio. The target investment return is 3-4% in 2026.

PICC P&C attributed the industry-wide decline in auto insurance premiums in 1Q26 to the decline in new vehicle sales and the usual pricing factor changes. Management expects auto sales to recover gradually, driving improvements in auto insurance premium growth in the coming quarters.

In terms of underwriting results, PICC P&C attributes its better COR to a combination of: 1) better risk pricing, 2) internal expense management, 3) a close relationship with OEMs, and 4) expertise in claims management. As the NEV market gradually matures, PICC P&C expects the claims ratio to improve broadly, and believes its competitive advantages can enable the company to continue delivering above-peer underwriting results.

# Price Target Risks and Methodology - China Life Insurance Co.

We rate China Life H/A at Neutral/Neutral. Our 12-month, ROA-based target prices are HK\$28.5/Rmb42.0, implying 1.0X/1.7X FY27E P/B.

Downside risks: Further weakness in the investment market, which could reduce the solvency ratio and limit its ability to raise dividends; a further decline in the 10-year government bond yield to below $2\%$ ; weak insurance sales growth in lower-tier cities, where China Life has a more dominant market share; below-peer agent productivity gains.

Upside risks: Strong A-share performance given China Life's leverage to A-share returns; sustained double-digit NBV growth; better-than-expected shareholders' return plans; an increase in long-term bond yield.

# Price Target Risks and Methodology - Ping An Insurance Group

We are Buy rated on Ping An's A and H shares. Our 12-month SOTP-based target prices are HK\$75.0/Rmb77.0, implying 1.1X/1.3X FY27E P/Bs. We value 1) Ping An Life at 1.9X/2.4X FY27E P/B, based on our ROA projection, 2) Ping An P&C at 1.0X P/B, based on FY27E ROE of 12%; and 3) Ping An Bank at 2.125X target P/PPOP (covered by Shuo Yang).

Downside risks: A further decline in operating profit and/or CSM (contractual service margin) would put downward pressure on dividend growth; further deterioration in sales mix, leading to greater sensitivity of future profit to interest rate and investment returns; further investment asset losses/impairment in non-insurance businesses, such as banking and asset management businesses.

# Price Target Risks and Methodology - China Pacif

[中间内容因长度限制已省略]

, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
