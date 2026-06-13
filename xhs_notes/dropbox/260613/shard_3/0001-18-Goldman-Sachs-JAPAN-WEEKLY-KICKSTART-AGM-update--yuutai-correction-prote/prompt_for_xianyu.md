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
JAPAN WEEKLY KICKSTART

# AGM update; yuutai correction protection

## Summary of the week

TOPIX: 3,881.96 (-1.7%) / NK225: 66,020.04 (-0.9%)

■ Top sectors: Insurance, Real Estate  
■ Bottom sectors: Non-Ferrous Metals, Communications

In this week's Japan Weekly Kickstart we focus on the current AGM season in Japan. As can be seen in Exhibit 1 below, the peak period for AGMs is 23-26 June in terms of the number of companies holding meetings. In Japan Portfolio Strategy: Finding multiple ways to win again: CY2026 1H corporate governance playbook (13 February 2026), we screened for companies that were in the bottom decile for AGM approval ratings during the CY2025 AGM season. So far, 10 out of 12 companies in the screen saw improvements in their approval rating this year (Exhibit 5).

Low AGM approval screen: Since the last AGM season, CY2025 low AGM approval rating screen outperformed the TOPIX by 13ppts until the start of the Iran conflict (Exhibit 4). However, they have not participated so far in the AI-driven rally since April. We believe that low AGM approvals are a strong predictor of shareholder-friendly activity going into the following year's AGM.

Yuutai-related stock performance since 3 June confirms their defensive qualities: Since we published Japan Portfolio Strategy: Unequal equities - How do stocks with shareholder benefits perform during major market corrections? (3 June 2026), our yuutai plus dividends screen (Exhibit 8) has out-performed our no yuutai, no dividends screen (Exhibit 9) by 12ppts, and has out-performed TOPIX by 4ppts (Exhibit 6).

Domestic demand defensives outperformed AI and Tech: The best-performing indices during this week's correction included Food and Beverage (+3% wow) and Retail (+3% wow), while worst-performers included System Integrators (-7% wow) and Apple Supply Chain (-6% wow).

Domestic Institutions and Individuals were net buyers, Foreigners were net sellers: According to the latest data from the TSE, for the week 1-5 June, Domestic institutions and Individuals net bought ¥214bn and ¥298bn of TSE Prime cash equities respectively, while Foreigners net sold -¥65bn.

Bruce Kirk, CFA

+81(3)4587-9950 | bruce.kirk@gs.com

GS Japan Co., Ltd.

Julius Chan

+81(3)4587-1789 | julius.chan@gs.com

GS Japan Co., Ltd.

## 2026 AGM schedule

Exhibit 1: Mar FY-end companies AGM schedule by number of companies  
![](images/32b17e942fd4d6b2f7a2a6875bd1dae807340c94edf868849ce6bd5c04bd9af2.jpg)

<details>
<summary>bar chart</summary>

| Date | By number of companies |
|---|---|
| 6/16 | 15 |
| 6/17 | 33 |
| 6/18 | 47 |
| 6/19 | 133 |
| 6/20 | 8 |
| 6/21 | 2 |
| 6/22 | 34 |
| 6/23 | 216 |
| 6/24 | 317 |
| 6/25 | 480 |
| 6/26 | 635 |
| 6/27 | 14 |
| 6/28 | 1 |
| 6/29 | 88 |
| 6/30 | 9 |
</details>

Source: JPX

Exhibit 2: Mar FY-end companies AGM schedule by market cap  
![](images/83e1718401db8e672b7ec302094377485d689779adb3be0ddf2b0c51c65ad29f.jpg)

<details>
<summary>bar chart</summary>

| Date | By market cap (JPY tn) |
|---|---|
| 6/16 | 2 |
| 6/17 | 35 |
| 6/18 | 32 |
| 6/19 | 118 |
| 6/20 | 1 |
| 6/21 | 0 |
| 6/22 | 43 |
| 6/23 | 130 |
| 6/24 | 182 |
| 6/25 | 145 |
| 6/26 | 289 |
| 6/27 | 4 |
| 6/28 | 0 |
| 6/29 | 50 |
| 6/30 | 1 |
</details>

Exhibit 3: Concentration of AGM for peak day increased slightly  
% of companies

