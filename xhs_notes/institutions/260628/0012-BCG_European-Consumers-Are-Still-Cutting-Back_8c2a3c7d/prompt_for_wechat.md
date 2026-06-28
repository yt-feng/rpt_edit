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
![](images/4db1bc3807e5316a2170c69fdebcf4ad1c3fef87d79f396ac7a3f53266ce1e7d.jpg)

CONSUMER PRODUCTS INDUSTRY

# European Consumers Are Still Cutting Back

By Andreas Malby, Nicolas de Bellefonds, Rohan Sajdeh, and Vishakha Chopra

ARTICLE JUNE 09, 2026 12 MIN READ

European consumers have been navigating a prolonged period of economic strain. Inflation and fear of a potential recession raised consumer pessimism about the economy in 2025 to 54%, up 5 points from the prior year. That trend continued in 2026, increasing to 56%, as consumers say that rising energy prices and geopolitical tensions are impacting them. Consumers also show growing pessimism about politics and their personal finances. (See Exhibit 1.)

Economic situation

Sources: 2026 BCG European Consumer Sentiment Survey (April 2026) with 20,093 respondents across 11 countries (\~1,800 responses per country); 2025 BCG European Consumer Sentiment Survey (April 2025) with 16,412 respondents in 9 countries; 2024 BCG Consumer Sentiment Survey (July 2024) with 7,000 respondents in 5 countries; BCG analysis. Note: Some bars total more than 100 due to rounding. Question: "How do you currently feel about each of the following?"

## EXHIBIT 1

Consumers Are Pessimistic on the Economy but Positive About Their Health

Your personal finances

Political atmosphere

Climate

Your physical health

Your mental health

![](images/8cdcb8c05ca781be1792dde3994f94ebaf8dc6e623d102102ab29d28e0dd959f.jpg)

Personal health is an exception to this negative sentiment. Nearly two thirds, or 65%, of consumers rate their mental health and 56% rate their physical health as good. These findings emerge from our third annual survey of European consumers. We surveyed more than 20,000 consumers in 11 European countries. (See “Methodology.”)

## - Methodology

From April 2 to 22, we partnered with NativeResearch to survey approximately 1,800 consumers in each of 11 European countries: Denmark, Finland, France, Germany, Italy, Norway, Poland, Romania, Spain, Sweden, and the UK. Respondents answered questions about their current concerns, personal financial situations, and shopping behaviors across 12 consumer categories.

Year-on-year comparisons draw on two prior surveys: an April 2025 survey of nine countries (Denmark, France, Germany, Italy, Norway, Romania, Spain, Sweden, and the UK, totaling 16,412 respondents) and a July 2024 survey of five countries (Denmark, France, Germany, Sweden, and the UK, totaling 7,000 consumers). Comparisons with 2025 and 2024 include only the countries surveyed in that year.

The survey captures consumer sentiment by looking at net spending—the percentage difference between the share of consumers reporting they have or will spend more and those reporting they have or will spend less. As with all

# Financial Stress Is the Default

This pessimism is causing financial distress. More than half, or 53%, of European consumers are worried about their daily personal finances, up from 40% in 2024. Six in ten are concerned about having enough money in retirement. (See Exhibit 2.)

## EXHIBIT 2

More Than Half of European Consumers Are in Financial Distress and Changing Their Consumption Patterns

![](images/77aebef27662638389d7c1ecc69eac82c1fd58b08ab914ba9530048cef795d67.jpg)  
Sources: 2026 BCG European Consumer Sentiment Survey (April 2026) with 20,093 respondents across 11 countries (\~1,800 responses per country); 2025 BCG European Consumer Sentiment Survey (April 2025) with 16,412 respondents in 9 countries; 2024 BCG Consumer Sentiment Survey (July 2024) with 7,000 respondents in 5 countries; BCG analysis.
Question: "Please tell us to what extent you agree with each of the following statements." (Results shown for "Agree.")

