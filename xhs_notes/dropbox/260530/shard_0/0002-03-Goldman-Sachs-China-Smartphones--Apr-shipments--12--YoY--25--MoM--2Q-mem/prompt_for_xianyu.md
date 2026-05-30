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
# China Smartphones: Apr shipments +12% YoY/ +25% MoM; 2Q memory cost pressures remained

April smartphone shipments in China were +12% YoY to 25m units, or +25% MoM. Monthly shipments continued the sequential increase trend in April post March shipments at +24% MoM. We expect 2Q26 shipments to decline at 6% YoY (report link), given rising memory cost weighing on demand. For cameras, the number of cameras per phone peaked in 2022 at 3.8 cameras and declined to 3.1/2.9 cameras in 2025/2026 YTD; however, 20MPx+ penetration increased to 57%/63% in 2025/2026 YTD (vs. 52%/39% in 2024/23), in line with our view on camera specification upgrades for China smartphones (report link). Read more: Smartphone TAM.

Buy: Hon Hai (on CL), AAC, Lingyi, Largan, SZS, Fositek, and TSMC (on CL).

# Key China smartphone data in April China 5G phone market in April

5G phone shipments in China came in at 25m units in April, +26% MoM, +24% YoY, with a 96% penetration rate, per MIIT.   
The number of new 5G smartphone models launched in China was $+95\%$ YoY to 37 models in April 2026 vs. $-61\%$ YoY to 13 models in Mar 2026, per MIIT.

# China smartphone market in April

- Smartphone shipments in China were +12% YoY to 25m units in April 2026 vs. -6% YoY in March 2026, per MIIT.   
The number of new smartphone models launched in China was +56% YoY to 50 models in April 2026 vs. -69% YoY to 15 models in March 2026, per MIIT.

# Smartphone camera pixels in leading China smartphone brands in 2026 YTD

We reviewed the 141 models launched by Honor, Xiaomi, OPPO, Vivo and Transsion in 2026 YTD, totaling 412 cameras.   
Average number of cameras per model was at 2.9 in 2026 YTD, vs. 3.1/ 3.3/ 3.5/ 3.8 / 4.1 / 4.9 / 4.0 in 2025/ 2024/ 2023 / 2022 / 2021 / 2020 / 2019. Among the 412 cameras, $25\%$ of cameras were 2MPx/5MPx/8MPx, vs. $31\%$ / $36\%$ / $45\%$ / $51\%$ / $50\%$ / $57\%$ / $46\%$ in 2025/ 2024/ 2023 / 2022 / 2021 / 2020 / 2019.   
■ 19 models have been launched by Honor in 2026 YTD with a total of 55 cameras,

# Allen Chang

+852-2978-2930

allen.k.chang@gs.com

GS (Asia) L.L.C.

# Verena Jeng

+852-2978-1681 | verena.jeng@gs.com

GS (Asia) L.L.C.

# Ting Song

+852-2978-6466 | ting.song@gs.com

GS (Asia) L.L.C.

# Yifan Hu

+852-2978-0996 | yifan.hu@gs.com

GS (Asia) L.L.C.

or 2.9 cameras per model, vs. Huawei at 2.9 cameras, OPPO at 3.0 cameras, Xiaomi at 2.7 cameras, Vivo at 3.0 cameras, and Transsion at 2.8 cameras.

Among the 155 cameras in the 51 models that Oppo has launched in 2026 YTD, $25\%$ were 2MPx/5MPx/8MPx, vs. Huawei at $26\%$ , Honor at $22\%$ , Xiaomi at $26\%$ , Vivo at $21\%$ , and Transsion at $33\%$ .

# China smartphone shipments and specification

Exhibit 1: 5G smartphone shipments in China: 25m units in April   
![](images/910189cf31afb3eb941dfe57b98b22ced33c9210e9e738f3febef13feb81fd4c.jpg)

<details>
<summary>bar</summary>

