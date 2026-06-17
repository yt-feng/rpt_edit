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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`GS`。标题格式建议：`# GS：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
CHINA NEW ENERGY VEHICLE WEEKLY CHARTBOOK

2026 Week 24 - Weekly NEV orders -14%/-13% yoy/wow, 67% NEV penetration

Bottom line: Weekly NEV orders were -14% yoy and -13% wow coming off the initial pulse of new model launches in late May. Retail/Wholesale NEV penetration reached 66.7%/67.2% in Jun 1-7.

A curated compilation of the most topical charts on weekly passenger vehicle market performance, organized into the following categories: (1) Key NEV brands' weekly orders amount, (2) Key events to watch, (3) NEV/ICE dealer price discount tracker, and (4) Upstream battery pricing dynamics.

## 2026 Week 24 highlights:

Key brand orders: Geely / BYD / Tesla showed defensive growth at +8%/-4%/-8% wow.  
CPCA weekly trend: As of Jun 1-7, PV retail volume was 228k units (-23% yoy/-11% mom), while PV wholesale volume was 204k units (-25% yoy/+10% mom) per CPCA. Meanwhile, NEV retail volume was 152k units (-14% yoy/+8% mom), and NEV wholesale volume was 137k units (-6% yoy/+17% mom), with NEV penetration at 66.7%/67.2% in Jun 1-7, compared to 63%/61.1% in May.

■ Key pricing trends: NEV dealer discount narrowed wow and ICE dealer discount widened wow.  
Upstream battery pricing dynamics: Battery grade lithium carbonate price increased to Rmb174.5k/ton (+3.6% wow), while prismatic cell (LFP) and prismatic cell (NCM) prices were stable wow.

## Tina Hou

+86(21)2401-8694

tina.hou@goldmansachs.cn

GS (China) Securities

Company Limited

## Jenny Du

+86(21)2401-8978

jenny.x.du@goldmansachs.cn

GS (China) Securities

Company Limited

## Weekly order summary

Key brand weekly order trends during 2026 week 24 (6/8-6/14):

Key NEV OEMs combined orders were -14% yoy and -13% wow in week 24 coming off the initial pulse of new model launches in late May.  
■ Geely / BYD / Tesla showed defensive growth at +8%/-4%/-8% wow.  
In terms of YTD orders, Nio / HIMA / Tesla showed relatively defensive growth at +93%/+31%/+3% yoy.

Exhibit 1: NEV brand weekly orders summary

<table><tr><td></td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td><td>2026 YTD</td></tr><tr><td colspan="7">Monthly order (units)</td></tr><tr><td>BYD (Dynasty &amp; Ocean)</td><td>123535</td><td>96547</td><td>252181</td><td>223899</td><td>197343</td><td>986905</td></tr><tr><td>Geely (Galaxy &amp; Zeekr)</td><td></td><td></td><td>85343</td><td>125606</td><td>114161</td><td>376710</td></tr><tr><td>HIMA</td><td>26347</td><td>19574</td><td>45610</td><td>122320</td><td>143479</td><td>399750</td></tr><tr><td>Leapmotor</td><td></td><td></td><td>50257</td><td>82036</td><td>67357</td><td>225780</td></tr><tr><td>Tesla</td><td>30271</td><td>32614</td><td>60929</td><td>61914</td><td>57371</td><td>270400</td></tr><tr><td>Nio</td><td>15817</td><td>13400</td><td>38190</td><td>44025</td><td>86183</td><td>245115</td></tr><tr><td>Li Auto</td><td>18243</td><td>14614</td><td>26851</td><td>36401</td><td>43150</td><td>151410</td></tr><tr><td>Xiaomi</td><td>5529</td><td>10171</td><td>60587</td><td>33513</td><td>33980</td><td>156200</td></tr><tr><td>XPeng</td><td>16957</td><td>14597</td><td>41607</td><td>39394</td><td>54514</td><td>184900</td></tr><tr><td>SUM</td><td>236699</td><td>201519</td><td>661556</td><td>769108</td><td>797539</td><td>2997170</td></tr><tr><td colspan="7">YoY (%)</td></tr><tr><td>BYD (Dynasty &amp; Ocean)</td><td>-57%</td><td>-64%</td><td>-31%</td><td>-29%</td><td>-41%</td><td>-48%</td></tr><tr><td>Geely (Galaxy &amp; Zeekr)</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>HIMA</td><td>-25%</td><td>-22%</td><td>-21%</td><td>14%</td><td>154%</td><td>31%</td></tr><tr><td>Leapmotor</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Tesla</td><td>-37%</td><td>-37%</td><td>2%</td><td>55%</td><td>55%</td><td>3%</td></tr><tr><td>Nio</td><td>-9%</td><td>-2%</td><td>97%</td><td>24%</td><td>190%</td><td>93%</td></tr><tr><td>Li Auto</td><td>-47%</td><td>-46%</td><td>-20%</td><td>-9%</td><td>-19%</td><td>-27%</td></tr><tr><td>Xiaomi</td><td>-86%</td><td>-79%</td><td>-27%</td><td>-5%</td><td>51%</td><td>-35%</td></tr><tr><td>XPeng</td><td>-18%</td><td>-41%</td><td>-26%</td><td>7%</td><td>18%</td><td>-11%</td></tr><tr><td>SUM</td><td>-51%</td><td>-56%</td><td>-22%</td><td>-8%</td><td>6%</td><td>-23%</td></tr><tr><td colspan="7">MoM (%)</td></tr><tr><td>BYD (Dynasty &amp; Ocean)</td><td>-55%</td><td>-22%</td><td>161%</td><td>-11%</td><td>-12%</td><td></td></tr><tr><td>Geely (Galaxy &amp; Zeekr)</td><td></td><td></td><td></td><td>47%</td><td>-9%</td><td></td></tr><tr><td>HIMA</td><td>-52%</td><td>-26%</td><td>133%</td><td>168%</td><td>17%</td><td></td></tr><tr><td>Leapmotor</td><td></td><td></td><td></td><td>63%</td><td>-18%</td><td></td></tr><tr><td>Tesla</td><td>-39%</td><td>8%</td><td>87%</td><td>2%</td><td>-7%</td><td></td></tr><tr><td>Nio</td><td>-49%</td><td>-15%</td><td>185%</td><td>13%</td><td>96%</td><td></td></tr><tr><td>Li Auto</td><td>-28%</td><td>-20%</td><td>84%</td><td>36%</td><td>19%</td><td></td></tr><tr><td>Xiaomi</td><td>-63%</td><td>84%</td><td>496%</td><td>-45%</td><td>1%</td><td></td></tr><tr><td>XPeng</td><td>-43%</td><td>-14%</td><td>185%</td><td>-5%</td><td>38%</td><td></td></tr><tr><td>SUM</td><td>-51%</td><td>-15%</td><td>161%</td><td>16%</td><td>4%</td><td></td></tr></table>

<table><tr><td>2025</td><td>2025</td><td>2025</td><td>2025</td><td>2026</td><td>2026</td><td>2026</td><td>2026</td></tr><tr><td>W215/19-5/25</td><td>W225/26-6/1</td><td>W236/2-6/8</td><td>W246/9-6/15</td><td>W215/18-5/24</td><td>W225/25-5/31</td><td>W236/1-6/7</td><td>W246/8-6/14</td></tr><tr><td colspan="8">Weekly order (units)</td></tr><tr><td>70000</td><td>80000</td><td>75000</td><td>84000</td><td>42300</td><td>48700</td><td>47700</td><td>45700</td></tr><tr><td></td><td></td><td></td><td></td><td>36250</td><td>22100</td><td>24840</td><td>26760</td></tr><tr><td>10200</td><td>9200</td><td>11400</td><td>9300</td><td>21140</td><td>40680</td><td>24180</td><td>18240</td></tr><tr><td></td><td></td><td></td><td></td><td>13800</td><td>15100</td><td>14600</td><td>11530</td></tr><tr><td>7500</td><td>8000</td><td>12000</td><td>13000</td><td>11800</td><td>14000</td><td>14200</td><td>13100</td></tr><tr><td>6100</td><td>5900</td><td>5400</td><td>5100</td><td>11830</td><td>38810</td><td>28020</td><td>19480</td></tr><tr><td>10000</td><td>11000</td><td>8900</td><td>9200</td><td>11600</td><td>8700</td><td>6650</td><td>5500</td></tr><tr><td>4500</td><td>5000</td><td>5000</td><td>5000</td><td>9800</td><td>8600</td><td>7410</td><td>5010</td></tr><tr><td>6800</td><td>22500</td><td>11300</td><td>9000</td><td>28800</td><td>11100</td><td>9510</td><td>8320</td></tr><tr><td>115100</td><td>141600</td><td>129000</td><td>134600</td><td>187320</td><td>207790</td><td>177110</td><td>153640</td></tr><tr><td colspan="8">YoY (%)</td></tr><tr><td></td><td></td><td></td><td></td><td>-40%</td><td>-39%</td><td>-36%</td><td>-46%</td></tr><tr><td></td><td></td><td></td><td></td><td>107%</td><td>342%</td><td>112%</td><td>96%</td></tr><tr><td></td><td></td><td></td><td></td><td>57%</td><td>75%</td><td>18%</td><td>1%</td></tr><tr><td></td><td></td><td></td><td></td><td>94%</td><td>558%</td><td>419%</td><td>282%</td></tr><tr><td></td><td></td><td></td><td></td><td>16%</td><td>-21%</td><td>-25%</td><td>-40%</td></tr><tr><td></td><td></td><td></td><td></td><td>118%</td><td>72%</td><td>48%</td><td>0%</td></tr><tr><td></td><td></td><td></td><td></td><td>324%</td><td>-51%</td><td>-16%</td><td>-8%</td></tr><tr><td></td><td></td><td></td><td></td><td>19%</td><td>20%</td><td>7%</td><td>-14%</td></tr><tr><td colspan="8">WoW (%)</td></tr><tr><td>3%</td><td>14%</td><td>-6%</td><td>12%</td><td>4%</td><td>15%</td><td>-2%</td><td>-4%</td></tr><tr><td></td><td></td><td></td><td></td><td>77%</td><td>-39%</td><td>12%</td><td>8%</td></tr><tr><td>-11%</td><td>-10%</td><td>24%</td><td>-18%</td><td>-33%</td><td>92%</td><td>-41%</td><td>-25%</td></tr><tr><td></td><td></td><td></td><td></td><td>9%</td><td>9%</td><td>-3%</td><td>-21%</td></tr><tr><td>10%</td><td>7%</td><td>50%</td><td>8%</td><td>4%</td><td>19%</td><td>1%</td><td>-8%</td></tr><tr><td>5%</td><td>-3%</td><td>-8%</td><td>-6%</td><td>-44%</td><td>228%</td><td>-28%</td><td>-30%</td></tr><tr><td>-13%</td><td>10%</td><td>-19%</td><td>3%</td><td>-13%</td><td>-25%</td><td>-24%</td><td>-17%</td></tr><tr><td>-10%</td><td>11%</td><td>0%</td><td>0%</td><td>92%</td><td>-12%</td><td>-14%</td><td>-32%</td></tr><tr><td>-4%</td><td>231%</td><td>-50%</td><td>-20%</td><td>433%</td><td>-61%</td><td>-14%</td><td>-18%</td></tr><tr><td>-1%</td><td>23%</td><td>-9%</td><td>4%</td><td>16%</td><td>11%</td><td>-15%</td><td>-18%</td></tr></table>

Source: ThinkerCar, Data compiled by GS Global Investment Research

## Key events to watch

## 2026 Week 25, Jun 15-21

Jun 15: Nio launched ET5/ET5T/EC6 facelifts; Li Auto host Livis Day Software and Artificial Intelligence Launch Event.  
■ Jun 16: Leapmotor to launch C10/C11/C16 facelifts.  
■ Jun 17: BYD to officially launch Da Tang.

## 2026 Week 26, Jun 22-28

■ Jun 23: Li Auto to officially launch L8 facelift.  
■ Jun 23: BYD to launch N8L flash-charging version.  
■ Jun 25: Leapmotor to start pre-sales of D99.

## 2026 Week 27, Jun 29-Jul 5

■ Jul 1: NEV OEM monthly volume release.  
■ Jul 2: XPeng to unveil MONA L03.

## 2026 Week 28-30, Jul 6-Jul 26

Jul 10-11: CPCA will release PV/NEV industry and by model wholesale/retail data.  
■ Jul: XPeng to officially launch MONA L03.

## Retail end-pricing

■ NEV: average dealer discount vs. MSRP was 7.54% as of Jun 13, vs. 7.79%/8.18% as of Jun 6, 2026/Jun 16, 2025; BYD average dealer discount vs. MSRP was 4.27% as of Jun 13, vs. 5.14%/5.56% as of Jun 6, 2026/Jun 16, 2025.  
ICE: average dealer discount vs. MSRP was 19.56% as of Jun 13, vs. 19.54%/23.03% as of Jun 6, 2026/Jun 16, 2025.

Exhibit 2: NEV dealer discount trend  
![](images/2eb8fd10e19d21869fc7d5c377c24a4290c94e3f316afb939ea313dd42cec39e.jpg)

<details>
<summary>line chart</summary>

| Date       | NEV    |
| ---------- | ------ |
| Jan 06     | -7.5%  |
| Feb 06     | -7.0%  |
| Mar 06     | -6.5%  |
| Apr 06     | -7.0%  |
| May 06     | -8.0%  |
| Jun 06     | -10.0% |
| Jul 06     | -8.5%  |
| Aug 06     | -8.0%  |
| Sep 06     | -8.5%  |
| Oct 06     | -8.0%  |
| Nov 06     | -8.5%  |
| Dec 06     | -8.0%  |
| Jan 07     | -8.5%  |
| Feb 07     | -8.0%  |
| Mar 07     | -8.5%  |
| Apr 07     | -8.0%  |
| May 07     | -8.5%  |
| Jun 07     | -8.0%  |
</details>

![](images/24eb1d92585f55bedd89969182607641718c7ee6b01864ba6e4ae9b916b88a29.jpg)

<details>
<summary>line chart</summary>

| Month-Year | GM-Wuling | Volkswagen | BMW | Nissan | Honda | Mercedes | Volvo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Jan 6 | -5% | -10% | -25% | -10% | -25% | -25% | -25% |
| Mar 1 | -10% | -15% | -30% | -10% | -25% | -25% | -25% |
| Apr 1 | -10% | -15% | -30% | -10% | -25% | -25% | -25% |
| May 1 | -10% | -15% | -30% | -10% | -25% | -25% | -25% |
| Jun 1 | -10% | -15% | -30% | -10% | -25% | -25% | -25% |
| Jul 1 | -10% | -15% | -30% | -10% | -25% | -25% | -25% |
| Aug 1 | -10% | -15% | -30% | -10% | -25% | -25% | -25% |
| Sep 1 | -10% | -15% | -30% | -10% | -25% | -25% | -25% |
| Oct 1 | -10% | -15% | -30% | -10% | -25% | -25% | -25% |
| Nov 1 | -10% | -15% | -30% | -10% | -25% | -25% | -25% |
| Dec 1 | -10% | -15% | -30% | -10% | -25% | -25% | -25% |
| Jan 6 | -10% | -15% | -30% | -10% | -25% | -25% | -25% |
| Feb 6 | -10% | -15% | -30% | -10% | -25% | -25% | -25% |
| Mar 6 | -10% | -15% | -30% | -10% | -25% | -25% | -25% |
| Apr 6 | -10% | -15% | -30% | -10% | -25% | -25% | -25% |
| May 6 | -10% | -15% | -30% | -10% | -25% | -25% | -25% |
| Jun 6 | -10% | -15% | -30% | -10% | -25% | -25% | -25% |
| Jul 6 | -10% | -15% | -30% | -10% | -25% | -25% | -25% |
| Aug 6 | -10% | -15% | -30% | -10% | -25% | -25% | -25% |
| Sep 6 | -10% | -15% | -30% | -10% | -25% | -25% | -25% |
| Oct 6 | -10% | -15% | -30% | -10% | -25% | -25% | -25% |
| Nov 6 | -10% | -15% | -30% | -10% | -25% | -25% | -25% |
| Dec 6 | -10% | -15% | -30% | -10% | -25% | -25% | -25% |
| Jan 7 | -10% | -15% | -30% | -10% | -25% | -25% | -25% |
| Feb 7 | -10% | -15% | -30% | -10% | -25% | -25% | -25% |
| Mar 7 | -10% | -15% | -30% | -10% | -25% | -25% | -25% |
| Apr 7 | -10% | -15% | -30% | -10% | -25% | -25% | -25% |
| May 7 | -10% | -15% | -30% | -10% | -25% | -25% | -25% |
| Jun 7 | -10% | -15% | -30% | -10% | -25% | -25% | -25% |
| Jul 7 | -10% | -15% | -30% | -10% | -25% | -25% | -25% |
| Aug 7 | -10% | -15% | -30% | -10% | -25% | -25% | -25% |
| Sep 7 | -10% | -15% | -30% | -10% | -25% | -25% | -25% |
| Oct 7 | -10% | -15% | -30% | -10% | -25% | -25% | -25% |
| Nov 7 | -10% | -15% | -30% | -10% | -25% | -25% | -25% |
| Dec 7 | -10% | -15% | -30% | -10% | -25% | -25% | -25% |
</details>

![](images/177cef328d2e9fea778e880e50d600ee442fcf61c991d4d957158282007ac7fc.jpg)

<details>
<summary>line chart</summary>

| Date       | BYD   | Geely | ChangAn | Aion  | Chery | Great Wall | Leapmotor | SAIC  | XPeng |
|------------|-------|-------|---------|-------|-------|------------|-----------|-------|-------|
| Jan 6      | -5%   | -5%   | -5%     | -5%   | -5%   | -5%        | -5%       | -5%   | -5%   |
| Feb 1      | -5%   | -5%   | -5%     | -5%   | -5%   | -5%        | -5%       | -5%   | -5%   |
| Mar 1      | -5%   | -5%   | -5%     | -5%   | -5%   | -5%        | -5%       | -5%   | -5%   |
| Apr 1      | -5%   | -5%   | -5%     | -5%   | -5%   | -5%        | -5%       | -5%   | -5%   |
| May 1      | -5%   | -5%   | -5%     | -5%   | -5%   | -5%        | -5%       | -5%   | -5%   |
| Jun 1      | -5%   | -5%   | -5%     | -5%   | -5%   | -5%        | -5%       | -5%   | -5%   |
| Jul 1      | -5%   | -5%   | -5%     | -5%   | -5%   | -5%        | -5%       | -5%   | -5%   |
| Aug 1      | -5%   | -5%   | -5%     | -5%   | -5%   | -5%        | -5%       | -5%   | -5%   |
| Sep 1      | -5%   | -5%   | -5%     | -5%   | -5%   | -5%        | -5%       | -5%   | -5%   |
| Oct 1      | -5%   | -5%   | -5%     | -5%   | -5%   | -5%        | -5%       | -5%   | -5%   |
| Nov 1      | -5%   | -5%   | -5%     | -5%   | -5%   | -5%        | -5%       | -5%   | -5%   |
| Dec 1      | -5%   | -5%   | -5%     | -5%   | -5%   | -5%        | -5%       | -5%   | -5%   |
| Jan 2      | -5%   | -5%   | -5%     | -5%   | -5%   | -5%        | -5%       | -5%   | -5%   |
| Feb 2      | -5%   | -5%   | -5%     | -5%   | -5%   | -5%        | -5%       | -5%   | -5%   |
| Mar 2      | -5%   | -5%   | -5%     | -5%   | -5%   | -5%        | -5%       | -5%   | -5%   |
| Apr 2      | -5%   | -5%   | -5%     | -5%   | -5%   | -5%        | -5%       | -5%   | -5%   |
| May 2      | -5%   | -5%   | -5%     | -5%   | -5%   | -5%        | -5%       | -5%   | -5%   |
| Jun 2      | -5%   | -5%   | -5%     | -5%   | -5%   | -5%        | -5%       | -5%   | -5%   |
| Jul 2      | -10%  | 0%    | 0%      | 0%    | 0%    | 0%         | 0%        | 0%    | 0%    |
| Aug 2      | 0%    | 0%    | 0%      | 0%    | 0%    | 0%         | 0%        | 0%    | 0%    |
| Sep 2      | 0%    | 0%    | 0%      | 0%    | 0%    | 0%         | 0%        | 0%    | 0%    |
| Oct 2      | 0%    | 0%    | 0%      | 0%    | 0%    | 0%         | 0%        | 0%    | 0%    |
| Nov 2      | 0%    | 0%    | 0%      | 0%    | 0%    | 0%         | 0%        | 0%    | 0%    |
| Dec 2      | 0%    | 0%    | 0%      | 0%    | 0%    | 0%         | 0%        | 0%    | 0%    |
| Jan 3      | 0%    | 0%    | 0%      | 0%    | 0%    | 0%         | 0%        | 0%    | 0%    |
| Feb 3      | 0%    | 0%    | 0%      | 0%    | 0%    | 0%         | 0%        | 0%    | 0%    |
| Mar 3      | 0%    | 0%    | 0%      | 0%    | 0%    | 0%         | 0%        | 0%    | 0%    |
| Apr 3      | 0%    | 0%    | 0%      | 0%    | 0%    | 0%         | 0%        | 0%    | 0%    |
| May 3      | 0%    | 0%    | 0%      | 0%    | 0%    | 0%         | 0%        | 0%    | 0%    |
| Jun 3      | 0%    | 0%    | 0%      | 0%    | 0%    | 0%         | 0%        | 0%    | 0%    |
| Jul 3      | 0.7477| 1.8877|1.8877   \n\n|1.8877|1.8877|1.8877      \n|1.8877     \n|1.8877|1.8877|
| Aug 3      | ...   ...| ...   ...| ...     ...| ...   ...| ...   ...| ...        |\n|        |\n| 
| Sep 3      | ...   ...| ...   ...| ...     ...| ...   ...| ...   ...| ...        |\n|        |\n| 
| Oct 3      | ...   ...| ...   ...| ...     ...| ...   ...| ...   ...| ...        |\n|        |\n| 
| Nov 3      | ...   ...| ...   ...| ...     ...| ...   ...| ...   ...| ...        |\n|        |\n| 
| Dec 3      | ...   ...| ...   ...| ...     ...| ...   ...| ...   ...| ...        |\n|        |\n| 
| Jan 4      | ...   ...| ...   ...| ...     ...| ...   ...| ...   ...| ...        |\n|        |\n| 
| Feb 4      | ...   ...| ...   ...| ...     ...| ...   ...| ...   ...| ...        |\n|        |\n| 
| Mar 4      | ...   ...| ...   ...| ...     ...| ...   ...| ...   ...| ...        |\n|        |\n| 
| Apr 4      | ...   ...| ...   ...| ...     ...| ...   ...| ...   ...| ...        |\n|        |\n| 
| May 4      | ...   ...| ...   ...| ...     ...| ...   ...| ...   ...| ...        |\n|        |\n| 
| Jun 4      | ...   ...| ...   ...| ...     ...|...   ...|...   ...|...        |\n|        |\n|
</details>

By brand dealer discount is based on best-selling models.  
Source: Autohome, Data compiled by GS Global Investment Research

Exhibit 3: ICE dealer discount trend  
![](images/e1a575c330afef1f14d90746e36c855e0773da72819d81daea1501a877547330.jpg)

<details>
<summary>line chart</summary>

| Date       | ICE    |
| ---------- | ------ |
| Jan 6      | -21%   |
| Feb 3      | -20%   |
| Mar 1      | -21%   |
| Apr 1      | -22%   |
| May 1      | -23%   |
| Jun 1      | -24%   |
| Jul 1      | -22%   |
| Aug 1      | -21%   |
| Sep 1      | -22%   |
| Oct 1      | -23%   |
| Nov 1      | -22%   |
| Dec 1      | -21%   |
| Jan 2      | -20%   |
| Feb 2      | -19%   |
| Mar 1      | -20%   |
| Apr 1      | -21%   |
| May 1      | -22%   |
| Jun 1      | -23%   |
| Jul 1      | -24%   |
| Aug 1      | -23%   |
| Sep 1      | -22%   |
| Oct 1      | -21%   |
| Nov 1      | -20%   |
| Dec 1      | -19%   |
| Jan 3      | -18%   |
| Feb 3      | -17%   |
| Mar 3      | -16%   |
| Apr 3      | -15%   |
| May 3      | -14%   |
| Jun 3      | -13%   |
| Jul 3      | -12%   |
| Aug 3      | -11%   |
| Sep 3      | -10%   |
| Oct 3      | -9%    |
| Nov 3      | -8%    |
| Dec 3      | -7%    |
| Jan 4      | -6%    |
| Feb 4      | -5%    |
| Mar 4      | -4%    |
| Apr 4      | -3%    |
| May 4      | -2%    |
| Jun 4      | -1%    |
| Jul 4      | 0%     |
| Aug 

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
