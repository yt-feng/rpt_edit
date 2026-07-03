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
FINANCIAL INSTITUTIONS
BCG FLAGSHIP REPORT

# The Future of Digital Assets

May 2026

By Chris Schmid, Inderpreet Batra, and Roy Choudhury

![](images/add6a81de6a32132ed367ab132ca62a345c72c0d02706c5ed70c5360fb7af5fd.jpg)

## Acknowledgements

Since its inception, the BCG Digital Asset Working Group has been an invaluable source of domain expertise, insight generation, and problem-solving on the most complex topics, as well as a strong foundation of collaboration driven by a shared commitment to delivering excellence to our global clients.

This flagship report would not have been possible without this collective depth of knowledge and the group's extensive work across the ecosystem, including Global Systemically Important Banks (G-SIBs), regional banks, fintechs, industry associations, and other key stakeholders.

We would like to thank the following individuals for their valuable contributions:

Markus Ampenberger
Managing Director and Partner
Munich

Carlos Bravo
Director BCG Vantage
Madrid

Frédéric Brugère
Managing Director and Partner
Paris

Kaj Burchardi
Platinion Managing Director
Amsterdam

David Chan
Managing Director and Partner
Hong Kong

João Paulo Curado
Managing Director and Partner
São Paulo

Assia Gardiner
Partner and Associate Director
Zurich

Sander van Loosbroek
Platinion Director
Amsterdam

Kunal Jhanji
Managing Director and Partner
London

Dr. Laurin Karl Frommann
Managing Director and Partner
Zurich

Yue Hong Zhang
Managing Director and Partner
Hong Kong

Bernhard Gehra
Managing Director and Senior Partner
New York

Dr. Bernhard Kronfellner
Partner and Associate Director
Vienna

Tibor Mérey
Managing Director and Partner
Vienna

Arjun Nath
Partner and Associate Director
Toronto

Alexander Paddington
Managing Director and Partner
New York

Urs Rahne
Managing Director and Partner
Berlin

Christian N. Schmid
Managing Director and Senior Partner
Munich

Humza Samad
Partner
London

Gonzalo Troncoso Fuentes
Managing Director and Partner
Santiago

Pascal Vogt
Partner and Director
Cologne

Max Zevin
Managing Director and Partner
New York

Ivana Zupa
Managing Director and Partner
Zurich

New York, May 18, 2026
Chris Schmid, Inderpreet Batra, Roy Choudhury

![](images/b8b075dcf1472a34893e8f0b67c9d8d24186f160bc8bb017fbbc03fcc88e1438.jpg)

## Preface

## There is almost no day without another headline and report to be published about digital assets.

This report aims at something different: providing an in-depth reading for financial services executives wanting to learn about the concepts, contentions, threats, and opportunities that this new technology brings to financial markets.

Rather than presenting a linear narrative, this report is structured to help decision-makers engage with digital assets from multiple vantage points. It starts with a Framing chapter that establishes a common language—defining the three core domains of digital assets (digital money, tokenized RWAs, and crypto) and sizing their current and potential economic relevance. This chapter is intended as a foundation: readers less familiar with the space may choose to start there, while others can use it as a reference point.

The report then moves into a BoD View, focusing on the strategic questions that matter under uncertainty. This includes the core benefits and controversies of digital assets, the structural tensions they introduce, and a set of four forward-looking scenarios. These scenarios are not predictions, but rather tools to think through how market structure, regulation, and adoption could evolve—and what that means for banks’ revenue pools, balance sheets, and competitive positioning.

Building on this, the Executive Committee View translates these scenarios into concrete implications across businesses. It examines digital money, tokenized assets, and crypto in more detail, and then walks through impacts by business line—from personal and corporate banking to asset management and capital markets. This chapter also provides a view on regulation across jurisdictions, helping readers understand how uneven policy development shapes strategic choices.

The report then shifts into functional deep dives. The CRO View explores how risk changes in programmable, always-on markets, highlighting new control points and governance requirements. The CTO View focuses on how to build and scale digital asset capabilities, outlining key architectural decisions, operating model implications, and sequencing considerations.

Finally, the report concludes with a Ten-Step Guide to Managing Digital Assets, offering a structured set of actions for leadership teams. This section synthesizes the insights into a ten-step guide designed to help banks navigate uncertainty, define their strategic posture, and execute in a disciplined way.

