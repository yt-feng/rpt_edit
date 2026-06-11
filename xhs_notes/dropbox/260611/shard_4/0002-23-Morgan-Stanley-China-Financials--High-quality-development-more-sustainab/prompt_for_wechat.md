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
## Investor Presentation | Asia Pacific

# China Financials: High-quality development more sustainable for the financial system in China

## Related reports:

China Financials: Earlier-than-expected NIM rebound and decline in overcapacity risk (25 May 2026)

China Financials: Tracking industrial risks: still healthy profit growth and reduction of overcapacity risks despite slower headline macro numbers (3 Jun 2026)

China Financials: 1Q26: healthy payment data; Some consumption payment returned to bank cards (1 Jun 2026)

China Financials: Further rationalization in loan growth with continued new household savings shifting to investments (14 May 2026)

China Financials: Another Milestone Policy Change – No More Quantitative Target for Inclusive SME loans (20 May 2026)

MS ASIA LIMITED+

## Richard Xu, CFA

Equity Analyst

Richard.Xu@morganstanley.com +852 2848-6729

## Beryl Yang

Research Associate

Beryl.Yang@morganstanley.com +852 3963-2224

## Chiyao Huang

Equity Analyst

Chiyao.Huang@morganstanley.com +852 3963-4624

## Chenqian Liu

Research Associate

Chenqian.Liu@morganstanley.com +852 3963-0359

## Asia Summer School 2026

![](images/b2be23037ff3e1053829d03bb27518f854ef46a13ba8c695fdacb5d6082ce683.jpg)

## CHINA FINANCIALS

Asia Pacific

Industry View

Attractive

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## High-quality Development More Sustainable for the Financial System in China

Despite some divergence among major economic data and volatility in recent months, we believe a high-quality development approach without significant stimulus better supports a more sustainable financial system in China.

More evidence of an earlier-than-expected positive loop for China Financials:

o Strong export growth supported by tech and industrial upgrades, offsetting risks from prior stimulus;  
- Gradually easing PPI pressure with improving industrial profitability;  
o Strong growth in household financial assets, alongside a recovery in consumption payment;  
○ Moderating TSF growth amid support from government bonds and more rational loan growth.

We expect an earlier-than-expected NIM rebound, more reasonable balance sheet growth, healthy fee income growth, and lower credit cost assumptions over the coming years for China's banks. This should support revenue and earnings growth, as well as steady performance among China's banks.

China Financials: Earlier-than-expected NIM rebound and decline in overcapacity risk (25 May 2026)

## Healthy 1Q26 Payment Data

Total system payment volume picked up 29% YoY in 1Q26 vs 5% in 4Q25  
![](images/3885172bd5e05b4715a3656f6625d7feb998d48e8135434f0b3d9517f3b49ae5.jpg)

<details>
<summary>line chart</summary>

Total system payment volume yoy
| Date | Total system payment volume yoy (%) |
|---|---|
| 2012-12 | 28.0 |
| 2013-06 | 27.0 |
| 2013-12 | 13.0 |
| 2014-06 | 11.0 |
| 2014-12 | 20.0 |
| 2015-06 | 10.0 |
| 2015-12 | 27.0 |
| 2016-06 | 49.0 |
| 2016-12 | 15.0 |
| 2017-06 | 5.0 |
| 2017-12 | 3.0 |
| 2018-06 | 13.0 |
| 2018-12 | 14.0 |
| 2019-06 | 16.0 |
| 2019-12 | 8.0 |
| 2020-06 | 4.0 |
| 2020-12 | 25.0 |
| 2021-06 | 30.0 |
| 2021-12 | 10.0 |
| 2022-06 | 14.0 |
| 2022-12 | 22.0 |
| 2023-06 | 8.0 |
| 2023-12 | 13.0 |
| 2024-06 | -3.0 |
| 2024-12 | -8.0 |
| 2025-06 | -13.0 |
| 2025-12 | 29.3 |
</details>

