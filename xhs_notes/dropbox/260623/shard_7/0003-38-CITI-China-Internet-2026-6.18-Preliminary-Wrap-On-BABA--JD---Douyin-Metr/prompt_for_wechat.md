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
- 已识别机构名：`Citi`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份Citi研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# China Internet

## 2026 6.18 Preliminary Wrap On BABA, JD & Douyin Metrics

## CITI'S TAKE

This year's 6.18 shopping festival concluded quietly, reflecting a continued soft macro environment and cautious, selective consumer spending, in our view. As Alibaba scaled back investment in quick commerce this year, the absence of aggressive subsidies across industry players further contributed to a quiet campaign. Alibaba shifted its strategy towards brand ads endorsement while JD.com saw record transacting users driven by growth in services. Fudan's Big Data Lab estimated a modest 3.2% yoy growth in online GMV for 2026 6.18 festival with Taobao and JD captured \~60% of total shares. As we are waiting for Syntun forecast release, we reconcile 2026 likely be the most low-profile/quiet 6.18 for the past 16 years, considering the muted macro and cautious consumption spend.

Fudan's Big Data Lab — According to a report from Fudan Consumer Market Big Data Lab, total online GMV during the 2026 6.18 shopping festival is estimated to grow by a modest 3.2% yoy, with Taobao & Tmall and JD.com captured 34% and 25% of the GMV, respectively, while Douyin at 20% and PDD at 7% of the total GMV. The Fudan Lab report also suggested that JD solidified its leadership in the 3C, appliance, and healthcare sectors, capturing market shares of 57.8%, 53.9%, and 48.6%, respectively. The fashion and apparel category saw a general slowdown across all platforms, though JD still posted the fastest growth at 11.6%, while Taobao & Tmall's growth notably accelerated to 5.9% from the previous year. In the home living segment, Douyin and JD led with growth rates of 10.6% and 10.5%, respectively, while Taobao & Tmall and PDD experienced flat performance.

Alibaba — In contrast to last year's aggressive campaign in promoting Taobao Shangou, Alibaba has significantly scaled back its subsidies this year, and instead focusing on investment in brand ads in popular dramas. It also shifted its celebrity campaign, moving from direct sponsorships to featuring endorsements from several participating brands. Mixed performance for 3C category while declining trend for home living and outdoor category noticed for BABA. (see more detail)

JD.com — JD announced transacting users reaching record level, driven by growth in service categories including housekeeping, nursery services and appliance installation services. Throughout the campaign, total time spent of JD live-stream users increased by $>100\%$ driven by growing sessions for celebrity, C-suite and supermarket live-streaming (link to our flash).

Douyin — Douyin E-commerce's 2026 6.18 shopping festival concluded with 120,000 merchants and 570,000 streamers whose GMV doubling yoy. Over 30,000 new merchants participated in 6.18 on Douyin for the first time with each generating GMV exceeding Rmb1mn, while long-tail streamers have contributed over 80% of total KOL GMV. Douyin's content strategy boosted e-commerce success. Viewership of short videos with shopping carts rose by 57% yoy contributed by strategic use of consumption vouchers.

# 2026 6.18 Preliminary Wrap Fudan data read-through

## Total online GMV +3.2% during 2026 6.18

Reported by Sohu News dated Jun 19 (link), Fudan Consumer Market Big Data Lab released 2026 6.18 online consumption report which suggested that total online GMV grew by 3.2% yoy during 6.18 2026, suggesting a relatively flat momentum comparing to last year likely due to softer consumption sentiment in our view.

With no major ecommerce platforms disclosing actual GMV of GMV growth during 6.18, Fudan Lab estimates Taobao & Tmall and JD accounted 34/25% of GMV respectively during 2026 6.18, which in total accounting for a majority GMV mix of \~60%. On the other hand, Douyin contributed 20% GMV mix during 2026 6.18, while PDD at 7%.

## Moderate category performance

Fudan Lab suggested that JD maintained a dominant position in 3C, appliances and healthcare categories during 2026 6.18 with 57.8%, 53.9% and 48.6% respectively.

For fashion and apparel categories, all platforms have experienced a slowdown during 2026 6.18 comparing to 2025 with the fastest GMV growth from JD at 11.6%, followed by Douyin at 7.3% and PDD at 6.7%. Comparing to last year, Taobao & Tmall is estimated to see an accelerating apparel growth at 5.9%, vs. 3.5% in 2025.

