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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`Bernstein`。标题格式建议：`# Bernstein：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份Bernstein研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## Global Semiconductors

# Global Semi: South Korea Equipment Import Tracker (May 26): Import +51% YoY

![](images/e9a37bb2708adcad6c42bfc74c57e6cebb3a7f369ebc344c0fc88f5229454548.jpg)

David Dai, CFA

+852 2918 5704

david.dai@bernsteinsg.com

![](images/3a25d064eb660d51ebc00d643afa7d56309c557abf5f6ab0fd9373eab2c45f76.jpg)

Mark Li

+852 2123 2645

mark.li@bernsteinsg.com

![](images/d393da812f4e030a4035fbb0630711bbab4a8c7a6c5ba02c06a1806cffd4dea3.jpg)

Juho Hwang

+852 2123 2632

juho.hwang@bernsteinsg.com

![](images/8eb129057d8a94dc5cb4b1cbf857a23887eaa198b48a12bebf4c2e638e4bb45b.jpg)

Carmine Milano, CFA

+44 20 7762 1857

carmine.milano@bernsteinsg.com

![](images/6e399aec375ec079bc08db92c8e6abb4f9fda00ec83db4a2755f2d4851e1994c.jpg)

Jack Lin

+852 2123 2683

jack.lin@bernsteinsg.com

![](images/1f9e94b473c40a2c9056938a7d5b963b45a5b9696d8f96044e082b45391b97f7.jpg)

Edward Hou, CFA

+852 2123 2623

edward.hou@bernsteinsg.com

![](images/eff0913d6dac645e4c3563394598530fc7c8528642e50a555d9590ecc43a3931.jpg)

Yipin Cai, CFA

+852 2123 2669

yipin.cai@bernsteinsg.com

Korea Customs Service released May 2026 semiconductor equipment import data on June 15 $^{th}$ . We have extracted and analyzed relevant information that has strong significance for our coverage companies. The import data can be downloaded here: South Korea SPE Import.

Strong Korean SPE imports. Overall, South Korean semi equipment imports in May were globally +51% YoY / -5% MoM. YTD YoY % has accelerated to 39% vs. 37% of April. Imports for Japanese SPE were +40% YoY and -7% MoM.

Strong tester import. Advantest's memory tester revenue has good correlation with South Korea tester import data, which was +5% MoM / +103% YoY. Regression suggests Advantest to see a +84% QoQ increase in JunQ South Korea tester revenue although with only 2 month of data and recent correlation has been weaker. For reference, consensus projects Advantest revenue to be +3% QoQ, to which Korean import suggests upside.

Litho imports point to continued very strong momentum. SK's WFE equipment imports from the Netherlands reached €928mn in May, marking the second-highest second month of a quarter on record, up 28% MoM and \~150% YoY. Based on our regression model, we estimate ASML SK Q2 system sales at \~€2.31bn, down 18% QoQ but more than doubling YoY. This suggests that Korea would account for 37% of total Q2 system sales. Overall, this points to sustained revenue momentum in South Korea and in Memory, likely supported by meaningful DRAM capacity expansion and fast adoption of the 1c node which has considerably higher Litho intensity.

Japan WFE import declines. South Korean import data for the relevant categories for TEL (CVD, dry etching, cleaning, coater & developer, RTP, etc.) in May was +52% YoY / -27% MoM. Our regression suggests a decline in JunQ revenue (-15% QoQ). The regression-based Korea import implies downside vs. consensus of flat QoQ.

For Samsung & SK hynix, we find their combined capex has been reasonably correlated with the import data. Despite rising equipment import, their 1Q26 capex came down QoQ, likely due to seasonality and some infrastructure investments front-loaded to 4Q25. Both however have guided substantial increase in 2026 capex, and so we expect future capex to recover and likely grow even stronger than import data soon.

BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="3">15 Jun 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>6857.JP (Advantest)</td><td>O</td><td>JPY</td><td>29,420</td><td>39,200</td><td>202.1%</td><td>JPY</td><td>534.21</td><td>735.65</td><td>870.09</td><td>55.1</td><td>40.0</td><td>33.8</td></tr><tr><td>ASML (ASML)</td><td>O</td><td>USD</td><td>1,863.55</td><td>1,971.00</td><td>122.0%</td><td>USD</td><td>27.95</td><td>36.96</td><td>53.13</td><td>57.6</td><td>43.6</td><td>30.3</td></tr><tr><td>ASML.NA (ASML)</td><td>O</td><td>EUR</td><td>1,629.60</td><td>1,700.00</td><td>130.8%</td><td>EUR</td><td>24.72</td><td>32.69</td><td>46.98</td><td>65.9</td><td>49.8</td><td>34.7</td></tr><tr><td>8035.JP (Tokyo Electron)</td><td>O</td><td>JPY</td><td>72,760</td><td>59,200</td><td>161.9%</td><td>JPY</td><td>1,250.88</td><td>1,504.14</td><td>1,848.77</td><td>58.2</td><td>48.4</td><td>39.4</td></tr><tr><td>005930.KS (SEC- Samsung)</td><td>O</td><td>KRW</td><td>341,500</td><td>225,000</td><td>444.9%</td><td>KRW</td><td>6,611.53</td><td>35,740</td><td>49,548</td><td>51.7</td><td>9.6</td><td>6.9</td></tr><tr><td>005935.KS (SEC-Pref - Samsung)</td><td>O</td><td>KRW</td><td>216,000</td><td>191,250</td><td>313.9%</td><td>KRW</td><td>6,611.53</td><td>35,740</td><td>49,548</td><td>32.7</td><td>6.0</td><td>4.4</td></tr><tr><td>SMSN.LI (Samsung)</td><td>O</td><td>USD</td><td>5,400.00</td><td>3,888.00</td><td>388.9%</td><td>USD</td><td>116.15</td><td>617.62</td><td>856.24</td><td>46.5</td><td>8.7</td><td>6.3</td></tr><tr><td>000660.KS (SK hynix)</td><td>O</td><td>KRW</td><td>2,320,000</td><td>1,150,000</td><td>844.3%</td><td>KRW</td><td>60,341</td><td>286,732</td><td>385,594</td><td>38.4</td><td>8.1</td><td>6.0</td></tr><tr><td>JPL</td><td></td><td></td><td>2,549.03</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SPX</td><td></td><td></td><td>7,431.46</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EDME</td><td></td><td></td><td>1,570.59</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ASIAX</td><td></td><td></td><td>1,966.72</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EM</td><td></td><td></td><td>1,831.26</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended  
Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We rate Tokyo Electron (PT=¥59,200), ASML (PT=€1,700.00) and Advantest (PT=¥39,200) Outperform.

We rate Samsung Electronics OP with PT=KRW 225,000 and SK hynix OP with PT=KRW 1,150,000.

## DETAILS

## SOUTH KOREA SEMI EQUIPMENT IMPORTS OVERALL

- Overall, South Korea semi equipment imports were +51% YoY globally in May '26, Japan SPE was +40% (Exhibit 1, Exhibit 2).  
- MoM shows slight decline — globally -5% and -7% from Japan, and 3-month moving average sequentially was flat globally and +3% for Japan.  
- Historical data shows good correlation between the South Korea equipment imports and the combined capex of Samsung & SK hynix (Exhibit 3). 1QCY26 capex came down QoQ for both Samsung and SK hynix, despite rising equipment import data, likely due to seasonality and also as some infrastructure investments were front loaded in 4Q25 (Exhibit 4). Going forward, both companies have guided substantial increase in 2026 capex, with focus on infrastructure and strategic equipment. So we expect future capex to recover and likely grow even stronger than import data soon.

EXHIBIT 1: May South Korea imports for SPE was \$3.2bn, -5% MoM.  
![](images/7b81df4024c162b56f68f192bb307f1e6e4d31fff50b04129741e4eca73dc9cb.jpg)

<details>
<summary>line chart</summary>

| Month   | South Korea SPE Import (USD mn) | 3 per. Mov. Avg. (South Korea SPE Import) |
|---------|----------------------------------|------------------------------------------|
| Jan-20  | 1000                             | 1500                                     |
| Apr-20  | 2100                             | 1800                                     |
| Jul-20  | 2000                             | 2000                                     |
| Oct-20  | 1400                             | 1400                                     |
| Jan-21  | 2900                             | 2700                                     |
| Apr-21  | 3000                             | 2800                                     |
| Jul-21  | 2400                             | 2500                                     |
| Oct-21  | 1700                             | 1800                                     |
| Jan-22  | 2700                             | 2300                                     |
| Apr-22  | 2300                             | 2100                                     |
| Jul-22  | 2500                             | 2400                                     |
| Oct-22  | 1800                             | 2100                                     |
| Jan-23  | 3000                             | 2300                                     |
| Apr-23  | 2600                             | 2400                                     |
| Jul-23  | 2400                             | 2300                                     |
| Oct-23  | 1500                             | 1600                                     |
| Jan-24  | 1900                             | 1900                                     |
| Apr-24  | 1800                             | 1900                                     |
| Jul-24  | 1700                             | 1800                                     |
| Oct-24  | 2600                             | 2100                                     |
| Jan-25  | 3100                             | 2500                                     |
| Apr-25  | 3400                             | 2600                                     |
| Jul-25  | 2600                             | 2300                                     |
| Oct-25  | 3100                             | 2400                                     |
| Jan-26  | 3300                             | 2700                                     |
| Apr-26  | 3800                             | 3400                                     |
</details>

Source: Korea Customs Services, Bernstein analysis

EXHIBIT 2: May South Korea imports for Japanese SPE was \$651mn, -7% MoM.  
![](images/6d3744103a7aff767dedf4accce31df736896f058acd24db0c5566a3f2d3f82a.jpg)

<details>
<summary>line chart</summary>

| Month   | South Korea SPE Import (USD mn) | 3 per. Mov. Avg. (South Korea SPE Import) (USD mn) |
|---------|----------------------------------|----------------------------------------------------|
| Jan-20  | 250                              | 400                                                |
| Apr-20  | 500                              | 450                                                |
| Jul-20  | 450                              | 420                                                |
| Oct-20  | 400                              | 400                                                |
| Jan-21  | 700                              | 650                                                |
| Apr-21  | 650                              | 600                                                |
| Jul-21  | 500                              | 550                                                |
| Oct-21  | 450                              | 500                                                |
| Jan-22  | 600                              | 550                                                |
| Apr-22  | 700                              | 600                                                |
| Jul-22  | 500                              | 550                                                |
| Oct-22  | 450                              | 500                                                |
| Jan-23  | 600                              | 450                                                |
| Apr-23  | 550                              | 475                                                |
| Jul-23  | 500                              | 450                                                |
| Oct-23  | 350                              | 375                                                |
| Jan-24  | 450                              | 475                                                |
| Apr-24  | 475                              | 450                                                |
| Jul-24  | 500                              | 475                                                |
| Oct-24  | 600                              | 525                                                |
| Jan-25  | 800                              | 650                                                |
| Apr-25  | 550                              | 600                                                |
| Jul-25  | 600                              | 550                                                |
| Oct-25  | 450                              | 475                                                |
| Jan-26  | 750                              | 650                                                |
| Apr-26  | 850                              | 750                                                |
</details>

Source: Korea Customs Services, Bernstein analysis

EXHIBIT 3: South Korea SPE monthly import data has good directional correlation with Samsung and SK hynix's quarterly capex.  
![](images/30f3f18d6559cca9016bd41fdbf0f9c6ba1af075915fb09ab1c8d515e70963b4.jpg)

<details>
<summary>line chart</summary>

| Date   | SEC + SK hynix Capex (Quarterly/3) | South Korea SPE Import |
|--------|-------------------------------------|------------------------|
| Jan-20 | 3.1                                 | 1.9                    |
| Apr-20 | 3.2                                 | 4.2                    |
| Jul-20 | 3.1                                 | 4.1                    |
| Oct-20 | 3.8                                 | 2.8                    |
| Jan-21 | 4.2                                 | 5.9                    |
| Apr-21 | 4.8                                 | 6.1                    |
| Jul-21 | 4.9                                 | 5.2                    |
| Oct-21 | 4.1                                 | 3.5                    |
| Jan-22 | 4.3                                 | 5.5                    |
| Apr-22 | 4.3                                 | 4.5                    |
| Jul-22 | 4.3                                 | 4.8                    |
| Oct-22 | 5.2                                 | 3.7                    |
| Jan-23 | 4.3                                 | 6.0                    |
| Apr-23 | 4.5                                 | 5.3                    |
| Jul-23 | 3.7                                 | 4.8                    |
| Oct-23 | 4.3                                 | 3.0                    |
| Jan-24 | 4.1                                 | 4.6                    |
| Apr-24 | 3.4                                 | 3.8                    |
| Jul-24 | 3.4                                 | 3.9                    |
| Oct-24 | 5.5                                 | 5.3                    |
| Jan-25 | 5.6                                 | 6.1                    |
| Apr-25 | 4.1                                 | 4.8                    |
| Jul-25 | 4.1                                 | 5.6                    |
| Oct-25 | 5.3                                 | 6.1                    |
| Jan-26 | 6.0                                 | 6.3                    |
| Apr-26 | 6.5                                 | 7.7                    |
</details>

Source: Company disclosures, Korea Customs Services, Bernstein analysis.

EXHIBIT 4: 1QCY26 capex came down QoQ for both Samsung and SK hynix due to seasonality and some front loaded infrastructure investments in 4Q25, but we expect their capex will pick up again soon.  
![](images/adadddbb331fcf7d58a544458397016417231225217256efe7cbfe669050858d.jpg)

<details>
<summary>bar-line hybrid</summary>

Capex (KRW B)
| Quarter | Samsung (KRW B) | SK hynix (KRW B) | KR SPE Import (RHS) |
| :--- | :--- | :--- | :--- |
| 1Q24 | 9000 | 3000 | 8000 |
| 2Q24 | 9000 | 2500 | 8000 |
| 3Q24 | 10500 | 3500 | 8500 |
| 4Q24 | 16000 | 7500 | 11000 |
| 1Q25 | 11500 | 6500 | 11500 |
| 2Q25 | 9500 | 4500 | 9500 |
| 3Q25 | 7800 | 4500 | 9500 |
| 4Q25 | 19500 | 11500 | 11500 |
| 1Q26 | 10500 | 7500 | 13500 |
</details>

Source: Company reports, Korea Customs Service, Bernstein estimates and analysis

## ADVANTEST – SOUTH KOREA TESTER IMPORT DATA

- Advantest memory tester revenue is highly correlated to the Korean tester import (Exhibit 6). Korean import of testers from Japan and Malaysia was +5% MoM and +103% YoY. 3-month average was +2% MoM (Exhibit 5).  
- Our regression indicates JunQ Korean sales for Advantest of +84% QoQ (Exhibit 7, Exhibit 8), which suggest upside to JunQ consensus for Advantest corporate revenue of +3%.

EXHIBIT 5: May tester imports from Japan and Malaysia collectively was +5% MoM.  
![](images/9fcad00a77cdd434fc38e10c89735e1ee9aba0c527361130f370343484438821.jpg)

<details>
<summary>line chart</summary>

| Month    | Testers (Japan/Malaysia) | 3 per. Mov. Avg. (Testers (Japan/Malaysia)) |
| -------- | ------------------------ | ------------------------------------------ |
| Jan-20   | ~40                      | ~60                                        |
| Apr-20   | ~35                      | ~55                                        |
| Jul-20   | ~70                      | ~90                                        |
| Oct-20   | ~80                      | ~100                                       |
| Jan-21   | ~70                      | ~85                                        |
| Apr-21   | ~50                      | ~70                                        |
| Jul-21   | ~60                      | ~65                                        |
| Oct-21   | ~55                      | ~60                                        |
| Jan-22   | ~70                      | ~75                                        |
| Apr-22   | ~100                     | ~80                                        |
| Jul-22   | ~90                      | ~75                                        |
| Oct-22   | ~80                      | ~70                                        |
| Jan-23   | ~60                      | ~65                                        |
| Apr-23   | ~40                      | ~55                                        |
| Jul-23   | ~90                      | ~70                                        |
| Oct-23   | ~120                     | ~95                                        |
| Jan-24   | ~130                     | ~105                                       |
| Apr-24   | ~140                     | ~120                                   

[中间内容因长度限制已省略]

nce system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
