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
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`波士顿咨询`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
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
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：加入社群，领取完整研报解读与原始图表。。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份波士顿咨询研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
![](images/71eb6cac42794d1be85aadda89a32a65f7c8af4ca85ce3fdf55f0fac58a36b9d.jpg)

INTERNATIONAL BUSINESS

# The Great Divide: How the US and China Are Splitting the AI World

By Nikolaus Lang, Sylvain Duranton, Vladimir Lukic, Matt Langione, Rodrigo Ortiz Mena, Jona Lampert, and David Zuluaga Martínez

ARTICLE JUNE 30, 2026 15 MIN READ

The AI landscape today is dominated by the US and China, as both countries continue to put the weight of their private and public sectors behind the development of this technology. $^{1}$ But despite the superpowers' shared recognition of the importance of AI as a source of national power, their AI strategies have diverged. Each country is developing an AI technology stack designed to reduce its dependence on the other—which also means their stacks are increasingly incompatible. CEOs and policymakers across the globe may have to choose sides sooner than they think.

In 2024, we argued that the US was the clear leader in the burgeoning AI race, with China quickly gaining ground. Our updated, 2026 analysis across the six key enablers of AI supply—capital, talent, intellectual property (IP), data, energy, and compute—reveals the US has maintained its lead, fueled by its strength in talent and capital deployment. (See “Methodology.”) But China has continued to close the gap on compute power and has systematically translated its IP strengths into a consistent “fast follower” approach to frontier model development, with clear focus on rapid adoption of AI across the real economy. (See Exhibit 1.)

## - Methodology

Our research draws on an extensive quantitative comparison of the relative strength of the US, China, and select middle powers across the key enablers of AI supply (particularly of generative models and agentic systems built on them). We assess each country's strengths across 19 variables spanning the six key enablers of AI supply, drawing on a combination of public and proprietary data and analyses. These variables were selected as indicators or proxies for the national characteristics most critical for the development of AI.

Our analysis of comparative country strength in AI stretches back to 2024, when the geopolitics of AI were gaining global relevance. Our 2026 analysis reflects updated data and, in some cases, revisions that reflect the shifting center of gravity in the development trajectory of the technology.

Since our primary objective was to develop a relative sense of strength across enablers, we developed normalized scores by enabler and country or region in the following way:

\- Each indicator leads to an absolute value by country or region. These values are not normalized by population, size of the economy, or other such factors, because competition in the supply of AI is largely a function of scale.

\- Values for each indicator are then (linearly) normalized into country or region scores on a scale from 0 to 1, where 1 equals the highest actual value in our data set and 0 is set as absolute 0. Two indicators use a different anchor: for industrial electricity price, 0 is set at the lowest actual price; for mobile-broadband affordability, 0 is set at the UN Broadband Commission target of 2% of gross national income (GNI) per capita.

\- For each country or region, we then take the average normalized score across the indicators associated with an enabler to generate the enabler score. A country would have a score of 1 on an enabler only if it had the highest absolute value of all countries in our data set on every indicator associated with the enabler in question.

The following are the indicators we used to develop the stage-setting analysis of relative strength across the enablers of AI supply, with the sources for each indicated in parentheses. For further details on the analysis and data used in this study, please contact the authors.

## Capital

\- Venture capital funding from 2019 to 2026 (year-to-date), based on the observed AI-directed share of investments by venture capital funds, by country. In the case of China, this includes the sizeable pool of government VC funds devoted to AI. (PitchBook; Martin Beraja et al., “Government as Venture Capitalists in AI,” NBER working paper, and personal communication with the authors)

\- Corporate research and development (R&D) spending by the 20 largest technology companies, by country. (European Commission)

\- Capital expenditure (CAPEX) by the same set of technology companies. (S&P Capital IQ, company reports)

\- Sovereign wealth and public pension-fund investment power, adjusted for the share of assets under management allocated to equities and alternative investments (therefore excluding bonds, real estate and infrastructure investments, and risk-free assets). Whereas VC investments, corporate R&D, and CAPEX approximate actual spend on AI, this indicator widens the aperture to the country-level (i.e., sovereign) capital pools that could support strong national bets on AI. (Sovereign Wealth Fund Institute, sovereign wealth fund reports)

## Talent

\- Share of the top 2,000 AI researchers worldwide, based on the institution-affiliation of authors of leading AI publications. (AMiner)

• Share of the top 300 AI institutions. (AMiner)

