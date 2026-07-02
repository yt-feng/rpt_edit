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
# KYRGYZ REPUBLIC

## SELECTED ISSUES

July 2026

This paper on the Kyrgyz Republic was prepared by a staff team of the International Monetary Fund. It is based on the information available at the time it was completed on May 14, 2026.

Copies of this report are available to the public from

International Monetary Fund • Publication Services
PO Box 92780 • Washington, D.C. 20090

Telephone: (202) 623-7430 • Fax: (202) 623-7201

E-mail: publications@imf.org Web: http://www.imf.org

International Monetary Fund
Washington, D.C.

# KYRGYZ REPUBLIC

## SELECTED ISSUES

May 14, 2026

## Approved By

Middle East and

Central Asia

Department

Prepared By Nasir Rao, Anvar Muratkhanov, and Farid Talishli (all MCD)

## CONTENTS

## BEYOND THE POLICY RATE: A BROADER VIEW OF MONETARY AND FINANCIAL

CONDITIONS 2

A. Introduction 2

B. Methodology and Results 5

C. Conclusion and Policy Recommendations \_\_\_\_ 7

## BOX

1. Why the Policy Rate Loses Traction Under Surplus Liquidity \_\_\_\_ 4

## ANNEX

I. Methodology \_\_\_\_ 9

References 13

INFORMAL ECONOMY IN THE KYRGYZ REPUBLIC 15

A. Introduction 15

B. Labor Market and the Main Drivers of Informality in Kyrgyz Republic 15

C. Discussion and Policy Recommendations 23

## BOX

1. Tax Fragmentation and Compliance Costs in the Kyrgyz Republic \_\_\_\_ 19

References 26

# BEYOND THE POLICY RATE: A BROADER VIEW OF MONETARY AND FINANCIAL CONDITIONS $^{1}$

This study assesses the effective monetary stance in the Kyrgyz Republic amid persistent excess liquidity, rapid household credit growth, and elevated inflation pressures. It constructs a monthly Financial Conditions Index (FCI) that captures liquidity conditions, market rates, monetary aggregates, credit dynamics, and external financial factors. The results point to a marked easing in financial conditions since early 2024, driven by strong credit and monetary expansion and declining market rates, despite a relatively tight policy rate. Neutral rate estimates and the real policy rate gap corroborate that monetary conditions have at times remained accommodative in real terms, underscoring the need to complement interest-rate policy with stronger liquidity management, improved corridor operations, and targeted macroprudential tools to safeguard price stability.

## A. Introduction

1. The Kyrgyz Republic's post-COVID experience shows why monetary stance must be assessed beyond the policy rate. Although the National Bank of the Kyrgyz Republic (NBKR) has

maintained a relatively tight headline policy rate, the operational stance – captured by short-term market rates – has remained accommodative amid persistent excess liquidity driven by NBKR's domestic gold purchases, capitalization of state-owned banks to support directed lending, and the placement of government deposits in the banking system. As shown in Text Figure 1, broad money growth has accelerated, with M2X reaching 50 percent of GDP, indicating a sizable expansion of system-wide liquidity. Consequently, money

![](images/98993de0e0b9f0766ee703edb822a50c4861ab296afc2f11cbf1dd8f961d5243.jpg)

market rates (interbank rate) have stayed well below the policy rate, implying looser effective financing conditions despite a restrictive signal. This wedge weakens transmission and complicates interest-rate calibration amid strong domestic demand.

2. Easy liquidity conditions have fueled rapid credit growth, sustaining demand and price pressures. Following the initial cost-push inflation surge triggered by external shocks in 2020–22, inflation dynamics increasingly reflects domestic demand pressures. Credit growth has outpaced nominal GDP, with households relying more heavily on short-term consumer loans and mortgages. New lending has also shifted sharply toward households, whose share in total new credit reached

historically high levels in 2024–25, while corporate lending expanded more moderately. As shown in Text Figure 2, total new bank lending now exceeds 25 percent of GDP, underscoring rapid financial deepening but also rising macro-financial vulnerabilities.

