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
# Company UnitedHealth Group

Rating
Hold

North America
United States

Reuters
UNH.N

Bloomberg
UNH US

Health Care
Managed Care

# No Good Deed: UNH Delivers Robust Outlook, Shares Fade

Strong Beat & Raise; 2026 Becomes Higher Baseline: UNH delivered an everything-investors-wanted quarter with a strong beat and raise, effectively squashing near-term concerns around MA MLR and the quality of the recovery. 2026 adjusted EPS guidance was raised by \~\$1.50 at the midpoint to \$19.50 to \$20.00, mostly reflecting the \~\$1.49 beat in the quarter and ahead of the \$18.49 consensus. The company also lowered and narrowed the full-year MLR guidance by \~70bps at the midpoint to 88.1% +/- 25bps. We suspect the raise could still prove conservative considering the potential for further improvements across the model: operating expenses remain elevated due to investments in people, communities and AI; provider cost pressure in Commercial remains high; OptumHealth is recovering faster than expected; Optum Insight is beginning to show AI-driven operating and product momentum; and stronger cash flow increases capital deployment flexibility. Management framed the \$19.50 to \$20.00 EPS range as the right baseline for 2027 growth, even though it includes prior period development, and reiterated confidence in the 13%-16% long-term EPS growth algorithm. Despite this better-than-expected print, the shares faded from opening \~+9% to end the session up only 1%, as the entire MCO space sold off despite the MCO leader's robust outlook.

Solid Q2 Beat With Broad-based Strength: UNH reported Q2 total revenue of \$112.0B, coming in above our \$110.0B estimate and the Street's \$110.6B, while adjusted EPS of \$6.38 was also well above our \$4.73 estimate and consensus of \$4.89. Consolidated MLR of 86.7% beat the consensus estimate by 170 bps, helped by \$860mm of net favorable prior period medical development, the majority of which was in-year development. Importantly, days claims payable increased to 47 days, up \~2.5 days year over year, which should provide comfort on reserving quality despite the favorable development. Management noted Medicare trend remains elevated versus historical levels but is running below its initial \~10% expectation, driven by benefit design, care management, network curation, product positioning, favorable claims experience, lighter respiratory season and weather patterns. MA membership retention is now expected to be better than prior expectations, with enrollment expected to decline by \~1.1mm lives for the year and Medicare margins expected to finish above 3%. Medicaid was broadly in line with expectations, with 2026 margins still expected within the prior negative 1.0% to negative 1.7% range. Annualized 2026 rate impacts are expected around 6%-7% but still lag elevated medical trend. Optum delivered strong results in Q2, with OptumHealth the standout as stronger care

Date
17 July 2026

Rating    Hold
Price target (USD)    467.00
Price at 16 Jul 26    15.51
52-week range    431.68 – 15.51

Valuation & Risks

George Hill
Research Analyst
+1-212-2507822

Maxi Ma, CFA
Research Associate
+1-901-338-2175

Liz Li
Research Associate
+1-617-251-2782

Graham Harris
Research Associate
+1-929-701-6999

Key changes

Price target (USD) 370 467 26%

Source: DB

management, operating discipline and payer alignment support a more visible margin recovery path from a little above 2% in 2026 toward \~4% in 2027 and the 6% aspirational level in 2028. Optum Rx remains steady with no major investment required for the new transparency model, while Optum Insight's Q2 upside benefited from payment integrity timing pull-forward, though the longer-term AI/product opportunity remains intact.

Commercial Is The Main Nit, But Also A Future Recovery Lever: The main offset was Commercial, where management said cost trend remains stubbornly high and modestly above the prior \~11% expectation. The drivers include pressure from the No Surprises Act independent dispute resolution process, higher provider coding intensity, higher service intensity and pharmacy cost pressure, including specialty drugs, anti-inflammatory drugs and GLP-1s. Management now expects Commercial margin recovery to take longer than previously anticipated, with full recovery extending past 2027, but characterized this as a delay rather than a setback. We view this as one of the important future upside levers: the current Commercial run-rate clearly pressures margins, but it also leaves room for recovery from pricing, administrative cost efficiency, AI-enhanced fraud/waste/abuse efforts and tighter medical cost management over time.

