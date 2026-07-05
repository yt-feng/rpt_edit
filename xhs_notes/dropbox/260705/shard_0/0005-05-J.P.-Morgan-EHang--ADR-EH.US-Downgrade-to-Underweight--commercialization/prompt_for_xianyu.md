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
# JPM

## EHang - ADR

## Downgrade to Underweight; commercialization delayed, first-mover advantage diminished

Certification is no longer enough. We downgrade EHang to Underweight from Neutral and cut our PT to US\$4.4 (from US\$9.7) as we believe China's passenger eVTOL commercialization has entered a structural reset. Our original thesis assumed EHang's certification lead would rapidly convert into commercialization, generating operating cash flow to fund future aircraft while competitors remained in certification. Instead, regulators have continued moving the commercialization goalposts since 2H25, while the recent nationwide suspension of most general aviation activities following the Beijing aviation accident (26 June) further delays passenger deployment. We cut our FY26E/27E/28E revenue forecasts to Rmb261mn/Rmb290mn/Rmb319mn (55%/66%/75% below consensus), forecast non-GAAP net losses of Rmb407mn/Rmb176mn/Rmb89mn (also below consensus), and lower our valuation multiple to 7.7x FY27E P/S, reverting to 4Q23/1Q24 levels as the commercialization premium unwinds. Despite the stock declining 52% YTD, versus western eVTOL peers (-30%) and the Nasdaq (+11%), we believe the market continues to price EHang as a commercialization story when it has effectively reverted to a certification story.

\- Commercialization has become a moving regulatory target. Our original thesis assumed TC, PC, AC and the first OCs represented the final regulatory hurdles before passenger commercialization. Instead, every major milestone has been followed by new commercialization requirements. Following the first OCs, regulators introduced operator training frameworks, licensing standards and standardized operating procedures before broader deployment. Shortly thereafter, CAAC requested onboard obstacle detection and detect-and-avoid capability before approving public ticketed operations. The recent nationwide suspension of most general aviation activities following the Beijing aviation accident further reinforces our view that passenger eVTOL commercialization will progress materially slower than previously expected.

\- We cut estimates materially and expect management to lower FY26 guidance. We expect 2Q26 revenue of Rmb113mn (flat YoY, +340% QoQ), supported by deferred revenue recognition from 4Q25 and stronger non-passenger businesses, but forecast a wider non-GAAP net loss of Rmb124mn (vs. Rmb12mn in 2Q25 and Rmb75mn in 1Q26). We expect a much sharper slowdown during 2H26 as customers increasingly defer deliveries while commercialization remains uncertain. Our revised forecasts imply FY26E/27E/28E revenue 55%/66%/75% below consensus, and we believe management is likely to revise its Rmb600mn FY26 revenue target lower.

\- What could change our view? We would become more constructive if commercialization becomes predictable rather than progressively delayed. Specifically, we would look for a stable regulatory framework without further material commercialization requirements, approval of additional operators and cities under a repeatable operating framework, accelerating passenger aircraft deliveries driven by commercial demand rather than demonstration projects, and evidence that commercial operations are generating sufficient operating cash flow to support internally funded development of future aircraft generations.

Sources for: Style Exposure – JPM Global Markets Strategy; all other tables are company data and JPM estimates.

## ▼ Underweight

See page 11 for analyst certification and important disclosures, including non-US analyst disclosures.

Previous: Neutral

EH, EH US
Price (02 Jul 26):\$6.31

▼ Price Target (Dec-27):\$4.40
Prior (Mar-27):\$9.70

Infrastructure, Industrials & Transport

Beatrice Lam AC
(852) 2800-8738
beatrice.lam@JPM.com

Karen Li, CFA
(852) 2800-8589
karen.yy.li@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

## Key Changes (FYE Dec)

<table><tr><td></td><td>Prev</td><td>Cur</td><td> $\Delta$ </td></tr><tr><td>Adj. EPS - 26E (Rmb)</td><td>(1.31)</td><td colspan="2">(5.55)-321.8%</td></tr><tr><td>Adj. EPS - 27E (Rmb)</td><td>0.31</td><td colspan="2">(2.40)-870.4%</td></tr></table>

