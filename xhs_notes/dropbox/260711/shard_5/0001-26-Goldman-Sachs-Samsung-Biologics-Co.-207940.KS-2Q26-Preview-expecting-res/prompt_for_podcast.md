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
# Samsung Biologics Co. (207940.KS)

2Q26 Preview: expecting resilient earnings on FX tailwinds; strike impact shifts to 3Q with recovery thereafter

207940.KS 12m Price Target: W2,000,000 Price: W1,363,000 Upside: $46.7\%$

Samsung Biologics is scheduled to report 2Q26 results on July 23rd, and we expect another strong quarter, with 2Q26 revenue growth of c.+30% y/y and adjusted net profit growth of c.+41% for CDMO business to reach W1,314bn/470bn, 0%/7% above VA consensus, supported by continued full utilization of Plants 1–4 and the initial ramp-up of Plant 5 on a more favorable FX, driving operating margin in the mid-40% range. Importantly, while Plant 5 contribution begins to emerge, we expect limited margin dilution given its relatively small base versus the existing Korea facilities and ongoing efficiency improvements highlighted by management.

GS View: We see the recent pullback as an attractive opportunity to add positions, with scope for sentiment to improve as uncertainties surrounding the labor strike gradually fade and order conversion becomes more visible over the coming quarters. We believe the long-term investment case remains intact, supported by high utilization across existing facilities, continued capacity expansion, and sustained demand from global biologics outsourcing. At \~31x 12-month forward P/E, versus its five-year historical average of \~68x, current valuation appears increasingly attractive relative to its long-term growth prospects.

On FX, we see ongoing tailwinds as USD/KRW at \~1,500 in 2Q26, remains 7% above management's embedded assumption of \~1,400, which should partly offset any near-term operational headwinds and limit downside risk to FY26 guidance of 15–20% revenue growth, where we forecast 23% revenue growth after including the newly consolidated US facilities. Per our previous analysis, with 95% of the company's revenue denominated in US dollars and most costs in Korean won, a 2.5% chg of the USD/KRW exchange rate change would lead to a 5% change in EBIT (see Exhibit 13 in our previous report).

■ On labor dynamics, the partial strike in early May is unlikely

BUY

Chris Pan, CFA  
+852-2978-7993 | chris.pan@gs.com  
GS (Asia) L.L.C.

Ziyi Chen  
+852-2978-0526 | ziyi.chen@gs.com  
GS (Asia) L.L.C.

Key Data

Market cap: W63.1tr / \$42.0bn  
Enterprise value: W62.1tr / \$41.4bn  
3m ADTV: W89.7bn / \$59.6mn  
South Korea  
China & Korea Medtech & Services  
M&A Rank: 3  
Leases incl. in net debt & EV?: Yes

GS Forecast

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Revenue (W bn) New</td><td>4,557.0</td><td>5,589.2</td><td>6,554.3</td><td>7,461.9</td></tr><tr><td>Revenue (W bn) Old</td><td>4,557.0</td><td>5,386.2</td><td>6,343.2</td><td>7,166.0</td></tr><tr><td>EBITDA (W bn)</td><td>2,438.5</td><td>2,804.8</td><td>3,405.7</td><td>3,866.3</td></tr><tr><td>EPS (W) New</td><td>38,539</td><td>42,852</td><td>51,505</td><td>58,207</td></tr><tr><td>EPS (W) Old</td><td>38,539</td><td>41,633</td><td>50,994</td><td>57,881</td></tr><tr><td>P/E (X)</td><td>41.1</td><td>31.8</td><td>26.5</td><td>23.4</td></tr><tr><td>P/B (X)</td><td>9.9</td><td>6.7</td><td>5.4</td><td>4.4</td></tr><tr><td>Dividend yield (%)</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>CROCI (%)</td><td>23.9</td><td>23.8</td><td>24.3</td><td>23.6</td></tr><tr><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td>EPS (W)</td><td>10,132</td><td>10,145</td><td>10,344</td><td>12,231</td></tr></table>

GS Factor Profile

![](images/e065c0a885cb06ebaeec1c832d17a58931838b4b52f3ba608a3cfe33431dbbea.jpg)  
Source: Company data, GS estimates. See disclosures for details.

