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
## Australia Materials | Asia Pacific

# DataDig: Sovereign Supply to Counter Sovereign Demand?

Charts, analysis and comparables for the global mining sector.

With the establishment of CMRG as a central buying agency to provide China with increased buying power, a new sovereign demand/supply trend seems to be gathering pace. Indonesia is centralising commodity exports, starting with coal, palm oil, and ferroalloys, through a state-linked export agency, PT Danantara Sumberdaya Indonesia or DSI. The policy aims to improve export transparency, reduce under-invoicing/transfer pricing and keep more proceeds onshore. Indonesia accounts for \~55% of global palm oil exports, and 45% of traded thermal coal supply for 2026. Australia represents \~59% of seaborne iron ore exports, 38% and 20% for met and thermal coal, and 24% for lithium (by our estimates). Currently, Australian miners have limited scope to coordinate directly, and cannot agree on pricing, terms, allocation, production, or marketing strategy without creating competition law risk. Although a state-linked export desk for Australian IO and other commodities would create trade and sovereign risk concerns, it could also give Australian producers a way to tackle concentrated buying by governments in markets where Australia has sizable supply. For our IO coverage, BHP (OW) implies an IO price of \~US\$82/t, preferred over RIO.AX (EW; US\$89/t) (see our global insight). UW on FMG, implying US\$98/t. OW on DRR (FY27e yield 5.1%, US\$98/t).

Exhibit 1: Australia Exports a Significant Share of Key Commodities  
![](images/d9c519491a81ac44a936066dc4e9232f71f9e7e06c63454523769c1a31853e9f.jpg)

<details>
<summary>bar chart</summary>

Share of Global Seaborne Supply
| Country | Palm Oil (%) | Thermal Coal (%) | Met Coal (%) | Iron Ore (%) | Lithium (%) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Indonesia | 55 | 45 | 3 | | |
| Australia | | 20 | 38 | 59 | 24 |
</details>

Note: Lithium and Palm Oil shown as a percentage of total Global Supply. Source: MS estimates.

<table><tr><td>ASX Miners Relative Preference Table</td><td>P2</td><td>China – Macro Outlook</td><td>P16</td></tr><tr><td>ASX Coverage Valuation Tables</td><td>P3</td><td>Electric Vehicle-related Charts</td><td>P22</td></tr><tr><td>ASX Mining Equities</td><td>P5</td><td>Commodities: Aluminium</td><td>P27</td></tr><tr><td>ASX Miners Revenue Exposures</td><td>P6</td><td>Commodities: Coal</td><td>P30</td></tr><tr><td>ASX Mining Sector vs. Industrials Ex-Banks</td><td>P7</td><td>Commodities: Copper</td><td>P32</td></tr><tr><td>ASX Mining vs. Industrials – Relative</td><td>P8</td><td>Commodities: Gold and Precious Metals</td><td>P35</td></tr><tr><td>Australian Mining vs. Global Mining Sector</td><td>P9</td><td>Commodities: Iron Ore</td><td>P37</td></tr><tr><td>Global Mining Sector vs. Global Market</td><td>P10</td><td>Commodities: Lithium</td><td>P40</td></tr><tr><td>Global Miners – Valuation Tables</td><td>P11</td><td>Commodities: Nickel</td><td>P48</td></tr><tr><td>Commodities vs. Marginal Cost</td><td>P15</td><td>Commodities: Zinc</td><td>P50</td></tr></table>

MS AUSTRALIA LIMITED+

Rahul Anand, CFA

Equity Analyst

R.Anand@morganstanley.com +61 2 9770-1136

Michael A Stancliff

Research Associate

Michael.Stancliff@morganstanley.com +61 2 9770-9253

Asia Summer School 2026

![](images/9f49c355ea8f18b37d95b5d09f7862da66da2d376547948e02aaaf9e8b714d8d.jpg)

## AUSTRALIA MATERIALS

Asia Pacific

Industry View

Attractive

Recent Research:

Sustainability & Metals & Mining: EU's Critical Raw Materials Security in a Multipolar World (5 Jun 2026)

Asia Energy Security and AI: Energy Meets

Compute: Supercycle Recharges (21 May 2026)

Mineral Resources Limited: TripNotes: Wodgina Site Visit (20 May 2026)