Given a hypothetical windfall of 10% to 15% extra income, nearly half of consumers said their top priority would be to save more, signaling that they are focused on building a financial buffer and may not spend more right away when the economy improves. Their second priority would be to spend on experiences like travel and dining out, followed by other discretionary categories.

EXHIBIT 3 Consumers Continue to Prioritize Essentials

## A Big Leap Toward Essentials

The shift to essentials has continued and deepened. The survey captures consumer sentiment by looking at net spending—the percentage difference between the share of consumers who reported increased spending and those who reported decreased spending.

Over the past six months, groceries and pet care are the only categories posting positive net spending. This reported growth is primarily fueled by increasing prices rather than greater volume. Every other category is flat or negative. As in 2025, consumers report the largest negative net spending on fashion, alcohol, and packaged snacks. (See Exhibit 3.)

![](images/522704bebd09cb501873adf688be3a60eb10d7c861b42a9e4984b0043915ed3a.jpg)  
Sources: 2026 BCG European Consumer Sentiment Survey (April 2026) with 20,093 total respondents across 11 countries (\~1,800 responses per country); BCG analysis. Note: Net spending is the percentage difference between the share of respondents indicating an increase of spending and those indicating a decrease of spending within a category. For products bought less frequently (home appliances and furniture) net spending is shown for the past year and next year, rather than previous and next six months. OTC = Over-the-counter drugs and supplements.

³Question: "In the past six months/one year, how much has your total spending changed compared to six months ago/a year ago?" ²Question: "How much do you expect your total spending to change in the next six months/year compared to today?"

Even within categories, consumers are making sharp distinctions between essential and indulgent items. For example, within fashion, footwear (−12 points net spending), casual wear (−13 points), and sportswear (−14 points) have held up better than formal and evening wear (−20 points), handbags (−23 points), and accessories (−22 points). Within pet care, the category with the highest overall positive net spending sentiment (12 points), consumers report spending more on everyday pet food (19 points) than on pet accessories (−10 points).

Consumers of all incomes and ages are pulling back from categories misaligned with their health goals. They report sharply decreasing their spending on alcohol, sugary snacks, ice cream, and beverages.

## The Great Generational Divide

There are age-related nuances to this overall picture. Younger consumers report cutting less relative to older cohorts. Over the next six months, reported net spending among Gen X and Baby Boomers is -13 points, and for Gen Z and Millennials it is -2 points. This 11-point delta increased by 2 points over 2025, driven by older cohorts cutting even further this year.

The gap widens measurably in individual categories. In furniture, younger consumers report net spending of +3 points, compared with -22 points for older consumers, a 25-point gap. In fashion, the net spending is 23 points higher for young consumers; in home appliances, 16 points. (See Exhibit 4.)

## EXHIBIT 4

Older Generations Are Cutting Discretionary Spending More

![](images/ad938ba553d9710c495c263753893d5dbb6bb5278dea72bcee64231744039650.jpg)  
Sources: 2026 BCG European Consumer Sentiment (April 2026) with 20,093 respondents across 11 countries (\~1,800 responses per country); BCG analysis. Note: Net spending is the percentage difference between the share of respondents indicating an increase of spending and those indicating a decrease of spending within a category. For products bought less frequently (home appliances and furniture) net spending is shown for the past year and next year, rather than previous and next six months. OTC = Over-the-counter drugs and supplements.
Question: "How much do you expect your total spending to change in the next six months/year compared with today?"

Life stage more than income likely explains the difference. Younger consumers are spending to create a home and raise a family, even under financial pressure. When asked about their reasons for spending less, younger generations said they were trading down to less-expensive brands or stores or buying lower-quality items; older consumers said they were reducing overall consumption.

The younger generation are less loyal to brands, with only 28% reporting they usually buy the same brand, compared with 44% of older consumers. They are also more than twice as likely to buy second-hand goods.

## Health Is the New Wealth

Against a backdrop of broad spending cuts, health and well-being are becoming essentials in consumers' minds. Two-thirds of European consumers say health and wellness are extremely important to their lifestyle. Their actions reflect this conviction. Nearly half, or 46%, report drinking less alcohol or are considering it. Many consumers are choosing abstinence, with only 28% choosing low- or no-alcohol alternatives. (See Exhibit 5.)