UnionPay payment growth rebounded from 4Q, up 11.2% YoY...  
![](images/7ee573c5af816a88bc92eb7ace6aa3899d94cd2552270c2026a7f3beb4d3b76e.jpg)

<details>
<summary>bar-line hybrid</summary>

| Quarter | NetsUnion payment volume - Rmb bn | YoY (%) |
|---|---|---|
| 1Q20 | 63,000 | 7.5 |
| 2Q20 | 78,000 | 11.5 |
| 3Q20 | 98,000 | 12.5 |
| 4Q20 | 110,000 | 12.0 |
| 1Q21 | 104,000 | 65.0 |
| 2Q21 | 112,000 | 12.5 |
| 3Q21 | 122,000 | 9.0 |
| 4Q21 | 125,000 | 6.5 |
| 1Q22 | 106,000 | 4.5 |
| 2Q22 | 104,000 | -1.5 |
| 3Q22 | 120,000 | -3.5 |
| 4Q22 | 122,000 | -3.5 |
| 1Q23 | 118,000 | 6.5 |
| 2Q23 | 123,000 | 7.5 |
| 3Q23 | 133,000 | 6.5 |
| 4Q23 | 122,000 | 4.5 |
| 1Q24 | 122,000 | 4.5 |
| 2Q24 | 132,000 | 4.5 |
| 3Q24 | 145,000 | 6.5 |
| 4Q24 | 138,000 | 13.5 |
| 1Q25 | 145,000 | 17.5 |
| 2Q25 | 155,000 | 18.5 |
| 3Q25 | 160,000 | 18.5 |
| 4Q25 | 158,000 | 16.5 |
| 1Q26 | 150,000 | 7.2 |
</details>

Source: PBOC, CEIC, MS.

Bank card consumption growth turned positive, up 3.2% YoY, vs a decline in 2025  
![](images/4c872cfaa7c4ee371be0ce7b4283625f9aebb9c237426cb305bb215e29d69812.jpg)

<details>
<summary>bar-line hybrid</summary>

