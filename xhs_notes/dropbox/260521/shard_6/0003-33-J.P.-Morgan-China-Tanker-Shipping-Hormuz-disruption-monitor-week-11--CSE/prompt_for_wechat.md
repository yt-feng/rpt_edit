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
# China Tanker Shipping

Hormuz disruption monitor - week 11: CSET recovers as shadow fleet risks build

VLCC freight rebounded again into early May, with momentum strongest around 7–11 May before moderating slightly last week. Partial recovery in Gulf export flows remains supportive for tanker demand and utilization, with Saudi-bound VLCCs recovering to 31 this week from 26 last week, although still below the 48 seen on 22 March. Cosco Shipping Energy Transport (CSET)'s idle rate also declined further to \~5% of active VLCC deployment, the lowest since the conflict erupted, suggesting improving utilization and successful redeployment into alternative trade flows. Meanwhile, TD34/Oman–China and Atlantic Basin VLCC earnings remained historically elevated, indicating tanker markets remain tight as rerouting, resilient oil demand and constrained effective vessel supply continue to support freight. A new emerging risk, however, is that prolonged Iranian influence over Hormuz may gradually complicate the expected tightening cycle for the compliant tanker markets and tanker shipbuilding if recovering Gulf-linked exports increasingly migrate toward Iran-friendly shadow operators rather than compliant listed fleets.

- CSET utilization improved to the strongest level since the conflict began: CSET idle rate declined further to $\sim 5\%$ , the lowest since the conflict erupted, indicating improving fleet utilization despite softer spot momentum. Saudi-bound exposure stabilized modestly, while overall deployment continued to shift toward active trading routes.   
- Atlantic Basin redeployment continued accelerating: CSET's West Africa exposure increased to 11% from only \~2–3% through most of April, while its South America exposure increased further to 19%. By contrast, Middle East exposure remained below pre-conflict levels at \~26% versus >40% in late March.   
- Recovering Gulf exports remained supportive for freight: Saudi-bound VLCC participation recovered to 31 this week from 26 last week. TD34/Oman–China and Atlantic Basin VLCC earnings remained elevated, suggesting tanker supply remains effectively tight.   
- Shadow fleet risks may gradually build under prolonged Iranian influence: If Iran retains effective influence over Hormuz without a full peace settlement, a larger share of Gulf-linked exports may increasingly migrate toward Iran-friendly shadow operators rather than compliant listed fleets. Compliant owners remain more constrained by crew safety concerns, war-risk insurance, and the risk of secondary sanctions if Iran-mediated transit arrangements are viewed as sanctions violations.   
- The key downside risk remains demand destruction: Recovery in Gulf export flows and eventual peace agreements should remain supportive for tanker demand, utilization and cargo recovery, particularly if buyers move into replacement-barrel sourcing or inventory rebuilding. The larger downside risk instead remains a prolonged Hormuz disruption eventually triggering recessionary demand destruction rather than panic restocking.

# Infrastructure, Industrials & Transport

Beatrice Lam AC

(852) 2800-8738

beatrice.lam@JPM.com

Karen Li, CFA

(852) 2800-8589

karen.yy.li@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

# Freight rebounds as utilization improves

VLCC freight rebounded again into early May, with the strongest momentum around 7–11 May before moderating modestly last week. Despite a partial recovery in Gulf export flows, TD34/Oman–China and Atlantic Basin routes remain historically elevated, suggesting tanker markets remain fundamentally tight as rerouting, resilient oil demand and constrained effective vessel supply continue to support freight. More importantly, CSET utilization improved further, with floating storage/waiting exposure declining to \~5% of active VLCC deployment, the lowest since the conflict erupted.

Figure 1: TD15: West Africa-China VLCC earnings remain supported by replacement-barrel demand   
![](images/c34a865c2ca3488f68b32f9752bfba2ba322abd0d1a8a15206e4f3a78e59df4b.jpg)

<details>
<summary>line</summary>

