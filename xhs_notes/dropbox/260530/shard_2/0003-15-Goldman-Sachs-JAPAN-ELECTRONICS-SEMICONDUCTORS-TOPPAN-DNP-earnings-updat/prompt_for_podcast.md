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
# JAPAN ELECTRONICS/SEMICONDUCTORS

# TOPPAN/DNP earnings update: Reaffirming our positive view on MTPs; current share prices look low at less than 1X P/B

In this report, we update our earnings forecasts for TOPPAN/DNP, review the content of both companies' new medium-term plans, and cross-check our target prices by comparing implied P/B and P/E, as well as ROE/WACC and expected stock returns.

Key points are as follows: (1) We model TOPPAN's FC-BGA sales to grow at a $+35\%$ CAGR and operating profit at a $+26\%$ CAGR. We expect higher investment in next-generation semiconductor packages will weigh on profits, and that this business's operating margin will remain flat to slightly down. (2) For TOPPAN, an acceleration in earnings growth has been deferred to the next medium-term plan (MTP), but we think the company's strong commitment to corporate actions, led by shareholder returns, should be a positive factor that should help sustain market expectations. (3) For DNP's metal masks, we take a more cautious stance than before, given a decline in demand for development stage products due to the memory semiconductor shortage. (4) Our impression of DNP's new MTP is that it signals a shift toward improving the earnings structure through capital allocation and business portfolio strategies centered on agility/flexibility, and through ongoing structural reforms. This raises our expectations for high profit growth as sales growth accelerates. (5) Based on a comparison of implied P/B and P/E, as well as ROE/WACC and expected stock returns, we believe TOPPAN's current share price looks particularly attractive.

Having revised our earnings forecasts and mark-to-market EV/EBITDA peer multiples, we leave our SoTP-based 12m target price for TOPPAN unchanged at ¥6,000 and update our TP for DNP to ¥3,000, from ¥3,100. We maintain our Buy rating on TOPPAN. For DNP, while the current stock price appears undervalued based on the Implied PBR/PER comparison, we maintain our Neutral rating considering the upside potential relative to our target price.

# Updating our earnings forecasts

We maintain our FY3/27-FY3/28 operating profit forecasts for TOPPAN and raise our FY3/29 forecast by +4%. Compared to our post-results forecasts, we raise our sales estimates for the FC-BGA business, mainly due to the normalization of operations from a reduced takt time and volume growth driven by the start-up of a new plant.

# Mitsuhiro Icho

+81(3)4587-9836

mitsuhiro.x.icho@gs.com

GS Japan Co., Ltd.

# Daiki Takayama

+81(3)4587-9870

daiki.takayama@gs.com

GS Japan Co., Ltd.

The main reason for raising our FY3/29 operating profit forecast is the inclusion of a volume contribution from the new plant that year.

Exhibit 1: TOPPAN sales/operating profits by segment: Our old vs. new forecasts 

