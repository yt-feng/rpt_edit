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
- 已识别机构名：`HSBC`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份HSBC研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# China AIDCs and Supply Chain

Riding on robust demand for AI compute

\- We expect demand for AI compute in 2028e to be 5x that of 2025's level as model training and inference needs grow...

\- ... benefiting leaders in AI data centres (AIDCs) and supply chain participants at various stages like switches

◆ Initiate on Range and Ruijie with Buy ratings in separate reports

Strong AI compute demand. We estimate China's AI compute demand to boom and reach c5GW by 2028, c5x more than 2025, driven by explosive demand for large language model training and inference. Domestic hyperscalers are rapidly boosting their capex, with the combined spending of ByteDance, Alibaba, and Tencent reaching RMB346bn in 2025 and set to more than double to over RMB700bn in 2026 (see Ex 6). This is still well below the spending intensity of US peers, indicating there's substantial growth potential. Leading AIDC operators and key supply chain participants (like switch vendors) should benefit.

AI network upgrades. We see the TAM for data centre switches – the high-speed traffic controllers of a network – reaching RMB118bn in 2030e, implying a 28% CAGR in 2025-30e, on 1) more layers being added to a network's structure given larger GPU clusters; 2) upgrades to switch port speed could boost product prices; and 3) scale-up switches (that connect GPUs within a rack) are new revenue drivers on rising penetration of SuperPOD. The shift to these SuperPOD cluster architecture raises technical barriers and boosts the value of specialised AIDC operators like Range whose market share we expect to reach 9% in 2028e vs 6% in 2025 in the domestic data centre space, and Ruijie's market share in China data centre switches should reach 24% in 2028e vs 21% in 2025.

Going global opportunities. Over the long term, domestic IDC operators have the potential to serve global inference demand via "token exports", leveraging China's model cost-efficiency, abundant low-cost green power in western China, and lower construction, mechanical and electrical equipment costs.

Prefer Range and Ruijie (both rated Buy). Benefiting from the AI compute boom, we expect robust AIDC revenue growth for Range, and a 43% 2025-28e EBITDA CAGR with improving margins. We expect Ruijie to gain market share in the fast-growing data centre switch market and expect its net margin to improve to 10% in 2028e vs 5% in 2025 given better economies of scale. See our initiation reports published today on Range and Ruijie.

Equities IT Services

China

Yiran Liu\* (Reg. No. S1700520040001)  
Head of A-share IT Software Research  
HSBC Qianhai Securities Limited  
yiran1.liu@hsbcqh.com.cn  
+86 10 5795 2349

Heng Zhang\* (Reg. No. S1700524050001)

Analyst, A-share IT Software Research

HSBC Qianhai Securities Limited

heng.zhang@hsbcqh.com.cn

+86 10 5795 2384

\* Employed by a non-US affiliate of HSBC Securities (USA) Inc, and is not registered/ qualified pursuant to FINRA regulations

Exhibit 1. Ratings, target prices, financials, and valuations of our preferred stocks

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Market CapUSDbn</td><td rowspan="2">3MADTVUSDm</td><td rowspan="2">TPLC</td><td rowspan="2">PriceLC</td><td rowspan="2">Rating</td><td rowspan="2">Upside</td><td colspan="2">EPS growth_</td><td colspan="2">Rev growth_</td><td colspan="2">__PE (x)_</td><td colspan="2">__PS (x)_</td><td colspan="2">PEG (x)</td><td colspan="2">__ROE</td></tr><tr><td>2026e</td><td>2027e</td><td>2026e</td><td>2027e</td><td>2026e</td><td>2027e</td><td>2026e</td><td>2027e</td><td>2026e</td><td>2027e</td><td>2026e</td><td>2027e</td></tr><tr><td>Range</td><td>300442 CH</td><td>20.7</td><td>697</td><td>111.00</td><td>85.18</td><td>Buy</td><td>30%</td><td>-45%</td><td>38%</td><td>39%</td><td>33%</td><td>51</td><td>37</td><td>17.8</td><td>13.3</td><td>0.9</td><td>18%</td><td>21%</td><td></td></tr><tr><td>Ruijie</td><td>301165 CH</td><td>11.2</td><td>141</td><td>89.00</td><td>67.80</td><td>Buy</td><td>31%</td><td>115%</td><td>27%</td><td>27%</td><td>26%</td><td>50</td><td>40</td><td>4.2</td><td>3.3</td><td>1.1</td><td>23%</td><td>30%</td><td></td></tr></table>

