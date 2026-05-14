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
# US Equity Strategy Watch

S&P 500 above 8,000? It's possible: we outline how

Equity Strategy
North America

- We revise higher our year-end 2026 S&P 500 target to 7,650 on earnings strength...   
- ... but could see the S&P 500 breaching 8,000 on a sentiment rebound in tech, AI, geopolitics, macro, etc   
- Downside risks include tech earnings slowdown, energy supply shocks, a Fed pivot to hikes

The S&P 500 is back at record highs as tech stages a comeback, US Equity Wrap, 4 May. A solid Q1 earnings season is also providing support. We're taking the opportunity to revise our 2026 index EPS estimates up by $8\%$ , incorporating the latest quarterly results. We now expect 2026 EPS growth of $20\%$ or USD325, with tech/Mag7 still the main drivers. With higher earnings expectations, we revise our year-end S&P 500 target to 7,650 from 7,500 previously.

While earnings remain supportive, sentiment is on shakier ground. The recent rally has been relatively narrow in breadth. Most stocks are still trading below their 52-week highs, suggesting scope for further upside if participation broadens. For that to happen, we'd look for a rebound in sentiment across tech, continued AI adoption, and an easing of concerns around geopolitics, trade, and rates.

A sentiment rebound could drive the S&P 500 past the 8,000 mark, in our view. We outline several potential paths for the index to notch another leg higher, including:

◆ Tech re-rates as IPOs set a higher bar for valuations   
Laggards catch-up as geopolitical and trade uncertainties fade   
- AI efficiency gains broaden as margins expand   
A “Goldilocks” backdrop returns as long-term rates fall

We see each of these potential paths adding between 100–700 pts to the S&P 500. The clearest route to an additional leg up rests with tech: the sector (including hyperscalers) now represents over half of the S&P 500's market cap and more than 40% of index earnings. As a result, sentiment around tech is one of the biggest swing factors. We also see long-term rates as key. While the market has partially decoupled from long-term rate moves, the rate environment may become increasingly important as tech companies look to finance capex.

Downside risks: What could reverse the rally? Key concerns include sustained elevated oil prices feeding through to slower economic growth; a slowdown in tech earnings coinciding with elevated capex needs; and a hawkish Fed pivot if inflation re-accelerates.

# Nicole Inui\*, CFA

Head of Equity Strategy, Americas

Banco HSBC S.A.

nicole.inui@HSBC.com

+55 11 2802 3475

# Alastair Pinder, CFA

Head EM and Global Equity Strategist

HSBC Securities (USA) Inc.

alastair.pinder@us.HSBC.com

+1 212 525 5972

\* Employed by a non-US affiliate of HSBC Securities (USA) Inc, and is not registered/ qualified pursuant to FINRA regulations

HSBC Funding the Future Survey

Sentiment, AI and Private Credit

Click to view

# Disclosures & Disclaimer

This report must be read with the disclosures and the analyst certifications in the Disclosure appendix, and with the Disclaimer, which forms part of it.

Issuer of report: Banco HSBC S.A.

View HSBC Global Investment Research at:

https://www.research.HSBC.com

# Path to breaching 8,000 on the S&P 500

# Tech re-rates: potentially adding 300-700+ points

Tech companies (including hyperscalers) now represent over half of the S&P 500's market cap and more than $40\%$ of index earnings. As a result, sentiment around tech is one of the biggest swing factors for the S&P 500 performance. Valuations look reasonable, with the sector (IT and Mag 7) trading on a forward P/E of 25.8x and forward 12-month consensus earnings estimated to grow c31%. That said, valuations remain below prior highs: a return to those levels would add c360 points to the S&P 500. We could also see the sector trading at a premium to prior highs if IPOs of AI/tech stocks set a higher bar for valuations, potentially adding 700 points or more to the index. During the late-1990s internet boom, tech stocks traded at an average $50\%$ -plus premium to the overall market; today, that premium is $12\%$ (and below the average since the release of ChatGPT).

Tech premium off recent peak levels and well below dot com boom extremes   
![](images/e7bebd57504119d88139c727ba5533a8537de392b0985a798520cd25a9c93751.jpg)

<details>
<summary>line</summary>

