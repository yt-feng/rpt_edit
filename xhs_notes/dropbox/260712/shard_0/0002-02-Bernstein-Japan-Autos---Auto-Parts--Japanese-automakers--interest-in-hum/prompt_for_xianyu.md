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

# Japan Autos & Auto Parts: Japanese automakers' interest in humanoid robots appears to be re-emerging

![](images/2ba368c6768233e7a349887c1221084d90b13d5a10f5b120001f4fa4bbebd945.jpg)

Masahiro Akita

+81 3 6777 6998

masahiro.akita@bernsteinsg.com

![](images/bfd31a44f8b03b849f6130603c193029bac410fc0a6aac109517c7d48bedfec9.jpg)

Tomohiro Kashimoto

+81 3 6777 6975

tomohiro.kashimoto@bernsteinsg.com

![](images/9774b886fb6a63b4905feed4ac4da66e19b48bbbd12c58ff0b2555422557887c.jpg)

Seunghyeok Kim

+81 3 6777 6974

seunghyeok.kim@bernsteinsg.com

Yesterday, Mitsubishi Motors announced that it had entered into an MOU with a Japanese startup to jointly develop and mass-produce humanoid robots. As is well known, Japanese automakers have a history of involvement in robotics. As the global automotive market becomes increasingly challenging, will Japanese automakers step up their efforts in robotics as an alternative growth engine?

Mitsubishi eyes humanoid robot development and mass production: Mitsubishi Motors (MMC, not covered) has signed an MOU (link) with Highlanders, a University of Tokyo spin-off specializing in humanoid robotics, to jointly develop and mass-produce humanoid robots based on Highlanders' humanoid robot platform, 'N'. The partnership includes plans to deploy robots at MMC's manufacturing facilities while leveraging the automaker's expertise in mass-production and quality assurance. Production is expected at MMC's Kyoto plant, utilizing idle factory space, with an initial target capacity of 1,000 units per month as early as 2027. MMC, which has already invested in Highlanders, also plans to increase its stake to support commercialization. As investor interest in humanoid robotics continues to grow, we view the announcement positively for the sector as it signals that Japanese automakers are taking steps toward cultivating a new mid- to long-term growth driver beyond its automotive business.

Japanese automakers have a history of involvement in robotics: Japanese automakers have a long, albeit uneven, history of involvement in robotics. Honda is widely regarded as the industry's pioneer, having begun bipedal humanoid robot research in 1986 and unveiling ASIMO in 2000, one of the world's best-known humanoids. Toyota followed with its Partner Robot program in the 2000s, targeting assistance, healthcare, and human-machine interaction applications. While these initiatives demonstrated how automotive expertise in sensing, motion control, and mechatronics could be applied beyond vehicles, robotics remained primarily a research activity rather than a commercial business.

Global humanoid robot market to reach USD 729 bn by 2025: We forecast global humanoid robot shipment to reach 49 mn units by 2050 (2025-2050 CAGR of \~37%), with the market expanding to \~USD 729 bn (\~32% CAGR), making humanoid robotics an attractive growth opportunity for automakers. The sector is particularly relevant to the automotive industry given the overlap in core technologies, including actuators (motors, gear reducers, etc.), sensors, batteries, control units, and AI-enabled software, areas in which automakers and suppliers have built expertise through vehicle development. Amid intensifying competition, labor shortages, and rapid AI advances, Japanese automakers' interest in humanoid robotics appears to be re-emerging. Toyota also highlighted robotics initiatives in factories, including parts logistics and picking processes, at its latest earnings briefing. The company further indicated that it ultimately extends robotics applications beyond manufacturing into healthcare and retail. The market will likely watch for more concrete commercialization efforts.

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="3">Ticker</td><td colspan="5">9 Jul 2026</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td></td><td></td><td rowspan="2">Closing Price</td><td rowspan="2">Price Target</td><td rowspan="2">TTM Rel. Perf.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Rating</td><td>Cur</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>7203.JP (Toyota)</td><td>O</td><td>JPY</td><td>2,824.00</td><td>4,200.00</td><td>(31.9)%</td><td>JPY</td><td>295.25</td><td>308.93</td><td>367.29</td><td>9.6</td><td>9.1</td><td>7.7</td></tr><tr><td>7269.JP (Suzuki)</td><td>O</td><td>JPY</td><td>2,027.50</td><td>2,550.00</td><td>(23.3)%</td><td>JPY</td><td>227.69</td><td>234.71</td><td>255.99</td><td>8.9</td><td>8.6</td><td>7.9</td></tr><tr><td>7267.JP (Honda)</td><td>M</td><td>JPY</td><td>1,502.00</td><td>1,300.00</td><td>(44.9)%</td><td>JPY</td><td>(106.06)</td><td>161.84</td><td>147.24</td><td>(14.2)</td><td>9.3</td><td>10.2</td></tr><tr><td>7201.JP (Nissan)</td><td>U</td><td>JPY</td><td>304.50</td><td>350.00</td><td>(45.6)%</td><td>JPY</td><td>(152.58)</td><td>4.78</td><td>53.06</td><td>(2.0)</td><td>63.6</td><td>5.7</td></tr><tr><td>7261.JP (Mazda)</td><td>U</td><td>JPY</td><td>1,106.00</td><td>1,000.00</td><td>(15.0)%</td><td>JPY</td><td>55.64</td><td>116.61</td><td>142.17</td><td>19.9</td><td>9.5</td><td>7.8</td></tr><tr><td>7270.JP (Subaru)</td><td>U</td><td>JPY</td><td>2,488.50</td><td>2,350.00</td><td>(47.4)%</td><td>JPY</td><td>125.50</td><td>222.96</td><td>249.75</td><td>19.8</td><td>11.2</td><td>10.0</td></tr><tr><td>8015.JP (Toyota Tsusho)</td><td>O</td><td>JPY</td><td>6,110.00</td><td>8,150.00</td><td>42.5%</td><td>JPY</td><td>350.95</td><td>451.35</td><td>489.20</td><td>17.4</td><td>13.5</td><td>12.5</td></tr><tr><td>6902.JP (Denso)</td><td>M</td><td>JPY</td><td>1,928.00</td><td>2,050.00</td><td>(47.2)%</td><td>JPY</td><td>162.96</td><td>169.90</td><td>190.05</td><td>11.8</td><td>11.3</td><td>10.1</td></tr><tr><td>7259.JP (Aisin)</td><td>M</td><td>JPY</td><td>2,289.50</td><td>2,450.00</td><td>(23.8)%</td><td>JPY</td><td>232.64</td><td>248.13</td><td>236.66</td><td>9.8</td><td>9.2</td><td>9.7</td></tr><tr><td>JPL</td><td></td><td></td><td>2,629.48</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We rate Toyota as Outperform with a price target of JPY 4,200.00.

