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
# Weekend Healthcare Pulse: Global medical imaging - AI Innovation from the land of Silicon Valley

Susannah Ludwig +41 582 723 127 susannah.ludwig@bernsteinsg.com

Courtney Breen +1 917 344 8407 courtney.breen@bernsteinsg.com

Lee Hambright +1 917 344 8429 lee.hambright@bernsteinsg.com

Nandan Kulkarni +91 22 6842 1436 nandan.kulkarni@bernsteinsg.com

Delphine Le Louet +33 1 42 13 92 93 delphine.le-louet@bernsteinsg.com

Rebecca Liang, Ph.D. +852 2123 2656 rebecca.liang@bernsteinsg.com

William Pickering, MD +1 917 344 8340 william.pickering@bernsteinsg.com

Justin Smith +44 20 7762 5899 justin.smith@bernsteinsg.com

Miki Sogi, Ph.D. +81 3 6777 6991 miki.sogi@bernsteinsg.com

Lance Wilkes +1 917 344 8501 lance.wilkes@bernsteinsg.com

Jeffrey Walch +1 917 344 8613 jeffrey.walch@bernsteinsg.com

As AI and machine learning excel at pattern recognition and anomaly detection, image analysis is one of the healthcare segments best suited for adoption. Over the past decade, leading imaging companies, major technology firms, and a growing number of start-ups have introduced AI-driven tools aimed at improving both the speed and accuracy of lesion detection. In today's Weekend Healthcare Pulse, we examine several prominent start-ups and recently IPO-listed players in radiology, focusing on how they are using AI to enhance clinical workflows and the competitive dynamics between these players and the incumbent OEMs.

By Susannah Ludwig, Estelle Pang and Richard Hombach

## RADIOLOGY IS THE MOST ADVANCED SUBMARKET FOR AI ADOPTION IN MEDTECH

Radiology is widely regarded as the most advanced submarket for AI adoption within medtech, primarily because it involves a pattern recognition problem applied to vast volumes of medical images, supported by highly structured and repeatable workflows. Radiologists routinely interpret thousands of images across modalities such as CT, MRI, and X-ray, making the specialty particularly amenable to algorithmic assistance. In this context, AI offers clear and measurable efficiency gains by helping clinicians manage rising scan volumes, reducing reporting workloads, and prioritizing time sensitive cases more effectively.

AI applications are already being embedded across multiple stages of the radiology workflow. These include image acquisition, workflow coordination, post-processing analysis, as well as follow-up management and training (Exhibit 1). In the long-term, there is potential in transforming radiology from a discipline of qualitative interpretation to one of quantitative analysis. This shift is often referred to as radiomics. But in imaging, and in medtech more broadly, AI's main impact in the near to medium-term will likely be more around speeding up workflows, increasing the efficiency of radiology suites, reducing errors, and improving the accuracy of

diagnosis.

EXHIBIT 1: AI application in Diagnostic Imaging

## AI IN DIAGNOSTIC IMAGING

## CENTRALIZED PLATFORM (IIOT)

## IMAGE ACQUISITION

• Patient positioning for MRI  
• Optimal use of contrast agents  
- Faster MRI scan times through under-sampling and reconstruction  
• Coordination of AI applications  
• Post-acquisition assessment prioritization  
• Information management / Treatment planning  
- Coordination of AI applications

Real time scan quality analysis

• Automatic labelling of anatomy (e.g. adjacent organs at risk)  
• Automatic identification of lesions  
• Additional measurements and metrics

## DIAGNOSTIC AIDS (CADx)

• Identifying areas of concern for further investigation (e.g. U/S for fatty liver disease)  
• Identifying aggressive forms of tumour (e.g. in prostate cancer)  
• Suggesting relevant elements of patient history or clinically similar historic cases

One highly skilled radiologist can only train a limited number of new radiologists in one location  
If the skilled radiologist trains an AI tool, then that AI tool can be used to train many more radiologists all over the world

Source: Bernstein analysis

## COVID-19 HAS BEEN A WAKE-UP CALL FOR HOSPITALS TO INVEST FOR EFFICIENCY

Prior to the pandemic, equipment and healthcare IT vendors often struggled to persuade hospitals to adopt new technologies. Many advanced software solutions were seen as useful but not essential, making it difficult to justify investment during procurement. This mindset shifted in 2020, when COVID-19 forced hospitals to rapidly expand ICU capacity and operate more efficiently to manage surging patient volumes. In the aftermath, radiology departments faced significant backlogs, with the pressure persisting as long-term trends continued to intensify. An aging population, as baby boomers move into higher-care years, is increasing demand for imaging services while ongoing staff shortages are pressuring capacity. As a result, the need for technologies that improve efficiency and streamline workflows in the radiology suite persists.

## AGING POPULATION SUSTAINING RADIOLOGY DEMAND

