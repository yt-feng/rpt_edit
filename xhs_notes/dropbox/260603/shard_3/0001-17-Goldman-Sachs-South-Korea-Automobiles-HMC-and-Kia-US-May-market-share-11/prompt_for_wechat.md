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
# South Korea Automobiles: HMC and Kia US May market share 11.8% (+0.3ppt YoY)

Hyundai Motor (HMC) and Kia US sales numbers for May were released overnight (Motor Intelligence) where HMC delivered 94,358 units (+9.1% MoM, +3.4% YoY) and Kia 80,502 units (+10.7% MoM, +1.9% YoY). Industry demand in May came in at 1,479,626 units (+7.2% MoM, +0.4% YoY).

YTD HMC US retail sale is tracking at +1.1% and Kia +2.1%. As a recap on 2026 guidance, HMC is looking for 0.5% YoY volume growth in North America (wholesale) and Kia is looking for 4.7% YoY volume growth in the US (retail).

In terms of May market share, HMC recorded 6.4% (+0.1ppt MoM, +0.2ppt YoY) and Kia 5.4% (+0.2ppt MoM, +0.1ppt YoY). Combined market share recorded 11.8% (+0.3ppt MoM, +0.3ppt YoY). We expect 12.0% M/S by end of 2026E, with the help of new model refreshes towards 2H26.

HEV demand in the US continued to be strong, with the May number at 255,645 units (+14.4% MoM, +32.5% YoY) and BEVs at 86,495 units (+10.3% MoM, -19.8% YoY). HMC's HEV volume was 25,559 units (+18.9% MoM, +90.1% YoY) and Kia's 25,392 units (+33.9% MoM, +179.4% YoY).

In terms of HEV market share for May, HMC recorded 10.0% (+0.4ppt MoM, +3.0ppt YoY) and Kia 9.9% (+1.5ppt MoM, +5.2ppt YoY). Combined market share recorded 19.9% (+1.8ppt MoM, +8.3ppt YoY). HEV accounted for 27.1% of HMC's total volume in May and for Kia, HEV was 31.5% of its total volume.

In terms of incentives, HMC spent \$3,330 (+16.9% MoM, +16.8% YoY) per car in May and Kia \$3,440 (+9.9% MoM, +26.4% YoY). Industry average incentive trended at \$3,502 (+2.9% MoM, +5.6% YoY).

## Do Hyoung Kim

+82(2)3788-1376

dohyoung.kim@gs.com

GS (Asia) L.L.C., Seoul

Branch

## Joshua Kim

+82(2)3788-1791 | joshua.kim@gs.com

GS (Asia) L.L.C., Seoul

Branch

Exhibit 1: HMC & Kia (together HMK) US monthly key metrics snapshot

