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
European Biopharmaceuticals

# Pan-Euro Pharma Primer: 'protein strangling' (ATTR): why should AZN (O) lead in this \$20bn peak cardio market?

![](images/ff5f2e8434d29df3422a72468b1f7dd65ceacca6223b8e5e94e2488a4d6d0c72.jpg)

Justin Smith

+44 20 7762 5899

justin.smith@bernsteinsg.com

![](images/29502063f97e71ad25b4664351bf3c63e84df95a6413e6f2dca2d3809c54152c.jpg)

Shan Mian

+44 20 7676 8981

shan.mian@bernsteinsg.com

![](images/ca8e8b77b63262c32423011ff5eef172a748435fbed780bb1bbdcb66cc393eee.jpg)

Maximilian Brewster

+44 20 7550 2193

maximilian.brewster@bernsteinsg.com

Specialist Sales

![](images/1bfd4e356b8fbfbee46c7d368d0689cecc52f2d02c863b0c5f448ba472c54562.jpg)

Christian Moore

+1 917 344 8555

christian.moore@bernsteinsg.com

Despite the strong launch of Amvuttra (Alnylam; ALNY; O; Will Pickering; consensus peak \$9bn), 'protein strangling' of the heart (ATTR-CM) has a 5-year survival worse than many severe cancers as US diagnosis is just 25%. Consensus (Bloomberg throughout) projects ALNY & AZN to capture ATTR-CM peak shares of 55% and 12% respectively. But post expert calls, we see four reasons why AZN should lead in this \$20bn peak market, which would drive upside surprise for this stock 1/ AZN is the only company with all 3 validated drug mechanisms of action 2/ AZN's launches will materially expand the market as ATTR-CM is a very heterogeneous disease 3/ physician awareness of AZN's Alexion (rare disease) brand is already high 4/ the landmark phase 3 CardioTTRansform trial (out in 2H26) should be the most competitive dataset and thus make Wainua AZN's $2^{nd}$ largest non-oncology drug. Our new 2036e AZN ATTR of \$10bn implies 10% upside to the consensus group sales.

Why is ATTR relevant? Amyloidosis is the dangerous build-up of harmful proteins in vital internal organs which can be life-threatening. The most share price relevant amyloidosis sub-type is ATTR for which the greatest unmet medical need lies in the heart (ATTR-cardiomyopathy (CM); ca 800k sufferers in the G8) as the 5-year US survival rate is $<<40\%$ . Hence, ATTR-CM is often more of a ‘death sentence’ than many severe cancers.

