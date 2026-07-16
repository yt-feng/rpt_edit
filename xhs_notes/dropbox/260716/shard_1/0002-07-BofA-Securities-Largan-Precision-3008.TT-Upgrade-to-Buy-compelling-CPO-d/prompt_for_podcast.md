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
Largan Precision

# Upgrade to Buy: compelling CPO-driven valuation and earnings upcycle from 2028E

Rating Change: BUY | PO: 5,600 TWD | Price: 4,345 TWD

## Upgrade to Buy: Stronger long-term upside from CPO

We upgrade Largan to Buy from Neutral on strong revenue/earnings upside from 2028E, led by its potential share gain at FA/FAU for CPO switches. We raise Largan's 2026-28E earnings by 1-13%, and lift our PO to NT\$5,600 (25x 2028E P/E) from NT\$2,900 (16x 2H26-1H27E P/E). We use 2028E to capture CPO's volume take-off, and our 25x target multiple is at its historical peak P/E, matches with last round's earnings upcycle. Given CPO is still at an early stage while optical interconnect is a long-term upcycle, we note the market is willing to look beyond 2028. Thus, we use SOTP for a sanity check on CPO's value into 2030, and derive a value of NT\$5,641 per share by applying 30x P/E on CPO business (base case: 30% share at FA in Exhibit 9 and Exhibit 4).

## CPO to drive 5-10% EPS upside in 2028E, 60%+ in 2030E

We are more confident on Largan entering Nvidia's CPO supply chain. According to mgmt., Largan is engaging with more than one customer, progressing through certification (coming months), and capacity expansion (pilot line by 3Q26-end). Although Largan has no track record in datacom, we see edge is in high-precision optic alignment via automation and its partnership with CPO ecosystem (see FAU sector report). Our analysis shows 2028E EPS could see $5 - 10\%$ upside vs 2026E from FA, assuming $20 - 30\%$ share and $30 - 40\%$ net margin (Exhibit 7). Into 2030E, under a bear/base/bull case analysis, earnings could expand by $24\% / 63\% / 184\%$ vs 2028E, respectively (Exhibit 9).

## Resilient smartphone business with iPhone spec upgrade

Although the overall smartphone supply chain is under pressure amid memory price hikes, we view Largan as more resilient on iPhone's multi-year spec upgrade cycle and its leading position. We expect variable aperture on the Pro series to drive 30-50% main camera ASP upside in 2H26, while Largan should continue to benefit from rising MP or higher lens count in main/periscope cam into 2027-28.

<table><tr><td>Estimates (Dec) (NT$)</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Net Income (Adjusted - mn)</td><td>25,915</td><td>21,275</td><td>25,049</td><td>26,929</td><td>30,226</td></tr><tr><td>EPS</td><td>191.2</td><td>156.9</td><td>184.8</td><td>198.6</td><td>223.0</td></tr><tr><td>EPS Change (YoY)</td><td>44.8%</td><td>-17.9%</td><td>17.7%</td><td>7.5%</td><td>12.2%</td></tr><tr><td>Consensus EPS (Visible Alpha)</td><td></td><td></td><td>186.93</td><td>205.34</td><td>220.05</td></tr><tr><td>Dividend / Share</td><td>97.5</td><td>80.0</td><td>94.2</td><td>101.3</td><td>113.7</td></tr><tr><td>Free Cash Flow / Share</td><td>153.2</td><td>103.0</td><td>179.2</td><td>214.4</td><td>244.6</td></tr><tr><td>Valuation (Dec)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>P/E</td><td>22.7x</td><td>27.7x</td><td>23.5x</td><td>21.9x</td><td>19.5x</td></tr><tr><td>Dividend Yield</td><td>2.2%</td><td>1.8%</td><td>2.2%</td><td>2.3%</td><td>2.6%</td></tr><tr><td>EV / EBITDA*</td><td>14.7x</td><td>14.2x</td><td>13.0x</td><td>11.7x</td><td>10.5x</td></tr><tr><td>Free Cash Flow Yield*</td><td>3.5%</td><td>2.3%</td><td>4.1%</td><td>4.9%</td><td>5.5%</td></tr></table>

