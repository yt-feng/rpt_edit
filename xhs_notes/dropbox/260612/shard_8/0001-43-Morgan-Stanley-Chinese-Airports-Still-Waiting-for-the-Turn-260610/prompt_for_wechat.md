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
# Chinese Airports | Asia Pacific

# Still Waiting for the Turn

We remain cautious on Chinese airports, as elevated fuel costs weigh on traffic growth and duty-free improvements take time. GBIA also faces an uncertain earnings rebound amid capacity expansion in soft macro. Move GBIA to UW; remain EW on SIAC and UW on BCIA.

Air traffic growth under pressure amid energy shock: China's air pax growth has been under pressure since Apr-26 as the global energy shock lifted air ticket prices. We observed a pax shift from air to railway starting Mar-26. Domestic pax growth at SIAC, GBIA and BCIA slowed to $3 - 4\%$ YoY in Apr-26 from $6 - 10\%$ YoY in 1Q26. Non-domestic traffic growth also softened to $4 - 18\%$ YoY in Apr-26 from $7 - 24\%$ YoY in 1Q26. SIAC underperformed likely due to higher exposure to Japan routes.

Duty-free business still in transition: Although we believe the new duty-free (DF) contracts signed in Dec-25 favor airports, airport DF revenue remained under pressure in 1Q26 due to the rent-free period at SIAC and disruption during the transition between duty-free operators. DF rent at SIAC fell to Rmb176mn in 1Q26, down 49% YoY. BCIA also saw a decline in per-pax DF spending in 1Q26. That said, we believe per-pax DF spending at Chinese airports has largely bottomed. Over the medium to long term, spending could improve as new product categories are introduced and new operators gradually ramp up.

Uncertain earnings recovery amid capacity expansion in soft macro: The cost-sharing framework between GBIA and its parent has not yet been finalized. We see a possibility that the final profit impact could be greater than under the current transitional arrangement, which involves an asset-use fee of \~Rmb900mn in 2026. Revenue ramp-up is also constrained by: 1) softer travel demand amid elevated fuel costs; and 2) the closure of T1 from May-26 for renovation, which offsets incremental revenue from T3. As a result, we think GBIA's earnings recovery could be slower than previously expected.

Earnings and PT changes: We cut earnings for the three Chinese airports factoring in slower traffic growth, lower DF revenue and higher costs. Our PTs are down \~40% after adjusting outer-year capex (SIAC) and WACC assumptions (GBIA, BCIA).

Move GBIA to UW: GBIA's share price has relatively outperformed among peers YTD2026 (-14ppt vs +0ppt for SSE). However, we expect GBIA's earnings recovery to be slower than expected due to soft traffic growth, T1's closure and potentially greater P&L impact from the still-undetermined cost-sharing arrangement for new capacity. Our 2026-28e earnings for GBIA are 1%, 8% and 20% below consensus, respectively. Remain EW on SIAC: We expect SIAC's DF revenue to normalize from 2Q26, as the impact from the rent-free period fades. We believe per pax DF spending has largely bottomed, but a meaningful recovery will likely take time.

Remain UW on BCIA: We see earnings pressure for BCIA if new flight slots are not added. Its exclusion from Stock Connect could also continue to weigh on valuation.

MS ASIA LIMITED+

## Tenny Song

Equity Analyst

Tenny.Song@morganstanley.com +852 3963-1737

## Qianlei Fan, CFA

Equity Analyst

Qianlei.Fan@morganstanley.com +852 2239-1875

## Evan Chen

Research Associate

Evan.Chen@morganstanley.com +852 2848-7317

## Asia Summer School 2026

![](images/3cfdcc9c967b5a963d80c1170baebb438bc1ecf15fc137b29c6791bed6c3ff46.jpg)

## HONG KONG/CHINA TRANSPORTATION &

## INFRASTRUCTURE

Asia Pacific

Industry View In-Line

WHAT'S CHANGED

