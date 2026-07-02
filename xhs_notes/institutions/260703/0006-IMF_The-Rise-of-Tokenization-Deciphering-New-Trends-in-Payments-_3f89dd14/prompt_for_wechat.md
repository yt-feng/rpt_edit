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
- 已识别机构名：`IMF`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份IMF研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
![](images/d9e30c55a229e7643202de9004d53cb3222821bc530cebc5b2f3ebc2e9d24628.jpg)

IMF

NOTES

# The Rise of Tokenization Deciphering New Trends in Payments and Asset Tokenization

Tobias Adrian, Yaiza Cabedo, and Tommaso Mancini-Griffoli

NOTE/2026/006

# ©2026 International Monetary Fund

# The Rise of Tokenization: Deciphering New Trends in Payments and Asset Tokenization

NOTE/2026/006

Tobias Adrian, Yaiza Cabedo, and Tommaso Mancini-Griffoli $^{1}$

DISCLAIMER: The IMF Notes Series aims to quickly disseminate succinct IMF analysis on critical economic issues to member countries and the broader policy community. The views expressed in IMF Notes are those of the author(s), although they do not necessarily represent the views of the IMF, or its Executive Board, or its Management.

ABSTRACT: Tokenization—the process of issuing and transferring assets on blockchain-based infrastructures—is gaining momentum in financial markets and will have significant implications for market structure, risk management, and financial stability. This Note identifies emerging trends in tokenized finance and examines the policy questions they raise. It analyzes developments in blockchain infrastructure design, architectural configurations allowing for interoperability, and the evolving role of the public sector. The Note also assesses tokenized deposits and stablecoins as alternative forms of monetary liabilities, highlighting trade-offs related to distribution models, governance, and loss absorption. The analysis highlights and clarifies policy-relevant questions to guide discussions in a rapidly evolving field.

RECOMMENDED CITATION: Adrian, Tobias, Yaiza Cabedo, and Tommaso Mancini-Griffoli. 2026. “The Rise of Tokenization: Deciphering New Trends in Payments and Asset Tokenization.” IMF Note 2026/006, International Monetary Fund, Washington, DC.

Publication orders may be placed online, by fax, or through the mail:

International Monetary Fund, Publications Services
P.O. Box 92780, Washington, DC 20090, USA
Tel.: (202) 623-7430 Fax: (202) 623-7201
Email: publications@imf.org
bookstore.IMF.org
elibrary.IMF.org

## Contents

Introduction .... 4
Trends in the Infrastructure Layer .... 6
Technology, Governance, and Infrastructure.... 6
Architecture Design.... 9
The Role of the Public Sector .... 11
Trends in the Asset Layer.... 12
Tokenized Deposits.... 12
Stablecoins.... 14
Tokenized Central Bank Reserves .... 17
Implications of Tokenized Architecture for Financial Market Infrastructures.... 18
Conclusions .... 19
Acronyms and Glossary .... 21
References .... 22

# The Rise of Tokenization

Tobias Adrian, Yaiza Cabedo, and Tommaso Mancini-Griffoli $^{2}$

July 2026

Tokenization—the process of issuing and transferring assets on blockchain-based infrastructures—is gaining momentum in financial markets and will have significant implications for market structure, risk management, and financial stability. This Note identifies emerging trends in tokenized finance and examines the policy questions they raise. It analyzes developments in blockchain infrastructure design, architectural configurations allowing for interoperability, and the evolving role of the public sector. The Note also assesses tokenized deposits and stablecoins as alternative forms of monetary liabilities, highlighting trade-offs related to distribution models, governance, and loss absorption. The analysis highlights and clarifies policy-relevant questions to guide discussions in a rapidly evolving field.

## Introduction

Tokenization has become a prominent concept and an area of active exploration in financial services. $^{3}$ At its most basic level, it involves issuing assets, recording ownership, and transacting on a blockchain. $^{4}$ Although the concept appears straightforward, its implications for market structure, risk management, inclusion, and public policy can be more complex and far-reaching. In an environment characterized by rapid technological change, broad experimentation, and frequent announcements of new products and services, it can be difficult for policymakers to identify which developments are durable and where policy attention should focus.

