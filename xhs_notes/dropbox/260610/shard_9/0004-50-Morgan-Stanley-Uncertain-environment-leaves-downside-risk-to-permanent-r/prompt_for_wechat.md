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
## Staffers | Europe

# Uncertain environment leaves downside risk to permanent recruitment

Uncertain backdrop and labour market data point to risk of further deterioration of perm, a drag on top-line growth, gross margin and operating leverage across the space. Prefer Randstad (EW) vs Adecco (UW) in this context for its lower leverage and limited dilution risk, and Hays (EW) vs Page Group (UW).

Why are we writing now? Despite the recent improvement in organic growth across the staffing space, mainly driven by better temporary staffing, we reiterate our cautious stance on the sub-sector. The macroeconomic and geopolitical environment has become more uncertain and could take a toll on the recruitment/ staffing market, something we think has not yet been fully reflected in consensus expectations. Concerns over the AI risk in the mid term also remain and could continue to weigh on valuation, together with short-term macro headwinds.

Risk to perm limits the upside. The lack of positive share-price reaction to recent organic growth beats across the space suggests investors are looking for gross margin recovery and better operating leverage to turn more positive. However, we believe the macro/geopolitical backdrop and recent labour market data point to a risk of further deterioration of perm recruitment, which would in turn continue to put pressure on staffers' gross margin and operating profit. We therefore see limited positive catalysts for staffing names to re-rate over the coming earnings season.

Re-shuffling ratings. We update our order of preference within our staffing coverage. Within generalist staffing, we shift our preference to Randstad (EW) over Adecco (UW) on larger downside risk to expectations for the latter, combined with elevated leverage and risk of potential shareholder dilution from scrip dividend. We also neutralise our rating on Hays to EW and reiterate our UW on Page Group, which has the largest exposure to perm recruitment and higher risk of additional dividend cuts, in our view.

MS & CO. INTERNATIONAL PLC+

## Remi Grenu

Equity Analyst

Remi.Grenu@morganstanley.com +44 20 7425-0552

## Annelies Vermeulen

Equity Analyst

Annelies.Vermeulen@morganstanley.com +44 20 7425-4367

## Zachariah Al-Qaryooti

Research Associate

Zach.Al-Qaryooti@morganstanley.com +44 20 7425-2400

BUSINESS SERVICES

<table><tr><td colspan="2">Europe</td></tr><tr><td>Industry View</td><td>Attractive</td></tr></table>

WHAT'S CHANGED

<table><tr><td>Adecco Group (ADEN.S) Rating</td><td>From Equal-weight</td><td>To Underweight</td></tr><tr><td>Price Target</td><td>SFr 20.50</td><td>SFr 15.00</td></tr><tr><td>Randstad NV (RAND.AS) Rating</td><td>From Underweight</td><td>To Equal-weight</td></tr><tr><td>Price Target</td><td>€26.00</td><td>€25.50</td></tr><tr><td>Page Group PLC (PAGE.L) Price Target</td><td>From 195p</td><td>To 110p</td></tr><tr><td>Hays PLC (HAYS.L) Rating</td><td>From Underweight</td><td>To Equal-weight</td></tr><tr><td>Price Target</td><td>44p</td><td>35p</td></tr></table>

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Investment case in charts

Exhibit 1: Staffers' organic growth has recovered, mainly driven by temp...  
![](images/e32ca2c9ac9e9292def76b8b0ab4ea64c3327d354196dde9509c0ec242d8cfe0.jpg)

<details>
<summary>line chart</summary>

