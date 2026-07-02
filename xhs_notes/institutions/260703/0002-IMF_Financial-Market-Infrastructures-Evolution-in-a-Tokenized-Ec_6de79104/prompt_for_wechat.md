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
# The Evolution of Financial Market Infrastructures in a Tokenized Economy

# Exploring blockchain implementation options for issuance, central clearing, settlement, and reporting

Prepared by Yaiza Cabedo, Tommaso Mancini-Griffoli, Fabian Schär, Nicolas Zhang

WP/26/136

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

2026
JUL

![](images/7f22ea2bed6a912c27b9311808e34818b7599fe92da7e6c21a27acc4b6565bf9.jpg)

IMF Working Paper
Monetary and Capital Markets Department

The Evolution of Financial Market Infrastructures in a Tokenized Economy Prepared by Yaiza Cabedo, Tommaso Mancini-Griffoli, Fabian Schär, and Nicolas Zhang\*

Authorized for distribution by Marcello Miccoli
July 2026

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

ABSTRACT: This paper examines how tokenization and distributed ledger technology may transform Financial Market Infrastructures (FMIs) by enabling smart contracts to perform a growing share of functions traditionally undertaken by central securities depositories, central counterparties, and trade repositories. It argues that while record-keeping, settlement, collateral management, and reporting can increasingly be executed on-chain, key functions requiring legal certainty, governance, accountability, and discretion remain institutional in nature. The analysis assesses which activities across issuance, clearing, settlement, and reporting can migrate to code, where limitations persist, and how risks evolve in tokenized environments. It finds that tokenization is more likely to reconfigure than eliminate FMIs, creating new efficiencies while introducing novel operational and governance risks. The most plausible outcome is a hybrid FMI model in which technology and institutions jointly provide the trust, resilience, and oversight required for financial stability.

RECOMMENDED CITATION: Cabedo, Yaiza, Tommaso Mancini-Griffoli, Fabian Schär, and Nicolas Zhang. 2026. "The Evolution of Financial Market Infrastructures in a Tokenized Economy". International Monetary Fund, Washington, DC. No. WP/26/136.

<table><tr><td>JEL Classification Numbers:</td><td>E58, G15, O33, O38</td></tr><tr><td>Keywords:</td><td>Tokenization; central counterparty; securities settlement system; central securities depository; trade repository; blockchain; smart contracts</td></tr><tr><td>Authors&#x27; email addresses:</td><td>YCabedo@imf.org, TMancini-Griffoli@bis.org, $^{1}$  F.Schaer@unibas.ch, $^{2}$  NZhang@imf.org</td></tr></table>

# The Evolution of Financial Market Infrastructures in a Tokenized Economy

# Exploring blockchain implementation options for issuance, central clearing, settlement, and reporting

Prepared by Yaiza Cabedo, Tommaso Mancini-Griffoli, $^{3}$ Fabian Schär, $^{4}$ Nicolas Zhang

## Contents

Introduction .... 3
I. Transaction Lifecycle, Risks, and the Role of Financial Market Infrastructures .... 5
The lifecycle of a transaction: issuance, trading, and post-trading .... 5
Risks associated with the lifecycle of a transaction.... 6
An overview of FMIs and how they mitigate risks .... 7
FMIs' ecosystem and governance.... 11
II. Features of Tokenized Financial Assets .... 13
Tokenization of financial assets.... 13
Blockchain governance .... 15
III. FMI Functions in a Tokenized World.... 20
Tokenized asset lifecycle.... 20
Risks and risk mitigation.... 24
Conclusion.... 32
Glossary.... 33
Annex 1. FMIs' value propositions and functions .... 38
Annex 2. Issuance, safekeeping of assets and settlement functions across platform models .... 40
Annex 3. Novation, multilateral netting and margin call functions across platform models.... 41
Annex 4. Derivatives data centralization functions across platform models.... 43
References.... 45
BOXES
1. FMIs relevant to this paper.... 8
FIGURES (as needed)
1. This paper's approach.... 4
2. The three possible relationships between ledgers, assets, and owners.... 17
3. Three architecture models exist.... 18

## Introduction

