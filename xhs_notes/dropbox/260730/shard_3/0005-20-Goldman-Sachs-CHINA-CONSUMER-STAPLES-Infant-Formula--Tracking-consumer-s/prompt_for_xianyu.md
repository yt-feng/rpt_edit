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
CHINA CONSUMER STAPLES

# Infant Formula: Tracking consumer sentiment #2; Cabio updates post Nestle IMF recall incident; Friso issue of elevated Lead levels

## What's new:

Cabio’s Profit warning: Following the ARA issue in Jan 26, Cabio (Not Covered) stated that due to the severe impact of overseas market public opinion and new regulatory requirements, its production and sales activities have been heavily disrupted. Cabio estimates that normal operations cannot be restored within the next 3 months, triggering the Shanghai Stock Exchange’s ST risk warning criteria for operational abnormality (trading of the company’s shares was suspended on July 27, 2026, and resumed on July 28, 2026, under the new stock abbreviation “ST Cabio”). Alongside the risk warning, Cabio released its preliminary financial forecast for 1H26, showing a decline to a net loss in 1H26 at -c.Rmb101mn. To address this, Cabio’s board outlined four primary initiatives while making an effort to establish a comprehensive, full-chain product risk monitoring system to ensure strict compliance with the latest global regulatory standards.

☐ Re-engaging Customers: Prioritizing communication with core clients to restore its non-infant formula “big health” (dietary supplements) business.

☐ Diversification: Accelerating non-ARA segments. In H1 2026, the company secured new large-scale orders for its algal DHA oil in the animal nutrition sector and deepened partnerships with international cosmetics brands.

Christina Liu
+852-2978-6983 | christina.liu@gs.com
GS (Asia) L.L.C.

Valerie Zhou
+852-2978-0820 | valerie.zhou@gs.com
GS (Asia) L.L.C.

\- Evolving situation on Friso: On Jul 25, the Macau government issued a food safety alert after an inspection which found that one batch of Hong Kong version of FrisoLac Stage 1 IMF product (800g, batch 1W07KPJ) exceeded regulatory Lead limit of $0.02\mathrm{mg/kg}$ . Macau authorities immediately ordered a recall on affected batch and Hong Kong Centre for Food safety also advised consumers not to use the product. On 26 Jul, China's General Administration of Customs stated that affected batch has not entered mainland China through general trade channels, although consumers who purchased via cross-boarder e-commerce or

Synthetic Biology Commercialization: Speeding up the industrialization of Human Milk Oligosaccharides (HMOs). Notably, its lacto-N-neotetraose (LNnT) product recently received regulatory approval from China's National Health Commission.

Leaf Liu  
+852-3966-4169 | leaf.liu@gs.com  
GS (Asia) L.L.C.

parallel imports were advised to check the batch number. In response, FrieslandCampina announced that an independent 3rd party lab retested the same batch and found a level of $<0.007\mathrm{mg/kg}$ , well below Macau gov's regulatory limit and the company also stated that all batches of Friso products officially imported into mainland China have undergone full pre-market quality testing with lead consistently reported as non-detected ( $<0.01\mathrm{mg/kg}$ ), well below China's limit of $0.08\mathrm{mg/kg}$ .

☐ Friesland has been gaining market share in offline IMF market based on Nielsen data in Jan-April 2026, and improved ranking on Douyin in recent 618 shopping festival.

Ausnutria (not covered) announced 1H26 profit warning on 24 July, guiding for Rmb3.07bn-3.17bn revenue (mid point at Rmb3.12bn, down c.20% yoy) and -Rmb685-785 net loss (vs. Rmb181mn net profit in 1H25) due to a combination of phased adjustments and external environmental factors. Excluding a one-time inventory-related adjustment, non-cash asset impairments and other related impacts, Ausnutria expects to record a core net operating profit at Rmb155mn-255mn for 1H26 (mid point at c. Rmb205mn, largely steady yoy). Ausnutria drove a 40% reduction in total supply chain inventory and the compression of channel inventory to under 30 days in 1H26, while the company is also actively streamlining SKUs and optimizing product structures.

☐ Specialized segments: While standard cow-milk IMF faces intense price competition, specialized segments like goat milk formula (e.g., Kabrita from Hyproca) continue to show robust international growth (particularly in North America and the Middle East).

☐ Beyond Infant Formula: it is also out “dual-engine” capabilities in professional nutrition and probiotics.

Tracking consumer sentiment: We tracked the Baidu index to gauge consumer sentiment trends on IMF related incidents.

For Friso IMF on elevated Lead levels, Baidu index indicated that a temporary peak of search has already reached on Jul 27th with absolute level much lower than that of Nestle IMF recall (For Nestlé IMF recall on ARA issue with Cabio, Baidu index indicated that this incident cooled down c.20 days post the media reports). Key things to focus on going forward will be further announcements of testing results or related updates from FrieslandCampina /Macau authorities/Mainland China authorities regarding the situation.

