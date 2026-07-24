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
# Asia Quantitative Strategy

# Japan Strategy Q326: The bright spot in the region - Ample opportunities for value & growth managers

![](images/92b5e80ba5843a2493ff182fd2e3b29b8724698643f8c1bc749a290fade374fa.jpg)  
Rupal Agarwal  
+65 6326 7641  
rupal.agarwal@bernsteinsg.com

![](images/55368023239ee47f25203700f1a12f171f30650f68f959a72ca782a09672ba61.jpg)

Cheng Zhang, CFA, CQF

+852 2123 2636

cheng.zhang@bernsteinsg.com

Japanese equities delivered robust returns in 1H26 with MSCI Japan up 16% and NK225 up 29%. While markets have been under pressure in July, we believe Japan still remains a bright spot within the region with reasonable valuations, broad-based earnings upgrade cycle, strong foreign investor sentiment and AI+non-AI opportunities.

Valuations, earnings, flow remain supportive: The market has de-rated from 17x fwd. PE to 14.9x ie. 10yr avg levels. Outside of KR/TW, Japan has been the only big Asian market seeing a broad-based upgrade cycle (see Asia Quant Strategy Deck) with most sectors seeing net upgrades. The trends look most positive for Healthcare, Materials, Financials, Tech, and Industrial; though earnings expectations for Tech, Financials, Industrial are now at record high. Japan has been the most favored Asian market this year, seeing +57.5bn USD of FII flow and global active funds have reduced their UW from -1.6% in Jan26 to -0.48% by May26. We expect foreign investor sentiment to be supportive and more recently, even retail sentiment seem to be coming back.

Domestic vs. exporters. We have been recommending balanced exposure across exporters and domestics. While 1H exporters outperformed domestics (35% vs. 20%), more number of domestic sectors have done well such as Banks, Insurance, Retailing, Materials, Commercial & Pro services and F&B. Domestics continue to offer stronger revenue growth (23% vs 12% for exporters), higher dividend yield (2.2% vs. 1.7%), buyback yield (1.3% vs 0.5%) and cheaper valuations; however, exporters have superior ROE (11.2% vs. 9.3%) and better relative earnings revisions. Given these mixed signals, we maintain our preference for both exporters and domestics, though we believe the case for domestics is improving as extreme weak Yen support for exporters is largely behind us.

Industry outlook. We remain positive on tech sector with a preference towards chasing momentum names selectively but also diversifying into undervalued opportunities. See - Japan Tech Strategy 3Q26. Based on our updated industry scorecard and its historical efficacy, we recommend being positive on Capital Goods, Banks, Diversified Financials, Insurance, Energy and Household & Personal products while being cautious towards Pharma, Transportation, F&B, Food & Staples Retailing and Software & Services.

Style positioning. We maintain our value and growth barbell. Leadership in 2026 has been driven by growth/momentum factors, while quality, low volatility and small Caps have lagged. While Japan momentum has not been as vulnerable as TW/KR momentum; the high correlation of the AI trade has created pressure on Japan momentum basket as well. Instead of taking direct momentum exposure in Japan, we have been chasing names where momentum is likely to increase; which is growth stocks on price momentum aspect and value stocks on earnings momentum. Both these baskets are cheap and while growth stocks are looking better on continued upward revisions, value has dropped to extreme bearish sentiment which is likely to bottom. Value also has the macro tailwind from rate hike cycle. We believe large-cap leadership is likely to continue given better earnings support, however, opportunities within small/mid-caps are also emerging. We show our preferred screens in Exhibit 29–Exhibit 30.

## DETAILS

## PERFORMANCE SO FAR

