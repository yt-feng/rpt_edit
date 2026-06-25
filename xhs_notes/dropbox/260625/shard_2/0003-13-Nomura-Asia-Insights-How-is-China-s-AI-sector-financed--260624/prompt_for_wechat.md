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
- 已识别机构名：`NOM`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份NOM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Asia Insights

Economics - Asia ex-Japan

## How is China's AI sector financed?

In our recent AI and double "K-shapes" thematic report, we discussed the US-China AI race and estimated the size of China's AI capex. A clear distinction in AI capex between the US and China is the role of government. US AI capex is overwhelmingly driven by the private sector, especially the hyperscalers, while China's AI capex is led and mainly funded by the state. In this note, we illustrate the decisive role of state capital from both the central and local governments, and we will also comment on private AI spending centered on cloud services and LLMs. With the renewed sharp declines in investment in Q2 and Beijing's commitment to stabilizing investment, we believe Beijing will likely accelerate bond issuance and step up fiscal spending in coming months. The AI sector will likely become an even more strategic policy focus, as China seeks to nurture its own full AI supply chains and pursue technology self-reliance.

## The decisive role of state capital

China's AI capex lags US levels materially, while the structure of its spending differs considerably from that of the US. While the US government offers a package of USD53bn in funding via the CHIPS and Science Act, the US AI ecosystem is overwhelmingly driven by the private sector, with the vast majority of AI capex funded by hyperscalers. Facing restricted access to advanced chips and a substantial technology gap with the US, China has mobilized extensive, multi-tiered state capital to support its own full AI supply chains, in pursuit of technological self-reliance. Although private enterprises dominate LLMs and AI agents, state capital plays a decisive role in the AI industrial chain's most constrained segments, particularly chip design and manufacturing. We illustrate the multi-layered funding schemes from the central government, local governments and SOEs.

## "Big Fund": From Semiconductors to AI

The National Integrated Circuit Industry Investment Fund (commonly known as the "Big Fund") is a core state-backed investment vehicle for China's semiconductor sector, with the strategic goal of elevating domestic IC industrial chains to global advanced standards and fostering world-leading enterprises by 2030. Three fund phases have been launched: Phases I, II and III were launched in September 2014, October 2019 and May 2024, with registered capital of RMB139bn, RMB204bn and RMB344bn, respectively. Major shareholders include the Ministry of Finance, China Development Bank, six major state-owned commercial banks and leading central SOEs, such as China National Tobacco and China Mobile.

The focus of investment has evolved progressively across these fund phases. Phase I prioritized downstream chip manufacturing, packaging and testing to support industrial chain leaders. Phase II shifted upward to target high-barrier upstream semiconductor equipment and materials. Phase III has the broadest coverage, focusing comprehensively on core bottleneck areas. Beyond the traditional semiconductor chain, Phase II has expanded its investment scope to printed circuit boards (PCBs) and AI industries.

Phase III has accelerated tangible AI capital deployment. In January 2025, it co-established the RMB60bn National AI Industry Investment Fund with Guozhitou (Shanghai) Private Equity Fund Management. In early May 2026, it was widely reported that the Big Fund was in active negotiations to lead the initial financing of Chinese AI startup DeepSeek. Collectively, the three Big Fund phases provide nearly RMB700bn in state capital support for semiconductors and AI.

## Ultra-long central government special bonds

To boost domestic demand, the central government started to issue ultra-long-term special bonds from 2024, with a large part of the funding designated to support the “Two Majors” (implementing major national strategies and building up security capacity in key areas). In 2026, Beijing allocated RMB800bn out of an overall RMB1.3trn in ultra-long

## Research Analysts

Asia Economics

Jing Wang - NIHK

jing.wang@NOM.com

+852 2252 1011

Ting Lu - NIHK

ting.lu@NOM.com

+852 2252 1306

central government special bonds (CGSB) for the “Two Majors”, with the scale the same as in 2025. In 2025, this RMB800bn funding supported 1,459 major projects covering transportation, water conservancy, energy, environmental protection and farmland construction. For 2026, the first batch of the “Two Majors” funding was RMB390bn, still prioritizing transportation and energy infrastructure projects. However, for the second batch of RMB217bn announced in April, AI was explicitly identified as one of the key areas for support, marking a formal shift of the use of CGSBs toward AI-related sectors.

