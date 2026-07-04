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
Policy Research Working Paper

11072

# Revisiting the Gains from Trade in EMDEs

The Case of Selected East Asian and East African Economies

Enkhmaa Battogtvor

Socrates Kraido Majune

Angella Faith Montfaucon

POLICY RESEARCH WORKING PAPER 11072

## Abstract

Following the gains from variety literature, this paper estimates the welfare impact of growth of the variety of imported goods in 28 countries in East Africa and East Asia and compares the results. While estimating the gains from variety, the elasticities of substitution are estimated for each country at the Harmonized System six-digit level of disaggregation. More than 100,000 elasticities are estimated, and the paper constructs an exact price index to measure the welfare gains from variety growth. The findings show that from 1995 to 2021, African countries gained on average 5.47 percent of their gross domestic product (0.20 percent annually), and Asian countries excluding Bhutan gained 3.46 percent (0.13 percent annually). Bhutan, Mongolia, Rwanda, and Mozambique are among the countries with the highest gains over the sample period. The evidence indicates that the creation and extension of trade linkages can be a source of welfare, particularly for small and transitioning economies, a point that is occasionally overlooked in discussions about the positive effects of globalization and economic integration. The estimated elasticities may also be useful for other studies.

# Revisiting the Gains from Trade in EMDEs: The Case of Selected East Asian and East African Economies\*

Enkhmaa Battogtvor, $^{\dagger}$ , Socrates Kraido Majune; and Angella Faith Montfaucon $^{\S}$

JEL Classification : F18, D22, Q56

Keywords: Gains from trade, Gains from variety, Elasticity of substitution, Welfare effect of trade liberalization, Economic integration

## 1 Introduction

In the core of the monopolistic competition model with differentiated goods pioneered by Dixit and Stiglitz (1977), consumers benefit from having more varieties of final goods. These benefits stem from lower unit costs of imports and these lower costs are the source of the welfare gains. However, most studies focus on the conventional sources of gains from trade, such as productivity improvement due to increasing returns to scale, trade-induced innovation, technology spillover, and improved market efficiency because of import competition (Chen and Ma, 2012). These studies often assume a constant set of products over time, and this leads to systematically understated welfare gain calculations.

This paper estimates the comprehensive gains from import variety in emerging markets and developing economies (EMDEs), particularly for each of 28 Asian (including one Pacific Island nation) and East African economies during 1995-2021, following the seminal works by Feenstra (1994) and Broda and Weinstein (2006). The gains from variety for the economies were estimated, using six-digit harmonized system (HS) product data. We estimated more than 100,000 elasticities in total and with the elasticities, we constructed an exact price index to measure the welfare gains from variety growth. This method is consistent with the theory of monopolistic competition and is robust in empirical applications (Feenstra, 1994), from which the quantitative analysis of gains from variety started.

Feenstra (1994) showed how to estimate the elasticity of substitution of individual products, and using these elasticities he offered the formula for an exact price index that can account for entry and exit of varieties. By doing so, Feenstra (1994) demonstrated that new product varieties lead to an increase in consumer utility. However, a comprehensive measure of the gains from import variety puts tremendous demands on data availability and was not realized until Broda and Weinstein (2006).

Applying Feenstra's estimation technique, Broda and Weinstein (2006) estimated the welfare gain that the United States enjoyed through trade liberalization over 30 years by computing the elasticities of substitutions of more than 30,000 products. Using the elasticities, they created the import price index adjusted for new and disappearing varieties and measured the value that consumers attached to these new product varieties. They found that the total gain from the introduction of new varieties in the United States was 2.6 percent of GDP between 1972 and 2001. This meant that to obtain the new set of varieties imported each year, consumers would be ready to pay on average 0.1 percent of their income.

Following Broda and Weinstein (2006), a body of country studies emerged, using the same methodology. $^{1}$ For instance, Chen and Ma (2012) found that the welfare gain in the Chinese economy as a result of new import variety amounts to 4.9 percent of GDP, or 0.4 percent annually between 1997 and 2008. Minondo and Requena (2010) investigated the welfare gains due to Spanish imports of new varieties over the period 1988-2006. They found that the total welfare gain is equal to 1.2 percent of GDP in 2006. In a comparative study of Switzerland and the United States, Mohler (2009) estimated a lower and an upper bound of the gains from variety. He found that during the period from 1990 to 2006, the gains from variety in Switzerland were between 0.3 and 4.98 percent of GDP and that in the United States the gains from variety were between 0.5 and 4.7 percent of GDP.

