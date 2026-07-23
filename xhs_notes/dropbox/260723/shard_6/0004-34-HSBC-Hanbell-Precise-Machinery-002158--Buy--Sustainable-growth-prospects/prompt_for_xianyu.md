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
# Hanbell Precise Machinery (002158 CH)

Buy: Sustainable growth prospects

\- 2026 growth will not be fast, but we see increasing visibility of growth prospects from 2027 and beyond 2030

Semiconductor business will first register significant growth off a low base; AIDC and industrial heat pump to follow suit

◆ Maintain Buy rating and TP of RMB38.80

Growth outlook unchanged despite recent stock volatility: Over the past three months, Hanbell's share price has been relatively volatile, in line with other China semiconductor equipment names. The market regards Hanbell as a semiconductor play, mainly because of high expectations of domestic semiconductor market growth driven by AI development and the large market share gain potential in semiconductor vacuum pumps for Hanbell, we believe. We forecast Hanbell's semiconductor vacuum pump revenue to increase from an estimated RMB100m in 2025 to RMB202m in 2026e, which is significant considering this business has been flattish since 2021 for Hanbell. We expect this segment to grow even faster in 2027 as Hanbell completes product certification for more downstream clients for 12-inch equipment, including for memory chips (see pages 5-6 for more details).

Market size is key: We like Hanbell mainly because it has exposure to several industries with large markets, which should ensure consecutive growth for the next 10 years for the company. While supply shortages of refrigerant compressors for US AIDC do not look as severe (compared to some other equipment), our latest global market forecast of magnetic levitation compressors for data centres is RMB16.9bn in 2028e (pages 3-4), which indicates decent growth potential for Hanbell. We think downstream AIDC heat solution providers will not solely rely on Danfoss for magnetic levitation compressor supply and will find second or third suppliers. In addition, while the China industrial heat pump market has grown slower than our expectations in 1H26, but this does not change our long-term investment thesis. Currently, industrial heat pump demand is effectively helping Hanbell to mitigate the weakness in central air conditioning and refrigeration markets. In 1H26, China data centre demand and the industrial heat pump market registered 13.6% and 15.5% y-o-y growth, respectively. We also highlight the potential of Europe's industrial heat pump market (pages 8-9).

Maintain Buy; 2026-28 earnings and TP of RMB38.80 unchanged: We make no changes to our 2026-28 net profit estimates and our DCF-based TP remains RMB38.80. The stock is trading at 23.8x 2026e PE and 17.6x 2027e PE, compared with its historical average of 19x since 2016. Our target price of RMB38.80 implies 44.4% upside to the current stock price and we therefore maintain our Buy rating. See key downside risks on page 11.

## Disclosures & Disclaimer

This report must be read with the disclosures and the analyst certifications in the Disclosure appendix, and with the Disclaimer, which forms part of it.

## Equities Machinery

China

![](images/9f9468b759f1ee6cef352debec2883a1be6ac761def275b72f1cda2ff2de5b70.jpg)

## MAINTAIN BUY

TARGET PRICE (CNY) PREVIOUS TARGET (CNY)

38.80 38.80

SHARE PRICE (CNY) UPSIDE/DOWNSIDE

26.87 +44.4%

## MARKET DATA

<table><tr><td>Market cap (CNYm)</td><td>14368.0</td></tr><tr><td>Market cap (USDm)</td><td>2120.2</td></tr><tr><td>3m ADTV (USDm)</td><td>88.1</td></tr></table>

<table><tr><td>Free float</td><td>39%</td></tr><tr><td>BBG</td><td>002158 CH</td></tr><tr><td>RIC</td><td>002158.SZ</td></tr></table>

FINANCIALS AND RATIOS (CNY)

<table><tr><td>Year to</td><td>12/2025a</td><td>12/2026e</td><td>12/2027e</td><td>12/2028e</td></tr><tr><td>HSBC QH EPS</td><td>0.88</td><td>1.13</td><td>1.53</td><td>2.15</td></tr><tr><td>HSBC QH EPS prev</td><td>0.88</td><td>1.13</td><td>1.53</td><td>2.15</td></tr><tr><td>Change (%)</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Consensus EPS</td><td>1.13</td><td>1.11</td><td>1.36</td><td>1.64</td></tr><tr><td>PE (x)</td><td>30.7</td><td>23.8</td><td>17.6</td><td>12.5</td></tr><tr><td>Dividend yield (%)</td><td>1.7</td><td>2.2</td><td>2.9</td><td>4.1</td></tr><tr><td>EV/EBITDA (x)</td><td>19.7</td><td>16.1</td><td>12.0</td><td>8.4</td></tr><tr><td>ROE (%)</td><td>10.9</td><td>13.2</td><td>16.4</td><td>20.5</td></tr></table>