\* For full definitions of iQmethod $^{SM}$ measures, see page 10.

This research report provides general information only. No part of this report may be used or reproduced or quoted in any manner whatsoever in Taiwan by the press or other persons without the express written consent of BofA.

>> Employed by a non-US affiliate of BofAS and is not registered/qualified as a research analyst under the FINRA rules.

Refer to "Other Important Disclosures" for information on certain BofA entities that take responsibility for the information herein in particular jurisdictions.

BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.

Refer to important disclosures on page 11 to 13. Analyst Certification on page 8. Price Objective Basis/Risk on page 8. 12993351

## 14 July 2026

Equity

## Key Changes

<table><tr><td>(NT$)</td><td>Previous</td><td>Current</td></tr><tr><td>Inv. Opinion</td><td>B-2-7</td><td>B-1-7</td></tr><tr><td>Inv. Rating</td><td>NEUTRAL</td><td>BUY</td></tr><tr><td>Price Obj.</td><td>2,900.00</td><td>5,600.00</td></tr><tr><td>2026E Rev (m)</td><td>64,699.9</td><td>67,599.2</td></tr><tr><td>2027E Rev (m)</td><td>67,560.1</td><td>73,749.0</td></tr><tr><td>2028E Rev (m)</td><td>68,798.3</td><td>79,192.9</td></tr><tr><td>2026E EPS</td><td>183.80</td><td>184.77</td></tr><tr><td>2027E EPS</td><td>194.32</td><td>198.64</td></tr><tr><td>2028E EPS</td><td>196.54</td><td>222.96</td></tr></table>

Robert Cheng >>
Research Analyst
BofA (Taiwan)
robert.cheng@bofa.com

Katherine Zhu >>
Research Analyst
BofA (Hong Kong)
kexin.zhu@bofa.com

Doris Kao >>
Research Analyst
BofA (Taiwan)
doris.kao@bofa.com

## Stock Data

<table><tr><td>Price</td><td>4,345 TWD</td></tr><tr><td>Price Objective</td><td>5,600 TWD</td></tr><tr><td>Date Established</td><td>14-Jul-2026</td></tr><tr><td>Investment Opinion</td><td>B-1-7</td></tr><tr><td>52-Week Range</td><td>2,020 TWD-5,360 TWD</td></tr><tr><td>Mrkt Val / Shares Out (mn)</td><td>18,308 USD / 135.6</td></tr><tr><td>Market Value (mn)</td><td>589,039 TWD</td></tr><tr><td>Average Daily Value (mn)</td><td>374.45 USD</td></tr><tr><td>Free Float</td><td>58.1%</td></tr><tr><td>BofA Ticker / Exchange</td><td>LGANF / TAI</td></tr><tr><td>Bloomberg / Reuters</td><td>3008 TT / 3008.TW</td></tr><tr><td>ROE (2026E)</td><td>12.6%</td></tr><tr><td>Net Dbt to Eqty (Dec-2025A)</td><td>-68.8%</td></tr></table>

For acronyms, please refer to Exhibit 11

Key Cash Flow Statement Data  
iQprofile $^{SM}$ Largan Precision

