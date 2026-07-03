你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`JPM`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份JPM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Top 10 US Ideas Quarterly

# Introducing the Top 10 US Ideas for Q3 2026

Strategy

## High-conviction Ideas to Drive American Alpha

We present our new list of ten short-term stock recommendations among US stocks under coverage based on our view that these stocks could have significant market and business-related catalysts in the quarter ahead. For 3Q26, our Top 10 Ideas include nine Buys and one Underperform across ten sub-sectors. Our Buys are Ford Motor, IBM, Ionis Pharma, JPM Chase, Knight-Swift, Snowflake, Spotify, Visa Inc, and Walmart. Our Underperform is Lennar Corp.

## Red, White, and Bullish (mostly)

BofA's RIC Outlook points to a largely bullish backdrop for the U.S. economy and global equities, with indicators confirming the “new industrial cycle” remains intact and earnings momentum strengthening. The Global Earnings Revision Ratio has improved to a six-month high, with particularly strong readings in the U.S. and broad-based upgrades across regions, while the Global Wave of macro data is rising in tandem with the earnings cycle—historically a supportive signal for equity returns. Although valuations and positioning suggest markets may be somewhat overheated in the near term, we think any summer pullback could be a potential buying opportunity, especially in real assets, credit, and value-oriented areas. See reports linked in the side bar for more on these themes.

## How this list will be maintained and updated

We will publish this list at the beginning of each quarter. Ideas will generally remain on the list through the quarter unless coverage is dropped or the rating changes. Any security that is removed will not be replaced. If there are changes to the list during the quarter, we will publish the change in a research report. Securities are intended to stay on the list for one quarter, although some may be chosen for the next quarter's list. We will publish performance quarterly.

## Table 1: Top 10 US Ideas List – 3Q26

High-conviction, short-term stock recommendations for the quarter ahead.

<table><tr><td>Company</td><td>Ticker</td><td>Analyst</td><td>Rating</td><td>Rec</td><td>Price</td><td>PO</td><td>Mkt Cap (bn)</td></tr><tr><td>Ford Motor</td><td>F</td><td>Perry,Alexander</td><td>C-1-7</td><td>BUY</td><td>$13.90</td><td>$20.00</td><td>$63,694.68</td></tr><tr><td>Int Business Machine</td><td>IBM</td><td>Mohan,Wamsi</td><td>B-1-7</td><td>BUY</td><td>$281.21</td><td>$315.00</td><td>$267,716.92</td></tr><tr><td>Ionis</td><td>IONS</td><td>Gerberry,Jason</td><td>C-1-9</td><td>BUY</td><td>$79.29</td><td>$111.00</td><td>$12,325.28</td></tr><tr><td>JPM Chase</td><td>JPM</td><td>Poonawala,Ebrahim</td><td>B-1-7</td><td>BUY</td><td>$327.33</td><td>$362.00</td><td>$820,571.45</td></tr><tr><td>Knight-Swift</td><td>KNX</td><td>Hoexter,Ken</td><td>B-1-7</td><td>BUY</td><td>$77.87</td><td>$84.00</td><td>$12,101.35</td></tr><tr><td>Snowflake</td><td>SNOW</td><td>Ikeda,Koji</td><td>C-1-9</td><td>BUY</td><td>$254.50</td><td>$300.00</td><td>$65,730.39</td></tr><tr><td>Spotify</td><td>SPOT</td><td>Reif Ehrlich,Jessica</td><td>C-1-9</td><td>BUY</td><td>$459.13</td><td>$685.00</td><td>$95,154.32</td></tr><tr><td>Visa</td><td>V</td><td>O’Neill,Matthew</td><td>B-1-7</td><td>BUY</td><td>$343.09</td><td>$410.00</td><td>$547,438.72</td></tr><tr><td>Walmart</td><td>WMT</td><td>Nardone,Christopher</td><td>B-1-7</td><td>BUY</td><td>$113.26</td><td>$144.00</td><td>$967,199.99</td></tr><tr><td>Lennar Corporation</td><td>LEN</td><td>Jadrosich,Rafe</td><td>B-3-7</td><td>U/P</td><td>$90.49</td><td>$77.00</td><td>$24,563.29</td></tr></table>

