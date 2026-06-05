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

# China Banks

# SME policy pivot - near-term AQ pain, medium-term yield recovery. Implications for banks vary

China's financial regulator has pivoted from encouraging banks to grow inclusive loans to instead focusing on the quality and sustainability of the loans (Table 4). We view this shift as a response to rising SME credit risks (Table 2-Table 3) and relatively soft loan demand. Given the worsening debt-servicing ability of SMEs, the deceleration in inclusive loan growth could intensify near-term asset quality pressure. But in the medium term, it may ease pricing competition and support a modest recovery in inclusive loan yields. The implications for banks vary. We prefer CCB, SPDB and CRCB as these three banks reported declines in personal business loan (a sub-category of inclusive finance) NPL ratios in 2025, and look set to benefit from improvement in loan yield. By contrast, we remain cautious on PSBC and CSRCB on this topic, given their larger inclusive finance exposure (Figure 8) and continued asset quality pressure.

\- What's new? On May $19^{\text{th}}$ , the NFRA issued the Notice on MSE Financial Services for 2026 (link), with the most important change being the removal of explicit encouragement of MSE loan growth. Rather than focusing on volume growth, the 2026 Notice reorients the policy objective around credit structure optimization and asset quality improvement.

\- A refresher on the regulatory shift on SME lending - from volume race to quality competition (Table 4). The NAFR formally introduced the "two increases, two controls" (两增两控) framework in 2018, requiring banks to ensure inclusive SME loan growth was no lower than overall loan growth and that the number of SME borrowers was no lower than the prior year level, with a higher target set specifically for the Big 5 banks. Starting in 2023, the "two increases" hard requirement was dropped, but regulators continued to guide banks towards high SME lending growth directionally. The 2026 Notice marks a more decisive pivot from quantity to quality with no mention of the SME loans growth target, while there is an emphasis on asset quality improvement.

\- We see rising asset quality risks for SME loans: NBS PMI data shows that while large enterprises' PMI trended up m/m to 51.1 in May, small enterprises' PMI declined to 48.5 (Figure 1). Data also shows that since Covid, there has been significant divergence in interest coverage ratios and account-receivable turnover days between large and small enterprises. Small enterprises' interest coverage ratio is meaningfully lower (Figure 2) and accounts receivable cycle notably longer than large peers (Figure 3). The guidance change from PBOC may lead to further deceleration of inclusive loan growth (Figure 4, Figure 5); we think this would intensify the asset quality for SME loans in the near term.

\- The economics of SME loans meaningfully deteriorated in recent years: From 2022 to 2025, the lending rate of new inclusive finance loans contracted 1.2pcts to $3.31\%$ , while the NPL ratio of personal business loans, a sub-category of inclusive finance, rose by 70bps to $1.66\%$ . We have not seen an inflexion point for the worsening economics, with the exception of SPDB and CCB whose NPL as a $\%$ of personal business loans saw marginal improvement in 2025 on a y/y basis.

# Banks & Financial Services

# Katherine Lei AC

(852) 2800-8552

katherine.lei@JPM.com

JPM Securities (Asia Pacific) Limited/

JPM Broking (Hong Kong) Limited

# Haomin Chen AC

(86-21) 6106 6347

haomin.chen@JPM.com

SAC Registration Number: S1730524080002

JPM Securities (China) Company

Limited

# Peter Zhang

(852) 2800-8557

peter.zhang@JPM.com

JPM Securities (Asia Pacific) Limited/

JPM Broking (Hong Kong) Limited

# Lincoln Yu

(852) 2800 8523

lincoln.yu@JPM.com

JPM Securities (Asia Pacific) Limited/

JPM Broking (Hong Kong) Limited

