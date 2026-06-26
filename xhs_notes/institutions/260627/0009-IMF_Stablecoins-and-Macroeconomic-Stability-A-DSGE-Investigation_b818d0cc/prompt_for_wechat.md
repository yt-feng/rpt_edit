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
- 已识别机构名：`国际货币基金组织`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份国际货币基金组织研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Stablecoins and Macroeconomic Stability: A DSGE Investigation

Hui He, Yao Zhao, and Dayong Zhou

WP/26/129

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

2026
JUN

![](images/6a489f3be04ab948c50ebc969c41d9448643ee267d0e54c34137090406517417.jpg)

# IMF Working Paper Monetary and Capital Markets Department

Stablecoins and Macroeconomic Stability: A DSGE Investigation Prepared by Hui He, Yao Zhao, and Dayong Zhou

Authorized for distribution by Oana Croitoru
June 2026

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

ABSTRACT: The paper develops a new monetarist DSGE model to examine the macroeconomic implications of fiat-money-backed stablecoins and the effectiveness of prudential policies in mitigating associated risks. The model features two segmented sectors: a centralized real economy where fiat money facilitates consumption and investment, and a decentralized virtual economy characterized by anonymous bilateral search and matching, in which transactions are exclusively conducted using stablecoins. Calibrated to the U.S. economy, the simulation results reveal that stablecoins amplify the propagation of exogenous shocks to key macroeconomic variables by weakening the effectiveness of monetary policy. However, prudential regulations—specifically those governing the backing ratio of stablecoins to fiat-denominated reserve assets, analogous to banking liquidity requirements—can serve as stabilizing instruments, dampening volatility and enhancing macroeconomic resilience in the presence of stablecoins.

RECOMMENDED CITATION: He, H., Zhao, Y., and Zhou, D. (2026). “Stablecoins and Macroeconomic Stability: A DSGE Investigation.” IMF Working Paper No. 26/129, International Monetary Fund, Washington DC.

JEL Classification Numbers:

E12, E32, E41, E42, E52

Keywords:

Stablecoin; DSGE; Monetary Search; Currency

Competition; Prudential Regulation

Author's E-Mail Address:

hhe@imf.org; bnuer0011@gmail.com; zdy669782@gmail.com

WORKING PAPERS

# Stablecoins and Macroeconomic Stability: A DSGE Investigation

Prepared by Hui He, Yao Zhao, and Dayong Zhou $^{12}$

## Contents

1. Introduction .... 3
2. Model .... 6
2.1 Households .... 7
2.2 Firms .... 14
3. Model parameterization and calibration .... 17
3.1 Parameter parameterization .... 17
3.2 Calibration .... 18
3.3 Solution method .... 19
4. Dynamic Analysis .... 19
4.1 Impulse responses of various shocks .... 19
4.2 Stablecoins, macro stability, and prudential regulation .... 24
4.3 Sensitivity Analysis .... 26
5. Conclusions .... 28
References .... 28
Annex 1: General Equilibrium Conditions .... 31
Annex 2: Sensitivity Analysis .... 33

## 1 Introduction

In the digital era, the global financial landscape has rapidly evolved, as has the nature of money. In June 2019, Facebook, a big tech company, released a white paper proposing a simple and borderless stablecoin named Libra. $^{1}$ Libra, first global stablecoin as identified by Adachi et al. (2020), would fall into the category of digital money issued by the private sector (Adrian and Mancini-Griffoli, 2019; G7, 2019). On August 7, 2023, the global payment conglomerate PayPal launched a native stablecoin, PYUSD. This marked the first time a USD-denominated stablecoin was issued by a licensed financial institution, in collaboration with a public blockchain platform (Paxos), following the path of the pioneering USD stablecoin USDT, issued by the startup Tether, which is now the largest stablecoin globally. $^{2}$

Today, various digital forms of money have emerged, $^{3}$ including government-run central bank digital currencies (CBDC), blockchain-based bank deposits (tokenized deposits), stablecoins run by big tech or private platforms, and crypto assets based on public blockchains (for example, Bitcoin and Ethereum). $^{4}$

