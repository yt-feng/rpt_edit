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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份世界银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Technology and Corporate Ethical Standards

Marika Carboni

Marta Degl'Innocenti

Franco Fiordelisi

Davide Salvatore Mare

POLICY RESEARCH WORKING PAPER 11068

## Abstract

Using data from the World Bank Enterprise Surveys from 2006 to 2023, this paper studies the corporate ethical standards of technological digital oriented firms. The findings indicate that technology and digitalization positively impact the adoption of environmental and social standards. However, digital oriented technological firms show lower governance standards. These results are influenced by country culture, the burden of business regulation, and the perception of the courts as an obstacle to business activity. This underscores the importance of the broader society and the quality of the business environment in shaping how digital oriented technological firms adopt ethical standards.

# Technology and Corporate Ethical Standards

Marika Carboni
Roma Tre University, Italy

Marta Degl'Innocenti
Università degli Studi di Milano, Italy

Franco Fiordelisi
University of Essex, United Kingdom

Davide Salvatore Mare\*
World Bank, United States; University of Edinburgh, United Kingdom

JEL Classification: Q56, G30, O14

Keywords: Technology, Ethics, ESG, Sustainability, Culture, Corporate Governance

## 1 Introduction

Interest in ethics and sustainability in firm management has grown globally in recent decades, with the concepts of ethics and sustainability being intrinsically linked (Crane et al., 2019; Torelli, 2021). A prime example is the United Nations' 17 Sustainable Development Goals (SDGs), which underscore the importance of addressing a broad set of issues such as environmental, social, and governance concerns to eradicate poverty and preserve the environment. These goals have become central to political agendas worldwide.

The relationship between technology and sustainability has been increasingly examined in recent years, with technological progress playing a key role in sustainable development (United Nations, 2019). Technological change can accelerate achievement of the SDGs by replacing environmentally damaging modes of production with more sustainable ones, improving incomes through higher productivity and lower costs of goods and services, and supporting more inclusive forms of participation in social and economic life. However, while technology can create opportunities that enable innovative solutions, it also poses health and environmental risks, such as pollution from electronic waste containing non-biodegradable materials and toxic substances. Technology may also have negative social impacts by increasing unemployment and exacerbating economic inequality. Therefore, the relationship between technology and ethical practices is complex, as technological development accelerates sustainable development but can also create environmental and social problems.

In this paper, we study the propensity of digital-oriented technological firms to adopt ethical practices. Our analysis is particularly relevant in today's digital age, where having an online presence is crucial for firms to increase their competitive advantage. For example, a website enhances a company's reputation by effectively sharing and communicating its mission and values to the public. Websites also significantly increase sales opportunities by reaching a broader audience and improving customer engagement and experience (Dolan et al., 2015; Chaffey, 2015). Similarly, the use of social media, a digital technology that enables the sharing of ideas and information, allows companies to communicate their Corporate Social Responsibility (CSR) to the public without having to go through the gatekeeping function of the news media (Vogler et al., 2021). We combine the concepts of technology and online presence to define these firms as digital-tech-oriented firms. We then assess the ethical behavior of such firms by examining their monitoring of $\mathrm{CO}_{2}$ emissions, provision of employee training, and employment of female top managers. Our research focuses on the adoption of ethical practices as it signals that companies are concerned about the environment and the social consequences of their activities.

For our analyses, we gather firm-level data from the World Bank Enterprise Surveys (ES). Our sample encompasses up to 192,132 observations across 158 countries from 2006 to 2023. We consider three main dimensions of firms' ethical behavior capturing environmental, social, and governance (ESG) standards: monitoring of $\mathrm{CO}_{2}$ emissions (environmental dimension, or E), formal training programs for employees (social dimension, or S), and the presence of female top managers (governance dimension, or G). The selection of these ESG dimensions is motivated by past papers that emphasize the importance of technology in reducing $CO_{2}$ emissions (Jaffe, Newell, and Stavins, 2003) and highlight how technological advancements enhance the effectiveness of training programs and employee performance (Bhattacherjee and Premkumar, 2004). Moreover, the appointment of women directors to corporate boards has been a longstanding and widely debated topic in corporate governance research. The extant literature provides evidence of a potential association between diverse boards and innovation (see, for example, the literature review in Kirsch, 2018). We extend this literature by investigating whether digital-tech-oriented firms hire women in managerial roles.

