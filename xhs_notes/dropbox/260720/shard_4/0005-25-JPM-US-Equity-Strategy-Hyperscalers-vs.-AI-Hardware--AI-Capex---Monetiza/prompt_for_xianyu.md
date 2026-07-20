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
Momentum Crowding

# JPM

## US Equity Strategy

Hyperscalers vs. AI Hardware, AI Capex & Monetization, Momentum Unwind, 2Q Earnings

The AI cycle remains intact. The key theme this reporting season remains centered on the hyperscaler capex guide, but with a greater focus on more tangible evidence of monetization. This includes incremental use cases such as Meta's move to sell excess AI compute capacity. Additionally, the potential implications of the Anthropic Mythos development suggest that security concerns could accelerate the timeline for moving workloads onto cloud-based platforms across both the private and increasingly the public sector, creating another long-term tailwind for cloud providers, data centers, semiconductors, and enterprise software (see Frontier AI Escalates Security Costs). If these signals begin to surface in forward commentary, they could provide significant incremental support to hyperscaler earnings and FCF curves. Given this fundamental backdrop, improving valuation and current investor positioning, over the medium-term we see better risk-reward in the hyperscaler complex (i.e., AI Midstream) relative to other areas of Tech, along with select opportunities in Software such as cybersecurity, which has emerged as a major secular investment theme and one we re-emphasized during peak AI disruption fears earlier this year (see Report).

\- Another reason the hyperscaler capex guide continues to draw significant attention is its broad implications for the Momentum trade (i.e., Memory and the rest of AI Upstream). The momentum factor has been unwinding recently from extreme crowding levels. While positioning is still far from flushed, the setup appears tactically healthier heading into the reporting period. However, further out, volatility in the Momentum factor could persist as concerns remain around incoming and competing AI equity supply both domestically and internationally, the slope of the forward capex curve and the ability of debt markets to absorb this funding, as well as potential breakthrough efficiencies and broader questions around terminal profit margins tied to the balance between demand and supply across the AI infrastructure market.

The broader earnings setup during this reporting season remains constructive but concentrated, with 2Q26 earnings expected to rise +23% y/y led by Tech (Nvidia and Micron contributing \~37% of total), or +19% excl. Energy, while top line is expected to increase +12% y/y. All sectors are expected to deliver positive revenue growth, and all sectors except Healthcare are expected to post positive earnings growth. The core of the season will come over the next two weeks when \~52% of market cap reports, including the four major hyperscalers, while Nvidia and several other key semiconductor names will follow later with reports expected in mid-to-late August.

\- 2Q26 Hyperscaler capex numbers will once again serve as a pivotal validation point for the AI infrastructure build-out, as investors increasingly seek evidence that incremental ROIC can justify sustained, elevated spending levels. Consensus estimates now project AI-related capex to approach \~\$870B by year-end 2026 (\~+77% y/y), with hyperscalers to account for \~\$750 billion of that total. Our Internet analysts remain positive on the capex outlook for 2026 and have meaningfully revised up their 2027 projections. For next year, they forecast capex growth of +54% for GOOGL (\~\$300B), +42% for AMZN (\$300B), and +42% for META (\~\$200B). For more information, please see our analysts' notes here. This implies upside to

See page 9 for analyst certification and important disclosures.

## US Equity Strategy

Dubravko Lakos-Bujas AC
(1-212) 622-3601
dubravko.lakos-bujas@JPM.com

Bhupinder Singh AC
(1-212) 622-9812
bhupinder.singh@JPM.com

Ana Pous Avila
(1-212) 622-0496
ana.pousavila@JPM.com

William Matheson
(1-212) 622-9538
william.matheson@jpmchase.com
JPM Securities LLC

Relative Performance – Hyperscalers vs. Semiconductors & Nasdaq 100
Difference; Index = 100

![](images/196fced9595a8e79959f05c3c8e67e470934409d872576355f788b261f3161e1.jpg)  
Source: JPM Equity Strategy and Quantitative Research, Bloomberg Finance L.P.

![](images/42425f6d6e327da2564e3ed0f9949ba9035540c3e89d0081417f1f8ea2bdbdab.jpg)  
Source: JPM Equity Strategy and Quantitative Research, Bloomberg Finance L.P.

consensus capex estimates for the next 4-6 quarters. If these companies can justify the spend with higher earnings guidance as datacenters come online, there is a risk that the momentum factor could more rapidly rotate out of “AI Hardware” and back into Quality Growth / Hyperscalers (a similar Mag-7 / Mega-cap narrow leadership seen prior to the Momentum Crash in 1Q2025).

