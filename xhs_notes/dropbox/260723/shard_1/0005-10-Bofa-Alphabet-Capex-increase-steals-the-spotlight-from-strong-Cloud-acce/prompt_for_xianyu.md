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
Alphabet

# Capex increase steals the spotlight from strong Cloud acceleration; Buy

Reiterate Rating: BUY | PO: 430.00 USD | Price: 342.09 USD

## 2Q beat driven by Cloud upside; Search largely in-line

2Q Net Rev at \$103.6bn beat Street at \$101.1bn, driven by upside in Cloud, accelerating to 82% growth vs 65% expected. Search grew 17% y/y, and was just in line, tabling the N.T. AI upside thesis. 2Q OM at 39.3% was below Street at 40.3% impacted by higher G&A (expect some details in the 10-Q). However, Cloud margins 35.6% vs Street 31.3%, suggesting strong infrastructure returns, and limited mgn. impact from new TPU sales. 2Q EPS of \$9.11 was above Street at \$2.90 & benefited from 1x higher Other Income.

## Higher capex but ROI case strengthened by Cloud accel.

To meet capacity demand, Google is accelerating capacity deployment and increased its FY26 capex guide by \$15bn (\~8%) to \$195bn-\$205bn. While the increase drove a negative AH stock reaction, we note several data points that suggest capacity driving strong returns, including: Strong \$50bn 2Q q/q backlog growth to \$514bn, well above the \$15bn '26 capex increase, customer consumption exceeding commitments by >50% vs 45% in 1Q, GC is winning new customers at >2x the pace vs last year, and cloud margins were up 270bps q/q and almost 15pts y/y. More capacity = more sales.

## Raising 2027 net revenue by 3% and EPS by 2%

We raise revs. to reflect higher Cloud, YouTube and Network growth offset by slightly lower Search & Sub. revs. We est 93% Cloud growth in 3Q. However, we also raise Cost of Revenue reflecting higher infrastructure costs & raise share count. For 3Q we raise revenue by 3% and EPS by 1% to \$3.07 from \$3.03. For 2027, we raise net revenue by 3% to \$553bn and EPS by 2% to \$15.01. Maintain our PO of \$430 based on a higher '27 EPS & slightly lower 27x P/E multiple (vs 28x) given capex concerns for the sector.

## Another strong Qtr validates AI differentiation; Buy

A solid Q that validates that 1) Search usage and monetization remains robust despite competing AI engagement growth, 2) Gemini & TPUs remain competitive advantages, supporting Cloud margin growth & continued share gains, & 3) Incremental capex is directly accelerating growth. At the \$332 AH price, GOOG is valued at \~22x our higher '27 GAAP EPS est, in line with historical avg despite recent acceleration. Next Catalysts: public launch of Gemini 3.5 Pro, new agentic features, ramp in TPU sales. Risks include: tougher 3Q comps, social media trials, OpenAI ad ramp, flow of funds into AI IPOs

<table><tr><td>Estimates (Dec) (US$)</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>EPS</td><td>8.04</td><td>10.81</td><td>20.58</td><td>15.01</td><td>18.58</td></tr><tr><td>EPS Change (YoY)</td><td>38.6%</td><td>34.5%</td><td>90.4%</td><td>-27.1%</td><td>23.8%</td></tr><tr><td>Consensus EPS (Bloomberg)</td><td></td><td></td><td>14.50</td><td>15.57</td><td>18.66</td></tr><tr><td>Consensus EPS (Visible Alpha)</td><td></td><td></td><td>20.33</td><td>14.51</td><td>17.34</td></tr><tr><td>DPS</td><td>0.60</td><td>0.63</td><td>0.71</td><td>0.78</td><td>0.87</td></tr><tr><td>EPS (GOOG - US$)</td><td>8.04</td><td>10.81</td><td>20.58</td><td>15.01</td><td>18.58</td></tr><tr><td>DPS (GOOG - US$)</td><td>0.60</td><td>0.63</td><td>0.71</td><td>0.78</td><td>0.87</td></tr><tr><td>Valuation (Dec)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>P/E</td><td>42.5x</td><td>31.6x</td><td>16.6x</td><td>22.8x</td><td>18.4x</td></tr><tr><td>Dividend Yield</td><td>0.2%</td><td>0.2%</td><td>0.2%</td><td>0.2%</td><td>0.3%</td></tr><tr><td>EV / EBITDA*</td><td>28.5x</td><td>24.5x</td><td>18.3x</td><td>13.8x</td><td>10.6x</td></tr><tr><td>Free Cash Flow Yield*</td><td>1.7%</td><td>1.7%</td><td>-0.4%</td><td>-0.4%</td><td>0.9%</td></tr></table>

