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
- 已识别机构名：`波士顿咨询`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
8. 不要写任何 CTA、广告、扫码、社群、知识星球、网站、域名或关注引导；系统会在最结尾统一插入固定信息。
9. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
10. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.</p>`

【CTA 要求】
- 不要输出任何 CTA。不要写“加入社群”“扫码”“星球”“完整报告领取”“网站”“域名”“关注”“星标”“更多查看”等表达。
- 文末也不要写 CTA；系统会在最结尾统一插入固定信息。
- 正文中间不要出现“如果你从某些关键词搜到这里”“单篇文章只能解决一个切片”“我每天会把……”“这篇可以沿着……”这类表达。

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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份波士顿咨询研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## Luxury is back on track

True-Luxury Global Consumer Insights 2026

12th Edition

JULY 2026

We keep
enlarging our
sources and
tools,
leveraging AI
for the first
time

![](images/296ce916f5d8c2a138fddedc413950d33238a718b26cb36291cc6b75805f0a80.jpg)

Quantitative Consumer Survey with 10,000+ respondents, 100+ questions on both True Luxury Consumers and Aspirationals

![](images/d9f2c890ec2687294786af623b1f07af9892382249995c38c3d6bbd4def4ba83.jpg)

Categories

nativeresearch Research partner

26 Luxury categories explored
Across the 7 Altagamma sectors $^{1}$

Markets Top 11 WW Luxury Markets

美国

![](images/344d9c77382e6f46772b748658d8196b21ebdd4a9eb891add3a0501d16ecb998.jpg)

Qualitative Consumer survey, with 100+ luxury clients interviewed through AI-powered interviews on their purchasing behaviors and preferences VERSO Research partner

![](images/0ca84b4b8506cedb46dcc371c7df1ad52d7a926cb6d150240c6e32b66ce1c63f.jpg)

![](images/564d77233cd4052afb05098e04c18235d1b7450a97924bfc1c2434d50c6879c3.jpg)

Enriched findings with Altrata's database, providing insights into HNWI/UHNWI $^{2}$ wealth composition and spending

ALTRATA Research partner

![](images/d7c828934cfac703779b528635eb7e5124d96a23ef284e4bff228c778e4609c5.jpg)

20+ 1:1 sessions with industry-leading CEOs & executives through the BCGxAltagamma Advisory Board

![](images/3e720b861eb1ce0f95a75622356da27dddbd2e711543821f29c944fee969a76f.jpg)

20+ Luxury experts and Luxury industry educational partners

## BCGxAltagamma 2026 Advisory Board

The priorities of
Altagamma's
partner brands
shaped this
year's
True Luxury
Consumer
Study

![](images/4fc0aeaefcb13bc1b0b8d7793a07da5525667568c0c97d42d82de669d20366ac.jpg)  
Food & Beverage  
Fashion

## We collected from the BCGxAltagamma Advisory Board the top 5 topics that keep executives awake at night

Ranking of priority topics
Top 5 ranking (out of 20+ topics), including unprompted and prompted options

Luxury
purchase
drivers

Creative Direction's relevance

WHY
Consumers buy

AI's impact on Luxury

HOW
Innovation disrupts

Rebound of
Aspirational
Consumer

Geopolitics impact

WHO

Drives growth

## Luxury is back on track

## WHO Drives growth

From "aspirational-driven"

to a balanced
consumer base

## WHY Consumers buy

From
showing off

to feeling better

HOW
Innovation disrupts

From
hype that fades

to lasting shift (AI)

## Luxury is back on track

WHO
Drives growth

From
""aspirational-driven""

to a balanced
consumer base

WHY
Consumers buy

From
showing off

to feeling better

## HOW Innovation disrupts

From
hype that fades

to lasting shift (AI)

## Personal Luxury is back on track, with a similar growth rate as pre-Covid

Personal Luxury goods market growth evolution
CAGR % on period

![](images/7f5752d28da2cd447641560bfe617e630594bb7d4c83f91f0f9068c2b4c4180f.jpg)

## Growth is restarting from a healthier base

![](images/afe17b5f0e464a806a4eca96abd9ef81074037bf4eaeedf02b0ee4e748d02620.jpg)

From travel flows to wealth flows

![](images/6ef220836a42800a6ddb6a21e9a8f9eb1f990398a8a4e0743b4d88f65ed37df2.jpg)  
Personal and Experiential Luxury $^{1}$ Market, Consumer Pyramid

## Pyramid | Top Tier still driving growth, Aspirational stabilizing

20 k€

5 k€

2 k€

<table><tr><td rowspan="2">Cluster</td><td colspan="3">Population Mn</td><td colspan="3">Spend B€</td></tr><tr><td>2015</td><td>2024</td><td>2025</td><td>2015</td><td>2024</td><td>2025</td></tr><tr><td>Top Tier Clients</td><td>0.40.1%</td><td>0.60.1%</td><td>0.70.2%</td><td>12214%</td><td>23623%</td><td>26124%</td></tr><tr><td>Top Absolute</td><td>1.40.3%</td><td>1.80.4%</td><td>1.80.4%</td><td>305%</td><td>485%</td><td>495%</td></tr><tr><td>Entry Absolute</td><td>154%</td><td>174%</td><td>175%</td><td>9611%</td><td>11311%</td><td>12010%</td></tr><tr><td>Top Aspirational</td><td>205%</td><td>225%</td><td>225%</td><td>546%</td><td>606%</td><td>626%</td></tr><tr><td>Other Aspirational</td><td>36591%</td><td>38490%</td><td>38890%</td><td>54864%</td><td>56355%</td><td>57455%</td></tr><tr><td>Total True Luxury</td><td>402</td><td>425</td><td>429</td><td>850</td><td>1,021</td><td>1,066</td></tr></table>

CAGR
'15-'25

+8%

+3%

![](images/64bb800db73fb29e577451d79373c888310acef0e753a6d81c901d5b8cee9fcd.jpg)

Aspirational stabilizing

## Top Tier Clients

• Proven and constant growth engine for the past 10 years: moving from 14% to 24% in spend-share, resilient (indifferent) to macro-cycles
• 420k€ avg. yearly luxury spend

## Absolute

• The solid spine: steady, consistent and quietly growing in value year after year

## Aspirational

\- Back to slow growth

• Volatility driver: macro-driven behavior creating demand instability and swings

## In the USA, AI/Tech is minting new money

![](images/d842c8f4311b7b66e0f52ce842a2c8b224573b58574df57eca177c18830d972e.jpg)

## Wealth ≠ Luxury propensity for new money when it comes to personal luxury

![](images/b75288d6c58e2d05c1f4338745550db6a763cf4dc5d18fc62286b54ab076e333.jpg)

## Pyramid | Aspirational appetite freefall is stabilizing

Q: How will your luxury spend evolve in the next 18 months?
10k+ respondents, %

![](images/2dee8be1e21d8131755af533a89b9c7deb753380fabfdd498f5e2da0fb1022c6.jpg)

![](images/9dec75a92e24e6e36eea2c4ba830881cc5780cba8038e8c6f7beeac19b52900f.jpg)  
1. Net Appetite: \% of Increased a lot - \% of Decreased a lot

## Luxury is back on track

WHO
Drives growth

From
""aspirational-driven""

to a balanced
consumer base

## WHY Consumers buy

From
showing off

to feeling better

HOW
Innovation disrupts

From
hype that fades

to lasting shift (AI)

![](images/a7575779b4f38ebe68b0d8b57ea55aeb69c85c1766be0af7df293a8d136a5843.jpg)  
Today  
9 years ago  
3 years ago

## Meaning of luxury / The time of showing off is over

## Q: What is "luxury" for you?

Top 3 choices, all respondents based on 11 statements

## Self / Intro values

![](images/ce048cd9cbf6f6a0e99d6b7845648bb2cc88a2bc35266a9727e319061e83dbfe.jpg)

## Luxury's new currency is time & health

Luxury's meaning today is directly linked to self-reward, time, health and longevity

## Product

## Status / Extro values

![](images/ca9cdc138032e9669e870def1e3bab43e7b21b062f8285079638248d6e24b45b.jpg)

## Core values remain unchanged

The definition of luxury related to product - rooted in quality, long-term value - remains stable over time

![](images/e8f543d4348670db0c576de450e822e83385d9a96f614d303477c832712219e5.jpg)

## Status is losing relevance

Recognition/Status and Symbol of belonging as definition of luxury have lost relevance vs. 9 years ago

## Purchase drivers for Luxury Goods | Despite everything, product is still king

## Q: Rank the key purchase drivers behind your last purchase in luxury

![](images/32d46b1810a4df94a0ccb6cbfaa151e0876e3b4ccd28d8b636d18c5900c81f08.jpg)  
Source: BCGxAltagamma Proprietary True Luxury Consumer Survey, N=10000, 11 markets: Italy, France, UK, USA, China, Japan, Korea, KSA, UAE, India, Brazil, as of Jun 26

Creative
directors
do not
influence
(most)
consumers

## 56% OF ASPIRATIONALS DO NOT KNOW WHO THE CREATIVE DIRECTOR OF BRANDS THEY BUY IS...

Q: Thinking about the luxury brands you buy, would you say you know who their creative director is?

![](images/b0b84f6d2aeae641cf2059eebcbec5398eb62a736006497d4cb7ac7a85d1c4cc.jpg)

## ... WHILE TOP-TIERS ARE SOMEWHAT INFLUENCED

Q: Thinking about creative directors, which of the following apply to you?

## \~25%

of Top Tier consumers bought from a brand because of the creative director

\~15%

of Top Tier consumers stopped buying a brand because of a change in creative direction

## 70% walked away because of misaligned price, but not all are lost: 50%+ remain within sector

Both Aspirational and Top Tier did not purchase because of price

Q: Have you decided not to buy a luxury product because you felt the price was not justified?

![](images/2c5711a90bf80fedc805a3eaa243bb6c63ca8b9e1378c73811dd9eafeefc13d4.jpg)  
However, they are not lost: 50+% still remain in the sector  
Q: When that happened what did you do instead?
Multiple choice question

![](images/7a8abb43b98c55b4dbb30cb9dc510504d41da42ce75470b23410dca6741cabd7.jpg)  
Source: BCGxAltagamma Proprietary True Luxury Consumer Survey, N=10000, 11 markets: Italy, France, UK, USA, China, Japan, Korea, KSA, UAE, India, Brazil, as of June '26

PRICE REJECTION
IS STRUCTURAL,
NOT TIER-SPECIFIC

Every brand needs to review its price strategy and merchandising grid

## Luxury is back on track

WHO
Drives growth

From
""aspirational-driven""

to a balanced
consumer base

## WHY Consumers buy

From
showing off

to feeling better

## HOW Innovation disrupts

From
hype that fades

to lasting shift (AI)

## AI meets Luxury: what we asked the consumer

1

CONSUMER ADOPTION

Are Luxury consumers already using AI in their personal lives?

2

CONSUMER
RESEARCH & TRUST

Are they using it to research Luxury? Do they trust it?

3

BRAND IMPACT

Does AI affect brand perception and purchase?

Tested on 7 selected use cases across customer-facing domains

Is AI an innovation that is going to last?

## AI is here to stay for Luxury consumers, not another experiment

15 years ago, online disrupted the traditional luxury retail model and transformed the consumer journey...

...now, AI is the major technological trend of the past 15 years, already crossing the consumer adoption threshold

2010s-today

2018-2024

2019-2022

2019-2022

2021-2023

2021-2023

2023-now

![](images/1209cba8f10bbfc9879dd87605852c6e92d2d5c6cc62fc5efa48a1ad58733e9e.jpg)

## Online / omnichannel

Luxury moves from store-only to digital-first; COVID makes online a core channel

![](images/6a5cb776f31b14537f0a7226d9161b474619245f7054814425df4df95f575e51.jpg)  
Lasting innovation

## Immersive 3D-AR/VR

Virtual stores, VR shows and headset worlds for brand storytelling

![](images/8df6881c61488724405a2de2e10033bdafa80a2563be30b56ab86bf9b0d04e84.jpg)  
Hype that faded
×

## Virtual try-on

AR "try before you buy" for eyewear, beauty, watches and sneakers

![](images/387e6bbe1fc7631bbed63dd8e15d200503f3943e1058cc596c397525e6aed43f.jpg)  
Evolution not revolution \~

Gamification

## Branded skins, in-game drops and playable worlds to reach Gen Z

![](images/0b289f130c60b8bc9ef121b80cd0983d68197f56829c09dc652748e132053c28.jpg)  
Evolution not revolution \~

Digital collectibles

## Blockchain-certified digital collectibles sold as a new revenue stream

![](images/804ff1c35bf506b6afae7bb12b92493f8d10b30f280f06ed3457a47455be0a37.jpg)  
Hype that faded
×

Metaverse

## Virtual worlds (Decentraland $^{1}$ , Roblox) as a parallel reality to shop and socialize

![](images/2e527233af1f2b441c9fdbc6bb48dd29525cd17e726e2e927be3b1f773edb517.jpg)  
Hype that faded
×

![](images/854625f1abdb623b23e907b4822e2e8afa6b8dd50b7a66aa61f7a2c7c7232d70.jpg)

## AI / GenAI

AI shifting towards consumer-facing use cases in Luxury (Personalization, Content, After-sales..)

![](images/30707b09fa4bbcef586862c9fcd6c92d76de284541eb9095ba710105effde43c.jpg)  
Lasting innovation

## Luxury consumers are bringing AI into the Luxury consideration journey

Q1: How frequently do you use GenAI tools?
Q2: Have you used GenAI to research Luxury?

Consumers are GenAI-literate in their personal life

Consumers using GenAI to research Luxury

![](images/e14732f077a36aa2977cababe056db797d201095351b27b8e72d171fc1e042f4.jpg)  
Q3: Think about the last time you interacted with GenAI platforms about Luxury. What did you ask?  
What luxury consumers are asking AI $^{1}$ ...

![](images/3ba1b03af6063eb7d17ff041ff53754c8fe6851814abeaa8ffec6cd8f0417e87.jpg)  
...And which categories they are researching $^{2}$

![](images/11d475b256a0f281d3879d0f0d288d8fc97329d4f1ad459705baab97a538feae.jpg)  
1. % of respondents; 2. Out of all the consumers that included a category in the answer;  
Source: BCGxAltagamma Proprietary True Luxury Consumer Survey, N=10000, 11 markets: Italy, France, UK, USA, China, Japan, Korea, KSA, UAE, India, Brazil, as of June '26

# GenAI trusted nearly as much as word of mouth, and 2x social media & influencers

Q: How much do you trust each of the following sources when looking for Luxury products/experiences?
Net Score $^{1}$ , pp

![](images/7a3ebcbe1d0ca723e043e21d0b808c6c3331fef00a99467f070943b2c8c7c902.jpg)

GenAI is
a trusted
source

But still in its early stages, and seen by consumers as more unbiased than social media /influencers, with no sponsored content (yet)

![](images/24ddada43ceb4a7b2654945c452bf9de4edc31db2c9f74ed72338c591c3e3e63.jpg)

## In the research, we tested AI use cases within a Luxury brand ecosystem experience for four client-facing domains

Core Operational Pillars

Design

GenAI product development

Merchan-
dising

Merchandising (AI pricing, assortment...)

Supply Chain

Manufacturing

3

AI Supply Chain (Demand forecast, allocation, replenishment...)

Augmented Manufacturing

Retail operations

5

AI
Retail Ops
(Virtual
Merchandising,
labor
scheduling...)

9

Mark., eComm & Clienteling

8

Customer Experience

After-Sales

Personalization & Clienteling

O O

Agentic Marketing
(Spend allocation, MMM, campaign optimization)

Agentic Commerce / After-sales

Front-end domains

Back-end domains

Domain tested with consumers in this report

![](images/19d8ba9840aa3ebd2a924aa8ae8be57dc7cd4fdae02f9d5762854ff8849cbd91.jpg)

## AI and GenAI are expected and accepted by consumers in most domains...

![](images/bc3bf375f9312ddc41c1389bb9ffb2a3a4c2a531cd4177fcb3b20b09154f6166.jpg)

GenAI Product development
Bag product

Personalization & Clienteling
Client Advisor 1:1 message

Personalization & Clienteling
Clienteling in hospitality

Agentic Commerce (After-sales)
AI After-sales Support (Agent)

GenAI Content
Advertising AI Campaign (Video)

GenAI Content
AI-generated still-life images for website

GenAI Content
AI-generated on-model images for website

## AWARENESS

Would you expect AI to help/support in the example? $^{1}$

![](images/7eb366409443f6ad9fd918b348673eef12bae488725b97c246f952497c48bd6b.jpg)

62% of consumers expect AI-assistance across key luxury use cases

## PERCEPTION

Would you still perceive the brand positively knowing AI helped?

![](images/c56b779209282e56e6991256b5d2794e86238492181c71a66d3506af142b83d8.jpg)

83% still perceive the brand positively after discovering AI-assistance

## IMPACT

Would you still buy the product knowing AI helped?1

![](images/4226c9c537301942ed88c16138305f8dd374365ab08e0a46e55ef8e282472749.jpg)

But nearly 1 in 5 remains uncertain and the headline hides the nuances

77% keep buying from a brand that uses GenAI

1. Product Detail Page

## ...but some “pockets of resistance” need to be managed

![](images/864262e7e925d493592cfe16e25893d7483a6ec71a61d534283146e92b01ae45.jpg)

After Sales, Experiential and Product design use cases have no resistance from the consumers

All other use cases highly accepted, with small pockets of resistance concentrated among Boomers in Western markets (EU and US) on content and clienteling

A de-averaged approach is needed: education on content use cases, value and trust on clienteling

## While Consumers are embracing AI, Luxury companies still lag behind

AI Laggards

Fashion & Luxury
Cumulative share of companies

AI Stagnating

Global

14%

22%

AI Emerging

46%

57%

AI Leaders

AI Scaling

AI Future-built

40%

21%

2024 Fashion & Luxury Average

0

Taking minimal or no AI action, lack foundational capabilities, and are not generating value

2024 average

## 2025 average 2025 Fashion & Luxury Average

Have developed foundational capabilities and started initial experimentation but are struggling to scale and generate value

50

Have developed an AI strategy and advanced capabilities, and are scaling them effectively while starting to generate value

BFFxAI 2025 maturity score $^{1}$

75

100

At the forefront of AI innovation, systematically building cutting-edge AI capabilities across functions and consistently generating substantial value

\~60% of Fashion and Luxury Companies are still at an emerging stage of AI Maturity

1. AI Maturity is assessed through 41 dimensions 2. Based on 2024 AI maturity score, 3. AI Leaders vs AI Stagnating + AI Emerging data for Consumer industry, 4. External metrics, (Capital IQ): Total Shareholder Return (June 24 – May 25 for 1-year, June 20 – May 25 for 5-year); 5. External metrics (Capital IQ): Return on Capital Full Year 2024
Source: BCG Build for the Future 2025 Global Study (n = 1,250 ; n=49 for Fashion & Luxury)

Significant
value
creation
opportunities
even in
domains with
(very) limited
customer
resistance

## GEN AI Use cases: potential value and consumer acceptance

![](images/58fe08ae4f5f9f1cf9485a318295a263cccd22a3153d93084410e67efb2afab9.jpg)

## Altagamma & BCG Team for the 12th edition of the study

![](images/854fb95b60aea1b2925210446e37fab2d64e4dc304bce9f7e48c0e1475d63303.jpg)  
Stefania
Lazzaroni
Altagamma
General Manager

![](images/b6ff1dc27acb093c5adb9686ed55c075fed3025d99575ec9a1b9d6beb6b12bce.jpg)

![](images/6e93ae19ac09be8609da8a005815cce5f8c7160783b05a258710f95d65969e2d.jpg)  
Guia Ricci
BCG Managing Director & Partner

![](images/936a14ae5c4ce8f2cb89eb1f9d125637ffc75552d502500b3fea059579c3b7e9.jpg)  
Luca
Solca
BCG
Senior Advisor

![](images/862633e2762d9c61eaa15af55200cf37d412a298a024c06f4c982948f971a6bf.jpg)  
Lucia
Casagranda
BCG
Principal

![](images/3e23f5630bdff2e9ab4264167f53da76139b988e2383c389daac1394c1b29391.jpg)  
Ioulia Chafrai
BCG Consultant

![](images/042248bb399fe1e39016478c66843ec6d5f153c188b28617bbf2da417d7d66a2.jpg)

![](images/3de3786d72a2d6466e81fcbeb8fa95b1db2b947bb03cf69ad910ebb2f038ad87.jpg)  
Sebastian
Boger
BCG Managing
Director
& Senior Partner  
Beatrice Lemucchi
BCG Managing Director & Partner

![](images/7efed2c2c6a2bf1b38b1474fee7dd197dd4ad861b59370d981bf72795644d5f4.jpg)  
Javier
Seara
BCG Managing
Director
& Senior Partner

![](images/472d956c547ebbaa1c4c988a40e0f5ca845080774353c4c171ffb3f25310d210.jpg)  
Veronique Yang
BCG Managing Director
& Senior Partner

![](images/615a7ac6f03a39fa3636e7ae63a937051d7f188b4596f0adec17875305dd35d2.jpg)  
Pierre Dupreelle
BCG Managing Director & Partner

![](images/c99518dbe7e34bac69d816e2d916c0b67db0856821e8f4080315c36111c8bef0.jpg)  
Yasmine
Hamri
BCG Managing
Director
& Partner

![](images/0dff4680d4e12800ee3da0aa3ea7bd65f611804355708ed6a31b63f3e6223631.jpg)  
Stefano
Todescan
BCG Managing
Director
& Partner

![](images/df83e5f57d997d8ccf01138e76e22ae269aa2862190932e8739a6f67fc963245.jpg)  
Simone Gentili
BCG Managing Director & Partner

## Thank you.

![](images/ef3bc1b6bbdf1cb555d362fd9cef56b0928a2f0b68a50a5e8a9f6aa1692ac3a2.jpg)
"""