- The silver lining is that the lending yield for inclusive finance loans may improve in the medium term: With the deceleration of loan growth, particularly from SOE banks, we may see moderate improvement in loan pricing. But the magnitude is likely to be small as banks' risk appetite remains low, and debt-servicing ability of small enterprises is yet to recover.   
- Implications for SOEs and JSBs – prefer CCB and SPDB and avoid PSBC. We see risk to Minsheng from this topic: On the positive side, CCB and SPDB reported NPL ratio contraction for personal business loans in 2025 (Table 2), thus if lending yield can improve following the ease in competition, economics for inclusive finance may improve. On the negative side, PSBC has the highest exposure to inclusive finance loans, and continued to see lending yield contraction and a rise in NPL ratios for this portfolio in 2025 (Table 1, Table 2). For Minsheng, although it has done a better job in managing assert quality for personal business loans in past three years, its share price performance may still lag due to its relatively sizable inclusive finance portfolio.   
- Implications for city and rural commercial banks: We see short-term pain but long-term gain for regional banks with genuine SME service capabilities. In the short term, the pressure is on AQ. We are yet to observe an inflection point in personal business loans NPL % across our covered banks (Table 3), and any large bank credit withdrawal from the SME segment could amplify repayment stress. In the long term, a reduction in irrational pricing pressure from large banks should create room for NIM recovery and gradual market share stabilization in their key operating regions. Among our covered banks, we think CSRCB is more exposed to near-term AQ downside, given its largest inclusive finance exposure (Figure 8) and continued deterioration in personal business AQ (Table 3). However, the longer-term read through is constructive. Since 2020, CSRCBs' SME growth had been meaningfully constrained by aggressive large bank competition (Figure 9). As competitive dynamics normalize, we believe CSRCB will be best placed to regain share with its deep local knowledge and effective “loan factory” credit model. We stay cautious on CSRCB until we observe positive signs from its AQ. We like CRCB as its NPL ratio on personal business loan contracted 49bps h/h in 2H25, likely supported by local macro recovery and better underwriting capacity (Table 3).

Figure 1: PMI for small and medium enterprises have been trending below that of the large enterprises   
![](images/4a9be38757b117eb14c41a7a13a76ee7b6dd9bf66bfbcccb9043ecca8a657a59.jpg)

<details>
<summary>line</summary>

| Month    | Manufacturing PMI - Large enterprises | Manufacturing PMI - Medium enterprises | Manufacturing PMI - Small enterprises |
|----------|----------------------------------------|-----------------------------------------|----------------------------------------|
| May-21   | 51.0                                   | 50.5                                    | 49.5                                   |
| Aug-21   | 50.5                                   | 50.0                                    | 48.5                                   |
| Nov-21   | 51.5                                   | 50.5                                    | 49.0                                   |
| Feb-22   | 50.0                                   | 49.5                                    | 47.0                                   |
| May-22   | 51.0                                   | 50.0                                    | 48.0                                   |
| Aug-22   | 50.5                                   | 49.5                                    | 47.5                                   |
| Nov-22   | 50.0                                   | 49.0                                    | 46.5                                   |
| Feb-23   | 53.0                                   | 48.0                                    | 45.0                                   |
| May-23   | 51.5                                   | 47.5                                    | 46.0                                   |
| Aug-23   | 50.0                                   | 47.0                                    | 46.5                                   |
| Nov-23   | 51.0                                   | 48.0                                    | 47.0                                   |
| Feb-24   | 50.5                                   | 47.5                                    | 46.5                                   |
| May-24   | 51.0                                   | 48.0                                    | 47.0                                   |
| Aug-24   | 50.5                                   | 47.5                                    | 46.5                                   |
| Nov-24   | 51.0                                   | 48.0                                    | 47.0                                   |
| Feb-25   | 52.0                                   | 49.0                                    | 48.0                                   |
| May-25   | 51.5                                   | 48.5                                    | 47.5                                   |
| Aug-25   | 50.0                                   | 47.0                                    | 46.0                                   |
| Nov-25   | 51.0                                   | 48.0                                    | 47.0                                   |
| Feb-26   | 50.5                                   | 47.5                                    | 46.5                                   |
| May-26   | 51.0                                   | 48.0                                    | 47.0                                   |
</details>

