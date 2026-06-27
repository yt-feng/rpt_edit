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
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`JPM`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
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
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份JPM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## A cyclical state of mind

## 2026 Mid-Year Global Economic Outlook

\- The first half of 2026 delivered a material energy price shock, but we maintain our forecast for a cyclical upturn—led by a continued tech boom, and a rebound in hiring and non-tech investment—that sustains global growth at an above-potential pace.

\- As projected in our year-ahead outlook, fading business caution following last year's trade war is the catalyst for the cyclical lift now underway.

\- The risk of a disruptive energy price shock short-circuiting this lift has been reduced by the agreement to open the Strait of Hormuz. However, global GDP growth is still expected to downshift into midyear as the recent CPI spike softens consumption gains.

\- Several factors should temper this downshift and set the stage for a 2H26 reacceleration. Industrial activity will be supported by a positive turn in the inventory cycle. Fiscal measures are cushioning the household purchasing power squeeze, while the opening of the Strait should boost sentiment.

\- Two important developments to watch for: First, we see the recent pickup in US job growth as linked to fading business caution and anticipate sustained gains of 100k per month or faster.

\- Second, we expect European sentiment readings to rebound smartly, placing Euro area growth on track to accelerate to an above-trend pace later this year.

\- While likely to boost productivity growth, AI is also an important contributor to global demand this year. Spending on new technologies is broadening beyond hyperscalers.

\- The energy sector looks set to return to balance earlier than expected and we now project Brent crude oil prices to average \$80/bbl in 2H26.

\- Our constructive growth outlook comes at the cost of price stability and should produce labor supply constraints. Despite an expected drop in energy prices, 2026 global headline and core CPI should rise by more than 3%.

\- Core inflation surprises are sufficient to deliver hikes by many central banks, even as falling oil prices reduce the near-term pressures reflected in current market pricing. In the US, the interaction of elevated core inflation with a fall in the unemployment rate will bring the Fed to hike.

\- Supportive financial conditions linked to central banks' tolerance of persistently elevated inflation underpin our baseline forecast, which anticipates global policy rates will rise less than 30bp over the coming year.

\- More aggressive action by central banks is a material outlook risk. Past experience suggests that an unexpected reset of monetary policy expectations tends to generate financial stress, even with an otherwise healthy economic backdrop.

## Economic and Policy Research

Bruce Kasman
(1-212) 834-5515
bruce.c.kasman@JPM.com
JPM Chase Bank NA

Joseph Lupton
(1-212) 834-5735
joseph.p.lupton@JPM.com
JPM Chase Bank NA

Nora Szentivanyi
(44-20) 7134-7544
nora.szentivanyi@JPM.com
JPM Securities plc

(1-212) 622-8435
maia.crook@JPM.com
JPM Chase Bank NA

## Alex Gallin

(1-212) 270-5492
alex.gallin@JPM.com
JPM Chase Bank NA

Maia Crook (1-212) 622-8435
maia.crook@JPM.com

Bruce Kasman (1-212) 834-5515
bruce.c.kasman@JPM.com
JPM Chase Bank NA
Joseph Lupton (1-212) 834-5735
joseph.p.lupton@JPM.com

## A cyclical state of mind

Our 2026 year-ahead outlook had anticipated a conscious recoupling in which non-tech business spending and hiring would rebound from depressed levels. This focus on a cyclical lift amidst sticky core inflation contrasts with a widely held macroeconomic narrative that last year's job stall represents a structural shift—related to weak labor supply and the diffusion of new technologies—that promotes productivity-led growth and a normalization in central bank policy stances. This start-of-year debate was interrupted by an escalation of the conflict in the Middle East which closed the Strait of Hormuz. Energy price increases have raised consumer price inflation sharply and pushed central bankers into a more hawkish stance than expected. A dark cloud has also hovered over the outlook as fears of an extended Strait closure elevated the risk of a disruptive energy price shock threatening the life of the expansion.