\- Hyperscaler fundamentals remain resilient despite growing capex-related pressure on free cash flow, which has increased reliance on debt and equity financing. Initially, these companies funded capex primarily through internally generated cash flow, but debt issuance has risen materially in recent years as AI datacenter investment has accelerated. Across the five largest hyperscalers, aggregate debt issuance has increased from \~\$40–50B in 2022 (largely to fund buybacks) to \~\$190B in 2026 (primarily to support datacenter buildout). This has contributed to growing investor concern around hyperscalers' ability to continue accessing debt markets at scale. However, our credit research team views these concerns as overstated, arguing that insurer concentration limits are not yet binding and that the high-grade market still has substantial capacity to absorb future issuance, although spreads may continue to adjust as supply expectations evolve (see AI Capex & Growing Pains). Funding sources are also beginning to broaden towards equity, with GOOGL raising \$85B in equity in June and recent reports indicating that META is evaluating similar alternatives. Importantly, the increase in external financing does not appear to reflect weakening operating fundamentals. Operating cash flow is still expected to exceed \$900B by 2027, while FactSet estimates imply average year-over-year sales growth of 17% through 2030 (vs. 15% avg last 5y) and net income margins remaining above trend at \~26% (vs. 20% avg last 5y) over the same period. In effect, the Street appears to be underwriting the AI datacenter monetization case: elevated capex today should ultimately translate into higher revenue, stronger margins, and expanding cash flow. Our base case is that hyperscalers will increasingly guide toward AI monetization, with FCF beginning to inflect higher as early as 2027. A broader and more durable recovery, however, may not emerge until 2028 or later, particularly if AI infrastructure investments require more time to translate into attractive ROIC.

\- Mark-to-market accounting of private investments could be an even larger swing factor in 2Q. The tailwind to 1Q26 earnings reflected non-cash revaluations of private-company stakes (i.e., Anthropic at Alphabet and Amazon) recorded under “Other Income” on company income statements. For Mag7 companies, this line increased from \~\$10B in 1Q25 to \~\$36B in 1Q26, and we estimated that roughly \~\$4 of the \~\$75 reported EPS figure in 1Q reflects these marks. However, considering most of the valuation re-rating in private AI companies occurred after the end of March, we expect the contribution from one-time gains to be larger in 2Q, reflecting the rise in private valuations during April and May. That said, the precise contribution is difficult to quantify given rapidly evolving private-market valuations and uncertainty around ownership stakes, which ultimately depend on several other factors. While these non-recurring gains (and losses) are typically excluded from both consensus and our estimates, major data providers seem to be including them, making the quality of upward EPS revisions harder to assess in coming quarters.

\- Strong earnings expected, but growth remains narrowly concentrated. 2Q26 earnings are expected to rise +23% y/y, or +19% excluding the Energy sector. This represents an improvement from +15% at the start of the year and +18% as of April 1st, implying upward revisions of +8% and +5%, respectively. Revenue is expected to increase +12% y/y. All sectors are expected to deliver positive revenue growth, while all sectors except Healthcare (-19% y/y) are expected to post positive earnings growth. Notably, the expected earnings contraction in Healthcare is largely driven by a handful of companies. Excluding Energy (+122% y/y), Tech (+64% y/y) is once again expected to lead earnings growth, with Nvidia and Micron alone expected to contribute \~37% of the total. Other companies that stand out in terms of earnings growth attribution include XOM ( $\sim7\%$ ), CVX ( $\sim6\%$ ), AVGO ( $\sim6\%$ ), and GOOGL ( $\sim6\%$ ).

AI Capex (LTM Actuals vs Estimates) \$ in billion  
![](images/8a9bfbdeac2e1053268ff44c6795f089067d274ff31979faeb205605a55226a6.jpg)  
Source: JPM Equity Strategy & Quantitative Research, Bloomberg Finance L.P., FactSet.

S&P Consensus Annual EPS  
![](images/b15afd213d372813ba39caecdc0f61d5569341a28cbe6d771d97369b84c9b091.jpg)  
Source: JPM Equity Strategy & Quantitative Research, Bloomberg Finance L.P., FactSet.

## Select Sector Previews:

\- AI capex supercycle remains the dominant theme heading into hyperscaler earnings, with a clear bias towards the upside. Across the group, the key swing factors are AI monetization and returns, where investors are looking for improved monetization across cloud, ads, and enterprise, in addition to token pricing dynamics, frontier model competition (Claude, GPT-5.5/5.6, Grok 4.5, Muse Spark 1.1, Gemini 3.5), and a more volatile macro backdrop where resilient spending could drive guidance upside even as softer consumer sentiment and renewed military activity could temper some 3Q outlooks. Key earnings dates: Alphabet Inc (7/22), Microsoft Corp (7/29), Meta Platforms Inc (7/29) & Amazon.com Inc (7/31).