Our findings show that digital-tech-oriented firms are more likely to engage in monitoring $CO_{2}$ emissions and providing formal training programs for employees. This suggests that technology can help to achieve sustainability goals. However, we find that these firms are less likely to employ female top managers. Women are underrepresented in managerial roles, as is the case in many other sectors, potentially due to stereotypes against women or other barriers to entering the labor market. This may be more pronounced in technological firms due to the historical gender gap in STEM (Science, Technology, Engineering, and Mathematics) education and career paths that have restricted the number of qualified female candidates for managerial positions within digital-tech-oriented firms.

Country-specific traits can significantly influence corporate practices, including ethical practices (Kostova and Roth, 2002). To account for this heterogeneity, we consider both cultural factors and the quality of the business environment. We capture cultural influences using five dimensions of national culture, proposed by Hofstede et al. (2010). Our findings highlight that national culture may be a critical factor, particularly in the context of hiring female top managers. Specifically, we observe that digital-tech-oriented firms exhibit a stronger negative relationship with employing female top managers in countries characterized by strong masculine preferences and short-term orientation.

To investigate the role of the quality of critical public services, we introduce regulatory burden and businesses' perception of the courts. Both factors can be seen as related to the literature that focuses on the need for and impact of regulation on sustainability (Behera and Sethi, 2022; Li et al., 2021). It may be that regulatory and bureaucratic burdens challenge the flexibility and adaptability needed for proactive ethical strategies. In support of this view, we find that digital-tech-oriented firms are positively associated with monitoring $\mathrm{CO}_{2}$ emissions and with offering training programs when the regulatory burden is low. However, we also observe that reducing the regulatory burden widens the gender gap. This phenomenon may be due to the fact that women tend to spend more time navigating regulatory requirements. Hence, a reduction in regulatory burden has a negative impact on the presence of female top managers. The gender gap instead narrows as bureaucracy intensifies (Baron et al., 2007).

Finally, we consider how the justice courts are perceived as a relevant obstacle to business activity. In this regard, we find that digital-tech-oriented firms hire fewer female top managers when courts are not perceived as a significant obstacle to doing business. This finding calls for a deeper scrutiny of the mechanisms through which the quality of the business environment influences the gender gap in digital-tech-oriented firms.

Our paper relates to various literature strands. First, it contributes to the extant knowledge of the relationship between technology and sustainability (e.g., Bekhet and Latif, 2018; Omri, 2020; Sharif et al., 2022; Zhang et al., 2022; Higón et al., 2017; Zakari et al., 2022; Sun et al., 2019; de Vries et al., 2020; Tyrowicz et al., 2020; Yang et al., 2022), confirming that such a relationship is ambiguous. On the one hand, we show a positive relationship between digital-tech-oriented firms and the monitoring of CO₂ emissions, as well as the provision of employee training programs, suggesting virtuous behavior by digital-tech-oriented firms. On the other hand, we find a negative relationship between digital-tech-oriented firms and the employment of female top managers, suggesting that technology may promote the widening of the gender gap in top management positions.

Our study provides nuanced evidence to papers examining the impact of technology firms' ethical behavior (Okafor et al., 2021; Boulouta and Pitelis, 2014; Bernal-Conesa et al., 2017; Lin et al., 2020). Unlike these papers, we focus on the impact of technology on firms' ESG practices while accounting for country and heterogeneity in the business environment. As such, our findings may have important implications for policies aiming at simultaneously advancing technological progress and sustainability goals.