Source: Wind, HSBC Qianhai Securities estimates. Note: Priced at close of 18 June 2026. TP – target price; nm = not meaningful

## Disclosures & Disclaimer

This report must be read with the disclosures and the analyst certifications in the Disclosure appendix, and with the Disclaimer, which forms part of it.

Issuer of report: HSBC Qianhai Securities Limited

View HSBC Qianhai Securities at: https://www.research.hsbc.com

# Robust demand, limited supply

\- Strong token consumption brings robust demand for compute, benefiting AIDC players

\- Price increases in the GPU rental business (GPUaaS) are likely to continue with leaders gaining market share

◆ Next step is for tokens to keep going global

## Robust token consumption brings strong AIDC demand

## AIDC is the core infrastructure for AI compute

We believe AIDC is one of the key sections in the AI compute supply chain. As the physical infrastructure of compute, AIDCs process data and connect hardware to software.

Exhibit 2. AI compute supply chain: Data centres are key infrastructure  
![](images/fb0d837dc8184e4e51f16f5be56a861f01bb9737578c9bd69c7d619d89ecadbf.jpg)

Data Annotation

Source: Company data, HSBC Qianhai Securities

Data Governance

Large Models

Computer Vision

Speech Recognition

Machine Learning Platform

Applications Layer

Embodied Intelligence

AI Mobile Devices

AI Wearable Devices

Enterprise Services

Due to 1) strong AI demand and 2) limited GPU and AIDC capacity supply, the GPU rental (GPUaaS) business is quite popular in both China and US. Some traditional internet data centre (IDC)/AIDC players have moved into this business. We list several GPUaaS businesses below. In our view, GPUaaS provides multiple advantages compared to in-house built GPU infrastructure, including 1) easier/quicker access to high-end GPUs compared to self-built; and 2) less investment required as rental refers to Opex instead of Capex for enterprises.

Exhibit 3. Data centres and GPU leasing business model comparisons

<table><tr><td>Feature</td><td>Retail data centres</td><td>Wholesale / Hyperscale data centres</td><td>AI data centres</td><td>GPU rental (GPUaaS)</td><td>Neo-cloud (GPUaaS)</td><td>Hyperscale public cloud</td></tr><tr><td>Representative companies</td><td>VNET (VNET US), Sinnet (300383 CH)</td><td>GDS (GDS US/9698 HK), VNET (VNET), Range (300442 CH), Chindata (Hec 600673 CH), Baosight (600845 CH)</td><td>Range (300442 CH), Chindata (Hec 600673 CH), Baosight (600845 CH), BONC (300166 CH)</td><td>Range (300442 CH), Lettall Electronic (603629 CH), Sharetronic (300857 CH), Glory View (301396 CH), BONC (300166 CH), Dawei (600589 CH)</td><td>CoreWeave (CRWV US), Nebius (NBIS US)</td><td>AWS, Azure, AliCloud</td></tr><tr><td>Pricing model</td><td>Monthly operation fee</td><td>Monthly operation fee</td><td>Monthly operation fee</td><td>Monthly rental fee + Revenue sharing based on token consumption</td><td>Pay-As-You-Go/ On-demand saving plans (commitment) Preemptible virtual machines</td><td>Pay-As-You-Go/ On-demand saving plans (commitment)</td></tr><tr><td>Service description</td><td>Physical facility rights</td><td>Physical facility rights</td><td>Physical facility and hardware rights, deeply tuned network</td><td>Physical hardware rights</td><td>AI-native cloud services</td><td>General-purpose virtualized cloud resources</td></tr><tr><td>Own data centres?</td><td>Yes</td><td>Yes</td><td>Yes</td><td>No</td><td>Partially</td><td>Partially</td></tr><tr><td>Own servers?</td><td>No</td><td>No</td><td>Partially</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Network capability</td><td>Customer defined connectivity</td><td>Standard Ethernet at scale</td><td>Deeply tuned to support GPU clusters</td><td>Varies</td><td>Deeply tuned to support GPU clusters</td><td>Standardised SDN (software defined network)</td></tr><tr><td>Software support</td><td>Limited</td><td>Limited</td><td>Limited</td><td>Limited</td><td>AI containers, rendering &amp; inference</td><td>Full-stack (database, security, web, serverless)</td></tr><tr><td>Target market</td><td>General businesses</td><td>Hyperscalers, AI labs, large enterprises</td><td>AI labs, hyperscalers</td><td>AI labs, hyperscalers</td><td>AI labs, hyperscalers</td><td>General businesses</td></tr><tr><td>Contract terms</td><td>Short-to-long-term lease (1-10 years)</td><td>Long-term lease (e.g. 7-15 years)</td><td>Long-term lease (e.g. 3-5 years)</td><td>Short-to-long-term lease (e.g. 1-5 years)</td><td>Long-term lock-in but greater contractual flexibility</td><td>Highly flexible (pay-as-you-go by hour/second)</td></tr><tr><td>Key advantages</td><td>Cost-effective, reliable operations, scalable, good connectivity, proximity</td><td>Cost-effective, physical privacy, reliable operations, scalable, good connectivity</td><td>AI-optimized, physical privacy, reliable operations, scalable, good connectivity, advanced GPU access, high cluster performance</td><td>Advanced GPU access, high cluster performance</td><td>Advanced GPU access, high cluster performance, flexible contract terms</td><td>Global reach, versatile, instant scalability</td></tr></table>

