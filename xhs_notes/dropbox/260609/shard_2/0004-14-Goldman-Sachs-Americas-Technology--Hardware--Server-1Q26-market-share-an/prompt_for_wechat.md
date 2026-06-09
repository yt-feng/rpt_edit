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
# Americas Technology: Hardware: Server 1Q26 market share and outlook update

BOTTOM LINE: We update our industry server model to reflect the latest available 1Q26 data from 650 Group. Key takeaways:

AI server forecasts for 2026-2030 raised by \~18% on average, now expected to reach \~\$1.24 tr by 2030 (v. \$961 bn prior per 4Q25 forecasts), with +3% increased outlook across units and +15% increased outlook across ASPs.  
Traditional server forecasts for 2026-2030 raised by \~31% on average, now forecast to reach \~\$164 bn by 2030 (v. \$105 bn prior per 4Q25 forecasts), with +19% increased outlook across units and +10% increased outlook across ASPs.  
DELL's C1Q26 traditional server revenue was up +85% year-over-year, driven by a +24% year-over-year increase in units and a +49% year-over-year increase in ASPs (v. +92% yoy reported growth for F1Q27, three months ending April 30, 2026). By vertical, 650 Group estimates that Dell's C1Q26 traditional server revenue growth was balanced across neoclouds +102% yoy (+34% yoy units, +50% yoy ASPs) and enterprise +91% yoy (+29% units yoy, +48% ASPs yoy). DELL gained market share in traditional server revenue (30% in 1Q26 v. 20% in 1Q25), including share gains in neocloud (35% in 1Q26 v. 26% in 1Q25) and enterprise (38% in 1Q26 v. 25% in 1Q25).  
HPE's C1Q26 traditional server revenue was up $+20\%$ year-over-year driven by flat unit shipments and $+20\%$ increase in ASPs. HPE maintained $11\%$ market share in traditional server revenue (unchanged v. 1Q25), with $17\%$ enterprise traditional server market share (flat yoy) and $7\%$ neocloud market share (v. $8\%$ in 1Q25).

## Server forecast updates

650 Group upgraded its outlook for the server market, now expecting the overall server market to reach \$1.4 tr by 2030 at 38% 2025-2030 CAGR (v. \$1.1 tr on prior 4Q25 forecast). Estimates for the overall server market were raised by 20% on average, with unit shipment expectations revised up \~+13% and ASPs up \~+6% on average.

650 Group raised its annual AI server forecasts for 2026-2030 by \~18% on average, now expecting the AI server market to achieve \~\$1.24 tr by 2030 (v.

Katherine Murphy

+1(212)902-1151

katherine.a.murphy@gs.com

GS & Co. LLC

Michael Ng, CFA

+1(212)902-8618 | michael.ng@gs.com

GS & Co. LLC

Zorayda Montemayor

+1(212)357-6403

zorayda.montemayor@gs.com

GS & Co. LLC

\$961 bn prior per 4Q25 forecasts), with +3% increased outlook across units and +15% increased outlook across ASPs. By vertical, 650 Group raised its outlook for (1) neocloud AI server revenue growth for 2026-2030 by \~22% on average (+4% units, +17% ASPs), (2) hyperscale AI server revenue growth for 2026-2030 by \~17% on average (+3% units, +13% ASPs), and (3) enterprise AI server revenue growth for 2026-30 by \~16% (+1% units, +16% ASPs). 650 Group is forecasting the AI server revenue market to grow at a +45% 5-yr CAGR with +29% growth in units and +12% growth in ASPs.

650 Group raised its annual traditional server forecasts for 2026-2030 by \~31% on average, now expecting the traditional server market to achieve \~\$164 bn by 2030 (v. \$105 bn prior per 4Q25 forecasts), with +19% increased outlook across units and +10% increased outlook across ASPs. By vertical, 650 Group raised its outlook for (1) enterprise traditional server revenue growth for 2026-2030 by \~48% on average (+30% units, +13% ASPs) and (2) hyperscale traditional server revenue growth for 2026-2030 by \~47% on average (+32% units, +10% ASPs). 650 Group is forecasting the traditional server revenue market to grow at a +13% 5-yr CAGR with +5% growth in units and +8% growth in ASPs.

Exhibit 1: 650 Group expects the overall server market to grow to \$1.4 tr by 2030 on growth across both AI (+45% 5-yr CAGR) and traditional servers (+13% 5-yr CAGR)
Global data center server by vertical and AI/traditional (\$, mn)

