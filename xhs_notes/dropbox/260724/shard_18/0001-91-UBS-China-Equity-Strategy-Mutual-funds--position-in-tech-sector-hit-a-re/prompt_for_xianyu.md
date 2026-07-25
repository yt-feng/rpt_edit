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
# China Equity Strategy

# Mutual funds' position in tech sector hit a record high in Q226

## MFs added electronics/telecom/machinery; cut electrical equipment/non-ferrous metals/F&B

In Q226, mutual funds (MFs) added the most positions in electronics, telecom and machinery, up 20.2/4.4/0.8ppt QoQ (Figure 1). Specifically, the global AI wave continues to drive robust capex growth at global tech players, underpinning the strong fundamentals of tech hardware. Both MFs' position in and overweight ratio of electronics and telecom rose sharply to all-time highs in Q226. Machinery posted a 0.8ppt position increase in the quarter, with the humanoid robotics value chain growing fast and the construction machinery's overseas growth recovering.

## MFs sharply lifted STAR Board/ChiNext positions; AUM % of tech-focused active MFs hit record high

As the focus of global stock markets returned to the AI-related greater tech sector in Q226, A-share MFs also meaningfully increased their allocation to tech-related sectors and boards. MFs raised their position in the STAR Board/ChiNext Board substantially in the quarter (ie, up 9.9ppt/3.5ppt QoQ), both hitting record highs. MFs' position in and overweight ratio of the greater tech sector hit 57.3% and 18.5%, both new highs, with the allocation ratio well above the previous peak of 43.7% posted by the greater consumer sector. Meanwhile, we define actively managed track funds as those where at least seven of the ten largest holdings (as per their quarterly disclosures) are from a specific sector and their combined weighting tops 50%. We note the actively managed tech track funds as % of the overall actively managed MF AUM hit a record-high of 27.5% as of Q226. We also find that the AUM share of actively managed tech track funds has risen well above that of active funds benchmarked against tech-related indices.

## Northbound swung to net inflows in Q226

Our estimates show that northbound swung to a net inflow of Rmb223bn in Q226 from a net outflow of Rmb13bn in Q126. We think the increasing appeal of A-share hard tech stocks is a major reason. By sector, industrials and IT netted northbound inflows of Rmb128.5bn and Rmb67.2bn in Q226, respectively, whereas consumer staples and telecom were the only two sectors with net outflows (Rmb9.7bn and Rmb3.1bn, respectively).

Equity strategy: With deleveraging near the end, how to position going ahead? In our note "With ETF trading amounts expanding, A-share deleveraging may be nearing the end", we ascribe the increased volatility of global tech stocks and the sharp A-share tech pullback recently chiefly to profit-taking, reduced trade crowdedness and deleveraging pressure. However, the A-share earnings fundamentals are improving; we expect all A-shares' earnings YoY growth to pick up from 3.9% in 2025 to 11% in 2026. Since the start of Q226, the industrial enterprises' profit growth has accelerated, and the earnings estimates for the ChiNext Board and STAR Board have seen continuous upward revisions. Meanwhile, policy support for AI development remains a secular tailwind. As the market fluctuated sharply recently, regulators, state-owned capital operation companies, and insurers expressed commitments to safeguarding market stability. The CSI 300/ChiNext Index/STAR 50 ETFs saw trading volume spikes, with large-scale net inflows. Moreover, the balance of margin financing of the A-share market has fallen rapidly from its peak; margin financing in the tech sector has contracted significantly, while its leverage ratio remains broadly comparable to the overall market. These suggest the current A-share deleveraging phase may be nearing its end, in our view.

## Equity Strategy

China

Lei Meng

Strategist

lei.meng@ubs.com

+86-21-3866 8939

Yu Sheng

Strategist

S1460524080001

yu.sheng@ubs.com

+86-21-3866 4873

James Wang

Strategist

james-zb.wang@ubs.com

+852-3712 2557

Tommy Tang, CFA

Strategist

tommy.tang@ubs.com

+852-2971 8357