Why ‘prime’ on ATTR-CM now? ALNY delivered an innovation ‘step-up’ via its 2025 launch of first in class gene silencer Amvuttra. Unlike earlier, ‘lower tech’ stabilizers (eg Vyndaqel (Pfizer; Courtney Breen; 2025 sales \$6bn), ‘higher tech’ silencers cut ATTR production. In 2H26 AZN will publish the landmark phase 3 cardioTTRransform data for Wainua (consensus peak \$2bn; guidance >\$5bn). Although the 2 $^{nd}$ silencer, we expect this drug to materially expand the market as 1/ ATTR-CM is very heterogeneous disease, so doctors need many different mechanisms to treat it (Wainua binds to genetic code (mRNA) whereas Amvuttra degrades it) 2/ US diagnosis of ATTR-CM is only 25%. But in our view, there are many examples of rare disease (RD) market expansion driven by new entrants. And Key Opinion Leaders (KOLs) have told us that AZN has invested heavily pre-launch. (Whilst ALNY’s twice yearly ‘Next Gen’ silencer nucesiran may ‘step-up’ convenience, we expect it to cannibalize Amvuttra. For nucesiran there no payaways to Sanofi (O)), which receives a blended mid-20’s royalty from sales of Amvuttra.

Who will lead in this \$20bn (10% CAGR) peak sales market? We think it's AZN for three reasons 1/ portfolio: AZN uniquely owns drugs with each of the proven mechanisms: stabilizer, silencer and depleter. Unlike silencers, depleters eradicate ATTR plaques & AZN's cliramitug (consensus peak \$2bn vs guidance \$3-5bn) is first in class with a projected 2029 launch. KOLs have opined to us that combination therapy will deliver the best outcomes (AZN plans studies of Wainua maintenance post climaritug induction, which would imply upside to our AZN base case forecasts) 2/ strongest legacy: in our view AZN's Alexion RD platform is a sustainable competitive advantage 3/ dataset: cardioTTRansform is the largest phase 3 trial with the most rigorous endpoint and has a 4-year lead over TRITON (nucesiran phase 3). If the Vyndamax pre-treated subgroup 'works' in cardioTTRansform there would be 34% upside to our base case 2036e Wainua of \$6bn.

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2"></td><td colspan="4">2 Jul 2026</td><td>TTM</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td>Rating</td><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Rel. Perf.</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>AZN.LN (AstraZeneca)</td><td>O</td><td>GBp</td><td>14,538</td><td>18,900</td><td>19.8%</td><td>USD</td><td>9.16</td><td>10.58</td><td>12.62</td><td>21.2</td><td>18.3</td><td>15.4</td></tr><tr><td>EDME</td><td></td><td></td><td>1,622.79</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

Source: Bloomberg, Bernstein estimates and analysis.

## Table Of Contents

Executive Summary - why should azn lead in a \$20bn peak non-oncology market?......4
Introduction to ATTR......6
How is ATTR Treated? - conventional (symptom relief only)......9
What Are Stabilisers?......10
What are Silencers?......11
siRNA Deep Dive......13
ASO Deep Dive......16
Stabilisers & Silencers - The Current Paradigm......18
Depleters - What Are They?......19
Why do we believe that aZN should Lead in ATTR-CM?......20
Why Are Our ATTR revenue Forecasts increasing and Why is this franchise now a Source of Positive Surprise for AZN?......23
The Bull Case - Combination, Combination, Combination......28

## DETAILS

## EXECUTIVE SUMMARY - WHY SHOULD AZN LEAD IN A \$20BN PEAK NON-ONCOLOGY MARKET?

Transthyretin amyloidosis (ATTR) is a disease where mis-folded proteins accumulate to cause life-threatening organ failure, most seriously in the heart (cardiomyopathy (ATTR-CM); ca 800k sufferers in the G8). Disease modifying treatments (unlike most drugs which alleviate symptoms) include stabilisers and more importantly gene silencers like Amvuttra (consensus peak \$9Bn) developed by Alnylam (Pickering; O). But mortality rates in ATTR-CM still mirror those in severe cancers, with US diagnosis rates of just 25%.

We've deep dived into ATTR-CM (by far the largest ATTR segment) because in 2H26 AZN will release the landmark phase III study (cardioTTRansform) for its silencer Wainua (peak guidance >\$5Bn vs peak consensus of \$2Bn). In our view, strong results would secure best in class status and make Wainua AZN's second largest non-oncology drug. In this primer, we've also prosecuted AZN's other promising ATTR-CM phase 3 drug (cliramitug; peak guidance \$3-5Bn vs consensus of \$2Bn) which has a new mechanism of action (depleter) and is first-in-class. Depleters uniquely remove the ATTR plaques which cause the debilitating symptoms in the heart.

EXHIBIT 1: Wainua: change to Bernstein global sales forecasts and comparison to consensus (\$m)  
![](images/11407fcb6c3b38e9ab550e0ea8aed8bebf03ec6cf34209049be065e37adbfd9a.jpg)  
Source: Bloomberg, Bernstein analysis & estimates

EXHIBIT 2: Cliramitug: change to Bernstein global sales forecasts and comparison to consensus (\$m)  
![](images/f15f7665a5ee22977b0718374a64702f2da3018e6d08c2f082844c6cb28b3de3.jpg)  
Source: Bloomberg, Bernstein analysis & estimates

## Why do we expect AstraZeneca to win in the \$20bn peak ATTR market (which offers a 10% CAGR to (26-36e))?

We believe that Wainua & cliramitug, plus AZN's commercialization of stabiliser Attruby in Japan (BridgeBio (Pickering;O), global peak sales \$4Bn) makes it the only company with a complete portfolio of ATTR drugs. Key Opinion Leaders (KOLs) have emphasized to us that a combination drug approach will yield the best results. In addition, post our channel checks with experts, we understand that AZN's Alexion Rare Disease legacy is an important competitive advantage in ATTR-CM.

Via thorough new bottom-up patient based modeling, corroborated by top-down US prescription data, we now increase our 2036e risk adjusted base case Wainua and cliramitug forecasts by 20% and 4x to \$6.2Bn and \$3.3Bn respectively (Exhibit 1; Exhibit 2). Considering Rare Disease precedents, we also now expect greater market expansion in ATTR. Our newfound enthusiasm for the depleter mechanism also means that we now expect AZN to capture more share in ATTR (Exhibit 3) and price cliramitug much higher. We also now think silencers are far tougher to ‘generic copycat’ due to higher barriers.

If the landmark phase 3 CardioTTRansform study proves that Wainua is more effective in silencer pre-treated patients it will take more share from Amvuttra, which lacks this data. In this bull case, our 2036e global Wainua forecast would increase by 37% to \$8.5bn for a 34% market share. This compares to a base case of 31% - 25% of US patients are currently diagnosed.

EXHIBIT 3: 2036 global ATTR market shares (by value): Bernstein old vs new estimates  
![](images/a2e5daf141694c029194ceec853c4d8dbf58afbffeea4937d3a26cc91368c88c.jpg)  
Includes ATTR-PN (polyneuropathy) and ATTR-CM (cardiomyopathy). Alnylam bar is Amvuttra (silencer); BridgeBio and Pfizer bars are both stabilisers (Attruby and Vyndamax respectively)

EXHIBIT 4: Bernstein global sales forecast like for like (\$m)  
![](images/4c616def2ab96100fd2e9bfa1d62a5281dbd47af95b14564e35616ca417ff085.jpg)  
Source: Bernstein analysis & estimates  
Source: Bernstein analysis & estimates, Bloomberg

Our upgraded Wainua sales forecasts (Exhibit 1; Exhibit 2) now reasonably imply a ramp up in line with Amvuttra (Exhibit 4). We acknowledge that Alnylam could deliver a step-change in convenience via the launch of its twice yearly ‘next gen’ silencer nuresiran in the early 2030s. Nonetheless, we believe that AZN will lead long term due to its portfolio approach and better data (4 point MACE endpoint in cardioTTR transform vs 3 point MACE endpoint for nuresiran in the TRITON phase 3).

Unlike Amvuttra, if nucesiran is approved no royalties would be payable by Alnylam to Sanofi (O). Hence, we think Alnylam's best path to maximize shareholder value is to drive the sales of nucesiran at the expense of Amvuttra (Exhibit 4). But consensus is assuming that the sales of nucesiran will be entirely supplemental to Amvuttra. We think this is unlikely, hence we expect intra-Alnylam cannibalization (Exhibit 5).

EXHIBIT 5: Consensus - ATTR global market share  
![](images/821244cbeac1addacbc09078e451d40803ebc555c7d5f544e8207c6b58728934.jpg)  
Includes both ATTR-PN (polyneuropathy) and ATTR-CM (cardiomyopathy). Alnylam includes nucesiran  
Source: Bloomberg, Bernstein analysis & estimates

EXHIBIT 6: Bernstein - ATTR global market share  
![](images/06b05fb86b18a9f58ff02a9ea52186cf77edaf093592fc5c999d0ead418d0c17.jpg)  
Includes both ATTR-PN (polyneuropathy) and ATTR-CM (cardiomyopathy). Alnylam includes nuresiran  
Source: Bernstein analysis & estimates

## INTRODUCTION TO ATTR

"Amyloidosis" is a broad term that refers to the build up of abnormal clumps of proteins (amyloids/fibrils) in various tissues of the body, thereby causing a wide range of potentially life threatening health problems. Amyloids can accumulate due to prolonged inflammation or genetic mutations that lead to the misfolding of diseased proteins thereby causing their aggregation and clumping. In all, there are estimated to be over 36 types of amyloidosis, specific to the type of protein that misfolds or the predisposing gene.

We are focusing specifically on transthyretin amyloidosis, or ATTR. This particular condition involves the misfolding of the transthyretin protein (TTR), which is normally synthesized in the liver and is involved in the transportation of thyroid proteins and vitamin A (essential for metabolism and vision) in the body.

The complex structure of the TTR protein lends itself to being easily misfolded. Therefore ATTR is the second most common cause of amyloidosis, making up around a third of all cases.

Scientists classify ATTR into two subtypes:

\- In hereditary ATTR (hATTR), 1 of over 120 gene variants that lead to protein misfolding is inherited from a biological parent. Those of African descent are known to carry a gene change predisposing to hATTR.

\- In wild-type ATTR (wATTR), the TTR protein starts misfolding spontaneously, either due to an acquired mutation or simply due to age related changes in cell structures responsible for healthy protein formation. As such, wATTR is more common over the age of 65.

Regardless of the type, the disease process ends up being similar, with the amyloid deposits accumulating everywhere in the body (Exhibit 7).

EXHIBIT 7: Common symptoms of ATTR  
![](images/1c7ac98e44f7b377d0398a96d3978a185e3ae3cdd539048ae07dc9b05159ce6e.jpg)  
Source: American Journal of Managed Care

When taken together, the sum of health problems caused by ATTR-CM results in 5 year survival rates from diagnosis in untreated patients of well under 50%.

Out of all the organ systems impacted by ATTR, two categories have emerged that represent the most common and clinically meaningful symptom sets that are associated with this disease.

EXHIBIT 8: Musculoskeletal, peripheral nerve, and autonomic nervous symptoms of ATTR-PN  
![](images/35cecedb0f2169716c6cd7eb0ab0c3028d10e412edd9d97f8246ad206e101229.jpg)  
Source: Heart Failure Reviews

## ATTR - polyneuropathy (ATTR-PN)

In this category, neurological symptoms prevail, with amyloid deposits predominantly affecting the nervous system and joints. In joints the amyloids cause pain, in peripheral nerves they can cause both pain and dysfunction of the nerves leading to muscle weakness. When affecting more centrally located nerves, the amyloids can cause “autonomic” symptoms, which lead to overall frailty and imbalance in the body’s nervous control (Exhibit 8).

The deposits of amyloid on the nerves are usually permanent, and their damage long-lasting. Hence, after diagnosis it's often a race against time to prevent irreversible symptomatic decline.

Polyneuropathy symptoms can be deeply unpleasant, and affect the quality of life of patients. Nevertheless, it is widely accepted by physicians that ATTR-PN is less likely to lead to mortality in patients than the cardiac equivalent of ATTR disease, as there is usually no key organ system involvement.

## ATTR- cardiomyopathy (ATTR-CM)

In this category amyloid deposits build up in heart tissue which cause debilitating symptoms. The amyloid fibrils can be toxic to the cardiac tissues. But more commonly the deposits just make it more difficult for the heart to perform its pumping action as the chambers of the heart become blocked with amyloid plaques. This leads to the muscles and walls of the heart enlarging to compensate (dilated cardiomyopathy), further worsening the blockage (Exhibit 9). Ultimately heart failure results, which leads to a well documented storm of symptoms including breathlessness and fluid congestion in the lungs as the heart is unable to perform its circulatory function. ATTR-CM can be more life-threatening than some forms of cancer.

Heart failure can also be caused by a variety of other health issues. Nevertheless, in ATTR-CM the precipitous decline in heart function accelerated by the constantly accumulating amyloid deposits often leads to rapid health deterioration and death. ATTR-CM is widely accepted as the more dangerous category of ATTR. As such, it dominates R&D into ATTR treatments, and is where, in our view, the majority of the potential market for innovative drug treatments exists in ATTR.

EXHIBIT 9: ATTR-CM pathophysiology  
![](images/ac5e6dd803762444776a2efaf72dc558920c8e09a2a406ddb988b69d7dbae2f6.jpg)  
Source: European Soc

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
