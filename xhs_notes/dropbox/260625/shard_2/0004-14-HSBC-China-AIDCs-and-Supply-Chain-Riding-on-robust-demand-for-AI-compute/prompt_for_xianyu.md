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
# China AIDCs and Supply Chain

Riding on robust demand for AI compute

\- We expect demand for AI compute in 2028e to be 5x that of 2025's level as model training and inference needs grow...

\- ... benefiting leaders in AI data centres (AIDCs) and supply chain participants at various stages like switches

◆ Initiate on Range and Ruijie with Buy ratings in separate reports

Strong AI compute demand. We estimate China's AI compute demand to boom and reach c5GW by 2028, c5x more than 2025, driven by explosive demand for large language model training and inference. Domestic hyperscalers are rapidly boosting their capex, with the combined spending of ByteDance, Alibaba, and Tencent reaching RMB346bn in 2025 and set to more than double to over RMB700bn in 2026 (see Ex 6). This is still well below the spending intensity of US peers, indicating there's substantial growth potential. Leading AIDC operators and key supply chain participants (like switch vendors) should benefit.

AI network upgrades. We see the TAM for data centre switches – the high-speed traffic controllers of a network – reaching RMB118bn in 2030e, implying a 28% CAGR in 2025-30e, on 1) more layers being added to a network's structure given larger GPU clusters; 2) upgrades to switch port speed could boost product prices; and 3) scale-up switches (that connect GPUs within a rack) are new revenue drivers on rising penetration of SuperPOD. The shift to these SuperPOD cluster architecture raises technical barriers and boosts the value of specialised AIDC operators like Range whose market share we expect to reach 9% in 2028e vs 6% in 2025 in the domestic data centre space, and Ruijie's market share in China data centre switches should reach 24% in 2028e vs 21% in 2025.

Going global opportunities. Over the long term, domestic IDC operators have the potential to serve global inference demand via "token exports", leveraging China's model cost-efficiency, abundant low-cost green power in western China, and lower construction, mechanical and electrical equipment costs.

Prefer Range and Ruijie (both rated Buy). Benefiting from the AI compute boom, we expect robust AIDC revenue growth for Range, and a 43% 2025-28e EBITDA CAGR with improving margins. We expect Ruijie to gain market share in the fast-growing data centre switch market and expect its net margin to improve to 10% in 2028e vs 5% in 2025 given better economies of scale. See our initiation reports published today on Range and Ruijie.

Equities IT Services

China

Yiran Liu\* (Reg. No. S1700520040001)  
Head of A-share IT Software Research  
HSBC Qianhai Securities Limited  
yiran1.liu@hsbcqh.com.cn  
+86 10 5795 2349

Heng Zhang\* (Reg. No. S1700524050001)

Analyst, A-share IT Software Research

HSBC Qianhai Securities Limited

heng.zhang@hsbcqh.com.cn

+86 10 5795 2384

\* Employed by a non-US affiliate of HSBC Securities (USA) Inc, and is not registered/ qualified pursuant to FINRA regulations

Exhibit 1. Ratings, target prices, financials, and valuations of our preferred stocks

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Market CapUSDbn</td><td rowspan="2">3MADTVUSDm</td><td rowspan="2">TPLC</td><td rowspan="2">PriceLC</td><td rowspan="2">Rating</td><td rowspan="2">Upside</td><td colspan="2">EPS growth_</td><td colspan="2">Rev growth_</td><td colspan="2">__PE (x)_</td><td colspan="2">__PS (x)_</td><td colspan="2">PEG (x)</td><td colspan="2">__ROE</td></tr><tr><td>2026e</td><td>2027e</td><td>2026e</td><td>2027e</td><td>2026e</td><td>2027e</td><td>2026e</td><td>2027e</td><td>2026e</td><td>2027e</td><td>2026e</td><td>2027e</td></tr><tr><td>Range</td><td>300442 CH</td><td>20.7</td><td>697</td><td>111.00</td><td>85.18</td><td>Buy</td><td>30%</td><td>-45%</td><td>38%</td><td>39%</td><td>33%</td><td>51</td><td>37</td><td>17.8</td><td>13.3</td><td>0.9</td><td>18%</td><td>21%</td><td></td></tr><tr><td>Ruijie</td><td>301165 CH</td><td>11.2</td><td>141</td><td>89.00</td><td>67.80</td><td>Buy</td><td>31%</td><td>115%</td><td>27%</td><td>27%</td><td>26%</td><td>50</td><td>40</td><td>4.2</td><td>3.3</td><td>1.1</td><td>23%</td><td>30%</td><td></td></tr></table>

