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
# Healthcare - China (H/A)

# Robust deal activity and continued R&D progress driving healthcare re-rating

Price Objective Change

## CSPC: another collaboration with AstraZeneca

On 2 July, CSPC announced a collaboration agreement with AstraZeneca (AZ) to leverage CSPC's siRNA drug-discovery and extrahepatic targeted-delivery platforms. CSPC and AZ will co-develop PCCs for two renal disease targets. AZ will have the option to obtain exclusive global, or ex-China, rights for each preclinical candidate, while CSPC will retain China rights to one candidate. CSPC will receive an upfront payment of US\$30mn and is eligible for up to US\$540mn/US\$1.2bn in development/sales milestone payments plus potential single-digit royalties. We add the US\$30mn upfront payment to our estimates and raise our 2027 revenue/NP estimate by 0.8%/2.0%, as well as lift our long-term sales estimates. Our PO increases to HK\$7.6 from HK\$6.8. However, we reiterate our Underperform rating on CSPC given continued sales pressure on its key marketed drugs.

## Gushengtang: footprint expansion through acquisitions

On 5 July, Gushengtang (GST) announced the acquisitions of Shahe Hospital and Beijing Hongyang Hospital. The acquisitions will expand the company's medical institution network and strengthen its presence in Beijing. Mgmt. expects the acquired hospitals to generate synergies with GST's existing medical institutions and online healthcare platform. The transactions will be funded by proceeds from the company's recent share placement and convertible bond issuance, as well as internal cash resources. We maintain our Buy rating and HK\$32.60 PO on GST.

## Innovent: commercialization deal with Lilly on CDK4/6

Recently, Innovent announced a commercialization agreement with Lilly for Verzenios (abemaciclib) in mainland China. Under the agreement, Innovent will be responsible for the product's imports, marketing, distribution, and promotion. Verzenios was the first CDK4&6 inhibitor to be included in the NRDL in 2021 and has since secured reimbursement coverage for both early and advanced breast cancer indications. To reflect the revenue contribution from abemaciclib from 2H26, we lift our 2026/27/28 revenue estimates by 3.3%/5.3%/4.7%. Consequently, we raise our DCF-derived PO to HK\$119.2 (from HK\$116.8) and reiterate our Buy rating given the company's enriched commercial products portfolio and solid in-house R&D capabilities.

## Hengrui: multiple innovative drug R&D updates

Hengrui has announced multiple R&D updates recently. It disclosed that the marketing application for SHR-A1811's third indication (1L/2L HER2-low mBC) has been accepted by NMPA and granted priority review. In addition, Hengrui received clinical trial approvals for several innovative drug candidates, including HRS-4508 (for breast and lung cancers), SHR-6914 (for PCa), HRS-7525 (for solid tumor), and several combo therapies. Although we are concerned about the potential impact on generics from the new round of anti-corruption campaign, especially in low-tier cities, we still believe its sales growth on innovative drugs portfolio can achieve 30% growth in 2026E. We reiterate our Buy rating and RMB\$72.70 PO on Hengrui.

## 07 July 2026

Equity
China
Healthcare

David Li >>
Research Analyst
BofA (Hong Kong)
+852 3508 4531
davidbo.li@bofa.com

Sandra Sun >>
Research Analyst
BofA (Hong Kong)
sandra.sun@bofa.com

Ethan Cui >>
Research Analyst
BofA (Hong Kong)
ethan.cui@bofa.com

## Exhibit 1: PO changes

We lift CSPC's and Innovent's POs

<table><tr><td>Company</td><td>Currency</td><td>Old PO</td><td>New PO</td></tr><tr><td>CSPC</td><td>HK$</td><td>6.8</td><td>7.6</td></tr><tr><td>Innovent</td><td>HK$</td><td>116.8</td><td>119.2</td></tr></table>

Source: BofA Global Research  
BofA GLOBAL RESEARCH

## Abbreviations:

siRNA: Small interfering ribonucleic acid

PCC: Pre-clinical Candidate

GST: Gushengtang

CDK4/6: Cyclin-Dependent Kinase 4/6

NRDL: National Reimbursement Drug List

HER2: Human Epidermal Growth Factor Receptor 2

mBC: Metastatic Breast Cancer

1/2L: first/second-line

NMPA: National Medical Products Administration

PCa: prostate cancer

EGFR: Epidermal Growth Factor Receptor

ADC: Antibody-Drug Conjugate

NSCLC: Non-Small Cell Lung Cancer

NP: Net Profit

## Estimate changes

## CSPC

