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
# Cheap, but fundamentally challenged; Reinstating Underperform and \$190 PO

Reinstating Coverage: UNDERPERFORM | PO: 190.00 USD | Price: 218.07 USD

## AI-driven disruption narrows Adobe's competitive moat

We are reinstating coverage of Adobe (ADBE) with an Underperform rating and a \$190 PO, based on 7x CY27E EV/FCF. We flag rising risk to the growth profile as generative AI (GenAI) lowers barriers to content creation and increases competition from lower-cost and AI-native alternatives. We believe some professionals will remain focused on pixel level control and continue to utilize Adobe's tools, but AI will likely displace large parts of the core market over time, with likely pressure on pricing and seat expansion. We see Adobe's own AI strategy as largely defensive, supporting engagement and retention but limited on its ability to generate incremental high-quality ARR at scale.

## Growth reacceleration unlikely in the near term

Our report is centered on a key question: can Adobe reaccelerate growth in the age of AI? Adoption across AI products is notable, but we see limited evidence it translates into meaningful ARR uplift, with AI-first ARR still representing $<2\%$ of total ARR. Risk is concentrated in lower-end and prosumer cohorts, where “good enough” AI output can substitute for paid workflows, while professional and enterprise use cases remain more resilient but not immune. At the same time, the shift toward freemium and consumption-based pricing introduces monetization risk. We expect growth to decelerate over time and model it to decline from 10.5% in 2025 to 8.8% FY27E, with no clear path to near-term reacceleration.

## Valuation is tempting, but no catalyst in sight

The stock trades at the low end of the peer group, at 8x CY27E EV/FCF, but valuation alone is insufficient to drive outperformance, in our view. Our 7x CY27E EV/FCF multiple reflects structurally slower growth and increasing uncertainty around monetization quality. We expect margins and FCF generation to remain strong, but see limited multiple expansion without clear evidence of AI monetization and growth acceleration.

<table><tr><td>Estimates (Nov) (US$)</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>EPS</td><td>18.43</td><td>20.95</td><td>24.40</td><td>27.54</td><td>31.08</td></tr><tr><td>GAAP EPS</td><td>12.37</td><td>16.70</td><td>17.55</td><td>19.99</td><td>23.27</td></tr><tr><td>EPS Change (YoY)</td><td>14.8%</td><td>13.7%</td><td>16.5%</td><td>12.9%</td><td>12.9%</td></tr><tr><td>Consensus EPS (Bloomberg)</td><td></td><td></td><td>24.38</td><td>27.30</td><td>30.71</td></tr><tr><td>Consensus EPS (Visible Alpha)</td><td></td><td></td><td>18.03</td><td>20.99</td><td>23.99</td></tr><tr><td colspan="6">Valuation (Nov)</td></tr><tr><td>P/E</td><td>11.8x</td><td>10.4x</td><td>8.9x</td><td>7.9x</td><td>7.0x</td></tr><tr><td>GAAP P/E</td><td>17.6x</td><td>13.1x</td><td>12.4x</td><td>10.9x</td><td>9.4x</td></tr><tr><td>EV / EBITDA*</td><td>7.4x</td><td>6.8x</td><td>6.2x</td><td>5.8x</td><td>5.4x</td></tr><tr><td>Free Cash Flow Yield*</td><td>9.1%</td><td>11.4%</td><td>11.9%</td><td>12.9%</td><td>14.1%</td></tr><tr><td colspan="6">* For full definitions of iQmethodSMmeasures, see page 21.</td></tr></table>

## 07 July 2026

Equity

Tal Liani
Research Analyst
BofAS
+1 646 855 5107
tal.liani@bofa.com

Eden Vacnich
Research Analyst
BofAS
+1 646 855 1971
eden.vacnich@bofa.com

Kevin Niederpruem
Research Analyst
BofAS
+1 646 855-1540
kevin.niederpruem@bofa.com

## Stock Data