<table><tr><td colspan="9">HMK US monthly metrics</td></tr><tr><td>(Volume)</td><td>May-26</td><td>Apr-26</td><td>MoM (%)</td><td>May-25</td><td>YoY (%)</td><td>5M26</td><td>5M25</td><td>YTD YoY (%)</td></tr><tr><td colspan="9">HMC</td></tr><tr><td>Volume (units)</td><td>94,358</td><td>86,513</td><td>9.1%</td><td>91,244</td><td>3.4%</td><td>404,576</td><td>400,116</td><td>1.1%</td></tr><tr><td>BEV volume (units)</td><td>6,483</td><td>4,779</td><td>35.7%</td><td>6,108</td><td>6.1%</td><td>24,072</td><td>25,742</td><td>-6.5%</td></tr><tr><td>HEV volume (units)</td><td>25,559</td><td>21,496</td><td>18.9%</td><td>13,448</td><td>90.1%</td><td>102,137</td><td>61,852</td><td>65.1%</td></tr><tr><td>Incentives ($/car)</td><td>3,330</td><td>2,848</td><td>16.9%</td><td>2,852</td><td>16.8%</td><td>2,784</td><td>3,124</td><td>-10.9%</td></tr><tr><td colspan="9">Kia</td></tr><tr><td>Volume (units)</td><td>80,502</td><td>72,703</td><td>10.7%</td><td>79,007</td><td>1.9%</td><td>360,220</td><td>352,662</td><td>2.1%</td></tr><tr><td>BEV volume (units)</td><td>2,822</td><td>2,407</td><td>17.2%</td><td>1,489</td><td>89.5%</td><td>10,505</td><td>11,600</td><td>-9.4%</td></tr><tr><td>HEV volume (units)</td><td>25,392</td><td>18,962</td><td>33.9%</td><td>9,087</td><td>179.4%</td><td>84,286</td><td>41,711</td><td>102.1%</td></tr><tr><td>Incentives ($/car)</td><td>3,440</td><td>3,129</td><td>9.9%</td><td>2,721</td><td>26.4%</td><td>3,333</td><td>3,074</td><td>8.4%</td></tr><tr><td colspan="9">HMK</td></tr><tr><td>Volume (units)</td><td>174,860</td><td>159,216</td><td>9.8%</td><td>170,251</td><td>2.7%</td><td>764,796</td><td>752,778</td><td>1.6%</td></tr><tr><td>BEV volume (units)</td><td>9,305</td><td>7,186</td><td>29.5%</td><td>7,597</td><td>22.5%</td><td>34,577</td><td>37,342</td><td>-7.4%</td></tr><tr><td>HEV volume (units)</td><td>50,951</td><td>40,458</td><td>25.9%</td><td>22,535</td><td>126.1%</td><td>186,423</td><td>103,563</td><td>80.0%</td></tr><tr><td>Incentives ($/car)</td><td>3,381</td><td>2,976</td><td>13.6%</td><td>2,791</td><td>21.1%</td><td>3,043</td><td>3,101</td><td>-1.9%</td></tr><tr><td colspan="9">Industry</td></tr><tr><td>Volume (units)</td><td>1,479,626</td><td>1,380,007</td><td>7.2%</td><td>1,474,079</td><td>0.4%</td><td>6,560,650</td><td>6,861,379</td><td>-4.4%</td></tr><tr><td>BEV volume (units)</td><td>86,495</td><td>78,409</td><td>10.3%</td><td>107,886</td><td>-19.8%</td><td>381,474</td><td>505,468</td><td>-24.5%</td></tr><tr><td>HEV volume (units)</td><td>255,645</td><td>223,549</td><td>14.4%</td><td>192,970</td><td>32.5%</td><td>1,005,666</td><td>856,896</td><td>17.4%</td></tr><tr><td>Incentives ($/car)</td><td>3,502</td><td>3,402</td><td>2.9%</td><td>3,315</td><td>5.6%</td><td>3,415</td><td>3,341</td><td>2.2%</td></tr><tr><td>(Market share)</td><td>May-26</td><td>Apr-26</td><td>MoM (%)</td><td>May-25</td><td>YoY (%)</td><td>5M26</td><td>5M25</td><td>YTD YoY (%)</td></tr><tr><td colspan="9">HMC M/S</td></tr><tr><td>Market share</td><td>6.4%</td><td>6.3%</td><td>0.1%pt</td><td>6.2%</td><td>0.2%pt</td><td>6.2%</td><td>5.8%</td><td>0.3%pt</td></tr><tr><td>BEV market share</td><td>7.5%</td><td>6.1%</td><td>1.4%pt</td><td>5.7%</td><td>1.8%pt</td><td>6.3%</td><td>5.1%</td><td>1.2%pt</td></tr><tr><td>HEV market share</td><td>10.0%</td><td>9.6%</td><td>0.4%pt</td><td>7.0%</td><td>3.0%pt</td><td>10.2%</td><td>7.2%</td><td>2.9%pt</td></tr><tr><td colspan="9">Kia M/S</td></tr><tr><td>Market share</td><td>5.4%</td><td>5.3%</td><td>0.2%pt</td><td>5.4%</td><td>0.1%pt</td><td>5.5%</td><td>5.1%</td><td>0.4%pt</td></tr><tr><td>BEV market share</td><td>3.3%</td><td>3.1%</td><td>0.2%pt</td><td>1.4%</td><td>1.9%pt</td><td>2.8%</td><td>2.3%</td><td>0.5%pt</td></tr><tr><td>HEV market share</td><td>9.9%</td><td>8.5%</td><td>1.5%pt</td><td>4.7%</td><td>5.2%pt</td><td>8.4%</td><td>4.9%</td><td>3.5%pt</td></tr><tr><td colspan="9">HMK M/S</td></tr><tr><td>Market share</td><td>11.8%</td><td>11.5%</td><td>0.3%pt</td><td>11.5%</td><td>0.3%pt</td><td>11.7%</td><td>11.0%</td><td>0.7%pt</td></tr><tr><td>BEV market share</td><td>10.8%</td><td>9.2%</td><td>1.6%pt</td><td>7.0%</td><td>3.7%pt</td><td>9.1%</td><td>7.4%</td><td>1.7%pt</td></tr><tr><td>HEV market share</td><td>19.9%</td><td>18.1%</td><td>1.8%pt</td><td>11.7%</td><td>8.3%pt</td><td>18.5%</td><td>12.1%</td><td>6.5%pt</td></tr><tr><td>(Mix)</td><td>May-26</td><td>Apr-26</td><td>MoM (%)</td><td>May-25</td><td>YoY (%)</td><td>5M26</td><td>5M25</td><td>YTD YoY (%)</td></tr><tr><td colspan="9">HMC mix</td></tr><tr><td>BEV mix</td><td>6.9%</td><td>5.5%</td><td>1.3%pt</td><td>6.7%</td><td>0.2%pt</td><td>5.9%</td><td>6.4%</td><td>-0.5%pt</td></tr><tr><td>HEV mix</td><td>27.1%</td><td>24.8%</td><td>2.2%pt</td><td>14.7%</td><td>12.3%pt</td><td>25.2%</td><td>15.5%</td><td>9.8%pt</td></tr><tr><td>ICE &amp; others mix</td><td>66.0%</td><td>69.6%</td><td>-3.6%pt</td><td>78.6%</td><td>-12.5%pt</td><td>68.8%</td><td>78.1%</td><td>-9.3%pt</td></tr><tr><td colspan="9">Kia mix</td></tr><tr><td>BEV mix</td><td>3.5%</td><td>3.3%</td><td>0.2%pt</td><td>1.9%</td><td>1.6%pt</td><td>2.9%</td><td>3.3%</td><td>-0.4%pt</td></tr><tr><td>HEV mix</td><td>31.5%</td><td>26.1%</td><td>5.5%pt</td><td>11.5%</td><td>20.0%pt</td><td>23.4%</td><td>11.8%</td><td>11.6%pt</td></tr><tr><td>ICE &amp; others mix</td><td>65.0%</td><td>70.6%</td><td>-5.7%pt</td><td>86.6%</td><td>-21.7%pt</td><td>73.7%</td><td>84.9%</td><td>-11.2%pt</td></tr><tr><td colspan="9">HMK mix</td></tr><tr><td>BEV mix</td><td>5.3%</td><td>4.5%</td><td>0.8%pt</td><td>4.5%</td><td>0.9%pt</td><td>4.5%</td><td>5.0%</td><td>-0.4%pt</td></tr><tr><td>HEV mix</td><td>29.1%</td><td>25.4%</td><td>3.7%pt</td><td>13.2%</td><td>15.9%pt</td><td>24.4%</td><td>13.8%</td><td>10.6%pt</td></tr><tr><td>ICE &amp; others mix</td><td>65.5%</td><td>70.1%</td><td>-4.5%pt</td><td>82.3%</td><td>-16.8%pt</td><td>71.1%</td><td>81.3%</td><td>-10.2%pt</td></tr><tr><td colspan="9">Industry mix</td></tr><tr><td>BEV mix</td><td>5.8%</td><td>5.7%</td><td>0.2%pt</td><td>7.3%</td><td>-1.5%pt</td><td>5.8%</td><td>7.4%</td><td>-1.6%pt</td></tr><tr><td>HEV mix</td><td>17.3%</td><td>16.2%</td><td>1.1%pt</td><td>13.1%</td><td>4.2%pt</td><td>15.3%</td><td>12.5%</td><td>2.8%pt</td></tr><tr><td>ICE &amp; others mix</td><td>76.9%</td><td>78.1%</td><td>-1.2%pt</td><td>79.6%</td><td>-2.7%pt</td><td>78.9%</td><td>80.1%</td><td>-1.3%pt</td></tr></table>

