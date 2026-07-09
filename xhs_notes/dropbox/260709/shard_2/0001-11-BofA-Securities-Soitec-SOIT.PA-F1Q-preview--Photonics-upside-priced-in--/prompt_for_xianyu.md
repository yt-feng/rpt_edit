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
Soitec

# F1Q preview: Photonics upside priced in;

Lower PO

Reiterate Rating: NEUTRAL | PO: 138.00 EUR | Price: 118.40 EUR

## Photonics growing but expectations are elevated; Neutral

Soitec reports F1Q revenue on July 28 $^{th}$ . We believe there is downside risk to css estimates for both Mobile, given the weak smartphone market, and Edge AI, given the high implied Photonics-SOI growth. However, we expect the overall business to recover from its FY26 earnings trough. We raise FY27-29E Edge AI but lower Mobile and Auto/Industrial ests, lowering EBITDA. Reit. Neutral with lower €138 PO (was €193) on updated SOTP valuation.

## Street is projecting Photonics-SOI growing above industry

We view Soitec's Photonics-related upside as priced in, with Edge and Cloud AI (of which Photonics-SOI was 42% in FY26) forecasted to grow by css at 28%/34%/43% in FY27/28/29E. This would imply Photonics revenue growth significantly higher than the 50% CAGR for FY26-29E that we model, which is based on Photonics-SOI total die area CAGR forecasts. For context, our global team projects 40%+ total optical revenue growth CAGR in data centers. Given various uncertainties including amount of NPO/CPO content growth, we lack conviction in further Photonics revenue revisions.

## Uncertainties remain on Photonics growth assumptions

With questions on various Photonics-SOI content assumptions hard to answer, it is difficult to project its revenue growth CAGR. Yields, transceiver speeds, changing optical engine requirements PIC sizes, NPO/CPO ramp timelines and associated content growth all present various headwinds and tailwinds to Photonics-SOI growth. We believe the implied css Photonics-SOI growth rate already prices in growth acceleration from NPO/CPO which we view to still be uncertain given the different moving parts. Finally, GlobalWafers' planned ramp in Photonics/RF-SOI has not been derisked, introducing questions on Soitec's market share position going forward.

## Mobile recovering but at slow pace on phone price hikes

Mobile was more than half of FY26 revenue, and given announced price hikes by smartphone-makers, we believe there is downside to css FY27E decline of 6% in Mobile revenue (we model 11% decline). RF-SOI revenue continues to be significantly impacted by elevated customer inventories, sitting at \~2mm wafers with a slowing pace of digestion due to the weak end-market. We model 19%/27% growth in Mobile in FY28/29E, reflecting gradual customer inventory digestion.

<table><tr><td>Estimates (Mar) (EUR)</td><td>2025A</td><td>2026A</td><td>2027E</td><td>2028E</td><td>2029E</td></tr><tr><td>EPS (Adjusted Diluted)</td><td>2.54</td><td>(6.17)</td><td>(0.17)</td><td>1.78</td><td>3.82</td></tr><tr><td>EPS Change (YoY)</td><td>-46.3%</td><td>-343.1%</td><td>97.3%</td><td>NM</td><td>114.8%</td></tr><tr><td>Consensus EPS (Visible Alpha)</td><td></td><td></td><td>(0.14)</td><td>2.00</td><td>4.62</td></tr><tr><td>Valuation (Mar)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>P/E</td><td>46.7x</td><td>NM</td><td>NM</td><td>66.6x</td><td>31.0x</td></tr><tr><td>EV / EBITDA*</td><td>14.1x</td><td>27.9x</td><td>26.0x</td><td>17.0x</td><td>12.5x</td></tr><tr><td>Free Cash Flow Yield*</td><td>0.05%</td><td>1.75%</td><td>1.80%</td><td>4.06%</td><td>2.43%</td></tr></table>

\* For full definitions of IQmethod $^{SM}$ measures, see page 7.

>> Employed by a non-US affiliate of BofAS and is not registered/qualified as a research analyst under the FINRA rules.