Source: BofA Global Research, Bloomberg  
BofA GLOBAL RESEARCH

Trading ideas and investment strategies discussed herein may give rise to significant risk and are not suitable for all investors. Investors should have experience in relevant markets and the financial resources to absorb any losses arising from applying these ideas or strategies.
BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.
Refer to important disclosures on page 30 to 34. Analyst Certification on page 23. Price Objective Basis/Risk on page 20.
12989472

## 01 July 2026

Equity
United States

Anthony Cassamassino
Strategist
BofAS
+1 212 449 6874
anthony.cassamassino@bofa.com

See Team Page for List of Analysts

## BofA Global Research Reports

<table><tr><td>Title: Subtitle</td><td>Primary</td><td>Date</td></tr><tr><td></td><td>Author</td><td>Published</td></tr></table>

S&P 500 Target Update: Savita 30 June

Mid-year 2026: take Subramanian 2026

Global Wave: Macro and Nigel Tupper 25 June earnings converge 2026

The RIC Report: Research 10 June

Exceptional economy, Investment 2026

remarkable markets Committee

## Ford (F)

Alexander Perry
Research Analyst
BofAS
+1 646 855 1365
aperry3@bofa.com

## Buy, PO \$20

## 3Q investment thesis

We expect continued upward estimate revisions for Ford given: 1) Ford's primary North America market is better positioned compared to Europe/China given a protectionist trade agenda (no Chinese EV disruption), a favorable regulatory environment given the roll off of emission standards programs that allows Ford to produce its highest margin accretive ICE vehicles, and resilient demand despite higher gas prices, 2) mix benefit from shift to higher margin trims at F Blue including off-road & V8 trims, 3) Novelis recovery progressing better than expected, 4) outsized growth in F's high margin software & services business, 5) support from Ford's new battery energy storage business & the scaling of its new EV platform with the launch of an affordable pickup next year.

Table 2: We highlight Ford as a 3Q26 top pick F key stock data

<table><tr><td>Industry</td><td>Automotive</td></tr><tr><td>Market cap (mm)</td><td>$63,695</td></tr><tr><td>Price</td><td>$13.90</td></tr><tr><td>P/E (2027)</td><td>6.8x</td></tr><tr><td>% of sell-side rated Buy</td><td>21%</td></tr><tr><td>Short Interest % of float</td><td>2.93%</td></tr></table>

Source: BofA Global Research estimates, Bloomberg  
BofA GLOBAL RESEARCH

## Catalysts:

Mix should improve from shift to higher margin trims at F Blue: We think Ford should see a continued mix benefit as production shifts toward higher-margin trims, including the Ranger Raptor, Explorer Tremor, and potentially higher V8 penetration on the F-150. Ford had been under-producing certain margin-accretive products relative to demand given the prior regulatory backdrop, and we expect management to lean further into its truck/SUV profit pools as constraints ease. We think this reinforces Ford's exposure to the right North America profit pools, while Ford's middle-upper income truck/SUV customer base appears relatively resilient despite the recent period of higher gas prices.

Expect Novelis recovery to support production and soften costs: We think the Novelis, Ford's key aluminum supplier, Oswego plant recovery following a fire should lessen recent production volatility for Ford's high margin F-Series. Novelis' restart appears largely in line with Ford's expectations. This should help reduce reliance on alternatively sourced aluminum, where Ford expects a \$1.5-\$2.0bn headwind. Ford's F-Series production also appears to be improving, with May production the highest year-to-date.

BESS opportunity offers diversification into faster growing end market: We think customer announcements related to Ford's new battery energy storage system (BESS) offering could be a strong catalyst. We believe Ford is likely to emerge as a credible BESS competitor in a market where hardware differentiation is limited, but demand remains strong across utilities, data centers, and large C&I customers. Tesla remains the benchmark with Megapack, but Ford should benefit from strong brand recognition, its