GS view: We believe these reinforce a more cautious near-term sentiment towards the IMF sector (online IMF market sales declined by -17% in 2Q26 and -11% in 1Q26; offline down 8% in Jan-April 2026), while the industry continues to face some headwinds beyond underlying soft demand, incl. supply chain risks/regulatory scrutiny/product quality concerns and ongoing channel adjustments. While these events are largely company/brand specific rather than a systematic disruption in product safety, they are likely to weigh on consumer sentiment and investor confidence in the near-term. We continue to expect leading brands with strong quality control and brand power to gain shares and to be better positioned during the current cycle. Bellamy and Biostime

remain the key market share gainers, up $70\% / 43\%$ yoy in IMF online sales in Jun 2026.

The authors would like to thank Lily Qi for her contribution to this report.

Exhibit 1: MNC players saw sequential market share trend mixed in Mar-Apr, Friesland/Danone/A2 value share increased while Wyeth decreased vs. Jan-Feb Offline international IMF brands market share by value

![](images/e64eb33af8e8eb4c4ba86400bc76a79d5127d568e293a00b1a9e9eb19f13b17f.jpg)  
Source: Nielsen

Exhibit 2: IMF 618 Shopping festival - Douyin sales ranking by category

<table><tr><td colspan="4">IMF</td></tr><tr><td>1</td><td>1</td><td>Aptamil</td><td>Danone</td></tr><tr><td>2</td><td>2</td><td>Mengniu</td><td>Mengniu</td></tr><tr><td>4</td><td>3</td><td>Pro-kido</td><td>Yili</td></tr><tr><td>10</td><td>4</td><td>AusNuotore</td><td>MLove</td></tr><tr><td>7</td><td>5</td><td>Biostime</td><td>H&amp;H Group</td></tr><tr><td>8</td><td>6</td><td>Friso</td><td>FrieslandCampina</td></tr><tr><td>6</td><td>7</td><td>Junlebao</td><td>Junlebao</td></tr><tr><td>5</td><td>8</td><td>A2</td><td>A2 Milk</td></tr><tr><td>3</td><td>9</td><td>Firmus</td><td>China Feihe</td></tr><tr><td>&gt;10</td><td>10</td><td>Adopt ACow</td><td>Adopt ACow</td></tr></table>

Source: Chanmama, GS Global Investment Research

## Tracking Consumer Sentiment

We tracked the Baidu index to gauge consumer sentiment trends on IMF related incidents.

For Nestlé IMF recall on ARA issue with Cabio, Baidu index indicated that this incident already cooled down c.20 days post the media reports.

For Friso IMF on elevated Lead levels, Baidu index indicated that a temporary peak of search has already reached on Jul 27th with absolute level much lower than that of Nestle IMF recall. Key things to focus on going forward will be further announcements of testing results or related updates from FrieslandCampina /Macau authorities/Mainland China authorities regarding the situation.

Exhibit 3: Baidu search index of Friso IMF on elevated Lead levels has reached a temporary peak while still much lower than that of Nestle IMF recall back in Jan 2026  
![](images/52ba2c092227433936e57077cbf4d2a9ccf7ac0e5881558777f849747ecb6e74.jpg)  
Source: Baidu Index

Exhibit 4: Baidu search index shows that the Nestle IMF recall on ARA issues already cooled down  
![](images/ac1968d3790851a5ba9595ed19fcc39f94c6cd272e63b49286442d7e784a4e5c.jpg)  
Source: Baidu index

## Disclosure Appendix

## Reg AC

We, Leaf Liu, Christina Liu and Valerie Zhou, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Leaf Liu GS (Asia) L.L.C., Christina Liu GS (Asia) L.L.C., Valerie Zhou GS (Asia) L.L.C..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses inputs for the fiscal year at least seven quarters in the future compared with the year at least three quarters in the future (on a per-share basis for all metrics).

For a more detailed description of how we calculate the GS Factor Profile, please contact your GS representative.

## M&A Rank

Across our global coverage, we examine stocks using an M&A framework, considering both qualitative factors and quantitative factors (which may vary across sectors and regions) to incorporate the potential that certain companies could be acquired. We then assign a M&A rank as a means of scoring companies under our rated coverage from 1 to 3, with 1 representing high (30%-50%) probability of the company becoming an acquisition target, 2 representing medium (15%-30%) probability and 3 representing low (0%-15%) probability. For companies ranked 1 or 2, in line with our standard departmental guidelines we incorporate an M&A component into our target price. M&A rank of 3 is considered immaterial and therefore does not factor into our price target, and may or may not be discussed in research.

## Quantum

Quantum is GS' proprietary database providing access to detailed financial statement histories, forecasts and ratios. It can be used for in-depth analysis of a single company, or to make comparisons between companies in different sectors and markets.

## Disclosures

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See 'Ratings, Coverage universe and related definitions' below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

Additional disclosures required under the laws and regulations of jurisdictions other than the United States
The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only a

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
