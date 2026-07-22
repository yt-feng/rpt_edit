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
Japan Autos & Auto Parts

# Japan Autos & Auto Parts: FY3/27 Q1 Preview - Honda, Suzuki, and Toyota Tsusho poised for strong results

![](images/e44337366575e7a627315b1c9408aa2259dfe07078d166fd2e26968663ec28bb.jpg)  
Masahiro Akita  
+81 3 6777 6998

masahiro.akita@bernsteinsg.com

![](images/86e20ff1223915ae184bfea164c2970ab7ceff2568c91b3faf1c517103202bfa.jpg)

Tomohiro Kashimoto

+81 3 6777 6975

tomohiro.kashimoto@bernsteinsg.com

![](images/fd3218400949fea4a026e38542e0053fb40358ee51e3a68a510ae897831fa21d.jpg)

Seunghyeok Kim

+81 3 6777 6974

seunghyeok.kim@bernsteinsg.com

Ahead of the upcoming earnings season, we review Q1 (April–June) volume trends across our coverage universe and present our outlook for each company's Q1 earnings results.

Honda, Suzuki, and Toyota Tsusho poised for strong results: Key areas of focus for the Japan Autos & Auto Parts sector's Q1 (April–June) earnings are likely to include the earnings benefit from lower US import tariffs, which have declined to 15% this quarter from 27.5% a year ago, as well as headwinds from Middle East-related volume disruptions and higher raw material and logistics costs. Within our coverage, we see Honda, Suzuki, and Toyota Tsusho as the most likely positive standouts this earnings season. Meanwhile, although we forecast YoY profit declines for Subaru and Toyota, both companies are still expected to deliver broadly favorable results, driven by earnings that should exceed consensus expectations and healthy progress toward their initial full-year guidance.

Suzuki and Honda likely to stand out in Q1 sales performance: Aggregate Q1 sales across our coverage are estimated to rise 3.9% YoY. Suzuki is expected to post the strongest growth, driven by robust demand in India, while Honda should benefit from strong HEV sales in the US and improving demand in Japan. Subaru's sales trend also remains solid. By contrast, Nissan, Mazda, and Toyota are likely to see modest sales declines. However, Toyota's latest production plan points to a return to YoY growth from Q2 onward, suggesting sales momentum should improve in the coming quarters.

Particularly bullish on Honda and Suzuki into Q1 results: Honda and Suzuki stand out as the most compelling Q1 earnings stories within our coverage. We expect both companies to deliver solid YoY profit growth and outperform current consensus expectations. Honda should benefit from strong US HEV demand, lower tariff costs, and the absence of last year's sizable EV-related charges, potentially resulting in exceptionally strong progress against full-year guidance. Suzuki is also well positioned, supported by robust volume growth in India and resilient earnings momentum. While Subaru and Toyota are expected to report YoY declines in operating profit, both are still likely to deliver favorable results relative to market expectations. By contrast, Nissan and Mazda are likely to be relative laggards, reflecting weaker earnings momentum and limited progress against their initial full-year guidance.