Separately, CSPC has initiated two Phase III studies for SYS6010 (EGFR ADC) in NSCLC recently. We add the US\$30mn upfront payment to our estimate and raise our 2027 revenue/NP estimates by 0.8%/2.0%. As the partnered candidates remain at the preclinical stage, we do not include any revenue contribution from these candidates in our estimates. We also raise our SYS6010 NSCLC penetration assumptions from 2029 and lift our revenue estimates for the product, reflecting its broader Phase III development plan. Overall, we lift our PO to HK\$7.6 from HK\$6.8. We reiterate our Underperform rating given continued sales pressure on CSPC's key marketed drugs.

## Exhibit 2: Estimate changes

We raise 2027E revenue/NP by 0.8%/2.0%

<table><tr><td></td><td colspan="3">New</td><td colspan="3">Old</td><td colspan="3">% Change (New vs Old)</td></tr><tr><td>(RMB mn)</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Total Revenue</td><td>34,906</td><td>25,493</td><td>27,155</td><td>34,906</td><td>25,281</td><td>27,155</td><td>0.0%</td><td>0.8%</td><td>0.0%</td></tr><tr><td>COGS</td><td>(8,884)</td><td>(8,624)</td><td>(9,232)</td><td>(8,884)</td><td>(8,620)</td><td>(9,232)</td><td>0.0%</td><td>0.0%</td><td>0.0%</td></tr><tr><td>Gross profit</td><td>26,022</td><td>16,868</td><td>17,923</td><td>26,022</td><td>16,661</td><td>17,923</td><td>0.0%</td><td>1.2%</td><td>0.0%</td></tr><tr><td>Selling and distribution costs</td><td>(6,458)</td><td>(6,118)</td><td>(6,246)</td><td>(6,458)</td><td>(6,067)</td><td>(6,246)</td><td>0.0%</td><td>0.8%</td><td>0.0%</td></tr><tr><td>Administrative expenses</td><td>(956)</td><td>(892)</td><td>(950)</td><td>(956)</td><td>(885)</td><td>(950)</td><td>0.0%</td><td>0.8%</td><td>0.0%</td></tr><tr><td>R&amp;D expense</td><td>(5,829)</td><td>(5,353)</td><td>(5,838)</td><td>(5,829)</td><td>(5,309)</td><td>(5,838)</td><td>0.0%</td><td>0.8%</td><td>0.0%</td></tr><tr><td>Financing expenses</td><td>(31)</td><td>(25)</td><td>(19)</td><td>(31)</td><td>(25)</td><td>(19)</td><td>0.0%</td><td>0.0%</td><td>0.0%</td></tr><tr><td>Profit Before Tax</td><td>13,638</td><td>5,371</td><td>5,815</td><td>13,638</td><td>5,266</td><td>5,815</td><td>0.0%</td><td>2.0%</td><td>0.0%</td></tr><tr><td>Tax expense</td><td>(2,387)</td><td>(940)</td><td>(1,018)</td><td>(2,387)</td><td>(922)</td><td>(1,018)</td><td>0.0%</td><td>2.0%</td><td>0.0%</td></tr><tr><td>Net Income</td><td>11,082</td><td>4,364</td><td>4,725</td><td>11,082</td><td>4,279</td><td>4,725</td><td>0.0%</td><td>2.0%</td><td>0.0%</td></tr><tr><td>Adjusted net income</td><td>11,127</td><td>4,411</td><td>4,774</td><td>11,127</td><td>4,326</td><td>4,774</td><td>0.0%</td><td>2.0%</td><td>0.0%</td></tr><tr><td>Basic EPS</td><td>0.97</td><td>0.38</td><td>0.41</td><td>0.97</td><td>0.37</td><td>0.41</td><td>0.0%</td><td>2.0%</td><td>0.0%</td></tr><tr><td>Fully diluted EPS</td><td>0.97</td><td>0.38</td><td>0.41</td><td>0.97</td><td>0.37</td><td>0.41</td><td>0.0%</td><td>2.0%</td><td>0.0%</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="3">changes in percentage point</td></tr><tr><td>Gross margin (%)</td><td>74.5%</td><td>66.2%</td><td>66.0%</td><td>74.5%</td><td>65.9%</td><td>66.0%</td><td>0.0</td><td>0.3</td><td>0.0</td></tr><tr><td>Selling expense % of sales</td><td>-18.5%</td><td>-24.0%</td><td>-23.0%</td><td>-18.5%</td><td>-24.0%</td><td>-23.0%</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>G&amp;A % of sales</td><td>-2.7%</td><td>-3.5%</td><td>-3.5%</td><td>-2.7%</td><td>-3.5%</td><td>-3.5%</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>R&amp;D expenses as % of sales</td><td>-16.7%</td><td>-21.0%</td><td>-21.5%</td><td>-16.7%</td><td>-21.0%</td><td>-21.5%</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Tax rate (%)</td><td>-17.5%</td><td>-17.5%</td><td>-17.5%</td><td>-17.5%</td><td>-17.5%</td><td>-17.5%</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Net margin (%)</td><td>31.7%</td><td>17.1%</td><td>17.4%</td><td>31.7%</td><td>16.9%</td><td>17.4%</td><td>0.0</td><td>0.2</td><td>0.0</td></tr><tr><td>%yoy Growth</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Revenue</td><td>34.2%</td><td>-27.0%</td><td>6.5%</td><td>34.2%</td><td>-27.6%</td><td>7.4%</td><td>0.0</td><td>0.6</td><td>-0.9</td></tr><tr><td>Net income</td><td>185.5%</td><td>-60.6%</td><td>8.3%</td><td>185.5%</td><td>-61.4%</td><td>10.4%</td><td>0.0</td><td>0.8</td><td>-2.2</td></tr></table>

