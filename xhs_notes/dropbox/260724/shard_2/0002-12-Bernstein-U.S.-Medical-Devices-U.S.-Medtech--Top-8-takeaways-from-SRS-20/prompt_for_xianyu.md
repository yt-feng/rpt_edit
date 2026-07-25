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
U.S. Medical Devices

# U.S. Medtech: Top 8 takeaways from SRS 2026; plus thoughts on JNJ Ottava clearance and continued ISRG weakness

![](images/f7a238e5e254b6789ff2e3d552ff6a9b5a11df83080ca31bb4e78e3258882c35.jpg)

Lee Hambright

+1 917 344 8429

lee.hambright@bernsteinsg.com

![](images/0070b2c471f977e0db4ec6920d23d4ec8b9707ec86ff3fe2efe891154c448c41.jpg)

Adam Chow

+1 212 845 7820

adam.chow@bernsteinsg.com

Specialist Sales

![](images/fa388e2c6e099085c6f44efd4470642b9778f036b79f5659c4db59318576e6b5.jpg)

Christian Moore

+1 917 344 8555

christian.moore@bernsteinsg.com

Yesterday, we attended investor day sessions at the first day of SRS 2026, the Society of Robotic Surgery's annual conference. Hot topics included artificial intelligence, the shift to ASCs, new competitors, and telesurgery. We highlight our top 8 takeaways below, and then we share more detailed thoughts from fireside chats with JNJ, MDT and ISRG. Bottom line: Near-term concerns have created an incredibly attractive entry point for ISRG, and stepping back at SRS to consider the longer-term opportunities in the space just serves to deepen our conviction in the ISRG story.

(1) Long runway for growth in soft-tissue robotics. Last week, Intuitive's 2Q26 earnings reignited a debate about the durability of procedure growth in the U.S. market. After the first day of SRS 2026, we came away with a sense that the journey is just beginning for soft-tissue robotic-assisted surgery. Surgeons, hospitals and medtech management teams all highlighted the enormity of the opportunity ahead. We heard an overwhelming sense of excitement about newer applications for soft-tissue robotics (e.g., cardiac, after-hours, benign general, benign GYN, ASCs, endoluminal, and single-port) as well as a recognition that there is more work to be done to fully unlock the opportunity within current applications. We expect to hear more about all these opportunities in the clinical sessions over the remaining days of the conference.

(2) High barriers to entry are getting higher with AI. Competing in soft-tissue robotics is not just about building a competitive piece of equipment that sits in the operating room. Over the last 30 years, Intuitive has spent billions of dollars investing not just in hardware but in a broader ecosystem of value (integrated systems, software, data and insights, workflows, training, service and support, etc.). Listening to hospital leadership teams and influential surgeons at the conference, it's clear to us that these investments have paid off in elevating the basis of competition in the space. While there is openness to considering new technology from JNJ/MDT/others, it's clear that ISRG has set the bar very high—to get real traction, newer platforms will have to solve problems that aren't being solved today. We also heard A LOT of discussion about artificial intelligence can raise the bar even higher by helping hospitals turn data into useful insights, and ISRG is clearly ahead of the pack on this front.

(3) JNJ Ottawa clearance. JNJ reached a major milestone this week with FDA clearance for Ottawa as the “world’s first table-integrated soft-tissue robotic system.” Management highlighted Ottawa’s (a) 30%-50% smaller footprint, (b) synchronized motion of the table and arms (twin motion), (c) proven Ethicon instruments, (d) Polyphonic open digital ecosystem, and (e) connection to J&J’s legacy in continuous education and customer support. JNJ views the global soft-tissue robotic surgery market as being \~8% penetrated, and they see Ottawa as a market-expanding technology. Medtronic has been ahead of JNJ with Hugo clearances in Europe in Oct 2021 and the U.S. in Dec 2025. Nevertheless, given the features and benefits that Ottawa brings to the table, JNJ may ultimately close the gap with MDT despite Hugo’s earlier market entry—assuming JNJ can navigate the well-documented execution challenges inherent in launching surgical robotics platforms... [continued on p3]

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2"></td><td colspan="4">22 Jul 2026</td><td>TTM</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td colspan="2"></td><td rowspan="2">Closing Price</td><td rowspan="2">Price Target</td><td rowspan="2">Rel. Perf.</td><td rowspan="2">Cur</td><td rowspan="2">2025A</td><td rowspan="2">2026E</td><td rowspan="2">2027E</td><td rowspan="2">2025A</td><td rowspan="2">2026E</td><td rowspan="2">2027E</td></tr><tr><td>Ticker</td><td>Rating</td><td>Cur</td></tr><tr><td>ISRG (Intuitive Surgical)</td><td>O</td><td>USD</td><td>340.69</td><td>685.00</td><td>(51.0)%</td><td>USD</td><td>8.93</td><td>11.08</td><td>12.71</td><td>38.1</td><td>30.7</td><td>26.8</td></tr><tr><td>JNJ (J&amp;J)</td><td>M</td><td>USD</td><td>255.63</td><td>261.00</td><td>32.3%</td><td>USD</td><td>10.75</td><td>11.65</td><td>12.81</td><td>23.8</td><td>21.9</td><td>20.0</td></tr><tr><td>MDT (Medtronic)</td><td>O</td><td>USD</td><td>81.89</td><td>97.00</td><td>(29.8)%</td><td>USD</td><td>5.53</td><td>5.97</td><td>6.44</td><td>14.8</td><td>13.7</td><td>12.7</td></tr><tr><td>SYK (Stryker)</td><td>O</td><td>USD</td><td>309.24</td><td>410.00</td><td>(41.7)%</td><td>USD</td><td>13.66</td><td>14.98</td><td>16.72</td><td>22.6</td><td>20.6</td><td>18.5</td></tr><tr><td>SPX</td><td></td><td></td><td>7,498.96</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