## National Venture Capital Guidance Fund backed by ultra-long CGSBs

Launched in December 2025 under the joint promotion of the NDRC and Ministry of Finance, the National Venture Capital Guidance Fund is funded by ultra-long-term CGSBs, with initial capital of RMB100bn. With a 20-year lifespan, the fund provides stable, long-cycle capital for tech startups. It strategically targets frontier and high-growth sectors, including integrated circuits, AI, biopharmaceuticals, quantum technology and 6G communications, further supplementing state capital support for early-stage AI innovation.

## A Bloomberg report on a RMB2.0trn plan funded by ultra-long CGSBs

Recent news reports suggest Beijing might rely more on ultra-long CGSBs to support the AI sectors. For example, on 9 June 2026, Bloomberg reported that the Chinese government is drafting a RMB2.0trn plan to establish a cohesive nationwide network of data centers over the next five years. The network will rely on domestic suppliers for at least 80% of core technology, including AI chips from Huawei, and will be predominantly operated by state telecom giants, including China Mobile and China Telecom. When factoring in associated power grid infrastructure investments, total project spending is likely to reach at least RMB5.0trn. Funding will primarily come from ultra-long central government special bonds and state funds designated for strategic industries, supplemented by bank loans and private capital.

## The "new policy financing tools"

To arrest the sharp decline in investment, Beijing introduced “new policy financing tools (NPFT)”, which were launched in September 2025 with an initial quota of RMB500bn and an additional RMB800bn in the fiscal budget for this year. Like the previous two similar schemes in 2015-17 and 2022, these new tools are designed to channel equity financing from three policy banks to investment projects. Unlike the previous two rounds that focused on conventional infrastructure projects, the current program prioritizes the digital economy, AI and consumer infrastructure construction. The initial RMB500bn funding quota was divided up as follows: RMB250bn for China Development Bank (CDB), RMB150bn for Agricultural Development Bank of China (ADBC) and RMB100bn for the Export-Import Bank of China (CEXIM). Specifically, CDB allocated 37.5% of its funds to the digital economy and AI sectors, while CEXIM designated 40% of its capital for these fields. Acting as a quasi-fiscal tool, policy bank financing clearly demonstrates the shift of focus of governmental spending toward the AI industries.

Crucially, these funds serve as project equity capital, delivering a substantial investment leverage effect. According to the NDRC, the initial RMB500bn fund is expected to drive over RMB7trn in total project investment, and the leverage effect could be similar to the additional quota of RMB800bn announced this year.

## Local government funding for AI sectors has generally been contained

Compared with central government funding, local governments have deployed relatively less of their own funding to promote AI, as the property fallout continues to weigh on local fiscal conditions. In fact, a significant portion of local government bond issuance over the past three years has been allocated to replace local hidden debt or clean up arrears owed to the private sector.

The net financing of local government bonds totaled RMB5.4trn in 2025, including RMB0.8trn in general bonds and RMB4.6trn in special bonds. Nevertheless, only RMB140bn (merely $2.7\%$ ) was channelled into new infrastructure and strategic emerging industrial infrastructure. The proportion further declined to $1.0\%$ in Q1 2026, reflecting limited direct local funding for AI investment in general.

That said, some local governments have managed to ramp up their investment significantly to benefit from the global AI boom. For example, amid the unprecedented global memory supercycle, in April 2026, China's central tech hub Wuhan unveiled a funding package of RMB260bn to support memory chips production expansion in 2026, targeting two major companies: YMTC and XMC.

## Favorable financing conditions for AI Firms

In addition to direct state capital, China's financial system has also been supportive for the AI sectors. First, corporate financing costs have trended steadily downward. In 2025, according to the PBoC's Q1 2026 MPR, the overall financing cost of AI-related bond-issuing enterprises fell by about 35bp, outperforming the 24bp decline in average corporate loan rates, even though the 10y CGB yield rose by 18bp, reflecting policy-driven financing cost advantages for AI firms. Second, on funding structure, AI enterprises secured around RMB250bn in direct financing in 2025, with a notable expansion in medium- and long-term bond issuance. This provides stable, long-term capital for core technological R&D and production capacity expansion. Third, innovative financing tools are rapidly expanding. The issuance scale of tech innovation bonds and other specialized instruments surged by over $71\%$ in 2025, effectively diversifying financing channels and easing capital constraints for AI enterprises of various stages.

