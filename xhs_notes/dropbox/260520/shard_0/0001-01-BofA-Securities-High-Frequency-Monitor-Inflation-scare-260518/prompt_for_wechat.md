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
# High Frequency Monitor Inflation scare

# Global equities moderated on inflation concerns

Global equity markets fell -0.6% last week as optimism surrounding earnings and the AI theme was offset by concerns about rising inflation. Last week, the best performing region was the US (+0.2%) while Emerging Markets lagged (-2.5%). Among global sectors, Energy (+4.2%) and Tech Hardware (+2.0%) were the best performers, while Utilities (-3.0%), Materials (-3.0%) and Real Estate (-2.9%) fell the most. The global earnings cycle remains strong and the Global News Pulse is improving, but an increasing risk is that rising inflation prompts central banks to raise rates.

# Best performing themes: Space, Renewable Energy

Last week, among the 12 themes we monitor, the best performers were Space (+4.3%) and Renewable Energy (+1.5%). In contrast, Nuclear Energy (-7.2%), Gold (-6.8%), and Luxury Lifestyle (-5.4%) performed worst. Triple Momentum remains strongest for Gold, Rare Earths, and Robotics, and weakest for Luxury Lifestyle and SaaS.

# Triple Momentum: Semis, Energy, Tech Hardware

By global sector, Triple Momentum remains strongest for Semis, Energy, and Tech Hardware. Among large and liquid stocks globally (min \$20bn market cap and \$20mn ADTV), the Triple Momentum Rank is highest for Bloom Energy, Renesas Electronics, Samsung SDI, SEMCO, Murata, Shinhan Financial, STMicroelectronics, Intel, and AMD.

Chart 1: Triple Momentum for Global Themes (earnings, price, news)   
Triple Momentum strongest for Gold and Rare Earths, weakest for SaaS and Luxury Lifestyle   
![](images/64d6a1883168d8ea4b4b1aaf5cfa4bd0574623cd3a68990205800c48e2b8870c.jpg)

<details>
<summary>scatter</summary>

| Company           | Price Momentum Rank (100 = Best) | Earnings Momentum Rank (100 = Best) |
| ----------------- | -------------------------------- | ------------------------------------ |
| SaaS              | 15                               | 60                                   |
| Luxury Lifestyle  | 38                               | 42                                   |
| AI                | 52                               | 57                                   |
| Defense           | 53                               | 49                                   |
| Quantum           | 56                               | 62                                   |
| Space             | 66                               | 46                                   |
| Renewable Energy  | 63                               | 35                                   |
| Robotics          | 67                               | 60                                   |
| Space             | 67                               | 46                                   |
| Energy Storage    | 78                               | 57                                   |
| Rare Earths       | 81                               | 53                                   |
| Gold              | 83                               | 73                                   |
</details>

Source : BofA Global Quantitative Strategy, MSCI, IBES, RavenPack

BofA GLOBAL RESEARCH

Trading ideas and investment strategies discussed herein may give rise to significant risk and are not suitable for all investors. Investors should have experience in relevant markets and the financial resources to absorb any losses arising from applying these ideas or strategies.

>> Employed by a non-US affiliate of BofAS and is not registered/qualified as a research analyst under the FINRA rules.

Refer to "Other Important Disclosures" for information on certain BofA entities that take responsibility for the information herein in particular jurisdictions.

BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.

# 18 May 2026

Quant Strategy

Global

Nigel Tupper >>

Quant Strategist

BofA (Australia)

+61 2 9226 5735

nigel.tupper@bofa.com

Amar Vashi >>

Quant Strategist

BofA (Australia)

amar.vashi@bofa.com

Sumuhan Shanmugalingam >>

Quant Strategist

BofA (Australia)

sumuhan.shanmugalingam@bofa.com

Unless otherwise noted all links on the front page of this report refer to sections in this research report.

Market Performance

Style Performance

Earnings Revision Ratio

Earnings Revision Ratio by Style

NewsAlpha

Word Cloud

