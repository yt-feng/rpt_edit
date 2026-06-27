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
- 已识别机构名：`摩根斯坦利`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
MS & CO. LED
Sean Diffley, CFA
Equity Analyst
Sean.DIFFLEY@morganstanley.com +1 212 761-5868
Brian Nowak, CFA
Equity Analyst
Brian.Nowak@morganstanley.com +1 212 761-3365
Erik W Woodring
Equity Analyst
Erik.Woodring@morganstanley.com +1 212 296-8083
Daniel Duran
Equity Analyst
Daniel.Duran@morganstanley.com +1 212 761-4822
Patrick A Ho
Equity Analyst
Patrick.Ho@morganstanley.com +1 212 761-2764
Erica Crouser
Data Analyst
Erica.Crouser@morganstanley.com +1 212 761-4807

June 25, 2026 09:18 AM GMT

AI & The Entertainment Industry | North America

# 16th Annual Streaming Survey, More Is More

Our 16th annual survey of \~3K American consumers suggests a competitive, but growing streaming landscape with AMZN Prime, NFLX & GOOGL's YouTube showing the strongest engagement & stickiness. The ave HH has >5 services and watches \~3 hours of content per day, while Sports are increasingly streamed.

AlphaWise α

## Key Takeaways

Nearly $90\%$ (21 of 24) of entertainment services surveyed saw y/y increases in engagement this year, while the big continue to get bigger (AMZN, NFLX & GOOGL/YT)

NFLX continues to have the strongest net retention score and is perceived to have the best original content, despite investor concerns over engagement

DIS's ESPN remains the dominant sports platform, while Disney+ and Hulu saw solid increases in engagement

\- Paramount+ and HBO Max scored best on having people's favorite TV shows, which bodes well for the pro forma PSKY+WBD

■ META is gaining traction in video with Facebook & Instagram Reels showing the largest y/y increases in engagement across platforms

## Top 10 takeaways from our 16th annual Alphawise streaming survey:

1. More services, more hours... the average US HH has >5 streaming services including free (5.4 vs 4.9 last year) with 3+ paid subscriptions (up to 3.2 from 3.1 last year, see Exhibit 25) & watches \~3 hours per day of TV, movies and online videos (with older cohorts skewing higher, see Exhibit 26 - Exhibit 27).

2. Distribution at scale is the holy grail... Amazon Prime Video (+264bps y/y to 66%), Netflix (+352bps y/y to 55%) and YouTube (+476bps to 47%) remain the 3 dominant streaming platforms w/ penetration up y/y (see Exhibit 1).

3. DIS & PSKY+HBO solid engagement... Disney+/Hulu also saw y/y increases (+100-200bps y/y) to 36/38%, while Paramount+ and HBO Max were also up >200bps y/y to 28/27%, which bodes well for the pro forma PSKY+WBD (see Exhibit 1).

4. Everything is TV... IG/FB Reels & TikTok see largest y/y increases... Social platforms saw the largest y/y gains on self-reported usage for entertainment with META's Instagram/Facebook Reels and TikTok up >1,000bps y/y, as these platforms push harder into short-form video with more long-form coming, which is increasingly

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

competing with TV time (see Exhibit 1). We are also monitoring micro dramas as an emerging category taking more time spent for younger consumers.

5. NFLX, followed by AMZN & HBO for "best" original programming... Netflix is perceived to have the best original programing (+360bps y/y to 31%) after declining the last few years (see Exhibit 9), while Amazon Prime (+72bps to 17%) and HBO Max (+260bps to 7%) also saw steady gains (see Exhibit 8); Netflix scores best on adding content that people like and having a broad selection, while Paramount+ and HBO Max scored best on having people's favorite TV shows (see Exhibit 10). Users approach Netflix with higher intentionality, typically launching the platform with a specific title in mind (see Exhibit 12) and with higher attention than other services (see Exhibit 14), leading to higher "quality" engagement (Exhibit 15). Meanwhile, Disney+, Peacock and YouTube are often the destination for browsing and/or background entertainment.

6. Ad-tier adoption increasing... The Netflix ad-tier continues to gain traction rising to 26% (from 22% last year) of total respondents, while those without ads held steady at \~30% suggesting that ad-supported offerings are more incremental than cannibalistic (see Exhibit 28).

7. YT TV most popular vMVPD... Google's YouTube TV is the most preferred vMVPD with strong y/y gains (\~30%), followed by Hulu+ Live TV (\~20%), while Charter's video push does appear to be bearing fruit (see Exhibit 22 - Exhibit 23).

