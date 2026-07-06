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
# Asia-Pacific Growth Monitor: Better on balance as energy pressures begin to ease

This publication summarizes regional and country-specific growth data across the Asia-Pacific economies we cover. $^{1}$ We include June PMIs, but the most recent “hard” economic indicators refer to May in most cases.

The latest set of (June) PMIs was mixed in terms of month-on-month changes, though generally consistent with solid factory sector growth in terms of absolute levels. China saw both its official PMIs strengthen while the unofficial measures weakened. India’s manufacturing and services indexes both weakened, while Japan’s both strengthened. Supplier delays remained an issue for many manufacturers in the region.

\- Our GS Current Activity Indicators (CAIs) generally held up well or improved in May and preliminary June data. We upgraded GDP growth forecasts at least slightly in many economies in recent weeks, reflecting the easing of energy price pressures.

■ Financial conditions eased in the majority of economies in recent weeks, reflecting relief from oil prices, among other factors. Korea and Taiwan continue to see massive easing as equity markets surge. Thailand has also eased, with FX depreciation playing a key role. Conversely, Indonesia has seen a meaningful FCI tightening amid policy rate hikes and an equity market selloff.

Andrew Tilton
+852-2978-1802 |
andrew.tilton@gs.com
GS (Asia) L.L.C.

Andrew Boak, CFA
+61(2)9321-8576 |
andrew.boak@gs.com
GS Australia Pty Ltd

Goohoon Kwon, CFA
+852-2978-0048 |
goohoon.kwon@gs.com
GS (Asia) L.L.C.

Hui Shan
+852-2978-6634 | hui.shan@gs.com
GS (Asia) L.L.C.

Tomohiro Ota
+81(3)4587-9984 |
tomohiro.ota@gs.com
GS Japan Co., Ltd.

Santanu Sengupta
+91(22)6616-9042 |
santanu.sengupta@gs.com
GS India SPL

Yuriko Tanaka
+81(3)4587-9964 |
yuriko.tanaka@gs.com
GS Japan Co., Ltd.

Lisheng Wang
+852-3966-4004 |
lisheng.wang@gs.com
GS (Asia) L.L.C.

Chris Poh
+65-6889-3454 | chris.poh@gs.com
GS (Singapore) Pte

(Green/red = faster/slower growth for economy shown)  
Regional growth - summary indicators  
Exhibit 1: Early CAI data suggest improvement  
![](images/aef12e93368ecb8d671a521c2ceae0cc6e0d779edd621b556088c6b7ad177fd0.jpg)  
Source: GS Global Investment Research

Exhibit 2: Improvement in China CAI  
![](images/78718ce7269b59292ef44da457ff60f82ea50ccb4d805f5d2f2b00d4f0831f3f.jpg)  
Source: GS Global Investment Research

Exhibit 3: We have upgraded our growth forecasts for many countries recently  
![](images/dc356ed2af482d8a9fcc4f903ee51b0eee6fa349b6cf4ec26487174a78f117c5.jpg)  
Source: GS Global Investment Research

Exhibit 4: Recent data have surprised to the upside in Japan, to the downside in Australia  
![](images/5ec5d69eed27c3d2201cf10f2e0cb1f5e1a3aae7bd4d1c1a3b8ac74142c35d0d.jpg)  
Source: GS Global Investment Research

GS Current Activity Indicator (mom, annual rate)

