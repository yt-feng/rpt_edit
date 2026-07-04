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
# Does Free Sound Too Cheap?

# The Adverse Effect of a Randomized Text Message Campaign on Program Take-up

Jeannie Annan

Estelle Koussoubé

Joséphine Tassy

Léa Rouanet

Clara Delavallade

David Evans

POLICY RESEARCH WORKING PAPER 11063

## Abstract

This study conducted a randomized experiment to improve participation in a youth employment program in Côte d'Ivoire by testing text message outreach methods. Sending text messages highlighting that the program was free only to eligible youth had no impact, but messages sent to both youth and trusted contacts led to reduced enrollment. This negative effect was smaller for women, and null when their contact was also female. Qualitative findings suggest that distrust among unfamiliar contacts contributed to this decline. The study highlights the importance of tailoring communication strategies in job training programs to increase effectiveness, considering recipients' relationships and trust.

# Does Free Sound Too Cheap? The Adverse Effect of a Randomized Text Message Campaign on Program Take-up\*

Jeannie Annan Ⓡ Estelle Koussoubé Ⓡ Joséphine Tassy
 ⓇLéa Rouanet ⓇClara Delavallade ⓇDavid Evans

Keywords: youth employment, text message incentives, program take-up.
JEL Codes: O15, J16, J24, D83

## 1 Introduction

With Sub-Saharan Africa's working-age population expected to reach 1.3 billion by 2050, making up $25\%$ of the global labor force (World Bank, 2023), and $20\%-30\%$ of youth currently not in employment, education, or training (UNICEF, 2022), there is an urgent need to equip young people with the skills required to secure meaningful employment. Although there is significant heterogeneity across programs, the average effects of technical and vocational education and training (TVET) programs on youth employment have been positive in both higher and lower income country settings (Hanushek et al., 2017; Tripney and Hombrados, 2013). However, low take-up rates significantly challenge the effectiveness of training programs in such settings (McKenzie and Woodruff, 2014). Improving uptake of TVET programs in Africa is thus a potentially important step in introducing skilled individuals into the labor market and reducing youth unemployment.

The range of TVET offerings in Africa is extensive, with participant costs varying significantly (Van Lieshout and Mehtha, 2017). Removing cost barriers has been shown to increase product usage in low- and middle-income countries (Cohen and Dupas, 2010; Kremer and Miguel, 2007) as well as participation in basic education (Duflo et al., 2023). Analogously, reducing costs could boost enrollment in training programs. One tool that has proven effective at shifting behaviors at low cost in some contexts is sending informational text messages (Grácio and Vicente 2021; Rodríguez and Saavedra 2019), making use of growing mobile phone penetration in low and middle income countries.

This study uses a randomized controlled trial to test the impact of sending text messages (i.e., short message service, or SMS messages) to youth and—in some cases—a trusted contact the youth have identified in order to increase uptake of a youth employment program in Côte d'Ivoire. We find that SMS messages that make salient the fact that the training program is free can discourage enrollment. Specifically, we show that the negative impact on enrollment is significant only when both the potential applicant and their contact are sent SMS messages. This finding is consistent with the theoretical literature that suggests pricing can serve as a signal of quality, with higher prices indicating better product quality (Bagwell and Riordan, 1991). Furthermore, in collectivist cultures such as Côte d'Ivoire, youth career choices are heavily influenced by family expectations (Akosah-Twumasi et al., 2018). The support and approval from family members are pivotal, and youth are more likely to choose careers that are perceived to enhance the family's social standing and fulfill familial obligations. Moreover, our evidence shows that this influence varies according to the gender of both the youth and their contacts. The discouragement effect is significantly less for women, and it is not statistically significant for women whose contact is also a woman.

We complement our quantitative results with qualitative interviews with the youths' contacts, which demonstrate that the perception of the program by those contacts plays a role. The decision to enroll in a training program is based on both cost and the program's reputation. We conclude the paper with a discussion on the broader implications of our findings and potential areas for future research.

## 2 Intervention, Empirical Strategy and Data

This study evaluates the impact of an SMS intervention to increase interest and take-up in the PRO-Jeunes youth employment program, which was implemented in urban and peri-urban Côte d'Ivoire by the International Rescue Committee. The PRO-Jeunes program was extensively publicized through a comprehensive communication strategy, including a public relations campaign, direct marketing, media activities, and community mobilization. The public relations campaign engaged local authorities, professional training centers, employment agencies, social centers, and private enterprises. Media activities included press releases, advertisements, and direct broadcasts on the PRO-Jeunes website and on social media platforms (Twitter, YouTube, Facebook), as well as on local and regional television and radio. Additionally, community mobilization initiatives involved meeting with community leaders, distributing flyers, and informing communities about the project launch and

