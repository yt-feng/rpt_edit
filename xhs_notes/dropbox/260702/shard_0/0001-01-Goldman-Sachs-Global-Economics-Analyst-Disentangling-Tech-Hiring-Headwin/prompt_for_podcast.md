你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
GLOBAL ECONOMICS ANALYST

# Disentangling Tech Hiring Headwinds: Higher Rates, Overhiring, and AI

Three labor market headwinds—a hawkish Fed pivot that slowed growth and raised rates, AI efficiency gains, and a correction for pandemic-era overhiring—have plausibly contributed to a weaker tech labor market since 2022. Disentangling the role of each is complicated, and some commentators have suggested that companies are “AI-washing” layoffs by falsely attributing them to AI efficiencies. In this Global Economics Analyst, we leverage detailed company/occupation-level employment data to quantify the contribution of each headwind since 2022.

Joseph Briggs +1(212)902-2163 | joseph.briggs@gs.com GS & Co. LLC

Sarah Dong +1(212)357-9741 | sarah.dong@gs.com GS & Co. LLC

First, we find little evidence that higher interest rates have driven the slowdown in tech hiring. Hiring trends are virtually identical across tech companies that were more and less exposed to higher rates.

Second, we find that AI has slowed hiring, but its impact is small. Differences in occupational AI exposure explain around $\frac{1}{2}$ pp of the slowdown in annual tech employment growth since 2022. We also find that AI-layoff announcements appear credible, as companies that announced AI-related layoffs lowered headcount in AI-related occupations more than companies that cited other reasons for layoffs.

Third, we find stronger evidence that hiring has underperformed among companies that overhired between 2020-2022. Statistical estimates that account for both company and occupational hiring trends suggest that headcount normalization can explain up to 2pp of the slowdown in annual tech employment growth since 2022.

The main caveat to our results is that they can only explain around half of the 5pp/year slowdown in tech hiring (vs. trend) since 2022. But our results imply that both AI and post-pandemic headcount normalizations have contributed to the recent tech-sector hiring slowdown, with headcount normalization roughly 3-4 times as important. These relative rankings are generally consistent with company commentary on the role of AI in tech sector layoffs, suggesting AI-washing is not a widespread issue.

## Disentangling Tech Hiring Headwinds: Higher Rates, Overhiring, and AI

After hiring surged during the pandemic, the tech-sector labor market has weakened significantly since late 2022, with job growth in several subsectors underperforming its long-run trend by around 5pp. As a result, the tech sector's share of overall employment has fallen below its long-run trend (Exhibit 1).

Exhibit 1: Tech Sector Employment Has Underperformed Since 2022  
![](images/5f5521aec83a31b9173485b25498a32b0607611c93b0c8372d3d38acb6755f81.jpg)

![](images/40fd3d4858e7cc251d4d55128f32115194cf1648fbefc85beb907baedcd6a2ab.jpg)  
Source: US Bureau of Labor Statistics, Haver Analytics, GS Global Investment Research

Three labor market dynamics—a hawkish Fed pivot that slowed growth and raised rates, AI efficiency gains, and a correction for pandemic overhiring—have plausibly contributed to the tech sector’s labor market pullback since late 2022. But disentangling the role of each is difficult since all three headwinds emerged at the same time. Most notably, the hawkish Fed pivot that raised financing costs and led to a downgrade in growth expectations (thereby possibly kicking off a headcount normalization) arrived at the same time as the release of ChatGPT. And while recent studies and company anecdotes strongly point to significant AI-related uplifts to tech worker productivity, some commentators have suggested that companies are “AI-washing” layoffs by overstating the role of AI.

In this Global Economics Analyst, we leverage detailed company/occupation-level employment data from Revelio Labs to quantify the impact of each of these three headwinds has had on tech sector employment.

The Overall Tech Sector Hiring Slowdown and Identification Challenge Before examining the three potential drivers of the slowdown in tech hiring, we first consider overall tech labor market trends and what questions our new data might be able (and not be able) to answer.

