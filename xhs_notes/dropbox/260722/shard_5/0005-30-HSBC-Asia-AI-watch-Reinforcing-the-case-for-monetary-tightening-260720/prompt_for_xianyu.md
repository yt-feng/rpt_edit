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
# Asia AI watch

Reinforcing the case for monetary tightening

\- Asia’s growth is being lifted by AI hardware exports and data centre investment, while labour disruption is limited so far

\- AI is increasingly influencing Asia’s inflation dynamics, with upstream cost pressure feeding into broader prices over time

\- This backdrop may push some Asian central banks, such as those in Korea and Taiwan, towards tighter monetary policy

## Growth upside

Economics Asia

Artificial intelligence (AI) offers meaningful growth upside for many Asian economies. The most immediate channels are surging AI hardware exports – equivalent to almost half of GDP in Taiwan and Vietnam – and accelerating data centre investment, which is particularly prominent in Malaysia. Beyond these near-term catalysts, AI could also lift long-term growth potential through productivity gains.

## Labour disruption

AI's second-round effects have so far been modest: there have been no mass layoffs and no step-change in productivity. Drawing on an earnings call analysis, we find that mainland Chinese companies may face the most near-term labour disruption – potentially serving as a “canary in the coal mine” for other Asian economies. Across the region, AI adoption will displace some roles, but the impact can be mitigated by reskilling and redeployment. It’s also important to remember that AI can augment labour as well as substitute it, raising output per worker in many occupations.

## Inflation crosscurrents

Inflation dynamics in Asia are increasingly shaped by the AI build-out rather than the traditional oil-and-food cycle. As hyperscalers ramp up capex, demand is concentrating in a narrow set of inputs, pushing up upstream costs first and only later filtering into broader inflation via higher compute and services prices. The impact will vary, depending on where an economy sits in the AI tech stack – upstream hardware producers, midstream assemblers, or downstream adopters. Inflation risks look asymmetric: upstream suppliers, such as Korea and Taiwan, are likely to feel pressures earlier than downstream pure adopters, such as India and Indonesia.

## Central bank implications

The AI supercycle strengthens the case for tighter monetary policy in economies with meaningful AI-driven growth upside that sit upstream in the tech supply chain, and are, therefore, likely to see cost pressures first. Korea and Taiwan are two prime examples, where AI may tilt the balance towards further monetary tightening.

This is our latest report on the Disruptive Technology theme. If you want to subscribe to any of our nine big themes, click here.

## Disclosures & Disclaimer

This report must be read with the disclosures and the analyst certifications in the Disclosure appendix, and with the Disclaimer, which forms part of it.

## Justin Feng

The Hongkong and Shanghai Banking Corporation Limited
justin.feng@hsbc.com.hk
+852 22887108

## Frederic Neumann

Chief Asia Economist, Co-head Global Research Asia  
The Hongkong and Shanghai Banking Corporation Limited  
fredericneumann@hsbc.com.hk  
+852 2822 4556

## Mark McDonald

Head of AI and Data Science
HSBC Bank plc
mark.mcdonald@hsbcib.com
+44 20 7991 3119

## Thomas Devlin

Analyst, Data Science
HSBC Securities (USA) Inc.
thomas.devlin@us.hsbc.com
+1 212 525 0672

## Abanti Bhaumik

Associate Bangalore

2026 Extel Global Fixed-Income Research Survey
6 – 24 July
Click to vote

Issuer of report: The Hongkong and Shanghai Banking Corporation Limited

View HSBC Global Investment Research at: https://www.research.hsbc.com

## What AI means for Asian central banks

Asia's central bankers are confronting an unusually broad and fast-moving set of challenges.

The Middle East geopolitical situation remains fluid, creating uncertainties in energy and industrial supply chains for Asian economies. At the same time, the prospect of higher food and commodity prices linked to this year's El Niño, alongside US monetary policy uncertainty under new Federal Reserve Chair Kevin Warsh, is keeping Asian central banks on their toes (see The Fed, El Niño, and Al, 3 July 2026).

The AI boom – still running hot on the back of robust capex intentions from big tech – adds a further complication for policymakers.

## What are the AI theme's implications for Asian central bank policy?