Source: NBS, CEIC. Data as of 1 June 2026.

Figure 2: EBIT/financial expenses for small industrial enterprises have been weaker than large and medium enterprises   
![](images/126f0e6fbbcaf54f50f9799e14b53e4fe7dc365e6720a2fd6e42b6d23b1bc00c.jpg)

<details>
<summary>line</summary>

| Date   | Small enterprises | Large and medium enterprises |
|--------|-------------------|-------------------------------|
| Apr-14 | 7.0x              | 6.5x                          |
| Apr-15 | 6.5x              | 6.0x                          |
| Apr-16 | 6.5x              | 6.0x                          |
| Apr-17 | 7.0x              | 7.0x                          |
| Apr-18 | 6.0x              | 7.0x                          |
| Apr-19 | 5.5x              | 7.5x                          |
| Apr-20 | 5.0x              | 7.0x                          |
| Apr-21 | 6.5x              | 9.0x                          |
| Apr-22 | 7.0x              | 11.0x                         |
| Apr-23 | 6.0x              | 11.5x                         |
| Apr-24 | 7.0x              | 13.0x                         |
| Apr-25 | 5.5x              | 12.5x                         |
| Apr-26 | 5.0x              | 9.5x                          |
</details>

Source: CEIC. Data as of 1 June 2026.

Figure 3: Account receivables for small industrial enterprises is picking up and is higher than for large and medium enterprises   
![](images/79907e0b2f3126b3738bb2d6a94571998851991775866b6cfad5c1cfc8b62bfd.jpg)

<details>
<summary>line</summary>

| Date   | Small industrial enterprises | large and medium industrial enterprises |
|--------|------------------------------|----------------------------------------|
| Apr-14 | 30                           | 35                                     |
| Apr-15 | 32                           | 38                                     |
| Apr-16 | 35                           | 40                                     |
| Apr-17 | 38                           | 42                                     |
| Apr-18 | 45                           | 48                                     |
| Apr-19 | 55                           | 52                                     |
| Apr-20 | 80                           | 65                                     |
| Apr-21 | 60                           | 50                                     |
| Apr-22 | 70                           | 55                                     |
| Apr-23 | 75                           | 60                                     |
| Apr-24 | 80                           | 65                                     |
| Apr-25 | 85                           | 70                                     |
| Apr-26 | 90                           | 75                                     |
</details>

Source: CEIC. Data as of 1 June 2026.

Figure 4: SOE banks have higher inclusive finance growth than the system level   
![](images/e2aa0f0062b77fe4078ede94e011d9965297c4494304b31019cb817d48402ff4.jpg)

<details>
<summary>line</summary>

| Quarter | SOE banks inclusive finance y/y growth (%) | System inclusive finance y/y growth (%) |
|---|---|---|
| 1Q20 | 45.5 | 23.5 |
| 2Q20 | 47.0 | 25.0 |
| 3Q20 | 49.5 | 28.0 |
| 4Q20 | 48.5 | 30.0 |
| 1Q21 | 49.5 | 33.5 |
| 2Q21 | 45.0 | 30.0 |
| 3Q21 | 33.5 | 27.0 |
| 4Q21 | 35.5 | 26.0 |
| 1Q22 | 32.0 | 24.5 |
| 2Q22 | 31.0 | 24.0 |
| 3Q22 | 33.5 | 24.5 |
| 4Q22 | 31.5 | 24.0 |
| 1Q23 | 34.0 | 25.5 |
| 2Q23 | 35.0 | 25.5 |
| 3Q23 | 34.5 | 24.5 |
| 4Q23 | 34.0 | 23.5 |
| 1Q24 | 31.5 | 21.0 |
| 2Q24 | 27.0 | 17.0 |
| 3Q24 | 21.5 | 14.0 |
| 4Q24 | 23.0 | 13.0 |
| 1Q25 | 19.5 | 11.5 |
| 2Q25 | 20.5 | 11.0 |
| 3Q25 | 19.5 | 10.5 |
| 4Q25 | 18.0 | 10.0 |
| 1Q26 | 16.5 | 9.5 |
</details>