<table><tr><td rowspan="2">($, mn)</td><td colspan="3">AI Servers</td></tr><tr><td>2025</td><td>2030</td><td>5-yr CAGR</td></tr><tr><td>Hyperscalers</td><td>$135,444</td><td>$611,663</td><td>35%</td></tr><tr><td>Tier 2 Cloud + SP</td><td>$45,209</td><td>$540,481</td><td>64%</td></tr><tr><td>Enterprise</td><td>$14,430</td><td>$91,472</td><td>45%</td></tr><tr><td>Total AI Data Center</td><td>$195,083</td><td>$1,243,616</td><td>45%</td></tr><tr><td rowspan="2"></td><td colspan="3">Traditional Servers</td></tr><tr><td>2025</td><td>2030</td><td>5-yr CAGR</td></tr><tr><td>Hyperscalers</td><td>$20,881</td><td>$35,164</td><td>11%</td></tr><tr><td>Tier 2 Cloud + SP</td><td>$29,539</td><td>$53,548</td><td>13%</td></tr><tr><td>Enterprise</td><td>$38,570</td><td>$74,844</td><td>14%</td></tr><tr><td>Total Traditional Data Center</td><td>$88,990</td><td>$163,556</td><td>13%</td></tr><tr><td rowspan="2"></td><td colspan="3">Total Servers</td></tr><tr><td>2025</td><td>2030</td><td>5-yr CAGR</td></tr><tr><td>Hyperscalers</td><td>$156,325</td><td>$646,827</td><td>33%</td></tr><tr><td>Tier 2 Cloud + SP</td><td>$74,748</td><td>$594,029</td><td>51%</td></tr><tr><td>Enterprise</td><td>$53,000</td><td>$166,315</td><td>26%</td></tr><tr><td>Total Data Center</td><td>$284,073</td><td>$1,407,171</td><td>38%</td></tr></table>

Source: 650 Group

Exhibit 2: 650 Group raised its annual AI server forecasts for 2026-2030 by \~18% on average, now expecting the AI server market to achieve \~\$1.24 tr by 2030 (v. \$961 bn prior per 4Q25 forecasts)  
Industry AI server estimate revisions (\$, mn)  
![](images/d892071fb86a7baaf012472ff7a27dbd710d38921202b80dc8fb00d23fb5ffba.jpg)

<details>
<summary>bar chart</summary>

| Year | Previous (As of 2Q25) ($ mn) | Previous (As of 3Q25) ($ mn) | Previous (As of 4Q25) ($ mn) | Current (As of 1Q26) ($ mn) |
|---|---|---|---|---|
| 2024 | 100,000 | 100,000 | 100,000 | 100,000 |
| 2025 | 200,000 | 200,000 | 200,000 | 200,000 |
| 2026 | 300,000 | 320,000 | 330,000 | 360,000 |
| 2027 | 420,000 | 450,000 | 480,000 | 540,000 |
| 2028 | 520,000 | 580,000 | 640,000 | 760,000 |
| 2029 | 580,000 | 680,000 | 790,000 | 990,000 |
| 2030 | - | 830,000 | 950,000 | 1250,000 |
</details>

Source: 650 Group

Exhibit 3: Traditional server forecasts for 2026-2030 were revised upwards by \~31% on average annually
Industry traditional server estimate revisions (\$, mn)  
![](images/303a17b014b1c0989b405a2ba567fd9fa4748bcfde94dc4606fde68b8e791620.jpg)

<details>
<summary>bar chart</summary>

| Year | Previous (As of 2Q25) ($ mn) | Previous (As of 3Q25) ($ mn) | Previous (As of 4Q25) ($ mn) | Current (As of 1Q26) ($ mn) |
|---|---|---|---|---|
| 2024 | 80,000 | 80,000 | 80,000 | 80,000 |
| 2025 | 82,000 | 83,000 | 107,000 | 107,000 |
| 2026 | 80,000 | 82,000 | 108,000 | 118,000 |
| 2027 | 78,000 | 81,000 | 114,000 | 128,000 |
| 2028 | 75,000 | 80,000 | 102,000 | 139,000 |
| 2029 | 73,000 | 79,000 | 103,000 | 151,000 |
| 2030 | - | 79,000 | 105,000 | 164,000 |
</details>

Source: 650 Group

## C1Q26 vendor market share

DELL gained share in the traditional & AI server markets, with broad-based growth across enterprise and neocloud verticals driven by both unit growth and ASP uplift. Per 650 Group estimates:

