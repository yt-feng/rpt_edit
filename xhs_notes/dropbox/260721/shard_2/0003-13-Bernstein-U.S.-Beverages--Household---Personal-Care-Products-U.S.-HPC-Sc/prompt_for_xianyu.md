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
# U.S. Beverages, Household & Personal Care Products

# U.S. HPC Scanner Update: beauty remains the bright spot as household demand stays soft

![](images/f173b77d664a6dbe68892d7e818a618ceb15993602ad26e1dfaa9df1131c726c.jpg)  
Cristian Rios  
+1 917 344 8615  
cristian.rios@bernsteinsg.com

![](images/46356bda241c92e10a9b77b91fd9c9269152c3327bab526740b6c7ea0a063113.jpg)

Yolanda Zhang

+1 917 344 8346

yolanda.zhang@bernsteinsg.com

U.S. HPC scanner trends remained mixed in the latest quarter. We publish our Q3 QTD scanner update, covering the period ending July 11, with comparisons against Q2 and Q1. Beauty continues to be the bright spot, while Household and Family Care categories remain relatively subdued.

Among our coverage names, P&G delivered +2.5% sales growth in Q3 QTD, down from +3.0% in Q2, reflecting moderating category growth and softer pricing. Beauty remained P&G's strongest segment (+6.4%), supported by +4.7% volume growth, while Fabric & Home Care grew +2.2% and Baby, Feminine & Family Care increased just +0.5%.

Colgate posted +3.5% sales growth in Q3 QTD, down from +4.0% in Q2, driven by improving volume trends, particularly in Home Care (+8.3%) and Pet Nutrition (+6.5%). Oral Care remained positive at +1.7%, while Personal Care declined 4.0%.

e.l.f. Beauty's total sales grew +1.0% in Q3 QTD, down from +1.2% in Q2, as weakness in Cosmetics (-6.3%) was offset by continued strength in Skin Care (+38.8%). For e.l.f., we used Nielsen's xAOC dataset rather than U.S. Full View to better reflect Naturium's underlying performance, as changes to Naturium's Amazon distribution strategy may distort trends in the U.S. Full View dataset. Even on this basis, Naturium remained the standout performer, generating +58.2% sales growth, driven by +88.1% volume growth. Notably, Nielsen captured e.l.f.'s Hair Care business for the first time this quarter. The category represented \~4% of company sales during the period and provides an incremental growth driver beyond Cosmetics and Skin Care, and it is not yet reflected in the Cosmetics/Skin Care segment tables below. We will incorporate Hair Care into future e.l.f. scanner updates.

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2"></td><td colspan="4">20 Jul 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td>Rating</td><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>ELF (elf)</td><td>M</td><td>USD</td><td>79.65</td><td>60.00</td><td>(50.5)%</td><td>USD</td><td>3.13</td><td>3.20</td><td>3.52</td><td>25.4</td><td>24.9</td><td>22.7</td></tr><tr><td>PG (Procter &amp; Gamble Co)</td><td>M</td><td>USD</td><td>149.13</td><td>156.00</td><td>(22.1)%</td><td>USD</td><td>6.83</td><td>6.86</td><td>7.12</td><td>21.8</td><td>21.7</td><td>20.9</td></tr><tr><td>CL (Colgate-Palmolive Co)</td><td>M</td><td>USD</td><td>91.93</td><td>96.00</td><td>(12.3)%</td><td>USD</td><td>3.68</td><td>3.87</td><td>4.09</td><td>25.0</td><td>23.8</td><td>22.5</td></tr><tr><td>SPX</td><td></td><td></td><td>7,443.28</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

ELF base year is 2026;

Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We rate e.l.f Beauty Market-Perform, with a PT of \$60. We believe e.l.f has the most relevant operating model for today's consumer -social media fluency, rapid innovation cycles, and a viral-prone approach to new product development. However, EPS have been extremely volatile after a big acquisition (Rhode), distribution expansion, increased marketing and payroll investments and a slowing-down core. We are long term believers, but think some stability and margin expansion is needed before the stock can appreciate.

We forecast 2% and 7% YoY EPS growth NTM and NTM+1, respectively, making us bearish vs. consensus on NTM+1 EPS by \~5%. We have a target multiple of 17x.

