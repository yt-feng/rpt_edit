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
# Japan banking sector monthly: May 2026

EQUITY: JAPAN BANKS

# Bank stocks seesawing on speculation about BOJ monetary policy

Bank stocks underperformed the TOPIX by 1.7ppt over the past month

# Investment perspective

Bank stocks recovered somewhat from the second half of March through mid-April as equity markets priced in a temporary easing of the situation in the Middle East and expectations were rekindled for a BOJ rate hike in April. However, bank stocks fell through late April even as AI-related stocks rose globally, as expectations for a rate hike at the April monetary policy meeting receded from mid-month following comments by Minister of Finance Satsuki Katayama on 15 April that the BOJ would take a wait-and-see stance in view of the negative impact of the situation in the Middle East, and a report in the Nikkei on 21 April that the BOJ was increasingly likely to leave its policy rate unchanged at 0.75% at its monetary policy meeting on 27–28 April. Bank stocks then outperformed the TOPIX through mid-May, partly because of reports that three policy board members had opposed leaving the policy rate unchanged at the monetary policy meeting and because of somewhat hawkish wording in the Outlook Report. JGB yields have been on an essentially constant upward trajectory over the past month, but bank stocks seesawed on expectations for BOJ rate hikes and underperformed the TOPIX by 1.7ppt over the past month.

# 26/3 results announcements (still in progress): Lending market in Japan

Our first impression of the 26/3 results at major and regional banks released thus far (through 13 May) is that they have been slightly stronger than we had expected. Many banks made progress in improving the health of their balance sheets (including unrealized gains on securities) in 26/3 despite rising interest rates. At the same time, we also see widening disparities among banks in terms of securities portfolio management skills. Our first impression is that guidance for 27/3 is more bullish than in the past in terms of both profit growth and divergence from market consensus forecasts. Loan–deposit operations in Japan have also been performing better than expected. These businesses have been supported not only by an improvement in loan–deposit spreads but also by strong growth in loans outstanding in Japan, particularly in the corporate sector (Figure 10, Figure 14). In structural terms, capex-related lending has been firm. We attribute this to several factors, including solid capex at large companies backed by favorable economic sentiment, DX- and GX-related investment, geopolitical factors (supply chain shifts), borrowings for improvement in corporate value (including LBOs, MBOs, and M&A), and investment in measures to cope with labor shortages. Many bank executives appear to expect these structural funding needs to remain in place for the time being. Recently this has also been compounded by cyclical factors. As during previous periods of financial market turmoil (such as the global financial crisis and the COVID-19 pandemic), more companies have been building up their liquidity on hand (working capital borrowings) in response to the situation in the Middle East, and it looks as though their usage of commitment lines has also risen both in terms of value and of usage rates (Figure 37).

# Research Analysts

Japan banks

Ken Takamiya - NSC

ken.takamiya@NOM.com

+81 3 6703 1140

# Bank sector stock valuations, share prices, performance indicators, and CDS spreads

Fig. 1: Valuations   
2026/5/13 

