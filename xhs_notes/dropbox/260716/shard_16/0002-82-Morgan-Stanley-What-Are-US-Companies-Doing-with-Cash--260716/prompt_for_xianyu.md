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
<table><tr><td colspan="2">MS &amp; CO. LLC</td></tr><tr><td colspan="2">Todd Castagno, CFA, CPA</td></tr><tr><td colspan="2">GVAT Strategist</td></tr><tr><td>Todd.Castagno@morganstanley.com</td><td>+1 212 761-6893</td></tr><tr><td colspan="2">Clinton Chang, CFA, CPA</td></tr><tr><td colspan="2">GVAT Strategist</td></tr><tr><td>Clinton.Chang@morganstanley.com</td><td>+1 212 761-1185</td></tr><tr><td colspan="2">Kate Konetzke, CFA, CPA</td></tr><tr><td colspan="2">GVAT Strategist</td></tr><tr><td>Kate.Konetzke@morganstanley.com</td><td>+1 212 761-3457</td></tr><tr><td colspan="2">Mariah Thompson</td></tr><tr><td colspan="2">GVAT Strategist</td></tr><tr><td>Mariah.Thompson@morganstanley.com</td><td>+1 212 761-1147</td></tr></table>

July 16, 2026 12:55 AM GMT

Global Valuation, Accounting & Tax | North America

# What Are US Companies Doing with Cash?

Cash continues its ascent, while the cash/EV ratio and FCF yield moved in the opposite direction, hitting their 20-year lows of 3.3% and 2.6%, respectively. Companies continue to pour money earned and raised into growth capex and consensus believes that margins will continue expanding.

The Russell 1000 cash balance grew to \$2.3 trillion, as its cash/EV ratio continued its path lower to 3.3%. Most of the cash is held in the Information Technology, Consumer Discretionary, and Communication Services sectors. >\$50 billion market cap companies such as ABNB, NKE, NEM, INTU, MDT, EW, VRTX, HPE, ROST, and DDOG have robust levels of cash. Exhibit 5 contains the full list of companies with ample cash balances.

In 1Q26, companies generated \$1.7T of free cash flow, while the FCF yield fell to +2.6%. Operating cash flows increased to \$3.0T (+20.6% y/y) as capex increased by +27.1% y/y to \$1.3T. The Russell 1000 consensus NTM margin estimate increased to \~16.4% at the end of 1Q26.

Companies with ample FCF are self-financing and may better withstand any deeper or prolonged corrections in the market. >\$50B market cap companies with expected strong FCF growth include F, HPE, DASH, NKE, NEM, AMGN, DDOG, EW, MDT, and ABNB. See Exhibit 13 for additional companies that screen well on a FCF growth basis.

Total shareholder return (net buybacks + dividends) increased to \$2.0T (+2.8% q/q and +8.0% y/y). \$800B of dividends and \$1.2T of net buybacks. Exhibit 18 contains Russell 1000 companies with a total shareholder return of at least 7.5%, including >\$50B market cap companies such as ACN, CRM, C, WFC, TFC, GM, JCI, and BAC.

The cash conversion cycle (CCC) slowed over the past quarter and currently stands at 84 days, up +1 day q/q. The CCC increased due to less favorable days inventory outstanding. Exhibit 21, Exhibit 22, Exhibit 23, and Exhibit 24 contain CCC ideas based on the strongest CCC, weakest CCC, and greatest y/y changes (largest percentage increases and decreases).

Interest Rates. As interest rates have fallen, every sector except Communication Services increased their debt levels over the past quarter. Utilities, Real Estate, Financials, and Consumer Discretionary increased their debt the most versus a year ago. CLX, BG, PSX, MAA, ADM, CPT, SWK, MKC, ECHO, SMCI, R, CRWV, GPC, and SBAC are >\$10B market cap companies that may have near-term refinancing needs (Exhibit 27)

Exhibit 1 : Industry Trends (y/y quarterly changes)