Source: BofA Global Research estimates  
BofA GLOBAL RESEARCH

## Innovent

Exhibit 3: Estimate changes

We lift 2026/27/28E revenue by 3.3%/5.3%/4.7%

<table><tr><td></td><td colspan="3">New</td><td colspan="3">Old</td><td colspan="3">% Change (New vs Old)</td></tr><tr><td>(RMB mn)</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Total Revenue</td><td>18,453</td><td>25,001</td><td>27,688</td><td>17,871</td><td>23,749</td><td>26,447</td><td>3.3%</td><td>5.3%</td><td>4.7%</td></tr><tr><td>COGS</td><td>-2,566</td><td>-4,443</td><td>-4,974</td><td>-2,450</td><td>-4,193</td><td>-4,726</td><td>4.8%</td><td>6.0%</td><td>5.3%</td></tr><tr><td>Gross profit</td><td>15,886</td><td>20,558</td><td>22,714</td><td>15,421</td><td>19,557</td><td>21,721</td><td>3.0%</td><td>5.1%</td><td>4.6%</td></tr><tr><td>R&amp;D expense</td><td>-4,613</td><td>-4,500</td><td>-4,569</td><td>-4,468</td><td>-4,275</td><td>-4,364</td><td>3.3%</td><td>5.3%</td><td>4.7%</td></tr><tr><td>SG&amp;A expense</td><td>-9,226</td><td>-12,000</td><td>-13,014</td><td>-8,935</td><td>-11,400</td><td>-12,430</td><td>3.3%</td><td>5.3%</td><td>4.7%</td></tr><tr><td>Other income/expense</td><td>400</td><td>400</td><td>400</td><td>400</td><td>400</td><td>400</td><td></td><td></td><td></td></tr><tr><td>Operating income</td><td>996</td><td>2,861</td><td>3,776</td><td>966</td><td>2,686</td><td>3,571</td><td>3.0%</td><td>6.5%</td><td>5.7%</td></tr><tr><td>Other income/expenses</td><td>167</td><td>250</td><td>277</td><td>162</td><td>237</td><td>264</td><td>3.3%</td><td>5.3%</td><td>4.7%</td></tr><tr><td>Finance costs</td><td>-88</td><td>-95</td><td>-95</td><td>-88</td><td>-95</td><td>-95</td><td>0.0%</td><td>0.0%</td><td>0.0%</td></tr><tr><td>Profit Before Tax</td><td>1,075</td><td>3,015</td><td>3,957</td><td>1,041</td><td>2,828</td><td>3,740</td><td>3.3%</td><td>6.6%</td><td>5.8%</td></tr><tr><td>Tax expense</td><td>-140</td><td>-392</td><td>-514</td><td>-135</td><td>-368</td><td>-486</td><td>3.3%</td><td>6.6%</td><td>5.8%</td></tr><tr><td>Net Income</td><td>935</td><td>2,623</td><td>3,443</td><td>905</td><td>2,460</td><td>3,254</td><td>3.3%</td><td>6.6%</td><td>5.8%</td></tr><tr><td>Basic EPS</td><td>0.56</td><td>1.56</td><td>2.05</td><td>0.54</td><td>1.47</td><td>1.94</td><td>3.3%</td><td>6.6%</td><td>5.8%</td></tr><tr><td>Fully diluted EPS</td><td>0.54</td><td>1.51</td><td>1.98</td><td>0.52</td><td>1.41</td><td>1.87</td><td>3.3%</td><td>6.6%</td><td>5.8%</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="3">(changes in percentage points)</td></tr><tr><td>Gross margin (%)</td><td>86%</td><td>82%</td><td>82%</td><td>86%</td><td>82%</td><td>82%</td><td>-0.2</td><td>-0.1</td><td>-0.1</td></tr><tr><td>R&amp;D expense % of sales</td><td>-25%</td><td>-18%</td><td>-17%</td><td>-25%</td><td>-18%</td><td>-17%</td><td>0.0</td><td>0.0</td><td>0.0</td></tr></table>