DELL's C1Q26 traditional server revenue was up +85% year-over-year (v. +92% reported), driven by a +24% increase in units and a +49% increase in ASPs. By vertical, 650 Group estimates that Dell's C1Q26 traditional server revenue growth was balanced across neoclouds +102% yoy (+34% yoy units, +50% yoy ASPs) and enterprise +91% yoy (+29% units yoy, +48% ASPs yoy). DELL's C1Q26 traditional server hardware revenue of \~\$8.0 bn was \~54% enterprise, \~40% neocloud, \~6% hyperscalers/service provider (v. 52%/36%/12% in C1Q25). DELL gained market share in traditional server revenue (30% in 1Q26 v. 20% in 1Q25), including share gains in neocloud (35% in 1Q26 v. 26% in 1Q25) and enterprise (38% in 1Q26 v. 25% in 1Q25).  
- DELL's C1Q26 AI server revenue was up +\$11.3 bn year-over-year (+622% year-over-year), driven by a +300% increase in units and a +81% increase in ASPs. By vertical, 650 Group estimates that Dell's C1Q26 AI server revenue growth was broadbased across neoclouds (+\$9 bn) and enterprise (+\$2 bn). DELL gained market share in AI server revenue (17% in 1Q26 v. 5% in 1Q25), including share gains in neocloud (48% in 1Q26 v. 24% in 1Q25) and enterprise (47% in 1Q26 v. 17% in 1Q25).

HPE maintained its share in the traditional server market but ceded some share in AI servers. Per 650 Group estimates:

HPE's C1Q26 traditional server revenue was up $+20\%$ year-over-year driven by flat unit shipments and $+20\%$ increase in ASPs. By vertical, 650 Group estimates that HPE's C1Q26 traditional server revenue balanced growth across enterprise $+22\%$ $(+1\%$ units, $+21\%$ ASPs) and neoclouds $+18\%$ $(-1\%$ units, $+19\%$ ASPs). HPE

maintained 11% market share in traditional server revenue (unchanged v. 1Q25), with 17% enterprise traditional server market share (flat YoY) and 7% neocloud market share (v. 8% in 1Q25).

HPE's C1Q26 AI server revenue was up +11% year-over-year (\~flat sequentially), with units -6% year-over-year and ASPs +18%. By vertical, 650 Group estimates that HPE's C1Q26 AI server revenue growth was balanced across neoclouds (+11%) and enterprise (+10%). HPE lost market share in the overall AI server revenue market in enterprise, with 17% share in 1Q26 v. 30% share in 1Q25.

## SMCI lost AI server market share, but gained +1 pt of traditional server market share. Per 650 Group estimates:

SMCI's C1Q26 traditional server revenue was up $+58\%$ year-over-year, with a $-23\%$ decrease in units offset by a $+104\%$ increase in ASPs. Per 650 Group, SMCI primarily sold traditional servers to neoclouds, where it had $10\%$ market share in the quarter (v. $2\%$ market share in 1Q25).  
SMCI's C1Q26 AI server revenue was up +\$5.3 bn year-over-year (+173%), driven by a +164% increase in units and a +4% increase in ASPs. By vertical, 650 Group estimates that SMCI's C1Q26 AI server revenue growth was driven by neoclouds (+260% year-over-year). SMCI gained market share in AI server revenue (11% in 1Q26 v. 8% in 1Q25), with share gains in enterprise (4% share in 1Q26 v. 2% in 1Q25) and service provider (42% v. 9% in 1Q25) more than offsetting weaker market share in neocloud (33% v. 37% in 1Q25)

Exhibit 4: Nvidia leads the AI server market with 44% share as of 1Q26, followed by whitebox players (22%), Dell (17%), and Super Micro (11%)  
AI server revenue market share (%)  
![](images/946442ae1274319da5434ea0460d47127da13dc7506ffd832c1ab52cf2adc207.jpg)

<details>
<summary>line chart</summary>

| Quarter | Dell  | HPE   | Super Micro | Nvidia | Others - White Box |
|---------|-------|-------|-------------|--------|--------------------|
| 1Q23    | 10%   | 10%   | 10%         | 15%    | 50%                |
| 2Q23    | 5%    | 5%    | 15%         | 40%    | 20%                |
| 3Q23    | 5%    | 5%    | 15%         | 65%    | 15%                |
| 4Q23    | 5%    | 5%    | 15%         | 60%    | 10%                |
| 1Q24    | 5%    | 5%    | 15%         | 60%    | 10%                |
| 2Q24    | 5%    | 5%    | 15%         | 60%    | 10%                |
| 3Q24    | 5%    | 5%    | 15%         | 55%    | 10%                |
| 4Q24    | 5%    | 5%    | 15%         | 55%    | 15%                |
| 1Q25    | 5%    | 5%    | 10%         | 50%    | 20%                |
| 2Q25    | 10%   | 5%    | 10%         | 45%    | 20%                |
| 3Q25    | 10%   | 5%    | 10%         | 45%    | 20%                |
| 4Q25    | 10%   | 5%    | 10%         | 40%    | 20%                |
| 1Q26    | 15%   | 5%    | 10%         | 40%    | 20%                |
</details>