Tactical Indicators

Volatility

Rates

Triple Momentum

Themes

# Contents

Notice to Readers: 3

Market Performance 4

Market Breadth 6

Style Performance 7

Global Wave and Earnings 8

Earnings Revision Ratio 9

Quantessential Styles: Earnings Revision Ratio 11

NewsAlpha 12

Tactical Indicators 15

Commodities 17

Volatility 18

Fed 19

Rates 20

Valuation 23

Revenue Exposure 24

Triple Momentum 25

Global Regions: Triple Momentum Charts 29

Global Sectors: Triple Momentum Charts 32

Countries: Triple Momentum Charts 40

Themes 43

Performance by Theme 43

Ranking by Triple Momentum 44

What's Improving / Deteriorating? 45

Global Stocks (Most Important) by Theme 47

Asia Stocks (Most Important) by Theme 49

Country Exposure to Themes 51

# Notice to Readers:

The various screens identified in this report are intended to be indicative metrics only and may not be used for reference purposes or as a measure of performance for any financial instrument or contract, or otherwise relied upon by third parties for any other purpose, without the prior written consent of BofA Global Research. These screens were not created to act as a benchmark.

The Global News Pulse (and the regional and sectors versions of it) is intended to be an indicative metric only and may not be used for reference purposes or as a measure of performance for any financial instrument or contract, or otherwise relied upon by third parties for any other purpose, without the prior written consent of BofA Global Research. This News Pulse was not created to act as a benchmark.

Please refer to the “Global Quant Publications” page for a summary of all our published reports which details methodology on each of the analysis included in this report.

# Market Performance

Chart 2: Global Regions Performance: Last Week   
Best performing region last week was the USA   
![](images/5d7bf4f7817739e2857a3dcc0d72e097421be0153c0d48926ee92b30d8b70cc9.jpg)

<details>
<summary>bar</summary>

| Region | Returns (USD) |
| :--- | :--- |
| USA | 0.2 |
| Global | -0.6 |
| Japan | -0.8 |
| Europe | -2.0 |
| Asia Pac ex-Japan | -2.1 |
| GEM | -2.5 |
</details>

Source : BofA Global Quantitative Strategy, MSCI   
BofA GLOBAL RESEARCH

Chart 4: Global Regions Performance: MTD   
Asia Pac ex-Japan is the best performing region this month   
![](images/116e5debab9182fd6c1a02246e404b4be6ba5aa17ad70cbc4e06975ab7c7ca64.jpg)

<details>
<summary>bar</summary>

| Category | Returns (USD) |
| :--- | :--- |
| Asia Pacific ex Japan | 4.7% |
| GEM | 4.2% |
| USA | 2.7% |
| Japan | 2.1% |
| Global | 2.0% |
| Europe | -1.5% |
</details>

Source : BofA Global Quantitative Strategy, MSCI   
BofA GLOBAL RESEARCH

Chart 6: Global Regions Performance: YTD   
Asia Pac ex-Japan is the best performing region this year   
![](images/eb744f397d3b435fa8fde1a802589541866eb41dd8d03d2672848a6eb1348000.jpg)

<details>
<summary>bar</summary>

| Category | Returns (USD) (%) |
| :--- | :--- |
| Asia Pac ex-Japan | 19.1 |
| GEM | 18.8 |
| Japan | 12.1 |
| Global | 8.3 |
| USA | 7.9 |
| Europe | 1.4 |
</details>

Source : BofA Global Quantitative Strategy, MSCI   
BofA GLOBAL RESEARCH

Chart 3: Global Sectors Performance: Last Week   
Best performing sector last week was Energy   
![](images/f416d44046aa4e75a4f1c19292361a3f3ce8cb7a92d8cf800a5f9498705657d6.jpg)

<details>
<summary>bar</summary>

