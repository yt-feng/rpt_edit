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

## LG Electronics

2Q26 OP beat; positive CDU business progress vs. immature robotics outlook; maintain N

Following the 2Q26 headline beat (link), management guided for an above-seasonal 3Q outlook, helped by prudent cost control at the MS and HS divisions, in our view. LGE is in a transitional period of pivoting from a B2C-centric business portfolio to an AIDC CDU/robotics manufacturer, in our view, with management highlighting NVDA certification (link) and mass-production of actuators in 2H26. The company disclosed W600bn worth of CDU order wins in 1H26, with the amount likely to reach several trillion won by year-end. Between CDU and robotics, we continue to take a conservative stance on the robotics business opportunity, given intensifying market competition and a lack of tangible business strategy. Given the downward slope in earnings in 2H26, as well as a limited robotics business opportunity, we advise investors to stay on the sidelines.

\- 2Q26 earnings beat thanks to tariff refund. LGE reported an earnings beat despite geopolitical uncertainty, with OP of W1.58tn on sales of W23.8tn (OPM: 6.6%), driven mainly by: (1) HS sales growing 7% Y/Y, with OPM at 9.7% (both above original guidance of mid-single-digit % sales growth/OPM), largely aided by LGE's two-track strategy, as well as reciprocal tariff refunds (one-off gain net of expense: W300bn, per management); and (2) MS reporting mid-teens % y-y sales growth, coupled with a mid-single-digit % OPM (vs. JPMe: 16% Y-Y and 0% OPM), on global sporting event demand. VS was better than feared, recording mid-single-digit % Y/Y sales growth, helped by continued stable growth of the infotainment business, with profitability improving due to operational efficiency. On the other hand, ES reported low-single-digit % sales growth and a high-single-digit OPM, with profitability declining YoY due to higher logistics cost. Management emphasized completion of AI DC validation toward NVDA for its 600kW CDU (link) and disclosed W600bn worth of order wins in 1H26, projected to grow to several trillions by year-end. On the robotics front, management reiterated building a robotics data factory in 2H26, with production of initial actuators under way following the completion of pilot lines.

\- 3Q26 earnings outlook and CDU business as the next growth engine. For 3Q, management guides to an above-seasonal outlook of low-teens % y-y growth with a mid-single-digit % OPM, helped by prudent cost control at the MS division (BEP margin guidance following labor restructuring and WebOS) and the VS division (high-single-digit % OPM guidance from strong order booking). Management expects the HS division to post at the high end of high-single-digit % sales growth from continued two-track and broadening subscription business with a mid-single-digit % margin. On the ES division, guidance remained conservative, at mid-single-digit % y-y top-line growth and a mid-single-digit % OPM, due mainly due to an investment burden on the CDU and robotics business. We maintain our positive view on LGE's CDU business acting as the next growth engine, more so than robotics. Management guides that the W600bn order backlog is not inclusive of big tech companies, and we expect additional order wins in 2H26E to act as a positive growth driver for the ES division in 2027 and into 2028.

\- Share price outlook. LGE’s share price performance has been volatile YTD

See page 7 for analyst certification and important disclosures, including non-US analyst disclosures.

## Neutral

066570.KS, 066570 KS

Price (30 Jul 26):W147,500

Price Target (Jun-27):W190,000

## Technology - Semiconductors

Jay Kwon AC
(82-2) 758-5725
jay.h.kwon@JPM.com
JPM Securities (Far East) Limited, Seoul Branch

Sangsik Lee
(82-2) 758 5146
sangsik.lee@JPM.com
JPM Securities (Far East) Limited, Seoul Branch

Neelay Y Kamath
(91-22) 6157 3764
neelay.kamath@jpmchase.com
JPM India Private Limited

