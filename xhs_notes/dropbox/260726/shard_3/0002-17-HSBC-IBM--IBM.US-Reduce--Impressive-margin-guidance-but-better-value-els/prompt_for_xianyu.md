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
# Reduce: Impressive margin guidance but better value elsewhere

IBM cut its 2026 constant currency revenue guidance but still guided to non-GAAP PBT margin improving 100bp y-o-y

\- Increasing our 2026-30e non-GAAP EPS estimates by 1-2% to reflect higher-than-expected margin guidance

\- TP cut to USD174 (from USD175) despite 1-2% higher EPS estimates due to lower multiples. Maintain Reduce

Impressive margin guidance: As pre-announced on 14 July 2026, 2Q26 revenue rose $1\%$ y-o-y cc to USD17,161m (1Q26: $6\%$ ). The company cut its 2026 cc revenue growth guidance to $4\%-5\%$ from more than $5\%$ previously. Despite the cut to revenue guidance, the management maintained it expects 2026 non-GAAP profit before tax margin to rise by 100bp y-o-y. 2Q26 non-GAAP profit before tax margin rose 30bp y-o-y but it was largely a result of a favourable USD280m non-GAAP other income in 2Q26 (2Q25: USD65m). The extent to which the expected margin improvement comes from one-off items such as other income is a key monitorable.

Software segment disappoints: Software segment cc growth slowed to 4.6% from 8% in 1Q26. Organic growth slipped to 0% y-o-y in 2Q26 (1Q26: we estimate 7%). Management cut 2026 cc revenue growth guidance to 6-8% from more than 10% previously. Transaction processing subsegment dipped 9% y-o-y (cc) (1Q26: +2%). The management expects low- to mid-single-digit % decline in 2H26 but suggested most of the missing revenue is likely delayed and not lost. Hybrid cloud subsegment cc growth accelerated to 11% y-o-y in 2Q26 (1Q26: 10%). Automation segment cc growth slipped to 3% in 2Q26 (1Q26: 7%). Reported growth for the data subsegment accelerated to 19% in 2Q26 (1Q26: 16%), but, net of c18-19pp inorganic contribution from the Confluent acquisition in 2Q26, organic growth slowed considerably.

Infrastructure segment inflecting: Infrastructure cc revenue dipped 7% y-o-y in 2Q26 (1Q26: +12%) as the new z17 series entered its fifth quarter since launch. The weakness in the mainframes subsegment was partially offset by a strong distributed infrastructure subsegment where revenue rose 37% y-o-y (1Q26: 13%), on a low base. The management now expects infrastructure segment cc revenue to rise by low-single-digit % in 2026 (previously low-single-digit decline) largely due to stronger distributed infra subsegment.

Expensive valuation: IBM shares are trading at 14.2x CY27e non-GAAP EV/EBIT (sector median: 13.9x). We expect IBM's non-GAAP EPS to rise at a CAGR of $6.7\%$ over CY26-28e (sector median $19.2\%$ ). Our TP of USD174 (was USD175) is based on our SOTP valuation. Our TP implies $15.4\%$ downside, and we maintain a Reduce rating as we see better value elsewhere.

## Disclosures & Disclaimer

This report must be read with the disclosures and the analyst certifications in the Disclosure appendix, and with the Disclaimer, which forms part of it.

United States

![](images/f77b3985b5c63b5be575c12d86709b8eacf0ce12412674753655a2516d156e7d.jpg)

## MAINTAIN REDUCE

TARGET PRICE (USD) PREVIOUS TARGET (USD)

174.00 175.00

SHARE PRICE (USD) UPSIDE/DOWNSIDE

205.77 -15.4%

(as of 22 Jul 2026)

## MARKET DATA

<table><tr><td>Market cap (USDm)</td><td>193,400</td></tr><tr><td>Market cap (USDm)</td><td>193,400</td></tr><tr><td>3m ADTV (USDm)</td><td>2,815</td></tr></table>

<table><tr><td>Free float</td><td>100%</td></tr><tr><td>BBG</td><td>IBM US</td></tr><tr><td>RIC</td><td>IBM.N</td></tr></table>

FINANCIALS AND RATIOS (USD)

