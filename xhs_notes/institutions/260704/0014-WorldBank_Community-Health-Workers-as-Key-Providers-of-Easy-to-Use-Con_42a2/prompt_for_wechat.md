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
- 已识别机构名：`世界银行`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- CTA 必须每篇重新写，不能固定套话。它需要自然包含这些信息：更多国际信源汇编&评论，扫码交流，每日更新，汇总国际主流叙事&数据&图表，观测边际变化；汇聚了头部券商、PE/VC、投行、并购、hedge fund、资管机构、战略咨询、智库等朋友，期待交流。

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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份世界银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Community Health Workers as Key Providers of Easy-to-Use Contraceptive Injectables

Experimental Evidence from Rural Burundi

Michele Andreottola

Olivier Basenya

Victor Orozco-Olvera

Arndt Reichert

Paula Spinola

POLICY RESEARCH WORKING PAPER 11074

## Abstract

This study employs a cluster randomized controlled trial and administrative health center data to investigate the effects of authorizing community health workers to deliver a new generation of contraceptive injections directly to women during routine home visits following comprehensive training. The paper observes a significant increase of approximately 70 percent in the administered quantity of these injections, which provide average protection for three months. However, the results suggest that the intervention does not produce a statistically significant change in contraceptive coverage because of significant substitution effects away from long-acting contraceptive implants and intrauterine devices that women might otherwise have adopted.

![](images/da971e604c4a69a0698485c3ae08db4f1349595d8cd440ddcf3e365b8de9c902.jpg)

# Community Health Workers as Key Providers of Easy-to-Use Contraceptive Injectables: Experimental Evidence from Rural Burundi $^{1}$

Michele Andreottola $^{3}$ Olivier Basenya $^{4}$

Victor Orozco-Olvera $^{3}$ Arndt Reichert $^{5}$ Paula Spinola $^{2,6}$

Key words: Family planning, fertility preferences, contraceptive injections, community health workers, randomized field experiment, administrative data, health centers.
JEL Codes: I10, I15, I18, J13.

## 1 Introduction

In Sub-Saharan Africa and many other parts of the world, there persists a notable discrepancy between high fertility rates and the desire of many women for fewer children (United Nations, 2022; Dupas, 2011). This underscores the significant challenge of low utilization rates of (free-of-charge) modern contraceptive services. Governments and development organizations are increasingly focused on enhancing contraception coverage not only to support women in aligning reproductive choices with their preferences and reducing the risks associated with early childbearing (Patton et al., 2009), but also to capitalize on the substantial economic advantages such measures can provide including for instance, professional career investments of women (Ashraf et al., 2014; Goldin and Katz, 2002). $^{1}$

Accessing contraceptives typically requires women to visit health centers, as current methods, such as the most popular intramuscular contraceptive injections in Sub-Saharan Africa (Tsui et al., 2017), require administration by trained and highly-skilled health care professionals (PATH, 2018). Barriers such as travel distance, transportation costs, and logistical challenges related to scheduling appointments and arranging child care likely deter utilization. Long wait times and the risk of not finding qualified staff available may further discourage visiting health centers. Additionally, entrenched social norms and significant stigma surrounding contraception potentially constrain women from seeking birth control at health centers because of confidentiality risks (Bassi and Rasul, 2017; Munshi and Myaux, 2006). These risks arise from, for example, being seen entering health centers or the lack of private spaces within them, which can disclose a woman's contraceptive intentions. While reducing the number of health center visits, home delivery by external health care officials (i.e., professionals from outside the community) can also inadvertently disclose contraceptive use to community members who typically associate these professionals with delivering family planning services (Ndayizigiye et al., 2017).

