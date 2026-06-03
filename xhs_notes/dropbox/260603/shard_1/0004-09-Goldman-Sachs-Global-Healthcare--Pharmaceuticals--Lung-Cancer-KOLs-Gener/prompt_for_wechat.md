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
1. `# 标题`：一句主判断，不超过 32 字。
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
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Global Healthcare: Pharmaceuticals: Lung Cancer KOLs Generally Positive on ASCO Developments

On the back of the American Society of Clinical Oncology (ASCO) conference, we hosted two lung cancer KOLs to discuss key updates, notably MRK/Kelun's sac-TMT optiTROP-05 trial in NSCLC, SMMT/Akeso's single-region (China) Ph3 HARMONi-6 overall survival results for ivonescimab+chemotherapy in frontline squamous NSCLC, and readthrough on programs from AZN, BNTX/BMY, and PFE.

Key takeaways from the discussion include: 1) sac-TMT's strong PFS was well-received with the KOLs optimistic around the safety profile and ability to manage toxicity, noting the final global overall survival (OS) data will ultimately be important in guiding treatment decisions; 2) ivo's OS benefit over Tevimbra (anti-PD-1, similar to MRK's Keytruda) is meaningful, albeit the KOLs acknowledged debates regarding efficacy in older patients and noted confirmation in the global Ph3 HARMONi-3 study is needed, where they see a high PoS for the squamous cohort final PFS analysis in 2H; and 3) For AZN's Datroway, while the developmental lead was noted, the KOLs see potential for superior efficacy and safety from sac-TMT based on China data, contingent on global trial validation. The KOLs also highlighted novel approaches they are watching in lung cancer including tri-specifics (PD1xCTLA4xVEGF) and RAS-inhibitors.

## Key Takeaways

In parallel with the American Society of Clinical Oncology (ASCO) meeting, we spoke with two KOLs: 1) a Professor of Oncology at Johns Hopkins University School of Medicine and Trinity College Dublin, and 2) an Assistant Professor, and Medical Director of Oncology at Stanford University, to discuss key non-small cell lung cancer (NSCLC) data from the conference. The Johns Hopkins KOL is a thoracic medical oncologist who sees \~200 patients annually in his practice, almost all NSCLC, with a \~70% non-squamous, 25%-30% squamous distribution, and a focus on early-phase immunotherapy trials. The Stanford KOL is a medical oncologist who sees a substantial NSCLC population, with prior experience in gastrointestinal cancer and melanoma via prior roles at Memorial Sloan Kettering Cancer Center and the Dana-Farber Cancer Institute.

We highlight the following key takeaways from the discussion:

■ Current 1L mNSCLC patient management. Both doctors first check for the

Asad Haider, CFA

+1(212)902-0691 | asad.haider@gs.com

GS & Co. LLC

Salveen Richter, CFA

+1(212)934-4204

salveen.richter@gs.com

GS & Co. LLC

Rajan Sharma

+44(20)7051-7995

rajan.sharma@gs.com

GS International

Nick Jennings

+1(415)249-7412

nick.jennings@gs.com

GS & Co. LLC

Mark Aleynick, Ph.D.

+1(212)357-6820

mark.aleynick@gs.com

GS & Co. LLC

Max Da, Ph.D.

+44(20)7051-8835 | max.da@gs.com

GS International

Jeff Su

+1(212)357-9930 | jeff.su@gs.com

GS & Co. LLC

presence of actionable genetic alterations, and if there are none, treatment is determined by PD-L1 expression and histology (squamous/non-squamous). For patients that are PD-L1 TPS >= 50%, one KOL favors Keytruda monotherapy while the other favors Keytruda + chemotherapy, because he feels that provides the best opportunity for a response. For patients below TPS 50%, both use Keytruda + chemo, with the chemo being histology specific.

## Overall impressions of MRK partner Kelun's sac-TMT OptiTROP-Lung05 data.

