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
# Healthcare Facilities & Managed Care Healthcare Horizons: The First Baby Boomer Hits 80 This Year, So What?

With this research note, we are introducing a new thematic report which we are calling "Healthcare Horizons" We plan to use these reports to look at broader evolving themes in healthcare services. This first edition examines the implications of the first baby boomer reaching 80 years of age in 2026.

## The Baby Boomer Demographic is Set to Boost the "Over 80" Age Cohort for the Next 15 Years

The year 2026 represents a pivotal demographic milestone, as the first members of the Baby Boomer generation (born 1946–1964) reach 80 years of age. Although population aging has been an enduring trend, numerous demographic analyses highlight that outcomes, healthcare utilization, and expenditures undergo significant shifts once individuals reach their 80s, setting this stage apart from the broader 65+ demographic. Brookings Institution research projects that the U.S. population aged 80 and older will approximately double between the mid 2020s and mid 2040s, rising from roughly 15 mln to nearly 30 mln individuals. U.S. Census Bureau data similarly shows older population cohorts are expected to grow at a faster rate than younger age cohorts. More specifically, the Census Bureau projects that adults aged 85 and older are expected to reach \~14 mln by 2040, representing a 72% increase over the roughly 6 mln adults aged 85 older as of 2022. From the standpoint of healthcare services, this transition is significant not solely due to population expansion, but also because medical care requirements, length of care, and dependence on support services escalate considerably beyond age 80, altering both the composition and magnitude of healthcare demand.

## Healthcare Spending Increases Significantly with Age

National Health Expenditure data shows that healthcare costs increase significantly with age and escalate further among the oldest age cohorts. For instance, in 2020, personal healthcare spending per capita for individuals aged 65 and older amounted to \$22,356, which is over five times the spending level for children and approximately 2.5 times that of working-age adults. Despite representing just 17% of the population, this age group accounted for \~37% of total healthcare expenditures in 2020. CMS data also reveals that per capita healthcare spending for adults aged 85 and older is even higher, averaging around \$36,000, exceeding the spending levels for younger seniors. This data underscores the notion that the demographic shift toward an aging population, particularly those aged 80 and above, creates a structural tailwind for healthcare spending, which is anticipated to further accelerate moving forward.

## However, The Type of Care Healthcare Utilized Changes with Increasing Age, Particularly at the 80+ Mark

As the population ages from 65 toward 80+, healthcare utilization shifts meaningfully from preventative and elective services toward more complex chronic disease management and higher-acuity care, driven by rising multi-morbidity and greater care coordination needs across settings. While younger seniors (65–74) remain in a “maintenance phase,” with spend concentrated in outpatient, physician, and drug utilization, the 75–84 cohort sees a notable step-up in inpatient admissions, specialist intensity, and post-acute utilization. This trend accelerates further in the 85+ population, where spending increasingly skews toward duration-based services such as skilled nursing, home health, hospice, and long-term services and supports (LTSS). Against this backdrop, aging demographics—already consuming healthcare at a multiple of the general population—should continue to drive incremental demand across the system, even as care delivery structurally shifts. Concurrently, a growing preference for “aging in

## Equities

Americas
Healthcare Providers

AJ Rice
Analyst
aj.rice@ubs.com
+1-212-713 4299

Steve Bock, CFA
HOLT Sector Specialist
steven.bock@ubs.com
+1-312-525 5724

James Kurek
Analyst
james.kurek@ubs.com
+1-212-713 3704

Ashley Minns
HOLT Sector Specialist
ashley.minns@ubs.com
+1-212-713 8120

Jonathan Yong
Analyst
jonathan.yong@ubs.com
+1-212-713 6268

Michael Wei
Associate Analyst
michael.wei@ubs.com
+1-212-713 2565

Joseph Overman
Associate Analyst
joseph.overman@ubs.com
+1-212-882 0086

place" (with a majority of seniors favoring home-based care) reinforces a secular tailwind for home health and community-based services, supported by cost considerations, social factors, and improved at-home care capabilities.

## SNFs, Home Health, Inpt Rehab, Hospice, Assisted Living, Funeral Homes To See a Positive Inflection Point

We expect post-acute settings to be a primary beneficiary of the growth in the over 80 population. This includes settings such as inpatient rehab facilities (IRFs), home health care, hospice, and skilled nursing facilities (SNFs), which we would expect to see volume benefits from the growth of this population, as these settings primarily care for an older patient cohort. Volumes to lower cost sites of care should also benefit from the fact that MCOs and payers are increasingly looking to control costs and, as such, likely to steer patients to these lower cost settings, such as home health care and skilled nursing facilities (SNFs). As such, we view home health, IRF, and skilled nursing operators as clear winners from this demographic trend. Areas like assisted living, hospice, personal care, and funeral homes are also likely to benefit. As a result, we are highlighting seven names we believe could benefit from the aging baby boomers over the next decade: Addus HomeCare Corporation (ADUS), BrightSpring Health Services (BTSG), Encompass Health (EHC), Ensign Group (ENSG), Health Care Services Group (HCSG), PACS Group (PACS) and Service Corporation (SCI). Non-covered stocks exposed to the theme include Brookdale Senior Living (BKD), Chemed (CHE) and Pennant Group (PNTG).

