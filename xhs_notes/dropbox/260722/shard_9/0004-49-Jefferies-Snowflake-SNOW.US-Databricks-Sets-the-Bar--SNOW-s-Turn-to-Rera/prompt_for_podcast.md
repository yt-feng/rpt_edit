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
TARGET CHANGE

\*FY end Jan
\*\*\*SNOW - Product Rev
\*\*\*65% core growth, 80% when including LLMs

## Databricks Sets the Bar; SNOW's Turn to Rerate

Databricks is raising \$3B, led by Coatue, at a \$188B valuation – a 40% step-up from the \$134B mark set in Dec 2025. Assuming a 65% revenue CAGR from FY26 to FY28, this implies \~17x FY28 rev. SNOW currently trades at just \~13x FY28 rev on a \$100B EV. We see SNOW as a key beneficiary of this read-through, as a rising tide in data cloud demand lifts multiple boats; even a discount at 15x would imply a \$310 stock and a \~\$115B EV. Reiterate Buy.

Higher growth rate, higher valuation. According to The Information, Databricks is raising a \$3B round, led by Coatue Management, at a \$188B valuation, a 40% step-up from the \$134B mark set in December. There were no fresh financial disclosures alongside the raise, but recall that as of mid-June, Databricks indicated that its annualized F1H27E revenue is expected to surpass \$6.9B, up \~80% y/y (\~65% core, \~80% including LLM monetization), vs our SNOW F1H27E run rate of \~\$5.5B growing 32% y/y. Our what-if scenario below frames Databricks' implied FY28E revenue multiple across a 14-20x range on this valuation. Assuming Databricks compounds revenue at a 65% CAGR from FY26 to FY28E, the \$188B valuation implies \~17x FY28 revenue. SNOW currently trades at \~13x FY28 revenue on \$100B of enterprise value. We see SNOW as a beneficiary of this read-through, and even a discounted multiple at 15x would imply a \$310 stock at \~\$115B in enterprise value.

GPU demand triggered the fundraise. Databricks' CEO recently told CNBC that surging demand for both proprietary and open-source models has left the company running out of GPUs across multiple regions. "We nearly exhausted our GPU capacity in Asia, and demand is rising in countries including Japan, South Korea, the United States, and India. We therefore need to acquire a large number of additional GPUs, which requires significant funding. That demand was what triggered our latest fundraising round: we were inundated with customer requests and needed more GPU capacity".

Rising tide lifts multiple boats. We continue to believe the leading data analytics vendors, Databricks and SNOW, are best positioned to help organizations make sense of their business data and apply AI to run analytical workflows faster and more efficiently, and we expect momentum to build across the board. Databricks' Genie and SNOW's CoCo/CoWork are both gaining traction, with early adoption metrics inflecting. At the same time, we view the two companies' aggressive investment in AI-driven analytics as making the competitive landscape incrementally tougher for PLTR. In particular, Databricks' Genie Ontology adds an enterprise context layer and knowledge graph that could encroach on PLTR's core value proposition.

<table><tr><td>FY (Jan)</td><td>2025A</td><td>2026A</td><td>2027E</td><td>2028E</td></tr><tr><td>Rev. (MM)</td><td>3,626.4</td><td>4,683.9</td><td>6,098.4</td><td>7,713.6</td></tr><tr><td>Cons. Rev.</td><td>3,626.4</td><td>4,683.9</td><td>6,098.4</td><td>7,660.8</td></tr><tr><td>Cons. EPS</td><td>0.82</td><td>1.25</td><td>1.93</td><td>2.73</td></tr><tr><td>EPS</td><td>0.82</td><td>1.25</td><td>1.97</td><td>2.79</td></tr></table>

<table><tr><td>RATING</td><td>BUY</td></tr><tr><td>PRICE</td><td>$268.90^</td></tr><tr><td>PRICE TARGET | % TO PT</td><td>↑$310.00 ($300.00) | +15%</td></tr><tr><td>52W HIGH-LOW</td><td>$284.99 - $118.30</td></tr><tr><td>FLOAT (%) | ADV MM (USD)</td><td>89.8% | 1,710.36</td></tr><tr><td>MARKET CAP</td><td>$100.8B</td></tr><tr><td>TICKER</td><td>SNOW</td></tr></table>