Japanese equities delivered robust returns in 1H26 with MSCI Japan up 16% and NK225 up 29%. Since April, NK225 surged ahead of Topix/MSCI Japan, implying strong large-cap leadership. Within Japan, AI theme has been a key driver with Semis up 101% followed by Tech Hardware up 58%. However, even domestic sectors like Banks, Insurance have done well along with Commercial & Pro Services. The worst hit industries have been Food & Staples Retailing (-29%) and Software & Services (-23%). 1H26, exporters have done better, up 35% vs. domestics up 20%. In Jul, however, Domestics (+4%) outperformed exporters (-6%). From factor perspective, GARP (+28%) has been the winning factor in Japan in 1H26 relative to the market, followed by Growth (27%), price momentum (18%) and earnings momentum (16%). The worst styles in 1H26, have been quality, low vol and small-caps, down -14%, -14% and -13% respectively vs. market. In Jul MTD, Low vol (6%), value (6%), high yield (6%) outperformed while momentum (-14%) saw sharp unwind followed by growth/GARP (-4%/-8%). Within Tech sector, 1H 2026, GARP (35-47%) led followed by Momentum with 29% returns relative to market. Other styles other than momentum and growth have underperformed the market, and ROIC (-18%) and Low vol (-21%) saw the weakest performance. In Jul, high yield (+5%) has outperformed the most. (Exhibit 1-Exhibit 5)

EXHIBIT 1: YTD, MSCI Japan is up 14% and NK225 is up 29%. NK225 saw -6% correction in Jul  
Japan Market Performance - MSCI Japan, TOPIX, NIKKEI 225  
![](images/019d9195591ae1a442c06ee34868651bb670467d346f14a1bfe2c7dfaeb406ab.jpg)

Data till Jul 21th 2026

Source: Bloomberg, Bernstein analysis

EXHIBIT 2: Semis (79%) remains the winning sector in 2026 YTD, followed by Tech Hardware (42%), Banks (38%) and Commercial & Pro Services (33%)

MSCI Japan - 2026 Industry Performance (USD Returns)  
![](images/e61298ce33cbfbe82f8a46bc81087c2a92dae930b1cafb439479386a2734edaa.jpg)  
Data as of Jul 21 $^{st}$ 2026. Blue represents domestic oriented while green represents export oriented industries. We define domestic and exporters based on median sale exposure across different geographies in a fiscal year. Industries with above 50% sale exposure outside Japan are defined as exporters
Source: Bloomberg, Bernstein analysis  
EXHIBIT 3: In 1H2026, performance of Japan exporters was stronger (35%) compared to domestics (20%) in USD. In Jul, however, Domestics (+4%) outperformed exporters (-6%)  
Japan Performances since 2022 in Dollar - Domestic vs. Exporters

![](images/4afc17195ed561ffeca340a7cf82a35b1b7dd43e08dc484a92048aa86837ac38.jpg)  
Japan Performances since 2022 in Yen - Domestic vs. Exporters

![](images/41b00234a051bc439b57837cf42a8e904c2123b9cac9269e1f0a4df578967c5b.jpg)  
Data as of Jul 21 $^{st}$ 2026. We define domestic and exporters based on median sale exposure across different geographies in a fiscal year. Industries with above 50% sale exposure outside Japan are defined as exporters
Source: IBES, MSCI, FactSet, Bernstein analysis

EXHIBIT 4: GARP/Growth (+28%) has been the winning factor in Japan 1H 26, followed by price momentum (18%) and earnings momentum (16%). The worst styles YTD, have been low vol and small-caps, down -14% and -13% respectively vs. market. In Jul MTD, Low vol (6%), value (6%), high yield (6%) outperformed while growth and momentum underperformed  
![](images/d9464227db930d337f8936ad61b30a937c521db0bbf2120d5618d0abae342341.jpg)  
Data till Jul 21 $^{st}$ 2026
Source: MSCI, FactSet, Bernstein analysis  
Japan Tech Factor Performance rel. to Tech Sector 2026 YTD

EXHIBIT 5: 1H 2026, GARP (35-47%) led followed by Momentum with 29% relative to market. The rest styles other than momentum and growth have underperformed the market, and ROIC (-18%) and Low vol (-21%) saw the weakest performance. In Jul, high yield (+5%) outperformed the most

![](images/231255373639c48b06e5be7c515e1d4f7de5537b5c77647745240986264394cb.jpg)  
Data till Jul 17 $^{th}$ 2026

Source: IBES, MSCI, FactSet, Bernstein analysis

## VALUATIONS, EARNINGS AND SENTIMENT

Japan market saw sharp de-rating since June, dropping from 17x forward P/E to 14.9x fwd. PE now, which is 10yr average multiples. Hence, valuation is no longer a challenge while earnings upgrade cycle continues. An average stock in Japan has been seeing net upgrades with ample room for upward revisions to continue. Except Consumer, Utilities, Communications; all sectors in Japan are seeing net upgrades and the trends look most positive for Healthcare, Materials, Financials, Tech, and