In the spectrum of digital assets, a stablecoin is unique since it is designed to be backed/pegged by a specific asset or a pool/basket of assets. Therefore, it aims to maintain a stable value compared to other forms of crypto assets. A stablecoin is minted on the blockchain and is typically identifiable by one of four underlying collateral structures: fiat-backed, crypto-backed, commodity-backed, or algorithmic. While underlying collateral structures can vary, stablecoins always aim for the same goal: stability (Bullmann et al., 2019). $^{5}$

Against the backdrop of fast-changing financial landscape, stablecoins brought several important perspectives to academia and industry:

(1) Stablecoins are digital assets that aim to maintain a stable value relative to a reference asset. Eichengreen (2019) defines stablecoins and raises doubts about whether these private digital assets can successfully meet the challenges required to scale and maintain their peg over time. He suggests that private stablecoins will face challenges during periods of financial stress, when investors could panic and trigger a “run” on the stablecoin issuers, similar to a bank run. Catalini and Massari (2021) argue that stablecoins can offer some advantages over traditional crypto assets, such as lower volatility, faster transactions, lower costs, and greater accessibility. Lyons and Viswanath-Natraj (2020) take Tether stablecoin (USDT) as an example to explore the theoretical mechanism of stablecoins to stabilize Bitcoin prices and conduct empirical tests. Intriguingly, the quest for stable money is not new, with historical precedents offering valuable insights into the governance challenges inherent in such systems. Frost et al. (2020) examine the erstwhile Bank of Amsterdam, a predecessor to the stablecoins, to show whether the early institutional attempt can provide a stable medium of exchange. They highlight how historical endeavors faced challenges in maintaining trust, managing reserves, and navigating the complexities of monetary governance. This historical lens underscores that the economic and governance issues confronting modern stablecoins are deeply rooted in the persistent challenge of creating reliable, stable forms of money. Uhlig (2022) provides a novel theory accounting for a recent price collapse—a failure algorithm stablecoin named Terra’s UST coin—and quantifies the model’s explanations using the real-world market collapse data.

(2) Despite their design features, stablecoins are susceptible to various forms of risks, such as regulatory uncertainty, consumer protection, and financial instability. Ma et al. (2025) observe that the largest stablecoin issuer, Tether, limits redemption to a concentrated group of agents (around six agents per month). This centralization of arbitrage, coupled with the backing of stablecoins by imperfectly liquid USD assets, introduces significant risks to financial stability, as the ability to maintain the peg under stress relies on the timely and full convertibility of these reserves, and this convertibility would be undermined by “stablecoin runs.” Gross and Senner (2026) provide a detailed analysis of risks faced by stablecoin issuers and by the financial systems in which they operate. They show that systemically large fiat-backed stablecoins can amplify financial stress through redemption-driven fire sales that spill over into sovereign bond markets. Using a structural model, they demonstrate that capital and liquidity buffers are the most effective tools for reducing run risk and market volatility, with redemption gates and shorter asset duration providing additional mitigation. Iyer (2022) studies the transmission between crypto asset markets (particularly Bitcoin and USDT) and traditional financial equity markets. She finds that the transmission effect among crypto assets has been strengthened, and spillovers from crypto asset markets to financial markets are on the significant rise. The findings support calls for global coordination in crypto regulation to mitigate systemic risks. Therefore, stablecoins need to be regulated and supervised by appropriate authorities and comply with relevant standards and rules, as recommended by the IMF (Bains et al. 2022), IMF-FSB (2023) and international standard setting bodies (SSBs, various publications, see footnote 7).