BHP Group Ltd: Rising data centre build favours BHP's commodity mix – but there's plenty of alpha too (13 May 2026)

Boss Energy Ltd: Updating Estimates and Price Target (1 May 2026)

Mineral Resources Limited: Updating Estimates (30 Apr 2026)

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## ASX Miners Relative Preference Table

Exhibit 2: ASX Miners – Investment thesis, upside/downside to share price, financial metrics and consensus ratings

<table><tr><td>Rank</td><td>Code</td><td>Rating</td><td>Index</td><td>Consensus(Buy, Hold, Sell)</td><td>Last Price</td><td>Target</td><td>Upside /Downside</td><td>EV/EBITDA1yr fwd</td><td>FCF Yield1yr fwd</td><td>Div. Yield1yr fwd</td><td>Gearing1yr fwd</td><td>12 Mth move</td><td>Investment Thesis</td></tr><tr><td>1</td><td>WHC</td><td>OW</td><td>100</td><td>64% 21% 14%</td><td>9.37</td><td>9.55</td><td>2%</td><td>4.3</td><td>13%</td><td>6%</td><td>12%</td><td></td><td>WHC has seen improving operational performance across assets, which we think could continue into FY26e. FID Winchester South would boost valuation further, while generating strong operating cash flow following cost-out initiatives at Queensland assets.</td></tr><tr><td>2</td><td>PDN</td><td>OW</td><td>200</td><td>53% 27% 20%</td><td>11.05</td><td>13.65</td><td>24%</td><td>15.5</td><td>4%</td><td>0%</td><td>-7%</td><td></td><td>We expect production issues faced during ramp up of Langer Heinrich to be rectified in FY26. PDN also has strong growth potential through Patterson Lake South, a 9.1 Mbpa project in Canada with first production expected in CY31e, which could make PDN a sizeable uranium player.</td></tr><tr><td>3</td><td>S32</td><td>OW</td><td>50</td><td>69% 25% 6%</td><td>4.63</td><td>4.85</td><td>5%</td><td>6.5</td><td>2%</td><td>3%</td><td>-2%</td><td></td><td>S32 has potential to continue generating significant cash flow, enabling strong shareholder returns along with potential to grow base metals production through its Hermosa project in the US.</td></tr><tr><td>4</td><td>BHP</td><td>OW</td><td>20</td><td>25% 75% 0%</td><td>61.24</td><td>67.50</td><td>10%</td><td>7.6</td><td>5%</td><td>4%</td><td>13%</td><td></td><td>BHP has an attractive commodity mix (iron ore, copper, met coal), resilient FCF and potential for shareholder returns, while maintaining a strong balance sheet for favourable growth and/or increasing cash shareholder returns.</td></tr><tr><td>5</td><td>ILU</td><td>OW</td><td>200</td><td>56% 44% 0%</td><td>7.75</td><td>7.95</td><td>3%</td><td>24.9</td><td>-11.4%</td><td>2%</td><td>41%</td><td></td><td>We see ILU&#x27;s rare earth downstream strategy well positioned to benefit from establishment of an ex-China rare earths supply chain. We also see any near-term weakness in the mineral sand market as being fairly priced in.</td></tr><tr><td>6</td><td>BOE</td><td>OW</td><td>N/A</td><td>33% 33% 33%</td><td>1.28</td><td>1.80</td><td>41%</td><td>2.4</td><td>8%</td><td>0%</td><td>-11%</td><td></td><td>We see potential for an improved production scenario from a revised Honeymoon Feasibility Study expected 3QCY26. Although uncertainty remains, we see risks and opportunities skewed to the upside, and we remain constructive on the outlook for Uranium.</td></tr><tr><td>7</td><td>DRR</td><td>OW</td><td>200</td><td>50% 50% 0%</td><td>4.40</td><td>4.45</td><td>1%</td><td>10.5</td><td>6%</td><td>5%</td><td>31%</td><td></td><td>We like DRR&#x27;s high-grade iron ore exposure, primarily from the MAC asset. Deterra&#x27;s yields are less sensitive to change in iron ore prices being a royalty company.</td></tr><tr><td>8</td><td>PLS</td><td>EW</td><td>50</td><td>47% 27% 27%</td><td>5.91</td><td>5.60</td><td>-5%</td><td>11.8</td><td>2%</td><td>1%</td><td>-30%</td><td></td><td>PLS has expansion optionality at Pilgangoora, and we also see potential for a near-term restart at Ngungaju to capitalise on the strong rebound in spodumene prices. P2000 FID could boost valuation, with study results expected CY26-end.</td></tr><tr><td>9</td><td>LYC</td><td>EW</td><td>50</td><td>62% 23% 15%</td><td>18.16</td><td>20.45</td><td>13%</td><td>16.4</td><td>3%</td><td>0%</td><td>-67%</td><td></td><td>LYC stands to benefit from rare earths supply chain diversification, and is also expanding its separated HRE product offerings through a new separation facility in Malaysia which we expect will drive earnings growth, however we see the stock as fairly valued currently.</td></tr><tr><td>10</td><td>RIO</td><td>EW</td><td>20</td><td>47% 47% 7%</td><td>184.58</td><td>171.50</td><td>-7%</td><td>8.6</td><td>4%</td><td>4%</td><td>13%</td><td></td><td>The company maintains a robust balance sheet, giving flexibility to pursue growth and/or increase cash shareholder returns. We see company offering volume growth prospects for iron ore and lithium in particular, however this comes with some execution risk.</td></tr><tr><td>11</td><td>FMG</td><td>UW</td><td>20</td><td>6% 50% 44%</td><td>20.53</td><td>18.85</td><td>-8%</td><td>6.4</td><td>4%</td><td>4%</td><td>5%</td><td></td><td>FMG continues to have strong cash generation through its Hematite operations, supporting attractive dividends yields, however we think this is more than fairly valued currently.</td></tr><tr><td>12</td><td>SFR</td><td>UW</td><td>100</td><td>69% 15% 15%</td><td>19.28</td><td>16.00</td><td>-17%</td><td>4.9</td><td>10%</td><td>4%</td><td>-34%</td><td></td><td>Despite opportunities to extend reserve lives at Motheo and MATSA, and development potential at Black Butte, we see the market more than pricing this in with downside to our base case valuation and probability-weighted price target.</td></tr><tr><td>13</td><td>IGO</td><td>UW</td><td>100</td><td>31% 62% 8%</td><td>8.98</td><td>6.85</td><td>-24%</td><td>26.9</td><td>1%</td><td>0%</td><td>-79%</td><td></td><td>IGO offers diversified exposure to clean energy metals, and despite seeing value in this theme, we think this is more than accounted for in the current stock price. We also remain cautious on acquisition risks, with the Nova Operation end of life fast approaching in CY26 and minority Greenbushes stake.</td></tr></table>