\- Size of the AI-specialized talent pool working within a country based on AI-related job titles. (LinkedIn)

## IP

\- Share of the top 100 most-cited AI publications, 2019–2025. This indicator illustrates countries’ contributions to breakthrough research. (OpenAlex)

\- Share of the top 10% most-cited AI publications, 2019–2025. This indicator captures countries’ contributions to highly influential research more broadly, beyond the handful of landmark papers. (OpenAlex)

\- Share of notable machine learning models developed since 2019 based on the country/countries associated with the developing organization(s). (Epoch AI)

\- Average frontier-model capability, May 2025 through April 2026. This indicator uses the Epoch AI Capability Index, which combines scores across many benchmarks to allow models to be compared over time even as individual benchmarks reach saturation. (Epoch AI)

\- AI patent quantity, measured as the number of AI patent families, 2020 to present. (LexisNexis PatentSight)

\- Average AI patent quality, calculated by combining a patent's market coverage and its technological relevance based on the number of citations it receives from later patents, corrected for patent age. (LexisNexis PatentSight)

## Data

\- Total number of active handset-based and computer-based (i.e., connected by USB/dongle) mobile-broadband subscriptions, as proxy for relative magnitudes of digital data generation. (International Telecommunication Union)

\- Mobile-broadband affordability, measured as the cost of a data-only 5 GB basket as share of gross national income (GNI) per capita in 2025. (International Telecommunication Union; UN Broadband Commission)

These indicators serve as a proxy for the quantity of local data available, through the number of mobile-broadband subscriptions, and the amount of data produced by each individual, through the mobile-broadband affordability measure, which are important enablers for the development of locally optimized AI models. The data availability score is the product of the normalized subscriptions and normalized affordability values. While these metrics are

directionally indicative of the degree of digitization and the volume of (digital) data produced in each country, they do not, however, account for other important factors, such as the regulatory flexibility of data uses or the level of contextualization of data (i.e., how easily data of different types and sources can be used in an integrated fashion).

## Energy

\- Cost of electricity for a typical commercial/industrial user per kilowatt-hour. (Global Petrol Prices; Eurostat; GOV.UK)

\- Lead time to grid connection for a new 50 MW data center. (International Energy Agency, Al Israel, IESO)

Access to affordable energy is among the biggest bottlenecks for data center buildouts, as shown by the delays countries like Japan and the US have faced in getting new capacity built and running. These two indicators capture both sides of the constraint: availability, via grid connection lead times, and affordability, via the cost of electricity.

## Compute

\- Existing data center capacity, including hyperscaler, colocation, and enterprise facilities, measured in gigawatts. While not all data center capacity is optimized for AI workloads, as noted in footnote 3 of the text, internationally comparable data on AI-specific compute capacity is not publicly available; we therefore rely on total data center capacity as a proxy for countries' AI compute capacity. (datacenterHawk, CBRE, S&P Global)

\- Access to cutting-edge semiconductors optimized for AI workloads, such as NVIDIA's Blackwell and H200 chips. Access is scored 1.0 for countries and regions with no formal barriers, and 0.75 or 0.5 for progressively tighter levels of export-control restriction. NVIDIA's chips remain the industry gold standard, so regulatory barriers to access serve as a useful proxy for a country's ability to build out AI-optimized compute capacity. (US Department of Commerce)

![](images/8c98d3f69a8cceda6ee6028494f2fe144b2952c7c72e36015737776788ca9f6c.jpg)  
Source: BCG Institute analysis.
Note: See methodology sidebar for details on indicators by enabler.

As the US and China pursue AI sovereignty, the effects of their bifurcating technology stacks will be felt across geographies and sectors—defining the options leaders have available to engage with AI. In our 2024 study, we found that countries and companies could still mix and match across both superpower stacks. Since then, the two ecosystems have diverged to the point where neutrality may soon become harder to sustain, which changes the calculus. For most countries, the question is how best to develop AI resilience by ensuring robust access. AI is no longer something countries compete for, but something they compete with. For senior executives, the choice of which AI stack to use increasingly determines where a company can operate and how exposed it is to geopolitical volatility.

# The US and China: The Great Bifurcation

In late 2024 we argued that China had effectively reached parity with the US on AI model performance. Then, in January 2025, the US announced “Stargate,” a \$500 billion AI infrastructure joint venture led by OpenAI, Oracle, SoftBank, and MGX, while China released its highly capable and low-cost DeepSeek R1 model. $^{2}$