(3) The fast proliferation of stablecoin market holds significant implications for monetary policy transmission in the competitive landscape of the banking sector. The IMF, in its Finance and Development magazine (2025), notes that the demand for U.S. Treasuries could increase due to rising dollar-backed stablecoins, while also highlighting potential risks to banking sectors and fiscal accounts. Currency competition between private digital currencies, such as stablecoins, and traditional fiat money, particularly in countries facing monetary instability or high inflation, also emerges. This competition can exert pressure on central banks which aim to maintain financial stability and the value of their fiat currencies. Benigno et al. (2022) provide a theoretical framework for understanding the concept they term “Crypto-Enforced Monetary Policy Synchronization (CEMPS),” implying that the classic Impossible Trinity (where a country can not simultaneously have independent monetary policy, a fixed exchange rate, and free capital movement) becomes even less reconcilable in a two-country economy with a global cryptocurrency. This leads to tight restrictions on central banks’ monetary policy autonomy. The competition is further nuanced by the rivalry between privately issued stablecoins and CBDCs (Choi and Kim, 2024). $^{6}$

(4) Understanding the cross-border movement of stablecoins is essential for evaluating their global economic implications and for fostering effective international policy coordination. Reuter (2025) introduces a novel methodology to estimate the geographic distribution of international stablecoin flows. Cardozo et al. (2024) explore the channels through which cross-border crypto flows materialize and review various approaches to measure them. Azzimonti and Quadrini (2025) explore how stablecoins, as part of the broader digital economy, could reshape international financial markets using a multi-country model. They postulate that the “reserve demand effect” (stablecoins backed by dollar-denominated assets increase demand for U.S. Treasuries) might, in the long run, lead to lower U.S. interest rates and a rise in U.S. foreign borrowing. A key takeaway from their work is that the design of stablecoins—particularly their collateral backing—plays a pivotal role in shaping international financial flows.

(5) Stablecoins have also gained significant attention from policymakers. In 2019, concerns over regulatory and data gaps led G20 countries to agree that no stablecoin project should proceed until its associated risks and challenges are adequately addressed. Since then, extensive work has been issued by the IMF, the Financial Stability Board (FSB), and international standard setting bodies (SSBs) on the macroeconomic and financial stability implications of crypto-assets, including stablecoins. These organizations have put forward comprehensive recommendations and standards guided by the principle of “same activity, same risk, same regulation.” This establishes a minimum baseline that jurisdictions should aim to meet, addressing a range of issues common across most regions. The recommendations and standards cover financial stability, financial integrity, market integrity, investor protection, prudential, and other risks associated with crypto-assets. $^{7}$ On legal side, GENIUS Act (Guiding and Establishing National Innovation for U.S. Stablecoins) was signed into law by President Trump in July 2025, marking the first major federal framework for stablecoins in the US where its two largest stablecoins (USDT and USDC) represent around 90% of the stablecoin market capitalization. $^{8}$ Hong Kong enacted its stablecoin law, the Stablecoins Ordinance, on August 1, 2025, requiring fiat-referenced stablecoin issuers to obtain licenses from the Hong Kong Monetary Authority (HKMA). These legislative developments mark a turning point in crypto regulation, aiming to balance innovation with consumer protection and financial stability. They are expected to encourage further stablecoin issuance in the long run.

Despite the active policy discourse and regulatory advances, fundamental economic questions about stablecoins remain unresolved. For instance, Can stablecoins help stabilizing economies against shocks and fostering a stable environment for cryptocurrency adoption? What would be the macroeconomic impacts on an economy if both fiat money and stablecoins co-exist as a mean-of-payment? Would monetary policies be affected by the introduction of stablecoins? And if so, how shall we address to it? The current paper seeks to address these gaps by presenting the first comprehensive DSGE model of stablecoins, with focus on fiat-backed stablecoins. We then can quantify the model to answer the questions raised above.

To do so, we build up a DSGE model with two currencies. Based on the monetary search model as in Aruoba and Schorfheide (2011, hereafter AS) which is rooted in Lagos and Wright (2005, hereafter LW), we incorporate a stablecoin which is backed by fiat money reserve assets into a rather standard New Keynesian (NK) DSGE setting. In this model, cash-in-advance (CIA) constraint justifies the need for the fiat money. In contrast, the demand of a stablecoin comes from households who have to use the stablecoins to purchase goods with their price exclusively denominated in stablecoins. $^{9}$ Three model features distinguish a stablecoin from a fiat currency. First, stablecoins are fully digital and are anonymously traded in Decentralized Finance (DeFi) environment, aligning naturally with the Lagos-Wright framework. Fiat money $^{10}$ , by contrast, is physical legal tender. Second, the production and transaction cost of a stablecoin is much less than that of a fiat money since it is a digital currency. Third, private issuers of stablecoins peg their coins to fiat currency and try to comply this peg, in the spirit of recently passed acts such as GENIUS and HKMA Stablecoin Bill; While fiat currency relies on the trust in government and does not peg to anything.

