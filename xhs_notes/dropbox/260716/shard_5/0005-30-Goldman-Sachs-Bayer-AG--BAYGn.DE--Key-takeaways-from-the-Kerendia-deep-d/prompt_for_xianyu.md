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
# Bayer AG (BAYGn.DE): Key takeaways from the Kerendia deep-dive event

We hosted Bayer for a Kerendia deep-dive event on July 15 with Bernardo Kanahuati – Kerendia Product Team Lead from Bayer, Dr. Meike Brinker– Kerendia Development Lead from Bayer, and Dr. Vlado Perkovic – Provost and Scientia Professor at the University of New South Wales (no replay available).

Our key takeaways are: 1) Bayer sees a multi-blockbuster opportunity across CKD and Heart Failure, with $800\mathrm{m}+$ patients eligible for therapy, with a strong body of evidence and positive guidelines supporting Kerendia as part of the standard of care; 2) The KOL is optimistic about Kerendia's rapid uptake driven by non-diabetic CKD data which support drug use across various CKD subtypes and in combination of SGLT2s; 3) The KOL underscored Kerendia's competitive advantage over other CKD drugs including Baxfendy (in clinical development) and Vanrafia, while noting combination potential with APRIL inhibitors; 4) Bayer management expressed confidence in a positive outcome of the reduced ejection fraction (HFrEF) trial, noting potential to update peak sales guidance for Kerendia, although data will now likely be disclosed in 2027.

An emerging question on Kerendia is potential future competition from Baxfendy/the Aldosteron Synthetase Inhibitor class - in our view, given the timing of clinical trials, Baxfendy will only have a similar data package to Kerendia c.2 years prior to Kerendia patent expiry, and given the time required for CV launches to accelerate, we see limited impact on Kerendia peak sales - where we sit ahead of Visible Alpha Consensus at €4.5bn vs. c.€3bn. Therefore, we believe Kerendia remains a key source of upside for the Bayer Pharma business, with high gross margins and outsized earnings upside relative to consensus estimates.

James Quigley  
+44(20)7051-3800 |  
james.quigley@gs.com  
GS International

Rajan Sharma  
+44(20)7051-7995 | rajan.sharma@gs.com GS International

Max Da, Ph.D.
+44(20)7051-8835 | max.da@gs.com
GS International

Shyam Kotadia  
+44(20)7051-6153 |  
shyam.kotadia@gs.com  
GS International

Kaaviya Ganesan +1(332)245-7519 | kaaviya.ganesan@gs.com GS India SPL

## Detailed takeaways

Commercial opportunity could be significant, with 800m+ patients eligible for Kerendia treatment across heart failure and CKD. From an unmet need/addressable population perspective, Bayer highlighted that in the past 12 months around 2.5m patients have been treated with Kerendia. In CKD, Kerendia is approved in 102 countries and has launched in 93 countries, while in heart failure, Kerendia has been approved in 46 countries and launched in 14 markets – with blockbuster potential in each area.

☐ Our view; Applying the current average price per patient over the past 12 months (2.5m patients vs. c.€1bn revenue), suggests around 9-10m patients being treated with Kerendia globally at peak in 2032 of €4.5bn, which given the current trajectory, and 6.5 years, is very achievable. Especially, with the non-diabetic CKD and heart failure with reduced ejection fraction populations still to contribute to the peak sales potential.

The KOL is optimistic about Kerendia's rapid uptake driven by non-diabetic CKD data which support drug use across various CKD subtypes and in combination with SGLT2s. This data supports the drug's utility across diverse CKD subtypes and in combination with SGLT2 inhibitors (as highlighted in the CONFIDENCE trial), which have become standard-of-care. The KOL also noted that physicians understand the underlying reasons for the acute eGFR decline observed in the FIND-CKD trial, and therefore, do not anticipate it will hinder clinical adoption. In terms of overcoming clinical inertia in the community, the KOL pointed towards the SGLT-2 class, which saw stronger uptake in CKD when a CV benefit was seen in the non-diabetic setting, which could benefit Kerendia uptake following the FIND-CKD data.

The KOL underscored Kerendia's competitive advantage over other CKD drugs including Baxfendy (in clinical development) and Vanrafia, while noting combination potential with APRIL inhibitors. For IgAN patients, the KOL noted a two-pronged treatment approach: addressing IgAN-specific drivers (e.g., inhibiting toxic IgA synthesis) and managing generic responses (e.g., reducing proteinuria and blood pressure). This strategy suggests a potential for Kerendia to be combined with APRIL inhibitors. Regarding competition from Vanrafia, KOLs noted Kerendia's comparable efficacy and highlighted the benefit of physician familiarity, given Kerendia demonstrated efficacy across various CKD subtypes, including IgAN. With respect to Baxfendy, which is currently in Phase 3 trials with results anticipated in 2028/2029, the KOL acknowledged that a combination with Kerendia is unlikely. Nevertheless, he pointed to Kerendia's first-mover advantage as a significant factor supporting its clinical utility, while ultimately stressing that future clinical trial data will be the key determinant.

☐ Our view; We agree that optically, based on UACR/UPCR data, Vanrafia and Kerendia look similar in IgAN (c.35% decline vs. c.39% decline for Kerendia). A key difference will come from cost - the list price of Vanrafia is \$14,291 per month vs. \$1,100 per month for Kerendia, which gives Kerendia a volume advantage with payors/ PBMs in our view. This could be a negative impact on our Novartis Vanrafia peak sales forecast of \$1.2bn.

