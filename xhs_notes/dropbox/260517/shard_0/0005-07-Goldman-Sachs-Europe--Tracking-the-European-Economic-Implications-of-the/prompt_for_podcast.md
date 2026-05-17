你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
# Europe: Tracking the European Economic Implications of the Middle East Conflict (15/05)

We track the economic implications for Europe of the conflict in Iran, leveraging daily data and our proprietary tools, including the GS Financial Conditions Index, daily indicators of consumer sentiment, and our higher-frequency growth model jointly considering energy prices, financial conditions, and foreign growth. We compare the reaction of key macroeconomic variables to their move in March 2022.

Giovanni Pierdomenico

+44(20)7051-6807

giovanni.pierdomenico@gs.com

GS International

Exhibit 1: Current Shock is Seen as More Contained for European Natural Gas Than in 2022; Oil Shock Expected to Be More Persistent   
![](images/4c3c849af029803fbbe211ad259b29eb28b8fe44ca8e9d15155cc0ed5719a8a1.jpg)

<details>
<summary>line</summary>

| Months Ahead | Current Forwards | Current GS Baseline Forecast | March 2022 Forwards | Feb 2026 Forwards |
| ------------- | ---------------- | ---------------------------- | -------------------- | ------------------ |
| 0             | 110              | 105                          | 125                  | 70                 |
| 5             | 95               | 90                           | 110                  | 68                 |
| 10            | 85               | 85                           | 100                  | 67                 |
| 15            | 80               | 80                           | 95                   | 66                 |
| 20            | 78               | 78                           | 90                   | 66                 |
| 25            | 77               | 77                           | 85                   | 66                 |
</details>

March 2022: as of day of peak TTF. Feb 2026: as of February 27.

![](images/95b3fe003dc68e960a8c8a2ff2c501eba8cbd561af77bd607b1af3b961d00b42.jpg)

<details>
<summary>line</summary>

| Months Ahead | Current Forwards (EUR/MWh) | Current GS Baseline Forecast (EUR/MWh) | March 2022 Forwards (EUR/MWh) | Feb 2026 Forwards (EUR/MWh) |
|---|---|---|---|---|
| 0 | 50 | 50 | 230 | 30 |
| 5 | 48 | 40 | 200 | 28 |
| 10 | 45 | 35 | 150 | 25 |
| 15 | 35 | 25 | 75 | 20 |
| 20 | 32 | 20 | 65 | 18 |
| 25 | 28 | 18 | 60 | 15 |
</details>

March 2022: as of day of peak TTF. Feb 2026: as of February 27.   
Source: Haver Analytics, Bloomberg, GS Global Investment Research

Exhibit 2: Spot Gasoline Prices and Electricity Forward Prices Have Risen Since the Onset of the Conflict But Are Below Their Recent Peaks   
![](images/01ca3f5589f7bfbd0db3e3d45fdbd3b393b679a11bcdd1764e87bde269920242.jpg)

<details>
<summary>line</summary>

| Date     | EUR/MWh |
| -------- | ------- |
| 05-Dec   | 95      |
| 04-Jan   | 98      |
| 03-Feb   | 92      |
| 05-Mar   | 125     |
| 04-Apr   | 132     |
| 04-May   | 118     |
</details>

![](images/5e22cef9b163022c7f77df1b36ec58b448f19b77e3d4aff3c021217db1daee5f.jpg)

<details>
<summary>line</summary>

| Date    | Gasoline | Diesel |
|---------|----------|--------|
| Jun-22  | 2.1      | 2.1    |
| Dec-22  | 1.8      | 1.9    |
| Jun-23  | 1.7      | 1.6    |
| Dec-23  | 1.9      | 1.8    |
| Jun-24  | 1.7      | 1.6    |
| Dec-24  | 1.7      | 1.5    |
| Jun-25  | 1.7      | 1.5    |
| Dec-25  | 1.7      | 1.6    |
| Jun-26  | 1.9      | 2.2    |
</details>

Source: Eurostat, Bloomberg, Haver Analytics, GS Global Investment Research

Exhibit 3: Consumer Confidence Appears to Have Stabilised   
![](images/36b93954a9571f96a74627d533beeccf160e24854547b77faf47894672737a54.jpg)

<details>
<summary>line</summary>