enrollment sites.

Recruitment for the PRO-Jeunes program was carried out in two stages: (i) interested youth first registered, expressing their interest in the program; (ii) after screening all the applications, the project team invited eligible applicants to come to an “enrollment meeting.” According to data from the first two cohorts from the program, a significant share of eligible applicants who had expressed their interest in stage 1 did not attend the subsequent enrollment meeting in stage 2. The intervention evaluated in this study targeted the next cohort, and took place between the two stages, aiming to increase take-up from registration to enrollment.

Eligible applicants were randomly selected to receive an SMS reminding them that the program was free. $^{1}$ Youth were already informed that the program was free at pre-registration and the message served as a reminder. Randomization was stratified by gender and geographic location. The SMS message read as follows: “Come participate in an information session about PRO-Jeunes, a program offering free training, support for self-employment and employment opportunities.” In the first treatment, the SMS was randomly sent to the youth only. In the second, treatment, the SMS was sent to the youth and their listed contact person. At pre-registration, youth were asked to list a person to contact in case they could not be reached. It was specified that youth who did not live by themselves should provide the name of a person they lived with.

Our study uses administrative data collected in 2019 on a sample of 2,926 eligible applicants to the PRO-Jeunes program who had completed the pre-registration stage, during which they provided identification and contact information for their contact person, as described in Table 2. The data include variables such as date of birth, phone number, gender and geographic location for youth, and the relationship to the youth and phone number for contacts. Contact gender was inferred from the relationship variable. Listed relationships were mother/father, uncle/aunt, brother/sister, grandparents, cousin, guardian, spouse, friend and other.

The average age of youth in our sample is 23 years (25th percentile: 20 years; 75th percentile: 26 years), and half of the sample are women. In terms of contacts, about half of the youth listed a parent as their contact; another $9\%$ provided a spouse as a contact. Women are $18.5\%$ less likely than men to choose women as contacts. $15.6\%$ of women choosing their husband as a contact, compared to only $1.7\%$ of men choosing their wife (Table 1). These statistics are balanced across treatment groups (Table 2).

To complement the quantitative data, we conducted a qualitative survey to better understand the quantitative findings, including 12 individual interviews and 4 focus group discussions among youth and their contacts in August-September 2023. In the focus group discussions, men and women were interviewed separately to better understand the gender differences in the observed results.

We use the following specification for our main estimates:

$$
\begin{array}{r} E n r o l l e d _ {i} = \beta_ {0} + \beta_ {1} W o m a n _ {i} + \beta_ {2} T _ {1 i} + \beta_ {3} T _ {1 i} \cdot W o m a n _ {i} + \\ \beta_ {4} T _ {2 i} + \beta_ {5} T _ {2 i} \cdot W o m a n _ {i} + X _ {i} ^ {\prime} + \lambda_ {e, c} + \varepsilon_ {i} \end{array}\tag{1}
$$

Where $Enrolled_{i}$ is a binary variable indicating whether individual i has completed the enrollment process. $T_{1i}$ is a binary variable indicating whether the individual was in the first treatment group, where an SMS was sent to youth only. $T_{2i}$ is a binary variable indicating whether the individual was in the second treatment group, where an SMS was sent to youth and their contact. $Woman_{i}$ is a binary variable taking the value of one when the individual is a woman. $X_{i}^{\prime}$ is a vector of control variables, including age and geographic location. We also run a heterogeneity test with the same specification, comparing two sub-groups: youth with male contacts versus youth with female contacts.

## 3 Results

## 3.1 Overall impact on enrollment

Table 3 presents the treatment effects of sending the SMS to youth only or to youth and their contact on enrollment. We find that sending the SMS to youth only has no statistically significant impact on enrollment. Sending the SMS to both youth and their contact significantly decreases the probability of enrolling for both men (from $43.8\%$ to $25.2\%$ ) and women (from $38.5\%$ to $30.7\%$ ), equivalent to a $42.4\%$ decrease for men and a $20.2\%$ decrease for women, both significant at the $5\%$ level. The decrease in enrollment is significantly greater for men, with men's enrollment decreasing by 10.8 percentage points more than women's.