This Note extracts and explains the emerging trends that appear most relevant for policymakers. It does not take a normative stance on policy choices. Instead, it highlights implications and trade-offs to inform and guide policy dialogue and decision making. In a rapidly evolving landscape, definitive answers are often premature. The Note is divided into three parts. The first surveys recent developments in infrastructure with an emphasis on governance models, interoperability, and the role of the public sector. The second surveys innovations in financial assets, namely tokenized deposits, stablecoins, and tokenized central bank reserves. The last part considers the possible evolution of financial market infrastructures in particular, drawing on the discussions and concepts introduced in the first two parts of this note. The focus remains on frontier developments and novel questions affecting policy.

The landscape relevant to tokenization is broad. A wide range of assets can be tokenized, from commodities and real estate to financial instruments (Agur and others 2025; Aldasoro and others 2023). This Note focuses primarily on money and other financial assets, including securities and derivatives. Money is typically the instrument used to acquire financial assets such as equities or bonds, whereas securities and derivatives also serve as backing for new forms of quasi money, most notably stablecoins.

To structure the analysis, the Note relies on a simple three-layer framework applicable to both traditional and tokenized financial architectures $^{5}$ . At the bottom of the stack lies the infrastructure layer, where transactions are settled. This layer encompasses the rails and rules governing finance, including databases, platforms, systems, operators, and third-party service providers behind the scenes. In traditional finance, this layer includes messaging providers such as Swift and settlement infrastructures such as TARGET2 operated by the European Central Bank (ECB). In a tokenized environment, the infrastructure layer is formed by the blockchain and the rules governing how ownership and transactions are validated.

Above the infrastructure layer sits the asset layer, which represents the value held by end users—money and other financial assets associated with issuers and their balance sheets. In a tokenized environment, the asset layer includes stablecoins, tokenized deposits, central bank digital currency (CBDC), tokenized securities, and tokenized money market funds, for instance.

At the top of the stack is the services layer, comprising functions such as asset management, fraud detection, customer due diligence, and transaction monitoring. In a tokenized environment, the services layer consists of applications such as wallets and exchanges.

Traditionally, money issuance and wholesale payments have been provided through vertically integrated models over the layers of the technology stack. Money was issued by commercial banks by way of deposits, and the same banks offered services and ran much of the settlement infrastructure (central banks underpinned the system with their own infrastructure ensuring final settlement). More recently, initiatives such as Banking-as-a-Service, including open banking, have introduced greater flexibility primarily at the services layer. $^{6}$ Figure 1 compares the models of traditional commercial banks and the tokenized stack.

Figure 1. Today's Commercial Bank Money Model and the Tokenization Stack  
![](images/f4230c61b2b4021860733663a4755a0acbd1eeeeb01e472b24687eaa5233fced.jpg)  
Source: Authors' elaboration.  
Note: ACH = automated clearing house; DLT = distributed ledger technology; FPS = fast payments system; RTGS = real-time gross settlement system; QR = quick response.

Tokenization enables new configurations. Issuers of liabilities no longer need to build and operate proprietary infrastructures, and service providers can develop applications independently on shared infrastructure. For example, stablecoins are accessed through third-party wallets at the services layer, issued by entities responsible for backing at the asset layer, and settled on public permissionless infrastructures operated by a multitude of participants. Decoupling asset issuance from infrastructure operation can reduce the costs of

building and maintaining proprietary systems and allows each layer of the stack to evolve more flexibly than in traditional vertically integrated models.

This Note first examines trends in the infrastructure layer, before turning to developments at the asset layer. It does not analyze the services layer in detail, though it reflects how services are evolving as a result of changes at lower layers of the technology stack. As background, Box 1 provides a concise overview of tokenization and its core features, summarizing the key technological and governance characteristics that underpin tokenized systems.

## Box 1. Features of Tokenization

\- Tokenization involves issuing assets, or representations of assets, on a blockchain.

\- Tokenization benefits derive from the core features of blockchain technology and smart contracts.

\- A blockchain functions as a shared ledger that applies standardized transaction rules and can provide a transparent and consistent record compared with conventional databases. By synchronizing multiple copies of the ledger to maintain a single state of transactions, it can reduce reconciliation and reporting costs.

\- Smart contracts consist of code-based instructions stored on the blockchain that execute predefined rules automatically when a transaction triggers them by calling the smart contract function.

\- Composability refers to the ability of smart contracts to interact with and call functions of other smart contracts, so that a single transaction can trigger a chain of sequential contract executions.

\- Atomicity ensures that when a transaction triggers multiple smart contract calls, the protocol treats them as a single indivisible unit. The system records all resulting state changes only if every step executes successfully; if any step fails, it reverts the entire sequence, leaving no partial execution.

