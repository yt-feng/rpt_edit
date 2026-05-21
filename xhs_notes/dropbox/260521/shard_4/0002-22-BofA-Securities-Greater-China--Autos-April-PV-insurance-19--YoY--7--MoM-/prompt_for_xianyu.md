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
# April PV insurance -19% YoY/-7% MoM; channel inventory declined; EV -6% YoY

Industry Overview

# April PV insurance reg. -19% YoY; inventory destocking

In April, PV insurance registrations (retail sales) came in at 1.36mn units, down 19% YoY/down 7% MoM. In 4M26, PV insurance registrations were down 18% YoY. Based on the variation between wholesales (2.13mn, -4% YoY, as reported by CAAM) and insurance registrations, and considering the export volume (796k units), we estimate channel inventory decreased 23k units in April. Geographically, some provinces/cities, such as Jiangsu, Zhejiang, Hunan, and Shanghai outperformed, while Shandong, Henan, Sichuan, Hebei, and Anhui underperformed in April.

# EV insurance reg. -6% YoY/+3% MoM to 827k units

Locally manufactured EVs' insurance registrations totaled 827k units in April, down $6\%$ YoY/up $3\%$ MoM. In 4M26, domestic EVs' insurance registrations were down $18\%$ YoY. Among OEMs, Geely, Changan, Li Auto, NIO, Xiaomi, Leapmotor, AITO, and BAIC BJEV outgrew the EV market in April. BYD's insurance registrations were down $30\%$ YoY to 184k units. Tesla's domestic sales were down $11\%$ YoY to 26k units: Model 3 sales came in at 3k units and Model Y at 23k units (including 4k Model Y L). April registration numbers for EV startups: Li Auto 34k units $(-4\%$ YoY), XPeng 25k units $(-17\%$ YoY), AITO 23k units $(+10\%$ YoY), GAC Aion 22k units $(-12\%$ YoY), Leapmotor 50k units $(+53\%$ YoY), NIO 34k units $(+34\%$ YoY), and Zeekr (excluding Lynk) 23k units $(+86\%$ YoY).

# Most JV brands and luxury brands declined in April

Among JV brands, Japanese JV brands like GAC Honda (-49% YoY), GAC Toyota (-18% YoY), DF Honda (-47% YoY), DF Nissan (-13% YoY), and FAW Toyota (-21% YoY) saw a drop in April. In addition, other JV brands, including Changan Ford (-54% YoY), FAW VW (-33% YoY), SGM Wuling (-32% YoY), SAIC GM (-32% YoY), and SAIC VW (-46% YoY) also posted sales decline in April. Among luxury brands, Lexus was -34% YoY, FAW Audi -38% YoY, Brilliance BMW -20% YoY, Beijing Benz -32% YoY, and Porsche -45% YoY.

# Own brands: SAIC PV outperformed among peers

Vehicle insurance registrations for Geely (including Lynk/Zeekr)/GWM/Changan were down 6% YoY/down 16% YoY/ down 11% YoY in April. GAC Trumpchi was down 34% YoY; GAC Aion was down 12% YoY. DF Fengshen saw 38% YoY decline, while SAIC PV saw 33% YoY growth due to delivery of Shangjie H5 and Z7/Z7T.

# 19 May 2026

Equity

Greater China

Autos

Ming Hsun Lee, CFA >>

Research Analyst

BofA (Hong Kong)

+852 3508 5006

minghsun.lee@bofa.com

Joey Yang, CFA >>

Research Analyst

BofA (Hong Kong)

+852 3508 4021

joey.z.yang@bofa.com

Fiona Liang >>

Research Analyst

BofA (Hong Kong)

+852 3508 4390

fiona.liang3@bofa.com

Jessie Lo >>

Research Analyst

BofA (Singapore)

+65 6678 1134

jessie.lo@bofa.com

PV: Passenger vehicle

CAAM: China Association of

Automobile Manufacturers

EV: Electric vehicle

OEM: Original equipment

manufacturer

JV: Joint venture

BEV: Battery electric vehicle