We rate Suzuki as Outperform with a price target of JPY 2,550.00.

We rate Honda as Market-Perform with a price target of JPY 1,300.00.

We rate Nissan as Underperform with a price target of JPY 350.00.

We rate Mazda as Underperform with a price target of JPY 1,000.00.

We rate Subaru as Underperform with a price target of JPY 2,350.00.

We rate Toyota Tsusho as Outperform with a price target of JPY 8,150.00.

We rate Denso as Market-Perform with a price target of JPY 2,050.00.

We rate Aisin as Market-Perform with a price target of JPY 2,450.00.

## DETAILS

EXHIBIT 1: Highlanders' humanoid robot 'N'  
![](images/81ded896de774babc73da1a62bd71bdeb6f56b61d95e4160a0e00d75085dce9b.jpg)  
Source: Company webstie  
EXHIBIT 2: Honda's history of robotics development

![](images/881c3c559dc05f3962c1adf88b085258ed7174b86f936d19cdb209bc3f49d5b4.jpg)  
Source: Company website

EXHIBIT 3: Toyota's 'Mobility Robot'  
![](images/05ec0f051e98129da0e7aeeeba9a31bff3d98db3b43ecc005204ac895f790893.jpg)  
Source: Company website

EXHIBIT 4: Toyota's 'Violin-Playing Robot'  
![](images/fcc19881dcf6d75ac859d8eaa1033c021e513ab26cadb196efa65a0e3f1befbb.jpg)

EXHIBIT 5: Toyota Research Institute's robots in a factory  
![](images/2ae36eb58d8518daa8f49c2b0ed195ae20110ad8a1de5d75e8f6c5fcf2b19222.jpg)  
Source: Company website  
Source: Company website

EXHIBIT 6: Toyota Research Institute's humanoid robot for mobile manipulation  
![](images/2e7977bf2ddb362b42c50103744cb7319f9878f97eaae565c3bb60f066202956.jpg)  
Source: Company website

EXHIBIT 7: We forecast global humanoid robot shipment to reach 49 mn units by 2050  
![](images/df2182c36a8da05d35a72658d3573223a6b9b06d66c3e0906a4305e0402d1109.jpg)  
Source: Bernstein's Asia Emerging Robotics team, Bernstein analysis and estimates

EXHIBIT 8: We forecast global humanoid market size to reach USD 729 bn by 2050  
![](images/b785abd1949f8f0236b1d530abc11293ee0055137e44ff1ed328a52cecca0549.jpg)  
Source: Bernstein's Asia Emerging Robotics team, Bernstein analysis and estimates

## I. REQUIRED DISCLOSURES

References to "Bernstein" or the "Firm" in these disclosures relate to the following entities: Bernstein Institutional Services LLC (April 1, 2024 onwards), Bernstein & Co., LLC (pre April 1, 2024), Bernstein Autonomous LLP, BSG France S.A. (April 1, 2024 onwards), Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited, Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社) and analysts employed by SG Africa Technologies & Services to produce Bernstein under a Global Services Agreement in place between Bernstein and SG.

Bernstein is part of a joint venture between SG (SG) and AllianceBernstein, L.P. (AB). Unless specifically noted otherwise, for purposes of these disclosures, references to Bernstein's “affiliates” relate to both SG and AB and their respective affiliates.

