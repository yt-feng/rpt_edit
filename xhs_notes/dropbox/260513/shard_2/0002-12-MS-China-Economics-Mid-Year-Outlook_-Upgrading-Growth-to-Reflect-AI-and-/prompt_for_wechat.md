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
# China Economics Mid-Year Outlook

# Upgrading Growth to Reflect AI and Energy Capex Super-cycle

Strong exports plus AI and green capex lift our 2026e real GDP growth 0.1ppt, to 4.8%; our GDP deflator rises 0.3ppt, to 0.5%. But reflation is narrow: domestic consumption lags amid a soft labor market and ongoing property adjustments. Policy is on cruise control – additional easing is unlikely.

Exports driving growth amid AI and energy capex super-cycle: We lift our 2026 and 2027 real GDP growth forecasts 0.1ppt each, to 4.8% and 4.7%. Exports lead – China's supply chain resilience enables incremental export market share gains. The economy is also relatively insulated from the oil shock, supported by a more balanced energy mix and strategic reserves. The Middle East conflict is accelerating green transition demand that plays to China's renewable supply chain. Domestic demand still lags: consumption is constrained by a soft labor market and ongoing property adjustment, though investment is accelerating modestly. Infrastructure is supported by quasi-fiscal tools, manufacturing capex is underpinned by AI and exports, and housing is becoming marginally less of a drag.

Inflation is rising but reflation is narrow: We see higher energy costs and demand tied to AI and the green transition lifting PPI to 1.5% in 2026, but pass-through to core consumer prices remains limited – weak domestic demand and a soft labor market constrain pricing power. Headline CPI should average 0.8%Y, with core CPI at 1.1%Y on a shallow moderating path. We raise our GDP deflator forecast 0.3ppt, to 0.5%. Strong export volumes provide support, though terms of trade losses from higher commodity import prices keep it below headline inflation. As energy effects fade, headline inflation should soften into 2027.

Policy on cruise control: Strong exports reduce the urgency for stimulus. We remove our calls for 2H fiscal top-ups and additional monetary easing. Instead, we see a flat augmented deficit; the PBoC will rely on liquidity operations and targeted credit tools, not rate cuts. The Middle East conflict may reinforce supply-side priorities on energy security and tech self-sufficiency, with rebalancing of consumption proceeding gradually. On RMB, we revise year-end USDCNY to 6.75 (from 7.00), and see a near-term shift toward 6.70 as possible, given growth outperformance and a softer USD as risk aversion fades. But we think the PBoC remains mindful of soft domestic prices. It is unlikely to use currency strength to address growth imbalances.

Risks hinge on external demand and domestic policy direction: Stronger global growth would further boost exports, giving room for economic rebalancing policies. Conversely, a demand-destructive oil shock would hit mainly via weaker exports, compressing margins, lowering capacity utilization, and renewing deflationary pressures. Cyclical easing may step up, but policy mix would remain supply-centric. MS ASIA LIMITED

# Robin Xing

Chief China Economist

Robin.Xing@morganstanley.com +852 2848-6511

# Jenny Zheng, CFA

Economist

Jenny.L.Zheng@morganstanley.com +852 3963-4015

# Zhipeng Cai

Economist

Zhipeng.Cai@morganstanley.com +852 2239-7820

# Harry Zhao

Economist

Harry.Zhao@morganstanley.com +852 2239-7229

Exhibit 1 : Forecast summary table 

