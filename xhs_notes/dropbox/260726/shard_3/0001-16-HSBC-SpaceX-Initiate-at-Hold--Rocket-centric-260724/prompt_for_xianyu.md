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
Global

Thematic research

By: Nicolas Cote-Colisson and Charlie Rothbarth

July 2026 www.research.hsbc.com

# SpaceX

Initiate at Hold: Rocket-centric

Space, Connectivity, and AI are designed to leverage a repeatable, vertically integrated, cost-efficient model; SpaceX's market leading rocket operation already effectively supports Starlink

Full vertical integration relies on as yet unproven technologies, including orbital compute power for its GenAI models, the outcome of which impacts the required Space launch cadence

We initiate at Hold with an SOTP-based target price of USD115, including an innovation premium of 2x. Our blue-sky scenario is USD293

Disclosures & Disclaimer: This report must be read with the disclosures and the analyst certifications in the Disclosure appendix, and with the Disclaimer, which forms part of it.

## Financials & valuation: SpaceX

Financial statements

<table><tr><td>Year to</td><td>12/2025a</td><td>12/2026e</td><td>12/2027e</td><td>12/2028e</td></tr><tr><td colspan="5">Profit &amp; loss summary (USDm)</td></tr><tr><td>Revenue</td><td>18,674</td><td>38,208</td><td>49,783</td><td>62,272</td></tr><tr><td>EBITDA</td><td>4,112</td><td>15,426</td><td>22,728</td><td>33,671</td></tr><tr><td>Depreciation &amp; amortisation</td><td>-6,701</td><td>-15,612</td><td>-24,194</td><td>-32,187</td></tr><tr><td>Operating profit/EBIT</td><td>-2,589</td><td>-186</td><td>-1,465</td><td>1,484</td></tr><tr><td>Net interest</td><td>-1,630</td><td>-3,040</td><td>-883</td><td>-958</td></tr><tr><td>PBT</td><td>-4,219</td><td>-3,226</td><td>-2,348</td><td>526</td></tr><tr><td>HSBC PBT</td><td>-1,747</td><td>238</td><td>3,022</td><td>5,877</td></tr><tr><td>Taxation</td><td>-718</td><td>-184</td><td>399</td><td>-89</td></tr><tr><td>Net profit</td><td>-4,937</td><td>-4,080</td><td>-1,949</td><td>436</td></tr><tr><td>HSBC net profit</td><td>-2,465</td><td>-617</td><td>3,421</td><td>5,787</td></tr></table>

Cash flow summary (USDm)

## Hold

Key forecast drivers

<table><tr><td>Cash flow from operations</td><td>6,785</td><td>14,708</td><td>28,240</td><td>38,498</td></tr><tr><td>Capex</td><td>-20,737</td><td>-68,587</td><td>-53,847</td><td>-59,109</td></tr><tr><td>Cash flow from investment</td><td>-19,575</td><td>-75,204</td><td>-53,847</td><td>-59,109</td></tr><tr><td>Dividends</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Change in net debt</td><td>-3,459</td><td>-30,702</td><td>26,477</td><td>21,521</td></tr><tr><td>FCF equity</td><td>-14,247</td><td>-53,962</td><td>-25,607</td><td>-20,612</td></tr></table>

Balance sheet summary (USDm)

<table><tr><td>Year to</td><td>12/2025a</td><td>12/2026e</td><td>12/2027e</td><td>12/2028e</td></tr><tr><td>Space revenues</td><td>4,086</td><td>3,757</td><td>4,970</td><td>5,680</td></tr><tr><td>Connectivity revenues</td><td>11,387</td><td>15,551</td><td>21,903</td><td>28,822</td></tr><tr><td>AI revenues</td><td>3,201</td><td>18,901</td><td>22,454</td><td>27,222</td></tr><tr><td>Space Adj EBITDA</td><td>653</td><td>-740</td><td>883</td><td>1,641</td></tr><tr><td>Connectivity Adj EBITDA</td><td>7,168</td><td>10,089</td><td>14,626</td><td>19,864</td></tr><tr><td>AI Adj EBITDA</td><td>-1,237</td><td>9,541</td><td>12,589</td><td>17,518</td></tr></table>