Source: Company data, HSBC Qianhai Securities

## Strong compute demand to drive accelerated growth; we expect China intelligent compute to grow at a CAGR of $74\%$ over 2025-28e, reaching 5GW in 2028e

With more advanced model launches in 2026, token consumption has shown strong growth. Per National Data Administration, China's daily token consumption reached 140trn in March 2026, which is $40\%$ more vs December 2025. In addition, IDC estimates that global agent token usage will grow to 152,667 peta $(10^{15})$ in 2030e, vs 0.0005 peta in 2025. The rising penetration of generative artificial intelligence (GAI) and robust token usage growth potential brings strong demand for AI compute, and hence, CSPs/Internet companies have raised their capex. Notably, per company guidance and media reporting, China hyperscalers' total capex in 2026e is set to more than double to over cRMB700bn (see Ex 6).

As GAI penetration is still in the early stages, we expect the strong compute demand to persist and expect China intelligent compute (@FP16, or 16-bit binary floating-point computer number format) to grow to over 12 ZFLOPS (10^3 EFLOPS) in 2028e, close to 8x vs 2025 level. In addition, we expect China intelligent compute data centre demand to grow at a CAGR of $74\%$ over 2025-28e and to reach c5.4GW in 2028e. AIDC players that have more reserved/running capacity should benefit.

Exhibit 4. China daily token usage grew robustly over the last two years  
![](images/71f0ba3a78a7a6e9cd216d36279acf4f5eb1f4846c1906103bd8f800a24c3bba.jpg)  
Source: National Data Administration, HSBC Qianhai Securities

Exhibit 5. IDC estimates global agent token usage will grow to 152,667 peta in 2030e  
![](images/7d9041068ae7d770b34e0a4ab5544a9f3f3af61637ad650c2d54cf8f106bfee6.jpg)  
Source: IDC estimates, HSBC Qianhai Securities

Exhibit 6. China CSPs continue to raise their capex  
![](images/cd22078b11eb73b7e4284b20c28aa89a43be74d08a32286d8c7c57dbdf7a6368.jpg)  
Source: Company data (capex guidance), Reuters (23 Dec 2025), Bloomberg (May 2026), South China Morning Post (9 May 2026), HSBC Qianhai Securities

Exhibit 7. We expect China intelligent compute to grow to c12,354 EFLOPS (@FP16) in 2028e  
![](images/b9b85fa1b063e827f4b31741bc8ab7b28539442fc9cd3acea2123a53ca015099.jpg)  
Source: MIIT, CAICT, IDC, HSBC Qianhai Securities estimates

Exhibit 8. We expect China intelligent compute data centre demand to grow at a CAGR of 74% over 2025-28e and to reach c5.4GW in 2028e  
![](images/b0c78b4f914bbbd38aea0cb1709d1dd9babb3d0a42e2c12dd854e35ba7554846.jpg)  
Source: MIIT, CAICT, IDC, Nvidia, HSBC Qianhai Securities estimates

Based on 1) our above forecast for China's intelligent compute data centre capacity and the compute scale and pricing of mainstream NVIDIA GPU servers/compute trays, etc.; and 2) Range's annual data centre operation revenue per MW, we expect China's data centre market to reach RMB165bn in 2028. Specifically, we expect the AIDC market to grow at a CAGR of $78\%$ over 2025-28e, reaching RMB75bn on 2028e.