Demographic trends are set to provide a sustained tailwind for diagnostic imaging demand over the coming decade. Aging populations, in particular, are a primary driver, as older individuals typically require more frequent imaging procedures to manage chronic conditions and monitor disease progression. According to the World Bank, the population aged 65 and above is projected to grow at roughly +3% annually through 2030 in the US (Exhibit 2), while Europe is expected to see a growth rate of around +2% over the same period (Exhibit 3). As a result, the underlying demand for basic diagnostic imaging services is likely to remain robust in the medium-term, reinforcing the importance of workflow optimization solutions to help providers keep pace with rising volumes.

EXHIBIT 2: The U.S. senior population will grow at a 3% CAGR through 2030  
![](images/5027f7be2eb7a6d1cf8901fe4ebc713f722507cb35dc7b7114aec9755030894a.jpg)

<details>
<summary>bar chart</summary>

| Year | Number of people aged 65+ in the U.S. |
| ---- | ------------------------------------- |
| 2000 | 35                                    |
| 2005 | 38                                    |
| 2010 | 40                                    |
| 2015 | 45                                    |
| 2020 | 55                                    |
| 2025 | 65                                    |
| 2030 | 75                                    |
| 2035 | 80                                    |
| 2040 | 85                                    |
| 2045 | 90                                    |
| 2050 | 95                                    |
</details>

Source: World Bank estimates (>2020), Bernstein analysis

EXHIBIT 3: The European senior population will grow at a 2% CAGR through 2030  
![](images/e269193fc78bacfb54807a231b1628d908cc6370ee736a9cb84063b5d6ee38a7.jpg)

<details>
<summary>bar chart</summary>

| Year | Number of people aged 65+ in Europe |
| ---- | ----------------------------------- |
| 2000 | 50mn                                |
| 2005 | 58mn                                |
| 2010 | 63mn                                |
| 2015 | 68mn                                |
| 2020 | 74mn                                |
| 2025 | 80mn                                |
| 2030 | 88mn                                |
| 2035 | 94mn                                |
| 2040 | 99mn                                |
| 2045 | 102m                                |
| 2050 | 103m                                |
</details>

Source: World Bank estimates (>2020), Bernstein analysis

## AI CAN ALLEVIATE STAFFING SHORTAGES BY FREEING UP TIME FOR HOSPITAL STAFF

Labor shortages have been a persistent and structural challenge across healthcare systems, particularly in the United States, and continue to act as a key constraint on radiology throughput. According to the U.S. Health Resources and Services Administration's National Center for Health Workforce Analysis, supply growth of radiology physicians categories is expected to lag demand well into the 2030s. The gap between demand and supply is expected to reach -10% by 2034 (Exhibit 4). As a result, labor availability remains the primary bottleneck to improving imaging

volumes and reducing backlogs, meaning that efficiency gains will be critical to meeting growing demand.

EXHIBIT 4: The gap between U.S. demand and supply of physicians in radiology is expected to reach -10% by 2034  
Estimated supply and demand for radiology physicians (2024-2034E)  
![](images/d40fd5f4f409c21530b15f36292366f65a8abdb9bdba50ec32a4a4dc57bfc211.jpg)

<details>
<summary>line chart</summary>

| Year | Supply | Demand |
|------|--------|--------|
| 2024 | 42,500 | 43,000 |
| 2030 | 41,500 | 45,000 |
| 2034 | 41,500 | 45,500 |
</details>

Source: Projection from the US Department of Health and Human Services, Health Resources and Services Administration, Bernstein analysis

AI driven workflow innovation represents one of the most promising levers for alleviating these pressures. Rather than replacing clinical roles, AI has the potential to augment staff productivity by automating repetitive and time intensive tasks across the care pathway. According to a McKinsey industry report, AI could free up to 48% of a medical equipment preparer's time, or 23% for a pharmacist (Exhibit 5). Applied to radiology, similar gains in areas such as image triage, documentation, and coordination could meaningfully expand effective capacity without requiring proportional increases in headcount, positioning AI as a critical enabler of more resilient and scalable imaging workflows in the years ahead.

EXHIBIT 5: AI could free up a significant amount of time for hospital staff  
![](images/132620aff617c95987b65188fab1f2481ea881ad02f024102a0d8b9becfdbcfb.jpg)

<details>
<summary>bar chart</summary>

| Category | Percentage (%) |
| :--- | :--- |
| Medical equipment preparers | 48 |
| Medical assistants | 32 |
| Pharmacy technicians | 29 |
| Dental assistants | 26 |
| Pharmacists | 23 |
| Medical records and information technicians | 23 |
| Radiation therapists | 21 |
| Dietitians and nutritionists | 19 |
| Audiologists | 17 |
| Nurse anaesthetists | 16 |
| Surgeons | 7 |
| Opticians | 6 |
| Chiropractors | 2 |
</details>

Source: McKinsey Global Institute, Bernstein analysis

## LONG WAIT TIMES DRIVING NEED FOR EFFICIENCY IMPROVEMENTS

