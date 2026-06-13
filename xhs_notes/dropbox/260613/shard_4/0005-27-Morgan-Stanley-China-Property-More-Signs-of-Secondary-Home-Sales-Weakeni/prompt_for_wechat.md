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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`摩根斯坦利`。标题格式建议：`# 摩根斯坦利：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## China Property | Asia Pacific

# More Signs of Secondary Home Sales Weakening

## Key Takeaways

25-city secondary real-time home sales softened to 9.2% y-y MTD as of June 10 (vs. 30% in April, 26% in May) despite a lower base from Dragon Boat holiday.  
Low-tier 2 cities (Nanchang, Foshan, Nantong, Dongguan, Ningbo, Xi'an) saw fast deceleration and select cities (Tianjin, Changsha, Chengdu) turned negative y-y.  
Cities with policy easing in late April saw divergence - Suzhou/Wuhan remained robust, while Guangzhou/Shenzhen/Foshan decelerated by double-digit ppts.  
This is consistent with our call for milder y-y in June, with potential to turn negative y-y in 3Q amid diminishing policy effects and pent-up demand...  
… leading to a broadly soft m-m home price downtrend in 2026–27, though select Tier 1 cities may see a mild uptrend due to better destocking progress.

Stay selective: In our recent insight report - An Inflection or Another False Start? - we emphasized that the unexpected rebound in secondary home sales in March-April may have been due to the release of pent-up demand from 4Q25 on the back of HPR/HPF mortgage easing and less-panicky resident sentiment. With increasing uncertainty around sales sustainability, we still see industry risk/reward skewing to the downside despite an 18% share price pullback since mid-May (vs. HSI -8%).

We suggest closely monitoring sales volumes, home prices, secondary listing volumes, transaction mixes, and rental rates in June-August to assess whether a market inflection is forming. We stay prudent, and continue to recommend sticking to beneficiaries with both industry beta and self-help alpha. CR Land (1109.HK) remains our Top Pick, followed by C&D (1908.HK), as both offer solid EPS outlooks, attractive dividend yields, and medium-term re-rating potential even absent notable recovery in the physical market.

Exhibit 1: Bingshan 25-city secondary real-time home sales continued to decelerate, to $+9\%$ y-y in MTD June  
![](images/64753226fe9b4e7f9a23debd72e14d4a989b8f3091859f15b6a1a4b1b5a787cc.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Month    | 25-city monthly secondary sales (k units) | Y-Y (%) |
|----------|---------------------------------------------|---------|
| Oct-21   | 90                                          | 0       |
| Nov-21   | 100                                         | 0       |
| Dec-21   | 110                                         | 0       |
| Jan-22   | 120                                         | 0       |
| Feb-22   | 130                                         | 0       |
| Mar-22   | 140                                         | 0       |
| Apr-22   | 150                                         | 0       |
| May-22   | 160                                         | 0       |
| Jun-22   | 170                                         | 0       |
| Jul-22   | 180                                         | 0       |
| Aug-22   | 190                                         | 0       |
| Sep-22   | 200                                         | 0       |
| Oct-22   | 210                                         | 0       |
| Nov-22   | 220                                         | 0       |
| Dec-22   | 230                                         | 0       |
| Jan-23   | 240                                         | 0       |
| Feb-23   | 250                                         | 0       |
| Mar-23   | 260                                         | 0       |
| Apr-23   | 270                                         | 0       |
| May-23   | 280                                         | 0       |
| Jun-23   | 290                                         | 0       |
| Jul-23   | 300                                         | 0       |
| Aug-23   | 310                                         | 0       |
| Sep-23   | 320                                         | 0       |
| Oct-23   | 330                                         | 0       |
| Nov-23   | 340                                         | 0       |
| Dec-23   | 350                                         | 0       |
| Jan-24   | 360                                         | 0       |
| Feb-24   | 370                                         | 0       |
| Mar-24   | 380                                         | 0       |
| Apr-24   | 390                                         | 0       |
| May-24   | 400                                         | 0       |
| Jun-24   | 410                                         | 0       |
| Jul-24   | 420                                         | 0       |
| Aug-24   | 430                                         | 0       |
| Sep-24   | 440                                         | 0       |
| Oct-24   | 450                                         | 0       |
| Nov-24   | 460                                         | 0       |
| Dec-24   | 470                                         | 0       |
| Jan-25   | 480                                         | 0       |
| Feb-25   | 490                                         | 0       |
| Mar-25   | 500                                         | 0       |
| Apr-25   | 510                                         | 0       |
| May-25   | 520                                         | 0       |
| Jun-25   | 530                                         | 0       |
| Jul-25   | 540                                         | 0       |
| Aug-25   | 550                                         | 0       |
| Sep-25   | 560                                         | 0       |
| Oct-25   | 570                                         | 0       |
| Nov-25   | 580                                         | 0       |
| Dec-25   | 590                                         | 0       |
| Jan-26   | 600                                         | 0       |
| Feb-26   | 610                                         | 0       |
| Mar-26   | 620                                         | 0       |
| Apr-26   | 630                                         | 0       |
| May-26   | 640                                         | 0       |
| Jun-26   | 650                                         | 0       |
</details>

Source: Bingshan, MS

Exhibit 2: Chinese New Year-adjusted cumulative secondary real-time home sales fell $\sim 1\%$ y-y in those cities  
![](images/96accda32a32145fd2a60f10a72fbe914c93f970f2ef3853a337d87c23c11912.jpg)

<details>
<summary>line chart</summary>

| Period | 2023  | 2024  | 2025  | 2026  |
|--------|-------|-------|-------|-------|
| T-20   | ~90%  | ~50%  | ~-30% | ~-10% |
| T-18   | ~70%  | ~45%  | ~-25% | ~-15% |
| T-16   | ~60%  | ~40%  | ~-20% | ~-20% |
| T-14   | ~50%  | ~35%  | ~-15% | ~-25% |
| T-12   | ~40%  | ~30%  | ~-10% | ~-30% |
| T-10   | ~30%  | ~35%  | ~-5%  | ~-35% |
| T-8    | ~25%  | ~30%  | ~0%   | ~-35% |
| T-6    | ~20%  | ~35%  | ~5%   | ~-35% |
| T-4    | ~15%  | ~30%  | ~10%  | ~-35% |
| T-2    | ~10%  | ~25%  | ~15%  | ~-35% |
| T      | ~5%   | ~20%  | ~20%  | ~-35% |
| T+2    | ~0%   | ~15%  | ~25%  | ~-35% |
| T+4    | ~5%   | ~10%  | ~30%  | ~-35% |
| T+6    | ~10%  | ~5%   | ~35%  | ~-35% |
| T+8    | ~15%  | ~0%   | ~40%  | ~-35% |
| T+10   | ~20%  | ~5%   | ~45%  | ~-35% |
| T+12   | ~25%  | ~10%  | ~50%  | ~-35% |
| T+14   | ~30%  | ~15%  | ~55%  | ~-35% |
| T+16   | ~35%  | ~20%  | ~60%  | ~-35% |
| T+18   | ~40%  | ~25%  | ~65%  | ~-35% |
| T+20   | ~45%  | ~30%  | ~70%  | ~-35% |
</details>

Source: Bingshan, MS

MS ASIA LIMITED+

Stephen Cheung, CFA

Equity Analyst

Stephen.Cheung@morganstanley.com

+852 3963-0385

Cara Zhu

Equity Analyst

Cara.Zhu@morganstanley.com

+852 2848-7117

## Asia Summer School 2026

![](images/2319a5e31c7cfc643fa7c92099b62daab20fcaa2dffd15e4f96e219594d62838.jpg)

## CHINA PROPERTY

Asia Pacific

Industry View

In-Line

## Related reports:

1. An Inflection or Another False Start? (18 May 2026)  
2. Diverging Home Price Trends Continued in May (2 June 2026)  
3. Managed Housing Downcycle to Last Another Two Years (25 January 2026)  
4. 2026 Outlook: Physical Market Stays  
Challenging; Diverging Outperformance of Alpha Plays (10 December 2025)

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

Exhibit 3: Bingshan 25-city secondary real-time home sales decelerated rapidly to 9% y-y MTD in June, from 30% in April and 26% in May

<table><tr><td rowspan="2"></td><td colspan="25">Residential property sales (units)</td><td></td></tr><tr><td>Beijing 北京</td><td>Shanghai 上海</td><td>Shenzhen 深圳</td><td>Guangzhou 广州</td><td>Chengdu 成都</td><td>Shenyang 沈阳</td><td>Dalian 大连</td><td>Foshan 佛山</td><td>Dongguan 东莞</td><td>Zhuhai 珠海</td><td>Changsha 长沙</td><td>Wuhan 武汉</td><td>Qingdao 青岛</td><td>Xi&#x27;an 西安</td><td>Hangzhou 杭州</td><td>Ningbo 宁波</td><td>Nanchang 南昌</td><td>Xiamen 厦门</td><td>Tianjin 天津</td><td>Wuxi 无锡</td><td>Suzhou 苏州</td><td>Hefei 合肥</td><td>Nanjing 南京</td><td>Xuzhou 徐州</td><td>Nantong 南通</td><td>25 Cities 25城</td></tr><tr><td colspan="26">Secondary sales (real-time)</td><td></td></tr><tr><td>Jan-26</td><td>16,815</td><td>24,350</td><td>5,495</td><td>9,630</td><td>17,173</td><td>7,630</td><td>2,856</td><td>5,364</td><td>3,215</td><td>2,147</td><td>4,548</td><td>9,550</td><td>5,175</td><td>8,692</td><td>5,353</td><td>5,264</td><td>2,790</td><td>2,146</td><td>11,969</td><td>3,766</td><td>5,812</td><td>7,609</td><td>9,173</td><td>1,600</td><td>1,918</td><td>180,040</td></tr><tr><td>Feb-26</td><td>7,486</td><td>11,127</td><td>1,874</td><td>3,549</td><td>8,954</td><td>3,783</td><td>1,624</td><td>2,048</td><td>958</td><td>984</td><td>2,222</td><td>4,245</td><td>2,610</td><td>3,944</td><td>2,202</td><td>2,563</td><td>1,668</td><td>875</td><td>5,583</td><td>1,677</td><td>2,536</td><td>3,826</td><td>4,298</td><td>1,236</td><td>1,528</td><td>83,400</td></tr><tr><td>Mar-26</td><td>22,182</td><td>35,950</td><td>7,341</td><td>13,136</td><td>29,112</td><td>14,529</td><td>5,464</td><td>7,470</td><td>4,309</td><td>3,129</td><td>7,489</td><td>15,224</td><td>8,415</td><td>14,050</td><td>8,728</td><td>10,034</td><td>4,487</td><td>3,043</td><td>19,190</td><td>7,104</td><td>9,422</td><td>13,051</td><td>14,007</td><td>2,794</td><td>3,130</td><td>282,790</td></tr><tr><td>Apr-26</td><td>16,891</td><td>26,428</td><td>6,250</td><td>11,311</td><td>23,268</td><td>13,136</td><td>4,392</td><td>6,245</td><td>4,390</td><td>2,794</td><td>5,901</td><td>13,496</td><td>7,667</td><td>11,324</td><td>7,589</td><td>8,187</td><td>3,811</td><td>2,575</td><td>16,823</td><td>5,913</td><td>7,963</td><td>10,241</td><td>10,389</td><td>2,430</td><td>2,391</td><td>231,805</td></tr><tr><td>May-26</td><td>16,403</td><td>26,525</td><td>6,201</td><td>11,737</td><td>22,280</td><td>13,212</td><td>4,170</td><td>6,849</td><td>4,010</td><td>2,550</td><td>5,888</td><td>12,891</td><td>6,946</td><td>9,941</td><td>7,416</td><td>8,061</td><td>3,631</td><td>2,458</td><td>14,385</td><td>5,617</td><td>7,704</td><td>9,518</td><td>9,650</td><td>2,149</td><td>2,478</td><td>222,670</td></tr><tr><td>Jun-26</td><td>5,040</td><td>7,278</td><td>1,670</td><td>3,376</td><td>6,292</td><td>3,851</td><td>1,225</td><td>1,974</td><td>1,207</td><td>782</td><td>1,648</td><td>3,945</td><td>2,045</td><td>2,789</td><td>2,060</td><td>2,381</td><td>973</td><td>721</td><td>3,833</td><td>1,570</td><td>2,300</td><td>2,838</td><td>2,510</td><td>709</td><td>653</td><td>63,670</td></tr><tr><td colspan="26">Y-Y</td><td></td></tr><tr><td>Jan-26</td><td>66%</td><td>64%</td><td>78%</td><td>66%</td><td>37%</td><td>37%</td><td>78%</td><td>103%</td><td>123%</td><td>93%</td><td>43%</td><td>79%</td><td>90%</td><td>83%</td><td>31%</td><td>79%</td><td>88%</td><td>68%</td><td>47%</td><td>119%</td><td>106%</td><td>97%</td><td>102%</td><td>105%</td><td>108%</td><td>68%</td></tr><tr><td>Feb-26</td><td>-34%</td><td>-40%</td><td>-52%</td><td>-49%</td><td>-54%</td><td>-60%</td><td>-37%</td><td>-39%</td><td>-51%</td><td>-22%</td><td>-54%</td><td>-47%</td><td>-42%</td><td>-46%</td><td>-63%</td><td>-48%</td><td>-19%</td><td>-34%</td><td>-53%</td><td>-45%</td><td>-45%</td><td>-34%</td><td>-38%</td><td>-7%</td><td>-11%</td><td>-46%</td></tr><tr><td>Mar-26</td><td>13%</td><td>15%</td><td>-6%</td><td>2%</td><td>8%</td><td>13%</td><td>30%</td><td>25%</td><td>17%</td><td>32%</td><td>5%</td><td>26%</td><td>15%</td><td>31%</td><td>-25%</td><td>28%</td><td>39%</td><td>19%</td><td>10%</td><td>52%</td><td>24%</td><td>45%</td><td>35%</td><td>90%</td><td>67%</td><td>17%</td></tr><tr><td>Apr-26</td><td>30%</td><td>25%</td><td>22%</td><td>22%</td><td>15%</td><td>27%</td><td>44%</td><td>54%</td><td>74%</td><td>45%</td><td>13%</td><td>39%</td><td>33%</td><td>46%</td><td>-15%</td><td>60%</td><td>57%</td><td>39%</td><td>26%</td><td>70%</td><td>41%</td><td>47%</td><td>26%</td><td>72%</td><td>44%</td><td>30%</td></tr><tr><td>May-26</td><td>17%</td><td>20%</td><td>27%</td><td>29%</td><td>15%</td><td>25%</td><td>24%</td><td>53%</td><td>47%</td><td>34%</td><td>22%</td><td>31%</td><td>24%</td><td>29%</td><td>15%</td><td>62%</td><td>60%</td><td>38%</td><td>11%</td><td>45%</td><td>40%</td><td>38%</td><td>14%</td><td>50%</td><td>46%</td><td>26%</td></tr><tr><td>Jun-26</td><td>4%</td><td>-3%</td><td>17%</td><td>6%</td><td>-1%</td><td>14%</td><td>16%</td><td>22%</td><td>24%</td><td>16%</td><td>-5%</td><td>29%</td><td>6%</td><td>9%</td><td>3%</td><td>37%</td><td>25%</td><td>21%</td><td>-9%</td><td>24%</td><td>37%</td><td>22%</td><td>3%</td><td>58%</td><td>19%</td><td>9%</td></tr><tr><td>6M26</td><td>16%</td><td>14%</td><td>10%</td><td>12%</td><td>2%</td><td>8%</td><td>24%</td><td>35%</td><td>36%</td><td>34%</td><td>3%</td><td>23%</td><td>18%</td><td>24%</td><td>-15%</td><td>32%</td><td>42%</td><td>26%</td><td>5%</td><td>42%</td><td>29%</td><td>35%</td><td>22%</td><td>59%</td><td>43%</td><td>16%</td></tr></table>

Note: June 2026 sales represent MTD sales as of June 10. Shanghai has disclosed data until June 7, and we pro-rata for June 8-10. Source: Bingshan, MS.

## Valuation Methodology and Risks

## China Resources Land Ltd. (1109.HK)

Our HK\$60.88/share 2026e NAV comprises HK\$15.62 of development properties (DCF, 8.0% WACC), HK\$55.22 of investment properties (cap rate 5-8%) and HK\$9.96 of net debt. To this we apply a 30% discount based on our developers' scorecard, comprising landbank (with a 8/10 score), execution (8), scale (9), growth (8), profitability (8), financing (10) and leverage (10). We use 30-45% discounts in our coverage.

## Risks to Upside

■ Stronger-than-expected contracted sales.  
■ Accelerated openings of new malls.

## Risks to Downside

■ Weaker-than-expected contracted sales.  
■ Slower-than-expected openings of new shopping malls.

## C&D International Investment Group Ltd (1908.HK)

Our HK\$32.59/share 2026e NAV comprises HK\$25.65/share of development properties (DCF, 8.2% WACC), HK\$1.14/share of other business and HK\$5.79/share of net cash. To this we apply a 35% discount based on our developers' scorecard, comprising landbank (with a 8/10 score), execution (8), scale (8), growth (8), profitability (7), financing (9), and leverage (8). We use 30-45% discounts in our coverage.

## Risks to Upside

■ Stronger-than-expected contracted sales.  
■ Stronger-than-expected gross margin.

## Risks to Downside

■ Weaker-than-expected gross margin.  
■ Slower-than-expected land acquisitions.

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Asia Limited (which accepts the responsibility for its contents) and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents), and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS, and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or 

[中间内容因长度限制已省略]

Stanley International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

MS Hong Kong Securities Limited is the liquidity provider/market maker for securities of China Overseas Land & Investment Ltd., China Resources Land Ltd., China Vanke Company Ltd., Longfor Group Holdings Ltd. listed on the Stock Exchange of Hong Kong Limited. An updated list can be found on HKEx website: http://www.hkex.com.hk.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: China Property

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/11/2026)</td></tr></table>

Stephen Cheung, CFA

<table><tr><td>C&amp;D International Investment Group Ltd (1908.HK)</td><td>O (08/01/2024)</td><td>HK$15.19</td></tr><tr><td>China Jinmao Holdings Group Ltd (0817.HK)</td><td>E (03/28/2024)</td><td>HK$1.56</td></tr><tr><td>China Merchants Shekou Industrial Zone (001979.SZ)</td><td>E (05/06/2021)</td><td>Rmb8.27</td></tr><tr><td>China Overseas Land &amp; Investment Ltd. (0688.HK)</td><td>E (01/20/2025)</td><td>HK$15.62</td></tr><tr><td>China Resources Land Ltd. (1109.HK)</td><td>O (01/02/2019)</td><td>HK$36.88</td></tr><tr><td>China Vanke Company Ltd. (2202.HK)</td><td>E (11/07/2023)</td><td>HK$2.62</td></tr><tr><td>China Vanke Company Ltd. (000002.SZ)</td><td>U (11/30/2022)</td><td>Rmb3.12</td></tr><tr><td>Gemdale Corporation (600383.SS)</td><td>U (01/28/2026)</td><td>Rmb2.48</td></tr><tr><td>Greentown China Holdings (3900.HK)</td><td>U (08/26/2025)</td><td>HK$8.31</td></tr><tr><td>Longfor Group Holdings Ltd. (0960.HK)</td><td>E (05/17/2024)</td><td>HK$8.55</td></tr><tr><td>Poly Developments and Holdings Group (600048.SS)</td><td>E (05/17/2024)</td><td>Rmb5.15</td></tr><tr><td>Seazen Group Ltd (1030.HK)</td><td>O (01/28/2026)</td><td>HK$1.66</td></tr><tr><td>Seazen Holdings Company Ltd. (601155.SS)</td><td>O (11/03/2025)</td><td>Rmb11.68</td></tr><tr><td>Yuexiu Property Co Ltd (0123.HK)</td><td>O (09/27/2024)</td><td>HK$4.30</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
