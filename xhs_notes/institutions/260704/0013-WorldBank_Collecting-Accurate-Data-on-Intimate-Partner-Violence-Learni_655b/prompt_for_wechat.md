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
# Collecting Accurate Data on Intimate Partner Violence Learnings from Pakistan

Nasir Iqbal

Amen Jalal

Mahreen Mahmud

Kate Vyborny

POLICY RESEARCH WORKING PAPER 11077

## Abstract

Accurate measurement of intimate partner violence is challenging in face-to-face interviews due to concerns about anonymity and privacy, which can deter disclosure. In settings with high illiteracy, self-administered surveys are also impractical. To tackle these issues, this study adapted self-interviewing tools for rural-poor contexts and conducted two experiments: one to assess comprehension, and another to compare disclosure of intimate partner violence when questions were asked face-to-face first versus through audio computer-assisted interviewing first. The findings show that despite high illiteracy, respondents can effectively understand audio computer-assisted interviewing questionnaires. Additionally, initially answering questions privately via audio computer-assisted interviewing significantly increases subsequent disclosure of intimate partner violence by 41 to 57 percent during face-to-face interviews. This indicates that starting with private questioning enhances openness and consistency in reporting sensitive topics, making it a viable and effective method for improving data collection on intimate partner violence.

# Collecting Accurate Data on Intimate Partner Violence: Learnings from Pakistan\*

Nasir Iqbal Amen Jalal Mahreen Mahmud Kate Vyborny

JEL codes: J12, C83, J16

## 1 Introduction

Collecting accurate data on intimate partner violence (IPV) is difficult because of under-reporting by women, often due to the fear, stigma, and shame associated with IPV. It is especially challenging in face-to-face (F2F) interviews where the lack of anonymity can inhibit disclosure. While self-completed surveys offer more privacy, they are impractical when illiterate respondents are the target population. In low-income or rural settings, small homes increase the risk of family members overhearing conversations with enumerators, raising further ethical concerns about privacy and the potential for backlash from perpetrators. Nonetheless, ensuring accurate IPV disclosure is crucial to preventing and responding to IPV. It is especially important in experimental or quasi-experimental studies where the interventions themselves may affect disclosure of IPV, or where low rates of disclosure may undermine statistical power.

We addressed these issues by adapting existing measurement tools to better suit rural-poor settings. We also fielded two experiments, one to evaluate respondents' comprehension of questions using these adapted tools, and the other to compare the impacts of face-to-face (F2F) enumerator-administered modules versus audio computer assisted interviewing (ACASI) on IPV reporting. $^{1}$ In the second experiment, we randomized at the respondent-level, whether they answered IPV-related questions via ACASI first, or F2F first.

We have two key findings. First, our experiments demonstrate that respondents comprehend ACASI well, despite high levels of illiteracy. By randomizing the order of the Likert-scale answer options corresponding to different frequencies of IPV, we found that reporting does not depend on the ordering of the response options. This is further reinforced by the fact that we found high agreement in responses to non-IPV questions when asked via ACASI or F2F.

Second, answering sensitive questions in private first increases IPV disclosure later. Specifically, we find that F2F reports of IPV are significantly higher for respondents who previously answered the same questions using ACASI. By contrast, we observe no similar impact for non-IPV questions which were first asked by ACASI and then repeated F2F. The continued higher reporting of IPV in subsequent F2F interviews indicates that discussing sensitive topics in private initially helps respondents open up to enumerators later, or that respondents wish to maintain consistency in their responses. Overall, our results suggest that introducing respondents to sensitive questions privately, even if on a limited scale, is both feasible given high comprehension, and effective, as it helps respondents ease into difficult topics.

We implemented this experiment during in-person surveys from February to March 2023, involving over 6,000 currently married women from rural-poor households in the Layyah district of Punjab, Pakistan. All surveys were conducted by female enumerators. $^{2}$ Respondents belong to poor households which were within a +/- 5 bandwidth of a multi-dimensional poverty score cut-off used to determine eligibility for Pakistan's national unconditional cash transfers program. All respondents are under the age of 60 years and the average age is 48 years. The vast majority of these women (93%) are illiterate. We relied on questions from the standard IPV module of the Demographic and Health Surveys (DHS), and asked 7 questions on experience of physical violence, 4 on sexual violence and 4 related to injuries due to violence.

The literature so far has focused on comparing the measurement of IPV using ACASI with F2F interviews by randomizing respondents to either answer questions using ACASI or F2F surveys (Park et al., 2021; Cullen, 2023; Peterman et al., 2024). Our experiment exploits within subject randomization instead. Park et al. (2021) also report that ACASI based questioning was poorly comprehended by respondents. We successfully addressed this concern by making the ACASI interface more accessible to our respondents (i.e., illiterate, rural-poor women). Moreover, existing studies have generally found significantly higher rates of ACASI-based IPV reporting in Malawi, Rwanda and Senegal but the results are not always consistently higher across all types of IPV, and no significant differences were found for any type of IPV in Liberia (Park et al., 2021). Our study explores a context outside Africa, where the majority of the evidence has been concentrated thus far. We also contribute to a broader literature on the use of innovative survey methods beyond