| Month | 2022 | 2023 | 2024 | 2025 | 2026 |
|-------|------|------|------|------|------|
| Jan   | ~10,000 | ~30,000 | ~30,000 | ~30,000 | ~50,000 |
| Feb   | ~15,000 | ~40,000 | ~40,000 | ~40,000 | ~80,000 |
| Mar   | ~25,000 | ~60,000 | ~60,000 | ~60,000 | ~270,000 |
| Apr   | ~30,000 | ~50,000 | ~50,000 | ~50,000 | ~130,000 |
| May   | ~35,000 | ~45,000 | ~45,000 | ~45,000 | ~115,000 |
| Jun   | ~35,000 | ~45,000 | ~45,000 | ~45,000 | ~115,000 |
| Jul   | ~35,000 | ~45,000 | ~45,000 | ~45,000 | ~115,000 |
| Aug   | ~35,000 | ~45,000 | ~45,000 | ~45,000 | ~115,000 |
| Sep   | ~45,000 | ~45,000 | ~45,000 | ~45,000 | ~115,000 |
| Oct   | ~55,000 | ~45,000 | ~45,000 | ~45,000 | ~115,000 |
| Nov   | ~65,000 | ~45,000 | ~45,000 | ~45,000 | ~115,000 |
| Dec   | ~75,000 | ~45,000 | ~45,000 | ~45,000 | ~115,000 |
</details>

Source: Clarksons Research (as of 18 May 2026)

Figure 2: TD22: US Gulf-China VLCC earnings remain elevated on longer-haul trade flows   
![](images/5b8a60fe778553c5ebbdd97a43c94d69b38543b28e0ba1433ed4d6e2997c9607.jpg)

<details>
<summary>line</summary>

| Month | 2022   | 2023   | 2024   | 2025   | 2026   |
|-------|--------|--------|--------|--------|--------|
| Jan   | ~10,000| ~30,000| ~40,000| ~45,000| ~60,000|
| Feb   | ~15,000| ~35,000| ~45,000| ~50,000| ~90,000|
| Mar   | ~20,000| ~40,000| ~50,000| ~55,000| ~180,000|
| Apr   | ~15,000| ~45,000| ~55,000| ~60,000| ~160,000|
| May   | ~10,000| ~45,000| ~55,000| ~65,000| ~110,000|
| Jun   | ~5,000 | ~45,000| ~55,000| ~70,000| ~115,000|
| Jul   | ~15,000| ~45,000| ~55,000| ~75,000| ~115,000|
| Aug   | ~25,000| ~45,000| ~55,000| ~85,000| ~115,000|
| Sep   | ~35,000| ~45,000| ~55,000| ~95,000| ~115,000|
| Oct   | ~45,000| ~45,000| ~55,000| ~115,000| ~115,000|
| Nov   | ~65,000| ~45,000| ~55,000| ~135,000| ~115,000|
| Dec   | ~75,000| ~45,000| ~55,000| ~135,000| ~115,000|
</details>

Source: Clarksons Research (as of 18 May 2026)

Figure 3: TD34/Oman-China VLCC freight remains structurally strong   
![](images/2b13d17d3070ac8badcfa4dd73677c275cab91f91f17bf4a437ac1e27c2b4fa9.jpg)

<details>
<summary>line</summary>

| Date       | Value |
| ---------- | ----- |
| 24-Mar-26  | 220   |
| 31-Mar-26  | 198   |
| 7-Apr-26   | 180   |
| 14-Apr-26  | 185   |
| 21-Apr-26  | 175   |
| 28-Apr-26  | 160   |
| 5-May-26   | 150   |
| 12-May-26  | 140   |
</details>

Source: Clarksons Research (as of 18 May 2026)

# Atlantic Basin redeployment continues to accelerate

CSET deployment continues to shift away from direct Middle East exposure toward replacement-barrel and Atlantic Basin trades. West Africa exposure rose sharply to 11% this week from only \~2–3% through most of April, while South America exposure increased further to 19%. By contrast, Middle East exposure remains structurally below pre-conflict levels at \~26% versus >40% in late March. This suggests compliant

operators increasingly prefer Atlantic Basin deployment.

Figure 4: CSET deployment mix: CSET continues pivoting toward Atlantic Basin replacement-barrel trades 