Mohler and Seitz (2012) applied the methodology to the 27 countries of the European Union for the period 1999 to 2008. Their results show that within the European Union, especially “newer” and smaller member states exhibit high gains from newly imported varieties. For instance, Estonia gained 2.80 percent of GDP (GDP of Estonia); the Slovak Republic, 2.37 percent; Latvia, 1.65 percent; and Bulgaria, 1.59 percent. They also found that interestingly, two of the largest economies in the group, France and Germany, both had negative gains from variety. They argue that the reason for this is that these larger economies were already heavily integrated in the European economy and therefore did not experience the increase in product varieties as did the “new”, smaller economies.

Our analysis of 4,537 elasticities of substitution across 28 countries reveals that the average elasticity is 13.0, while the median is 4.1. A lower elasticity indicates that goods are highly differentiated, suggesting a significant potential for gains from variety. The median lambda ratio for countries indicates significant variety growth in imported products. The average welfare gain owing to newly imported varieties from 1995 to 2021 amounts to 5.49 percent of GDP, or 0.20 percent annually. This average distorts significant heterogeneity among countries. African countries gained on average 5.47 percent of their GDP, however Asian countries excluding Bhutan gained less from import variety by 3.46 percent. Nevertheless, this is a significant result considering the moderate annual gains of 0.1 per cent (Broda and Weinstein, 2006) to 0.4 percent (Chen and Ma, 2012).

The evidence indicates that the creation and extension of trade linkages can be a source of welfare, particularly for small and transitioning economies, a point occasionally overlooked in discussions about the positive effects of globalization and economic integration. Gains from increased import varieties are not limited to consumers. Access to more imported varieties may enhance productivity growth, leading domestic firms to gain substantially. In fact, with the widely used constant elasticity of substitution (CES) structure, new varieties could be modeled either as consumption goods or as intermediate inputs (Romer, 1994). While we follow Broda and Weinstein (2006) and treat all imported goods as intended for final consumption, future research could expand on this work in this direction as well as potential losses such as fiscal costs (revenue losses) for specific groups and related policies to mitigate such costs.

We contribute to the growing literature by providing measures of East Asian and East African countries' welfare gain due to import variety from 1995 to 2021. To our knowledge, this is the first study that pursues these measures for the selected countries, thus we have two motivations in mind. First, as small open economies, most of the countries underwent significant trade liberalization after their accession to World Trade Organization (WTO). Thus, measuring their gains from import varieties provides supporting evidence favoring trade liberalization for developing countries. It may also provide informative implications to the countries' policymakers. Second, we obtain estimates for thousands of elasticities of substitution using highly disaggregated import data, which may be useful for other studies. For example, different elasticities may imply different responsiveness of imported products to demand shocks or exchange rate movements suggested by Chen and Ma (2012).

The rest of the paper is organized as follows. Section 2 describes the data and reviews import growth from 1995 to 2021. Section 3 reviews Broda and Weinstein's (2006) model. Section 4 explains the estimation strategy and gives a brief overview of the importance of elasticities of substitution. Section 5 reports the results of the analysis and presents the welfare gain. Section 6 concludes the study.

## 2 Data and Descriptive Analysis

We used trade data from BACI (Gaulier and Zignago, 2010). $^{2}$ We used the import data of the selected countries from 1995 to 2021, covering 27 continuous years. The data contains information on the total values, quantities, and exporters of registered products to the countries. Unspecified country data and products with data on their quantities are dropped. Furthermore, due to the insufficient numbers of observations, HS-6 products with fewer than 26 observations are dropped in the sample. This is due to the problem that many products were not imported to the countries constantly throughout the period. This left us with more than 40 million observations of 5,383 products. $^{3}$ Gross domestic product (GDP) data were taken from the World Bank's World Development Indicators (WDI) Database.

To study the welfare implications of the drastic increase in imports of the countries, we should consider the increase in value of each product (i.e., the intensive margin) and the increase in the number of products and varieties for each product (i.e., the extensive margin).

Figure 1 shows average annual imports as shares of GDP between 1995 and 2021. The imports share of GDP greatly varies among the countries. For instance, Japan has an import share as low as 11% on average and Hong Kong SAR, China, has the highest share of imports in its GDP of 163%. The rest of the countries, during the 27 years on average, spend 35% of their GDP for the imported products. No matter what the annual imports-to-GDP ratio for an individual country is, the data shows a general upward trend, suggesting that international trade increased for the selected EMDEs.