<table><tr><td></td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td></tr><tr><td>GDP Nominal %, YoY</td><td>4.2</td><td>4.0</td><td>5.4</td><td>5.1</td></tr><tr><td>GDP Real %, YoY</td><td>5.0</td><td>5.0</td><td>4.8</td><td>4.7</td></tr><tr><td>Household Consumption</td><td>5.3</td><td>4.5</td><td>3.7</td><td>4.0</td></tr><tr><td>Government Consumption</td><td>1.4</td><td>4.9</td><td>4.5</td><td>4.0</td></tr><tr><td>Gross Capital Formation</td><td>2.9</td><td>2.0</td><td>3.5</td><td>2.8</td></tr><tr><td>Goods and Service Exports</td><td>15.9</td><td>10.8</td><td>6.6</td><td>8.9</td></tr><tr><td>Goods and Service Imports</td><td>10.3</td><td>2.4</td><td>3.5</td><td>3.9</td></tr><tr><td colspan="5">Contribution to GDP, ppts</td></tr><tr><td>Household Consumption</td><td>2.1</td><td>1.8</td><td>1.5</td><td>1.6</td></tr><tr><td>Government Consumption</td><td>0.2</td><td>0.8</td><td>0.7</td><td>0.7</td></tr><tr><td>Gross Capital Formation</td><td>1.1</td><td>0.8</td><td>1.3</td><td>1.0</td></tr><tr><td>Net Exports</td><td>1.5</td><td>1.6</td><td>1.3</td><td>1.5</td></tr><tr><td colspan="5">Inflation, YoY%</td></tr><tr><td>GDP Deflator</td><td>-0.8</td><td>-0.9</td><td>0.5</td><td>0.3</td></tr><tr><td>CPI</td><td>0.2</td><td>0.1</td><td>0.8</td><td>0.6</td></tr><tr><td>Core CPI</td><td>0.5</td><td>0.8</td><td>1.1</td><td>0.8</td></tr><tr><td>PPI</td><td>-2.2</td><td>-2.6</td><td>1.5</td><td>-0.4</td></tr><tr><td colspan="5">Policy</td></tr><tr><td>7-day Reverse Repo Rate^</td><td>1.50</td><td>1.40</td><td>1.40</td><td>1.40</td></tr><tr><td>Augmented Fiscal Deficit#, % of GDP</td><td>-11.1</td><td>-11.7</td><td>-11.7</td><td>-11.7</td></tr><tr><td>USD/CNY^</td><td>7.30</td><td>6.99</td><td>6.75</td><td>6.75</td></tr></table>

Source: CEIC, MS Estimates (E) # General fiscal balance + off-budget quasi fiscal balance (including LGFV debt, net land sales revenue, and policy bank supports). ^End of Period.

# A Two-Speed Economy, Stable in Aggregate

China's economy is running on its exports engine. We lift our 2026 real GDP growth forecast 0.1ppt, to 4.8%, with the GDP deflator raised 0.3ppt, to 0.5%. Structural tailwinds from AI and energy transition, along with supply chain resilience culminate in strong exports, largely offsetting the drag from higher oil prices.

But the economy remains distinctly two-speed: private consumption growth is slowing, while investment is policy-driven and mixed. Infrastructure is accelerating with quasi-fiscal support, manufacturing capex is diverging sharply across sectors, and property remains in contraction, though the drag is incrementally milder.

Exhibit 2: GDP expenditure breakdown   
![](images/05739f534b009b07892cee19182fd1986e30bb3e5e192ab5481d89ffb1fa87b7.jpg)

<details>
<summary>bar_line</summary>

China Real GDP Growth by Expenditure, %
| Year | Net Exports (%) | GFCF (%) | Government Consumption (%) | Household Consumption (%) | Changes in Inventories (%) | Real GDP (in %) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2019 | 0.6 | 2.3 | 1.4 | 1.8 | -0.5 | 6.1 |
| 2020 | 0.7 | 1.4 | 0.5 | -0.8 | 0.2 | 2.4 |
| 2021 | 1.7 | 1.1 | 0.6 | 4.5 | 0.0 | 8.0 |
| 2022 | 0.3 | 1.4 | 0.9 | 0.0 | -0.2 | 3.1 |
| 2023 | -0.5 | 1.8 | 1.3 | 2.5 | -0.7 | 5.4 |
| 2024 | 1.5 | 1.0 | 0.2 | 2.1 | 0.1 | 5.0 |
| 2025E | 1.6 | 0.8 | 0.8 | 1.8 | 0.0 | 5.0 |
| 2026E | 1.3 | 1.3 | 0.7 | 1.5 | 0.0 | 4.8 |
| 2027E | 1.5 | 1.0 | 0.7 | 1.6 | 0.0 | 4.7 |
</details>