![](images/99b8e5811b2068a104e49f68a630b0ec204a977db9f029a4405fd64ddf31b0fa.jpg)

<details>
<summary>line chart</summary>

| Fiscal Year | Most concentrated day | Top 5 days |
| ----------- | --------------------- | ---------- |
| FY98        | 90%                   | 98%        |
| 25          | 31.0%                 | 87.9%      |
</details>

Source: JPX

Exhibit 4: Since the 2025 AGM season, low approval screen outperformed until the start of the Iran war, but remains a laggard as the market focused on AI themes  
![](images/19e5c0c365c40de79be855652f99ef1e38f21ca7a9a79e056e3f9c9ad6e29073.jpg)

<details>
<summary>line chart</summary>

| Date   | Low AGM rating / TOPIX | Nikkei 225 / TOPIX |
|--------|------------------------|--------------------|
| 7/25   | 100                    | 100                |
| 8/25   | 100                    | 100                |
| 9/25   | 100                    | 100                |
| 10/25  | 100                    | 100                |
| 11/25  | 100                    | 110                |
| 12/25  | 105                    | 105                |
| 1/26   | 105                    | 105                |
| 2/26   | 110                    | 105                |
| 3/26   | 110                    | 105                |
| 4/26   | 105                    | 105                |
| 5/26   | 105                    | 115                |
| 6/26   | 105                    | 120                |
</details>

Source: FactSet, Data compiled by GS Global Investment Research

Exhibit 5: So far, 10 out of 12 companies in the low 2025 AGM approval screen saw improvement in approval rating this year