| Year | Average premium % |
|------|-------------------|
| 1998 | 1998 - 2000       |
| 2024 | Average premium % since release of ChatGPT |
</details>

Source: IBES, LSEG Datastream, HSBC

IPOs are picking up at the start of the year...   
![](images/b9b46c760f62b379d166c6526699b95a360bd47fda74a83b9b584f0a7bc14bf0.jpg)

<details>
<summary>line</summary>

| Month | 2023 | 2024 | 2025 | 2026 |
|-------|------|------|------|------|
| Jan   | 15   | 10   | 20   | 30   |
| Mar   | 40   | 30   | 50   | 80   |
| May   | 60   | 50   | 100  | 110  |
| Jul   | 90   | 80   | 140  | -    |
| Sep   | 110  | 130  | 180  | -    |
| Nov   | 140  | 170  | 270  | -    |
</details>

Source: Bloomberg, HSBC Includes only priced IPOs

... but still lagging behind the IPO tech spree in the late 1990s   
![](images/408c3553288cb9170087ecf97483b3a19a1b14b701abb2ad700286ee0df92b26.jpg)

<details>
<summary>line</summary>

| Month | 1998 | 1999 | 2000 | 2026 |
|---|---|---|---|---|
| Jan | 30 | 35 | 35 | 35 |
| Mar | 100 | 120 | 140 | 100 |
| May | 200 | 180 | 220 | 120 |
| Jul | 320 | 340 | 360 | - |
| Sep | 350 | 420 | 440 | - |
| Nov | 380 | 580 | 620 | - |
| End | 430 | 620 | 630 | - |
</details>

Source: Bloomberg, HSBC Includes only priced IPOs

# Laggards catch up: potentially adding 100+ points

Geopolitical and trade policy uncertainty, while easing, remains elevated. Some sectors exposed to trade and geopolitical risks have underperformed. The consumer staples sector, for example, is feeling the hit to consumption from higher oil prices, alongside cost pressures linked to trade policy. Industrials is another area of vulnerability to trade, given the sector's reliance on imported inputs and exposure to supply-chain disruption, but overall, the sector is roughly flat since the Middle East conflict began as AI beneficiaries outperform. If uncertainty retreats to prior levels, these laggards (highlighted in chart below) could catch up, adding c130 points to the S&P 500.

US Geopolitical uncertainty remains at elevated levels...   
![](images/a3f14e6d7532613eb631283fe98f287f4379c162afbf1b9448975072aa0bbc81.jpg)

<details>
<summary>line</summary>

| Date   | US Geopolitical risk uncertainty |
|--------|----------------------------------|
| Apr-16 | ~100                             |
| Apr-18 | ~120                             |
| Apr-20 | ~80                              |
| Apr-22 | ~320                             |
| Apr-24 | ~180                             |
| Apr-26 | ~330                             |
</details>

Source: LSEG Datastream, HSBC

...while trade policy uncertainty is falling but still at higher than historical levels   
![](images/79de69d4cc6c84e51e2711ec2b08dd97d3982ef8fcf26ead4937a5208bc03b1d.jpg)

<details>
<summary>line</summary>

| Date    | US trade policy uncertainty |
|---------|-----------------------------|
| Apr-16  | ~0                          |
| Apr-18  | ~500                        |
| Apr-20  | ~2000                       |
| Apr-22  | ~0                          |
| Apr-24  | ~0                          |
| Apr-26  | ~8000                       |
</details>

Source: LSEG Datastream, HSBC

US industry groups performance since the start of the Iran conflict   
![](images/c00472d0c656abf9c7b3c0badb14bd14302c9159aacbecbf9bd21f1f8a2328f7.jpg)

<details>
<summary>bar</summary>

| Sector | US Industry groups absolute performance since Iran war (%) |
|---|---|
| S&P 500 | 7 |
| Semis | 31 |
| Cons Disc Dist.&Ret. | 17 |
| Tech Hi/wEq | 14 |
| Media | 14 |
| Banks | 5 |
| Software | 4 |
| Equity REITs | 2 |
| Energy | 1 |
| Cap Goods | 1 |
| Financial Svs | -1 |
| Transportation | -1 |
| Cons Stap Dist.&Ret. | -1 |
Autos | -1 |
| Materials | -2 |
| Utilities | -3 |
| Consumer Svs. | -4 |
| Insurance | -5 |
| Food Bev&Tob. | -6 |
| RealEstate Mgmt&Dev. | -8 |
| Pharma | -9 |
| Telecom | -10 |
| Health Care Eq&Svs. | -11 |
| Comm&Prof Svs | -12 |
| House.&Pers Prod. | -13 |
| Cons Dur&App. | -15 |
</details>

