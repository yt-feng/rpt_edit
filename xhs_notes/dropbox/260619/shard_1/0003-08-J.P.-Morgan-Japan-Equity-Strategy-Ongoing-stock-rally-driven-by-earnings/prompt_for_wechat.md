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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`JPM`。标题格式建议：`# JPM：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份JPM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## Japan Equity Strategy

Ongoing stock rally driven by earnings: Raising price targets to 75,000 for Nikkei 225 and 4,400 for TOPIX

With earnings-driven stock rally to continue in 2H 2026, raise our 2026 year-end targets to 75,000 for Nikkei 225 and 4,400 for TOPIX: We expect Japanese equities to stay on an upward trend in 2H 2026 and raise our 2026 year-end price targets to 75,000 for the Nikkei 225 and 4,400 for TOPIX (Figure 1 and Figure 2: FY2026E TOPIX EPS +11% YoY, P/E 17x). In 1H, TOPIX rose 18% YoY and has outperformed the MSCI World, S&P 500, and STOXX 600 indexes as of June 17 (same below). The Liberal Democratic Party's (LDP's) landslide victory in the February Lower House election heightened policy expectations. Since April, as stock markets recovered, AI semiconductor stocks have led the way, and the Nikkei 225 (with AI-related stocks accounting for about 50% of its market capitalization) is up 39% YTD, significantly outpacing TOPIX's return (with AI-related stocks accounting for about 30%: Figure 6). We have had a bullish stance since the start of the year, and moved early to raise our price targets in a market driven by AI semiconductors since April (Nikkei 225 to 70,000 and TOPIX to 4,300; see our April 22 report). However, with a faster pace than we expected in the global AI supercycle, as of mid-June, the Nikkei 225 had reached our target mid-year, while the remaining upside for TOPIX is just 7-8%. Although the pace of share price gains was rapid in 1H, semiconductor and semiconductor production equipment (SPE) companies, such as Kioxia and electric wire & cable manufacturers, reported strong growth in earnings (we raise our FY2026 EPS estimate from ¥198 as of end-2025 to the current ¥234: Figure 3). Valuations (P/E, Figure 4) have cooled to the 16x level, alleviating concerns about overheating. We see upside risk to profit growth.

In 2H, inflation, the start of interest rate hikes by central banks (the US Fed's reaction function is still unclear) and geopolitical risks are the main concerns in global markets. However, AI appears to be in a supercycle, with AI inference as the main growth area and US hyperscalers' investments in data centers driving up demand for semiconductor chips, memory, and electronic components beyond market expectations. Large IPOs by SpaceX, Anthropic (planned), and OpenAI (planned) with initial public offerings on the scale of a trillion dollars this year are also likely to support risk-taking sentiment in the market. In the Japanese market, investors are concerned about fiscal policy, rising long-term interest rates, and depreciation pressure on the yen. We believe such negative factors are outweighed by positive factors, such as structural changes (corporate reforms improving balance sheets and profitability, larger fund inflows into Japanese equities), growth strategies, and tailwinds from the AI semiconductor cycle.

Risks include excessive yen depreciation and sharp increases in interest rates: Rising interest rates and yen weakness are risks for Japanese equities. As the BoJ has noted, however, underlying inflation is finally approaching 2%, so the rate hikes might accelerate going forward. While the Fed may turn more hawkish under Chairman Warsh (an increase in the number of hikes priced in by the OIS market), this might not be so straightforward. However, if a more hawkish Fed results in a moderate correction of yen depreciation, it would be a positive factor for Japanese equities. Yen depreciation beyond the ¥160/\$ level would be negative for households, due to stronger domestic inflation from high pass-through, and also for capital markets through the lens of equity investment returns for overseas investors. Although the

## Equity Strategy

## Rie Nishihara AC

(81-3) 6736-8629

rie.nishihara@JPM.com

JPM Securities Japan Co., Ltd.

## Yong Guo, CFA

(81-3) 6736-8623

yong.guo@JPM.com

JPM Securities Japan Co., Ltd.

## Mansi Das

(91) 2261 573343

mansi.das@jpmchase.com

JPM India Private Limited

## Mislav Matejka, CFA

(44-20) 7134-9741

mislav.matejka@JPM.com

JPM Securities plc

## Rajiv Batra

(65) 6882-8151

rajiv.j.batra@JPM.com

JPM Securities Singapore Private Limited

## Dubravko Lakos-Bujas

(1-212) 622-3601

dubravko.lakos-bujas@JPM.com

JPM Securities LLC

market is concerned about fiscal expansion, we do not expect fiscal policy outlined in the upcoming release of the Basic Policy on Economic and Fiscal Management and Reform to immediately trigger an uncontrollable surge in long-term interest rates, owing to economic growth under inflation. In this environment, we expect a faster pace of growth in corporate earnings driven by corporate business restructuring and capital policy, and a clearer inflow of funds to Japanese equities from individual investors, pension funds, and financial institutions to serve as catalysts for the Japanese equity market.

Equity investment strategy for 2H 2026: We expect the global AI revolution and the AI-driven market to continue in 2H. We therefore believe AI semiconductors and financials should be positioned as the core of Japanese equity portfolios. If the Middle East situation stabilizes, we expect a short-term share price rebound in the construction, transportation, chemicals, and defense sectors, helped by a decline in crude oil prices. We also expect the food sector to recover, as higher crude oil prices will probably be passed onto consumers and the consumption tax on food looks likely to be cut this summer. In the 1H results announcement season this autumn, we expect share prices to rebound, driven by upward revisions to earnings estimates for large-cap banks, automakers, and the defense sector. We believe these factors could lead to a partial correction of the AI-dominated market toward year-end. Even as the AI-driven market continues unabated, we observe widening differences in signs of overheating among business domains within the AI semiconductor space. Toward year-end, we expect higher-than-expected earnings for SPE and memory makers, and we look for share prices to catch up in lagging domains, such as physical AI (Figure 7).

Figure 1: Target Prices for Japanese Equities  
![](images/a5e8cbc34036d955c1d61fe9697b3ab621093c1c191ba31f6ce833e962dbdc87.jpg)

<details>
<summary>line chart</summary>

| Date     | TOPIX (pt) | TOPIX: 4400 pt, upside +8.2% | Nikkei (rhs) | Nikkei: 75k, upside +5.6% |
|----------|------------|------------------------------|--------------|---------------------------|
| 25/10    | ~3,100     | ~4,400                       | ~3,300       | ~4,500                    |
| 25/11    | ~3,300     | ~4,400                       | ~3,400       | ~4,500                    |
| 25/12    | ~3,400     | ~4,400                       | ~3,500       | ~4,500                    |
| 26/01    | ~3,500     | ~4,400                       | ~3,600       | ~4,500                    |
| 26/02    | ~3,700     | ~4,400                       | ~3,700       | ~4,500                    |
| 26/03    | ~3,900     | ~4,400                       | ~3,800       | ~4,500                    |
| 26/04    | ~3,600     | ~4,400                       | ~3,700       | ~4,500                    |
| 26/05    | ~3,800     | ~4,400                       | ~3,900       | ~4,500                    |
| 26/06    | ~4,100     | ~4,400                       | ~4,200       | ~4,500                    |
| As of 2026/06/18 | ~4,400   | 4,400                        | ~4,500       | 75,000                    |
</details>

Source: Bloomberg Finance L.P., JPM estimates

Figure 3: TOPIX EPS Forecast  
![](images/4820348a7579a2d633f5ba92d36ad1adc715de3fb0bd6a34334f89520a0f4749.jpg)

<details>
<summary>bar chart</summary>

| Fiscal Year | Actual (JPY) | JPMе (JPY) | IBES consensus (JPY) |
| :--- | :--- | :--- | :--- |
| FY18A | 115.0 | - | - |
| FY19A | 82.0 | - | - |
| FY20A | 91.0 | - | - |
| FY21A | 139.0 | - | - |
| FY22A | 145.0 | - | - |
| FY23A | 170.0 | - | - |
| FY24A | 188.0 | - | - |
| FY25A | 210.2 | - | - |
| FY26E | 234.2 | 234.2 | 234.2 |
| FY27E | 262.3 | 262.3 | 262.3 |
As of: 2026/06/17
FY25 Act YoY: +11.2%
FY26 YoY JPMе: +11.4%; vs IBES +10.7%
FY27 YoY JPMе: +12.0%; vs IBES +11.5%
NTM YoY at 2026-end: +11.9%
7Y CAGR: +8.0%
</details>

Source: Datastream, JPM estimates  
Note: The 7-year CAGR is from FY2018 to FY2025. EPS consensus is IBES.

Figure 5: TOPIX ROE Forecast  
![](images/f6c33bb9f5e1f9d02be075fe5381ec6e47cf469b50f1faf1478ee54335c25627.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Fiscal Year | ROE (%) | ROE (excluding FX effects) (%) |
| :--- | :--- | :--- |
| FY17 | 9.7 | 9.5 |
| FY18 | 8.7 | 8.7 |
| FY19 | 6.2 | 6.3 |
| FY20 | 6.8 | 6.8 |
| FY21 | 9.0 | 8.7 |
| FY22 | 8.6 | 7.8 |
| FY23 | 9.2 | 9.0 |
| FY24 | 9.4 | 9.1 |
| FY25 | 9.6 | 9.5 |
| FY26e | 10.0 | 10.0 |
| FY27e | 10.8 | 10.8 |
| FY28e | 11.4 | 11.4 |
</details>

Source: Bloomberg Finance L.P., JPM estimates

Figure 2: Japanese Equities Outlook to End-2026 (TOPIX, Nikkei 225)

<table><tr><td rowspan="2">NT ratio:17.0x</td><td colspan="3">FY26-end</td><td colspan="5">TOPIX 12-month forward PER (x)</td></tr><tr><td>YoY</td><td>EPS</td><td>NTM EPS</td><td>16.0x</td><td>16.5x</td><td>17.0x</td><td>17.5x</td><td>18.0x</td></tr><tr><td rowspan="7">EPS growth in FY2026 and FY-end NTM EPS(expect NTM growth of 12% at FY-end)</td><td>+13%</td><td>238</td><td>266</td><td>4,250 pt72,500 Yen</td><td>4,400 pt74,500 Yen</td><td>4,450 pt76,000 Yen</td><td>4,600 pt78,000 Yen</td><td>4,750 pt80,500 Yen</td></tr><tr><td>+12%</td><td>235</td><td>263</td><td>4,200 pt71,500 Yen</td><td>4,350 pt74,000 Yen</td><td>4,450 pt75,000 Yen</td><td>4,550 pt77,500 Yen</td><td>4,700 pt79,500 Yen</td></tr><tr><td>+11%</td><td>234</td><td>262</td><td>4,200 pt71,500 Yen</td><td>4,300 pt73,500 Yen</td><td>4,400 pt75,000 Yen</td><td>4,550 pt77,000 Yen</td><td>4,650 pt79,500 Yen</td></tr><tr><td>+8%</td><td>227</td><td>254</td><td>4,050 pt69,000 Yen</td><td>4,200 pt71,500 Yen</td><td>4,250 pt72,500 Yen</td><td>4,400 pt74,500 Yen</td><td>4,500 pt77,000 Yen</td></tr><tr><td>+6%</td><td>223</td><td>249</td><td>4,000 pt68,000 Yen</td><td>4,100 pt70,000 Yen</td><td>4,200 pt71,000 Yen</td><td>4,300 pt73,500 Yen</td><td>4,450 pt75,500 Yen</td></tr><tr><td>+5%</td><td>221</td><td>247</td><td>3,950 pt67,000 Yen</td><td>4,100 pt69,500 Yen</td><td>4,150 pt70,500 Yen</td><td>4,250 pt72,500 Yen</td><td>4,400 pt74,500 Yen</td></tr><tr><td>+4%</td><td>219</td><td>245</td><td>3,900 pt66,500 Yen</td><td>4,050 pt68,500 Yen</td><td>4,100 pt70,000 Yen</td><td>4,250 pt72,000 Yen</td><td>4,350 pt74,000 Yen</td></tr></table>

Source: JPM estimates  
Note: Orange shading indicates the end-2026 target price.

Figure 4: TOPIX P/E Forecast  
![](images/b353000cd6c24eae538bbd4f2a3f94f15963fc3de3922172c5fdf64ef8226290.jpg)

<details>
<summary>line chart</summary>

| Date     | TOPIX NTM P/E (as of 26/06/17 : 16.6x) |
| -------- | ------------------------------------- |
| 23/01    | ~12.5                                 |
| 24/01    | ~14.5                                 |
| 25/01    | ~13.5                                 |
| 26/01    | ~17.5                                 |
</details>

Source: Datastream, JPM estimates  
Note: NTM P/E is based on IBES consensus.

Figure 6: 2026 Year-to-Date Performance  
![](images/53a316285ad2e49da9adb425d9596ba0baa1a4f4f7c751365a4f81ade5c04c7a.jpg)

<details>
<summary>line chart</summary>

| Date   | TOPIX | Nikkei | S&P 500 | MSCI World |
|--------|-------|--------|---------|------------|
| 01/02  | 100   | 100    | 100     | 100        |
| 01/16  | 105   | 105    | 102     | 101        |
| 01/30  | 108   | 107    | 103     | 102        |
| 02/13  | 112   | 110    | 104     | 103        |
| 02/27  | 115   | 112    | 105     | 104        |
| 03/13  | 110   | 108    | 103     | 102        |
| 03/27  | 105   | 105    | 98      | 99         |
| 04/10  | 110   | 115    | 102     | 103        |
| 04/24  | 115   | 120    | 105     | 106        |
| 05/08  | 120   | 125    | 108     | 109        |
| 05/22  | 125   | 130    | 110     | 112        |
| 06/05  | 130   | 135    | 112     | 115        |
| 06/27  | 135   | 140    | 115     | 118        |
</details>

Source: Bloomberg Finance L.P., JPM

Figure 7: Sector Allocation

<table><tr><td>GICS 11 Sector</td><td>Energy</td><td>Materials</td><td>Industrials</td><td>Consumer Discretionary</td><td>Consumer Staples</td><td>Health Care</td><td>Financials</td><td>Information Technology</td><td>Comm. Services</td><td>Utilities</td><td>Real Estate</td></tr><tr><td rowspan="4">GICS 25 Industry GroupsBlue = OWRed = UWBlack = N</td><td>Energy</td><td>Materials</td><td>Capital Goods</td><td>Automobiles &amp; Components</td><td>Consumer Staples Distr. &amp; Retail</td><td>Health Care Equip. &amp; Serv.</td><td>Banks</td><td>Software &amp; Services</td><td>Telecom Serv.</td><td>Utilities</td><td>Real Estate</td></tr><tr><td></td><td></td><td>Commercial &amp; Prof. Serv.</td><td>Consumer Durab. &amp; Appar.</td><td>Food, Beverage &amp; Tobacco</td><td>Pharms., Biotech. &amp; Life Sciences</td><td>Financial Services</td><td>Tech. Hardware &amp; Equip.</td><td>Media &amp; Entertainment</td><td></td><td></td></tr><tr><td></td><td></td><td>Transportation</td><td>Consumer Services</td><td>Household &amp; Personal Products</td><td></td><td>Insurance</td><td>Semicon. &amp; Semicon. Equip.</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>Consumer Discr. Distri. &amp; Retail</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Allocation</td><td>OW</td><td>OW</td><td>N</td><td>N</td><td>UW</td><td>UW</td><td>OW</td><td>OW</td><td>N</td><td>UW</td><td>N</td></tr></table>

Source: JPM estimates

Figure 8: EPS Estimates by TOPIX 17 Sectors  
![](images/987cbc64482bd716dd2a7066d3a2449d8eceee605a5265353fbf8de8743ad9b8.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Sector | 6/17/2026 (%) | 1M revision (%) |
| :--- | :--- | :--- |
| TOPIX | 13 | 24 |
| Elec. Pwr. & Gas | 48 | 22 |
| Energy Reso. | 44 | -5 |
| Autos & Trans. Equip. | 41 | 30 |
| Steel & Nonfer | 39 | 28 |
| Elec Appl. & Prec. | 34 | 34 |
| Foods | 26 | -15 |
| Raw & Chem. | 20 | 22 |
| Machinery | 22 | 28 |
| Comm. & Wholesale | 16 | 31 |
| Banks | 15 | 24 |
| Retail Trade | 11 | 22 |
| Real Estate | 3 | -13 |
| Const. & Mater. | 2 | 19 |
| Fin ex Bank | -1 | -10 |
| Pharmaceutical | -5 | -5 |
| Transport. & Logi. | -5 | -10 |
| IT & Service | -16 | 24 |
</details>

Source: Bloomberg Finance L.P., JPM  
Note: EPS estimates are Bloomberg consensus.

Figure 10: Net Profit Estimates for the Nikkei 225 Constituents  
![](images/8e4b415f68bd5ff540096b71e733a5a9afa20a915182478e99a6dbb8f399a613.jpg)

<details>
<summary>bubble chart</summary>

| Company                  | FY26-28 Net profit growth | 2026YTD perf |
| ------------------------ | ------------------------ | ------------ |
| Semiconductors & Equip.  | ~300%                    | ~100%        |
| Technology Hardware & Equip. | ~50%                     | ~75%         |
</details>

Source: Bloomberg Finance L.P., JPM  
Note: EPS is Bloomberg consensus. Circle size indicates index constituent weight.

Figure 9: Valuation Levels by TOPIX 17 Sectors  
![](images/265e7b45e98d37b13a7c286142337b6ac02ea52caf4f4ac109216613851a3ae7.jpg)

<details>
<summary>bar chart</summary>

| Sector | 6/17/2026 | 5/18/2026 |
| --- | --- | --- |
| TOPIX NTM PER | 2.0 | 1.5 |
| Raw & Chem. | 5.5 | 4.5 |
| Steel & Nonfer | 3.5 | 4.0 |
| Banks | 3.0 | 1.5 |
| Elec Appl. & Prec. | 3.0 | 1.5 |
| Fin ex Bank | 2.5 | 2.0 |
| Const. & Mater. | 2.0 | 1.5 |
| Machinery | 1.0 | 1.5 |
| Comm. & Wholesale | 1.0 | 3.0 |
| Transport. & Logi. | 1.0 | 1.5 |
| Pharmaceutical | 1.0 | -0.5 |
| Real Estate | 0.5 | 1.0 |
| Elec Pwr. & Gas | 0.5 | 1.0 |
| Autos & Trans. Equip. | 0.0 | 0.5 |
| Foods | -0.5 | -0.5 |
| Retail Trade | -1.0 | -1.5 |
| Energy Reso. | -2.0 | -2.5 |
| IT & Service | -4.0 | -5.0 |
</details>

Source: Bloomberg Finance L.P., JPM  
Note: PER estimates are Bloomberg consensus.

Figure 11: Net Profit Estimates for the TOPIX 500 Constituents  
![](images/1c17eecfb97777d3b52ce638fed150e2ef89435600f55239247acd3875f5c943.jpg)

<details>
<summary>bubble chart</summary>

| Category                  | FY26-28 Net profit growth |
| ------------------------- | ------------------------ |
| Semiconductors & Equip.   | ~300%                    |
| Technology Hardware & Equip. | ~50%                     |
</details>

Source: Bloomberg Finance L.P., JPM  
Note: EPS is Bloomberg consensus. Circle size indicates index constituent weight.

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companie

[中间内容因长度限制已省略]

dates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All

Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 18 Jun 2026 07:26 PM JST

Disseminated 18 Jun 2026 07:28 PM JST
"""