F2F interviewing (e.g., list experiments) to measure IPV (Agüero and Frisancho, 2022; Joseph et al., 2017; Bulte and Lensink, 2019).

In the following, we discuss the innovations to ACASI in section 2 and the two experiments, one to test understanding of our innovations to ACASI implementation in section 3 and the results from our experiment comparing F2F and ACASI reports of IPV in section 4.

## 2 Modifying the ACASI Experience

Park et al. (2021) provide evidence that women in rural Liberia and Malawi face comprehension issues when responding to questions using ACASI, and one-third answer training questions incorrectly (i.e., questions that have objectively correct or incorrect responses). This indicates that the higher IPV responses they observe in ACASI-based interviewing may overestimate the incidence of IPV.

In light of this, we attempt to make ACASI more user-friendly to our respondents, following the guidelines from Cullen and Mahmud (2020). To allow illiterate respondents to answer the questions directly, previous studies used colored boxes or images to represent different answer options. However, this requires respondents to memorize which shapes or colors correspond to a given answer. Since that may be cognitively challenging, we worked with local enumerators in Pakistan to develop images that may make it easier for respondents to link the images to frequency-based answer options on a Likert scale (see a screenshot of the options in Figure 1).

During piloting, we also discovered that requesting our respondents to wear headphones for the ACASI module drew the attention of other household members, who at times demanded to hear what we were asking. To protect the privacy of our respondents and avoid backlash in case they reported IPV, we added some non-sensitive questions to the start of the ACASI module, which were answered on a similar scale to the IPV questions. Though we did not randomize this feature, qualitative reports from enumerators suggest that it helped diffuse distrust among other household members who at times asked to hear some of the questions once we asked them to put on headphones.

Figure 1: A training question preceding the ACASI administered IPV module  
![](images/57345b52ace0a4dd6d3421730906d12f6b350643b9b5ab6da968cfd1bdf4ee98.jpg)

## 3 Experiment 1: Do respondents understand ACASI?

To test if the modification to visual response options improved women's comprehension and use of ACASI, we did two measurement experiments. In one experiment, we randomized the order of the frequency answer options: for half the respondents, the options appeared in ascending order and for the other half, they appeared in descending order. This tests whether women correctly associated the response options with the frequency of IPV acts, rather than simply choosing the first option. We do not find a statistically significant difference in the frequency of violence across the two orderings (Table 1). We interpret this as evidence that the respondents understood the mapping of images to answer the choices accurately.

Table 1: Impact of the Measurement Experiment I on ACASI IPV Reporting

<table><tr><td></td><td>(1)Push, Shake, Throw</td><td>(2)Slap</td><td>(3)Twist arm,Pull hair</td><td>(4)Punch</td><td>(5)Choke,Burn</td><td>(6)Threaten to attack with weapon</td></tr><tr><td>Ascending</td><td>-0.0156(0.0135)</td><td>0.0100(0.0139)</td><td>-0.00549(0.0131)</td><td>-0.00407(0.0130)</td><td>-0.00385(0.0115)</td><td>-0.000552(0.00921)</td></tr><tr><td>Observations</td><td>6133</td><td>6134</td><td>6135</td><td>6134</td><td>6135</td><td>6135</td></tr></table>

Notes: The table reports results from an experiment where we randomised the order of the frequency answer options. Ascending is an indicator of the order options displayed to the respondent in ascending order for questions related to the experience of violence asked using ACASI. The dependent variables take on the value 0 if the respondent did not experience the type of violence in the last 6 months, 1.5 if she experienced it once or twice and 3 if she experienced it three or more times. Standard errors are in parentheses. \* p < 0.10, \*\* p < 0.05, \*\*\* p < 0.01.

Second, we asked generic (non-IPV) questions on food consumption to women using both F2F and ACASI methods. We find a very high agreement between ACASI and F2F: 94% agreement for the question “How many times did your husband eat meat in last 7 days?” 96% for the question “How many times did your husband eat fruit in last 7 days?” and 95% for the question “How many times did your husband eat eggs in last 7 days?” This provides additional evidence that respondents understood how to use ACASI.

## 4 Experiment 2: Does answering sensitive questions using ACASI change disclosure face-to-face?

We study whether asking the same respondent questions related to their experience of violence F2F versus via ACASI affects their rate of IPV reporting. We chose two questions for the experiment: one on physical violence “During the last 6 months, how often did your husband slap you?” and one on injuries sustained as a result of violence “During the last 6 months, did you ever have cuts or bruises or aches as a result of what your husband did to you?" For half the respondents, these two questions were asked F2F first and then via ACASI; and for the other half, the questions were asked via ACASI first and F2F later. We present respondents with the following answer options: three or more times, once or twice, and never. Our experiment design is illustrated in Figure 2. The F2F and ACASI questions appeared in the questionnaire with a gap and allowed us to experimentally study how it might change responses. Beyond these two questions, the full DHS IPV module on physical and sexual violence, and injuries was asked to everyone using ACASI only. For the respondents who got the ACASI-first treatment, the two selected questions were followed by the rest of the ACASI-based IPV module in standard order. In a separate section of the questionnaire, the two questions were then asked again F2F. Respondents who were randomized into F2F were first asked two F2F questions, followed by all the ACASI questions in the standard order.

