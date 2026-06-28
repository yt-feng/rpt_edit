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
## Cybersecurity in the Age of AI

Building a Synchronous BFSI Enterprise

MAY 2026

## BCG

Boston Consulting Group partners with leaders in business and society to tackle their most important challenges and capture their greatest opportunities. BCG was the pioneer in business strategy when it was founded in 1963. Today, we work closely with clients to embrace a transformational approach aimed at benefiting all stakeholders— empowering organizations to grow, build sustainable competitive advantage, and drive positive societal impact.

Our diverse, global teams bring deep industry and functional expertise and a range of perspectives that question the status quo and spark change. BCG delivers solutions through leading-edge management consulting, technology and design, and corporate and digital ventures. We work in a uniquely collaborative model across the firm and throughout all levels of the client organization, fueled by the goal of helping our clients thrive and enabling them to make the world a better place.

## DSCI PROMOTING DATA PROTECTION

Data Security Council of India (DSCI) is a not-for-profit, think tank on data protection, cyber security and critical technologies in India, setup by Nasscom, committed towards making the cyberspace safe, secure and trusted by establishing best practices, standards and initiatives in cyber security and privacy. DSCI works together with the Government, law enforcement agencies, defense, industry sectors including IT-BPM, BFSI, CII, Telecom, and other think tanks for public advocacy, thought leadership, capacity building and outreach initiatives.

<table><tr><td colspan="2">Cybersecurity in the Age of AI</td></tr><tr><td colspan="2">Foreword</td></tr><tr><td><img src="images/c137cbb453ed7cd909fe56dfbb35a81c3f47b3b1c93e9bbec49f548c97ada15c.jpg"/></td><td>Vinayak GodseChief Executive Officer, Data Security Council of India</td></tr></table>

Cybersecurity in the Age of AI

## Foreword

![](images/cea1a5cd2390ca5867250307b56ced1ab2e880717d87a16a84f9f25eb98c1b69.jpg)

## Nisha Bachani

Managing Director and Partner, Boston Consulting Group

India's BFSI sector has been at the forefront of digital and technology adoption. Digital channels now mediate majority of customer interactions across banking, insurance and capital markets, and the operational transformation in this sector has seen material advancements in the last decade. Few sectors operate at this scale, velocity, and with this density of interconnections.

Into this landscape, artificial intelligence has arrived as the defining force and is reshaping cybersecurity fundamentally on both sides of the line. It is putting sophisticated defense capabilities within reach of any institution that chooses to adopt them, while simultaneously collapsing the cost, skill and time required to mount sophisticated attacks. Exploit windows that once ran into months are being measured in days. For the first time, the offensive side of the cyber curve is scaling faster than the defensive side, and adversaries are deploying the same frontier capabilities

Indian BFSI faces a sharper version of this challenge than almost any peer – due to the nature of data, complex web of related parties, impact of breach and potential losses that will emerge. Attack intensity is materially higher in Indian BFSI than in global markets, the ecosystem is more interconnected, and risks are rising fast - the opportunity cost and losses due to cyber attacks now materially outweigh the investments and effort in planning the defense. While AI adoption is picking pace, AI-specific security controls still have some ground to cover. The strategy cannot be more compliance, it has to be stronger capabilities, better governance and controls.

We are delighted to launch this report as a product of the partnership between BCG and the Data Security Council of India. It draws on a survey of Indian and Global CISOs, structured conversations with senior leaders across BFSI, and BCG's broader experience in cyber and financial services.

Our study shows Indian BFSI's technical foundations have strengthened, but the threat environment has outpaced them. Cyber leaders remain deliberate about many initiatives and rightly maintain human-in-the-loop governance even as AI-native defense becomes essential. However, few structural gaps still remain - spanning risk quantification with a business & customer impact lens, third-party linked resilience, recovery readiness, talent and others. These risks need to be addressed in a coordinated rather than siloed way. The new operating model will be a lot more “synchronous” with Cyber defense aligned across stakeholders and not just limited to CISO/CIO.