| Month | Value (m units) |
|---|---|
| Jan-21 | 27 |
| Feb-21 | 28 |
| Mar-21 | 22 |
| Apr-21 | 16 |
| May-21 | 19 |
| Jun-21 | 23 |
| Jul-21 | 17 |
| Aug-21 | 15 |
| Sep-21 | 26 |
| Oct-21 | 29 |
| Nov-21 | 27 |
| Dec-21 | 26 |
| Jan-22 | 11 |
| Feb-22 | 16 |
| Mar-22 | 14 |
| Apr-22 | 17 |
| May-22 | 18 |
| Jun-22 | 23 |
| Jul-22 | 14 |
| Aug-22 | 14 |
| Sep-22 | 15 |
| Oct-22 | 19 |
| Nov-22 | 18 |
| Dec-22 | 23 |
| Jan-23 | 16 |
| Feb-23 | 17 |
| Mar-23 | 17 |
| Apr-23 | 13 |
| May-23 | 20 |
| Jun-23 | 17 |
| Jul-23 | 15 |
| Aug-23 | 16 |
| Sep-23 | 29 |
| Oct-23 | 26 |
| Nov-23 | 27 |
| Dec-23 | 24 |
| Jan-24 | 26 |
| Feb-24 | 13 |
| Mar-24 | 17 |
| Apr-24 | 20 |
| May-24 | 26 |
| Jun-24 | 23 |
| Jul-24 | 20 |
| Aug-24 | 19 |
| Sep-24 | 23 |
| Oct-24 | 27 |
| Nov-24 | 28 |
| Dec-24 | 30 |
| Jan-25 | 24 |
| Feb-25 | 18 |
| Mar-25 | 19 |
| Apr-25 | 19 |
| May-25 | 20 |
| Jun-25 | 18 |
| Jul-25 | 23 |
| Aug-25 | 19 |
| Sep-25 | 24 |
| Oct-25 | 29 |
| Nov-25 | 27 |
| Dec-25 | 23 |
| Jan-26 | 19 |
| Feb-26 | 16 |
| Mar-26 | 19 |
| Apr-26 | 25 |
</details>

Source: MIIT

Exhibit 2: Monthly # of new 5G smartphone models launched in China   
![](images/39980fca09e45211aaa2e71df8c9fcde15ecbd5522aec65e4ce915b22b8654b3.jpg)

<details>
<summary>bar</summary>

| Date | Value (units) |
|---|---|
| Jan-21 | 32 |
| Apr-21 | 16 |
| Jul-21 | 10 |
| Oct-21 | 27 |
| Jan-22 | 16 |
| Apr-22 | 24 |
| Jul-22 | 15 |
| Oct-22 | 24 |
| Jan-23 | 15 |
| Apr-23 | 27 |
| Jul-23 | 9 |
| Oct-23 | 25 |
| Jan-24 | 10 |
| Apr-24 | 19 |
| Jul-24 | 11 |
| Oct-24 | 29 |
| Jan-25 | 7 |
| Apr-25 | 18 |
| Jul-25 | 30 |
| Oct-25 | 19 |
| Jan-26 | 18 |
| Apr-26 | 10 |
| May-26 | 37 |
</details>

Source: MIIT

Exhibit 3: 2014-15 4G mobile phone shipments and penetration rate   
![](images/d6615dd410635f2466d42b33e7775c7930ceb169e703bccf3ed1a9f675e84610.jpg)

<details>
<summary>bar_line</summary>

| Month | 4G mobile phone shipments to China (mn units) | Penetration rate (RHS) (%) |
|---|---|---|
| Jan-14 | 5 | 8 |
| Feb-14 | 2 | 6 |
| Mar-14 | 4 | 10 |
| Apr-14 | 7 | 15 |
| May-14 | 9 | 20 |
| Jun-14 | 14 | 25 |
| Jul-14 | 15 | 30 |
| Aug-14 | 11 | 35 |
| Sep-14 | 19 | 45 |
| Oct-14 | 21 | 55 |
| Nov-14 | 31 | 65 |
| Dec-14 | 31 | 70 |
| Jan-15 | 35 | 75 |
| Feb-15 | 20 | 80 |
| Mar-15 | 29 | 80 |
| Apr-15 | 37 | 85 |
| May-15 | 37 | 85 |
| Jun-15 | 32 | 85 |
| Jul-15 | 39 | 85 |
| Aug-15 | 40 | 85 |
| Sep-15 | 36 | 85 |
| Oct-15 | 32 | 85 |
| Nov-15 | 46 | 85 |
| Dec-15 | 50 | 90 |
</details>

