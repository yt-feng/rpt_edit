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
8. 不要写任何 CTA、广告、扫码、社群、知识星球、网站、域名或关注引导；系统会在最结尾统一插入固定信息。
9. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
10. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.</p>`

【CTA 要求】
- 不要输出任何 CTA。不要写“加入社群”“扫码”“星球”“完整报告领取”“网站”“域名”“关注”“星标”“更多查看”等表达。
- 文末也不要写 CTA；系统会在最结尾统一插入固定信息。
- 正文中间不要出现“如果你从某些关键词搜到这里”“单篇文章只能解决一个切片”“我每天会把……”“这篇可以沿着……”这类表达。

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
![](images/cab48ebf540713490f0573939393282128ddf923b144ca29be713f3765a3f5f4.jpg)

FSI Insights
on policy implementation
No 76

# On the comparison of capital requirements for global systemically important banks

by Patrizia Baudino, Jonathan Beissinger, Renzo Corrias, Mathias Drehmann, Egemen Eren, Burcu Erik and Nikola Tarashev

July 2026

JEL classification: G21, G28, F65, P52

Keywords: Basel Framework, banking regulation, capital buffers, capital requirements, financial stability, G-SIBs, macroprudential policy, microprudential policy, supervisory practices

FSI Insights are written by members of the Financial Stability Institute (FSI) of the Bank for International Settlements (BIS), often in collaboration with staff from supervisory agencies and central banks. The papers aim to contribute to international discussions on a range of contemporary regulatory and supervisory policy issues and implementation challenges faced by financial sector authorities. The views expressed in this publication are those of the authors and do not necessarily reflect the views of the BIS, its member central banks or the Basel-based standard-setting bodies.

Authorised by the Chair of the FSI, Fernando Restoy.

This publication is available on the BIS website (www.bis.org). To contact the BIS Global Media and Public Relations team, please email media@bis.org. You can sign up for email alerts at www.bis.org/emailalerts.htm.

© Bank for International Settlements 2026. All rights reserved. Brief excerpts may be reproduced or translated provided the source is stated.

## Contents

Executive summary....1   
Section 1 - Introduction....3   
Section 2 - The structure of the Basel III risk-based capital requirements....4 Risk-based capital stack - Pillar 1 requirements....6 Risk-based capital stack - Pillar 2 supervisory review....9 Risk-based capital stack - overall requirements....11 Risk-weighted assets....13   
Section 3 - The structure of the Basel III leverage ratio requirements....18   
Section 4 - Conclusions....24   
References....25   
Annex 1: List of G-SIBs in the sample....27   
Annex 2: Variation in capital requirements and actual capital ratios....28   
Annex 3: Variation in capital requirements (after excluding different components)....29   
Annex 4: RWA density and CET1 capital requirements....30   
Annex 5: Use of internal models and credit risk RWA densities before model restrictions....31   
Annex 6: Advanced IRB RWA density by exposure type....32   
Annex 7: Capital requirements stack by jurisdiction, over time (2014-25)....33   
Abbreviations....35

# On the comparison of capital requirements for global systemically important banks $^{1}$

Executive summary

Following the Great Financial Crisis (GFC), Basel III introduced a comprehensive package of capital reforms to bolster the resilience of the global banking system. The framework increased the quality of regulatory capital, raised minimum capital requirements and introduced regulatory buffers to absorb losses in stress and mitigate procyclicality. Alongside risk-based requirements, it added a non-risk-based leverage ratio requirement as a backstop. It also imposed additional regulatory buffers on global systemically important banks (G-SIBs), to lower the probability of their failure. Basel III has significantly strengthened banks' resilience, and the transition to full implementation is now well advanced across major jurisdictions.

As a minimum standard for internationally active banks, Basel III supports regulatory convergence across jurisdictions. The common baseline set by Basel III prevents a competitive race to the bottom and regulatory fragmentation. Comparability, combined with transparency, is essential for ensuring market discipline.

The Basel Framework gives national authorities flexibility to exceed the minimum standards. The possibility to tailor regulatory requirements to reflect structural differences across banking sectors and other supervisory considerations allows authorities to ensure that the same risk receives the same capital treatment. In particular, Pillar 2 allows supervisors to impose higher requirements where Pillar 1 requirements are seen as falling short of capturing fully all relevant risks at the bank or system level. At the same time, different practices make the comparison of capital requirements across jurisdictions more challenging.

Heterogeneous applications of Basel III have become central to current debates on how regulation may influence banks' competitiveness. Differences in the way and extent to which jurisdictions exceed the minimum Basel III standards may have fuelled perceptions of an uneven playing field. In the context of initiatives aiming at regulatory modernisation, the comparability of capital standards across jurisdictions has come under the intense scrutiny of authorities and market participants.

A key contribution of this paper is to document the various components of G-SIBs' overall capital requirement stacks and discuss potential drivers of the differences. While banks are required to publicly disclose key information on capital requirements, the information is generally not available in a centralised, consistent and machine-readable manner. The analysis in the paper relies on a hand-collected, harmonised data set from publicly available sources. It covers risk-based and leverage ratio capital requirements for 29 G-SIBs from seven jurisdictions, for the period 2014–25. These data contain information about banks' risk-weighted assets and exposure measures, and the underlying methodologies. The database also covers the different components of the capital ratio requirements, ie minima, regulatory buffers and supervisory guidance.

The data show that the composition of the capital stacks is heterogeneous across jurisdictions, and the level of capital ratio requirements is less dispersed for the highest-quality capital than for the overall measure. Minimum capital requirements are globally consistent. Some jurisdictions, however, require that they be met to a greater extent with higher-quality capital than prescribed by Basel III. In addition, heterogeneity in the capital stacks emerges as jurisdictions implement various regulatory buffers, supervisory add-ons and/or non-binding supervisory guidance, thus differently using the flexibility embedded in the Basel Framework. For instance, across the seven jurisdictions, the number of different elements of the total capital stack ranges from four to eight. In 2025 data, individual components, excluding minima, contributed to the overall ratio from as little as 0.1 percentage points on average across the banks in a jurisdiction to as much as 3 percentage points on average in another jurisdiction. The portion of the required ratios that refers to the highest-quality capital – Common Equity Tier 1 (CET1), possibly spanning several stack components – ranged from around 8 to around 11 percentage points on average across jurisdictions. At the level of the total requirements – comprising also additional Tier 1 and Tier 2 capital – the range was larger, from almost 12 to almost 17 percentage points on average.

Differences in required capital ratios stem partly from banks' different levels of systemic importance. Reflecting such differences, the current Basel III G-SIB buffers range from 1 to 2.5% of risk-weighted assets (RWA). One jurisdiction imposes higher surcharges (up to 4.5%) using a parallel method that generally yields more conservative surcharges than those prescribed by Basel III. In addition, some jurisdictions do not disclose Pillar 2 guidance or only disclose aggregate values – which can only be estimated in the data set.

The interpretation of comparisons of capital ratio requirements across jurisdictions may be distorted by differences in the approach to the computation of risk weights. There is suggestive evidence of different degrees of conservatism in risk weight measurement. The data reveal significant heterogeneity in the average risk density – ie the ratio of total assets to RWA – across jurisdictions. While this could reflect the riskiness of underlying exposures, it also seems to be influenced by the conservatism in the measurement approach and, in particular, the extent to which internal models can be used to calculate RWA. Consistent with measurement playing a role, risk densities tend to be less dispersed across banks if risk weights are counterfactually based on similar approaches. Moreover, there are indications that authorities may tend to compensate for lower risk measurement conservatism with higher capital requirements, considering that lower actual risk densities are often accompanied by higher required capital ratios.

Cross-country averages also highlight significant heterogeneity in the levels and capital composition of the leverage ratio requirements for G-SIBs. Similarly to the risk-based capital stack, national authorities have implemented different leverage ratio minima, buffer structures, capital quality requirements and adjustments to the exposure measure (the denominator of the leverage ratio). These differences result in heterogeneous capital stacks for the leverage ratio, with different levels of overall requirements.

A comprehensive cross-jurisdictional comparison requires looking at all elements of the capital requirements jointly. This includes the interaction of risk-based capital ratio requirements and RWA measurement, which jointly determine the risk-based capital requirements; the leverage ratio requirements; binding versus non-binding buffers; and supervisory expectations, which may not be fully evident in public data.

Drawing on lessons from the Basel III transition, several authorities are exploring ways to modernise their national frameworks. These efforts may help to simplify the structure of capital requirements. At the same time, if these proposals are approved, they may also affect comparisons across jurisdictions. International dialogue can help to ensure progress and avoid financial fragmentation. Meanwhile, ongoing efforts by the Basel Committee on Banking Supervision (BCBS) to facilitate access to published supervisory data will increase transparency regarding the diverse approaches taken by different jurisdictions.

## Section 1 – Introduction

1. Following the Great Financial Crisis (GFC), the Basel III framework introduced a comprehensive set of regulatory capital reforms to enhance the resilience of the global financial system. Except for some specific requirements, transition towards full implementation of the Basel III framework is well advanced. These reforms have raised minimum capital requirements, tightened the definition of regulatory capital and introduced capital buffers to absorb losses in periods of stress, prevent excessive risk-taking during financial expansions and mitigate the procyclical amplification of shocks during periods of economic stress. In addition to risk-based capital requirements, these reforms also introduced a non-risk-based leverage ratio, as a backstop to limit excessive leverage. To reduce the default probability of “too-big-to-fail” institutions, the reforms imposed additional capital surcharges for global systemically important banks (G-SIBs).

2. While the Basel III standards set minimum regulatory requirements for internationally active banks, individual jurisdictions have some flexibility to tailor the implementation. Certain elements of Basel III are principles-based rather than prescriptive, enabling authorities to adapt them to their domestic conditions, including differences in banks' risk profiles. Moreover, Basel III envisages that authorities may choose to go beyond the minimum rules and impose stricter requirements. Consequently, jurisdictions may use different tools and calibrations, making cross-country comparisons challenging.

3. Heterogeneous applications of Basel III have become central to current debates on how regulation may influence banks' competitiveness. Differences in the way and extent to which jurisdictions exceed the minimum Basel III standards may have fuelled perceptions of an uneven playing field. In the context of initiatives aiming at regulatory modernisation, the comparability of capital standards across jurisdiction has come under the intense scrutiny of authorities and market participants (see Box C for a review of some authorities' recent initiatives to modernise bank regulation).

4. To contribute to this debate, which draws comparisons across jurisdictions, this paper documents differences in G-SIBs' capital requirements – as revealed by publicly available data – and reviews potential underlying drivers. $^{2}$ Differences in G-SIBs' capital requirements may reflect banks' relative degree of systemic importance, as captured by the Basel III indicator-based methodology or as perceived by national supervisors. In addition, authorities may see different needs to compensate for the degree of conservatism embedded in the measurement of risk-weighted assets (RWA), in particular those based on banks' internal models. This paper aims to provide a rigorous review of the structure of capital requirements for G-SIBs and seeks to shed light on the various potential drivers of cross-jurisdictional differences.

5. The analysis focuses on both risk-based and leverage ratio capital requirements to provide a comprehensive perspective using a novel data set covering G-SIBs, based on public disclosures. The analysis draws on data covering 29 G-SIBs from 2014 to 2025, with granular bank-level information on capital requirements, hand-collected from public sources and harmonised across jurisdictions. It abstracts from resolution $^{3}$ and liquidity requirements. The analysis and charts in this paper are based on 2025 year-end data, unless otherwise indicated.

6. The remainder of the paper is organised as follows. Section 2 describes in detail the risk-based capital requirements, breaking them down into their main components, and analyses country-specific adjustments to the Basel III framework. This section also introduces the novel data set used in the paper (see Box A for more details). Section 3 examines the Basel III leverage ratio requirements and country-specific differences. Section 4 concludes.

## Section 2 – The structure of the Basel III risk-based capital requirements

7. The Basel III capital requirements are built on three pillars: minimum capital requirements and buffers (Pillar 1), supervisory review (Pillar 2) and market discipline (Pillar 3). Under Pillar 1, risk-based requirements prescribe a minimum proportion of bank capital to RWA:

$$
\frac {c a p i t a l}{R W A} \geq c a p i t a l r a t i o r e q u i r e m e n t.
$$

Basel III sets three minimum requirements depending on the quality of capital (Common Equity Tier 1 (CET1), Tier 1 capital and total capital), as discussed in the next subsection. The capital ratio requirements are composed of various elements which, together, make up the "capital stack". The RWA are the bank's assets weighted by their risk, according to the methodologies set by the Basel standards. The Pillar 2 supervisory review complements the Pillar 1 requirements with bank-specific add-ons to the capital stack meant to address risks not adequately covered by the Pillar 1 requirements. Finally, Pillar 3 requires public disclosures of key risk and capital adequacy metrics to improve transparency.

8. The requirements are composed of minima and buffers. The minimum requirements must be met at all times, while the buffers are meant to absorb losses in times of stress. Although banks are allowed to use these buffers while they are a going concern, breaching them triggers restrictions on the distribution of profits to a bank's shareholders. Such restrictions, known as the maximum distributable amount (MDA), address the need to ensure prompt capital restoration. Should a bank breach the minimum requirements, it would be considered a gone concern, ie deemed non-viable, and would enter resolution under the authority of the relevant resolution body.

9. In line with the objectives of Basel III, the quality and quantity of capital held by G-SIBs have increased since the start of the implementation phase. Since the beginning of the transition towards full implementation of the Basel III framework in 2014, capital requirements for banks have increased, relative to both CET1 capital – the more restrictive definition of capital – and total capital (Graph 1.A). In line with such developments, actual capital levels as a proportion of RWA have also increased (Graph 1.B).

10. Notwithstanding the overall rise in capital requirements, there have been notable differences across banks. Wide interquartile ranges reflect both variation in national implementation and differences in the business models and risk exposures of individual institutions. As of end-2025, G-SIBs' actual capital ratios appear to be relatively more homogenous compared with the variation in the requirements.

## Regulatory capital requirements and actual capital levels of G-SIBs $^{1}$

![](images/b04fa1d27047d674eb1e7be10815f65f8a36d63b9118afa221160996cc9b7fb5.jpg)  
$^{1}$ Capital requirements include minimum requirements and all legally binding buffers and capital add-ons – eg the capital conservation buffer (CCoB) and countercyclical capital buffer (CCyB), systemic surcharges and Pillar 2 requirements – and exclude non-binding supervisory recommendations, whether explicitly communicated (eg Pillar 2 guidance, Domestic Stability Buffer) or implied by stress test results (eg US Comprehensive Capital Analysis and Review prior to Q4 2020). Includes a constant sample of banks with G-SIB status as of end-2025. Includes capital requirements under the US standardised approach for US G-SIBs.  
Source: Banks' disclosures; S&P Capital IQ; authors' calculations.

11. The rest of the section discusses in detail the Pillar 1 and Pillar 2 risk-based requirements. To understand the requirements applicable to individual G-SIBs according to the specific implementation of Basel III in their home jurisdictions, the following subsections provide more information about the elements of Pillar 1 and Pillar 2 as set under Basel III, and the adjustments made to them by the home authorities.

## Banking data set

The data set used for the analysis in the paper includes 29 banks across seven jurisdictions designated as G-SIBs by the Financial Stability Board (FSB) as communicated on 27 November 2025 (see full list in Annex Table A.1). $^{①}$ Of these, seven are from the European banking union (BU), two from Canada, five from China, 

[中间内容因长度限制已省略]

capital. Non-binding capital buffers are shaded. Actual total capital ratios and requirements are shown reflecting transitional arrangements, eg for the CCoB or the G-SIB buffer. $^{2}$ Before 2020, P2R had to be fully met with CET1 capital. From 2020, P2R must be met with at least 56.25% CET1 capital, 75% with Tier 1 capital and a maximum of 25% with Tier 2 capital. For the G-SIB surcharge, the higher of the G-SIB buffer as per the FSB G-SIB list and O-SII buffer as per national discretion applies. As of end-2025, the O-SII buffer is binding for three G-SIBs in the BU. For P2G, the system-wide average is disclosed since 2018, the G-SIB average available since 2023. $^{3}$ The DSB applies system-wide to D-SIBs and has been disclosed since 2018. For the G-SIB surcharge, the higher of the G-SIB buffer as per the FSB G-SIB list and D-SIB buffer as per national discretion applies. $^{4}$ Phase-in timelines of G-SIB buffers and the CCoB are inferred from BCBS (2016b) due to limited information in banks' disclosures in earlier years.

Sources: Banks' disclosures; BCBS (2016b); ECB; S&P capital IQ; authors' calculations.

Risk-based total capital ratios: required vs actual, by jurisdiction, over time $^{1}$ (cont) Graph A.7.2

Switzerland $^{2}$  
![](images/e392bc0ab10496e824d15c3fc33cd66e81edc020a3917c310e1003e5db2924eb.jpg)

![](images/859339005947e77666ae1f9e30840cf58e645575d36ee37223fd5ca70ea608a1.jpg)

United States – advanced approach $^{4}$  
![](images/64135f634d01febe38aed1a7fa88ef22e02ebbef7aced4f4a7677668d8d5f507.jpg)

United States – standardised approach $^{4}$  
![](images/e72f96d9c030748aacc9fef95fce6931c4e933ebf6f65a6c741509ae83108e52.jpg)

$^{1}$ Shows risk-based capital requirements by jurisdiction as a percentage of RWA, on a weighted average basis. Unless otherwise indicated, all stack components must be met with CET1 capital. Non-binding capital buffers are shaded. Actual total capital ratios and requirements are shown reflecting transitional arrangements, eg for the CCoB or the G-SIB buffer. $^{2}$ The Swiss SRB CET1 buffer is defined as the remainder after subtracting the internationally applicable CCoB and G-SIB surcharge from the Swiss-specific CET1 systemic risk buffer of 5.5%. From 2016 onwards, Tier 2 capital is not eligible to meet the "P1R AT1+T2" component under the too-big-to-fail framework. $^{3}$ The UK P2B, which has been set since before 2014, is not disclosed (also not as a system-wide average) but can be visually approximated based on the Bank of England (2025) report covering the 14 largest banks in the UK. In 2014, no minimum CET1 or AT1 components were required to meet the P2A requirements. $^{4}$ Due to the two-stack approach, both advanced approach (AA) and standardised approach (SA) requirements apply separately to US G-SIBs. Under the AA, the internationally applicable CCoB applies; under the SA, the CCoB applied until October 2020 and was subsequently replaced by the dynamic stress capital buffer. For each bank, the binding approach is the one that yields a higher nominal capital requirement, calculated as AA (SA) RWA times AA (SA) capital ratio requirements. For both AA and SA, for the G-SIB surcharge, the higher of Method 1 (equivalent to the FSB G-SIB list surcharges) and Method 2 applies, where the latter replaces the substitutability indicator of Method 1 with a measure of short-term wholesale funding and applies fixed coefficients for the denominators, rather than calculating a market share based on other banks' values each year. By design, Method 2 leads to higher or equal surcharges for all US G-SIBs.

Sources: Banks' disclosures; S&P capital IQ; authors' calculations.

## Abbreviations

<table><tr><td>AA</td><td>advanced approach</td></tr><tr><td>A-IRB</td><td>advanced internal ratings-based</td></tr><tr><td>ALRB</td><td>additional leverage ratio buffer</td></tr><tr><td>AT1</td><td>Additional Tier 1</td></tr><tr><td>CCLB</td><td>countercyclical leverage buffer</td></tr><tr><td>CCoB</td><td>capital conservation buffer</td></tr><tr><td>CCyB</td><td>countercyclical capital buffer</td></tr><tr><td>CET1</td><td>Common equity Tier 1</td></tr><tr><td>CV</td><td>coefficient of variation</td></tr><tr><td>CVA</td><td>credit valuation adjustment</td></tr><tr><td>DSB</td><td>Domestic Stability Buffer</td></tr><tr><td>D-SIB</td><td>domestic systemically important bank</td></tr><tr><td>EAD</td><td>exposure at default</td></tr><tr><td>eSLR</td><td>enhanced supplementary leverage ratio</td></tr><tr><td>G-SIB</td><td>global systemically important bank</td></tr><tr><td>IMM</td><td>internal model method</td></tr><tr><td>IRB</td><td>internal ratings-based</td></tr><tr><td>IRRBB</td><td>interest rate risk in the banking book</td></tr><tr><td>LGD</td><td>loss given default</td></tr><tr><td>LR</td><td>leverage ratio</td></tr><tr><td>LREM</td><td>leverage ratio exposure measure</td></tr><tr><td>MDA</td><td>maximum distributable amount</td></tr><tr><td>O-SII</td><td>other systemically important institution</td></tr><tr><td>OLRR</td><td>overall leverage ratio requirement</td></tr><tr><td>P2A</td><td>Pillar 2A</td></tr><tr><td>P2B</td><td>Pillar 2B</td></tr><tr><td>P2R</td><td>Pillar 2 requirement</td></tr><tr><td>P2G</td><td>Pillar 2 guidance</td></tr><tr><td>PD</td><td>probability of default</td></tr><tr><td>RRE</td><td>residential real estate</td></tr><tr><td>RWA</td><td>risk-weighted assets</td></tr><tr><td>SA</td><td>standardised approach</td></tr><tr><td>SCB</td><td>stress capital buffer</td></tr><tr><td>SFT</td><td>securities financing transactions</td></tr><tr><td>SyRB</td><td>systemic risk buffer</td></tr><tr><td>T1</td><td>Tier 1</td></tr><tr><td>T2</td><td>Tier 2</td></tr></table>
"""
