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
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Property Data Monitor

Mainland China: Divergence between primary & secondary sales; HK: Weekend primary sales reached a 2.5-year high

# Mainland China

- Leading indicator #1) The Centraline tier-1 Cities' secondary asking price index mildly rose from 19.0 last week to 19.3 (Figure 1). Shenzhen saw the largest W/W increase (up 1.0 to 28.1), likely due to policy easing in late April.   
- Leading indicator #2) The Centaline manager confidence index stayed flattish at 57 (Figure 2).   
- 60-city primary sales registrations dropped 7% Y/Y (last week: +1%) (more). Tier-1 / 2 Cities outperformed (-3% Y/Y). YTD, 20-city sales have dropped 10% Y/Y.   
- 12-city secondary sales registrations increased 16% Y/Y (last week: +25% (Figure 5)). YTD, 12-city secondary sales have risen 3% Y/Y (Shanghai +9%; Beijing +4%; Shenzhen +1%).   
- Southbound holdings rose 0.01% W/W (Table 5): Yuexiu +0.7%; Greentown, C&D, COLI, Country Garden all +0.3%.   
- Share price moves (Figure 14): The sector rose 14% last week, significantly outperforming the HSI (+1%), due to solid data from Golden Week (more in Golden Week stayed solid; target \~20% upside). The outperformers were Longfor (+22%), Yuexiu & COLI (both +18%), and Jinmao (+17%). The underperformer was Country Garden (-2%).   
- JPM top picks: COLI (more in A laggard poised to outperform), CR Land, Jinmao & CR Mixc.

# Hong Kong SAR

- The home price index rose 0.2% W/W (Figure 10). Home prices have risen 8.0% YTD and are just 2% away from reaching our 2026 home price forecast of 10-15%.   
- Secondary transactions in the top 35 estates totaled 78 units, down 24% W/W but up 22% Y/Y (Figure 9).   
- The Centa Valuation Index (CVI) (Figure 11) rose to 89.3 (last week: 85.3). This is a leading indicator that home price growth may continue (a reading of >60 = banks revising up property valuations).   
- The Centa Salesman Index (CSI) (Figure 12) stays elevated at 69.7 (last week: 70.3). A reading of $>50 =$ sentiment is positive and property prices are likely to rise.   
- SHKP & Henderson's launches achieved 100% sell-through rates: The primary market saw 560 transactions over the weekend, the highest in the past 2.5 years. 3 primary launches were all 100% sold out, including the 1st batch of Lime Spark (by SHKP; in Tseun Wan) (154 units; ASP 14% higher than secondary), Highwood Ph2 (by Henderson; in To Kwa Wan) (150 units, ASP 14% higher than secondary), One Victoria Cove Ph3 (led by Henderson;

# Mainland China/Hong Kong Property & Conglomerates

Karl Chan AC

(852) 2800-8513

karl.chan@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Jocelyn Gao

(852) 2800-8529

jocelyn.gao@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Venus Choi

(852) 2800-8599

venus.choi@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

# APAC Credit Research

Alvin Au AC

(852) 2800-8533

alvin.au@JPM.com

JPM Securities (Asia Pacific) Limited

Soo Chong Lim

(852) 2800-7387

soochong.lim@JPM.com

JPM Securities (Asia Pacific) Limited

Shirley Yau

(852) 2800-0566

shirley.yau@JPM.com

JPM Securities (Asia Pacific) Limited

in Hung Hom) (130 units; ASP 20% higher than secondary). Meanwhile, PORTO (by Wang On; in Ap Lei Chau) launched the first batch (86 units; ASP 31% higher than secondary), and it was 51% sold.

- Southbound holdings rose 0.07% W/W (Table 5): Hang Lung +0.5%; Henderson +0.3%.   
- Share price moves (Figure 15): The sector rose 4% last week, outperforming the HSI (1%). The outperformers were CK Hutchison (+11%; due to disposal of 49% stake in VodafoneThree UK), NWD (+10%) and Wharf Holdings (+9%). The underperformers were MTRC and Hang Lung (both +1%).   
- JPM top picks: Developers – SHKP & Sino; landlords – Swire Prop & Hang Lung; conglomerates – JM & CKH.