We calibrate the model to represent the US economy in a forward-looking fashion, with particular attention to stablecoin-related parameters, which are informed by data and projections from major U.S. fiat-backed stablecoins. By feeding in multiple shocks to the model, we find that a higher stablecoin penetration rate amplifies volatilities of all major macroeconomic variables. This suggests that, as a by-product of their design, stablecoins may not contribute to macroeconomic stability. Furthermore, the model reveals a significant currency switching effect between fiat money and stablecoins, indicating the presence of currency competition in the payment system. $^{11}$

The policy implications of our findings are clear: They lend support to regulatory frameworks targeting stablecoins. Our analysis further demonstrates that well-designed prudential regulations—particularly those governing the backing ratio between stablecoins and fiat assets—can mitigate the additional macroeconomic volatility associated with stablecoin adoption. By limiting amplification effects on output and financial conditions, such regulations operate as effective “stabilizers”, helping to smooth business cycle fluctuations.

Our contributions to the literature are twofold: (a) Model innovation: this is the first paper to incorporate a micro-founded monetary search framework to endogenously justify demand for stablecoins within a New Keynesian DSGE model. We explicitly model the coexistence of fiat money and stablecoins in a unified macroeconomic setting; (b) Policy framework: We develop a theoretical foundation for applying prudential regulations to address the macroeconomic instabilities caused by stablecoins. This provides a new lens through which to evaluate digital currency policy interventions. In doing so, our paper responds to the concerns outlined in items (1), (2), (3), and (5) above. Item (4), which relates to the international dimension of stablecoin flows, remains outside the scope of this paper and would require an open-economy extension of our model.

Our paper builds closely on AS (2011) who were the first to integrate monetary search model (LW, 2005) into a rather standard NK-DSGE model with sticky price. They demonstrate that monetary frictions are as important as price stickiness in shaping optimal monetary policy, challenging the traditional emphasis on price rigidity alone. We extend their framework by introducing stablecoins, showing that monetary search frictions are also critical in understanding the role of digital currencies. More importantly, we provide a theoretical basis for using prudential regulation tools to address the intrinsic instabilities that stablecoins may introduce—an innovation beyond the original AS (2011) model.

Our paper challenges a well-known conclusion Woodford drew regarding the effectiveness of monetary policy and “cashless economy.” In his influential book Interest and Prices (2003), Woodford argues that the effectiveness of monetary policy does not rely on money as a medium of exchange but on the central bank’s ability to control the expected path of short-term nominal interest rates that anchor intertemporal prices in a given unit of account. In his New Keynesian framework, aggregate demand and inflation are determined by forward-looking Euler and Phillips-curve relations that make no reference to money demand, implying that even in a cashless economy a credible interest-rate rule suffices to influence real activity and inflation through expectations. However, this irrelevance result may fail once stablecoins are introduced in environments with money search frictions, even this movement would push the economy towards more “cashless.” In such settings, stablecoins can weaken monetary transmission by fragmenting the medium of exchange or competing for unit-of-account functions, rendering monetary policy effectiveness contingent on payment frictions and monetary dominance rather than solely on expectati

[中间内容因长度限制已省略]