^Prior trading day's closing price unless otherwise noted.

<table><tr><td>FY (Jan)</td><td colspan="3">CHANGE TO JEFe</td><td colspan="2">JEF vs CONS</td></tr><tr><td></td><td>2027</td><td>2028</td><td>2027</td><td>2028</td><td></td></tr><tr><td>REV</td><td>NA</td><td>NA</td><td>NM</td><td>+1%</td><td></td></tr><tr><td>EPS</td><td>NA</td><td>NA</td><td>+2%</td><td>+2%</td><td></td></tr><tr><td>2027 ($)</td><td>Q1A</td><td>Q2</td><td>Q3</td><td>Q4</td><td>FY</td></tr><tr><td>EPS</td><td>0.43</td><td>0.45</td><td>0.52</td><td>0.58</td><td>1.97</td></tr><tr><td>PREV</td><td></td><td></td><td></td><td></td><td></td></tr></table>

Chart 1 - Databricks vs Snowflake: Key Metrics

<table><tr><td>Metrics</td><td>Databricks</td><td>Snowflake</td></tr><tr><td>FY24 Revenue ($M)**</td><td>&gt;$1,600</td><td>$2,667</td></tr><tr><td>% YoY Growth</td><td>&gt;50%</td><td>38%</td></tr><tr><td>FY25 Revenue ($M)**</td><td>&gt;$2,600</td><td>$3,462</td></tr><tr><td>% YoY Growth</td><td>&gt;60%</td><td>30%</td></tr><tr><td>FY26 Revenue ($M)**</td><td>&gt;$4,100</td><td>$4,472</td></tr><tr><td>% YoY Growth</td><td>&gt;55%</td><td>29%</td></tr><tr><td>F3H27 Revenue Run Rate ($M)**</td><td>&gt;$6,900</td><td>$5,505</td></tr><tr><td>% YoY Growth</td><td>80%***</td><td>32%</td></tr><tr><td>Total Customers</td><td>20,000</td><td>13,912</td></tr><tr><td>&gt;1M+ ARR Customers</td><td>&gt;750</td><td>779</td></tr><tr><td>&gt;510M ARR Customers</td><td>~80</td><td>64</td></tr><tr><td>AI Customers</td><td>15,000</td><td>13,600</td></tr><tr><td>Net Retention Rate</td><td>140%</td><td>126%</td></tr><tr><td>Employees</td><td>&gt;10,000</td><td>9,250</td></tr><tr><td>AI ARR ($M)</td><td>&gt;$1,700M</td><td>Not Disclosed</td></tr><tr><td>Data Warehousing ARR ($M) - June &#x27;26</td><td>&gt;$1,500M</td><td>Not Disclosed</td></tr><tr><td>Data Warehousing ARR ($M) - January &#x27;25</td><td>&gt;$800M</td><td>Not Disclosed</td></tr><tr><td>Data Warehousing ARR ($M) - December &#x27;24</td><td>&gt;$600M</td><td>Not Disclosed</td></tr><tr><td>Data Warehousing ARR ($M) - June &#x27;24</td><td>&gt;$400M</td><td>Not Disclosed</td></tr></table>

Source: JEF, Company Data

Chart 2 - What-If Analysis: Databricks' Implied FY28E Revenue Multiple on \$188B Valuation

<table><tr><td>FY26-28E Rev CAGR</td><td>50%</td><td>55%</td><td>60%</td><td>65%</td><td>70%</td><td>75%</td><td>80%</td></tr><tr><td>Implied Multiple</td><td>20.4x</td><td>19.1x</td><td>17.9x</td><td>16.8x</td><td>15.9x</td><td>15.0x</td><td>14.2x</td></tr><tr><td colspan="8">Source: JEF, company data</td></tr></table>

Brent Thill \* | Equity Analyst
+1 (415) 229-1559 | bthill@JEF.com

Bo Yin \* | Equity Associate

+1 (212) 284-2249 | byin@JEF.com

Maximilian Joseph \* | Equity Associate

+1 (212) 778-8926 | mjoseph1@JEF.com

ShengQi Lin \* | Equity Associate

+1 (212) 778-8504 | slin4@JEF.com

