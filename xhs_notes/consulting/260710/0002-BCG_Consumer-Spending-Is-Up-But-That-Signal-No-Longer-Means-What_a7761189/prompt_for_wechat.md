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
Consumer Spending Is Up, But That Signal No Longer Means What It Once Did

By Terence Smith, James Gott, Trap Yates, Kathleen Polsinello, and Shloka Sharan

July 2026

Source: StatsCan, BCG Analysis

Canada's consumer looks resilient. Real spending rose about $2\%$ in Q1 2026, in line with Canada's ten-year average and the US, and per-capita spending has now grown for six straight quarters. In the past, signals like these usually meant households were in good shape and buying more. But resilience is not durability.

Outside the top $20\%$ of earners, the growth isn't coming from income. Households are covering their spending by relying more on savings, leaning on rising portfolio values, and borrowing. And much of the increase isn't buying goods at all. Services are driving most of the growth, including financial services tied to borrowing and asset-linked fees, while real spending on essentials is flat and purchases of cars, furniture, and appliances are falling.

The strain has reached the mass market most consumer businesses are built on. The middle 60% are still spending, but their savings and balance sheets are moving more in the direction of the bottom 20% than the top 20%. The question is whether their spending starts to follow suit.

## Canadians Are Spending More Than They Earn

Across income tiers, Canadian households raised their spending by roughly the same proportion between 2021 and 2025: up 27% in the lowest band, 19% in the middle, and 24% at the top. (See Exhibit 1.) What separated these bands was how much of the increased spending their incomes could cover.

## EXHIBIT 01

Spending Up Across Groups But Only Top Had Income to Support It

![](images/9a7189b6bc1bb47df30792431625a11442a9f2f84a3a3b8178afb473f07ab530.jpg)

The top 20% of earners were the only segment where income growth fully matched and supported spending expansion, covering 106% of their increased expenditures. For the middle 60% of earners, the traditional bedrock of commercial demand, income growth covered just 57 cents of every dollar of new spending. The lowest 20% covered almost none of it. With income up by just 3%, the rest came from somewhere other than their paycheques.

## The Middle Is Relying More on Savings

Annual household savings rose for the wealthiest households and deteriorated for the remaining 80% of Canadians. Between 2021 and 2025, the top 20% saved more over time, while savings weakened across the rest of the income distribution. Many households are now moving closer to, or further into, negative savings. (See Exhibit 2.)

Top 20%

## EXHIBIT 02

## Bottom 80% of Earners Sliding Deeper Into Negative Savings

Average yearly household savings (\$K, nominal)

![](images/293d83052b9e7c4701dc81aae2d67e573d3c8407cf71f543277ee90ce963775d.jpg)  
Source: StatsCan, BCG Analysis

The middle 60% moved from a modest positive savings position to spending more than their income, a deterioration of roughly \$7 thousand per household. The lowest 20% fell deeper into a negative savings position, with annual savings declining by roughly \$15 thousand per household.

Some of this reflects the composition of the lowest-income group, including retirees, students, temporarily unemployed households, and others with low current income who may still spend by drawing on prior savings, family support, or borrowing. Still, the direction of travel is clear: savings buffers are weakening across much of the income distribution. The BCG Global Consumer Radar Survey reinforces this point: 41% of Canadians say they do not expect to save, or expect to save less, over the next six months, a high share that remains slightly above September 2024 levels.

## Asset Gains Are Sustaining Spending, but Not Equally

With household budgets under pressure, asset gains have enabled sustained spending across the top 80%. These cohorts saw total assets grow by 13% to 26%, helped by rising market valuations. (See Exhibit 3.) Those gains likely provided confidence to keep spending and, for some households, additional equity to borrow against, even as income failed to fully keep pace with spending for the middle 60%.

## EXHIBIT 03

## Asset Gains Have Driven a Wealth Effect for the Top 80%

![](images/2f2f9e796d62af26ea32279861e6791cd0ec947fc79b573f69840f7c5fcf174f.jpg)  
Source: StatsCan, BCG Analysis

Financial asset growth driver
Financial assets outpaced total asset growth in all quintiles, equity markets are primary wealth engine

## Assets concentrated at top

Highest quintile holds >50% of asset gains across the different segments, with 4x the assets of the lowest 20%

## Diverging consumer resilience

Diverging consumer resilience
Top 80% benefiting from increased consumer confidence from wealth effect, bottom 20% has liquidated assets to sustain spending growth

This asset-driven confidence does not extend to the lower end of the income scale. The bottom 20% saw their total assets shrink by 2%, leaving households with the fewest buffers least able to benefit from rising asset values.

## Borrowing Is Filling the Gap

The last support is credit. When income lags and savings thin, households borrow to keep up. The middle 60% saw the fastest growth in liabilities, up 22%. (See Exhibit 4.) Asset gains have kept their net wealth positive on paper, but much of that wealth sits in homes and other illiquid assets they cannot easily access. That leaves households more exposed to the rising debt.