The clouds appear to be clearing with the recent agreement to open the Strait, but the consequences of the year's energy price shock are still being felt. Global GDP growth looks set to downshift into midyear as consumer purchasing power is squeezed by the recent sharp CPI spike. While headline inflation should moderate next quarter, the pass-through of this shock to higher core inflation will persist. The energy price shock has thus raised our 2026 projections for headline (1%pt) and core inflation (0.2%pt) and lowered our global GDP growth projections by 0.2%pt (Figure 1).

Figure 1: Global forecast evolution, 2026  
![](images/440d2472f93ba513112ee29988c391daf3b6a9e2d708797d2bfa599b3113f37f.jpg)  
Source: JPM Global Economics. \*ex. China and Türkiye.

The Middle East conflict has not, however, dampened our conviction that a cyclical upturn is taking hold (Table 1). Incoming economic reports point to a broadening base of tech spending during 1H26. While the application of new technologies should boost productivity growth, it is also boosting demand and contributing to goods price pressures. Evidence suggests that this lift is being complemented by a pickup in non-tech activity as business sentiment rebounds from last year's depressed levels. There are also signs that labor demand is starting to firm.

Table 1: Global GDP growth  
% chg saar, annual figures are %4Q/4Q; potential growth estimates in parentheses

<table><tr><td></td><td>2024</td><td>2025</td><td>1H 2026</td><td>2H 2026</td><td>2027</td></tr><tr><td>Global (2.3)</td><td>2.9</td><td>2.6</td><td>2.7</td><td>2.2</td><td>2.5</td></tr><tr><td>Global ex China (1.9)</td><td>2.4</td><td>2.2</td><td>2.2</td><td>1.9</td><td>2.2</td></tr><tr><td>DM (1.4)</td><td>1.8</td><td>1.5</td><td>1.7</td><td>1.4</td><td>1.7</td></tr><tr><td>United States (1.8)</td><td>2.4</td><td>2.0</td><td>2.5</td><td>1.6</td><td>2.0</td></tr><tr><td>Euro area ex. Irl (1)</td><td>1.0</td><td>1.1</td><td>0.6</td><td>1.1</td><td>1.4</td></tr><tr><td>Japan (0.6)</td><td>0.7</td><td>0.4</td><td>1.0</td><td>0.9</td><td>0.7</td></tr><tr><td>United Kingdom (1)</td><td>2.0</td><td>1.0</td><td>1.8</td><td>0.7</td><td>1.1</td></tr><tr><td>China (3.8)</td><td>5.4</td><td>4.5</td><td>5.0</td><td>3.6</td><td>4.1</td></tr><tr><td>EM ex China (3.3)</td><td>3.7</td><td>3.8</td><td>3.5</td><td>3.2</td><td>3.5</td></tr><tr><td>EMAX (3.4)</td><td>3.4</td><td>4.8</td><td>4.5</td><td>3.3</td><td>3.8</td></tr><tr><td>EMEA EM (2.7)</td><td>3.6</td><td>2.1</td><td>1.8</td><td>3.0</td><td>2.8</td></tr><tr><td>Latam (2.1)</td><td>2.4</td><td>2.0</td><td>2.3</td><td>1.8</td><td>2.0</td></tr></table>

Source: JPM Global Economics

The middle months of the year will likely highlight the tension between an energy shock drag and the business sector lift. While a moderation in global growth towards a potential pace is anticipated, several factors should cushion the drag and set the stage for a growth reacceleration later this year.

\- A normalization in business sentiment... A rebound in business sentiment from its slide following last year's trade war took hold as we turned into 2026 and was the catalyst for the recovery in non-tech spending and hiring (Figure 2). The rise in our business expectations index was interrupted by the Middle East conflict, but receding tensions and falling energy prices point to a resumption in the normalization in sentiment in the coming months.

Figure 2: Global business confidence and employment  
![](images/4b15c0e385456a64092c0b293dbc10eaddab6d8430644f0317168c7394e19fbb.jpg)  
Source: National sources, JPM. Details on request.

