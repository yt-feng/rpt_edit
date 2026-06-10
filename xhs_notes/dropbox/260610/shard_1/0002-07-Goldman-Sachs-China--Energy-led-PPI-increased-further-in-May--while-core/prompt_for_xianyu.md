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
# China: Energy-led PPI increased further in May, while core CPI softened

## Bottom line:

China's headline CPI inflation was flat at $+1.2\%$ yoy in May, as higher energy prices were broadly offset by lower food prices. Core CPI inflation edged down to $+1.1\%$ yoy, likely due to softer tourism-related services prices. Headline PPI inflation increased further to $+3.9\%$ yoy in May from $+2.8\%$ yoy in April, mainly due to higher chemical, energy, and coal prices. Overall, upstream sectors accounted for around $82\%$ of the rebound in year-over-year headline PPI inflation.

## Key numbers:

CPI: +1.2% yoy (+1.0% mom annualized\*) in May vs. GS: +1.4% yoy, Bloomberg consensus: +1.3% yoy; April: +1.2% yoy (+2.4% mom annualized\*).

Food: -1.7% yoy in May (-0.9% mom annualized\*) vs. -1.6% yoy in April.  
Non-food: +1.9% yoy in May (+1.8% mom annualized\*) vs. +1.8% yoy in April.  
Core: +1.1% yoy in May (-0.1% mom annualized\*) vs. +1.2% yoy in April.

PPI: +3.9% yoy in May (+9.7% mom annualized\*) vs. GS: +4.0% yoy, Bloomberg consensus: +3.9% yoy; April: +2.8% yoy (+22.4% mom annualized\*).

(\*seasonally adjusted by GS)

## Main points:

1. China's headline CPI was flat at $+1.2\%$ yoy in May, as higher energy prices were broadly offset by lower food prices (Exhibit 1). In month-on-month terms, headline CPI slowed to $+1.0\%$ (annualized, seasonally adjusted) in May (vs. $+2.4\%$ mom s.a. ann in April).

2. In year-over-year terms, food inflation edged down to $-1.7\%$ yoy in May from $-1.6\%$ yoy in April (Exhibit 2). Among major food items, pork prices fell by $16.1\%$ yoy in May (vs. $-15.2\%$ yoy in April). Fresh vegetable prices rose by $1.6\%$ yoy in May (vs. $-0.5\%$ yoy in April), and fresh fruit prices fell by $2.2\%$ yoy in May (vs. $-1.0\%$ yoy in April).

3. Non-food CPI inflation edged up to $+1.9\%$ yoy in May from $+1.8\%$ yoy in April, mainly on higher energy prices (Exhibit 3). Specifically, fuel costs rose by $+21.1\%$ yoy in May (vs. $+17.4\%$ yoy in April), accounting for all of the increase in non-food CPI inflation from April to May. After excluding food and energy prices, core CPI inflation edged down to $+1.1\%$ yoy in May (vs. $+1.2\%$ yoy in April), likely reflecting softer tourism-related services prices, with transportation services inflation easing to $4.7\%$

Xinquan Chen

+852-2978-2418

xinquan.chen@gs.com

GS (Asia) L.L.C.

yoy in May (vs. +5.1% yoy in April).

4. Year-over-year PPI inflation rose to $+3.9\%$ yoy in May from $+2.8\%$ yoy in April, largely reflecting higher chemical, oil & gas, and coal prices (Exhibit 4). Overall, upstream sectors accounted for around $82\%$ of the rebound in headline PPI inflation, with chemicals, oil & gas, and coal contributing 0.3pp, 0.2pp, and 0.2pp, respectively, to the 1.1pp increase in headline PPI inflation. In month-over-month terms, PPI inflation fell to $9.7\%$ (annualized, seasonally adjusted) in May (vs. $22.4\%$ in April). PPI inflation in producer goods rose to $+5.2\%$ yoy in May from $+3.8\%$ yoy in April, and PPI inflation in consumer goods edged up to $-0.8\%$ yoy in May (vs. $-1.0\%$ yoy in April).

## Xinquan Chen

Exhibit 1: Year-over-year PPI inflation increased further from April to May  
![](images/4f057dedc324e75aa99a5975642e80a081414f78224a3bef7cad8d19b7d7cb77.jpg)

<details>
<summary>line chart</summary>

