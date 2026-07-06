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
- 已识别机构名：`亚洲开发银行`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
8. 文末自然承接未解问题，只写一段很短的轻 CTA。不要照抄固定话术，不要堆身份名单；语义可以参考但不必全塞：更多完整报告、中文摘要、KC评论和图表合集，会放进每日国际信源汇编。适合快速扫当天主流叙事，也方便后续追问和横向比较。。
9. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
10. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定套话。文末只保留 1-2 句，重点说“完整报告、中文摘要、KC评论和图表合集可以放回当天国际主线里继续看”，不要在正文中段出现。
- 严禁中段 CTA。正文中间不要出现“如果你从某些关键词搜到这里”“单篇文章只能解决一个切片”“我每天会把……”这类表达。

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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份亚洲开发银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## KEY POINTS

\- This brief presents experimental estimates on Mongolia's digital economy. The analysis applies the Digital Supply and Use Table (DSUT) framework to measure digitalization across three dimensions—digital industries, digital products, and digital transactions.

\- Using Mongolia's 2015–2019 Supply and Use Tables, experimental DSUTs are compiled, focusing on digitally enabling industries due to data limitations. Preliminary results show that the digital economy contributed an average of 1.6% to Mongolia's gross domestic product from 2015 to 2019.

\- To complement the DSUT-based estimates, the analysis also applies the Asian Development Bank's input-output-based value flow methodology. Estimates derived from the two approaches highlight the growing importance of digital activities in Mongolia's economy.

\- This brief also discusses the use of alternative data sources and further methodological refinements to enhance and enable broader coverage of future estimates.

# Measuring the Digital Economy of Mongolia

Sameeksha Jain
Consultant
Economic Research and Development
Impact Department (ERDI)
Asian Development Bank (ADB)

Mahinthan Joseph Mariasingham
Principal Statistician
ERDI, ADB

Aparajita Pandharkar
Consultant
Pacific Department, ADB

Maegan Saroca
Consultant
ERDI, ADB

Nuri Ohn
Statistician
ERDI, ADB

Irene Talam
Consultant
ERDI, ADB

## INTRODUCTION

The emergence of the digital economy marks a pivotal transformation in the global economic landscape, fundamentally reshaping how economic activities are conducted and how products are created, managed, stored, and exchanged. This shift has been driven by the widespread adoption of technology and has revolutionized business operations, consumer behavior, supply chains, and the flow of goods and services across the world.

In Mongolia, the development of information and communication technology (ICT) is recognized as a key driver of economic diversification and long-term growth. This priority aligns with the Government of Mongolia's Vision 2050, which identifies science, technology, and innovation as central pillars of national development. Policy initiatives led by the Ministry of Digital Development, Innovation, and Communications aim to promote software and digital content production and expand exports of digital goods and services (Government of Mongolia, Ministry of Digital Development, Innovation, and Communications n.d.). Strengthening ICT infrastructure and improving internet connectivity are expected to enhance e-commerce, help overcome geographical constraints, and contribute to economic diversification (United Nations Trade and Development 2023).

As digital transformation advances, the availability of robust, consistent, and policy-relevant statistics becomes increasingly important for understanding the scale, structure, and evolution of the digital economy. This policy brief is a product of the collaborative initiative between the Asian Development Bank (ADB) and the National Statistics Office of Mongolia, with support from the Republic of Korea e-Asia and Knowledge Partnership Fund, to compile an experimental Digital Supply and Use Table (DSUT) for Mongolia. The DSUT framework provides a systematic approach to measuring digitalization by distinguishing between digital industries, digital products, and digital transactions.

The experimental DSUTs cover 2015–2019 and focus on digitally enabling industries, reflecting current data availability. This brief presents preliminary results, discusses key methodological and data challenges, and introduces an alternative input-output-based value flow approach developed by ADB. Together, these methods provide complementary insights into the role of digital activities in Mongolia's economy and inform future statistical development efforts.

Preliminary findings indicate that digital industries comprised an estimated $1.51\%$ to $1.81\%$ of Mongolia's gross domestic product (GDP) between 2015 and 2019. Comparing the growth of digital industries with that of the overall economy provides valuable insights for policymakers in formulating strategies to advance Mongolia's digitalization agenda. Future iterations of the DSUTs are expected to refine these estimates, incorporate additional digital industries, and expand coverage to other dimensions of the digital economy.

## CONSTRUCTION OF MONGOLIA'S 2015–2019 DIGITAL SUPPLY AND USE TABLES

