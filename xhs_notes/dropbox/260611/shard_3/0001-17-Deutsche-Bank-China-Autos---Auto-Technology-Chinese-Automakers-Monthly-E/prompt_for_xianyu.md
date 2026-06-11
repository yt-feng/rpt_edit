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
Asia
Emerging Europe
Europe

Consumer
Autos & Auto Technology

# Industry China Autos & Auto Technology

Date
9 June 2026

Industry Update

# Chinese Automakers Monthly European Market Volume Monitor: Apr. 2026

This monthly chartbook product - "Chinese Automakers Monthly European Market Volume Monitor" - tracks the European sales of leading Chinese automakers.

We anticipate overseas volumes to become the key growth driver, with the European market representing a significant growth market for Chinese automakers.

Bin Wang
Research Analyst
+852-220-35496

Wei Huang
Research Associate
+852-2203-7057

Figure 1: Chinese OEMs European market volume by country

<table><tr><td colspan="6">Chinese OEM European Volume by Country</td></tr><tr><td>(unit)</td><td>Apr-26</td><td>YoY</td><td>MoM</td><td>4M 2026</td><td>YoY</td></tr><tr><td>CN OEMs Sales</td><td>163,288</td><td>41.7%</td><td>-13.9%</td><td>573,291</td><td>40.4%</td></tr><tr><td>Russia</td><td>53,337</td><td>-9.7%</td><td>13.6%</td><td>170,640</td><td>-13.8%</td></tr><tr><td>UK</td><td>24,656</td><td>192.8%</td><td>-57.2%</td><td>111,830</td><td>127.7%</td></tr><tr><td>Italy</td><td>19,952</td><td>130.4%</td><td>-6.4%</td><td>71,837</td><td>129.5%</td></tr><tr><td>Spain</td><td>15,400</td><td>91.4%</td><td>-8.2%</td><td>54,073</td><td>72.2%</td></tr><tr><td>Germany</td><td>9,819</td><td>144.3%</td><td>20.8%</td><td>29,906</td><td>139.0%</td></tr><tr><td>France</td><td>7,744</td><td>71.4%</td><td>40.7%</td><td>20,089</td><td>46.5%</td></tr><tr><td>Poland</td><td>6,602</td><td>107.7%</td><td>-11.5%</td><td>23,566</td><td>129.8%</td></tr><tr><td>Turkiye</td><td>4,321</td><td>-54.3%</td><td>1.7%</td><td>19,546</td><td>-26.5%</td></tr><tr><td>Austria</td><td>2,381</td><td>133.2%</td><td>-7.4%</td><td>7,544</td><td>101.8%</td></tr><tr><td>Belgium</td><td>2,256</td><td>122.0%</td><td>-11.1%</td><td>7,956</td><td>118.9%</td></tr><tr><td>Portugal</td><td>1,764</td><td>126.7%</td><td>-23.7%</td><td>7,318</td><td>131.9%</td></tr><tr><td>Netherlands</td><td>1,662</td><td>56.9%</td><td>-22.8%</td><td>7,042</td><td>101.9%</td></tr><tr><td>Denmark</td><td>1,605</td><td>57.5%</td><td>13.2%</td><td>5,124</td><td>77.6%</td></tr><tr><td>Norway</td><td>1,591</td><td>27.0%</td><td>-22.7%</td><td>5,110</td><td>26.2%</td></tr><tr><td>Romania</td><td>1,294</td><td>372.3%</td><td>23.8%</td><td>3,955</td><td>218.7%</td></tr><tr><td>Czech Republic</td><td>1,255</td><td>127.8%</td><td>14.2%</td><td>3,730</td><td>92.1%</td></tr><tr><td>Switzerland</td><td>1,220</td><td>260.9%</td><td>-5.6%</td><td>3,813</td><td>240.8%</td></tr><tr><td>Greece</td><td>1,212</td><td>53.6%</td><td>-11.6%</td><td>4,482</td><td>64.2%</td></tr><tr><td>Sweden</td><td>1,100</td><td>142.8%</td><td>61.5%</td><td>2,490</td><td>59.9%</td></tr><tr><td>Hungary</td><td>1,010</td><td>260.7%</td><td>129.5%</td><td>1,930</td><td>71.4%</td></tr></table>