For home living categories, Douyin and JD maintained a relatively higher growth at 10.6% and 10.5% respectively despite both also experienced slowdown vs. last year. Both Taobao & Tmall and PDD have seen a flattish growth in home living categories in 2026 6.18.

Figure 1. 2026 6.18 GMV breakdown by platform  
![](images/42307a3f221924172ae3799b134a091c878e382bed22081996963093466952c6.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Fudan Consumer Market Big Data Lab, Sohu News, Citi

Figure 2. 2026 6.18 GMV breakdown by key categories  
![](images/581805aa24854ed6a103a3dfaaa7efc0f94bec4781347154f7f4d7e2834f3539.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Fudan Consumer Market Big Data Lab, Sohu News, Citi

Figure 3. GMV growth in apparel category by platforms during 6.18  
![](images/8f3a22ccdf5df20d6e942db57d1f78ca537e68181c35aeb74151f1dd3704daac.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Fudan Consumer Market Big Data Lab, Sohu News, Citi

Figure 4. GMV growth in home living category by platforms during 6.18  
![](images/6de6f4f0111f752190819543e20e5cb97146f2eea1d0b53959c030740f8bf6ba.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Fudan Consumer Market Big data Lab, Sohu News, Citi

## Alibaba

## Low-profile marketing this year

Compared to heavy subsidies on Taobao Shangou in 2025 6.18, this year Alibaba has significantly scaled-back subsidies on Taobao Shangou. In contrast, this year Tmall has invested in brand ads in multiple long-drama including Family Business, The First Jasmine, Zhan Zhao Adventures and Ashes to Crown. Major ads are in forms of pre-streaming ads, ad placements and creative ads.

Tmall also adjusted its celebrity campaign this year by inviting brand endorsement which participated in 2026 6.18 instead of directly sponsoring its own endorsement like last year. Major participating brands include Spes, Dessmann, Bose, Molsion, Fila, CeraVe, Gillette, Jimmy Choo and Florasis.

Taobao & Tmall also invited celebrities from popular variety shows Ride the Wind 2026 as its major endorsement. During its official endorsed live-streaming session on Tmall on May 27, the live-streaming session had generated Rmb20mn GMV with over 1mn viewership and over 35mn interactions. These celebrities also participated in FIFA World Cup showcase on Tmall on Jun 11 that drove meaningful traffic growth on Tmall platform.

## Category performance

According to a third-party tracking firm All View Cloud (AVC) on June 17 (link), which suggested a sequential GMV and order volume growth on Tmall by product categories:

■ 3C: Tmall saw faster sequential growth for mouse and keyboards in terms of sequential GMV and order volume growth. This compares to relatively flattish volume growth for smart watch, sound bar and portable chargers. A flat sequential growth for wireless earphone vs. 7.5% sequential volume growth likely indicate a larger promotional effort during 6.18 period.

■ Home living: major home living categories saw single digit to teens % sequential decline in order volume and GMV including mattress, blanket, pillow and illumination devices. Intelligent switch is the only category covered AVC that saw mid-single digit growth in sales volume and GMV on Tmall.

■ Outdoor: major categories including bikes, treadmill, spinning also saw decline in sales volume and GMV on Tmall in week of Jun 8-14, while the magnitude of decline in GMV is smaller for bikes and treadmill comparing to its order volume decline.

Figure 5. Sequential GMV and sales volume growth on Tmall by categories in week of Jun 8-14

<table><tr><td colspan="3">3C</td><td colspan="3">Home living</td><td colspan="3">Outdoor</td></tr><tr><td>Sub-categories</td><td>GMV</td><td>Volume</td><td>Sub-categories</td><td>GMV</td><td>Volume</td><td>Sub-categories</td><td>GMV</td><td>Volume</td></tr><tr><td>Wireless earphone</td><td>-0.1%</td><td>7.5%</td><td>Mattress</td><td>-1.5%</td><td>-5.3%</td><td>Bicycles</td><td>-12.6%</td><td>-16.7%</td></tr><tr><td>Smart watch</td><td>3.7%</td><td>-0.2%</td><td>Blanket</td><td>-22.9%</td><td>-22.3%</td><td>Treadmill</td><td>-2.4%</td><td>-5.0%</td></tr><tr><td>Sound bar</td><td>-5.5%</td><td>-0.7%</td><td>Ceiling light</td><td>-8.8%</td><td>-3.0%</td><td>Spinning</td><td>-4.2%</td><td>-3.9%</td></tr><tr><td>Portable charger</td><td>-0.8%</td><td>-0.3%</td><td>Pillow</td><td>-8.5%</td><td>-7.9%</td><td>Massage chair</td><td>-1.7%</td><td>-0.1%</td></tr><tr><td>Mouse</td><td>14.8%</td><td>7.7%</td><td>Eye-friendly lamp</td><td>-14.1%</td><td>-15.0%</td><td rowspan="4" colspan="3"></td></tr><tr><td>Keyboard</td><td>16.6%</td><td>21.8%</td><td>Shower head</td><td>-4.0%</td><td>-16.0%</td></tr><tr><td rowspan="2" colspan="3"></td><td>Bathroom heater</td><td>0.5%</td><td>-1.7%</td></tr><tr><td>Intelligent switch</td><td>6.3%</td><td>6.6%</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: All View Cloud, Citi

## JD.com

## Record transacting users

Shortly after mid-night of Jun 19th Asia time, JD announced key performance metrics for 618 campaign with transacting users reaching record level as of Jun 18 23:59, driven by growth in service categories including housekeeping, nursery services and appliance installation services. Throughout the campaign, total time spent of JD live-stream users increased by >100% driven by growing sessions for celebrity, C-suite and supermarket live-streaming (link to our flash).

## Active brand participation

During 618, number of brands which released new products on JD platform up 5x yoy, while number of SME merchants participating in JD's 618 campaign grew by >62% yoy. >3,000 new merchants which participated in JD's 618 for the first time generated >Rmb1mn GMV.

## Category performance

■ 3C: GMV of AI-related electronic products doubled yoy. GMV of high-end smartphones and high-end laptops from brands such as Apple, Lenovo, Huawei and Asus grew by 300%/100% yoy respectively. Reported by Sohu News dated Jun 19 (link), Apple continued to top both GMV and sales volume rank on JD as of Jun 18. In terms of sales volume by smartphone brand, Xiaomi and Huawei have come after Apple while it is Huawei and Oppo which came after Apple if measured by GMV.

■ Appliances: GMV of >1,800 home appliances brands grew by >100% yoy. Major brands including Midea, Haier, Hisense, TCL, Gree and Xiaomi each generated >Rmb1bn GMV on JD during the entire 618 period. GMV of trade-in appliances grew >50% yoy.

■ Home living: GMV of major home living brands such as Jomoo, Sleemon, Arrow, Chivas Regal, Opple and Hegii exceeded Rmb100mn.

■ Supermarkets: GMV and user base of JD Supermarket both achieved double-digit growth. >1,000 brands on JD Supermarket achieved >100% GMV yoy growth. >1,500 fresh food brands achieved doubling GMV.

■ Fashion: GMV growth of 42 fashion categories including male and female apparel, outdoor equipment, jewelry and accessories exceeded industry average. >2,000 fashion brands including Uniqlo, Komfymed, Lao Feng Xiang doubled yoy, while GMV of 2,100 SME fashion merchants grew by >200% yoy.

## Solid momentum for new initiatives Jingxi, food delivery and overseas

■ Jingxi: GMV of Jingxi Self-Operated products doubled yoy, driven by 8-fold expansion of top 10 categories. Order volume of Jingxi Shop grew by 50% yoy, driven by 4-fold expansion in its top 8 categories.

■ Local services: On Jun 8, JD Travel launches pet tourism booking as China's first one-stop platform for pet travel. JD Food Delivery continued to partner with quality merchants such as Auntea Jenny, Mixue and McDonald's.

■ Overseas: JoyBuy kicked-off its summer Black Friday campaign since Jun 15, driving record transacting users and order volume on first day. GMV of >800 brands doubled vs. their initial on-boarding. Popular brands for European consumers on JoyBuy include Midea, Apple, TCL, Nintendo, Ecovacs.

■ Hong Kong JD Mall grand opening: JD also celebrated the grand opening of the Jingdong Mall physical store in Wan Chai Hong Kong on June 18th featuring 30,000 sq feet retail space with notable international and Chinese domestic brands. Some brands are deploying their physical retail channels in Hong Kong for the first time through JD.

## All-scenario AI adoption

JD's JoyAI large model has covered 3,000 scenarios in retail, logistics, health, industrial, food delivery and housekeeping with token usage up 7.7x yoy. Key AI applications include: 1) JoyInside intelligent hardware, 2) JoyStreamer digital avatar live-streaming; 3) JoyMarketing AI integrated marketing solution.

Figure 6. Top 10 smartphone brands on JD by GMV and sales volume as of Jun 18

<table><tr><td>Rank</td><td>By volume</td><td>By GMV</td></tr><tr><td>1</td><td>Apple</td><td>Apple</td></tr><tr><td>2</td><td>Xiaomi</td><td>Huawei</td></tr><tr><td>3</td><td>Huawei</td><td>Oppo</td></tr><tr><td>4</td><td>Oppo</td><td>Vivo / iQOO</td></tr><tr><td>5</td><td>Honor</td><td>Xiaomi</td></tr><tr><td>6</td><td>Vivo / iQOO</td><td>Honor</td></tr><tr><td>7</td><td>Realme</td><td>Realme</td></tr><tr><td>8</td><td>Philips</td><td>Samsung</td></tr><tr><td>9</td><td>Gionee</td><td>Nubia</td></tr><tr><td>10</td><td>K-Touch</td><td>Moto</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: JD, Sohu News, Citi

## Douyin

## New merchants growth on live-streaming and short video

According to a report from Ebrun dated Jun 20 (link), Douyin ecommerce has concluded its 2026 6.18 with over 120,000 merchants and over 570,000 streamers generating doubling live-streaming GMV yoy. Over 30,000 new merchants participated in 6.18 on Douyin for the first time with each generating GMV exceeding Rmb1mn, while long-tail streamers have contributed over 80% of total KOL GMV.

Douyin continued to support merchants by providing consumption vouchers to enhance operating efficiency and stimulate sales. Number of merchants whose GMV exceeded Rmb1mn driven by consumption vouchers grew by 152/432% yoy for live-streaming/short video respectively, compared to previous years.

Leveraging Douyin's content capabilities, the viewership of short videos that included a shopping cart increased by $57\%$ yoy. This growth helped increase the number of merchants generating Rmb1mn and Rmb10mn in GMV from short videos by $55\%$ and $56\%$ yoy, respectively. In live-streaming, over 120,000 merchants contributed to the doubling of GMV, while the number of merchants generating Rmb10mn in GMV through search functionality grew by $53\%$ yoy.

## Category performance

■ Fresh food: no. of merchants generating Rmb10mn GMV on Douyin Mall increased by 400% yoy. GMV of rice dumplings, durian and watermelon increased by 63/63/59% yoy.

■ Apparel: no. of new brand products increased by over 140% yoy. Number of apparel brands with >Rmb100mn live-streaming GMV exceeded 60% yoy, while number of outdoor merchants exceeding Rmb10mn GMV increased by 44% yoy.

■ Cosmetics: number of new brand cosmetic products increased by 144% yoy, while consumption vouchers have driven 67% yoy growth for international cosmetics brands with GMV >Rmb1mn.

■ Appliances: store GMV which participated in national subsidy scheme increased by 121% yoy, while order volume of dehumidifier, ice maker, fan and fridge increased by 130/133/450/85% yoy respectively.

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

# Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

Analysts' compensation is determined by Citi management and Citi's senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the “Firm”). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in equity research analyst compensation is arranging corporate access events between institutional clients and the management teams of covered companies. Typically, company management is more likely to participate when the analyst has a positive view of the company.

For financial instruments recommended in the Product in which the Firm is not a market maker, the Firm is a liquidity provider in such financial instruments (and any underlying instruments) and may act as principal in connection with transactions in such instruments. The Firm is a regular issuer of traded financial instruments linked to securities that may have been recommended in the Product. The Firm regularly trades in the securities of the issuer(s) discussed in the Produc

[中间内容因长度限制已省略]

ves, financial situation or needs of any particular investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a

subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.  
Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.
"""
