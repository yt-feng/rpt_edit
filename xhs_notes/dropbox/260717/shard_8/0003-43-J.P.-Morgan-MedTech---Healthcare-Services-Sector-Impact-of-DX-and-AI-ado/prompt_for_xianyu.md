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
# MedTech & Healthcare Services Sector

Impact of DX and AI adoption in healthcare: Initiatives that will lead to future market share gains are underway behind the scenes

Digital transformation (DX) and AI use seem to have recently advanced under the radar at healthcare facilities, and we summarize near-term implications. Within our coverage, we believe this could contribute to longer-term market share growth for monitors and other products in Nihon Kohden's digital healthcare solutions (DHS) segment, although the scale of this business is still small. In the healthcare services sector, M3 and JMDC are moving forward in using AI in various businesses, and while we expect longer-term contributions to enhancing competitive advantages and raising the profitability of new services, we focus on higher AI-related investment in the short term (increases in engineer hiring, AI system usage fees, and capex).

\- Implications for Nihon Kohden (6849): Nihon Kohden's medium-term business plan outlines a strategy to expand DHS sales by focusing on alarm solutions for medical staff providing inpatient care and on systems that facilitate inpatient monitoring and management. We expect the adoption of DX and AI in healthcare services to increase from July 2026 as Japanese hospitals use government subsidies to deploy ICT equipment and software to enhance the operational efficiency of healthcare facilities and improve workplace environments (application submissions are scheduled to open in June 2026). At Nihon Kohden, although the scale of sales for individual DHS products is not large, we believe the gradual recognition of its DHS products at US hospitals while it builds a deployment track record in Japan could contribute to raising its US market share for patient monitors (installed basis). In fact, new DHS products contributed to monitor sales growth in the US in FY2024, and with this potentially leading to large projects, we believe it is important from a longer-term perspective. Following the end of Covid-19-related special demand, Nihon Kohden had especially weak earnings and low valuations from FY2024 due to worsening market conditions in Japan and some overseas markets and to higher wages. However, it has been discontinuing low-profit businesses and implementing structural reforms since FY2025. In addition, Nihon Kohden's monitor sales in Japan resumed double-digit (\%) growth in YoY in 4Q FY2025, and as it seems that capex at Japanese hospitals is already showing signs of recovery, we expect the share price to rise toward 2Q FY2026 (Nihon Kohden said improved market conditions in Japan should fully contribute to earnings from 2H FY2026).

\- Changes needed at medical device manufacturers: Healthcare facilities have been moving quickly to experiment with DX and AI since the broader launch of generative AI services, and recent examples of DX and AI use at hospitals and clinics were presented at the Eucalia Friendship Meeting on July 4 (we summarize the takeaways from page 3). Japanese hospitals have been able to apply for subsidies under a government program to enhance operational efficiency and improve workplace environments since July 2026. The program offers subsidies up to ¥80 million per hospital to support the deployment of ICT equipment and software, including for communications equipment, AI

See page 11 for analyst certification and important disclosures, including non-US analyst disclosures.

Japan Equity Research
Medical Technologies & Services

Seiji Wakao, Ph.D.

seiji.wakao@JPM.com

JPM Securities Japan Co., Ltd.

medical consultation, generative AI document creation, conveyance robots, monitoring devices, and network infrastructure. However, with medical institutions introducing advanced computer and systems infrastructure for using AI (see our report here for initiatives by NVIDIA and others to provide healthcare AI infrastructure), it seems healthcare facilities are investing more than we expected in DX and AI. We believe the effective use of limited funds is important for healthcare facilities. Before Covid-19, there were a number of challenges in applying DX and AI to healthcare, including divergence with the actual needs of healthcare facilities, and issues related to precision, safety, ethics, and operations (Figure 15). Recently, however, the number of approved medical devices that use DX and AI has increased, and while we do not see problems with the products themselves, it seems to us that competing medical device manufacturers have released a growing number of similar AI products. In this environment, we believe a key issue now is whether products have the competitive advantages and unique features needed to make them the preferred choice of healthcare facilities. For example, Fukuda Denshi's electrocardiographs with AI analysis capabilities can perform AI diagnosis similar to competing products, but the ability to use this system with lower-performance computers is a unique advantage compared with competing products. With a recent focus on the risk of higher fixed costs for DX and AI deployment at healthcare facilities, we think medical device manufacturers, when developing products that use DX and AI, need to consider not only improving diagnostic and treatment capabilities, but also the capex burden for healthcare facilities.

## Rapidly accelerating adoption of DX and AI on the medical front

## Takeaways from meeting on DX and AI use on the medical front