| Q1:26 | - | - |
| --- | --- | --- |
| Q2:26 | - | - |
| Q3:26 | - | - |
| Q4:26 | - | - |
| Q1:27: End of next quarter (not labeled) | - | - |
| Q2:27: End of next quarter (not labeled) | - | - |
| Q3:27: End of next quarter (not labeled) | - | - |
| Q4:27: End of next quarter (not labeled) | - | - |
| Q1:28: End of next quarter (not labeled) | - | - |
| Q2:28: End of next quarter (not labeled) | - | - |
| Q3:28: End of next quarter (not labeled) | - | - |
| Q4:28: End of next quarter (not labeled) | - | - |
| Q1:29: End of next quarter (not labeled) | - | - |
| Q2:29: End of next quarter (not labeled) | - | - |
| Q3:29: End of next quarter (not labeled) | - | - |
| Q4:29: End of next quarter (not labeled) | - | - |
| Q1:30: End of next quarter (not labeled) | - | - |
| Q2:30: End of next quarter (not labeled) | - | - |
| Q3:30: End of next quarter (not labeled) | - | - |
| Q4:30: End of next quarter (not labeled) | - | - |
| Q1:31: End of next quarter (not labeled) | - | - |
| Q2:31: End of next quarter (not labeled) | - | - |
| Q3:31: End of next quarter (not labeled) | - | - |
| Q4:31: End of next quarter (not labeled) | - | - |
| Q1:32: End of next quarter (not labeled) | - | - |
| Q2:32: End of next quarter (not labeled) | - | - |
| Q3:32: End of next quarter (not labeled) | - | - |
| Q4:32: End of next quarter (not labeled) | - | - |
| Q1:33: End of next quarter (not labeled) | - | - |
| Q2:33: End of next quarter (not labeled) | - | - |
| Q3:33: End of next quarter (not labeled) | - | - |
| Q4:33: End of next quarter (not labeled) | - | - |
| Q1:34: End of next quarter (not labeled) | - | - |
| Q2:34: End of next quarter (not labeled) | - | - |
| Q3:34: End of next quarter (not labeled) | - | - |
| Q4:34: End of next quarter (not labeled) | - | - |
| Q1:35: End of next quarter (not labeled) | - | - |
| Q2:35: End of next quarter (not labeled) | - | - |
| Q3:35: End of next quarter (not labeled) | - | - |
| Q4:35: End of next quarter (not labeled) | - | - |
| Q1:36: End of next quarter (not labeled) | - | - |
| Q2:36: End of next quarter (not labeled) | - | - |
| Q3:36: End of next quarter (not labeled) | - | - |
| Q4:36: End of next quarter (not labeled) | - | - |
| Q1:37: End of next quarter (not labeled) | - | - |
| Q2:37: End of next quarter (not labeled) | - | - |
| Q3:37: End of next quarter (not labeled) | - | - |
| Q4:37: End of next quarter (not labeled) | - | - |
| Q1:38: End of next quarter (not labeled) | - | - |
| Q2:38: End of next quarter (not labeled) | - | - |
| Q3:38: End of next quarter (not labeled) | - | - |
| Q4:38: End of next quarter (not labeled) | - | - |
| Q1:39: End of next quarter (not labeled) | - | - |
| Q2:39: End of next quarter (not labeled) | - | - |
| Q3:39: End of next quarter (not labeled) | - | - |
| Q4:39: End of next quarter (not labeled) | - | - |
| Q1:40: End of next quarter (not labeled) | - | - |
| Q2:40: End of next quarter (not labeled) | - | - |
| Q3:40: End of next quarter (not labeled) | - | - |
| Q4:40: End of next quarter (not labeled) | - | - |
| Q1:41: End of next quarter (not labeled) | - | - |
| Q2:41: End of next quarter (not labeled) | - | - |
| Q3:41: End of next quarter (not labeled) | - | - |
| Q4:41: End of next quarter (not labeled) | - | - |
| Q1:42: End of next quarter (not labeled) | - | - |
| Q2:42: End of next quarter (not labeled) | - | - |
| Q3:42: End of next quarter (not labeled) | - | - |
| Q4:42: End of next quarter (not labeled) | - | - |
| Q1:43: End of next quarter (not labeled) | - | - |
| Q2:43: End of next quarter (not labeled) | - | - |
| Q3:43: End of next quarter (not labeled) | - | - |
| Q4:43: End of next quarter (not labeled) | - | - |
</details>

...while NetsUnion payment growth slightly moderated to 7.2% YoY  
![](images/bbb27b95a2bae5d9680ffdd191903046a223f4faed240d00eb4bf7c3940f8fe9.jpg)

<details>
<summary>bar-line hybrid</summary>

| Quarter | UnionPay Payment Volume - Rmb bn | YoY Growth |
| ------- | --------------------------------- | ---------- |
| 3Q16    | 18,000                            | 35%        |
| 1Q17    | 20,000                            | 40%        |
| 3Q17    | 22,000                            | 45%        |
| 1Q18    | 25,000                            | 50%        |
| 3Q18    | 28,000                            | 35%        |
| 1Q19    | 32,000                            | 45%        |
| 3Q19    | 38,000                            | 65%        |
| 1Q20    | 45,000                            | 50%        |
| 3Q20    | 50,000                            | 25%        |
| 1Q21    | 55,000                            | 45%        |
| 3Q21    | 60,000                            | 30%        |
| 1Q22    | 65,000                            | 25%        |
| 3Q22    | 70,000                            | 20%        |
| 1Q23    | 75,000                            | 15%        |
| 3Q23    | 70,000                            | 10%        |
| 1Q24    | 65,000                            | -15%       |
| 3Q24    | 60,000                            | -10%       |
| 1Q25    | 65,000                            | 5%         |
| 3Q25    | 70,000                            | 15%        |
| 1Q26    | 75,000                            | 11.2%      |
</details>

