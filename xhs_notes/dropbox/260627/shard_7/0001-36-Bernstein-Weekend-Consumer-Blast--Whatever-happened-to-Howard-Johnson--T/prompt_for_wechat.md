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
- 已识别机构名：`Bernstein`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份Bernstein研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Weekend Consumer Blast: Whatever happened to Howard Johnson? The lifecycle of a hotel brand

Richard J. Clarke, FCA +44 20 7676 6850 richard.clarke@bernsteinsg.com

Euan McLeish +81 3 5962 9611 euan.mcleish@bernsteinsg.com

Jignanshu Gor +91 226 842 1494 jignanshu.gor@bernsteinsg.com

Luca Solca +41 582 723 126 luca.solca@bernsteinsg.com

Nadine Sarwat, CFA +44 20 7676 6849 nadine.sarwat@bernsteinsg.com

Trevor Stirling +44 20 7676 7521 trevor.stirling@bernsteinsg.com

William Woods +44 20 7676 6806 william.woods@bernsteinsg.com

Alexia Howard +1 917 344 8453 alexia.howard@bernsteinsg.com

Aneesha Sherman +1 917 344 8457 aneesha.sherman@bernsteinsg.com

Callum Elliott, CFA, ACA +44 20 7676 7183 callum.elliott@bernsteinsg.com

Danilo Gargiulo +1 917 344 8475 danilo.gargiulo@bernsteinsg.com

## By Richard Clarke

When was the last time you stayed (or ate) at a Howard Johnson? Arguably the originator of the hospitality franchise in the 1940/50s, the brand went from a peak of more than 1,500 locations in the 1970s (nb 30 years after post-WW2 relaunch) to \~120 today. Has America fallen out of love with hamburgers, ice-cream and colorful hotel rooms? It doesn't seem so - hospitality brands simply have a lifecycle. Crowne Plaza also illustrates this well - Crowne Plaza launched in 1983 as Holiday Inn Crowne Plaza and rebranded to Crowne Plaza Hotels in 1994. In 2019, we wrote a note claiming fixing Crowne Plaza would be like launching a new brand (IHG: IHG's problem child. Turning around Crowne Plaza would be like launching a new brand). But again maybe Crowne Plaza had simply had its time. In the US, the pipeline peaked in 2008 at 43 hotels, 25 years post launch; total hotels peaked at 210, 28 years post launch. Even factoring in that these peaks coincided with the pre-GFC hubris and the post-GFC decline, this trend of a pipeline peak 25-30 years post launch and a room peak \~30-35 years post launch is remarkably consistent across major US hotel brands. Crowne Plaza currently has 429 hotels globally and a US pipeline of 5 hotels. Luxury brands can achieve heritage, mainstream brands cannot and will eventually run out of steam and shrink.

We often get asked why hotel groups have so many brands, and normally offer an answer of customer segmentation and opportunity to perfect for higher returns, but we supplement this with an argument that this is also a necessity - brands have a lifecycle and every brand passing through the peak has to

be replaced by one in the fast adoption phase. Those groups that reinvent their brand portfolio at the right time look set to outperform over the longer term.

This is a consumer blast not a true research piece, and hence we take certain liberties on assumed launch dates and which brands we choose to look at. For example, Quality Inn (Howard Johnson's biggest rival for franchise pioneer) achieved growth well beyond 30 years but enjoyed a brand split and reinvigoration in the 1990s that few others seem to have pulled off. Overall, however we expect the conclusions hold weight.

EXHIBIT 1: A Howard Johnson's motor lodge in Panama City (in the 60's)  
![](images/2e2fa1f6d6eb944126edfc861831d41aff50383c82f6cb341e910b7b73076499.jpg)  
Source: Florida Memory

## KEY CHART

EXHIBIT 2: Across many of the largest hotel brands in the US the number of hotels has tended to peak at \~30 years  
![](images/6fcde02ce6bfe198d2365f3af7d42728dc61aba71406a1a2dbdd96cd4343aaf8.jpg)  
\* Holiday Inn ▲ Crowne Plaza ● Comfort Inn ◆ Rodeway  
Source: Company reports, Bernstein analysis

## THE HOTEL BRAND LIFECYCLE

Early growth - New (asset light) hotel brands are difficult to create. Brand owners have to convince third parties to take a risk and invest capital to open new hotels under their brand, often with little evidence of prior brand performance. As such many brands move slowly at first, adding a small number of hotels to the pipeline initially, which slowly flow through to supply, before accelerating - for example Hilton's Tru, launched in 2016 took \~24 months for the number of hotel rooms to meaningfully inflect upwards. Here conversion brands can offer more initial momentum, with a much lower initial investment and far shorter time to flow through from the pipeline. Although the shape of the early stages of a brands' lifecycle can be similar, brands can vary drastically in performance. Comparing the first \~8.5 years of growth for Hilton's Tru and IHG's Avid shows the different growth paths between to fairly similar brands - the discrepancy was apparent after the first 3 years of the brands' existence.