<table><tr><td>Industry Group</td><td>CFO</td><td>Capex</td><td>FCF</td><td>Dividends</td><td>Buybacks</td></tr><tr><td>Autos &amp; Comp</td><td>▼</td><td>—</td><td>▼</td><td>▼</td><td>▼</td></tr><tr><td>Banks</td><td></td><td></td><td></td><td>▲</td><td>▲</td></tr><tr><td>Capital Goods</td><td>▲</td><td>▲</td><td>▲</td><td>—</td><td>—</td></tr><tr><td>Prof Svcs</td><td>▲</td><td>—</td><td>▲</td><td>▲</td><td>▲</td></tr><tr><td>Retailing</td><td>▲</td><td>▲</td><td>▼</td><td>—</td><td>▲</td></tr><tr><td>Cons Durables</td><td>▼</td><td>▲</td><td>▲</td><td>▼</td><td>▼</td></tr><tr><td>Cons Services</td><td>▲</td><td>—</td><td>▲</td><td>▲</td><td>▲</td></tr><tr><td>Staples</td><td>—</td><td>▲</td><td>▼</td><td>▼</td><td>▼</td></tr><tr><td>Energy</td><td>▼</td><td>▲</td><td>▼</td><td>▲</td><td>▼</td></tr><tr><td>Div Fin&#x27;ls</td><td></td><td></td><td></td><td>▲</td><td>▲</td></tr><tr><td>Food &amp; Bev</td><td>▲</td><td>—</td><td>▲</td><td>▲</td><td>▼</td></tr><tr><td>Health Care</td><td>▲</td><td>—</td><td>▲</td><td>—</td><td>—</td></tr><tr><td>Household Prod</td><td>▲</td><td>▲</td><td>▲</td><td>—</td><td>▼</td></tr><tr><td>Insurance</td><td></td><td></td><td>▲</td><td>▲</td><td>▲</td></tr><tr><td>Materials</td><td>▲</td><td>▼</td><td>▲</td><td>▲</td><td>—</td></tr><tr><td>Media</td><td>▲</td><td>▲</td><td>▼</td><td>▲</td><td>▼</td></tr><tr><td>Pharma &amp; Biotech</td><td>▲</td><td>—</td><td>▲</td><td>—</td><td>▲</td></tr><tr><td>Real Estate</td><td></td><td></td><td></td><td>—</td><td>▲</td></tr><tr><td>Semiconductors</td><td>▲</td><td>▲</td><td>▲</td><td>▲</td><td>▲</td></tr><tr><td>Software</td><td>▲</td><td>▲</td><td>▼</td><td>▲</td><td>▲</td></tr><tr><td>Tech Hardware</td><td>▲</td><td>▲</td><td>▲</td><td>▲</td><td>▼</td></tr><tr><td>Telecom</td><td>▼</td><td>▲</td><td>▼</td><td>—</td><td>▲</td></tr><tr><td>Transportation</td><td>▲</td><td>—</td><td>▲</td><td>—</td><td>▼</td></tr><tr><td>Utilities</td><td>—</td><td>▲</td><td>▼</td><td>▲</td><td>▲</td></tr></table>

Note: Russell 1000 universe. y/y changes are calculated by comparing 1Q26 vs 1Q25. >5.0% YoY increase indicated by an up arrow, +5.0% to -5% YoY change denoted by a flat trend line, and <-5.0% YoY marked by a down arrow.
Source: FactSet and MS.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

## Recent Global Valuation, Accounting & Tax Research:

\- Snapshot: SBC is Back (25 Jun 2026)

• OBBBA Benefits Still Ahead (11 Jun 2026)

• NOLs: Spinning Your Wheels? (10 Jun 2026)

• AI: Charting Recent Trends (9 Jun 2026)

• The State of Stock-Based Compensation (8 Jun 2026)

\- Snapshot: New Income Tax Disclosures (3 Jun 2026)

• Dividend Playbook Quarterly (27 May 2026)

• 2026 US Corporate Pensions (22 May 2026)

\- Snapshot: Spin-Off Happenings (19 May 2026)

Cash Still Climbing

Russell 1000 companies' cash marched higher this quarter, growing its balance to \~\$2.3 trillion as its cash/EV ratio fell further to \~3.3%. Information Technology (29.9%), Consumer Discretionary (18.8%), Communication Services (15.4%), and Health Care (11.4%) account for approximately three quarters of the Russell 1000 cash (ex-Financials, Real Estate, and Utilities).

Exhibit 2: Cash and Equivalents (USD in billions)  
![](images/f5b07c7579f7902a2dae08c9f8d73d20688e35dfae604bf9c4ba757049f496ba.jpg)  
Note: Russell 1000 universe, excluding Financials, Real Estate, and Utilities sectors. Source: FactSet and MS.

Exhibit 3: Cash by Industry Group (1Q26)  
![](images/2cda98480e2a8434d1139a8f5d3cb5f8d06ecc05cdb9b6364d6e72514f3648bd.jpg)  
Note: Russell 1000 universe, excluding Financials, Real Estate, and Utilities sectors. Source: FactSet and MS.