For context, not every central bank is moving in the same direction. During the second half of 2026, we forecast rate hikes in Japan, Korea, Taiwan, India, Singapore, Indonesia, Vietnam, the Philippines, and New Zealand, while mainland China, Hong Kong, Malaysia, Thailand, Bangladesh, and Australia are expected to keep policy rates unchanged (see Asian Economics Quarterly: Still runnin', 24 June 2026).

If AI boosts productivity without materially lifting inflation, it would strengthen the case for holding rates steady. Conversely, if the AI data centre build-out functions more like a negative supply-side shock, it could reinforce the tightening bias for central banks planning to hike.

In this report, we examine what the AI boom could mean for Asian central banks during the current policy cycle by assessing how it may shape the growth, labour and inflation outlook across Asian economies over the next one to two years.

## Growth upside

AI promises to be a genuinely transformative technology, with far-reaching implications for real economic activity. In Asia, the first-round macro effects of the AI infrastructure build-out are already visible in surging exports and data centre investment. As Chart 1 shows, AI's growth impact is most evident in AI hardware exports – equivalent to nearly half of GDP in Taiwan and Vietnam – and in data centre investment, which is most prominent in Malaysia.

Chart 1: AI enabled exports (2025) and data centre capex\*  
![](images/11b8371cb9540bd63415d664abfdebd56ad2951f8861b34c855bc488b06303e5.jpg)  
Source: IMF, ITC Trade Map, Cushman & Wakefield, HSBC. Note: CH stands for mainland China. \*Data centre capex refers to the projected total investment required (including land cost) as of 2025 for the development pipeline expected to become operational by 2030.

Chart 2: US hyperscalers\* AI capex  
![](images/5efbdfbf3149257af299fbb8692a8ddb26a4a299c23fea15f0e2617b2d14233f.jpg)  
Source: Bloomberg, HSBC. Note: \*Amazon, Google, Meta, and Microsoft. 2026 figures represent company guidance as of 30 April 2026.

Chart 3: Global semiconductor sales  
![](images/1ff66b49943a1e41af09ed5e00d0b5e7a67f516e57cc1132ae5a3429f654956d.jpg)  
Source: Macrobond, HSBC

In 2022, when OpenAI released an early ChatGPT demo that sparked widespread public interest in consumer-facing AI (and, for Justin and Thomas, proved a genuinely life-changing moment as students), the four major US hyperscalers – Amazon, Google, Meta and Microsoft – spent around USD150bn on AI capex. As Chart 2 shows, that figure is expected to surge to well above USD700bn this year, $^{1}$ which is roughly the size of Sweden's entire GDP.

This spending frenzy is funding the AI infrastructure build-out across the stack, from semiconductor chips (see Chart 3) to data centre equipment, such as servers, fibre-optic networks and liquid-cooling systems.

Many Asian economies are highly exposed to these growth opportunities, especially through AI hardware exports or via data centre investments.

Taiwan is arguably the linchpin of the global AI ecosystem. Since the AI boom began, US-based Nvidia's Hopper (and later the Blackwell) GPUs (graphics processing units) have become the workhorses for both training and inference. Yet, as a fabless chip designer, Nvidia depends on Taiwan's TSMC for fabrication.

TSMC, the world's leading foundry (c70% market share) and the only company mass-producing leading-edge two nanometre (nm) chips at commercially viable yields, also manufactures chips for AMD (Nvidia's closest competitor) and for mainland Chinese clients at legacy nodes (28nm and above, due to US technology restrictions) via its Nanjing and Shanghai fabs. $^{2}$ This breadth of customer coverage underscores TSMC's centrality in the global AI hardware value chain (see Taiwan in focus, 12 June 2026).

Korea stands out as the primary beneficiary of the memory chip “supercycle” driven by AI-related demand (see Korea in focus, 20 May 2026).

DRAM is high-speed, volatile (unable to retain data without constant power) memory commonly found in computers. High-bandwidth memory (HBM), closely linked to AI demand, stacks DRAM vertically to deliver the extreme speeds required by large language models (LLMs). NAND, meanwhile, provides non-volatile storage (able to retain data even without power). Both DRAM and NAND are essential for AI data centres. Korea's two champions, Samsung and SK Hynix, account for roughly 70% of the global DRAM market and over half of NAND Flash. $^{3}$