<table><tr><td>Price</td><td>218.07 USD</td></tr><tr><td>Price Objective</td><td>190.00 USD</td></tr><tr><td>Date Established</td><td>7-Jul-2026</td></tr><tr><td>Investment Opinion</td><td>B-3-9</td></tr><tr><td>52-Week Range</td><td>190.12 USD - 386.60 USD</td></tr><tr><td>Mrkt Val (mn) / Shares Out (mn)</td><td>86,683 USD / 397.5</td></tr><tr><td>Free Float</td><td>99.8%</td></tr><tr><td>Average Daily Value (mn)</td><td>1683.91 USD</td></tr><tr><td>BofA Ticker / Exchange</td><td>ADBE / NAS</td></tr><tr><td>Bloomberg / Reuters</td><td>ADBE US / ADBE.OQ</td></tr><tr><td>ROE (2026E)</td><td>83.2%</td></tr><tr><td>Net Dbt to Eqty (Nov-2025A)</td><td>6.7%</td></tr></table>

## See Glossary on page 19

<table><tr><td>Company Sector</td></tr><tr><td>Software</td></tr></table>

## iQprofile $^{SM}$ Adobe

## iQmethod $^{SM}$ – Bus Performance\*

<table><tr><td>(US$ Millions)</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Return on Capital Employed</td><td>37.6%</td><td>44.3%</td><td>46.6%</td><td>47.9%</td><td>47.8%</td></tr><tr><td>Return on Equity</td><td>54.1%</td><td>69.5%</td><td>83.2%</td><td>84.3%</td><td>79.7%</td></tr><tr><td>Operating Margin</td><td>46.6%</td><td>46.2%</td><td>45.0%</td><td>45.1%</td><td>45.0%</td></tr><tr><td>Free Cash Flow</td><td>7,873</td><td>9,852</td><td>10,323</td><td>11,161</td><td>12,245</td></tr></table>

## iQmethod $^{SM}$ – Quality of Earnings\*

<table><tr><td>(US$ Millions)</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Cash Realization Ratio</td><td>1.0x</td><td>1.1x</td><td>1.1x</td><td>1.1x</td><td>1.1x</td></tr><tr><td>Asset Replacement Ratio</td><td>0.1x</td><td>0.1x</td><td>0.1x</td><td>0.1x</td><td>0.1x</td></tr><tr><td>Tax Rate</td><td>19.8%</td><td>18.4%</td><td>23.2%</td><td>23.2%</td><td>22.6%</td></tr><tr><td>Net Debt-to-Equity Ratio</td><td>-14.1%</td><td>6.7%</td><td>4.8%</td><td>-17.5%</td><td>-40.2%</td></tr><tr><td>Interest Cover</td><td>NM</td><td>41.8x</td><td>46.3x</td><td>49.4x</td><td>NM</td></tr></table>

Income Statement Data (Nov)

<table><tr><td>(US$ Millions)</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Sales</td><td>21,505</td><td>23,769</td><td>26,531</td><td>28,857</td><td>31,357</td></tr><tr><td>% Change</td><td>10.8%</td><td>10.5%</td><td>11.6%</td><td>8.8%</td><td>8.7%</td></tr><tr><td>Gross Profit</td><td>19,264</td><td>21,489</td><td>23,843</td><td>25,825</td><td>28,075</td></tr><tr><td>% Change</td><td>12.2%</td><td>11.6%</td><td>11.0%</td><td>8.3%</td><td>8.7%</td></tr><tr><td>EBITDA</td><td>11,852</td><td>12,928</td><td>14,104</td><td>15,225</td><td>16,343</td></tr><tr><td>% Change</td><td>11.4%</td><td>9.1%</td><td>9.1%</td><td>7.9%</td><td>7.3%</td></tr><tr><td>Net Interest &amp; Other Income</td><td>142</td><td>(15)</td><td>(62)</td><td>(108)</td><td>(45)</td></tr><tr><td>Net Income (Adjusted)</td><td>8,284</td><td>8,946</td><td>9,748</td><td>10,574</td><td>11,545</td></tr><tr><td>% Change</td><td>12.3%</td><td>8.0%</td><td>9.0%</td><td>8.5%</td><td>9.2%</td></tr></table>

## Free Cash Flow Data (Nov)

