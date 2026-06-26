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
Gen-AI: Artificial Intelligence and the Future of Work

Prepared by Mauro Cazzaniga, Florence Jaumotte, Longji Li, Giovanni Melina, Augustus J. Panton, Carlo Pizzinelli, Emma Rockall, and Marina M. Tavares

SDN/2024/001

IMF Staff Discussion Notes (SDNs) showcase policy-related analysis and research being developed by IMF staff members and are published to elicit comments and to encourage debate. The views expressed in Staff Discussion Notes are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

2024
JAN

![](images/20f4040081ed7c176f41c3318410bd55d676a25e302efc5663ba34409ac5e66f.jpg)

# IMF Staff Discussion Notes Research Department

# Gen-AI: Artificial Intelligence and the Future of Work

Prepared by Mauro Cazzaniga, Florence Jaumotte, Longji Li, Giovanni Melina, Augustus J. Panton, Carlo Pizzinelli, Emma Rockall, and Marina M. Tavares\*

Authorized for distribution by Pierre-Olivier Gourinchas
January 2024

IMF Staff Discussion Notes (SDNs) showcase policy-related analysis and research being developed by IMF staff members and are published to elicit comments and to encourage debate. The views expressed in Staff Discussion Notes are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

ABSTRACT: Artificial intelligence (AI) has the potential to reshape the global economy, especially in the realm of labor markets. Advanced economies will experience the benefits and pitfalls of AI sooner than emerging market and developing economies, largely because their employment structure is focused on cognitive-intensive roles. There are some consistent patterns concerning AI exposure: women and college-educated individuals are more exposed but also better poised to reap AI benefits, and older workers are potentially less able to adapt to the new technology. Labor income inequality may increase if the complementarity between AI and high-income workers is strong, and capital returns will increase wealth inequality. However, if productivity gains are sufficiently large, income levels could surge for most workers. In this evolving landscape, advanced economies and more developed emerging market economies need to focus on upgrading regulatory frameworks and supporting labor reallocation while safeguarding those adversely affected. Emerging market and developing economies should prioritize the development of digital infrastructure and digital skills.

RECOMMENDED CITATION: Cazzaniga and others. 2024. “Gen-AI: Artificial Intelligence and the Future of Work.” IMF Staff Discussion Note SDN2024/001, International Monetary Fund, Washington, DC.

<table><tr><td>ISBN:</td><td>979-8-40026-254-8</td></tr><tr><td>JEL Classification Numbers:</td><td>E24, J24, J31, O33, O38</td></tr><tr><td>Keywords:</td><td>Artificial Intelligence, Labor Market, Job Displacement, Income Inequality, Advanced Economies, Emerging Market Economies, Low-Income Developing Countries</td></tr><tr><td>Author&#x27;s E-Mail Address:</td><td>mauro98cazzaniga@gmail.com, FJaumotte@imf.org, LLi4@imf.org, GMelina@imf.org, APanton@imf.org, CPizzinelli@imf.org, ERockall@stanford.edu, MMendestavares@imf.org</td></tr></table>

## Contents

Executive Summary 2

I. Introduction 3

II. AI Exposure and Complementarity 5

III. Worker Reallocation in the AI-Induced Transformation 11

IV. AI, Productivity, and Inequality 15

V. AI Preparedness 19

VI. Conclusions and Policy Considerations 22

Annex I. Data 26

Annex 2. Additional Information on AI Occupational Exposure and Potential Complementarity \_\_\_\_ 28

Annex 3. Methodology for the Worker Transition Analysis \_\_\_\_ 29

Annex 4. Model Details 32

Annex 5. AI Preparedness Index 34

References 36

## Boxes

1. AI Occupational Exposure and Potential Complementarity1 \_\_\_\_ 24

2. Artificial-Intelligence-led Innovation and the Potential for Greater Inclusion1 25

## Figures

1. Employment Shares by AI Exposure and Complementarity: Country Groups and Select \_\_\_\_ 8

2. Employment Share by Exposure and Complementarity (Selected Countries) 9

3. Share of Employment in High-Exposure Occupations by Demographic Groups 10

4. Share of Employment in High-Exposure Occupations by Income Deciles 11

5. Occupational Transitions for College-Educated High-Exposure Workers for BRA and GBR \_\_\_\_ 12

6. Life Cycle Profiles of Employment Shares by Education Level for Brazil and the United 13

