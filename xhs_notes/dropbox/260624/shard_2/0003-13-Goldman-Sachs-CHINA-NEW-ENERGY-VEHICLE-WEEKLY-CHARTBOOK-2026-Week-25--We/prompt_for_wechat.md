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
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`GS`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
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
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

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
# CHINA NEW ENERGY VEHICLE WEEKLY CHARTBOOK

# 2026 Week 25 - Weekly NEV orders +31%/+34% yoy/wow driven by new model launches

Bottom line: Weekly NEV orders were +31% yoy and +34% wow driven by new model launches (e.g. BYD's Da Tang on Jun 17, Leapmotor's C10/C11/C16 facelifts on Jun 16). Retail/Wholesale NEV penetration reached 64%/68% in Jun 1-14.

A curated compilation of the most topical charts on weekly passenger vehicle market performance, organized into the following categories: (1) Key NEV brands' weekly orders amount, (2) Key events to watch, (3) NEV/ICE dealer price discount tracker, and (4) Upstream battery pricing dynamics.

## 2026 Week 25 highlights:

■ Key brand orders: BYD / Xiaomi / Leapmotor showed the highest growth at +134%/+44%/+22% wow.

CPCA weekly trend: As of Jun 1-14, PV retail volume was 534k units (-18% yoy/-5% mom), while PV wholesale volume was 556k units (-15% yoy/+8% mom) per CPCA. Meanwhile, NEV retail volume was 341k units (-8% yoy/+5% mom), and NEV wholesale volume was 378k units (+10% yoy/+22% mom), with NEV penetration at 63.9%/67.9% in Jun 1-14, compared to

63%/61.1% in May.

■ Key pricing trends: NEV dealer discount narrowed wow and ICE dealer discount widened wow.

■ Upstream battery pricing dynamics: Battery grade lithium carbonate price decreased to Rmb167.5k/ton (-4.0% wow), while prismatic cell (LFP) and prismatic cell (NCM) prices were stable wow.

Tina Hou
+86(21)2401-8694 |
tina.hou@goldmansachs.cn
GS (China) Securities
Company Limited

Jenny Du
+86(21)2401-8978 |
jenny.x.du@goldmansachs.cn
GS (China) Securities
Company Limited

## Weekly order summary

Key brand weekly order trends during 2026 week 25 (6/15-6/21):

Key NEV OEMs combined orders were $+31\%$ yoy and $+34\%$ wow in week 25 driven by new model launches (e.g. BYD's Da Tang on Jun 17, Leapmotor's C10/C11/C16 facelifts on Jun 16).

BYD / Xiaomi / Leapmotor showed the highest growth at +134%/+44%/+22% wow.

In terms of YTD orders, Nio / HIMA / Tesla showed relatively defensive growth at +96%/+31%/+3% yoy.

Exhibit 1: NEV brand weekly orders summary