In addition, we contribute to the corporate social responsibility (CSR) literature (e.g., Angelidis and Ibrahim, 2004; Arnold and Valentin, 2013; Mahoney et al., 2013; Ferrell et al., 2019; Chantziaras et al., 2020), by differentiating the findings on the relationship between digital-tech-oriented firms and ethical practices across cultural dimensions. Therefore, we also add to the strand of literature examining the link between cultural dimensions and sustainability (Sedita et al., 2022; Kucharska and Kowalczyk, 2019; Lahuerta-Otero and González-Bravo, 2018; Parboteeah et al., 2012; Onel and Mukherjee, 2014; Husted, 2005; Vachon, 2010; Gallego-Álvarez and Ortas, 2017), as well as to studies focusing on the issue of regulation in sustainability (Behera and Sethi, 2022; Li et al., 2021), since we examine how regulatory burdens and perceptions of courts as an obstacle to business activity are related to firms' ethical behavior.

The remainder of the paper is organized as follows. In section 2, we describe the data and variables; in section 3 we present our empirical approach; in section 4 we discuss our results. Finally, section 5 concludes the paper.

## 2 Data and Variables

We collected data from various sources to analyze the correlation between firms' technology and ethical practices. First, we gathered firm-level data from the World Bank Enterprise Surveys (ES), covering 158 countries from 2006 to 2023, for a total of 192,132 observations. $^{1}$ We consider firms in the manufacturing and non-manufacturing industries as per the ISIC Code Revision 4 classification. $^{2}$ In addition, we obtained GDP per capita from the World Bank's World Development Indicators, $^{3}$ and cultural dimensions data from Geert Hofstede's website. $^{4}$

We capture the environmental, social, and governance dimensions that represent ethical practices by constructing three binary variables from the ES. Specifically, the environmental dimension is captured by a binary variable that takes the value of one if the firm has monitored its $CO_{2}$ emissions over the past three years (“mon\_emi”), and zero otherwise. $^{5}$ The social dimension is captured by a binary variable that takes the value of one if the firm offered formal training programs for permanent, full-time employees (“training”) in the last fiscal year, and zero otherwise. The governance dimension, related to the employment of female top managers (a gender issue) is captured by a binary variable that takes the value of one if a company employs female top managers (“top\_man\_fem”), and zero otherwise.

To identify digital-tech-oriented firms, we build two binary variables. First, we exploit the R&D intensity classification at the two-digit level by Galindo-Rueda and Verger (2016). We construct a first binary variable that takes the value of one for firms in sectors with at least medium technology orientation as implied by their R&D intensity classification, and zero otherwise (“tech orientation”). $^{6}$ Second, we compute a binary variable that takes the value of one if the establishment has its own website or a social media page, and zero otherwise (“digital orientation”). The product of tech orientation and digital orientation defines digital-tech companies (“digital-tech orientation”).

We also consider various factors that could impact the relationship between the adoption of ethical practices and digital-tech-oriented firms, such as the firm size (“large”), the presence of a line of credit or loan from a financial institution (“fin\_ins”), the real annual sales growth in percent (“sal\_gro”), the logarithm of GDP per capita (“log (GDPpercapita)”) $^{7}$ and the “age” of the firm, given by the difference between the year of the survey and the year in which a firm began operations (“age”).

We obtained data for cultural dimensions from Geert Hofstede's website, which includes six dimensions: long-term orientation, individualism, power distance, uncertainty avoidance, masculinity, and indulgence. We focus on five dimensions to explore their influence on the relationship between technology and ethical practices. Specifically, we examine whether: (i) long-term orientation and individualism affect the relationship between digital-tech-oriented firms and emissions monitoring; (ii) power distance and uncertainty avoidance modify the relationship between digital-tech-oriented firms and training; and (iii) masculinity and long-term orientation influence the relationship between digital-tech-oriented firms and the presence of female top managers.

While indulgence may be related to environmental issues (Gallego-Álvarez and Ortas, 2017), we believe that long-term orientation (“ltowvs”) and individualism (“idv”) are more appropriate to influence the relationship between digitally oriented firms and emissions monitoring. According to Geert Hofstede's website, long-term orientation ("ltowvs"), expressed on a scale from 0 (least long-term oriented) to 100 (most long-term oriented), pertains to change. In a long-term oriented culture, there is a fundamental belief that the world is changing, necessitating preparation for the future. Conversely, in a short-term oriented culture, the world is perceived as static, with the past providing a moral compass that should be followed.