MDT base year is 2026;

Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We rate ISRG, MDT, and SYK Outperform. We rate JNJ Market-Perform.

Our models can be downloaded here: ISRG \* JNJ \* MDT \* SYK

## RECENT RESEARCH

17 Jul 2026 - Intuitive Surgical 2Q26: Reviving debates on U.S. growth trend

17 Jul 2026 - Abbott 2Q26: EPS beat and raise on in-line sales, and a vehement defense of medtech market health  
15 Jul 2026 - Johnson & Johnson 2Q26: Solid beat and raise, reassuring commentary on underlying medtech trends  
15 Jul 2026 - U.S. Medtech: Another step down after HCA pre-release; is there any relief in sight for the sector?  
26 Jun 2026 - Weekend Healthcare Pulse: Deadtech forever? Can Medtech recover?

## CONTEXT ON SOFT-TISSUE ROBOTICS PROGRAMS AT MDT AND JNJ

8 Nov 2023 - Johnson & Johnson: Our key takeaways from the OTTAVA soft tissue robotics update

20 Nov 2020 - Johnson & Johnson - Med Device analyst day recap; introducing the new "Ottava" robot

25 Sep 2019 - Medtronic: Our top 10 takeaways from yesterday's robotic-assisted surgery event; everybody wins

6 Sep 2019 - Intuitive Surgical: What do experts think about J&J's new surgical robot?

15 Aug 2019 - Intuitive Surgical: What do experts think about Medtronic's new surgical robot?

## DETAILS

[continued from p1]

(4) MDT Hugo update. We didn't hear much new news from MDT. Management framed Hugo as a flexible, cost-efficient robotic platform, leveraging modular design, an open console, and integration with MDT's Touch Surgery digital ecosystem, with AI-enabled intraoperative guidance as a key long-term focus. The company continues to pursue a measured U.S. rollout—initially in urology with planned expansion into general surgery and gynecology—while emphasizing bundled offerings and hospital partnerships rather than rapid system placements. Management believes increasing competition will expand robotic adoption from low penetration levels.

(5) SYK continues to be a wildcard. As the leader in hard-tissue orthopedic robotics with Mako, Stryker has made it clear over time that the company sees soft-tissue robotics as an attractive space. Management has also made it clear that Stryker has very strong capabilities in M&A and has been evaluating deals in the soft-tissue robotics space. At the same time, Stryker does not appear to be interested in competing head-to-head with Intuitive. Investors are intrigued about potential deals that could bring an ASC-focused soft-tissue robotics capability to Stryker (e.g., Distalmotion or Moon Surgical).

(6) ASCs in the spotlight. There was a lot of discussion about the continued migration of procedures away from hospital inpatient and outpatient settings toward ambulatory surgical centers (ASCs). Robotic platforms can help enable this transition by reducing variability and making procedures more repeatable. ASC customer needs are different (e.g., cost sensitivity, space constraints), so as Intuitive works to scale up in the ASC setting with refurbished Xi systems (XiR), attackers are rushing in with value propositions that are tailored to ASC needs.

(7) Not worried about remanufactured instruments. Surgeon and hospital panelists were frequently asked questions about whether they had tried or were trialing remanufactured instruments. The vast majority were not interested. While there is clearly interest in controlling costs in the hospital, several panelists framed some version of the question: "if you were performing the procedure on yourself or on your mother, which instruments would you choose?"

(8) Lots of talk on telesurgery. Telesurgery continues to be a hot topic, and it got plenty of air time during the first day of SRS. As ISRG noted during yesterday's fireside chat and again in their PR this morning, Intuitive believes telecollaboration technologies can help surgeons learn from one another, provide additional experience to local care teams, and expand access to specialized care. ISRG sees telesurgery as one example of how those capabilities may evolve in the future, and there is potential for telesurgery to address health equity issues globally.

Bottom line: Intuitive's 2Q26 earnings reignited a debate about the durability of U.S. procedure growth. Data points from other medtech/tools players have stoked investor concerns that ISRG may be uniquely exposed to pressures from declining ACA enrollment given the company's procedure mix (i.e., JNJ/ABT did not see any impact from ACA, data points from tools/Dx have been positive). These near-term concerns have created an incredibly attractive entry point for ISRG, and stepping back at SRS to consider the longer-term opportunities in the space just serves to deepen our conviction in the ISRG story.

