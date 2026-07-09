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
# China Investment Compass - Quarterly

# 3Q26: navigating a K-shaped market

Equity Strategy

## A stock pickers' market with diverging performance

China equities posted divergent performance in 2Q: MSCI China/HSCEI fell 7.6%/9.8%, while ChiNext/STAR 50 surged 38.6%/78.6%, highlighting the gap between internet-heavy HK benchmarks and A-share growth indices. Globally, macro events (eg Iran conflict, the Trump-Xi meeting) had limited market impact, while AI capex drove earnings upgrades across tech supply chains. Positioning became more concentrated and crowded, volatility is elevated, and retail leverage (incl leveraged ETFs) amplified market swings. Sentiment became more fragile amid inflation and liquidity concerns. We continue to view China as a stock pickers' market, with A-shares likely to outperform H-shares until the global AI rally unwinds. We maintain our barbell strategy, favoring both value/yield and sectors with strong earnings support and R.E.A.L. moats.

## Market: inexpensive, but not yet compelling

MSCI China fell 7.6% in 2Q26 in USD terms, underperforming global markets (vs MSCI World: +14.5%, MSCI EM: +23.3%). Within MSCI China, IT was the only sector with positive return in 2Q (+36.7%), while Consumer Discretionary (-20.7%), Consumer Staples (-18.6%) and Materials (-18.3%) were the worst performers. The index currently trades at 10.3x forward P/E, a 12% discount to its long-term average, but still above the historical trough of 8-9x. Earnings remain challenged, with consensus 2026E EPS growth revised down from 11-12% in Jan to 2-3% now. Flow-wise, liquidity pressures are building in 3Q, with nearly HKD540bn of lock-up expiries and a strong IPO pipeline.

## Macro: uneven growth with continued domestic softness

China Investment Compass (CIM) should mostly be in the C4/stimulating phase in 2026. Credit growth slowed from 8.2% in 2025 to 7.7% in 1Q26 and 7.4% in May, alongside weak domestic demand. FAI declined 4.1% YoY, while retail sales rose just 1.4% in 5M26. Exports remained a bright spot (+15.5% YoY in 5M26), but the uneven growth caps investor conviction on China equities. PPI turned positive in Mar-26, after 41 consecutive months of deflation, and rose to 3.9% by May, driving a strong industrial profit growth of 18.8% YoY in 5M26. However, sustainability is questionable given the lower energy prices. Expectations for near-term policy stimulus remain muted.

## Model portfolio: industrials/tech over utilities/consumers

For 3Q26, our quant-driven portfolio upgrades industrials (incl. heavy machinery and electrical equipment) and tech hardware to the Top-10 OW list. We stay positive on communications equipment, which was up 92% in 2Q. We also upgrade diversified financials for strong 2Q earnings, and remain constructive on metals & mining (ex-gold), chemicals, and life sciences sectors. On the other hand, our model downgrades IPPs & renewables and liquors to the Bottom-10 UW list, while remains cautious on the autos, gas & water utilities, real estate, biotech, and household durables sectors.

## 07 July 2026

Equity Strategy
China

BofA
Data Analytics

![](images/77e83dcfcec08cd0f40833320def2cace9e319be41b48ebb3541a230f127cd66.jpg)

## Table of Contents

<table><tr><td>Executive summary: the 3Ms</td><td>2</td></tr><tr><td>Market: inexpensive, but not compelling</td><td>3</td></tr><tr><td>China flow lens</td><td>7</td></tr><tr><td>Macro: export-led, uneven growth</td><td>10</td></tr><tr><td>Other key things investors are watching</td><td>13</td></tr><tr><td>Sector model portfolio</td><td>16</td></tr><tr><td>Appendix</td><td>18</td></tr><tr><td>China Investment Compass (中国投资罗盘)</td><td>18</td></tr><tr><td>Sector classification</td><td>20</td></tr><tr><td>Valuation comp table</td><td>24</td></tr></table>

## Winnie Wu >>

Research Analyst
BofA (Hong Kong)
+852 3508 3058
winnie.wu@bofa.com

Patrick Pan, CFA >>
Research Analyst
BofA (Hong Kong)
+852 3508 4601
patrick.pan2@bofa.com

Gina Wu >>
Strategist
BofA (Hong Kong)
+852 3508 8008
gina.wu@bofa.com

## Glossary

OW: overweight

UW: underweight