Refer to "Other Important Disclosures" for information on certain BofA entities that take responsibility for the information herein in particular jurisdictions.

BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.

Refer to important disclosures on page 8 to 10. Analyst Certification on page 6. Price Objective Basis/Risk on page 6. 1299

## 07 July 2026

Equity

## Key Changes

<table><tr><td>(EUR)</td><td>Previous</td><td>Current</td></tr><tr><td>Price Obj.</td><td>193.00</td><td>138.00</td></tr><tr><td>2027E Rev (m)</td><td>624.5</td><td>604.1</td></tr><tr><td>2028E Rev (m)</td><td>780.6</td><td>741.9</td></tr><tr><td>2029E Rev (m)</td><td>1,033.1</td><td>955.6</td></tr><tr><td>2027E EPS</td><td>0.31</td><td>-0.17</td></tr><tr><td>2028E EPS</td><td>2.26</td><td>1.78</td></tr><tr><td>2029E EPS</td><td>4.88</td><td>3.82</td></tr></table>

## Oliver Wong >>

Research Analyst
MLI (UK)
+44 20 7995 9014
oliver.wong2@bofa.com

## Didier Scemama >>

Research Analyst
MLI (UK)
+44 20 7995 6751
didier.scemama@bofa.com

Amelia Banks >>
Research Analyst
MLI (UK)
+44 20 7995 3554
amelia.banks@bofa.com

## Stock Data

<table><tr><td>Price</td><td>118.40 EUR</td></tr><tr><td>Price Objective</td><td>138.00 EUR</td></tr><tr><td>Date Established</td><td>07-Jul-2026</td></tr><tr><td>Investment Opinion</td><td>C-2-9</td></tr><tr><td>52-Week Range</td><td>22.62 EUR-200.50 EUR</td></tr><tr><td>Mrkt Val / Shares Out (mn)</td><td>4,224 EUR / 35.7</td></tr><tr><td>Average Daily Value (mn)</td><td>64.76 USD</td></tr><tr><td>Free Float</td><td>69.5%</td></tr><tr><td>BofA Ticker / Exchange</td><td>SLOIF / ENP</td></tr><tr><td>Bloomberg / Reuters</td><td>SOI FP / SOIT.PA</td></tr><tr><td>ROE (2027E)</td><td>-0.4%</td></tr><tr><td>Net Dbt to Eqty (Mar2026A)</td><td>4.4%</td></tr></table>

AI: Artificial intelligence

CPO: Co-packaged optics

NPO: Near packaged optics

PIC: Photonic integrated circuit

RF: Radio frequency

SOI: Silicon on insulator

SOTP: Sum of the parts

css: consensus

<table><tr><td colspan="3">Stock Data</td></tr><tr><td colspan="2">Price to Book Value</td><td>3.1x</td></tr><tr><td colspan="3">Half-yearly Earnings Estimates</td></tr><tr><td></td><td>2026</td><td>2027</td></tr><tr><td>H1</td><td>OA</td><td>-0.36E</td></tr><tr><td>H2</td><td>OA</td><td>0.20E</td></tr></table>

## iQprofile $^{SM}$ Soitec