<table><tr><td rowspan="2">Code</td><td rowspan="2">Company</td><td rowspan="2">Rating</td><td rowspan="2">Share price26/5/13(¥)</td><td rowspan="2">Market cap(¥bn)</td><td colspan="3">Fair value</td><td rowspan="2">Dividendyield25/3 (%)</td><td rowspan="2">DPS25/3 (¥)</td><td colspan="2">P/E</td><td>P/B</td><td colspan="2">ROE</td></tr><tr><td>Target price(¥)</td><td>DCF(¥)</td><td>Relative P/E(¥)</td><td>26/3E(x)</td><td>27/3E(x)</td><td>25/3(x)</td><td>26/3E(%)</td><td>27/3E(%)</td></tr><tr><td>8306</td><td>Mitsubishi UFJ Financial Group</td><td>Buy</td><td>2,926.5</td><td>34,730.9</td><td>3,100</td><td>3,159</td><td>2,948</td><td>2.19</td><td>64.0</td><td>15.7</td><td>12.6</td><td>1.64</td><td>10.2</td><td>11.9</td></tr><tr><td>8308</td><td>Resona Holdings</td><td>Neutral</td><td>2,061.5</td><td>4,756.2</td><td>1,650</td><td>1,819</td><td>1,511</td><td>1.21</td><td>25.0</td><td>19.5</td><td>18.0</td><td>1.73</td><td>8.6</td><td>8.8</td></tr><tr><td>8309</td><td>Sumitomo Mitsui Trust Group</td><td>Buy</td><td>5,660</td><td>3,955.3</td><td>5,700</td><td>6,634</td><td>4,840</td><td>2.74</td><td>155.0</td><td>13.9</td><td>12.3</td><td>1.30</td><td>9.1</td><td>9.7</td></tr><tr><td>8316</td><td>Sumitomo Mitsui Financial Group</td><td>Buy</td><td>5,852</td><td>22,398.5</td><td>6,500</td><td>6,645</td><td>6,425</td><td>2.08</td><td>122.0</td><td>14.2</td><td>11.6</td><td>1.54</td><td>10.6</td><td>12.1</td></tr><tr><td>8411</td><td>Mizuho Financial Group</td><td>Buy</td><td>7,050</td><td>17,222.0</td><td>7,200</td><td>7,252</td><td>7,048</td><td>1.99</td><td>140.0</td><td>15.0</td><td>12.4</td><td>1.69</td><td>10.9</td><td>12.2</td></tr><tr><td>7182</td><td>Japan Post Bank</td><td>Neutral</td><td>2,849.0</td><td>10,187.7</td><td>2,850</td><td>N/A</td><td>N/A</td><td>2.04</td><td>58.0</td><td>20.4</td><td>13.9</td><td>1.13</td><td>5.5</td><td>7.8</td></tr></table>

Note: (1) Estimates are by NOM. (2) P/B ratios are based on common stock, while P/E ratios are based on EPS diluted for private-sector held preferred shares. (3) ROE includes preferred shares, etc
Source: Company data, NOM estimates

Fig. 2: Bank share price performance   
2026/5/13 

<table><tr><td rowspan="2">Code</td><td rowspan="2">Company</td><td colspan="4">Absolute return</td><td colspan="4">Excess return (vs TOPIX)</td><td colspan="4">Excess return (vs TOPIX banks)</td></tr><tr><td>1M</td><td>3M</td><td>6M</td><td>12M</td><td>1M</td><td>3M</td><td>6M</td><td>12M</td><td>1M</td><td>3M</td><td>6M</td><td>12M</td></tr><tr><td>8306</td><td>Mitsubishi UFJ Financial Group</td><td>2.3%</td><td>-2.5%</td><td>19.4%</td><td>53.4%</td><td>-3.0%</td><td>-5.2%</td><td>3.5%</td><td>12.0%</td><td>-1.2%</td><td>1.0%</td><td>-11.6%</td><td>-15.2%</td></tr><tr><td>8316</td><td>Sumitomo Mitsui Financial Group</td><td>4.9%</td><td>-3.5%</td><td>35.1%</td><td>64.5%</td><td>-0.3%</td><td>-6.1%</td><td>19.2%</td><td>23.1%</td><td>1.4%</td><td>0.1%</td><td>4.0%</td><td>-4.1%</td></tr><tr><td>8411</td><td>Mizuho Financial Group</td><td>4.7%</td><td>-8.2%</td><td>32.7%</td><td>86.3%</td><td>-0.6%</td><td>-10.9%</td><td>16.8%</td><td>44.9%</td><td>1.1%</td><td>-4.6%</td><td>1.6%</td><td>17.7%</td></tr><tr><td>8304</td><td>Aozora Bank</td><td>-2.1%</td><td>-6.0%</td><td>16.0%</td><td>33.2%</td><td>-7.4%</td><td>-8.7%</td><td>0.1%</td><td>-8.2%</td><td>-5.7%</td><td>-2.4%</td><td>-15.1%</td><td>-35.4%</td></tr><tr><td>8308</td><td>Resona Holdings</td><td>9.6%</td><td>-3.8%</td><td>30.8%</td><td>72.9%</td><td>4.3%</td><td>-6.4%</td><td>14.9%</td><td>31.5%</td><td>6.0%</td><td>-0.2%</td><td>-0.3%</td><td>4.3%</td></tr><tr><td>8309</td><td>Sumitomo Mitsui Trust Group</td><td>5.9%</td><td>-1.4%</td><td>28.6%</td><td>57.0%</td><td>0.6%</td><td>-4.0%</td><td>12.7%</td><td>15.7%</td><td>2.3%</td><td>2.2%</td><td>-2.5%</td><td>-11.6%</td></tr><tr><td>7182</td><td>Japan Post Bank</td><td>4.5%</td><td>-7.9%</td><td>60.7%</td><td>89.8%</td><td>-0.8%</td><td>-10.6%</td><td>44.8%</td><td>48.4%</td><td>0.9%</td><td>-4.3%</td><td>29.6%</td><td>21.2%</td></tr><tr><td>7186</td><td>Yokohama Financial Group</td><td>5.5%</td><td>-3.7%</td><td>39.9%</td><td>71.3%</td><td>0.3%</td><td>-6.4%</td><td>24.0%</td><td>29.9%</td><td>2.0%</td><td>-0.2%</td><td>8.8%</td><td>2.7%</td></tr><tr><td>8331</td><td>Chiba Bank</td><td>2.7%</td><td>-5.2%</td><td>46.8%</td><td>74.0%</td><td>-2.6%</td><td>-7.9%</td><td>30.9%</td><td>32.6%</td><td>-0.9%</td><td>-1.6%</td><td>15.7%</td><td>5.4%</td></tr><tr><td>5831</td><td>Shizuoka Financial Group</td><td>1.7%</td><td>-5.0%</td><td>35.6%</td><td>83.2%</td><td>-3.6%</td><td>-7.7%</td><td>19.7%</td><td>41.9%</td><td>-1.9%</td><td>-1.4%</td><td>4.5%</td><td>14.6%</td></tr><tr><td>8354</td><td>Fukuoka Financial Group</td><td>2.9%</td><td>-5.6%</td><td>49.4%</td><td>66.2%</td><td>-2.4%</td><td>-8.2%</td><td>33.5%</td><td>24.9%</td><td>-0.7%</td><td>-2.0%</td><td>18.3%</td><td>-2.4%</td></tr><tr><td></td><td>TOPIX bank</td><td>3.6%</td><td>-3.6%</td><td>31.1%</td><td>68.6%</td><td>-1.7%</td><td>-6.2%</td><td>15.2%</td><td>27.2%</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td></td><td>TOPIX</td><td>5.3%</td><td>2.6%</td><td>15.9%</td><td>41.4%</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr></table>