Source: Motor Intelligence, Data compiled by GS Global Investment Research

Exhibit 2: HMK US volume trend  
![](images/39684ce73c4e9b9cb5e9286914afb2c28fd1061054ad295d91c84e9ddef30e5b.jpg)

<details>
<summary>stacked bar chart</summary>

| Month | HMC US volume (units) | Kia US volume (units) |
|---|---|---|
| Jan-23 | 57,000 | 108,000 |
| Feb-23 | 61,000 | 121,000 |
| Mar-23 | 81,000 | 152,000 |
| Apr-23 | 78,000 | 145,000 |
| May-23 | 77,000 | 146,000 |
| Jun-23 | 74,000 | 144,000 |
| Jul-23 | 73,000 | 143,000 |
| Aug-23 | 75,000 | 142,000 |
| Sep-23 | 76,000 | 125,000 |
| Oct-23 | 69,000 | 136,000 |
| Nov-23 | 78,000 | 141,000 |
| Dec-23 | 81,000 | 143,000 |
| Jan-24 | 52,000 | 103,000 |
| Feb-24 | 65,000 | 123,000 |
| Mar-24 | 83,000 | 152,000 |
| Apr-24 | 75,000 | 139,000 |
| May-24 | 84,000 | 159,000 |
| Jun-24 | 74,000 | 139,000 |
| Jul-24 | 87,000 | 161,000 |
| Aug-24 | 73,000 | 128,000 |
| Sep-24 | 79,000 | 147,000 |
| Oct-24 | 81,000 | 155,000 |
| Nov-24 | 86,000 | 159,000 |
| Dec-24 | 59,000 | 116,000 |
| Jan-25 | 68,000 | 131,000 |
| Feb-25 | 93,000 | 169,000 |
| Mar-25 | 91,000 | 163,000 |
| Apr-25 | 93,000 | 169,000 |
| May-25 | 78,000 | 141,000 |
| Jun-25 | 86,000 | 157,000 |
| Jul-25 | 97,000 | 178,000 |
| Aug-25 | 79,000 | 144,000 |
| Sep-25 | 79,000 | 144,000 |
| Oct-25 | 81,000 | 155,000 |
| Nov-25 | 87,000 | 163,000 |
| Dec-25 | 61,000 | 124,000 |
| Jan-26 | 71,000 | 137,000 |
| Feb-26 | 92,000 | 167,000 |
| Mar-26 | 87,000 | 159,000 |
| Apr-26 | 95,000 | 175,000 |
| May-26 | 95,000 | 176,000 |
</details>

