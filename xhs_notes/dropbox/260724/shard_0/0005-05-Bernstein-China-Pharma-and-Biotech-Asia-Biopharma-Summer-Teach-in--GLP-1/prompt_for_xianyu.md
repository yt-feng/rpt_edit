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
China Pharma and Biotech

# Asia Biopharma Summer Teach-in: GLP-1 and new approaches to metabolic management

![](images/a47a1d5102eced9227c45a9a83302a29823997f0e25b6a6ad32dd8c3a6574c4e.jpg)

Rebecca Liang, Ph.D.

+852 2123 2656

rebecca.liang@bernsteinsg.com

![](images/7fc314c9aad8663d352efc45bf28d5779c112e8e100a8f17f36cb03323643061.jpg)

Ellie Li

+852 2123 2621

ellie.li@bernsteinsg.com

![](images/554eb88058e8d5ad4b9d3a64a0419190ab4d30d48d05792076d638c23e585818.jpg)

Miki Sogi, Ph.D.

+81 3 6777 6991

miki.sogi@bernsteinsg.com

![](images/9a96159841801b10151f3f3fb6d2367ae74e1194553462acb41bc7366db415b3.jpg)

Tian Tan

+81 3 6777 6976

tian.tan@bernsteinsg.com

The obesity market is entering its next phase, where competition extends beyond weight loss efficacy. While next-generation injectable therapies have pushed placebo-adjusted weight loss beyond 20%, differentiation is increasingly shifting toward broader metabolic benefits, lean mass preservation, and convenience. We believe future winners will not only deliver superior weight reduction but also address cardiovascular, renal, liver, and body composition outcomes.

Oral GLP-1s and long-acting therapies are expanding the treatment toolbox. While injectable therapies continue to provide the strongest efficacy, oral GLP-1s are creating a compelling alternative for patients seeking easier administration and moderate weight loss. Lilly's Foundayo (orforglipron) and Novo Nordisk's oral semaglutide have demonstrated that oral therapies can achieve approximately 10% weight loss, which may be sufficient for many patients. Foundayo's small-molecule design provides additional convenience because it avoids the strict fasting requirements associated with peptide-based oral semaglutide. Among China-based programs, Innovent's IBI3032 has emerged as a notable contender after delivering placebo-adjusted weight loss of 8.6% in only four weeks, while weekly oral candidate IBI3042 highlights the industry's broader push toward reducing dosing frequency without sacrificing efficacy.

Emerging modalities aim to extend durability beyond traditional GLP-1 therapies. Antibody-peptide conjugates (APCs), circRNA therapeutics, and gene therapies are being developed to achieve monthly dosing or potentially long-lasting metabolic control following a single administration. Amgen's MariTide provides the most advanced proof-of-concept today, while Chinese innovators including Innovent and PegBio are actively building exposure to these next-generation platforms.

Despite pricing pressure, we continue to project a \~CNY85bn China GLP-1 market by 2030E. Despite accelerated price erosion and increasing regulatory scrutiny around obesity-drug prescribing, underlying demand remains robust. We have revised our market assumptions to reflect lower long-term pricing but higher penetration and a broader eligible population, resulting in an unchanged estimate of approximately CNY85bn for the China GLP-1 market by 2030E. A major launch wave beginning in 2027 should further expand patient access and accelerate market penetration. In our view, the industry's next stage of growth will be driven by a combination of efficacy, metabolic benefits, body composition, convenience, and affordability rather than any single attribute alone.

