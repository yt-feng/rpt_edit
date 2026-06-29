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
- 已识别机构名：`麦肯锡`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份麦肯锡研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# The state of AI in 2025

Agents, innovation, and transformation

November 2025

![](images/fe4887c16d2810744b223b8db4666d722b8f4097b8ee4eb454f400850d373ace.jpg)

![](images/1e9d9b0ed7eda273eba8387e36dc15b26c3ca0c58183ae352db2ab37251afa92.jpg)

# Almost all survey respondents say their organizations are using AI, and many have begun to use AI agents. But most are still in the early stages of scaling AI and capturing enterprise-level value.

This article is a collaborative effort by Alex Singla, Alexander Sukharevsky, Lareina Yee, and Michael Chui, with Bryce Hall and Tara Balakrishnan, representing views from QuantumBlack, AI by McKinsey.

![](images/141f59898df2bfea1468933f22a89a5a75ecc870ea8ae9bb62bd41674f917f4a.jpg)

## Key findings

1. Most organizations are still in the experimentation or piloting phase: Nearly two-thirds of respondents say their organizations have not yet begun scaling AI across the enterprise.

2. High curiosity in AI agents: Sixty-two percent of survey respondents say their organizations are at least experimenting with AI agents.

3. Positive leading indicators on impact of AI: Respondents report use-case level cost and revenue benefits, and 64 percent say that AI is enabling their innovation. However, just 39 percent report EBIT impact at the enterprise level.

4. High performers use AI to drive growth, innovation, and cost: Eighty percent of respondents say their companies set efficiency as an objective of their AI initiatives, but the companies seeing the most value from AI often set growth or innovation as additional objectives.

5. Redesigning workflows is a key success factor: Half of those AI high performers intend to use AI to transform their businesses, and most are redesigning workflows.

6. Differing perspectives on employment impact: Respondents vary in their expectations of AI's impact on the overall workforce size of their organizations in the coming year: 32 percent expect decreases, 43 percent no change, and 13 percent increases.

Three years since the introduction of gen AI tools triggered a new era of artificial intelligence, nearly nine out of ten survey respondents say their organizations are regularly using AI—but the pace of progress remains uneven. While AI tools are now commonplace,

most organizations have not yet embedded them deeply enough into their workflows and processes to realize material enterprise-level benefits. The latest McKinsey Global Survey on the state of AI reveals a landscape defined by both wider use—including growing proliferation of agentic AI—and stubborn growing pains, with the transition from pilots to scaled impact remaining a work in progress at most organizations.

Use of AI by respondents' organizations, % of respondents

# AI use continues to broaden but remains primarily in pilot phases

Our latest survey shows a larger share of respondents reporting AI use by their organizations, though most have yet to scale the technologies. The share of respondents saying their organizations are using AI in at least one business function has increased since our research last year: 88 percent report regular AI use in at least one business function, compared with 78 percent a year ago. But at the enterprise level, the majority are still in the experimenting or piloting stages (Exhibit 1), with approximately one-third reporting that their companies have begun to scale their AI programs.

## Exhibit 1

Reported use of AI in at least one business function continues to increase.

![](images/441b17e7e080c0b0de42db7d5f884881f260bcb53fb2de755282b2f84f927715.jpg)  
Phase of AI use among organizations using AI in 2025

![](images/f7c0f72551df6fcdadbba8df0c64132a16b7a05ff2f8a581d54b5ee8b360d2da.jpg)  
$^{1}$ In 2017, the definition for AI use was using AI in a core part of the organization's business or at scale. In 2018–19, the definition was embedding at least 1 AI capability in business processes or products. From 2020, the definition was that the organization has adopted AI in at least 1 function, and in 2025, the definition was regular use of AI in at least 1 function.

Source: McKinsey Global Surveys on the state of AI, 2017–25

## Many organizations are already experimenting with AI agents

Organizations are also beginning to explore opportunities with AI agents—systems based on foundation models capable of acting in the real world, planning and executing multiple steps in a workflow. Twenty-three percent of respondents report their organizations are scaling an agentic AI system somewhere in their enterprises (that is, expanding the deployment and adoption of the technology within a least one business function), and an additional 39 percent say they have begun experimenting with AI agents. But use of agents is not yet widespread: Most of those who are scaling agents say they’re only doing so in one or two functions. In any given business function, no more than 10 percent of respondents say their organizations are scaling AI agents (Exhibit 2).

Exhibit 2

No more than 10 percent of respondents report scaling AI agents in any individual function.