## Solid Export Growth Aided by Tech and Industrial Upgrades

- Nominal GDP growth improved notably in 1Q26 to $4.9\%$ YoY, supported by strong export growth and PPI returning to positive levels.  
- Despite some volatility in March, YTD export growth remained strong at 14.5% YoY in April, which supported production recovery.

Nominal GDP growth improved notably in 1Q26  
![](images/743c477a5125d8a820437b5ce8c7e88d0de12c981e3d325be5b6c926c7d337ca.jpg)

<details>
<summary>line chart</summary>

| Month    | Nominal GDP YoY |
| -------- | --------------- |
| Mar-23   | 5.5             |
| Jun-23   | 5.8             |
| Sep-23   | 4.1             |
| Dec-23   | 4.4             |
| Mar-24   | 4.2             |
| Jun-24   | 3.9             |
| Sep-24   | 3.9             |
| Dec-24   | 4.6             |
| Mar-25   | 4.6             |
| Jun-25   | 3.9             |
| Sep-25   | 3.7             |
| Dec-25   | 3.9             |
| Mar-26   | 4.9             |
</details>

YTD export growth remained strong at 14.5% YoY in April  
![](images/55cf7298953889c62dfb0d7e9e4fb139edff321ef15becbaa1b7ab8f1888b323.jpg)

<details>
<summary>line chart</summary>

| Month    | YTD  |
| -------- | ---- |
| Mar-22   | 15.0 |
| Jun-22   | 14.0 |
| Sep-22   | 13.0 |
| Dec-22   | 7.0  |
| Mar-23   | 3.0  |
| Jun-23   | 5.0  |
| Sep-23   | 4.0  |
| Dec-23   | 8.0  |
| Mar-24   | 3.0  |
| Jun-24   | 5.0  |
| Sep-24   | 6.0  |
| Dec-24   | 5.0  |
| Mar-25   | 6.0  |
| Jun-25   | 6.0  |
| Sep-25   | 5.0  |
| Dec-25   | 10.0 |
| Mar-26   | 15.0 |
</details>

Source: NBS, CEIC, MS.

## Industrial: Still Healthy Profit Growth and Reduction of Overcapacity Risks Despite Slower Headline Macro Numbers

- April YTD manufacturing FAI growth dropped to 1.2% from 4.1% YoY in March from a high base last year.  
- YTD manufacturing profit growth accelerated further to 20.4% YoY in April 2026.  
- Overall gross margin improved 6bps YoY, helped by both PPI rebound and cost control.

Manufacturing FAI and IP gap declined to -7.6%, from -2.8% in April, with lower FAI growth  
![](images/b37056b558be448a2596e1f94202e7bd26af2ecf40d39674553b51fdf502ee55.jpg)

<details>
<summary>line chart</summary>

| Month    | FAI YTD yoy | Nominal - IP yoy |
| -------- | ----------- | ---------------- |
| Mar-26   | 1.2         | 8.8              |
</details>

Strong PPI growth at 1.7% MoM and 2.8% YoY  
![](images/7b91ef967c4597c86dc45cdedc5e51f0869c1716a16be68dedc125c55a921b2d.jpg)

<details>
<summary>line chart</summary>

| Date    | YoY  | MoM (RHS) |
|---------|------|-----------|
| Apr-26  | 2.8  | 1.7       |
</details>

Source: NBS, CEIC, MS.

## Industrial: By-sector Data Showed Better Trends in Apr-26 vs 1H24

\- 84.5% (in terms of liabilities) of sectors slowed capex in April 2026 vs. 1H24; 37.2% of sectors showed better profit trends in April.

![](images/23f1032ae430c5434e886b575e5fd5ecb76c0f99b0045a8e7ce80b98717e060d.jpg)

<details>
<summary>stacked bar chart</summary>