<table><tr><td>Intangible fixed assets</td><td>15,628</td><td>75,830</td><td>76,230</td><td>76,140</td></tr><tr><td>Tangible fixed assets</td><td>43,862</td><td>100,371</td><td>149,625</td><td>176,547</td></tr><tr><td>Current assets</td><td>30,952</td><td>101,964</td><td>55,197</td><td>36,714</td></tr><tr><td>Cash &amp; others</td><td>24,747</td><td>87,818</td><td>41,316</td><td>19,795</td></tr><tr><td>Total assets</td><td>92,079</td><td>279,459</td><td>282,345</td><td>290,695</td></tr><tr><td>Operating liabilities</td><td>27,858</td><td>34,947</td><td>35,706</td><td>39,179</td></tr><tr><td>Gross debt</td><td>22,896</td><td>55,265</td><td>35,240</td><td>35,240</td></tr><tr><td>Net debt</td><td>-1,851</td><td>-32,553</td><td>-6,076</td><td>15,445</td></tr><tr><td>Shareholders&#x27; funds</td><td>41,325</td><td>182,198</td><td>204,349</td><td>209,227</td></tr><tr><td>Invested capital</td><td>16,184</td><td>155,401</td><td>204,029</td><td>230,428</td></tr></table>

Ratio, growth and per share analysis

Valuation data

<table><tr><td>Year to</td><td>12/2025a</td><td>12/2026e</td><td>12/2027e</td><td>12/2028e</td></tr><tr><td>EV/sales</td><td>81.0</td><td>38.8</td><td>30.3</td><td>24.6</td></tr><tr><td>EV/EBITDA</td><td>368.0</td><td>96.1</td><td>66.4</td><td>45.5</td></tr><tr><td>EV/IC</td><td>93.5</td><td>9.5</td><td>7.4</td><td>6.6</td></tr><tr><td>PE*</td><td>nm</td><td>nm</td><td>440.4</td><td>260.3</td></tr><tr><td>PB</td><td>8.2</td><td>6.8</td><td>7.4</td><td>7.2</td></tr><tr><td>FCF yield (%)</td><td>-0.9</td><td>-3.6</td><td>-1.7</td><td>-1.4</td></tr><tr><td>Dividend yield (%)</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr></table>

\* Based on HSBC EPS (diluted)

ESG metrics

<table><tr><td>Environmental Indicators</td><td>12/2025a</td></tr><tr><td>GHG emission intensity*</td><td>n/a</td></tr><tr><td>Energy intensity*</td><td>n/a</td></tr><tr><td>CO2 reduction policy</td><td>Yes</td></tr><tr><td>Social Indicators</td><td>12/2025a</td></tr><tr><td>Employee costs as % of revenues</td><td>n/a</td></tr><tr><td>Employee turnover (%)</td><td>n/a</td></tr><tr><td>Diversity policy</td><td>Yes</td></tr></table>

<table><tr><td>Governance Indicators</td><td>12/2025a</td></tr><tr><td>No. of board members</td><td>8</td></tr><tr><td>Average board tenure (years)</td><td>12.9</td></tr><tr><td>Female board members (%)</td><td>12.5</td></tr><tr><td>Board members independence (%)</td><td>62.5</td></tr><tr><td>No. of board members</td><td></td></tr><tr><td>No. of board members</td><td></td></tr></table>

Source: Company data, HSBC  
\* GHG intensity and energy intensity are measured in kg and kWh respectively against revenue in USD '000s