The US Leads in Capital Deployment for AI

These events were early indications of the increasingly distinct AI ecosystems that the US and China are committed to developing and expanding. China is increasingly focused on foundational research (publications, patents), domestic chip development, and real-economy adoption (deployment across industry and public services). By contrast, the US dominates the model and infrastructure layers, pouring capital into frontier models and the compute power required to serve them.

## The US: Building Data Centers and Top-Performing Models with Big Capital

The US strategy can best be described as winning through scale. In practice, this has meant an acceleration in capital deployment over the past 18 months, with the center of gravity shifting from frontier model development toward the data center infrastructure needed to meet growing inference demand from enterprise uptake and the rise of AI agents.

Even with this shift, significant capital continues to flow into the development of frontier models. Since 2023, US-based startups have raised around \$380 billion in AI-related venture capital, and incumbent tech giants invested more than \$300 billion in R&D in 2024 alone. A sizeable portion of those funds is invested in AI and adjacent innovations. The depth of these capital pools exceeds every other country’s and is reflected in the valuations of frontier model developers. (See Exhibit 2.)

## EXHIBIT 2

AI VC investment $^{1}$ (2023–2026 YTD, \$B)

![](images/bd2b9878b74b291497bbe01c9ccaec7ffdb9c962e9c998a17747862cd0a84cb1.jpg)  
Tech company R&D spend $^{2}$ (2024, \$B)

![](images/73e5325345e517de2b8211687be431bd775450a7d50e6d7fb92ed7e7b217eaa9.jpg)  
AI lab valuation $^{3}$ (2025–2026 YTD, \$B)

![](images/4090fa01609c72430646c52011756d62f2d03528068b3b376a0db69e1523a299.jpg)  
Source: BCG Institute analysis.  
$^{3}$ Values for China based on PitchBook data as baseline plus consideration for the government's role as VC investor based on the NBER working paper "Government as Venture Capitalists in AI" by Martin Beraja et al.; 185 billion invested by the Chinese government 2000–2023 has been distributed across the years using the same distribution that results from the PitchBook dataset; for years beyond 2023 we assumed the same growth/decline for government VC as results from the PitchBook data; the resulting decline in VC between 2023–2026 YTD compared to the prior period is consistent with an overall decline in the Chinese VC landscape as also reported by the OECD, PitchBook, and Preqin.  
$^{2}$ By top 20 tech companies in each country.  
$^{3}$ Based on most recent valuation in private markets through June 1, 2026.

What's new is the sheer scale of spending by US tech giants on the infrastructure to serve those models: CAPEX by the top technology companies surpassed \$400 billion in 2025—compared with \$63 billion in China—and is estimated to exceed \$800 billion in 2026. (See Exhibit 3.) That spending is expanding what is already the world's largest data center base with 50+ GW of capacity at the end of 2025, compared to 31 GW in China and 12 GW in the EU. $^{3}$ This extraordinary level of investment is responding to skyrocketing demand. For example, Google's monthly inference volume grew about 50-fold year-on-year, and the three largest US cloud providers now hold more than \$1.4 trillion in contracted future revenue, more than double a year ago and in significant measure driven by AI.

## EXHIBIT 3

## The US Speeds Ahead on Tech CAPEX

Tech CAPEX (TOP 20 TECH COMPANIES BY COUNTRY, \$B)

![](images/25bb54574001a1ad9dfcf4e32f03de3073a07d571ba6ab18dced18a639acd713.jpg)  
Tech CAPEX intensity
(TOP 20 TECH COMPANIES BY COUNTRY, CAPEX TO REVENUE RATIO) $^{1}$

![](images/777711e7895c1c6835ca5b824a616455271dc4b49497f6c4c0012935338c9bf0.jpg)  
Source: Capital IQ; company quarterly earnings and annual reports (Huawei, Oracle, Alibaba); BCG Institute analysis.
Note: US companies are Apple, Microsoft, NVIDIA, Amazon, Meta, Alphabet, Broadcom, Salesforce, Oracle, Adobe, ServiceNow, Accenture, IBM, AMD, Cisco, Qualcomm, Texas Instruments, Danaher, Intuit, Palantir; Chinese companies are Tencent, CATL, NetEase, Luxshare, Hikvision, Cambricon, NAURA, Will Semiconductor, SMIC, Techtronic, ZTE, DiDi, Kuaishou, Inovance, Hygon, Huawei (Huawei CAPEX from "Additions" line in Note 14 (PP&E) of annual reports; revenue from annual reports. CNY converted at FRED annual average rate), Alibaba, Xiaomi, Baidu, NARI. $^{1}$ Weighted average across companies.  
$^{2}$ Based on latest company guidance as of June 1, 2026, and estimated growth rate where company guidance not available.