\- Blockchain governance defines how participants validate transactions, upgrade protocols, and adjust system parameters. In tokenized markets, clear and pre-agreed governance rules strengthen trust through transparency, while distributed validation and oversight enhance operational resilience by reducing single points of failure.

$^{1}$ There have been discussions about non-distributed ledger technology tokenization, but it is commonly agreed that the tokenization in financial markets involves distributed ledger technology. See BIS-CPMI (2024) and Cabedo and others (2026).

## Trends in the Infrastructure Layer

The infrastructure layer raises three essential questions. The first is about the operation and governance of infrastructure. Will it be open to the public, with anyone able to validate transactions, or will permissions be closely managed? The second is about the resulting architecture and specifically the arrangements that would allow interoperability of assets across chains. Third, what could be the role for the public sector? $^{7}$

## Technology, Governance, and Infrastructure

Market participants, including banks, fintechs, and traditional service providers, seem to have gone back and forth between permissionless and permissioned infrastructure architectures. On the one hand, relatively new entrants such as Circle, Coinbase, and Stripe began by favoring permissionless and decentralized ledgers such as Ethereum and Solana. These firms have touted the benefits of a global, always-available, stable, standardized, and relatively cheap infrastructure with distributed and transparent governance. Recent developments suggest that a more nuanced or hybrid view is emerging. These companies are now building their own proprietary ledgers or centralizing elements in their architecture to optimize costs, speed, and privacy—in a race to control infrastructure and related services.

On the other hand, banks have traditionally favored and explored permissioned ledgers operated by themselves or by a consortium of known entities for their own purposes and clients. They have emphasized privacy, scalability, accountability, and predictable costs. However, several institutions have recently announced at least a partial shift to permissionless ledgers for issuance and transactions, such as JP Morgan (2026), UBS (FintechNewsCH 2025), and Societe Generale (SG Forge 2026). For instance, JP Morgan Coin represents bank deposits and is now deployed on Coinbase's permissionless chain, Base. UBS, alongside other financial institutions, has joined Tempo's testnet, an infrastructure that aspires to validate payments and explore settlement and reconciliation capabilities on a permissionless chain. Regulated financial institutions are leveraging the flexibility of permissionless networks, which allow them to incorporate permission controls such as whitelisting to govern who can hold and transact tokens, creating what could be called hybrid governance models. In addition, some banks appear interested in issuing stablecoins on permissionless blockchains, such as Société Générale's EUR denominated stablecoin CoinVertible issued on Ethereum, Solana, Stellar, and the XRP Ledger.

Another notable development, pointing instead toward permissioned ledgers, is the entry of Swift in the market for blockchain-based infrastructure. Swift is a global provider of messaging services with links to a large share of the world's financial institutions, and it already operates the network that token-native firms are seeking to build. Swift is now exploring an open-source, blockchain-based and Ethereum Virtual Machine (EVM)—compatible infrastructure. $^{8}$ Swift will operate the ledger, providing orchestration of transaction workflows, validation of funding commitments, and coordination of interbank processes. Banks will operate their own environments and retain full authority over keys, assets, funding, and settlement through real-time gross settlement system (RTGS) systems, correspondent banking relationships, and other agreed mechanisms between participants. This new infrastructure will support programmable corporate payment flows, foreign exchange Payment versus Payment (PvP), and cash movements for securities transactions (Swift 2026). Given Swift's size and network, this infrastructure has the potential to offer a truly global infrastructure.

Another significant development is the announcement by a group of large US banks including JPMorgan Chase, Bank of America, Citigroup, and Wells Fargo of a new network to clear tokenized deposits (Heeb and Huang 2026). It will be operated by The Clearing House (TCH), the payments network owned by the same banks that today clears nearly \$2 trillion dollars per day. From early 2027, the new network will help banks clear their tokenized deposits, with settlement taking place in central bank reserves.

Which arrangement will eventually dominate is an open question that will depend on various factors including whether the technology supporting public permissionless blockchains will overcome hurdles such as scalability and privacy. $^{9, 10}$ For identity and compliance, techniques like zero-knowledge proofs (such as zk-SNARKs) allow users to check if they meet certain requirements, for instance verifying they are not on a sanctions list, without revealing personal data. $^{11}$ These systems are now in early production use. To protect sensitive financial information such as account balances and transaction amounts, many different projects are developing encryption methods that allow computations on encrypted data, meaning that transactions can be validated without exposing details, while benefiting from improved performance supported by recent upgrades to Ethereum (for example, through Layer 2s). Finally, institutional-grade security is being strengthened through

