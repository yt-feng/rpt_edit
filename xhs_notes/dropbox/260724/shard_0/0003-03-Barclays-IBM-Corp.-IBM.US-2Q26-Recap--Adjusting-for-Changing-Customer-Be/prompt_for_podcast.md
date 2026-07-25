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

<table><tr><td></td><td colspan="3">2026E</td><td colspan="3">2027E</td></tr><tr><td>$, mn</td><td>New</td><td>Old</td><td>% Chg</td><td>New</td><td>Old</td><td>% Chg</td></tr><tr><td>Hybrid Cloud Revenue</td><td>8,174</td><td>8,179</td><td>0.0%</td><td>8,992</td><td>9,117</td><td>-1.4%</td></tr><tr><td>Automation Revenue</td><td>8,134</td><td>8,425</td><td>-3.5%</td><td>8,540</td><td>9,260</td><td>-7.8%</td></tr><tr><td>Data Revenue</td><td>7,419</td><td>7,787</td><td>-4.7%</td><td>8,145</td><td>8,576</td><td>-5.0%</td></tr><tr><td>Transaction Processing Revenue</td><td>8,273</td><td>9,009</td><td>-8.2%</td><td>8,481</td><td>9,416</td><td>-9.9%</td></tr><tr><td>Total Software Revenue</td><td>31,993</td><td>33,399</td><td>-4.2%</td><td>34,158</td><td>36,369</td><td>-6.1%</td></tr><tr><td>Total Consulting Revenue</td><td>21541</td><td>21,707</td><td>-0.8%</td><td>22162</td><td>22,290</td><td>-0.6%</td></tr><tr><td>Total Infrastructure Revenue</td><td>15915</td><td>15,680</td><td>1.5%</td><td>15707</td><td>15,471</td><td>1.5%</td></tr><tr><td>Total Revenue</td><td>70372</td><td>71,611</td><td>-1.7%</td><td>72961</td><td>74,966</td><td>-2.7%</td></tr><tr><td>Non-GAAP Gross Profit</td><td>42227</td><td>43,494</td><td>-2.9%</td><td>44478</td><td>46,133</td><td>-3.6%</td></tr><tr><td>% margin</td><td>60.0%</td><td>60.7%</td><td></td><td>61.0%</td><td>61.5%</td><td></td></tr><tr><td>Non-GAAP Operating Profit (loss)</td><td>15352</td><td>15,486</td><td>-0.9%</td><td>16540</td><td>16,524</td><td>0.1%</td></tr><tr><td>% margin</td><td>21.8%</td><td>21.6%</td><td></td><td>22.7%</td><td>22.0%</td><td></td></tr><tr><td>Operating Cash Flow</td><td>15977</td><td>15,863</td><td>0.7%</td><td>17021</td><td>17,171</td><td>-0.9%</td></tr><tr><td>Capex</td><td>-1206</td><td>-1,301</td><td>-7.3%</td><td>-1238</td><td>-1,351</td><td>-8.3%</td></tr><tr><td>Adj. Free Cash Flow</td><td>15770</td><td>15,695</td><td>0.5%</td><td>17321</td><td>16,643</td><td>4.1%</td></tr></table>

Source: Company data, BARC estimates

Financial Model  
FIGURE 2. IBM Income Statement

<table><tr><td>Fiscal = DecIn $mn</td><td>2022A</td><td>2023A</td><td>2024A</td><td>2025A</td><td>1Q26A</td><td>2Q26A</td><td>3Q26E</td><td>4Q26E</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td></tr><tr><td>Software Revenue</td><td>25,038.0</td><td>26,407.0</td><td>27,086.0</td><td>30,042.0</td><td>7,057.2</td><td>7,761.0</td><td>7,587.8</td><td>9,587.2</td><td>31,993.3</td><td>34,158.5</td><td>36,442.5</td><td>38,751.6</td><td>41,012.6</td></tr><tr><td>y/y % growth</td><td>5.2%</td><td>5.5%</td><td>2.6%</td><td>10.9%</td><td>11.4%</td><td>5.1%</td><td>5.3%</td><td>5.2%</td><td>6.5%</td><td>6.8%</td><td>6.7%</td><td>6.3%</td><td>5.8%</td></tr><tr><td>Consulting Revenue</td><td>19,108.0</td><td>19,986.0</td><td>20,692.0</td><td>21,007.0</td><td>5,270.7</td><td>5,327.0</td><td>5,430.5</td><td>5,512.9</td><td>21,541.1</td><td>22,162.1</td><td>22,740.3</td><td>23,194.8</td><td>23,774.7</td></tr><tr><td>y/y % growth</td><td>7.1%</td><td>4.6%</td><td>3.5%</td><td>1.5%</td><td>4.0%</td><td>0.2%</td><td>2.0%</td><td>4.0%</td><td>2.5%</td><td>2.9%</td><td>2.6%</td><td>2.0%</td><td>2.5%</td></tr><tr><td>Infrastructure Revenue</td><td>15,287.0</td><td>14,592.0</td><td>14,020.0</td><td>15,686.0</td><td>3,322.1</td><td>3,835.0</td><td>3,568.7</td><td>5,189.0</td><td>15,914.8</td><td>15,707.0</td><td>16,007.7</td><td>16,094.1</td><td>16,290.5</td></tr><tr><td>y/y % growth</td><td>7.7%</td><td>-4.5%</td><td>-3.9%</td><td>11.9%</td><td>15.1%</td><td>-7.4%</td><td>0.3%</td><td>1.7%</td><td>1.5%</td><td>-1.3%</t