<table><tr><td>Key Income Statement Data (Dec)</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td colspan="6">(NT$ Millions)</td></tr><tr><td>Sales</td><td>59,458</td><td>61,148</td><td>67,599</td><td>73,749</td><td>79,193</td></tr><tr><td>Gross Profit</td><td>31,209</td><td>30,837</td><td>33,434</td><td>36,862</td><td>41,180</td></tr><tr><td>Sell General &amp; Admin Expense</td><td>(1,930)</td><td>(1,985)</td><td>(2,050)</td><td>(2,185)</td><td>(2,304)</td></tr><tr><td>Operating Profit</td><td>24,033</td><td>23,558</td><td>25,663</td><td>28,646</td><td>32,563</td></tr><tr><td>Net Interest &amp; Other Income</td><td>8,142</td><td>2,342</td><td>4,426</td><td>3,998</td><td>3,998</td></tr><tr><td>Associates</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>Pretax Income</td><td>32,174</td><td>25,900</td><td>30,088</td><td>32,644</td><td>36,561</td></tr><tr><td>Tax (expense) / Benefit</td><td>(5,963)</td><td>(4,340)</td><td>(4,829)</td><td>(5,504)</td><td>(6,124)</td></tr><tr><td>Net Income (Adjusted)</td><td>25,915</td><td>21,275</td><td>25,049</td><td>26,929</td><td>30,226</td></tr><tr><td>Average Fully Diluted Shares Outstanding</td><td>136</td><td>136</td><td>136</td><td>136</td><td>136</td></tr></table>

<table><tr><td>Net Income</td><td>25,915</td><td>21,275</td><td>25,049</td><td>26,929</td><td>30,226</td></tr><tr><td>Depreciation &amp; Amortization</td><td>6,230</td><td>7,732</td><td>8,577</td><td>9,217</td><td>9,697</td></tr><tr><td>Change in Working Capital</td><td>(943)</td><td>(1,208)</td><td>(1,709)</td><td>(1,534)</td><td>(1,270)</td></tr><tr><td>Deferred Taxation Charge</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>Other Adjustments, Net</td><td>376</td><td>(1,719)</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Cash Flow from Operations</td><td>31,579</td><td>26,080</td><td>31,916</td><td>34,612</td><td>38,653</td></tr><tr><td>Capital Expenditure</td><td>(11,126)</td><td>(12,338)</td><td>(8,000)</td><td>(6,000)</td><td>(6,000)</td></tr><tr><td>(Acquisition) / Disposal of Investments</td><td>(7,374)</td><td>(1,704)</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Other Cash Inflow / (Outflow)</td><td>2,434</td><td>4,805</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Cash Flow from Investing</td><td>(16,066)</td><td>(9,236)</td><td>(8,000)</td><td>(6,000)</td><td>(6,000)</td></tr><tr><td>Shares Issue / (Repurchase)</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Cost of Dividends Paid</td><td>(10,811)</td><td>(11,412)</td><td>(10,677)</td><td>(12,577)</td><td>(13,521)</td></tr><tr><td>Cash Flow from Financing</td><td>(10,764)</td><td>(13,458)</td><td>(10,677)</td><td>(12,650)</td><td>(13,524)</td></tr><tr><td>Free Cash Flow</td><td>20,453</td><td>13,743</td><td>23,916</td><td>28,612</td><td>32,653</td></tr><tr><td>Net Debt</td><td>(123,416)</td><td>(131,295)</td><td>(144,534)</td><td>(160,568)</td><td>(179,700)</td></tr><tr><td>Change in Net Debt</td><td>(5,956)</td><td>(2,496)</td><td>(13,239)</td><td>(15,963)</td><td>(19,132)</td></tr></table>

