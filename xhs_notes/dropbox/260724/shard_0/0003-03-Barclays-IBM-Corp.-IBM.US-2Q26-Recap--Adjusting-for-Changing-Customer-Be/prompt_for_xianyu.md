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
IBM Corp.

# 2Q26 Recap: Adjusting for Changing Customer Behavior

IBM's 2H acceleration centers on its ability to recover more of the slipped ELA deals, improve overall execution, and continued strength in distributed infrastructure, storage, Power, and the z17 mainframe cycle.

Following mgmt commentary that roughly one-third of the delayed large enterprise transactions had already closed within the first few weeks of Q3 as well as an emphasis that the customer behavior is due to demand deferral rather than demand destruction, we have more confidence around IBM's 4% y/y growth base case for FY26. That said, the timing and normalization of customer behavior away from AI infrastructure / storage / memory purchases is debatably an uncontrollable nuance to IBM's upside in 2H. We expect execution to improve in the back-half of the year, which can be an offset to this potential headwind, and IBM is tracking ahead on its productivity agenda (guiding to 100bps of operating pre-tax margin expansion and reiterating its FCF guide). We reiterate our OW rating, although lower our PT to \$262 (from \$288) to account for potentially lower upside in FY26.

The Numbers: Total revenue of \$17.2bn grew 1% y/y (1% in cc vs. cons. 3% cc) and came in -3% below cons. (\$17.86bn). Total software revenue was reported at \$7.76bn (vs. cons. \$8bn), growing 5% cc (vs. 8% cc in Q1), powered by hybrid cloud growth of 11% cc (vs. cons. 10.8% cc), automation growth of 3% cc (vs. cons. 8.5% cc), data growth of 18% cc (vs. cons. 20% cc), and transaction processing growth of -9% cc (vs. cons. -2.6% cc). Consulting revenue of \$5.33bn (vs. cons \$5.40bn) grew 1% cc (vs. 0.9% cc in Q1), and was driven by strategy and technology growth of 1% cc (vs. cons. 2% cc) and intelligent operations growth of 1% cc (vs. cons 1.3% cc). Infrastructure revenue was \$3.84bn (vs. cons \$3.97bn) growing -7% cc (vs. 11.7% cc in Q1), driven by hybrid infrastructure growth of -10% cc (vs. -2% cc), and infrastructure support growth of -1% cc (vs. cons. -6% cc). Non-GAAP gross profit margin of 59.4% was \~100bps below cons (60.4%), and Non-GAAP OM of 20.4% beat by 25bps (20.2%). Mgmt. moved FY 2026 guidance from 5% cc revenue growth to 4-5% y/y, although kept FCF growth expectations at \$1bn.

Positives: (1) Infrastructure guidance was raised from a low-to-mid single-digit y/y decline to low single-digit growth as customer CapEx spend shifts toward AI infrastructure, underscored by 37% growth in Distributed Infrastructure, IBM's strongest quarter on record. (2) Mgmt. expects strong 2H acceleration driven by normalization in ELA conversion rates and improving software transaction closures, supporting its FY26 software growth outlook of 6-8%. (3) Mgmt. maintained its FY26 free cash flow growth outlook (\~\$1B y/y increase) despite lowering revenue guidance, reflecting confidence that productivity initiatives can offset revenue headwinds.

IBM OVERWEIGHT Unchanged

U.S. Software POSITIVE Unchanged

Price Target USD 262.00 lowered -9% from USD 288.00

Price (22-Jul-26) USD 205.77  
Potential Upside/Downside +27.3%  
Source: Bloomberg, BARC

<table><tr><td>Market Cap (USD mn)</td><td>193400</td></tr><tr><td>Shares Outstanding (mn)</td><td>939.89</td></tr><tr><td>Free Float (%)</td><td>99.12</td></tr><tr><td>52 Wk Avg Daily Volume (mn)</td><td>6.7</td></tr><tr><td>Dividend Yield (%)</td><td>3.28</td></tr><tr><td>Return on Equity TTM (%)</td><td>35.93</td></tr><tr><td>Current BVPS (USD)</td><td>35.08</td></tr><tr><td colspan="2">Source: Bloomberg</td></tr></table>

Price Performance Exchange-NYSE

![](images/971f9e207a5712ea4e1ae6a977099a1ffb111bfc0a7728e60f35de784d174bd7.jpg)  
Source: IDC  
Link to BARC Live for interactive charting