We rate Procter & Gamble Market-Perform, with a PT of \$156. P&G has a diversified portfolio (categories and regions) that is, by design, hard to accelerate or disrupt. Bright spots in Beauty (relative to the rest of the portfolio) will help sustain LSD organic sales growth, with potential upside from upcoming innovation in Laundry Detergents, but challenges from Private Label in more commoditized categories like Bathroom Tissue and from smaller competitors in Disposable Diapers are unlikely to go away.

We forecast 1% and 5% YoY EPS growth NTM and NTM+1, respectively, making us bearish vs. consensus on NTM+1 EPS by \~1%. We have a target multiple of 21.6x.

We rate Colgate-Palmolive Market-Perform, with a PT of \$96. Colgate has the most productive geographic footprint in our coverage, balancing diversification with growth and powered by strong HPC Brands in International markets. While HPC will be partially weighed down by their underperforming North America segment (stagnant categories, share loss), we like CL's Global Pet business, which will further premiumize as Cat Food, which has a higher price per pound, grows faster than Dog Food.

We forecast 4% and 9% YoY EPS growth NTM and NTM+1, respectively, making us bullish vs. consensus on NTM+1 EPS by \~2%. We have a target multiple of 23.1x.

## DETAILS

## EXHIBIT 1: 2026 Q3 QTD Performance - PG

Latest Period End: 2026-07-11

<table><tr><td></td><td>Sales ($M)</td><td>Volume (EQ, M)</td><td>Price ($/EQ)</td><td>YoY Sales Growth</td><td>YoY Volume Growth</td><td>YoY Price Growth</td><td>Sales Mix (%)</td><td>Market Share (%)</td><td>YoY Mkt Share Chg (pp)</td><td>Category Growth YoY</td></tr><tr><td>Fabric &amp; Home Care</td><td>1,386</td><td>7,416</td><td>0.19</td><td>2.2%</td><td>-1.0%</td><td>3.2%</td><td>35.3%</td><td>27.8%</td><td>0.7%</td><td>-0.5%</td></tr><tr><td>Baby, Feminine &amp; Family Care</td><td>1,151</td><td>5,116</td><td>0.23</td><td>0.5%</td><td>1.1%</td><td>-0.6%</td><td>29.3%</td><td>29.1%</td><td>-0.2%</td><td>1.1%</td></tr><tr><td>Grooming</td><td>192</td><td>79</td><td>2.42</td><td>3.9%</td><td>1.2%</td><td>2.8%</td><td>4.9%</td><td>38.1%</td><td>0.5%</td><td>2.5%</td></tr><tr><td>Health Care</td><td>525</td><td>1,175</td><td>0.45</td><td>2.0%</td><td>4.1%</td><td>-2.0%</td><td>13.4%</td><td>9.8%</td><td>0.0%</td><td>2.0%</td></tr><tr><td>Beauty</td><td>633</td><td>942</td><td>0.67</td><td>6.4%</td><td>4.7%</td><td>1.7%</td><td>16.1%</td><td>8.9%</td><td>0.3%</td><td>3.4%</td></tr><tr><td>Other</td><td>39</td><td>12</td><td>3.24</td><td>10.9%</td><td>-3.6%</td><td>15.0%</td><td>1.0%</td><td>0.1%</td><td>0.0%</td><td>2.5%</td></tr><tr><td>Total</td><td>3,926</td><td>14,739</td><td>0.27</td><td>2.5%</td><td>0.5%</td><td>2.0%</td><td>100.0%</td><td>5.0%</td><td>0.0%</td><td>2.3%</td></tr></table>

Source: Nielsen Total US Full View (Modeled) + Conv + Pet Retail + Costco (Model) + Rem Accounts, Bernstein Analysis

## EXHIBIT 2: 2026 Q2 Performance - PG

Latest Period End: 2026-06-27

