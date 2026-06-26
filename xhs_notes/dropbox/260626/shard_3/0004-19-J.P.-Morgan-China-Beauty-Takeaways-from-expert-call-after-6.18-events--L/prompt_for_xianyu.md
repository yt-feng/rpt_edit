你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

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

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); Neutral (over the duration of the price target indicated in this report, we expect this stock will perform in line with the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); and Underweight (over the duration of the price target indicated in this report, we expect this stock will underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe. NR is Not Rated. In this case, JPM has removed the rating and, if applicable, the price target, for this stock because of either a lack of a sufficient fundamental basis or for legal, regulatory or policy reasons. The previous rating and, if applicable, the price target, no longer should be relied upon. An NR designation is not a recommendation or a rating. Some stocks under coverage have a rating but no price target; in these cases, we expect the stock will outperform/perform in line/underperform the average 

[中间内容因长度限制已省略]

ies discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own

independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Securities (China) Company Limited. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
