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
# Weekend Consumer Blast: Japan, the revenue management dream

Euan McLeish +81 3 5962 9611 euan.mcleish@bernsteinsg.com

Alexia Howard +1 917 344 8453 alexia.howard@bernsteinsg.com

Aneesha Sherman +1 917 344 8457 aneesha.sherman@bernsteinsg.com

Callum Elliott, CFA, ACA +44 20 7676 7183 callum.elliott@bernsteinsg.com

Danilo Gargiulo +1 917 344 8475 danilo.gargiulo@bernsteinsg.com

Jignanshu Gor +91 226 842 1494 jignanshu.gor@bernsteinsg.com

Luca Solca +41 582 723 126 luca.solca@bernsteinsg.com

Nadine Sarwat, CFA +44 20 7676 6849 nadine.sarwat@bernsteinsg.com

Richard J. Clarke, FCA +44 20 7676 6850 richard.clarke@bernsteinsg.com

Trevor Stirling +44 20 7676 7521 trevor.stirling@bernsteinsg.com

William Woods +44 20 7676 6806 william.woods@bernsteinsg.com

Yugo Shima +81 3 6777 6994 yugo.shima@bernsteinsg.com

Zhihan Ma, CFA +1 917 344 8303 zhihan.ma@bernsteinsg.com

Geographic Where To Play choices (see here) are the bedrock of winning consumer goods strategies and, with huge regional disparities, Japan is a dream for revenue managers.

While many consumer focused executives treat Japan's 47 Prefectures like their children - loving each one equally - those willing to discriminate can effectively compete in a market the same size as South Korea by focusing on just six prefectures.

Brands making this sort of targeted Where To Play choice can benefit from a tailwind of c.30% faster consumption expenditure growth compared to the rest of the country.

EXHIBIT 1: $70\%$ of Japan's population lives in a narrow band stretching from Tokyo to Fukuoka  
![](images/ebfea7fc91ed0394e8999d0fc395dc3f08512d4c804e72741c6e3b88c9b2f5e1.jpg)

As of Oct 2024

Source: Statistics of Japan, Bernstein analysis

Around $70\%$ of Japan's population, totaling c. 87mn people, live in a narrow band stretching from Tokyo in the East to Fukuoka in the West and, while the rest of the country is stunningly beautiful, it is sparsely populated, aging fast and economic activity is dwindling.

Across this concentrated band, six Prefectures stand out. Greater Tokyo, Chiba (just across the Edo River) and Kanagawa (of Yokohama fame) form a compelling Eastern cluster of 37mn consumers. Osaka's scale in the center of Japan is a stone's throw from Aichi (famed for Nagoya city, Ninja culture and Toyota) with a combined 16mn population, and Fukuoka balances out the ellipse close to Japan's Western tip.

Together these Prefectures account for $44\%$ of Japan's working age population and they form the key engine of Japan's Consumer economy.

EXHIBIT 2: The number of households in Tokyo is growing at a 1.5% CAGR, followed by the Six Stars prefectures at 1.3%, more than double the 0.6% rate for the remaining 41 Prefectures

Japan Total Households Growth CAGR (2019-24)

![](images/2e47041a56560ca55c0be92fba503239fca7b62f30da2e2441ea61530b66c5a2.jpg)  
Top 6 Prefectures: Tokyo, Chiba, Kanagawa, Aichi, Osaka, and Fukuoka  
Source: Statistics of Japan, Bernstein analysis

EXHIBIT 3: $44\%$ of Japan's working age population live in six key Prefectures which form the key engine of Japan's Consumer economy

Top 6 Growing Prefectures Working Age Population % of Japan Total  
30mn people, $44\%$ of National Working Age Population  
![](images/87398e33d25b7f8f055e3c7f981f3b896fe3516e5899e19ea30534236827f07b.jpg)  
Source: Statistics of Japan, Bernstein analysis  
EXHIBIT 4: Incomes in these six stars are also significantly outperforming, growing at a $2.8\%$ CAGR from 2019-2024 compared to the rest at $1.3\%$ and, unsurprisingly, Tokyo stands out with $3.1\%$ Income growth

The number of households in these six stars Prefectures is growing at a 1.3% 2019-24 CAGR, more than double the 0.6% rate for the remaining 41 Prefectures.