The fact that we only see a decrease when the contacts are included, coupled with our qualitative evidence, point to contacts being an important influence over youth's decisions. About half of youth listed a parent as their contact (Table 2). Qualitative interviews indicate that youth select the contact based on either personal relationships (family members or friends) or the contact's professional experience, and that youth expect their contact to provide significant guidance.

Qualitative interviews also indicate that while the program being free was perceived positively by both youth and contacts, it can also signal either poor quality or potential fraud. When asked what could improve the message's perception, interviewees suggested that it should illustrate the reputability of the organization providing the program. Both contacts and youth mentioned the importance of trusting the organization. This could explain why sending the SMS to youth and their contact had a worse effect on enrollment, compared to sending it to youth only. When the SMS were sent, youth had already attended a pre-registration information session, and therefore already had some information about the organization, whereas contacts had no prior interactions with the implementing organization. Contacts had no reason to have trust in the program, which could have led to them discouraging youth to register.

## 3.2 Impact on enrollment by gender of contact

Table 4 shows the treatment effects of sending SMS to youth only or to youth and their contact on program enrollment for two subsamples: column (1) shows the impact on youth whose contacts are men, and column (2) shows the impact on youth whose contacts are women. It presents a more nuanced picture when we consider the gender of the contact. Sending SMS to male youth and their contact always has a negative impact, regardless of the contact's gender: the effect corresponds to a $36.2\%$ decrease in enrollment for men with male contacts and to a $52.3\%$ for men with female contacts. The impact on women's enrollment of the SMS to youth and their contact is driven by women with male contacts. Women with male contacts are $30.3\%$ less likely to enroll, whereas women with female contacts are the only group which does not exhibit a significant decrease in enrollment. This is not explained by differences in delivery rates (Figure 1).

Our results are robust to restricting the analysis to the subsample of youth whose contact is a parent: young women whose mothers were sent the contact SMS are the only ones not discouraged by the SMS. This may suggest that women value the opportunity cost of the program for young women less than men, either because they discount less the expected quality of the program based on the free message or because they are more aware than men of the limitations in job market opportunities for young women. However, these findings may be subject to selection bias in contact choice. The observed differences in effects by contact gender could be partially attributed to unobserved characteristics of youth who choose male versus female contacts, rather than solely to the gender of the contact itself.

## 4 Discussion

Low take-up is a major barrier to the effectiveness of a large number of development programs and social policies. In some cases, that low take-up may reflect insufficient information regarding the program. This study sought to boost the uptake of a youth employment program by making the free nature of the program salient through SMS reminders sent to both applicants and their contacts.

We provide quantitative evidence that this had no significant impact on program enrolment when youth were contacted alone and a discouraging effect when youth were contacted along with a person of reference. This discouraging effect was found for all youth, except women with a female contact, and is significantly stronger among men.

Complementary qualitative evidence highlights the key role played by trust in the program in shaping recipients' perception of the SMS messages. A message highlighting the program's cost-free aspect can inadvertently backfire if the target audience lacks familiarity with the offering, leading to skepticism about quality rather than generating interest. This finding underscores the value of building trust in the program before promoting it, ensuring that recipients are familiar with and confident in its value. Additionally, our results indicate that contacts are critical in influencing youth's take-up decisions. While they can be effective channels for information dissemination, trust needs to be cultivated not only with the youth, but also with the contacts, especially for male participants and male contacts, among whom the discouraging effect was strongest.

Focusing solely on the free nature of the program may not be enough to attract participants and can even lead to distrust when interpreted as a low-quality signal. Future communication strategies should highlight the quality and value of the program to align with the expectations and aspirations of the youth and the contacts influencing their decisions. Program coordinators could actively build trust with youth and their contacts by providing them with detailed, transparent information about the program's value and quality, and incorporating this type of information in messaging strategies. Additionally, messaging strategies could be tailored to align with the specific expectations of both youth and their contacts, potentially involving pre-engagement initiatives to familiarize them with the program before direct outreach.

Gender dynamics further complicate the enrollment process, particularly among female recipients. The analysis indicates that the deterrent effect of the messaging is significantly less pronounced among women with female contacts than among women with male contacts. This heterogeneity suggests that the perception and impact of the program's promotional messages are influenced by broader social and cultural factors. However, this finding should be interpreted with caution given the potential selection bias in contact choice. Future research could address this by randomly assigning suggested contact gender to establish causal relationships, collecting more detailed data on reasons for contact selection, and exploring the interaction between youth characteristics and contact gender.