Japan is a major supplier of chipmaking equipment, chemicals and materials

Japan plays a pivotal role in the semiconductor value chain as a major supplier of chipmaking equipment, chemicals and materials (see Japan in focus, 10 February 2026). The government recently proposed a JPY370trn (USD2.3trn), 14-year strategic investment plan focused on AI, semiconductors and other critical technologies. Supported in part by regional subsidies, Japan is also seeing an AI data centre boom, driven by both domestic and foreign investors. $^{4}$

Mainland China is less directly tied to the US hyperscaler capex cycle than Taiwan or Korea, but domestic AI demand is rising quickly. Since the US introduced sweeping chip restrictions in October 2022, China has accelerated supply chain localisation, creating opportunities for national champions, such as Huawei, foundry SMIC, memory producers YMTC (NAND) and CXMT (DRAM), equipment maker SMEE, and others (see Mainland China in focus, 15 April 2026). Beijing is also planning around RMB2trn (USD295bn) of data centre investment over the next five years, aiming to source at least 80% of AI chips from local suppliers. $^{5}$

Australia is experiencing a data centre investment boom

Southeast Asia has long been a hub for semiconductor assembly, testing and packaging. Two ASEAN economies also have meaningful front-end manufacturing: Singapore (memory) and Malaysia (automotive chips). Several ASEAN economies – such as Malaysia and Thailand – have also emerged as key destinations for data centre investment (see Chart 4). By pragmatically hedging amid rising geopolitical frictions, many ASEAN economies have leveraged neutrality and local advantages to attract investment from China, the US, and the EU across data centres, chips, autos, green energy and electronics (see Asia in the “G2” world, 14 May 2026).

Australia is also seeing strong growth in data centre investment. However, with around $85\%$ of equipment imported, the near-term domestic growth uplift may be smaller than in economies that produce more AI hardware and components (see Paul Bloxham, The data centre boom: lessons from the LNG boom, 29 June 2026).

Beyond the two immediate growth catalysts – AI hardware exports and data centre investment – AI could also lift long-term growth through productivity gains. The scale of that uplift will depend on how transformative AI ultimately proves to be (still hotly debated) $^{6}$ and how effectively individual economies adopt the technology, which may favour developed markets based on the IMF's AI Preparedness Index (see Chart 5).

Chart 4: Top recipients of data centre FDI  
![](images/97ce8cb185a11cc9f5261e751ba769cbc98384471fee710150c9241482334f08.jpg)  
Source: UNCTAD, HSBC. Note: Data covers the first three quarters of 2025.

Chart 5: AI Preparedness Index  
![](images/a74a4384b10f6a026d76c54c3036be48a13b167aa0d66a6cdd46067e871244f1.jpg)  
Source: IMF, HSBC

## AI adoption has generally not led to mass layoffs so far

## Labour disruption

Beyond the initial infrastructure build-out, AI's second-round macro effects have been modest so far, with no mass layoffs or step-change in productivity. Adoption is still gradual, like past general-purpose technologies: productivity rises over time, some roles are displaced, others emerge, and widespread joblessness is avoided (though unemployment could edge up near term). Of course, if adoption accelerates, faster capability gains could widen labour displacement (see James Pomeroy and Bethan Ellis, Gamechangers, 20 April 2026).

## What are the potential labour impacts across Asian economies?

To start, we compare “explicit” and “implicit” signals in earnings call commentary across sectors in Asia’s emerging versus developed markets (see Chart 6 and Chart 7). $^{7}$ Unsurprisingly, early signals are strongest in services – particularly information technology (IT), financials and consumer discretionary – and tend to be more pronounced in emerging markets.

Chart 6: AI's potential labour market impact in Asia EM economies  
![](images/6137d1cf288790406e4f5237c7a869eb8cdb6f9a77e3900ee50e968dc5ed7bba.jpg)  
Source: LSEG, TKRD, FTSE Russell, HSBC. Note: Figure inside columns indicate the number of companies. Emerging markets (EM) economies include mainland China, India, Thailand, Malaysia, the Philippines and Indonesia.

