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
# China Healthcare

# Expert call takeaways: Pulse check on China's clinical CROs in Q226

## H126: Strong order recovery; mild price recovery in some segments

We hosted a senior executive from a domestic private clinical CRO on 13 July. He noted a continued strong recovery in domestic clinical CRO order intake in H126, with overall order volume up 20-30% YoY, mainly driven by an uptick in the number of innovative drug clinical trials, increased outsourcing demand from small biotech companies and eased competition following the exit of small/medium-sized CROs. He indicated prices did not rebound sharply in Q2, although quotes for some orders in data management/clinical services edged up 3-5% vs. significantly less services for low-priced bioequivalence (BE) trials. Also, as an essential segment, SMOs had a more meaningful price recovery, with the service fees/gross profit of awarded contracts up 5-10%. The expert expects order intake to continue outpacing pricing in H226, with pricing likely to maintain mild single-digit growth.

## Limited geopolitical impact; actually closer global drug R&D ties

The expert thinks geopolitics had disruptions in sentiment for China's clinical CROs and innovative drugs going global, without changing the sector's going global trajectory. There is great uncertainty about whether proposals to restrict US regulators from accepting overseas clinical data can be implemented, while only a few companies may have concerns due to risk appetite. For one thing, the expert noted biotech companies' steady progress in overseas expansion, and many companies need ongoing R&D funding via out-licensing. For another, the expert believes China's clinical CROs have notable advantages in cost/patient enrolment speed, attracting overseas capital/global pharma firms to conduct early-stage clinical validation of targets in China. On this basis, the expert noted actually closer ties between global pharma and domestic CROs/pharma firms; the early trend shows domestic CROs are receiving more outsourcing orders from multinational companies, while they are following domestic innovative drug companies in overseas expansion.

## AI helps clinical CROs raise efficiency; investing by traditional/AI-based CROs

The expert mentioned AI has become a key approach to improve efficiency in clinical CROs, although currently more as workflow tool upgrades, rather than revolutionary business model changes. He said domestic/overseas CROs, pharma firms and EDC vendors are investing in AI. Multinational CROs are working with external suppliers to develop AI platforms, with efficiency in some processes likely to improve c30-50%. Domestic CROs have relatively limited investment, usually c1-2% of revenue, and mostly for internal-use tools. He emphasized statistical programming, data management, pharmacovigilance, medical writing and medical translation will be the first to benefit. For example, statistical programming can compress 20-30 hours of work into less than one hour, and there is a lot of room to lift the productivity of data management and statistics teams. He sees a positive boost from AI to margins, although it is unlikely to significantly raise industry pricing in the near term. Also, avoiding result bias and strengthening manual quality control remain challenges in implementation, while on-site clinical execution roles, including CRA and CRC, are still unlikely to be fundamentally replaced over the next five years.

## More details from the expert are provided below

The following pages contain key takeaways from the expert discussion, which are intended for investor reference only.

Equities

China

Healthcare

Chen Chen, PhD

Analyst

chen-zb.chen@ubs.com

+86-10-5832 8201

David Guo, PhD

Analyst

S1460524040001

david-za.guo@ubs.com

+86-10-5832 8010

Anita Wei

Analyst

anita.wei@ubs.com

+852-2971 7459

## TRANSCRIPT HIGHLIGHTS

Below, we present highlights from our recent expert call. We may have edited the transcript below for clarity. Minor grammatical changes that do not impact the meaning of content have been applied. The opinions expressed by the expert herein do not necessarily reflect the views and opinions of UBS. UBS accepts no responsibility for the accuracy, reliability or completeness of the information and will not be liable either directly or indirectly for any loss or damage arising out of the use of this information or any part thereof.

## 1. Did the ASP and volume of domestic clinical CRO orders in Q2 improve further from Q1?

Expert: Order intake picked up significantly in Q226 vs. Q126, with c20-30% YoY growth in H126. Prices in general had no notable changes, with only some orders having mild price rises of 3-5%. The drug regulator's latest annual clinical trial report showed continued YoY growth in trial volume, with that of innovative drugs gaining c18% YoY in 2025 (mainly class 1 innovative drugs). Coupled with the exit of small and medium-sized CROs and eased competition, there was a broad-based order intake increase, with SMOs having the most significant recovery (service fees and gross profit of awarded contracts up c5-10%).

## 2. What types of orders had moderate price increases, and why?