<table><tr><td colspan="11">(mn JPY)</td><td></td></tr><tr><td rowspan="2">Revenue</td><td colspan="3"></td><td colspan="3">CoE</td><td rowspan="2">Operating Profit</td><td colspan="3"></td><td>CoE</td></tr><tr><td>FY26E</td><td>FY27E</td><td>FY28E</td><td>FY26E</td><td>...</td><td>FY28E</td><td>FY26E</td><td>FY27E</td><td>FY28E</td><td>FY26E</td></tr><tr><td>As of May 15th</td><td>1,910,000</td><td>2,000,000</td><td>2,070,000</td><td></td><td></td><td></td><td>As of May 15th</td><td>85,000</td><td>105,000</td><td>115,000</td><td></td></tr><tr><td>New</td><td>1,913,000</td><td>2,030,000</td><td>2,130,000</td><td>1,925,000</td><td></td><td>2,130,000</td><td>New</td><td>85,000</td><td>105,000</td><td>120,000</td><td>80,000</td></tr><tr><td>% change</td><td>+0%</td><td>+1%</td><td>+3%</td><td></td><td></td><td></td><td>% change</td><td>0%</td><td>0%</td><td>+4%</td><td></td></tr><tr><td>Revenue by segment</td><td colspan="3"></td><td colspan="3"></td><td>OP by segment</td><td colspan="3"></td><td></td></tr><tr><td>Info. &amp; Communications</td><td>FY26E</td><td>FY27E</td><td>FY28E</td><td>FY26E</td><td>...</td><td>FY28E</td><td>Info. &amp; Communications</td><td>FY26E</td><td>FY27E</td><td>FY28E</td><td>FY28E</td></tr><tr><td>As of May 15th</td><td>950,000</td><td>970,000</td><td>980,000</td><td></td><td></td><td></td><td>As of May 15th</td><td>55,000</td><td>58,000</td><td>60,000</td><td></td></tr><tr><td>New</td><td>950,000</td><td>970,000</td><td>980,000</td><td>966,000</td><td></td><td>985,000</td><td>New</td><td>54,000</td><td>55,000</td><td>60,000</td><td>54,500</td></tr><tr><td>% change</td><td>0%</td><td>0%</td><td>0%</td><td></td><td></td><td></td><td>% change</td><td>-2%</td><td>-5%</td><td>0%</td><td></td></tr><tr><td>Living &amp; Industry</td><td colspan="3"></td><td colspan="3"></td><td>Living &amp; Industry</td><td colspan="3"></td><td></td></tr><tr><td>As of May 15th</td><td>800,000</td><td>840,000</td><td>880,000</td><td></td><td></td><td></td><td>As of May 15th</td><td>48,000</td><td>60,000</td><td>64,000</td><td></td></tr><tr><td>New</td><td>806,000</td><td>860,000</td><td>910,000</td><td>827,000</td><td></td><td>915,000</td><td>New</td><td>48,000</td><td>60,000</td><td>70,000</td><td>49,500</td></tr><tr><td>% change</td><td>+1%</td><td>+2%</td><td>+3%</td><td></td><td></td><td></td><td>% change</td><td>0%</td><td>0%</td><td>+9%</td><td></td></tr><tr><td>Electronics</td><td colspan="3"></td><td colspan="3"></td><td>Electronics</td><td colspan="3"></td><td></td></tr><tr><td>As of May 15th</td><td>160,000</td><td>190,000</td><td>210,000</td><td></td><td></td><td></td><td>As of May 15th</td><td>31,000</td><td>39,000</td><td>41,000</td><td></td></tr><tr><td>New</td><td>157,000</td><td>200,000</td><td>240,000</td><td>162,000</td><td></td><td>230,000</td><td>New</td><td>30,000</td><td>36,000</td><td>40,000</td><td>24,000</td></tr><tr><td>% change</td><td>-2%</td><td>+5%</td><td>+14%</td><td></td><td></td><td></td><td>% change</td><td>-3%</td><td>-8%</td><td>-2%</td><td></td></tr></table>

Source: GS Global Investment Research

We lower our FY3/27 operating profit forecast for DNP by 5% as we adopt a more cautious assumption for metal mask volumes, and maintain our FY3/28-29 forecasts. We take into account the current declining demand for low-priced G6 metal masks, impacted by the memory semiconductor shortage (details below).

Exhibit 2: DNP sales/operating profits by segment: Our old vs. new forecasts 

