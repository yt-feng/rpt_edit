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
# Americas Healthcare: Pharmaceuticals: Illustrative Impact Analysis and Company Commentary on CMS Proposed Rule

We have been receiving inbounds regarding the CMS proposed rule on the Medicare Drug Price Negotiation Program, which would, in addition to formally codifying policies previously implemented under the IRA, look to consider formulations with two or more active moieties/ingredients or vaccine antigen components as one for purposes of negotiation eligibility. Combinations with hyaluronidase are specifically called out, suggesting potential implications for MRK's Keytruda Qlex, BMY's Opdivo Qvantig, and JNJ's Darzalex Faspro — contributing to slight underperformance (MRK -2.8%, JNJ -2.2%, BMY -1.6% vs DRG -1.3%, XLV -0.6%). We note this issue was raised last year, as the CMS draft guidance for the IPAY 2028 class included a paragraph around fixed combinations — however this clause was removed in the final guidance. Within, we refresh our illustrative impact analysis for including these SC drugs in the 2029 IRA price negotiations, which implies a theoretical minimal low-single digit EBIT impact for these companies in 2029/2030.

Company responses to the proposal are largely consistent with prior commentary. JNJ notes that their position on Darzalex has not changed — consistent with what the company has shared previously, they do not expect IRA price setting for Darzalex Faspro before 2034. BMY noted the development is not unexpected, and that the company disagrees and is mobilized and will make their thoughts known during the comment period. MRK, while concerned about the precedent the rule sets, and will continue to engage with CMS through the comment period, notes that regardless of whether Keytruda Qlex is included in IRA negotiations, the company does not expect a material financial impact, and have always stated their pricing strategy for Keytruda Qlex will take into account the likelihood that IV Keytruda will be subject to IRA price setting beginning in 2029, and the likely entry of biosimilars in December 2028. Based on the latest draft guidance issued by the CMS, MRK anticipates Keytruda IV and Keytruda Qlex will be subject to IRA price negotiation with an effective date of January 2029. (Given the earliest anticipated biosimilar competition for KEYTRUDA is December 2028, when the compound patent expires, at this time, MRK does not anticipate that biosimilar competition will preclude KEYTRUDA from being subject to IRA negotiation.) With regard to MRK, given their Keytruda Qlex pricing strategy is messaged by the company to be consistent irrespective of price negotiation, we see the possibility that inclusion could theoretically create a tailwind from an access/ coverage perspective.

On next steps, there is a 60-day comment period (through August 17), after which during Fall 2026 CMS plans to issue the final rule for initial price applicability years

Asad Haider, CFA

+1(212)902-0691 | asad.haider@gs.com

GS & Co. LLC

Nick Jennings

+1(415)249-7412

nick.jennings@gs.com

GS & Co. LLC

Jeff Su

+1(212)357-9930 | jeff.su@gs.com

GS & Co. LLC

(IPAY) 2029 and beyond, and February 1, 2027 is the deadline for CMS to publish the list of up to 20 drugs payable under Part B and/or covered under Part D for negotiation.

## Illustrative Impact Analysis

To contextualize and quantify the potential impact of subcutaneous formulation inclusion for IPAY 2029, we update our prior illustrative analysis. Limitations of this analysis include (1) assumption that price impact only applies to the US Medicare and there is no follow through to commercial or other segments; (2) our estimated net price discount of 36% is based on the approximate average discount from the IPAY 2027 class and could be higher, and (3) the latest CMS drug spending data is from 2023, on which we base our estimate of percent Medicare exposure, and this number could be a different percentage today or at the time of impact.

Based on the latest available 2023 CMS drug spending data, Medicare represented \~45% of JNJ's Darzalex sales (Darzalex + Darzalex Faspro) and \~37% for BMY's Opdivo and MRK's Keytruda. (Note, these exposure figures may have changed.)

Exhibit 1: Estimated Medicare Exposure Based On CMS 2023 Medicare Part B and Part D Spending  
\$ in mn