<table><tr><td>Key Income Statement Data (Mar)</td><td>2025A</td><td>2026A</td><td>2027E</td><td>2028E</td><td>2029E</td></tr><tr><td colspan="6">(EUR Millions)</td></tr><tr><td>Sales</td><td>891</td><td>592</td><td>604</td><td>742</td><td>956</td></tr><tr><td>EBITDA Adjusted</td><td>298</td><td>151</td><td>162</td><td>248</td><td>337</td></tr><tr><td>Depreciation &amp; Amortization</td><td>(140)</td><td>(138)</td><td>(140)</td><td>(146)</td><td>(155)</td></tr><tr><td>EBIT Adjusted</td><td>158</td><td>13.0</td><td>22.0</td><td>102</td><td>182</td></tr><tr><td>Net Interest &amp; Other Income</td><td>(9.00)</td><td>(30.0)</td><td>(8.97)</td><td>(6.62)</td><td>(0.87)</td></tr><tr><td>Tax Expense / Benefit</td><td>(19.0)</td><td>(61.0)</td><td>1.05</td><td>(11.2)</td><td>(24.2)</td></tr><tr><td>Net Income (Adjusted)</td><td>91.0</td><td>(220)</td><td>(5.95)</td><td>63.7</td><td>137</td></tr><tr><td>Average Fully Diluted Shares Outstanding</td><td>35.9</td><td>35.7</td><td>35.8</td><td>35.9</td><td>36.0</td></tr><tr><td colspan="6">Key Cash Flow Statement Data</td></tr><tr><td>Net Income (Reported)</td><td>92.0</td><td>(222)</td><td>(5.95)</td><td>63.7</td><td>137</td></tr><tr><td>Depreciation &amp; Amortization</td><td>140</td><td>138</td><td>140</td><td>146</td><td>155</td></tr><tr><td>Change in Working Capital</td><td>(100)</td><td>50.0</td><td>39.0</td><td>38.3</td><td>(120)</td></tr><tr><td>Deferred Taxation Charge</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Other CFO</td><td>69.0</td><td>236</td><td>27.9</td><td>37.9</td><td>45.1</td></tr><tr><td>Cash Flow from Operations</td><td>201</td><td>202</td><td>201</td><td>286</td><td>218</td></tr><tr><td>Capital Expenditure</td><td>(199)</td><td>(128)</td><td>(125)</td><td>(115)</td><td>(115)</td></tr><tr><td>(Acquisition) / Disposal of Investments</td><td>4.00</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Other CFI</td><td>19.0</td><td>14.0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Cash Flow from Investing</td><td>(176)</td><td>(114)</td><td>(125)</td><td>(115)</td><td>(115)</td></tr><tr><td>Share Issue / (Repurchase)</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Cost of Dividends Paid</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>Increase (decrease) debt</td><td>34.0</td><td>(161)</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Other CFF</td><td>(84.0)</td><td>(43.0)</td><td>(8.97)</td><td>(6.62)</td><td>(0.87)</td></tr><tr><td>Cash Flow from Financing</td><td>(50.0)</td><td>(204)</td><td>(8.97)</td><td>(6.62)</td><td>(0.87)</td></tr><tr><td>Total Cash Flow (CFO + CFI + CFF)</td><td>(25.0)</td><td>(116)</td><td>67.0</td><td>165</td><td>102</td></tr><tr><td>FX and other changes to cash</td><td>5.00</td><td>(10.0)</td><td>(0.01)</td><td>(0.32)</td><td>0</td></tr><tr><td>Change in Cash</td><td>(20.0)</td><td>(126)</td><td>67.0</td><td>164</td><td>102</td></tr><tr><td>Change in Net Debt</td><td>54.0</td><td>(35.0)</td><td>(67.0)</td><td>(164)</td><td>(102)</td></tr><tr><td>Net Debt</td><td>93.0</td><td>58.0</td><td>(8.98)</td><td>(173)</td><td>(275)</td></tr><tr><td colspan="6">Key Balance Sheet Data</td></tr><tr><td>Property, Plant &amp; Equipment</td><td>1,003</td><td>893</td><td>853</td><td>797</td><td>732</td></tr><tr><td>Goodwill</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>Other Intangibles</td><td>130</td><td>94.0</td><td>119</td><td>144</td><td>169</td></tr><tr><td>Other Non-Current Assets</td><td>162</td><td>68.0</td><td>68.0</td><td>68.0</td><td>68.0</td></tr><tr><td>Trade Receivables</td><td>463</td><td>280</td><td>234</td><td>244</td><td>314</td></tr><tr><td>Cash &amp; Equivalents</td><td>688</td><td>562</td><td>629</td><td>793</td><td>895</td></tr><tr><td>Other Current Assets</td><td>362</td><td>383</td><td>434</td><td>397</td><td>448</td></tr><tr><td>Total Assets</td><td>2,808</td><td>2,280</td><td>2,336</td><td>2,443</td><td>2,626</td></tr><tr><td>Long-Term Debt</td><td>375</td><td>517</td><td>517</td><td>517</td><td>517</td></tr><tr><td>Other Non-Current Liabilities</td><td>94.0</td><td>122</td><td>122</td><td>122</td><td>122</td></tr><tr><td>Short-Term Debt</td><td>406</td><td>103</td><td>103</td><td>103</td><td>103</td></tr><tr><td>Other Current Liabilities</td><td>338</td><td>213</td><td>255</td><td>279</td><td>304</td></tr><tr><td>Total Liabilities</td><td>1,213</td><td>955</td><td>997</td><td>1,021</td><td>1,046</td></tr><tr><td>Total Equity</td><td>1,594</td><td>1,327</td><td>1,341</td><td>1,425</td><td>1,582</td></tr><tr><td>Total Equity &amp; Liabilities</td><td>2,807</td><td>2,282</td><td>2,338</td><td>2,445</td><td>2,628</td></tr><tr><td colspan="6">Business Performance*</td></tr><tr><td>Return On Capital Employed</td><td>6.12%</td><td>1.03%</td><td>1.71%</td><td>4.95%</td><td>7.97%</td></tr><tr><td>Return On Equity</td><td>5.89%</td><td>-15.1%</td><td>-0.45%</td><td>4.61%</td><td>9.14%</td></tr><tr><td>Operating Margin</td><td>13.5%</td><td>-22.1%</td><td>0.33%</td><td>11.0%</td><td>17.0%</td></tr><tr><td>Free Cash Flow (MM)</td><td>2.00</td><td>74.0</td><td>76.0</td><td>171</td><td>103</td></tr><tr><td colspan="6">Quality of Earnings*</td></tr><tr><td>Cash Realization Ratio</td><td>2.21x</td><td>NM</td><td>NM</td><td>4.49x</td><td>1.58x</td></tr><tr><td>Asset Replacement Ratio</td><td>1.42x</td><td>0.93x</td><td>0.89x</td><td>0.79x</td><td>0.74x</td></tr><tr><td>Tax Rate</td><td>17.1%</td><td>NM</td><td>15.0%</td><td>15.0%</td><td>15.0%</td></tr><tr><td>Net Debt/Equity</td><td>5.83%</td><td>4.37%</td><td>-0.67%</td><td>-12.2%</td><td>-17.4%</td></tr><tr><td>Interest Cover</td><td>5.64x</td><td>0.30x</td><td>0.77x</td><td>3.55x</td><td>6.37x</td></tr></table>