In this randomized field experiment conducted in a rural setting, we estimate the effect of authorizing internal (i.e., local community members), low-skilled community health workers (CHWs) to administer contraceptive injectables within villages following comprehensive training. A large network of CHWs typically performs routine home visits in their area of residence for various services unrelated to contraception, thus avoiding the need for extra appointments and reducing the ability of the social environment to infer about the provision of injectable shots. $^{2}$ We take advantage of a unique setting in Burundi, where Sayana Press, a new generation of non-intramuscular contraceptive injections, had been deployed across the country in recent years. Their operational advancement consists of simplified injections by using a pre-filled syringe for subcutaneous administration, making it easier for lower-skilled professionals to administer while offering the same three-month protection as the traditional injectable method (Keith et al., 2014; Askew and Wells, 2018). However, their key attribute for rural areas—safe administration by CHWs (Burke et al., 2014)—was not yet leveraged. In coordination with health authorities willing to allow administration upon proper theoretical and practical training more broadly and with a large World Bank operation providing financing, we implemented an intervention at the health-center level to make CHWs eligible for administering non-intramuscular injections. $^{3}$ It comprised a theoretical training that would help CHWs encourage rural women to visit health centers for medical assessment and receive their initial non-intramuscular injection. After completing a practical phase, CHWs became eligible to administer injection renewals during their routine home visits in the communities. Rather than the overall effect of introducing the new generation of injectables, the randomized intervention allows us to evaluate their novel feature of a substantively easier but still equally safe administration, which makes it feasible to entrust CHWs with the deployment of contraceptive injections in remote areas.

Using detailed administrative data from health centers, we find that the average number of non-intramuscular injections administered was approximately 13 units higher per month within health centers' catchment areas due to the intervention, representing roughly a $70\%$ increase over the mean of the control group. This statistically significant increase was observed during both the theoretical and practical phases of the CHW training. After certification, there was also a strong and statistically significant increase in renewal injections administered by CHWs

during home visits.

However, the total quantity of health centers' dispensed contraceptives was not significantly affected by the intervention. Consistent with this finding, we observe a statistically significant shift away from long-acting contraceptive methods which would have been introduced in the absence of the intervention, particularly implants and intrauterine devices (IUDs). The estimated monthly decline in the use of these devices amounts to 2.7 units per health center, which greatly diminished the protection benefits of Sayana Press. Accounting for the different protection horizons of the available contraceptive methods, explorative estimates suggest that the intervention, in net terms, did not result in added contraceptive coverage throughout the analysis period.

Our paper contributes to the literature on the effects of public efforts to enhance contraceptive protection. Most existing studies focus on improving or facilitating access to health facilities and family planning centers (Dupas et al., 2024; Miller, 2010; Ferre et al., 2023; Cronin et al., 2018; Karra et al., 2022) and promoting awareness through education interventions (Strupat, 2017; Carr and Packham, 2017). Community outreach programs have also been studied (Sinha, 2005; Phillips et al., 2012; Joshi and Schultz, 2013; Desai and Tarozzi, 2011). However, none of these studies examines a family planning strategy that fully leverages the advantages of an established rural health service delivery approach centered around CHW routine home visits for the provision of modern contraceptives. Our study therefore fills an important evidence gap. It is also the first to elucidate the potential of the substantively simplified administration of the new generation of injectables to enhance contraceptive coverage rates, whose relevance is arguably further heightened when women eventually are entrusted with self-administration (Burke et al., 2018; Aderoba et al., 2023). Additionally, given the added privacy arguably associated with the examined intervention, our paper relates to previous literature on interventions aimed at enhancing the privacy of health services (Ashraf et al., 2014; Church et al., 2013; Li et al., 2013).

The remainder of this paper is structured as follows. Sections 2 and 3 present the background and the intervention under evaluation, respectively. Section 4 details the study design, including the randomization procedure, the data used, the study sample, as well as the empirical strategy adopted. Results are reported in Section 5 and further discussed in Section 6.

Finally, Section 7 concludes.

## 2 Background

## Contraceptive Coverage and Provision

Burundi has one of the lowest contraceptive coverage rates globally (United Nations, 2022). In 2017, only 21.5% of women aged 15 to 49 used reversible modern contraceptive methods such as pills, condoms, injectables, implants, and IUDs, while 6.3% used traditional methods (Burundi Institute of Statistics and Economic Studies, 2017). $^{4}$ Even though birth control tools are free of charge, there is a significant unmet need for family planning in the country, with three out of every ten women of childbearing age not using any contraceptive method despite wanting to space their next birth or stop childbearing altogether. The average number of children per woman in a union is 5.5, which exceeds their desired number of children by 1.9 (Burundi Institute of Statistics and Economic Studies, 2017).