<table><tr><td>Year to</td><td>12/2025a</td><td>12/2026e</td><td>12/2027e</td><td>12/2028e</td></tr><tr><td>HSBC EPS</td><td>11.59</td><td>12.16</td><td>12.30</td><td>13.86</td></tr><tr><td>HSBC EPS (prev)</td><td>11.59</td><td>11.56</td><td>12.10</td><td>13.60</td></tr><tr><td>Change (%)</td><td>0.0</td><td>5.2</td><td>1.7</td><td>1.9</td></tr><tr><td>Consensus EPS</td><td>11.35</td><td>12.30</td><td>13.11</td><td>14.29</td></tr><tr><td>PE (x)</td><td>17.8</td><td>16.9</td><td>16.7</td><td>14.8</td></tr><tr><td>Dividend yield (%)</td><td>3.3</td><td>3.3</td><td>3.3</td><td>3.3</td></tr><tr><td>EV/EBITDA (x)</td><td>13.2</td><td>14.4</td><td>12.6</td><td>11.3</td></tr><tr><td>ROE (%)</td><td>36.6</td><td>32.8</td><td>29.3</td><td>29.2</td></tr></table>

52-WEEK PRICE (USD)  
![](images/2f9b5671224d6e88c825ea5388cb2b7301db89d72d793fe3aa556657be1a84ba.jpg)  
Source: LSEG IBES, HSBC estimates

## Abhishek Shukla\*, CFA

Senior Analyst, Technology
HSBC Bank Middle East Limited, DIFC
abhishek2.shukla@hsbc.com
+971 4 5093343

## Stephen Bersey

Head of US Technology Research
HSBC Securities (USA) Inc.
stephen.bersey@us.hsbc.com
+1 212 525 4153

## Sameer Lam\*

Global Software Analyst

HSBC Bank plc

sameer.lam@hsbc.com

+44 20 7992 3780

\* Employed by a non-US affiliate of HSBC Securities (USA) Inc, and is not registered/ qualified pursuant to FINRA regulations

Issuer of report: HSBC Bank Middle East Limited, DIFC

View HSBC Global Investment Research at: https://www.research.hsbc.com

## Financials & valuation: IBM

Financial statements

<table><tr><td>Year to</td><td>12/2025a</td><td>12/2026e</td><td>12/2027e</td><td>12/2028e</td></tr><tr><td colspan="5">Profit &amp; loss summary (USDm)</td></tr><tr><td>Revenue</td><td>67,535</td><td>70,025</td><td>71,325</td><td>75,081</td></tr><tr><td>EBITDA</td><td>16,843</td><td>15,619</td><td>17,199</td><td>18,214</td></tr><tr><td>Depreciation &amp; amortisation</td><td>-5,022</td><td>-3,605</td><td>-4,319</td><td>-3,655</td></tr><tr><td>Operating profit/EBIT</td><td>11,821</td><td>12,014</td><td>12,880</td><td>14,559</td></tr><tr><td>Net interest</td><td>-1,935</td><td>-1,937</td><td>-2,043</td><td>-2,097</td></tr><tr><td>PBT</td><td>10,329</td><td>10,735</td><td>11,155</td><td>13,038</td></tr><tr><td>HSBC PBT</td><td>12,713</td><td>13,744</td><td>14,067</td><td>15,950</td></tr><tr><td>Taxation</td><td>242</td><td>-1,584</td><td>-1,785</td><td>-2,086</td></tr><tr><td>Net profit</td><td>10,571</td><td>9,151</td><td>9,370</td><td>10,952</td></tr><tr><td>HSBC net profit</td><td>10,994</td><td>11,607</td><td>11,817</td><td>13,398</td></tr><tr><td colspan="5">Cash flow summary (USDm)</td></tr><tr><td>Cash flow from operations</td><td>13,193</td><td>16,772</td><td>15,718</td><td>17,737</td></tr><tr><td>Capex</td><td>-1,617</td><td>-1,574</td><td>-1,600</td><td>-1,600</td></tr><tr><td>Cash flow from investment</td><td>-10,302</td><td>-11,770</td><td>-1,600</td><td>-1,600</td></tr><tr><td>Dividends</td><td>-6,254</td><td>-6,354</td><td>-6,409</td><td>-6,450</td></tr><tr><td>Change in net debt</td><td>2,950</td><td>2,345</td><td>-7,845</td><td>-10,254</td></tr><tr><td>FCF equity</td><td>11,575</td><td>15,230</td><td>14,118</td><td>16,137</td></tr><tr><td colspan="5">Balance sheet summary (USDm)</td></tr><tr><td>Intangible fixed assets</td><td>79,108</td><td>87,561</td><td>85,781</td><td>84,246</td></tr><tr><td>Tangible fixed assets</td><td>33,715</td><td>32,409</td><td>31,483</td><td>31,018</td></tr><tr><td>Current assets</td><td>36,944</td><td>35,308</td><td>41,376</td><td>50,565</td></tr><tr><td>Cash &amp; others</td><td>30,654</td><td>28,036</td><td>33,881</td><td>42,134</td></tr><tr><td>Total assets</td><td>151,879</td><td>157,306</td><td>160,669</td><td>167,858</td></tr><tr><td>Operating liabilities</td><td>48,861</td><td>49,708</td><td>50,398</td><td>53,284</td></tr><tr><td>Gross debt</td><td>61,260</td><td>60,987</td><td>58,987</td><td>56,987</td></tr><tr><td>Net debt</td><td>30,606</td><td>32,951</td><td>25,106</td><td>14,853</td></tr><tr><td>Shareholders&#x27; funds</td><td>32,740</td><td>38,008</td><td>42,681</td><td>48,984</td></tr><tr><td>Invested capital</td><td>70,252</td><td>77,533</td><td>74,361</td><td>70,411</td></tr></table>