EXHIBIT 3: Hilton's Spark brand saw an upward inflection in the pace of additions within 12 months of launching  
Hilton brands - Room count relative to room count after 3 years of launch  
![](images/38379e9502167b2f4fa205208de3c18955a5d67f985b85695ec7eefec558ea52.jpg)  
Source: CoStar, Bernstein analysis

EXHIBIT 4: Not all brands are created equal though, similarly targeted brands can see very different success - the first 3 years provide a strong indication of potential  
Hotels - number of hotel rooms under Midscale brands  
![](images/de3e7001b151022ae0d96b8ace8777a4a11f0061c30b139b6ab7a11e623ea5ea.jpg)  
Source: CoStar, Bernstein analysis

EXHIBIT 5: Hotel brands tend to peak \~30 years after creation  
![](images/f2b3b4d61821dad596857f46eb1303d12d203a1bacdb888cc0d1d85d6084e6c6.jpg)  
Source: Company reports, CoStar, Bernstein analysis

The peak - After the early acceleration, the successful hotel brands tend to face a steady upwards trajectory, with a relatively consistent number of hotels added annually, until at roughly 30 years the total number of hotels begins to peak, with the pipeline soon to follow, tending to peak 5 years later at \~35 years. After 30 years brands typically then see a decline, stabilizing into the future well below the initial peak. However, the stabilized range is not homogeneous - Comfort Inn has seen its footprint stabilize at 80% of its maximum, while Holiday Inn has settled at \~40%.

EXHIBIT 6: No mainstream brands launched before the early 80's delivered growth from 2008-2026  
Room growth 2008-2026 by brand launch year (Upscale and below)  
![](images/eab2d69d38d8cab2980fa999c9e4e140ec326a3cc7e23df2b29998cf70563b90.jpg)  
Source: CoStar, Bernstein analysis

EXHIBIT 7: Similarly pipelines tend to peak (ex-some pre GFC over optimism)  
Pipeline vs peak (Americas)  
![](images/4687e7aecbd5e6dda569f2a41d10d74c870e55b528d8bd79ae394a5878e9fb6f.jpg)  
Source: Company reports, Bernstein analysis

EXHIBIT 8: On average hotel brand pipelines have peaked after 34 years, shortly after the total hotel number peaks  
Years post launch/acquisition pipeline peaked  
![](images/23955f86c3b72cb681c755557653bf645b99a51b1dba053dc6c0c417a4f57e28.jpg)  
Source: Company reports, CoStar, Bernstein analysis

## WHY DO BRANDS PEAK?

There are some key reasons we see that would explain a brand seeing rooms peak after 25-30 years:

\- Newer hotels are preferred by guests - Newer hotels receive better review scores from guests in the mainstream segments. As hotel brands age, the hotels within their brand will begin to show ware and tear, and if not properly maintained by owners, will eventually weigh on the perception of the brand. The older a brand is the greater the likelihood of older hotels under the brand, eventually weighing on the RevPAR even new hotels can deliver, meaning incremental developers are likely to move to other brands in search of a better ROI, and the more likely hotels will need to be removed to maintain brand standards.

\- Guest preferences change - Over time consumer preferences are not fixed, yet brand standards tend to be relatively more static. For example, consumer preferences have shifted away from the offerings of a 'full service' hotel (an on site restaurant, meeting spaces, a manned front desk, etc.) and have instead shifted towards limited service offerings - a headwind to Holiday Inn (a full service brand), which is more expensive to run due to offering amenities guests are no longer willing to pay for. The older a brand the more likely guest preferences are to move against it. The recent strength of extended stay ROI relative to Upscale is a big driver for the relative strength in the relatively newer extended stay segment (Exhibit 10).

\- Running out of whitespace - It is not uncommon for hotels to cluster in locations with high lodging demand. However, brand owners will avoid allowing hotels under the same brand to cluster too closely, both to protect its incumbent owners, and to maximize future owners' returns. The result is eventually brands run out of locations that can take incremental hotels under a brand. This is issue can be particularly acute at the high end, where the number of markets that can accommodate a Luxury hotel are limited, and the scarcity of a brand is a bigger driver of pricing.

\- Franchise contract lengths mean declines are unlikely within the first \~20 years. Given most franchise contracts are 10-20 years long, churn is highly unlikely for the first 2 decades of a brands existence.