Robin Xu

Analyst

S1460511010012

bin.xu@ubs.com

+86-21-3866 8872

Figure 1: MFs' position change in Q226 (QoQ)  
![](images/31f35910f1a5876184d3592ebbeff2bf17e21bb9a42b3f2e94d2ea6027fdcb2f.jpg)  
Source: Wind, UBS-S estimates

Figure 2: Q226 MFs' % of overweight/underweight by sector (benchmark against CSI300)  
![](images/33181dd35eb0b91ac326d78ff227a57f90e6f4426d9e1e62e11c827a8340c03b.jpg)  
Source: Wind, UBS-S estimates

Figure 3: MFs' sector allocation  
![](images/eb4f41c6a255a3ecf03fc6007966a01725f71d7de814579a3d25a85aa6813332.jpg)  
Source: Wind, UBS-S estimates

Figure 4: MFs' position in SOEs shrank materially  
![](images/954abf1f84e504a1cc50461f2b348e01b785eec6be38f035bdcda51fb3d2ab39.jpg)  
Source: Wind, UBS-S estimates

Figure 5: Both MFs' position in and overweight % of STAR Board jumped  
![](images/ba6c225b520c5aa655abd601b5f624af0b48a56faa033681f0ce8e089b50991c.jpg)  
Source: Wind, UBS-S estimates

Figure 6: Both MFs' position in and overweight % of ChiNext rose sharply  
![](images/66c86f9c8ed7782aefad5a5fd53c075350c9ee180eed93cceb00dcbc9bceebdc.jpg)  
Source: Wind, UBS-S estimates

Figure 7: MFs' position in electrical equipment fell substantially  
![](images/13b32ad88f250133737ea8636168afcd8d2e7988e354f984ad556e46a9594f4c.jpg)  
Source: Wind, UBS-S estimates

Figure 8: MFs' position in food & beverages fell further  
![](images/1d7415cdbf3b19c8fff417b405f1f40e8b863f52bf450c6efa64065352ef06ca.jpg)  
Source: Wind, UBS-S estimates

Figure 9: Both MFs' position in and overweight % of healthcare declined  
![](images/b52eb83849afd3a00e712205e8f26a4284f6d14549cc262568335253c39b621d.jpg)  
Source: Wind, UBS-S estimates

Figure 10: Both MFs' position in and overweight % of machinery rebounded further  
![](images/bd0857f5e6121836bd5f7d339ae81cbb01fa0c3dd891d8ec8505efac51da93cb.jpg)  
Source: Wind, UBS-S estimates

Figure 11: MFs' position in home appliances fell further  
![](images/90524c399d8ce2d0815a4b5193ba15ec22cc58a9fe4a1175e4a379da2e3548c9.jpg)  
Source: Wind, UBS-S estimates

Figure 12: MFs' position in coal dropped, while the underweight ratio narrowed  
![](images/c05617e47b1f3a3515d42f122c7fdcd4eab0c6e570b4be1e5b4f1fb7d042cbd7.jpg)  
Source: Wind, UBS-S estimates

Figure 13: MFs' position in oil and petrochemicals fell  
![](images/c71466bbcae3f9509dacad1900e81858ee8f1a724a767dc89e95169f79b8d4ec.jpg)  
Source: Wind, UBS-S estimates

Figure 14: MFs' position in non-ferrous metals was down sharply  
![](images/15d85d191dfe658123925a9fe1b0cc77f16ca27307e829ac35fc96c5eed3d46b.jpg)  
Source: Wind, UBS-S estimates

Figure 15: MFs' position in chemicals fell significantly  
![](images/334dec31a69fef6203c4dd924783fc433229b33e8923c6f00653d0e2d4909a5f.jpg)  
Source: Wind, UBS-S estimates

Figure 16: MFs' position in national defence fell notably  
![](images/521b587c9173088372134cf6adec817623c8580f095af00d6d67b4eac098fe28.jpg)  
Source: Wind, UBS-S estimates