## Reduce

Key forecast drivers  
Ratio, growth and per share analysis

<table><tr><td>Year to</td><td>12/2025a</td><td>12/2026e</td><td>12/2027e</td><td>12/2028e</td></tr><tr><td>Revenue growth</td><td>8</td><td>4</td><td>2</td><td>5</td></tr><tr><td>Non-GAAP operating margin</td><td>21</td><td>21</td><td>22</td><td>23</td></tr><tr><td>Non-GAAP profit before tax margin</td><td>19</td><td>20</td><td>20</td><td>21</td></tr><tr><td>Non-GAAP EPS growth</td><td>12</td><td>5</td><td>1</td><td>13</td></tr></table>

Valuation data

<table><tr><td>Year to</td><td>12/2025a</td><td>12/2026e</td><td>12/2027e</td><td>12/2028e</td></tr><tr><td>EV/sales</td><td>3.3</td><td>3.2</td><td>3.0</td><td>2.7</td></tr><tr><td>EV/EBITDA</td><td>13.2</td><td>14.4</td><td>12.6</td><td>11.3</td></tr><tr><td>EV/IC</td><td>3.2</td><td>2.9</td><td>2.9</td><td>2.9</td></tr><tr><td>PE*</td><td>17.8</td><td>16.9</td><td>16.7</td><td>14.8</td></tr><tr><td>PB</td><td>5.9</td><td>5.1</td><td>4.6</td><td>4.0</td></tr><tr><td>FCF yield (%)</td><td>6.0</td><td>7.9</td><td>7.3</td><td>8.3</td></tr><tr><td>Dividend yield (%)</td><td>3.3</td><td>3.3</td><td>3.3</td><td>3.3</td></tr></table>

\* Based on HSBC EPS (diluted)

ESG metrics

<table><tr><td>Environmental Indicators</td><td>12/2024a</td></tr><tr><td>GHG emission intensity*</td><td>n/a</td></tr><tr><td>Energy intensity*</td><td>n/a</td></tr><tr><td>CO2 reduction policy</td><td>Yes</td></tr><tr><td>Social Indicators</td><td>12/2024a</td></tr><tr><td>Employee costs as % of revenues</td><td>n/a</td></tr><tr><td>Employee turnover (%)</td><td>n/a</td></tr><tr><td>Diversity policy</td><td>Yes</td></tr></table>