## EXHIBIT 04

## All Households Leaning on Debt But Lowest 20% Most Underwater

![](images/76e47e6062e7dccd8e7e0fe432d8128c264e46d855ff5b315ad68255fd20cd7b.jpg)  
Source: StatsCan, BCG Analysis

![](images/fd12657677801db9331379e99a1952319a8a82b9647d61f584998569712a63d5.jpg)

The lowest-income band added 17% to its liabilities against a shrinking asset base, cutting net wealth by roughly \$35 thousand per household. Together, the data point to a growing reliance on borrowing to sustain spending, especially among households with the fewest financial buffers.

## What This Means for Business Leaders

Equity valuations sit near a 25-year high relative to the size of the economy, and five-year Government of Canada bond yields have risen about 40 basis points in recent months. If asset values soften while borrowing costs climb, the households with the thinnest buffers have the least room to absorb the shock.

The result is that Canada no longer has a single “average consumer” to plan around. The top fifth is pulling away on income, assets, and balance-sheet strength; everyone else is leaning on supports that are thinning. For leadership teams, that means growth plans need to be built around a more uneven, more financially constrained consumer. Three shifts matter most.

\- The middle may become even more value-oriented. As financial pressure moves up the income spectrum, middle-income consumers may become more selective and deliberate about what categories they buy, when they buy, and what they are willing to pay for. While price, promotions, and quality will remain table stakes for delivering value, larger pack sizes and bulk options may become increasingly important value drivers for low- and middle-income consumers, particularly for everyday purchases.

\- Credit conditions will matter more. As more spending is supported by borrowing, demand may become more sensitive to interest rates, credit availability, and household debt-service pressure. Leadership teams should stress-test category demand against tighter credit conditions, especially in higher-ticket and discretionary categories. Automotive, luxury goods, dining, and pet care are among the categories with the largest spending differences across income groups.

\- Wealth will not translate evenly into spending. Asset gains have supported confidence, but much of that wealth sits in homes and other illiquid holdings, creating friction for discretionary purchases. If higher oil prices bleed into broader inflation, consumers may struggle to keep up (even if asset prices remain elevated), increasing the need for financing, trade-in, or deferred-payment options.

## About the Authors

![](images/51be134764b33e35cac9ebad8547ab91b74d53e3efb405788f93ac5f85bbae7d.jpg)  
Terence Smith
Senior Director, Centre for Canada's Future
Toronto
smith.terence@bcg.com

![](images/5fb6dccd9bae948e89d8f38139ac4e94f1cc11634e2bd03e8e97ec9452531c2a.jpg)  
James Gott
Managing Director & Partner
Toronto
gott.james@bcg.com

![](images/121311d9dfe0350642f45f6e6defbc81f0ce0079c4460afb02347bb284a39aad.jpg)  
Trap Yates
Managing Director & Partner
Toronto
yates.trap@bcg.com

![](images/65daec77c50df6efed09a2244ac99a08972a74b6c7617d734bb5db8bacce4a05.jpg)  
Kathleen Polsinello
Managing Director and Senior Partner
Toronto
polsinello.kathleen@bcg.com

![](images/2f6c893323b9078120ab8596599fac784660da814dfe7e443df4bb552dfa21fd.jpg)  
Shloka Sharan
Partner
New York
sharan.shloka@bcg.com

## Acknowledgments

Thank you for significant contributions from Kate Banting, Anguel Dimov, David Oliver, and Ciarra Collison.

## Boston Consulting Group

## Where Strategic Clarity Meets Applied AI

We are navigating an era of unprecedented change and disruption—powered by technology, marked by complexity, where change amplifies at scale. To lead, companies need a partner that can bridge the gap between ambition and outcomes. BCG is built for this moment. We bring strategic clarity, rooted in over 60 years of deep domain knowledge, to ensure leaders make the right choices. We combine it with applied AI, shaped and wielded by our practitioners, teaming shoulder-to-shoulder with your teams to deliver transformative impact at scale. The result? Stronger returns, transferred capabilities, and change that sticks. We are BCG.

## Centre for Canada's Future

BCG Canada launched the Centre for Canada's Future in 2017 to mark the country's 150th anniversary, with a forward-looking effort to assess Canada's opportunities and challenges. The Centre serves as a catalyst for progress by shaping the national agenda, elevating public dialogue, and identifying pathways to a more prosperous future.

This work reflects BCG's longstanding commitment to Canada and the legacy of civic entrepreneur David Pecaut. Guided by rigorous analytics and strategic insight, we focus on tackling society's most pressing issues and on helping Canada realize its full potential.

For information or permission to reprint, please contact BCG at permissions@bcg.com. To find the latest BCG content and register to receive e-alerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on LinkedIn, Instagram, Facebook, and X.

![](images/8e91c1ba99929d7612e00d64a5834a912bda80d5a7098ed6ea5772920f5324a5.jpg)
"""