Expert: Overall order intake picked up, while the supply-demand dynamics improved due to the exit of some competitors amid previous weakness. The released ICH E6 (R3) clinical trial guidelines have more stringent requirements for quality and follow-up management throughout the whole clinical trial process, further raising the requirements for CROs. Under this circumstance, scaled CROs have no sharp price cuts for order intake, as small CROs used to do. Currently, orders related to statistics have had mild price increases, while fewer companies are willing to accept low-priced orders, such as BE studies.

## 3. What is your outlook for order intake and pricing in H226? Has the industry entered a recovery phase?

Expert: The recovery trend is relatively clear, and capital investment in new drugs is no longer as cautious as in the past two years. Also, China now ranks first globally by clinical trial volume and second only to the US by overall environment (policy, pricing, research institutions and transparency) among major countries. Prices are only about one-third to one-half of those in the US, while patient enrolment speed is about five times that of the US. Faster enrolment and earlier results have also attracted some overseas biopharma firms to conduct trials or make enquiries in China. Looking ahead to H226, prices could maintain mild single-digit increases, while order intake growth could be faster.

## 4. Are there differences or new changes in demand from large pharma companies, and small, medium-sized and large biotech companies?

Expert: Leading pharma companies have a relatively high proportion of in-house teams for domestic clinical business (including SMOs), and only outsource a small number of MRCT projects to multinational CROs. Large and mature biotech companies have also shifted from outsourcing to in-house teams in recent years, and tend to outsource most IIT and RWS to domestic CROs. Therefore, domestic CROs mainly undertake orders from small biotech companies, with demand rising amid trial number increases, although the cash flow of the latter is not as healthy as for the first two groups. In addition, an early new trend is that multinational pharma companies began to outsource some China-based projects to larger, higher-quality domestic CROs. After years of development, domestic CROs have been on par with multinational CROs by scale and clinical trial quality; they have notable price advantages and are also more competitive in maintaining relationships with research institutions and principal investigators (PIs).

## 5. What progress has been made in domestic CROs' strategy of following innovative drug makers going global and undertaking overseas clinical trials?

Expert: Going global is an inevitable trend, and destinations are no longer limited to the US; inquiries about Europe, Japan, Southeast Asia and Hong Kong have increased notably. Among them, leading CROs building overseas footprints earlier have acquired local CROs in Japan and Southeast Asia and gained advantages, while most others collaborate with local partners. Out-licensing of domestic innovative drugs neared US \$140bn in 2025, with the value of deals in H126 outpacing that in H125. CROs are also following domestic innovative drug makers in going global.

## 6. How are industry margins trending? Besides price increases, are there any other factors?

Expert: Margins have recovered slightly YoY and vs. Q126, rising c5%. Besides price increases, the main driver is cost reduction and efficiency improvement. Labour utilisation has improved c15-20%, offsetting cost pressure arising from earlier price declines. AI has also contributed. For example, in statistical programming, tasks such as SDTM/ADaM mapping that previously required 20-30 hours can now be shortened to less than one hour with AI assistance.

## 7. If the US implements policies restricting the FDA from accepting China's clinical data and strengthening cross-border data review, what would be the implications?

Expert: Currently, there is still great uncertainty in whether such policies will be implemented and how large the impact would be. Chinese biopharma companies' out-licensing has a greater impact on overseas start-ups that follow a similar model of "early-stage clinical trials + out-licensing" (Chinese innovative drugs have lowered the licensing prices of such assets); this trend is actually positive for multinational pharma companies, which are therefore pleased to see the continuing development of Chinese innovative drugs. Also, China has review procedures for the export of technology platforms. Overall, countries may have review measures, but the overall globalization trend will remain intact. This has also prompted more Chinese companies to conduct multi-regional clinical trials (MRCTs) at the early clinical trial stage.

## 8. How are domestic clinical CROs building AI capability? Apart from statistical programming, what other applications are there?

Expert: With extensive applications, AI is enabling the entire value chain. In clinical trials, applications include protocol design, CRF design, document management, risk control and statistical programming. However, companies vary in building their presences. Multinational companies mostly cooperate with well-developed external platforms, improving overall efficiency 30-50%. Domestic CROs are smaller in scale and have limited investment, so they mostly build small tools for internal use. By comparison, EDC companies are more proactive in investing (their results can also be commercialised).

## 9. Roughly what percentage of revenue will clinical CROs' AI investment account for in 2026-27?

