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
# Internet/e-Commerce

# Raising Internet capex ests: A look into Internet capex, capacity and monetization

Industry Overview

## AI capex returns remain the top hyperscaler debate

The biggest debate for the Internet hyperscaler stocks remains the return profile on AI capex spend, while biggest concern in 2Q results is that higher capex (and lower FCF ests.) will overshadow strong revs. In our view, this concern has outweighed recent positive cloud pricing (Amazon) and capacity monetization data points. In this report, we raise our capex estimates, translate capex into estimated data center GW capacity, and review monetization estimates on that capacity. We also conduct an internet hyperscaler valuation analysis & list potential catalysts that could improve hyperscaler sentiment.

## Raising capex estimates as hyperscalers prioritize capacity

Given the recent capital raise by Alphabet, reported server order increases by Amazon, LLM capacity use comments from Meta, and higher memory costs, we are raising our sector capex estimates. For Alphabet, we now expect Capex of \$195bn in 2026 (vs \$187bn previously), \$290bn in 2027 (vs \$257bn). For Meta, we expect Capex of \$145bn in 2026 (vs \$130bn previously) and \$185bn in 2027 (vs \$157bn). For Amazon AWS (excludes retail), we expect Capex of \$159bn in 2026 (unchanged), \$230bn in 2027 (vs \$196bn). (We will adjust our ests for related revenues & depreciation as additional June advertising and Cloud data points come in.)

## Sizing hyperscaler data center GW capacity through 2030

We est. capacity by triangulating capex results and outlooks, Amazon's GW disclosures, and industry estimates on costs to build data center capacity. We estimate the Big-3 Internet mega caps had \~27GW capacity exiting 2025, which will grow to 39GW in 2026 and 57GW in 2027. We estimate Amazon will add the most capacity in 2026-2027 at 15GW, followed by Google at 9GW and Meta at \~6GW, with Amazon's capacity additions at a lower cost than peers (at around \$24bn in AWS capex per GW per 2025 disclosures).

## Recent capacity deals suggest growing capacity value

Assuming 70% of Amazon's AWS capacity is used for Cloud (vs 30% for core), we estimate AWS revenue per GW of capacity at \$10.6bn in 2026, with Google Cloud at \$15.7bn. These revenues/GW are well below recent capacity deals by Anthropic and Google with SpaceX at up to \$50bn per GW (for specialized AI capacity), which give us optimism on future capacity related revenue upside. For Meta, we estimate the company could have up to \~23GW of capacity by 2030, and if 40% is available for AI enterprise sales, we estimate a \$110bn potential enterprise opportunity (assuming \$12bn/GW).

## Internet hyperscaler valuation analysis

For our valuation analysis, we back out est. valuations for core advertising and retail revenues (at 12-15x implied P/Es) and look at valuations imbedded in hyperscaler stocks per unit of GW capacity. While our analysis is subject to numerous assumptions & excludes the impact of projects like Leo and Reality Labs., we think our analysis identifies the limited implied value the Street is giving to Meta's capacity build. Our analysis suggests an implied value for Google at \$110bn per 2028 Cloud GW (assuming 70% of capacity for Cloud), Amazon at \$59bn per AWS GW, and Meta at \$4bn per AI GW. We note that Meta is the major beneficiary with proof points on capacity revenue levers. See our other conclusions on the next page.

## 07 July 2026

Equity
United States

Justin Post
Research Analyst
BofAS
+1 415 676 3547
justin.post@bofa.com

## Nitin Bansal, CFA

Research Analyst

BofAS

+1 415 676 3551

nbansal7@bofa.com

AI: Artificial Intelligence

FCF: Free Cash Flow

GW: Gigawatt

API: Application Programming Interface

MTIA: Meta Training and Inference Accelerator

TAM: Total Addressable Market

LLM: Large Language Model

## Introduction