<table><tr><td>Property, Plant &amp; Equipment</td><td>46,936</td><td>51,472</td><td>51,117</td><td>48,121</td><td>44,646</td></tr><tr><td>Other Non-Current Assets</td><td>23,827</td><td>15,029</td><td>14,808</td><td>14,586</td><td>14,365</td></tr><tr><td>Trade Receivables</td><td>10,360</td><td>10,462</td><td>14,816</td><td>16,164</td><td>17,357</td></tr><tr><td>Cash &amp; Equivalents</td><td>123,620</td><td>131,295</td><td>144,534</td><td>160,568</td><td>179,700</td></tr><tr><td>Other Current Assets</td><td>11,784</td><td>12,529</td><td>11,432</td><td>11,879</td><td>12,064</td></tr><tr><td>Total Assets</td><td>216,527</td><td>220,787</td><td>236,706</td><td>251,319</td><td>268,132</td></tr><tr><td>Long-Term Debt</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Other Non-Current Liabilities</td><td>561</td><td>171</td><td>171</td><td>171</td><td>171</td></tr><tr><td>Short-Term Debt</td><td>203</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Other Current Liabilities</td><td>30,375</td><td>29,749</td><td>31,297</td><td>31,558</td><td>31,666</td></tr><tr><td>Total Liabilities</td><td>31,139</td><td>29,919</td><td>31,467</td><td>31,728</td><td>31,836</td></tr><tr><td>Total Equity</td><td>185,388</td><td>190,868</td><td>205,239</td><td>219,591</td><td>236,296</td></tr><tr><td>Total Equity &amp; Liabilities</td><td>216,527</td><td>220,787</td><td>236,706</td><td>251,319</td><td>268,132</td></tr></table>

<table><tr><td colspan="6">iQmethodSM - Bus Performance*</td></tr><tr><td>Return On Capital Employed</td><td>13.2%</td><td>12.3%</td><td>12.6%</td><td>12.8%</td><td>13.3%</td></tr><tr><td>Return On Equity</td><td>14.8%</td><td>11.3%</td><td>12.6%</td><td>12.7%</td><td>13.3%</td></tr><tr><td>Operating Margin</td><td>40.4%</td><td>38.5%</td><td>38.0%</td><td>38.8%</td><td>41.1%</td></tr><tr><td>EBITDA Margin</td><td>50.9%</td><td>51.2%</td><td>50.7%</td><td>51.3%</td><td>53.4%</td></tr></table>

<table><tr><td>Cash Realization Ratio</td><td>1.2x</td><td>1.2x</td><td>1.3x</td><td>1.3x</td><td>1.3x</td></tr><tr><td>Asset Replacement Ratio</td><td>1.8x</td><td>1.6x</td><td>0.9x</td><td>0.7x</td><td>0.6x</td></tr><tr><td>Tax Rate (Reported)</td><td>18.5%</td><td>16.8%</td><td>16.0%</td><td>16.9%</td><td>16.8%</td></tr><tr><td>Net Debt-to-Equity Ratio</td><td>-66.6%</td><td>-68.8%</td><td>-70.4%</td><td>-73.1%</td><td>-76.0%</td></tr><tr><td>Interest Cover</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr></table>

## Key Metrics

\* For full definitions of IQmethod $^{SM}$ measures, see page 10.

## Company Sector

Industrials/Multi-Industry

## Company Description

Largan, established in 1987, is based in Tai Chung, Taiwan. The company is Taiwan's leading optical lens manufacturer for digital imaging products. These include digital cameras, mobile phone cameras, projectors, and MFPs.

## Investment Rationale

We have a Buy rating on Largan, eyeing rising visibility on potential CPO project gains. We believe CPO will drive a valuation re-rating and potential earning upside from 2028E. Besides, legacy business should stay resilient thanks to iPhone's multi-year spec upgrade cycle.

## Stock Data

Price to Book Value 2.9x

## Upgrade to Buy: stronger long-term upside from CPO

We upgrade Largan to Buy from Neutral on strong revenue/earnings upside from 2028E, led by its potential share gain at FA/FAU for CPO switches. Meanwhile, the legacy business should remain resilient, thanks to iPhone's multi-year camera upgrade cycle. We raise Largan's 2026-28E earnings by $1 - 13\%$ to reflect potential upside from CPO and a solid Apple business.

We lift our PO to NT\$5,600 (25x 2028E P/E) from NT\$2,900 (16x 2H26-1H27E P/E). We use 2028E to capture CPO's volume take-off, and our 25x target multiple is at its historical peak P/E, matching last round's earnings upcycle.