Source: FactSet, HSBC

# AI efficiency gains broaden: potentially adding 200 points

Better sentiment around AI adoption and efficiency-driven margin improvement has been centered on tech so far, but as adoption widens, the market could start pricing in higher margins across other sectors—particularly those that are more labor-intensive. A rebound in sentiment around AI adoption and disruption would likely hinge on a re-rating, supported by clearer evidence of margin and profitability benefits. A major sentiment shift leading to a re-rating for AI adopters could add c200 points to the S&P 500 (assuming both software and financials re-rate).

AI adoption by US businesses is rising overall...   
![](images/227c825669857763ef3885a85f714e6db12ff49d9f2a581173ab877d2f59986b.jpg)

<details>
<summary>line</summary>

| Date   | RampAI Adoption |
| ------ | --------------- |
| Mar-23 | 8               |
| Mar-24 | 16              |
| Mar-25 | 40              |
| Mar-26 | 50              |
</details>

Source: Ramp AI, HSBC   
Note: Percentage of US businesses adopting AI

... with certain sectors increasingly reporting the use of AI   
![](images/e8138c4ac7ff287939cbebce8202f40ed8c5c88da1613452402956b7dd2d9131.jpg)

<details>
<summary>bar</summary>

| Sector | Proportion of businesses reporting use of AI (%) |
| :--- | :--- |
| IT | 38 |
| Prof Services | 34 |
| Education | 30 |
| Finance | 30 |
| Real Estate | 23 |
| Management | 21 |
| Health Care | 20 |
| Entertainment | 17 |
| Admin | 16 |
| Utilities | 13 |
| Wholesale Trade | 13 |
| Retail Trade | 12 |
| Manufacturing | 12 |
| Other Services | 10 |
| Construction | 9 |
| Food Service | 8 |
</details>

Source: US Consensus Bureau, HSBC

Net profit margins for the tech sector have risen exponentially...   
![](images/6f20c683d4a5e7cf05c31fbe1415622c47293849f8ca9f9096d04f2f09d68f0c.jpg)

<details>
<summary>line</summary>

| Date   | N12M net profit margins (%) |
|--------|-----------------------------|
| May-16 | 17%                         |
| May-18 | 21%                         |
| May-20 | 20%                         |
| May-22 | 24%                         |
| May-24 | 28%                         |
| May-26 | 33%                         |
</details>

Source: FactSet, HSBC

...while the rest of the index is also seeing margin gains but at a slower pace   
![](images/b1053b78900764e1729a44211e8f94bf5cfc60ce92bd9115398fe11faf012259.jpg)

<details>
<summary>line</summary>

| Date   | N12M net profit margins (%) |
|--------|-----------------------------|
| May-16 | 9.5%                        |
| May-18 | 11.0%                       |
| May-20 | 8.5%                        |
| May-22 | 11.5%                       |
| May-24 | 11.0%                       |
| May-26 | 12.0%                       |
</details>

Source: FactSet, HSBC

# Goldilocks backdrop returns: potentially adding 300 points

Macro sentiment improves – US 10-year Treasury yields are once again rising, getting close to the “danger zone” cited by our multi-asset team as the level at which risk assets tend to falter. Hawkish messaging from certain Fed members, alongside solid jobs growth and higher headline inflation pushed yields higher, though they’ve since eased somewhat. US mortgage rates also remain stubbornly above 6%. If yields move lower in a Goldilocks scenario – disinflation continuing towards 2% alongside resilient growth – equity valuations and earnings would likely lift, potentially adding c300 points to the S&P 500.

Tech has outperformed in spite of rising treasury yields...   
![](images/eaa402b1313af2ae42d667bfce405616fcbb2248f2a641e84821059721f33860.jpg)

<details>
<summary>line</summary>