shared control mechanisms like multi-signature governance and threshold cryptography that require multiple parties to approve a transaction.

Second, which model will offer more acceptable governance? Governance mostly concerns the rulebook regulating transactions. Questions addressed by rulebooks include the following: Who can access the infrastructure, under what conditions, which assets and transactions are permitted, what information is needed to validate a transaction and who validates it, how and when are transactions considered settled irrevocably, and how are disputes managed? Infrastructure provision goes beyond technology, as it fundamentally depends on legal frameworks and governance arrangements.

As noted earlier, permissionless base layers allow restrictions at higher layers, whereas permissioned base layers are built on purpose to enforce restrictions. The premise of public permissionless infrastructure is that few constraints exist at the outset. Nearly any user, asset, or transaction is potentially welcome, as long as it obeys the network's protocol rules. However, participants can create Layer 2 solutions or can hard-code constraints in the assets they create, leveraging smart contracts. Layer 2 blockchains are scaling solutions that operate off the main chain and rely on the base layer for security, settlement finality, data integrity, and dispute resolution. $^{12}$ Smart contracts can be used to impose regulatory requirements such that only clients or investment professionals can transact certain assets, also known as whitelisting participants after verifying whether they comply with predefined requirements. Mancini-Griffoli and others (2024) offer a more detailed discussion of governance models and their implications.

Instead, the premise of permissioned infrastructures is that users are parsed at the outset by the infrastructure operator, so only certain users and assets can access a given blockchain. The advantage is potentially more scalable settlement and trusted counterparties. For example, Circle has launched Arc, a permissioned Layer 1 blockchain designed for stablecoin-native applications and operated by approved validators that improve fee predictability and accountability. Arc incorporates features such as a built-in foreign exchange engine, mechanisms to protect sensitive payment data, and PvP settlement, with transaction fees paid in USDC (Rodriguez, 2025). Stripe's Tempo fo

[中间内容因长度限制已省略]

otype.” Federal Register 90, no. 244 (December 23): 60096–99.

https://www.federalregister.gov/documents/2025/12/23/2025-23712/request-for-information-and-comment-on-reserve-bank-payment-account-prototype

Buterin, Vitalik. 2021a. “An Approximate Introduction to How zk-SNARKs Are Possible.” January 26, 2021. https://vitalik.eth.limo/general/2021/01/26/snarks.html

Buterin, Vitalik. 2021b. “Why Sharding Is Great: Demystifying the Technical Properties.” April 7, 2021. https://vitalik.eth.limo/general/2021/04/07/sharding.html

Cabedo, Yaiza, Tommaso Mancini-Griffoli, Fabian Schär, and Nicolas Zhang. 2026. “Evolution of Financial Market Infrastructures in a Tokenized Economy.” IMF Working Paper 26/136, International Monetary Fund, Washington DC.

Chainalysis. 2024. “Introduction to Zero-Knowledge Proofs.” https://www.chainalysis.com/blog/introduction-to-zero-knowledge-proofs-zkps/

Copestake, Alexander, Divya Kirti, Maria Soledad Martinez Peria, and Yao Zeng. 2025. “Integrating Fragmented Networks: The Value of Interoperability in Money and Payments.” IMF Working Paper 25/126, International Monetary Fund, Washington, DC. https://www.imf.org/en/publications/wp/issues/2025/06/27/integrating-fragmented-networks-the-value-of-interoperability-in-money-and-payments-568008

Duarte, Angelo, Jon Frost, Leonardo Gambacorta, Priscilla Koo Wilkens, Hyun Song Shin. 2022. “Central Banks, the Monetary System and Public Payment Infrastructures: Lessons from Brazil’s Pix.” BIS Bulletin No 52, Bank of International Settlements. https://www.bis.org/publ/bisbull52.pdf

Eroglu, Hakan, Giulio Cornelli, Jon Frost, Friederike Rühmann, and Vatsala Shreeti. 2026. Opening Doors to Open Finance: Evidence from the International Experience. BIS Papers No. 168. Basel: Bank for International Settlements. March 30. https://www.bis.org/publ/bppdf/bispap168.htm

European Central Bank. 2026. “Appia – Paving the Way for a Future-Ready, Integrated Financial Ecosystem Leveraging Tokenisation and DLT.” https://www.ecb.europa.eu/press/payments-news/ecb.pubconpm202603.en.html