Chart 7: AI's potential labour market impact in Asia DM economies  
![](images/c3b66ea1f809176608f19081b02232f4e0b8758adabc1bac0bccb0f25178142b.jpg)  
Source: LSEG, TKRD, FTSE Russell, HSBC. Note: Figure inside columns indicate the number of companies. Developed markets (DM) economies include Japan, South Korea, Taiwan, Hong Kong, Singapore, Australia, and New Zealand.

Mainland Chinese companies report the highest potential labour impact...

While mass layoffs haven't occurred, other Asian economies can look to mainland China as a potential bellwether for AI's labour impact. As Chart 8 shows, companies there report the largest number of both explicit impacts (directly linked to layoffs) and implicit impacts (no direct link, but signs of substitution or slower hiring) in Asia.

Chart 8: AI's potential labour market impact across individual Asian economies  
![](images/39536e81e22820b7ff88dad1caa8fe41a33f795b092daad570549ce37b915bb3.jpg)  
Source: LSEG, TKRD, FTSE Russell, HSBC. Note: Figure inside columns indicate the number of companies. CH stands for mainland China.

Mainland China's higher potential labour impact compared to the rest of Asia reflects its rapid AI adoption rate (defined as the share of companies whose transcripts mention practical AI adoption) and deeper integration of AI into business processes (see Chart 9 and Table 1). $^{8}$

Chart 9: Mainland China has Asia's highest AI adoption rate, even exceeding the US\*  
![](images/39ec09fc6958b4313b964e959569581df1c8fd4555b5591cda27c69b774b86eb.jpg)  
Source: LSEG, TKRD, FTSE Russell, HSBC. Note: CH stands for mainland China. \*Our analysis may potentially overstate mainland China's figure due to coverage limitations and our reliance on English-language earnings call transcripts in the database.

Economies with high-tech exposure, such as Korea and Taiwan, also rank highly on AI adoption and usage. Thailand's surveyed companies also score strongly. By contrast, there are fewer clear signs of AI adoption in Indonesia and the Philippines.

Table 1: Average AI usage scores across individual Asian economies and sectors

<table><tr><td></td><td># companies with earnings calls</td><td>Market Score</td><td>Comms Svsc</td><td>Cons. Disc</td><td>Cons. Staples</td><td>Energy</td><td>Financials</td><td>Health Care</td><td>Industrials</td><td>Technology</td><td>Materials</td><td>Real Estate</td><td>Utilities</td></tr><tr><td>Mainland China</td><td>77</td><td>2.9</td><td>4.1</td><td>3.2</td><td>2.2</td><td>0.0</td><td>3.3</td><td>1.3</td><td>3.1</td><td>2.5</td><td>4.0</td><td>1.5</td><td>0.0</td></tr><tr><td>Thailand</td>

[中间内容因长度限制已省略]

C México, SA, Institución de Banca Múltiple, Grupo Financiero HSBC is authorized and regulated by Secretaría de Hacienda y Crédito Público and Comisión Nacional Bancaria y de Valores (CNBV). In Brazil, this document has been distributed by Banco HSBC SA ("HSBC Brazil"), and/or its affiliates. As required by Resolution No. 20/2021 of the Securities and Exchange Commission of Brazil (Comissão de Valores Mobiliários), potential conflicts of interest concerning (i) HSBC Brazil and/or its affiliates; and (ii) the analyst(s) responsible for authoring this report are stated on the chart above labelled "HSBC & Analyst Disclosures".

If you are a customer of HSBC International Wealth & Premier Banking ("IWPB"), including HSBC Private Bank, you are eligible to receive this publication only if: (i) you have been approved to receive relevant research publications by an applicable HSBC legal entity; (ii) you have agreed to the applicable HSBC entity's terms and conditions and/or customer declaration for accessing research; and (iii) you have agreed to the terms and conditions of any other internet banking, online banking, mobile banking and/or investment services offered by that HSBC entity, through which you will access research publications (collectively with (ii), the "Terms"). If you do not meet the above eligibility requirements, please disregard this publication and, if you are a IWPB customer, please notify your Relationship Manager or call the relevant customer hotline. Distribution of this publication is the sole responsibility of the HSBC entity with whom you have agreed the Terms. Receipt of research publications is strictly subject to the Terms and any other conditions or disclaimers applicable to the provision of the publications that may be advised by IWPB. © Copyright 2026, The Hongkong and Shanghai Banking Corporation Limited, ALL RIGHTS RESERVED. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, on any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of The Hongkong and Shanghai Banking Corporation Limited.

