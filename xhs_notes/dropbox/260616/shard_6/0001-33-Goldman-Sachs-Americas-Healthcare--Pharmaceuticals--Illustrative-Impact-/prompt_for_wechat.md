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
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`GS`。标题格式建议：`# GS：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

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

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses inputs for the fiscal year at least seven quarters in the future compared with the year at least three quarters in the future (on a per-share basis for all metrics).

For a more detailed description of how we calculate the GS Factor Profile, please contact your GS representative.

## M&A Rank

Across our global coverage, we examine stocks using an M&A framework, considering both qualitative factors and quantitative factors (which may vary across sectors and regions) to incorporate the potential that certain companies could be acquired. We then assign a M&A rank as a means of scoring companies under our rated coverage from 1 to 3, with 1 representing high (30%-50%) probability of the company becoming an acquisition target, 2 representing medium (15%-30%) probability and 3 representing low (0%-15%) probability. For companies ranked 1 or 2, in line with our standard departmental guidelines we incorporate an M&A component into our target price. M&A rank of 3 is considered immaterial and therefore does not factor into our price target, and may or may not be discussed in research.

## Quantum

Quantum is GS' proprietary database providing access to detailed financial statement histories, forecasts and ratios. It can be used for in-depth analysis of a single company, or to make comparisons between companies in different sectors and markets.

## Disclosures

The rating(s) for Bristol-Myers Squibb Co., Johnson & Johnson and Merck & Co. is/are relative to the other companies in its/their coverage universe: AbbVie Inc., BioNTech, Bristol-Myers Squibb Co., Eli Lilly & Co., Innoviva Inc., Johnson & Johnson, Merck & Co., NewAmsterdam Pharma, Pfizer Inc., Royalty Pharma Plc, Vaxcyte Inc.

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS has received compensation for investment banking services in the past 12 months: Bristol-Myers Squibb Co. (\$56.24), Johnson & Johnson (\$235.66) and Merck & Co. 

[中间内容因长度限制已省略]

m impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
