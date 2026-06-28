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
# At 250, sustaining America's competitive edge

![](images/adfb37e686497e37dfa015e41e30e463d2f38105de7361b0339369caf961b4b3.jpg)

Authors
Rebecca J. Anderson
Olivia White
Eric Kutcher
Kweilin Ellingrud
Shubham Singhal
Scott Blackburn
Arvind Govindarajan
Aly Spencer
TJ Radigan
Mark Staples

![](images/5c2d5e3da5ad3108bddf903d1ec11aea12ec393470fa48d908df2af6a5a5c316.jpg)

Confidential and proprietary. Any use of this material without specific permission of McKinsey & Company is strictly prohibited.

Copyright © 2026 McKinsey & Company. All rights reserved.

# McKinsey Global Institute

The McKinsey Global Institute was established in 1990. Our mission is to provide a fact base to aid decision making on the economic and business issues most critical to the world's companies and policy leaders. We benefit from the full range of McKinsey's regional, sectoral, and functional knowledge, skills, and expertise, but editorial direction and decisions are solely the responsibility of MGI directors and partners.

Our research is currently grouped into five major themes:

— Productivity and prosperity: Creating and harnessing the world’s assets most productively

— Resources of the world: Building, powering, and feeding the world sustainably

— Human potential: Maximizing and achieving the potential of human talent

— Global connections: Exploring how flows of goods, services, people, capital, and ideas shape economies

— Technologies and markets of the future: Discussing the next big arenas of value and competition

We aim for independent and fact-based research. None of our work is commissioned or funded by any business, government, or other institution; we share our results publicly free of charge; and we are entirely funded by the partners of McKinsey. While we engage multiple distinguished external advisers to contribute to our work, the analyses presented in our publications are MGI's alone, and any errors are our own.

You can find out more about MGI and our research at www.mckinsey.com/mgi.

MGI directors

Shubham Singhal (chair)

MGI partners

Arvind Govindarajan

Chris Bradley

Mekala Krishnan

Tanguy Catlin

Kweilin Ellingrud

Anu Madgavkar

Sylvain Johansson

Jan Mischke

Nick Leung

Jeongmin Seong

Olivia White

## Contents

At a glance 3
Introduction 5

CHAPTER 1

At 250, the United States is the world's most competitive economy 6

CHAPTER 2

Looking back: Four chapters 21

CHAPTER 3

The foundations of US competitiveness 38

CHAPTER 4

Looking ahead: Securing the next era 46

CHAPTER 5

America's national project 65

Acknowledgments 67

Endnotes 68

## At a glance

\- At 250 years old, the United States is the world's most competitive economy. It generates 26 percent of global GDP and is home to 59 of the world's top 100 firms. In the past several years, accelerating US productivity growth and announced foreign direct investment inflows have sharpened its edge over other advanced economies.

— It's a new world. AI is unveiling an ever-expanding realm of possibilities, just as geopolitical contention is growing and fertility rates are falling. The United States is a global technology leader today and spends 27 percent of the world's research and development dollars—but will that be enough to sustain its current 59 percent share of top firms?

— Some US historical competitive advantages are becoming liabilities. Current generations owe it to future ones to address deteriorating fiscal health, eroding infrastructure, declining educational achievement, fading manufacturing know-how, and sustained disparities in income and wealth.

\- Safeguarding an economic edge requires evolving, as America has before. The United States has repeatedly adapted its economic model to meet, and then shape, new technologies and geopolitical realities. Since the country's founding, American competitiveness has shifted but sustained across four historical chapters: agricultural, industrial, scientific, and digital. A new one is coming.

— A culture of innovation and natural abundance are abiding strengths on which to draw. By our count, Americans created or supported 76 of the 100 most important inventions since 1776, from steamboats to smartphones, from the electrical grid to generative AI. Over its history, the country has profited from twice as much agricultural land per capita as any other large economy, and it was largely self-sufficient in energy for 200 years, including since 2019. These are just a few examples of its resource wealth.

— We the people will write the coming chapter. Collective effort from American individuals, business, and government can ensure energy abundance, an infrastructure backbone, education that builds minds and skills to match new technology, and the financial strength to pay for it all. The prize is continued growth, national economic security, and economic opportunity for everyone.

US share of global total, %

![](images/76f9e78eb015a7cdb709c9d2f4fa2697ea97730e0b336cbb5f7ae4305ee4e5f4.jpg)  
$^{1}$ As of December 31, 2025.  
$^{2}$ Epoch AI defines “notable AI models” as particularly influential machine learning models, selected based on criteria such as state-of-the-art performance, historical significance, and high citation rates. The data set is manually curated and not exhaustive.