\- ... with a recovery in Western Europe. The rebound in business sentiment should be concentrated in Western Europe, which experienced the most significant drop when the Strait of Hormuz closed (Figure 3). Aligned with this rebound, we anticipate Euro area growth to accelerate towards an above-trend pace in the coming quarters after a soft 1H26, highlighting the regional breadth of the current phase of the global expansion.

Bruce Kasman (1-212) 834-5515
bruce.c.kasman@JPM.com
JPM Chase Bank NA
Joseph Lupton (1-212) 834-5735
joseph.p.lupton@JPM.com

Maia Crook (1-212) 622-8435
maia.crook@JPM.com

Figure 3: Business expectations index  
Std dev from 2010-19 avg; shaded region denotes forecast  
![](images/833db34d7145eec683ca03b25e4cf06bd4c26554faa067d5743f0afdfceec7a8.jpg)  
Source: National sources, S&P Global, JPM. Details on request.

\- Industry gets inventory boost as consumers take a breather. Global retail sales volume growth is expected to stall into midyear, but industrial production gains are expected to remain at a solid pace (Figure 4). In addition to sustained support from tech spending, a turn in the stockbuilding cycle looks to be taking hold that should boost goods sector activity in the middle quarters of this year.

Figure 4: Global consumer goods spending and mfg output %3m/3m, saar  
![](images/aaf43c518f17de8e3521c0de55d793ce315c126ba81637a86d49e50fe74ef71b.jpg)  
Source: National sources, JPM. Details on request.

\- Double-barreled cushions for consumer purchasing power. The softening in consumer spending is expected to be tempered by a pickup in job growth that is already taking hold in the US and EM economies (Figure 5). If we are right, US job gains will be sustained at a 100k per month pace or stronger, while global employment gains will rebound towards 1%ar. At the same time, our commodities team has recently revised up their estimates of global energy inventories, prompting a downward revision to their 2H26 oil price forecast—to \$86/bbl in 3Q and \$80 in 4Q. Such a path would provide a meaningful boost to household purchasing power in 2H26 (Figure 6).

Figure 5: Global (ex China) employment  
![](images/7e1703ecf1ec84e12a7a446e0aac54620ae2af611e831a61f3147d2a8c087d1b.jpg)  
Source: National sources, JPM. Details on request.

Figure 6: Energy contribution to global CPI  
![](images/f31b0336b22d7f9ff4d108f5ef0e04bc85be0082a9bd92ba86aa99bbba02a9fe.jpg)  
Source: JPM Global Economics. \*\$78bbl

Underpinning this constructive outlook are accommodative financial conditions and supportive fiscal stances. The Fed's model of the financial conditions impulse for US growth is sending its strongest signal in two decades, excluding episodes of recession exit (Figure 7).

Figure 7: US Fed FCI-G and global credit stress  
![](images/fd2a4657b5a23263420a78395cd9afc2c22a25faf98b48648e929a25f26d2468.jpg)  
Source: FRB, US Dept of Treasury, JPM. FCI-G uses 1-yr lookback.

A similar signal comes from measures of global credit stress. To be sure, household savings rates have moved lower in the past year, but wealth gains have been material and debt servicing costs remain low. If we are right, the recovery in job growth and decline in inflation should support an expansion that continues to generate balanced profit and labor income growth (Figure 8).

Figure 8: US corporate profits and private wages  
![](images/461ad32362daca0103320fc418cfe46768b1f04e7fdfd4e7858afd26eccddf40.jpg)  
You can't have your cake and eat it too

While the cyclical lift embedded in our 2026 year-ahead outlook has been tempered by the energy shock, the shock's impact on inflation is singularly to the upside. Strong growth combined with rising energy prices is a potent mix for the broader pricing complex, particularly when inflation has been elevated for several years. In this regard, the rub to our constructive growth outlook is the threat to price stability against a backdrop of labor supply constraints (Figure 9).

