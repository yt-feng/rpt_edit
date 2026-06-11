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
Asia

China

Consumer

Autos & Auto Technology

Industry

## Autos & Auto Technology

Date

9 June 2026

Industry Update

# China NEV demand leading indicator (weekly new orders) - June 1st week

This chartbook tracks China passenger vehicle new orders on a weekly basis, detailing new order flow trends for key Chinese new energy vehicle (NEV) automakers.

Figure 1: Weekly new order summary for key OEMs

<table><tr><td colspan="2">(unit)</td><td>Jun-26</td><td>May-26</td><td>Jun-25</td><td>WoW</td><td>YoY</td></tr><tr><td colspan="2">Week #</td><td>W23</td><td>W22</td><td>W23</td><td></td><td></td></tr><tr><td colspan="2">Calendar days</td><td>1-7D</td><td>25-31D</td><td>2-8D</td><td></td><td></td></tr><tr><td colspan="7">Weekly New Orders of key OEMs</td></tr><tr><td>1211 HK</td><td>BYD</td><td>47.7 k</td><td>48.7 k</td><td>75 k</td><td>-2%</td><td>-36%</td></tr><tr><td>0175 HK</td><td>Geely (Zeekr and Galaxy)</td><td>24.8 k</td><td>22.1 k</td><td></td><td>12%</td><td></td></tr><tr><td>9927 HK</td><td>HIMA (mainly AITO)</td><td>24.2 k</td><td>40.7 k</td><td>11.4 k</td><td>-41%</td><td>112%</td></tr><tr><td>9863 HK</td><td>Leap Motor</td><td>14.6 k</td><td>15.1 k</td><td></td><td>-3%</td><td></td></tr><tr><td>TSLA US</td><td>Tesla</td><td>14.2 k</td><td>14 k</td><td>12 k</td><td>1%</td><td>18%</td></tr><tr><td>9866 HK</td><td>NIO</td><td>28 k</td><td>38.8 k</td><td>5.4 k</td><td>-28%</td><td>419%</td></tr><tr><td>2015 HK</td><td>Li Auto</td><td>6.7 k</td><td>8.7 k</td><td>8.9 k</td><td>-24%</td><td>-25%</td></tr><tr><td>1810 HK</td><td>Xiaomi</td><td>7.4 k</td><td>8.6 k</td><td>5 k</td><td>-14%</td><td>48%</td></tr><tr><td>9868 HK</td><td>XPeng</td><td>9.5 k</td><td>11.1 k</td><td>11.3 k</td><td>-14%</td><td>-16%</td></tr></table>

Source : Thinkercar

Bin Wang

Research Analyst

+852-220-35496

Wei Huang

Research Associate

+852-2203-7057

Figure 2: Weekly new orders trend of key automakers (Li, NIO, XPeng, Leap, Xiaomi, Tesla)  
![](images/d0e1ffe6855d9cca27c9d4cc8b60d1fe102676ec3ff646f2d89efbedbbc10413.jpg)  
Source : Thinkercar

Figure 3: Weekly BYD, Geely, HIMA (mainly AITO) new orders trend  
![](images/864d5a0fa2524bea915bbee6a1ad4b07d77b5a6533b5471d15f9cb0e1348cf41.jpg)

<details>
<summary>line chart</summary>

| Month    | BYD  | HIMA (mainly AITO) | Geely (Galaxy+Zeekr) |
|----------|------|--------------------|----------------------|
| Jan-26 W1 | 5    | 3                  | 3                    |
| Jan-26 W2 | 20   | 5                  | 5                    |
| Jan-26 W3 | 30   | 6                  | 6                    |
| Jan-26 W4 | 38   | 7                  | 7                    |
| Jan-26 W5 | 35   | 8                  | 8                    |
| Feb-26 W1 | 30   | 7                  | 7                    |
| Feb-26 W2 | 25   | 6                  | 6                    |
| Feb-26 W3 | 12   | 5                  | 5                    |
| Feb-26 W4 | 18   | 6                  | 6                    |
| Mar-26 W1 | 45   | 10                 | 15                   |
| Mar-26 W2 | 48   | 9                  | 18                   |
| Mar-26 W3 | 55   | 10                 | 20                   |
| Mar-26 W4 | 85   | 11                 | 22                   |
| Apr-26 W1 | 65   | 12                 | 20                   |
| Apr-26 W2 | 55   | 11                 | 22                   |
| Apr-26 W3 | 48   | 10                 | 35                   |
| Apr-26 W4 | 45   | 65                 | 35                   |
| May-26 W1 | 50   | 50                 | 30                   |
| May-26 W2 | 45   | 30                 | 25                   |
| May-26 W3 | 40   | 35                 | 20                   |
| May-26 W4 | 45   | 40                 | 35                   |
| May-26 W5 | 48   | 40                 | 25                   |
| Jun-26 W1 | 48   | 30                 | 25                   |
</details>