(+60% vs. LGIT/LGD : +55%/-28% vs. KOSPI: +33%), mainly on robotics business initiative expectations. However, given the lingering geopolitical risks and heavy profit-taking after an overheated AI & robotics rally, the stock has corrected -61% from its peak on 1 June (vs. KOSPI -36%). In the near term, we expect the debate to shift from robotics to the CDU business acting as the next growth engine, as well as MS margin normalization. On LGE's robotics side, while initial production of actuators is under way, limited business visibility and distant major orders suggest it is too early to price in as an emerging business. Therefore, we remain Neutral on the stock and recommend investors wait on the sidelines for a better entry point.

Table 1: LGE 2Q26 earnings comparison

<table><tr><td>Won in billions</td><td>2Q25</td><td>1Q26</td><td>2Q26 Actual</td><td>2Q26 JPMe</td><td>Diff. (%)</td><td>Q/Q (%)</td><td>Y/Y (%)</td></tr><tr><td>Sales</td><td>20,735</td><td>23,727</td><td>23,827</td><td>22,594</td><td>5.5</td><td>0.4</td><td>14.9</td></tr><tr><td>Home Appliance Solution</td><td>6,597</td><td>6,943</td><td>7,076</td><td>6,862</td><td>3.1</td><td>1.9</td><td>7.2</td></tr><tr><td>Eco Solution</td><td>2,644</td><td>2,822</td><td>2,726</td><td>2,703</td><td>0.9</td><td>-3.4</td><td>3.1</td></tr><tr><td>Media Entertainment Solution</td><td>4,393</td><td>5,169</td><td>5,115</td><td>4,905</td><td>4.3</td><td>-1.1</td><td>16.4</td></tr><tr><td>Vehicle components Solution</td><td>2,849</td><td>3,064</td><td>3,026</td><td>3,069</td><td>-1.4</td><td>-1.3</td><td>6.2</td></tr><tr><td>LG Innotek sales</td><td>3,796</td><td>5,424</td><td>5,419</td><td>4,756</td><td>13.9</td><td>-0.1</td><td>42.8</td></tr><tr><td>Others</td><td>455</td><td>304</td><td>465</td><td>300</td><td>55.1</td><td>53.2</td><td>2.3</td></tr><tr><td>Operating profit</td><td>639</td><td>1,674</td><td>1,579</td><td>1,074</td><td>47.0</td><td>-6</td><td>147</td></tr><tr><td>Margin (%)</td><td>3.1</td><td>7.1</td><td>6.6</td><td>4.8</td><td></td><td></td><td></td></tr><tr><td>Home Appliance Solution</td><td>438</td><td>570</td><td>686</td><td>425</td><td>61.2</td><td>20</td><td>56</td></tr><tr><td>Margin (%)</td><td>6.6</td><td>8.2</td><td>9.7</td><td>6.2</td><td></td><td></td><td></td></tr><tr><td>Eco Solution</td><td>251</td><td>249</td><td>236</td><td>230</td><td>2.6</td><td>-5</td><td>-6</td></tr><tr><td>Margin (%)</td><td>9.5</td><td>8.8</td><td>8.6</td><td>8.5</td><td></td><td></td><td></td></tr><tr><td>Media Entertainment Solution</td><td>-192</td><td>372</td><td>219</td><td>2</td><td>9,262.3</td><td>-41</td><td>na</td></tr><tr><td>Margin (%)</td><td>-4.4</td><td>7.2</td><td>4.3</td><td>0.0</td><td></td><td></td><td></td></tr><tr><td>Vehicle Components</td><td>126</td><td>212</td><td>191</td><td>246</td><td>-22.1</td><td>-10</td><td>52</td></tr><tr><td>Margin (%)</td><td>4.4</td><td>6.9</td><td>6.3</td><td>8.0</td><td></td><td></td><td></td></tr><tr><td>LG Innotek</td><td>16</td><td>298</td><td>252</td><td>166</td><td>52.0</td><td>-15</td><td>1,506</td></tr><tr><td>Margin (%)</td><td>0.4</td><td>5.5</td><td>4.7</td><td>3.5</td><td></td><td></td><td></td></tr><tr><td>Others</td><td>0</td><td>-26</td><td>-5</td><td>5</td><td>na</td><td>na</td><td>na</td></tr><tr><td>Recurring profit</td><td>762</td><td>1,401</td><td>1,239</td><td>854</td><td>n.a</td><td>-11.5</td><td>62.7</td></tr><tr><td>Tax</td><td>151</td><td>396</td><td>458</td><td>226</td><td>n.a</td><td>15.7</td><td>203.4</td></tr><tr><td>Net profit</td><td>605</td><td>816</td><td>668</td><td>464</td><td>n.a</td><td>-18.1</td><td>10.5</td></tr></table>