Source: Wind, HSBC Qianhai Securities estimates. Note: Priced at close of 18 June 2026. TP – target price; nm = not meaningful

## Disclosures & Disclaimer

This report must be read with the disclosures and the analyst certifications in the Disclosure appendix, and with the Disclaimer, which forms part of it.

Issuer of report: HSBC Qianhai Securities Limited

View HSBC Qianhai Securities at: https://www.research.hsbc.com

# Robust demand, limited supply

\- Strong token consumption brings robust demand for compute, benefiting AIDC players

\- Price increases in the GPU rental business (GPUaaS) are likely to continue with leaders gaining market share

◆ Next step is for tokens to keep going global

## Robust token consumption brings strong AIDC demand

## AIDC is the core infrastructure for AI compute

We believe AIDC is one of the key sections in the AI compute supply chain. As the physical infrastructure of compute, AIDCs process data and connect hardware to software.

Exhibit 2. AI compute supply chain: Data centres are key infrastructure  
![](images/fb0d837dc8184e4e51f16f5be56a861f01bb9737578c9bd69c7d619d89ecadbf.jpg)

Data Annotation

Source: Company data, HSBC Qianhai Securities

Data Governance

Large Models

Computer Vision

Speech Recognition

Machine Learning Platform

Applications Layer

Embodied Intelligence

AI Mobile Devices

AI Wearable Devices

Enterprise Services

Due to 1) strong AI demand and 2) limited GPU and AIDC capacity supply, the GPU rental (GPUaaS) business is quite popular in both China and US. Some traditional internet data centre (IDC)/AIDC players have moved into this business. We list several GPUaaS businesses below. In our view, GPUaaS provides multiple advantages compared to in-house built GPU infrastructure, including 1) easier/quicker access to high-end GPUs compared to self-built; and 2) less investment required as rental refers to Opex instead of Capex for enterprises.

Exhibit 3. Data centres and GPU leasing business model comparisons