Source : Thinkercar

Figure 4: Weekly HIMA (mainly AITO) new orders trend  
![](images/c879681054c2ef674e8b59d37c2defa727be66f000f2fd3216e0a015f2f05d7a.jpg)

<details>
<summary>line chart</summary>

| Date       | Value (000 units) |
| ---------- | ----------------- |
| Jan-26 W1  | 2                 |
| Jan-26 W2  | 5                 |
| Jan-26 W3  | 6                 |
| Jan-26 W4  | 7                 |
| Jan-26 W5  | 7                 |
| Feb-26 W1  | 7                 |
| Feb-26 W2  | 5                 |
| Feb-26 W3  | 3                 |
| Feb-26 W4  | 5                 |
| Mar-26 W1  | 12                |
| Mar-26 W2  | 9                 |
| Mar-26 W3  | 9                 |
| Mar-26 W4  | 11                |
| Apr-26 W1  | 11                |
| Apr-26 W2  | 11                |
| Apr-26 W3  | 10                |
| Apr-26 W4  | 65                |
| May-26 W1  | 50                |
| May-26 W2  | 30                |
| May-26 W3  | 32                |
| May-26 W4  | 21                |
| May-26 W5  | 41                |
| Jun-26 W1  | 24                |
</details>

Source : Thinkercar

Figure 5: Weekly Li Auto new orders trend  
![](images/6f485c05bf5df0c03b8087c06f3eb4f79c0893dfcb20d2488123f30f9487a73c.jpg)

<details>
<summary>line chart</summary>

| Date       | Value (000 units) |
| ---------- | ----------------- |
| Jan-26 W1  | 2                 |
| Jan-26 W2  | 4                 |
| Jan-26 W3  | 4                 |
| Jan-26 W4  | 4                 |
| Jan-26 W5  | 4.5               |
| Feb-26 W1  | 4                 |
| Feb-26 W2  | 3                 |
| Feb-26 W3  | 2.5               |
| Feb-26 W4  | 4                 |
| Mar-26 W1  | 5.5               |
| Mar-26 W2  | 5                 |
| Mar-26 W3  | 6                 |
| Mar-26 W4  | 7                 |
| Apr-26 W1  | 8.5               |
| Apr-26 W2  | 9.5               |
| Apr-26 W3  | 9                 |
| Apr-26 W4  | 8                 |
| May-26 W1  | 7                 |
| May-26 W2  | 6                 |
| May-26 W3  | 13.5              |
| May-26 W4  | 12                |
| May-26 W5  | 9                 |
| May-26 W6  | 7                 |
| Jun-26 W1  | 6                 |
</details>

Source : Thinkercar

Figure 6: Weekly NIO group new orders trend  
![](images/512b3273449375d2255779dcc38ac6a87e4c9d7532096cf75edeed71d6778131.jpg)

<details>
<summary>line chart</summary>

| Date       | Value (000 units) |
| ---------- | ----------------- |
| Jan-26 W1 | 1                 |
| Jan-26 W2 | 3                 |
| Jan-26 W3 | 4                 |
| Jan-26 W4 | 5                 |
| Jan-26 W5 | 4                 |
| Feb-26 W1 | 3                 |
| Feb-26 W2 | 2                 |
| Feb-26 W3 | 2                 |
| Feb-26 W4 | 8                 |
| Mar-26 W1 | 9                 |
| Mar-26 W2 | 8                 |
| Mar-26 W3 | 9                 |
| Mar-26 W4 | 10                |
| Apr-26 W1 | 10                |
| Apr-26 W2 | 9                 |
| Apr-26 W3 | 10                |
| Apr-26 W4 | 11                |
| May-26 W1 | 10                |
| May-26 W2 | 10                |
| May-26 W3 | 21                |
| May-26 W4 | 12                |
| May-26 W5 | 39                |
| Jun-26 W1 | 28                |
</details>

Source : Thinkercar

