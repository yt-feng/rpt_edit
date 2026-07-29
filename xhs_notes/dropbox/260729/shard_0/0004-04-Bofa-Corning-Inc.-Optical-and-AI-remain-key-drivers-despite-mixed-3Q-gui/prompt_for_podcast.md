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
Corning Inc.

# Optical and AI remain key drivers despite mixed 3Q guide; PO to \$200

Reiterate Rating: BUY | PO: 200.00 USD | Price: 121.28 USD

## Strong enterprise growth +65% y/y offset by weak guide

GLW reported F2Q results with accelerating growth in Ent. Optical (Gen AI contribution nearly doubling y/y) but this was overlooked due to 1) weaker than expected 3Q guide, 2) Segments (ex. Ent. & Solar) seeing slow growth, and 3) lack of incremental hyperscaler color. We view our core thesis on GLW as unchanged (this is a multi-year growth story) but understand the premium GLW has recently been commanding (>60x C26E, vs 5-year median of 22x) comes with expectations of outperformance. While the guide for 3Q (\$4.9-\$5.0bn revs) was slightly below consensus, commentary around the Ent. business shows datacenter demand remains robust with 3Q seeing q/q growth after a strong 2Q. Reiterate Buy on structurally higher revs in Optical & incremental OP from new MAPs.

## Bright spots of the quarter: Enterprise, Solar, & margins

Ent. Optical strength was driven by robust demand exceeding capacity and accelerating adoption of high-density connectorized content. Notably, Ent. revs reflect only scale-out demand and we cont. to expect upside from scale-up & CPO adoption. Solar revs grew +90% y/y despite the wafer transition and mgmt. expects q/q growth and margin leverage as transition headwinds subside. OMs grew +184bps y/y & +70bps q/q reflecting higher margin fiber content and a slight benefit from pricing.

## Weaker spots & things bears will point to

F3Q guide of +17% y/y growth at the high-end, (flat to 2Q growth) appears to not fully reflect the strength and commentary surrounding the Ent. business. Carrier revs in 2Q were soft, reflecting pull-ins in 1Q. Capex is stepping up materially in the 2H to \$2bn (vs \$1.7bn prior) for F26 reflecting capacity expansions. Glass Innovations in 2H implies cont. muted growth due to the overall hand-held industry despite the Apple Foldable launch in 3Q. Ent. Optical growth is increasingly tied to LTAs (limiting upside if pricing accelerates). Scale Up & CPO timing remains uncertain.

## Adjusting estimates; PO to \$200

PO moves to \$200 on 31x C28E EPS of \$6.46 (prior \$243 on 37x C28E of \$6.50). Lower multiple to reflect the broader concern around the sustainability of datacenter build out.

<table><tr><td>Estimates (Dec) (US$)</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>EPS</td><td>1.97</td><td>2.54</td><td>3.30</td><td>4.99</td><td>6.46</td></tr><tr><td>GAAP EPS</td><td>0.59</td><td>1.84</td><td>2.45</td><td>3.99</td><td>5.35</td></tr><tr><td>EPS Change (YoY)</td><td>15.9%</td><td>28.9%</td><td>29.9%</td><td>51.2%</td><td>29.5%</td></tr><tr><td>Consensus EPS (Bloomberg)</td><td></td><td></td><td>3.17</td><td>4.21</td><td>5.83</td></tr><tr><td>Consensus EPS (Visible Alpha)</td><td></td><td></td><td>3.19</td><td>4.46</td><td>5.71</td></tr><tr><td>DPS</td><td>1.12</td><td>1.12</td><td>1.12</td><td>1.12</td><td>1.12</td></tr><tr><td colspan="6">Valuation (Dec)</td></tr><tr><td>P/E</td><td>61.6x</td><td>47.7x</td><td>36.8x</td><td>24.3x</td><td>18.8x</td></tr><tr><td>GAAP P/E</td><td>205.6x</td><td>65.9x</td><td>49.5x</td><td>30.4x</td><td>22.7x</td></tr><tr><td>Dividend Yield</td><td>0.9%</td><td>0.9%</td><td>0.9%</td><td>0.9%</td><td>0.9%</td></tr><tr><td>EV / EBITDA*</td><td>29.7x</td><td>25.6x</td><td>20.4x</td><td>14.9x</td><td>11.4x</td></tr><tr><td>Free Cash Flow Yield*</td><td>0.9%</td><td>1.4%</td><td>2.1%</td><td>1.6%</td><td>3.3%</td></tr></table>

