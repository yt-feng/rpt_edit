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
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`麦肯锡`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份麦肯锡研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
![](images/34ed8684c0531acedaa8f3ec637c5227a202d2e83c103c1477202d35abfa8dff.jpg)

# Global Banking Annual Review 2026

Precision with speed

In this preview of our 2026 Global Banking Annual Review, we provide a glimpse of banks' continued strong results in 2025; the emergence of a new world map; the tipping point for customer ownership; and the unprecedented pace at which AI is remaking the industry, prompting banks to accelerate their precision strategies and evolve into multispeed organizations.

This report is a collaborative effort by Klaus Dallerup, Miklós Dietz, Pradip Patiath, and Vik Sohoni, with Valeria Laszlo, representing views from McKinsey's Financial Services Practice.

In 2025, the global banking industry outdid itself—again. Net income rose to \$1.3 trillion, up 7 percent from 2024's record-setting tally. Once again, banking recorded the most net income of any industry. $^{1}$ As rates began to fall in major markets, net interest margins (NIM) declined slightly, globally from 1.65 percent in 2024 to 1.63 percent in 2025. However, some markets improved their margins. US banks' NIM rose 9 basis points (bps), Japan's banks (7 bps), and UK banks (6 bps). Emerging markets were not quite as fortunate, as margins slipped slightly, and in Brazil, dramatically (from 3.55 percent to 2.93 percent.) Balances (deposits, loans, and assets under management) grew by 6.5 percent in 2025, up from 6.2 percent annually in 2020–24. Investors benefited from higher dividends and share buybacks; and banks socked away another \$853 billion in surplus free cash flow to equity, which, while somewhat lower than previous years, continued the record-setting trend begun in 2022.

It's a remarkable picture of a flourishing industry. But look elsewhere and some signals are flashing yellow. Banking's price-to-book (P/B) and price-to-equity (P/E) ratios have lagged behind other industries for many years. And even after all the success of 2024–25, the gap has closed only slightly, and banking continues to have the lowest P/B and P/E of any industry. It seems that investors are likely delighted with recent results but are not buying in to a long-term vision of continued growth and profit. Return on tangible equity has started to decrease again (from 12.4 in 2024 to 11.8 in 2025). Memories are long; last year's peak in ROTE is a shadow of the truly great years for banks, 2003–07, when the industry touched 20 percent. And few have forgotten the dark years of the global financial crisis (and the increase in regulatory capital requirements, which reset expectations for return on equity) leading to the lost decade of 2012–2021, when the industry did not create real shareholder value. Investors may be questioning whether banks have used their recent success to reset the business for long-term value creation.

Geopolitical dynamics have been making the headlines recently, and for the most part, banks have adapted well. Investment banks have done exceptionally well from volatility in 2025 and 2026. The new frictions are far from settled, of course, and doubtless will require even more agility from banks. Meantime, the industry also faces four rising challenges to its most vital asset: the customer relationship. Fintechs (including neobanks, like Revolut and Nubank) were mostly an irritant to incumbents for the past 20 years—until 2025, when irritation became something more acute. A new breed of mature fintechs has, by one measure, claimed 17 percent of industry revenues and is looking for more. Neobanks pose a second challenge. “The call is coming from inside the house” is a trope of many horror films, and banking is experiencing a version of it. Neobanks such as Revolut and Nubank have broken through the growth/performance frontier and rewritten the expectations of incumbent institutions. Agentic AI and digital assets, such as stablecoins, are a two-headed technological revolution that make it easier for retail and corporate customers to bank without banks. Finally, customers’ attitudes are reaching a tipping point; they now not only favor but also trust more the new entrants delivering everyday reliable services.

Banks have seen off many threats in the past, most often by waiting them out. While the rise of the internet and the smartphone upended other consumer industries, banks chose to adopt the technologies much slower than others. They enjoyed a singular advantage: They derived most of their revenues and profits from older customers, who could be counted on to move at the same pace. That advantage won't work this time: AI adoption is the fastest in history, and young and old people are piling in at nearly the same rate.

In last year's report, we outlined the precision strategies that could help banks get past the macro-focused, scale-driven, broad-brush approaches that had run out of steam. Precision strategies are still the order of the day, with a twist: Banks must develop a new and increased velocity of execution, to match the speed of AI development. The brutal pace is a new and defining challenge for bank leaders who have likely never experienced anything like it before.

