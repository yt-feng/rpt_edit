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
# Global Data Watch: Asia

EMAX resilience drives more hawkishness

# EMAX resilience to energy shock prompts more central bank hawkishness

Asia was always feared to be the region most susceptible to shortages from a prolonged closure of the Strait of Hormuz given its dependence on the region. However, the worst fears have not materialized because the region -- outside of China -- has been able to source imports from other areas. Daily tanker import volumes reveal that May imports of energy in EMAX and India, for example, are rapidly approaching normal levels. Enhanced procurement has been complemented by the running down of national energy reserves and the move to other fuel sources (coal, biofuel) to buffer the hit on activity. These dynamics, in conjunction with continued strong tech momentum – reinforced by this week's April IP prints in the region – alongside fiscal policy supports in some economies, has meant the hit to activity from the energy shock, while visible, is less potent than had been initially feared. But resilience has come at a price, with inflation pressures continuing to build in the region reflected in surging input and output prices in the April PMIs. With growth holding up, central banks have turned their attention to inflation and have become progressively hawkish.

The BSP and Bank of Indonesia have already hiked in recent weeks though for different reasons (the former because of an inflation shock, the latter because FX has come under pressure) and this week the Bank of Korea joined the camp of hawks. While the BoK kept rates on hold, as we had expected, it delivered a strongly hawkish message, signaling a faster and more robust hiking cycle than previously anticipated. The central bank's forward guidance now points to a rate hike as early as July with additional increases likely through next year. This shift is driven by Korea's sustained growth momentum, particularly from the tech sector, and a growing concern that this strength will spill over into demand side-inflation pressures. We therefore now pencil in four 25 bps hikes over the next year (compared to our previous forecast of 50 bps through the end of 2027), with the first hike in July itself.

In contrast, one central bank that is expected to remain patient is India's Reserve Bank of India. Even as markets price in multiple hikes, our longstanding view is that the bar for hikes in India is high. This week, the Governor reiterated the RBI will only react if energy pressures spill into core inflation, and with core very benign at the moment we expect the RBI to remain comfortably on hold at next week's review.

# Emerging Markets Asia, Economic and Policy Research

# Sajjid Z Chinoy

(91-22) 6157-3386

sajjid.z.chinoy@JPM.com

JPM Chase Bank, N.A., Mumbai Branch

# Anusha Mital

(91-22) 6157-4113

anusha.mital@jpmchase.com

JPM India Private Limited

Contents 

<table><tr><td>Australian housing: Grinding gears</td><td>6</td></tr><tr><td colspan="2">Data Watches</td></tr><tr><td>Japan</td><td>8</td></tr><tr><td>Australia and New Zealand</td><td>12</td></tr><tr><td>Greater China</td><td>14</td></tr><tr><td>Korea</td><td>17</td></tr><tr><td>ASEAN</td><td>19</td></tr><tr><td>India</td><td>22</td></tr><tr><td>Regional Data Calendars</td><td>24</td></tr></table>

Figure 1: EMAX tanker imports   
![](images/b06ea547a5e62e6a0b9dcc2a50f1bb6d85a11f547d3c32e7eee58c691a62d8fd.jpg)

<details>
<summary>line</summary>

| X-axis | 2023-25 avg | 2026 |
|--------|-------------|------|
| 1      | ~1.85       | ~1.8 |
| 31     | ~1.85       | ~1.8 |
| 61     | ~1.85       | ~1.8 |
| 91     | ~1.85       | ~1.7 |
| 121    | ~1.85       | ~1.6 |
| 151    | ~1.85       | ~1.7 |
| 181    | ~1.85       | ~1.7 |
| 211    | ~1.85       | ~1.7 |
| 241    | ~1.85       | ~1.7 |
| 271    | ~1.85       | ~1.7 |
| 301    | ~1.85       | ~1.7 |
| 331    | ~1.85       | ~1.7 |
| 361    | ~1.85       | ~1.7 |
</details>

