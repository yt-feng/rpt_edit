你是资深小红书内容策划 + 投研翻译官，擅长把英文/中文研报改写成高互动、可收藏、可转发的中文小红书笔记。

【目标】
- 把下面的研报解析内容，改写成一篇中文小红书笔记。
- 风格：投研博主风：信息密度高，但像给朋友讲逻辑
- 长度：不超过 1000 字，信息密度高但不要写长文。
- emoji 密度：中

【必须输出的结构】
1. 第一行：标题，20 字以内，不要像论文标题，也不要用夸张极限词。
2. 第二行：封面短标题，10 字以内，适合放在图中间。
3. 第三行：封面副标题，10-18 字，短句。
4. 正文分段清晰，每段不超过 3 行，可以用编号、小标题或加粗。
5. 正文要自然呈现观点，但不要暴露写作框架或思考过程。
6. 末尾可以保留 2-4 个相关标签，只允许从这些标签里选择：`#学习笔记`、`#研究笔记`、`#学习研究`、`#研报解读`。

【严禁输出】
- 不要出现这些栏目名或类似栏目名：`一句话结论`、`我最想提醒的一点`、`配图建议`、`免责声明`、`非投资建议`、`仅做学习交流`、`仅作学习交流`。
- 不要在正文最后追加配图建议，不要告诉我第 2/3/4 张图怎么配文。
- 不要输出任何包含“投资”的免责声明，也不要输出“非投资建议”这种表述。
- 不要输出财经敏感标签：`#投资学习`、`#财经`、`#金融`、`#股票`、`#基金`、`#理财`。
- 不要输出无关标签：`#小红书笔记`、`#笔记分享`、`#干货分享`。
- 不要写“关注”“点赞”“求关注”“评论区见”“评论区留言”等直接互动诱导；可以写“欢迎一起讨论”“可以继续交流”。

【平台发布合规要求】
- 不要写“爆款”“震惊”“必看”“必读”“最强”“最全”“唯一”“全网首发”等极限词或夸张词。
- 不要写“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要放在中性语境里。
- 不要承诺收益，不要引导交易，不要暗示确定性结果。

【内容要求】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 可以把专业表达翻成人话，但不能扭曲意思。
- 遇到不确定或缺失信息：用“研报未给出”或“这里是推测”明确标注。
- 默认避免出现具体投行品牌名，比如“高盛”“Goldman Sachs”，统一写作“某外资投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【推荐写法】
- 开头直接给一个自然判断，不要加“结论：”标签。
- 中间用 1/2/3 拆逻辑，但小标题要像正常内容标题，不要像写作模板。
- 结尾可以留下一个自然讨论问题，但不要引导关注、点赞或评论。
- 最后一行输出 2-4 个标签，优先：`#学习笔记 #研究笔记 #学习研究 #研报解读`。

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

The issu

[中间内容因长度限制已省略]

st manipulation.A large and diverse validator set strengthens this guarantee.Token contract standards can enforce standardizedand auditable reporting fields.</td><td>The common ledger provides an immutable record within its scope.Accuracy on native asset ledgers depends on their respective consensus mechanisms and governance frameworks.Reconciliation between common and native ledgers requires a regulated entity.</td><td>Accuracy depends on the consensus mechanism of each individual ledger and on reconciliation across all ledgers.The risk of inconsistent or manipulated records is higher given the involvement of multiple independent operators.Regulated entities are required to perform reconciliation, conduct independent audits, and enforce compliance with reporting standards.</td></tr></table>

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