We note the market is confident that optical interconnect will be a long-term upcycle, and we believe investors tend to be willing to look beyond 2028 to see the long-term upside potential from CPO. If CPO switches can reach a certain scale into 2028-30E, our analysis shows a stronger earnings upcycle for Largan vs the smartphone camera upcycle in 2016-18. Thus, emerging CPO/FAU suppliers in Greater China tend to trade at a high P/E of 29x 2028E on average. We also use SOTP valuation for a sanity check on CPO's long-term value, and we derive a value per share of NT\$5,641 by applying 30x 2030E P/E on CPO business (base case: 30% share at FA).

Exhibit 1: We lift 2026-28E earnings estimates by 1-13%
Earnings estimate changes, 2026-28E

<table><tr><td rowspan="2">(NT$mn)</td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td>New</td><td>Old</td><td>Diff (%)</td><td>New</td><td>Old</td><td>Diff (%)</td><td>New</td><td>Old</td><td>Diff (%)</td></tr><tr><td>Total sales</td><td>67,599</td><td>64,700</td><td>4.5</td><td>73,749</td><td>67,560</td><td>9.2</td><td>79,193</td><td>68,798</td><td>15.1</td></tr><tr><td>Gross Profit</td><td>33,434</td><td>32,878</td><td>1.7</td><td>36,862</td><td>35,211</td><td>4.7</td><td>41,180</td><td>35,748</td><td>15.2</td></tr><tr><td>Gross margin</td><td>49.5%</td><td>50.8%</td><td>-1.4</td><td>50.0%</td><td>52.1%</td><td>-2.1</td><td>52.0%</td><td>52.0%</td><td>0.0</td></tr><tr><td>Operating income</td><td>25,663</td><td>25,468</td><td>0.8</td><td>28,646</td><td>27,646</td><td>3.6</td><td>32,563</td><td>27,997</td><td>16.3</td></tr><tr><td>Operating margin</td><td>38.0%</td><td>39.4%</td><td>-1.4</td><td>38.8%</td><td>40.9%</td><td>-2.1</td><td>41.1%</td><td>40.7%</td><td>0.4</td></tr><tr><td>Pretax income</td><td>30,088</td><td>29,943</td><td>0.5</td><td>32,644</td><td>31,645</td><td>3.2</td><td>36,561</td><td>31,995</td><td>14.3</td></tr><tr><td>Pretax margin</td><td>44.5%</td><td>46.3%</td><td>-1.8</td><td>44.3%</td><td>46.8%</td><td>-2.6</td><td>46.2%</td><td>46.5%</td><td>-0.3</td></tr><tr><td>Net income</td><td>25,049</td><td>24,917</td><td>0.5</td><td>26,929</td><td>26,343</td><td>2.2</td><td>30,226</td><td>26,645</td><td>13.4</td></tr><tr><td>Net margin</td><td>37.1%</td><td>38.5%</td><td>-1.5</td><td>36.5%</td><td>39.0%</td><td>-2.5</td><td>38.2%</td><td>38.7%</td><td>-0.6</td></tr><tr><td>EPS (NT$)</td><td>184.8</td><td>183.8</td><td>0.5</td><td>198.6</td><td>194.3</td><td>2.2</td><td>223.0</td><td>196.5</td><td>13.4</td></tr></table>

Source: BofA Global Research estimates  
BofA GLOBAL RESEARCH

Exhibit 2: Our 2026-28E earnings are largely in line with consensus
BofAe vs. consensus, 2026-28E

