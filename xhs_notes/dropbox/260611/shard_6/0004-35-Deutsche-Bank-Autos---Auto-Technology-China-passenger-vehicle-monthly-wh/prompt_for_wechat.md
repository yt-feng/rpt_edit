你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`DB`。标题格式建议：`# DB：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份DB研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
Asia

China

Consumer

Autos & Auto Technology

Industry

## Autos & Auto Technology

Date

9 June 2026

Industry Update

# China passenger-vehicle monthly wholesale chartbook - May 2026

This chartbook tracks China's passenger-vehicle wholesale volume on a monthly basis, detailing wholesale trends of various automakers.

Figure 1: Wholesale sales volume summary – key OEMs

<table><tr><td colspan="7">Listed Auto Names Summary</td></tr><tr><td>Ticker</td><td>Name</td><td>May-26</td><td>YoY</td><td>MoM</td><td>5M 2026</td><td>YoY</td></tr><tr><td>Total</td><td>Industry</td><td>2,212,337</td><td>-4.9%</td><td>4.9%</td><td>10,189,897</td><td>-6.0%</td></tr><tr><td>Total NEV</td><td>Industry</td><td>1,347,490</td><td>12.0%</td><td>10.3%</td><td>5,290,677</td><td>2.2%</td></tr><tr><td>NEV penetration</td><td></td><td>60.9%</td><td>9.2%</td><td>3.0%</td><td>51.9%</td><td></td></tr><tr><td>1211 HK</td><td>BYD</td><td>383,453</td><td>0.3%</td><td>19.4%</td><td>1,405,039</td><td>-20.3%</td></tr><tr><td>600104 CH</td><td>SAIC</td><td>277,848</td><td>-8.4%</td><td>6.7%</td><td>1,280,073</td><td>-5.7%</td></tr><tr><td>0175 HK</td><td>Geely</td><td>235,319</td><td>0.0%</td><td>0.1%</td><td>1,179,841</td><td>0.6%</td></tr><tr><td>9973 HK</td><td>Chery</td><td>231,867</td><td>21.0%</td><td>-1.9%</td><td>1,034,232</td><td>6.9%</td></tr><tr><td>000625 CH</td><td>Chang&#x27;an</td><td>126,194</td><td>-28.4%</td><td>2.8%</td><td>670,251</td><td>-21.7%</td></tr><tr><td>2238 HK</td><td>GAC</td><td>126,692</td><td>7.9%</td><td>5.2%</td><td>626,337</td><td>3.6%</td></tr><tr><td>2333 HK</td><td>Great Wall</td><td>100,399</td><td>-1.8%</td><td>-5.6%</td><td>475,815</td><td>3.6%</td></tr><tr><td>1958 HK</td><td>BAIC</td><td>75,000</td><td>-11.1%</td><td>24.4%</td><td>341,955</td><td>-10.7%</td></tr><tr><td>9863 HK</td><td>Leap</td><td>81,569</td><td>81.0%</td><td>14.3%</td><td>263,111</td><td>51.5%</td></tr><tr><td>TLSA US</td><td>Tesla China</td><td>85,982</td><td>39.4%</td><td>8.2%</td><td>378,858</td><td>29.4%</td></tr><tr><td>1810 HK</td><td>Xiaomi</td><td>32,759</td><td>16.9%</td><td>-10.7%</td><td>150,317</td><td>13.5%</td></tr><tr><td>9927 HK</td><td>AITO</td><td>30,257</td><td>-16.8%</td><td>0.8%</td><td>130,264</td><td>19.8%</td></tr><tr><td>9868 HK</td><td>Xpeng</td><td>32,158</td><td>-4.1%</td><td>3.7%</td><td>125,851</td><td>-22.6%</td></tr><tr><td>9866 HK</td><td>NIO</td><td>37,705</td><td>62.3%</td><td>28.4%</td><td>150,526</td><td>68.7%</td></tr><tr><td>2015 HK</td><td>Li auto</td><td>33,350</td><td>-18.4%</td><td>-2.2%</td><td>162,577</td><td>-3.0%</td></tr><tr><td>1114 HK</td><td>Brilliance BMW</td><td>31,544</td><td>-31.7%</td><td>-2.7%</td><td>185,411</td><td>-14.5%</td></tr><tr><td>7489 HK</td><td>Voyah</td><td>13,003</td><td>29.7%</td><td>-14.1%</td><td>62,041</td><td>34.7%</td></tr></table>

Source : ThinkerCar

Wei Huang

Research Associate

+852-2203-7057

Bin Wang

Research Analyst

+852-220-35496

Figure 2: Monthly total passenger-vehicle sales trend  
![](images/e6ba86053655a7ea67c023aa5c5cd8c1d952319f24dadf82bb792f73e626b0b8.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Month   | Total Passenger Vehicle Sales (000 Unit) | YoY (%) |
|---------|------------------------------------------|---------|
| Jan-25  | 2100                                     | 12.0    |
| Feb-25  | 1800                                     | 32.0    |
| Mar-25  | 2400                                     | 17.0    |
| Apr-25  | 2200                                     | 18.0    |
| May-25  | 2300                                     | 19.0    |
| Jun-25  | 2500                                     | 20.0    |
| Jul-25  | 2300                                     | 20.0    |
| Aug-25  | 2500                                     | 21.0    |
| Sep-25  | 2800                                     | 18.0    |
| Oct-25  | 3000                                     | 14.0    |
| Nov-25  | 3100                                     | 8.0     |
| Dec-25  | 2800                                     | -6.0    |
| Jan-26  | 1900                                     | -8.0    |
| Feb-26  | 1500                                     | -18.0   |
| Mar-26  | 2400                                     | -1.0    |
| Apr-26  | 2100                                     | -3.0    |
| May-26  | 2200                                     | -4.0    |
</details>

Source : ThinkerCar

Figure 3: Monthly new-energy vehicle (NEV) passenger-vehicle sales trend  
![](images/df78efd37ad9fce1b72dc98d1d984792f44a65feca3417219d8fef4a6f2368b6.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Month | Total NEV passenger vehicle (1,000 Unit) | YoY (%) |
| :--- | :--- | :--- |
| Jan-25 | 880 | 25 |
| Feb-25 | 830 | 90 |
| Mar-25 | 1140 | 35 |
| Apr-25 | 1130 | 40 |
| May-25 | 1210 | 35 |
| Jun-25 | 1240 | 25 |
| Jul-25 | 1180 | 25 |
| Aug-25 | 1300 | 25 |
| Sep-25 | 1480 | 20 |
| Oct-25 | 1600 | 15 |
| Nov-25 | 1700 | 15 |
| Dec-25 | 1560 | 5 |
| Jan-26 | 860 | -5 |
| Feb-26 | 710 | -18 |
| Mar-26 | 1160 | 5 |
| Apr-26 | 1230 | 10 |
| May-26 | 1340 | 15 |
</details>

Source : ThinkerCar

Figure 4: Monthly NEV sales trend  
![](images/bcce464a0295a650b709a20257da2403be08025d2d2c843b9e1fbd25a5c5ce3b.jpg)

<details>
<summary>stacked bar chart</summary>

| Month | ICE (000 Unit) | PHEV (000 Unit) | EV (000 Unit) |
| :--- | :--- | :--- | :--- |
| Jan-25 | 1450 | 450 | 500 |
| Feb-25 | 1350 | 450 | 500 |
| Mar-25 | 1700 | 550 | 700 |
| Apr-25 | 1450 | 450 | 700 |
| May-25 | 1550 | 550 | 750 |
| Jun-25 | 1650 | 600 | 750 |
| Jul-25 | 1450 | 450 | 700 |
| Aug-25 | 1650 | 600 | 800 |
| Sep-25 | 1950 | 750 | 950 |
| Oct-25 | 2150 | 850 | 1000 |
| Nov-25 | 2250 | 950 | 1100 |
| Dec-25 | 1950 | 850 | 950 |
| Jan-26 | 1350 | 450 | 500 |
| Feb-26 | 950 | 350 | 450 |
| Mar-26 | 1650 | 650 | 700 |
| Apr-26 | 1350 | 650 | 800 |
| May-26 | 1350 | 750 | 900 |
</details>

Source : ThinkerCar

Figure 5: Monthly NEV penetration rate trend  
![](images/bd35b39bb31a462e50aa85f1c230c2eb0aecbe9110797fc57fca6f8b641975bc.jpg)

<details>
<summary>line chart</summary>

| Month | Value (%) |
|---|---|
| Jan-25 | 42 |
| Feb-25 | 46.5 |
| Mar-25 | 46.8 |
| Apr-25 | 51.5 |
| May-25 | 51.8 |
| Jun-25 | 49 |
| Jul-25 | 51.7 |
| Aug-25 | 51.8 |
| Sep-25 | 52.5 |
| Oct-25 | 54.2 |
| Nov-25 | 56.1 |
| Dec-25 | 55.3 |
| Jan-26 | 44 |
| Feb-26 | 47 |
| Mar-26 | 48 |
| Apr-26 | 58 |
| May-26 | 61 |
</details>

Source : ThinkerCar

Figure 6: BYD monthly wholesale volume trend  
![](images/5a63b474b636ae9fed7b235cad745060d2dccda27abb4a7d5a56c837b7c08142.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Month | Total Sales | YoY (%) |
| :--- | :--- | :--- |
| Jan-25 | 300 | 45 |
| Feb-25 | 320 | 170 |
| Mar-25 | 380 | 25 |
| Apr-25 | 380 | 23 |
| May-25 | 380 | 21 |
| Jun-25 | 380 | 19 |
| Jul-25 | 340 | 18 |
| Aug-25 | 370 | 18 |
| Sep-25 | 400 | 16 |
| Oct-25 | 440 | 14 |
| Nov-25 | 480 | 18 |
| Dec-25 | 420 | 10 |
| Jan-26 | 210 | -10 |
| Feb-26 | 190 | -45 |
| Mar-26 | 300 | -15 |
| Apr-26 | 320 | -10 |
| May-26 | 380 | 19 |
</details>

Source : ThinkerCar

Figure 7: BYD market share trend  
![](images/d4c7a5ef3e4dfacdc0dd22f4461144692c7a95589ad19f3ff5dec6adcf879389.jpg)

<details>
<summary>line chart</summary>

| Month   | Value  |
| ------- | ------ |
| Jan-25  | 14.0%  |
| Feb-25  | 18.0%  |
| Mar-25  | 15.5%  |
| Apr-25  | 17.0%  |
| May-25  | 16.5%  |
| Jun-25  | 15.5%  |
| Jul-25  | 15.0%  |
| Aug-25  | 14.5%  |
| Sep-25  | 14.0%  |
| Oct-25  | 15.0%  |
| Nov-25  | 16.0%  |
| Dec-25  | 15.0%  |
| Jan-26  | 10.5%  |
| Feb-26  | 12.5%  |
| Mar-26  | 12.5%  |
| Apr-26  | 14.0%  |
| May-26  | 17.0%  |
</details>

Source : ThinkerCar

Figure 8: Tesla China monthly wholesale volume trend  
![](images/ee55e23f37349af497473f2fcf555419551f034ce5c1a1c7a2b7eb05c71e2225.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Month   | Total Sales | YoY    |
|---------|-------------|--------|
| Jan-25  | 63          | 38%    |
| Feb-25  | 30          | -60%   |
| Mar-25  | 79          | 35%    |
| Apr-25  | 58          | 40%    |
| May-25  | 62          | 32%    |
| Jun-25  | 72          | 45%    |
| Jul-25  | 68          | 38%    |
| Aug-25  | 83          | 42%    |
| Sep-25  | 91          | 48%    |
| Oct-25  | 62          | 35%    |
| Nov-25  | 87          | 50%    |
| Dec-25  | 97          | 45%    |
| Jan-26  | 70          | 50%    |
| Feb-26  | 59          | 110%   |
| Mar-26  | 86          | 10%    |
| Apr-26  | 80          | 35%    |
| May-26  | 86          | 40%    |
</details>

Source : ThinkerCar

Figure 9: Tesla China market share trend  
![](images/311899e3cef833e69604c7c1da3c1338b454bdaeefe2070c5075d97f777f610e.jpg)

<details>
<summary>line chart</summary>

| Month   | Value |
|---------|-------|
| Jan-25  | 3.0%  |
| Feb-25  | 1.7%  |
| Mar-25  | 3.3%  |
| Apr-25  | 2.7%  |
| May-25  | 2.7%  |
| Jun-25  | 2.8%  |
| Jul-25  | 3.0%  |
| Aug-25  | 3.3%  |
| Sep-25  | 3.2%  |
| Oct-25  | 2.1%  |
| Nov-25  | 3.0%  |
| Dec-25  | 3.5%  |
| Jan-26  | 3.6%  |
| Feb-26  | 3.9%  |
| Mar-26  | 3.6%  |
| Apr-26  | 3.8%  |
| May-26  | 3.9%  |
</details>

Source : ThinkerCar

Figure 10: Li Auto monthly wholesale volume trend  
![](images/a6407641019bc8cf4c0ffbbefde632652b84bf0666d3d366d9f5d992e4cc9974.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Month | Li auto Monthly Sales Volume (in thousands) | YoY (%) |
| :--- | :--- | :--- |
| Jan-25 | 30 | -10 |
| Feb-25 | 26 | 30 |
| Mar-25 | 37 | 28 |
| Apr-25 | 34 | 35 |
| May-25 | 41 | 25 |
| Jun-25 | 36 | -15 |
| Jul-25 | 31 | -45 |
| Aug-25 | 29 | -40 |
| Sep-25 | 34 | -30 |
| Oct-25 | 32 | -35 |
| Nov-25 | 33 | -20 |
| Dec-25 | 44 | -10 |
| Jan-26 | 28 | -10 |
| Feb-26 | 27 | -5 |
| Mar-26 | 41 | 10 |
| Apr-26 | 34 | -5 |
| May-26 | 33 | -18 |
</details>

Source : ThinkerCar

Figure 11: Li Auto market share trend  
![](images/f632f52330bd5761da2a099301d2541f392dba79db30a0d44e0f2079fcd3c1d9.jpg)

<details>
<summary>line chart</summary>

| Month   | Value  |
|---------|--------|
| Jan-25  | 1.4%   |
| Feb-25  | 1.45%  |
| Mar-25  | 1.5%   |
| Apr-25  | 1.55%  |
| May-25  | 1.75%  |
| Jun-25  | 1.45%  |
| Jul-25  | 1.35%  |
| Aug-25  | 1.15%  |
| Sep-25  | 1.2%   |
| Oct-25  | 1.05%  |
| Nov-25  | 1.1%   |
| Dec-25  | 1.55%  |
| Jan-26  | 1.4%   |
| Feb-26  | 1.75%  |
| Mar-26  | 1.7%   |
| Apr-26  | 1.65%  |
| May-26  | 1.5%   |
</details>

Source : ThinkerCar

Figure 12: NIO monthly wholesale volume trend  
![](images/f842989ed5de95d03df3c976a4f6e3a0ba93243121472296aa799d505a950c61.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Month   | NIO Monthly Sales Volume | YoY   |
|---------|--------------------------|-------|
| Jan-25  | 13                       | 40%   |
| Feb-25  | 13                       | 60%   |
| Mar-25  | 10                       | 20%   |
| Apr-25  | 24                       | 60%   |
| May-25  | 23                       | 20%   |
| Jun-25  | 25                       | 40%   |
| Jul-25  | 21                       | 0%    |
| Aug-25  | 31                       | 60%   |
| Sep-25  | 35                       | 80%   |
| Oct-25  | 41                       | 100%  |
| Nov-25  | 37                       | 80%   |
| Dec-25  | 48                       | 60%   |
| Jan-26  | 27                       | 100%  |
| Feb-26  | 21                       | 60%   |
| Mar-26  | 36                       | 140%  |
| Apr-26  | 30                       | 20%   |
| May-26  | 38                       | 60%   |
</details>

Source : ThinkerCar

Figure 13: NIO market share trend  
![](images/2d2be6730649a54959de7c81ae0f2d571263c1c5d3394129fbaf0f43331de07b.jpg)

<details>
<summary>line chart</summary>

| Month    | Value  |
| -------- | ------ |
| Jan-25   | 0.6%   |
| Feb-25   | 0.7%   |
| Mar-25   | 0.6%   |
| Apr-25   | 1.1%   |
| May-25   | 1.0%   |
| Jun-25   | 1.0%   |
| Jul-25   | 0.9%   |
| Aug-25   | 1.2%   |
| Sep-25   | 1.3%   |
| Oct-25   | 1.4%   |
| Nov-25   | 1.2%   |
| Dec-25   | 1.7%   |
| Jan-26   | 1.4%   |
| Feb-26   | 1.4%   |
| Mar-26   | 1.5%   |
| Apr-26   | 1.4%   |
| May-26   | 1.7%   |
</details>

Source : ThinkerCar

Figure 14: Xpeng monthly wholesale volume trend  
![](images/0828accc561e00e521f90c3a12f1dc7f701d9e5c445155ddac2cae784e3a9dbe.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Month | Xpeng Monthly Sales Volume (000 Unit) | YoY (%) |
|---|---|---|
| Jan-25 | 30 | 200 |
| Feb-25 | 30 | 600 |
| Mar-25 | 33 | 200 |
| Apr-25 | 35 | 200 |
| May-25 | 34 | 180 |
| Jun-25 | 35 | 180 |
| Jul-25 | 36 | 180 |
| Aug-25 | 37 | 150 |
| Sep-25 | 41 | 100 |
| Oct-25 | 42 | 80 |
| Nov-25 | 36 | 50 |
| Dec-25 | 37 | 30 |
| Jan-26 | 20 | -10 |
| Feb-26 | 15 | -15 |
| Mar-26 | 27 | -5 |
| Apr-26 | 31 | -2 |
| May-26 | 32 | -1 |
</details>

Source : ThinkerCar

Figure 15: Xpeng market share trend  
![](images/73981c5b3ac736ea1d160e42765cceb4084f50a00a9ab85643c220907334935c.jpg)

<details>
<summary>line chart</summary>

| Month   | Value  |
| ------- | ------ |
| Jan-25  | 1.4%   |
| Feb-25  | 1.7%   |
| Mar-25  | 1.3%   |
| Apr-25  | 1.6%   |
| May-25  | 1.4%   |
| Jun-25  | 1.3%   |
| Jul-25  | 1.6%   |
| Aug-25  | 1.5%   |
| Sep-25  | 1.4%   |
| Oct-25  | 1.4%   |
| Nov-25  | 1.2%   |
| Dec-25  | 1.3%   |
| Jan-26  | 1.0%   |
| Feb-26  | 1.0%   |
| Mar-26  | 1.1%   |
| Apr-26  | 1.5%   |
| May-26  | 1.4%   |
</details>

Source : ThinkerCar

Figure 16: Leapmotor monthly wholesale volume trend  
![](images/79fe49b66ce3e99ca8639d1e68c5c1a4f99c444d187dc48e8bd97b4848c03e5a.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Month   | Leap Motor Monthly Sales Volume | YoY   |
|---------|----------------------------------|-------|
| Jan-25  | 25                               | 100%  |
| Feb-25  | 25                               | 200%  |
| Mar-25  | 37                               | 150%  |
| Apr-25  | 41                               | 170%  |
| May-25  | 45                               | 150%  |
| Jun-25  | 48                               | 130%  |
| Jul-25  | 50                               | 110%  |
| Aug-25  | 57                               | 90%   |
| Sep-25  | 67                               | 80%   |
| Oct-25  | 70                               | 70%   |
| Nov-25  | 70                               | 60%   |
| Dec-25  | 60                               | 40%   |
| Jan-26  | 32                               | 20%   |
| Feb-26  | 28                               | 10%   |
| Mar-26  | 50                               | 40%   |
| Apr-26  | 71                               | 70%   |
| May-26  | 81                               | 80%   |
</details>

Source : ThinkerCar

Figure 17: Leapmotor market share trend  
![](images/b32d7948184a8404154c12dc4689d1a5bdb5789bb08ab312017157c950f07d85.jpg)

<details>
<summary>line chart</summary>

| Month    | Value |
| -------- | ----- |
| Jan-25   | 1.2%  |
| Feb-25   | 1.4%  |
| Mar-25   | 1.5%  |
| Apr-25   | 1.9%  |
| May-25   | 1.9%  |
| Jun-25   | 1.9%  |
| Jul-25   | 2.2%  |
| Aug-25   | 2.3%  |
| Sep-25   | 2.4%  |
| Oct-25   | 2.4%  |
| Nov-25   | 2.3%  |
| Dec-25   | 2.1%  |
| Jan-26   | 1.6%  |
| Feb-26   | 1.8%  |
| Mar-26   | 2.1%  |
| Apr-26   | 3.4%  |
| May-26   | 3.7%  |
</details>

Source : ThinkerCar

Figure 18: AITO monthly wholesale volume trend  
![](images/210297a6f9c24c8a6652889faab118b25f313c17a0a56e670de2ce18269018a1.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Month   | AITO Monthly Sales Volume (000 unit) | YoY     |
|---------|-------------------------------------|---------|
| Jan-25  | 16                                  | -       |
| Feb-25  | 14                                  | -       |
| Mar-25  | 13                                  | -       |
| Apr-25  | 27                                  | -       |
| May-25  | 36                                  | -       |
| Jun-25  | 43                                  | -       |
| Jul-25  | 41                                  | -       |
| Aug-25  | 41                                  | -       |
| Sep-25  | 41                                  | -       |
| Oct-25  | 49                                  | -       |
| Nov-25  | 52                                  | -       |
| Dec-25  | 54                                  | -       |
| Jan-26  | 40                                  | -       |
| Feb-26  | 9                                   | -       |
| Mar-26  | 30                                  | -       |
| Apr-26  | 30                                  | -       |
| May-26  | 30                                  | -       |
</details>

Source : ThinkerCar

Figure 19: AITO market share trend  
![](images/6378b9a185363e3f2d0a12b476ddf23e18ce304e4a3c0d36fdd4122acd584ca4.jpg)

<details>
<summary>line chart</summary>

| Month   | Value |
|---------|-------|
| Jan-25  | 0.8%  |
| Feb-25  | 0.9%  |
| Mar-25  | 0.6%  |
| Apr-25  | 1.3%  |
| May-25  | 1.6%  |
| Jun-25  | 1.8%  |
| Jul-25  | 1.9%  |
| Aug-25  | 1.7%  |
| Sep-25  | 1.5%  |
| Oct-25  | 1.7%  |
| Nov-25  | 1.8%  |
| Dec-25  | 1.9%  |
| Jan-26  | 2.0%  |
| Feb-26  | 0.7%  |
| Mar-26  | 0.9%  |
| Apr-26  | 1.4%  |
| May-26  | 1.4%  |
</details>

Source : ThinkerCar

Figure 20: Voyah monthly wholesale volume trend  
![](images/80b92cfb70f3e01c5eb8b6eec67deb527952b9912b936e97eda312a5d0a1ac93.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Month | Total Sales (000 Unit) | YoY (%) |
|---|---|---|
| Jan-25 | 8 | 20 |
| Feb-25 | 8 | 140 |
| Mar-25 | 10 | 60 |
| Apr-25 | 10 | 140 |
| May-25 | 10 | 100 |
| Jun-25 | 10 | 60 |
| Jul-25 | 11 | 80 |
| Aug-25 | 13 | 130 |
| Sep-25 | 15 | 60 |
| Oct-25 | 17 | 90 |
| Nov-25 | 20 | 110 |
| Dec-25 | 17.5 | 70 |
| Jan-26 | 10.5 | 40 |
| Feb-26 | 8.5 | 10 |
| Mar-26 | 15 | 50 |
| Apr-26 | 15 | 50 |
| May-26 | 13 | 30 |
</details>

Source : ThinkerCar

Figure 21: Voyah market share trend  
![](images/6e8679476a4d5077f2061e83a28e606298ba03a09a34c2a5f17f38b244987f51.jpg)

<details>
<summary>line chart</summary>

| Month | Value (%) |
|---|---|
| Jan-25 | 0.38 |
| Feb-25 | 0.45 |
| Mar-25 | 0.41 |
| Apr-25 | 0.46 |
| May-25 | 0.43 |
| Jun-25 | 0.40 |
| Jul-25 | 0.49 |
| Aug-25 | 0.54 |
| Sep-25 | 0.54 |
| Oct-25 | 0.59 |
| Nov-25 | 0.67 |
| Dec-25 | 0.63 |
| Jan-26 | 0.53 |
| Feb-26 | 0.55 |
| Mar-26 | 0.63 |
| Apr-26 | 0.72 |
| May-26 | 0.59 |
</details>

Source : ThinkerCar

Figure 22: Xiaomi monthly wholesale volume trend  
![](images/ab9dac9f239629af155069ddfe4e8683d01b370ea58075949ff33a055c890b43.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Month   | Total Sales | YoY    |
|---------|-------------|--------|
| Jan-25  | 23          | -      |
| Feb-25  | 24          | -      |
| Mar-25  | 29          | 600%   |

[中间内容因长度限制已省略]

t from current or potential Banking clients the costs of travel, accommodations, or other expenses incurred by analysts attending site visits, conferences, social events, and the like. Similarly, without prior approval from Research Management and Anti-Bribery and Corruption ("ABC") team, analysts may not accept perks or other items of value for their personal use from issuers they cover.

Additional information relative to securities, other financial products or issuers discussed in this report is available upon request. This report may not be reproduced, distributed or published without DB's prior written consent.

Backtested, hypothetical or simulated performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG. It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG

## David Folkerts-Landau

Group Chief Economist and Global Head of Research

Pam Finelli
COO and Head of Fixed
Income Research

Matthew Barnard
Head of Americas
Company Research

Francis Yared
Global Head of Rates
Research

Steve Pollard
Global Head of Company
Research and Sales

Debbie Jones
Global Head of
Sustainability and Data
Innovation, Research

George Saravelos
Global Head of FX
Research

Jim Reid
Global Head of Macro and
Thematic Research

Robin Winkler
Head of German Macro
Research

Peter Hooper
Vice-Chair of Research

Tim Rokossa
Head of European
Company Research

Sameer Goel
Global Head of EM &
APAC Research

Nilendra de-Mel
Head of APAC & Middle
East Product
Development

International Production Locations

<table><tr><td>DB AG</td><td>DB AG</td><td>DB AG</td><td>Deutsche Securities Inc.</td></tr><tr><td>DB Place</td><td>Equity Research</td><td>Filiale Hongkong</td><td>1-3-1 Azabudai</td></tr><tr><td>Level 16</td><td>Mainzer Landstrasse 11-17</td><td>International Commerce</td><td>Azabudai Hills Mori JP Tower</td></tr><tr><td>Corner of Hunter &amp; Phillip</td><td>60329 Frankfurt am Main</td><td>Centre,</td><td>Minato-ku, Tokyo 106-0041</td></tr><tr><td>Streets</td><td>Germany</td><td>1 Austin Road West,Kowloon,</td><td>Japan</td></tr><tr><td>Sydney, NSW 2000</td><td>Tel: (49) 69 910 00</td><td>Hong Kong</td><td>Tel: (81) 3 6730 1000</td></tr><tr><td>Australia</td><td></td><td>Tel: (852) 2203 8888</td><td></td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td></td><td></td></tr><tr><td>DB AG</td><td>DB Securities Inc.</td><td>DB AG</td><td></td></tr><tr><td>21 Moorfields</td><td>The DB Center</td><td>Filiale Singapur</td><td></td></tr><tr><td>London EC2Y 9DB</td><td>1 Columbus Circle</td><td>One Raffles Quay, South</td><td></td></tr><tr><td>United Kingdom</td><td>New York, NY 10019</td><td>Tower,</td><td></td></tr><tr><td>Tel: (44) 20 7545 8000</td><td>Tel: (1) 212 250 2500</td><td>Singapore 048583</td><td></td></tr><tr><td></td><td></td><td>Tel: +65 6423 8001</td><td></td></tr></table>
"""