| Quarter | Adecco | Randstad | Manpower* |
|---------|--------|----------|-----------|
| 1Q22    | 5.0%   | 15.0%    | 6.0%      |
| 2Q22    | 4.0%   | 10.0%    | 5.0%      |
| 3Q22    | 6.0%   | 8.0%     | 4.0%      |
| 4Q22    | 5.0%   | 5.0%     | 3.0%      |
| 1Q23    | 3.0%   | -5.0%    | -2.0%     |
| 2Q23    | 4.0%   | -7.0%    | -3.0%     |
| 3Q23    | 3.0%   | -8.0%    | -4.0%     |
| 4Q23    | 2.0%   | -9.0%    | -5.0%     |
| 1Q24    | 1.0%   | -8.0%    | -6.0%     |
| 2Q24    | -1.0%  | -7.0%    | -5.0%     |
| 3Q24    | -3.0%  | -6.0%    | -4.0%     |
| 4Q24    | -5.0%  | -5.0%    | -3.0%     |
| 1Q25    | -4.0%  | -4.0%    | -2.0%     |
| 2Q25    | -2.0%  | -3.0%    | -1.0%     |
| 3Q25    | 1.0%   | -2.0%    | 0.0%      |
| 4Q25    | 3.0%   | -1.0%    | 1.0%      |
| 1Q26    | 4.0%   | 0.0%     | 2.0%      |
| 2Q26e   | 5.0%   | 1.0%     | 3.0%      |
| 3Q26e   | 4.0%   | 2.0%     | 4.0%      |
| 4Q26e   | 3.0%   | 3.0%     | 5.0%      |
</details>

Source: Company data, MS estimates

Exhibit 3: Indeed job postings have continued to deteriorate...

<table><tr><td>Indeed Job Postings data</td><td>May-25</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td></tr><tr><td>France</td><td>120.7</td><td>117.6</td><td>114.1</td><td>111.7</td><td>110.5</td><td>106.8</td><td>105.6</td><td>104.2</td><td>104.4</td><td>108.8</td><td>104.7</td><td>97.0</td><td>96.7</td></tr><tr><td>Germany</td><td>122.4</td><td>120.2</td><td>115.9</td><td>114.6</td><td>116.1</td><td>116.1</td><td>115.6</td><td>114.7</td><td>114.3</td><td>113.5</td><td>111.8</td><td>109.3</td><td>110.4</td></tr><tr><td>UK</td><td>78.0</td><td>77.5</td><td>77.1</td><td>75.8</td><td>75.1</td><td>75.3</td><td>76.3</td><td>77.1</td><td>75.2</td><td>76.6</td><td>76.3</td><td>71.2</td><td>70.3</td></tr><tr><td>US</td><td>105.9</td><td>105.2</td><td>104.3</td><td>104.8</td><td>102.8</td><td>101.0</td><td>101.3</td><td>102.9</td><td>103.3</td><td>104.6</td><td>104.1</td><td>102.7</td><td>102.0</td></tr><tr><td>Australia</td><td>148.5</td><td>150.6</td><td>151.0</td><td>148.6</td><td>148.9</td><td>149.7</td><td>148.8</td><td>146.9</td><td>153.1</td><td>163.0</td><td>161.9</td><td>151.4</td><td>152.7</td></tr></table>

Source: Indeed, MS

Exhibit 5: Staffing exposure to permanent recruitment (% of gross profit)  
![](images/ff4c7767ce13173b83bfdbc63217baad851fa7fa138968a2501a07de8a7e8327.jpg)

<details>
<summary>bar chart</summary>

| Category | Value (%) |
|---|---|
| Adecco | 15-17 |
| Randstad | 16 |
| Hays | 38 |
| Page Group | 72 |
</details>

Source: Company data, MS

Exhibit 2: ... but gross margins remain under pressure  
![](images/30cbf866dbc6a9c6e4f08dc8dc8b0e6a1811debfabf7ccf71ff981fddcbff2a2.jpg)

<details>
<summary>bar chart</summary>

| Quarter | Adecco (%) | Randstad (%) |
| :--- | :--- | :--- |
| 1Q22 | 21.1 | 20.5 |
| 2Q22 | 21.1 | 21.1 |
| 3Q22 | 20.9 | 20.9 |
| 4Q22 | 20.9 | 20.8 |
| 1Q23 | 21.3 | 20.9 |
| 2Q23 | 20.7 | 20.7 |
| 3Q23 | 20.8 | 20.6 |
| 4Q23 | 20.2 | 20.7 |
| 1Q24 | 19.8 | 20.2 |
| 2Q24 | 19.4 | 19.8 |
| 3Q24 | 19.4 | 19.5 |
| 4Q24 | 19.3 | 18.8 |
| 1Q25 | 19.5 | 19.4 |
| 2Q25 | 18.9 | 18.9 |
| 3Q25 | 19.2 | 18.4 |
| 4Q25 | 19.2 | 18.4 |
| 1Q26 | 18.8 | 18.5 |
| 2Q26e | 18.6 | 18.3 |
| 3Q26e | 18.9 | 18.4 |
| 4Q26e | 19.0 | 18.3 |
</details>