\* For full definitions of iQmethod $^{SM}$ measures, see page 13.

BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.
Refer to important disclosures on page 14 to 17. Analyst Certification on page 12. Price Objective Basis/Risk on page 12.
12997585

## 23 July 2026

Equity

## Key Changes

<table><tr><td>(US$)</td><td>Previous</td><td>Current</td></tr><tr><td>2026E Rev (m)</td><td>426,879.8</td><td>433,587.4</td></tr><tr><td>2027E Rev (m)</td><td>536,557.4</td><td>552,793.7</td></tr><tr><td>2028E Rev (m)</td><td>677,541.2</td><td>701,204.7</td></tr><tr><td>2026E EPS</td><td>19.70</td><td>20.58</td></tr><tr><td>2027E EPS</td><td>14.70</td><td>15.01</td></tr><tr><td>2028E EPS</td><td>18.12</td><td>18.58</td></tr><tr><td>2026E DPS</td><td>0.72</td><td>0.71</td></tr></table>

Justin Post

Research Analyst

BofAS

+1 415 676 3547

justin.post@bofa.com

## Nitin Bansal, CFA

Research Analyst
BofAS
+1 415 676 3551
nbansal7@bofa.com

## Stock Data

<table><tr><td>Price (NAS / NAS)</td><td>342.09 USD / 341.91 USD</td></tr><tr><td>Price Objective</td><td>430.00 USD / 430.00 USD</td></tr><tr><td>Date Established</td><td>30-Apr-2026 / 30-Apr-2026</td></tr><tr><td>Investment Opinion</td><td>B-1-7 / B-1-7</td></tr><tr><td>52-Week Range</td><td>187.82 USD - 408.61 USD</td></tr><tr><td>Market Value (mn)</td><td>4,247,047 USD</td></tr><tr><td>Free Float</td><td>98.8%</td></tr><tr><td>Average Daily Value</td><td>11334.49 USD</td></tr><tr><td>Shares Outstanding (mn)</td><td>12,415.0 / 12,415.0</td></tr><tr><td>BofA Ticker / Exchange</td><td>GOOGL / NAS</td></tr><tr><td>BofA Ticker / Exchange</td><td>GOOG / NAS</td></tr><tr><td>Bloomberg / Reuters</td><td>GOOGL US / GOOGL.OQ</td></tr><tr><td>ROE (2026E)</td><td>43.5%</td></tr><tr><td>Net Dbt to Eqty (Dec-2025A)</td><td>8.9%</td></tr></table>

GCP: Google Cloud Platform

OM: Operating Margins

AIO: AI Overviews

SOTP: Sum of the parts

## iQprofile $^{SM}$ Alphabet

## iQmethod $^{SM}$ – Bus Performance\*

Key Changes

<table><tr><td>(US$ Millions)</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Return on Capital Employed</td><td>37.2%</td><td>37.6%</td><td>40.0%</td><td>22.0%</td><td>22.3%</td></tr><tr><td>Return on Equity</td><td>35.3%</td><td>37.8%</td><td>43.5%</td><td>22.1%</td><td>21.7%</td></tr><tr><td>Operating Margin</td><td>45.8%</td><td>44.9%</td><td>47.0%</td><td>47.0%</td><td>46.6%</td></tr><tr><td>Free Cash Flow</td><td>72,764</td><td>73,266</td><td>(16,071)</td><td>(18,466)</td><td>36,815</td></tr></table>

iQmethod $^{SM}$ – Quality of Earnings\*

<table><tr><td>(US$ Millions)</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Cash Realization Ratio</td><td>1.3x</td><td>1.2x</td><td>0.7x</td><td>1.5x</td><td>1.6x</td></tr><tr><td>Asset Replacement Ratio</td><td>3.4x</td><td>4.3x</td><td>6.5x</td><td>5.9x</td><td>4.3x</td></tr><tr><td>Tax Rate</td><td>16.4%</td><td>16.8%</td><td>18.4%</td><td>16.7%</td><td>16.7%</td></tr><tr><td>Net Debt-to-Equity Ratio</td><td>1.7%</td><td>8.9%</td><td>11.1%</td><td>8.6%</td><td>6.4%</td></tr><tr><td>Interest Cover</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr></table>

Income Statement Data (Dec)