Toyota Tsusho likely to stand out among Toyota affiliates: While Denso and Aisin are unlikely to deliver significant earnings surprises, we expect Toyota Tsusho's Q1 net profit to exceed expectations, primarily driven by strong Toyota Land Cruiser sales in Africa. Although lower Toyota production volumes remain a headwind for Denso and Aisin, favorable FX and tariff pass-through measures should support broadly stable earnings, making a significant earnings surprise unlikely. By contrast, Toyota Tsusho appears well positioned to outperform expectations. Our analysis shows that Land Cruiser sales in Africa and EUR/JPY are both highly correlated with earnings in Toyota Tsusho's Africa business net profit. With IHS forecasting African Land Cruiser sales to increase 28.4% YoY in Q1 and EUR/JPY remaining supportive, we expect robust earnings growth in the Africa business, increasing the likelihood of a meaningful upside surprise in Q1 earnings.

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2"></td><td colspan="4">17 Jul 2026</td><td>TTM</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td></td><td></td><td rowspan="2">Closing Price</td><td rowspan="2">Price Target</td><td rowspan="2">Rel. Perf.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Ticker</td><td>Rating</td><td>Cur</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>7203.JP (Toyota)</td><td>O</td><td>JPY</td><td>2,899.50</td><td>4,200.00</td><td>(25.1)%</td><td>JPY</td><td>295.25</td><td>308.93</td><td>367.29</td><td>9.8</td><td>9.4</td><td>7.9</td></tr><tr><td>7269.JP (Suzuki)</td><td>O</td><td>JPY</td><td>2,050.50</td><td>2,550.00</td><td>(13.9)%</td><td>JPY</td><td>227.69</td><td>234.71</td><td>255.99</td><td>9.0</td><td>8.7</td><td>8.0</td></tr><tr><td>7267.JP (Honda)</td><td>M</td><td>JPY</td><td>1,535.50</td><td>1,300.00</td><td>(37.1)%</td><td>JPY</td><td>(106.06)</td><td>161.84</td><td>147.24</td><td>(14.5)</td><td>9.5</td><td>10.4</td></tr><tr><td>7201.JP (Nissan)</td><td>U</td><td>JPY</td><td>329.30</td><td>350.00</td><td>(32.5)%</td><td>JPY</td><td>(152.58)</td><td>4.78</td><td>53.06</td><td>(2.2)</td><td>68.8</td><td>6.2</td></tr><tr><td>7261.JP (Mazda)</td><td>U</td><td>JPY</td><td>1,137.00</td><td>1,000.00</td><td>(5.9)%</td><td>JPY</td><td>55.64</td><td>116.61</td><td>142.17</td><td>20.4</td><td>9.8</td><td>8.0</td></tr><tr><td>7270.JP (Subaru)</td><td>U</td><td>JPY</td><td>2,534.00</td><td>2,350.00</td><td>(39.8)%</td><td>JPY</td><td>125.50</td><td>222.96</td><td>249.75</td><td>20.2</td><td>11.4</td><td>10.1</td></tr><tr><td>8015.JP (Toyota Tsusho)</td><td>O</td><td>JPY</td><td>6,076.00</td><td>8,150.00</td><td>46.2%</td><td>JPY</td><td>350.95</td><td>451.35</td><td>489.20</td><td>17.3</td><td>13.5</td><td>12.4</td></tr><tr><td>6902.JP (Denso)</td><td>M</td><td>JPY</td><td>1,964.00</td><td>2,050.00</td><td>(39.9)%</td><td>JPY</td><td>162.96</td><td>169.90</td><td>190.05</td><td>12.1</td><td>11.6</td><td>10.3</td></tr><tr><td>7259.JP (Aisin)</td><td>M</td><td>JPY</td><td>2,256.00</td><td>2,450.00</td><td>(20.4)%</td><td>JPY</td><td>232.64</td><td>248.13</td><td>236.66</td><td>9.7</td><td>9.1</td><td>9.5</td></tr><tr><td>JPL</td><td></td><td></td><td>2,545.21</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We rate Toyota as Outperform with a price target of JPY 4,200.

We rate Suzuki as Outperform with a price target of JPY 2,550.

We rate Honda as Market-Perform with a price target of JPY 1,300.

We rate Nissan as Underperform with a price target of JPY 350.

We rate Mazda as Underperform with a price target of JPY 1,000.

We rate Subaru as Underperform with a price target of JPY 2,350.

We rate Toyota Tsusho as Outperform with a price target of JPY 8,150.

We rate Denso as Market-Perform with a price target of JPY 2,050.

We rate Aisin as Market-Perform with a price target of JPY 2,450.

## DETAILS

## SUZUKI AND HONDA LIKELY TO STAND OUT IN Q1 SALES PERFORMANCE

Based on our estimates of vehicle sales in key markets excluding China, which do not directly impact the consolidated revenues and operating profits of the six Japanese automakers under our coverage, aggregate Q1 (April–June) sales are likely to increase by 3.9% YoY on average (Exhibit 1). That said, performance is expected to vary considerably across automakers.