Adjusting Estimates: We are raising our 2026 revenue estimate from \$447.2B to \$448.9B, above the Street's \$444.0B. Our adjusted EPS estimate is increased from \$18.45 to \$19.94 reflecting the Q2 beat as well as expectations for stable trend in MA and Medicaid. This positions us close to the high end of the guidance range and above the \$18.49 consensus – which we suspect will move closer to \$20. We continue to see sources for upside to 2026 EPS including conservative MLR guidance, discretionary spend, capital deployment, and the potential for State rate improvements. UNH increased its guidance for CFO from \$18B to \$24B and doubled its share repo target to \$5B+.

Maintain Hold: We maintain our Hold rating on UNH's shares and raise our price target from \$370 to \$467 now representing 20x our 2027 EPS estimate. With two quarters of 2026 in the books, we are rolling forward to 2027 numbers for valuation purposes. Our target multiple reflects a comprehensive path towards margin expansion in 2026 and 2027 following the transition year that was 2025. Downside risks include worsening cost trends, inability to achieve prudent pricing and plan exits, healthcare regulatory changes at the federal and state levels, managed-care pricing competition, any impact from the reported DOJ investigation, and drug-pricing/PBM reform, which appear to be diminishing. Upside risks include better-than-expected execution of the margin recovery story and significant EPS outperformance versus our estimates and consensus. UNH delivered that outperformance today, which appeared to already be priced into the shares.

Figure 1: UNH Q Comp

