你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `建议价格：` 一行，给一个资料类商品常见价格区间，例如 `8-20 元`，不要承诺成交价。
3. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
4. `搜索关键词：` 一行，给 8-15 个关键词，用空格分隔。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  ✅ 三大情景框架：DCF、P/ARR、EV/Sales
  ✅ 关键变量分析
  ✅ 估值逻辑、假设、终值占比等核心内容覆盖
  ✅ 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要写“原版/内部/独家/无水印/全网最低”等容易违规或夸张的词。
- 不要承诺投资收益。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

【研报解析内容】
"""
# The Great Broadband Bake Off

# U.S. Cable & Telecom Results & Reflections

- 1Q26 earnings across the Telecom & Cable sectors told a familiar but increasingly divergent story. The wireless carriers continued to execute well, with healthy sUBScriber trends, improving churn, and convergence strategies gaining traction, even as balance sheets remain in transition following a wave of acquisitions and elevated network investment. Cable operators, by contrast, continued to lose broadband sUBScribers at an uncomfortable pace, with top-of-funnel pressures showing few signs of structural relief.   
- Against this backdrop, we maintain a preference for Telecom over Cable. The wireless carriers offer more predictable cash flow profiles, credible delevering roadmaps, and demand tailwinds tied to mobility and fiber that we view as more durable than the pricing and bundling levers Cable is increasingly relying on to stabilize results.   
- Within Telecom, we continue to rate all three of the major carriers at Neutral. Fundamentals are generally moving in the right direction across AT&T, Verizon, and T-Mobile, but spreads across the group have compressed to the point where differentiation is limited and the risk-reward for adding exposure looks less compelling than it once did.   
- Charter is the one name in Cable where we see near-term value, though our Overweight rating on the IG Secured notes is a relative value call rather than a view that the fundamental picture has improved. The pending Cox acquisition adds footprint and synergy potential, and a more conservative capital allocation posture during integration should provide some near-term credit support.   
- Comcast screens as a more difficult name to own at current levels. Despite its higher ratings, spreads already reflect a best-case stabilization scenario that the underlying financials have not yet validated, and the company faces simultaneous pressures across broadband, streaming investment, and sports rights costs that limit near-term earnings visibility.   
- Longer-term, Cable sector consolidation remains an open question. This quarter, T-Mobile closed the door on any Cable transaction, at least for now, and the more plausible endgame in our view involves Comcast eventually separating its Media and Connectivity assets and combining the latter with Charter, though regulatory and leverage hurdles make that a multi-year rather than near-term conversation in our view.

Table 1: U.S. Cable & Telecom Comps 

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Issuer</td><td colspan="2">Reported Leverage</td><td rowspan="2">EV$ mns</td><td colspan="3">Ratings</td><td colspan="3">G-Spread (mid)</td></tr><tr><td>Gross</td><td>Net</td><td>Moody&#x27;s</td><td>S&amp;P</td><td>Fitch</td><td>5yr</td><td>10yr</td><td>30yr</td></tr><tr><td>CHTR</td><td>Charter Communications Inc</td><td>4.2x</td><td>4.2x</td><td>114,638</td><td>Ba1</td><td>BBB-</td><td>BBB- *+</td><td>97</td><td>181</td><td>221</td></tr><tr><td>CMCSA</td><td>Comcast Corp</td><td>2.6x</td><td>2.4x</td><td>174,876</td><td>A3</td><td>A-</td><td>A-</td><td>68</td><td>72</td><td>119</td></tr><tr><td>COXENT</td><td>Cox Communications Inc</td><td>5.0x</td><td>5.0x</td><td>N/A</td><td>Baa2 *-</td><td>BBB *-</td><td>BBB+ *-</td><td>112</td><td>173</td><td>203</td></tr><tr><td>TMUS</td><td>T-Mobile US Inc</td><td>2.5x</td><td>2.4x</td><td>324,517</td><td>Baa1</td><td>BBB+</td><td>BBB+</td><td>73</td><td>82</td><td>109</td></tr><tr><td>T</td><td>AT&amp;T Inc</td><td>3.0x</td><td>2.7x</td><td>335,353</td><td>Baa2</td><td>BBB</td><td>BBB+ *-</td><td>59</td><td>89</td><td>123</td></tr><tr><td>VZ</td><td>Verizon Communications Inc</td><td>3.4x</td><td>3.2x</td><td>385,550</td><td>Baa1</td><td>BBB+</td><td>A-</td><td>58</td><td>92</td><td>112</td></tr></table>

Source: Company reports & Bloomberg Finance L.P.

North American Corporate Credit – Tech, Media, & Telecom (IG)

Erica R Spear AC

(1-212) 834-4143

erica.spear@jpmchase.com

JPM Securities LLC

Table 2: IG Cable & Telco Ratings 

<table><tr><td>T</td><td>AT&amp;T</td><td>N</td></tr><tr><td>CHTR</td><td>Charter Communications (IG)</td><td>OW</td></tr><tr><td>CMCSA</td><td>Comcast</td><td>UW</td></tr><tr><td>TMUS</td><td>T-Mobile US Inc.</td><td>N</td></tr><tr><td>VZ</td><td>Verizon Communications</td><td>N</td></tr></table>

Source: JPM.

# Sector & Relative Value Views

1Q results across U.S. Telecom were mostly constructive, with operators delivering steady wireless performance, improving customer metrics, and stable to slightly better cash generation, even as elevated capex and near-term leverage remain part of the story. Management commentary across the group pointed to continued strength in mobility, disciplined promotions, and growing benefits from convergence strategies that are supporting churn and ARPU stability and long-term customer value, alongside clearer visibility into de-levering paths despite ongoing investment and selective M&A. In contrast, Cable results were more mixed to weaker, with broadband sUBScriber trends continuing to deteriorate amid intense competition from fixed wireless and fiber, and a still-muted housing backdrop weighing on gross additions. While underlying churn and ARPU dynamics remain relatively stable and wireless bundling is providing some offset, near-term EBITDA and growth visibility remains pressured by pricing actions, promotional intensity, and ongoing investment, leaving the sector more reliant on execution and future stabilization to support the credit story.

As such, we continue to prefer U.S. Telecom over Cable as the sector offers a more stable and visible credit trajectory supported by resilient wireless fundamentals, clearer paths to de-levering, and improving convergence-driven economics, while Cable faces more structural and execution-driven headwinds that limit confidence in forward cash flow durability. Across the Telecom cohort, operators are demonstrating steady service revenue growth, improving churn, and tangible benefits from bundling wireless with fiber and fixed wireless, which is supporting lifetime customer value and driving a more predictable FCF profile alongside defined leverage targets and disciplined capital allocation frameworks. Cable operators continue to face persistent broadband sUBScriber losses driven by fixed wireless sUBStitution, fiber overbuild, and a muted housing backdrop, with growth increasingly reliant on pricing and bundling strategies that pressure ARPU and near-term EBITDA. At the same time, Cable balance sheets remain more levered and more sensitive to execution, particularly as capital allocation remains skewed toward shareholder returns, raising the risk of slower de-levering in a declining or uncertain top-line environment. While select near-term catalysts such as M&A synergies and capex normalization may support FCF, we view these as less durable than the structural demand tailwinds in Telecom tied to mobility, fiber expansion, and convergence, leading us to favor Telecom as offering a more balanced risk-reward with stronger visibility.

At a high level, our ratings across AT&T, Verizon, and T-Mobile reflect that more constructive view on the Telecom sector's underlying credit stability, though tempered by valuations that largely capture improving fundamentals, while our stance on Charter and Comcast reflects a more cautious view on Cable given weaker growth visibility and greater execution risk. Within Telecom, we remain Neutral on the Big Three as steady wireless performance, convergence benefits, and defined de-levering paths support the credit story, but spreads across the group have traded broadly flat and leave limited room for meaningful outperformance without a clearer inflection in leverage or growth. On Cable, our views diverge based on valuation and structure, with a more constructive stance on Charter's secured debt driven by relative value and near-term catalysts, despite structural headwinds, while Comcast remains an Underweight given tight spreads relative to both Cable and Telecom peers alongside ongoing transition risk in its operating model.

The steady decline of the Cable sector over the past \~five years has led many to speculate about the future of the industry and the potential pathways toward consolidation. The early phases have already begun, as demonstrated by Charter's pending acquisition of Cox, though the belief has been that there will eventually be more significant consolidation among the bigger players. T-Mobile acquiring Charter is one idea that has been pushed for years, though this quarter T-Mobile definitively stated that it has no interest in acquiring any Cable assets, noting that it will not pursue scale for the sake of scale. In our view, a more likely answer is that Comcast will eventually split its Cable and Media assets and combine its Cable business with Charter's. On the merits, a combined Comcast/Charter entity would create a true national broadband incumbent, consolidating overlapping capex programs, eliminating duplicate network investments, and generating meaningful scale efficiencies across programming, wireless, and equipment procurement. The structure would likely mirror what Comcast has already telegraphed comfort with through Versant, spinning the NBCU media assets into a separately traded entity and leaving a pure-play connectivity business. In fact, Comcast recently explored an alternative version of this strategy when it participated in the bidding process for the WBD streaming and studio assets, and it is our belief that Comcast would need to have at least one transaction lined up for either side of the business in order to justify a split. The challenge is where to begin with regulatory hurdles, as a combined Comcast/Charter entity would serve a majority of the U.S. broadband footprint, and while the two systems are largely non-overlapping geographically, antitrust scrutiny in a broadband-consolidation context would likely be intense regardless of administration. Leverage is a secondary but real constraint, with Charter already carrying elevated leverage, a transaction of this scale would likely require either a stock-heavy structure or meaningful asset sales. Recent commentary from Charter has suggested that the firm is willing to explore all potential consolidation opportunities, and Comcast's management team has signaled a similar willingness, though they did say that the firm is focused on itself for now. While we do not necessarily expect this to be a near-term priority, we do expect Cable consolidation chatter to get even louder as we near the end of the decade.

Figure 1: Telecommunications & Media Benchmark 10s30s G-Spreads   
![](images/f7dd90ea363f0f34eda9d7ad599401a38bb6e6c21896d3c82b51bedce84d2f31.jpg)

<details>
<summary>bar_stacked</summary>

| Category | Value 1 | Value 2 |
| :--- | :--- | :--- |
| CHTR | 180 | 1255 |
| COXENT | 173 | 954 |
| RCICN | 106 | 52 |
| TCN | 101 | 49 |
| FOXA | 100 | 49 |
| OCI | 99 | 51 |
| EQIX | 92 | 52 |
| BCECN | 106 | 54 |
| T | 117 | 56 |
| META | 134 | 56 |
| ORAFP | 87 | 36 |
| VZ | 104 | 54 |
| AMT | 83 | 51 |
| TMUS | 107 | 56 |
| CMCSA | 119 | 55 |
| VOD | 108 | 54 |
| DIS | 73 | 51 |
| NFLX | 66 | 54 |
| QBRCN | 126 | 35 |
| TTWO | 112 | 34 |
| OMC | 105 | 34 |
| NBNAUS | 71 | 33 |
| WMG | 63 | 31 |
| SESGFP | 287 | 43 |
| CLNXSM | 138 | 41 |
| TELEFO | 129 | 49 |
| BRITEL | 95 | 49 |
| DT | 94 | 50 |
</details>

Spreads as of 11 May 2026. Cash prices adjusted by 0.17bp per cash point.   
Source: JPM & Bloomberg Finance L.P.

Figure 2: U.S. Telco & Cable G-Spread Curves   
![](images/fac28110e719761fd1b5e9a59962692bed8b71cffccdf21ae8e2b23db2345842.jpg)

<details>
<summary>scatter</summary>

| Date    | CHTR | CMCSA | COXENT | T   | TMUS | VZ  |
|---------|------|-------|--------|-----|------|-----|
| Nov-27  | 85   | 35    | 145    | 40  | 50   | 30  |
| May-33  | 185  | 60    | 175    | 70  | 75   | 60  |
| Oct-38  | 230  | 110   | 240    | 100 | 100  | 90  |
| Apr-44  | 235  | 125   | 225    | 110 | 110  | 100 |
| Oct-49  | 225  | 130   | 210    | 120 | 115  | 110 |
| Mar-55  | 240  | 135   | 205    | 125 | 115  | 105 |
| Sep-60  | 230  | 130   | -      | 120 | 110  | 55  |
| Mar-66  | -    | -     | -      | -   | -    | 115 |
</details>

Spreads as of 11 May 2026. Cash prices adjusted by 0.17bp per cash point.   
Source: JPM & Bloomberg Finance L.P.

# AT&T

- AT&T posted strong 1Q results, with modest upside versus estimates for key headline metrics, while reaffirming prior FY26 guidance and signaling improving momentum throughout the balance of the year. Results reflected continued resilience in wireless, steady fiber execution, and early benefits from pricing and cost actions, offset by still-elevated investment levels tied to network expansion. Management maintained a constructive tone on convergence, broadband growth, and balance sheet repair, though leverage is set to rise near-term as strategic transactions close.   
- We remain Neutral on AT&T as current spreads already reflect improving execution, including steady wireless net adds, fiber growth, cost actions, and solid FCF generation. While management has outlined a credible de-levering path, leverage remains higher than that of Verizon or T-Mobile, with Lumen and EchoStar funding needs likely to keep issuance elevated and balance sheet progress gradual. With spreads essentially flat to Verizon and T-Mobile for months now, we see limited room for meaningful outperformance absent a clearer leverage inflection. Within the group, AT&T's long end offers the best relative value, though still not enough to drive a more constructive stance. Risks to our rating include faster-than-expected de-levering or spread widening that creates relative value upside, or, conversely, heavier-than-expected spectrum acquisition and issuance, or weaker competitive trends.   
- Financials. Headline results broadly exceeded Street estimates, with revenue (\$31.51bn vs. \$31.25bn), adj. EBITDA (\$11.98bn vs. \$11.79bn), and EPS (\$0.54/share vs. \$0.55/share) outperforming. Capex of \$4.88bn (vs. \$5.08bn) came in below consensus, supporting FCF of \$2.51bn (vs. \$2.43bn). However, FCF still fell \$600mn y/y due to higher capex from accelerated fiber deployment. Under the new reporting structure, Advanced Connectivity generated over 90% of revenue and EBITDA, while Advanced Home Internet grew 27% y/y.   
- Guidance. Management reaffirmed prior FY26 guidance and expressed confidence in a stronger cadence through the year, driven by improving service revenue and EBITDA trends as pricing actions flow through, convergence scales, and cost initiatives advance. The company continues to expect low-single-digit service revenue growth and 3-4% adj. EBITDA growth, with EBITDA growth improving in 2Q as comparisons normalize and incremental cost actions are implemented. On cash generation, the firm guided to \$4.0-4.5bn of 2Q FCF and reiterated \$18bn+ for the year.   
- Capital Allocation & Balance Sheet. AT&T ended 1Q with \$138bn of long-term debt and \$12bn of cash. Net leverage rose to 2.7x from 2.5x at 4Q and is expected to increase to \~3.2x after the EchoStar transaction, before declining to \~3.0x by YE26 and returning to the 2.5x target over the next three years. The firm also expects to close a minority stake sale of its Lumen fiber assets in 2H. Management emphasized continued network investment in fiber and 5G alongside shareholder returns and a defined leverage path. The firm repurchased \$2.3bn shares and paid \~\$2bn of dividends in 1Q, reiterated its \$8bn buyback plan for this year, and signaled a steady pace through 2028 as part of its \$45bn return target. Following results, AT&T issued \$6bn of senior notes, bringing YTD issuance to \

[中间内容因长度限制已省略]

t performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its sUBSidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised April 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 11 May 2026 11:54 PM EDT

Disseminated 12 May 2026 06:45 AM EDT
"""
