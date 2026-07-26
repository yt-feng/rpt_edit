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
# European Luxury and Sporting Goods Weekly

Timely & Priceless

The European Luxury Goods sector was down -6% this week, significantly underperforming the MSCI Europe Index (-1%), reversing the strong performance last week (+4%). Q2/H1 reporting season continued, showing mixed trends across those that reported this week, Swatch (-18%), Moncler (-9%) and Zegna (-4%). The deliveries this week further confirm our view that, while the luxury backdrop was relatively OK in the quarter, performance remains highly polarised amidst macro volatility and with an increasingly discerning luxury consumer. The mixed deliveries from the reporters led to a large sector sell-off, with LVMH -10%, Kering -7%, Burberry -7% (mainly down on its own trading update last week) and Ferragamo -7%. Zooming in on the learnings from this week's reporting: Swatch reported a 2% beat on H1 sales, showing strong traction in the US and pockets of Asia, but still challenging trends in China (a read to all players, in our view); Moncler delivered group sales in line with expectations and a beat on EBIT, but softness at Moncler brand in Q2 confirmed the brand's structural seasonality and still very mixed trends among tourists in Europe (we think performance of tourist spend will be one of the most mixed outcomes of this reporting, driven by the brand's exposures to the different nationalities and specific brand's momentum); Zegna strong Q2 trading update, with double-digit DTC growth at all three brands, confirmed our positive views on both the attractiveness of the very high-end RTW category (in our view a key beneficiary of the wealth effect, especially in men) and growing strength of the Zegna brand portfolio. We also think this solid result should be read positively to Brunello Cucinelli (-4%), which we have placed on Positive Catalyst Watch into results next week. This leaves us with a mixed read-across as we move into the bulk of the reporting next week, with LVMH, Kering and Hermes up next. Positioning is definitely lighter than how we started reporting and hence the risk reward might be better now. Still, with such mixed learnings so far, we would continue to be very selective on stock picking, backing stories with self-help to grow, rather than trying to call a sector-wide inflection. And in this context, to us one of the main learnings of this week is how robust the Richemont delivery was, both in absolute and relative terms, increasingly warranting a valuation premium vs its own history and to the sector.

The European Sporting Goods sector was -6% this week, also underperforming the MSCI Europe Index, and continuing to be volatile driven by macro headlines. On (-9%) and Puma (-6%) underperformed, whereas adidas (-4%) and JD Sports (-2%) were also soft, on limited company specific newsflow. adidas (-4%, and -3% as we write) came under pressure after the company released sell-side consensus yesterday, but without accompanying a highly anticipated pre-release or guidance upgrade. Our discussions with investors suggest that expectations were higher following the positive World-Cup related headlines, thus a lack of an upgrade might lead to some disappointment and invite questions about the outlook for the rest of the year. Still, adidas is more than a Q2 trade, in our view, and the consistent innovation, brand building and execution across lifestyle and performance should support solid earnings delivery from H2 onwards. Elsewhere, read-across from Deckers (owners of Hoka and UGG, not covered) suggest resilient demand for premium sporting goods, despite a broadly challenging trading environment and softer sentiment in Europe. In China, Q2 updates from Anta and Xtep (both covered by Qian Yao) last Friday confirmed

See page 11 for analyst certification and important disclosures, including non-US analyst disclosures.

European Luxury & Sporting Goods

Chiara Battistini AC
(39-02) 8895-2700
chiara.x.battistini@JPM.com
JPM Securities plc/ JPM Securities (Asia Pacific) Limited

Wendy Liu AC
(44-20) 3493-9733
wendy.liu@JPM.com
JPM Securities plc

Apurva Vishwaraj
apurva.vishwaraj@jpmchase.com
JPM Securities plc

Victoria Saden
(44-20) 3493-0435
victoria.saden@JPM.com
JPM Securities plc

Specialist Sales contact details:

Olivia Petronilho - Specialist Sales - European Consumer
(44-20) 3493-3709
olivia.b.petronilho@JPM.com

that the retail environment for sporting goods remained tough, with both flagging short-term headwinds, including a lukewarm retail environment and unfavourable weather. On the other hand, Nike (covered by Matthew Boss) confirmed that it will take back its China e-commerce operations from its retail partners and concentrate online sales through DTC beginning in January 2027, in an effort to create a consistent consumer experience. In the near term, we see risks that the transition could add to the promotional environment in China, especially if retailers rush to clear online inventories by year end, although we think such a move is constructive for the sector in the medium term.

Table 1: Forex Watch

<table><tr><td>Forex</td><td>Value</td><td>Up/Dwn</td><td>Week%</td></tr><tr><td>$/€</td><td>1.138</td><td>▲</td><td>0.6%</td></tr><tr><td>€/£</td><td>1.170</td><td>▲</td><td>0.6%</td></tr><tr><td>$/£</td><td>1.331</td><td>▲</td><td>1.2%</td></tr><tr><td>SF/€</td><td>0.930</td><td>▼</td><td>-0.4%</td></tr><tr><td>Yen/€</td><td>186.430</td><td>▼</td><td>-0.3%</td></tr><tr><td>RMB/€</td><td>7.710</td><td>▲</td><td>0.5%</td></tr></table>

