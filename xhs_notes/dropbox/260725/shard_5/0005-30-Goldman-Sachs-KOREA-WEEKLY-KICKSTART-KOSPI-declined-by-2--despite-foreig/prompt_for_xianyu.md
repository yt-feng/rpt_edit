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
KOREA WEEKLY KICKSTART

# KOSPI declined by $2\%$ despite foreign inflows and Alphabet's AI capex boost

KOSPI declined by $2\%$ despite foreign inflows and Alphabet's AI capex boost. The Construction, Software and Telecom sectors outperformed this week, while Securities, Auto and Insurance sectors underperformed the most (Exhibit 9).

■ Foreign investors continued to buy the KOSPI market, driven by inflows for KOSPI Tech (Exhibit 36).

KOSPI 12m-forward EPS was revised down by -0.4%. The Chemicals sector saw the strongest upward earnings revisions, while the Auto sector was revised down the most this week (Exhibit 23).

The KRW strengthened 1.6% vs. USD this week. It also strengthened by 2.5% vs. JPY and 2.1% vs. EUR.

The latest Korea Equity Risk Barometer (GSSRKERB Index) is at -1.1, staying in a risk-averse territory.

Charts of the Week: Korea: Retail Margin Loans and Leveraged ETFs; Foreign Flows, Positioning and Short-Selling Activities

■ Retail Margin Loans and Leveraged ETFs: As recent market volatility has driven deleveraging among retail investors, retail margin loan balances have declined from a peak of US\$25bn to US\$22bn, while remaining at 0.5% on a market-cap-adjusted basis. Despite heightened volatility, retail margin calls as a percentage of receivables fell to 0.7% as of July 23. In addition, brokerage receivables have recently declined to KRW 0.9trn. Amid recent market weakness, Korea leveraged ETF AUM has fallen from a peak of US\$53bn to US\$26bn, with leveraged exposure now equivalent to 2.1% of market free float.

■ Foreign Flows, Positioning and Short-Selling Activities: As investors seek opportunities amid recent market weakness, the KOSPI has recorded foreign inflows for two consecutive weeks. However, despite this recent improvement, the market continues to face significant foreign outflows. As a result, foreign ownership in the KOSPI semiconductor sector remains light, at nearly -2 standard deviations versus historical levels. Over the past month, hedge funds have been taking profits in Japan, Taiwan, and Korea, while China has benefited from some rotation buying. Korea has also begun to see a rebound in interest over the past one to two weeks. Amid the recent market weakness, short-selling balances and trading activity have also declined meaningfully.

Timothy Moe, CFA
+65-6889-1199 | timothy.moe@gs.com
GS (Singapore) Pte

John Kwon  
+65-6654-6337 |  
jongmin.kwon@gs.com  
GS (Singapore) Pte

## Table of Contents

Charts of the week: Retail Margin Loans and Leveraged ETFs 3
Charts of the week: Foreign Flows, Positioning and Short-Selling Activities 4
Summary 6
Investment flows 7
Macro Indicators 8
Performance 9
Valuations 11
Valuation discount relative to Global and Asia regional peers 13
Flows 14
Currency, rates and commodities 16
Korea ERB, Credit and Market Technicals 17
Disclosure Appendix 18

## Charts of the week: Retail Margin Loans and Leveraged ETFs

Exhibit 1: Margin loan balance declined to 22bn USD from 25bn USD at the peak while sustaining its market cap adjusted level to 0.5%

![](images/f6560d9ed6e28f71b2147bbebac67303ed2b2fb1b0733dbc12e982ff452199e9.jpg)  
Source: Quantiwise, GS Global Investment Research

Exhibit 2: Despite the market volatility, margin call to receivable fell to $0.7\%$ as of 23th of July

![](images/63e529c072ecfc47b94eb0d93250299a6c4a68fba61e80180586990949372ab5.jpg)  
Source: Quantiwise, Korea Financial Investment Association

## Exhibit 3: Brokerages receivables have declined to 0.9trn KRW recently

![](images/d992b209f650554b1f08c32a1b9c019d8d7c9c33ea090c6435427d144075ab07.jpg)  
Source: Korea Financial Investment Association

Exhibit 4: Korea leveraged ETF AUM has declined from a peak of US\$53bn to US\$26bn, with leveraged exposure now equivalent to 2.1% of market free float