![](images/c226b11297288a8ce8b1c6629e2c052154fc06f7f8318f04633d31f7449d9920.jpg)

<details>
<summary>bar_stacked</summary>

| Category | Outperforming TOPIX by 15% or more | Underperforming TOPIX by 15% or more |
| -------- | --------------------------------- | ----------------------------------- |
| Outperforming TOPIX | 15% | 15% |
| Underperforming TOPIX | 15% | 15% |
| Outperforming TOPIX banks | 10% | 10% |
| Underperforming TOPIX banks | 10% | 10% |
</details>

Source: NOM, based on company data

Fig. 3: Share price performance relative to TOPIX   
2026/5/13   
![](images/34f03a99a5987ac3b066d30459b2cd0673d77425b9f72c2acfb78bcf7f6cb450.jpg)

<details>
<summary>line</summary>

| Date   | TOPIX | TOPIX bank |
|--------|-------|------------|
| 25/5   | -5%   | -5%        |
| 25/7   | -10%  | -10%       |
| 25/9   | -5%   | -5%        |
| 25/11  | 10%   | 10%        |
| 26/1   | 20%   | 30%        |
| 26/3   | 30%   | 70%        |
| 26/5   | 40%   | 80%        |
</details>

![](images/78b16b672b095558d34e04835e0e93bd9a01cc06c1c88b0ddcd63dbdde353bb6.jpg)

<details>
<summary>line</summary>

| Date   | TOPIX | Bank | Electric appliances | Transport equip. | Real estate | Elec. power & gas | Pharmaceuticals |
|--------|-------|------|---------------------|------------------|-------------|-------------------|-----------------|
| 25/5   | ~0%   | ~0%  | ~0%                 | ~0%              | ~0%         | ~0%               | ~0%             |
| 25/7   | ~10%  | ~10% | ~0%                 | ~0%              | ~0%         | ~0%               | ~0%             |
| 25/9   | ~15%  | ~15% | ~0%                 | ~0%              | ~0%         | ~0%               | ~0%             |
| 25/11  | ~20%  | ~20% | ~0%                 | ~0%              | ~0%         | ~0%               | ~0%             |
| 26/1   | ~30%  | ~30% | ~0%                 | ~0%              | ~0%         | ~0%               | ~0%             |
| 26/3   | ~40%  | ~45% | ~0%                 | ~-10%            | ~-5%        | ~10%              | ~-10%           |
| 26/5   | ~45%  | ~35% | ~0%                 | ~-30%            | ~-10%       | ~-5%              | ~-30%           |
</details>