## Methodology and Data Sources for the Compilation of the Digital Supply and Use Tables

The experimental DSUTs of Mongolia follow the recommendations of the Organisation for Economic Co-operation and Development (OECD) framework on measuring the digital economy. Under this framework, digitalization is captured across three key dimensions: digital industries, digital products, and digital transactions. Due to data constraints, the current compilation focuses solely on digital industries and, within this category, is limited only to the digitally enabling industries. The remaining six digital industries (Table 1), as well as the dimensions of digital products and digital transactions, will be incorporated in future iterations of the tables as more detailed data becomes available.

The foundation for the construction of Mongolia's 2015–2019 experimental DSUTs are the conventional 2015–2019 Supply and Use Tables (SUTs). The methodology involves reallocating output, intermediate consumption, and gross value added (GVA) from existing SUT industry columns to a newly defined column representing digitally enabling industries. Reallocation ratios are derived using revenue data from the Statistical Business Register (SBR) of Mongolia.

Table 1: List of Digital Industries

<table><tr><td>1</td><td>Digitally enabling industries</td></tr><tr><td>2</td><td>Digital intermediation platforms charging a fee</td></tr><tr><td>3</td><td>Data- and advertising-driven digital platforms</td></tr><tr><td>4</td><td>Producers dependent on digital intermediation platforms</td></tr><tr><td>5</td><td>E-tailers</td></tr><tr><td>6</td><td>Financial service providers predominantly operating digitally</td></tr><tr><td>7</td><td>Other producers only operating digitally</td></tr></table>

Source: OECD. 2023. OECD Handbook on Compiling Digital Supply and Use Tables. OECD Publishing.

Digitally enabling industries comprise producers of goods and services that facilitate digital transformation, such as manufacturers of ICT equipment and providers of ICT services. Compared to other digital industries, this classification is based on the nature of production activities and not the “digital activity” generated. Digitally enabling industries correspond broadly to “ICT industries” as defined by the OECD. They include the manufacture of computers, electronics, and optical products; wholesale and repairs of ICT products; software publishing; telecommunications; and production of IT and information services (OECD 2023). A more detailed list of these ICT industries is provided in Table 2.

Table 2: Information and Communication Technology Industries

<table><tr><td>International Standard Industrial Classification Code</td><td>Description</td></tr><tr><td>2610</td><td>Manufacture of electronic components and boards</td></tr><tr><td>2620</td><td>Manufacture of computers and peripheral equipment</td></tr><tr><td>2630</td><td>Manufacture of communication equipment</td></tr><tr><td>2640</td><td>Manufacture of consumer electronics</td></tr><tr><td>2680</td><td>Manufacture of magnetic and optical media</td></tr><tr><td>4651</td><td>Wholesale of computers, computer peripheral equipment, and software</td></tr><tr><td>4652</td><td>Wholesale of electronic and telecommunications equipment and parts</td></tr><tr><td>5820</td><td>Software publishing</td></tr><tr><td>61</td><td>Telecommunications</td></tr><tr><td>62</td><td>Computer programming, consultancy, and related activities</td></tr><tr><td>6311</td><td>Data processing, hosting, and related activities</td></tr><tr><td>6312</td><td>Web portals</td></tr><tr><td>9511</td><td>Repair of computers and peripheral equipment</td></tr><tr><td>9512</td><td>Repair of communication equipment</td></tr></table>

Source: International Standard Industrial Classification of All Economic Activities (ISIC) Revision 4.

Some ICT industries exhibit a one-to-one correspondence with the industries already identified in Mongolia's SUTs, namely electronic components and board manufacturing, communication equipment manufacturing, electrical connection and computer programming, and consulting and related activities. The entire columns of these industries are reallocated to the digitally enabling industries column. Other ICT industries are only partially digital. Hence, the following industry codes were disaggregated to reallocate the output, intermediate consumption, and GVA of the digital subindustries into the “digitally enabling industry” column in the DSUT:

(a) 465—wholesale of machinery, equipment, and their accessories;

(b) 58—original preparation and publication activities;

(c) 63—information service activities; and

(d) 95—repair and service of goods for personal and household use, computers.

The following steps were undertaken to compile the DSUTs:

## Digital Supply Table

(a) Full reallocation of ICT industries with one-to-one correspondence to the digitally enabling industries column;

(b) Computation of output reallocation ratios using the revenue data from the SBR; and