| Year | Morning Consult (left) | European Commission (right) |
|------|------------------------|-----------------------------|
| 2019 | ~100                   | ~1                          |
| 2020 | ~90                    | ~-1                         |
| 2021 | ~80                    | ~0                          |
| 2022 | ~70                    | ~-1                         |
| 2023 | ~45                    | ~-3                         |
| 2024 | ~70                    | ~-1                         |
| 2025 | ~85                    | ~0                          |
| 2026 | ~60                    | ~-2                         |
</details>

![](images/4b8e3e53cea770622815b94d9a266d8efd8478916e4c36432d446070f975116d.jpg)

<details>
<summary>line</summary>

| Year | Morning Consult (left) | European Commission (right) |
|------|------------------------|-----------------------------|
| 2019 | ~65                    | ~70                         |
| 2020 | ~75                    | ~80                         |
| 2021 | ~65                    | ~75                         |
| 2022 | ~75                    | ~90                         |
| 2023 | ~55                    | ~55                         |
| 2024 | ~65                    | ~70                         |
| 2025 | ~60                    | ~65                         |
| 2026 | ~55                    | ~55                         |
</details>

![](images/5d63e3b94abd472d4cd0451760b7546320a97f2f6ff3e6fbcb418efda0ebfe4f.jpg)

<details>
<summary>line</summary>

| Year | Morning Consult (left) | European Commission (right) |
|------|------------------------|-----------------------------|
| 2019 | ~85                    | ~0.5                        |
| 2020 | ~65                    | ~-1.0                       |
| 2021 | ~85                    | ~1.0                        |
| 2022 | ~70                    | ~-1.5                       |
| 2023 | ~60                    | ~-1.0                       |
| 2024 | ~75                    | ~-0.5                       |
| 2025 | ~80                    | ~0.0                        |
| 2026 | ~65                    | ~-1.5                       |
</details>

![](images/6c74b4941a11ad0c8e524417ece7b5c38308719327deaac14932e66b4b9bb7f5.jpg)

<details>
<summary>line</summary>

| Year | Morning Consult (left) | European Commission (right) |
|------|------------------------|-----------------------------|
| 2019 | ~95                    | ~1.0                        |
| 2020 | ~60                    | ~-2.0                       |
| 2021 | ~80                    | ~0.5                        |
| 2022 | ~85                    | ~0.0                        |
| 2023 | ~65                    | ~-1.0                       |
| 2024 | ~80                    | ~0.0                        |
| 2025 | ~85                    | ~0.5                        |
| 2026 | ~75                    | ~-0.5                       |
</details>

Source: Morning Consult, Haver Analytics, GS Global Investment Research, European Commission

Exhibit 4: Euro Area GSFCIs Have Tightened by Around 25bp Since the Start of the War   
![](images/0a113fc1a0d94fb0ad80aabfab03228b33341cc11e76074c59a365a3ef53f1ba.jpg)

<details>
<summary>line</summary>

| Date     | Percentage points |
| -------- | ----------------- |
| 15-May   | 0.23              |
</details>

Source: GS Global Investment Research

Exhibit 5: Our Model Points to a 0.25pp Drag on Growth This Year from the Energy Shock   
![](images/fa193d82ce911cd5193d9139f4916ec0c74798147013bacc85f6e431af45fda4.jpg)

<details>
<summary>line</summary>

| Date    | Total  | Energy Prices | GS Euro Area FCI |
|---------|--------|---------------|------------------|
| Feb-02  | 0.0    | 0.0           | 0.0              |
| Feb-16  | 0.0    | 0.0           | 0.0              |
| Mar-02  | -0.3   | -0.1          | -0.1             |
| Mar-16  | -0.4   | -0.2          | -0.2             |
| Mar-30  | -0.3   | -0.1          | -0.1             |
| Apr-15  | -0.2   | -0.1          | -0.1             |
| Apr-29  | -0.3   | -0.1          | -0.1             |
| May-14  | -0.2   | -0.1          | -0.1             |
</details>

Model updated as of 6pm London time, May 15th.   
Source: Haver Analytics

Exhibit 6: We Have Downgraded GDP Growth in 2026 by Around 0.8pp in the Euro Area; Pre-War Data Surprised to the Upside in the UK   
![](images/b4ff0ccaccca4e498950f53bf2e60f01d059c282d7bf34afffc353f4526216ee.jpg)

<details>
<summary>line</summary>