Source: Motor Intelligence

Exhibit 3: HMK US volume YoY trend  
![](images/287d344d20e156fb77996b44b4448f0f93a9a2140385e287b971a6c74e2b0a79.jpg)

<details>
<summary>line chart</summary>

| Month   | HMC US volume YoY (%) | Kia US volume YoY (%) |
|---------|------------------------|------------------------|
| Jan-23  | 8.0%                   | 22.0%                  |
| Feb-23  | 9.0%                   | 23.0%                  |
| Mar-23  | 27.0%                  | 20.0%                  |
| Apr-23  | 15.0%                  | 18.0%                  |
| May-23  | 18.0%                  | 24.0%                  |
| Jun-23  | 10.0%                  | 8.0%                   |
| Jul-23  | 11.0%                  | 14.0%                  |
| Aug-23  | 3.0%                   | 9.0%                   |
| Sep-23  | 17.0%                  | 19.0%                  |
| Oct-23  | 11.0%                  | 2.0%                   |
| Nov-23  | 5.0%                   | 3.0%                   |
| Dec-23  | -8.0%                  | -4.0%                  |
| Jan-24  | 6.0%                   | -4.0%                  |
| Feb-24  | 3.0%                   | -4.0%                  |
| Mar-24  | -4.0%                  | -6.0%                  |
| Apr-24  | -3.0%                  | -10.0%                 |
| May-24  | -4.0%                  | -12.0%                 |
| Jun-24  | -3.0%                  | -10.0%                 |
| Jul-24  | -3.0%                  | -12.0%                 |
| Aug-24  | 21.0%                  | -13.0%                 |
| Sep-24  | -15.0%                 | -17.0%                 |
| Oct-24  | 18.0%                  | 17.0%                  |
| Nov-24  | 10.0%                  | 21.0%                  |
| Dec-24  | 5.0%                   | 21.0%                  |
| Jan-25  | 14.0%                  | 13.0%                  |
| Feb-25  | 4.0%                   | 13.0%                  |
| Mar-25  | 18.0%                  | 14.0%                  |
| Apr-25  | 8.0%                   | -3.0%                  |
| May-25  | 4.0%                   | -3.0%                  |
| Jun-25  | 14.0%                  | 11.0%                  |
| Jul-25  | 13.0%                  | 11.0%                  |
| Aug-25  | -3.0%                  | -3.0%                  |
| Sep-25  | -3.0%                  | -3.0%                  |
| Oct-25  | -3.0%                  | -3.0%                  |
| Nov-25  | -3.0%                  | -3.0%                  |
| Dec-25  | -3.0%                  | -3.0%                  |
| Jan-26  | -3.0%                  | -3.0%                  |
| Feb-26  | -3.0%                  | -3.0%                  |
| Mar-26  | -3.0%                  | -3.0%                  |
| Apr-26  | -3.0%                  | -3.0%                  |
| May-26  | -3.0%                  | -3.0%                  |
</details>