<table><tr><td colspan="11">UnitedHealth GroupQ2-26 Results</td></tr><tr><td rowspan="2"></td><td colspan="3">FY-26</td><td colspan="3">Q2-26</td><td colspan="4">Growth</td></tr><tr><td>Initial Outlook</td><td>Q1 Guide</td><td>Q2 Guide</td><td>Consensus</td><td>DB</td><td>Actual</td><td>Q2-25</td><td>Consensus</td><td>DB</td><td>Actual</td></tr><tr><td>Total Revenue</td><td>&gt;$439,000</td><td></td><td></td><td>$ 110,667</td><td>$ 110,034</td><td>$ 112,032</td><td>$ 111,616</td><td>-0.9%</td><td>-1.4%</td><td>0.4%</td></tr><tr><td>Total Operating Expenses</td><td></td><td></td><td></td><td>104,177</td><td>102,627</td><td>104,041</td><td>106,466</td><td></td><td></td><td></td></tr><tr><td>EBITDA</td><td></td><td></td><td></td><td>7,377</td><td>7,407</td><td>9,031</td><td>6,234</td><td>18.3%</td><td>18.8%</td><td>44.9%</td></tr><tr><td>Depreciation and Amortization</td><td>-4,400</td><td></td><td></td><td>979</td><td>1,039</td><td>1,040</td><td>1,084</td><td></td><td>OP Margin</td><td></td></tr><tr><td>Operating Income</td><td>&gt;24,000</td><td></td><td>&gt;25,450</td><td>6,525</td><td>6,103</td><td>7,991</td><td>5,150</td><td>5.90%</td><td>5.55%</td><td>7.13%</td></tr><tr><td>Interest Expense</td><td>-3,700</td><td></td><td></td><td>927</td><td>916</td><td>962</td><td>1,027</td><td></td><td></td><td></td></tr><tr><td>Pre-Tax Income</td><td></td><td></td><td></td><td>5,412</td><td>5,380</td><td>6,968</td><td>4,082</td><td>32.6%</td><td>31.8%</td><td>70.7%</td></tr><tr><td>Income Taxes</td><td></td><td></td><td></td><td>1,063</td><td>1,130</td><td>1,298</td><td>510</td><td></td><td></td><td></td></tr><tr><td>Tax Rate</td><td>-19.25%</td><td></td><td>-18.5%</td><td>19.6%</td><td>20.7%</td><td>18.5%</td><td>12.4%</td><td></td><td></td><td></td></tr><tr><td>Net Income</td><td>&gt;15,600</td><td></td><td>&gt;16,750</td><td>4,236</td><td>4,250</td><td>5,670</td><td>3,572</td><td>18.6%</td><td>19.0%</td><td>58.7%</td></tr><tr><td>Noncontrolling interests</td><td></td><td></td><td></td><td>183</td><td>(201)</td><td>(186)</td><td>(166)</td><td></td><td></td><td></td></tr><tr><td>Adjusted Net Income</td><td></td><td></td><td></td><td>4,439</td><td>4,314</td><td>5,792</td><td>3,716</td><td>19.4%</td><td>16.1%</td><td>55.9%</td></tr><tr><td>Adjusted EPS</td><td>&gt;$17.75</td><td>&gt;$18.25</td><td>$19.50-$20.00</td><td>$4.89</td><td>$4.73</td><td>$6.38</td><td>$4.08</td><td>19.7%</td><td>15.8%</td><td>56.3%</td></tr><tr><td>Diluted Share Count</td><td>910-915</td><td></td><td></td><td>908</td><td>912</td><td>906</td><td>910</td><td></td><td></td><td></td></tr><tr><td colspan="11">UnitedHealthcare</td></tr><tr><td>Revenue</td><td>&gt;335,000</td><td></td><td></td><td>84,911</td><td>82,616</td><td>86,017</td><td>86,103</td><td>-1.4%</td><td>-4.0%</td><td>-0.1%</td></tr><tr><td>Adj. Operating Profit</td><td>&gt;10,800</td><td></td><td>&gt;12,000</td><td>3,104</td><td>3,387</td><td>3,942</td><td>2,075</td><td>49.6%</td><td>63.2%</td><td>90.0%</td></tr><tr><td>OP margin</td><td>-3.2%</td><td></td><td></td><td>3.7%</td><td>4.1%</td><td>4.6%</td><td>2.4%</td><td></td><td></td><td></td></tr><tr><td>MLR</td><td>88.3%-89.3%</td><td></td><td>87.85%-88.35%</td><td>88.4%</td><td>88.5%</td><td>86.7%</td><td>89.4%</td><td></td><td></td><td></td></tr><tr><td>Eliminations</td><td></td><td></td><td></td><td></td><td>-</td><td>-</td><td>-</td><td></td><td></td><td></td></tr><tr><td colspan="11">Optum</td></tr><tr><td>OptumHealth</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Revenue</td><td>&gt;91,000</td><td></td><td></td><td>23,218</td><td>22,407</td><td>23,472</td><td>24,725</td><td>-6.1%</td><td>-9.4%</td><td>-5.1%</td></tr><tr><td>Adj. Operating Profit</td><td>&gt;2,200 (GAAP)</td><td></td><td>&gt;2,215</td><td>481</td><td>479</td><td>1,174</td><td>636</td><td>-24.3%</td><td>-24.6%</td><td>84.6%</td></tr><tr><td>OP margin</td><td>-2.4%</td><td></td><td></td><td>2.1%</td><td>3.32%</td><td>5.00%</td><td>2.6%</td><td></td><td></td><td></td></tr><tr><td colspan="11">OptumInsight</td></tr><tr><td>Revenue</td><td>&gt;21,000</td><td></td><td></td><td>5,292</td><td>5,227</td><td>5,402</td><td>5,232</td><td>1.1%</td><td>-0.1%</td><td>3.2%</td></tr><tr><td>Adj. Operating Profit</td><td>&gt;4,750 (GAAP)</td><td></td><td>&gt;4,750</td><td>1,169</td><td>943</td><td>1,373</td><td>998</td><td>17.1%</td><td>-5.6%</td><td>37.6%</td></tr><tr><td>OP margin</td><td>-22.6%</td><td></td><td></td><td>22.1%</td><td>18.0%</td><td>25.4%</td><td>19.1%</td><td></td><td></td><td></td></tr><tr><td colspan="11">OptumRx</td></tr><tr><td>Revenue</td><td>&gt;150,500</td><td></td><td></td><td>37,646</td><td>40,524</td><td>38,292</td><td>38,459</td><td>-2.1%</td><td>5.4%</td><td>-0.4%</td></tr><tr><td>Adj. Operating Profit</td><td>&gt;6,250</td><td></td><td>&gt;6,250</td><td>1,501</td><td>1,559</td><td>1,490</td><td>1,441</td><td>4.2%</td><td>8.2%</td><td>3.4%</td></tr><tr><td>OP margin</td><td>-4.2%</td><td></td><td></td><td>4.0%</td><td>3.85%</td><td>3.89%</td><td>3.7%</td><td></td><td></td><td></td></tr><tr><td>Optum Eliminations</td><td>-(5,000)</td><td></td><td></td><td>(1,204)</td><td>(1,071)</td><td>(1,503)</td><td>(1,191)</td><td>1.1%</td><td>-10.1%</td><td>26.2%</td></tr><tr><td>OptumRx Quarterly Adj Scripts (mlns)</td><td></td><td></td><td></td><td>-</td><td>-</td><td>387</td><td>414</td><td></td><td></td><td>-6.5%</td></tr><tr><td colspan="11">UnitedHealth Membership Data</td></tr><tr><td>Commercial Risk-Based</td><td>6,765-6,865</td><td></td><td></td><td>7,344</td><td>7,730</td><td>7,655</td><td>8,440</td><td>-13.0%</td><td>-8.4%</td><td>-9.3%</td></tr><tr><td>Commercial Fee-Based</td><td>22,035-22,235</td><td></td><td></td><td>22,275</td><td>22,278</td><td>22,265</td><td>21,530</td><td>3.5%</td><td>3.5%</td><td>3.4%</td></tr><tr><td>Total Commercial Enrollment</td><td>28,800-29,100</td><td></td><td></td><td>29,619</td><td>30,008</td><td>29,920</td><td>29,970</td><td>-1.2%</td><td>0.1%</td><td>-0.2%</td></tr><tr><td>Medicare Advantage</td><td>7,245-7,295</td><td></td><td></td><td>7,444</td><td>7,265</td><td>7,565</td><td>8,350</td><td>-10.9%</td><td>-13.0%</td><td>-9.4%</td></tr><tr><td>Medicare Supplement</td><td>4,235-4,285</td><td></td><td></td><td>4,266</td><td>4,265</td><td>4,260</td><td>4,305</td><td>61.6%</td><td>-0.9%</td><td>-1.0%</td></tr><tr><td>Stand-Alone PDP</td><td>2,570-2,670</td><td></td><td></td><td>2,697</td><td>2,706</td><td>2,710</td><td>2,800</td><td>-3.7%</td><td>-3.4%</td><td>-3.2%</td></tr><tr><td>Total Medicare &amp; Retirement</td><td>14,050-14,250</td><td></td><td></td><td>14,407</td><td>14,236</td><td>14,535</td><td>15,455</td><td>-6.8%</td><td>-7.9%</td><td>-6.0%</td></tr><tr><td>Medicaid</td><td>6,665-6,815</td><td></td><td></td><td>6,958</td><td>7,170</td><td>6,780</td><td>7,490</td><td>-7.1%</td><td>-4.3%</td><td>-9.5%</td></tr><tr><td>International</td><td></td><td></td><td></td><td>1,053</td><td>1,049</td><td>1,145</td><td>1,165</td><td>-9.6%</td><td>-10.0%</td><td>-1.7%</td></tr></table>