Source: MS, Thomson Reuters. Order of Preference considers relative upside/downside to TP, relative market capitalization, relative risk-reward balance and timing of potential performance drivers. Green shading on company metrics identifies equities with values more favourable than the weighted average. Consensus Rating cell highlighted in orange is a contrarian call for the respective equity. IGO EV/EBITDA multiple includes IGO's share of lithium EBITDA.  
Source: Refinitiv, MS. Note: Share prices as of June 5, 2026.

# ASX Coverage Valuation Tables

## Base Case

Exhibit 3: Base case valuation multiples and key metrics: ASX miners under MS coverage

<table><tr><td rowspan="2"></td><td rowspan="2">Rating</td><td rowspan="2">Year ending</td><td rowspan="2">FX</td><td rowspan="2">Base Case Valuation (A$)</td><td rowspan="2">Market Cap (mn)</td><td rowspan="2">EV (mn)</td><td colspan="2">P/E</td><td colspan="2"> $EV/EBITDA^*$ </td><td colspan="2">FCF Yield</td><td colspan="2">Dividend Yield</td><td colspan="2">Gearing</td></tr><tr><td>FY27/CY26</td><td>FY28/CY27</td><td>FY27/CY26</td><td>FY28/CY27</td><td>FY27/CY26</td><td>FY28/CY27</td><td>FY27/CY26</td><td>FY28/CY27</td><td>FY27/CY26</td><td>FY28/CY27</td></tr><tr><td colspan="17">Diversified</td></tr><tr><td>BHP</td><td>OW</td><td>June</td><td>USD</td><td>56.90</td><td>219,558</td><td>252,011 e</td><td>15.6</td><td>16.7</td><td>7.9</td><td>9.0</td><td>4.8%</td><td>4.0%</td><td>3.8%</td><td>3.6%</td><td>14%</td><td>15%</td></tr><tr><td>Rio Tinto Ltd.</td><td>EW</td><td>December</td><td>USD</td><td>147.50</td><td>211,375</td><td>255,705 e</td><td>14.7</td><td>15.2</td><td>8.7</td><td>8.6</td><td>3.8%</td><td>4.5%</td><td>4.1%</td><td>4.0%</td><td>16%</td><td>13%</td></tr><tr><td colspan="17">Bulks</td></tr><tr><td>Fortescue Metals Group</td><td>UW</td><td>June</td><td>USD</td><td>18.95</td><td>44,612</td><td>45,752 e</td><td>17.3</td><td>14.4</td><td>7.1</td><td>6.3</td><td>3.8%</td><td>4.6%</td><td>3.8%</td><td>4.6%</td><td>5%</td><td>4%</td></tr><tr><td>Deterra Royalties</td><td>OW</td><td>June</td><td>AUD</td><td>4.17</td><td>2,333</td><td>2,422 e</td><td>15.1</td><td>15.1</td><td>10.7</td><td>10.6</td><td>6.2%</td><td>7.2%</td><td>5.0%</td><td>5.0%</td><td>31%</td><td>14%</td></tr><tr><td>Whitehaven Coal</td><td>OW</td><td>June</td><td>AUD</td><td>9.35</td><td>7,800</td><td>8,664 e</td><td>8.3</td><td>9.4</td><td>4.2</td><td>4.7</td><td>9.8%</td><td>-1.4%</td><td>6.8%</td><td>5.3%</td><td>12%</td><td>16%</td></tr><tr><td colspan="17">Base Metals</td></tr><tr><td>South32</td><td>OW</td><td>June</td><td>USD</td><td>3.90</td><td>14,698</td><td>14,437 e</td><td>9.6</td><td>11.3</td><td>5.6</td><td>6.4</td><td>4.5%</td><td>1.5%</td><td>3.8%</td><td>3.3%</td><td>-2%</td><td>2%</td></tr><tr><td>Sandfire Resources</td><td>UW</td><td>June</td><td>USD</td><td>11.90</td><td>6,235</td><td>5,617 e</td><td>13.9</td><td>17.6</td><td>5.2</td><td>5.8</td><td>9.7%</td><td>9.8%</td><td>3.6%</td><td>2.8%</td><td>-34%</td><td>-65%</td></tr><tr><td>IGO Ltd</td><td>UW</td><td>June</td><td>AUD</td><td>5.80</td><td>6,800</td><td>5,638 e</td><td>13.3</td><td>15.8</td><td>6.8</td><td>8.9</td><td>24.4%</td><td>13.2%</td><td>3.0%</td><td>5.8%</td><td>-79%</td><td>-74%</td></tr><tr><td colspan="17">Other</td></tr><tr><td>Iluka Resources</td><td>OW</td><td>December</td><td>AUD</td><td>7.30</td><td>3,354</td><td>4,762 e</td><td>NM</td><td>NM</td><td>28.9</td><td>14.2</td><td>-10.8%</td><td>-19.6%</td><td>2.3%</td><td>0.7%</td><td>41%</td><td>49%</td></tr><tr><td>Pilbara Minerals</td><td>EW</td><td>June</td><td>AUD</td><td>4.30</td><td>19,204</td><td>18,108 e</td><td>25.0</td><td>36.3</td><td>13.4</td><td>18.1</td><td>2.0%</td><td>-0.9%</td><td>0.5%</td><td>0.0%</td><td>-40%</td><td>-22%</td></tr><tr><td>Lynas Rare Earths</td><td>EW</td><td>June</td><td>AUD</td><td>15.10</td><td>17,852</td><td>16,155 e</td><td>29.3</td><td>24.6</td><td>17.4</td><td>14.6</td><td>3.0%</td><td>4.0%</td><td>0.0%</td><td>0.0%</td><td>-67%</td><td>-95%</td></tr><tr><td>Boss Energy</td><td>OW</td><td>June</td><td>USD</td><td>1.00</td><td>374</td><td>316 e</td><td>7.4</td><td>7.8</td><td>3.8</td><td>3.8</td><td>5.4%</td><td>-0.4%</td><td>0.0%</td><td>0.0%</td><td>-10%</td><td>-8%</td></tr><tr><td>Paladin Energy</td><td>OW</td><td>June</td><td>USD</td><td>8.80</td><td>3,512</td><td>3,330 e</td><td>29.6</td><td>28.7</td><td>22.8</td><td>25.5</td><td>2.7%</td><td>-1.3%</td><td>0.0%</td><td>0.0%</td><td>-8%</td><td>-1%</td></tr></table>