| Sector             | Returns (USD) |
| ------------------ | ------------- |
| Energy             | 4.2%          |
| Tech Hardware      | 2.0%          |
| Health Care        | 0.5%          |
| Cons. Staples      | 0.4%          |
| Software           | 0.3%          |
| Insurance          | 0.2%          |
| Semiconductors     | 0.1%          |
| Div/Financials     | -0.5%         |
| Media & Ent.       | -1.0%         |
| Telecom            | -1.9%         |
| Banks              | -2.2%         |
| Industrials        | -2.4%         |
| Cons. Discretionary| -2.4%         |
| Real Estate        | -2.9%         |
| Materials          | -3.0%         |
| Utilities          | -3.0%         |
</details>

Source : BofA Global Quantitative Strategy, MSCI   
BofA GLOBAL RESEARCH

Chart 5: Global Sectors Performance: MTD   
Semiconductors is the best performing sector this month   
![](images/116c4cf0281c116ecf2248aaa52875e9fdcb923cafefcf30884851943807edd3.jpg)

<details>
<summary>bar</summary>

| Sector           | Returns (USD) |
| ---------------- | ------------- |
| Semiconductors   | 11.7%         |
| Tech Hardware    | 10.2%         |
| Software         | 4.7%          |
| Media & Ent      | 1.2%          |
| Cons Staples    | 0.2%          |
| Materials        | -0.1%         |
| Cons Discretionary | -0.1%       |
| Insurance        | -0.2%         |
| Div Financials   | -0.8%         |
| Health Care      | -1.1%         |
| Telecom          | -1.2%         |
| Industrials      | -1.6%         |
| Energy           | -1.8%         |
| Real Estate      | -2.4%         |
| Banks            | -2.7%         |
| Utilities        | -6.3%         |
</details>

Source : BofA Global Quantitative Strategy, MSCI   
BofA GLOBAL RESEARCH

Chart 7: Global Sectors Performance: YTD   
Semiconductors is the best performing sector this year   
![](images/443cb9ceb822e36fd4a35da23026f029e7fc10bb689b734a95bc54a3eeb2383a.jpg)

<details>
<summary>bar</summary>

| Sector             | Returns (USD) |
| ------------------ | ------------- |
| Semiconductors     | 44.9%         |
| Tech Hardware      | 29.8%         |
| Energy             | 28.7%         |
| Materials          | 10.4%         |
| Industrials        | 10.3%         |
| Media & Ent.       | 6.6%          |
| Cons. Staples      | 5.8%          |
| Real Estate        | 5.1%          |
| Telecom            | 5.0%          |
| Utilities          | 4.7%          |
| Banks              | 0.4%          |
| Insurance          | -1.3%         |
| Cons. Discretionary| -3.0%         |
| Div Financials     | -6.0%         |
| Health Care        | -6.2%         |
| Software           | -16.0%        |
</details>

Source : BofA Global Quantitative Strategy, MSCI   
BofA GLOBAL RESEARCH

Table 1: Global Region Country Sector Performance: Last week

Best performing sector last week was Energy

