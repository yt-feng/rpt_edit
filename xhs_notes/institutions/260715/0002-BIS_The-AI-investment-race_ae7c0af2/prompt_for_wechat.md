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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份国际清算银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
![](images/92e326c3d0872b5c06abac1d0bfabde7759590667258ca2ccff3a370872e8cba.jpg)

# BIS Working Papers No 1367

The AI investment race
by Phurichai Rungcharoenkitkul

Monetary and Economic Department

July 2026

JEL classification: G01, G32, L13, O33
Keywords: artificial intelligence, investment, contest theory, circular financing, boom-bust cycle, financial fragility, network

BIS Working Papers are written by members of the Monetary and Economic Department of the Bank for International Settlements, and from time to time by other economists, and are published by the Bank. The papers are on subjects of topical interest and are technical in character. The views expressed in this publication are those of the authors and do not necessarily reflect the views of the BIS or its member central banks.

This publication is available on the BIS website (www.bis.org).

© Bank for International Settlements 2026. All rights reserved. Brief excerpts may be reproduced or translated provided the source is stated.

# The AI Investment Race\*

Phurichai Rungcharoenkitkul $^{†}$

7 July 2026

## Abstract

The AI build-out ranks among the largest technology-driven investment booms in US history. Its scale, reliance on debt and circular equity ties raise questions about the boom's sustainability and financial stability. We study a dynamic contest in which firms competing for a few dominant positions over-commit resources. The over-investment leaves the sector exposed to revenue disappointment that could turn boom into bust. The larger the boom, the deeper the eventual bust. The race to commit early through debt and circular financing also makes a bust more likely. Calibrated to balance sheet and deal data, the model points to over-investment of around 1.5 times the efficient level, rising to around three times where demand is less elastic. A network analysis shows that stress in one firm could cascade to others through chains of financial exposures.

JEL: G01, G32, L13, O33

Keywords: artificial intelligence, investment, contest theory, circular financing, financial fragility, boom-bust cycle, network

## 1 Introduction

Technological breakthroughs are typically accompanied by investment booms and buoyant macroeconomic activity. Exuberance about the promise of new technologies intensifies competition among firms eager to capture a share of the revenues. The race to get ahead can result in excessive investment that makes the boom unsustainable and prone to a disruptive end. This fragility is further aggravated by the leverage that accompanies the rapid ramp-up of investment. This boom-bust pattern recurs across history, from the US canal mania in the 1830s and the British railway mania in the 1840s, to the roaring 20s and the dotcom boom in the late 90s. These episodes all ended in sharp corrections (Figure 1, panel (a)), with wider economic fallout.

The current AI build-out boom shares many of these characteristics. Total capital expenditure (capex) by the major hyperscalers has grown rapidly over the past few years and is set to exceed \$700 billion in 2026 alone. Over the coming years, aggregate investment in AI infrastructures is widely expected to run into the trillions. $^{1}$ The potential demand for AI services is clearly vast and could justify a substantial expansion in computational power. Yet relative to its pre-boom trough, the current build-out is on track to outgrow every previous episode only three years in (Figure 1, panel (a)). To the extent that contest motives also shape investment decisions this time around, the tendency toward excessive commitment raises questions about the sustainability of the current boom.

The financing of the current AI boom also displays the financial vulnerabilities that characterised earlier boom-bust episodes. Although many hyperscalers hold large cash balances, the rapid capex expansion has led some to resort increasingly to borrowing, not only through bond issuance but also through special purpose vehicles and non-bank lenders. Some firms have also engaged in so-called circular financing, in which a firm engaging in the build-out takes an equity position in an AI lab in exchange for the lab's commitment to purchase future compute. Such arrangements have enabled greater deployment of capital, but they also create interconnectedness, shown in panel (b) of Figure 1. Rising leverage and more complex financing structures have raised questions about the financial stability risks of the current AI boom.

In this paper, we examine these real and financial forces driving the AI boom in a simple setup. We develop a dynamic contest model, in which coalitions of AI firms compete with each other in a winner-take-most environment. $^{2}$ Aggregate investment determines total AI output, but most of the reward goes to a small number of contest winners rather than being shared proportionately. As a result, each coalition invests heavily to outcompete its rivals and improve its chance of capturing the reward. This contest motive creates externalities as each coalition does not internalise the effect of its investment on others' returns. The sector as a whole becomes prone to excessive investment relative to the socially optimal level. $^{3}$

Figure 1: AI boom and its financing  
(a) AI investment boom and historical episodes  
![](images/85007a4f9731a71f7ab6b24e648066d6b54055a240307146e45874f643175cb0.jpg)

