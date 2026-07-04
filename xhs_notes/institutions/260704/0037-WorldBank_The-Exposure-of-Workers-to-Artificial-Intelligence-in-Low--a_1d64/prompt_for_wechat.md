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
11057

# The Exposure of Workers to Artificial Intelligence in Low- and Middle-Income Countries

Gabriel Demombynes

Jörg Langbein

Michael Weber

POLICY RESEARCH WORKING PAPER 11057

## Abstract

Research on the labor market implications of artificial intelligence has focused principally on high-income countries. This paper analyzes this issue using microdata from a large set of low- and middle-income countries, applying a measure of potential artificial intelligence occupational exposure to a harmonized set of labor force surveys for 25 countries, covering a population of 3.5 billion people. The approach advances work by using harmonized microdata at the level of individual workers, which allows for a multivariate analysis of factors associated with exposure. Additionally, unlike earlier papers, the paper uses highly detailed (4 digit) occupation codes, which provide a more reliable mapping of artificial intelligence exposure to occupation. Results within countries, show that artificial intelligence exposure is higher for women, urban workers, and those with higher education. Exposure decreases by country income level, with high exposure for just 12 percent of workers in low-income countries and 15 percent of workers in lower-middle-income countries. Furthermore, lack of access to electricity limits effective exposure in low-income countries. These results suggest that for developing countries, and in particular low-income countries, the labor market impacts of artificial intelligence will be more limited than in high-income countries. While greater exposure to artificial intelligence indicates larger potential for future changes in certain occupations, it does not equate to job loss, as it could result in augmentation of worker productivity, automation of some tasks, or both.

# The Exposure of Workers to Artificial Intelligence in Low- and Middle-Income Countries

Gabriel Demombynes, $^{1}$ Jörg Langbein, $^{2}$ and Michael Weber $^{3}$

JEL classification: J24, J21, O33

Keywords: Jobs and Development, Human Capital and Growth, Digital Economy Strategy

## 1. Introduction

The field of artificial intelligence (AI) has undergone remarkable development in recent years. Most notable has been the takeoff of generative AI since the introduction of ChatGPT 3.5 in November 2022. Investment in the sector has exploded, and the topic of AI has become a focus in debates worldwide (Maslej et al. 2024). While the future of AI is unpredictable (Brynjolfsson et al. 2024), many observers expect that AI will lead to fundamental changes in jobs, skills requirements, and economic structures like those set in motion by the Industrial Revolution and the advent of the digital age (Cazzaniga et al. 2024). The ultimate effects on workers and jobs, however, remain highly uncertain.

Most economic research on the effects of generative AI on workers has focused on high-income countries (HICs). Only a few papers have considered what AI will mean for low- and middle-income countries (LMICs) (Comunale and Manera, 2024, Gmyrek et al. 2024). AI's overall impacts may differ in LMICs from HICs due to differences in three principal areas: infrastructure, human capital, and economic structure. First, the basic foundations for AI use—consistent access to electricity and affordable internet—are not universally available in some developing countries. In low-income countries, less than half of the people have access to electricity and just over one in four (27 percent) use the internet. Second, the levels of human capital needed to work effectively with AI are much lower in LMICs. Around 70 percent of children in low- and middle-income countries are “learning poor,” meaning that they cannot read and comprehend a simple text by age 10 (World Bank 2022). Third, LMICs typically have a different economic structure, with a large share of workers in agriculture and low-skilled service jobs and fewer in knowledge-intensive sectors and occupations, which may be most affected by AI.

In this paper we analyze how differences in occupational composition may affect AI's impact on jobs, with a focus on middle- and low-income countries and including the United States for comparison. We advance over the existing nascent literature in a number of ways. First, we apply the AI Occupational Exposure (AIOE) index developed by Felten et al. (2021) to labor force surveys covering a population of 3.5 billion people or around 45 percent of the world's population. The AIOE relies on the O\*NET classification of occupations originally developed for the US labor market. Second, we use detailed microdata from a larger set of low-, lower-middle-, and upper-middle-income countries than employed in earlier studies like Cazzaniga et al. (2024) and Pizzinelli et al. (2023). The use of harmonized individual-level data for 25 countries across all income groups allows the identification of systematic differences and stylized facts. The dataset includes occupation-level data at the more granular four-digit International Standard Classification of Occupation (ISCO) level. Third, we exploit that microdata to explore how AI exposure varies by different socio-demographic groups in a multivariate framework. This allows us to provide a more differentiated view than earlier studies.