In Burundi, contraceptive services are primarily provided by the government, especially for modern methods. Approximately 85% of modern contraceptives dispensed in the country between 2016 and 2017 were supplied by the public sector (Burundi Institute of Statistics and Economic Studies, 2017). $^{5}$ This percentage is expected to be significantly higher in rural areas, where private facilities are scarce. Within this framework, health centers play a crucial role by delivering health planning services to defined catchment areas. Each health center is staffed with skilled personnel, supported by affiliated CHWs (Agents de Santé Communautaires) and, occasionally, an associated health promotion officer (HPO, Technicien de Promotion de la Santé). Although less common, HPOs are trained healthcare professionals who possess more advanced skills compared to CHWs. HPOs and CHWs primarily operate within the community, with their affiliated health centers monitoring their activities and supplying them with the necessary resources for their home visits during monthly coordination meetings. CHWs receive performance incentives based on the delivery of a comprehensive package of community activities, with a key focus on family planning. Their tasks typically include distributing condoms and pills, as well as referring women to health centers if they express interest in the adoption of more modern family planning alternatives.

## Sayana Press Introduction

In early 2019, Sayana Press (SP) was added into the pool of modern contraceptive methods available in Burundi. SP represents a significant technological and operational advancement, enabling lower-skilled professionals to safely administer contraceptive injections (Burke et al., 2014). Unlike the incumbent injectable solution, DMPA-IM, SP uses a relatively short syringe pre-filled with the contraceptive drug (subcutaneous depo medroxyprogesterone acetate). It simplifies the administration process because the syringe is injected into the fat underneath the skin rather than into the muscle and is longer filled from a separate vial (PATH, 2018). SP has been evaluated as equally effective as the DMPA-IM, providing protection for a duration of three months (Keith et al., 2014; Askew and Wells, 2018).

An initial visit to the health center, with or without a referral from community workers, is required for eligibility assessment and administration of the initial SP injection. Renewals, needed every three months for continuous protection, were available at health centers or, depending on availability, by HPOs at the women's homes upon request. Despite being eligible to administer the injectable, the limited availability of HPOs hindered their involvement in providing SP renewals. Health center personnel and affiliated HPOs, already skilled in delivering DMPA-IM injections, required minimal training to start administering SP due to its simpler application. CHWs were not eligible to administer SP prior to the intervention.

## 3 The Intervention

The intervention being evaluated involved training CHWs to become certified and administer SP injection renewals during routine home visits within communities. This training was part of the Reproductive Health National Program under the Ministry of Health's supervision. It was financed by the World Bank through the Investing in Early Years and Fertility in Burundi project, which targeted six of the country's 18 provinces, namely Bubanza, Cankuzo, Cibitoke, Kirundo, Makamba, and Muyinga. $^{6}$

The training comprised three stages: a theoretical component, a practical internship, and a final stage where CHWs administered SP renewals within communities. The theoretical sessions, conducted at the provincial level, lasted three days and included approximately 40 CHWs from geographically connected health centers. They aimed to equip CHWs with comprehensive knowledge about Sayana Press, covering product characteristics, potential side effects, counseling skills, and general instructions on how to administer the injectable. The practical internship involved a five-day training at their affiliated health centers, where CHWs gained hands-on experience administering SP injections under the supervision of health staff. CHWs needed to apply five SP injections to complete their internship and be certified for its administration.

Figure 1 outlines the timeline for the introduction of the SP program and the CHW training sessions. Upon our engagement with the ministry, health centers started recording SP injections in January 2020. In April 2022, CHWs in the treatment arm commenced the theoretical stage of training, followed by the practical internship in October 2022. By November 2022, all health centers in the treatment group had completed the practical internship phase and were authorized to offer the injectable within their communities. Since CHW training was extended to the control group in December 2023, our analysis focuses on the period before this month.

## Figure 1: Intervention timeline

\- renewals delivered in health centers (or during home visits by HPO, with very limited capacity)

![](images/1d70ce2cdf7c1d8207c5ef75da5efadc8a2f1d1dee7d2b14b1d809310ca57eff.jpg)

## 4 Study Design

## Randomization

