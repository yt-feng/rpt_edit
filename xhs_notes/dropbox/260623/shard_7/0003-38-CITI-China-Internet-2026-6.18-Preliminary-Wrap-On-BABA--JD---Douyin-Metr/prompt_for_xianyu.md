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

If you 

[中间内容因长度限制已省略]

information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a

subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.  
Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.
"""
