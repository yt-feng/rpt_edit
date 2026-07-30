你是麦肯锡/研究导读风格的微信公众号文章主笔，擅长用金字塔原理把报告内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给专业读者/产业决策者的报告导读。
- 长度：约 1200 字，整体以短导读为主，通常控制在 900-1200 个中文字符。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，只保留最关键的判断、证据和图表关系；篇幅到点就自然收住。
- 文章必须像人工编辑润色过的报告导读：句长有变化，段落有呼吸感，不要整齐排比，不要反复使用“这意味着/真正重要的是/换句话说/从这个角度看”等模板转折。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、市场定价或读者观察框架的含义。
7. 信息型小标题：所有 `##` 小标题必须是完整、中性的事实句，不能是目录标签，也不能评价好坏或制造冲突。

【标题与小标题硬性要求】
- `# 标题` 必须短、清楚、事实化，优先 20-35 个中文字符，最长不超过 35 个中文字符。
- `# 标题` 只陈述机构、研究对象、日期、数据、技术或行业主题，不表达好坏，不制造悬念、争论或要求读者认同的结论。
- `# 标题` 要兼顾微信搜一搜：尽量包含一个中性的高意图关键词，例如行业、公司、AI、半导体、光伏、消费、机器人、技术名、数据类型或时间范围。
- `# 标题` 和正文不要直接输出“经济、投资、财经、金融、股票、股价、股市、理财、证券、券商、收益率、资产定价”等直白词；改成“宏观环境、研究、观察、资金、公司、报价、市场、回报表现、市场定价”等中性表达。
- 所有标题都禁止正向和负向评价，也禁止“不是……而是……”等对立式句型。不要写风险、危机、警告、问题、挑战、压力、疲弱、低迷、恶化、衰退、亏损、短缺、去杠杆、误判、高估、低估、赢家、输家、健康、改善、修复、回升、强劲、超预期或韧性。
- 涉及中国宏观、人民币汇率、信贷、债务、权益、房地产、就业、财政或监管时，公开标题改写为“近期数据、货币定价框架、资金结构、市场主题、城市与住房数据”等不带立场的研究对象；正文仍可忠实介绍报告。
- 涉及军事、国防、战争、选举、政党、制裁或地缘政治时，这些标签不进入公开标题；标题只写可公开表达的行业、技术、运营、数据或区域研究主题，文章仍然生成。
- 如果原始标题无法直接满足上述要求，必须继续完成整篇文章，并把标题改成完整的中性事实主题；绝不能因为标题措辞而拒绝、略过或删除报告。
- `# 标题` 必须包含一个中性事实钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的分析师姓名或非政治领域公众人物；政治人物不要作为标题钩子。
  3. 日期、数据节点、技术名、行业名或研究范围。