Industrial where pace of upgrades have been increasing. However, earnings expectations for Tech, Financials, Industrial are now at record high levels while earnings revision cycle for Staples, Discretionary, Communications, Utilities and Real Estate have been weakening. (Exhibit 6-Exhibit 8). Global investors have been a key driver of market flow this year - foreign investors have poured +57.5bn USD YTD in Japan and global active funds have reduced their UW from -1.6% since the beginning of the year to -0.48% by May 2026. Interestingly, global active investors are still not OW Japan, leaving ample room for global inflow to continue. On the other hand, domestics investors have been net sellers- YTD, Japan retail investors have pulled out -5bn USD while domestic institutions have net sold -40bn USD. More recently, retail sentiment seem to be coming back. (Exhibit 9-Exhibit 11)

EXHIBIT 6: Japan has de-rated from 17x in Feb to 14.9x fwd PE ie. at10yr average level  
![](images/c64aa185b89c7e69b80b6dcfdfde40b69bfdb317fad09cb9df8e10165c6a4b0b.jpg)  
Data as of Jul 21 $^{st}$ 2026. PE data are market-cap weighted Source: MSCI, IBES, FactSet, Bernstein Analysis

EXHIBIT 7: Earnings upgrade has been a key support for markets - while the large-caps have seen record high earnings expectations, even an average stock remains in net upgrade with room for upward revisions to continue

Japan Earnings Revisions Balance

![](images/223d53ba29e6044a7946dcdfa0a6dbcf6008fb02ba96bf91cb2641b6b02d9c2c.jpg)  
Data till Jun 30 $^{th}$ 2026
Source: MSCI, FactSet, Bernstein analysis

EXHIBIT 8: Except Consumer, Utilities, Communications; all sectors in Japan are seeing net upgrades. The trends look most positive for Healthcare, Materials, Financials, Tech, and Industrials where pace of upgrades have been increasing. However, earnings expectations for Tech, Financials, Industrials are now at record high levels

Consumer Staples - JP

![](images/527d18841aba520f7b478a892083fa74a81946fa6fdf1f8d5d978e07e9549dd3.jpg)

![](images/178eaf6996855aca9f6bf7ec6ec119c921cb59179e26da9967ed444684abcccc.jpg)

![](images/18f9e3060e8df17af9aa0fba42ada9dc0fc99689898dba81b7569fad94225b71.jpg)

![](images/3532f692d8072f838739d3cacd51a289bff0459f76363263c5449cb657bc516e.jpg)

![](images/ae60f9f0d2d27cd8c5cdad27c0a614fce4d261b28e5276f708681d691784a10e.jpg)

![](images/14228a6a67cb18fe0b1c4a8c8e9d2d8582a72ea60182b46f971ed071bb762571.jpg)

![](images/0a758d1f542956e496918546a5f0aeba6ca29514a893508b6f0126498655a0b9.jpg)

![](images/ac833bac8bbd79d80e88caa93e8f20052f5a672c82333c1cc6a94ab7a21baf4d.jpg)

![](images/2fd29c8af201f2813ba96501a328cab14bd494d84f9a5a397b119b71f8819137.jpg)

Data as of Jun 30 $^{th}$ 2026

Source: IBES, MSCI, FactSet, Bernstein analysis

![](images/dd27eec1195a9d5775d6b5952628a660259b7a398a4223929f985eaa22219dcc.jpg)

![](images/55938486545b03ee3dad4f6aa21ae492a35d83886b62de71941a6146639131b9.jpg)

EXHIBIT 9: Global active funds are returning back to Japanese equities since beginning of the year - they have reduced their UW from -1.6% to -0.48% by May 2026. This is the lowest UW position in Japan held by active global funds since 2009

Global Active Funds Japan Allocation vs. MSCI ACWI IMI Index  
![](images/8183ba383f5890314117c02f9bd646f0908e01d1d7ba1ee18ab803bc7c7358d9.jpg)  
Data till May 31 $^{st}$ 2026
Source: EPFR, Bernstein analysis