(c) Disaggregation of partially digital ICT industries using the reallocation ratios and reallocation of the digital subindustries to the digitally enabling industries column.

## Digital Use Table

(b) Computation of GVA reallocation ratios using the revenue data from the SBR as proxy indicator(s);

(c) Derivation of the GVA for digital and non-digital subindustries;

(d) Residual estimation of intermediate consumption by subtracting the derived GVA from the derived gross output; and

(e) Distribution of intermediate consumption across product rows using the original SUT use structure, assuming similar production processes for digital and non-digital firms within the same industry.

## Challenges in the Compilation of the Digital Supply and Use Tables and Future Refinements

The primary challenge of compiling Mongolia's experimental DSUTs is the limited scope of the digital economy that can be captured given current data availability. While the OECD framework distinguishes seven digital industries and features three dimensions of digitalization, the present estimates are focused only on the digitally enabling industries. The reliance on SBR revenue data alone constrains the ability to compute reallocation ratios for other digital industries, such as e-tailers and digital intermediary platforms. Expanding coverage will require access to more granular and diverse data sources, including establishment lists, enterprise microdata, financial statements, annual reports, and e-commerce-specific surveys. Improved data integration would also enable future DSUT iterations to incorporate digital products and transactions, thereby providing a more comprehensive view of Mongolia's digital economy.

## PRELIMINARY AGGREGATE RESULTS

The experimental estimates indicate that Mongolia's digital economy exhibited strong growth during the period particularly between 2016 and 2019 (Figure 1). The growth of the digital GDP was higher than the non-digital GDP and overall economy in the years 2016 and 2019, likely reflecting the increased adoption of internet and mobile technologies in the country. The digital economy increased in absolute terms over the 5-year period despite a slowdown in its growth in 2017. This underscores the rising demand for digital technologies and products among households and businesses during this period.

Figure 2 illustrates the relative size of the digital economy as a share of Mongolia's economy-wide GDP, showing a gradual decline from $1.77\%$ in 2015 to $1.58\%$ in 2019. However, this trend should not be interpreted as a reduction in the economic significance of digital activities. On the contrary, digital GDP increased in absolute terms over the period, reflecting continued expansion of the digital sector.

Figure 1: Comparison of Digital Gross Domestic Product and Total Economy Gross Domestic Product Growth Rates, 2015–2019
(%)  
![](images/dc02f117496d30f29d71064828b16217cb1fe10b13385c6b0975fa5c57d245d9.jpg)  
GDP = gross domestic product.  
Source: Authors' calculations using National Statistics Office of Mongolia Supply and Use Tables and data from the Statistical Business Register.

Figure 3: Composition of the Digital Economy, 2015–2019 (% each component contributed to digital gross domestic product)  
Figure 2: Size of the Digital Economy of Mongolia, 2015–2019  
![](images/fa96c61324e0137239cab2ac98e413b4435dfa479c3d01b7bcdf717f51429241.jpg)  
GDP = gross domestic product, LCU = local currency unit.  
Source: Authors' calculations using National Statistics Office of Mongolia Supply and Use Tables and data from the Statistical Business Register.

The observed decline in the digital economy's share of GDP should therefore be interpreted with caution. The strong growth of overall GDP during 2015–2019 mechanically affects the relative weight of the digital economy, as total GDP serves as the denominator in computing its share. As the broader economy expands, particularly resource-based and traditional sectors, the proportional contribution of digital activities may appear smaller even when digital output is rising in absolute terms.

Additionally, the estimates are expressed in current prices and have not been adjusted for inflation. Given that the prices of digital products and services tend to decline over time due to rapid technological progress and productivity gains, current-price measures may understate real growth in the digital economy. The use of constant-price data will provide a more accurate assessment of real growth in the digital economy.

In examining the digital economy by sector, telecommunications consistently accounted for the largest share of digital GDP from 2015 to 2019 (Figure 3). This is followed by the providers of computer programming, consulting, and related services; then wholesalers of computers and peripheral equipment. The remaining digitally enabling industries made up only around 1.48% to 2.91% of total digital GDP during the given period. The fastest growing among all the digital sectors was computer programming, consulting, and related services, showing significant growth from 2018 onward. As this sector becomes a larger part of the economy today, the need to capture its full extent more accurately intensifies.

![](images/192189c05419e33e5d154c1089284a6f0c241538ff2fb68e92d3ebc0e91f180b.jpg)  
Source: Authors' calculations using National Statistics Office of Mongolia Supply and Use Tables and data from the Statistical Business Register.