\* For full definitions of iQmethod $^{SM}$ measures, see page 7.

## Company Sector Semiconductors

## Company Description

Soitec designs and manufactures semiconductor substrates, predominantly based on silicon on insulator (SOI) technologies. Soitec has recently been diversifying into technologies such as POI, SiC and GaN. Soitec's products are key enablers and beneficiaries of many fast growing trends such as 5G communications, vehicle electrification, silicon photonics, 3D sensing and increasing demand for low power/cost processing power. Soitec is listed on Euronext Paris and is headquartered in Bernin, France.

## Investment Rationale

Soitec is a leader in silicon on insulator (SOI) substrates. Recently, Soitec has moved into new areas, such as gallium nitride (GaN) & piezoelectric on insulator (POI), with silicon carbide (SiC) in development. Soitec's products are key enablers & beneficiaries of many fast-growing trends, such as optical connectivity and 5G communications. However, we still lack visibility on when customer inventory digestion will end and tariff overhang on consumer (PC/Smartphone) demand may clear.

## Bottom-up forecast

Exhibit 1: We project 23%/29% revenue growth in FY28/29E driven by Photonics-SOI growth and RF-SOI recovery

Soitec bottom-up revenue build, FY26-29E

<table><tr><td>EUR mm</td><td>FY26E</td><td>FY27E</td><td>FY28E</td><td>FY29E</td></tr><tr><td>Mobile Comm.</td><td>309</td><td>276</td><td>327</td><td>415</td></tr><tr><td>RF-SOI</td><td>169</td><td>119</td><td>149</td><td>214</td></tr><tr><td>FD-SOI</td><td>39</td><td>43</td><td>48</td><td>52</td></tr><tr><td>POI</td><td>101</td><td>114</td><td>130</td><td>149</td></tr><tr><td>Auto &amp; Ind.</td><td>69</td><td>69</td><td>78</td><td>89</td></tr><tr><td>Power-SOI</td><td>59</td><td>59</td><td>65</td><td>71</td></tr><tr><td>FD-SOI</td><td>6</td><td>6</td><td>6</td><td>7</td></tr><tr><td>SmartSiC</td><td>5</td><td>5</td><td>8</td><td>11</td></tr><tr><td>Edge &amp; Cloud AI</td><td>214</td><td>259</td><td>337</td><td>451</td></tr><tr><td>Photonics-SOI</td><td>90</td><td>135</td><td>202</td><td>304</td></tr><tr><td>FD-SOI</td><td>100</td><td>110</td><td>121</td><td>133</td></tr><tr><td>PD-SOI</td><td>14</td><td>14</td><td>14</td><td>14</td></tr><tr><td>Other</td><td>10</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Total</td><td>592</td><td>605</td><td>743</td><td>955</td></tr><tr><td>Total yoy %</td><td>-34%</td><td>2%</td><td>23%</td><td>29%</td></tr></table>