\* For full definitions of iQmethod $^{SM}$ measures, see page 6.

BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.
Refer to important disclosures on page 7 to 9. Analyst Certification on page 5. Price Objective Basis/Risk on page 5.
12999836

## 28 July 2026

Equity

## Key Changes

<table><tr><td>(US$)</td><td>Previous</td><td>Current</td></tr><tr><td>Price Obj.</td><td>243.00</td><td>200.00</td></tr><tr><td>2026E Rev (m)</td><td>19,322.9</td><td>19,180.2</td></tr><tr><td>2027E Rev (m)</td><td>24,879.9</td><td>24,872.8</td></tr><tr><td>2028E Rev (m)</td><td>30,565.6</td><td>30,446.1</td></tr><tr><td>2027E EPS</td><td>5.00</td><td>4.99</td></tr><tr><td>2028E EPS</td><td>6.50</td><td>6.46</td></tr></table>

## Wamsi Mohan

Research Analyst
BofAS
+1 646 855 3854
wamsi.mohan@bofa.com

## Ruplu Bhattacharya

Research Analyst
BofAS
+1 646 855 0315
ruplu.bhattacharya@bofa.com

## Aisling Grueninger

Research Analyst
BofAS
+1 646 855 4273
aisling.grueninger@bofa.com

## Ryan Seungin Choi

Research Analyst
BofAS
+1 646 743 0587
ryan.choi2@bofa.com

## Stock Data

<table><tr><td>Price</td><td>121.28 USD</td></tr><tr><td>Price Objective</td><td>200.00 USD</td></tr><tr><td>Date Established</td><td>28-Jul-2026</td></tr><tr><td>Investment Opinion</td><td>C-1-7</td></tr><tr><td>52-Week Range</td><td>54.92 USD - 271.78 USD</td></tr><tr><td>Mrkt Val (mn) / Shares Out (mn)</td><td>104,181 USD / 859.0</td></tr><tr><td>Free Float</td><td>91.9%</td></tr><tr><td>Average Daily Value (mn)</td><td>1828.30 USD</td></tr><tr><td>BofA Ticker / Exchange</td><td>GLW / NYS</td></tr><tr><td>Bloomberg / Reuters</td><td>GLW US / GLW.N</td></tr><tr><td>ROE (2026E)</td><td>22.6%</td></tr><tr><td>Net Dbt to Eqty (Dec-2025A)</td><td>56.1%</td></tr></table>

Abbreviations on Page 4

## iQprofile $^{SM}$ Corning Inc.

## iQmethod $^{SM}$ – Bus Performance\*

<table><tr><td>(US$ Millions)</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Return on Capital Employed</td><td>9.1%</td><td>11.3%</td><td>13.1%</td><td>13.3%</td><td>14.1%</td></tr><tr><td>Return on Equity</td><td>15.3%</td><td>19.6%</td><td>22.6%</td><td>28.7%</td><td>29.7%</td></tr><tr><td>Operating Margin</td><td>17.5%</td><td>19.3%</td><td>21.8%</td><td>23.3%</td><td>24.3%</td></tr><tr><td>Free Cash Flow</td><td>974</td><td>1,413</td><td>2,214</td><td>1,684</td><td>3,411</td></tr></table>

## iQmethod $^{SM}$ – Quality of Earnings\*