<table><tr><td colspan="5">(mn JPY)</td><td colspan="7">(mn JPY)</td></tr><tr><td rowspan="2">Revenue</td><td colspan="3"></td><td>CoE</td><td rowspan="2">Operating Profit</td><td colspan="3"></td><td colspan="3">CoE</td></tr><tr><td>FY26E</td><td>FY27E</td><td>FY28E</td><td>FY26E</td><td>FY26E</td><td>FY27E</td><td>FY28E</td><td>FY26E</td><td>FY27E</td><td>FY28E</td></tr><tr><td>As of May 14th</td><td>1,550,000</td><td>1,624,200</td><td>1,690,900</td><td></td><td>As of May 14th</td><td>105,000</td><td>115,000</td><td>125,000</td><td></td><td></td><td></td></tr><tr><td>New</td><td>1,540,000</td><td>1,622,500</td><td>1,690,200</td><td>1,530,000</td><td>New</td><td>100,000</td><td>115,000</td><td>125,000</td><td>108,000</td><td>120,000</td><td>130,000</td></tr><tr><td>% change</td><td>-1%</td><td>-0%</td><td>-0%</td><td></td><td>% change</td><td>-5%</td><td>0%</td><td>0%</td><td></td><td></td><td></td></tr><tr><td>Revenue by segment</td><td colspan="3"></td><td colspan="8">OP by segment</td></tr><tr><td>Smart Communication</td><td>FY26E</td><td>FY27E</td><td>FY28E</td><td>FY26E</td><td>Smart Communication</td><td>FY26E</td><td>FY27E</td><td>FY28E</td><td>FY26E</td><td>FY27E</td><td>FY28E</td></tr><tr><td>As of May 14th</td><td>760,000</td><td>788,800</td><td>820,700</td><td></td><td>As of May 14th</td><td>41,000</td><td>46,000</td><td>52,000</td><td></td><td></td><td></td></tr><tr><td>New</td><td>760,000</td><td>788,800</td><td>820,300</td><td>742,000</td><td>New</td><td>42,000</td><td>46,000</td><td>52,000</td><td>43,000</td><td>47,000</td><td>50,000</td></tr><tr><td>% change</td><td>0%</td><td>0%</td><td>-0%</td><td></td><td>% change</td><td>+2%</td><td>0%</td><td>0%</td><td></td><td></td><td></td></tr><tr><td>Life &amp; Healthcare</td><td colspan="3"></td><td>Life &amp; Healthcare</td><td colspan="7"></td></tr><tr><td>As of May 14th</td><td>520,000</td><td>547,200</td><td>562,800</td><td></td><td>As of May 14th</td><td>37,000</td><td>41,000</td><td>43,000</td><td></td><td></td><td></td></tr><tr><td>New</td><td>520,000</td><td>551,400</td><td>567,400</td><td>516,000</td><td>New</td><td>37,000</td><td>42,000</td><td>43,000</td><td>39,000</td><td>43,000</td><td>46,000</td></tr><tr><td>% change</td><td>0%</td><td>+1%</td><td>+1%</td><td></td><td>% change</td><td>0%</td><td>+2%</td><td>0%</td><td></td><td></td><td></td></tr><tr><td>Electronics</td><td colspan="3"></td><td>Electronics</td><td colspan="7"></td></tr><tr><td>As of May 14th</td><td>270,000</td><td>288,200</td><td>307,400</td><td></td><td>As of May 14th</td><td>54,000</td><td>57,000</td><td>61,000</td><td></td><td></td><td></td></tr><tr><td>New</td><td>260,000</td><td>282,300</td><td>302,500</td><td>274,000</td><td>New</td><td>50,000</td><td>56,000</td><td>61,000</td><td>54,000</td><td>59,000</td><td>65,000</td></tr><tr><td>% change</td><td>-4%</td><td>-2%</td><td>-2%</td><td></td><td>% change</td><td>-7%</td><td>-2%</td><td>0%</td><td></td><td></td><td></td></tr></table>

Source: GS Global Investment Research

<table><tr><td>7911.T</td><td>12m Price Target: ¥6000</td><td colspan="2">Price: ¥4632</td><td colspan="2">Upside: 29.5%</td></tr><tr><td>Buy</td><td>GS Forecast</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>3/26</td><td>3/27E</td><td>3/28E</td><td>3/29E</td></tr><tr><td>Market cap: ¥1.3tr / $8.2bn</td><td>Revenue (¥ bn)</td><td>1,805.0</td><td>1,913.0</td><td>2,030.0</td><td>2,130.0</td></tr><tr><td>Enterprise value: ¥1.4tr / $9.0bn</td><td>Op. profit (¥ bn) New</td><td>67.1</td><td>85.0</td><td>105.0</td><td>120.0</td></tr><tr><td>3m ADTV :¥8.8bn/ $55.7mn</td><td>Op. profit (¥ bn) Old</td><td>67.1</td><td>85.0</td><td>105.0</td><td>115.0</td></tr><tr><td>Japan</td><td>Op. profit CoE (¥ bn)</td><td>70.0</td><td>80.0</td><td>--</td><td>--</td></tr><tr><td rowspan="2">Japan Electronic Components/Semiconductors</td><td>EPS (¥) New</td><td>229.8</td><td>328.0</td><td>401.0</td><td>461.1</td></tr><tr><td>EPS (¥) Old</td><td>229.8</td><td>211.4</td><td>270.4</td><td>306.5</td></tr><tr><td>M&amp;A Rank: 3</td><td>P/E (X)</td><td>18.3</td><td>14.1</td><td>11.6</td><td>10.0</td></tr><tr><td></td><td>P/B (X)</td><td>0.9</td><td>0.9</td><td>0.9</td><td>0.9</td></tr><tr><td></td><td>CROCI (%)</td><td>5.6</td><td>5.1</td><td>5.5</td><td>5.8</td></tr><tr><td></td><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td></td><td>EPS (¥)</td><td>23.7</td><td>48.0</td><td>63.9</td><td>88.0</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of May 27th 2026 close.