Source: MIIT

Exhibit 4: Monthly # of new 4G mobile phone models launched in China   
![](images/a258f10aeb88ee415f2aec78ba77c57baa469140797d08143d21dfc23923a5c1.jpg)

<details>
<summary>bar</summary>

| Month | # of new 4G mobile phone models (units) |
|---|---|
| Jun-14 | 128 |
| Jul-14 | 76 |
| Aug-14 | 58 |
| Sep-14 | 117 |
| Oct-14 | 47 |
| Nov-14 | 74 |
| Dec-14 | 74 |
</details>

Source: MIIT

Exhibit 5: Smartphone shipments in China   
![](images/e1484eb62efd63e1b0e9dacef67f1fe46ac5071c6c198b026574447b3dd75534.jpg)

<details>
<summary>bar_line</summary>

| Date | Smartphone shipments in China (m units) | YoY(RHS) (%) |
|---|---|---|
| Jan-21 | 39.5 | 90 |
| Mar-21 | 21.2 | 240 |
| May-21 | 26.7 | -18 |
| Jul-21 | 25.1 | 6 |
| Sep-21 | 23.0 | 7 |
| Nov-21 | 32.8 | 11 |
| Jan-22 | 34.7 | 11 |
| Mar-22 | 32.5 | 5 |
| May-22 | 14.5 | -10 |
| Jul-22 | 20.9 | 9 |
| Sep-22 | 18.7 | 5 |
| Nov-22 | 23.8 | 4 |
| Jan-23 | 26.7 | 5 |
| Mar-23 | 18.1 | -10 |
| May-23 | 21.3 | 8 |
| Jul-23 | 25.1 | 10 |
| Sep-23 | 17.4 | 7 |
| Nov-23 | 31.9 | 15 |
| Jan-24 | 28.0 | 10 |
| Mar-24 | 26.7 | -7 |
| May-24 | 30.0 | 11 |
| Jul-24 | 28.7 | 9 |
| Sep-24 | 21.9 | 11 |
| Nov-24 | 27.8 | -5 |
| Jan-25 | 32.3 | 10 |
| Mar-25 | 24.5 | -5 |
| May-25 | 21.6 | -8 |
| Jul-25 | 22.3 | -6 |
| Sep-25 | 24.6 | -8 |
| Nov-25 | 31.3 | -7 |
| Jan-26 | 28.4 | -6 |
| Mar-26 | 16.3 | -7 |
| Apr-26 | 20.0 | -6 |
(Note: The data labels appear as 'Jan-21' to 'Mar-26') are not explicitly provided in the image, so they are not explicitly labeled on the chart itself.)
</details>

Source: MIIT

Exhibit 6: Number of new smartphone models launched in China   
![](images/b41d6d950fd84b544b78de7fb4743c183fbc33b58a4a9922ab37695178649ccf.jpg)

<details>
<summary>bar_line</summary>