For boards and chief executives, investments in this space are going to be more crucial than ever before and will differentiate the leaders & build greater customer confidence. Institutions that move decisively over the next twelve to eighteen months will define how the rest of the decade plays out, and will be positioned to lead in an AI-driven financial system.

We are grateful to the industry leaders who gave us their valuable inputs in shaping these perspectives and to DSCI for partnering to bring this to light. We look forward to your engagement on this and hope you find it an insightful read!

<table><tr><td colspan="2">Cybersecurity in the Age of AI</td></tr><tr><td colspan="2">Executive Summary (I/II)</td></tr><tr><td>Indian BFSI is at a cyber inflection point – and the gap is widening faster than most organizations are recognizing.</td><td rowspan="2">76% of Indian BFSI CISOs rank AI-enabled attacks as a top-4 priority.69% expect significant impact within 12 months. However, no single control area in our survey crossed the 50% confidence threshold for readiness against an AI-enabled breach.71% of Indian BFSI firms have already reached AI-assisted SOC maturity or higher43% of Indian CISOs say attackers are already moving faster than their defenses – but only 19% have increased cyber budgets by more than 10% to respond</td></tr><tr><td>India’s BFSI is attacked 1.6x more intensely than the global average. Cyber incidents have more than doubled in four years – 1.4 million (2021) to 2.9 million (2025). Breach costs are rising +7% YoY to USD 2.5 million and at the same time, mean time to contain a breach in India is at 263 days and still climbing. The mid-tier Indian BFSI sits in the most exposed position: they have digitized aggressively, are deeply interconnected, but their cyber investments are much smaller than larger players</td></tr><tr><td>The biggest shift is on the attackers’ side. AI has rewritten the economics of offense:Time to exploit: 745 days → 44 days (-94%)Cost of attack: down by 70%+</td><td>To be truly ready, every BFSI institution must now simultaneously curb AI-powered attacks, deploy AI for defense, and secure its own AI systems – as one unified effort.</td></tr><tr><td>Our survey of 40+ Indian BFSI CISOs and multiple direct interactions with the relevant stakeholders revealed a strong intent to action on the AI-oriented cybersecurity agenda, but with some gaps in policy and execution</td><td>AI, however, is only the accelerant. Foundational cyber resilience in Indian BFSI is finding it difficult to keep pace with the digital scale of operations</td></tr></table>

## Executive Summary (II/II)

<table><tr><td>Indian BFSI has built strong digital foundations. The institutions that act decisively on the remaining gaps over the next 12–18 months will define the sector&#x27;s resilience posture for the rest of the decade.
Our survey identified four areas where targeted action can deliver the highest risk-buydown:
• Investment headroom exists: 60%+ Indian BFSI currently directs less than 10% of IT spend to cyber - need to review cyber defense capabilities to ensure exposures are well-managed and within risk appetite
• Third-party risk is manageable with the right model: 55% cite it as a top concern, yet only 49% already have mature controls. Currently the gap is governance and continuity
• AI governance needs a boost: Only 29% have both an AI security owner and a defined policy
The path forward is not more controls – it is synchronicity. Indian BFSI&#x27;s next cyber operating model must shift from a security-function agenda to a synchronized resilience system across five fronts:</td><td>Business: Cyber priorities aligned with business priorities and risk – not an afterthought
Cross-functional teams: Business, Risk, Legal, IT and Security operating as one accountable unit – not serial handoffs
Vendors: Third parties governed as extensions of the enterprise, not managed annually at procurement
Humans: The attack surface inside and outside the bank defended as a single discipline – insider risk and customer fraud as one program
Ecosystem: Threat intelligence shared across peers, regulators and industry bodies – not captured in siloes
Attackers already operate as a coordinated economy. The institutions that match that coordination – synchronizing defense across all five fronts – will be the ones that turn cyber resilience into competitive advantage. Those that don&#x27;t will remain permanently reactive, defending yesterday&#x27;s perimeter against tomorrow&#x27;s threat.</td></tr></table>

## Table of contents

