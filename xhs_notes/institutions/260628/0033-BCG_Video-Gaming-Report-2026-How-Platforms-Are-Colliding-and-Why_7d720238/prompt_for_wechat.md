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
- 已识别机构名：`波士顿咨询`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份波士顿咨询研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
![](images/f5bddebf1e79096697eb534ed92a358290acce318712dde0031cf2ad05ec9b9b.jpg)

VIDEO GAMING REPORT 2026

# How Platforms Are Colliding and Why This Will Spark the Next Era of Growth

December 2025
By Ernesto Pagano, Giorgo Paizanis, Povilas Joniškis, Niels Danielsen, Francisco Smart, Siddharth Modi, and Henry Anderson

## Contents

03 Introduction
07 GenAI: Opportunities and Risks
10 Platform Evolution: From Console Wars to Cloud Wars
13 UGC: Welcome to the New Creator Economy
16 App Stores Opening Up: A Revolution for Distribution
19 Improving Monetization: The New Math of Game Pricing
23 Growth Through Disruption
24 About the Global Gaming Survey
24 About the Authors

![](images/12e49fe0b84197cccc04469010a548bda429f8c83ec7d9eaef57bc6e6b7b21fa.jpg)

## Introduction

As 2025 comes to a close, the video game industry is emerging from its post-pandemic slump and ready to enter a new, more upbeat era. Employment and investment in the sector are stabilizing; growth is starting to pick up.

This cautiously optimistic industry outlook is evident in BCG's latest Global Gaming Survey of approximately 3,000 gamers, as well as in numerous conversations with industry leaders and our work with companies in the industry. These data points suggest that the long-awaited end to the three-year “video game winter” is imminent, although growth will not return to the rates achieved during the 2010s, when the industry doubled in size in a decade. (See Exhibit 1.)

One ground for optimism is that gamers remain passionate about gaming. Around 55% of gamers in our survey have increased their gaming time over the past six months. In addition, gaming parents told us they are introducing the children to the activity early, creating a pipeline of new players. About 44% of such parents say that their children are playing video games by the age of five, and two of the three most popular first games that their children play include a significant amount of user-generated content (UGC): Minecraft and Roblox. (See Exhibit 2.)

## EXHIBIT 1

# Gaming Industry Growth Is Set to Increase, Ending the Post-Pandemic Slowdown

GLOBAL GAMING REVENUE BY TYPE (\$BILLIONS)

![](images/ee00fbab4f592b184772bc12b38fe1fa0e2a9feb7b5388788ef2487816aa392e.jpg)

<table><tr><td rowspan="2"></td><td colspan="2">REVENUE ($BILLIONS)</td><td colspan="2">CAGR (%)</td></tr><tr><td>2025E</td><td>2020-2025E</td><td colspan="2">2025E-2030E</td></tr><tr><td colspan="5">Cloud</td></tr><tr><td>Streaming service</td><td>0.6</td><td>57</td><td colspan="2">69</td></tr><tr><td>Multigame subscription</td><td>0.4</td><td>52</td><td colspan="2">74</td></tr><tr><td>Game transactional</td><td>0.5</td><td>66</td><td colspan="2">59</td></tr><tr><td colspan="5">PC and console</td></tr><tr><td>Console hardware</td><td>18.3</td><td>3</td><td colspan="2">-7</td></tr><tr><td>Multigame subscription</td><td>13.7</td><td>10</td><td colspan="2">13</td></tr><tr><td>Game transactional</td><td>69.6</td><td>0</td><td colspan="2">3</td></tr><tr><td colspan="5">Mobile</td></tr><tr><td>Advertising</td><td>31.9</td><td>19</td><td colspan="2">9</td></tr><tr><td>In-app purchases</td><td>128.7</td><td>2</td><td colspan="2">5</td></tr></table>

Sources: Ampere Analysis; SensorTower; BCG analysis of historical and forecasted data.
Note: Console hardware data includes handheld PC devices. In-app purchases include mobile subscriptions such as Apple Arcade. CAGR = compound annual growth rate.

## EXHIBIT 2

Almost Half of All Gamer Parents' Kids Start Playing Video Games by Age 5, and Two of Their Most Common First Games Contain UGC

Today, more than 50% of respondents' children began their digital journey by age 5, and about 77% began playing video games by age 7

Q: How old was your child when they had their first digital experience? (%)

Q: How old was your child when they first started playing video games? (%)

![](images/0b742fad9385f1ba09516d0b1a963f5864b071be3e31b081ab7c04f9d1399c32.jpg)  
Two of the three most popular first games for kids are UGC games: Minecraft and Roblox  
Q: What was the first video game your child ever played? (%)