Source: Motor Intelligence

Exhibit 4: HMK US M/S trend  
![](images/644114beac85ebc4cce9f634fe639140d664b924fd768d8bfc871af53d228387.jpg)

<details>
<summary>stacked area chart</summary>

| Month | HMC M/S (%) | Kia M/S (%) |
| :--- | :--- | :--- |
| Jan-23 | 5.2 | 4.8 |
| Mar-23 | 5.7 | 5.1 |
| May-23 | 5.5 | 5.0 |
| Jul-23 | 5.4 | 5.1 |
| Sep-23 | 5.5 | 5.0 |
| Nov-23 | 6.0 | 4.9 |
| Jan-24 | 4.7 | 4.9 |
| Mar-24 | 5.6 | 5.1 |
| May-24 | 5.7 | 5.2 |
| Jul-24 | 5.8 | 5.3 |
| Sep-24 | 5.9 | 5.2 |
| Nov-24 | 5.9 | 5.1 |
| Jan-25 | 5.3 | 5.1 |
| Mar-25 | 5.8 | 5.2 |
| May-25 | 6.0 | 5.3 |
| Jul-25 | 6.3 | 5.4 |
| Sep-25 | 6.1 | 5.3 |
| Nov-25 | 6.3 | 5.4 |
| Jan-26 | 5.4 | 5.4 |
| Mar-26 | 6.4 | 5.6 |
| May-26 | 6.3 | 5.7 |
</details>

Source: Motor Intelligence

Exhibit 5: HMK US M/S YoY gain trend  
![](images/6b09f97ffc004d5ff1a4de48f60cc48006e92b9d5131a088a6a66dfdc167f0b9.jpg)

<details>
<summary>line chart</summary>

| Month   | Kia M/S YoY gain (%pt) | HMC M/S YoY gain (%pt) |
|---------|------------------------|------------------------|
| Jan-23  | 0.7                    | 0.15                   |
| Feb-23  | 0.6                    | 0.0                    |
| Mar-23  | 0.5                    | 0.8                    |
| Apr-23  | 0.4                    | 0.2                    |
| May-23  | -0.1                   | -0.2                   |
| Jun-23  | -0.3                   | -0.4                   |
| Jul-23  | -0.4                   | -0.7                   |
| Aug-23  | -0.3                   | -0.1                   |
| Sep-23  | -0.2                   | 0.1                    |
| Oct-23  | -0.1                   | 0.15                   |
| Nov-23  | -0.2                   | -0.6                   |
| Dec-23  | -0.3                   | -0.6                   |
| Jan-24  | -0.4                   | -0.5                   |
| Feb-24  | -0.5                   | -0.1                   |
| Mar-24  | -0.4                   | -0.1                   |
| Apr-24  | -0.3                   | 0.1                    |
| May-24  | -0.2                   | 0.3                    |
| Jun-24  | -0.1                   | 0.1                    |
| Jul-24  | -0.6                   | 0.6                    |
| Aug-24  | -0.2                   | 0.1                    |
| Sep-24  | -0.1                   | 0.3                    |
| Oct-24  | 0.1                    | -0.1                   |
| Nov-24  | 0.3                    | 0.5                    |
| Dec-24  | 0.7                    | 0.1                    |
| Jan-25  | 0.4                    | 0.2                    |
| Feb-25  | 0.3                    | 0.1                    |
| Mar-25  | 0.1                    | 0.4                    |
| Apr-25  | 0.1                    | 0.4                    |
| May-25  | 0.1                    | 0.4                    |
| Jun-25  | -0.1                   | 0.4                    |
| Jul-25  | -0.1                   | 0.4                    |
| Aug-25  | 0.1                    | 0.3                    |
| Sep-25  | 0.3                    | 0.1                    |
| Oct-25  | 0.5                    | 0.1                    |
| Nov-25  | 0.7                    | 0.1                    |
| Dec-25  | 0.4                    | 0.1                    |
| Jan-26  | 0.7                    | 0.6                    |
| Feb-26  | 0.4                    | 0.6                    |
| Mar-26  | 0.1                    | 0.3                    |
| Apr-26  | 0.1                    | 0.2                    |
| May-26  | 0.1                    | 0.1                    |
</details>

