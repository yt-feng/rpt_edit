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
This material is neither intended to be distributed to Mainland China investors nor to provide securities investment consultancy services within the territory of Mainland China. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM.

# China Basic Materials

Apr 26 NBS data: Weakening domestic demand to be partially offset by exports; macro and supply are stronger short-term drivers

China's April activity data came in broadly below expectations, with industrial production recording its steepest MoM contraction in three years (link to report). Across our coverage universe, base metals face growing headwinds as US rate hike expectations intensify amid slowing global growth and persistent inflationary pressures. SHFE Aluminum prices hovered at \~RMB 24–25k/t, supported by a structural global supply deficit amid Middle East disruptions and persistent tightness through 2026. Lithium spot briefly touched RMB 200k/t but has since pulled back to \~RMB 190k/t, supported by resilient ESS demand and a recovery in EV adoption driven by elevated oil prices, though we are beginning to see early signs of a mine supply response. For coal and steel, prices have shown a slight recovery, but sustainability hinges on downstream demand follow-through and whether policy-led supply discipline can have a material impact. Zijin Mining remains our top pick despite near-term sentiment being pressured by hawkish repricing. We also like Chalco and China Hongqiao, with the pace of destocking being a key catalyst.

\- April property data came in underwhelming: NBS figures showed signs of deterioration relative to March. New starts declined 27% YoY (vs. -17% in Mar26 YoY and -22% in Apr25 YoY). Completions remained depressed, though the pace of contraction has moderated, falling 19% YoY in April (flat vs. Mar26). Real estate investment stayed subdued at -20% YoY (down vs. -12% Feb26). While home prices continue to show signs of stabilization, JPM property analyst Karl Chan expects new starts to remain weak over the next few months due to soft land sales volume in 1Q26. The new forecast expects a -18% YoY and -19% YoY decline in new starts and completions, respectively, implying a -16% and -17% decline for the rest of the year (link to report).

Figure 1: YTD China property GFA growth   
![](images/5dafb688362e1b7bef900d25130a60fca1e09d896ed7b4bc9d9417c6783d3f6b.jpg)

<details>
<summary>line</summary>

| Date    | FS New Starts | FS Sold | FS Under Construction | FS Completed |
|---------|---------------|---------|------------------------|--------------|
| Jan-18  | ~0%           | ~0%     | ~0%                    | ~0%          |
| Apr-18  | ~0%           | ~0%     | ~0%                    | ~0%          |
| Jul-18  | ~0%           | ~0%     | ~0%                    | ~0%          |
| Oct-18  | ~0%           | ~0%     | ~0%                    | ~0%          |
| Jan-19  | ~0%           | ~0%     | ~0%                    | ~0%          |
| Apr-19  | ~0%           | ~0%     | ~0%                    | ~0%          |
| Jul-19  | ~0%           | ~0%     | ~0%                    | ~0%          |
| Oct-19  | ~0%           | ~0%     | ~0%                    | ~0%          |
| Jan-20  | ~-40%         | ~-20%   | ~-10%                  | ~-15%        |
| Apr-20  | ~-20%         | ~-10%   | ~-5%                   | ~-10%        |
| Jul-20  | ~-10%         | ~-5%    | ~-5%                   | ~-5%         |
| Oct-20  | ~-5%          | ~100%   | ~-5%                   | ~40%         |
| Jan-21  | ~60%          | ~100%   | ~-5%                   | ~40%         |
| Apr-21  | ~20%          | ~20%    | ~-5%                   | ~20%         |
| Jul-21  | ~10%          | ~10%    | ~-5%                   | ~10%         |
| Oct-21  | ~5%           | ~5%     | ~-5%                   | ~5%          |
| Jan-22  | ~-5%          | ~-5%    | ~-5%                   | ~-5%         |
| Apr-22  | ~-10%         | ~-5%    | ~-5%                   | ~-5%         |
| Jul-22  | ~-15%         | ~-5%    | ~-5%                   | ~-5%         |
| Oct-22  | ~-20%         | ~-5%    | ~-5%                   | ~-5%         |
| Jan-23  | ~-25%         | ~-5%    | ~-5%                   | ~-5%         |
| Apr-23  | ~-30%         | ~-5%    | ~-5%                   | ~-5%         |
| Jul-23  | ~-35%         | ~-5%    | ~-5%                   | ~-5%         |
| Oct-23  | ~-40%         | ~-5%    | ~-5%                   | ~-5%         |
| Jan-24  | ~-45%         | ~-5%    | ~-5%                   | ~-5%         |
| Apr-24  | ~-45%         | ~-5%    | ~-5%                   | ~-5%         |
| Jul-24  | ~-45%         | ~-5%    | ~-5%                   | ~-5%         |
| Oct-24  | ~-45%         | ~-5%    | ~-5%                   | ~-5%         |
| Jan-25  | ~-45%         | ~-5%    | ~-5%                   | ~-5%         |
| Apr-25  | ~-45%         | ~-5%    | ~-5%                   | ~-5%         |
| Jul-25  | ~-45%         | ~-5%    | ~-5%                   | ~-5%         |
| Oct-25  | ~-45%         | ~-5%    | ~-5%                   | ~-5%         |
| Jan-26  | ~-45%         | ~-5%    | ~-5%                   | ~-5%         |
| Apr-26  | ~-45%         | ~-5%    | ~-5%                   | ~-5%         |
</details>