![](images/ae54686c164748839097ebe83770eb57b45f8e8b7eb2fbc58a2a766ed0b017b4.jpg)  
Source: Bloomberg, GS Global Investment Research

## Charts of the week: Foreign Flows, Positioning and Short-Selling Activities

Exhibit 5: Despite the recent foreign inflows, KOSPI has seen strong foreign outflows

![](images/ebc65b17fb533d9741baa833e09cd75daa321820b3610f874f673c3f9464244b.jpg)  
Source: Quantiwise, GS Global Investment Research  
Exhibit 6: Foreign ownership in KOSPI semiconductor sector remained light given strong foreign outflows

![](images/43b9ad9b26933af073f42139dc027814907bbaa24fb6c13c0e6432b6d4dfc4ec.jpg)  
Source: Quantiwise, GS Global Investment Research

Exhibit 7: Hedge funds have been taking profits in Japan, Taiwan, and Korea over the past month, while China has seen some rotation buying; Korea has also started to see a rebound in interest over the past one to two weeks

![](images/76614786eaf4ab68255c97d36f397648d4b241c7e076f973ba9bb96f78bfd1a5.jpg)  
Source: GS FICC and Equities and Prime Services

Exhibit 8: Amid the recent market weakness, short selling balance and trading activities have declined meaningfully

![](images/92a923b656358d246548e3840b88d7f8191d3cabbf5619a77180212fe51c9938.jpg)  
Source: Quantiwise, GS Global Investment Research

<table><tr><td colspan="5">Equity Market Performance</td></tr><tr><td></td><td>P/E 2026E</td><td></td><td></td><td>1-wk chg</td></tr><tr><td>KOSPI</td><td>5.7</td><td>6,690.62</td><td>↓</td><td>(1.9)</td></tr><tr><td>KOSDAQ</td><td>22.7</td><td>748.22</td><td>↓</td><td>(5.5)</td></tr><tr><td>MSCI Korea</td><td>5.0</td><td>2,463.08</td><td>↓</td><td>(2.3)</td></tr><tr><td colspan="5">KOSPI Performance by sector</td></tr><tr><td>Top 3</td><td>wk chg (%)</td><td>Bottom 3</td><td></td><td>1wk chg (%)</td></tr><tr><td>Construction</td><td>8.4</td><td>Securities</td><td></td><td>(6.5)</td></tr><tr><td>Software</td><td>7.1</td><td>Auto</td><td></td><td>(4.4)</td></tr><tr><td>Telecom</td><td>6.9</td><td>Insurance</td><td></td><td>(3.8)</td></tr><tr><td colspan="5">Market Flows</td></tr><tr><td colspan="2">Equities (KRW bn)</td><td>1-wk flow</td><td></td><td>in std dev*</td></tr><tr><td colspan="2">KOSPI Flows: Foreigners</td><td>2,329</td><td>↑</td><td>0.4</td></tr><tr><td></td><td>Institutions</td><td>(2,798)</td><td>↓</td><td>-1.2</td></tr><tr><td></td><td>Individuals</td><td>461</td><td>↑</td><td>0.1</td></tr><tr><td></td><td>Pensions</td><td>170</td><td>↑</td><td>0.6</td></tr><tr><td colspan="2">KOSDAQ Flows: Foreigners</td><td>(222)</td><td>↓</td><td>-0.4</td></tr><tr><td></td><td>Institutions</td><td>(631)</td><td>↓</td><td>-0.4</td></tr><tr><td></td><td>Individuals</td><td>831</td><td>↑</td><td>0.5</td></tr><tr><td></td><td>Pensions</td><td>(102)</td><td>↓</td><td>-1.0</td></tr><tr><td colspan="5">FX/Interest Rate</td></tr><tr><td></td><td></td><td>Current</td><td></td><td>1-wk chg</td></tr><tr><td colspan="2">USDKRW</td><td>1,463</td><td>↓</td><td>(1.6)</td></tr><tr><td colspan="2">JPYKRW</td><td>8.93</td><td>↓</td><td>(2.5)</td></tr><tr><td colspan="2">USDKRW 1M Risk Reversal/ATM vc</td><td>0.04</td><td>↑</td><td>1bp</td></tr><tr><td colspan="2">USDKRW 1yr swap basis</td><td>(85)</td><td>↑</td><td>4bp</td></tr><tr><td colspan="2">3-year KTB</td><td>3.96</td><td>↑</td><td>11bp</td></tr><tr><td colspan="2">10-year KTB</td><td>4.45</td><td>↑</td><td>15bp</td></tr></table>