<table><tr><td></td><td>Sales ($M)</td><td>Volume (EQ, M)</td><td>Price ($/EQ)</td><td>YoY Sales Growth</td><td>YoY Volume Growth</td><td>YoY Price Growth</td><td>Sales Mix (%)</td><td>Market Share (%)</td><td>YoY Mkt Share Chg (pp)</td><td>Category Growth YoY</td></tr><tr><td>Fabric &amp; Home Care</td><td>4,859</td><td>26,877</td><td>0.18</td><td>1.5%</td><td>-0.4%</td><td>1.9%</td><td>35.4%</td><td>29.1%</td><td>-0.4%</td><td>2.7%</td></tr><tr><td>Baby, Feminine &amp; Family Care</td><td>3,992</td><td>18,606</td><td>0.21</td><td>1.6%</td><td>-0.4%</td><td>2.0%</td><td>29.1%</td><td>28.9%</td><td>-0.1%</td><td>2.1%</td></tr><tr><td>Grooming</td><td>631</td><td>271</td><td>2.33</td><td>5.0%</td><td>1.8%</td><td>3.1%</td><td>4.6%</td><td>38.7%</td><td>0.2%</td><td>4.5%</td></tr><tr><td>Health Care</td><td>1,961</td><td>4,349</td><td>0.45</td><td>5.2%</td><td>-0.6%</td><td>5.9%</td><td>14.3%</td><td>10.2%</td><td>0.2%</td><td>3.2%</td></tr><tr><td>Beauty</td><td>2,188</td><td>3,283</td><td>0.67</td><td>5.8%</td><td>1.0%</td><td>4.7%</td><td>15.9%</td><td>9.3%</td><td>0.0%</td><td>6.1%</td></tr><tr><td>Other</td><td>97</td><td>31</td><td>3.11</td><td>16.8%</td><td>6.5%</td><td>9.7%</td><td>0.7%</td><td>0.0%</td><td>0.0%</td><td>2.7%</td></tr><tr><td>Total</td><td>13,728</td><td>53,418</td><td>0.26</td><td>3.0%</td><td>-0.3%</td><td>3.3%</td><td>100.0%</td><td>5.1%</td><td>0.0%</td><td>3.0%</td></tr></table>

Source: Nielsen Total US Full View (Modeled) + Conv + Pet Retail + Costco (Model) + Rem Accounts, Bernstein Analysis

## EXHIBIT 3: 2026 Q1 Performance - PG

Latest Period End: 2026-03-21

<table><tr><td></td><td>Sales ($M)</td><td>Volume (EQ, M)</td><td>Price ($/EQ)</td><td>YoY Sales Growth</td><td>YoY Volume Growth</td><td>YoY Price Growth</td><td>Sales Mix (%)</td><td>Market Share (%)</td><td>YoY Mkt Share Chg (pp)</td><td>Category Growth YoY</td></tr><tr><td>Fabric &amp; Home Care</td><td>4,290</td><td>24,415</td><td>0.18</td><td>2.4%</td><td>1.6%</td><td>0.8%</td><td>35.8%</td><td>30.6%</td><td>-0.2%</td><td>3.2%</td></tr><tr><td>Baby, Feminine &amp; Family Care</td><td>3,501</td><td>17,991</td><td>0.19</td><td>1.4%</td><td>-0.4%</td><td>1.8%</td><td>29.2%</td><td>29.0%</td><td>-0.4%</td><td>2.9%</td></tr><tr><td>Grooming</td><td>479</td><td>208</td><td>2.30</td><td>-1.1%</td><td>-6.1%</td><td>5.3%</td><td>4.0%</td><td>37.8%</td><td>-1.4%</td><td>2.7%</td></tr><tr><td>Health Care</td><td>1,944</td><td>4,139</td><td>0.47</td><td>2.5%</td><td>-2.5%</td><td>5.1%</td><td>16.2%</td><td>11.1%</td><td>0.1%</td><td>1.7%</td></tr><tr><td>Beauty</td><td>1,745</td><td>2,662</td><td>0.66</td><td>6.5%</td><td>0.7%</td><td>5.7%</td><td>14.6%</td><td>9.4%</td><td>-0.1%</td><td>7.4%</td></tr><tr><td>Other</td><td>18</td><td>8</td><td>2.37</td><td>36.3%</td><td>15.3%</td><td>18.2%</td><td>0.2%</td><td>0.0%</td><td>0.0%</td><td>4.4%</td></tr><tr><td>Total</td><td>11,978</td><td>49,422</td><td>0.24</td><td>2.6%</td><td>0.4%</td><td>2.1%</td><td>100.0%</td><td>5.2%</td><td>-0.1%</td><td>4.3%</td></tr></table>