<table><tr><td>Guangzhou Baiyun Int&#x27;l Airport(600004.SS)</td><td>From</td><td>To</td></tr><tr><td>Price Target</td><td>Rmb10.90</td><td>Rmb6.60</td></tr><tr><td>Rating</td><td>Equal-weight</td><td>Underweight</td></tr><tr><td>Shanghai International Airport(600009.SS)</td><td>From</td><td>To</td></tr><tr><td>Price Target</td><td>Rmb35.90</td><td>Rmb21.10</td></tr><tr><td>Beijing Capital Int&#x27;l Airport(0694.HK)</td><td>From</td><td>To</td></tr><tr><td>Price Target</td><td>HK$2.40</td><td>HK$1.40</td></tr></table>

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Chinese Airports: Order of Preference

Exhibit 1: Chinese airports: Order of preference

<table><tr><td></td><td>SIAC600009.SS</td><td>BCIA0694.HK</td><td>GBIA600004.SS</td></tr><tr><td></td><td colspan="3"><img src="images/90317c281b9a3887f201a58d031b830dcea9ab010a67e30d060064fe335a56dc.jpg"/></td></tr><tr><td>Rating</td><td>Equal-weight</td><td>Underweight</td><td>Underweight</td></tr><tr><td>Trading Currency</td><td>CNY</td><td>HKD</td><td>CNY</td></tr><tr><td>Price Target</td><td>21.10</td><td>1.40</td><td>6.60</td></tr><tr><td>Current Price</td><td>23.72</td><td>1.70</td><td>8.06</td></tr><tr><td>Upside/(Downside) (%)</td><td>-11%</td><td>-18%</td><td>-18%</td></tr><tr><td>Market Cap (in USD mm)</td><td>8,715.5</td><td>993.8</td><td>3,067.3</td></tr><tr><td>Avg Daily Traded Vol (in USD mm)</td><td>54.0</td><td>3.3</td><td>21.2</td></tr><tr><td colspan="4">Street View: Ratings</td></tr><tr><td>Buy/OverweightHold/Equal-weightSell/Underweight</td><td colspan="3"><img src="images/942e934b4eb72aab6c03900d23f6065f5589913f2bddf4039d93579736d053ea.jpg"/></td></tr><tr><td>Bull Case Value</td><td>33.00</td><td>2.20</td><td>10.50</td></tr><tr><td>Upside (%)</td><td>39%</td><td>29%</td><td>30%</td></tr><tr><td>Bear Case Value</td><td>9.50</td><td>1.00</td><td>4.20</td></tr><tr><td>Downside (%)</td><td>-60%</td><td>-41%</td><td>-48%</td></tr><tr><td>Risk/Reward Skew</td><td>0.7</td><td>0.7</td><td>0.6</td></tr><tr><td colspan="4">MS Estimates</td></tr><tr><td>FY26e</td><td>CNY</td><td>CNY</td><td>CNY</td></tr><tr><td>Sales</td><td>13,814</td><td>5,981</td><td>8,560</td></tr><tr><td>EBITDA</td><td>6,804</td><td>1,890</td><td>2,362</td></tr><tr><td>EBIT</td><td>3,950</td><td>326</td><td>840</td></tr><tr><td>EPS</td><td>1.07</td><td>0.01</td><td>0.26</td></tr><tr><td colspan="4">FY27e</td></tr><tr><td>Sales</td><td>14,792</td><td>6,233</td><td>9,245</td></tr><tr><td>EBITDA</td><td>7,619</td><td>2,108</td><td>2,567</td></tr><tr><td>EBIT</td><td>4,671</td><td>526</td><td>988</td></tr><tr><td>EPS</td><td>1.29</td><td>0.04</td><td>0.30</td></tr><tr><td colspan="4">FY26 MSe vs. Consensus Mean</td></tr><tr><td>Sales</td><td>-3.5%</td><td>-1.4%</td><td>5.2%</td></tr><tr><td>EBITDA</td><td>8.3%</td><td>0.3%</td><td>-5.6%</td></tr><tr><td>EBIT</td><td>22.2%</td><td>-11.4%</td><td>2.2%</td></tr><tr><td>EPS</td><td>-0.8%</td><td>-72.0%</td><td>-15.4%</td></tr><tr><td colspan="4">FY27 MSe vs. Consensus Mean</td></tr><tr><td>Sales</td><td>-2.5%</td><td>-2.7%</td><td>5.2%</td></tr><tr><td>EBITDA</td><td>9.8%</td><td>-1.8%</td><td>-6.6%</td></tr><tr><td>EBIT</td><td>21.8%</td><td>-4.3%</td><td>-5.6%</td></tr><tr><td>EPS</td><td>3.5%</td><td>-35.1%</td><td>-16.8%</td></tr></table>

