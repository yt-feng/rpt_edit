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
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`GS`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
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
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

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
# Americas Healthcare: Biotechnology: Takeaways from our lunch with Endocrinologist on key launches, recent data

We hosted a lunch with an adult endocrinologist, Dr. Aren Skolnick (\~350 monthly patients under care), where we discussed a broad range of endocrine conditions including: hypoparathyroidism, Congenital Adrenal Hyperplasia, Post-bariatric Hypoglycemia, Prader-Willi syndrome, Hypothalamic Obesity, achondroplasia, acromegaly, and Graves' disease/Thyroid Eye disease. Across indications, the physician is using novel therapies in a handful of patients noting good experience to-date with Yorvipath, Crenessity, and Vykat in particular, despite insurance/reimbursement hurdles which he cited are an issue across high price point rare disease therapies that his office is navigating, often with significant support from manufacturers. With respect to development stage candidates, the doctor sees i) potential for atulmenant to be differentiated via convenience/mechanism of action in CAH (particularly for patients not well managed on Crenessity), ii) recent setmelanotide data in PWS as unprecedented with respect to weight loss, and compelling on quality of life endpoints, iii) significant unmet need in PBH that could be addressed by avexitide (with a $50\%$ absolute reduction in L2/L3 events the bar for clinical meaningfulness), and iv) encouraging evidence of clinical activity with canvuparatide, noting responder analyses in clinical trials do not reflect real-world treatment practice.

Please see within for additional details.

Corinne Johnson +1(917)343-1445 | corinne.johnson@gs.com GS & Co. LLC

Paul Choi
+1(212)902-5217 | paul.k.choi@gs.com
GS & Co. LLC

Richard Law, Ph.D.  
+1(212)357-6054 | richard.law@gs.com  
GS & Co. LLC

Daniel Ni, Ph.D.  
+1(212)902-2365 | daniel.ni@gs.com  
GS & Co. LLC

Kevin Strang, Ph.D.  
+1(212)357-7227 |  
kevin.strang@gs.com  
GS & Co. LLC

Jane Wu, Ph.D.  
+1(212)357-0180 | jane.wu@gs.com  
GS & Co. LLC

Erik Wong  
+1(212)357-9964 | erik.wong@gs.com  
GS & Co. LLC

Anupam Srivastava +1(332)245-7980 | anupam.srivastava@gs.com GS India SPL

## Key takeaways

## Hypoparathyroidism (ASND, MBX)

Weekly-dosing is preferable, but real-world adoption is dictated by the comprehensive data profile.

The KOL manages roughly ten HPT patients in his clinic, of which half of the patients were well managed and five patients were currently treated with Yorvipath.

The doctor noted patients who have escalated to Yorvipath don't mind the daily injection frequency, and were overall satisfied to taper off the supplements and were still able to sustain blood calcium levels.

■ Yorvipath were initially prescribed in the severe and poorly managed patients (have hypocalcemia events in regular basis/ kidney issues) or are hospitalized, and is now moving towards use in the moderately controlled population.

## KOL sees a $50\%$ response rate threshold for the weekly-injectables.

On the recent MBX once-weekly canvuparatide 52-week data update that showed a decline in responder rate to $57\%$ vs. $79\%$ at 26 weeks (see note), the KOL noted Yorvipath still stands as the gold standard in terms of treatment (recall, Yorvipath Ph3 data demonstrated stable efficacy of c.80% over 26-52 weeks). However, the KOL sees a $50\%$ response rate as a reasonable trade-off threshold for a weekly-injectable, and noted that response criteria in clinical studies which limit PRN use do not reflect real-world treatment practice and thus should be evaluated in the context of the totality of clinical benefit.

\- Canvuparatide is most likely to capture patients who are stable on daily dosing and want a less-frequent dosing interval. Additionally, he might start new patients who otherwise wouldn't tolerate daily injections. Ahead, he wants to monitor if the efficacy in longer follow-ups sustains.

\- With respect to pricing, the KOL thinks canvuparatide could be priced at a premium, though expects some payor hurdles.

## Congenital Adrenal Hyperplasia (NBIX, CRNX)

