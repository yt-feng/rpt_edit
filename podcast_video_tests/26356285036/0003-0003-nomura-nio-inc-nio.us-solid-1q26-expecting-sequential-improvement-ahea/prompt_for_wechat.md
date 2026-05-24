你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 1800 字，允许上下浮动 15%。
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
1. `# 标题`：一句主判断，不超过 32 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来社群继续拆完整报告。
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
- 默认避免出现具体投行品牌名，比如“高盛”“Goldman Sachs”，统一写作“某外资投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Solid 1Q26; expecting sequential improvement ahead Quick Note

# 1Q26: revenue +112% y-y and -26% q-q while GPM +11.4pp y-y and +1.5pp q-q; second consecutive quarter with non-GAAP profit achieved

NIO reported 1Q26 results on 21 May before US market open. The company delivered a revenue of CNY25.5bn, +112% y-y while -26% q-q, at the high-end of its original guidance and in line with market expectation. While vehicle shipments reached 83.5k, +98% y-y and -33% q-q (also at the high-end of its guidance), vehicle sales were at CNY22.8bn, +129% y-y and -28% q-q, as a result of an 8% q-q sequential increase in vehicle ASP due to the solid sales of ES8, which contributed 54% of total sales in 1Q26. NIO's GPM was at 19.0%, +11.4pp y-y and +1.5pp q-q, and its vehicle margin was at 18.8% in the quarter, +8.6pp y-y and +0.8pp q-q, again owing to both shipment growth and/or product mix improvement. Its OPM was at -1.2%, +52.1pp y-y and -3.5pp q-q, as a result of less favourable operating leverage during the weak auto season. As a result, NIO reported a net loss of CNY496mn in 1Q26, with the loss decreasing 93% y-y. Its non-GAAP net profit was at CNY43.5mn, as the company recorded a second consecutive quarter with non-GAAP profit.

On 2Q26 guidance, the company expects to deliver 110-115k units of sales, +53-60% y-y, also implying an average 41-43k sales into May/Jun-26. On top line, the company guided for a revenue range of CNY32.8-34.4bn in 2Q, potentially +72-81% y-y. With that, we estimate that the implied ASP per unit in 2Q26F would be around CNY267k, slightly down 2% q-q from 1Q26 ASP of 273k, considering more shipments may come from new models like Onvo L80 and ES9 in 2Q26.

While Onvo L80 is already launched, we believe the entire market would be tracking ES9's performance as the model would be launched next Wednesday (27 May). With a sustainable ES8 shipment/order situation, we believe NIO will need to have more in-demand models to further support its shipment, market share and margin profile.

Considering a good feedback for its ES9 pre-order data, according to our industry survey, we remain positive on the name and expect NIO to deliver a sequential improvement in shipment and financials into following quarters in 2026. We maintain our Buy rating and DCF-based TP of USD8.6 for the share. The stock is currently trading at 2026F P/S of 0.7x.

# Earnings call takeaways:

- With ES9 reaching stores, the company said that it has attracted more in-store visits in the past one month, therefore helping ES8 getting more orders. Management mentioned that in the first 20 days in May, its orders locked for ES8 reached the highest level for the same period since Oct-25.   
- Looking at the GPM outlook for 2Q26 and entire 2026, management mentioned that the BOM (bill of materials) cost increase, including lithium price, memory, aluminium and copper (the impact of the increase to be CNY10k per vehicle) are not yet fully reflected in 1Q26 due to its inventory. Overall, the company continues to target for a $17 - 18\%$ vehicle GPM for 2Q26 and full-year 2026. Meanwhile, NOI targets to maintain a $20\%$ GPM for its business other than vehicle sales.   
- For 2H26, NIO will release a five-seat version of ES8 and targets three-five new models each year in the next few years. The core strategy for NIO is to establish itself as a premium brand, targeting at becoming the next car after BBA (Benz, BMW and Audi) brands.

<table><tr><td>RatingRemains</td><td>Buy</td></tr><tr><td>Target priceRemains</td><td>USD 8.60</td></tr><tr><td>Closing price20 May 2026</td><td>USD 5.59</td></tr></table>

