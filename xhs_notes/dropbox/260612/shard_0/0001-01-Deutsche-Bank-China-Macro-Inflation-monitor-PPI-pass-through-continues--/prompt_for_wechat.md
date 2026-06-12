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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`DB`。标题格式建议：`# DB：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份DB研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
Economics

China Macro

# Inflation monitor: PPI pass-through continues; CPI points to softer demand

China's PPI reflation continued as expected in May, while the underlying drivers are shifting. Headline PPI inflation rose to $3.9\%$ YoY, accelerating by 1.1ppt from April. On a MoM basis, PPI inflation moderated by 1.2ppt from the previous month but remained positive at $0.5\%$ MoM. With international oil prices broadly stable during the month, oil-related sectors saw a small MoM drop in prices. Meanwhile, the pass-through of earlier energy price increases to mid- and downstream sectors continued, with chemicals, ferrous metals and textiles all registering faster sequential price gains. In addition, AI-related demand continued to push up prices in non-ferrous metals such as tin and copper, electrical machinery, optical fibers, wires and cables, as well as computers.

Looking ahead, we maintain our forecast that PPI inflation will rise to around $5\%$ by year-end, averaging $3.3\%$ in 2026. While energy prices were the key driver in March and April, the focus ahead will be on the breadth of pass-through to mid- and downstream sectors, as well as the strength of AI-related demand.

Headline CPI inflation was unchanged at 1.2% YoY, but the breakdown points to softening domestic demand. Sequential inflation turned negative, falling 0.1% MoM after a 0.3% increase in April. Services, food, household goods and autos all saw MoM declines and slower YoY inflation, pointing to softer consumer demand. Energy prices declined 0.1% MoM, compared with a 5.7% rise in the previous month. Meanwhile, AI-related demand lifted prices of mobile phones and computers, which rose 1.6% and 1.1% MoM, respectively, while the arrival of summer also supported stronger clothing prices.

As the boost to goods consumption from the trade-in subsidies will likely diminish marginally, consumer demand is likely to remain soft. We therefore lower our full-year CPI inflation forecast to 1.5% from 1.6%, and now expect it to rise to 1.8% by year-end, compared with our previous forecast of 2.0%.

Date

10 June 2026

Deyun Ou

Economist

+852-2203-6166

Yi Xiong, Ph.D.

Chief Economist

+852-2203-6139

Figure 1: PPI reflation was in line with our forecast  
![](images/f1f920deed54ecbbf0f654cf3b9099779d53bcb4ad480032bd874385ea481c16.jpg)

<details>
<summary>line chart</summary>

| Date       | 2002 Dec | 2009 Dec | 2016 Sep | 2021 Jan | Consensus Fcst. |
|------------|----------|----------|----------|----------|-----------------|
| PPI % YoY  | -12      | -12      | -12      | -12      | -12             |
| 12 month   | -9       | -9       | -9       | -9       | -9              |
| 24 month   | -3       | -3       | -3       | -3       | -3              |
| 3 month     | 0        | 0        | 0        | 0        | 0               |
| 6 month     | 3        | 3        | 3        | 3        | 3               |
| 9 month     | 6        | 6        | 6        | 6        | 6               |
| 12 month    | 9        | 9        | 9        | 9        | 9               |
| 15 month    | 7        | 7        | 7        | 7        | 7               |
| 18 month    | 5        | 5        | 5        | 5        | 5               |
| 21 month    | 3        | 3        | 3        | 3        | 3               |
| 24 month    | 1        | 1        | 1        | 1        | 1               |
</details>

Source: DB, Wind

Figure 2: Pass-through of energy price increases continued  
![](images/387754dc9801c14206aa1256b549dadd9702aa9ef38154287b3b4c77abe678f5.jpg)

<details>
<summary>bar chart</summary>

| Category                  | April | May |
| ------------------------- | ----- | --- |
| Petroleum Extraction      | 18.0  | -   |
| Production & Supply of Gas | -     | -   |
| Ferrous Metal Mining      | -     | -   |
| Non-ferrous Metals Processing | -     | -   |
| Ferrous Metals Processing  | -     | -   |
| Rubber & Plastic Products  | -     | -   |
| Chemical Fibres           | -     | -   |
| Chemical Materials & Products | 8.0   | -   |
| Coal Mining               | -     | 3.0 |
| Production & Supply of Gas  | -     | -   |
</details>

Source: DB, Wind

Figure 3: CPI was unchanged at 1.2% YoY, while core CPI slowed to 1.1% YoY  
![](images/1143cd4ab75313c02e7e7cecfe2fe7c20666eb4170748013014648df07e34241.jpg)

<details>
<summary>line chart</summary>

| Year | Headline | Core |
|------|----------|------|
| '15  | 1.0      | 1.5  |
| '16  | 1.8      | 1.7  |
| '17  | 2.5      | 2.0  |
| '18  | 2.0      | 1.8  |
| '19  | 2.8      | 1.5  |
| '20  | 5.5      | 1.0  |
| '21  | -0.5     | 0.5  |
| '22  | 1.5      | 1.0  |
| '23  | 2.8      | 0.8  |
| '24  | -0.8     | 0.5  |
| '25  | 0.5      | 1.0  |
</details>

Source: DB, Wind

Figure 4: Energy price increases continued to support CPI inflation  
![](images/255c2f3806a0e03188d062fdf67bde8413fcb10ed63df478669decc7c9d455d6.jpg)

<details>
<summary>stacked bar chart</summary>

| Month | Pork (%) | Energy and fuels (%) | Transport & communication (%) | Education & health care (%) | Other food (%) | Rent, HH goods & services (%) | Travel (%) | CPI (%) |
|---|---|---|---|---|---|---|---|---|
| Jan-24 | -0.8 | 0.1 | -0.1 | 0.5 | -0.9 | 0.1 | 0.1 | -0.7 |
| Apr-24 | 0.1 | 0.1 | -0.3 | 0.7 | 0.3 | 0.1 | 0.1 | 0.3 |
| Jul-24 | 0.3 | 0.4 | -0.4 | 0.8 | 0.2 | 0.1 | 0.1 | 0.2 |
| Oct-24 | 0.2 | 0.3 | -0.3 | 0.6 | 0.3 | 0.1 | 0.1 | 0.2 |
| Jan-25 | 0.1 | 0.1 | -0.5 | 0.4 | 0.2 | 0.1 | 0.1 | 0.1 |
| Apr-25 | 0.1 | 0.1 | -0.3 | 0.3 | 0.2 | 0.1 | 0.1 | 0.1 |
| Jul-25 | -0.1 | -0.2 | -0.4 | 0.4 | -0.1 | 0.1 | 0.1 | -0.3 |
| Oct-25 | -0.2 | -0.3 | -0.5 | 0.5 | -0.2 | 0.1 | 0.1 | -0.2 |
| Jan-26 | -0.3 | -0.4 | -0.6 | 0.6 | -0.3 | 0.1 | 0.1 | 0.7 |
| Apr-26 | -0.3 | -0.4 | -0.6 | 0.6 | -0.3 | 0.1 | 0.1 | 1.2 |
The chart displays a stacked bar chart with categories including 'Pork', 'Energy and fuels', 'Transport & communication', 'Education & health care', 'Other food', 'Rent, HH goods & services', 'Travel', and 'CPI'. The values for each category are labeled on top of each bar.
</details>

Source: DB, Wind

Figure 5: Core inflation declined on a MoM basis  
![](images/7a8a80f0ad5d0b5acc75b44a7799d94cd14b25dd4053699cfda6fdef07b2ba65.jpg)

<details>
<summary>area chart</summary>

| Month | 2022-25 interval (%) | 2026 (%) |
|---|---|---|
| Feb | 0.38 | 0.51 |
| Mar | -0.64 | -0.71 |
| Apr | 0.19 | 0.21 |
| May | -0.18 | -0.11 |
| Jun | 0.08 | -0.05 |
| Jul | 0.48 | 0.10 |
| Aug | -0.21 | -0.03 |
| Sep | 0.05 | 0.01 |
| Oct | 0.20 | 0.01 |
| Nov | -0.31 | -0.06 |
| Dec | 0.19 | 0.03 |
</details>

Source: DB, Wind

Figure 6: Food inflation rebounded slightly but was still in negative territory  
![](images/8f00567f88ba04376cc7abf4f5cbcbc04b06fe6160f9b52491a0f80b916c1b34.jpg)

<details>
<summary>area chart</summary>

| Month | 2022-25 interval (%) | 2026 (%) |
|---|---|---|
| Feb | 1.8 | 1.0 |
| Mar | -1.3 | -2.8 |
| Apr | 0.9 | -1.4 |
| May | -0.2 | -0.5 |
| Jun | -1.7 | -0.3 |
| Jul | 3.0 | -0.1 |
| Aug | 3.4 | 0.5 |
| Sep | 1.8 | 0.3 |
| Oct | 0.3 | -0.2 |
| Nov | 0.5 | -2.8 |
| Dec | 0.9 | -0.6 |
</details>

Source: DB, Wind

Figure 7: We revise down the full-year CPI forecast to 1.5% from 1.6%  
![](images/7ec3a420b7229f7a9ae4a3b42ae3f53ed3e812de5232ac5b9057e26600ac0c90.jpg)

<details>
<summary>line chart</summary>

| Year | % YoY |
|------|-------|
| 2018 | ~2.5  |
| 2019 | ~2.0  |
| 2020 | ~5.5  |
| 2021 | ~-0.5 |
| 2022 | ~2.5  |
| 2023 | ~2.0  |
| 2024 | ~-0.5 |
| 2025 | ~0.5  |
| 2026 | ~1.5  |
| 2027 | ~3.0  |
</details>

Source: DB, Wind

Figure 8: PPI reflation emerged in mid- and downstream sectors  
![](images/bf64813992817fe75be2970e1ddd73178ac517105c113aa4c94058d98bcd2103.jpg)

<details>
<summary>line chart</summary>

| Year | Downstream | Upstream | Midstream |
|------|------------|----------|-----------|
| '20  | -          | 4.5      | -         |
| '21  | -          | 20.0     | 6.0       |
| '22  | 2.5        | 18.0     | 10.5      |
| '23  | -          | 1.0      | -         |
| '24  | -          | -        | -         |
| '25  | -          | 4.0      | -         |
| '26  | -          | 12.0     | 1.5       |
</details>

Source: DB, Wind

Figure 9: May inflation momentum

<table><tr><td>%, YoY</td><td>21avg</td><td>22avg</td><td>23avg</td><td>24avg</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td></tr><tr><td>Headline CPI</td><td>0.9</td><td>2.0</td><td>0.2</td><td>0.2</td><td>0.2</td><td>0.7</td><td>0.8</td><td>0.2</td><td>1.3</td><td>1.0</td><td>1.2</td><td>1.2</td></tr><tr><td>Core CPI</td><td>0.8</td><td>0.9</td><td>0.7</td><td>0.5</td><td>1.2</td><td>1.2</td><td>1.2</td><td>0.8</td><td>1.8</td><td>1.1</td><td>1.2</td><td>1.1</td></tr><tr><td>Food, Tobacco and Liquor</td><td>-0.3</td><td>2.5</td><td>0.3</td><td>-0.1</td><td>-1.6</td><td>0.3</td><td>0.8</td><td>-0.2</td><td>1.4</td><td>0.4</td><td>-1.6</td><td>-1.7</td></tr><tr><td>Clothing</td><td>0.3</td><td>0.5</td><td>1.0</td><td>1.4</td><td>1.7</td><td>1.9</td><td>1.7</td><td>1.9</td><td>1.9</td><td>1.6</td><td>1.5</td><td>1.4</td></tr><tr><td>Housing</td><td>0.8</td><td>0.7</td><td>0.0</td><td>0.1</td><td>0.1</td><td>0.0</td><td>-0.2</td><td>-0.1</td><td>-0.2</td><td>-0.2</td><td>-0.2</td><td>-0.2</td></tr><tr><td>Household Articles &amp; Services</td><td>0.4</td><td>1.2</td><td>0.1</td><td>0.5</td><td>1.9</td><td>2.1</td><td>2.2</td><td>2.6</td><td>2.8</td><td>1.5</td><td>1.4</td><td>1.8</td></tr><tr><td>Transportation and Communication</td><td>4.2</td><td>5.2</td><td>-2.3</td><td>-1.9</td><td>-1.5</td><td>-2.3</td><td>-2.6</td><td>-3.4</td><td>-0.7</td><td>0.9</td><td>4.6</td><td>5.4</td></tr><tr><td>Recreation, Education and Cultural Srvcs</td><td>1.9</td><td>1.8</td><td>2.0</td><td>1.5</td><td>0.9</td><td>0.8</td><td>0.9</td><td>0.0</td><td>2.0</td><td>1.1</td><td>1.3</td><td>1.3</td></tr><tr><td>Medicine, Medical Care, Personal Articles</td><td>0.4</td><td>0.6</td><td>1.1</td><td>1.3</td><td>1.4</td><td>1.6</td><td>1.8</td><td>1.7</td><td>1.9</td><td>1.9</td><td>2.2</td><td>2.1</td></tr><tr><td colspan="13"></td></tr><tr><td>PPI</td><td>8.1</td><td>4.2</td><td>-3.0</td><td>-2.2</td><td>-2.1</td><td>-2.2</td><td>-1.9</td><td>-1.4</td><td>-0.9</td><td>0.5</td><td>2.8</td><td>3.9</td></tr><tr><td>Mining &amp; Quarrying</td><td>34.8</td><td>18.7</td><td>-7.6</td><td>-2.8</td><td>-7.8</td><td>-6.1</td><td>-4.7</td><td>-8.1</td><td>-5.3</td><td>2.0</td><td>10.6</td><td>15.8</td></tr><tr><td>Raw Materials</td><td>15.9</td><td>10.7</td><td>-4.3</td><td>-1.6</td><td>-2.5</td><td>-2.9</td><td>-2.6</td><td>-2.0</td><td>-1.9</td><td>1.1</td><td>7.1</td><td>9.2</td></tr><tr><td>Manufacturing</td><td>6.7</td><td>1.6</td><td>-3.3</td><td>-2.9</td><td>-1.9</td><td>-1.9</td><td>-1.6</td><td>-0.4</td><td>0.3</td><td>0.9</td><td>1.5</td><td>2.3</td></tr></table>

Source: DB, Wind

## Appendix 1

## Analyst Certification

The views expressed in this report accurately reflect the personal views of the undersigned lead analyst(s). In addition, the undersigned lead analyst(s) has not and will not receive any compensation for providing a specific recommendation or view in this report. Deyun Ou, Yi Xiong, Ph.D..

## Important Disclosures

Prices are current as of the end of the previous trading session unless otherwise indicated and are sourced from local exchanges via Reuters, Bloomberg and other vendors. Other information is sourced from DB, subject companies, and other sources. For further information regarding disclosures relevant to DB, please visit our global disclosure look-up page on our website at

https://research.db.com/Research/Disclosures/FICCDisclosures. Aside from within this report, important risk and conflict disclosures can also be found at https://research.db.com/Research/Disclosures/Disclaimer. Investors are strongly encouraged to review this information before investing.

## Additional Information

The information and opinions in this report were prepared by DB AG or one of its affiliates (collectively 'DB'). Though the information herein is believed to be reliable and has been obtained from public sources believed to be reliable, DB makes no representation as to its accuracy or completeness. Hyperlinks to third-party websites in this report are provided for reader convenience only. DB neither endorses the content nor is responsible for the accuracy or security controls of those websites.

If you use the services of DB in connection with a purchase or sale of a security that is discussed in this report, or is included or discussed in another communication (oral or written) from a DB analyst, DB may act as principal for its own account or as agent for another person.

DB may consider this report in deciding to trade as principal. It may also engage in transactions, for its own account or with customers, in a manner inconsistent with the views taken in this research report. Others within DB, including strategists, sales staff and other analysts, may take views that are inconsistent with those taken in this research report. DB issues a variety of research products, including fundamental analysis, equity-linked analysis, quantitative analysis and trade ideas. Recommendations contained in one type of communication may differ from recommendations contained in others, whether as a result of differing time horizons, methodologies, perspectives or otherwise. DB and/or its affiliates may also be holding debt or equity securities of the issuers it writes on. Analysts are paid in part based on the profitability of DB AG and its affiliates, which includes investment banking, trading and principal trading revenues.

Opinions, estimates and projections constitute the current judgment of the author as of the date of this report. They do not necessarily reflect the opinions of DB and are subject to change without notice. DB provides liquidity for buyers and sellers of securities issued by the companies it covers. DB analysts sometimes have shorter-term trade ideas that may be inconsistent with DB's existing longer-term ratings. Some trade ideas for equities are listed as Catalyst Calls on the Research Website (https://research.db.com/Research/), and can be found on the general coverage list and also on the covered company's page. A Catalyst Call represents a high-conviction belief by an analyst that a stock will outperform or underperform the market and/or a specified sector over a time frame of no less than two weeks and no more than three months. In addition to Catalyst Calls, analysts may occasionally discuss with our clients, and with DB salespersons and traders, trading strategies or ideas that reference catalysts or events that may have a near-term or medium-term impact on the market price of the securities discussed in this report, which impact may be directionally counter to the analysts' current 12-month view of total return or investment return as described herein. DB has no obligation to update, modify or amend this report or to otherwise notify a recipient thereof if an opinion, forecast or estimate changes or becomes inaccurate. Coverage and the frequency of changes in market conditions and in both general and company-specific economic prospects make it difficult to update research at defined intervals. Updates are at the sole discretion of the coverage analyst or of the Research Department Management, and the majority of reports are published at irregular intervals. This report is provided for informational purposes only and does not take into account the particular investment objectives, financial situations, or needs of individual clients. It is not an offer or a solicitation of an offer to buy or sell any financial instruments or to participate in any particular trading strategy. Target prices are inherently imprecise and a product of the analyst's judgment. The financial instruments discussed in this report may not be suitable for all investors, and investors must make their own informed investment decisions. Prices and availability of financial instruments are subject to change without notice, and investment transactions can lead to losses as a result of price fluctuations and other factors. If a financial instrument is denominated in a currency other than an investor's currency, a change in exchange rates may adversely affect the investment. Past performance is not necessarily indicative of future results. Performance calculations exclude transaction costs, unless otherwise indicated. Unless otherwise indicated, prices are current as of the end of the previous trading session and are sourced from local exchanges via Reuters, Bloomberg and other vendors. Data is also sourced from DB, subject companies, and other parties. Artificial intelligence tools may be used in the preparation of this material, including but not limited to assist in fact-finding, data analysis, pattern recognition, content drafting and editorial corrections pertaining to research material.

The DB Department is independent of other business divisions of the Bank. Details regarding our organizational arrangements and information barriers we have to prevent and avoid conflicts of interest with respect to our research are available on our website (https://research.db.com/Research/) under Disclaimer.

Macroeconomic fluctuations often account for most of the risks associated with exposures to instruments that promise to pay fixed or variable interest rates. For an investor who is long fixed-rate instruments (thus receiving these cash flows), increases in interest rates naturally lift the discount factors applied to the expected cash flows and thus cause a loss. The longer the maturity of a certain cash flow and the higher the move in the discount factor, the higher will be the loss. Upside surprises in inflation, fiscal funding needs, and FX depreciation rates are among the most common adverse macroeconomic shocks to receivers. But counterparty exposure, issuer creditworthiness, client segmentation, regulation (including changes in assets holding limits for different types of investors), changes in tax policies, currency convertibility (which may constrain currency conversion, repatriation of profits and/or liquidation of positions

[中间内容因长度限制已省略]

al in the report, and/or site-visit attendance. Without prior approval from Research Management, analysts may not accept from current or potential Banking clients the costs of travel, accommodations, or other expenses incurred by analysts attending site visits, conferences, social events, and the like. Similarly, without prior approval from Research Management and Anti-Bribery and Corruption ("ABC") team, analysts may not accept perks or other items of value for their personal use from issuers they cover.

Additional information relative to securities, other financial products or issuers discussed in this report is available upon request. This report may not be reproduced, distributed or published without DB's prior written consent.

Backtested, hypothetical or simulated performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG.

It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG

David Folkerts-Landau  
Group Chief Economist and Global Head of Research

<table><tr><td>Pam Finelli
COO and Head of Fixed Income Research</td><td>Steve Pollard
Global Head of Company Research and Sales</td><td>Jim Reid
Global Head of Macro and Thematic Research</td><td>Tim Rokossa
Head of European Company Research</td></tr><tr><td>Matthew Barnard
Head of Americas
Company Research</td><td>Debbie Jones
Global Head of Sustainability and Data Innovation, Research</td><td>Robin Winkler
Head of German Macro Research</td><td>Sameer Goel
Global Head of EM &amp; APAC Research</td></tr><tr><td>Francis Yared
Global Head of Rates Research</td><td>George Saravelos
Global Head of FX Research</td><td>Peter Hooper
Vice-Chair of Research</td><td>Nilendra de-Mel
Head of APAC &amp; Middle East Product Development</td></tr></table>

International Production Locations

<table><tr><td>DB AG</td><td>DB AG</td><td>DB AG</td><td>Deutsche Securities Inc.</td></tr><tr><td>DB Place</td><td>Equity Research</td><td>Filiale Hongkong</td><td>1-3-1 Azabudai</td></tr><tr><td>Level 16</td><td>Mainzer Landstrasse 11-17</td><td>International Commerce Centre</td><td>Azabudai Hills Mori JP Tower</td></tr><tr><td>Corner of Hunter &amp; Phillip Streets</td><td>60329 Frankfurt am Main Germany</td><td>1 Austin Road West, Kowloon, Hong Kong</td><td>Minato-ku, Tokyo 106-0041</td></tr><tr><td>Sydney, NSW 2000 Australia</td><td>Tel: (49) 69 910 00</td><td>Tel: (852) 2203 8888</td><td>Japan Tel: (81) 3 6730 1000</td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td></td><td></td></tr><tr><td>DB AG</td><td>DB Securities Inc.</td><td>DB AG</td><td></td></tr><tr><td>21 Moorfields London EC2Y 9DB United Kingdom Tel: (44) 20 7545 8000</td><td>The DB Center 1 Columbus Circle New York, NY 10019 Tel: (1) 212 250 2500</td><td>Filiale Singapur One Raffles Quay, South Tower Singapore 048583 Tel: (65) 6423 8001</td><td></td></tr></table>
"""
