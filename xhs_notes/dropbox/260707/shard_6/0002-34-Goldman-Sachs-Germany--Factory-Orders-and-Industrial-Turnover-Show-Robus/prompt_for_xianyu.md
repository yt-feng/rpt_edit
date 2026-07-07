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
# Germany: Factory Orders and Industrial Turnover Show Robust Increase in May

BOTTOM LINE: Today's manufacturing data for May were solid. Manufacturing orders increased by $+1.9\%$ mom in May, above consensus expectations $(+1.1\%)$ , partially reversing the decline in April, and were down $-0.3\%$ on a less volatile 3m3m basis. Manufacturing orders excluding major orders increased slightly less strongly by $+1.0\%$ mom, but are up $+4.1\%$ on a 3m3m basis. Driven by stronger foreign turnover, industrial turnover increased by $+1.8\%$ mom in May, somewhat more modestly than the preliminary estimate of $+2.7\%$ suggested, and is up $+1.1\%$ on a 3m3m basis. As a result of the better than expected turnover data, we expect tomorrow's industrial production data to show a $+0.5\%$ mom increase in May on the back of robust manufacturing production.

Niklas Garnadt
+49(69)7532-1537 |
niklas.garnadt@gs.com
GS Bank Europe SE

Giovanni Pierdomenico
+44(20)7051-6807 |
giovanni.pierdomenico@gs.com
GS International

## KEY NUMBERS:

Manufacturing Orders (May): +1.9%, Consensus: +1.1%, Previous: -3.2%, revised up from -3.8% (all figures mom, non-annualised)

Manufacturing Turnover (May): +1.8%, Preliminary Estimate: +2.7%, Previous: +0.1%, unrevised from +0.1% (all figures mom, non-annualised)

## MAIN POINTS:

1. German manufacturing orders increased by +1.9%mom in May, an upside surprise to consensus expectations (+1.1%). Manufacturing orders excluding major orders likewise increased, although slightly less strongly, by +1.0%mom. On the less volatile 3m3m sequential basis, orders were down by -0.3%. Orders excluding major orders were up +4.1% on a 3m3m basis. Other transport equipment (which contains aircraft and major defence goods) boosted order intake (+85.0%mom), as did electrical equipment (+3.7%) and machinery and equipment (+3.7%), rebounding from a weaker April. Orders in vehicle manufacturing continued to decline (-3.8%).

2. Industrial turnover increased by +1.8%mom in May, less than the preliminary estimate of +2.7% suggested, reaching the highest level since February 2024. On a 3m3m sequential basis, turnover increased by +1.1%. Across sectors, basic metals (+7.1%), computers and electronics (+4.6%) and chemicals (+3.6%, reaching the highest level since 2022) contributed most positively, with the important motor vehicles manufacturing sector (+3.1%) also expanding robustly. Overall, 66% of sectors (weighted) saw an increase in turnover in May on a mom basis, and 66% on a 3m3m basis, indicating a relatively broad sales expansion.

3. Across markets, the Euro Area performed strongest, with orders and sales increasing strongly, rebounding from a weak April. Non-Euro Area orders were somewhat weaker but sales continued to increase. Domestic orders, which are most affected by volatile domestic defence orders, stabilised, but were weaker on a 3m3m basis due to base effects from a strong end to 2025. This confirms the trend since late last year, with Euro Area demand leading the way while domestic demand lags behind.

4. Taken together, today's orders data indicate a stabilisation of forward-looking indicators and strong spot activity in Q2. Real turnover currently stands $1.3\%$ above the Q1 average. Furthermore, turnover data in May were better than we expected (as we had marked down the exceptionally strong preliminary data), indicating robust manufacturing IP growth of $+1.2\%$ mom in May, with data to be released tomorrow. We expect industrial production growth at $+0.5\%$ in May, above consensus, as robust growth in manufacturing should be balanced by broadly flat energy and declining construction production.

5. We will update our GDP tracking estimate in our regular Euro area data update later this morning.

## Niklas Garnadt

Giovanni Pierdomenico

Exhibit 1: German Manufacturing Orders and Sales - Overview