Figure 9: Global (ex China) labor markets  
![](images/a1b323f94e50648f6eb7e6bbe93be65ce08e8be6c83f35746a1b11e7f91908ba.jpg)

Incoming reports highlight building pressure on goods prices. While the recent spike in energy prices is expected to fade, a mix of tech sector bottlenecks, stronger non-tech demand, and rising commodity and transportation costs are now evident. Relative to average annual gains of 0.9% during 2024-25, our models point to core goods price increases of 2%ar this year (Figure 10). The associated firming in goods inflation looks to be broadly based across regions, as signaled by a pickup in import price gains across the G-4.

Our view that global core service price inflation would remain stable, posting a $3.3\%$ increase this year, was challenged by last year's sharp slide—from a $3.7\%$ ar in 1H25 to $2.9\%$ ar in 4Q25. We downplayed the importance of this decline, anticipating an unwinding of a transitory US drag related to the government shutdown and the seasonal bunching of price increases at the start of the year. In the event, services inflation has rebounded—to a $3.8\%$ ar in the first five

months of this year (Figure 11). This pickup has been broad-based across regions.

Figure 10: Global\* core goods CPI model  
![](images/aa02189dfae79dddf1f3f9e31a929405c802e7e82a942d81fb9d11b55e0f5f7a.jpg)

The main source of uncertainty for service price inflation stems from last year's decoupling of labor demand from GDP growth. Estimates of output gaps point to steadily reducing global slack, but the global unemployment rate rose $0.4\%$ pt last year, returning to its pre-pandemic level. We anticipated that this rise would be arrested—by a pickup in hiring amidst weak labor force gains—and the recent firming in global employment gains and decline in unemployment rates is consistent with this view.

Figure 11: Global core CPI  
![](images/7fbb6c8a723c12a49c1f56d1ebc5f8dc903579762e5a0d98a88e4d2fb5fd2884.jpg)

Amidst this uncertainty, we continue to take our lead on service price inflation from labor cost dynamics and signals of pricing power. Consistent with the broad easing in labor markets last year, wage inflation has moderated, but at 3.5% it still stands higher than the pace seen at the peak of the 2000s expansion. A full alignment of service-sector inflation with its pre-pandemic trend could thus remain elusive.

## Tightening pressures increase risk of financial stress

Core inflation is set to remain above central bank targets for a sixth straight year, with our forecasts anticipating US core PCE at $3.4\%$ (4Q/4Q basis), Euro area HICP at $2.5\%$ and EM ex. China and Türkiye is averaging $3.7\%$ . This year's core inflation surprises are sufficient to deliver hikes, which we

expect to continue even as falling oil prices reduce pressure outside the US relative to current market pricing. In the US, it is the interaction of elevated core inflation with a tightening labor market that will bring the Fed to hikes.

## Figure 12: Real policy rate

%; Nominal rate less 2y trailing core inflation  
![](images/a37d8cb4f14f44330d00e8bfba7cf009111b5ab344233c717152063dee30554a.jpg)

The expansion's resilience and supportive financial conditions are linked to the tolerance of central banks in the face of persistently elevated inflation. Global policy rates have fallen over the past two years with core inflation remaining close to $3\%$ . While real rates are above their post-GFC levels, they remain low relative to earlier episodes in which central banks have restrained demand to lower inflation (Figure 12). While our baseline forecast anticipates a broad tightening takes hold, the shallow adjustment anticipated by the Fed, ECB, and most other central banks will push global policy rates up by less than 30bp over the coming year. The threat that more action will be required to contain inflation in an environment of above-potential growth is material, particularly as labor markets tighten and views on $\mathbf{r}^*$ are likely to tilt higher. Past experience suggests that an unexpected reset of monetary policy expectations tends to generate financial stress in an otherwise healthy expansion.

The global economic outlook in summary