(b) AI's circular financing structure  
![](images/245d2706010bf752b00877ffa700067966e410d4d6d3228404779ed95b1da6ab.jpg)  
Note: Panel (a) shows investment during five innovation-led booms as multiples of each episode's pre-boom trough: canals (US, from 1835), railways (GB, from 1843), the 1920s (US, from 1921), dotcom (US, from 1995) and AI hyperscaler capex (from 2023, with 2026 from announced guidance). Panel (b) shows the network of equity stakes and compute-purchase commitments linking hyperscalers, chipmakers, AI labs and the leading neocloud, with thicker edges for larger deals. Sources: SEC filings (10-K, 10-Q, 8-K), company announcements, earnings-call guidance, and financial press.

We then study how this contest interacts with financial fragility. Coalitions fund the build-out not only from their own resources but also through leverage and circular stakes in their partner firms. The setup yields the paper's central result: an AI boom creates fragility that undermines itself. The more capacity the sector builds, the higher the productivity bar it must clear to sustain the boom, so a larger boom is both more likely to disappoint and more damaging when it does. Unlike the usual financial accelerator which amplifies an exogenous shock to balance sheets, the vulnerability here is endogenously generated by the boom itself. The financing structure is also central to the mechanism, with debt and circular stakes both propelling the boom and exacerbating the losses during busts. The debt-financed capital is specialised, so a synchronised retrenchment forces it into a thin resale market and the recovery rate falls the more the sector as a whole has borrowed, deepening the bust. Firms foresee this fire-sale when they choose their leverage and pull back correspondingly, yet the contest motive still leaves them over-building. The equity stakes behind circular financing add to that fragility rather than diversifying it away. Real and financial exuberance are thus bound together: the competition that over-builds the boom is also what selects the fragile financing that turns it into a bust.

To gauge the magnitudes involved, we calibrate the model to AI firms' balance sheets and to the public deal records. The concentration of the sector gives unusual, if incomplete, visibility into firms' financial positions, lending discipline to the calibration. The baseline results are plausible and material. The contest externality alone delivers over-investment of around 1.5 times the social optimum, and several times higher where demand for AI services is less elastic. Anticipating the fire sale lowers borrowing somewhat, but the contest motive still leaves over-investment around 1.4 times. The financing structure then creates vulnerabilities that can reduce net economic surplus (total output minus cost of capital) by more than half relative to the boom. Once the build-out is sufficiently large, which we estimate at around \$3 tn, net economic surplus turns negative in expectation. Industry projections of \$3–4 tn overall capex over the coming years thus place the sector in the region of significant downside risks.

Finally, we relax the coalition abstraction and consider the network structure with bilateral financial linkages between hyperscalers, AI labs, chipmakers and neoclouds. A new vulnerability emerges, as a shock to one firm could propagate and become systemic. Circular financing is again central. Because a hyperscaler holds equity in the labs it backs, the failure of one lab could hit the hyperscaler's balance sheet, forcing a retrenchment from another lab, distributing the stress further. The reach of such a cascade widens as the build-out grows and as funding concentrates on the backers that bridge several labs.

Related literature. The paper draws on and contributes to three literatures. The first is the theory of contests and innovation races, in which firms competing for a prize over-invest relative to the social optimum (Tullock, 1980; Loury, 1979; Konrad, 2009), with the patent-race tradition (Reinganum, 1989; Gilbert and Newbery, 1982; Aghion and Howitt, 1992; Akcigit and Kerr, 2018) the closest analytical antecedent. Our over-investment operates on a margin distinct from the classic business-stealing result of Mankiw and Whinston (1986). There, free entry is excessive on the extensive margin: too many firms enter the market. Here the set of competitors is fixed and the distortion is intensive, as each incumbent over-builds capacity because part of the return to a marginal dollar is share taken from rivals rather than output created. We embed this contest in concave aggregate production with bounded sectoral demand, which disciplines the size of the wedge, and we add a dynamic timing dimension. The novelty of our work relative to this strand is that the over-investment is self-undermining. The productivity a build-out must reach to repay itself rises with its scale, so the contest does not merely inflate investment but co-determines the boom and the bust.