<table><tr><td rowspan="2" colspan="2"></td><td colspan="3">Level (2021=100)</td><td colspan="3">MoM</td><td colspan="3">3m3m</td></tr><tr><td>2026-02</td><td>2026-03</td><td>2026-04</td><td>2026-02</td><td>2026-03</td><td>2026-04</td><td>2026-02</td><td>2026-03</td><td>2026-04</td></tr><tr><td rowspan="4">Orders</td><td>Total</td><td>92.6</td><td>89.6</td><td>91.3</td><td>4.5%</td><td>-3.2%</td><td>1.9%</td><td>-4.2%</td><td>-2.9%</td><td>-0.3%</td></tr><tr><td>Domestic</td><td>85</td><td>83</td><td>84.1</td><td>1.8%</td><td>-2.4%</td><td>1.3%</td><td>-10.6%</td><td>-11.5%</td><td>-7.8%</td></tr><tr><td>EA</td><td>106.2</td><td>95</td><td>105.6</td><td>10.6%</td><td>-10.5%</td><td>11.2%</td><td>-1.2%</td><td>2.8%</td><td>7.4%</td></tr><tr><td>Non-EA</td><td>92.9</td><td>93.8</td><td>90.8</td><td>3.2%</td><td>1.0%</td><td>-3.2%</td><td>1.7%</td><td>3.8%</td><td>3.4%</td></tr><tr><td rowspan="4">Orders ex major Orders</td><td>Total</td><td>90.4</td><td>87.4</td><td>88.3</td><td>4.5%</td><td>-3.3%</td><td>1.0%</td><td>1.4%</td><td>3.6%</td><td>4.1%</td></tr><tr><td>Domestic</td><td>86.5</td><td>82.8</td><td>82.4</td><td>4.2%</td><td>-4.3%</td><td>-0.5%</td><td>1.0%</td><td>2.1%</td><td>2.2%</td></tr><tr><td>EA</td><td>100.4</td><td>94.2</td><td>98.2</td><td>9.1%</td><td>-6.2%</td><td>4.2%</td><td>2.3%</td><td>6.0%</td><td>8.4%</td></tr><tr><td>Non-EA</td><td>88.7</td><td>88.5</td><td>89.1</td><td>1.6%</td><td>-0.2%</td><td>0.7%</td><td>1.2%</td><td>3.8%</td><td>3.5%</td></tr><tr><td rowspan="4">Turnover</td><td>Total</td><td>95.5</td><td>95.6</td><td>97.3</td><td>1.1%</td><td>0.1%</td><td>1.8%</td><td>0.7%</td><td>-0.1%</td><td>1.1%</td></tr><tr><td>Domestic</td><td>91.3</td><td>92</td><td>91.5</td><td>0.3%</td><td>0.8%</td><td>-0.5%</td><td>0.1%</td><td>-0.8%</td><td>-0.2%</td></tr><tr><td>EA</td><td>106</td><td>103.7</td><td>109.6</td><td>3.6%</td><td>-2.2%</td><td>5.7%</td><td>1.9%</td><td>2.2%</td><td>4.2%</td></tr><tr><td>Non-EA</td><td>95.6</td><td>96.4</td><td>98.7</td><td>0.2%</td><td>0.8%</td><td>2.4%</td><td>1.1%</td><td>-0.5%</td><td>1.0%</td></tr></table>

Source: Haver Analytics, GS Global Investment Research

Exhibit 2: German Manufacturing Orders by Destination  
![](images/1947166a3756bddc6d979d4633ee607529dffa9517970aa8462b33e789a70658.jpg)

![](images/8a28545a9dbffa5d1c0b32649cb7f8faa28d376478f156f7b2cf86a2106c3087.jpg)  
Monthly series in dashed, 3 month moving average in bold.  
Source: Haver Analytics, GS Global Investment Research

Exhibit 3: German Manufacturing Orders by Sub-Sector  
![](images/e3660f046b7718ecc427561082f30b99af345a14b1fd428372fef5d4de6260ed.jpg)  
Source: Haver Analytics, GS Global Investment Research

![](images/d45659494d237c3c4830710a510352002f1c55f3cd456f1913d14b71103e9689.jpg)

Exhibit 4: German Manufacturing Turnover (Sales)  
![](images/393c193425830f648bbf3166a8e530cddb43a7becc0e403923481e79c568ff38.jpg)

![](images/1a643c8975869aed688b3134ee78742c02667fda527f579774336ae759bee205.jpg)

Monthly series in dashed, 3 month moving average in bold.

Source: Haver Analytics, GS Global Investment Research  
Exhibit 5: Orders and Sales Diffusion Indices  
![](images/775e8ade797608f33f179bbbba148acb19abf3177050adf133fcb55a464500b3.jpg)  
Monthly series in dashed, 3 month moving average in bold  
Source: Haver Analytics, GS Global Investment Research

