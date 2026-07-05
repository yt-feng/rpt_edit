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
# Defence innovation and procurement reform: an empirical evaluation of the US Defense Innovation Unit

Ethan B. Kapstein, Javier Ospital and Guntram B. Wolff

## Abstract

Battlefields are evolving rapidly, with new technologies reshaping military strategy and tactics. Many of the new technologies originate in firms outside the traditional defence sector, rather than with the existing prime contractors. In the United States, the Department of Defense (DoD) created the Defense Innovation Unit (DIU) in 2015 to incentivise commercial tech companies to work on national security challenges. How successful has this new unit been in achieving its mission? We provide the first causal evaluation of the DIU's effects on defence procurement. Using administrative procurement data and a firm-level panel covering 2017-2025, and employing propensity score matching, additional firm-level covariates and a staggered difference-in-differences design, we find that the DIU has expanded both the extensive and intensive margins of defence contracting. We find not only a significant increase in the likelihood of receiving a DoD contract because of DIU treatment, but also in the size of the contract. Our findings show that defence innovation organisations can broaden and deepen the defence-supplier base. Governments updating their defence acquisition strategies in response to the lessons from recent conflicts can benefit from reforms that facilitate firm entry into procurement, overcoming the transaction cost and information asymmetry problems typical in defence markets.

## Authors

Ethan B. Kapstein is Executive Director of the Empirical Studies of Conflict Project, Princeton University Javier Ospital (octavio.ospital@bruegel.org) is a Research Assistant at Bruegel Guntram B. Wolff (guntram.wolff@bruegel.org) is a Senior Fellow at Bruegel and a Professor at Université Libre de Bruxelles

## Contents

1 Introduction 3
2 How US military procurement has changed to improve access for new firms 5
3 Data collection and descriptive statistics 8
4 Data matching 11
5 Regression methodology: difference-in-difference with staggered adoption time 14
6 Empirical results 16
7 Robustness checks 18
8 Conclusions 20
References 20
Annex 23

## 1 Introduction

The experience in Ukraine of real-time battlefield innovation and rapidly changing defence technologies is generating a stream of lessons for military forces. Ukraine has transformed its military procurement through a highly decentralised and digitalised system, sometimes described as an "Amazon for weaponry", allowing the country to become a world leader in new defence tech with multiple companies producing for the armed forces and competing for contracts. The armament strategies of the United States, the United Kingdom and France, among others, are starting to reflect these lessons. The US Department of Defense (DoD), for example, issued in November 2025 an Acquisition Transformation Strategy to accelerate delivery of high-tech weaponry $^{2}$ , while the UK Strategic Defence Review 2025 shows a substantive doctrinal shift characterised by the integration of conventional forces with digitally enabled and increasingly autonomous systems such as drones (Ministry of Defence, 2025).

In most countries, the defence ecosystem is dominated by a relatively small number of 'prime' contractors; yet Ukraine's experience and the new defence strategy documents mentioned highlight the need to enlarge the defence industrial base and tap into new, highly innovative firms. How can governments reshape procurement processes to facilitate the entry of new, predominantly commercial firms that are at the forefront of defence-related innovations or civilian innovation with large dual-use potential? The answer to that question has major implications for security and possibly also economic growth (Goolsbee, 1998; Wolff and Reinthaler, 2008; Pallante et al, 2023; Santoleri et al, 2024; Gazzani et al, 2025; Antolin-Diaz and Surico, 2025).

Howell et al (2025) provide causal evidence that the design of procurement mechanisms matters for outcomes. They evaluate a 2018 reform of the US Air Force Small Business Innovation Research (SBIR) programme and show that 'open' bottom-up solicitations, which allow firms to propose technologies rather than respond to the requests of procurement officers, significantly increase subsequent defence contracts, venture capital funding and patenting, while conventional competitions have no statistically significant effects. Earlier work on the SBIR program documents positive long-run effects on firm growth and commercialisation (Lerner, 1999). In its review of SBIR at the DoD, the National Academy of Sciences (2026) similarly found open-topic competitions have expanded participation in SBIR solicitations.

This paper builds on that literature to study another major innovation in how defence procurement is organised. Specifically, it investigates whether a key US institutional reform – the creation of the Defence Innovation Unit (DIU) in 2015 – has had a measurable impact on defence procurement from new and highly innovative firms. In seeking to draw such firms into the weapon-acquisition ecosystem, the DIU's mission was to minimise the high transaction costs for commercial tech firms that might have an interest in working with the Pentagon (Williamson, 1975, 1985) along with overcoming information asymmetries concerning the demand for defence-related products (Aghion and Tirole, 1997). These transaction costs and information asymmetries are important barriers to entry for new firms and bind procurement agencies and big incumbent contractors into mutual, self-reinforcing lock-ups (Becht et al, 2026) $^{3}$ . Has the DIU reduced these barriers to entry? Are new entrants indeed receiving DoD contracts? This Working Paper seeks to answer these questions. Government reporting has highlighted the DIU's positive contributions (GAO, 2025a), but a systematic evaluation is still missing.