We find large differences in exposure to AI occupations by country income level. We normalize exposure at the individual worker level on a scale that ranges from 0 (no exposure) to 100 (full exposure). Mean exposure across workers is greatest in our high-income country (the United States) at 62. This is followed by upper-middle-income countries with an average exposure level of 49, and lower-middle-income countries with a mean of 44. Workers in low-income countries have an exposure value to AI of 37. At the worker level, education level is strongly associated with AI occupation exposure in middle-income countries. Female workers are more exposed to AI in all country income levels, but the gap is much more pronounced in high- and upper middle-income countries. Urban workers are generally more exposed to AI than rural workers. Overall, we find general support for the notion that advances in AI will disproportionately affect white-collar occupations.

We also overlay the measure of AI exposure at the worker level with household-level data on electricity access. This analysis shows that energy access is a further constraint to AI exposure, principally for rural residents of low-income countries.

The paper is structured as follows: Section 2 provides a literature review on AI and the labor market with a focus on low- and middle-income countries and introduces the data and approach used in the analysis. Section 3 reports stylized facts about cross-country AI occupation exposure for the country sample. Section 4 concludes.

## 2. Measuring AI exposure and labor market impacts

Artificial intelligence (AI) may transform labor markets and the nature of work in a manner analogous to the Industrial Revolution (Cazzaniga et al. 2024). With its capacity to automate tasks, optimize processes, and augment human capabilities, AI is poised to reshape job roles, the skills required, and the composition of the economy. In contrast to previous episodes of technological change, this process is not characterized only by the automation of routine, repetitive tasks. Generative AI models can learn from data and create new things on their own, affecting diverse sectors of the economy. As a result, AI could fundamentally alter the nature of work. To gauge the potential effects of AI, the literature has used a “task model” approach following Autor et al. (2003). These models consider each occupation as a set of tasks. Linking this to AI, tasks are classified by their level of “exposure” to AI, and then these measures are aggregated into a measure of exposure at the occupation level. Definitions of exposure and its interpretation vary across studies.

It is important to note that exposure does not necessarily mean that a task or job will be replaced by AI. It could also mean that AI will augment productivity of the task or result in a reconfiguration of the composition of occupations or jobs.

The following section describes approaches to measure the exposure of occupations to AI before reviewing some of the current empirical literature on AI.

## 2.1. Measuring AI exposure

A task model approach has been employed by numerous research efforts to assess the impact of digital technologies and AI on occupations, utilizing the US-based O\*NET database (e.g., Autor and Handel 2013). The O\*NET database has most often been used for analysis of the labor market of the United States and other high-income countries. Originally developed by the US Department of Labor, the database provides detailed information on a wide range of occupations, including job duties, required skills, educational qualifications and labor market trends. The primary goal of the database is to help individuals make informed decisions about career paths based on their skills and interests. It does this by providing a detailed description of current occupations and the tasks and skills required to perform them. It is updated regularly, and the job definitions have been used in research to provide insights into job trend analysis and workforce development.

One of the most prevalent indicators utilized in AI-related analysis is the "Artificial Intelligence Occupation Exposure" (AIOE) index developed by Felten, Raj, and Seanmans (2021). This index is predicated on the O\*NET classification of occupations and defines AI exposure by linking the human tasks in an occupation with AI applications, continuing the work by Frey and Osborne (2017) who focused on computerization. Pizzinelli et al. (2023) further developed this index by incorporating additional information from the O\*NET database. This included the social, ethical, and physical context of occupations, as well as the required skill level. Another similar research approach was developed by Webb (2020). This approach identified the intersection between AI capabilities described in patents and the job descriptions provided by O\*NET. Occupations with a higher fraction of tasks that overlap with patented AI capabilities are classified as more exposed to AI. This index provides a patent-based perspective on AI exposure, offering a unique lens on how emerging AI technologies might impact various job roles. Both Felten et al. (2021) and Webb (2020) underscore the capabilities of AI within existing tasks. Separately, Brynjolfsson et al. (2018) evaluate the suitability of specific tasks for machine learning and connect these assessments to O\*NET occupations.

## 2.2. AI impacts in the labor market worldwide

The body of work on potential AI-related impacts in the labor market is growing, with a particular focus on the United States. $^{4}$ A stylized economic model assumes that AI-related tasks increase the productivity of workers, either substituting or complementing current work. Research has been conducted within firms, at the macroeconomic level, and considering overall effects of AI on workers.