<table><tr><td rowspan="2"></td><td colspan="8">Cosco Shipping Energy VLCC-in-transit % breakdown</td></tr><tr><td>22nd Mar</td><td>29th Mar</td><td>5th Apr</td><td>12th Apr</td><td>26th Apr</td><td>3rd May</td><td>10th May</td><td>17th May</td></tr><tr><td>Southeast Asia</td><td>13%</td><td>11%</td><td>15%</td><td>15%</td><td>10%</td><td>12%</td><td>24%</td><td>18%</td></tr><tr><td>Middle East</td><td>42%</td><td>34%</td><td>25%</td><td>32%</td><td>24%</td><td>24%</td><td>21%</td><td>26%</td></tr><tr><td>Waiting</td><td>15%</td><td>13%</td><td>15%</td><td>15%</td><td>31%</td><td>17%</td><td>14%</td><td>5%</td></tr><tr><td>South America</td><td>3%</td><td>5%</td><td>5%</td><td>5%</td><td>10%</td><td>10%</td><td>11%</td><td>19%</td></tr><tr><td>North America</td><td>5%</td><td>5%</td><td>5%</td><td>5%</td><td>10%</td><td>10%</td><td>8%</td><td>3%</td></tr><tr><td>Intra-region</td><td>2%</td><td>3%</td><td>2%</td><td>0%</td><td>2%</td><td>10%</td><td>8%</td><td>5%</td></tr><tr><td>Southern Africa</td><td>5%</td><td>11%</td><td>13%</td><td>15%</td><td>0%</td><td>5%</td><td>5%</td><td>5%</td></tr><tr><td>In Hormuz</td><td>8%</td><td>8%</td><td>8%</td><td>5%</td><td>5%</td><td>5%</td><td>5%</td><td>3%</td></tr><tr><td>West Africa</td><td>3%</td><td>3%</td><td>3%</td><td>5%</td><td>2%</td><td>2%</td><td>3%</td><td>11%</td></tr><tr><td>Central Africa</td><td>5%</td><td>3%</td><td>5%</td><td>3%</td><td>5%</td><td>5%</td><td>0%</td><td>5%</td></tr><tr><td>East Africa</td><td>0%</td><td>3%</td><td>3%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>South Asia</td><td>0%</td><td>3%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr></table>

Source: Clarksons Research data and Vessel Finder AIS data compiled by JPM (as of 18 May 2026)

Figure 5: China remained the largest destination for Asian import-in-transit crude flows 

<table><tr><td></td><td>Share of import in-transit VLCC flows (by destination)</td></tr><tr><td>China</td><td>29.8%</td></tr><tr><td>Singapore</td><td>23.6%</td></tr><tr><td>South Korea</td><td>15.1%</td></tr><tr><td>Japan</td><td>11.1%</td></tr><tr><td>Taiwan</td><td>5.2%</td></tr><tr><td>India</td><td>5.2%</td></tr><tr><td>Malaysia</td><td>4.2%</td></tr><tr><td>Sri Lanka</td><td>4.2%</td></tr><tr><td>Hong Kong</td><td>1.1%</td></tr><tr><td>Indonesia</td><td>0.5%</td></tr></table>

Source: Clarksons Research data and Vessel Finder AIS data compiled by JPM (as of 18 May 2026)

Figure 6: North America surpassed the Middle East as Asia's largest VLCC crude origin 

<table><tr><td></td><td>Share of import-in-transit VLCC flows (by origin)</td></tr><tr><td>North America</td><td>22.7%</td></tr><tr><td>East Asia</td><td>18.9%</td></tr><tr><td>Middle East</td><td>18.1%</td></tr><tr><td>Southeast Asia</td><td>16.7%</td></tr><tr><td>West Africa</td><td>11.6%</td></tr><tr><td>South America</td><td>7.8%</td></tr><tr><td>Central Africa</td><td>2.1%</td></tr><tr><td>South Asia</td><td>2.0%</td></tr></table>

Source: Clarksons Research data and Vessel Finder AIS data compiled by JPM (as of 18 May 2026)

Figure 7: Atlantic Basin and Indian Ocean routes now dominate in-transit VLCC positioning 

<table><tr><td></td><td>Share of in-transit VLCC flows (by current location)</td></tr><tr><td>Indian Ocean</td><td>29.0%</td></tr><tr><td>Atlantic Basin</td><td>23.9%</td></tr><tr><td>East Asia</td><td>19.5%</td></tr><tr><td>Southeast Asia</td><td>14.6%</td></tr><tr><td>Persian Gulf</td><td>6.6%</td></tr><tr><td>Red Sea</td><td>5.2%</td></tr><tr><td>Pacific Basin</td><td>1.2%</td></tr></table>

Source: Clarksons Research data and Vessel Finder AIS data compiled by JPM (as of 18 May 2026)

# Gulf recovery remains partial

Saudi-bound VLCC participation recovered to 31 this week from 26 last week, but still remains below the 48 seen on 22 March. Bahri participation recovered to 15 VLCCs, while CSET and CMES remained limited at only one VLCC each. Recovering Gulf exports remain supportive for tanker demand and utilization in the near term, particularly if replacement-barrel demand and inventory rebuilding continue.

Figure 8: Saudi-bound VLCC participation recovers modestly from April lows 