Exhibit 2 illustrates the variation we exploit by scatter plotting 2019-2022 hiring vs. 2022-2025 hiring at both the company- and company/occupation-levels. These scatter plots illustrate several key points.

First, tech hiring slowed broadly across most companies and occupations from 2022-2025, suggesting that aggregate factors and a broad sectoral slowdown in hiring explains a large share of the labor market underperformance in recent years. Our new analysis—which leverages cross-sectional differences in company- and occupation-level hiring patterns—will not be able to conclusively identify the shock that drove this overall slowdown.

Second, both scatters illustrate that hiring patterns differed significantly across companies and particularly across occupations. Leveraging the distribution of hiring shifts across companies that were differentially exposed to higher rates and overhiring and across occupations that are differentially exposed to AI should provide useful insights into the relative importance of the different tech-sector labor market headwinds.

Exhibit 2: Company- and Company/Occupation-Level Headcount Changes Imply a Sharp Slowdown for the Sector Overall, but Substantial Variation  
![](images/5f43151f372e4f5d448dd4ddc80f9c21b332b7e24f1235d606991b630b52f5c6.jpg)  
Source: Revelio Labs, GS Global Investment Research

Against this backdrop, we analyze the role of each hiring headwind separately.

## Interest Rate Effects Appear Minimal

First, we find limited evidence that the tech labor market slowdown is driven by higher rates.

While the Fed's acceleration in rate hikes in late 2022 may have led to a broader downgrade in the tech sector's equity valuations, growth outlook, and hiring plans, we would expect hiring to slow more for companies that are more exposed to rate increases if they were the main driver of hiring underperformance the last several years

To test the effects of higher interest rates on tech hiring, we split our universe of public US tech companies based on changes in their interest coverage ratio (ICR, defined as annual revenue divided by annual interest expense) over the hiking cycle. We find essentially no difference in headcount evolution between the top and bottom ICR change terciles and both are essentially identical to overall tech industry trend (Exhibit

3). The lack of a relationship between interest rate exposure and tech hiring is confirmed by company-level regressions (not shown), leading us to conclude that the effect of higher rates had little impact on the tech sector's labor market underperformance.

Exhibit 3: Interest Exposure Appears to Have Had No Impact on Hiring  
![](images/54cffb8c7bd81cbfdcd228f6c0164b1b1bbcf17df4f45be39a084abd6336c988.jpg)  
Source: GS Global Investment Research

## Small Overall Impact, but Some Evidence AI Layoffs Are Credible Second, we find evidence that AI has slowed hiring, but only modestly.

To test for AI's impact, we leverage our company-occupational panel that measures headcount in over 800 distinct occupations for over 300 public tech companies from 2019-2025. We regress annual occupational headcount growth on the occupation's AI exposure—defined as the share of work tasks that are exposed to AI automation—with a time interaction to capture the evolution of the effect by year, while also controlling for company- and occupation-fixed effects.

The resulting coefficients on the AI exposure-time interaction are shown in the left chart of Exhibit 4. Prior to 2023, AI exposure was positively correlated with occupational headcount growth. But by 2025, a 10pp difference in occupational AI exposure was associated with a 0.4pp drag. We repeat this analysis with the AI displacement scores we developed last year in the right chart of Exhibit 4. Our results are similar, with a one standard deviation gap in vulnerability score having a positive relationship with headcount growth prior to 2022 but implying a 0.4pp drag in 2025.

Given that tech sector employees are, on average, just over 10pp more exposed to AI than the average worker in the US economy according to our scores, this estimate suggests that AI exposure can explain around $\frac{1}{2}$ pp of the tech sector's annual employment growth underperformance relative to economy-wide hiring.

Exhibit 4: Higher AI Exposure Has Weighed Slightly on Employment Growth Since 2023  
![](images/d395926f88088bf96d0e337a16c8577580bd337893b82583271b04c2000e57ec.jpg)  
Source: GS Global Investment Research