Studying the effectiveness of the DIU is also relevant for policymakers in Europe, India and Canada, where governments have begun opening dedicated defence-innovation agencies, such as France's Agence de l'Innovation de Défense opened in September 2018, Canada's Defence Innovation Secure Hubs (DISHs) opened in November 2025 and Germany's Innovationszentrum Bundeswehr opened in February 2026. The Indian Ministry of Defence (MoD) even launched its Defence Acceleration Ecosystem (INDUS-X) in collaboration with the US DIU. Whether such institutional reforms successfully broaden the defence industrial base on which governments can draw remains an open empirical question.

The DIU seeks to accelerate the adoption of commercial technologies by selecting firms to develop prototypes which are then featured in its Commercial Solutions Catalogue, used by DoD agencies for procurement. We analyse whether this DIU treatment leads to measurable changes in procurement. Our analysis compares likelihood of procurement from, and value of contracts with, treated and non-treated firms. First, we use administrative data from the US General Service Administration (GSA) to match firms appearing in the DIU catalogue to a large pool of DoD contractors that are comparable in their location, sector and products sold to the DoD. In a second matching step, we use firm-level data from the database Orbis and the US Patent and Trademark Office (USPTO) to account for differences in firm revenue, age, number of employees and patenting. This two-step approach allows us to estimate the effects of DIU treatment relative to a group of untreated firms that resemble treated firms across a broad set of covariates.

Our empirical results provide strong causal evidence of the benefits of DIU: prior to engaging with DIU, our treated and comparison groups of defence contractors have the same likelihood of receiving a DoD contract; after a listing in the DIU catalogue, the likelihood of winning a defence procurement contract increases significantly. We also show that the size of procurement contracts increases substantially thanks to DIU treatment. These results are robust to numerous robustness checks.

The remainder of the paper is structured as follows. Section 2 describes policy initiatives to reform US defence procurement and the workings of the DIU in detail. Section 3 describes the administrative data for this study. Section 4 explains the propensity-score

The likelihood of a contractor winning a defence procurement contract increases significantly after listing in the DIU catalogue

matching procedure used to construct the comparison group and describes the additional firm-level data collected from Orbis and the USPTO. Section 5 presents the empirical strategy, a staggered difference-in-differences design that accounts for firm fixed effects, time effects, and variation in treatment timing. Sections 6 and 7 present our findings and robustness checks, while section 8 concludes.

## 2 How US military procurement has changed to improve access for new firms

Procurement by the US Department of Defense $^{4}$ (also called the Department of War by the Trump Administration) is a complex and lengthy process, and as such favours those firms that can navigate it and have established relations with the DoD (Sorenson, 2008). This process, governed by the Federal Acquisition Regulation (FAR), is primarily designed to acquire goods and services at scale, which is a barrier to entry for smaller firms. Further, the DoD imposes numerous operating conditions on firms (eg regarding the handling of classified information) which are costly to incorporate, creating additional barriers. The National Research Council (2014) found that the standard US procurement process favours firms with government contracting experience, because of the need to comply with these extensive administrative and reporting requirements $^{5}$ .

To reduce high transaction costs and increase the participation of small firms and startups, the DoD has introduced several grant-based innovation programmes $^{6}$ . The Small Business Innovation Research (SBIR) is a government-wide programme, overseen by the US Small Business Administration, funds research in small businesses. Launched in 1982, the programme was augmented in 1992 by the Small Business Technology Transfer (STTR) programme, which requires small businesses to partner with research institutions $^{7}$ . The DoD has made over 13,400 awards via SBIR/STTR during the programme's lifetime (NAS, 2026). The DoD is its largest user, accounting for roughly for 80 percent of SBIR/STTR spending since 2014 $^{8}$ . In 2018, the US Air Force reformed its implementation of the SBIR programme by introducing an 'open topic' solicitation mechanism (GAO, 2025b), which Howell et al (2025) showed to have been a successful policy reform $^{9}$ . Since the success of this reform, the SBIR and STTR Extension Act of 2022 mandated that the DoD expand its open topic program beyond the Air Force and apply it to the entire department.

## 2.1 The Defense Innovation Unit (DIU)