R.E.A.L.: Regulatory Critical – Enduring Cycles – Asset Heavy – Local Services

## Executive summary: the 3Ms

Market: MSCI China and H-share significantly underperformed A-share and global markets in 2Q. MSCI China's forward P/E at 10.3x currently is $12\%$ below the long-term average. EPS growth expectations have been reduced to $2 - 3\%$ YoY for 2026E.

Exhibit 1: MSCI China's P/E at 10.3x is $12\%$ below long-term average Forward P/E valuation of MSCI China Index  
![](images/60a2567cdc5d47b49a455c287585e25718f48906ba80d98cff6460792babfaba.jpg)  
Source: Bloomberg, MSCI  
BofA GLOBAL RESEARCH

Exhibit 2: Consensus EPS forecast was cut from >11% in Jan to <3%
Consensus forecast for MSCI China earnings growth  
![](images/c472fe75502ace95e7af485b4b9dfe2447d2e0388f1b7d6b797c78bfb81bf55c.jpg)  
Source: MSCI, FactSet  
BofA GLOBAL RESEARCH

Macro: Credit and nominal GDP growth softened in 5M26, along with weak FAI and consumption, although higher energy prices drove up PPI and industrial profits.

Exhibit 3: China's consumer confidence retreated in Mar-Apr 2026
China consumer confidence index (CCI)  
![](images/38cce390ac944d86435c4b4af9c39d4aacfbde1bed5cac7562d48bb3862abe68.jpg)  
Source: NBS

Exhibit 4: Industrial profit growth accelerated to 18.8% YoY in 5M26
Industrial profit growth (YTD) vs PPI inflation  
![](images/8a7b8ab88934f61ec11062c25a22d0f109bae00ddb32ea0257b8f3bd16dafc73.jpg)  
Source: NBS, CEIC  
BofA GLOBAL RESEARCH

BofA GLOBAL RESEARCH

Model portfolio: For 3Q26, we prefer industrials (heavy machinery, electrical equipment), tech (communications equipment, hardware), and materials. Underweight utilities (IPPs, gas & water), consumers (liquors, auto, durables) and biotech sectors.

Exhibit 5: We prefer brokers/industrials/tech sectors over consumer/utilities in 3Q26
China Investment Compass based model portfolio recommendation: 3Q26

<table><tr><td>#</td><td>Overweight Sectors</td><td>vs 2Q26</td><td>Underweight Sectors</td><td>vs 2Q26</td></tr><tr><td>1</td><td>FI- Diversified Financials</td><td>↑</td><td>UTL- Independent Power &amp; Renewable</td><td>↓</td></tr><tr><td>2</td><td>MAT- Metals &amp; Mining (ex. gold)</td><td>√</td><td>CS- Liquors</td><td>↓</td></tr><tr><td>3</td><td>MAT- Chemicals</td><td>√</td><td>CD- Auto</td><td>√</td></tr><tr><td>4</td><td>IND- Heavy Machinery</td><td>↑</td><td>COM- Telecom</td><td>√</td></tr><tr><td>5</td><td>IND- Electrical Equipment</td><td>↑</td><td>CD- Household Durables</td><td>√</td></tr><tr><td>6</td><td>IT- Communications Equipment</td><td>√</td><td>IND- Construction &amp; Engineering</td><td>↓</td></tr><tr><td>7</td><td>IND- Airline, Logistics &amp; Shipping</td><td>√</td><td>RE- Real Estate</td><td>√</td></tr><tr><td>8</td><td>IT- Technology Hardware</td><td>↑</td><td>HC- Biotechnology</td><td>√</td></tr><tr><td>9</td><td>COM- Interactive Entertainment</td><td>↑</td><td>UTL- Gas &amp; Water Utilities</td><td>√</td></tr><tr><td>10</td><td>HC- Life Sciences Tools &amp; Services</td><td>√</td><td>MAT- Construction Materials &amp; Paper</td><td>↓</td></tr></table>

Source: BofA Global Research \*V shows sectors on our OW/UW list last quarter; ↑ shows new upgrades, ↓ shows new downgrades  
BofA GLOBAL RESEARCH

## Market: inexpensive, but not compelling

## Market performance review