<table><tr><td></td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td><td>Jun-26 MTD</td><td>2026 YTD</td></tr><tr><td colspan="8">Monthly order (units)</td></tr><tr><td>BYD (Dynasty &amp; Ocean)</td><td>123535</td><td>96547</td><td>252181</td><td>223899</td><td>197343</td><td>200200</td><td>1093705</td></tr><tr><td>Geely (Galaxy &amp; Zeekr)</td><td></td><td></td><td>85343</td><td>125606</td><td>114161</td><td>75780</td><td>400890</td></tr><tr><td>HIMA</td><td>26347</td><td>19574</td><td>45610</td><td>122320</td><td>143479</td><td>54095</td><td>411425</td></tr><tr><td>Leapmotor</td><td></td><td></td><td>50257</td><td>82036</td><td>67357</td><td>40230</td><td>239880</td></tr><tr><td>Tesla</td><td>30271</td><td>32614</td><td>60929</td><td>61914</td><td>57371</td><td>39900</td><td>283000</td></tr><tr><td>Nio</td><td>15817</td><td>13400</td><td>38190</td><td>44025</td><td>86183</td><td>61950</td><td>259565</td></tr><tr><td>Li Auto</td><td>18243</td><td>14614</td><td>26851</td><td>36401</td><td>43150</td><td>18080</td><td>157340</td></tr><tr><td>Xiaomi</td><td>5529</td><td>10171</td><td>60587</td><td>33513</td><td>33980</td><td>19620</td><td>163400</td></tr><tr><td>XPeng</td><td>16957</td><td>14597</td><td>41607</td><td>39394</td><td>54514</td><td>26830</td><td>193900</td></tr><tr><td>SUM</td><td>236699</td><td>201519</td><td>661556</td><td>769108</td><td>797539</td><td>536685</td><td>3203105</td></tr><tr><td colspan="8">YoY (%)</td></tr><tr><td>BYD (Dynasty &amp; Ocean)</td><td>-57%</td><td>-64%</td><td>-31%</td><td>-29%</td><td>-41%</td><td>-16%</td><td>-40%</td></tr><tr><td>Geely (Galaxy &amp; Zeekr)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>HIMA</td><td>-25%</td><td>-22%</td><td>-21%</td><td>14%</td><td>154%</td><td>82%</td><td>31%</td></tr><tr><td>Leapmotor</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Tesla</td><td>-37%</td><td>-37%</td><td>2%</td><td>55%</td><td>55%</td><td>8%</td><td>3%</td></tr><tr><td>Nio</td><td>-9%</td><td>-2%</td><td>97%</td><td>24%</td><td>190%</td><td>302%</td><td>96%</td></tr><tr><td>Li Auto</td><td>-47%</td><td>-46%</td><td>-20%</td><td>-9%</td><td>-19%</td><td>-33%</td><td>-27%</td></tr><tr><td>Xiaomi</td><td>-86%</td><td>-79%</td><td>-27%</td><td>-5%</td><td>51%</td><td>40%</td><td>-33%</td></tr><tr><td>XPeng</td><td>-18%</td><td>-41%</td><td>-26%</td><td>7%</td><td>18%</td><td>-8%</td><td>-11%</td></tr><tr><td>SUM</td><td>-51%</td><td>-56%</td><td>-22%</td><td>-8%</td><td>6%</td><td>8%</td><td>-21%</td></tr><tr><td colspan="8">MoM (%)</td></tr><tr><td>BYD (Dynasty &amp; Ocean)</td><td>-55%</td><td>-22%</td><td>161%</td><td>-11%</td><td>-12%</td><td></td><td></td></tr><tr><td>Geely (Galaxy &amp; Zeekr)</td><td></td><td></td><td></td><td>47%</td><td>-9%</td><td></td><td></td></tr><tr><td>HIMA</td><td>-52%</td><td>-26%</td><td>133%</td><td>168%</td><td>17%</td><td></td><td></td></tr><tr><td>Leapmotor</td><td></td><td></td><td></td><td>63%</td><td>-18%</td><td></td><td></td></tr><tr><td>Tesla</td><td>-39%</td><td>8%</td><td>87%</td><td>2%</td><td>-7%</td><td></td><td></td></tr><tr><td>Nio</td><td>-49%</td><td>-15%</td><td>185%</td><td>15%</td><td>96%</td><td></td><td></td></tr><tr><td>Li Auto</td><td>-28%</td><td>-20%</td><td>84%</td><td>36%</td><td>19%</td><td></td><td></td></tr><tr><td>Xiaomi</td><td>-63%</td><td>84%</td><td>496%</td><td>-45%</td><td>1%</td><td></td><td></td></tr><tr><td>XPeng</td><td>-43%</td><td>-14%</td><td>185%</td><td>-5%</td><td>38%</td><td></td><td></td></tr><tr><td>SUM</td><td>-51%</td><td>-15%</td><td>161%</td><td>16%</td><td>4%</td><td></td><td></td></tr></table>

Source: ThinkerCar, Data compiled by GS Global Investment Research