Phase of AI agent use at respondents' organizations, by business function, $^{1}$ % of respondents (n = 1,933)

![](images/f17e987bc266f806f34e25b8fe9e1f74817c94c59ed475974a2de40ee393ffb3.jpg)  
Note: Figures may not sum to 100%, because of rounding. $^{1}$ Question was asked only of respondents who reported regular use of AI in the respective functions and was rebased to reflect the total sample. Source: McKinsey Global Survey on the state of AI, 1,993 participants at all levels of the organization, June 25–July 29, 2025

McKinsey & Company

Looking at individual business functions, agent use is most commonly reported in IT and knowledge management, where agentic use cases such as service-desk management in IT and deep research in knowledge management have quickly developed. By industry, the use of AI agents is most widely reported in the technology, media and telecommunications, and healthcare sectors (Exhibit 3).

Exhibit 3

Use of AI agents is most often reported by respondents working in technology, media and telecommunications, and healthcare.

AI agent use that has reached the scaling phase, $^{1}$ by industry and business function, % of respondents

$$
\begin{array}{c|c|c|c|c|c|c|c:c:cccccc} & & \text {Technology} & & \text {Media and telecom} & & \text {Healthcare} & & \text {Insurance} & & \text {Advanced manufacturing} & & \text {Professional services} & & \text {Pharma and medical products} & & \text {Engineering and construction} & & \text {Financial institutions} & & \text {Consumer goods and retail} \\ \hline \text {Total} & 9 & 22 & 12 & 13 & 15 & 10 & 9 & 6 & 6 & 8 & 6 & 3 & 7 \\ \hline \text {IT} & 8 & 12 & 7 & 14 & 16 & 6 & 5 & 2 & 6 & 6 & 4 & 4 & 6 \\ \text {Knowledge management} & 7 & 16 & 10 & 6 & 20 & 8 & 5 & 6 & 8 & 5 & 4 & 4 & 7 \\ \text {Marketing and sales} & 7 & 21 & 16 & 6 & 2 & 7 & 3 & 6 & 3 & 1 & 3 & 5 & 1 \\ \text {Service operations} & 7 & 18 & 3 & 7 & 2 & 6 & 6 & 4 & 6 & 11 & 6 & 3 & 3 \\ \text {Product and/ or service development} & 7 & 24 & 6 & 1 & 0 & 7 & 0 & 3 & 4 & 2 & 2 & 3 & 1 \\ \text {Software engineering} & 5 & 9 & 8 & 6 & 16 & 4 & 0 & 3 & 5 & 1 & 0 & 7 & 3 \\ \text {Risk, legal, and compliance} & 4 & 6 & 5 & 5 & 0 & 3 & 4 & 5 & 6 & 1 & 4 & 4 & 3 \\ \text {Strategy and corporate finance} & 4 & 9 & 7 & 2 & 1 & 5 & 1 & 4 & 0 & 2 & 4 & 4 & 1 \\ \text {Human resources} & 2 & 4 & 1 & 3 & 1 & 2 & 3 & 1 & 2 & 4 & 0 & 0 & 3 \\ \text {Supply chain/ inventory management} & 2 & 2 & -1 & -4 & -0.5 | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| \(\begin{array}c|cc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|ccccc|\end{array}\)
$$

$^{1}$ Includes respondents who answered “scaling” and “fully scaled.” Question was asked only of respondents who reported regular use of AI in the respective functions and was rebased to reflect the total sample. In technology, n = 237; insurance, n = 80; healthcare, n = 129; media and telecommunications, n = 93; energy and materials, n = 141; advanced manufacturing (includes advanced electronics, aerospace, automotive and assembly, and semiconductors), n = 118; professional services (includes legal services, management consulting, market research, and product research), n = 259; consumer goods and retail, n = 116; travel, logistics, and infrastructure, n = 75; engineering, construction, and building materials, n = 77; banking and other financial institutions, n = 153; pharmaceuticals and medical products, n = 78. Source: McKinsey Global Survey on the state of AI, 1,993 participants at all levels of the organization, June 25–July 29, 2025

McKinsey & Company

![](images/16d39984c8045d1fa8804f206430940a5b816f24624a1a64f40cc93c9d9ff89d.jpg)

## McKinsey commentary Michael Chui Senior fellow

AI agents have been the subject of intense buzz and excitement. Already, about a quarter of our survey respondents report that they have started scaling at least one agentic AI system, but usually only in one or two business functions. Looking across the entire enterprise landscape, the use of agents is not yet widespread. This gap highlights the contrast between the great potential that manifests in a “hype cycle” and the current reality on the ground: For those companies that respondents say have started to use agents in any particular business function, most of them are still in the exploratory stages. And as we recently documented in another article about the lessons we’ve learned from a year of building agentic AI tools: When it comes to agents, it takes hard work to do it well.