<table><tr><td>(US$ Millions)</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Sales</td><td>295,118</td><td>342,910</td><td>433,587</td><td>552,794</td><td>701,205</td></tr><tr><td>% Change</td><td>15.1%</td><td>16.2%</td><td>26.4%</td><td>27.5%</td><td>26.8%</td></tr><tr><td>Gross Profit</td><td>203,712</td><td>240,301</td><td>305,168</td><td>383,068</td><td>476,375</td></tr><tr><td>% Change</td><td>17.0%</td><td>18.0%</td><td>27.0%</td><td>25.5%</td><td>24.4%</td></tr><tr><td>EBITDA</td><td>150,486</td><td>175,128</td><td>234,771</td><td>310,713</td><td>405,545</td></tr><tr><td>% Change</td><td>21.9%</td><td>16.4%</td><td>34.1%</td><td>32.3%</td><td>30.5%</td></tr><tr><td>Net Interest &amp; Other Income</td><td>(15,360)</td><td>4,834</td><td>108,057</td><td>(32,043)</td><td>(41,343)</td></tr><tr><td>Net Income (Adjusted)</td><td>100,076</td><td>132,206</td><td>254,680</td><td>189,884</td><td>237,717</td></tr><tr><td>% Change</td><td>35.6%</td><td>32.1%</td><td>92.6%</td><td>-25.4%</td><td>25.2%</td></tr></table>

## Free Cash Flow Data (Dec)

<table><tr><td>(US$ Millions)</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Net Income from Cont Operations (GAAP)</td><td>100,118</td><td>132,170</td><td>254,626</td><td>189,882</td><td>237,726</td></tr><tr><td>Depreciation &amp; Amortization</td><td>15,311</td><td>21,136</td><td>30,914</td><td>50,736</td><td>78,836</td></tr><tr><td>Change in Working Capital</td><td>(9,343)</td><td>618</td><td>(17,865)</td><td>1,321</td><td>4,533</td></tr><tr><td>Deferred Taxation Charge</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>Other Adjustments, Net</td><td>19,213</td><td>10,789</td><td>(84,258)</td><td>40,168</td><td>57,468</td></tr><tr><td>Capital Expenditure</td><td>(52,535)</td><td>(91,447)</td><td>(199,488)</td><td>(300,573)</td><td>(341,749)</td></tr><tr><td>Free Cash Flow</td><td>72,764</td><td>73,266</td><td>-16,071</td><td>-18,466</td><td>36,815</td></tr><tr><td>% Change</td><td>4.7%</td><td>0.7%</td><td>NM</td><td>-14.9%</td><td>NM</td></tr><tr><td>Share / Issue Repurchase</td><td>(8,879)</td><td>(2,269)</td><td>(25,502)</td><td>(17,500)</td><td>(19,100)</td></tr><tr><td>Cost of Dividends Paid</td><td>(7,363)</td><td>(7,616)</td><td>(8,651)</td><td>(9,774)</td><td>(10,952)</td></tr><tr><td>Change in Debt</td><td>(2,423)</td><td>(6,333)</td><td>(11,328)</td><td>0</td><td>0</td></tr></table>

Balance Sheet Data (Dec)

<table><tr><td>(US$ Millions)</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Cash &amp; Equivalents</td><td>24,048</td><td>30,708</td><td>48,619</td><td>49,874</td><td>53,251</td></tr><tr><td>Trade Receivables</td><td>47,964</td><td>62,886</td><td>79,834</td><td>101,660</td><td>127,937</td></tr><tr><td>Other Current Assets</td><td>99,518</td><td>112,444</td><td>224,777</td><td>188,311</td><td>195,100</td></tr><tr><td>Property, Plant &amp; Equipment</td><td>134,345</td><td>246,597</td><td>422,774</td><td>672,638</td><td>935,609</td></tr><tr><td>Other Non-Current Assets</td><td>96,517</td><td>142,646</td><td>257,647</td><td>258,447</td><td>259,247</td></tr><tr><td>Total Assets</td><td>402,392</td><td>595,281</td><td>1,033,652</td><td>1,270,930</td><td>1,571,144</td></tr><tr><td>Short-Term Debt</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Other Current Liabilities</td><td>81,814</td><td>102,745</td><td>123,651</td><td>152,129</td><td>189,525</td></tr><tr><td>Long-Term Debt</td><td>28,725</td><td>67,740</td><td>132,473</td><td>132,273</td><td>132,073</td></tr><tr><td>Other Non-Current Liabilities</td><td>8,474</td><td>9,531</td><td>22,819</td><td>22,819</td><td>22,819</td></tr><tr><td>Total Liabilities</td><td>119,013</td><td>180,016</td><td>278,943</td><td>307,221</td><td>344,417</td></tr><tr><td>Total Equity</td><td>283,379</td><td>415,265</td><td>754,709</td><td>963,709</td><td>1,226,727</td></tr><tr><td>Total Equity &amp; Liabilities</td><td>402,392</td><td>595,281</td><td>1,033,652</td><td>1,270,930</td><td>1,571,144</td></tr></table>