Exhibit 4: y/y Quarterly Change in Cash  
![](images/c5d14bec4719f96afc2773c2267b1bbfebefae3a08afd70ff2c89ddaa2b80f3f.jpg)  
Note: Russell 1000 universe, excluding Financials, Real Estate, and Utilities sectors. Source: FactSet and MS.

## Screen #1. Fortress Balance Sheets

Here we've identified companies with strong balance sheets and sufficient liquidity, that also generate excess returns over their cost of capital. With liquidity and solvency to run operations and service debt, these stocks could have better downside protection than the average.

## Screening Criteria:

• Russell 1000 companies, excluding Financials, Real Estate, and Utilities sectors

\- Cash / EV >5.0%

\- Positive FCF growth CAGR expected over the next two years, with positive growth in each year

\- $>10.0\%$ return on invested capital expected in each of the next two years

\- Current ratio (current assets / current liabilities) >1.0x

\- Low leverage (debt / equity) <2.5x

• Investment grade credit rating

\- Excludes companies with negative equity

Note: This is a quantitative screen and qualitative assessment is warranted. Additionally, Apple [AAPL] was quantitatively excluded from this screen, despite having one of the strongest balance sheets around. Apple holds \$45.6 billion of cash, \$22.9 billion of short-term securities, and \$78.1 billion of long-term investments, with the majority of its long-term investments held in corporate debt securities (46.3%), mortgage- and asset-backed securities (30.4%), and U.S. Treasuries (14.5%).

Exhibit 5: Strong Balance Sheets