Figure 7: Weekly Tesla new orders trend  
![](images/fc2625f6289329464e56fd514017026638fbbbcf3a65bbc8b00d5d35fb0c58e1.jpg)

<details>
<summary>line chart</summary>

| Date     | Value (000 units) |
| -------- | ----------------- |
| Jan-26 W1 | 2                 |
| Jan-26 W2 | 7                 |
| Jan-26 W3 | 8                 |
| Jan-26 W4 | 7                 |
| Jan-26 W5 | 8                 |
| Feb-26 W1 | 9                 |
| Feb-26 W2 | 8                 |
| Feb-26 W3 | 6                 |
| Feb-26 W4 | 10                |
| Mar-26 W1 | 11                |
| Mar-26 W2 | 14                |
| Mar-26 W3 | 15                |
| Mar-26 W4 | 15                |
| Apr-26 W1 | 15                |
| Apr-26 W2 | 16                |
| Apr-26 W3 | 13                |
| Apr-26 W4 | 13                |
| May-26 W1 | 15                |
| May-26 W2 | 14                |
| May-26 W3 | 11                |
| May-26 W4 | 12                |
| May-26 W5 | 14                |
| Jun-26 W1 | 14                |
</details>

Source : Thinkercar

Figure 8: Weekly Xiaomi new orders trend  
![](images/f0f5d4d2b28de4fe1f4e0c2fc9076463af786959ace2bba574b3885a8393e70f.jpg)

<details>
<summary>line chart</summary>

| Date     | Value (000 units) |
| -------- | ----------------- |
| Jan-26 W1 | 0                 |
| Jan-26 W2 | 1                 |
| Jan-26 W3 | 1                 |
| Jan-26 W4 | 2                 |
| Jan-26 W5 | 2                 |
| Feb-26 W1 | 2                 |
| Feb-26 W2 | 1                 |
| Feb-26 W3 | 2                 |
| Feb-26 W4 | 4                 |
| Mar-26 W1 | 3                 |
| Mar-26 W2 | 3                 |
| Mar-26 W3 | 36                |
| Mar-26 W4 | 14                |
| Apr-26 W1 | 10                |
| Apr-26 W2 | 8                 |
| Apr-26 W3 | 7                 |
| Apr-26 W4 | 5                 |
| May-26 W1 | 8                 |
| May-26 W2 | 7                 |
| May-26 W3 | 5                 |
| May-26 W4 | 10                |
| May-26 W5 | 9                 |
| Jun-26 W1 | 7                 |
</details>

Source : Thinkercar

Figure 9: Weekly XPeng new orders trend  
![](images/60d0449690d49aa661f9ffaa22f2a56dee7c70dda75f7173ad856821f65d5790.jpg)

<details>
<summary>line chart</summary>

| Date       | Value (000 units) |
| ---------- | ----------------- |
| Jan-26 W1  | 0                 |
| Jan-26 W2  | 3                 |
| Jan-26 W3  | 4                 |
| Jan-26 W4  | 5                 |
| Jan-26 W5  | 5                 |
| Feb-26 W1  | 5                 |
| Feb-26 W2  | 3                 |
| Feb-26 W3  | 2                 |
| Feb-26 W4  | 4                 |
| Mar-26 W1  | 16                |
| Mar-26 W2  | 8                 |
| Mar-26 W3  | 5                 |
| Mar-26 W4  | 6                 |
| Apr-26 W1  | 16                |
| Apr-26 W2  | 9                 |
| Apr-26 W3  | 8                 |
| Apr-26 W4  | 7                 |
| May-26 W1  | 7                 |
| May-26 W2  | 7                 |
| May-26 W3  | 5                 |
| May-26 W4  | 29                |
| May-26 W5  | 11                |
| Jun-26 W1  | 9                 |
</details>

Source : Thinkercar

## Appendix 1

Important Disclosures

\*Other information available upon request

\*Prices are current as of the end of the previous trading session unless otherwise indicated and are sourced from local exchanges via Reuters, Bloomberg and other vendors. Other information is sourced from DB, subject companies, and other sources. For disclosures pertaining to recommendations or estimates made on securities other than the primary subject of this research, please see the most recently published company report or visit our global disclosure look-up page on our website at https://research.db.com/Research/Disclosures/EquityResearchDisclosures. Aside from within this report, important risk and conflict disclosures can also be found at https://research.db.com/Research/Disclosures/Disclaimer. Investors are strongly encouraged to review this information before investing.

## Analyst Certification