## U.S. Software

Raimo Lenschow, CFA +1 212 526 2712
raimo.lenschow@BARC.com
BCI, US

Sheldon McMeans  
+1 212 526 1544  
sheldon.mcmeans@BARC.com  
BCI, US

Eamon Coughlin  
+1 212 526 6142  
eamon.coughlin@BARC.com  
BCI, US

Negatives: (1) IBM lowered its FY26 revenue guide by \~100bps to 4-5% growth due to slipping mainframe-related ELAs and weakness in Transaction Processing software, as customer capex spending shifts toward infrastructure over software. (2) Software revenue grew 5%, but growth was largely driven by the HashiCorp and Confluent acquisitions, while the core business delivered approximately 0% organic growth. (3) The FY26 outlook now relies on a meaningful 2H re-acceleration in software and ELA conversions, creating execution risk if customers continue prioritizing AI infrastructure spending over software purchases.

Potential Catalysts: Q2 earnings in October (tentative).

IBM: Quarterly and Annual EPS (USD)

<table><tr><td></td><td>2025</td><td colspan="3">2026</td><td colspan="3">2027</td><td colspan="2">Change y/y</td></tr><tr><td>FY Dec</td><td>Actual</td><td>Old</td><td>New</td><td>Cons</td><td>Old</td><td>New</td><td>Cons</td><td>2026</td><td>2027</td></tr><tr><td>Q1</td><td>1.61A</td><td>1.91A</td><td>1.91A</td><td>1.91A</td><td>2.03E</td><td>2.11E</td><td>2.07E</td><td>19%</td><td>10%</td></tr><tr><td>Q2</td><td>2.80A</td><td>2.77E</td><td>2.93A</td><td>2.97E</td><td>3.10E</td><td>3.14E</td><td>3.18E</td><td>5%</td><td>7%</td></tr><tr><td>Q3</td><td>2.65A</td><td>2.91E</td><td>2.80E</td><td>2.89E</td><td>3.07E</td><td>3.00E</td><td>3.14E</td><td>6%</td><td>7%</td></tr><tr><td>Q4</td><td>4.52A</td><td>4.77E</td><td>4.77E</td><td>4.47E</td><td>4.91E</td><td>4.89E</td><td>4.72E</td><td>6%</td><td>3%</td></tr><tr><td>Year</td><td>11.59A</td><td>12.36E</td><td>12.41E</td><td>12.20E</td><td>13.12E</td><td>13.14E</td><td>13.10E</td><td>7%</td><td>6%</td></tr><tr><td>P/E</td><td>17.8</td><td></td><td>16.6</td><td></td><td></td><td>15.7</td><td></td><td></td><td></td></tr></table>

Consensus numbers are from Bloomberg received on 22-Jul-2026; 12:50 GMT Source: BARC

Note: FY End Dec

## U.S. Software

<table><tr><td>Income statement ($mn)</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td><td>CAGR</td></tr><tr><td>Revenue</td><td>67,534</td><td>70,372</td><td>72,961</td><td>76,132</td><td>4.1%</td></tr><tr><td>EBITDA (adj)</td><td>19,151</td><td>20,553</td><td>21,375</td><td>22,070</td><td>4.8%</td></tr><tr><td>Operating profit (adj)</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td>Pre-tax income (adj)</td><td>12,714</td><td>13,842</td><td>14,599</td><td>15,685</td><td>7.2%</td></tr><tr><td>Net income (adj)</td><td>10,994</td><td>11,824</td><td>12,526</td><td>13,405</td><td>6.8%</td></tr><tr><td>EPS (adj) ($)</td><td>11.59</td><td>12.41</td><td>13.14</td><td>14.05</td><td>6.6%</td></tr><tr><td>Diluted shares (mn)</td><td>949</td><td>953</td><td>954</td><td>954</td><td>0.2%</td></tr><tr><td>DPS ($)</td><td>6.59</td><td>6.66</td><td>6.66</td><td>6.66</td><td>0.3%</td></tr></table>