3. Credit expansion has been accompanied by a rapid buildup of excess liquidity, which is sterilized primarily through short-term instruments. While the NBKR's absorption operations have been extensive, heavy reliance on overnight placements makes sterilization highly reversible and vulnerable to shifts in banks' behavior and market sentiment. Excess liquidity rose sharply during 2021–25, from around KGS 30 billion (3.8 percent of GDP) in 2021 to nearly KGS 150 billion (9.2 percent of GDP) most recently. Although this liquidity is formally absorbed by the NBKR, more than 80 percent is placed in overnight deposits and can quickly re-enter the system through renewed credit expansion (Text Figure 3). This combination can keep financing conditions easier than intended, reinforce demand pressures, and complicate the pursuit of price stability.

![](images/52f2bd519c2bd06c9800295e0eade5dfbc19ff88eaf7960d3d17fda8ed7e4be3.jpg)

![](images/40f6e5d68379bb283d1a46fd79d98042d702353a308e306f77071b2b90a8eecb.jpg)

4. These developments highlight the limitations of using the policy rate alone to assess monetary stance. With a persistent structural liquidity surplus, the NBKR has effectively operated as a net borrower from banks, with no refinancing to banks since 2022, underscoring ample liquidity in the system (Text Figure 4). In this environment, the interest rate corridor floor has become the operative anchor for short-term market rates. When the corridor floor was lowered, interbank rates and short-term yields fell even though the headline policy rate was unchanged (Text Figure 5). As a result, the policy signal became divergent from the financing conditions faced by households and firms in practice (Text Box 1), underscoring the need for a broader measure – such as an FCI – that captures liquidity, market rates, credit dynamics, and external financial influences.

Text Figure 4. Composition of Net NBKR Liabilities to Banks

(borrowing from banks minus lending to banks, KGS bn)

![](images/3c18a48436dd8bcd2178ab1ed1672a4e921336710ad8f5e782489d17bffdb23e.jpg)  
Source: NBKR and IMF staff calculations.

Text Figure 5. NBKR Interest Rate Corridor (in percent)  
![](images/6e8e2405280190e9c9fa78f72d2e97c39ab0d49d11498697bb29436bd71bef1b.jpg)  
Source: NBKR and IMF staff calculations.

## Box 1. Why the Policy Rate Loses Traction Under Surplus Liquidity

In an interest rate corridor system, the policy rate is meant to guide short-term market rates through active interbank trading. This mechanism works best when banks have a structural need to borrow liquidity. When the system is in persistent surplus, banks hold ample reserves and interbank activity becomes thin. Instead of borrowing from each other, banks place excess funds at the central bank deposit facility, earning the corridor floor rate. As a result, money market rates are pulled toward the floor rather than the headline policy rate.

In such conditions, the central bank effectively becomes a net borrower from the banking system and the corridor floor – not the policy rate – anchors short-term pricing. Unless excess liquidity is absorbed durably, policy rate changes may have limited influence on interbank rates, short-term yields, and the financing conditions faced by households and firms. Empirical evidence supports this mechanism, excess liquidity weakens monetary transmission (Saxegaard, 2006), large inflows can delink funding costs from the policy rate (Barajas et al., 2016), and banks with higher reserves may reduce credit supply less after rate hikes (Fricke et al., 2024).

5. This study develops a Financial Conditions Index (FCI) for the Kyrgyz Republic to provide a high-frequency, comprehensive gauge of the effective monetary stance beyond the policy rate. To support and interpret the FCI signals, it also presents an indicative estimate of the real neutral interest rate and compares it with the ex-ante real policy rate. Together, these tools help assess whether overall monetary conditions are effectively restrictive or accommodative in real terms and whether the policy signal is aligned with financing conditions faced by households and firms. This integrated framework is particularly useful in episodes when excess liquidity and strong credit growth weaken the pass-through of the policy rate to market rates and inflation outcomes. By combining a broad conditions-based measure with a real-rate benchmark, it helps identify when tightening “on paper” may not translate into tighter conditions in practice.

## B. Methodology and Results

## Financial Condition Index

6. The FCI draws on methodologies used in recent IMF analytical work. The index is constructed at monthly frequency and combines indicators covering policy instruments, market interest rates, monetary aggregates, credit dynamics, exchange rate movements, and global financial conditions (Text Table 1). $^{2}$ Each series is transformed so that higher values indicate tighter financial conditions and then standardized using "Z" scores to ensure comparability across variables measured in different units. The resulting FCI provides a consistent measure of how overall financial conditions evolve over time and complements the neutral-rate benchmark in assessing whether the effective monetary stance is restrictive or accommodative in practice.