EXHIBIT 9: Similarly in the Midscale segment older hotels receive weaker review scores  
Midscale brands - average year built vs average review score  
![](images/e02887b0447d73eecb28c150c9abbbae7855206b0e3429e76f1f6e7bf2ca789e.jpg)  
Source: Google Hotels, Bernstein analysis  
EXHIBIT 10: ROI differs between brands, but some of this is driven by the chain scale that the brand operates in - we see that generally higher chain scale brands deliver lower ROIs

![](images/cf049dc5800b7a9182850cd68b868d32beedafe1cc9f11ecd790f0dccfe80bd6.jpg)  
Source: Company reports, Franchise Disclosure Documents, Bernstein analysis

EXHIBIT 11: ROI is a strong predictor of relative pipeline size although Midscale hotels outperform the trend on ROI

ROI vs relative supply by segment

![](images/7e8e246b90e33c6bf909c4adb970b0dcb176d4bfb7ed99caf0b1aead2782cf15.jpg)  
Source: STR, Bernstein analysis

## CAN BRANDS DEFY THE 30 YEAR PEAK?

The two key ways where we see brands persistently defy the peak are through:

1. International expansion - While brands face issues of an aging incumbent hotel base within brands, running out of whitespace, and shifting consumer tastes, expanding internationally can help to solve a number of these issues. A brand can reposition itself in a new international market, which along with new whitespace, provides a somewhat blank canvas away from the incumbent aging hotels under the brand in a different market, and able to tweak the brand format to appeal to changes in consumer tastes. On a global basis we do not see the same 30-year peaks with hotel brands that we do when looking at specific markets.

2. Owner operated brands - While an asset light brand is somewhat exposed to the whims of its owner base when it comes to maintaining brand standards, when the brand owner also wholly owns the hotels they can be far more rigorous in maintaining standards, and preventing aging hotels from reducing brand perception. They also have far less ability to switch to a new brand format to cater to shifts in consumer taste, so much also do more work to stay current with consumer tastes. For example in the UK Whitbread's Premier Inn brand is almost 40 years old and still seeing growth - although this growth has slowed, with whitespace becoming a greater concern.

3. Luxury brands - Luxury brands do not tend to see the same decline in quality as their hotels age, while older Luxury brands tend to be more highly appreciated by customers - investment in the brand and the brand standards are far more important at the top end, where premium pricing can be driven from brand value. As such Luxury brands are far less likely to see the same drop off post \~30 years - and we see no correlation between brand launch year and growth within luxury.

EXHIBIT 12: On a worldwide basis we don't see the same 30 year peak for brands

![](images/3378f9ff21ad1067544b30514a019311e934257541908401ccbaecc3ac30e57f.jpg)  
Source: Company reports, Bernstein analysis

EXHIBIT 13: Whitbread has also been able to push past the 30 year peak (albeit with the UK room count beginning to plateu as we approach 40 years)  
Whtibread - UK Premier Inn rooms  
![](images/288da17bbefd7c0f10972604c4c93b73091da2029aece45e89bd7c368307688f.jpg)  
Source: Company reports, Bernstein analysis

EXHIBIT 15: In Luxury there is no correlation between brand age and growth - InterContinental still delivered growth from 2010-2025 despite turning 80 years old this year  
Room growth - 2010-2025 by brand lanch year (Luxury)  
![](images/880a0f3528b7138e623bfbfbdac7a092e5d6dfe87fb1b023a54d3f800b7c3f08.jpg)

EXHIBIT 14: We see little correlation between hotel age and average review score in the luxury segment, and a slightly negative slope  
Luxury brands - average year built vs average review score  
![](images/f61de3ff0455f3f6a5ff502b16f3124e7e6c4f1bba0d9a6ef34dc97de88430c4.jpg)  
Source: Google Hotels, Bernstein analysis  
Source: CoStar, Bernstein analysis

EXHIBIT 16: Intercontinental have just opened their Red Sea Resort, despite the brand turning 80 years old in 2026  
![](images/5ab49ed13d6b72f8b2a7b8f66d6057a603f8eeb4682788757329bcb3ec419aaa.jpg)  
Source: Company website

EXHIBIT 17: Hyatt are set to open the Grand Hyatt Miami Beach in 2027 - under a 46 year old brand  
![](images/e4540f51568457990b46173fb041d96ddfc8b10f271abaefac9b89bb38596824.jpg)  
Source: Company website

## WHAT DOES THIS MEAN FOR THE COMPANIES?

The clearest implication from this analysis is that the hotel groups with newer brands, which still have some time left before the brands hit the 30-year peak, are best positioned for growth. Perhaps unsurprisingly Hilton and Hyatt come out best - both have the youngest brand portfolio, and also lead the industry on NUG, the age profiles of their brands would imply a continued growth advantage.

EXHIBIT 18: Hilton and Hyatt have the 'newest' brands among the asset light hotel groups  
Hotels - Age of hotel brands by owner (years)  
![](images/57da989d3f874603c955a402c17f68558137e2e4836133a95f6fce227b4b3846.jpg)  
Wyndham not covered  
Source: Company reports, CoStar, Bernstein analysis