Exhibit 9. China third-party data centre TAM/growth  
![](images/17a631d43de27d09431fd2b28a4fe8082334d7b938bc872075ccd5f726addfaa.jpg)  
Source: MIIT, CAICT, IDC, Range company data, HSBC Qianhai Securities estimates

## Supply is the bottleneck; leaders to gain market share

We expect AIDC to face supply shortages; GPUaaS should see robust growth
Due to strong AI demand and given limited GPU and AIDC capacity supply, since 2025, the GPUaaS market saw continued price hikes. Note that the Nvidia H100 rental price has risen from RMB12/GPU/hour to RMB17/GPU/hour, up c40%. Meanwhile, leading CSPs have announced cloud services price rises as well.

A new AIDC buildout usually needs 18-24 months for construction and utilisation ramp-up (source: Range company data). Per third party AIDC capacity plans, we expect supply shortages to continue, and the GPU rental business should see continued growth. AIDC players providing GPU leasing services (such as Range and Hec, per Exhibit 3), will continue to enjoy benefits from tight supply.

Exhibit 10. H100 1-year rental price has continued to rise since 2026  
![](images/0a7bf5d2e19136a9d7144abf48ba196b3819a3e25c49c0120bf9a306977bdc0f.jpg)  
Source: SemiAnalysis GPU pricing index, HSBC Qianhai Securities

Exhibit 11. Nebius raised further its GPU rental prices in May 2026  
![](images/f641bb18ec6c25e67227cdd483bf25d9d3dfec8893a271947d3fbca6c482c551.jpg)  
Source: Nebius, HSBC Qianhai Securities

Exhibit 12. Many CSPs have announced cloud services price hikes since 1Q26

<table><tr><td>Company</td><td>Announcement date</td><td>Effective date</td><td>Adjusted services</td><td>Price hikes</td></tr><tr><td colspan="5">Chinese hyperscalers</td></tr><tr><td>Tencent Cloud</td><td>4/9/2026</td><td>5/9/2026</td><td>AI computing power, TKE native nodes and EMR</td><td>+5%</td></tr><tr><td>Tencent Cloud</td><td>3/11/2026</td><td>3/13/2026</td><td>Tencent HY2.0 Instruct/Think model token prices</td><td>+420%-+463%</td></tr><tr><td>Baidu Cloud</td><td>3/18/2026</td><td>4/18/2026</td><td>AI computing products and parallel file storage</td><td>+5%-+30%</td></tr><tr><td>AliCloud</td><td>4/15/2026</td><td>5/15/2026</td><td>Bailian MaaS platform model unit prices</td><td>+2%-+5%</td></tr><tr><td>AliCloud</td><td>4/14/2026</td><td>4/14/2026</td><td>DataWorks API quotas adjustment and usage based billings</td><td>Charging on excess usage</td></tr><tr><td>AliCloud</td><td>3/18/2026</td><td>4/18/2026</td><td>GPU computing services e.g. T-head Zhenwu 810E GPU</td><td>+5%-+34%</td></tr><tr><td>AliCloud</td><td>3/18/2026</td><td>4/18/2026</td><td>Cloud parallel file storage (AI computing version)</td><td>+30%</td></tr><tr><td>Ucloud</td><td>2/11/2026</td><td>3/1/2026</td><td>All products and services for contract renewals and new contract</td><td>+5%-+12%</td></tr><tr><td>Wangsu</td><td>2/1/2026</td><td>2/1/2026</td><td>CDN standard service traffic/CDN fast origin-pull traffic</td><td>+35%/+40%</td></tr><tr><td>Wangsu</td><td>2/1/2026</td><td>2/1/2026</td><td>Object storage service</td><td>+40%</td></tr><tr><td colspan="5">Overseas hyperscalers</td></tr><tr><td>Google Cloud</td><td>1/27/2026</td><td>5/1/2026</td><td>Networking services for CDN interconnect, direct peering and carrier peering (data transfer fees)</td><td>+100% for North America +60% for Europe +40% for Asia</td></tr><tr><td>Amazon AWS</td><td>1/23/2026</td><td>1/23/2026</td><td>EC2 machine learning capacity blocks</td><td>+15%</td></tr></table>

Source: Company data, HSBC Qianhai Securities

Exhibit 13. Overview of leading third-party IDC suppliers' in-service IT capacity and plans  
![](images/8ce2b381ebd873c5b0ae041d60cb287efb246f99e4d30ec05bdf0e511b545a1d.jpg)  
Source: Company data, HSBC Qianhai Securities

## SuperPOD cluster architecture increases AIDC operators' value proposition