<table><tr><td colspan="6">Text Table 1. Components of Financial Condition Index.</td></tr><tr><td>Policy Rate</td><td>Market Interest rates</td><td>Monetary Aggregates</td><td>Banking Credit</td><td>Exchange rate</td><td>External Indicators</td></tr><tr><td>NBKR&#x27;s policy rate</td><td>NBKR&#x27;s interbank rate, government securities rate, banking lending rate, and banking deposit rate</td><td>Monetary base and broad money</td><td>Business credits and household credits</td><td>Nominal effective exchange rate</td><td>Fed rate</td></tr></table>

7. The weights of the FCI components are derived using three complementary approaches. An equal-weight specification provides a transparent baseline, treating each indicator as equally important. Principal component analysis (PCA) is then used to extract the common underlying factor across the data, capturing shared variation in financial conditions. Finally, structural VAR (SVAR) assigns weights based on the cumulative impact of each component on real GDP growth. To keep the SVAR tractable given the large number of underlying indicators, it is implemented in two stages: PCA is first applied within key groups (market interest rates, monetary aggregates, and banking credit) to construct representative sub-indices, which are then included in the SVAR alongside real GDP growth. This multi-method approach enhances robustness by combining a transparent benchmark, a purely statistical summary measure, and an economically interpretable weighting scheme based on the estimated output effects of financial shocks.

8. Results across all three approaches point to a notable easing in financial conditions from early 2024 (Figure 6). The FCI decomposition suggests that this easing has been driven mainly by faster credit growth and monetary expansion, alongside a decline in market interest rates, even as the policy rate contribution remained tightening (Figure 7). This pattern indicates that the

restrictive policy signal was partly offset by liquidity and credit dynamics, leaving overall financing conditions more accommodative than implied by the policy rate alone.

![](images/3ed5297e0d44e91b361ee44d48b482c60dbd3c77809392d711e8905b9b90067b.jpg)  
Source: IMF staff calculations.  
Text Figure 7. FCI Decomposition (higher value = tighter financial conditions)

![](images/7cd303828d56e7bb76d3db287f5df6248bb30c41205ea97040eea60886513dfe.jpg)  
Source: IMF staff calculations.

9. Lower FCI values – indicating looser financial conditions – are associated with higher subsequent inflation. With headline inflation already above the NBKR's medium-term target range

of 5–7 percent, this pattern suggests that inflation persistence reflects not only exogenous cost-push shocks but also sustained domestic demand supported by still-easy financial conditions. This is confirmed by both the visual relationship in Text Figure 8 and by a simple regression where the sixth lag of the FCI is statistically significant for inflation. In this environment, excess liquidity and strong credit dynamics can weaken the pass-through of the policy rate to market

![](images/cb7ef3e95feb42c151ce4e9b0b8d17f804173be7ba717008fc2030def13d16f1.jpg)

pricing and borrowing conditions. The FCI therefore provides a useful leading indicator of inflationary pressures and complements the policy rate in assessing the effective monetary stance and near-term inflation risks.

## Real Neutral Rate

10. Rolling Taylor-rule estimates suggest that the current real neutral interest rate is around 2 percent. This estimation focuses on the period after the NBKR introduced its medium-term inflation objective of 5–7 percent and strengthened its interest rate based monetary policy framework. Results also suggest that the neutral rate was higher earlier in the sample averaging around 3 percent during 2014-19, before gradually declining in recent years (Text Figure 9). This is broadly consistent with earlier evidence for the Kyrgyz Republic – range of 3.5 to 4 percent at the end of 2019 determined by Teodoru and Toktonalieva (2020).

11. The real policy rate gap, defined as the difference between the ex-ante real policy rate $^{3}$ and the estimated real neutral rate, is currently negative, suggesting that monetary conditions remain accommodative in real terms despite elevated nominal policy rates (Text Figure 10). Movements in the real policy rate gap closely track the FCI, reinforcing the conclusion that effective financing conditions have loosened at times even when the policy rate signal remained tight. By contrast, the positive real rate gap in 2023–24 coincided with a tightening in financial conditions and a decline in inflation toward its medium-term target, underscoring the effectiveness of a sufficiently restrictive stance when real rates rise above the neutral benchmark.

![](images/0a2565aff78a16a1361437a806bf617e0c3a6a3f42f76b7754fed09645ac6d15.jpg)