[中间内容因长度限制已省略]

 scope of its existing DFSA licence. Related financial products or services are only available to Professional Clients, as defined by the Dubai Financial Services Authority. BARC Bank PLC in the UAE is regulated by the Central Bank of the UAE and is licensed to conduct business activities as a branch of a commercial bank incorporated outside the UAE in Dubai (Licence No.: 13/1844/2008, Registered Office: Building No. 6, Burj Dubai Business Hub, Sheikh Zayed Road, Dubai City) and Abu Dhabi (Licence No.: 13/952/2008, Registered Office: Al Jazira Towers, Hamdan Street, PO Box 2734, Abu Dhabi). This material does not constitute or form part of any offer to issue or sell, or any solicitation of any offer to subscribe for or purchase, any securities or investment products in the UAE (including the Dubai International Financial Centre) and accordingly should not be construed as such. Furthermore, this information is being made available on the basis that the recipient acknowledges and understands that the entities and securities to which it may relate have not been approved, licensed by or registered with the UAE Central Bank, the Dubai Financial Services Authority or any other relevant licensing authority or governmental agency in the UAE. The content of this report has not been approved by or filed with the UAE Central Bank or Dubai Financial Services Authority. BARC Bank PLC in the Qatar Financial Centre (Registered No. 00018) is authorised by the Qatar Financial Centre Regulatory Authority (QFCRA). BARC Bank PLC-QFC Branch may only undertake the regulated activities that fall within the scope of its existing QFCRA licence. Principal place of business in Qatar: Qatar Financial Centre, Office 1002, 10th Floor, QFC Tower, Diplomatic Area, West Bay, PO Box 15891, Doha, Qatar. Related financial products or services are only available to Business Customers as defined by the Qatar Financial Centre Regulatory Authority.

Russia: This material is not intended for investors who are not Qualified Investors according to the laws of the Russian Federation as it might contain information about or description of the features of financial instruments not admitted for public offering and/or circulation in the Russian Federation and thus not eligible for non-Qualified Investors. If you are not a Qualified Investor according to the laws of the Russian Federation, please dispose of any copy of this material in your possession.

Sustainable Investing Related Research: There is currently no globally accepted framework or definition (legal, regulatory or otherwise) of, nor market consensus as to what constitutes a ‘sustainable’, ‘ESG’, ‘green’, ‘climate-friendly’ or an equivalent company, investment, strategy or consideration or what precise attributes are required to be eligible to be categorised by such terms. This means there are different ways to evaluate a company or an investment and so different values may be placed on certain sustainability credentials as well as adverse ESG-related impacts of companies and ESG controversies. The evolving nature of sustainable investing considerations, models and methodologies means it can be challenging to definitively and universally classify a company or investment under a sustainable investing label and there may be areas where such companies and investments could improve or where adverse ESG-related impacts or ESG controversies exist. The evolving nature of sustainable finance related regulations and the development of jurisdiction-specific regulatory criteria also means that there is likely to be a degree of divergence as to the interpretation of such terms in the market. We expect industry guidance, market practice, and regulations in this field to continue to evolve.

Any information, data, image, or other content including from a third party source contained, referred to herein or used for whatsoever purpose by BARC or a third party (“Information”), in relation to any actual or potential ‘ESG’, ‘sustainable’ or equivalent objective, issue, factor or consideration is not intended to be relied upon for ESG or sustainability classification, regulatory regime or industry initiative purposes (“ESG Regimes”), unless otherwise stated. Nothing in these materials, including any images included therein, is intended to convey, suggest or indicate that BARC considers or represents any product, service, person or body mentioned in these materials as meeting or qualifying for any ESG or sustainability classification, label or similar standards that may exist under ESG Regimes. BARC has not conducted any assessment of compliance with ESG Regimes. Parties are reminded to make their own assessments for these purposes.

IRS Circular 230 Prepared Materials Disclaimer: BARC does not provide tax advice and nothing contained herein should be construed to be tax advice. Please be advised that any discussion of U.S. tax matters contained herein (including any attachments) (i) is not intended or written to be used, and cannot be used, by you for the purpose of avoiding U.S. tax-related penalties; and (ii) was written to support the promotion or marketing of the transactions or other matters addressed herein. Accordingly, you should seek advice based on your particular circumstances from an independent tax advisor.

© Copyright BARC Bank PLC (2026). All rights reserved. No part of this publication may be reproduced or redistributed in any manner without the prior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request.
"""