We can also see evidence of AI's labor market effects in layoff announcements. To illustrate, we first collect data on public layoff announcements—stratified by those attributed to AI and those attributed to other factors—and merge them with our company-and occupation-level employment data. We then compare hiring trends across companies that did not announce layoffs, that announced layoffs but did not cite AI, and that attributed layoffs to AI.

The left chart of Exhibit 5 unsurprisingly shows that companies that announced layoffs (whether AI-related or not) slowed hiring by more than other companies since 2022, with companies that did not cite AI efficiencies seeing the largest headcount reductions. After reweighting headcount by AI exposure, however, the right chart of Exhibit 5 shows that headcount reductions have been larger for companies that attributed headcount reductions to AI. At a high level, this pattern suggests that companies are reducing headcount in a manner consistent with public announcements.

Exhibit 5: Companies That Attributed Layoffs to AI Experienced Smaller Headcount Reductions on an Overall Basis but Larger on an AI-Weighted Basis  
![](images/b526f9afc63d051d6ceb98b67a16dc060488b86a7b031e63d215224af16f932d.jpg)  
Source: GS Global Investment Research

Exhibit 6 provides more rigorous statistical support for the view that AI-attributed layoff announcements are credible. After converting our panel to event time (and controlling for aggregate drivers), the left chart shows that overall headcount reductions following layoff announcements were similar across companies that did and did not cite AI as justification, but that AI-exposure weighted reductions were larger when layoffs were attributed to AI. The right chart considers the intensive margin of exposure and similarly finds that occupation-level headcount was more sensitive to AI exposure at companies that cited AI efficiencies as the reason for layoffs.

Exhibit 6: AI-Layoffs Led to Similar Overall Headcount Reductions (vs. Non-AI-Layoffs), but Larger Headcount Reductions on an AI-Weighted Basis  
![](images/11d5e25eed0dac5f21ebd5d0b1e1cba76b78b823af383a7dc97fbda360010f8a.jpg)  
Source: GS Global Investment Research

Taken together, these analyses suggest that AI efficiencies have indeed weighed on tech sector hiring over the last several years, particularly at companies that attributed headcount reductions to AI. Effects appear small, however, and the direct differences in occupational exposure can only explain about $\frac{1}{2}$ pp of the 5pp slowdown in annual tech employment growth since 2022.

Post-Pandemic Overhiring Normalization Creates a Moderate Drag Third, we find that pandemic-era overhiring has more meaningfully weighed on job growth in recent years.

The main challenge in testing for overhiring is that headcount is inherently tied to underlying demand, so that it is difficult to tell whether company-level hiring slowdowns reflect actual overhiring or more simply a worse growth outcome. We identify companies that overhired as those who accelerated their pace of headcount growth from 2019 to 2022 while also experiencing declining revenue per employee. $^{1}$ We then test whether this “overhiring” proxy predicts subsequent headcount growth in the post-2022 period.

Exhibit 7 provides an initial illustration of headcount trends stratified by our overhiring proxy. We find that since 2022 total headcount at companies that overhired has grown by 10%, underperforming the tech companies that did not overhire by roughly 7pp.

Exhibit 7: Companies Where Hiring Accelerated the Most from 2020-2022 Slowed More Since 2025, Possibly Due to Slower Productivity Growth  
![](images/3af4c321ec05c2f20788af392fc27d98036524ae0b96dc1b2344c5b22bd2dada.jpg)  
Source: GS Global Investment Research

To statistically test the effect of a pandemic normalization in overhiring, we regress occupation-level headcount growth on the change in hiring from 2020-2022 (vs. 2018-2020) interacted with an indicator for below-average revenue per employee growth. We again include fixed company-and occupation fixed effects to control for aggregate effects. Our resulting estimate implies that a 10pp acceleration in hiring from 2020-2022 was associated with a 1-2pp underperformance in annual occupation-level growth from 2023-2025 (Exhibit 8). Given that sector-wide hiring accelerated by roughly 10pp according to the Revelio data, our statistical estimates suggest that up to 2pp of the slowdown in tech sector hiring can be explained by headcount normalization.