10</td><td>1.8016</td><td>1.8412</td><td>1.9073</td></tr><tr><td>Y (RE)</td><td>1.7539</td><td>1.8013</td><td>1.8594</td><td>1.9319</td></tr><tr><td>Consumption</td><td>1.1863</td><td>1.2043</td><td>1.2328</td><td>1.2746</td></tr><tr><td>Investment</td><td>2.9690</td><td>3.0331</td><td>3.1339</td><td>3.2781</td></tr><tr><td>Capital</td><td>0.6671</td><td>0.6969</td><td>0.7472</td><td>0.8200</td></tr><tr><td>Inflation</td><td>0.2852</td><td>0.2906</td><td>0.3012</td><td>0.3182</td></tr><tr><td> $m^{S}$  balance</td><td>4.8902</td><td>4.1887</td><td>3.8954</td><td>3.6768</td></tr><tr><td> $m^{F}$  balance</td><td>1.3139</td><td>1.3508</td><td>1.4110</td><td>1.4997</td></tr><tr><td> $m^{S}$  price</td><td>4.0556</td><td>3.7597</td><td>3.7056</td><td>3.6848</td></tr></table>

Table 6: Macro stability for different values of $\sigma$ : $\chi M^{S} / \mathbb{Y}^{N} = 0.30$

<table><tr><td></td><td> $\nu = 0.8$ </td><td> $\nu = 1$ </td><td> $\nu = 1.2$ </td></tr><tr><td>Y (total)</td><td>1.8428</td><td>1.8016</td><td>1.7686</td></tr><tr><td>Y (RE)</td><td>1.8328</td><td>1.8013</td><td>1.7726</td></tr><tr><td>Consumption (RE)</td><td>1.2110</td><td>1.2043</td><td>1.2012</td></tr><tr><td>Investment</td><td>3.0602</td><td>3.0331</td><td>3.0183</td></tr><tr><td>Capital</td><td>0.7195</td><td>0.6969</td><td>0.6820</td></tr><tr><td>Inflation</td><td>0.2980</td><td>0.2906</td><td>0.2853</td></tr><tr><td> $m^{S}$  balance</td><td>4.6085</td><td>4.1887</td><td>3.5908</td></tr><tr><td> $m^{F}$  balance</td><td>1.3720</td><td>1.3508</td><td>1.3379</td></tr><tr><td> $m^{S}$  price</td><td>3.2832</td><td>3.7597</td><td>4.4732</td></tr></table>

Table 7: Macro stability for different values of $\nu$ : $\chi M^{S}/Y^{N}=0.30$

<table><tr><td></td><td> $\sigma = 0.02$ </td><td> $\sigma = 0.1$ </td><td> $\sigma = 0.2$ </td><td> $\sigma = 0.3$ </td><td> $\sigma = 0.4$ </td></tr><tr><td>Y (total)</td><td>1.7243</td><td>1.7254</td><td>1.7256</td><td>1.7258</td><td>1.7260</td></tr><tr><td>Y (RE)</td><td>1.7217</td><td>1.7237</td><td>1.7265</td><td>1.7292</td><td>1.7320</td></tr><tr><td>Consumption</td><td>1.1999</td><td>1.2002</td><td>1.2011</td><td>1.2020</td><td>1.2031</td></tr><tr><td>Investment</td><td>3.0153</td><td>3.0156</td><td>3.0180</td><td>3.0207</td><td>3.0235</td></tr><tr><td>Capital</td><td>0.6738</td><td>0.6738</td><td>0.6743</td><td>0.6749</td><td>0.6756</td></tr><tr><td>Inflation</td><td>0.2805</td><td>0.2805</td><td>0.2805</td><td>0.2804</td><td>0.2804</td></tr><tr><td> $m^{S}$  balance</td><td>10.5336</td><td>5.4845</td><td>4.7730</td><td>4.5507</td><td>4.4432</td></tr><tr><td> $m^{F}$  balance</td><td>1.3297</td><td>1.3301</td><td>1.3314</td><td>1.3328</td><td>1.3343</td></tr><tr><td> $m^{S}$  price</td><td>7.5864</td><td>4.2227</td><td>4.1276</td><td>4.1463</td><td>4.1640</td></tr></table>

Table 8: Macro stability for different values of $\sigma:\chi M^{S}/Y^{N}=0.02$