<table><tr><td>Ticker</td><td>Company</td><td>Sector</td><td>Market Cap ($M)</td><td>Cash / EV</td><td>Debt / Equity</td><td>Current Ratio</td><td>FCF Growth FY1</td><td>FCF Growth FY2</td><td>ROIC FY1</td><td>ROIC FY2</td><td>YTD Total Return</td></tr><tr><td>VEEV</td><td>Veeva Systems Inc.</td><td>Health Care</td><td>31,366</td><td>29.4%</td><td>0.0x</td><td>4.7x</td><td>12.4%</td><td>13.5%</td><td>16.8%</td><td>14.5%</td><td>-13.5%</td></tr><tr><td>PATH</td><td>UiPath, Inc.</td><td>Info Tech</td><td>6,186</td><td>25.8%</td><td>0.0x</td><td>2.2x</td><td>12.5%</td><td>14.8%</td><td>18.8%</td><td>18.9%</td><td>-27.2%</td></tr><tr><td>ESTC</td><td>Elastic NV</td><td>Info Tech</td><td>6,478</td><td>23.2%</td><td>0.5x</td><td>1.6x</td><td>27.6%</td><td>23.6%</td><td>16.0%</td><td>16.3%</td><td>-17.4%</td></tr><tr><td>INCY</td><td>Incyte Corporation</td><td>Health Care</td><td>22,951</td><td>20.3%</td><td>0.0x</td><td>3.7x</td><td>5.2%</td><td>28.9%</td><td>23.6%</td><td>21.2%</td><td>16.3%</td></tr><tr><td>HUBS</td><td>HubSpot, Inc.</td><td>Info Tech</td><td>10,739</td><td>17.7%</td><td>0.1x</td><td>1.5x</td><td>27.1%</td><td>19.1%</td><td>27.2%</td><td>24.4%</td><td>-47.7%</td></tr><tr><td>COLM</td><td>Columbia Sportswear Co.</td><td>Cons Disc</td><td>3,207</td><td>16.5%</td><td>0.3x</td><td>3.1x</td><td>18.4%</td><td>4.2%</td><td>11.5%</td><td>12.0%</td><td>14.9%</td></tr><tr><td>ZS</td><td>Zscaler, Inc.</td><td>Info Tech</td><td>24,594</td><td>15.5%</td><td>0.8x</td><td>1.8x</td><td>7.2%</td><td>21.4%</td><td>15.9%</td><td>15.0%</td><td>-32.4%</td></tr><tr><td>ABNB</td><td>Airbnb, Inc.</td><td>Cons Disc</td><td>86,972</td><td>15.2%</td><td>0.3x</td><td>1.4x</td><td>13.8%</td><td>11.5%</td><td>25.2%</td><td>23.1%</td><td>8.0%</td></tr><tr><td>SSNC</td><td>SS&amp;C Technologies Hldgs</td><td>Industrials</td><td>16,085</td><td>14.5%</td><td>1.1x</td><td>1.1x</td><td>2.2%</td><td>11.5%</td><td>12.6%</td><td>14.0%</td><td>-23.0%</td></tr><tr><td>NKE</td><td>NIKE, Inc. Class B</td><td>Cons Disc</td><td>63,471</td><td>13.8%</td><td>0.7x</td><td>2.0x</td><td>33.4%</td><td>13.6%</td><td>11.9%</td><td>14.7%</td><td>-31.4%</td></tr><tr><td>WDAY</td><td>Workday, Inc.</td><td>Info Tech</td><td>34,533</td><td>12.5%</td><td>0.6x</td><td>1.0x</td><td>14.3%</td><td>15.9%</td><td>25.2%</td><td>23.6%</td><td>-34.9%</td></tr><tr><td>BBY</td><td>Best Buy Co., Inc.</td><td>Cons Disc</td><td>17,700</td><td>11.1%</td><td>1.3x</td><td>1.1x</td><td>7.4%</td><td>29.2%</td><td>29.9%</td><td>29.3%</td><td>28.3%</td></tr><tr><td>AA</td><td>Alcoa Corporation</td><td>Materials</td><td>12,947</td><td>10.7%</td><td>0.4x</td><td>1.5x</td><td>41.7%</td><td>75.2%</td><td>18.6%</td><td>15.9%</td><td>-7.3%</td></tr><tr><td>ONON</td><td>On Holding AG</td><td>Cons Disc</td><td>12,492</td><td>10.5%</td><td>0.3x</td><td>3.0x</td><td>18.8%</td><td>42.6%</td><td>16.1%</td><td>16.5%</td><td>-18.8%</td></tr><tr><td>PCOR</td><td>Procore Technologies Inc</td><td>Info Tech</td><td>6,494</td><td>10.1%</td><td>0.1x</td><td>1.1x</td><td>32.0%</td><td>25.6%</td><td>19.2%</td><td>20.4%</td><td>-40.8%</td></tr><tr><td>MDB</td><td>MongoDB, Inc.</td><td>Info Tech</td><td>27,722</td><td>9.4%</td><td>0.0x</td><td>4.7x</td><td>13.5%</td><td>22.3%</td><td>15.9%</td><td>16.1%</td><td>-17.9%</td></tr><tr><td>DT</td><td>Dynatrace, Inc.</td><td>Info Tech</td><td>13,072</td><td>9.2%</td><td>0.1x</td><td>1.3x</td><td>15.2%</td><td>18.6%</td><td>19.1%</td><td>18.5%</td><td>3.9%</td></tr><tr><td>ALGN</td><td>Align Technology, Inc.</td><td>Health Care</td><td>12,781</td><td>9.0%</td><td>0.0x</td><td>1.4x</td><td>90.3%</td><td>12.0%</td><td>17.8%</td><td>18.0%</td><td>14.3%</td></tr><tr><td>NEM</td><td>Newmont Corporation</td><td>Materials</td><td>101,150</td><td>8.8%</td><td>0.2x</td><td>2.4x</td><td>33.0%</td><td>18.9%</td><td>23.9%</td><td>22.7%</td><td>-4.6%</td></tr><tr><td>INTU</td><td>Intuit Inc.</td><td>Info Tech</td><td>77,255</td><td>8.7%</td><td>0.3x</td><td>1.5x</td><td>25.1%</td><td>6.6%</td><td>23.9%</td><td>24.6%</td><td>-56.8%</td></tr><tr><td>SNA</td><td>Snap-on Incorporated</td><td>Industrials</td><td>20,960</td><td>8.4%</td><td>0.2x</td><td>3.5x</td><td>9.2%</td><td>4.4%</td><td>14.3%</td><td>14.9%</td><td>18.8%</td></tr><tr><td>EBAY</td><td>eBay Inc.</td><td>Cons Disc</td><td>49,968</td><td>8.2%</td><td>1.6x</td><td>1.2x</td><td>95.4%</td><td>3.6%</td><td>26.3%</td><td>26.5%</td><td>29.9%</td></tr><tr><td>RHI</td><td>Robert Half Inc.</td><td>Industrials</td><td>3,647</td><td>7.9%</td><td>0.2x</td><td>1.5x</td><td>23.4%</td><td>2.0%</td><td>11.7%</td><td>19.3%</td><td>35.6%</td></tr><tr><td>FLS</td><td>Flowserve Corporation</td><td>Industrials</td><td>8,894</td><td>7.8%</td><td>0.9x</td><td>2.2x</td><td>4.7%</td><td>21.2%</td><td>11.5%</td><td>11.9%</td><td>0.9%</td></tr><tr><td>NBIX</td><td>Neurocrine Biosciences, Inc.</td><td>Health Care</td><td>17,299</td><td>7.8%</td><td>0.1x</td><td>2.9x</td><td>33.2%</td><td>50.2%</td><td>18.3%</td><td>19.1%</td><td>21.3%</td></tr><tr><td>AU</td><td>Anglogold Ashanti PLC</td><td>Materials</td><td>40,572</td><td>7.7%</td><td>0.3x</td><td>2.7x</td><td>51.1%</td><td>19.9%</td><td>42.5%</td><td>39.6%</td><td>-2.4%</td></tr><tr><td>CDE</td><td>Coeur Mining, Inc.</td><td>Materials</td><td>16,488</td><td>7.6%</td><td>0.1x</td><td>3.7x</td><td>278.3%</td><td>26.5%</td><td>15.5%</td><td>16.8%</td><td>-10.2%</td></tr><tr><td>MDT</td><td>Medtronic Plc</td><td>Health Care</td><td>101,508</td><td>7.5%</td><td>0.6x</td><td>2.1x</td><td>17.3%</td><td>12.6%</td><td>10.1%</td><td>10.6%</td><td>-16.0%</td></tr><tr><td>EW</td><td>Edwards Lifesciences Corp</td><td>Health Care</td><td>51,874</td><td>7.4%</td><td>0.1x</td><td>4.4x</td><td>20.6%</td><td>25.6%</td><td>14.4%</td><td>14.8%</td><td>5.7%</td></tr><tr><td>NXT</td><td>Nextpower Inc.</td><td>Industrials</td><td>15,872</td><td>7.3%</td><td>0.0x</td><td>2.4x</td><td>11.6%</td><td>45.6%</td><td>25.6%</td><td>26.4%</td><td>20.1%</td></tr><tr><td>RDDT</td><td>Reddit, Inc.</td><td>Comm Svcs</td><td>39,131</td><td>7.2%</td><td>0.0x</td><td>12.7x</td><td>88.0%</td><td>32.4%</td><td>12.9%</td><td>12.8%</td><td>-11.6%</td></tr><tr><td>TOL</td><td>Toll Brothers, Inc.</td><td>Cons Disc</td><td>14,257</td><td>6.7%</td><td>0.3x</td><td>3.8x</td><td>199.9%</td><td>14.4%</td><td>10.6%</td><td>10.7%</td><td>13.4%</td></tr><tr><td>LOPE</td><td>Grand Canyon Education, Inc.</td><td>Cons Disc</td><td>3,951</td><td>6.5%</td><td>0.1x</td><td>2.7x</td><td>11.6%</td><td>11.0%</td><td>35.5%</td><td>29.6%</td><td>-10.4%</td></tr><tr><td>GWRE</td><td>Guidewire Software, Inc.</td><td>Info Tech</td><td>11,715</td><td>6.3%</td><td>0.5x</td><td>2.4x</td><td>23.3%</td><td>23.2%</td><td>14.6%</td><td>14.5%</td><td>-30.0%</td></tr><tr><td>VRTX</td><td>Vertex Pharmaceuticals Inc</td><td>Health Care</td><td>120,890</td><td>6.2%</td><td>0.1x</td><td>3.0x</td><td>43.6%</td><td>7.9%</td><td>21.6%</td><td>20.0%</td><td>5.1%</td></tr><tr><td>HPE</td><td>Hewlett Packard Enterprise</td><td>Info Tech</td><td>65,627</td><td>6.2%</td><td>0.8x</td><td>1.1x</td><td>263.4%</td><td>28.9%</td><td>10.2%</td><td>11.2%</td><td>107.5%</td></tr><tr><td>FFIV</td><td>F5, Inc.</td><td>Info Tech</t

[中间内容因长度限制已省略]

he reference number 149169; in the US by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products.

MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

The following authors are neither Equity Research Analysts/Strategists nor Fixed Income Research Analysts/Strategists and are not opining on or expressing recommendations on equity or fixed income securities: Todd Castagno, CFA, CPA; Clinton Chang, CFA, CPA.

© 2026 MS
"""
