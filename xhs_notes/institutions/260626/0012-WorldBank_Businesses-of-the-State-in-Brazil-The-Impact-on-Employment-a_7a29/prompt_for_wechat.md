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
Policy Research Working Paper

11082

# Businesses of the State in Brazil The Impact on Employment and Business Dynamism

Sara Brolhato

Xavier Cirera

Antonio Martins-Neto

POLICY RESEARCH WORKING PAPER 11082

## Abstract

Businesses of the state (BOS) have regained the public debate in midst of the COVID-19 pandemic, especially as a source of resilience to shocks and a mechanism for technology development and diffusion. However, little is known about the impacts on the economy. This paper uses a novel dataset that allows exploring the importance of BOS in Brazil, including registered state-owned or mixed enterprises and with indirect state participation in competitive sectors. The paper looks at their impact through two connected perspectives: employment and business dynamism. First, the analysis tests whether BOS pay a wage premium to their employees. Then, it estimates the impacts of privatization on workers' outcomes and firms' total employment. The findings indicate that BOS firms pay a substantial wage premium in Brazil and that privatization events lead to a significant decline in workers' wages. Yet, the analysis does not find robust evidence that privatization results in a decline in total employment. The findings show that BOS tend to use more technical workers, a proxy for innovation, and are larger and grow faster in terms of employment than private companies. Finally, the paper analyzes what the presence of BOS means for the business dynamism of sectors. It finds that a higher presence of BOS in a given sector is negatively correlated with young firms' participation and exit rates, and job destruction rates. Meanwhile, BOS participation is positively correlated with market concentration, but also job creation rates. The results suggest that BOS have significant impacts on markets, and that assessment of the state's footprint needs to consider the effects of public investments in private companies, directly and indirectly.

# Businesses of the State in Brazil: The Impact on Employment and Business Dynamism

Sara Brolhato $^{1}$ , Xavier Cirera $^{*1}$ , and Antonio Martins-Neto $^{1}$

$^{1}$ The World Bank

## 1 Introduction

After decades of uneven privatization across countries, the recent Covid-19 pandemic has brought back discussions about the role of state-owned enterprises (SOEs) and firms with state participation in the economy. Increasing economies' resilience to shocks, using state participation as a mechanism for the diffusion of technologies for climate mitigation and adaptation, and ensuring the production of critical health products, technologies, and infrastructure in the midst of growing geopolitical tensions are being used to justify an increased presence of Businesses of the State (BOS) - defined as firms with direct or indirect state participation of at least 10% - in the economy.

In the case of Brazil, despite the large privatization program in the 1990s and the recent privatization processes carried out by the latest administrations, BOS are still important in some sectors - especially in infrastructure, extractive industries, and postal activities - and the state footprint has expanded to investments to private firms in competitive sectors. However, little is known about the impact of these BOS on markets and how effectively they play some of the roles they are supposed to play. This paper studies the effects of BOS in Brazil from different angles, particularly their effects on the labor market and business dynamism. The contribution of this paper is twofold. First, in addition to the traditional analysis of SOEs, the analysis uses a unique dataset that allows describing BOS in their different modalities, from fully public enterprises to private companies with minority state participation operating in competitive sectors. Second, in addition to measuring the effects of specific roles of the state footprint on the labor market, we also study the impact that BOS presence has on business dynamism.

Specifically, we first provide a descriptive analysis of BOS and find that, on average, BOS pay higher wages, are older, and are larger than their private peers. Next, we perform a series of estimates controlling for firms' characteristics to examine how BOS differ from private firms in terms of innovation, employment and employment growth. Using data from 2016 to 2020, we find that BOS are more innovative and larger than fully private companies, consistent with findings in China (Lo et al., 2022). In particular, participated companies - private companies with public investments - are more innovative and have higher employment relative to other types of BOS, thus suggesting the public sector invests essentially in some key sectors and innovative private companies. Furthermore, BOS grew more in terms of employment, although it is only statistically significant for participated firms.

Following this initial assessment, we explore the link between BOS and the labor market by testing for a wage premium associated with BOS. BOS, especially public enterprises, have different wage-setting mechanisms, commonly resulting in a wage premium, which, in turn, is usually linked to distortions in workers' employment choices and productivity losses (Cavalcanti and Santos, 2020). We estimate several firm-level and worker-level regressions and find a robust positive wage premium of $18.5\%$ ; yet, once we add workers' fixed effect to control for workers' sorting into BOS, the wage premium declines to $4.5\%$ in our preferred specification.