| Date   | US 10Y Bond Yield (%, Inverted) | SPX IT relative to SPX (RHS) |
|--------|----------------------------------|------------------------------|
| May-25 | 4.3                              | 0.70                         |
| Aug-25 | 4.2                              | 0.75                         |
| Nov-25 | 4.1                              | 0.80                         |
| Feb-26 | 4.0                              | 0.85                         |
| May-26 | 3.9                              | 0.90                         |
</details>

Source: LSEG Datastream, HSBC

...but rates could become more relevant for sector performance as capex rises   
![](images/9c178f21fedb4c1a4d76e30bbeab589aa90cf1f1c1c3b98aa9060e6e480b6981.jpg)

<details>
<summary>bar</summary>

| Year | US hyperscalers capex (USDbn) |
|---|---|
| 2020 | 95 |
| 2021 | 125 |
| 2022 | 155 |
| 2023 | 160 |
| 2024 | 240 |
| 2025 | 420 |
| 2026e | 720 |
| 2027e | 860 |
</details>

Source: FactSet, HSBC Hyperscalers include Amazon (AMZN US, Buy, CMP USD271.17); Alphabet (GOOGL US, Buy, CMP USD397.99), Meta Platforms (META US, Buy, CMP USD616.81); Microsoft (MSFT US, Buy, CMP USD420.77); and Oracle (ORCL US, Buy, CMP USD194.59). Prices as of close on 7 May 2026

S&P 500 sensitivity table to bond yields and earnings growth 

<table><tr><td rowspan="2" colspan="2"></td><td colspan="6">US 10Y bond yield (%)</td></tr><tr><td>3.0</td><td>3.5</td><td>4.0</td><td>4.3</td><td>4.5</td><td>5.0</td></tr><tr><td rowspan="6">2026 EPS</td><td>11%</td><td>7220</td><td>7150</td><td>7090</td><td>7050</td><td>7030</td><td>6970</td></tr><tr><td>15%</td><td>7460</td><td>7400</td><td>7330</td><td>7290</td><td>7260</td><td>7200</td></tr><tr><td>17%</td><td>7580</td><td>7510</td><td>7446</td><td>7410</td><td>7380</td><td>7310</td></tr><tr><td>20%</td><td>7820</td><td>7760</td><td>7690</td><td>7650</td><td>7620</td><td>7550</td></tr><tr><td>24%</td><td>8060</td><td>7990</td><td>7900</td><td>7880</td><td>7850</td><td>7780</td></tr><tr><td>26%</td><td>8180</td><td>8110</td><td>8040</td><td>7990</td><td>7970</td><td>7900</td></tr></table>

Source: LSEG Datastream, FactSet, HSBC Shaded cells represent S&P index target at 4% 10Y bond yields, Dark shaded cell represents current S&P target

# Tech and its relevance in the index

Mag 7 + IT market weight within S&P 500 close to all time high ...   
![](images/d45be72544077d1d078c86bd3284bf880bc931def4e65891483d5563f9c10ed3.jpg)

<details>
<summary>line</summary>

| Date   | Mag & + IT marketcap as % of SPX |
|--------|-----------------------------------|
| Jan-20 | 34                                |
| Jan-21 | 42                                |
| Jan-22 | 43                                |
| Jan-23 | 34                                |
| Jan-24 | 45                                |
| Jan-25 | 47                                |
| Jan-26 | 51                                |
</details>

Source: FactSet, HSBC

...and its forward 12-month earnings weight steadily moves higher   
![](images/46743733a4125a6e7d9b080a338d9139e48281a63da3bed0110951a532fc5274.jpg)

<details>
<summary>line</summary>

| Date   | Mag 7 + IT companies earnings weight in S&P 500 (%) |
|--------|--------------------------------------------------|
| Jan-20 | 24.0                                             |
| Jan-21 | 28.5                                             |
| Jan-22 | 29.0                                             |
| Jan-23 | 26.0                                             |
| Jan-24 | 31.0                                             |
| Jan-25 | 35.0                                             |
| Jan-26 | 43.0                                             |
</details>

Source: FactSet, HSBC

Earnings growth expectations for the S&P excluding tech in the low double digits   
![](images/f1b988f484a1ec1ddc0cb53d92ed9594d930f96e2a1454a362a985b423d6fafd.jpg)