## Style Exposure

<table><tr><td rowspan="2">Quant Factors</td><td rowspan="2">Current %Rank</td><td colspan="4">Hist %Rank (1=Top)</td></tr><tr><td>6M</td><td>1Y</td><td>3Y</td><td>5Y</td></tr><tr><td>Value</td><td>95</td><td>97</td><td>99</td><td>99</td><td>98</td></tr><tr><td>Growth</td><td>83</td><td>72</td><td>64</td><td>10</td><td>6</td></tr><tr><td>Momentum</td><td>99</td><td>15</td><td>97</td><td>8</td><td>8</td></tr><tr><td>Quality</td><td>98</td><td>99</td><td>98</td><td>99</td><td>95</td></tr><tr><td>Low Vol</td><td>81</td><td>90</td><td>94</td><td>100</td><td>100</td></tr></table>

Price Performance  
![](images/870df558515762cbc2f002cb3cde749ed64387850087974fc57381808417ece4.jpg)

— EH Price (\$) — RTY (rebased)

<table><tr><td></td><td>YTD</td><td>1m</td><td>3m</td><td>12m</td></tr><tr><td>Abs</td><td>-52.1%</td><td>-38.3%</td><td>-39.1%</td><td>-62.8%</td></tr><tr><td>Rel</td><td>-72.8%</td><td>-40.4%</td><td>-57.5%</td><td>-97.3%</td></tr></table>

Company Data

<table><tr><td>Shares O/S (mn)</td><td>67</td></tr><tr><td>52-week range ($)</td><td>20.45-5.97</td></tr><tr><td>Market cap ($ mn)</td><td>424</td></tr><tr><td>Market cap ($ mn)</td><td>424</td></tr><tr><td>Exchange rate</td><td>1.00</td></tr><tr><td>Free float (%)</td><td>-</td></tr><tr><td>3M ADV (mn)</td><td>0.94</td></tr><tr><td>3M ADV ($ mn)</td><td>8.1</td></tr><tr><td>Volatility (90 Day)</td><td>81</td></tr><tr><td>Index</td><td>RUSSELL 2000</td></tr><tr><td>BBG ANR (Buy | Hold | Sell)</td><td>15|2|0</td></tr></table>

Key Metrics (FYE Dec)

<table><tr><td>Rmb in millions</td><td>FY25A</td><td>FY26E</td><td>FY27E</td><td>FY28E</td></tr><tr><td colspan="5">Financial Estimates</td></tr><tr><td>Revenue</td><td>418</td><td>261</td><td>290</td><td>319</td></tr><tr><td>Adj. EBITDAR</td><td>(41)</td><td>(389)</td><td>(144)</td><td>(47)</td></tr><tr><td>Adj. EBIT</td><td>(71)</td><td>(431)</td><td>(191)</td><td>(100)</td></tr><tr><td>Adj. net income</td><td>(30)</td><td>(407)</td><td>(176)</td><td>(89)</td></tr><tr><td>Adj. EPS</td><td>(0.41)</td><td>(5.55)</td><td>(2.40)</td><td>(1.22)</td></tr><tr><td>BBG EPS</td><td>1.40</td><td>(0.99)</td><td>0.71</td><td>2.33</td></tr><tr><td>Cashflow from operations</td><td>(180)</td><td>101</td><td>99</td><td>23</td></tr><tr><td>FCFF</td><td>(367)</td><td>(227)</td><td>(132)</td><td>87</td></tr><tr><td colspan="5">Margins and Growth</td></tr><tr><td>Revenue Growth Y/Y (%)</td><td>(8.4%)</td><td>(37.5%)</td><td>11.0%</td><td>9.9%</td></tr><tr><td>EBITDAR margin</td><td>(9.7%)</td><td>(149.0%)</td><td>(49.6%)</td><td>(14.8%)</td></tr><tr><td>EBITDAR growth</td><td>(204.4%)</td><td>859.9%</td><td>(63.1%)</td><td>(67.2%)</td></tr><tr><td>EBIT margin</td><td>(16.9%)</td><td>(165.1%)</td><td>(66.0%)</td><td>(31.5%)</td></tr><tr><td>Net margin</td><td>(7.1%)</td><td>(155.7%)</td><td>(60.6%)</td><td>(28.1%)</td></tr><tr><td>Adj. EPS growth</td><td>(163.0%)</td><td>1264.1%</td><td>(56.8%)</td><td>(49.1%)</td></tr><tr><td colspan="5">Ratios</td></tr><tr><td>Adj. tax rate</td><td>(15.0%)</td><td>(0.3%)</td><td>(0.3%)</td><td>(0.3%)</td></tr><tr><td>Interest cover</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>Net debt/Equity</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>Net debt/EBITDA</td><td>4.0</td><td>0.2</td><td>0.8</td><td>0.2</td></tr><tr><td>ROCE</td><td>(7.6%)</td><td>(44.5%)</td><td>(27.7%)</td><td>(18.0%)</td></tr><tr><td>ROE</td><td>(2.9%)</td><td>(47.0%)</td><td>(30.7%)</td><td>(20.3%)</td></tr><tr><td colspan="5">Valuation</td></tr><tr><td>FCFF yield</td><td>(11.7%)</td><td>(7.2%)</td><td>(4.2%)</td><td>2.8%</td></tr><tr><td>Dividend yield</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>EV/EBITDAR</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>EV/Revenue</td><td>6.5</td><td>10.7</td><td>9.5</td><td>9.0</td></tr><tr><td>Adj. P/E</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr></table>

