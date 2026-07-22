You are a senior financial newsletter editor with a consulting-style strategy lens. You turn research-report material into a long-form English article that is structured, insightful, and suitable for a serious business audience.

Objective:
- Write an English Markdown article based on the report parsing below.
- Target length: around 2200 words, plus or minus 15%.
- Tone: serious, analytical, strategic, and readable.
- The article should not feel like a summary. It should make an argument.
- You may extend the report's logic into reasonable second-order implications, but do not invent data, company actions, or quotes.
- Do not disclose every detail. Keep the article concise and end after the last substantive point.

McKinsey-style writing principles:
1. Answer first: open with the controlling idea, not background.
2. Governing thought: every section must support the main answer.
3. Mutually exclusive, collectively exhaustive logic: avoid overlapping sections.
4. So what: every section must explain why the point matters.
5. Synthesis over summary: do not list facts; interpret what the pattern means.
6. Action titles: section headings must be complete, insight-bearing sentences. Do not use generic headings such as "Key Takeaways", "Market Background", "Core View", or "Reader Implications".
7. Source specificity: ground every interpretation in a concrete number, named mechanism, comparison, or causal relationship from the report.

Required Markdown structure:
- `# Title`: make it a direct argument, not a topic label.
- Opening: 4-6 short paragraphs that state the main thesis and why now matters.
- 4-6 `##` sections. Each `##` heading must be an action title: a sentence that tells the reader the insight.
- One section should translate the report into a decision framework for readers.
- Never create a section about unresolved questions, what the report failed to answer, research gaps, limitations, further reading, or community access. If the source explicitly states a limitation, mention it once inside the relevant analytical paragraph.
- End with the final substantive paragraph. Do not add a CTA, promotional invitation, website, community reference, summary, or rhetorical question.
- End with: `*For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.*`

Content boundaries:
- Do not mention specific investment bank names such as GS. Use "a global investment bank report" if needed.
- Do not use emoji.
- Do not write like a viral post.
- Open with the most specific fact, contrast, or tension in the source. Avoid generic openings such as "Against this backdrop", "In recent years", or "As the market evolves".
- Vary sentence and paragraph length naturally. Do not repeat stock transitions such as "This means", "In other words", or "What matters most".
- Do not invent a personal voice, interview, or first-hand experience. Editorial character must come from evidence selection and precise phrasing.
- Do not output your reasoning process.
- Do not generate image Markdown; the system will insert original MinerU images afterward.