Source: Nielsen Total US Full View (Modeled) + Conv + Pet Retail + Costco (Model) + Rem Accounts, Bernstein Analysis

EXHIBIT 4: PG Overall Performance Trends  
![](images/f11d1c8a42bbf81ea4d104014903e9816805919aa0ec50b28368b941760a70e2.jpg)  
Source: Nielsen Total US Full View (Modeled) + Conv + Pet Retail + Costco (Model) + Rem Accounts, Bernstein Analysis

## EXHIBIT 5: PG Performance Trends by Segment

PG - Fabric & Home Care YoY Growth Rolling 12 Weeks (3 Months)  
![](images/468044389a0dafa19161ebc5c9fe3193bd884825f3125dd79ec2b7c54f6dd759.jpg)

PG - Baby, Feminine & Family Care YoY Growth Rolling 12 Weeks (3 Months)  
![](images/dd746a46cf22bae281136a3fa0b782480f3da2708b5e75cbe1b92ad2d6270d15.jpg)

PG - Grooming YoY Growth
Rolling 12 Weeks (3 Months)  
![](images/cee75d60dd36bec47d5a625d049a434e9019728c34b91f01e709a797f259d052.jpg)

![](images/fbe55b1c5bf6ec05d2457032ffcb3fcd64b040042056ad0f5bce9ab3924a6733.jpg)

PG - BeautyYoY Growth
Rolling 12 Weeks (3 Months)  
![](images/2142aab9f28cf7171aa036e906115db461b31b4a9407b7a1087e8c7081c6a7f4.jpg)

## EXHIBIT 6: 2026 Q3 QTD Performance - CL

Latest Period End: 2026-07-11

<table><tr><td></td><td>Sales ($M)</td><td>Volume (EQ, M)</td><td>Price ($/EQ)</td><td>YoY Sales Growth</td><td>YoY Volume Growth</td><td>YoY Price Growth</td><td>Sales Mix (%)</td><td>Market Share (%)</td><td>YoY Mkt Share Chg (pp)</td><td>Category Growth YoY</td></tr><tr><td>Oral Care</td><td>187</td><td>247</td><td>0.76</td><td>1.7%</td><td>-2.4%</td><td>4.2%</td><td>19.2%</td><td>17.8%</td><td>0.1%</td><td>0.8%</td></tr><tr><td>Personal Care</td><td>90</td><td>352</td><td>0.26</td><td>-4.0%</td><td>-8.9%</td><td>5.3%</td><td>9.2%</td><td>2.2%</td><td>-0.2%</td><td>4.5%</td></tr><tr><td>Home Care</td><td>104</td><td>1,332</td><td>0.08</td><td>8.3%</td><td>10.1%</td><td>-1.7%</td><td>10.6%</td><td>3.8%</td><td>0.2%</td><td>1.9%</td></tr><tr><td>Oral, Personal, and Household Care</td><td>381</td><td>1,930</td><td>0.20</td><td>1.9%</td><td>4.4%</td><td>-2.4%</td><td>39.0%</td><td>4.9%</td><td>-0.1%</td><td>3.1%</td></tr><tr><td>Pet</td><td>214</td><td>54</td><td>3.97</td><td>6.5%</td><td>-0.5%</td><td>7.0%</td><td>21.9%</td><td>5.1%</td><td>0.1%</td><td>3.3%</td></tr><tr><td>Total</td><td>595</td><td>1,984</td><td>0.30</td><td>3.5%</td><td>4.3%</td><td>-0.7%</td><td>61.0%</td><td>0.8%</td><td>0.0%</td><td>2.3%</td></tr></table>

Source: Nielsen Total US Full View (Modeled) + Conv + Pet Retail + Costco (Model) + Rem Accounts, Bernstein Analysis

## EXHIBIT 7: 2026 Q2 Performance - CL

Latest Period End: 2026-06-27