## Summary Investment Thesis and Valuation

## Investment Thesis

We are Underweight on EHang. We continue to believe China will become one of the world's largest long-term passenger eVTOL markets and that EHang retains a meaningful first-mover advantage through its TC, PC, AC and the first Operating Certificates (OCs). However, we believe the investment case has fundamentally changed. Rather than transitioning from certification into commercialization, regulators have continued introducing additional operational requirements after major certification milestones, while the recent nationwide suspension of most general aviation activities further reduces visibility on commercialization timing. We now expect passenger commercialization to progress materially slower than previously anticipated, delaying operating cash flow, extending cash burn and reducing the economic value of EHang's certification lead. While overseas markets and non-passenger businesses remain long-term opportunities, we do not expect either to offset weaker domestic passenger commercialization over our forecast horizon.

## Valuation

Our Dec-27 price target of US\$4.4 is based on a 7.7x FY27E P/S multiple, equivalent to one standard deviation below EHang's average forward P/S multiple since 2023. We believe the commercialization premium that emerged following the first OCs has largely unwound as commercialization becomes increasingly dependent on evolving regulatory requirements rather than certification alone. We therefore value EHang closer to its historical certification-stage valuation framework until commercialization becomes more predictable.

Performance Drivers  
![](images/2f92f579f509fa951fc28dec50a424d6b73a52e8f0dc87b18fd9960aed92762a.jpg)

<table><tr><td>Factors</td><td>6M Corr</td><td>1Y Corr</td></tr><tr><td>Market: MSCI Asia Pac ex JP</td><td>0.36</td><td>0.43</td></tr><tr><td>Region: Hong Kong</td><td>-0.23</td><td>-0.20</td></tr><tr><td>Macro:</td><td></td><td></td></tr><tr><td>JPM EMBI Global Spread</td><td>-0.22</td><td>-0.30</td></tr><tr><td>Citi Economic Surprise - EM</td><td>-0.43</td><td>-0.29</td></tr><tr><td>Emerging Central Bank Rate</td><td>-0.48</td><td>-0.23</td></tr><tr><td>Quant Styles:</td><td></td><td></td></tr><tr><td>Quality</td><td>-0.16</td><td>-0.34</td></tr><tr><td>Momentum</td><td>-0.09</td><td>-0.12</td></tr><tr><td>LowVol</td><td>-0.05</td><td>-0.08</td></tr></table>

## Why our investment thesis broke

Our original thesis assumed certification would be the principal hurdle before passenger eVTOL commercialization. As the first company globally to obtain TC, PC, AC and operator OCs, we expected EHang to commercialize well ahead of competitors, generate operating cash flow, accumulate operating experience and fund successive generations of aircraft while peers remained in certification.