Source: IMF Portwatch, JPM.

Figure 2: India tanker imports   
![](images/86d25b3c1360aa6869aa6dcfff19a85c93569b6c24f002a0ce8b68e9916a53e0.jpg)

<details>
<summary>line</summary>

| Year | 2023-25 avg | 2026 |
|------|-------------|------|
| 1    | ~0.28       | ~0.24 |
| 31   | ~0.29       | ~0.30 |
| 61   | ~0.28       | ~0.28 |
| 91   | ~0.29       | ~0.23 |
| 121  | ~0.31       | ~0.24 |
| 151  | ~0.32       | ~0.36 |
| 181  | ~0.34       | —    |
| 211  | ~0.35       | —    |
| 241  | ~0.33       | —    |
| 271  | ~0.31       | —    |
| 301  | ~0.28       | —    |
| 331  | ~0.27       | —    |
| 361  | ~0.27       | —    |
</details>

Source: IMF Portwatch, JPM

# China: May PMIs to test near-term resilience

The Middle East conflict and energy shocks weighed on China's production and domestic demand in April, raising questions about the economy's resilience. Oil supply disruptions pushed processed oil and petrochemical output into contraction, partly reflecting the difficulties that small refiners face to switch suppliers and weaker incentives for SOE refiners to ramp up production amidst the export ban. Alternative indicators suggest processed crude output may have contracted further in May. Meanwhile, higher coke-oven operating rates point to increased oil-to-coal switching, partially offsetting the drag.

April's activity softness also appears to be associated with some scaling back of fiscal support and greater policy patience (relative to subsidy rollouts in some regional peers). General budget expenditure slipped into contraction, driven by weaker infrastructure outlays despite decent revenue growth. After three months of drawdowns, fiscal deposits jumped in April by more than typical seasonality, helping to explain the recent investment slide. All told, fiscal support has been less frontloaded than we had initially envisaged with the implication that the expected payback in the second half will also be less acute than feared.

Meanwhile, exports remained resilient in April and did the heavy lifting: a stronger-than-expected April rebound offset domestic weakness, though recent tailwinds appear increasingly concentrated in less labor-intensive categories such as memory ICs, EVs, solar, and batteries. Port trackers show slower month-on-month outbound container and bulk deadweight tonnage, pointing to a partial cooling. Taken together, for next week's May PMIs, we expect a modest dip to 50.1 for NBS manufacturing (vs. 50.3 in April) and 51.0 for RatingDog (vs. 52.2 in April).

Table 1: EM Asia data release 