## MEASURING MONGOLIA'S DIGITAL ECONOMY USING ADB'S INPUT-OUTPUT-BASED VALUE FLOW METHODOLOGY

While highly valuable for disaggregating a country's digital economy estimates, the development of DSUTs has extensive data requirements. ADB proposes an alternative approach to measuring the scale of the digital economy grounded in input-output framework analysis. This method measures both the direct and indirect value-added contributions of digital industries to economy-wide GDP. This input-output-based measurement framework, fundamentally rooted in Leontief's analytical insights (Leontief 1936), assesses the direct and indirect value-added contributions of identified digital industries to the production of final goods and services.

Under this framework, digital products are defined as goods and services primarily used to generate, process, or store digitized data. Industries that predominantly produce these products are classified as digital industries. Five “core” digital products/industries are identified: (i) hardware, (ii) software publishing, (iii) web publishing, (iv) telecommunications services, and (v) specialized and support services. Table 3 lays out the five “core” digital products/industries, including their subcomponents.

By focusing on these core components, the input–output-based value flow approach adopts a narrow scope to produce estimates of the digital economy, providing a solid basis for informed policymaking while avoiding the uncertainty associated with judging the degree of “digitalization” in products whose functions are only partly digital, such as conventional appliances with smart features.

Table 3: Main Digital Industries by International Standard Industrial Classification of All Economic Activities Revision 4 (ISIC Rev. 4)

<table><tr><td>Main Activity Group</td><td>Code</td><td>Industry</td></tr><tr><td rowspan="2">Hardware</td><td>2620</td><td>Manufacture of computers and peripheral equipment</td></tr><tr><td>2680</td><td>Manufacture of magnetic and optical media</td></tr><tr><td>Software publishing</td><td>5820</td><td>Software publishing</td></tr><tr><td>Web publishing</td><td>6312</td><td>Web portals</td></tr><tr><td>Telecommunication services</td><td>61</td><td>Telecommunication services</td></tr><tr><td rowspan="2">Specialized and support services</td><td>62</td><td>Computer programming services, consulting, and other related services</td></tr><tr><td>6311</td><td>Data processing, hosting, and related activities</td></tr></table>

Source: Special Supplement to 2021 ADB Key Indicators for Asia and the Pacific—Capturing the Digital Economy: A Proposed Measurement Framework and Its Applications.

The core-digital GDP equation used in this measurement framework is specified as follows:

$$
GDP_{digital} = \underbrace{i^{T}\hat{v}B\hat{y}\varepsilon_{1}}_{\text{Backward linkage}} + \underbrace{i^{T}(\hat{v}B\hat{y})^{T}\varepsilon_{1}}_{\text{Forward linkage}} - \underbrace{\left[\text{diag}(\hat{v}B\hat{y})\right]^{T}\varepsilon_{1}}_{\text{Double - counted term}} + \underbrace{(i - \varepsilon_{1})^{T}\hat{v}B\hat{y}\hat{r}\varepsilon_{2}}_{\substack{\text{Backward linkage to other fixed investments by digital sectors}}}
$$

where, $\hat{V}$ is the diagonalized vector of value-added to gross output ratios, B is the Leontief (1936) inverse, $\hat{y}$ is the diagonalized vector final demands, i is a summation vector, and $E_{1}$ and $E_{2}$ are the first eliminator vector, which excludes transactions related to non-digital industries, and the second eliminator vector, which excludes fixed assets in digital products.

The first term from this equation accounts for the backward linkages between the digital industries and the industries from which

[中间内容因长度限制已省略]

ctuations across the period, which could stem from episodic digital infrastructure upgrades and shifts in economic and policy conditions.

Table 4 shows the digital economy as a share of GDP for selected economies using the ADB measurement framework. The estimates show considerable variation across countries, reflecting differences in economic structure and the extent of digital integration. Mongolia's digital economy share is comparable to those of its Central Asian peers, including Georgia and Kazakhstan, while remaining below levels observed in more digitally advanced economies including Singapore, Malaysia, and Australia. This pattern is consistent with differing stages of digital development across the sample and underscores the usefulness of the ADB framework for producing consistent and comparable digital economy estimates across countries.

Table 4: Digital Economy as Percentage of Gross Domestic Product: Core Framework Estimates for Selected Economies

