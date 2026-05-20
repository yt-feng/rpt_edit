你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  ✅ 三大情景框架：DCF、P/ARR、EV/Sales
  ✅ 关键变量分析
  ✅ 估值逻辑、假设、终值占比等核心内容覆盖
  ✅ 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

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

<table><tr><td></td><td>Energy</td><td>Materials</td><td>Industrials</td><td>Cons. Discretionary</td><td>Cons. Staples</td><td>Health Care</td><td>Banks</td><td>Div Financials</td><td>Insurance</td><td>Software</td><td>Tech Hardware</td><td>Semiconductors</td><td>Telecom</td><td>Media &amp; Ent.</td><td>Utilities</td><td>Real Estate</td><td>Country</td></tr><tr><td>Canada</td><td>4.6%</td><td>-4.7%</td><td>-3.0%</td><td>-4.3%</td><td>-1.3%</td><td>n/a</td><td>0.3%</td><td>-3.1%</td><td>-1.2%</td><td>-1.0%</td><td>-4.2%</td><td>n/a</td><td>-4.1%</td><td>n/a</td><td>-1.1%</td><td>-3.6%</td><td>-1.1%</td></tr><tr><td>USA</td><td>6.6%</td><td>-2.3%</td><td>-1.0%</td><td>-3.1%</td><td>1.3%</td><td>1.1%</td><td>-2.3%</td><td>0.2%</td><td>1.1%</td><td>0.8%</td><td>3.1%</td><td>0.5%</td><td>-2.8%</td><td>-0.7%</td><td>-2.2%</td><td>-2.7%</td><td>0.2%</td></tr><tr><td>Belgium</td><td>n/a</td><td>n/a</td><td>n/a</td><td>-7.1%</td><td>1.0%</td><td>1.0%</td><td>-4.0%</td><td>-4.2%</td><td>0.5%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>-6.3%</td><td>n/a</td><td>-0.1%</td></tr><tr><td>Finland</td><td>3.1%</td><td>-2.3%</td><td>-1.3%</td><td>n/a</td><td>-2.7%</td><td>-2.0%</td><td>-2.2%</td><td>n/a</td><td>0.0%</td><td>n/a</td><td>7.4%</td><td>n/a</td><td>-0.3%</td><td>n/a</td><td>-2.6%</td><td>n/a</td><td>0.9%</td></tr><tr><td>France</td><td>2.4%</td><td>-0.7%</td><td>-5.4%</td><td>-4.6%</td><td>-3.1%</td><td>-0.4%</td><td>-3.9%</td><td>-1.2%</td><td>-5.7%</td><td>-2.2%</td><td>n/a</td><td>6.4%</td><td>0.9%</td><td>-6.3%</td><td>-4.1%</td><td>-5.6%</td><td>-3.2%</td></tr><tr><td>Germany</td><td>n/a</td><td>-2.3%</td><td>-4.8%</td><td>-1.7%</td><td>-2.1%</td><td>-1.2%</td><td>1.6%</td><td>-1.8%</td><td>-2.2%</td><td>-2.7%</td><td>n/a</td><td>4.4%</td><td>-0.2%</td><td>0.4%</td><td>-4.2%</td><td>-4.1%</td><td>-2.5%</td></tr><tr><td>Italy</td><td>2.3%</td><td>-7.5%</td><td>-3.3%</td><td>-5.2%</td><td>-5.1%</td><td>1.7%</td><td>-1.3%</td><td>-0.1%</td><td>-1.9%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>-0.1%</td><td>n/a</td><td>-3.3%</td><td>n/a</td><td>-2.0%</td></tr><tr><td>Netherlands</td><td>n/a</td><td>-3.3%</td><td>-4.4%</td><td>-5.8%</td><td>-1.5%</td><td>-6.7%</td><td>-0.1%</td><td>-6.1%</td><td>0.9%</td><td>24.2%</td><td>n/a</td><td>-2.2%</td><td>-0.5%</td><td>2.5%</td><td>n/a</td><td>n/a</td><td>-1.4%</td></tr><tr><td>Norway</td><td>4.9%</td><td>0.4%</td><td>-6.5%</td><td>n/a</td><td>0.8%</td><td>n/a</td><td>-0.9%</td><td>n/a</td><td>-0.4%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>2.6%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>0.9%</td></tr><tr><td>Spain</td><td>1.1%</td><td>n/a</td><td>-4.2%</td><td>-4.1%</td><td>n/a</td><td>0.4%</td><td>-2.6%</td><td>n/a</td><td>-0.4%</td><td>-3.0%</td><td>n/a</td><td>n/a</td><td>-1.0%</td><td>n/a</td><td>-2.3%</td><td>n/a</td><td>-2.6%</td></tr><tr><td>Sweden</td><td>n/a</td><td>-3.1%</td><td>-5.4%</td><td>-3.0%</td><td>-1.9%</td><td>-1.0%</td><td>-2.7%</td><td>-3.7%</td><td>n/a</td><td>n/a</td><td>2.5%</td><td>n/a</td><td>-1.4%</td><td>4.6%</td><td>n/a</td><td>-3.8%</td><td>-3.1%</td></tr><tr><td>Switzerland</td><td>n/a</td><td>-4.0%</td><td>-1.5%</td><td>-3.1%</td><td>-0.7%</td><td>0.5%</td><td>1.9%</td><td>1.1%</td><td>0.5%</td><td>n/a</td><td>-4.4%</td><td>n/a</td><td>-0.2%</td><td>n/a</td><td>-2.1%</td><td>-2.1%</td><td>-0.4%</td></tr><tr><td>UK</td><td>0.9%</td><td>-1.9%</td><td>-4.9%</td><td>0.5%</td><td>0.8%</td><td>-0.4%</td><td>-3.3%</td><td>-6.7%</td><td>-0.6%</td><td>-3.1%</td><td>-3.4%</td><td>n/a</td><td>-8.0%</td><td>-5.6%</td><td>-9.5%</td><td>-6.0%</td><td>-2.3%</td></tr><tr><td>Australia</td><td>2.9%</td><td>1.7%</td><td>-1.4%</td><td>0.5%</td><td>-3.9%</td><td>-12.9%</td><td>-7.8%</td><td>-0.3%</td><td>3.5%</td><td>-7.8%</td><td>n/a</td><td>n/a</td><td>0.1%</td><td>-5.5%</td><td>0.3%</td><td>1.1%</td><td>-2.8%</td></tr><tr><td>Hong Kong</td><td>n/a</td><td>n/a</td><td>-1.3%</td><td>-0.5%</td><td>-4.0%</td><td>n/a</td><td>1.5%</td><td>-2.4%</td><td>1.1%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>0.6%</td><td>n/a</td><td>1.1%</td><td>0.2%</td><td>-0.2%</td></tr><tr><td>Japan</td><td>4.4%</td><td>-5.0%</td><td>-1.0%</td><td>2.7%</td><td>0.6%</td><td>-0.3%</td><td>2.3%</td><td>3.1%</td><td>6.6%</td><td>-5.4%</td><td>-2.2%</td><td>-7.7%</td><td>-2.9%</td><td>-7.5%</td><td>-1.6%</td><td>-7.4%</td><td>-0.8%</td></tr><tr><td>Singapore</td><td>n/a</td><td>n/a</td><td>-2.9%</td><td>1.7%</td><td>1.2%</td><td>n/a</td><td>2.1%</td><td>0.1%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>1.8%</td><td>n/a</td><td>-4.4%</td><td>-2.4%</td><td>0.8%</td></tr><tr><td>China</td><td>-0.1%</td><td>-7.7%</td><td>-0.8%</td><td>-3.1%</td><td>-2.7%</td><td>-4.8%</td><td>0.2%</td><td>-3.1%</td><td>-4.3%</td><td>-7.8%</td><td>-0.2%</td><td>0.8%</td><td>-0.5%</td><td>-3.8%</td><td>0.6%</td><td>0.0%</td><td>-2.7%</td></tr><tr><td>India</td><td>-6.3%</td><td>-1.4%</td><td>-5.1%</td><td>-5.9%</td><td>-1.9%</td><td>0.1%</td><td>-3.5%</td><td>-6.1%</td><td>-1.9%</td><td>-7.0%</td><td>n/a</td><td>-

[中间内容因长度限制已省略]

lect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