# Credit views (by Alvin Au)

- The JACI China HY Property Index rose 1.7% last week (vs China HY: +0.7%), bringing YTD returns to +1.3%.   
- Hysan: Swire Properties' 1Q26 data indicated that HK retail tenant sales growth accelerated from +6% yoy in 4Q25 to +13% in 1Q26. For HK office, Swire expects negative rental reversion to narrow at Pacific Place in 2H26, on the back of increased leasing activities and stabilizing office rents in Central (see details in equity report). We believe a solid HK retail market and gradual stabilization of office segment is positive for Hysan (covered by Soo Chong Lim), and we prefer Hysan 7.2% perp (105.825, 5.7% ytc, z+189) as the best credit to ride on the recovery of HK commercial property market.   
- CR Land: REDD reported last week that China Resources Land (CR Land) plans to inject Rmb10bn-15bn of shopping mall assets into public REITs in 2026, and it targets to issue a total of Rmb60bn in public REITs by 2030. \~60% of the proceeds from REITs will be used for construction and maintenance spending on existing projects, and \~30% will be allocated for M&A activities. We note that commercial REITs have become an emerging funding channel for developers with material IP resources, such as CR Land and Seazen, etc.

# Table Of Contents

Mainland China.... 1

Hong Kong SAR 1

Credit views (by Alvin Au) 2

1. Mainland China – Leading indicators.... 4

2. Mainland China – Weekly Primary Sales 5

3. Mainland China – Weekly Secondary Sales.... 7

4. Hong Kong – Residential Market Update 9

5. Hong Kong – Tourist Arrivals & Resident Departures..... 13

6. Share price update 14

7. Credit recommendations .... 18

8. Equity valuation summary 19

# 1. Mainland China – Leading indicators

Figure 1: Centraline secondary asking price index vs. NBS secondary home price index M/M in tier-1 Cities   
![](images/8581aaa9832701b8459c309637850832fa3c922ca43d3e8f938626c45d5085c0.jpg)

<details>
<summary>line</summary>

| Date     | Tier-1 Cities' secondary asking price index | Tier-1 Cities' secondary home price M/M change |
|----------|---------------------------------------------|--------------------------------------------------|
| Apr-23   | ~30                                         | ~0.8%                                            |
| May-23   | ~28                                         | ~0.6%                                            |
| Jun-23   | ~25                                         | ~0.4%                                            |
| Jul-23   | ~27                                         | ~0.6%                                            |
| Aug-23   | ~30                                         | ~0.8%                                            |
| Sep-23   | ~28                                         | ~0.6%                                            |
| Oct-23   | ~25                                         | ~0.4%                                            |
| Nov-23   | ~20                                         | ~0.2%                                            |
| Dec-23   | ~18                                         | ~0.0%                                            |
| Jan-24   | ~20                                         | ~0.2%                                            |
| Feb-24   | ~25                                         | ~0.4%                                            |
| Mar-24   | ~28                                         | ~0.6%                                            |
| Apr-24   | ~25                                         | ~0.4%                                            |
| May-24   | ~20                                         | ~0.2%                                            |
| Jun-24   | ~18                                         | ~0.0%                                            |
| Jul-24   | ~25                                         | ~0.2%                                            |
| Aug-24   | ~28                                         | ~0.4%                                            |
| Sep-24   | ~35                                         | ~0.6%                                            |
| Oct-24   | ~37                                         | ~0.8%                                            |
| Nov-24   | ~30                                         | ~0.6%                                            |
| Dec-24   | ~28                                         | ~0.4%                                            |
| Jan-25   | ~25                                         | ~0.2%                                            |
| Feb-25   | ~28                                         | ~0.4%                                            |
| Mar-25   | ~25                                         | ~0.6%                                            |
| Apr-25   | ~20                                         | ~0.4%                                            |
| May-25   | ~18                                         | ~0.2%                                            |
| Jun-25   | ~15                                         | ~0.0%                                            |
| Jul-25   | ~18                                         | ~0.2%                                            |
| Aug-25   | ~20                                         | ~0.4%                                            |
| Sep-25   | ~18                                         | ~0.6%                                            |
| Oct-25   | ~15                                         | ~0.4%                                            |
| Nov-25   | ~18                                         | ~0.6%                                            |
| Dec-25   | ~15                                         | ~0.4%                                            |
| Jan-26   | ~18                                         | ~0.6%                                            |
| Feb-26   | ~25                                         | ~0.8%                                            |
| Mar-26   | ~30                                         | ~1.0%                                            |
| Apr-26   | ~35                                         | ~1.2%                                            |
| May-26   | ~30                                         | ~1.0%                                            |
</details>