## The UBS HOLT Lens Provides Further Insight

In this report, we also leverage the UBS HOLT framework to supplement our analysis. UBS HOLT is an objective, cash flow-based framework for evaluating corporate performance and valuation that is independent of our fundamental analysis. Based on the HOLT Scorecard, this group screens favorably overall, with eight of ten companies ranking in the top half of the HOLT universe. Operational Quality is the strongest factor, with five firms in the top quintile (ADUS, BTSG, CHE, EHC, and SCI) supported by their high and stable Cash Flow Return on Investment (CFROI) profiles.

## ASSESSING THE IMPACT OF AN AGING POPULATION

## U.S. Population is Getting Older

The year 2026 marks a demographic inflection, as the first members of the Baby Boomer cohort (born 1946–1964) reach age 80. Although population aging has been a persistent trend, numerous demographic analyses highlight that outcomes, healthcare usage, and expenditures undergo significant shifts when individuals reach their 80s, setting this stage apart from the wider 65+ demographic. Brookings Institution research projects that the U.S. population aged 80 and older will approximately double between the mid 2020s and mid 2040s, rising from roughly 15 million to nearly 30 mln individuals. U.S. Census Bureau data similarly shows older population cohorts are expected to grow at a faster rate than younger age cohorts. More specifically, the Census Bureau projects that adults aged 85 and older are expected to reach \~14 mln by 2040, representing a 72% increase over the roughly 6 mln adults aged 85 older as of 2022. From a healthcare services perspective, this shift is important not simply because of population growth, but because care needs, duration of care, and reliance on support services increase disproportionately after age 80, changing both the mix and intensity of healthcare demand.

Figure 1: Adults in the U.S. Aged 85 Years and Older, in thousands  
![](images/92f9722d1e6cc42999f0ea5d23ebb65ddeed482f03cb7e3fdd8a044b0d9caa47.jpg)  
Source: Census Bureau and UBS; population in thousands

The U.S. population is also expected to see an increasing rate of chronic conditions among the population. Per Frontier Health, the number of people aged 50 years and older with at least one chronic disease is estimated to increase by 99.5% (to \~143 mln from \~72 mln in 2020) by 2050, while those with multi-morbidities are forecasted to increase just over 90% to 15 mln by 2050. Data from the Centers for Disease Control and Prevention found that 9 in 10 older U.S. adults report 1 or more chronic conditions, while \~79% of older adults had multiple chronic conditions.

Figure 2: Prevalence of Chronic Conditions Increases with Age  
![](images/9d901096fe7a7da00297f7245ca476c230e665c91d5029ea0f5d125f2dcc2a0f.jpg)  
Source: Centers for Disease Control

Figure 3: Trends in Chronic Conditions  
![](images/1c63fca29592654461d4dede5a641479d984cbd6356c35641a2f3e60d50cc8b9.jpg)  
Source: Centers for Disease Control

## Spending Rises Sharply with Advanced Age

With the increasing prevalence of chronic conditions, frailty, need for daily living assistance, etc., it is no surprise that healthcare spending increases with age. National Health Expenditure data provides clear evidence that healthcare spending rises steeply with age and accelerates further at the oldest ages. For example, personal healthcare spending for individuals aged 65 and older totaled \$22,356 (per capita) in 2020, more than five times the level for children and roughly 2.5 times that of working age adults. The age cohort also accounted for the smallest portion of the population (e.g. 17%), but accounted for \~37% of all healthcare spending in 2020. CMS tables show that per capita healthcare spending for adults aged 85 and older is even more elevated, reaching \~\$36,000, substantially higher than for younger seniors. Although individuals 85+ represent a relatively small share of the total population, they account for a disproportionately large share of total personal healthcare expenditures. This data supports the premise that the aging of the population into the 80+ cohort creates a structural spending tailwind, which we expect to accelerate moving forward. While not the only contributor to expectations for increased healthcare costs in the U.S., we do believe the aging baby boomers are one of the drivers of the growing total of healthcare expenditures in the country. CMS's National Healthcare Expenditure data forecasts healthcare expenditures growing to \~\$9 trillion by 2034, representing a 5.4% CAGR (2025-2034). CMS notes that this growth is projected to outpace that of average GDP growth (\~4%), resulting in an increase in the health spending share of GDP from \~18% to \~21% by 2034.

Figure 4: Total Personal Health Care Per-capita Spending by Age Group  
![](images/2224d23c50202a845edfa6d118a7924bf99b4fc4ae912985712af9cb0092fd15.jpg)  
Source: Census Bureau and UBS