<table><tr><td>Date</td><td>Market</td><td>Data</td><td>Period</td><td>Unit</td><td>JPM</td><td>Consensus</td><td>Previous</td></tr><tr><td rowspan="8">Mon, 01-Jun</td><td>TW</td><td>PMI mfg.</td><td>May</td><td>Index</td><td>53.0</td><td>-</td><td>55.3</td></tr><tr><td>KR</td><td>Trade balance</td><td>May</td><td>US$bn</td><td>23.0</td><td>24.5</td><td>23.8</td></tr><tr><td>KR</td><td>Exports</td><td>May</td><td>%oya</td><td>50.1</td><td>48.4</td><td>48.0</td></tr><tr><td>KR</td><td>Imports</td><td>May</td><td>%oya</td><td>25.2</td><td>21.9</td><td>16.7</td></tr><tr><td>KR</td><td>PMI mfg.</td><td>May</td><td>Index</td><td>53.5</td><td>-</td><td>53.6</td></tr><tr><td>CN</td><td>PMI mfg. (RatingDog)</td><td>May</td><td>Index</td><td>51.0</td><td>51.3</td><td>52.2</td></tr><tr><td>IN</td><td>PMI mfg.</td><td>May</td><td>Index</td><td>-</td><td>-</td><td>54.3</td></tr><tr><td>IN</td><td>IP</td><td>Apr</td><td>%oya</td><td>4.0</td><td>3.8</td><td>4.1</td></tr><tr><td rowspan="7">Tue, 02-Jun</td><td>KR</td><td>CPI</td><td>May</td><td>%oya</td><td>3.0</td><td>2.9</td><td>2.6</td></tr><tr><td>ID</td><td>Trade balance</td><td>Apr</td><td>US$bn</td><td>1.4</td><td>0.2</td><td>3.3</td></tr><tr><td>ID</td><td>Exports</td><td>Apr</td><td>%oya</td><td>3.2</td><td>10.2</td><td>-3.1</td></tr><tr><td>ID</td><td>Imports</td><td>Apr</td><td>%oya</td><td>-2.7</td><td>9.0</td><td>1.5</td></tr><tr><td>ID</td><td>CPI</td><td>May</td><td>%oya</td><td>2.7</td><td>2.9</td><td>2.4</td></tr><tr><td>HK</td><td>Retail sales</td><td>Apr</td><td>%oya</td><td>9.4</td><td>-</td><td>9.8</td></tr><tr><td>SG</td><td>PMI</td><td>May</td><td>Index</td><td>50.9</td><td>-</td><td>50.7</td></tr><tr><td>Wed, 03-Jun</td><td>HK</td><td>PMI</td><td>May</td><td>Index</td><td>50.3</td><td>-</td><td>48.6</td></tr><tr><td>Thu, 04-Jun</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="6">Fri, 05-Jun</td><td>KR</td><td>Current account balance</td><td>May</td><td>US$bn</td><td>29.0</td><td>-</td><td>37.3</td></tr><tr><td>PH</td><td>CPI</td><td>May</td><td>%oya</td><td>6.8</td><td>8.0</td><td>7.2</td></tr><tr><td>IN</td><td>RBI monetary policy meeting</td><td>Jun</td><td>%p.a.</td><td>5.25</td><td>5.25</td><td>5.25</td></tr><tr><td>IN</td><td>GDP</td><td>1Q</td><td>%oya</td><td>7.5</td><td>7.0</td><td>7.8</td></tr><tr><td>TH</td><td>CPI</td><td>May</td><td>%oya</td><td>2.7</td><td>3.2</td><td>2.9</td></tr><tr><td>TW</td><td>CPI</td><td>May</td><td>%oya</td><td>2.1</td><td>2.2</td><td>1.7</td></tr><tr><td colspan="8">During the week</td></tr><tr><td>Sun, 31-May</td><td>CN</td><td>PMI mfg. (NBS)</td><td>May</td><td>US$bn</td><td>50.1</td><td>50.0</td><td>50.3</td></tr></table>

Source: Bloomberg Finance L.P. and JPM forecasts

Regional Economic Outlook in Summary 