EXHIBIT 19: In the US specifically Hyatt and Hilton look to have the newest brands, and should be off the peak room count for 64% and 30% of their brands respectively

% US Hotels in brands >30 years old  
![](images/7513df29aa9f3275dca7fded03a77a19876c93446d396f407287d3d335e340ce.jpg)  
Wyndham not covered  
Source: Company reports, CoStar, Bernstein analysis

## BERNSTEIN TICKER TABLE

<table><tr><td colspan="3"></td><td colspan="2">25 Jun 2026</td><td>TTM</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td>Ticker</td><td>Rating</td><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Rel. Perf.</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>MAR (Marriott)</td><td>O</td><td>USD</td><td>378.91</td><td>402.00</td><td>21.7%</td><td>USD</td><td>10.02</td><td>11.53</td><td>13.30</td><td>37.8</td><td>32.9</td><td>28.5</td></tr><tr><td>HLT (Hilton)</td><td>M</td><td>USD</td><td>340.55</td><td>320.00</td><td>13.5%</td><td>USD</td><td>8.11</td><td>8.96</td><td>10.28</td><td>42.0</td><td>38.0</td><td>33.1</td></tr><tr><td>H (Hyatt)</td><td>O</td><td>USD</td><td>197.01</td><td>202.00</td><td>22.9%</td><td>USD</td><td>2.25</td><td>4.03</td><td>5.17</td><td>87.5</td><td>48.8</td><td>38.1</td></tr><tr><td>IHG.LN (IHG)</td><td>M</td><td>USD</td><td>172.65</td><td>154.00</td><td>32.9%</td><td>USD</td><td>5.01</td><td>5.69</td><td>6.48</td><td>34.4</td><td>30.4</td><td>26.6</td></tr><tr><td>BKNG (Booking)</td><td>M</td><td>USD</td><td>177.05</td><td>188.00</td><td>(40.1)%</td><td>USD</td><td>9.12</td><td>10.53</td><td>12.29</td><td>19.4</td><td>16.8</td><td>14.4</td></tr><tr><td>EXPE (Expedia)</td><td>M</td><td>USD</td><td>250.95</td><td>253.00</td><td>30.6%</td><td>USD</td><td>15.86</td><td>20.92</td><td>25.20</td><td>15.8</td><td>12.0</td><td>10.0</td></tr><tr><td>TRIP (TripAdvisor)</td><td>O</td><td>USD</td><td>12.80</td><td>20.00</td><td>(18.4)%</td><td>USD</td><td>1.27</td><td>1.30</td><td>1.88</td><td>10.1</td><td>9.8</td><td>6.8</td></tr><tr><td>ABNB (Airbnb )</td><td>O</td><td>USD</td><td>141.88</td><td>168.00</td><td>(11.4)%</td><td>USD</td><td>4.03</td><td>5.44</td><td>6.65</td><td>35.2</td><td>26.1</td><td>21.3</td></tr><tr><td>SPX</td><td></td><td></td><td>7,357.49</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EDME</td><td></td><td></td><td>1,591.52</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

Source: Bloomberg, Bernstein estimates and analysis.

## I. REQUIRED DISCLOSURES

References to "Bernstein" or the "Firm" in these disclosures relate to the following entities: Bernstein Institutional Services LLC (April 1, 2024 onwards), Bernstein & Co., LLC (pre April 1, 2024), Bernstein Autonomous LLP, BSG France S.A. (April 1, 2024 onwards), Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited, Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社) and analysts employed by SG Africa Technologies & Services to produce Bernstein under a Global Services Agreement in place between Bernstein and SG.

Bernstein is part of a joint venture between SG (SG) and AllianceBernstein, L.P. (AB). Unless specifically noted otherwise, for purposes of these disclosures, references to Bernstein's “affiliates” relate to both SG and AB and their respective affiliates.

## VALUATION METHODOLOGY

This research publication covers six or more companies. For valuation methodology and other company disclosures: Please visit: https://bernstein-autonomous.bluematrix.com/sellside/Disclosures.action.

Or, you can also write to the Director of Compliance, Bernstein Institutional Services LLC, 245 Park Avenue, New York, NY 10167.

## RISKS

This research publication covers six or more companies. For risks and other company disclosures: Please visit: https://bernstein-autonomous.bluematrix.com/sellside/Disclosures.action. Or, you can also write to the Director of Compliance, Bernstein Institutional Services LLC, 245 Park Avenue, New York, NY 10167.

## RATINGS DEFINIT

[中间内容因长度限制已省略]

nce system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively "Bloomberg"). Bloomberg or Bloomberg's licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg's licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan

KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