7. 1-Year Re-Employment Probability of Separated Workers \_\_\_\_ 14

8. Estimated Wage Premia from Occupation Changes 15

9. Exposure to AI and to Automation and Income in the UK 17

10. Change in Total Income by Income Percentile 18

11. Impact on Aggregates (Percentage 18

12. AI Preparedness Index and \_\_\_\_ 20

13. ICT Employment Share and Individual Components of the AI Preparedness Index \_\_\_\_ 21

## EDITOR'S NOTE (3/1/24)

A correction has been made to Annex Table 5.1, which displays the AI Preparedness Indicators.

Specifically, the indicator under dimension IV, Regulation and Ethics, has been modified from "Overall

governance" to "Government effectiveness".

## Executive Summary

Artificial intelligence (AI) is set to profoundly change the global economy, with some commentators seeing it as akin to a new industrial revolution. Its consequences for economies and societies remain hard to foresee. This is especially evident in the context of labor markets, where AI promises to increase productivity while threatening to replace humans in some jobs and to complement them in others.

Almost 40 percent of global employment is exposed to AI, with advanced economies at greater risk but also better poised to exploit AI benefits than emerging market and developing economies. In advanced economies, about 60 percent of jobs are exposed to AI, due to prevalence of cognitive-task-oriented jobs. A new measure of potential AI complementarity suggests that, of these, about half may be negatively affected by AI, while the rest could benefit from enhanced productivity through AI integration. Overall exposure is 40 percent in emerging market economies and 26 percent in low-income countries. Although many emerging market and developing economies may experience less immediate AI-related disruptions, they are also less ready to seize AI's advantages. This could exacerbate the digital divide and cross-country income disparity.

AI will affect income and wealth inequality. Unlike previous waves of automation, which had the strongest effect on middle-skilled workers, AI displacement risks extend to higher-wage earners. However, potential AI complementarity is positively correlated with income. Hence, the effect on labor income inequality depends largely on the extent to which AI displaces or complements high-income workers. Model simulations suggest that, with high complementarity, higher-wage earners can expect a more-than-proportional increase in their labor income, leading to an increase in labor income inequality. This would amplify the increase in income and wealth inequality that results from enhanced capital returns that accrue to high earners. Countries' choices regarding the definition of AI property rights, as well as redistributive and other fiscal policies, will ultimately shape its impact on income and wealth distribution.

The gains in productivity, if strong, could result in higher growth and higher incomes for most workers. Owing to capital deepening and a productivity surge, AI adoption is expected to boost total income. If AI strongly complements human labor in certain occupations and the productivity gains are sufficiently large, higher growth and labor demand could more than compensate for the partial replacement of labor tasks by AI, and incomes could increase along most of the income distribution.

College-educated workers are better prepared to move from jobs at risk of displacement to high-complementarity jobs; older workers may be more vulnerable to the AI-driven transformation. In the UK and Brazil, for instance, college-educated individuals historically moved more easily from jobs now assessed to have high displacement potential to those with high complementarity. In contrast, workers without postsecondary education show reduced mobility. Younger workers who are adaptable and familiar with new technologies may also be better able to leverage the new opportunities. In contrast, older workers may struggle with reemployment, adapting to technology, mobility, and training for new job skills.

To harness AI's potential fully, priorities depend on countries' development levels. A novel AI preparedness index shows that advanced and more developed emerging market economies should invest in AI innovation and integration, while advancing adequate regulatory frameworks to optimize benefits from increased AI use. For less prepared emerging market and developing economies, foundational infrastructural development and building a digitally skilled labor force are paramount. For all economies, social safety nets and retraining for AI-susceptible workers are crucial to ensure inclusivity.

## I. Introduction

Artificial intelligence (AI) promises to boost productivity and growth, but its impact on economies and societies is uncertain, varying by job roles and sectors, with the potential to amplify disparities. As a positive productivity shock, AI will expand economies' production frontiers and will lead to reallocations between labor and capital while triggering potentially profound changes in many jobs and sectors. AI offers unprecedented opportunities for solving complex problems and improving the accuracy of predictions, enhancing decision-making, boosting economic growth, and improving lives. However, precisely because of its vast and flexible applicability in numerous domains, the implications for economies and societies are uncertain (Ilzetzki and Jain 2023).

AI represents a wide spectrum of technologies designed to enable machines to perceive, interpret, act, and learn with the intent to emulate human cognitive abilities. Across this spectrum, generative AI (GenAI) includes systems such as sophisticated large language models that can create new content, ranging from text to images, by learning from extensive training data. Other AI models, in contrast, are more specialized, focusing on discrete tasks such as pattern identification. Meanwhile, automation is characterized by its focus on optimizing repetitive tasks to boost productivity, rather than producing new content. The field of AI is experiencing a swift evolution, especially with the advent of GenAI, which has broadened AI's potential applications. This suggests that its impact will expand to reshape job functions and the division of labor.

One critical dimension to consider is the societal acceptability of AI. Acceptability may vary depending on job roles. Some professions may seamlessly integrate AI tools, while others could face resistance because of cultural, ethical, or operational concerns. This uncertainty becomes especially pronounced in labor markets. Although AI holds the potential for production-oriented applications, its effect will likely be mixed. In some sectors where human oversight of AI is necessary, it could amplify worker productivity and labor demand. Conversely, in other sectors, AI might pave the way for significant job displacements. A rise in aggregate productivity of the economy could however strengthen overall economic demand, potentially creating more job opportunities for most workers in a ripple effect. Moreover, this evolution could also lead to the emergence of new sectors and job roles—and the disappearance of others—transcending mere intersectoral reallocation.

Beyond immediate job effects, another critical economic dimension is the capital income channel. As AI drives efficiency and innovations, those who own AI technologies or have stakes in AI-driven industries may experience increased capital income. This shift could potentially exacerbate inequalities.

AI challenges the belief that technology affects mainly middle and, in some cases, low-skill jobs: its advanced algorithms can now augment or replace high-skill roles previously thought immune to automation. While historical waves of automation and the integration of information technology affected predominantly routine tasks, AI's capabilities extend to cognitive functions, enabling it to process vast amounts of data, recognize patterns, and make decisions. As a result, even high-skill occupations, which were previously considered immune to automation because of their complexity and reliance on deep expertise now face potential disruption. $^{1}$ Jobs that require nuanced judgment, creative problem-solving, or intricate data

interpretation—traditionally the domain of highly educated professionals—may now be augmented or even replaced by advanced AI algorithms, potentially exacerbating inequality across and within occupations. This shift challenges the conventional wisdom that technological advances threaten primarily lower-skill jobs and points to a broader and deeper transformation of the labor market than by previous technological revolutions.

The impact of AI is also likely to differ significantly across countries at different levels of development or with different economic structures. Advanced economies, with their mature industries and service-driven economies, typically have a higher concentration of jobs in sectors that require complex cognitive tasks. These economies are therefore both more susceptible to, yet better positioned to benefit from, AI innovations. Conversely, emerging market and developing economies, often still reliant on manual labor and traditional industries, may initially face fewer AI-induced disruptions. However, these economies may also miss out on early AI-driven productivity gains, given their lack of infrastructure and a skilled workforce. Over time, the AI divide could exacerbate existing economic disparities, with advanced economies harnessing AI for competitive advantage while emerging market and developing economies grapple with integrating AI into their growth models.

To inform the discussion on the potential impact of AI on the future of work and which policies countries should enact in response, this note aims to answer six questions.

(1) Which countries are more exposed to AI adoption? Which countries are likely to benefit most?

(2) How differently will AI affect workers within countries? Which segments of workers are likely to thrive and which face more risks?

(3) Historically, how frequently did workers shift between roles now facing varying AI exposure? What insights do these shifts reveal about labor adaptability?

(4) In what ways could AI reshape income and wealth inequality?

(5) What is the potential impact for growth and productivity?

(6) Which countries appear better prepared for the AI transition? How can policies maximize gains and mitigate likely AI-related challenges?

This note builds on a growing body of work that explores the impact of AI on labor markets and the macroeconomy. Many empirical studies so far have focused largely on the US, finding that many of the tasks of a significant portion of the workforce, including those of high-skilled workers, could be substantially replaced by AI (for example, Felten, Raj, and Seamans 2021, 2023; Eloundou and others 2023; Webb 2020). A few studies (OECD 2023; Albanesi and others 2023; Briggs and Kodnani 2023) adopt a cross-country approach; Gmyrek, Berg, and Bescond (2023) undertake a comprehensive review of emerging market economies and find less exposure to AI than in advanced economies; Colombo, Mercorio, and Mezzanzanica (2019) focus on the Italian labor market. These studies apply empirical approaches similar to those used in the automation literature (for example, Autor and Dorn 2013, Acemoglu and Restrepo 2022, Das and Hilgenstock 2022).

This note contributes to the existing literature in four significant ways. First, while previous AI exposure measures often implicitly equate exposure with substitutability of human tasks, this note attempts to assess the potential for complementarity and substitution with labor, using the approach developed by Pizzinelli and others (2023). This method considers the wider social, ethical, and physical context of occupations, along with required skill levels, to discern whether AI may complement or replace roles. This adds to recent studies that have attempted to make this distinction using a purely task-based framework (Acemoglu and Restrepo 2018, 2022; Gmyrek, Bert, and Bescond 2023). Second, the note offers some initial insight into the potential for

workers to make the transition from occupations at risk of displacement to those with high AI-complementarity potential, drawing on microdata for one advanced and one emerging market economy. Third, it takes a deep look at how AI may affect income and wealth inequality within countries. It dissects AI exposure patterns across demographics and earnings levels and uses a model-based analysis to evaluate AI's impact on labor and capital income inequality, as well as on income levels. Last, the note examines how AI preparedness for this technological shift may differ across countries at different income levels, using a very large sample of advanced and emerging market and developing economies.

With this analysis there are some important caveats. First, although in the model analysis activity grows in occupations with high AI complementarity and falls in low-complementarity occupations—mimicking sectoral reallocations—the analysis on AI exposure assumes that sector sizes are fixed and that the tasks required in each occupation are unchanged. Consequently, the results are more pertinent for the short to medium term. Over longer horizons, workers will likely migrate across different sectors and roles, or acquire new skills, and jobs will evolve. In addition, the analysis assumes that workers within the same occupation will be affected in the same way, but there can be variation in the effects of AI. AI may also affect firm dynamics and market concentration (Babina and others, forthcoming), driving inequality between workers at different firms. Second, the study relies on the premise that tasks performed within similar occupations are homogenous around the world, while there can be significant cross-country variations. Third, the approach abstracts from linkages across occupations and countries (trade linkages), as well as from cross-border spillovers of AI exposure. Last, while the analyses on workers' AI exposure and soc

[中间内容因长度限制已省略]

022. "Understanding Growth through Automation." Research Department, Federal Reserve Bank of Philadelphia, Philadelphia, PA.

Eloundou, T., S. Manning, P. Mishkin, and D. Rock. 2023. “GPTs are GPTs: An Early Look at the Labor Market Impact Potential of Large Language Models.” arXiv.org working paper.

Financial Conduct Authority (FCA). 2022. “Machine Learning in UK Financial Services.” Bank of England and Financial Conduct Authority, London, UK.

Felten, E., M. Raj, and R. Seamans. 2021. "Occupational, Industry, and Geographic Exposure to Artificial Intelligence: A Novel Dataset and Its Potential Uses." Strategic Management Journal 42 (12): 2195–217.

Felten, E., M. Raj, and R. Seamans. 2023. "How Will Language Modelers Like ChatGPT Affect Occupations and Industries?" arXiv.org working paper.

Gmyrek, P., J. Berg, and D. Bescond. 2023. Generative AI and Jobs: A Global Analysis of Potential Effects on Job Quantity and Quality. ILO Working Paper 96. International Labour Organization, Geneva, Switzerland.

International Finance Corporation (IFC). 2020. “Artificial Intelligence in Emerging Markets: Opportunities, Trends and Emerging Business Models.” International Finance Corporation. World Bank, Washington, DC.

Ilzetzki, E., and S. Jain. 2023. The Impact of Artificial Intelligence on Growth and Employment. VoxEU.org, June 20.

Haksar, V., Y. Carriere-Swallow, E. Islam, A. Giddings, K. Kao, E. Kopp, and G. Quiros-Romero. 2021. "Toward a Global Approach to Data in the Digital Age," IMF Staff Discussion Note 2021/005, International Monetary Fund, Washington, DC.

International Monetary Fund (IMF). 2017. World Economic Outlook: Gaining Momentum? Chapter 3. International Monetary Fund, Washington, DC, April.

International Monetary Fund (IMF). 2023. World Economic Outlook: A Rocky Recovery, Chapter 2. International Monetary Fund, Washington, DC, April.

Jamilov, R., H. Rey, and A. Tahoun. 2023. "The Anatomy of Cyber Risk." NBER Working Paper 28906, National Bureau of Economic Research, Cambridge, MA.

Kambourov, G., and I. Manovskii. 2009. "Occupational Mobility and Wage Inequality." Review of Economic Studies 50: 731–59.

Keller, W. "International Technology Diffusion." 2004. Journal of Economic Literature 42 (3): 752–82.

Klinova, K., and A. Korinek. 2021. "AI and Shared Prosperity." In Proceedings of the 2021 AAAI/ACM Conference on AI, Ethics, and Society, 645–51.

Moll, B., L. Rachel, and P. Restrepo. 2022. "Uneven Growth: Automation's Impact on Income and Wealth Inequality." Econometrica 90 (6): 2645–683.

Monsueto, S. E., A. Moreira Cunha, and J. da Silva Bichara. 2014. "Occupational Mobility and Income Differentials: The experience of Brazil between 2002 and 2010." Cepal Review 113: 139–55.

Moscarini, G., and F. G. Vella. 2008. “Occupational Mobility and the Business Cycle.” NBER Working Paper 13819, National Bureau of Economic Research, Cambridge, MA.

Nicoletti, G., C. V. Rueden, and D. Andrews. 2020. “Digital Technology Diffusion: A Matter of Capabilities, Incentives or Both?” European Economic Review 128: 103513.

Organisation for Economic Co-operation and Development (OECD). 2023. “OECD Employment Outlook 2023: Artificial Intelligence and the Labour Market.” Paris, France.

Oxford Insights. 2022. "Government AI Readiness Index." Malvern, UK.

Pizzinelli, C., A. Panton, M. M. Tavares, M. Cazzaniga, and L. Li. 2023. "Labor Market Exposure to AI: Cross-Country Differences and Distributional Implications." IMF Working Paper 2023/216, International Monetary Fund, Washington, DC.

Ribas, R. P., and S. S. D. Soares. 2008. “The IBGE Monthly Employment Survey (PME) Panel.” Discussion Paper 1348, Institute of Applied Economic Research, Brasília, Brazil.

Rockall, E., C. Pizzinelli, and M. Mendes Tavares. Forthcoming. "Artificial Intelligence Adoption and Inequality." IMF Working Paper, International Monetary Fund, Washington, DC.

Sahay, R., M. Čihák, P. N'Diaye, A. Barajas, S. Mitra, A. Kyobe, Y. N. Mooi, and S. R. Yousefi. 2017. "Financial Inclusion: Can It Meet Multiple Macroeconomic Goals?" IMF Staff Discussion Note 2015/017, International Monetary Fund, Washington, DC.

Sahay, R., and M. Čihák. 2020. "Finance and Inequality." IMF Staff Discussion Note 2020/001, International Monetary Fund, Washington, DC.

Sahay, R., U. Eriksson von Allmen, A. Lahreche, P. Khera, S. Ogawa, M. Bazarbash, and K. Beaton. 2020. "The Promise of Fintech: Financial Inclusion in the Post COVID-19 Era." IMF Departmental Paper 2020/009, International Monetary Fund, Washington, DC.

Shabsigh, G., and E. B. Boukherouaa. 2023. “Generative Artificial Intelligence in Finance.” Fintech Note 2023/006, International Monetary Fund, Washington, DC.

United Nations Educational, Scientific and Cultural Organization (UNESCO). 2021. “AI and Education: Guidance for Policy-Makers.” Paris, France.

US Agency for International Development (USAID). 2019. “Artificial Intelligence in Global Health: Defining a Collective Path Forward.” Washington, DC.

Wahl, B., A. Cossy-Gantner, S. Germann, and N. R. Schwalbe. 2018. "Artificial Intelligence (AI) and Global Health: How Can AI Contribute to Health in Resource-Poor Settings?" BMJ Global Health 3 (4): e000798.

Webb, M. 2020. “The Impact of Artificial Intelligence on the Labor Market.” Stanford University Working Paper, Stanford, CA.

Wootton, C. W., and B. E. Kemmerer. 2007. "The Emergence of Mechanical Accounting in the US, 1880–1930." Accounting Historians Journal 34 (1): 91–124.

Yashiro, N., T. Kyyrä, H. Hwang, and J. Tuomala. 2022. “Technology, Labour Market Institutions and Early Retirement.” Economic Policy 37 (112): 811–49.

![](images/ad3b2b359842b04ea78b0d72e843d7960b1c886587a4a28d550404c23af185b1.jpg)
"""