Incomes in these six stars are also significantly outperforming, growing at a 2.8% CAGR from 2019-2024 compared to the rest at 1.3% and, unsurprisingly, Tokyo stands out with 3.1% Income growth.

When it comes to consuming, however, Chiba really stands out with its $5.1\%$ CAGR materially outstripping Tokyo's $3.2\%$ , the six stars at $2.7\%$ and the rest of the country at only $1.6\%$ .

Japan Income Growth CAGR (2019-24)

![](images/83ab2904bac6cfb3c45c6fe07312581726a47c090a0c132cfdc0811aec869a5b.jpg)  
Top 6 Prefectures: Tokyo, Chiba, Kanagawa, Aichi, Osaka, and Fukuoka  
Source: Statistics of Japan, Bernstein analysis

Known for its beaches and surfing - as well as excessively long travel times into Tokyo from Narita airport - Chiba has a much more relaxed vibe than Tokyo. The Prefecture is drawing a younger crowd of inhabitants who often commute into Tokyo, and is also benefiting from inbound tourism with visitors hitting Disneyland, and the stunning hiking trails.

EXHIBIT 5: Chiba's Consumption Expenditure stands out with a $5.1\%$ CAGR materially outstripping Tokyo's $3.2\%$ , the six stars at $2.7\%$ and the rest of the country at only $1.6\%$

Japan Consumption Expenditure Growth CAGR (2019-24)  
![](images/263d4b961eeb80be9a40f8d83414fcae1bd8b3b695e62cfeaee046ad614bafc4.jpg)  
Top 6 Prefectures: Tokyo, Chiba, Kanagawa, Aichi, Osaka, and Fukuoka  
Source: Statistics of Japan, Bernstein analysis

People in Chiba love drinking, and eating, with total expenditure on non-alcoholic beverages growing almost 4x faster than the six stars average, at a 10.4% CAGR since 2019. Similarly, spend on alcoholic beverage has been growing 1.9x faster, at a 4.3% CAGR, and food spend has been growing 30% faster at a 5.1% CAGR.

EXHIBIT 6: Chiba's total expenditure on Food and Beverages is growing much faster than the Six Stars perfectures average Japan Food & Beverages Expenditure Growth CAGR (2019-24)  
![](images/2dffa896a1258f63c3cdf7c1f4d669b6cbbc156767e19c2a53ab37c9e54c63ec.jpg)  
Greater Tokyo: Tokyo, Chiba, Kanagawa, and Saitama; Top 6 Prefectures: Tokyo, Chiba, Kanagawa, Aichi, Osaka, and Fukuoka  
Source: Statistics of Japan, Bernstein analysis  
EXHIBIT 7: Expenditure on eating out in Tokyo has been growing at an 11% CAGR, compared to the six stars average at a still impressive 7.7% and the remaining 41 prefectures at -0.2%

Outside Chiba, consumer spending on F&B has been growing broadly in line with CPI, however.

When it comes to eating out, Tokyo is where it's at!

Expenditure on eating out in Tokyo has been growing at an 11% CAGR, compared to the six stars average at a still impressive 7.7% and the remaining 41 prefectures at -0.2%.

Presumably, this dynamic growth has been aided by tourism, and partially reflects the dogged devotion of foreign tourists to trudging on and off the Shinkansen along the Golden Route from Tokyo, via Mt Fuji / Hakone, Nagoya, and Kyoto, to Osaka.

Japan Eating Out Expenditure Growth CAGR (2019-24)

![](images/e2adbd9368cf385339a0565af2a72187911dc3a0f25ac7c66efd3dd193cf1d34.jpg)  
Greater Tokyo: Tokyo, Chiba, Kanagawa, and Saitama; Top 6 Prefectures: Tokyo, Chiba, Kanagawa, Aichi, Osaka, and Fukuoka
Source: Statistics of Japan, Bernstein analysis

Based on the increasing prevalence of eating out in Tokyo, cosmetics and personal care expenditure growth in the capital might reasonably be expected to outperform too. But while the 5.1% CAGR is respectable compared to the 4.4% national average, it is again the Chiba people who are focusing on appearances with spend in the prefecture growing at a whopping 7.1% CAGR since 2019.