| Category | Investment slowing (%) | Investment accelerating (%) |
| --- | --- | --- |
| Slowing and improving | 37.2 | Stable and profit mixed (13%) Accelerating and profit mixed (1.8%) |
| Slowing and improving (General equipment) | 27.7 | Stable and profit mixed (13%) Accelerating and profit mixed (1.8%) |
| Slowing and improving (Specific equipment) | 27.7 | Stable and profit mixed (13%) Accelerating and profit mixed (1.8%) |
| Slowing and improving (Ferrous metal processing) | 27.7 | Stable and profit mixed (13%) Accelerating and profit mixed (1.8%) |
| Non ferrous metal processing | 27.7 | Stable and profit mixed (13%) Accelerating and profit mixed (1.8%) |
| Non metal mineral | 27.7 | Stable and profit mixed (13%) Accelerating and profit mixed (1.8%) |
| Non metal mineral (Printing) | 27.7 | Stable and profit mixed (13%) Accelerating and profit mixed (1.8%) |
| Non metal mineral (Pharma) | 27.7 | Stable and profit mixed (13%) Accelerating and profit mixed (1.8%) |
| Non metal mineral (Agricultural product processing) | 27.7 | Stable and profit mixed (13%) Accelerating and profit mixed (1.8%) |
| Slowing but still deteriorating | 19.7 | Stable and profit mixed (13%) Electricai equipment |
| Slowing but still deteriorating (Instrumentation) | 19.7 | Stable and profit mixed (13%) Electricai equipment |
| Slowing but still deteriorating (Furniture Entertainment) | 19.7 | Stable and profit mixed (13%) Electricai equipment |
| Slowing but still deteriorating (Wood Alcohol Metalware Rubber & Plastic Auto Leather Tobacco) | 19.7 | Stable and profit mixed (13%) Electricai equipment |
| Slowing but still deteriorating (Apparel) | 19.7 | Stable and profit mixed (13%) Electricai equipment |
| Investment accelerating | - | Stable and profit mixed (13%) Electricai equipment |
| Investment accelerating (Textile) | - | Stable and profit mixed (13%) Electricai equipment |
| Investment accelerating (Accelerating and deteriorating) | - | Stable and profit mixed (13%) Electricai equipment |
| Investment accelerating (Apparel) | - | Stable and profit mixed (13%) Electricai equipment |
| Investment accelerating (Accreating and deteriorating) | - | Stable and profit mixed (13%) Electricai equipment |
| Investment accelerating (Accreating and deteriorating) | - | Stable and profit mixed (13%) Electricai equipment |
| Investment accelerating (Accreating and deteriorating) | - | Stable and profit mixed (13%) Electricai equipment |
| Investment accelerating (Accreating and deteriorating) | - | Stable and profit mixed (13%) Electricai equipment |
| Investment accelerating (Accurately and deteriorating) | - | Stable and profit mixed (13%) Electricai equipment |
| Investment accelerating (Accurately and deteriorating) | - | Stable and profit mixed (13%) Electricai equipment |
| Investment accelerating (Accurately and deteriorating) | - | Stable and profit mixed (13%) Electricai equipment |
| Investment accelerating (Accurately and deteriorating) | - | Stable and profit mixed (13%) Electricai equipment |
| Investment acceleration (Accurately and deteriorating) | - | Stable and profit mixed (13%) Electricai equipment |
| Investment accelerating (Accurately and deteriorating) | - | Stable and profit mixed (13%) Electricai equipment |
| Investment accelerating (Accurately and deteriorating) | - | Stable and profit mixed (13%) Electricai equipment |
| Investment accelerating (Accurately and deteriorating) | - | Stable and profit mixed (13%) Electricai Equipment |
| Investment accelerating (Accurately and deteriorating) | - | Stable and profit mixed (13%) Electricai Equipment |
| Investment accelerating (Accurately and deteriorating) | - | Stable and profit mixed (13%) Electricai Equipment |
| Investment accelerating (Accurately and deteriorating) | - | Stable and profit mixed (13%) Electricai Equipment |
| Investment accelerating (Accurately and deteriorating) | - | Stable and profit mixed (10.6%) Apparel |
| Investment accelerating (Accurately and deteriorating) | - | Stable and profit mixed (10.6%) Apparel |
| Investment accelerating (Accurately and deteriorating) | - | Stable and profit mixed (10.6%) Apparel |
| Investment accelerating (Accurately and deteriorating) | - | Stable and profit mixed (10.6%) Apparel |
| Investment accelerating (Accurately and deteriorating) | - | Stable and profit mixed (14.8%) Textile<nl> |
</details>