8. Sports biggest live draw, increasingly streamed... >60% of people regularly watch Sports live on TV (although this is down y/y to 62% vs 65% last year) and those viewing naturally indexes higher among pay-TV users (>70%), although \~30% of those not using pay-TV report regularly watching live sports content (see Exhibit 40 - Exhibit 41).

9. DIS/ESPN remains top stop for sports... Disney's ESPN remains the dominant channel/platform for watching sports (31% vs 30% last year) with a modest bump after launching ESPN Unlimited (see Exhibit 42), meanwhile Amazon is making strides coming in at #2 (22% vs 17% last year) likely helped by the NFL/TNF and Netflix moved up a few notches (12% vs 10% last year).

10. Starz and AMC+ remained at the bottom of the self-reported usage scale and also had the weakest net retention scores, while Apple TV+ engagement was down y/y (see Exhibit 1), but did score well on quality of engagement (high primary focus & destination marks).

We remain Overweight DIS, NFLX & PSKY, Equal-weight WBD & STRZ, and Underweight AMCX.

## Spotlight on Netflix

Netflix sentiment has deteriorated (down -23% YTD, market cap down >\$130bn since WB deal announced on Dec 5) driven by: 1) concerns around engagement growth slowing and a lack of recent break-through new content; 2) less margin expansion than historical (\~200bps vs \~300bps); 3) AI positioning uncertainty (on the notion that UGC platforms are better positioned); 4) concerns of elevated churn / unfavorable seasonality; and 5) an M&A discount post WB S&S interest.

Despite investor concerns around engagement and pricing power, Netflix showed the strongest net retention score of all video streaming services (+18 = 36% to cancel last – 18% to cancel first), followed by YouTube Premium and Amazon Prime Video.

While Netflix recently increased prices, the value perception remains strong with most thinking that the current standard ad-free plan pricing at \~\$20 per month is a 'great buy for the money' while they have room to >\$30 per month before it is perceived to be 'getting expensive' and would give some thought to subscribing.

## The HBO Max/Paramount+ Super Service

Key to our OW rating on PSKY is its ability to merge Paramount+ and HBO Max into a unified profitable "super service". Survey results below are encouraging, with only 10% of HBO/Para+ subs very unlikely or somewhat unlike to subscribe to the new super service. Even more, \~40-50% of non-HBO/Para+ subs would reportedly sign on to the super service (Exhibit 17 - Exhibit 18). Per the survey, there's a \~28% overlap in HBO/Para+ subscribers vs MSe \~25-30%.

## Streaming Service Adoption

Amazon Prime Video, Netflix, and YouTube (free) continue to lead the pack among video streaming platforms, used by 66%, 55%, and 47% of respondents, respectively. Platform adoption is up YoY overall, with the average respondent subscribing to 5.4 free or paid services (vs. 5.0 last year).

Exhibit 1: Paid streaming service user penetration sees gains YoY  
![](images/21cdf8764546cab2c913a1883539a0b09ef44146046899782a9b896e3b54cdda.jpg)  
Note: \* Netflix, HBO Max, Disney+, Hulu, Paramount+, and Amazon Prime Video reflect each respective service with or without ads.  
Source: AlphaWise, MS

## Share of Time

Exhibit 2: Among total TV/video watchers, AMZN, NFLX, and YT lead on SVOD share of time  
![](images/9147efc553fc9c32d3dbec6b4742b0c1c8805e4ebab529fa1687d8e346f252db.jpg)  
Source: AlphaWise, MS

Exhibit 3: Pay TV subs spend 43% of their watching time watching pay TV, suggesting further opportunity for streaming.  
![](images/cfdec3b1856a46647865f4581873403fdbcacd787b47bfac31d9db302fae5f82.jpg)  
Source: AlphaWise, MS

Exhibit 4: Netflix and YouTube get the largest on-platform watching hours/share than other streaming services

![](images/31a470a6db1f414fe77c049c01da48a5018f40bc4022c42b91748c8448aa5b04.jpg)  
Source: AlphaWise, MS

## Quality of Engagement on Streaming Platforms

As video streaming reaches near-ubiquity, platforms are shifting their focus to maximizing retention, quality, engagement, and monetization of their subscriber bases.

Retention: We asked respondents which of their streaming services they would cancel first, if they had to choose, and which would they cancel last. Consistent with other findings from our survey, Netflix, Amazon Prime Video, and YouTube appear to outcompete the rest of the competition – for all three of these platforms, current users were more likely to indicate them as the service they would cancel last than

as the one they would cancel first, implying that they are not easily replaced. The stickiness of these platforms could be attributed to the quality of their content, breadth of variety, or in the case of Prime Video, being part of a service bundle like Amazon Prime. Perhaps not surprisingly, ad-tier subscriptions are generally more likely than ad-free ones to be the first to cancel.

