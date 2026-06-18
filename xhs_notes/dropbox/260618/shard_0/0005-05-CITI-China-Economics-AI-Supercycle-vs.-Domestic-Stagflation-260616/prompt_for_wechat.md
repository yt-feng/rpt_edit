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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`Citi`。标题格式建议：`# Citi：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份Citi研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
16 Jun 2026 02:17:17 ET | 13 pages

# China Economics

AI Supercycle vs. Domestic Stagflation

## CITI'S TAKE

China's K-shaped economy appears to be playing out through the contrast between an AI supercycle and domestic stagflation. AI is driving industrial production and exports, with high-tech IP reaching a five-year high. But domestic demand is faltering, as retail sales contracted for the first time since Covid and FAI decline deepened. Steady CPI and broader PPI suggest stagflation risks are on the rise for the domestic economy. We maintain our headline GDP forecast at 4.5% YoY for 26Q2E and 4.7% YoY for 2026E. On policies, we see an acceleration of targeted support for domestic demand but not broad-based stimulus ahead. Investment-stabilization measures such as the “Six Networks” initiative are underway. Consumption and household income growth could be a key focus of July’s Politburo meeting. But an outright lift of budget deficit or government bond quota is not our base case, and monetary policy does not appear to be in the driver’s seat.

Xiangrong Yu AC

+852-2501-2754

xiangrong.yu@citi.com

Xinyu Ji AC

+852-2501-2792

xinyu.ji@citi.com

AI supercycle vs. domestic stagflation is now the dominant force in China's K-shaped economy, as mixed activities indicators for May revealed.

■ AI supercycle powers production and trade. Industrial production rebounded to 4.5% YoY in May, in line with our above-consensus expectations (Citi/Mkt: 4.5/4.4% YoY). >50% of the growth came from high-tech sectors per our estimate, whose IP expanded at 15.1% YoY, a five-year high. Output of ICs, industrial robots, and NEVs all rose further, echoing earlier exports data. The AI supercycle generated investment only in selected sectors, with capex in telecom manufacturing growing at double-digit and investment in intellectual property rising 9.3% YoY Ytd.

■ Stagflation risks on the domestic side rise further. Domestic demand indicators missed already subdued expectations. Retail sales contracted for the first time since Covid at -0.6%YoY (Citi/Mkt: 0.0/-0.2%YoY). Investment decline deepened to -4.1%YoY Ytd (Citi/Mkt: -2.5/-2.3%YoY Ytd), with the monthly rate estimated by us at -10.7%YoY, the lowest rate since 25Q4. Compounded with steady CPI and rising PPI, real growth of retail sales and FAI both turned negative and created new lows since Covid. The Middle East conflict may not be fully to blame: PPI reflation was more than energy prices in May, and the supply constraint from crude loosened with recovering petrochemical related outputs.

Headline growth could remain steady despite the bifurcated nature. With IP at 4.5%YoY and service output index up 4.4%YoY, monthly proxy for GDP could hover \~4.5%YoY, the lower end of this year's target. The sharpest slowdown is also likely behind us with a lower base starting to kick in from 26H2 and Middle East conflict resolution, although there is little visibility for a pickup ahead. We maintain our growth forecast unchanged at 4.5%YoY for 26Q2E and 4.7%YoY for 2026E as such.

We see an acceleration of targeted support for domestic demand but not broad-based stimulus ahead. Targeted measures such as the “Six Networks” initiative are underway, enabling AI transition and stabilizing investment. Consumption and household income growth could be a key focus of the July Politburo meeting (held on the 30 $^{th}$ in 2025). We still think job market stress over the summer could prompt more targeted efforts. Having said that, steady headline GDP raises the bar for more significant policy adjustments. An outright lift of the budget deficit or government bond quota is not our base case. Although monetary policy is not in the driver’s seat, we still keep our call for a symbolic 10bps cut in 26H2E, with risks skewed to earlier.

Figure 1. China's K-shaped economy now showing through an AI supercycle vs. domestic stagflation  
![](images/008b57bb2241b8edcac1de0857933d6a5c29b73b800a6ba0e31c01223530a1ca.jpg)

<details>
<summary>line chart</summary>

| Month   | Industrial production | Retail sales | FAI  | Exports |
|---------|------------------------|--------------|------|---------|
| Jan-20  | -20                    | -20          | -20  | -20     |
| Jan-21  | 35                     | 10           | 35   | 40      |
| Jan-22  | 5                      | 5            | 10   | 15      |
| Jan-23  | 5                      | 15           | 5    | 10      |
| Jan-24  | 5                      | 5            | 5    | 5       |
| Jan-25  | 5                      | 5            | 5    | 10      |
| Jan-26  | 5                      | 0            | -15  | 20      |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: China Customs, NBS, Wind, Citi

Figure 2. Stagflation risks on the domestic side rise with contractionary retail sales and investment in May  
![](images/8a3735fee82640ae1af69f2ed30dcd04eebf5bdcf4a897dea94074f2e7db2b42.jpg)

<details>
<summary>line chart</summary>

| Date   | Retail Sales | CPI  | FAI, monthly est | PPI  |
|--------|--------------|------|------------------|------|
| Jan-24 | 6            | 0    | 4                | -3   |
| Jul-24 | 3            | 0    | 3                | -2   |
| Jan-25 | 5            | 0    | 4                | -3   |
| Jul-25 | 6            | 0    | -5               | -4   |
| Jan-26 | 3            | 0    | -15              | -1   |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: NBS, Wind, Citi

## Readthrough Monthly Indicators

Monthly indicators came in mixed for May. The supply side continued to outpace the demand side, with AI supercycle and domestic stagflation now two dominant forces in the K-shaped economy.

Industrial production rebounded to 4.5%YoY, in line with our above-consensus forecast (Citi/Mkt: 4.5/4.4%YoY). The AI supercycle appears to have helped.

■ AI supercycle powers ahead. High-tech IP rose 15.1%YoY, up from previously 12.8%YoY and hitting a five-year high. With its share at \~17% in IP (NBS, Oct 20 $^{th}$ , 2025), it could have contributed >50% of IP. Output of high-tech products rose further, with ICs at 22.9%YoY (vs. 22.1%YoY in April), industrial robots at 27.9%YoY (vs. 15.1%YoY), and NEVs at 17.8%YoY (vs. 3.8%YoY). Exports delivery remained steady at 10.1%YoY.  
■ Impact from Middle East conflict faded. Output of ethylene recovered to 2.1%YoY (vs. -4.1%YoY) and contraction narrowed for sulfuric acid to -1.6%YoY (-2.2%YoY). The resolution to the Middle East conflict could help further.  
■ Old economy showed no sign of stabilization. Crude steel output continued to contract -2.7%YoY (vs. -2.8%YoY), while cement output dropped -8.1%YoY (-10.8%YoY). The Six Networks investment could have just started and may take longer to shore up actual investment and production.

Retail sales recorded the first negative reading since Covid. The May reading came in at -0.6%YoY, below already subdued expectations (Citi/Mkt: 0.0/-0.2%YoY, Prior: 0.2%YoY). Steady CPI at 1.2%YoY in May could have sent real growth to \~1.8%YoY.

Trade-in subsidies remained a drag. We estimate the drag at -2.2ppts in May vs. -2.0ppts in April, a marginal deterioration insufficient to address the further decline, in our view. Auto sales stayed soft at -16.1%YoY (vs. -15.3%YoY), while home appliances remained sluggish at -15.6%YoY (vs. -15.1%YoY). Telecom equipment sales slowed further to 0.7%YoY (vs. 6.2%YoY), which could be under a “double whammy” from reduced subsidies and price increases. The high-base from last year's trade-in subsidies could further kick in, and some easing in contraction could follow in 26H2.

■ Demand shock from Mideast conflict faded. Energy & fuel sales dropped -3.2%YoY (vs. -6.5%YoY) and jewelry sales contracted -8.9%YoY (vs. -21.3%YoY), both narrowing from previous readings through remaining negative. Struggle of big retailers (annual sales >RMB5mn) continued, with their monthly sales at -5.2%YoY (vs. -4.9%YoY).  
■ Services economy softened. Cumulative retail services growth edged down to 5.4%YoY Ytd from previously 5.6%YoY for the first four months. Holiday economy related items were sluggish: restaurant revenue grew merely 0.6%YoY in May; beverage sales increased 6.1%YoY, and tobacco & liquor sales grew 4.8%YoY. The NBS attributed part the fluctuations to weather (SCIO, Jun 16 $^{th}$ ). Food deflation despite overall steady CPI could drive the nominal readings lower.

Investment contraction deepened further. Cumulative FAI growth dropped -4.1%YoY (Citi/Mkt: -2.5/-2.3%YoY Ytd), after turning negative at -1.6%YoY Ytd in April. The monthly reading could have deteriorated to -10.7%YoY per our estimate, the lowest reading since 25Q4.

■ Manufacturing investment showed tentative signs of stabilization amid an overall worsening picture. Cumulative capex growth dropped to -0.4%YoY Ytd from previously +1.2%YoY, yet its monthly rate could have stabilized at -4.2%YoY (vs. -4.3%YoY) based on our estimate.

- New economy led the stabilization. Investment in telecom mfg strengthened to 6.7%YoY Ytd from 5.4%YoY Ytd in April, and we estimate its monthly rate to pick up to 10.4%YoY. Investment in rail, ship and other transportation equipment stayed buoyant at 23.6%YoY Ytd. The new economy investment could also span more in intellectual property – its growth was solid at 9.3%YoY for Jan-May (NBS, Jun 16 $^{th}$ ).  
- PPI reflation beneficiaries showed little signs of capex, unsurprising amid anti-involution actions and Mideast conflict impact. Capex of chemicals dropped $-12.2\%$ YoY in the month, with its cumulative reading at $-5.9\%$ YoY.

Infrastructure investment dropped further to 0.6% YoY Ytd from previously 4.3% YoY Ytd. We estimate monthly contraction to have expanded to -9.1% YoY from -4.9% YoY, inching close to lowest readings excluding Covid disruptions. The Six Networks investment could have started but it may take longer to shore up FAI data. Weather disruptions into the summer could create more volatility.

■ Green shoots in the property sector sustained, but not spreading. This is particularly the case for prices and second-hand sales in top-tier cities.

- Second-hand prices rose another $0.4\%$ MoM in Tier-1 cities, with its 3M/3M annualized rate now at $4.9\%$ , the highest since mid-2023. Second-hand sales in cities such as Shanghai continued to trend above last year's level. The price momentum didn't spread: 10 cities out of the 70 cities surveyed by the NBS reported a sequential increase in second-hand prices, further down from 12 in April, and the contraction deepened in Tier-3 cities. National sales dropped $-13.1\%$ YoY in terms of floor space and $-9.5\%$ YoY in value terms.  
- Property investment contracted further. The cumulative reading dropped -16.2%YoY Ytd, with the monthly rate estimated at -24.3%YoY, and housing new starts remained in deep contraction of -24.6%YoY.

Figure 3. Industrial production growth and major sectors  
![](images/6d70e19c06162f8fa81a89857edebe42373c8c4f12bde5f97cda493cb68dcaea.jpg)

<details>
<summary>line chart</summary>

| Date   | Industrial Production | Manufacturing | High-Tech IP |
|--------|------------------------|---------------|--------------|
| Jan-22 | 7.0                    | 7.0           | 14.0         |
| Jul-22 | -3.0                   | -4.0          | 4.0          |
| Jan-23 | 2.0                    | 6.0           | 1.0          |
| Jul-23 | 4.0                    | 5.0           | 3.0          |
| Jan-24 | 6.0                    | 7.0           | 8.0          |
| Jul-24 | 5.0                    | 6.0           | 11.0         |
| Jan-25 | 6.0                    | 7.0           | 9.0          |
| Jul-25 | 5.0                    | 6.0           | 10.0         |
| Jan-26 | 4.0                    | 5.0           | 13.0         |
| May-26 | 3.0                    | 4.0           | 15.0         |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: NBS, Wind, Citi

Figure 5. Output growth of new-economy items  
![](images/4cbfca85dcbb62d8eb49deaf24ec37258d6ea04c9897a3f7aa387a817f310fef.jpg)

<details>
<summary>bar chart</summary>

Output Growth, New Economy
| Category | 2025 (%)YoY | Apr-26 (%)YoY | May-26 (%)YoY |
|---|---|---|---|
| ICs | 11 | 22 | 23 |
| Industrial Robots | 28 | 15 | 28 |
| Auto | 10 | -2 | -3 |
| NEVs | 25 | 4 | 18 |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: NBS, Wind, Citi

Figure 7. Exports growth and exports delivery growth  
![](images/4db28394af57a092ee141fbdd398beead2ebeef69df075eab4b3dfaee54a8999.jpg)

<details>
<summary>line chart</summary>

| Date   | Exports Growth (RMB) | Exports Delivery |
|--------|----------------------|------------------|
| Jan-22 | 15                   | 17               |
| Jul-22 | 22                   | 15               |
| Jan-23 | -5                   | -8               |
| Jul-23 | -10                  | -10              |
| Jan-24 | 10                   | 5                |
| Jul-24 | 10                   | 7                |
| Jan-25 | 10                   | 5                |
| Jul-25 | 10                   | 0                |
| Jan-26 | 19                   | 7                |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: NBS, Wind, Citi

Figure 4. Sales-to-production ratio by month  
![](images/a24ca5542d830fa1a00db8a126d07b3b0b2b460f58bf1123ffbcc35f3b4af140.jpg)

<details>
<summary>line chart</summary>

Sales-to-Production Ratio
| Month | 2026 (%) | 2025 (%) | 2024 (%) | 2023 (%) |
|---|---|---|---|---|
| Jan | 95.4 | 95.4 | 96.0 | 95.8 |
| Feb | 95.4 | 95.4 | 96.0 | 95.8 |
| Mar | 93.8 | 93.1 | 93.1 | 94.1 |
| Apr | 97.1 | 97.3 | 97.3 | 97.4 |
| May | 96.1 | 96.0 | 96.5 | 96.6 |
| Jun | 94.4 | 94.4 | 94.5 | 95.7 |
| Jul | 97.1 | 97.1 | 97.1 | 97.8 |
| Aug | 96.6 | 96.7 | 96.5 | 97.4 |
| Sep | 96.7 | 96.7 | 96.0 | 97.4 |
| Oct | 96.4 | 96.5 | 97.3 | 97.4 |
| Nov | 96.5 | 96.5 | 97.1 | 97.4 |
| Dec | 98.2 | 98.3 | 98.8 | 98.3 |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: NBS, Wind, Citi

Figure 6. Output growth petrochemical related products  
![](images/ebd87bef836c5a048ebaa7d7c19a84c72dbf13c93e8ae7f23a0114b50785f684.jpg)

<details>
<summary>bar chart</summary>

Output Change, Petrochemical Related
| Category | 2023 (%) | 2024 (%) | 2025 (%) | Apr-26 (%) | May-26 (%) |
|---|---|---|---|---|---|
| Raw Coal | 2.8 | 1.3 | 1.1 | -1.0 | -1.8 |
| Coke | 3.6 | -0.8 | 2.9 | -1.0 | 1.1 |
| Ethylene | 6.0 | 0.6 | 6.4 | -4.4 | 2.0 |
| Sulfuric Acid | 3.3 | 7.0 | 4.5 | -2.3 | -1.3 |
| Crude Oil | 2.0 | 1.8 | 1.6 | 1.1 | 0.4 |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: NBS, Wind, Citi

Figure 8. Cargo throughput at ports  
![](images/2611a685da22387d954867b1dae192a6211ae148d6997e41ca0e43e80a4e623f.jpg)

<details>
<summary>line chart</summary>

Cargo Throughput at Ports
| Month | 2023 (tons) | 2024 (tons) | 2025 (tons) | 2026 (tons) |
|---|---|---|---|---|
| Jan | 255 | 258 | 257 | 260 |
| Feb | 185 | 188 | 187 | 280 |
| Mar | 235 | 238 | 245 | 190 |
| Apr | 250 | 255 | 270 | 260 |
| May | 230 | 245 | 285 | 265 |
| Jun | 245 | 250 | 260 | 275 |
| Jul | 240 | 245 | 270 | 260 |
| Aug | 230 | 235 | 265 | 255 |
| Sep | 245 | 250 | 270 | 260 |
| Oct | 230 | 235 | 265 | 255 |
| Nov | 240 | 245 | 275 | 260 |
| Dec | 215 | 230 | 260 | 250 |
Weekly, mn tons
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: MoT, Wind, Citi

Figure 9. Retail sales growth by major categories

<table><tr><td colspan="2">(%YoY)</td><td>2024</td><td>2025</td><td>25Q4</td><td>26Q1</td><td>Apr 2026</td><td>May 2026</td></tr><tr><td colspan="2">Retail Sales</td><td>3.5</td><td>3.7</td><td>1.7</td><td>2.4</td><td>0.2</td><td>-0.6</td></tr><tr><td rowspan="5">Trade-in Subsidies</td><td>Auto</td><td>-0.5</td><td>-1.5</td><td>-6.5</td><td>-9.0</td><td>-15.3</td><td>-16.1</td></tr><tr><td>Home Appliances</td><td>12.3</td><td>11.0</td><td>-17.7</td><td>0.0</td><td>-15.1</td><td>-15.6</td></tr><tr><td>Telecom Equipment</td><td>9.9</td><td>20.9</td><td>21.6</td><td>20.8</td><td>6.2</td><td>0.7</td></tr><tr><td>Furniture</td><td>3.6</td><td>14.6</td><td>0.6</td><td>-5.2</td><td>-10.4</td><td>-8.7</td></tr><tr><td>Cultural &amp; Office</td><td>-0.3</td><td>17.3</td><td>11.5</td><td>9.3</td><td>-6.9</td><td>-1.5</td></tr><tr><td rowspan="3">Holiday Economy</td><td>Beverage</td><td>2.1</td><td>1.0</td><td>3.9</td><td>6.7</td><td>3.6</td><td>6.1</td></tr><tr><td>Tobacco &amp; Liquor</td><td>5.7</td><td>2.7</td><td>-1.0</td><td>16.0</td><td>11.7</td><td>4.8</td></tr><tr><td>Restaurants&#x27; Revenue</td><td>5.3</td><td>3.2</td><td>3.0</td><td>4.2</td><td>2.2</td><td>0.6</td></tr><tr><td rowspan="2">Global Prices</td><td>Energy &amp; Fuel</td><td>0.3</td><td>-5.7</td><td>-8.3</td><td>-6.4</td><td>-6.5</td><td>-3.2</td></tr><tr><td>Jewelry</td><td>-3.1</td><td>12.8</td><td>16.7</td><td>12.6</td><td>-21.3</td><td>-8.9</td></tr><tr><td rowspan="2">Staples</td><td>Grains &amp; Food</td><td>9.9</td><td>9.3</td><td>6.2</td><td>10.0</td><td>4.1</td><td>1.9</td></tr><tr><td>Daily Necessities</td><td>3.0</td><td>6.3</td><td>3.3</td><td>5.9</td><td>3.5</td><td>1.6</td></tr><tr><td rowspan="4">Other Discretionary</td><td>Apparel &amp; Footwear</td><td>0.3</td><td>3.2</td><td>3.3</td><td>9.3</td><td>3.6</td><td>3.8</td></tr><tr><td>Sport &amp; Recreation</td><td>11.1</td><td>15.7</td><td>6.3</td><td>1.9</td><td>-8.0</td><td>-8.0</td></tr><tr><td>Cosmetics</td><td>-1.1</td><td>5.1</td><td>8.2</td><td>5.9</td><td>4.7</td><td>2.5</td></tr><tr><td>Home Decoration</td><td>-2.0</td><td>-2.7</td><td>-12.5</td><td>-4.7</td><td>-13.8</td><td>-13.6</td></tr><tr><td colspan="2">Retail Services Sales</td><td>6.2</td><td>5.5</td><td colspan="2"></td><td>5.6</td><td>5.4</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: NBS, Wind, Citi

Figure 10. Retail sales, goods and restaurants' revenue  
![](images/470d363ce4222ff3c886a84b1bfaa62bc9301c1a2f0738af9fe9d46693bd2805.jpg)

<details>
<summary>line chart</summary>

| Month   | Retail Sales | Goods | Restaurants' Revenue |
|---------|--------------|-------|----------------------|
| Jan-24  | 6.0          | 5.0   | 20.0                 |
| Jul-24  | 3.0          | 2.0   | 5.0                  |
| Jan-25  | 4.0          | 3.0   | 4.0           

[中间内容因长度限制已省略]

lar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