52-WEEK PRICE (CNY)  
![](images/05b26b30d62b2de8cefd0976a4ee1732b963f7572cbd73df8a3e5ab2f987c99c.jpg)  
Source: LSEG IBES, HSBC Qianhai Securities estimates

Dun Wang\*, CFA, CPA (Reg. No. S1700519060002)
Analyst, A-share Industrials & Renewables Research
HSBC Qianhai Securities Limited
dun.wang@hsbcqh.com.cn
+86 21 5066 2027

Corey Chan\* (Reg. No. S1700518100001)
Head, A-share Industrials & Renewables Research
HSBC Qianhai Securities Limited
corey.chan@hsbcqh.com.cn
+86 21 5066 2001

\* Employed by a non-US affiliate of HSBC Securities (USA) Inc, and is not registered/ qualified pursuant to FINRA regulations

No country for bears

The $24^{\text{th}}$ edition of the EM Sentiment Survey Click to view

Issuer of report: HSBC Qianhai Securities Limited

View HSBC Qianhai Securities at: https://www.research.hsbc.com

## Financials & valuation: Hanbell Precise Machinery

Financial statements

<table><tr><td>Year to</td><td>12/2025a</td><td>12/2026e</td><td>12/2027e</td><td>12/2028e</td></tr><tr><td colspan="5">Profit &amp; loss summary (CNYm)</td></tr><tr><td>Revenue</td><td>2926.7</td><td>3428.9</td><td>4370.7</td><td>5586.8</td></tr><tr><td>EBITDA</td><td>670.5</td><td>770.6</td><td>1004.8</td><td>1379.4</td></tr><tr><td>Depreciation &amp; amortisation</td><td>-130.8</td><td>-100.3</td><td>-113.0</td><td>-124.6</td></tr><tr><td>Operating profit/EBIT</td><td>539.7</td><td>670.3</td><td>891.8</td><td>1254.8</td></tr><tr><td>Net interest</td><td>-19.9</td><td>-1.4</td><td>14.9</td><td>21.1</td></tr><tr><td>PBT</td><td>519.8</td><td>668.9</td><td>906.7</td><td>1275.9</td></tr><tr><td>HSBC Qianhai PBT</td><td>519.8</td><td>668.9</td><td>906.7</td><td>1275.9</td></tr><tr><td>Taxation</td><td>-50.0</td><td>-64.4</td><td>-87.2</td><td>-122.8</td></tr><tr><td>Net profit</td><td>468.7</td><td>603.2</td><td>817.6</td><td>1150.5</td></tr><tr><td>HSBC Qianhai net profit</td><td>468.7</td><td>603.2</td><td>817.6</td><td>1150.5</td></tr><tr><td colspan="5">Cash flow summary (CNYm)</td></tr><tr><td>Cash flow from operations</td><td>778.5</td><td>1390.4</td><td>915.3</td><td>1227.6</td></tr><tr><td>Capex</td><td>-416.8</td><td>-292.0</td><td>-292.0</td><td>-292.0</td></tr><tr><td>Cash flow from investment</td><td>-416.8</td><td>-292.0</td><td>-292.0</td><td>-292.0</td></tr><tr><td>Dividends</td><td>-240.6</td><td>-309.6</td><td>-419.7</td><td>-590.6</td></tr><tr><td>Change in net debt</td><td>-341.2</td><td>-810.2</td><td>-313.7</td><td>-516.0</td></tr><tr><td>FCF equity</td><td>361.7</td><td>1098.4</td><td>623.3</td><td>935.6</td></tr><tr><td colspan="5">Balance sheet summary (CNYm)</td></tr><tr><td>Intangible fixed assets</td><td>211.5</td><td>201.5</td><td>196.3</td><td>191.2</td></tr><tr><td>Tangible fixed assets</td><td>1100.9</td><td>1293.4</td><td>1477.5</td><td>1650.2</td></tr><tr><td>Current assets</td><td>4207.3</td><td>4492.5</td><td>5115.7</td><td>6018.8</td></tr><tr><td>Cash &amp; others</td><td>1823.5</td><td>2642.6</td><td>2956.3</td><td>3472.3</td></tr><tr><td>Total assets</td><td>6252.0</td><td>6719.7</td><td>7521.9</td><td>8592.5</td></tr><tr><td>Operating liabilities</td><td>1175.4</td><td>1270.0</td><td>1562.4</td><td>1899.5</td></tr><tr><td>Gross debt</td><td>678.4</td><td>687.3</td><td>687.3</td><td>687.3</td></tr><tr><td>Net debt</td><td>-1145.1</td><td>-1955.3</td><td>-2269.0</td><td>-2785.0</td></tr><tr><td>Shareholders&#x27; funds</td><td>4372.8</td><td>4735.4</td><td>5243.3</td><td>5974.1</td></tr><tr><td>Invested capital</td><td>2520.8</td><td>2074.9</td><td>2270.9</td><td>2488.4</td></tr></table>