\* For full definitions of IQmethod $^{SM}$ measures, see page 13.

## Company Sector

Internet/e-Commerce

## Company Description

Alphabet is a global technology company focused on key areas, such as search, advertising, operating systems and platforms, enterprise and hardware products. The company generates revenue primarily by delivering online advertising and by selling apps and content on Google Play as well as hardware products. The company provides its products and services in more than 100 languages and in 190 countries, regions, and territories.

## Investment Rationale

We see Alphabet as well positioned long term with leading AI technology to apply to search, YouTube, and Cloud businesses. Alphabet should also benefit from increasing mobile usage, video usage, Google Play activity, and connected device activity (including autos). We believe that Alphabet should trade at a premium to a media peer group given technology leadership, high margins, and strong cash flow generation for buybacks.

## Stock Data

<table><tr><td>Average Daily Volume</td><td>33,133,056</td></tr><tr><td>Shares / Common - Dual Listed</td><td>1.00</td></tr></table>

Quarterly Earnings Estimates

<table><tr><td></td><td>2025</td><td>2026</td></tr><tr><td>Q1</td><td>2.81A</td><td>5.11A</td></tr><tr><td>Q2</td><td>2.31A</td><td>9.11A</td></tr><tr><td>Q3</td><td>2.87A</td><td>3.07E</td></tr><tr><td>Q4</td><td>2.82A</td><td>3.33E</td></tr></table>

<table><tr><td>(US$)</td><td>Previous</td><td>Current</td></tr><tr><td>2026E EPS</td><td>19.70</td><td>20.58</td></tr><tr><td>2027E EPS</td><td>14.70</td><td>15.01</td></tr><tr><td>2028E EPS</td><td>18.12</td><td>18.58</td></tr><tr><td>2026E DPS</td><td>0.72</td><td>0.71</td></tr></table>

## 2Q Summary and thoughts on the stock

Google reported a strong 2Q that we believe met Search and exceeded Cloud expectations. The quarter was highlighted by accelerating Cloud growth (82% vs. 63% in 1Q), expanding Cloud margins (35.6% vs 32.9% in 1Q) and healthy backlog growth (up 11% q/q and 375% y/y), underscoring accelerating enterprise demand for AI infrastructure and services. 2Q Search revenues grew 17% y/y and was largely in line with Street, a modest negative after a strong 1Q. YouTube revenues grew 13% y/y (vs Street 10%) aided by World Cup activity. Margins missed, primarily due to 1x legal and other (non-disclosed) items in G&A. Quarter was not as clean as recent prior quarters.

Despite strong 2Q headline results, the stock was down \~3% in the AH, likely due to higher capex outlook (\$195-\$205 vs \$189-\$190 previously), lack of upside on Search revenues, call commentary that suggested tougher comps for search in 3Q and possible modest margin pressure from capacity leasing at high rates, and expected continued pressure on FCF from capacity investment (which could suggest for negative FCF). However, management's commentary appeared constructive on the 3Q demand environment, and we believe added capacity from capex and capacity leasing will translate directly into further cloud revenue acceleration in 2H'26.

In our view, the quarter reinforces the thesis that: 1) Google Search remains a net AI beneficiary, despite robust AI engagement growth on other platforms, as revenue growth continues to outpace growth in 2023-2025, 2) Gemini and Google's TPU infrastructure continue to represent important competitive advantages for Google Cloud and are driving higher margins and market share growth, and 3) Ongoing data center capacity expansion and near-term use of third party capacity are driving incremental Cloud deal activity for Google, and will drive revenue acceleration in 2H'26. Risks are: Tough 3Q comps drive deceleration in search growth, YouTube user harms highlighted at upcoming social media trials, OpenAI's ad ramp, high-profile model and product launches by competitors, flow of funds to AI IPOs.

## Why to buy the stock here:

\- Further Cloud acceleration and upside: Google Cloud has been growing well above the broader industry, and we see potential for further Cloud upside, driven by: 1) new capacity coming online accelerating backlog conversion, 2) growing traction of Google's differentiated AI assets (Gemini and TPUs) that offer potential performance and cost advantages, and 3) ramp of external TPU sales. Google's 2Q backlog of \$514bn sugge

[中间内容因长度限制已省略]

s between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in

connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This

Content contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Subject to the quiet period applicable under laws of the various jurisdictions in which we distribute research reports and other legal and BofA policy-related restrictions on the publication of research reports, fundamental equity reports are produced on a regular basis as necessary to keep the investment recommendation current.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