Source: NBS, JPM

Figure 2: Completion end vs new starts end commodity performance   
![](images/06b537e45f9229deccd4ad3d7f868ac42f7f1b32e44dc541d59a057b9304d464.jpg)

<details>
<summary>line</summary>

| Month   | Rebar | Cement | Glass | Aluminum (LME) |
|---------|-------|--------|-------|----------------|
| Jan-25  | 100   | 100    | 100   | 100            |
| Feb-25  | 100   | 98     | 98    | 105            |
| Mar-25  | 100   | 96     | 96    | 108            |
| Apr-25  | 100   | 94     | 94    | 106            |
| May-25  | 100   | 92     | 92    | 104            |
| Jun-25  | 100   | 90     | 90    | 102            |
| Jul-25  | 100   | 88     | 88    | 100            |
| Aug-25  | 100   | 86     | 86    | 98             |
| Sep-25  | 100   | 84     | 84    | 96             |
| Oct-25  | 100   | 82     | 82    | 94             |
| Nov-25  | 100   | 80     | 80    | 92             |
| Dec-25  | 100   | 78     | 78    | 90             |
| Jan-26  | 100   | 76     | 76    | 88             |
| Feb-26  | 100   | 74     | 74    | 86             |
| Mar-26  | 100   | 72     | 72    | 84             |
| Apr-26  | 100   | 70     | 70    | 82             |
| May-26  | 100   | 68     | 68    | 80             |
</details>

Source: Bloomberg Finance L.P., JPM

# Asia Basic Materials

# Avery Chan AC

(852) 2800-8659

avery.chan@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

# Sabrina Liu

(852) 2800-8535

sabrina.liu@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

# Frankie Fong

(852) 2800-8574

frankie.fong@JPM.com

JPM Securities (Asia Pacific) Limited

See page 10 for analyst certification and important disclosures, including non-US analyst disclosures.

\- FAI growth slowed significantly in April. In April, total FAI growth declined sharply by 12% YoY (vs. +1.7% YoY in 1Q26), with manufacturing FAI declining by 4% YoY and 16% MoM, reversing from the growth trend in 1Q26 (+4% YoY) amidst energy-shock disruptions. Infrastructure FAI declined by 3% YoY and 24% MoM in April (vs. +9% 1Q26).

Figure 3: YTD China FAI growth   
![](images/6bdc618d9be754a2c1c232cf4a06b960ad3ca319b314ba5bb77e2b7a6e66c4a1.jpg)