Ratio, growth and per share analysis

Buy

Valuation data

<table><tr><td>Year to</td><td>12/2025a</td><td>12/2026e</td><td>12/2027e</td><td>12/2028e</td></tr><tr><td>EV/sales</td><td>4.5</td><td>3.6</td><td>2.8</td><td>2.1</td></tr><tr><td>EV/EBITDA</td><td>19.7</td><td>16.1</td><td>12.0</td><td>8.4</td></tr><tr><td>EV/IC</td><td>5.2</td><td>6.0</td><td>5.3</td><td>4.7</td></tr><tr><td>PE*</td><td>30.7</td><td>23.8</td><td>17.6</td><td>12.5</td></tr><tr><td>PB</td><td>3.3</td><td>3.0</td><td>2.7</td><td>2.4</td></tr><tr><td>FCF yield (%)</td><td>2.5</td><td>7.6</td><td>4.3</td><td>6.5</td></tr><tr><td>Dividend yield (%)</td><td>1.7</td><td>2.2</td><td>2.9</td><td>4.1</td></tr></table>

\* Based on HSBC Qianhai EPS (diluted)

ESG metrics

<table><tr><td>Environmental Indicators</td><td>12/2025a</td></tr><tr><td>GHG emission intensity*</td><td>n/a</td></tr><tr><td>Energy intensity*</td><td>n/a</td></tr><tr><td>CO2 reduction policy</td><td>Yes</td></tr><tr><td>Social Indicators</td><td>12/2025a</td></tr><tr><td>Employee costs as % of revenues</td><td>n/a</td></tr><tr><td>Employee turnover (%)</td><td>n/a</td></tr><tr><td>Diversity policy</td><td>Yes</td></tr></table>

Source: Company data, HSBC Qianhai Securities

<table><tr><td>Governance Indicators</td><td>12/2025a</td></tr><tr><td>No. of board members</td><td>9</td></tr><tr><td>Average board tenure (years)</td><td>3.2</td></tr><tr><td>Female board members (%)</td><td>11.1</td></tr><tr><td>Board members independence (%)</td><td>33.3</td></tr></table>

\* GHG intensity and energy intensity are measured in kg and kWh respectively against revenue in USD '000s

Issuer information

<table><tr><td>Share price (CNY)</td><td>26.87</td><td>Free float</td><td>39%</td></tr><tr><td>Target price (CNY)</td><td>38.80</td><td>Sector</td><td>Machinery</td></tr><tr><td>RIC (Equity)</td><td>002158.SZ</td><td>Country/Region</td><td>China</td></tr><tr><td>Bloomberg (Equity)</td><td>002158 CH</td><td>Analyst</td><td>Dun Wang, CFA, CPA</td></tr><tr><td>Market cap (USDm)</td><td>2120.2</td><td>Contact</td><td>+86 21 5066 2027</td></tr></table>