Readers can approach this report sequentially or selectively, depending on their role and priorities. Board members may focus on board-level perspectives and “So What,” executive teams on the Executive Committee View and functional leaders on CRO View and CTO View. Taken together, the chapters are designed to provide not just an understanding of digital assets, but also a framework for acting on them.

Although we encourage executives to take the time for an in-depth reading, the following is a seven-page bullet-style summary about “what you need to know,” followed by the detailed report.

## Contents

04 Preface
06 Report Essentials on Seven Pages
13 Framing: Digital Asset Classes and Market Sizing
Digital Money
Digital Real-World Assets (RWAs)
Crypto
16 BoD View: Digital Asset Benefits, Controversies, and Scenarios
The Promise of Digital Assets
Why Digital Assets Are Controversial: System-Level Fault Lines
Four Scenarios for Financial Market Decision-Makers
Potential Financial Outcomes and Inflection Points
Implications for BoD Decision-Making
24 Executive Committee View: Understanding and Acting on Digital Assets
Digital Money and a World of Contentions
Digital RWA: A Capital Markets Transformation
A Word on Crypto: Where the Volumes Are Today
Banking Business Lines: One Bank, Many Outcomes
Digital Asset Regulation: One World, Many Regimes
48 CRO View: Risk Control in Programmable, Always-On Markets
Digital Assets Change How Risk Arises and Propagates
Risks Become More Interdependent and Infrastructure-Driven
Digital Assets Create New Risks
A Deeper View: Control Points Matter

## Contents

From Rulebooks to Supervisory Practice
From Policy to Performance
What CROs Should Do Now

57 CTO View: Making It Happen
Five Core Technology Controversies in DLT for Financial Services
Seven Principles for CTO Strategies
Create a Capability Map
Operating Model Implications
Build vs. Partner vs. Buy: The Need for a Clear Decision Framework
How Should CTOs Think About Sequencing?

63 So What? A Ten-Step Guide to Managing Digital Assets

65 About the Authors

# The Future of Digital Assets

# One-page summary followed by a summary of six

## BOTTOM LINE

Digital assets should now be treated as a strategic infrastructure transition for banks, not as a niche innovation theme. The CEO task is not to predict the winning rail, but to keep the bank relevant, trusted, and in control as money, assets, and settlement become programmable.

## What is happening

Crypto is already a \~\$3 trillion asset class and stablecoins are \~\$300 billion. Digital real-world assets (RWAs) are still small today, but are also the category with the biggest structural relevance for banking over the next decade.

## Why it matters for banks

If digital assets scale quickly, pressure on transaction banking, Net Interest Income (NII), and legacy post-trade economics can become material. The risk is less about one product and more about losing client interface, balance-sheet relevance, and control of critical infrastructure.

## What management should do

Move from experimentation to strategic positioning. Quantify what is at risk, pick the ambition level by business line, and build the no-regret capabilities that preserve optionality: wallet/custody, risk controls, and a bank-grade digital asset platform.

## Numbers that matter

\- Today's market is dominated by crypto (\~\$3 trillion) and stablecoins (\~\$300 billion); Digital RWAs remain much smaller (\~\$30 billion publicly visible today).

\- In progressive scenarios, Digital RWAs could reach roughly 16% of global investable assets by 2035, varying by asset class.

\- In the report's rapid digital expansion scenario, banks could face \~10% smaller balance sheets, \~14% lower revenues, and \~30% lower profits by 2035 versus the no-digital-asset case.

## CEO implications now

\- This is a strategic and governance issue, not just an innovation issue.

\- The bank must decide where it wants to own the client interface, where it is willing to partner, and where it cannot afford to be a price taker.

\- The right near-term objective is optionality with discipline: learn early and scale only where economics and controls support it.

# Framing Digital Assets: Market Sizing and Growth

The three categories look similar from the outside, but their economics and strategic relevance are different.