Long wait times have emerged as one of the most visible and pressing consequences of the structural constraints facing radiology, reinforcing the urgency for workflow efficiency improvements. The deferral of non-urgent procedures during the COVID pandemic created a substantial backlog that healthcare systems have struggled to unwind, even as operations normalize. Despite efforts to expand capacity through incremental hiring and equipment upgrades in the post-pandemic period, waiting lists in many regions remain elevated. The NHS provides a particularly clear example of this dynamic: the number of patients in England waiting more than six weeks for a CT or MRI scan surged from approximately 8,000 pre-pandemic to around 80,000 in 2020, and remains persistently high at roughly 75,000 in 2025 (Exhibit 6).

This sustained backlog underscores a fundamental challenge: healthcare systems face finite labor pools and slow-moving capacity expansion cycles, making it difficult to materially increase throughput through conventional means alone. As a result, reducing wait times is increasingly dependent on improving productivity within existing labor resources. This requires enabling the same number of radiologists and imaging systems to handle greater volumes, which in turn necessitates faster image acquisition, streamlined workflows, and more efficient interpretation. AI-enabled solutions are particularly well positioned to address these bottlenecks by accelerating scan protocols, automating prioritization of urgent cases, and reducing reporting turnaround times. Efficiency gains driven by AI are not merely incremental improvements, but a critical lever for addressing systemic delays and ensuring timely patient access to diagnostic services.

EXHIBIT 6: The number of patients who had to wait at least six weeks for a CT or an MRI more than quadrupled between 2019 and 2020, and continues to be elevated compared to pre-pandemic  
Patients waiting six weeks or more for a MRI or CT scan at NHS  
![](images/211ef5e20454e53b62b2e561326f0b592bbba50ff3bf8aa49ef9a70ea9784afa.jpg)

<details>
<summary>bar chart</summary>

| Year | MRI (in thousands) | CT (in thousands) |
| :--- | :--- | :--- |
| 2018 | 4.9 | 2.7 |
| 2019 | 5.7 | 3.6 |
| 2020 | 47.1 | 32.3 |
| 2021 | 55.0 | 29.3 |
| 2022 | 68.6 | 32.9 |
| 2023 | 58.8 | 27.7 |
| 2024 | 58.6 | 19.4 |
| 2025 | 57.6 | 18.9 |
</details>

Source: NHS website, Bernstein analysis

## HOW IS SILICON VALLEY STEPPING IN TO SOLVE THE PROBLEMS IN RADIOLOGY

## STARTUPS ARE ADVANCING IN AI-ENABLED SOFTWARE SOLUTIONS

Against the backdrop of mounting pressure on radiology departments, start-ups are stepping in to address these systemic inefficiencies through the development of advanced, AI-enabled software solutions. These firms are rethinking radiology workflows, from image acquisition to reporting and clinical decision support. By leveraging machine learning, automation, and cloud-based platforms, these technologies aim to streamline operations, reduce administrative burden, and enable radiologists to focus on higher-value clinical tasks. The following section highlights several leading startups at the forefront of this transformation, examining the specific challenges they target and the innovative approaches they are deploying to enhance efficiency across the radiology ecosystem.

## Radiology workflow

A typical radiology workflow follows a structured sequence that begins with patient registration, followed by the creation of an imaging order, scheduling, examinations, data archiving (typically in a Picture Archiving and Communication System (PACS)) and reporting review. (Exhibit 7).

EXHIBIT 7: A summary of radiology workflow  
![](images/857d268cfec226db42963e9b6ee0501aa2de30e98ebeefe07faa7f5ba702255f.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Patient Registration"] --> B["Imaging Order"]
  B --> C["Order Scheduling"]
  C --> D["Exam"]
  D --> E["Storage Archiving (PACS System)"]
  E --> F["Post-processing review"]
  F --> G["Radiology Workflow"]
```
</details>

Source: Bernstein analysis

## Storage archiving solutions

In recent years, many of the radiology workflow solutions have focused on the storage and archiving phase, particularly within PACS and adjacent systems. The PACS stores images captured from scanners, organizes them by patient and exam, and makes them instantly available on diagnostic workstations and other

screens inside or outside the hospital. This stage serves as a critical central hub where imaging data is aggregated, retrieved, and prepared for interpretation. AI-enabled solutions are increasingly being deployed here to enhance data management, automate image prioritization, and pre-analyze scans before radiologist review.

## Aidoc (April 2026 Series E, \$520m valuation)

Aidoc is a privately held company, headquartered in Israel. The company's core focus is AI-enabled analysis of CT and X-ray scans, embedded into the radiology workflow via its aiOS and CARE platforms (Exhibit 8), which plug into PACS and hospital systems to run “always-on” image analysis, triage acute findings, and coordinate downstream care teams in areas such as stroke, PE, cardiology, and oncology. This positions Aidoc not just as a point solution but as an enterprise orchestration layer spanning multiple service lines and modalities, differentiating it from vendors that sell single-indication algorithms.

EXHIBIT 8: Aidoc's aiOS platform provides a unified user interface

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
