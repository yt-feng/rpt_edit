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
- 已识别机构名：`国际清算银行`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
8. 文末自然承接未解问题，只写一段很短的轻 CTA。不要照抄固定话术，不要堆身份名单；语义可以参考但不必全塞：更多完整报告、中文摘要、KC评论和图表合集，会放进每日国际信源汇编。适合快速扫当天主流叙事，也方便后续追问和横向比较。。
9. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
10. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定套话。文末只保留 1-2 句，重点说“完整报告、中文摘要、KC评论和图表合集可以放回当天国际主线里继续看”，不要在正文中段出现。
- 严禁中段 CTA。正文中间不要出现“如果你从某些关键词搜到这里”“单篇文章只能解决一个切片”“我每天会把……”这类表达。

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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份国际清算银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## BIS Bulletin

## No 126

## Blockchain consensus mechanisms and fragmentation

Daniel Eidan, Jon Frost, Rudraksh Kansal, Ulf Lewrick, Sang Hyuk Lim and Tomasz Rybarczyk

BIS Bulletins are written by staff members of the Bank for International Settlements, and from time to time by other economists, and are published by the Bank. The papers are on subjects of topical interest and are technical in character. The views expressed in this publication are those of the authors and do not necessarily reflect the views of the BIS or its member central banks. The authors thank Matteo Aquilina, Sebastian Doerr, Pablo Hernández de Cos, Hyun Song Shin and Leanne Zhang for helpful comments and suggestions, and Nicola Faessler for administrative support.

The editors of the BIS Bulletin series are Gaston Gelos and Frank Smets.

This publication is available on the BIS website (www.bis.org).

# Blockchain consensus mechanisms and fragmentation

## Key takeaways

\- While all permissionless blockchains use token-based incentives to sustain honest validation, differences in how validator rewards, coordination and participation are structured lead to distinct equilibria and trade-offs between decentralisation, security and scalability.

\- These trade-offs underpin the emergence of multiple layer 1 networks and the expansion of layer 2 solutions, resulting in fragmentation of infrastructure, liquidity and assets across and within chains.

\- Tools to mitigate fragmentation – eg bridges and native multi-chain issuance – can reduce frictions, but they reintroduce new dependencies on trust, governance and operational resilience.

Public permissionless blockchains reduce reliance on centralised intermediaries by using decentralised, open infrastructure. Since the emergence of Bitcoin and Ethereum, activity built on distributed ledger technology (DLT) has expanded rapidly, spanning payments, decentralised finance and broader digital asset markets. Yet rather than converging on a single scalable infrastructure, a multitude of networks have arisen, fragmenting liquidity and diluting network effects. This Bulletin describes consensus mechanisms, asks why fragmentation occurs and explores what it means for market structure and resilience.

We examine how consensus mechanisms in permissionless blockchains balance decentralisation, security and scalability. $^{1}$ These choices shape validator participation, costs and coordination and generate distinct equilibria across different layer 1 (L1) blockchains. They have also driven the growth of layer 2 (L2) solutions that execute off-chain. L1s are the base networks that validate, process and finalise transactions directly in the shared ledger (on-chain). L2s, in turn, run on top of an L1 to enhance efficiency and scalability. We assess how this architecture fragments activity across and within chains, and how mitigation tools reduce frictions while introducing new trust, governance and operational dependencies. We conclude with implications for the potential role of permissionless blockchains as financial market infrastructures and for policy. The online appendix provides further details and a glossary.

## Consensus mechanisms: equilibria and trade-offs

Blockchains are append-only, shared databases (ledgers) maintained by validators who may not know or trust one another. In permissionless settings, anyone may attempt to validate or propose blocks; thus, incentives must align validators' private rewards with the public good of a coherent ledger (eg Budish (2025); Saleh (2021)). Participation depends on chain-specific requirements such as energy expenditure (work), minimum “locked” resources (stake), hardware capacity and voting or participation costs (eg fees for attestations or votes).

To sustain an honest equilibrium, validators must be compensated not only for operating costs but also for coordination risks arising from relying on other validators' participation. For example, Bitcoin miners incur energy and hardware costs to earn block rewards (proof of work). Ethereum validators must lock up their native token (Ether) and risk "slashing" penalties (loss of staked tokens) for deviating from predetermined rules (proof of stake). These and other incentives shape validator behaviour and determine whether consensus is maintained. Overly large sets of validators raise coordination costs, while excessive concentration increases the risk of disruption or control (Auer et al (2025)). Seen through this economic lens, blockchain consensus mechanisms are best understood as a range of token-incentivised equilibria (supported by "tokenomics"), in which validator behaviour depends on how rewards, penalties and participation costs are structured.