The second literature is macro-finance and the amplification of shocks through balance sheets. We build on the leverage and collateral cycles of Brunnermeier and Pedersen (2009), Geanakoplos (2010) and Adrian and Boyarchenko (2015), the net-worth feedback of Kiyotaki and Moore (1997), Bernanke and Gertler (1989) and Gertler and Kiyotaki (2010), the fire-sale and intangible-capital channels of Lorenzoni (2008), Bianchi (2011) and Crouzet and Eberly (2021), the complexity-driven feedback of Caballero and Simsek (2013), and the financial-network models (Allen and Gale, 2000; Elliott et al., 2014; Acemoglu et al., 2015; Allen, Babus, and Carletti, 2012; Cabrales, Gottardi, and Vega-Redondo, 2017). Our mechanism departs from this work in two ways. First, the bust is endogenous to the boom rather than the consequence of an exogenous shock to net worth or collateral, because the productivity threshold for averting collapse rises with the contest-driven investment itself. Second, the shock propagates through a network of equity cross-holdings, so that a single firm's failure reaches others in the network, a channel that bilateral and own-balance-sheet models do not generate.

The third literature is the economics of the AI boom itself. Closest to our focus, Caballero (2026) interprets the build-out as a speculative-growth episode, in which coordinated optimism about the technology sustains a boom, which is fragile to uncertain payoff. Wachter and Wachter (2026) combine a bottom-up reconstruction of hyperscaler capital expenditure with a theory of rare productivity booms, inferring the observed investment as a revealed bet on a large advance in AI productivity and tracing its implications for growth and asset prices. We share their diagnosis of the boom's fragility and advance a complementary hypothesis grounded on contest externalities and their interaction with financial fragility. A contest for dominance that drives the build-out also generates fire-sale destruction in the bust, creating an endogenous cycle. One advantage our approach affords is the ability to quantify over-investment and fragility, through observable financing structure and build-out, which we exploit to calibrate the model. The rest of the literature examines the AI boom from varied perspectives. Acemoglu (2024) questions the aggregate productivity gains of AI and warns of over-investment, Korinek and Vipra (2025) studies the concentration that scaling laws imply, and Eisfeldt et al. (2023) examines AI's asset-pricing implications. On the descriptive side, Van Nieuwerburgh (2026) discusses the contemporaneous macro picture that we formalise in a model. Aldasoro et al. (2026) and Eren et al. (2026) document the debt-issuance, off-balance-sheet and bank-exposure dynamics that our financing block takes as its empirical counterpart. Finally, the capital-structure-and-product-market interaction (Brander and Lewis, 1986; Bolton and Scharfstein, 1990) and the moral-hazard foundation for debt capacity (Holmström and Tirole, 1997) provide the financial-frictions building blocks.

Outline. Section 2 sets out the dynamic contest model. Section 3 derives the analytical results under the symmetric specification. Section 4 calibrates the symmetric model to current AI coalitions and reports the headline magnitudes. Section 5 extends the model to the bipartite financing network and shows how a single lab's failure cascades across firms. Section 6 concludes.

## 2 Model

The model has two building blocks: (i) a physical environment governing investment and the contest for sector revenue, and (ii) a financing structure describing how investment is funded. In this section, we describe each in turn, specify the optimisation problems faced by coalitions and a benevolent planner, and state the equilibrium concept.

## 2.1 Environment

There are n identical coalitions, each consisting of a hyperscaler and an AI laboratory, treated as a joint decision-maker. This abstraction isolates the contest and financing externalities from the effects of a detailed ownership network and asymmetric leverage, which we return to in Section 5.

There are three periods. In period 1, each coalition k chooses an investment level $I_{1,k}$ , financed by a combination of equity and debt. Because the contest rewards early scale, this period-1 commitment is strategically decisive and, once sunk, is exposed to the later productivity draw. In period 2, the AI productivity $\rho \in [0,2]$ is drawn from a symmetric beta distribution, $\mathrm{Beta}(2,2)$ with mean of 1. $\rho > 1$ captures faster AI adoption and breakthrough capabilities, while $\rho < 1$ represents disappointments. After observing the productivity, the coalitions decide how much to invest in the second period, $I_{2,k}$ . In period 3, the contest resolves, debts in periods 1 and 2 are repaid at gross rate $R_d^4$ , and the aggregate AI payoff is determined and distributed to winning coalitions' equity holders.

Coalition $k$ 's investments over the two periods dictate its effective "compute":

$$
Q _ {k} (\rho) = \left(I _ {1, k} + \theta I _ {2, k} (\rho)\right) ^ {\nu} (1 + \psi \gamma_ {k})\tag{1}
$$