Suzuki is likely to deliver the strongest growth, with global sales estimated to rise 18.4% YoY (Exhibit 2). The key driver remains India, where sales are projected to increase 33% YoY, benefiting significantly from the GST rate cuts implemented last year. With the Kharkhoda plant commencing operations in May, we expect this momentum to continue in the near term. In Japan, Suzuki also appears to have maintained resilient performance, with sales estimated to decline only 0.7% YoY, despite a temporary shift in demand from mini vehicles toward registered vehicles following the April tax changes.

Honda is expected to post the second-strongest performance, with global sales estimated to increase 5.9% YoY (Exhibit 3). Growth is likely to be led by the US, where sales are projected to rise 8.4% YoY, supported by record HEV sales, particularly of the CR-V. Japanese sales are also estimated to increase 8.2% YoY, benefiting from stronger demand for registered vehicles following the tax changes, as well as continued ramp up of the recently launched CR-V.

Subaru is also expected to deliver solid results, with sales estimated to increase 2.1% YoY (Exhibit 4). The US should remain the key contributor, supported by growing demand for the HEV versions of the Forester and Crosstrek. In contrast, Nissan's sales are estimated to decline 0.8% YoY (Exhibit 5). While US sales are projected to increase 9.6% YoY, supported by locally produced models such as the Rogue, Pathfinder, and Frontier, weakness in Europe and Asia is likely to offset these gains.

Mazda's sales are estimated to decline 1.0% YoY (Exhibit 6). The newly launched CX-5, a key focus for the market, had already been introduced in Europe and was rolled out in North America and Japan during the quarter. Europe continues to show positive momentum, while the new CX-5 also appears to be contributing to stronger sales in Japan. North American sales are likewise expected to return to growth. However, while Mazda3 and CX-50 HEV sales have been expanding in the US, sales of the CX-5 have been declining, warranting further evaluation. Overall, gains in Europe, Japan, and North America are likely to be more than offset by weakness in other markets, resulting in a modest YoY decline.

Toyota's sales are estimated to decline 1.4% YoY (Exhibit 7). Relative to peers, Q1 may appear somewhat soft, although sales remain healthy in key markets such as the US and Japan. The primary headwind appears to be a sharp decline in exports and sales to the Middle East, where Toyota has the greatest exposure among Japanese automakers. In the US, HEV models such as the Camry and RAV4 continue to post robust sales growth. In Japan, strong demand for the new RAV4, Corolla Cross, and Lexus NX is likely providing support. While Q1 global sales are expected to be slightly down YoY, Toyota's latest July to September production plan implies 3.4% YoY growth globally, suggesting sales momentum should recover from Q2 onward.

EXHIBIT 1: Suzuki and Honda likely to stand out in Q1 sales performance  
![](images/f9b4b9cda9bef8ed5de469d7f56b5e4f162fe16e87b7c8bd5e9dcde70ad69de7.jpg)  
Note: Apr-May 2026 figures are based on officially disclosed company data, while Jun figures are based on publicly available country-level data where available, and estimates derived from country-level data for markets where June data have not yet been released
Source: Company reports, Marklines, Autodata, JADA, Zenkeijikyo, ACEA, SMMT, PFA, KBA, FADA, Gaikindo, Bernstein analysis and estimates

EXHIBIT 2: Suzuki's estimated FY3/27 Q1 sales volume reached 893k units (+18.4% YoY)  
![](images/097aa4c4c407c54de305c6b5340496536f31ccd8edaeee516722bb664353035d.jpg)  
Note: Apr-May 2026 figures are based on officially disclosed company data, while Jun figures are based on publicly available country-level data where available, and estimates derived from country-level data for markets where June data have not yet been released  
Source: Company reports, Marklines, Autodata, JADA, Zenkeijikyo, ACEA, SMMT, PFA, KBA, FADA, Gaikindo, Bernstein analysis and estimates