<details>
<summary>line</summary>

| Date    | Manufacturing FAI | Infrastructure FAI | Real Estate Development Investment | Total FAI |
|---------|-------------------|--------------------|------------------------------------|-----------|
| Jan-18  | ~5%               | ~10%               | ~10%                               | ~5%       |
| Apr-18  | ~5%               | ~5%                | ~5%                                | ~5%       |
| Jul-18  | ~5%               | ~5%                | ~5%                                | ~5%       |
| Oct-18  | ~5%               | ~5%                | ~5%                                | ~5%       |
| Jan-19  | ~5%               | ~5%                | ~5%                                | ~5%       |
| Apr-19  | ~5%               | ~5%                | ~5%                                | ~5%       |
| Jul-19  | ~5%               | ~5%                | ~5%                                | ~5%       |
| Oct-19  | ~5%               | ~5%                | ~5%                                | ~5%       |
| Jan-20  | ~-30%             | ~-20%              | ~-20%                              | ~-25%     |
| Apr-20  | ~-10%             | ~-5%               | ~-5%                               | ~-10%     |
| Jul-20  | ~0%               | ~0%                | ~0%                                | ~0%       |
| Oct-20  | ~0%               | ~0%                | ~0%                                | ~0%       |
| Jan-21  | ~35%              | ~35%               | ~35%                               | ~35%      |
| Apr-21  | ~20%              | ~20%               | ~20%                               | ~20%      |
| Jul-21  | ~10%              | ~10%               | ~10%                               | ~10%      |
| Oct-21  | ~5%               | ~5%                | ~5%                                | ~5%       |
| Jan-22  | ~20%              | ~10%               | ~10%                               | ~10%      |
| Apr-22  | ~10%              | ~10%               | ~10%                               | ~10%      |
| Jul-22  | ~10%              | ~10%               | ~10%                               | ~10%      |
| Oct-22  | ~10%              | ~10%               | ~10%                               | ~10%      |
| Jan-23  | ~10%              | ~10%               | ~10%                               | ~10%      |
| Apr-23  | ~10%              | ~10%               | ~10%                               | ~10%      |
| Jul-23  | ~10%              | ~10%               | ~10%                               | ~10%      |
| Oct-23  | ~10%              | ~10%               | ~10%                               | ~10%      |
| Jan-24  | ~10%              | ~10%               | ~10%                               | ~10%      |
| Apr-24  | ~10%              | ~10%               | ~10%                               | ~10%      |
| Jul-24  | ~10%              | ~10%               | ~10%                               | ~10%      |
| Oct-24  | ~10%              | ~10%               | ~10%                               | ~10%      |
| Jan-25  | ~10%              | ~10%               | ~10%                               | ~10%      |
| Apr-25  | ~10%              | ~10%               | ~10%                               | ~10%      |
| Jul-25  | ~5%               | ~5%                | ~5%                                | ~5%       |
| Oct-25  | ~5%               | ~5%                | ~5%                                | ~5%       |
| Jan-26  | ~5%               | ~5%                | ~5%                                | ~5%       |
| Apr-26  | ~5%               | ~5%                | ~5%                                | ~5%       |
</details>

Source: NBS, JPM