<table><tr><td>ASSET CLASS</td><td>SIZE TODAY</td><td>WHERE VALUE IS CREATED TODAY</td><td>WHY IT MATTERS FOR A BANK</td></tr><tr><td>Crypto:Bitcoin, Ethereum, others</td><td>~$3 trillion market cap at the end of 2025; ~$90 billion revenue pool</td><td>Trading, derivatives, custody, prime services, staking</td><td>Commercially meaningful now, but cyclical and volatile. Banks should treat it as a client-driven revenue pool, not as the core transformation story.</td></tr><tr><td>Digital money:Stablecoins, Tokenized Deposits, Central Bank Digital Currency (CBDC)</td><td>Stablecoins ~$300 billion; tokenized deposits and CBDC still early</td><td>Crypto cash leg, store-of-value in emerging markets (EMs), early B2B and cross-border payments</td><td>This is the most immediate threat to payments, foreign exchange (FX), and deposit economics. The end state is likely coexistence across stablecoins, tokenized deposits, and CBDCs.</td></tr><tr><td>Digital Real-World Assets (RWAs):Tokenized securities, commodities, alternatives</td><td>~$30 billion visible today, mostly money market fund (MMF), strongest long-term growth potential</td><td>Repo, collateral mobility, tokenized funds, money market instruments</td><td>This is where banking relevance is deepest because tokenization can re-architect issuance, settlement, custody, servicing, and collateral usage.</td></tr></table>

## READ THE CURRENT MARKET CORRECTLY

Stablecoins matter, but today, roughly two-thirds of supply is currently tied to crypto trading and related DeFi activity; around a quarter is store-of-value demand (namely USD in EMs); only around a tenth is linked to real-economy payments, and growing fast. This means the strategic story is not yet mass retail disruption, but rather a transition from crypto-native use to broader payment, treasury, and settlement use cases.

## What is likely to scale first

\- Digital money for wholesale settlement, treasury, and cross-border use cases where legacy rails are slow, expensive, or fragmented.

\- Tokenized funds, repo, collateral, and short-dated fixed income where faster settlement and lower operational friction have clear economics.

\- Selective crypto services where client demand already exists and banks can add trust, governance, and integration.

## Four conditions for scale

\- Customer adoption: real user demand must move beyond pilots and niche segments.

\- Policy and regulation: clarity is increasingly the catalyst for institutional scale-up.

\- Technology infrastructure: banks need production-grade, not experimental, Distributed Ledger Technology (DLT) capabilities.

\- Interoperability: without it, tokenized money and tokenized assets remain fragmented point solutions.

## CEO TAKEAWAY

The long-term prize is not crypto trading; it is control of the next generation of money movement, asset servicing, and market infrastructure. The question is where your bank wants to participate in that stack.

# Threats and Opportunities for Banks

# The strategic answer is not “threat or opportunity”; it is both. Value shifts away from pure intermediation and toward interface, orchestration, and infrastructure.

## WHAT IS AT RISK STRUCTURALLY

Three forces work against incumbent banking economics: tokenization reduces the need for intermediaries; value shifts from banks toward non-bank platforms and asset managers; and parallel operation of legacy and tokenized rails creates temporary cost duplication.

<table><tr><td>BUSINESS LINE</td><td>MAIN THREAT</td><td>MOST RELEVANT OPPORTUNITY</td><td>ILLUSTRATIVE UPSIDE FROM THE REPORT</td></tr><tr><td>Retail &amp; wealth</td><td>Deposit leakage and client-interface disintermediation as wallets and crypto platforms become the primary interface for digitally native clients.</td><td>Win back the interface through bank wallets, custody, advice, on-/off-ramping, and lending against digital assets.</td><td>For an average G-SIB, ~$340 million-$600 million annual revenue upside as off-bank digital assets grow.</td></tr><tr><td>Corporate banking</td><td>Pressure on cross-border payments, FX spreads, and liquidity float as programmable money becomes a credible alternative rail.</td><td>Offer programmable treasury, stablecoin-enabled cross-border payments, and banking services for crypto-native firms.</td><td>For an average G-SIB, ~$200 million-$600 million annual revenue upside.</td></tr><tr><td>Asset management</td><td>Higher fee transparency and easier product comparison can compress unit margins over time.</td><td>Tokenized funds and alternatives can increase asset capture, improve mix, and expand distribution efficiency.</td><td>A $2 trillion asset manager could unlock roughly 15%-30% revenue uplift, or ~$1.2 billion-$2.5 billion.</td></tr><tr><td>Capital markets</td><td>Legacy post-trade, float, and servicing economics compress as settlement accelerates and automation increases.</td><td>Tokenized issuance, collateral mobility, repo, digital custody, and faster settlement improve capital velocity and return on equity (RoE).</td><td>Trading businesses could see up to ~4% RoE uplift, translating to ~$1 billion+ profit upside for an average G-SIB.</td></tr></table>