Source: Company data, MS estimates

Exhibit 4: .... and so have job vacancies in key recruitment markets  
![](images/c1d0693347e75799c00dc2a073cd207f0907c5f5d624485e81819d346ce7ae9e.jpg)

<details>
<summary>line chart</summary>

| Date     | France | Germany | UK   | US   |
|----------|--------|---------|------|------|
| 12/2018  | 100    | 100     | 100  | 100  |
| 04/2019  | 105    | 95      | 98   | 97   |
| 08/2019  | 102    | 92      | 95   | 94   |
| 12/2019  | 98     | 88      | 92   | 90   |
| 04/2020  | 60     | 75      | 65   | 70   |
| 08/2020  | 75     | 78      | 70   | 85   |
| 12/2020  | 85     | 80      | 75   | 95   |
| 04/2021  | 105    | 85      | 95   | 135  |
| 08/2021  | 120    | 95      | 115  | 140  |
| 12/2021  | 125    | 100     | 125  | 135  |
| 04/2022  | 128    | 105     | 130  | 130  |
| 08/2022  | 130    | 108     | 135  | 135  |
| 12/2022  | 125    | 105     | 130  | 130  |
| 04/2023  | 120    | 100     | 125  | 125  |
| 08/2023  | 115    | 95      | 120  | 120  |
| 12/2023  | 110    | 90      | 115  | 115  |
| 04/2024  | 105    | 85      | 110  | 110  |
| 08/2024  | 100    | 80      | 105  | 105  |
| 12/2024  | 95     | 75      | 100  | 100  |
| 04/2025  | 90     | 78      | 95   | 95   |
| 08/2025  | 85     | 75      | 90   | 90   |
| 12/2025  | 88     | 78      | 88   | 88   |
| 04/2026  | 90     | 80      | 85   | 90   |
</details>

Source: ONS, BLS, INSEE, Bundesbank

Exhibit 6: Adecco's financial leverage compared to Randstad's  
![](images/f07dbc8183a976e255c89fe77c98d6afa9eab84a657af54969a767d0793231f0.jpg)

<details>
<summary>line chart</summary>

| Fiscal Year | Adecco | Randstad |
|-------------|--------|----------|
| FY15        | 0.8x   | 0.2x     |
| FY16        | 0.7x   | 0.8x     |
| FY17        | 0.8x   | 1.4x     |
| FY18        | 1.0x   | 1.2x     |
| FY19        | 0.3x   | 0.6x     |
| FY20        | 0.4x   | -0.5x    |
| FY21        | 0.1x   | -0.2x    |
| FY22        | 2.5x   | 0.2x     |
| FY23        | 2.5x   | 0.3x     |
| FY24        | 2.8x   | 1.5x     |
| FY25        | 2.7x   | 1.3x     |
| FY26e       | 2.5x   | 1.5x     |
| FY27e       | 2.3x   | 1.3x     |
| FY28e       | 2.0x   | 1.0x     |
| FY29e       | 1.5x   | 0.6x     |
</details>

Source: Company data, MS estimates

Exhibit 7: Adecco EV/EBIT valuation relative to Randstad  
![](images/10d8f376d6ea52681e13143653632792d4db9a2d9604f36f278a60385b17e34c.jpg)

<details>
<summary>line chart</summary>