On the firm level, many assume that productivity may increase following the introduction of AI (e.g. Agrawal et al. 2019), viewing it as an additional input to a firm's production function. However, firms will need time to adapt to the new technology and the impact on productivity may only be observed with a delay (Brynjolfsson et al. 2019). Researchers have linked firm economic performance to AI patent registration (e.g. van Roy et al. 2020, Behrens and Truschke 2020), analyzed online job vacancies (e.g. Acemoglu et al. 2022, Babina et al. 2024), and used a survey-based approach to assess the prevalence of AI usage within firms (Czarnitzki et al. 2023). Svanberg et al. (2024) estimate that firms will introduce AI gradually and at a much slower pace than originally anticipated given the introduction costs firms face. A synthesis of several academic studies estimates the overall impact of AI adoption on annual worker productivity growth within a firm to be between 1.7 and 2.7 percentage points (Hatzius et al. 2023).

There is some evidence that highly skilled workers will be particularly affected by recent AI developments (e.g., Felten et al. 2021, Felten et al. 2023). Some recent studies on generative AI have demonstrated that for a given task, productivity gains are primarily observed in lower-skilled, less experienced workers (Brynjolfsson et al. 2023, Noy and Zhang 2023).

In a study on the United States, Eloundou et al. (2023) used the O\*NET database to gauge the impacts of large language models (LLMs) and calculate the potential for AI and automation. The authors conclude that approximately 20 percent of jobs are exposed to LLM in more than 50 percent of their tasks, suggesting that the impact of AI is pervasive and has significant effects on economic activities. A McKinsey study (2024) obtains similar results and estimates that about 27 percent of tasks in European countries and around 30 percent of tasks in the US will be AI-based in the near future (Hazan et al. 2024). Hatzius et al. (2023) conclude that generative AI could substitute up to one-quarter of current work, thereby raising US labor productivity growth by approximately 1.5 percentage points over the next ten years.

To date, only a few papers have considered the potential impacts of AI on low- and middle-income countries. The most recent and prominent examples are Pizzinelli et al. (2023) and Cazzaniga et al. (2024). Pizzinelli et al. (2023) expanded the AIOE index with a measure of complementarity and applied it to two high-income countries (the United Kingdom and the United States) and four middle-income countries (Brazil, Colombia, India, and South Africa). The authors identified differences between countries when examining AI occupation exposure due to disparate employment structures. However, when accounting for complementarity, these differences diminished. In all countries, the authors detect a higher occupational exposure to AI for women and highly educated workers, as well as for workers with higher earnings. Cazzaniga et al. (2024) further develop this approach and find that, using ILO employment indicators, nearly 40 percent of workers worldwide are exposed to AI. Additionally, they conclude that AI may exacerbate inequality. Overall, they conclude that the degree of AI exposure varies across economies, with advanced economies reporting a higher prevalence of AI-impacted jobs, reaching up to 60 percent compared to 40 percent in emerging markets and 26 percent in low-income countries.

Gmyrek et al. (2023) employ a distinct methodology, prompting ChatGPT-4 to gauge occupational and task-level exposure to AI. The resulting estimates are then applied to country-level data from 59 countries, comprising eight low-income countries, 24 lower-middle-income countries, 19 upper-middle-income countries, and eight high-income countries. The authors conclude that the effect of AI on labor markets varies across country income groups. Focusing only on workers in Latin America, Gmyrek et al. (2024) further estimate that it is mostly younger, urban-based and better educated workers that are exposed to AI. Workers in high-income countries have the highest exposure to automation and augmentation. Focusing on China as an example of a middle-income country, Lou et al. (2024) demonstrate that the occupational exposure to AI is lower than in the United States. The effects of AI are still pervasive throughout the Chinese economy, but the magnitude of these effects varies by geographic location within China.

Other researchers have used simulations or theoretical frameworks to assess AI's potential impacts. Acemoglu and Restrepo (2019), for example, provide a framework for AI-related or automation technologies. The framework's core concept is that labor demand for workers in occupations susceptible to automation-induced displacement may decline due to the accrual of productivity gains. Accordingly, the overall effects on job displacement then depend on the workers' ability to move to other occupations and the potential to create new jobs. Depending on what magnitude of the two opposing effects prevails, this could overall result in either more jobs being created (World Economic Forum 2023) or more jobs disappearing (Acemoglu and Johnson 2023). $^{5}$ There is also the risk of linking humanoid robots to generative AI appliances, which could further expand the effects of AI on the workforce (Acemoglu and Restrepo 2020). Importantly, certain demographic groups may encounter greater challenges in adapting to this process. For instance, younger workers may be more readily able to adjust to AI than older workers.

## 2.3. Data and methodology

We rely on two different types of data to examine AI exposure:

(1) Worker-level information: We use the global labor database (GLD) that provides access to harmonized labor force surveys for 25 countries. The surveys are harmonized on all levels for a set of key variables and give access to the 4-digit International Standard Classification of Occupations (ISCO). The countries included in the database are predominantly low- and middle-income countries. To enable comparisons with high income countries, we also include household survey data for the United States and Chile. $^{6}$ We rely on the latest labor force survey data collected from 2014 to 2023 for these 25 countries. Overall, the analysis encompasses data from approximately 3 million workers.

(2) Indicator on AI occupational exposure (AIOE): This study adopts the AIOE index, developed by Felten et al. (2021) to explore the potential for AI exposure on occupations. The construction of the index is twofold. In a first step, Felten et al. (2021) identified a set of applications of AI building on the information provided by the Electronic Frontier Foundation AI Progress Measurement Project. In a second step, Felten et al (2021) combine information on the AI applications with the tasks and abilities as listed in the Occupational Information Network (O\*NET). This yields the AIOE, a measure of occupational exposure to AI applications. This measure ranges from the lowest AIOE of -2.67, which is for “Dancers”, to the highest calculated AIOE of 1.58 for “Genetic Counselors”. The occupations the index reports stem from the Standard Occupational Classification (SOC) system in the 2018 version. As our harmonized surveys are stored in the International Standard Classification of Occupations (ISCO), we map the SOC level information to ISCO 2008

[中间内容因长度限制已省略]

d>43</td><td>53</td><td>33</td><td>39</td><td>47</td><td>69</td><td>44</td><td>51</td><td>47</td></tr><tr><td>Türkiye</td><td>52</td><td>54</td><td>51</td><td>N/A</td><td>N/A</td><td>37</td><td>39</td><td>48</td><td>74</td><td>48</td><td>57</td><td>50</td></tr><tr><td>United States</td><td>62</td><td>65</td><td>59</td><td>56</td><td>63</td><td>41</td><td>33</td><td>49</td><td>70</td><td>51</td><td>62</td><td>64</td></tr><tr><td>Zambia</td><td>54</td><td>59</td><td>50</td><td>44</td><td>59</td><td>48</td><td>48</td><td>55</td><td>76</td><td>46</td><td>55</td><td>55</td></tr><tr><td>Zimbabwe</td><td>51</td><td>57</td><td>46</td><td>45</td><td>56</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>43</td><td>50</td><td>54</td></tr><tr><td>Overall Mean</td><td>47</td><td>49</td><td>46</td><td>39</td><td>55</td><td>34</td><td>38</td><td>48</td><td>70</td><td>43</td><td>49</td><td>47</td></tr></table>

Note: Results are population weighted and include workers aged 15 to 64

Table 4: AIOE regression output

<table><tr><td></td><td>High Income</td><td>Upper-middle Income</td><td>Lower-middle Income</td><td>Low Income</td></tr><tr><td>Elementary occupations</td><td>Base</td><td>Base</td><td>Base</td><td>Base</td></tr><tr><td>Professionals</td><td>66.28**(36.61)</td><td>56.27***(22.66)</td><td>59.63***(77.39)</td><td>56.34***(22.66)</td></tr><tr><td>Technicians</td><td>53.62**(29.62)</td><td>39.71***(11.95)</td><td>39.65***(29.39)</td><td>37.34***(25.32)</td></tr><tr><td>Clerks</td><td>52.94**(42.42)</td><td>50.43***(9.29)</td><td>52.40***(41.91)</td><td>46.23***(31.18)</td></tr><tr><td>Service and market sales workers</td><td>36.05**(19.57)</td><td>21.92**(3.55)</td><td>25.29***(24.67)</td><td>21.84***(5.87)</td></tr><tr><td>Skilled agricultural</td><td>22.83(2.71)</td><td>11.48***(6.53)</td><td>4.039**(2.91)</td><td>-5.570***(-22.82)</td></tr><tr><td>Craft workers</td><td>20.88(6.24)</td><td>4.083(1.12)</td><td>6.219***(8.17)</td><td>7.611(1.01)</td></tr><tr><td>Machine operators</td><td>23.26*(9.95)</td><td>8.303*(2.15)</td><td>10.06***(12.83)</td><td>6.451*(2.44)</td></tr><tr><td>Managers</td><td>62.62**(26.17)</td><td>49.86***(12.12)</td><td>51.26***(25.14)</td><td>49.46***(18.74)</td></tr><tr><td>Agriculture</td><td>Base</td><td>Base</td><td>Base</td><td>Base</td></tr><tr><td>Mining</td><td>6.305(0.78)</td><td>3.084(0.94)</td><td>-2.952**(-2.87)</td><td>-4.697(-1.65)</td></tr><tr><td>Manufacturing</td><td>6.809(1.02)</td><td>9.010(1.71)</td><td>-0.600(-0.38)</td><td>0.875(0.19)</td></tr><tr><td>Public utilities</td><td>7.603(1.22)</td><td>10.87**(2.80)</td><td>1.639(1.70)</td><td>6.291**(3.92)</td></tr><tr><td>Construction</td><td>7.668(0.97)</td><td>1.002(0.19)</td><td>-5.899***(-6.34)</td><td>-0.113(-0.13)</td></tr></table>