<table><tr><td>Margin and return data</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td><td>Average</td></tr><tr><td>EBITDA (adj) margin (%)</td><td>28.4</td><td>29.2</td><td>29.3</td><td>29.0</td><td>29.0</td></tr><tr><td>Operating margin (adj) (%)</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td>Pre-tax (adj) margin (%)</td><td>18.8</td><td>19.7</td><td>20.0</td><td>20.6</td><td>19.8</td></tr><tr><td>Net (adj) margin (%)</td><td>16.3</td><td>16.8</td><td>17.2</td><td>17.6</td><td>17.0</td></tr><tr><td>ROIC (%)</td><td>10.9</td><td>10.8</td><td>11.0</td><td>11.2</td><td>11.0</td></tr><tr><td>ROA (%)</td><td>7.0</td><td>6.5</td><td>6.6</td><td>6.7</td><td>6.7</td></tr><tr><td>ROE (%)</td><td>32.4</td><td>26.3</td><td>23.9</td><td>22.0</td><td>26.1</td></tr></table>

<table><tr><td>Balance sheet and cash flow ($mn)</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td><td>CAGR</td></tr><tr><td>Net PP&amp;E</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td>Goodwill</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td>Cash and equivalents</td><td>13,590</td><td>11,127</td><td>19,889</td><td>30,745</td><td>31.3%</td></tr><tr><td>Total assets</td><td>151,880</td><td>158,799</td><td>167,576</td><td>178,417</td><td>5.5%</td></tr><tr><td>Short and long-term debt</td><td>61,260</td><td>61,987</td><td>61,987</td><td>61,987</td><td>0.4%</td></tr><tr><td>Other long-term liabilities</td><td>9,810</td><td>9,875</td><td>9,587</td><td>10,519</td><td>2.4%</td></tr><tr><td>Total liabilities</td><td>119,139</td><td>119,380</td><td>121,299</td><td>124,290</td><td>1.4%</td></tr><tr><td>Net debt/(funds)</td><td>46,843</td><td>49,900</td><td>41,138</td><td>30,282</td><td>-13.5%</td></tr><tr><td>Shareholders&#x27; equity</td><td>32,741</td><td>39,419</td><td>46,277</td><td>54,127</td><td>18.2%</td></tr><tr><td>Change in working capital</td><td>-4,090</td><td>-1,585</td><td>-1,023</td><td>898</td><td>N/A</td></tr><tr><td>Cash flow from operations</td><td>13,194</td><td>15,977</td><td>17,021</td><td>19,200</td><td>13.3%</td></tr><tr><td>Capital expenditure</td><td>1,617</td><td>1,822</td><td>1,910</td><td>1,993</td><td>7.2%</td></tr><tr><td>Free cash flow</td><td>14,736</td><td>15,770</td><td>17,321</td><td>18,176</td><td>7.2%</td></tr></table>

<table><tr><td>Valuation and leverage metrics</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td><td>Average</td></tr><tr><td>P/E (adj) (x)</td><td>17.8</td><td>16.6</td><td>15.7</td><td>14.6</td><td>16.2</td></tr><tr><td>EV/sales (x)</td><td>3.5</td><td>3.4</td><td>3.2</td><td>2.9</td><td>3.3</td></tr><tr><td>EV/EBITDA (adj) (x)</td><td>12.5</td><td>11.8</td><td>10.9</td><td>10.1</td><td>11.3</td></tr><tr><td>Equity FCF yield (%)</td><td>7.5</td><td>8.0</td><td>8.8</td><td>9.3</td><td>8.4</td></tr><tr><td>Dividend yield (%)</td><td>3.2</td><td>3.2</td><td>3.2</td><td>3.2</td><td>3.2</td></tr><tr><td>Net debt/EBITDA (adj) (x)</td><td>2.4</td><td>2.4</td><td>1.9</td><td>1.4</td><td>2.0</td></tr><tr><td>Total debt/capital (%)</td><td>65.2</td><td>61.1</td><td>57.3</td><td>53.4</td><td>59.2</td></tr></table>

<table><tr><td>Selected operating metrics</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td><td>CAGR</td></tr><tr><td>License revenue</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td>Maintenance revenue</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td>Services revenue</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td>Deferred revenue</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td></tr></table>

Source: Company data, Bloomberg, BARC

Price (22-Jul-2026) USD 205.77  
Price Target USD 262.00

## Why OVERWEIGHT?

IBM's portfolio of hybrid cloud infrastructure, AI and enterprise software solutions supports mission-critical workloads for large customers. IBM is expanding into higher growth software areas while seeing healthy demand for its existing solutions, providing steady growth and margin expansion, with upside growth potential coming from quantum computing.