Source: NOM, based on company data

Fig. 4: Investment stance on Japanese financial stocks   
QUICK survey   
![](images/b49c81d37f18fbc4eb1a8275b0a08b5fc5031e2b95cc60d77cc83f2724e69522.jpg)

<details>
<summary>line</summary>

| Date   | Overweight | Underweight | Net overweight |
|--------|------------|-------------|----------------|
| 00/9   | ~0%        | ~30%        | ~-20%          |
| 02/9   | ~10%       | ~50%        | ~-50%          |
| 04/9   | ~15%       | ~35%        | ~-10%          |
| 06/9   | ~20%       | ~30%        | ~-15%          |
| 08/9   | ~15%       | ~40%        | ~-20%          |
| 10/9   | ~10%       | ~35%        | ~-15%          |
| 12/9   | ~15%       | ~30%        | ~-10%          |
| 14/9   | ~20%       | ~35%        | ~-15%          |
| 16/9   | ~15%       | ~40%        | ~-20%          |
| 18/9   | ~10%       | ~35%        | ~-15%          |
| 20/9   | ~15%       | ~40%        | ~-10%          |
| 22/9   | ~20%       | ~35%        | ~-15%          |
| 24/9   | ~30%       | ~40%        | ~-20%          |
</details>

Source: NOM, based on QUICK data

Fig. 5: Japanese, US, and European bank stocks   
![](images/0ff2194601889032f794d8412dab8574c43cc8ea5a86a281acd474266001a720.jpg)

<details>
<summary>line</summary>

| Date   | TOPIX bank | S&P 500 Banks | S&P Europe 350 Banks | TOPIX |
|--------|-----------|---------------|----------------------|-------|
| 25/11  | 100       | 100           | 100                  | 100   |
| 25/12  | 105       | 102           | 103                  | 101   |
| 26/1   | 110       | 108           | 107                  | 104   |
| 26/2   | 130       | 115           | 120                  | 110   |
| 26/3   | 145       | 105           | 118                  | 115   |
| 26/4   | 130       | 100           | 115                  | 112   |
| 26/5   | 135       | 102           | 118                  | 114   |
</details>

![](images/e4bf8d1b6400a8c22a65141f1d9a5606e83c9c79a11ae89fa0174814f91b2510.jpg)

<details>
<summary>line</summary>

| Date   | TOPIX bank | S&P 500 Banks | S&P Europe 350 Banks | TOPIX |
|--------|-----------|---------------|----------------------|-------|
| 25/5   | 100       | 100           | 100                  | 100   |
| 25/7   | 110       | 115           | 110                  | 105   |
| 25/9   | 125       | 120           | 115                  | 110   |
| 25/11  | 135       | 125           | 120                  | 115   |
| 26/1   | 150       | 135           | 130                  | 125   |
| 26/3   | 180       | 140           | 145                  | 140   |
| 26/5   | 170       | 135           | 140                  | 145   |
</details>

Source: NOM, based on Bloomberg data

Fig. 6: Japanese, US, and European CDS index spreads   
![](images/2168dcca39d7c822a90c1203501603df6d4d53f11f721163bc5c516ff3e509f3.jpg)

<details>
<summary>line</summary>

| Date   | iTraxx Japan | itraxx EUR | DJ-CDX NA IG |
|--------|--------------|----------|--------------|
| 25/5   | 100          | 100      | 100          |
| 25/5   | 95           | 95       | 95           |
| 25/6   | 90           | 85       | 80           |
| 25/7   | 85           | 80       | 75           |
| 25/8   | 80           | 75       | 70           |
| 25/9   | 75           | 70       | 65           |
| 25/10  | 80           | 75       | 70           |
| 25/11  | 85           | 80       | 75           |
| 25/12  | 80           | 75       | 70           |
| 26/1   | 75           | 70       | 65           |
| 26/2   | 80           | 75       | 70           |
| 26/3   | 90           | 85       | 80           |
| 26/4   | 100          | 110      | 100          |
| 26/5   | 90           | 85       | 80           |
</details>