Source: Company data, JPM estimates, Bloomberg Finance L.P.

Figure 1: LGE – 12M forward P/E bands
Won  
![](images/78d9bb5ccf7a187c7c9065f9fc0953c3afd18a9eb389ce4d891c7814d9e6ad6d.jpg)  
Source: Bloomberg Finance L.P., JPM estimates.

Figure 2: LGE – 12M forward P/BV and ROE
Won, %  
![](images/fca229dafe2f0c5a5a0570c4173db4cbe09cf4dfbf88f1536657d804997c8d42.jpg)  
Source: Bloomberg Finance L.P., JPM estimates.

Figure 3: LGE – 12M forward core P/E multiple trend  
![](images/eed53aa6f77d1d5cbd5674e8105b40abe855b372f8b9823f8b07eedad7b07699.jpg)  
Source: Bloomberg Finance L.P., JPM estimates

Figure 4: LGE – 12M forward P/BV multiple trend  
![](images/c538f89895e867c408ba6e7abe7e74c4e0a9d09ac66a57bdbb077bfd5bc7c97b.jpg)  
Source: Bloomberg Finance L.P., JPM estimates

Figure 5: LGE vs. subsidiaries – YTD performance %  
![](images/7e388e0653bade23eca8e9c24e48ab6ece532d440f9fef7e4389786a49602a19.jpg)  
Source: Bloomberg Finance L.P. Note: Past results are not an indicator of future performance.

Figure 6: LGE vs. H&A peers – YTD performance %  
![](images/ad02a43ce372c2307d947d637dfb134d9c461690bb4db9e161b8b14f449c967d.jpg)  
Source: Bloomberg Finance L.P. Note: Past results are not an indicator of future performance.

## 2Q26 earnings call recap – Our summary

## Q. [Corporate] Following news flow on NVIDIA CEO meeting LG management, any details on ongoing collaboration with NVIDIA? What is the roadmap outlook?

A. In the robotics sector, LGE is pursuing a joint project aimed at combining its robot hardware technology with Nvidia's physical AI technology stack. By collaborating from the proof-of-concept stage, the project is targeted at robot manufacturing up to actual application. LGE is focused on advancing robot foundation models and developing simulation and verification platforms. In the AI datacenter, LGE is collaborating on the development of advanced high-density cooling technologies (Coolant Distribution Unit). The company's models of CDU received Nvidia certification, marking a meaningful milestone. For the mobility sector, the engineering teams of both companies have begun to develop an AI-based software vehicle platform. Currently, practical work is under way, and companies are conducting reviews of next-generation high-performance computing platforms.

## Q. [HS] Any expectations of freight rates rising in the near term? Outlook for logistics costs for 2H26E?

A. SCFI rates have been trending higher due to geopolitical tensions. With more carriers entering the market in 2H26 and global shipping demand likely to moderate after the peak season, we will continue to renegotiate terms with carriers by leveraging large-scale volume and long-standing relationships. LGE is improving to further optimize operations to minimize logistics costs. LGE believes freight rates could peak in 3Q26, and easing market conditions could drive rates back to prior-year levels.