IBM's hybrid cloud strategy could see greater interest and demand from clients as they look to modernize their IT posture while better controlling cloud costs. Further, IBM has a compelling opportunity ahead around quantum computing that could accelerate growth if successful.

## Downside case USD 151.00

IBM operates in a competitive market across many of its product areas and has expanded into adjacent markets through M&A, which creates execution risk. Further, IBM has a compelling LT growth opportunity around quantum computing that if not successful could compress multiples.

Upside/Downside scenarios  
![](images/df0bf03b4e561144f5975cc65cfe18ffd291595da45be695ad7cc004a2c56335.jpg)

## 2Q26 Results Review

IBM broadly reported mixed Q2 results that came in lower than expected across most key metrics, but this was well known due to the company's pre-announcement (IBM Corp.: Negative Q2 Pre-Announcement Requires Second Look, 7/14/26). Turning to software segment results, Hybrid Cloud (Red Hat) revenue grew $11\%$ y/y (11% ccy vs. 10% ccy in Q1), Automation +4% y/y (3% ccy vs. 7% ccy in Q1), Data +19% y/y (18% ccy vs. 16% ccy in Q1) and Transaction Processing -8% y/y (-9% ccy vs. +2% ccy in Q1). For Consulting segment revenue, Strategy and Technology grew $1\%$ y/y (1% ccy vs. 1% in Q1) and Intelligent Operations grew $1\%$ y/y (1% ccy).

## Commentary on Guidance

Mgmt lowered its FY26 total revenue growth to 4%-5% (prior: 5%+), reflecting the Q2 revenue miss driven by delayed large enterprise transactions. IBM also now expects software revenue growth of 6%-8% (prior: 10%+ y/y), infrastructure growth in the low single digits (unchanged), and consulting growth in the low-to-mid-single digits (prior: decline low-to-mid-single digits) for FY26. That said, IBM maintained its expectation for \~\$1 billion of free cash flow growth in FY26 and now expects 100bps of operating pre-tax margin expansion (due to productivity initiatives more than offsetting revenue-headwinds). For Q3, IBM expects constant-currency rev. growth consistent with its full-year outlook (\~1.5pt FX headwind from the stronger U.S. dollar), operating pre-tax margins similar to Q2 levels, and a mid-teens operating tax rate.

## Takeaways from Callback

On our callback, IBM attributed its Q2 shortfall primarily to the delay of a handful of large enterprise transactions as customers redirected spending toward AI infrastructure and other CapEx priorities, with the weakness largely due to \~20% of software revenue that remains transactional while its recurring revenue base continued to perform well (\~8% y/y ARR growth). Mgmt emphasized that the business is now approximately 80% recurring revenue and believes the delayed demand is largely timing-related rather than structural, noting that several slipped deals have already closed and that the company continues to see healthy underlying demand trends. IBM reiterated a 4% FY26 revenue growth base case, with software growth of 6%-8% remaining the key swing factor and guidance assuming pipeline conversion rates stay below historical norms. The company also pushed back on the idea that AI spending is broadly cannibalizing software budgets, arguing that customers continue to invest across infrastructure, storage, memory, and software while increasingly utilizing flexible OpEx-oriented consumption models alongside traditional ELAs. Despite the softer revenue outlook, IBM maintained its roughly \$15.7 billion free cash flow target, supported by productivity initiatives, inventory normalization expected to become a 2H tailwind.

## Estimate Changes and Valuation

We update our estimates following results and provide a summary in the table below. We maintain our Overweight rating, although lower our price target to \$262 (from \$288) based on 16x EV/CY27E uFCF (from 18x) and CY27E uFCF of \$19.1bn (prior: \$18.4bn). We lower our price target to account for less upside to IBM's FY26 and lower peer group valuation levels.

FIGURE 1. Summary of Estimate Changes