## STAR market and Hong Kong stock market are fueling China's AI ambitions

Amid efforts to revive mainland stock markets and restore capital market confidence, overall IPO activity in China's A-share market has been largely suspended since early 2024. However, a steady stream of tech firms have been allowed to be listed and raise capital on the Shanghai Stock Exchange's STAR Market. Specifically, in the past year, leading domestic GPU designers Moore Threads (RMB8bn) and MetaX (RMB3.9bn), alongside advanced packaging leader SJ Semiconductor (RMB4.8bn) have all completed their IPOs, underscoring institutional support for equity financing of the chips and AI sectors.

In contrast with onshore, Hong Kong has deliberately relaxed its IPO regulations to revitalize its capital market and attract mainland companies, particularly in the technology sector. This policy shift has effectively spurred a wave of listings. Key examples include PCB maker Victory Giant Technology, which raised HKD23bn in April, the largest Hong Kong IPO year to date. Computing chip designer Montage Technology completed a dual listing in Hong Kong with an IPO of HKD8bn, while LLMs firms Zhupu AI and MiniMax raised HKD4.4bn and HKD5.5bn, respectively. Together, the onshore STAR Market and the offshore Hong Kong stock market have strategically channelled substantial capital into Chinese tech companies, supporting the rise of China's chips and AI sectors.

## Other industrial incentive policies

Complementing high-profile fiscal and financial instruments, China might have also rolled out other industrial incentive schemes to counter external tech restrictions and enhance supply chain autonomy. For example, in December 2022, Reuters reported a proposed package of five-year, over RMB1trn in subsidies and tax credits to bolster domestic chip R&D and production capacity. In December 2025, Bloomberg disclosed a potential chip incentive program offering up to RMB500bn in subsidies and financial support, aiming to reduce reliance on overseas high-end chips and strengthen technological competitiveness amid US-China tech rivalry.

## Private AI spending focuses on cloud services and LLMs

Complementing state-led fiscal and industrial investment, China's private sector also makes contributions to large-scale AI capex, primarily driven by leading cloud service providers (CSPs) and LLM developers. Annual AI capex from major domestic hyperscalers totals approximately RMB500bn, forming a dual-drive investment pattern alongside public funding and fueling the rapid expansion of domestic AI computing capacity.

ByteDance raised its 2026 AI capex plan to over RMB200bn, according to a report from the South China Morning Post in early May, a $25\%$ increase from the RMB160bn preliminary budget discussed at end-2025. Alibaba commits industry-record long-term capital resources to AI and cloud infrastructure. In February 2025, the firm announced a three-year investment plan of over RMB380bn for cloud computing and AI hardware infrastructure, exceeding its total cumulative investment in this sector over the past decade and setting a new benchmark for private sector AI infrastructure spending in China. Importantly, in May 2026, Alibaba further signaled an upward revision of its investment roadmap, saying that its five-year AI infrastructure deployment budget will far surpass the previously announced RMB380bn, reflecting continuous upward adjustment of long-term AI capital deployment.

Other internet giants are also catching up or maintaining their spending trend. Tencent has recently accelerated its AI-focused capital outlays amid booming industrial demand. The

company recorded RMB37bn in AI-related capex in Q1 2026, up $16\%$ y-o-y and notably higher than Alibaba's RMB27bn for the same period. Tencent also vowed to boost full-year 2026 AI capital expenditure, according to Reuters, led by a stronger investment push in H2. Baidu maintains consistent long-term investment in indigenous AI innovation. Since the official launch of its Ernie Bot in 2023, Baidu's cumulative capital and R&D investment in the AI sector have exceeded RMB100bn, underpinning its continuous iteration of LLMs, autonomous driving technology and dedicated AI computing infrastructure.

Fig. 1: The decisive role of state capital in driving China's AI capex