# FC-BGA

At its results briefing, TOPPAN indicated that FC-BGA earnings growth will not occur until the next MTP (starting from FY3/30), dampening market expectations for earnings growth during the new MTP period (FY3/27-FY3/29) (LINK). The main reason given was due to increased upfront investment cost (capex + R&D expenses) in the next-generation semiconductor packages (mainly glass core substrates) which will weigh on profits in the next few years.

We forecast a sales CAGR of +35% in FY3/27-29 (Exhibit 3). In addition to the gradual start-up of plants and increased production capacity, we expect sales growth to be driven by an improving product mix (= higher unit price per production capacity) as the proportion of high-end network switches and AI ASICs increases. We model operating profit growth in this business to be slower than sales growth, at a +26% CAGR (Exhibit 4). At the results briefing (LINK), TOPPAN discussed plans to increase investment in next-generation semiconductor packages from c.¥1bn in FY3/26 to c.¥8 bn in FY3/27. We expect this will increase further to c.¥15 bn in FY3/28 before peaking in FY3/29. On this basis, we look for the operating margin for FC-BGA to trend flat to slightly down over FY3/27-29. This is in line with the company's assumption for the non-GAAP operating margin for its semiconductor-related business presented at the results briefing.

Exhibit 3: FC-BGA sales growth: FY24=100   
![](images/4ed5a63513b0e321786d961623469d1113a6788b3192e6e9babb7bbdc475ee27.jpg)

<details>
<summary>bar</summary>

FC-BGA revenue
| Fiscal Year | Revenue ($M) |
| :--- | :--- |
| FY24 | 100 |
| FY25 | 100 |
| FY26E | 175 |
| FY27E | 260 |
| FY28E | 335 |
CAGR+35%
</details>

Source: GS Global Investment Research

Exhibit 4: FC-BGA operating profit growth: FY24=100   
![](images/afa6048b0bfeb0972105c82f6d41a5a9cc6c81ae2666d544e4ccc6ce81a4e7fc.jpg)

<details>
<summary>bar</summary>

FC-BGA OP
| Period | FC-BGA OP |
|---|---|
| FY24 | 100 |
| FY25 | 75 |
| FY26E | 155 |
| FY27E | 215 |
| FY28E | 255 |
CAGR+26%
</details>

Source: GS Global Investment Research

Exhibit 5: FC-BGA production capacity trend   
![](images/448aebb965a61bea5f33973d3c81186774a6d684da71b53173a2a9b45a9c7893.jpg)

<details>
<summary>line</summary>

TOPPAN FC-BGA capacity expansion (2024 End=100)
| Period | Capacity (MW) |
|---|---|
| 1H 2025 | 100 |
| 2H 2025 | 150 |
| 1H 2026 | 155 |
| 2H 2026 | 165 |
| 1H 2027 | 200 |
| 2H 2027 | 220 |
| 1H 2028 | 250 |
| 2H 2028 | 255 |
| 1H 2029 | 265 |
| 2H 2029 | 270 |
| 1H 2030 | 280 |
| 2H 2030 | 300 |
</details>

GS estimates from FY26 onward   
Source: Company data, GS Global Investment Research

# Info & Communications

Regarding the current status of its digital solutions, TOPPAN sees a challenge in that many sales are limited to standalone digital solutions, which has prevented it from achieving scale. Solutions proposal activities that integrate operational support—intended to serve as a driver of earnings recovery—have not progressed sufficiently, according to the company. As a result, revenue growth based on the envisioned cycle of digital solutions $\rightarrow$ operational support $\rightarrow$ data analysis $\rightarrow$ consulting has fallen short of the company's expectations, and has not kept pace with capex.

In response, TOPPAN is shifting its business model from the provision of one-time digital solutions to a recurring service model that combines multiple solutions, including operational support. It is also developing services that combine multiple solutions tailored to customer challenges, building long-term relationships with customers and reinforcing its business model to capture cyclical business, as noted above. These efforts are gradually bearing fruit, and in TOPPAN's BPO business, recurring projects now account for $90\%$ of recent sales, helping to secure more stable profits. Going forward, we expect TOPPAN to secure higher margins in this segment by expanding sales while strengthening its leveraged business structure specific to digital businesses (= sharing of products and services).