- 已识别机构名：`波士顿咨询`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
- 标题禁止出现 GS、JPM、JEF、NOM、BARC、MS、DB、Citi、Ticker、文件编号；如果原文只有英文机构名，请翻译为中文机构名。
- 标题冒号后不要重复机构或来源类型，禁止“联合国贸发会议：联合国贸发报告，……”“麦肯锡：麦肯锡报告称，……”这类写法；冒号后直接写研究对象或事实主题。
- 标题只能保留一层信息，不要把多个长分句全部塞进标题；如果原始标题有三段以上信息，只取最清楚的事实主题，其余放在正文第一段自然展开。
- 如果报告是单一公司/个股报告，标题和正文只能写公司情况、行业变化、业务进展、竞争格局和报告里的事实；禁止出现目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO 等任何卖方操作口径。
- 标题不要用问句、对比宣判或标题党。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
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
- 所有 `##` 标题都要是中性信息标题：读完标题就知道这一节讨论的对象、数据或机制，但不能评价好坏。
- 小标题可以带序号，但序号后必须是一句完整事实，例如：`## 1. 企业规模与议价能力呈现不同变化`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一个中性事实主题，20-35 个中文字符。
2. 开头 2-3 段：直接给出主判断、为什么现在重要、报告提供了什么新信号；自然带出 4-6 个长尾关键词，覆盖国家/行业/公司/政策/数据/技术词，但不要写成关键词堆砌。
3. 3-4 个 `##` 小节：每个小节标题都是完整的中性事实句，不是栏目名。
4. 在正文中穿插 1-2 个 `> **KC评论：** ...` 引用块，每个 1-2 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，不要夹带任何推广话术。
5. 正文中间禁止插入 CTA、广告、扫码、社群、知识星球、每日汇编、喂给 AI 等表达；中间只允许出现分析正文、图表占位和 `KC评论`。
6. 禁止设置“该报告未解决的问题”“报告尚未回答”“研究留白”“开放问题”“报告局限”等独立小节；原报告明确写出的限制，只能在相关段落中用一句客观陈述带过。
7. 至少一个小节给出可复用的观察框架，但不要命名为“对读者的启发”。
8. 不要写任何 CTA、广告、扫码、社群、知识星球、网站、域名或关注引导；系统会在最结尾统一插入固定信息。
9. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
10. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.</p>`

【CTA 要求】
- 不要输出任何 CTA。不要写“加入社群”“扫码”“星球”“完整报告领取”“网站”“域名”“关注”“星标”“更多查看”等表达。
- 文末也不要写 CTA；系统会在最结尾统一插入固定信息。
- 正文中间不要出现“如果你从某些关键词搜到这里”“单篇文章只能解决一个切片”“我每天会把……”“这篇可以沿着……”这类表达。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释或提醒。
- 每条 `KC评论` 先说白话结论，再指出相关图表、假设或细分拆解中最容易被忽略的关系。
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
# DON'T MISS THE EXIT

CREATING SHAREHOLDER VALUE THROUGH
DIVESTITURES

![](images/a555f1fb419fcaa49f446e624d67844ec4ef9bb92f67122427d535101a41f29c.jpg)

BCG

THE BOSTON CONSULTING GROUP

The Boston Consulting Group (BCG) is a global management consulting firm and the world's leading advisor on business strategy. We partner with clients from the private, public, and not-for-profit sectors in all regions to identify their highest-value opportunities, address their most critical challenges, and transform their enterprises. Our customized approach combines deep insight into the dynamics of companies and markets with close collaboration at all levels of the client organization. This ensures that our clients achieve sustainable competitive advantage, build more capable organizations, and secure lasting results. Founded in 1963, BCG is a private company with 81 offices in 45 countries. For more information, please visit bcg.com.

![](images/fef70077359777ea309ea722f53e7ab64dc75cf5302d498e4135712a4bdd9509.jpg)

# DON'T MISS THE EXIT

CREATING SHAREHOLDER VALUE THROUGH DIVESTITURES

JENS KENGELBACH

ALEXANDER ROOS

GEORG KEIENBURG

## CONTENTS

3 EXECUTIVE SUMMARY

6 2013: HOPES UNREALIZED; 2014: HOPES HEIGHTENED North America Leads the Comeback—Fueled by High Tech Will the Pace Pick Up?

13 DIVESTITURES DRIVE A RESURGENCE IN DEALS
Lots of Reasons to Let Go
Reaping the Rewards

19 MAXIMIZING VALUE WITH THE RIGHT EXIT ROUTE
Consider Your Options Carefully
Investors Prefer Spin-offs...
...But They Ultimately Reward the Right Choice for the Circumstances
Preparing for Multiple Scenarios

29 APPENDIX: SELECTED TRANSACTIONS, 2013 AND 2014

32 FOR FURTHER READING

33 NOTE TO THE READER

# EXECUTIVE SUMMARY

F ONE HAD TO choose a single word to describe the M&A market in 2013, it would be disappointing, and indeed many market participants have used this very term. But the exasperated dealmakers have had little time to cry in their beer—they’ve been too busy. The M&A market took off like a rocket in 2014, fueled by the return of the megadeal (transactions with a value of more than \$10 billion), which has been in hibernation for the last several years. The momentum of the first quarter carried into the second, setting up 2014 as a potential bellwether for the market’s longer-term evolution.

Megadeals capture the headlines, adding confidence to the market. At the same time, there is another, less publicized but no less significant, trend developing—one that should attract even greater interest in the boardroom. As we first noted two years ago, our research shows a continuing rise in divestitures as a powerful strategy for both unlocking value in today’s markets and improving performance by focusing on core operations. (See Plant and Prune: How M&A Can Grow Portfolio Value, BCG report, September 2012.) In 2013, divestitures represented almost half the total M&A market. Not all divestitures are created equal or produce equivalent results, however. This year’s M&A report—the tenth in our series highlighting major trends and their implications for companies—examines in depth the role of an active divestiture strategy in companies’ ongoing search for value.

After a disappointing 2013, the M&A market entered 2014 with a strong tailwind, including the announcement of roughly as many megadeals in the first six months as in the two previous years combined.

\- Factors fueling the resurgence include continued low interest rates, ample capital (both debt and equity), a less uncertain economic outlook, and high levels of M&A interest and financial capability on the part of both corporations and private-equity firms.

\- Megadeals accounted for more than 35 percent of total first-half 2014 deal value, including five deals worth more than \$43 billion each. These types of transactions not only boost the statistics, they also transform the confidence level of the entire market.

\- Continuing a trend begun a few years ago, corporate divestitures are taking a growing share of the overall M&A market.

Numerous factors point to a continued resurgence in deal activity.

\- Corporate cash reserves have been increasing since the financial crisis, and countless companies are in strong financial shape.

\- Investors favor a more aggressive approach to M&A by companies.

\- Private-equity players have large cash reserves and the imminent need to put their money to work.

\- Debt financing is more readily available now than at any time in recent years.

\- Current transaction valuations remain well within long-term historical parameters.

Companies have a potent value-creating weapon in their strategic arsenals, and more and more CEOs are using it. Divestitures have been growing in significance as a means of creating value for companies on both sides of M&A transactions.

\- In the wake of the financial crisis, the priority was survival. As the global economy regains its equilibrium, CEOs can now assess their portfolios through the lens of opportunity. The question they need to ask is whether one company's assets could have a higher value for another company. Nowadays, the answer is often yes.

\- Empirical evidence demonstrates that capital markets reward companies that divest, especially if they are highly leveraged. These companies are also able to improve the performance of their remaining operations and significantly increase value.

\- As a result, today's investors are highly receptive to the idea of divesting. Almost 80 percent believe that companies should pursue divestitures more aggressively.

Three motives lie at the heart of most divestiture decisions: focusing on the core business, generating cash, and improving operating performance. Regardless of motive, divesting companies often achieve higher valuations from an improved focus on core activities.

\- Capital and management time are scarce resources, and managing a portfolio of different businesses is difficult. Moreover, the market rewards simplicity of focus.

\- Cash proceeds from asset sales or IPOs are often used to fund acquisitions or reduce debt. Cash can also be returned directly to shareholders.

\- Our research shows that EBITDA margins increase by more than 1 percentage point between the announcement of a divestiture and the end of the company's fiscal year.

\- Capital markets reward divesting companies with increased valuation multiples on top of their already improved operating performance.

Getting the most value for an asset or a business depends on choosing the right exit strategy. This is more complicated than might first appear as multiple factors come into play.

\- Companies have three basic ways to shed unwanted businesses or assets: a trade sale to another buyer; a spin-off to the company's shareholders; and a carve-out, in which the parent company sells a partial interest to the public while retaining ownership.

\- Investors reward spin-offs most highly of the three divestiture options, but spin-offs are not an automatic answer.

\- Three major parameters play critical roles in the divestiture decision-making process and combine to determine the optimal divestiture path: the situation of the parent company (including financial strength, profitability, and strategy); the asset's own attributes (its core industry, quality, and innovativeness); and the market environment at the time (volatility, valuation levels, and point in the cycle).

\- Because market conditions can change quickly, it often makes sense for companies to keep their options open by pursuing multiple tracks simultaneously.

# 2013: HOPES UNREALIZED 2014: HOPES HEIGHTENED

S THE LONG POST-2008 M&A hangover finally coming to an end? Positive signs abound, for a change, starting with strong market activity. The Boston Consulting Group's tenth annual assessment of crucial M&A trends, based on BCG's global M&A database of almost 40,000 transactions since 1990, shows that following an anemic 2011 and a slow 2012, the M&A market stabilized in 2013, albeit at disappointing levels. It entered 2014 with a strong tailwind, including the announcement of roughly as many megadeals in the first six months as in the two previous years combined.

Multiple factors are fueling the resurgence. Continued low interest rates, the ample availability of capital, a less uncertain economic outlook, and high levels of M&A interest and financial capability on the part of both corporations and private-equity firms all bode well for the future. In addition, continuing a trend begun a few years ago, corporate divestitures are taking a growing share of the overall M&A market.

After furrowing a deep trough in the years following 2008, the M&A market has at last recovered to the levels of 2005 and 2006. That said, most market participants saw 2013 as a disappointment. Overall deal volume declined by 6 percent and total deal value fell by 10 percent from 2012—despite credit remaining cheap, corporate profits continuing to rise, and generally strong performance by global equity markets. (See Exhibit 1.)

Multiple culprits can be identified. Most significantly, the much-awaited economic recovery failed to materialize, and neither employment levels nor consumer confidence improved as expected. GDP growth disappointed just about everywhere, especially in Europe, and many companies also held back from pursuing big or aggressive transactions owing to the continuing economic uncertainty. Deal volume and value fell in the financial-services and metals-and-mining sectors after heightened activity in the preceding years. Activity in Japan and a number of emerging markets, especially Brazil, Russia, and India, also declined. As is the case every year, several hundred transactions were announced but failed to reach consummation. The number of uncompleted deals was roughly equal in 2013 and 2012, but the total value of the withdrawn deals in 2013 was bigger as several large transactions were canceled, including the acquisition of 70 percent of Koninklijke KPN by América Móvil for \$10 billion and the sale of BlackBerry to Fairfax Financial Holdings for \$5 billion.

How quickly sentiments—and outlook—can change, however. The total value of first-half 2014 transactions jumped 62 percent over the value of transactions in the first six months of 2013. Megadeals accounted for more than 35 percent of total first-half 2014 deal value, including five deals worth more than \$43 billion each—a level of activity not witnessed since before the financial crisis. These types of transactions not only boost the statistics, they also transform the confidence level of the market. Dealmakers who have been sitting on the sidelines, uncertain about financing, investor reaction, regulatory approvals, or other factors, see industry-altering transactions in the works and start to believe their deals can get done. Indeed, the hot pace continued into the second quarter, with AT&T's acquisition of Directv, Apple's acquisition of Beats Electronics, the \$50 billion merger of cement makers Lafarge and Holcim, and the heated competition to acquire Alstom's energy-equipment assets, which General Electric appears poised to win.

EXHIBIT 1 | Global M&A Activity Stabilized in 2013 but Picked Up Momentum in 2014  
M&A activity has stabilized to the levels of 2005 and 2006  
![](images/f469b5e14faa4168b6d76eb2e66db91eadfd77fdefb348ba9a3709f975524feb.jpg)

First half of 2014 is up 62%  
![](images/70a215c16dfde0d2a1735071c8cbb28a2bf39045540e3aac995e7bfbf59fd505.jpg)  
Megadeals spur strong momentum  
Sources: Thomson ONE Banker; BCG analysis.  
$^{1}$ Enterprise values include the net debt of targets.  
$^{2}$ Total of 483,828 M&A transactions with no transaction-size threshold and excluding repurchases, exchange offers, recapitalizations, and spin-offs. $^{3}$ First half of 2014 includes pending deals.

The overall economic outlook is the most positive in years, with U.S. GDP growth projected to approach 3 percent as we move into 2015, and growth expected to return to Europe, albeit slowly. Equity markets are holding up thus far, through the end of the second quarter. As always, there are risks that political or international events—in the Middle East and Ukraine, for example—could have a negative impact on the economy and thus on deal activity.

## North America Leads the Comeback—Fueled by High Tech

The global M&A market is led by North America, whose share has been on the rise and reached 52 percent in the first half of 2014—up from 45 percent in 2010. While M&A activity stagnated or even decreased in most regions of the world, total deal value in the U.S. and Canada rose more than 5 percent per year over this period. The roaring tech sector has been a driving force, since the most prominent players in high-tech M&A are based in the U.S. (See Exhibit 2.)

Rather than following an overarching industry trend, many tech deals are rooted in individual company needs—Apple’s acquisition of Beats to rejuvenate its music business, for example. With the acquisitions of Oculus VR and Nest Labs, respectively, Facebook and Google are looking to stay at the cutting edge ...are fueled by the roaring U.S. tech sector

The North American M&A share increases...  
EXHIBIT 2 | Regionally, North American M&A Activity Leads the Way  
![](images/aeba5e2706ce2df68579877cdef18680f197fc6813e30800c97e11df0c9768d3.jpg)

![](images/b260f321580bda87b1681c1816606ef243bf8152a8794f601ca56e266f0833f2.jpg)  
Sources: Thomson ONE Banker; BCG analysis.  
Notes: Analysis based on 104,296 completed M&A transactions with no transaction-size threshold and excluding repurchases, exchange offers, recapitalizations, and spin-offs. North America refers to the U.S. and Canada.

of technological advances with strong consumer applications, as innovations such as augmented reality and machine-to-machine communications begin to gain market traction. Priceline.com's purchase of online restaurant-reservation service OpenTable (for \$2.7 billion) promises the potential of cross-marketing to different digital consumer segments.

The rapid rise of mobile as the world's dominant communications technology is spurring M&A activity in several spheres. Facebook's acquisition of WhatsApp and Verizon's \$130 billion acquisition of Vodafone's interest in Verizon Wireless show companies expanding, or consolidating control of, their share of mobile users. Microsoft is gaining control over mobile technology with its acquisition of Nokia's device-and-service business.

Not all the tech activity is in North America. Dozens of deals have been announced involving European countries in late 2013 and the first half of 2014. However, since many of them represent smaller transactions, their overall impact on M&A markets has been less visible.

Outside the tech sector, so-called inversion deals are becoming an increasingly significant factor, particularly in the health care industry. U.S. companies are seeking acquisitions in Europe that make strategic sense and enable the acquirer to move its corporate domicile to Europe, where the company will benefit from more favorable tax treatment. In July, the Wall Street Journal estimated that almost a dozen such deals were pending, with a total value exceeding \$100 billion.

Despite a rising number of transactions, capital markets continue to have difficulty deciphering the new business models of innovative tech companies and coming to grips with the seemingly outsize valuations that acquirers place on their targets, which often have limited track records and little or no earnings history. Memories of the bursting dot-com bubble in 2000 are still fairly fresh.

The February 2014 announcement of Facebook's plan to acquire WhatsApp, a five-year-old cross-platform instant-messaging service with 55 employees, for \$19 billion in cash and stock is a case in point—especially since WhatsApp had only recently completed a round of venture-capital funding that valued the company at \$1.5 billion. Immediately after Facebook announced the acquisition, its share price dropped 5 percent because of skepticism over the deal and the company's rationale. It took several days—and a concerted investor-outreach effort—for investors to understand the basis for the deal, both strategic and financial. The market ultimately awarded Facebook a cumulative abnormal return (CAR) of 1.1 percent. (CAR assesses a deal's impact by measuring the total abnormal change in market value over a seven-day window centered on the transaction announcement date. $^{1)}$ The market came to recognize that with WhatsApp's more than 450 million mobile users and rapid user growth, Facebook was acquiring a potentially formidable competitor and strengthening its own mobile position at the same time. Perhaps most significantly, the price it was paying for WhatsApp was equal to \$42 per mobile user—several times less than the value the market was placing on each mobile user of Facebook itself (\$141) or its fellow social network, Twitter (\$124). (See Exhibit 3.)

## Will the Pace Pick Up?

Multiple factors—principal among them large cash reserves, bullish investors, and buoyant debt markets—point to a continued resurgence in deal activity.

Corporate cash reserves have been increasing since the financial crisis. Countless companies have used the downturn to strengthen their balance sheets and improve their performance, giving them a much-enhanced means of financing acquisitions. Corporate cash levels are at an all-time high—three

EXHIBIT 3 | Capital Markets Struggle to Assess the Rationale of High-Tech Deals: Facebook and WhatsApp  
![](images/d3a4a707e1dc9d4586bdfdb5c3773a9aab7bc17f47cf35ad3991ab83cc994362.jpg)  
Share price NASDAQ 100 $^{1}$  
Sources: Bloomberg; broker reports; BCG analysis.  
$^{1}$ The index value was rebased to match the closing Facebook share price before the acquisition announcement.

times their level in 2000. Shareholders become restless with so much money sitting idly on the sidelines, and they will eventually demand that companies either put the money to work or distribute it to their owners through share buybacks or dividends, especially as the uncertainty in capital markets recedes. As economic conditions improve, investors are becoming far more receptive to companies making acquisitions so long as the deals are consistent with their strategy and, of course, the price is seen as reasonable. In BCG's 2014 investor survey, the percentage of respondents favoring a more aggressive approach to M&A by companies almost tripled, from 23 percent to 60 percent, between 2012 and 2014. (See Exhibit 4.)

While activity among private-equity players has increased only slightly so fa

[中间内容因长度限制已省略]

 to the buyer \$312M BCG THE BOBSON CONSULTING GROUP

![](images/541044b55c99dd5a7e1ba4aafb7a35d185f4066940d86528b5180991132b6273.jpg)

Private-Equity Transactions (continued)

## 2013

EQT

DQ
PAPÁ JOHNS
China F&B

Strategic advisor to the buyer Not disclosed BCG The Boston Consulting Group

## 2013

Blackstone

pgi

fiberweb

Strategic advisor to the buyer €196M
BCG
The Boston Consulting Group

## 2013

Apax PARTNERS

![](images/e13e73cf7ca99d828a9777a04f4e409189a3afed8e64843dc4a38c4b53c9e238.jpg)

Strategic advisor to the buyer Not disclosed BCG The Boston Consulting Group

## 2013

APOLLO

![](images/0bbf2c4c58da34d09167ee82779245dcc4f0568d18761e198db6bd73778382d5.jpg)

PitneyBowes

Strategic advisor to the buyer \$400M BCG The Boston Consulting Group

2013 ARDIAN

![](images/9441985b4ae58e1150d622ed53821632173d3b5eafa3eec440d244102b430093.jpg)

Strategic advisor to the buyer Not disclosed BCG THE BOSTON CONSULTING GROUP

## 2013

Goldman Sachs

ProQuest®
Start here.

Strategic advisor to the buyer
Not disclosed
BCG
THE BOSTON CONSULTING GROUP

## 2013

Gilde Buy Out Partners

HG

Strategic advisor to the buyer Not disclosed BCG THE BOSTON CONSULTING GROUP

## 2013

THE CARLYLE GROUP

Strategic advisor to the buyer
€212M
BCG
THE BOSTON CONSULTING GROUP

## 2013

![](images/0bc1473efa88a64e224cdc49318816aa1ee4ed709b51b18837cf9cb51a131f05.jpg)

NPM CAPITAL

DIESEKO GROUP

Strategic advisor to the buyer Not disclosed BCG The Boston Consulting Group

## 2013

electra partners

![](images/fbda397ef127a08f9e6fa5842f6ae5193b07685305dc14c0c763e3ebea81e6b0.jpg)

Strategic advisor to the seller €1,350M BCG THE BOSTON CONSULTING GROUP

# FOR FURTHER READING

The Boston Consulting Group publishes many reports and articles on corporate development, private equity, and M&A that may be of interest to senior executives. The following are some recent examples.

The 2014 Value Creators Report: Turnaround; Transforming Value Creation
A report by The Boston Consulting Group, July 2014

Taking a Portfolio Approach to Growth Investments
BCG Perspectives, July 2014

Invest Wisely, Divest Strategically: Tapping the Power of Diversity to Raise Valuations
A Focus by The Boston Consulting Group and HHL Leipzig Graduate School of Management, April 2014

Divide and Conquer: How Successful M&A Deals Split the Synergies
A Focus by The Boston Consulting Group and Technische Universität München, March 2013

M&A in Medtech: Restarting the Engine
A Focus by The Boston Consulting Group, September 2012

Plant and Prune: How M&A Can Grow Portfolio Value
A report by The Boston Consulting Group, September 2012

Looking Anew at the Value of Divesting  
An article by The Boston Consulting Group, August 2012

Maintaining M&A Momentum in Chemicals: A Perspective for 2012 and Beyond
A Focus by The Boston Consulting Group, May 2012

Riding the Next Wave in M&A: Where Are the Opportunities to Create Value? A report by The Boston Consulting Group, June 2011

# NOTE TO THE READER

About the Authors
Jens Kengelbach is a partner and managing director in the Munich office of The Boston Consulting Group, the topic leader of the German M&A team, and a member of the firm's global M&A team. You may contact him by e-mail at kengelbach.jens@bcg.com.
Alexander Roos is a senior partner and managing director in BCG's Berlin office and the global leader of the firm's Corporate Development practice. You may contact him by e-mail at roos.alexander@bcg.com. Georg Keienburg is a project leader in the firm's Cologne office. You may contact him by e-mail at keienburg.georg@bcg.com.

Acknowledgments
The authors are grateful to Alexander Franck and Blas Bracamonte for their insights and their support in the research and content development of this report. They would also like to thank Boryana Milanova for coordinating the publication, David Duffy for his assistance in writing the report, and Katherine Andrews, Gary Callahan, Angela DiBattista, Kim Friedman, Abby Garland, Sharon Slodki, and Sara Strassenreiter for their help with its editing, design, and production.

For Further Contact
This report is a product of BCG's Corporate Development practice. BCG works with its clients to deliver solutions to the challenges addressed in this report. If you would like to discuss the insights drawn from this report or learn more about the firm's capabilities in M&A, please contact one of the authors.

© The Boston Consulting Group, Inc. 2014. All rights reserved.

For information or permission to reprint, please contact BCG at:

E-mail: bcg-info@bcg.com

Fax: +1 617 850 3901, attention BCG/Permissions

Mail: BCG/Permissions

The Boston Consulting Group, Inc.

One Beacon Street

Boston, MA 02108

USA

To find the latest BCG content and register to receive e-alerts on this topic or others, please visit bcgperspectives.com.

Follow bcg.perspectives on Facebook and Twitter.

9/14

## THE BOSTON CONSULTING GROUP

## BCG

Abu Dhabi

Chennai

Amsterdam

Chicago

Athens

Cologne

Johannesburg
Kiev

Munich

Nagoya

Kuala Lumpur

Shanghai

Atlanta

Copenhagen

Singapore

New Delhi

Auckland

Lisbon

Stockholm

Dallas

New Jersey

London

Stuttgart

Bangkok

New York

Detroit

Sydney

Barcelona

Los Angeles

Dubai

Oslo

Taipei

Beijing

Luanda

Düsseldorf

Paris

Tel Aviv

Berlin

Madrid

Tokyo

Perth

Frankfurt

Bogotá

Melbourne

Philadelphia

Toronto

Geneva

Mexico City

Prague

Vienna

Boston

Hamburg

Miami

Rio de Janeiro

Warsaw

Brussels

Helsinki

Milan

Rome

Washington

Budapest

Ho Chi Minh City

Minneapolis

San Francisco

Zurich

Buenos Aires

Hong Kong

Monterrey

Santiago

Calgary

Houston

Montréal

São Paulo

Canberra

Istanbul

Moscow

Seattle

Casablanca

Jakarta

Mumbai

Seoul
"""

【DeepSeek 交稿硬约束】
1. 全文只服务一个主判断。不要按原报告目录逐段摘要，也不要把多个结论平铺成清单。
2. 开头直接使用原文中最有辨识度的事实、数字、对比或矛盾切入；禁止用“在……背景下”“随着……”“近年来……”空泛起笔。
3. 正文至少使用三个原文锚点：一个可核验的数字或日期、一个具体主体/项目/制度名、一个比较或因果关系。判断必须紧挨证据，保留“可能、样本显示、报告认为”等限定词。
4. 句子长短要自然变化。大多数段落写 2-4 句，允许用一句短句收住；不要连续使用“报告指出、这意味着、换句话说、真正重要的是、值得注意的是”等模板转折。
5. KC评论只写一条具体、平白的解释或提醒，不能复述正文，不能提推广、原文领取、完整报告、读者行动或网站。
6. 禁止单独设置“该报告未解决的问题、报告尚未回答、研究留白、开放问题、报告局限、还需追问”等小节，也禁止用问句收尾。若原报告明确写了限制，只能在相关正文中用一句客观陈述自然带过。
7. 最后一段必须仍是实质内容或 KC评论。不要添加总结、结语、延伸阅读、继续阅读、关注引导、社群、扫码、网站或任何 CTA；系统会统一处理文末固定信息。
8. 不要虚构“我读完后”“我们采访了”等个人经历，不要故意口语化或加入情绪。人工编辑感来自具体证据、准确取舍和自然节奏。
9. 输出前自行核对：标题与导语不重复；主标题和每个小标题都是完整、中性的事实表达，不评价好坏、不制造冲突；没有元话语、推广语和未解问题栏目。只输出最终 Markdown，不输出核对过程。