| Date     | Adecco/Randstad | Average | + 1σ  | 1σ   |
|----------|-----------------|---------|-------|------|
| 06/2006  | ~0%             | ~-10%   | ~0%   | ~-20%|
| 06/2007  | ~35%            | ~-10%   | ~0%   | ~-20%|
| 06/2008  | ~-30%           | ~-10%   | ~0%   | ~-20%|
| 06/2009  | ~25%            | ~-10%   | ~0%   | ~-20%|
| 06/2010  | ~-45%           | ~-10%   | ~0%   | ~-20%|
| 06/2011  | ~-20%           | ~-10%   | ~0%   | ~-20%|
| 06/2012  | ~-15%           | ~-10%   | ~0%   | ~-20%|
| 06/2013  | ~5%             | ~-10%   | ~0%   | ~-20%|
| 06/2014  | ~15%            | ~-10%   | ~0%   | ~-20%|
| 06/2015  | ~25%            | ~-10%   | ~0%   | ~-20%|
| 06/2016  | ~-15%           | ~-10%   | ~0%   | ~-20%|
| 06/2017  | ~5%             | ~-10%   | ~0%   | ~-20%|
| 06/2018  | ~-15%           | ~-10%   | ~0%   | ~-20%|
| 06/2019  | ~-15%           | ~-10%   | ~0%   | ~-20%|
| 06/2020  | ~15%            | ~-10%   | ~0%   | ~-20%|
| 06/2021  | ~-35%           | ~-10%   | ~0%   | ~-20%|
| 06/2022  | ~5%             | ~-10%   | ~0%   | ~-20%|
| 06/2023  | ~25%            | ~-10%   | ~0%   | ~-20%|
| 06/2024  | ~-25%           | ~-10%   | ~0%   | ~-20%|
| 06/2025  | ~-15%           | ~-10%   | ~0%   | ~-20%|
</details>

Source: Datastream

Exhibit 8: Staffing coverage FCF yield valuation  
![](images/45f2a160766a6484b569f6f3aef6ad2823f79c9b80e79231ebb31b552b4030df.jpg)

<details>
<summary>bar chart</summary>

| Category | Value (%) |
|---|---|
| Page Group | 1.8 |
| Hays | 3.9 |
| Randstad | 9.1 |
| Adecco | 9.5 |
</details>

Source: MS estimates

## Business services order of preference

Exhibit 9: Business services: order of preference