commercial footprint, and a manufacturing/supply-chain strategy designed to align with ITC and domestic-content requirements, which can reduce eligible project costs by \~30%-40%.

Software and services add high-margin growth lever: We think Ford's software and physical services business offers another high-margin growth lever, with management targeting 8% annual revenue growth through 2030 off a \~\$15bn base in 2025. While Ford Pro represents the majority of current revenue, we see potential for growth to become increasingly weighted toward Ford Blue as BlueCruise expands across more vehicles and functionality advances toward eyes-off autonomy beginning in 2028. Ford also sees opportunity to take share in parts from independents by expanding its catalogue and refining pricing, which could help reduce the perceived premium to consumers while supporting higher-margin recurring revenue.

BofA Global Research Reports

<table><tr><td>Title: Subtitle</td><td>Primary Author</td><td>Date Published</td></tr><tr><td>Automotive Industry: Weekly automotive pit stop: Thoughts on recent Ford rally</td><td>Alexander Perry</td><td>29 May 2026</td></tr><tr><td>Ford Motor: NDR Takeaways: See benefits from mix, UEV scaling, &amp; software &amp; services growth</td><td>Alexander Perry</td><td>07 May 2026</td></tr><tr><td>Ford Motor: Tariff adjustment &amp; timing of investments help drive 1Q beat</td><td>Alexander Perry</td><td>30 April 2026</td></tr><tr><td>Automotive Industry: Switching lanes in 2026: Reinstating coverage on N. American Autos/Auto-tech</td><td>Alexander Perry</td><td>04 March 2026</td></tr></table>

Upside risks: Upside risks to our PO are: 1) continued resilience in US light vehicle auto sales, 2) better than expected growth in higher margin revenue streams, incl. software & services and Ford Energy, 3) mix and pricing remain favorable, and 4) stronger production of ICE SUVs/trucks.

Downside risks: Downside risks to our PO are: 1) material downturn in US auto sales from weak consumer confidence & affordability challenges, 2) a sharp and sustained rise in input costs, 3) disruption in the supply base, 4) a sustained period of higher gas prices, 5) new vehicle pricing deteriorates, and 6) F energy ramps slower than expected.

Company Description: Ford Motor is one of the world's largest vehicle producers, with over 4mm units manufactured/sold globally under the Ford and Lincoln brands. In 2023, Ford re-segmented the business into Ford Blue, Ford Model e, Ford Pro, and Ford Credit. Most recently, Ford announced its entrance into the Battery Energy Storage Systems (BESS) market through Ford Energy, which plans to provide U.S.-assembled storage solutions for utilities, data centers, and large industrial/commercial customers. Ford's primary profit center remains North America, though the company also operates across Europe, South America, and Asia Pacific/China. Ford remains focused on positioning itself for the evolving auto industry through balanced investments across ICE/hybrid trucks and SUVs, electrification, software/services, autonomy, and mobility-adjacent opportunities.

# International Business Machines (IBM)

Wamsi Mohan
Research Analyst
BofAS
+1 646 855 3854
wamsi.mohan@bofa.com

## Buy, PO \$315

## 3Q investment thesis

We expect IBM to be well positioned into 3Q, supported by: 1) a decent F2Q setup that should reinforce the durability of the Software segment 2) Software growth that appears more resilient than recent broader software concerns imply, 3) Consulting expectations that have already been reset to a low bar, 4) continued Red Hat, Data, and Automation momentum, with Data benefiting from Confluent and strong organic trends, 5) underappreciated Infrastructure strength across distributed infrastructure, storage, and Power, 6) FCF durability supported by productivity, mix, and disciplined execution, and 7) quantum as an increasingly visible strategic catalyst where IBM appears to be receiving limited credit today. The broader pullback in software (from agentic AI concerns) and the Consulting-related pressure following peer commentary appear overdone in IBM's case. IBM's software portfolio is concentrated in the infrastructure layer where AI adoption should increase the need for hybrid cloud platforms, governed data, automation, and secure transaction processing rather than displace demand and Consulting represents only a minority of IBM's mix. Our PO of \$315 is based on 21x our C27 EV/FCF.