<table><tr><td rowspan="3"></td><td colspan="3">2021 Nominal GDP, US$</td><td colspan="3">Real GDP</td><td colspan="3">Consumer prices</td></tr><tr><td rowspan="2">Total billion</td><td rowspan="2">% of region</td><td rowspan="2">per capita</td><td colspan="3">% year-on-year</td><td colspan="3">% year-on-year</td></tr><tr><td>2024</td><td>2025</td><td>2026</td><td>2024</td><td>2025</td><td>2026</td></tr><tr><td>Japan</td><td>4,935</td><td>n.a.</td><td>40,114</td><td>-0.2</td><td>1.1</td><td>0.7</td><td>2.7</td><td>3.2</td><td>2.1</td></tr><tr><td>Australia</td><td>1,634</td><td>n.a.</td><td>64,327</td><td>1.0</td><td>2.0</td><td>2.0</td><td>3.2</td><td>2.8</td><td>4.3</td></tr><tr><td>New Zealand</td><td>247</td><td>n.a.</td><td>48,861</td><td>-0.3</td><td>0.2</td><td>1.9</td><td>2.9</td><td>2.8</td><td>3.7</td></tr><tr><td>Emerging Asia</td><td>26,963</td><td>100.0</td><td>8,048</td><td>4.9</td><td>5.1</td><td>4.8</td><td>1.2</td><td>0.6</td><td>1.8</td></tr><tr><td>ex China and India</td><td>6,175</td><td>22.9</td><td>10,794</td><td>3.9</td><td>3.9</td><td>4.5</td><td>2.1</td><td>1.6</td><td>2.9</td></tr><tr><td>China</td><td>17,706</td><td>65.7</td><td>12,572</td><td>4.9</td><td>5.0</td><td>4.7</td><td>0.2</td><td>0.0</td><td>1.0</td></tr><tr><td>Hong Kong SAR, China</td><td>368</td><td>1.4</td><td>49,849</td><td>2.6</td><td>3.6</td><td>3.4</td><td>1.7</td><td>1.4</td><td>1.6</td></tr><tr><td>Taiwan, China</td><td>777</td><td>2.9</td><td>33,071</td><td>5.3</td><td>8.7</td><td>9.8</td><td>2.2</td><td>1.7</td><td>2.0</td></tr><tr><td>Korea</td><td>1,809</td><td>6.7</td><td>35,126</td><td>2.0</td><td>1.0</td><td>3.0</td><td>2.3</td><td>2.1</td><td>2.7</td></tr><tr><td>India</td><td>3,082</td><td>11.4</td><td>2,250</td><td>6.5</td><td>7.5</td><td>6.0</td><td>4.9</td><td>2.1</td><td>4.6</td></tr><tr><td>Indonesia</td><td>1,187</td><td>4.4</td><td>4,358</td><td>5.0</td><td>5.1</td><td>4.7</td><td>2.3</td><td>1.9</td><td>3.5</td></tr><tr><td>Malaysia</td><td>373</td><td>1.4</td><td>11,476</td><td>5.1</td><td>5.2</td><td>4.6</td><td>1.8</td><td>1.4</td><td>1.9</td></tr><tr><td>Philippines</td><td>393</td><td>1.5</td><td>3,576</td><td>5.7</td><td>4.4</td><td>4.0</td><td>3.2</td><td>1.6</td><td>6.8</td></tr><tr><td>Singapore</td><td>397</td><td>1.5</td><td>79,601</td><td>5.3</td><td>5.0</td><td>4.3</td><td>2.4</td><td>0.9</td><td>2.1</td></tr><tr><td>Thailand</td><td>506</td><td>1.9</td><td>7,237</td><td>2.9</td><td>2.4</td><td>2.1</td><td>0.4</td><td>-0.1</td><td>2.7</td></tr><tr><td>Vietnam</td><td>365</td><td>1.4</td><td>3,757</td><td>7.1</td><td>7.9</td><td>7.3</td><td>3.6</td><td>3.3</td><td>5.3</td></tr><tr><td rowspan="3"></td><td colspan="3">Current account balance</td><td colspan="3">Current account</td><td colspan="3">Foreign reserves</td></tr><tr><td colspan="3">US$ billion</td><td colspan="3">% of GDP</td><td colspan="3">US$ billion</td></tr><tr><td>2024</td><td>2025</td><td>2026</td><td>2024</td><td>2025</td><td>2026</td><td>2024</td><td>2025</td><td>2026</td></tr><tr><td>Japan</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>4.6</td><td>4.8</td><td>3.9</td><td>n.a.</td><td>n.a.</td><td>n.a.</td></tr><tr><td>Australia</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>-2.2</td><td>-2.6</td><td>-2.0</td><td>n.a.</td><td>n.a.</td><td>n.a.</td></tr><tr><td>New Zealand</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>-4.8</td><td>-3.7</td><td>-4.2</td><td>n.a.</td><td>n.a.</td><td>n.a.</td></tr><tr><td>Emerging Asia</td><td>786.9</td><td>1165.0</td><td>1170.4</td><td>2.6</td><td>3.8</td><td>3.6</td><td>n.a.</td><td>n.a.</td><td>n.a.</td></tr><tr><td>ex China and India</td><td>385.9</td><td>456.8</td><td>495.6</td><td>5.4</td><td>6.1</td><td>6.7</td><td>n.a.</td><td>n.a.</td><td>n.a.</td></tr><tr><td>China</td><td>423.9</td><td>747.9</td><td>754.1</td><td>2.3</td><td>3.8</td><td>3.6</td><td>n.a.</td><td>n.a.</td><td>n.a.</td></tr><tr><td>Hong Kong SAR, China</td><td>52.5</td><td>54.7</td><td>47.3</td><td>12.9</td><td>12.8</td><td>10.5</td><td>421</td><td>426</td><td>428</td></tr><tr><td>Taiwan, China</td><td>112.7</td><td>139.3</td><td>135.2</td><td>14.1</td><td>15.1</td><td>13.6</td><td>578</td><td>585</td><td>592</td></tr><tr><td>Korea</td><td>99.0</td><td>122.7</td><td>195.9</td><td>5.3</td><td>6.6</td><td>10.2</td><td>409</td><td>427</td><td>445</td></tr><tr><td>India</td><td>-23.0</td><td>-39.7</td><td>-79.3</td><td>-0.6</td><td>-1.0</td><td>-2.0</td><td>n.a.</td><td>n.a.</td><td>n.a.</td></tr><tr><td>Indonesia</td><td>-8.7</td><td>-10.2</td><td>-15.7</td><td>-0.6</td><td>-0.8</td><td>-1.1</td><td>149</td><td>145</td><td>140</td></tr><tr><td>Malaysia</td><td>7.2</td><td>9.7</td><td>14.9</td><td>1.7</td><td>2.1</td><td>2.8</td><td>124</td><td>127</td><td>130</td></tr><tr><td>Philippines</td><td>-17.5</td><td>-16.3</td><td>-21.9</td><td>-3.8</td><td>-3.3</td><td>-4.4</td><td>95</td><td>91</td><td>74</td></tr><tr><td>Singapore</td><td>98.5</td><td>100.9</td><td>128.0</td><td>17.2</td><td>16.7</td><td>19.9</td><td>n.a.</td><td>n.a.</td><td>n.a.</td></tr><tr><td>Thailand</td><td>11.6</td><td>22.8</td><td>2.3</td><td>2.2</td><td>3.9</td><td>0.4</td><td>217</td><td>249</td><td>270</td></tr><tr><td>Vietnam</td><td>30.5</td><td>33.1</td><td>9.7</td><td>6.8</td><td>6.6</td><td>1.8</td><td>83</td><td>87</td><td>82</td></tr><tr><td rowspan="3"></td><td colspan="3">External debt</td><td colspan="3">Short-term foreign debt</td><td colspan="3">Government balance</td></tr><tr><td colspan="3">% of GDP, end of period</td><td colspan="3">US$ billion, end of period</td><td colspan="3">% of GDP, end of period</td></tr><tr><td>2024</td><td>2025</td><td>2026</td><td>2024</td><td>2025</td><td>2026</td><td>2024</td><td>2025</td><td>2026</td></tr><tr><td>Japan</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>-6.1</td><td>-6.7</td><td>-6.9</td></tr><tr><td>Australia</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>0.0</td><td>-0.4</td><td>-0.6</td></tr><tr><td>New Zealand</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>-2.6</td><td>-2.4</td><td>-2.7</td></tr><tr><td>China</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>-3.0</td><td>-4.0</td><td>-4.0</td></tr><tr><td>Hong Kong SAR, China</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>-1.8</td><td>0.1</td><td>0.6</td></tr><tr><td>Taiwan, China</td><td>26.2</td><td>23.6</td><td>22.5</td><td>207</td><td>213</td><td>221</td><td>-0.6</td><td>-1.0</td><td>-1.6</td></tr><tr><td>Korea</td><td>35.6</td><td>37.9</td><td>40.3</td><td>146</td><td>178</td><td>178</td><td>-1.7</td><td>-1.8</td><td>-0.5</td></tr><tr><td>India</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>-8.4</td><td>-8.0</td><td>-8.3</td></tr><tr><td>Indonesia</td><td>27.4</td><td>25.3</td><td>23.6</td><td>43</td><td>43</td><td>43</td><td>-2.7</td><td>-2.9</td><td>-3.0</td></tr><tr><td>Malaysia</td><td>50.6</td><td>47.3</td><td>44.0</td><td>119</td><td>129</td><td>139</td><td>-4.3</td><td>-3.8</td><td>-3.5</td></tr><tr><td>Philippines</td><td>28.5</td><td>30.6</td><td>33.6</td><td>21</td><td>22</td><td>27</td><td>-5.7</td><td>-4.8</td><td>-6.0</td></tr><tr><td>Singapore</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>0.4</td><td>0.4</td><td>0.2</td></tr><tr><td>Thailand</td><td>37.0</td><td>34.1</td><td>32.1</td><td>86</td><td>75</td><td>75</td><td>-4.0</td><td>-4.7</td><td>-4.5</td></tr><tr><td>Vietnam</td><td>46.1</td><td>47.1</td><td>48.1</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>-3.6</td><td>-3.8</td><td>-4.0</td></tr></table>