Source: Centraline, Wind, NBS. Note: The asking price index represents the percentage of projects with home price increases. For example, an index of 20 means that 20% of projects raise prices (while 80% do not).

Figure 2: Centraline secondary manager confidence index in tier-1 Cities vs. three-month rolling secondary sales   
![](images/7d86cce9b3d08147d9d2d985b1793af3189c5fc75c889efc370b08b14a5460ca.jpg)

<details>
<summary>line</summary>

| Date    | Sales manager confidence index | Sales 3-month rolling Y/Y |
|---------|----------------------------------|---------------------------|
| May-21  | 58                               | 40%                       |
| Jul-21  | 55                               | 20%                       |
| Sep-21  | 40                               | -40%                      |
| Nov-21  | 45                               | -20%                      |
| Jan-22  | 50                               | 0%                        |
| Mar-22  | 55                               | 20%                       |
| May-22  | 50                               | 40%                       |
| Jul-22  | 45                               | 60%                       |
| Sep-22  | 50                               | 80%                       |
| Nov-22  | 55                               | 100%                      |
| Jan-23  | 65                               | 120%                      |
| Mar-23  | 60                               | 140%                      |
| May-23  | 55                               | 120%                      |
| Jul-23  | 50                               | 100%                      |
| Sep-23  | 45                               | 80%                       |
| Nov-23  | 50                               | 60%                       |
| Jan-24  | 55                               | 40%                       |
| Mar-24  | 60                               | 20%                       |
| May-24  | 55                               | 0%                        |
| Jul-24  | 50                               | -20%                      |
| Sep-24  | 45                               | -40%                      |
| Nov-24  | 50                               | -60%                      |
| Jan-25  | 65                               | -40%                      |
| Mar-25  | 60                               | -20%                      |
| May-25  | 55                               | 0%                        |
| Jul-25  | 50                               | 20%                       |
| Sep-25  | 45                               | 40%                       |
| Nov-25  | 50                               | 60%                       |
| Jan-26  | 55                               | 80%                       |
| Mar-26  | 60                               | 100%                      |
| May-26  | 55                               | 120%                      |
</details>

Source: Centraline, Wind. Note: The index surveys managers across the country for their judgment on the market outlook.

# 2. Mainland China – Weekly primary sales

Figure 3: 60-city weekly primary sales registrations – compared with 2019-24   
![](images/50e6bee6d0f6ae75d9eb874aeff6d4b1c362d820681f8e6a1a62b3e44ad9580e.jpg)  
Source: CREIS.

Figure 4: 60-city weekly primary sales registrations   
![](images/5ac8b6d6db2c0fb39f68ca3a9aae2a5e789adbb98047cd117a9f4f2247cad562.jpg)  
Source: CREIS.

Table 1: 60-city weekly primary sales registrations by tier 