Note: Eli Lilly and Amgen are covered by Courtney Breen, Novo Nordisk is covered by Justin Smith.

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="3">23 Jul 2026</td><td colspan="2">TTMRel.</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Target Perf.</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td><td></td></tr><tr><td>9926.HK (Akeso)</td><td>M</td><td>HKD</td><td>102.80</td><td>130.00</td><td>(56.6)%</td><td>CNY</td><td>(0.60)</td><td>(0.52)</td><td>0.70</td><td>(146.9)</td><td>(172.1)</td><td>127.1</td><td></td></tr><tr><td>ONC (BeOne)</td><td>O</td><td>USD</td><td>319.93</td><td>412.00</td><td>(10.3)%</td><td>USD</td><td>2.63</td><td>5.65</td><td>8.93</td><td>121.6</td><td>56.6</td><td>35.8</td><td></td></tr><tr><td>1093.HK (CSPC)</td><td>M</td><td>HKD</td><td>8.37</td><td>10.70</td><td>(30.5)%</td><td>HKD</td><td>0.37</td><td>0.52</td><td>0.56</td><td>19.6</td><td>14.0</td><td>12.9</td><td></td></tr><tr><td>3692.HK (Hansoh)</td><td>O</td><td>HKD</td><td>32.58</td><td>44.00</td><td>(34.0)%</td><td>CNY</td><td>0.93</td><td>0.97</td><td>0.88</td><td>30.3</td><td>29.1</td><td>32.0</td><td></td></tr><tr><td>1801.HK (Innovent)</td><td>O</td><td>HKD</td><td>91.05</td><td>120.00</td><td>(24.8)%</td><td>HKD</td><td>0.48</td><td>0.71</td><td>2.90</td><td>187.7</td><td>128.3</td><td>31.4</td><td></td></tr><tr><td>600276.CH (Hengrui)</td><td>O</td><td>CNY</td><td>54.91</td><td>65.00</td><td>(32.2)%</td><td>CNY</td><td>1.18</td><td>1.42</td><td>1.78</td><td>46.5</td><td>38.8</td><td>30.8</td><td></td></tr><tr><td>6990.HK (Kelun-Biotech)</td><td>O</td><td>HKD</td><td>521.50</td><td>526.00</td><td>10.8%</td><td>CNY</td><td>(1.66)</td><td>(2.75)</td><td>0.85</td><td>44.9</td><td>45.6</td><td>28.1</td><td></td></tr><tr><td>1177.HK (Sino BioPh)</td><td>M</td><td>HKD</td><td>5.19</td><td>7.90</td><td>(50.7)%</td><td>CNY</td><td>0.19</td><td>0.20</td><td>0.22</td><td>23.4</td><td>22.0</td><td>20.2</td><td></td></tr><tr><td>9688.HK (Zai Lab)</td><td>M</td><td>HKD</td><td>16.03</td><td>15.00</td><td>(73.8)%</td><td>USD</td><td>(0.16)</td><td>(0.15)</td><td>(0.09)</td><td>0.5</td><td>0.5</td><td>0.4</td><td></td></tr><tr><td>ASIAX</td><td></td><td></td><td>1,907.19</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SPX</td><td></td><td></td><td>7,498.96</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended  
6990.HK, 9688.HK valuation is EV/Sales (x); 9926.HK, 1093.HK, 1177.HK base year is 2024;

Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We rate BeOne, Hansoh, Innovent, Hengrui, and Kelun-Biotech Outperform, and Akeso, CSPC, SBP, and Zai Lab Market-Perform.

## DETAILS

Traditionally, discussion around GLP-1 therapies has been dominated by clinical efficacy, safety, and commercial adoption. However, as the category expands beyond early adopters and moves toward a broader obesity and metabolic health market, it is equally important to understand how consumers themselves evaluate these products. To prepare for this GLP-1 teach-in, we reviewed a range of patient and consumer preference research and identified several themes that consistently emerge as the most important factors influencing treatment choice.

First, weight-loss efficacy remains the single most important attribute. Multiple studies suggest that patients are willing to tolerate, at least in the short term, gastrointestinal side effects if doing so translates into meaningfully greater weight loss. In other words, once safety is considered acceptable, efficacy often becomes the primary determinant of preference. This reflects the reality that many patients view weight reduction as the core therapeutic objective and are willing to make trade-offs to achieve better outcomes (source).

Second, consumers are increasingly focusing on metabolic and body composition benefits. Broader metabolic and body composition benefits are receiving increased attention. Metrics such as lean mass preservation, visceral fat reduction, and overall quality of weight loss are becoming important differentiators as consumers seek healthier and more sustainable outcomes rather than simply maximizing pounds lost (source1, source2).

