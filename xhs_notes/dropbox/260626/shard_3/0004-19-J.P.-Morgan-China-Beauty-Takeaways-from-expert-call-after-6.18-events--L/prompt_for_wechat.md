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
# JPM

## China Beauty

## Takeaways from expert call after 6.18 events: Local leaders hold ground, international players maintain momentum

We hosted a China beauty expert call on 23 June to decode the latest industry shifts and market evolution following the recently concluded 6.18 events. Beauty sector GMV grew $11\%$ yoy during 6.18 events (5/13-6/18; platforms including Tmall, JD, PDD, Douyin and Kuaishou; Source: Analysis.cn 易观), outperforming overall GMV growth of $6\%$ , continuing the recovery trajectory (cosmetics retail sales outpacing overall retail sales in the past 11 months; Source: NBS). Key highlights from the discussion include: (1) a divergence of pricing range trends between platforms: Tmall's $>Rmb800$ ASP segment GMV up $>20\%$ , while Douyin's Rmb300-500 segment up $c25\%$ ; (2) the effective discount level deepened further, given platform coupons, livestreaming coupons and government subsidies, despite the leading brands' largely stable nominal discounts; (3) the leading domestics brands with solid brand equity held their ground, with Proya remaining in the Top 4 on both Tmall and Douyin, and Mao Geping (MGP) and Winona GMV up $>20\%$ ; and (4) international brands' momentum continued, with international brands reclaiming the No.1 spot on both Tmall and Douyin, and overall ranking improving across the board. MGP is our top pick in the China beauty market, given its superior positioning for the experience-led consumption trend.

\- Leading domestic brands held their ground. Despite international brands' recovery and overall domestic brands' weakness, the leading domestic brands with solid brand equity and product offerings still delivered quality growth: (1) MGP continued to lead growth among the leading domestic brands, with overall GMV up c35% and its new IP crossover collections (with Panda Creation) highly favored by consumers. (2) The Proya brand maintained its leading position (No. 3/4 on Tmall/Douyin, likely No.1 on Tmall during 5/21-6/21), with GMV recovering to positive growth (vs. sales -10% in 2025). (3) Botanee's Winona registered solid growth of >20% on both Tmall and Douyin. (4) Chicmax's KANS faced pressure during the promotion events (negative GMV growth on Douyin, No.6 ranking on Douyin vs. No.2 in April and No.1 in January-March), given its mass-market positioning and value-for-money pricing strategy. However, the expert remained confident in Chicmax's fundamentals due to its: (a) comprehensive brand portfolio, such as its rapidly growing brand Newpage (triple-digit GMV growth during the event); (b) R&D strength; (c) capable management team; and (d) aggressive culture. (5) Giant Biogene's Comfy has recovered to positive growth, following questions about its product formula last year. (6) Forest Cabin delivered strong momentum on Douyin, with triple-digit GMV growth.

\- International brands' momentum continued. Most international brands have registered $>10\%$ GMV growth in the past year, according to the expert, and the momentum was verified during the 6.18 events. In terms of rankings: (1) Skin Ceuticals (owned by L'Oréal, covered by Celine Pannutil, CFA, see latest report) and Estée Lauder (covered by Andrea Teixeira, CFA, see latest report) reclaimed the No.1 position on Tmall and Douyin,

## Consumer

Qian Yao AC  
(86-21) 6106 6277  
qian.q.yao@JPM.com  
SAC Registration Number: S1730521050001  
JPM Securities (China) Company Limited

Carson Fan  
(86-21) 6106-6294  
rong.fan@JPM.com  
SAC Registration Number: S1730522070002  
JPM Securities (China) Company Limited

Andrea Teixeira, CFA  
(1-212) 622-6735  
andrea.f.teixeira@JPM.com  
JPM Securities LLC

Celine Pannuti, CFA (44-20) 7134-7123  
celine.pannuti@JPM.com  
JPM Securities plc

25 May 2026 Mao Geping: Global China Summit 2026 takeaways

25 May 2026 Chicmax: Global China Summit 2026 takeaways

24 Apr 2026 Proya: Ramp up of emerging brands; enhanced shareholder return; maintain OW

31 Mar 2026 Chicmax: Multi-brand portfolio to support long-term vision

31 Mar 2026 Mao Geping: Robust FY25; experience-led model drives long-term growth; NDR takeaways

16 Mar 2026 China Beauty: Takeaways from expert call post the 3.8 events

26 Feb 2026 China Jewelry & Beauty: Spring Festival Gala as a catalyst: how traditional heritage is reshaping Chinese brands