<table><tr><td rowspan="3"></td><td colspan="3">Real GDP</td><td colspan="6">Real GDP</td><td colspan="4">Consumer prices</td></tr><tr><td colspan="3">% over a year ago</td><td colspan="6">% over previous period, saar</td><td colspan="4">% over a year ago</td></tr><tr><td>2025</td><td>2026</td><td>2027</td><td>4Q25</td><td>1Q26</td><td>2Q26</td><td>3Q26</td><td>4Q26</td><td>1Q27</td><td>4Q25</td><td>2Q26</td><td>4Q26</td><td>2Q27</td></tr><tr><td>United States</td><td>2.1</td><td>2.1</td><td>2.0</td><td>0.5</td><td>2.1</td><td>3.0</td><td>1.5</td><td>1.8</td><td>2.3</td><td>2.7</td><td>3.9</td><td>3.8</td><td>2.2</td></tr><tr><td>Canada</td><td>1.9</td><td>0.4</td><td>1.5</td><td>-1.0</td><td>-0.1</td><td>1.0</td><td>1.4</td><td>1.4</td><td>1.7</td><td>2.2</td><td>2.6</td><td>1.8</td><td>1.3</td></tr><tr><td>Latin America</td><td>2.1</td><td>1.8</td><td>2.0</td><td>2.3</td><td>1.6</td><td>2.9</td><td>2.1</td><td>1.5</td><td>1.8</td><td>3.9</td><td>4.5</td><td>4.6</td><td>3.7</td></tr><tr><td>Argentina</td><td>4.4</td><td>3.2</td><td>3.2</td><td>4.7</td><td>3.0</td><td>5.5</td><td>4.0</td><td>3.0</td><td>2.8</td><td>31.8</td><td>32.8</td><td>29.4</td><td>20.5</td></tr><tr><td>Brazil</td><td>2.3</td><td>1.8</td><td>1.6</td><td>1.0</td><td>4.5</td><td>2.0</td><td>0.8</td><td>0.4</td><td>1.6</td><td>4.5</td><td>4.6</td><td>4.8</td><td>3.6</td></tr><tr><td>Chile</td><td>2.5</td><td>1.6</td><td>3.6</td><td>2.1</td><td>-1.1</td><td>4.5</td><td>4.1</td><td>3.5</td><td>1.5</td><td>3.4</td><td>4.0</td><td>3.8</td><td>3.4</td></tr><tr><td>Colombia</td><td>2.6</td><td>2.6</td><td>1.5</td><td>0.1</td><td>2.4</td><td>2.5</td><td>1.5</td><td>0.5</td><td>1.5</td><td>5.3</td><td>5.8</td><td>6.2</td><td>5.9</td></tr><tr><td>Ecuador</td><td>3.7</td><td>3.0</td><td>2.0</td><td>12.7</td><td>4.5</td><td>0.3</td><td>1.0</td><td>2.0</td><td>3.0</td><td>1.4</td><td>1.9</td><td>2.2</td><td>1.5</td></tr><tr><td>Mexico</td><td>0.5</td><td>1.0</td><td>1.7</td><td>2.9</td><td>-2.4</td><td>3.3</td><td>2.5</td><td>2.0</td><td>1.6</td><td>3.7</td><td>4.3</td><td>4.3</td><td>3.6</td></tr><tr><td>Peru</td><td>3.4</td><td>3.0</td><td>2.9</td><td>2.2</td><td>2.4</td><td>2.5</td><td>4.0</td><td>2.5</td><td>3.5</td><td>1.4</td><td>4.2</td><td>4.2</td><td>2.8</td></tr><tr><td>Uruguay</td><td>1.8</td><td>1.1</td><td>1.4</td><td>0.8</td><td>3.2</td><td>0.4</td><td>0.0</td><td>1.0</td><td>1.3</td><td>4.0</td><td>3.1</td><td>4.3</td><td>5.1</td></tr><tr><td>Asia/Pacific</td><td>4.5</td><td>4.2</td><td>3.7</td><td>5.1</td><td>5.9</t

[中间内容因长度限制已省略]

terial only and are therefore subject to change without

notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