From an efficacy and safety perspective, one KOL noted the sac-TMT arm performance was impressive (one of the few drugs that he has seen show a PFS HR that significant, acknowledging that Keytruda monotherapy is not the relevant control arm globally) and that the tox is a little more than chemo so is watching AEs that can be an issue for some patients, such as stomatitis and ILD, but overall is optimistic that the global trials will be positive. The other KOL noted the Keytruda arm seemed to underperform, and there was a trend to OS, and described the sac-TMT arm discontinuation rate of \~5% as amazing.  
sac-TMT toxicity profile. Focusing on the safety data known thus far, one KOL noted the profile seems similar to AZN's Dato-DXD, and notes that in his experience with ADCs, patients' individual reactions and/or ability to tolerate can be highly variable. The other KOL noted that when he discusses ADCs with patients, he anticipates chemo-like side effects, and believes those to be manageable, and noted that he was encouraged that they did not see unique side effects (pneumonitis, ocular, etc).  
■ sac-TMT efficacy profile. From an efficacy perspective, the KOLs agreed that all groups showed benefit, with PD-L1 high where there is clearest relevance (given Keytruda monotherapy control arm), as there are some patients for whom Keytruda mono is the better choice.  
Bars for clinical decision making. One KOL provided a range for how he interprets HRs in baseball terms, with better than 0.85 being a single, \~0.7 to \~0.85 being a double, \~0.5 to \~0.7 being a triple and below 0.5 being a home run, and also considering the shape of the curve, aiming to steer patients towards options with higher survival benefit — for the next sac-TMT data set, he would be looking for HR of 0.7 to 0.8 with response rates of 65% to 70% to displace the standard of care, noting the Keytruda patent expiry in 2028 could increase pressure (by insurers) to use the drug. The other KOL agrees broadly, but sees ADCs more for non-squamous disease, and PD1xVEGF for squamous — for OS, he notes that in order to be stat sig, HR will usually be less than 0.8, and believes the bar for clinically meaningful HR is 0.75.  
Overall impressions of SMMT partner Akeso's HARMONi-6 OS data. The KOLs noted the overall survival (OS) benefit seen with SMMT and partner Akeso's PD1xVEGF bispecific ivonescimab (ivo) over Tevimbra (ONC's anti-PD-1, similar to MRK's Keytruda) + chemotherapy in the Ph3 HARMONi-6 study is meaningful and suggests ivo is an effective therapy, with relatively little drop-off between progression-free survival (PFS; HR=0.60) and OS (HR=0.66). However, acknowledging debates from the plenary discussion section regarding the

perceived lack of benefit in the age>65 subgroup (see management commentary here), they cautioned that the China-only study needs to be repeated in a global population (which typically includes older patients).

Additionally, regional pathophysiological differences in NSCLC per smoking and other factors is possible, further supporting the need for global confirmation. On safety, the KOLs highlighted that HARMONi-6 included patients who have higher bleeding risk per blood vessel encasement, who would traditionally not be candidates for VEGF therapies, noting relatively little VEGF-mediated toxicity (hypertension, hemorrhage) for ivo as differentiating from bevacizumab, and that immune-mediated toxicities were similar to those seen with Keytruda.

HARMONi-6 translation to the global HARMONi-3 study. On translation of the HARMONi-6 results to SMMT's global Ph3 HARMONi-3 frontline NSCLC study, the KOLs believe the final PFS results from the squamous HARMONi-3 cohort in 2H are likely to be positive, as the totality of positive ivo data across HARMONi-6 and other indications (e.g. global Ph2 colorectal cancer data shared at ASCO) suggests the efficacy signal is real. When discussing readthrough of the squamous-only HARMONi-6 data to non-squamous NSCLC (recall, the global Ph3 HARMONi-3 study contains a squamous and a non-squamous NSCLC patient cohort), the KOLs noted that squamous NSCLC is generally more homogeneous, with a greater prevalence in smokers, thus per the available data greater benefit is expected in squamous patients, noting modest readthrough between the histologies. Overall, the KOLs believe ivo could potentially be better than Keytruda, and await data from the global Ph3 HARMONi-3 study for clarity on the magnitude of benefit.