The seemingly unstoppable rise in both CAPEX and VC investment in AI reflects the tightly integrated network of cross-investments and commercial commitments that has come to characterize the US tech ecosystem. Since 2024, deals worth more than \$1.5 trillion have been announced between US AI labs, chip designers, hyperscalers, and capital providers: equity stakes, multi-year compute contracts, and chip purchase agreements that link the major players to each other on multiple sides at once. (See Exhibit 4.) These investments are part of a concerted effort by big tech companies to ensure that suppliers across the AI value chain have the necessary capital to keep up with skyrocketing demand. While these integrated relationships and capital commitments are based on real, rapidly growing revenues, they create systemic risk in the US tech ecosystem: a default, write-down, or supply disruption at any major player could ripple quickly across the rest.

EXHIBIT 4 The Self-Reinforcing US AI Ecosystem  
![](images/16cc8c5878f0d40cec666083669a6a900435b2877a6d8cdf1c5cd267f3f27f11.jpg)  
Note: As of June 1, 2026; non-exhaustive illustration of US ecosystem; includes deals that span multiple years into the future; companies may fall into more than one category; includes deals above \$1B; not all companies shown are US companies; equity stakes sized at initial value of investment, not current value. $^{1}$ Announcements of “up to” these figures. $^{2}$ \$1.25B per month until May 2029.  
$^{3}$ Media reported figure, deal size not officially confirmed.  
$^{4}$ 40B investment includes other investors, e.g., MGX.

The inflow of capital to AI has been aided by the US government's emphasis on promoting bundled, exportable “AI stacks” of chips, models, cloud, and software. While maintaining targeted restrictions, US policy is more focused on outpacing through speed, scale, and ecosystem reach.

The US's light-touch regulatory strategy, however, has been tested by the arrival of increasingly powerful models with national security implications. In April 2026, Anthropic announced it was delaying the public release of its Claude Mythos model to allow the US government and select companies to prepare for the model's cyber capabilities. A version of Anthropic's model with built-in safeguards was released to the public in June 2026; days later, the US government issued an export control directive for Anthropic to suspend all access to the model by any foreign national, whether inside or outside the US (with the net effect that the model had to be suspended for all customers), indicating that national security concerns may in some instances take precedence over the global diffusion of the most capable AI models.

# China: Prioritizing Adoption of Cost-Optimized AI

China is pursuing a visibly different trajectory. While its investments remain sizeable, it is not mobilizing a comparable share of its economy to match the US at the frontier of model

Frontier model cost
(2025–2026 YTD, AVERAGE USD PER MILLION TOKENS FOR TOP 5 MODELS) $^{1}$

development or data center expansion. Instead, its strategy has focused on accelerating domestic adoption of AI while decreasing its reliance on foreign chips.

This shift is premised on China’s ability to remain competitive at the level of foundation models despite its limited access to the highest-end computing power. Indeed, since the release of DeepSeek R1 in Ja

[中间内容因长度限制已省略]

custom models for specific use cases (particularly when off-the-shelf models underperform), locally tailored applications, domestic cloud services, and regional compute capacity. For companies based outside the two superpowers, consider whether non-superpower alternatives for each tech stack layer

provide value from localization and diversification that justifies the additional costs and different performance profiles. This matters most for companies based in countries or regions with robust national AI strategies their firms can plug into.

\- How do you prepare for a landscape that keeps shifting? Build resilience in your AI tech stack by applying three principles: redundancy, modularity, and heterogeneity. Redundancy means having fallback options for the layers most exposed to disruption, such as contracting with two frontier model providers so a price hike or policy change impacting any one doesn’t strand critical workflows. Modularity means designing your stack so a shock at one layer doesn’t cascade through the others, for example by building applications in a way that lets you switch from one model provider to another without rewriting the underlying code. Heterogeneity means ensuring those fallbacks aren’t exposed to the same risks, such as pairing a US closed-weight model with an open-weights alternative that can be self-hosted, or running primary workloads on a US hyperscaler’s infrastructure with a sovereign-cloud option for regulated workloads.