\- The setup for semiconductors remains constructive, supported by strengthening AI demand and continued upward earnings revisions. The group is expected to deliver another solid quarter, with better 2Q26 results, constructive 3Q commentary, and higher CY27 expectations extending the recent positive earnings revision cadence. Strong results could help drive a rebound after the recent \~15% pullback, particularly as demand signals continue to strengthen, with hyperscalers and AI labs capacity-constrained, agentic-AI inference accelerating, and hyperscaler data center capex expectations moving higher. NVDA's Blackwell/Rubin framework and AVGO's path toward \$100B+ of AI revenue in FY27 have extended demand visibility into CY27+, shifting the debate from whether AI demand is real to whether supply chains and power availability can keep pace. Beyond accelerators, AI strength continues to broaden across custom silicon, memory, networking, semicaps, and EDA. Offsetting this, consumer/client markets are more mixed, with memory-driven (bill of materials) inflation pressuring smartphone and PC demand, though the broader industrial-led cyclical recovery remains on track. Overall, semis industry revenue is expected to grow 30%+ ex-memory this year, with preferred exposures concentrated in high-quality AI and cyclical recovery names. Key earnings dates: Nvidia Corp (8/26), Broadcom Inc (9/4) & Micron Technology Inc (9/23).

\- Energy is driving an outsized share of 2Q earnings growth expectations, led by Chevron and Exxon. Despite representing only \~4% of the S&P 500's market cap, consensus implies Energy contributes \~23% of the quarter's y/y earnings growth expectations, with 2Q sector earnings expected to increase roughly +122% y/y. That strength is largely attributed to higher oil prices following the Iran conflict, with growth expectations for the quarter beginning the year at +12%. Consistent with that setup, both Chevron and Exxon are positioned for a materially stronger quarter versus 1Q, reflecting higher upstream earnings leverage to commodity realizations and better operating performance, plus a downstream and refining rebound as margins normalize and prior headwinds ease. For Chevron, the focus is on improved production and operating rates and downstream returning to profitability. For Exxon, the key themes include the company's updated adjusted EPS framework to reduce derivative timing noise in addition to a broad-based sequential improvement across Upstream, Energy Products, and Chemicals. Key earnings dates: ExxonMobil Holdings (7/31) & Chevron Corp (7/31).

\- Healthcare stands out as the only sector expected to post negative earnings growth in 2Q, although the decline is attributable to a few companies. Earlier this year, we became more constructive on the higher-growth areas of the sector (see Report), where interest from generalist investors has been building. In particular, it is one of the key beneficiaries of AI adoption from both higher revenues (speeding the drug discovery process) and reducing overhead costs. Given that it is defensive and relatively under owned, the sector remains our favorite Low Vol sector. The group has rallied meaningfully over the past several weeks, particularly Biotech and Life Sciences, due to ongoing rotation out of Spec-Growth areas of the market. That said, going into the earnings season, the sector will become more name specific and dependent on whether 2Q earnings, guidance updates, or pipeline catalysts can sustain the recent momentum. Within Pharma, the 2Q setup looks constructive. Trends across the group remain positive, most companies are expected to beat and raise guidance, and our analysts do not expect management commentary to raise concerns that would prompt investors to rotate out of the sector. Life Science Tools have also seen sentiment improve despite guidance ranges that generally do not assume a material end market recovery, with recent outperformance potentially holding into 2Q earnings given less likelihood of policy disruption and positivity around demand trends showing signs of improvement that could support some upside this year and a more constructive fundamental view into 2027. Key earnings dates: LLY (8/5), ABBV (7/31) & MRK (8/4).

\- Aerospace & Defense enters earnings with stronger fundamental momentum in commercial aerospace, but a more favorable tactical setup in defense after recent underperformance. Commercial aerospace regained some momentum as Middle East risk concerns started to fade and investor focus returned to production recovery, aftermarket strength, and improving supply chain execution, while defense has lagged as capital rotated into higher growth stocks, budget and midterm uncertainty increased, contract activity remained uneven, and investors weighed potential limits on capital returns. This leaves a higher earnings bar for commercial aerospace and a lower one for defense. In the near term, that setup could allow Defense to outperform on solid earnings or positive contract news, though any squeeze would likely reflect lighter positioning and lower valuations rather than a fundamental change in the outlook. Commercial aerospace still has the stronger underlying story, supported by visible demand, production normalization, and aftermarket growth, but upside may be more selective after the recent rebound. Keep in mind Defense sentiment is unlikely to turn decisively without more clarity on appropriations, the FY27 budget path, and cash deployment flexibility, yet the longer-term backdrop remains constructive given persistent geopolitical tensions and global demand for weapons and defense capabilities.

## Earnings Scorecard:

\- Beats/Misses. With only 6% of S&P 500 companies having reported, 

[中间内容因长度限制已省略]

f market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
