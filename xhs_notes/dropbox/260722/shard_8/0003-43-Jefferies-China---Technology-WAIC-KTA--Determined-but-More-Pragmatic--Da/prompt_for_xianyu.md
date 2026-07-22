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

This report was prepared for general circulation and does not provide investment recommendations specific to individual investors. As such, the financial instruments discussed in this report may not be suitable for all investors and investors must make their own investment decisions based upon their specific investment objectives and financial situation utilizing their own financial adviso

[中间内容因长度限制已省略]

the recipient based on this report is consistent with a recipient's investment objectives, portfolio holdings, strategy, financial situation, or needs.

By providing this report, neither JRS nor any other JEF entity accepts any authority, discretion, or control over the management of the recipient's assets. Any action taken by the recipient of this report, based on the information in the report, is at the recipient's sole judgment and risk. The recipient must perform his or her own independent review of any prospective investment. If the recipient uses the services of JEF LLC (or other affiliated broker-dealers), in connection with a purchase or sale of a security that is a subject of these materials, such broker-dealer may act as principal for its own accounts or as agent for another person. Only JRS is registered with the SEC as an investment adviser; and therefore neither JEF LLC nor any other JEF affiliate has any fiduciary duty in connection with distribution of these reports.

The price and value of the investments referred to herein and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

This report may contain forward looking statements that may be affected by inaccurate assumptions or by known or unknown risks, uncertainties, and other important factors. As a result, the actual results, events, performance or achievements of the financial product may be materially different from those expressed or implied in such statements.

This report has been prepared independently of any issuer of securities mentioned herein and not as agent of any issuer of securities. No Equity Research personnel have authority whatsoever to make any representations or warranty on behalf of the issuer(s). Any comments or statements made herein are those of the JEF entity producing this report and may differ from the views of other JEF entities.

This report may contain information obtained from third parties, including ratings from credit ratings agencies such as Standard & Poor's, and information derived from third-party or proprietary generative artificial intelligence (Gen AI) models. JEF does not guarantee the accuracy, completeness, timeliness or availability of this information, and is not responsible for any errors or omissions (negligent or otherwise), regardless of the cause, or for the results obtained from the use of such content. Neither JEF nor any third-party content providers, including providers of Gen AI models, give any express or implied warranties, including, but not limited to, any warranties of merchantability or fitness for a particular purpose or use. Neither JEF nor any third-party content provider shall be liable for any direct, indirect, incidental, exemplary, compensatory, punitive, special or consequential damages, costs, expenses, legal fees, or losses (including lost income or profits and opportunity costs) in connection with any use of their content, including ratings. Credit ratings are statements of opinions and are not statements of fact or recommendations to purchase, hold or sell securities. They do not address the suitability of securities or the suitability of securities for investment purposes, and should not be relied on as investment advice. Reproduction and distribution of third party content in any form is prohibited except with the prior written permission of the related third party.

JEF reports are disseminated and available electronically, and, in some cases, also in printed form. Electronic research is simultaneously made available to all clients. This report or any portion hereof may not be copied, reprinted, sold, or redistributed or disclosed by the recipient or any third party, by content scraping or extraction, automated processing, or any other form or means, without the prior written consent of JEF. Any unauthorized use is prohibited. Neither JEF nor any of its respective directors, officers or employees, is responsible for guaranteeing the financial success of any investment, or accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this report or its contents. Nothing herein shall be construed to waive any liability JEF has under applicable U.S. federal or state securities laws.

For Important Disclosure information relating to JRS, please see https://adviserinfo.sec.gov/IAPD/Content/Common/crd\_iapd\_Brochure.aspx?BRCHR\_VRSN\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://javatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.

© 2026 JEF
"""