<table><tr><td>Year to</td><td>12/2025a</td><td>12/2026e</td><td>12/2027e</td><td>12/2028e</td></tr><tr><td colspan="5">Y-o-y % change</td></tr><tr><td>Revenue</td><td>33.2</td><td>104.6</td><td>30.3</td><td>25.1</td></tr><tr><td>EBITDA</td><td>-4.1</td><td>275.2</td><td>47.3</td><td>48.1</td></tr><tr><td>Operating profit</td><td>-655.6</td><td></td><td></td><td></td></tr><tr><td>PBT</td><td>-1843.4</td><td></td><td></td><td></td></tr><tr><td>HSBC EPS</td><td>-875.9</td><td></td><td></td><td>69.1</td></tr><tr><td colspan="5">Ratios (%)</td></tr><tr><td>Revenue/IC (x)</td><td>0.9</td><td>0.4</td><td>0.3</td><td>0.3</td></tr><tr><td>ROIC</td><td>-14.5</td><td>-0.2</td><td>-0.7</td><td>0.6</td></tr><tr><td>ROE</td><td>-7.3</td><td>-0.6</td><td>1.8</td><td>2.8</td></tr><tr><td>ROA</td><td>-6.6</td><td>-1.8</td><td>-0.7</td><td>0.2</td></tr><tr><td>EBITDA margin</td><td>22.0</td><td>40.4</td><td>45.7</td><td>54.1</td></tr><tr><td>Operating profit margin</td><td>-13.9</td><td>-0.5</td><td>-2.9</td><td>2.4</td></tr><tr><td>EBITDA/net interest (x)</td><td>2.5</td><td>5.1</td><td>25.8</td><td>35.1</td></tr><tr><td>Net debt/equity</td><td>-4.5</td><td>-17.2</td><td>-2.9</td><td>7.1</td></tr><tr><td>Net debt/EBITDA (x)</td><td>-0.5</td><td>-2.1</td><td>-0.3</td><td>0.5</td></tr><tr><td>CF from operations/net debt</td><td></td><td></td><td></td><td>249.3</td></tr><tr><td colspan="5">Per share data (USD)</td></tr><tr><td>EPS Rep (diluted)</td><td>-1.69</td><td>-0.38</td><td>-0.15</td><td>0.03</td></tr><tr><td>HSBC EPS (diluted)</td><td>-0.84</td><td>-0.06</td><td>0.26</td><td>0.44</td></tr><tr><td>DPS</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>Book value</td><td>14.12</td><td>16.91</td><td>15.63</td><td>16.01</td></tr></table>

Issuer information

<table><tr><td>Share price (USD)</td><td>115.26</td></tr><tr><td>Target price (USD)</td><td>115.00</td></tr><tr><td>RIC (Equity)</td><td>SPCX.N</td></tr><tr><td>Bloomberg (Equity)</td><td>SPCX US</td></tr><tr><td>Market cap (USDm)</td><td>1,516,729</td></tr></table>

<table><tr><td colspan="2">Free float</td><td>5%</td></tr><tr><td>Sector</td><td colspan="2">Internet Software &amp; Services</td></tr><tr><td colspan="2">Country/Region</td><td>United States</td></tr><tr><td>Analyst</td><td colspan="2">Nicolas Cote-Colisson</td></tr><tr><td>Contact</td><td colspan="2">+44 20 7991 6826</td></tr></table>

Price relative  
![](images/420012114dbff2c1fcd8fbe2fd8d9c473b19675d8db815dd64070f2e47e0e38b.jpg)  
Source: HSBC  
Note: Priced at close of 22 Jul 2026

## Meet our global tech analysts

Paul Rossington\*  
Yaryna Kobel  
![](images/dbf4fb740cdc0ca1386583268fed150636bdb8dd68fc7f85308ccfa1b0b6b7a5.jpg)

Nicolas Cote-Colisson\*  
MD, Head of Global Tech Platforms  
Subscribe to Nicolas's research  
nicolas.cote-colisson@hsbcib.com

![](images/168fda1fd18224b4e63fa35734e9096aabc203d97a616353ebb42df8f16a7a14.jpg)

Global Tech Platforms Analyst

Subscribe to Charlie's research

charlie.rothbarth@hsbc.com

![](images/1ac93ed128a8771124a273545fb27c64032ba5dce37fbec3d6fc95008aa8f501.jpg)

Senior Global Tech Platforms Analyst
Subscribe to Paul's research
paul.rossington@hsbcib.com

Abhishek Shukla\*, CFA  
![](images/797fedcc6b18eeb8ed7910a23da0ea713a53aab97938bb9150181930a43eb6d9.jpg)

Subscribe to Abhishek's research

abhishek2.shukla@hsbc.com

Mohammed Khallouf\*, CFA  
![](images/60a2f0491218be82305f5cea0ae14caccb1059b42e4e888e774f54bdc24dff9d.jpg)  
Madhvendra Singh\*, CFA