<table><tr><td rowspan="2"></td><td colspan="6">2025</td><td colspan="6">2026</td></tr><tr><td>J</td><td>A</td><td>S</td><td>O</td><td>N</td><td>D</td><td>J</td><td>F</td><td>M</td><td>A</td><td>M</td><td>J</td></tr><tr><td>Mainland China</td><td>4.9</td><td>4.6</td><td>5.7</td><td>4.4</td><td>4.8</td><td>4.8</td><td>6.4</td><td>6.6</td><td>5.7</td><td>2.9</td><td>4.4</td><td></td></tr><tr><td>South Korea</td><td>4.4</td><td>2.2</td><td>6.6</td><td>1.6</td><td>2.1</td><td>3.5</td><td>3.8</td><td>3.9</td><td>4.1</td><td>1.7</td><td>2.1</td><td></td></tr><tr><td>Taiwan</td><td>3.3</td><td>3.7</td><td>5.2</td><td>3.2</td><td>7.0</td><td>8.5</td><td>9.2</td><td>4.8</td><td>9.3</td><td>3.5</td><td>7.5</td><td></td></tr><tr><td>India</td><td>7.2</td><td>7.1</td><td>7.6</td><td>7.8</td><td>8.6</td><td>7.1</td><td>7.0</td><td>6.9</td><td>6.5</td><td>7.7</td><td>7.8</td><td>7.7</td></tr><tr><td>Indonesia</td><td>5.1</td><td>4.4</td><td>5.1</td><td>5.5</td><td>4.9</td><td>6.0</td><td>5.6</td><td>5.9</td><td>5.2</td><td>8.0</td><td>5.1</td><td></td></tr><tr><td>Malaysia</td><td>9.0</td><td>5.1</td><td>4.9</td><td>9.3</td><td>6.6</td><td>8.9</td><td>7.1</td><td>2.1</td><td>1.7</td><td>15.9</td><td>6.2</td><td></td></tr><tr><td>Philippines</td><td>6.3</td><td>4.6</td><td>5.2</td><td>6.2</td><td>5.9</td><td>7.3</td><td>6.1</td><td>6.3</td><td>7.1</td><td>5.1</td><td>5.7</td><td></td></tr><tr><td>Thailand</td><td>0.6</td><td>-2.7</td><td>11.1</td><td>12.1</td><td>1.7</td><td>8.2</td><td>15.1</td><td>3.8</td><td>2.2</td><td>2.3</td><td>-1.3</td><td></td></tr><tr><td>Japan</td><td>-0.9</td><td>0.1</td><td>1.2</td><td>1.1</td><td>0.1</td><td>0.7</td><td>4.1</td><td>1.3</td><td>0.0</td><td>2.5</td><td>2.1</td><td>1.7</td></tr><tr><td>Hong Kong</td><td>6.3</td><td>5.0</td><td>5.8</td><td>8.5</td><td>6.3</td><td>10.1</td><td>11.4</td><td>6.5</td><td>9.5</td><td>7.9</td><td>8.6</td><td></td></tr><tr><td>Singapore</td><td>8.3</td><td>1.6</td><td>6.0</td><td>11.6</td><td>10.4</td><td>7.1</td><td>9.9</td><td>7.4</td><td>5.5</td><td>9.6</td><td>11.3</td><td>9.5</td></tr><tr><td>Australia</td><td>2.4</td><td>2.4</td><td>2.7</td><td>2.7</td><td>2.5</td><td>2.1</td><td>2.0</td><td>2.2</td><td>2.0</td><td>0.7</td><td>1.4</td><td>1.5</td></tr><tr><td>New Zealand</td><td>3.3</td><td>3.0</td><td>3.6</td><td>3.2</td><td>3.4</td><td>4.2</td><td>4.3</td><td>3.9</td><td>3.0</td><td>1.9</td><td>1.8</td><td>2.7</td></tr></table>

Note: Monthly CAI values are only shown after more than 20% of the constituent data has been reported.  
Source: GS Global Investment Research

## Regional manufacturing, services, and trade

Exhibit 6: Aggregate PMIs in modest expansion territory  
![](images/96ae5ee2130e02c01a0e33b39bc7bed29d172e5e295608f74f9434236f57e415.jpg)  
Source: Haver Analytics, GS Global Investment Research

Exhibit 7: Prospects for manufacturing improvement looking more positive  
![](images/bc96c37dd4abac0b6addc09ddb51f38d24ab2ac0ec85c1625998fb54dc3dad5a.jpg)  
Source: Haver Analytics, GS Global Investment Research

Exhibit 8: Supply chain disruptions still a concern  
![](images/8d728c28e8fda5ff4d53c95e4074f9bc2144046119e77304212ef784893b428c.jpg)  
Source: Haver Analytics, GS Global Investment Research

Exhibit 9: Services PMIs down in India, up in Japan  
![](images/7f58d541ccfbcaa94b1b33549e94cf9761da2f7248fc7b8cd37517762d6ae113.jpg)  
China is average of NBS non-mfg PMI and RatingDog services PMI.  
Source: Haver Analytics, GS Global Investment Research

Exhibit 10: Trade activity continues to surge  
![](images/9bae6211b4eeadd8acbada75df75c3c2990ae03bec1bd3c0a30fec2b2004190d.jpg)  
Source: CPB World Trade Monitor, Haver Analytics, GS Global Investment Research

Exhibit 11: East Asian exports picked up in May  
![](images/df9f5988327db62b7d43168424c8d4ef17c59e366c4444b157ad4d87173616d1.jpg)  
Source: Haver Analytics, GS Global Investment Research

## EM Asia - growth and financial conditions by economy

We show the 3-month averages of our CAIs in these charts, to smooth results and ease comparison with GDP data. The very latest CAI data and FCI data can be found on the GS research portal. Note that in 2023 we updated and revised our China CAI.

Exhibit 12: China growth and financial conditions  
![](images/58b163f46c6e60cc41fc9138747a9d4fcd9ccc2c3a143b96de73f92b146d9bcf.jpg)  
Source: Haver Analytics, GS Global Investment Research

Exhibit 13: Korea growth and financial conditions  
![](images/7be410c2c6b091862adbbe4fc1eccf396642b316c2bef47d7362931ff4a6644b.jpg)  
Source: Haver Analytics, CEIC, GS Global Investment Research