PHEV: Plug-in hybrid electric vehicle

>> Employed by a non-US affiliate of BofAS and is not registered/qualified as a research analyst under the FINRA rules.
Refer to "Other Important Disclosures" for information on certain BofA entities that take responsibility for the information herein in particular jurisdictions.
BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.

Exhibit 1: Industry's monthly inventory changes   
Inventory at channels decreased 23k units in April, after adjusting for export volumes   
![](images/ba4f03abba50b974cfbb87eacbad040b0e7a090442dabe604d17cecb0585c722.jpg)

<details>
<summary>bar</summary>

| Month | Inventory |
|---|---|
| Jan-16 | 150000 |
| Jun-16 | 220000 |
| Nov-16 | -100000 |
| Apr-17 | 480000 |
| Sep-17 | -150000 |
| Feb-18 | 280000 |
| Jul-18 | 300000 |
| Dec-18 | -700000 |
| May-19 | 500000 |
| Oct-19 | 180000 |
| Mar-20 | -25000 |
| Aug-20 | 150000 |
| Jan-21 | -350000 |
| Jun-21 | -150000 |
| Nov-21 | 320000 |
| Apr-22 | 220000 |
| Sep-22 | 280000 |
| Feb-23 | -450000 |
| Jul-23 | 50000 |
| Dec-23 | -150000 |
| May-24 | 80000 |
| Oct-24 | -15000 |
| Mar-25 | 180000 |
| Aug-25 | 380000 |
| Jan-26 | -18000 |
</details>

Source: China auto market, CAAM   
BofA GLOBAL RESEARCH

Exhibit 2: Monthly vehicle insurance data (vehicles manufactured in China only)   
April PV insurance registrations came in at 1.36mn units, down $19\%$ YoY/7% MoM   
![](images/f9bcab1961fc8a4954929a13afdb6cc69b862f70c4577bbde799c2e5ebf442e9.jpg)

<details>
<summary>bar_line</summary>

| Month    | Industry insurance registration (LHS) | YoY% (RHS) |
|----------|----------------------------------------|------------|
| Jan-18   | 2.1                                    | 0%         |
| Jun-18   | 1.7                                    | -10%       |
| Nov-18   | 2.6                                    | 0%         |
| Apr-19   | 1.4                                    | 100%       |
| Sep-19   | 1.8                                    | -50%       |
| Feb-20   | 1.0                                    | -150%      |
| Jul-20   | 1.6                                    | 50%        |
| Dec-20   | 2.4                                    | 550%       |
| May-21   | 1.5                                    | -50%       |
| Oct-21   | 2.2                                    | 0%         |
| Mar-22   | 1.3                                    | -50%       |
| Aug-22   | 1.8                                    | 0%         |
| Jan-23   | 2.5                                    | 50%        |
| Jun-23   | 1.9                                    | -50%       |
| Nov-23   | 2.4                                    | 0%         |
| Apr-24   | 1.7                                    | -50%       |
| Sep-24   | 2.3                                    | 0%         |
| Feb-25   | 2.7                                    | 50%        |
| Jul-25   | 2.1                                    | -50%       |
| Dec-25   | 1.4                                    | -100%      |
</details>

Source: China auto market   
BofA GLOBAL RESEARCH

Exhibit 3: Market share of major EV startups and BYD in China BEV + PHEV

In April, Tesla's market share was $3.2\%$ , while BYD's $22.2\%$