## What the scenarios imply

\- The future may be privately led, institution led, fragmented, or partially constrained. The key point is not to pick one end state with confidence, but rather to remain relevant across more than one plausible future.

\- The most exposed pools are transaction banking and NII. The largest upside pools are asset management, trading/collateral, and the trusted client interface.

## Strategic watch-outs

\- Do not confuse low current volume in Digital RWAs with low strategic significance. The timing is uncertain, but the direction of travel is meaningful.

\- Do not issue products without a network strategy. Tokenized deposits or Digital RWAs without interoperability risk becoming costly features, not strategic assets.

# Board of Director-Level Discussion on Strategy

Boards should frame digital assets as an issue of market structure, control points, and strategic optionality—not as a narrow product question.

## Principle 1: Neutrality is not neutral

Every decision—including not acting on digital assets—embeds a bet on future market structure, regulation, and the balance between private platforms and public institutions.

## Principle 2: Optimize for optionality

Boards should distinguish between no-regret capabilities, option-value investments, and franchise-threatening bets. The objective is not certainty; it is relevance across multiple plausible futures.

## Principle 3: Ambition must match capability

A bold narrative without governance, controls, and architecture will destroy credibility. The bank's digital asset posture must be consistent with its real risk appetite and delivery capacity.

<table><tr><td>BUSINESS LINE</td><td>MAIN THREAT</td></tr><tr><td>Where to compete</td><td>Decide which layers must be controlled by the bank: client interface, product layer, or infrastructure/control plane. Do not allow uncoordinated pilots to define strategy by default.</td></tr><tr><td>How bold to be</td><td>Choose an ambition archetype: defensive integrator, scaled participant, or infrastructure shaper. Different businesses can sit in different archetypes, but the choice must be explicit.</td></tr><tr><td>How to source capabilities</td><td>Be clear about where to build, where to partner, and where to buy. In DLT transitions, early clarity on this question prevents duplicated spend and lock-in.</td></tr><tr><td>How fast to move</td><td>Select the right posture by business line: first mover where standards and client relevance are at stake; fast follower where economics are attractive but uncertainty remains high.</td></tr><tr><td>How to govern</td><td>Assign clear executive accountability, set a board review cadence, and require quantified updates on revenues at risk, opportunities, capital effects, and control readiness.</td></tr></table>

## THE CORE STRATEGIC TENSION FOR A BOARD

Should the bank defend the existing franchise incrementally or reshape parts of it before others do? In infrastructure transitions, the biggest mistake is often not moving too early; it is moving too late, after the interface and standards have already shifted elsewhere.

# Risk and Technology Management

# In programmable, always-on markets, control points matter more than policy statements do. Scale will be limited by control effectiveness, not by ambition.

## Risk priorities for management

\- Anti-money laundering (AML) and sanctions become flow based and wallet centric. Screening only direct counterparties is not enough; banks need ongoing monitoring of wallet behavior and indirect exposure.

\- Custody is a first-order control risk. Legal responsibility, technical control of keys, and authority to move or freeze assets must align.

\- Smart contracts should be governed like high-risk models: tested before deployment, monitored continuously, and equipped with explicit pause, upgrade, or intervention authority.

\- Shared infrastructure creates new concentration risk. Bridges, cloud providers, node operators, analytics vendors, and common protocols can become systemic dependencies.

\- Always-on markets compress crisis timelines. Escalation rights, kill switches, and incident playbooks must work in real time, not only in paper form.

## Technology design principles

\- Treat DLT as infrastructure, not as a collection of isolated business pilots. Reuse platform capab

[中间内容因长度限制已省略]

smart contract governance, and AML execution can be growth constraints if underbuilt. CEOs should ensure the following:

\- Clear intervention authority (kill switches, escalation rights)

\- Wallet-based AML and sanctions monitoring capabilities

\- Explicit governance over key management and smart contract upgrades

In digital asset markets, your ability to scale revenue is constrained by the design of your control framework, not just by demand or capital. In traditional banking, controls sit around the product. In programmable markets, controls sit inside the product. That changes everything.

## 6. Architect for optionality, not prediction

CTOs must grapple with multi-chain coexistence and regulatory reversibility. CEOs must require:

\- modular, ledger-agnostic architecture,

\- vendor exit paths, and

