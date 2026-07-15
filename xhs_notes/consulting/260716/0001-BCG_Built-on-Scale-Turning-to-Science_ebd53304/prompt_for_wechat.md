你是麦肯锡/研究导读风格的微信公众号文章主笔，擅长用金字塔原理把报告内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给专业读者/产业决策者的报告导读。
- 长度：约 1200 字，整体以短导读为主，通常控制在 900-1200 个中文字符。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，只保留最关键的判断、证据和图表关系；篇幅到点就自然收住。
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
- 已识别机构名：`波士顿咨询`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
6. 禁止设置“该报告未解决的问题”“报告尚未回答”“研究留白”“开放问题”“报告局限”等独立小节；原报告明确写出的限制，只能在相关段落中用一句客观陈述带过。
7. 至少一个小节给出可复用的观察框架，但不要命名为“对读者的启发”。
8. 不要写任何 CTA、广告、扫码、社群、知识星球、网站、域名或关注引导；系统会在最结尾统一插入固定信息。
9. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
10. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.</p>`

【CTA 要求】
- 不要输出任何 CTA。不要写“加入社群”“扫码”“星球”“完整报告领取”“网站”“域名”“关注”“星标”“更多查看”等表达。
- 文末也不要写 CTA；系统会在最结尾统一插入固定信息。
- 正文中间不要出现“如果你从某些关键词搜到这里”“单篇文章只能解决一个切片”“我每天会把……”“这篇可以沿着……”这类表达。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释或提醒。
- 每条 `KC评论` 先说白话结论，再指出相关图表、假设或细分拆解中最容易被忽略的关系。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份波士顿咨询研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
![](images/d6b5024f9441be4b23dcd34075a4886c085cb0cc1cf10502686823599b97f4d0.jpg)

BUILT ON
SCALE,
TURNING
TO SCIENCE

INDIA'S PHARMA AND LIFE SCIENCES
INNOVATION OPPORTUNITY

JULY
2026

![](images/7095c7e064d3f91d92a8a23a89a6e4acdb36b24af41db20429367d134935c4a4.jpg)

## About Boston Consulting Group

Boston Consulting Group bridges the gap between ambition and outcomes for the world's leading companies and organizations. We are built for this era of unprecedented change — bringing strategic clarity rooted in over 60 years of deep domain knowledge, combined with applied AI shaped by our practitioners. BCG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com

## HEALTHKISIS

HealthKois (Fund III) is a \$300Mn India-focused healthcare innovation and impact fund. The fund is led by Charles Janssen, Ajay Mahipal, and Dr. Pinak Shrikhande, building on a strong track record of investing in highly innovative and scalable healthcare business models that deliver both superior financial returns and measurable social impact.

HealthKois focuses on high-growth, innovation-led companies across HealthTech, Biopharma, MedTech, Healthcare Delivery, and Climate Health, with a particular emphasis on AI-enabled healthcare models. The fund targets businesses operating at the intersection of technology, clinical excellence, and scalable delivery, addressing critical gaps in access, affordability, and quality of care in India and the broader Global South.

Guided by a disciplined investment strategy focused on capital efficiency and risk-adjusted returns, HealthKois seeks to build a concentrated portfolio of high-impact companies, balancing growth-stage scalability with exposure to cutting-edge innovation.

## FOREWORD

Several indicators suggest that innovation activity in Indian pharma and life sciences is increasing, though the shift remains early and uneven. Across laboratories, startups, and boardrooms, ambitions are shifting: from replication to origination, from process excellence to scientific discovery, and from serving global supply chains to building globally relevant pipelines. The early signs are clear. Over the past decade, India has seen a more than 4x increase in patent filings, \~1.5x growth in innovation pipeline assets, a \~1.6x rise in biotech startups, and a sharp increase in private capital directed toward healthcare innovation. These are not incremental changes — they signal the emergence of a new innovation trajectory.

This momentum is being supported by a convergence of enablers: increasing government funding, a more deliberate role for academia, evolving regulatory frameworks, and the build-out of shared research and manufacturing infrastructure. Together, these are beginning to create the foundations of a full-stack innovation ecosystem.

Yet, India's innovation story remains early and uneven. Much of the current momentum is concentrated in late-stage translation, while gaps persist in early-stage research, clinical execution, regulatory consistency, and access to patient capital. The challenge is no longer whether India can innovate — but whether it can do so at scale.

This report, developed jointly by BCG and HealthKois, maps India's pharma and life sciences innovation landscape with both rigor and realism. It highlights where India's structural advantages are strongest, where constraints remain, and what will be required to translate potential into global leadership.

India's innovation activity is gaining momentum, but its evolution into a sustained innovation engine is not assured. Realizing this potential will require focused execution, patient capital, and coordinated action across the ecosystem.

![](images/e9c0b1c2d7cd982a352b77bdacf60553546cd1f88fc5265d0e6989b45ecab8fd.jpg)  
Priyanka Aggarwal
Managing Director and Senior Partner, BCG
India and South East Asia Leader,
Healthcare Practice

![](images/9a780db9b50c0155149e29782dd29fe1916a0e60b2bbe3fd31eea0ea85ba54ea.jpg)  
Charles Janssen
Managing Partner,
HealthKois

## APPROACH

## We have collated inputs from a wide range of sources

## Primary sources

30+ in-depth interviews with biotech founders, pharma executives, investors, and ecosystem enablers across India and global markets

Insights from global experts across India, US, Europe, and emerging biotech hubs (China, Singapore)

Founder perspectives on capital, translation, regulatory, and infrastructure challenges captured through primary interviews

![](images/47d3ec4c531d39562cedd440566ee22d421a7a5cdf431ebaece33e491ba57edc.jpg)

Cross-section of stakeholders including startups (precision medicine, CGT, AI drug discovery), large pharma, CROs, incubators, and VCs

Detailed case studies of Indian innovation leaders (e.g., ImmunoACT, Glenmark, Zydus)

## Secondary sources

S&P Capital IQ

Clarivate

Citeline

Evaluate

Derwent Innovation

Inven

Crunchbase

Web of Science

PubMed

![](images/79309c4a74f8c5c929dcbd0cf04dbcd1a79c78b5b0aef0999c6eaabcec3c1b4f.jpg)

![](images/49d7d6b956c6decab82120eebc466ab8172ec815eb9bd5383f61dfb82c16af28.jpg)

## |

## Green shoots of innovation are emerging in Indian pharma and the momentum is building

India's pharma and life sciences sector is at an important turning point. Over the past decade, more than 10 novel drug assets have originated from India — spanning first-in-class NCEs, indigenous CAR-T therapies, and AI-discovered molecules. PE/VC investment has grown \~2.1x over the last five years to \$731Mn in FY26, while biotech startups have increased \~1.6x (from \~1,500 to \~2,400). Patent filings have risen more than 4x, and the innovation pipeline has expanded \~1.5x.

This shift is qualitative, not just quantitative: Indian companies are moving beyond generics and biosimilars to originate, license, and compete globally.

Yet India's scale in innovation remains limited. R&D spend stands at \~\$2–3Bn — a fraction of US (\~\$70–75Bn). Despite carrying \~15% of the global disease burden, India conducts just \~4% of global clinical trials. The opportunity ahead is significant, but so is the gap to be bridged.

## ||

## A full-stack innovation engine is beginning to take shape

This momentum is being enabled by four converging forces: \~\$5.0Bn in government funding, strengthening academia-industry linkages, an evolving regulatory framework, and the build-out of shared R&D and manufacturing infrastructure.

Early proof points of lab-to-market translation, including ImmunoACT's NexCAR19 and BIRSA 101 demonstrate that a full-stack innovation engine is beginning to take shape.

## 三

## Companies are pursuing multiple pathways to build competitive advantage

Indian companies are pursuing this opportunity through multiple innovation pathways: late-stage in-licensing, India-first validation before global expansion, global-first innovation monetized through out-licensing, academic spin-outs, and pure-play biotech platforms.

Landmark deals such as Glenmark's \$700Mn upfront licensing agreement with AbbVie and ImmunoACT's partnership with Cipla for Africa, signal growing global credibility.

## IV

## India's right to win is concentrated in three arenas

India's right to win is concentrated rather than broad. The strongest structural advantages lie in three arenas: cost-disruptive innovation that re-engineers advanced therapies for affordability at scale; India-specific biology and data that enable non-replicable precision medicine solutions; and science-driven platform innovation that leverages talent and cost efficiency. India's edge lies in combining cost, data, and talent — not in competing on frontier science alone.

## V

## Solving structural gaps will determine whether Indian pharma can realize full innovation potential

Structural constraints, however, remain significant. Access to early-stage, patient capital is limited with only \~10-15% VCs in India having deep pharma / biotech expertise, compared to \~60% in the US. Bench-to-bedside translation from academia remains weak. And execution gaps in clinical trial infrastructure, regulatory capacity, and domestic supply chains continue to slow innovation scale-up.

The next five years will determine whether India evolves into a global innovation originator or remains a sophisticated development hub. The conditions are in place — but the outcome is not guaranteed.

![](images/162e89ee919c76cd1c2d7e1b22aa61393a72370d46123ac75d1d2197397fde88.jpg)

## TABLE OF CONTENTS →

![](images/8b422020d71b023e4fa51ad7607c393137106b31f70c432457611ca3f8b4da5b.jpg)

## Green Shoots of Innovation Emerging in Indian Pharma

12-23 →

## Full-Stack Innovation Engine Coming Together

24-33 →

![](images/b06bc191ae91a1503eb90f9c741004a844c26ec3dfddd97732d0ce1f329bc6cf.jpg)

![](images/8773b8fc84ff8616687b7ad2a47d7304aa930b282e541c9d1f25e3ca44d1d5de.jpg)

| |

![](images/c3d9434cd86ba3c18563f45434553c8d90b6db507da5ed5ac201258fe0046a13.jpg)

## Multiple Pathways to Build Competitive Advantage

IV

34-41 →

India's Right to Win

42-49 →

## Structural Gaps and What Needs to Change

50-57 →

![](images/a0f4abe1aa0ad29487815cfef3454a2b26fc5094fb958c43d5326ffab29e4090.jpg)

## Green Shoots of Innovation Emerging in Indian Pharma

![](images/d1e96d35f622a5a163b7466df578e35d9161c5f0d98145697c0445f21a31f506.jpg)

## India's pharma journey: Established in scale, emerging in science

![](images/25ac1228455125e893e1dcc766885ecd09c438b326a8384b8758b584073187c4.jpg)

Next Frontier: Innovation

## Generics

$3^{rd}$ largest pharma producer (by volume)

\~40% of US generics demand served

\~20% of global generic supply (by volume)

Vaccines

\~60% of global vaccines produced

\~60% of UNICEF's vaccine demand

\~4Bn doses supplied globally \~\$0.8Bn exports; projected \~\$4.2Bn by 2030

\~15% of US biosimilars volume \~\$8Bn Indian CRDMO market (2024)

Growing at $\sim 13\%$ CAGR (vs $\sim 9\%$ global)

China+1 opportunity \$700Mn - \$1Bn annually

Source: Company annual reports; Analyst reports, BCG analysis

## Novel Drug Discovery

10+ novel assets originating from India in the last decade

Early global validation through out-licensing:

Peptris licensed to Revio

Ichnos / Glenmark licensed assets to AbbVie and Almirall

Funding momentum, policy push, and R&D incentives are accelerating the shift

Focus of this report

## India's pharma R&D spend remains nascent relative to global peers, leaving significant room for expansion

Total annual spend on Pharma R&D  
![](images/59e7ca4fb4a17720614e7d2798fe942d2dc41715c9d54891bd438ae83818924e.jpg)

![](images/55492a6c691877ad6dbd42f643a08dc4e23872bf70ad1495dd04cd6429d49f86.jpg)  
Europe  
\$55-60Bn

![](images/975b8cd10df4dc47227f53bb68a3b7e6f11282060c32b8d5268205444b78ba24.jpg)  
China  
\$15-20Bn

![](images/18df17e2380505156878ae00ce04a88de539f3d4752ca2528a64516d9afba6cd.jpg)

China has lower R&D expenditure than Europe and USA but accounts for 15-20% of the global novel drug pipeline, due to inherent advantages: Fully integrated pharma supply chain, relatively low labour costs vs. US, EU and government investments into R&D

Historically, pharma R&D investment in India has remained modest, reflecting limited support for early-stage and translational research and an industry mix skewed toward generics — both of which are now beginning to change

Source: EFPIA, The Pharmaceutical Industry in Figures 2025 (2023 pharma R&D spend; underlying sources: EFPIA member associations, PhRMA, JPMA, and China Statistical Yearbook); Federal Reserve Board, G.5A Annual (2023 average exchange rates used to convert EUR and RMB into USD). India estimate based on publicly disclosed R&D spend of listed Indian pharma / biopharma companies and public early-stage / translational research support

Innovation is increasingly happening ground-up in India — across CGT, mRNA, and immuno-oncology

## India remains significantly under-indexed vs global peers; \~1.6x growth in pharma / biotech startups over the last decade

India is significantly under-indexed in startups per capita vs peers

#pharma / biotech startups per capita

![](images/b22b38ee4fac4a629a90d775ffe3113bc68d7313a9705f88d32cc34b1643128f.jpg)  
1. Includes active startups, operating in the pharma and biotechnology segment, excluding hospitals, diagnostics, agriculture, digital apps, allied health sectors etc.
Source: Evaluate Pharma, Citeline, Quid, BCG analysis  
\~1.6x growth in number of pharma startups $^{1}$ in India from 2015–25...
# of biotech startups

## #

![](images/9018e46d2f3dc272b2ad58189bb99ad3ffaf1aff404f5d653c06ac9e9778542b.jpg)

## \$731Mn investment by PE/VC in pharma in FY26; >2x increase in last 5 years

## \~2.1x investment increase in pharma over last 5 years

![](images/063dbed1d7b05aefba408c752977a2e9683a96f2d7f750b46b93d0e067683753.jpg)

## Notable PE/VC deals focused on R&D (FY22–FY26)

<table><tr><td>Funding year</td><td>Company</td><td>Investors</td><td>Purpose of seeking investment</td><td>Latest deal size</td><td>Total funding raised</td></tr><tr><td>2026</td><td>Pandorum Technologies</td><td>Protons Corporate</td><td>Advance clinical development and scale manufacturing for regenerative medicine pipeline</td><td>$18Mn</td><td>$50Mn</td></tr><tr><td>2024</td><td>Immuneel Therapeutics</td><td>Taiba Middle East FZ, Eight Roads, True North, F-Prime</td><td>Advance clinical development of CAR-T product pipeline</td><td>$12Mn</td><td>$40Mn</td></tr><tr><td>2022</td><td>Bugworks</td><td>Lightrock, 3one4 Capital, UTEC</td><td>Clinical development of novel antibiotic BWC0977 + preclinical development for immuno-onco asset</td><td>$18Mn</td><td>$40Mn</td></tr></table>

Private capital inflow will serve as a great accelerator and will fill the gap of government funding in India

— CEO,
Life-sciences focused
investment firm

For every 100 VCs in the USA almost 60 of them will have experience in investing in biotech vs. 10 or 15 in India

— Founder, Biotech start-up

Note: \~2,900 companies related to 'pharma / life science / biotech' founded since 2000 were considered for the analysis. Companies were allowed to cluster based on (Business Descriptions) i.e., similar products, technology, customers, service offerings etc. Data based on disclosed investment amounts (USD) only. Last 5 Years data (01-Apr-2021 to 01-Apr-2026)
Source: Quid, Inc24, BCG analysis

\# of pharma patents originating from India $^{1}$

Patent grant rate of $\sim 40\%$ lags global peers

## >4x increase in pharma patents filed in India over the last decade, but grant rates and quality lag global peers

## Surge in patent applications in India

![](images/ed2b95febf64d50280dbceceb18edb3cca5659899522fecdb60318a0dc972361.jpg)  
Source: Derwent Innovation, Times of India, IP5 Statistics Report 2024, BCG analysis  
Note: Analysis based on \~12,800 patent families filed since 2015 in the "pharma / life science / biotech" domain by India (as priority country); patent family is a collection of individual patent records covering the same invention in multiple geographies

![](images/71abbbff102cbce24bdb5a19f8123210c855d9b0d08bdd43661b00637ba8d9bb.jpg)  
indicating gap in novelty and industrial use of the patents filed $^{2}$  
Stark contrast in grant rate across academia:

## \~60%+

## vs. 1-10%

Premier institutes like IITs, IISC

Private universities
like Galgotias,
Amity etc.

## India's pipeline is scaling and maturing, with clinical assets concentrated in oncology

\~1.5x growth in innovation pipeline of Indian firms in last 10 years

#pipeline assets

![](images/2fe000999113eb4af8eba918f3cd9fe74524e74b53cf3723ae13898fa708513b.jpg)  
Majority of clinical pipeline concentrated in Oncology
Clinical assets of Indian companies, by TA

![](images/5a253b21a9a8fe39714cdf4f9a98f806123ed04cc6545050e3ccbdc806cc9069.jpg)

![](images/fc518437b0ffc9032496b1e1cbe4235f1bc0338f1e9f70a3f36356ff87ffc938.jpg)

India's life sciences sector has emerged as a diversified life sciences innovation hub, with over 1,095 drug discovery programs across 195 companies, with nearly $86\%$ of programs focused on major diseases like oncology, infectious diseases etc. $^{1}$

— Managing Director, Differding Consulting

1. https://chemistry-europe.onlinelibrary.wiley.com/doi/10.1002/cmdc.70304
Source: Evaluate Pharma, Citeline, Quid, BCG analysis

![](images/48f751397060a194ecf4c117f4a0eb5ec403821fccf51b95641e8bad31e74645.jpg)

## India's innovation bets are concentrated in oncology and infectious diseases

## PE/VC capital deployed

% of investments
over last 5 years

2

## Patents

% of alive patent families $^{1}$ (2015-2024)

## Scientific literature

% of publications $^{2}$ (2020-2026)

1. Analysis based on \~4,300 patent families classified "Alive" of total \~12,800 patent families filed since 2015 in the "pharma / life science / biotech" domain by India (as priority country); patent family is a collection of individual patent records covering the same invention in multiple geographies; 2. Analysis based on \~8,600 publications with 10+ citations; Others includes: CROs, CDMOs, CRAMS companies etc. spanning across therapeutic areas
Source: Quid, Derwent Innovation, Inven; BCG analysis

![](images/b122d6af3b452e6093f12d7f3245aca55b7c8639443a94cd9172ed4fade0a91b.jpg)

Small molecules dominate India's innovation across every signal — patents, capital, and science

% of publications $^{2}$ (2020-2026)

1. Analysis based on \~4,300 patent families classified "Alive" of total \~12,800 patent families filed since 2015 in the "pharma / life science / biotech" domain by India (as priority country); patent family is a collection of individual patent records covering the same invention in multiple geographies; 2. Analysis based on \~8,600 publications with 10+ citations; Others includes: CROs, CDMOs, CRAMS companies etc. spanning across therapeutic areas
Source: Quid, Derwent Innovation, Inven, BCG analysis

![](images/ccbc7a64ef0e98f0733bed0bbc891893adb4088df7361141a720a0e3bf5dd5ff.jpg)

# A decade of Indian-origin innovation: 10+ novel drugs emerging from India, from first NCEs to CAR-T and AI-discovered drugs

## Commercially available

## Orchid Pharma Ltd.

## Zydus

Saroglitazar $^{1}$ 2013: First drug for NASH treatment in India; 2022: Phase II trials in US for PBC

Enmetazobactam
2024: First India-invented antibiotic to receive US FDA approval

## ImmunoACT

NexCAR19 de 2023: India's first indigenous CAR-T therapy, \~10x cheaper than imported CAR-Ts

Nafithromycin
2025: Novel macrolide antibiotic, granted QIDP designation by US FDA

![](images/ad787a2b9052a736d543110c0d30f98fe7e44c10b262b3befe7c

[中间内容因长度限制已省略]

 limited integration

\- Low adoption of standardized electronic health records (EHRs) and interoperability protocols

## Health Data Infrastructure

\- India's structured datasets remain significantly smaller vs. global benchmarks despite population scale
  - e.g., Genome India (\~10,000 genomes) vs. UK Biobank (\~500,000)

90% of our materials are imported from US, Europe, China...with lead times of 30-45 days

— Founder, Gene Therapy startup

Limited access to cleanroom infrastructure for startups

— Founder, Drug-delivery startup

Important to have insurance coverage for precision diagnostics to ensure patient accessibility

— Founder, Precision Medicines startup

India has population - scale advantages ...but needs ecosystem support to build assets like an Indian Biobank

— Founder, AI-drug discovery startup

## Key initiatives that will determine India's innovation decade

![](images/e0f68da34ace1f0572b64a5670abaee5da9f7ac4bb8c8bc44253fbb55600ff09.jpg)

## Build India's first generation of specialist biotech capital

\- Introduce targeted government schemes and tax incentives to catalyze industry investment in R&D

\- Increase direct public funding for early-stage and translational research

\- Expand funding for novel drug development programs

\- Harmonize grants across schemes and streamline application and disbursement processes

\- Ease access to external capital: single-window clearances, relaxed IPO / listing norms

• Strengthen investor confidence in the Indian biotech ecosystem

Without patient, specialist capital, deep biotech innovation will not scale

## Encourage academia – industry partnerships and collaboration

\- Prioritize 8–10 anchor institutions, revamp performance management, and deepen industry collaboration

\- Establish independent bodies to catalyze collaboration (e.g., A\*STAR, CTI)

\- Enable flexible IP ownership models to incentivize joint R&D

\- Expand research and incubation centers in universities with tech transfer and commercialization capabilities

\- Create aligned frameworks for academia-industry collaboration (objectives, timelines, success metrics)

Shift from publication-driven research → product-driven innovation

Source: BCG analysis, expert interviews, IPA-India Report: Catalyzing the Pharma innovation ecosystem in India

![](images/2dcd775352cff21c97821f7262ee4e0af071936e9d9add79632f53cc24f26d92.jpg)

## Create fast-track regulatory pathways for novel therapies

\- Build dedicated project management capacity for new drug applications to accelerate review timelines

\- Implement application tracking with defined milestones and timelines; enforce performance management

\- Establish specialized review teams for advanced modalities (CGT, mRNA, precision medicine)

\- Align drug approval processes with global standards to enable faster approvals

Shift from risk-averse regulation → innovation-enabling regulation

## Build domestic supply chain and enable market access

\- Inclusion of innovator drugs in public health schemes at appropriate price to increase access

\- Invest in domestic manufacturing of research-grade materials to reduce lead times

\- Expand insurance coverage for genomics, precision medicine, CGT

\- Pilot outcomes-based reimbursement models

Innovation will not scale without viable supply chains and domestic demand

## Bridging talent quality gap in R&D and innovation

\- Offer return fellowships, fast-track grants, and leadership roles to attract global talent

\- Embed hands-on lab training, GMP exposure, and industry-oriented curriculum within universities

\- Create structured mobility programs for researchers across academia, startups, and industry

\- Promote industry-sponsored programs at Masters and PhD levels

High-quality talent critical to move from being a low-cost execution hub to an innovation powerhouse

![](images/88d55515e679968ed24bc394767a868b9ebd2ddbfad9a6541dba4f6929234a84.jpg)

![](images/0a3a86c791cfd695d51fa5421e806f0ab8091dc591221c73cfc6481d06ccac68.jpg)

## ABOUT THE AUTHORS

## BCG

![](images/356ee4b3c942402c4d6bab35290436e8eb13bfe623793e23403af21acef2c754.jpg)

Priyanka Aggarwal
Managing Director and Senior Partner
Aggarwal.Priyanka@bcg.com

![](images/4e6df98977f765294938767f521e7fe6b1fba0cd3da0a7e0e2e30542c215770a.jpg)

Abhinav Anand
Partner
Anand.Abhinav@bcg.com

![](images/ffd1bbde7fc08ec79349698ade5b5a3ec0c5a4158fca3371e063771eb2704cfc.jpg)

Ananya Mitra
Project Leader
Mitra.Ananya@bcg.com

![](images/d691995ef883b0e31095091a6ae5323ee32dda751f44c68d27e3217c23a31525.jpg)

Ayushi Shukla
Senior Analyst - BCG Vantage
Shukla.Ayushi@bcg.com

## HealthKois

![](images/4417fcd6f2c9524bc5d5dee9c9172f7143de9356183dcb8b142d45b0466aec6b.jpg)

Charles Janssen
Managing Partner
Charles.Janssen@healthkois.com

![](images/efdc317f8a0332c54417044df3345fbdb08bc67ca8f541c392f4dd654a1d4bfe.jpg)

Ajay Mahipal
Partner
Ajay.Mahipal@healthkois.com

![](images/e5f6099054b834400f64a33b900c8f4b6a7908a68c83f8929c890b749a92377f.jpg)

Dr. Pinak Shrikhande
Partner
Pinak.Shrikhande@healthkois.com

![](images/579344cbb0632e90adb8a59c5d38b4f7eb4af80e9728104a6c803426458a59d9.jpg)

Shubham Jain
Vice President
Shubham.Jain@healthkois.com

![](images/805e4a3a30dc5f337c685273f191ca7f1dea898c4352790a1421fb784b292d1a.jpg)

Senior Associate
Kanika.Jain@healthkois.com

## ACKNOWLEDGMENTS

The authors thank and acknowledge the support provided by Mayank Kak from BCG in preparation of this report. Marketing Process: Nidhi Yadav, Bhumika Gupta, Simran Wadhwa. Design and Production: Saroj Singh, Ratna Soni, Subhradeep Basu, Abbasali Asamdi, Pavithran NS, Nitesh Tirkey, and Yashika M.

© Boston Consulting Group 2026. All rights reserved. 7/26

## BCG + HEALTHKOS
"""

【DeepSeek 交稿硬约束】
1. 全文只服务一个主判断。不要按原报告目录逐段摘要，也不要把多个结论平铺成清单。
2. 开头直接使用原文中最有辨识度的事实、数字、对比或矛盾切入；禁止用“在……背景下”“随着……”“近年来……”空泛起笔。
3. 正文至少使用三个原文锚点：一个可核验的数字或日期、一个具体主体/项目/制度名、一个比较或因果关系。判断必须紧挨证据，保留“可能、样本显示、报告认为”等限定词。
4. 句子长短要自然变化。大多数段落写 2-4 句，允许用一句短句收住；不要连续使用“报告指出、这意味着、换句话说、真正重要的是、值得注意的是”等模板转折。
5. KC评论只写一条具体、平白的解释或提醒，不能复述正文，不能提推广、原文领取、完整报告、读者行动或网站。
6. 禁止单独设置“该报告未解决的问题、报告尚未回答、研究留白、开放问题、报告局限、还需追问”等小节，也禁止用问句收尾。若原报告明确写了限制，只能在相关正文中用一句客观陈述自然带过。
7. 最后一段必须仍是实质内容或 KC评论。不要添加总结、结语、延伸阅读、继续阅读、关注引导、社群、扫码、网站或任何 CTA；系统会统一处理文末固定信息。
8. 不要虚构“我读完后”“我们采访了”等个人经历，不要故意口语化或加入情绪。人工编辑感来自具体证据、准确取舍和自然节奏。
9. 输出前自行核对：标题与导语不重复；每个小标题都是完整判断；没有元话语、推广语和未解问题栏目。只输出最终 Markdown，不输出核对过程。