Report parsing:
"""
## WAIC KTA: Determined but More Pragmatic; Data/Semi in Focus

China's AI policies focus on open-source models, export of AI/compute to EMs, and int'l collaboration on standards/governance. Semis set to be the key driver. We see super nodes connected by optical modules/NPO, and 3D DRAM stacking, as emerging solutions. China is aggressively catching up on data generation/labelling and agent harnessing/productization. Robotics still a big theme, but with a pragmatically lower focus on humanoids. Top picks: AMEC, SMIC, VNET.

China's AI strategies focus on developing a China-friendly EM ecosystem. President Xi's address at the 2026 WAIC (his first attendance) indicates China's key strategy is to export AI/ compute/green energy to EMs, which complements its One-Belt, One-Road program. Thus, Chinese AI players will likely have to maintain an open-source approach, which is less positive for monetization. Compute and, therefore, semi remain the key success factors in this strategy, implying a high likelihood of big foundry capex ahead. Given that China's Kimi 3 (by MoonShot) is now only $5\%$ behind Anthropic's Fable 5 in terms of intelligence (see here), China's open-source approach is very likely to put pricing pressure on US closed-source models, but will also make China's models affordable for other EMs. In our view, this strategy could "kill two birds with one stone." We believe the most likely US response is to 1) tighten export controls to prevent AI chips from being diverted to China, and 2) require all US AI players to put anti-distillation features in their advanced models.

Supernode connected by optics and stacking DRAM on GPUs seem a popular roadmap for China. Huawei launched Atlas 950 SuperPoD, a supernode design connecting 1,024 Ascend 950 GPUs (next gen will be 8,192) using LPO (2,048 lower-powered optical modules). It offers memory bandwidth of 107.52 TB/s and 2 EFLOPs of compute, vs 20.7 TB/s and 1.4 EFLOPs (FP4) for NVIDIA's Vera Rubin NVL72. But it consumes 7.4x more power (1.7MW) than Rubin NVL72. Hence, we like China's IDC players. Moreover, we have seen two Chinese GPU players adopt 3D DRAM tech, stacking 4 layers of DDR5 on top of their GPUs using hybrid bonding in response to the HBM constraints. They believe this will deliver 20+ TB/s of bandwidth, similar to HBM4. Stacking will be done by Chinese OSAT players, and the DDR5 by CXMT. But these players' GPUs are based on only 14nm. Therefore, such 100%-localized solutions focus more on memory bandwidth than compute, likely driven by agentic AI inference demand. We see foundry capacity (both logic and memory) as the biggest investment areas to support China's AI strategies. Hence, we like AMEC and SMIC.

China catching up on data generation and agent harness capabilities. The US has led in data collection for AI. However, data availability is now a big challenge as text data has been exhausted, and the remaining data is mostly proprietary at the enterprise level. For the world model, real-life 3D data is hard to collect for individual AI players. Following the "data as a factor of production" policy in 2022, the Bureau of Data was created in Oct 2023. This year, it will likely establish a central SOE to facilitate the collection, labeling, and trading of high-quality and reliable datasets across industries. China is also in a strong position, as the cost of hiring local professionals/experts to verify/contribute datasets remains competitive. Moreover, Chinese AI players have offered agentic products with strong harnessing in context mgmt, sub-agent orchestration, tool utilization, guardrails, managing feedback loops, etc. Harness is as important as model intelligence for delivering strong agent performance.

PIs see P2 for AI smartphone and robotics.

Edison Lee, CFA \* | Equity Analyst
852 3743 8009 | edison.lee@JEF.com

Matt Ma \* | Equity Analyst
852 3767 1109 | matt.ma@JEF.com

Nick Cheng \* | Equity Analyst
+852 3743 8750 | nick.cheng@JEF.com

Jacky He \* | Equity Analyst
+852 3743 8084 | jacky.he@JEF.com

Annie Ping, CFA, FRM \* | Equity Associate +852 3767 1273 | annie.ping@JEF.com

AI smartphone remains a big challenge. A Chinese AI player demonstrated a self-designed AI smartphone powered by the smartphone versions of its LLM (1bn-10bn data parameters) instead of a traditional OS (but the kernel is still Android) and made by an ODM. We believe OpenAI may want to do something similar. But we do not think the experience is differentiated enough (vs cloud-based services). The ecosystem could also be limited as major Internet players may block its APIs for security purposes, or to defend their own ecosystems. A lack of bargaining power in the hardware supply chain and high memory prices are additional challenges.

Robotics still a big theme with many players, but de-emphasizing humanoids is a realistic strategy. Robotics occupies \~25% of the WAIC's exhibition space, bigger than last year and thus still a very important AI theme for China. However, we saw a meaningful decline in the demo and exhibition of humanoids. The focus now is more on robots on wheels, which are lower-cost and easier to commercialize. We believe this means robotics players have become more pragmatic, suggesting lower risks for the sector. We have taken the view that humanoids are likely 5 years away, given challenges in compute (especially for China), memory (expensive), overheating, dexterous hands (miniaturization of power semi and motors), and reducers, etc. We believe robots on wheels are much less challenging to produce, competitive in terms of cost, and easier to commercialize.

## Company Valuation/Risks

Advanced Micro-Fabrication Eqp Inc China

Our PT of Rmb415.00 is based on 80x/58x 2026E/27E P/E. Key risks include 1) further sanction from US Department of Commerce, 2) slower-than-expected customer capacity expansion, 3) slower-than-expected new customer acquisition outside China, and 4) slower-than-expected new tool development.

## NVIDIA Corporation

Price Target: \$300 implies 21x our CY28E EPS of \$14.14.

## Risks:

• Emerging competitive threats from INTC, AMD, and internally designed ASICs from Hyperscalers take share and pressure ASPs.

\- Slowing datacenter capital spending from Enterprises and Hyperscalers.

\- Slower-than-expected ramp of Automotive platform.

## Semiconductor Manufacturing International Corporation

Our price target for the HK share is based on 4.0x 2026E P/B, and our price target for the A share is based on 7.0x 2026E P/B. Key risks include: 1) supply chain risk decelerating if the US continues to grant licenses to US SPE companies to supply SMIC with mature node equipment to deal with global chipset shortage, and 2) better--than-expected mature node demand driven by 5G, IOT, CIS, etc. resulting in further ASP increases.

## VNET Group

Our price target is based on SOTP. Risks to our price target include slower-than-expected demand growth, failure to obtain sufficient power allocation from the government, and lower-than-expected pricing due to more intense competition.

## Analyst Certification:

I, Edison Lee, CFA, certify that all of the views expressed in this research report accurately reflect my personal views about the subject security(ies) and subject company(ies). I also certify that no part of my compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed in this research report.

I, Matt Ma, certify that all of the views expressed in this research report accurately reflect my personal views about the subject security(ies) and subject company(ies). I also certify that no part of my compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed in this research report.

I, Nick Cheng, certify that all of the views expressed in this research report accurately reflect my personal views about the subject security(ies) and subject company(ies). I also certify that no part of my compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed in this research report.

I, Jacky He, certify that all of the views expressed in this research report accurately reflect my personal views about the subject security(ies) and subject company(ies). I also certify that no part of my compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed in this research report.

I, Annie Ping, CFA, FRM, certify that all of the views expressed in this research report accurately reflect my personal views about the subject security(ies) and subject company(ies). I also certify that no part of my compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed in this research report.

Registration of non-US analysts: Edison Lee, CFA is employed by JEF Hong Kong Limited, a non-US affiliate of JEF LLC and is not registered/qualified as a research analyst with FINRA. This analyst(s) may not be an associated person of JEF LLC, a FINRA member firm, and therefore may not be subject to the FINRA Rule 2241 and restrictions on communications with a subject company, public appearances and trading securities held by a research analyst.

Registration of non-US analysts: Matt Ma is employed by JEF Hong Kong Limited, a non-US affiliate of JEF LLC and is not registered/qualified as a research analyst with FINRA. This analyst(s) may not be an associated person of JEF LLC, a FINRA member firm, and therefore may not be subject to the FINRA Rule 2241 and restrictions on communications with a subject company, public appearances and trading securities held by a research analyst. Registration of non-US analysts: Nick Cheng is employed by JEF Hong Kong Limited, a non-US affiliate of JEF LLC and is not registered/qualified as a research analyst with FINRA. This analyst(s) may not be an associated person of JEF LLC, a FINRA member firm, and therefore may not be subject to the FINRA Rule 2241 and restrictions on communications with a subject company, public appearances and trading securities held by a research analyst. Registration of non-US analysts: Jacky He is employed by JEF Hong Kong Limited, a non-US affiliate of JEF LLC and is not registered/qualified as a research analyst with FINRA. This analyst(s) may not be an associated person of JEF LLC, a FINRA member firm, and therefore may not be subject to the FINRA Rule 2241 and restrictions on communications with a subject company, public appearances and trading securities held by a research analyst. Registration of non-US analysts: Annie Ping, CFA, FRM is employed by JEF Hong Kong Limited, a non-US affiliate of JEF LLC and is not registered/qualified as a research analyst with FINRA. This analyst(s) may not be an associated person of JEF LLC, a FINRA member firm, and therefore may not be subject to the FINRA Rule 2241 and restrictions on communications with a subject company, public appearances and trading securities held by a research analyst.

As is the case with all JEF employees, the analyst(s) responsible for the coverage of the financial instruments discussed in this report receives compensation based in part on the overall performance of the firm, including investment banking income. We seek to update our research as appropriate, but various regulations may prevent us from doing so. Aside from certain industry reports published on a periodic basis, the large majority of reports are published at irregular intervals as appropriate in the analyst's judgement.

## Investment Recommendation Record

(Article 3(1)e and Article 7 of MAR)

Recommendation Published

July 19, 2026 12:34 P.M.

Recommendation Distributed

July 19, 2026 12:34 P.M.

## Explanation of JEF Ratings

Buy - Describes securities that we expect to provide a total return (price appreciation plus yield) of 15% or more within a 12-month period.

Hold - Describes securities that we expect to provide a total return (price appreciation plus yield) of plus 15% or minus 10% within a 12-month period. Underperform - Describes securities that we expect to provide a total return (price appreciation plus yield) of minus 10% or less within a 12-month period. The expected total return (price appreciation plus yield) for Buy rated securities with an average security price consistently below \$10 is 20% or more within a 12-month period as these companies are typically more volatile than the overall stock market. For Hold rated securities with an average security price consistently below \$10, the expected total return (price appreciation plus yield) is plus or minus 20% within a 12-month period. For Underperform rated securities with an average security price consistently below \$10, the expected total return (price appreciation plus yield) is minus 20% or less within a 12-month period.

NR - The investment rating and price target have been temporarily suspended. Such suspensions are in compliance with applicable regulations and/or JEF policies.

CS - Coverage Suspended. JEF has suspended coverage of this company.

NC - Not covered. JEF does not cover this company.

Restricted - Describes issuers where, in conjunction with JEF engagement in certain transactions, company policy or applicable securities regulations prohibit certain types of communications, including investment recommendations.

Monitor - Describes securities whose company fundamentals and financials are being monitored, and for which no financial projections or opinions on the investment merits of the company are provided.

## Valuation Methodology

JEF' methodology for assigning ratings may include the following: market capitalization, maturity, growth/value, volatility and expected total return over the next 12 months. The price targets are based on several methodologies, which may include, but are not restricted to, analyses of market risk, growth rate, revenue stream, discounted cash flow (DCF), EBITDA, EPS, cash flow (CF), free cash flow (FCF), EV/EBITDA, P/E, PE/growth, P/CF, P/FCF, premium (discount)/average group EV/EBITDA, premium (discount)/average group P/E, sum of the parts, net asset value, dividend returns, and return on equity (ROE) over the next 12 months.

## JEF Franchise Picks

JEF Franchise Picks include stock selections from among the best stock ideas from our equity analysts over a 12 month period. Stock selection is based on fundamental analysis and may take into account other factors such as analyst conviction, differentiated analysis, a favorable risk/reward ratio and investment themes that JEF analysts are recommending. JEF Franchise Picks will include only Buy rated stocks and the number can vary depending on analyst recommendations for inclusion. Stocks will be added as new opportunities arise and removed when the reason for inclusion changes, the stock has met its desired return, if it is no longer rated Buy and/or if it triggers a stop loss. Stocks having 120 day volatility in the bottom quartile of S&P stocks will continue to have a 15% stop loss, and the remainder will have a 20% stop. Franchise Picks are not intended to represent a recommended portfolio of stocks and is not sector based, but we may note where we believe a Pick falls within an investment style such as growth or value.

## Risks which may impede the achievement of our Price Target

This report was prepared for general circulation and does not provide investment recommendations specific to individual investors. As such, the financial instruments discussed in this report may not be suitable for all investors and investors must make their own investment decisions based upon their specific investment objectives and financial situation utilizing their own financial advisors as they deem necessary. Past performance of the financial instruments recommended in this report should not be taken as an indication or guarantee of future results. The price, value of, and income from, any of the financial instruments mentioned in this report can rise as well as fall and may be affected by changes in economic, financial and political factors. If a financial instrument is denominated in a currency other than the investor's home currency, a change in exchange rates may adversely affect the price of, value of, or income derived from the financial instrument described in this report. To the extent prices are shown in non-US currency, please note that our local currency price targets are based on a currency conversion using an exchange rate as of the prior trading day (unless otherwise noted). Should there be fluctuations in the exchange rate after this date, that will affect the non-US target prices and should no longer be relied upon. In addition, investors in securities such as ADRs, whose values are affected by the currency of the underlying security, effectively assume currency risk.

## Other Companies Mentioned in This Report

• Advanced Micro-Fabrication Eqp Inc China (688012 CH: CNY350.69, BUY)

• NVIDIA Corporation (NVDA: \$202.81, BUY)

\- Semiconductor Manufacturing International Corporation (981 HK: HK\$67.70, BUY)

Rating and Price Target History for: Advanced Micro-Fabrication Eqp Inc China (688012 CH) as of 07-17-2026  
![](images/8dfd9ae300caa4ec90e0b563fea0accf325c46fbcfc6f84c5fd76357a0ab6c78.jpg)

Rating and Price Target History for: Semiconductor Manufacturing International Corporation (981 HK) as of 07-17-2026  
![](images/ca6f9c30e4cfc098cd9678b44564eae81bd01ca8c50857de575116b02902250a.jpg)

Rating and Price Target History for: NVIDIA Corporation (NVDA) as of 07-17-2026  
![](images/42015ad152b1c64cf45b098573bf14a60a18d475e15cecba690cc1396032772b.jpg)

![](images/888c138d1e122944cfe2c5fcc368e776439da11eff2af5ba4505e2eb2d9cee9d.jpg)

Notes: Each box in the Rating and Price Target History chart above represents actions over the past three years in which an analyst initiated on a company, made a change to a rating or price target of a company or discontinued coverage of a company.
Legend:

I: Initiating Coverage

D: Dropped Coverage

B: Buy

H: Hold

UP: Underperform

Distribution of Ratings  
IB Serv./Past12 Mos.

<table><tr><td></td><td>Count</td><td>Percent</td><td>Count</td><td>Percent</td><td>Count</td><td>Percent</td></tr><tr><td>BUY</td><td>2237</td><td>62.63%</td><td>387</td><td>17.30%</td><td>110</td><td>4.92%</td></tr><tr><td>HOLD</td><td>1173</td><td>32.84%</td><td>94</td><td>8.01%</td><td>15</td><td

[中间内容因长度限制已省略]

lar investment objectives, portfolio holdings, strategy, financial situation, or needs of any recipient. As such, any advice or recommendation in this report may not be suitable for a particular recipient. JEF assumes recipients of this report are capable of evaluating the information contained herein and of exercising independent judgment. A recipient of this report should not make any investment decision without first considering whether any advice or recommendation in this report is suitable for the recipient based on the recipient's particular circumstances and, if appropriate or otherwise needed, seeking professional advice, including tax advice. JEF does not perform any suitability or other analysis to check whether an investment decision made by the recipient based on this report is consistent with a recipient's investment objectives, portfolio holdings, strategy, financial situation, or needs.

By providing this report, neither JRS nor any other JEF entity accepts any authority, discretion, or control over the management of the recipient's assets. Any action taken by the recipient of this report, based on the information in the report, is at the recipient's sole judgment and risk. The recipient must perform his or her own independent review of any prospective investment. If the recipient uses the services of JEF LLC (or other affiliated broker-dealers), in connection with a purchase or sale of a security that is a subject of these materials, such broker-dealer may act as principal for its own accounts or as agent for another person. Only JRS is registered with the SEC as an investment adviser; and therefore neither JEF LLC nor any other JEF affiliate has any fiduciary duty in connection with distribution of these reports.

The price and value of the investments referred to herein and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

This report may contain forward looking statements that may be affected by inaccurate assumptions or by known or unknown risks, uncertainties, and other important factors. As a result, the actual results, events, performance or achievements of the financial product may be materially different from those expressed or implied in such statements.

This report has been prepared independently of any issuer of securities mentioned herein and not as agent of any issuer of securities. No Equity Research personnel have authority whatsoever to make any representations or warranty on behalf of the issuer(s). Any comments or statements made herein are those of the JEF entity producing this report and may differ from the views of other JEF entities.

This report may contain information obtained from third parties, including ratings from credit ratings agencies such as Standard & Poor's, and information derived from third-party or proprietary generative artificial intelligence (Gen AI) models. JEF does not guarantee the accuracy, completeness, timeliness or availability of this information, and is not responsible for any errors or omissions (negligent or otherwise), regardless of the cause, or for the results obtained from the use of such content. Neither JEF nor any third-party content providers, including providers of Gen AI models, give any express or implied warranties, including, but not limited to, any warranties of merchantability or fitness for a particular purpose or use. Neither JEF nor any third-party content provider shall be liable for any direct, indirect, incidental, exemplary, compensatory, punitive, special or consequential damages, costs, expenses, legal fees, or losses (including lost income or profits and opportunity costs) in connection with any use of their content, including ratings. Credit ratings are statements of opinions and are not statements of fact or recommendations to purchase, hold or sell securities. They do not address the suitability of securities or the suitability of securities for investment purposes, and should not be relied on as investment advice. Reproduction and distribution of third party content in any form is prohibited except with the prior written permission of the related third party.

JEF reports are disseminated and available electronically, and, in some cases, also in printed form. Electronic research is simultaneously made available to all clients. This report or any portion hereof may not be copied, reprinted, sold, or redistributed or disclosed by the recipient or any third party, by content scraping or extraction, automated processing, or any other form or means, without the prior written consent of JEF. Any unauthorized use is prohibited. Neither JEF nor any of its respective directors, officers or employees, is responsible for guaranteeing the financial success of any investment, or accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this report or its contents. Nothing herein shall be construed to waive any liability JEF has under applicable U.S. federal or state securities laws.

For Important Disclosure information relating to JRS, please see https://adviserinfo.sec.gov/IAPD/Content/Common/crd\_iapd\_Brochure.aspx?BRCHR\_VRSN\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://javatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.

© 2026 JEF
"""