☐ On Baxfendy competition, the overlapping mechanism/ safety profiles (hyperkalemia) make combination therapies unlikely. Phase 3 data for Baxfendy + Farxiga in BaxDuo-Arctic (CKD with hypertension) is expected in 2028 with approval by end 2028, and BaxDuo-pacific is anticipated by the end of 2029, with approval by mid-2030 and Prevent-HF is also expected by the end of 2029, with approval by mid-2030. Therefore, it will take at least a further four years before Baxfendy has a similar label to Kerendia, by which time, we will be almost 2 years away from Kerendia generic entry, and Baxfendy will take time to drive physician education and uptake (in line with general CV launches). Therefore, we are not concerned about the near-to-mid term potential competitive threat from Baxfendy.

Bayer management expressed confidence in a positive outcome of the reduced ejection fraction (HFrEF) trial, noting potential to update peak sales guidance for Kerendia. They cited supportive data from Phase 2 studies and subgroup analyses within the Phase 3 FINEARTS-HF trial, which demonstrated consistent benefits in patients with lower ejection fraction values. Additionally, the company's peak sales guidance on Kerendia could be updated at the right time, per management.

☐ Our view; We continue to believe that the data from the ARTS-HF trial (the original Phase 2 trial in HFrEF patients), combined with FINEARTS-HF provide strong evidence that both FINALITY-HF and CONFIRMATION-HF will both yield positive results. We continue to believe that the heart failure indication, could be one of the key reasons why our forecasts are significantly ahead of Vare Consensus peak sales with GSe peak of €4.5bn vs. consensus of around €3bn.

## Valuation and risks

We are Buy rated on Bayer. Our DCF valuation (50% weighting in the PT) is €65 per share which assumes an 8.8% WACC and TV growth rate of 1.5%. Our SOTP-based valuation (50% weighting in the PT) is €60 per share. This leads to our 12-month target price of €62.5.

Key downside risks to our view and price target: (1) Earnings momentum in Crop Science returning to negative territory; (2) Greater-than-anticipated margin impact from Pharma generics holding back divisional earnings development; (3) Negative outcomes and slower resolution across the various litigation processes; (4)

Slower-than-anticipated realisation of the cost and operational benefits from the new DSO operating model.

<table><tr><td>BAYGn.DE</td><td>12m Price Target: €62.50</td><td colspan="2">Price: €49.12</td><td colspan="2">Upside: 27.2%</td></tr><tr><td>Buy</td><td colspan="5">GS Forecast</td></tr><tr><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td rowspan="9">Market cap: €48.3bn / $55.2bn Enterprise value: €81.8bn / $93.6bn 3m ADTV: €131.4mn / $151.8mn Germany Europe Pharma &amp; Life Sciences M&amp;A Rank: 3 Leases incl. in net debt &amp; EV?: Yes</td><td>Revenue (€ mn)</td><td>45,575.0</td><td>45,558.5</td><td>46,878.9</td><td>48,523.7</td></tr><tr><td>EBIT (€ mn)</td><td>8,082.0</td><td>7,394.2</td><td>8,027.0</td><td>8,955.7</td></tr><tr><td>EPS (€)</td><td>4.91</td><td>4.32</td><td>4.61</td><td>5.43</td></tr><tr><td>P/E (X)</td><td>5.3</td><td>11.4</td><td>10.7</td><td>9.1</td></tr><tr><td>EV/EBITDA (ex lease,X)</td><td>5.8</td><td>8.6</td><td>7.9</td><td>7.1</td></tr><tr><td>Dividend yield (%)</td><td>0.4</td><td>2.3</td><td>2.4</td><td>2.6</td></tr><tr><td>FCF yield (%)</td><td>13.5</td><td>(1.4)</td><td>8.3</td><td>9.4</td></tr><tr><td>CROCI (%)</td><td>1.0</td><td>7.8</td><td>7.4</td><td>7.7</td></tr><tr><td>N debt/EBITDA (ex lease,X)</td><td>3.2</td><td>3.5</td><td>3.2</td><td>2.8</td></tr><tr><td></td><td></td><td>12/25</td><td>3/26E</td><td>6/26E</td><td>9/26E</td></tr><tr><td></td><td>EPS (€)</td><td>0.62</td><td>2.71</td><td>0.77</td><td>0.44</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 14 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, James Quigley, Rajan Sharma, Max Da, Ph.D., Shyam Kotadia and Kaaviya Ganesan, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: James Quigley GS International, Rajan Sharma GS International, Max Da, Ph.D. GS International, Shyam Kotadia GS International, Kaaviya Ganesan GS India SPL.

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

The rating(s) for Bayer AG is/are relative to the other companies in its/their coverage universe: AstraZeneca, Bayer AG, GSK Plc, GSK Plc (ADR), Galderma, Lonza Group, Novartis, Novartis (ADR), Novo Nordisk, Novo Nordisk (ADR), Roche, Sandoz Group AG, Sanofi, Sanofi (ADR), Sartorius AG, Sartorius Stedim Biotech

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS has received compensation for investment banking services in the past 12 months: Bayer AG (\$7.68) and Bayer AG (€49.12)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Bayer AG (\$7.68) and Bayer AG (€49.12)

GS has received compensation for non-investment banking services during the past 12 months: Bayer AG (\$7.68) and Bayer AG (€49.12)

GS had an investment banking services client relationship during the past 12 months with: Bayer AG (\$7.68) and Bayer AG (€49.12)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: Bayer AG (\$7.68) and Bayer AG (€49.12)

GS had a non-securities services client relationship during the past 12 months with: Bayer AG (\$7.68) and Bayer AG (€49.12)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history 

[中间内容因长度限制已省略]

including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY

10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