E = MS estimates. Source: Factset, MS. Share prices are as of the close on June 10, 2026.

# Air Traffic Growth Under Pressure Amid Energy Shock

China's air pax growth has been under pressure since Apr-26 as the global energy shock lifted air ticket prices. While China remains comparatively more insulated than Asian peers – benefiting from domestic fuel price caps, strategic reserves and a coal-heavy energy mix – the demand impact has become increasingly visible: China's total air pax grew only 0.4% YoY in April (domestic -0.2%), a dramatic deceleration from 6.5% YoY in 1Q26. In contrast, China's railway pax growth accelerated to 10.5% in Apr-26 from 5.5% in 1Q26, reflecting pax shift from air to railway, we think. During Labor Day holiday, air pax traffic dropped 5.7% YoY vs. +11.8% YoY during the same holiday in 2025, while railway pax was up 4.6% YoY. China's domestic operated flights and non-domestic capacity both trended down from Mar-26. Non-domestic flight frequency growth YoY even turned negative from May-26.

Exhibit 2: Domestic-operated flights  
![](images/a6c2018951751fd6bd86a7db7a6d1dddca18222b7ee0d71bf6c37a2fa2163bc9.jpg)

<details>
<summary>line chart</summary>

| Month   | Total domestic operated flights YoY |
|---------|------------------------------------|
| Jul-25  | ~0%                                |
| Aug-25  | ~1%                                |
| Sep-25  | ~0%                                |
| Oct-25  | ~5%                                |
| Nov-25  | ~0%                                |
| Dec-25  | ~1%                                |
| Jan-26  | ~0%                                |
| Feb-26  | ~4%                                |
| Mar-26  | ~9%                                |
| Apr-26  | ~3%                                |
| May-26  | ~-7%                               |
</details>

Source: CEIC, MS

Exhibit 3: China's non-domestic capacity YoY  
![](images/ad4167ddfda3538331bf7a335b4562ff35911e9e2f7a7f444f111f61c75c77cd.jpg)

<details>
<summary>line chart</summary>

| Month   | ASK    | Seat   | Frequency |
|---------|--------|--------|-----------|
| Jan-25  | 30%    | 35%    | 40%       |
| Mar-25  | 20%    | 15%    | 10%       |
| May-25  | 15%    | 10%    | 15%       |
| Jul-25  | 10%    | 5%     | 10%       |
| Sep-25  | 5%     | 0%     | 5%        |
| Nov-25  | 10%    | 5%     | 10%       |
| Jan-26  | -5%    | -10%   | -5%       |
| Mar-26  | 5%     | 0%     | 10%       |
| May-26  | 0%     | -5%    | -10%      |
</details>

Source: OAG, MS

Exhibit 4: Railway is gaining market share vs. air since Mar-26.  
![](images/1f51c9e121dcad34346d40e8327ba603bb14ed9ab35150fe75344fb963970611.jpg)

<details>
<summary>line chart</summary>

| Month   | Air pax (mn ppl) | Rail pax (mn ppl) |
|---------|------------------|-------------------|
| Jan-25  | 65               | 380               |
| Feb-25  | 60               | 370               |
| Mar-25  | 59               | 360               |
| Apr-25  | 63               | 390               |
| May-25  | 64               | 410               |
| Jun-25  | 61               | 400               |
| Jul-25  | 70               | 450               |
| Aug-25  | 76               | 500               |
| Sep-25  | 63               | 380               |
| Oct-25  | 68               | 420               |
| Nov-25  | 60               | 370               |
| Dec-25  | 61               | 380               |
| Jan-26  | 63               | 400               |
| Feb-26  | 68               | 430               |
| Mar-26  | 67               | 440               |
| Apr-26  | 61               | 470               |
</details>

Source: CEIC, MS