## Twenty-three percent of respondents report their organizations are scaling an agentic AI system somewhere in their enterprises.

![](images/63757a7e9157c7575f1e80e46f21fca835f6edda66ffa0a5c459c64d2d936f00.jpg)

Exhibit 4

## For most organizations, AI use remains in pilot phases

The use of AI overall is broadening within organizations. Respondents increasingly report that their organizations are using AI in more business functions (Exhibit 4). More than two-thirds of respondents now say their organizations are using AI in more than one function, and half report using AI in three or more functions (for a breakdown by industry, see sidebar, “Reported AI use ticks upward in nearly every industry”).

Organizations are increasingly using AI in multiple functions.

Business functions at respondents' organizations that are using AI, $^{1}$ % of respondents  
![](images/82362ca1dfaa479f5dfd72a560fe136022a08b1f2cb2ea24019ed16263f3b28f.jpg)  
In 2021, n = 1,843; in 2022, n = 1,492; in 2023, n = 1,684; in Feb–Mar 2024, n = 1,363; in July 2024, n = 1,491; in June–July 2025, n = 1,993. The survey question asks about 11 functions: HR; IT; manufacturing: marketing and sales; product and/or service development; risk, legal, and compliance; service operations; software engineering; strategy and corporate finance; supply chain/inventory management; and knowledge management.

McKinsey Global Surveys on the state of AI, 2021–25

McKinsey & Company

## Sidebar

## Reported AI use ticks upward in nearly every industry

In every industry besides the technology sector (which had already exceeded 90 percent reporting AI use), the share of respondents saying that their organization is regularly using AI in at least one business function has meaningfully increased since our previous survey. In last year's research, respondents working for technology

companies reported being ahead of other industries with respect to their use of AI. Now, respondents in media and telecommunications and insurance are just as likely as those in technology to report AI use (exhibit). Throughout eight years of AI research, we have consistently seen IT and marketing and sales as the business functions that respondents most often say are using AI. But our latest findings show that knowledge management is now also one of the functions with the most reported AI use.

Looking at individual use cases within business functions, respondents most often report using AI to capture information as well as processing and delivering it, such as through a conversational interface; in content support for marketing strategy, including drafting, generating ideas, and presenting knowledge for creating marketing strategies; and in contact-center or customer service automation.

Exhibit

Respondents working in media and telecommunications, insurance, and technology report the most use of AI.

Business functions in which respondents' organizations are regularly using AI, by industry, $^{1}$ % of respondents

<table><tr><td></td><td>Media and telecom</td><td>Insurance</td><td>Technology</td><td>Consumer goods and retail</td><td>Professional services</td><td>Travel and logistics</td><td>Energy and materials</td><td>Financial institutions</td><td>Advanced manufacturing</td><td>Engineering and construction</td><td>Pharma and medical products</td></tr><tr><td>Total</td><td>40</td><td>34</td><td>64</td><td>46</td><td>54</td><td>28</td><td>58</td><td>36</td><td>33</td><td>34</td><td>29</td></tr><tr><td>Knowledge management</td><td>39</td><td>45</td><td>52</td><td>49</td><td>31</td><td>51</td><td>46</td><td>34</td><td>33</td><td>35</td><td>29</td></tr><tr><td>Marketing and sales</td><td>34</td><td>38</td><td>55</td><td>56</td><td>32</td><td>32</td><td>21</td><td>32</td><td>39</td><td>32</td><td>40</td></tr><tr><td>IT</td><td>33</td><td>46</td><td>60</td><td>45</td><td>27</td><td>34</td><td>32</td><td>47</td><td>32</td><td>34</td><td>22</td></tr><tr><td>Service operations</td><td>31</td><td>32</td><td>40</td><td>49</td><td>33</td><td>21</td><td>33</td><td>34</td><td>28</td><td>29</td><td>30</td></tr><tr><td>Product and/or service development</td><td>26</td><td>33</td><td>39</td><td>58</td><td>22</td><td>19</td><td>13</td><td>19</td><td>30</td><td>22</td><td>32</td></tr><tr><td>Software engineering</td><td>21</td><td>28</td><td>16</td><td>28</td><td>22</td><td>22</td><td>20</td><td>9</td><td>22</td><td>19</td><td>18</td></tr><tr><td>Human resources</td><td>17</td><td>17</td><td>46</td><td>18</td><td>15</td><td>11</td><td>15</td><td>19</td><td>17</td><td>47</td><td>7</td></tr><tr><td>Risk, legal, and compliance</td><td>17</td><td>17</td><td>6</td><td>20</td><td>17</td><td>9</td><td>22</td><td>22</td><td>20</td><td>15</td><td>16</td></tr><tr><td>Strategy and corporate finance</td><td>12</td><td>6</td><td>4</td><td>10</td><td>11</td><td>22</td><td>4</td><td>19</td><td>19</td><td>3</td><td>25</td></tr><tr><td>Supply chain/ inventory management</td><td>10</td><td>5</td><td>0</td><td>9</td><td>6</td><td>13</td><td>1</td><td>1</td><td>21</td><td>1</td><td>26</td></tr><tr><td>Manufacturing</td><td>88</td><td>96</td><td>95</td><td>95</td><td>92</td><td>91</td><td>91</td><td>90</td><td>89</td><td>86</td><td>86</td></tr><tr><td>Use in at least 1 business function, %</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

