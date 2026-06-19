你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

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
| Elec Pwr. & Gas 

[中间内容因长度限制已省略]

mance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All

Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 18 Jun 2026 07:26 PM JST

Disseminated 18 Jun 2026 07:28 PM JST
"""