Source: World Bank; World Intellectual Property Organization; McKinsey Value Intelligence; Epoch AI, “Data on AI Models,” published online at epoch.ai, accessed February 2026; McKinsey Global Institute analysis

McKinsey & Company

![](images/8b776c4267a288915bb6bb446d0a79a56d16de030382b3fc66d5f5be6491a86f.jpg)

## Introduction

It began with a startling act of rebellion. In July 1776, delegates from 13 British colonies declared their independence, dissolved their bonds with England, threatened war, and pledged “our Lives, our Fortunes and our sacred Honor” to each other and their newly united states.

One delegate described the mood in the room as a “pensive, awful silence.” The new nation’s leaders harbored grave reservations. All were acutely aware of the potential consequences of their choice: ruin, prison, war, and death. At a remove of 250 years, it’s hard to conceive of the courage that the founders summoned as each walked to the desk and picked up the quill.

Their courage paid off. Over two and a half centuries, the country has transformed from a collection of agrarian colonies into the world's largest and most influential economy. American firms shape global markets, accounting for more than half of the world's market capitalization. US innovation ecosystems define the frontier of science and technology; 76 of the 100 most influential innovations of the past 250 years came at least in part from American minds and hands. Average living standards have exceeded those of any other large nation for the past 100 years, even as affordability remains an issue. By these and many other measures, the United States today is the most economically competitive country in the world.

America's enduring economic edge was never inevitable. The United States, like most every nation, has been shaped by extraordinary difficulties—wars, recessions, depressions, and pandemics. But America has consistently come through in ways that others have not. In large measure, that's thanks to two foundations of American economic competitiveness that it has relied on again and again: a culture of ambition and individual achievement, and a bountiful natural endowment.

Through every chapter of the past 250 years, the United States has harnessed these foundations, not in a fixed economic model but through flexible institutions that have made the next adaptation possible. And it has done so collectively. “We the people”—farmers in the fields, tinkerers in backyard workshops, teachers in schoolrooms, machinists at forges, seamstresses at machines, developers pulling all-nighters to invent world-changing code—have built an American economic powerhouse.

Today, the United States possesses immense economic strengths anchored in its twin foundations. But if history is any guide, these will carry the country only so far. The challenges are clear and present: a mounting national debt, eroding infrastructure, slipping test scores, fading manufacturing know-how, and sustained disparities in income and wealth. The question America confronts today is not how to celebrate its past but whether it can once again find a new alignment of its resources, ambitions, institutions, and policies to secure competitiveness in the next chapter of its story.

Much is at stake: individuals' access to productive employment and affordable essential goods, businesses' ability to scale and take risks, and government's capacity to raise funds and ensure national economic security.

This report examines the arc of US competitiveness, past, present, and future. America's history of reinvention holds compelling lessons as the nation confronts a future of immense if uncertain opportunity.

![](images/a084dbced461762967b911af72a4e95ca2c9b6a8cccf73eedb9ed2d00f1a621d.jpg)

CHAPTER 1

# At 250, the United States is the world's most competitive economy

Over the course of 250 years, the United States has transformed from a small agrarian economy to the world's leading economic power, a position it has enjoyed for more than a century. Today it has the highest income of any populous country (Exhibit 1). $^{1}$

American firms have undergone a spectacular evolution, from small textile mills in New England to world-leading industrial powerhouses to platform technology companies that shape everyday lives around the globe. American innovation, once a matter of adapting tools developed elsewhere to local settings, has gone on to set the global technology frontier. Over time, rising productivity has steadily lifted household living standards and created economic opportunities for millions.

The combination of leadership in global markets, powerful innovation ecosystems, and individual economic opportunity and prosperity can be summed up in one phrase: economic competitiveness (see sidebar "Defining—and measuring—competitiveness").

Today, the United States has 4 percent of the global population but generates 26 percent of GDP, and it accounts for more than 50 percent of market capitalization (Exhibit 2). It has exceeded many of its rich-country peers in labor productivity and growth, especially in recent years, when productivity has accelerated at levels unseen in other major economies. $^{2}$ Leadership in technology also continues to underpin US competitiveness: The country is home to a plurality of the world's top-cited scientists and has the most notable AI models. $^{3}$ Announced annual inflows of greenfield foreign direct investment (FDI) have roughly doubled from the prepandemic period. $^{4}$ And today, as it has since roughly 1900, GDP per capita exceeds that of other major economies.