Pax growth at Chinese airports saw similar trend. Domestic air pax growth at SIAC, GBIA and BCIA slowed to 3-4% YoY in Apr-26 from 6-10% YoY in 1Q26. Non-domestic traffic growth also softened to 4-18% YoY in Apr-26 from 7-24% YoY in 1Q26. SIAC underperformed likely due to higher exposure to Japan routes.

Exhibit 5: Domestic air pax growth at SIAC, GBIA and BCIA slowed to 3-4% YoY in Apr-26 from 6-10% YoY in 1Q26  
![](images/a58e0e8b0391ad6c0ae6ea5f379a64e15d395aa2f3c9373a821df339a6c3871f.jpg)

<details>
<summary>line chart</summary>

| Month   | BCIA  | GBIA  | SIAC (PVG+SHA) |
|---------|-------|-------|----------------|
| Jan-25  | -2.0% | 8.0%  | 6.0%           |
| Feb-25  | -4.0% | -12.0%| -3.0%          |
| Mar-25  | -1.0% | 27.0% | 9.0%           |
| Apr-25  | 5.0%  | 12.0% | 8.0%           |
| May-25  | 6.0%  | 10.0% | 6.0%           |
| Jun-25  | 0.0%  | 8.0%  | 4.0%           |
| Jul-25  | -1.0% | 4.0%  | 2.0%           |
| Aug-25  | -2.0% | 2.0%  | 3.0%           |
| Sep-25  | 4.0%  | 11.0% | 6.0%           |
| Oct-25  | 5.0%  | 10.0% | 7.0%           |
| Nov-25  | 6.0%  | 10.0% | 7.0%           |
| Dec-25  | 6.0%  | 10.0% | 7.0%           |
| Jan-26  | 6.0%  | 1.0%  | 4.0%           |
| Feb-26  | 9.0%  | 17.0% | 8.0%           |
| Mar-26  | 8.0%  | 14.0% | 7.0%           |
| Apr-26  | 4.0%  | 4.0%  | 3.0%           |
</details>

Source: Company data, MS

Exhibit 6: Non-domestic traffic growth also softened to 4-18% YoY in Apr-26 from 7-24% YoY in 1Q26  
![](images/6dc492e160bde78cd858ba7912cb16916c5754f2e630da02db9b09777be9e6fe.jpg)

<details>
<summary>line chart</summary>

| Month   | BCIA  | SIAC (PVG+SHA) | GBIA  |
|---------|-------|----------------|-------|
| Jan-25  | 38.0% | 42.0%          | 44.0% |
| Feb-25  | 9.0%  | 10.0%          | 15.0% |
| Mar-25  | 15.0% | 20.0%          | 22.0% |
| Apr-25  | 20.0% | 22.0%          | 25.0% |
| May-25  | 18.0% | 21.0%          | 19.0% |
| Jun-25  | 15.0% | 17.0%          | 16.0% |
| Jul-25  | 12.0% | 14.0%          | 13.0% |
| Aug-25  | 14.0% | 16.0%          | 15.0% |
| Sep-25  | 16.0% | 18.0%          | 17.0% |
| Oct-25  | 18.0% | 20.0%          | 21.0% |
| Nov-25  | 16.0% | 18.0%          | 20.0% |
| Dec-25  | 10.0% | -5.0%          | 15.0% |
| Jan-26  | 5.0%  | -8.0%          | 18.0% |
| Feb-26  | 22.0% | 14.0%          | 27.0% |
| Mar-26  | 18.0% | 12.0%          | 24.0% |
| Apr-26  | 10.0% | 4.0%           | 18.0% |
</details>

Source: Company data, MS

## Duty-free business is still in a transition period

Both SIAC and BCIA signed new duty-free contracts in Dec-25. We highlight the following changes, which indicate airports are regaining bargaining power vs. duty-free operators, supported by continual traffic growth.