Up (↑) = Up wow vs. the previous week  
Asterisk (\*) = Expressed in standard deviation of 1-wk change in 1-year

## Summary

## Exhibit 9: Summary of the past week's performance

## Exhibit 10: Summary of year-to-date flows

Year-to-date Foreign Inflows to Korea  
![](images/b8254011a52839dfca7edf6c5564737bdc7613e15f53e49a4b1d768565f9f9c1.jpg)

![](images/01bd2657bfde939a5f9de72fa3ffc8fa0d05f6109ebaf22a15b8bddd9f001490.jpg)

## Investment flows

Exhibit 11: Equity inflows to 5 AEJ markets 4-week rolling sum  
![](images/e158e107825c5bf2883940555b9e525f09a8ab717a9e123387993da204645ab1.jpg)  
Source: Bloomberg, GS Global Investment Research

Exhibit 12: Equity inflows to 5 AEJ markets  
![](images/49818beef9884d592c4fe3130b2c42641513b6eb94b7cee2aeeea48a397d0186.jpg)  
Source: Bloomberg

Exhibit 13: Bond inflows to 4 AEJ markets 4-week rolling sum  
![](images/9dd30a30809988f6722b7bad2292fc0106be49289df24e8f699cd7e73f8a454b.jpg)  
Source: Bloomberg, Haver Analytics, GS Global Investment Research

Exhibit 14: Bond inflows to 4 AEJ markets  
![](images/c5d115b43cef8af4764d8dac663dae03c1727a6e943c5b413d336bf7e8834bef.jpg)  
Source: Bloomberg, Haver Analytics, GS Global Investment Research

## Macro Indicators

Exhibit 15: Housing prices and rental prices National, monthly and weekly price changes  
![](images/65e489489c8534b4ccd23cf121810cfa9394698642e5bcafd166efbaffd1f3f9.jpg)  
Source: KAB  
Exhibit 16: Living expense price changes Monthly and weekly changes vs. CPI

![](images/be5d6e9c6ff09ea6077df0e50361d62b3cc52aa6906b8dfb386f0342093170cd.jpg)  
Source: Bloomberg, Korea Price Research Center, GS Global Investment Research

Exhibit 17: Daily Financial Condition Index Jan 1, 2013=100  
![](images/8f6187a8f9dab695addd98a9fea67b85467c2a928c6e98b3103fa3300c513155.jpg)  
Source: Bloomberg, CEIC, GS Global Investment Research

## Exhibit 18: Korea Economic Forecasts

Monthly indicators

<table><tr><td>Monthly (% yoy)</td><td>Nov</td><td>Dec</td><td>Jan</td><td>Feb</td><td>Mar</td><td>Apr</td><td>May</td><td>Jun</td></tr><tr><td>Exports ex ships</td><td>9.5</td><td>14.1</td><td>35.7</td><td>29.0</td><td>52.7</td><td>47.9</td><td>54.5</td><td>73.3</td></tr><tr><td>Industrial production</td><td>0.0</td><td>1.6</td><td>6.8</td><td>-2.3</td><td>3.8</td><td>1.5</td><td>-0.9</td><td></td></tr><tr><td>Employment</td><td>0.8</td><td>0.6</td><td>0.4</td><td>0.8</td><td>0.7</td><td>0.3</td><td>-0.1</td><td>0.2</td></tr><tr><td>CPI</td><td>2.4</td><td>2.3</td><td>2.0</td><td>2.0</td><td>2.2</td><td>2.6</td><td>3.1</td><td>3.2</td></tr><tr><td>BOK Policy Rate</td><td>2.50</td><td>2.50</td><td>2.50</td><td>2.50</td><td>2.50</td><td>2.50</td><td>2.50</td><td>2.50</td></tr><tr><td colspan="9">Note: Blue-shaded cells denote positive weekly changes and acceleration in monthly changes</td></tr></table>

Macro and market outlook