<table><tr><td>Governance Indicators</td><td>12/2025a</td></tr><tr><td>No. of board members</td><td>13</td></tr><tr><td>Average board tenure (years)</td><td>n/a</td></tr><tr><td>Female board members (%)</td><td>23.1</td></tr><tr><td>Board members independence (%)</td><td>92.3</td></tr></table>

Source: Company data, HSBC  
\* GHG intensity and energy intensity are measured in kg and kWh respectively against revenue in USD '000s

<table><tr><td>Year to</td><td>12/2025a</td><td>12/2026e</td><td>12/2027e</td><td>12/2028e</td></tr><tr><td colspan="5">Y-o-y % change</td></tr><tr><td>Revenue</td><td>7.6</td><td>3.7</td><td>1.9</td><td>5.3</td></tr><tr><td>EBITDA</td><td>22.3</td><td>-7.3</td><td>10.1</td><td>5.9</td></tr><tr><td>Operating profit</td><td>26.0</td><td>1.6</td><td>7.2</td><td>13.0</td></tr><tr><td>PBT</td><td>78.2</td><td>3.9</td><td>3.9</td><td>16.9</td></tr><tr><td>HSBC EPS</td><td>11.7</td><td>5.0</td><td>1.1</td><td>12.7</td></tr><tr><td colspan="5">Ratios (%)</td></tr><tr><td>Revenue/IC (x)</td><td>1.0</td><td>0.9</td><td>0.9</td><td>1.0</td></tr><tr><td>ROIC</td><td>18.2</td><td>13.9</td><td>14.2</td><td>16.9</td></tr><tr><td>ROE</td><td>36.6</td><td>32.8</td><td>29.3</td><td>29.2</td></tr><tr><td>ROA</td><td>8.7</td><td>7.0</td><td>7.0</td><td>7.7</td></tr><tr><td>EBITDA margin</td><td>24.9</td><td>22.3</td><td>24.1</td><td>24.3</td></tr><tr><td>Operating profit margin</td><td>17.5</td><td>17.2</td><td>18.1</td><td>19.4</td></tr><tr><td>EBITDA/net interest (x)</td><td>8.7</td><td>8.1</td><td>8.4</td><td>8.7</td></tr><tr><td>Net debt/equity</td><td>93.5</td><td>86.7</td><td>58.8</td><td>30.3</td></tr><tr><td>Net debt/EBITDA (x)</td><td>1.8</td><td>2.1</td><td>1.5</td><td>0.8</td></tr><tr><td>CF from operations/net debt</td><td>43.1</td><td>50.9</td><td>62.6</td><td>119.4</td></tr><tr><td colspan="5">Per share data (USD)</td></tr><tr><td>EPS Rep (diluted)</td><td>11.14</td><td>9.59</td><td>9.76</td><td>11.33</td></tr><tr><td>HSBC EPS (diluted)</td><td>11.59</td><td>12.16</td><td>12.30</td><td>13.86</td></tr><tr><td>DPS</td><td>6.71</td><td>6.75</td><td>6.76</td><td>6.76</td></tr><tr><td>Book value</td><td>35.12</td><td>40.36</td><td>45.00</td><td>51.32</td></tr></table>

Issuer information

<table><tr><td>Share price (USD)</td><td>205.77</td></tr><tr><td>Target price (USD)</td><td>174.00</td></tr><tr><td>RIC (Equity)</td><td>IBM.N</td></tr><tr><td>Bloomberg (Equity)</td><td>IBM US</td></tr><tr><td>Market cap (USDm)</td><td>193,400</td></tr></table>

<table><tr><td>Free float</td><td>100%</td></tr><tr><td>Sector</td><td>It Services</td></tr><tr><td>Country/Region</td><td>United States</td></tr><tr><td>Analyst</td><td>Abhishek Shukla, CFA</td></tr><tr><td>Contact</td><td>+971 4 5093343</td></tr></table>

Price relative  
![](images/3631b91dd2c1f1da1b9ccf2ec42ec319e34749fb3a7627adad981b02a18f7adb.jpg)  
Source: HSBC

Note: Priced at close of 22 Jul 2026

## Impressive margin guidance

IBM announced its 2Q26 results on 22 July 2026. The company pre-announced most of the key income statement items on 14 July 2026 but had not updated its full year guidance.