In this preview of our October 2026 report, we begin by reviewing 2025 performance and the new alignments of business models around the world. We then consider the four developments that threaten to wrest control of the customer away from banks. We conclude with considerations of why banks have less time to act than they are used to and outline the newly accelerated strategies that banks can use to remain relevant to customers and investors in coming years.

## State of the industry: Strong economics and new alignments

In 2025, global banking continued to grow; margins remained elevated and were little changed. Less positively, the share of global funds parked on banks' balance sheets is shrinking, reflecting big changes in how banks earn revenues and profits.

The most salient macro development in 2025 was the sharper prominence of diverse regional models. Simply put, banks in some parts of the world do business differently from their peers—and their results reflect that. While regionalism has always been strong, recent changes are lifting this regionalism to something new. Combined with the emergence of new, scalable technologies, this trend is creating tailwinds for a new model of banking expansion.

## Steady growth and continued strong margins

Banking revenues are closely linked to wealth accumulation, and wealth has long been growing faster than GDP (Exhibit 1). From 2020 to 2025, funds intermediated by the financial system

## Exhibit 1

Financial assets are mounting quickly; wealth accumulation is outpacing the real economy.

Intermediated funds in global financial system, 2020–25

Share of intermediated funds, \$ trillion

![](images/44e6edd0650efa30857866c47f2448d3ee7bfe37b22f0794530e43227cf2c535.jpg)

![](images/c34173c5c8043352826d9c85e3073dbb82ddbeb1c976ba18dd33985c2eb6ae4c.jpg)  
Note: Figures may not sum to 100%, because of rounding.  
$^{1}$ Includes sovereign wealth funds, public pension funds, and other alternatives (eg, hedge funds, real estate funds). $^{2}$ Includes private capital and private debt. $^{3}$ Includes banks' bonds and other equity; corporate deposits, corporate investments. $^{4}$ Includes retail deposits, insurance and pension assets under management (AUM), and securities and derivative, mutual funds AUM held by households. $^{5}$ Includes corporate deposit and retail and institutional asset management. $^{6}$ Includes retail deposits, pensions, insurance, retail investments, and household cash.

Source: S&P Capital IQ; McKinsey Panorama—Global Banking Pools

McKinsey & Company

(including banks and others) expanded by \$131 trillion, reaching \$468 trillion in 2025. While all categories grew faster than nominal GDP, private capital's share took flight, growing 14.1 percent annually. Still, private capital is a small slice of the system, and retail banking remains by far the most important home of accumulated wealth worldwide.

As more capital flowed through the system, banking revenues and profits rose. Balances held by banks (deposits, loans, and assets under management) rose from \$381 trillion in 2024 to \$406 trillion in 2025. Revenues before risk costs rose from \$6.1 trillion in 2024 to \$6.4 trillion in 2025. Profits spiked 7 percent year-on-year, to \$1.3 trillion.

Margins remained consistent. By our measure, $^{2}$ revenue margins declined slightly from 0.97 in 2024 to 0.94 in 2025 (Exhibit 2). Costs also improved, dropping from 1.31 percent of assets in 2024 to 1.23 percent in 2025. While both stories are positive, it remains the case that revenue margins are still well below the highs achieved in the early 2000s.

## Exhibit 2

Margins are declining, which could pressure banks to further reduce costs.

Global revenue margins $^{1}$ and cost/assets

![](images/26366690f665ad2914c61ea3ddb72f2230c62c52bbee00fce923873b4827a365.jpg)  
$^{1}$ Revenue = revenue after risk cost; balances include deposits, loans, and assets under management balances. Source: S&P Global; McKinsey Panorama—Global Banking Pools

![](images/74f2c2ab47c0c97ab4564323205e576bed7ec08295de7fd08bb183427319d1bb.jpg)

## McKinsey & Company

Viewed another way, banks' economics are changing, and not necessarily for the better. The global financial system now holds \$468 trillion. Since 2022, the portion of on-balance sheet has shrunk, from 44 percent in 2022 to 40 percent in 2025. This reveals a shift in the way banks earn their keep. As the balance sheet becomes less important, revenues and profits from transaction banking and distribution have leapt in prominence. We estimate that those two categories now account for 47 percent of revenues and 57 percent of profits. The balance sheet remains vital, of course, but accounts for 53 percent of revenues and 43 percent of profits. These areas have far more competition and faster disruption from new business models.