<table><tr><td rowspan="2">Company</td><td rowspan="2">Drug</td><td colspan="3">2023 Sales/Medicare Spending ($ mn)</td><td rowspan="2">Medicare Exposure</td></tr><tr><td>US Sales</td><td>Medicare Part D Spending</td><td>Medicare Part B Spending</td></tr><tr><td>JNJ</td><td>Darzalex + Darzalex Faspro</td><td>$5,277</td><td>$86</td><td>$2,298</td><td>45.2%</td></tr><tr><td>MRK</td><td>Keytruda</td><td>$15,114</td><td>$117</td><td>$5,434</td><td>36.7%</td></tr><tr><td>BMY</td><td>Opdivo</td><td>$5,283</td><td>$51</td><td>$1,910</td><td>37.1%</td></tr></table>

Source: Company data, CMS, GS Global Investment Research

## JNJ's Darzalex Faspro:

We apply the 36% net price discount to the estimated US portion of Darzalex Faspro sales exposed to Medicare (\~45%, per above). With these assumptions we calculate \~\$1.9bn sales impact per year in the 2029-2030 time frame, which represents \~9% of our estimated total Darzalex sales, \~1.4% of total JNJ sales, and \~4% of JNJ total adjusted EBIT.

Exhibit 2: JNJ's Darzalex: Illustrative Incremental Impact of Potential Darzalex Faspro Inclusion in IRA  
\$ in mn

<table><tr><td>JNJ&#x27;s Darzalex - GS estimates</td><td>2029</td><td>2030</td></tr><tr><td colspan="3">Before Darzalex Faspro inclusion in IRA:</td></tr><tr><td>US Sales:</td><td>$12,031</td><td>$12,151</td></tr><tr><td>of which Darzalex Faspro (SC):</td><td>$11,429</td><td>$11,544</td></tr><tr><td>of which Medicare</td><td>$5,162</td><td>$5,214</td></tr><tr><td>of which non-Medicare</td><td>$6,267</td><td>$6,330</td></tr><tr><td>of which Darzalex (IV)</td><td>$602</td><td>$608</td></tr><tr><td>OUS Sales:</td><td>$8,420</td><td>$8,504</td></tr><tr><td>Total Darzalex Sales (IV+SC)</td><td>$20,451</td><td>$20,656</td></tr></table>

Illustrative Darzalex Faspro inclusion in IRA:

<table><tr><td>US Sales:</td><td>$10,173</td><td>$10,274</td></tr><tr><td>of which Darzalex Faspro (SC):</td><td>$9,571</td><td>$9,667</td></tr><tr><td>of which Medicare</td><td>$3,304</td><td>$3,337</td></tr><tr><td>of which non-Medicare</td><td>$6,267</td><td>$6,330</td></tr><tr><td>of which Darzalex (IV)</td><td>$602</td><td>$608</td></tr><tr><td>OUS Sales:</td><td>$8,420</td><td>$8,504</td></tr><tr><td>Total Darzalex Sales (IV+SC)</td><td>$18,593</td><td>$18,779</td></tr></table>

<table><tr><td colspan="3">Total Darzalex Sales Impact:</td></tr><tr><td>$ Impact</td><td>-$1,858</td><td>-$1,877</td></tr><tr><td>% Impact</td><td>-9.1%</td><td>-9.1%</td></tr></table>

<table><tr><td>Whole Co. Sales (GS)</td><td>$130,161</td><td>$139,326</td></tr><tr><td>$ Impact % of Whole Co.</td><td>-1.4%</td><td>-1.3%</td></tr></table>

<table><tr><td>Whole Co. Adj. EBIT (GS)</td><td>$46,207</td><td>$49,461</td></tr><tr><td>$ Impact % of Whole Co.</td><td>-4.0%</td><td>-3.8%</td></tr></table>

Source: GS Global Investment Research

## MRK's Keytruda Qlex:

We apply the 36% net price discount to the estimated US portion of Keytruda Qlex sales exposed to Medicare (\~37%, per above). With these assumptions we calculate \~\$900mn sales impact per year in the 2029-2030 time frame, which represents \~3% of our estimated total Keytruda sales, 1.3% of total MRK sales, and 3.0% of MRK total adjusted EBIT.