## EXHIBIT 5 Health Is the New Wealth

![](images/be27887c481632d80bb3922f0e11682ef6852169d7ecb611d0cce3db4ede847c.jpg)  
About two-thirds of consumers say health and well-being are extremely important to their lifestyle

![](images/bb4eb7de6ed9f8459e0742a3669446cf1fadeb27fddc5a84adeacbbbb07e2355.jpg)  
Sources: 2026 BCG European Consumer Sentiment Survey (April 2026) with 20,093 respondents across 11 countries (\~1,800 responses per country); BCG analysis. Question: "Please tell us to what extent you agree with each of the following statements in relation to [assigned category]." (Results shown for "Somewhat agree" and "Strongly agree.")

In snacks, the shift toward functional and clean-label formats signifying simple, natural ingredients with minimal processing and no artificial additives shows up both in attitudes and reported spending. Indulgent sub-categories like chocolates, ice creams, and cookies are among the weakest in the survey, while healthier formats like protein-fortified snacks are performing better. Supplements are growing, with 29% of consumers reporting increased spending in the past year.

GLP-1 appetite-suppressing medications, such as Ozempic, Wegovy, and Mounjaro, have achieved remarkable consumer awareness. Nearly three-quarters of Europeans, or 74%, know what they are. One in four European consumers report either using them or are seriously considering doing so. Gen Z and Millennials are more likely to consider these medications (19%) than GenX and Baby Boomers (8%). If this awareness converts to consumption, the implications for food, personal care, and health categories will be meaningful.

The health and wellness mindset also applies to pet care. Six in ten consumers report they are willing to spend more on high-quality pet food, and 68% want clearly listed, recognizable ingredients in pet food. In this respect, they have higher standards for labeling of pet food than human food. Pet care is where health and wellness concerns meet emotional spending, making it a bright spot in an otherwise subdued consumer landscape.

## The Price Is the Message

After two years of uncertainty and cut-backs, value-seeking is now deeply embedded in consumer behavior. Nearly two-thirds, or 63%, of consumers will only buy at a discount or actively seek deals—the same as last year. In fashion, that share reaches 73%. Even in over-the-counter medicines and supplements, the category with the highest brand loyalty, half of consumers are hunting for a better price.

Brand loyalty is on a decline, with 62% of consumers reporting that they are willing to switch brands for better offers. The willingness exceeds 70% in categories such as furniture and fashion. This translates into reported purchasing behavior. A significant share of consumers (44%) say that, in their most recent purchase, they have either switched to a brand they don’t normally buy or one they have never bought before. This shift is reinforced by the steady rise of private labels, particularly in groceries (39% of consumers always or often buy private label brands), home care (30%), and fashion (29%).

Discounts and in-store visibility are the strongest influences converting consumers into purchasers and the top reason for brand switching. Brand reputation ranks fifth. For brands that focus on broad, mass-reach marketing, these findings call into question the belief that awareness leads to conversion. (See Exhibit 6.)

## Discounts Are the Top Reason to Switch Brands

RESPONDENTS WILLING TO SWITCH BRANDS IF VS. 2025 THERE ARE BETTER OFFERS $^{1}$ (%) (PP)

![](images/69c19af0b179175ead8bafded5b49f36200524e0a476f64de18c6c2c9bf5cca4.jpg)  
TOP FACTORS INFLUENCING PURCHASE DECISIONS FOR CONSUMERS $^{2}$

![](images/f7e862d93cc40127a932a9f757c92dd872a65cf0ea225401d0b8202fcb26e6f2.jpg)  
WHAT BEST DESCRIBES THE CHOICE OF 44% OF CONSUMERS WHO REPORTEDLY CHANGED BRAND IN THEIR RECENT PURCHASE? $^{3}$

