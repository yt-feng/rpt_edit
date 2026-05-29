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
# Japan Machinery: Automation: Trade statistics: April 2026 robot/Robodrill volume inferred from customs data

The Ministry of Finance announced April 2026 trade statistics (customs data) during morning trading on May 28. We use this data as an indicator of volume trends for Fanuc's (Sell) robots and Robodrill No. 30 vertical machining centers, and Yaskawa Electric's (Buy, on the CL) robots. Japanese companies have a large share of the global robot market and high domestic production ratios. Since Japan accounts for the majority of global robot production, we believe export volume trends from Japan to the rest of the world can be viewed as an indicator of investment in robots and automation, mainly in the auto and electronics industries. In this note, we outline our views on the robot industry and casing demand trends inferred from this month's data.

# Yuichiro Isayama

+81(3)4587-9806

yuichiro.isayama@gs.com

GS Japan Co., Ltd.

# Takeru Adachi

+81(3)4587-4067

takeru.adachi@gs.com

GS Japan Co., Ltd.

# Takato Enoki

+81(3)4587-1739

takato.enoki@gs.com

GS Japan Co., Ltd.

Exhibit 1: Robots: Trade statistics summary 

<table><tr><td colspan="5">Robot: Japan</td></tr><tr><td></td><td>N. America</td><td>Europe</td><td>China</td><td>Global</td></tr><tr><td>Volume</td><td>2,065</td><td>1,991</td><td>6,206</td><td>14,271</td></tr><tr><td>yoy</td><td>-4%</td><td>74%</td><td>33%</td><td>41%</td></tr><tr><td>mom</td><td>-19%</td><td>13%</td><td>-18%</td><td>-4%</td></tr><tr><td>Value (¥mn)</td><td>5,569</td><td>5,187</td><td>10,899</td><td>27,532</td></tr><tr><td>yoy</td><td>-9%</td><td>87%</td><td>41%</td><td>33%</td></tr><tr><td>mom</td><td>-22%</td><td>7%</td><td>-18%</td><td>-7%</td></tr><tr><td>ASP (¥mn)</td><td>2.70</td><td>2.61</td><td>1.76</td><td>1.93</td></tr><tr><td>yoy</td><td>-5%</td><td>7%</td><td>6%</td><td>-6%</td></tr><tr><td>mom</td><td>-4%</td><td>-5%</td><td>0%</td><td>-4%</td></tr></table>

<table><tr><td colspan="5">Robot: Fanuc (GSE)</td></tr><tr><td></td><td>N. America</td><td>Europe</td><td>China</td><td>Global</td></tr><tr><td>Volume</td><td>1,633</td><td>1,578</td><td>4,665</td><td>9,398</td></tr><tr><td>yoy</td><td>-1%</td><td>142%</td><td>38%</td><td>49%</td></tr><tr><td>mom</td><td>-23%</td><td>18%</td><td>-14%</td><td>-4%</td></tr><tr><td>Value (¥mn)</td><td>4,834</td><td>4,532</td><td>9,245</td><td>20,536</td></tr><tr><td>yoy</td><td>-8%</td><td>130%</td><td>40%</td><td>35%</td></tr><tr><td>mom</td><td>-23%</td><td>15%</td><td>-14%</td><td>-8%</td></tr><tr><td>ASP (¥mn)</td><td>2.96</td><td>2.87</td><td>1.98</td><td>2.19</td></tr><tr><td>yoy</td><td>-7%</td><td>-5%</td><td>1%</td><td>-9%</td></tr><tr><td>mom</td><td>-1%</td><td>-2%</td><td>0%</td><td>-4%</td></tr></table>

Source: Ministry of Finance, GS Global Investment Research

Exhibit 2: Robodrills: Trade statistics summary 