Data as of Jun 10, 2026

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Name</td><td rowspan="2">Sector</td><td rowspan="2">6M ADTV ($ mn)</td><td rowspan="2">Mcap (¥ bn)</td><td colspan="2">2025 Approval</td><td colspan="3">2026 Approval</td></tr><tr><td>Rating (%)</td><td>Fiscal Year end</td><td>Rating (%)</td><td>pt chg (%)</td><td>AGM date</td></tr><tr><td>6302</td><td>SUMITOMO HEAVY IND</td><td>Machinery</td><td>27</td><td>597</td><td>62.3</td><td>12/2024</td><td>70.6</td><td>+8.3</td><td>2026/3/27</td></tr><tr><td>7752</td><td>RICOH CO</td><td>Electric Appliances</td><td>20</td><td>831</td><td>64.0</td><td>03/2025</td><td></td><td></td><td>2026/6/23</td></tr><tr><td>8306</td><td>MITSUBISHI UFJ FIN</td><td>Banks</td><td>794</td><td>37,775</td><td>65.2</td><td>03/2025</td><td></td><td></td><td>2026/6/26</td></tr><tr><td>8316</td><td>SUMITOMO MITSUI FG</td><td>Banks</td><td>501</td><td>23,834</td><td>68.9</td><td>03/2025</td><td></td><td></td><td>2026/6/26</td></tr><tr><td>5844</td><td>KYOTO FINANCIAL GR</td><td>Banks</td><td>31</td><td>1,354</td><td>69.4</td><td>03/2025</td><td></td><td></td><td>2026/6/26</td></tr><tr><td>2579</td><td>COCA-COLA BOTTLERS</td><td>Foods</td><td>20</td><td>665</td><td>69.6</td><td>12/2024</td><td>83.6</td><td>+14.0</td><td>2026/3/26</td></tr><tr><td>6971</td><td>KYOCERA CORP</td><td>Electric Appliances</td><td>99</td><td>5,048</td><td>69.8</td><td>03/2025</td><td></td><td></td><td>2026/6/25</td></tr><tr><td>8630</td><td>SOMPO HOLDINGS INC</td><td>Insurance</td><td>98</td><td>5,742</td><td>70.3</td><td>03/2025</td><td></td><td></td><td>2026/6/22</td></tr><tr><td>5938</td><td>LIXIL CORPORATION</td><td>Metal Products</td><td>24</td><td>500</td><td>71.4</td><td>03/2025</td><td></td><td></td><td>2026/6/18</td></tr><tr><td>8308</td><td>RESONA HOLDINGS</td><td>Banks</td><td>114</td><td>4,935</td><td>71.9</td><td>03/2025</td><td></td><td></td><td>2026/6/24</td></tr><tr><td>2432</td><td>DENA CO LTD</td><td>Information &amp; Communication</td><td>31</td><td>325</td><td>72.0</td><td>03/2025</td><td></td><td></td><td>2026/6/27</td></tr><tr><td>8830</td><td>SUMITOMO RLTY&amp;DEV</td><td>Real Estate</td><td>84</td><td>3,267</td><td>73.0</td><td>03/2025</td><td></td><td></td><td>2026/6/26</td></tr><tr><td>3769</td><td>GMO PAYMENT GATEWA</td><td>Information &amp; Communication</td><td>18</td><td>600</td><td>73.1</td><td>09/2025</td><td></td><td></td><td>2026/12</td></tr><tr><td>5201</td><td>AGC INC</td><td>Glass &amp; Ceramics Products</td><td>59</td><td>1,509</td><td>73.7</td><td>12/2024</td><td>77.6</td><td>+3.9</td><td>2026/3/27</td></tr><tr><td>6471</td><td>NSK LTD</td><td>Machinery</td><td>21</td><td>550</td><td>74.5</td><td>03/2025</td><td></td><td></td><td>2026/6/25</td></tr><tr><td>4768</td><td>OTSUKA CORP</td><td>Information &amp; Communication</td><td>29</td><td>1,113</td><td>74.9</td><td>12/2024</td><td>na</td><td>na</td><td>2026/3/27</td></tr><tr><td>7276</td><td>KOITO MFG CO LTD</td><td>Electric Appliances</td><td>16</td><td>858</td><td>75.8</td><td>03/2025</td><td></td><td></td><td>2026/6/26</td></tr><tr><td>2160</td><td>GNI GROUP LTD</td><td>Pharmaceutical</td><td>25</td><td>153</td><td>76.3</td><td>12/2024</td><td>78.0</td><td>+1.7</td><td>2026/3/26</td></tr><tr><td>6278</td><td>UNION TOOL CO</td><td>Machinery</td><td>29</td><td>442</td><td>76.5</td><td>12/2024</td><td>80.3</td><td>+3.8</td><td>2026/3/26</td></tr><tr><td>9202</td><td>ANA HOLDINGS INC</td><td>Air Transportation</td><td>54</td><td>1,367</td><td>77.0</td><td>03/2025</td><td></td><td></td><td>2026/6/26</td></tr><tr><td>6861</td><td>KEYENCE CORP</td><td>Electric Appliances</td><td>344</td><td>17,727</td><td>77.1</td><td>03/2025</td><td></td><td></td><td>2026/6/12</td></tr><tr><td>3994</td><td>MONEY FORWARD INC</td><td>Information &amp; Communication</td><td>24</td><td>223</td><td>77.1</td><td>11/2024</td><td>89.4</td><td>+12.3</td><td>2026/2/26</td></tr><tr><td>3350</td><td>METAPLANET INC</td><td>Wholesale Trade</td><td>68</td><td>293</td><td>77.3</td><td>12/2024</td><td>89.3</td><td>+12.1</td><td>2026/3/25</td></tr><tr><td>8267</td><td>AEON CO LTD</td><td>Retail Trade</td><td>111</td><td>3,961</td><td>77.8</td><td>02/2025</td><td>94.0</td><td>+16.3</td><td>2026/5/27</td></tr><tr><td>4502</td><td>TAKEDA PHARMACEUTI</td><td>Pharmaceutical</td><td>162</td><td>8,068</td><td>77.9</td><td>03/2025</td><td></td><td></td><td>2026/6/24</td></tr><tr><td>3659</td><td>NEXON CO LTD</td><td>Information &amp; Communication</td><td>45</td><td>1,750</td><td>77.9</td><td>12/2024</td><td>75.2</td><td>-2.7</td><td>2026/3/25</td></tr><tr><td>7012</td><td>KAWASAKI HEAVY IND</td><td>Transportation Equipment</td><td>367</td><td>2,401</td><td>78.8</td><td>03/2025</td><td></td><td></td><td>2026/6/25</td></tr><tr><td>7014</td><td>NAMURA SHIPBUILDING</td><td>Transportation Equipment</td><td>47</td><td>237</td><td>79.1</td><td>03/2025</td><td></td><td></td><td>2026/6/23</td></tr><tr><td>1963</td><td>JGC HLDGS CORP</td><td>Construction</td><td>38</td><td>618</td><td>79.3</td><td>03/2025</td><td></td><td></td><td>2026/6/26</td></tr><tr><td>7013</td><td>IHI CORPORATION</td><td>Machinery</td><td>433</td><td>2,641</td><td>79.7</td><td>03/2025</td><td></td><td></td><td>2026/6/24</td></tr><tr><td>4506</td><td>SUMITOMO PHARMA CO</td><td>Pharmaceutical</td><td>157</td><td>637</td><td>79.9</td><td>03/2025</td><td></td><td></td><td>2026/6/25</td></tr><tr><td>5714</td><td>DOWA HOLDINGS</td><td>Nonferrous Metals</td><td>40</td><td>558</td><td>80.7</td><td>03/2025</td><td></td><td></td><td>2026/6/24</td></tr><tr><td>8750</td><td>DAI-ICHI LIFE HOLD</td><td>Insurance</td><td>84</td><td>6,397</td><td>80.8</td><td>03/2025</td><td></td><td></td><td>2026/6/22</td></tr><tr><td>5830</td><td>IYOGIN HOLDINGS IN</td><td>Banks</td><td>18</td><td>953</td><td>81.0</td><td>03/2025</td><td></td><td></td><td>2026/6/26</td></tr><tr><td>5711</td><td>MITSUBISHI MATERLS</td><td>Nonferrous Metals</td><td>55</td><td>588</td><td>81.0</td><td>03/2025</td><td></td><td></td><td>2026/6/23</td></tr><tr><td>4755</td><td>RAKUTEN GROUP INC</td><td>Services</td><td>73</td><td>1,571</td><td>81.0</td><td>12/2024</td><td>76.6</td><td>-4.5</td><td>2026/3/27</td></tr><tr><td>8227</td><td>SHIMAMURA CO</td><td>Retail Trade</td><td>19</td><td>750</td><td>81.1</td><td>02/2025</td><td>94.1</td><td>+13.0</td><td>2026/5/15</td></tr><tr><td>8359</td><td>HACHIJUNI NAGANO</td><td>Banks</td><td>19</td><td>1,151</td><td>81.4</td><td>03/2025</td><td></td><td></td><td>2026/6/26</td></tr><tr><td>1801</td><td>TAISEI CORP</td><td>Construction</td><td>103</td><td>2,209</td><td>81.7</td><td>03/2025</td><td></td><td></td><td>2026/6/23</td></tr><tr><td>4324</td><td>DENTSU GROUP INC</td><td>Services</td><td>31</td><td>830</td><td>81.9</td><td>12/2024</td><td>86.9</td><td>+5.1</td><td>2026/3/27</td></tr><tr><td>8411</td><td>MIZUHO FINL GP</td><td>Banks</td><td>460</td><td>18,600</td><td>82.0</td><td>03/2025</td><td></td><td></td><td>2026/6/26</td></tr></table>