Samsung Biologics Co. (207940.KS) Rating since Apr 29, 2024  
Ratios & Valuation

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>P/E (X)</td><td>41.1</td><td>31.8</td><td>26.5</td><td>23.4</td></tr><tr><td>P/B (X)</td><td>9.9</td><td>6.7</td><td>5.4</td><td>4.4</td></tr><tr><td>FCF yield (%)</td><td>0.8</td><td>(0.2)</td><td>2.7</td><td>0.9</td></tr><tr><td>EV/EBITDAR (X)</td><td>29.6</td><td>22.1</td><td>17.7</td><td>15.5</td></tr><tr><td>EV/EBITDA (excl. leases) (X)</td><td>29.6</td><td>22.1</td><td>17.7</td><td>15.5</td></tr><tr><td>CROCI (%)</td><td>23.9</td><td>23.8</td><td>24.3</td><td>23.6</td></tr><tr><td>ROE (%)</td><td>19.3</td><td>23.6</td><td>22.5</td><td>20.5</td></tr><tr><td>Net debt/equity (%)</td><td>(15.1)</td><td>(10.7)</td><td>(22.8)</td><td>(22.4)</td></tr><tr><td>Net debt/equity (excl. leases) (%)</td><td>(15.1)</td><td>(10.7)</td><td>(22.8)</td><td>(22.4)</td></tr><tr><td>Interest cover (X)</td><td>14.6</td><td>34.6</td><td>42.5</td><td>48.3</td></tr><tr><td>Days inventory outst, sales</td><td>166.5</td><td>174.6</td><td>158.8</td><td>159.8</td></tr><tr><td>Receivable days</td><td>58.6</td><td>58.6</td><td>58.6</td><td>58.6</td></tr><tr><td>Days payable outstanding</td><td>144.2</td><td>80.0</td><td>80.0</td><td>80.0</td></tr><tr><td>DuPont ROE (%)</td><td>21.8</td><td>21.1</td><td>20.2</td><td>18.6</td></tr><tr><td>Turnover (X)</td><td>0.4</td><td>0.4</td><td>0.4</td><td>0.4</td></tr><tr><td>Leverage (X)</td><td>1.5</td><td>1.4</td><td>1.3</td><td>1.3</td></tr><tr><td>Gross cash invested (ex cash) (W)</td><td>8,650.9</td><td>11,108.3</td><td>11,923.3</td><td>14,800.3</td></tr><tr><td>Average capital employed (W)</td><td>7,190.1</td><td>7,343.5</td><td>8,747.2</td><td>10,165.6</td></tr><tr><td>BVPS (W)</td><td>160,192</td><td>203,044</td><td>254,550</td><td>312,757</td></tr></table>

<table><tr><td colspan="5">Growth &amp; Margins (%)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue growth</td><td>30.3</td><td>22.7</td><td>17.3</td><td>13.8</td></tr><tr><td>EBITDA growth</td><td>27.8</td><td>15.0</td><td>21.4</td><td>13.5</td></tr><tr><td>EPS growth</td><td>64.7</td><td>11.2</td><td>20.2</td><td>13.0</td></tr><tr><td>DPS growth</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>EBIT margin</td><td>45.4</td><td>43.8</td><td>45.8</td><td>45.8</td></tr><tr><td>EBITDA margin</td><td>53.5</td><td>50.2</td><td>52.0</td><td>51.8</td></tr><tr><td>Net income margin</td><td>35.4</td><td>35.5</td><td>36.4</td><td>36.1</td></tr></table>

![](images/77d9db70d847200e9e01de7b73a8d295faf3cdbc193d10f152ad004c89197edb.jpg)  
Source: FactSet. Price as of 8 Jul 2026 close.

Income Statement (W bn)