2Q26 was marked by AI-led market leadership, resulting in sharper divergence between tech and non-tech sectors and between A- and H-shares. While investors increasingly looked through geopolitical headlines, concerns over weak domestic demand and an export-reliant economy continued to cap conviction on China equities. In USD terms, KOSPI (+64.2%), ChiNext (+38.6%), and Nikkei 225 (+34.1%) outperformed in 2Q26, while HSCEI (-9.8%), HSI (-7.7%), and MSCI China (-7.6%) lagged. Within MSCI China, IT was the only sector with positive return in 2Q (+36.7%), while Consumer Discretionary (-20.7%), Consumer Staples (-18.6%) and Materials (-18.3%) were the worst performers. A/H-share divergence widened notably: CSI 300 +13.7% in 2Q, while HSCEI -9.8%. P/E valuation of MSCI China fell back to 10.3x, which is a 12% discount to its long-term average, but still above the historical trough of 8-9x.

Exhibit 6: KOSPI, ChiNext, and Nikkei 225 outperformed in 2Q26 while HSCEI, HSI and MSCI China lagged
Comparison of key global market performance  
![](images/4ced1b68520e78aaaad1a7f35dabcc63b3046aa2fc1724c5bb6d683de723a621.jpg)  
Source: Bloomberg, MSCI \*Net return excluding dividend  
BofA GLOBAL RESEARCH

Exhibit 7: IT significantly outperformed in 2Q26, while consumer discretionary, consumer staples and materials lagged
Comparison of MSCI China sector performance  
![](images/cb8c7065cdff7f0bc24d05e2983a8c85393be768b0a6bd6661262e034082654d.jpg)  
Source: Bloomberg, MSCI \*Net return excluding dividend  
BofA GLOBAL RESEARCH

All of the top 10 market cap gainers in 2Q26 came from the tech hardware and semis sectors, whereas the largest market cap losers spread across the energy, internet, consumer and materials sectors.

Exhibit 8: AI hardware and semis stocks were among the top market cap gainers
Top 10 market cap gainers in MSCI China (2Q26)  
![](images/c92a5bf7c3ec38c6fbc03b4aa7e0b7541d1aae9af372295bba6e27584e90bc3d.jpg)  
Source: Bloomberg, MSCI  
BofA GLOBAL RESEARCH

Exhibit 9: Energy, internet and consumer stocks were among the top market cap losers
Top 10 market cap losers in MSCI China (2Q26)  
![](images/53a82982055320d75e604771114b64674f5c8f13629595b99feef40674c98adb.jpg)  
Source: Bloomberg, MSCI  
BofA GLOBAL RESEARCH

AI investing became increasingly nuanced in 2Q26, as markets grappled with shifting narratives around memory supercycles, CPO deployment delays, domestic GPU substitution, and internet platforms' AI monetization. However, a series of brief but sharp sentiment resets from late May highlighted growing investor discomfort. Concentrated holdings, elevated volatility, retail leverage (including leveraged ETFs), and rising inflation and liquidity concerns contributed to increasingly jittery market sentiment. Global yield breakouts, a muted Trump-Xi summit, China's cross-border capital flow tightening, and renewed geopolitical uncertainty further triggered periodic de-risking. The narrow rally also widened the divergence between A-shares and H-shares. China's AI localization theme remained a key source of support for onshore equities, while the offshore Hong Kong market, with lower exposure to domestic semiconductor champions and higher weights in internet and financial stocks, was more vulnerable to earnings risks, macro headwinds, and domestic policy actions.

Policy actions in 2Q26 appeared more targeted, in contrast to the broad-based margin requirement tightening in January. In late May, regulators launched a two-year crackdown on illegal cross-border investment by mainland investors and penalized three online brokers. In addition, the State Council issued Order No. 837 on Outbound Investment, expanding oversight to resident individuals and embeds national security, export control, and cross-border compliance considerations into overseas investment activities. Meanwhile, Chinese tax authorities have stepped up scrutiny of overseas income and assets reported through CRS (Common Reporting Standard) information-sharing mechanisms, prompting investor concerns on outbound wealth flows and offshore asset holdings. These developments raised worries over Hong Kong's liquidity and its insurance, wealth management, and property sectors. Separately, regulatory overhang on large internet platforms resurfaced, as evidenced by SAMR-led actions targeting platform marketing practices during the "618" shopping festival, food delivery competition and safety standards, and online train-ticketing services.