As an alternative to exploring the wage premium of SOEs, we also analyze the effects of privatizations on workers' wages and firms' total employment. Using an event-study methodology, our estimates indicate that privatizations negatively affect workers' wages. For instance, workers who are part of a privatization event see relative wages decline by about 10% in the first two years after the shock compared to the control group. Furthermore, in exploring the heterogeneities of our results, we observe that privatized firms tend to lay off more educated, older, and long-tenured individuals.

Our findings are consistent with the growing literature on the impacts of privatization. For instance, Olsson and Tåg (2021) evaluate the impact of privatizations in Sweden from 1997 to 2011 and find that wage declines of about 4% in the first two years and 9% during the third and fourth years $^{1}$ . In the case of Brazil, Arnold (2022) evaluates the impact of privatizations during the 1990s - the first wave of large privatization in the country. Focusing on the banking, telecommunications, and electricity sectors, the author observes a substantial wage premium for public firms and that privatizations negatively affect workers' wages.

Lastly, we study the relationship between BOS and business dynamism. In particular, we test whether a higher concentration of BOS is correlated to entry rate, exit rate, gross job creation, and other measures of business dynamism at the industry level. We find robust evidence that BOS' participation correlates with a smaller share of employment in young firms and higher market concentration. In competitive industries, we also find that a higher concentration of BOS is associated with lower firm exit rates. In terms of labor market dynamics, we find that BOS participation is associated with higher net employment change - resulting from simultaneously higher gross job creation and lower job destruction rates. Combined, our results suggest that the presence of BOS could potentially generate adverse impacts on the sectors in which they operate, reducing business dynamics through lower entrepreneurship, less intense selection, higher concentration and, consequently, limited competition.

The rest of the paper is structured as follows. Section 2 describes the datasets used in this study and our classification of BOS. Section 3 presents a description of the industries in which BOS operate and their performance, innovation, employment and employment growth relative to privately-owned firms. Section 4 estimates the wage premium associated with workers in BOS relative to the private sector using firm-level and worker-level data. Section 4.3 uses privatizations of public firms as a natural experiment for providing additional evidence on the BOS wage premium, and estimates the effects of these events on worker and firm-level outcomes. Section 5 presents empirical evidence on business dynamism in Brazil over the last decade, and estimates how the presence of BOS affects multiple measures of dynamism at the industry level. Section 6 concludes.

## 2 Data

Our main data source is the Relação Anual de Informações Sociais (RAIS), an annual census of active working contracts for all formal employees in Brazil. The dataset includes information on over 3 million establishments and 40 million workers annually. Each entry in the RAIS dataset is an employee-employer match, with both establishments and individuals having a unique identifier. Establishments' identifiers include 14-digits, with the first 8-digits representing the firm. Throughout our analysis, we will concentrate on firm-level data. The primary use of the RAIS is to compute federal wage supplements, social security benefits, and unemployment insurance. Data collection is mandatory, and given its importance, firms and workers provide high-quality information, especially on wages.

We use data from 2010 to 2020 and focus on the productive sector – we exclude workers in public administration, non-profit organizations, extraterritorial organizations, and specific categories for individual entities such as political candidates and individual rural producers. We use worker-level information including age, level of education, tenure, wage, gender, date of admission, and occupation (CBO classification codes). At the firm-level, we measure employment as the number of active workers on December 31st of each reference year, and we include only establishments with positive employment in the sample. We also use the information on the 4-digit CNAE sector classification codes $^{2}$ and the legal nature of firms, which is a key variable in this study used to identify state-owned firms.

We also compute firm characteristics from worker-level information, for instance, we measure average firm wage, the share of college-educated workers, and firm-level innovation intensity, which is measured as the share of employment in technical and scientific occupations (PoTec), a proxy for R&D expenditure proposed by Araújo et al. (2009). We take advantage of the database panel structure to infer firm entry and exit based on the first and last years a firm is observed in the data. Since RAIS does not directly contain the entry year for each firm, we compute age considering that a firm's entry year is the earliest observed admission year reported for workers in that firm. $^{3}$ We correct these age measures whenever they are inconsistent with the entry observed in our sampled period.