$^{1}$ Respondents who said “don’t know” or “other” are not shown. In media and telecom, n = 98; insurance, n = 61; technology, n = 249; healthcare, n = 101; consumer goods and retail, n = 129; professional services, n = 291; travel, logistics, and infrastructure, n = 66; energy and materials, n = 191; banking and other financial institutions, n = 152; advanced manufacturing (includes advanced electronics, aerospace, automotive and assembly, and semiconductors), n = 136; engineering, construction, and building materials, n = 90; pharmaceuticals and medical products, n = 77.

Source: McKinsey Global Survey on the state of AI, 1,993 participants at all levels of the organization, June 25–July 29, 2025

However, many companies—particularly smaller ones—have yet to integrate AI deeply across their workflows. While only one-third of all respondents say they are scaling their AI programs across their organizations, larger companies—both in terms of revenues and the number of employees—are more likely to have reached the scaling phase. Nearly half of respondents from companies with more than \$5 billion in revenue have reached the scaling phase, compared with 29 percent of those with less than \$100 million in revenues (Exhibit 5).

Exhibit 5

Larger companies lead the way in scaling AI beyond pilots.

Phase of organization's use of AI, by company revenues, $^{1}$ % of respondents

![](images/c60a48c0f9299ce05f63b88bf32790fc0c0ee1312c2527dc5547c4e7b75225a3.jpg)  
Note: Figures may not sum to 100%, because of rounding. $^{1}$ Respondents who said “don’t know” are not shown, but represent <2% of the total.

Source: McKinsey Global Survey on the state of AI, 1,993 participants at all levels of the organization, June 25–July 29, 2025  
McKinsey & Company

While only one-third of all respondents say they are scaling their AI programs across their organizations, larger companies are more likely to have reached the scaling phase.

## AI as a catalyst for innovation

Responses suggest that for most organizations, the use of AI has not yet significantly affected enterprise-wide EBIT. Thirty-nine percent of respondents attribute any level of EBIT impact to AI, and most of those respondents say that less than 5 percent of their organization's EBIT is attributable to AI use. However, respondents see other company-wide qualitative outcomes: A majority say that their organizations' use of AI has improved innovation, and nearly half report improvement in customer satisfaction and competitive differentiation (Exhibit 6).

## Exhibit 6

Respondents most often cite benefits from AI in innovation, employee and customer satisfaction, and competitive differentiation.

![](images/a98ded0791244f4c8c8ad7b7a90787dcee8c96cdb8441f806a7c5e88d88e5835.jpg)  
Note: Figures may not sum to 100%, because of rounding. $^{1}$ Asked only of respondents who said their organizations regularly use AI in at least 1 business function.

Source: McKinsey Global Survey on the state of AI, 1,993 participants at all levels of the organization, June 25–July 29, 2025

## McKinsey & Company

Cost decrease within business units from AI use, past 12 months, by function, $^{1}$ % of respondents

While reported cases of enterprise-wide EBIT impact are limited, many respondents say they are seeing cost benefits from individual AI use cases—especially in software engineering, manufacturing, and IT (Exhibit 7)

[中间内容因长度限制已省略]

h the use of AI are mitigated by most respondents' organizations. In our latest findings, the share of respondents reporting mitigation efforts for risks such as personal and individual privacy, explainability, organizational reputation, and regulatory compliance has grown since we last asked about risks associated with AI overall in 2022. (In 2023 and 2024, we asked specifically about gen AI-related risks.) Back in 2022, respondents reported acting to manage an average of two AI-related risks, compared with four risks today.