| Date       | GS    | Bloomberg Consensus |
| ---------- | ----- | --------------------- |
| 08-Jan     | 1.4   | 1.4                   |
| 23-Jan     | 1.4   | 1.4                   |
| 07-Feb     | 1.4   | 1.4                   |
| 22-Feb     | 1.4   | 1.4                   |
| 09-Mar     | 1.2   | 1.3                   |
| 24-Mar     | 1.0   | 1.2                   |
| 08-Apr     | 0.7   | 1.2                   |
| 23-Apr     | 0.6   | 0.9                   |
| 08-May     | 0.5   | 0.8                   |
</details>

![](images/408c98bf7870053e66f2f44bd11aa1a903afc027d4cc7dea9ac7e09ccc68b727.jpg)

<details>
<summary>line</summary>

Q4/Q4 2026 Real GDP Growth in the UK
| Date | GS (%) | Bloomberg Consensus (%) |
|---|---|---|
| 08-Jan | 1.39 | 1.33 |
| 23-Jan | 1.39 | 1.33 |
| 07-Feb | 1.40 | 1.40 |
| 22-Feb | 1.45 | 1.40 |
| 09-Mar | 1.50 | 1.42 |
| 24-Mar | 0.92 | 1.25 |
| 08-Apr | 0.63 | 1.15 |
| 23-Apr | 1.00 | 0.85 |
| 08-May | 1.05 | 0.85 |
</details>

Source: Bloomberg, GS Global Investment Research

Exhibit 7: We Have Raised Our End-2026 Inflation Forecast By Around 1.9pp in the Euro Area and 1.3pp in the UK   
![](images/818a06e5f8bdf6e112d666d6fb28acf433455a73bd5d91e8df029cc3690d0468.jpg)

<details>
<summary>line</summary>

| Date       | GS   | Bloomberg Consensus |
| ---------- | ---- | ------------------- |
| 08-Jan-23  | 1.50 | 1.80                |
| Jan-07     | 1.75 | 1.80                |
| Feb-22     | 1.75 | 1.80                |
| Mar-09     | 2.25 | 1.90                |
| Apr-24     | 3.00 | 2.25                |
| May-08     | 3.25 | 3.00                |
| Jun-23     | 3.50 | 3.10                |
</details>

![](images/7bcc55ce678644e167a902282d82ae1870d7218a5bb3aeebdda78403fed6854d.jpg)

<details>
<summary>line</summary>

| Date       | GS   | Bloomberg Consensus |
| ---------- | ---- | --------------------- |
| 08-Jan-23  | 2.00 | 2.25                  |
| Jan-07     | 2.10 | 2.25                  |
| Feb-22     | 2.05 | 2.20                  |
| Mar-09     | 2.10 | 2.30                  |
| Apr-24     | 2.50 | 2.75                  |
| May-08     | 3.00 | 3.25                  |
| Jun-23     | 3.25 | 3.35                  |
| Jul-06     | 3.30 | 3.45                  |
</details>

Source: Bloomberg, GS Global Investment Research

Exhibit 8: Data Recap for April 