<table><tr><td></td><td colspan="3">2026E</td><td colspan="3">2027E</td></tr><tr><td>$, mn</td><td>New</td><td>Old</td><td>% Chg</td><td>New</td><td>Old</td><td>% Chg</td></tr><tr><td>Hybrid Cloud Revenue</td><td>8,174</td><td>8,179</td><td>0.0%</td><td>8,992</td><td>9,117</td><td>-1.4%</td></tr><tr><td>Automation Revenue</td><td>8,134</td><td>8,425</td><td>-3.5%</td><td>8,540</td><td>9,260</td><td>-7.8%</td></tr><tr><td>Data Revenue</td><td>7,419</td><td>7,787</td><td>-4.7%</td><td>8,145</td><td>8,576</td><td>-5.0%</td></tr><tr><td>Transaction Processing Revenue</td><td>8,273</td><td>9,009</td><td>-8.2%</td><td>8,481</td><td>9,416</td><td>-9.9%</td></tr><tr><td>Total Software Revenue</td><td>31,993</td><td>33,399</td><td>-4.2%</td><td>34,158</td><td>36,369</td><td>-6.1%</td></tr><tr><td>Total Cons

[中间内容因长度限制已省略]

 and accordingly should not be construed as such. Furthermore, this information is being made available on the basis that the recipient acknowledges and understands that the entities and securities to which it may relate have not been approved, licensed by or registered with the UAE Central Bank, the Dubai Financial Services Authority or any other relevant licensing authority or governmental agency in the UAE. The content of this report has not been approved by or filed with the UAE Central Bank or Dubai Financial Services Authority. BARC Bank PLC in the Qatar Financial Centre (Registered No. 00018) is authorised by the Qatar Financial Centre Regulatory Authority (QFCRA). BARC Bank PLC-QFC Branch may only undertake the regulated activities that fall within the scope of its existing QFCRA licence. Principal place of business in Qatar: Qatar Financial Centre, Office 1002, 10th Floor, QFC Tower, Diplomatic Area, West Bay, PO Box 15891, Doha, Qatar. Related financial products or services are only available to Business Customers as defined by the Qatar Financial Centre Regulatory Authority.

Russia: This material is not intended for investors who are not Qualified Investors according to the laws of the Russian Federation as it might contain information about or description of the features of financial instruments not admitted for public offering and/or circulation in the Russian Federation and thus not eligible for non-Qualified Investors. If you are not a Qualified Investor according to the laws of the Russian Federation, please dispose of any copy of this material in your possession.

Sustainable Investing Related Research: There is currently no globally accepted framework or definition (legal, regulatory or otherwise) of, nor market consensus as to what constitutes a ‘sustainable’, ‘ESG’, ‘green’, ‘climate-friendly’ or an equivalent company, investment, strategy or consideration or what precise attributes are required to be eligible to be categorised by such terms. This means there are different ways to evaluate a company or an investment and so different values may be placed on certain sustainability credentials as well as adverse ESG-related impacts of companies and ESG controversies. The evolving nature of sustainable investing considerations, models and methodologies means it can be challenging to definitively and universally classify a company or investment under a sustainable investing label and there may be areas where such companies and investments could improve or where adverse ESG-related impacts or ESG controversies exist. The evolving nature of sustainable finance related regulations and the development of jurisdiction-specific regulatory criteria also means that there is likely to be a degree of divergence as to the interpretation of such terms in the market. We expect industry guidance, market practice, and regulations in this field to continue to evolve.

Any information, data, image, or other content including from a third party source contained, referred to herein or used for whatsoever purpose by BARC or a third party (“Information”), in relation to any actual or potential ‘ESG’, ‘sustainable’ or equivalent objective, issue, factor or consideration is not intended to be relied upon for ESG or sustainability classification, regulatory regime or industry initiative purposes (“ESG Regimes”), unless otherwise stated. Nothing in these materials, including any images included therein, is intended to convey, suggest or indicate that BARC considers or represents any product, service, person or body mentioned in these materials as meeting or qualifying for any ESG or sustainability classification, label or similar standards that may exist under ESG Regimes. BARC has not conducted any assessment of compliance with ESG Regimes. Parties are reminded to make their own assessments for these purposes.

IRS Circular 230 Prepared Materials Disclaimer: BARC does not provide tax advice and nothing contained herein should be construed to be tax advice. Please be advised that any discussion of U.S. tax matters contained herein (including any attachments) (i) is not intended or written to be used, and cannot be used, by you for the purpose of avoiding U.S. tax-related penalties; and (ii) was written to support the promotion or marketing of the transactions or other matters addressed herein. Accordingly, you should seek advice based on your particular circumstances from an independent tax advisor.

© Copyright BARC Bank PLC (2026). All rights reserved. No part of this publication may be reproduced or redistributed in any manner without the prior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request.
"""