To define state-owned firms, we primarily use firms' legal nature information available in RAIS. The problem of using only legal nature is that it omits a large footprint of the state via investing in private firms. Therefore, we complement our analysis by identifying private firms with government participation using ownership information from the Orbis database available for 2019. Specifically, we define three types of BOS based on the magnitude of state participation within a firm: public, mixed, and participated firms. Using the information on the legal nature of firms provided in RAIS, we identify fully public and mixed-capital firms (those where the government owns the majority of voting shares). Participated firms are defined as private firms with minority state participation. $^{4}$ These are firms for which state ownership is identified through the Orbis database but that are classified as fully private in RAIS. $^{5}$ Whenever we generally speak of BOS, we are referring to the definition that encompasses all these three groups of firms, unless stated otherwise.

Table 1 details the merge of firms with state participation in Orbis with the RAIS dataset. Of 1,302 firms with state ownership containing a valid Brazilian tax identifier in 2019, we can find 1,067 of these firms in RAIS within the same year (82%). Even though RAIS is supposed to be a census of all Brazilian firms in the formal sector, we cannot match 235 firms. Additionally, 323 of the matched firms did not report worker-level information in 2019, either because they had no active working contracts or halted operations during the reference year. Of the 1,067 matched companies, 129 are registered as fully public firms, and 238 are registered as mixed capital firms. We define as participated the 377 firms that are registered in RAIS as fully private firms but contain minority state participation as identified in Orbis. Table 2 presents the resulting number of firms by year in the sample, along with a decomposition between the number of privately-owned firms (POEs) and BOS, and their classification into each of the three BOS types after combining data from Orbis and legal nature information in RAIS.

Additionally, we use Orbis data combined with firm ownership structure information to obtain estimates for the share of government ownership in each BOS. Whenever firms are directly owned by the state, with only one public entity as the shareholder, we consider the percentage of government ownership provided by Orbis or by other sources used to validate the data, such as the Overview of State-Owned Companies made available by the Secretariat for Coordination and Governance of State-owned Companies (SEST). $^{6}$ In the case of indirect ownership by the government, through multiple entities or other state-owned firms, it is less straightforward to obtain a reliable measure of the ownership fraction. In those cases, we provide a conservative estimate of the government ownership share by considering the minimum share observed in the multiple layers of ownership.

We test the reliability of the ownership share estimates by plotting a distribution of the firms' government shares in Orbis for each BOS type according to the classification in RAIS. Figure 1 illustrates that the government ownership shares are mostly consistent with the information on ownership type in RAIS, concentrated in $100\%$ for fully public firms, with values ranging from $50\%$ and $99\%$ for mixed firms, and with a more scattered distribution in values lower than $50\%$ for participated firms. We use available ownership information in RAIS to correct the shares of government ownership shares when possible: we input ownership of $100\%$ for all public firms, and we input ownership of $51\%$ for mixed-capital firms whenever the estimated share is below that level or when an estimate for that firm is not available.

Lastly, we use the sector taxonomy industry classification proposed by Dall'Olio et al. (2022), which defines three groups based on the rationale for industry state participation. According to this classification, competitive industries are those with no issues of economic efficiency or market failures that would justify the presence of state-owned enterprises. By contrast, industries described as natural monopolies or partially contestable would have some grounds for justifying the presence of state-owned firms. While in natural monopolies this justification is based on a market structure characterized by economies of scale and subadditivity costs, partially contestable industries are defined by the presence of market failures that could be addressed with direct state participation, such as market power or externalities (Dall'Olio et al., 2022). Table 3 shows the total number of firms within our sample within each taxonomy group in 2020, along with the corresponding percentage relative to the total number of firms and the number of BOS within those groups.

Table 1: Summary of RAIS matching (2019).

<table><tr><td colspan="3">Matched firms</td></tr><tr><td>Firms with a valid tax id</td><td>1,302</td><td>100%</td></tr><tr><td>Matched</td><td>1,067</td><td>82%</td></tr><tr><td>Not matched</td><td>235</td><td>18%</td></tr><tr><td colspan="3">Matched firms by establishment type</td></tr><tr><td>Public</td><td>129</td><td>12%</td></tr><tr><td>Mixed</td><td>238</td><td>22%</td></tr><tr><td>Participated</td><td>377</td><td>35%</td></tr><tr><td>Zero employment</td><td>323</td><td>30%</td></tr><tr><td>Total matched</td><td>1,067</td><td>100%</td></tr></table>