The trilemma associated with achieving consensus $^{1}$

Graph 1

![](images/ff7a032bda1f054dc2e93e3925d70d46c91c0469d2ea40a1cb2373783a6f73b0.jpg)  
$^{1}$ Triangle positions represent general tendencies of consensus mechanisms. The triangle's exact shape and placement may vary by blockchain implementation and configuration. $^{2}$ Proof of work (PoW) and proof of stake (PoS) support broad validator participation and thus decentralisation but can introduce scalability constraints in layer 1 networks. $^{3}$ Delegated proof of stake (DPoS) and proof of staked authority (PoSA) rely on smaller validator sets, which can enhance coordination efficiency and speed, but reflect different assumptions about validator participation and governance (see Table 1).

Sources: BIS (2022), Buterin (2021); authors' elaboration.

The “blockchain trilemma” highlights the trade-offs between decentralisation, security and scalability (Buterin (2021)). Consensus mechanisms position themselves differently along these dimensions (Graph 1). Allowing many validators to independently verify and confirm blocks supports decentralisation and security, but it also increases communication and verification costs. This limits throughput and raises latency (ie the time needed to confirm transactions), as in proof of work and proof of stake blockchains (red triangle). By contrast, designs that prioritise scalability achieve higher throughput and lower latency confirmations by reducing the number of validators or increasing hardware requirements, which narrows participation and weakens decentralisation, as in delegated proof of stake (eg Tron) or proof of staked authority (eg BNB Smart Chain) (blue triangle). These design choices reflect different economic equilibria rather than purely technical constraints.

Security considerations reinforce these trade-offs. When the value secured by a blockchain increases, the resources required to compromise the network – the attack cost – must also rise to deter malicious behaviour. In permissionless blockchains, these costs are borne by users through fees, congestion rents or dilution of tokens, implying that higher security standards come with tighter capacity constraints.

L1 networks feature distinct consensus mechanisms, shaping cost, latency and resilience (ie the ability to recover from disruptions). Their coexistence reflects competition among platforms to attract users with diverse needs and preferences. Early blockchains such as Bitcoin and Ethereum prioritised decentralisation and security through broad validator participation. This approach limits scalability: when demand for scarce block space rises, congestion intensifies and transaction fees increase, pushing out more price-sensitive users (Boissay et al (2022); Shin (2026)). Proof-of-stake systems can also face scalability constraints when security relies on large validator sets and frequent coordination. In response, newer L1s feature greater degrees of centralisation, such as smaller validator sets or higher hardware requirements, to raise throughput while lowering latency and fees (Table 1; Table A.1 in the online appendix).

No one size fits all: the plethora of layer 1 consensus mechanisms

<table><tr><td>Design [example]</td><td>Consensus mechanism</td><td>Trade-offs</td></tr><tr><td>Proof of work (PoW)[eg Bitcoin]</td><td>Participants expend computing power to add blocks by competing to solve cryptographic puzzles. The protocol adjusts difficulty to maintain steady block times as computing power changes.</td><td>Robust and decentralised, but throughput is intentionally low; energy consumption depends on hardware efficiency.</td></tr><tr><td>Proof of stake (PoS)[eg Ethereum]</td><td>Participants lock up (stake) native tokens and are selected to propose/verify blocks; misbehaviour such as proposing conflicting blocks or failing to attest as required can result in part of the stake being forfeited (slashing). Finality is achieved through many stakers attesting to the same block.</td><td>More efficient than PoW and supports rollups for scale, but still faces challenges to decentralisation, due to stake concentration risks, and coordination, due to consensus requiring a supermajority, which can also face scalability constraints.</td></tr><tr><td>Time ordering + BFT[eg Solana (PoH + PoS/Tower BFT)]</td><td>A cryptographic clock orders events, enabling faster agreement, followed by Byzantine fault tolerance (BFT), in which a supermajority of validators must agree before blocks are confirmed.</td><td>Low latency and high throughput, but hardware and bandwidth needs raise barriers to entry for validators, potentially limiting decentralisation.</td></tr><tr><td>Probabilistic sampling[eg Avalanche (Snow*)]</td><td>Nodes repeatedly poll small, random subsets of validators until the network converges, achieving fast finality with high probability.</td><td>Fast confirmation and flexible subnets, but security and liveness depend on sampling settings and the distribution of stake in the network.</td></tr><tr><td>Delegated validator sets[eg Tron (DPoS), BNB Smart Chain (PoSA)]</td><td>A small, elected or rotating group of validators produces blocks, with selection based on votes or delegated stake.</td><td>High throughput and quick finality but concentrates governance and validation power, which may reduce decentralisation.</td></tr></table>