![](images/ff562e1208ecf0be8492807a86a2d82edd3190711a14d1d365b57c76fa4a3be7.jpg)  
Sources: BCG Global Gaming Survey 2025 (N = 2,972); BCG analysis.
Note: UGC = user-generated content. Because of rounding some bar chart totals do not add up to 100%.

Adults are increasing their engagement with games and are continuing to play later in life. In our survey, 40% of baby boom gamers and 50% of Gen X gamers report spending five hours or more each week playing video games. Many adult gamers are introducing the next generation to gaming as well, with 57% of parents saying that they introduced their child to video games. (See Exhibit 3.) This intergenerational influence helps explain why Gen Alpha and Millennials share similar preferences for primary platforms (PlayStation and Nintendo Switch), while Gen Z shows a slightly stronger inclination toward PC gaming. Millennials, the first generation to grow up with PlayStation and Nintendo consoles at home, seem to be perpetuating this gaming cycle across generations. (See Exhibit 4.)

Our upbeat forecast is founded on much more than this, however. We have identified four strategic trends that will reshape the industry over the next five to ten years and create new revenue opportunities. Each is powerful individually, but in combination they are more powerful still because they will bring in a new era of convergence, opening huge new opportunities as gaming platforms collide and old rules of development and distribution no longer apply. Here are the four trends:

\- Generative AI (GenAI), which has the potential to overhaul the building of games, will likely trigger a flood of new games. Although many of them will be low-grade “gameslop,” making curation and discovery more important than ever, some may be breakthrough games that help the industry grow. Today’s definition of “quality” games emphasizes eye-popping graphics and polished storylines, but in the future it may move toward topical or novel titles. We analyzed metadata from Steam and discovered, as of the middle of 2025, around 20% of new games disclosing the use of AI, double the figure of a year earlier.

\- The expansion of user-generated content (UGC) will drive engagement far beyond its current audience of mostly young users. The creator economy for Fortnite and Roblox alone will see payouts exceeding \$1.5 billion in 2025. In BCG's Global Gaming Survey, 40% of gamers said they are consuming more UGC than they did a year ago.

\- The rise of cloud gaming will accelerate fundamental changes in distribution, a critical part of the gaming value chain. It will also broaden access and push gaming toward its new, hardware-agnostic future. Cloud gaming is primed for takeoff: 60% of players in the survey said they had tried it, and 80% of these reported a positive experience.

\- The opening up of app stores will enable developers to pay lower fees and will give them huge new opportunities to control their own distribution. This is an earthquake for mobile gaming, which represents 50% of global gaming revenues, but the tremors may be felt, in time, across the entire gaming ecosystem.

## EXHIBIT 3

Adults Are Driving Growth at Both Ends by Introducing the Next Generation to Gaming and Remaining Engaged Well into Retirement

Most children are introduced to gaming by their parents, making adults the primary onboarding channel

Q: How was your child first introduced to video games? (%)

![](images/15dacd5c54f1a4c04ca9c34602b716fd07763d0d679ba63d3ef963b9ea7a45f6.jpg)  
Sources: BCG Global Gaming Survey (N = 2,972); BCG analysis. Note: Because of rounding not all bar chart totals add up to 100%.  
Boomers continue gaming into retirement, signaling long-term engagement  
Q: How much time do you spend playing video games? (%)

![](images/fc166445fb09b9359b1ff947a8e0357958c6f9175ef3ceb8eb5d5fc270d0e735.jpg)

## EXHIBIT 4

# Younger Gamers Prefer Consoles, Particularly PlayStation and Switch, While Gen X and Boomers Spend More Time Gaming on Mobile

## RESPONDENT'S PRIMARY GAMING PLATFORM, BY GENERATION (%)

![](images/dc93db8b2f5d8cdca0bf14942b4f48cbc7c5b3e552a1dc9cdac3b49e4f44f521.jpg)

\- Console gamers tend to be younger, as consoles—Xbox, Switch, and PlayStation—are the primary platform for well over 50% of Gen Alpha, Gen Z, and Millennial gamers

Sources: BCG Global Gaming Survey 2025 (N = 2,972); BCG analysis.

\- PC games are popular across age groups, with older adults enjoying casino games and younger gamers preferring live service games such as League of Legends

\- Baby boomers lean heavily toward mobile gaming as their primary platform (\~55%)

Note: “Primary gaming platform” refers to the platform that respondents spend the most time on. Respondents who answered “Others” were excluded from the results. The N for AR/VR as primary gaming platform is very low (N = 40). AR/VR = augmented reality/virtual reality. Because of rounding not all bar chart totals add up to 100%.