<table><tr><td rowspan="2">Economy</td><td colspan="2">Input-Output-Based Framework Estimates (Core)</td></tr><tr><td>Year</td><td>Percentage of Gross Domestic Product</td></tr><tr><td>Georgia</td><td>2018</td><td>2.5</td></tr><tr><td>Kazakhstan</td><td>2018</td><td>2.4</td></tr><tr><td>Indonesia</td><td>2016</td><td>2.9</td></tr><tr><td rowspan="2">Singapore</td><td>2016</td><td>6.8</td></tr><tr><td>2019</td><td>6.5</td></tr><tr><td rowspan="2">Malaysia</td><td>2015</td><td>7.6</td></tr><tr><td>2020</td><td>8.7</td></tr><tr><td rowspan="2">Australia</td><td>2018</td><td>5.0</td></tr><tr><td>2021</td><td>5.3</td></tr></table>

Source: ADB estimates.

## CONCLUSION AND RECOMMENDATIONS

The compilation of the experimental DSUTs for 2015–2019 marks a significant milestone for the statistical system of Mongolia. This statistical framework facilitates a fuller understanding of the state, evolution, and impact of economic digitalization. Although the experimental DSUTs are limited to digitally enabling industries, they provide valuable initial evidence on the scale and growth dynamics of digital activities in the country. Addressing existing data gaps will be essential for expanding coverage to other digital industries and dimensions of digitalization. Strengthening administrative and survey data, enhancing the SBR, and integrating alternative data sources will support more accurate estimates. ADB's input-output-based framework offers a useful complementary perspective and can serve as a validation tool for DSUT-based results. Continued collaboration between ADB and the National Statistics Office of Mongolia, combined with sustained investment in statistical capacity building, will be critical for advancing digital economy measurement in Mongolia. Improved statistics will help policymakers design evidence-based strategies to harness digitalization as a driver of inclusive and sustainable economic growth.

## REFERENCES

ADB. 2021. Capturing the Digital Economy: A Proposed Measurement Framework and Its Applications—A Special Supplement to Key Indicators for Asia and the Pacific 2021. http://dx.doi.org/10.22617/FLS210307-3.

Government of Mongolia, Ministry of Digital Development, Innovation, and Communications. n.d. Strategic Goals. (In Mongolian.) https://mddic.gov.mn/mn/strategic-goals/.

OECD. 2023. OECD Handbook on Compiling Digital Supply and Use Tables. OECD Publishing. https://doi.org/10.1787/11a0db02-en.

United Nations Trade and Development. 2023. Mongolia Eyes E-Commerce to Diversify Its Economy. 8 June. https://unctad.org/news/mongolia-eyes-e-commerce-diversify-its-economy.

W. Leontief. 1936. Quantitative Input and Output Relations in the Economic System of the United States. Review of Economics and Statistics. 18.

## About the Asian Development Bank

ADB is a leading multilateral development bank supporting inclusive, resilient, and sustainable growth across Asia and the Pacific. Working with its members and partners to solve complex challenges together, ADB harnesses innovative financial tools and strategic partnerships to transform lives, build quality infrastructure, and safeguard our planet. Founded in 1966, ADB is owned by 69 members—50 from the region.

ADB Briefs are based on papers or notes prepared by ADB staff and their resource persons. The series is designed to provide concise, nontechnical accounts of policy issues of topical interest, with a view to facilitating informed debate. The Department of Communications and Knowledge Management administers the series.

www.adb.org/publications/series/adb-briefs

The views expressed in this publication are those of the authors and do not necessarily reflect the views and policies of ADB or its Board of Governors or the governments they represent. ADB does not guarantee the accuracy of the data included here and accepts no responsibility for any consequence of their use. The mention of specific companies or products of manufacturers does not imply that they are endorsed or recommended by ADB in preference to others of a similar nature that are not mentioned. By making any designation of or reference to a particular territory or geographic area in this document, ADB does not intend to make any judgments as to the legal or other status of any territory or area.

Asian Development Bank
6 ADB Avenue, Mandaluyong City
1550 Metro Manila, Philippines
www.adb.org

![](images/165016175763dfdfa8c3745aa64967399769cb2e3405230e670fe1377eeb072c.jpg)

## Creative Commons Attribution 3.0 IGO license (CC BY 3.0 IGO)

© 2026 ADB. The CC license does not apply to non-ADB copyright materials in this publication.
https://www.adb.org/terms-use#openaccess http://www.adb.org/publications/corrigenda pubsmarketing@adb.org
"""