<table><tr><td rowspan="2"></td><td rowspan="2">Company</td><td rowspan="2">Market cap (bn)</td><td rowspan="2">Share Price</td><td rowspan="2">MS PT</td><td rowspan="2">Upside to Price Target</td><td colspan="5">Valuation (CY 2026)</td><td colspan="4">Share price performance</td></tr><tr><td>P/E</td><td>EV / EBITDA</td><td>Div. Yield</td><td>Net Debt / EBITDA</td><td>FCF Yield</td><td>-1M</td><td>-3M</td><td>-6M</td><td>-12M</td></tr><tr><td rowspan="11">Overweight</td><td><img src="images/ec7e5c19f63c50cf20d41cdb205231514a973268653888ea11648841e80dd588.jpg"/></td><td>£24.1</td><td>2,620p</td><td>4,100p</td><td>56.5%</td><td>17.8x</td><td>11.4x</td><td>2.2%</td><td>1.7x</td><td>4.5%</td><td>-2.2%</td><td>-4.9%</td><td>-21.2%</td><td>-31.2%</td></tr><tr><td><img src="images/7a085daf2f87f92d0d5225ba4bc940c7f398bb7496d4723806199b0b48a7f857.jpg"/></td><td>€11.3</td><td>€25.6</td><td>€35.0</td><td>36.6%</td><td>16.4x</td><td>9.9x</td><td>4.0%</td><td>1.6x</td><td>6.6%</td><td>-3.3%</td><td>-11.4%</td><td>-4.0%</td><td>-14.6%</td></tr><tr><td><img src="images/f60e723d372df3ac38dc140e9cd2db1305ac67a0094a382695ab343074c3547d.jpg"/></td><td>€11.4</td><td>€11.0</td><td>€18.5</td><td>68.5%</td><td>19.4x</td><td>8.6x</td><td>0.6%</td><td>2.7x</td><td>1.9%</td><td>0.8%</td><td>20.9%</td><td>-25.1%</td><td>-</td></tr><tr><td>[4XD1]</td><td>£9.5</td><td>7,020p</td><td>8,250p</td><td>17.5%</td><td>29.2x</td><td>19.9x</td><td>0.9%</td><td>0.8x</td><td>3.3%</td><td>0.6%</td><td>31.0%</td><td>28.0%</td><td>51.0%</td></tr><tr><td>Rentokil Initial</td><td>£11.2</td><td>442p</td><td>570p</td><td>28.8%</td><td>20.4x</td><td>9.7x</td><td>2.1%</td><td>1.8x</td><td>6.3%</td><td>-10.4%</td><td>-6.1%</td><td>4.0%</td><td>26.4%</td></tr><tr><td>[S|Z6ZZ]</td><td>€8.2</td><td>€48.3</td><td>€53.0</td><td>9.6%</td><td>14.8x</td><td>9.5x</td><td>2.7%</td><td>1.8x</td><td>7.7%</td><td>-3.1%</td><td>-4.2%</td><td>2.4%</td><td>7.8%</td></tr><tr><td><img src="images/5118595ea0415c204ebf66bd5c7933941da13a28ce1d27a511478b0aa2daa29e.jpg"/></td><td>£3.0</td><td>649p</td><td>790p</td><td>21.7%</td><td>15.7x</td><td>9.4x</td><td>3.8%</td><td>1.0x</td><td>5.5%</td><td>6.9%</td><td>-1.7%</td><td>4.1%</td><td>13.9%</td></tr><tr><td><img src="images/7536ef9f8a455f1a2a06ec49b16f2b42335a7202cac32e82340a59649d30734f.jpg"/></td><td>$33.9</td><td>$79.4</td><td>$85.0</td><td>7.1%</td><td>19.1x</td><td>8.4x</td><td>1.4%</td><td>1.6x</td><td>12.4%</td><td>5.9%</td><td>5.8%</td><td>-</td><td>-</td></tr><tr><td><img src="images/714a6e40f6375d8431852b8d32f0d9110c7702bd183dac0c26a7c6e0fc923e2a.jpg"/></td><td>€6.7</td><td>€25.8</td><td>€31.5</td><td>21.9%</td><td>12.8x</td><td>5.2x</td><td>2.0%</td><td>1.7x</td><td>6.3%</td><td>-3.9%</td><td>4.6%</td><td>8.4%</td><td>10.0%</td></tr><tr><td><img src="images/9796070055e065758512d7ce0f5225d1957af84d0b185c6a01988e8e26e69a04.jpg"/></td><td>DKK42.6</td><td>DKK252</td><td>DKK300</td><td>18.9%</td><td>12.3x</td><td>8.6x</td><td>1.6%</td><td>2.4x</td><td>7.7%</td><td>0.4%</td><td>16.6%</td><td>21.7%</td><td>44.8%</td></tr><tr><td>FERGUSON</td><td>$45.3</td><td>$230</td><td>$290</td><td>26.3%</td><td>20.8x</td><td>13.6x</td><td>1.6%</td><td>0.7x</td><td>5.2%</td><td>-9.2%</td><td>-5.5%</td><td>-8.8%</td><td>8.7%</td></tr><tr><td rowspan="9">Equal-weight</td><td><img src="images/1613c122f36d0ea29acf209594d2a8613994754acf77f4920e99e734348e9f7b.jpg"/></td><td>SFr 16.7</td><td>SFr 89.5</td><td>SFr 102</td><td>14.0%</td><td>22.0x</td><td>10.8x</td><td>3.6%</td><td>1.9x</td><td>5.5%</td><td>4.7%</td><td>-4.0%</td><td>-1.2%</td><td>5.5%</td></tr><tr><td><img src="images/200e957829556c05ce3ec5e61ed647cca40351fd229dda786f4b864cd6ecb174.jpg"/></td><td>€12.0</td><td>€64.9</td><td>€67.5</td><td>4.0%</td><td>15.1x</td><td>8.8x</td><td>1.3%</td><td>1.9x</td><td>7.0%</td><td>10.5%</td><td>-1.1%</td><td>10.4%</td><td>14.0%</td></tr><tr><td><img src="images/7c702c49a87bc557f27264aaffdd468c29909bcd9f33a0555cde1324f307b520.jpg"/></td><td>€3.5</td><td>€59.2</td><td>€56.0</td><td>-5.5%</td><td>4.3x</td><td>3.5x</td><td>7.7%</td><td>1.7x</td><td>23.3%</td><td>-6.8%</td><td>1.9%</td><td>-1.4%</td><td>-34.6%</td></tr><tr><td><img src="images/ddf0a25699486402b3ff0f904889f86349ed8bd3a920c0ec42e633a50f8c4599.jpg"/> IMCD</td><td>€5.3</td><td>€88.9</td><td>€105</td><td>18.1%</td><td>15.5x</td><td>11.7x</td><td>2.1%</td><td>2.5x</td><td>7.4%</td><td>-11.2%</td><td>21.5%</td><td>16.1%</td><td>-23.9%</td></tr><tr><td><img src="images/ad4842cc334f90564da68f1f204cf873a8a95dd997de4cbf4903331a1de2cb0d.jpg"/></td><td>€2.5</td><td>€10.4</td><td>€12.0</td><td>15.4%</td><td>17.5x</td><td>8.7x</td><td>1.7%</td><td>3.2x</td><td>10.7%</td><td>-7.6%</td><td>33.8%</td><td>10.4%</td><td>-25.2%</td></tr><tr><td>Travis Perkins</td><td>£1.2</td><td>543p</td><td>685p</td><td>26.2%</td><td>19.4x</td><td>6.0x</td><td>1.9%</td><td>2.3x</td><td>-0.6%</td><td>2.6%</td><td>-13.0%</td><td>-13.1%</td><td>-11.7%</td></tr><tr><td><img src="images/796f2b1f72594af0ea29957ce6212a19a4c5343ce3f1f3b4eda3c8f490d21066.jpg"/></td><td>£8.0</td><td>2,470p</td><td>2,550p</td><td>3.2%</td><td>14.0x</td><td>8.7x</td><td>3.1%</td><td>1.8x</td><td>5.2%</td><td>1.0%</td><td>10.6%</td><td>14.8%</td><td>8.0%</td></tr><tr><td>randstad</td><td>€4.7</td><td>€27.4</td><td>€25.5</td><td>-6.8%</td><td>10.8x</td><td>6.2x</td><td>5.9%</td><td>1.6x</td><td>8.2%</td><td>8.8%</td><td>1.5%</td><td>-15.6%</td><td>-24.7%</td></tr><tr><td><img src="images/d7c9e8e0ddfebb7082ceceeec5631726945a123299c50f68d470196c4486ad82.jpg"/></td><td>£0.6</td><td>35p</td><td>35p</td><td>0.8%</td><td>24.4x</td><td>4.7x</td><td>1.6%</td><td>NM</td><td>1.5%</td><td>3.8%</td><td>-10.6%</td><td>-35.9%</td><td>-50.5%</td></tr><tr><td rowspan="4">Underweight</td><td>[BRENTAG]</td><td>€8.6</td><td>€56.8</td><td>€52.0</td><td>-8.5%</td><td>17.1x</td><td>8.9x</td><td>3.5%</td><td>2.3x</td><td>2.8%</td><td>-9.6%</td><td>20.1%</td><td>15.5%</td><td>-6.5%</td></tr><tr><td>THE ADECCO GROUP</td><td>SFr 2.7</td><td>SFr 16.6</td><td>SFr 15.0</td><td>-9.4%</td><td>8.3x</td><td>5.9x</td><td>5.9%</td><td>2.5x</td><td>9.5%</td><td>-6.7%</td><td>-21.4%</td><td>-24.6%</td><td>-26.1%</td></tr><tr><td>[SHC]</td><td>£0.4</td><td>123p</td><td>110p</td><td>-10.4%</td><td>31.5x</td><td>5.1x</td><td>4.2%</td><td>NM</td><td>2.2%</td><td>-7.3%</td><td>-19.2%</td><td>-48.0%</td><td>-54.6%</td></tr><tr><td>[SHC]</td><td>SEK89.4</td><td>SEK156</td><td>SEK125</td><td>-19.9%</td><td>12.5x</td><td>9.1x</td><td>4.4%</td><td>2.1x</td><td>6.9%</td><td>0.3%</td><td>-1.5%</td><td>8.1%</td><td>9.8%</td></tr></table>