Exhibit 14: Taiwan growth and financial conditions  
![](images/681519ed9d1fc85ce6769508caeda297ee45ca96b6789afdaf446a1a0d74a41c.jpg)  
Source: Haver Analytics, CEIC, GS Global Investment Research

![](images/ccdb9eb1505da6f812ab88bac0e07872f0571db1406236e6418da39727460769.jpg)

Exhibit 15: India growth and financial conditions  
![](images/92001d6ffbe958c393873d4d1671521cc087597ae61c8eed141a0d72d5adcfbc.jpg)  
Source: Haver Analytics, CEIC, GS Global Investment Research

Exhibit 16: Indonesia growth and financial conditions  
![](images/98c27d1d90df3e541bf9bc4970ea18626bb2cf0439ee0de99eba400e22de2176.jpg)  
Source: Haver Analytics, CEIC, GS Global Investment Research

Exhibit 17: Malaysia growth and financial conditions  
![](images/87286e8e44ec69186fd2eb4b532ffed279390d34d067f0a1801fceeb13d82e76.jpg)  
Source: Haver Analytics, CEIC, GS Global Investment Research

![](images/999646ad33fc4a39fadbf0006b8f5f1853f50413985ab1833f67c3d3ea249ace.jpg)

Exhibit 18: Philippines growth and financial conditions  
![](images/24d54d908f91b78dd287624b8e31d3ba2c285b957611be9e8783cf11663faecf.jpg)  
Source: Haver Analytics, CEIC, GS Global Investment Research

Exhibit 19: Thailand growth and financial conditions  
![](images/eefc14da61e337ae6cda5a30a9925581ad036c58790adf01cb651fad3c668473.jpg)  
Source: Haver Analytics, CEIC, GS Global Investment Research

![](images/92a526627c7edc382e04e3e0d7e0ccafa71df3c5c210c610ce55b4af8639f069.jpg)

## DM Asia - growth and financial conditions by economy

Exhibit 20: Japan growth and financial conditions  
![](images/8fb4e9eba81360f77520442985d24cdc45d4d48ee7bf96e0ce4e89fae08cf260.jpg)  
Source: Haver Analytics, CEIC, GS Global Investment Research

Exhibit 21: Hong Kong growth and financial conditions  
![](images/6f0e77017bde9f6d254ae9be4f78acbfd6ee36fb117244d77af8c805a5493420.jpg)

![](images/6051f5bebf10ab307a5b837551cbc49bf4d2b5dd66b76ac5947f146447a3f82a.jpg)  
Source: Haver Analytics, CEIC, GS Global Investment Research

Exhibit 22: Singapore growth and financial conditions  
![](images/7fffbe89b929758ad4c1b9f6810c44c50427f2a28323f32829bac06f4b65d504.jpg)  
Source: Haver Analytics, CEIC, GS Global Investment Research

![](images/3f4ff7a1bd53f6580282cd9f2dcf73cff29e6198077a0e00b8791e028e8600ae.jpg)

Exhibit 23: Australia growth and financial conditions  
![](images/94ee12de34e76d166fd639eaddff95a93ca30a7ca0efa77f5e568dc5c173ddf6.jpg)  
Source: Haver Analytics, CEIC, GS Global Investment Research

Exhibit 24: New Zealand growth and financial conditions  
![](images/0dc1d921e9b1014a8a0af3bb0c1538cee68265b6e2884ba4163e68d0bdc94e82.jpg)  
Source: Haver Analytics, CEIC, GS Global Investment Research

![](images/c53d6d6f77604ade88507331f3e2b688b21b80e63ed5c760074166d04893ef19.jpg)

## Disclosure Appendix

## Reg AC

I, Andrew Tilton, hereby certify that all of the views expressed in this report accurately reflect my personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Andrew Tilton GS (Asia) L.L.C., Andrew Boak, CFA GS Australia Pty Ltd, Goohoon Kwon, CFA GS (Asia) L.L.C., Hui Shan GS (Asia) L.L.C., Tomohiro Ota GS Japan Co., Ltd., Santanu Sengupta GS India SPL, Yuriko Tanaka GS Japan Co., Ltd., Lisheng Wang GS (Asia) L.L.C., Chris Poh GS (Singapore) Pte.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for information purposes only and is not, and under no circumstances should be construed as, an advertisement, offering or solicitation by GS & Co. LLC for purchasers of securities in Canada to trade in any Canadian security. GS & Co. LLC is not registered as a dealer in any jurisdiction in Canada under applicable Canadian securities laws and generally is not permitted to trade in Canadian securities and may be prohibited from selling certain securities and products in certain jurisdictions in Canada. If you wish to trade in any Canadian securities or other products in Canada please contact GS Canada Inc., an affiliate of The GS Group Inc., or another registered Canadian dealer. Hong Kong: Further information on the securities of covered companies referred to in this research may be obtained on request from GS (Asia) L.L.C. India: Further information o

[中间内容因长度限制已省略]

attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