<table><tr><td>Year to</td><td>12/2025a</td><td>12/2026e</td><td>12/2027e</td><td>12/2028e</td></tr><tr><td colspan="5">Y-o-y % change</td></tr><tr><td>Revenue</td><td>-20.3</td><td>17.2</td><td>27.5</td><td>27.8</td></tr><tr><td>EBITDA</td><td>-38.6</td><td>14.9</td><td>30.4</td><td>37.3</td></tr><tr><td>Operating profit</td><td>-43.6</td><td>24.2</td><td>33.0</td><td>40.7</td></tr><tr><td>PBT</td><td>-48.6</td><td>28.7</td><td>35.5</td><td>40.7</td></tr><tr><td>HSBC Qianhai EPS</td><td>-45.7</td><td>28.7</td><td>35.5</td><td>40.7</td></tr><tr><td colspan="5">Ratios (%)</td></tr><tr><td>Revenue/IC (x)</td><td>1.2</td><td>1.5</td><td>2.0</td><td>2.3</td></tr><tr><td>ROIC</td><td>20.6</td><td>26.6</td><td>37.3</td><td>47.9</td></tr><tr><td>ROE</td><td>10.9</td><td>13.2</td><td>16.4</td><td>20.5</td></tr><tr><td>ROA</td><td>7.6</td><td>9.3</td><td>11.5</td><td>14.3</td></tr><tr><td>EBITDA margin</td><td>22.9</td><td>22.5</td><td>23.0</td><td>24.7</td></tr><tr><td>Operating profit margin</td><td>18.4</td><td>19.5</td><td>20.4</td><td>22.5</td></tr><tr><td>EBITDA/net interest (x)</td><td>33.7</td><td>552.7</td><td></td><td></td></tr><tr><td>Net debt/equity</td><td>-26.0</td><td>-41.1</td><td>-43.0</td><td>-46.4</td></tr><tr><td>Net debt/EBITDA (x)</td><td>-1.7</td><td>-2.5</td><td>-2.3</td><td>-2.0</td></tr><tr><td colspan="5">CF from operations/net debt</td></tr><tr><td colspan="5">Per share data (CNY)</td></tr><tr><td>EPS Rep (diluted)</td><td>0.88</td><td>1.13</td><td>1.53</td><td>2.15</td></tr><tr><td>HSBC Qianhai EPS (diluted)</td><td>0.88</td><td>1.13</td><td>1.53</td><td>2.15</td></tr><tr><td>DPS</td><td>0.45</td><td>0.58</td><td>0.78</td><td>1.10</td></tr><tr><td>Book value</td><td>8.18</td><td>8.86</td><td>9.81</td><td>11.17</td></tr></table>

Price relative  
![](images/a0aaa603c5d0898d2bec54dcc3fb0af1f079bb38575bdf32d4817778a31a3363.jpg)  
Source: HSBC Qianhai Securities  
Note: Priced at close of 17 Jul 2026

## A more detailed look at AIDC exposure

## The best is yet to come

In 2026, many global leading HAVAC players (see Exhibit 1) stated that data centre cooling has become one of the key drivers of their growth. Some of these HAVAC players, such as Trane or Carrier, have in-house compressor manufacturing capacity but also purchase externally some types of refrigerant compressors. For example, Danfosss has been a popular choice for maglev compressors for a few of these companies (source: Danfoss official website). We think this represents opportunities for specialized compressor makers like Hanbell, especially as next-generation AIDC need high-performance compressors such as maglev compressors or gas-bearing refrigeration compressors.

As most of Hanbell's new products (large capacity maglev compressors, for example) are going through certification and testing process for downstream clients, we believe Hanbell's refrigerant segment can register fast growth in 2027. While we expect Hanbell's centrifugal compressor sales (including maglev compressors) to expand significantly y-o-y in 6M26 (partly driven by data centres and partly by refrigeration or heat pump demand), we note the base is still low and therefore 2026e growth in absolute value will be limited to some extent. We estimate that centrifugal compressors accounted for c10% of its total refrigerant segment revenue in 2025, while the rest were mostly screw compressors.

Exhibit 1. Global leading AIDC HAVAC players and their relationships with Hanbell

<table><tr><td></td><td>Recent data centre related orders</td><td>Relationship with Hanbell</td></tr><tr><td>Trane</td><td>1Q26 Exceptional CHVAC bookings / revenues, up ~40% / up HSD, respectively. Strong services growth with revs up double digits. 3yr stack revs up ~50% (applied up &gt;80%)</td><td>In contact to see if Hanbell can supply maglev compressors for AIDC</td></tr><tr><td>Carrier</td><td>1Q26 Global CHVAC3 orders up 35%, with data center orders up &gt;500%</td><td>Hanbell has been supplying compressors for air conditioning; in contact to see if they can supply maglev compressors for AIDC</td></tr><tr><td>York (under Johnson Controls)</td><td>Total new orders (inc HAVAC) increased 39% y-o-y in 1QFY26 and 30% y-o-y in 2QFY26. In FY2Q26 in the Americas, organic revenue increased 7%, led by continued strength in Applied HVAC and solid double-digit growth in service</td><td>Hanbell has been supplying screw engines for air conditioning; in contact to see if can supply maglev compressors for AIDC;</td></tr><tr><td>Vertiv</td><td>Global leading liquid cooling solution provider also has subsidiaries that make chillers</td><td>Testing and certifying Hanbell&#x27;s compressors</td></tr><tr><td>Teco</td><td>Production capacity for its chillers has been upgraded to the thousand-ton class, successfully penetrating the North American market; following a strategic alliance involving a share swap with Hon Hai, the company has engaged in deep collaboration on US AIDC infrastructure</td><td>Hanbell will be the major compressor supplier once Teco secures HVAC contracts for US AIDC</td></tr><tr><td>Dunham-Bush (under Moon Environment Tech)</td><td>US AIDC chiller demand going up and the company is expanding capacity</td><td>Hanbell is supplying screw engines for compressor units of US AIDC</td></tr></table>