How should financial market infrastructures (FMIs) prepare for a world in which assets are tokenized? This paper argues that smart contracts and distributed ledgers can perform a substantial share of the functions now carried out by central securities depositories (CSDs), securities settlement systems (SSSs), central counterparties (CCPs), and trade repositories (TRs), especially where processes are deterministic, rules-based, and data-driven. $^{5}$ Record-keeping, settlement, collateral transfers and reporting can move on-chain. Yet code cannot by itself provide legal certainty, bear accountability, or exercise discretion under stress.

Tokenization does not imply disintermediation, but institutional redesign. The most plausible outcome is a hybrid FMI model, in which smart contracts perform a greater share of operational and transactional functions, while legal entities remain responsible for governance, compliance, risk management, and interventions to preserve business continuity. $^{6}$ This is particularly true where functions depend on off-chain inputs, cross-ledger coordination, supervisory access, or judgment in the calibration of margins, or the management of defaults.

This paper examines the shifts across issuance, clearing, settlement, and reporting. It asks which CSD, CCP and TR functions can migrate on-chain, where the main limitations remain, and where hybrid arrangements are likely to emerge. The objective is not to predict a single end-state, but to clarify the trade-offs and identify how responsibilities may be redistributed between technology and institutions in a tokenized financial system.

This analysis is intended for policymakers, supervisors and market participants alike. It aims to support a more systematic assessment of how existing infrastructures could adapt, how trust and accountability are reallocated between institutions and technology, and how efficiency gains can be realized without undermining financial stability.

Figure 1. This paper's approach  
![](images/7e8ec0506f1c408f9b1d85783b7031289aebe5dce1ffbbe9031d451158673c72.jpg)

## Source: Authors' elaboration.

Note: This paper focuses primarily on FMIs and their functions, issuance, clearing, settlement, and reporting for securities and derivatives. The paper analyzes how these functions may evolve in a tokenized environment through the asset lifecycle dimension. In this Figure, “Trading” appears in a different color, to indicate that the emphasis is on the other lifecycle stages that more directly relate to FMIs.

The paper is built around the lifecycle of securities and derivatives transactions, following the logic illustrated in Figure 1. Section 1 presents the lifecycle of a transaction in today's financial markets, the risks that parties to a transaction face, and how FMIs help mitigate them. Section 2 examines the features of tokenized financial assets, governance in blockchain ecosystems, and three possible architectures that arise from the relationships between ledgers, assets, and owners—the single, compatible, and common models. Section 3 explores how the lifecycle of a transaction may evolve in a tokenized environment, which risks would persist, and how these could be mitigated. Lastly, the paper offers conclusions and four annexes with tables that summarize the value propositions of FMIs today and how the functions of CSDs, SSSs, CCPs, and TRs could be delivered on blockchain across the three different architecture models.

# I. Transaction Lifecycle, Risks, and the Role of Financial Market Infrastructures

This section examines how financial transactions are structured today and the role that FMIs play in mitigating the risks that market participants face when transacting securities and derivatives. It first outlines the lifecycle of a transaction—from issuance to post-trade processes including clearing, settlement, and reporting—and identifies the key risks that arise at each stage. It then explains how FMIs are designed to mitigate these risks through a combination of operational, legal, and financial safeguards. Finally, it provides an overview of the FMI ecosystem and its governance arrangements. This framework serves as a benchmark for assessing how these functions, and the risks FMIs address, may evolve in a tokenized environment.

## The lifecycle of a transaction: issuance, trading, and post-trading

Issuance is the basis of securities markets, it is the creation of the security and its placement in the primary market. Initially, securities were issued as physical certificates, but this has evolved into dematerialized processes, where securities are transferred electronically via book-entry accounts. The process begins with opening an issuance account to record the number of assets created.

The accuracy of issuance records is essential for market confidence. Market participants depend on the integrity of issuance systems, responsible for maintaining accurate records to prevent the creation of unauthorized securities, thereby ensuring transparency and credibility in the issuance process. $^{7}$

Trading involves agreement on the terms to exchange assets. These include price, coupons, and settlement dates, as well as the verification of transaction details and written confirmations between parties. Trading occurs through matching platforms that bring together buyers and sellers. $^{8}$ All following stages of the asset lifecycle are known as post-trading.