## Exhibit 3: Estimate changes

We lift 2026/27/28E revenue by 3.3%/5.3%/4.7%

<table><tr><td></td><td colspan="3">New</td><td colspan="3">Old</td><td colspan="3">% Change (New vs Old)</td></tr><tr><td>SG&amp;A % of sales</td><td>-50%</td><td>-48%</td><td>-47%</td><td>-50%</td><td>-48%</td><td>-47%</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Operating margin (%)</td><td>5%</td><td>11%</td><td>14%</td><td>5%</td><td>11%</td><td>14%</td><td>0.0</td><td>0.1</td><td>0.1</td></tr><tr><td>Tax rate (%)</td><td>-13%</td><td>-13%</td><td>-13%</td><td>-13%</td><td>-13%</td><td>-13%</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Net margin (%)</td><td>5%</td><td>10%</td><td>12%</td><td>5%</td><td>10%</td><td>12%</td><td>0.0</td><td>0.1</td><td>0.1</td></tr><tr><td>% yoy</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Revenue</td><td>41%</td><td>35%</td><td>11%</td><td>37%</td><td>33%</td><td>11%</td><td>4.5</td><td>2.6</td><td>-0.6</td></tr></table>

Source: BofA Global Research estimates  
BofA GLOBAL RESEARCH

## Exhibit 4: Stocks mentioned

Prices and ratings for stocks mentioned in this report

<table><tr><td>BofA Ticker</td><td>Bloomberg ticker</td><td>Company name</td><td>Price</td><td>Rating</td></tr><tr><td>CHJTF</td><td>1093 HK</td><td>CSPC Pharmaceutical</td><td>HK$ 8.23</td><td>C-3-7</td></tr><tr><td>GSHTF</td><td>2273 HK</td><td>Gushengtang</td><td>HK$ 30.78</td><td>C-1-7</td></tr><tr><td>XMOKF</td><td>600276 CH</td><td>Hengrui Medicine</td><td>CNY 56.77</td><td>B-1-7</td></tr><tr><td>IVBXF</td><td>1801 HK</td><td>Innovent</td><td>HK$ 90.5</td><td>C-1-9</td></tr></table>

Source: BofA Global Research  
BofA GLOBAL RESEARCH

## Price objective basis & risk

## CSPC Pharmaceutical (CHJTF)

Our DCF model for CSPC derived a PO of HK\$7.6. Our assumption of the DCF model includes a 5% debt-to-asset ratio, a 4.0% risk free rate, 7.0% market premium, and 5.0% cost of debt. We apply beta of 0.8 and arrive at 9.6% cost of equity and 9.3% WACC. We estimate a 1.5% terminal growth for the company.

Upside risks to our PO are: strong performance of newly launched products, lower-than-expected impact from VBP and NRDL price cut, better-than-expected clinical progress and results.

Downside risks to our PO are: price-cut pressure from VBP on new drugs, failure in clinical trials.

## Gushengtang (GSHTF)

We use discounted cash flow to arrive at a PO of HK\$32.6. We use a debt to asset ratio of 5%, a risk free rate of 4%, a market premium of 7%, and a beta of 1.1 to arrive at a 11.7% cost of equity. We also apply a 5% cost of debt. We use a WACC of 11.4% and a terminal growth of 1.5%.

Downside risks: 1) policy and regulatory risks on TCM and healthcare service providers, 2) intense competition, 3) failure in recruiting professionals, 4) data protection risks, 5) soft consumption environment in China and weak demand for TCM services.

## Hengrui Medicine (XMOKF)

Our PO of RMB72.7 is based on a DCF model. Our assumption of the DCF model includes a 0% debt-to-asset ratio, a 2.0% risk free rate, 7.0% market premium, and 5.1% cost of debt. We apply beta of 0.69 and arrive at 6.8% cost of equity. We estimate a

## 3.5% terminal growth for the company.

Downside risks to our PO are (1) setback in drug development and a delay in product approvals, (2) slow sales ramp-up of new products, (3) increasing pricing risk from VBP (4) stiffer competition for PD-1 and other drugs, and (5) slow overseas expansion.

Upside risks to our PO are: (1) higher-than-expected net profit margin and (2) faster-than-expected progress of pipeline candidates.