Source: Company data, HSBC Qianhai Securities

## Size of the compressor market for AIDC

As we stated in our report Hanbell Precise Machinery (002158 CH): Buy: Investor feedback (26 Nov 2025), for refrigerant compressors used in data centres, we estimate screw compressors cost cRMB600m per GW and magnetic levitation compressors cost cRMB1-1.5bn per GW (source: 2025 China Compressor Industry Development Yearbook). This estimate was based on our estimated total market size divided by the amount of data centres bu

[中间内容因长度限制已省略]

ssion and the Financial Supervisory Service of Korea. In Singapore, this publication is distributed by The Hongkong and Shanghai Banking Corporation Limited, Singapore Branch for the general information of institutional investors or other persons specified in Sections 274 and 304 of the Securities and Futures Act 2001 of Singapore ("SFA") and accredited investors and other persons in accordance with the conditions specified in Sections 275 and 305 of the SFA. Only Economics or Currencies reports are intended for distribution to a person who is not an Accredited Investor, Expert Investor or Institutional Investor as defined in SFA. The Hongkong and Shanghai Banking Corporation Limited, Singapore Branch accepts legal responsibility for the contents of reports. This publication is not a prospectus as defined in the SFA. It may not be further distributed in whole or in part for any purpose. The Hongkong and Shanghai Banking Corporation Limited Singapore Branch is regulated by the Monetary Authority of Singapore. Recipients in Singapore should contact a "Hongkong and Shanghai Banking Corporation Limited, Singapore Branch" representative in respect of any matters arising from, or in connection with this report. Please refer to The Hongkong and Shanghai Banking Corporation Limited Singapore Branch's website at www.business.hsbc.com.sg for contact details. In Australia, this publication has been distributed by The Hongkong and Shanghai Banking Corporation Limited (ABN 65 117 925 970, AFSL 301737) for the general information of its "wholesale" customers (as defined in the Corporations Act 2001). Where distributed to retail customers, this research is distributed by HSBC Bank Australia Limited (ABN 48 006 434 162, AFSL No. 232595). These respective entities make no representations that the products or services mentioned in this document are available to persons in Australia or are necessarily suitable for any particular person or appropriate in accordance with local law. No consideration has been given to the particular investment objectives, financial situation or particular needs of any recipient.

HSBC Securities (USA) Inc., a US-registered broker-dealer and member of FINRA, accepts responsibility for the content of this research report prepared by its non-US foreign affiliate. The information contained herein is under no circumstances to be construed as investment advice and is not tailored to the needs of the recipient. All US persons receiving and/or accessing this report and wishing to effect transactions in any security discussed herein should do so with HSBC Securities (USA) Inc. in the United States and not with its non-US foreign affiliate, the issuer of this report. HSBC México, S.A., Institución de Banca Múltiple, Grupo Financiero HSBC is authorized and regulated by Secretaría de Hacienda y Crédito Público and Comisión Nacional Bancaria y de Valores (CNBV). In Brazil, this document has been distributed by Banco HSBC SA ("HSBC Brazil"), and/or its affiliates. As required by Resolution No. 20/2021 of the Securities and Exchange Commission of Brazil (Comissão de Valores Mobiliários), potential conflicts of interest concerning (i) HSBC Brazil and/or its affiliates; and (ii) the analyst(s) responsible for authoring this report are stated on the chart above labelled "HSBC & Analyst Disclosures".

If you are a customer of HSBC International Wealth & Premier Banking ("IWPB"), including HSBC Private Bank, you are eligible to receive this publication only if: (i) you have been approved to receive relevant research publications by an applicable HSBC legal entity; (ii) you have agreed to the applicable HSBC entity's terms and conditions and/or customer declaration for accessing research; and (iii) you have agreed to the terms and conditions of any other internet banking, online banking, mobile banking and/or investment services offered by that HSBC entity, through which you will access research publications (collectively with (ii), the "Terms"). If you do not meet the above eligibility requirements, please disregard this publication and, if you are a IWPB customer, please notify your Relationship Manager or call the relevant customer hotline. Distribution of this publication is the sole responsibility of the HSBC entity with whom you have agreed the Terms. Receipt of research publications is strictly subject to the Terms and any other conditions or disclaimers applicable to the provision of the publications that may be advised by IWPB. © Copyright 2026, HSBC Qianhai Securities Limited, ALL RIGHTS RESERVED. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, in any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of HSBC Qianhai Securities Limited.
"""