Source: NBS, MS (E) estimates

# Exports anchor cyclical growth momentum

We forecast China's goods export growth at 10%Y in nominal terms and 9%Y in real terms in 2026. Net exports should contribute \~1.3ppt to real GDP growth in 2026 – down slightly from 1.6ppt in 2025 owing to a terms of trade shock, but remaining the key growth driver.

\- Near term – market share gain largely offsets oil shock: On an annualized basis, we think China's global export market share gains could approach the upper end of our previously estimated 0.3-0.9ppt range, concentrated in the "new three" (solar, batteries, EVs), electrical capital goods (including power equipment), electronics and AI-related categories, and select basic materials. Even if global GDP growth may slow 0.5ppt in 2Q26 in response to the energy shock – implying roughly a 1ppt slowdown in global trade growth – share gains alone could bring an additional 4-5ppt of export growth. The April PMI new export orders index rebounded to 50.3, the highest in recent years, reflecting strong sUBStitution demand from overseas buyers as supply elsewhere is less insulated from the oil shock.

- Structural driver #1 – the global AI super-cycle: With the semiconductor market projected to surpass US\$1trn in 2026 and broadening deployment of agentic AI, China's deep electronics supply chain is a direct beneficiary. AI chip localization is accelerating, and Chinese capital goods companies are gaining share in global AI infrastructure.   
- Structural driver #2 – energy transition: The Middle East conflict has likely accelerated global demand for renewables and power equipment, and China controls over 80% of key solar manufacturing stages. Combined exports of solar, batteries, and EVs surged 70% YoY in March, to a record US\$21.9bn.

# Why export strength may translate into narrower improvement in job market than in previous cycles

The demand arithmetic is demanding: Housing and related sectors are still a drag on nominal GDP of roughly 2ppt this year. With exports at \~15% of GDP on a value-added basis, fully offsetting this drag alone would require sustained nominal export growth of 14-15% – a bar China has rarely cleared in recent years. Exports are clearly doing the heavy lifting, but the math shows that the hole they need to fill is exceptionally large.

The employment content of today's export dollar is lower than in previous cycles: China's export mix has shifted decisively up the value chain - toward EVs, ships, semiconductors, and power equipment – sectors that are more capital-intensive and automated. This means that each incremental dollar of export growth generates fewer jobs than it used to.

Overcapacity in the broader manufacturing sector means firms will raise utilization before headcount: Years of rapid investment in 2022–24 have left significant excess capacity across much of the manufacturing base. As export orders pick up, the natural corporate response is to run existing lines harder—not to expand capex, particularly under the anti-involution policy guidance. Job gains at the extensive margin only materialize once capacity utilization tightens meaningfully, which requires a strong and sustained export cycle beyond a few quarters.

That said, wage growth in select sectors could accelerate, supporting aggregate income: Export strength and profitability improvement are concentrated in a handful of high-value sectors populated by skilled labor. Wage growth in these pockets may accelerate even as the broader labor market remains soft, supporting aggregate wage growth. But this is a narrow, segmented improvement, not the broad-based income recovery that would move the needle on aggregate consumption.

Bottom line: Exports are helping, but the labor market arithmetic has structurally changed. The bar for a full offset via exports is high, and overcapacity means that transmission works with a longer lag. This is why the improvement in the job market is likely to remain narrower and slower than in previous export-driven cycles.

Exhibit 3: The spillover from profits to employment growth is also weakening as the industrial sector becomes more capital intensive and automated   
![](images/a7e17e7f252cfc63c4400650d3d127619f4b6076d145cad9b1a3964fa227c0ce.jpg)  
Source: NBS, Economic Census, MS