<table><tr><td>Feature</td><td>Retail data centres</td><td>Wholesale / Hyperscale data centres</td><td>AI data centres</td><td>GPU rental (GPUaaS)</td><td>Neo-cloud (GPUaaS)</td><td>Hyperscale public cloud</td></tr><tr><td>Representative companies</td><td>VNET (VNET US), Sinnet (300383 CH)</td><td>GDS (GDS US/9698 HK), VNET (VNET), Range (300442 CH), Chindata (Hec 600673 CH), Baosight (600845 CH)</td><td>Range (300442 CH), Chindata (Hec 600673 CH), Baosight (600845 CH), BONC (300166 CH)</td><td>Range (300442 CH), Lettall Electronic (603629 CH), Sharetronic (300857 CH), Glory View (301396 CH), BONC (300166 CH), Dawei (600589 CH)</td><td>CoreWeave (CRWV US), Nebius (NBIS US)</td><td>AWS, Azure, AliCloud</td></tr><tr><td>Pricing model</td><td>Monthly operation fee</td><td>Monthly operation fee</td><td>Monthly operation fee</td><td>Monthly rental fee + Revenue sharing based on token consumption</td><td>Pay-As-You-Go/ On-demand saving plans (commitment) Preemptible virtual machines</td><td>Pay-As-You-Go/ On-demand saving plans (commitment)</td></tr><tr><td>Service description</td><td>Physical facility rights</td><td>Physical facility rights</td><td>Physical facility and hardware rights, deeply tuned network</td><td>Physical hardware rights</td><td>AI-native cloud services</td><td>General-purpose virtualized cloud resources</td></tr><tr><td>Own data centres?</td><td>Yes</td><td>Yes</td><td>Yes</td><td>No</td><td>Partially</td><td>Partially</td></tr><tr><td>Own servers?</td><td>No</td><td>No</td><td>Partially</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Network capability</td><td>Customer defined connectivity</td><td>Standard Ethernet at scale</td><td>Deeply tuned to support GPU clusters</td><td>Varies</td><td>Deeply tuned to support GPU clusters</td><td>Standardised SDN (software defined network)</td></tr><tr><td>Software support</td><td>Limited</td><td>Limited</td><td>Limited</td><td>Limited</td><td>AI containers, rendering &amp; inference</td><td>Full-stack (database, security, web, serverless)</td></tr><tr><td>Target market</td><td>General businesses</td><td>Hyperscalers, AI labs, large enterprises</td><td>AI labs, hyperscalers</td><td>AI labs, hyperscalers</td><td>AI labs, hyperscalers</td><td>General businesses</td></tr><tr><td>Contract terms</td><td>Short-to-long-term lease (1-10 years)</td><td>Long-term lease (e.g. 7-15 years)</td><td>Long-term lease (e.g. 3-5 years)</td><td>Short-to-long-term lease (e.g. 1-5 years)</td><td>Long-term lock-in but greater contractual flexibility</td><td>Highly flexible (pay-as-you-go by hour/second)</td></tr><tr><td>Key advantages</td><td>Cost-effective, reliable operations, scalable, good connectivity, proximity</td><td>Cost-effective, physical privacy, reliable operations, scalable, good connectivity</td><td>AI-optimized, physical privacy, reliable operations, scalable, good connectivity, advanced GPU access, high cluster performance</td><td>Advanced GPU access, high cluster performance</td><td>Advanced GPU access, high cluster performance, flexible contract terms</td><td>Global reach, versatile, instant scalability</td></tr></table>

Source: Company data, HSBC Qianhai Securities

## Strong compute demand to drive accelerated growth; we expect China intelligent compute to grow at a CAGR of $74\%$ over 2025-28e, reaching 5GW in 2028e

With more advanced model launches in 2026, token consumption has shown strong growth. Per National Data Administration, China's daily token consumption reached 140trn in March 2026, which is $40\%$ more vs December 2025. In addition, IDC estimates that global agent token usage will grow to 152,667 peta $(10^{15})$ in 2030e, vs 0.0005 peta in 2025. The rising penetration of generative artificial intelligence (GAI) and robust token usage growth potential brings strong demand for AI compute, and hence, CSPs/Internet companies have raised their capex. Notably, per company guidance and media reporting, China hyperscalers' total capex in 2026e is set to more than double to over cRMB700bn (see Ex 6).

As GAI penetration is still in the early stages, we expect the strong compute demand to persist and expect China intelligent compute (@FP16, or 16-bit binary floating-point computer number format) to grow to over 12 ZFLOPS (10^3 EFLOPS) in 2028e, close to 8x vs 2025 level. In addition, we expect China intelligent compute data centre demand to grow at a CAGR of $74\%$ over 2025-28e and to reach c5.4GW in 2028e. AIDC players that have more reserved/running capacity should benefit.

Exhibit 4. China daily token usage grew robustly over the last two years  
![](images/71f0ba3a78a7a6e9cd216d36279acf4f5eb1f4846c1906103bd8f800a24c3bba.jpg)  
Source: National Data Administration, HSBC Qianhai Securities