<table><tr><td>(US$ Millions)</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Cash Realization Ratio</td><td>1.1x</td><td>1.2x</td><td>1.5x</td><td>1.1x</td><td>1.2x</td></tr><tr><td>Asset Replacement Ratio</td><td>0.7x</td><td>1.0x</td><td>1.4x</td><td>1.7x</td><td>1.2x</td></tr><tr><td>Tax Rate</td><td>16.3%</td><td>13.0%</td><td>14.4%</td><td>30.8%</td><td>35.4%</td></tr><tr><td>Net Debt-to-Equity Ratio</td><td>49.2%</td><td>56.1%</td><td>38.6%</td><td>29.9%</td><td>13.8%</td></tr><tr><td>Interest Cover</td><td>7.7x</td><td>9.4x</td><td>11.1x</td><td>20.7x</td><td>24.7x</td></tr></table>

Income Statement Data (Dec)

<table><tr><td>(US$ Millions)</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Sales</td><td>14,469</td><td>16,408</td><td>19,180</td><td>24,873</td><td>30,446</td></tr><tr><td>% Change</td><td>6.5%</td><td>13.4%</td><td>16.9%</td><td>29.7%</td><td>22.4%</td></tr><tr><td>Gross Profit</td><td>5,523</td><td>6,293</td><td>7,586</td><td>10,025</td><td>12,578</td></tr><tr><td>% Change</td><td>12.0%</td><td>13.9%</td><td>20.5%</td><td>32.2%</td><td>25.5%</td></tr><tr><td>EBITDA</td><td>3,880</td><td>4,507</td><td>5,651</td><td>7,718</td><td>10,144</td></tr><tr><td>% Change</td><td>7.4%</td><td>16.2%</td><td>25.4%</td><td>36.6%</td><td>31.4%</td></tr><tr><td>Net Interest &amp; Other Income</td><td>(246)</td><td>(242)</td><td>(354)</td><td>(192)</td><td>(220)</td></tr><tr><td>Net Income (Adjusted)</td><td>1,699</td><td>2,199</td><td>2,887</td><td>4,357</td><td>5,617</td></tr><tr><td>% Change</td><td>16.1%</td><td>29.4%</td><td>31.3%</td><td>50.9%</td><td>28.9%</td></tr></table>

## Free Cash Flow Data (Dec)

<table><tr><td>(US$ Millions)</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Net Income from Cont Operations (GAAP)</td><td>592</td><td>1,742</td><td>2,355</td><td>3,655</td><td>4,844</td></tr><tr><td>Depreciation &amp; Amortization</td><td>1,350</td><td>1,347</td><td>1,473</td><td>1,921</td><td>2,737</td></tr><tr><td>Change in Working Capital</td><td>(303)</td><td>(183)</td><td>102</td><td>(1,404)</td><td>(1,648)</td></tr><tr><td>Deferred Taxation Charge</td><td>(33)</td><td>(355)</td><td>(101)</td><td>0</td><td>0</td></tr><tr><td>Other Adjustments, Net</td><td>333</td><td>144</td><td>457</td><td>690</td><td>855</td></tr><tr><td>Capital Expenditure</td><td>(965)</td><td>(1,282)</td><td>(2,073)</td><td>(3,177)</td><td>(3,377)</td></tr><tr><td>Free Cash Flow</td><td>974</td><td>1,413</td><td>2,214</td><td>1,684</td><td>3,411</td></tr><tr><td>% Change</td><td>58.4%</td><td>45.1%</td><td>56.7%</td><td>-23.9%</td><td>102.5%</td></tr><tr><td>Share / Issue Repurchase</td><td>(165)</td><td>(162)</td><td>9</td><td>(365)</td><td>(260)</td></tr><tr><td>Cost of Dividends Paid</td><td>(986)</td><td>(999)</td><td>(985)</td><td>(977)</td><td>(973)</td></tr><tr><td>Change in Debt</td><td>(118)</td><td>(79)</td><td>(242)</td><td>0</td><td>0</td></tr></table>

## Balance Sheet Data (Dec)