# The United States has cause for celebration. But there are also reasons for reflection.

## Exhibit 1

## By 1900, the United States had the world's leading economy by size and individual incomes.

Real gross domestic product, $^{1}$ 1820–2024, \$ trillion in 2024  
![](images/4622202c62916a6b1862516b9ed143376ac7daa2fba80d9dad827aea4dfacc76.jpg)

Real gross domestic product per capita, $^{2}$ purchasing power parity, 1800–2024  
![](images/f9df14b01081e6c4e0150370e9041c2aab7dbc98fe6d86158e5805c55254ba06.jpg)  
$^{1}$ Graph shown using real dollars with the base year 2022, using real annual growth rates from the Maddison Project to project backward. Using this methodology, the US economy surpasses the United Kingdom's economy in 1858. Using purchasing power parity, this crossover happens in 1862. Estimates by other academic and journalistic sources range from 1860 to 1890 (eg, Chinn and Frankel, 2008). $^{2}$ In constant 2011 prices.  
$^{3}$ At various times throughout history, several smaller countries with populations of fewer than 10 million people have had a higher GDP per capita than the US (eg, Ireland and Norway today).  
Source: Maddison Project (2023); World Bank; McKinsey Global Institute analysis

## McKinsey & Company

Sidebar

## Defining—and measuring—competitiveness

While there is no universally agreed-upon definition of “competitiveness,” we identified three features that are central to most discussions of the topic, straightforward to understand, and readily visible in the world today: $^{1}$

1. Globally leading firms. First and foremost, a competitive economy has firms that can compete globally and reach scale through a combination of lower relative operating costs (greater efficiency) and quality.

2. Innovation and technology leadership.
A competitive economy also has growing productivity, which is fundamentally driven by expanding know-how, innovation, and new technological development. Sustained competitiveness across time means always being a technological step ahead.

3. Economic opportunity. An economy is only truly competitive if the gains from economic activity translate to prosperity for its people. In the long run, wages and overall prosperity tend to rise with productivity.

A common theme across academic literature is productivity, which both signals and drives competitiveness. High productivity suggests a significant degree of know-how in addition to sophisticated capital inputs, such as machinery. A high growth rate suggests rapid knowledge development, innovation, and advancement of technology. Without high productivity, countries and their firms cannot lead markets over time. Productivity also translates to wage gains for workers and greater prosperity in the long term. $^{2}$

The last feature may be surprising to some. Prosperity is fundamental to competitiveness for multiple reasons. For one, it is mutually reinforcing with market leadership and innovation, as higher wages attract top talent. Households that can

fulfill their basic needs and generate wealth are more productive and spend more as consumers, further reinforcing growth. And economic opportunity is essential to countries in the competition to be the most attractive places to live and work.

Several metrics can be used to measure global market-leading firms, innovation and technology leadership, and individual opportunity and prosperity. Selecting a few is inevitably arbitrary to some degree. The metrics in Exhibit 2, especially those pertaining to individual opportunity and prosperity, are a representative sample, showing a range of strengths and challenges for every country. Not shown are a host of metrics that measure the inputs needed to achieve growth—for example plentiful energy and human capital. We discuss some of these in later chapters.

# Prosperity is mutually reinforcing with market leadership and innovation, as higher wages attract top talent.

# The United States remains the world's largest economy, is home to the world's most valuable companies, and leads in technology and innovation.

Competitiveness indicators for G7 economies and Mainland China