## Positive experience with Crenessity, atumelnant could address unmet need via differentiated mechanism of action

Our expert is treating around 20 CAH patients and has been using Crenessity in three of his female patients to better control high androgen levels. Use has been limited thus far based on patient symptom burden (including Cushingoid symptoms), while some patients do not have the classic form of CAH and others have not been to the office since Crenessity's launch (1-2x visits per year is standard). The three patients on Crenessity have been able to lower their GC usage while achieving lower weight and glucose levels. Reimbursement has been manageable, with NBIX helpful in navigating through documentation and prior authorization requirements, and it usually only takes 3-4 weeks for payers to approve patients for Crenessity.

The physician found the recent 2-year update on bone effects for Crenessity to be useful since younger patients are still accruing their peak bone mass and can further support use in these patients. The cardiometabolic benefits were already expected. However, the doctor noted that the 2x daily dosing requirement for Crenessity and lack of impact on androgen (stabilization vs. reductions observed) are limitations of the medication. These drawbacks could incentivize the expert to use atumelnant when it is approved due to its once daily oral dosing and the potential to lower A4 levels to below the upper limit of normal (ULN) based on its differentiated MC2R antagonist mechanism, particularly among treatment naïve patients and those who are symptomatic or not well controlled on Crenessity. The expert mentioned that two of his three patients on Crenessity could potentially benefit from switching to atumelnant, but acknowledged this is a small sample size.

■ With respect to liver tox findings previously observed with atumelnant, the physician is not concerned given the incidence is low and cases seem mild. However, if future results suggest that LFT levels exceed 3x ULN this could present a reason for concern.

## Post-Bariatric Surgery Hypoglycemia (AMLX)

## Significant unmet need in PBH population, estimated at 15-20% of patients and reflected in patient demand for new therapeutic options

The physician characterized this as a very high unmet need population, noting patient engagement among the highest across his practice with respect to patients seeking new and better treatment options and frustration with current standard of care. He noted that standard of care options like diazoxide do not work well, and come with significant quality of life burden; while he has tried GLP-1 agonists (predicated on slowing gastric emptying), these do not work particularly well and a significant portion of patients require new options.

\- Of \~30 patients under his care, the doctor noted \~40% are not well managed with dietary modifications or existing therapy and at least 15-20% are having regular, severe, hypoglycemia events. The latter population would be the most obvious candidates for treatment initiation on approval of avexitide, and we note that this aligns closely with our own estimates that \~30K patients would form the initial addressable market (relative to 160K patient prevalence).

Ahead of Ph3 data, the KOL noted a 50% absolute reduction in Level 2/Level 3 events would be compelling with respect to efficacy, which compares to assumptions underpinning trial design of a 35% placebo-adjusted improvement and expectations for \~50% placebo response.

While the physician anticipates documentation will be required for insurance coverage of avexitide, if approved for PBH, he does not see this as a meaningful hurdle for treatment adoption noting classification of PBH vs. other forms of hypoglycemia is already standard practice.

In addition to PBH, the KOL sees some promise in the use of avexitide or another GLP-1 antagonist for the treatment of other forms of hypoglycemia.

## Prader-Willi Syndrome (NBIX, CRNX, RYTM)

## Enthusiasm for both Vykat and setmelanotide in this very difficult to treat patient population

The physician is currently using Vykat in a handful of patients with plans to inform his broader population of the new option, noting his experience to-date reflects improvement in patient and especially caregiver quality of life. The latter is of particular importance to him, and will inform plans to expand use of this agent over time. With respect to safety, while the doctor is monitoring for edema/hyperglycemia, and may restrict the drug from patients at risk of these effects, he has not observed significant side effects to-date. Insurance reimbursement has been a moderate hurdle to treatment adoption.

■ Regarding recent data from RYTM in PWS, the physician commented that weight loss results were unprecedented relative to this difficult to treat and highly metabolic resistant population, noting GLP-1s in the population may deliver 1-3% weight loss over a year. Moreover, benefit on HCQT was described as impressive, and consistent with his experience using Vykat, the doctor sees these quality of life endpoints as particularly important for the population of patients with PWS.