These principles are harder to apply as the bifurcation deepens, and some break down entirely in a fully bifurcated world. Prioritizing them now won’t make you immune, but it buys time to pivot. Alongside the principles, leaders must maintain a watch list of shifts—tightening export controls or technical breakthroughs in either ecosystem—that would force them to activate these principles.

AI and the technologies that power it are irreversibly intertwined with the geopolitical environment; the more dependent a company is on technology, the more exposed to volatility. What separates strong companies from those that are more exposed to risk is whether they can translate this awareness into geopolitical muscle, building resilience that holds up as the superpower bifurcation deepens.

The authors would like to thank Azeem Azhar, founder of Exponential View; Wenwei Peng, post-doctoral fellow at Harvard University's Department of Economics; and Leonid Zhukov, director of the BCG X AI Science Institute, for their generous contributions to our research.

The BCG Institute is Boston Consulting Group's strategy think tank, dedicated to exploring and developing valuable new insights from business, technology, and science by embracing the powerful technology of ideas. The Institute engages leaders in provocative discussion and experimentation to expand the boundaries of business theory and practice and to translate innovative ideas from within and beyond

business. For more ideas and inspiration from the Institute, please visit our website and follow us on LinkedIn and X (formerly Twitter).

## Authors

![](images/c1b6a02dafb55587032039e72a7b93c52aa7859eaadfe346f3ac674fde9cb4a3.jpg)

![](images/4ffa0f45f375ef299d23e0d5afd4dd286dfe1a6b967900e61a423ace0d73e739.jpg)

![](images/e0dfd31c094b820c86716ca435f1737a4b085e725e39de0d9af34d9ca782b432.jpg)

![](images/2bdf18f25341c2c5c89228eced45079931912e851dbb5df78c2e74aa72f2862a.jpg)  
Managing Director & Senior Partner; Global Leader, BCG Institute; Global Vice Chair, Global Advantage Practice Munich

## Nikolaus Lang

![](images/0547b0d7f04628ccc39545df7e11d5a969867d3c7f5b90a079f95b0bb227e027.jpg)

## Vladimir Lukic

Managing Director & Senior Partner; Global Leader, Tech and Digital Advantage
Boston

![](images/8f30ea9ec69270fb449562d10824598d45d56f0326d38012b9b90fb99f09500e.jpg)

## Rodrigo Ortiz Mena

BCG Institute Ambassador, Geopolitics & Society Lab
New York

![](images/4f76281186054d2f2627f5189912e92f6bf45a735677d0611ff304a0e019a998.jpg)

![](images/ba8c8295cf4b3e7e901f3964464a60b40e8aba78e1622f21aa593890f2dc8016.jpg)

![](images/f01da118171f902c5dd444d49d1b02abfe71da4118051cd5662002e2329c12e0.jpg)

## Sylvain Duranton

![](images/9cf3c4187b96ac9e5633df421da37d25cf28a5fc27f880da5d6a9a3be2f8e44b.jpg)  
Managing Director & Senior Partner; Global Leader, BCG X Paris

## Matt Langione

Managing Director & Partner
Boston

![](images/218ac42c5385ffbc1325128d6f4d2131800d90a373b393bb37bab685f8cd7629.jpg)

![](images/3bc15b3605605d03588019a68dc4920217397edc20d5546d3011d706213d5b69.jpg)

## Jona Lampert

Consultant Doha

## David Zuluaga Martínez

![](images/7b2e85c9d4454c7d5d2fc4e6423bface0e5042d169a18299bbac1b1901004b6a.jpg)

Senior Director, BCG Institute
New York

![](images/663395b063b047c7b066162c11203d0042f0e322029bdfb3fcd6e5eb0ccf05e3.jpg)

## ABOUT BOSTON CONSULTING GROUP

Boston Consulting Group bridges the gap between ambition and outcomes for the world's leading companies and organizations. We are built for this era of unprecedented change — bringing strategic clarity rooted in over 60 years of deep domain knowledge, combined with applied AI shaped by our practitioners. BCG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com.

1 Generative AI has been the focal point of the commercial and geopolitical competition since 2024, but agentic and physical AI are rising in relevance—hence this piece’s broader use of “AI” rather than generative AI alone.

2 OpenAI has since pivoted toward leasing capacity from third parties rather than owning data centers directly.
"""