Global Tech Platforms Analyst
Subscribe to Mohammed's research
mohammed.khallouf@hsbc.com

Senior Analyst, TMT  
Subscribe to Madhvendra's research madhvendra.singh@hsbc.com

![](images/e97f1bc6bc362258867dde532f4802bf8b4b4881b8115ca044e4a796ce143084.jpg)

![](images/2981971fb2e83cb85b7e98121a84da6405bc488ab451bed2b4af277e89c694c8.jpg)

Phani Kanumuri

<table><tr><td>Analyst, TMT</td></tr><tr><td>Subscribe to Phani&#x27;s researchphani.kanumuri@us.hsbc.com</td></tr></table>

![](images/2d0e84e53a6b7640a0e7837949fd52d2f58efa2456efaa78bfa9cec93e033437.jpg)  
Ali Naqvi\*

ali.naqvi@hsbc.com

![](images/a0e9c02d2c273136f2fbb1303051e45eca59df264316970d5be2560ab17c31b9.jpg)

![](images/a30419791ae59d7e291b355fd2603dfb24650c8eaae6aa3baf38d7e7ce215b3e.jpg)

Global Head of Tech Hardware & Semi Research

Subscribe to Frank's research

frank.lee@hsbc.com.hk

![](images/316df7d4d377e13ae4c654ba16ec1deb41389ba85d9dc5946eb9fd26c12ff06d.jpg)  
Pushkar Tendolkar\*

Corey Chan\*
(Reg. No. S1700518100001)
Head, A-share Industrials & Renewables Research

Subscribe to Corey's research

corey.chan@hsbcqh.com.cn

Senior Global Autos Analyst

Subscribe to Mike's research

michael.tyndall@hsbc.com

![](images/ca1d594539fe2c2da998a0b531fe79df3a8a65c8732b394046905cb2dbf610a9.jpg)

Subscribe to Pushkar's research pushkarnarendratendolkar@hsbc.co.in

Dylan Whitfield\*, FCA  
![](images/5540e3b3a66b49f6569693312b668a91820acd238541c70540f80b1a6c57fccc.jpg)

Head, Accounting Valuations & Forensic Accounting

dylan.b.whitfield@hsbc.com

![](images/cce971cfa93c63773edf3215a10bc862ea970ae31ed0a701f9858b85f596208d.jpg)

Corporate Governance Analyst

yaryna.kobel@hsbc.com

![](images/f107dd64aea4f3871d33f7d694b5f15f222af66f8acd7460154bb4e829868606.jpg)  
Stephen Bersey

Head of US Technology Research

Subscribe to Steve's research

stephen.bersey@us.hsbc.com

## Contents

Why read this report? 4
The message from Space(X) 8
Valuation premium warranted 17
Space – the platform 29
Connectivity / Starlink 42
AI 57
Financial statement review 86
Learnings from Tesla 89
Governance 92
Disclosure appendix 102
Disclaimer 105

We acknowledge the contribution of Bangalore Associates Sonam Chamaria (Lead AVP) and Pulkit Aggarwal (AVP) in the preparation of this report.

## Why read this report?

\- SpaceX holds a competitive, leading position in the commercial space launch market, underpinning its long-term strategy

\- Strong innovation track record so far; we are prudent on pricing in SpaceX’s futuristic calls including space datacentres, Terafab, and the lunar economy

We apply an “innovation premium” to our fundamental valuation to derive our TP of USD115.00, which implies 0.2% downside, and we therefore initiate with a Hold rating; our blue-sky scenario implies a valuation of USD293.00

## How the market views SpaceX

We believe there are two broad investor camps for SpaceX. There are those whose view the company as a foundation platform incorporating all of CEO Elon Musk's vision, which has the potential to change the world. The second camp may not fully dismiss Mr Musk's plans, but is not ready to pay ahead of delivery. We note that Tesla has not traded on classical fundamentals, reflecting the fact that there may be greater support from bullish investors than the more sceptical investors.

## What we bring to the debate