<table><tr><td colspan="5">Robodrill: Japan</td></tr><tr><td></td><td>Asia</td><td>China</td><td>AeCJ</td><td>Global</td></tr><tr><td>Volume</td><td>1,571</td><td>837</td><td>734</td><td>1,642</td></tr><tr><td>yoy</td><td>-25%</td><td>-27%</td><td>-22%</td><td>-24%</td></tr><tr><td>mom</td><td>12%</td><td>-6%</td><td>43%</td><td>8%</td></tr><tr><td>Value (¥mn)</td><td>10,925</td><td>5,991</td><td>4,934</td><td>12,621</td></tr><tr><td>yoy</td><td>-8%</td><td>-1%</td><td>-15%</td><td>-5%</td></tr><tr><td>mom</td><td>0%</td><td>-6%</td><td>7%</td><td>-5%</td></tr><tr><td>ASP (¥mn)</td><td>6.95</td><td>7.16</td><td>6.72</td><td>7.69</td></tr><tr><td>yoy</td><td>23%</td><td>36%</td><td>9%</td><td>24%</td></tr><tr><td>mom</td><td>-11%</td><td>1%</td><td>-25%</td><td>-12%</td></tr></table>

<table><tr><td colspan="5">Robodrill: Fanuc (GSE)</td></tr><tr><td></td><td>Asia</td><td>China</td><td>AeCJ</td><td>Global</td></tr><tr><td>Volume</td><td>1,147</td><td>621</td><td>526</td><td>1,149</td></tr><tr><td>yoy</td><td>-24%</td><td>-16%</td><td>-31%</td><td>-24%</td></tr><tr><td>mom</td><td>5%</td><td>-11%</td><td>34%</td><td>4%</td></tr><tr><td>Value (¥mn)</td><td>6,789</td><td>3,869</td><td>2,920</td><td>6,842</td></tr><tr><td>yoy</td><td>-17%</td><td>-3%</td><td>-30%</td><td>-18%</td></tr><tr><td>mom</td><td>-7%</td><td>-12%</td><td>1%</td><td>-9%</td></tr><tr><td>ASP (¥mn)</td><td>5.92</td><td>6.23</td><td>5.55</td><td>5.95</td></tr><tr><td>yoy</td><td>9%</td><td>16%</td><td>1%</td><td>8%</td></tr><tr><td>mom</td><td>-11%</td><td>-1%</td><td>-24%</td><td>-12%</td></tr></table>

Source: Ministry of Finance, GS Global Investment Research

# Robot export volume (Fanuc, Yaskawa Electric, and Japan overall)

Fanuc: We estimate that Fanuc robots made at its Yamanashi main plant and its Tsukuba plant account for the bulk of exports from Tokyo/Yokohama. We believe the mom decline in export volume is attributable to the unwinding of the fiscal year-end effect. We think mom momentum of $-14\%$ in export volume to China suggests that Fanuc is not seeing the same sustained growth as some machine tools and FA equipment. We assume that companies with a strong presence in smaller 6-axis or SCARA robots are better positioned to benefit from AI-related demand in China. Although there are differences in the prior-year comparison base, yoy momentum for North America has also turned negative, and we will need to watch for whether the environment here is also changing.

Yaskawa Electric (global exports from Moji in April: 1,309 units, +35% yoy/+33% mom): Yaskawa Electric is the only major robot maker with a production base in Kyushu, and we therefore believe its robots account for the majority of export volume from the port of Moji. Exports were flat to down for South Korea (372 units; 0% mom) and China (104 units; -21% mom). At the same time, the trend in exports to India (381 units) improved, rising +140% mom. Given the characteristics of the company's regional exports, we believe the increase was mainly driven by automotive-related projects, and reflects project circumstances specific to India rather than a global trend.

Exhibit 3: Fanuc: Robot shipment value by destination (GSe)   
![](images/1d612fc144c6dddb6827cf6165432cccb6c4934fcab8e81a1381620e82e3984b.jpg)

<details>
<summary>line</summary>

