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
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`GS`。标题格式建议：`# GS：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Americas Retail: Specialty Hardlines: Analyzing the impact of Best Buy and Meta's partnership on eyewear retailers

On June 8th, Best Buy announced a partnership with Meta to open Meta Labs across more than 50 store locations. These experiential spaces provide customers the opportunity to explore Meta's AI glasses and VR headsets through interactive demos, smart mirrors, personalized fittings, and more. In this note, we assess the partnership's potential impact on eyewear retailers (EYE, WRBY, ESLX) by analyzing each retailer's product offerings, store proximity to Best Buy locations, and IR commentary following the announcement.

Bottom line: We are encouraged to see Best Buy and Meta's partnership, and its potential to expand adoption of AI smart glasses across the industry. For EYE, we do not view the partnership as a meaningful risk, given National Vision's differentiation vs. Best Buy with its seamless eye exam, prescription, lens, and frames offering for the Ray-Ban Meta glasses. For WRBY, we believe the announcement will increase focus on the company's ability to capture traffic ahead of its AI glasses launch this fall. We do not view the partnership as a risk given WRBY's integrated prescription and lens capabilities and broad store distribution across \~337 owned locations and digital channels. For ESLX, we view the announcement favourably - expanding distribution and providing additional resources to support consumer education is a helpful step to broadening adoption of smart glasses.

## Details on the Best Buy and Meta partnership

On June 8th, Best Buy announced a partnership with Meta to open Meta Labs across more than 50 store locations. These 900 sq. ft experiential spaces will provide customers the opportunity to explore Meta's AI product lineup, including the Ray-Ban Meta, Meta Ray-Ban Display, Oakley Meta, Meta Quest 3, and Meta Quest 3S VR headsets. Each Meta Lab will also feature dedicated Meta Sales Specialists to help guide the customer experience. Customers can engage with the assortment through a variety of methods, including immersive demos, built-in prompts, and tech-forward displays that allow shoppers to virtually try on different frames and styles.

Best Buy noted that over $50\%$ of their customers want to see Meta's AI glasses in person before making a purchase, and these labs will offer a hands-on experience that cannot be found at other retailers. The first few Meta Lab locations will launch in Best Buy stores this June, with additional locations rolling out through the summer and into the holiday season.

Kate McShane, CFA

+1(212)902-6740

kate.mcshane@gs.com

GS & Co. LLC

Brooke Roach, CFA

+1(212)357-2421

brooke.roach@gs.com

GS & Co. LLC

Richard Felton, CFA

+44(20)7552-7872

richard.felton@gs.com

GS International

Mark Jordan, CFA

+1(617)772-7951

mark.jordan@gs.com

GS & Co. LLC

Emily Ghosh

+1(713)658-2632

emily.ghosh@gs.com

GS & Co. LLC

Nishi Agarwal

+1(332)245-7668

nishi.agarwal@gs.com

GS India SPL

Grace Chee

+1(212)357-9730 | grace.chee@gs.com

GS & Co. LLC

Mentesnot Adamu

+1(801)744-0630

mentesnot.adamu@gs.com

GS & Co. LLC

Samantha Chiang

+1(212)357-7992

samantha.chiang@gs.com

GS & Co. LLC

Carly Chasen

+1(212)902-2327

carly.chasen@gs.com

GS & Co. LLC

Dan Duggan, Ph.D.

+1(212)902-4726

dan.duggan@gs.com

GS & Co. LLC

Sreenya Chitluri

+1(332)245-7761

sreenya.chitluri@gs.com

GS India SPL

We spoke with management following the announcement, who noted they are excited about the expanding partnership with Meta, and plan to test the initial 50 locations before committing to a broader store rollout. Within the labs, management expects a wide assortment of styles and colors, given the large \~900 sq. ft. format. They also highlighted that they would expect to work with additional vendors in the future to expand the assortment for smart glasses and related AI products.

## Implications for the eyewear retailers

We evaluate the partnership's potential impact by analyzing the store proximity between Best Buy and each retailer. In our analysis, we assess store base proximity across all Best Buy locations, assuming that Meta Labs are eventually rolled out across the full fleet. While Best Buy plans to implement the Meta Labs in only 50 stores initially, we note management only disclosed a list of five locations on the press release.

Among the three eyewear retailers, Warby Parker had the highest share of stores within a three-mile radius of a Best Buy and continued to have the highest store penetration beyond that radius. Specifically, 49% of ESLX's stores, 53% of EYE's stores, and 54% of WRBY's stores are within three miles of a Best Buy location. For stores within a one mile radius of Best Buy, EYE had the highest penetration. In contrast, Best Buy has the highest percentage of its store base near an EYE location and the lowest percentage of its store base near a Warby Parker location.

Exhibit 1: Retailers' % of stores within all Best Buy locations, if Meta shop in shops were to be opened in every store

<table><tr><td>stores within x miles of target company</td><td>&lt; 0.1 Mi.</td><td>&lt; 0.5 Mi.</td><td>&lt; 1.0 Mi.</td><td>&lt; 3.0 Mi.</td><td>&lt; 5.0 Mi.</td><td>&lt; 10.0 Mi.</td><td>&lt; 25.0 Mi.</td></tr><tr><td>ESLX w/in BBY</td><td>2%</td><td>19%</td><td>30%</td><td>49%</td><td>68%</td><td>87%</td><td>96%</td></tr><tr><td>EYE w/in BBY</td><td>4%</td><td>23%</td><td>36%</td><td>53%</td><td>70%</td><td>91%</td><td>98%</td></tr><tr><td>WRBY w/in BBY</td><td>0%</td><td>12%</td><td>19%</td><td>54%</td><td>78%</td><td>98%</td><td>99%</td></tr></table>

<table><tr><td>target company stores within x miles</td><td>&lt; 0.1 Mi.</td><td>&lt; 0.5 Mi.</td><td>&lt; 1.0 Mi.</td><td>&lt; 3.0 Mi.</td><td>&lt; 5.0 Mi.</td><td>&lt; 10.0 Mi.</td><td>&lt; 25.0 Mi.</td></tr><tr><td>BBY w/in ESLX</td><td>1%</td><td>13%</td><td>20%</td><td>29%</td><td>40%</td><td>60%</td><td>79%</td></tr><tr><td>BBY w/in EYE</td><td>4%</td><td>27%</td><td>41%</td><td>57%</td><td>68%</td><td>78%</td><td>84%</td></tr><tr><td>BBY w/in WRBY</td><td>0%</td><td>2%</td><td>3%</td><td>7%</td><td>11%</td><td>26%</td><td>51%</td></tr></table>

EYE locations contain America's Best and Eyeglass World while ESLX locations contain Sunglass Hut and LensCrafter  
Source: GS Global Investment Research, Placer.ai, DataWorks

Exhibit 2: AI glasses comparison table for EYE/WRBY/BBY/ESLX

<table><tr><td></td><td>EYE</td><td>WRBY</td><td>BBY</td><td>ESLX</td></tr><tr><td>Company</td><td>National Vision / America&#x27;s Best</td><td>Warby Parker</td><td>Best Buy</td><td>EssilorLuxottica</td></tr><tr><td>What they do</td><td>Optical retailer (eye exams + glasses + Rx fulfillment)</td><td>Optical retailer / eyewear brand (AI glasses launching this fall)</td><td>Electronics retailer / distributor</td><td>Eyewear + lens manufacturer / brand owner / optical retail ecosystem</td></tr><tr><td>AI glasses</td><td>Ray Ban Meta, Oakley Meta</td><td>Intelligent Eyewear with Google/Samsung (pre-launch)</td><td>Ray Ban Meta, Meta Ray Ban Display, Oakley Meta, PRIMEPLUS, Miro, BleeqUp, Azpen</td><td>Ray Ban Meta, Meta Ray Ban Display, Oakley Meta</td></tr><tr><td>Styles</td><td>Ray Ban Meta: Blayzer, Scriber, Skyler, Wayfarer; Oakley Meta: HSTN</td><td>TBD</td><td>Ray Ban Meta: Wayfarer, Skyler, Headliner; Meta Ray Ban Display; Oakley Meta: HSTN, Vanguard; PRIMEPLUS: Bluetooth Smart Glasses, Cycling Smart Glasses; Miro: iVision6, W5; Bleequp GLCG00A Ranger Ai Sports; Azpen VUEX</td><td>Ray Ban Meta: Wayfarer, Blayzer, Scriber, Skyler, Headliner, x Coperni Limited Edition; Oakley Meta: HSTN, Vanguard</td></tr><tr><td>Style count</td><td>5</td><td>TBD</td><td>12</td><td>8</td></tr><tr><td>Entry price tier</td><td>~$379 entry for Wayfarer; Oakley HSTN ~$399</td><td>TBD</td><td>$119 Miro; ~$247 Ray Ban Gen 1 / ~$379 Ray Ban Gen 2</td><td>~$247 Wayfarer Gen 1; ~$399 Oakley HSTN</td></tr><tr><td>Premium price tier</td><td>~$499 for Scriber/Blayzer</td><td>TBD</td><td>~$799 for Meta Ray-Ban Display; ~ $499 for Oakley Vanguard</td><td>~$499 Scriber/Blayzer Gen 2; ~$499 Oakley Vanguard</td></tr><tr><td>Color counts</td><td>Ray Ban: 5; Oakley: 1</td><td>TBD</td><td>Ray Ban: 6; Meta Display: 2; Oakley: 3; PRIMEPLUS: 3; Miro: 1; BleeqUp: 1; Azpen: 1</td><td>Ray Ban: 8; Oakley: 6</td></tr><tr><td>One-stop-shop / Rx fulfillment</td><td>Strongest one-stop-shop angle (exam + Rx + AI glasses in optical setting)</td><td>Core optical one-stop-shop; AI-glasses-specific workflow still TBD until launch</td><td>Product sold at retail, but Rx configuration is routed to Meta&#x27;s Rx website</td><td>Strongest ecosystem / brand + lens + optical retail infrastructure</td></tr></table>

Source: Company data, Data compiled by GS Global Investment Research

We also looked at Google search trends around AI glasses at Best Buy, America's Best, and Warby Parker. Searches for Best Buy AI glasses have largely outpaced peers for the majority of 2025/26, though the searches have been steadily declining since its Dec 2025 peak. Meanwhile, we have observed an uptick in searches for Warby Parker AI glasses in recent weeks.

## Exhibit 3: Search intensity for Best Buy AI glasses has largely led peers, though we see an uptick in Warby Parker trends in recent weeks

Trailing 4 week search intensity for: ai glasses best buy (US); america's best meta (US); ai glasses warby (US)

![](images/66123b1a6e01504fd9cb8d8b4d2a1f8bb194410a55b9e384ee17d5a4e5a068a9.jpg)

<details>
<summary>line chart</summary>

| Month    | Best Buy | America's Best | Warby Parker |
|----------|----------|----------------|--------------|
| Dec-24   | 0        | 0              | 0            |
| Jan-25   | 0        | 0              | 0            |
| Feb-25   | 0        | 0              | 30           |
| Mar-25   | 0        | 0              | 0            |
| Apr-25   | 0        | 0              | 0            |
| May-25   | 0        | 0              | 40           |
| Jun-25   | 100      | 0              | 0            |
| Jul-25   | 80       | 0              | 0            |
| Aug-25   | 160      | 0              | 0            |
| Sep-25   | 100      | 0              | 30           |
| Oct-25   | 130      | 0              | 0            |
| Nov-25   | 170      | 0              | 60           |
| Dec-25   | 310      | 160            | 140          |
| Jan-26   | 240      | 310            | 30           |
| Feb-26   | 190      | 310            | 140          |
| Mar-26   | 240      | 0              | 40           |
| Apr-26   | 160      | 130            | 80           |
| May-26   | 150      | 70             | 190          |
</details>

Source: Google Trends (https://www.google.com/trends), Data compiled by GS Global Investment Research

We utilized GS Data Works for the store overlap analysis. GS Data Works leverages alternative data sources and advanced analysis techniques to create unique data-driven insights across

equity, credit and macro research.

GS Data Works analysis provided by Dan Duggan, Ph.D and Sreenya Chitluri.

## EYE

National Vision initially launched Ray-Ban Meta glasses in 50 of its stores in 2Q25, before completing a full roll-out across all locations by April 2026. Management highlighted in March that the Meta glasses are the fastest turning SKUs in their assortment, with sell-through exceeding expectations. Additionally, they noted that Ray-Ban Meta consumers carry some of the highest average transaction values within their portfolio.

In our conversations with management, they noted that they are not concerned about Best Buy's partnership with Meta, as National Vision is able to offer a seamless shopping experience that Best Buy cannot replicate. Specifically, National Vision can fulfill the eye exam, lenses, and frames for the customer all within a single visit. In contrast, if a Best Buy customer requires different lenses, they have to send their glasses off to a lab, creating an inconvenient process. National Vision highlighted that they offer demo experiences in their stores as well, and are expanding associate training for Meta glasses across the full customer journey (purchase through pick-up).

## WRBY

We believe the Meta x Best Buy partnership is positive for the intelligent eyewear category in aggregate, as expanded distribution and consumer education efforts help broaden awareness and adoption of smart glasses. That said, as we move into the holiday season, this announcement will increase focus on WRBY's ability to capture share of traffic as the company prepares to launch its AI glasses in partnership with Google and Samsung in Fall 2026.

In our conversations with the company, WRBY noted the product will be sold only through WRBY's \~337 owned stores (across 103 markets / 256 cities) and select digital channels on launch (no initial wholesale to third party retailers). This enables sharp control over the consumer experience and initial introduction to the product, and also provides an opportunity for WRBY to offer holistic visioncare services and drive prescription / lens attachment rates. WRBY has invested in its store and customer experience teams to drive a smooth rollout of the product this year. Importantly, WRBY's store fleet footprint is broad-based across 44 states, in all major cities, and accessible to the majority of the US population. Economics by channel are also a consideration. Over time, management has indicated an interest in scaling distribution over time to potential wholesale doors, but has indicated they will be thoughtful in their approach.

We expect investor focus to remain centered on the company's upcoming fall product launch, consumer receptivity to the WRBY product vs. competitor items (Gentle Monster / Ray Ban and Oakley Meta), the pace at which unit sales can scale, and the broader halo that these intelligent eyewear products can provide on the broader WRBY ecosystem (traffic / conversion / fixed cost leverage).

## ESLX

From the perspective of EssilorLuxottica, we view the announcement between Meta and Best Buy favourably. Expanding distribution and providing additional resources to support consumer education is a helpful step to broadening adoption of smart glasses – especially for Rayban Meta Display for availability of product demonstrations appointments had been a bottleneck for growth in recent quarters. We do see incremental benefits from selling through EssilorLuxottica's DTC network or specialist optical retailer rather than a retail such as Best Buy – for instance higher attachment rates of prescription or photochromic lenses which come with more favourable economics vs frames – but also note that management had pointed to third party sales of AI glasses as incremental.

## Valuations & Risks

## BBY

We are Sell rated on BBY. Our 12-month price target is \$62 with downside/base/upside case EV/EBITDA multiples at 5.0x/5.5x/6.0x.

Upside risks include if the company receives incremental sales from pull-forward purchases and tax refunds; if the company is able to mitigate memory supply shortages better than expected; if the company's marketplace and advertising initiatives more than offset memory margin pressure; if more consumers trade up to premium devices, improving product margin; if the housing market improves, and BBY's appliances sales improves; if BBY gains share relative to other retailers; if innovation in consumer electronics and mobile phones / computing helps accelerate the top line.

## EYE

We are Neutral rated on EYE. Our 12-month price target is \$24 with downside/base/upside case EV/EBITDA multiples of 8.5x/9.5x/10.5x.

Upside risks include better-than-expected demand for eye care and eyeglasses following softer trends in recent years; a meaningful acceleration in trade down trends; if margins recover faster than expected; and the potential for a multiple re-rating if sentiment improves following better-than-expected top line results and a clear pathway to margin recovery.

Downside risks include a slower-than-expected top line recovery as lower-income and uninsured customers defer demand, or if certain consumers exit the market altogether; less-than-expected trade down; continued exam capacity headwinds; margin headwinds due to higher wages; increased competition; and the risk that certain costs remain elevated.

## WRBY

We are Buy rated on WRBY with a 12-month price target of \$31 based on 22.0x Q5-Q8 EV/EBITDA valuation methodology.

Downside risks include: (1) Slow growth of new customers or limited in-network utilization; (2) Slower growth in e-commerce; (3) Terminal margin uncertainty; and (4) Weaker store productivity.

## ESLX

Our 12-month price target of €260 is derived using an equal blend of a DCF and a multiples-based valuation (using our annualised Q5-Q8 estimates). Our DCF implies an intrinsic value of €264 per share and uses a WACC of 8.3% and terminal growth rate of +3.5%. Our multiples-based approach applies a 34x P/E multiple to our annualised Q5-Q8 EPS estimates and implies a value of €255 per share.

Downside risks: (1) Slowdown in new launches or delayed rollout; (2)

Lower-than-expected operational leverage; (3) Retail network disruption; and (4)

Weaker-than-expected consumer confidence.

## Disclosure Appendix

## Reg AC

We, Kate McShane, CFA, Brooke Roach, CFA, Richard Felton, CFA, Mark Jordan, CFA, Emily Ghosh, Nishi Agarwal, Grace Chee, Mentesnot Adamu, Samantha Chiang and Carly Chasen, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

We, Dan Duggan, Ph.D. and Sreenya Chitluri, hereby certify that all of the views expressed in this report accurately reflect our personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Kate McShane, CFA GS & Co. LLC, Brooke Roach, CFA GS & Co. LLC, Richard Felton, CFA GS International, Mark Jordan, CFA GS & Co. LLC, Emily Ghosh GS & Co. LLC, Nishi Agarwal GS India SPL, Grace Chee GS & Co. LLC, Mentesnot Adamu GS & 

[中间内容因长度限制已省略]

m impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