<table><tr><td>(US$ Millions)</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Net Income from Cont Operations (GAAP)</td><td>5,560</td><td>7,130</td><td>7,013</td><td>7,676</td><td>8,645</td></tr><tr><td>Depreciation &amp; Amortization</td><td>1,833</td><td>1,942</td><td>2,155</td><td>2,224</td><td>2,224</td></tr><tr><td>Change in Working Capital</td><td>(165)</td><td>(167)</td><td>(264)</td><td>157</td><td>193</td></tr><tr><td>Deferred Taxation Charge</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>Other Adjustments, Net</td><td>828</td><td>1,126</td><td>1,633</td><td>1,392</td><td>1,497</td></tr><tr><td>Capital Expenditure</td><td>(183)</td><td>(179)</td><td>(213)</td><td>(289)</td><td>(314)</td></tr><tr><td>Free Cash Flow</td><td>7,873</td><td>9,852</td><td>10,323</td><td>11,161</td><td>12,245</td></tr><tr><td>% Change</td><td>13.4%</td><td>25.1%</td><td>4.8%</td><td>8.1%</td><td>9.7%</td></tr><tr><td>Share / Issue Repurchase</td><td>(9,500)</td><td>(11,281)</td><td>(8,811)</td><td>(8,444)</td><td>(8,444)</td></tr><tr><td>Cost of Dividends Paid</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>Change in Debt</td><td>0</td><td>(1,500)</td><td>0</td><td>0</td><td>0</td></tr></table>

## Balance Sheet Data (Nov)

<table><tr><td>(US$ Millions)</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Cash &amp; Equivalents</td><td>7,613</td><td>5,431</td><td>6,080</td><td>8,973</td><td>12,950</td></tr><tr><td>Trade Receivables</td><td>2,072</td><td>2,344</td><td>2,181</td><td>2,519</td><td>2,737</td></tr><tr><td>Other Current Assets</td><td>1,547</td><td>2,388</td><td>2,070</td><td>2,168</td><td>2,439</td></tr><tr><td>Property, Plant &amp; Equipment</td><td>1,936</td><td>1,873</td><td>1,506</td><td>897</td><td>251</td></tr><tr><td>Other Non-Current Assets</td><td>17,062</td><td>17,460</td><td>19,046</td><td>19,142</td><td>19,174</td></tr><tr><td>Total Assets</td><td>30,230</td><td>29,496</td><td>30,884</td><td>33,699</td><td>37,550</td></tr><tr><td>Short-Term Debt</td><td>1,499</td><td>0</td><td>1,843</td><td>1,843</td><td>1,843</td></tr><tr><td>Other Current Liabilities</td><td>9,022</td><td>10,200</td><td>10,797</td><td>12,061</td><td>13,452</td></tr><tr><td>Long-Term Debt</td><td>4,129</td><td>6,210</td><td>4,802</td><td>4,802</td><td>4,802</td></tr><tr><td>Other Non-Current Liabilities</td><td>1,475</td><td>1,463</td><td>1,622</td><td>1,717</td><td>1,753</td></tr><tr><td>Total Liabilities</td><td>16,125</td><td>17,873</td><td>19,064</td><td>20,423</td><td>21,850</td></tr><tr><td>Total Equity</td><td>14,105</td><td>11,623</td><td>11,820</td><td>13,276</td><td>15,701</td></tr><tr><td>Total Equity &amp; Liabilities</td><td>30,230</td><td>29,496</td><td>30,884</td><td>33,699</td><td>37,550</td></tr></table>

\* For full definitions of IQmethod $^{SM}$ measures, see page 21.

## Company Description

Adobe is a diversified software company providing cloud-based solutions across digital media, document workflows, and enterprise marketing. The company's core offerings include Creative Cloud, Document Cloud, and Experience Cloud, serving creative professionals, enterprises, and a broad base of prosumer and business users. Adobe's platforms are built around industry standards such as Photoshop and Acrobat, with increasing integration of AI capabilities across products.

## Investment Rationale

We see increasing risk to Adobe's growth trajectory driven by: 1) AI compressing barriers of entry for competition from point solutions and AI-natives, 2) slowing adoption with potential seat reduction in the core creative professional market segment, and 3) AI consumption may weigh on margins and profitability. This is balanced by: 1) large Creative Cloud subscriber base 2) distribution channel & marketing personnel 3) breadth & depth of the digital content and experience software suite.