Source: BofA Global Research estimates  
BofA GLOBAL RESEARCH

## Changes to estimates

Exhibit 2: We lower our FY27-29E topline ests by 3-8%, resulting in 9-14% decrease in EBITDA Soitec Changes to estimates, FY27-29E

<table><tr><td colspan="10">EUR millions except per share data</td></tr><tr><td rowspan="2"></td><td colspan="3">FY27E</td><td colspan="3">FY28E</td><td colspan="3">FY29E</td></tr><tr><td>Old</td><td>New</td><td>% chg</td><td>Old</td><td>New</td><td>% chg</td><td>Old</td><td>New</td><td>% chg</td></tr><tr><td>Sales</td><td>624.5</td><td>604.1</td><td>-3.3%</td><td>780.6</td><td>741.9</td><td>-5.0%</td><td>1,033.1</td><td>955.6</td><td>-7.5%</td></tr><tr><td>YoY growth (%)</td><td>5.5%</td><td>2.0%</td><td>-344 bps</td><td>25.0%</td><td>22.8%</td><td>-220 bps</td><td>32.3%</td><td>28.8%</td><td>-354 bps</td></tr><tr><td>LfL growth (%) (at Constant Scope &amp; FX)</td><td>5.5%</td><td>2.0%</td><td>-344 bps</td><td>25.0%</td><td>22.8%</td><td>-220 bps</td><td>32.3%</td><td>28.8%</td><td>-354 bps</td></tr><tr><td>FX effect</td><td>0.0%</td><td>0.0%</td><td>-</td><td>0.0%</td><td>0.0%</td><td>-</td><td>0.0%</td><td>0.0%</td><td>-</td></tr><tr><td>Gross profit</td><td>143.9</td><td>119.8</td><td>-16.8%</td><td>234.2</td><td>207.7</td><td>-11.3%</td><td>361.6</td><td>305.8</td><td>-15.4%</td></tr><tr><td>margin (%)</td><td>23.0%</td><td>19.8%</td><td>-322 bps</td><td>30.0%</td><td>28.0%</td><td>-200 bps</td><td>35.0%</td><td>32.0%</td><td>-300 bps</td><

[中间内容因长度限制已省略]

arriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This

information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Subject to the quiet period applicable under laws of the various jurisdictions in which we distribute research reports and other legal and BofA policy-related restrictions on the publication of research reports, fundamental equity reports are produced on a regular basis as necessary to keep the investment recommendation current.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.
"""