Source: Company filings, FactSet, Data compiled by GS Global Investment Research

## Unequal Equities?

Exhibit 6: Y+D screen has outperformed NYND screen by 12ppt since June 3rd ...  
![](images/cb70a6a1a291c80483dd87c40822f6c7e753a59c2d911667c63c77730bbb6126.jpg)

<details>
<summary>line chart</summary>

| Date   | TOPIX | Y+D  | NYND |
|--------|-------|------|------|
| Jun-03 | 100   | 100  | 100  |
| Jun-06 | 99    | 101  | 97   |
| Jun-09 | 97    | 101  | 95   |
| Jun-12 | 97    | 102  | 89   |
</details>

Source: FactSet, GS Global Investment Research

Exhibit 7: ... and SMID Y+D has outperformed SMID NYND by 7ppts in the same period  
![](images/f93ce6bec6574756091b686927a9240297efe14bb3f9ea35569ee5b5ff23a349.jpg)

<details>
<summary>line chart</summary>

| Date   | TOPIX | SMID Y+D | SMID NYND |
|--------|-------|----------|-----------|
| Jun-03 | 100   | 100      | 100       |
| Jun-06 | 98    | 100      | 99        |
| Jun-09 | 97    | 100      | 97        |
| Jun-12 | 97    | 100      | 93        |
</details>