Vibrant IPO market is bright spot amid tech boom, with A-share IPO fundraising +89% YoY to USD10bn in 1H26 and HK proceeds +91% YoY to USD27bn, the strongest first-half on record. Concerns of capital rotation away from existing holdings to fund new offerings, as well as selling pressure from upcoming lock-up expirations of recently listed names, increasingly weighed on near-term sentiment.

Macro activity data in Apr-May pointed to further weakness in domestic demand and investment, and economic growth became increasingly reliant on exports. Policy direction remained broadly consistent. The new overnight rate framework signals higher tolerance for lower rates, while fiscal spending YTD appeared more delayed and conditional. Apr Politburo meeting readout indicated no rush on stimulus and highlighted economic resilience, as market expected. The Lujiazui forum in Jun unveiled a narrower short-term rate corridor (50bp vs. 70bp previously) to improve short-term liquidity guidance, introduced a new “FIMA RMB Repo” to supply offshore yuan liquidity, and relaxed STAR listing criteria to accommodate pre-profit AI model companies.

Geopolitics remained an overhang across Asian markets, but its marginal influence diminished during 2Q26, particularly for A-shares. Investors looked through geopolitical shocks and focused on regions and sectors with stronger AI fundamentals, notably Korea and Taiwan, while China relatively underperformed.

On US-China relations, the Trump-Xi summit in May delivered modest economic agreements, although progress on core disputes remained limited. A positive takeaway was Trump's invitation for Xi to visit the White House in Sep-2026, providing a degree of near-term policy stability. China was also not singled out in the Section 301 findings released in early June; the 12.5% tariff was imposed alongside measures targeting multiple major trading partners over forced-labor concerns. That said, geopolitical and reputational risks continue to rise as new restrictions emerge. In June, the Pentagon updated its Section 1260H list of entities with alleged military ties, adding several major Chinese companies, including Alibaba, Baidu, BYD, CXMT, and Unitree.

Exhibit 10: 2Q26 was shaped by a narrow tech rally. Within China, Star 50, ChiNext, CSI500, and CSI 1000 outperformed NASDAQ Golden Dragon, HSCEI and HSI  
Performance comparison (net return in USD terms, as of Jun 30 $^{th}$ )

<table><tr><td rowspan="2"></td><td rowspan="2">Current level</td><td colspan="8">Performance (%)</td><td colspan="8">Ranking</td></tr><tr><td>1M</td><td>3M</td><td>6M</td><td>12M</td><td>YTD</td><td>3yr</td><td>5yr</td><td>10yr</td><td>1M</td><td>3M</td><td>6M</td><td>12M</td><td>YTD</td><td>3yr</td><td>5yr</td><td>10yr</td></tr><tr><td colspan="18">Major indices</td></tr><tr><td>S&amp;P 500</td><td>7,499</td><td>-1.1</td><td>14.9</td><td>9.6</td><td>20.9</td><td>9.6</td><td>68.5</td><td>74.5</td><td>257.3</td><td>12</td><td>9</td><td>10</td><td>11</td><td>10</td><td>6</td><td>3</td><td>2</td></tr><tr><td>Dow Jones</td><td>52,319</td><td>2.5</td><td>12.9</td><td>8.9</td><td>18.7</td><td>8.9</td><td>52.1</td><td>51.6</td><td>191.8</td><td>7</td><td>11</td><td>11</td><td>12</td><td>11</td><td>9</td><td>5</td><td>4</td></tr><tr><td>NASDAQ</td><td>26,214</td><td>-2.8</td><td>21.4</td><td>12.8</td><td>28.7</td><td>12.8</td><td>90.1</td><td>80.7</td><td>441.3</td><td>13</td><td>5</td><td>8</td><td>9</td><td>8</td><td>4</td><td>2</td><td>1</td></tr><tr><td>Euro Stoxx 50</td><td>6,328</td><td>2.3</td><td>12.4</td><td>6.3</td><td>15.8</td><td>6.3</td><td>50.4</td><td>50.0</td><td>127.7</td><td>8</td><td>12</td><td>12</td><td>13</td><td>12</td><td>10</td><td>6</td><td>7</td></tr><tr><td>FTSE 100</td><td>10,497</td><td>-0.8</td><td>3.4</td><td>4.1</td><td>15.8</td><td>4.1</td><td>45.2</td><td>43.2</td><td>61.2</td><td>11</td><td>14</td><td>14</td><td>14</td><td>14</td><td>11</td><td>7</td><td>9</td></tr><tr><td

[中间内容因长度限制已省略]

ect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content

contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