We think the biggest debate for the Internet hyperscaler stocks, in our view, remains the return profile on AI capex spend. The elevated capex spend has increased hyperscalers fixed costs, lowered competitive differentiation and increased long-term margin risk. While risk of incremental near-term FCF pressure is increasing, there have been recent positive cloud pricing (Amazon), capacity leasing (Anthropic deal with SpaceX) and LLM data points (Meta improvements with Watermelon) that suggest strong monetization potential. However, despite strong and accelerating Cloud sector revenue growth, Amazon and Meta P/E valuations are well below historical averages, and Google has underperformed since announcing a capital raise on June 3 $^{rd}$ , suggesting investors remain skeptical on AI capex spend ROIs.

In this report, we update our capex estimates, translate capex into implied installed GW data center capacity, and estimate the potential monetization value of that capacity through a revenue-per-GW analysis. We also analyze for Internet hyperscaler capacity, and potential catalysts that could drive stock multiple expansion.

Our key conclusions:

\- Amazon will add most capacity in 2026-2027 and therefore has potential for most capacity driven incremental revenue growth in the group. We estimate Amazon will add 15GW of capacity over the 2-year period, followed by Google at 9GW and Meta at \~6GW. Reiterate Buy on Amazon.

We estimate that Amazon will have the lowest cost per incremental GW of capacity. We estimate Amazon capacity additions at \$25bn/GW in 2026 vs Google at \$37bn/GW and Meta at \$45bn/GW, which reflects AWS's scale advantage, use of internal chips, and more balanced mix of core cloud workloads (vs AI). Higher costs at Google and Meta in 2026 partially reflect additional upfront facilities spend (vs chips), more specialized AI capacity (GPUs vs CPUs).

\- Google has higher revenue per GW of estimated AI / Cloud capacity, which is due to its premium cloud mix and differentiated AI infrastructure anchored by TPUs. However, with estimated 2026 AWS revenue per AWS GW at roughly \$10bn versus Alphabet Cloud at \$16bn, there is potential upside to our AWS revenue estimates as AI workloads grow as a percent of total.

\- There is significant upside potential to our Cloud revenue estimates based on recent capacity deals. We estimate annual Cloud revenues per GW of capacity for Amazon and Google ranging from \$10bn to \$17bn, well below recent capacity deals signed by Anthropic and Google with SpaceX at over \$40bn a GW (estimated). We also use a conservative \$12bn per GW in estimating Meta's enterprise revenue potential, which could have significant upside considering specialized AI capacity that Meta is building.

\- Meta is getting little to negative value on its capacity build. Even using a conservative 5x 2027 revenues on Meta's ads business (which translates to around 12x P/E assuming $50\%$ margins) and assuming a relatively high $60\%$ of capacity will be used for the core ad business, Meta's stock valuation embeds a $\$4bn/GW$ AI capacity valuation based on our capacity estimates. Reiterate Buy on Meta.

## Section 1: Raising Capex Estimates

Given the recent capital raises by Alphabet and Amazon, combined with a DigiTimes report that AWS has asked server supply chain partners to increase 3Q26 shipments, comments from Meta's management on increase capacity needs for its new LLM (Watermelon), Google's commentary emphasizing a significant step-up in capex next year, and DRAM spot pricing data that suggests pricing is up $40\%$ q/q, we are raising our capex estimates. We believe hyperscalers will prioritize capacity availability over near-term FCF optimization, as demand for AI training, inference, cloud workloads and internal AI product deployment remains supply constrained. Recent commentary supporting our outlook for higher capex:

\- In June Google indicated plans to raise \$80 in capital to fund infrastructure investment,

In early July, Meta said its next-gen AI model 'Watermelon' uses 10x more compute,

In early July, Amazon Web Services has told its server supply chain partners to raise shipment volumes for 3Q'26 (per Digitimes), and

In mid-June, per Bloomberg, Meta signed a 1.6GW capacity agreement with neo cloud provider, Crusoe

Exhibit 1: We are raising our capex estimates to reflect recent Cloud industry data points. Updated Capex Estimates for Alphabet, Meta and Amazon AWS (\$ bn)  
![](images/9a58f6ef346bd5b2110f0a2dcde8c43f482613556ef3bd63e123d95f9e35bf73.jpg)  
Source: BofA Global Research Estimates  
BofA GLOBAL RESEARCH