Exhibit 4: Reduced transmission effect of export strength to capex given pervasive excess capacity problems   
![](images/d963dae903a8c32e6799f48190948424aa3a60cfc6be98561575c9c7380a9a52.jpg)  
Source: NBS, MS. \*3-year rolling correlation

# Domestic demand is still lagging

Consumption remains a laggard in China's growth mix, constrained by a soft labor market: We forecast private consumption growth of 3.7% in 2026, down from 4.5% in 2025 – below headline GDP growth – implying that consumption's share of growth continues to underwhelm relative to exports.

- Labor market slack is the key binding constraint: The urban surveyed unemployment rate rose to a 13-month high of 5.4% in March, with YoY change in youth unemployment remaining positive (barring LNY distortions) since the definition change. Critically, the weakness is structural:   
- Export strength is concentrated in capital-intensive, higher-value-added sectors with limited job spillover.   
- Most labor-intensive domestic sectors – led by construction and derivative services – remain in a prolonged adjustment.

\- AI diffusion adds a medium-term headwind: As a form of skill-biased technical change, AI displaces entry-level or even medium-level cognitive work. Labor market for fresh/recent graduates will likely remain loose, particularly given 12-13mn new entrants each year.

\- Social welfare reform is advancing only incrementally: Beijing will likely maintain a supply-centric policy framework – as evidenced in the Five-Year Plan – which limits fiscal space for demand-side support/transfers. Without a meaningful pivot toward strengthening social protection, precautionary savings will stay elevated and private spending will remain in a slow lane.

Investment presents a mixed picture: We forecast real growth of gross fixed asset formation to rebound to 3.5% in 2026 from 2% in 2025. The key drivers would be booming AI capex, policy support for infrastructure, and export-driven capex in select manufacturing sectors. Manufacturing investment is stabilizing but divergent, and property remains a persistent but slightly milder drag.

\- Infrastructure capex will likely accelerate modestly with carryover of quasi-fiscal funding: The newly planned RMB800bn in policy-based financing instruments, together with RMB500bn carried over from 2H25 – largely unused owing to a lack of eligible projects – should more than offset the continued decline in local government land revenue. At the same time, the front-loading and launch of key national strategic projects under the 15th Five-Year Plan helps alleviate the project pipeline bottleneck that constrained infrastructure spending last year.

\- Overall manufacturing capacity consolidation to continue: Anti-involution policies should continue to cap manufacturing investment upside, following the rapid capacity buildout in 2022-24 that partially offset the housing investment slump. That said, there should be wider divergence across sectors: those with severe excess capacity (e.g., solar) may see capacity utilization improve but are unlikely to add new investment, while sectors where supply and demand are more balanced/tight amid AI- and green transition-related demand (e.g., power equipment) could see investment accelerate.

\- Property investment to remain sluggish in view of weak new starts and land sales: Years of declining new starts have depleted the construction pipeline, and the weakness has persisted into 2026: new starts fell another 22% YoY and land sale revenues declined 24%, pointing to subdued construction activity in coming quarters. While secondary home sales have shown signs of recovery, the improvement remains localized and narrow, concentrated in select Cities and low-lump sum units. We expect broader stabilization across Tier 1 and 2 Cities by 2027, but until then, property investment will likely remain sluggish, though incrementally less bad.

Exhibit 5: Structural labor market weakness in non-manufacturing sectors   
![](images/8337072479dd46dade52cb5d4256fda97fe2061ee044b4600f4844c3f70d0d2b.jpg)

<details>
<summary>line</summary>

| Date   | Manufacturing | Non-manufacturing |
|--------|---------------|-------------------|
| Apr-15 | 48.0          | 49.0              |
| Apr-16 | 47.5          | 48.5              |
| Apr-17 | 49.5          | 50.5              |
| Apr-18 | 48.5          | 49.0              |
| Apr-19 | 47.0          | 48.0              |
| Apr-20 | 51.0          | 48.5              |
| Apr-21 | 49.5          | 48.0              |
| Apr-22 | 47.0          | 46.0              |
| Apr-23 | 45.0          | 43.0              |
| Apr-24 | 48.0          | 46.0              |
| Apr-25 | 48.5          | 45.5              |
| Apr-26 | 49.0          | 45.0              |
</details>