Exhibit 6: Comparison of turnover and capex in TOPPAN's info & communications segment and DNP's smart communication segment)   
![](images/9412781f2e78a89dcb75212804eaa4dfdc1bbbaeed24de276b2fd61cd047542d.jpg)

<details>
<summary>bar_line</summary>

| Year | TOPPAN Capex (LHS) (mn JY) | DNP Capex (LHS) (mn JY) | TOPPAN turnover (RHS) | DNP turnover (RHS) |
| :--- | :--- | :--- | :--- | :--- |
| FY20 | 24500 | 26000 | 1.05 | 0.87 |
| FY21 | 24000 | 19000 | 1.10 | 0.80 |
| FY22 | 26300 | 36800 | 1.02 | 0.86 |
| FY23 | 35400 | 24500 | 0.95 | 0.89 |
| FY24 | 32000 | 31300 | 0.85 | 0.91 |
</details>

Source: Company data, GS Global Investment Research

Management's view is that FY3/27 and FY3/28 will serve as the key benchmark for achieving its FY3/29 target of ¥985 bn in sales and ¥72.5 bn in non-GAAP operating profit. At present, our forecasts do not incorporate a positive contribution from earnings structure reform, and are thus more conservative than management's target.

# New medium-term plan

We take a positive view of the direction of the corporate actions set forth in the MTP. In particular, the policy of a 100% floor on the total payout ratio is in line with our prior expectations. Although accelerated earnings growth has been deferred to the next MTP, we believe the strong commitment to corporate actions, led by shareholder returns, will help sustain market expectations.

In addition to shareholder returns, TOPPAN outlined plans to improve capital efficiency through a 2pp reduction in SG&A expenses (mainly head office costs) and balance sheet reforms (30% reduction in total assets). TOPPAN's head office assets/expenses have long been viewed by the equity market as a drag on the company's profitability, capital returns, and turnover (Exhibit 7, Exhibit 8), and management's commitment to aim for major progress in the first 1-2 years of the three-year MTP is likely to be welcomed by investors, in our view. In addition, cross-shareholdings had fallen to 12.3% of consolidated net assets as of end-FY3/26, and TOPPAN has set a target to continue reducing them to less than 7% during the new MTP period.

Exhibit 7: TOPPAN/DNP: Asset ratios by segment 

<table><tr><td colspan="2"></td><td>FY3/16</td><td>FY3/17</td><td>FY3/18</td><td>FY3/19</td><td>FY3/20</td><td>FY3/21</td><td>FY3/22</td><td>FY3/23</td><td>FY3/24</td><td>FY3/25</td></tr><tr><td rowspan="4">TOPPAN</td><td>Info. &amp; Communications</td><td>42%</td><td>40%</td><td>38%</td><td>39%</td><td>40%</td><td>34%</td><td>37%</td><td>38%</td><td>42%</td><td>44%</td></tr><tr><td>Living &amp; Industry</td><td>20%</td><td>21%</td><td>21%</td><td>19%</td><td>22%</td><td>19%</td><td>22%</td><td>23%</td><td>23%</td><td>23%</td></tr><tr><td>Electronics</td><td>11%</td><td>10%</td><td>10%</td><td>10%</td><td>10%</td><td>9%</td><td>10%</td><td>14%</td><td>14%</td><td>13%</td></tr><tr><td>Adjustment</td><td>27%</td><td>29%</td><td>31%</td><td>32%</td><td>28%</td><td>39%</td><td>31%</td><td>25%</td><td>21%</td><td>20%</td></tr><tr><td rowspan="4">DNP</td><td>Smart Communication</td><td>52%</td><td>50%</td><td>50%</td><td>50%</td><td>46%</td><td>49%</td><td>47%</td><td>45%</td><td>42%</td><td>39%</td></tr><tr><td>Life &amp; Healthcare</td><td>28%</td><td>28%</td><td>28%</td><td>28%</td><td>28%</td><td>27%</td><td>27%</td><td>27%</td><td>28%</td><td>25%</td></tr><tr><td>Electronics</td><td>16%</td><td>15%</td><td>13%</td><td>13%</td><td>12%</td><td>12%</td><td>13%</td><td>13%</td><td>15%</td><td>20%</td></tr><tr><td>Adjustment</td><td>4%</td><td>7%</td><td>9%</td><td>9%</td><td>14%</td><td>12%</td><td>13%</td><td>15%</td><td>15%</td><td>15%</t

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