<table><tr><td>Indicator</td><td>Date</td><td>Reference Period</td><td>Geography</td><td>Notes</td></tr><tr><td>Final Mfg PMI</td><td>01-Apr</td><td>March</td><td>Euro Area, EMU4</td><td>Broadly confirmed flash prints.</td></tr><tr><td>Employment</td><td>06-Apr</td><td>March</td><td>Spain</td><td>Firmer than previous months.</td></tr><tr><td>Final Svcs/Composite PMIs</td><td>07-Apr</td><td>March</td><td>Euro Area, EMU4</td><td>Broadly confirmed flash prints.</td></tr><tr><td>sentix Survey</td><td>07-Apr</td><td>April</td><td>Euro area, Germany</td><td>Further deterioration in expectations and current conditions.</td></tr><tr><td>Final CPI Details</td><td>16-Apr</td><td>March</td><td>Euro Area</td><td>Details stronger than the flash.</td></tr><tr><td>ZEW Survey</td><td>21-Apr</td><td>April</td><td>Euro area, Germany</td><td>0.2sd moderation in both components.</td></tr><tr><td>Flash Consumer Confidence</td><td>22-Apr</td><td>April</td><td>Euro area</td><td>0.9sd drop in consumer confidence</td></tr><tr><td>INSEE Business Survey</td><td>23-Apr</td><td>April</td><td>France</td><td>Rise in selling price plans in the manuf. and retail sectors.</td></tr><tr><td>Flash PMIs</td><td>23-Apr</td><td>April</td><td>Euro area, France, Germany, UK</td><td>Miss on activity, meaningful rise in output prices.</td></tr><tr><td>ifo Survey</td><td>24-Apr</td><td>April</td><td>Germany</td><td>Drop in current conditions and esp. in expectations (most notably in services).</td></tr><tr><td>INSEE Consumer Survey</td><td>24-Apr</td><td>April</td><td>France</td><td>Further rise in expected price developments.</td></tr><tr><td>ECB SAFE Survey</td><td>27-Apr</td><td>Q1</td><td>Euro Area</td><td>Higher non-labour costs and selling price expectations. Unchanged wage expectations.</td></tr><tr><td>GfK Survey</td><td>27-Apr</td><td>April</td><td>Germany</td><td>Lower sentiment, unchanged price expectations.</td></tr><tr><td>Retail Sales</td><td>28-Apr</td><td>March</td><td>Spain</td><td>Firm on fuel and non-fuel sales.</td></tr><tr><td>Lending Data</td><td>29-Apr</td><td>March</td><td>Euro Area</td><td>Resilient.</td></tr><tr><td>ISTAT Survey</td><td>29-Apr</td><td>April</td><td>Italy</td><td>Unchanged sentiment but higher price-related surveys.</td></tr><tr><td>EC Survey</td><td>29-Apr</td><td>April</td><td>Euro Area</td><td>Selling price expectations components rose by a further 1.5sd in manufacturing, by 1.3sd in retail trade, and by 0.6sd in services.</td></tr><tr><td>ECB&#x27;s Consumer Expectations</td><td>29-Apr</td><td>March</td><td>Euro area</td><td>1.5pp rise in median 1-year-ahead inflation expectations to 4.0%.</td></tr><tr><td>Preliminary CPI Data</td><td>30-Apr</td><td>April</td><td>Euro Area, member states</td><td>Energy inflation increased to 10.9%yoy, close to our expectations.</td></tr><tr><td>Q1 GDP</td><td>30-Apr</td><td>Q1</td><td>Euro Area, member states</td><td>Domestic demand likely slowed.</td></tr></table>

Note: Shade indicates released data.

Source: GS Global Investment Research, Bloomberg

Exhibit 9: Data to Watch in May 

<table><tr><td>Indicator</td><td>Date</td><td>Reference Period</td><td>Geography</td><td>Notes</td></tr><tr><td>ECB&#x27;s CTS</td><td>05-May</td><td>Q1</td><td>Euro area</td><td>Uptick in 2026 wage growth expectations.</td></tr><tr><td>Employment</td><td>05-May</td><td>April</td><td>Spain</td><td>+0.2%mom, 3m AR at +3.1%.</td></tr><tr><td>sentix Survey</td><td>05-May</td><td>May</td><td>Euro area, Germany</td><td>Both components broadly unchanged at the area-wide level, some further softeness in Germany.</td></tr><tr><td>Final PMIs</td><td>04-06 May</td><td>April</td><td>Euro area, EMU4</td><td>Broadly unrevised vs. flash prints.</td></tr><tr><td>Industrial Production</td><td>06-08 May</td><td>March</td><td>Germany, France, Spain</td><td>Firm in France and Spain, softer in Germany.</td></tr><tr><td>ECB&#x27;s Wage Tracker</td><td>06-May</td><td>-</td><td>Euro area</td><td>Broadly unchanged.</td></tr><tr><td>Retail Sales</td><td>07-May</td><td>March</td><td>Euro area</td><td>Weak fuel sales volumes (-1.6%mom) and soft food spending, but firmer core-goods spending.</td></tr><tr><td>ZEW Survey</td><td>12-May</td><td>May</td><td>Euro area, Germany</td><td>Stabilisation at weak levels in the Euro area, slightly softer in Germany.</td></tr><tr><td>Industrial Production</td><td>12-May</td><td>March</td><td>Italy</td><td>Firm monthly growth in March.</td></tr><tr><td>Industrial Production</td><td>13-May</td><td>March</td><td>Euro area</td><td>+0.2%mom, with weaker Germany.</td></tr><tr><td>PPI</td><td>20-May</td><td>April</td><td>Germany</td><td></td></tr><tr><td>Final CPI Details</td><td>20-May</td><td>April</td><td>Euro Area</td><td>With country releases over the prior week.</td></tr><tr><td>Flash PMIs</td><td>21-May</td><td>May</td><td>Euro area, France, Germany, UK</td><td></td></tr><tr><td>Flash Consumer Confidence</td><td>21-May</td><td>May</td><td>Euro area</td><td></td></tr><tr><td>GfK Survey</td><td>22-May</td><td>May</td><td>Germany</td><td></td></tr><tr><td>INSEE Business Survey</td><td>22-May</td><td>May</td><td>France</td><td></td></tr><tr><td>ifo Survey</td><td>22-May</td><td>May</td><td>Germany</td><td></td></tr><tr><td>INSEE Consumer Survey</td><td>27-May</td><td>May</td><td>France</td><td></td></tr><tr><td>Retail Sales</td><td>28-May</td><td>April</td><td>Spain</td><td></td></tr><tr><td>EC Survey</td><td>28-May</td><td>May</td><td>Euro area</td><td></td></tr><tr><td>ECB&#x27;s Consumer Expectations</td><td>28-May</td><td>April</td><td>Euro area</td><td></td></tr><tr><td>Preliminary CPI Data</td><td>29-May</td><td>May</td><td>France, Spain, Germany</td><td></td></tr><tr><td>Monthly Goods Consumption</td><td>29-May</td><td>April</td><td>France</td><td></td></tr><tr><td colspan="5">Note: Shade indicates released data.</td></tr></table>