## Revised estimates:

\- Alphabet: We now expect Capex of \$195bn in 2026 (vs \$187bn previously), growing 49% y/y to \$290bn in 2027 (vs \$257bn previously) and 14% y/y in 2028 to \$330bn (vs \$310bn previously).

■ Meta: We now expect Capex of \$145bn in 2026 (vs \$130bn previously), growing 28% y/y to \$185bn in 2027 (vs \$157bn previously) and 14% y/y in 2028 to \$210bn (vs \$171bn previously).

\- Amazon AWS: We expect Capex of \$159bn in 2026 (unchanged), growing 44% y/y to \$230bn in 2027 (vs \$196bn previously) and 20% y/y in 2028 to \$276bn (vs \$221bn previously).

Note: Our updated Alphabet, Amazon and Meta models just reflect revisions to our capex estimates only. We will incorporate the associated impact on depreciation, EPS, FCF and other financial metrics as we receive June revenue data points.

## Section 2: Estimating installed GW Capacity

Using our capex estimates, we estimate historical and future installed GW data center capacity for Alphabet, Meta and Amazon AWS. Our analysis uses company-level capex as the starting point, then applies an estimated cost to build and equip AI-oriented data center capacity. While the exercise is high-level given limited company-level disclosures, we believe it helps in sizing the scale of hyperscaler infrastructure deployment and the potential monetizable compute base. Our key assumptions include:

## Cost to Build a GW of Capacity

We estimate that in 2026, the cost to build 1GW of data center capacity is \$25bn to \$45bn, inclusive of the major infrastructure and compute components. The range reflects differences in accelerator mix, rack density, power redundancy, cooling architecture, land and construction costs, and whether the capacity is optimized for training, inference or mixed workloads. We think capex cost per GW could be elevated for Meta and Google in 2026 as land and construction costs are elevated ahead of chip deployment, and capacity is more specialized for AI workloads than various Cloud competitors. Future offsets could include improving chip performance, use of proprietary chips, and rapid growth in memory and other supply availability.

Using data from multiple secondary sources, we estimate that the largest component of AI data center build cost is AI servers and GPUs, which account for roughly 55% to 60% of total cost. This reflects the high cost of accelerators, server systems and related compute hardware required to support training and inference workloads. Power infrastructure is the next largest cost category at approximately 12% to 18%, including substations, transformers, switchgear, backup generation and power distribution equipment needed to support dense AI workloads. Networking represents another 8% to 12% of total cost, driven by high-performance interconnects, switches and optical networking required to link large GPU or TPU clusters. Beyond compute and power, we estimate building, land and site work account for roughly 8% to 12% of total cost, including land acquisition, shell construction, site preparation and related civil work. Cooling and mechanical systems represent approximately 6% to 10%, and other costs and contingency account for \~3% to 5%.

Exhibit 2: We estimate \$25bn to \$45bn to build 1GW of AI data center capacity
Cost Build-up of 1GW Capacity Data center (\$ bn)

<table><tr><td>Capex bucket</td><td>Approx. % of total</td><td>Lower ($ bn)</td><td>Higher ($ bn)</td><td>What it includes</td></tr><tr><td>AI servers / GPUs</td><td>55%-60%</td><td>$14</td><td>$28</td><td>GPU servers, CPUs, memory, storage inside servers</td></tr><tr><td>Networking</td><td>8%-12%</td><td>$2</td><td>$5</td><td>Switches, optical modules, NICs, cables, back-end GPU networking</td></tr><tr><td>Power infrastructure</td><td>12%-18%</td><td>$3</td><td>$8</td><td>Substations, transformers, switchgear, UPS, PDUs, backup generation</td></tr><tr><td>Cooling / mechanical systems</td><td>6%-10%</td><td>$2</td><td>$5</td><td>Liquid cooling, chillers, cooling distribution, heat rejection</td></tr><tr><td>Building / land / site work</td><td>8%-12%</td><td>$2</td><td>$5</td><td>Land, shell, security, physical construction, permitting</td></tr><tr><td>Other / contingency</td><td>3%-5%</td><td>$1</td><td>$2</td><td>Design, engineering, commissioning, spares, buffers</td></tr><tr><td>Total</td><td>100%</td><td>$25</td><td>$45</td><td>1GW AI data center</td></tr></table>