# Global Economics Research Team

## Global

Global Chief Economist
Janet Henry +44 20 7991 6711
janet.henry@hsbcib.com

Global Economist  
James Pomeroy +44 20 7991 6714  
james.pomeroy@hsbc.com

Global Economist  
Bethan Ellis +44 20 7991 6714  
bethan.ellis@hsbc.com

Senior Trade Economist  
Shanella Rajanayagam +44 20 3268 4118  
shanella.l.ajanayagam@hsbc.com

Trade Economist
Prachi Mathur +91 99 5880 6333
prachi.mathur@hsbc.co.in

## Europe

Chief European Economist
Simon Wells +44 20 7991 6718
simon.wells@hsbcib.com

Senior Economist
Chris Hare +44 20 7991 2995
chris.hare@hsbc.com

## United Kingdom

Senior Economist, UK
Elizabeth Martins +44 20 7991 2170
liz.martins@hsbc.com

UK Economist
Emma Wilks + 44 20 3268 5948
emma.wilks@hsbc.com

## Germany

Stefan Schilbe +49 211 910 3137
stefan.schilbe@hsbc.de

Anja Sabine Heimann +44 738 724 7457  
anja.sabine.heimann@hsbc.com

## France

Chantana Sam +33 1 4070 7795
chantana.sam@hsbc.fr

## North America

## US

Ryan Wang +1 212 525 3181
ryan.wang@us.hsbc.com

## Asia Pacific

Co-Head of Global Research, Asia-Pacific and Co-Head of Asian Economics Research
Frederic Neumann +852 2822 4556
fredericneumann@hsbc.com.hk

Chief Economist, Australia, New Zealand and Global Commodities  
Paul Bloxham +612 9255 2635  
paulbloxham@hsbc.com.au

Chief Economist, India and Indonesia
Pranjul Bhandari +65 6658 4976
pranjul.bhandari@hsbc.com.sg

Jamie Culling +612 9006 5042
jamie.culling@hsbc.com.au

Jing Liu +852 3941 0063
jing.econ.liu@hsbc.com.hk

Ines Lam +852 2288 7131
ines.y.k.lam@hsbc.com.hk

Yun Liu +852 2822 4297
yun.liu@hsbc.com.hk

Aayushi Chaudhary +91 22 2268 5543
aayushi.b.chaudhary@hsbc.co.in

Maitreyi Das +91 80 6737 3155
maitreyi.das@hsbc.co.in

Erin Xin +852 2996 6975 erin.y.xin@hsbc.com.hk

Aris Dacanay +852 3945 1247
aris.dacanay@hsbc.com.hk

Jin Choi +852 2996 6597 jin.h.j.choi@hsbc.com.hk

Akiko Kitamura +852 2996 6676
akiko.kitamura@hsbc.com.hk

Justin Feng +852 2288 7108
justin.feng@hsbc.com.hk

Taylor Wang +852 2288 8650
taylor.t.l.wang@hsbc.com.hk

Priya Mehrishi +91 97 3916 9567  
priya.mehrishi@hsbc.co.in

## CEEMEA

Chief Economist, CEEMEA
Simon Williams +971 50 9143382
simon.williams@hsbc.com

Senior Economist, Central & Eastern Europe
Agata Urbanska-Giner +44 20 7992 2774
agata.urbanska@hsbcib.com

Senior Economist, CEEMEA  
Melis Metiner +44 20 3359 2636  
melismetiner@hsbcib.com

Senior Economist, South Africa  
Hugo Pienaar +44 20 7718 9563  
hugo.pienaar@hsbc.com

## Latin America

Chief Economist, Mexico
Jose Carlos Sanchez +52 55 5721 5623
jose.c.sanchez@hsbc.com.mx

Head of Brazil Economics Research
Daniel Lavarda +55 11 2802 2640
daniel.lavarda@hsbc.com
"""