Source: NOM, based on Bloomberg data

# Major bank and major regional bank share price performance

Fig. 7: Relative performance vs bank sector
2026/5/13   
![](images/fe71e8d983d0c417f9a46db83347fe043ffe6870534de7c7650b216c0b89432c.jpg)

<details>
<summary>line</summary>

| Date   | MUFG  | TOPIX Banks | Relative performance |
|--------|-------|-------------|----------------------|
| 25/5   | ~10%  | ~10%        | ~0%                  |
| 25/7   | ~15%  | ~15%        | ~0%                  |
| 25/9   | ~30%  | ~30%        | ~0%                  |
| 25/11  | ~40%  | ~40%        | ~0%                  |
| 26/1   | ~60%  | ~60%        | ~0%                  |
| 26/3   | ~50%  | ~70%        | ~-10%                |
</details>

![](images/9dcd2e0fa490cc69ba3947636f0132df8bb9b51959101faee08fbb7e158d4e01.jpg)

<details>
<summary>line</summary>

| Date   | SMFG  | TOPIX Banks | Relative performance |
|--------|-------|-------------|----------------------|
| 25/5   | ~0%   | ~0%         | ~0%                  |
| 25/7   | ~10%  | ~15%        | ~0%                  |
| 25/9   | ~20%  | ~30%        | ~0%                  |
| 25/11  | ~40%  | ~50%        | ~0%                  |
| 26/1   | ~60%  | ~70%        | ~0%                  |
| 26/3   | ~70%  | ~80%        | ~0%                  |
</details>

![](images/adb97f186d970afadb1ad8f8c90c9be7b799e55b19a7e694fbe8b01c029edd1a.jpg)

<details>
<summary>line</summary>

| Date   | Mizuho Financial Group | TOPIX Banks (yy/m) |
|--------|------------------------|--------------------|
| 25/5   | ~0%                    | ~0%                |
| 25/7   | ~20%                   | ~15%               |
| 25/9   | ~40%                   | ~30%               |
| 25/11  | ~60%                   | ~45%               |
| 26/1   | ~80%                   | ~60%               |
| 26/3   | ~100%                  | ~70%               |
</details>

![](images/772c35425be607724c6732ba000b56e1ef763947760346d97cf9ccddf1f06c68.jpg)

<details>
<summary>line</summary>

| Date   | Resona Holdings | TOPIX Banks | Relative performance |
|--------|-----------------|-------------|----------------------|
| 25/5   | ~10%            | ~10%        | ~0%                  |
| 25/7   | ~30%            | ~20%        | ~5%                  |
| 25/9   | ~40%            | ~30%        | ~10%                 |
| 25/11  | ~50%            | ~40%        | ~5%                  |
| 26/1   | ~60%            | ~50%        | ~0%                  |
| 26/3   | ~80%            | ~70%        | ~0%                  |
</details>

![](images/d9a3b8db3515cf74fe5f710114aa7f7f488834f54dc4ff4e330fa7d4d7b52f75.jpg)

<details>
<summary>line</summary>

| Date   | SMTG  | TOPIX Banks |
|--------|-------|-------------|
| 25/5   | ~0%   | ~0%         |
| 25/7   | ~10%  | ~15%        |
| 25/9   | ~20%  | ~30%        |
| 25/11  | ~30%  | ~40%        |
| 26/1   | ~50%  | ~60%        |
| 26/3   | ~60%  | ~80%        |
</details>

![](images/068dc490f8aa0bcc6c60d113b9062a4958b9ac4370a36160f4945c5cda3c5510.jpg)

<details>
<summary>line</summary>

| Date   | Japan Post Bank | TOPIX Banks |
|--------|-----------------|-------------|
| 25/5   | ~0%             | ~0%         |
| 25/7   | ~10%            | ~15%        |
| 25/9   | ~20%            | ~30%        |
| 25/11  | ~30%            | ~40%        |
| 26/1   | ~60%            | ~70%        |
| 26/3   | ~90%            | ~80%        |
</details>

Source: NOM, based on company data

Fig. 8: Relative performance vs bank sector (regional banks)
2026/5/13   
![](images/51d54da978629ea251b914f25f6c7a2b8704ce05c75cd06f6a175767e7aba7a2.jpg)