Figure 17: MFs' position in autos edged lower  
![](images/11c6f0ef94091ba15fa7d20015b4bfd14a2902f343b61c52be90ac5689600035.jpg)  
Source: Wind, UBS-S estimates

Figure 18: MFs' position in banks fell further  
![](images/953db03f5958aa6094ace1f6bafe75388e583a285844ffe7f34cc272249d24bd.jpg)  
Source: Wind, UBS-S estimates

Figure 19: MFs' position in non-bank financials moved lower  
![](images/f0eaafdd7ec0c2b1dfac26174b0823edbe13520ac9152f9bff2078c6c0340a0e.jpg)  
Source: Wind, UBS-S estimates

Figure 20: Both MFs' position in and overweight % of electronics jumped  
![](images/03733d2702ec4220a9c97a52d441e7ca6d4b3abf309afe9f7f32f7a00887e334.jpg)  
Source: Wind, UBS-S estimates

Figure 21: MFs' position in computer declined  
![](images/f194dc9839769e459d1391e7a68319698b7685134809b1e93b3b80bbd7206275.jpg)  
Source: Wind, UBS-S estimates

Figure 22: Both MFs' position in and overweight % of telecom jumped further  
![](images/5a3df68d7809ff081576f663f9a311bb9658d480eab2fbf4509bfed2705772f1.jpg)  
Source: Wind, UBS-S estimates

Figure 23: MFs' position in utilities edged down  
![](images/44530c22201155b28b14c036989fd3f0b1d14665b9c230bd1f2df40a2d659221.jpg)  
Source: Wind, UBS-S estimates

Figure 24: MFs' overweight % of the greater tech sector jumped  
![](images/566831ad70d4502498a5995b5a6e6d182d5959c59ca74b4f322ce57803cd14e0.jpg)  
Source: Wind, UBS-S estimates. Note: Note: The greater tech sector includes electronics, telecom, computers and national defence.

Figure 25: MFs' position in and overweight % of the greater consumer sector  
![](images/ccb218560deb7f53c7a0ce03e2c093b8c3746ea4b840dc743de53389a336988a.jpg)  
Source: Wind, UBS-S estimates. Note: The greater consumer sector includes agriculture, food and beverage, healthcare, home appliances, textile, light manufacturing, social services, commercial trade, beauty treatments and conglomerates.

Figure 26: AUM of actively managed tech, consumer and new energy funds as % of total actively managed funds  
![](images/2e282d3cd92440ada50a98bd490031bb8f62c4ea8371134ea23b495e4131229a.jpg)  
AUM of actively managed tech track funds as of total actively managed funds (%)
AUM of actively managed consumer track funds as of total actively managed funds (%)
AUM of actively managed New energy track funds as of total actively managed funds (%)  
We define actively managed track funds as those where at least seven of the ten largest holdings are from a specific sector and their combined weighting tops 50%. We note actively managed tech track funds have been rising fast as a portion of the overall actively managed MF AUM since Q225, to a record-high of 27.5% as of Q226.  
Source: Wind, UBS-S estimates. Note: We define actively managed track funds as those where at least seven of the ten largest holdings are from a specific sector and their combined weighting tops 50%. Tech funds cover electronics, telecoms, computer and national defence. Consumer funds cover agriculture, food and beverage, healthcare, home appliances, textile, light manufacturing, social services, commercial trade, beauty treatments and conglomerates. New energy funds cover electrical equipment, utilities and autos.

Figure 27: AUM of actively managed track funds as % of total actively managed MFs  
![](images/435102f5945a81892248df7bd5887c99798f82b49a4c9acb8938b8224bc2f2c3.jpg)  
We also find that the AUM share of actively managed tech track funds has risen well above that of active funds benchmarked against tech-related indices.  
Source: Wind, UBS-S estimates. Note: Q219/Q322/Q226 data for consumer/new energy/tech sector comparisons

Figure 28: Q226 southbound net inflows by sector  
![](images/f94270560bc69ce6952ffcf15dfa4e91cb5d7513a469bcf0ad964ce44de63fd7.jpg)  
Source: Wind, UBS-S estimates