Exhibit 8: Pandemic Overhiring Was Associated with Up to a 2pp Subsequent Slowdown in Job Growth, With Effects Largest for Companies Where Productivity Growth Slowed

![](images/55362440954ebb0a7f467e268d57f92913231a08bac21708a29dc947c263c78f.jpg)  
Source: GS Global Investment Research

## Interpreting Impacts on Overall Tech Labor Market

Our cross-company and cross-occupation estimates suggest that higher interest rates had a limited impact on tech hiring, that AI exposure has slowed hiring by up to $\frac{1}{2}$ pp, and that headcount normalization has slowed hiring by up to 2pp. Combined, these channels can explain up to $2\frac{1}{2}$ pp of the slowdown in annual tech sector headcount growth, or roughly half of its 5pp underperformance (vs. long-run trend) since 2022.

That leaves around half of the hiring underperformance unexplained by cross-company and cross-occupation variation, and therefore attributable to aggregate shocks that are common to all tech companies and workers. While it is hard to identify the source of these shocks, our estimates suggest that post-pandemic overhiring has been 3-4 times as important as AI efficiencies in explaining the slowdown in tech sector employment growth in recent years.

These relative rankings are generally consistent with tech companies' public comments on the role of AI in recent tech sector headcount reductions. The left chart of Exhibit 9 shows that prior to the last few months, very few layoffs in the overall economy were attributed to AI, while the right chart shows a similar pattern for the tech sector specifically. Only in the last year has the share of AI-attributed layoffs risen above $20\%$ .

Although AI has not played a dominant role in slowing tech hiring so far, four patterns suggest that companies are not overstating the role of AI in layoff announcements. First, tech companies that cited AI-efficiencies as a main reason for layoffs have indeed reduced headcount in AI-exposed occupations. Second, most tech companies are still not citing AI as the main driver of layoffs. Third, the share of layoff announcements that cite AI are consistent with our estimates of the relative importance of AI in recent tech

company headcount reductions. Fourth, the time patterns shown in Exhibit 4 and Exhibit 8—which imply that AI-efficiencies played a small role in headcount reductions in 2023 and 2024 but a relatively more important role recently—align with the recent pickup in AI-attributed layoffs. As a result, we do not see “AI-washing” as a widespread issue.

Exhibit 9: Our Results Align with Patterns Suggesting That Most Layoff Announcements Are Not Attributable to AI, Although AI Efficiency Gains Have Contributed to Layoffs Recently

![](images/0332eeddb9983cbf27ad7aab8c3dcb7dba85441ff006bc12f36925b2d59cc3f3.jpg)  
Source: Challenger, Haver Analytics, GS Global Investment Research

![](images/eaca2653a5ff9a07ee0c008899f1e0d3ec3c738ac28d3960057fd5b32d60979b.jpg)

Joseph Briggs

Sarah Dong

## The Global Economics Team

Jan Hatzius +1(212)902-0394 jan.hatzius@gs.com GS & Co. LLC

Megan Peters

+44(20)7051-2058

megan.l.peters@gs.com

GS International

Joseph Briggs +1(212)902-2163 joseph.briggs@gs.com GS & Co. LLC

Sarah Dong +1(212)357-9741 sarah.dong@gs.com GS & Co. LLC

## Disclosure Appendix

## Reg AC

We, Joseph Briggs and Sarah Dong, hereby certify that all of the views expressed in this report accurately reflect our personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Joseph Briggs GS & Co. LLC, Sarah Dong GS & Co. LLC.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; $1\%$ or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of c

[中间内容因长度限制已省略]

 have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

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