<details>
<summary>line</summary>

| Date   | Chiba Bank | TOPIX Banks |
|--------|------------|-------------|
| 25/5   | ~0%        | ~0%         |
| 25/7   | ~10%       | ~10%        |
| 25/9   | ~20%       | ~25%        |
| 25/11  | ~30%       | ~35%        |
| 26/1   | ~50%       | ~60%        |
| 26/3   | ~80%       | ~75%        |
| 26/5   | ~65%  

[中间内容因长度限制已省略]

ide consumer price index. The notional principal of inflation-indexed JGBs changes in line with the rate of change in nationwide CPI inflation from the time of its issuance. The amount of the coupon payment is calculated by multiplying the coupon rate by the notional principal at the time of payment. The maturity value is the amount of the notional principal when the issue becomes due. For JI17 and sUBSequent issues, the maturity value shall not undercut the face amount. Purchases of investment trusts (and sales of some investment trusts) are subject to a purchase or sales fee of up to 5.5% (tax included) of the transaction amount. Also, a direct cost that may be incurred when selling investment trusts is a fee of up to 2.0% of the unit price at the time of redemption. Indirect costs that may be incurred during the course of holding investment trusts include, for domestic investment trusts, an asset management fee (trust fee) of up to 5.5% (tax included/annualized basis) of the net assets in trust, as well as fees based on investment

performance. Other indirect costs may also be incurred. For foreign investment trusts, indirect fees may be incurred during the course of holding such as investment company compensation.

Investment trusts invest mainly in securities such as Japanese and foreign equities and bonds, whose prices fluctuate. Investment trust unit prices fluctuate owing to price fluctuations in the underlying assets and to foreign exchange rate fluctuations. As such, investment trusts carry the risk of losses. Fees and risks vary by investment trust. Maximum applicable fees are subject to change; please thoroughly read the written materials provided, such as prospectuses or documents delivered before making a contract.

In interest rate swap transactions and USD/JPY basis swap transactions (“interest rate swap transactions, etc.”), only the agreed transaction payments shall be made on the settlement dates. Some interest rate swap transactions, etc. may require pledging of margin collateral. In some of these cases, transaction payments may exceed the amount of collateral. There shall be no advance notification of required collateral value or collateral ratios as they vary depending on the transaction. Interest rate swap transactions, etc. carry the risk of losses owing to fluctuations in market prices in the interest rate, currency and other markets, as well as reference indices. Losses incurred as such may exceed the value of margin collateral, in which case margin calls may be triggered. In the event that both parties agree to enter a replacement (or termination) transaction, the interest rates received (paid) under the new arrangement may differ from those in the original arrangement, even if terms other than the interest rates are identical to those in the original transaction. Risks vary by transaction. Please thoroughly read the written materials provided, such as documents delivered before making a contract and disclosure statements.

In OTC transactions of credit default swaps (CDS), no sales commission will be charged. When entering into CDS transactions, the protection buyer will be required to pledge or entrust an agreed amount of margin collateral. In some of these cases, the transaction payments may exceed the amount of margin collateral. There shall be no advance notification of required collateral value or collateral ratios as they vary depending on the financial position of the protection buyer. CDS transactions carry the risk of losses owing to changes in the credit position of some or all of the referenced entities, and/or fluctuations of the interest rate market. The amount the protection buyer receives in the event that the CDS is triggered by a credit event may undercut the total amount of premiums that he/she has paid in the course of the transaction. Similarly, the amount the protection seller pays in the event of a credit event may exceed the total amount of premiums that he/she has received in the transaction. All other conditions being equal, the amount of premiums that the protection buyer pays and that received by the protection seller shall differ. In principle, CDS transactions will be limited to financial instruments business operators and qualified institutional investors. Transfers of equities to another securities company via the Japan Securities Depository Center are subject to a transfer fee of up to ¥11,000 (tax included) per issue transferred depending on volume. No account fee will be charged for marketable securities or monies deposited.

# NOM Securities Co., Ltd.

Financial instruments firm registered with the Kanto Local Finance Bureau (registration No. 142)

Member associations: Japan Securities Dealers Association; Investment Management Association of Japan; The Financial Futures Association of Japan; Type II Financial Instruments Firms Association; and Japan Security Token Offering Association.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM Securities Co., Ltd., Japan. All rights reserved.
"""