<table><tr><td>2025</td><td>2025</td><td>2025</td><td>2025</td><td>2026</td><td>2026</td><td>2026</td><td>2026</td></tr><tr><td>W225/26-6/1</td><td>W236/2-6/8</td><td>W246/9-6/15</td><td>W256/16-6/22</td><td>W225/25-5/31</td><td>W236/1-6/7</td><td>W246/8-6/14</td><td>W256/15-6/21</td></tr><tr><td colspan="8">Weekly order (units)</td></tr><tr><td>80000</td><td>75000</td><td>84000</td><td>80000</td><td>48700</td><td>47700</td><td>45700</td><td>106800</td></tr><tr><td></td><td></td><td></td><td></td><td>22100</td><td>24840</td><td>26760</td><td>24180</td></tr><tr><td>9200</td><td>11400</td><td>9300</td><td>9000</td><td>40680</td><td>24180</td><td>18240</td><td>11675</td></tr><tr><td></td><td></td><td></td><td></td><td>15100</td><td>14600</td><td>11530</td><td>14100</td></tr><tr><td>8000</td><td>12000</td><td>13000</td><td>12000</td><td>14000</td><td>14200</td><td>13100</td><td>12600</td></tr><tr><td>5900</td><td>5400</td><td>5100</td><td>4900</td><td>38810</td><td>28020</td><td>19480</td><td>14450</td></tr><tr><td>11000</td><td>8900</td><td>9200</td><td>9000</td><td>8700</td><td>6650</td><td>5500</td><td>5930</td></tr><tr><td>5000</td><td>5000</td><td>5000</td><td>4000</td><td>8600</td><td>7410</td><td>5010</td><td>7200</td></tr><tr><td>22500</td><td>11300</td><td>9000</td><td>8800</td><td>11100</td><td>9510</td><td>8320</td><td>9000</td></tr><tr><td>141600</td><td>129000</td><td>134600</td><td>127700</td><td>207790</td><td>177110</td><td>153640</td><td>205935</td></tr><tr><td colspan="8">YoY (%)</td></tr><tr><td></td><td></td><td></td><td></td><td>-39%</td><td>-36%</td><td>-46%</td><td>34%</td></tr><tr><td></td><td></td><td></td><td></td><td>342%</td><td>112%</td><td>96%</td><td>30%</td></tr><tr><td></td><td></td><td></td><td></td><td>75%</td><td>18%</td><td>1%</td><td>5%</td></tr><tr><td></td><td></td><td></td><td></td><td>558%</td><td>419%</td><td>282%</td><td>195%</td></tr><tr><td></td><td></td><td></td><td></td><td>-21%</td><td>-25%</td><td>-40%</td><td>-34%</td></tr><tr><td></td><td></td><td></td><td></td><td>72%</td><td>48%</td><td>0%</td><td>80%</td></tr><tr><td></td><td></td><td></td><td></td><td>-51%</td><td>-16%</td><td>-8%</td><td>2%</td></tr><tr><td></td><td></td><td></td><td></td><td>20%</td><td>7%</td><td>-14%</td><td>31%</td></tr><tr><td colspan="8">WoW (%)</td></tr><tr><td>14%</td><td>-6%</td><td>12%</td><td>-5%</td><td>15%</td><td>-2%</td><td>-4%</td><td>134%</td></tr><tr><td></td><td></td><td></td><td></td><td>-39%</td><td>12%</td><td>8%</td><td>-10%</td></tr><tr><td>-10%</td><td>24%</td><td>-18%</td><td>-3%</td><td>92%</td><td>-41%</td><td>-25%</td><td>-36%</td></tr><tr><td></td><td></td><td></td><td></td><td>9%</td><td>-3%</td><td>-21%</td><td>21%</td></tr><tr><td>7%</td><td>50%</td><td>8%</td><td>-8%</td><td>19%</td><td>1%</td><td>-8%</td><td>-4%</td></tr><tr><td>-3%</td><td>-8%</td><td>-6%</td><td>-4%</td><td>228%</td><td>-28%</td><td>-30%</td><td>-26%</td></tr><tr><td>10%</td><td>-19%</td><td>3%</td><td>-2%</td><td>-25%</td><td>-24%</td><td>-17%</td><td>8%</td></tr><tr><td>11%</td><td>0%</td><td>0%</td><td>-20%</td><td>-12%</td><td>-14%</td><td>-32%</td><td>44%</td></tr><tr><td>231%</td><td>-50%</td><td>-20%</td><td>-2%</td><td>-61%</td><td>-14%</td><td>-18%</td><td>8%</td></tr><tr><td>23%</td><td>-9%</td><td>4%</td><td>-5%</td><td>11%</td><td>-15%</td><td>-18%</td><td>34%</td></tr></table>

## Key events to watch

## 2026 Week 26, Jun 22-28

■ Jun 23: Li Auto to officially launch L8 facelift.

■ Jun 23: BYD to launch N8L flash-charging version.

■ Jun 25: Leapmotor to start pre-sales of D99.

■ Jun 28: Nio to start pre-sales of ES8 5-seater version.

## 2026 Week 27, Jun 29-Jul 5

■ Jul 1: NEV OEM monthly volume release.

■ Jul 2: XPeng to launch MONA L03.

## 2026 Week 28, Jul 6-Jul 12

Jul 10-11: CPCA will release PV/NEV industry and by model wholesale/retail data.

## 2026 Week 29-31, Jul 13-Aug 2

■ Aug 1: NEV OEM monthly volume release.

## Retail end-pricing

■ NEV: average dealer discount vs. MSRP was 7.48% as of Jun 20, vs. 7.54%/8.15% as of Jun 13, 2026/Jun 23, 2025; BYD average dealer discount vs. MSRP was 4.27% as of Jun 20, vs. 4.27%/5.50% as of Jun 13, 2026/Jun 23, 2025.