Source: FactSet, Data compiled by GS Global Investment Research

## Exhibit 8: Yuutai + Dividend Screen

Data as of May 1, 2026. Highlighted names indicate the SMID Y+D screen

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Company Name</td><td rowspan="2">GICS Sector</td><td rowspan="2">Quoted Price(JPY)</td><td colspan="2">SortedSize and Liquidity</td><td colspan="2">&gt;0Valuations</td></tr><tr><td>Mkt Cap(JPY bn)</td><td>6M ADTV(US$ mn)</td><td>FY1 P/E(x)</td><td>FY0 P/B(x)</td></tr><tr><td colspan="8">No yuutai + No dividend screen</td></tr><tr><td>9501</td><td>TOKYO ELEC POWER H</td><td>Utilities</td><td>613</td><td>984.6</td><td>337.9</td><td>-2.3</td><td>0.4</td></tr><tr><td>4324</td><td>DENTSU GROUP INC</td><td>Communication Services</td><td>2,967</td><td>788.6</td><td>30.9</td><td>9.5</td><td>2.1</td></tr><tr><td>4506</td><td>SUMITOMO PHARMA CO</td><td>Health Care</td><td>1,730</td><td>776.9</td><td>173.9</td><td>7.3</td><td>2.3</td></tr><tr><td>4385</td><td>MERCARI INC</td><td>Consumer Discretionary</td><td>3855.0</td><td>636.2</td><td>42.1</td><td>23.8</td><td>6.4</td></tr><tr><td>6753</td><td>SHARP CORP</td><td>Consumer Discretionary</td><td>582</td><td>378.8</td><td>14.1</td><td>6.7</td><td>1.4</td></tr><tr><td>4194</td><td>VISIONAL INC</td><td>Industrials</td><td>7,429</td><td>298.8</td><td>14.6</td><td>17.2</td><td>4.4</td></tr><tr><td>6366</td><td>CHIYODA CORP</td><td>Industrials</td><td>1,023</td><td>266.3</td><td>51.0</td><td>6.6</td><td>8.0</td></tr><tr><td>6670</td><td>MCJ CO LTD</td><td>Information Technology</td><td>2,183</td><td>222.2</td><td>9.0</td><td>14.4</td><td>2.0</td></tr><tr><td>6707</td><td>SANKEN ELECTRIC CO</td><td>Information Technology</td><td>9,663</td><td>202.2</td><td>6.5</td><td>-21.5</td><td>1.6</td></tr><tr><td>3697</td><td>SHIFT INC</td><td>Information Technology</td><td>649</td><td>173.7</td><td>39.7</td><td>14.5</td><td>4.2</td></tr><tr><td>2160</td><td>GNI GROUP LTD</td><td>Health Care</td><td>3,020</td><td>168.4</td><td>24.3</td><td>60.8</td><td>3.3</td></tr><tr><td>4443</td><td>SANSAN INC</td><td>Information Technology</td><td>1,250</td><td>158.5</td><td>13.3</td><td>27.8</td><td>10.6</td></tr><tr><td>4592</td><td>SANBIO COMPANY LTD</td><td>Health Care</td><td>1,970</td><td>153.7</td><td>17.7</td><td>-53.5</td><td>11.5</td></tr><tr><td>4587</td><td>PEPTIDREAM INC</td><td>Health Care</td><td>1,167</td><td>151.7</td><td>9.2</td><td>8.9</td><td>2.9</td></tr><tr><td>3103</td><td>UNITIKA LTD</td><td>Consumer Discretionary</td><td>2,382</td><td>137.6</td><td>112.8</td><td>6.9</td><td>4.1</td></tr><tr><td>4478</td><td>FREEE K K</td><td>Information Technology</td><td>2,274</td><td>135.7</td><td>10.2</td><td>113.1</td><td>6.9</td></tr><tr><td>3993</td><td>PKSHA TECHNOLOGY I</td><td>Information Technology</td><td>3,280</td><td>104.8</td><td>7.8</t

[中间内容因长度限制已省略]

attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