$\theta \in (0,1)$ discounts second-period capacity, which is deployed later and has less time to accumulate training time before the contest resolves. Capacity deployed early thus enjoys an early-deploy premium. $\nu \in (0,1]$ reflects supply friction (GPU rationing, power and cooling bottlenecks). $(1 + \psi\gamma_k)$ represents the strategic synergy within the coalition. $\gamma_k \in [0,1]$ is the share of ‘circular financing’, taking the form of the hyperscaler’s equity stake in the lab in exchange for the lab’s compute-purchase commitments. The hyperscaler wants to lock in demand for its build-out, but cannot enforce the lab’s promise to purchase compute. An equity stake aligns the two sides’ interests, making the commitment credible. More circular financing thus yields a productivity benefit from closer partnership at rate $\psi$ , microfounded as the deadweight loss avoided by resolving this bilateral hold-up (see Appendix B.1). Equation (1) characterises $Q_k$ under partnership continuation; if the partnership is disrupted (a condition derived in Proposition 4), partnership- and debt-financed capital are partially destroyed through asset specificity, with surviving fractions governed by parameters introduced in Section 2.2.

The aggregate AI sector revenue depends on total effective compute from all coalitions subject to a concave sector demand function:

$$
\Theta (\rho) = \rho A (J (\rho)) ^ {\beta}, \quad J (\rho) = \sum_ {k = 1} ^ {n} Q _ {k} (\rho).\tag{2}
$$

The exponent $\beta < 1$ captures diminishing returns at the sector level, arising from demand saturation for AI services, complementary input bottlenecks and substitution with alternative technologies.

The contest awards $K \leq n$ winning slots through K independent Tullock lotteries with replacement. In each lottery coalition k wins with probability $I_{1,k}^{\varepsilon}Q_{k}(\rho)/\sum_{j}I_{1,j}^{\varepsilon}Q_{j}(\rho)$ . The same coalition can win multiple slots, and each slot pays $\Theta(\rho)/K$ . The expected number of slots coalition k wins is therefore

$$
\pi_ {k} (\rho) = K \frac {I _ {1 , k} ^ {\varepsilon} Q _ {k} (\rho)}{\sum_ {j} I _ {1 , j} ^ {\varepsilon} Q _ {j} (\rho)}\tag{3}
$$

and its expected gross contest payoff is $\pi_{k}(\rho)\Theta(\rho)/K=I_{1,k}^{\varepsilon}Q_{k}(\rho)\Theta(\rho)/\sum_{j}I_{1,j}^{\varepsilon}Q_{j}(\rho)$ . The parameter K cancels in expected payoffs and only represents the number of winners that share contest revenue in any given draw. The exponent $\varepsilon\geq0$ is the contest head-start elasticity: committed period-1 capacity captures contest share that the same capacity deployed later cannot replicate. Reaching the frontier first locks in users, builds the usage-and-data advantage that keeps a model ahead, and draws in the developers and researchers who compound the lead, so a latecomer with equal compute arrives to a market already taken. Appendix B.2 provides one microfoundation through a discrete-choice demand system. Setting $\varepsilon=0$ nests the simple Tullock contest 

[中间内容因长度限制已省略]

the enterprise side, so the baseline $\varepsilon = 0.20$ sits in the low-middle of this bracket, and the sensitivity range [0.1, 0.3] of Appendix C covers the calibration's neighbourhood within it. One moment the calibration does not target then falls into place: at $\varepsilon = 0.20$ the model's period-1 debt share is one third, inside the 30–40 per cent that bond issuance and lease disclosures imply for the observed build-out.

## References

Acemoglu, D. (2024). The simple macroeconomics of AI. NBER Working Paper 32487.

Acemoglu, D., A. Ozdaglar, and A. Tahbaz-Salehi (2015). Systemic risk and stability in financial networks. American Economic Review, 105(2):564–608.

Adrian, T. and N. Boyarchenko (2015). Intermediary leverage cycles and financial stability. Federal Reserve Bank of New York Staff Reports 567, August 2012, revised February 2015.

Aghion, P. and P. Howitt (1992). A model of growth through creative destruction. Econometrica, 60(2):323–351.

Akcigit, U. and W. R. Kerr (2018). Growth through heterogeneous innovations. Journal of Political Economy, 126(4):1374–1443.

Aldasoro, I., S. Doerr, and D. Rees (2026). Financing the AI boom: from cash flows to debt.
BIS Bulletin 120, January.

Allen, F. and D. Gale (2000). Financial contagion. Journal of Political Economy, 108(1):1–33.

Allen, F., A. Babus, and E. Carletti (2012). Asset commonality, debt maturity and systemic risk. Journal of Financial Economics, 104(3):519–534.

Bank for International Settlements (2026). Progress and peril. Annual Economic Report 2026, Chapter I, June.