Figure 29: Q226 northbound net inflows by sector  
![](images/92acc002b4b09c2c63723187332013729cd7dbeb3750a955ddc06a2635029149.jpg)  
Source: Wind, UBS-S estimates

## Valuation Method and Risk Statement

For various stocks across the industries we cover in the Hong Kong and mainland China stock markets, we use a variety of valuation approaches, including DCF models, Gordon growth model analysis and relative valuation analysis using various multiples such as PE, EV/EBITDA and P/BV.

We think the risks facing China's equities include a hard landing for the property market, a capital exodus associated with currency depreciation and slow structural reform progress. In our view, any government policies that do not adequately address these risks could result in a shock to the market. For example, an excess of stimulus policies could pose a risk to the transition from an investment-driven to a consumption-driven economy and increase the debt of government and state-owned enterprises.

## Required Disclosures

This document has been prepared by UBS Asia Limited, an affiliate of UBS AG. UBS AG, its subsidiaries, branches and affiliates, including former CS AG and its subsidiaries, branches and affiliates are referred to herein as "UBS".

For information on the ways in which UBS manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures. Unless otherwise indicated, information and data in this report are based on company disclosures including but not limited to annual, interim, quarterly reports and other company announcements. The figures contained in performance charts refer to the past; past performance is not a reliable indicator of future results. Additional information will be made available upon request. UBS Co. Limited is licensed to conduct securities investment consultancy businesses by the China Securities Regulatory Commission. UBS acts or may act as principal in the debt securities (or in related derivatives) that may be the subject of this report. This recommendation was finalized on: 22 July 2026 03:53 PM GMT. UBS has designated certain UBS Global Research department members as Derivatives Research Analysts where those department members publish research principally on the analysis of the price or market for a derivative, and provide information reasonably sufficient upon which to base a decision to enter into a derivatives transaction. Where Derivatives Research Analysts co-author research reports with Equity Research Analysts or Economists, the Derivatives Research Analyst is responsible for the derivatives investment views, forecasts, and/or recommendations. Quantitative Research Review: UBS Global Research publishes a quantitative assessment of its analysts' responses to certain questions about the likelihood of an occurrence of a number of short term factors in a product known as the 'Quantitative Research Review'. Views contained in this assessment on a particular stock reflect only the views on those short term factors which are a different timeframe to the 12-month timeframe reflected in any equity rating set out in this note. For the latest responses, please see the Quantitative Research Review Addendum at the back of this report, where applicable. For previous responses please make reference to (i) previous UBS Global Research reports; and (ii) where no applicable research report was published that month, the Quantitative Research Review which can be found at https://neo.ubs.com/quantitative, or contact your UBS sales representative for access to the report or the Quantitative Research Team on ubs-quant-answers@ubs.com. A consolidated report which contains all responses is also available and again you should contact your UBS sales representative for details and pricing or the Quantitative Research team on the email above.

## Analyst Certification:

Each research analyst primarily responsible for the content of this research report, in whole or in part, certifies that with respect to each security or issuer that the analyst covered in this report: (1) all of the views expressed accurately reflect his or her personal views about those securities or issuers and were prepared in an independent manner, including with respect to UBS, and (2) no part of his or her compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in the research report.

UBS Global Research: Global Equity Rating Definitions

<table><tr><td>12-Month Rating</td><td>Definition</td><td>Coverage $^{1}$ </td><td>IB Services $^{2}$ </td></tr><tr><td>Buy</td><td>FSR is &gt; 6% above the MRA.</td><td>55%</td><td>24%</td></tr><tr><td>Neutral</td><td>FSR is between -6% and 6% of the MRA.</td><td>40%</td><td>21%</td></tr><tr><td>Sell</td><td>FSR is &gt; 6% below the MRA.</td><td>6%</td><td>21%</td></tr></table>

Source: UBS. Rating allocations a

[中间内容因长度限制已省略]

