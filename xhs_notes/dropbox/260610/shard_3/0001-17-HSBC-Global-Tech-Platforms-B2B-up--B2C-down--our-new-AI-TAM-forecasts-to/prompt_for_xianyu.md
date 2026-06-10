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
# Global Tech Platforms

## B2B up, B2C down: our new AI TAM forecasts to 2030

## Equities

## Internet Software & Services

## United States

B2B: AI adoption up, driven by Anthropic but lifting all boats; we increase industry revenue forecasts by 74% in 2026-30e  
B2C: we cut our 2026-30e market revenue by 20% as user growth slows and monetisation lags at leader OpenAI  
We increase our AI TAM by 38% in 2026-30e; we update our OAI 2026-30e funding gap calculation, halved at USD77bn

## We increase our AI TAM by 38% in 2026-30e

Trends that have emerged since April: (1) the B2B AI market is accelerating significantly and (2) the B2C market is not growing as fast as we were expecting. For background, see Global Tech Platforms: OpenAI: Back to chatbots – new HSBC forecasts, 1 April and OpenAI launches its new frontier model, 24 April.

## We are updating our industry revenue estimates:

AI B2B industry revenue: we increase our estimates by 74% over 2026-30e. Agentic AI brings new use cases and accelerates adoption, coding tools are progressing fast too. Anthropic is a clear leader in B2B, OpenAi (OAI) remains a serious but distant contender alongside Gemini.  
B2C AI industry revenue: we cut our forecasts by 20% over 2026-30e driven by weaker user growth than expected in the market, notably at leader OAI and more complex monetisation of consumer chatbots than we initially expected. ARPU dilution from low tiered packages impacts subscription revenue.  
B2B+B2C AI industry revenue: we increase our 2026-30e AI total market revenue by 38%.

## The global AI landscape is shaping toward high concentration in the West

We think we are witnessing the build-up of an LLM oligopoly in the western side of the world, shaped by the very high cost of compute that has created a high barrier to entry. Significant cost cutting is not an option in our view. Scaling law dominates: more compute → smarter models → more users → more revenue. Such market structure increases the probability of recouping sunk costs by achieving long-term RoIC higher than WACC, absent sector regulation.

We believe that OAI is well positioned to be one of the key participants in the forming oligopoly. With this in mind, we cut our OAI 2030 funding gap estimate to USD77bn from USD154bn, through a combination of lower estimated FCF deficit, incremental equity raise, and increase in the value of Advanced Micro Devices (AMD US) shares that OAI could sell when they vest. Options to close the gap include an IPO (Anthropic just filed with the SEC) and another funding round (the latest round raised USD122bn in April 2026).

## Nicolas Cote-Colisson\*

MD, Head of Global Tech Platforms
HSBC Continental Europe
nicolas.cote-colisson@hsbcib.com
+44 20 7991 6826

## Abhishek Shukla\*, CFA

Senior Analyst, Technology
HSBC Bank Middle East Limited, DIFC
abhishek2.shukla@hsbc.com
+971 4 5093343

## Mohammed Khallouf\*, CFA

Global Tech Platforms Analyst
HSBC Bank Middle East Limited, DIFC
mohammed.khallouf@hsbc.com
+971 4 509 3337

## Paul Rossington\*

Senior Global Tech Platforms Analyst
HSBC Bank plc
paul.rossington@hsbcib.com
+44 20 7991 6734

## Charlie Rothbarth\*

Global Tech Platforms Analyst
HSBC Bank plc
charlie.rothbarth@hsbc.com
+44 203 2685284

## Stephen Bersey

Head of US Technology Research
HSBC Securities (USA) Inc.
stephen.bersey@us.hsbc.com
+1 212 525 4153

## Sameer Lam\*

Global Software Analyst
HSBC Bank plc
sameer.lam@hsbc.com
+44 20 7992 3780

\* Employed by a non-US affiliate of HSBC Securities (USA) Inc, and is not registered/ qualified pursuant to FINRA regulations

## Disclosures & Disclaimer

This report must be read with the disclosures and the analyst certifications in the Disclosure appendix, and with the Disclaimer, which forms part of it.

Issuer of report: HSBC Continental Europe