Expert: Among domestic CROs, leading CROs invest cRmb100-200m, taking up less than 5% of revenue; in general, CROs invest c1-2% of revenue.

## 10. How much clinical CRO work could be undertaken by AI? Which areas will be most affected?

Expert: This can be viewed by risk level: low-risk or risk-free work will be undertaken by AI; medium-risk work will still require full-process manual quality control; high-risk, highly individualised work will still require human involvement. AI involvement may be stronger in data management, biostatistics, pharmacovigilance, medical writing and translation. However, roles such as CRC/CRA that communicate with research institutions, which also involve legal and regulatory requirements, may not change fundamentally over the next five years.

## 11. What advantages/disadvantages do AI-enabled CROs have compared with traditional leading CROs?

Expert: In the short term, they are less likely to have revolutionary differentiated advantages. Mature CROs already have historical protocol libraries for reference, and all CRO companies are investing in AI-related capability.

## Valuation Method and Risk Statement

We believe the risks facing China's medtech industry include: 1) larger-than-expected price reductions and smaller-than-expected market share gains from medical device VBP programs; 2) weaker-than-expected demand from equipment renewal programs; 3) a greater-than-expected impact from the anti-corruption drive; 4) geopolitical risks affecting the supply chain of medical device products; and 5) slower-than-expected product R&D and technological breakthroughs.

## Required Disclosures

This document has been prepared by UBS Asia Limited, an affiliate of UBS AG. UBS AG, its subsidiaries, branches and affiliates, including former CS AG and its subsidiaries, branches and affiliates are referred to herein as "UBS".

For information on the ways in which UBS manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures. Unless otherwise indicated, information and data in this report are based on company disclosures including but not limited to annual, interim, quarterly reports and other company announcements. The figures contained in performance charts refer to the past; past performance is not a reliable indicator of future results. Additional information will be made available upon request. UBS Co. Limited is licensed to conduct securities investment consultancy businesses by the China Securities Regulatory Commission. UBS acts or may act as principal in the debt securities (or in related derivatives) that may be the subject of this report. This recommendation was finalized on: 13 July 2026 11:18 PM GMT. UBS has designated certain UBS Global Research department members as Derivatives Research Analysts where those department members publish research principally on the analysis of the price or market for a derivative, and provide information reasonably sufficient upon which to base a decision to enter into a derivatives transaction. Where Derivatives Research Analysts co-author research reports with Equity Research Analysts or Economists, the Derivatives Research Analyst is responsible for the derivatives investment views, forecasts, and/or recommendations. Quantitative Research Review: UBS Global Research publishes a quantitative assessment of its analysts' responses to certain questions about the likelihood of an occurrence of a number of short term factors in a product known as the 'Quantitative Research Review'. Views contained in this assessment on a particular stock reflect only the views on those short term factors which are a different timeframe to the 12-month timeframe reflected in any equity rating set out in this note. For the latest responses, please see the Quantitative Research Review Addendum at the back of this report, where applicable. For previous responses please make reference to (i) previous UBS Global Research reports; and (ii) where no applicable research report was published that month, the Quantitative Research Review which can be found at https://neo.ubs.com/quantitative, or contact your UBS sales representative for access to the report or the Quantitative Research Team on ubs-quant-answers@ubs.com. A consolidated report which contains all responses is also available and again you should contact your UBS sales representative for details and pricing or the Quantitative Research team on the email above.

## Analyst Certification:

Each research analyst primarily responsible for the content of this research report, in whole or in part, certifies that with respect to each security or issuer that the analyst covered in this rep

[中间内容因长度限制已省略]

and/or Market Counterparties only as classified under the DFSA rulebook. It should not be distributed to Retail Clients. The Investment Research is provided for information purposes only and is not a recommendation or offer to buy/sell/hold a particular investment. The investment research may be out of date. You should seek investment advice before acting on the basis of the Investment Research. Abu Dhabi: UBS AG Abu Dhabi Branch is licensed and regulated by the Financial Services Regulatory Authority ("FSRA") of the Abu Dhabi Global Market. This material is intended solely for professional clients or market counterparties, as defined in the rules of the FSRA. It is not directed at, nor intended for, retail clients or any person who does not meet the criteria of a professional client or market counterparty. United Kingdom: This document is issued by UBS Wealth Management, a division of UBS AG which is authorised and regulated by the Financial Market Supervisory Authority in Switzerland. In the United Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.
"""