BFT = Byzantine fault tolerance (a class of consensus methods that allow the system to function correctly even if some validators are faulty or malicious); PoH = proof of history (a cryptographic time source used to create a verifiable and consistent ordering of events); PoSA = proof of staked authority (a small, governance-approved validator set is selected based on a combination of stake and authority); Snow = Avalanche "Snow" family of probabilistic sampling protocols (eg Snowball, Snowman, which achieve consensus through repeated random sampling of small validator subsets); DPoS = delegated proof of stake (token holders delegate their stake to elect a limited, rotating set of validators who produce blocks on their behalf).

Source: authors' elaboration.

The diversity of networks separates users and liquidity across different, siloed networks. While Ethereum remains dominant in decentralised finance (DeFi), new L1s have expanded “horizontally” (Graph 2.A). Some have disappeared, eg Terra – which grew rapidly before failing spectacularly in 2022 – or have seen falling use, eg Fantom. Meanwhile, some networks have shifted towards modular architectures that split functions “vertically” across layers, providing separation of execution, settlement, data availability and sequencing across specialised layers (Graph 2.B). While specific design features vary (see Table A.2 in the online appendix), all L2 solutions work by processing transactions off-chain and writing results back to their base L1 for settlement and data availability. $^{2}$ This modularity raises efficiency when systems are robust and governance is clear. But it also creates distinct execution environments, each with its own transaction ordering, pricing and points of failure. L2s develop their own liquidity pools and governance mechanisms, adding vertical fragmentation to the patchwork of networks. Modularity thus redistributes, rather than eliminates, trade-offs across layers and introduces new governance and interoperability challenges.

Graph 2  
![](images/c7d63695dca1e253becb31a9bc6f81f1ba5ea58c3d9af2488becef7996b107e0.jpg)  
$^{1}$ Also includes L2 networks $^{2}$ L2s have been selected based on Token Terminal's methodology  
Sources: DefiLlama; Token Terminal; BIS; authors' calculations.

## Rising fragmentation across layer 1 (L1) and layer 2 (L2) networks

As a percentage of total value locked

## Mitigation mechanisms: benefits and trade-offs

Rising fragmentation across L1 and L2 networks has increased demand for mechanisms to connect assets, liquidity and applications across blockchains. These mitigation mechanisms aim to reduce frictions while preserving basic security and permissionless participation. But none eliminates fragmentation entirely. Instead, each shifts risks based on introducing new trust assumptions, governance arrangements and operational dependencies.

\- Bridges. Bridges transfer value across blockchains by locking an asset on one network and issuing (minting) a corresponding representation on another. Bridges can be implemented via custodial groups, guardian sets, relayers/oracles or on-chain light-client verification. Bridges are convenient for users, but they concentrate risk: compromised keys, falsified messages and bugs in smart contracts have led to large losses (eg USD 625 million in the March 2022 Ronin Network hack).

\- Native multi-chain issuance. Large issuers (eg of stablecoins) mint native versions of their tokens across several chains. While these tokens have identical names, they cannot be transferred across chains, and the same user has different wallet addresses on each chain (Graph 3.A). Each version typically trades in its own liquidity pool, deepening fragmentation and reliance on cross-chain arbitrageurs to mitigate price differences. This form of issuance shifts the operational burden from bridges to issuer coordination, treasury management and consistent governance across chains.

![](images/4023791b8a63ef60c425144c74d60f844b4f5e327f26c107605baab16ce557bb.jpg)

\- Shared layers for security, data and sequencing. Some ecosystems seek to reduce fragmentation in their own environments by providing shared services to multiple rollups. These include shared security, where a common pool of stake backs several L2s; shared data-availability layers that store and publish transaction data so that anyone can verify execution; and shared sequencers that determine transaction ordering across rollups. By coordinating execution and reducing delays, these shared layers can improve efficiency and limit the scope for rents. At the same time, they concentrate governance and operational risk in a small number of components that may become systemically relevant within an ecosystem.

\- Interoperability protocols (message-passing/state coordination). Rather than moving assets across blockchains, interoperability protocols allow chains to communicate by verified messages or proofs, enabling applications to act remotely (eg mint, redeem, settle). Some systems rely on cryptographic verification, where one blockchain verifies another's state on-chain. Others depend on external parties (eg relayers or oracles) to transmit messages. By keeping assets on their original chains, these designs reduce duplication and fragmentation but introduce new trust assumptions that on-chain verification rather than external intermediaries should minimise.