Together, these trends will significantly change the industry's value chain. For instance, the console wars will become increasingly irrelevant as the battle shifts to competing ecosystems underpinned by omniscreen cloud gaming technology. Another contest will involve discoverability. Shelf space has become digital and infinite, and the hard lines between platforms are diminishing as players move between multiple devices and as games become increasingly multiplatform. In this crowded, noisy marketplace, developers that master community, algorithmic discovery, and new engagement-oriented business models, including subscription and microtransactions, will be the winners.

In addition, the industry is in a position to improve monetization in multiple ways. Some gamers are clearly feeling the cost-of-living squeeze, as more than 75% of survey respondents told us that game prices will impact their purchase choices. Nevertheless, we see many opportunities for the industry to attract valuable incremental revenue.

![](images/98c70d69582387839a884377ab841c4e0c11e2a89be4cc0af3c6e7c019b99a6d.jpg)

# GenAI: Opportunities and Risks

## What's Changing

AI is overhauling the game development process, driving innovation and reducing development costs and time-to-market. But the technology offers no shortcuts to customer acquisition, and this may become more of a challenge if rapidly produced games saturate the market.

## What the Numbers Show

BCG has analyzed metadata from Steam that indicates how quickly the industry is adopting AI: around 7,300 games on the platform disclose AI applications. (See Exhibit 5.)

On the basis of this data, we estimate that approximately 50% of studios are now using AI. Even AAA studios, despite initial reluctance, seem to be moving forward, as shown by the partnership announced in October between EA and Stability AI, which EA says will “reimagine how content is built.”

We see traction increasing in four areas (see Exhibit 6):

\- AI efficiency plays as technology improves code, automates quality assurance, and more broadly tilts the economics of conventional game development in a favorable direction, which may lead to more cross-platform games

\- Game-generating tools that use GenAI to create entire immersive, high-quality games, which some vendors say can accelerate game development by 90%

\- Intelligent nonplayer characters (NPCs) with memory, personality, and adaptive behaviors, putting a long-overdue end to predictable, “Welcome, adventurer” dialogue

\- New types of gameplay in which GenAI co-creates the game, adapting to player choice

Players, however, are generally not concerned. In our Global Gaming Survey, the most significant point of resistance involved adult gamers reacting to AI for generating art/animation; but even there, only 10% had a negative view. Likewise, just 7% of adult gamers had a negative view of using AI to generate story lines and quests, and a mere 5% reacted negatively to having AI generate NPCs and dialogue.

Even this limited degree of skepticism varies across age groups. Child and young adult gamers tend to be much more receptive—indeed, often enthusiastic—about the prospect of NPCs that behave like true friends or of hypercomplex, adaptive quests that human developers would find difficult to script.

## EXHIBIT 5

## GenAI Is Becoming More Common in Game Development

![](images/9a38bbe61a55d2e06ab9073d7382dc803ef0706f5c8690bf311c49e4a7470412.jpg)

## Approximately one-fifth of titles released in Q3 2025 disclosed AI integration

![](images/036669dea1f62bc238c5fa723c21b773aa387122fad180debc9f16d85e990aca.jpg)  
The top three genres disclosing AI use are casual (20%), adventure (16%), and action (14%)  
Source: BCG analysis of data from scraped from Steam platform as of August 2025.
Note: NPC = nonplayer character.

![](images/8c2cb78f53e4282692b9f866d0bb3ec83328673eb9751916303659b860739433.jpg)

Asset creation is the main use; narrative, audio, and user experience are secondary  
![](images/8a36ad7886f1dc55e998c7150db50f2a947231a35b7cb2d8de75c62ae37c815f.jpg)

## EXHIBIT 6

## How GenAI Is Changing the Games Industry

![](images/16da03878fda8dd5ec1f5803eda774ba0347743ca3bd91cd9fd41883d21b7ccf.jpg)

## Driving efficiency

Modl.AI and Mighty Build & Test are complementary AI platforms that automate QA, representing the shift to AI-driven production pipelines. Bots simulate player behavior to detect issues earlier, and automation shortens release cycles and raises code quality.

\- Modl.AI's virtual player bots explore builds and find defects to speed up testing and iteration.

\- Mighty Build & Test runs scalable automated build-and-test pipelines that validate games across devices 24–7.

![](images/abbbf7b61c859ad33992fcc0c365525ee91c0a5d90f50374b5b89fd9e22380d6.jpg)

## Generating games

BitMagic and Series Entertainment are at the forefront of a new wave in game development, using GenAI to make creative, immersive, high-quality games in less time and at lower cost.