EXHIBIT 8: In Cosmetics and Personal care expenditure, Greater Tokyo's $5.1\%$ CAGR is well above the $3.8\%$ growth elsewhere, and Chiba again leads the growth at $7.1\%$

Japan Personal Care & Cosmetic Products Expenditure Growth CAGR (2019-24)

![](images/ebd88466e2904e499014e1a21e7d42768592a74e79f2467a687c60b63ea5539c.jpg)  
Greater Tokyo: Tokyo, Chiba, Kanagawa, and Saitama; Top 6 Prefectures: Tokyo, Chiba, Kanagawa, Aichi, Osaka, and Fukuoka  
Source: Statistics of Japan, Bernstein analysis

EXHIBIT 9: Tourism is still highly concentrated along Japan's "Golden Route"  
![](images/8df7bc99b5e2461af8d4145fff8337d0deebe0eb4aa0514a82e695e1b2a663d7.jpg)  
Source: Japan National Tourism Organization Website

## BERNSTEIN TICKER TABLE

<table><tr><td colspan="3"></td><td colspan="2">9 Jul 2026</td><td>TTM</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td>Ticker</td><td>Rating</td><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Rel. Perf.</td><td>Cur</td><td>2026A</td><td>2027E</td><td>2028E</td><td>2026A</td><td>2027E</td><td>2028E</td></tr><tr><td>2802.JP (Ajinomoto)</td><td>O</td><td>JPY</td><td>5,721.00</td><td>7,100.00</td><td>0.5%</td><td>JPY</td><td>138.36</td><td>152.65</td><td>192.70</td><td>41.3</td><td>37.5</td><td>29.7</td></tr><tr><td>2502.JP (Asahi)</td><td>O</td><td>JPY</td><td>1,626.50</td><td>2,700.00</td><td>(57.7)%</td><td>JPY</td><td>100.50</td><td>133.87</td><td>162.55</td><td>16.2</td><td>12.2</td><td>10.0</td></tr><tr><td>2897.JP (Nissin Foods)</td><td>O</td><td>JPY</td><td>2,896.00</td><td>4,700.00</td><td>(44.9)%</td><td>JPY</td><td>98,227</td><td>106,036</td><td>112,956</td><td>10.1</td><td>9.4</td><td>8.8</td></tr><tr><td>2503.JP (Kirin)</td><td>M</td><td>JPY</td><td>2,920.50</td><td>2,800.00</td><td>2.1%</td><td>JPY</td><td>182.13</td><td>219.22</td><td>229.08</td><td>16.0</td><td>13.3</td><td>12.7</td></tr><tr><td>2801.JP (Kikkoman)</td><td>M</td><td>JPY</td><td>1,658.50</td><td>1,600.00</td><td>(15.7)%</td><td>JPY</td><td>106,258</td><td>117,712</td><td>121,745</td><td>14.5</td><td>13.1</td><td>12.7</td></tr><tr><td>2875.JP (Toyo Suisan)</td><td>M</td><td>JPY</td><td>10,735</td><td>11,600</td><td>(25.1)%</td><td>JPY</td><td>104,089</td><td>109,711</td><td>112,436</td><td>9.1</td><td>8.6</td><td>8.4</td></tr><tr><td>2267.JP (Yakult)</td><td>O</td><td>JPY</td><td>2,836.50</td><td>3,600.00</td><td>(37.6)%</td><td>JPY</td><td>150.72</td><td>176.31</td><td>191.28</td><td>18.8</td><td>16.1</td><td>14.8</td></tr><tr><td>JPL</td><td></td><td></td><td>2,610.86</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

2897.JP, 2801.JP, 2875.JP estimate is EBITDA (M); 2897.JP, 2801.JP, 2875.JP valuation is EV/EBITDA (x); 2502.JP, 2503.JP base year is 2025; Source: Bloomberg, Bernstein estimates and analysis.

## I. REQUIRED DISCLOSURES