The Defense Innovation Unit (DIU) is an organisation created in 2015 to increase the uptake of commercial technologies at the DoD and to bridge the gap between defence procurement and Silicon Valley (Shah and Kirchhoff, 2024). Operating directly under the Secretary of Defense, the DIU's primary goal is to transition commercially available technologies into military use throughout the entire department. Following the creation of the DIU, the DoD has launched additional innovation organisations embedded within specific services and agencies. Howell et al (2025) study the effect of a policy change implemented by one of these organisations, AFWERX, at the Air force $^{10}$ . Instead of commercially available technologies across the department, these organisations are focused on the development of new technologies fit for the operational needs of their particular unit.

Based in Silicon Valley, the DIU engages innovative companies in the US and allied countries to develop prototypes using commercially available technologies (Beck, 2024). The DIU uses a bottom-up solicitation mechanism by calling for proposals through so-called commercial solutions openings (CSO). CSOs set out a defence problem and invite companies to submit short proposals without stipulating technical requirements that restrict participation (GAO, 2025a). The DIU evaluates how viable these proposals are and then selects companies to present prototypes $^{11}$ . Successful prototypes are then published as products by the DIU in its Commercial Solutions Catalogue, for procurement by DoD agencies $^{12}$ .

Figure 1: Number of proposals received by the DIU  
![](images/ba773ce8f9489d3e468d1b0d6e63b355b244279610b6502357c3dca6047e3a77.jpg)  
Source: Bruegel based on DIU. Note: 'Awarded' refers to 'other transaction agreements' (OTAs) granted to commercial companies, while 'rejected' means that a proposal was received but an OTA was not granted.

In 2020, the DIU received 1016 proposals in response to CSOs, more than double the previous year (Figure 1). Even though few of these proposals became operational products $^{13}$ , GAO (2025a) argues that the DIU has demonstrated the military application of commercial technologies. The GAO report uses document reviews and interviews with DIU officials and end users to assess six DIU projects $^{14}$ . In the successful cases where DIU engagement led to procurement contracts with the DoD, officials highlighted three features important for success: (1) frequent interaction between the DIU, military end users, and firms; (2) DIU staff's 'dual fluency' in both defence needs and commercial technologies; and (3) the use of broadly framed problem statements in CSOs, which allow firms to propose feasible commercial solutions rather than requiring the DoD to define a solution in advance.

This descriptive evidence suggests that the DIU can increase DoD procurement of commercial technologies by reducing information asymmetries and transaction costs between defence buyers and commercial technology suppliers $^{15}$ . Anduril Industries, a company created in 2017, develops AI software for the autonomous control of defence platforms. Since its first product was published in the Commercial Solutions Catalogue in 2021, it has grown as a DoD vendor, reaching 300 million in sales to the DoD in 2025 $^{16}$ . From 2017 to 2025, the DIU has published products from 126 other companies in its catalogue $^{17}$ across five different technological areas (Figure 2). While there has still been no empirical evaluation of the agency's effectiveness in engaging with these companies, the US Defense Innovation Board has recommended additional congressional funding for the DIU to expand its activities and focus on scaling up the production of commercial solutions (DIB, 2025).

Figure 2: Number of products published in the DIU's catalogue by technological area  
![](images/2abf73dd38dab39d081af0d4172301aea4adc14e527a67d39eb0f9fc64610101.jpg)  
Source: Bruegel based on DIU. Note: 'AI/ML': artificial intelligence and machine learning applications. 'Cyber': software for the protection of critical infrastructure and warfighting systems. 'Autonomy': small, unmanned aircraft systems, maritime systems and drones. 'Space': access to space, satellite capabilities and broadband. 'Energy': strengthening military installations and operations. 'Human Systems': capabilities that improve the war fighter's readiness, survivability and lethality.

## 3 Data collection and descriptive statistics

To evaluate the effectiveness of the DIU, we first constructed a novel dataset of DoD procurement. Our dependent variable is whether a contract was awarded by the DoD (to capture the extensive margin) and how large the contracts are (to capture the intensive margin). We compile this data from the US government's GSA database $^{18}$ . Specifically, we downloaded data on all the contracts awarded by the DoD from 2017 to $2025^{19}$ . We aggregated the value of these contracts in 2024 dollars at the level of the vendor's parent company and the year of the award to obtain the annual value of contracts with the DoD by firm.

Second, we obtained data on the DIU's engagement with companies by downloading its Commercial Solutions Catalogue $^{20}$ . We then merged this information with our procurement dataset matching company names and years $^{21}$ . The resulting dataset is a large, balanced, firm-year panel comprising 118,159 firms over eight years, covering all firms with procurement relationships with the DoD from 2017 to 2025. The large number of firms is evidence of the wide-ranging procurement relationships of the DoD: the dataset covers all kinds of purchases, including gardening and cleaning services for facilities.

In addition to annual contract values, the GSA database provides detailed information on vendor characteristics by contract, including their location, sector, business size and the types of products and services it sells. Each contract is classified using the six-digit North American Industry Classification System (NAICS) for industry and a four-character Product and Servic