\- BitMagic's prompt-based, browser-based solution now has around 1.2M users.

\- Series raised \$28M in funding. Its Rho Engine is a multimodal full-stack creation platform that speeds game development by 90%.

![](images/0cf5b15299964be0fa3177e2e5b05b01582af68cf8ff70b68450dfebbf2f6df4.jpg)

## Making better NPCs

NVIDIA's ACE and Inworld AI are platforms for building intelligent NPCs.

\- ACE delivers a full GenAI stack for natural, real-time character interaction (e.g., in Naraka: Bladepoint).

\- Inworld builds tools and models for powering real-time conversational AI in interactive apps and games.

## Creating new gameplay

![](images/5aa8b331eccb026af03f6f47487f0b7946ef843d0d90f3743581cd2d869abeef.jpg)

Generative AI is shifting games from static menus to co-creation platforms.

\- AI Roguelite is a fully GenAI-driven RPG roguelite where LLMs generate every element (locations, items, and so on), using probabilistic simulations to drive both combat and narrative.

\- Whispers from the Star is a GenAI-driven narrative sandbox game where players interact with an intelligent avatar through natural conversation that evolves with every dialogue.

Note: LLM = large language model; NPC = nonplayer character; QA = quality assurance; RPG = role-playing game.

Significantly, the gamers in our survey were reacting to features they have not yet experienced. A tsunami of low-grade AI-created games could quickly sour their views.

Data from our survey of developers reveals that some are moving fast while many others are holding back. (See Exhibit 7.)

## EXHIBIT 7

## Developers Still Fear Pushback from Gamers over GenAI Use

![](images/dc786a1290835b36284b2d3fbd7ae2b47d1c3411fc1fa6fa7a174f9d41baf226.jpg)  
Source: BCG 2023 Game Developer Survey (N = 81).

## Seizing the Opportunity

It is a mistake to think of AI as nothing more than a way to relieve the pressure of development costs, which can reach \$300 million for an AAA-rated game. AI's promise of faster development cycles and new types of content with lower development costs could trigger a wave of innovation and experimentation. AI can also have a huge impact on the management of live service games, among other forms of live operations content management.

It also opens the way for a new breed of AI-native studios whose output may complement rather than compete with traditional and somewhat hand-crafted AAA game developers. Initially, these efforts may produce lower-quality results, but Clayton Christensen's The Innovator's Dilemma, one of the most important academic studies of disruptive business models, observes that low-end disruptive innovations can quickly improve under the right conditions. In the gaming world, consumers may appreciate having more variety and faster refresh. This may impact discoverability, however, as blockbuster games (with their blockbuster budgets) will have to work harder to stand out in a market crowded with AI titles.

Crucially, realizing this broadly positive future for the industry depends on using AI wisely. Poor-quality,

derivative experiences may overwhelm undercurated game stores, burdening AI with an image problem and creating reputation problems for developers who approach AI more thoughtfully. Copyright and intellectual property issues are another concern. Major studios will not stand idly by if new developers produce lookalike content trained on their rivals' assets or even code base.

Leaders must establish clear principles for AI deployment: transparency, curation, and the redeployment of savings into more ambitious creativity. AI should expand what games can be, not erode the creative canvas.

A further issue relates to trust and the human touch, the sometimes quirky elements that help gamers connect emotionally with the games they love. Even AI-native studios must find a way to generate that kind of personal connection.

## The Takeaway

Deployed with care, AI is a generational opportunity for game developers. But there are risks too. If AI creates a wave of new games, curation and community-driven discovery will become even more important as vehicles for ensuring that gamers can find the experience they want.

![](images/30590458a76cfa8ef9915d86a2ad558c773cf95f593f054ec0884d503ba5f1e0.jpg)

# Platform Evolution: From Console Wars to Cloud Wars

## What's Changing

Cloud gaming is ready to go mainstream, which will transport the industry to a new hardware-agnostic era. The ramifications of this shift will affect companies and individuals across the gaming ecosystem, from console makers to developers to distributors.

There are three models o

[中间内容因长度限制已省略]

and discard much of the industry's old playbook. (See Exhibit 18.)

Cloud gaming ecosystems, user-generated content, AI, and the opening up of app stores will drive rapid changes—both positive and negative, depending on where in the value chain a company sits—that will affect every aspect of the industry. Collectively, they will redefine game production and distribution, which in turn will reshape the gaming landscape and redefine consumer expectations. Improved monetization and the shifting app store ecosystem will have a more immediate impact on companies' bottom line.