<table><tr><td></td><td> $\nu = 0.8$ </td><td> $\nu = 1.0$ </td><td> $\nu = 1.2$ </td></tr><tr><td>Y (total)</td><td>1.7277</td><td>1.7243</td><td>1.7210</td></tr><tr><td>Y (RE)</td><td>1.7218</td><td>1.7217</td><td>1.7216</td></tr><tr><td>Consumption</td><td>1.1984</td><td>1.1999</td><td>1.2014</td></tr><tr><td>Investment</td><td>3.0101</td><td>3.0153</td><td>3.0206</td></tr><tr><td>Capital</td><td>0.6726</td><td>0.6738</td><td>0.6750</td></tr><tr><td>Inflation</td><td>0.2807</td><td>0.2805</td><td>0.2802</td></tr><tr><td> $m^{S}$  balance</td><td>13.3477</td><td>10.5336</td><td>3.5714</td></tr><tr><td> $m^{F}$  balance</td><td>1.3275</td><td>1.3297</td><td>1.3320</td></tr><tr><td> $m^{S}$  price</td><td>4.5187</td><td>7.5864</td><td>22.3285</td></tr></table>

Table 9: Macro stability for different values of $\nu$ : $\chi M^{S}/\mathbb{Y}^{N}=0.02$

<table><tr><td></td><td> $\sigma = 0.1$ </td><td> $\sigma = 0.2$ </td><td> $\sigma = 0.3$ </td><td> $\sigma = 0.4$ </td></tr><tr><td>Y (total)</td><td>1.7422</td><td>1.7680</td><td>1.7970</td><td>1.8296</td></tr><tr><td>Y (RE)</td><td>1.7398</td><td>1.7461</td><td>1.7582</td><td>1.7778</td></tr><tr><td>Consumption</td><td>1.1989</td><td>1.2077</td><td>1.2199</td><td>1.2354</td></tr><tr><td>Investment</td><td>3.0105</td><td>3.0399</td><td>3.0807</td><td>3.1332</td></tr><tr><td>Capital</td><td>0.6736</td><td>0.6850</td><td>0.7030</td><td>0.7277</td></tr><tr><td>Inflation</td><td>0.2818</td><td>0.2835</td><td>0.2869</td><td>0.2921</td></tr><tr><td> $m^{S}$  balance</td><td>4.4450</td><td>4.1137</td><td>3.9640</td><td>3.8530</td></tr><tr><td> $m^{F}$  balance</td><td>1.3298</td><td>1.3465</td><td>1.3705</td><td>1.4023</td></tr><tr><td> $m^{S}$  price</td><td>3.8132</td><td>3.7476</td><td>3.7317</td><td>3.7186</td></tr></table>

Table 10: Macro stability for different values of $\sigma$ : Kalai solution

<table><tr><td></td><td> $\nu = 0.8$ </td><td> $\nu = 1$ </td><td> $\nu = 1.2$ </td></tr><tr><td>Y (total)</td><td>1.7896</td><td>1.7680</td><td>1.7479</td></tr><tr><td>Y (RE)</td><td>1.7622</td><td>1.7461</td><td>1.7344</td></tr><tr><td>Consumption (RE)</td><td>1.2125</td><td>1.2077</td><td>1.2047</td></tr><tr><td>Investment</td><td>3.0577</td><td>3.0399</td><td>3.0282</td></tr><tr><td>Capital</td><td>0.6960</td><td>0.6850</td><td>0.6781</td></tr><tr><td>Inflation</td><td>0.2868</td><td>0.2835</td><td>0.2814</td></tr><tr><td> $m^{S}$  balance</td><td>4.6389</td><td>4.1137</td><td>3.3035</td></tr><tr><td> $m^{F}$  balance</td><td>1.3589</td><td>1.3465</td><td>1.3383</td></tr><tr><td> $m^{S}$  price</td><td>3.0998</td><td>3.7476</td><td>4.8342</td></tr></table>

Table 11: Macro stability for different values of $\nu$ : Kalai solution

![](images/85c1468092f1d0674dab833d9921c446c166ceca932aea4ce190ea463c09a7cd.jpg)
"""