<table><tr><td rowspan="2">(NT$mn)</td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td>BofAe</td><td>Consensus</td><td>Diff (%)</td><td>BofAe</td><td>Consensus</td><td>Diff (%)</td><td>BofAe</td><td>Consensus</td><td>Diff (%)</td></tr><tr><td>Total sales</td><td>67,599</td><td>66,318</td><td>1.9</td><td>73,749</td><td>71,653</td><td>2.9</td><td>79,193</td><td>79,957</td><td>-1.0</td></tr><tr><td>Gross profit</td><td>33,434</td><td>33,427</td><td>0.0</td><td>36,862</td><td>37,120</td><td>-0.7</td><td>41,180</td><td>42,145</td><td>-2.3</td></tr><tr><td>Gross margin</td><td>49.5%</td><td>50.4%</td><td>-0.9</td><td>50.0%</td><td>51.8%</td><td>-1.8</td><td>52.0%</td><td>52.7%</td><td>-0.7</td></tr><tr><td>Operating profit</td><td>25,663</td><td>25,814</td><td>-0.6</td><td>28,646</td><td>28,962</td><td>-1.1</td><td>32,563</td><td>32,687</td><td>-0.4</td></tr><tr><td>Operating margin</td><td>38.0%</td><td>38.9%</td><td>-1.0</td><td>38.8%</td><td>40.4%</td><td>-1.6</td><td>41.1%</td><td>40.9%</td><td>0.2</td></tr><tr><td>Pretax income</td><td>30,088</td><td>30,414</td><td>-1.1</td><td>32,644</td><td>33,574</td><td>-2.8</td><td>36,561</td><td>37,731</td><td>-3.1</td></tr><tr><td>Pretax margin</td><td>44.5%</td><td>45.9%</td><td>-1.4</td><td>44.3%</td><td>46.9%</td><td>-2.6</td><td>46.2%</td><td>47.2%</td><td>-1.0</td></tr><tr><td>Net income</td><td>25,049</td><td>24,811</td><td>1.0</td><td>26,929</td><td>27,102</td><td>-0.6</td><td>30,226</td><td>30,219</td><td>0.0</td></tr><tr><td>Net margin</td><td>37.1%</td><td>37.4%</td><td>-0.4</td><td>36.5%</td><td>37.8%</td><td>-1.3</td><td>38.2%</td><td>37.8%</td><td>0.4</td></tr><tr><td>EPS (NT$)</td><td>184.8</td><td>183.0</td><td>1.0</td><td>198.6</td><td>199.9</td><td>-0.6</td><td>223.0</td><td>222.9</td><td>0.0</td></tr></table>

Source: BofA Global Research estimates, Bloomberg consensus  
BofA GLOBAL RESEARCH

Exhibit 3: The stock trades at 20x 1-year forward P/E, above +1SD Largan's 1-year forward P/E with -1/+1 standard deviation  
![](images/696370c3fa479706b64fc59cc75d64c40fa6adb3242b646bcf2bc7ceb32430e6.jpg)  
Source: BofA Global Research  
BofA GLOBAL RESEARCH

## Exhibit 4: We drive a value per share of NT\$5,641 by applying 30x P/E on CPO business' EPS in 2030

SOTP valuation for sanity check of CPO's long-term contribution

<table><tr><td colspan="2">SOTP Sumber check</td></tr><tr><td>Legacy business</td><td>2026E</td></tr><tr><td>EPS</td><td>185</td></tr><tr><td>P/E</td><td>13</td></tr><tr><td>Value per share</td><td>2,402</td></tr><tr><td>CPO</td><td>2030E</td></tr><tr><td>EPS</td><td>140</td></tr><tr><td>P/E</td><td>30</td></tr><tr><td>Value per share</td><td>4,210</td></tr><tr><td>Value per share discount back to 2028E</td><td>3,239</td></tr><tr><td>Total value per share</td><td>5,641<

[中间内容因长度限制已省略]

ilable material. Any unauthorized use or disclosure is prohibited. Receipt and review of this information constitutes your agreement not to redistribute, retransmit, or disclose to others the contents, opinions, conclusion, or information contained herein (including any investment recommendations, estimates or price targets) without first obtaining express permission from an authorized officer of BofA.

Materials prepared by BofA Global Research personnel are based on public information. Facts and views presented in this material have not been reviewed by, and may not reflect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

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