Figure 2: Chinese OEMs European market volume by automaker

<table><tr><td colspan="6">Chinese OEM European Market Volume by OEM</td></tr><tr><td>(unit)</td><td>Apr-26</td><td>YoY</td><td>MoM</td><td>4M 2026</td><td>YoY</td></tr><tr><td>CN OEMs Sales</td><td>163,288</td><td>41.7%</td><td>-13.9%</td><td>573,291</td><td>40.4%</td></tr><tr><td>Chery</td><td>40,841</td><td>29.0%</td><td>-18.7%</td><td>146,687</td><td>40.6%</td></tr><tr><td>SAIC</td><td>29,839</td><td>35.7%</td><td>-25.1%</td><td>110,875</td><td>9.8%</td></tr><tr><td>BYD</td><td>28,358</td><td>57.0%</td><td>-26.1%</td><td>107,637</td><td>94.3%</td></tr><tr><td>Geely</td><td>18,234</td><td>46.8%</td><td>5.9%</td><td>59,345</td><td>49.3%</td></tr><tr><td>Great Wall Motor</td><td>18,148</td><td>21.9%</td><td>10.5%</td><td>58,007</td><td>11.9%</td></tr><tr><td>Leapmotor</td><td>8,758</td><td>415.8%</td><td>-22.0%</td><td>32,747</td><td>590.0%</td></tr><tr><td>Chang&#x27;an</td><td>5,491</td><td>19.8%</td><td>24.3%</td><td>15,065</td><td>-14.7%</td></tr><tr><td>XPeng</td><td>3,344</td><td>102.7%</td><td>8.1%</td><td>10,433</td><td>107.3%</td></tr><tr><td>Dongfeng Motor</td><td>2,793</td><td>120.8%</td><td>18.1%</td><td>8,512</td><td>61.7%</td></tr><tr><td>FAW</td><td>2,148</td><td>208.2%</td><td>6.5%</td><td>7,039</td><td>187.1%</td></tr><tr><td>GAC</td><td>2,139</td><td>62.3%</td><td>18.8%</td><td>6,272</td><td>34.3%</td></tr><tr><td>Chinese Brands</td><td>1,010</td><td></td><td>129.5%</td><td>1,930</td><td></td></tr><tr><td>BAIC</td><td>597</td><td>-52.5%</td><td>-30.7%</td><td>2,535</td><td>-34.2%</td></tr><tr><td>Li Auto</td><td>348</td><td>-64.7%</td><td>-5.2%</td><td>1,757</td><td>-46.9%</td></tr><tr><td>Seres</td><td>288</td><td>-50.8%</td><td>17.6%</td><td>994</td><td>-49.6%</td></tr><tr><td>Fujian Motor (FJMG)</td><td>263</td><td>17.4%</td><td>338.3%</td><td>399</td><td>-47.4%</td></tr><tr><td>JAC</td><td>259</td><td>-47.3%</td><td>-19.6%</td><td>1,174</td><td>-25.8%</td></tr><tr><td>Shineray</td><td>189</td><td>-71.0%</td><td>-23.2%</td><td>945</td><td>-64.8%</td></tr><tr><td>NIO</td><td>46</td><td>-14.8%</td><td>-14.8%</td><td>210</td><td>-23.9%</td></tr><tr><td>212</td><td>38</td><td></td><td>153.3%</td><td>53</td><td></td></tr></table>

## By Country