Exhibit 5. IDC estimates global agent token usage will grow to 152,667 peta in 2030e  
![](images/7d9041068ae7d770b34e0a4ab5544a9f3f3af61637ad650c2d54cf8f106bfee6.jpg)  
Source: IDC estimates, HSBC Qianhai Securities

Exhibit 6. China CSPs continue to raise their capex  
![](images/cd22078b11eb73b7e4284b20c28aa89a43be74d08a32286d8c7c57dbdf7a6368.jpg)  
Source: Company data (capex guidance), Reuters (23 Dec 2025), Bloomberg (May 2026), South China Morning Post (9 May 2026), HSBC Qianhai Securities

Exhibit 7. We expect China intelligent compute to grow to c12,354 EFLOPS (@FP16) in 2028e  
![](images/b9b85fa1b063e827f4b31741bc8ab7b28539442fc9cd3acea2123a53ca015099.jpg)  
Source: MIIT, CAICT, IDC, HSBC Qianhai Securities estimates

Exhibit 8. We expect China intelligent compute data centre demand to grow at a CAGR of 74% over 2025-28e and to reach c5.4GW in 2028e  
![](images/b0c78b4f914bbbd38aea0cb1709d1dd9babb3d0a42e2c12dd854e35ba7554846.jpg)  
Source: MIIT, CAICT, IDC, Nvidia, HSBC Qianhai Securities estimates

Based on 1) our above forecast for China's intelligent compute data centre capacity and the compute scale and pricing of mainstream NVIDIA GPU servers/compute trays, etc.; and 2) Range's annual data centre operation revenue per MW, we expect China's data centre market to reach RMB165bn in 2028. Specifically, we expect the AIDC market to grow at a CAGR of $78\%$ over 2025-28e, reaching RMB75bn on 2028e.

Exhibit 9. China third-party data centre TAM/growth  
![](images/17a631d43de27d09431fd2b28a4fe8082334d7b938bc872075ccd5f726addfaa.jpg)  
Source: MIIT, CAICT, IDC, Range company data, HSBC Qianhai Securities estimates

## Supply is the bottleneck; leaders to gain market share

We expect AIDC to face supply shortages; GPUaaS should see robust growth
Due to strong AI demand and given limited GPU and AIDC capacity supply, since 2025, the GPUaaS market saw continued price hikes. Note that the Nvidia H100 rental price has risen from RMB12/GPU/hour to RMB17/GPU/hour, up c40%. Meanwhile, leading CSPs have announced cloud services price rises as well.

A new AIDC buildout usually needs 18-24 months for construction and utilisation ramp-up (source: Range company data). Per third party AIDC capacity plans, we expect supply shortages to continue, and the GPU rental business should see continued growth. AIDC players providing GPU leasing services (such as Range and Hec, per Exhibit 3), will continue to enjoy benefits from tight supply.

Exhibit 10. H100 1-year rental price has continued to rise since 2026  
![](images/0a7bf5d2e19136a9d7144abf48ba196b3819a3e25c49c0120bf9a306977bdc0f.jpg)  
Source: SemiAnalysis GPU pricing index, HSBC Qianhai Securities

Exhibit 11. Nebius raised further its GPU rental prices in May 2026  
![](images/f641bb18ec6c25e67227cdd483bf25d9d3dfec8893a271947d3fbca6c482c551.jpg)  
Source: Nebius, HSBC Qianhai Securities

Exhibit 12. Many CSPs have announced cloud services price hikes since 1Q26