Note: This table summarizes the number of BOS identified through Orbis that we were able to locate in RAIS, using firm identifiers. In the lower panel, the table illustrates the legal nature information in RAIS of firms successfully located in RAIS, as well as the number of firms which are registered as having zero employment during the whole year of 2019. Data from RAIS and Orbis, 2019.

Table 2: Number of firms by year.

<table><tr><td>Year</td><td>Firms</td><td>POEs</td><td>BOS</td><td>Public</td><td>Mixed</td><td>Participated</td></tr><tr><td>2016</td><td>2,531,848</td><td>2,529,989</td><td>1,859</td><td>910</td><td>583</td><td>366</td></tr><tr><td>2017</td><td>2,518,208</td><td>2,516,404</td><td>1,804</td><td>877</td><td>559</td><td>368</td></tr><tr><td>2018</td><td>2,501,936</td><td>2,500,773</td><td>1,163</td><td>389</td><td>408</td><td>366</td></tr><tr><td>2019</td><td>2,494,135</td><td>2,493,215</td><td>920</td><td>243</td><td>291</td><td>386</td></tr><tr><td>2020</td><td>2,464,407</td><td>2,463,514</td><td>893</td><td>233</td><td>290</td><td>370</td></tr></table>

Note: This table illustrates the total number of firms, including the distinction between private firms and BOS, in the sample. Data from RAIS, from 2016 to 2020.

Table 3: Sector taxonomy, 2020.

<table><tr><td></td><td>Number of firms</td><td>(%)</td><td>Number of BOS</td></tr><tr><td>Competitive</td><td>2,234,377</td><td>90.67</td><td>521</td></tr><tr><td>Partially contestable</td><td>34,228</td><td>1.39</td><td>163</td></tr><tr><td>Natural monopoly</td><td>13,310</td><td>0.54</td><td>190</td></tr><tr><td>Excluded</td><td>182,492</td><td>7.41</td><td>19</td></tr></table>

Note: Data from RAIS, 2020.

Figure 1: Distribution of ownership shares by BOS type  
![](images/f6a660fd44a12a736a559038350d2f67481c9e171cf715559697ab8444efb981.jpg)  
(a) Public

![](images/87038b734c6e1375c283d779e8803e0dca9a076fa352d1bab63f86405b8c04e2.jpg)  
(b) Mixed

![](images/3047093f1cad21794cd777364741b8f0135550b9543adb46fb09b2dff7b3fefb.jpg)  
(c) Participated  
No

[中间内容因长度限制已省略]

792389302a1903.jpg)  
Note: Fraction of employment of firms with up to 5 years of age relative to aggregate employment. Data includes productive sectors from RAIS, 2010-2020.

Figure A4: Job creation and destruction by sector.  
![](images/9001096d130f02538ef72348175abce5dea641ddf2264735348b24889dc58f4b.jpg)  
Note: Gross job creation is the sum of employment gains across all firms that expand or entry the market. Gross job destruction is the sum of employment losses across all firms that contract or shut down. Data includes productive sectors from RAIS, 2010-2020.

Figure A5: Job reallocation by sector.  
![](images/26fc008dcd84d721cc78b489bd8116e82b938899f0f761a8df4c1833d40ce650.jpg)

Note: Gross job creation is the sum of employment gains across all firms that expand or entry the market. Gross job destruction is the sum of employment losses across all firms that contract or shut down. Net employment change is the difference between gross job creation and destruction. Gross job reallocation is the sum of all firm-level employment gains and losses. Data includes productive sectors from RAIS, 2010-2020.

Figure A6: Standard deviation of firm employment growth by sector - BOS.  
![](images/9e7a97e8c2c471d010e32d56e7c13ff4d7853dbe8eb88f084a8d4ee378019ca2.jpg)  
Note: Standard deviation of firm-level employment growth rates for private firms and BOS. Data includes productive sectors from RAIS, 2010-2020.

# B Appendix B - Results with less restrictive matching