| Month | # of new smartphone models (units) | YoY(RHS) (%) |
|---|---|---|
| Jan-21 | 41 | 65 |
| Feb-21 | 24 | 75 |
| Mar-21 | 33 | 25 |
| Apr-21 | 26 | -15 |
| May-21 | 21 | -10 |
| Jun-21 | 30 | -10 |
| Jul-21 | 21 | -30 |
| Aug-21 | 51 | 40 |
| Sep-21 | 53 | 35 |
| Oct-21 | 23 | -25 |
| Nov-21 | 46 | 35 |
| Dec-21 | 28 | -15 |
| Jan-22 | 28 | -30 |
| Feb-22 | 35 | -10 |
| Mar-22 | 35 | 30 |
| Apr-22 | 19 | -10 |
| May-22 | 28 | -10 |
| Jun-22 | 18 | -15 |
| Jul-22 | 43 | -10 |
| Aug-22 | 28 | -30 |
| Sep-22 | 37 | -10 |
| Oct-22 | 33 | -30 |
| Nov-22 | 37 | -10 |
| Dec-22 | 33 | -30 |
| Jan-23 | 11 | -60 |
| Feb-23 | 26 | -40 |
| Mar-23 | 42 | -10 |
| Apr-23 | 51 | 40 |
| May-23 | 27 | -40 |
| Jun-23 | 46 | -10 |
| Jul-23 | 28 | -40 |
| Aug-23 | 32 | -30 |
| Sep-23 | 21 | -40 |
| Oct-23 | 19 | -40 |
| Nov-23 | 17 | -40 |
| Dec-23 | 19 | -40 |
| Jan-24 | 17 | -40 |
| Feb-24 | 19 | -40 |
| Mar-24 | 29 | -40 |
| Apr-24 | 28 | -40 |
| May-24 | 37 | -40 |
| Jun-24 | 19 | -40 |
| Jul-24 | 35 | -40 |
| Aug-24 | 19 | -40 |
| Sep-24 | 33 | -40 |
| Oct-24 | 26 | -40 |
| Nov-24 | 18 | -40 |
| Dec-24 | 25 | -40 |
| Jan-25 | 25 | -40 |
| Feb-25 | 48 | -40 |
| Mar-25 | 32 | -40 |
| Apr-25 | 27 | -40 |
| May-25 | 49 | -40 |
| Jun-25 | 29 | -40 |
| Jul-25 | 26 | -40 |
| Aug-25 | 50 | -40 |
| Sep-25 | 29 | -40 |
| Oct-25 | 26 | -40 |
| Nov-25 | 21 | -40 |
| Dec-25 | 33 | -40 |
| Jan-26 | 18 | -60 |
| Feb-26 | 15 | -80 |
| Mar-26 | 50 | -60 |
The chart displays a combination of bar values (bars) and a line value (line) for the year 'Mar' through the year 'Dec'. The data is already in English. The y-axis is labeled as '(units)' and the x-axis is labeled as 'Month'. The line series is also labeled as 'YoY(RHS)' but does not correspond to the bar values. The data is presented in the same order: 'Jan', 'Feb', 'Mar', etc. The bars are filled with blue, and the line is filled with red. The y-axis is labeled as '(units)' and the x-axis is labeled as 'Month'.
</details>

Source: MIIT

Exhibit 7: Mobile phone shipments in China 