Source: Bloomberg Finance L.P.

## Luxury Goods

\- Moncler reported Q2 sales broadly in line and a 5% beat on EBIT excluding one-off charges. Moncler brand grew +3% ex-FX in Q2, below expectations, dragged by softer tourist trends and the "buy now, wear now" consumer behaviour delaying Fall/Winter purchases, while the Spring/Summer collection performed ahead of expectations. This retail delivery, in our view, is better than it looks at first sight, including a LFL that remained positive in a low seasonal quarter, successful Spring / Summer collection that was not pushed to its full potential and continued to be supported by good traction in most regions. H1 EBIT was a strong beat, driven by tight opex control and strong Q1 topline leverage. Read more in our note A slow Q2, and yet a strong H1 EBIT delivery.

\- Zegna Group reported a robust Q2 trading update with a very high-quality mix. Group sales came in at €517m, up 11% ex-FX, accelerating sequentially. The beat was driven primarily by very strong DTC performance, +17% ex-FX, with all three brands up double-digit DTC growth (inc Zegna brand +18%). Wholesale remained a drag but came in better than feared. By region, the Americas and Rest of APAC posted the strongest results, Greater China was solid while EMEA remained muted. Management highlighted that AUR was the primary driver of DTC growth, characterising it as a mix rather than a price story. Read more in our note Q2 26 trading update first takes: strong across the board.

\- Swatch Group reported its H1 26 results with a solid top-line beat of +8.5% ex-FX, driven by strong performance in the US, Japan, Korea and other high-potential markets such as India, Saudi Arabia and Mexico. Mainland China remained the drag where management does not expect an inflection in H2. Despite the top-line beat, EBIT was a significant miss dragged by negative FX and continued operating deleverage in the Production segment. Read more in our notes First Take - H1 Results, H1 Conference call snippets and Model Update - H1 26 Results.

\- Swiss Watch Exports in June improved to +11% from +0.4% in May on tougher comps. However, on a trading days adjusted basis, exports decelerated to +1% vs +12% in May (Q2 -1% vs Q1 +2%). By region, the US improved to +13% on softer comps, although on a two-year basis, US exports were still -7%. China remained volatile, -16.5% in June, while HK grew to +7%. Exports to Europe overall grew 12%. By price point, trends improved across categories: watches in the higher-priced bracket (>SF3,000) improved to +14% vs +4% last month, watches in the SF500–3,000 bracket improved to -5% vs May -17% despite tougher comps. Watches in the SF200–500 bracket accelerated to +54% vs May +24% on comps 10pp easier, and at the lower end, watches <SF200 improved to +10% vs. May -4.5%.

Figure 1: Exports yoy growth (value) by region  
![](images/b982213707d518c43dabc39249caee161314507bddebd4345d5e148d291970dc.jpg)  
Source: FHS data

Figure 2: Exports yoy growth (value) by region  
![](images/cd43e322d280382c5f2354aef05215e13c16b97a0f191f3524dee186ba9cee79.jpg)

\- Chow Tai Fook released its Q1 (CY Q2) trading update with Mainland China SSS +20% yoy in owned stores and +16% in franchised stores (71% of total stores), accelerating from CY Q1 +0.2%/-7% despite comps 1000bps tougher, with the release noting that the group is “outperforming the overall jewellery retail market.” Hong Kong+Macau SSS was very strong, up 42% vs Q1 +40%, on comps 25pp tougher, driven by positive consumer sentiment and strong customer traffic. Improvement in both Mainland China and HK was driven primarily by an acceleration in weight-based gold jewellery.

\- M&A: Frasers Group acquired a further 2.5mn Hugo Boss shares, lifting its total holding to about 30.28%. Frasers noted that the offer of €38/ share remains open, with the initial acceptance period ending on July 27 $^{th}$ .

\- ESG: 1) The EU has implemented a ban preventing major fashion groups from destroying unsold clothes and footwear, requiring them to instead re-sell, re-purpose or donate returns and over-production. Medium-sized companies will be subject to the same rules from 2030; 2) As part of an investigation into alleged worker exploitation at sub-contractors, the Italian police requested documents on governance and supply-chain controls from nine high-end fashion firms including Brunello Cucinelli, Moncler, Chanel and Bulgari. Brunello Cucinelli said in a statement it was surprised and deeply saddened that part of the materials intended for its packaging were found at an unsuitable workplace, despite supplier checks and fair pricing, and pledged full co-operation to protect workers and the wider 'Made in Italy' brand.