## The Long View: Snowflake

Investment Thesis

Snowflake is an early beneficiary of the cloud data warehousing space, and we see rapid growth sustainability on rising penetration among enterprises and potential expansion in the product offering to address adjacent workloads. We like: 1) best-in-class software growth rates; 2) significant room for profitability expansion following evidence of scale in FY21. Key risks: 1) narrowing of competitive differentiation as Redshift, Azure Synapse Analytics, and BigQuery add features/functionality; 2) more limited rev visibility vs traditional SaaS, given consumption-based business model; 3) aggressive valuation premium to high-growth software peers.

Risk/Reward - 12 Month View  
![](images/0ea877162fcd1c7fd4d504b0e949efceda60f7740d14173eaf3df9c3d84f65a1.jpg)

Base Case,

\$310, +15%

• Assumes FY27E/FY28E total rev growth of 30%/27%

• Assumes FY27E/FY28E gross margins of 72%/72%

• Assumes FY27E/FY28E FCF margins of 23%/24%

• PT of \$310 implies 15x FY28E revenue

Upside Scenario, \$350, +30%

• Assumes FY27E/FY28E total rev growth of >30%/>27%

• Assumes FY27E/FY28E gross margins of >72%/>72%

• Assumes FY27E/FY28E FCF margins of >23%/>24%

• PT of \$350 implies 17x FY28E revenue

Downside Scenario, \$180, -33%

• Assumes FY27E/FY28E total rev growth of <30%/<27%

• Assumes FY27E/FY28E gross margins of <72%/<72%

• Assumes FY27E/FY28E FCF margins of <23%/<24%

• PT of \$180 implies 9x FY28E revenue

## Sustainability Matters

Top Material Issue(s): 1) Employee Engagement, Diversity & Inclusion: Snowflake fosters a culture of inclusion across a workforce that is diverse in many ways. Combined with its performance-based culture of individual accountability, it believes this will fuel innovation, encourage authenticity, and serve its customers by enabling every organization to become data-driven. 2) Data Security: As a data company, Snowflake understands the importance of responsibly investing in the governance and technology required to protect data in an increasingly complex, global environment.

\- SNOW is likely to report F2Q27 results in late August

## Catalysts

Company Target(s): 1) The co is in the early stages of developing a sustainability program and has identified three high-impact areas to address in its workplace operations: a) Energy management; b) GHG emissions (Scopes 1-3); c) Waste management solutions.

\- Ramp in adoption of CoCo and CoWork, as well as Data Engineering solutions (Snowpark, Dynamic Tables, Notebooks and others)

\- More proofpoints in successfully embedding AI in the GTM strategy

Qs to Mgmt: 1) What actions/steps is management taking to increase representation of minorities across its employee base? 2) What cost savings do you expect from a more diverse workforce?

ESG Sector Deep Dive

Chart 3 - Non-GAAP Income Statement