Source: MS estimates. Note: \* IGO EBITDA includes IGO's share of lithium EBITDA for EV/EBITDA calculation and IGO FCF Yield includes dividends received from associates. Prices as of June 5, 2026.

## Spot Case

Exhibit 4: Spot case valuation multiples and key metrics: ASX miners under MS coverage

<table><tr><td rowspan="2"></td><td rowspan="2">Rating</td><td rowspan="2">Year Ending</td><td rowspan="2">Close Price (A$)</td><td rowspan="2">Price Target (A$)</td><td rowspan="2">FX</td><td rowspan="2">Valuation at Spot (A$)</td><td rowspan="2">Market Cap (mn)</td><td rowspan="2">EV (mn)</td><td colspan="2">P/E</td><td colspan="2">EV/EBITDA</td><td colspan="2">FCF Yield</td><td colspan="2">Dividend Yield</td><td colspan="2">Gearing</td></tr><tr><td>FY27/CY26</td><td>FY28/CY27</td><td>FY27/CY26</td><td>FY28/CY27</td><td>FY27/CY26</td><td>FY28/CY27</td><td>FY27/CY26</td><td>FY28/CY27</td><td>FY27/CY26</td><td>FY28/CY27</td></tr><tr><td colspan="19">Diversified</td></tr><tr><td>BHP</td><td>OW</td><td>June</td><td>61.24 AUD</td><td>67.50</td><td>USD</td><td>61.85</td><td>219,558</td><td>252,011</td><td>19.3</td><td>18.6</td><td>7.2</td><td>7.3</td><td>5.8%</td><td>5.6%</td><td>4.4%</td><td>4.5%</td><td>12%</td><td>12%</td></tr><tr><td>Rio Tinto Ltd.</td><td>EW</td><td>December</td><td>184.58 AUD</td><td>171.50 AUD</td><td>USD</td><td>151.50</td><td>211,375</td><td>255,705</td><td>14.3</td><td>13.3</td><td>8.3</td><td>7.6</td><td>4.2%</td><td>5.7%</td><td>4.3%</td><td>4.6%</td><td>15%</td><td>11%</td></tr><tr><td colspan="19">Bulks</td></tr><tr><td>Fortescue Metals Group</td><td>UW</td><td>June</td><td>20.53 AUD</td><td>18.85 AUD</td><td>USD</td><td>20.15</td><td>44,612</td><td>45,752</td><td>12.8</td><td>11.1</td><td>6.3</td><td>5.7</td><td>5.0%</td><td>5.8%</td><td>4.6%</td><td>5.3%</td><td>3%</td><td>2%</td></tr><tr><td>Deterra Royalties</td><td>OW</td><td>June</td><td>4.40</td><td>4.45</td><td>AUD</td><td>4.40</td><td>2,333</td><td>2,422</td><td>13.6</td><td>13.6</td><td>9.8</td><td>9.7</td><td>6.5%</td><td>7.8%</td><td>5.4%</td><td>5.4%</td><td>30%</td><td>11%</td></tr><tr><td>Whitehaven Coal</td><td>OW</td><td>June</td><td>9.37</td><td>9.55</td><td>AUD</td><td>11.00</td><td>7,800</td><td>8,664</td><td>7.3</td><td>5.5</td><td>4.3</td><td>3.7</td><td>8.7%</td><td>2.6%</td><td>6.5%</td><td>7.6%</td><td>13%</td><td>13%</td></tr><tr><td colspan="19">Base Metals</td></tr><tr><td>South32</td><td>OW</td><td>June</td><td>4.63 AUD</td><td>4.85 AUD</td><td>USD</td><td>5.00</td><td>14,698</td><td>14,437</td><td>7.8</td><td>7.6</td><td>4.5</td><td>4.5</td><td>8.0%</td><td>6.0%</td><td>5.0%</td><td>5.1%</td><td>-6%</td><td>-6%</td></tr><tr><td>Sandfire Resources</td><td>UW</td><td>June</td><td>19.28 AUD</td><td>16.00 AUD</td><td>USD</td><td>15.15</td><td>6,235</td><td>5,617</td><td>15.6</td><td>15.0</td><td>4.5</td><td>4.1</td><td>11.4%</td><td>12.7%</td><td>4.4%</td><td>4.6%</td><td>-40%</td><td>-77%</td></tr><tr><td>IGO Ltd</td><td>UW</td><td>June</td><td>8.98</td><td>6.85</td><td>AUD</td><td>8.25</td><td>6,800</td><td>5,638</td><td>8.7</td><td>7.4</td><td>5.0</td><td>4.7</td><td>30.3%</td><td>24.6%</td><td>6.2%</td><td>11.5%</td><td>-95%</td><td>-89%</td></tr><tr><td colspan="19">Other</td></tr><tr><td>Iluka Resources</td><td>OW</td><td>December</td><td>7.75</td><td>7.95</td><td>AUD</td><td>5.95</td><td>3,354</td><td>4,762</td><td>NM</td><td>NM</td><td>NM</td><td>27.7</td><td>-13.3%</td><td>-23.3%</t