## View HSBC Global Investment Research at:

https://www.research.hsbc.com

## The global AI landscape is shaping further

3.5 years after the groundbreaking launch of ChatGPT (30 November 2022), the AI landscape is still in the making. If OpenAI (OAI) remains a leading reference in the West, its pioneer status didn't guarantee a perpetual lead position: Anthropic has surpassed OAI's Q2 2026 ARR (annualised rate of revenue). We also continue to observe a strategy gap and outcomes in the West and the East.

## A selected group of frontier models in the West...

Pioneer OAI has been rapidly joined by well-funded competitors, essentially Anthropic and Gemini, but also, from a distance, by Meta. We think we are witnessing the build-up of an oligopoly in the western side of the world, shaped by the very high cost of compute that has created a high barrier to entry (a “sunk costs” economy). This is illustrated by the step-up in unit measurements, from billion dollars to trillion dollars, from megawatts to gigawatts. Europe is leveraging these Western models but is looking at gaining some independence: Mistral AI can play a big role there. The French company has raised EUR1.7bn in September 2025 (a series C funding led by ASML valuing the company at EUR11.7bn post-money) to become the AI name for Europe, focusing on building precise business cases and deep integration into clients’ processes. The company is not focused on reaching the state of AGI (artificial general intelligence) in the way that OAI, Gemini, or Anthropic are.

## ...and a different structure in Asia

China is very active when it comes to models, with a combination of frontier models from large tech giants including Alibaba, Tencent, ByteDance and independent labs including DeepSeek, Minimax, Zhipu or Kimi to name a few. Models from independent labs tend to be smaller in size and have been built on much lower budgets than their Western peers. Western models claim that some of these have been trained by distilling their own frontier models (Anthropic, 14 May 2026). A more focused approach to model infrastructure optimisation, combined with a larger electricity grid supply (which is more of a constraint in the West) means a rapid adoption of AI, both in B2C and B2B in Asia and possibly a more fragmented market than the US.

## Reasons for different market structures explained