Source: 650 Group

Exhibit 5: Neocloud AI server market share leadership oscillates between DELL and SMCI  
Neocloud AI server revenue market share (%)  
![](images/be0b62804bfdd1c7b51f4d0b91079f97f95754a99bd655e80b5e11014466ad12.jpg)

<details>
<summary>line chart</summary>

| Quarter | Dell  | Nvidia | Super Micro |
|---------|-------|--------|-------------|
| 1Q23    | 10%   | 20%    | 30%         |
| 2Q23    | 15%   | 10%    | 70%         |
| 3Q23    | 20%   | 15%    | 45%         |
| 4Q23    | 25%   | 10%    | 55%         |
| 1Q24    | 30%   | 10%    | 40%         |
| 2Q24    | 40%   | 10%    | 35%         |
| 3Q24    | 35%   | 10%    | 40%         |
| 4Q24    | 30%   | 10%    | 45%         |
| 1Q25    | 25%   | 10%    | 35%         |
| 2Q25    | 45%   | 5%     | 30%         |
| 3Q25    | 40%   | 5%     | 25%         |
| 4Q25    | 35%   | 5%     | 50%         |
| 1Q26    | 45%   | 5%     | 30%         |
</details>

Source: 650 Group

Exhibit 6: Dell gained significant share in enterprise AI servers in 1Q26 (47%)  
Enterprise AI server revenue market share  
![](images/d5206e8604fe73a50d16e070a0a1830b61eb8a4c54e656b7e45ec6d41e85022a.jpg)

<details>
<summary>line chart</summary>

| Quarter | Dell | HPE | Nvidia | Super Micro | Others - White Box |
|---------|------|-----|--------|-------------|---------------------|
| 1Q21    | 10%  | 65% | 10%    | 0%          | 0%                  |
| 2Q21    | 10%  | 65% | 10%    | 0%          | 0%                  |
| 3Q21    | 10%  | 70% | 10%    | 0%          | 0%                  |
| 4Q21    | 10%  | 55% | 10%    | 0%          | 0%                  |
| 1Q22    | 10%  | 55% | 10%    | 0%          | 0%                  |
| 2Q22    | 10%  | 55% | 10%    | 0%          | 0%                  |
| 3Q22    | 10%  | 55% | 10%    | 0%          | 0%                  |
| 4Q22    | 10%  | 60% | 10%    | 0%          | 0%                  |
| 1Q23    | 30%  | 30% | 20%    | 0%          | 0%                  |
| 2Q23    | 30%  | 30% | 20%    | 0%          | 0%                  |
| 3Q23    | 30%  | 30% | 20%    | 0%          | 0%                  |
| 4Q23    | 30%  | 30% | 20%    | 0%          | 0%                  |
| 1Q24    | 30%  | 35% | 20%    | 0%          | 0%                  |
| 2Q24    | 30%  | 45% | 20%    | 0%          | 0%                  |
| 3Q24    | 30%  | 45% | 20%    | 0%          | 0%                  |
| 4Q24    | 30%  | 45% | 20%    | 0%          | 0%                  |
| 1Q25    | 30%  | 35% | 20%    | 0%          | 0%                  |
| 2Q25    | 30%  | 35% | 20%    | 0%          | 0%                  |
| 3Q25    | 30%  | 35% | 20%    | 5%          | 0%                  |
| 4Q25    | 35%  | 35% | 15%    | 10%         | 0%                  |
| 1Q26    | 45%  | 15% | 10%    | 5%          | 0%                  |
</details>

Source: 650 Group

Exhibit 7: Dell lead the traditional server market in 1Q26 (30% share), followed by white-box (24%), HPE (11%), Lenovo (7%), and IBM (6%).  
Traditional server revenue market share (%)  
![](images/91aa922ddd44078929a86c3d2e139ce8dc6bbf62fb83d2beef36cb6cdc2e5e4b.jpg)

<details>
<summary>line chart</summary>