ICE: average dealer discount vs. MSRP was 19.62% as of Jun 20, vs. 19.56%/22.95% as of Jun 13, 2026/Jun 23, 2025.

Exhibit 2: NEV dealer discount trend  
![](images/c8bcfa64cbeae651ab75f7be3f11b8a32f3aa09ce00bfa988d6c65acbccd4b17.jpg)  
By brand dealer discount is based on best-selling models.

![](images/74765722b192c7b12510f3b0a1906d9886ac31770343e752661748abc261644f.jpg)

![](images/12c47a69a32651dc8d4e5334fc6b8821a63f48a80932421feec0ab9c6cf17f2c.jpg)

Source: Autohome, Data compiled by GS Global Investment Research  
Exhibit 3: ICE dealer discount trend  
![](images/29a177481c751b98a8af1c7e95b61e2ad246dd1f6deb01526bc47a0e4b9613f3.jpg)  
By brand dealer discount is based on best-selling models.

![](images/c833d75210915f35677a5fe7d55f484bb82c8e69fb4e3765b6d22fd3e251c6eb.jpg)

ICE dealer discount - domestic brand  
![](images/cc07d3a0111f941af10fb2c24595d44d180b97f8f204f7601b628e8df95b0253.jpg)

## Upstream battery pricing dynamics

Battery grade lithium carbonate price decreased to Rmb167.5k/ton (-4.0% wow), while prismatic cell (LFP) and prismatic cell (NCM) prices were stable wow.

Exhibit 4: Battery and battery raw materials prices

<table><tr><td>Material</td><td>Unit</td><td>4/7/2026</td><td>4/13/2026</td><td>4/20/2026</td><td>4/27/2026</td><td>5/6/2026</td><td>5/11/2026</td><td>5/18/2026</td><td>5/25/2026</td><td>6/1/2026</td><td>6/8/2026</td><td>6/13/2026</td><td>6/22/2026</td><td>WoW</td><td>3Q25</td><td>4Q25</td><td>1Q26</td></tr><tr><td>Cathode</td><td>Unit</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Lithium Carbonate (battery grade)</td><td>Rmb k / ton</td><td>156.5</td><td>155.5</td><td>170.5</td><td>170.5</td><td>177.0</td><td>190.0</td><td>191.0</td><td>181.0</td><td>179.5</td><td>168.5</td><td>174.5</td><td>167.5</td><td>-4.0%</td><td>132%</td><td>91%</td><td>5%</td></tr><tr><td>Battery</td><td>Unit</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Prismatic cell (LFP)</td><td>Rmb / Wh</td><td>0.34</td><td>0.34</td><td>0.34</td><td>0.35</td><td>0.35</td><td>0.35</td><td>0.35</td><td>0.35</td><td>0.35</td><td>0.35</td><td>0.35</td><td>0.35</td><td>0.0%</td><td>14%</td><td>14%</td><td>4%</td></tr><tr><td>Prismatic cell (NCM)</td><td>Rmb / Wh</td><td>0.47</td><td>0.47</td><td>0.47</td><td>0.47</td><td>0.47</td><td>0.47</td><td>0.47</td><td>0.47</td><td>0.47</td><td>0.47</td><td>0.47</td><td>0.47</td><td>0.0%</td><td>13%</td><td>10%</td><td>0%</td></tr></table>

Source: ICC Sino, Data compiled by GS Global Investment Research

## Disclosure Appendix

## Reg AC

We, Tina Hou and Jenny Du, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Contributing Authors: Tina Hou GS (China) Securities Company Limited, Jenny Du GS (China) Securities Company Limited.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses inputs for the fiscal year at least seven quarters in the future compared with the year at least three quarters in the future (on a per-share basis for all metrics).

For a more detailed description of how we calculate the GS Factor Profile, please contact your GS representative.

## M&A Rank

Across our global coverage, we examine stocks using an M&A framework, considering both qualitative factors and quantitative factors (which may vary across sectors and regions) to incorporate the potential that certain companies could be acquired. We then assign a M&A rank as a means of scoring companies under our rated coverage from 1 to 3, with 1 representing high (30%-50%) probability of the company becoming an acquisition target, 2 representing medium (15%-30%) probability and 3 representing low (0%-15%) probability. For companies ranked 1 or 2, in line with our standard departmental guidelines we incorporate an M&A component into our target price. M&A rank of 3 is considered immaterial and therefore does not factor into our price target, and may or may not be discussed in research.

## Quantum

Quantum is GS' proprietary database providing access to detailed financial statement histories, forecasts and ratios. It can be used for in-depth analysis of a single company, or to make comparisons between companies in different sectors and markets.

## Disclosures

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other

ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or dir

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