\- Management on the move: 1) Moncler appointed Sidney Toledano as Director, replacing Alexandre Arnault and Geoffroy van Raemdonck who both resigned from the Board. Toledano brings extensive industry experience, most recently serving as Special Advisor to the Chairman and CEO of LVMH since 2024; 2) Chanel appointed Helene de Tissot as its next CFO, replacing Philippe Blondiaux who will retire at year-end. De Tissot joins from Pernod Ricard, where she spent over two decades, including eight years as EVP of Finance and Technology and a stint as CFO for Asia. She will assume full responsibilities in January, reporting to CEO Leena Nair; 3) Tapestry appointed Jonathan Saunders as creative director for Kate Spade New York, filling a vacant role. Saunders brings experience from Calvin Klein, Diane von Furstenberg, and Tiffany & Co; 4) LVMH has appointed Yann Musquin as brand MD for LVMH Fragrance Brands from Aug. 3, replacing Romain Spitzer who moves on to become CEO of Kering's Bottega Veneta; Musquin currently serves as chief brand officer for Givenchy Parfums and Beauty and will

report to Veronique Courtois. His focus will be on boosting the desirability of the Givenchy and Kenzo perfume brands.

\- Small but interesting:1) China's surveyed youth unemployment in urban areas rose to 14.9% in June, the highest for June since the government excluded university students from the sample more than two years ago. The ratio may increase further, especially as a record 12.7m graduates are expected to enter the workforce this year;2) Christie's and Sotheby's highlighted growth in the luxury second-hand market, noting that Millennials and Gen Z now account for about a third of watch bidders. They also noted increased demand in the jewelry category; 3) Hermes opened a new store at Chatswood Chase in Sydney, Australia, following recent openings in California and Australia; 4) Prada tapped Academy Award-winning filmmaker Barry Jenkins to direct its fall 2026 campaign, featuring a cast of international actors. This marks Jenkins' first creative collaboration with a fashion label; 5) The docufilm Brunello: The Gracious Visionary, produced by Brunello Cucinelli S.p.A., has secured distribution deals across Europe, Asia and the Middle East, with a UK, Ireland and North America release set for 24 July; 6) Moët & Chandon (owned by LVMH) returned as title sponsor of the Belgian Grand Prix for the second consecutive year, reaffirming its historic connection with the sport and its iconic role in celebrating Formula 1's greatest victories; 7) LMDV Capital, the family office of EssilorLuxottica's heir Leonardo Maria Del Vecchio, signed a deal with Apollo to refinance its c.€1.1bn debt at an 8% interest rate, with Apollo also reportedly ready to increase the facility to c.€10bn to potentially fund a buy-out of two of Leonardo Maria's siblings in the Del Vecchio family holding, Delfin; 8) Dior opened its largest boutique in Brazil at the Cidade Jardim complex in Sao Paulo, relocating and expanding from its previous c.5,380 square foot store at the same complex which it had operated since 2013.

## Sporting Goods

\- Deckers (NC) reported its Q1 27 (CYQ2, Apr-Jun) results with sales +5% ex-FX (CYQ1 +8%) or +6% reported, incl. Hoka sales +8% (CYQ1 +14.5%) reported yoy driven by DTC sales +17%, which was broad based with strong demand for most popular products, alongside well-received updates to emerging models. Hoka WS sales were +3%, affected by an expected timing shift in shipment. By region, the US was solid, Asia was strong and management called the consumer in Europe “probably a bit more pressured than it is in the US” due to energy prices, but highlighted strong underlying demand. On the FY27 outlook, the company reiterated its topline guidance (Hoka sales +LDD%), while upgraded profitability targets.

\- Into the Back-to-School Season: 1) According to data from Circana's latest consumer survey, running-inspired styles, as well as low-profile sneakers and Mary Jane-inspired silhouettes are expected to stand out in this year's back-to-school season. This reflects the broader fashion trends, as well as a focus on “versatility,” as families look for footwear that can transition seamlessly between the classroom, extra-curricular activities, and other events. Sneakers, including cleats, generate about two-thirds of footwear sales during the peak back-to-school months of July and August. 2) National Retail Federation (NRF) forecasts US back-to-school spending of \$146.8bn, up 14% from \$128.2bn in 2025, based on a survey of 7,677 consumers from July 1 to 8. Clothing, accessories and shoes are among the top categories. In the past, retailers usually kicked off the season around mid-July, but this year, early shopping was already seen in June, although spurred by heightened back-to-school promotions.

\- US Tariff: The Trump administration imposed new tariffs of 10% and 12.5% on goods from 60 trading partners, over allegations of lax enforcement of forced labour bans, just as a temporary 10% global tariff expired. Among the major sporting goods manufacturing hubs in Southeast Asia, Vietnam was assigned a 12.5% rate, whereas Cambodia, India and Indonesia were assigned 10%. The US also announced an additional 25% tariff on imports from Brazil, which could also face a further proposed 12.5% Section 301 duty on top.

\- Nike (covered by Matthew Boss) announced it will end online mainland China sales through distributors Topsports and Pou Sheng from the beginning of next year. Online sales of Nike products cont

[中间内容因长度限制已省略]

mance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 24 Jul 2026 10:37 AM BST

Disseminated 24 Jul 2026 10:37 AM BST
"""