## Stock Data

<table><tr><td>Average Daily Volume</td><td>7,721,867</td></tr></table>

## Quarterly Earnings Estimates

<table><tr><td></td><td>2025</td><td>2026</td></tr><tr><td>Q1</td><td>5.08A</td><td>6.05A</td></tr><tr><td>Q2</td><td>5.06A</td><td>5.97A</td></tr><tr><td>Q3</td><td>5.31A</td><td>6.08E</td></tr><tr><td>Q4</td><td>5.50A</td><td>6.30E</td></tr></table>

## Can growth reaccelerate in the GenAI era?

Adobe remains deeply entrenched across creative, document, and marketing workflows, and its products remain the standard for many creative professionals and enterprises. The install base gives Adobe meaningful advantages: broad distribution, strong brand recognition, workflow familiarity, high switching costs in professional use cases, and a large subscription revenue base.

However, the stock is down 70% since its 2024 peak (vs. +68% NASDAQ index) on growing concerns that GenAI could structurally disrupt Adobe's core value proposition by lowering the skill barrier for content creation, enabling cheaper and simpler AI-native competitors, and shifting value away from tools and toward models and workflows. This threatens Adobe's pricing power, seat-based revenue model, and growth durability. Even with solid AI product execution, the risk is that Adobe becomes less valuable in a world where creation is increasingly simplified, resulting in sustained growth slowdown.

The Company responded by introducing its own AI based solutions, and we see evidence of initial traction. In 2Q26, AI-first ARR more than tripled YoY to \~\$500mn and in 1Q26, generative credit consumption grew 45% QoQ. This traction remains early in the monetization cycle, representing less than 2% of total ARR, and we believe will unlikely drive meaningful growth reacceleration.

We frame our views across five key points in this report:

\- Asymmetrical risk of AI disruption across different customer segments: risk is highest in lower-end non-professional use cases, while professional and enterprise use cases remain more resilient, but not immune.

\- AI monetization is progressing, but not yet material: We see strong adoption across Firefly with +50% ARR growth QoQ, Acrobat and Express also saw +21% MAUs growth QoQ, and Creative Freemium MAUs were up +70% YoY However, this growth has not translated into meaningful ARR uplift or revenue acceleration as the company is focusing on freemium attach.

\- Cannibalization of legacy products: Progress in AI capabilities has begun to pressure paid assets and incremental seats, creating downside risk to higher-margin businesses. Adobe has acknowledged pressure on certain monetization vectors, including continued declines in Adobe Stock, though it does not quantify the impact. Looking ahead, we see broader risk to seat expansion and pricing as free or low-cost alternatives substitute for paid workflows.

\- Leadership departure adds execution risk at key AI transition: simultaneous CEO and CFO turnover heightens risk around strategy, continuity, and leadership stability.

\- Valuation is attractive, but the stock lacks catalysts given the fundamental challenges. Stock valuation already discounts slower growth and AI risk, and we believe downside risk is limited. However, the potential for AI monetization and growth reacceleration remains constrained, and we don't see a clear near-term catalyst for multiple expansion.

Our view: AI risk is real; low valuation is insufficient for a more positive view

Current valuation reflects 8x CY27E EV/FCF, compared to historical range of \~25-30x. We also flag strong operating margins of 45% and FCF margins of 39%, supporting robust FCF generation. Nevertheless, we reinstate coverage with an Underperform rating, as we believe the company will face challenges to maintain its base due to AI disruption, which could pressure a large part of its revenue base. We believe the company will have difficulty converting its AI innovation to meaningful ARR contribution, and that the current AI growth is mostly related to Freemium attach rather than new product monetization.

The key issue is both adoption and economics, in our view. We see Adobe's AI strategy as largely defensive and believe structural disruption makes recovery challenging. We see the market as fabricated to a small group of power users who require pixel-based control and the unique tools Adobe is providing, and a larger group of occasional users, where AI represents a serious risk of displacement and migration to cheaper AI-native solutions, which brings up potential risks to the number of seats, and potential cannibalization of high-margin legacy revenues.

## Eroding moat in the age of AI

Advancements in GenAI capabilities lower the barriers of entry for creative software, and we see clear evidence of pressure on growth.