<table><tr><td rowspan="2"></td><td rowspan="2">Global rank among large countries with data available1</td><td colspan="3">Mainland China</td><td>Japan</td><td>France</td><td colspan="2">Canada</td></tr><tr><td>US</td><td colspan="2">Germany</td><td>UK</td><td colspan="3">Italy</td></tr><tr><td rowspan="9">Globally leading firms</td><td>GDP nominal, $ trillion, 2024</td><td>29</td><td>19</td><td>5</td><td>4</td><td>4</td><td>3</td><td>2</td></tr><tr><td>Labor productivity per hour, $ PPP, 2024</td><td>98</td><td>22</td><td>93</td><td>59</td><td>79</td><td>88</td><td>75</td></tr><tr><td>Share of top 100 firms by revenue, %, 2024</td><td>47</td><td>18</td><td>6</td><td>6</td><td>2</td><td>4</td><td>1</td></tr><tr><td>Share of top 100 firms by market capitalization, %, 2025</td><td>59</td><td>12</td><td>2</td><td>2</td><td>4</td><td>3</td><td></td></tr><tr><td>Share of global market capitalization, %, 2022</td><td>54</td><td>10</td><td>2</td><td>6</td><td>3</td><td>2</td><td>1</td></tr><tr><td>Share of global venture capital investment, %, 2024</td><td>58</td><td>12</td><td>2</td><td>1</td><td>5</td><td>2</td><td></td></tr><tr><td>Share of global FDI inflows, %, 2024</td><td>18</td><td>8</td><td>0</td><td>1</td><td>-3</td><td>2</td><td>2</td></tr><tr><td>Share of global manufacturing output, %, 2024</td><td>11</td><td>45</td><td>4</td><td>3</td><td>1</td><td>2</td><td>2</td></tr><tr><td>Share of global exports, %, 2024</td><td>10</td><td>17</td><td>8</td><td>3</td><td>2</td><td>3</td><td>3</td></tr><tr><td rowspan="7">Innovation and technology leadership</td><td>Productivity growth, %, 2019–24</td><td>1.8</td><td>5.7</td><td>0.3</td><td>0.7</td><td>0.4</td><td>-0.4</td><td>-0.1</td></tr><tr><td>R&amp;D expenditure as share of GDP, %, 2023</td><td>4</td><td>3</td><td>3</td><td>3</td><td>3</td><td>2</td><td>1</td></tr><tr><td>Total AI private investment, $ billion, 2024</td><td>109.1</td><td>9.3</td><td>2.0</td><td>0.9</td><td>4.5</td><td>2.6</td><td>0.9</td></tr><tr><td>Count of notable AI models,2 2025</td><td>48</td><td>32</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td>Share of last 10 years&#x27; most cited scientists, %, 2016–25</td><td>38</td><td>5</td><td>5</td><td>4</td><td>9</td><td>3</td><td>3</td></tr><tr><td>Share of last 10 years&#x27; science Nobel Prizes, %, 2016–25</td><td>47</td><td>0</td><td>4</td><td>7</td><td>16</td><td>9</td><td>1</td></tr><tr><td>Global Innovation Index rank, 2025</td><td>3</td><td>10</td><td>11</td><td>12</td><td>6</td><td>13</td><td>28</td></tr><tr><td rowspan="4">Economic opportunity</td><td>GDP per capita, $ thousand PPP, 2024</td><td>86</td><td>27</td><td>72</td><td>52</td><td>61</td><td>61</td><td>61</td></tr><tr><td>Top 10% to bottom 50% pretax income ratio,3 2024</td><td>35</td><td>31</td><td>20</td><td>23</td><td>17</td><td>17</td><td>15</td></tr><tr><td>Average total years of schooling, 2023</td><td>14</td><td>8</td><td>14</td><td>13</td><td>13</td><td>12</td><td>11</td></tr><tr><td>PISA simple average of math/reading/science scores,4 2022</td><td>489</td><td>579</td><td>482</td><td>533</td><td>494</td><td>478</td><td>477</td></tr></table>

$^{1}$ The ranking is out of countries with population greater than 10 million. Country availability varies by metric, up to 94 countries.  
$^{2}$ Epoch AI defines “notable AI models” as particularly influential machine learning models, selected based on criteria such as state-of-the-art performance, historical significance, and high citation rates. The data set is manually curated and not exhaustive.  
$^{3}$ The ratio of the share of income received by the top 10% of the population t

[中间内容因长度限制已省略]

nds continue, this investment will account for 60 percent of a total \$7.2 trillion investment need over the next decade, based on estimates from the American Society of Civil Engineers. Note that this figure is calculated based on the total infrastructure need of \$9.1 trillion minus the \$1.9 trillion needed for energy specifically. "ASCE report card gives U.S. infrastructure highest-ever 'C' grade, stresses need for sustained investment to support economic growth," American Society of Civil Engineers, March 25, 2025.

200 For further reading, see The infrastructure moment: Investing in the expanding foundations of modern society, McKinsey, September 9, 2025.

201 In semiconductors, for example, the United States retains more than 50 percent of global revenues but saw its share of manufacturing capacity fall from 37 percent in 1990 to just 10 percent by 2022, with near-zero presence in advanced logic and high-bandwidth memory chips. State of the U.S. semiconductor industry, Semiconductor Industry Association, July 2025.