<table><tr><td>Company</td><td>Announcement date</td><td>Effective date</td><td>Adjusted services</td><td>Price hikes</td></tr><tr><td colspan="5">Chinese hyperscalers</td></tr><tr><td>Tencent Cloud</td><td>4/9/2026</td><td>5/9/2026</td><td>AI computing power, TKE native nodes and EMR</td><td>+5%</td></tr><tr><td>Tencent Cloud</td><td>3/11/2026</td><td>3/13/2026</td><td>Tencent HY2.0 Instruct/Think model token prices</td><td>+420%-+463%</td></tr><tr><td>Baidu Cloud</td><td>3/18/2026</td><td>4/18/2026</td><td>AI computing products and parallel file storage</td><td>+5%-+30%</td></tr><tr><td>AliCloud</td><td>4/15/2026</td><td>5/15/2026</td><td>Bailian MaaS platform model unit prices</td><td>+2%-+5%</td></tr><tr><td>AliCloud</td><td>4/14/2026</td><td>4/14/2026</td><td>DataWorks API quotas adjustment and usage based billings</td><td>Charging on excess usage</td></tr><tr><td>AliCloud</td><td>3/18/2026</td><td>4/18/2026</td><td>GPU computing services e.g. T-head Zhenwu 810E GPU</td><td>+5%-+34%</td></tr><tr><td>AliCloud</td><td>3/18/2026</td><td>4/18/2026</td><td>Cloud parallel file storage (AI computing version)</td><td>+30%</td></tr><tr><td>Ucloud</td><td>2/11/2026</td><td>3/1/2026</td><td>All products and services for contract renewals and new contract</td><td>+5%-+12%</td></tr><tr><td>Wangsu</td><td>2/1/2026</td><td>2/1/2026</td><td>CDN standard service traffic/CDN fast origin-pull traffic</td><td>+35%/+40%</td></tr><tr><td>Wangsu</td><td>2/1/2026</td><td>2/1/2026</td><td>Object storage service</td><td>+40%</td></tr><tr><td colspan="5">Overseas hyperscalers</td></tr><tr><td>Google Cloud</td><td>1/27/2026</td><td>5/1/2026</td><td>Networking services for CDN interconnect, direct peering and carrier peering (data transfer fees)</td><td>+100% for North America +60% for Europe +40% for Asia</td></tr><tr><td>Amazon AWS</td><td>1/23/2026</td><td>1/23/2026</td><td>EC2 machine learning capacity blocks</td><td>+15%</td></t

[中间内容因长度限制已省略]

ed to the applicable HSBC entity's terms and conditions and/or customer declaration for accessing research; and (iii) you have agreed to the terms and conditions of any other internet banking, online banking, mobile banking and/or investment services offered by that HSBC entity, through which you will access research publications (collectively with (ii), the "Terms"). If you do not meet the above eligibility requirements, please disregard this publication and, if you are a IWPB customer, please notify your Relationship Manager or call the relevant customer hotline. Distribution of this publication is the sole responsibility of the HSBC entity with whom you have agreed the Terms. Receipt of research publications is strictly subject to the Terms and any other conditions or disclaimers applicable to the provision of the publications that may be advised by IWPB. © Copyright 2026, HSBC Qianhai Securities Limited, ALL RIGHTS RESERVED. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, in any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of HSBC Qianhai Securities Limited.

# HSBC Qianhai Research Team

Head of Research, HSBC Qianhai Securities  
Steven Sun +86 755 8898 3158  
stevensun@hsbcqh.com.cn

## China Equity Strategy

Analyst, Head of China Equity Strategy Research  
Steven Sun +86 755 8898 3158 stevensun@hsbcqh.com.cn

Analyst, China Equity Strategy Research  
Jeffrey Xie +86 10 5795 2361  
jeffrey.p.xie@hsbcqh.com.cn

Analyst, China Equity Strategy Research
Neal Chen +86 21 5066 2066
neal.m.chen@hsbcqh.com.cn

Analyst, China Equity Strategy Research  
Lydia Li +86 21 5066 2022  
lydia.j.y.li@hsbcqh.com.cn

## Agriculture & Fishery

Analyst, Head of A-share Agriculture Research
Yihui Sha +86 21 5066 2004
yihui.sha@hsbcqh.com.cn

## Auto & Auto Parts

Analyst, China Autos Research  
Elaine Chen +86 10 5795 2364  
elaine.chen@hsbcqh.com.cn