Rising fragmentation has fuelled rapid growth in the use of interoperability protocols in particular (Graph 3.B). Mitigation mechanisms could reduce some frictions but introduce new dependencies. As private sector experimentation continues, designs that combine verifiable security, transparent governance and clearly defined failure modes are more likely to emerge and to be more robust. At the same time, market participants may converge around a limited number of shared layers, warranting heightened attention to their operational resilience and governance arrangements.

Rising fragmentation has spurred demand for mitigation mechanisms

![](images/c42a5cfa1ae51de0c5a0b99be4640e1b83e22d69984e558e81154b280b98ae71.jpg)  
$^{1}$ The graph provides a stylised example of how a stablecoin (eg USDT) can be issued natively on multiple blockchains (eg Ethereum and Solana) by the issuer. While this improves availability across blockchains, tokens remain siloed and non-tradable across chains. Wallets are represented with a certain value of tokens (blue or red circles) and wallet address below them. Without mitigation mechanisms, sending stablecoins between wallets on different blockchains (eg Solana to Ethereum) may fail, risking permanent loss. $^{2}$ Axelar Network, Circle Cross-Chain Transfer Protocol (CCTP), Chainlink, deBridge, LayerZero. $^{3}$ Across, Allbridge Core, deBridge Liquidity Network (DLN), Everclear, Hop Protocol, Hyperbridge, Ren, Stargate, Synapse, zkSync Era Bridge.

Sources: Token Terminal; BIS; authors' elaboration.

## The prospect of permissionless blockchains as financial market infrastructures

Permissionless blockchains, including the applications built on them, are intended to provide general purpose financial infrastructure. In practice, however, binding economic constraints drive them towards specialisation and fragmentation. Consensus trade-offs generate multiple equilibria rather than convergence towards a single, unified infrastructure. Mitigation mechanisms designed to reconnect fragmented systems often reintroduce intermediaries and new dependencies. These dynamics limit the extent to which permissionless chains can naturally evolve into financial market infrastructures (FMIs) without additional governance and oversight. If permissionless blockchains are to support functions akin to FMIs, several policy dimensions warrant consideration:

\- Operational and cyber resilience. Diverse consensus mechanisms, validator incentives and governance models complicate risk assessment, incident response and recovery planning. While consolidation around common middleware can reduce fragmentation, it may create critical points of failure if a small number of shared services become critical to system functioning.

\- Regulatory perimeter and oversight. Shared sequencers, data-availability layers and cross-chain messaging services increasingly perform functions similar to those of traditional market infrastructures. As these components grow in scale, they may warrant governance arrangements, resilience standards and supervisory attention comparable to those applied to FMIs.

\- Competition versus standardisation. Open and interoperable standards can help reduce fragmentation while preserving innovation and competition among platforms. At the same time, cross-border coordination may be needed to mitigate operational risks and regulatory arbitrage, as activities span multiple jurisdictions and infrastructures.

Ultimately, the case for decentralisation is strongest in environments where trust is limited and reliance on central intermediaries is costly or impractical. Still, sustaining robust consensus equilibria at scale requires careful calibration of incentives, transparent governance and effective operational controls. Where permissionless systems take on more mainstream or infrastructure-like roles, the trade-offs inherent in their design should be made explicit and managed in ways that prioritise resilience and accountability, with particular scrutiny of shared components that could become systemically important.

## References

Auer, R, C Monnet and H S Shin (2025): "Distributed ledgers and the governance of money", Journal of Financial Economics, vol 167, 104026.

Bains, P (2025): "Blockchain consensus mechanisms: a primer for supervisors", IMF Working Papers, no 186.

Bank for International Settlements (BIS) (2022): "The future monetary system", Annual Economic Report 2022, Chapter III.

Boissay, F, G Cornelli, S Doerr and J Frost (2022): "Blockchain scalability and the fragmentation of crypto", BIS Bulletin, no 56.

Budish, E (2025): "Trust at scale: the economic limits of cryptocurrencies and blockchains", Quarterly Journal of Economics, vol 140, no 1.

Buterin, V (2021): "Why sharding is great: demystifying the technical properties", available at https://vitalik.eth.limo/general/2021/04/07/sharding.html.

Saleh, F (2021): "Blockchain without waste: proof-of-stake", Review of Financial Studies, vol 34, no 3.

Shin, H S (2026): "Tokenomics and blockchain fragmentation", BIS Working Papers, no 1335.
"""