Exhibit 5: Prime Video, Netflix, and YT Premium are more likely to be canceled last than canceled first

![](images/633f72efbd8d96b5a2dd1dddd8b9d35dc81b629fc0e91d5625ecee01b3ccdfd8.jpg)  
Note: \* Netflix, HBO Max, Disney+, Hulu, Paramount+, and Amazon Prime Video reflect each respective service with or without ads.  
Source: AlphaWise, MS  
Exhibit 6: Meanwhile, platform subscribers are quicker to drop Starz, Crunchyroll, and MGM+

![](images/36f552ca2927848c7da68b178ac2ac2e2bd8936a8eb20f1a9537b106daee0415.jpg)  
Note: \* Netflix, HBO Max, Disney+, Hulu, Paramount+, and Amazon Prime Video reflect each respective service with or without ads.  
Source: AlphaWise, MS

Exhibit 7: Generally, ad-free tiers are stickier than their with-ads counterparts. In our view, likely due to the price sensitivity of subscribers

![](images/d8924887582086db46de299776557422899de87d6d638be63167edc82503e7c4.jpg)  
Source: AlphaWise, MS

Quality of Content: In 2020, Netflix was the undisputed leader on the perceived quality of its original programming, but the "streaming wars" in ensuing years saw a rapid influx of competition from other platforms. Our 2026 survey indicates a second consecutive year of growth in the percentage of total respondents who view Netflix as having the "best original programming" among its peers. Compared to other major streaming platforms, Netflix scores highest as a platform that "adds content I like", "has a broad selection of content", and "has my favorite movies".

Why do you subscribe to \_\_\_\_? (Among Platform Subscribers)  
Exhibit 8: Netflix continues to lead on original programming, increasing further YoY  
![](images/ab36a788e73cfee579f5e75efc508726cd73bb3f9449d053f58238f8a3d9f219.jpg)  
Source: AlphaWise, MS  
% of respondents viewing Netflix as service with "best original programming" among major streaming services & premium networks

Exhibit 9: After years of decline, Netflix appears to be regaining ground as the host of the best original programming

![](images/d46224203f9d3ce04478e939a7afa59fe41c4227e5a3e427990d5d34be4ea74e.jpg)  
Source: AlphaWise, MS

Exhibit 10: Netflix leads on many content quality-related metrics, although Paramount+, HBO Max, and Peacock compete closely on TV shows

![](images/6f93d0e5b4206a4ca02cee9b896a250b09640419bb55514ba73919db833b4328.jpg)  
Source: AlphaWise, MS

Platform Market Fit: The quality of engagement with platform content is a complex and multifaceted measure, and can vary across user segments. We asked streaming subscribers about their typical level of focus when watching content on that platform, and about how often they come to the platform with a specific piece of

content in mind. Overall, a large majority of subscribers watch platform content as a primary focus, and come to platforms with a specific content destination, although levels vary across platforms. Interestingly, results suggest that these two measures are positively correlated. Netflix, Apple TV+, and HBO Max users are the most likely to be fully focused when they watch, and they are most likely to have 'destination content'. Meanwhile, Disney+, YouTube, and Peacock are relatively more associated with playing in the background and browsing. Scoring lower on these indices may not indicate lower quality of engagement, but rather fulfilling a distinct market niche.

Across most platforms tested, younger subscribers (18-24) had the lowest focus index scores, suggesting higher rates of multitasking behaviors.

Exhibit 11: When you watch content on each of these platforms, how often is the content your primary focus versus something you mainly have on in the background while doing other activities?  
![](images/aabfd7538eae336ab116b24d6dce7b34f5f9b9221cc530fe450022cc2ad41727.jpg)  
Source: AlphaWise, MS

Exhibit 12: Netflix, Apple TV+, and HBO Max elicit the most focus for subscribers  
![](images/23a48dbe816ab85f23bb081f1ee2cb4008594f9ed159211c8b385b421f7d69fb.jpg)  
Source: AlphaWise, MS

Exhibit 13: How often do you open this platform with a specific show, movie, or video in mind?  
![](images/6c7ce0c13cf1acfdee330ab4213f138a707f3bce3061a4b3b40f1442ab0d7522.jpg)  
Source: AlphaWise, MS

Exhibit 14: YouTube, Peacock, and Disney+ have the most 'browsing' users  
![](images/dfcff1f8ad483af138e937b372974d9579ef9ca7dcb4e08858420406803501e7.jpg)  
Source: AlphaWise, MS

Exhibit 15: Quality is King: Focus index and destination index are positively correlated  
![](images/f5cea34a0bd3d5b4f24b523e5bc4ad1434e93114d15fb2348e36b25474db8f78.jpg)  
Source: AlphaWise, MS