Figure 3: European market total volume trend  
![](images/48e9bdad4a5d5b2f82e24f70c193e6ca4286da38624ed24d6a8813c3b99e9049.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Month   | European Auto Sales | YoY    |
|---------|---------------------|--------|
| Jan-25  | 1150                | 6%     |
| Feb-25  | 1100                | -4%    |
| Mar-25  | 1600                | 0%     |
| Apr-25  | 1250                | 0%     |
| May-25  | 1300                | 2%     |
| Jun-25  | 1400                | -8%    |
| Jul-25  | 1250                | 4%     |
| Aug-25  | 1000                | 2%     |
| Sep-25  | 1450                | 8%     |
| Oct-25  | 1350                | 4%     |
| Nov-25  | 1300                | 2%     |
| Dec-25  | 1450                | 8%     |
| Jan-26  | 1100                | -4%    |
| Feb-26  | 1150                | 0%     |
| Mar-26  | 1750                | 10%    |
| Apr-26  | 1350                | 6%     |
</details>

Source : Marklines

Figure 4: Total European market volume breakdown by OEM  
![](images/48ac1b6d15279214c7465c046dad55f13f4f0841aa6cb30a49880242be799954.jpg)

<details>
<summary>pie chart</summary>

| Category | Percentage (%) |
| :--- | :--- |
| Non-Chinese OEM | 88 |
| Chinese OEM | 12 |
</details>

Source : Marklines

Figure 5: Chinese OEMs' aggregate European market volume trend  
![](images/b7f2a2e32d8bd0a83ca72102a69fcab69357a64390de0524eb02014b7611264d.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Month   | CN OEMs Sales | YoY   |
|---------|---------------|-------|
| Jan-25  | 88            | 18%   |
| Feb-25  | 84            | -5%   |
| Mar-25  | 118           | -10%  |
| Apr-25  | 114           | 6%    |
| May-25  | 118           | 6%    |
| Jun-25  | 123           | -5%   |
| Jul-25  | 134           | 6%    |
| Aug-25  | 120           | 5%    |
| Sep-25  | 163           | 20%   |
| Oct-25  | 163           | 10%   |
| Nov-25  | 147           | 40%   |
| Dec-25  | 177           | 45%   |
| Jan-26  | 107           | 20%   |
| Feb-26  | 113           | 35%   |
| Mar-26  | 190           | 60%   |
| Apr-26  | 163           | 40%   |
</details>

Source : Marklines

Figure 6: Aggregate market share of Chinese OEMs in European market  
![](images/594ebcb69b6771509414449ec98766b4514d61e22eb374b2e138dec00d270036.jpg)

<details>
<summary>line chart</summary>

| Month   | Value  |
| ------- | ------ |
| Jan-25  | 7.8%   |
| Feb-25  | 7.5%   |
| Mar-25  | 7.3%   |
| Apr-25  | 9.0%   |
| May-25  | 9.0%   |
| Jun-25  | 8.5%   |
| Jul-25  | 10.5%  |
| Aug-25  | 12.0%  |
| Sep-25  | 11.0%  |
| Oct-25  | 12.0%  |
| Nov-25  | 11.0%  |
| Dec-25  | 12.0%  |
| Jan-26  | 9.8%   |
| Feb-26  | 10.0%  |
| Mar-26  | 10.8%  |
| Apr-26  | 12.0%  |
</details>

Source : Marklines

Figure 7: Germany market wide volume trend  
![](images/eafcc68c685d2322b51fc67997db2eb9e08e72902b041b46da5fb1cedfa30802.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Month | Germany total sales (000 Unit) | YoY (%) |
| :--- | :--- | :--- |
| Jan-25 | 208 | -1.3 |
| Feb-25 | 204 | -5.7 |
| Mar-25 | 253 | -4.9 |
| Apr-25 | 242 | -1.1 |
| May-25 | 238 | 0.9 |
| Jun-25 | 256 | -16.4 |
| Jul-25 | 264 | 11.6 |
| Aug-25 | 208 | 4.7 |
| Sep-25 | 236 | 13.0 |
| Oct-25 | 249 | 6.8 |
| Nov-25 | 251 | 1.7 |
| Dec-25 | 246 | 6.0 |
| Jan-26 | 193 | -7.3 |
| Feb-26 | 211 | 7.9 |
| Mar-26 | 258 | 16.4 |
| Apr-26 | 249 | 1.8 |
</details>

Source : Marklines

Figure 8: Germany market wide volume breakdown by automaker  
![](images/28800e8747146cb972477a384d0f2b87812158b5e6b4f1eda75c4ad8dd6604d8.jpg)

<details>
<summary>pie chart</summary>

| Category | Percentage (%) |
| :--- | :--- |
| Non-Chinese OEMs | 96.8 |
| BYD | 1.5 |
| SAIC | 0.9 |
| Other CN OEMs | 0.7 |
</details>

Source : Marklines

Figure 9: Chinese OEMs' aggregate volume trend in Germany  
![](images/9b4da64a843257708f0bd67a7a9e25b1e86e4304e7aa1cbadd50c8947dc31e52.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Month   | CN OEMs Sales in Germany (000 Unit) | YoY (%) |
|---------|-------------------------------------|---------|
| Jan-25  | 2.5                                 | 150     |
| Feb-25  | 2.3                                 | 50      |
| Mar-25  | 3.5                                 | 150     |
| Apr-25  | 4.0                                 | 250     |
| May-25  | 5.0                                 | 100     |
| Jun-25  | 6.0                                 | 0       |
| Jul-25  | 4.5                                 | 150     |
| Aug-25  | 4.5                                 | 300     |
| Sep-25  | 7.2                                 | 500     |
| Oct-25  | 7.5                                 | 250     |
| Nov-25  | 8.0                                 | 350     |
| Dec-25  | 8.5                                 | 200     |
| Jan-26  | 5.2                                 | 100     |
| Feb-26  | 6.8                                 | 180     |
| Mar-26  | 8.1                                 | 120     |
| Apr-26  | 9.8                                 | 130     |
</details>

Source : Marklines

Figure 10: Aggregate market share of Chinese OEMs in Germany  
![](images/affe0628d0a73ad1667424a2abc392d0c91ed1e772e67bd6b217455eecaeb678.jpg)

<details>
<summary>line chart</summary>

| Month   | Value |
| ------- | ----- |
| Jan-25  | 1.2%  |
| Feb-25  | 1.2%  |
| Mar-25  | 1.4%  |
| Apr-25  | 1.7%  |
| May-25  | 2.1%  |
| Jun-25  | 2.3%  |
| Jul-25  | 1.6%  |
| Aug-25  | 2.1%  |
| Sep-25  | 3.0%  |
| Oct-25  | 3.0%  |
| Nov-25  | 3.2%  |
| Dec-25  | 3.4%  |
| Jan-26  | 2.7%  |
| Feb-26  | 3.2%  |
| Mar-26  | 2.8%  |
| Apr-26  | 4.0%  |
</details>

Source : Marklines

Figure 11: France market wide volume trend  
![](images/90567d87360ac5af0b8f697ccff362bdd583a6567ddc3374355ece0d28732ac2.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Month | France total sales (000 Unit) | YoY (%) |
| :--- | :--- | :--- |
| Jan-25 | 114 | -7.5 |
| Feb-25 | 141 | 1.3 |
| Mar-25 | 154 | -14.8 |
| Apr-25 | 139 | 8.0 |
| May-25 | 124 | -13.0 |
| Jun-25 | 170 | -7.5 |
| Jul-25 | 116 | -7.8 |
| Aug-25 | 88 | 2.8 |
| Sep-25 | 141 | 1.6 |
| Oct-25 | 140 | 3.3 |
| Nov-25 | 133 | 1.0 |
| Dec-25 | 173 | -8.0 |
| Jan-26 | 107 | -7.8 |
| Feb-26 | 120 | -14.8 |
| Mar-26 | 176 | 14.0 |
| Apr-26 | 137 | -0.8 |
</details>

Source : Marklines

Figure 12: France market wide volume breakdown by automaker  
![](images/ff81286a6994f2a6904b9da98684806bbd0666efd8571b6d1915fe77a9d2399f.jpg)

<details>
<summary>pie chart</summary>

| Category | Percentage (%) |
| :--- | :--- |
| Non-Chinese OEMs | 96.3 |
| SAIC | 1.7 |
| BYD | 1.1 |
| Other CN OEMs | 0.9 |
</details>

Source : Marklines

Figure 13: Chinese OEMs' aggregate volume trend in France  
![](images/c009210b37e7e045e24a3c7c583491d096d20523062c0eb61792e6421158ed13.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Month   | CN OEMs Sales in France | YoY   |
|---------|--------------------------|-------|
| Jan-25  | 2                        | 0%    |
| Feb-25  | 3                        | 0%    |
| Mar-25  | 4                        | 100%  |
| Apr-25  | 4.5                      | 300%  |
| May-25  | 4                        | 250%  |
| Jun-25  | 4.5                      | 100%  |
| Jul-25  | 3.5                      | 150%  |
| Aug-25  | 3                        | 175%  |
| Sep-25  | 5                        | 150%  |
| Oct-25  | 5                        | 125%  |
| Nov-25  | 4.5                      | 100%  |
| Dec-25  | 10.5                     | 0%    |
| Jan-26  | 3                        | 0%    |
| Feb-26  | 4                        | 0%    |
| Mar-26  | 5.5                      | 0%    |
| Apr-26  | 7.5                      | 75%   |
</details>

Source : Marklines

Figure 14: Aggregate market share of Chinese OEMs in France  
![](images/bc25537a10f1e03942e9b6ed70e41f0d7558f43ff394da1c68d2dd628a37522b.jpg)

<details>
<summary>line chart</summary>

| Month   | Value |
| ------- | ----- |
| Jan-25  | 2.0%  |
| Feb-25  | 2.1%  |
| Mar-25  | 2.8%  |
| Apr-25  | 3.3%  |
| May-25  | 3.4%  |
| Jun-25  | 2.6%  |
| Jul-25  | 3.5%  |
| Aug-25  | 3.9%  |
| Sep-25  | 4.0%  |
| Oct-25  | 3.8%  |
| Nov-25  | 3.7%  |
| Dec-25  | 6.2%  |
| Jan-26  | 2.7%  |
| Feb-26  | 3.3%  |
| Mar-26  | 3.1%  |
| Apr-26  | 5.7%  |
</details>

Source : Marklines

Figure 15: UK market wide volume trend  
![](images/241e0ba0a32378d2c61a6da8885af88155813a3a66d604cbc98c56e4abab7763.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Month | UK total sales (000 Unit) | YoY (%) |
|---|---|---|
| Jan-25 | 140 | -1.5 |
| Feb-25 | 85 | -1.0 |
| Mar-25 | 360 | 12.5 |
| Apr-25 | 120 | -10.0 |
| May-25 | 150 | 1.5 |
| Jun-25 | 195 | 7.5 |
| Jul-25 | 140 | -3.0 |
| Aug-25 | 85 | -1.0 |
| Sep-25 | 315 | 14.5 |
| Oct-25 | 145 | 1.0 |
| Nov-25 | 150 | -1.5 |
| Dec-25 | 145 | 3.5 |
| Jan-26 | 145 | 3.5 |
| Feb-26 | 90 | 7.5 |
| Mar-26 | 380 | 7.0 |
| Apr-26 | 150 | 25.0 |
</details>

Source : Marklines

Figure 16: UK market wide volume breakdown by automaker  
![](images/9cd4fbeb2cd09c85534851be79e8e562bad1efab8ef617971af63678a2443b88.jpg)

<details>
<summary>pie chart</summary>

| Category | Percentage (%) |
| :--- | :--- |
| Non-Chinese OEMs | 85.4 |
| Chery | 6.0 |
| SAIC | 4.0 |
| BYD | 3.5 |
| Other CN OEMs | 1.1 |
</details>

Source : Marklines

Figure 17: Chinese OEMs' aggregate volume trend in the UK  
![](images/bc446e0dc6c6e72bdbb3ea17472362668133dfa25298901dbf93128093e0b7ab.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Month | CN OEMs Sales in UK (000 Unit) | YoY (%) |
| :--- | :--- | :--- |
| Jan-25 | 8 | 30 |
| Feb-25 | 5 | 70 |
| Mar-25 | 26 | 100 |
| Apr-25 | 8 | 40 |
| May-25 | 13 | 60 |
| Jun-25 | 16 | 70 |
| Jul-25 | 13 | 80 |
| Aug-25 | 7 | 100 |
| Sep-25 | 39 | 250 |
| Oct-25 | 15 | 100 |
| Nov-25 | 18 | 70 |
| Dec-25 | 26 | 180 |
| Jan-26 | 19 | 100 |
| Feb-26 | 11 | 60 |
| Mar-26 | 58 | 120 |
| Apr-26 | 24 | 180 |
</details>

Source : Marklines

Figure 18: Aggregate market share of Chinese OEMs in UK  
![](images/7452aae9d9aa2cb7e1be5531dafc231cf30afd521963419e9ebdcd92ab6e1c30.jpg)

<details>
<summary>line chart</summary>

| Month   | Value  |
| ------- | ------ |
| Jan-25  | 6.0%   |
| Feb-25  | 7.0%   |
| Mar-25  | 7.5%   |
| Apr-25  | 7.0%   |
| May-25  | 8.5%   |
| Jun-25  | 8.0%   |
| Jul-25  | 9.0%   |
| Aug-25  | 8.5%   |
| Sep-25  | 12.0%  |
| Oct-25  | 10.0%  |
| Nov-25  | 11.5%  |
| Dec-25  | 18.0%  |
| Jan-26  | 13.0%  |
| Feb-26  | 11.5%  |
| Mar-26  | 15.0%  |
| Apr-26  | 17.0%  |
</details>

Source : Marklines

Figure 19: Italy market wide volume trend  
![](images/a7e41e7d08fe6baf817fbd3c60fee3f9f83e1b578a67fa3d54a0e5313494c3ae.jpg)

<deta

[中间内容因长度限制已省略]

s. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG. It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG

## David Folkerts-Landau

Group Chief Economist and Global Head of Research

Pam Finelli
Global Chief Operating Officer
Research

Steve Pollard
Global Head of Company
Research and Sales

Jim Reid
Global Head of
Macro and Thematic Research

Tim Rokossa
Head of Germany
Research

Gerry Gallagher
Head of European
Company Research

Matthew Barnard
Head of Americas
Company Research

Peter Milliken
Head of APAC
Company Research

Debbie Jones
Global Head of Sustainability
and Data Innovation, Research

Sameer Goel
Global Head of EM & APAC
Research

Francis Yared
Global Head of Rates Research

George Saravelos
Global Head of FX Research

Peter Hooper
Vice-Chair of Research

International Production Locations

<table><tr><td>DB AG</td><td>DB AG</td><td>DB AG</td><td>Deutsche Securities Inc.</td></tr><tr><td>DB Place</td><td>Equity Research</td><td>Filiale Hongkong</td><td>1-3-1 Azabudai</td></tr><tr><td>Level 16</td><td>Mainzer Landstrasse 11-17</td><td>International Commerce</td><td>Azabudai Hills Mori JP Tower</td></tr><tr><td>Corner of Hunter &amp; Phillip</td><td>60329 Frankfurt am Main</td><td>Centre,</td><td>Minato-ku, Tokyo 106-0041</td></tr><tr><td>Streets</td><td>Germany</td><td>1 Austin Road West,Kowloon,</td><td>Japan</td></tr><tr><td>Sydney, NSW 2000</td><td>Tel: (49) 69 910 00</td><td>Hong Kong</td><td>Tel: (81) 3 6730 1000</td></tr><tr><td>Australia</td><td></td><td>Tel: (852) 2203 8888</td><td></td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td></td><td></td></tr><tr><td>DB AG</td><td>DB Securities Inc.</td><td>DB AG</td><td></td></tr><tr><td>21 Moorfields</td><td>The DB Center</td><td>Filiale Singapur</td><td></td></tr><tr><td>London EC2Y 9DB</td><td>1 Columbus Circle</td><td>One Raffles Quay, South</td><td></td></tr><tr><td>United Kingdom</td><td>New York, NY 10019</td><td>Tower,</td><td></td></tr><tr><td>Tel: (44) 20 7545 8000</td><td>Tel: (1) 212 250 2500</td><td>Singapore 048583</td><td></td></tr><tr><td></td><td></td><td>Tel: +65 6423 8001</td><td></td></tr></table>
"""