When comparing NSCLC data across bispecifics, including ASCO presentations from BNTX/BMY's pumitamig and PFE's PF'4404, the KOLs noted minimal drop-off in efficacy when going from China-only to global data, and that the data overall support the PD1/L1xVEGF class. The KOLs additionally highlighted promising novel approaches including the tri-specific PD1xCTLA4xVEGF molecule CS2009 from the Chinese biotech CStone Pharmaceuticals.

The KOLs highlighted AZN's Datroway's developmental lead while acknowledging sac-TMT's potential for superior efficacy and safety based on China data, contingent on global trial validation. The KOLs highlighted Datroway's developmental lead, noting the FDA approval of the monotherapy and established clinical experience, which simplifies physicians' integration of the combination of Datroway and IO therapies into their treatment algorithm. While acknowledging sac-TMT's potential for superior efficacy, based on current China data, and its low discontinuation rates in those trials, the KOLs underscored the requirement for these results to be validated in global studies. With respect to the AVANZAR trial, the biomarker strategy was noted as sound, with Datroway showing potential for greater efficacy over pemetrexed. However, the selection of Imfinzi instead of Keytruda for the control arm introduced risks.

Novel approaches the KOLs are watching in lung cancer. In terms of emerging treatment paradigms, the KOLs highlighted potential for multiple “novel-novel” combinations including ADCs + IO, bispecifics, trispecifics (PD1xCTLA4xVEGF) and called out RAS-inhibitors as an area of interest (including combining these with

IOs/ADCs).

## Valuation and Risks

MRK (Buy). Valuation: We arrive at our 12-month target of \$137 using a 14.0x multiple on our (Q5-Q8) adjusted EPS. Downside risks: Faster-than-expected erosion of the Keytruda LOE / lower than expected conversion to SubQ Keytruda. Further slowdown in established vaccine products, slower ramp of newly launched products, and regulatory uncertainty. Disappointments from pipeline assets. Tougher-than-expected regulatory/market environment related to vaccines, FDA, and tariffs, and M&A.

SMMT (Buy). Valuation: Our 12-month PT of \$41 is based on a blended 85%/15% risk-adjusted DCF value of \$35 (WACC of 18% and TGR of 2%) and a theoretical M&A value of \$73 (11x 2031E sales). Downside risks: Clinical, technology and manufacturing risk - data generated by partner Akeso in China may not translate to SMMT's global clinical studies; U.S.-China trade relations may adversely impact supply chain operations; unexpected safety issues or clinical delays may push launch timelines. Regulatory risk - failure to secure regulatory approval for indications or territories could impact commercial success and would pose significant downside risk to our sales estimates. Competitive risk - competitor PD-1/L1xVEGF assets could demonstrate superior data, or advance through clinical development ahead of expectations. Financing risk/dilution.

AstraZeneca (Buy): Our 12-month price target is derived from a 50:50 blend of DCF and P/E. Our bottom-up DCF analysis suggests a valuation of 15,912p per share (WACC 8.0%; TGR 2.5%) and on a multiples basis we believe AstraZeneca should trade on 20x 2027E EPS, giving a valuation of 17,318p per share. As a result, our price targets are 16,525p/\$219 per share. Key risks to our view and price target: (i) Clinical trial failure; (ii) Commercial execution; (iii) Pricing; (iv) Competitive developments; and (v) Patent exposure.

## Disclosure Appendix

## Reg AC

We, Asad Haider, CFA, Salveen Richter, CFA, Rajan Sharma, Nick Jennings, Mark Aleynick, Ph.D., Max Da, Ph.D. and Jeff Su, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Asad Haider, CFA GS & Co. LLC, Salveen Richter, CFA GS & Co. LLC, Rajan Sharma GS International, Nick Jennings GS & Co. LLC, Mark Aleynick, Ph.D. GS & Co. LLC, Max Da, Ph.D. GS International, Jeff Su GS & Co. LLC.

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

## Pricing information

AstraZeneca (\$179.71), AstraZeneca (13,434p), Merck & Co. (\$115.17) and Summit Therapeutics Inc. (\$15.71)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

Distribution of ratings: See the distribution of ratings disclosure above. Price chart: See the price chart, with changes of ratings and price targets in prior periods, above, or, if electronic

[中间内容因长度限制已省略]

 impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global

Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