# Research Analysts

# China Autos & Auto Parts

Joel Ying, CFA - NIHK

joel.ying@nomura.com

+852 2252 2153

# Global EV Batteries & Materials

Ethan Zhang - NIHK

ethan.zhang@nomura.com

+852 2252 2157

- In terms of R&D cost, the company reiterated a CNY2.0-2.5bn quarterly expenditure. On SG&A expense, NIO maintained its target to control it at 10% of total sales for full-year 2026 while there could be fluctuations during quarters. As key new models releasing in 2Q26, management expects selling expense to grow evidently q-q. NIO maintained its guidance to achieve non-GAPP operating profit breakeven in 2026E.   
- For its self-developed Shenji NX9031 chips, management targets for $80 - 85\%$ penetration of it within its total shipment into 2H26.   
- For its battery swap station, the company targets to build 1k new stations in 2026 while its third generation station will start to deploy from 3Q26.

Fig. 1: NIO - 1Q26 results review 

<table><tr><td rowspan="2" colspan="2">(CNY mn)</td><td rowspan="2">1Q25A</td><td rowspan="2">2Q25A</td><td rowspan="2">3Q25A</td><td rowspan="2">4Q25A</td><td rowspan="2">1Q26A</td><td colspan="2">% chg</td><td rowspan="2" colspan="2">2Q26Guidance</td><td rowspan="2">2023A</td><td rowspan="2">2024A</td><td rowspan="2">2025A</td></tr><tr><td>y-y</td><td>q-q</td></tr><tr><td colspan="2">Total revenue</td><td>12,035</td><td>19,009</td><td>21,794</td><td>34,650</td><td>25,533</td><td>112%</td><td>-26%</td><td>32,777</td><td>34,436</td><td>55,618</td><td>65,732</td><td>87,488</td></tr><tr><td></td><td>% y-y</td><td>21%</td><td>9%</td><td>17%</td><td>76%</td><td>112%</td><td></td><td></td><td>72.4%</td><td>81.2%</td><td>13%</td><td>18%</td><td>33%</td></tr><tr><td colspan="2">Vehicle sales</td><td>9,939</td><td>16,136</td><td>19,202</td><td>31,606</td><td>22,784</td><td>129%</td><td>-28%</td><td></td><td></td><td>49,257</td><td>58,234</td><td>76,884</td></tr><tr><td></td><td>% y-y</td><td>19%</td><td>3%</td><td>15%</td><td>81%</td><td>129%</td><td></td><td></td><td></td><td></td><td>8%</td><td>18%</td><td>32%</td></tr><tr><td colspan="2">COGS</td><td>(11,115)</td><td>(17,111)</td><td>(18,769)</td><td>(28,576)</td><td>(20,674)</td><td>86%</td><td>-28%</td><td></td><td></td><td>(52,566)</td><td>(59,239)</td><td>(75,572)</td></tr><tr><td></td><td>% y-y</td><td>18%</td><td>9%</td><td>13%</td><td>64%</td><td>86%</td><td></td><td></td><td></td><td></td><td>19%</td><td>13%</td><td>28%</td></tr><tr><td colspan="2">Vehicle COGS</td><td>(8,926)</td><td>(14,473)</td><td>(16,379)</td><td>(25,893)</td><td>(18,491)</td><td>107%</td><td>-29%</td><td></td><td></td><td>(44,588)</td><td>(51,095)</td><td>(65,671)</td></tr><tr><td></td><td>% y-y</td><td>17%</td><td>5%</td><td>13%</td><td>70%</td><td>107%</td><td></td><td></td><td></td><td></td><td>14%</td><td>15%</td><td>29%</td></tr><tr><td colspan="2">Gross profit</td><td>920</td><td>1,898</td><td>3,025</td><td>6,074</td><td>4,859</td><td>428%</td><td>-20%</td><td></td><td></td><td>3,052</td><td>6,493</td><td>11,916</td></tr><tr><td></td><td>% y-y</td><td>89%</td><td>12%</td><td>51%</td><td>163%</td><td>428%</td><td></td><td></td><td></td><td></td><td>-41%</td><td>113%</td><td>84%</td></tr><tr><td colspan="2">Vehicle GP</td><td>1,014</td><td>1,663</td><td>2,824</td><td>5,713</td><td>4,292</td><td>323%</td><td>-25%</td><td></td><td></td><td>4,670</td><td>7,139</td><td>11,213</td></tr><tr><td></td><td>% y-y</td><td>32%</td><td>-13%</td><td>29%</td><td>150%</td><td>323%</td><td></td><td></td><td></td><td></td><td>-25%</td><td>53%</td><td>57%</td></tr><tr><td colspan="2">OPEX</td><td>(7,338)</td><td>(6,806)</td><td>(6,546)</td><td>(5,267)</td><td>(5,168)</td><td>-30%</td><td>-2%</td><td></td><td></td><td>(25,707)</td><td>(28,778)</td><td>(25,957)</td></tr><tr><td colspan="2">SG&amp;A</td><td>(4,401)</td><td>(3,965)</td><td>(4,185)</td><td>(3,537)</td><td>(3,497)</td><td>-21%</td><td>-1%</td><td></td><td></td><td>(12,885)</td><td>(15,741)</td><td>(16,088)</td></tr><tr><td colspan="2">R&amp;D expense</td><td>(3,181)</td><td>(3,007)</td><td>(2,391)</td><td>(2,026)</td><td>(1,885)</td><td>-41%</td><td>-7%</td><td></td><td></td><td>(13,431)</td><td>(13,037)</td><td>(10,605)</td></tr><tr><td colspan="2">Operating profit</td><td>(6,418)</td><td>(4,909)</td><td>(3,522)</td><td>807</td><td>(309)</td><td>-95%</td><td>-138%</td><td></td><td></td><td>(22,655)</td><td>(22,286)</td><td>(14,041)</td></tr><tr><td></td><td>% y-y</td><td>19%</td><td>-6%</td><td>-33%</td><td>-113%</td><td>-95%</td><td></td><td></td><td></td><td></td><td>45%</td><td>-2%</td><td>-37%</td></tr><tr><td colspan="2">Interest and investment income</td><td>173</td><td>108</td><td>354</td><td>127</td><td>116</td><td></td><td></td><td></td><td></td><td>2,210</td><td>854</td><td>762</td></tr><tr><td colspan="2">Interest expense</td><td>(245)</td><td>(213)</td><td>(223)</td><td>(205)</td><td>(214)</td><td></td><td></td><td></td><td></td><td>(404)</td><td>(798)</td><td>(885)</td></tr><tr><td colspan="2">Pretax income</td><td>(6,745)</td><td>(4,952)</td><td>(3,423)</td><td>300</td><td>(320)</td><td>-95%</td><td>-207%</td><td></td><td></td><td>(20,459)</td><td>(22,425)</td><td>(14,821)</td></tr><tr><td></td><td>% y-y</td><td>30%</td><td>-2%</td><td>-32%</td><td>-104%</td><td>-95%</td><td></td><td></td><td></td><td></td><td>42%</td><td>10%</td><td>-34%</td></tr><tr><td colspan="2">Taxes</td><td>(5)</td><td>(43)</td><td>(57)</td><td>(17)</td><td>(12)</td><td></td><td></td><td></td><td></td><td>(261)</td><td>23</td><td>(122)</td></tr><tr><td colspan="2">Net income</td><td>(6,891)</td><td>(5,141)</td><td>(3,661)</td><td>122</td><td>(496)</td><td>-93%</td><td>-505%</td><td></td><td></td><td>(21,147)</td><td>(22,658)</td><td>(15,571)</td></tr><tr><td></td><td>% y-y</td><td>31%</td><td>0%</td><td>-29%</td><td>-102%</td><td>-93%</td><td></td><td></td><td></td><td></td><td>45%</td><td>7%</td><td>-31%</td></tr><tr><td colspan="14">Ratio Analysis</td></tr><tr><td colspan="2">GPM</td><td>7.6%</td><td>10.0%</td><td>13.9%</td><td>17.5%</td><td>19.0%</td><td>11.4pp</td><td>1.5pp</td><td></td><td></td><td>5.5%</td><td>9.9%</td><td>13.6%</td></tr><tr><td colspan="2">Vehicle GPM</td><td>10.2%</td><td>10.3%</td><td>14.7%</td><td>18.1%</td><td>18.8%</td><td>8.6pp</td><td>0.8pp</td><td></td><td></td><td>9.5%</td><td>12.3%</td><td>14.6%</td></tr><tr><td colspan="2">OPEX</td><td>-61.0%</td><td>-35.8%</td><td>-30.0%</td><td>-15.2%</td><td>-20.2%</td><td>40.7pp</td><td>-5.0pp</td><td></td><td></td><td>-46.2%</td><td>-43.8%</td><td>-29.7%</td></tr><tr><td colspan="2">OPM</td><td>-53.3%</td><td>-25.8%</td><td>-16.2%</td><td>2.3%</td><td>-1.2%</td><td>52.1pp</td><td>-3.5pp</td><td></td><td></td><td>-40.7%</td><td>-33.9%</td><td>-16.0%</td></tr><tr><td colspan="2">NPM</td><td>-57.3%</td><td>-27.0%</td><td>-16.8%</td><td>0.4%</td><td>-1.9%</td><td>55.3pp</td><td>-2.3pp</td><td></td><td></td><td>-38.0%</td><td>-34.5%</td><td>-17.8%</td></tr></table>