- Breaking the monopoly: Duty-free stores at SIAC and BCIA were previously exclusively operated by CTGDF and its related party. Under the new contracts, both airports have engaged two duty-free operators across different terminals. By leveraging the strength of multiple operators, airports can enrich product categories and improve operating efficiency, which should help boost duty-free spending, in our view.  
- Rewriting the rent formula: The new rent structure is calculated as fixed rent plus commission rent vs. the previous model of minimum rent or commission rent, whichever was higher. For example, at Pudong Terminal 2, the monthly fee is now Rmb3,090/sqm (fixed) plus an 8-24% commission on sales by category, compared with the previous structure of base rent or 18-36% revenue sharing. This new formula will stabilize airports' revenue and motivate duty-free operators to promote sales, we think.  
- Increasing shareholding in duty-free operators: SIAC has established JVs with the new duty-free operators, holding a 49% stake vs. effectively 12.5% previously.

Operators are also encouraged to introduce competitive new product categories and items with gross margins below the maximum commission rate, with a preferential commission applied to such products.

Despite the structurally favorable contract terms, airport duty-free revenue remains under near-term pressure considering: 1) the new contracts only took effect from January 1, 2026 (SIAC) and February 11, 2026 (BCIA). The transition from the previous incumbent to the new operators is ongoing, and new operators require time to build out their product assortment, supply chains, etc. 2) SIAC contracts include a three-month rent-free period during the contract term, which creates a direct near-term drag on airport duty-free revenue. As a result, duty-free rent at SIAC dropped to Rmb176mn in 1Q26, down 49%

YoY. BCIA also saw per pax duty-free spending dropped in 1Q26.

We believe per-pax duty-free spending at Chinese airports has largely bottomed, and we think per pax duty-free spending could improve over the mid- to long-term with new product category expansion and new operators ramping up.

Exhibit 7: Duty-free rent at SIAC dropped 49% YoY in 1Q26 due mainly to rent-free period, we think  
![](images/d0f50ce24d337b75a7646957d5a149f18b64625c9512e553ae39be5750f0ddfc.jpg)

<details>
<summary>line chart</summary>

| Quarter | Duty-free rent at SIAC (Rmb mn) |
| ------- | ------------------------------ |
| 1Q21    | ~90                            |
| 3Q21    | ~140                           |
| 1Q22    | ~100                           |
| 2Q22    | ~20                            |
| 3Q22    | ~100                           |
| 1Q23    | ~350                           |
| 2Q23    | ~530                           |
| 3Q23    | ~480                           |
| 1Q24    | ~350                           |
| 2Q24    | ~280                           |
| 3Q24    | ~300                           |
| 1Q25    | ~350                           |
| 2Q25    | ~300                           |
| 3Q25    | ~320                           |
| 1Q26    | ~180                           |
</details>

Exhibit 8: New duty-free contract at SIAC

<table><tr><td></td><td>Operator</td><td>Fixed rent Rmb/sqm/month</td><td>Commission rate</td><td>Area Sqm</td><td>Fixed rent Rmb mn/year</td><td>Contract period</td></tr><tr><td>PVG T1+S1</td><td>Dufry</td><td>3,141</td><td>8-24%</td><td>8,466</td><td>319</td><td>3 years from 2026 and can be extended 5 years to 2033. (*3+5*)</td></tr><tr><td>PVG T2+S2</td><td>CTG</td><td>3,090</td><td>8-24%</td><td>9,631</td><td>357</td><td>5 years from 2026 and can be extended 3 years to 2033. (*5+3*)</td></tr><tr><td>SHA (Hongqiao)</td><td>CTG</td><td>2,827</td><td>8-22%</td><td>2,471</td><td>84</td><td>5 years from 2026 and can be extended 3 years to 2033. (*5+3*)</td></tr><tr><td colspan="4"></td><td>Total</td><td>760</td><td></td></tr></table>

Source: Company data, MS  
Source: Company data, MS

## Uncertain earnings recovery amid new capacity expansion in soft macro

GBIA's T3 and fifth runway were officially put into use on October 30, 2025, with over Rmb50bn upfront capex undertaken by the parent company. The cost-sharing framework between GBIA and the parent is broadly taking shape but has not yet been finalized: the final arrangement is expected to combine base rent, asset acquisition by GBIA and revenue sharing with the parent – a more complex and multi-layered structure than a simple lease.

The current \~Rmb900mn ann

[中间内容因长度限制已省略]