Source: National statistics authorities and JPM

Key economic statistics 

<table><tr><td colspan="2"></td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26</td><td>3Q26</td><td>4Q26</td></tr><tr><td colspan="10">Real GDP, %-ch over 1 quarter, saar</td></tr><tr><td colspan="2">Japan</td><td>1.8</td><td>1.4</td><td>-2.5</td><td>0.8</td><td>2.1</td><td>0.2</td><td>1.0</td><td>0.8</td></tr><tr><td colspan="2">Australia</td><td>1.7</td><td>3.4</td><td>1.9</td><td>3.2</td><td>1.3</td><td>1.6</td><td>1.5</td><td>1.9</td></tr><tr><td colspan="2">New Zealand</td><td>4.5</td><td>-3.4</td><td>3.5</td><td>1.0</td><td>3.3</td><td>1.2</td><td>3.4</td><td>1.2</td></tr><tr><td colspan="2">Emerging Asia</td><td>4.7</td><td>4.9</td><td>4.4</td><td>5.6</td><td>6.8</td><td>3.7</td><td>3.4</td><td>3.4</td></tr><tr><td colspan="2">ex China and India</td><td>2.9</td><td>5.3</td><td>5.0</td><td>6.0</td><td>6.5</td><td>2.3</td><td>2.9</td><td>3.0</td></tr><tr><td colspan="2">China</td><td>4.9</td><td>4.2</td><td>3.7</td><td>5.2</td><td>6.7</td><td>4.0</td><td>3.2</td><td>3.2</td></tr><tr><td colspan="2">Hong Kong SAR, China</td><td>4.6</td><td>3.3</td><td>3.8</td><td>4.3</td><td>12.2</td><td>3.0</td><td>2.8</td><td>2.8</td></tr><tr><td colspan="2">Taiwan, China</td><td>6.4</td><td>13.2</td><td>7.4</td><td>23.6</td><td>11.9</td><td>2.2</td><td>3.6</td><td>3.6</td></tr><tr><td colspan="2">Korea</td><td>-0.9</td><td>2.7</td><td>5.4</td><td>-0.6</td><td>6.9</td><td>1.0</td><td>2.0</td><td>2.0</td></tr><tr><td colspan="2">India</td><td>7.2</td><td>8.5</td><td>7.5</td><td>7.5</td><td>7.4</td><td>4.3</td><td>5.5</td><td>5.

[中间内容因长度限制已省略]

aterial only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