Finally, convenience. Oral therapy has been an evolution after traditional subcutaneous forms, and companies are also exploring long-acting agents. Based on these themes, our GLP-1 teach-in will focus on these key areas that may shape the next phase of competition within the GLP-1 landscape.

EXHIBIT 1: Weight loss, convenience, body composition/metabolic benefits are the key investor preference when choosing GLP-1 products

![](images/1ea2accb9ecb02a5e964ef78e57a6fe82197b08d4e91e16cd8777ba445a6807f.jpg)  
Source: Diabetes Obes Metab, Patient Preference and Adherence, Scandinavian Journal of Primary Health Care, Patient Care, Bernstein analysis

## PART 1: WEIGHT LOSS EFFICACY AND EFFICIENCY

Efficacy benchmark in weight loss has evolved from -10% to more than -20% after placebo adjustment. Only a few years ago, the market viewed achieving more than 10% placebo-adjusted weight loss as a significant breakthrough, with semaglutide setting a new standard at approximately 12.4%. Since then, the pace of innovation has accelerated dramatically. Tirzepatide pushed placebo-adjusted weight loss close to 18%, while a new wave of next-generation candidates - including retatrutide, subcutaneous amycretin, enicepatide (CT-388), and CagriSema—have demonstrated placebo-adjusted weight loss exceeding 20% in clinical studies. As a result, the competitive landscape is entering a new phase where multiple therapies are capable of delivering similar levels of substantial weight reduction.

Note: Novo Nordisk and Roche are covered by Justin Smith; Eli Lilly and Pfizer are covered by Courtney Breen

EXHIBIT 2: Competitive landscape of subcutaneous GLP-1  
![](images/f90c198d46a04ed9057f2e493211ad88f7806008f3a0ec7b0f86981919d63f54.jpg)

1) Mazdutide's GLORY-2 (9mg) and CagriSema's REDEFINE-1 results at 2026 ADA are the same as previous reportings; 2) HS-20094: Likely not PBO-adj; Eli Lilly and Pfizer are covered by Breen Courtney, Novo Nordisk and Roche are covered by Justin Smith, BrightGene is not covered
Source: Company disclosure, ADA, EASD, Bernstein analysis

Among the key contenders, retatrutide delivered approximately 26.1% placebo-adjusted weight loss by Week 80, while subcutaneous amycretin and enicepatide (CT-388) achieved around 23.2% and 22.5%, respectively, by Weeks 36–48. CagriSema also demonstrated strong efficacy at roughly 20.4% placebo-adjusted weight loss by Week 68. Importantly, the differentiation is not limited to final weight-loss outcomes. The weight-loss trajectories show that these agents begin separating from one another relatively early in treatment, with some candidates demonstrating double-digit weight loss by approximately 16–24 weeks and continuing to widen the gap thereafter. This suggests that the new generation of therapies is not only achieving greater absolute weight loss, but also delivering meaningful efficacy at a faster pace (Exhibit 3).

Compared with semaglutide, which achieved approximately 12.4% placebo-adjusted weight loss at Week 68, the leading next-generation agents begin to show visible differentiation as early as the first few weeks of treatment and increasingly so by the 10–20 week timeframe. Mechanistically, this is consistent with the industry's shift from single-target GLP-1 agonism toward multi-target approaches that engage complementary metabolic pathways, such as GLP-1/GIP, GLP-1/amylin, or even triple G mechanisms. These therapies therefore appear to represent more than an incremental improvement on semaglutide; they reflect a broader enhancement in the intensity and breadth of metabolic regulation. From a commercial perspective, the earlier onset of efficacy may also be an important advantage. Patients who experience noticeable weight loss within the first several weeks of treatment are more likely to perceive the therapy as working, which could support better adherence, persistence, and ultimately long-term treatment retention.

EXHIBIT 3: Leading subcutaneous GLP-1s in the space achieve >20% weight loss, demonstrating superior efficacy from the early stages of treatment compared to semaglutide