Figure B1: Effect of privatization on workers' wages

![](images/0f5f2a22c42bddd066b62d6a718831297b264ea700a754142192d2548787412e.jpg)  
(a) All workers

![](images/bfa8dd98a7e03ad35f20beff1b59443053ec0f2b8f98ac14eaade5725f550130.jpg)  
(b) Incumbents  
Note: The figures show the estimates of time-to-event dummies interacted with a privatization indicator from regressions including individual, region, sector, time-to-event dummies, and year fixed effects. Panel (a) includes all workers employed in BOS at the time of treatment, while panel (b) only includes workers that stayed in the same company until $t + 3$ . The dependent variable is relative wages. Relative wages are measured by dividing the worker's monthly wage by the worker's average wage in year t - 1. Year t - 1 is the base year. Vertical bars show estimated 95% confidence interval based on standard errors clustered at individual level.

Figure B2: Effect of privatization on workers' wages for different groups  
![](images/8815eed820969aed006951646f28a557b2004aec54e2ef72e3020613ba0fac15.jpg)  
(a) Education

![](images/84a24cf211077e7cb1eca156982916f4ed07e9b81a3d46ea7920f921656c6fec.jpg)  
(b) Age

![](images/8e1ab57b0df38222cf6f4b0cb4eb1f1206d197ef5d4ccafdcca82bb24083907c.jpg)  
(c) Tenure

![](images/3e2ee04cfbce7c29bd8abbbe78912a17a9bceebebdeb7f645d1169a2a133856a.jpg)  
(d) Occupation  
Note: The figures show the estimates of time-to-event dummies interacted with a privatization indicator from regressions including individual, region, sector, time-to-event dummies, and year fixed effects. All panels only include workers that stayed in the same company until $t + 3$ . The dependent variable is relative wages. Relative wages are measured by dividing the worker's monthly average wage by the worker's wage in year t - 1. Year t - 1 is the base year. Vertical bars show estimated 95% confidence interval based on standard errors clustered at individual level.

# C Appendix C - Results using broader matching and alternative Difference-in-Differences (DiD) method

Figure C1: Effect of privatization on workers' wages

![](images/09c3f721fd1a934a060332478eb18a9f3206bb180ef461248c74e25a0866d685.jpg)  
(a) All workers

![](images/0974a245553119bbdc5fc2b09ab61aa57732ea62acf2cbcc3e52a81110d29f1e.jpg)  
(b) Incumbents  
Note: The figures show the estimates of time-to-event dummies interacted with a privatization indicator from regressions including individual, region, sector, time-to-event dummies, and year fixed effects. Panel (a) includes all workers employed in BOS at the time of treatment, while panel (b) only includes workers that stayed in the same company until $t + 3$ . The dependent variable is relative wages. Relative wages are measured by dividing the worker's monthly average wage by the worker's wage in year t - 1. Year t - 1 is the base year. Vertical bars show estimated 95% confidence interval based on standard errors clustered at individual levels.

## D Appendix D - Fixed effects

This section examines whether privatized BOS pay a larger wage premium than other BOS. To this end, we estimate an AKM model for the largest connected set in the period 2010 and 2014 and compare firms' fixed effects between non-privatized BOS and those that privatized from 2015 to 2020 $^{17}$ . In particular, we estimate the following wage model:

$$
l n (w _ {i t}) = \alpha_ {0} + \beta_ {i} \theta_ {f} + \sigma_ {t} + X _ {i t} ^ {\prime} \delta + \epsilon_ {i t}\tag{6}
$$

where $w_{it}$ is the log hourly wage. $\theta_{f}$ is a firm-specific intercept, $\beta_{i}$ is an individual-level intercept, $\sigma_{t}$ are yearly dummies, and $\epsilon_{it}$ is an idiosyncratic error term. Moreover, $X_{it}^{\prime}$ is a vector of education, quadratic, and cubic age interacted with year indicators. We follow Card et al. (2018) and normalized workers' age to 40 years old for males and 35 for females. We then estimate a simple linear model controlling for sectors (2-digits CNAE) and weighting by firms' number of employees. The results indicate that privatized BOS have a wage premium of 0.04 log points larger than their non-privatized peers, the difference between the two groups is not statistically different from zero. $^{18}$
"""