## New landscape, new macro strategy

As shifting geopolitical dynamics have roiled the world, McKinsey research has documented some of the biggest changes in the global economy: the new composition of trade, the great trade rearrangement and its effects on business, and the implications for manufacturing footprints, among others.

In all this, where is banking? One way to answer this is to follow the money. A critical feature in the world's growing wealth has been faster growth in the United States, which has long been the world's wealthiest. Canadian wealth also expanded sharply. From this large base, North American intermediated funds grew 8 percent from 2022 to 2025, largely because of dramatic inflows to US asset managers. European wealth grew at half that rate. Latin America is something of a puzzle: Growth there was fast, but slower than GDP growth. (We discuss these and other regional variations below.)

A proportionally larger share of flows into North America, despite a lower gross savings rate (18 percent in the United States versus 25 percent in the European Union) $^{3}$ is made possible, of course, by investors' trust in the relative stability of the US financial system compared with its peers. Policy changes and a growing national deficit are denting that confidence. But it remains intact for now, even amid regulatory flux around AI and the potential for further consolidation. The United States remains a favored destination for wealth.

A greater share of wealth management revenues benefited the US banking industry (and other financial institutions), lifting ROEs to 12 percent. European banks also improved, from 10.7 percent in 2024 to 11.6 percent in 2025—but this was mainly the result of operational performance improvement. Western European banks' share prices recovered sharply in 2025, after years in the doldrums. Total shareholder returns surged 62.9 bps in 2025.

But divergence in performance has deeper roots. We analyzed banks worldwide by the degree to which they have shucked off the balance sheet and moved into fee-based services, and by their efficiency, which we call disintermediation (Exhibit 3). We're seeing an alignment by business model that reflects traditional regional affinities but also see banks in some countries behaving most like peers thousands of miles away, pointing toward the emergence of a new world map of banking.

The new world ‘map’ of banking reveals fundamentally different business models in different regions.

Different business models, by region, 2026  
![](images/e73b35fa883a5ed0a7993f2c0a9ad375336d038ca840a4b19e01a4d5ec9433e7.jpg)  
$^{1}$ Off-balance sheet volumes (retail investments assets under management [AUM]) + insurance and pension AUM + institutional AUM) divided by total volumes (on-balance + off-balance: corporate and retail deposits + retail investments AUM + insurance and pension AUM + institutional AUM). $^{2}$ Operating expense as a share of average assets.  
Source: S&P Capital IQ; McKinsey Panorama—Global Banking Pools

McKinsey & Company

The North American financial system has historically been more disintermediated than others, a result of efficient capital markets and banks' preference for corporate bonds rather than loans on their balance sheets. Gulf Cooperation Council banks are among the most reliant on the balance sheet, but they counter that with strong cost efficiency. Northwest Europe, Australia, and New Zealand banks, which nearly match US peers on independence from the balance sheet, are broadly more efficient. Sweden and Finland represent the best of both worlds, showing a potential way forward for a highly robust and low-transaction-cost intermediary system for the rest of the world. In other parts of Europe, banks rely more on the balance sheet, and costs are broadly higher.

What accounts for the stark differences among regions and the business models each has developed? Exhibits 4 and 5 lay out the key distinctions, and the sidebar “Regional models” explains the dynamics.

## Exhibit 4

Six regional models are marked by differences in levels of disintermediation and wealth.

Key metrics for six banking groups, 2025

<table><tr><td></td><td>North America</td><td>Western Europe, Australia, and New Zealand</td><td>East Asia and Pacific</td><td>Latin America</td><td>Gulf Cooperation Council</td><td>Southeast Europe, South Asia, and Africa</td></tr><tr><td>Share of disintermediation</td><td>64%</td><td>49%</td><td>38%</td><td>40%</td><td>16%</td><td>26%</td></tr><tr><td>Total wealth as a share of nominal GDP</td><td>599%</td><td>422%</td><td>443%</td><td>140%</td><td>144%</td><td>160%</td></tr><tr><td>Cost-to-asset ratio</td><td>2.1%</td><td>1.2%</td><td>0.7%</td><td>3.3%</td><td>0.9%</td><td>1.8%</td></tr><tr><td>Price to book</td><td>1.4×</td><td>1.2×</td><td>0.7×</td><td>1.5×</td><td>1.3×</td><td>1.4×</td></tr><tr><td>Change in total financial assets 2022–25, $ trillion</td><td>32.3</td><td>12.8</td><td>23.8</td><td>3.1</td><td>3.0</td><td>13.9</td></tr><tr><td>Asset growth compared to GDP growth 2022–25</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