EXHIBIT 10: Japan has seen the highest foreign investor flow YTD across the region. YTD, there has been +57.5 bn net FII inflow  
Japan Monthly FII Flows (bn USD)  
![](images/d933a2ccd235a393610d96340546a5014be60fac9cc7b3e444e411570e38485d.jpg)  
Data as of Jul $10^{\text{th}}$ 2026. The FII flow is international portfolio investment that covers investment in equity and debt securities, excluding any such instruments that are classified as direct investment or reserve assets.  
Source: Bloomberg, Bernstein analysis

EXHIBIT 11: YTD, Japan retail investors pulled out -5bn while domestic institutions have net sold -40bn USD.

Japan TSE Domestic Weekly Net Flows Individuals vs. Institutions (USD bn)  
![](images/aeabf7ac227ff9f1ca764c89ff2c69c89ef2b83e2d5e119796f60fb43b2c2afc.jpg)  
Data as of Jul 10 $^{th}$ 2026  
Source: Bloomberg, Bernstein analysis

## JAPAN DOMESTICS VS. EXPORTERS

We started the year with a balanced view on domestics and exporters given the fundamental and macro/political tailwinds were mixed across the two cohorts. YTD, exporters have done better than domestics, largely driven by Semis and Cap goods and some very poor performance by domestic sectors like Software & Services and Food & Staples Retailing. However, interestingly the number of domestic sectors that have outperformed the market are still higher led by Banks, retailing, materials, utilities etc. Domestics still have better top line growth (23% vs. 12% for exporters) and are better proxies of corporate governance reforms with higher dividend yield (2.2% vs. 1.7%) and higher buyback yield (1.3% vs. 0.5%), despite lower ROE (9.3% vs. 11.2%). We believe the currency tailwind for exporters from a weaker Yen is largely behind us as policy is likely to support currency at these levels. However, the scope for relative earnings improvement is higher for exporters compared to domestics while domestics have a huge relative valuation advantage as they trade below -1SD levels relative to exporters. Do note, we already started seeing normalization from extreme net short position on Yen (which reached close to levels last seen in summer of 2024), indicating traders have already started positioning for a stronger Yen from here. The path for policy normalization is also intact with market pricing in 68% probability of a hike in Oct and 100% probability in Dec. Hence, rate cycle and currency are more constructive for domestics. So the biggest support for exporters is coming from continued earnings support while domestics is looking stronger fundamentally and macro-wise. Given these mixed signals, we maintain our preference for both exporters and domestics, though we believe the case for domestics is improving.

EXHIBIT 12: Japan domestics still have better top-line growth vs. exporters (23% vs. 12%) but interestingly since April, we are back to a broad-based improvement in top-line growth across domestics and exporters

Japan Domestics Sale and YoY Growth  
![](images/e17a23ae4bf32b799519c8457ebf0841c7a3e21a70fc73344ca198d73af5085a.jpg)

Japan Exporters Sale and YoY Growth  
![](images/3ee4066303bd65731f09658271d9e17e7438b5bf8a2d8781d93a472328e8d70e.jpg)  
Source: IBES, MSCI, FactSet, Bernstein analysis  
Data till Jun 30 $^{th}$ 2026

EXHIBIT 13: Domestics are still trading at a discount relative to exporters  
12m Fwd. PE Valuation - Domestics relative to Exporters  
![](images/15884c19459b81ae9bafc406f2ceb688dfb5bbbe728898bac1ef3eb87cdd7ac2.jpg)  
Data till Jun 30 $^{th}$ 2026
Source: MSCI, FactSet, Bernstein analysis

EXHIBIT 14: However, earnings revision trends are better for exporters vs. domestics  
Earnings Revision - Domestics relative to Exporters  
![](images/da0fccbbe3a69fcb1ab45ba131af9f4ded934a14b991ee09c469f17be9c9a0c7.jpg)  
Data till Jun 30 $^{th}$ 2026
Source: MSCI, FactSet, Bernstein Analysis

EXHIBIT 15: YTD, net short position on Yen has built-up quite sharply reaching close to levels last seen in 2024 summer. More recently, traders have started changing their stance  
CFTC CME Japanese Yen Net Non-Commercial Futures Positions and Lev

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