SpaceX brings a host of technological innovations and futuristic opportunities. However, there are a series of questions that we believe investors should consider when evaluating company. We aim to analyse these in further detail in this report, alongside challenging some implications from the SEC Form S-1 prospectus, including the total addressable market (TAM) for connectivity, the necessity or feasibility of orbital datacentres, as well as Terafab, and therefore the degree of launch cadence required.

## What we expect for 2030e

For the group, we estimate revenues of USD106bn, adjusted EBITDA of USD76bn, GAAP operating profit of USD16bn and FCF of USD12.9bn. From what we can learn from Visible Alpha consensus, we are 72% below expectations on revenues and adjusted EBITDA for 2030e. Ultimately, we may be wrong, but we could be right too – for these higher revenue estimates to come to fruition, a variety of challenges must be overcome, but we do not think this is feasible by 2030.

## How we value SpaceX – a detailed SOTP and an “innovation premium”

We value each business segment separately before we apply an “innovation premium” of 2.0x (page 17).

When valuing a company, analysts may sometimes apply a discount (holding structures, dyssynergies, risks etc), but we also consider the case for applying a premium, especially when a strong founder has a proven track record of transforming some industries (including cars and rockets). We considered several valuation approaches, including those for valuing SPACs, mining stocks, or the biotech/pharma sector, but in our view none of these methodologies correctly capture the innovation multiple that we believe should be considered. Therefore, we have looked at Tesla's share price performance over the first 10-years since its IPO, as we believe this is the most appropriate proxy to determine a valuation premium given the commonality in CEO/founder, innovation approach, and developing disruptive technology into a sustainable business.

Based on our observation of Tesla's share price performance and consensus target prices set by sell side research analysts covering the stock, we conclude that over the first 10 years since its IPO, i.e. 2010-20 (we take this period to reflect the early stage and rate of innovation of the business), Tesla's share price was more than double (118%) the average target price the year before. This indicates that fundamental valuation methods do not reflect what the market may be ready to pay for management or 'flywheel' effects, i.e. incremental advances in technology and efficiency compound over time, eventually leading to a sustainable, growing business model. We also conducted the same calculation for the 'Magnificent 7' (Mag-7) peer group (Alphabet, Amazon, Apple, Meta, Microsoft, Nvidia, and Oracle) and derive a much lower premium of 18% over the same timeframe (2010-20). We therefore estimate a 100% (118% for Tesla minus 18% for the Mag-7) "innovation premium" (i.e. 2.0x) for Tesla vs the broader tech market. We think the same premium co

[中间内容因长度限制已省略]

tes. As required by Resolution No. 20/2021 of the Securities and Exchange Commission of Brazil (Comissão de Valores Mobiliários), potential conflicts of interest concerning (i) HSBC Brazil and/or its affiliates; and (ii) the analyst(s) responsible for authoring this report are stated on the chart above labelled "HSBC & Analyst Disclosures". If you are a customer of HSBC International Wealth & Premier Banking ("IWPB"), including HSBC Private Bank, you are eligible to receive this publication only if: (i) you have been approved to receive relevant research publications by an applicable HSBC legal entity; (ii) you have agreed to the applicable HSBC entity's terms and conditions and/or customer declaration for accessing research; and (iii) you have agreed to the terms and conditions of any other internet banking, online banking, mobile banking and/or investment services offered by that HSBC entity, through which you will access research publications (collectively with (ii), the "Terms"). If you do not meet the above eligibility requirements, please disregard this publication and, if you are a IWPB customer, please notify your Relationship Manager or call the relevant customer hotline. Distribution of this publication is the sole responsibility of the HSBC entity with whom you have agreed the Terms. Receipt of research publications is strictly subject to the Terms and any other conditions or disclaimers applicable to the provision of the publications that may be advised by IWPB.

© Copyright 2026, HSBC Continental Europe, ALL RIGHTS RESERVED. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, on any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of HSBC Continental Europe.

## Main contributors

![](images/fff28a0cfa8cd10e8b115de6a726b075a6ed11f3b983033fcc6683264fbeac01.jpg)

## Nicolas Cote-Colisson\*

Nicolas Cote-Colisson\*
MD, Head of Global Tech Platforms
HSBC Continental Europe
nicolas.cote-colisson@hsbcib.com
+44 20 7991 6826