In the era of intelligent computing, cluster network communication bottlenecks have become the core constraint for both AI training and inference. However, a highly integrated SuperPOD architecture can break through bottlenecks related to scale, performance, and reliability. A SuperPOD is a technical architecture that aggregates multiple GPUs into a single SuperPOD in one rack via high-bandwidth interconnects, enabling large-scale parallel training.

This technological leap is driving new requirements for data centres in terms of cooling, power supply capacity, floor load-bearing capacity, ceiling height, and network architecture. Leading vendors with strong technical capabilities and capital resources are better positioned to secure SuperPOD data centre orders, leading to accelerated market share consolidation.

Moreover, the value proposition of SuperPOD data centres is expanding across multiple dimensions. Taking Range as an example, its AIDC business has not yet deployed SuperPOD solutions at scale, with high-performance servers remaining its primary equipment. However, its 2025 annualized revenue per MW of deployed capacity is already cRMB15m, representing a $c56\%$ increase compared to the cRMB9.6m generated by traditional IDC operation services. This provides early validation of the value uplift in AI data centres.

We believe that given the growing use of intelligent agents and large language models, data centres will evolve into “token factories”. Demand for long-context processing and high-concurrency throughput are intensifying, which is driving intelligent computing centres to enhance computing density, network bandwidth, and energy efficiency. AIDC service providers that possess sufficient energy quota reserves, high-bandwidth low-latency networks, liquid cooling technologies, and scalable operational and delivery capabilities will gain structural advantages during the industry upcycle and the ongoing shift in technical paradigms and are expected to continue benefiting in the long term.

Exhibit 14. SuperPOD brings higher requirements for data centre operators

<table><tr><td></td><td>General purpose CPU cabinet</td><td>Traditional AIDC cabinetExample: DGX H100</td><td>Overseas SuperPOD AIDC cabinetExample: DGX GB300 NVL72</td><td>Domestic SuperPOD AIDC cabinetExample: Atlas 950 SuperPoD</td></tr><tr><td>Cabinet power</td><td>4-12kW</td><td>40kW</td><td>120kW</td><td>Over 120kW</td></tr><tr><td>Core components</td><td>CPU servers</td><td>4 DGX H100 servers + 3 P

[中间内容因长度限制已省略]

tiple, Grupo Financiero HSBC is authorized and regulated by Secretaría de Hacienda y Crédito Público and Comisión Nacional Bancaria y de Valores (CNBV). In Brazil, this document has been distributed by Banco HSBC SA ("HSBC Brazil"), and/or its affiliates. As required by Resolution No. 20/2021 of the Securities and Exchange Commission of Brazil (Comissão de Valores Mobiliários), potential conflicts of interest concerning (i) HSBC Brazil and/or its affiliates; and (ii) the analyst(s) responsible for authoring this report are stated on the chart above labelled "HSBC & Analyst Disclosures".

If you are a customer of HSBC International Wealth & Premier Banking ("IWPB"), including HSBC Private Bank, you are eligible to receive this publication only if: (i) you have been approved to receive relevant research publications by an applicable HSBC legal entity; (ii) you have agreed to the applicable HSBC entity's terms and conditions and/or customer declaration for accessing research; and (iii) you have agreed to the terms and conditions of any other internet banking, online banking, mobile banking and/or investment services offered by that HSBC entity, through which you will access research publications (collectively with (ii), the "Terms"). If you do not meet the above eligibility requirements, please disregard this publication and, if you are a IWPB customer, please notify your Relationship Manager or call the relevant customer hotline. Distribution of this publication is the sole responsibility of the HSBC entity with whom you have agreed the Terms. Receipt of research publications is strictly subject to the Terms and any other conditions or disclaimers applicable to the provision of the publications that may be advised by IWPB. © Copyright 2026, HSBC Qianhai Securities Limited, ALL RIGHTS RESERVED. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, in any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of HSBC Qianhai Securities Limited.

# HSBC Qianhai Research Team

Head of Research, HSBC Qianhai Securities  
Steven Sun +86 755 8898 3158  
stevensun@hsbcqh.com.cn

## China Equity Strategy

Analyst, Head of China Equity Strategy Research  
Steven Sun +86 755 8898 3158 stevensun@hsbcqh.com.cn

Analyst, China Equity Strategy Research  
Jeffrey Xie +86 10 5795 2361  
jeffrey.p.xie@hsbcqh.com.cn

Analyst, China Equity Strategy Research
Neal Chen +86 21 5066 2066
neal.m.chen@hsbcqh.com.cn