<table><tr><td>Funding schemes</td><td>Funding size</td><td>Funding allocated to chips or AI-related sectors</td><td>Funding sources</td><td>Targeted areas</td></tr><tr><td>National Integrated Circuit Industry Investment Fund (&quot;Big Fund&quot;)</td><td>Phase I: RMB139bn (Sep 2014) Phase II: RMB204bn (Oct 2019) Phase III: RMB344bn (May 2024) A sum of RMB687bn</td><td>Fully</td><td>Ministry of Finance, China Development Bank, six state banks, and leading central SOEs such as China National Tobacco and China Mobile</td><td>Phase I: Chip manufacturing, foundries Phase II: more upstream, including chipmaking equipment, and chip design, packaging and testing Phase III: A more full AI supply chain, including memory chips, lithography equipment, LLMs such as DeepSeek</td></tr><tr><td>National AI Industry Investment Fund</td><td>RMB60bn (Jan 2025)</td><td>Fully</td><td>&quot;Big Fund&quot; Phase III and Guozhitou (Shanghai) Private Equity Fund Management</td><td>AI chips, memoary chips, AI applications</td></tr><tr><td>National Venture Capital Guidance Fund</td><td>RMB100bn (Dec 2025)</td><td>Partially</td><td>Ultra-long central government special bonds</td><td>Frontier sectors: including chips, AI, biopharmaceuticals, quantum technology, and 6G communications</td></tr><tr><td>Ultra-long central government special bonds</td><td>2024: RMB1.0trn 2025: RMB1.3trn 2026: RMB1.3trn</td><td>Partially, under &quot;Two Majors&quot; (major national strategies and security enhancement in major areas)</td><td>Issued by central government (Ministry of Finance)</td><td>The RMB800bn &quot;Two Majors&quot; in 2025 mainly covered transportation and energy. For the RMB800bn &quot;Two Majors&quot; in 2026, the first batch was RMB390bn, still prioritizing types of projects similar to 2025. However, for the second batch of RMB217bn announced in April 2026, AI was explicitly identified as a key supporting area</td></tr><tr><td>&quot;New Policy Financing Tools&quot;</td><td>RMB500bn (Sep 2025) RMB800bn (Mar 2026) A sum of RMB1.3trn</td><td>Partially</td><td>Three policy banks: China Development Bank (CDB), Agricultural Development Bank of China (ADBC), and Export-Import Bank of China (CEXIM)</td><td>Digital economy, AI, low-altitude economy, consumption infrastructure, green sectors, the agricultural sector and the rural areas, transportation and logistics, and industrial parks. The initial RMB500bn: RMB250bn for CDB, RMB150bn for ADBC, and RMB100bn for CEXIM, with about 40% allocated to the digital economy and AI sectors. Funds serve as project equity capital, delivering a substantial leverage effect, with the initial RMB500bn expected to drive over RMB7trn in total investment</td></tr><tr><td>Local government special bonds</td><td>2024: RMB4.0trn+RMB0.4trn 2025: RMB4.4trn+RMB0.5trn 2026: RMB4.4trn</td><td>Partially</td><td>Issued by local governments</td><td>Municipal infrastructure, industrial parks, transportation, environment protection, energy, state purchase of properties Funds could be served as project equity capital, while a large portion of funding in recent years have been used to swap out hidden debt or clean up arrears owed to the private sector, rather than direct investment</td></tr></table>

Source: NOM Global Economics.

## Appendix A-1

This report has been produced by NOM International (Hong Kong) Ltd. (NIHK), Hong Kong. See Disclaimers for NOM Group entity details.

## Analyst Certification

We, Jing Wang and Ting Lu, hereby certify (1) that the views expressed in this Research report accurately reflect our personal views about any or all of the subject securities or issuers referred to in this Research report, (2) no part of our compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this Research report and (3) no part of our compensation is tied to any specific investment banking transactions performed by NOM Securities International, Inc., NOM International plc or any other NOM Group company.

## Important Disclosures

## Online availability of research and conflict-of-interest disclosures

NOM Group research is available on www.NOMnow.com/research, Bloomberg, Capital IQ, Factset, LSEG.

Important disclosures may be read at http://go.NOMnow.com/research/m/Disclosures or requested from NOM Securiti

[中间内容因长度限制已省略]

34. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia ('Saudi Arabia') or a 'Market Counterparty' or a 'Professional Client' (as defined by the Dubai Financial Services Authority) in the United Arab Emirates ('UAE') or a 'Market Counterparty' or a 'Business Customer' (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar ('Qatar') by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

## NOM Securities Co., Ltd.

Financial instruments firm registered with the Kanto Local Finance Bureau (registration No. 142)

Member associations: Japan Securities Dealers Association; Investment Management Association of Japan; The Financial Futures Association of Japan; Type II Financial Instruments Firms Association; and Japan Security Token Offering Association.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