<table><tr><td colspan="2">Non-GAAP Income Statement</td></tr><tr><td>Fiscal Quarters</td><td>FY25</td></tr><tr><td>Calendar Quarter</td><td></td></tr><tr><td>Days in Quarter</td><td>366</td></tr><tr><td>Total Revenue</td><td>$3,626.4</td></tr><tr><td>YoY</td><td>29.2%</td></tr><tr><td>QoQ</td><td></td></tr><tr><td>Cost of Product Revenue</td><td>$819.1</td></tr><tr><td>% of Product Revenue</td><td>23.7%</td></tr><tr><td>Cost of Professional Service &amp; Other Revenue</td><td>$158.6</td></tr><tr><td>% of Professional Services &amp; Other Revenue</td><td>96.7%</td></tr><tr><td>Total Cost of Revenue</td><td>$977.7</td></tr><tr><td>% of Total Revenue</td><td>27.0%</td></tr><tr><td>Product Gross Profit</td><td>$2,643.3</td></tr><tr><td>Product Gross Margin</td><td>76.3%</td></tr><tr><td>Professional Services &amp; Other Gross Profit</td><td>$5.4</td></tr><tr><td>Professional Services &amp; Other Gross Margin</td><td>3.3%</td></tr><tr><td>Gross Profit</td><td>$2,648.7</td></tr><tr><td>% margin</td><td>73.0%</td></tr><tr><td>YoY</td><td>27.2%</td></tr><tr><td>Research &amp; Development</td><td>$883.0</td></tr><tr><td>YoY</td><td>44.3%</td></tr><tr><td>QoQ</td><td></td></tr><tr><td>% of Revenue</td><td>24.3%</td></tr><tr><td>Sales &amp; Marketing</td><td>$1,291.2</td></tr><tr><td>YoY</td><td>24.0%</td></tr><tr><td>QoQ</td><td></td></tr><tr><td>% of Revenue</td><td>35.6%</td></tr><tr><td>General &amp; Administrative</td><td>$242.8</td></tr><tr><td>YoY</td><td>21.7%</td></tr><tr><td>QoQ</td><td></td></tr><tr><td>% of Revenue</td><td>6.7%</td></tr><tr><td>Total Operating Expenses</td><td>$2,417.0</td></tr><tr><td>YoY</td><td>30.4%</td></tr><tr><td>Operating Income</td><td>$231.7</td></tr><tr><td>YoY</td><td>0.9%</td></tr><tr><td>% margin</td><td>6.4%</td></tr><tr><td>Other Income</td><td>($35.3)</td></tr><tr><td>Interest Expense</td><td>$209.0</td></tr><tr><td>Pre-tax Income</td><td>$405.4</td></tr><tr><td>Pre-tax Margin</td><td>11.2%</td></tr><tr><td>Provision for Income Taxes</td><td>$105.4</td></tr><tr><td>Effective Tax Rate</td><td>26.0%</td></tr><tr><td>Net income, Non-GAAP</td><td>$300.0</td></tr><tr><td>EPS, Non-GAAP</td><td>$0.82</td></tr><tr><td>Basic Shares</td><td>364.3</td></tr><tr><td>Diluted Shares</td><td>364.3</td></tr></table>

Source: JEF, Company Data