| Date     | Total | US   | Europe | China |
|----------|-------|------|--------|-------|
| 2010/01  | 1000  | 500  | 300    | 200   |
| 2011/01  | 2000  | 800  | 400    | 300   |
| 2012/01  | 3000  | 1200 | 600    | 400   |
| 2013/01  | 4000  | 1500 | 800    | 500   |
| 2014/01  | 5000  | 1800 | 1000   | 600   |
| 2015/01  | 6000  | 2200 | 1200   | 700   |
| 2016/01  | 7000  | 2500 | 1500   | 800   |
| 2017/01  | 8000  | 3000 | 1800   | 900   |
| 2018/01  | 9000  | 3500 | 2200   | 1100  |
| 2019/01  | 10000 | 4000 | 2500   | 1300  |
| 2020/01  | 11000 | 4500 | 3000   | 1500  |
| 2021/01  | 12000 | 5000 | 3500   | 1700  |
| 2022/01  | 13000 | 5500 | 4000   | 1900  |
| 2023/01  | 14000 | 6000 | 4500   | 2100  |
| 2024/01  | 15000 | 6500 | 5000   | 2300  |
| 2025/01  | 16000 | 7000 | 5500   | 2500  |
| 2026/01  | 17000 | 7500 | 6000   | 2700  |
</details>

Source: Ministry of Finance, GS Global Investment Research

Exhibit 4: Japan: Robot shipment value by destination   
![](images/9eb041e41378eeabd97925ebb66ab558e7ed312b5a826f6c1e6648cc0a48a950.jpg)

<details>
<summary>line</summary>

| Date     | Total  | US    | Europe | China |
|----------|--------|-------|--------|-------|
| 2010/01  | 5000   | 1000  | 500    | 500   |
| 2011/01  | 8000   | 1500  | 800    | 800   |
| 2012/01  | 12000  | 2000  | 1200   | 1200  |
| 2013/01  | 15000  | 2500  | 1500   | 1500  |
| 2014/01  | 18000  | 3000  | 1800   | 1800  |
| 2015/01  | 22000  | 3500  | 2200   | 2200  |
| 2016/01  | 25000  | 4000  | 2500   | 2500  |
| 2017/01  | 30000  | 4500  | 3000   | 3000  |
| 2018/01  | 35000  | 5000  | 3500   | 3500  |
| 2019/01  | 40000  | 5500  | 4000   | 4000  |
| 2020/01  | 45000  | 6000  | 4500   | 4500  |
| 2021/01  | 55000  | 7000  | 5500   | 5500  |
| 2022/01  | 65000  | 8500  | 6500   | 6500  |
| 2023/01  | 75000  | 12500 | 7500   | 7500  |
| 2024/01  | 85000  | 15500 | 8500   | 8500  |
| 2025/01  | 95000  | 18500 | 9500   | 9500  |
| 2026/01  | 115667 | 23567 | 13567  | 13567 |
</details>

Source: Ministry of Finance, Data compiled by GS Global Investment Research

Exhibit 5: Fanuc: Robot export volume to China and average export price (GSe)   
![](images/957fba952889f8e302f9748c4317197c1bf607930d1bffea52f1a07dc990ec93.jpg)

<details>
<summary>line</summary>

| Date     | Unit (LHS) | ASP (RHS) |
|----------|------------|-----------|
| 2010/01  | ~500       | ~2,500    |
| 2011/01  | ~700       | ~2,800    |
| 2012/01  | ~800       | ~3,000    |
| 2013/01  | ~900       | ~3,200    |
| 2014/01  | ~1,000     | ~3,500    |
| 2015/01  | ~1,200     | ~3,300    |
| 2016/01  | ~1,500     | ~3,100    |
| 2017/01  | ~1,800     | ~3,000    |
| 2018/01  | ~2,000     | ~2,900    |
| 2019/01  | ~2,200     | ~2,800    |
| 2020/01  | ~2,500     | ~2,700    |
| 2021/01  | ~3,500     | ~2,600    |
| 2022/01  | ~4,500     | ~2,500    |
| 2023/01  | ~5,500     | ~2,400    |
| 2024/01  | ~4,500     | ~2,300    |
| 2025/01  | ~5,500     | ~2,200    |
| 2026/01  | ~6,500     | ~2,100    |
</details>

Source: Ministry of Finance, GS Global Investment Research

Exhibit 6: Fanuc: Robot export volume to North America and average export price (GSe)   
![](images/933d907db393de64418a1abc9e8a558df912cb2b5e553dca2412bdf41c6ba2bb.jpg)

<details>
<summary>line</summary>