<table><tr><td></td><td>Sales ($M)</td><td>Volume (EQ, M)</td><td>Price ($/EQ)</td><td>YoY Sales Growth</td><td>YoY Volume Growth</td><td>YoY Price Growth</td><td>Sales Mix (%)</td><td>Market Share (%)</td><td>YoY Mkt Share Chg (pp)</td><td>Category Growth YoY</td></tr><tr><td>Oral Care</td><td>608</td><td>790</td><td>0.77</td><td>2.1%</td><td>-1.4%</td><td>3.6%</td><td>18.8%</td><td>16.8%</td><td>-0.4%</td><td>4.8%</td></tr><tr><td>Personal Care</td><td>295</td><td>1,174</td><td>0.25</td><td>2.2%</td><td>-4.6%</td><td>7.1%</td><td>9.1%</td><td>2.2%</td><td>-0.1%</td><td>8.2%</td></tr><tr><td>Home Care</td><td>338</td><td>4,143</td><td>0.08</td><td>2.8%</td><td>-0.6%</td><td>3.4%</td><td>10.5%</td><td>3.6%</td><td>0.0%</td><td>2.6%</td></tr><tr><td>Oral, Personal, and Household Care</td><td>1,242</td><td>6,108</td><td>0.20</td><td>2.3%</td><td>-1.5%</td><td>3.9%</td><td>38.5%</td><td>4.7%</td><td>-0.2%</td><td>5.7%</td></tr><tr><td>Pet</td><td>745</td><td>189</td><td>3.94</td><td>7.0%</td><td>0.3%</td><td>6.7%</td><td>23.1%</td><td>5.1%</td><td>0.2%</td><td>3.6%</td></tr><tr><td>Total</td><td>1,987</td><td>6,297</td><td>0.32</td><td>4.0%</td><td>-1.4%</td><td>5.5%</td><td>61.5%</td><td>0.7%</td><td>0.0%</td><td>3.0%</td></tr></table>

Source: Nielsen Total US Full View (Modeled) + Conv + Pet Retail + Costco (Model) + Rem Accounts, Bernstein Analysis

## EXHIBIT 8: 2026 Q1 Performance - CL

Latest Period End: 2026-03-21

<table><tr><td></td><td>Sales ($M)</td><td>Volume (EQ, M)</td><td>Price ($/EQ)</td><td>YoY Sales Growth</td><td>YoY Volume Growth</td><td>YoY Price Growth</td><td>Sales Mix (%)</td><td>Market Share (%)</td><td>YoY Mkt Share Chg (pp)</td><td>Category Growth YoY</td></tr><tr><td>Oral Care</td><td>516</td><td>697</td><td>0.74</td><td>-1.6%</td><td>-3.5%</td><td>1.9%</td><td>18.9%</td><td>16.5%</td><td>-1.0%</td><td>4.1%</td></tr><tr><td>Personal Care</td><td>232</td><td>1,130</td><td>0.21</td><td>2.0%</td><td>2.2%</td><td>-0.2%</td><td>8.5%</td><td>2.2%</td><td>-0.2%</td><td>9.2%</td></tr><tr><td>Home Care</td><td>293</td><td>3,623</td><td>0.08</td><td>-0.8%</td><td>-4.2%</td><td>3.5%</td><td>10.7%</td><td>3.6%</td><td>-0.1%</td><td>3.0%</td></tr><tr><td>Oral, Personal, and Household Care</td><td>1,041</td><td>5,450</td><td>0.19</td><td>-0.6%</td><td>-2.8%</td><td>2.3%</td><td>38.2%</td><td>4.7%</td><td>-0.3%</td><td>6.1%</td></tr><tr><td>Pet</td><td>642</td><td>167</td><td>3.84</td><td>6.9%</td><td>0.5%</td><td>6.4%</td><td>23.6%</td><td>5.0%</td><td>0.1%</td><td>4.0%</td></tr><tr><td>Total</td><td>1,683</td><td>5,617</td><td>0.30</td><td>2.1%</td><td>-2.7%</td><td>5.0%</td><td>61.8%</td><td>0.7%</td><td>0.0%</td><td>4.3%</td></tr></table>

Source: Nielsen Total US Full View (Modeled) + Conv + Pet Retail + Costco (Model) + Rem Accounts, Bernstein Analysis

EXHIBIT 9: CL Overall Performance Trends  
![](images/3dbc2187ee6bfe42cca066f6c8ffbf880970dddb508008c0382299b4a5cb2e96.jpg)  
Source: Nielsen Total US Full View (Modeled) + Conv + Pet Retail + Costco (Model) + Rem Accounts, B

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