Source: BofA Global Research Estimates, Epoch AI, JLL

BofA GLOBAL RESEARCH

Company specific assumptions: Google and Amazon custom silicon Advantage
For company-specific assumptions, we use a 2026 cost per GW of \~\$45bn for Meta, \$37bn for Alphabet and \$25bn Amazon. For Amazon, we can triangulate cost per GW based on Amazon's capex and 2-year GW capacity growth outlook. The higher Meta assumption reflects greater upfront costs for data center land/building (ahead of GPU deployment) and reliance on external GPU infrastructure. For Alphabet and Amazon, we assume lower cost per GW to reflect custom silicon usage, particularly the ability to use internally developed TPUs and Trainium/Graviton chips, which we believe can lower effective compute cost versus a more GPU-heavy architecture.

## Alphabet Installed Capacity Estimates

We estimate Alphabet had 5.5W of capacity in 2025, which will increase $62\%$ y/y to 8.9GW in 2026 and $66\%$ y/y to 14.7GW in 2027. By 2030, we project Alphabet's installed capacity to reach 32.4GW.

Exhibit 3: We estimate Alphabet capacity will grow to 15GW by 2027 Estimated Alphabet Installed Data Center Capacity (GW)  
![](images/c7c50f7ca722ae65d7c445e689aa305d39b371dd18b3af898e3cfc46f5f157e1.jpg)  
Source: BofA Global Research Estimates  
BofA GLOBAL RESEARCH

We est. Alphabet's capex of \$195bn in 2026 and \$290bn in 2027. Assuming share of capex directed towards Cloud business and AI data centers increases from 45% in 2024, to 60% in 2025 and 70% by 2030 and avg. cost to add 1GW of capacity increases from \~\$31bn in 2024 to \~\$46bn by 2030, we estimate Alphabet's capacity will increase from \~8.9GW in 2026 to 32.4GW by 2030. The increase in cost per GW in 2026, followed by a decline in 2027, reflects timing dynamics in the capacity buildout (physical infrastructure before chips are deployed). We expect revenue per GW to fall in 2027 to reflect timing of capacity deployment, and then increase again in 2028.

Exhibit 4: We estimate Alphabet's capacity will increase from \~8.9GW in 2026 to \~32.4GW by 2030
Alphabet's Capex and Commissioned capacity estimates by year