<table><tr><td>Sales volume</td><td>May-25</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>4M26</td></tr><tr><td>BYD</td><td>282,328</td><td>339,083</td><td>263,495</td><td>303,311</td><td>344,155</td><td>295,520</td><td>302,929</td><td>327,862</td><td>104,714</td><td>87,490</td><td>185,053</td><td>183,938</td><td>561,195</td></tr><tr><td>Tesla</td><td>39,236</td><td>61,519</td><td>41,353</td><td>57,225</td><td>71,115</td><td>27,477</td><td>72,856</td><td>93,621</td><td>20,026</td><td>38,111</td><td>55,286</td><td>26,513</td><td>139,936</td></tr><tr><td>Li Auto</td><td>44,606</td><td>36,015</td><td>31,234</td><td>28,229</td><td>34,502</td><td>31,338</td><td>32,174</td><td>43,131</td><td>27,653</td><td>26,102</td><td>40,381</td><td>33,506</td><td>127,642</td></tr><tr><td>Leap Motor</td><td>32,017</td><td>40,623</td><td>39,896</td><td>48,870</td><td>58,850</td><td>50,474</td><td>45,783</td><td>56,275</td><td>21,495</td><td>16,584</td><td>37,711</td><td>49,848</td><td>125,638</td></tr><tr><td>NIO</td><td>25,349</td><td>22,073</td><td>21,792</td><td>33,228</td><td>34,248</td><td>38,552</td><td>36,062</td><td>45,538</td><td>29,873</td><td>21,020</td><td>34,590</td><td>33,594</td><td>119,077</td></tr><tr><td>Xiaomi</td><td>28,019</td><td>25,465</td><td>30,335</td><td>36,313</td><td>42,020</td><td>48,354</td><td>46,418</td><td>50,212</td><td>39,406</td><td>20,511</td><td>22,418</td><td>36,724</td><td>119,059</td></tr><tr><td>AITO</td><td>35,968</td><td>44,498</td><td>41,664</td><td>39,296</td><td>40,994</td><td>44,367</td><td>51,511</td><td>60,777</td><td>38,904</td><td>16,393</td><td>16,910</td><td>23,247</td><td>95,454</td></tr><tr><td>Zeekr (exclude Lynk)</td><td>16,623</td><td>13,653</td><td>13,978</td><td>14,805</td><td>14,367</td><td>16,494</td><td>23,221</td><td>25,865</td><td>19,088</td><td>14,712</td><td>23,594</td><td>23,010</td><td>80,404</td></tr><tr><td>XPeng</td><td>27,038</td><td>32,635</td><td>31,719</td><td>35,345</td><td>38,298</td><td>34,835</td><td>29,290</td><td>34,518</td><td>15,976</td><td>12,691</td><td>21,670</td><td>25,352</td><td>75,689</td></tr><tr><td>GAC Aion</td><td>24,686</td><td>28,605</td><td>25,786</td><td>24,482</td><td>27,658</td><td>22,133</td><td>24,642</td><td>32,358</td><td>15,792</td><td>7,930</td><td>22,730</td><td>21,506</td><td>67,958</td></tr><tr><td>Total NEV sales</td><td>973,110</td><td>1,120,170</td><td>985,783</td><td>1,107,772</td><td>1,298,853</td><td>1,199,373</td><td>1,227,640</td><td>1,338,917</td><td>567,287</td><td>432,117</td><td>806,066</td><td>827,550</td><td>2,633,020</td></tr><tr><td>Market share</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>BYD</td><td>29.0%</td><td>30.3%</td><td>26.7%</td><td>27.4%</td><td>26.5%</td><td>24.6%</td><td>24.7%</td><td>24.5%</td><td>18.5%</td><td>20.2%</td><td>23.0%</td><td>22.2%</td><td>21.3%</td></tr><tr><td>Tesla</td><td>4.0%</td><td>5.5%</td><td>4.2%</td><td>5.2%</td><td>5.5%</td><td>2.3%</td><td>5.9%</td><td>7.0%</td><td>3.5%</td><td>8.8%</td><td>6.9%</td><td>3.2%</td><td>5.3%</td></tr><tr><td>Li Auto</td><td>4.6%</td><td>3.2%</td><td>3.2%</td><td>2.5%</td><td>2.7%</td><td>2.6%</td><td>2.6%</td><td>3.2%</td><td>4.9%</td><td>6.0%</td><td>5.0%</td><td>4.0%</td><td>4.8%</td></tr><tr><td>Leap Motor</td><td>3.3%</td><td>3.6%</td><td>4.0%</td><td>4.4%</td><td>4.5%</td><td>4.2%</td><td>3.7%</td><td>4.2%</td><td>3.8%</td><td>3.8%</td><td>4.7%</td><td>6.0%</td><td>4.8%</td></tr><tr><td>NIO</td><td>2.6%</td><td>2.0%</td><td>2.2%</td><td>3.0%</td><td>2.6%</td><td>3.2%</td><td>2.9%</td><td>3.4%</td><td>5.3%</td><td>4.9%</td><td>4.3%</td><td>4.1%</td><td>4.5%</td></tr><tr><td>Xiaomi</td><td>2.9%</td><td>2.3%</td><td>3.1%</td><td>3.3%</td><td>3.2%</td><td>4.0%</td><td>3.8%</td><td>3.8%</td><td>6.9%</td><td>4.7%</td><td>2.8%</td><td>4.4%</td><td>4.5%</td></tr><tr><td>AITO</td><td>3.7%</td><td>4.0%</td><td>4.2%</td><td>3.5%</td><td>3.2%</td><td>3.7%</td><td>4.2%</td><td>4.5%</td><td>6.9%</td><td>3.8%</td><td>2.1%</td><td>2.8%</td><td>3.6%</td></tr><tr><td>Zeekr (exclude Lynk)</td><td>1.7%</td><td>1.2%</td><td>1.4%</td><td>1.3%</td><td>1.1%</td><td>1.4%</td><td>1.9%</td><td>1.9%</td><td>3.4%</td><td>3.4%</td><td>2.9%</td><td>2.8%</td><td>3.1%</td></tr><tr><td>XPeng</td><td>2.8%</td><td>2.9%</td><td>3.2%</td><td>3.2%</td><td>2.9%</td><td>2.9%</td><td>2.4%</td><td>2.6%</td><td>2.8%</td><td>2.9%</td><td>2.7%</td><td>3.1%</td><td>2.9%</td></tr><tr><td>GAC Aion</td><td>2.5%</td><td>2.6%</td><td>2.6%</td><td>2.2%</td><td>2.1%</td><td>1.8%</td><td>2.0%</td><td>2.4%</td><td>2.8%</td><td>1.8%</td><td>2.8%</td><td>2.6%</td><td>2.6%</td></tr></table>