<table><tr><td>FY25366</td><td>F1Q26Apr-2589</td><td>F2Q26Jul-2592</td><td>F3Q26Oct-2592</td><td>F4Q26Jan-2692</td><td>FY26365</td></tr><tr><td>$3,626.4</td><td>$1,042.1</td><td>$1,145.0</td><td>$1,212.9</td><td>$1,284.0</td><td>$4,683.9</td></tr><tr><td>29.2%</td><td>25.7%</td><td>31.8%</td><td>28.7%</td><td>30.1%</td><td>29.2%</td></tr><tr><td></td><td>5.6%</td><td>9.9%</td><td>5.9%</td><td>5.9%</td><td></td></tr><tr><td>$819.1</td><td>$242.7</td><td>$256.9</td><td>$279.2</td><td>$305.2</td><td>$1,083.9</td></tr><tr><td>23.7%</td><td>24.3%</td><td>23.6%</td><td>24.1%</td><td>24.9%</td><td>24.2%</td></tr><tr><td>$158.6</td><td>$47.3</td><td>$52.8</td><td>$53.4</td><td>$58.1</td><td>$211.6</td></tr><tr><td>96.7%</td><td>104.4%</td><td>97.0%</td><td>97.9%</td><td>101.3%</td><td>100.0%</td></tr><tr><td>$977.7</td><td>$290.0</td><td>$309.7</td><td>$332.6</td><td>$363.3</td><td>$1,295.5</td></tr><tr><td>27.0%</td><td>27.8%</td><td>27.0%</td><td>27.4%</td><td>28.3%</td><td>27.7%</td></tr><tr><td>$2,643.3</td><td>$754.1</td><td>$833.6</td><td>$879.2</td><td>$921.5</td><td>$3,388.4</td></tr><tr><td>76.3%</td><td>75.7%</td><td>76.4%</td><td>75.9%</td><td>75.1%</td><td>75.8%</td></tr><tr><td>$5.4</td><td>($2.0)</td><td>$1.7</td><td>$1.2</td><td>($0.8)</td><td>$0.0</td></tr><tr><td>3.3%</td><td>(4.4%)</td><td>3.0%</td><td>2.1%</td><td>(1.3%)</td><td>0.0%</td></tr><tr><td>$2,648.7</td><td>$752.124</td><td>$835.3</td><td>$880.3</td><td>$920.7</td><td>$3,388.4</td></tr><tr><td>73.0%</td><td>72.2%</td><td>73.0%</td><td>72.6%</td><td>71.7%</td><td>72.3%</td></tr><tr><td>27.2%</td><td>23.5%</td><td>31.3%</td><td>28.1%</td><td>28.6%</td><td>27.9%</td></tr><tr><td>$883.0</td><td>$238.8</td><td>$247.1</td><td>$254.5</td><td>$263.2</td><td>$1,003.7</td></tr><tr><td>44.3%</td><td>17.6%</td><td>10.2%</td><td>13.3%</td><td>14.0%</td><td>13.7%</td></tr><tr><td></td><td>3.5%</td><td>3.5%</td><td>3.0%</td><td>3.4%</td><td></td></tr><tr><td>24.3%</td><td>22.9%</td><td>21.6%</td><td>21.0%</td><td>20.5%</td><td>21.4%</td></tr><tr><td>$1,291.2</td><td>$357.9</td><td>$392.1</td><td>$429.6</td><td>$447.9</td><td>$1,627.5</td></tr><tr><td>24.0%</td><td>14.5%</td><td>26.9%</td><td>26.1%</td><td>36.2%</td><td>26.0%</td></tr><tr><td></td><td>8.8%</td><td>9.6%</td><td>9.6%</td><td>4.3%</td><td></td></tr><tr><td>35.6%</td><td>34.3%</td><td>34.2%</td><td>35.4%</td><td>34.9%</td><td>34.7%</td></tr><tr><td>$242.8</td><td>$63.8</td><td>$68.5</td><td>$64.9</td><td>$70.4</td><td>$267.5</td></tr><tr><td>21.7%</td><td>11.6%</td><td>15.8%</td><td>3.1%</td><td>10.6%</td><td>10.2%</td></tr><tr><td></td><td>0.2%</td><td>7.4%</td><td>(5.2%)</td><td>8.4%</td><td></td></tr><tr><td>6.7%</td><td>6.1%</td><td>6.0%</td><td>5.4%</td><td>5.5%</td><td>5.7%</td></tr><tr><td>$2,417.0</td><td>$660.5</td><td>$707.7</td><td>$749.0</td><td>$781.5</td><td>$2,898.7</td></tr><tr><td>30.4%</td><td>15.3%</td><td>19.5%</td><td>19.2%</td><td>25.4%</td><td>19.9%</td></tr><tr><td>$231.7</td><td>$91.7</td><td>$127.6</td><td>$131.3</td><td>$139.2</td><td>$489.7</td></tr><tr><td>0.9%</td><td>152.9%</td><td>191.6%</td><td>123.0%</td><td>49.9%</td><td>111.3%</td></tr><tr><td>6.4%</td><td>8.8%</td><td>11.1%</td><td>10.8%</td><td>10.8%</td><td>10.5%</td></tr><tr><td>($35.3)</td><td>($28.1)</td><td>($5.0)</td><td>($2.1)</td><td>($24.1)</td><td>($59.2)</td></tr><tr><td>$209.0</td><td>$53.2</td><td>$49.5</td><td>$45.7</td><td>$42.4</td><td>$190.8</td></tr><tr><td>$405.4</td><td>$116.8</td><td>$172.1</td><td>$174.9</td><td>$157.5</td><td>$621.3</td></tr><tr><td>11.2%</td><td>11.2%</td><td>15.0%</td><td>14.4%</td><td>12.3%</td><td>13.3%</td></tr><tr><td>$105.4</td><td>$29.2</td><td>$43.1</td><td>$43.7</td><td>$39.4</td><td>$155.3</td></tr><tr><td>26.0%</td><td>25.0%</td><td>25.0%</td><td>25.0%</td><td>25.0%</td><td>25.0%</td></tr><tr><td>$300.0</td><td>$87.6</td><td>$129.0</td><td>$131.3</td><td>$118.1</td><td>$466.0</td></tr><tr><td>$0.82</td><td>$0.24</td><td>$0.35</td><td>$0.35</td><td>$0.32</td><td>$1.25</td></tr><tr><td>364.3</td><td>332.7</td><td>335.2</td><td>339.6</td><td>342.3</td><td>372.7</td></tr><tr><td>364.3</td><td>370.9</td><td>372.4</td><td>373.4</td><td>374.0</td><td>372.7</td></tr></table>