Source: Company data, Nomura research

Fig. 2: NIO - quarterly shipment trend 

<table><tr><td rowspan="2" colspan="2"></td><td rowspan="2">1Q25A</td><td rowspan="2">2Q25A</td><td rowspan="2">3Q25A</td><td rowspan="2">4Q25A</td><td rowspan="2">1Q26A</td><td colspan="2">% chg</td><td rowspan="2" colspan="2">2Q26Guidance</td><td rowspan="2">2023A</td><td rowspan="2">2024A</td><td rowspan="2">2025A</td></tr><tr><td>y-y</td><td>q-q</td></tr><tr><td colspan="2">Total vehicle delivery</td><td>42,094</td><td>72,056</td><td>87,071</td><td>124,807</td><td>83,465</td><td>98%</td><td>-33%</td><td>110,000</td><td>115,000</td><td>160,038</td><td>221,970</td><td>326,028</td></tr><tr><td></td><td>% y-y</td><td>40%</td><td>26%</td><td>41%</td><td>72%</td><td>98%</td><td></td><td></td><td>52.7%</td><td>59.6%</td><td>31%</td><td>39%</td><td>47%</td></tr><tr><td>ET series</td><td></td><td>11,658</td><td>21,961</td><td>19,600</td><td>16,278</td><td>7,804</td><td>-33%</td><td>-52%</td><td></td><td></td><td>67,852</td><td>84,681</td><td>69,497</td></tr><tr><td></td><td>% y-y</td><td>-5%</td><td>-11%</td><td>-23%</td><td>-27%</td><td>-33%</td><td></td><td></td><td></td><td></td><td>94%</td><td>25%</td><td>-18%</td></tr><tr><td>ES series</td><td></td><td>10,924</td><td>18,434</td><td>13,231</td><td>48,177</td><td>49,256</td><td>351%</td><td>2%</td><td></td><td></td><td>77,201</td><td>86,437</td><td>90,766</td></tr><tr><td></td><td>% y-y</td><td>-16%</td><td>-24%</td><td>-51%</td><td>118%</td><td>351%</td><td></td><td></td><td></td><td></td><td>9%</td><td>12%</td><td>5%</td></tr><tr><td>EC series</td><td></td><td>4,731</td><td>6,737</td><td>4,097</td><td>2,978</td><td>1,483</td><td>-69%</td><td>-50%</td><td></td><td></td><td>14,985</td><td>30,091</td><td>18,543</td></tr><tr><td></td><td>% y-y</td><td>-2%</td><td>-19%</td><td>-52%</td><td>-65%</td><td>-69%</td><td></td><td></td><td></td><td></td><td>-12%</td><td>101%</td><td>-38%</td></tr><tr><td>Onvo</td><td></td><td>14,781</td><td>17,081</td><td>37,656</td><td>38,290</td><td>13,339</td><td>-10%</td><td>-65%</td><td></td><td></td><td></td><td>20,761</td><td>107,808</td></tr><tr><td></td><td>% y-y</td><td></td><td></td><td>4426%</td><td>92%</td><td>-10%</td><td></td><td></td><td></td><td></td><td></td><td></td><td>419%</td></tr><tr><td>Firefly</td><td></td><td>-</td><td>7,843</td><td>12,487</td><td>19,084</td><td>11,583</td><td>n.a.</td><td>-39%</td><td></td><td></td><td></td><td></td><td>39,414</td></tr><tr><td></td><td>% y-y</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Source: Company data, CAAM, Nomura research