Note: number in () represents their mix in total manufacturing liabilities  
Source: NBS, CEIC, MS.

## Moderating TSF, Enough to Support Business Activities Rebound

• TSF growth continued to moderate in April, to 7.8% YoY, of which Rmb loan growth further slowed to 5.6% YoY.  
• Government bonds were still the main support, up 15.6% YoY.  
- Rmb loans declined Rmb401bn in April 2026 (vs. an Rmb88bn increase last year), suggesting more rational loan growth besides seasonality after quarter-end.

Total TSF (ex government bonds) has slowed to below 6% in April 2026, vs >9% even in 2021  
![](images/b7a3b6bf2b301a621629330ad260794b2fdbc70ac68ef206ef26d50f8938cd19.jpg)

<details>
<summary>line chart</summary>

| Date   | yoy (%) |
|--------|---------|
| Oct-21 | 9.3     |
| Jan-22 | 9.4     |
| Apr-22 | 9.1     |
| Jul-22

[中间内容因长度限制已省略]

es relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products.

MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: China Financials

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/08/2026)</td></tr><tr><td colspan="3">Chiyao Huang</td></tr><tr><td>China International Capital Corp. Ltd. (3908.HK)</td><td>O (02/28/2025)</td><td>HK$18.63</td></tr><tr><td>CMS Co Ltd (600999.SS)</td><td>U (09/29/2022)</td><td>Rmb16.90</td></tr><tr><td>CMS Co Ltd (6099.HK)</td><td>U (10/29/2024)</td><td>HK$14.84</td></tr><tr><td>CITIC Co. (6030.HK)</td><td>E (10/29/2024)</td><td>HK$24.94</td></tr><tr><td>CITIC Co. (600030.SS)</td><td>O (08/07/2025)</td><td>Rmb25.43</td></tr><tr><td>East Money Information Co Ltd (300059.SZ)</td><td>E (09/19/2025)</td><td>Rmb17.72</td></tr><tr><td>Futu Holdings Ltd (FUTU.O)</td><td>O (11/18/2024)</td><td>US$91.08</td></tr><tr><td>Galaxy Securities (6881.HK)</td><td>E (02/27/2020)</td><td>HK$7.52</td></tr><tr><td>Galaxy Securities (601881.SS)</td><td>U (09/29/2022)</td><td>Rmb11.86</td></tr><tr><td>GF Securities (000776.SZ)</td><td>E (08/07/2025)</td><td>Rmb18.65</td></tr><tr><td>GF Securities (1776.HK)</td><td>E (01/06/2023)</td><td>HK$15.75</td></tr><tr><td>HTSC (601688.SS)</td><td>E (09/23/2024)</td><td>Rmb18.74</td></tr><tr><td>HTSC (6886.HK)</td><td>E (09/23/2024)</td><td>HK$16.30</td></tr><tr><td colspan="3">Richard Xu, CFA</td></tr><tr><td>Agricultural Bank of China Limited (601288.SS)</td><td>E (05/07/2019)</td><td>Rmb6.57</td></tr><tr><td>Agricultural Bank of China Limited (1288.HK)</td><td>O (10/19/2020)</td><td>HK$5.82</td></tr><tr><td>Bairong Inc. (6608.HK)</td><td>E (09/09/2025)</td><td>HK$5.45</td></tr><tr><td>Bank of Beijing Co Ltd (601169.SS)</td><td>E (08/17/2022)</td><td>Rmb5.12</td></tr><tr><td>Bank of Chengdu Co Ltd (601838.SS)</td><td>O (08/17/2022)</td><td>Rmb18.97</td></tr><tr><td>Bank of China Limited (601988.SS)</td><td>E (05/07/2019)</td><td>Rmb6.14</td></tr><tr><td>Bank of China Limited (3988.HK)</td><td>O (01/10/2020)</td><td>HK$5.36</td></tr><tr><td>Bank of Communications (3328.HK)</td><td>U (05/20/2022)</td><td>HK$7.43</td></tr><tr><td>Bank of Communications (601328.SS)</td><td>U (09/05/2014)</td><td>Rmb6.86</td></tr><tr><td>Bank of Hangzhou Co Ltd (600926.SS)</td><td>E (08/17/2022)</td><td>Rmb16.13</td></tr><tr><td>Bank of Ningbo Co. Ltd (002142.SZ)</td><td>O (08/17/2022)</td><td>Rmb31.01</td></tr><tr><td>China CITIC Bank Corporation Limited (601998.SS)</td><td>E (04/16/2025)</td><td>Rmb7.69</td></tr><tr><td>China CITIC Bank Corporation Limited (0998.HK)</td><td>O (04/16/2025)</td><td>HK$7.63</td></tr><tr><td>China Construction Bank Corp. (0939.HK)</td><td>O (10/11/2012)</td><td>HK$8.76</td></tr><tr><td>China Construction Bank Corp. (601939.SS)</td><td>E (05/07/2019)</td><td>Rmb10.33</td></tr><tr><td>China Everbright Bank Co Ltd (6818.HK)</td><td>U (05/12/2023)</td><td>HK$3.21</td></tr><tr><td>China Everbright Bank Co Ltd (601818.SS)</td><td>U (05/20/2022)</td><td>Rmb3.12</td></tr><tr><td>China Merchants Bank (600036.SS)</td><td>O (01/07/2019)</td><td>Rmb38.50</td></tr><tr><td>China Merchants Bank (3968.HK)</td><td>O (09/20/2018)</td><td>HK$48.16</td></tr><tr><td>China Minsheng Banking Corp. (600016.SS)</td><td>O (08/28/2025)</td><td>Rmb3.55</td></tr><tr><td>China Minsheng Banking Corp. (1988.HK)</td><td>O (05/12/2023)</td><td>HK$3.41</td></tr><tr><td>Chongqing Rural Commercial Bank (3618.HK)</td><td>U (05/12/2023)</td><td>HK$6.46</td></tr><tr><td>Hua Xia Bank (600015.SS)</td><td>U (06/30/2015)</td><td>Rmb6.79</td></tr><tr><td>Industrial and Commercial Bank of China (1398.HK)</td><td>O (08/09/2013)</td><td>HK$6.93</td></tr><tr><td>Industrial and Commercial Bank of China (601398.SS)</td><td>E (09/19/2022)</td><td>Rmb7.50</td></tr><tr><td>Industrial Bank Co. Ltd. (601166.SS)</td><td>O (02/25/2019)</td><td>Rmb18.54</td></tr><tr><td>Lufax (LU.N)</td><td></td><td>US$1.38</td></tr><tr><td>Ping An Bank (000001.SZ)</td><td>O (05/07/2019)</td><td>Rmb11.03</td></tr><tr><td>Postal Savings Bank of China Co Ltd (1658.HK)</td><td>O (11/01/2016)</td><td>HK$5.02</td></tr><tr><td>Qifu Technology Inc (QFIN.O)</td><td>O (08/25/2020)</td><td>US$14.27</td></tr><tr><td>Shanghai Pudong Development Bank (600000.SS)</td><td>E (08/05/2025)</td><td>Rmb9.37</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