Subscription revenues account for 97% of total revenues, and until FY26 were reported in two segments: Digital Media (\~75% of sub revenue) and Digital Experience (\~25%). The Company no longer provides this disclosure and now reports subscription revenue across two customer-oriented groups: Creative & Marketing Professionals (\~71% of sub revenue) and Business Professionals & Consumers (\~29%).

\- Creative & Marketing Professionals (CMP). This segment accounts for 71% of subscription revenues and addresses professional creators, creative teams, marketers, and enterprises that rely on Adobe to create, manage, distribute, and measure content across channels. CMP includes Creative Cloud, Digital Experience, Firefly & AI tools, as well as adjacent creative workflow products. Growth trends of this segment are somewhat more stable with growth accelerating from 9.9% in FY24 to 11.8% in FY26, mainly driven by uplift from the recent SEMRush acquisition. However, we model a decline in the growth rate to 8.6% by FY28 reflecting increasing pressure from AI-native competition and slower growth in mature Creative Cloud workflows.

\- Business Professionals & Consumers (BPC). This segment accounts for 29% of subscription revenue and represents Adobe's volume-driven segment, focused on document workflows and productivity use cases across SMBs, enterprises, and individual users. It addresses users that rely on Adobe for document creation, editing, and collaboration, and includes Document Cloud (Acrobat) and Adobe Express. We model a decline in growth from 14.6% in FY25 to 10.8% by FY28, reflecting increasing competition from freemium and lower-cost alternatives, limiting incremental monetization and pricing power.

Exhibit 1: CMP remains the majority of revenue, while BPC grows faster off a smaller base
Subscription segment revenue estimates, FY24-FY28E

<table><tr><td></td><td>FY24</td><td>FY25</td><td>FY26E</td><td>FY27E</td><td>FY28E</td></tr><tr><td>Total Subscription Revenue ($, mn)</td><td>20,521.0</td><td>22,904.0</td><td>25,768.6</td><td>28,102.8</td><td>30,716.0</td></tr><tr><td>YoY growth (%)</td><td>12.2%</td><td>11.6%</td><td>12.5%</td><td>9.1%</td><td>9.3%</td></tr><tr><td>Creative &amp; Marketing Professionals Revenue ($, mn)</td><td>14,750.0</td><td>16,310.0</td><td>18,242.7</td><td>19,765.6</td><td>21,468.5</td></tr><tr><td>YoY growth (%)</td><td>9.9%</td><td>10.6%</td><td>11.8%</td><td>8.3%</td><td>8.6%</td></tr><tr><td>share of total subscription revenue (%)</td><td>71.9%</td><td>71.2%</td><td>70.8%</td><td>70.3%</td><td>69.9%</td></tr><tr><td>Business Professionals &amp; Consumers Revenue ($, mn)</td><td>5,670.0</td><td>6,500.0</td><td>7,461.4</td><td>8,322.1</td><td>9,217.2</td></tr><tr><td>YoY growth (%)</td><td>19.4%</td><td>14.6%</td><td>14.8%</td><td>11.5%</td><td>10.8%</td></tr><tr><td>share of total subscription revenue (%)</td><td>27.6%</td><td>28.4%</td><td>29.0%</td><td>29.6%</td><td>30.0%</td></tr></table>

Source: BofA Global Research estimates, company report  
BofA GLOBAL RESEARCH

## Asymmetrical AI risk across different customer profiles

The company does not disclose revenue split by customer type, yet we see the risks and opportunities around GenAI as be

[中间内容因长度限制已省略]

ailable material. Any unauthorized use or disclosure is prohibited. Receipt and review of this information constitutes your agreement not to redistribute, retransmit, or disclose to others the contents, opinions, conclusion, or information contained herein (including any investment recommendations, estimates or price targets) without first obtaining express permission from an authorized officer of BofA.

Materials prepared by BofA Global Research personnel are based on public information. Facts and views presented in this material have not been reviewed by, and may not reflect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Subject to the quiet period applicable under laws of the various jurisdictions in which we distribute research reports and other legal and BofA policy-related restrictions on the publication of research reports, fundamental equity reports are produced on a regular basis as necessary to keep the investment recommendation current.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.
"""