2Q26 revenue rose 1% y-o-y (constant currency) to USD17,161m (1Q26: 6%). The company cut its 2026 constant currency revenue growth guidance to 4%-5% from more than 5% previously.

Despite the cut to revenue growth guidance, the management maintained it expects non-GAAP profit before tax margin to rise by 100bp y-o-y due to higher productivity and efficiency, better supply chain optimization and lower third-party spend. 2Q26 non-GAAP profit before tax margin rose 30bp y-o-y but it was largely a result of a favourable USD280m non-GAAP other income in 2Q26 (2Q25: USD65m). Non-GAAP operating margin dipped 106bp y-o-y to $20.4\%$ . But for the favourable impact of other income, the non-GAAP PBT margin would have been down about 90bp y-o-y.

IBM: Evolution of results

<table><tr><td>USDm, FYE Dec</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26</td><td>3Q26e</td><td>4Q26e</td></tr><tr><td>Revenue</td><td>17,554</td><td>14,541</td><td>16,978</td><td>16,330</td><td>19,686</td><td>15,918</td><td>17,161</td><td>16,697</td><td>20,248</td></tr><tr><td>Software</td><td>7,924</td><td>6,336</td><td>7,387</td><td>7,209</td><td>9,031</td><td>7,052</td><td>7,761</td><td>7,544</td><td>9,423</td></tr><tr><td>Consulting</td><td>5,175</td><td>5,068</td><td>5,314</td><td>5,324</td><td>5,349</td><td>5,272</td><td>5,327</td><td>5,317</td><td>5,388</td></tr><tr><td>Infrastructure</td><td>4,256</td><td>2,886</td><td>4,142</td><td>3,559</td><td>5,132</td><td>3,326</td><td>3,835</td><td>3,612</td><td>5,234</td></tr><tr><td>Other</td><td>199</td><td>251</td><td>135</td><td>238</td><td>174</td><td>268</td><td>238</td><td>225</td><td>204</td></tr><tr><td>Revenue: y-o-y</td><td>0.5%</td><td>0.5%</td><td>7.7%</td><td>9.1%</td><td>12.1%</td><td>9.5%</td><td>1.1%</td><td>2.2%</td><td>2.9%</td></tr><tr><td>Software</td><td>10.4%</td><td>7.4%</td><td>9.6%</td><td>10.5%</td><td>14.0%</td><td>11.3%</td><td>5.1%</td><td>4.6%</td><td>4.3%</td></tr><tr><td>Consulting</td><td>-2.0%</td><td>-2.3%</td><td>2.6%</td><td>3.3%</td><td>3.4%</td><td>4.0%</td><td>0.2%</td><td>-0.1%</td><td>0.7%</td></tr><tr><td>Infrastructure</td><td>-7.6%</td><td>-6.2%</td><td>13.6%</td><td>17.0%</td><td>20.6%</td><td>15.2%</td><td>-7.4%</td><td>1.5%</td><td>2.0%</td></tr><tr><td>Revenue: y-o-y, constant FX</td><td>2.0%</td><td>2.0%</td><td>5.0%</td><td>7.0%</td><td>9.0%</td><td>6.0%</td><td>1.0%</td><td>3.8%</td><td>3.9%</td></tr><tr><td>Software</td><td>9.0%</td><td>9.0%</td><td>8.0%</td><td>9.0%</td><td>11.0%</td><td>8.0%</td><td>4.6%</td><td>6.2%</td><td>5.3%</td></tr><tr><td>Consulting</td><td>1.0%</td><td>0.0%</td><td>0.0%</td><td>2.0%</td><td>1.0%</td><td>1.0%</td><td>1.1%</td><td>1.4%</td><td>1.7%</td></tr><tr><td>Infrastructure</td><td>-3.0%</td><td>-4.0%</td><td>11.0%</td><td>15.0%</td><td>17.0%</td><td>12.0%</td><td>-7.4%</td><td>3.0%</td><td>3.0%</td></tr><tr><td>FX effect</td><td>-1.5%</td><td>-1.5%</td><td>2.7%</td><td>2.1%</td><td>3.1%</td><td>3.5%</td><td>0.1%</td><td>-1.5%</td><td>-1.0%</td></tr><tr><td>Operating profit (Non-GAAP)</td><td>4,403</td><td>2,005</td><td>3,641</td><td>3,334</td><td>5,149</td><td>2,505</td><td>3,498</td><td>3,463</td><td>5,326</td></tr><tr><td>Margin</td><td>25.1%</td><td>13.8%</td><td>21.4%</td><td>20.4%</td><td>26.2%</td><td>15.7%</td><td>20.4%</td><td>20.7%<