The Cybersecurity Imperative Scaling Threats and elevating 'Unknowns'

![](images/126a1c6735ae9fd769331247f2886ccf12cfe21637284be316ff2e5903405c69.jpg)

Reflection on Our Position
Voice of Global and Indian CISOs

Page 22

![](images/4bb0dbcea45bcc93f7fbd278aa3f6428cffc08f1ff793ea592cda2512124a692.jpg)

Path Forward
Five Fronts where Indian BFSI must Synchronize for a stronger Cyber Defense

## The Cybersecurity Imperative Scaling Threats and elevating 'Unknowns'

1. UK NCSC (April 2026)
Source: Information Security Incorporated, BCG analysis

Frontier AI can attempt a full enterprise network attack for \~USD 80 $^{1}$

## Cyber attacks have evolved over last 4 decades and AI is accelerating the sophistication

![](images/0adb5ef5bad852df29002bdb4d13c54e4599f4707af679cbcdac825928383291.jpg)

## India BFSI faces a steep challenge on managing cyber attack intensity

<table><tr><td></td><td></td><td></td><td>Global</td><td>India</td></tr><tr><td>Intensity</td><td colspan="2">Cyber attacks per organization (2025)1</td><td>1x</td><td>1.6x</td></tr><tr><td rowspan="3">Impact</td><td colspan="2">YoY change in average cost of a data breach (2024-25)2</td><td>-9% (to USD 4.4 Mn)</td><td>+7% (to USD 2.5 Mn)</td></tr><tr><td colspan="2">Mean time to identify and contain a data breach (March 2025)2</td><td>241 days</td><td>263 days</td></tr><tr><td colspan="2">Share of total attacks in BFSI sector (2025)3,4</td><td>27%</td><td>17%</td></tr><tr><td rowspan="2">Preparedness</td><td colspan="2">Percentage of BFSI leaders who consider AI related attacks as a top issue (2026)5,6</td><td>61%</td><td>76%</td></tr><tr><td colspan="2">Percentage of BFSI organizations investing &gt; 10% of IT spend on cybersecurity (2025)5,6</td><td>76%</td><td>38%</td></tr></table>

Source: 1. Check Point Cyber Security Report 2026 (Jan '25 – Dec'25); 2. IBM Cost of a Data Breach Report 2025 (Apr'24 – Mar'25); 3. IBM X-Force Threat Intelligence Index; 4. DSCI x Seqrite India Cyber Threat Report 2025/6; 5. BCG x GLG Global CISO Survey 2026, Banking and Securities + Insurance excl. health subset (N=53); 6. BCG x DSCI India CISO Survey (N=42); BCG analysis

## Cyber incidents in India have doubled in last 4 years BFSI has seen significant breaches

## Cyber incidents handled by CERT-In per year doubled in last four years in India (Mn / year) $^{1}$

![](images/2e2aaad12f4e85a28e37e6981c962c34bfdc6356eb0f31f5304345e88574d8ca.jpg)

![](images/059ee4274223cc19f3d7158b0441b58c7ca40254345d4819a43fdc6f7225dd0f.jpg)

## Few Indian BFSI breaches in last 24 months

## Cloud misconfiguration exposes client data at top-3 retail brokers (February 2025) $^{4}$

Environment managed by a leading global cloud services provider was compromised, exposing client data on the dark web; huge erosion in market cap post event.

![](images/91d9219b393e6b391d0fbdea4e0fa382952ca8773a4b623868398aa81df92097.jpg)

## Ransomware on shared tech vendor freezes 300 banks (July 2024) $^{4}$

A ransomware group exploited an unpatched DevOps automation server at a shared technology service provider, disrupting payment services for approximately 300 cooperative and regional rural banks.

![](images/0fa3f1798c7720bb01e6350803871c027a2c6dd5efeb9c4b7a92655b220f792a.jpg)

## Sophisticated heist drains INR 2K Cr from one of India's largest crypto exchange (July 2024) $^{5}$