Source: PBOC (as of 1 June 2026, NAFR (as of 1 June 2026), Wind (as of 1 June 2026).

Figure 5: Inclusive finance loans' contribution to total loans increased from $7\%$ in 1Q19 to $13.7\%$ in 1Q26, and contribution from SOE banks is becoming more significant   
![](images/76da423ac585c90141ec4f45ee2f65c633e553f912663acff52063f1e9913904.jpg)

<details>
<summary>bar_stacked</summary>

| Quarter | SOE banks' inclusive loans as % of total loans (%) | Non-SOE inclusive loans as % of total loans (%) |
|---|---|---|
| 1Q19 | 1.8 | 4.5 |
| 2Q19 | 2.0 | 4.7 |
| 3Q19 | 2.2 | 4.8 |
| 4Q19 | 2.3 | 4.9 |
| 1Q20 | 2.5 | 5.0 |
| 2Q20 | 2.7 | 5.2 |
| 3Q20 | 2.9 | 5.4 |
| 4Q20 | 3.0 | 5.5 |
| 1Q21 | 3.2 | 5.7 |
| 2Q21 | 3.4 | 5.9 |
| 3Q21 | 3.6 | 6.0 |
| 4Q21 | 3.7 | 6.1 |
| 1Q22 | 3.9 | 6.3 |
| 2Q22 | 4.0 | 6.4 |
| 3Q22 | 4.1 | 6.5 |
| 4Q22 | 4.2 | 6.6 |
| 1Q23 | 4.4 | 6.8 |
| 2Q23 | 4.6 | 7.0 |
| 3Q23 | 4.8 | 7.1 |
| 4Q23 | 4.9 | 7.2 |
| 1Q24 | 5.3 | 7.3 |
| 2Q24 | 5.5 | 7.4 |
| 3Q24 | 5.6 | 7.5 |
| 4Q24 | 5.7 | 7.6 |
| 1Q25 | 5.9 | 7.7 |
| 2Q25 | 6.0 | 7.8 |
| 3Q25 | 6.1 | 7.9 |
| 4Q25 | 6.2 | 8.0 |
| 1Q26 | 6.5 | 8.1 |
</details>

Source: PBOC (as of 1 June 2026, NAFR (as of 1 June 2026), Wind (as of 1 June 2026).

Figure 6: Weighted average new SME lending yield vs overall loan yield for banks with relevant disclosures   
![](images/6f2cd9d5352bf136d3262dd37c17c0707c5796cb2bcca0202f9731cb59e607a5.jpg)

<details>
<summary>line</summary>

| Period | Weighted average new SME lending yield (%) | Weighted average loan yield (%) |
|---|---|---|
| 2H20 | 4.45 | 4.38 |
| 1H21 | 4.38 | 4.36 |
| 2H21 | 4.39 | 4.35 |
| 1H22 | 4.32 | 4.31 |
| 2H22 | 4.18 | 4.17 |
| 1H23 | 3.90 | 4.05 |
| 2H23 | 3.78 | 3.95 |
| 1H24 | 3.60 | 3.75 |
| 2H24 | 3.45 | 3.55 |
| 1H25 | 3.15 | 3.10 |
| 2H25 | 3.08 | 2.90 |
</details>

Source: 2H20-2H25 company reports of ICBC, CCB, BOC, ABC, CMB, HXB, MSB, EB, and Industrial. Note: We include only these banks as they made consistent disclosure of new SME lending yields from 2H20-2H25.

Figure 7: Weighted average NPL ratio for personal business loans has trended up since 1H23, while that for overall loans decreased   
![](images/c9cd28ba91a71eab76824d650e695c9d3392a37ffe44915dccc8d29834b1122c.jpg)

<details>
<summary>line</summary>

| Period | Weighted average personal business loans NPL% | Weighted average overall NPL% |
|---|---|---|
| 1H20 | 1.25 | 1.45 |
| 2H20 | 1.50 | 1.48 |
| 1H21 | 1.25 | 1.43 |
| 2H21 | 1.20 | 1.39 |
| 1H22 | 1.15 | 1.36 |
| 2H22 | 1.10 | 1.34 |
| 1H23 | 0.95 | 1.32 |
| 2H23 | 1.05 | 1.30 |
| 1H24 | 1.20 | 1.28 |
| 2H24 | 1.45 | 1.27 |
| 1H25 | 1.60 | 1.26 |
| 2H25 | 1.80 | 1.25 |
</details>

Source: 1H20-2H25 company reports of ABC, CCB, ICBC, BoCom, PSBC, CMB, SPDB, MSB, and Industrial. Note: We include only these banks as they made consistent disclosure of new SME lending yields from 1H20-2H25

Figure 8: Inclusive finance as % of total loans in 2020 vs 2025, by bank   
![](images/1964ae22ca09bf3f40f5c0d5563a73e47390ba95a2c9d98ccf0d40b8d01af829.jpg)

<details>
<summary>bar</summary>

| Company | 2020 (%) | 2025 (%) |
| :--- | :--- | :--- |
| PSBC | 13.5 | 18.5 |
| ABC | 6.0 | 14.0 |
| CCB | 9.0 | 13.5 |
| BOC | 4.0 | 11.5 |
| ICBC | 3.5 | 11.5 |
| Bocomm | 4.0 | 10.0 |
| Minsheng | 11.5 | 15.5 |
| Pingan | 10.5 | 14.5 |
| CMB | 10.5 | 13.5 |
| Everbright | 6.5 | 11.5 |
| Citic Industrial | 7.0 | 11.0 |
| SPDB | 4.5 | 10.0 |
| Huaxia | 6.0 | 9.5 |
| CSRCB | 38.5 | 41.5 |
| CRCB | 14.5 | 18.5 |
| Hangzhou | 15.5 | 17.0 |
| Ningbo | 12.5 | 14.5 |
| Nanjing Shanghai | 7.5 | 11.0 |
| Beijing | 4.5 | 10.5 |
</details>

Source: 2020 and 2025 annual reports for the banks mentioned in the chart above. J.P Morgan estimate for CSRCB 2020 inclusive finance loan balance, as the bank did not disclose this data in 2020.

Figure 9: Inclusive finance CAGR in 2020-2025, by bank   
![](images/3f2e023df499b6754b1263c9d99c703ef30039aeeb2fe5119f8f71d7e02fbb1c.jpg)

<details>
<summary>bar</summary>

| Company | 5Y CAGR (%) |
|---|---|
| ICBC | 38 |
| BOC | 35 |
| ABC | 32 |
| Bocomm | 28 |
| CCB | 21 |
| PSBC | 17 |
| Industrial | 25 |
| Everbright | 18 |
| Citic | 16 |
| SPDB | 14 |
| CMB | 12 |
| Pingan | 11 |
| Huaxia | 9 |
| Minsheng | 8 |
| Beijing | 31 |
| Shanghai | 28 |
| Nanjing | 25 |
| Ningbo | 23 |
| Hangzhou | 19 |
| CSRCB | 16 |
| CRCB | 14 |
</details>

Source: 2020 and 2025 annual reports for the banks mentioned in the chart above. J.P Morgan estimate for CSRCB 2020 inclusive finance loan balance, as the bank did not disclose this data in 2020.

Table 1: New inclusive finance lending yield vs gross loan lending yield by bank in 2022-25 

<table><tr><td rowspan="2"></td><td colspan="6">New Inclusive finance lending yield</td><td colspan="6">Gross loans lending yield</td></tr><tr><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2025-

[中间内容因长度限制已省略]

hout notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own

independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Securities (China) Company Limited and JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