Source: GS Global Investment Research, Bloomberg

Exhibit 10: Investor and Consumer Sentiment and Business Surveys Have Softened, Price-Related Surveys Have Risen   
![](images/381bbd535412d254cb3fe98c801d65b49b52da5a8a0380ae6dd8250145f524b2.jpg)

<details>
<summary>line</summary>

Euro Area EC Consumer Confidence: Deviations from Previous 6m Average
| Months since Event | Middle East War (2026) (%) | Ukraine Invasion (2022) (%) |
|---|---|---|
| -6 | 0.0 | 1.0 |
| -4 | 0.0 | -0.5 |
| -2 | 0.0 | -1.0 |
| 0 | -1.0 | -3.0 |
| 2 | -2.0 | -3.0 |
| 4 | -3.0 | -4.0 |
| 6 | -4.0 | -4.5 |
</details>

![](images/41d143b6ccfc005aa717e0eef5087400336492b614066fee790ea91afe3787df.jpg)

<details>
<summary>line</summary>

| Months since Event | Middle East War (2026) | Ukraine Invasion (2022) |
| ------------------- | ---------------------- | ----------------------- |
| -6                  | 0.1                    | 0.1                     |
| -4                  | 0.0                    | -0.2                    |
| -2                  | 0.0                    | 0.0                     |
| 0                   | -1.5                   | -2.5                    |
| 2                   | -1.0                   | -2.0                    |
| 4                   | -1.5                   | -2.5                    |
| 6                   | -2.0                   | -2.5                    |
</details>

![](images/3d7b3f8128ded808488557958253c863baef863c05c8cf7bd53c615b1cddcd54.jpg)

<details>
<summary>line</summary>

Euro Area EA Manufacturing Output PMI: Deviations from Previous 6m Average
| Months since Event | Middle East War (2026) | Ukraine Invasion (2022) |
|---|---|---|
| -6 | 0.15 | 0.25 |
| -4 | -0.15 | -0.25 |
| -2 | -0.35 | -0.15 |
| 0 | 0.25 | 0.25 |
| 2 | 0.25 | -0.75 |
| 4 | 0.25 | -1.50 |
| 6 | 0.25 | -1.50 |
</details>

![](images/442ce4155a1fe56296d11cf6b91c9f85942d84475e6c1a8ed1920665c0da03a3.jpg)

<details>
<summary>line</summary>

| Months since Event | Middle East War (2026) | Ukraine Invasion (2022) |
| ------------------- | ---------------------- | ------------------------ |
| -6                  | -0.2                   | 0.5                      |
| -4                  | 0.3                    | 0.4                      |
| -2                  | -0.1                 

[中间内容因长度限制已省略]

e have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to sUBStantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g.,

marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