By 2030, we should see an explosion of gaming content, an expansion of the global audience for games, and broadening expectations for omniplatform gaming. We anticipate a healthy, growing market, although there will be on the AAA business model will experience continued pressure, and top-tier developers will need to invest further in strategies related to brand, franchise, intellectual property, platform curation, subscription, and windowing. Together, these efforts will challenge and reshape the current landscape and alter value pools.

Executives who understand these changes and position their businesses to seize the opportunities will define gaming's next decade.

## EXHIBIT 18

## The Gaming World in 2030 and Beyond

![](images/ee3ab075f50be4656997f52e21cedb7c454b3ef3d9649a7ca2fd464c4f4db91c.jpg)

## Explosion of content

Discovery and curation will become decisive platform advantages as tens of thousands of new professional and UGC titles flood the market.

![](images/ca0bcf8667ba36b6393f608ce3d3105f060137f5b7b081c890120d337a7f6213.jpg)

## Global TAM expansion

Cloud distribution will reduce large upfront investments and expand access, bringing millions of new players into gaming, particularly if new experiences can be unlocked.

![](images/8a519d5631801485cf675bfdfe2037e7334bc0f22b306c1bf5070412abf3cc8f.jpg)

## Omniplatform gaming

Players will expect persistent access across screens and devices, with ability to take their progress and library with them wherever they go.

![](images/ab3dd4dded89c451d303805c1c63729cb63098732de51dc19da3190368c5851e.jpg)

## Blockbusters as cornerstones

Large-scale hits and exclusive IP will become critical, as gaming blockbusters emerge as the last untapped source of billion-dollar IP. Monetization will demand robust windowing strategies.

![](images/7f3f8eda234afc134954d8bf190d5ab1b467a4ec4300edb832d23631a95c7d20.jpg)  
Note: IP = intellectual property; TAM = total addressable market; UGC = user-generated content.

## Value pools in flux

Value pools will shift across different publishers, infrastructure owners, cloud platforms, storefronts, and creators.

# About the Global Gaming Survey

To better understand gamers' thinking on key issues, BCG commissioned Dynata to conduct a global online survey of 2,972 respondents, ranging from casual mobile gamers to a small number who play video games more than 50 hours per week. Dynata conducted fieldwork from July 9 to July 18, 2025.

A total of 22% of survey respondents resided in the US. Other major countries represented include China (8%), Germany (8%), Japan (8%), and South Korea (8%).

This is BCG's second global survey of gamers. For information about the results of our 2024 survey, see our previous report, Leveling Up for the New Reality.

## About the Authors

Ernesto Pagano is a managing director and senior partner in the Dallas office of Boston Consulting Group and global leader of the media sector. You may contact him by email at pagano.ernesto@bcg.com.

Povilas Joniškis is a managing director and partner in BCG's Dubai office. You may contact him by email at joniskis.povilas@bcg.com.

Francisco Smart is a project leader in BCG's Miami office. You may contact him by email at smart.francisco@bcg.com.

Henry Anderson is a manager in BCG's London office. You may contact him by email at anderson.henry@bcg.com.

Giorgo Paizanis is a partner in the firm's Los Angeles office. You may contact him by email at paizanis.giorgo@bcg.com.

Niels Danielsen is a principal in the firm's Miami office. You may contact him by email at danielsen.niels@bcg.com.

Siddharth Modi is a project leader in the firm's Miami office. You may contact him by email at modi.siddharth@bcg.com.

## For Further Contact

If you would like to discuss this report, please contact the authors.

## Acknowledgments

The authors would like to thank industry collaborators Alejandro Marin Vidal and Rob Schonfeld.

The authors are also grateful to the following for their contributions to this article: Tor Fryer Petersson, Janet Hernandez, Max Legemah, Claire Liu, Jahan Sahni, and Ziwei Tang.

## BCG

Boston Consulting Group partners with leaders in business and society to tackle their most important challenges and capture their greatest opportunities. BCG was the pioneer in business strategy when it was founded in 1963. Today, we work closely with clients to embrace a transformational approach aimed at benefiting all stakeholders—empowering organizations to grow, build sustainable competitive advantage, and drive positive societal impact.

Our diverse, global teams bring deep industry and functional expertise and a range of perspectives that question the status quo and spark change. BCG delivers solutions through leading-edge management consulting, technology and design, and corporate and digital ventures. We work in a uniquely collaborative model across the firm and throughout all levels of the client organization, fueled by the goal of helping our clients thrive and enabling them to make the world a better place.

![](images/5222010d510a5e95ab69501cb00afaa75c4150e60b107da1dc41914c29120e1f.jpg)

BCG
"""