To that end, he would hope to see benefit on HCQT prioritized in registrational studies, though effect on both weight and quality of life endpoints would be a best case scenario (noting Vykat does not improve weight). In a registrational study evaluating weight changes, the doctor noted most patients reach stable (but elevated) weight in their late 20s/early 30s, and he would not anticipate significant weight gain in those age groups (when considering potential placebo performance).

If reimbursed by insurance, the physician would find combination use of setmelanotide with Vykat as compelling given distinct mechanisms of action.

## Hypothalamic Obesity (RYTM)

The physician has not yet prescribed Imcivree for HO, noting patients are seen only 1-2x per year, but plans to put \~20% of patients on therapy near-term based on their weight/refractoriness to therapy and comorbidities. Given this is an adult population, the physician noted that GLP-1 reimbursement is relatively straightforward and provides up to 15% weight loss in some patients.

## Thyroid Eye Disease / Graves' Disease (VRDN, ROIV/IMVT)

We touched briefly on Graves' disease, where the physician noted $\sim 25\%$ of his patients are not well-controlled on anti-thyroid medications and another portion are controlled but cannot get off of ATDs, with both likely to be candidates for advanced therapies in the indication like FcRns or IgG degraders. He would anticipate a mix of chronic use and intermittent treatment with these agents, similar to current practice with ATDs.

## Achondroplasia (ASND, BBIO, BMRN, TYRA)

## Oral options could meaningfully expand treatment for achondroplasia

The KOL manages ten pediatric ACH patients, which are a mix of hereditary and de novo cases. Two of his patients are currently on Voxzogo. With respect to limited adoption to-date, he sees daily injections as a huge burden in pediatric care, and thinks weekly Yuviwel could bring more patients in for treatment. Oral drugs would be a good fit for ACH when introduced (such as infigratinib and dabogratinib), and note that some patients might be deferring treatment for the orals to launch.

The KOL noted families are sometimes hesitant to start new medications, but thinks the practice will add 3 patients on infigratinib vs 3-4 on injections out of the 10 patients in his care.

■ FGFR3 biology: The KOL cares about the hyperphosphatemia associated with FGFR effects. That said, he thinks it is manageable and overall not a clinical deterrent to getting on therapy. While early, the KOL thinks dabogatinib could be comparable or slight better than infigratinib in a pivotal study given greater selectivity for FGFR3.

## Acromegaly (CRNX)

## Palsonify used in $10\%$ patients but half may qualify, fasting could be challenging to manage

\- Our expert is treating around 20-25 acromegaly patients and has been using Palsonify for 2-3 of these patients. The limited usage is due to short time since approval, payers requiring step edits through 2-3 drugs due to Palsonify's high list price, and availability of oral Mycapssa since 2020. The expert's practice has a specialized pituitary center which is why he is able to treat more acromegaly patients. Compared to CAH, acromegaly has many effective treatment options.

\- Palsonify's 1-hour post-dose fasting requirement is somewhat problematic since many patients have transphenoidal resection and $80\%$ of these patients have thyroid deficiencies that require Synthroid treatment that also have fasting requirements. The various fasting requirements from these treatments are challenging to manage for patients. However, the expert will increase use in the future and 10 of his patients could qualify for Palsonify.

## Disclosure Appendix

## Reg AC

We, Corinne Johnson, Paul Choi, Richard Law, Ph.D., Daniel Ni, Ph.D., Kevin Strang, Ph.D., Jane Wu, Ph.D., Erik Wong and Anupam Srivastava, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Corinne Johnson GS & Co. LLC, Paul Choi GS & Co. LLC, Richard Law, Ph.D. GS & Co. LLC, Daniel Ni, Ph.D. GS & Co. LLC, Kevin Strang, Ph.D. GS & Co. LLC, Jane Wu, Ph.D. GS & Co. LLC, Erik Wong GS & Co. LLC, Anupam Srivastava GS India SPL.

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

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; $1\%$ or other ownership; compensation for certain services; t

[中间内容因长度限制已省略]

 impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g.,

marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