202 "Critical goods" refers to goods and materials that are critical to public health and biological preparedness, information and communications technology, energy, and critical minerals, as defined by the Biden administration's Executive Order 14017. "Draft list of critical supply chains," US International Trade Administration, accessed February 16, 2026.

203 "Semiconductor fabs: Construction challenges in the United States," McKinsey, January 27, 2023.

204 See, for example, Wassen Mohammad, Adel Elomri, and Laoucine Kerbache, "The global semiconductor chip shortage: Causes, implications, and potential remedies," IFAC-PapersOnLine, International Federation of Automatic Control, 2022, Volume 55, Number 10.

205 "Outlook for key minerals," global critical minerals outlook 2024, International Energy Agency, May 2024; The hard stuff: Navigating the physical realities of the energy transition, McKinsey Global Institute, August 14, 2024; "The FDI shake-up: How foreign direct investment today may shape industry and trade tomorrow," McKinsey Global Institute, September 22, 2025.

206 "Rare earths and the F-35: Untangling fact, speculation, and spin," Rare Earth Exchanges, September 13, 2025; "6 military uses of rare earth elements in defense technology," Rare Earth Exchanges, October 4, 2025.

207 Based on data from the US Census Bureau, 2025.

208 Niels Graham, "Pharmaceuticals are China's next trade weapon," Atlantic Council, November 7, 2025.

209 "The FDI shake-up: How foreign direct investment today may shape industry and trade tomorrow," McKinsey Global Institute, September 22, 2025, using data from fDi Markets; McKinsey Semiconductor Supply and Demand Model; "Comments of ITIF to the Department of Commerce Bureau of Industry and Security," Information Technology & Innovation Foundation, May 7, 2025, using data from the Semiconductor Industry Association.

$^{210}$ Based on data from the US Census Bureau and Jonathan E. Hillman, U.S. economic security: Winning the race for tomorrow's technologies, Council on Foreign Relations, Task Force on Economic Security report number 83, November 13, 2025.

211 Based on data from the US Census Bureau.

212 Jonathan E. Hillman, U.S. economic security: Winning the race for tomorrow's technologies, Council on Foreign Relations task force report number 83, November 13, 2025; Jonas Löfvendahl, "Low noise with high potential," Quantum Sweden Innovation Platform, accessed February 12, 2026; "Case: Kyocera Technologies—

Shared-use cleanroom powers MEMS resonator innovation," VTT Research, accessed February 12, 2026.

213 Jonathan E. Hillman, U.S. economic security: Winning the race for tomorrow's technologies, Council on Foreign Relations task force report number 83, November 13, 2025.

214 "In a moment of tariffs, can the world find balance and trust to thrive?", McKinsey, May 2, 2025.

215 Based on data from the National Science Foundation. From 1953 to 1990, average business-funded R&D was 1.0 percent of GDP, while federally funded R&D was 1.3 percent of GDP.

216 Based on data from the US Census Bureau.

217 Based on data from the US Census Bureau (Trade Data Online), the US Bureau of Labor Statistics (Current Population Survey), and Lightcast.

218 For example, previous MGI researched found that greater greenfield FDI flows tended to result in higher exports, if sufficient human capital and infrastructure, global value chain integration, and meaningful domestic investment are present. "The FDI shake-up: How foreign direct investment today may shape industry and trade tomorrow," McKinsey Global Institute, September 22, 2025. See also Christine Zhenwei Qiang, Yan Liu, and Victor Steenbergen, An investment perspective on global value chains, World Bank, May 2021.

219 "The FDI shake-up: How foreign direct investment today may shape industry and trade tomorrow," McKinsey Global Institute, September 22, 2025.

220 Jonathan E. Hillman, U.S. economic security: Winning the race for tomorrow's technologies, Council on Foreign Relations task force report number 83, November 13, 2025.

221 See, for example: Jonathan E. Hillman, U.S. economic security: Winning the race for tomorrow's technologies, Council on Foreign Relations task force report number 83, November 13, 2025; Tim Welter et al., 2025 economic statecraft summit report, Potomac Institute for Policy Studies, December 16, 2025.

McKinsey Global Institute

March 2026

Copyright © McKinsey & Company

Designed by the McKinsey Global Institute

mckinsey.com/mgi

X @McKinsey\_MGI

@McKinseyGlobalInstitute

in @McKinseyGlobalInstitute

Subscribe to MGI's LinkedIn newsletter,

Forward Thinking: mck.co/forwardthinking
"""