Table 3: We highlight Int Business Machine as a 3Q26 top pick IBM key stock data

<table><tr><td>Industry</td><td>IT Services</td></tr><tr><td>Market Cap (mn)</td><td>$267,717</td></tr><tr><td>Price</td><td>$281.21</td></tr><tr><td>P/E (2027)</td><td>21.9x</td></tr><tr><td>% of sell-side rated Buy</td><td>71%</td></tr><tr><td>Short interest % of float</td><td>3.21%</td></tr></table>

Source: BofA Global Research estimates, Bloomberg  
BofA GLOBAL RESEARCH

## Catalysts:

F2Q should support a better F3Q setup: IBM guided F2Q constant-currency revenue growth to be similar to F26 of >5%, with operating pre-tax margin expansion of \~50bps as software mix and productivity are partly offset by Confluent dilution. For F26, IBM expects >5% constant-currency revenue growth, \~\$1bn y/y FCF growth, Software growth of 10%+, Consulting growth in the low-to-mid single-digit range, and Infrastructure down low-single-digits, lapping difficult Z17 compares. We expect F2Q to be broadly consistent with this framework, with the potential for modest upside from better Software growth, including Data / Confluent and continued Automation strength, with slight acceleration in Red Hat (lapping tougher comps). Consulting expectations remain low but potential for stronger than guided growth in the 2H as enterprise AI adoption accelerates. Infrastructure trends should benefit from demand across Power, Storage, and broader hybrid infrastructure. A solid F2Q would help reinforce the durability of IBM's model and leave the company better positioned into 3Q.

Software concerns look overdone given IBM's portfolio: Recent software pressure has centered on whether agentic AI could disrupt traditional application software, but IBM's portfolio is tied to the infrastructure layer of enterprise IT which should benefit from agentic AI/enterprise AI adoption due to complexity created by more models, agents, workflows, and data movement across hybrid environments. IBM has emphasized that only a very small portion of its Software portfolio is application-like and we see IBM as better positioned for AI-driven software demand than the broader software pullback has implied.

Consulting concerns overdone relative to the size and setup of the business: Consulting is also only \~15% of IBM, so treating the recent pressure as evidence of a broader IBM demand issue appears too punitive, particularly given signings returned to growth in 1Q and AI is already embedded across a meaningful portion of backlog.

Quantum provides an underappreciated catalyst: Quantum should become a more visible part of the IBM story as interest increases (given recent pure-play Quantum IPOs). IBM reiterated in F1Q that it remains on track to deliver its first large-scale fault-tolerant quantum computer by 2029 and noted that partners could achieve the first examples of quantum advantage this year using IBM hardware. More recently, IBM and the U.S. Department of Commerce announced an LOI to create Anderon, a standalone U.S. quantum chip foundry supported by a proposed \$1bn CHIPS award and a \$1bn IBM cash contribution, followed by IBM announcing plans to invest more than \$10bn in quantum over the next five years. We view these announcements as material for IBM's quantum leadership to receive greater attention and see IBM's quantum business providing optionality for the stock.

BofA Global Research Reports