Source: Motor Intelligence

Exhibit 6: HMK US HEV volume trend  
![](images/86c1033eb0892b6d5b0d971ed2a4d98a68afa8002d6d391b2b38e0f91cc102d1.jpg)

<details>
<summary>stacked bar chart</summary>

| Month | HMC HEV volume (units) | Kia HEV volume (units) |
| --- | --- | --- |
| Jan-23 | 6500 | 7000 |
| Feb-23 | 7000 | 8000 |
| Mar-23 | 8000 | 9000 |
| Apr-23 | 8500 | 10000 |
| May-23 | 9000 | 11000 |
| Jun-23 | 8500 | 12000 |
| Jul-23 | 8000 | 13000 |
| Aug-23 | 7500 | 14000 |
| Sep-23 | 7000 | 15000 |
| Oct-23 | 6500 | 16000 |
| Nov-23 | 7000 | 17000 |
| Dec-23 | 6500 | 18000 |
| Jan-24 | 5500 | 19000 |
| Feb-24 | 6500 | 20000 |
| Mar-24 | 8500 | 21000 |
| Apr-24 | 9500 | 22000 |
| May-24 | 11500 | 23000 |
| Jun-24 | 12500 | 24000 |
| Jul-24 | 13500 | 25000 |
| Aug-24 | 14500 | 26000 |
| Sep-24 | 15500 | 27000 |
| Oct-24 | 16500 | 28000 |
| Nov-24 | 17500 | 29000 |
| Dec-24 | 18500 | 30000 |
| Jan-25 | 11500 | 16500 |
| Feb-25 | 14500 | 24500 |
| Mar-25 | 15500 | 25500 |
| Apr-25 | 16500 | 26500 |
| May-25 | 17500 | 27500 |
| Jun-25 | 18500 | 28500 |
| Jul-25 | 19500 | 29500 |
| Aug-25 | 21500 | 31500 |
| Sep-25 | 23500 | 33500 |
| Oct-25 | 25500 | 35500 |
| Nov-25 | 27500 | 37500 |
| Dec-25 | 29500 | 39500 |
| Jan-26 | 31500 | 41500 |
| Feb-26 | 33500 | 43500 |
| Mar-26 | 35500 | 45500 |
| Apr-26 | 37500 | 47500 |
| May-26 | 39500 | 49500 |
| Jun-26 | 41500 | 51500 |
</details>

Source: Motor Intelligence

Exhibit 7: HMK US HEV volume YoY trend  
![](images/901e8ea7a7f7822e9ac65888a7c0ffed849a161de8ae9bf30229f733c5e2a06f.jpg)

<details>
<summary>line chart</summary>

| Month   | Kia HEV volume growth (%) | HMC HEV volume growth (%) |
|---------|---------------------------|---------------------------|
| Jan-23  | 170.0%                    | 20.0%                     |
| Feb-23  | 130.0%                    | 30.0%                     |
| Mar-23  | 200.0%                    | 100.0%                    |
| Apr-23  | 50.0%                     | 120.0%                    |
| May-23  | 100.0%                    | 110.0%                    |
| Jun-23  | 100.0%                    | 40.0%                     |
| Jul-23  | 120.0%                    | 50.0%                     |
| Aug-23  | -30.0%                    | 20.0%                     |
| Sep-23  | -40.0%                    | 10.0%                     |
| Oct-23  | -30.0%                    | -10.0%                    |
| Nov-23  | -2

[中间内容因长度限制已省略]

m impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