Comparison of bodyweight % changes in GLP-1 clinical trials (PBO-adj)  
![](images/1cdf1873e296b8e46ee2472ed432ed338d6ba0f2775ce9855beac7e0e526f982.jpg)  
Source: Company disclosure, NEJM, Lancet, Bernstein analysis

## PART 2: METABOLIC BENEFITS

There is substantial patient overlap across obesity, diabetes, CKD, CVD, and MASH / MAFLD, with these conditions often coexisting as manifestations of shared underlying metabolic dysfunction. Obesity is a known risk factor and a common comorbidity for these diseases. For example, about 44% of individuals with CKD also have obesity, and 39% of obesity patients have MAFLD. Therefore, treatment of obesity with GLP-1 drugs have resulted in metabolic benefits that alleviated other diseases as mentioned (Exhibit 4).

EXHIBIT 4: Large overlapping population between obesity, diabetes, CKD, CVD, and MASH

Focus will remain on core therapy areas and prioritising unmet needs, including comorbidities

![](images/68366a1fa61a5871606752433d4c335065198d9ca7cfc1f40199dd02368a8154.jpg)  
Source: Novo Nordisk  
Patient overlaps for key focus areas in type 2 diabetes

![](images/c6100e9fea6c9bbddcee4ce2620dac138bf11d8a70bcbfa841910a9934a7d369.jpg)

The obesity market is increasingly evolving beyond weight loss alone, with GLP-1 therapies demonstrating benefits across a growing range of comorbidities including cardiovascular disease (CVD), chronic kidney disease (CKD), heart failure, MASH, and obstructive sleep apnea (OSA). Semaglutide has established the broadest evidence base to date, with approved indications and positive outcomes across cardiovascular, renal disease, and MASH, while tirzepatide has generated particularly strong data in MASH and OSA. These findings reinforce the view that obesity is a systemic disease and that GLP-1 therapies can deliver clinically meaningful benefits across multiple organ systems, potentially expanding the addressable patient population well beyond those seeking weight reduction alone.

Looking ahead, next-generation agents are aiming to further differentiate through enhanced efficacy and broader cardiometabolic benefits. Among the emerging therapies, mazdutide and retatrutide stand out, particularly in liver-related outcomes, with placebo-adjusted reductions in liver fat content of approximately 81% and 83%, respectively—substantially greater than those reported for semaglutide or tirzepatide. Retatrutide has also shown promising data in OSA and osteoarthritis, while several ongoing Phase 3 outcomes studies will determine whether these efficacy advantages translate into superior cardiovascular and renal protection. As the field matures, competition is likely to shift from weight loss alone toward a broader assessment of total metabolic benefit across obesity-related complications.

Trial completed and indication approved Trial with positive data but not yet approved Ongoing trials pending result  
EXHIBIT 5: Approved indications: CVD, CDK, MASH, OSA, and more players coming into the space

<table><tr><td rowspan="2">Medication</td><td colspan="9">Other metabolic benefits</td></tr><tr><td>CVD</td><td>HFpEF</td><td>CKD</td><td>UA reduction</td><td>MAFLD / MASLD</td><td>MASH</td><td>OSA</td><td>OA</td><td>AD</td></tr><tr><td rowspan="2">Semaglutide</td><td>(-20%/26% MACE risk)</td><td>(-7.8 in KCCQ-CSS)</td><td>(-24% kidney disease)</td><td></td><td>(-42% LFC reduction)</td><td>Fibrosis improvement: 37% vs 22% (PBO) ptsMASH resolution: 63% vs 34% (PBO) pts</td><td>(-52% in OSA incident)</td><td>(-14.2 WOMAC)</td><td>-</td></tr><tr><td>SELECT/SUSTAIN 6 (Ph3)</td><td>STEP HFpEF (Ph3)</td><td>FLOW (Ph3)</td><td></td><td>NCT02970942 (Ph2)</td><td>ESSENCE (Ph3)</td><td></td><td>STEP 9 (Ph3)</td><td></td></tr><tr><td rowspan="2">Tirzepatide</td><td>-</td><td>(-6.9 in KCCQ-CSS)</td><td>-</td><td>about -54μmol/L, ~48 after PBO-adj</td><td

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