[中间内容因长度限制已省略]

 customers, this research is distributed by HSBC Bank Australia Limited (ABN 48 006 434 162, AFSL No. 232595). These respective entities make no representations that the products or services mentioned in this document are available to persons in Australia or are necessarily suitable for any particular person or appropriate in accordance with local law. No consideration has been given to the particular investment objectives, financial situation or particular needs of any recipient.

HSBC Securities (USA) Inc. accepts responsibility for the content of this research report prepared by its non-US foreign affiliate. The information contained herein is under no circumstances to be construed as investment advice and is not tailored to the needs of the recipient. All U.S. persons receiving and/or accessing this report and wishing to effect transactions in any security discussed herein should do so with HSBC Securities (USA) Inc. in the United States and not with its non-US foreign affiliate, the issuer of this report. HSBC México, S.A., Institución de Banca Múltiple, Grupo Financiero HSBC is authorized and regulated by Secretaría de Hacienda y Crédito Público and Comisión Nacional Bancaria y de Valores (CNBV). In Brazil, this document has been distributed by Banco HSBC SA ("HSBC Brazil"), and/or its affiliates. As required by Resolution No. 20/2021 of the Securities and Exchange Commission of Brazil (Comissão de Valores Mobiliários), potential conflicts of interest concerning (i) HSBC Brazil and/or its affiliates; and (ii) the analyst(s) responsible for authoring this report are stated on the chart above labelled "HSBC & Analyst Disclosures".

This document is not and should not be construed as an offer to sell or the solicitation of an offer to purchase or subscribe for any investment. HSBC has based this document on information obtained from sources it believes to be reliable but which it has not independently verified; HSBC makes no guarantee, representation or warranty and accepts no responsibility or liability as to its accuracy or completeness. The opinions contained within the report are based upon publicly available information at the time of publication and are subject to change without notice. From time to time research analysts conduct site visits of covered issuers. HSBC policies prohibit research analysts from accepting payment or reimbursement for travel expenses from the issuer for such visits. Past performance is not necessarily a guide to future performance. The value of any investment or income may go down as well as up and you may not get back the full amount invested. Where an investment is denominated in a currency other than the local currency of the recipient of the research report, changes in the exchange rates may have an adverse effect on the value, price or income of that investment. In case of investments for which there is no recognised market it may be difficult for investors to sell their investments or to obtain reliable information about its value or the extent of the risk to which it is exposed. The document is intended to be distributed in its entirety. Unless governing law permits otherwise, you must contact a HSBC Group member in your home jurisdiction if you wish to use HSBC Group services in effecting a transaction in any investment mentioned in this document.

If you are a customer of HSBC International Wealth & Premier Banking ("IWPB"), including HSBC Private Bank, you are eligible to receive this publication only if: (i) you have been approved to receive relevant research publications by an applicable HSBC legal entity; (ii) you have agreed to the applicable HSBC entity's terms and conditions and/or customer declaration for accessing research; and (iii) you have agreed to the terms and conditions of any other internet banking, online banking, mobile banking and/or investment services offered by that HSBC entity, through which you will access research publications (collectively with (ii), the "Terms"). If you do not meet the above eligibility requirements, please disregard this publication and, if you are a IWPB customer, please notify your Relationship Manager or call the relevant customer hotline. Distribution of this publication is the sole responsibility of the HSBC entity with whom you have agreed the Terms. Receipt of research publications is strictly subject to the Terms and any other conditions or disclaimers applicable to the provision of the publications that may be advised by IWPB. © Copyright 2026, HSBC Bank Middle East Limited, DIFC, ALL RIGHTS RESERVED. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, on any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of HSBC Bank Middle East Limited.
"""