![](images/5db66b723c7b543f98fc1ccc3c89bf1d2f56ad72d054a5b3451537ffc1e3b5e0.jpg)  
Figure 1: Average annual imports 1995-2021 (% of GDP)  
Source: Authors' calculation based on United Nations Comtrade - International Trade Statistics database

Table 1 summarizes the count measure of imported varieties of the selected 28 countries in 1995 and 2021. The definition of variety used in this paper is same as the variety defined in Broda and Weinstein (2006), which is an Armington (1969) definition of a product variety. By this definition, a variety is a particular good produced in a particular country. To be more specific, a product in this paper is defined as a six-digit Harmonized System (HS) good. To give an example, in Mongolia a sparkling wine (with HS-6 product code 220410) was imported from only one country, Germany, in 1989. In contrast, the same wine was imported from 13 different countries, such as France, Spain, Italy and Chile, in 2015. This represents an increase from a single variety to 13 different varieties. Therefore, by the Armington (1969) assumption, an HS-6 product supplied by one country is regarded as different from the same product supplied by any other country.

The data reveals that behind the rapid growth in import value, the growth in import varieties is similarly dramatic. Columns (1) and (4) of Table 1 report the number of HS-6 products for the years 1995 and 2021 respectively. We can see that the number of HS-6 products increased by almost a factor of 3 in Bhutan during the period, growing from 519 in 1995 to 1,537 in 2021. Similarly imported HS-6 products more than doubled in Rwanda and almost doubled in Cambodia, Mongolia, and Mozambique. On average, the number of imported products increased by $31\%$ for the sample countries. Moreover, columns (3) and (6) show the total number of imported product varieties in 1995 and 2021 respectively, which can be calculated as the number of HS-6 products multiplied by the average variety in columns (2) and (5) respectively.

Comparing columns (3) and (6), we can see that the total number of varieties increased more than 10 times in Rwanda, 8 times in Mongolia, 7 times in Cambodia, 6 times in Mozambique, 5 times in Bhutan, and 4 times in Brunei, Kenya, the Lao People's Democratic Republic and Viet Nam. The total number of varieties grew 3.5 times from 1995 to 2021 for an average country of the sample. However, we can say that African countries on average show more increase in their total import varieties with 3.65 times growth compared to 3.37 times for the average of Asian countries. Columns (2) and (5) show the average number of exporting countries, i.e., the number of varieties in 1995 and 2021 respectively. We can observe that the number of exporting countries increased over time in all 28 countries. For example in China, 16 varieties or source countries were available per good in 1995, but in

2021 on average 33 varieties were available. These dramatic changes in goods and varieties suggest that conventional measures using a fixed basket of goods or varieties could be largely biased. Consequently, these facts demonstrate that the gains from variety are not negligible.

Table 1: Variety in Imports (1995-2021)