<table><tr><td>Commerce</td><td>8.108(1.28)</td><td>17.01*(2.04)</td><td>8.305***(5.58)</td><td>17.24***(8.12)</td></tr><tr><td>Transport and Communications</td><td>7.484(1.18)</td><td>12.74*(2.49)</td><td>4.454***(3.61)</td><td>10.42**(3.90)</td></tr><tr><td>Financial and Business Services</td><td>12.52(1.79)</td><td>11.70*(2.04)</td><td>4.251***(3.37)</td><td>9.439*(2.81)</td></tr><tr><td>Public Administration</td><td>6.322(0.98)</td><td>10.91*(2.20)</td><td>1.153(0.84)</td><td>5.327*(2.84)</td></tr><tr><td>Other Services</td><td>1.274(0.19)</td><td>4.475(0.88)</td><td>-3.788**(-2.82)</td><td>3.980(1.31)</td></tr><tr><td>15-24</td><td>Base</td><td>Base</td><td>Base</td><td>Base</td></tr><tr><td>25-34</td><td>1.682**(19.10)</td><td>0.121(0.43)</td><td>0.173**(2.93)</td><td>0.379(1.36)</td></tr><tr><td>35-64</td><td>3.614**(31.18)</td><td>0.272(1.04)</td><td>0.241**(3.09)</td><td>0.719(0.93)</td></tr><tr><td>Female</td><td>Base</td><td>Base</td><td>Base</td><td>Base</td></tr><tr><td>Male</td><td>-2.520**(-49.21)</td><td>-0.478***(-5.48)</td><td>-0.123(-0.91)</td><td>0.176(0.24)</td></tr><tr><td>Rural</td><td>Base</td><td>Base</td><td>Base</td><td>Base</td></tr><tr><td>Urban</td><td>0.960**(57.85)</td><td>-0.310(-1.14)</td><td>0.363***(3.32)</td><td>-0.0351(-0.05)</td></tr><tr><td>No education</td><td>Base</td><td>Base</td><td>Base</td><td>Base</td></tr><tr><td>Primary</td><td>-0.800(-0.81)</td><td>0.197(0.44)</td><td>0.249(1.30)</td><td>-0.246(-0.26)</td></tr><tr><td>Secondary</td><td>-0.245(-0.30)</td><td>0.577(1.55)</td><td>0.0924(0.38)</td><td>-0.287(-0.30)</td></tr><tr><td>Post-secondary</td><td>3.241(3.57)</td><td>3.750***(5.76)</td><td>1.767***(5.05)</td><td>0.975(1.61)</td></tr></table>

<table><tr><td>Paid employee</td><td>Base</td><td>Base</td><td>Base</td><td>Base</td></tr><tr><td rowspan="2">Non-paid employee</td><td>4.704*</td><td>2.038**</td><td>3.209***</td><td>4.817***</td></tr><tr><td>(12.46)</td><td>(3.44)</td><td>(4.94)</td><td>(18.61)</td></tr><tr><td rowspan="2">Employer</td><td>-3.701</td><td>2.822**</td><td>1.550</td><td>4.898**</td></tr><tr><td>(-2.67)</td><td>(2.99)</td><td>(1.09)</td><td>(5.75)</td></tr><tr><td rowspan="2">Self-employed</td><td>-1.357</td><td>5.191***</td><td>4.075***</td><td>6.913***</td></tr><tr><td>(-1.21)</td><td>(11.07)</td><td>(6.24)</td><td>(32.86)</td></tr><tr><td rowspan="2">Other worker</td><td></td><td>-3.842</td><td>1.963***</td><td>4.099**</td></tr><tr><td></td><td>(-1.32)</td><td>(3.93)</td><td>(4.60)</td></tr><tr><td>Country Dummies</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Survey Dummies</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td rowspan="2">Constant</td><td>10.50</td><td>18.65***</td><td>26.46***</td><td>24.19***</td></tr><tr><td>(1.26)</td><td>(6.56)</td><td>(30.59)</td><td>(19.99)</td></tr><tr><td>Observations</td><td>123780</td><td>814562</td><td>1269224</td><td>82189</td></tr></table>
"""