\- April crude steel output fell 3% YoY; steel product exports declined 9% YoY. China's crude steel production came in at 84mt in April, down 3% YoY, representing an improvement from 1Q26 and bringing 4M26 cumulative output to 331mt, down 4% YoY. The downtrend persists, with early-May CISA key members' daily output at 2.11mn tons (-4.3% YoY). April finished steel exports totaled 9.5mt (-9% YoY, vs. -10% 1Q26 avg). We expect a near-term recovery in steel exports driven by resurgent Middle East demand following tension de-escalation, even as the tailwind from EU front-loading — which supported Q1 volumes — fades under quota constraints. On margins, we are seeing a cost-driven steel price rally since the second half of April, with margins improving off the lows (the share of profitable mills rising to 64% now from 48% in early April; however, with still-sluggish domestic demand and elevated input costs continuing to weigh, we expect no material margin recovery until meaningful policy follow-through materializes.

Figure 4: China YTD Crude Steel Production   
![](images/552d8d1adc2f7854f226f3ad13129e19a6944a78ff8f0c4b3c9c8b262f6c54ab.jpg)

<details>
<summary>bar</summary>

| Month | 2024 (mn tons) | 2025 (mn tons) | YoY % (RHS) |
|-------|----------------|----------------|-------------|
| Feb   | 180            | 170            | -3.6%       |
| Mar   | 250            | 260            | -4.6%       |
| Apr   | 350            | 340            | -4.1%       |
| May   | 450            | 430            |             |
| Jun   | 550            | 520            |             |
| Jul   | 620            | 600            |             |
| Aug   | 700            | 680            |             |
| Sep   | 780            | 750            |             |
| Oct   | 850            | 820            |             |
| Nov   | 950            | 920            |             |
| Dec   | 1050           | 1020           |             |
</details>

Source: NBS, JPM

Figure 5: CISA Key Members Daily Average Crude Steel Output   
![](images/590cf594e953de14fe32546618c012c7a7391b5d1e054842e84b925279bb664b.jpg)

<details>
<summary>line</summary>

| Month | 2022 | 2023 | 2024 | 2025 | 2026 |
|-------|------|------|------|------|------|
| Jan   | 1.9  | 1.9  | 2.0  | 2.1  | 1.9  |
| Feb   | 1.9  | 1.9  | 2.0  | 2.1  | 1.9  |
| Mar   | 1.9  | 2.0  | 2.1  | 2.2  | 2.0  |
| Apr   | 1.9  | 2.1  | 2.1  | 2.2  | 2.0  |
| May   | 1.9  | 2.2  | 2.1  | 2.2  | 2.0  |
| Jun   | 1.9  | 2.3  | 2.2  | 2.1  | 2.1  |
| Jul   | 1.9  | 2.3  | 2.1  | 2.1  | 2.0  |
| Aug   | 1.9  | 2.3  | 2.0  | 2.0  | 1.9  |
| Sep   | 1.9  | 2.3  | 1.9  | 1.9  | 1.8  |
| Oct   | 1.9  | 2.3  | 1.9  | 1.9  | 1.8  |
| Nov   | 1.9  | 2.3  | 1.9  | 1.8  | 1.7  |
| Dec   | 1.9  | 2.3  | 1.8  | 1.7  | 1.6  |
</details>

Source: CISA, JPM

Figure 6: Daily Average Molten Iron Output
mn tons/day   
![](images/107f7ac54626131c346842d8b0b91f6db7ebe66f6e92d1f9a859af3a2b5b599f.jpg)

<details>
<summary>line</summary>

| Month | 2022 | 2023 | 2024 | 2025 | 2026 |
|-------|------|------|------|------|------|
| Jan   | 2.1  | 2.2  | 2.2  | 2.3  | 2.3  |
| Feb   | 2.0  | 2.3  | 2.3  | 2.3  | 2.3  |
| Mar   | 2.1  | 2.4  | 2.3  | 2.3  | 2.3  |
| Apr   | 2.3  | 2.4  | 2.3  | 2.4  | 2.4  |
| May   | 2.4  | 2.5  | 2.4  | 2.4  | 2.4  |
| Jun   | 2.4  | 2.4  | 2.4  | 2.4  | 2.4  |
| Jul   | 2.4  | 2.5  | 2.4  | 2.4  | 2.4  |
| Aug   | 2.1  | 2.5  | 2.4  | 2.4  | 2.4  |
| Sep   | 2.3  | 2.5  | 2.3  | 2.4  | 2.4  |
| Oct   | 2.4  | 2.5  | 2.3  | 2.4  | 2.4  |
| Nov   | 2.3  | 2.4  | 2.3  | 2.4  | 2.4  |
| Dec   | 2.3  | 2.3  | 2.3  | 2.3  | 2.3  |
</details>

Source: Wind, JPM.

Figure 7: CISA Key Member Daily Average Pig Iron Output   
![](images/cb13f25ba9fd269bf19d51058c529a1ad73148e45d238dff2583353248763fd8.jpg)

<details>
<summary>line</summary>

| Month | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|-------|------|------|------|------|------|------|
| Jan   | 1.9  | 1.75 | 1.85 | 1.85 | 1.85 | 1.75 |
| Feb   | 1.95 | 1.7  | 1.9  | 1.9  | 1.95 | 1.8  |
| Mar   | 2.0  | 1.8  | 1.95 | 1.95 | 2.0  | 1.85 |
| Apr   | 1.95 | 1.85 | 1.95 | 1.95 | 1.95 | 1.9  |
| May   | 2.05 | 1.9  | 2.0  | 2.0  | 2.05 | 1.95 |
| Jun   | 2.05 | 1.95 | 2.05 | 2.05 | 2.05 | 1.95 |
| Jul   | 1.95 | 1.85 | 1.95 | 1.95 | 1.95 | 1.95 |
| Aug   | 1.9  | 1.8  | 1.9  | 1.9  | 1.9  | 1.9  |
| Sep   | 1.95 | 1.85 | 1.95 | 1.95 | 1.95 | 1.85 |
| Oct   | 1.85 | 1.75 | 1.85 | 1.85 | 1.85 | 1.75 |
| Nov   | 1.75 | 1.7  | 1.75 | 1.75 | 1.75 | 1.65 |
| Dec   | 1.7  | 1.65 | 1.7  | 1.7  | 1.7  | 1.65 |
| Jan   | -    | -    | -    | -    | -    | -    |
</details>

Source: CISA, JPM

Figure 8: China steel mills operating ratio and profitability   
![](images/a88a99dc949bce86a013e39c33e8283417dce86334f45c986e4afbe08475f603.jpg)

<details>
<summary>line</summary>

| Month   | Operating ratio (EAF) | Operating ratio (BF) | % of sample BF steel mills making profit |
|---------|------------------------|----------------------|------------------------------------------|
| Jan-22  | 50                     | 75                   | 85                                       |
| Mar-22  | 70                     | 80                   | 80                                       |
| May-22  | 60                     | 85                   | 75                                       |
| Jul-22  | 50                     | 80                   | 50                                       |
| Sep-22  | 60                     | 85                   | 60                                       |
| Nov-22  | 50                     | 80                   | 30                                       |
| Jan-23  | 30                     | 75                   | 10                                       |
| Mar-23  | 60                     | 80                   | 60                                       |
| May-23  | 65                     | 85                   | 70                                       |
| Jul-23  | 60                     | 80                   | 65                                       |
| Sep-23  | 65                     | 85                   | 75                                       |
| Nov-23  | 60                     | 80                   | 50                                       |
| Jan-24  | 50                     | 75                   | 30                                       |
| Mar-24  | 60                     | 80                   | 55                                       |
| May-24  | 65                     | 85                   | 60                                       |
| Jul-24  | 60                     | 80                   | 40                                       |
| Sep-24  | 50                     | 75                   | 10                                       |
| Nov-24  | 60                     | 80                   | 70                                       |
| Jan-25  | 65                     | 85                   | 65                                       |
| Mar-25  | 60                     | 80                   | 55                                       |
| May-25  | 65                     | 85                   | 60                                       |
| Jul-25  | 60                     | 80                   | 70                                       |
| Sep-25  | 65                     | 85                   | 65         

[中间内容因长度限制已省略]

pdates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 19 May 2026 11:54 PM HKT

Disseminated 19 May 2026 11:54 PM HKT
"""