<table><tr><td>F1Q27Apr-2689</td><td>F2Q27EJul-2692</td><td>F3Q27EOct-2692</td><td>F4Q27EJan-2792</td><td>FY27E365</td></tr><tr><td>$1,391.0</td><td>$1,486.1</td><td>$1,566.6</td><td>$1,654.7</td><td>$6,098.4</td></tr><tr><td>33.5%</td><td>29.8%</td><td>29.2%</td><td>28.9%</td><td>30.2%</td></tr><tr><td>8.3%</td><td>6.8%</td><td>5.4%</td><td>5.6%</td><td></td></tr><tr><td>$331.6</td><td>$353.1</td><td>$375.3</td><td>$394.1</td><td>$1,454.2</td></tr><tr><td>24.9%</td><td>24.9%</td><td>25.0%</td><td>24.9%</td><td>24.9%</td></tr><tr><td>$61.3</td><td>$64.7</td><td>$62.2</td><td>$65.4</td><td>$253.5</td></tr><tr><td>108.2%</td><td>95.0%</td><td>95.0%</td><td>95.0%</td><td>97.9%</td></tr><tr><td>$392.9</td><td>$417.8</td><td>$437.5</td><td>$459.5</td><td>$1,707.7</td></tr><tr><td>28.2%</td><td>28.1%</td><td>27.9%</td><td>27.8%</td><td>28.0%</td></tr><tr><td>$1,002.7</td><td>$1,065.0</td><td>$1,125.9</td><td>$1,191.7</td><td>$4,385.2</td></tr><tr><td>75.1%</td><td>75.1%</td><td>75.0%</td><td>75.1%</td><td>75.1%</td></tr><tr><td>($4.6)</td><td>$3.4</td><td>$3.3</td><td>$3.4</td><td>$5.5</td></tr><tr><td>(8.2%)</td><td>5.0%</td><td>5.0%</td><td>5.0%</td><td>2.1%</td></tr><tr><td>$998.051</td><td>$1,068.4</td><td>$1,129.1</td><td>$1,195.1</td><td>$4,390.7</td></tr><tr><td>71.8%</td><td>71.9%</td><td>72.1%</td><td>72.2%</td><td>72.0%</td></tr><tr><td>32.7%</td><td>27.9%</td><td>28.3%</td><td>29.8%</td><td>29.6%</td></tr><tr><td>$284.3</td><td>$325.5</td><td>$336.8</td><td>$355.8</td><td>$1,302.4</td></tr><tr><td>19.1%</td><td>31.7%</td><td>32.3%</td><td>35.2%</td><td>29.8%</td></tr><tr><td>8.0%</td><td>14.5%</td><td>3.5%</td><td>5.6%</td><td></td></tr><tr><td>20.4%</td><td>21.9%</td><td>21.5%</td><td>21.5%</td><td>21.4%</td></tr><tr><td>$471.8</td><td>$475.6</td><td>$485.6</td><td>$496.4</td><td>$1,929.5</td></tr><tr><td>31.8%</td><td>21.3%</td><td>13.1%</td><td>10.8%</td><td>18.6%</td></tr><tr><td>5.3%</td><td>0.8%</td><td>2.1%</td><td>2.2%</td><td></td></tr><tr><td>33.9%</td><td>32.0%</td><td>31.0%</td><td>30.0%</td><td>31.6%</td></tr><tr><td>$76.1</td><td>$81.7</td><td>$86.2</td><td>$91.0</td><td>$335.0</td></tr><tr><td>19.4%</td><td>19.3%</td><td>32.8%</td><td>29.3%</td><td>25.2%</td></tr><tr><td>8.2%</td><td>7.4%</td><td>5.4%</td><td>5.6%</td><td></td></tr><tr><td>5.5%</td><td>5.5%</td><td>5.5%</td><td>5.5%</td><td>5.5%</td></tr><tr><td>$832.3</td><td>$882.8</td><td>$908.6</td><td>$943.2</td><td>$3,566.9</td></tr><tr><td>26.0%</td><td>24.7%</td><td>21.3%</td><td>20.7%</td><td>23.0%</td></tr><tr><td>$165.8</td><td>$185.6</td><td>$220.5</td><td>$252.0</td><td>$823.8</td></tr><tr><td>80.8%</td><td>45.5%</td><td>67.9%</td><td>81.0%</td><td>68.2%</td></tr><tr><td>11.9%</td><td>12.5%</td><td>14.1%</td><td>15.2%</td><td>13.5%</td></tr><tr