[中间内容因长度限制已省略]

Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

MS Hong Kong Securities Limited is the liquidity provider/market maker for securities of Aluminum Corp. of China Ltd., China Hongqiao Group, China Shenhua Energy, Ganfeng Lithium Co. Ltd., Jiangxi Copper, MMG Ltd, Yankuang Energy Group Co Ltd listed on the Stock Exchange of Hong Kong Limited. An updated list can be found on HKEx website: http://www.hkex.com.hk.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Australia Materials

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/05/2026)</td></tr><tr><td colspan="3">Rahul Anand, CFA</td></tr><tr><td>BHP Group Ltd (BHPB.L)</td><td>O (09/19/2024)</td><td>3,127p</td></tr><tr><td>BHP Group Ltd (BHGJ.J)</td><td>O (09/19/2024)</td><td>ZAc 69,531</td></tr><tr><td>BHP Group Ltd (BHP.AX)</td><td>O (09/19/2024)</td><td>A$61.24</td></tr><tr><td>Boss Energy Ltd (BOE.AX)</td><td>O (01/16/2026)</td><td>A$1.28</td></tr><tr><td>Deterra Royalties Ltd (DRR.AX)</td><td>O (01/16/2026)</td><td>A$4.40</td></tr><tr><td>Fortescue Metals Group Ltd. (FMG.AX)</td><td>U (01/16/2026)</td><td>A$20.53</td></tr><tr><td>IGO Ltd (IGO.AX)</td><td>U (07/15/2025)</td><td>A$8.98</td></tr><tr><td>Iluka Resources Ltd (ILU.AX)</td><td>O (05/22/2025)</td><td>A$7.75</td></tr><tr><td>Lynas Rare Earths (LYC.AX)</td><td>E (04/14/2026)</td><td>A$18.16</td></tr><tr><td>Mineral Resources Limited (MIN.AX)</td><td>++</td><td>A$67.57</td></tr><tr><td>Paladin Energy Ltd (PDN.AX)</td><td>O (10/08/2025)</td><td>A$11.05</td></tr><tr><td>PLS Group Ltd (PLS.AX)</td><td>E (04/14/2026)</td><td>A$5.91</td></tr><tr><td>Rio Tinto Limited (RIO.AX)</td><td>E (04/09/2025)</td><td>A$184.58</td></tr><tr><td>Sandfire Resources Ltd (SFR.AX)</td><td>U (12/16/2024)</td><td>A$19.28</td></tr><tr><td>South32 Ltd (S32.AX)</td><td>O (12/16/2024)</td><td>A$4.63</td></tr><tr><td>South32 Ltd (S32J.J)</td><td>O (12/16/2024)</td><td>ZAc 5,364</td></tr><tr><td>Whitehaven Coal Ltd (WHC.AX)</td><td>O (04/14/2026)</td><td>A$9.37</td></tr><tr><td colspan="3">Shannon J Sinha</td></tr><tr><td>Nickel Industries (NIC.AX)</td><td>E (04/09/2025)</td><td>A$1.02</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