Fig. 3: NIO – monthly sales by sub brands   
![](images/a4da35d784e2ab281729fd70df9a2349b660c9b1d3f6c86ce6e5e00471764668.jpg)

<details>
<summary>bar_stacked</summary>

| Month | NIO brand sales (k units) | Onvo sales (k units) | Firefly sales (k units) |
|---|---|---|---|
| Jan-24 | 10 | 0 | 0 |
| Mar-24 | 8 | 0 | 0 |
| May-24 | 15 | 0 | 0 |
| Jul-24 | 21 | 0 | 0 |
| Sep-24 | 20 | 1 | 0 |
| Nov-24 | 15 | 3 | 0 |
| Jan-25 | 20 | 7 | 0 |
| Mar-25 | 8 | 3 | 0 |
| May-25 | 18 | 4 | 1 |
| Jul-25 | 13 | 5 | 0 |
| Sep-25 | 10 | 11 | 9 |
| Nov-25 | 17 | 11 | 11 |
| Jan-26 | 31 | 9 | 13 |
| Mar-26 | 15 | 4 | 7 |
| End of Year | 19 | 4 | 6 |
</details>

Source: Company data, CAAM, Nomura research

Fig. 4: NIO - EV market share trend in China   
![](images/cbdb255cea10bcc2818b85bbaaa4a0357c945131610fdfd72f7cb4c132861889.jpg)