![](images/d80cb08dc6a7a04b71bfa430596242bb89fb17a0564206da4744c8f58c055e4f.jpg)  
Sources: 2026 BCG European Consumer Sentiment Survey (April 2026) with 20,093 total respondents across 11 countries (\~1,800 responses per country); BCG analysis. Note: OTC = Over-the-counter drugs and supplements.

¹Question: “To what extent do you agree with the following statement: I rarely switch brands for the [category] I buy, even if there were better offers for other brands.” (Results shown for all who do not “Disagree.”) ²Question: “What were the reasons that influenced your decision during your last purchase of [allocated category]?” ³Question: “Thinking of the last time you purchased [allocated category], which of the following best describes your choice of brand?”

# Sustainability Is Losing Momentum

As value rises in importance, sustainability has become less influential in purchase decisions. The share of consumers who report taking sustainability into account declined by an average of 3 percentage points across categories in 2026 from a year earlier. However, this pullback is not uniform. In categories such as home care, groceries, fashion, and personal care, consumers say they are slightly more likely to consider sustainability in their purchasing decision. (See Exhibit 7.) Willingness to pay a premium though remains stable with 17% of consumers, or one in six, willing to pay a green premium for sustainable products.

EXHIBIT 7 Consideration for Sustainability Has Slightly Decreased  
![](images/c0c166b3fe01a148355ffb0d7117d69464768e15f30deb0bd9a593ce3a388bcb.jpg)  
Sources: 2026 BCG European Consumer Sentiment Survey (April 2026) with 20,093 respondents across 11 countries (\~1,800 responses per country); BCG analysis. Note: OTC = Over-the-counter drugs and supplements.  
$^{1}$ Question: “Being completely honest, how often do you think about sustainability when you make decisions regarding the purchase of [category]?” $^{2}$ Question: “How have your sustainability considerations when purchasing [category] changed over the past year?”, “Net change in consideration” is the difference between those who say it has increased and those who say it has decreased. $^{3}$ Question: “How much less or more would you be willing to pay in [category] products for sustainable alternatives that minimize your climate impact (vs. non-sustainable alternatives)?”

The second-hand market, on the other hand, continues to expand. Nearly half of consumers, or 47%, report that they sometimes, often, or almost always buy second-hand products, rising 4 points since last year. However, the underlying motivation is primarily economic rather than environmental. Among second-hand buyers, 46% cite saving money, 21% cite access to premium brands at lower prices, and just 17% point to sustainability as the primary reason. This shift positions second-hand as a value and “smart consumption” channel, especially among Gen Z and Millennials who are nearly twice more likely to buy second-hand items than older cohorts.

# Digital Channels Are Reshaping Discovery

The use of GenAI tools such as ChatGPT, Gemini, and Copilot in product discovery has quadrupled since 2024, with 8% of consumers reporting they regularly use them. Usage is highest in research-led categories like home appliances (13%) and OTC medicines (11%) and lowest in impulse categories like packaged snacks and beverages (5%).

The fastest-growing discovery channel overall is social media, particularly among younger consumers. Nearly one-third of Gen Z and Millennials, or 32%, use Instagram, and 27% use TikTok to find and research fashion, compared with 11% and 6%, respectively, for older consumers. Influencer and celebrity recommendations matter to 15% of younger consumers in fashion and

personal care versus 3% for older generations. Both GenAI and social media are growing at the direct expense of general internet search, which is flat to declining across every category.

Stores remain significant for closing the sale, with 40% of consumers ranking them first in influencing their final purchase decision. So while discovery increasingly happens online, stores remain vital for conversion.

## Focus on Growth and Execution

The findings of this survey show that consumer brands do not need a fundamental strategic reset. The trends identified in 2025 have persisted in 2026, confirming that the shifts in consumer beliefs and behaviors are more structural than temporary. The agenda sharpens around four priorities. (See Exhibit 8.)

![](images/1dc85958eb31b8b5b2eb745d51f0619918ebc28b2e41096ef647d56b83c5d5b4.jpg)  
$^{1}$ More relevant for grocery, personal care, beverages, and pet care, where health and wellness are growing trends.