Taken together, our mixed-method study demonstrates the challenges of promoting the uptake of youth employment programs, highlighting the need for nuanced context-specific approaches. Increasing youth enrollment in skills development programs is a critical challenge, often hindered by issues of trust and perceptions of program benefits. It is crucial for program coordinators to focus on building trust and familiarity before emphasizing cost-free aspects. Messaging strategies should account for the complex dynamics between youth, their contacts, and gender. Leveraging existing trusted networks, such as religious or educational institutions, could enhance program credibility. By addressing the complexities of trust, social networks, and gender dynamics, program organizers can develop more effective strategies to improve registration outcomes and, ultimately, youth employment opportunities.

## References

Akosah-Twumasi, P., Emeto, T. I., Lindsay, D., Tsey, K., and Malau-Aduli, B. S. (2018). A systematic review of factors that influence youths career choices—the role of culture. In Frontiers in Education, volume 3, page 58. Frontiers Media SA.

Bagwell, K. and Riordan, M. H. (1991). High and declining prices signal product quality. The American Economic Review, pages 224–239.

Cohen, J. and Dupas, P. (2010). Free distribution or cost-sharing? evidence from a randomized malaria prevention experiment. The Quarterly Journal of Economics, 125(1):1–45.

Duflo, E., Dupas, P., and Kremer, M. (2023). The impact of secondary school subsidies on career trajectories in a dual labor market: Experimental evidence from ghana.

Grácio, M. and Vicente, P. C. (2021). Information, get-out-the-vote messages, and peer infl

[中间内容因长度限制已省略]

colspan="2">(1) Control</td><td colspan="2">(2) SMS to youth</td><td colspan="2">(3) SMS to youth &amp; contact</td><td rowspan="2">t-test (1)-(2)</td><td rowspan="2">t-test (1)-(3)</td><td rowspan="2">t-test (2)-(3)</td></tr><tr><td>N</td><td>Mean/SE</td><td>N</td><td>Mean/SE</td><td>N</td><td>Mean/SE</td></tr><tr><td>Woman</td><td>1466</td><td>0.487[0.013]</td><td>731</td><td>0.487[0.018]</td><td>729</td><td>0.483[0.019]</td><td>0.000</td><td>0.004</td><td>0.004</td></tr><tr><td>Age</td><td>1466</td><td>23.128[0.098]</td><td>731</td><td>23.064[0.142]</td><td>729</td><td>23.252[0.139]</td><td>0.064</td><td>-0.124</td><td>-0.188</td></tr><tr><td>Contact is a woman</td><td>1475</td><td>0.452[0.013]</td><td>736</td><td>0.413[0.018]</td><td>737</td><td>0.438[0.018]</td><td>0.039*</td><td>0.014</td><td>-0.025</td></tr><tr><td>Contact is youth&#x27;s mother</td><td>1475</td><td>0.310[0.012]</td><td>736</td><td>0.283[0.017]</td><td>737</td><td>0.299[0.017]</td><td>0.027</td><td>0.011</td><td>-0.016</td></tr><tr><td>Contact is youth&#x27;s father</td><td>1475</td><td>0.199[0.010]</td><td>736</td><td>0.196[0.015]</td><td>737</td><td>0.225[0.015]</td><td>0.004</td><td>-0.026</td><td>-0.030</td></tr><tr><td>Contact is youth&#x27;s mother or father</td><td>1475</td><td>0.509[0.013]</td><td>736</td><td>0.478[0.018]</td><td>737</td><td>0.524[0.018]</td><td>0.031</td><td>-0.015</td><td>-0.045*</td></tr><tr><td>Contact is youth&#x27;s spouse</td><td>1475</td><td>0.087[0.007]</td><td>736</td><td>0.087[0.010]</td><td>737</td><td>0.076[0.010]</td><td>-0.000</td><td>0.011</td><td>0.011</td></tr></table>

Notes: The value displayed for t-tests are the differences in the means across the groups. \*\*\* p < 0.01, \*\* p < 0.05, \* p < 0.1

Table 3: Treatment effects on enrollment rates

