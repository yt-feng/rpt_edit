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

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses inputs for the fiscal year at least seven quarters in the future compared with the year at least three quarters in the future (on a per-share basis fo

[中间内容因长度限制已省略]

including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

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