<table><tr><td rowspan="3"></td><td rowspan="3">Country</td><td colspan="3">1995</td><td colspan="3">2021</td></tr><tr><td>Number of HS-6 products</td><td>Average number of varieties</td><td>Total number of varieties</td><td>Number of HS-6 products</td><td>Average number of varieties</td><td>Total number of varieties</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td></tr><tr><td>1</td><td>Bhutan</td><td>519</td><td>1.7</td><td>883</td><td>1537</td><td>3.4</td><td>5152</td></tr><tr><td>2</td><td>Brunei Darussalam</td><td>3373</td><td>3.1</td><td>10505</td><td>4075</td><td>10.8</td><td>43892</td></tr><tr><td>3</td><td>Cambodia</td><td>2446</td><td>2.6</td><td>6299</td><td>4270</td><td>10.5</td><td>44776</td></tr><tr><td>4</td><td>China</td><td>5198</td><td>16.0</td><td>83360</td><td>5349</td><td>33.7</td><td>180519</td></tr><tr><td>5</td><td>Congo, Rep.</td><td>2880</td><td>3.9</td><td>11324</td><td>3703</td><td>10.1</td><td>37354</td></tr><tr><td>6</td><td>Fiji</td><td>3243</td><td>2.7</td><td>8917</td><td>4003</td><td>7.6</td><td>30372</td></tr><tr><td>7</td><td>Hong Kong SAR, China</td><td>5165</td><td>15.7</td><td>81260</td><td>5262</td><td>22.3</td><td>117246</td></tr><tr><td>8</td><td>Indonesia</td><td>5110</td><td>12.8</td><td>65576</td><td>5284</td><td>22.1</td><td>116905</td></tr><tr><td>9</td><td>Japan</td><td>5240</td><td>19.0</td><td>99689</td><td>5342</td><td>25.0</td><td>133629</td></tr><tr><td>10</td><td>Kenya</td><td>3940</td><td>4.7</td><td>18371</td><td>4786</td><td>16.5</td><td>78886</td></tr><tr><td>11</td><td>KoreaRep</td><td>5197</td><td>14.2</td><td>73880</td><td>5332</td><td>29.4</td><td>156867</td></tr><tr><td>12</td><td>Lao PDR</td><td>2357</td><td>2.1</td><td>5016</td><td>3369</td><td>6.5</td><td>21963</td></tr><tr><td colspan="2"></td><td colspan="3">1995</td><td colspan="3">2021</td></tr><tr><td>13</td><td>Macao SAR, China</td><td>3521</td><td>5.8</td><td>20446</td><td>3561</td><td>12.1</td><td>43042</td></tr><tr><td>14</td><td>Malawi</td><td>3023</td><td>3.8</td><td>11527</td><td>3583</td><td>4.3</td><td>15458</td></tr><tr><td>15</td><td>Malaysia</td><td>5143</td><td>12.8</td><td>65902</td><td>5292</td><td>21.5</td><td>113892</td></tr><tr><td>16</td><td>Mauritius</td><td>4369</td><td>7.6</td><td>33026</td><td>4652</td><td>13.7</td><td>63552</td></tr><tr><td>17</td><td>Mongolia</td><td>2074</td><td>2.5</td><td>5226</td><td>3639</td><td>12.3</td><td>44783</td></tr><tr><td>18</td><td>Mozambique</td><td>2442</td><td>3.2</td><td>7786</td><td>4408</td><td>11.1</td><td>48770</td></tr><tr><td>19</td><td>Myanmar</td><td>3313</td><td>3.2</td><td>10629</td><td>4395</td><td>8.9</td><td>39076</td></tr><tr><td>20</td><td>Philippines</td><td>4851</td><td>7.3</td><td>35177</td><td>5173</td><td>19.3</td><td>99606</td></tr><tr><td>21</td><td>Rwanda</td><td>1608</td><td>2.4</td><td>3876</td><td>3731</td><td>11.3</td><td>42112</td></tr><tr><td>22</td><td>Singapore</td><td>5150</td><td>16.5</td><td>84864</td><td>5247</td><td>27.9</td><td>146637</td></tr><tr><td>23</td><td>Tanzania</td><td>3801</td><td>6.7</td><td>25641</td><td>4609</td><td>14.8</td><td>68335</td></tr><tr><td>24</td><td>Thailand</td><td>5122</td><td>14.4</td><td>73973</td><td>5305</td><td>26.4</td><td>140160</td></tr><tr><td>25</td><td>Uganda</td><td>3523</td><td>5.8</td><td>20590</td><td>4062</td><td>7.3</td><td>29806</td></tr><tr><td>26</td><td>Viet Nam</td><td>4332</td><td>5.3</td><td>23033</td><td>5189</td><td>19.3</td><td>100091</td></tr><tr><td>27</td><td>Zambia</td><td>3656</td><td>4.5</td><td>16422</td><td>4409</td><td>10.4</td><td>45827</td></tr><tr><td>28</td><td>Zimbabwe</td><td>3982</td><td>6.0</td><td>23881</td><td>4438</td><td>8.6</td><td>37991</td></tr></table>

Source: Authors' calculation

## 3 Methodology: The Broda and Weinstein Method

Following Feenstra (1994) and Broda and Weinstein (2006), we start by deriving an exact price index for a constant elasticity of substitution (CES) utility function of a single good with a constant number of varieties. This index is then extended by allowing for new and disappearing varieties. Finally, we show how to construct an aggregate import price index and gains from variety formula. Let us start with a simple CES utility function with the following functional form for a single imported good. Assume that varieties of a good g are treated 

[中间内容因长度限制已省略]

import share of the United States to be 6.7 percent for 1972-1988 and 10.3 percent for 1990-2001, respectively and Chen and Ma (2012) found the log-change ideal weight of China's imports in GDP to be 11.5 percent during 1997-2008.

Since we used the share of imports in GDP as a weight $w_{t}^{M}$ in equation 13, and most gaining countries' import share of GDP is relatively high, as a result the variety gain is consequently high.