A multi-sig wallet was breached in a single coordinated attack, attributed to a state-sponsored threat actor, with funds laundered globally through crypto mixers.

The mid-tier in Indian BFSI — mid-size private banks, small finance banks, NBFCs, urban cooperative banks — sits in the most exposed position: they have digitized aggressively (and therefore have valuable data and payment rails) and are deeply interconnected through shared infrastructure. But their cyber budgets are a fraction of the large players

Note: CERT-In: Indian Computer Emergency Response Team

1. Cert-In Annual Report 2021, 2022, 2023, 2024, 2025; 3. Business Standard ( $3^{rd}$ March 2025); 4. Deccan Herald ( $31^{st}$ July 2024); 5. Business Today ( $14^{th}$ January 2025);

Source: Press releases and articles; BCG analysis

## 8 structural forces are raising BFSI cyber risk in India (I/II) Span across an increased attack surface, AI driven threats and other structural issues

![](images/a0ea137cf98a6adda485d1503d05ff50287569243ff6afd57b2b2867fee959e8.jpg)

## Digital Scale and Expanding Attack Surface

India's financial attack surface has expanded faster than any comparable economy. Over 1 billion Indians are now online, with 660 million smartphone users, a base that nearly doubled in six years.

![](images/4457c9239d779ef8e3c072f9156db99c24c3809bd7129cab6ec878603daf2534.jpg)

## Surge in AI Driven Threats

AI tools have collapsed the barrier to entry for cyber attacks. Malicious LLMs enable low-cost, highly targeted attacks. The attacker advantage has shifted: speed of exploitation now outpaces speed of defense.

![](images/90bc8983d90bf24213bf24025a48c5484935ab481641b3bca04dc2723157a310.jpg)

## Excessive Third Party Reliance

Indian financial institutions increasingly rely on shared 3 $^{rd}$ party technology providers for core operations.

A single vendor compromise can cascade across the entire chain.

![](images/ac4eacadae5a2d389958b0ab1fae458c8f2b817087f2516386faa7f7ac40d7c4.jpg)

## Legacy Systems

Legacy core systems running on extended patch cycles are structurally unable to respond to shorter exploit timelines.

Legacy systems typically are more exposed as well.

## >1 Bn

Internet users in India by end-2025 $^{1}$

## 90%+

Reduction in Time-to-Exploit with emergence of Al $^{2}$

![](images/48aae95aae8415bd2c6e84b898ed25ccc177980d2841bc9b6721678f28ffa779.jpg)

Reduction in cost of attacks with Al $^{3}$

## 50%+

Of BFSI leaders report 3 $^{rd}$ party and supply chain risk management remains ad hoc or reactive $^{4}$

## <15%

Of BFSI CISOs report high confidence in managing unpatchable legacy and embedded systems $^{4}$

1. DataReportal Digital 2026: India; 2. Flashpoint 2026 Global Threat Intelligence Report; 3. Proxied on decrease in annual subscription cost of WormGPT; 4. BCG x DSCI India CISO Survey 2026 (N=42)
Source: BCG analysis

# 8 structural forces are raising BFSI cyber risk in India (II/II) Span across an increased attack surface, AI driven threats and other structural issues

![](images/74f93e52b832614994842ce6ccf7170e63917db422f73b9286dbdde3ff941946.jpg)

## Talent Scarcity

There is a growing shortage of cybersecurity talent in both India and globally, driven not only by insufficient workforce capacity but also by a widening gap between skills and expertise needed.

![](images/20458337ff8de33dde5245c85030350db10fbdfb40794ebb65559ef64c9980e9.jpg)

## Limited Leadership Focus and Investment

Cyber is governed as an IT and compliance issue at several Indian financial institutions, rather than as an enterprise-wide risk.

Indian BFSI's cyber spend lags global peers, reinforcing the gap.

![](images/2fcc6727d70b689c9b7e290c242bc188a310a2464b178851bfdccb825f4ef8da.jpg)

## Software Visibility Bottleneck