ofessional/institutional clients only and not for distribution to any retail clients. Malaysia: This material is authorized to be distributed in Malaysia by UBS Malaysia Sdn. Bhd (Capital Markets Services License No.: CMSL/A0063/2007). This material is intended for professional/institutional clients only and not for distribution to any retail clients. India: Distributed by UBS India Private Ltd. (Corporate Identity Number U67120MH1996PTC097299) Unit 2901, Level 29 Altimus, Pandurang Budhkar Road, Worli, Mumbai – 400 018. It provides brokerage services bearing SEBI Registration Number: INZ000259830; Merchant Banking services bearing SEBI Registration Number: INM000013101; and Research Analyst services bearing SEBI Registration Number: INH000001204. Name of Compliance Officer Mr Parameshwaran Shivaramakrishnan, Phone : +912261556151, Email : parameshwaran.s@ubs.com, Name of Grievance Officer Parameshwaran Shivaramakrishnan, Phone : +912261556151, Email: ol-ubs-sec-compliance@ubs.com Registration granted by SEBI, and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. UBS may have debt holdings or positions in the subject Indian company/companies. UBS may have financial interests (e.g. loan/derivative products, rights to or interests in investments, etc.) in the subject Indian company / companies from time to time. Within the past 12 months, UBS may have received compensation for non-investment banking securities-related services and/or non-securities services from the subject Indian company/companies. The subject company/companies may have been a client/clients of UBS during the 12 months preceding the date of distribution of the research report with respect to investment banking and/or non-investment banking securities-related services and/or non-securities services. With regard to information on associates, please refer to the Annual Report at: https://www.ubs.com/global/en/about\_ubs/investor\_relations/annualreporting.html The Research Annual Compliance Report for UBS India Private Limited is available on www.ubs.com/ubssi under Research tab. Taiwan: Except as otherwise specified herein, this material may not be distributed in Taiwan. Information and material on securities/instruments that are traded in a Taiwan organized exchange is deemed to be issued and distributed by UBS Pte. LTD., Taipei Branch to professional institutional investors and/or persons permitted under applicable regulation. Unless permitted by applicable Taiwan laws and regulations, this material is for reference and information only and should not constitute "recommendation" to clients or recipients in Taiwan for the covered companies or any companies mentioned in this document. No portion of the document may be reprinted, reproduced or quoted by the press or any other person without authorisation from UBS. Indonesia: This report is being distributed by PT UBS Sekuritas Indonesia and is delivered by its licensed employee(s), including marketing/sales person, to its client. PT UBS Sekuritas Indonesia, having its registered office at Sequis Tower Level 22 unit 22-1,Jl Jend. Sudirman, kav.71, SCBD lot 11B, Jakarta 12190. Indonesia, is a subsidiary company of UBS AG and licensed under Capital Market Law no. 8 year 1995, a holder of broker-dealer and underwriter licenses issued by the Capital Market and Financial Institution Supervisory Agency (now Otoritas Jasa Keuangan/OJK). PT UBS Sekuritas Indonesia is also a member of Indonesia Stock Exchange and supervised by Otoritas Jasa Keuangan (OJK). Neither this report nor any copy hereof may be distributed in Indonesia or to any Indonesian citizens except in compliance with applicable Indonesian capital market laws and regulations. This report is not an offer of securities in Indonesia and may not be distributed within the territory of the Republic of Indonesia or to Indonesian citizens in circumstance which constitutes an offering within the meaning of Indonesian capital market laws and regulations.

The disclosures contained in research documents produced by UBS AG, London Branch or UBS Europe SE shall be governed by and construed in accordance with English law.

UBS specifically prohibits the redistribution of this document in whole or in part without the written permission of UBS and in any event UBS accepts no liability whatsoever for any redistribution of this document or its contents or the actions of third parties in this respect. Images may depict objects or elements that are protected by third party copyright, trademarks and other intellectual property rights. © UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/9281fda464ec7719039ad7f5bb2ac7d612097e50c686ff8393ef3b8af868d666.jpg)
"""