Bernanke, B. and M. Gertler (1989). Agency costs, net worth, and business fluctuations. American Economic Review, 79(1):14–31.

Bianchi, J. (2011). Overborrowing and systemic externalities in the business cycle. American Economic Review, 101(7):3400–3426.

Bolton, P. and D. Scharfstein (1990). A theory of predation based on agency problems. American Economic Review, 80(1):93–106.

Brander, J. A. and T. R. Lewis (1986). Oligopoly and financial structure. American Economic Review, 76(5):956–970.

Brunnermeier, M. and L. Pedersen (2009). Market liquidity and funding liquidity. Review of Financial Studies, 22(6):2201–2238.

Caballero, R. J. (2026). Speculative growth and the AI “bubble”. NBER Working Paper 34722.

Caballero, R. J. and E. Farhi (2018). The safety trap. Review of Economic Studies, 85(1):223–274.

Caballero, R. J. and A. Simsek (2013). Fire sales in a model of complexity. Journal of Finance, 68(6):2549–2587.

Cabrales, A., P. Gottardi, and F. Vega-Redondo (2017). Risk-sharing and contagion in networks. Review of Financial Studies, 30(9):3086–3127.

Clark, D. J. and C. Riis (1996). A multi-winner nested rent-seeking contest. Public Choice, 87(1–2):177–184.

Crouzet, N. and J. C. Eberly (2021). Intangibles, markups, and the measurement of productivity growth. Journal of Monetary Economics, 124:S92–S109.

Eisfeldt, A. L., G. Schubert, and M. B. Zhang (2023). Generative AI and firm values. NBER Working Paper 31222.

Elliott, M., B. Golub, and M. Jackson (2014). Financial networks and contagion. American Economic Review, 104(10):3115–3153.

Eren, E., I. Krohn, and K. Todorov (2026). Financing the AI infrastructure boom: on- and off-balance sheet borrowing. BIS Quarterly Review, March.

Geanakoplos, J. (2010). The leverage cycle. NBER Macroeconomics Annual, 24:1–65.

Gertler, M. and N. Kiyotaki (2010). Financial intermediation and credit policy in business cycle analysis. Handbook of Monetary Economics, 3:547–599.

Gilbert, R. J. and D. M. G. Newbery (1982). Preemptive patenting and the persistence of monopoly. American Economic Review, 72(3):514–526.

Grossman, S. J. and O. D. Hart (1986). The costs and benefits of ownership: A theory of vertical and lateral integration. Journal of Political Economy, 94(4):691–719.

Holmström, B. and J. Tirole (1997). Financial intermediation, loanable funds, and the real sector. Quarterly Journal of Economics, 112(3):663–691.

Huang, J. (2025). Remarks on end-of-decade AI infrastructure investment. NVIDIA FY2026 second-quarter earnings call, August 2025.

Kiyotaki, N. and J. Moore (1997). Credit cycles. Journal of Political Economy, 105(2):211–248.

Konrad, K. A. (2009). Strategy and Dynamics in Contests. Oxford University Press.

Korinek, A. and J. Vipra (2025). Concentrating intelligence: Scaling and market structure in artificial intelligence. Economic Policy, 40(121):225–256.

Leland, H. E. (1994). Corporate debt value, bond covenants, and optimal capital structure. Journal of Finance, 49(4):1213–1252.

Lorenzoni, G. (2008). Inefficient credit booms. Review of Economic Studies, 75(3):809–833.

Loury, G. (1979). Market structure and innovation. Quarterly Journal of Economics, 93(3):395–410.

Mankiw, N. G. and M. D. Whinston (1986). Free entry and social inefficiency. RAND Journal of Economics, 17(1):48–58.

Reinganum, J. F. (1989). The timing of innovation: Research, development, and diffusion. In R. Schmalensee and R. D. Willig (Eds.), Handbook of Industrial Organization, vol. 1, pp. 849–908. North-Holland.

Shleifer, A. and R. W. Vishny (1992). Liquidation values and debt capacity: A market equilibrium approach. Journal of Finance, 47(4):1343–1366.

Tirole, J. (2006). The Theory of Corporate Finance. Princeton University Press.

Tullock, G. (1980). Efficient rent seeking. In J. M. Buchanan, R. D. Tollison, and G. Tullock (Eds.), Toward a Theory of the Rent-Seeking Society, pp. 97–112. Texas A&M University Press.

Van Nieuwerburgh, S. (2026). Financing the AI buildout. Journal of Economic Perspectives, forthcoming.

Wachter, J. and J. Wachter (2026). What investment data implies about the AI transition. NBER Working Paper 35290.
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