With 70–90% of modern software built on open-source libraries, vendor sub-dependencies and legacy systems, even mature Financial institutions find it difficult to maintain a complete, real-time inventory of what they run.

![](images/51fd287253c2363dc72e866e48bbacaae13f02e0cb99f2dfb01a28b3875765d1.jpg)

## Geopolitical Landscape

State-aligned threat groups and hacktivist networks escalate sharply around every flashpoint, and BFSI sits adjacent to the government and infrastructure they target.

## 90%+

Of organizations in India report cybersecurity talent gaps $^{1}$

## 40%+

BFSI CXOs report board oversight, cyber risk appetite measurement and reporting is ad hoc or reactive $^{2}$

## <17%

Of BFSI CISOs report high confidence visibility into third party and open-source dependency exposure $^{2}$

## 1.5 Mn+

Cyber attacks on Indian websites in a single fortnight after the May 2025 geopolitical flashpoint $^{3}$

1. DSCI Report – Indian Cybersecurity Product Landscape 3.0.; 2. BCG x DSCI India CISO Survey 2026 (N=42); 3. Road of Sindoor Report by Maharashtra Cyber Police Source: BCG analysis

## Vulnerability disclosures have grown 1.5x since 2024 with AI increasing the threat

Vulnerability disclosures have doubled since 2020, with the steepest acceleration in the last 24 months $^{1}$

![](images/a46bb45612758e36d47e62d6f63f49ad7dd1210a22a1085057239487aa5dc352.jpg)

![](images/c3a33c602604ed7870571ac447419870f34e2c292572142f37d7214f0ba6debe.jpg)

of these vulnerabilities could be exploited without authentication, significantly increasing the attack surface $^{1}$

## According to Indian CXOs, threat from AI-led attacks is real and fast evolving $^{2}$

![](images/2011f0c02effd3b2cd12641a5ca66daa1357298b63d6f8fd6232e2d1a404ec2e.jpg)

Of Indian BFSI CISOs rank AI-enabled attacks as a top-4 priority for 2026

![](images/a39f14b8416e9ea326da1af55900784390753fc4b2b89e4051c45c98ec2a39a8.jpg)

Believe AI-powered threats will have significant impact in next 12 months

![](images/a644056260ee86159e2cb651135fee737c8097462272c24952067eb1e79a05e5.jpg)

## Third party and supply chain risks are now “first party” risks – AI increasing the potential risk of breach and impact

Supply chain risk is a growing priority for BFSIs....

\- Soph

[中间内容因长度限制已省略]

ecurity in the Age of AI

## Authors

Boston Consulting Group

Nisha Bachani

Managing Director & Partner
Bachani.Nisha@bcg.com

![](images/ca69245a1bbef6511875724bbc0068af4b7d81b39fda6b212f7edff77eee575a.jpg)

Ayush Kanwar
Partner
Kanwar.Ayush@bcg.com

![](images/a00c9cc0700d5df8dbe38f06332d11cc6a9432e76854f2c22dc9f0ad7065251d.jpg)

## Anand Raman

Senior Analyst
Raman2.Anand@bcg.com

![](images/d0b0455e6f76ded4f37bde9924e8ed5aab6fc9b379ad2223dfede4238f00602f.jpg)

## Vijay Pasupathinathan

Principal Pasupathinathan.Vijay@bcg.com

![](images/988f0259b0442e5e1017883e0e23f8592377b76a4928f922f993baef868ad7b6.jpg)

Hardik Jain
Principal
Jain.Hardik@bcg.com

![](images/c18ca1038a0a34af99bebf4bd546b8eea3da3802f53b33d44cb4a6e165b4b865.jpg)

Anirudh Gupta
Senior Associate
Kanwar.Ayush@bcg.com

![](images/dbc820cd3828d0b7fbd21c4ac1bba7403cb175a4ae12bed2825db07346f110da.jpg)

## Data Security Council of India

Vinayak Godse CEO

![](images/bc58e7c0a134a798698479dd9eec5c54260b74b69cea4aed4da357107e89a22b.jpg)