We also see that, largely, the risks that organizations are experiencing and are working to mitigate are connected: Respondents are more likely to say their organizations are mitigating each of the risks they have experienced consequences from. Overall, 51 percent of respondents from organizations using AI say their organizations have seen at least one instance of a negative consequence, with nearly one-third of all respondents reporting consequences stemming from AI inaccuracy (Exhibit 19). Inaccuracy is one of two risks that most respondents say their organizations are working to mitigate. However, the second-most-commonly-reported risk—explainability—is not among the most commonly mitigated.

Inaccuracy is the AI-related risk that respondents most often say their organizations have experienced and are working to mitigate.

Negative consequences and risk mitigation in the past year, $^{1}$ % of respondents (n = 1,753)

![](images/2cea1007cb232c8353cac0b1b94b9d73c1fb1e392a12c196268e61fec867e1e3.jpg)  
$^{1}$ Questions were asked only of respondents whose organizations regularly use AI in at least 1 function. Respondents who said “don’t know/not applicable” are not shown.
Source: McKinsey Global Survey on the state of AI, 1,993 participants at all levels of the organization, June 25–July 29, 2025

McKinsey & Company

Respondents from AI high performers, who say their organizations have deployed twice as many AI use cases as others have, are more likely than others to report negative consequences—particularly related to intellectual property infringement and regulatory compliance. High performers also try to protect against a larger number of risks.

![](images/c340b6f6f7529ec0e03666bc9c370d80dc5fe22623a84b56b462e596f7fbd02b.jpg)

## McKinsey commentary Alexander Sukharevsky Senior partner

We know that AI high performers—respondents who say their organizations are deriving higher impact from their use of AI—tend to have more ambitious agendas than their peers. Interestingly, they are also more likely than their peers to report more, rather than fewer, negative consequences from AI use. This isn't as counterintuitive as it might seem. After all, because they are more ambitious, AI high performers are likely to be using the technology in mission-critical contexts that require sensitive monitoring. They also report mitigating these risks at a higher rate than others, given that they are aware of them. Their ambition also has considerable upside: It helps explain why these organizations tend to outperform—and offers an important lesson to those who are still struggling to realize value from their AI efforts. Approaching AI solely through the lens of efficiency, our survey suggests, is not enough. Achieving measurable results requires leaders to pursue a bold agenda, driven by innovation and transformation. That, we are learning, may be the true pathway to high performance.

While the use of AI is now common, our new survey suggests that its full promise still remains ahead. Most organizations are still navigating the transition from experimentation to scaled deployment, and while they may be capturing value in some parts of the organization, they're not yet realizing enterprise-wide financial impact. The experience of the highest-performing companies suggests a path forward. These organizations stand out for thinking beyond incremental efficiency gains: They treat AI as a catalyst to transform their organizations, redesigning workflows and accelerating innovation. As AI tools, including agents, improve and companies' capabilities mature, the opportunity to embed AI more fully into the enterprise will offer organizations new ways to capture value and create competitive advantage.

## About the research

The online survey was in the field from June 25 to July 29, 2025, and garnered responses from 1,993 participants in 105 nations representing the full range of regions, industries, company sizes, functional specialties, and tenures. Thirty-eight percent of respondents say they work for organizations with more than \$1 billion in annual revenues. To adjust for differences in response rates, the data are weighted by the contribution of each respondent's nation to global GDP.

Alex Singla is the global leader of QuantumBlack, AI by McKinsey, and a senior partner in McKinsey's Chicago office; Alexander Sukharevsky is a senior partner in the London office; Lareina Yee is a senior partner in the Bay Area office, where Michael Chui is a senior fellow; Bryce Hall is an associate partner in the Washington, DC, office; and Tara Balakrishnan is an associate partner in the Seattle office.

The authors wish to thank Hailey Bobsein, Hannah Wagner, Larry Kanter, Robert Levin, and Santi Canedo for their contributions to this work.

This article was edited by Heather Hanselman, a senior editor in the Atlanta office.

![](images/f4630f869aca72ce3ee3389d1f879637dbadcc3898c23c2840a3fe4b6381cdd1.jpg)

![](images/d9bf5174d8802996597740b869f79604f19761ff29c6ddf9b3288f34159e888d.jpg)

Find more content like this on the McKinsey Insights App

![](images/04cc9211788e331e3cee66333e67c499b4f7f6ee9b6af2b9927b40b2e6a1eff2.jpg)
"""