| Date | Unit (LHS) (Units) | ASP (RHS) ($'000$) |
|---|---|---|
| 2010/01 | 300 | 28 |
| 2010/07 | 500 | 24 |
| 2011/01 | 800 | 29 |
| 2011/07 | 1000 | 30 |
| 2012/01 | 1200 | 35 |
| 2012/07 | 1300 | 36 |
| 2013/01 | 1100 | 33 |
| 2013/07 | 1200 | 28 |
| 2014/01 | 1300 | 25 |
| 2014/07 | 1400 | 24 |
| 2015/01 | 1500 | 23 |
| 2015/07 | 1600 | 22 |
| 2016/01 | 1400 | 23 |
| 2016/07 | 1800 | 24 |
| 2017/01 | 2500 | 25 |
| 2017/07 | 2600 | 24 |
| 2018/01 | 2400 | 23 |
| 2018/07 | 2300 | 22 |
| 2019/01 | 500 | 24 |
| 2019/07 | 800 | 25 |
| 2020/01 | 1400 | 24 |
| 2020/07 | 1600 | 23 |
| 2021/01 | 1800 | 22 |
| 2021/07 | 2800 | 21 |
| 2022/01 | 2600 | 23 |
| 2022/07 | 3800 | 19 |
| 2023/01 | 450 | 35 |
| 2023/07 | 1600 | 24 |
| 2024/01 | 450 | 25 |
| 2024/07 | 850 | 23 |
| 2025/01 | 1550 | 24 |
| 2025/07 | 1650 | 23 |
| 2026/01 | 1550 | 23 |
</details>

Source: Ministry of Finance, GS Global Investment Research

# Vertical machining center export volume from Tokyo/Yokohama (assumes Fanuc accounts for the majority of export volume)

Fanuc: We estimate that Robodrills made at Fanuc's Tsukuba plant account for the bulk of the No. 30 vertical machining centers exported to Asia from Tokyo/Yokohama customs. Mom momentum in export volume to China was down $-11\%$ , and we believe this is due to a roll over from peak post-Lunar New Year demand from major customers, such as leading US smartphone makers. Moreover, the peak season ended early, with exports down $-16\%$ yoy. We assume momentum in the current cycle may have been limited due to factors such as persistently high labor costs. While momentum in export volume to India grew a sharp $+328\%$ mom, the volume figure is low compared with past levels. Volume still looks too small to suggest that demand from US smartphone makers has completely shifted to India, but this warrants continued monitoring. We think that smartphone-related demand could remain limited in CY26 although this needs further monitoring.

Exhibit 7: Fanuc: Breakdown of Robodrill export volume by region (GSe)   
![](images/af2a77cc8b59d6fb3998d8d5346ea26c5592e2ad27e57e2c9a0be25984ef72b2.jpg)

<details>
<summary>area</summary>

| Date | Mainland China plus HK (units) | Vietnam (units) | India (units) |
|---|---|---|---|
| 2010/01 | 800 | 0 | 0 |
| 2010/07 | 1000 | 0 | 0 |
| 2011/01 | 1200 | 0 | 0 |
| 2011/07 | 1500 | 0 | 0 |
| 2012/01 | 2500 | 0 | 0 |
| 2012/07 | 3000 | 0 | 0 |
| 2013/01 | 2800 | 0 | 0 |
| 2013/07 | 1500 | 0 | 0 |
| 2014/01 | 3500 | 0 | 0 |
| 2014/07 | 3600 | 3500 | 0 |
| 2015/01 | 3500 | 4800 | 0 |
| 2015/07 | 3500 | 3500 | 500 |
| 2016/01 | 1500 | 500 | 50 |
| 2016/07 | 1500 | 500 | 50 |
| 2017/01 | 2200 | 500 | 50 |
| 2017/07 | 2500 | 500 | 50 |
| 2018/01 | 2200 | 500 | 50 |
| 2018/07 | 2500 | 500 | 50 |
| 2019/01 | 500 | 50 | 5 |
| 2019/07 | 500 | 50 | 5 |
| 2020/01 | 500 | 50 | 5 |
| 2020/07 | 1200 | 50 | 5 |
| 2021/01 | 2800 | 50 | 5 |
| 2021/07 | 3500 | 50 | 5 |
| 2022/01 | 1500 | 50 | 5 |
| 2022/07 | 1500 | 50 | 5 |
| 2023/01 | 800 | 50 | 5 |
| 2023/07 | 800 | 50 | 5 |
| 2024/01 | 800 | 50 | 5 |
| 2024/07 | 800 | 50 | 5 |
| 2025/01 | 800 | 50 | 856 |
| 2025/07 | 800 | 50 | 856 |
| 2026/01 | 800 | 50 | 856 |
</details>

Source: Ministry of Finance, GS Global Investment Research

Exhibit 8: Fanuc: Robodrill export volume to China and average export price (GSe)   
![](images/08ecfeb26952a7cb8a7f036418e07509bf57dd9e99087635cd5b0b70f5161000.jpg)

<details>
<summary>line</summary>

| Date     | Unit (LHS) | ASP (RHS) |
|----------|------------|-----------|
| 2010/01  | ~1,000     | ~6,000    |
| 2011/01  | ~1,500     | ~6,500    |
| 2012/01  | ~2,000     | ~7,000    |
| 2013/01  | ~3,000     | ~8,000    |
| 2014/01  | ~1,500     | ~6,500    |
| 2015/01  | ~2,500     | ~12,000   |
| 2016/01  | ~1,500     | ~8,000    |
| 2017/01  | ~2,000     | ~9,000    |
| 2018/01  | ~1,500     | ~7,500    |
| 2019/01  | ~2,500     | ~12,500   |
| 2020/01  | ~1,500     | ~8,500    |
| 2021/01  | ~2,500     | ~9,500    |
| 2022/01  | ~1,500     | ~7,500    |
| 2023/01  | ~1,500     | ~8,500    |
| 2024/01  | ~1,500     | ~7,500    |
| 2025/01  | ~1,500     | ~8,500    |
| 2026/01  | ~1,500     | ~8,500    |
</details>

Source: Ministry of Finance, GS Global Investment Research

# Price Target Risks and Methodology - Yaskawa Electric (6506.T)

Our 12-month target price of ¥9,200 is based on FY2/28E EV/EBITDA, applying the sector-average multiple of 10X and a 90% sector-relative premium.

Key downside risks include (1) a slowdown in semiconductor and AI Capex related business, (2) slower-than-expected results from cost optimization measures, and (3) disappointment in the capital policy and growth strategy in the next medium-term plan and long-term vision.

# Price Target Risks and Methodology - Fanuc (6954.T)

Our 12-month target price of ¥5,600 is based on FY3/28E EV/EBITDA, applying the sector-average multiple of 10X and a 70% sector-relative premium.

Key upside risks include sales in the FA business recovering to levels above past peaks, greater-than-expected improvement in robot business margins, and share buybacks or other moves to strengthen shareholder returns.

# Disclosure Appendix

# Reg AC

We, Yuichiro Isayama, Takeru Adachi and Takato Enoki, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Yuichiro Isayama GS Japan Co., Ltd., Takeru Adachi GS Japan Co., Ltd., Takato Enoki GS Japan Co., Ltd..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

# GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses inputs for the fiscal year at least seven quarters in the future compared with the year at least three quarters in the future (on a per-share basis for all metrics).

For a more detailed description of how we calculate the GS Factor Profile, please contact your GS representative.

# M&A Rank

Across our global coverage, we examine stocks using an M&A framework, considering both qualitative factors and quantitative factors (which may vary across sectors and regions) to incorporate the potential that certain companies could be acquired. We then assign a M&A rank as a means of scoring companies under our rated coverage from 1 to 3, with 1 representing high (30%-50%) probability of the company becoming an acquisition target, 2 representing medium (15%-30%) probability and 3 representing low (0%-15%) probability. For companies ranked 1 or 2, in line with our standard departmental guidelines we incorporate an M&A component into our target price. M&A rank of 3 is considered immaterial and therefore does not factor into our price target, and may or may not be discussed in research.

# Quantum

Quantum is GS' proprietary database providing access to detailed financial statement histories, forecasts and ratios. It can be used for in-depth analysis of a single company, or to make comparisons between companies in different sectors and markets.

# Disclosures

The

[中间内容因长度限制已省略]

rm impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