Source: NBS, MS

Exhibit 6: AI diffusion could further weigh on youth employment, which is already at a low starting point   
![](images/ffa94dfca5a26bd98dac1c7f32a312071a267c7eadeb180d25df8e587cd97745.jpg)

<details>
<summary>bar</summary>

| Date    | Unemployment Rate (pp) |
|---------|------------------------|
| Mar-19  | 0.8                    |
| Jul-19  | 1.5                    |
| Nov-19  | 2.5                    |
| Mar-20  | 3.8                    |
| Jul-20  | 3.7                    |
| Nov-20  | 2.0                    |
| Mar-21  | -0.5                   |
| Jul-21  | -1.0                   |
| Nov-21  | 1.5                    |
| Mar-22  | 4.5                    |
| Jul-22  | 3.8                    |
| Nov-22  | 3.5                    |
| Mar-23  | 3.7                    |
| Jul-23  | 2.0                    |
| Nov-23  | 1.8                    |
| Mar-24  | 0.8                    |
| Jul-24  | 0.5                    |
| Nov-24  | 1.5                    |
| Mar-25  | 1.2                    |
| Jul-25  | 0.8                    |
| Nov-25  | 0.5                    |
| Mar-26  | -0.5                   |
</details>

Source: CEIC, MS

Exhibit 7:   
FAI Breakdown 

<table><tr><td></td><td>Weight</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td></tr><tr><td>Overall FAI Growth</td><td>100%</td><td>5.4%</td><td>2.9%</td><td>4.9%</td><td>5.1%</td><td>3.0%</td><td>3.2%</td><td>-3.8%</td><td>3.0%</td><td>2.0%</td></tr><tr><td>Manufacturing</td><td>36%</td><td>3.1%</td><td>-2.2%</td><td>13.5%</td><td>9.1%</td><td>6.5%</td><td>9.2%</td><td>0.6%</td><td>4.5%</td><td>4.0%</td></tr><tr><td>Infrastructure</td><td>29%</td><td>3.3%</td><td>3.4%</td><td>0.2%</td><td>11.5%</td><td>8.2%</td><td>9.2%</td><td>-1.5%</td><td>8.0%</td><td>4.5%</td></tr><tr><td>- Utility</td><td>7%</td><td>4.5%</td><td>17.6%</td><td>1.1%</td><td>19.3%</td><td>23.0%</td><td>23.9%</td><td>9.1%</td><td>8.5%</td><td>6.0%</td></tr><tr><td>- Transportation, Storage and Postal Service</td><td>10%</td><td>3.4%</td><td>1.4%</td><td>1.6%</td><td>9.1%</td><td>10.5%</td><td>5.9%</td><td>-1.2%</td><td>12.5%</td><td>4.9%</td></tr><tr><td>- Water Conservancy &amp; Environment Management</td><td>12%</td><td>2.9%</td><td>0.2%</td><td>-1.2%</td><td>10.3%</td><td>0.1%</td><td>4.2%</td><td>-8.4%</td><td>3.5%</td><td>3.0%</td></tr><tr><td>Property</td><td>16%</td><td>9.2%</td><td>5.0%</td><td>5.0%</td><td>-8.4%</td><td>-8.1%</td><td>-10.8%</td><td>-17.5%</td><td>-11.5%</td><td>-10.0%</td></tr><tr><td>By Developers</td><td>13%</td><td>9.9%</td><td>7.0%</td><td>4.4%</td><td>-10.0%</td><td>-9.6%</td><td>-10.6%</td><td>-17.2%</td><td>-14.0%</td><td>-12.5%</t

[中间内容因长度限制已省略]

ccepts responsibility for its contents; in Korea by MS & Co International plc, Seoul Branch; in India by MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the United States by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

© 2026 MS
"""