Source: Company Reports, DB, Bloomberg Finance LP

## Appendix 1

## Important Disclosures

<table><tr><td>Company</td><td>Ticker</td><td>Recent price</td><td>Disclosure</td></tr><tr><td>UnitedHealth Group</td><td>UNH.N</td><td>15.51 (USD) 16 Jul 26</td><td>7, 8, 14, 15, 21, 24, 26</td></tr></table>

Prices are current as of the end of the previous trading session unless otherwise indicated and are sourced from local exchanges via Reuters, Bloomberg and other vendors. Other information is sourced from DB, subject companies, and other sources.

## Important Disclosures Required by U.S. Regulators

7 - DB and/or its affiliate(s) has received compensation from this company for the provision of investment banking or financial advisory services within the past year.

8 - DB and/or its affiliate(s) expects to receive, or intends to seek, compensation for investment banking services from this company in the next three months.

14 - DB and/or its affiliate(s) has received compensation from this company within the past year for non-investment banking related services.

15 - This company has been a client of DB Securities Inc. within the past year during which time it received investment banking services.

21 - This company has been a client of DB Securities Inc. within the past year, during which time it received non-investment banking securities-related services.

## Important Disclosures Required by Non-U.S. Regulators

24 - DB and/or its affiliate(s) is or has been over the previous 12 months party to an agreement with the company relating to the provision of services set out in Sections A and B of Annex I of Directive 2014/65/EU, or has over the previous 12 months been obliged or entitled (as applicable) to pay or receive compensation relating to the provision of services set out in Sections A and B of Annex I of Directive 2014/65/EU.