One year later, we believe this assumption no longer holds. Rather than moving from certification into commercialization, the industry has entered an iterative regulatory process where each major milestone has been followed by additional operational requirements. While these requirements are positive for long-term industry safety, they have transformed commercialization from a finite certification process into a moving regulatory target.

Figure 1: Evolution of commercialization requirements following certification

<table><tr><td>Timing</td><td>Investor expectation</td><td>What actually happened</td><td>Investment implication</td></tr><tr><td>1Q25</td><td>First OCs would unlock commercial passenger operations</td><td>Operations remained limited to highly controlled aircraft, routes and operating scenarios</td><td>Commercial rollout proved slower than expected</td></tr><tr><td>3Q25</td><td>Passenger operations would gradually expand and more OCs would be granted</td><td>Regulators introduced operator training standards, licensing requirements and examination procedures before broader deployment</td><td>New commercialization hurdle emerged after certification</td></tr><tr><td>Apr-26</td><td>Public ticket sales targeted by end-March</td><td>CAAC headquarters requested additional onboard obstacle detection and detect-and-avoid capability before launch</td><td>Ticket sales were postponed and another regulatory hurdle emerged</td></tr><tr><td>May-26</td><td>National operator training standards became effective, paving the way for commercialization</td><td>Public ticket sales were expected shortly thereafter</td><td>Commercialization appeared close</td></tr><tr><td>Jun-26</td><td>Gradual commercialization would continue</td><td>Beijing aviation accident disrupted parts of China&#x27;s general aviation sector and reinforced aviation safety priorities</td><td>China indefinitely banned most general aviation (GA) nationwide.Commercialization visibility deteriorated further</td></tr></table>

Source: JPM.

The Beijing aviation accident did not create this trend, but it reinforced regulators' already cautious approach toward aviation safety and reduced confidence that passenger eVTOL commercialization will accelerate in the near term. In our view, the key investment debate has shifted from “who can obtain certification first?” to “when will regulators permit commercialization at scale?” This fundamentally changes EHang's earnings trajectory and valuation framework.

## Why delayed commercialization disproportionately hurts EHang

The same regulatory environment does not affect every eVTOL developer equally. We believe EHang is disproportionately exposed because its competitive strategy was built around commercializing first, rather than developing the industry's highest-performance aircraft.

The EH216-S was intentionally designed as a first-generation commercial platform capable of reaching certification quickly under a relatively constrained operating environment. The investment thesis was straightforward: obtain certification ahead of competitors, begin commercial operations, generate operating cash flow and reinvest that cash into successive generations of aircraft with longer range, higher payload, improved charging efficiency and broader urban air mobility use cases.

Instead, commercialization has repeatedly been delayed.

Without meaningful commercial deployment, EHang will remain in a cash-burning phase for longer than originally anticipated. This delays internally funded product development while competitors continue progressing toward certification with newer aircraft designs.

The issue is not simply that commercialization has been postponed. Rather, every year of delay reduces the value of being first. Certification only creates shareholder value if it can be converted into commercial operations before competitors narrow the gap.

Management has also acknowledged that meaningful upgrades involving batteries, propulsion systems, flight-control software or onboard obstacle detection would require additional CAAC testing and certification. As a result, even if technology advances rapidly, implementation into certified commercial aircraft is unlikely to be immediate.

Figure 2: How our investment thesis has changed

<table><tr><td>Original investment thesis</td><td>Revised investment thesis</td></tr><tr><td>Certification lead</td><td>Certification lead remains intact</td></tr><tr><td>Rapid commercialization</td><td>Commercialization repeatedly delayed by evolving regulatory requirements</td></tr><tr><td>Operating cash flow generated from EH216-S</td><td>Prolonged cash burn and greater reliance on external funding</td></tr><tr><td>Cash flow funds second- and third-generation aircraft</td><td>Next-generation product roadmap progresses more slowly than expected</td></tr><tr><td>Co

[中间内容因长度限制已省略]

f market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and

should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