Our study sample includes all health centers within the six provinces targeted by the World Bank operation, where SP was already available but CHWs had not yet been trained to administer the injectable. This cluster randomized controlled trial assigned half of the 138 health centers to either a treatment or a control group. Nearly all the health centers in our study sample are classified by the government as rural (136 of 138). To improve comparability between the treatment and control groups and achieve efficiency gains (Bruhn and McKenzie, 2009), the randomization was stratified based on province, population density, total number of contraceptive products, and the proportion of alternative contraceptive injections (DMPA-IM) delivered in 2021. The group assignments for health centers were disclosed to the government on February 17, 2022.

## Data and Outcomes

The data were sourced from the National Health Information System (NHIS). This system provides monthly data at the health center level on the quantity of each contraceptive method distributed within their designated catchment area by the Burundian government as well as the number of CHW referrals to health center facilities. An important limitation of the NHIS data is the difficulty of distinguishing between true zeros and missing values when a health center reports no data for a contraceptive method in a given month. To partly address this issue, we classify observations as missing if all contraceptive methods show zero quantities for a given health center and month. This classification applies to approximately 5% of our sample.

The primary outcome of our study is the quantity of SP injections reported by health centers in the NHIS data. As secondary outcomes, we employ the quantities of relevant alternative contraceptive methods to investigate potential substitution effects.

## Study Sample

Table 1 summarizes key information on the 138 study health centers, revealing the limited capacity of health centers and low contraceptive utilization (column 1). Panel A shows that only 38 health centers (28%) had HPO availability. Among these health centers, each had only one HPO, indicating very limited in-home administration capacity before the CHW intervention rollout. On average, there were 16 CHWs serving a population of 15,775 within the health centers' catchment areas. Of this population, an estimated 3,739 are women of childbearing age, translating to roughly 230 women per CHW.