21 Jan 2026 Chicmax: China Opportunity Forum takeaways: positive 2026 outlook

18 Jan 2026 China Sports, Beauty & Jewelry: 2026: Seeking Alpha Led by Experience

13 Jan 2026: Mao Geping: Positive in 2026; strategic co-operation; shareholding reduction plan; maintain OW

respectively; La Mer (also owned by Estée Lauder) has had the best performance on Douyin over the past three years, while SK-II (owned by Procter & Gamble, covered by Andrea Teixeira, CFA, see latest report) also recovered spots in both platforms; and (2) overall international brands' rankings improved across the board, with 9/6 seats among the Top 10 on Tmall/Douyin (vs. 8/5 during Double-11 2025), driven by: (a) expanded KOL livestreaming collaborations, especially mid-tier KOLs; (b) successful launches of more sets with attractive prices; and (c) gifts with purchase with greater emotional value, capturing the gifting demand. The expert expects this momentum to continue in the coming one to two years, supported by the momentum of: (1) midrange to high-end segments on Tmall; and (2) KOL livestreaming and Douyin Mall on Douyin. However, the expert was cautious about the growth prospects of international brands targeting the mass market, such as the L'Oréal brand and Olay (owned by P&G), given the fierce competition from domestic brands.

Table 1: Tmall Top 20 cosmetics brands during promotion events (in terms of GMV)

<table><tr><td>Ranking</td><td>5/16 - 6/20
18 Jun 2025</td><td>10/15 - 11/11
Double-11 2025</td><td>5/6 - 6/21
18 Jun 2026</td></tr><tr><td>1</td><td>Proya 珀莱雅</td><td>Proya 珀莱雅</td><td>Skin Ceuticals 修丽可</td></tr><tr><td>2</td><td>Lancôme 兰蔻</td><td>Estée Lauder 雅诗兰黛</td><td>Estée Lauder 雅诗兰黛</td></tr><tr><td>3</td><td>L&#x27;Oréal Paris 巴黎欧莱雅</td><td>Lancôme 兰蔻</td><td>Proya 珀莱雅</td></tr><tr><td>4</td><td>Estée Lauder 雅诗兰黛</td><td>L&#x27;Oréal Paris 巴黎欧莱雅</td><td>Lancôme 兰蔻</td></tr><tr><td>5</td><td>La Mer 海蓝之谜</td><td>Skin Ceuticals 修丽可</td><td>SK-II</td></tr><tr><td>6</td><td>Skin Ceuticals 修丽可</td><td>La Mer 海蓝之谜</td><td>L&#x27;Oréal Paris 巴黎欧莱雅</td></tr><tr><td>7</td><td>SK-II</td><td>SK-II</td><td>La Mer 海蓝之谜</td></tr><tr><td>8</td><td>HR 赫莲娜</td><td>Winona 薇诺娜</td><td>Clarins 娇韵诗</td></tr><tr><td>9</td><td>CPB 肌肤之钥</td><td>Olay 玉兰油</td><td>HR 赫莲娜</td></tr><tr><td>10</td><td>Clarins 娇韵诗</td><td>CPB 肌肤之钥</td><td>CPB 肌肤之钥</td></tr><tr><td>11</td><td>YSL 圣罗兰</td><td>YSL 圣罗兰</td><td>YSL 圣罗兰</td></tr><tr><td>12</td><td>Winona 薇诺娜</td><td>Clarins 娇韵诗</td><td>Shiseido 资生堂</td></tr><tr><td>13</td><td>Olay 玉兰油</td><td>HR 赫莲娜</td><td>Comfy 可复美</td></tr><tr><td>14</td><td>Kiehl&#x27;s 科颜氏</td><td>Guerlain 娇兰</td><td>Guerlain 娇兰</td></tr><tr><td>15</td><td>Shiseido 资生堂</td><td>Shiseido 资生堂</td><td>Winona 薇诺娜</td></tr><tr><td>16</td><td>Comfy 可复美</td><td>Kiehl&#x27;s 科颜氏</td><td>Olay 玉兰油</td></tr><tr><td>17</td><td>La Roche-Posay 理肤泉</td><td>La Roche-Posay 理肤泉</td><td>La Roche-Posay 理肤泉</td></tr><tr><td>18</td><td>Maogeping 毛戈平</td><td>Comfy 可复美</td><td>Maogeping 毛戈平</td></tr><tr><td>19</td><td>Guerlain 娇兰</td><td>Chando 自然堂</td><td>Kiehl&#x27;s 科颜氏</td></tr><tr><td>20</td><td>TIMAGE 彩棠</td><td>Maogeping 毛戈平</td><td>Chando 自然堂</td></tr></table>