<table><tr><td></td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td></tr><tr><td>Existing Capacity</td><td>3.0</td><td>3.8</td><td>5.5</td><td>8.9</td><td>14.7</td><td>20.7</td><td>26.6</td></tr><tr><td>GW Addition</td><td>0.8</td><td>1.7</td><td>3.4</td><td>5.8</td><td>6.0</td><td>5.9</td><td>5.8</td></tr><tr><td>Total Capacity</td><td>3.8</td><td>5.5</td><td>8.9</td><td>14.7</td><td>20.7</td><td>26.6</td><td>32.4</td></tr><tr><td>Alphabet Capex ($ bn)</td><td>$52.5</td><td>$91.4</td><td>$195.0</td><td>$290.0</td><td>$330.0</td><td>$356.4</td><td>$384.9</td></tr><tr><td>Y/Y</td><td>63%</td><td>74%</td><td>113%</td><td>49%</td><td>14%</td><td>8%</td><td>8%</td></tr><tr><td>% for Cloud</td><td>45%</td><td>60%</td><td>64%</td><td>70%</td><td>70%</td><td>70%</td><td>70%</td></tr><tr><td>Google Cloud Capex ($ bn)</td><td>$23.6</td><td>$54.9</td><td>$124.8</td><td>$203.0</td><td>$231.0</td><td>$249.5</td><td>$269.4</td></tr><tr><td>Y/Y</td><td>109%</td><td>132%</td><td>127%</td><td>63%</td><td>14%</td><td>8%</td><td>8%</td></tr><tr><td>Cost per GW Added</td><td>$31.0</td><td>$31.9</td><td>$36.7</td><td>$34.9</td><td>$38.4</td><td>$42.2</td><td>$46.4</td></tr><tr><td>Y/Y</td><td></td><td>3%</td><td>15%</td><td>-5%</td><td>10%</td><td>10%</td><td>10%</td></tr><tr><td>Google Cloud Revenues (BofA Estimates)</td><td>$43</td><td>$59</td><td>$97</td><td>$156</td><td>$238</td><td>$309</td><td>$387</td></tr><tr><td>Y/Y</td><td>31%</td><td>36%</td><td>66%</td><td>61%</td><td>52%</td><td>30%</td><td>25%</td></tr><tr><td>Street Estimates</td><td></td><td></td><td>$97</td><td>$149</td><td>$210</td><td>$273</td><td>$344</td></tr><tr><td>% Difference (BofA vs Street)</td><td></td><td></td><td>0.5%</td><td>5.2%</td><td>13.2%</td><td>13.5%</td><td>12.4%</td></tr><tr><td>Incremental Y/Y Revenue</td><td>$10.1</td><td>$15.5</td><td>$38.7</td><td>$59.0</td><td>$81.5</td><td>$71.4</td><td>$77.3</td></tr><tr><td>Incremental Rev per GW Added</td><td>$13.3</td><td>$9.0</td><td>$11.4</td><td>$10.1</td><td>$13.5</td><td>$12.1</td><td>$13.3</td></tr><tr><td>Y/Y</td><td>-27%</td><td>-32%</td><td>26%</td><td>-11%</td><td>34%</td><td>-11%</td><td>10%</td></tr></table>

Source: BofA Global Research Estimates  
BofA GLOBAL RESEARCH

## Amazon Installed Capacity Estimates

We estimate Amazon had 16.2GW of installed capacity in 2025, which will increase 40% y/y to 22.6GW in 2026 and 38% y/y to 31.3GW in 2027. By 2030, we project Amazon's installed capacity to reach 58.1GW.

Exhibit 5: We estimate Amazon AWS capacity will increase to 31GW by 2027
Estimated Amazon Installed Data Center Capacity (GW)  
![](images/7dc44cc5afa2fcfa03c161fdc776637cdb7e216d7b35140aacb56b6d273f1e82.jpg)  
Source: BofA Global Research Estimates  
BofA GLOBAL RESEARCH

We estimate AWS capex of \$159bn in 2026 and \$230bn in 2027. Assuming share of capex directed towards data centers at 100% and average cost to add 1GW of new capacity increases from \~\$23bn in 2024 to \~\$36bn by 2030 (as capacity becomes more weighted toward AI), we estimate Amazon's capacity will increase from \~22.6GW in 2026 to \~58.1GW by 2030.

Exhibit 6: We estimate Amazon's AI data center capacity will increase from \~22.6GW in 2026 to \~58.1GW by 2030 Amazon Capex and Commissioned capacity estimates by year

<table><tr><td></td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td></tr><tr><td>Existing Capacity</td><td>10.0</td><td>12.3</td><td>16.2</td><td>22.6</td><td>31.3</td><td>40.5</td><td>49.5</td></tr><tr><td>GW Addition</td><td>2.3</td><td>3.9</td><td>

[中间内容因长度限制已省略]

ons, conclusion, or information contained herein (including any investment recommendations, estimates or price targets) without first obtaining express permission from an authorized officer of BofA.

Materials prepared by BofA Global Research personnel are based on public information. Facts and views presented in this material have not been reviewed by, and may not reflect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content

contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Subject to the quiet period applicable under laws of the various jurisdictions in which we distribute research reports and other legal and BofA policy-related restrictions on the publication of research reports, fundamental equity reports are produced on a regular basis as necessary to keep the investment recommendation current.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