The second dimension we consider is individualism (“idv”), where 100 represents the most individualistic country and 0 the least. Individualism measures the degree to which people feel independent, as opposed to interdependent as members of a larger whole.

For the social dimension, we use power distance (“pdi”), which ranges from 0 (lowest) to 100 (highest). Power distance measures the degree to which the less powerful members of organizations and institutions accept and expect power to be distributed unequally. Additionally, we use uncertainty avoidance (“uai”), which addresses a society’s tolerance for uncertainty and ambiguity, also ranging from 0 (lowest) to 100 (highest).

For the governance dimension, we use long-term orientation (“ltowvs”) and masculinity (“mas”). Masculinity measures the extent to which the use of force is socially endorsed, with higher scores (closer to 100) indicating more masculine societies.

Table 1 shows the list of countries in our sample, covering different world regions: Africa (AFR), East Asia and Pacific (EAP), Europe and Central Asia (ECA), Latin America and the Caribbean (LAC), Middle East and North Africa (MNA) and

South Asia (SAR). Table 2 shows the summary statistics, reporting the number of observations, the mean, the standard deviation, minimum and maximum for the variables we used.

[Insert Tables 1-2 about here]

The mean value of “top\_man\_fem” is low (0.1548), indicating a low number of female top managers for the firms in the sample. Also the mean of the variable “tim\_spe” is relatively low (0.0640), indicating that the time spent by senior management in dealing with regulations is generally less than 50%.

Table 3 shows the correlation matrix. Pairwise correlation coefficients are relatively low, reducing concerns about multicollinearity in the estimates.

[Insert Table 3 about here]

## 3 Empirical Approach

For our analysis, we employ a conditional model in which a variable capturing firms' digital orientation interacts with a variable measuring firms' technological orientation. This approach allows us to investigate the combined effect of these two dimensions, providing a more nuanced understanding of their influence on the outcomes of interest. Our model takes the following form:

$$
\begin{array}{r l} \text {ethical\_orientation} _ {\mathrm{ict}} & = \beta_ {0} + \beta_ {1} \text {digital orientation} _ {\mathrm{ict}} + \beta_ {2} \text {tech orientation} _ {\mathrm{ict}} \\ & + \beta_ {3} \text {digital orientation} _ {\mathrm{ict}} * \text {tech orientation} _ {\mathrm{ict}} + \beta_ {4} X _ {\mathrm{ict}} \\ & + \alpha_ {\mathrm{c}} + \alpha_ {\mathrm{t}} + \varepsilon_ {\mathrm{ict}} \end{array}\tag{1}
$$

The dependent variable (ethical\_orientation) is a binary variable that we define in different ways to capture each ESG ethical dimension (mon\_emi, training, and top\_man\_fem, respectively). Specifically, we capture the environmental dimension with a binary variable that takes the value of one if the firm has monitored its CO₂ emissions over the past three years (“mon\_emi”), and zero otherwise.⁸ The social dimension is captured by a binary variable that takes the value of one if the firm offered formal training programs for permanent, full-time employees (“training”) in the last fiscal year, and zero otherwise. The governance dimension is captured by a binary variable that takes the value of one if the firm has female top managers (“top\_man\_fem”), and zero otherwise. The main variable of interest is the interaction between digita

[中间内容因长度限制已省略]