Source: Global E-businessman, as of 22 June 2026. Note: Red text = domestic brands; red & bold text = domestic brands owned by listed companies.

Table 2: Douyin Top 20 cosmetics brands during promotion events (in terms of GMV)

<table><tr><td>Ranking</td><td>5/13 - 6/18 18 Jun 2025</td><td>10/9 - 11/11 Double-11 2025</td><td>5/15 - 6/18 18 Jun 2026</td></tr><tr><td>1</td><td>KANS 韩束</td><td>KANS 韩束</td><td>Estée Lauder 雅诗兰黛</td></tr><tr><td>2</td><td>Proya 珀莱雅</td><td>Proya 珀莱雅</td><td>HR 赫莲娜</td></tr><tr><td>3</td><td>HR 赫莲娜</td><td>L&#x27;Oréal 欧莱雅</td><td>La Mer 海蓝之谜</td></tr><tr><td>4</td><td>L&#x27;Oréal 欧莱雅</td><td>HR 赫莲娜</td><td>Proya 珀莱雅</td></tr><tr><td>5</td><td>Estée Lauder 雅诗兰黛</td><td>Grainrain 谷雨</td><td>Lancôme 兰蔻</td></tr><tr><td>6</td><td>La Mer 海蓝之谜</td><td>Pechoin 百雀羚</td><td>KANS 韩束</td></tr><tr><td>7</td><td>Lancôme 兰蔻</td><td>Chando 自然堂</td><td>L&#x27;Oréal 欧莱雅</td></tr><tr><td>8</td><td>Chando 自然堂</td><td>Estée Lauder 雅诗兰黛</td><td>Chando 自然堂</td></tr><tr><td>9</td><td>SK-II</td><td>Whoo 后</td><td>Pechoin 百雀羚</td></tr><tr><td>10</td><td>Whoo 后</td><td>Lancôme 兰蔻</td><td>SK-II</td></tr><tr><td>11</td><td>na</td><td>Forest Cabin 林清轩</td><td>Grainrain 谷雨</td></tr><tr><td>12</td><td>na</td><td>SK-II</td><td>Mistine 蜜斯婷</td></tr><tr><td>13</td><td>na</td><td>HBN</td><td>CPB 肌肤之钥</td></tr><tr><td>14</td><td>na</td><td>Winona 薇诺娜</td><td>Maogeping 毛戈平</td></tr><tr><td>15</td><td>na</td><td>Marubi 丸美</td><td>Forest Cabin 林清轩</td></tr><tr><td>16</td><td>na</td><td>La Mer 海蓝之谜</td><td>YSL 圣罗兰</td></tr><tr><td>17</td><td>na</td><td>Galenic 科兰黎</td><td>Skin Ceuticals 修丽可</td></tr><tr><td>18</td><td>na</td><td>CPB 肌肤之钥</td><td>Dirovo 蒂洛薇</td></tr><tr><td>19</td><td>na</td><td>Olay 玉兰油</td><td>Comfy 可复美</td></tr><tr><td>20</td><td>na</td><td>Shiseido 资生堂</td><td>Whoo 后</td></tr></table>

Source: BeautyInSight, as of 22 June 2026. Note: Red text = domestic brands; red & bold text = domestic brands owned by listed companies.

# Companies Discussed in This Report (all prices in this report as of market close on 24 June 2026, unless otherwise indicated)

Mao Geping - H(1318.HK/HK\$51.80/OW)

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

\- Market Maker/ Liquidity Provider: JPM is a market maker and/or liquidity provider in the financial instruments of/related to Mao Geping - H or related entities.

\- Market Maker/ Liquidity Provider (Hong Kong): JPM Securities (Asia Pacific) Limited and/or JPM Broking (Hong Kong) Limited and/or an affiliate is a market maker and/or liquidity provider in the securities of Mao Geping - H or related entities and/or warrants or options thereon, which are listed or traded on The Stock Exchange of Hong Kong Limited.

\- Manager or Co-manager: JPM acted as manager or co-manager in a public offering of securities or financial instruments (as such term is defined in Directive 2014/65/EU) of/for Mao Geping - H or related entities within the past 12 months.

\- Client: JPM currently has, or had within the past 12 months, the following entity(ies) as clients: Mao Geping - H or related entities.

\- Client/Investment Banking: JPM currently has, or had within the past 12 months, the following entity(ies) as investment banking clients: Mao Geping - H or related entities.

\- Client/Non-Investment Banking, Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-investment-banking, securities-related: Mao Geping - H or related entities.

