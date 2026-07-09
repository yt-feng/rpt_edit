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

<table><tr><td colspan="10">EUR millions except per share data</td></tr><tr><td rowspan="2"></td><td colspan="3">FY27E</td><td colspan="3">FY28E</td><td colspan="3">FY29E</td></tr><tr><td>Old</td><td>New</td><td>% chg</td><td>Old</td><td>New</td><td>% chg</td><td>Old</td><td>New</td><td>% chg</td></tr><tr><td>Sales</td><td>624.5</td><td>604.1</td><td>-3.3%</td><td>780.6</td><td>741.9</td><td>-5.0%</td><td>1,033.1</td><td>955.6</td><td>-7.5%</td></tr><tr><td>YoY growth (%)</td><td>5.5%</td><td>2.0%</td><td>-344 bps</td><td>25.0%</td><td>22.8%</td><td>-220 bps</td><td>32.3%</td><td>28.8%</td><td>-354 bps</td></tr><tr><td>LfL growth (%) (at Constant Scope &amp; FX)</td><td>5.5%</td><td>2.0%</td><td>-344 bps</td><td>25.0%</td><td>22.8%</td><td>-220 bps</td><td>32.3%</td><td>28.8%</td><td>-354 bps</td></tr><tr><td>FX effect</td><td>0.0%</td><td>0.0%</td><td>-</td><td>0.0%</td><td>0.0%</td><td>-</td><td>0.0%</td><td>0.0%</td><td>-</td></tr><tr><td>Gross profit</td><td>143.9</td><td>119.8</td><td>-16.8%</td><td>234.2</td><td>207.7</td><td>-11.3%</td><td>361.6</td><td>305.8</td><td>-15.4%</td></tr><tr><td>margin (%)</td><td>23.0%</td><td>19.8%</td><td>-322 bps</td><td>30.0%</td><td>28.0%</td><td>-200 bps</td><td>35.0%</td><td>32.0%</td><td>-300 bps</td></tr><tr><td>EBITDA (Continuing operations)</td><td>188.1</td><td>162.0</td><td>-13.9%</td><td>274.9</td><td>248.0</td><td>-9.8%</td><td>389.2</td><td>337.0</td><td>-13.4%</td></tr><tr><td>margin (%)</td><td>30.1%</td><td>26.8%</td><td>-332 bps</td><td>35.2%</td><td>33.4%</td><td>-178 bps</td><td>37.7%</td><td>35.3%</td><td>-240 bps</td></tr><tr><td>Operating income (EBIT)</td><td>22.1</td><td>2.0</td><td>-91.1%</td><td>101.5</td><td>81.6</td><td>-19.6%</td><td>206.6</td><td>162.4</td><td>-21.4%</td></tr><tr><td>margin (%)</td><td>3.5%</td><td>0.3%</td><td>-322 bps</td><td>13.0%</td><td>11.0%</td><td>-200 bps</td><td>20.0%</td><td>17.0%</td><td>-300 bps</td></tr><tr><td>Net Profit (Group)</td><td>11.2</td><td>-5.9</td><td>-153.2%</td><td>81.0</td><td>63.7</td><td>-21.3%</td><td>175.5</td><td>137.3</td><td>-21.8%</td></tr><tr><td>Net Margin (%)</td><td>2%</td><td>-1.0%</td><td></td><td>10%</td><td>9%</td><td></td><td>17%</td><td>14%</td><td></td></tr><tr><td>Basic EPS (calculated)</td><td>0.31</td><td>-0.17</td><td>-153.2%</td><td>2.27</td><td>1.79</td><td>-21.3%</td><td>4.92</td><td>3.85</td><td>-21.8%</td></tr><tr><td>Diluted EPS (calculated)</td><td>0.31</td><td>-0.17</td><td>-153.2%</td><td>2.26</td><td>1.78</td><td>-21.3%</td><td>4.88</td><td>3.82</td><td>-21.8%</td></tr><tr><td>Operating Exp.</td><td>-121.8</td><td>-117.8</td><td>-3.3%</td><td>-132.7</td><td>-126.1</td><td>-5.0%</td><td>-155.0</td><td>-143.3</td><td>-7.5%</td></tr><tr><td>Net Debt (Cash)</td><td>-22.0</td><td>-9.0</td><td>-59.2%</td><td>-195.3</td><td>-173.3</td><td>-11.3%</td><td>-318.4</td><td>-275.0</td><td>-13.6%</td></tr><tr><td>Capex</td><td>125.0</td><td>125.0</td><td>0.0%</td><td>125.0</td><td>115.0</td><td>-8.0%</td><td>125.0</td><td>115.0</td><td>-8.0%</td></tr></table>

<table><tr><td colspan="10">SEGMENTS:</td></tr><tr><td>Mobile Communications</td><td>291.6</td><td>275.8</td><td>-5.4%</td><td>389.2</td><td>326.9</td><td>-16.0%</td><td>567.1</td><td>415.1</td><td>-26.8%</td></tr><tr><td>YoY growth (%)</td><td>-5.6%</td><td>-10.7%</td><td>-508 bps</td><td>33.5%</td><td>18.5%</td><td>-1500 bps</td><td>45.7%</td><td>27.0%</td><td>-1870 bps</td></tr><tr><td>Automotive &amp; Industrial</td><td>80.4</td><td>69.2</td><td>-13.9%</td><td>90.8</td><td>78.2</td><td>-13.9%</td><td>104.4</td><td>89.2</td><td>-14.6%</td></tr><tr><td>YoY growth (%)</td><td>14.8%</td><td>-1.1%</td><td>-1591 bps</td><td>13.0%</td><td>13.0%</td><td>-</td><td>15.0%</td><td>14.0%</td><td>-100 bps</td></tr><tr><td>Edge &amp; Cloud AI</td><td>252.6</td><td>259.0</td><td>2.6%</td><td>300.6</td><td>336.8</td><td>12.0%</td><td>361.6</td><td>451.3</td><td>24.8%</td></tr><tr><td>YoY growth (%)</td><td>18.0%</td><td>21.0%</td><td>303 bps</td><td>19.0%</td><td>30.0%</td><td>1100 bps</td><td>20.3%</td><td>34.0%</td><td>1370 bps</td></tr><tr><td>Total Revenue</td><td>624.

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