References to "Bernstein" or the "Firm" in these disclosures relate to the following entities: Bernstein Institutional Services LLC (April 1, 2024 onwards), Bernstein & Co., LLC (pre April 1, 2024), Bernstein Autonomous LLP, BSG France S.A. (April 1, 2024 onwards), Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited, Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社) and analysts employed by SG Africa Technologies & Services to produce Bernstein under a Global Services Agreement in place between Bernstein and SG.

Bernstein is part of a joint venture between SG (SG) and AllianceBernstein, L.P. (AB). Unless specifically noted otherwise, for purposes of these disclosures, references to Bernstein's “affiliates” relate to both SG and AB and their respective affiliates.

## VALUATION METHODOLOGY

This research publication covers six or more companies. For valuation methodology and other company disclosures: Please visit: https://bernstein-autonomous.bluematrix.com/sellside/Disclosures.action.

Or, you can also write to the Director of Compliance, Bernstein Institutional Services LLC, 245 Park Avenue, New York, NY 10167.

## RISKS

This research publication covers six or more companies. For risks and other company disclosures: Please visit: https://bernstein-autonomous.bluematrix.com/sellside/Disclosures.action. Or, you can also write to the Director of Compliance, Bernstein Institutional Services LLC, 245 Park Avenue, New York, NY 10167.

## RATINGS DEFINITIONS, BENCHMARKS AND DISTRIBUTION

## EQUITY RATINGS DEFINITIONS

## Bernstein brand

The Bernstein brand rates stocks based on forecasts of relative performance for the next 12 months versus the S&P 500 for stocks listed on the U.S. and Canadian exchanges, versus the Bloomberg Europe Developed Markets Large and Mid Cap Price Return Index EUR (EDME) for stocks listed on the European exchanges and emerging markets exchanges outside of the Asia Pacific region, versus the Bloomberg Japan Large and Mid Cap Price Return Index USD (JPL) for stocks listed on the Japanese exchanges, and versus the Bloomberg Asia ex-Japan Large and Mid Cap Price Return Index (ASIAX) for stocks listed on the Asian (ex-Japan) exchanges -unless otherwise specified.

The Bernstein brand has three categories of ratings:

\- Outperform: Stock will outpace the market index by more than 15 pp

• Market-Perform: Stock will perform in line with the market index to within +/-15 pp

\- Underperform: Stock will trail the performance of the market index by more than 15 pp

Coverage Suspended: Coverage of a company under the Bernstein brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors on events and developments.

Not Covered (NC) denotes companies that are not under coverage.

Bernstein brand stock ratings are based on a 12-month time horizon.

## Autonomous brand – common stocks

The Autonomous brand rates common stocks as indicated below. As our benchmarks we use the Bloomberg Europe 500 Banks And Financial Services Index (BEBANKS) and Bloomberg Europe Dev Mkt Financials Large and Mid Cap Price Ret Index EUR (EDMFI) index for developed European banks and Payments, the Bloomberg Europe 500 Insurance Index (BEINSUR) for European insurers, the S&P 500 and S&P Financials for US banks and Payments coverage, S5LIFE for US Insurance, the S&P Insurance Select Industry (SPSIINS) for US Non-Life Insurers coverage, and the Bloomberg Emerging Markets Financials Large, Mid and Small Cap Price Return Index (EMLSF) for emerging market banks and insurers and Payments. Ratings are stated relative to the sector (not the market).

The Autonomous brand has three categories of common stock ratings:

\- Outperform (OP): Stock will outpace the relevant index by more than 10 pp

\- Neutral (N): Stock will perform in line with the market index to within +/-10 pp

\- Underperform (UP): Stock will trail the performance of the relevant index by more than 10 pp

Coverage Suspended: Coverage of a company under the Autonomous research brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors on events and developments.

Those denoted as 'Feature' (e.g., Feature Outperform FOP, Feature Under Outperform FUP) are our core ideas.

Not Covered (NC) denotes companies that are not under coverage.

Autonomous brand common stock ratings are based on a 12-month time horizon.

## Autonomous brand – preferred stocks

The Autonomous brand has three categories of preferred stock ratings:

\- Outperform (OP): The total return of the preferred instrument is expected to outperform preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

\- Neutral (N): The total return of the preferred ins

[中间内容因长度限制已省略]

 you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively "Bloomberg"). Bloomberg or Bloomberg's licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg's licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan

KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