<table><tr><td>(US$ Millions)</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Cash &amp; Equivalents</td><td>1,768</td><td>1,526</td><td>2,910</td><td>3,252</td><td>5,430</td></tr><tr><td>Trade Receivables</td><td>2,053</td><td>2,779</td><td>2,733</td><td>3,407</td><td>4,338</td></tr><tr><td>Other Current Assets</td><td>4,171</td><td>4,631</td><td>5,795</td><td>7,004</td><td>8,011</td></tr><tr><td>Property, Plant &amp; Equipment</td><td>13,359</td><td>14,825</td><td>15,567</td><td>16,915</td><td>17,648</td></tr><tr><td>Other Non-Current Assets</td><td>6,384</td><td>7,215</td><td>7,066</td><td>6,974</td><td>6,882</td></tr><tr><td>Total Assets</td><td>27,735</td><td>30,976</td><td>34,070</td><td>37,553</td><td>42,308</td></tr><tr><td>Short-Term Debt</td><td>326</td><td>804</td><td>668</td><td>668</td><td>668</td></tr><tr><td>Other Current Liabilities</td><td>4,593</td><td>4,824</td><td>5,326</td><td>5,806</td><td>6,095</td></tr><tr><td>Long-Term Debt</td><td>6,885</td><td>7,630</td><td>7,756</td><td>7,756</td><td>7,756</td></tr><tr><td>Other Non-Current Liabilities</td><td>4,861</td><td>5,411</td><td>6,052</td><td>6,052</td><td>6,052</td></tr><tr><td>Total Liabilities</td><td>16,665</td><td>18,669</td><td>19,802</td><td>20,282</td><td>20,571</td></tr><tr><td>Total Equity</td><td>11,070</td><td>12,307</td><td>14,269</td><td>17,271</td><td>21,737</td></tr><tr><td>Total Equity &amp; Liabilities</td><td>27,735</td><td>30,976</td><td>34,070</td><td>37,553</td><td>42,308</td></tr></table>

\* For full definitions of iQmethod $^{SM}$ measures, see page 6.

## Company Sector

Electrical Equipment

## Company Description

Corning's Display Technologies (25% of sales) manufactures liquid crystal display (LCD) glass for flat-panel displays. Telecommunications (32% of sales) produces optical fiber and cable, component hardware and equipment, and photonic components for the telecommunications, CATV and networking industry. Environmental Technologies (12% of sales) produces specialized glass, glass ceramic and polymer-based products for the automotive industry.

## Investment Rationale

Our Buy rating on Corning is based on glass supply and demand remaining in balance and glass price declines remaining moderate (post COVID-19) while the Optical market benefits from a cyclical recovery of carrier spending and a secular benefit from Gen AI. Corning has a strong capital return program. Increased adoption of Gorilla Glass in other end markets (automobiles), growth of Fiber-to-the-Home and gas particulate filters should be catalysts for Corning.

## Stock Data

<table><tr><td>Average Daily Volume</td><td>15,075,029</td></tr></table>

## Quarterly Earnings Estimates

<table><tr><td></td><td>2025</td><td>2026</td></tr><tr><td>Q1</td><td>0.54A</td><td>0.70A</td></tr><tr><td>Q2</td><td>0.60A</td><td>0.78E</td></tr><tr><td>Q3</td><td>0.67A</td><td>0.88E</td></tr><tr><td>Q4</td><td>0.72A</td><td>0.94E</td></tr></table>