Source: China auto market   
BofA GLOBAL RESEARCH

Exhibit 4: Monthly vehicle insurance registration (retail sales in China, export sales not included)   
Among OEMs, SAIC PV, Geely, GAC Toyota, GAC Aions, Changan, DF Nissan, GWM, Tesla, NIO, XPeng, and Li outperformed in April 

<table><tr><td>(units)</td><td>May-25</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>4M26</td></tr><tr><td>BYD brand</td><td>257,719</td><td>308,612</td><td>240,146</td><td>278,916</td><td>311,373</td><td>258,343</td><td>256,342</td><td>263,532</td><td>77,244</td><td>69,588</td><td>158,831</td><td>155,085</td><td>460,748</td></tr><tr><td>Denza</td><td>12,417</td><td>11,963</td><td>9,526</td><td>9,269</td><td>10,233</td><td>7,770</td><td>11,938</td><td>15,891</td><td>6,186</td><td>4,284</td><td>5,105</td><td>9,278</td><td>24,853</td></tr><tr><td>Fangchengbao</td><td>12,059</td><td>18,309</td><td>13,482</td><td>14,709</td><td>21,855</td><td>28,782</td><td>33,983</td><td>47,567</td><td>20,849</td><td>13,387</td><td>20,819</td><td>19,312</td><td>74,367</td></tr><tr><td>Yangwang</td><td>133</td><td>199</td><td>341</td><td>417</td><td>694</td><td>625</td><td>666</td><td>872</td><td>435</td><td>231</td><td>298</td><td>263</td><td>1,227</td></tr><tr><td>SAIC VW</td><td>84,865</td><td>100,351</td><td>81,085</td><td>81,420</td><td>86,127</td><td>82,763</td><td>68,610</td><td>85,717</td><td>86,305</td><td>66,099</td><td>54,798</td><td>43,816</td><td>251,018</td></tr><tr><td>SAIC GM</td><td>43,213</td><td>46,731</td><td>39,752</td><td>41,650</td><td>47,209</td><td>42,790</td><td>41,465</td><td>51,019</td><td>48,660</td><td>32,840</td><td>32,539</td><td>27,198</td><td>141,237</td></tr><tr><td>SAIC GM Wuling</td><td>63,999</td><td>67,426</td><td>64,091</td><td>79,981</td><td>92,487</td><td>112,631</td><td>97,331</td><td>60,090</td><td>32,350</td><td>28,977</td><td>50,519</td><td>43,097</td><td>154,943</td></tr><tr><td>SAIC PV</td><td>20,948</td><td>21,159</td><td>21,545</td><td>24,638</td><td>37,540</td><td>41,873</td><td>41,926</td><td>35,714</td><td>28,336</td><td>19,217</td><td>25,811</td><td>28,622</td><td>101,986</td></tr><tr><td>FAW VW</td><td>81,419</td><td>96,601</td><td>73,946</td><td>73,827</td><td>83,709</td><td>83,087</td><td>67,243</td><td>86,012</td><td>81,780</td><td>62,044</td><td>54,578</td><td>46,577</td><td>244,979</td></tr><tr><td>FAW Toyota</td><td>63,776</td><td>74,374</td><td>66,592</td><td>64,589</td><td>65,745</td><td>57,899</td><td>52,424</td><td>61,517</td><td>67,298</td><td>44,797</td><td>55,028</td><td>47,212</td><td>214,335</td></tr><tr><td>FAW VW Audi</td><td>39,916</td><td>47,209</td><td>34,644</td><td>37,415</td><td>50,250</td><td>45,057</td><td>45,057</td><td>56,896</td><td>55,094</td><td>30,935</td><td>33,665</td><td>22,604</td><td>142,298</td></tr><tr><td>Geely brand</td><td>145,506</td><td>172,981</td><td>158,531</td><td>177,339</td><td>198,956</td><td>183,665</td><td>169,641</td><td>188,889</td><td>120,098</td><td>100,770</td><td>124,857</td><td>115,662</td><td>461,387</td></tr><tr><td>Lynk</td><td>22,903</td><td>26,579</td><td>24,261</td><td>26,494</td><td>29,285</td><td>31,174</td><td>32,488</td><td>38,063</td><td>19,784</td><td>14,348</td><td>17,855</td><td>14,516</td><td>66,503</td></tr><tr><td>Zeekr</td><td>16,623</td><td>13,653</td><td>13,978</td><td>14,805</td><td>14,367</td><td>16,494</td><td>23,221</td><td>25,865</td><td>19,088</td><td>14,712</td><td>23,594</td><td>23,010</td><td>80,404</td></tr><tr><td>GAC Toyota</td><td>64,567</td><td>76,187</td><td>62,540</td><td>64,826</td><td>73,291</td><td>67,648</td><td>62,167</td><td>71,388</td><td>61,710</td><td>41,084</td><td>55,168</td><td>49,695</td><td>207,657</td></tr><tr><td>GAC Honda</td><td>26,996</td><td>32,190</td><td>23,305</td><td>27,459</td><td>27,397</td><td>28,218</td><td>28,054</td><td>36,029</td><td>22,499</td><td>12,725</td><td>15,097</td><td>12,065</td><td>62,386</td></tr><tr><td>GAC Aion</td><td>24,686</td><td>28,605</td><td>25,786</td><td>24,482</td><td>27,658</td><td>22,133</td><td>24,642</td><td>32,358</td><td>15,792</td><td>7,930</td><td>22,730</td><td>21,506</td><td>67,958</td></tr><tr><td>GAC Trumpchi</td><td>21,677</td><td>22,704</td><td>23,150</td><td>22,123</td><td>22,583</td><td>19,967</td><td>17,280</td><td>21,792</td><td>21,751</td><td>11,972</td><td>13,561</td><td>13,661</td><td>60,945</td></tr><tr><td>Changan</td><td>79,138</td><td>8

[中间内容因长度限制已省略]

lect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