<table><tr><td></td><td>Energy</td><td>Materials</td><td>Industrials</td><td>Cons. Discretionary</td><td>Cons. Staples</td><td>Health Care</td><td>Banks</td><td>Div Financials</td><td>Insurance</td><td>Software</td><td>Tech Hardware</td><td>Semiconductors</td><td>Telecom</td><td>Media &amp; Ent.</td><td>Utilities</td><td>Real Estate</td><td>Country</td></tr><tr><td>Canada</td><td>4.6%</td><td>-4.7%</td><td>-3.0%</td><td>-4.3%</td><td>-1.3%</td><td>n/a</td><td>0.3%</td><td>-3.1%</td><td>-1.2%</td><td>-1.0%</td><td>-4.2%</td><td>n/a</td><td>-4.1%</td><td>n/a</td><td>-1.1%</td><td>-3.6%</td><td>-1.1%</td></tr><tr><td>USA</td><td>6.6%</td><td>-2.3%</td><td>-1.0%</td><td>-3.1%</td><td>1.3%</td><td>1.1%</td><td>-2.3%</td><td>0.2%</td><td>1.1%</td><td>0.8%</td><td>3.1%</td><td>0.5%</td><td>-2.8%</td><td>-0.7%</td><td>-2.2%</td><td>-2.7%</td><td>0.2%</td></tr><tr><td>Belgium</td><td>n/a</td><td>n/a</td><td>n/a</td><td>-7.1%</td><td>1.0%</td><td>1.0%</td><td>-4.0%</td><td>-4.2%</td><td>0.5%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>-6.3%</td><td>n/a</td><td>-0.1%</td></tr><tr><td>Finland</td><td>3.1%</td><td>-2.3%</td><td>-1.3%</td><td>n/a</td><td>-2.7%</td><td>-2.0%</td><td>-2.2%</td><td>n/a</td><td>0.0%</td><td>n/a</td><td>7.4%</td><td>n/a</td><td>-0.3%</td><td>n/a</td><td>-2.6%</td><td>n/a</td><td>0.9%</td></tr><tr><td>France</td><td>2.4%</td><td>-0.7%</td><td>-5.4%</td><td>-4.6%</td><td>-3.1%</td><td>-0.4%</td><td>-3.9%</td><td>-1.2%</td><td>-5.7%</td><td>-2.2%</td><td>n/a</td><td>6.4%</td><td>0.9%</td><td>-6.3%</td><td>-4.1%</td><td>-5.6%</td><td>-3.2%</td></tr><tr><td>Germany</td><td>n/a</td><td>-2.3%</td><td>-4.8%</td><td>-1.7%</td><td>-2.1%</td><td>-1.2%</td><td>1.6%</td><td>-1.8%</td><td>-2.2%</td><td>-2.7%</td><td>n/a</td><td>4.4%</td><td>-0.2%</td><td>0.4%</td><td>-4.2%</td><td>-4.1%</td><td>-2.5%</td></tr><tr><td>Italy</td><td>2.3%</td><td>-7.5%</td><td>-3.3%</td><td>-5.2%</td><td>-5.1%</td><td>1.7%</td><td>-1.3%</td><td>-0.1%</td><td>-1.9%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>-0.1%</td><td>n/a</td><td>-3.3%</td><td>n/a</td><td>-2.0%</td></tr><tr><td>Netherlands</td><td>n/a</td><td>-3.3%</td><td>-4.4%</td><td>-5.8%</td><td>-1.5%</td><td>-6.7%</td><td>-0.1%</td><td>-6.1%</td><td>0.9%</td><td>24.2%</td><td>n/a</td><td>-2.2%</td><td>-0.5%</td><td>2.5%</td><td>n/a</td><td>n/a</td><td>-1.4%</td></tr><tr><td>Norway</td><td>4.9%</td><td>0.4%</td><td>-6.5%</td><td>n/a</td><td>0.8%</td><td>n/a</td><td>-0.9%</td><td>n/a</td><td>-0.4%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>2.6%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>0.9%</td></tr><tr><td>Spain</td><td>1.1%</td><td>n/a</td><td>-4.2%</td><td>-4.1%</td><td>n/a</td><td>0.4%</td><td>-2.6%</td><td>n/a</td><td>-0.4%</td><td>-3.0%</td><td>n/a</td><td>n/a</td><td>-1.0%</td><td>n/a</td><td>-2.3%</td><td>n/a</td><td>-2.6%</td></tr><tr><td>Sweden</td><td>n/a</td><td>-3.1%</td><td>-5.4%</td><td>-3.0%</td><td>-1.9%</td><td>-1.0%</td><td>-2.7%</td><td>-3.7%</td><td>n/a</td><td>n/a</td><td>2.5%</td><td>n/a</td><td>-1.4%</td><td>4.6%</td><td>n/a</td><td>-3.8%</td><td>-3.1%</td></tr><tr><td>Switzerland</td><td>n/a</td><td>-4.0%</td><td>-1.5%</td><td>-3.1%</td><td>-0.7%</td><td>0.5%</td><td>1.9%</td><td>1.1%</td><td>0.5%</td><td>n/a</td><td>-4.4%</td><td>n/a</td><td>-0.2%</td><td>n/a</td><td>-2.1%</td><td>-2.1%</td><td>-0.4%</td></tr><tr><td>UK</td><td>0.9%</td><td>-1.9%</td><td>-4.9%</td><td>0.5%</td><td>0.8%</td><td>-0.4%</td><td>-3.3%</td><td>-6.7%</td><td>-0.6%</td><td>-3.1%</td><td>-3.4%</td><td>n/a</td><td>-8.0%</td><td>-5.6%</td><td>-9.5%</td><td>-6.0%</td><td>-2.3%</td></tr><tr><td>Australia</td><td>2.9%</td><td>1.7%</td><td>-1.4%</td><td>0.5%</td><td>-3.9%</td><td>-12.9%</td><td>-7.8%</td><td>-0.3%</td><td>3.5%</td><td>-7.8%</td><td>n/a</td><td>n/a</td><td>0.1%</td><td>-5.5%</td><td>0.3%</td><td>1.1%</td><td>-2.8%</td></tr><tr><td>Hong Kong</td><td>n/a</td><td>n/a</td><td>-1.3%</td><td>-0.5%</td><td>-4.0%</td><td>n/a</td><td>1.5%</td><td>-2.4%</td><td>1.1%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>0.6%</td><td>n/a</td><td>1.1%</td><td>0.2%</td><td>-0.2%</td></tr><tr><td>Japan</td><td>4.4%</td><td>-5.0%</td><td>-1.0%</td><td>2.7%</td><td>0.6%</td><td>-0.3%</td><td>2.3%</td><td>3.1%</td><td>6.6%</td><td>-5.4%</td><td>-2.2%</td><td>-7.7%</td><td>-2.9%</td><td>-7.5%</td><td>-1.6%</td><td>-7.4%</td><td>-0.8%</td></tr><tr><td>Singapore</td><td>n/a</td><td>n/a</td><td>-2.9%</td><td>1.7%</td><td>1.2%</td><td>n/a</td><td>2.1%</td><td>0.1%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>1.8%</td><td>n/a</td><td>-4.4%</td><td>-2.4%</td><td>0.8%</td></tr><tr><td>China</td><td>-0.1%</td><td>-7.7%</td><td>-0.8%</td><td>-3.1%</td><td>-2.7%</td><td>-4.8%</td><td>0.2%</td><td>-3.1%</td><td>-4.3%</td><td>-7.8%</td><td>-0.2%</td><td>0.8%</td><td>-0.5%</td><td>-3.8%</td><td>0.6%</td><td>0.0%</td><td>-2.7%</td></tr><tr><td>India</td><td>-6.3%</td><td>-1.4%</td><td>-5.1%</td><td>-5.9%</td><td>-1.9%</td><td>0.1%</td><td>-3.5%</td><td>-6.1%</td><td>-1.9%</td><td>-7.0%</td><td>n/a</td><td>-7.9%</td><td>3.1%</td><td>-6.6%</td><td>-5.3%</td><td>-9.3%</td><td>-4.1%</td></tr><tr><td>Korea</td><td>-8.7%</td><td>-13.5%</td><td>-9.9%</td><td>13.1%</td><td>-3.9%</td><td>-4.5%</td><td>-6.2%</td><td>-10.3%</td><td>4.0%</td><td>5.5%</td><td>-1.5%</td><td>5.4%</td><td>6.0%</td><td>-5.7%</td><td>-13.8%</td><td>n/a</td><td>-1.0%</td></tr><tr><td>Taiwan</td><td>n/a</td><td>-4.5%</td><td>-10.3%</td><td>-4.4%</td><td>1.5%</td><td>6.6%</td><td>-2.2%</td><td>-4.1%</td><td>-2.6%</td><td>n/a</td><td>-1.4%</td><td>n/a</td><td>1.5%</td><td>-2.4%</td><td>n/a</td><td>n/a</td><td>-1.9%</td></tr><tr><td>Brazil</td><td>-2.3%</td><td>-2.2%</td><td>-10.6%</td><td>-5.8%</td><td>-9.2%</td><td>-12.1%</td><td>-8.8%</td><td>-9.9%</td><td>-5.9%</td><td>-14.5%</td><td>n/a</td><td>n/a</td><td>-9.6%</td><td>n/a</td><td>-10.0%</td><td>n/a</td><td>-7.2%</td></tr><tr><td>Mexico</td><td>n/a</td><td>-3.9%</td><td>-4.0%</td><td>n/a</td><td>-2.2%</td><td>n/a</td><td>-5.2%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>-1.9%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>-3.3%</td></tr><tr><td>South Africa</td><td>n/a</td><td>-9.5%</td><td>-1.8%</td><td>-4.2%</td><td>-1.0%</td><td>n/a</td><td>-2.3%</td><td>-2.8%</td><td>-3.5%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>-1.3%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>-5.5%</td></tr><tr><td>Global Sector</td><td>4.2%</td><td>-3.0%</td><td>-2.4%</td><td>-2.4%</td><td>0.4%</td><td>0.5%</td><td>-2.2%</td><td>-0.5%</td><td>0.2%</td><td>0.3%</td><td>2.0%</td><td>0.1%</td><td>-1.9%</td><td>-1.0%</td><td>-3.0%</td><td>-2.9%</td><td>-0.6%</td></tr><tr><td>Europe Sector</td><td>1.6%</td><td>-2.0%</td><td>-4.4%</td><td>-3.3%</td><td>-0.5%</td><td>0.1%</td><td>-2.5%</td><td>-2.4%</td><td>-1.3%</td><td>1.0%</td><td>3.0%</td><td>-1.0%</td><td>-1.4%</td><td>0.8%</td><td>-4.0%</td><td>-4.6%</td><td>-2.0%</td></tr><tr><td>APxJ Sector</td><td>-2.9%</td><td>-2.2%</td><td>-5.7%</td><td>-1.4%</td><td>-2.4%</td><td>-4.8%</td><td>-3.2%</td><td>-3.7%</td><td>-0.8%</td><td>-6.9%</td><td>-1.3%</td><td>-0.2%</td><td>1.9%</td><td>-3.9%</td><td>-2.1%</td><td>-0.6%</td><td>-2.1%</td></tr><tr><td>GEM Sector</td><td>-3.0%</td><td>-5.6%</td><td>-6.7%</td><td>-1.8%</td><td>-2.4%</td><td>-2.9%</td><td>-2.9%</td><td>-5.9%</td><td>-2.8%</td><td>-6.6%</td><td>-1.3%</td><td>-0.2%</td><td>0.2%</td><td>-3.9%</td><td>-4.8%</td><td>-3.5%</td><td>-2.5%</td></tr></table>

Source : BofA Global Quantitative Strategy, MSCI

BofA GLOBAL RESEARCH

# Market Breadth

Chart 8: MSCI AC World Market Cap vs. Equal weighted index performance - last week/MTD/YTD   
Last week, ACWI index returned -0.6%, while Equal Weighted index returned -2.2%   
![](images/45b725da7ac6dc0d137e095bb306be467637259b846de0ab85a97b554f74e6fc.jpg)

<details>
<summary>bar</summary>

| Period | ACWI Index (%) | ACWI Equal W

[中间内容因长度限制已省略]

ch information is distributed simultaneously to internal and client websites and other portals by BofA and is not publicly-available material. Any unauthorized use or disclosure is prohibited. Receipt and review of this information constitutes your agreement not to redistribute, retransmit, or disclose to others the contents, opinions, conclusion, or information contained herein (including any investment recommendations, estimates or price targets) without first obtaining express permission from an authorized officer of BofA.

Materials prepared by BofA Global Research personnel are based on public information. Facts and views presented in this material have not been reviewed by, and may not reflect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