\- Investment Banking Compensation Received: JPM has received in the past 12 months compensation for investment banking services from Mao Geping - H or related entities.

\- Potential Investment Banking Compensation: JPM expects to receive, or intends to seek, compensation for investment banking services in the next three months from Mao Geping - H or related entities.

\- Non-Investment Banking Compensation Received: JPM has received compensation in the past 12 months for products or services other than investment banking from Mao Geping - H or related entities.

\- Debt Position: JPM may hold a position in the debt securities of Mao Geping - H or related entities, if any.

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

Mao Geping - H (1318.HK, 1318 HK) Price Chart  
![](images/df030bf2ecd8e6c65ddc6312a5254dbd0fad2104dc00da51e0c3c81c88ef7655.jpg)

<table><tr><td>Date</td><td>Rating</td><td>Price (HK$)</td><td>Price Target (HK$)</td></tr><tr><td>12-Oct-25</td><td>OW</td><td>99.55</td><td>128</td></tr><tr><td>14-Jan-26</td><td>OW</td><td>87.20</td><td>130</td></tr></table>

Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends. Initiated coverage Oct 12, 2025. All share prices are as of market close on the previous business day.

The chart(s) show JPM's continuing coverage of the stocks; the current analysts may or may not have covered it over the entire period.

JPM ratings or designations: OW = Overweight, N = Neutral, UW = Underweight, NR = Not Rated

## Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); Neutral (over the duration of the price target indicated in this report, we expect this stock will perform in line with the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); and Underweight (over the duration of the price target indicated in this report, we expect this stock will underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe. NR is Not Rated. In this case, JPM has removed the rating and, if applicable, the price target, for this stock because of either a lack of a sufficient fundamental basis or for legal, regulatory or policy reasons. The previous rating and, if applicable, the price target, no longer should be relied upon. An NR designation is not a recommendation or a rating. Some stocks under coverage have a rating but no price target; in these cases, we expect the stock will outperform/perform in line/underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe of the relevant duration of the region. In our Asia (ex-Australia and ex-India) and U.K. small- and mid-cap Equity Research, each stock's expected total return is compared to the expected total return of a benchmark country market index, not to those Research Analysts' coverage universe. If it does not appear in the Important Disclosures section of this report, the certifying Research Analyst's coverage universe can be found on JPM's Research website, https://www.JPMmarkets.com.

Coverage Universe: Yao, Qian : Anta Sports (2020) (2020.HK), Best Pacific (2111) (2111.HK), Bosideng (3998.HK), Botanee (300957.SZ), CTG Duty-Free – A (601888.SS), Chicmax (2145.HK), Chow Tai Fook Jewellery (1929) (1929.HK), HLA Group Corp Ltd - A (600398.SS), Lao Feng Xiang - A (600612.SS), Laopu Gold - H (6181.HK), Li Ning (2331) (2331.HK), Luolai Lifestyle - A (002293.SZ), Luthai Textile - A (000726.SZ), Mao Geping - H (1318.HK), Marubi (603983.SS), Peacebird Fashion - A (603877.SS), Proya (603605.SS), Semir Garment - A (002563.SZ), Shanghai Jahwa (600315.SS), Shenzhou International (2313) (2313.HK), Xtep International (1368.HK)

JPM Equity Research Ratings Distribution, as of April 04, 2026

<table><tr><td></td><td>Overweight (buy)</td><td>Neutral (hold)</td><td>Underweight (sell)</td></tr><tr><td>JPM Global Equity Research Coverage*</td><td>51%</td><td>37%</td><td>12%</td></tr><tr><td>IB clients**</td><td>83%</td><td>79%</td><td>74%</td></tr><tr><td>JPMS Equity Research Coverage*</td><td>49%</td><td>39%</td><td>13%</td></tr><tr><td>IB clients**</td><td>94%</td><td>93%</td><td>85%</td></tr></table>

\*Please note that the percentages may not add to 100% because of rounding.  
\*\*Percentage of subject companies within each of the "buy," "hold" and "sell" categories for which JPM has provided investment banking services within the previous 12 months.

For purposes of FINRA ratings distribution rules only, our Overweight rating falls into a buy rating category; our Neutral rating falls into a hold rating category; and our Underweight rating falls into a sell rating category. Please note that stocks with an NR designation are not included in the table above. This information is current as of the end of the most recent calendar quarter.

Equity Valuation and Risks: For valuation methodology and risks associated with covered companies or price targets for covered companies, please see the most recent company-specific research report at http://www.JPMmarkets.com, contact the primary analyst or your J.P. Mo

[中间内容因长度限制已省略]

re subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own

independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Securities (China) Company Limited. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