In Figure 3 we report the mean value for respondents who were randomized to either answer the IPV questions using ACASI first (“ACASI First”) or to answer them F2F initially and ACASI later (“ACASI Second”). We report both the frequency and incidence of the two IPV-related questions. We find that F2F reports for both the frequency and incidence of violence are significantly higher for respondents who have already answered the question using ACASI. Specifically, the reported frequency of slaps is 57% higher and the reported frequency of cuts is 47% higher. On the extensive margin, the ACASI Second group has a 6.2% likelihood of reporting any incidence of slapping in the past six months. In comparison, this likelihood is 3.2 percentage points (52%) higher when the questions were asked via ACASI first. A similar trend is observed for the likelihood of reporting cuts: women in the ACASI Second group have a 3.9% likelihood of reporting being cut, while the ACASI First group reports a 1.6 percentage point (41%) higher likelihood. These findings suggest that respondents may become more comfortable disclosing sensitive information to enumerators after first answering privately. $^{3}$

Figure 2: Design of the Measurement Experiment II  
![](images/6fef6f4f8b12a7f05d0e53842bad153ffed524588a4ea587fac2be7364148147.jpg)

Figure 3: Impact of the Measurement Experiment II on Face-to-Face IPV Reporting  
![](images/59baf4356c0f4f8ede32f1e67cc8440c03ea91a79d7308f9b8849e3bc1331568.jpg)  
Notes: The figure shows results from an experiment where for half the respondents two questions were asked F2F first and then via ACASI; and for the other half, the questions were asked via ACASI first and F2F later. Each bar shows the mean value for the outcome reported F2F. ACASI first is the mean value for the respondents who were asked the IPV questions using ACASI first and ACASI second is the mean value for those who were asked the IPV questions using ACASI second. Slaps Frequency is the response to the question "During the last 6 months, how often did your husband slap you?" and Cuts Frequency is the response to the question "During the last 6 months, did you ever had cuts or bruises or aches as a result of what your husband did to you?". The responses are on a scale of 0 to 2 (0: never, 1.5: once or twice, and 3: three or more times). Slaps indicator and cuts indicator are indicator variables for any experience of this type of IPV by the respondent in the last 6 months. Black vertical lines indicate $90\%$ confidence intervals on the test for mean difference for each outcome between ACASI First and ACAI Second.

## 5 Conclusion

In this note, we report results from two measurement experiments with 6,135 women in rural Punjab, Pakistan, who were asked questions related to their experience of intimate partner violence. The key takeaways are:

\- There is high comprehension of survey questions asked via “audio computer assisted interviewing” (a self-interviewing tool), despite high levels of illiteracy. We randomize the order of Likert-scale answer options corresponding to different frequencies of intimate partner violence, and find that reporting does not depend on the ordering of the response options.

\- Answering sensitive questions privately before face-to-face interviews increases later disclosure of intimate partner violence. We randomized the order in which respondents answered two questions—either face-to-face with an enumerator first, or privately using audio computer-assisted self-interviewing first. Our findings show that answering privately first significantly increases later face-to-face disclosure of intimate partner violence by 41%-57%.

## References

Agüero, J. M. and Frisancho, V. (2022). Measuring violence against women with experimental methods. Economic Development and Cultural Change, 70 (4), 1565–1590.

Bulte, E. and Lensink, R. (2019). Women's empowerment and domestic abuse: Experimental evidence from Vietnam. European Economic Review, 115, 172–191.

Cullen, C. (2023). Method matters: The underreporting of intimate partner violence. The World Bank Economic Review, 37 (1), 49–73.

— and Mahmud, M. (2020). Surveying on sensitive topics: Using audio computer assisted self-interviewing. MBRG Methods Briefs.

Joseph, G., Javaid, S. U., Andres, L. A., Chellaraj, G., Solotaroff, J. and Rajan, S. I. (2017). Underreporting of gender-based violence in Kerala, India: An application of the list randomization method. World Bank Policy Research Working Paper, (8044).

Park, D. S., Aggarwal, S., Jeong, D., Kumar, N., Robinson, J. and Spearot, A. (2021). Private but misunderstood? Evidence on measuring intimate partner violence via self-interviewing in rural Liberia and Malawi. NBER Working Paper 29584.

Peterman, A., Dione, M., Le Port, A., Briaux, J., Lamesse, F. and Hidrobo, M. (2024). Disclosure of violence against women and girls in Senegal. World Bank Economic Review Forthcoming.
"""