<details>
<summary>line</summary>

| Month    | Value |
| -------- | ----- |
| Jan-24   | 1.5%  |
| Mar-24   | 2.0%  |
| May-24   | 2.5%  |
| Jul-24   | 2.3%  |
| Sep-24   | 2.0%  |
| Nov-24   | 1.8%  |
| Jan-25   | 2.4%  |
| Mar-25   | 1.9%  |
| May-25   | 2.7%  |
| Jul-25   | 2.3%  |
| Sep-25   | 2.8%  |
| Nov-25   | 3.2%  |
| Jan-26   | 4.5%  |
| Mar-26   | 4.0%  |
</details>

Source: Company data, CPCA, Nomura research

# Appendix A-1

This report has been produced by Nomura International (Hong Kong) Ltd. (NIHK), Hong Kong.

See Disclaimers for Nomura Group entity details.

# Analyst Certification

I, Joel Ying, hereby certify (1) that the views expressed in this Research report accurately reflect my personal views about any or all of the subject securities or issuers referred to in this Research report, (2) no part of my compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this Research report and (3) no part of my compensation is tied to any specific investment banking transactions performed by Nomura Securities International, Inc., Nomura International plc or any other Nomura Group company.

# Issuer Specific Regulatory Disclosures

The terms "Nomura" and "Nomura Group" used herein refer to Nomura Holdings, Inc. and its affiliates and subsidiaries, including Nomura Securities International, Inc. ('NSI') and Instinet, LLC ('ILLC'), U. S. registered broker dealers and members of SIPC.

Materially mentioned issuers 

<table><tr><td>Issuer</td><td>Ticker</td><td>Price</td><td>Price date</td><td>Stock rating</td><td>Sector rating</td><td>Disclosures</td></tr><tr><td>NIO Inc</td><td>NIO US</td><td>USD 5.59</td><td>20-May-2026</td><td>Buy</td><td>N/A</td><td></td></tr></table>