<details>
<summary>bar</summary>

| Year | S&P 500 | S&P ex Mag 7 | S&P 500 ex IT & Mag 7 |
|---|---|---|---|
| 2026e | 21.8 | 18.4 | 11.7 |
| 2027e | 13.3 | 12.3 | 8.7 |
</details>

Source: FactSet, HSBC

Capex growth still driven by the Mag7 and tech cohort   
![](images/6f5602c3c505adc82347617071ddc3520a6c652f788fb6b1585f64adbd47906a.jpg)

<details>
<summary>bar</summary>

YTD Change in 2026 Capex revisions (%)
| Sector | YTD Change (%) |
| :--- | :--- |
| S&P 500 | 14 |
| Mag 7 | 39 |
| Cons Disc | 28 |
| Comm Serv | 24 |
| IT | 12 |
| Utilities | 10 |
| Financials | 10 |
| Industrials | 7 |
| Energy | 4 |
| Real Estate | 4 |
| Health Care | 4 |
| Cons Stap | 3 |
| Materials | 1 |
</details>

Source: LSEG Datastream, HSBC

Semis and Tech hardware & equipment seeing strong earnings revisions...   
![](images/4463b92828212fb329d3941af16134afc78dbf927e1280336c418c4ad700c926.jpg)

<details>
<summary>line</summary>

| Date   | Semis | Tech H/w & Eq. | Software | S&P ex IT |
|--------|-------|----------------|----------|-----------|
| Apr-21 | 7.0   | 7.0            | 5.0      | 5.0       |
| Apr-22 | 4.0   | 3.0            | 2.0      | 1.0       |
| Apr-23 | -6.0  | -3.0           | -2.0     | -1.0      |
| Apr-24 | 1.0   | 2.0            | 3.0      | 1.0       |
| Apr-25 | 4.0   | 6.0            | 5.0      | 2.0       |
| Apr-26 | 5.0   | 7.0            | 6.0      | 3.0       |
</details>

Source: IBES, LSEG Datastream, HSBC

...as IT and Mag 7 see one of the strongest earnings growth potential in 2026e   
![](images/3b136cb5783919365ce7cbd377c1966b6a0aae4fc0c814ffc76357e68fe43418.jpg)

<details>
<summary>bar</summary>

| Sector | Latest (%) | Jan-26 (%) |
| :--- | :--- | :--- |
| S&P 500 | 22 | 15 |
| Energy | 49 | 5 |
| IT | 43 | 28 |
| Materials | 36 | 20 |
| Mag 7 | 30 | 20 |
| Comm Serv. | 27 | 15 |
| Cons Disc | 13 | 11 |
| Utilities | 11 | 9 |
| Industrials | 10 | 15 |
| Financials | 9 | 10 |
| Health Care | 8 | 8 |
| Real Estate | 6 | 6 |
| Cons Stap | 5 | 7 |
</details>

Source FactSet, HSBC

# Valuations

S&P 500 trades at $5\%$ premium to its five-year average   
![](images/0702ec5f32f4544e792704fdbd7bd0222f66be359c88452e1b507c6e7d3278a4.jpg)

<details>
<summary>line</summary>

| Date   | S&P 500 | Average | +/- 1Stdev |
|--------|---------|---------|------------|
| May-21 | 22      | 20      | 18         |
| May-22 | 16      | 20      | 18         |
| May-23 | 18      | 20      | 18         |
| May-24 | 20      | 20      | 18         |
| May-25 | 23      | 20      | 18         |
| May-26 | 21      | 20      | 18         |
</details>

Source: FactSet, HSBC

Even when excluding tech, S&P 500 trades at a 5% premium to historical average   
![](images/1578251787885d6d5346ea0288c3aa7e87612deef0d4d4ac4bf677196ef3d336.jpg)



[中间内容因长度限制已省略]

on-US foreign affiliate, the issuer of this report.