![](images/fdae39c1e6d15445527e7b4fa3a1bbaae7c9ff2ff1f99a47d67583d2144027d7.jpg)

## C. Conclusion and Policy Recommendations

12. Overall, the analysis suggests that financial conditions in the Kyrgyz Republic have been more accommodative than implied by the headline policy rate alone. The constructed FCI indicates that conditions have eased since early 2024 despite a relatively tight policy signal, consistent with the decline in the real policy rate gap toward accommodative territory in real terms. Ample liquidity, declining market interest rates, and rapid household credit growth have supported domestic demand and weakened the pass-through of monetary tightening to market rates and borrowing conditions. In this context, maintaining a sufficiently restrictive real stance remains important to curb inflationary pressures, particularly amid strengthening demand and the announced increases in public sector wages.

13. Strengthening monetary policy transmission will require a multi-instrument policy response that addresses liquidity conditions, operational implementation, and credit dynamics. First, improving the durability of liquidity absorption is critical under persistent structural surplus: greater use of longer-tenor sterilization instruments, stronger liquidity forecasting, and reduced reliance on overnight operations would limit reversibility and prevent excess funds from quickly re-entering the system during demand upswings. Second, refining the corridor framework – including a higher corridor floor and a more symmetric design – would help anchor money market rates closer to the intended stance rather than the lower bound. Third, stronger coordination between the NBKR and the public sector- particularly the Ministry of Finance, given its role in state-owned bank capitalization and fiscal cash management – would reduce autonomous liquidity fluctuations through improved information sharing, more predictable placement of government deposits, and better alignment of fiscal operations with monetary objectives. Finally, given rapid household credit expansion, targeted macroprudential measures could complement monetary policy by containing demand-driven pressures and limiting risks to price stability. Together, these measures would narrow the wedge between the policy signal and effective financing conditions, strengthening the overall effectiveness of monetary policy.

# Annex I. Methodology

## A. Estimating the FCI Weights

## Principal Component Analysis (PCA)

1. PCA is used to summarize a large set of financial indicators into a small number of common factors while retaining as much information as possible. Technically, principal components are obtained from the eigen-decomposition of the correlation matrix of standardized variables. The first principal component captures the largest share of common variation across indicators and is interpreted as the PCA-based measure of overall financial conditions.

2. The eigenvalue of the first principal component is 4.22; with eleven standardized indicators, this implies that it explains about 38 percent of the total variance. Text Table 1 reports the corresponding factor loadings, which indicate that the common factor is driven primarily by domestic interest rates and liquidity conditions, reflecting their dominant contribution to overall variation in the data. Credit variables also load positively but play a more secondary role, while the exchange rate and external financial conditions contribute relatively little. Overall, the PCA-based FCI therefore mainly reflects domestic monetary and liquidity dynamics in the Kyrgyz Republic.

<table><tr><td colspan="2">Table 1. Kyrgyz Republic: Variables Loadings in PC1.</td></tr><tr><td>Indicator</td><td>Loadings</td></tr><tr><td>Policy Rate</td><td></td></tr><tr><td>NBKR&#x27;s Policy Rate</td><td>0.422</td></tr><tr><td>Market Interest Rates</td><td></td></tr><tr><td>NBKR&#x27;s Interbank Rate</td><td>0.406</td></tr><tr><td>Government Securities Rate</td><td>0.361</td></tr><tr><td>Banking Lending Rate</td><td>-0.000</td></tr><tr><td>Banking Deposit Rate</td><td>0.263</td></tr><tr><td>Monetary Aggregates</td><td></td></tr><tr><td>Monetary Base</td><td>0.415</td></tr><tr><td>Broad Money</td><td>0.417</td></tr><tr><td>Banking Credit</td><td></td></tr><tr><td>Business Credits</td><td>0.233</td></tr><tr><td>House

[中间内容因长度限制已省略]

ransitions. Expanding budget allocations for unemployment insurance, health coverage, and pensions would help ensure broader, more reliable coverage and reduce households' reliance on informal work as a coping strategy. Designing benefits to operate countercyclically—automatically expanding during economic downturns—would strengthen income stabilization and social resilience. At the same time, greater investment in active labor market policies, including job search assistance, vocational training, and reskilling programs, would facilitate mobility from informal to formal employment. These measures should be complemented by reforms that enhance labor market flexibility, such as more adaptable employment contracts and streamlined hiring and dismissal procedures, alongside the development of portable benefits systems to encourage formalization while protecting workers $^{9}$ .