3">Dependent variables</td></tr><tr><td>Monitoring CO2 emissions over the past three years</td><td>mon_emi</td><td>A binary variable that takes the value of one if the establishment has monitored its CO2 emissions over the past three years, and zero otherwise</td></tr><tr><td>Availability of formal training programs in the last fiscal year</td><td>training</td><td>A binary variable that takes the value of one if there was a formal training programs for permanent, full-time employees in the last fiscal year, and zero otherwise</td></tr><tr><td>Female top manager</td><td>top_man_fem</td><td>A binary variable that takes the value of one if the top manager is female, and zero otherwise</td></tr><tr><td colspan="3">Main independent variables</td></tr><tr><td>R&amp;D intensity classification at a two-digit level</td><td>tech orientation</td><td>A binary variable that takes the value of 1 if the firm is classified as having high, medium-high or medium R&amp;D intensity at the 2-digit level of ISIC Rev 4, and 0 if the firm is classified as having medium-low or low R&amp;D intensity 10</td></tr><tr><td>Website or social media page availability</td><td>digital orientation</td><td>A binary variable that takes the value of one if the establishment has its own website or social media page, and zero otherwise</td></tr><tr><td>High, medium-high or medium R&amp;D intensity firms at the 2-digit level of ISIC Rev 4 with their own website or a social media page</td><td>digital-tech orientation</td><td>A binary variable that takes the value of 1 if the firm is classified as having high, medium-high or medium R&amp;D intensity at the 2-digit level of ISIC Rev 4 and has its own website or social media page, and zero otherwise</td></tr><tr><td colspan="3">Firm-level variables</td></tr><tr><td>Firm size</td><td>large</td><td>A binary variable that takes the value of one if a firm has 100 and more employees (classified as “large”), and zero if a firm is classified as medium (20-99 employees) or small (&lt;20 employees)</td></tr><tr><td>Availability of a credit line or loan from a financial institution</td><td>fin_ins</td><td>A binary variable that takes the value of one if the establishment has a line of credit or loan from a financial institution, and zero otherwise</td></tr><tr><td>Real annual sales growth</td><td>sal_gro</td><td>A variable indicating the real annual sales growth at the firm level (%)</td></tr><tr><td>Age</td><td>age</td><td>A variable that is given by the difference between the year of the survey and the year in which a firm began operations</td></tr><tr><td colspan="3">Country-level variables</td></tr><tr><td>GDP per capita (constant international $)</td><td>log (GDPpercapita)</td><td>GDP per capita based on purchasing power parity (PPP). PPP GDP is gross domestic product converted to international dollars using purchasing power parity rates. An international dollar has the same purchasing power over GDP as the U.S. dollar has in the United States. GDP at purchaser's prices is the sum of gross value added by all resident producers in the country plus any product taxes and minus any subsidies not included in the value of the products. It is calculated without making deductions for depreciation of fabricated assets or for depletion and degradation of natural resources. Data are in constant 2021 international dollars 11</td></tr><tr><td>Long-term orientation</td><td>ltowvs</td><td>Long-term orientation deals with change. As with the other dimensions of culture, it is expressed on a scale from 0 (the most short-term oriented country) to 100 (the most long-term oriented country) 12</td></tr><tr><td>Individualism</td><td>idv</td><td>Individualism is the degree to which people feel independent as opposed to interdependent as members of a larger whole. As with the other dimensions of culture, it is expressed on a scale of 0 (the least individualistic country) to 100 (the most individualistic country)</td></tr><tr><td>Power distance</td><td>pdi</td><td>Power distance is the degree to which the less powerful members of organizations and institutions accept and expect power to be distributed unequally. As with the other dimensions of culture, it is expressed on a scale from 0 (lowest power distance) to 100 (highest power distance)</td></tr><tr><td>Uncertainty avoidance</td><td>uai</td><td>Uncertainty avoidance deals with a society's tolerance for uncertainty and ambiguity. As with the other dimensions of culture, it is expressed on a scale from 0 (the most uncertainty-tolerant country) to 100 (the most uncertainty-averse country).</td></tr><tr><td>Masculinity</td><td>mas</td><td>Masculinity is the degree to which the use of force is socially endorsed. As with the other dimensions of culture, it is expressed on a scale from 0 (the least masculine country) to 100 (the most masculine country)</td></tr><tr><td colspan="3">Obstacles</td></tr><tr><td>Senior management's time spent on dealing with regulations</td><td>tim_spe</td><td>A binary variable that takes the value of one if the percentage of time spent by all senior managers (managers, directors, and officers above the level of direct supervisor of production or sales workers) in a typical week during the past year dealing with requirements imposed by government regulations is greater than or equal to 50%, and zero otherwise</td></tr><tr><td>Courts perceived as a major or very severe obstacle</td><td>courts</td><td>A binary variable that takes the value of one if the courts are perceived as a major/very severe obstacle to the current operations of the firm, and zero if the courts are perceived as either a minor/moderate obstacle or not perceived as an obstacle</td></tr></table>
"""