Neha Mishra
Lead – Insights and Research

Priya Sharma Senior Associate, Strategy & Insights,

![](images/8244df04bb32bcf00012c15b118f87ca578aa65ef3795a96133e2f5f6a69aaa9.jpg)

# Acknowledgements

We would like to express our sincere gratitude to the teams at BCG and DSCI for their invaluable contributions, collaboration, and support in developing this report. We also thank the CISOs and CXOs who filled the survey and gave their valuable insights in face-to-face interviews. Their expertise, guidance, research support, and efforts across content development, analytics, marketing, editorial review, and production were instrumental in bringing this publication to completion.

Strategic Guidance

Research and Analytical Support

Editorial and Legal Review

Vanessa Lyon
Managing Director and Senior Partner, BCG

Design and Production

Alex Asen
Senior Director - Cyber and Digital Risk, BCG Vantage

Eric Gregoire
Global Media Relations
Director, BCG

Sujatha Moraes
Creative Manager,
BCG Design Studios

Sean Mitchell
Senior Manager,
BCG Vantage

Massimiliano Merlini
Managing Director and
Senior Partner, BCG

Amit Ghosh
Associate Director Marketing and Communications Data Security Council of India

Eshita Bhargava
Senior Designer,
BCG Design Studios

Karan Bhardwaj
Manager, BCG Vantage

Courtney Fears
Senior Legal Counsel,
BCG

Or Klier
Managing Director and
Partner, BCG

Jasper Christy  
Senior Designer, BCG Design Studios

Bhumika Gupta
Team Leader – Marketing,
BCG

Nadya Bartol  
Platinion Managing Director, BCG

Nihar Mehta
Designer,
BCG Design Studios

Jose Qian
Asia Pacific Managing Editor,
BCG

Preet Nair
Designer,
BCG Design Studios

Sanya Jain
Marketing Graduate Trainee,
BCG

The images across the report have been generated using AI

## Disclaimer

This document has been prepared in good faith on the basis of information available at the date of publication without any independent verification. BCG and DSCI ('we/us') do not guarantee or make any representation or warranty as to the accuracy, reliability or completeness, of the information in this document nor its usefulness in achieving any purpose. Readers are responsible for assessing the relevance and accuracy of the content of this document. It is unreasonable for any party to rely on this document for any purpose, and we will not be liable for any loss, damage, cost, or expense incurred or arising by reason of any person using or relying on information in this document. To the fullest extent permitted by law (and except to the extent otherwise agreed in a signed writing), we shall have no liability whatsoever to any party, and any person using this document hereby waives any rights and claims it may have at any time against BCG and DSCI with regard to the document. Receipt and review of this document shall be deemed agreement with and consideration for the foregoing. This document is based on a primary qualitative and quantitative research. BCG does not provide legal, accounting, or tax advice. Parties are responsible for obtaining independent advice concerning these matters. This advice may affect the guidance in the document. Further, we have made no undertaking to update the document after the date hereof, notwithstanding that such information may become outdated or inaccurate. BCG does not provide fairness opinions or valuations of market transactions, and this document should not be relied on or construed as such. Further, any evaluations, projected market information, and conclusions contained in this document are based upon standard valuation methodologies, are not definitive forecasts, and are not guaranteed by us. We have used data from various sources and assumptions provided to us from other sources. We have not independently verified the data and assumptions from these sources used in these analyses. Changes in the underlying data or operating assumptions will clearly impact the analyses and conclusions. This document is not intended to make or influence any recommendation and should not be construed as such by the reader or any other entity. This document does not purport to represent the views of the companies mentioned in the document. Reference herein to any specific commercial product, process, or service by trade name, trademark, manufacturer, or otherwise, does not necessarily constitute or imply its endorsement, recommendation, or favoring by us. No part of this report can be reproduced for commercial purposes either on paper or electronic media without permission. Any reproduction, distribution, or reuse of this material requires prior consent from DSCI and, where applicable, Boston Consulting Group.

## BCG | DSCI PROMOTING DATA PROTECTION
"""