## VALUATION METHODOLOGY

This research publication covers six or more companies. For valuation methodology and other company disclosures: Please visit: https://bernstein-autonomous.bluematrix.com/sellside/Disclosures.action.

Or, you can also write to the Director of Compliance, Bernstein Institutional Services LLC, 245 Park Avenue, New York, NY 10167.

## RISKS

This research publication covers six or more companies. For risks and other company disclosures:

Please visit: https://bernstein-autonomous.bluematrix.com/sellside/Disclosures.action.

Or, you can also write to the Director of Compliance, Bernstein Institutional Services LLC, 245 Park Avenue, New York, NY 10167.

RATINGS DEFINITIONS, BENCHMARKS AND DISTRIBUTION

## EQUITY RATINGS DEFINITIONS

## Bernstein brand

The Bernstein brand rates stocks based on forecasts of relative performance for the next 12 months versus the S&P 500 for stocks listed on the U.S. and Canadian exchanges, versus the Bloomberg Europe Developed Markets Large and Mid Cap Price Return Index EUR (EDME) for stocks listed on the European exchanges and emerging markets exchanges outside of the Asia Pacific region, versus the Bloomberg Japan Large and Mid Cap Price Return Index USD (JPL) for stocks listed on the Japanese exchanges, and versus the Bloomberg Asia ex-Japan Large and Mid Cap Price Return Index (ASIAX) for stocks listed on the Asian (ex-Japan) exchanges -unless otherwise specified.

The Bernstein brand has three categories of ratings:

\- Outperform: Stock will outpace the market index by more than 15 pp

• Market-Perform: Stock will perform in line with the market index to within +/-15 pp

• Underperform: Stock will trail the performance of the market index by more than 15 pp

Coverage Suspended: Coverage of a company under the Bernstein brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors on events and developments.

Not Covered (NC) denotes companies that are not under coverage.

Bernstein brand stock ratings are based on a 12-month time horizon.

Autonomous brand – common stocks

The Autonomous brand rates common stocks as indicated below. As our benchmarks we use the Bloomberg Europe 500 Banks And Financial Services Index (BEBANKS) and Bloomberg Europe Dev Mkt Financials Large and Mid Cap Price Ret Index EUR (EDMFI) index for developed European banks and Payments, the Bloomberg Europe 500 Insurance Index (BEINSUR) for European insurers, the S&P 500 and S&P Financials for US banks and Payments coverage, S5LIFE for US Insurance, the S&P Insurance Select Industry (SPSIINS) for US Non-Life Insurers coverage, and the Bloomberg Emerging Markets Financials Large, Mid and Small Cap Price Return Index (EMLSF) for emerging market banks and insurers and Payments. Ratings are stated relative to the sector (not the market).

The Autonomous brand has three categories of common stock ratings:

\- Outperform (OP): Stock will outpace the relevant index by more than 10 pp

\- Neutral (N): Stock will perform in line with the market index to within +/-10 pp

\- Underperform (UP): Stock will trail the performance of the relevant index by more than 10 pp

Coverage Suspended: Coverage of a company under the Autonomous research brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors on events and developments.

Those denoted as ‘Feature’ (e.g., Feature Outperform FOP, Feature Under Outperform FUP) are our core ideas.

Not Covered (NC) denotes companies that are not under coverage.

Autonomous brand common stock ratings are based on a 12-month time horizon.

## Autonomous brand – preferred stocks

The Autonomous brand has three categories of preferred stock ratings:

\- Outperform (OP): The total return of the preferred instrument is expected to outperform preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

\- Neutral (N): The total return of the preferred instrument is expected to perform in line with preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

\- Underperform (UP): The total return of the preferred instrument is expected to underperform preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

Autonomous preferred stock ratings are based on a 6-month time horizon.

## AUTONOMOUS CREDIT RESEARCH

Where this report contains investment recommendations for credit instruments, as defined in article 3(1)(35) of the Market Abuse Regulation, the information below is presented to comply with its disclosure requirements.

The report may also include reference(s) to published opinions by other Autonomous or Bernstein analysts covering the equity securities of the issuer(s) referenced herein. Please note an investment recommendation for credit instruments published by the author(s) of this report may differ from the published view of the analyst covering equity securities for the issuer(s) contained in this report and vice versa.

## CREDIT RATINGS DEFINITIONS

The Autonomous brand has three categories of credit ratings:

\- Credit Outperform (C-OP): The total return of the Reference Credit Instrument is expected to outperform the credit spread of bonds of other issuers operating in similar sectors or rating categories over the next six months.

\- Credit Neutral (C-N): The total return of the Reference Credit Instrument is expected to perform in line with the credit spread of bonds of other issuers operating in similar sectors or rating categories over the next six months.

\- Credit Underperform (C-UP): The total return of the Reference Credit Instrument is expected to underperform the credit spread of bonds of other issuers operating in similar sectors or rating categories

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