<table><tr><td rowspan="2"></td><td colspan="8">Saudi-bound VLCCs (Number)</td></tr><tr><td>22nd Mar</td><td>29th Mar</td><td>5th Apr</td><td>12th Apr</td><td>26th Apr</td><td>3rd May</td><td>10th May</td><td>17th May</td></tr><tr><td>Angelicoussis Group</td><td>3</td><td>2</td><td>2</td><td>-</td><td>2</td><td>1</td><td>-</td><td>2</td></tr><tr><td>Bahri</td><td>22</td><td>24</td><td>20</td><td>5</td><td>14</td><td>13</td><td>12</td><td>15</td></tr><tr><td>Cosco Shipping Energy</td><td>8</td><td>4</td><td>-</td><td>3</td><td>4</td><td>3</td><td>1</td><td>1</td></tr><tr><td>China Merchants</td><td>-</td><td>1</td><td>-</td><td>4</td><td>3</td><td>4</td><td>3</td><td>1</td></tr><tr><td>DHT Holdings</td><td>1</td><td>1</td><td>1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Fredriksen Group</td><td>2</td><td>1</td><td>1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1</td></tr><tr><td>Sinokor Merchant</td><td>3</td><td>3</td><td>6</td><td>3</td><td>5</td><td>4</td><td>7</td><td>7</td></tr><tr><td>Others</td><td>9</td><td>4</td><td>4</td><td>5</td><td>7</td><td>6</td><td>3</td><td>4</td></tr><tr><td>Total</td><td>48</td><td>40</td><td>34</td><td>20</td><td>35</td><td>31</td><td>26</td><td>31</td></tr></table>

Source: Clarksons Research data and Vessel Finder AIS data compiled by JPM (as of 18 May 2026)

Figure 9: CSET continues redeploying toward Atlantic Basin and replacement-barrel trades 

<table><tr><td rowspan="2"></td><td colspan="8">Cosco Shipping Energy VLCC-in-transit % breakdown</td></tr><tr><td>22nd Mar</td><td>29th Mar</td><td>5th Apr</td><td>12th Apr</td><td>26th Apr</td><td>3rd May</td><td>10th May</td><td>17th May</td></tr><tr><td>Southeast Asia</td><td>13%</td><td>11%</td><td>15%</td><td>15%</td><td>10%</td><td>12%</td><td>24%</td><td>18%</td></tr><tr><td>Middle East</td><td>42%</td><td>34%</td><td>25%</td><td>32%</td><td>24%</td><td>24%</td><td>21%</td><td>26%</td></tr><tr><td>Waiting</td><td>15%</td><td>13%</td><td>15%</td><td>15%</td><td>31%</td><td>17%</td><td>14%</td><td>5%</td></tr><tr><td>South America</td><td>3%</td><td>5%</td><td>5%</td><td>5%</td><td>10%</td><td>10%</td><td>11%</td><td>19%</td></tr><tr><td>North America</td><td>5%</td><td>5%</td><td>5%</td><td>5%</td><td>10%</td><td>10%</td><td>8%</td><td>3%</td></tr><tr><td>Intra-region</td><td>2%</td><td>3%</td><td>2%</td><td>0%</td><td>2%</td><td>10%</td><td>8%</td><td>5%</td></tr><tr><td>Southern Africa</td><td>5%</td><td>11%</td><td>13%</td><td>15%</td><td>0%</td><td>5%</td><td>5%</td><td>5%</td></tr><tr><td>In Hormuz</td><td>8%</td><td>8%</td><td>8%</td><td>5%</td><td>5%</td><td>5%</td><td>5%</td><td>3%</td></tr><tr><td>West Africa</td><td>3%</td><td>3%</td><td>3%</td><td>5%</td><td>2%</td><td>2%</td><td>3%</td><td>11%</td></tr><tr><td>Central Africa</td><td>5%</td><td>3%</td><td>5%</td><td>3%</td><td>5%</td><td>5%</td><td>0%</td><td>5%</td></tr><tr><td>East Africa</td><td>0%</td><td>3%</td><td>3%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>South Asia</td><td>0%</td><td>3%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr></table>

Source: Clarksons Research data and Vessel Finder AIS data compiled by JPM (as of 18 May 2026)

# Deployment divergence continues to widen across owners

Fleet deployment remains increasingly bifurcated between operators maintaining cautious Middle East exposure and operators redeploying toward the Atlantic Basin and replacement-barrel trades.

Figure 10: Idle rate continues declining across VLCC fleets 