| Quarter | Dell  | HPE   | IBM   | Lenovo | Others - White Box |
|---------|-------|-------|-------|--------|---------------------|
| 1Q23    | 17.5% | 17.0% | 6.0%  | 7.0%   | 31.0%               |
| 2Q23    | 17.5% | 17.0% | 6.0%  | 7.0%   | 30.0%               |
| 3Q23    | 17.5% | 17.0% | 6.0%  | 7.0%   | 30.0%               |
| 4Q23    | 17.5% | 17.0% | 6.0%  | 7.0%   | 30.0%               |
| 1Q24    | 15.0% | 14.0% | 6.0%  | 8.0%   | 35.0%               |
| 2Q24    | 15.0% | 13.0% | 6.0%  | 9.0%   | 34.0%               |
| 3Q24    | 20.0% | 12.0% | 6.0%  | 9.0%   | 32.0%               |
| 4Q24    | 20.0% | 12.0% | 6.0%  | 10.0%  | 27.0%               |
| 1Q25    | 20.0% | 12.0% | 6.0%  | 11.0%  | 28.0%               |
| 2Q25    | 15.0% | 13.0% | 6.0%  | 12.0%  | 28.0%               |
| 3Q25    | 22.0% | 12.0% | 6.0%  | 11.0%  | 26.0%               |
| 4Q25    | 19.0% | 12.0% | 8.0%  | 12.0%  | 27.0%               |
| 1Q26    | 30.0% | 11.0% | 6.0%  | 7.0%   | 24.0%               |
</details>

Source: 650 Group

Exhibit 8: Neocloud traditional server market share is more mixed, with DELL and SMCI leading in 1Q26  
Neocloud traditional server market share  
![](images/3e24fcd5372590a775fcda4c26323e839b17191041f7a21c7a5cfd788f4165b6.jpg)

<details>
<summary>line chart</summary>

| Quarter | Dell  | HPE   | IBM   | Lenovo | Super Micro | Others - White Box |
|---------|-------|-------|-------|--------|-------------|--------------------|
| 1Q23    | 12%   | 23%   | 4%    | 10%    | 4%          | 25%                |
| 2Q23    | 15%   | 22%   | 4%    | 10%    | 6%          | 24%                |
| 3Q23    | 18%   | 21%   | 4%    | 10%    | 7%          | 24%                |
| 4Q23    | 20%   | 20%   | 4%    | 10%    | 8%          | 24%                |
| 1Q24    | 18%   | 19%   | 4%    | 10%    | 9%          | 27%                |
| 2Q24    | 15%   | 18%   | 4%    | 10%    | 8%          | 26%                |
| 3Q24    | 17%   | 17%   | 4%    | 10%    | 8%          | 25%                |
| 4Q24    | 20%   | 16%   | 4%    | 10%    | 8%          | 25%                |
| 1Q25    | 23%   | 15%   | 4%    | 10%    | 8%          | 25%                |
| 2Q25    | 25%   | 14%   | 4%    | 10%    | 8%          | 29%                |
| 3Q25    | 15%   | 13%   | 4%    | 10%    | 8%          | 28%                |
| 4Q25    | 28%   | 12%   | 4%    | 8%     | 38%         | 18%                |
| 1Q26    | 43%   | 4%    | 4%    | 8%     | 25%         | 12%                |
</details>

Source: 650 Group

Exhibit 9: DELL leads the enterprise traditional server market with $38\%$ share in 1Q26  
Enterprise traditional server revenue market share  
![](images/c6e651f2c4d79287ea4fad95298c98f9755b01a179b526a7870eec5bed7ac54c.jpg)

<details>
<summary>line chart</summary>

| Quarter | Dell  | HPE   | IBM   | Lenovo | Super Micro |
|---------|-------|-------|-------|--------|-------------|
| 1Q23    | 28%   | 25%   | 10%   | 9%     | 2%          |
| 2Q23    | 27%   | 26%   | 11%   | 9%     | 2%          |
| 3Q23    | 26%   | 27%   | 11%   | 9%     | 2%          |
| 4Q23    | 25%   | 26%   | 11%   | 9%     | 2%          |
| 1Q24    | 24%   | 25%   | 11%   | 10%    | 2%          |
| 2Q24    | 23%   | 24%   | 11%   | 11%    | 2%          |
| 3Q24    | 24%   | 23%   | 11%   | 12%    | 2%          |
| 4Q24    | 25%   | 22%   | 10%   | 13%    | 2%          |
| 1Q25    | 26%   | 21%   | 9%    | 14%    | 3%          |
| 2Q25    | 25%   | 20%   | 8%    | 15%    | 4%          |
| 3Q25    | 24%   | 19%   | 7%    | 16%    | 5%          |
| 4Q25    | 23%   | 18%   | 6%    | 17%    | 3%          |
| 1Q26    | 38%   | 17%   | 13%   | 9%     | 2%          |
</details>

Source: 650 Group

## Dell Technologies (DELL, Buy)

We are Buy rated on DELL with a 12-month target price of \$500 (unchanged) based on 22.0x (uncha

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