# NIO Inc (NIO US)

Rating and target price chart (three year history)   
![](images/76e6d08db2182d24888c63e1cd66f80c0083d491bbf04638a79e526be88dde52.jpg)

<details>
<summary>line</summary>

| Date       | Closing Price | Target Price Change | Recommendation Changes |
| ---------- | ------------- | ------------------- | ----------------------- |
| 2023/07/01 | ~15.00        | -                   | 7.50                    |
| 2024/01/01 | ~9.00         | -                   | -                       |
| 2025/01/01 | ~5.00         | 5.00                | -                       |
| 2026/01/01 | ~6.50         | 8.50                | 5.50                    |
</details>

USD 5.59 (20-May-2026) Buy (Sector rating: N/A) 

<table><tr><td>Date</td><td>Rating</td><td>Target price</td><td>Closing price</td></tr><tr><td>22-Apr-26</td><td></td><td>8.60</td><td>6.48</td></tr><tr><td>11-Mar-26</td><td>Buy</td><td></td><td>5.47</td></tr><tr><td>11-Mar-26</td><td></td><td>6.60</td><td>5.47</td></tr><tr><td>22-Sep-25</td><td></td><td>8.40</td><td>6.91</td></tr><tr><td>23-Mar-25</td><td></td><td>5.00</td><td>4.50</td></tr><tr><td>11-Jun-23</td><td>Neutral</td><td></td><td>7.73</td></tr><tr><td>11-Jun-23</td><td></td><td>7.50</td><td>7.73</td></tr></table>

Source: LSEG, Nomura   
For explanation of ratings refer to the stock rating keys located after chart(s)

Valuation Methodology Our TP of USD8.60 is based on DCF valuation method. Our DCF valuation assumes a WACC of 9.8%, market risk premium of 10.1% and terminal growth rate of 1.5% while we discounted back cash flow to 2026 as a 12 months forward valuation. Our TP implies 1.1x 2026F P/S. The benchmark index for this stock is the NASDAQ Composite Index.

Risks that may impede the achievement of the target price Downside risks include: 1) failure to ramp up production capacity meeting its rising demand; 2) fail to gain further market share from new models; 3) less than expected opex improvement lead to more pressure on its financials.

# Important Disclosures

# Online availability of research and conflict-of-interest disclosures

Nomura Group research is available on www.nomuranow.com/research, Bloomberg, Capital IQ, Factset, LSEG.

Important disclosures may be read at http://go.nomuranow.com/research/m/Disclosures or requested from Nomura Securities International, Inc. If you have any difficulties with the website, please email grpsupport@nomura.com for help.

The analysts responsible for preparing this report have received compensation based upon various factors including the firm's total revenues, a portion of which is generated by Investment Banking activities. Unless otherwise noted, the non-US analysts listed at the front of this report are not registered/qualified as research analysts under FINRA rules, may not be associated persons of NSI, and may not be subject to FIN

[中间内容因长度限制已省略]

 SUITABILITY OF THE INVESTMENT, UNDER A SEPARATE ENGAGEMENT, AS THE RECIPIENT DEEMS FIT. Unless prohibited by the provisions of Regulation S of the 1933 Act, this material is distributed in the US, by NSI, a US-registered broker-dealer, which accepts responsibility for its contents in accordance with the provisions of Rule 15a-6, under the US Securities Exchange Act of 1934. The entity that prepared this document permits its separately operated affiliates within the Nomura Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia ('Saudi Arabia') or a 'Market Counterparty' or a 'Professional Client' (as defined by the Dubai Financial Services Authority) in the United Arab Emirates ('UAE') or a 'Market Counterparty' or a 'Business Customer' (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar ('Qatar') by Nomura Saudi Arabia, NIplc or any other member of the Nomura Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than 'Authorised Persons', 'Exempt Persons' or 'Institutions' located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOMURA GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOMURA INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by Nomura Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOMURA GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The Nomura Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of Nomura listed on the front page. Disclosures information is available upon request and disclosure information is available at the Nomura Disclosure web page:

http://go.nomuranow.com/research/m/Disclosures

Copyright © 2026 Nomura International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