<table><tr><td></td><td>Share of active VLCC fleet %</td></tr><tr><td>Floating Storage/Waiting</td><td>33.7%</td></tr><tr><td>Intra-region</td><td>11.4%</td></tr><tr><td>In Hormuz</td><td>6.8%</td></tr><tr><td>Southeast Asia→Middle East</td><td>5.0%</td></tr><tr><td>East Asia→Southeast Asia</td><td>4.8%</td></tr><tr><td>North America→East Asia</td><td>4.3%</td></tr><tr><td>Middle East→East Asia</td><td>4.2%</td></tr><tr><td>Southeast Asia→East Asia</td><td>2.9%</td></tr><tr><td>Southeast Asia→South America</td><td>2.8%</td></tr><tr><td>Southeast Asia→North America</td><td>2.8%</td></tr><tr><td>Middle East→Southeast Asia</td><td>1.7%</td></tr><tr><td>West Africa→East Asia</td><td>1.7%</td></tr><tr><td>South America→East Asia</td><td>1.6%</td></tr><tr><td>North America→Southeast Asia</td><td>1.5%</td></tr><tr><td>Southeast Asia→South Asia</td><td>1.3%</td></tr><tr><td>Others</td><td>13.6%</td></tr></table>

Source: Clarksons Research data and Vessel Finder AIS data compiled by JPM (as of 18 May 2026)

Figure 11: CSET continues pivoting toward Atlantic Basin replacement-barrel trades 

<table><tr><td></td><td>Share of active CSET VLCC fleet %</td></tr><tr><td>Middle East→East Asia</td><td>23.2%</td></tr><tr><td>East Asia→Southeast Asia</td><td>10.4%</td></tr><tr><td>Southeast Asia→South America</td><td>8.2%</td></tr><tr><td>West Africa→East Asia</td><td>8.0%</td></tr><tr><td>South America→East Asia</td><td>8.0%</td></tr><tr><td>Southeast Asia→South Asia</td><td>7.7%</td></tr><tr><td>Intra-region</td><td>5.4%</td></tr><tr><td>Floating Storage/Waiting</td><td>5.3%</td></tr><tr><td>Southeast Asia→Central Africa</td><td>5.3%</td></tr><tr><td>Southeast Asia→Southern Africa</td><td>5.3%</td></tr><tr><td>In Hormuz</td><td>2.7%</td></tr><tr><td>South America→Southeast Asia</td><td>2.7%</td></tr><tr><td>Southeast Asia→North America</td><td>2.7%</td></tr><tr><td>West Africa→Southeast Asia</td><td>2.7%</td></tr><tr><td>Southeast Asia→Middle East</td><td>2.6%</td></tr></table>

Source: Clarksons Research data and Vessel Finder AIS data compiled by JPM (as of 18 May 2026)

Figure 12: CMES maintains diversified exposure across Atlantic and Asia routes 

<table><tr><td></td><td>Share of active CMES VLCC fleet %</td></tr><tr><td>Floating Storage/Waiting</td><td>23.6%</td></tr><tr><td>Intra-region</td><td>10.2%</td></tr><tr><td>North America→East Asia</td><td>10.2%</td></tr><tr><td>Southeast Asia→North America</td><td>8.0%</td></tr><tr><td>Middle East→East Asia</td><td>7.7%</td></tr><tr><td>West Africa→East Asia</td><td>6.1%</td></tr><tr><td>North America→Southeast Asia</td><td>4.1%</td></tr><tr><td>Southeast Asia→West Africa</td><td>4.1%</td></tr><tr><td>Central Africa→East Asia</td><td>4.0%</td></tr><tr><td>Southeast Asia→Southern Africa</td><td>3.9%</td></tr><tr><td>Central America→East Asia</td><td>2.1%</td></tr><tr><td>West Africa→Southeast Asia</td><td>2.1%</td></tr><tr><td>South America→Southeast Asia</td><td>2.1%</td></tr><tr><td>Southeast Asia→South America</td><td>2.1%</td></tr><tr><td>Southeast Asia→East Asia</td><td>2.1%</td></tr><tr><td>Others</td><td>7.9%</td></tr></table>

Source: Clarksons Research data and Vessel Finder AIS data compiled by JPM (as of 18 May 2026)

Figure 13: Sinokor continues maintaining elevated Hormuz exposure and floating storage positioning 

<table><tr><td></td><td>Share of active Sinkor VLCC fleet %</td></tr><tr><td>Floating Storage/Waiting</td><td>34.9%</td></tr><tr><td>In Hormuz</td><td>8.7%</td></tr><tr><td>Intra-region</td><td>8.3%</td></tr><tr><td>Southeast Asia→Middle East</td><td>6.2%</td></tr><tr><td>North America→East Asia</td><td>5.7%</td></tr><tr><td>East Asia→Southeast Asia</td><td>5.7%</td></tr><tr>

[中间内容因长度限制已省略]

dates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 20 May 2026 02:16 AM HKT

Disseminated 20 May 2026 02:16 AM HKT
"""