Clearing is the process of determining the obligations of participants. Clearing through a central counterparty (CCP) involves novating the initial counterparties' contract, and the CCP becomes the buyer and the seller of the transaction. Clearing is calculating net positions and ensuring funds or securities are available to meet these commitments. CCPs use multilateral netting to consolidate obligations into a single position per participant, reducing risk.

Settlement occurs after the trade has been executed, it completes the transfer of ownership updating ownership records electronically at a CSD through book-entry accounts. During the time between trade and settlement (T and T+x), counterparties face risks such as asset destruction, failure to receive the asset, parties reneging on the trade, or the possibility of delivering an asset without receiving anything in return. To mitigate these risks, counterparties can either fully pre-fund the assets to be delivered from the moment the trade is entered or use risk management techniques, such as providing collateral.

The final step in the transaction lifecycle is reporting. Reporting involves providing data on executed transactions to enhance transparency and ensure access for authorities. The accuracy, completeness, and timeliness of the information reported are of the essence, as errors or delays can undermine transparency and hinder effective oversight.

Market participants rely on accurate records and coordinated processes. Settlement processes depend on the accuracy of ownership records at the CSD and the coordination between intermediaries such as custodians and registrars to maintain the integrity of securities ownership. Clear operational boundaries and robust reconciliation processes are essential, particularly in jurisdictions where registrars, rather than CSDs, oversee initial issuance.

The lifecycle of a transaction relies on coordination across systems and participants. Parties need to coordinate and reconcile across different IT systems, ledgers, and platforms operated in isolation by FMIs, participants, and intermediaries. Reliable relationships and regular data reconciliations between these entities are essential to maintaining operational integrity, reducing risks, and ensuring the smooth functioning of financial markets.

## Risks associated with the lifecycle of a transaction

Transactions in financial markets are exposed to a range of risks that arise at different stages of their lifecycle, from execution to clearing, settlement, and asset custody. These risks affect counterparties directly, shaping their ability to complete transactions as intended and to preserve the value of exchanged assets.

Legal risk can arise at any stage of the transaction lifecycle and refers to the possibility that the unexpected application of laws or regulations results in a loss. This includes situations where due to legal uncertainty, contracts underpinning a transaction are rendered illegal or unenforceable by courts. These risks are particularly acute in cross-border settings.

Operational risk stems from deficiencies in information technology systems, human errors, management failures, or system disruptions that may delay, alter, or prevent the execution and completion of transactions. Cyber risk constitutes a key subset of operational risk. $^{9}$

Custody risk arises where assets are held on behalf of counterparties and reflects the possibility of loss due to a custodian's or sub-custodian's insolvency, negligence, fraud, poor administration, or inadequate recordkeeping.

As transactions move toward completion, settlement risk becomes a central concern. Settlement risk refers to the possibility that settlement will not occur as expected, such that one counterparty delivers a financial asset but does not receive the corresponding payment. Delivery versus Payment (DvP) is a core mechanism designed to mitigate settlement risk by ensuring the simultaneous exchange of securities and cash. By linking the transfer of the asset to the transfer of funds, DvP significantly reduces the risk that one

counterparty performs while the other fails to do so. Settlement risk is closely linked to credit, liquidity, legal and operational risks and is particularly relevant in securities transactions.

In practice, DvP relies on coordinated processes and standardized messaging between the relevant systems and agents involved in transferring securities and cash, ensuring that both legs of the transaction are executed together. The effectiveness of DvP depends on the reliable synchronization of these processes so that neither leg is completed in isolation. The cash leg is typically settled either in central bank money or in commercial bank money, with central bank money generally considered safer due to the absence of credit risk. The importance of DvP was reinforced following the 1987 equity market crisis, after which the G-30 recommended its implementation in settlement systems, with the G-10 subsequently developing its framework (CPSS 1992). This requirement is now embedded in the CPMI-IOSCO Principles for Financial Market Infrastructures (PFMIs), where it constitutes a key safeguard for ensuring the safe and efficient completion of transactions.

Credit risk arises from the possibility that a counterparty is unable to meet its financial obligations—when due or at any point in the future – while liquidity risk arises when a counterparty fails to meet its obligations on time, even if it remains solvent and may be able to perform later. These risks can also be referred to as counterparty risks, and are relevant to clearing and settlement phases, when financial obligations crystallize and must be discharged.