<table><tr><td rowspan="2">Week ending</td><td colspan="5">60-City</td><td colspan="5">Tier-1</td><td colspan="5">Tier-2</td><td colspan="5">Tier-3/4</td></tr><tr><td>No. of units</td><td>Y/Y</td><td>W/W</td><td>1M rolling Y/Y</td><td>vs. 18-21 avg</td><td>No. of units</td><td>Y/Y</td><td>W/W</td><td>1M rolling Y/Y</td><td>vs. 18-21 avg</td><td>No. of units</td><td>Y/Y</td><td>W/W</td><td>1M rolling Y/Y</td><td>vs. 18-21 avg</td><td>No. of units</td><td>Y/Y</td><td>W/W</td><td>1M rolling Y/Y</td><td>vs. 18-21 avg</td></tr><tr><td>8-Mar-26</td><td>16,815</td><td>-22%↑</td><td>35%↓</td><td>-52%↓</td><td>-66%↑</td><td>1,725</td><td>-46%↑</td><td>20%↓</td><td>-62%↓</td><td>-60%↑</td><td>11,097</td><td>-17%↑</td><td>37%↓</td><td>-50%↓</td><td>-62%↑</td><td>3,993</td><td>-21%↑</td><td>36%↓</td><td>-51%↓</td><td>-75%↑</td></tr><tr><td>15-Mar-26</td><td>22,191</td><td>-6%↑</td><td>32%↓</td><td>-46%↑</td><td>-61%↑</td><td>3,550</td><td>-9%↑</td><td>106%↑</td><td>-54%↑</td><td>-32%↑</td><td>13,197</td><td>-7%↑</td><td>19%↓</td><td>-45%↑</td><td>-61%↑</td><td>5,444</td><td>-3%↑</td><td>36%↑</td><td>-45%↑</td><td>-69%↑</td></tr><tr><td>22-Mar-26</td><td>25,414</td><td>-23%↓</td><td>15%↓</td><td>-29%↑</td><td>-59%↑</td><td>3,286</td><td>-34%↓</td><td>-7%↓</td><td>-40%↑</td><td>-43%↓</td><td>17,125</td><td>-15%↓</td><td>30%↑</td><td>-25%↑</td><td>-54%↑</td><td>5,003</td><td>-37%↓</td><td>-8%↓</td><td>-31%↑</td><td>-73%↓</td></tr><tr><td>29-Mar-26</td><td>36,602</td><td>-8%↑</td><td>44%↑</td><td>-14%↑</td><td>-32%↑</td><td>5,928</td><td>4%↑</td><td>80%↑</td><td>-18%↑</td><td>42%↑</td><td>24,617</td><td>-1%↑</td><td>44%↑</td><td>-9%↑</td><td>-25%↑</td><td>6,057</td><td>-34%↑</td><td>21%↑</td><td>-26%↑</td><td>-63%↑</td></tr><tr><td>5-Apr-26</td><td>28,805</td><td>11%↑</td><td>-21%↓</td><td>-8%↑</td><td>-49%↓</td><td>6,082</td><td>30%↑</td><td>3%↓</td><td>-2%↑</td><td>53%↑</td><td>16,560</td><td>8%↑</td><td>-33%↓</td><td>-4%↑</td><td>-53%↓</td><td>6,163</td><td>4%↑</td><td>2%↓</td><td>-21%↑</td><td>-65%↓</td></tr><tr><td>12-Apr-26</td><td>18,580</td><td>-9%↓</td><td>-35%↓</td><td>-8%↓</td><td>-70%↓</td><td>3,339</td><td>4%↓</td><td>-45%↓</td><td>0%↑</td><td>-26%↓</td><td>11,293</td><td>-1%↓</td><td>-32%↑</td><td>-3%↑</td><td>-71%↓</td><td>3,948</td><td>-31%↓</td><td>-36%↓</td><td>-26%↓</td><td>-79%↓</td></tr><tr><td>19-Apr-26</td><td>21,601</td><td>8%↑</td><td>16%↑</td><td>0%↑</td><td>-68%↑</td><td>3,737</td><td>5%↑</td><td>12%↑</td><td>11%↑</td><td>-35%↓</td><td>13,370</td><td>23%↑</td><td>18%↑</td><td>6%↑</td><td>-68%↑</td><td>4,494</td><td>-18%↑</td><td>14%↑</td><td>-21%↑</td><td>-77%↑</td></tr><tr><td>26-Apr-26</td><td>22,029</td><td>-12%↓</td><td>2%↓</td><td>0%↑</td><td>-63%↑</td><td>4,303</td><td>6%↑</td><td>15%↑</td><td>13%↑</td><td>-23%↑</td><td>13,251</td><td>-10%↓</td><td>-1%↓</td><td>4%↓</td><td>-62%↑</td><td>4,475</td><td>-27%↓</td><td>0%↓</td><td>-18%↑</td><td>-76%↑</td></tr><tr><td>3-May-26</td><td>22,468</td><td>1%↑</td><td>2%↑</td><td>-3%↓</td><td>-63%↓</td><td>4,216</td><td>12%↑</td><td>-2%↓</td><td>7%↓</td><td>-14%↑</td><td>13,627</td><td>12%↑</td><td>3%↑</td><td>5%↑</td><td>-63%↓</td><td>4,625</td><td>-26%↑</td><td>3%↑</td><td>-26%↓</td><td>-75%↑</td></tr><tr><td>10-May-26</td><td>19,317</td><td>-7%↓</td><td>-14%↓</td><td>-3%↑</td><td>-69%↓</td><td>3,355</td><td>-3%↓</td><td>-20%↓</td><td>5%↓</td><td>-33%↓</td><td>11,351</td><td>-3%↓</td><td>-17%↓</td><td>4%↓</td><td>-70%↓</td><td>4,611</td><td>-18%↑</td><td>0%↓</td><td>-22%↑</td><td>-77%↓</td></tr></table>