<table><tr><td></td><td>Completed enrollment process</td></tr><tr><td>Woman</td><td>-0.052**</td></tr><tr><td>p-value</td><td>0.033</td></tr><tr><td>sharpened q-value</td><td>0.035</td></tr><tr><td>SMS to youth</td><td>-0.023</td></tr><tr><td>p-value</td><td>0.431</td></tr><tr><td>sharpened q-value</td><td>0.275</td></tr><tr><td>SMS to youth x Woman</td><td>0.015</td></tr><tr><td>p-value</td><td>0.724</td></tr><tr><td>sharpened q-value</td><td>0.408</td></tr><tr><td>SMS to youth &amp; contact</td><td>-0.186***</td></tr><tr><td>p-value</td><td>0.000</td></tr><tr><td>sharpened q-value</td><td>0.001</td></tr><tr><td>SMS to youth &amp; contact x Woman</td><td>0.108**</td></tr><tr><td>p-value</td><td>0.011</td></tr><tr><td>sharpened q-value</td><td>0.024</td></tr><tr><td>SMS to youth: p(T + T*W)=0</td><td>0.784</td></tr><tr><td>SMS to youth &amp; contact: p(T + T*W)=0</td><td>0.011</td></tr><tr><td>Control mean</td><td>0.438</td></tr><tr><td>R-squared</td><td>0.067</td></tr><tr><td>Observations</td><td>2926</td></tr></table>

Notes: T=Treatment. W=Woman.  
\*\*\* p < 0.01, \*\* p < 0.05, \* p < 0.1  
Sharpened q-values are p-values that have been adjusted for the False Discovery Rate (FDR). Controls: Age and geographic location.

Table 4: Treatment effects on enrollment rates - by contact gender

<table><tr><td rowspan="2"></td><td colspan="3">Completed enrolment process</td></tr><tr><td>Contact is a man</td><td>Contact is a woman</td><td>T-test (1)=(2)</td></tr><tr><td></td><td>(1)</td><td>(2)</td><td></td></tr><tr><td>Woman</td><td>-0.035</td><td>-0.081**</td><td>0.249</td></tr><tr><td>p-value</td><td>0.296</td><td>0.026</td><td></td></tr><tr><td>sharpened q-value</td><td>1.000</td><td>0.027</td><td></td></tr><tr><td>SMS to youth</td><td>-0.007</td><td>-0.050</td><td>0.514</td></tr><tr><td>p-value</td><td>0.846</td><td>0.285</td><td></td></tr><tr><td>sharpened q-value</td><td>1.000</td><td>0.166</td><td></td></tr><tr><td>SMS to youth x Woman</td><td>-0.011</td><td>0.058</td><td>0.379</td></tr><tr><td>p-value</td><td>0.840</td><td>0.366</td><td></td></tr><tr><td>sharpened q-value</td><td>1.000</td><td>0.172</td><td></td></tr><tr><td>SMS to youth &amp; contact</td><td>-0.158***</td><td>-0.229***</td><td>0.191</td></tr><tr><td>p-value</td><td>0.000</td><td>0.000</td><td></td></tr><tr><td>sharpened q-value</td><td>0.001</td><td>0.001</td><td></td></tr><tr><td>SMS to youth &amp; contact x Woman</td><td>0.036</td><td>0.196***</td><td>0.033</td></tr><tr><td>p-value</td><td>0.532</td><td>0.002</td><td></td></tr><tr><td>sharpened q-value</td><td>1.000</td><td>0.004</td><td></td></tr><tr><td>SMS to youth: p(T + T*W)=0</td><td>0.652</td><td>0.852</td><td>0.553</td></tr><tr><td>SMS to youth &amp; contact: p(T + T*W)=0</td><td>0.005</td><td>0.452</td><td>0.090</td></tr><tr><td>Control mean</td><td>0.438</td><td>0.438</td><td></td></tr><tr><td>R-squared</td><td>0.065</td><td>0.076</td><td></td></tr><tr><td>Observations</td><td>1632</td><td>1294</td><td></td></tr></table>

Notes: T=Treatment. W=Woman. \*\*\* p < 0.01, \*\* p < 0.05, \* p < 0.1. Sharpened q-values are p-values that have been adjusted for the False Discovery Rate (FDR). Controls: Age and geographic location.

Figure 1: SMS Delivery Rates by Treatment Group  
![](images/c28896ed8249626fcc12078de00868807048599b1523ea599c4bacb1d79fd820.jpg)

## Appendix

## SMS on long-term benefits of the program

Another type of SMS, emphasizing the long-term benefits of the program, was sent to either youth only or youth and their contacts. Similarly to the SMS highlighting that the program was free, it had no impact on enrollment when sent exclusively to youth. However, when sent to both youth and their contacts, the impact differed by gender: it decreased enrollment for men but increased enrollment for women. Due to the inconclusive nature of these results, we have chosen to focus on the first type of SMS in this paper.
"""