<table><tr><td colspan="5">Income Statement (W bn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue</td><td>4,557.0</td><td>5,589.2</td><td>6,554.3</td><td>7,461.9</td></tr><tr><td>Cost of goods sold</td><td>(2,040.3)</td><td>(2,569.6)</td><td>(2,901.9)</td><td>(3,326.1)</td></tr><tr><td>SG&amp;A</td><td>(447.4)</td><td>(572.5)</td><td>(651.7)</td><td>(719.6)</td></tr><tr><td>R&amp;D</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other operating inc./(exp.)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>EBITDA</td><td>2,438.5</td><td>2,804.8</td><td>3,405.7</td><td>3,866.3</td></tr><tr><td>Depreciation &amp; amortization</td><td>(369.3)</td><td>(357.7)</td><td>(405.0)</td><td>(450.1)</td></tr><tr><td>EBIT</td><td>2,069.2</td><td>2,447.1</td><td>3,000.7</td><td>3,416.2</td></tr><tr><td>Net interest inc./(exp.)</td><td>9.4</td><td>(10.4)</td><td>(10.4)</td><td>(10.4)</td></tr><tr><td>Income/(loss) from associates</td><td>43.1</td><td>43.1</td><td>43.1</td><td>43.1</td></tr><tr><td>Pre-tax profit</td><td>2,118.6</td><td>2,579.8</td><td>3,103.4</td><td>3,508.9</td></tr><tr><td>Provision for taxes</td><td>(504.6)</td><td>(596.1)</td><td>(719.2)</td><td>(814.5)</td></tr><tr><td>Minority interest</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Preferred dividends</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (pre-exceptionals)</td><td>1,614.0</td><td>1,983.7</td><td>2,384.2</td><td>2,694.5</td></tr><tr><td>Post-tax exceptionals</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (post-exceptionals)</td><td>1,784.0</td><td>1,983.7</td><td>2,384.2</td><td>2,694.5</td></tr><tr><td>EPS (basic, pre-except) (W)</td><td>34,866</td><td>42,852</td><td>51,505</td><td>58,207</td></tr><tr><td>EPS (diluted, pre-except) (W)</td><td>38,539</td><td>42,852</td><td>51,505</td><td>58,207</td></tr><tr><td>EPS (basic, post-except) (W)</td><td>38,539</td><td>42,852</td><td>51,505</td><td>58,207</td></tr><tr><td>EPS (diluted, post-except) (W)</td><td>38,539</td><td>42,852</td><td>51,505</td><td>58,207</td></tr><tr><td>DPS (W)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Div. payout ratio (%)</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr></table>

<table><tr><td colspan="5">Balance Sheet (W bn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Cash &amp; cash equivalents</td><td>1,441.5</td><td>1,325.5</td><td>3,002.1</td><td>3,567.2</td></tr><tr><td>Accounts receivable</td><td>676.6</td><td>1,117.1</td><td>986.3</td><td>1,408.3</td></tr><tr><td>Inventory</td><td>2,275.4</td><td>3,070.7</td><td>2,631.0</td><td>3,904.7</td></tr><tr><td>Other current assets</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total current assets</td><td>4,393.5</td><td>5,513.2</td><td>6,917.0</td><td>8,880.3</td></tr><tr><td>Net PP&amp;E</td><td>6,524.4</td><td>7,564.2</td><td>8,060.4</td><td>9,504.0</td></tr><tr><td>Net intangibles</td><td>60.2</td><td>39.1</td><td>28.5</td><td>23.2</td></tr><tr><td>Total investments</td><td>45.9</td><td>45.9</td><td>45.9</td><td>45.9</td></tr><tr><td>Other long-term assets</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total assets</td><td>11,024.0</td><td>13,162.4</td><td>15,537.5</td><td>18,427.0</td></tr><tr><td>Accounts payable</td><td>485.8</td><td>640.6</td><td>631.5</td><td>826.5</td></tr><tr><td>Short-term debt</td><td>319.7</td><td>319.7</td><td>319.7</td><td>319.7</td></tr><tr><td>Short-term lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other current liabilities</td><td>1,727.0</td><td>1,727.0</td><td>1,727.0</td><td>1,727.0</td></tr><tr><td>Total current liabilities</td><td>2,532.5</td><td>2,687.2</td><td>2,678.2</td><td>2,873.2</td></tr><tr><td>Long-term debt</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Long-term lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other long-term liabilities</td><td>1,076.0</td><td>1,076.0</td><td>1,076.0</td><td>1,076.0</td></tr><tr><td>Total long-term liabilities</td><td>1,076.0</td><td>1,076.0</td><td>1,076.0</td><td>1,076.0</td></tr><tr><td>Total liabilities</td><td>3,608.5</td><td>3,763.2</td><td>3,754.2</td><td>3,949.2</td></tr><tr><td>Preferred shares</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total common equity</td><td>7,415.4</td><td>9,399.1</td><td>11,783.4</td><td>14,477.8</td></tr><tr><td>Minority interest</td><td>--</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Total liabilities &amp; equity</td><td>11,024.0</td><td>13,162.4</td><td>15,537.5</td><td>18,427.0</td></tr><tr><td>Net debt, adjusted</td><td>(1,121.8)</td><td>(1,005.8)</td><td>(2,682.4)</td><td>(3,247.5)</td></tr></table>

<table><tr><td colspan="5">Cash Flow (W bn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Net income</td><td>1,784.0</td><td>1,983.7</td><td>2,384.2</td><td>2,694.5</td></tr><tr><td>D&amp;A add-back</td><td>369.3</td><td>357.7</td><td>405.0</td><td>450.1</td></tr><tr><td>Minority interest add-back</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net (inc)/dec working capital</td><td>(278.7)</td><td>(1,081.1)</td><td>263.8</td><td>(1,203.1)</td></tr><tr><td>Other operating cash flow</td><td>1,862.8</td><td>1,983.7</td><td>2,384.2</td><td>2,694.5</td></tr><tr><td>Cash flow from operations</td><td>1,953.5</td><td>1,260.3</td><td>3,053.0</td><td>1,941.4</td></tr><tr><td>Capital expenditures</td><td>(1,376.3)</td><td>(1,376.3)</td><td>(1,376.3)</td><td>(1,376.3)</td></tr><tr><td>Acquisitions</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Divestitures</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>(399.7)</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Cash flow from investing</td><td>(1,770.4)</td><td>(1,376.3)</td><td>(1,376.3)</td><td>(1,376.3)</td></tr><tr><td>Repayment of lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Dividends paid (common &amp; pref)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Inc/(dec) in debt</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other financing cash flows</td><td>(2,287.4)</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Cash flow from financing</td><td>(341.1)</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Total cash flow</td><td>(158.1)</td><td>(116.0)</td><td>1,676.7</td><td>565.1</td></tr><tr><td>Free cash flow</td><td>577.1</td><td>(116.0)</td><td>1,676.7</td><td>565.1</td></tr></table>

Source: Company data, GS estimates.

to have materially impacted 2Q performance, consistent with management's indication that operations have resumed with no disruption to core processes and no observable order cancellations. The potential earnings impact skewed toward 3Q, where prior commentary suggested possible short-term disruption, albeit partly recoverable in subsequent quarters, supported by relatively high fixed cost structure that helps buffer volatility.

Separately, the company announced several contract amendments in June, including incremental orders with additional US\$62.9mn for an Asian pharma, +US\$69mn for US pharma and +34.3mn for a European pharma. We believe additional large-scale contract wins could help strengthen investor confidence in the sustainability of mid-term earnings growth.

Looking ahead to the 2Q26 earnings call (10am KST/9am HKT, July 23rd), we expect investor focus on (1) guidance sensitivity, particularly around FX, plant ramp-up, and labor cost dynamics; (2) progress on labor negotiations and contingency planning; (3) updates on capacity expansion, including Plant 6 timing and capital allocation priorities across new modalities (e.g., ADCs, CGT); and (4) order pipeline visibility, including potential large multiyear contracts and early traction from US site-related or dual-site manufacturing strategies.

Exhibit 1: Avg USD/KRW at 1,500 in 2Q26 versus 1,400 factored in company guidance  
![](images/cbb5686465e4db21c85c57e00921490c581bb5c8224f9356ae94ddd6bfdb273b.jpg)

Exhibit 2: Samsung Biologics is trading at a 31x 12m fwd P/E Data as of Jul 6, 2026  
![](images/ba6a8c460f5093fdeb92f2f12008daf70ac32b506eb5a2dba7a0680d6b361397.jpg)

Exhibit 3: ...versus Lonza at 30x 12m fwd P/E Data as of Jul 6, 2026

![](images/a6f8112839213c39f20acf93bce1f19cfb24d200ae662063fee1209f66d5b3cf.jpg)  
Source: Bloomberg

Exhibit 4: We see an upward guidance revision for Samsung Bio more likely in 3Q

<table><tr><td></td><td colspan="4">2023Jan-Mar Apr-Jun Jul-Sep Oct-Dec</td><td colspan="4">2024Jan-Mar Apr-Jun Jul-Sep Oct-Dec</td><td colspan="4">2025Jan-Mar Apr-Jun Jul-Sep Oct-Dec</td><td>2026Jan-Mar Apr-May</td><td>The latest guidance</td></tr><tr><td colspan="15">China and Korea</td></tr><tr><td>Samsung Bio</td><td>—</td><td>▲</td><td>—</td><td>▲</td><td>—</td><td>—</td><td>—</td><td>▲</td><td>—</td><td>—</td><td>▲</td><td>—</td><td>—</td><td>FY26 revenue growth of +15-20% y/y</td></tr><tr><td>WuXi AppTec</td><td>—</td><td>—</td><td>—</td><td>▼</td><td>▼</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>▲</td><td>—</td><td>—</td><td>FY26 revenue growth of 18-22% (or 22-26% at constant currency) for continuing operations</td></tr><tr><td>WuXi Bio</td><td>—</td><td>—</td><td>—</td><td>▼</td><td>▼</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>▲</td><td>—</td><td>—</td><td>FY26 revenue growth guidance of 13-17% y/y (16-20% at constant currency)</td></tr><tr><td>WuXi XDC</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>▲</td><td>—</td><td>—</td><td>35% group revenue growth for FY26 on a constant-currency, like-for-like basis (including BioDlink) or 40% on a pro forma basis</td></tr><tr><td>Pharmaron</td><td>—</td><td>—</td><td>▼</td><td>▼</td><td>—</td><td>—</td><td>—</td><td>▼</td><td>—</td><td>—</td><td>—</td><td>▲</td><td>—</td><td>FY26 revenue growth at 12-18% y/y, incorporating a ~3% USD depreciation headwind;</td></tr><tr><td>Asymchem</td><td>—</td><td>—</td><td>▼</td><td>—</td><td>—</td><td>—</td><td>▼</td><td>—</td><td>—</td><td>—</td><td>▲</td><td>—</td><td>—</td><td>19-22% y/y revenue growth in FY26, incorporating a 2-3% FX headwind</td></tr><tr><td colspan="15">EU &amp; US</td></tr><tr><td>Lonza</td><td>—</td><td>—</td><td>▼</td><td>▼</td><td>▲</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>▲</td><td>—</td><td>▲</td><td>FY26 CDMO CER sales growth 11-12%FY26 CDMO core EBITDA margin &gt;32%</td></tr><tr><td>Thermo Fisher</td><td>—</td><td>—</td><td>▼</td><td>▼</td><td>—</td><td>▲</td><td>▲</td><td>—</td><td>—</td><td>▼</td><td>▲</td><td>▲</td><td>—</td><td>FY26 organic revenue growth of 3-4%</td></tr><tr><td colspan="15">India</td></tr><tr><td>Piramal</td><td>n.a.</td><td>n.a.</td><td>—</td><td>▲</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>▼</td><td>—</td><td>—</td><td>▼</td><td>Low to mid-teen topline growth with EBITDA/ PAT growth faster than topline growth in FY27</td></tr><tr><td>Divi&#x27;s Lab</td><td>—</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>Double digit growth with stable margins in FY27</td></tr><tr><td>Syngene</td><td>▲</td><td>—</td><td>▼</td><td>▼</td><td>▼</td><td>—</td><td>—</td><td>▼</td><td>▼</td><td>▼</td><td>—</td><td>—</td><td>▼</td><td>Flattish topline growth in FY27 (H1 expected to be weaker) with mid-20s% margin</td></tr><tr><td>Laurus</td><td>▼</td><td>—</td><td>n.a.</td><td>n.a.</td><td>—</td><td>▼</td><td>—</td><td>—</td><td>—</td><td>▲</td><td>—</td><td>—</td><td>—</td><td>Expects to maintain strong CDMO growth in FY27</td></tr><tr><td>Neuland</td><td>n.a.</td><td>▲</td><td>—</td><td>▼</td><td>—</td><td>—</td><td>—</td><td>▼</td><td>—</td><td>▼</td><td>—</td><td>—</td><td>▼</td><td>Expects a healthy growth in FY27</td></tr><tr><td>Cohance</td><td>▼</td><td>n.a.</td><td>n.a.</td><td>▼</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>n.a.</td><td>▼</td><td>▼</td><td>▼</td><td>Growth should return in F

[中间内容因长度限制已省略]

m impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
