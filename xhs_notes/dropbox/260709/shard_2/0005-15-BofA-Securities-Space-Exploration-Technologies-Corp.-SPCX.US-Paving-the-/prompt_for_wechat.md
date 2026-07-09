你是麦肯锡/研究导读风格的微信公众号文章主笔，擅长用金字塔原理把报告内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给专业读者/产业决策者的报告导读。
- 长度：约 1200 字，整体以短导读为主，通常控制在 900-1200 个中文字符。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，只讲最关键的判断、图表和未解问题，让读者有动力去看原文。
- 文章必须像人工编辑润色过的报告导读：句长有变化，段落有呼吸感，不要整齐排比，不要反复使用“这意味着/真正重要的是/换句话说/从这个角度看”等模板转折。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、市场定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须短、锐利、可转发，优先 20-35 个中文字符，最长不超过 35 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 要兼顾微信搜一搜：尽量包含一个高意图关键词，例如行业/公司/政策/AI/房地产/半导体/光伏/消费/美联储/利率/通胀/机器人/比特币等。
- `# 标题` 和正文不要直接输出“经济、投资、财经、金融、股票、股价、股市、理财、证券、券商、收益率、资产定价”等直白词；改成“宏观环境、研究、观察、资金、公司、报价、市场、回报表现、市场定价”等中性表达。
- 涉及中国、国内、内地、大陆、人民币、A股、港股时，必须使用中性客观表达；不要写“不好、不行、疲弱、低迷、恶化、危机、衰退、崩盘、放缓、压力、拖累、唱衰”等负面判断。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`BofA`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题禁止出现 GS、JPM、JEF、NOM、BARC、MS、DB、Citi、Ticker、文件编号；如果原文只有英文机构名，请翻译为中文机构名。
- 标题冒号后不要重复机构或来源类型，禁止“联合国贸发会议：联合国贸发报告，……”“麦肯锡：麦肯锡报告称，……”这类写法；冒号后直接写判断或变量。
- 标题只能保留一层信息，不要把多个长分句全部塞进标题；如果原始标题有三段以上信息，只取最有传播性的主判断，其余放在正文第一段自然展开。
- 如果报告是单一公司/个股报告，标题和正文只能写公司情况、行业变化、业务进展、竞争格局和报告里的事实；禁止出现目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO 等任何卖方操作口径。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 观察提示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，20-35 个中文字符。
2. 开头 2-3 段：直接给出主判断、为什么现在重要、报告提供了什么新信号；自然带出 4-6 个长尾关键词，覆盖国家/行业/公司/政策/数据/技术词，但不要写成关键词堆砌。
3. 3-4 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 1-2 个 `> **KC评论：** ...` 引用块，每个 1-2 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，不要夹带任何推广话术。
5. 正文中间禁止插入 CTA、广告、扫码、社群、知识星球、每日汇编、喂给 AI 等表达；中间只允许出现分析正文、图表占位和 `KC评论`。
6. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
7. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
8. 不要写任何 CTA、广告、扫码、社群、知识星球、网站、域名或关注引导；系统会在最结尾统一插入固定信息。
9. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
10. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.</p>`

【CTA 要求】
- 不要输出任何 CTA。不要写“加入社群”“扫码”“星球”“完整报告领取”“网站”“域名”“关注”“星标”“更多查看”等表达。
- 文末也不要写 CTA；系统会在最结尾统一插入固定信息。
- 正文中间不要出现“如果你从某些关键词搜到这里”“单篇文章只能解决一个切片”“我每天会把……”“这篇可以沿着……”这类表达。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。
- `KC评论` 里禁止夹带 CTA，不要写扫码、社群、知识星球、每日汇编、喂给 AI、市场主线、完整报告领取等表达；它只能做解释、提醒或追问。

【人工编辑感要求】
- 段落不要像 AI 摘要清单。每段只推进一个意思，必要时用短句收住。
- 不要展开成完整长文。每个小节只保留最有信息量的一段，细节留给原文和图表。
- 避免连续使用同一种句式开头，避免连续三段都是“报告指出/这意味着/真正重要的是”。
- 不要机械重复标题、机构名或同一句判断。标题已经写过的内容，正文第一段要换一种说法展开。
- 保留一点自然语气，但不要口水化；像一个认真读过报告的人在做导读。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 单公司报告不能写成交易提示；不要输出目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO，也不要保留这些英文/中文卖方评级词。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份BofA研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Space Exploration Technologies Corp.

# Paving the superhighway to the stars; Initiate at Buy, PO of \$235

Initiating Coverage: BUY | PO: 235.00 USD | Price: 162.00 USD

## Launch leadership enables everything else

We initiate coverage of SpaceX (SPCX) with a Buy rating and \$235 PO, derived by a long-term DCF considering base, bear, and bull cases (see inside). SpaceX has evolved from a launch company into the foundational enabler of the space economy and the leading provider of space-based applications as a result. SpaceX's extensive moats on reusable launch and proliferated space applications are in our view laying the foundation for Starship and future applications to drive another paradigm shift in capabilities.

## Monetizing the mass to orbit moat

SpaceX has demonstrated a unique ability to convert launch and manufacturing capabilities into market-leading, recurring applications businesses, notably Starlink. The result is a powerful flywheel, where launch enables space applications, applications generate cash flow, and those cash flows support further infrastructure investment. While not reflected directly in financials given company accounting, Falcon and Starship launch economics are the primary drivers of SpaceX's ability to develop high-margin application layers on orbit.

## It all hinges on the “King of the Cosmos”

The central debate is whether Starship can achieve the reliability, cadence, and economics required to unlock the next phase of growth. Much of SpaceX's long-term opportunity, including Starlink v3 deployment and future compute infrastructure, depend on Starship successfully commercializing full reusability. If achieved, we believe launch costs could decline by an order of magnitude while capacity expands dramatically. If delayed, the timing of many future growth vectors moves materially to the right.

## Orbital compute demonstrates differentiated option value

SpaceX's vision for orbital compute creates substantial upside potential, but is also indicative of broader option value realizable by SpaceX's launch moat, vertical integration, and manufacturing scale. Entry into AI infrastructure and applications markets represent attractive opportunities for SpaceX to apply its leading space positioning within rapidly growing and competitive markets. Other emerging and potential space applications could provide additional value in time, again predicated on the ultimate success of Starship as a means of further expanding space access.

<table><tr><td>Estimates (Dec) (US$)</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>EPS</td><td>0.08</td><td>(1.69)</td><td>(0.02)</td><td>1.37</td><td>3.78</td></tr><tr><td>EPS Change (YoY)</td><td>NA</td><td>NM</td><td>98.8%</td><td>NM</td><td>175.9%</td></tr><tr><td>Consensus EPS (Bloomberg)</td><td></td><td></td><td>(0.99)</td><td>(0.04)</td><td>0.50</td></tr><tr><td>Consensus EPS (Visible Alpha)</td><td></td><td></td><td>(0.51)</td><td>0.15</td><td>0.72</td></tr><tr><td colspan="6">Valuation (Dec)</td></tr><tr><td>P/E</td><td>2,025.0x</td><td>NM</td><td>NM</td><td>118.2x</td><td>42.9x</td></tr><tr><td>EV / EBITDA*</td><td>217.1x</td><td>176.4x</td><td>59.5x</td><td>24.1x</td><td>11.9x</td></tr><tr><td>Free Cash Flow Yield*</td><td>-0.4%</td><td>-1.1%</td><td>-2.7%</td><td>-5.5%</td><td>-6.5%</td></tr><tr><td colspan="6">* For full definitions of  $IQmethod^{SM}$  measures, see page 38.</td></tr></table>

BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.
Refer to important disclosures on page 39 to 41. Analyst Certification on page 37. Price Objective Basis/Risk on page 37.
12991046

## 07 July 2026

Equity

Ronald J. Epstein
Research Analyst
BofAS
+1 646 855 5695
r.epstein@bofa.com

Justin Post
Research Analyst
BofAS
justin.post@bofa.com

Tal Liani
Research Analyst
BofAS
tal.liani@bofa.com

Michael J. Funk
Research Analyst
BofAS
michael.j.funk@bofa.com

## Mariana Perez Mora

Research Analyst
BofAS
+1 646 855 5696
mariana.perezmora@bofa.com

## Alexander Preston

Research Analyst
BofAS
+1 646 855 3599
alexander.preston@bofa.com

## Kevin Niederpruem

Research Analyst
BofAS
kevin.niederpruem@bofa.com

## Stock Data

<table><tr><td>Price</td><td>162.00 USD</td></tr><tr><td>Price Objective</td><td>235.00 USD</td></tr><tr><td>Date Established</td><td>7-Jul-2026</td></tr><tr><td>Investment Opinion</td><td>C-1-9</td></tr><tr><td>52-Week Range</td><td>147.11 USD - 225.64 USD</td></tr><tr><td>Mrkt Val (mn) / Shares Out (mn)</td><td>1,209,092 USD / 7,463.5</td></tr><tr><td>Free Float</td><td>8.6%</td></tr><tr><td>Average Daily Value (mn)</td><td>NA</td></tr><tr><td>BofA Ticker / Exchange</td><td>SPCX / NAS</td></tr><tr><td>Bloomberg / Reuters</td><td>SPCX US / SPCX.OQ</td></tr><tr><td>ROE (2026E)</td><td>-0.2%</td></tr><tr><td>Net Dbt to Eqty (Dec-2025A)</td><td>-7.5%</td></tr></table>

<table><tr><td colspan="2">Stock Data</td></tr><tr><td>Average Daily Volume</td><td>NA</td></tr></table>

## iQprofile $^{SM}$ Space Exploration Technologies Corp.

iQmethod $^{SM}$ – Bus Performance\*

<table><tr><td>(US$ Millions)</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Return on Capital Employed</td><td>NA</td><td>-4.4%</td><td>2.5%</td><td>8.2%</td><td>14.3%</td></tr><tr><td>Return on Equity</td><td>6.2%</td><td>-14.7%</td><td>-0.2%</td><td>12.3%</td><td>26.9%</td></tr><tr><td>Operating Margin</td><td>3.3%</td><td>-13.9%</td><td>8.5%</td><td>26.0%</td><td>37.5%</td></tr><tr><td>Free Cash Flow</td><td>(5,387)</td><td>(13,834)</td><td>(32,394)</td><td>(66,908)</td><td>(78,745)</td></tr></table>

## iQmethod $^{SM}$ – Quality of Earnings\*

<table><tr><td>(US$ Millions)</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Cash Realization Ratio</td><td>7.3x</td><td>NM</td><td>NM</td><td>2.5x</td><td>1.8x</td></tr><tr><td>Asset Replacement Ratio</td><td>2.9x</td><td>3.1x</td><td>3.7x</td><td>4.6x</td><td>4.4x</td></tr><tr><td>Tax Rate</td><td>NM</td><td>NM</td><td>NM</td><td>5.0%</td><td>5.0%</td></tr><tr><td>Net Debt-to-Equity Ratio</td><td>3.4%</td><td>-7.5%</td><td>-35.8%</td><td>12.2%</td><td>46.4%</td></tr><tr><td>Interest Cover</td><td>0.4x</td><td>-1.8x</td><td>2.2x</td><td>6.2x</td><td>8.1x</td></tr></table>

Income Statement Data (Dec)

<table><tr><td>(US$ Millions)</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Sales</td><td>14,015</td><td>18,674</td><td>40,770</td><td>78,207</td><td>142,785</td></tr><tr><td>% Change</td><td>NA</td><td>33.2%</td><td>118.3%</td><td>91.8%</td><td>82.6%</td></tr><tr><td>Gross Profit</td><td>6,019</td><td>9,223</td><td>25,430</td><td>52,764</td><td>98,130</td></tr><tr><td>% Change</td><td>NA</td><td>53.2%</td><td>175.7%</td><td>107.5%</td><td>86.0%</td></tr><tr><td>EBITDA</td><td>5,350</td><td>6,584</td><td>19,503</td><td>48,142</td><td>97,699</td></tr><tr><td>% Change</td><td>NA</td><td>23.1%</td><td>196.2%</td><td>146.8%</td><td>102.9%</td></tr><tr><td>Net Interest &amp; Other Income</td><td>(224)</td><td>(1,630)</td><td>(3,452)</td><td>(3,299)</td><td>(6,602)</td></tr><tr><td>Net Income (Adjusted)</td><td>796</td><td>(4,945)</td><td>(211)</td><td>17,862</td><td>49,284</td></tr><tr><td>% Change</td><td>NA</td><td>NM</td><td>95.7%</td><td>NM</td><td>175.9%</td></tr></table>

## Free Cash Flow Data (Dec)

<table><tr><td>(US$ Millions)</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Net Income from Cont Operations (GAAP)</td><td>791</td><td>(4,937)</td><td>(173)</td><td>16,170</td><td>44,621</td></tr><tr><td>Depreciation &amp; Amortization</td><td>3,824</td><td>6,701</td><td>13,037</td><td>23,861</td><td>38,257</td></tr><tr><td>Change in Working Capital</td><td>3,312</td><td>9,633</td><td>17,934</td><td>27,823</td><td>44,127</td></tr><tr><td>Deferred Taxation Charge</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>Other Adjustments, Net</td><td>(2,151)</td><td>(4,612)</td><td>(14,916)</td><td>(23,861)</td><td>(38,257)</td></tr><tr><td>Capital Expenditure</td><td>(11,163)</td><td>(20,619)</td><td>(48,276)</td><td>(110,900)</td><td>(167,493)</td></tr><tr><td>Free Cash Flow</td><td>-5,387</td><td>-13,834</td><td>-32,394</td><td>-66,908</td><td>-78,745</td></tr><tr><td>% Change</td><td>NA</td><td>-156.8%</td><td>-134.2%</td><td>-106.5%</td><td>-17.7%</td></tr><tr><td>Share / Issue Repurchase</td><td>12,061</td><td>17,514</td><td>89,634</td><td>0</td><td>0</td></tr><tr><td>Cost of Dividends Paid</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Change in Debt</td><td>(77)</td><td>9,131</td><td>28,250</td><td>50,000</td><td>100,000</td></tr></table>

## Balance Sheet Data (Dec)

<table><tr><td>(US$ Millions)</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Cash &amp; Equivalents</td><td>11,385</td><td>24,747</td><td>102,000</td><td>85,092</td><td>106,347</td></tr><tr><td>Trade Receivables</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>Other Current Assets</td><td>4,723</td><td>6,205</td><td>41,173</td><td>77,729</td><td>142,550</td></tr><tr><td>Property, Plant &amp; Equipment</td><td>21,147</td><td>42,602</td><td>82,647</td><td>169,687</td><td>298,923</td></tr><tr><td>Other Non-Current Assets</td><td>19,111</td><td>18,384</td><td>65,074</td><td>124,826</td><td>227,900</td></tr><tr><td>Total Assets</td><td>56,366</td><td>91,938</td><td>290,894</td><td>457,334</td><td>775,720</td></tr><tr><td>Short-Term Debt</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Other Current Liabilities</td><td>16,100</td><td>26,477</td><td>103,032</td><td>197,638</td><td>360,836</td></tr><tr><td>Long-Term Debt</td><td>12,262</td><td>21,659</td><td>54,138</td><td>104,138</td><td>204,138</td></tr><tr><td>Other Non-Current Liabilities</td><td>2,200</td><td>2,477</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Total Liabilities</td><td>30,562</td><td>50,613</td><td>157,170</td><td>301,776</td><td>564,974</td></tr><tr><td>Total Equity</td><td>25,804</td><td>41,325</td><td>133,724</td><td>155,558</td><td>210,746</td></tr><tr><td>Total Equity &amp; Liabilities</td><td>56,366</td><td>91,938</td><td>290,894</td><td>457,334</td><td>775,720</td></tr></table>

\* For full definitions of IQmethod $^{SM}$ measures, see page 38.

## Company Sector

Satellite Services

## Company Description

SpaceX is an integrated provider of launch and space systems, communications, and AI with a goal of making human life interplanetary. The company operates under three segments: Space, including launch of its Falcon, Dragon, and Starship vehicles, Connectivity, operating Starlink and Starshield and Mobile connectivity service, and AI, which includes development of data center compute, the company's Grok large language model, and other applications.

## Investment Rationale

SpaceX has evolved from a launch company into the foundational enabler of the space economy and the leading provider of space-based applications as a result. SpaceX's extensive moats on reusable launch and proliferated space applications are in our view laying the foundation for Starship and future applications to drive another paradigm shift in capabilities.

## Quarterly Earnings Estimates

<table><tr><td></td><td>2025</td><td>2026</td></tr><tr><td>Q1</td><td>-0.18A</td><td>-1.10A</td></tr><tr><td>Q2</td><td>-0.34A</td><td>-0.16E</td></tr><tr><td>Q3</td><td>-0.36A</td><td>0.21E</td></tr><tr><td>Q4</td><td>-0.79A</td><td>0.27E</td></tr></table>

## Investment thesis

We initiate coverage of SpaceX (SPCX) with a Buy rating and a PO of \$235. SpaceX is an integrated provider of launch and space systems, communications, and AI with a goal of making human life interplanetary. The company operates under three segments: Space, including launch of its Falcon family of vehicles, Dragon spacecraft, and Starship; Connectivity, operating Starlink and Starshield as well as Mobile connectivity service; and AI, which includes development of data center compute, the company's Grok large language model, and other applications.

Our PO of \$235 is based on an average long-term DCF of base, bull, and bear cases for different revenue and cash generation scenarios between now and 2045. Our DCF factors in an 18% discount rate in the base case, 28% discount rate in the bull case, and 14% discount rate in the bear case and assigns an equal weighting to each case. Our DCF factors in a long-term growth rate of 5% in the base, bull, and bear cases. In our view, the varied discount rates fairly reflect the relative uncertainty associated with each scenario, with base case discount rate in line with the median of the peer group, bull case discount rate in line with the higher growth and higher risk peers, and bear case discount rate in line with more established, lower execution risk peers.

## Upside risks to our PO

Upside risks to our PO are better-than-expected cost cutting and margin expansion, well-integrated M&A activity, market share gains among launch, satellite services, and/or AI applications, and better-than-expected commercialization of the Starship launch vehicle.

## Downside risks to our PO

Downside risks to our PO are production delays, inability to achieve M&A synergies, potential impact to capex / FCF from space systems and/or AI investments, regulatory risks to launch cadence and/or satellite service deployment, and setbacks to Starship and/or satellite program development.

## Investment positives

## (+) Strong moat on reusable launch underpins services businesses

We see SpaceX's launch business as the foundation of its competitive advantage and its most enduring moat against competitors in the space economy. The Falcon family of vehicles has established SpaceX as the global preeminent launch provider and space enabler, flying over 650 launches to date at $99\%+$ mission success and delivering $80\%+$ global mass to orbit in recent years. The combination of proven out reusable hardware (\~35 reflights by the most reused Falcon booster), vertical integration, and high launch cadence has enabled material reductions in launch cost to orbit while rapidly scaling activity in space and delivering reliability of orbital access.

While Falcon itself is years ahead of capabilities that can be deployed by competitors, Starship would represent a further paradigm shift for space access when it is successfully commercialized at scale. Full reusability of both booster and upper stage could deliver a further order-of-magnitude decrease in per-kg launch costs while enabling increased flight cadence. Starship's enhanced capabilities and cost effectiveness are integral to planned constellations including next-generation Starlink v3 and Mobile satellites and potential orbital compute platforms. Importantly, despite accounting of launch costs driving visibly low financial performance in the launch segment, access to scaled launch has fundamentally enabled the comparatively better financial performance of Starlink to date, while also supporting third-party commercial, civil, and national security customers.

## Exhibit 1: Starship's increased scale vs. Falcon and full reusability could drive launch costs into hundreds of dollars per kg SpaceX Starship

![](images/ac84877a408e5544fdc2b2d22feb116da57140c4af509b122a3ee92e9fd51362.jpg)  
BofA GLOBAL RESEARCH  
Source: SpaceX

Exhibit 2: Falcon's demonstrated booster recovery and reflight capability has driven sea change in launch cadence and cost to orbit
Landed Falcon 9 booster

![](images/877ff8f8adb554cb2528a3aea9e8484ef90734e9bf14c5e734045667a19cd522.jpg)  
Source: SpaceX  
BofA GLOBAL RESEARCH

## (+) Sticky relationships with US, int'l customers across segments

SpaceX has developed relationships across a diverse set of customers spanning commercial satellite operators, civil space agencies, defense organizations, and enterprise communications customers. Launch customers include commercial operators, NASA, the U.S. Department of Defense, and national security agencies, while Starlink now serves consumer, enterprise, aviation, maritime, mobility, and government markets across more than 160 countries. This diversification reduces dependence on any single customer segment and increases opportunities for cross-selling capabilities over time.

Customer relationships could become increasingly sticky as SpaceX expands beyond launch services into mission-critical connectivity and government applications. For example, Starlink is increasingly embedded into mobility, maritime, enterprise, and defense use cases (through Starshield) where reliability and global coverage are critical. Similarly, government customers are increasingly purchasing integrated capabilities spanning launch, communications, and national-security-focused services. As SpaceX broadens its portfolio, switching costs may increase as customers become reliant on an integrated ecosystem of transportation and communications infrastructure rather than a single standalone product.

## (+) Unparalleled vertical integration enables scale, derisks execution

SpaceX has oriented itself around end-to-end vertical integration as a means of controlling timelines, program ramps, and margins. This extends from the program and subsystem level – where SpaceX has in-housed the majority of its supply chains for launch, satellite buses, value-added payloads, and beyond – to the organization of its segments, where its constellation services are fundamentally enabled by internal launch capacity. This vertically integrated operating model enables rapid product iteration, tighter coordination across business units, and potentially lower total system costs than more fragmented competitors.

The value of this integration is particularly evident in Starlink. SpaceX designs and manufactures satellites, launches them on internally controlled vehicles, operates the communications network, and serves end customers directly. The company does not depend on third-party launch availability to deploy capacity or respond to network demand. This level of control has allowed SpaceX to scale Starlink to approximately 10,000 satellites and over 10 million subscribers in a relatively short timeframe. We believe this integrated model may become increasingly important as the company pursues larger and more complex opportunities such as next-gener

[中间内容因长度限制已省略]

nauthorized use or disclosure is prohibited. Receipt and review of this information constitutes your agreement not to redistribute, retransmit, or disclose to others the contents, opinions, conclusion, or information contained herein (including any investment recommendations, estimates or price targets) without first obtaining express permission from an authorized officer of BofA.

Materials prepared by BofA Global Research personnel are based on public information. Facts and views presented in this material have not been reviewed by, and may not reflect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

Information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Subject to the quiet period applicable under laws of the various jurisdictions in which we distribute research reports and other legal and BofA policy-related restrictions on the publication of research reports, fundamental equity reports are produced on a regular basis as necessary to keep the investment recommendation current.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies. Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