Exhibit 3: MRK's Keytruda: Illustrative Incremental Impact of Potential SC pembrolizumab Inclusion in IRA  
\$ in mn

<table><tr><td>MRK&#x27;s Keytruda - GS estimates</td><td>2029</td><td>2030</td></tr><tr><td colspan="3">Before SC Keytruda inclusion in IRA:</td></tr><tr><td>US Sales:</td><td>$15,079</td><td>$10,612</td></tr><tr><td>of which SC Keytruda:</td><td>$6,925</td><td>$6,424</td></tr><tr><td>of which Medicare</td><td>$2,543</td><td>$2,359</td></tr><tr><td>of which non-Medicare</td><td>$4,382</td><td>$4,065</td></tr><tr><td>of which Keytruda (IV)</td><td>$8,154</td><td>$4,188</td></tr><tr><td>OUS Sales:</td><td>$14,372</td><td>$14,151</td></tr><tr><td>Total Keytruda Sales (IV + SC)</td><td>$29,451</td><td>$24,763</td></tr></table>

Illustrative SC Keytruda inclusion in IRA:

<table><tr><td>US Sales:</td><td>$14,164</td><td>$9,763</td></tr><tr><td>of which SC Keytruda:</td><td>$6,010</td><td>$5,575</td></tr><tr><td>of which Medicare</td><td>$1,628</td><td>$1,510</td></tr><tr><td>of which non-Medicare</td><td>$4,382</td><td>$4,065</td></tr><tr><td>of which Keytruda (IV)</td><td>$8,154</td><td>$4,188</td></tr><tr><td>OUS Sales:</td><td>$14,372</td><td>$14,151</td></tr><tr><td>Total Keytruda Sales (IV + SC)</td><td>$28,536</td><td>$23,914</td></tr></table>

<table><tr><td colspan="3">Total Keytruda Sales Impact:</td></tr><tr><td>$ Impact</td><td>-$916</td><td>-$849</td></tr><tr><td>% Impact</td><td>-3.1%</td><td>-3.4%</td></tr></table>

<table><tr><td>Whole Co. Sales (GS)</td><td>$69,953</td><td>$71,802</td></tr><tr><td>$ Impact % of Whole Co.</td><td>-1.3%</td><td>-1.2%</td></tr></table>

<table><tr><td>Whole Co. Adj. EBIT (GS)</td><td>$30,779</td><td>$31,593</td></tr><tr><td>$ Impact % of Whole Co.</td><td>-3.0%</td><td>-2.7%</td></tr></table>

Source: GS Global Investment Research

## BMY's Opdivo Qvantig:

We apply the 36% net price discount to the US Opdivo Qvantig sales exposed to Medicare (\~37%, per above). With these assumptions we calculate \~\$270mn sales impact in the 2029-2030 time frame, which represents 4% of Opdivo sales, \~0.8% of total BMY sales, and \~2.5%% of BMY total adjusted EBIT.

Exhibit 4: BMY's Opdivo: Illustrative Incremental Impact of Potential Opdivo Qvantig Inclusion in IRA  
\$ in mn

<table><tr><td>BMY&#x27;s Opdivo - GS estimates</td><td>2029</td><td>2030</td></tr><tr><td colspan="3">Before Opdivo Quantig inclusion in IRA:</td></tr><tr><td>US Sales:</td><td>$4,082</td><td>$3,054</td></tr><tr><td>of which Opdivo Quantig:</td><td>$2,068</td><td>$2,019</td></tr><tr><td>of which Medicare</td><td>$768</td><td>$750</td></tr><tr><td>of which non-Medicare</td><td>$1,300</td><td>$1,269</td></tr><tr><td>of which Opdivo (IV)</td><td>$2,015</td><td>$1,035</td></tr><tr><td>OUS Sales:</td><td>$4,073</td><td>$3,388</td></tr><tr><td>Total Opdivo Sales (IV + SC)</td><td>$8,155</td><td>$6,442</td></tr></table>