<table><tr><td>m units</td><td>Apr-25</td><td>May-25</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td></tr><tr><td>Mobile phones</td><td>25</td><td>24</td><td>23</td><td>28</td><td>23</td><td>28</td><td>32</td><td>30</td><td>24</td><td>23</td><td>17</td><td>21</td><td>26</td></tr><tr><td>YoY</td><td>4%</td><td>-22%</td><td>-9%</td><td>16%</td><td>-6%</td><td>10%</td><td>9%</td><td>2%</td><td>-29%</td><td>-16%</td><td>-15%</td><td>-7%</td><td>3%</td></tr><tr><td>MoM</td><td>10%</td><td>-5%</td><td>-5%</td><td>24%</td><td>-20%</td><td>24%</td><td>16%</td><td>-7%</td><td>-19%</td><td>-7%</td><td>-27%</td><td>26%</td><td>22%</td></tr><tr><td>5G</td><td>19.9</td><td>21.2</td><td>18.4</td><td>22.6</td><td>20.0</td><td>24.1</td><td>29.3</td><td>27.6</td><td>22.1</td><td>19.9</td><td>15.9</td><td>19.7</td><td>24.7</td></tr><tr><td>5G to mobile phones</td><td>79%</td><td>89%</td><td>82%</td><td>81%</td><td>88%</td><td>86%</td><td>91%</td><td>92%</td><td>90%</td><td>87%</td><td>95%</td><td>93%</td><td>96%</td></tr><tr><td>Chinese Brands</td><td>22</td><td>19</td><td>17</td><td>25</td><td>21</td><td>24</td><td>25</td><td>23</td><td>21</td><td>20</td><td>14</td><td>18</td><td>22</td></tr><tr><td>Chinese Brands to mobile phones</td><td>86%</td><td>81%</td><td>77%</td><td>90%</td><td>94%</td><td>85%</td><td>78%</td><td>77%</td><td>87%</td><td>88%</td><td>86%</td><td>84%</td><td>86%</td></tr><tr><td>Smartphone</td><td>22</td><td>23</td><td>21</td><td>24</td><td>22</td><td>26</td><td>31</td><td>29</td><td>23</td><td>21</td><td>16</td><td>20</td><td>25</td></tr><tr><td>YoY</td><td>-2%</td><td>-21%</td><td>-14%</td><td>10%</td><td>3%</td><td>8%</td><td>12%</td><td>2%</td><td>-29%</td><td>-16%</td><td>-13%</td><td>-6%</td><td>12%</td></tr><tr><td>MoM</td><td>4%</td><td>1%</td><td>-9%</td><td>19%</td><td>-11%</td><td>18%</td><td>22%</td><td>-8%</td><td>-20%</td><td>-9%</td><td>-21%</td><td>24%</td><td>25%</td></tr><tr><td>Smartphone to mobile phones</td><td>89%</td><td>95%</td><td>91%</td><td>87%</td><td>96%</td><td>92%</td><td>97%</td><td>95%</td><td>93%</td><td>91%</td><td>97%</td><td>95%</td><td>97%</td></tr><tr><td># of new smartphone models (units)</td><td>32</td><td>27</td><td>10</td><td>28</td><td>49</td><td>29</td><td>26</td><td>24</td><td>21</td><td>32</td><td>18</td><td>15</td><td>50</td></tr><tr><td>YoY</td><td>14%</td><td>-27%</td><td>-47%</td><td>56%</td><td>40%</td><td>53%</td><td>-21%</td><td>-8%</td><td>17%</td><td>28%</td><td>64%</td><td>-69%</td><td>56%</td></tr><tr><td>MoM</td><td>-33%</td><td>-16%</td><td>-63%</td><td>180%</td><td>75%</td><td>-41%</td><td>-10%</td><td>-8%</td><td>-13%</td><td>52%</td><td>-44%</td><td>-17%</td><td>233%</td></tr><tr><td># of new mobile models (units)</td><td>50</td><td>39</td><td>36</td><td>48</td><td>65</td><td>47</td><td>45</td><td>31</td><td>41</td><td>37</td><td>23</td><td>19</td><td>59</td></tr><tr><td>5G</td><td>19</td><td>13</td><td>8</td><td>23</td><td>31</td><td>23</td><td>19</td><td>24</td><td>11</td><td>20</td><td>15</td><td>13</td><td>37</td></tr><tr><td>5G to total new mobile models</td><td>38%</td><td>33%</td><td>22%</td><td>48%</td><td>48%</td><td>49%</td><td>42%</td><td>77%</td><td>27%</td><td>54%</td><td>65%</td><td>68%</td><td>63%</td></tr></table>

Source: MIIT

Exhibit 8: Model pricing for various foldable smartphone brands   
![](images/e0626b20d767f969a408d4ea9561c58c994e6b4878de2489d95f780a3d223131.jpg)

<details>
<summary>bar</summary>

| Model | Sales ($) |
|---|---|
| Samsung Galaxy Z Fold 5 | 1870 |
| Huawei Mate X5 | 1860 |
| Oppo Find N3 | 1430 |
| Huawei Pocket 2 Vivo X Fold 3 | 1050 |
| Honor Magic V Flip | 710 |
| Xiaomi Mix Fold 4 | 1290 |
| Huawei Nova Flip | 760 |
| Huawei Mate XT Ultimate | 2850 |
| Tecno Phantom V Fold 2 | 1090 |
| Huawei Mate X6 | 1860 |
| Oppo Find N5 | 1420 |
| Huawei Pura X | 1040 |
| Honor Magic V5 | 1280 |
| Honor Magic V Flip2 | 780 |
| Huawei Mate XTs Ultimate Design | 2570 |
| Samsung W26 | 2410 |
| Huawei Mate X7 | 1850 |
| Samsung Galaxy Z TriFold | 2840 |
| Honor Magic V6 | 1280 |
| Huawei Pura X Max | 1570 |
| Lenovo moto razr fold | 1420 |
</details>