| Year | CPI   | PPI   |
|------|-------|-------|
| 07   | 3.0   | 2.5   |
| 08   | 8.0   | 10.0  |
| 09   | -2.0  | -8.0  |
| 10   | 4.0   | 6.0   |
| 11   | 6.0   | 8.0   |
| 12   | 4.0   | 6.0   |
| 13   | 3.0   | 4.0   |
| 14   | 2.0   | 2.0   |
| 15   | 1.0   | -2.0  |
| 16   | 2.0   | -6.0  |
| 17   | 3.0   | 8.0   |
| 18   | 2.0   | 4.0   |
| 19   | 3.0   | 2.0   |
| 20   | 5.0   | -4.0  |
| 21   | -1.0  | 12.0  |
| 22   | 3.0   | -6.0  |
| 23   | 1.0   | -4.0  |
| 24   | 0.0   | -2.0  |
| 25   | -1.0  | -4.0  |
| 26   | 1.0   | 4.0   |
</details>

Source: NBS

Exhibit 2: Food CPI inflation fell in May on a broad-based decline in food prices  
![](images/28a733db4f85f9687b8eab18ae465a61db3150206efcb6c78aaf8a8f6899c324.jpg)

<details>
<summary>bar chart</summary>

Contribution to year-over-year food inflation
| Year | Pork (%) | Fresh vegetables (%) | Fresh fruits (%) | Eggs (%) | Others (%) |
|---|---|---|---|---|---|
| 19 | -0.5 | 0.2 | 0.8 | 0.3 | 2.1 |
| 20 | 14.2 | -0.8 | -1.5 | 12.3 | 18.7 |
| 21 | -2.1 | 0.5 | 0.3 | -1.2 | 1.8 |
| 22 | -6.8 | -1.2 | 0.7 | -0.5 | 3.5 |
| 23 | -1.5 | 0.1 | 0.9 | -0.2 | 5.2 |
| 24 | -3.2 | -0.3 | -0.1 | -0.8 | -6.1 |
| 25 | 0.8 | 0.5 | 0.4 | 0.2 | 0.9 |
| 26 | -0.7 | -0.4 | -0.6 | -0.3 | 1.2 |
</details>

Source: NBS, GS Global Investment Research

Exhibit 3: Non-food CPI inflation edged up on higher energy prices  
![](images/911cd38abe2e4797aec40147c37d93d56d693d5beea8e9045ff954cce394d91b.jpg)

<details>
<summary>line chart</summary>

| Year | Energy | Tourism-related | Durable goods | Shelter | Administered items | Others | Nonfood |
|------|--------|-----------------|---------------|---------|--------------------|--------|---------|
| 16   | -0.5   | 0.5             | 0.0           | 0.0     | 0.0                | 0.0    | 1.0     |
| 17   | 0.0    | 1.0             | 0.5           | 0.5     | 0.5                | 0.5    | 2.5     |
| 18   | 0.5    | 1.5             | 1.0           | 1.0     | 1.0                | 1.0    | 2.5     |
| 19   | 1.0    | 2.0             | 1.5           | 1.5     | 1.5                | 1.5    | 2.0     |
| 20   | -0.5   | 0.5             | 0.0           | 0.0     | 0.0                | 0.0    | 1.5     |
| 21   | -1.0   | -1.0            | -0.5          | -0.5    | -0.5               | -0.5   | -1.0    |
| 22   | 0.5    | 1.5             | 1.0           | 1.0     | 1.0                | 1.0    | 2.5     |
| 23   | -0.5   | 0.5             | 0.0           | 0.0     | 0.0                | 0.0    | 1.5     |
| 24   | 0.0    | 1.0             | 0.5           | 0.5     | 0.5                | 0.5    | 2.0     |
| 25   | -0.5   | 0.5             | 0.0           | 0.0     | 0.0                | 0.0    | 1.5     |
| 26   | 0.5    | 1.5             | 1.0           | 1.0     | 1.0                | 1.0    | 2.5     |
</details>

Source: CEIC, GS Global Investment Research

Exhibit 4: PPI inflation increased further from April to May, mainly due to higher energy and related chemical prices  
![](images/d84351128c8e0a529c6c6fde8dcbc4df76e092b21d74a2e6c62802306457e636.jpg)

<details>
<summary>bar-line hybrid</summary>