![](images/6ac3201189a33bfea59a662c40d2245c97ebd3ddcf686719351c85b0762de76e.jpg)

## Abhishek Shukla\*, CFA

Senior Analyst, Technology
HSBC Bank Middle East Limited, DIFC
abhishek2.shukla@hsbc.com
+971 4 509 3343

![](images/2c3b6666262c92b9580cb70a02ed5faced197a03e18c4436b51dcc32999d4589.jpg)

## Mohammed Khallouf\*, CFA

Global Tech Platforms Analyste
HSBC Bank Middle East Limited, DIFC
mohammed.khallouf@hsbc.com
+971 4509 3337

![](images/3ac6dd4f152ea7bf6080d6328c839a316df0c23f4e807d584341f7322e9e4e64.jpg)

## Madhvendra Singh\*, CFA

Senior Analyst, TMT
HSBC Bank Middle East Limited, DIFC
madhvendra.singh@hsbc.com
+971 4509 3348

![](images/8a66c0abf775cd2ecaab57fdf5b577a56eb41f6fe37f9e695bfbbe7f714c83f6.jpg)

## Michael Tyndall\*, CFA

Senior Global Autos Analyst
HSBC Bank plc
michael.tyndall@hsbc.com
+44 20 3359 6301

![](images/c8a5001e2bc1cd168e95d55b1b3252415fc1c0eb0c4b1d638d7e3aee8a53862d.jpg)

## Corey Chan\* (Reg. No. S1700518100001)

Head, A-share Industrials & Renewables Research  
HSBC Qianhai Securities Limited  
corey.chan@hsbcqh.com.cn  
+86 21 5066 2001

![](images/59b8bc25260593a82959df7e8697ce1188772224f3f801d6e7561778cc1d6c68.jpg)

## Stephen Bersey

Head of US Technology Research
HSBC Securities (USA) Inc
stephen.bersey@us.hsbc.com
+1 212 525 4153

![](images/1a56aa5c0e2ebd500f32d8f2a58a967fe260e8d921b16210d49d3baae19a1906.jpg)

## Charlie Rothbarth\*

Global Tech Platforms Analyst
HSBC Bank plc
charlie.rothbarth@hsbc.com
+44 20 3268 5284

![](images/47bc147df82bf5c158f4ea7c8152c7373eeb2dd21ff82975334d66c814bdb1b5.jpg)

## Paul Rossington\*

Senior Global Tech Platforms Analyst
HSBC Bank plc
paul.rossington@hsbcib.com
+44 20 7991 6734

![](images/a8e2b2c8b48b1a0421cf9d2f8dfac0c03a5f68fbc11e1f5dacc743158ac456f3.jpg)

## Frank Lee\*

Global Head of Tech Hardware & Semi Research  
The Hongkong and Shanghai Banking Corporation Limited  
frank.lee@hsbc.com.hk  
+852 2996 6916

![](images/44d186e06aa4edf1f493cb84a380a260c5644fc92beb8c0d4d7279b0cfbc86c0.jpg)

## Phani Kanumuri

Analyst, TMT
HSBC Securities (USA) Inc.
phani.kanumuri@us.hsbc.com
+1 240 709 8135

![](images/9036114b779f894b4b474c1042ffd2318edc63202bfdebd8c2a524d21b2ebe07.jpg)

## Pushkar Tendolkar\*

Global Autos Analyst
HSBC Securities and Capital Markets (India)
Private Limited
pushkarnarendratendolkar@hsbc.co.in
+91 80 4555 2752

![](images/ca5680d9dd5008affc45890b471fb61dce7c93cdf9665e3e25233a708907763f.jpg)

## Dylan Whitfield\*, FCA

Head, Accounting Valuations & Forensic Accounting  
HSBC Bank plc  
dylan.b.whitfield@hsbc.com  
+44 20 3359 5903

![](images/4c7f816f0c94a9b2e98991f23d291cf67aa1fb5f034c5fa6d618736a4fd9c4c4.jpg)

## Yaryna Kobel

Corporate Governance Analyst
HSBC Bank plc
yaryna.kobel@hsbc.com
+44 20 3359 6152
"""