In Japan, this publication has been distributed by HSBC Securities (Japan) Co., Ltd.. It may not be further distributed in whole or in part for any purpose. In Hong Kong, this document has been distributed by The Hongkong and Shanghai Banking Corporation Limited in the conduct of its Hong Kong regulated business for the information of its institutional and professional investor (as defined by the Securities and Future Ordinance (Chapter 5710) customers only; it is not intended for and should not be distributed to retail customers in Hong Kong, unless permitted otherwise. The Hongkong and Shanghai Banking Corporation Limited is regulated by the Hong Kong Monetary Authority. All enquires by recipients in Hong Kong must be directed to your HSBC contact in Hong Kong. If it is received by a customer of an affiliate of HSBC, its provision to the recipient is subject to the terms of business in place between the recipient and such affiliate. The Hongkong and Shanghai Banking Corporation Limited makes no representations that the products or services mentioned in this document are available to persons in Hong Kong or are necessarily suitable for any particular person or appropriate in accordance with local law. It may not be further distributed in whole or in part for any purpose.

In Singapore, this publication is distributed by The Hongkong and Shanghai Banking Corporation Limited, Singapore Branch for the general information of institutional investors or other persons specified in Sections 274 and 304 of the Securities and Futures Act 2001 of Singapore ("SFA") and accredited investors and other persons in accordance with the conditions specified in Sections 275 and 305 of the SFA. Only Economics or Currencies reports are intended for distribution to a person who is not an Accredited Investor, Expert Investor or Institutional Investor as defined in SFA. The Hongkong and Shanghai Banking Corporation Limited, Singapore Branch accepts legal responsibility for the contents of reports. This publication is not a prospectus as defined in the SFA. It may not be further distributed in whole or in part for any purpose. The Hongkong and Shanghai Banking Corporation Limited Singapore Branch is regulated by the Monetary Authority of Singapore. Recipients in Singapore should contact a "Hongkong and Shanghai Banking Corporation Limited, Singapore Branch" representative in respect of any matters arising from, or in connection with this report. Please refer to The Hongkong and Shanghai Banking Corporation Limited Singapore Branch's website at www.business.HSBC.com.sg for contact details.

In Korea, this publication is distributed by either The Hongkong and Shanghai Banking Corporation Limited, Seoul Securities Branch ("HBAP SLS") or The Hongkong and Shanghai Banking Corporation Limited, Seoul Branch ("HBAP SEL") for the general information of professional investors specified in Article 9 of the Financial Investment Services and Capital Markets Act ("FSCMA"). This publication is not a prospectus as defined in the FSCMA. It may not be further distributed in whole or in part for any purpose. Both HBAP SLS and HBAP SEL are regulated by the Financial Services Commission and the Financial Supervisory Service of Korea.

In Australia, this publication has been distributed by The Hongkong and Shanghai Banking Corporation Limited (ABN 65 117 925 970, AFSL 301737) for the general information of its "wholesale" customers (as defined in the Corporations Act 2001). Where distributed to retail customers, this research is distributed by HSBC Bank Australia Limited (ABN 48 006 434 162, AFSL No. 232595). These respective entities make no representations that the products or services mentioned in this document are available to persons in Australia or are necessarily suitable for any particular person or appropriate in accordance with local law. No consideration has been given to the particular investment objectives, financial situation or particular needs of any recipient.

HSBC México, S.A., Institución de Banca Múltiple, Grupo Financiero HSBC is authorized and regulated by Secretaría de Hacienda y Crédito Público and Comisión Nacional Bancaria y de Valores (CNBV).

If you are a customer of HSBC International Wealth & Premier Banking ("IWPB"), including HSBC Private Bank, you are eligible to receive this publication only if: (i) you have been approved to receive relevant research publications by an applicable HSBC legal entity; (ii) you have agreed to the applicable HSBC entity's terms and conditions and/or customer declaration for accessing research; and (iii) you have agreed to the terms and conditions of any other internet banking, online banking, mobile banking and/or investment services offered by that HSBC entity, through which you will access research publications (collectively with (ii), the "Terms"). If you do not meet the above eligibility requirements, please disregard this publication and, if you are a IWPB customer, please notify your Relationship Manager or call the relevant customer hotline. Distribution of this publication is the sole responsibility of the HSBC entity with whom you have agreed the Terms. Receipt of research publications is strictly subject to the Terms and any other conditions or disclaimers applicable to the provision of the publications that may be advised by IWPB.

© Copyright 2026, Banco HSBC S.A., ALL RIGHTS RESERVED. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, on any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of Banco HSBC S.A.

[1279064]
"""