The Eucalia Friendship Meeting on July 4 showcased many recent examples of the use of digital technologies and AI on the medical front from the perspective that hospital and clinic management should essentially maximize the time medical professionals spend with patients, leading to wide-ranging discussions. We summarize the main points below.

Figure 1: Clinical workflow support systems Japan market size  
![](images/6bf32670209a38f5c591f6c502a96dd628550d1dad1cd4e94e988b6de86d9f46.jpg)  
Source: Medley estimates, JPM
Note: Historical data are Medley estimates.

## (1) AI significantly reduces documentation time in medical practices

In one example at a hospital, use of AI enabled the generation of electronic medical records in less than sixty seconds by capturing the conversation between the patient and the medical professional through voice recognition and generating the text in the SOAP format (with subjective information, objective information, assessment, and plan of care). In addition, the use of Claude allowed medical professionals to compose routine emails and informational materials 1.8 times faster.

## (2) Some hospitals use proprietary data

The meeting showcased a hospital that created a dashboard for analyzing data in response to the medical fee revision in June 2026. Electronic medical records in particular are connected to various departmental systems, so the hospital plans to collect data from these systems and use them to improve operations and business efficiency.

## (3) Automation of medical paperwork not only reduces hospital business hours but also leads to retroactive billing for compensation

The future direction of medical administration was discussed. Hospitals and clinics have faced the issues of increased specialized work related to medical reimbursement claims and chronic labor shortages in recent years. The meeting highlighted an example of a hospital that reduced man-hours by 550 hours a month, the equivalent of 3.6 employees, by using robotic process automation (RPA) and automating medical administrative operations. This enabled all staff members to focus on reception and patient-facing work during the day rather than internal administrative tasks. By using RPA, the hospital also identified tens of millions of yen in medical claims that had previously been overlooked due to dependence on human skills, and was able to request retroactive reimbursements.

(4) AI agents could replace some of hospitals' reception operations and specialist classifications, possibly causing hospital and clinic capex to rise for AI use

The meeting showcased an AI agent co-developed by Fujitsu and NVIDIA for healthcare providers that helps receptionists assign specialists to patients. The product enables AI to take over tasks such as patient intake and interviews by standardizing previous intake interviews and letting patients speak with an AI avatar on a screen when arriving at the hospital. AI can also take over the task of assigning patients to appropriate specialists, automating a series of intake tasks previously performed by medical professionals. Going forward, the companies plan to screen patients on their smartphones by conducting interviews tailored to patients ahead of time, proposing a specialist to see, and advising whether an online visit is an option. These initiatives aim to facilitate a hospital's first contact with a patient. Because hospitals need computers with a certain level of sophistication to safely handle confidential medical data internally and use generative AI, we believe demand for desktop AI supercomputers might increase.

## (5) Prevalence of online medical visits

Online medical visits are currently the most widespread in China and India. In Japan, the majority of online visits are used at clinics, but hospitals often use doctor-to-doctor online service to allow cardiac surgeons and other physicians to collaborate with specialists at remote locations. The use of products such as Join, DeNA's app for communication between medical professionals, is increasing.

## The key question is whether digital solutions and AI functionality will be recognized and valued, ultimately driving an increase in device market share

Nihon Kohden: DHS's business scale still small, but focus is on whether it contributes to higher monitor share in North America

Nihon Kohden's medium-term plan strategy is to expand digital health solutions (DHS) sales to hospitals, and we expect new products including alarm solutions and next-generation central monitors to contribute to earnings from FY2026. At Japanese hospitals in particular, we expect increased use of the Japanese government's supplementary budget intended to improve operational efficiency and workplace environment on the medical front through the use of information and communications technology (ICT) equipment from July 2026 onward, increasing the use of digital technologies in medicine. We also believe the medical fee increase at hospitals from June 2026 has improved their business environment, providing some reassurance. We thus think this could provide some tailwinds to DHS product sales of Nihon Kohden's patient-monitoring business. While the scale of the company's DHS sales is still small, we believe the profit margin is better than that of equipment products. As a future focal point, while Philips and GE HealthCare now hold high shares in the US market, we believe what is important is whether Nihon Kohden's DHS is well received by hospitals and contributes to an increase in its patient monitoring systems' US share (on the basis of equipment installed).

Figure 2: Nihon Kohden: Key New Products and Services for Improving Hospital Management Efficiency and Healthcare Economics