24. Education and skills. Reforming education financing and strengthening skills development are critical for reducing informality over the medium term. Rather than focusing solely on increasing education budgets, greater emphasis should be placed on improving the efficiency and targeting of spending—particularly through investments in teacher training, curriculum modernization, and digital learning infrastructure. Expanding vocational and technical education, especially in close

partnership with private sector employers, would help address persistent skills mismatches and facilitate smoother school-to-work transitions. Introducing performance-based budgeting that links funding to measurable improvements in learning outcomes and employability could further enhance impact. In addition, increasing support for disadvantaged groups through targeted scholarships, career guidance, and skills training programs would help reduce disparities in access to formal employment.

25. Governance and institutions. Strengthening governance and institutional capacity is central to reducing informality in the Kyrgyz Republic. Increased investment in public administration reform, digitalization of government services, and anti-corruption measures would improve regulatory quality, enhance transparency, and reduce compliance costs for formal firms. Strengthening contract enforcement, property rights, and the consistency of regulatory application would build trust in institutions and incentivize participation in the formal economy. At the same time, upgrading monitoring and data systems—particularly payroll and employment databases—would enable more regular, evidence-based reviews of public sector wages and employment trends, improving fiscal management and labor market oversight. Together, these reforms would support a more predictable business environment and reinforce incentives for firms and workers to operate formally.

26. Access to finance. Expanding access to finance would support the growth of small and medium-sized enterprises and facilitate their transition to the formal sector. Improved access to credit would lower barriers to formalization and increase its net benefits for both firms and workers. These measures should be implemented cautiously to avoid undermining financial sector stability.

## References

Arnold, J. M., A. Caldera Sánchez, P. Garda, A. González Pandiella, and S. Nieto Parra (2025). Towards Better Social Protection for More Workers in Latin America: Challenges and Policy Considerations. OECD Publishing.

Asian Development Bank (2023). Skills and Employment Challenges in the Kyrgyz Republic. ADB.

Bizimana, O., and S. Arzoumanian (2023). Informality, Labor Market Dynamics, and Business Cycles in North Africa. IMF Working Paper.

International Labour Organization (2014). Transitioning from the Informal to the Formal Economy. ILO.

International Labour Organization (2017). Gender and the Informal Economy: Key Challenges and Policy Responses. ILO Working Paper No. 236 (Naoko Otobe).

International Labour Organization (2023). Labour Market Trends and Youth Transitions in the Kyrgyz Republic. ILO.

International Labour Organization (2023). Women and Men in the Informal Economy: A Statistical Update. ILO.

International Monetary Fund (2022). Informality, Development, and the Business Cycle in North Africa. IMF Departmental Paper.

International Monetary Fund (2023). Estimating the Elasticity of Formality with Respect to Taxes and Social Security Contributions. IMF Selected Issues Paper.

International Monetary Fund (2024a). Tax Potential in the Kyrgyz Republic. IMF Selected Issues Paper.

International Monetary Fund (2024b). Reducing Informality to Raise Productivity and Promote Inclusion in Uganda. IMF Selected Issues Paper.

Loayza, N. V. (2018). Informality: Why Is It So Widespread and How Can It Be Reduced? World Bank Research and Policy Brief.

Medina, L., and F. Schneider (2019). Shedding Light on the Shadow Economy: A Global Database and the Interaction with the Official One. CESifo Working Paper No. 7981.

Organisation for Economic Co-operation and Development (2024). Education, Skills, and Informality: Evidence from Global Labor Markets. OECD Publishing.

World Bank (2019). Learning for the Future: Education and Skills for Growth. World Bank.

World Bank (2021). Kyrgyz Republic: Education Sector Public Expenditure Review. World Bank.

World Bank (2022). The Long Shadow of Informality: Challenges and Policies. World Bank.

World Bank (2024). Assessment of Tax Compliance Costs for Businesses in the Kyrgyz Republic, 2012–2023. World Bank.

World Bank (2024). Kyrgyz Republic Skills and Jobs Diagnostic. World Bank.

National Development Program of the Kyrgyz Republic (2030). National Development Program of the Kyrgyz Republic until 2030.
"""