Analyst, China Equity Strategy Research  
Lydia Li +86 21 5066 2022  
lydia.j.y.li@hsbcqh.com.cn

## Agriculture & Fishery

Analyst, Head of A-share Agriculture Research
Yihui Sha +86 21 5066 2004
yihui.sha@hsbcqh.com.cn

## Auto & Auto Parts

Analyst, China Autos Research  
Elaine Chen +86 10 5795 2364  
elaine.chen@hsbcqh.com.cn

Analyst, China Autos Research  
Michel Liu +86 10 5795 2351  
michel.m.liu@hsbcqh.com.cn

## Consumer

Analyst, Head of A-share Consumer Research
Kathy Song +86 21 5066 2007
kathy.l.h.song@hsbcqh.com.cn

Analyst, A-share Food & Beverage and Pulp & Paper Research  
Darron Xue +86 755 8898 3407  
darron.xue@hsbcqh.com.cn

Analyst, A-Share Consumer  
Li Quan +86 755 8898 3471  
li.quan@hsbcqh.com.cn

Analyst, A-Share Consumer
Doris Luo +86 755 8898 3161
doris.y.s.luo@hsbcqh.com.cn

Analyst, A-Share Consumer
Eric Liu +86 21 5066 2053
eric.x.c.liu@hsbcqh.com.cn

## Financials

Analyst, Head of A-share Financials Research
Angel Sun +86 21 5066 2015
angel.y.sun@hsbcqh.com.cn

## Industrials & Renewables

Analyst, Head of A-share Industrials & Renewables Research  
Corey Chan +86 21 5066 2001  
corey.chan@hsbcqh.com.cn

Analyst, A-share Industrials & Renewables Research  
Amy Hu +86 755 8898 3408  
ruo.lin.hu@hsbcqh.com.cn

Analyst, A-share Industrials & Renewables Research  
Dun Wang +86 21 5066 2027  
dun.wang@hsbcqh.com.cn

Analyst, A-share Industrials & Renewables Research
Echo Zhang +86 10 5795 2314
echo.x.zhang@hsbcqh.com.cn

Analyst, A-share Industrials & Renewables Research  
Gary Yao +86 21 5066 2078  
gary.x.d.yao@hsbcqh.com.cn

## Healthcare

Analyst, Head of China Healthcare Research
Linda Shu +86 755 8898 3246
linda.y.l.shu@hsbcqh.com.cn

Analyst, China Healthcare Research
Cindy Chai +86 21 5066 2005
cindy.x.r.chai@hsbcqh.com.cn

Analyst, China Healthcare Research
Oliver Wang +86 21 5066 2058
oliver.h.y.wang@hsbcqh.com.cn

Analyst, China Healthcare Research  
Andre Sun +86 21 5066 2034  
andre.h.j.sun@hsbcqh.com.cn

Associate Evie Liu

## Petrochemical & New Materials

Analyst, Head of A-share Petrochem & New Materials Research  
Yi Ru +86 21 5066 2008  
yi.ru@hsbcqh.com.cn

Analyst, A-share Petrochem & New Materials Research  
Jill Huang +86 21 5066 2024  
jill.q.huang@hsbcqh.com.cn

Telecoms, Media & Technology  
Analyst, A-share Technology Hardware Research  
Bingyi Zheng +86 21 5066 2028  
bingyi.zheng@hsbcqh.com.cn

Analyst, A-share Technology Hardware Research  
Cara Su +86 21 5066 2080  
cara.z.h.su@hsbcqh.com.cn

Associate Yongzhu Wang

Analyst, Head of A-share Media & Internet Research  
Jing Han +86 10 5795 2344  
jing01.han@hsbcqh.com.cn

Analyst, A-share Media & Internet Research  
Bruce Sun +86 10 5795 2357  
bruce.z.j.sun@hsbcqh.com.cn

Analyst, Head of A-share IT Software Research
Yiran Liu +86 10 5795 2349
yiran1.liu@hsbcqh.com.cn

Analyst, A-share IT Software Research  
Heng Zhang +86 10 5795 2384  
heng.zhang@hsbcqh.com.cn

## Transportation and Logistics

Analyst, Head of A-share Transportation & Logistics Research
David Wu +86 21 5066 2002
david.wu@hsbcqh.com.cn

Analyst, A-share Transportation & Logistics Research
William Sun +86 21 5066 2061
william.x.d.sun@hsbcqh.com.cn
"""