Source: Thomson Reuters, MS estimates, Priced as at 5th June 2026

# Temporary staffing better, but not enough to drive upside to expectations

## Market focus on operating leverage rather than organic growth

While organic growth remains negative or relatively soft across the board (except at Adecco), it has gradually improved over the last few quarters (see Exhibit 10 and Exhibit 11). Th

[中间内容因长度限制已省略]

e DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Business Services

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/08/2026)</td></tr><tr><td colspan="3">Annelies Vermeulen</td></tr><tr><td>Azelis (AZE.BR)</td><td>E (09/10/2025)</td><td>€10.22</td></tr><tr><td>Brenntag SE (BNRGn.DE)</td><td>U (01/06/2026)</td><td>€54.84</td></tr><tr><td>Bunzl PLC (BNZL.L)</td><td>E (01/12/2024)</td><td>2,494p</td></tr><tr><td>Bureau Veritas SA (BVI.PA)</td><td>O (01/27/2025)</td><td>€25.32</td></tr><tr><td>DCC Plc (DCC.L)</td><td>++</td><td>5,975p</td></tr><tr><td>Diploma PLC (DPLM.L)</td><td>O (09/06/2023)</td><td>7,060p</td></tr><tr><td>Elis SA (ELIS.PA)</td><td>O (06/09/2020)</td><td>€25.80</td></tr><tr><td>Experian PLC (EXPN.L)</td><td>O (07/08/2022)</td><td>2,639p</td></tr><tr><td>Ferguson Enterprises Inc (FERG.L)</td><td>O (01/09/2025)</td><td>16,950p</td></tr><tr><td>Ferguson Enterprises Inc (FERG.N)</td><td>O (02/03/2025)</td><td>US$229.58</td></tr><tr><td>IMCD NV (IMCD.AS)</td><td>E (01/06/2026)</td><td>€87.20</td></tr><tr><td>Intertek Group PLC (ITRK.L)</td><td>++</td><td>5,570p</td></tr><tr><td>Rentokil Initial PLC (RTO.L)</td><td>O (01/06/2026)</td><td>445p</td></tr><tr><td>RS Group PLC (RS1R.L)</td><td>O (01/06/2026)</td><td>641p</td></tr><tr><td>SGS SA (SGSN.S)</td><td>E (01/06/2026)</td><td>SFr 89.60</td></tr><tr><td>Sunbelt Rentals Inc. (SUNB.L)</td><td>O (07/08/2022)</td><td>6,046p</td></tr><tr><td>Sunbelt Rentals Inc. (SUNB.N)</td><td>O (03/13/2026)</td><td>US$79.36</td></tr><tr><td>Travis Perkins PLC (TPK.L)</td><td>E (07/08/2022)</td><td>537p</td></tr><tr><td>Verisure PLC (VSURE.ST)</td><td>O (11/18/2025)</td><td>€10.87</td></tr><tr><td colspan="3">Remi Grenu</td></tr><tr><td>Adecco Group (ADEN.S)</td><td>U (06/09/2026)</td><td>SFr 16.58</td></tr><tr><td>Eurofins Scientific SE (EUFI.PA)</td><td>E (04/30/2025)</td><td>€64.88</td></tr><tr><td>Hays PLC (HAYS.L)</td><td>E (06/09/2026)</td><td>36p</td></tr><tr><td>ISS A/S (ISS.CO)</td><td>O (01/06/2026)</td><td>DKr 253.00</td></tr><tr><td>Page Group PLC (PAGE.L)</td><td>U (12/03/2025)</td><td>124p</td></tr><tr><td>Randstad NV (RAND.AS)</td><td>E (06/09/2026)</td><td>€26.84</td></tr><tr><td>Securitas AB (SECUb.ST)</td><td>U (10/25/2024)</td><td>SKr 155.40</td></tr><tr><td>SPIE (SPIE.PA)</td><td>O (04/08/2026)</td><td>€47.82</td></tr><tr><td>TP (TEPRF.PA)</td><td>E (03/24/2026)</td><td>€58.66</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