Source: CREIS.

# 3. Mainland China – Weekly secondary sales

Figure 5: 12-city daily secondary sales registrations   
![](images/c2feb1055cb679bfc0647333cef6ffe326239a98b34016982a34a47fe89a060a.jpg)  
Source: Wind.

Figure 6: 12-city secondary sales registrations' seven-day moving average   
![](images/67d13670f948275dd5bbd67a3ff30058f10f7f1b99f8dec907ac49f8bcc11450.jpg)

<details>
<summary>line</summary>

| Month   | 2018-21 avg | 2022  | 2023  | 2024  | 2025  | 2026  |
|---------|-------------|-------|-------|-------|-------|-------|
| 1-Jan   | ~1,500      | ~1,600| ~1,400| ~1,700| ~2,400| ~2,100|
| 1-Feb   | ~1,600      | ~1,700| ~1,500| ~1,800| ~2,300| ~2,300|
| 1-Mar   | ~1,800      | ~1,900| ~1,700| ~2,000| ~2,500| ~1,800|
| 1-Apr   | ~2,000      | ~1,800| ~1,900| ~2,300| ~2,700| ~2,900|
| 1-May   | ~2,500      | ~1,700| ~2,100| ~2,400| ~2,600| ~2,800|
| 1-Jun   | ~2,300      | ~1,600| ~1,900| ~2,200| ~2,300| ~2,100|
| 1-Jul   | ~2,400      | ~1,700| ~1,800| ~2,300| ~2,200| ~2,300|
| 1-Aug   | ~2,300      | ~1,600| ~1,700| ~2,100| ~2,100| ~2,100|
| 1-Sep   | ~2,200      | ~1,500| ~1,600| ~1,900| ~1,900| ~1,900|
| 1-Oct   | ~2,300      | ~1,600| ~1,700| ~2,800| ~1,900| ~1,900|
| 1-Nov   | ~2,400      | ~1,700| ~1,800| ~2,700| ~2,100| ~2,300|
| 1-Dec   | ~2,500      | ~1,800| ~1,900| ~3,100| ~2,500| ~2,600|
</details>

Source:

[中间内容因长度限制已省略]

ates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its sUBSidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised April 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 12 May 2026 01:09 AM HKT

Disseminated 12 May 2026 01:09 AM HKT
"""