FintechNewsCH. 2025. “UBS Joins Tempo Public Testnet to Explore Stablecoin Payments.” Fintech Schweiz Digital Finance News. https://fintechnews.ch/blockchain\_bitcoin/ubs-tempo-public-testnet/79754/

Garrido, José M. 2023. “Digital Tokens: A Legal Perspective.” IMF Working Paper 23/151, International Monetary Fund, Washington, DC.

Gross, Marco, and Richard Senner. 2026. “From Par to Pressure: Liquidity, Redemptions, and Fire Sales with a Systemic Stablecoin.” IMF Working Paper 26/5, International Monetary Fund, Washington, DC.

Heeb, Gina and Vicky Ge Huang. 2026. “JPMorgan, Citi and Big Banks Plan New Tokenized Deposit System to Answer Crypto.” The Wall Street Journal, June 4. https://www.wsj.com/finance/banking/jpmorgan-citi-and-big-banks-plan-new-tokenized-deposit-system-to-answer-crypto-6b2d696b

Holmstrom, Bengt. 2015. “Understanding the Role of Debt in the Financial System.” BIS Working Papers No 479, Monetary and Economic Department. https://economics.mit.edu/sites/default/files/2022-09/Holmstrom%20Understanding%20debt%20WP%20479%20BIS%202015-no%20co.pdf

JP Morgan. 2026. “JPM Coin: Institutional Deposit Tokens & Blockchain Payments by Kinexys.” https://www.jpmorgan.com/kinexys/digital-payments/jpm-coin.

Klapper, Leora, Dorothe Singer, Laura Starita, and Alexandra Norris. 2025. “The Global Findex Database 2025: Connectivity and Financial Inclusion in the Digital Economy.” World Bank, Washington, DC.

Kunaratskul, Tansaya, Ashley Lannquist, André Reslow, and Nicolas Xuan-Yi Zhang. 2025. “Central Bank Exploration of Tokenized Reserves.” IMF Fintech Note 2025/011, International Monetary Fund, Washington, DC. https://www.imf.org/-/media/files/publications/ftn063/2025/english/ftnea2025011.pdf

Li, Bo, Tommaso Mancini-Griffoli, Marcello Miccoli, Brandon Tan, and Longmei Zhang. 2026. “Making Stablecoins Stable.” IMF Working Paper 26/74, International Monetary Fund, Washington, DC. https://www.imf.org/-/media/files/publications/wp/2026/english/wpiea2026074-source-pdf.pdf

Mancini-Griffoli, Tommaso. 2025. “The Money Dialogues.” IMF Finance and Development, International Monetary Fund. https://www.imf.org/en/publications/fandd/issues/2025/09/the-money-dialogues-tommaso-mancini

Mancini-Griffoli, Tommaso, Yaiza Cabedo, Marco Gross, Yinan Qiu, Edona Reshidi, André Reslow, Nicolas Zhang, Marianne Bechara, Juliana Bolzani, Jose Garrido, Maksym Markevych, Itai Agur, Sole Martinez Peria, Marco Reuter, Eugenio Cerutti, and Melih Firat. 2024. “G-20 Note On Financial Platforms: What Are They and What Are Their Macro-Financial Implications?” International Monetary Fund. https://www.imf.org/-/media/files/research/imf-and-g20/2024/g20-report-2024-financial-platforms-macrofinancial-implications-imf-oct2024-final-board-publish.pdfg

Rodriguez, Jesus. 2025. “Some Technical Notes about Circle’s New Blockchain.” Sentora, Medium. https://medium.com/sentora/some-technical-notes-about-circles-new-blockchain-d09b8d26e0a4

Schär, Fabian. 2021. “Decentralized Finance: On Blockchain- and Smart Contract-Based Financial Markets.” Federal Reserve Bank of St. Louis Review 103 (2): 153–74. https://doi.org/10.20955/r.103.153-74

SG Forge. 2026. “SG-FORGE’s EUR CoinVertible is Now Available on the XRP Ledger.” https://www.sgforge.com/sgf-coinvertible-on-the-xrp-ledger/

Swift. 2026. “Swift’s Blockchain-Based Shared Ledger Progresses to MVP Implementation.” https://www.swift.com/news-events/news/swifts-blockchain-based-shared-ledger-progresses-mvp-implementation

Tempo Team. 2025. "Tempo's Testnet Is Live." https://tempo.xyz/blog/testnet

![](images/bcfea95179a52a8c74cb4c029ff87f3e60a5dbedf2c490153faacc46150d8a85.jpg)
"""