Illustrative Opdivo Qvantig inclusion in IRA:

<table><tr><td>US Sales:</td><td>$3,806</td><td>$2,784</td></tr><tr><td>of which Opdivo Qvantig:</td><td>$1,791</td><td>$1,749</td></tr><tr><td>of which Medicare</td><td>$491</td><td>$480</td></tr><tr><td>of which non-Medicare</td><td>$1,300</td><td>$1,269</td></tr><tr><td>of which Opdivo (IV)</td><td>$2,015</td><td>$1,035</td></tr><tr><td>OUS Sales:</td><td>$4,073</td><td>$3,388</td></tr><tr><td>Total Opdivo Sales (IV + SC)</td><td>$7,879</td><td>$6,172</td></tr></table>

<table><tr><td colspan="3">Total Opdivo Sales Impact:</td></tr><tr><td>$ Impact</td><td>-$276</td><td>-$270</td></tr><tr><td>% Impact</td><td>-3.4%</td><td>-4.2%</td></tr></table>

<table><tr><td>Whole Co. Sales (GS)</td><td>$36,089</td><td>$35,853</td></tr><tr><td>$ Impact % of Whole Co.</td><td>-0.8%</td><td>-0.8%</td></tr></table>

<table><tr><td>Whole Co. Adj. EBIT (GS)</td><td>$11,187</td><td>$11,294</td></tr><tr><td>$ Impact % of Whole Co.</td><td>-2.5%</td><td>-2.4%</td></tr></table>

Source: GS Global Investment Research

## Valuation and Risks

## JNJ:

Valuation: We arrive at our 12-month price target of \$275 based on a 20x P/E multiple on our Q5-Q8 EPS.

Key downside risks: The ramp of new products could be slower than we expect, resulting in less revenue to replenish declining products. Further uncertainty related to the Talc litigation could result in higher-than-expected payouts and hamper multiples. A more-difficult-to-navigate external environment related to macro and tariffs could create downside to our estimates.

## MRK:

Valuation: We arrive at our 12-month target of \$137 using a 14.0x multiple on our (Q5-Q8) adjusted EPS.

Key Downside Risks: Faster-than-expected erosion of the Keytruda LOE / lower than expected conversion to SubQ Keytruda. Further slowdown in established vaccine products, slower ramp of newly launched products, and regulatory uncertainty. Disappointments from pipeline assets. Tougher-than-expected regulatory/market environment related to vaccines, FDA, and tariffs, and M&A.

## BMY:

Valuation: We derive our 12-month price target of \$61 through a 10.0x multiple on our Q5-Q8 EPS estimates.

Key upside risks: Commercial — higher than expected revenue growth from the growth portfolio (Cobenfy, Camzyos, Reblozyl, Opdualag, Breyanzi) could create upside to our estimates. Additionally, signs of better than expected durability of the legacy portfolio could create further upside. Financial — better than forecast negative impact to legacy business revenues based on LOEs and IRA implementation as well as more significant flow-through of cost-cutting efforts could create upside to our earnings estimates. Clinical/Regulatory — stronger than expected outcomes from key pipeline programs (e.g. Cobenfy in Alzheimer’s disease psychosis, milvexian in SSP and AF) could lead to both upward revisions to our medium-long-term estimates and expansion of multiples.

Key downside risks: Commercial — slower than expected revenue growth from the Growth portfolio (Cobenfy, Camzyos, Reblozyl, Opdualag, Breyanzi) as well as the legacy portfolio eroding at a faster pace could result in downside to our estimates. Financial — greater than forecast negative impact to base business revenues based on LOEs and IRA implementation could result in significant downside to our estimates. Clinical/Regulatory — negative outcomes from key pipeline programs (e.g. Cobenfy in Alzheimer’s disease psychosis, milvexian AF) could create downside to our estimates.

## Disclosure Appendix

## Reg AC

We, Asad Haider, CFA, Nick Jennings and Jeff Su, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Asad Haider, CFA GS & Co. LLC, Nick Jennings GS & Co. LLC, Jeff Su GS & Co. LLC.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company wi

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