Contribution to year-over-year PPI inflation
| Year | Ferrous metals mining/smelting (%) | Petrol mining/processing (%) | Raw chemicals/chemical fiber (%) | Downstream (%) | Nonferrous metals mining/smelting (%) | Coal mining (%) | Nonmetal mining/mfg (%) | Headline (%) |
|---|---|---|---|---|---|---|---|---|
| 19 | 0.5 | 0.2 | -0.3 | 0.1 | 0.4 | 0.6 | 0.7 | 0.3 |
| 20 | -0.8 | -1.2 | -0.5 | -0.6 | -0.3 | -0.1 | -0.2 | -1.5 |
| 21 | 1.2 | 0.8 | 0.5 | 0.3 | 1.5 | 1.8 | 1.6 | 1.2 |
| 22 | 2.5 | 2.0 | 1.8 | 1.5 | 3.0 | 2.5 | 2.2 | 3.5 |
| 23 | -0.5 | -0.8 | -0.3 | -0.4 | -0.2 | -0.6 | -0.7 | -1.8 |
| 24 | -0.3 | -0.5 | -0.2 | -0.3 | -0.1 | -0.4 | -0.5 | -1.2 |
| 25 | -0.1 | -0.3 | -0.1 | -0.2 | 0.1 | -0.2 | -0.3 | -0.8 |
| 26 | 0.8 | 1.2 | 0.9 | 0.7 | 1.5 | 1.8 | 1.6 | 3.5 |
Percentage point: Fertures metals mining/smelting; Petrol mining/processing; Raw chemicals/chemical fiber; Downstream; Nonferrous metals mining/smelting; Coal mining; Nonmetal mining/mfg; Headline.
</details>

Source: NBS, GS Global Investment Research

## The China Economics Team

## Andrew Tilton

+852-2978-1802

andrew.tilton@gs.com

GS (Asia) L.L.C.

## Hui Shan

+852-2978-6634

hui.shan@gs.com

GS (Asia) L.L.C.

## Lisheng Wang

+852-3966-4004

lisheng.wang@gs.com

GS (Asia) L.L.C.

## Xinquan Chen

+852-2978-2418

xinquan.chen@gs.com

GS (Asia) L.L.C.

## Yuting Yang

+852-2978-7283

yuting.y.yang@gs.com

GS (Asia) L.L.C.

## Chelsea Song

+852-2978-0106

chelsea.song@gs.com

GS (Asia) L.L.C.

## Disclosure Appendix

## Reg AC

I, Xinquan Chen, hereby certify that all of the views expressed in this report accurately reflect my personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Xinquan Chen GS (Asia) L.L.C..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; $1\%$ or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for information purposes only and is not, and under no circumstances should be construed as, an advertisement, offering or solicitation by GS & Co. LLC for purchasers of securities in Canada to trade in any Canadian security. GS & Co. LLC is not registered as a dealer in any jurisdiction in Canada under applicable Canadian securities laws and generally is not permitted to trade in Canadian securities and may be prohibited from selling certain securities and products in certain jurisdictions in Canada. If you wish to trade in any Canadian securities or other products in Canada please contact GS Canada Inc., an affiliate of The GS Group Inc., or another registered Canadian dealer. Hong Kong: Further information on the securities of covered companies referred to in this research may be obtained on request from GS (Asia) L.L.C. India: Further information on the subject company or companies referred to in this research may be obtained from GS (India) Securities Private Limited, Research Analyst - SEBI Registration Number INH000001493, 10th Floor, Ascent-Worli, Sudam Kalu Ahire Marg, Worli, Mumbai-400 025, India, Corporate Identity Number U74140MH2006FTC160634, Phone +91 22 6616 9000, Fax +91 22 6616 9001. GS may beneficially own 1% or more of the securities (as such term is defined in clause 2 (h) the Indian Securities Contracts (Regulation) Act, 1956) of the subject company or companies referred to in this research report. Investment in securities market are subject to market risks. Read all the related documents carefully before investing. Registration granted by SEBI and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. GS (India) Securities Private Limited compliance officer and investor grievance contact details can be found at: https://www.goldmansachs.com/worldwide/india/documents/Grievance-Redressal-and-Escalation-Matrix.pdf, and a copy of the annual audit compliance report can be found at this link: https://publishing.gs.com/content/site/india-annual-compliance-report.html. Japan: See below. Korea: This research, and any access to it, is intended only for “professional investors” within the meaning of the Financial Services and Capital Markets Act, unless otherwise agreed by GS. Further information on the subject company or companies referred to in this research may be obtained from GS (Asia) L.L.C., Seoul Branch. New Zealand: GS New Zealand Limited and its affiliates are neither “registered banks” nor “deposit takers” (as defined in the Reserve Bank of New Zealand Act 1989) in New Zealand. This research, and any access to it, is intended for “wholesale clients” (as defined in the Financial Advisers Act 2008) unless otherwise agreed by GS. A copy of certain GS Australia and New Zealand disclosure of interests is available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Russia: Research reports distributed in the Russian Federation are not advertising as defined in the Russian legislation, but are information and analysis not having product promotion as their main purpose and do not provide appraisal within the meaning of the Russian legislation on appraisal activity. Research reports do not constitute a personalized investment recommendation as defined in Russian laws and regulations, are not addressed to a specific client, and are prepared without analyzing the financial 

[中间内容因长度限制已省略]

ttempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g.,

marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