## TAKEAWAYS FROM JNJ/MDT/ISRG

Below, we share more detailed thoughts on SRS 2026 fireside chats with management teams from JNJ, MDT and ISRG.

## Johnson & Johnson

J&J announced U.S. clearance for Ottawa yesterday, which came 4-5 months earlier than investors had expected, and management took questions during a fireside chat at SRS. IR has scheduled a conference call for investors at 8am ET on August 3 to discuss the announcement.

FDA clearance for Ottawa. In a press release issued yesterday, JNJ announced FDA De Novo authorization for Ottawa as the “world’s first table-integrated soft-tissue robotic system.” JNJ argues that Ottawa’s architecture—with arms built into the OR table—is designed to compress the OR footprint by roughly 30–50% versus current systems, freeing space and improving workflow, and uses “proven” Ethicon instruments integrated into the platform. The umbrella authorization covers multiple procedures in upper-abdominal general surgery, including Roux-en-Y gastric bypass, gastrectomy, cholecystectomy, splenectomy, gastric sleeve, small bowel resection, appendectomy, lysis of adhesions, fundoplication, and hiatal hernia repair.

JNJ has an ongoing clinical trial to add an inguinal hernia indication for Ottawa.

Key features of Ottawa. In addition to Ottawa's space-saving footprint and connection to JNJ's portfolio of trusted surgical instruments, the company emphasizes Ottawa's open digital ecosystem Polyphonic, which is intended to connect data and systems across sites and support AI-enabled insights. The PR emphasizes simple setup and twin motion, which is the synchronized motion of the table and arms, which can simplify patient repositioning intraoperatively for multi-quadrant access to the anatomy. A promotional video (click on second image from the top) highlights an “open” philosophy, Ottawa's smaller footprint, “automation from day one,” twin motion, proven instrument technology, and an open digital ecosystem. The company also highlights that Ottawa is backed by Johnson & Johnson's legacy in continuous education, with learning resources designed for new and experienced robotic surgeons.

Fireside chat takeaways. In a fireside chat at SRS, Tim Schmid (EVP and Worldwide Chairman of MedTech) and Hani Abouhalka (Company Group Chairman for Surgery) stressed that Ottawa's de novo pathway and lack of a predicate reflect a "truly unique" platform rather than an incremental variant. They stated J&J's ambition to remain a "leader in surgery," extending from open and laparoscopy into robotics, and they expect Ottawa to be a significant contributor to company growth "by the end of the decade." Abouhalka stressed the potential for Polyphnic digital platform to support education, performance analytics, collaborative surgery and further automation, and he highlighted system openness as a differentiator versus more closed incumbents.

Instrumentation. Management did not specify exactly what instrumentation would available on Ottawa at launch, though Abouhalka did refer to two instruments mentioned in the PR—a two-in-one needle driver designed to reduce unintended suture cutting, and monopolar curved scissors for consistent and complete cuts—as evidence of JNJ’s ability to deliver differentiated surgical instruments. From photos and videos posted on JNJ’s website, it wasn’t clear whether the latest-generation Dualto Energy System would be available on Ottawa at launch.

Launch details. After Medtronic initiated Hugo launch in South America and Europe before coming to the U.S., J&J will target the U.S. first for Ottawa launch, which the company has positioned as sign of their confidence that the platform is ready to compete. JNJ views the global soft-tissue robotic surgery market as being \~8% penetrated, and they see Ottawa as a market-expanding technology. Launch will be “thoughtful,” starting in selected U.S. centers to generate evidence and refine workflows, then expanding more broadly as software, instruments and indications iterate quickly. The team mentioned flexible commercial models and competitive pricing but did not give specifics.

## Medtronic

During a fireside chat at SRS, Matt Anderson (SVP and President, Surgical) outlined Medtronic's positioning and progress with the Hugo robotic-assisted surgery platform, emphasizing that increasing competition—highlighted by J&J's recent approval—should expand overall market adoption given robotic penetration remains in the single digits.

Key features of Hugo. Commercially, Medtronic is prioritizing flexible business models (capital sale, leasing, usage-based) and leveraging its large open/laparoscopic portfolio to create bundled value propositions. While pricing specifics were not disclosed, the company continues to position Hugo as a potentially lower-cost-per-procedure alternative over time. Differentiation centers on its modular architecture (offering OR flexibility), open console (enhancing collaboration), and integration with Medtronic's digital Touch Surgery ecosystem. This platform—already deployed in \~1,500 ORs—supports data, analytics, and emerging AI applications, including intraoperative guidance, which management views as a key long-term differentiator versus pure-play robotic systems. This week, MDT issued a press release highlighting some of the early features of Touch Surgery Aide, the company's next-generation compute platform for the operating room.

Hugo launch status. Medtronic is focused on a measured U.S. rollout, starti

[中间内容因长度限制已省略]

 you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient

makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