## Innovent (IVBXF)

We derive our PO of HK\$119.2 from a DCF model, assuming a WACC of 9.6% and a terminal growth rate of 4%. The DCF is based on PD-1, biosimilars, mazdutide and a few other drugs' commercial sales as well as revenue estimate of key pipeline assets including IBI363 and others.

Downside risks: commercialization for PD-1 and biosimilars below expectation, clinical development setback for late stage assets, and pricing pressure from NRDL's inclusion of competitors' products.

Upside risk: faster-than-expected sales growth of drugs included in NRDL.

## Analyst Certification

We, David Li and Ethan Cui, hereby certify that the views each of us has expressed in this research report accurately reflect each of our respective personal views about the subject securities and issuers. We also certify that no part of our respective compensation was, is, or will be, directly or indirectly, related to the specific recommendations or view expressed in this research report.

APR - Healthcare Coverage Cluster

<table><tr><td>Investment rating</td><td>Company</td><td>BofA Ticker</td><td>Bloomberg symbol</td><td>Analyst</td></tr><tr><td colspan="5">BUY</td></tr><tr><td></td><td>Adicon Holdings</td><td>ADCNF</td><td>9860 HK</td><td>David Li</td></tr><tr><td></td><td>Aier Eye Hospital</td><td>XAEOF</td><td>300015 CH</td><td>David Li</td></tr><tr><td></td><td>Akeso</td><td>AKESF</td><td>9926 HK</td><td>Ethan Cui</td></tr><tr><td></td><td>Angelalign Technology Inc</td><td>AGLFF</td><td>6699 HK</td><td>David Li</td></tr><tr><td></td><td>Apollo Hospital</td><td>XWQAF</td><td>APHS IN</td><td>Neha Manpuria</td></tr><tr><td></td><td>Astellas Pharma</td><td>ALPMF</td><td>4503 JP</td><td>Koichi Mamegano</td></tr><tr><td></td><td>Astellas Pharma</td><td>ALPMY</td><td>ALPMY US</td><td>Koichi Mamegano</td></tr><tr><td></td><td>Asymchem Laboratories</td><td>XALPF</td><td>002821 CH</td><td>David Li</td></tr><tr><td></td><td>Aurobindo</td><td>XLZFF</td><td>ARBP IN</td><td>Neha Manpuria</td></tr><tr><td></td><td>Baiyunshan</td><td>GZPHF</td><td>874 HK</td><td>Sandra Sun</td></tr><tr><td></td><td>Bangkok Chain Hospital</td><td>BKKFF</td><td>BCH TB</td><td>Teerapol Udomvej, CFA</td></tr><tr><td></td><td>Bangkok Dusit Medical Services</td><td>BDMSF</td><td>BDMS TB</td><td>Teerapol Udomvej, CFA</td></tr><tr><td></td><td>Beijing Tongrentang Co., Limited</td><td>BJTGF</td><td>600085 CH</td><td>David Li</td></tr><tr><td></td><td>BeOne Medicines Ltd</td><td>BEIGF</td><td>6160 HK</td><td>David Li</td></tr><tr><td></td><td>BeOne Medicines Ltd</td><td>ONC</td><td>ONC US</td><td>David Li</td></tr><tr><td></td><td>Bumrungrad Hospital</td><td>BUHHF</td><td>BH TB</td><td>Teerapol Udomvej, CFA</td></tr><tr><td></td><td>Cansino Bio</td><td>CASBF</td><td>6185 HK</td><td>David Li</td></tr><tr><td></td><td>Chularat Hospital Group</td><td>XOCOF</td><td>CHG TB</td><td>Teerapol Udomvej, CFA</td></tr><tr><td></td><td>Cochlear Limited</td><td>CHEOF</td><td>COH AU</td><td>Lyanne Harrison</td></tr><tr><td></td><td>CR Pharmaceutical</td><td>CRPGF</td><td>3320 HK</td><td>David Li</td></tr><tr><td></td><td>Daiichi Sankyo</td><td>DSKYF</td><td>4568 JP</td><td

[中间内容因长度限制已省略]

ons, conclusion, or information contained herein (including any investment recommendations, estimates or price targets) without first obtaining express permission from an authorized officer of BofA.

Materials prepared by BofA Global Research personnel are based on public information. Facts and views presented in this material have not been reviewed by, and may not reflect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.

may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Subject to the quiet period applicable under laws of the various jurisdictions in which we distribute research reports and other legal and BofA policy-related restrictions on the publication of research reports, fundamental equity reports are produced on a regular basis as necessary to keep the investment recommendation current.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.
"""