Creating structural value is essential as value remains the primary purchase driver and consumers continue seeking deals. Brands should cut costs aggressively to deliver better value to consumers who are trading down or switching for a better price. Brands should maintain promotional investment but use AI to optimize how that spend is deployed to maximize ROI. In the medium term, brands should direct innovation investments toward functional innovation as consumers report prioritizing functionality over aesthetics or branding.

Aligning new demand generation with Gen Z and Millennials is critical as they will drive a disproportionate share of future growth. Brands should redirect their marketing spending and rebuild go-to-market capabilities to win younger consumers, who have significantly less brand commitment. Brands should integrate flexible ownership models—including rental, subscription, resale, and financing options—given younger consumers’ willingness to buy second-hand goods. Companies can also promote loyalty and rewards programs to build relationships early with younger consumers.

Capturing share in the growing health segment, because it is one of the few areas where spending remains resilient. Brands should rebalance their portfolio toward health-aligned SKUs and prepare for the structural demand shifts that GLP-1 adoption will accelerate. Brands should assess M&A opportunities to move into health-adjacent categories and align marketing with targeted health-oriented messaging. Consumers respond to specific functional benefits over generic positioning.

Winning the digital discovery journey requires investing in the channels that are leading product discovery. Social media is the primary discovery channel for younger consumers. Brands should optimize content and invest in discovery-to-purchase pathways to convert at the moment of highest intent, including in-app checkout and affiliate links. Brands should be relevant in GenAI queries, as consumer usage in product discovery has quadrupled in two years while traditional search has declined. E-commerce continues to be a high-growth purchase channel and warrants sustained investment.

# Explore how these consumer trends are playing out at the country level.

<table><tr><td>Denmark</td><td>Finland</td><td>France</td></tr><tr><td>Germany</td><td>Italy</td><td>Norway</td></tr><tr><td>Poland</td><td>Romania</td><td>Spain</td></tr><tr><td>Sweden</td><td>UK</td><td></td></tr></table>

The authors thank Abi Sonnenberg and Martina Scrocco for their contributions. They also acknowledge BCG's Center for Customer Insight, especially Tim Schulz van Endert and Gaby Barrios, for their support and NativeResearch for conducting the survey.

## About BCG's Center for Customer Insight

Boston Consulting Group's Center for Customer Insight (CCI) applies a unique, integrated approach that combines quantitative and qualitative consumer and citizen research with a deep understanding of business strategy, competitive dynamics as well as public policy context. The center works closely with BCG's various practices to translate its insights into actionable strategies that lead to tangible economic impact and improved public outcomes for our clients across both the private and public sector. In the course of its work, the center has amassed a rich set of proprietary data on consumers and citizens from around the world, in both emerging and developed markets. The CCI is sponsored by BCG's Marketing, Sales & Pricing practice and Global Advantage practice. For more information, please visit the Center for Customer Insight.

## Authors

![](images/59540b4d01c0b9d306f0c40349701e25e245b3d40d0ea6628bb297ffb5d3376e.jpg)

![](images/2a50e1f0d795dfea5997d3e439619023ce02a03b6dcbe1ee5b5fc243d025b51f.jpg)  
Andreas Malby  
Managing Director & Senior Partner
Copenhagen

## Rohan Sajdeh

Managing Director & Senior Partner
Chicago

![](images/8d5582d7a4690bf6c817fdfc0a05818e6f270cdd160ca6b5e2a4f7f0e6e30245.jpg)  
Nicolas de
Bellefonds  
Managing Director & Senior Partner
Paris

![](images/21beddf8e62881eee48a600fb7cabd4bddd7cf38bc8f46617e1c006bf7c8801e.jpg)  
Vishakha Chopra  
Principal
Johannesburg

## ABOUT BOSTON CONSULTING GROUP

Boston Consulting Group bridges the gap between ambition and outcomes for the world's leading companies and organizations. We are built for this era of unprecedented change — bringing strategic clarity rooted in over 60 years of deep domain knowledge, combined with applied AI shaped by our practitioners. BCG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com.
"""