[中间内容因长度限制已省略]

</td><td></td></tr></table>

Source: Bruegel. Note: estimates report the augmented $ATT(X)^{SR}$ for awarded contracts. In each specification, innovative profile is proxied by patenting activity measured over a common time window applied identically to treated and control firms. For the pre-treatment window specifications, treated firms whose treatment year falls within the relevant window are excluded to avoid contamination from post-treatment patenting. Extensive-margin coefficients are interpreted as percentage-point changes, and intensive-margin coefficients are reported in log points.

Annex Figures 1 and 2 show that the unit-placebo distributions are centred near zero in their central mass, while our actual short-run estimates, shown by the red vertical lines, lie in the right tail of each distribution. For the augmented specification on the intensive margin, the placebo density is based on 344 successful replications, since 156 of the 500 placebo replications did not converge $^{36}$ . The estimation failed in these replications because, after random assignment to treatment and conditioning on covariates, some placebo-treated firms had too few comparable control observations for reliable estimation. This does not alter the substantive conclusion, since most placebo replications are successful and continue to produce estimates centred near zero and far from the observed effect.

Figure A1: Distribution of unit-placebo tests, intensive margin of DoD awarded contracts
ATT
ATT[X]  
![](images/fa19f0afbbfb9f500c600e244086533c44eec1f63963be56cd5183b5e20c5d0f.jpg)  
Source: Bruegel. Note: the figure reports the distribution of unit-placebo $ATT^{SR}$ estimates on the intensive margin of awarded contracts. The left panel shows the baseline matched specification ( $ATT^{SR}$ ), and the right panel shows the covariate-adjusted specification ( $ATT^{SR}(X)$ ). The red vertical line marks our estimated effect for each specification. In the augmented specification, the distribution is computed from successful placebo replications only.

Figure 2: Distribution of unit-placebo tests, extensive margin of awarded contracts  
![](images/b9980aef0e7be862bd9f906b6e3d7b9dc647902778d781de846fc47576bf1e1b.jpg)  
Source: Bruegel. Note: the figure reports the distribution unit-placebo $ATT^{SR}$ estimates on the extensive margin of awarded contracts to the DoD. The left panel shows the baseline specification ( $ATT^{SR}$ ) and the right panel shows the covariate-adjusted specification ( $ATT^{SR}(X)$ ). The red vertical line marks our estimated effect for each specification.

Figures 3 and 4 show that the resulting leave-one-out estimates are clustered around the original estimated effects for both specifications and outcomes. This indicates that no single firm is driving our estimated effects; instead, they reflect a broad pattern of increases in contracting across the treated sample. In the baseline specification, all leave-one-out replications remain statistically significant. In the augmented specification, which conditions on firm age, employment, revenue and patent history, all leave-one-out replications also remain positive and statistically significant on both margins. Taken together, these results indicate that the estimated effects are broadly shared across treated firms rather than being driven by any single outlier.

Figure A3: Leave-one-out replications, baseline specification  
![](images/7f804ad66937f13e1a9f32346903724adfb3c17f19a31faeac9455b1f6aafb40.jpg)  
Source: Bruegel. Note: the figure shows the distribution of leave-one-out $ATT^{SR}$ estimates for the baseline specification. In each replication, one treated firm is omitted, and the short-run effect is re-estimated without re-matching the sample. The red vertical line marks the corresponding estimate in the full sample.

Figure A4: Leave-one-out replications, augmented specification  
![](images/315db6dbb2084f788a82209852b8028c96e38ce81181ec2f52fa017e7520f3f0.jpg)  
Source: Bruegel. Note: the figure shows the distribution of leave-one-out estimates for the augmented specification, $ATT^{SR}(X)$ . In each replication, one treated firm is omitted, and the short-run effect is re-estimated without re-matching the sample. The red vertical line marks the corresponding estimate in the full sample.

© Bruegel 2026. Bruegel publications can be freely republished and quoted according to the Creative Commons licence CC BY-ND 4.0. Please provide a full reference, clearly stating the relevant author(s) and including a prominent hyperlink to the original publication on Bruegel's website. You may do so in any reasonable manner, but not in any way that suggests the author(s) or Bruegel endorse you or your use. Any reproduction must be unaltered and in the original language. For any alteration (for example, translation), please contact us at press@bruegel.org. Publication of altered content (for example, translated content) is allowed only with Bruegel's explicit written approval. Bruegel takes no institutional standpoint. All views expressed are the researchers' own.

![](images/08afdfb80e8004990cd9577446a13f548ea6b0755e8eba7b45f91ac7ecf26596.jpg)

Bruegel, Rue de la Charité 33, B-1210 Brussels (+32) 2 227 4210
info@bruegel.org
www.bruegel.org
"""