tor covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Hong Kong/China Transportation & Infrastructure

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/10/2026)</td></tr><tr><td colspan="3">Qianlei Fan, CFA</td></tr><tr><td>Air China Limited (601111.SS)</td><td>O (02/09/2026)</td><td>Rmb6.16</td></tr><tr><td>Air China Limited (0753.HK)</td><td>O (01/13/2025)</td><td>HK$4.31</td></tr><tr><td>Beijing-Shanghai High-Speed Railway (601816.SS)</td><td>O (07/03/2020)</td><td>Rmb5.02</td></tr><tr><td>BOC Aviation (2588.HK)</td><td>O (03/21/2022)</td><td>HK$73.45</td></tr><tr><td>Cathay Pacific Airways (0293.HK)</td><td>O (06/10/2026)</td><td>HK$11.93</td></tr><tr><td>China Eastern Airlines (600115.SS)</td><td>O (02/09/2026)</td><td>Rmb3.83</td></tr><tr><td>China Eastern Airlines (0670.HK)</td><td>O (01/13/2025)</td><td>HK$3.23</td></tr><tr><td>China Merchants Energy Shipping Co. Ltd. (601872.SS)</td><td>O (03/10/2020)</td><td>Rmb14.62</td></tr><tr><td>China Southern Airlines (600029.SS)</td><td>O (02/09/2026)</td><td>Rmb5.11</td></tr><tr><td>China Southern Airlines (1055.HK)</td><td>O (01/13/2025)</td><td>HK$3.50</td></tr><tr><td>COSCO SHIPPING Energy Transportation (1138.HK)</td><td>O (01/12/2023)</td><td>HK$13.03</td></tr><tr><td>COSCO SHIPPING Energy Transportation (600026.SS)</td><td>O (11/25/2025)</td><td>Rmb16.58</td></tr><tr><td>COSCO Shipping Holdings Ltd (601919.SS)</td><td>U (07/15/2024)</td><td>Rmb14.41</td></tr><tr><td>COSCO Shipping Holdings Ltd (1919.HK)</td><td>U (07/15/2024)</td><td>HK$13.93</td></tr><tr><td>J&amp;T Global Express Ltd (1519.HK)</td><td>E (08/21/2024)</td><td>HK$8.79</td></tr><tr><td>Orient Overseas (International) Ltd (0316.HK)</td><td>U (07/15/2024)</td><td>HK$129.90</td></tr><tr><td>Pacific Basin Shipping (2343.HK)</td><td>E (07/04/2025)</td><td>HK$2.86</td></tr><tr><td>S.F. Holding Co Ltd (002352.SZ)</td><td>E (09/01/2025)</td><td>Rmb34.83</td></tr><tr><td>SITC International Holdings Company (1308.HK)</td><td>E (01/12/2023)</td><td>HK$33.48</td></tr><tr><td>Spring Airlines (601021.SS)</td><td>O (08/31/2015)</td><td>Rmb45.15</td></tr><tr><td>TravelSky Technology (0696.HK)</td><td>U (01/13/2025)</td><td>HK$8.97</td></tr><tr><td>ZTO Express (ZTO.N)</td><td>O (11/21/2016)</td><td>US$21.94</td></tr><tr><td colspan="3">Tenny Song</td></tr><tr><td>Beijing Capital Int'l Airport (0694.HK)</td><td>U (09/23/2025)</td><td>HK$1.73</td></tr><tr><td>Guangzhou Baiyun Int'l Airport (600004.SS)</td><td>U (06/10/2026)</td><td>Rmb8.11</td></tr><tr><td>JD Logistics, Inc. (2618.HK)</td><td>O (03/09/2026)</td><td>HK$12.89</td></tr><tr><td>Shanghai International Airport (600009.SS)</td><td>E (09/23/2025)</td><td>Rmb23.82</td></tr><tr><td>STO Express Co Ltd (002468.SZ)</td><td>E (10/22/2024)</td><td>Rmb14.01</td></tr><tr><td>YTO Express Group Co Ltd (600233.SS)</td><td>O (09/11/2025)</td><td>Rmb17.06</td></tr><tr><td>YUNDA Holding Co Ltd (002120.SZ)</td><td>U (07/29/2020)</td><td>Rmb6.57</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