\- configurable compliance controls.

Strategic lock-in to a single chain, issuer, or ecosystem converts uncertainty into structural dependency risk.

## 7. Sequence with discipline

Avoid two common failure modes: isolated pilots and uncontrolled scaling. A disciplined sequencing approach:

\- 0–12 months. Establish unified DLT governance, offer secure client wallets, join at least one institutional network, and clarify stablecoin/tokenized deposit posture.

\- 12–36 months. Scale custody and collateral use cases, integrate tokenized assets into wealth mandates, and industrialize first capital markets workflows.

\- 3–5 years. Optimize balance sheet usage through tokenized collateral and rationalize legacy post-trade infrastructure where scale permits.

Speed matters, but architectural integrity matters more.

## 8. Align governance with automation speed

Digital asset execution compresses risk timelines. CEOs should:

\- assign a single accountable executive sponsor (CEO/COO-level),

• centralize DLT platform ownership, and

\- institute a board-level review cadence tied to scenario monitoring.

Governance fragmentation in programmable markets fosters risk propagation.

## 9. Choose your ambition archetype

Three viable models emerge from this report:

\- Defensive integrator protects client interface and focus on custody and orchestration.

\- Scaled participant competes on issuance, collateral, and prime while managing balance sheet exposures.

\- Infrastructure shaper invests to influence settlement networks and interoperability standards.

Drift between models is the highest-risk posture. If a bank does not deliberately choose its digital asset ambition and incrementally adds activities without strategic coherence, it accumulates risk faster than revenue. Drift is not neutral; it is unmanaged exposure.

## 10. Revisit core assumptions annually

The evolution of digital assets will be path dependent. CEOs should annually revisit five interrogatories:

\- Where does irrelevance risk now exceed execution risk?

\- Which regulatory or interoperability assumptions could break our strategy?

\- Are we infrastructure price takers or price setters?

\- Does our liquidity model hold-in atomic settlement stress?

\- Are we preserving optionality or accumulating hidden lock-in?

Digital assets are not a product cycle; they are a structural transition akin to the telecom dual-rail migration discussed earlier. Banks will operate legacy and tokenized infrastructure in parallel for years. Margins on traditional intermediation will compress, but new value pools will emerge around orchestration, programmable servicing, and balance-sheet velocity.

The CEO mandate is clear: do not attempt to predict the winning rail. Instead, ensure that you remain systemically relevant regardless of which rail scales. Strategic clarity, quantified economics, disciplined architecture, and governance that matches automation speed will determine which banks shape the next settlement stack—and which merely connect to it.

## About the Authors

![](images/af5d720593c53cb7d2732c1b0c7f85b08d20d834c2a51b9604dd446391aaadf8.jpg)

Chris Schmid is a Senior Partner and Global Leader. He leads BCG's Global Banking business. You may contact him by email at schmid.christian@bcg.com.

![](images/af9815935e26f1b156557715b0442cff8ba691a29b0d22413073dfd06dd02d2b.jpg)

Roy Choudhury is a Senior Partner and Regional Leader. He leads BCG's CIB business in North America. You may contact him by email at choudhury.roy@bcg.com.

![](images/61b8facb9dcd52e2ed7988a5d7b0c7691af85af73e3bccdb3c14f7be0e5ebf6d.jpg)

Inderpreet Batra is a Senior Partner and Global Leader. He leads BCG's Payments and Fintech business. You may contact him by email at batra.inderpreet@bcg.com.

## For Further Contact

If you would like to discuss this report, please contact the authors.

## BCG

Boston Consulting Group partners with leaders in business and society to tackle their most important challenges and capture their greatest opportunities. BCG was the pioneer in business strategy when it was founded in 1963. Today, we work closely with clients to embrace a transformational approach aimed at benefiting all stakeholders—empowering organizations to grow, build sustainable competitive advantage, and drive positive societal impact.

Our diverse, global teams bring deep industry and functional expertise and a range of perspectives that question the status quo and spark change. BCG delivers solutions through leading-edge management consulting, technology and design, and corporate and digital ventures. We work in a uniquely collaborative model across the firm and throughout all levels of the client organization, fueled by the goal of helping our clients thrive and enabling them to make the world a better place.

![](images/33ba8eed6213e5d6aa854c48ade4a2af13dccb9c3bd4f0827cbc9db27c6cfb63.jpg)
"""