McKinsey & Company

Within these regions, the structure of revenue pools shows clear tendencies.  
![](images/e6ed3ca0e756e7315437ffb4eda2d14ff4061860a480fde6249aebfe654d95f4.jpg)  
Note: Figures may not sum to 100%, because of rounding.  
$^{1}$ Includes large corporates and small and medium enterprises.  
$^{2}$ Includes nonbanking financial institutions and public.  
Source: S&P Capital IQ; McKinsey Panorama—Global Banking Pools  
$^{3}$ Wealth and asset management.

## McKinsey & Company

## Sidebar

## Regional models

In the following, we highlight some of the hallmarks of business models in the six groups.

In North America, highly advanced capital markets drive most disintermediation. Older demographics account for a relatively higher share of revenues and have also led to a slower pace of digitization. Banks rely on a higher share of traditional wealth management revenues. The underbanked population is higher than in other regions. Credit cards play a disproportionate role versus lower-rate bank loans.

In Western Europe, Australia, and New Zealand, more wholesale funding is done on–balance sheet. These regions typically have a more balanced distribution of retail revenues across demographics. Markets in general are more competitive and operate at lower margins. Unsecured lending is

heavily biased toward low-interest-rate products.

In East Asia and Pacific, corporate funding is very heavily on–balance sheet, frequently provided by large state-owned or industry-linked banks. Consumers are strong savers but less active investors, with a large share of wealth held in deposits and real estate. Digitization rates are high. “Superapps” and nonbanks are disrupting markets.

Latin America displays different savings and consumption patterns from other regions. A large unbanked and underbanked population is raising demand for consumer credit, payments, and microfinance, supported by regulatory pushes for inclusion. Neobanks are expanding quickly by targeting underbanked populations with low-cost, mobile-first offerings.

In Gulf Coast Council countries, more revenues stem from corporate lending than in other regions. For most banks in this region, the Islamic banking value proposition has

grown quickly due to high adoption in the lower- and middle-income segments, further supported by the introduction of consumer-friendly products (such as home finance). Loan-to-deposit ratios grew significantly over the past five-plus years (from 87 percent in 2019 to 109 percent in 2025), though growth is expected to slow. Digitization is strong in everyday banking, as seen in the emergence of large ecosystem players (such as WIO Bank PJSC, the United Arab Emirates' first platform bank; and STC Bank's telco-anchored digital financial platform), but less developed in wealth management and other businesses.

Banks in Southeast Europe, South Asia, and Africa have the potential to leapfrog other regions by building digital and AI infrastructure from scratch. It's an opportunity to develop highly innovative, next-generation banking models. Low-cost structures enable more transaction-oriented banking models.