26 - Within the preceding 12 months, DB and/or its affiliate(s) has received compensation for the provision of investment banking services or is currently providing or has provided investment banking services to this company.

For disclosures pertaining to recommendations or estimates made on securities other than the primary subject of this research, please see the most recently published company report or visit our global disclosure look-up page on our website at https://research.db.com/Research/Disclosures/EquityResearchDisclosures. Aside from within this report, important risk and confli

[中间内容因长度限制已省略]

ble upon request. This report may not be reproduced, distributed or published without DB's prior written consent.

Backtested, hypothetical or simulated performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG.

It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG

David Folkerts-Landau
Group Chief Economist and Global Head of Research

<table><tr><td>Pam FinelliCOO and Head of Fixed Income Research</td><td>Steve PollardGlobal Head of Company Research and Sales</td><td>Jim ReidGlobal Head of Macro and Thematic Research</td><td>Tim RokossaHead of European Company Research</td></tr><tr><td>Matthew BarnardHead of AmericasCompany Research</td><td>Debbie JonesGlobal Head of Sustainability and Data Innovation, Research</td><td>Robin WinklerHead of German Macro Research</td><td>Sameer GoelGlobal Head of EM &amp; APAC Research</td></tr><tr><td>Francis YaredGlobal Head of Rates Research</td><td>George SaravelosGlobal Head of FX Research</td><td>Peter HooperVice-Chair of Research</td><td>Nilendra de-MelHead of APAC &amp; Middle East Product Development</td></tr></table>

International Production Locations

<table><tr><td>DB AG</td><td>DB AG</td><td>DB AG</td><td>Deutsche Securities Inc.</td></tr><tr><td>DB Place</td><td>Equity Research</td><td>Filiale Hongkong</td><td>1-3-1 Azabudai</td></tr><tr><td>Level 16</td><td>Mainzer Landstrasse 11-17</td><td>International Commerce Centre</td><td>Azabudai Hills Mori JP Tower</td></tr><tr><td>Corner of Hunter &amp; Phillip Streets</td><td>60329 Frankfurt am Main Germany</td><td>1 Austin Road West, Kowloon,</td><td>Minato-ku, Tokyo 106-0041</td></tr><tr><td>Sydney, NSW 2000 Australia</td><td>Tel: (49) 69 910 00</td><td>Hong Kong</td><td>Japan</td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td>Tel: (852) 2203 8888</td><td>Tel: (81) 3 6730 1000</td></tr></table>

DB AG
21 Moorfields
London EC2Y 9DB
United Kingdom
Tel: (44) 20 7545 8000

DB Securities Inc.

The DB Center
1 Columbus Circle
New York, NY 10019
Tel: (1) 212 250 2500

DB AG
Filiale Singapur
One Raffles Quay, South Tower
Singapore 048583
Tel: (65) 6423 8001
"""