## Q. [Robotics] Any color on commercialization of actuators? Any guidance on visibility into earning recognition and scope of partnership?

A. The 1H26 actuator pilot line has been completed and is now focused on quality testing and automation. In partnership, LGE signed an MOU in June and is considering more collaborative efforts. LGE aims to become a provider of customized solutions in robotics, not only a components provider. By integrating data platforms and AI agents, LGE targets to deliver physical AI solutions. In the newly established Robotics Business Center, LGE plans on collaborating with not only big tech companies like NVIDIA, but also with leading Chinese robotics players. Last, LGE seeks synergy across LG affiliates and portfolio companies.

## Q. [Corporate] Regarding the US tariff refund, any details on how much of the refund was reflected in 2Q?

A. The company followed the refund guidance provided by the US government. LGE received a full refund in 2Q26, and net of one-time expense was approximately W300bn. While tariff concerns remain in 2H26, LGE aims to reduce volatility by leveraging supply chain optimization and flexible pricing policies.

## Q. [VS] Regarding LG Magna, any details on operating status in Mexico and Hungary? And outlook during market volatility?

A. LGE is seeking to expand its revenue base beyond the NA market and has been operating in the EU and Asia. The company has secured meaningful EV powertrain order wins from Asia and EU OEMs in 1H26. This allows LGE to diversify regional exposure and reduce heavy reliance on select companies. (1) Mexico – achieved stable operations since opening in 2023 and contributing to more than 40% of total sales; (2) Hungary – key hub for Europe localization efforts and anticipates MP in Jan-27. To address demand volatility, LGE is closely monitoring various external factors, like promotions and incentives.

Q. [ES] With high expectations for the AI datacenter chiller business, which regions are the primary target?

A. NA is the primary area for AI datacenter cooling business. IT capacity is expected to grow from 25GW in 2026 to 70GW in 2031, and more than 60% will be in NA. Hence, CSPs are the primary channel partners for chillers and liquid/cooling components. For Asia, the company seeks to expand customers by leveraging its existing track record and using the “One LG” strategy.

Q. [MS] The MS division delivered significant improvement, recording operating profit. What were the drivers to the improvement, and any guidance on outlook?

A. OP improvement was driven by a higher proportion of premium products and enhanced performance from overseas operations. In 2H26, management expects macro environment volatility and rising memory cost to affect profitability. In response, LGE will optimize strategic inventory and continue cost-efficiency initiatives. LGE expects a full year of operating profit. Over the mid- to long term, LGE aims to accelerate the growth of WebOS system and maintain a stable profitability trend.

# Investment Thesis, Valuation and Risks

LG Electronics (Neutral; Price Target: W190,000)

## Investment Thesis

We estimate that LGE's core NOPAT will grow at a double-digit rate throughout our forecast period, driven by stable profit improvement from core operations. However, new business initiatives are at an early stage, such that meaningful business transition is limited. Based on our mid-cycle valuation, we view the risk/reward as unfavorable at the current share price. We remain Neutral on the stock.

## Valuation

Our Jun-27 PT of W190K valuation is based on 17x FY27E core NOPAT per share, in line to a mid-cycle valuation to reflect a growing AI DC grade chiller and cooling solutions business opportunity and core business cycle earnings normalization. On the other hand, we believe it is too early to give credit to the robotics business growth opportunity.

## Risks to Rating and Price Target

Upside risks include: (1) stronger H&A margin expansion, driven by faster new business growth (e.g., Chiller, HVAC, and others); (2) Web OS customer diversification outside captive customers or faster end-market diversification into automotive customers; and (3) a recovery in the EV market and LGE's further vehicle-business design wins.

Downside risks include: (1) raw materials/logistics cost-related margin headwinds; (2) continued TV panel price strength resulting in further HE hardware profitability; and (3) further delays in the EV market recovery and slowing new order wins in the vehicle component business.

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Kor

[中间内容因长度限制已省略]

f market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