<table><tr><td colspan="14">GLW Earnings Model</td></tr><tr><td rowspan="2">Wamsi Mohan($ in millions except EPS)</td><td colspan="4">2025</td><td colspan="4">2026E</td><td colspan="5"></td></tr><tr><td>1Q25A</td><td>2Q25A</td><td>3Q25A</td><td>4Q25A</td><td>1Q26A</td><td>2Q26A</td><td>3Q26E</td><td>4Q26E</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td colspan="14">Non-GAAP Income Statement</td></tr><tr><td>Sales</td><td>3,679</td><td>4,045</td><td>4,272</td><td>4,412</td><td>4,345</td><td>4,738</td><td>5,007</td><td>5,090</td><td>14,469</td><td>16,408</td><td>19,180</td><td>24,873</td><td>30,446</td></tr><tr><td>Cost of sales</td><td>2,284</td><td>2,493</td><td>2,608</td><td>2,730</td><td>2,645</td><td>2,864</td><td>2,997</td><td>3,089</td><td>8,946</td><td>10,115</td><td>11,594</td><td>14,847</td><td>17,868</td></tr><tr><td>Gross profit</td><td>1,395</td><td>1,552</td><td>1,664</td><td>1,682</td><td>1,700</td><td>1,874</td><td>2,010</td><td>2,002</td><td>5,523</td><td>6,293</td><td>7,586</td><td>10,025</td><td>12,578</td></tr><tr><td>SG&amp;A</td><td>463</td><td>508</td><td>550</td><td>507</td><td>546</td><td>590</td><td>605</td><td>534</td><td>1,915</td><td>2,028</td><td>2,275</td><td>2,751</td><td>3,364</td></tr><tr><td>R&amp;D</td><td>271</td><td>274</td><td>276</td><td>284</td><td>278</td><td>295</td><td>283</td><td>277</td><td>1,078</td><td>1,105</td><td>1,133</td><td>1,477</td><td>1,806</td></tr><tr><td>Amort. of purchased intangibles</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Operating Income</td><td>661</td><td>770</td><td>838</td><td>891</td><td>876</td><td>989</td><td>1,122</td><td>1,191</td><td>2,530</td><td>3,160</td><td>4,178</td><td>5,797</td><td>7,408</td></tr><tr><td>Interest income</td><td>12</td><td>5</td><td>10</td><td>11</td><td>9</td><td>12</td><td>0</td><td>0</td><td>47</td><td>38</td><td>21</td><td>40</td><td>32</td></tr><tr><td>Interest expense</td><td>-82</td><td>-83</td><td>-78</td><td>-93</td><td>-92</td><td>-94</td><td>-95</td><td>-95</td><td>-329</td><td>-336</td><td>-376</td><td>-280</td><td>-300</td></tr><tr><td>Translated earnings contract gain/loss</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Other Net</td><td>25</td><td>-3</td><td>9</td><td>10</td><td>4</td><td>-9</td><td>-5</td><td>-5</td><td>-2</td><td>41</td><td>-15</td><td>32</td><td>32</td></tr><tr><td>Pretax income</td><td>616</td><td>689</td><td>779</td><td>819</td><td>797</td><td>898</td><td>1,022</td><td>1,091</td><td>2,246</td><td>2,903</td><td>3,808</td><td>5,589</td><td>7,172</td></tr><tr><td>Taxes</td><td>121</td><td>135</td><td>154</td><td>148</td><td>148</td><td>168</td><td>189</td><td>199</td><td>461</td><td>558</td><td>704</td><td>1,062</td><td>1,363</td></tr><tr><td>NCI</td><td>28</td><td>31</td><td>40</td><td>47</td><td>37</td><td>50</td><td>60</td><td>70</td><td>86</td><td>146</td><td>217</td><td>170</td><td>192</td></tr><tr><td>Net income att. to GLW</td><td>467</td><td>523</td><td>585</td><td>624</td><td>612</td><td>680</td><td>773</td><td>822</td><td>1,699</td><td>2,199</td><td>2,887</td><td>4,357</td><td>5,617</td></tr><tr><td>Adjusted EPS</td><td>$0.54</td><td>$0.60</td><td>$0.67</td><td>$0.72</td><td>$0.70</td><td>$0.78</td><td>$0.88</td><td>$0.94</td><td>$1.97</td><td>$2.54</td><td>$3.30</td><td>$4.99</td><td>$6.46</td></tr><tr><td>Average shares (mn basic)</td><td>855</td><td>855</td><td>856</td><td>856</td><td>857</td><td>862</td><td>862</td><td>862</td><td>854</td><td>856</td><td>861</td><td>862</td><td>862</td></tr><tr><td>Average shares (mn diluted)</td><td>866</td><td>865</td><td>868</td><td>868</td><td>871</td><td>875</td><td>875</td><td>875</td><td>864</td><td>867</td><td>874</td><td>873</td><td>869</td></tr><tr><td>Dividend</td><td>$0.28</td><td>$0.28</td><td>$0.28</td><td>$0.28</td><td>$0.28</td><td>$0.28</td><td>$0.28</td><td>$0.28</td><td>$1.12</td><td>$1.12</td><td>$1.12</td><td>$1.12</td><td>$1.12</td></tr><tr><td>Payout</td><td>52%</td><td>46%</td><td>42%</td><td>39%</td><td>40%</td><td>36%</td><td>32%</td><td>30%</td><td>57%</td><td>44%</td><td>34%</td><td>22%</td><td>17%</td></tr><tr><td colspan="14">As % of Revenue</td></tr><tr><td>Cost of sales</td><td>62.1%</td><td>61.6%</td><td>61.0%</td><td>61.9%</td><td>60.9%</td><td>60.4%</td><td>59.8%</td><td>60.7%</td><td>61.8%</td><td>61.6%</td><td>60.4%</td><td>59.7%</td><td>58.7%</td></tr><tr><td>Chg in bps</td><td>-109</td><td>-47</td><td>24</td><td>44</td><td>-121</td><td>-118</td><td>-120</td><td>-120</td><td>-185</td><td>-18</td><td>-120</td><td>-76</td><td>-101</td></tr><tr><td>Gross profit</td><td>37.9%</td><td>38.4%</td><td>39.0%</td><td>38.1%</td><td>39.1%</td><td>39.6%</td><td>40.2%</td><td>39.3%</td><td>38.2%</td><td>38.4%</td><td>39.6%</td><td>40.3%</td><td>41.3%</td></tr><tr><td>Chg in bps</td><td>109</td><td>47</td><td>-24</td><td>-44</td><td>121</td><td>118</td><td>120</td><td>120</td><td>185</td><td>18</td><td>120</td><td>76</td><td>101</td></tr><tr><td>SG&amp;A</td><td>12.6%</td><td>12.6%</td><td>12.9%</td><td>11.5%</td><td>12.6%</td><td>12.5%</td><td>12.1%</td><td>10.5%</td><td>13.2%</td><td>12.4%</td><td>11.9%</td><td>11.1%</td><td>11.1%</td></tr><tr><td>Chg in bps</td><td>-95</td><td>-68</td><td>-41</td><td>-144</td><td>-2</td><td>-11</td><td>-80</td><td>-100</td><td>97</td><td>-88</td><td>-50</td><td>-80</td><td>-1</td></tr><tr><td>R&amp;D</td><td>7.4%</td><td>6.8%</td><td>6.5%</td><td>6.4%</td><td>6.4%</td><td>6.2%</td><td>5.7%</td><td>5.4%</td><td>7.5%</td><td>6.7%</td><td>5.9%</td><td>5.9%</td><td>5.9%</td></tr><tr><td>Chg in bps</td><td>-46</td><td>-50</td><td>-117</td><td>-69</td><td>-97</td><td>-55</td><td>-80</td><td>-100</td><td>-10</td><td>-72</td><td>-83</td><td>3</td><td>-1</td></tr><tr><td>Operating Income</td><td>18.0%</td><td>19.0%</td><td>19.6%</td><td>20.2%</td><td>20.2%</td><td>20.9%</td><td>22.4%</td><td>23.4%</td><td>17.5%</td><td>19.3%</td><td>21.8%</td><td>23.3%</td><td>24.3%</td></tr><tr><td>Chg in bps</td><td>250</td><td>164</td><td>135</td><td>169</td><td>219</td><td>184</td><td>280</td><td>320</td><td>97</td><td>177</td><td>253</td><td>152</td><td>102</td></tr><tr><td>Incremental OMs Y/Y

[中间内容因长度限制已省略]

nions, conclusion, or information contained herein (including any investment recommendations, estimates or price targets) without first obtaining express permission from an authorized officer of BofA.

Materials prepared by BofA Global Research personnel are based on public information. Facts and views presented in this material have not been reviewed by, and may not reflect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Subject to the quiet period applicable under laws of the various jurisdictions in which we distribute research reports and other legal and BofA policy-related restrictions on the publication of research reports, fundamental equity reports are produced on a regular basis as necessary to keep the investment recommendation current.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies. Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