Figure 5: U.S. Healthcare Expenditure Projections  
![](images/692e39163b6d5d955616a23da3f0d310bc0b04045ae8bc9910b931a13eb1bbe6.jpg)  
Source: CMS

## Seniors Healthcare Utilization Changes as They Age

As seniors transition from age 65 toward 80 years of age, healthcare utilization shifts materially from preventative care and elective procedures toward the intensive management of chronic disease and higher-acuity treatment. This reflects the growing burden of multi-morbidity, which increases both the frequency and complexity of care encounters, driving higher utilization across primary, specialty, and coordinated care settings. Industry commentary underscores that aging cohorts require progressively greater chronic disease management and higher-intensity interventions, and this dynamic is amplified by the fact that individuals aged 65+ already utilize healthcare services at a multiple of the general population. As a result, the aging demographic will only serve to increase demand of healthcare resources and services in the U.S. At the same time, care delivery continues to migrate toward outpatient and ambulatory settings in earlier stages of the aging curve, reflecting both clinical preference and improved outcomes in lower-acuity environments.

Importantly, the increase in spending with age is not purely a volume story but reflects a fundamental rotation in the mix of care delivered. In the 65–74 cohort, spending is still dominated by outpatient, physician, and drug utilization consistent with a “maintenance phase” of chronic disease management, with limited reliance on institutional care. By ages 75–84, rising multi-morbidity drives a step-up in inpatient admissions and specialist intensity, alongside a growing role for post-acute services as more patients are discharged to rehabilitation and skilled nursing settings. The most pronounced shift occurs in the 85+ cohort, where spending becomes increasingly concentrated in post-acute and supportive care categories, including skilled nursing facilities (SNFs), home health, and hospice. At this stage, cost growth is driven less by discrete clinical interventions and more by duration-based utilization, including SNF days, home health episodes, and end-of-life care, as well as long-term services and supports (LTSS).

## IMPLICATIONS FOR HEALTHCARE SERVICES

## Site of Care Shifts to Benefit Post-Acute Settings

We expect post-acute settings to be a primary beneficiary of an aging population. This includes settings such as inpatient rehab facilities (IRFs), home health care, hospice, and skilled nursing facilities (SNFs), which we expect to see volume benefits from an aging population, as these settings primarily care for an older patient cohort. Volumes to lower cost sites of care should also benefit from the fact that MCOs and payers are increasingly looking to control costs and, as such, likely to steer patients to these lower cost settings.

Home Health viewed as one of the biggest beneficiaries: As MCOs and state/federal funded agencies look to optimize treatment and cost efficiency, home-based care have emerged as beneficiaries given their lower cost. As seen below, home health care is up to 13x cheaper than the most expensive treatment solutions. Furthermore, research suggests that the benefits to home-based care are not just financial. Indeed, home based care has been shown to be less costly and importantly result in fewer readmissions relative to hospital care according to a study published in the National Library of Medicine (see here). In addition, the National Library of Medicine estimates that there is roughly \$41 bln in annual avoidable costs related to patients readmitted within 30 days after discharge. Furthermore, a study published in the American Journal of Managed Care found that patients who received home health care had a 60% lower risk of readmission.

Figure 6: Per Day Treatment Cost based on Site of Care Setting  
![](images/8cf30d461506c143d1f2659b45d27750e034dd9ee7132538b8c9d90736f7b8c7.jpg)  
Source: Company reports and Genworth Cost of Care Survey

Figure 7: Share of Post-Acute Discharges for Medicare Fee-for-Service  
![](images/8c364b66b29139d448c5403a354b56c39096a529fd505b329804947aa76a763b.jpg)  
Source: MedPac Databook

Acute Hospital Care at Home episodes were also associated with lower Medicare spending in the 30-day post-discharge period across more than half of the top 25 Medicare Severity Diagnosis Related Groups (MS-DRGs) compared to traditional inpatient episodes. All this goes to support the cost-efficiency and increased attractiveness of home-based care for payors, patients, and providers. It is unsurprising, therefore, that McKinsey estimates up to \$265 bln worth of care currently delivered in traditional facilities for FFS and MA beneficiaries could shift to 

[中间内容因长度限制已省略]

and/or Market Counterparties only as classified under the DFSA rulebook. It should not be distributed to Retail Clients. The Investment Research is provided for information purposes only and is not a recommendation or offer to buy/sell/hold a particular investment. The investment research may be out of date. You should seek investment advice before acting on the basis of the Investment Research. Abu Dhabi: UBS AG Abu Dhabi Branch is licensed and regulated by the Financial Services Regulatory Authority ("FSRA") of the Abu Dhabi Global Market. This material is intended solely for professional clients or market counterparties, as defined in the rules of the FSRA. It is not directed at, nor intended for, retail clients or any person who does not meet the criteria of a professional client or market counterparty. United Kingdom: This document is issued by UBS Wealth Management, a division of UBS AG which is authorised and regulated by the Financial Market Supervisory Authority in Switzerland. In the United Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.
"""