Second and the main reason is that not only growth in number of varieties was drastic, but also growth in the number of products was significant in these countries. Columns (1) and (2) of Table 7 show the percentage increase in number of products and number of varieties from 1995 to 2021. For example, in Bhutan the number of varieties increased 97%, from 1.7 to 3.4 $^{12}$ , and on the other hand, the number of products increased 196%, from 519 to 1537 $^{13}$ . This means that the numerator of the lambda ratios, $\lambda_{gt}$ , which captures the impact of newly available varieties is low. Since $\lambda_{gt}$ is the ratio of expenditures on varieties available in both periods (i.e., $c \in I_g = (I_{gt} \cap I_{g-1})$ ) relative to the entire set of varieties available in period t (i.e., $c \in I_{gt}$ ), evolving of the new variety decreases $\lambda_{gt}$ . Hence, the exact price index is relatively low, and the welfare gain is relatively high. We can see from Table 7 that Bhutan, Mongolia, Rwanda, and Mozambique are the countries with the highest increases in both number of products and number of varieties. Compared to these countries China; Hong Kong SAR, China; Japan; and the Republic of Korea have moderate increase in their number of products during the period.

## 6 Conclusion

There is a considerable amount of literature attempting to quantify the welfare gain from growing import variety. Thus, the importance of importing new varieties has been long-established. Moreover, the literature confirms that gains from trade varieties are in general much higher in developing countries than in developed countries. In our study, we looked at 17 Asian countries, 10 East African countries (mostly EMDEs), and Fiji. Compared to their size, the economies import a great deal, spending on average 41 percent of the total expenditure in a year from 1995 to 2021. At the same time, these economies have been gaining greatly from international trade. However, no comprehensive study exists on how much they have gained from import variety growth.

We use highly disaggregated import data from 1995 to 2021 to estimate the elasticities of substitution for 4,537 imported goods on average for all 28 countries. These elasticities allow us to construct a comprehensive measure of the welfare gain using the seminal works by Feenstra (1994) and Broda and Weinstein (2006). The welfare gain as a result of growth in import variety during the period amounts to an average of 5.49% of GDP. We found that African countries on average gained more than Asian countries excluding Bhutan during the period. This indeed confirms the finding in the literature that the welfare impact of import variety growth is greater in developing countries.

The evidence from this paper indicates that for small and transitioning economies, the establishment and expansion of trade linkages can be a significant source of welfare. This aspect is often overlooked in discussions about the effects of globalization and economic integration.

## References

Armington, P. S. (1969). A theory of demand for products distinguished by place of production (une théorie de la demande de produits différenciés d'après leur origine)(una teoría de la demanda de productos distinguiéndolos según el lugar de producción). Staff Papers-International Monetary Fund, pages 159–178.

Broda, C. and Weinstein, D. (2004). Globalization and the gains from variety. Technical report, Federal Reserve Bank of New York.

Broda, C. and Weinstein, D. E. (2006). Globalization and the gains from variety. The Quarterly journal of economics, 121(2):541–585.

Chen, B. and Ma, H. (2012). Import variety and welfare gain in china. Review of International Economics, 20(4):807–820.

Diewert, W. E. (1976). Exact and superlative index numbers. Journal of econometrics, 4(2):115–145.

Dixit, A. K. and Stiglitz, J. E. (1977). Monopolistic competition and optimum product diversity. The American economic review, 67(3):297–308.

Feenstra, R. C. (1994). New product varieties and the measurement of international prices. The American Economic Review, pages 157–177.

Gaulier, G. and Zignago, S. (2010). Baci: international trade database at the product-level (the 1994-2007 version).

Hansen, L. P. (1982). Large sample properties of generalized method of moments estimators. Econometrica: Journal of the econometric society, pages 1029–1054.

Krugman, P. et al. (1980). Scale economies, product differentiation, and the pattern of trade. American economic review, 70(5):950–959.

Minondo, A. and Requena, F. (2010). Welfare gains from imported varieties in spain, 1988-2006. Institu-to Valenciano de Investigaciones Económicas SA (Ivie).

Mohler, L. (2009). Globalization and the gains from variety: size and openness of countries and the extensive margin.

Mohler, L. and Seitz, M. (2012). The gains from variety in the european union. Review of World Economics, 148:475–500.

Romer, P. (1994). New goods, old theory, and the welfare costs of trade restrictions. Journal of development Economics, 43(1):5–38.

Sato, K. (1976). The ideal log-change index number. The Review of Economics and Statistics, pages 223–228.

Vartia, Y. O. (1976). Ideal log-change index numbers. scandinavian Journal of statistics, pages 121–126.
"""