The views expressed in this report accurately reflect the personal views of the undersigned lead analyst about the subject issuers and the securities of those issuers. In addition, the undersigned lead analyst has not and will not receive any compensation for providing a specific recommendation or view in this report. Bin Wang.

Equity rating dispersion and banking relationships  
![](images/ee167a3d37146ad7d30ccd97c3d9e0e680a4a072b49c59d98b764941b35ab3fc.jpg)

<details>
<summary>bar chart</summary>

Asia Universe
| Category | companies covered (%) | Cos. w/ Banking Relationship (%) | MIFID Investment & Ancillary Services (%) |
| :--- | :--- | :--- | :--- |
| BUY | 81 | 30 | 67 |
| HOLD | 15 | 16 | 56 |
| SELL | 4 | 0 | 50 |
</details>

## Equity Rating and Dispersion Key

The Equity Rating Dispersion Chart depicts the following:

The proportion of recommendations that are rated "buy", "sell" and "hold" over the previous 12 months. This is shown for securities issued in the stated region e.g. "Europe Universe". See rating definitions below. This is represented by the "Companies Covered" bars in the chart. The percentage value displayed above the bar is the proportion as a percentage. E.g. 50% above the "buy" / "Companies Covered" bar means that 50% of DB's equity research covered companies over the past 12 months have a "buy" rating.

Next to each of the three respective bars showing the proportion of "buy", "sell" and "hold" recommendations we provide two additional bars to show:

\- The proportion of "buy", "sell" or "hold recommendations where DB and or/Affiliates provided MIFID Investment or Ancillary Services in the past 12 months. This is represented in the "MIFID Investment and Ancillary Services" bar. The percentage value displayed above the bar shows the proportion of Companies Covered with the given rating where DB has also provided MIFID Investment and Ancillary Services in the past 12 months. E.g. 50% above the "Cos. w/ MIFID Investment and Ancillary Services" bar means 50% of the Companies Covered with the rating stated have also received MIFID Investment and Ancillary Services from DB.

\- The proportion of "buy" (or "sell" or "hold") recommendations where DB and or/Affiliates has provided Investment Banking services in the past 12 months for which it has received compensation. The percentage value displayed above the bar shows the proportion of Companies Covered with the stated rating where DB has also provided Investment Banking services in the past 12 months. E.g. 50% above the "Cos. w/ Investment Banking relationship" bar means 50% of the Companies Covered with the rating stated also have an Investment Banking Relationship with DB.

Buy: Based on a current 12-month view of TSR, we recommend that investors buy the stock.

Sell: Based on a current 12-month view of TSR, we recommend that investors sell the stock.

Hold: We take a neutral view on the stock 12-months out and, based on this time horizon, do not recommend either a Buy or Sell.

TSR = Total Shareholder Return. Percentage change in share price from current price to projected target price plus projected dividend yield

Newly issued research recommendations and target prices supersede previously published research.

## Additional Information

The information and opinions in this report were prepared by DB AG or one of its affiliates (collectively 'DB'). Though the information herein is believed to be reliable and has been obtained from public sources believed to be reliable, DB makes no representation as to its accuracy or completeness. Hyperlinks to third-party websites in this report are provided for reader convenience only. DB neither endorses the content nor is responsible for the accuracy or security controls of those websites.

If you use the services of DB in connection with a purchase or sale of a security that is discussed in this report, or is included or discussed in another communication (oral or written) from a DB analyst, DB may act as principal for its own account or as agent for another person.

DB may consider this report in deciding to trade as principal. It may also engage in transactions, for its own account or with customers, in a manner inconsistent with the views taken in this research report. Others within DB, including strategists, sales staff and other analysts, may take views that are inconsistent with those taken in this research report. DB issues a variety of research products, including fundamental analysis, equity-linked analysis, quantitative analysis and trade ideas. Recommendations contained in one type of communication may differ from recommendations contained in others, whether as a result of differing time horizons, methodologies, perspectives or otherwise. DB and/or its affiliates may also be holding debt or equity securities of the issuers it writes on. Analysts are paid in part based on the profitability of DB AG and its affiliates, which includes investment banking, trading and principal trading revenues.