## An overview of FMIs and how they mitigate risks

FMIs are central to the stability, efficiency, and resilience of financial markets. By providing multilateral arrangements for clearing, settlement, and the recording of financial transactions, FMIs reduce counterparty, settlement, and operational risks, limit contagion, and enhance transparency. Centralization of these functions enables netting efficiencies, risk mutualization, and coordinated risk management across participants, thereby supporting orderly market functioning and financial stability.

These objectives are achieved through a diverse set of infrastructures, each specialized in performing distinct functions along the transaction life-cycle. FMIs therefore encompass a range of systems that differ in scope, design, and risk-management responsibilities.

This paper focuses primarily on CSDs, CCPs, SSSs, and TRs, the FMIs primarily involved in transactions of securities and derivatives. At the same time, payment systems are also linked to the other FMIs, as they are involved in securities and derivatives' transactions, for the cash leg or payment. The main types of FMIs are outlined in Box 1 below.

## Box 1. FMIs relevant to this paper $^{10}$

Central Securities Depositories (CSDs) are responsible for the safekeeping, maintenance, and transfer of securities. In addition, many CSDs act as securities registrars and provide ancillary services, such as corporate action processing or securities' lending. International CSDs further support cross-border financial transactions by accommodating a range of globally traded instruments.

The issuance process differs across jurisdictions. In many countries, issuance occurs at a Central Securities Depository (CSD), while in other jurisdictions, official registrar services handle the process and ensure the accurate recording and safekeeping of securities in the initial issuance.

Securities Settlement Systems (SSSs) facilitate the transfer and settlement of securities by book entry, following a set of predetermined multilateral rules. When securities transactions involve a payment, SSSs ensure delivery versus payment (DvP), a mechanism that guarantees the transfer of securities only occurs if the corresponding payment is made, reducing settlement risk. In many jurisdictions, a CSD operates an SSS. For instance, in the European Union an SSS must be operated by a CSD.

Central Counterparties (CCPs) interpose themselves between counterparties to financial transactions, assuming the counterparty risk of both sides of the trade and ensuring the fulfillment of contractual obligations. In addition, CCPs significantly reduce risks to participants through the multilateral netting of trades, and by imposing risk controls on all participants. For example, CCPs require collateral from participants to cover exposures and have mechanisms to mutualize losses in case of a participant's default. As a result, CCPs reduce systemic risk.

Trade Repositories (TRs) provide centralized electronic repositories for transaction data and

[中间内容因长度限制已省略]

provide a comprehensive view.</td><td>Comprehensive regulatory access requires integration of data from all asset ledgers and off-chain sources managed by the orchestrator.A TR or equivalent regulated entity is needed to collect, reconcile, and provide access to information.</td></tr><tr><td>Ensuring accuracy of transaction data</td><td>Immutable transaction records, enforced by the consensus mechanism, provide a primary safeguard against manipulation.A large and diverse validator set strengthens this guarantee.Token contract standards can enforce standardizedand auditable reporting fields.</td><td>The common ledger provides an immutable record within its scope.Accuracy on native asset ledgers depends on their respective consensus mechanisms and governance frameworks.Reconciliation between common and native ledgers requires a regulated entity.</td><td>Accuracy depends on the consensus mechanism of each individual ledger and on reconciliation across all ledgers.The risk of inconsistent or manipulated records is higher given the involvement of multiple independent operators.Regulated entities are required to perform reconciliation, conduct independent audits, and enforce compliance with reporting standards.</td></tr></table>

## References

Agur, Itai, Germán Villegas-Bauer, Tommaso Mancini-Griffoli, Maria Soledad Martinez Peria, and Brandon Tan. 2025. “Tokenization and Financial Market Inefficiencies.” IMF Fintech Note No. 25/001. International Monetary Fund, Washington, DC. Tokenization and Financial Market Inefficiencies.

Aldasoro, Iñaki, Sebastian Doerr, Leonardo Gambacorta, Rodney Garratt, and Priscilla Koo Wilkens. 2023. "The Tokenisation Continuum." BIS Bulletin No. 72. Bank for International Settlements, Basel, April. The tokenisation continuum.