Source: Company data, Data compiled by GS Global Investment Research

Exhibit 9: 2025 to 2026 smartphone model launch pipeline across key vendors   
![](images/0f7582bcc44cb28f39eb0803b2e22f52b5bb89115c5d487599099ee63f96be6d.jpg)  
Expected model and launch date for those cells with white background   
Source: Company data, Data compiled by GS Global Investment Research

Exhibit 10: Cameras per smartphone model peaking out Smartphone models launched by Huawei, Honor, Xiaomi, OPPO, Vivo, Transsion since Dec 2020   
![](images/34c14b397e155ff478bd8e20bc7571df7fc3ac951ab357e2a816c1d26adb6c8f.jpg)

<details>
<summary>bar_line</summary>

| Month | # of models (RHS) | Cameras per model |
|---|---|---|
| Jan-23 | 1.3 | 47 |
| Feb-23 | 1.3 | 46 |
| Mar-23 | 2.3 | 45 |
| Apr-23 | 2.1 | 44 |
| May-23 | 2.1 | 44 |
| Jun-23 | 1.8 | 43 |
| Jul-23 | 1.5 | 42 |
| Aug-23 | 1.0 | 43 |
| Sep-23 | 1.9 | 44 |
| Oct-23 | 1.0 | 45 |
| Nov-23 | 1.8 | 45 |
| Dec-23 | 1.7 | 44 |
| Jan-24 | 1.6 | 45 |
| Feb-24 | 1.3 | 44 |
| Mar-24 | 1.7 | 45 |
| Apr-24 | 2.6 | 44 |
| May-24 | 2.5 | 43 |
| Jun-24 | 1.8 | 42 |
| Jul-24 | 1.6 | 41 |
| Aug-24 | 1.7 | 40 |
| Sep-24 | 1.5 | 39 |
| Oct-24 | 2.6 | 38 |
| Nov-24 | 1.7 | 39 |
| Dec-24 | 1.6 | 39 |
| Jan-25 | 1.5 | 39 |
| Feb-25 | 1.4 | 39 |
| Mar-25 | 2.3 | 38 |
| Apr-25 | 2.0 | 39 |
| May-25 | 2.3 | 39 |
| Jun-25 | 1.8 | 38 |
| Jul-25 | 1.8 | 37 |
| Aug-25 | 1.9 | 36 |
| Sep-25 | 1.9 | 37 |
| Oct-25 | 1.7 | 38 |
| Nov-25 | 1.3 | 39 |
| Dec-25 | 1.3 | 38 |
| Jan-26 | 3.0 | 37 |
| Feb-26 | 1.0 | 36 |
| Mar-26 | 2.5 | 35 |
| Apr-26 | 3.7 | 34 |
| May-26 | 1.1 | 37 |
</details>

Data as of May 27, 2026   
Source: Company data, Data compiled by GS Global Investment Research

# Exhibit 12: Huawei/Honor/Xiaomi/OPPO/Vivo/Transsion: 20MPx+ becomes the main contributor

Cameras on smartphones launched by Huawei, Honor, Xiaomi, OPPO, Vivo, Transsion since 2018: % of cameras in terms of pixels

![](images/7a4e86d0aa921b9998221cb34d5426e3ce02391451b7f44bda992ed0f8eebd5d.jpg)

<details>
<summary>line</summary>

| Quarter | 2/5/8MPx | 20MPx+ | 10-19MPx |
|---------|----------|--------|----------|
| 1Q18    | 35%      | 10%    | 55%      |
| 2Q18    | 38%      | 20%    | 45%      |
| 3Q18    | 40%      | 25%    | 40%      |
| 4Q18    | 42%      | 28%    | 35%      |
| 1Q19    | 45%      | 30%    | 30%      |
| 2Q19    | 48%      | 32%    | 25%      |
| 3

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global

Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