<table><tr><td>Forecasts</td><td>2025</td><td>2026</td><td>2027</td><td>1Q26</td><td>2Q26</td><td>3Q26</td><td>4Q26</td><td>1Q27</td></tr><tr><td>Real GDP</td><td>1.1</td><td>2.7</td><td>2.3</td><td>3.8</td><td>3.1</td><td>1.9</td><td>2.2</td><td>1.2</td></tr><tr><td>Domestic Demand</td><td>0.6</td><td>2.4</td><td>3.0</td><td>2.2</td><td>2.5</td><td>2.0</td><td>2.8</td><td>2.1</td></tr><tr><td>Exports</td><td>4.3</td><td>8.3</td><td>2.7</td><td>11.8</td><td>8.0</td><td>6.3</td><td>7.5</td><td>2.0</td></tr><tr><td>Imports</td><td>3.3</td><td>8.0</td><td>5.0</td><td>8.5</td><td>7.6</td><td>6.5</td><td>9.3</td><td>6.4</td></tr><tr><td>Consumer Prices</td><td>2.1</td><td>2.6</td><td>2.2</td><td>2.1</td><td>2.9</td><td>3.0</td><td>2.6</td><td>2.5</td></tr><tr><td>Current Account - % GDP</td><td>6.5</td><td>13.4</td><td>15.8</td><td>14.7</td><td>13.6</td><td>13.6</td><td>11.9</td><td>9.8</td></tr><tr><td>KOSPI (end / 12mf)</td><td>4214</td><td>12000*</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Policy rate (end)</td><td>2.50</td><td>3.00</td><td>3.25</td><td>2.50</td><td>2.50</td><td>2.75</td><td>3.00</td><td>3.25</td></tr><tr><td>USDKRW (end)</td><td>1,444</td><td>1,476</td><td>1,413</td><td>1,346</td><td>1,501</td><td>1,485</td><td>1,451</td><td>1,436</td></tr></table>

\* KOSPI for 2025 is the year-end level and KOSPI for 2026 is 12-month target

## Performance

Exhibit 19: Performance of Korean and regional equity markets