Auer, Raphael, Jon Frost and Jose Maria Vidal Pastor. 2022. “Miners as intermediaries: extractable value and market manipulation in crypto and DeFi.” BIS Bulletin No. 58. Bank for International Settlements, Basel, June. Miners as intermediaries: extractable value and market manipulation in crypto and DeFi.

Bank for International Settlements (BIS) and BIS Committee on Payments and Market Infrastructures (CPMI). 2024. “Tokenisation in the Context of Money and Other Assets: Concepts and Implications for Central Banks.” Report to the G20, October. Bank for International Settlements, Basel. Tokenisation in the context of money and other assets: concepts and implications for central banks.

Bank for International Settlements and BIS Committee on Payment and Settlement Systems of the central banks of the Group of Ten countries. 1992. Delivery versus payment in securities settlement systems. Delivery versus payment in securities settlement systems - Oct 1992.

Buterin, Vitalik, Jacob Illum, Matthias Nadler, Fabian Schär, and Ameen Soleimani. 2023. “Blockchain Privacy and Regulatory Compliance: Towards a Practical Equilibrium.” Blockchain: Research and Applications, Vol. 4, No. 4. https://doi.org/10.1016/j.bcra.2023.100109.

Committee on Payments and Market Infrastructures and International Organization of Securities Commissions (CPMI-IOSCO). 2012. “Principles for Financial Market Infrastructures.” Bank for International Settlements, Basel, and International Organization of Securities Commissions. Principles for Financial Market Infrastructures.

European Commission: Directorate-General for Financial Stability, Financial Services and Capital Markets Union and Fabian Schär. 2024. “Enhancing financial services with permissionless blockchains.” Publications Office of the European Union. https://data.europa.eu/doi/10.2874/8306042.

Financial Stability Board (FSB). 2024. “The Financial Stability Implications of Tokenisation.” FSB Report, October. https://www.fsb.org/2024/10/the-financial-stability-implications-of-tokenisation/.

Gaidosch, Tamas, Emran Islam, Tanai Khiaonarong, Rangachary Ravikumar, and Christopher Wilson. 2026. "Good Practices in Cyber Risk Regulation and Supervision." IMF Departmental Papers No. 26/001. International Monetary Fund, Washington, DC.

Mackinga, Torgin, Tejaswi Nadahalli, and Roger Wattenhofer. 2022. "TWAP Oracle Attacks: Easier Done than Said?" Paper presented at the IEEE International Conference on Blockchain and Cryptocurrency (ICBC 2022). Cryptology ePrint Archive, Paper 2022/445. https://eprint.iacr.org/2022/445.

Mancini-Griffoli, Tommaso, Cabedo, Yaiza, Gross, Marco, Qiu, Yinan, Reshidi, Edona, Reslow, André Zhang, Nicolas, Bechara, Marianne, Bolzani, Juliana, Garrido, Jose, Markevych, Maksym, Agur, Itai, Martinez Peria, Sole, Reuter, Marco, Cerutti, Eugenio and Melih Firat. 2024. “Financial Platforms: What Are They and What Are Their Macro-Financial Implications?” G-20 Note. International Monetary Fund, Washington,

DC, October. g20-report-2024-financial-platforms-macrofinancial-implications-imf-oct2024-final-board-publish.pdf

Narula, Neha, Willy Vasquez, and Madars Virza. 2018. “zkLedger: Privacy-Preserving Auditing for Distributed Ledgers.” In Proceedings of the 15th USENIX Symposium on Networked Systems Design and Implementation (NSDI '18), pp. 65–80. USENIX Association. nsdi18-narula.pdf

Schär, Fabian. 2021. “Decentralized Finance: On Blockchain- and Smart Contract-Based Financial Markets.” Federal Reserve Bank of St. Louis Review, Vol. 103, No. 2, pp. 153–174. https://doi.org/10.20955/r.103.153-74.

Schuler, Katrin, Ann Sofie Cloots, and Fabian Schär. 2024. “On DeFi and On-Chain CeFi: How (Not) to Regulate Decentralized Finance.” Journal of Financial Regulation, Vol. 10, No. 2, pp. 213–242. Oxford University Press. https://doi.org/10.1093/jfr/fjad014.

![](images/486b9fd2f43b8afcadc8d10d9af0c63e691b4c386774987c1d4df917da99f381.jpg)
"""