Users who actively chose their subscription are more focused on its content. Focus index scores differed depending on the reasons why respondents have the subscription(s) they have – Netflix users who subscribed to Netflix to access its specific content (e.g., sports programming, favorite movies, etc.) are more likely to be fully focused when watching, compared to their counterparts who have Netflix because someone else in their household uses it, or because it was part of a wireless bundle. This framework holds true across all platforms tested, with a few exceptions such as Disney+ (which is more often purchased for children in the household).

Exhibit 16: Level of focus is lower among platform users who got their subscription via a bundle or another member of their household

<table><tr><td></td><td colspan="12">Reasons for Subscribing to [Streaming Service]</td></tr><tr><td>Focus Index (%Primary focus - %Background entertainment)</td><td>Has my favorite TV shows*</td><td>Has my favorite movies*</td><td>Has a broad selection of movies / TV shows</td><td>Good value for the money</td><td>Continues to add movies and TV shows that I like*</td><td>There are no ads / an acceptable amount of ads</td><td>Has live sports programming</td><td>Someone else in my household uses it</td><td>Included with my home internet or wireless phone plan</td><td>Included with a bundle with [another streaming service]**</td><td>Included with some other types of subscription**</td><td>Subscribed via free annual offer with Apple hardware purchase</td></tr><tr><td>Netflix</td><td>77%</td><td>79%</td><td>76%</td><td>79%</td><td>78%</td><td>78%</td><td>80%</td><td>61%</td><td>71%</td><td></td><td></td><td></td></tr><tr><td>Amazon Prime Video</td><td>73%</td><td>74%</td><td>74%</td><td>69%</td><td>74%</td><td>77%</td><td>75%</td><td>55%</td><td></td><td></td><td>60%</td><td></td></tr><tr><td>Hulu</td><td>70%</td><td>70%</td><td>70%</td><td>69%</td><td>70%</td><td>75%</td><td>63%</td><td>45%</td><td>65%</td><td>58%</td><td>67%</td><td></td></tr><tr><td>Disney+</td><td>50%</td><td>52%</td><td>63%</td><td>56%</td><td>64%</td><td>59%</td><td>65%</td><td>47%</td><td>60%</td><td>47%</td><td></td><td></td></tr><tr><td>Apple TV+</td><td>70%</td><td>70%</td><td>70%</td><td>69%</td><td>70%</td><td>67%</td><td>63%</td><td>45%</td><td></td><td>58%</td><td>65%</td><td>75%</td></tr><tr><td>HBO Max</td><td>73%</td><td>73%</td><td>74%</td><td>70%</td><td>77%</td><td>75%</td><td>78%</td><td>55%</td><td>68%</td><td></td><td></td><td></td></tr><tr><td>Paramount+</td><td>72%</td><td>66%</td><td>65%</td><td>66%</td><td>69%</td><td>69%</td><td>68%</td><td>25%</td><td>69%</td><td></td><td>55%</td><td></td></tr><tr><td>Peacock</td><td>69%</td><td>62%</td><td>68%</td><td></td><td>65%</td><td>68%</td><td>66%</td><td>38%</td><td>59%</td><td>53%</td><td></td><td></td></tr><tr><td>Weighted Average</td><td>70%</td><td>71%</td><td>72%</td><td>66%</td><td>73%</td><td>73%</td><td>71%</td><td>49%</td><td>66%</td><td>52%</td><td>61%</td><td></td></tr></table>

Note: \*For Disney+, states "Has my / my kids' favorite TV shows/movies" and "Continues to add movies and TV shows I / my family likes"; \*\*SVOD bundling pairs include Disney+/Hulu and Apple TV+/Peacock.; \*\*\*Other types of subscriptions include Prime membership (Amazon Prime Video), Hulu+ with Live TV subscription (Hulu), Apple One subscription (Apple TV+), and Walmart+ subscription (Paramount+).  
Source: AlphaWise, MS

## Netflix Pricing Sensitivity

While Netflix recently increased prices, the value perception remains strong with most thinking that the current standard ad-free plan pricing at \~\$20 per month is a 'great buy for the money' while they have room to >\$30 per month before it is perceived to be 'getting expensive' and would give some thought to subscribing.

Exhibit 17: Netflix's pricing power remains clear as churn remains contained even through price hikes  
![](images/d173f8c5305f6ee652938852d11cc250abb791f4e41b36ecac0ea481fe707de3.jpg)  
Note: Credit card data is a panel proxy subject to panel composition, c

[中间内容因长度限制已省略]

onal Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., authorised and regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the US by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## © 2026 MS
"""
