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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`UBS`。标题格式建议：`# UBS：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份UBS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# UBS Global I/O Semiconductors

# Auto semis: Sustained Analog Momentum, but Selectivity Warranted

## Analog upcycle continues, but we remain selective

Following Q1, we have reviewed the latest leading indicators and refreshed our outlook for the automotive semiconductor market for 2026E–2027E. Recent data indicate that the cycle is progressing as expected, and we therefore leave our automotive estimates unchanged. However, we note some upward revisions to industrial forecasts from consensus and UBS. While pricing remains the key upside risk given pockets of supply/demand tightness, we believe these are limited—primarily within certain AI-related products—and that broader markets still face mixed demand and lingering oversupply. As such, we do not see conditions approaching a COVID-era shortage and maintain a selective stance, particularly after the recent strong performance. We also highlight a slowdown in the Chinese auto market, which could offset the recovery seen in Europe and the US.

## 1) Positive Analog revenue growth persisting through 2026E

Based on latest results, company guidance and consensus, positive momentum that started in Q2'25 is expected to continue throughout 2026E. Q1'26 revenue was up 20% y-o-y and consensus expects Q2 and FY26 to grow by 21% (FY26 16% previously). A supporting trend in the quarter was our distributor tracker data suggesting signs of price increases, after reports that several analog companies have increased pricing in Q1 (ie TI, IFX and NXP) due to inflation costs, which in our view suggests upside (ie flat pricing) vs previous expectations for LSD% price decline for FY26.

## 2) Automotive recovery is here, but there is an emerging headwind

Automotive semis revenues were up 7.8% y-o-y in Q1'26, achieving the first quarter of clear y-o-y growth in over two years, and consensus expects +9% growth in Q2'26. We forecast auto semis revs up 10% y-o-y in 2026E and +14% FY 2027 (all unchanged), primarily underpinned by the end of destocking. Despite positive trends, we are cautious around the Chinese market, with January–May retail sales data in China, and c20–30% of global automotive semiconductor demand down -15 to -20% YTD y-o-y with EVs -10 to -15% y-o-y YTD, which could raise the risk of an inventory correction in H2'26.

## 3) Industrial expectations lifted once again

On the industrial side, revs grew 26% y-o-y in Q1'26, driven by solid performance across the main analog players, and we expect Industrial revs to grow by 25% y-o-y in 2026E vs c16% previously. For 2027E, we forecast c16% y-o-y growth vs. 10% previously. AI continues to grow in importance with several companies lifting guidance, beating expectations, and gaining more visibility for the end-market during the quarter (MCHP, STM).

## Latest datapoints from the quarter

1) The latest UBS distributor tracker data showed reassuring inventory trends and that pricing continues to trend positively across the majority of products, up 2% m-o-m and 9% y-o-y; 2) April NEV wholesale volumes rebounded to 1.2m units, up 7% MoM and 8% YoY; 3) We lowered our smartphone industry unit Sell In forecast to 1.14bn or -10% YoY for 2026 (was -5%), and for 2027 to 1.16bn (+2%).

## Sector preferences - remaining positive but more selective

Analog semis are trading on c30x P/E 12m fwd, vs the 10Y avg of 19x. Most preferred names are Buy-rated TI, Renesas, and STM. Least preferred are ON (Neutral), IFX (Neutral), and Melexis (Neutral).

## Equities

Global

Semiconductors

Francois-Xavier Bouvignies

Analyst

francois.bouvignies@ubs.com

+44-20-7568 7105

Timothy Arcuri

Analyst

timothy.arcuri@ubs.com

+1-415-352 5676

Nicolas Gaudois

Analyst

nicolas.gaudois@ubs.com

+65-6495 5148

Kenji Yasui

Analyst

kenji.yasui@ubs.com

+81-3-5208 6211

Randy Abrams

Analyst

randy.abrams@ubs.com

+886-2-8722 7338

Sunny Lin

Analyst

sunny.lin@ubs.com

+886-2-8722 7346

Harry Blaiklock, CFA

Analyst

harry.blaiklock@ubs.com

+44-20-7568 5385

Jimmy Yu

Analyst

S1460517080002

jimmy.yu@ubs.com

+86-21-3866 8880

Shingo Hirata, CFA

Analyst

shingo.hirata@ubs.com

+81-3-5208 6224

Patrick Hummel, CFA

Analyst

patrick.hummel@ubs.com

+41-44-239 52 54

## LEAD INDICATORS CONTINUE TO BE SUPPORTIVE

We believe lead indicators are positive into the start of FY26E.

Figure 1: UBS leading indicators for Autos/Industrial semis - we see a general positive trend in terms of cycle

<table><tr><td rowspan="2">Indicator</td><td colspan="18">Trend</td><td></td></tr><tr><td>Q1&#x27;22</td><td>Q2&#x27;22</td><td>Q3&#x27;22</td><td>Q4&#x27;22</td><td>Q1&#x27;23</td><td>Q2&#x27;23</td><td>Q3&#x27;23</td><td>Q4&#x27;23</td><td>Q1&#x27;24</td><td>Q2&#x27;24</td><td>Q3&#x27;24</td><td>Q4&#x27;24</td><td>Q1&#x27;25</td><td>Q2&#x27;25</td><td>Q3&#x27;25</td><td>Q4&#x27;25</td><td>Q1&#x27;26</td><td>Q2&#x27;26E</td><td>Commentary</td></tr><tr><td>1) Semis y-o-y revenue growth</td><td>21%</td><td>22%</td><td>23%</td><td>11%</td><td>5%</td><td>2%</td><td>-3%</td><td>-8%</td><td>-17%</td><td>-18%</td><td>-15%</td><td>-14%</td><td>-8%</td><td>1%</td><td>5%</td><td>11%</td><td>20%</td><td>21%</td><td>Positive - Revenue turned positive in Q2&#x27;25 and is estimated continue to accelerate into FY26E</td></tr><tr><td>2) Semis vs OEM revenue gap</td><td>20%</td><td>23%</td><td>12%</td><td>1%</td><td>-4%</td><td>-12%</td><td>-13%</td><td>-15%</td><td>-15%</td><td>-16%</td><td>-12%</td><td>-12%</td><td>-6%</td><td>-2%</td><td>-3%</td><td>7%</td><td>15%</td><td>19%</td><td>Neutral- Strong outperformance suggesting overbuilding</td></tr><tr><td>3) Inventory days - Semis</td><td>114</td><td>115</td><td>117</td><td>127</td><td>144</td><td>148</td><td>147</td><td>155</td><td>166</td><td>170</td><td>167</td><td>181</td><td>179</td><td>175</td><td>166</td><td>170</td><td>171</td><td>164</td><td>Positive - Inventory days showing stability in Q1 26</td></tr><tr><td>4) Inventory days - OEMs</td><td>75</td><td>80</td><td>75</td><td>75</td><td>79</td><td>84</td><td>77</td><td>77</td><td>80</td><td>84</td><td>79</td><td>74</td><td>75</td><td>73</td><td>72</td><td>73</td><td>77</td><td>74</td><td>Positive- Inventory days showing signs of small increase in Q1 and expected to decrease in Q2</td></tr><tr><td>5) Autos production y-o-y</td><td>-4%</td><td>1.3%</td><td>29.5%</td><td>3.4%</td><td>7.4%</td><td>17.1%</td><td>5.2%</td><td>10.5%</td><td>0.1%</td><td>-0.6%</td><td>-4.5%</td><td>1.0%</td><td>3.6%</td><td>3.4%</td><td>6.7%</td><td>1.1%</td><td>-</td><td>-</td><td>Neutral - Production was robust in 2025 with +3.6% growth y-o-y. We estimate +1.3% y-o-y in 2026E but with signs of decline in China</td></tr></table>

Source: UBS estimates

Figure 2: We expect next quarter to grow by 9% q-o-q after an increase of 4% in Q1'26...  
![](images/28c662fdb67b37a0ec02973da9d74540cd10f7fdfd98c81755827201fdb58587.jpg)

<details>
<summary>bar chart</summary>

| Quarter | Value (%) |
|---|---|
| Q1 2021 | 2 |
| Q2 2021 | 4 |
| Q3 2021 | 4 |
| Q4 2021 | 8 |
| Q1 2022 | 4 |
| Q2 2022 | 5 |
| Q3 2022 | 5 |
| Q4 2022 | -3 |
| Q1 2023 | -1 |
| Q2 2023 | 2 |
| Q3 2023 | -0.2 |
| Q4 2023 | -8 |
| Q1 2024 | -11 |
| Q2 2024 | -1 |
| Q3 2024 | 4 |
| Q4 2024 | -7 |
| Q1 2025 | -4 |
| Q2 2025 | 9 |
| Q3 2025 | 8 |
| Q4 2025 | -1 |
| Q1 2026 | 3 |
| Q2 2026E | 8 |
| Q3 2026E | 9 |
| Q4 2026E | 0 |
</details>

Source: UBS estimates, company data. Note: data includes TI, ON, ADI, IFX, STM, Microchip, Melexis, NXP, Renesas

Figure 3: ...Q2'26E likely to deliver 21% y-o-y growth after 20% in Q1'26  
![](images/f2d51f17056a92dfd8b017fd69d47565ae2635c29ea34bbca6feacb899daa2a1.jpg)

<details>
<summary>bar chart</summary>

| Quarter | Value (%) |
|---|---|
| Q1 2021 | 24 |
| Q2 2021 | 35 |
| Q3 2021 | 21 |
| Q4 2021 | 19 |
| Q1 2022 | 21 |
| Q2 2022 | 22 |
| Q3 2022 | 23 |
| Q4 2022 | 11 |
| Q1 2023 | 5 |
| Q2 2023 | 2 |
| Q3 2023 | -3 |
| Q4 2023 | -8 |
| Q1 2024 | -17 |
| Q2 2024 | -18 |
| Q3 2024 | -15 |
| Q4 2024 | -14 |
| Q1 2025 | -8 |
| Q2 2025 | 1 |
| Q3 2025 | 5 |
| Q4 2025 | 11 |
| Q1 2026E | 20 |
| Q2 2026E | 21 |
| Q3 2026E | 21 |
| Q4 2026E | 23 |
</details>

Source: UBS estimates, company data. Note: data includes TI, ON, ADI, IFX, STM, Microchip, Melexis, NXP, Renesas

Figure 4: CQ2 26E Guidance Comp. Y-o-Y % Analog Semis  
![](images/cf4a7ad9515ac9876d7426051f94ab711c4bb0ac8912788250f8241350dc6c47.jpg)

<details>
<summary>bar chart</summary>

|        | Mar-26A | Jun-26 |
| ------ | ------- | ------ |
| ON     | 5%      | 8%     |
| NXP    | 12%     | 18%    |
| MELX   | 13%     | 1%     |
| IFX    | 18%     | 14%    |
| TXN    | 19%     | 17%    |
| RENESAS| 19%     | 8%     |
| STM    | 23%     | 25%    |
| MCHP   | 35%     | 35%    |
| ADI    | 37%     | 35%    |
</details>

Source: Company data. Note: \*Renesas - growth adj. for acquisition of Dialog

Figure 5: CQ2 26E Guidance Comp. Q-o-Q % Analog Semis  
![](images/45ae7c6ad2fa1028f90eeff782944bc30ece7d296af372a983bdb6237cc55497.jpg)

<details>
<summary>bar chart</summary>

|        | Mar-26A | Jun-26 |
| ------ | ------- | ------ |
| STM    | -7%     | 11%    |
| MELX   | -5%     | 3%     |
| NXP    | -5%     | 8%     |
| ON     | -1%     | 5%     |
| IFX    | 5%      | 7%     |
| RENESAS| 5%      | 2%     |
| TXN    | 9%      | 8%     |
| MCHP   | 11%     | 11%    |
| ADI    | 15%     | 8%     |
</details>

Source: Company data. Note: \* Renesas - growth adj. for acquisition of Dialog

Figure 6: We estimate 10% y-o-y auto semis revenue growth in 2026E (unchanged) and +c14% in 2027E vs (unchanged) based on our bottom-up estimates.

<table><tr><td></td><td colspan="5">GARTNER HISTORICS</td><td colspan="11">UBS ESTIMATES</td><td colspan="2"></td></tr><tr><td>Semi sales (US$bn)</td><td>2015</td><td>2016</td><td>2017</td><td>2018</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025E</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td><td>% CAGR (&#x27;23-&#x27;27)</td><td>% CAGR (&#x27;25-&#x27;30)</td></tr><tr><td>ADAS</td><td>1.7</td><td>3.0</td><td>4.1</td><td>5.1</td><td>5.9</td><td>5.4</td><td>10.4</td><td>13.9</td><td>16.1</td><td>16.7</td><td>15.3</td><td>20.3</td><td>27.0</td><td>33.8</td><td>36.6</td><td>38.8</td><td>14%</td><td>20%</td></tr><tr><td>Aftermarket</td><td>2.2</td><td>2.2</td><td>2.3</td><td>2.5</td><td>2.5</td><td>2.4</td><td>2.9</td><td>3.4</td><td>3.9</td><td>3.3</td><td>3.1</td><td>3.1</td><td>3.1</td><td>3.2</td><td>3.2</td><td>3.2</td><td>-5%</td><td>1%</td></tr><tr><td>Body</td><td>4.6</td><td>5.5</td><td>6.6</td><td>7.4</td><td>6.9</td><td>6.8</td><td>8.1</td><td>9.4</td><td>10.9</td><td>9.3</td><td>8.6</td><td>8.6</td><td>8.7</td><td>8.8</td><td>8.9</td><td>9.0</td><td>-5%</td><td>1%</td></tr><tr><td>Chassis</td><td>4.6</td><td>4.5</td><td>5.1</td><td>5.4</td><td>5.1</td><td>5.0</td><td>5.9</td><td>6.9</td><td>8.0</td><td>6.9</td><td>6.4</td><td>6.3</td><td>6.5</td><td>6.5</td><td>6.6</td><td>6.7</td><td>-5%</td><td>1%</td></tr><tr><td>Infotainment</td><td>7.2</td><td>7.7</td><td>8.4</td><td>9.0</td><td>8.4</td><td>8.3</td><td>9.8</td><td>12.0</td><td>14.0</td><td>12.6</td><td>12.1</td><td>12.8</td><td>13.9</td><td>15.1</td><td>15.3</td><td>15.5</td><td>0%</td><td>5%</td></tr><tr><td>Powertrain</td><td>5.4</td><td>6.8</td><td>7.4</td><td>8.0</td><td>7.5</td><td>7.4</td><td>11.3</td><td>16.0</td><td>20.4</td><td>19.5</td><td>19.0</td><td>20.2</td><td>22.5</td><td>24.2</td><td>26.1</td><td>28.1</td><td>3%</td><td>8%</td></tr><tr><td>Safety</td><td>4.4</td><td>4.3</td><td>4.6</td><td>4.7</td><td>4.1</td><td>4.1</td><td>4.8</td><td>5.9</td><td>6.8</td><td>5.8</td><td>5.5</td><td>5.7</td><td>6.0</td><td>6.2</td><td>6.3</td><td>6.4</td><td>-3%</td><td>3%</td></tr><tr><td>Total</td><td>30.1</td><td>34.1</td><td>38.5</td><td>42.2</td><td>40.5</td><td>39.4</td><td>53.3</td><td>67.5</td><td>80.0</td><td>74.1</td><td>70.0</td><td>77.0</td><td>87.8</td><td>97.8</td><td>103.2</td><td>107.7</td><td>2%</td><td>9%</td></tr><tr><td>% y-o-y</td><td></td><td>13.3%</td><td>13.1%</td><td>9.5%</td><td>-4.0%</td><td>-2.7%</td><td>35.3%</td><td>26.6%</td><td>18.5%</td><td>-7.3%</td><td>-5.5%</td><td>10.0%</td><td>14.0%</td><td>11.4%</td><td>5.5%</td><td>4.4%</td><td></td><td></td></tr><tr><td>Inventory adjustment (- restocking and + de-stocking)</td><td></td><td></td><td></td><td></td><td>-1</td><td>-5</td><td>-5</td><td>-5</td><td>-10</td><td>-1</td><td>7</td><td>5</td><td>2</td><td>0</td><td>0</td><td>0</td><td></td><td></td></tr><tr><td>Autos production(m)</td><td>88.8</td><td>93.1</td><td>95.3</td><td>94.2</td><td>88.7</td><td>74.6</td><td>77.2</td><td>82.3</td><td>90.5</td><td>89.6</td><td>92.8</td><td>94.0</td><td>95.4</td><td>96.8</td><td>98.4</td><td>99.3</td><td></td><td></td></tr><tr><td>% y-o-y</td><td></td><td>4.9%</td><td>2.3%</td><td>-1.2%</td><td>-5.8%</td><td>-15.9%</td><td>3.5%</td><td>6.7%</td><td>9.9%</td><td>-1.0%</td><td>3.6%</td><td>1.3%</td><td>1.4%</td><td>1.0%</td><td>1.0%</td><td>1.0%</td><td></td><td></td></tr></table>

Source: Gartner, UBS estimates

Figure 7: The analog semis within our coverage are trading on a -17% discount to semis cap, vs. a -2% discount a year ago  
![](images/580c09e7b977d20030480a78b8b5a1f38f17fa092a8d915070185a6c94dbc33e.jpg)

<details>
<summary>line chart</summary>

| Date    | Semis Premium/Discount Vs. SemiCaps | SemiCaps P/E | Semis analog P/E |
|---------|--------------------------------------|--------------|------------------|
| May-16  | ~25.0                                | ~15.0        | ~18.0            |
| Sep-16  | ~25.0                                | ~15.0        | ~18.0            |
| Jan-17  | ~25.0                                | ~15.0        | ~18.0            |
| May-17  | ~25.0                                | ~15.0        | ~18.0            |
| Sep-17  | ~25.0                                | ~15.0        | ~18.0            |
| Jan-18  | ~25.0                                | ~15.0        | ~18.0            |
| May-18  | ~25.0                                | ~15.0        | ~18.0            |
| Sep-18  | ~25.0                                | ~15.0        | ~18.0            |
| Jan-19  | ~25.0                                | ~15.0        | ~18.0            |
| May-19  | ~25.0                                | ~15.0        | ~18.0            |
| Sep-19  | ~25.0                                | ~15.0        | ~18.0            |
| Jan-20  | ~25.0                                | ~15.0        | ~18.0            |
| May-20  | ~35.0                                | ~25.0        | ~30.0            |
| Sep-20  | ~35.0                                | ~25.0        | ~30.0            |
| Jan-21  | ~35.0                                | ~30.0        | ~30.0            |
| May-21  | ~35.0                                | ~30.0        | ~30.0            |
| Sep-21  | ~35.0                                | ~30.0        | ~30.0            |
| Jan-22  | ~35.0                                | ~30.0        | ~30.0            |
| May-22  | ~35.0                                | ~30.0        | ~30.0            |
| Sep-22  | ~35.0                                | ~30.0        | ~30.0            |
| Jan-23  | ~35.0                                | ~30.0        | ~30.0            |
| May-23  | ~35.0                                | ~30.0        | ~30.0            |
| Sep-23  | ~35.0                                | ~35.0        | ~35.0            |
| Jan-24  | ~35.0                                | ~35.0        | ~35.0            |
| May-24  | ~35.0                                | ~35.0        | ~35.0            |
| Sep-24  | ~35.0                                | ~35.0        | ~35.0            |
| Jan-25  | ~35.0                                | ~35.0        | ~35.0            |
| May-25  | ~35.0                                | ~35.0        | ~35.0            |
| Sep-25  | ~35.0                                | ~40.0        | ~40.0            |
| Jan-26  | ~35.0                                | ~45.0        | ~45.0            |
| May-26  | ~35.0                                | ~45.0        | ~45.0            |
</details>

Source: UBS, Datastream. This chart includes global companies in analog and semis cap.

## China growth has been supportive through 2025, but we see some risks in 2026

We have broken out our auto semis model by region, and estimate that China auto semis revenues grew 7% y-o-y in 2025, consistent with commentary of relative strength through the year from our coverage. Looking into 2026, we expect China to grow 5%, with outperformance from non-China up 8% y-o-y. Importantly this 5% does not take into account any potential inventory correction which could drive growth lower. When accounting for potential share loss to domestic semis players, we think global incumbents' auto semis revenues in China are set to be flat in 2026, while we estimate non-China revenues will be up 8% y-o-y, not taking into account any impact from inventory build/correction.

Figure 8: China % of revenue for main analog players  
![](images/7d5f69ffd7e8469d93b90c115a60122d743f87fb47ec15ea61f64304bba9b81d.jpg)

<details>
<summary>bar chart</summary>

China % of revenue
| Year | IFX (%) | STM (%) | RENE (%) | TXN (%) | ADI (%) | NXP (%) |
|---|---|---|---|---|---|---|
| 2023 | 32 | 15 | 24 | 19 | 18 | |
| 2024 | 34 | 15 | 28 | 19 | 23 | 15 |
| 2025 | 30 | 14 | 31 | 21 | 26 | 17 |
</details>

Source: Company data, UBS; TXN and NXP is revenue from China HQ companies

Figure 9: China growth y-o-y by companies shows significant difference

<table><tr><td>YoY%</td><td>2015</td><td>2016</td><td>2017</td><td>2018</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td></tr><tr><td>IFX</td><td></td><td>17%</td><td>55%</td><td>14%</td><td>1%</td><td>17%</td><td>37%</td><td>10%</td><td>4%</td><td>-4%</td><td>14%</td></tr><tr><td>RENE</td><td></td><td>1%</td><td>41%</td><td>3%</td><td>-1%</td><td>14%</td><td>33%</td><td>54%</td><td>-21%</td><td>-3%</td><td>10%</td></tr><tr><td>TXN</td><td></td><td>3%</td><td>10%</td><td>6%</td><td>3%</td><td>-38%</td><td>3%</td><td>5%</td><td>-31%</td><td>-9%</td><td>26%</td></tr><tr><td>ADI</td><td></td><td>13%</td><td>46%</td><td>44%</td><td>9%</td><td>2%</td><td>20%</td><td>59%</td><td>-13%</td><td>-5%</td><td>34%</td></tr><tr><td>NXP</td><td></td><td>24%</td><td>-6%</td><td>20%</td><td>-7%</td><td>27%</td><td>-18%</td><td>12%</td><td>-7%</td><td>4%</td><td>6%</td></tr><tr><td>Total</td><td></td><td>11%</td><td>15%</td><td>13%</td><td>0%</td><td>-5%</td><td>8%</td><td>19%</td><td>-13%</td><td>-3%</td><td>18%</td></tr></table>

Source: Company data, UBS

Figure 10: China grew c7% y-o-y in 2025 but is set to grow more in 

[中间内容因长度限制已省略]

d Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

## CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with "Risk information" and "Important Information About Sustainable Investing Strategies" sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its subsidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/0c59cc7e8f295942721e98c1c6aa8525e5a1343733979c21f8a685aa17c49772.jpg)
"""