![](images/e8ce741610138c7453d2e1785598ee046f411d79f010a50711b2dff549d8b686.jpg)

Exhibit 6: We Expect Robust Manufacturing IP Growth After Today's Strong Manufacturing Sales  
![](images/06d1c2095c892272302c43bb07eeabb6fb2144aca3f319cd6ddd498ef4bc8eb2.jpg)  
Source: Destatis, Haver Analytics, GS Global Investment Research

Exhibit 7: Sectoral Spotlight on Defence  
![](images/4a1d54fd6b4b42ad59e91e9da998f1a938bad50c698e5e3858bc57de7763e146.jpg)

![](images/8f0ddf80c02bab4ca140d01736c493b9fab4f2d8f1c86c47a8264855ee0a6199.jpg)  
Monthly series in dashed, 6-month moving average in bold. We proxy defence using a weighted average of the other transport equipment and weapons & ammunition sectors.  
Source: Haver Analytics, GS Global Investment Research

## The European Economics Team

## Sven Jari Stehn

+44(20)7774-8061
jari.stehn@gs.com
GS International

## James Moberly

+44(20)7774-9444

james.r.moberly@gs.com

GS International

## Giovanni Pierdomenico

+44(20)7051-6807

giovanni.pierdomenico@gs.com

GS International

## Filippo Taddei

+44(20)7774-5458
filippo.taddei@gs.com
GS International

## Niklas Garnadt

+49(69)7532-1537
niklas.garnadt@gs.com
GS Bank Europe SE

## Alexandre Stott

+33(1)4212-1108
alexandre.stott@gs.com
GS Bank Europe SE - Paris Branch

## Katya Vashkinskaya

+44(20)7774-4833

katya.vashkinskaya@gs.com

GS International

## Disclosure Appendix

## Reg AC

We, Niklas Garnadt and Giovanni Pierdomenico, hereby certify that all of the views expressed in this report accurately reflect our personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Niklas Garnadt GS Bank Europe SE, Giovanni Pierdomenico GS International.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for information purposes only and is not, and under no circumstances should be construed as, an advertisement, offering or solicitation by GS & Co. LLC for purchasers of securities in Canada to trade in any Canadian security. GS & Co. LLC is not registered as a dealer in any jurisdiction in Canada under applicable Canadian securities laws and generally is not permitted to trade in Canadian securities and may be prohibited from selling certain securities and products in certain jurisdictions in Canada. If you wish to trade in any Canadian securities or other products in Canada please contact GS Canada Inc., an affiliate of The GS Group Inc., or another registered Canadian dealer. Hong Kong: Further information on the securities of covered companies referred to in this research may be obtained on request from GS (Asia) L.L.C. India: Further information on the subject company or companies referred to in this research may be obtained from GS (India) Securities Private Limited, Research Analyst - SEBI Registration Number INH000001493, 10th Floor, Ascent-Worli, Sudam Kalu Ahire Marg, Worli, Mumbai-400 025, India, Corporate Identity Number U74140MH2006FTC160634, Phone +91 22 6616 9000, Fax +91 22 6616 9001. GS may beneficially own 1% or more of the securities (as such term is defined in clause 2 (h) the Indian Securities Contracts (Regulation) Act, 1956) of the subject company or companies referred to in this research report. Registration granted by SEBI and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. GS (India) Securities Private Limited compliance officer and investor grievance contact details, a copy of the annual compliance audit report and other relevant information and disclosures can be found at this link:

https://www.goldmansachs.com/worldwide/india/research-analyst. Japan: See below. Korea: This research, and any access to it, is intended only for “professional investors” within the meaning of the Financial Services and Capital Markets Act, unless otherwise agreed by GS. Further information on the subject company or companies referred to in this research may be obtained from GS (Asia) L.L.C., Seoul Branch. New Zealand: GS New Zealand Limited and its affiliates are neither “registered banks” nor “deposit takers” (as defined in the Reserve Bank of New Zealand Act 1989) in New Zealand. This research, and any access to it, is intended for “wholesale clients” (as defined in the Financial Advisers Act 2008) unless otherwise agreed by GS. A copy of certain GS Australia and New Zealand disclosure of interests is available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Russia: Research reports distributed in the

[中间内容因长度限制已省略]

ttempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints.

As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