Opinions, estimates and projections constitute the current judgment of the author as of the date of this report. They do not necessarily reflect the opinions of DB and are subject to change without notice. DB provides liquidity for buyers and sellers of securities issued by the companies it covers. DB analysts sometimes have shorter-term trade ideas that may be inconsistent with DB's existing longer-term ratings. Some trade ideas for equities are listed as Catalyst Calls on the Research Website (https://research.db.com/Research/), and can be found on the general coverage list and also on the covered company's page. A Catalyst Call represents a high-conviction belief by an analyst that a stock will outperform or underperform the market and/or a specified sector over a time frame of no less than two weeks and no more than three months. In addition to Catalyst Calls, analysts may occasionally discuss with our clients, and with DB salespersons and traders, trading strategies or ideas that reference catalysts or events that may have a near-term or medium-term impact on the market price of the securities discussed in this report, which impact may be directionally counter to the analysts' current 12-month view of total return or investment return as described herein. DB has no obligation to update, modify or amend this report or to otherwise notify a recipient thereof if an opinion, forecast or estimate changes or becomes inaccurate. Coverage and the frequency of changes in market conditions and in both general and company-specific economic prospects make it difficult to update research at defined intervals. Updates are at the sole discretion of the coverage analyst or of the Research Department Management, and the majority of reports are published at irregular intervals. This report is provided for informational purposes only and does not take into account the particular investment objectives, financial situations, or needs of individual clients. It is not an offer or a solicitation of an offer to buy or sell any financial instruments or to participate in any particular trading strategy. Target prices are inherently imprecise and a product of the analyst's judgment. The financial instruments discussed

[中间内容因长度限制已省略]

t from current or potential Banking clients the costs of travel, accommodations, or other expenses incurred by analysts attending site visits, conferences, social events, and the like. Similarly, without prior approval from Research Management and Anti-Bribery and Corruption ("ABC") team, analysts may not accept perks or other items of value for their personal use from issuers they cover.

Additional information relative to securities, other financial products or issuers discussed in this report is available upon request. This report may not be reproduced, distributed or published without DB's prior written consent.

Backtested, hypothetical or simulated performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG. It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG

## David Folkerts-Landau

Group Chief Economist and Global Head of Research

Pam Finelli
COO and Head of Fixed
Income Research

Steve Pollard
Global Head of Company
Research and Sales

Jim Reid
Global Head of Macro and
Thematic Research

Tim Rokossa
Head of European
Company Research

Matthew Barnard
Head of Americas
Company Research

Debbie Jones
Global Head of
Sustainability and Data
Innovation, Research

Robin Winkler
Head of German Macro
Research

Sameer Goel
Global Head of EM &
APAC Research

Francis Yared
Global Head of Rates
Research

George Saravelos
Global Head of FX
Research

Peter Hooper
Vice-Chair of Research

Nilendra de-Mel
Head of APAC & Middle
East Product
Development

International Production Locations

<table><tr><td>DB AG</td><td>DB AG</td><td>DB AG</td><td>Deutsche Securities Inc.</td></tr><tr><td>DB Place</td><td>Equity Research</td><td>Filiale Hongkong</td><td>1-3-1 Azabudai</td></tr><tr><td>Level 16</td><td>Mainzer Landstrasse 11-17</td><td>International Commerce</td><td>Azabudai Hills Mori JP Tower</td></tr><tr><td>Corner of Hunter &amp; Phillip</td><td>60329 Frankfurt am Main</td><td>Centre,</td><td>Minato-ku, Tokyo 106-0041</td></tr><tr><td>Streets</td><td>Germany</td><td>1 Austin Road West,Kowloon,</td><td>Japan</td></tr><tr><td>Sydney, NSW 2000</td><td>Tel: (49) 69 910 00</td><td>Hong Kong</td><td>Tel: (81) 3 6730 1000</td></tr><tr><td>Australia</td><td></td><td>Tel: (852) 2203 8888</td><td></td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td></td><td></td></tr><tr><td>DB AG</td><td>DB Securities Inc.</td><td>DB AG</td><td></td></tr><tr><td>21 Moorfields</td><td>The DB Center</td><td>Filiale Singapur</td><td></td></tr><tr><td>London EC2Y 9DB</td><td>1 Columbus Circle</td><td>One Raffles Quay, South</td><td></td></tr><tr><td>United Kingdom</td><td>New York, NY 10019</td><td>Tower,</td><td></td></tr><tr><td>Tel: (44) 20 7545 8000</td><td>Tel: (1) 212 250 2500</td><td>Singapore 048583</td><td></td></tr><tr><td></td><td></td><td>Tel: +65 6423 8001</td><td></td></tr></table>
"""