Large US Frontier models benefit from the size of their local market and high GDP per head too, which can justify a high level of investment and opex, considering their revenue expectations. Western models also have access to a deep financial market to finance their ambition. These companies also benefit from accessing the best chips (NVIDIA's latest GPUs), whereas China faces US export restrictions. Western models are leading intelligence and skills contests at present, and this could remain the case: their larger compute capacity is improving quality faster than lighter structures (“scaling laws”). We believe that this would limit the penetration of non-Western models in the West at scale, which is another point reinforcing the oligopoly nature of the market eventually (and increasing the probability of recouping sunk costs by achieving long-term RoIC higher than WACC, absent sector regulation).

## Leadership position is still unclear in the West

Only a few companies may make it to the final list (oligopoly structure). We think that OAI stands a strong chance of remaining part of this, but OAI has been seen as losing ground, notably against Anthropic and Gemini over the last months. We base this view on several signs:

- ChatGPT user growth outlook moderates as competitors gain  
OpenAI losing market share in foundation model subsegment in the Enterprise market  
Codex tools revenue are also lower than at Anthropic

In this note, we update our AI TAM and our forecasts for the main market participants to reflect the latest trends.

Please see our previous Global Tech Platforms reports: OpenAI: Back to chatbots – new HSBC forecasts, 1 April and OpenAI launches its new frontier model, 24 April

## AI TAM: we increase our 2026-30 industry revenue by 38%

Trends that have emerged since April: (1) the B2B AI market is accelerating significantly and (2) the B2C market is not growing as fast as we were expecting.

We increase our B2B AI industry by 74% over 2026-30e. Agentic AI brings new use cases to enterprises and accelerates AI adoption, coding tools are progressing fast too. Anthropic is a clear leader in B2B, OAI remains a serious but distant contender alongside Gemini. We increase OAI B2B revenue forecasts by 31% in 2026-30e.  
B2C: we cut our B2C AI industry estimates by 20% over 2026-30 driven by lower OAI forecasts (-23%). We have cut our user forecasts for leader OAI, which combined with ARPU dilution from lower tiered packages impacts subscription and advertising revenue.  
We increase our 2026-30e AI industry revenue by 38%, a combination of much higher B2B and slightly lower B2C revenue expectations.

HSBC new AI industry forecasts...

<table><tr><td>USDbn</td><td>2025e</td><td>2026e</td><td>2027e</td><td>2028e</td><td>2029e</td><td>2030e</td><td>Cumulative 2026-30e</td></tr><tr><td colspan="7">Total AI revenue</td><td></td></tr><tr><td>New</td><td>33</td><td>148</td><td>326</td><td>482</td><td>671</td><td>920</td><td>2,547</td></tr><tr><td>Old</td><td>33</td><td>100</td><td>196</td><td>324</td><td>493</td><td>728</td><td>1,842</td></tr><tr><td>Change</td><td>0%</td><td>47%</td><td>66%</td><td>48%</td><td>36%</td><td>26%</td><td>38%</td></tr><tr><td colspan="7">o/w B2C - Consumer</td><td></td></tr><tr><td>New</td><td>13</td><td>26</td><td>62</td><td>108</td><td>158</td><td>212</td><td>565</td></tr><tr><td>Old</td><td>13</td><td>31</td><td>71</td><td>129</td><td>197</td><td>278</td><td>705</td></tr><tr><td>Change</td><td>-1%</td><td>-16%</td><td>-13%</td><td>-16%</td><td>-20%</td><td>-24%</td><td>-20%</td></tr><tr><td colspan="7">o/w B2B - Enterprise</td><td></td></tr><tr><td>New</td><td>20</td><td>122</td><td>264</td><td>374</td><td>514</td><td>708</td><td>1,981</td></tr><tr><td>Old</td><td>20</td><td>69</td><td>125</td><td>196</td><td>296</td><td>450</td><td>1,137</td></tr><tr><td>Change</td><td>1%</td><td>76%</td><td>111%</td><td>91%</td><td>73%</td><td>57%</td><td>74%</td></tr></table>

Source: HSBC

...Of which OAI – New vs Old (HSBCe)

<table><tr><td>USDbn</td><td>2026e</td><td>2027e</td><td>2028e</td><td>2029e</td><td>2030e</td><td>Cumulative 2026-30e</td></tr><tr><td colspan="7">OAI total revenue</td></tr><tr><td>New</td><td>36</td><td>76</td><td>113</td><td>154</td><td>201</td><td>580</td></tr><tr><td>Old</td><td>34</td><td>64</td><td>106</td><td>161</td><td>235</td><td>600</td></tr><tr><td>Change</td><td>8%</td><td>18%</td><td>6%</td><td>-4%</td><td>-14%</td><td>-3%</td></tr><tr><td colspan="7">o/w OAI B2B revenue</td></tr><tr><td>New</td><td>18</td><td>40</td><td>55</td><td>74</td><td>100</td><td>287</td></tr><tr><td>Old</td><td>11</td><td>22</td><td>36</td><td>57</td><td>92</td><td>219</td></tr><tr><td>Change</td><td>63%</td><td>82%</td><td>54%</td><td>29%</td><td>8%</td><td>31%</td></tr><tr><td colspan="7">o/w OAI B2C revenue</td></tr><tr><td>New</td><td>15</td><td>30</td><td>48</td><td>67</td><td>85</td><td>245</td></tr><tr><td>Old</td><td>19</td><td>36</td><td>59</td><td>87</td><td>119</td><td>320</td></tr><tr><td>Change</td><td>-21%</td><td>-17%</td><td>-19%</td><td>-23%</td><td>-28%</td><td>-23%</td></tr><tr><td colspan="7">o/w Other revenue</td></tr><tr><td>New</td><td>3</td><td>6</td><td>9</td><td>13</td><td>16</td><td>47</td></tr><tr><td>Old</td><td>3</td><td>7</td><td>11</td><td>16</td><td>24</td><td>62</td></tr></table>

Source: HSBC estimates, previous forecasts are from our 1 April 2026 report, Global Tech Platforms: OpenAI: Back to chatbots – new HSBC forecasts

## Consequently, we update our 2030 funding gap for OAI

Despite our 2026-30e revenue estimate cut by 3%, we reduce our funding gap forecast over the period to USD77bn from USD154bn. Our new forecast comes in significantly below due to three main reasons:

◆ +USD57bn from lower projected FCF deficit: from USD278bn to USD221bn over 2026-30e.  
+USD12bn of incremental equity raise. On 27 February 2026, OAI announced a USD110bn investment at a USD730bn pre-money valuation (USD30bn from Softbank, USD30bn NVIDIA and USD50bn Amazon). This was reflected in our previous funding gap calculation. We now factor in OAI's equity round (announced after market close on 31 March) that concluded at USD122bn, including an extra USD12bn raised from multiple financial institutions. We now reflect this extra USD12bn in our forecasts.  
$\diamond$ +USD8bn from the higher AMD shares that OAI could sell when they vest. AMD's share price has increased from USD203.43 on 31 March 2026 to USD466.38 on 5 June 2026 (+129%).

Our funding gap estimate over 2026-30 is halved to USD77bn  
![](images/f68e070641966d32b55e7879df290f7e500a003b5a8f65b244a70b4e9d8385b9.jpg)

<details>
<summary>bar chart</summary>

| Category | Value (USD bn) |
| :--- | :--- |
| Old HSBC funding gap | -USD154 |
| Lower FCF deficit | +USD57 |
| Equity raise | +USD12 |
| Higher AMD share price | +USD8 |
| New HSBC funding gap | -USD77 |
</details>

Source: HSBC

## AI TAM: our new forecasts

- Increasing our 2026-30e AI industry revenue by 38%, a combination of much higher B2B and slightly lower B2C revenue estimates  
B2B industry revenue forecasts up, driven by fast adoption of Agentic AI and coding tools, but we cut B2C subscription and ad revenue  
- High LLM concentration in the West, driven by sunk costs economy; we halve our OAI 2030 funding gap forecast to USD77bn

## Global AI industry revenue revised up by +38% in 2026-30e

## Stronger B2B but lower B2C

We have seen two trends emerge since April: (1) the B2B AI market is accelerating significantly and (1) the B2C market is not growing as fast as we were expecting. See our 1 April report, Global Tech Platforms: OpenAI: Back to chatbots – new HSBC forecasts.

Anthropic runs ahead of OAI

In B2B, headlines were dominated by strong revenue growth at Anthropic, the closest OpenAI rival in B2B. Anthropic (mostly focused on B2B) announced on 6 April 2026 a revenue run rate of more than USD30bn, compared to USD9bn at end-2025. Our latest estimates for May 2026 are now USD47bn ARR for Anthropic, up from USD20bn in our previous model. OAI is more exposed to B2C than Anthropic and may have just crossed only USD30bn ARR (B2B+B2C), according to media (The Information, 26 May 2026).

In B2C, press reports were pointing at user acquisition and revenue below target at market leader OpenAI, with the WSJ quoting people familiar with subscriber figures that the company “struggled with defection rates” (28 April 2026).

Annualised B2C+B2B revenue: Anthropic vs OAI, B2B-driven acceleration  
![](images/9ccc2d0e2c3a2fc8c83d1c741348c0d7addc5ebf015c63d0a928e40a261dfaf6.jpg)

<details>
<summary>line chart</summary>

| Month   | Anthropic | OpenAI |
|---------|-----------|--------|
| Jan-25  | 1         | 6      |
| Mar-25  | 2         | 7      |
| May-25  | 3         | 9      |
| Jul-25  | 4         | 11     |
| Sep-25  | 5         | 13     |
| Nov-25  | 7         | 17     |
| Jan-26  | 10        | 21     |
| Mar-26  | 18        | 25     |
| May-26  | 47        | 30     |
</details>

Source: Company data, The Information, HSBC estimates

Anthropic and OAI's JVs can accelerate AI adoption with companies

OpenAI focuses on regaining shares in B2B vs Anthropic

Challenges in monetising high but expensive use of chatbots by consumers

AI TAM revised up: +38% in 2026-30e

Other signals have emerged that indicate further growth accelerating in B2B while B2C monetisation may prove harder than we initially expected.

OpenAI and Anthropic are both setting up joint ventures with financial partners to boost the adoption of AI within enterprises. These JVs would benefit from their engineers' exp

[中间内容因长度限制已省略]

g and Shanghai Banking Corporation Limited Singapore Branch's website at www.business.hsbc.com.sg for contact details. In Australia, this publication has been distributed by The Hongkong and Shanghai Banking Corporation Limited (ABN 65 117 925 970, AFSL 301737) for the general information of its "wholesale" customers (as defined in the Corporations Act 2001). Where distributed to retail customers, this research is distributed by HSBC Bank Australia Limited (ABN 48 006 434 162, AFSL No. 232595). These respective entities make no representations that the products or services mentioned in this document are available to persons in Australia or are necessarily suitable for any particular person or appropriate in accordance with local law. No consideration has been given to the particular investment objectives, financial situation or particular needs of any recipient.

HSBC Securities (USA) Inc. accepts responsibility for the content of this research report prepared by its non-US foreign affiliate. The information contained herein is under no circumstances to be construed as investment advice and is not tailored to the needs of the recipient. All U.S. persons receiving and/or accessing this report and wishing to effect transactions in any security discussed herein should do so with HSBC Securities (USA) Inc. in the United States and not with its non-US foreign affiliate, the issuer of this report. HSBC México, S.A., Institución de Banca Múltiple, Grupo Financiero HSBC is authorized and regulated by Secretaría de Hacienda y Crédito Público and Comisión Nacional Bancaria y de Valores (CNBV). In Brazil, this document has been distributed by Banco HSBC SA ("HSBC Brazil"), and/or its affiliates. As required by Resolution No. 20/2021 of the Securities and Exchange Commission of Brazil (Comissão de Valores Mobiliários), potential conflicts of interest concerning (i) HSBC Brazil and/or its affiliates; and (ii) the analyst(s) responsible for authoring this report are stated on the chart above labelled "HSBC & Analyst Disclosures".

If you are a customer of HSBC International Wealth & Premier Banking ("IWPB"), including HSBC Private Bank, you are eligible to receive this publication only if: (i) you have been approved to receive relevant research publications by an applicable HSBC legal entity; (ii) you have agreed to the applicable HSBC entity's terms and conditions and/or customer declaration for accessing research; and (iii) you have agreed to the terms and conditions of any other internet banking, online banking, mobile banking and/or investment services offered by that HSBC entity, through which you will access research publications (collectively with (ii), the "Terms"). If you do not meet the above eligibility requirements, please disregard this publication and, if you are a IWPB customer, please notify your Relationship Manager or call the relevant customer hotline. Distribution of this publication is the sole responsibility of the HSBC entity with whom you have agreed the Terms. Receipt of research publications is strictly subject to the Terms and any other conditions or disclaimers applicable to the provision of the publications that may be advised by IWPB. © Copyright 2026, HSBC Continental Europe, ALL RIGHTS RESERVED. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, on any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of HSBC Continental Europe.

[1280753]

## Stay connected to our topical and timely thought leadership

![](images/50aa4908b04806031f2206a1fbb008ddc37d721919f27caaf36e6f83f9e1643c.jpg)

## Download the HSBC Global Investment Research app

From Apple's App Store or Google Play The app features topical and timely curated reports, multimedia, and upcoming events

![](images/9d7fd93d352737905f70225b3b5e6a1644786df28be1e07dfc4c62e3a6ed2aee.jpg)

## Log on to the Global Investment Research website

To access all reports and videos, visit research.hsbc.com

![](images/8da8f6e04cbb10c49838f151fce5ebbba044035d9b1123fab466418adca1b6e4.jpg)

## Connect with Global Investment Research on LinkedIn

Search #HSBCResearch for free to view insights that can easily be shared with clients and prospects

![](images/39b6ac2227045fe8b4f55fed79352c93da602ab3924ac828d91ccefe160f7505.jpg)

## Subscribe and listen

Under the Banyan Tree by HSBC Global Investment Research on Apple, Spotify or YouTube

The Macro Brief by HSBC Global Investment Research on Apple, Spotify or YouTube

![](images/c727b6c0c3ab1d94f441d72b056d0446995ea15e4e12daa1fe2ce7fada951097.jpg)

## Newsletters

Subscribe to our monthly collection of free to view reports and interviews in Open Pass or read our bite-sized round up of research covering our nine key themes, Talking Points
"""