Analyst, China Autos Research  
Michel Liu +86 10 5795 2351  
michel.m.liu@hsbcqh.com.cn

## Consumer

Analyst, Head of A-share Consumer Research
Kathy Song +86 21 5066 2007
kathy.l.h.song@hsbcqh.com.cn

Analyst, A-share Food & Beverage and Pulp & Paper Research  
Darron Xue +86 755 8898 3407  
darron.xue@hsbcqh.com.cn

Analyst, A-Share Consumer  
Li Quan +86 755 8898 3471  
li.quan@hsbcqh.com.cn

Analyst, A-Share Consumer
Doris Luo +86 755 8898 3161
doris.y.s.luo@hsbcqh.com.cn

Analyst, A-Share Consumer
Eric Liu +86 21 5066 2053
eric.x.c.liu@hsbcqh.com.cn

## Financials

Analyst, Head of A-share Financials Research
Angel Sun +86 21 5066 2015
angel.y.sun@hsbcqh.com.cn

## Industrials & Renewables

Analyst, Head of A-share Industrials & Renewables Research  
Corey Chan +86 21 5066 2001  
corey.chan@hsbcqh.com.cn

Analyst, A-share Industrials & Renewables Research  
Amy Hu +86 755 8898 3408  
ruo.lin.hu@hsbcqh.com.cn

Analyst, A-share Industrials & Renewables Research  
Dun Wang +86 21 5066 2027  
dun.wang@hsbcqh.com.cn

Analyst, A-share Industrials & Renewables Research
Echo Zhang +86 10 5795 2314
echo.x.zhang@hsbcqh.com.cn

Analyst, A-share Industrials & Renewables Research  
Gary Yao +86 21 5066 2078  
gary.x.d.yao@hsbcqh.com.cn

## Healthcare

Analyst, Head of China Healthcare Research
Linda Shu +86 755 8898 3246
linda.y.l.shu@hsbcqh.com.cn

Analyst, China Healthcare Research
Cindy Chai +86 21 5066 2005
cindy.x.r.chai@hsbcqh.com.cn

Analyst, China Healthcare Research
Oliver Wang +86 21 5066 2058
oliver.h.y.wang@hsbcqh.com.cn

Analyst, China Healthcare Research  
Andre Sun +86 21 5066 2034  
andre.h.j.sun@hsbcqh.com.cn

Associate Evie Liu

## Petrochemical & New Materials

Analyst, Head of A-share Petrochem & New Materials Research  
Yi Ru +86 21 5066 2008  
yi.ru@hsbcqh.com.cn

Analyst, A-share Petrochem & New Materials Research  
Jill Huang +86 21 5066 2024  
jill.q.huang@hsbcqh.com.cn

Telecoms, Media & Technology  
Analyst, A-share Technology Hardware Research  
Bingyi Zheng +86 21 5066 2028  
bingyi.zheng@hsbcqh.com.cn

Analyst, A-share Technology Hardware Research  
Cara Su +86 21 5066 2080  
cara.z.h.su@hsbcqh.com.cn

Associate Yongzhu Wang

Analyst, Head of A-share Media & Internet Research  
Jing Han +86 10 5795 2344  
jing01.han@hsbcqh.com.cn

Analyst, A-share Media & Internet Research  
Bruce Sun +86 10 5795 2357  
bruce.z.j.sun@hsbcqh.com.cn

Analyst, Head of A-share IT Software Research
Yiran Liu +86 10 5795 2349
yiran1.liu@hsbcqh.com.cn

Analyst, A-share IT Software Research  
Heng Zhang +86 10 5795 2384  
heng.zhang@hsbcqh.com.cn

## Transportation and Logistics

Analyst, Head of A-share Transportation & Logistics Research
David Wu +86 21 5066 2002
david.wu@hsbcqh.com.cn

Analyst, A-share Transportation & Logistics Research
William Sun +86 21 5066 2061
william.x.d.sun@hsbcqh.com.cn
"""