Panel B presents the baseline number of SP injections administered per month within the catchment area of health centers as well the overall quantity of all contraceptives dispensed, including injectables (SP and DMPA-IM), condoms, birth control pills, emergency contraceptive pills, implants, and intra-uterine devices. It is worth noting that this measure should be interpreted with caution given the varying protection duration across contraceptive methods. A detailed breakdown by each contraceptive method is provided in Table A1. Given the estimated average of 3,739 women of childbearing age residing in the catchment area served by each health center, these figures suggest low contraceptive coverage in our study areas. According to Burundi Institute of Statistics and Economic Studies (2017), the weighted average contraceptive coverage across the six provinces for the methods listed in Table A1 was 20.8% during the years of 2016 and 2017, just below the national average of 21.5% (Burundi Institute of Statistics and Econom

[中间内容因长度限制已省略]

. Perry, L. Bufumbo, D. Mbengue, B. M. Daff, and A. Mbonye (2014). Provider acceptability of Sayana®Press: results from community health workers and clinic-based providers in Uganda and Senegal. Contraception 89(5), 368–373.

Burundi Institute of Statistics and Economic Studies (2017). Troisième enquête démographique et de santé: 2016-2017. Technical report, Demographic and Health Survey.

Carr, J. B. and A. Packham (2017). The effects of state-mandated abstinence-based sex education on teen health outcomes. Health Economics 26(4), 403–420.

Church, K., A. Wringe, P. Fakudze, J. Kikuvi, D. Simelane, S. H. Mayhew, and T. I. Initiative (2013). Are integrated hiv services less stigmatizing than stand-alone models of care? a comparative case study from swaziland. Journal of the International AIDS Society 16(1), 17981.

Clarke, D. (2021, jul). RWOLF2: Stata module to calculate Romano-Wolf stepdown p-values for multiple hypothesis testing. Statistical Software Components, Boston College Department of Economics.

Cronin, C. J., D. K. Guilkey, and I. S. Speizer (2018). The effects of health facility access and quality on family planning decisions in urban Senegal. Health economics 27(3), 576–591.

Desai, J. and A. Tarozzi (2011). Microcredit, family planning programs, and contraceptive behavior: evidence from a field experiment in ethiopia. Demography 48(2), 749–782.

Dupas, P. (2011). Health behavior in developing countries. Annu. Rev. Econ. 3(1), 425–449.

Dupas, P., S. Jayachandran, A. Lleras-Muney, P. Rossi, J. Romo, and R. Building (2024). the Negligible Effect of Free Contraception on Fertility: Experimental Evidence From Burkina Faso. NBER Working Paper WP 32427.

Ferre, Z., P. Triunfo, and J.-I. Antón (2023). Subdermal contraceptive implants and repeat teenage motherhood: Evidence from a major maternity hospital-based program in Uruguay. Health Economics 32(12), 2679–2693.

Goldin, C. and L. F. Katz (2002). The power of the pill: Oral contraceptives and women's career and marriage decisions. Journal of political Economy 110(4), 730–770.

Hakizimana, S. and E. N. Odjidja (2021). Beyond knowledge acquisition: factors influencing family planning utilization among women in conservative communities in Rural Burundi.

Reproductive Health 18(1), 1–9.

Joshi, S. and T. P. Schultz (2013). Family planning and women's and children's health: Long-term consequences of an outreach program in matlab, bangladesh. Demography 50(1), 149–180.

Karra, M., D. Maggio, M. Guo, B. Ngwira, and D. Canning (2022). The causal effect of a family planning intervention on women's contraceptive use and birth spacing. Proceedings of the National Academy of Sciences 119(22), e2200279119.

Keith, B., S. Wood, S. Tifft, and J. Hutchings (2014). Home-based administration of Sayana® Press: Review and assessment of needs in low-resource settings. Contraception 89(5), 344–351.

Li, L., Z. Wu, L.-J. Liang, C. Lin, J. Guan, M. Jia, K. Rou, and Z. Yan (2013). Reducing HIV-related stigma in health care settings: A randomized controlled trial in China. American Journal of Public Health 103(2), 286–292.

Manirakiza, E., R. Niyonsaba, G. Nyinawumuntu, J. Nsabimana, and E. Gasaba (2022). Evaluation of Knowledge and Practice regarding Family Planning among Christians Pregnant Women of Gihanga Attending Antenatal Careat Vyizigiro Health Center, Bubanza, Burundi. Open Journal of Nursing 12(5), 363–375.

McKenzie, D. (2012). Beyond baseline and follow-up: The case for more t in experiments. Journal of Development Economics 99(2), 210–221.

Miller, G. (2010). Contraception as development? new evidence from family planning in colombia. The Economic Journal 120(545), 709–736.

Munshi, K. and J. Myaux (2006). Social norms and the fertility transition. Journal of development Economics 80(1), 1–38.

Ndayizigiye, M., M. C. Fawzi, C. T. Lively, and N. C. Ware (2017). Understanding low uptake of contraceptives in resource-limited settings: a mixed-methods study in rural Burundi. BMC Health Services Research 17(1), 1–12.

Nkunzimana, E., M. Sufiyan Babale, A. Ndoreraho, and J. Nyandwi (2021). Uptake of Modern Contraceptive Methods among Burundian Women and Associated Factors: Analysis of Demographic and Health Survey Data, Burundi 2016–2017. East African Health Research Journal 5(1), 75–81.

PATH (2018). The power to prevent pregnancy in women's hands: Dmpa-sc injectable contraception.

Patton, G. C., C. Coffey, S. M. Sawyer, R. M. Viner, D. M. Haller, K. Bose, T. Vos, J. Ferguson, and C. D. Mathers (2009). Global patterns of mortality in young people: a systematic analysis of population health data. The lancet 374 (9693), 881–892.

Phillips, J. F., E. F. Jackson, A. A. Bawah, B. MacLeod, P. Adongo, C. Baynes, and J. Williams (2012). The long-term fertility impact of the navrongo project in northern ghana. Studies in Family Planning 43(3), 175–190.

Romano, J. P. and M. Wolf (2005). Exact and approximate stepdown methods for multiple hypothesis testing. Journal of the American Statistical Association 100(469), 94–108.

Sinha, N. (2005). Fertility, child work, and schooling consequences of family planning programs: Evidence from an experiment in rural bangladesh. Economic Development and Cultural Change 54(1), 97–128.

Strupat, C. (2017). Do Targeted Reproductive Health Services Matter?—The Impact of a Midwife Program in Indonesia. Health Economics 26(12), 1667–1681.

Tsui, A. O., W. Brown, and Q. Li (2017). Contraceptive Practice in Sub-Saharan Africa. Population and development review 43(Suppl Suppl 1), 166–191.

United Nations (2022). World Family Planning 2022: Meeting the changing needs for family planning: Contraceptive use by age and method. UN DESA/POP/2022/TR/NO. 4.
"""