This geographic divergence of business models helps explain why global banking did not fully take hold. As the banking model has standardized, or nearly so, within each group, the global universal bank has evolved. Over the past decade, major institutions such as HSBC (reduced its presence in several markets) and Citi (selling its consumer businesses in 13 Asian and European, Middle Eastern, and 

[中间内容因长度限制已省略]

obal banks and fintechs, 2016–25 $^{1}$  
![](images/d213887a69e4aff7e76e33014e381eb438176fe739bc15fee90b06afd0c9d1a8.jpg)  
AI and digital assets are heavily skewed toward the highest-risk segment, combining high momentum with low penetration and limited track record. As the hottest yet least understood themes, they require a differentiated approach.  
With \~70% of ideas concentrated in high-popularity areas, banks must fundamentally rethink their innovation posture—shifting toward faster cycles, differentiated risk management, and scalable experimentation.

![](images/06182c070d3a7d20c3f82fd361b116763aa471744e0ffd81d5b8405b0d60c290.jpg)

![](images/0e54dcd23847ff45df3b89734ff681b06ba28d07ea7cd4e50f71e7f9909d24d0.jpg)

![](images/a7b29cebe595473f9a45b206fbe1d3a653e3c816c6d04ed98be9e7c6fcb8344a.jpg)

![](images/f4534564e1718b510849a3f4a421056600907f3347f05d29ae4d53eb63f52029.jpg)

![](images/6c7f7aa1a15a6728fd3bff958a7338d035048956c3ee39d4179060e1dda0a347.jpg)

![](images/bd454fa73e8678bf253d0f73b3dff5d97b32d7d62af957bff39876cb67c37616.jpg)  
$^{1}$ The analysis identifies 3,458 distinct ideas (value propositions) by clustering \~300,000 real-world products, services, and innovations launched by banks and fintechs globally. Each idea cluster groups multiple real-world examples of similar offerings (eg, "green mortgage" cluster/idea includes actual products from various banks/fintechs globally).  
$^{2}$ Change in idea launch frequency compared with average over the past 10 years (ie, increasing popularity means that the idea is being launched more often than the average idea).  
Source: McKinsey Panorama—Idea Analytics  
$^{3}$ Share of idea launched by sample set of 10,000 of the largest banks and fintechs globally.

## McKinsey & Company

Banks should adopt a three-speed organizational approach, matching the innovation type with the right organizational setup.

Technology, innovation, and development, by operating speed

![](images/e0ce4f6f49f692c3993868838f3a043c9ebe08ce2e1b98209a370ebd9294e8fa.jpg)

We do not suggest that banks need to operate fully at the speed of technology businesses. Banks are subject to different regulations and must carefully manage a broader range of risks. We do suggest, however, that banks can accelerate their baseline, business-as-usual speed to move faster while continuing to observe their current risk and compliance obligations. They can move even faster to incubate new noncore technologies and letting the laggards fail fast. And they can go even faster—at true tech speed—to seed “sandbox” innovation outside the regulatory moat around core production. Some banks already have a three-speed setup, but even these banks could stand to clarify their roles, incentives, and governance to increase the intensity of innovation output.

Operating at higher speed also requires a cultural shift, beyond adjusting the organizational setup. It brings higher failure rates, greater uncertainty, and new performance expectations. Banks must adapt incentives, risk tolerance, and leadership expectations accordingly, something they can emulate from inspirational examples in other sectors.

Done well, banks will be able to layer always-elusive agility onto their traditional stability and achieve the required pace to stay relevant amid technology shifts and the war for customer primacy.

Building the multispeed bank won't be easy, but this is a historic opportunity—even for the most traditional banks and smaller players. While banks were slow in digital and paid a price, AI is hurtling forward and taking no prisoners. Both AI and digital assets offer the opportunity to leapfrog the competition, to not just protect current revenue pools but also attack broader ecosystems, truly rewarding those that master velocity.

## More about McKinsey Panorama and Banking Pools

McKinsey Panorama equips financial institutions with data and insights to help them define strategies and accelerate innovation. Panorama offers granular intelligence on banking market sizing, customer segmentation, and innovations through a model designed around client needs. Panorama's core offerings include Banking Pools and Idea Analytics.

Banking Pools, the database underpinning the analysis in this report, provides granular insights into banking value pools across markets, customer segments, and individual players. Covering more than 70 products and segments across 100-plus countries, it allows for consistent, product-level comparisons across geographies, as well as deeper insight into customer behavior and preferences. It also supports tailored diagnostics for banks in specific contexts.

In practice, Banking Pools is used to quantify market size, develop customized projections, and stress test long-term strategies. It can also inform product origination, support decisions on international expansion or retrenchment, and provide a benchmark against market performance to help optimize portfolios.

Klaus Dallerup is a senior partner in McKinsey's Copenhagen office, Miklós Dietz is a senior partner in the Vancouver office, Pradip Patiath is a senior partner in the Miami office, Vik Sohoni is a senior partner in the Chicago office, and Valeria Laszlo is a senior capabilities and insights expert in the Budapest office.

The authors wish to thank Aron Vidman, Carine Zahra, Debopriyo Bhattacharyya, Jay Datesh, Hugo Tong, Istvan Rab, Kriti Suman, Mihael Maljak, Rauhan Nazir, Sherry Ghali, Shikha Gupta, and Zsofia Sveiczer for their contributions to this report.

This report was edited by Mark Staples, an editorial director in the New York office.

![](images/7cb34647a0e08ebfe18bf6231d8451531f90237718d8bc32383074c533eff9fb.jpg)

www.mckinsey.com
"""