<table><tr><td>Period</td><td>Region</td><td>Business</td><td>Products / Services</td></tr><tr><td>FY3/25</td><td></td><td>Solutions</td><td>Patient Condition Dashboard Software (for general wards)</td></tr><tr><td>FY3/25</td><td></td><td>Solutions</td><td>Patient Condition Dashboard Software (for critical care wards)</td></tr><tr><td>FY3/26</td><td></td><td>Solutions</td><td>Integrated Dashboard for PFM Center</td></tr><tr><td>FY3/26 2Q</td><td>U.S.</td><td>Solutions</td><td>Alarm Solution &quot;AlarmSense&quot;</td></tr><tr><td>FY3/26 3Q</td><td>Japan</td><td>Patient Monitors</td><td>Transmitter ZS-730/720P</td></tr><tr><td>FY3/26 4Q</td><td>Japan</td><td>Solutions</td><td>On-site Alarm Analysis Software</td></tr><tr><td>FY3/26 4Q</td><td>Japan</td><td>Solutions</td><td>Admission/Discharge Workflow Support Software</td></tr><tr><td>FY3/27</td><td>Europe</td><td>Solutions</td><td>Alarm Solution &quot;AlarmSense&quot;</td></tr><tr><td>FY3/27</td><td>U.S.</td><td>Patient Monitors</td><td>Next-generation Central Monitor</td></tr></table>

Source: Company data, company estimates, JPM  
Note: Solutions business = DHS (Digital Health Solutions) + ITS (IT Solutions); PFM (Patient Flow Management) Center: collects and analyzes in-hospital data in real time, and bed utilization and the patient intake/acceptance status are centrally managed in an integrated manner.

Figure 3: Nihon Kohden: DHS+ITS products Japan sales  
![](images/7d988509654122f7ea208bdaa79cd392eee95aa2205c8e0dd33fc2dfd48e5d08.jpg)  
Source: Company data, JPM

Figure 4: DHS products North America market size  
![](images/44dac741251a3aae85db7b89080d65cd87b519bf4ea9410d2cb372e0dbaf0699.jpg)  
Source: Nihon Kohden, Nihon Kohden estimates (from 2026), JPM

Figure 5: Nihon Kohden: Sales by type  
![](images/52457ee64b267c701d58d2b23b613430fe81d184f46e7c66f0b8ccffa58db2d4.jpg)  
Source: Company data, JPM estimates

Figure 6: Patient monitors global market shares (2024)  
![](images/34d26f736f64248390ed1d70fd55f04a3c4f0697e6486097aadd1f6070b40673.jpg)  
Source: Spherical Insights, Precedence Research, JPM

## Nihon Kohden: Solutions to reduce alarm fatigue among healthcare professionals at hospital wards

One of Nihon Kohden's strengths is its sensor technology for devices that measure patient biometrics such as blood oxygen saturation, exhaled carbon dioxide, pulse, and brainwaves. The company offers high-precision alarm management systems based on this information. When a hospitalized patient's alarm goes off now, a medical professional goes to the patient to verify the situation in person, but this has become an issue on the medical front, with some data suggesting that verification is unnecessary about 85% of the time (as of 2026, source: Nihon Kohden material). To solve this issue with alarms, Nihon Kohden provides alarm reports to the medical front (its service staff collects and analyzes alarm data offline and proposes operational improvement), launching an on-site alarm analysis software in FY2025. This software displays the occurrence and causes of alarms by patient in real time and on-site, making it easier to manage alarms on the medical front. On-site alarm analysis software QP-841N, launched in Japan in February 2026, is priced at ¥1.5 million, and the company expects to sell more than 100 sets by FY2028, mainly to Japanese healthcare providers. It plans to continue investing in R&D of high-precision alarm detection technology and provide full-scale consulting services for hospital ward alarm management (Figures 7-8).

Figure 7: Nihon Kohden: Alarm-state duration  
![](images/73f53c4fa2d35dba242a9d1df8b3aa0dc7dc1ac5ab73ae7c9831ac599857ce6c.jpg)  
Source: Company data (2026), JPM

Figure 8: Nihon Kohden: Alarm-sound duration  
![](images/87fd5682c54d7603f6866ed7210d8b15512590bcf1f603f12e9100639f97553b.jpg)  
Source: Company data (2026), JPM

## Fukuda Denshi: AI diagnostics raise detection rates of atrial fibrillation symptoms and contribute to prevention, can be used with non-high-end computers

Fukuda Denshi (Not Covered), which competes with Nihon Kohden, launched CardiMax 9 Ai (FCP-9900Ai system), an electrocardiograph with AI analysis function, in 2024. This system can estimate past atrial fibrillation, which was difficult to do with conventional electrocardiographs, and we believe it can contribute to early detection of atrial fibrillation risk and prevention of attacks. Fukuda's technology was featured in the July 2, 2026 edition of Nature (see here for the article). In addition, while several overseas competitors have also launched similar AI d

[中间内容因长度限制已省略]

ulatory regime thereunder. Opinions, forecasts or projections contained in this material represent JPM's current opinions or judgment as of the date of the material only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not
"""