<table><tr><td rowspan="2"></td><td rowspan="2" colspan="2">Index</td><td colspan="4">Price return (%)</td><td rowspan="2" colspan="3">% vs average</td></tr><tr><td colspan="2">Local Crncy</td><td colspan="2">USD</td></tr><tr><td>Korea</td><td>Crn</td><td>24-Jul</td><td>1-wk</td><td>YTD</td><td>1-wk</td><td>YTD</td><td>RSI</td><td>30D</td><td>60D</td></tr><tr><td>Kospi</td><td>KRW</td><td>6,691</td><td>(1.9)</td><td>58.8</td><td>(0.3)</td><td>56.2</td><td>45</td><td>(15)</td><td>(14)</td></tr><tr><td>Kospi 200</td><td>KRW</td><td>1,056</td><td>(2.3)</td><td>74.2</td><td>(0.7)</td><td>71.3</td><td>45</td><td>(16)</td><td>(14)</td></tr><tr><td>Kosdaq</td><td>KRW</td><td>748</td><td>(5.5)</td><td>(19.2)</td><td>(4.0)</td><td>(20.5)</td><td>41</td><td>(14)</td><td>(25)</td></tr><tr><td>MSCI Korea</td><td>KRW</td><td>2,463</td><td>(2.3)</td><td>78.5</td><td>(0.7)</td><td>75.6</td><td>45</td><td>(8)</td><td>7</td></tr><tr><td colspan="10">Selected sector indexes</td></tr><tr><td>Auto</td><td>KRW</td><td>2,897</td><td>(4.4)</td><td>14.5</td><td>(2.9)</td><td>12.7</td><td>48</td><td>(10)</td><td>(17)</td></tr><tr><td>Tech</td><td>KRW</td><td>106,870</td><td>(2.9)</td><td>114.7</td><td>(1.4)</td><td>111.2</td><td>45</td><td>46</td><td>2</td></tr><tr><td>Retail</td><td>KRW</td><td>616</td><td>(1.1)</td><td>28.6</td><td>0.4</td><td>26.5</td><td>43</td><td>(13)</td><td>(13)</td></tr><tr><td>Pharmaceutical</td><td>KRW</td><td>15,536</td><td>4.4</td><td>(10.1)</td><td>6.1</td><td>(11.6)</td><td>48</td><td>5</td><td>2</td></tr><tr><td>Steel</td><td>KRW</td><td>6,515</td><td>2.8</td><td>(0.4)</td><td>4.4</td><td>(2.0)</td><td>47</td><td>(3)</td><td>(15)</td></tr><tr><td>Chemicals</td><td>KRW</td><td>4,509</td><td>0.3</td><td>10.4</td><td>1.9</td><td>8.5</td><td>54</td><td>1</td><td>(6)</td></tr><tr><td>F&amp;B</td><td>KRW</td><td>4,750</td><td>2.7</td><td>5.1</td><td>4.4</td><td>3.3</td><td>51</td><td>2</td><td>(1)</td></tr><tr><td>Machinery</td><td>KRW</td><td>2,828</td><td>(2.1)</td><td>4.0</td><td>(0.6)</td><td>2.3</td><td>43</td><td>(13)</td><td>(25)</td></tr><tr><td>Construction</td><td>KRW</td><td>152</td><td>8.4</td><td>54.6</td><td>10.1</td><td>52.1</td><td>51</td><td>(4)</td><td>(15)</td></tr><tr><td>Shipbuilding</td><td>KRW</td><td>1,441</td><td>1.4</td><td>(0.5)</td><td>3.0</td><td>(2.2)</td><td>46</td><td>(11)</td><td>(22)</td></tr><tr><td>Utilities</td><td>KRW</td><td>1,091</td><td>4.8</td><td>(21.8)</td><td>6.4</td><td>(23.1)</td><td>49</td><td>(2)</td><td>(7)</td></tr><tr><td>Banking</td><td>KRW</td><td>1,644</td><td>(3.3)</td><td>26.1</td><td>(1.8)</td><td>24.1</td><td>54</td><td>3</td><td>4</td></tr><tr><td>Securities</td><td>KRW</td><td>5,465</td><td>(6.5)</td><td>30.4</td><td>(5.0)</td><td>28.3</td><td>43</td><td>(10)</td><td>(22)</td></tr><tr><td>Insurance</td><td>KRW</td><td>47,951</td><td>(3.8)</td><td>57.2</td><td>(2.3)</td><td>54.7</td><td>46</td><td>(9)</td><td>(4)</td></tr><tr><td>Telecom</td><td>KRW</td><td>648</td><td>6.9</td><td>32.7</td><td>8.6</td><td>30.6</td><td>58</td><td>5</td><td>1</td></tr><tr><td>Software</td><td>KRW</td><td>199</td><td>7.1</td><td>(4.9)</td><td>8.8</td><td>(6.4)</td><td>49</td><td>(36)</td><td>(37)</td></tr><tr><td>Leisure</td><td>KRW</td><td>281</td><td>(0.2)</td><td>(44.3)</td><td>1.4</td><td>(45.2)</td><td>42</td><td>(55)</td><td>(59)</td></tr><tr><td colspan="10">MSCI standard market and regional indexes</td></tr><tr><td>AC Asia Pacific ex Japan</td><td>USD</td><td>844</td><td>0.5</td><td>16.9</td><td>0.5</td><td>16.9</td><td>49</td><td>(4)</td><td>(4)</td></tr><tr><td>USA</td><td>USD</td><td>7,063</td><td>(0.7)</td><td>8.1</td><td>(0.7)</td><td>8.1</td><td>44</td><td>(1)</td><td>(1)</td></tr><tr><td>EU</td><td>EUR</td><td>214</td><td>-</td><td>8.5</td><td>(0.5)</td><td>5.2</td><td>50</td><td>0</td><td>2</td></tr><tr><td>China</td><td>HKD</td><td>74</td><td>0.9</td><td>(11.5)</td><td>1</td><td>(12.1)</td><td>54</td><td>1</td><td>(3)</td></tr><tr><td>Japan</td><td>JPY</td><td>2,468</td><td>2.5</td><td>18.1</td><td>1.7</td><td>13.0</td><td>54</td><td>(1)</td><td>1</td></tr><tr><td colspan="10">Regional indexes</td></tr><tr><td colspan="10">America</td></tr><tr><td>S&amp;P 500 (US)</td><td>USD</td><td>7,408</td><td>(0.7)</td><td>8.2</td><td>(0.7)</td><td>8.2</td><td>45</td><td>(1)</td>

[中间内容因长度限制已省略]

ttempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and

https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