[中间内容因长度限制已省略]

ular investment objectives, portfolio holdings, strategy, financial situation, or needs of any recipient. As such, any advice or recommendation in this report may not be suitable for a particular recipient. JEF assumes recipients of this report are capable of evaluating the information contained herein and of exercising independent judgment. A recipient of this report should not make any investment decision without first considering whether any advice or recommendation in this report is suitable for the recipient based on the recipient's particular circumstances and, if appropriate or otherwise needed, seeking professional advice, including tax advice. JEF does not perform any suitability or other analysis to check whether an investment decision made by the recipient based on this report is consistent with a recipient's investment objectives, portfolio holdings, strategy, financial situation, or needs.

By providing this report, neither JRS nor any other JEF entity accepts any authority, discretion, or control over the management of the recipient's assets. Any action taken by the recipient of this report, based on the information in the report, is at the recipient's sole judgment and risk. The recipient must perform his or her own independent review of any prospective investment. If the recipient uses the services of JEF LLC (or other affiliated broker-dealers), in connection with a purchase or sale of a security that is a subject of these materials, such broker-dealer may act as principal for its own accounts or as agent for another person. Only JRS is registered with the SEC as an investment adviser; and therefore neither JEF LLC nor any other JEF affiliate has any fiduciary duty in connection with distribution of these reports.

The price and value of the investments referred to herein and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

This report may contain forward looking statements that may be affected by inaccurate assumptions or by known or unknown risks, uncertainties, and other important factors. As a result, the actual results, events, performance or achievements of the financial product may be materially different from those expressed or implied in such statements.

This report has been prepared independently of any issuer of securities mentioned herein and not as agent of any issuer of securities. No Equity Research personnel have authority whatsoever to make any representations or warranty on behalf of the issuer(s). Any comments or statements made herein are those of the JEF entity producing this report and may differ from the views of other JEF entities.

This report may contain information obtained from third parties, including ratings from credit ratings agencies such as Standard & Poor's, and information derived from third-party or proprietary generative artificial intelligence (Gen AI) models. JEF does not guarantee the accuracy, completeness, timeliness or availability of this information, and is not responsible for any errors or omissions (negligent or otherwise), regardless of the cause, or for the results obtained from the use of such content. Neither JEF nor any third-party content providers, including providers of Gen AI models, give any express or implied warranties, including, but not limited to, any warranties of merchantability or fitness for a particular purpose or use. Neither JEF nor any third-party content provider shall be liable for any direct, indirect, incidental, exemplary, compensatory, punitive, special or consequential damages, costs, expenses, legal fees, or losses (including lost income or profits and opportunity costs) in connection with any use of their content, including ratings. Credit ratings are statements of opinions and are not statements of fact or recommendations to purchase, hold or sell securities. They do not address the suitability of securities or the suitability of securities for investment purposes, and should not be relied on as investment advice. Reproduction and distribution of third party content in any form is prohibited except with the prior written permission of the related third party.

JEF reports are disseminated and available electronically, and, in some cases, also in printed form. Electronic research is simultaneously made available to all clients. This report or any portion hereof may not be copied, reprinted, sold, or redistributed or disclosed by the recipient or any third party, by content scraping or extraction, automated processing, or any other form or means, without the prior written consent of JEF. Any unauthorized use is prohibited. Neither JEF nor any of its respective directors, officers or employees, is responsible for guaranteeing the financial success of any investment, or accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this report or its contents. Nothing herein shall be construed to waive any liability JEF has under applicable U.S. federal or state securities laws.

For Important Disclosure information relating to JRS, please see https://adviserinfo.sec.gov/IAPD/Content/Common/crd\_iapd\_Brochure.aspx?BRCHR\_VRSN\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://avatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.

© 2026 JEF
"""