EXHIBIT 3: Honda's estimated FY3/27 Q1 sales volume (excluding China) reached 756k units (+5.9% YoY)  
![](images/9bdf797e3aa83bf6a4855bb6f9bd2a518ffadc6e7e781bbac7a79237bdcf3dea.jpg)  
Note: Apr-May 2026 figures are based on officially disclosed company data, while Jun figures are based on publicly available country-level data where available, and estimates derived from country-level data for markets where June data have not yet been released  
Source: Company reports, Marklines, Autodata, JADA, Zenkeijikyo, ACEA, SMMT, PFA, KBA, FADA, Gaikindo, Bernstein analysis and estimates

EXHIBIT 4: Subaru's estimated FY3/27 Q1 sales volume reached 229k units (+18.4% YoY)  
![](images/4f3d6f61a22ec8f45ecfb5c89fc9a6988272e25d28302b38411ba85b1ecae918.jpg)  
Note: Apr-May 2026 figures are based on officially disclosed company data, while Jun figures are based on publicly available country-level data where available, and estimates derived from country-level data for markets where June data have not yet been released  
Source: Company reports, Marklines, Autodata, JADA, Zenkeijikyo, ACEA, SMMT, PFA, KBA, FADA, Gaikindo, Bernstein analysis and estimates

EXHIBIT 5: Nissan's estimated FY3/27 Q1 sales volume (excluding China) reached 581k units (-0.8% YoY)  
![](images/46c542dfb4c84aebef6d2100ba8fc4ff219969bfca919b9780947121f956740b.jpg)  
Note: Apr-May 2026 figures are based on officially disclosed company data, while Jun figures are based on publicly available country-level data where available, and estimates derived from country-level data for markets where June data have not yet been released  
Source: Company reports, Marklines, Autodata, JADA, Zenkeijikyo, ACEA, SMMT, PFA, KBA, FADA, Gaikindo, Bernstein analysis and estimates

EXHIBIT 6: Mazda's estimated FY3/27 Q1 sales volume (excluding China) reached 280k units (-1.0% YoY)  
![](images/92a81e1093a4d6279da1196aa0defeb9ea819822b95f366f045d33d6b302e246.jpg)  
Note: Apr-May 2026 figures are based on officially disclosed company data, while Jun figures are based on publicly available country-level data where available, and estimates derived from country-level data for markets where June data have not yet been released  
Source: Company reports, Marklines, Autodata, JADA, Zenkeijikyo, ACEA, SMMT, PFA, KBA, FADA, Gaikindo, Bernstein analysis and estimates

EXHIBIT 7: Toyota's estimated FY3/27 Q1 sales volume (excluding China) reached 2,327k units (-1.4% YoY)  
![](images/ae9b37b75e2f0db4aff002db00819106b0f2827dde3d21553078bb6e1cbd06ab.jpg)  
Note: Apr-May 2026 figures are based on officially disclosed company data, while Jun figures are based on publicly available country-level data where available, and estimates derived from country-level data for markets where June data have not yet been released  
Source: Company reports, Marklines, Autodata, JADA, Zenkeijikyo, ACEA, SMMT, PFA, KBA, FADA, Gaikindo, Bernstein analysis and estimates

## PARTICULARLY BULLISH ON HONDA AND SUZUKI INTO Q1 RESULTS

Key areas of focus for the Japanese auto sector's Q1 (April–June) earnings are likely to include the earnings benefit from lower US import tariffs, which have declined to 15% this quarter from 27.5% a year ago, as well as headwinds from Middle East-related volume disruptions and higher raw material and logistics costs.

Based on our estimates derived from Q1 sales trends across our coverage universe, we expect automakers' operating profit to increase by an average of 6.5% YoY (Exhibit 8). Among OEMs, we forecast Honda, Suzuki, Nissan, and Mazda to deliver YoY profit growth, while Subaru and Toyota are likely to post YoY declines. Relative to current consensus expectations, we see upside potential for Subaru, Honda, Suzuki, and Toyota, while Mazda appears at risk of missing expectations (Exhibit 9). Although consensus forecasts for Nissan remain widely dispersed, suggesting limited market visibility, we believe earnings are likely to exceed the current median estimate of JPY 4.4bn.

We also expect investors to focus on Q1 progress against full-year operating profit

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