<table><tr><td>Title: Subtitle</td><td>Primary Author</td><td>Date Published</td></tr><tr><td>International Business Machines Corp.: Takeaways from “View from the Top” Call with IBM CEO Arvind Krishna</td><td>Wamsi Mohan</td><td>10 March 2026</td></tr><tr><td>International Business Machines Corp.: An acquisition of Confluent inline with Hybrid Cloud/Al strategy</td><td>Wamsi Mohan</td><td>08 December 2025</td></tr><tr><td>International Business Machines Corp.: Red Hat: A deeper look into the portfolio and drivers of growth</td><td>Wamsi Mohan</td><td>01 December 2025</td></tr><tr><td>International Business Machines Corp.: Quick thoughts from IBM’s Quantum Investor Day at Watson Research Center</td><td>Wamsi Mohan</td><td>31 October 2025</td></tr><tr><td>International Business Machines Corp.: Why is there so much volatility in Transaction Processing?</td><td>Wamsi Mohan</td><td>29 July 2025</td></tr><tr><td>International Business Machines Corp.: A Deep Dive on Bull/Bear cases for IBM stock; PO to $320</td><td>Wamsi Mohan</td><td>18 June 2025</td></tr><tr><td>International Business Machines Corp.: Transaction Processing: a deep dive into the history, pricing and opportunity</td><td>Wamsi Mohan</td><td>28 May 2025</td></tr><tr><td>International Business Machines Corp.: Will the z17 cycle be better than the prior cycles? Deep dive into historical cycles</td><td>Wamsi Mohan</td><td>29 April 2025</td></tr></table>

Upside risks: 1) faster reacceleration of topline, 2) faster improvement in margins, 3) better-than-expected accretion from M&A, and 4) delivery of upside to FCF.

Downside risks: 1) failure to execute on the company's growth roadmap, 2) inability to realize expected cost savings from restructuring, 3) technology/competitor risk in hardware, software, and services, 4) unforeseen currency impacts on revenue and profits, 5) acquisition integration, given IBM's acquisitive nature, and 6) increased concern of economic uncertainty and tightening corporate IT budgets.

Company Description: IBM is a global technology company focused on hybrid cloud, AI, software, consulting, infrastructure, and financing. The company reports through four

primary segments: Software, Consulting, Infrastructure, and Financing. Software includes Hybrid Cloud / Red Hat, Automation, Data, and Transaction Processing. Consulting includes Strategy and Technology and Intelligent Operations. Infrastructure includes Hybrid Infrastructure, including IBM Z and Distributed Infrastructure, and Infrastructure Support. IBM's strategy is centered on helping large enterprise clients modernize core systems, deploy AI across hybrid environments, govern data and workflows, and run mission-critical workloads with security, resiliency, and scale.

## Ionis (IONS)

Jason 

[中间内容因长度限制已省略]

 co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content

contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Subject to the quiet period applicable under laws of the various jurisdictions in which we distribute research reports and other legal and BofA policy-related restrictions on the publication of research reports, fundamental equity reports are produced on a regular basis as necessary to keep the investment recommendation current.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies. Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.

## Research Analysts

Anthony Cassamassino
Strategist
BofAS
anthony.cassamassino@bofa.com

Thomas (T.J.) Thornton
Head of Research Marketing
BofAS
thomas.thornton2@bofa.com

Derek Harris
Portfolio Strategist
BofAS
derek.harris@bofa.com

Paul Ciana, CMT
Technical Strategist
BofAS
paul.ciana@bofa.com

Alexander Perry
Research Analyst
BofAS
aperry3@bofa.com.

Wamsi Mohan
Research Analyst
BofAS
wamsi.mohan@bofa.com

Jason M. Gerberry
Research Analyst
BofAS
jason.gerberry@bofa.com

Ebrahim H. Poonawala
Research Analyst
BofAS
ebrahim.poonawala@bofa.com

Ken Hoexter
Research Analyst
BofAS
ken.hoexter@bofa.com

Koji Ikeda, CFA
Research Analyst
BofAS
koji.ikeda@bofa.com

Jessica Reif Ehrlich
Research Analyst
BofAS
jessica.reif@bofa.com

Matthew C. O'Neill
Research Analyst
BofAS
matthew.c.oneill@bofa.com

Christopher Nardone
Research Analyst
BofAS
christopher.nardone@bofa.com

Rafe Jadrosich
Research Analyst
BofAS
rafe.jadrosich@bofa.com

Trading ideas and investment strategies discussed herein may give rise to significant risk and are not suitable for all investors. Investors should have experience in relevant markets and the financial resources to absorb any losses arising from applying these ideas or strategies.
"""
